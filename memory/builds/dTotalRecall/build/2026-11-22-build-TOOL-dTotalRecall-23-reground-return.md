**Serves:** research TOOL-dTotalRecall-23

# TOOL-dTotalRecall-23 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-23-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-23-reground-spec-writer.md), in substance.

- Folded to rev-3 at HEAD `f711a9567`; `--check-specs`, `check-spec-tokens.py --spec` and hygiene check 12 exit 0; three stale pinned-facts rows are the main loop's to shrink.
- The index is the file `tag_index.py#derive_index_path` names, reached at call time; leg rows are written inside the landed `build_index` transaction after `remove_unheld_rows`; reader versions follow the tag index's module-closure rule.
- A third reader, `spec-head` in `design_lib.py`, serves `collect`'s Files touched and edges; `read_rows_at` reads the working tree only.
- S5 builds nothing: unit 21 rev-3 S8 already grades the recall leg over the node's index, so the old recall arm goes and AC8 becomes AC7.
- F4 re-measured on a clone at `f711a956`, each figure PINNED 2026-11-22 in the spec.
- F5, F6 and F7 RESOLVED (agent, delegated): rows written in `build_index`'s transaction; the index found through `derive_index_path`; a `spec-head` reader over a further deviation.
- Edges to units 21, 9 and 43 kept with their payloads reworded; no sibling spec edited.
