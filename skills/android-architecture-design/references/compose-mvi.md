# Compose: lightweight MVI

For an independent new screen, default to Action → ViewModel → [UseCase] → Repository → immutable UiState → Screen. An extra Store framework is unnecessary. Follow [legacy interoperability](legacy-hybrid.md) for existing Compose MVVM or an XML-embedded component; do not automatically migrate or add another state layer.

- ViewModel exposes read-only StateFlow and action entry points. Define UiState or sealed Actions when needed. An Action is not android.content.Intent. Extract a pure reducer for complex transitions; simple transitions need no separate file.
- A Route obtains the state owner, collects state with lifecycle awareness supported by the project version, and connects navigation. Reusable Screens/components accept state and callbacks instead of depending on Repository, NavController, or ViewModel.
- A Composable body does not perform business IO or redispatch loading on recomposition. Effect keys, cancellation, and cleanup must match their meaning. Handle critical results and navigation under [architecture.md](architecture.md); do not add an Effect bus by default.
- Use remember for disposable local state and rememberSaveable for suitable restorable input. Business state belongs to the ViewModel; do not mirror UiState twice. Do not mutate externally held collections in place or use stability annotations to conceal mutability.
- Use real identity keys in lists and contentType where useful. Optimize measured hotspots; do not add remember, derivedStateOf, or @Stable indiscriminately. The M3 and theme defaults apply only to new or explicitly migrated areas.

Verify relevant action transitions, absence of repeated work on recomposition, error/cancellation paths, and re-entry. Sources: [Compose architecture](https://developer.android.com/develop/ui/compose/architecture), [UI events](https://developer.android.com/topic/architecture/ui-layer/events). MVI and Route/Screen separation are plugin conventions.
