---
slug: aWitnessedCrash
node: a
opened: 2026-11-13
streams: tooling
roster: TOOL
ids: TOOL-aWitnessedCrash-1
status: OPEN
---

# aWitnessedCrash — the hygiene engine reds when bash reports a runtime error and runs on

## The problem this build exists to solve

On a commit that stages a memory file outside every build folder, `check-memory-hygiene.sh --staged` prints
`line 3611: ALFORM: unbound variable` and exits 0. Check 23 declares its maps with `declare -A` and no value, so they stay
unset; reading `${#ALFORM[@]}` under `set -u` is an expansion error that bash 5.3 reports and does not exit on. The command
fails, the `if` reads it as false, and the run goes on to a green verdict. The exit status cannot see this class at all.

## Expected improvements

- No commit prints the check-23 unbound-variable line again.
- A bash runtime error anywhere in the engine reds the run, so a check that stopped part-way never reads as a pass.

## Detriments if this is not built

- Every commit staging a non-build memory file prints a crash and passes, which teaches readers to ignore the line.
- The next non-fatal runtime error in a check silently disarms that check while the hook stays green.

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-1: one kit's engine and its suite.
- The witness reds on bash's runtime-error shape only; the engine's own notices and findings keep their verdicts.
- No spec audit: not declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aWitnessedCrash-1` | check 23's maps are declared set, and the engine reds on a bash runtime-error line on its own stderr |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-13 · streams tooling
ids TOOL-aWitnessedCrash-1

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
