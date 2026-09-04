# TOOL-dRetiredFork-6 — acceptance ledger

**Serves:** journal TOOL-dRetiredFork-6

**Evidences:** TOOL-dRetiredFork-6
- AC1 — `python3 tools/drift-audit/selftest.py` — a moved counter renders `PARTIAL:` in both harnesses, and a consumer re-deriving it byte-matches because both the run and the arm call the same two extracted functions
- AC2 — `python3 tools/drift-audit/selftest.py` — nothing-moved renders `CLEAN:`, asserted distinct from the bare word `complete` the ternary emitted and, by a fourth arm, distinct from the other two states
- AC3 — `python3 tools/drift-audit/selftest.py` — the dead state renders `DEAD PROBE:`; observed RED first by reinstating the ternary's fall-through, under which the same counters rendered `PARTIAL: 3 lens(es) and 0 skeptic batch(es) died, 0 finding(s) unverified` and the suite exited 1
- AC4 — `node tools/workflows/check-workflow-syntax.js` — exits 0, 4 workflow scripts parsed clean
- AC5 — `bash tools/check-kit-versions.sh` — exits 0 after 1.8 to 1.9 across all FOUR pairings: the constant in `drift_report.py`, the README marker, and each harness's `meta.version` AND its own `gov:kit` marker

## One arm that passed for the wrong reason, recorded rather than trusted

Under AC3's staged break the DISTINCTNESS arm still passed: the dead fixture's counters differ from
the partial fixture's, so their two `PARTIAL:` sentences differ as strings even though the STATE
classification was wrong. Distinctness alone would therefore not have caught the ternary. The
DEAD PROBE arm is the load-bearing one, and this is why there are four arms per harness and not one.
