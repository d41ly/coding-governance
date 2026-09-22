# Acceptance ledger — TOOL-aQuenchedHarness-6

**Serves:** journal TOOL-aQuenchedHarness-6

**Evidences:** TOOL-aQuenchedHarness-6

Tier-2 · node a · 2026-09-07. One line per numbered criterion, each naming the observation that
answered it. A line saying MET without an observation is a checkbox, which is why the gate refuses
one; a line saying NOT MET is equally a result and is recorded the same way.

- AC1 — MET, OBSERVED — `bash tools/lib/extract-arms.sh tools/check-line-length.test.sh` produces an inventory identical to the pre-port one, diffed empty, and re-proved after each later change to the extractor.
- AC2 — MET, OBSERVED — one arm deleted from a scratch copy gives `17d16 < exactly at the limit passes` at exit 1, and with the suite's floor intact it gives UNEXTRACTABLE at exit 3 instead. Both layers seen.
- AC3 — MET for the suite that was ported: 31.9 s to 7.9 s is 4.03x against the declared 3.0x minimum, at the width `run-selftests.sh` exports.
- AC4 — MET, OBSERVED — `bash tools/run-gates/run-selftests.sh --rank` REFUSED on the real tree while the six unattended rows carried a budget rather than a reading, naming every one of them and computing no share at all.
- AC5 — NOT MET, and recorded as not met with the arithmetic. `bash tools/run-gates/run-selftests.sh --rank` reports 36031 s of recorded time over 58 rows and puts the declared 50% share on the TOP FIVE suites; the one suite ported carries 208 s of it, 0.6%. The share was NOT lowered to fit, and the survey record names every unported suite with its cost.
- AC6 — MET, OBSERVED — `bash tools/lib/extract-arms.sh` reports UNEXTRACTABLE by name at exit 3, and the survey found the state the criterion did not anticipate: PARTIAL extraction, which the tool used to wave through as a confident fraction and now refuses at exit 5.
- AC7 — MET, OBSERVED — `--rank` prints the condition each reading came from and reds on an unstated one; both branches armed in `tools/run-gates/run-selftests.test.sh`.
