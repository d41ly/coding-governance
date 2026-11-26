# TOOL-dTotalRecall-9 deviation 1006 — the finder's supersession map without the recall kit, a spec's record extent, the memory cell's wording and the sections cell's check

**Serves:** deviation TOOL-dTotalRecall-9

- **Departs from:** `TOOL-dTotalRecall-9@rev-7` [§2 S1, S3, S9; §4 "The rows"]
- **Hand-off:** spec-to-code
- **Before:** S3 hides a superseded record from every `find` and needs no recall kit for a filter-only one, while S7 names the served pairs' `fts_supersession` map, memory-recall's, as the map; S1 keys a spec's record by its defining H1 and §4's row table gives an id-anchored record no extent past its anchor; S9 has the memory cell name the card and the index each against the budget, in no wording; S2 has `read_sections` refuse a malformed cell and names no check that calls it.
- **After:** `tools/memory-tree/record_find.py#read_supersession_map` hands a filter-only `find` the served map where the recall kit resolves and `row_grammar.py#derive_relation_successors`, memory-tree's own derivation over the corpus, where it does not; a question and `budget` read the served map alone. `tools/playbook/record_extract.py#extract_record` spans a spec's defining-H1 record over its whole file, and `record_find.py#read_section` resolves an id anchored in several files to its spec first, then by path. `tools/playbook/memory_index.py#render_memory_line` prints `card <n> B within or over · MEMORY.md <n> B within or over · each its own <n> B budget` under `--card-bytes`, inside LINE_MAX, and its line without the flag is unchanged. `tools/memory-tree/record_kinds.py#check_row` reds a malformed `sections` cell through `read_sections`.
- **Cause:** builder discovery
- **Reason:** a filter-only find with no recall kit has no served map to hide superseded records by; a spec's H1 record holds only its title, so `record show <id>#<tag>` found no section in it and an id cited in a backlog row resolved to that row; the card part pushed the memory line past its cut at `tools/playbook/memory_index.py#LINE_MAX`; a malformed cell no check reads would refuse only at the door's next spec.
- **Evidence:** the pass commit of TOOL-dTotalRecall-9 and its acceptance ledger, `2026-11-22-build-TOOL-dTotalRecall-9-1-acceptance-ledger.md`
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-9
- **Made-by:** owner
