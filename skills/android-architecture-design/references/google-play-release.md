# Google Play and target SDK adaptation

Use this for release preparation, policy warnings, relevant restricted capabilities, or targetSdk upgrades. [Release verification](testing-release.md) owns artifact checks; do not create a duplicate workflow here.

## Verify current requirements

For the intended submission date, consult current policy and any accessible Play Console. Record sources, checked/effective/deadline dates, and applicability. Distinguish device category, first submission/update/existing distribution, track, region, and account eligibility. Inspect actual SDKs, native dependencies, third-party SDKs, and used capabilities. A new-submission threshold is not always an existing-distribution threshold; Android Auto and Automotive OS differ.

This skill hardcodes no target API, Billing, or tester/day thresholds. Verify them using [official target requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en), [account testing eligibility](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en), and applicable current pages. Extensions require evidence of the app's eligibility or approval. When sources conflict, reconcile dates and scope rather than claiming compliance from the most lenient figure.

Mark unknowns for verification and continue independent local work. Missing Console evidence is neither proof of compliance nor automatic proof of violation. Historical records and blogs provide context, not operative thresholds.

## Platform and artifact

- Distinguish minSdk installation coverage, compileSdk compile APIs, and targetSdk behavior. Changing only a number or raising minSdk to drop old users does not substitute for adaptation.
- Across the whole target upgrade span, inspect relevant all-app and target-specific behavior changes. Map them to actual permissions, background/foreground services, alarms, storage, components/PendingIntents, navigation, windows/IME, Back, and large-screen behavior. Explain applicability; do not add unused capabilities.
- Upgrade toolchain/dependencies only to a necessary compatible combination. Temporary opt-outs must remain officially supported, with scope and follow-up recorded. Do not lower target or disable checks to evade requirements. Verify affected behavior on representative old and new target systems and in-place upgrades.
- Inspect the final artifact, including transitive SDKs, for applicable ABI/64-bit/native `.so` and [16 KB ELF, packaging, and runtime compatibility](https://developer.android.com/guide/practices/page-sizes). Kotlin business code does not imply absence of native dependencies. When all dependencies are Kotlin/Java, do not add NDK without a need. Packaging tweaks or hidden warnings alone do not prove compatibility.
- Check current sources for SDK risks and deadlines. If Billing is used, consult the [deprecation schedule](https://developer.android.com/google/play/billing/deprecation-faq). Whether Play Billing is required depends on product, region, and applicable programs.

## Console and policy materials

| Condition | Verify |
| --- | --- |
| Store listing/App content | Real functionality, screenshots, ads, audience, and rating; do not invent credentials or qualifications |
| Data safety/privacy | Actual app/SDK/server collection, sharing, purpose, and deletion. Do not generalize track exemptions; collecting nothing does not automatically waive declarations. |
| Online account creation | Where applicable, in-app deletion request and an external web resource, plus related-data handling. Logout/deactivation is not deletion. |
| Restricted access | Working review access, environment, and instructions; do not fabricate URLs or credentials. |
| Sensitive/special categories | Trigger eligibility, disclosures, and declarations by actual permissions, children, health, finance, UGC, ads, or subscriptions; do not impose every category. |
| Account/testing | Actual developer verification, region, track, testing, and production access. Source code cannot prove eligibility; meeting testing conditions is not automatic approval. |

For rejection, retain a redacted reason, version/track, source, and deadline. Separate code, SDK, artifact, declaration, account, and backend issues, then make the smallest fix. Do not hide permissions or file false declarations. Appeals, upload, review submission, and rollout follow existing authorization.

Deliver an applicability matrix tied to the version: requirement/date, source, impact, status, evidence, and remaining blocker. Distinguish verified, pending verification, pending information, inapplicable, and clearly blocked. Local checks do not guarantee store approval.

Sources: [Target SDK migration](https://developer.android.com/google/play/requirements/target-sdk), [Review readiness](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en), [Data safety](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en), [Account deletion](https://support.google.com/googleplay/android-developer/answer/13327111).
