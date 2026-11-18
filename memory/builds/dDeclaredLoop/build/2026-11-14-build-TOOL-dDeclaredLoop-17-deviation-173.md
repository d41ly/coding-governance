# TOOL-dDeclaredLoop-17 deviation 173 — the leg's exempt row, the two stand-in verbs' usage rows and the stand-in's helpers the spec did not name

**Serves:** deviation TOOL-dDeclaredLoop-17

- **Departs from:** `TOOL-dDeclaredLoop-17@rev-4` [§4 The leg and its plants, §4 Inventory, §5 testing]
- **Hand-off:** spec-to-code
- **Before:** the spec at rev-4 ships the leg `loop computed witness` as a row of `tools/gate-legs.json` with no descriptor row and says the govkit selfcheck's descriptor-to-manifest join is untouched; it names one usage row, `script:{prefix}/loop/loop_witness.py`; its inventory mints `run_witness_commands`, `run_fixture` and `main` in the stand-in; and it gives `rerun` no `--root`.
- **After:** the leg also carries an `[[exempt_leg]]` row in `tools/govkit/registry.toml`, as `core selftest` does; `tools/govkit/usage.toml` also carries `script:{prefix}/loop/loop_witness.py#acceptance` and `#rerun`, each anchored on `help/loop.md`; the stand-in also carries the helpers its verbs and plants share (`read_memory_tree`, `read_clean_env`, `read_git`, `resolve_commit`, `remove_tree` over the memory-tree kit's own, `run_acceptance`, `run_rerun`, `run_selftest`, the fixture writers and one `check_<case>_plant` per plant); and `rerun` reads the repository at the current directory.
- **Cause:** builder discovery
- **Reason:** the govkit selfcheck reds a manifest leg that no descriptor claims and no `[[exempt_leg]]` row carries, so the gov-only leg the spec chose needs the row that says so; the docs leg tests every command a help page shows against a declared verb and its flags, so the page's stand-in commands need their verbs' rows; the helpers keep each plant one function and the git reads one spelling.
- **Evidence:** the pass commit of `TOOL-dDeclaredLoop-17`, `tools/govkit/govkit.py#selfcheck`, `tools/govkit/docs_leg.py#check_page_command`, and the acceptance ledger `2026-11-14-build-TOOL-dDeclaredLoop-17-1-acceptance-ledger.md`.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage script:{prefix}/loop/loop_witness.py#acceptance
- **Caused-by:** TOOL-dDeclaredLoop-17
