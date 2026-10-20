# Walk return: run B, walker 4, breakpoint, probe and lifecycle

**Serves:** research PLAY-dClosedLoop-1

Dispatch 174's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-15-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed in S6 because a build that spent its rework budget, or reached a review at its CEILING, had an ending the policies name but no transition row or route the engine accepts. The engine refused the ending, and the build sat open with nothing to drive it.

### B4-F1 — P23's enforcement row names a clause id that no chain clause carries
- **Address:** architecture-v2 [enforcement] `cl-dClosedLoop-0093`
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S7
- **Evidence:** [enforcement] reads "| `P23` | `cl-dClosedLoop-0093` |". I parsed every `cl-` id out of [chain] (scratch `chain.py`) and the only gap in 0001–0496 is 93. dDeclaredLoop's row runs from 0092 ("the position engine ... each claim's key and verdict printed") straight to 0094. [clause-ids] says "Retired: none".
- **Consequence:** P23 ("a claim is acted on only when its stored key recomputes equal ...") has no clause, so no spec carries it. P29's "Acted on" rule depends on P23's re-derivation and is unenforced too. dTrueNorth's carries join and dOrderedCharter's meta-check get a ghost id.
- **Fix:** Restore the P23 clause in dDeclaredLoop's row as `cl-dClosedLoop-0093` (the claim's key recomputed, its weakest source not agent-typed, otherwise re-derived or held as evidence).

### B4-F2 — Budget-exhaustion and park endings have no transition row and no terminal state
- **Address:** flow-steps [transitions]
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - [transitions] says "Landed, withdrawn, superseded, deferred, retired, refused, merged and answered are terminal" and "the engine refuses any transition the table lacks".
  - v2 `cl-dClosedLoop-0116` has `flow.on-exhausted` "closing the build incomplete with its branch and records kept, `park-for-owner` and `close-incomplete` the other values".
  - `cl-dClosedLoop-0326`: silence "parking the build, its lease released and the item open". layer-runtime [decide]: `stale-remote` "parks once `leases.expiry-hours` passes".
  - `grep -n incomplete` over flow-steps, layer-flow, layer-runtime and layer-memory printed nothing. The only hold state is `paused`, and it keeps its leases.
