# TOOL-dTotalRecall-21 deviation 1004 — the tag index's reset drops virtual tables first, then re-reads its table list

**Serves:** deviation TOOL-dTotalRecall-21

- **Departs from:** PLAY-dOrderedCharter-55@rev-7
- **Hand-off:** spec-to-code
- **Before:** PLAY-dOrderedCharter-55 S16 resets a stale-stamped or reset-asked index file in place by dropping every table one read of sqlite_master lists, then creating SCHEMA's tables, in one BEGIN IMMEDIATE transaction
- **After:** tools/playbook/tag_index.py#load_index first drops every table sqlite_master lists with sql LIKE 'CREATE VIRTUAL TABLE%', each drop removing its shadow tables, then reads the list again and drops what it still names, then creates SCHEMA's tables, in the same one transaction and the file never unlinked
- **Cause:** builder discovery
- **Reason:** once memory-recall's FTS5 tables share the file, a list read once names an FTS5 table's shadow tables after the table's own drop removed them, the next DROP refuses no such table, and every later reset, gov_tag.py#remove_index among them, refuses the same way; dropping a shadow table by name is refused under SQLITE_DBCONFIG_DEFENSIVE, so only the virtual-first order never names one (TOOL-dTotalRecall-21 §8 F8)
- **Evidence:** TOOL-dTotalRecall-21 §8 F8, S10 and AC8; memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-21-1-builder-return.md; tools/playbook/tag_index.py#load_index in the pass commit
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dTotalRecall-21 under the build's author-recorded value (PLAY-dClosedLoop-4)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-21
- **Made-by:** lease-dTotalRecall
