# Acceptance ledger — TOOL-aQuenchedHarness-5

**Serves:** journal TOOL-aQuenchedHarness-5

**Evidences:** TOOL-aQuenchedHarness-5

Tier-2 · node a · 2026-09-07. One line per numbered criterion, each naming the observation that
answered it. A line saying MET without an observation is a checkbox, which is why the gate refuses
one; a line saying NOT MET is equally a result and is recorded the same way.

- AC1 — MET, OBSERVED — `bash tools/lib/lib-selftest.test.sh` arms it directly: the per-arm lines are byte-identical at width 1 and width 4, and the summary names the width each run used.
- AC2 — MET, OBSERVED — armed as `a wedged arm reds rather than hanging the suite` plus `and the arms after it still run`, green.
- AC3 — MET, OBSERVED — armed as `a suite that declared no arms REFUSES rather than reporting a clean sweep`, exit 2, green.
- AC4 — MET, OBSERVED — `bash tools/lib/extract-arms.sh tools/check-line-length.test.sh` returns an inventory byte-identical to the pre-port one, 18 arms both sides, recorded in this build's arm-inventory record.
- AC5 — MET, OBSERVED — armed as `a suite with a failing arm exits 1` and `and NAMES the arm that failed, with what it expected`, green.
- AC6 — MET, OBSERVED — armed at widths 1 and 4 through an exported `SELFTEST_INNER_WIDTH`, and the harness resolves no profile of its own, which is asserted by a second arm.
- AC7 — MET, OBSERVED — `python tools/lexicon/lexicon.py` exits 0 over the tree, and the pin was DRAINED 980 to 975 rather than raised, because every function this build added leads with a declared verb.
