# Consistency, concurrency, and weak networks

Address reads, writes, caching, or synchronization only when the task touches them. Handling a weak network does not automatically require an offline-first database or sync engine.

## Ownership and concurrency

Identify the source of truth, Repository read/write entry points, local and remote responsibilities, and how UiState is derived. Share business data through contracts rather than mutating another ViewModel. Distinguish confirmed results, in-flight requests, and optimistic state; optimistic writes need failure recovery. Isolate caches, subscriptions, and in-flight requests by session so an old result cannot enter a new account.

| Operation | Strategy to define |
| --- | --- |
| Search/filter | Cancel or reject stale results by request identity. Debounce when the interaction needs it, not by a universal duration. |
| Refresh/paging | Coalesce, queue, or ignore duplicates; reset cursors when query conditions change; avoid merging the same page twice on retry. |
| Submit/payment/delete | Guard at both UI and business entry points. Cross-process/network writes require a backend idempotency contract; a local Boolean is insufficient. |
| Multiple tables/fields | Use local transactions where atomicity matters; do not pretend HTTP and database writes share one rollback. |
| Concurrent edits | Take version/conflict detection or merge rules from the contract; do not assume last-write-wins. |

Lock only where needed and do not hold locks across network waits. A retryable `StateFlow.update` calculation must not perform external side effects. Suspending implementations must be main-safe; dispatch blocking work by type. Propagate cancellation.

Timeout or cancellation of the wait does not mean the server reversed a write. For uncertain writes, query or recover idempotently according to contract. Retry only transient errors with bounds and backoff; do not retry authentication or input failures forever. Coordinate token refresh per session.

## Offline and weak-network experience

- Distinguish first load with no data, refresh failure with existing content, stale cache, unknown submit result, and pending sync. Retain content/input and show freshness or pending state when needed. Cached data is not automatically current, and network failure is not an empty list.
- Set timeout and manual/automatic retry from interaction and business cost. A connectivity signal does not prove the service is reachable; do not decide success solely from a connectivity callback.
- Keep loaded pages when later paging fails and retry the affected page. Reconnection must not replay non-idempotent payments automatically or overwrite edits in progress.
- Only for an explicit offline requirement, design a local source of truth, durable pending queue/outbox, conflict behavior, and failure feedback with [background work](background-work.md). An online-only app still needs a clear offline failure path.
- Drafts and unsynced user writes cannot be discarded as cache. Define cache keys, capacity, invalidation, and account isolation. Do not claim exactly-once writes without a backend contract.

Verify relevant out-of-order responses, double taps, results after cancellation, timeout after successful write, offline/slow network, paging retry, reconnection, and account switch. Use controlled data sources and time; do not add a real network test for every change.

Sources: [Data layer](https://developer.android.com/topic/architecture/data-layer), [Offline-first](https://developer.android.com/topic/architecture/data-layer/offline-first), [Coroutines best practices](https://developer.android.com/kotlin/coroutines/coroutines-best-practices).
