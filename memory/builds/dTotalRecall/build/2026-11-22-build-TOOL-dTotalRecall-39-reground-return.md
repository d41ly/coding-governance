**Serves:** research TOOL-dTotalRecall-39

# TOOL-dTotalRecall-39 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-39-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-39-reground-spec-writer.md), in substance.

- Folded to rev-3; `check-spec-tokens.py --spec`, `--check-specs`, hygiene check 12 and pinned-facts read green; no sibling spec edited.
- The adapter already exists: PLAY-dOrderedCharter-28 landed `edge_grammar.py#read_header_edges(text, path, binding=None)`, reading only column-0 header lines; the old claim that neither definition existed is gone. The route to memory-tree is `tag_index.py#load_memory_tree`.
- Probes over scratch texts showed an import-time alias would lose the landed target check and let unit 19's plain `ValueError` escape the edge walk.
- F3 RESOLVED (agent, delegated): a site adapter `check_header_edges` replaces the landed reader, looks up `tree_lib.read_header_edges` per call, turns its `ValueError` into an `EdgeRefusal` and keeps the target check.
- F4 RESOLVED (agent, delegated): binding the reader makes the edge walk read the typed records' bulleted causes, three of which are clause ids pinned to a revision; `caused-by`'s row moves from `pin = "none"` to `pin = "clause"`, simulated green at HEAD; `edges.toml`, the playbook README and `help/tags.md` join Files touched.
- The arm moves to `check-memory-hygiene.test.sh` with two new plants; the criteria are rewritten as AC1 to AC5.
