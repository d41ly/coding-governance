# Walk return: run A, walker 5, S6

**Serves:** research PLAY-dClosedLoop-1

Dispatch 164's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-5-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed in this scenario because the walk never declared how a build ends. The ratification park, the three `flow.on-exhausted` endings and the remote-outage park are outcomes the design promises, but `[transitions]` has no row or terminal state for any of them, and a loop that stops by its per-item bound on a blocking path leaves the build with nowhere to go.

**How I walked it.** No preset puts both Plan's ratification breakpoint and the other S6 failures on one build except `strict`, so I walked S6 under `strict` on a core-only install. `entry.claim` takes a lease only on `patch` or `repeat`, and such a build never reaches Plan. So S6's refused lease and its Plan ratification cannot happen to the same build, and I walked the refused lease as a patch build's. Before switching to the sealed copy I read the working tree's `whole-audit` from `[scenarios]` to the end, and listed the sibling briefs' slices. Every finding below is cited from the sealed copy only.

### A5-F1 — `[transitions]` has no state for a parked build, and no terminal for an incomplete ending
- **Address:** flow-steps [transitions]
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - The table's states are planning, designing, building, testing, deploying and paused. Its terminals (line 650) are "Landed, withdrawn, superseded, deferred, retired, refused, merged and answered", and it says "the engine refuses any transition the table lacks".
  - Endings the design declares elsewhere:
    - v2 `[policies]` `run.on-owner-silence`: "a ratification ... parks its build ... its lease released and the item open".
    - `flow.on-exhausted`: `park-for-owner` and `close-incomplete`, and best effort "descoping the failing units to asks and landing the rest, or closing the build incomplete" (`cl-dClosedLoop-0116`).
    - layer-runtime `[decide]` `stale-remote`: "parks once `leases.expiry-hours` passes".
  - Probe: `grep -n -i "incomplete\b"` over flow-steps, layer-flow, layer-memory and layer-runtime found no state. A parked state appears only as a count, `| parked | 8 |`, at layer-runtime:148.
  - `[lifecycle]` says "A paused build keeps its leases", so a parked build, whose lease is released, is not a paused one.
- **Consequence:** Several S6 failures end here: the owner's silence on the ratification, a spent budget under any of the three values, and an unreachable remote that outlasts the lease expiry. Each needs a transition the engine refuses. dDeclaredLoop's own termination check (`cl-dClosedLoop-0118`, "every state reaching a terminal") cannot be specced against a table that lacks these states.
- **Fix:**
  - Add a `parked` state with its rows: owner silence past `run.owner-deadline`, `park-for-owner` and `stale-remote`. Its witness is the park record, and its exit is the owner's disposition, which re-takes the lease.
  - Add a terminal `closed-incomplete` reached by `flow.on-exhausted`.
  - Give a descoped unit a row back from building or testing.

### A5-F2 — A loop that ends non-converging on a blocking item leaves the build with no route
- **Address:** flow-steps [rules], `build.acceptance`, `test.flakes`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - `[rules]`: "Past `flow.route-backs` returns to the same item, that item's loop ends non-converging and its open work goes to asks".
  - `build.acceptance`: "fail → a fix pass", with no arm for the bound.
  - `test.flakes`: "Each re-entry counts against `flow.route-backs`".
  - Build exits only when "every unit is built, with its acceptance recorded", and Test only when "no red blocks".
  - Defaults: `flow.route-backs` is 3 and `flow.rework-budget` is `4+2`, so the per-item bound trips before the budget is spent.
  - `cl-dClosedLoop-0117` says the opposite of `[rules]`: "fix passes against one acceptance red ending at a NON-CONVERGENT round, whose findings are promoted, to units while budget remains and to asks after".
