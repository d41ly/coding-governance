# TOOL-aTrimmedHook-4 — acceptance ledger

**Serves:** journal TOOL-aTrimmedHook-4

No merge bar and no self-test suite ran in this pass. AC1 was observed by running `test_staged_render`
alone through a slice: every arm held, in 14.7 s. With the carry replaced by `pass` in a scratch copy,
the new arm printed FAIL, which is the arm observed RED.

**Evidences:** TOOL-aTrimmedHook-4
- AC1 — `gen_build_index.py --selftest` — a build README edit staged only into a copy of the index
  named by `GIT_INDEX_FILE` saw a render owed, and with no variable the default index held nothing
  staged and skipped; with the carry dropped, the first arm saw a skip.
- AC2 — amended rev-2 — `grep -n GIT_INDEX_FILE tools/memory-tree/gen_build_index.py` listed the leak
  list entry, the carry in `check_staged_render` and the `test_staged_render` arm that sets and restores
  it; the criterion first read that arm as a second reader, and its section 9 rev-2 line logs the change.
