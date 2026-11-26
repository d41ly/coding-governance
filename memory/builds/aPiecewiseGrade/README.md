---
slug: aPiecewiseGrade
node: a
opened: 2026-11-15
streams: tooling
roster: TOOL
ids: TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2 TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-4 TOOL-aPiecewiseGrade-5 TOOL-aPiecewiseGrade-6 TOOL-aPiecewiseGrade-7 TOOL-aPiecewiseGrade-8 TOOL-aPiecewiseGrade-9
---

# aPiecewiseGrade — the spec-token checker re-grades only the specs whose inputs moved

## The problem this build exists to solve

`--dispatch` runs the whole-tree spec-token checker, about a minute on node `a`. aLightenedLoop keys
its cache on what the checker read, so a pass commit that moves any of those inputs still pays the
whole run, and every sequential pass commit does: it sets its unit's spec CLOSED. Scoping the check
to one build moves the cross-build joins, so the owner declined it in TOOL-aLightenedLoop-3. The
prompt is in `prompts/`.

## Expected improvements

- A `--dispatch` after a pass commit re-grades only the specs whose own inputs moved.
- The cross-build joins are rebuilt whole on every run, so every verdict, refusal line and stdout byte equals the whole-tree run's.

## Detriments if this is not built

- Every unit of a sequential run pays the whole checker at its dispatch, about a minute on node `a`.
- The cost grows with every spec the tree adds, whichever build owns it.

## Build-level rules

