# Walk return: run B, walker 3, test and deploy

**Serves:** research PLAY-dClosedLoop-1

Dispatch 171's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-12-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed in this scenario because the landing tail treats "filed" as "done". A core red at landing closes the build that caused it once a patch is filed. The patch chain then has nowhere to record the originating build's budget, and a dependent's hold on its parent never times out. So S3 and S5 never reach a terminal whose witness the owner can trust.

### B3-F1 — The seen-red check writes the record it checks for
- **Address:** layer-memory [design], kind `seen-red`; flow-steps [test] `test.seen-red`
- **Class:** K3, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:** In layer-memory's kind table: "| seen-red | dWitnessedBar | its writer is `test.seen-red` |". In flow-steps, `test.seen-red` "checks that every gate the build added or changed has a seen-red record", and its witness is "the seen-red records". `cl-dClosedLoop-0345` says only "seen-red records".
- **Consequence:** The only declared writer of the record is the item that checks it exists. A gate the S1 feature adds gets its seen-red record from the check itself, whether or not anyone ever saw it red, so `test.seen-red` always passes. The guard shares state with what it guards.
- **Fix:** Make the seen-red record's writer the run that observed the planted red: the leg factory's seen-red arm, run inside the unit's pass, keyed by the leg and the red SHA. Keep `test.seen-red` as a reader only. Seed a red case: a gate with no observed red must make `test.seen-red` red.

### B3-F2 — A core red at landing lets the build close once a patch is filed
- **Address:** flow-steps [deploy] `deploy.core`; architecture-v2 [chain] `cl-dClosedLoop-0423`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S3
- **Evidence:** `deploy.core`: "red → a patch build through the entry-point table's post-close row, and the close waits for its filing". v2's opening revision: "a core red that first appears in the landing merge still stops that build from closing". `cl-dClosedLoop-0423`: "so a core red the landing merge introduced stops that build from closing (foundations K1)". P16: "A violation the bypass let through stops the build that made it from closing".
- **Consequence:** In S3 the originating build reaches `deploy.close` and `landed` as soon as the patch is filed. The owner's K1 rule ("the violator pays") is loosened at the item that implements it. The originating build is closed before its patch lands, which also takes away the budget owner that F3 needs.
- **Fix:** Make `deploy.core`'s red route hold `deploy.close` until the patch build's `deploy.core` is green for a SHA that contains the landed one, or an owner exception (`core.exceptions`). Add a matching transitions row.

### B3-F3 — Patch builds have no link to the originating build's budget
- **Address:** flow-steps [rules] (the "Every route back is bounded" bullet); flow-steps [entry] `entry.claim`; architecture-v2 [chain] `cl-dClosedLoop-0440`
- **Class:** K6, c2
- **Severity:** high
- **Scenario:** S3
- **Evidence:** flow-steps [rules] lists only "A route back, a fix pass, a review round after the first, a re-dispatch after a refusal and a research or probe round trip" as drawing on the budget. v2's `flow.rework-budget` adds "patch build of the build's own landing", and `cl-dClosedLoop-0440` builds "a chain of patch builds shares one budget". `entry.claim`'s claim commit carries only "the claimant's key, the session and the intake's or the ask's content key". The census in stall-and-loop says every new build "starts at zero".
- **Consequence:** A patch build is claimed under a fresh slug, and nothing records which build it came from. So `cl-dClosedLoop-0440` has no key to charge. When the patch's own landing goes red again, S3 starts a new budget instead of drawing on the old one. "The originating build's budget spent" has no declared outcome, and the originating build may already be closed (F2).
- **Fix:** Add "a patch build of the build's own landing" to flow-steps [rules]. Make the post-close patch intake and `entry.claim` record the originating build's slug, and the budget key derived from it. Point `flow.on-exhausted` at the originating build's chain. Seed a red case: a patch chain whose second patch shows a fresh budget.

