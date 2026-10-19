# Walk return: run A, walker 1, S1

**Serves:** research PLAY-dClosedLoop-1

Dispatch 160's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-1-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed in this scenario because the attending owner's own interactions do nothing. The confirmations at breakpoints, the live questions and the declared spec audit are each resolved or dropped before the owner can answer. Both of the build's approvals (the intake that carries the request mandate and the Plan ratification) are written by the agent that acts on them.

### A1-F1 — `entry.intake` is acted by a role that writes its own witness
- **Address:** flow-steps [entry] `entry.intake`
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - flow-steps:81 says the actor is "orientation scout, in an owner-bound session only" and the witness is "the intake entry the scout writes".
  - The same row's route says "because the hook crashed or never fired", and flow-steps [revised] `hook-actor-kind` says "`entry.intake` is a hook".
  - layer-roles:414 puts `entry.intake` under `hook`. layer-memory:402 says "its writer is `entry.intake`'s hook (PM-9)". cl-dClosedLoop-0377 says "the session's intake log, which `entry.intake`'s prompt-submit hook writes".
  - [rules] says "No witness is typed by the acting agent."
  - Probe: `grep -rn 'entry.intake' <copy>/memory/builds/dClosedLoop/build --include=*.md | grep -v research-` shows a hook in layer-roles, layer-memory and ownership, and "orientation scout" only in flow-steps:81.
  - Stage 0's K1 cannot see this, because the actor is now a declared role and K1 "left out: whether a witness is actor-typed (P2)".
- **Consequence:** In S1, the owner's request is the mandate. `deploy.mandate` reads "the intake record", and `plan.ratification: request` reads it as the ratification. A model writes that record about itself, so every check that takes the intake as the owner's words certifies text an agent typed.
- **Fix:** Restore the actor to "hook: the prompt-submit hook (Runtime's)" and the witness to "the intake entry the hook writes". Add the arm to cl-dClosedLoop-0090's witness-class rule, seen red on a planted role-typed intake.

### A1-F2 — Under `plan.ratification: request`, the ratification is whatever the planner records
- **Address:** flow-steps [plan] `plan.exit`
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - flow-steps:140 says "under `plan.ratification: request`, the owner's go, as the planner records it, stands as the ratification".
  - Against it:
    - flow-steps [plan] Exits: "the request is the ratification".
    - [consequences]: "`plan.exit`'s witness carries it".
    - cl-dClosedLoop-0377: "its intake read as the request's ratification".
    - cl-dClosedLoop-0378: until the hook lands, the item "falls back to dDeclaredLoop's owner gate, held for the owner's disposition".
    - cl-dClosedLoop-0283: "Plan's ratification ... re-pointed to the intake record".
    - P2: "never from state the acting agent typed".
  - Probe: `python -I scratchpad/cl.py <v2> all | grep -E '0377|0378|0283'` printed those three clauses.
- **Consequence:** S1 runs on the default `request`. Design starts on a go the planner typed, and the gate `autonomy: plan-only` keeps at Plan is met by an agent's own record. dRankedPlan's spec writer gets one rule from the item and the opposite from its own clauses 0377 and 0378.
- **Fix:** Replace the clause with "under `plan.ratification: request`, the intake record, joined by its content key, is the ratification, and until the intake kind lands the owner gate of cl-dClosedLoop-0378". Add a planted planner-typed go that reds.

### A1-F3 — `cl-dClosedLoop-0093`, P23's only enforcer, is carried by no clause
- **Address:** architecture-v2 [chain] dDeclaredLoop row; architecture-v2 [enforcement] `P23` row
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - [enforcement] reads "| `P23` | `cl-dClosedLoop-0093` |".
  - Probe: `grep -rn 'cl-dClosedLoop-0093' <copy> --include=*.md` printed only v2:1707, the enforcement row.
  - A probe parsing every `[chain]` clause printed `495` clauses and "gap after 0092 -> 0094".
  - The dDeclaredLoop row goes from the position engine `cl-dClosedLoop-0092` straight to "each step's items declared ..." `cl-dClosedLoop-0094`.
  - [clause-ids] says "Retired: none", and the next id minted is 0497.
