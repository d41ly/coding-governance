---
slug: aTemperedLane
node: a
opened: 2026-11-25
streams: tooling
roster: TOOL
status: OPEN
ids: TOOL-aTemperedLane-1 TOOL-aTemperedLane-2
---

# aTemperedLane — the Red-fix lane's limits read past a generated region and read the guarded list at the commit's parent

## The problem this build exists to solve

The push boundary refuses nine pushed `Red-fix:` commits of the dBoundRoles run. Eight carry one
record row the index generator wrote into a spec, which L3 reads as a spec edit. One was committed
before the guarded list named its file, and L2 grades every commit against today's list. The RANGE
half reads no waiver, and built work is never rewritten in place.

## Expected improvements

- A record row the generator writes into a spec's `gen:spec-records` region is no L3 finding.
- A commit is graded against the guarded list that was in force when it was made.
- A fix commit that shortens the guarded list in itself is caught, which it is not today.

## Detriments if this is not built

- A finished run cannot land, and the next run whose index regen rides in a fix commit cannot either.

## Build-level rules

- Owner answers, 2026-11-25: "Fix gate on main" to the starting session, and "A: list at parent" to
  this one on which L2 rule lands. The landing ask covers these two changes and nothing else.
- **Classification (M2)**: two units at open, both MISSING, both Tier-2: each changes a shipped
  kit's contract. Order 1 then 2; both edit one function, so they build in sequence.
- Kit versions move through the lander's `mint`, once, after the last unit.
- No spec audit: none is declared, and the task's closed done-list names one adversarial review.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aTemperedLane-1` | L3 reads a spec change confined to the `gen:spec-records` region as no spec edit |
| 2 | `TOOL-aTemperedLane-2` | L2 reads the guarded list at the commit's first parent, the working tree's list where the parent has none |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-25 · streams tooling
ids TOOL-aTemperedLane-1 TOOL-aTemperedLane-2

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

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
