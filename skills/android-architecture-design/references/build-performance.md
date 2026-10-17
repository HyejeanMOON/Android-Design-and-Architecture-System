# Gradle build performance

Optimize the target app build only; do not add Gradle to this plugin repository. See [runtime performance](runtime-performance.md) for app behavior. First record the actual Wrapper/AGP/Kotlin/JDK, relevant plugins, and local/CI CPU, memory, and container limits.

Use existing analysis or local `--profile` to distinguish download, configuration, generation, compilation, and packaging bottlenecks. Compare cold, no-change, and localized implementation/API changes as needed. Keep variants, data, caches, and machine conditions comparable; do not clear caches by default.

| Candidate | Condition and validation |
| --- | --- |
| `org.gradle.parallel=true` | One Gradle invocation may schedule independent modules together; dependencies remain serial. Do not delete dependency edges or run processes against the same output directory. |
| `org.gradle.workers.max` | Size for effective CPU and total memory, not a fixed high worker count; check shared output and resource contention. |
| `org.gradle.jvmargs` / `-Xmx` | Increase only with GC/OOM evidence and available capacity. Preserve other arguments and budget Kotlin daemon, workers, IDE, and emulator together; no universal heap size. |
| `org.gradle.caching=true` | Verify actual `FROM-CACHE` output; it differs from `UP-TO-DATE`. |
| `org.gradle.configuration-cache=true` | Try after checking Wrapper/AGP/plugin compatibility and confirm configuration reuse. Do not ignore problems and claim success. |
| Incremental compilation | Preserve applicable defaults, diagnose invalidation, and verify a local change. Do not accumulate obsolete properties. |
| KSP/kapt | Prefer KSP for compatible new processors; evaluate existing migrations separately. Incrementality depends on actual processors. |

Custom tasks must declare inputs, outputs, and dependencies correctly. Avoid configuration-time IO and eager evaluation; do not falsely mark tasks cacheable. Avoid routine `clean`, `--rerun-tasks`, and `--refresh-dependencies` except for diagnosis. Do not use obsolete `android.enableBuildCache` or unverified experimental flags, or disable required tests/lint for speed.

Change project configuration rather than global user settings by default; consider local and CI separately. Remote caches and Build Scan uploads need existing authorization for external actions. Change a few factors at a time, compare results, and verify artifacts/relevant tests. Revert regressions; use a clean build when needed to rule out stale dependencies. Without measurements, describe a configuration as proposed, not a proven speedup.

Sources: [Android build optimization](https://developer.android.com/build/optimize-your-build), [Gradle performance](https://docs.gradle.org/current/userguide/performance.html), [Incremental tasks](https://docs.gradle.org/current/userguide/incremental_build.html), [Kotlin compilation](https://kotlinlang.org/docs/gradle-compilation-and-caches.html). Check the target versions.