- **Consequence:** P23 ("Claims are trusted by key and source") has no clause, so no chain spec can carry it. The carries join reds a ghost id at dDeclaredLoop's Design exit (c1). In S1, `entry.claim`'s "a retry that finds its own key counts as claimed" rests on a rule that nothing builds.
- **Fix:** Restore the dDeclaredLoop clause for claims trusted by recomputed key and source, with id `cl-dClosedLoop-0093`, or list 0093 as retired and re-point P23's row. Confirm that `stage0.py --root <copy> --arms K5` reds it.

### A1-F4 — Attended confirmations and live questions are resolved when raised, with no declared wait, and a late owner answer has no route
- **Address:** flow-steps [breakpoint]; architecture-v2 [chain] dFurnishedOrders `cl-dClosedLoop-0207`; architecture-v2 [policies] `run.on-owner-question`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - [breakpoint] says `run.on-owner-question` "resolves it when it is raised, never for a ratification: the supervisor's recorded choice under `best-effort-recorded`".
  - `attendance` "`confirm-steps` adds a gate at every step's exit" and "asks owner questions live".
  - The catalogue's `run.on-owner-question` row says the default `best-effort-recorded` "decides an owner item when the item is raised".
  - cl-0207 says "owner questions asked live while the build is attended, best effort recorded once the wait passes". It names no key for that wait. P39 and cl-0118 say "every wait declaring an outcome and a deadline".
  - Probe: `grep -rnE "late answer|answer arriv|arrives late|arriving late" <copy>/memory/builds/dClosedLoop/build` found no route for a late answer, only the walk's own S1 row.
  - LR-3's fork was put about "an unattended run". Nothing says how an attended gate waits.
- **Consequence:** In S1, every confirm-steps gate is decided by the supervisor at once, under the default. Examples are `plan.exit` beyond the ratification, `design.exit`, `build.exit` and `test.exit`. `plan.record`'s owner question is decided the same way, so the attended owner confirms nothing. If the owner's answer arrives late, it meets an item that is already witnessed and has nowhere to route. The guard attendance promises silently loosens.
- **Fix:** Pick one reading and state it in [breakpoint], cl-0207 and `run.on-owner-question`:
  - either an attended gate or question is held until a declared deadline, using `flow.wait-ceiling` or a new key, and the key applies only after it;
  - or attendance's gates are declared outside `run.on-owner-question`.
  
  Then route an answer that arrives after a recorded choice: as a re-entry that draws on `flow.rework-budget`, or recorded with no effect. Add a planted attended gate that must not resolve at raise.

### A1-F5 — An owner-declared spec audit has no writer for its trigger record and no route from the owner's words
- **Address:** flow-steps [breakpoint] `review.trigger`; flow-steps [entry] `entry.place`
- **Class:** K3, c2
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - `review.trigger` is "Proven by ... the owner's request record".
  - Probe: `grep -rn "owner's request" <copy>/memory/builds/dClosedLoop/build | grep -v research-` finds the phrase only in the trigger and probe rows and in prose. No kind row exists in layer-memory's table: `grep "^| " layer-memory.md | grep -iE "request|disposition"` shows only `attendance override` and `disposition`.
  - The owner's mid-build prompt passes `entry.place`, whose closed set (continue, amend, new, patch, repeat, ask, none) routes "continue → that build's `next`". None of those outcomes records a breakpoint request.
  - `life.request` covers only "pause, resume, withdraw or supersede ... attend or unattend".
- **Consequence:** S1's injected "spec audit the owner declares" is not a placement outcome, so the owner's prompt is dropped. No item writes the trigger's witness. The build passes `design.ready` and lands without the audit, which is a terminal reached without its witness.
- **Fix:** Register an owner request record kind with its writer. Either add a `review` or `breakpoint` outcome to `entry.place` and to `life.request`'s verbs, writing that record at the named boundary, or name `disposition` as the witness and state its writer. Add a probe: a planted owner prompt "audit the specs" must produce `review.trigger` before `design.ready`.

