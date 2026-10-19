# Skeptic return: run A, batch 4

**Serves:** research PLAY-dClosedLoop-1

Dispatch 178's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-19-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- A5-F11: confirmed low
  Both notes contradict the rule they annotate. flow-steps `[rules]` (lines 41-44) routes past `flow.route-backs` to "asks", then says "Revised 2026-10-19 by the owner's SL-1 and SL-2: the loop had become an owner item". `[breakpoint]` (lines 494-498) says "filed as an ask … Revised …: it became an owner item". v2 `flow.route-backs` (line 1133) says the open work "goes to asks (P39, the owner's SL-1)", so asks is the current route. Read the usual way, as what the revision did, each note says the opposite. The rubric grades this as wording, so low.
- A5-F9: confirmed medium
  v2 line 1146 defines the threshold only as "three consecutive greens unless set". cl-0368 uses it to release a leg, and so does `test.select` (flow-steps:294). `test.flakes` (flow-steps:298) holds "a leg past the threshold". layer-memory:570 says outright that the one threshold "serves both the hold and its release". No record says what is counted for the hold, or over what window, so the hold arm cannot be specced.
- A5-F8: confirmed medium
  `test.merge` (flow-steps:293) sends a conflict "→ Build for a resolution pass", and `[transitions]` has "testing | a fix pass, or a conflict to resolve | building". But `[build]` enters only "when every unit is READY", and none of its items is a resolution pass. flow-interactions' settlement ("a recorded resolution pass in the units it touches") is not carried into any item. `[rules]` (lines 40-41) says "a merge conflicted by another build's landing is re-verified in its turn", which leaves it unclear whether that pass draws on the budget.
- A5-F1: confirmed high
  `[transitions]` (flow-steps:623-650) has no parked state and no incomplete terminal, and line 621 says "the engine refuses any transition the table lacks". Endings declared elsewhere have nowhere to go:
  - v2:1103 `run.on-owner-silence`: a ratification "parks its build … its lease released and the item open";
  - v2:1135 `flow.on-exhausted`: `park-for-owner`, `close-incomplete`;
  - cl-0116: "closing the build incomplete".
  `[lifecycle]` line 596 says "A paused build keeps its leases", so `paused` cannot stand in for a parked build. One detail is overstated: layer-runtime:335 `stale-remote` parks the item, not the build. The other endings hold up, so it stays c2.
- A3-F3: confirmed high
  The `none → designing` row on `patch` (flow-steps:627) is witnessed by "the patch's derived plan record". layer-memory:404 says the plan kind's "writer is `plan.record`", and a patch build never reaches Plan. `entry.claim` (line 86) only claims the slug and takes the lease. A grep shows `patch.ratify` 0 times in flow-steps. v2:1519 sets `patch.ratify` to `owner` under the strict column (header at line 1345), so that ratification is silently skipped (c3).
- A1-F6: confirmed high
  `[design]` (lines 171-172) lists "a review finding disposed into a new unit" separately from "a fix unit". The only matching `[transitions]` row (line 637) names "a unit or feature re-entry, or a fix unit". `review.dispose` (line 488) sends built work to "built → released", and the flow resumes before `build.ratify`/`build.distill`. `build.distill`'s Needs (line 241) do not include the findings' units, so it reaches the frontier while they are still in Design. That breaks Build's exit "its findings built as new units" (line 228).
- A3-F4: confirmed medium (the walker said high; the rubric grades it medium)
  layer-expansions:225 `maintain.patch` "opens a patch build at Design", routing "Design, as `patch.ratify` says", which skips `entry.place` and `entry.claim`. But flow-steps `[entry]` (lines 108-110) already says a cadence filer's prompt "is recorded as intake … and placed by `entry.place` the same way". So the design does declare the right path, and the expansion row contradicts it. That is something a spec writer trips over, not a scenario that fails as designed.
- A3-F8: confirmed medium
  layer-expansions:225 keys the witness by "(reading, offender key)" only. `maintain.file` (line 226) at least keys its `seen` rows by period or event and SHA. cl-0092 makes items "idempotent by witness", so when a patched offender comes back under the same key, the existing intake counts as done.
- A3-F9: confirmed medium
  The Maintain and Loop Review tables (layer-expansions:220-262) have no Needs column. No route reaches `maintain.levels`, `maintain.record` or `loop.record`: `maintain.patch` → "Design", `maintain.file` → "Plan's triage", `loop.file` → "the owner's breakpoint". Only `maintain.record` "releases the lease". whole-audit `[stage0]` lists the same three as reached from no entry.
