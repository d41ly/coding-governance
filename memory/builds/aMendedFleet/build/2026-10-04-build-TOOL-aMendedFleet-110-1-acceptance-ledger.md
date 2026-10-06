# TOOL-aMendedFleet-110 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-110

**Evidences:** TOOL-aMendedFleet-110
- AC1 — `python tools/drift-audit/drift_report.py --check --base-ref HEAD` — in a `git clone --local` under a short `%TEMP%` path with the unit's change and its CLOSED spec committed, the unedited layer exited 0; with `closed_specs_with_no_product_commit` removed from `BASELINES` and set in `PINS` at 50 it exited 1, and stderr carried one RATCHET WEAKENED line naming the signal, 50 and the base set's 1 ids at HEAD
- AC2 — `BASELINES = {}` — the same clone with `PINS` at 3 and 2, one above each base set's size of 2 and 1, exited 1 with one RATCHET WEAKENED line per signal
- AC3 — `BASELINES = {}` — the same clone with `PINS` at 2 and 1, exactly the base sizes, exited 0 and printed no RATCHET WEAKENED line
- AC4 — `tools/drift-audit/drift_report.py` — with the new loop deleted and `if not baselines: return []` restored in the clone, signature kept, the AC1 and AC2 edits each exited 0, so both criteria tell the fixed code from the broken one
- AC5 — `grep -n "pinned no higher than" tools/drift-audit/README.md` — hit line 303, inside the `BASELINES` paragraph
