# SENTINEL — audit before this change set

Date: 2026-10-03. Input archive SHA256: `40fd8c535dd740cac0935669f5bf46e2740b805908645141938a39de582e6735`.
This report was written before changing application code. Findings are source-confirmed unless labelled unverified. An exhaustive absence-of-bugs claim is not made. Previous candidate already includes extensive hardening; preserve it.

## Confirmed findings

| ID | Severity | Evidence / consequence | Planned response |
| --- | --- | --- | --- |
| A01 | CRITICAL | `runtime_jobs._run_unified_webhook` starts the durable update pump without supervising its completion. `claim_pending`/`backlog` DB failures escape the pump, while the parent waits only for stop_event. HTTP and heartbeat can remain healthy while delivery stops. | Supervise pump lifecycle, bounded restart/backoff, failed readiness, incidents, fail process for platform recovery after exhausted budget. |
| A02 | HIGH | `telegram_bootstrap.initialize_with_retry` and setWebhook setup retry indefinitely; bootstrap initialize lacks an overall deadline. | Bounded attempts and call deadlines, stop-aware backoff. |
| A03 | HIGH | `services/experience_state.py` three pagination loops have no page/cursor guards. Repeated cursor or large datasets can occupy a blocking worker indefinitely. | Bounded pages and repeated-cursor detection; never reconcile truncated pages as complete. |
| A04 | HIGH | `_finish_approved_order` catches reward projection failure without durable retry state. An approved payment can permanently miss rewards until manually approved again. | Persistent reconciliation marker in the authoritative order, bounded retry job. |
| A05 | HIGH | Canonical reward ledgers enforce new event uniqueness but old point rows can be altered/deleted without checking old SQL evidence; economic-event deletion is also unchecked. | Enforce append-only integrity with documented privacy compatibility. |
| A06 | HIGH | Newly attributed accounts immediately qualify for signup points and referral_join missions; no maturity delay or review workflow. Telegram ID uniqueness does not prove unique people. | Delay new qualification, detect bursts, restricted fraud review; preserve original attribution. |
| A07 | HIGH | Full refund restoration reverses coupon/affiliate usage but not all derived points/VIP/milestone rewards. | Trace reversible sources; avoid silently subtracting unrelated purchased VIP; document any unresolved clawback scope. |
| A08 | MEDIUM | Requested `/health`, `/status`, `/errors`, `/system` are absent from command registry although HTTP health and Incident Center exist. | Reuse existing monitoring with permission checks and redacted details. |
| A09 | MEDIUM | `_clear_current_operation` clears user_data; persistent ConversationHandler state has no common inactivity expiration. | Common session timeout and conversation cleanup, preserving saved DB drafts. |
| A10 | MEDIUM | `require_admin_all` executes potentially blocking permission reads directly on event loop. | Move authorization reads through bounded blocking executor. |
| A11 | MEDIUM | `ResilientBot.answer_callback_query` handles network/expired callbacks but not RetryAfter; cosmetic ack can abort the actual action. | Treat throttled acknowledgement as unavailable; do not retry economic actions. |
| A12 | MEDIUM | Deleted signals renumber canonical and normalized lists, but already published Telegram posts and rendered image numbers remain historical. | Preserve immutable IDs; explicitly describe external-message limitation. |
| A13 | MEDIUM | Two concurrent approvals by the same actor may share an approving claim. Finalization is idempotent but invite preparation can duplicate. | Review claim ownership and recovery; regression coverage for concurrent approval. |

## Inspected areas / current safeguards

- Telegram: PTB 22.8 pinned; `NetworkError` correctly imported from `telegram.error`. `KeyedUpdateProcessor` inherits `BaseUpdateProcessor.process_update`; the name difference alone is NOT a confirmed bug. Add interface regression tests rather than a second dispatcher.
- Update concurrency: user-key serialization, bounded wait/handler deadline, finally release, update persistence/replay, global error handler and watchdog already exist. Audit cancellation paths rather than replacing these.
- DB/Redis: bounded pools, connection checks, transactions/rollback, statement and lock timeouts, distributed TTL/ownership, reconnect, normalized migrations already present. PostgreSQL/Redis live acceptance unavailable in this environment.
- Authentication/API/Mini App: initData HMAC/age/duplicate-field guards, sessions, origin/CSRF controls, upload and permission tests exist. Re-run security contracts and scan modified code.
- Payments/VIP/coupons/gifts/points/rewards/contests/missions: existing transaction and source-ID protections; critical remaining boundaries above. Monetary amounts must remain server-authoritative.
- Navigation: centralized deterministic parent callbacks and fallback Home already exist; static route audit and dynamic regression suite will run. No claim that static audit proves every dynamic callback.
- Signals: public number separate from immutable ID, deletion tombstones and normalized deletion, journal references, VIP authorization, album tests. Do not decrement primary keys.
- Education: built-in bot guide already removed, admin publishing/drafts/scheduling and media permissions exist.
- Tickets: existing server-built payment/signal/VIP/referral context and access controls; test rather than duplicate.
- Journal/risk/MT5/AI/providers/notifications: inspect dependency boundaries and run existing contracts; real brokers and provider credentials unavailable.
- Deployment: release candidate gates and reproducible runtime packaging exist. Docker digest, MT5 compile, live service/browser and hour-long production soak are not previously verified.

## Validation plan

Fault injection for pump crash/recovery/exhaustion, initialization limits, pagination loops, payment retry, ledger tampering, referral maturity/review, session cleanup and admin commands; full existing suite, import/build/static callback checks, release gate and restored runtime tests. Final report must distinguish confirmed fixes, tested safeguards and remaining production gates.