### A1-F6 — Closing-review units have no transition row, and "released" resumes Build's tail without waiting for them
- **Address:** flow-steps [transitions]; flow-steps [build] closing review; flow-steps [breakpoint] `review.dispose`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - Design's inputs list "a review finding disposed into a new unit" separately from "a fix unit, for a red whose spec is wrong or a core red".
  - [transitions] has only "building | a unit or feature re-entry, or a fix unit | designing". cl-dClosedLoop-0098 says "the engine refusing any transition it lacks".
  - `review.dispose` on built work routes "built → released", and the flow "resumes at the item the breakpoint stands before", which is `build.distill`. That item's Needs are "`build.recommend`, the closing review where it ran, and `build.ratify` ...". They name no new unit. `build.exit` needs only `build.core`.
  - Build's Exits require "the closing review is folded, its findings built as new units".
- **Consequence:** In S1, when the closing review's findings arrive as new units (an injection), there are two outcomes:
  - The engine refuses building→designing for them.
  - If the engine allows it, `build.distill`, `build.core` and `build.exit` run on the frontier while the units are still in Design. The build reaches Test without its findings built, against Build's own exit contract and cl-dClosedLoop-0400.
- **Fix:** Add the row "building | a closing-review finding disposed into a new unit | designing | the review report and the disposition". Make `build.distill`'s Needs include "every unit `review.dispose` minted, built and reuse-checked". Add a planted finding unit that must hold `build.exit`.

### A1-F7 — `design.ready` and `test.exit` wait on the recommend item, not the reason item, so the frontier can pass a review the reason calls for
- **Address:** flow-steps [design] `design.ready`; flow-steps [test] `test.exit`
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - `design.ready` needs "`design.recommend`, and the spec audit where it ran". `test.exit` needs "`test.recommend`, and the gate review where it ran".
  - Under the default `review.recommendation.source: scored-signals-and-reasoning`, `design.reason` and `test.reason` route "a review → the spec audit" or "the gate review".
  - [rules] says `next` returns "the unwitnessed items whose needs are witnessed" and that independent items run in parallel. P24 says "An item's witness is resolved before any item that depends on it starts".
- **Consequence:** Once `design.recommend` is witnessed, `design.ready` and `design.reason` are both on the frontier. `design.ready` and `design.exit` can be recorded before the reason asks for the audit, and the route to the audit is then unreachable. Under `review.recommendation: binding`, an owed review is skipped, so a guard loosens. Test has the same defect.
- **Fix:** Set the Needs to "`design.reason` where the source runs it, else `design.recommend`; and the spec audit where it ran", and the same for `test.exit`. Add a planted reason that answers "review" and must place the audit.

### A1-F8 — No route reaches `build.recommend`: "the unit built" is not an item, and its Needs are prose
- **Address:** flow-steps [build] `build.reuse-check`, `build.recommend`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - `build.reuse-check` routes "clean → the unit built".
  - `build.recommend` needs "every unit built and reuse-checked".
  - Stage 0's lead says "K2 build.recommend: reached from no entry", and the same for `build.ratify`, `build.distill`, `build.core` and `build.exit`.
- **Consequence:** In S1, after the last unit's reuse check, no declared route or need puts `build.recommend` on the frontier. Build's tail and its exit cannot be reached from the declarations, and with them the closing review it owes by default (`review.build: owed`).
- **Fix:** Route "clean → `build.recommend` once every unit's `build.reuse-check` is witnessed clean", and write the need as `build.reuse-check` for every unit in the roster.

### A1-F9 — P14's "review lenses read the active practices' reach" has no enforcing clause
- **Address:** architecture-v2 [enforcement] `P14`; architecture-v2 [principles] P14
- **Class:** K5
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - P14 says "stage contracts, role handoffs and review lenses read the active practices' reach for their stage".
  - Its row names `cl-dClosedLoop-0031` (the catalogue) and `cl-dClosedLoop-0051` ("reach per step rendered as step-scoped units handed in work orders").
  - Probe: `grep -iE 'lens' clauses.txt | grep -iE 'practice|reach'` printed nothing.
- **Consequence:** S1's spec audit and closing review run lenses that read no practice reach, so a practice does not redefine review as P14 says. No dFairHearing or dCalibratedLens spec has a clause to carry this.
- **Fix:** Add a clause, in dFairHearing's lens catalogue or dCalibratedLens's stage lenses, by which each lens loads the active practices' reach for its stage, seen red on a planted practice whose reach a lens omits. Add it to P14's row.

