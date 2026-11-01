# TOOL-dTotalRecall-21 deviation 211 — the FTS builder re-spelled `build_fts_rows`

**Serves:** deviation TOOL-dTotalRecall-21

- **Departs from:** `PLAY-dOrderedCharter-18@rev-3`
- **Hand-off:** spec-revised
- **Before:** PLAY-dOrderedCharter-18 S1 moves memory-recall's FTS5 builder into `tools/memory-tree/id_grammar.py` under its name `build_index`, while PLAY-dOrderedCharter-19 S4 names `build_index(root, tree)` in `tools/playbook/tag_index.py` the one index writer, so two functions share one name and TOOL-dTotalRecall-21 must call both
- **After:** the FTS builder is `build_fts_rows(db, table, docs, *, blob="", digest="", crumb=False)` in `id_grammar.py`, every caller re-pointed in TOOL-dTotalRecall-21's pass, and `tag_index.build_index` stays the one index writer that calls it
- **Cause:** design defect
- **Reason:** One index writer is the clause's point: the FTS rows move into the one index file through its writer. Two functions named `build_index` in two kits that now call each other make every reader ask which one a line means, and the rename falls on the narrower function, whose callers all sit in the kit this unit rewrites, rather than on the parent's index verb six chain units cite.
- **Evidence:** the brief's shared interface I14 (`memory/builds/dTotalRecall/prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md:227-229`); reuse scout B's shared interface 3; PLAY-dOrderedCharter-18 S1; PLAY-dOrderedCharter-19 S4; TOOL-dTotalRecall-21 S1 and §8 F1
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role of dTotalRecall's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-21
