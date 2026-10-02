# TOOL-aRepatriatedFork-47 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-47

Written by the unit pass on node a, 2026-09-30. No merge bar, no self-test runner and no whole suite
ran. The spec was committed at `542d35c1`, before any code. Each criterion ran its direct check. The
resolver self-test ran as SLICES in temp scripts inside the kit dir, removed afterwards: its prologue
with sections 2, 2b and 3c on the working tree, then prologue-plus-section slices in a scratch clone
carrying the change, where each red-first control was staged, observed and restored.

**Evidences:** TOOL-aRepatriatedFork-47
- AC1 — `tools/lib/resolve-python.test.sh` — `git grep -c '^# >>> resolve_prefix_token'` lists the canonical, the runbook, `check-spec-tokens.py`, `rank_harness.py`, `govkit.py`, the govkit selftest, `run-gates.sh` and `run-selftests.sh` at 2; `resolve_prefix_sh` lists `kit-rel.sh`, `check-dead-paths.sh` and `check-testsuite-counts.sh`. The parity slice passes with every block byte-identical to its canonical
- AC2 — `tools/run-gates/run-gates.sh` — one trailing byte added to its copy, the parity slice prints `inline copy of 'resolve_prefix_token' drifted` naming that file, block 1 of 1. Restored, it passes
- AC3 — `tools/run-gates/run-selftests.sh` — its SECOND block changed and the first left intact, the slice names the file, block 2 of 2. The `blk` extractor as it stands at `6830f257`, run on the same file, extracts a block equal to the canonical. Restored, it passes
- AC4 — `tools/lib/kit-rel.sh` — the behaviour section runs both canonicals over the six contract rows and both print them. With the shell canonical's bare-token result changed to `./`, the slice prints `the shell {prefix} canonical disagrees with the contract table`. Restored, it passes
- AC5 — `tools/check-spec-tokens.py` — with `x = s.replace("{prefix}/", "")` appended in the scratch clone, the ban slice names `tools/check-spec-tokens.py:935`. Removed, it is silent. The section's own plants fire once each on all four forms, and a plant inside a block is silent
- AC6 — `tools/check-kit-versions.sh` — exits 0 with run-gates bumped 1.15 to 1.16 in both carriers. `govkit.py shipped` lists `run-gates.sh`, `run-selftests.sh` and `check-testsuite-counts.sh` as engine rows; the last declares no version, and `rank_harness.py` is project-owned
- AC7 — `tools/check-dead-paths.sh` — it, `check-spec-tokens.py`, `check-testsuite-counts.sh` and `check_runbook_parity.py` each exit 0. `run-selftests.sh --list`, `--check` and `check-dead-paths.sh` printed byte-identical output before and after the change

Other direct checks: `check-install-prefix.sh` with an unchanged ratchet, `govkit.py selfcheck`,
`lexicon.py`, `encoding_posture.py`, `check-arms.py --check` and `test_codebase_map.py` after a map
regen exit 0. The whole resolver suite's executed count is the main loop's to record.
