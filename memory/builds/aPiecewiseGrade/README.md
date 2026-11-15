---
slug: aPiecewiseGrade
node: a
opened: 2026-11-15
status: OPEN
streams: tooling
roster: TOOL
ids: TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2
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

- **Classification (M2)**: two units, MISSING at open, Tier-2: a new mode of a kit's checker, and the driver's call to it.
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
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-15 · streams tooling
ids TOOL-aPiecewiseGrade-1 TOOL-aPiecewiseGrade-2

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 2 bound to this build, across 1 record folder(s).

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
