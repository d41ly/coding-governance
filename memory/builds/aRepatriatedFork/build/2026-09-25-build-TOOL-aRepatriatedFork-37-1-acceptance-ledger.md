# TOOL-aRepatriatedFork-37 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-37

Written by the unit pass on node a. The unattended suite ran as a SLICE: its prologue, lines 1-535,
plus the S8 roster block that holds the arm, in a temp script inside the kit dir, removed
afterwards. The foreign layout was a scratch repository under TEMP holding the kit at
`scripts/unattended/`, gov's lib at `scripts/lib/`, the generator at `scripts/gen_build_index.py`, and
a receipt row whose `source` is `tools/memory-tree/gen_build_index.py`; it was deleted afterwards.

**Evidences:** TOOL-aRepatriatedFork-37
- AC1 — `tools/unattended/unattended.test.sh` — the slice in gov exits 0 at `SLICE n=35 st=0`
- AC2 — `tools/unattended/unattended.test.sh` — in the foreign layout the new slice exits 0 at `SLICE n=35 st=0`; the same slice over `HEAD`'s suite exits 1 at `SLICE n=34 st=1` printing `FAIL missing: the --write mode of scripts/memory-tree/gen_build_index.py`
- AC3 — `tools/unattended/adopt-unattended.test.sh` — the class grep returns three other lines, each expecting a file its own fixture lays: `adopt-unattended.test.sh:139` (seeded at line 51), the two check-31 lines under `vendor/harness/workflows/`, and `unattended.test.sh:1019`'s probe-log substring
- AC4 — `bash tools/check-kit-versions.sh` — exits 0 with unattended 1.40; `bash tools/unattended/check-unattended.sh` and `bash tools/unattended/adopt-unattended.sh --check` exit 0
