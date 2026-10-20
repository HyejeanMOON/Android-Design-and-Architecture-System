# Changelog

## 1.2.0 — 2026-10-21

- Added a selectively loaded DI/Hilt reference grounded in current Android guidance: constructor injection, graph ownership, Hilt bindings and scopes, ViewModel ownership, legacy migration, multi-module limits, and test replacement.
- Preserved manual DI and suitable existing Koin/Dagger graphs; Hilt is a recommended choice for sufficiently complex apps, not a migration requirement for every legacy feature.
- Runtime Markdown is 21 files / 69,319 UTF-8 bytes (was 20 / 64,548); the skill entry is 2,930 bytes (was 2,861). DI detail is loaded only when relevant.

## 1.1.0 — 2026-10-21

- Added an ActionState/UiState/EventState contract and pure reducer guidance for new or explicitly redesigned screens with meaningful state transitions, including XML Fragment loading, content, empty, error, and refresh behavior.
- Kept transient feedback acknowledged in UI state, critical results recoverable, and legacy or embedded UI free from forced migration. This is a plugin convention informed by Android guidance and reducer examples, not a Google-mandated framework.
- Runtime Markdown is 20 files / 64,548 UTF-8 bytes (was 19 / 57,187); the entry is 2,861 bytes (was 2,631). The added detail lives in the selectively loaded reducer reference.

## Packaging — 2026-10-20

- Added a repository marketplace entry and a reproducible skills-only ZIP builder for Codex distribution. The plugin instructions and version remain 1.0.0; installation and publication are separate actions.

## 1.0.0 — 2026-10-17

- Translate the plugin interface, skill instructions, technical references, maintenance guidance, and evaluation material into English.
- Preserve the existing architectural defaults and evaluation boundaries. Version 1.0.0 marks an English-language release; it does not imply Android device, host installation, or model-behavior validation.
- Runtime Markdown now totals 57,187 UTF-8 bytes across 19 files (47,449 in 0.6.1); the skill entry is 2,631 bytes (2,235 in 0.6.1). These are size measurements, not token or quality scores.

## 0.6.1 — 2026-10-17

- Consolidated shared workflow, Review, legacy interoperability, and UI guidance. Defaults apply only to new or explicitly updated areas; legacy solutions are not globally migrated.
- Clarified that review-only tasks report without editing, implementation tasks fix within authorized scope, and valid tests for unchanged content can be reused. Theoretical risks do not widen remediation or approval scope.
- Streamlined modularization, builds, visuals, and repeated source notes. Kept dynamic Play verification and adaptation while removing hardcoded historical API/date thresholds from runtime guidance.
- Preserved all domain entry points and both Review checkpoints. Did not change evaluation scripts or fixture logic or claim that all risks were eliminated.

## 0.6.0 — 2026-10-17

- Added guidance for old projects mixing XML and Compose, covering incremental changes, host lifecycle, shared state, navigation, and themes.
- Distinguished independent Compose screens from XML-embedded Compose components; architecture defaults do not force wholesale migration.
- Added specialized review scenarios. This was a rule change, without an app project or claimed validation on a real mixed project.

## 0.5.0 — 2026-10-17

- Merged overlapping requirements, verification, and decision/completion flows into `references/workflow.md`. Shortened the skill entry and Review guidance; load domain details only when touched, rather than recursively following links.
- Kept XML MVVM, Compose MVI, Clean, Material 3, modularization, Gradle, release, and both Review checkpoints. Existing suitable solutions and user choices take precedence; no automatic scope expansion or rerun of valid unchanged tests.
- Expanded dependency upgrades, weak-network behavior, background work, and diagnosis. Added maintenance guidance and bounded fixtures/regressions.
- Merged former `requirements-acceptance.md`, `verification.md`, and `decisions-completion.md` paths. Users invoking the skill need no app migration; configurations linking those old files should point to workflow.md.
- Reported package structure/local regressions separately from Android device/model evaluations; see the version verification records.

## 0.1.0–0.4.0

Architecture and UI/UX, selection and builds, engineering quality and Play, then proofreading and Review were added iteratively in this conversation. Those versions had structural checks and author self-review only. Do not infer Android device or independent model evaluation from them.