- **Consequence:** S6's red unit at `build.acceptance`, and its flake at Test, each stop at the per-item bound. The open work becomes an ask, but the unit stays unbuilt or the leg stays red. Build or Test then cannot exit, and the budget is not spent, so `flow.on-exhausted` never fires. The build stalls until the stuck detector raises an owner item, which no route declares.
- **Fix:**
  - State one rule in `[rules]`, `build.acceptance` and `test.flakes`, consistent with `cl-dClosedLoop-0117`: past `flow.route-backs`, a blocking item's open work becomes a new unit while budget remains and goes to `flow.on-exhausted` after.
  - Plant the probe: an acceptance red that never greens must reach a terminal.

### A5-F3 — A refused lease routes "as `leases` says", but `leases` is the overlap switch
- **Address:** flow-steps [entry] `entry.claim`; also `plan.lease` and `build.unit-lease`
- **Class:** K1, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - `entry.claim` Then: "the lease refused → as `leases` says". `plan.lease` and `build.unit-lease` say the same.
  - v2 `[policies]`: "`leases` | warn, refuse | warn | R2.2". P5 reads that key as "overlap warns by default". It says nothing about what follows a refusal.
  - On `patch` or `repeat`, `entry.claim` first creates `refs/gov/claims/<slug>`, which is "never pruned", and then takes the lease. A refused lease therefore leaves a claimed slug with no transition record, and the rework budget lives "in its transition record".
  - `cl-dClosedLoop-0132`'s pre-claim budget covers only "placement loops before `entry.claim`".
  - `[rules]` says "A re-dispatch of a refused instance draws on the build's rework budget", while P39 says "Contention waits in its turn and draws nothing". A lease held by another build is both a refusal and contention.
- **Consequence:** S6's first failure has no declared route. The retry draws on no budget (none exists yet) or on one the rules forbid (contention). A spec writer cannot write the arm.
- **Fix:**
  - Route a refused lease explicitly: wait as contention within `flow.wait-ceiling` for the holder's release or expiry, then raise an owner item.
  - Count claim-time retries against `cl-dClosedLoop-0132`'s pre-claim budget.
  - Say what happens to the never-pruned slug claim when the lease is never taken.

### A5-F4 — Under `plan.ratification: request`, the ratification witness is typed by the planner
- **Address:** flow-steps [plan] `plan.exit`
- **Class:** K10, c3
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - `plan.exit`: "under `plan.ratification: request`, the owner's go, as the planner records it, stands as the ratification".
  - `[rules]`: "No witness is typed by the acting agent".
  - v2 `cl-dClosedLoop-0377`: "its intake read as the request's ratification by `plan.ratification`", the intake being hook-written.
  - v2 `[contracts]`: "Plan's witness is the hook-written intake (FR-1)".
- **Consequence:** An owner who is silent, or who never typed a go, is certified as having ratified on the planner's word. The guard certifies what it does not check.
- **Fix:** Make `plan.exit`'s witness under `request` the hook-written intake record keyed to the build's claim, never a planner record. Under `cl-dClosedLoop-0378`'s fallback, use the owner gate.

### A5-F5 — A build parked on the owner's silence loses its lease, and nothing takes it back
- **Address:** architecture-v2 [policies] `run.on-owner-silence` `cl-dClosedLoop-0326`; flow-steps [breakpoint]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - v2 `[policies]` `run.on-owner-silence` and `cl-dClosedLoop-0326`: parking releases the build's lease and leaves the item open.
  - `cl-dClosedLoop-0134`: "each release a hand-over, which any node may take".
  - `[lifecycle]`: "Resume enters its `next`". `plan.lease`'s instance is already witnessed, so `next` never re-runs it.
  - Design's contract takes "a planned, leased build".
- **Consequence:** After the 24-hour silence at Plan's ratification, another node may take over a build that is waiting for the owner. When the owner's late go arrives, the build enters Design holding no lease.
- **Fix:** Release the lease of a build parked for the owner as terminal-for-takeover, or keep it renewed as a paused build's is. Declare a lease re-take item on the owner's disposition of a parked build.

