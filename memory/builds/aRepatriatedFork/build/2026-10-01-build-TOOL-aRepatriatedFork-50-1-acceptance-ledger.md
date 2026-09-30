# TOOL-aRepatriatedFork-50 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-50

Written by the VERIFYING repair pass R1 on node a, 2026-10-01. No merge bar and no whole suite ran.
The spec's rev-1 committed before any code. The new arm and the check 36 block each ran as a SLICE,
the suite's prologue plus that block, in a temp script inside the kit dir, removed afterwards. The
check 24 slice ran first over the `6e7cb0df` library and then over the built one. A first cut that
read `base:` through a new pipeline spelling was withdrawn before commit: it would have left check 36's
two staged breaks unable to reach it.

**Evidences:** TOOL-aRepatriatedFork-50
- AC1 — `ARCH-tRos-7` — the two-run slice draws no check 24 failure naming the unit specced between the runs. Red first: over the `6e7cb0df` library the slice failed `unexpected: … ARCH-tRos-7 in`, 10 assertions, one failing
- AC2 — `ARCH-tRos-9` — the same slice still draws the check 24 failure for the unit added after the second run went live, on both libraries
- AC3 — `lib-unattended.sh` — the check 36 slice passes 12 assertions over the built library, both staged breaks redding as before
- AC4 — `bash tools/unattended/check-unattended.sh` — run alone over the working tree with the built library, exits 0 and names no unit under check 24. Red first: the full bar at `6e7cb0df` named 19 `aRepatriatedFork` units there
