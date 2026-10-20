# Legacy XML and Compose projects

Read this when changing legacy code, crossing XML/Compose boundaries, or migrating a feature. Mixed UI technology is not itself a defect. First identify the touched host, navigation, state owner, theme, data entry point, and actual versions; avoid a preliminary audit of the entire repository.

## Change boundaries

- When fixing an old screen, keep suitable UI, LiveData/Flow/Rx, DataBinding, DI, and navigation choices. A local fix does not trigger migration.
- The ActionState/UiState/EventState reducer convention applies to new or explicitly redesigned screen state; do not add it to a small legacy fix or an embedded widget merely to standardize names.
- Compose embedded in XML receives host state and callbacks; it needs no separate MVI or ViewModel. Apply the lightweight MVI default only to an independent new Compose screen, connected to existing navigation. A Fragment may still host it.
- For explicit migration, replace business slices and verify old/new contracts and data. Do not migrate unrelated toolchains, storage, or modules at the same time. A legacy project remains subject to applicable release requirements.

## Interoperability checks

- A ComposeView inside a Fragment should dispose its composition with the View lifecycle. Select a strategy supported by the project's version and host, such as `DisposeOnViewTreeLifecycleDestroyed`. RecyclerView pooling and other hosts have different strategies. Give multiple ComposeViews distinct, restorable IDs.
- Manage AndroidView/AndroidViewBinding creation, updates, reuse, callbacks, and resource release according to the actual API. Callbacks such as onReset/onRelease depend on version. Do not force a toolchain upgrade just to use them or release shared resources.
- Check ViewModel instance identity and scope across Fragment, Activity, navigation graph, and Compose. Do not duplicate one business state on both sides or forcibly merge unrelated local state. Bridges must not form update loops, duplicate subscriptions or requests, or consume results twice.
- Preserve navigation ownership, arguments, and results. Check Back, deep links, focus, scrolling, IME, and insets for duplicate handling. Re-entry, View recreation, and restoration must not retain stale Views/closures or wrong state.
- Material 2/AppCompat and Material 3 may coexist during migration. XML themes do not automatically flow into Compose. Prefer M3 for new or explicitly migrated areas while reusing design semantics; do not replace the global theme or introduce needless visual fragmentation.

Choose entry/Back, rotation, View recreation, process restoration, and relevant failure checks according to the change. Preserve existing user data; reinstalling or clearing data does not verify an upgrade. In Review, distinguish new defects, historical risks, and optional migration ideas. Report dynamic verification limits through the shared workflow.

Sources: [Migration strategy](https://developer.android.com/develop/ui/compose/migrate/strategy), [Compose in Views](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/compose-in-views), [Views in Compose](https://developer.android.com/develop/ui/compose/migrate/interoperability-apis/views-in-compose).
