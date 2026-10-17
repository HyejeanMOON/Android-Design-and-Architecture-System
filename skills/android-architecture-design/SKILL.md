---
name: android-architecture-design
description: Guide native Android architecture, UI/UX, review, and release preparation in existing XML and Compose projects. Default to XML MVVM, lightweight MVI for independent new Compose screens, Clean boundaries, and Material 3. Not for Flutter, web, or maintaining this plugin.
---

# Android Architecture & Design

Use the [shared workflow](references/workflow.md) for scope, rule priority, verification, and delivery. Inspect the actual project first; defaults do not require wholesale migration of legacy code. Explain changes and reasons in the user's language.

For new or explicitly updated areas, default to XML MVVM, lightweight MVI for independent Compose screens, Clean responsibility boundaries, and Material 3. Reuse suitable existing solutions; otherwise prefer applicable official guidance or mature libraries. Add UseCases, modules, generic frameworks, offline sync, and monitoring only for demonstrated needs.

After writing code and before an authorized commit, proofread and review it using [Review](references/code-review.md). Reuse valid test evidence for unchanged content. Do not invent business contracts, versions, verification results, or release eligibility. This skill does not authorize commits or publication.

## Read only what the task touches

Links are navigation aids, not an instruction to load every file recursively. Small changes do not require repository-wide audits or full reports.

| Task | Reference |
| --- | --- |
| Legacy project, mixed UI, incremental migration | [Legacy interoperability](references/legacy-hybrid.md) |
| Layers, modules, library selection | [Architecture](references/architecture.md), [Modularization](references/modularization.md), [Technology selection](references/technology-selection.md) |
| XML, Compose, UI/UX | [XML MVVM](references/xml-mvvm.md), [Compose MVI](references/compose-mvi.md), [Material 3](references/material3-uiux.md) |
| Concurrency, migration, background work | [Data consistency](references/data-consistency.md), [Data migrations](references/data-migrations.md), [Background work](references/background-work.md) |
| Performance, builds, security | [Runtime performance](references/runtime-performance.md), [Gradle](references/build-performance.md), [Security](references/security-privacy.md) |
| Release and Play readiness | [Release verification](references/testing-release.md), [Google Play](references/google-play-release.md) |

Check current applicable official sources for new APIs, versions, platform behavior, and policy; see [Sources](references/sources.md). State any verification limits.
