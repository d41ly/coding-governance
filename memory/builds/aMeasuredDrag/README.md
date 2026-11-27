---
slug: aMeasuredDrag
node: a
opened: 2026-11-15
streams: tooling
roster: TOOL
ids: TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 TOOL-aMeasuredDrag-12 TOOL-aMeasuredDrag-13 TOOL-aMeasuredDrag-14
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

- `TOOL-aMeasuredDrag-1` F1: the status-first reorder of `read_open_passes` is parked, because it adds stderr lines; the trailer-first `--check-commit` ships.
- `TOOL-aMeasuredDrag-3` F1: the `--staged --with-verdicts` half is parked, because it changes a crash's printed heading; the memo ships.
- `TOOL-aMeasuredDrag-2` is deferred whole: every spawn-skipping option moves check 54's refusal text.
- Each item's question, options and reason are in `RUN.md`.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aMeasuredDrag-1` | the driver tests a unit's terminal status before its pass walk, and reads a commit's `Pass:` trailer before building its per-unit rows |
| 2 | `TOOL-aMeasuredDrag-2` | the stop-guard reads `background_tasks` and the lease's terminal phase before it spawns `--liveness` (deferred) |
| 3 | `TOOL-aMeasuredDrag-3` | carries coverage derived once per `--check --with-verdicts` process (the staged half parked) |
| 4 | `TOOL-aMeasuredDrag-4` | the instruction-edits leg stops re-running the tags check the tags leg already runs |
| 5 | `TOOL-aMeasuredDrag-5` | procmon-hook decides its throttle before any process spawn, resolving the common dir by reading files |
| 6 | `TOOL-aMeasuredDrag-6` | the index renderer groups the tracked list by build once, instead of scanning it per build |
| 7 | `TOOL-aMeasuredDrag-7` | the recall cache budget sized above two gov indexes, so two worktrees stop evicting each other |
| 8 | `TOOL-aMeasuredDrag-8` | brief-recorded's date cutoff compared in the shell, with no process per README |
| 9 | `TOOL-aMeasuredDrag-9` | transition_audit parses each distinct conf blob once, not once per commit |
| 10 | `TOOL-aMeasuredDrag-10` | pre-commit reads the staged name list once and resolves python once |
| 11 | `TOOL-aMeasuredDrag-11` | the merge bar hands its own resolved python to its legs, so no leg re-probes the launcher |
| 12 | `TOOL-aMeasuredDrag-12` | the closing review's six minor items: an absolute-only launcher memo, and the arms and floors that make units 4, 10 and 11 fail when undone |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** DEFERRED · 12 unit(s) · node a · opened 2026-11-15 · streams tooling
ids TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 TOOL-aMeasuredDrag-12 TOOL-aMeasuredDrag-13
ids TOOL-aMeasuredDrag-14

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aMeasuredDrag-1 — `--check-commit` reads its `Pass:` trailer before it walks any pass, and walks only the units the message names](spec/2026-11-15-spec-TOOL-aMeasuredDrag-1.md) | 1 | 1 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aMeasuredDrag-2 — the stop-guard decides a terminal lease and a pending background task before it spawns `--liveness`](spec/2026-11-15-spec-TOOL-aMeasuredDrag-2.md) | 2 | 1 | DEFERRED | rev-2 | 2026-11-15 |
| [TOOL-aMeasuredDrag-3 — carries coverage derived once per `--check --with-verdicts` call](spec/2026-11-15-spec-TOOL-aMeasuredDrag-3.md) | 3 | 2 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aMeasuredDrag-4 — the instruction-edits leg stops re-running the tags check the tags leg already runs](spec/2026-11-15-spec-TOOL-aMeasuredDrag-4.md) | 4 | 2 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aMeasuredDrag-5 — procmon-hook decides its throttle before any process spawn, resolving the common dir by reading files](spec/2026-11-15-spec-TOOL-aMeasuredDrag-5.md) | 5 | 1 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aMeasuredDrag-6 — the index renderer groups the tracked list by build once, instead of scanning it per build](spec/2026-11-15-spec-TOOL-aMeasuredDrag-6.md) | 6 | 1 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aMeasuredDrag-7 — the recall cache budget sized above two gov indexes, so two worktrees stop evicting each other](spec/2026-11-15-spec-TOOL-aMeasuredDrag-7.md) | 7 | 1 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aMeasuredDrag-8 — brief-recorded's date cutoff compared in the shell, with no process per README](spec/2026-11-15-spec-TOOL-aMeasuredDrag-8.md) | 8 | 1 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aMeasuredDrag-9 — `transition_audit.read_modes` parses each distinct conf blob once, not once per commit](spec/2026-11-15-spec-TOOL-aMeasuredDrag-9.md) | 9 | 1 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aMeasuredDrag-10 — `.githooks/pre-commit` reads the staged list once and resolves python once, each leg keeping its own trigger](spec/2026-11-15-spec-TOOL-aMeasuredDrag-10.md) | 10 | 1 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aMeasuredDrag-11 — the merge bar hands its own resolved python to its legs, so no leg re-probes the launcher](spec/2026-11-15-spec-TOOL-aMeasuredDrag-11.md) | 11 | 2 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aMeasuredDrag-12 — the closing review's six minor items: an absolute-only launcher memo, and the arms and floor that make units 4, 10 and 11 fail when undone](spec/2026-11-15-spec-TOOL-aMeasuredDrag-12.md) | 12 | 2 | CLOSED | rev-1 | 2026-11-15 |
<!-- /gen:build-units -->

