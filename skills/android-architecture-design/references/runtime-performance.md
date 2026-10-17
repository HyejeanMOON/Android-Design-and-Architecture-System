# Runtime performance and diagnosis

Use this for performance/crash investigations or changes touching known hotspots. See [build performance](build-performance.md) for build time.

## Measure and optimize

Define the user path and metrics: cold/warm/hot startup, first interaction/full display, frame time, peak memory, retained objects after re-entry, and power. Record device/OS, variant, data/network, compilation state, and repetitions. Recheck important conclusions on real devices with production-like artifacts; state emulator limitations.

Choose Profiler, Trace, Perfetto, or Macrobenchmark for the hotspot; use Microbenchmark for fine-grained computation. Verify Baseline Profiles are packaged, active, and beneficial. Do not create a benchmark module for every small change.

| Hotspot | Inspect first |
| --- | --- |
| Startup/main thread | Application/Provider/DI initialization, synchronous IO, decoding, locks, and repeated computation. Dispatch by work type; do not send all work to the IO pool. |
| Compose/Views | State read scope, Effect keys, item identity, expensive computation, repeated binding/layout. Do not blanket-add remember or stability annotations or replace widgets. |
| Images/lists | Decode at display size, reuse loaders, bound and invalidate caches, page when useful. Avoid unbounded caches. |
| Memory/power | Lifecycle reference chains, resource cleanup, repeated work, and background frequency. Do not force GC or mask problems with permanent polling. |

Define cache keys, bounds, invalidation, and account isolation. Compare measurements under similar conditions and report variance and resource cost, not only the fastest run. Without measurement, call an optimization a candidate. For leak evidence, see [code review](code-review.md).

## Observability and diagnosis

Prefer existing logs, crash tools, and Android vitals. Do not automatically add a monitoring SDK or ongoing monitoring. For an incident, record redacted reproduction details, app version/variant, device/OS, phase, and stack trace. Use mapping/native symbols from the same release for obfuscated/JNI traces.

Use stable error categories, operation names, and necessary nonsensitive correlation IDs while preserving causes and exception chains. Do not log tokens, passwords, full responses, or personal data or use raw user IDs as tracing IDs. Set sampling, rate limits, uploads, and retention for actual diagnostic needs and privacy constraints; do not log every frame or add automatic collection.

Distinguish crashes, ANRs, cancellation, expected business errors, and process death. No telemetry does not prove no problem; tools with different denominators cannot be compared directly. Identify affected versions/devices and trigger chains before a minimal fix and verification. Ongoing alerts, rollout, and external uploads need existing authorization; diagnosis does not widen operational scope.

Sources: [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview), [Compose performance](https://developer.android.com/develop/ui/compose/performance/bestpractices), [Baseline Profile measurement](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile), [Android vitals](https://developer.android.com/google/play/vitals), [Log disclosure risks](https://developer.android.com/privacy-and-security/risks/log-info-disclosure).
