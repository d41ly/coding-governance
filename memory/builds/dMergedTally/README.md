---
slug: dMergedTally
node: d
opened: 2026-09-16
streams: tooling
roster: TOOL
ids: TOOL-dMergedTally-1
---

# dMergedTally — the disposal guard counts raw findings on both sides of its subtraction

## The problem this build exists to solve

The build harness's disposal guard subtracts `blockers + highs` from `confirmed`. `confirmed` counts
raw skeptic-confirmed findings, and the synthesis agent typed the two severity counts over the items
it merged raw findings into. On dLoggedFlight's round-1 spec audit, 13 confirmed in 10 items came back
as 1 and 5 against a raw 3 and 6, so the guard demanded 7 folds of 4 MEDIUMs and refused the only
honest disposal. Count both sides in one unit.

## Expected improvements

- A synthesis that merges findings no longer makes an honest by-severity disposal impossible.
- The two severity counts are derived from ids the harness can check, not typed by an agent.
- A synthesis that places a confirmed finding nowhere, or twice, is a named degraded round.

## Detriments if this is not built

- Every audit whose synthesis merges findings halts the unattended harness at disposal.
- An operator has to dispose by hand, around a guard that is wrong, as dLoggedFlight did.

## Build-level rules

- **Tier-2, re-tiered after the code.** Taken Tier-1 at kickoff; `tier2-review.js` ships to adopters,
  so the recorded shipped-kit class makes it Tier-2. The spec was written after the code and says so.
- **Merge and push each need the owner's explicit ask.** Nothing here is a standing mandate.
- **No unattended-kit self-test suite runs.** The owner's standing instruction.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dMergedTally-1` | 2 | `tier2-review.js` derives the severity counts from each synthesis item's raw confirmed ids |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node d · opened 2026-09-16 · streams tooling
ids TOOL-dMergedTally-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dMergedTally-1 — the disposal guard counts raw findings on both sides of its subtraction](spec/2026-09-16-spec-TOOL-dMergedTally-1.md) | — | 2 | INPROGRESS | rev-2 | 2026-09-16 |
<!-- /gen:build-units -->

Records: 2 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dMergedTally-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
