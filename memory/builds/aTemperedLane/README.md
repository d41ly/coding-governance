---
slug: aTemperedLane
opened: 2026-11-25
ids: TOOL-aTemperedLane-1 TOOL-aTemperedLane-2 TOOL-aTemperedLane-3
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
- A line a fix commit itself removes from the guarded list, the list still being present, still guards, which it does not today.

## Detriments if this is not built

- A finished run cannot land, and the next run whose index regen rides in a fix commit cannot either.

## Build-level rules

- Owner answers, 2026-11-25: "Fix gate on main" to the starting session, and "A: list at parent" to
  this one on which L2 rule lands. The landing ask covers these two changes and nothing else.
- **Classification (M2)**: two units at open, both MISSING, both Tier-2: each changes a shipped
  kit's contract. Order 1 then 2; both edit one function, so they build in sequence. Unit 3 is the closing review's batch (M4).
- Kit versions move through the lander's `mint`, once, after the last unit.
- No spec audit: none is declared, and the task's closed done-list names one adversarial review.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aTemperedLane-1` | L3 reads a spec change confined to the `gen:spec-records` region as no spec edit |
| 2 | `TOOL-aTemperedLane-2` | L2 reads the guarded list at the commit's first parent, the working tree's list where the parent has none |
| 3 | `TOOL-aTemperedLane-3` | the closing review's mediums and lows: the deleted-list gap stated and pinned, and four arms |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node a · opened 2026-11-25 · streams tooling
ids TOOL-aTemperedLane-1 TOOL-aTemperedLane-2 TOOL-aTemperedLane-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aTemperedLane-1 — the Red-fix lane's L3 reads a spec change confined to the `gen:spec-records` region as no spec edit](spec/2026-11-25-spec-TOOL-aTemperedLane-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-11-25 |
| [TOOL-aTemperedLane-2 — limit L2 reads the guarded list at the commit's first parent](spec/2026-11-25-spec-TOOL-aTemperedLane-2.md) | 2 | 2 | CLOSED | rev-1 | 2026-11-25 |
| [TOOL-aTemperedLane-3 — the closing review's three mediums and two lows: one false claim corrected and pinned, four coverage gaps given arms](spec/2026-11-25-spec-TOOL-aTemperedLane-3.md) | 3 | 1 | CLOSED | rev-1 | 2026-11-25 |
<!-- /gen:build-units -->

Records: 8 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aTemperedLane-1 TOOL-aTemperedLane-2 TOOL-aTemperedLane-3.

Ids whose spec moved past its audited revision: none — 0 of 3 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aTemperedLane-1` | no |
| 2 | `TOOL-aTemperedLane-2` | no |
| 3 | `TOOL-aTemperedLane-3` | no |

A step's `Parallel` yes means its units share an order; `doc.build-method#m6-passes-commits-parallelism` still sequences two of them whose write sets intersect at dispatch.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| the units | the units table above |
| briefs | `2026-11-25-prompt-TOOL-aTemperedLane-3-brief.md`, `2026-11-25-prompt-TOOL-aTemperedLane-1-brief.md` |
| reviews | `2026-11-25-review-TOOL-aTemperedLane-1-closing-diff-review-round1.md` (CLEAN WITH FIXES) |
| red-fix | `2026-11-25-build-TOOL-aTemperedLane-3-red-fix-1.md` |
| logs | `2026-11-25-build-TOOL-aTemperedLane-3-1-acceptance-ledger.md`, `2026-11-25-build-TOOL-aTemperedLane-2-1-acceptance-ledger.md` and 2 more under build/ |
| card ref | `refs/gov/builds/aTemperedLane/card` |
<!-- /gen:build-routes -->
