# Findings confirmed during implementation

These extend AUDIT_BEFORE_CHANGES.md; they were recorded after the initial audit.

| ID | Severity | Confirmed defect | Resolution |
|---|---|---|---|
| A14 | HIGH | PTB drains its queue into semaphore-waiting tasks; queue depth alone cannot bound leased webhook updates. | Admission now counts durable in-flight work per worker and caps it at processor concurrency; lease duration exceeds handler deadline. Pump restart retains outstanding leases. |
| A15 | HIGH | `mark_projected_order_notification` was a no-op, despite callers relying on persistent delivery outcomes. | Normalized order stores success, attempt count and next due time; bounded retry uses existing reconciliation job. Telegram delivery cannot be exactly-once across a network ambiguity; economics remain idempotent. |
| A16 | HIGH | Incident settings forced notifications off despite critical incidents; enabling them exposed unlimited retry and unrecovered sending claims. | Critical reference-only alerts enabled; 5-attempt cap, backoff and stale-claim recovery. Raw exception details stay in logs/authorized center. |
| A17 | MEDIUM | Four async handlers directly call synchronous `register_current_user`, allowing DB waits on the event loop. | Bounded executor in VIP, account and channel-membership guards. |
| A18 | MEDIUM | Event publisher creates a Redis client without explicit cleanup/connect timeout. | Context-managed close and 2-second connect/read timeouts. |
| A19 | LOW | Fixed-amount coupons display as 0% in My Rewards. | Render actual currency amount. |
| A20 | LOW | Notification regression test depends on real wall-clock quiet hours. | Fixture disables quiet hours only for the delivery-migration test. Product quiet hours preserved. |

A03 deliberately fails before reconciliation if a dataset exceeds 100 pages. It does not silently mark work complete from a truncated snapshot; very large installations need an incremental cursor reconciliation design.
A05 checks the existing common optimistic commit used by full and section writers. Whole-store import/restore is a separate privileged boundary and must not be exposed as a user mutation API.
A07 remains open: legacy full refunds now record a durable economic-review event plus a critical incident. They do not silently claw back unrelated VIP or already-spent reward value. Normalized-order full financial refund orchestration remains a production gate.
