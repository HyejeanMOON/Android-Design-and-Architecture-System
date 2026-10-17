# Background work and process lifetime

Read when work must continue after leaving a screen, when uploading/syncing/scheduling, or when process restoration matters. A background thread is not the same as durable work.

| Work need | Consider first |
| --- | --- |
| Subscription/animation while UI is visible | UI/View lifecycle; cancel when leaving. |
| Screen business request that survives configuration change | ViewModel scope; it does not automatically recover after process death. |
| Cross-screen work while the app process lives | Injected app scope with ownership, cancellation, and error handling; avoid GlobalScope by default. |
| Deferrable work requiring persistent scheduling | WorkManager with defined constraints, retries, and business identity. |
| Exact timing or user-visible ongoing work | Evaluate Alarm, foreground service, or other specialized APIs under current guidance, permissions, quotas, and Play eligibility. Do not put everything in a Worker. |

WorkManager supports persistent scheduling but does not guarantee exact timing, unlimited execution, or exactly-once execution. Quotas, Doze, constraints, and force-stop matter. Do not promise execution at a precise time after force-stop or conflate removing a task, process death, and force-stop.

- Use business identity and suitable unique work/replacement policy to control duplicate scheduling. Scope names by account/tenant. Choose KEEP, REPLACE, and other policies by actual meaning, not one universal rule.
- Workers must not retain a View/Activity. Pass small IDs; persist payload and progress when needed rather than relying on in-memory singletons. Retry/restart can re-enter work, so writes need contract-based idempotency.
- Cooperate with stop/cancellation and release resources. Handle account-specific work and credentials on logout; old work must not continue under a new identity.
- Set network/charging constraints by need. Retry transient errors with backoff, not authorization or validation failures forever. Expose outcomes to UI through Repository state rather than manipulating UI from a Worker.
- Verify duplicate enqueue, constraints absent/restored, process recreation, cancellation, and account switching. Check target-OS restrictions for affected permissions/APIs. List unrun scenarios honestly; do not evade system restrictions with an endless foreground service.

Sources: [Choosing background tasks](https://developer.android.com/develop/background-work/background-tasks), [Persistent work](https://developer.android.com/develop/background-work/background-tasks/persistent), [Managing work](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/manage-work).