### B3-F4 — The owner's landing gate can be passed by the supervisor's own choice
- **Address:** flow-steps [deploy] `deploy.mandate`; flow-steps [breakpoint]; architecture-v2 [policies] `run.on-owner-question`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:** `deploy.mandate` checks, "under `three-gates` and `every-stage`, the disposition of the owner's landing gate". [breakpoint]: an owner breakpoint is resolved by `run.on-owner-question` "when it is raised, never for a ratification ... the supervisor's recorded choice under `best-effort-recorded`". The witness list includes "under `best-effort-recorded`, the supervisor's recorded choice". `best-effort-recorded` is the default, and it is the `run.on-owner-question` value in every preset except strict (park-item).
- **Consequence:** An owner who sets `autonomy: three-gates` to gate landings gets a gate the supervisor fills in as soon as it is raised. `deploy.mandate` then certifies an owner mandate that the acting side typed, which breaks P2.
- **Fix:** Treat the design go and the landing gate like ratifications: `run.on-owner-question` and `apply-recommendation` never decide them. Make `deploy.mandate` refuse a gate witness that is not an owner disposition. Seed a red case: a planted `best-effort-recorded` choice offered as the gate's witness.

### B3-F5 — A parent hold has no deadline and no outcome
- **Address:** flow-steps [deploy] `deploy.parents`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S5
- **Evidence:** `deploy.parents`: "a parent unlanded or paused → holds", with no deadline. v2's `flow.wait-ceiling` names "a dependency hold ... past which the waiter takes its declared outcome". Stall-and-loop item 6: "dependency and mailbox waits: past their deadline, the waiter takes its declared default (replan ...)". `cl-dClosedLoop-0118` reds any wait that does not declare an outcome and a deadline. `cl-dClosedLoop-0328` releases dependents only on a wait cycle or when a parent ends incomplete.
- **Consequence:** If Y's parent X is alive but stalled or paused (a paused build's leases are renewed), Y waits at `deploy.parents` forever. The S5 probe "Y's wait outlasting its deadline" reaches no terminal, and gov's own item fails the design's own static termination check.
- **Fix:** Change `deploy.parents`' hold to "holds until `flow.wait-ceiling`, then as `deps.on-parent-withdrawn` says, with an owner item". Make it a counted wait with its witness.