### A5-F6 — An unreachable remote has no arm at the compare-and-swap items, and an unbounded one at `deploy.land`
- **Address:** flow-steps [entry] `entry.claim`, [plan] `plan.lease`, [breakpoint] `review.report`, [deploy] `deploy.land`
- **Class:** K2, c2
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - v2 `leases.offline` default `warn`: "records an acquisition and queues a claim or an ask-id mint keyed by content, each pushed by compare-and-swap on reconnection". `cl-dClosedLoop-0120` applies this "for every compare-and-swap mint alike".
  - None of the outcome sets of `entry.claim`, `plan.lease`, `build.unit-lease` or `review.report`'s `refs/gov/class-claims` has a queued or unreachable outcome.
  - `[transitions]` "none → planning" needs "the claim ref" as its witness.
  - `deploy.land`: "the remote unreachable ... → the supervisor's retry, then an owner item", with no count or deadline. layer-runtime `stale-remote` instead "holds and retries, and parks once `leases.expiry-hours` passes".
- **Consequence:** S6's unreachable remote either enters Plan with no witness for its claim, or stops a `new:` disposition that needs a claim "at report time". At `deploy.land` it either retries without bound or ends in one of two contradictory outcomes. That breaks P39's "every wait carries a deadline and a declared outcome".
- **Fix:**
  - Add a `queued` outcome to each compare-and-swap item. Its route waits on reconnection within `flow.wait-ceiling`, and the item's witness is the pushed ref, read on reconnection.
  - Bound `deploy.land`'s retry with a declared count or deadline and one outcome, aligned with `stale-remote`.

### A5-F7 — The review ceiling has no arm in the review program
- **Address:** flow-steps [breakpoint] `review.dispose`, `review.fold`
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - Probe: `grep -c "max-rounds\|CEILING"` over flow-steps finds 0 hits for either term.
  - `review.dispose` routes "a follow-up round as `review.follow-up` says", and `review.fold` routes "the next round as `review.design.rounds` says".
  - v2 `cl-dClosedLoop-0117` ("the round after the limit refused and the report reading CEILING") and `cl-dClosedLoop-0084` (dFairHearing computes CEILING) give no route once the report reads CEILING.
  - Design rounds also "count against `flow.route-backs`" (3), and `review.max-rounds` is also 3. Two different endings (non-converging to asks, and CEILING) fall on the same round.
- **Consequence:** S6's review at its CEILING has no declared next item. A spec writer for dFairHearing or dDeclaredLoop cannot say where the CEILING report's open highs go.
- **Fix:**
  - Add `review.max-rounds` to `[breakpoint]`'s policy list.
  - Give `review.dispose` and `review.fold` a CEILING arm, consistent with `cl-dClosedLoop-0117`'s promotion rule.
  - Order the two bounds.

### A5-F8 — A landing conflict sends the build to a resolution pass that Build does not declare
- **Address:** flow-steps [test] `test.merge`; [build]
- **Class:** K1
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - `deploy.land`: "refused before the push, a race included → Test". `test.merge`: "a conflict → Build for a resolution pass".
  - Build "Enters when every unit is READY", and its table has no resolution item, actor, lease or witness.
  - Re-entering Build re-runs `build.recommend` and the closing review, which `review.build: owed` requires under `strict`. A "review round after the first" draws on the budget, while `[rules]` says "a merge conflicted by another build's landing ... draws nothing".
- **Consequence:** A conflict caused by another build's landing is resolved by an undeclared actor. It indirectly spends the rework budget that contention must not touch.
- **Fix:** Declare a `build.resolve` item with its actor (the builder, or the architect when an interface clashes), its witness and its re-entry point back into Test. Mark its passes and any re-review as contention that draws nothing.

### A5-F9 — `verdict.flakes`' one threshold is the release streak, yet `test.flakes` reads it as the hold threshold
- **Address:** flow-steps [test] `test.flakes`; architecture-v2 [policies] `verdict.flakes`
- **Class:** K9
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - `test.flakes`: "under `quarantine`, a leg past the threshold `verdict.flakes` declares is held".
  - v2: "`verdict.flakes` | quarantine, record, retry-only; a threshold | quarantine | walk T3; the threshold three consecutive greens unless set".
  - `cl-dClosedLoop-0368` uses that same threshold to release a held leg.
