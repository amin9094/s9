# بررسی پیش از اصلاح نسخه 8.40

۱۲۴۵ آزمون قبلی و کنترل کیفیت واقعی نسخهٔ candidate گذشتند. آزمون‌ها به‌تنهایی خطاهای زیر را پوشش نمی‌دادند.

- **841-01 — CRITICAL**: BaseException in pooled transaction reaches __exit__(None,None,None), permitting partial commit instead of rollback. (`core/storage/engine.py`)
- **841-02 — HIGH**: Synchronous DB access in auth/csrf/bootstrap/session and synchronous Redis rate limiting run on the HTTP event loop. (`core/miniapp_server.py`)
- **841-03 — HIGH**: Recovery calls record_error/persist synchronously before exit, so a blocked metrics lock/filesystem can block recovery. Stop clears a shared event even when old thread is still alive. (`core/runtime_watchdog.py`)
- **841-04 — HIGH**: Concurrent lazy Redis creation has no async guard; losing candidate clients are not closed on ping failure/cancellation. (`core/distributed_jobs.py`)
- **841-05 — HIGH**: New unique keys can exceed the stated 20,000 entry cap; concurrent lazy clients can leak sockets. (`core/rate_limit.py`)
- **841-06 — HIGH**: A fresh coverage timestamp can be reused after a failed instrumented run without rerunning tests. (`scripts/finalize_quality_proof.py`)
- **841-07 — MEDIUM**: Polling startup explicitly requests infinite bootstrap retries. (`bot_runtime/runtime_jobs.py`)
- **841-08 — MEDIUM**: Configured stream rotation may outlive connection TTL; access/session is captured once per stream. (`core/miniapp_server.py`)
- **841-09 — MEDIUM**: SQLite setup errors after connect do not close the created connection. (`core/storage/engine.py;core/db.py;core/persistence.py`)
- **841-10 — MEDIUM**: Three different critical target sets produce inconsistent release coverage evidence. (`scripts/quality_gate.py;scripts/coverage_gate_worker.py;scripts/assemble_candidate_proof.py`)
- **841-11 — LOW**: Two risk response keys occur twice and earlier values are silently overwritten. (`services/miniapp_read_service_v2.py`)
- **841-12 — MEDIUM**: S3 backup verification uses SDK default timeouts/retries without a bounded explicit configuration. (`scripts/predeploy_migrate.py`)
- **841-13 — LOW**: Offline build check leaves POSTGRES_URL/REDIS_URL and external provider variables enabled. (`main.py`)

هشدارهای تحلیل ایستا جدا از باگ‌های تأییدشده ثبت شده‌اند؛ استقرار زنده در این محیط در دسترس نیست.
