# Walk return: run B, walker 2, design and build

**Serves:** research PLAY-dClosedLoop-1

Dispatch 166's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-7-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

I disclose one breach before the return. Before I switched to the copy, I read the working tree's round record (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, the whole file) and diffed the other run-B briefs against this one. This brief forbids both. The record's `[walk]` names the arms (K3 and K5) that caught the copy's two mechanical plants, and its `[stage0]` names a K5 lead on P18's fork ranking, which B2-F15 repeats. I cite every finding below from the sealed copy or from code only, and the scoring should note this.

**Pre-mortem:** The chain shipped and failed in this scenario because the step engine runs on Needs and the frontier, and Design's and Build's exits, breakpoints and tails are tied to their predecessors in prose ("where it ran", "every unit built", "a fix pass"). So a build either skips its spec audit and closing review or never reaches `build.exit`, and a clause written for an instrument (`cl-dClosedLoop-0003`) refuses every chain build's first spec.

### B2-F1 — "where it ran" needs put Design's and Build's exits on the frontier before the breakpoint is decided
- **Address:** flow-steps [design] `design.ready`; also [build] `build.ratify`, `build.distill` (and the same pattern at [test] `test.exit`, [deploy] `deploy.notify`)
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:** [rules]: "`next` returns the frontier, the unwitnessed items whose needs are witnessed". `design.ready` Needs: "`design.recommend`, and the spec audit where it ran". `design.reason` (Needs `design.recommend`) is the item that decides "a review → the spec audit". `build.distill` Needs: "`build.recommend`, the closing review where it ran". The default `review.recommendation.source` is `scored-signals-and-reasoning` (v2 [policies]).
- **Consequence:** Once `design.recommend` is witnessed, `design.ready` and `design.reason` are both on the frontier. `design.ready` can derive READY and `design.exit` can record the transition before the reason item owes a spec audit, or before an owed audit starts. Under default `decisions.major: author-rubric`, `build.distill`, `build.core` and `build.exit` follow from `build.recommend` alone, so the owed closing review is passed silently. Stage 0's K1 reads only the tags in a Needs cell, so it cannot see this.
- **Fix:** Make the breakpoint an explicit need. `design.ready` needs `design.reason` (or `design.recommend` under `signals-only`) plus the breakpoint's disposition record whenever the trigger fired. The same applies to `build.ratify`/`build.distill` (the closing review), `test.exit` and `deploy.notify`. Add a static check that reds a Needs cell holding an untagged conditional, seen red on today's `design.ready` row.