- A4-F18: confirmed low
  layer-expansions:455 routes on "`pull-and-watch` … `push-branches` … `pull-only`" without naming the key. v2:1177 is the only place `deploy.currency` appears in v2, and no clause reads it. One part of the finding is wrong: `kits.cut` and `kits.currency` already name `kits.host`, `kits.cadence` and `kits.watch-cadence` in their actor cells (lines 453-454). Stage 0's K4 arm misses them because it scans only the needs, does, proof and then cells (stage0.py:412-413).
- A4-F17: confirmed low
  layer-expansions:456 says "the design adds an eighth; the mode refuses all eight". cl-0435 adds "step processes a ninth spawn kind its mode refuses unless they run under the step kind's isolation contract", and also has `kits.offer` "running the steps that need no target code". The item mentions neither.
- A4-F8: confirmed medium
  layer-expansions:456 scopes the grant "to `gov/update-*` on its one remote". The grant field (layer-runtime:869-871) is a list of scopes that registration probes, and the `grant` fixture (line 1188) only checks granted against declared scopes. No copied design record says how a scope limited to one branch prefix is granted or probed (a grep for `gov/update-*` finds only line 456). The rubric could read this as high (a guard certifying what it does not check), but a refused push already routes to an outbox order, so medium holds.
- A4-F4: confirmed high
  layer-expansions:457 gives `kits.install`, `kits.update` the actor "the owner, or a command", against flow-steps `[rules]` "One actor per item, of one kind". Its only route is "an adapter that declares no target → its slot renders not installed". The walk's outcomes have no route: step k exits 1 and the receipt names k-1 (cl-0022), the downgrade refusal (cl-0021), a `retired-edited` order (cl-0026), a step marked attended (cl-0024).
- A2-F8: refuted
  The finding has node x pushing X's build branch, but cl-0319 (v2 dWellOiledMachine row) says the other node's unit holder drives "only that unit's passes on its own branch, pushed the same way … the driver alone running transitions". layer-runtime `[isolate]` "Integration before release" (lines 731-735) has the supervisor merge each unit branch into the build branch. So the race on the build branch the finding needs does not exist. The finding cites cl-0318 and cl-0133 but not cl-0319.
- A2-F2: confirmed medium (the walker said high; the rubric grades it medium)
  layer-runtime:405-406 and cl-0325 release only "the build's lease as a hand-over". No record releases the in-flight unit's lease under `leases.granularity: build-and-unit` (v2:1031). The finding's "no node can ever claim" branch does not hold. Under `leases.renewal: progress` (v2:1032) a wait renews only inside its deadline. After that the unit lease expires at `leases.expiry-hours` (24, v2:1033), and cl-0332's pick offers expired leases. So the build is delayed by up to a day, not stuck.
- A3-F18: confirmed low (the walker said medium; the rubric grades it low)
  layer-runtime:1043 says dDeclaredLoop keeps "the coordination feature (`gap-conc-01`, `gap-conc-02`)". v2:1639 gives dPlacedRequest "the coordination feature: one lease grammar". The gap join (gap-join.py) reads only v2's chain table, so the gap is not owned twice there. The layer record's line is a stale pointer.

- `deploy.mandate` S3: defect
  ### AS4-F1 — `deploy.mandate` takes a patch build's intake as its landing authority, so an owner-ratified patch lands unratified
  - **Address:** flow-steps [deploy] `deploy.mandate`
  - **Class:** K10, c3
  - **Severity:** medium
  - **Scenario:** S3
  - **Evidence:** Under `plan-only` (the default, v2:1021), the item checks "the request's mandate", proven by "the intake record". A Maintain patch's intake is written by `maintain.patch`, not by the owner. With `patch.ratify: owner` set as an override over `standard`, no item reads that key (A3-F3), and this check passes on the intake alone.
  - **Consequence:** A patch the owner is meant to ratify lands without that ratification. The preset combinations are safe (strict sets `every-stage`), so only an override reaches it.
  - **Fix:** Make the plan-only arm's witness, for a patch or repeat build, the derived plan record's ratification as `patch.ratify` says.
- `deploy.mandate` S6: holds
  Each S6 failure falls before this item (ratification silence parks the build, per v2:1103) or after it (`deploy.land`). Its one route is `deploy.parents`.