- **Consequence:** For S6's flake at Test, nothing says after how many flakes a leg is held. A spec writer cannot write the hold arm.
- **Fix:** Split the key into a hold threshold (flakes counted in a window) and a release threshold (consecutive greens), each with a default.

### A5-F10 — P23's only enforcing clause id is a ghost
- **Address:** architecture-v2 [enforcement] `P23`
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S6
- **Evidence:**
  - `| \`P23\` | \`cl-dClosedLoop-0093\` |`. The id appears once in v2, in that row.
  - A probe parsing every `[chain]` clause found 495 clauses. Missing id: `['0093']`. dDeclaredLoop's row jumps from `cl-dClosedLoop-0092` to `cl-dClosedLoop-0094`.
- **Consequence:** P23 ("Claims are trusted by key and source") has no clause that enforces it. That matters in S6 wherever a refusal's claim is re-read.
- **Fix:** Restore the dropped clause into dDeclaredLoop's row with its id, or retire 0093 and name P23's real enforcing clauses.

### A5-F11 — Revision notes contradict the route they annotate
- **Address:** flow-steps [rules]; [breakpoint] (the "unverified finding under `review.unverified: block`" bullet)
- **Class:** K2
- **Severity:** low
- **Scenario:** S6
- **Evidence:**
  - `[rules]`: "its open work goes to asks ... Revised 2026-10-19 by the owner's SL-1 and SL-2: the loop had become an owner item, resolved as [breakpoint]'s owner gate is (FH1)".
  - `[breakpoint]`: "the finding is filed as an ask with its evidence. Revised ...: it became an owner item".
- **Consequence:** A reader cannot tell whether the route past the bound is an ask or an owner item.
- **Fix:** Reword each note to say what the route was before the revision ("it had been an owner item until SL-1"), or drop it.