- **Consequence:** In S6 (budget spent, owner silent on the ratification) and S3 (originating budget spent), the ending P39 promises is a transition `cl-dClosedLoop-0098`'s engine refuses. The build never reaches a terminal, against P20's "ends in a terminal state flow-steps' `[transitions]` declares".
- **Fix:** Add the terminal state `closed-incomplete` and a `parked` state (lease released, item open, resumed by the owner's disposition). Add rows from every open state on `flow.on-exhausted` and on a park, each with its witness.

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

### B4-F5 — A paused build's lease is renewed with no progress and no deadline
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** high
- **Scenario:** S5
- **Evidence:**
  - [lifecycle]: "The supervisor renews them while it is paused, so `leases.expiry-hours` never expires a paused build". `life.quiesce` routes "pause → parked".
  - v2 `leases.renewal` default `progress`: "renews on witnessed progress at item boundaries and on declared waits inside their deadline".
  - layer-runtime [supervise]: "The beat is liveness and renews nothing by itself". P39: "Every wait carries a deadline".
  - `cl-dClosedLoop-0326` uses "parks" for a lease-released state.
- **Consequence:** Under the default, either the paused lease expires and `cl-dClosedLoop-0332`'s pick hands the paused build to another node (the S2 stale-beat path defeats the pause), or renewal runs on activity with no deadline, against P39 and `cl-dClosedLoop-0118`. "Parked" also contradicts "keeps its leases".
- **Fix:** Declare pause as a wait with a deadline (`flow.wait-ceiling` or its own key) and an outcome, renewed under `progress` as a declared wait. Rename the route to `paused`.

### B4-F6 — A replacement build never reaches `design.inventory`, so supersession's kept work has no route
- **Address:** flow-steps [lifecycle]
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Evidence:**
  - [lifecycle]: "A superseded build's kept work passes to its replacement through the replacement's `design.inventory`".
  - `design.input` routes "plan record → `design.seams`; ... plan revision → `design.inventory`". `design.inventory` judges "each completed unit" after a plan revision.
  - layer-flow F-E cites "the re-design inventory already settled for planning misses".
- **Consequence:** Z enters with its own plan record and goes to `design.seams`. X's built units are never inventoried, so the kept work is dropped.
- **Fix:** Add a `design.input` kind "superseding plan record", routed to `design.inventory` over the superseded build's units. Have `life.request` supersede name Z's slug before `life.notify`.

### B4-F7 — "Once a push is made, the build has landed" reads every pass push as a landing
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **Evidence:**
  - `life.quiesce`: "Once a push is made, the build has landed, and a pause, withdraw or supersede is refused".
  - v2 `cl-dClosedLoop-0318`: each role agent pushes "the build's branch as `build.push` says, every pass commit by default".
  - The layer-runtime `lifecycle` fixture tests only landed builds.
- **Consequence:** Read as written, X's first pass push refuses the owner's withdraw mid-Build, and no fixture would catch it.
- **Fix:** Say "once the landing push to the default branch is made". Add a fixture that withdraws after a pass push and is refused only after the landing push.

### B4-F8 — `life.quiesce` reaches only the driver's own acts
- **Address:** flow-steps [lifecycle] `life.quiesce`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S5
- **Evidence:**
  - `life.quiesce` is witnessed by "the executor's record of the acts it let finish", and "An open review fan finishes".
  - v2 `cl-dClosedLoop-0319`: a unit holder in another session or node drives "that unit's passes on its own branch".
  - No route says what `review.report` and `review.dispose` do with a finished fan's findings once the build is withdrawn.
- **Consequence:** A remote holder's acts run on unrecorded until the fence refuses their push after `life.unlease`. The finished review either disposes units into a withdrawn build or loses its findings silently.
- **Fix:** Have `life.quiesce` post a quiesce message to every unit holder and join their acknowledgements into its witness. Route a finished review's findings to asks under withdraw and to the replacement under supersede.

### B4-F9 — `probe.judge` mixes three actor kinds
- **Address:** flow-steps [probe] `probe.judge`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - The actor is "command: the executor's re-run, or the experiment's scorer". The witness adds "where no command can judge, the verifier's judgment, recorded as claimed".
  - [probe] Roles adds "a blind judge".
  - [rules]: "One actor per item, of one kind ... an item whose actor a policy value chooses is one item per value".
- **Consequence:** The executor, a command and a role all act in one item. The builder cannot give it one work order, allowance or return schema, and the role arm has no actor.
- **Fix:** Split it into `probe.judge` (command or executor re-run, or scorer) and `probe.judge-claimed` (the tester or blind judge), routed when no command can judge.

### B4-F10 — The reproduction probe before a patch fix has no trigger
- **Address:** flow-steps [probe] `probe.trigger`
- **Class:** K6
- **Severity:** medium
- **Scenario:** S3
- **Evidence:**
  - v2 `cl-dClosedLoop-0408` (dScopedBuild): "a red-first reproduction, a `reproduction` probe, before a patch build's fix when the build comes from a bug report".
  - `probe.trigger`'s closed set is "the boundary `probe.points` names, the owner's request, the observation `probe.observations` owes, or a role item's `probe` outcome".
  - `design.input` sends a patch straight to `design.unit-spec`.
- **Consequence:** Nothing opens the reproduction, so a patch fix lands without its red-first witness.
- **Fix:** Add the trigger "a patch build from a bug report" to `probe.trigger`, at the boundary before the patch's first `build.unit-pass`. Name it in `design.input`'s patch route.

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

### B4-F12 — `review.cost` writes shape fields before the shapes registry exists
- **Address:** flow-steps [breakpoint] `review.cost`
- **Class:** K7
- **Severity:** low
- **Scenario:** S7
- **Evidence:**
  - `review.cost` (dDeclaredLoop) extends the "`review-shape` line with `shape`, `efforts` and `role-sha` into the shape-run row".
  - v2 [owed]: "dBoundRoles builds the shapes registry". The shape-run kind is dTotalRecall's in layer-memory's table.
  - `grep review-shape tools/workflows/tier2-review.js` printed `renderShapeLine`, which has no shape or role-sha field.
- **Consequence:** From dDeclaredLoop to dBoundRoles, the item writes fields that have no source.
- **Fix:** State a stand-in (shape and role-sha left blank until dBoundRoles), or move the extension onto dBoundRoles.

### B4-F13 — An owner's late answer after the deadline has no route
- **Address:** flow-steps [breakpoint]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - [breakpoint] lists the witness "under `run.on-owner-silence: apply-recommendation`, the item's recommended option applied past the deadline". `confirm-steps` "adds a gate at every step's exit".
  - The v2 `run.on-owner-silence` default is `apply-recommendation`.
  - No clause says what an owner disposition arriving after that does.
- **Consequence:** In S1 the attended owner's late "no" on a step confirmation lands after the build has moved on. It is not refused, recorded or routed back.
- **Fix:** Declare a late disposition's outcome: recorded beside the applied one, and a contrary answer filed as an owner-raised amendment, or a route back drawing on the budget.

### B4-F14 — P29's row leaves out the clauses that carry most of P29
- **Address:** architecture-v2 [enforcement]
- **Class:** K5
- **Severity:** medium
- **Scenario:** S7
- **Evidence:**
  - The row reads "| `P29` | `cl-dClosedLoop-0178` |", and 0178 covers only "inputs handed as content ... re-cut fresh".
  - `roles.verifier-context`, `roles.answered-calls` and `roles.on-contradiction` sit in `cl-dClosedLoop-0196`, `0197` and `0198` (dFurnishedOrders), which are outside the row.
- **Consequence:** dOrderedCharter's meta-check reads P29 as enforced by one clause. Three of its six rules are never joined to the principle.
- **Fix:** Add 0196, 0197 and 0198 to P29's row.

### B4-F15 — Slice items write record kinds that are not registered
- **Address:** layer-memory [contract]
- **Class:** K3
- **Severity:** low
- **Scenario:** S5
- **Evidence:** Three records written by slice items have no row in the kind table:
  - `probe.trigger` writes "the trigger record";
  - `life.request` writes "the command's record";
  - `life.quiesce` writes "the executor's record of the acts it let finish".

  The table holds `attendance override`, `workspace`, `probe` and `review`, but nothing for these three.
- **Consequence:** Stage 0's K3 arm, which reads registered kinds only, cannot see them, so they have no declared reader, home or check.
- **Fix:** Register `probe trigger`, `lifecycle request` and `quiesce` rows, each with its writer item and readers.

| item | S<n> | actor | needs | witness | route | verdict |
|---|---|---|---|---|---|---|
| `review.trigger` | S1 | = | = | = | = | B4-F13 |
| `review.trigger` | S2 | = | = | = | = | holds |
| `review.trigger` | S3 | = | = | = | = | holds |
| `review.trigger` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.trigger` | S5 | = | = | = | = | not on path: after life.request nothing fires a new breakpoint |
| `review.trigger` | S6 | = | = | = | owner silence on ratification parks into no state | B4-F2 |
| `review.trigger` | S7 | = | = | = | = | holds |
| `review.pin` | S1 | = | = | = | = | holds |
| `review.pin` | S2 | = | = | = | = | holds |
| `review.pin` | S3 | = | = | = | = | holds |
| `review.pin` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.pin` | S5 | = | = | = | = | not on path: no breakpoint fires after withdrawal |
| `review.pin` | S6 | = | = | = | = | holds |
| `review.pin` | S7 | = | record-kind registry not yet landed | = | = | B4-F11 |
| `review.lens` | S1 | = | = | = | = | holds |
| `review.lens` | S2 | = | = | = | = | holds |
| `review.lens` | S3 | = | = | = | = | holds |
| `review.lens` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.lens` | S5 | = | = | = | = | holds |
| `review.lens` | S6 | = | = | = | = | holds |
| `review.lens` | S7 | = | = | = | = | holds |
| `review.refute` | S1 | = | = | = | = | holds |
| `review.refute` | S2 | = | = | = | = | holds |
| `review.refute` | S3 | = | = | = | = | holds |
| `review.refute` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.refute` | S5 | = | = | = | = | holds |
| `review.refute` | S6 | = | = | = | = | holds |
| `review.refute` | S7 | = | = | = | = | holds |
| `review.report` | S1 | = | = | = | = | holds |
| `review.report` | S2 | = | = | = | CAS class-claim race re-disposes | holds |
| `review.report` | S3 | = | = | = | = | holds |
| `review.report` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.report` | S5 | = | = | = | finished fan's findings unrouted | B4-F8 |
| `review.report` | S6 | = | = | = | = | holds |
| `review.report` | S7 | = | CAS refs not yet landed | = | routes to unlanded review.dispose | B4-F11 |
| `review.dispose` | S1 | = | = | = | plan and landing artifacts unrouted | B4-F4 |
| `review.dispose` | S2 | = | = | = | = | holds |
| `review.dispose` | S3 | = | = | = | landing review findings as units | B4-F4 |
| `review.dispose` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.dispose` | S5 | = | = | = | units into a withdrawn build | B4-F8 |
| `review.dispose` | S6 | = | = | = | = | holds |
| `review.dispose` | S7 | = | = | = | = | holds |
| `review.fold` | S1 | = | = | = | = | holds |
| `review.fold` | S2 | = | = | = | = | holds |
| `review.fold` | S3 | = | = | = | budget spent ends in no state | B4-F2 |
| `review.fold` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.fold` | S5 | = | = | = | = | not on path: a withdrawn build folds no spec |
| `review.fold` | S6 | = | = | = | no CEILING route; exhaustion has no state | B4-F2, B4-F3 |
| `review.fold` | S7 | = | = | = | = | holds |
| `review.cost` | S1 | = | = | = | = | holds |
| `review.cost` | S2 | = | = | = | = | holds |
| `review.cost` | S3 | = | = | = | = | holds |
| `review.cost` | S4 | = | = | = | = | not on path: update runs outside any build and fires no breakpoint |
| `review.cost` | S5 | = | = | = | = | holds |
| `review.cost` | S6 | = | = | = | = | holds |
| `review.cost` | S7 | = | shapes registry not yet landed | = | = | B4-F12 |
| `probe.trigger` | S1 | = | = | = | = | holds |
| `probe.trigger` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.trigger` | S3 | = | = | = | reproduction never opened | B4-F10 |
| `probe.trigger` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.trigger` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.trigger` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.trigger` | S7 | = | = | = | = | holds |
| `probe.pin` | S1 | = | = | = | = | holds |
| `probe.pin` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.pin` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.pin` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.pin` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.pin` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.pin` | S7 | = | = | = | = | holds |
| `probe.design` | S1 | = | = | = | = | holds |
| `probe.design` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.design` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.design` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.design` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.design` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.design` | S7 | owner item until the tester lands | = | = | = | holds |
| `probe.experiment` | S1 | = | = | = | = | holds |
| `probe.experiment` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.experiment` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.experiment` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.experiment` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.experiment` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.experiment` | S7 | owner item until the experiment shape lands | = | = | = | holds |
| `probe.run` | S1 | = | = | = | = | holds |
| `probe.run` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.run` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.run` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.run` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.run` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.run` | S7 | = | = | = | visual verification unrunnable until its adapter lands | holds |
| `probe.judge` | S1 | command, executor and a verifier role | = | = | = | B4-F9 |
| `probe.judge` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.judge` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.judge` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.judge` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.judge` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.judge` | S7 | = | = | = | = | holds |
| `probe.return` | S1 | = | = | = | = | holds |
| `probe.return` | S2 | = | = | = | = | not on path: S2's injections place or raise no probe |
| `probe.return` | S3 | = | = | = | = | not on path: S3's reproduction never opens at probe.trigger |
| `probe.return` | S4 | = | = | = | = | not on path: update runs outside any build and places no probe |
| `probe.return` | S5 | = | = | = | = | not on path: no probe is placed in a withdrawal or supersession |
| `probe.return` | S6 | = | = | = | = | not on path: S6's failures place or raise no probe |
| `probe.return` | S7 | = | = | written to the build folder until record lands | = | holds |
| `life.request` | S1 | = | = | = | attend writes the override | holds |
| `life.request` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.request` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.request` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.request` | S5 | = | = | command record of no registered kind | = | B4-F15 |
| `life.request` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.request` | S7 | unattended verbs stand in | = | = | = | holds |
| `life.quiesce` | S1 | = | = | = | = | not on path: attend and unattend stop at the record |
| `life.quiesce` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.quiesce` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.quiesce` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.quiesce` | S5 | driver's executor only | = | omits remote holders' acts | pass push read as landing; pause lease undeclared | B4-F5, B4-F7, B4-F8 |
| `life.quiesce` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.quiesce` | S7 | = | = | = | = | holds |
| `life.notify` | S1 | = | = | = | = | not on path: S1 withdraws and supersedes nothing |
| `life.notify` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.notify` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.notify` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.notify` | S5 | = | = | = | Y replans or its wait takes flow.wait-ceiling's default | holds |
| `life.notify` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.notify` | S7 | = | = | = | = | holds |
| `life.snapshot` | S1 | = | = | = | = | not on path: S1 withdraws and supersedes nothing |
| `life.snapshot` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.snapshot` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.snapshot` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.snapshot` | S5 | = | = | = | = | holds |
| `life.snapshot` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.snapshot` | S7 | = | = | = | = | holds |
| `life.unlease` | S1 | = | = | = | = | not on path: S1 withdraws and supersedes nothing |
| `life.unlease` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.unlease` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.unlease` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.unlease` | S5 | = | = | = | queued claim refused on the tombstone | holds |
| `life.unlease` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.unlease` | S7 | = | = | = | = | holds |
| `life.close` | S1 | = | = | = | = | not on path: S1 withdraws and supersedes nothing |
| `life.close` | S2 | = | = | = | = | not on path: S2 issues no owner control |
| `life.close` | S3 | = | = | = | = | not on path: S3 issues no owner control |
| `life.close` | S4 | = | = | = | = | not on path: update issues no owner control |
| `life.close` | S5 | = | = | = | kept work never reaches Z's design.inventory | B4-F6 |
| `life.close` | S6 | = | = | = | = | not on path: S6's failures issue no owner control |
| `life.close` | S7 | = | = | = | = | holds |

| dFairHearing | B4-F11 |
|---|---|
| dDeclaredLoop | B4-F1, B4-F2, B4-F3, B4-F4, B4-F12 |
| dWellOiledMachine | B4-F5, B4-F6, B4-F7, B4-F8, B4-F13 |
| dCalibratedLens | holds |

| P1 | holds |
|---|---|
| P5 | B4-F5 |
| P7 | B4-F4 |
| P20 | B4-F2 |
| P27 | holds |
| P29 | B4-F1, B4-F14 |
| P31 | B4-F9, B4-F10 |
| P36 | holds |
| P39 | B4-F2, B4-F3, B4-F5 |

Read outside the list above: none.

Seal defect: the copy's own round record, `[recall]`, tells every walker that the two mechanical plants sit in the K3 and K5 arms (`stage0.py --root <copy> --arms K3,K5`), which points walkers at where the plants are.
