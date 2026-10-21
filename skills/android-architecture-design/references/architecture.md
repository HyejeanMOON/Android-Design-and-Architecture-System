# Layers and state

Google recommends UI and data layers with unidirectional data flow; a domain layer is optional. Its typical domain-to-data dependency and this plugin's Clean dependency inversion are different, valid choices. Use the project's established boundary or the smallest suitable new one; neither direction is Google's mandatory Clean layout. Limit changes to legacy projects through the shared workflow.

```text
Official typical class dependency: UI → [domain] → data → data source
Plugin Clean compile-time option, when justified: presentation → domain contracts ← data implementation; app assembles them
Runtime in either option: UI → ViewModel → [UseCase] → Repository → DataSource
State: trusted data → screen state → UI; actions return to the state owner
```

- Data owns application data, source-of-truth coordination, and most data business logic. Each Repository is the entry point for its data; UI and ViewModel do not directly access DAOs, HTTP, or DataStore. Identify the authoritative source and make Repository/data-source calls main-safe. Map models where semantics differ; do not expose internal DTOs as public business contracts. See [data consistency](data-consistency.md) when reads, writes, or caching are involved.
- Add domain UseCases for complex or reused logic, not to forward every Repository method. In the official-style dependency, they may depend on data-layer Repositories; in the plugin's Clean option, the domain owns stable Repository contracts implemented by data. Keep domain business models and contracts independent of UI, Context, Room entities, and network DTOs. Coroutines and Flow may be used where the contract calls for them.
- Presentation exposes read-only state and business actions. The UI handles platform permissions, windows, and navigation execution. The app reuses existing DI or manual assembly; apply [DI and Hilt guidance](dependency-injection.md) when changing that graph.
- For screens with meaningful state transitions, distinguish incoming ActionState, renderable UiState, and optional acknowledged EventState. Reduce results into immutable UiState; see [state-reducer.md](state-reducer.md). These names and reducer shape are plugin conventions, not separate mandatory layers or three independent state streams.
- A small feature may separate packages and contracts in one module, with a ViewModel calling a Repository directly. Do not create empty UseCases. Do not refactor an existing sound layered layout solely because directories differ.
- Put state with the appropriate owner. Local expansion, focus, and animation need not all enter a ViewModel. Choose subscription strategies by cost. Save only suitable small inputs or IDs for restoration; persist business data separately. Surviving configuration changes is not process-death recovery.
- A ViewModel must not retain a View, Activity, binding, NavController, or short-lived Context. The UI can navigate for purely visual events. Represent important business results as state before the UI navigates, with defined return and re-entry behavior.
- Do not rely only on lossy Channel, SharedFlow, or SingleLiveEvent delivery for critical results. Acknowledged state can represent transient messages; do not promise exactly-once delivery by default.

Load concurrency, background, or module details only when relevant. Sources: [Architecture guide](https://developer.android.com/topic/architecture), [Architecture recommendations](https://developer.android.com/topic/architecture/recommendations), [Domain layer](https://developer.android.com/topic/architecture/domain-layer), [Data layer](https://developer.android.com/topic/architecture/data-layer), [UI events](https://developer.android.com/topic/architecture/ui-layer/events), [Saved state](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate).