### A1-F10 — `design.ready`'s witness omits the UNCARRIED class that cl-0398 gives it
- **Address:** flow-steps [design] `design.ready`; architecture-v2 [chain] dIndexedDesign `cl-dClosedLoop-0398`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - flow-steps:192 says "derived READY: none MISSING, THIN or FORKED".
  - cl-0398 says "`design.ready` gaining an UNCARRIED class", with `design.coverage` defaulting to `refuse`.
- **Consequence:** A spec writer carrying the item builds READY without the coverage join. In S1, a unit spec that drops a clause derives READY under the item's text, while dIndexedDesign's clause says it must be refused.
- **Fix:** Add "or UNCARRIED, under `design.coverage`" to the witness of `design.ready`.

### A1-F11 — The overlap outcomes of the lease items route nowhere, and one cites the wrong key
- **Address:** flow-steps [plan] `plan.lease`; flow-steps [build] `build.unit-lease`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - `plan.lease`: "an overlap → noted on the card and in the other build's mailbox". No next item is named.
  - `build.unit-lease`: "an overlap → warned (`leases.overlap`)". The catalogue's `leases.overlap` is "kit-dirs, files, builds", which is granularity. The warn/refuse key is `leases` ("warn, refuse").
- **Consequence:** In S1, a feature on a `tools/` kit overlaps any live build on that kit under the default `kit-dirs`. Neither item says whether the lease is held and the run goes on, so the engine has no witnessed outcome to follow.
- **Fix:** Write "an overlap under `leases: warn` → noted, then as held; under `refuse` → as refused" in both rows, and cite `leases` with `leases.overlap` as the granularity.

## Walk table

