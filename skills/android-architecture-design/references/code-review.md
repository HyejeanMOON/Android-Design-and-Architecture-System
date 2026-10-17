# Proofreading and review

Review the change and the context needed to understand it. Load domain references for actual issues; do not turn a task into repository-wide remediation.

## Two checkpoints

- **After writing:** Reread the real diff against acceptance criteria and contracts. Check the categories below and run suitable verification. For implementation tasks, fix problems within authorization and recheck. Review-only tasks report findings or blockers without editing.
- **Before an authorized commit:** Check repository, branch, base, actual staged diff, additions/deletions, and pre-existing user edits. Before push or PR, check the final commit range. Recheck affected parts after edits, conflict resolution, or rebase; unchanged valid tests need not run again.

Do not commit, push, or install hooks without authorization. If there is no commit stage or Git is unavailable, do not claim a staged-diff review. Fix material issues within scope or disclose them. Do not delete tests, expand suppressions, or disable checks and then claim success.

| Category | Proofreading and risk |
| --- | --- |
| Typos | Names, copy, resources, comments, tests, and copy/paste residue. Do not rename published fields or storage keys for English style alone. |
| Logic | Branches, bounds, nullability, units/time, failures, races, duplicate submissions, cancellation, retries, and restoration effects. |
| Anti-patterns | UI directly accessing data sources, cyclic dependencies, global mutable state, universal Base/Store classes, empty abstractions, swallowed exceptions, and unrequested migrations. |
| Android | Lifecycle, scope, main thread, UDF, restoration, permissions/Back, and API compatibility. An architecture label difference alone is not a defect. |
| Performance | Main-thread IO/decoding, duplicate requests, recomposition effects, list/image costs, unbounded caches, and background frequency. |
| Leaks/resources | Long-lived objects retaining short-lived UI, uncleared bindings/listeners/coroutines, and cleanup missed on failure or cancellation. |
| Regression/security | Existing data, external contracts, release/R8, sensitive logs, external inputs, and missing acceptance criteria. |

## Leak evidence

Trace references from ViewModel/DI/singletons/static fields/closures to Views, bindings, or short-lived Contexts. Check Fragment View lifecycle, Compose Effect/AndroidView cleanup, and callback updates. Not every Adapter must be nulled, and local state is not inherently a leak.

Observers, receivers, Handlers, timers, and coroutines need correct owners and cancellation. Cursors, streams, players, cameras, and sensors need cleanup on exceptions and cancellation. WeakReference, Application Context, forced GC, and largeHeap are not universal fixes.

Report long-lived holder → reference chain → object that should have been released, plus trigger. Growing memory, caches, or delayed GC alone do not prove a leak. Reproduce re-entry, rotation, and reconstruction with existing Profiler/heap tools when needed. Without a device, state that only static checks were done; do not add an SDK automatically.

## Findings

Give severity, location, trigger, impact, evidence, and the smallest useful fix. Separate preferences, suspicions, and confirmed defects; do not fill a finding quota. Report actual review scope and limits. No clear findings does not guarantee zero defects. Distinguish self-review, compilation, lint, logical review, and dynamic verification.

Sources: [Kotlin style](https://developer.android.com/kotlin/style-guide), [Lifecycle](https://developer.android.com/topic/libraries/architecture/views/coroutines-views), [Memory](https://developer.android.com/topic/performance/memory/manage-app-memory). The two checkpoints are a user convention.
