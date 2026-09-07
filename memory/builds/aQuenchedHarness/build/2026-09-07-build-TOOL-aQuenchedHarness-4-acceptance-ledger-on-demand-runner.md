# Acceptance ledger — TOOL-aQuenchedHarness-4

**Serves:** journal TOOL-aQuenchedHarness-4

**Evidences:** TOOL-aQuenchedHarness-4

Tier-2 · node a · 2026-09-07. One line per numbered criterion, each naming the observation that
answered it. A line saying MET without an observation is a checkbox, which is why the gate refuses
one; a line saying NOT MET is equally a result and is recorded the same way.

- AC1 — MET, OBSERVED — `bash tools/run-gates/run-selftests.sh --check` reports `declaration clean — 58 row(s), every held leg budgeted, every row resolvable`, asserting the declaration against the manifest in BOTH directions.
- AC2 — MET, OBSERVED — armed as `a suite that overruns its declared budget reds and NAMES the number it broke` in `tools/run-gates/run-selftests.test.sh`, green.
- AC3 — MET, OBSERVED — armed as `a HELD leg with no budget row reds` in the same suite, green.
- AC4 — MET, OBSERVED — armed as `a row naming a path git does not track reds`, green. It is also the arm that exposed the CRLF emitter, since every row read as untracked once the field order changed.
- AC5 — MET, OBSERVED — armed as `a --kit filter matching nothing REFUSES`, exit 2, green.
- AC6 — MET, OBSERVED — `bash tools/unattended/run-unattended-gates.sh` ran the six unattended suites through this runner on a frozen clone and produced their seconds; four came back RED, which is a fact about those suites and not about the runner.
- AC7 — NOT MET, and it changed shape. `OUTER` in `tools/run-gates/run-selftests.sh` divided the declared width by a pool of 4 that does not exist, because the run loop is SERIAL on purpose, so every ported suite was handed a quarter of the width it was owed -- 13.6 s against 7.9 s, measured on the first port. The constant is now 1 and the invariant is stated beside it; the peak-count observation the criterion asks for was NOT taken.
- AC8 — MET, OBSERVED — `tools/run-gates/kit.toml` claims `selftest-budgets.txt` as `project-owned`, so an adopter receives `run-selftests.sh` and not this repo's population.
- AC9 — MET, OBSERVED — the runner reads its width from `bash tools/run-gates/run-gates.sh --print-profile` rather than resolving a profile of its own, and `tools/lib/lib-selftest.test.sh` arms the other half: the harness reads `SELFTEST_INNER_WIDTH` and resolves nothing.
