# Layers and state

Google recommends UI and data layers with unidirectional data flow; a domain layer is optional. This plugin's Clean dependency inversion is a default convention, not Google's only official layout. Limit changes to legacy projects through the shared workflow.

```text
Compile time, when a separate business boundary exists: presentation → domain ← data; app assembles them
Runtime: UI → ViewModel → [UseCase] → Repository contract → implementation → DataSource
State: trusted data → screen state → UI; actions return to the state owner
```

- Domain contains pure Kotlin business models, necessary contracts, and valuable UseCases. It does not depend on UI, Context, Room entities, or network DTOs. Coroutines and Flow may be used where the contract calls for them.
- Data encapsulates sources and consistency. UI and ViewModel do not directly access DAOs, HTTP, or DataStore. Map models where semantics differ; do not expose internal DTOs as public business contracts.
- Presentation exposes read-only state and business actions. The UI handles platform permissions, windows, and navigation execution. The app reuses existing DI or manual assembly; apply [DI and Hilt guidance](dependency-injection.md) when changing that graph.
- For screens with meaningful state transitions, distinguish incoming ActionState, renderable UiState, and optional acknowledged EventState. Reduce results into immutable UiState; see [state-reducer.md](state-reducer.md). These names and reducer shape are plugin conventions, not separate mandatory layers or three independent state streams.
- A small feature may separate packages and contracts in one module, with a ViewModel calling a Repository directly. Do not create empty UseCases. Do not refactor an existing sound layered layout solely because directories differ.
- Put state with the appropriate owner. Local expansion, focus, and animation need not all enter a ViewModel. Choose subscription strategies by cost. Save only suitable small inputs or IDs for restoration; persist business data separately. Surviving configuration changes is not process-death recovery.
- A ViewModel must not retain a View, Activity, binding, NavController, or short-lived Context. The UI can navigate for purely visual events. Represent important business results as state before the UI navigates, with defined return and re-entry behavior.
- Do not rely only on lossy Channel, SharedFlow, or SingleLiveEvent delivery for critical results. Acknowledged state can represent transient messages; do not promise exactly-once delivery by default.

Load concurrency, background, or module details only when relevant. Sources: [Architecture recommendations](https://developer.android.com/topic/architecture/recommendations), [Domain layer](https://developer.android.com/topic/architecture/domain-layer), [UI events](https://developer.android.com/topic/architecture/ui-layer/events), [Saved state](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate).
