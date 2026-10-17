# Testing and release quality

See [workflow.md](workflow.md) for execution and delivery, and [code-review.md](code-review.md) for review checkpoints. This file covers release and test selection only.

| Change | Relevant evidence |
| --- | --- |
| Pure logic/state | Success, failure, boundaries, cancellation/races; controlled fakes and scheduling rather than fixed sleeps or live production calls |
| Data/background | Mapping, transactions, migrations, duplicate work, recovery, and account isolation |
| UI/navigation | Key tasks, semantics, input, Back, and state restoration; previews assist visual checks |
| System/SDK | Representative older and target versions, affected permission/window/background behavior |
| Release | Reflection/serialization, resources, deep links, JNI, and SDKs in the actual optimized artifact; debug success is insufficient |

Choose representative scenarios by risk, not a mandatory full matrix or universal coverage threshold. Prefer the project's Wrapper, variants, CI, and test framework. Distinguish regressions, pre-existing problems, and environment limits; do not delete tests or repeatedly rerun until a flaky pass appears.

## Before release

- Check applicationId, versionCode sequence, flavors, production environment, merged Manifest, debuggable, logs, and debug entry points. Preserve app identity and existing signing. Distinguish upload key from app signing key; never write keys to the repository or output.
- Keep applicable R8/resource shrinking and verify key paths. Minimize keep rules; do not retain all classes or disable shrinking to hide defects. Match mapping/native symbols to the actual release.
- Inspect the final AAB/generated install artifacts for ABI, split resources, and third-party native libraries. Upgrade over old versions to verify database, sessions, and background work; uninstall/reinstall is not a substitute.
- See [Google Play](google-play-release.md) for policy and eligibility. Tracks, upload, review submission, and rollout follow existing authorization. Pausing rollout does not make a database or APK naturally downgradeable.

Report actual version/variant, commands, devices, results, and limits. Distinguish artifact, upload, review, and public availability. Reuse existing post-release diagnostics under [runtime performance](runtime-performance.md); do not automatically add a monitoring platform.

Sources: [What to test](https://developer.android.com/training/testing/fundamentals/what-to-test), [R8](https://developer.android.com/build/shrink-code), [App signing](https://developer.android.com/studio/publish/app-signing), [App Bundle](https://developer.android.com/studio/publish/upload-bundle).
