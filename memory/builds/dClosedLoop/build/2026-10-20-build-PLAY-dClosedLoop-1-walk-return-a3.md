# Walk return: run A, walker 3, S3 and S5

**Serves:** research PLAY-dClosedLoop-1

Dispatch 162's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-3-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed in this scenario because a landed build's post-merge red sent it out to a patch build with no route back to its own close, and a withdrawn parent left its dependent in a wait that no record gives a route or a deadline.

### A3-F1 — A post-merge red leaves the originating build with no path to `landed`
- **Address:** flow-steps [deploy] `deploy.core`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **Evidence:** `deploy.core` Then: "red → a patch build through the entry-point table's post-close row, and the close waits for its filing". No other route leads to `deploy.record`. `deploy.close` Needs only "`deploy.unlease` and `deploy.released`", so no item writes or reads a filing witness. `[transitions]` has no `deploying` row for a post-merge red, and "the engine refuses any transition the table lacks".
- **Consequence:** The originating build never records its landing, never unleases and never closes. Its lease stays held until it expires, and "the close waits" has no witness to wait on.
- **Fix:** Route red to `deploy.record` with the landing recorded red. Name the patch intake's key in the landing record, and add that key's witness to `deploy.close`'s Needs.

### A3-F2 — The post-close row still sends a post-landing red to triage as an ask
- **Address:** flow [Entry points, settled 2026-10-14]
- **Class:** K2
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** The row reads "A failed verify after its build closed at landing | Plan's triage | filed as an ask, then a patch build or a planned build by its size". layer-flow `[settled]` says the row "now covers … a post-landing core red, each entering as a patch build", but the table was never revised. `deploy.core` routes to "a patch build through the entry-point table's post-close row".
- **Consequence:** A spec writer for `deploy.core` reads two contradictory entry paths: an ask through triage, or a patch at Design.
- **Fix:** Revise the row: a post-landing core red or a landing-review finding enters at Design as a patch build, and a post-close failed verify enters at triage.

### A3-F3 — No item writes a patch build's derived plan record, and no flow item reads `patch.ratify`
- **Address:** flow-steps [transitions] (none → designing on `patch`); [entry] `entry.claim`
- **Class:** K3, c3
- **Severity:** high
- **Scenario:** S3
- **Evidence:** The `patch` transition is witnessed by "the patch's derived plan record, the claim ref and the lease record". layer-memory's kind table says the plan kind's "writer is `plan.record`", and a patch build never reaches Plan. flow's entry-point table says the record is "derived from the intake and ratified as `patch.ratify` says". `grep patch.ratify` over flow-steps finds nothing. v2 `[presets]` sets `patch.ratify: owner` under `strict`.
- **Consequence:** A patch build's entry transition lacks its witness. Under `strict`, no owner gate exists, so the owner ratification the preset declares silently never happens.
- **Fix:** Give `entry.claim`, or a new dPlacedRequest item, the derivation of the plan record on `patch` and `repeat`. Make that item read `patch.ratify`, with `owner` raising an owner item resolved as `[breakpoint]`'s owner gate is.

### A3-F4 — `maintain.patch` opens a patch build at Design and skips placement, claim and lease
- **Address:** layer-expansions [Maintain items] `maintain.patch`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S3
- **Evidence:** It "opens a patch build at Design … Routes: Design, as `patch.ratify` says". flow-steps `[entry]` says a cadence filer's prompt "is recorded as intake … and placed by `entry.place` the same way". `[transitions]` requires the claim ref and the lease record for `patch`.
- **Consequence:** A Maintain patch has no slug claim, no lease and no transition witness. The engine refuses it, or the patch runs unleased against other nodes.
- **Fix:** Route `maintain.patch` to the filer's intake and then `entry.place`, so it reaches `entry.claim` the way every other patch does.

### A3-F5 — One post-merge red raises two patch builds, and one of them escapes the shared budget
- **Address:** flow-steps [deploy] `deploy.core`; layer-expansions [Maintain] `default-branch-red`; architecture-v2 [chain] `cl-dClosedLoop-0440`
- **Class:** K10
- **Severity:** high
- **Scenario:** S3
- **Evidence:** `deploy.core`: red → a patch build. The code at `tools/run-gates/post-merge.sh:249` is `PM_RED_REF=refs/gov/bar-red`, so a red is published. layer-expansions says the `default-branch-red` event is "produced by the core's runner-written bar verdict … which `refs/gov/bar-red` indexes", and `maintain.events` defaults to all three events. `maintain.patch` then opens a second patch. Patch builds skip `plan.dedupe`. `cl-0440` shares the budget only for "a patch build raised by a landing".
- **Consequence:** Two patch builds race to fix one red. The Maintain one starts on a fresh budget, so the chain of patches is no longer bounded (P39).
- **Fix:** Use one producer and one key, (`default-branch-red`, landed SHA). `deploy.core` files under the key Maintain's reading uses, and `maintain.patch` finds it. Extend `cl-0440` to a Maintain patch whose offender is a landed SHA, seen red on a planted double filing.

