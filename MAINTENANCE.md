# Plugin maintenance

For plugin maintainers, not a process to run for every Android app task.

## Rule ownership

| Content | Primary owner |
| --- | --- |
| Defaults and selective index | SKILL.md |
| Scope, conflicts, acceptance, evidence, delivery | references/workflow.md |
| Review checklist and checkpoints | references/code-review.md |
| Technical behavior | The relevant specialist reference; shared workflow links to it rather than copying it |
| Installation, updates, evaluation | Repository README, this file, CHANGELOG, and evals |

Before adding a rule, see whether an existing one can be corrected. Expand constraints for repeated real needs or reproducible failures, not every theoretical risk. State trigger, factual source, and verification method. Update the single owner for shared semantics and inspect callers. Links enable selective navigation, not recursive loading of the entire package.

## Changes and policy maintenance

- Distinguish new capabilities, defect fixes, and default changes. During 0.x, meaningful default or organization changes raised the minor version and small fixes the patch version. From 1.0 onward, breaking compatibility raises the major version. Synchronize both manifests and README. Do not claim universal host compatibility without testing.
- Record default differences, merged paths, retained capabilities, and user actions in release notes. Previously accepted project decisions remain in force after a plugin update; new defaults apply to future tasks and do not migrate user apps automatically.
- Recheck policy for each actual release task. Date repository snapshots rather than claiming perpetual freshness. Do not create recurring monitors without authorization. When a source is stale, update its current location and date, keeping only necessary historical context.
- If a source moves, find its maintainer's new location before changing dependency coordinates. Search callers, evaluations, and examples before deleting or merging rules. Remove obsolete entries instead of layering exceptions indefinitely.

## Update checks

Run structural validation, validator tests, and skill-creator validation. Record entry and total runtime Markdown byte changes to spot growth, without treating a size threshold as proof of quality. Run relevant regressions for source/example logic changes; prose-only changes do not require recompiling every fixture.

Evaluations should include genuine defects, correct controls, and scope control. Isolate inputs from answers; author self-review or keyword matching is not an independent model evaluation. Test failure paths for new scripts. Use minimal reproductions to correct omissions or false positives rather than piling up keywords.

Do not automatically install hooks, launch other agents, upload evaluation material, or operate a user's repository. Execution permissions come from the host. Use temporary directories and redacted fixtures. Passing tests supports only their actual coverage, not a promise to eliminate all risks.
