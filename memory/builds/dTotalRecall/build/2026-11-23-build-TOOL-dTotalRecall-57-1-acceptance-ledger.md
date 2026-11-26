# TOOL-dTotalRecall-57 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-57
**Caused-by:** TOOL-dTotalRecall-57

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-6 over base
`c736ff00f` and ran each probe below on node d, 2026-11-23, from `tools/memory-tree/` unless named: the
greps from the root, and the plant's fixture, which `record_causes.py#run_fixture` builds under the system
temp directory and removes. §7's legs and the `New arm:` RED-first observation of the plant
`kept-row-editable` in `tools/memory-tree/check-memory-hygiene.test.sh` are owed to the close.

**Evidences:** TOOL-dTotalRecall-57
- AC1 — `census: kept` — `python record_causes.py --fixture --plant kept-row-editable` exited 1 with exactly one `RED` line naming the row's path, `RED cause-writer CENSUS_KEPT_PATHS row tools/planted/editable.py: is no file under memory/builds/*/build/*, and an editable file is kept by its census marker: mark the kept line` followed by the marker `# census: kept <census> <reason>` (DERIVED 2026-11-23, this probe). With `tree_lib.py#KEPT_PATH_DOMAIN` rebound to `*` in a `python -c` probe of `record_causes.py#run_fixture`, the plant exited 0 and printed `record causes: green`, the staged break the `New arm:` names (DERIVED 2026-11-23, this probe). The arm's suite run and its RED-first observation are the close's (`memory-hygiene self-test`).
- AC2 — `ALIAS_COMPARE_KEPT|CAUSE_WRITER_KEPT` — `git grep -nE` over `tools` printed nothing and exited 1, and the spelled `fnmatch` probe over `tree_lib.py#CENSUS_KEPT_PATHS` printed `[]` and exited 0 (DERIVED 2026-11-23, this probe).
- AC3 — `check_alias_compares` — the spelled `python -c` probe, its `kept` the table plus one row naming `tools/memory-tree/tree_lib.py`, printed `1` (DERIVED 2026-11-23, this probe). Over the default table the alias census listed no red and its build-folder count line `54 script(s) under memory/builds/*/build · 1 hits · 1 kept · 0 red`, and `record_causes.py#check_cause_writers` no red and `104 code files under memory/builds/*/build · 9 census file(s) · 8 kept · 1 pinned · 0 red` (DERIVED 2026-11-23, this probe).
