# PLAY-dOrderedCharter-51 deviation 513 — `--gc` also sweeps the rows no live tree holds, and unit 44's `extractor-edit` plant counts served rows

**Serves:** deviation PLAY-dOrderedCharter-51

- **Departs from:** `PLAY-dOrderedCharter-51@rev-1 [§2 S5]`
- **Hand-off:** spec-to-code
- **Before:** S5 has `--gc` delete the rows, ledger rows and `tree_built` rows of every `(extractor, version)` pair no live worktree derives; §4 names `tag_index.py` and `gov_tag.py` as the files touched; and unit 44's `extractor-edit` plant counts every `blob_row` of the old version and every `blob_parsed` row of another version, asserting `0 rows of the old version`.
- **After:** `--gc` deletes those rows, then runs the sweep every build already runs, `remove_unheld_rows`, so a pruned worktree's tree and the rows only it held leave too; `extractor-edit` counts the old version's rows the view serves, printing `0 rows of the old version served`; and the pass also writes the selftest rows in `tools/playbook/adopt-playbook.sh` (the `New arm:` line's file), `help/tags.md`, and the `--gc` flag on `gov_tag.py`'s row in `tools/govkit/usage.toml` with the page's re-derived fingerprint.
- **Cause:** builder discovery
- **Reason:** S2 keeps every version's rows, so unit 44's count of stored old rows reds by design and S3's served view is what "no old row" now means; AC4 asks the live worktree's dump unchanged after `--gc`, and that dump leaves out only rows another LIVE worktree holds, so once the worktree is pruned its tree's rows enter the dump unless the collection sweeps them; the docs and usage rows follow the charter's `[docs]` rule for a new flag.
- **Evidence:** `python tools/playbook/gov_tag.py --fixture --plant two-versions` printed `the live dump unchanged`; `--plant extractor-edit` printed `0 rows of the old version served`; `tools/govkit/docs_leg.py`'s `derive_usage_fingerprint` over the row with `--gc` gives `6cb6638a`.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `report` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-44
