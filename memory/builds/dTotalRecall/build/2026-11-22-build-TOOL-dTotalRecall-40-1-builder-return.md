**Serves:** journal TOOL-dTotalRecall-40

# TOOL-dTotalRecall-40 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `cab28c239` from [2026-11-22-prompt-TOOL-dTotalRecall-40-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-40-build-brief.md), recorded whole; the pass tip is `dc1fd17e7`.

## Why

TOOL-dTotalRecall-40 is built as written. The spec's claims held against the tree at base: `render_routes` already routed the logs row through `resolve_kind` but compared the typed rows and the research row on the raw token, and the census probe found exactly what spec section 4 derived (7 hits in 2 govkit files out of 381 tracked code files). No divergence.

## Summary

TOOL-dTotalRecall-40 is built and committed as dc1fd17e7, on base cab28c239. The spec status is CLOSED in the same commit, and the commit carries the `Pass: TOOL-dTotalRecall-40` trailer. No gate, suite or bar ran in this pass.

**What changed**
- `tools/memory-tree/gen_build_index.py`, `render_routes` (S1): each record's kind is now read once through `resolve_kind`, and every row compares that value: each typed kind, research, and logs. `--selftest` gains one arm: a build holding one `log` and one `journal` record must show both under `logs`. Because unit 4 had already routed logs through `resolve_kind`, no existing `build-routes` region changed bytes (spec F3).
- `tools/memory-tree/record_kinds.py` (S2):
  - New function `check_alias_compares(root, tool_rel)` returns `(lines, reds)`, is called from `check_record_kinds`, and prints its lines after the alias join.
  - It reads every tracked `*.py`, `*.sh` and `*.js` file under the tool root. It flags a quoted `KIND_ALIASES` key used as an `==`/`!=`/`===`/`!==` operand, inside the bracket after ` in (` or ` in [`, or as a `case` pattern in a `*.sh` file.
  - New constant `ALIAS_COMPARE_KEPT` exempts `govkit/shims.py` and `govkit/selftest.py` as `homonym: the shim's install.on-shim-call mode`. Both keys are built from parts because the install-prefix ban reads a literal kit path. The constant was written only after the predicate had run over the real tree.
  - Two new plants, `raw-alias-compare` and `alias-compare-kept`, are in `PLANTS`, `build_fixture` and `run_selftest`. The module docstring gains an alias-census paragraph and the section 7 "what it does not check" list.
- Records: the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-40-1-acceptance-ledger.md`, plus `RUN.md`. Generated rewrites from `gen_build_index.py --write` and `gen_map.py --write`: `memory/LIVE.md`, `memory/backlog/TOOL.md`, the dTotalRecall `README.md`, the spec's records region, and `memory/map/generated/symbols.json`. The generator also set the build's derived status to DEFERRED, because no unit is INPROGRESS any more.

**Checks that ran in this pass**
- AC1, standing in for the build-index selftest's new arm: I made a `--shared` scratch clone of the base under `%TEMP%/r40` (since deleted), copied in both edited modules, and added a `bRoutes` build with one `**Serves:** log TOOL-bRoutes-1` record and one `**Serves:** journal TOOL-bRoutes-1` record. `gen_build_index.py --write` exited 0, and the region's `logs` row named both records. It rewrote only that README, `memory/LIVE.md` and the month ledger.
- AC2, an `ast.get_source_segment` probe: no line of `render_routes` spells `journal`, and it calls `resolve_kind(`. A direct `render_routes` call on the log-and-journal build printed both records under `logs`.
- AC3, standing in for the `record-kinds` leg's red case: `record_kinds.py --fixture --plant raw-alias-compare` exited 1 with one RED line under alias-compare naming the planted `tools/planted/compare.py` at its compare line. The green fixture exited 0 with 0 hits.
- AC4: `--fixture --plant alias-compare-kept` exited 0 and printed the planted line as `kept homonym: ...`. Calling `check_alias_compares('.', 'tools')` directly on the real tree printed all 7 govkit hits as kept and 0 red; before the constant was filled, the same probe printed those 7 as red.
- The naming lexicon answered OK for `check_alias_compares`. Running `record_kinds.py --check` was refused to my role by the hook, as the `record-kinds` leg.

**Owed to the main loop at the close**
- The `record-kinds` leg (`record_kinds.py --check`) on the real tree. It covers the `--check` halves of AC3 and AC4.
- `build-index selftest` and the record-kinds `--selftest`, plus the other gates in spec section 7.
- RED-first observation of new arm 1 (`gen_build_index.py --selftest`, AC1): break it by comparing the written token in `render_routes`. The arm should fail with the `journal` record missing.
- RED-first observation of new arm 2 (`record_kinds.py --selftest`, AC3 and AC4): break it by removing the `check_alias_compares` call from `check_record_kinds`. The `raw-alias-compare` case should stop being red, and `alias-compare-kept` should stop showing its kept line.

**Skipped and not re-run**
- `unattended.sh --dispatch ... --writes memory/LIVE.md memory/backlog/TOOL.md memory/builds/dTotalRecall/README.md` hit its 100 s bound (rc 124, DERIVED from the builder's tool timeout) and wrote no row. Its own output says the first two are generated outputs that commits may carry undeclared. The build README was not in the original write set, so it was committed without being declared; the pre-commit hooks passed. This is recorded in a `Decided:` trailer.

**Other notes**
- The bug-class checklist (`gotchas.py --for-diff HEAD~1..HEAD`) ran and selected 36 classes. I checked these against the commit:
  - The fixture-finds-nothing risk is covered: the plant reds and the real tree has kept hits.
  - The plants use the real alias token from `KIND_ALIASES` and the real `ALIAS_COMPARE_KEPT` key, not stand-in values.
  - Nothing was written through a heredoc, and no table or inline fence was added to a record.
  - The ledger carries its Serves line, and files are read as UTF-8 with `splitlines`.
  - No class needed a fix.
- The commit trailer is `Co-Authored-By: Claude Opus 5`, as AGENTS.md and the brief require, not the harness reminder's `Opus 5.5`.