### B3-F6 — dWitnessedBar owns the remote verdict, but no unit builds it
- **Address:** architecture-v2 [chain] dWitnessedBar row; architecture-v2 [enforcement] `P3`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** gap-test-02 (HIGH, on dWitnessedBar's row): "The verdict-backend registry Test declares, and the remote verdict before the landing under `verdict: remote-ci`, are this gap's". dWitnessedBar's clauses `cl-dClosedLoop-0339` to `cl-dClosedLoop-0368` include no registry, no remote-ci read, and nothing for `verdict.remote.trust`, `.pin` or `.pin-scope`. Stage 0's K4 lead lists all three keys as "read by no chain clause". The P3 row names only 0342 and 0344. flow-steps says the remote verdict "is built when CI exists (R5.2)". CI already exists today: `cl-dClosedLoop-0029` cites `.github/workflows/remote-ci.yml`.
- **Consequence:** If a node in S2 selects `verdict: remote-ci`, the remote verdict is judged by a workflow that sits in the tree it judges, and no unit builds the pin or the trust guard. P3's "designed slot" and a HIGH gap stay uncarried, and dTrueNorth's coverage report would show them uncarried only at Design exit.
- **Fix:** Give dWitnessedBar a clause for the backend registry and the pinned-workflow trust arm, seen red on a build that edits its own pinned workflow. Or move gap-test-02 and the three keys to an integrations row and record the move.

### B3-F7 — `test.route` sends a non-blocking MIXED red two ways
- **Address:** flow-steps [test] `test.route`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Evidence:** `test.route`: "routes each red by its computed class, as `verdict.blocks` says ... an OWN or MIXED red → `test.attribute`; ... a red that does not block → an ask". The default is `verdict.blocks: own-only` (v2 line 1144), under which MIXED does not block. layer-flow [settled]: "MIXED, CONTENDED and DEAD PROBE route by `verdict.blocks`: to an ask when they do not block".
- **Consequence:** Under the default, a MIXED red matches both arms. A spec writer cannot tell whether it goes to the tester, and so to a fix pass, or to an ask that lets the landing go ahead.
- **Fix:** Condition the arm: "an OWN red, or a MIXED red where `verdict.blocks` blocks it → `test.attribute`".

### B3-F8 — Several Test and Deploy outcomes end at an ask, leaving the build with no next step
- **Address:** flow-steps [test] `test.merge`; flow-steps [deploy] `deploy.land`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S6
- **Evidence:** `test.merge`: "refused → an ask naming the lander's refusal". `deploy.land`: "or an ask for a carried commit"; "an argument → an ask on the adapter". Memory [asks]' acceptance for a lander refusal is "`--prepare` next succeeds for the build", but no item routes back to `--prepare`, and [transitions] has no row for these cases.
- **Consequence:** The build sits in `testing` or `deploying`. It has no next item, no wait deadline and no owner item, against P39's "every wait expires".
- **Fix:** Route each of these to a counted wait on the ask's acceptance that re-enters `test.merge`. Past `flow.wait-ceiling`, raise an owner item. Add the transitions rows.

### B3-F9 — After the push, an unreachable remote spends the rework budget
- **Address:** flow-steps [deploy] `deploy.notify`, `deploy.snapshot`, `deploy.unlease`, `deploy.close`; flow-steps [rules]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Evidence:** Of these four items only `deploy.land` declares "the remote unreachable → the supervisor's retry, then an owner item". The other four each write to the remote (mailbox posts, the snapshot commit, tombstones, the transition under the claim ref) and declare no unreachable route. [rules]: "A re-dispatch of a refused instance draws on the build's rework budget". Only contention draws nothing.
- **Consequence:** In S6, a remote outage after the push re-dispatches these items against the budget of a build that has already landed. When the budget runs out, `flow.on-exhausted`'s endings (descope, close-incomplete) are applied to landed work.
- **Fix:** Class an unreachable remote as contention for every command item: a retry that draws nothing, then an owner item at `flow.wait-ceiling`, as `deploy.land` already does.

### B3-F10 — `landing.order` is never read, so strict's `owner-orders` does nothing
- **Address:** flow-steps [deploy] (landing order); architecture-v2 [chain] `cl-dClosedLoop-0422`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** flow-steps: "Landings on a node are ordered by `landing.order`". No item's Does cell reads it, and `cl-dClosedLoop-0422` says only "landings ordered through the landing queue it builds". Stage 0's K4 lead: "landing.order: read by no chain clause and no item". The strict preset sets `owner-orders`.
- **Consequence:** In S2, when X and Y verify at once, the landing order is whatever the queue does. Strict's `owner-orders` is silently ignored.
- **Fix:** Have `cl-dClosedLoop-0422` read `landing.order` with an arm for each value, and `deploy.land` need the queue's admission. Seed a red case: an `owner-orders` landing admitted with no order.

### B3-F11 — `deploy.mandate` reads the intake record as the plan-only mandate
- **Address:** flow-steps [deploy] `deploy.mandate`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** `deploy.mandate`'s witness is "the intake record, or the gate's witness" ("the request's mandate under `plan-only`"). v2's revision of 2026-10-14: under `plan-only`, "the owner's plan ratification is the mandate". flow-steps [plan]: only under `plan.ratification: request` is the request the ratification. A triage-selected build has no intake record, and gap-flow-14 lists "Maintain's agent-typed intake becomes a patch build's mandate".
- **Consequence:** The landing's authority comes from the wrong record. A ratified plan is not checked. An ask-selected build has no witness. An S3 patch from Maintain is mandated by a rendered intake, which is the defect gap-flow-14 records.
- **Fix:** Witness the mandate per entry: the `plan.exit` ratification (its disposition, or the request under `request`), the triage record for a select, and `patch.ratify`'s disposition for a patch.

### B3-F12 — `deploy.distill` can pass on an empty join before dScopedBuild lands
- **Address:** flow-steps [deploy] `deploy.distill`; architecture-v2 [chain] dShippedRelease row
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:** `deploy.distill` "confirms that the decision-log rows `build.distill` wrote are in the log", joined to "the build's major forks". `build.distill` belongs to dScopedBuild, and fork classes to dIndexedDesign. The design map gives dShippedRelease the parents "dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine, dLinkedLibrary, dFurnishedOrders", which include neither of those builds or their descendants.
- **Consequence:** dShippedRelease can land first. Its `deploy.distill` would then join zero classed forks to zero rows and pass, counting an empty population as coverage.
- **Fix:** Add dScopedBuild to dShippedRelease's parents. Or declare that `deploy.distill` reports "measured nothing" and never passes until `build.distill`'s writer lands, seen red on an empty population.

### B3-F13 — `test.exit` writes to a lease record that dWitnessedBar's parents don't build
- **Address:** flow-steps [test] `test.exit`; architecture-v2 [chain] dWitnessedBar row
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:** `test.exit` records "the verified tree on the build's lease record", and Test's exit needs "the verified tree is on the build's lease record". layer-memory: "| lease | dPlacedRequest |". dWitnessedBar's only parent is dDeclaredLoop, and the design map puts dPlacedRequest after dDeclaredLoop, not before dWitnessedBar. No stand-in is declared.
- **Consequence:** When dWitnessedBar is specced and built, its exit item writes into a record kind no ancestor provides, and dShippedRelease's landing order reads it later.
- **Fix:** Declare a stand-in (for example, the verified tree on the transition record until dPlacedRequest lands), or add dPlacedRequest to dWitnessedBar's parents.

| item | scenario | actor | needs | witness | route | verdict |
|---|---|---|---|---|---|---|
| `test.merge` | S1 | = | = | = | = | holds |
| `test.merge` | S2 | = | = | = | = | holds |
| `test.merge` | S3 | = | = | = | = | holds |
| `test.merge` | S4 | = | = | = | = | holds |
| `test.merge` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.merge` | S6 | = | = | = | refused → an ask with no re-entry | B3-F8 |
| `test.merge` | S7 | = | = | = | = | holds |
| `test.select` | S1 | = | = | = | = | holds |
| `test.select` | S2 | = | = | = | = | holds |
| `test.select` | S3 | = | = | = | = | holds |
| `test.select` | S4 | = | = | = | = | holds |
| `test.select` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.select` | S6 | = | = | = | = | holds |
| `test.select` | S7 | = | = | = | = | holds |
| `test.verdict` | S1 | = | = | = | = | holds |
| `test.verdict` | S2 | = | = | remote-ci verdict with no pin or trust clause | = | B3-F6 |
| `test.verdict` | S3 | = | = | = | = | holds |
| `test.verdict` | S4 | = | = | = | = | holds |
| `test.verdict` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.verdict` | S6 | = | = | = | = | holds |
| `test.verdict` | S7 | = | = | = | = | holds |
| `test.route` | S1 | = | = | = | MIXED under own-only routes two ways | B3-F7 |
| `test.route` | S2 | = | = | = | = | holds |
| `test.route` | S3 | = | = | = | = | holds |
| `test.route` | S4 | = | = | = | = | holds |
| `test.route` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.route` | S6 | = | = | = | = | holds |
| `test.route` | S7 | = | = | = | = | holds |
| `test.attribute` | S1 | = | = | = | = | holds |
| `test.attribute` | S2 | = | = | = | = | holds |
| `test.attribute` | S3 | = | = | = | = | holds |
| `test.attribute` | S4 | = | = | = | = | holds |
| `test.attribute` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.attribute` | S6 | = | = | = | = | holds |
| `test.attribute` | S7 | = | = | = | = | holds |
| `test.flakes` | S1 | = | = | = | = | holds |
| `test.flakes` | S2 | = | = | = | = | holds |
| `test.flakes` | S3 | = | = | = | = | holds |
| `test.flakes` | S4 | = | = | = | = | holds |
| `test.flakes` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.flakes` | S6 | = | = | = | = | holds |
| `test.flakes` | S7 | = | = | = | = | holds |
| `test.seen-red` | S1 | = | = | record written by the checker itself | = | B3-F1 |
| `test.seen-red` | S2 | = | = | record written by the checker itself | = | B3-F1 |
| `test.seen-red` | S3 | = | = | record written by the checker itself | = | B3-F1 |
| `test.seen-red` | S4 | = | = | record written by the checker itself | = | B3-F1 |
| `test.seen-red` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.seen-red` | S6 | = | = | record written by the checker itself | = | B3-F1 |
| `test.seen-red` | S7 | = | = | record written by the checker itself | = | B3-F1 |
| `test.recommend` | S1 | = | = | = | = | holds |
| `test.recommend` | S2 | = | = | = | = | holds |
| `test.recommend` | S3 | = | = | = | = | holds |
| `test.recommend` | S4 | = | = | = | = | holds |
| `test.recommend` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.recommend` | S6 | = | = | = | = | holds |
| `test.recommend` | S7 | = | = | = | = | holds |
| `test.reason` | S1 | = | = | = | = | holds |
| `test.reason` | S2 | = | = | = | = | holds |
| `test.reason` | S3 | = | = | = | = | holds |
| `test.reason` | S4 | = | = | = | = | holds |
| `test.reason` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.reason` | S6 | = | = | = | = | holds |
| `test.reason` | S7 | = | = | = | = | holds |
| `test.exit` | S1 | = | = | = | = | holds |
| `test.exit` | S2 | = | = | = | = | holds |
| `test.exit` | S3 | = | = | = | = | holds |
| `test.exit` | S4 | = | = | = | = | holds |
| `test.exit` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Test |
| `test.exit` | S6 | = | = | = | = | holds |
| `test.exit` | S7 | = | = | lease record of a non-ancestor build | = | B3-F13 |
| `deploy.current` | S1 | = | = | = | = | holds |
| `deploy.current` | S2 | = | = | = | = | holds |
| `deploy.current` | S3 | = | = | = | = | holds |
| `deploy.current` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.current` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.current` | S6 | = | = | = | = | holds |
| `deploy.current` | S7 | = | = | = | = | holds |
| `deploy.mandate` | S1 | = | = | intake record, or a supervisor-written gate choice | = | B3-F4, B3-F11 |
| `deploy.mandate` | S2 | = | = | = | = | holds |
| `deploy.mandate` | S3 | = | = | rendered Maintain intake as mandate | = | B3-F11 |
| `deploy.mandate` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.mandate` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.mandate` | S6 | = | = | = | = | holds |
| `deploy.mandate` | S7 | = | = | = | = | holds |
| `deploy.parents` | S1 | = | = | = | = | holds |
| `deploy.parents` | S2 | = | = | = | holds with no deadline | B3-F5 |
| `deploy.parents` | S3 | = | = | = | = | holds |
| `deploy.parents` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.parents` | S5 | = | = | = | Y holds past its deadline with no outcome | B3-F5 |
| `deploy.parents` | S6 | = | = | = | = | holds |
| `deploy.parents` | S7 | = | = | = | = | holds |
| `deploy.land` | S1 | = | = | = | = | holds |
| `deploy.land` | S2 | = | landing.order unread | = | = | B3-F10 |
| `deploy.land` | S3 | = | = | = | = | holds |
| `deploy.land` | S4 | = | = | = | = | holds |
| `deploy.land` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.land` | S6 | = | = | = | carried commit or argument → an ask with no re-entry | B3-F8 |
| `deploy.land` | S7 | = | = | = | = | holds |
| `deploy.core` | S1 | = | = | = | = | holds |
| `deploy.core` | S2 | = | = | = | = | holds |
| `deploy.core` | S3 | = | = | = | red → close after filing; patch has no budget link | B3-F2, B3-F3 |
| `deploy.core` | S4 | = | = | = | = | holds |
| `deploy.core` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.core` | S6 | = | = | = | = | holds |
| `deploy.core` | S7 | = | = | = | = | holds |
| `deploy.record` | S1 | = | = | = | = | holds |
| `deploy.record` | S2 | = | = | = | = | holds |
| `deploy.record` | S3 | = | = | = | = | holds |
| `deploy.record` | S4 | = | = | = | = | holds |
| `deploy.record` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.record` | S6 | = | = | = | = | holds |
| `deploy.record` | S7 | = | = | = | = | holds |
| `deploy.distill` | S1 | = | = | = | = | holds |
| `deploy.distill` | S2 | = | = | = | = | holds |
| `deploy.distill` | S3 | = | = | = | patch route carries no originating budget | B3-F3 |
| `deploy.distill` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.distill` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.distill` | S6 | = | = | = | = | holds |
| `deploy.distill` | S7 | = | rows from a non-ancestor build | empty join reads green | = | B3-F12 |
| `deploy.recommend` | S1 | = | = | = | = | holds |
| `deploy.recommend` | S2 | = | = | = | = | holds |
| `deploy.recommend` | S3 | = | = | = | = | holds |
| `deploy.recommend` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.recommend` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build and never reaches Deploy |
| `deploy.recommend` | S6 | = | = | = | = | holds |
| `deploy.recommend` | S7 | = | = | = | = | holds |
| `deploy.notify` | S1 | = | = | = | = | holds |
| `deploy.notify` | S2 | = | = | = | = | holds |
| `deploy.notify` | S3 | = | = | = | = | holds |
| `deploy.notify` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.notify` | S5 | = | = | = | = | not on path: a withdrawal posts through life.notify |
| `deploy.notify` | S6 | = | = | = | unreachable remote re-dispatch draws budget | B3-F9 |
| `deploy.notify` | S7 | = | = | = | = | holds |
| `deploy.released` | S1 | = | = | = | = | holds |
| `deploy.released` | S2 | = | = | = | = | holds |
| `deploy.released` | S3 | = | = | = | = | holds |
| `deploy.released` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.released` | S5 | = | = | = | = | not on path: X is withdrawn mid-Build, before any push |
| `deploy.released` | S6 | = | = | = | = | holds |
| `deploy.released` | S7 | = | = | = | = | holds |
| `deploy.snapshot` | S1 | = | = | = | = | holds |
| `deploy.snapshot` | S2 | = | = | = | = | holds |
| `deploy.snapshot` | S3 | = | = | = | = | holds |
| `deploy.snapshot` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.snapshot` | S5 | = | = | = | = | not on path: a withdrawal snapshots through life.snapshot |
| `deploy.snapshot` | S6 | = | = | = | unreachable remote re-dispatch draws budget | B3-F9 |
| `deploy.snapshot` | S7 | = | = | = | = | holds |
| `deploy.unlease` | S1 | = | = | = | = | holds |
| `deploy.unlease` | S2 | = | = | = | = | holds |
| `deploy.unlease` | S3 | = | = | = | = | holds |
| `deploy.unlease` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.unlease` | S5 | = | = | = | = | not on path: a withdrawal releases leases through life.unlease |
| `deploy.unlease` | S6 | = | = | = | unreachable remote re-dispatch draws budget | B3-F9 |
| `deploy.unlease` | S7 | = | = | = | = | holds |
| `deploy.close` | S1 | = | = | = | = | holds |
| `deploy.close` | S2 | = | = | = | = | holds |
| `deploy.close` | S3 | = | = | = | closes with its own core red open | B3-F2 |
| `deploy.close` | S4 | = | = | = | = | not on path: the adopter's update runs as kits.update outside any build |
| `deploy.close` | S5 | = | = | = | = | not on path: a withdrawal closes through life.close |
| `deploy.close` | S6 | = | = | = | unreachable remote re-dispatch draws budget | B3-F9 |
| `deploy.close` | S7 | = | = | = | = | holds |

| dWitnessedBar | B3-F1, B3-F6, B3-F7, B3-F8, B3-F13 |
|---|---|
| dShippedRelease | B3-F2, B3-F3, B3-F4, B3-F5, B3-F8, B3-F9, B3-F10, B3-F11, B3-F12 |
| dSafePassage | holds |
| dConvergedCharter | holds |

| P2 | B3-F1, B3-F4 |
|---|---|
| P3 | B3-F6 |
| P8 | holds |
| P9 | holds |
| P16 | B3-F2 |
| P37 | holds |
| P38 | holds |
| P42 | holds |

**Read outside the list above:**
- **Working-tree records, read before I took up the brief's read rule:**
  - `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, the round record, read whole.
  - The sibling briefs `...-walk-brief-a3.md`, `-b1.md`, `-b2.md`, `-b4.md` and `-b5.md` in the same folder, diffed against this brief.
  - Listings of that folder and of `memory/builds/dClosedLoop/reviews/`.
- **Lines from excluded records in the copy:**
  - A grep across the copy's `build/*.md` for floor statements printed one session-log line (`...-session-log.md:177`).
  - Other greps there filtered the compared, instruments and session-log records out of what they printed, but did search those files.
- **Brief defect:** the return's six-part order has no slot for the FMEA and STRIDE readings that steps 3 and 4 require, so this walk carries them only inside its findings.

Everything else I read was within the brief's list. My probes wrote only to `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-b3/`: `cl.py`, a clause extractor, and four clause dumps (`wb.txt`, `sr.txt`, `sp.txt`, `cc.txt`).
