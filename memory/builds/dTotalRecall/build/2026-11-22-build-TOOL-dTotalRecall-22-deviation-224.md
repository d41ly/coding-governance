# TOOL-dTotalRecall-22 deviation 224 — the names, return shape and fixture the cardinality check needed beside its inventory

**Serves:** deviation TOOL-dTotalRecall-22

- **Departs from:** `TOOL-dTotalRecall-22@rev-5` [§4 "Inventory", §4 "The check", §4 "The count", S5, AC5]
- **Hand-off:** spec-to-code
- **Before:** §4 "Inventory" mints `check_edge_bounds` and `Violation` in `design_lib.py` and `check_edge_cardinality`, `check_cardinality_mirror` and `read_relation_edges` in `edge_grammar.py`; S5 has the check exit 1 or 0 with its lines; §4 "The check" gives a README edge's `where` as the build's `README.md`; §4 "Output lines" spells the merge plant's builds `xA` and `xB`.
- **After:** beside the minted names the pass adds `tools/playbook/edge_grammar.py#parse_bound` (one end's value, an int or `many`, the one reading `read_edge_types` refuses by), `#derive_edge_bounds` (the `{type: (per_source, per_target)}` of every declared row, the bounds both the count and the mirror read), `#derive_cardinality_cell` (one kind row's expected cell, by §4's rule), `#run_cardinality_plant` (the four plants of §7), and the constants `#CARDINALITY_ENDS`, `#BOUND_RE`, `#CARDINALITY_PLANTS`, `#CARDINALITY_RECORD` and `#CARDINALITY_README`. `check_edge_cardinality` returns `(rc, lines)` and `main` prints them, so a plant reads the lines without a subprocess. A README edge carries no line, so its `where` is the README path alone. `tools/memory-tree/design_lib.py#check_edge_bounds` passes over a type its bounds do not name, so the derived `cites` and an unregistered type are not counted, and `Violation.members` holds each member edge whole; `tools/memory-tree/asbuilt_view.py#resolve_clause_rows` spells its derived relation's type `head`. The merge and branch plants build their repository on `gov_tag.py#build_tags_fixture` with `FAMILIES="playbook:PLAY"`, the empty stale-header waiver and a README per build with `status: OPEN`, since `gen_build_index.py --print-relations` refuses a tree lacking any of them, and name the builds `xAlpha` and `xBeta`, which the id grammar reads where it refused `PLAY-xA-1`. `derive-ceilings.py --write`, run for the leg's observed row, also carried the runner rows this node's local run records hold for legs that had no node `d` row, each a reading the runner took and none typed.
- **Cause:** builder discovery
- **Reason:** a bound's parse, the bounds table, the expected cell and the plants each need a name; a fixture build folder without a README, a family or the waiver is refused before any edge is read; `--write` moves every row of the node it names, and lowering one by hand is the hand edit its header forbids.
- **Evidence:** the pass commit of TOOL-dTotalRecall-22 and its acceptance ledger, `2026-11-22-build-TOOL-dTotalRecall-22-1-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-22
