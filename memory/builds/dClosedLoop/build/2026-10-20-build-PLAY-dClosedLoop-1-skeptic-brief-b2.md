# Skeptic brief: run B, batch 2

**Serves:** research PLAY-dClosedLoop-1

**Your task is to refute each finding below, and then to break each clean cell after them.** This brief is your
instructions, not the subject of your review: do not review it, the audit's seal or its instruments. A defect you see
in them goes in one line at the end of your return, and nowhere else.

You are one of four skeptics in run B of the whole-design audit (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, whose `[rubric]` grades
what you confirm). Each finding below was returned by a walker reading the sealed copy of the design at
`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Then try to break each clean cell listed after them, a
cell a walker judged to hold.

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b2/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

### B4-F4 — `review.dispose` routes by two artifact states, while a breakpoint pins four artifacts
- **Address:** flow-steps [breakpoint] `review.dispose`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - `review.pin` pins "the plan revision, the spec revisions, the commit range or the landing record".
  - `review.dispose` routes only "On an unbuilt spec ... On built work, they become new units or asks by `review.findings`".
  - [deploy] Breakpoints: the landing review's "findings enter as patch builds by the entry-point table's post-close row". [transitions] allows `designing` only "before the push".
- **Consequence:** A Plan review's findings have no route. A landing review's findings are disposed as new units of a build that has already landed, a transition the table lacks.
- **Fix:** Add an arm per artifact: plan revision goes to `plan.record` for revision, and the landing record goes to a patch-build intake by the post-close row.

### B4-F3 — The breakpoint program has no route for a CEILING or NON-CONVERGENT round
- **Address:** flow-steps [breakpoint] `review.fold`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - `review.fold` routes "the next round as `review.design.rounds` says, or released". `review.dispose` routes "a follow-up round as `review.follow-up` says".
  - `grep -n "max-rounds\|NON-CONVERG\|CEILING"` over flow-steps hits only line 703, the driver's old loop states. The [breakpoint] policy list leaves out `review.max-rounds`.
  - v2 `cl-dClosedLoop-0117`: "the round after the limit refused and the report reading CEILING ... findings ... promoted, to units while budget remains and to asks after, never folded".
- **Consequence:** At S6's "review at its CEILING" the item table, which is the draft the loop definition declares and which `cl-dClosedLoop-0118`'s static check reads, has no outcome for the refused round. The default refusal route re-dispatches it, and it ends only through B4-F2's missing exhaustion state.
- **Fix:** Give `review.fold` and `review.dispose` the outcomes CEILING and NON-CONVERGENT, routing to promotion (units while budget remains, asks after). Add `review.max-rounds` and `flow.rework-budget` to the [breakpoint] policy list.

### B4-F11 — dFairHearing's breakpoint items rest on later builds with no stand-in
- **Address:** flow-steps [breakpoint] `review.pin`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - `review.pin` (dFairHearing) chooses `design-audit` "by the record-kind registry", which is dTotalRecall's and later in the chain.
  - `review.report` (dFairHearing) claims `new:` slugs "by a compare-and-swap ref ... as `entry.claim` claims", which is dPlacedRequest's and later.
  - Stage 0's lead: "dFairHearing→review.dispose: order: routes `review.dispose`, dDeclaredLoop's, not an ancestor, UNCLASSED".
- **Consequence:** When dFairHearing lands, its preset choice, its slug claim and its next route all name parts that do not exist yet.
- **Fix:** Declare stand-ins in [breakpoint] as [probe] does: a record kind read from the filename, a `new:` slug checked locally, and disposition by hand until dDeclaredLoop. Class the lead in `[stage0-classes]`.

### B2-F6 — "A fix pass" and "a revert pass" are no items, so their allowance attaches nowhere
- **Address:** flow-steps [build] `build.acceptance` (also `build.scope`, `build.reuse-check`, and [test] "A fix pass keeps its check")
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **Evidence:** `build.acceptance` Then: "fail → a fix pass". `build.scope`: "routes to a revert pass on the unit". [test]: "A fix pass's allowance excludes the red leg's own test files … (M16)". No row declares a fix or revert pass, and P24 says "Every action that changes state belongs to an item".
- **Consequence:** At S6's red unit, the engine has no tag to put on the frontier. M16's narrowed allowance has no item to render into a work order, and the budget draw is attached to no instance.
- **Fix:** Declare `build.fix-pass` (builder, with Needs that name the red record, the allowance minus the red check's files and the acceptance files, and Then `build.acceptance`) and a revert pass as its own value or item. Then route every "fix pass" to that tag.

### B2-F18 — A re-entered Build lap owes a full closing review outside `review.follow-up`
- **Address:** flow-steps [build] `build.recommend`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Evidence:** `build.recommend` Then: "the closing review where owed". v2 [policies]: "`review.<stage>` … opt-in; Build owed". [build]: "a follow-up round runs after a HIGH finding (`review.follow-up`)". The findings' units return through Design to `build.recommend`.
- **Consequence:** Every lap owes a new full closing review, whatever `review.follow-up` (`after-high`, `never`) says. CEILING and NON-CONVERGENT are then counted across unrelated reviews.
- **Fix:** On a lap whose units came from a closing review's findings, make `build.recommend` route to that review's follow-up as `review.follow-up` says, never to a fresh owed review.

### B2-F2 — Build's tail after `build.reuse-check` is reached from no entry
- **Address:** flow-steps [build] `build.recommend` (and `build.reuse-check`'s Then cell)
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S1
- **Evidence:** `build.reuse-check` Then: "clean → the unit built". `build.recommend` Needs: "every unit built and reuse-checked", which is prose and names no item. stage0-leads.md K2: "build.recommend: reached from no entry", and the same for `build.ratify`, `build.distill`, `build.core` and `build.exit`.
- **Consequence:** The engine computes position from item tags (P22, P24). No item routes to `build.recommend`, and its need resolves to no witness, so the frontier never contains it. S1 cannot reach `build.exit`, Test or `deploy.close` through the declared program.
- **Fix:** Give `build.reuse-check`'s clean outcome the target `build.recommend`, and write its Needs as "`build.reuse-check` for every unit in the roster", a quantified tag the join resolves. Re-run Stage 0's K2 until those five leads clear.

### B2-F8 — Only the starting units' leases are taken by any item
- **Address:** flow-steps [build] `build.unit-lease`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** `build.unit-lease` "takes each starting unit's lease", Needs `build.base` (one instance). `build.scope`: "in scope → the unit's next pass, or, its last pass done, `build.reuse-check`".
- **Consequence:** A unit that starts later in declared order has no item that leases it. In S2 a node can claim it as "ready, unleased" while node d's queue also starts it.
- **Fix:** Make `build.unit-lease` per unit, with Needs that are the unit's predecessors in declared order, so each unit is leased as it becomes ready.

### B3-F10 — `landing.order` is never read, so strict's `owner-orders` does nothing
- **Address:** flow-steps [deploy] (landing order); architecture-v2 [chain] `cl-dClosedLoop-0422`
- **Class:** K4
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** flow-steps: "Landings on a node are ordered by `landing.order`". No item's Does cell reads it, and `cl-dClosedLoop-0422` says only "landings ordered through the landing queue it builds". Stage 0's K4 lead: "landing.order: read by no chain clause and no item". The strict preset sets `owner-orders`.
- **Consequence:** In S2, when X and Y verify at once, the landing order is whatever the queue does. Strict's `owner-orders` is silently ignored.
- **Fix:** Have `cl-dClosedLoop-0422` read `landing.order` with an arm for each value, and `deploy.land` need the queue's admission. Seed a red case: an `owner-orders` landing admitted with no order.

### B3-F2 — A core red at landing lets the build close once a patch is filed
- **Address:** flow-steps [deploy] `deploy.core`; architecture-v2 [chain] `cl-dClosedLoop-0423`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S3
- **Evidence:** `deploy.core`: "red → a patch build through the entry-point table's post-close row, and the close waits for its filing". v2's opening revision: "a core red that first appears in the landing merge still stops that build from closing". `cl-dClosedLoop-0423`: "so a core red the landing merge introduced stops that build from closing (foundations K1)". P16: "A violation the bypass let through stops the build that made it from closing".
- **Consequence:** In S3 the originating build reaches `deploy.close` and `landed` as soon as the patch is filed. The owner's K1 rule ("the violator pays") is loosened at the item that implements it. The originating build is closed before its patch lands, which also takes away the budget owner that F3 needs.
- **Fix:** Make `deploy.core`'s red route hold `deploy.close` until the patch build's `deploy.core` is green for a SHA that contains the landed one, or an owner exception (`core.exceptions`). Add a matching transitions row.

### B3-F12 — `deploy.distill` can pass on an empty join before dScopedBuild lands
- **Address:** flow-steps [deploy] `deploy.distill`; architecture-v2 [chain] dShippedRelease row
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **Evidence:** `deploy.distill` "confirms that the decision-log rows `build.distill` wrote are in the log", joined to "the build's major forks". `build.distill` belongs to dScopedBuild, and fork classes to dIndexedDesign. The design map gives dShippedRelease the parents "dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine, dLinkedLibrary, dFurnishedOrders", which include neither of those builds or their descendants.
- **Consequence:** dShippedRelease can land first. Its `deploy.distill` would then join zero classed forks to zero rows and pass, counting an empty population as coverage.
- **Fix:** Add dScopedBuild to dShippedRelease's parents. Or declare that `deploy.distill` reports "measured nothing" and never passes until `build.distill`'s writer lands, seen red on an empty population.

### B3-F11 — `deploy.mandate` reads the intake record as the plan-only mandate
- **Address:** flow-steps [deploy] `deploy.mandate`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** `deploy.mandate`'s witness is "the intake record, or the gate's witness" ("the request's mandate under `plan-only`"). v2's revision of 2026-10-14: under `plan-only`, "the owner's plan ratification is the mandate". flow-steps [plan]: only under `plan.ratification: request` is the request the ratification. A triage-selected build has no intake record, and gap-flow-14 lists "Maintain's agent-typed intake becomes a patch build's mandate".
- **Consequence:** The landing's authority comes from the wrong record. A ratified plan is not checked. An ask-selected build has no witness. An S3 patch from Maintain is mandated by a rendered intake, which is the defect gap-flow-14 records.
- **Fix:** Witness the mandate per entry: the `plan.exit` ratification (its disposition, or the request under `request`), the triage record for a select, and `patch.ratify`'s disposition for a patch.

### B3-F4 — The owner's landing gate can be passed by the supervisor's own choice
- **Address:** flow-steps [deploy] `deploy.mandate`; flow-steps [breakpoint]; architecture-v2 [policies] `run.on-owner-question`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:** `deploy.mandate` checks, "under `three-gates` and `every-stage`, the disposition of the owner's landing gate". [breakpoint]: an owner breakpoint is resolved by `run.on-owner-question` "when it is raised, never for a ratification ... the supervisor's recorded choice under `best-effort-recorded`". The witness list includes "under `best-effort-recorded`, the supervisor's recorded choice". `best-effort-recorded` is the default, and it is the `run.on-owner-question` value in every preset except strict (park-item).
- **Consequence:** An owner who sets `autonomy: three-gates` to gate landings gets a gate the supervisor fills in as soon as it is raised. `deploy.mandate` then certifies an owner mandate that the acting side typed, which breaks P2.
- **Fix:** Treat the design go and the landing gate like ratifications: `run.on-owner-question` and `apply-recommendation` never decide them. Make `deploy.mandate` refuse a gate witness that is not an owner disposition. Seed a red case: a planted `best-effort-recorded` choice offered as the gate's witness.

### B3-F9 — After the push, an unreachable remote spends the rework budget
- **Address:** flow-steps [deploy] `deploy.notify`, `deploy.snapshot`, `deploy.unlease`, `deploy.close`; flow-steps [rules]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Evidence:** Of these four items only `deploy.land` declares "the remote unreachable → the supervisor's retry, then an owner item". The other four each write to the remote (mailbox posts, the snapshot commit, tombstones, the transition under the claim ref) and declare no unreachable route. [rules]: "A re-dispatch of a refused instance draws on the build's rework budget". Only contention draws nothing.
- **Consequence:** In S6, a remote outage after the push re-dispatches these items against the budget of a build that has already landed. When the budget runs out, `flow.on-exhausted`'s endings (descope, close-incomplete) are applied to landed work.
- **Fix:** Class an unreachable remote as contention for every command item: a retry that draws nothing, then an owner item at `flow.wait-ceiling`, as `deploy.land` already does.

### B3-F5 — A parent hold has no deadline and no outcome
- **Address:** flow-steps [deploy] `deploy.parents`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S5
- **Evidence:** `deploy.parents`: "a parent unlanded or paused → holds", with no deadline. v2's `flow.wait-ceiling` names "a dependency hold ... past which the waiter takes its declared outcome". Stall-and-loop item 6: "dependency and mailbox waits: past their deadline, the waiter takes its declared default (replan ...)". `cl-dClosedLoop-0118` reds any wait that does not declare an outcome and a deadline. `cl-dClosedLoop-0328` releases dependents only on a wait cycle or when a parent ends incomplete.
- **Consequence:** If Y's parent X is alive but stalled or paused (a paused build's leases are renewed), Y waits at `deploy.parents` forever. The S5 probe "Y's wait outlasting its deadline" reaches no terminal, and gov's own item fails the design's own static termination check.
- **Fix:** Change `deploy.parents`' hold to "holds until `flow.wait-ceiling`, then as `deps.on-parent-withdrawn` says, with an owner item". Make it a counted wait with its witness.

### B2-F9 — A parent's `withdrawn` or `superseded` notice has no route before `deploy.parents`
- **Address:** flow-steps [design] `design.decompose` (policy lists of [design] and [build])
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Evidence:** `life.notify` "posts `withdrawn` or `superseded` to dependents". `deps.on-parent-withdrawn` (replan by default) is read only at [deploy] `deploy.parents`. Neither the [design] nor the [build] policy list names it, and `design.reentry`'s triggers are interface-change, review-cross-unit-flaw and planner-or-owner-flag.
- **Consequence:** Y reads the notice at an item boundary (`mailbox.reads`), but no route acts on it. Y keeps designing and building on X's withdrawn interface until Deploy, and then replans, spending its budget and leases.
- **Fix:** Route a parent's `withdrawn` or `superseded` notice read at any item boundary to `deps.on-parent-withdrawn` there, with replan going to `design.reentry`. Add the key to Design's and Build's policy lists.

### B2-F20 — A patch build skips the overlap check against live builds
- **Address:** flow-steps [design] `design.input`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** `design.input`: "patch → `design.unit-spec`, as a micro-spec". `design.unit-spec` Needs "… or the input's unit". `design.overlaps` "runs the design index over the roster's write sets, against live builds".
- **Consequence:** A patch's write set is never checked against live builds. The collision first shows at `build.unit-lease`, which only warns (`leases.overlap`), or at Test's merge conflict.
- **Fix:** Route patch, finding and fix inputs through `design.overlaps` for their unit before `design.unit-spec`.

### B2-F5 — A superseding build never reaches `design.inventory`, so the kept work has no route
- **Address:** flow-steps [design] `design.input` (and [lifecycle]'s kept-work rule)
- **Class:** K2, c4
- **Severity:** high
- **Scenario:** S5
- **Evidence:** [lifecycle]: "A superseded build's kept work passes to its replacement through the replacement's `design.inventory`." `design.input`: "plan record → `design.seams`; … plan revision → `design.inventory`". `design.inventory`: "after a plan revision".
- **Consequence:** Z enters Design with a ratified plan record and goes to `design.seams`. No input kind or route takes Z to `design.inventory`, so X's built units are never given kept, amended or retired verdicts in Z. Built work drops out of the trail.
- **Fix:** Add a `supersession` input kind, the replacement's plan record naming the build it supersedes, which `design.input` routes to `design.inventory` over the superseded build's built units. Add its row to [transitions].

### B2-F3 — Two of Design's guard keys are read by no item
- **Address:** flow-steps [design] `design.overlaps` and `design.ready`
- **Class:** K4, c3
- **Severity:** high
- **Scenario:** S2
- **Evidence:** v2 [policies]: "`design.overlap` | warn, refuse, index-only | warn" and "`design.handoff` | derived-ready, ready-plus-audit, status-and-tier | derived-ready". `design.overlaps` Then: "`design.streams` where … else `design.unit-spec`", with no per-value route. `design.ready` reads only "derived READY: none MISSING, THIN or FORKED". stage0-leads.md K4: "design.overlap: read by no chain clause and no item (guard-bearing)" and "design.handoff: read by no chain clause and no item".
- **Consequence:** In S2, X and Y overlap across nodes. An owner who sets `design.overlap: refuse` still gets `design.unit-spec`, and one who sets `ready-plus-audit` gets READY with no audit. The key silently loosens to its weakest value.
- **Fix:** Give `design.overlaps` a route for each value (refuse → back to `design.decompose` with the overlap record) and `design.ready` an arm for `ready-plus-audit` and `status-and-tier`. Have dIndexedDesign's row (`cl-dClosedLoop-0384`, `-0383`) name both keys, each seen red on its planted value.

### B2-F19 — `design.ready`'s witness lacks the UNCARRIED class its clause adds
- **Address:** flow-steps [design] `design.ready`
- **Class:** K6
- **Severity:** low
- **Scenario:** S7
- **Evidence:** `design.ready` witness: "none MISSING, THIN or FORKED". `cl-dClosedLoop-0398`: "`design.ready` gaining an UNCARRIED class".
- **Consequence:** A spec writer working from the item draft leaves out the coverage arm.
- **Fix:** Add UNCARRIED, under `design.coverage`, to the item's witness.

## Clean cells to attack

- `deploy.land` in S7
- `life.request` in S7
- `plan.input` in S7
- `review.refute` in S5
- `release.approve` in S7
- `test.reason` in S4
- `life.close` in S7
- `deploy.mandate` in S2

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <item> <scenario>: holds`, or `- <item> <scenario>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `BS2-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-b2/` only. Your effort is the one the owner's
role definition sets.
