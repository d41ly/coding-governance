# TOOL-dTotalRecall-21 deviation 1003 — recall writes its own fts_ rows on the tag index's connection

**Serves:** deviation TOOL-dTotalRecall-21

- **Departs from:** PLAY-dOrderedCharter-19@rev-8
- **Hand-off:** spec-to-code
- **Before:** PLAY-dOrderedCharter-19 S4 has the one index file written by the extractors alone through tools/playbook/tag_index.py#build_index, and deviation 211's after-clause has that writer call the FTS builder
- **After:** memory-recall writes its five fts_ tables on the connection tag_index.py#load_index opens, in its own BEGIN IMMEDIATE pass after tag_index.py#load_view (tools/memory-recall/query.py#write_recall_rows), and tools/memory-tree/id_grammar.py#build_fts_rows is called by recall, never by tag_index.build_index
- **Cause:** builder discovery
- **Reason:** tag_index.py#build_index returns at once for a tree tree_built holds under the extractor digest, so rows written inside it never move on an alias or conf edit to a built tree, failing TOOL-dTotalRecall-21 AC3, and it would make the playbook kit call the kit that requires it; recall's own pass on the one file keeps the one file the clause asks for (TOOL-dTotalRecall-21 §8 F5)
- **Evidence:** TOOL-dTotalRecall-21 §8 F5 and S2; tools/playbook/tag_index.py#build_index; tools/memory-recall/query.py#write_recall_rows and #load_served_set in the pass commit
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dTotalRecall-21 under the build's author-recorded value (PLAY-dClosedLoop-4)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-21
- **Made-by:** lease-dTotalRecall