- `deploy.core` S7: holds
  Today's tools match what the item reads: `push-main.sh:454-459` writes the per-SHA log and `gate-post-merge.start`, and `post-merge.sh:323-330` copies the run record to `gate-run/<run id>/`, whose header records `head` (run-gates.sh:2431).
- `test.flakes` S5: holds
  The held-flaky-leg ask is keyed by the leg's name, not by the build (layer-memory:569), so a withdrawal or supersession leaves nothing behind. X is withdrawn mid-Build and never reaches the item.
- `review.pin` S6: defect
  ### AS4-F2 — No breakpoint item reads `review.max-rounds`, so a round past the CEILING is pinned and run
  - **Address:** flow-steps [breakpoint] `review.pin`, `review.trigger`
  - **Class:** K2, c3
  - **Severity:** medium
  - **Scenario:** S6
  - **Evidence:** cl-0117 requires "the round after the limit refused and the report reading CEILING", and v2:1128 declares `review.max-rounds` (3). A grep for `max-rounds` and `CEILING` over flow-steps finds nothing: not `review.trigger` (fired → `review.pin`), not `review.pin`, and not `[breakpoint]`'s policy list (line 502).
  - **Consequence:** In S6's review at its CEILING, `review.pin` pins a fourth round. Only `flow.rework-budget` stops the loop, and no item produces the CEILING report.
  - **Fix:** Have `review.trigger` or `review.pin` read the round count against `review.max-rounds`, refuse the next round, and route to a CEILING report, with `review.max-rounds` added to the policy list.
- `plan.reason` S2: holds
  It has one actor (the planner) and its witness is joined, not typed. Its route to "the Plan breakpoint" passes through `review.trigger`, which decides not-fired under `review.recommendation: advice` (v2:1207). Nothing in it depends on which node runs it.
- `test.seen-red` S7: defect
  ### AS4-F3 — The seen-red record's only declared writer is the item that checks for it
  - **Address:** flow-steps [test] `test.seen-red`; layer-memory kind table `seen-red`
  - **Class:** K3, c3
  - **Severity:** high
  - **Scenario:** S7
  - **Evidence:** layer-memory:425 says "seen-red | dWitnessedBar | its writer is `test.seen-red`". flow-steps:299 has that item "check" for the record and be proven by "the seen-red records". No other item sees a gate red and records it, and cl-0345 is the bare phrase "seen-red records".
  - **Consequence:** Built as declared, the check reads records its own writer produced, so it certifies gates nobody saw red. Otherwise nothing writes the record, and every new gate of chain build k fails the check.
  - **Fix:** Name a writer that runs the gate against its plant (the unit's acceptance or the executor), and keep `test.seen-red` as a reader only.
- `entry.place` S2: defect
  ### AS4-F4 — Placement's closed disposition set has no way to offer one unit of a build leased elsewhere, which cl-0319 places "at placement"
  - **Address:** flow-steps [entry] `entry.place`; v2 [chain] dWellOiledMachine `cl-dClosedLoop-0319`
  - **Class:** K2, K6
  - **Severity:** medium
  - **Scenario:** S2
  - **Evidence:** cl-0319: "a unit of a leased build offered at placement to another session or node as `build.unit-holders` says". `entry.place`'s set is "continue, amend, new, patch, repeat, ask, none". `continue` goes to "that build's `next`", and orientation:153-154 checks it as "the build is live and its lease is free or this session's".
  - **Consequence:** Node x's request to take one of X's units either gets no disposition, or is refused under `placement.check: refuse` (the default, v2:1044) because d holds X's lease. A spec writer for dPlacedRequest cannot satisfy dWellOiledMachine's clause.
  - **Fix:** Add a `unit` disposition, routed to that unit's lease under `build.unit-holders` and refused under `driver-only`, with its check.

- **Read outside the list above:**
  - The handoff prompt `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-19-skeptic.md`, read once to find the task. It repeats the task block.
  - I also read the copy's own `.py` instruments under `build/` (`2026-10-19-build-PLAY-dClosedLoop-1-stage0.py` and `2026-10-19-build-PLAY-dClosedLoop-1-gap-join.py`) to check what the K4 arm and the gap join scan. They are not on the excluded list, but they are instruments rather than design records.
  - Listings only, no files read: the copy's root and the `seed-dcl/scratch/` folder.