| item | scenario | actor | needs | witness | route | verdict |
|---|---|---|---|---|---|---|
| `entry.intake` | S6 | = | = | = | = | holds |
| `entry.orient` | S6 | = | = | = | = | holds |
| `entry.place` | S6 | = | = | = | patch, then `entry.claim` | holds |
| `entry.place-check` | S6 | = | = | = | = | not on path: `placement` is `agent-places` |
| `entry.place-owner` | S6 | = | = | = | = | not on path: `placement` is `agent-places` |
| `entry.claim` | S6 | = | = | claim ref; no lease record on refusal | refused lease: `leases` is the overlap key; unreachable: no arm | A5-F3, A5-F6 |
| `plan.input` | S6 | = | = | = | = | holds |
| `plan.dedupe` | S6 | = | = | = | = | holds |
| `plan.triage-rule` | S6 | = | = | = | = | holds |
| `plan.triage-judge` | S6 | = | = | = | = | not on path: a rule decides |
| `plan.record` | S6 | = | = | = | = | holds |
| `plan.research` | S6 | = | = | = | = | not on path: no research request |
| `plan.place` | S6 | = | = | = | = | holds |
| `plan.lease` | S6 | = | = | = | refused: as `leases` says, an undeclared route; unreachable: no arm | A5-F3, A5-F6 |
| `plan.recommend` | S6 | = | = | = | = | holds |
| `plan.reason` | S6 | = | = | = | = | holds |
| `plan.exit` | S6 | = | the owner's ratification | under `request`, a planner-typed go | silence parks the build: no transition row, lease lost | A5-F1, A5-F4, A5-F5 |
| `design.input` | S6 | = | = | = | = | holds |
| `design.reentry` | S6 | = | = | = | = | not on path: no amendment |
| `design.inventory` | S6 | = | = | = | = | not on path: no plan revision |
| `design.seams` | S6 | = | = | = | = | holds |
| `design.decompose` | S6 | = | = | = | = | holds |
| `design.research` | S6 | = | = | = | = | not on path: no fact fork |
| `design.overlaps` | S6 | = | = | = | = | holds |
| `design.streams` | S6 | = | = | = | = | not on path: `design.streams` opt-in, not opted |
| `design.unit-spec` | S6 | = | = | = | = | holds |
| `design.recommend` | S6 | = | = | = | = | holds |
| `design.reason` | S6 | = | = | = | spec audit owed under `strict` | holds |
| `design.ready` | S6 | = | = | = | = | holds |
| `design.exit` | S6 | = | = | = | = | holds |
| `build.base` | S6 | = | = | = | = | holds |
| `build.unit-lease` | S6 | = | = | = | refused: as `leases` says, an undeclared route | A5-F3 |
| `build.unit-pass` | S6 | = | = | = | fix pass; the resolution pass is undeclared | A5-F2, A5-F8 |
| `build.acceptance` | S6 | = | = | = | fail: a fix pass, with no arm past `flow.route-backs` | A5-F2 |
| `build.scope` | S6 | = | = | = | = | holds |
| `build.reuse-check` | S6 | = | = | = | = | holds |
| `build.recommend` | S6 | = | = | = | closing review re-run on conflict re-entry | A5-F8 |
| `build.ratify` | S6 | = | = | = | silence on a ratification parks the build: no state | A5-F1 |
| `build.distill` | S6 | = | = | = | = | holds |
| `build.core` | S6 | = | = | = | = | holds |
| `build.exit` | S6 | = | = | = | unreachable after a non-converging unit | A5-F2 |
| `test.merge` | S6 | = | = | = | conflict: Build for an undeclared resolution pass | A5-F8 |
| `test.select` | S6 | = | = | = | = | holds |
| `test.verdict` | S6 | = | = | = | a flake re-entered past `flow.route-backs` has no route | A5-F2 |
| `test.route` | S6 | = | = | = | = | holds |
| `test.attribute` | S6 | = | = | = | = | holds |
| `test.flakes` | S6 | = | = | = | hold threshold undefined; past the bound, no route | A5-F2, A5-F9 |
| `test.seen-red` | S6 | = | = | = | = | holds |
| `test.recommend` | S6 | = | = | = | = | holds |
| `test.reason` | S6 | = | = | = | = | holds |
| `test.exit` | S6 | = | = | = | unreachable while a flaky leg blocks | A5-F2 |
| `deploy.current` | S6 | = | = | = | = | holds |
| `deploy.mandate` | S6 | = | = | = | = | holds |
| `deploy.parents` | S6 | = | = | = | = | holds |
| `deploy.land` | S6 | = | = | = | conflict: Test, then an undeclared resolution; unreachable: unbounded retry | A5-F6, A5-F8 |
| `deploy.core` | S6 | = | = | = | red: a patch build on a spent budget; ending has no state | A5-F1 |
| `deploy.record` | S6 | = | = | = | = | holds |
| `deploy.distill` | S6 | = | = | = | = | holds |
| `deploy.recommend` | S6 | = | = | = | = | holds |
| `deploy.notify` | S6 | = | = | = | = | holds |
| `deploy.released` | S6 | = | = | = | core-only: `policy-file.on-missing-expansion` | holds |
| `deploy.snapshot` | S6 | = | = | = | = | holds |
| `deploy.unlease` | S6 | = | = | = | = | holds |
| `deploy.close` | S6 | = | = | = | = | holds |
| `review.trigger` | S6 | = | = | = | = | holds |
| `review.pin` | S6 | = | = | = | = | holds |
| `review.lens` | S6 | = | = | = | = | holds |
| `review.refute` | S6 | = | = | = | = | holds |
| `review.report` | S6 | = | = | class claim not pushable while unreachable | no queued arm | A5-F6 |
| `review.dispose` | S6 | = | = | = | no CEILING arm | A5-F7, A5-F11 |
| `review.fold` | S6 | = | = | = | no CEILING arm | A5-F7 |
| `review.cost` | S6 | = | = | = | = | holds |
| `probe.trigger` | S6 | = | = | = | = | not on path: `probe.points` none, no observation claimed |
| `probe.pin` | S6 | = | = | = | = | not on path: no probe opened |
| `probe.design` | S6 | = | = | = | = | not on path: no probe opened |
| `probe.experiment` | S6 | = | = | = | = | not on path: no probe opened |
| `probe.run` | S6 | = | = | = | = | not on path: no probe opened |
| `probe.judge` | S6 | = | = | = | = | not on path: no probe opened |
| `probe.return` | S6 | = | = | = | = | not on path: no probe opened |
| `life.request` | S6 | = | = | = | resume of a parked build: no parked state, no lease re-take | A5-F1, A5-F5 |
| `life.quiesce` | S6 | = | = | = | = | not on path: S6 issues no control |
| `life.notify` | S6 | = | = | = | = | not on path: no withdrawal |
| `life.snapshot` | S6 | = | = | = | = | not on path: no withdrawal |
| `life.unlease` | S6 | = | = | = | = | not on path: no withdrawal |
| `life.close` | S6 | = | = | = | = | not on path: no withdrawal |
| `adopt.census` | S6 | = | = | = | = | not on path: repository-level, outside a build |
| `test.seed` | S6 | = | = | = | = | not on path: no check registered |
| `adopt.practices` | S6 | = | = | = | = | not on path: repository-level |
| `adopt.decisions` | S6 | = | = | = | = | not on path: repository-level |
| `adopt.reconstruct` | S6 | = | = | = | = | not on path: repository-level |
| `maintain.lease` | S6 | = | = | = | = | not on path: core-only install |
| `maintain.read` | S6 | = | = | = | = | not on path: core-only install |
| `maintain.direct` | S6 | = | = | = | = | not on path: core-only install |
| `maintain.patch` | S6 | = | = | = | = | not on path: core-only install |
| `maintain.file` | S6 | = | = | = | = | not on path: core-only install |
| `maintain.levels` | S6 | = | = | = | = | not on path: core-only install |
| `maintain.record` | S6 | = | = | = | = | not on path: core-only install |
| `loop.lease` | S6 | = | = | = | = | not on path: core-only install |
| `loop.gather` | S6 | = | = | = | = | not on path: core-only install |
| `loop.price` | S6 | = | = | = | = | not on path: core-only install |
| `loop.propose` | S6 | = | = | = | = | not on path: core-only install |
| `loop.file` | S6 | = | = | = | = | not on path: core-only install |
| `loop.record` | S6 | = | = | = | = | not on path: core-only install |
| `release.pick` | S6 | = | = | = | = | not on path: no integrations installed |
| `release.approve` | S6 | = | = | = | = | not on path: no integrations installed |
| `release.promote` | S6 | = | = | = | = | not on path: no integrations installed |
| `release.verify` | S6 | = | = | = | = | not on path: no integrations installed |
| `release.route` | S6 | = | = | = | = | not on path: no integrations installed |
| `release.record` | S6 | = | = | = | = | not on path: no integrations installed |
| `kits.version` | S6 | = | = | = | = | not on path: no distribution installed |
| `kits.cut` | S6 | = | = | = | = | not on path: no distribution installed |
| `kits.currency` | S6 | = | = | = | = | not on path: no distribution installed |
| `kits.adopters` | S6 | = | = | = | = | not on path: no distribution installed |
| `kits.offer` | S6 | = | = | = | = | not on path: no distribution installed |
| `kits.install` | S6 | = | = | = | = | not on path: no distribution installed |
| `kits.update` | S6 | = | = | = | = | not on path: no distribution installed |

| dFairHearing | A5-F6, A5-F7 |
|---|---|
| dLinkedLibrary | holds |

| P4 | holds |
|---|---|
| P18 | holds |
| P31 | holds |
| P32 | holds |
| P39 | A5-F1, A5-F2, A5-F3, A5-F5, A5-F6, A5-F7, A5-F8 |