- **Classification (M2)**: two units, MISSING at open, Tier-2: a new mode of a kit's checker, and the driver's call to it. A third, MISSING, added on the owner's answer to TOOL-aPiecewiseGrade-1's F1: the checker resolves `design_lib` once per run, built first. A fourth, MISSING, added on the owner's answer to TOOL-aPiecewiseGrade-2's divergence: the checker's next cache generation is promoted with no fixed-name temp, built before unit 2. Units 5 and 6, MISSING, promoted from the closing review's two medium items on the owner's word, built concurrently. Units 7 and 8, MISSING, promoted from the closing review round 2's two missing arms on the owner's word.
- No unit builds before aLightenedLoop lands on main; this build then reconciles onto it.
- No landing without the owner's explicit ask.
- No spec audit: not declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aPiecewiseGrade-1` | the checker's incremental mode: per-spec findings cached on their own inputs, every cross-build join rebuilt whole |
| 2 | `TOOL-aPiecewiseGrade-2` | `run_spec_token_check` runs the incremental mode on a whole-key miss |
| 3 | `TOOL-aPiecewiseGrade-3` | the checker resolves the memory-tree kit's `design_lib` once per run |
| 4 | `TOOL-aPiecewiseGrade-4` | the checker's next cache generation is promoted with no fixed-name temp |
| 5 | `TOOL-aPiecewiseGrade-5` | the per-spec counter names spelled once, and every mismatch loud |
| 6 | `TOOL-aPiecewiseGrade-6` | one per-slug lock over the driver's spec-token cache state |
| 7 | `TOOL-aPiecewiseGrade-7` | an arm for the spec-token lock's foreign-runtime clause |
| 8 | `TOOL-aPiecewiseGrade-8` | arms for the counter key-set guards |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 8 unit(s) · node a · opened 2026-11-15 · streams tooling
ids TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2 TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-4 TOOL-aPiecewiseGrade-5 TOOL-aPiecewiseGrade-6 TOOL-aPiecewiseGrade-7 TOOL-aPiecewiseGrade-8 TOOL-aPiecewiseGrade-9

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aPiecewiseGrade-3 — the spec-token checker resolves the memory-tree kit's `design_lib` once per process, so no caller pays the kit resolution per call](spec/2026-11-15-spec-TOOL-aPiecewiseGrade-3.md) | 1 | 1 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aPiecewiseGrade-1 — the spec-token checker's incremental mode: each live spec's findings cached on its own inputs, every join rebuilt whole](spec/2026-11-15-spec-TOOL-aPiecewiseGrade-1.md) | 2 | 2 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aPiecewiseGrade-4 — the spec-token checker writes its next cache generation into a directory the caller names, so no caller renames a fixed-name temp](spec/2026-11-15-spec-TOOL-aPiecewiseGrade-4.md) | 3 | 2 | CLOSED | rev-2 | 2026-11-16 |
| [TOOL-aPiecewiseGrade-2 — `run_spec_token_check` runs the checker's incremental mode on a whole-key miss, and names its per-spec cache's live generation in a file only where the whole key is recorded](spec/2026-11-15-spec-TOOL-aPiecewiseGrade-2.md) | 4 | 2 | CLOSED | rev-4 | 2026-11-16 |
| [TOOL-aPiecewiseGrade-5 — the spec-token checker's 24 per-spec counter names live in one tuple, and a mismatch is loud or a miss, never a silent 0](spec/2026-11-16-spec-TOOL-aPiecewiseGrade-5.md) | 5 | 2 | CLOSED | rev-1 | 2026-11-16 |
| [TOOL-aPiecewiseGrade-6 — one per-slug lock in the sidecar holds a dispatch's spec-token state from the start half to the end of the read half](spec/2026-11-16-spec-TOOL-aPiecewiseGrade-6.md) | 5 | 2 | CLOSED | rev-2 | 2026-11-16 |
| [TOOL-aPiecewiseGrade-7 — an arm for the stale check's foreign-runtime clause](spec/2026-11-16-spec-TOOL-aPiecewiseGrade-7.md) | 6 | 1 | CLOSED | rev-2 | 2026-11-16 |
| [TOOL-aPiecewiseGrade-8 — two permanent arms hold the spec-token checker's counter key-set guards](spec/2026-11-16-spec-TOOL-aPiecewiseGrade-8.md) | 6 | 1 | CLOSED | rev-1 | 2026-11-16 |
<!-- /gen:build-units -->

Records: 38 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2 TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-4 TOOL-aPiecewiseGrade-5 TOOL-aPiecewiseGrade-6 TOOL-aPiecewiseGrade-7 TOOL-aPiecewiseGrade-8.

Ids whose spec moved past its audited revision: none — 0 of 8 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aPiecewiseGrade-3` | no |
| 2 | `TOOL-aPiecewiseGrade-1` | no |
| 3 | `TOOL-aPiecewiseGrade-4` | no |
| 4 | `TOOL-aPiecewiseGrade-2` | no |
| 5 | `TOOL-aPiecewiseGrade-5`, `TOOL-aPiecewiseGrade-6` | yes |
| 6 | `TOOL-aPiecewiseGrade-7`, `TOOL-aPiecewiseGrade-8` | yes |

A step's `Parallel` yes means its units share an order; `doc.build-method#m6-passes-commits-parallelism` still sequences two of them whose write sets intersect at dispatch.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| the units | the units table above |
| briefs | `2026-11-16-prompt-TOOL-aPiecewiseGrade-8-review-brief.md`, `2026-11-16-prompt-TOOL-aPiecewiseGrade-8-1-spec-writer.md` and 19 more under prompts/ |
| reviews | `2026-11-16-review-TOOL-aPiecewiseGrade-5-diff-review-round2.md` (CLEAN WITH FIXES), `2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1.md` (CLEAN WITH FIXES) |
| red-fix | `2026-11-15-build-TOOL-aPiecewiseGrade-1-red-fix-4.md`, `2026-11-15-build-TOOL-aPiecewiseGrade-1-red-fix-3.md` and 2 more under build/ |
| logs | `2026-11-16-build-TOOL-aPiecewiseGrade-8-1-acceptance-ledger.md`, `2026-11-16-build-TOOL-aPiecewiseGrade-7-1-acceptance-ledger.md` and 9 more under build/ |
| open asks | `BACKLOG.md`, 1 open |
| card ref | `refs/gov/builds/aPiecewiseGrade/card` |
<!-- /gen:build-routes -->
