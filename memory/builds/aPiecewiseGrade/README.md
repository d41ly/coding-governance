---
slug: aPiecewiseGrade
node: a
opened: 2026-11-15
streams: tooling
roster: TOOL
ids: TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2 TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-4
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

- **Classification (M2)**: two units, MISSING at open, Tier-2: a new mode of a kit's checker, and the driver's call to it. A third, MISSING, added on the owner's answer to TOOL-aPiecewiseGrade-1's F1: the checker resolves `design_lib` once per run, built first. A fourth, MISSING, added on the owner's answer to TOOL-aPiecewiseGrade-2's divergence: the checker's next cache generation is promoted with no fixed-name temp, built before unit 2.
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
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 3 unit(s) · node a · opened 2026-11-15 · streams tooling
ids TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2 TOOL-aPiecewiseGrade-3 TOOL-aPiecewiseGrade-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aPiecewiseGrade-3 — the spec-token checker resolves the memory-tree kit's `design_lib` once per process, so no caller pays the kit resolution per call](spec/2026-11-15-spec-TOOL-aPiecewiseGrade-3.md) | 1 | 1 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aPiecewiseGrade-1 — the spec-token checker's incremental mode: each live spec's findings cached on its own inputs, every join rebuilt whole](spec/2026-11-15-spec-TOOL-aPiecewiseGrade-1.md) | 2 | 2 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aPiecewiseGrade-2 — `run_spec_token_check` runs the checker's incremental mode on a whole-key miss, and promotes its per-spec cache only where the whole key is recorded](spec/2026-11-15-spec-TOOL-aPiecewiseGrade-2.md) | 3 | 2 | SPECCED | rev-2 | 2026-11-15 |
<!-- /gen:build-units -->

Records: 13 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2 TOOL-aPiecewiseGrade-3.

Ids whose spec moved past its audited revision: none — 0 of 3 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aPiecewiseGrade-3` | no |
| 2 | `TOOL-aPiecewiseGrade-1` | no |
| 3 | `TOOL-aPiecewiseGrade-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
