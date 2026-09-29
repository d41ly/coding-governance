# TOOL-aRepatriatedFork-25 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-25

Written by the unit pass on node a, 2026-09-29. No merge bar, no self-test runner and no whole suite
ran. Fixture repositories were built under the temp root and removed after. The one changed
self-test arm ran as a slice: `test_remedy_paths_are_real` imported from `selftest.py` and called
alone. A red-first run staged the pre-change file into the fixture or the tree, ran the same check,
and restored the file.

**Evidences:** TOOL-aRepatriatedFork-25
- AC1 — a fixture repository with the kit's `merge-rows.py` and `merge-rows.sh` under `scripts/memory-tree/`, the program run with no arguments — exit 2, and the wiring line read `git config merge.rows.driver 'bash scripts/memory-tree/merge-rows.sh %O %A %B %P'`. The output named no `tools/` and no `pyrun.sh`
- AC2 — the same fixture with `2143b6d6`'s `merge-rows.py` — the wiring line read `bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py %O %A %B %P`, so the control is red as required
- AC3 — a per-line scan of the 33 owned files with the gate's own counter program — 128 counted lines before, 68 after. Every S1 to S4 line is gone. The rows for `map_lib.py`, `map_imports.py`, `map_extractors.template.py`, `drift_report.py`, `recall_conf.py`, `ps-hygiene.py`, `derive-ceilings.py`, `check-method-carriers.sh`, `adopt-playbook.sh` and `check-workflow-syntax.js` left the ledger, and every other owned row fell by exactly its drained lines. `--write-ratchet` wrote 210 rows, down from 220. What remains in these files is comment prose and canonical-copy markers, which are `TOOL-aRepatriatedFork-27`'s, and the executing derived-base joins spec rev-3 §4 returns to the main loop. `bash tools/check-install-prefix.sh` reads clean with 5 declared waivers, the `map_lib.py` `REGEN_CMD` row struck, and `none rising`
- AC4 — the same fixture with `map_lib.py` under `scripts/codebase-map/` and an adopted `.codebase-map.conf` at the root — `REGEN_CMD` and `regen_cmd()` both read `python scripts/codebase-map/gen_map.py --write`. `2143b6d6`'s file in the same place read `python codebase-map/gen_map.py --write`. The sliced `test_remedy_paths_are_real` passed, and with the old root literal staged back into `map_lib.py` it failed on the new pin, `('python codebase-map/gen_map.py --write', 'python tools/codebase-map/gen_map.py --write')`
- AC5 — `bash tools/check-kit-versions.sh` exits 0 after twelve kits moved in every carrier: agent-cap 1.23, codebase-map 1.13, drift-audit 1.16, lexicon 1.11, memory-recall 1.20, memory-tree 2.104, playbook-render 1.12, process-monitor 0.8, review-harness and tier2-review 1.15, run-gates 1.12, settings-merge 1.10 and unattended 1.42. `govkit.py selfcheck` exits 0. The `govkit.py epoch` verb grades commits, so it ran against this unit's commit, as the commit message records
- S1 — `derive-ceilings.py --help` from the fixture named the manifest beside its own kit dir, and under `GATE_LEGS=custom/legs.json` it named `custom/legs.json`