### A3-F6 — The shared rework budget has no declared home or writer once its build closes
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0115`, `cl-dClosedLoop-0440`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** `cl-0115` says the budget is "one per build in its transition record … keyed to the build". `cl-0440` says a patch build draws "on the originating build's rework budget, so a chain of patch builds shares one budget". The originating build's transitions end at `deploy.close`. No clause names the record that takes a patch's draws, or how draws from two nodes serialise.
- **Consequence:** Concurrent patch builds read the same remaining budget and both draw on it. Either the draws go to an unwritten record, or one draw is lost.
- **Fix:** Add a budget ledger per root build, appended by compare-and-swap under the root's claim ref, with each patch reaching its root through its `patches` edge. Show it red on two planted concurrent draws.

### A3-F7 — Once the budget is spent, a post-merge red ends in a closed-incomplete patch and a red default branch
- **Address:** flow-steps [deploy] `deploy.core`; architecture-v2 [chain] `cl-dClosedLoop-0116`
- **Class:** K10
- **Severity:** high
- **Scenario:** S3
- **Evidence:** `deploy.core` raises the patch unconditionally. `cl-0116`, under the default `best-effort-ending`: "closing the build incomplete … raising the budget the owner's alone". No owner item is raised for it.
- **Consequence:** The patch closes with only an ask filed, and the default branch stays red. Every later build's `test.route` then meets an INHERITED red and mints fix units on its own budget.
- **Fix:** When the shared budget is spent, a post-merge red opens an owner item to raise the budget or revert, whatever `flow.on-exhausted` says. Show it on a planted spent chain.

### A3-F8 — `maintain.patch`'s key has no period or SHA, so a recurrence after the patch lands counts as done
- **Address:** layer-expansions [Maintain items] `maintain.patch`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** Its witness is "the intake, keyed by (reading, offender key)". `maintain.file` instead adds a `seen` row "keyed by (reading, offender key, period, or event and SHA)". Items are "idempotent by witness" (`cl-0092`).
- **Consequence:** When the patch's own fix regresses, the existing witness reads the re-patch as done. The regression is neither patched nor filed.
- **Fix:** Key the intake by (reading, offender key, base SHA). With a patch still open, a recurrence adds a `seen` row. With the patch landed, it opens a new patch on the shared budget.

### A3-F9 — Neither cadence program reaches its closing item, so the lease release and the record go unwitnessed
- **Address:** layer-expansions [Maintain items] `maintain.record`, `maintain.levels`; [Loop Review items] `loop.record`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** Stage 0 leads: "maintain.levels / maintain.record / loop.record: reached from no entry". The expansion tables have no Needs column. `maintain.patch` routes "Design", and `maintain.file` routes "Plan's triage". Only `maintain.record` "releases the lease".
- **Consequence:** A Maintain run that patches or files never writes its maintenance record and never releases its lease. The same holds for the Loop Review's record.
- **Fix:** Add Needs columns, and route every outcome of `maintain.read`, `maintain.direct`, `maintain.patch` and `maintain.file` (and of `loop.file`) to the program's record item.

### A3-F10 — `deps.on-parent-withdrawn` has no per-value semantics, routes or transition rows, and is read only at Deploy
- **Address:** flow-steps [deploy] `deploy.parents`; [transitions]; architecture-v2 [chain] `cl-dClosedLoop-0100`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S5
- **Evidence:** `deploy.parents` routes "a parent withdrawn … → as `deps.on-parent-withdrawn` says". layer-flow only names the values: "`replan` by default, with `adopt-parent-work` and `withdraw-too` allowed". No record defines them, and `cl-0100` builds the key with no arm per value. `[transitions]` has no deploying, building or designing → planning row for `replan`. Stage 0 K4 reports `deps.coordination` and `deps.early-build` "read by no chain clause and no item". No item consumes `life.notify`'s `withdrawn` post before `deploy.parents`.
- **Consequence:** Y, waiting on X's interface in Design or Build, never reacts to the withdrawal. At Deploy, the default `replan` has no transition, so the engine refuses it and Y is stuck.
- **Fix:** Define each value's route:
  - `replan`: a plan revision, with designing/building/deploying → planning rows.
  - `adopt-parent-work`: `design.inventory` over X's kept branch.
  - `withdraw-too`: `life.request` with a command actor.

  Also add a boundary item that consumes `withdrawn` and `superseded` posts, and arm each value on a planted case.

### A3-F11 — Y's dependency hold at `deploy.parents` declares no deadline and no outcome
- **Address:** flow-steps [deploy] `deploy.parents`; architecture-v2 [policies] `flow.wait-ceiling`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S5
- **Evidence:** "a parent unlanded or paused → holds". `flow.wait-ceiling` is "the deadline gov's own waits declare, a dependency hold …", but only `cl-0162` (mailbox) and `cl-0368` (CONTENDED) bind it. Deploy's policy list omits it. `cl-0118` reds "a wait declaring no deadline".
- **Consequence:** A parent paused or held indefinitely keeps Y waiting forever, which is the condition `gap-flow-10` names. `cl-0118`'s check, once built, reds gov's own floor.
- **Fix:** Route `holds` past `flow.wait-ceiling` to an owner item, or to `deps.on-parent-withdrawn`'s route. Add a dShippedRelease clause seen red on a planted parent paused past the ceiling.

### A3-F12 — A supersession hands the kept work to nothing
- **Address:** flow-steps [lifecycle] `life.request`, kept-work note; [design] `design.input`
- **Class:** K2, c4
- **Severity:** high
- **Scenario:** S5
- **Evidence:** The kept-work note: "kept work passes to its replacement through the replacement's `design.inventory`". `design.input` routes only "plan revision → `design.inventory`", and Design's seven inputs include no supersession. `life.request` "asks to … supersede the build" and its witness is "the command's record", which holds no replacement. Even so, `life.notify` posts "with the replacement's slug". `life.unlease` "reclaims the build's workspaces". No item writes the `supersedes` edge (`cl-0217`).
- **Consequence:** Z enters Design through `design.seams`, X's built units are never inventoried, and X's workspaces are reclaimed. The kept work is lost, and dependents' links move to an unnamed replacement.
- **Fix:** Make supersede require a claimed replacement slug, refusing otherwise, and write the `supersedes` edge. Add a Design input "a supersession" that routes to `design.inventory` over X's units at its branch tip. Have `life.unlease` reclaim worktrees but keep the branch.

### A3-F13 — Lease refusals route "as `leases` says", which fails open on a terminal tombstone under the default `warn`
- **Address:** flow-steps [entry] `entry.claim`; [plan] `plan.lease`; [build] `build.unit-lease`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S5
- **Evidence:** Each item routes "refused → as `leases` says". v2's `leases` row is "warn, refuse | warn", with `standard` set to warn. R2.2: "overlap warns only". `cl-0281` and `cl-0415` require that "a queued claim replayed against a withdrawn build … is refused".
- **Consequence:** Under the default preset, a replayed take against X's tombstone proceeds with a warning, and units of a withdrawn build resume.
- **Fix:** Split the route. A tombstone, a terminal build or an epoch fence is always refused and files an ask. Only an overlap or a live holder goes "as `leases` says".

### A3-F14 — `entry.claim`'s own-key idempotency routes a replayed claim into a terminal build
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Evidence:** `entry.claim`: "a retry that finds its own key counts as claimed" → "claimed → Plan, or Design on `patch` or `repeat`". layer-memory: "A slug's claim ref is never pruned". `[transitions]` has no row leaving `withdrawn`.
- **Consequence:** A replayed intake after the withdrawal routes into a withdrawn build. The engine refuses the transition, and the request is neither placed nor answered.
- **Fix:** `entry.claim` reads the slug's last transition. If it is terminal, it mints a fresh slug or returns the request naming the terminal state.

### A3-F15 — Quiesce cannot stop acts other nodes run under X's unit leases
- **Address:** flow-steps [lifecycle] `life.quiesce`, `life.unlease`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **Evidence:** `life.quiesce`'s actor is the executor: "Each running act finishes within its ceiling", witnessed by "the executor's record of the acts it let finish". `life.unlease` then tombstones every lease.
- **Consequence:** Node x's in-flight unit pass is fenced mid-act. Its commits are neither kept nor recorded, and the witness claims a quiesce it never observed.
- **Fix:** Make `life.quiesce` wait, per unit lease, for the holder's hand-over or for its `runtime.act-ceiling`, witnessed per lease.

### A3-F16 — A post to a closed mailbox recreates a ref no one reads or prunes
- **Address:** flow-steps [rules] "Closing a mailbox"
- **Class:** K10
- **Severity:** low
- **Scenario:** S5
- **Evidence:** The rule reads "Only then is the ref pruned, and a missing ref counts as done". Refs are per writing session (`refs/gov/mail/<slug>/<fleet tag>/<session>`, `cl-0141`), and no refusal of a post to a closed build is declared.
- **Consequence:** Y's later question to withdrawn X lands on an orphan ref that nothing reads or prunes. Only `cl-0162`'s default answer ends Y's wait.
- **Fix:** Refuse a post whose slug carries a terminal transition, and answer the sender with that state.

### A3-F17 — `cl-dClosedLoop-0093` is carried by no clause, so P23's only enforcer is a ghost id
- **Address:** architecture-v2 [enforcement] `P23`; [chain] dDeclaredLoop
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S5
- **Evidence:** A probe over v2's `[chain]` found 495 distinct ids, with `[93]` the only one missing from 1..496. `[enforcement]` lists "`P23` | `cl-dClosedLoop-0093`". dDeclaredLoop's row jumps from `0092` to `0094`. `[clause-ids]` says "Retired: none".
- **Consequence:** "Claims are trusted by key and source" has no clause, which is the guard S5's replayed claim needs.
- **Fix:** Restore the dDeclaredLoop clause carrying `cl-dClosedLoop-0093`, or retire the id and name an enforcing clause in P23's row.

### A3-F18 — layer-runtime gives dDeclaredLoop the coordination feature that v2 places on dPlacedRequest
- **Address:** layer-runtime [supervise] "What stays where it is"
- **Class:** K8
- **Severity:** medium
- **Scenario:** S5
- **Evidence:** layer-runtime: "dDeclaredLoop keeps: … the coordination feature (`gap-conc-01`, `gap-conc-02`)". v2 `[chain]` has dPlacedRequest owning "the coordination feature: one lease grammar" and `gap-conc-01` and `gap-conc-02`.
- **Consequence:** Two builds each read as owning the lease grammar that S5's tombstones rest on.
- **Fix:** Re-point layer-runtime's line to dPlacedRequest.

### A3-F19 — `life.quiesce` routes a pause to `parked`, a state `[transitions]` lacks
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K1
- **Severity:** low
- **Scenario:** S5
- **Evidence:** "pause → parked". `[transitions]` reads "any open state | `life.request`: pause | paused".
- **Consequence:** A route names a state the engine does not know.
- **Fix:** Write "pause → paused".

### A3-F20 — A patch build skips the overlap check against live builds
- **Address:** flow-steps [design] `design.input`, `design.overlaps`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **Evidence:** "patch → `design.unit-spec`, as a micro-spec". `design.overlaps` "runs the design index over the roster's write sets, against live builds". `design.unit-spec` "acknowledges the unit's overlaps", but no overlap record exists for a patch.
- **Consequence:** Concurrent patch builds, or a patch and a live build, on the same paths are first seen at `build.unit-lease`, which only warns by default.
- **Fix:** Route patch → `design.overlaps` → `design.unit-spec`.

| item | scenario | actor | needs | witness | route | verdict |
|---|---|---|---|---|---|---|
| `entry.intake` | S3 | = | = | = | = | not on path: a Maintain or deploy.core filing is recorded by dWellOiledMachine's filer, not an owner session |
| `entry.intake` | S5 | = | = | = | = | holds |
| `entry.orient` | S3 | = | = | = | = | holds |
| `entry.orient` | S5 | = | = | = | = | holds |
| `entry.place` | S3 | = | = | = | patch → entry.claim; maintain.patch bypasses it | A3-F4 |
| `entry.place` | S5 | = | = | = | = | holds |
| `entry.place-check` | S3 | = | = | = | = | holds |
| `entry.place-check` | S5 | = | = | = | = | holds |
| `entry.place-owner` | S3 | = | = | = | = | holds |
| `entry.place-owner` | S5 | = | = | = | = | holds |
| `entry.claim` | S3 | = | = | claim ref and lease; no derived plan record written | Design with no plan record | A3-F3 |
| `entry.claim` | S5 | = | = | own-key claim on a terminal slug | claimed → Plan; refused → warn | A3-F13, A3-F14 |
| `plan.input` | S3 | = | = | = | = | not on path: a patch enters at Design |
| `plan.input` | S5 | = | = | = | = | holds |
| `plan.dedupe` | S3 | = | = | = | skipped by a patch, so no dedupe of two patches | A3-F5 |
| `plan.dedupe` | S5 | = | = | = | = | holds |
| `plan.triage-rule` | S3 | = | = | = | = | not on path: a patch enters at Design |
| `plan.triage-rule` | S5 | = | = | = | = | holds |
| `plan.triage-judge` | S3 | = | = | = | = | not on path: a patch enters at Design |
| `plan.triage-judge` | S5 | = | = | = | = | holds |
| `plan.record` | S3 | = | = | = | = | not on path: a patch enters at Design |
| `plan.record` | S5 | = | = | = | = | holds |
| `plan.research` | S3 | = | = | = | = | not on path: a patch enters at Design |
| `plan.research` | S5 | = | = | = | = | holds |
| `plan.place` | S3 | = | = | = | = | not on path: a patch enters at Design |
| `plan.place` | S5 | = | = | = | = | holds |
| `plan.lease` | S3 | = | = | = | = | not on path: entry.claim takes a patch's lease |
| `plan.lease` | S5 | = | = | = | refused → warn on a tombstone | A3-F13 |
| `plan.recommend` | S3 | = | = | = | = | not on path: a patch enters at Design |
| `plan.recommend` | S5 | = | = | = | = | holds |
| `plan.reason` | S3 | = | = | = | = | not on path: a patch enters at Design |
| `plan.reason` | S5 | = | = | = | = | holds |
| `plan.exit` | S3 | = | = | = | = | not on path: a patch enters at Design |
| `plan.exit` | S5 | = | = | = | = | holds |
| `design.input` | S3 | = | = | pins a patch plan record no item wrote | patch → design.unit-spec, skipping overlaps | A3-F3, A3-F20 |
| `design.input` | S5 | = | = | = | no supersession input; Z goes to design.seams | A3-F12 |
| `design.reentry` | S3 | = | = | = | = | not on path: a patch is no amendment |
| `design.reentry` | S5 | = | = | = | = | not on path: no amendment in the scenario |
| `design.inventory` | S3 | = | = | = | = | not on path: no plan revision |
| `design.inventory` | S5 | = | unreached for a replacement | = | = | A3-F12 |
| `design.seams` | S3 | = | = | = | = | not on path: a patch goes straight to a micro-spec |
| `design.seams` | S5 | = | = | = | = | holds |
| `design.decompose` | S3 | = | = | = | = | not on path: a micro-spec, unless a feature fork |
| `design.decompose` | S5 | = | = | = | = | holds |
| `design.research` | S3 | = | = | = | = | not on path: no fact fork in a micro-spec |
| `design.research` | S5 | = | = | = | = | holds |
| `design.overlaps` | S3 | = | = | no overlap record | skipped | A3-F20 |
| `design.overlaps` | S5 | = | = | = | = | holds |
| `design.streams` | S3 | = | = | = | = | not on path: a patch has one unit |
| `design.streams` | S5 | = | = | = | = | holds |
| `design.unit-spec` | S3 | = | the input's unit | = | = | holds |
| `design.unit-spec` | S5 | = | parents' interfaces; withdrawn post unread | = | = | A3-F10 |
| `design.recommend` | S3 | = | = | = | = | holds |
| `design.recommend` | S5 | = | = | = | = | holds |
| `design.reason` | S3 | = | = | = | = | holds |
| `design.reason` | S5 | = | = | = | = | holds |
| `design.ready` | S3 | = | = | = | = | holds |
| `design.ready` | S5 | = | = | = | = | holds |
| `design.exit` | S3 | = | = | = | = | holds |
| `design.exit` | S5 | = | = | = | = | holds |
| `build.base` | S3 | = | = | = | = | holds |
| `build.base` | S5 | = | = | = | = | holds |
| `build.unit-lease` | S3 | = | = | = | = | holds |
| `build.unit-lease` | S5 | = | = | replayed take on a tombstone | refused → warn | A3-F13 |
| `build.unit-pass` | S3 | = | = | = | = | holds |
| `build.unit-pass` | S5 | node x's in-flight builder | = | commits fenced and unrecorded | = | A3-F15 |
| `build.acceptance` | S3 | = | = | = | fail → fix pass on a shared budget with no home | A3-F6 |
| `build.acceptance` | S5 | = | = | = | = | holds |
| `build.scope` | S3 | = | = | = | = | holds |
| `build.scope` | S5 | = | = | = | = | holds |
| `build.reuse-check` | S3 | = | = | = | = | holds |
| `build.reuse-check` | S5 | = | = | = | = | holds |
| `build.recommend` | S3 | = | = | = | = | holds |
| `build.recommend` | S5 | = | = | = | = | not on path: X withdrawn mid-Build before its units finish |
| `build.ratify` | S3 | = | = | = | = | holds |
| `build.ratify` | S5 | = | = | = | = | not on path: X withdrawn mid-Build before its units finish |
| `build.distill` | S3 | = | = | = | = | holds |
| `build.distill` | S5 | = | = | = | = | not on path: X withdrawn mid-Build before its units finish |
| `build.core` | S3 | = | = | = | = | holds |
| `build.core` | S5 | = | = | = | = | not on path: X withdrawn mid-Build before its units finish |
| `build.exit` | S3 | = | = | = | = | holds |
| `build.exit` | S5 | = | = | = | = | not on path: X withdrawn mid-Build before its units finish |
| `test.merge` | S3 | = | = | = | = | holds |
| `test.merge` | S5 | = | = | = | = | holds |
| `test.select` | S3 | = | = | = | = | holds |
| `test.select` | S5 | = | = | = | = | holds |
| `test.verdict` | S3 | = | = | = | = | holds |
| `test.verdict` | S5 | = | = | = | = | holds |
| `test.route` | S3 | = | = | = | INHERITED red from an unfixed main | A3-F7 |
| `test.route` | S5 | = | = | = | = | holds |
| `test.attribute` | S3 | = | = | = | = | holds |
| `test.attribute` | S5 | = | = | = | = | holds |
| `test.flakes` | S3 | = | = | = | = | holds |
| `test.flakes` | S5 | = | = | = | = | holds |
| `test.seen-red` | S3 | = | = | = | = | holds |
| `test.seen-red` | S5 | = | = | = | = | holds |
| `test.recommend` | S3 | = | = | = | = | holds |
| `test.recommend` | S5 | = | = | = | = | holds |
| `test.reason` | S3 | = | = | = | = | holds |
| `test.reason` | S5 | = | = | = | = | holds |
| `test.exit` | S3 | = | = | = | = | holds |
| `test.exit` | S5 | = | = | = | = | holds |
| `deploy.current` | S3 | = | = | = | = | holds |
| `deploy.current` | S5 | = | = | = | = | holds |
| `deploy.mandate` | S3 | = | = | = | = | holds |
| `deploy.mandate` | S5 | = | = | = | = | holds |
| `deploy.parents` | S3 | = | = | = | = | holds |
| `deploy.parents` | S5 | = | = | = | holds with no deadline; withdrawn → undefined value, no transition | A3-F10, A3-F11 |
| `deploy.land` | S3 | = | = | = | = | holds |
| `deploy.land` | S5 | = | = | = | = | not on path: Y holds at deploy.parents |
| `deploy.core` | S3 | = | = | = | red → patch, and a second patch from Maintain; no route back; spent budget | A3-F1, A3-F5, A3-F7 |
| `deploy.core` | S5 | = | = | = | = | not on path: Y holds at deploy.parents |
| `deploy.record` | S3 | = | deploy.core red: unreached | = | = | A3-F1 |
| `deploy.record` | S5 | = | = | = | = | not on path: Y holds at deploy.parents |
| `deploy.distill` | S3 | = | = | = | = | A3-F1 |
| `deploy.distill` | S5 | = | = | = | = | not on path: Y holds at deploy.parents |
| `deploy.recommend` | S3 | = | = | = | = | A3-F1 |
| `deploy.recommend` | S5 | = | = | = | = | not on path: Y holds at deploy.parents |
| `deploy.notify` | S3 | = | = | = | = | A3-F1 |
| `deploy.notify` | S5 | = | = | = | = | not on path: Y holds at deploy.parents |
| `deploy.released` | S3 | = | = | = | = | A3-F1 |
| `deploy.released` | S5 | = | = | = | = | not on path: X withdrawn before the push |
| `deploy.snapshot` | S3 | = | = | = | = | A3-F1 |
| `deploy.snapshot` | S5 | = | = | = | = | not on path: X withdrawn before the push |
| `deploy.unlease` | S3 | = | = | = | = | A3-F1 |
| `deploy.unlease` | S5 | = | = | = | = | not on path: X withdrawn before the push |
| `deploy.close` | S3 | = | no filing witness among its needs | = | = | A3-F1 |
| `deploy.close` | S5 | = | = | = | = | not on path: X withdrawn before the push |
| `review.trigger` | S3 | = | = | = | = | holds |
| `review.trigger` | S5 | = | = | = | = | holds |
| `review.pin` | S3 | = | = | = | = | holds |
| `review.pin` | S5 | = | = | = | = | holds |
| `review.lens` | S3 | = | = | = | = | holds |
| `review.lens` | S5 | = | = | = | = | holds |
| `review.refute` | S3 | = | = | = | = | holds |
| `review.refute` | S5 | = | = | = | = | holds |
| `review.report` | S3 | = | = | = | = | holds |
| `review.report` | S5 | = | = | = | = | holds |
| `review.dispose` | S3 | = | = | = | = | holds |
| `review.dispose` | S5 | = | = | = | = | holds |
| `review.fold` | S3 | = | = | = | = | holds |
| `review.fold` | S5 | = | = | = | = | holds |
| `review.cost` | S3 | = | = | = | = | holds |
| `review.cost` | S5 | = | = | = | = | holds |
| `probe.trigger` | S3 | = | = | = | = | not on path: the patch intake carries a witnessed reading, not a claimed observation |
| `probe.trigger` | S5 | = | = | = | = | not on path: no probe placed or raised in the scenario |
| `probe.pin` | S3 | = | = | = | = | not on path: no probe opened |
| `probe.pin` | S5 | = | = | = | = | not on path: no probe opened |
| `probe.design` | S3 | = | = | = | = | not on path: no probe opened |
| `probe.design` | S5 | = | = | = | = | not on path: no probe opened |
| `probe.experiment` | S3 | = | = | = | = | not on path: no probe opened |
| `probe.experiment` | S5 | = | = | = | = | not on path: no probe opened |
| `probe.run` | S3 | = | = | = | = | not on path: no probe opened |
| `probe.run` | S5 | = | = | = | = | not on path: no probe opened |
| `probe.judge` | S3 | = | = | = | = | not on path: no probe opened |
| `probe.judge` | S5 | = | = | = | = | not on path: no probe opened |
| `probe.return` | S3 | = | = | = | = | not on path: no probe opened |
| `probe.return` | S5 | = | = | = | = | not on path: no probe opened |
| `life.request` | S3 | = | = | = | = | not on path: no owner control in S3 |
| `life.request` | S5 | = | = | command record holds no replacement | = | A3-F12 |
| `life.quiesce` | S3 | = | = | = | = | not on path: no owner control in S3 |
| `life.quiesce` | S5 | = | = | records only local acts | pause → parked | A3-F15, A3-F19 |
| `life.notify` | S3 | = | = | = | = | not on path: no owner control in S3 |
| `life.notify` | S5 | = | = | = | posts withdrawn, which no dependent item consumes | A3-F10 |
| `life.snapshot` | S3 | = | = | = | = | not on path: no owner control in S3 |
| `life.snapshot` | S5 | = | = | = | = | holds |
| `life.unlease` | S3 | = | = | = | = | not on path: no owner control in S3 |
| `life.unlease` | S5 | = | = | tombstones held remote leases; reclaims workspaces; mailbox reopens | = | A3-F12, A3-F15, A3-F16 |
| `life.close` | S3 | = | = | = | = | not on path: no owner control in S3 |
| `life.close` | S5 | = | = | = | = | holds |
| `adopt.census` | S3 | = | = | = | = | not on path: repository-level adoption, outside any build |
| `adopt.census` | S5 | = | = | = | = | not on path: repository-level adoption, outside any build |
| `test.seed` | S3 | = | = | = | = | not on path: no check registration in the scenario |
| `test.seed` | S5 | = | = | = | = | not on path: no check registration in the scenario |
| `adopt.practices` | S3 | = | = | = | = | not on path: repository-level adoption, outside any build |
| `adopt.practices` | S5 | = | = | = | = | not on path: repository-level adoption, outside any build |
| `adopt.decisions` | S3 | = | = | = | = | not on path: repository-level adoption, outside any build |
| `adopt.decisions` | S5 | = | = | = | = | not on path: repository-level adoption, outside any build |
| `adopt.reconstruct` | S3 | = | = | = | = | not on path: repository-level adoption, outside any build |
| `adopt.reconstruct` | S5 | = | = | = | = | not on path: repository-level adoption, outside any build |
| `maintain.lease` | S3 | = | = | = | = | holds |
| `maintain.lease` | S5 | = | = | = | = | not on path: no Maintain reading in S5 |
| `maintain.read` | S3 | = | = | = | default-branch-red over pin → a second patch | A3-F5 |
| `maintain.read` | S5 | = | = | = | = | not on path: no Maintain reading in S5 |
| `maintain.direct` | S3 | = | = | = | = | not on path: the fix changes tracked content |
| `maintain.direct` | S5 | = | = | = | = | not on path: no Maintain reading in S5 |
| `maintain.patch` | S3 | = | = | key lacks period or SHA | Design directly, no claim or lease | A3-F4, A3-F8 |
| `maintain.patch` | S5 | = | = | = | = | not on path: no Maintain reading in S5 |
| `maintain.file` | S3 | = | = | = | = | holds |
| `maintain.file` | S5 | = | = | = | = | not on path: no Maintain reading in S5 |
| `maintain.levels` | S3 | = | reached from no entry | = | = | A3-F9 |
| `maintain.levels` | S5 | = | = | = | = | not on path: no Maintain reading in S5 |
| `maintain.record` | S3 | = | reached from no entry | lease never released | = | A3-F9 |
| `maintain.record` | S5 | = | = | = | = | not on path: no Maintain reading in S5 |
| `loop.lease` | S3 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `loop.lease` | S5 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `loop.gather` | S3 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `loop.gather` | S5 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `loop.price` | S3 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `loop.price` | S5 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `loop.propose` | S3 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `loop.propose` | S5 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `loop.file` | S3 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `loop.file` | S5 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `loop.record` | S3 | = | reached from no entry | = | = | A3-F9 |
| `loop.record` | S5 | = | = | = | = | not on path: weekly cadence, outside the scenario |
| `release.pick` | S3 | = | = | = | = | not on path: a red landed SHA is never picked, and S3 declares no environment |
| `release.pick` | S5 | = | = | = | = | not on path: X never lands |
| `release.approve` | S3 | = | = | = | = | not on path: no release environment in S3 |
| `release.approve` | S5 | = | = | = | = | not on path: X never lands |
| `release.promote` | S3 | = | = | = | = | not on path: no release environment in S3 |
| `release.promote` | S5 | = | = | = | = | not on path: X never lands |
| `release.verify` | S3 | = | = | = | = | not on path: no release environment in S3 |
| `release.verify` | S5 | = | = | = | = | not on path: X never lands |
| `release.route` | S3 | = | = | = | = | not on path: no release environment in S3 |
| `release.route` | S5 | = | = | = | = | not on path: X never lands |
| `release.record` | S3 | = | = | = | = | not on path: no release environment in S3 |
| `release.record` | S5 | = | = | = | = | not on path: X never lands |
| `kits.version` | S3 | = | = | = | = | holds |
| `kits.version` | S5 | = | = | = | = | holds |
| `kits.cut` | S3 | = | = | = | = | not on path: distribution cadence, outside the scenario |
| `kits.cut` | S5 | = | = | = | = | not on path: distribution cadence, outside the scenario |
| `kits.currency` | S3 | = | = | = | = | not on path: adopter-side cadence |
| `kits.currency` | S5 | = | = | = | = | not on path: adopter-side cadence |
| `kits.adopters` | S3 | = | = | = | = | not on path: distribution cadence, outside the scenario |
| `kits.adopters` | S5 | = | = | = | = | not on path: distribution cadence, outside the scenario |
| `kits.offer` | S3 | = | = | = | = | not on path: distribution cadence, outside the scenario |
| `kits.offer` | S5 | = | = | = | = | not on path: distribution cadence, outside the scenario |
| `kits.install` | S3 | = | = | = | = | not on path: adopter install, outside any build |
| `kits.install` | S5 | = | = | = | = | not on path: adopter install, outside any build |
| `kits.update` | S3 | = | = | = | = | not on path: adopter update, outside any build |
| `kits.update` | S5 | = | = | = | = | not on path: adopter update, outside any build |

| dTendedCadence | A3-F4, A3-F5, A3-F8, A3-F9 |
|---|---|
| dDeclaredLoop | A3-F6, A3-F10, A3-F11, A3-F17, A3-F18 |
| dCalibratedLens | A3-F9 |
| dTotalRecall | A3-F3, A3-F14 |

| P6 | A3-F4, A3-F5, A3-F8, A3-F9 |
|---|---|
| P7 | holds |
| P9 | holds |
| P19 | A3-F12 |
| P20 | A3-F1, A3-F3, A3-F4, A3-F10, A3-F14 |
| P30 | A3-F3, A3-F6 |
| P33 | A3-F12 |
| P34 | holds |
| P35 | holds |
