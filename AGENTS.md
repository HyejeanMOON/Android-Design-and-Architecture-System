# Repository working agreement

- After changing code, explain what changed and why.
- After editing, proofread and review the change using `skills/android-architecture-design/references/code-review.md`. Before an authorized commit, review the final content again. For this repository, focus on rule semantics, typos, examples, links, manifests, and compatibility. Do not claim Android runtime checks that were not run or automatically commit or install hooks because of this rule.
- This repository contains the Codex Android architecture and design plugin, not an Android app. Do not create an Android project or add a Gradle toolchain without a task that requires it.
- `skills/android-architecture-design/SKILL.md` is the single entry point for Android development rules. Keep detailed rules in its `references/` directory rather than maintaining inconsistent copies.
- Distinguish official recommendations, user choices, and plugin conventions. Do not present XML MVVM, Compose MVI, or strict Clean layering as Google's only official architecture.
- `references/workflow.md` owns the shared workflow; specialist files own domain rules. Follow `MAINTENANCE.md` for plugin maintenance. Do not impose author maintenance or evaluation procedures on every Android task.
- After plugin changes, run skill structure validation and `scripts/validate_plugin.py`. Run `tests` when scripts change and relevant regressions when example logic changes. These checks cannot prove Android device or model behavior.
