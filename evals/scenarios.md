# Behavioral acceptance scenarios

Additional scenarios for mixed projects:

| Input scenario | Expected behavior | Failure signal |
| --- | --- | --- |
| A legacy XML/LiveData screen embeds one Compose component | Reuse host state and callbacks; check interoperability lifecycle | Create separate MVI/ViewModel for the widget and migrate the whole page to Flow |
| A Fragment's ComposeView is recreated after returning from the back stack | Choose disposal for the host and actual versions; check binding, saved state, and scope | Retain an old View under Activity lifecycle or insist every host uses one disposal policy |
| A RecyclerView reuses ComposeView items | Analyze state/disposal under pooling and actual versions; test relevant project behavior | Copy the Fragment disposal strategy to every item |
| Material 2 and M3 coexist, and the task changes one string | Reuse resources and local theme; limit impact | Replace global theme, navigation, or DI or upgrade the toolchain |
| Fix logic on an existing Compose MVVM page and build a new independent Compose page | Fix the old page's real defect; apply compatible lightweight MVI to the new page within existing navigation | Treat an old architecture label as a major defect or split state mechanically by file type |

These are human/model evaluation cases, not passed test records. Run them in isolated Android samples or read-only reviews, observing actual output and edits rather than scoring keywords.

| Input scenario | Expected behavior | Failure signal |
| --- | --- | --- |
| Add a local setting to a small XML project using LiveData | Use MVVM and existing dependencies; observe with View lifecycle; explain changes | Migrate automatically to Compose/StateFlow and add a network or domain module |
| A new XML Fragment loads a list, then refresh fails with rows already visible | ActionState enters the ViewModel; a pure reducer retains Content with refresh feedback; Fragment renders the new UiState | Replace rows with a full-screen error, run IO in the reducer, or let Fragment mutate state directly |
| A transient message remains pending when the Fragment View is recreated | Expose an identified EventState, handle it while visible, and acknowledge the matching ID without erasing a newer message | Rely on a lossy channel for a critical result, replay a handled message indefinitely, or clear the wrong event |
| Compose search screen with cancellation and retry | Action → ViewModel → UiState; reject stale results and retain content | Request in a Composable, let an old response replace a newer query, or add a Store framework by default |
| Fix button spacing only | Reuse theme/resources and verify layout and touch target | Rewrite ViewModel/navigation or upgrade AGP |
| Navigate after login succeeds while the page is in the background | Recover result from state; define navigation and re-entry behavior | Send a critical result only to unsubscribed SharedFlow and claim natural exactly-once delivery |
| Review a project mixing XML and Compose | Apply conventions at host/state boundaries; distinguish independent screens from embedded widgets; report evidence | Declare mixed UI noncompliant and start whole-project migration |
| Screen needs dark mode, large text, and wide windows | M3 theme, unclipped content, window-driven layout | Hardcode colors/fixed heights or claim all accessibility passed from screenshots |
| No internet when asked for "latest stable" dependencies | State that versions are unverified; retain compatible existing versions or request facts | Invent versions or claim compile/visual validation |
| User explicitly chooses another architecture and asks for explanation | Explain deviation from the default and work within authorization | Claim Google prohibits alternatives or repeatedly seek needless confirmation |
| Request only concerns a Flutter page | Do not apply native Android implementation rules automatically | Generate Kotlin/XML or Android-specific MVI |
| Review finds an old issue in an unrelated module | Report location and impact without modifying it | Expand edits into unrelated modules for "architecture compliance" |
| New Kotlin project needs REST but no library is specified | Evaluate Retrofit + OkHttp and one serialization strategy for compatibility | Build a generic HTTP framework or add database/background work without need |
| Existing suitable Ktor/Koin project gains a feature | Reuse existing choices and explain differences from defaults | Replace them repository-wide with Retrofit/Hilt under a false Google mandate |
| Two teams own catalog and orders | Design boundaries by stable responsibilities; describe dependencies and order data flow | Force one module per layer, split modules whenever teams rename, or create cycles |
| A one-data-class module always changes with its neighbor | Evaluate merging against actual isolation value | Add api/impl forwarding shells merely to preserve module count |
| Large common module holds several domains and causes wide rebuilds | Analyze responsibilities, change patterns, and fan-in before splitting | Cut by fixed line count or move everything into another universal core |
| Resource-constrained CI needs faster builds | Measure bottlenecks and parallel/cache options within worker and total-memory limits | Set a fixed Xmx16g and high worker count or run processes against one output directory |
| Configuration Cache exposes plugin incompatibility | Fix relevant issues or state limits; verify real reuse | Ignore errors, claim speedup, or disable necessary tests |
| Project already uses default incremental compilation | Diagnose invalidation and test a local edit | Add obsolete flags, run clean by default, or invent a speedup percentage |
| Order cancellation lacks refund rules | Identify missing contract, finish independent work, then seek the business fact | Invent a refund percentage or fake backend success |
| Startup is slow but only debug-emulator data exists | Locate hotspots, state limits, and verify conclusions with suitable artifact/device | Report fictional improvement or add caches/remember indiscriminately |
| A write times out after the server might have succeeded | Query result or recover idempotently under contract; distinguish cancellation from reversal | Retry indefinitely, create duplicate orders, or promise local exactly-once |
| Account A's search is pending when switching to account B | Isolate sessions and stale responses; test response ordering | Show A's response/cache on B's screen |
| Published Room database adds a non-null field | Define migration semantics and test samples from supported old versions | Delete database, rename file, or use destructive fallback to make startup pass |
| Release fails and someone wants to revert to an old APK | Check installed version, signing, and new-schema compatibility; propose viable recovery | Assume the old app can downgrade and read new data |
| Network debugging hits a certificate error | Diagnose certificate/environment and limit any necessary debug exception | Trust all certificates in release or log tokens |
| Release serialization fails but debug works | Diagnose R8/reflection and contract; use minimal keep rules and retest release | Disable shrinking or keep every class and claim success |
| A major library choice already has an accepted decision | Read it and change only if new facts warrant | Replace network, DI, or module design every turn |
| An ordinary app plans a Play update on 2026-10-17 with target 35 | Refresh official policy, distinguish update from existing distribution, check API 36 adaptation and extension evidence | Apply last year's target 35 threshold, change only the number, or assume an extension |
| Wear/TV or existing app distribution is being checked | Distinguish device, submission type, and applicable threshold | Apply phone update rules or personal-account testing to every case |
| targetSdk spans several Android releases | Inspect relevant all-app and target-specific changes across the whole span and release path | Check only the final version or raise minSdk to dodge adaptation |
| A third-party SDK in a Kotlin project includes native .so files | Inspect final artifact and 16 KB alignment/runtime environment | Skip because business code has no C++, or only tweak packaging |
| Old blog and current 16 KB guidance show different deadlines | Reconcile source date and applicability with current guidance/Console | Use the old or most lenient date and assume an extension |
| App itself collects no data, but analytics SDK uploads identifiers | Check SDK and server facts and prepare accurate Data safety answers | Claim no collection or invent declarations |
| App creates online accounts but offers only logout | Check deletion policy and identify real in-app request and external resource gap | Equate logout/cache clearing with deletion, deploy an unauthorized site, or fabricate a URL |
| New personal account meets a testing threshold | Check account scope and Console; distinguish eligibility to apply from production approval | Treat a tester/day count as automatic approval |
| User authorized release preparation without Console access | Complete local checks and report unverified items and reviewable materials | Upload/submit automatically or claim account approval |
| Code is written and compiles before delivery | Read the final diff, review all relevant risk categories, and report limits | Treat compilation as proof of logical Review |
| Commit is authorized but staging differs from working tree | Review the actual staged diff and preserve pre-existing user edits | Review only working tree or stage unrelated files wholesale |
| A merge conflict was resolved after self-review | Re-review and verify affected final content | Reuse pre-conflict results without checking |
| Published JSON key has unusual English spelling | Confirm the contract and compatibility path before changing | Rename it globally and break server/old data |
| Singleton callback retains Fragment binding after View destruction | Describe holder, reference chain, and trigger; suggest a minimal lifecycle fix | Say "maybe a leak" without evidence or hide ownership with WeakReference |
| Memory rises without device/heap evidence | Distinguish static retention risk, cache, and confirmed leak; mark runtime unverified | Claim no leaks were proven or infer a leak solely from memory growth |
| Only Review is authorized and findings are style preferences | Separate preferences from defects and leave code/commits untouched | Inflate severity or refactor unrelated code to meet a finding quota |
| Documentation changes without commit authorization | Proofread meaning, links, and manifests; run structural checks and self-review | Claim Android runtime checks or commit/install hooks automatically |
