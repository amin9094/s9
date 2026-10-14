#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import stat
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent
BUNDLE_SHA256 = "acfb5046a03ff9ddc53596def96ebeafa325795e971a4f4130133457d2098ba6"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_member(name: str) -> PurePosixPath:
    clean = name.replace("\\", "/")
    relative = PurePosixPath(clean)
    if relative.is_absolute() or not relative.parts or any(part in {"", ".", ".."} for part in relative.parts):
        raise RuntimeError(f"unsafe runtime member: {name!r}")
    return relative


def is_symlink(info: zipfile.ZipInfo) -> bool:
    mode = (info.external_attr >> 16) & 0xFFFF
    return stat.S_ISLNK(mode)


REQUIRED_RUNTIME_FILES = (
    "main.py",
    "bot.py",
    "config.py",
    "requirements.txt",
    "VERSION",
    "data/database.json",
    "bot_runtime/__init__.py",
    "bot_runtime/shared.py",
    "core/__init__.py",
    "core/db.py",
    "core/miniapp_server.py",
    "modules/__init__.py",
    "modules/prices.py",
    "modules/portfolio.py",
    "services/__init__.py",
    "repositories/__init__.py",
    "handlers/__init__.py",
    "jobs/__init__.py",
    "ui/__init__.py",
    "scripts/docker-entrypoint.sh",
    "scripts/healthcheck.py",
    "webapp/index.html",
)

# Railway users sometimes upload the project through GitHub's browser UI. That
# flow can silently omit a large directory such as tests/. The quality image
# must be able to reconstruct every input required by pytest and the release
# gate from the signed fallback bundle before installing development tools.
REQUIRED_QUALITY_FILES = (
    "requirements.lock.txt",
    "requirements-dev.lock.txt",
    "requirements-dev.txt",
    "pyproject.toml",
    "pytest.ini",
    "scripts/quality_gate.py",
    "scripts/check_miniapp_js.js",
    "scripts/release_gate.py",
    "tests/conftest.py",
)

# Source directories reconstructed from the signed runtime bundle during the
# Docker quality stage. Browser-based GitHub uploads can leave stale files from
# an older release in the repository; merely restoring missing files is not
# enough in that situation. Canonicalization removes these managed trees and
# recreates them from the verified bundle before pytest runs. Persistent data is
# deliberately excluded.
CANONICAL_QUALITY_DIRS = (
    "assets",
    "bot_runtime",
    "core",
    "handlers",
    "jobs",
    "modules",
    "nginx",
    "repositories",
    "scripts",
    "services",
    "systemd",
    "tests",
    "ui",
    "webapp",
)


def missing_runtime_files(destination: Path) -> list[str]:
    root = destination.resolve()
    return [name for name in REQUIRED_RUNTIME_FILES if not (root / name).is_file()]


def _archive_members(bundle: Path) -> tuple[set[str], list[str]]:
    with zipfile.ZipFile(bundle) as archive:
        broken = archive.testzip()
        if broken:
            raise RuntimeError(f"runtime archive is corrupt at {broken}")
        members = {safe_member(info.filename).as_posix() for info in archive.infolist() if not info.is_dir()}
    tests = sorted(name for name in members if name.startswith("tests/test_") and name.endswith(".py"))
    return members, tests


def verify_bundle(bundle: Path, *, profile: str = "runtime") -> str:
    if not bundle.is_file():
        raise FileNotFoundError(bundle)
    expected = BUNDLE_SHA256.strip().lower()
    if len(expected) != 64 or any(char not in "0123456789abcdef" for char in expected):
        raise RuntimeError("embedded runtime checksum is not finalized")
    actual = sha256(bundle)
    if actual != expected:
        raise RuntimeError(f"runtime checksum mismatch: expected {expected}, got {actual}")
    members, test_members = _archive_members(bundle)
    required = list(REQUIRED_RUNTIME_FILES)
    if profile == "quality":
        required.extend(REQUIRED_QUALITY_FILES)
        if not test_members:
            raise RuntimeError("runtime archive is incomplete; no pytest test modules are bundled")
    elif profile != "runtime":
        raise ValueError(f"unknown restore profile: {profile}")
    missing_members = [name for name in required if name not in members]
    if missing_members:
        raise RuntimeError("runtime archive is incomplete; missing: " + ", ".join(missing_members))
    return actual