Records: 68 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 TOOL-aMeasuredDrag-12 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9.

Ids whose spec moved past its audited revision: none — 0 of 12 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aMeasuredDrag-1` | no |
| 2 | `TOOL-aMeasuredDrag-2` | no |
| 3 | `TOOL-aMeasuredDrag-3` | no |
| 4 | `TOOL-aMeasuredDrag-4` | no |
| 5 | `TOOL-aMeasuredDrag-5` | no |
| 6 | `TOOL-aMeasuredDrag-6` | no |
| 7 | `TOOL-aMeasuredDrag-7` | no |
| 8 | `TOOL-aMeasuredDrag-8` | no |
| 9 | `TOOL-aMeasuredDrag-9` | no |
| 10 | `TOOL-aMeasuredDrag-10` | no |
| 11 | `TOOL-aMeasuredDrag-11` | no |
| 12 | `TOOL-aMeasuredDrag-12` | no |

A step's `Parallel` yes means its units share an order; `doc.build-method#m6-passes-commits-parallelism` still sequences two of them whose write sets intersect at dispatch.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| run state | `RUN.md` |
| the units | the units table above |
| briefs | `2026-11-15-prompt-TOOL-aMeasuredDrag-9-1-builder.md`, `2026-11-15-prompt-TOOL-aMeasuredDrag-8-1-builder.md` and 36 more under prompts/ |
| reviews | `2026-11-15-review-TOOL-aMeasuredDrag-1-performance.md` (CLEAN WITH FIXES), `2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md` (CLEAN WITH FIXES) |
| red-fix | `2026-11-15-build-TOOL-aMeasuredDrag-5-red-fix-2.md`, `2026-11-15-build-TOOL-aMeasuredDrag-3-red-fix-1.md` and 4 more under build/ |
| research | `2026-11-15-build-TOOL-aMeasuredDrag-1-verdicts.md`, `2026-11-15-build-TOOL-aMeasuredDrag-1-synthesis-brief.md` and 8 more under build/ |
| logs | `2026-11-15-build-TOOL-aMeasuredDrag-9-1-acceptance-ledger.md`, `2026-11-15-build-TOOL-aMeasuredDrag-8-1-acceptance-ledger.md` and 10 more under build/ |
| open asks | `BACKLOG.md`, 1 open |
| card ref | `refs/gov/builds/aMeasuredDrag/card` |
<!-- /gen:build-routes -->
