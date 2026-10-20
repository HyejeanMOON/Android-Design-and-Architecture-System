# Action, UI, and Event state with a reducer

Use this convention for new or explicitly updated screens with meaningful state transitions, especially XML Fragments that switch among loading, content, empty, and error views. Preserve suitable legacy state handling for local fixes. These three roles and the names below are plugin conventions, not a mandatory Google API or a reason to add an MVI framework.

| Role | Contract |
| --- | --- |
| `ActionState` | User or system input such as Refresh, Retry, or MessageAcknowledged. Despite its name, an action happens; it is not a persistent snapshot. The UI handles purely local visual actions itself and sends business actions to the ViewModel. |
| `UiState` | The ViewModel-owned immutable snapshot that the Fragment or Compose screen renders. Keep display state and relevant persistent business results here. Expose it read-only through the project's suitable StateFlow or LiveData. |
| `EventState` | Optional pending, UI-only feedback such as a snackbar. Give it identity and an acknowledgement path. It can be a field of `UiState` rather than a second, competing source of truth. Critical navigation or transaction outcomes must remain recoverable in `UiState`; do not assume a Channel, SharedFlow, or Event wrapper guarantees delivery exactly once. |

The flow is `ActionState → ViewModel → [UseCase/Repository] → Result/Mutation → reducer(previous UiState, mutation) → new UiState → render`. The ViewModel runs asynchronous work and rejects stale request/session results before reducing them. The reducer is a pure, synchronous state transition: no IO, navigation, View access, logging, clock reads, random IDs, or external mutation. When using `MutableStateFlow.update`, the reducer may be invoked again under contention, so derive from the supplied current state and create event IDs outside the update lambda. A simple `when` function or a small ViewModel-private function is enough; no Store or universal reducer framework is required.

For mutually exclusive whole-screen views, use a sealed display state. Keep an orthogonal `refreshing` flag when content or empty state remains visible during refresh. For example, the following is an illustrative pure Kotlin transition, not a production template:

```kotlin
sealed interface ActionState {
    object Refresh : ActionState
    data class MessageAcknowledged(val id: Long) : ActionState
}

sealed interface DisplayState {
    object Loading : DisplayState
    data class Content(val rows: List<String>) : DisplayState
    object Empty : DisplayState
    data class Error(val message: String) : DisplayState
}

data class EventState(val id: Long, val message: String)
data class UiState(
    val display: DisplayState = DisplayState.Loading,
    val refreshing: Boolean = false,
    val event: EventState? = null,
)

sealed interface Mutation {
    object Started : Mutation
    data class Loaded(val rows: List<String>) : Mutation
    data class Failed(val message: String, val eventId: Long) : Mutation
    data class EventAcknowledged(val id: Long) : Mutation
}

fun reduce(previous: UiState, change: Mutation): UiState = when (change) {
    Mutation.Started -> when (previous.display) {
        is DisplayState.Content, DisplayState.Empty -> previous.copy(refreshing = true)
        else -> previous.copy(display = DisplayState.Loading, refreshing = false)
    }
    is Mutation.Loaded -> previous.copy(
        display = if (change.rows.isEmpty()) DisplayState.Empty else DisplayState.Content(change.rows),
        refreshing = false,
    )
    is Mutation.Failed -> when (previous.display) {
        is DisplayState.Content, DisplayState.Empty -> previous.copy(
            refreshing = false,
            event = EventState(change.eventId, change.message),
        )
        else -> previous.copy(display = DisplayState.Error(change.message), refreshing = false)
    }
    is Mutation.EventAcknowledged -> if (previous.event?.id == change.id) {
        previous.copy(event = null)
    } else previous
}
```

The Fragment collects state with `viewLifecycleOwner` at an appropriate lifecycle state and has one `render(state)` path: show only the view selected by `display`, then apply refresh progress without hiding retained content. A full-screen error is for no usable content; a failed refresh preserves rows and exposes recoverable feedback. Convert backend errors into safe, localized UI text at the appropriate boundary. Render idempotently after View recreation. Handle a pending event while visible and acknowledge its matching ID after handling; an old acknowledgement must not erase a newer event. The sample keeps one pending event until acknowledgement and replaces it on a newer failure; if several messages must survive, model a bounded queue and acknowledgement instead. Navigation stays with the UI and needs an explicit re-entry/back-stack policy.

Test transitions for first load, empty result, success, failed first load, refresh over content, failed refresh retaining content, retry, stale response/session rejection, and acknowledgement after View recreation. Select only scenarios relevant to the feature. Keep a simple screen simple; local focus or animation state need not be forced into this contract.

Sources: [Android UI state production for Views](https://developer.android.com/topic/libraries/architecture/views/state-production-views), [UI events for Views](https://developer.android.com/topic/architecture/views/ui-layer/events-views), [Orbit MVI example](https://github.com/orbit-mvi/orbit-mvi), [Mavericks reducer guidance](https://github.com/airbnb/mavericks/wiki), [StateFlow.update contract](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/update.html). Orbit and Mavericks are examples of reducer design, not dependency requirements.
