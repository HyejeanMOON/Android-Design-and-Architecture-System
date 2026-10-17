# Technology selection and dependency maintenance

## Default choices

Order of preference: explicit user requirement → suitable existing project solution → applicable Google/AndroidX recommendation → mature, maintained third-party library. A library appearing in an official sample is not necessarily a mandatory recommendation. This table is not a stack to install wholesale.

| Capability | Default candidate and boundary |
| --- | --- |
| Language/asynchrony | Kotlin and coroutines/Flow for new code; retain Java interoperability |
| UI/state | Compose Material 3 or XML Material Components according to UI technology, with Lifecycle/ViewModel |
| REST/HTTP | Retrofit + OkHttp; raw HTTP or downloads may use OkHttp alone; evaluate non-REST protocols separately |
| JSON | Consider kotlinx.serialization for new Kotlin code; retain suitable Moshi/Gson, selecting the primary option for contracts and converters |
| Storage | Room for structured queries/transactions, DataStore for small settings; do not migrate suitable storage without cause or treat either as an encrypted credential vault |
| DI | Prefer Hilt when a framework is warranted; manual injection works for small graphs; retain suitable Koin/Dagger |
| Background/paging | Consider WorkManager for deferrable persistent work and Paging for large datasets, only when needed |
| Images | Consider Coil for new Compose images; reuse suitable Glide/Coil in XML, with network and decoder needs in mind |
| Navigation/testing | Reuse AndroidX or existing solutions fitting the current UI; do not migrate frameworks automatically |

Third-party defaults are plugin preferences. When introducing one, state the need, why existing capabilities are insufficient, maintainer, license, and compatibility. Do not create an ADR for every library. Reuse the version catalog or centralized dependency management and applicable BOMs; avoid dynamic versions or duplicate management systems.

Keep network configuration inside the data boundary. Reuse clients/loaders with suitable scope, without forcing separate security domains to share instances. Do not wrap every library in a universal interface.

## Upgrades and deprecated APIs

Start maintenance when an upgrade, known risk, policy deadline, or deprecated API actually blocks the task. Enabling the skill does not trigger a repository-wide upgrade.

1. Record current direct and transitive versions; check maintainer release notes, migration notes, known risks, and relevant official compatibility tables. Mark missing information unverified; do not invent latest stable versions or vulnerability conclusions.
2. Check affected AGP/Gradle/JDK, Kotlin/Compose compiler/KSP, SDK/NDK, and library combinations. These are investigation points, not a requirement to upgrade everything. Use mechanisms for the actual target version rather than copying obsolete plugin configuration.
3. Choose the smallest maintainable combination that addresses the need or risk. Neither pin obsolete versions indefinitely nor chase every release. Complete necessary authorized compatibility work; recommend optional major migrations without widening scope.
4. Check that replacement APIs preserve behavior on supported systems; retain compatibility paths when needed. Silencing a warning must not change semantics. Verify compilation/lint, key behavior, applicable release builds, and migrations. Update the real lockfile/catalog; do not hide conflicts by forcing transitive versions blindly.
5. Record breaking changes, rollback conditions, and remaining issues. Use [data migrations](data-migrations.md) for persistent formats; rolling back a dependency does not roll back user data.

Sources: [Upgrade strategies](https://developer.android.com/build/version-upgrade-strategies), [AGP](https://developer.android.com/build/releases/about-agp), [Hilt](https://developer.android.com/training/dependency-injection/hilt-android), [Data layer](https://developer.android.com/topic/architecture/data-layer), [Retrofit](https://github.com/lysine-dev/retrofit), [OkHttp](https://github.com/lysine-dev/okhttp), [Serialization](https://kotlinlang.org/docs/serialization.html), [Coil](https://coil-kt.github.io/coil/).
