# TOOL-dTotalRecall-40 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-40

No merge bar, no self-test suite and no gate leg ran in this pass; `record_kinds.py --check` is the
`record-kinds` leg, refused to the builder role, so the real-tree halves of AC3 and AC4 were observed by
calling `tools/memory-tree/record_kinds.py#check_alias_compares` directly, the arm `--check` runs, and the
leg itself is OWED to the close. Every probe ran on node d, 2026-11-22, from base `cab28c239`, over the
worktree before the pass commit. The gates of §7 and both `New arm:` RED-first observations are OWED to the
close, after the last unit is terminal.

**Evidences:** TOOL-dTotalRecall-40
- AC1 — `**Serves:** journal TOOL-bRoutes-1` — in a `--shared` scratch clone of base `cab28c239` under `%TEMP%`, the pass's two edited modules copied in, an added `memory/builds/bRoutes/` whose README types only `slug`, `opened`, `ids` and `status` and whose `build/` holds one record bound `**Serves:** log TOOL-bRoutes-1` and one bound `**Serves:** journal TOOL-bRoutes-1`, `python tools/memory-tree/gen_build_index.py --write` exited 0 and the README's `build-routes` region read one row, `logs`, naming both records; it wrote only that README, `memory/LIVE.md` and the month ledger, so no existing build's region changed bytes (§8 F3) and this pass re-renders none.
- AC2 — `ast.get_source_segment` — a `python -c` probe printed the `render_routes` segment of `tools/memory-tree/gen_build_index.py` with no line spelling the retired token and a `resolve_kind(` call in it, `True`; the same probe's `render_routes` over a build holding a `log` and a `journal` record printed both under `logs`, the subject of the `--selftest` arm this pass adds, whose RED-first observation is OWED.
- AC3 — `raw-alias-compare` — `python tools/memory-tree/record_kinds.py --fixture --plant raw-alias-compare` exited 1 with one RED line naming `tools/planted/compare.py:2` under `alias-compare`; `check_alias_compares` over the real tree listed no red hit (DERIVED 2026-11-22, the probe), and the `--check` half is OWED to the close as the `record-kinds` leg.
- AC4 — `alias-compare-kept` — `record_kinds.py --fixture --plant alias-compare-kept` exited 0 printing its planted line `kept homonym: the shim's install.on-shim-call mode`; `check_alias_compares` over the real tree printed every hit of the two govkit files §4 names as `kept homonym`, the population §4 derived (DERIVED 2026-11-22, the probe, before and after `ALIAS_COMPARE_KEPT` was written), and the green fixture printed its count line with no hit.