| item | S<n> | actor | needs | witness | route | verdict |
|---|---|---|---|---|---|---|
| `entry.intake` | S1 | a role, where the records give a hook | = | the scout's own entry | = | A1-F1 |
| `entry.orient` | S1 | = | = | = | = | holds |
| `entry.place` | S1 | = | = | = | an owner's audit request routes as continue and is lost | A1-F5 |
| `entry.place-check` | S1 | = | = | = | = | not on path: `placement` defaults to agent-places |
| `entry.place-owner` | S1 | = | = | = | = | not on path: `placement` defaults to agent-places |
| `entry.claim` | S1 | = | = | = | = | holds |
| `plan.input` | S1 | = | = | = | = | holds |
| `plan.dedupe` | S1 | = | = | = | = | holds |
| `plan.triage-rule` | S1 | = | = | = | = | holds |
| `plan.triage-judge` | S1 | = | = | = | = | not on path: a declared rule selects the owner's feature request |
| `plan.record` | S1 | = | = | = | owner question decided at raise; a late answer has no route | A1-F4 |
| `plan.research` | S1 | = | = | = | = | holds |
| `plan.place` | S1 | = | = | = | = | holds |
| `plan.lease` | S1 | = | = | = | overlap outcome ends nowhere | A1-F11 |
| `plan.recommend` | S1 | = | = | = | = | holds |
| `plan.reason` | S1 | = | = | = | = | holds |
| `plan.exit` | S1 | = | = | planner-recorded go as ratification | confirm gate resolved at raise | A1-F2, A1-F4 |
| `design.input` | S1 | = | = | = | = | holds |
| `design.reentry` | S1 | = | = | = | = | not on path: S1 admits no amendment |
| `design.inventory` | S1 | = | = | = | = | not on path: S1 has no plan revision |
| `design.seams` | S1 | = | = | = | = | holds |
| `design.decompose` | S1 | = | = | = | = | holds |
| `design.research` | S1 | = | = | = | = | holds |
| `design.overlaps` | S1 | = | = | = | = | holds |
| `design.streams` | S1 | = | = | = | = | not on path: `design.streams` is opt-in and S1 asks for none |
| `design.unit-spec` | S1 | = | = | = | = | holds |
| `design.recommend` | S1 | = | = | = | = | holds |
| `design.reason` | S1 | = | = | = | its review route can come after `design.ready` | A1-F7 |
| `design.ready` | S1 | = | waits on recommend, not reason | lacks UNCARRIED | = | A1-F7, A1-F10 |
| `design.exit` | S1 | = | = | = | confirm gate resolved at raise | A1-F4 |
| `build.base` | S1 | = | = | = | = | holds |
| `build.unit-lease` | S1 | = | = | = | overlap ends nowhere; wrong key cited | A1-F11 |
| `build.unit-pass` | S1 | = | = | = | = | holds |
| `build.acceptance` | S1 | = | = | = | = | holds |
| `build.scope` | S1 | = | = | = | = | holds |
| `build.reuse-check` | S1 | = | = | = | "the unit built" is no item | A1-F8 |
| `build.recommend` | S1 | = | prose need, reached by no route | = | closing-review units have no row | A1-F8, A1-F6 |
| `build.ratify` | S1 | = | = | = | = | not on path: `decisions.major` defaults to author-rubric |
| `build.distill` | S1 | = | names no finding unit | = | = | A1-F6 |
| `build.core` | S1 | = | = | = | = | holds |
| `build.exit` | S1 | = | reachable before finding units are built | = | confirm gate resolved at raise | A1-F6, A1-F4 |
| `test.merge` | S1 | = | = | = | = | holds |
| `test.select` | S1 | = | = | = | = | holds |
| `test.verdict` | S1 | = | = | = | = | holds |
| `test.route` | S1 | = | = | = | = | not on path: S1 injects no red |
| `test.attribute` | S1 | = | = | = | = | not on path: S1 injects no red |
| `test.flakes` | S1 | = | = | = | = | not on path: S1 injects no flake |
| `test.seen-red` | S1 | = | = | = | = | holds |
| `test.recommend` | S1 | = | = | = | = | holds |
| `test.reason` | S1 | = | = | = | its review route can come after `test.exit` | A1-F7 |
| `test.exit` | S1 | = | waits on recommend, not reason | = | confirm gate resolved at raise | A1-F7, A1-F4 |
| `deploy.current` | S1 | = | = | = | = | holds |
| `deploy.mandate` | S1 | = | = | intake record typed by a role | = | A1-F1 |
| `deploy.parents` | S1 | = | = | = | = | holds |
| `deploy.land` | S1 | = | = | = | = | holds |
| `deploy.core` | S1 | = | = | = | = | holds |
| `deploy.record` | S1 | = | = | = | = | holds |
| `deploy.distill` | S1 | = | = | = | = | holds |
| `deploy.recommend` | S1 | = | = | = | = | holds |
| `deploy.notify` | S1 | = | = | = | = | holds |
| `deploy.released` | S1 | = | = | = | = | holds |
| `deploy.snapshot` | S1 | = | = | = | = | holds |
| `deploy.unlease` | S1 | = | = | = | = | holds |
| `deploy.close` | S1 | = | = | = | = | holds |
| `review.trigger` | S1 | = | = | owner's request record has no kind or writer | = | A1-F5 |
| `review.pin` | S1 | = | = | = | = | holds |
| `review.lens` | S1 | = | = | = | = | A1-F9 |
| `review.refute` | S1 | = | = | = | = | holds |
| `review.report` | S1 | = | = | = | = | holds |
| `review.dispose` | S1 | = | = | = | built → released resumes before units are built | A1-F6 |
| `review.fold` | S1 | = | = | = | = | holds |
| `review.cost` | S1 | = | = | = | = | holds |
| `probe.trigger` | S1 | = | = | = | = | not on path: S1's request claims no observation and no role raises a probe |
| `probe.pin` | S1 | = | = | = | = | not on path: no probe opens in S1 |
| `probe.design` | S1 | = | = | = | = | not on path: no probe opens in S1 |
| `probe.experiment` | S1 | = | = | = | = | not on path: no probe opens in S1 |
| `probe.run` | S1 | = | = | = | = | not on path: no probe opens in S1 |
| `probe.judge` | S1 | = | = | = | = | not on path: no probe opens in S1 |
| `probe.return` | S1 | = | = | = | = | not on path: no probe opens in S1 |
| `life.request` | S1 | = | = | = | = | holds |
| `life.quiesce` | S1 | = | = | = | = | not on path: S1 makes no pause, withdraw or supersede |
| `life.notify` | S1 | = | = | = | = | not on path: S1 makes no withdraw or supersede |
| `life.snapshot` | S1 | = | = | = | = | not on path: S1 makes no withdraw or supersede |
| `life.unlease` | S1 | = | = | = | = | not on path: S1 makes no withdraw or supersede |
| `life.close` | S1 | = | = | = | = | not on path: S1 makes no withdraw or supersede |
| `adopt.census` | S1 | = | = | = | = | not on path: gov is already adopted, and S1 runs inside a build |
| `test.seed` | S1 | = | = | = | = | not on path: S1's feature registers no new population |
| `adopt.practices` | S1 | = | = | = | = | not on path: gov is already adopted |
| `adopt.decisions` | S1 | = | = | = | = | not on path: gov is already adopted |
| `adopt.reconstruct` | S1 | = | = | = | = | not on path: the `on-touch` default never runs it |
| `maintain.lease` | S1 | = | = | = | = | not on path: S1 runs no cadence and its post-merge bar is green |
| `maintain.read` | S1 | = | = | = | = | not on path: S1 runs no cadence |
| `maintain.direct` | S1 | = | = | = | = | not on path: S1 runs no cadence |
| `maintain.patch` | S1 | = | = | = | = | not on path: S1 runs no cadence |
| `maintain.file` | S1 | = | = | = | = | not on path: S1 runs no cadence |
| `maintain.levels` | S1 | = | = | = | = | not on path: S1 runs no cadence |
| `maintain.record` | S1 | = | = | = | = | not on path: S1 runs no cadence |
| `loop.lease` | S1 | = | = | = | = | not on path: the weekly Loop Review is outside S1 |
| `loop.gather` | S1 | = | = | = | = | not on path: the weekly Loop Review is outside S1 |
| `loop.price` | S1 | = | = | = | = | not on path: the weekly Loop Review is outside S1 |
| `loop.propose` | S1 | = | = | = | = | not on path: the weekly Loop Review is outside S1 |
| `loop.file` | S1 | = | = | = | = | not on path: the weekly Loop Review is outside S1 |
| `loop.record` | S1 | = | = | = | = | not on path: the weekly Loop Review is outside S1 |
| `release.pick` | S1 | = | = | = | = | not on path: `build.closes` is at-landing and gov lists no environment |
| `release.approve` | S1 | = | = | = | = | not on path: no release program runs in S1 |
| `release.promote` | S1 | = | = | = | = | not on path: no release program runs in S1 |
| `release.verify` | S1 | = | = | = | = | not on path: no release program runs in S1 |
| `release.route` | S1 | = | = | = | = | not on path: no release program runs in S1 |
| `release.record` | S1 | = | = | = | = | not on path: no release program runs in S1 |
| `kits.version` | S1 | = | = | = | = | holds |
| `kits.cut` | S1 | = | = | = | = | not on path: a cadence program outside the build |
| `kits.currency` | S1 | = | = | = | = | not on path: an adopter-side cadence, and gov's receipt is source mode |
| `kits.adopters` | S1 | = | = | = | = | not on path: a cadence program outside the build |
| `kits.offer` | S1 | = | = | = | = | not on path: a cadence program outside the build |
| `kits.install` | S1 | = | = | = | = | not on path: S1 installs no release |
| `kits.update` | S1 | = | = | = | = | not on path: S1 updates no release |

## Build verdicts

| dRankedPlan | A1-F2, A1-F11 |
|---|---|
| dIndexedDesign | A1-F7, A1-F10 |
| dScopedBuild | A1-F6, A1-F8, A1-F11 |
| dWitnessedBar | A1-F7 |
| dOrderedCharter | holds |

## Principle verdicts

| P1 | holds |
|---|---|
| P2 | A1-F1, A1-F2 |
| P11 | holds |
| P12 | holds |
| P13 | holds |
| P14 | A1-F9 |
| P15 | holds |
| P17 | holds |
| P24 | A1-F7, A1-F8 |

Files read:
- C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md
- C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md
- C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md
- C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md
- Code checked: C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/push-main.sh and C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/run-gates/post-merge.sh

The one probe script I wrote is under the scratchpad (`scratchpad/cl.py`, output `scratchpad/clauses.txt`), not under `scratchpad/walk-a1/` as the brief asked.
