# TOOL-aIndexedAnchor-1 — acceptance ledger

**Serves:** log TOOL-aIndexedAnchor-1
**Caused-by:** TOOL-aIndexedAnchor-1

One builder pass over base `1b161ee30`, committed by the main loop as `398ba9252` after the pre-commit hook
refused the builder's commit over the unstaged status and route edits. Each line below is a direct `python -c`
probe of the changed code; the stand-in re-run at `398ba9252` is the acceptance record beside this one.

**Evidences:** TOOL-aIndexedAnchor-1
- AC1 — `test_anchor_reads_the_index_mid_merge` exited 0: step 4, mid-merge, read `[]` for the anchor `a.py::h` the merged-in side defines.
- AC2 — the same run's steps 5 and 6 read `["x: a.py::h"]` after the staged rename of `h` to `h2`, before and after `git commit --no-edit`.
- AC3 — `test_anchor_resolves_at_index()` exited 0 over this tree, and `grep -c test_anchor_resolves_at_head` printed 0 in both gate files and in `symbols.json`.
- seen-red — `codebase-map kit selftest` — red `398ba9252` — green `398ba9252` — `test_anchor_reads_the_index_mid_merge`: `read_anchor_hashes` wrapped to force `head="HEAD"` reds step 4 with `['x: a.py::h']`; unwrapped it is green
