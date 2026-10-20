# Sources and verification boundaries

Domain documents link direct sources. This page explains how to interpret them. Links do not require querying everything on every task. For new APIs/dependencies, versions, system behavior, policies, or uncertain facts, check the relevant current official material.

| Topic | Preferred source |
| --- | --- |
| Android architecture, components, interoperability, toolchain | [Android Developers](https://developer.android.com/), using release and migration guidance matching the target project's versions |
| UI/UX | [Material 3](https://m3.material.io/foundations), together with actual XML/Compose component capabilities |
| Gradle/Kotlin | Official [Gradle](https://docs.gradle.org/current/userguide/performance.html) and [Kotlin](https://kotlinlang.org/docs/gradle-compilation-and-caches.html) material; a "current" page does not prove compatibility with an older version |
| Third-party libraries | Current maintainer releases, repositories, and migrations; a URL redirect does not automatically change Maven coordinates |
| Play | [Policy Help](https://support.google.com/googleplay/android-developer/), [target requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en), and actual Console evidence, scoped to submission date and app |

XML MVVM, independent Compose MVI, strict Clean, the Retrofit/OkHttp default, and two Review checkpoints are user/plugin conventions, not Google mandates. Distinguish recommendations, system behavior, store policy, and project preferences.
The ActionState/UiState/EventState naming and reducer structure are also plugin conventions. Android documents unidirectional state production and UI events; library examples demonstrate reducer implementations without requiring those dependencies.

Mark facts that cannot be checked as unknown. Do not invent versions, vulnerabilities, or eligibility. Old snapshots and blogs are not proof of current release requirements. Author maintenance/evaluation does not automatically become part of every app task.
