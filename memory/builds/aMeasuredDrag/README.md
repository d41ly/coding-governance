---
slug: aMeasuredDrag
node: a
opened: 2026-11-15
streams: tooling
status: OPEN
roster: TOOL
ids: TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11
---

# aMeasuredDrag — the performance review's eleven quick wins

## The problem this build exists to solve

An adversarial performance review of gov and its adopters (2026-11-15, base `aebbb4a72`) found that
whole-tree work runs on every commit, bar, Stop and dispatch, with no cache and in a costly order.
Eleven of its findings are small, confirmed fixes that change no verdict: they reorder a cheap test
ahead of an expensive one, memoise a pure function, or drop a duplicate run. The review, its
findings and its skeptic verdicts are the research records under `build/` and `reviews/`.

## Expected improvements

- The driver, the stop-guard and the hooks stop walking git where a cheap test already decides.
- A records commit stops deriving the same coverage twice.
- Each unit names its measured before and after, and no verdict moves.

## Detriments if this is not built

- The confirmed waste keeps costing roughly 15-25 hours of wall-clock a week across runs.
- Every later speed-up build pays the same hook and walk costs while it is built.

## Build-level rules

- **Classification (M2)**: eleven units, all MISSING at open. Each is a decision-preserving speed
  fix; a unit whose spec finds it must move a verdict, refusal or printed line parks that change.
- Every unit proves "no verdict moves" by an equality observation over the real tree or the
  unit's existing fixtures, and states its measured before and after beside a spawn baseline.
- Three unlanded branches edit some of the same files: `branch/speedups-9c2e63` (aTrimmedWait),
  `branch/alightenedloop-eb7b8b` (aLightenedLoop) and the live run `dDeclaredLoop`. This build
  does not touch their build folders or branches; their landings reconcile with this one.
- No self-test suite and no bar inside a pass. The bar runs once, at the close.
- No spec audit: not declared.
- Landing: unattended, on the owner's choice of 2026-11-15 (the brief in `prompts/`).

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aMeasuredDrag-1` | the driver tests a unit's terminal status before its pass walk, and reads a commit's `Pass:` trailer before building its per-unit rows |
| 2 | `TOOL-aMeasuredDrag-2` | the stop-guard reads `background_tasks` and the lease's terminal phase before it spawns `--liveness` |
| 3 | `TOOL-aMeasuredDrag-3` | carries coverage derived once per process, and the staged hygiene run reads checks 29 and 30 from check 9's process |
| 4 | `TOOL-aMeasuredDrag-4` | the instruction-edits leg stops re-running the tags check the tags leg already runs |
| 5 | `TOOL-aMeasuredDrag-5` | procmon-hook decides its throttle before any process spawn, resolving the common dir by reading files |
| 6 | `TOOL-aMeasuredDrag-6` | the index renderer groups the tracked list by build once, instead of scanning it per build |
| 7 | `TOOL-aMeasuredDrag-7` | the recall cache budget sized above one gov index, so two worktrees stop evicting each other |
| 8 | `TOOL-aMeasuredDrag-8` | brief-recorded's date cutoff compared in the shell, with no process per README |
| 9 | `TOOL-aMeasuredDrag-9` | transition_audit parses each distinct conf blob once, not once per commit |
| 10 | `TOOL-aMeasuredDrag-10` | pre-commit reads the staged name list once and resolves python once |
| 11 | `TOOL-aMeasuredDrag-11` | the merge bar hands its own resolved python to its legs, so no leg re-probes the launcher |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-15 · streams tooling
ids TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 0 bound to this build, across 0 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