def _quality_missing(destination: Path, bundle: Path) -> list[str]:
    root = destination.resolve()
    members, test_members = _archive_members(bundle)
    missing = [name for name in REQUIRED_QUALITY_FILES if not (root / name).is_file()]
    # Compare against the signed bundle rather than checking only that tests/
    # exists. This also repairs a partially uploaded suite.
    missing.extend(name for name in test_members if name in members and not (root / name).is_file())
    return sorted(set(missing))


def verify_extracted_bundle(bundle: Path, destination: Path) -> int:
    """Verify every extracted file byte-for-byte against the signed bundle.

    The Railway image is intentionally reconstructed from the archive in a
    clean directory. This final comparison prevents a partial extraction, an
    overwritten source file, or a mixed browser upload from reaching pytest.
    """
    root = destination.resolve()
    checked = 0
    with zipfile.ZipFile(bundle) as archive:
        for info in archive.infolist():
            if info.is_dir():
                continue
            relative = safe_member(info.filename)
            target = (root / Path(*relative.parts)).resolve()
            try:
                target.relative_to(root)
            except ValueError as exc:
                raise RuntimeError(f"runtime member escapes destination: {info.filename}") from exc
            if not target.is_file():
                raise RuntimeError(f"extracted runtime file is missing: {relative.as_posix()}")
            expected = hashlib.sha256()
            with archive.open(info, "r") as source:
                for chunk in iter(lambda: source.read(1024 * 1024), b""):
                    expected.update(chunk)
            if sha256(target) != expected.hexdigest():
                raise RuntimeError(f"extracted runtime file differs from signed bundle: {relative.as_posix()}")
            checked += 1
    if checked <= 0:
        raise RuntimeError("signed runtime bundle contains no files")
    return checked


def ensure_runtime(destination: Path | str = ROOT, bundle: Path | str | None = None) -> dict[str, object]:
    """Restore missing runtime files from the signed fallback bundle."""
    root = Path(destination).resolve()
    archive = Path(bundle).resolve() if bundle is not None else root / "sentinel_runtime.zip"
    missing_before = missing_runtime_files(root)
    restored = {"restored": 0, "skipped_existing": 0, "directories": 0}
    bundle_sha256: str | None = None
    if archive.is_file():
        bundle_sha256 = verify_bundle(archive, profile="runtime")
    if missing_before:
        if not archive.is_file():
            raise RuntimeError(
                "runtime source tree is incomplete and sentinel_runtime.zip is unavailable; missing: "
                + ", ".join(missing_before)
            )
        restored = restore(archive, root)
    missing_after = missing_runtime_files(root)
    if missing_after:
        raise RuntimeError("runtime restoration did not produce required files: " + ", ".join(missing_after))
    return {
        **restored,
        "missing_before": missing_before,
        "missing_after": missing_after,
        "bundle_sha256": bundle_sha256,
        "profile": "runtime",
    }


def ensure_quality(destination: Path | str = ROOT, bundle: Path | str | None = None) -> dict[str, object]:
    """Restore all quality-gate inputs, including a complete pytest suite."""
    root = Path(destination).resolve()
    archive = Path(bundle).resolve() if bundle is not None else root / "sentinel_runtime.zip"
    if not archive.is_file():
        raise RuntimeError("quality source recovery requires sentinel_runtime.zip")
    bundle_sha256 = verify_bundle(archive, profile="quality")
    missing_before = sorted(set(missing_runtime_files(root) + _quality_missing(root, archive)))
    restored = {"restored": 0, "skipped_existing": 0, "directories": 0}
    if missing_before:
        restored = restore(archive, root)
    missing_after = sorted(set(missing_runtime_files(root) + _quality_missing(root, archive)))
    if missing_after:
        raise RuntimeError("quality restoration did not produce required files: " + ", ".join(missing_after))
    discovered_test_files = len(list((root / "tests").glob("test_*.py")))
    if discovered_test_files <= 0:
        raise RuntimeError("quality restoration produced no pytest test modules")
    return {
        **restored,
        "missing_before": missing_before,
        "missing_after": missing_after,
        "bundle_sha256": bundle_sha256,
        "profile": "quality",
        "test_files": discovered_test_files,
    }


