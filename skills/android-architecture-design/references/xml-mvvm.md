# XML: MVVM

For a new or explicitly updated XML screen, default to View → ViewModel → [UseCase] → Repository, with state driving rendering back toward the View. Follow [legacy interoperability](legacy-hybrid.md) at existing and mixed boundaries; do not migrate them automatically.

- Activity/Fragment handles binding, rendering, platform interaction, and navigation; ViewModel owns business calls and state. XML expressions, Adapters, and UI callbacks do not implement business rules.
- Prefer ViewBinding for new bindings. Suitable existing DataBinding/LiveData can remain; new state may use read-only StateFlow. Do not replace sound choices merely for uniformity or duplicate business state.
- Observe with viewLifecycleOwner in a Fragment. Collect Flow with a lifecycle-aware method supported by the project; launch multiple long-running collections separately so they do not block one another. Release binding in onDestroyView; never put it in a ViewModel.
- Represent actual loading, content, empty, error, and input/submit states. Do not require every state on every page or clear content on every refresh. Handle RecyclerView diffing, identity, and invalidated positions correctly.
- When a Fragment must switch among several display modes, use [ActionState, UiState, EventState, and a pure reducer](state-reducer.md) in the ViewModel. The reducer decides the next immutable state; the Fragment has a single idempotent render path to show Loading, Content, Empty, or Error and optional in-content refresh progress. It does not run the reducer or business IO.
- XML Material 3 uses compatible Material Components and Theme.Material3; Compose libraries do not substitute for XML widgets. Preserve existing themes and navigation under the mixed-project rules.

Check touched interactions for duplicate observers, leaks, or lost state after View recreation. Sources: [Architecture recommendations](https://developer.android.com/topic/architecture/recommendations), [Material for Views](https://developer.android.com/develop/ui/views/theming/look-and-feel). MVVM naming and binding preferences are plugin conventions.
