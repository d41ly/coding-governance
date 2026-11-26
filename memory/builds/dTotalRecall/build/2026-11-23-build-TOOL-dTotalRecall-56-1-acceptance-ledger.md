# TOOL-dTotalRecall-56 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-56
**Caused-by:** TOOL-dTotalRecall-56

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-6 over base
`1e9a5ebab` and ran each probe below on node d, 2026-11-23, from `tools/memory-tree/` unless named: the
check over the working tree, the greps and the hash from the root, and the plant's fixture, which
`record_kinds.py#run_fixture` builds under the system temp directory and removes. §7's legs and the
`New arm:` RED-first observation of the plant `unkept-build-alias` in `record_kinds.py#run_selftest`'s `want`
are owed to the close.

**Evidences:** TOOL-dTotalRecall-56
- AC1 — `kept pinned instrument` — `python record_kinds.py --check` listed `alias-compare · memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py@30a1f15b:380 · kept pinned instrument`, read from its `tree_lib.py#CENSUS_KEPT_PATHS` row, and its build-folder count line `54 script(s) under memory/builds/*/build · 1 hits · 1 kept · 0 red` (DERIVED 2026-11-23, this probe). The check exited 1 on two `RED pocket` lines alone, `dHomedResolver` and `history-verdicts`, entries of the shared git common dir that no census of this unit reads and the close's `record-kinds` leg grades on its own node (DERIVED 2026-11-23, this probe). `git grep -c "census: kept" -- memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py` printed nothing and exited 1 (DERIVED 2026-11-23, this probe).
- AC2 — `unkept-build-alias` — `python record_kinds.py --fixture --plant unkept-build-alias` exited 1 with exactly one `RED` line, naming the fixture build bFix's planted probe script at its line 14 as comparing a retired kind token raw, line 14 being `tree_lib.py#BIND_HEAD_LINES` plus two (DERIVED 2026-11-23, this probe). With `tree_lib.read_kept_path` replaced by a reader keeping every path in a `python -c` probe, the plant exited 0 and listed the line `kept`, the staged break the `New arm:` names (DERIVED 2026-11-23, this probe). The arm's `--selftest` run and its RED-first observation are the close's (`record-kinds`).
- AC3 — `30a1f15bf67566aeaf5b7e1628483c630b23b416` — `git hash-object` on the deviations instrument printed it at the pass's working tree, the file unwritten (DERIVED 2026-11-23, this probe).
- AC4 — `ALIAS_COMPARE_KEPT` — `git grep -n ALIAS_COMPARE_KEPT -- tools` printed nothing and exited 1 (DERIVED 2026-11-23, this probe).
