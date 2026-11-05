---
slug: dFinishedRecord
node: d
opened: 2026-11-05
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dFinishedRecord-1
---

# dFinishedRecord — check 24 stops grading a run whose landing is already on the remote

## The problem this build exists to solve

Check 24 of the unattended kit gate skips a run record only when its recorded phase is `LANDED` or
`ABORTED`. An in-place landing leaves its record at `LANDING` forever, so a finished run stays graded.
When that build's roster grows after landing, check 24 asks for a `rescope · item add` row. The
`--rescope` verb reads the derived phase, sees LANDED and refuses (check 26), so no record can satisfy
both. dConvergedCharter's unit 41 hit this, and the bar refused its push. The prompt is in `prompts/`.

## Expected improvements

- Check 24 excludes a derived-LANDED record, as checks 7 and 23 already do.
- A finished run's roster can grow after its landing without redding the bar.

## Detriments if this is not built

- Any spec-only follow-up to a landed run reds the bar, and the only way past it is `--no-verify`.
- dConvergedCharter's post-landing records cannot land.

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-2: `check-unattended.sh` is a shipped kit
  file.
- The predicate is `check_derived_landed`, shared with checks 7 and 23. No second copy of it.
- Kit versions move through the lander's `mint`, never by hand.
- No spec audit: the owner declined one.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dFinishedRecord-1` | check 24's roster loop asks `check_derived_landed` after its recorded-phase skip and excludes a derived-LANDED record |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node d · opened 2026-11-05 · streams tooling
ids TOOL-dFinishedRecord-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dFinishedRecord-1 — check 24 stops grading a run that derived LANDED](spec/2026-11-05-spec-TOOL-dFinishedRecord-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-11-05 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dFinishedRecord-1.

Ids whose spec moved past its audited revision: none — 0 of 1 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dFinishedRecord-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