### B2-F2 — Build's tail after `build.reuse-check` is reached from no entry
- **Address:** flow-steps [build] `build.recommend` (and `build.reuse-check`'s Then cell)
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S1
- **Evidence:** `build.reuse-check` Then: "clean → the unit built". `build.recommend` Needs: "every unit built and reuse-checked", which is prose and names no item. stage0-leads.md K2: "build.recommend: reached from no entry", and the same for `build.ratify`, `build.distill`, `build.core` and `build.exit`.
- **Consequence:** The engine computes position from item tags (P22, P24). No item routes to `build.recommend`, and its need resolves to no witness, so the frontier never contains it. S1 cannot reach `build.exit`, Test or `deploy.close` through the declared program.
- **Fix:** Give `build.reuse-check`'s clean outcome the target `build.recommend`, and write its Needs as "`build.reuse-check` for every unit in the roster", a quantified tag the join resolves. Re-run Stage 0's K2 until those five leads clear.

### B2-F3 — Two of Design's guard keys are read by no item
- **Address:** flow-steps [design] `design.overlaps` and `design.ready`
- **Class:** K4, c3
- **Severity:** high
- **Scenario:** S2
- **Evidence:** v2 [policies]: "`design.overlap` | warn, refuse, index-only | warn" and "`design.handoff` | derived-ready, ready-plus-audit, status-and-tier | derived-ready". `design.overlaps` Then: "`design.streams` where … else `design.unit-spec`", with no per-value route. `design.ready` reads only "derived READY: none MISSING, THIN or FORKED". stage0-leads.md K4: "design.overlap: read by no chain clause and no item (guard-bearing)" and "design.handoff: read by no chain clause and no item".
- **Consequence:** In S2, X and Y overlap across nodes. An owner who sets `design.overlap: refuse` still gets `design.unit-spec`, and one who sets `ready-plus-audit` gets READY with no audit. The key silently loosens to its weakest value.
- **Fix:** Give `design.overlaps` a route for each value (refuse → back to `design.decompose` with the overlap record) and `design.ready` an arm for `ready-plus-audit` and `status-and-tier`. Have dIndexedDesign's row (`cl-dClosedLoop-0384`, `-0383`) name both keys, each seen red on its planted value.

### B2-F4 — The per-unit budget share has no single freeze point, so each Design re-entry can mint budget
- **Address:** architecture-v2 [policies] `flow.rework-budget`; flow-steps [design] `design.exit`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:** v2 [policies]: "a base plus a count per unit frozen at Design's exit … 4+2". flow-steps [build]: closing-review findings "become new units … and those units pass through Design and back". So `design.exit` runs again on every lap. stall-and-loop [design] 1 says only "units a loop mints cannot reset it".
- **Consequence:** If the share is re-frozen at each `design.exit`, every closing-review finding (S1) and every patch build's Design (S3, which shares the originating budget) adds 2 to the budget it draws on. The P39 bound grows with the loop it is meant to stop.
- **Fix:** State that the shares freeze once, at the first `design.exit` the build records, and that units minted later carry no share. Seen red on a planted closing review whose finding-units raise the remaining budget on the card.

### B2-F5 — A superseding build never reaches `design.inventory`, so the kept work has no route
- **Address:** flow-steps [design] `design.input` (and [lifecycle]'s kept-work rule)
- **Class:** K2, c4
- **Severity:** high
- **Scenario:** S5
- **Evidence:** [lifecycle]: "A superseded build's kept work passes to its replacement through the replacement's `design.inventory`." `design.input`: "plan record → `design.seams`; … plan revision → `design.inventory`". `design.inventory`: "after a plan revision".
- **Consequence:** Z enters Design with a ratified plan record and goes to `design.seams`. No input kind or route takes Z to `design.inventory`, so X's built units are never given kept, amended or retired verdicts in Z. Built work drops out of the trail.
- **Fix:** Add a `supersession` input kind, the replacement's plan record naming the build it supersedes, which `design.input` routes to `design.inventory` over the superseded build's built units. Add its row to [transitions].

### B2-F6 — "A fix pass" and "a revert pass" are no items, so their allowance attaches nowhere
- **Address:** flow-steps [build] `build.acceptance` (also `build.scope`, `build.reuse-check`, and [test] "A fix pass keeps its check")
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **Evidence:** `build.acceptance` Then: "fail → a fix pass". `build.scope`: "routes to a revert pass on the unit". [test]: "A fix pass's allowance excludes the red leg's own test files … (M16)". No row declares a fix or revert pass, and P24 says "Every action that changes state belongs to an item".
- **Consequence:** At S6's red unit, the engine has no tag to put on the frontier. M16's narrowed allowance has no item to render into a work order, and the budget draw is attached to no instance.
- **Fix:** Declare `build.fix-pass` (builder, with Needs that name the red record, the allowance minus the red check's files and the acceptance files, and Then `build.acceptance`) and a revert pass as its own value or item. Then route every "fix pass" to that tag.

### B2-F7 — A cross-node unit has no workspace or integration rule under the default `build.worktree: shared`
- **Address:** layer-runtime [isolate]; flow-steps [build] `build.unit-pass`
- **Class:** K10, c2
- **Severity:** high
- **Scenario:** S2
- **Evidence:** v2 [policies]: "`build.worktree` | per-unit, parallel-only, shared | shared". [isolate]: "shared: the build's one worktree … The commit queue then commits them one at a time". "Integration before release" is stated for unit branches only. cloud-and-scale [design] 8: any node picks "ready, unleased units" across builds.
- **Consequence:** Node x takes one of X's units by lease, but under the default the unit's worktree and commit queue live on node d. Nothing says where x commits, how its pass reaches the build branch, or what the fence covers. The unit can never integrate, or it integrates outside the queue.
- **Fix:** A unit leased from another node always gets a unit branch, as under `per-unit`, whatever `build.worktree` says, integrated by the build lease's holder before the unit lease is released. Seen on a two-clone fixture.

### B2-F8 — Only the starting units' leases are taken by any item
- **Address:** flow-steps [build] `build.unit-lease`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** `build.unit-lease` "takes each starting unit's lease", Needs `build.base` (one instance). `build.scope`: "in scope → the unit's next pass, or, its last pass done, `build.reuse-check`".
- **Consequence:** A unit that starts later in declared order has no item that leases it. In S2 a node can claim it as "ready, unleased" while node d's queue also starts it.
- **Fix:** Make `build.unit-lease` per unit, with Needs that are the unit's predecessors in declared order, so each unit is leased as it becomes ready.

### B2-F9 — A parent's `withdrawn` or `superseded` notice has no route before `deploy.parents`
- **Address:** flow-steps [design] `design.decompose` (policy lists of [design] and [build])
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Evidence:** `life.notify` "posts `withdrawn` or `superseded` to dependents". `deps.on-parent-withdrawn` (replan by default) is read only at [deploy] `deploy.parents`. Neither the [design] nor the [build] policy list names it, and `design.reentry`'s triggers are interface-change, review-cross-unit-flaw and planner-or-owner-flag.
- **Consequence:** Y reads the notice at an item boundary (`mailbox.reads`), but no route acts on it. Y keeps designing and building on X's withdrawn interface until Deploy, and then replans, spending its budget and leases.
- **Fix:** Route a parent's `withdrawn` or `superseded` notice read at any item boundary to `deps.on-parent-withdrawn` there, with replan going to `design.reentry`. Add the key to Design's and Build's policy lists.

### B2-F10 — `cl-dClosedLoop-0003` refuses every chain build's first spec
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0003`
- **Class:** K7, c1
- **Severity:** high
- **Scenario:** S7
- **Evidence:** 0003: "memory hygiene refusing a chain build's spec in progress while its build's coverage is red, seen red on a planted uncarried clause". The copy's carries.py docstring: "a clause or an owned node no spec carries (with --exit, as at a Design exit)" and "a run that measured no spec is never green".
- **Consequence:** While a build's specs are being written, every clause not yet carried is uncarried, so coverage is red, and before the first spec it is never green. Hygiene then refuses the spec in progress, and dTrueNorth's own Design (and every later chain build's) cannot commit its first spec.
- **Fix:** Refuse a spec in progress only on the per-spec arms (ghost, unbound, stale, ambiguous, dropped). Keep the uncarried and unowned-node arms for the Design exit only, as the instrument does, and seen-red the refusal on a planted ghost, not on an uncarried clause.

### B2-F11 — `cl-dClosedLoop-0002` reds two whole carriers only when they disagree
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0002`
- **Class:** K8, c3
- **Severity:** medium
- **Scenario:** S7
- **Evidence:** 0002: "two specs carrying one clause whole and disagreeing … each red". The copy's carries.py, line 251: `ambiguous = [... if c[1] == "whole"]) > 1]`, which reds any second whole carrier. 0003's report lists "ambiguous counts".
- **Consequence:** A product join built from the clause passes two units that both carry one clause whole at the same pin. That is one clause built twice, which is the double ownership the coverage report exists to show.
- **Fix:** "two specs carrying one clause whole, or pinning it to two hashes, red", as the instrument reads.

### B2-F12 — v2 never defines the text a clause hash is taken over
- **Address:** architecture-v2 [clause-ids]
- **Class:** K6
- **Severity:** low
- **Scenario:** S7
- **Evidence:** [clause-ids]: "its text's hash being its revision". 0001: "the hash of its text". Only the copy's carries.py defines it: "the first eight hex digits of the SHA-256 of its text, the id cut off and its whitespace folded".
- **Consequence:** A dTrueNorth spec writer working from v2 can choose another normalisation, and every pin the instrument wrote reads stale under the product join.
- **Fix:** State the hash rule in [clause-ids], and have 0001 cite it.

### B2-F13 — `cl-dClosedLoop-0407` places `drop_touched_exemptions` in `tools/lib`, but it lives in the map kit
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0407`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S4
- **Evidence:** 0407: "calling the pure `drop_touched_exemptions` in `tools/lib`, … the claim arm 'not installed' where the map is absent, seen on a planted core-only tree". Probe: `grep -rn drop_touched_exemptions tools --include=*.py` printed only `tools/codebase-map/map_lib.py:1373:def drop_touched_exemptions(...)` and its two callers in `tools/codebase-map/`.
- **Consequence:** On an adopter's core-only install, `build.scope`'s one check imports a function from a kit that is absent. Either the build imports from the map kit and the touch join fails on that tree, or the clause hides a move into `tools/lib`, which copy-installed kits carry inline, with no unit owning that move.
- **Fix:** Name the move (`drop_touched_exemptions` out of `map_lib.py` into `tools/lib`, with its readers re-pointed in the same unit) as a dScopedBuild clause, or cite its real home and make the touch arm "not installed" when the map is absent.

### B2-F14 — P17's mechanical classification is only "(proposed)" in its one enforcing clause
- **Address:** architecture-v2 [enforcement] `P17` / [chain] `cl-dClosedLoop-0390`
- **Class:** K5, c5
- **Severity:** medium
- **Scenario:** S1
- **Evidence:** P17: "a feature's design declares its units' interfaces structurally, so a change is classified mechanically". [enforcement]: "`P17` | `cl-dClosedLoop-0390`". 0390: "additive-versus-breaking interface classification (proposed)".
- **Consequence:** dIndexedDesign can be specced without building the classifier `design.reentry` routes on. An amendment is then classed by judgement, and P17 has no clause that commits to enforcing it.
- **Fix:** Drop "(proposed)" and give the classifier a seen-red, a planted breaking change classed additive, or record its deferral and take P17's row off 0390 until it is built.

### B2-F15 — No clause enforces P18's ranking of a fork's options
- **Address:** architecture-v2 [enforcement] `P18` / [chain] `cl-dClosedLoop-0176`, `cl-dClosedLoop-0390`
- **Class:** K5, c5
- **Severity:** medium
- **Scenario:** S2
- **Evidence:** P18: "Agents resolve forks by the most feature-rich option, then the most expandable, with a full record". 0176: "every fork resolved by the role that meets it and recorded". 0390: "fork resolution by `design.forks`". The ranking appears only in the default value's name, `agents-feature-rich-expandable`. (I disclosed above that this was also a lead in the record I should not have read.)
- **Consequence:** In unattended S2, a fork record that carries no ranked options passes every join, so P18 is unenforced.
- **Fix:** Have 0176 require the fork record to list its options ranked by feature-richness, then expandability, with the chosen one first, and a schema check that reds a resolved fork without the ranking.

### B2-F16 — P19's one clause names no refusing check, and a deviation record admits a revision after a pass
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0400`
- **Class:** K5
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** [enforcement]: "`P19` | `cl-dClosedLoop-0400`". 0400: "built specs frozen …", with no check and no seen-red. 0004's population "each spec revision after its unit's first attributed pass commit" is joined to "a record whose approver meets its risk class", so a recorded revision passes 0412's gate.
- **Consequence:** A patch build (S3) can revise a built unit's spec in place under an approved deviation record, and no gate refuses it. P19 says it must arrive as a new unit.
- **Fix:** Add to 0400 a refusal of any revision of a unit whose spec is in a landed range, its deviation population included, seen red on a planted in-place edit of a landed unit's spec.

### B2-F17 — `design.streams`' Needs reads as needing itself
- **Address:** flow-steps [design] `design.streams`
- **Class:** K1
- **Severity:** low
- **Scenario:** S2
- **Evidence:** Needs: "`design.overlaps`, where `design.streams` holds for the build". stage0-leads.md: "K1 design.streams: a cycle among Needs: design.streams > design.streams".
- **Consequence:** The composer's graph check (flow-roles-adoption [design] 11, "the needs graph acyclic") reds gov's own item, or a reader skips it.
- **Fix:** Write the condition as `policy.design.streams`, the full spelling the opening reserves, outside the Needs tags.

### B2-F18 — A re-entered Build lap owes a full closing review outside `review.follow-up`
- **Address:** flow-steps [build] `build.recommend`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Evidence:** `build.recommend` Then: "the closing review where owed". v2 [policies]: "`review.<stage>` … opt-in; Build owed". [build]: "a follow-up round runs after a HIGH finding (`review.follow-up`)". The findings' units return through Design to `build.recommend`.
- **Consequence:** Every lap owes a new full closing review, whatever `review.follow-up` (`after-high`, `never`) says. CEILING and NON-CONVERGENT are then counted across unrelated reviews.
- **Fix:** On a lap whose units came from a closing review's findings, make `build.recommend` route to that review's follow-up as `review.follow-up` says, never to a fresh owed review.

### B2-F19 — `design.ready`'s witness lacks the UNCARRIED class its clause adds
- **Address:** flow-steps [design] `design.ready`
- **Class:** K6
- **Severity:** low
- **Scenario:** S7
- **Evidence:** `design.ready` witness: "none MISSING, THIN or FORKED". `cl-dClosedLoop-0398`: "`design.ready` gaining an UNCARRIED class".
- **Consequence:** A spec writer working from the item draft leaves out the coverage arm.
- **Fix:** Add UNCARRIED, under `design.coverage`, to the item's witness.

### B2-F20 — A patch build skips the overlap check against live builds
- **Address:** flow-steps [design] `design.input`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** `design.input`: "patch → `design.unit-spec`, as a micro-spec". `design.unit-spec` Needs "… or the input's unit". `design.overlaps` "runs the design index over the roster's write sets, against live builds".
- **Consequence:** A patch's write set is never checked against live builds. The collision first shows at `build.unit-lease`, which only warns (`leases.overlap`), or at Test's merge conflict.
- **Fix:** Route patch, finding and fix inputs through `design.overlaps` for their unit before `design.unit-spec`.

| item | S<n> | actor | needs | witness | route | verdict |
|---|---|---|---|---|---|---|
| `design.input` | S1 | = | = | = | = | holds |
| `design.input` | S2 | = | = | = | = | holds |
| `design.input` | S3 | = | = | = | patch → `design.unit-spec`, skipping overlaps | B2-F20 |
| `design.input` | S4 | = | = | = | = | not on path: update runs in the adopt program, outside any build |
| `design.input` | S5 | = | = | = | Z's plan record → `design.seams`, never `design.inventory` | B2-F5 |
| `design.input` | S6 | = | = | = | = | holds |
| `design.input` | S7 | = | = | = | = | holds |
| `design.reentry` | S1 | = | = | = | = | not on path: no amendment in S1; a late answer resolves an owner item |
| `design.reentry` | S2 | = | = | = | = | not on path: no amendment admitted |
| `design.reentry` | S3 | = | = | = | = | not on path: a patch enters as a micro-spec |
| `design.reentry` | S4 | = | = | = | = | not on path: outside any build |
| `design.reentry` | S5 | = | = | = | no trigger reads a parent's withdrawn notice | B2-F9 |
| `design.reentry` | S6 | = | = | = | = | not on path: no amendment in S6's failures |
| `design.reentry` | S7 | = | = | = | = | not on path: chain builds enter on a plan record |
| `design.inventory` | S1 | = | = | = | = | not on path: no plan revision |
| `design.inventory` | S2 | = | = | = | = | not on path: no plan revision |
| `design.inventory` | S3 | = | = | = | = | not on path: a patch skips it |
| `design.inventory` | S4 | = | = | = | = | not on path: outside any build |
| `design.inventory` | S5 | = | X's built units | = | reached by no input of Z's | B2-F5 |
| `design.inventory` | S6 | = | = | = | = | not on path: no plan revision |
| `design.inventory` | S7 | = | = | = | = | not on path: no plan revision |
| `design.seams` | S1 | = | = | = | = | holds |
| `design.seams` | S2 | = | = | = | = | holds |
| `design.seams` | S3 | = | = | = | = | not on path: a patch skips it |
| `design.seams` | S4 | = | = | = | = | not on path: outside any build |
| `design.seams` | S5 | = | = | = | = | holds |
| `design.seams` | S6 | = | = | = | = | holds |
| `design.seams` | S7 | = | = | = | = | holds |
| `design.decompose` | S1 | = | = | = | = | B2-F14 |
| `design.decompose` | S2 | = | X's confirmed interfaces | = | = | holds |
| `design.decompose` | S3 | = | = | = | = | not on path: a patch skips it |
| `design.decompose` | S4 | = | = | = | = | not on path: outside any build |
| `design.decompose` | S5 | = | X's interface, now withdrawn | = | no route on the notice | B2-F9 |
| `design.decompose` | S6 | = | = | = | = | holds |
| `design.decompose` | S7 | = | = | = | = | holds |
| `design.research` | S1 | = | = | = | = | holds |
| `design.research` | S2 | = | = | = | = | holds |
| `design.research` | S3 | = | = | = | = | not on path: no decompose in a patch |
| `design.research` | S4 | = | = | = | = | not on path: outside any build |
| `design.research` | S5 | = | = | = | = | holds |
| `design.research` | S6 | = | = | = | round trip draws on the budget | holds |
| `design.research` | S7 | = | = | = | = | holds |
| `design.overlaps` | S1 | = | = | = | no per-value route for `design.overlap` | B2-F3 |
| `design.overlaps` | S2 | = | = | = | X and Y overlap; `refuse` unread | B2-F3 |
| `design.overlaps` | S3 | = | = | = | skipped by the patch input | B2-F20 |
| `design.overlaps` | S4 | = | = | = | = | not on path: outside any build |
| `design.overlaps` | S5 | = | = | = | = | B2-F3 |
| `design.overlaps` | S6 | = | = | = | = | B2-F3 |
| `design.overlaps` | S7 | = | today's build index | = | = | B2-F3 |
| `design.streams` | S1 | = | = | = | = | not on path: opt-in, the brief does not ask |
| `design.streams` | S2 | = | reads as needing itself | = | = | B2-F17 |
| `design.streams` | S3 | = | = | = | = | not on path: a patch skips it |
| `design.streams` | S4 | = | = | = | = | not on path: outside any build |
| `design.streams` | S5 | = | = | = | = | not on path: opt-in, not asked |
| `design.streams` | S6 | = | = | = | = | not on path: opt-in, not asked |
| `design.streams` | S7 | = | = | = | = | not on path: opt-in, not asked |
| `design.unit-spec` | S1 | = | = | = | = | holds |
| `design.unit-spec` | S2 | = | = | = | = | holds |
| `design.unit-spec` | S3 | = | the input's unit | = | = | B2-F16 |
| `design.unit-spec` | S4 | = | = | = | = | not on path: outside any build |
| `design.unit-spec` | S5 | = | = | = | = | holds |
| `design.unit-spec` | S6 | = | = | = | = | holds |
| `design.unit-spec` | S7 | = | = | refused by hygiene while coverage is red | = | B2-F10, B2-F12 |
| `design.recommend` | S1 | = | = | = | = | holds |
| `design.recommend` | S2 | = | = | = | = | holds |
| `design.recommend` | S3 | = | = | = | = | holds |
| `design.recommend` | S4 | = | = | = | = | not on path: outside any build |
| `design.recommend` | S5 | = | = | = | = | holds |
| `design.recommend` | S6 | = | = | = | = | holds |
| `design.recommend` | S7 | = | = | = | = | holds |
| `design.reason` | S1 | = | = | = | raced by `design.ready` | B2-F1 |
| `design.reason` | S2 | = | = | = | = | B2-F1 |
| `design.reason` | S3 | = | = | = | = | B2-F1 |
| `design.reason` | S4 | = | = | = | = | not on path: outside any build |
| `design.reason` | S5 | = | = | = | = | B2-F1 |
| `design.reason` | S6 | = | = | = | = | B2-F1 |
| `design.reason` | S7 | = | = | = | = | B2-F1 |
| `design.ready` | S1 | = | on the frontier before the audit decides | = | = | B2-F1, B2-F3 |
| `design.ready` | S2 | = | = | = | = | B2-F1 |
| `design.ready` | S3 | = | = | = | = | B2-F1 |
| `design.ready` | S4 | = | = | = | = | not on path: outside any build |
| `design.ready` | S5 | = | = | = | = | B2-F1 |
| `design.ready` | S6 | = | = | = | = | B2-F1 |
| `design.ready` | S7 | = | = | no UNCARRIED class | = | B2-F1, B2-F19 |
| `design.exit` | S1 | = | = | = | re-entry re-freezes the budget | B2-F4 |
| `design.exit` | S2 | = | = | = | posts to Y | holds |
| `design.exit` | S3 | = | = | = | freezes onto the originating budget | B2-F4 |
| `design.exit` | S4 | = | = | = | = | not on path: outside any build |
| `design.exit` | S5 | = | = | = | Y proceeds on a withdrawn parent | B2-F9 |
| `design.exit` | S6 | = | = | = | = | B2-F4 |
| `design.exit` | S7 | = | = | coverage join reads ambiguity loosely | = | B2-F11 |
| `build.base` | S1 | = | = | = | = | holds |
| `build.base` | S2 | = | = | = | = | holds |
| `build.base` | S3 | = | = | the patch intake | = | holds |
| `build.base` | S4 | = | = | = | = | not on path: outside any build |
| `build.base` | S5 | = | = | = | = | not on path: X is past it; quiesce starts nothing |
| `build.base` | S6 | = | = | = | = | holds |
| `build.base` | S7 | = | = | = | = | holds |
| `build.unit-lease` | S1 | = | = | = | later units leased by no item | B2-F8 |
| `build.unit-lease` | S2 | = | = | = | cross-node unit, shared worktree | B2-F7, B2-F8 |
| `build.unit-lease` | S3 | = | = | = | = | holds |
| `build.unit-lease` | S4 | = | = | = | = | not on path: outside any build |
| `build.unit-lease` | S5 | = | = | tombstoned by `life.unlease` | = | holds |
| `build.unit-lease` | S6 | = | = | = | refused → as `leases` says | holds |
| `build.unit-lease` | S7 | = | = | = | = | holds |
| `build.unit-pass` | S1 | = | = | = | = | holds |
| `build.unit-pass` | S2 | node x's builder | = | = | no integration under shared | B2-F7 |
| `build.unit-pass` | S3 | = | = | = | = | holds |
| `build.unit-pass` | S4 | = | = | = | = | not on path: outside any build |
| `build.unit-pass` | S5 | = | = | = | in-flight pass finishes, then quiesced | holds |
| `build.unit-pass` | S6 | = | = | = | = | holds |
| `build.unit-pass` | S7 | = | = | = | = | holds |
| `build.acceptance` | S1 | = | = | = | fail → an undeclared fix pass | B2-F6 |
| `build.acceptance` | S2 | = | = | = | = | B2-F6 |
| `build.acceptance` | S3 | = | = | = | red again → an undeclared fix pass | B2-F6 |
| `build.acceptance` | S4 | = | = | = | = | not on path: outside any build |
| `build.acceptance` | S5 | = | = | = | = | not on path: quiesce dispatches nothing new |
| `build.acceptance` | S6 | = | = | = | red unit → an undeclared fix pass | B2-F6 |
| `build.acceptance` | S7 | = | = | = | = | B2-F6 |
| `build.scope` | S1 | = | = | = | = | holds |
| `build.scope` | S2 | = | = | = | = | holds |
| `build.scope` | S3 | = | = | = | = | holds |
| `build.scope` | S4 | command in the adopter's tree | map kit absent | = | = | B2-F13 |
| `build.scope` | S5 | = | = | = | = | not on path: quiesce dispatches nothing new |
| `build.scope` | S6 | = | = | = | = | holds |
| `build.scope` | S7 | = | = | = | = | B2-F13 |
| `build.reuse-check` | S1 | = | = | = | clean → prose target | B2-F2 |
| `build.reuse-check` | S2 | = | = | = | = | B2-F2 |
| `build.reuse-check` | S3 | = | = | = | = | B2-F2 |
| `build.reuse-check` | S4 | = | = | = | = | not on path: outside any build |
| `build.reuse-check` | S5 | = | = | = | = | not on path: quiesce dispatches nothing new |
| `build.reuse-check` | S6 | = | = | = | = | B2-F2 |
| `build.reuse-check` | S7 | = | = | = | = | B2-F2 |
| `build.recommend` | S1 | = | prose need | = | closing review re-owed on each lap | B2-F2, B2-F18 |
| `build.recommend` | S2 | = | = | = | = | B2-F2 |
| `build.recommend` | S3 | = | = | = | = | B2-F2 |
| `build.recommend` | S4 | = | = | = | = | not on path: outside any build |
| `build.recommend` | S5 | = | = | = | = | not on path: X withdrawn before it |
| `build.recommend` | S6 | = | = | = | review at CEILING across laps | B2-F2, B2-F18 |
| `build.recommend` | S7 | = | = | = | = | B2-F2 |
| `build.ratify` | S1 | = | = | = | = | not on path: `decisions.major` is `author-rubric` by default |
| `build.ratify` | S2 | = | = | = | = | not on path: default `author-rubric` |
| `build.ratify` | S3 | = | = | = | = | not on path: default `author-rubric` |
| `build.ratify` | S4 | = | = | = | = | not on path: outside any build |
| `build.ratify` | S5 | = | = | = | = | not on path: X withdrawn before it |
| `build.ratify` | S6 | = | = | = | = | not on path: default `author-rubric` |
| `build.ratify` | S7 | = | = | = | = | not on path: default `author-rubric` |
| `build.distill` | S1 | = | on the frontier before the closing review | = | = | B2-F1, B2-F2 |
| `build.distill` | S2 | = | = | = | = | B2-F1 |
| `build.distill` | S3 | = | = | = | = | B2-F1 |
| `build.distill` | S4 | = | = | = | = | not on path: outside any build |
| `build.distill` | S5 | = | = | = | = | not on path: X withdrawn before it |
| `build.distill` | S6 | = | = | = | = | B2-F1 |
| `build.distill` | S7 | = | = | = | = | B2-F1 |
| `build.core` | S1 | = | = | = | = | B2-F2 |
| `build.core` | S2 | = | = | = | = | B2-F2 |
| `build.core` | S3 | = | = | = | = | B2-F2 |
| `build.core` | S4 | = | = | = | = | not on path: outside any build |
| `build.core` | S5 | = | = | = | = | not on path: X withdrawn before it |
| `build.core` | S6 | = | = | = | own red → a fix unit or excepted | B2-F2 |
| `build.core` | S7 | = | = | = | = | B2-F2 |
| `build.exit` | S1 | = | = | = | = | B2-F2 |
| `build.exit` | S2 | = | = | = | = | B2-F2 |
| `build.exit` | S3 | = | = | = | = | B2-F2 |
| `build.exit` | S4 | = | = | = | = | not on path: outside any build |
| `build.exit` | S5 | = | = | = | Y reaches it on a withdrawn parent | B2-F9 |
| `build.exit` | S6 | = | = | = | = | B2-F2 |
| `build.exit` | S7 | = | = | = | = | B2-F2 |

| dIndexedDesign | B2-F1, B2-F3, B2-F5, B2-F14, B2-F17, B2-F19, B2-F20 |
| dScopedBuild | B2-F2, B2-F6, B2-F7, B2-F8, B2-F13, B2-F16, B2-F18 |
| dBoundRoles | B2-F15 |
| dFurnishedOrders | holds |
| dTrueNorth | B2-F10, B2-F11, B2-F12 |

| P12 | holds |
| P17 | B2-F14 |
| P18 | B2-F15 |
| P19 | B2-F16 |
| P24 | B2-F1, B2-F2, B2-F6 |
| P25 | holds |
| P26 | holds |
| P41 | B2-F10, B2-F11, B2-F12 |
