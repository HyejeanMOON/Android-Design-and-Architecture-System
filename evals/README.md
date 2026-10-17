# Evaluation scope and execution

These fixtures test Review and repair behavior. They are not production templates or an Android app. Keep the skill rules separate from evaluation answers so reading the answer cannot be mistaken for detecting a defect.

## Three source slices

| Case | Content | Executable boundary |
| --- | --- | --- |
| [XML](cases/xml/prompt.md) | Fragment, layout, resources, and an external field key; lifecycle and typo defects plus a correct control | XML parses; the Fragment needs a separate Android test project to compile or verify leaks at runtime |
| [Compose](cases/compose/prompt.md) | Route, ViewModel interface, state, and display; recomposition side effect plus a correct control | Requires an Android/Compose build and UI environment; this repository has no app project |
| [State](cases/state/prompt.md) | Pure Kotlin state component suitable for ViewModel use; out-of-order, session, and refresh-failure defects | Compiles and runs deterministic behavior tests with Kotlin/JDK; does not establish thread safety or Android lifecycle correctness |

Each `input/` is the evaluation input; `fixed/` is one reference repair. An evaluated model need not produce identical code. Score actual behavior, evidence, and scope control.

## Local regression

```sh
python3 scripts/run_regressions.py --kotlinc /path/to/kotlinc --java /path/to/java
```

The script compiles in a temporary directory. Both defective and repaired variants must compile. The defective version must fail five specific behavior scenarios while passing the normal path; the repaired version must pass all six. Compilation failure does not count as defect detection. Missing tools return a not-run status rather than downloading or installing a toolchain.

State checks control completion order without sleeps, network, or implementation-text matching. XML checking parses syntax only; it is not an Android resource build. Reference Android API/binding code still needs separate project and device verification.

When evaluating a repair in an isolated copy, pass `--candidate /isolated/SearchModel.kt`. Candidate mode requires all six cases to pass. Default mode still expects failures in the original defective input. This avoids treating a successful repair as a broken baseline without changing tests or scoring.

## Human/model behavior evaluation

1. In an isolated directory, provide only the selected case's `input/`, `prompt.md`, and skill directory to the evaluator. Withhold `fixed/`, [oracle.json](oracle.json), this page, and previous answers.
2. Record raw output for review-only mode without edits or commits. In repair mode, edit only the isolated copy and run relevant behavior checks. Do not treat repository scoring files as agent instructions.
3. After evaluation, compare location, trigger, impact, evidence, and suggestion with the oracle's meaning. Record misses, false positives, external-key misrenames, unrelated refactors, false verification claims, and out-of-scope operations. Keywords and finding count alone cannot pass.
4. Repeat with correct controls or repaired variants to observe false positives. Run the same behavior regression after a repair to ensure tests were not weakened.
5. Record date, model/version, skill version, task and input versions, actual tools, output, and result. Do not call author self-review an independent model evaluation or launch agents/upload code without authorization.

More cross-domain scenarios are in [scenarios.md](scenarios.md); select by risk or rule change, not a mandatory full run after every prose edit. Actual historical execution is recorded in the [0.5.0 report](results/0.5.0-local.md).
