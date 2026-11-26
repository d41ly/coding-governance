# TOOL-aPrunedIndex-3 — acceptance ledger

**Serves:** journal TOOL-aPrunedIndex-3

No merge bar, no self-test suite and no gate leg ran in this pass, and nothing here opened either live index
file. Every reading is node a's, 2026-11-26, SQLite 3.53.4, Python 3.15.2, from base `47bd7e5b9`, by
`--fixture` plants and by one probe over a private copy in the run's scratch, opened through `load_index` with
`derive_index_path` pointed at the copy. Both new arms' staged reds, the legs of section 7, and AC4 and AC9
are owed at the close.

**Evidences:** TOOL-aPrunedIndex-3
- AC1 — `python tools/playbook/gov_tag.py --fixture --plant released-rows` — exit 0, one line per step, `lost` `[0, 0]` after every step. `left` read zero after steps 1 to 7, 14 and 17, and `[5, 3, 2]` at 8, `[10, 6, 4]` at 9, `[15, 6, 4]` at 10 and 11, `[10, 6, 4]` at 12, `[16, 10, 7]` at 13 and `[32, 18, 14]` at 16, each equal to the rows it named; both dumps equal; 49 s. Its staged reds are owed at the close. (PINNED, 2026-11-26)
- AC2 — `python tools/playbook/gov_tag.py --fixture --plant released-cost` — exit 0: the build's sweep 1395 steps, then 1395 after 320 padded rows, a delete on all three tables in each; the full sweep 469 steps, then 5029. Its staged reds are owed at the close. (PINNED, 2026-11-26)
- AC3 — `released-rows` — step 13's rebuild of a new commit left `[16, 10, 7]`, the three replaced edits and the three inserted rows, and after `run_gc` step 14 read `[0, 0, 0]`. (PINNED, 2026-11-26)
- AC4 — owed at the close: four `check` runs over a padded private copy of the clean index.
- AC5 — `EXPLAIN QUERY PLAN` over the five statements of `remove_released_rows`, 200 pairs in `released`, on a private copy of the clean 270,147,584-byte index opened through `load_index`, which built both SQL indexes: `SEARCH t USING INDEX tree_path_blob`, `SEARCH path_row USING COVERING INDEX path_row_key (path=? AND blob=?)`, `SEARCH t USING COVERING INDEX tree_path_blob`, `SEARCH blob_row USING COVERING INDEX blob_row_key`, `SEARCH blob_parsed USING COVERING INDEX sqlite_autoindex_blob_parsed_1`; the only scans are of `released` and `dirty_path`. The copy is the clean one, not AC4's padded one, which is owed. (PINNED, 2026-11-26)
- AC6 — `grep -n "remove_unheld_rows" tools/playbook/tag_index.py` — prints the definition taking `con` alone and the call in `remove_dead_versions`. `let go of` and `old edit` count 1 each in `tools/playbook/README.md`, `old uncommitted` 1 in `help/tags.md`, and the `ast.get_docstring` probe answered every clause of the criterion true.
- AC7 — `python tools/playbook/gov_tag.py --fixture --plant <case>` — `two-paths`, `dirty-revert`, `worktree-recreate`, `worktree-spelling`, `charter-dirty`, `two-versions` and `queued-writers` each exited 0, and so did `dirty`, `dirty-rename`, `dead-versions` and `named-probe`.
- AC8 — `released-rows` — the connection of step 7 read `doc.alpha#intro` again after step 9 and was served the same text, holding `g1`.
- AC9 — owed at the close: two `check` runs over a private copy of the 12.6 GB index.
- AC10 — `released-rows` — each of the six texts of step 15 was served as itself once put back, each staged save fired once, the failed read refused naming `memory/guides/ALPHA.md` with no row moved, the bytes that are not UTF-8 held `[2, 0, 2]` rows with no refusal, and after step 17 the dumps were equal. (PINNED, 2026-11-26)
- AC11 — `SELFTEST_ROWS` — the probe printed `released-rows|0|only replaced edits left, and nothing lost` and `released-cost|0|a sweep costs what was released`.
