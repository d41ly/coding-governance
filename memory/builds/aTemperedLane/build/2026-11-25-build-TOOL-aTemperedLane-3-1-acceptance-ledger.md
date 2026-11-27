# TOOL-aTemperedLane-3 — acceptance ledger

**Serves:** journal TOOL-aTemperedLane-3
**Caused-by:** TOOL-aTemperedLane-3

One builder pass from `4db37f5fb`, on node a. It ran no merge bar, no self-test suite and no gate leg. A
probe script cut the parent-list section out of `run_selftest` by its own text and ran it alone over scratch
fixtures under the temp folder: 13 of 13 arms held. Each staged break below replaced a function in the
probe's process, never an edit of this tree.

**Evidences:** TOOL-aTemperedLane-3
- AC1 — observed: `grep -c "absent from the working tree"` printed 1 for each of the three files, and each hit says both halves.
- AC2 — observed: `grep -c "the list still being present"` printed 1 for each page, and `grep -c "shortens the guarded list"` printed 0.
- AC3 — observed: `--red-fix-limits` for h7 exited 1 naming `L2` and src/b.txt, and 0 naming none once the disk copy was removed. With `resolve_guarded_path` answering the path with no file on disk, the second run named src/b.txt.
- AC4 — observed: `--red-fix-limits` for h3 exited 1 naming `L2` and src/a.txt. With `got[sha] = []` in the except, it passed, and no other arm turned.
- AC5 — observed: `--red-fix-limits` for h5 exited 1 naming `L2` and src/a.txt. With `got[sha] = []` in the None branch, it passed, as did g2 of unit 2, which shares the branch; the break of AC4 did not reach it.
- AC6 — observed: `--red-fix-limits` for m4 exited 1 naming `L2` and src/b.txt. With `parents[-1]` read, it passed, and no other arm turned.
- AC7 — observed: `read_blob_batch` raised `Refusal` for the first two streams in the words of section 4, and answered None and the blob's bytes for the third. Each refusal dropped, and a body skipped for a blob alone, turned this arm and no other.
- AC8 — observed: the check's python line exited 0 over `tools/memory-tree`, and 1 with `gen_build_index.check_marker_line`, then `routed_commits.check_marker_line`, replaced.
- AC9 — observed: `--red-fix-limits` exited 0 for each of the nine shas, and the diff from `7654f9db2` shows the module docstring, `build_fixture` and `run_selftest` alone.
- seen-red — `routed-commits selftest` — red `e7cae18c0` — green `e7cae18c0` — AC3: the list's path answered with no file on disk
- seen-red — `routed-commits selftest` — red `e7cae18c0` — green `e7cae18c0` — AC4: a list that is not UTF-8 read as empty
- seen-red — `routed-commits selftest` — red `e7cae18c0` — green `e7cae18c0` — AC5: a None answer read as empty
- seen-red — `routed-commits selftest` — red `e7cae18c0` — green `e7cae18c0` — AC6: the last parent read in place of the first
- seen-red — `routed-commits selftest` — red `e7cae18c0` — green `e7cae18c0` — AC7: the header refusal dropped, then the body refusal, then only a blob's body skipped
- seen-red — `marker contracts` — red `0a4783857` — green `0a4783857` — AC8: a local predicate using rstrip in `gen_build_index`, then in `routed_commits`

## Owed to the close

Every leg the spec's section 6 names, and the RED-first observation of its six arms. The break of AC3 also
turns the AC6 and AC7 arms of unit 2, whose readings stand on the same resolver.
