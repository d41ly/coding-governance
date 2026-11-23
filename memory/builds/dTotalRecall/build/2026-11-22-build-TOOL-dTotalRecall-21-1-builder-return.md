**Serves:** journal TOOL-dTotalRecall-21
**Caused-by:** TOOL-dTotalRecall-21

# TOOL-dTotalRecall-21 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `e0cd68745` from [2026-11-22-prompt-TOOL-dTotalRecall-21-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-21-build-brief.md), recorded whole: a divergence, nothing committed.

## Why

DIVERGENCE: The spec says something about current code that is false, and building it as written would break the shared index file.

1. Spec section 4, "The rows", says: "`load_index`'s schema reset drops these tables with its own; the next open creates them and the next query re-extracts." At HEAD, `tools/playbook/tag_index.py#load_index` resets by reading every `sqlite_master` name with `type='table'` and running DROP on each one. That list includes each FTS5 table's hidden shadow tables (`fts_record_data`, `_idx`, `_content`, `_docsize`, `_config`). Dropping the FTS5 table itself drops its shadow tables, so the next DROP raises `no such table: fts_record_data`. The transaction rolls back and `load_index` raises a `TagError` saying the file cannot be opened.
   - Probe: a scratch git repo under `%TEMP%/r21p`. I opened `load_index`, created `fts_record` with the spec's column shape, then called `load_index(reset=True)` twice. Both calls refused with "the tag index .../.git/gov/index-s3.db cannot be opened: no such table: fts_record_data".
   - Effect: once recall's tables are in the shared file, `tools/playbook/gov_tag.py#remove_index` (which calls `load_index(reset=True)`) and any stamp-mismatch reset can never succeed. Every tag verb and every recall query would refuse until someone deletes the file by hand.
   - What it would have to say: the reset tolerates FTS5 tables, for example by dropping only names `sqlite_master` still lists at each step, or by dropping virtual tables first and then re-reading the list. `tools/playbook/tag_index.py` (`load_index`, plus its module docstring, which says "written by the extractors alone through `build_index`" and lists the tables) has to join section 4's Files touched. Because that is the surface of a CLOSED parent (PLAY-dOrderedCharter-55 S16), the spec should name the departure the way F5 does. Without that, it should also say who stops a reset from bricking the file.

2. Files touched is also missing paths the commit hooks need:
   - `memory/guides/SESSION-KICKOFF.md`: `.memory-tree.conf` is on the kickoff manifest's `watch:` list, so staging it needs the manifest re-stamped in the same commit.
   - The deviation record under `memory/builds/dTotalRecall/build/` that F5 says this pass writes.

Every other claim I probed holds at HEAD:
- The `tag_index` surfaces section 2 cites: `derive_index_path`, `load_index`, `derive_context`, `load_view`, `build_overlay`, `read_worktree_trees`, `common_git_dir`, `derive_worktree_key`, `TagError`.
- `id_grammar.py#build_index`'s shape, and the `corpus_inputs`, `extract_records`, `extract_supersessions` and `derive_supersession_map` signatures.
- The five freshness inputs in `query.py#ensure_cache`.
- The reader lists that AC1's and AC6's greps print.
- The `common_git_dir` parity row, and the `legacy-homes.txt` row for `RECALL_CACHE_BUDGET_MB`.
- All five new names, which pass `lexicon.py --suggest --as py.function`.

## Summary

I did not build TOOL-dTotalRecall-21: the spec cannot be built as written, so nothing is committed.

The blocker: section 4 says the index file's schema reset drops recall's new full-text tables along with its own. It doesn't. Each full-text table carries hidden helper tables, the reset tries to drop those after they are already gone, and it fails every time. So once recall wrote its tables into the shared file, `tools/playbook/gov_tag.py#remove_index` and any schema reset would refuse until someone deleted the file by hand. I reproduced this in a scratch repo under `%TEMP%`: `load_index(reset=True)` refused both times with "no such table: fts_record_data". The fix lives in `tools/playbook/tag_index.py#load_index`, which is outside this unit's Files touched and belongs to a CLOSED parent, so the spec needs revising first. The spec's Files touched also lacks `memory/guides/SESSION-KICKOFF.md` (staging `.memory-tree.conf` needs it re-stamped) and the deviation record that F5 says this pass writes. The full list is in `why`.

What ran:
- The `--brief` record: unchanged, already at 71f5fc050ac9.
- The scratch-repo probe of `load_index`, plus probes confirming the other code claims hold at HEAD. These were feasibility checks of the spec, not checks of any code of mine, so they stand in for no gate.
- The naming lexicon on all five new names: all pass.

Nothing was written, so I ran no gate, suite or bar, and skipped `gotchas.py --for-diff` because there is no commit to check. No command timed out. The staged `memory/builds/dTotalRecall/RUN.md` and the two untracked fold prompts for TOOL-dTotalRecall-36 in `memory/builds/dTotalRecall/prompts/` were already there and are not mine; I left them alone.

Still owed at the close once a revised spec is built: the two `New arm:` arms in section 7 (in `tools/memory-recall/selftest.py` and `tools/memory-recall/test_recall_floor.py`), each to be seen red first, and the legs on the spec's gates section.