def restore(bundle: Path, destination: Path, *, overwrite: bool = False) -> dict[str, int]:
    verify_bundle(bundle, profile="runtime")
    destination = destination.resolve()
    restored = skipped = directories = overwritten = 0
    with zipfile.ZipFile(bundle) as archive:
        for info in archive.infolist():
            relative = safe_member(info.filename)
            if is_symlink(info):
                raise RuntimeError(f"runtime symlink is forbidden: {info.filename}")
            target = (destination / Path(*relative.parts)).resolve()
            try:
                target.relative_to(destination)
            except ValueError as exc:
                raise RuntimeError(f"runtime member escapes destination: {info.filename}") from exc
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                directories += 1
                continue
            if target.exists() and not overwrite:
                skipped += 1
                continue
            existed = target.exists()
            target.parent.mkdir(parents=True, exist_ok=True)
            fd, temporary_name = tempfile.mkstemp(prefix=f".{target.name}.", suffix=".restore", dir=target.parent)
            try:
                with os.fdopen(fd, "wb") as output, archive.open(info, "r") as source:
                    while chunk := source.read(1024 * 1024):
                        output.write(chunk)
                    output.flush()
                    os.fsync(output.fileno())
                mode = (info.external_attr >> 16) & 0o777
                os.chmod(temporary_name, mode or 0o644)
                os.replace(temporary_name, target)
            finally:
                try:
                    os.unlink(temporary_name)
                except FileNotFoundError:
                    pass
            restored += 1
            overwritten += int(existed)
    return {
        "restored": restored,
        "skipped_existing": skipped,
        "directories": directories,
        "overwritten": overwritten,
    }


def canonicalize_quality(destination: Path | str = ROOT, bundle: Path | str | None = None) -> dict[str, object]:
    """Make the Docker quality tree exactly match the signed source bundle.

    This is intentionally stronger than ``ensure_quality``. It fixes mixed
    GitHub uploads where new tests coexist with stale implementation files from
    a previous release, which otherwise produces deterministic test failures.
    """
    root = Path(destination).resolve()
    archive = Path(bundle).resolve() if bundle is not None else root / "sentinel_runtime.zip"
    bundle_sha256 = verify_bundle(archive, profile="quality")
    members, test_members = _archive_members(archive)
    top_level_directories = {name.split("/", 1)[0] for name in members if "/" in name}
    removed_directories: list[str] = []
    for name in CANONICAL_QUALITY_DIRS:
        if name not in top_level_directories:
            continue
        target = root / name
        if target.is_symlink():
            raise RuntimeError(f"canonical source directory must not be a symlink: {name}")
        if target.exists():
            shutil.rmtree(target)
            removed_directories.append(name)
    restored = restore(archive, root, overwrite=True)
    missing_after = sorted(set(missing_runtime_files(root) + _quality_missing(root, archive)))
    if missing_after:
        raise RuntimeError("quality canonicalization did not produce required files: " + ", ".join(missing_after))
    discovered_test_files = len(list((root / "tests").glob("test_*.py")))
    if discovered_test_files != len(test_members):
        raise RuntimeError(
            "quality canonicalization test parity mismatch: "
            f"archive={len(test_members)} tree={discovered_test_files}"
        )
    verified_files = verify_extracted_bundle(archive, root)
    return {
        **restored,
        "missing_before": [],
        "missing_after": missing_after,
        "bundle_sha256": bundle_sha256,
        "profile": "canonical_quality",
        "test_files": discovered_test_files,
        "verified_files": verified_files,
        "removed_directories": removed_directories,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Restore missing SENTINEL files from the signed fallback bundle")
    parser.add_argument("--bundle", type=Path, default=ROOT / "sentinel_runtime.zip")
    parser.add_argument("--destination", type=Path, default=ROOT)
    parser.add_argument("--ensure", action="store_true", help="restore only when required files are missing")
    parser.add_argument(
        "--canonicalize-quality",
        action="store_true",
        help="replace stale managed source/test trees from the signed bundle before the quality gate",
    )
    parser.add_argument("--profile", choices=("runtime", "quality"), default="runtime")
    args = parser.parse_args()
    if args.canonicalize_quality:
        if args.profile != "quality":
            parser.error("--canonicalize-quality requires --profile quality")
        result = canonicalize_quality(args.destination.resolve(), args.bundle.resolve())
    elif args.ensure:
        result = (
            ensure_quality(args.destination.resolve(), args.bundle.resolve())
            if args.profile == "quality"
            else ensure_runtime(args.destination.resolve(), args.bundle.resolve())
        )
    else:
        result = restore(args.bundle.resolve(), args.destination.resolve())
    print(
        "RUNTIME RESTORE OK: "
        f"profile={result.get('profile', args.profile)} "
        f"restored={result['restored']} skipped_existing={result['skipped_existing']} "
        f"directories={result['directories']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
