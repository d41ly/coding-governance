# PLAY-dOrderedCharter-70 deviation 702 — three Design sentences built wider, each to make its own criterion observable

**Serves:** deviation PLAY-dOrderedCharter-70

- **Departs from:** `PLAY-dOrderedCharter-70@rev-1` [Design]
- **Hand-off:** spec-to-code
- **Before:** M8's site table changes `read_index_rows` by filtering its `path_row` dump on the conf key alone; L1's arm copies the kit's `*.py` alone; `check_source_rows` reds a line whose first tab cell starts `memory/builds/`.
- **After:** `read_index_rows` also leaves out a blob row and a `blob_parsed` row that only a path row of another conf key reaches; the L1 arm copies the whole kit directory, `__pycache__` aside; `check_source_rows` reads a line as a row only where it carries a tab.
- **Cause:** builder discovery
- **Reason:** with the table's change alone the `charter-warm` plant reads its warm dump DIFFER from a cold one: the old charter's blob, still in the tree, keeps the `extract_doc` rows the old conf asked for, which a cold build under the new conf never writes, so AC11 could not hold; the added filter is the existing rule for another version's rows, applied to another conf's, and a blob row no path row reaches still prints, so a missed sweep still shows. The `*.py` copy exits 1 before check 18 runs, because `corpus_ids` asks `check-memory-hygiene.sh` for its sets, so AC24's line could never print. Without the tab rule the predicate also hits a `.gitattributes` example line in `tools/memory-tree/README.md`, where the Design section pins `positional-refs.txt` as its only hit.
- **Evidence:** the `charter-warm` and `charter-dirty` plants printed `incremental rows DIFFER from a cold build's` before the filter and `equal` after it; the copied kit's `--check` printed `corpus_ids ... check-memory-hygiene.sh is missing` before the whole-kit copy and the check 18 line after it; `check_source_rows` over this tree named the README's one line before the tab rule and nothing after it, and named `tools/playbook/positional-refs.txt` with 38552 rows with the new `[[files]]` block removed.
- **Risk:** stricter
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-70
