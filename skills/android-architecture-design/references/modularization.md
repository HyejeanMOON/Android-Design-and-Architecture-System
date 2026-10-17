# Proportionate modularization

Split by stable business capability, functional responsibility, or team ownership to achieve cohesion, loose coupling, and clear ownership. Teams and modules need not map one-to-one. Do not judge by fixed line counts, modules per screen/type, or module count.

| Signal | Interpretation |
| --- | --- |
| Worth splitting | Clear gains in independent changes/testing, reuse, ownership, or build isolation |
| Too small | Thin forwarding shells, isolated few types, frequent joint edits, and configuration/API costs greater than isolation benefits |
| Too large | Unrelated domains coupled together, team contention, difficult test isolation, or small edits rebuilding unrelated code |

Package boundaries can suffice for small projects. At larger scale, consider app assembly, features, business data, optional domain, and a small amount of shared core. This is not a scaffold checklist; do not automatically split every feature into api/impl/presentation/domain/data modules. Prefer Kotlin/Java for pure business modules with no Android needs.

- Keep compile dependencies acyclic. Follow [architecture.md](architecture.md) for Clean boundaries; the app assembles features, and core does not depend back on features.
- Features communicate through stable business contracts or navigation callbacks, not each other's internals. Do not hide cycles with a global event bus or mutate another feature's ViewModel.
- Avoid universal common/core modules and exposing DTOs just to skip mapping. Use `implementation` by default; use `api` when a public contract truly exposes a dependency, and protect implementation with visibility.
- Align DI lifetime with the state owner. Do not duplicate business data or sessions that should be shared, or force separate security domains to share one instance.
- More modules do not guarantee faster builds. Measure high fan-in changes, serial dependency chains, and configuration cost.

For module tasks, briefly describe responsibilities, owner if known, public capability, direct dependencies, and key runtime data flow. Distinguish the compile graph from runtime calls. Check assembly, resources, cycles, tests, and impact; a local feature task does not trigger a repository-wide split.

Sources: [Modularization guide](https://developer.android.com/topic/modularization), [Common patterns](https://developer.android.com/topic/modularization/patterns).
