# TOOL-dTotalRecall-6 deviation 63 — the names, fallbacks and messages the relation reader needed beside its inventory

**Serves:** deviation TOOL-dTotalRecall-6

- **Departs from:** `TOOL-dTotalRecall-6@rev-4` [§4 "Inventory", S3, S5, S7, AC10]
- **Hand-off:** spec-to-code
- **Before:** §4 "Inventory" mints seven functions in `gen_build_index.py`; S3 has `read_relation_rows()` return None where no playbook kit resolves and `parse_relations` refuse a README carrying both `parents` and `depends-on`; AC10's base observation names `collect`'s line and the three loop readers' as the `get("parents"` hits.
- **After:** beside the minted names the pass adds `tools/memory-tree/gen_build_index.py#ORDER_TYPE` (the `after` type), `#PARENTS_ROW` (the `parents` row read where no kit resolves, its inverse `before`), `#RELATION_KEYS` (the six keys, the set refused untyped where no kit resolves), `#RELATION_FORMS`, `#BUILD_REF_FORMS`, `#WITHDRAWN_STATUS_RE`, `#load_edge_grammar` (the one import of the playbook kit's tag parser and resolver, from the directory `read_relation_rows` found) and `#test_relations` (the `--selftest` arms of section 7). `read_relation_rows` also answers None where the table holds no `[[front-matter]]` row, so an older playbook kit reads `parents` as before. The alias refusal is any two keys of one type, which today is the `after` pair alone; a relation key no row types is refused naming `edges.toml`. `plan()` attaches `known` and `inverses` to each build for `render_edges`, and a target written twice renders once. `#derive_front_matter` reads `build["parents"]`, `collect`'s `after` targets, in place of its own `fm.get("parents"` split, the fifth `get("parents"` hit at base that AC10's base observation omits. The module docstring names the card and lease refs as an eighth source. `tools/loop/budget.py#derive_patch_origin`'s no-parent refusal and `tools/loop/loop_parents.py#read_withdrawn_parents`' not-a-folder refusal name `depends-on:` beside `parents:`, and `help/loop.md` lists the plant `depends-on-parent`.
- **Cause:** builder discovery
- **Reason:** a constant, an arm home and the fallback each need a name; a playbook kit predating the table must not turn every `parents:` README into a refusal; AC10's grep cannot print nothing while `derive_front_matter` keeps its split.
- **Evidence:** the pass commit of TOOL-dTotalRecall-6 and its acceptance ledger, `2026-11-22-build-TOOL-dTotalRecall-6-1-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-6
