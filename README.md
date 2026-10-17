# Android Architecture & Design

A Codex desktop skill package for Android architecture, UI/UX, review, and release preparation, version **1.0.0**. It provides guidance and evaluation resources, not an app, MCP service, or automated release tool.

## Defaults and scope

For new or explicitly updated areas, default to XML MVVM, lightweight MVI for independent Compose screens, Clean boundaries, and Material 3. Reuse suitable existing solutions. Without another requirement, prefer applicable official recommendations or mature libraries such as Retrofit and OkHttp. Add UseCases, modules, offline sync, and frameworks only when needed.

The [skill entry](skills/android-architecture-design/SKILL.md) states shared boundaries and routes to relevant topics. The [shared workflow](skills/android-architecture-design/references/workflow.md) owns scope, conflicts, verification, and delivery. [Review](skills/android-architecture-design/references/code-review.md) defines checks after writing and before an authorized commit. Read other references only when the task touches them.

| Task | Reference |
| --- | --- |
| Legacy/mixed projects | [Incremental changes and interoperability](skills/android-architecture-design/references/legacy-hybrid.md): keep suitable existing choices and change at the host/state boundary |
| Architecture, modules, selection | [Layers](skills/android-architecture-design/references/architecture.md), [modularization](skills/android-architecture-design/references/modularization.md), [libraries and maintenance](skills/android-architecture-design/references/technology-selection.md) |
| UI/UX | [XML](skills/android-architecture-design/references/xml-mvvm.md), [Compose](skills/android-architecture-design/references/compose-mvi.md), [Material 3](skills/android-architecture-design/references/material3-uiux.md) |
| Data and lifecycle | [Concurrency and weak networks](skills/android-architecture-design/references/data-consistency.md), [migrations](skills/android-architecture-design/references/data-migrations.md), [background work](skills/android-architecture-design/references/background-work.md) |
| Performance and privacy | [Runtime and diagnosis](skills/android-architecture-design/references/runtime-performance.md), [Gradle](skills/android-architecture-design/references/build-performance.md), [security](skills/android-architecture-design/references/security-privacy.md) |
| Release | [Release verification](skills/android-architecture-design/references/testing-release.md), [Play adaptation](skills/android-architecture-design/references/google-play-release.md) |

Explicit user requests and project conventions outrank plugin defaults. Preferences cannot waive platform behavior or applicable release requirements. See the [source index](skills/android-architecture-design/references/sources.md). The Play reference does not freeze version thresholds or deadlines; check current official requirements for a real submission.

## Use and packaging

`plugin.json` is the portable entry; `.codex-plugin/plugin.json` is a compatibility entry. Both share one skill directory. This repository has not been installed or published as part of this conversation. Import the root directory using the host's supported local method. If no import UI exists, use the complete skill directory or explicitly ask the agent to read its SKILL.md; manually reading rules does not mean the plugin is installed.

```text
Use $android-architecture-design to implement a search screen in this existing project.
Keep its suitable dependencies and navigation. Proofread and review the change, then explain
the reasons and actual verification.
```

```text
Use $android-architecture-design to review this change for typos, logic, anti-patterns,
Android conventions, performance, and memory leaks. Report evidence-backed findings only;
do not edit or commit yet.
```

```text
Use $android-architecture-design to assess Google Play release readiness.
Check policy as of the expected submission date, target SDK adaptation, and the final
artifact. Report blockers without uploading or submitting for review.
```

## Verification and maintenance

```sh
python3 scripts/validate_plugin.py
python3 -m unittest discover -s tests -v
python3 scripts/run_regressions.py --help
```

Also validate the skill with skill-creator's `quick_validate.py`. The first command checks package structure, links, and reachability; the second tests the validator. Kotlin regressions require a local Kotlin/JDK toolchain; see [evaluation guidance](evals/README.md) for execution and coverage. Android fragments have not been built as an app. Passing pure Kotlin or structural checks does not prove UI behavior or absence of leaks, and is not a model-behavior evaluation.

See [maintenance guidance](MAINTENANCE.md), the [changelog](CHANGELOG.md), and historical [0.5.0](evals/results/0.5.0-local.md) and [0.6.1](evals/results/0.6.1-local.md) local verification records.
