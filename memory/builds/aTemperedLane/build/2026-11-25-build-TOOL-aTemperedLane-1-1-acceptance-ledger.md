# TOOL-aTemperedLane-1 — acceptance ledger

**Serves:** journal TOOL-aTemperedLane-1

One builder pass from `88f7870c4`, on node a. It ran no merge bar, no self-test suite and no gate leg. The
fixture is the spec's r1 to r15, built under the temp folder by `build_fixture` from a probe script of its
own, and graded by the `--red-fix-limits` verb run as a process. Each staged break below was a copy of the
kit in the session scratch directory, never an edit of this tree.

**Evidences:** TOOL-aTemperedLane-1
- AC1 — observed: the verb exited 1 for each of the eight shas before the edit, naming L3, and exited 0 printing `is inside all four` for each after it.
- AC2 — observed: `--red-fix-limits` exited 0 for r1.
- AC3 — observed: the verb exited 1 for r2, r3, r4 and r15, each naming `L3 spec edit` and the spec's path. With CRLF folded before the compare, r4 passed.
- AC4 — observed: the verb exited 1 for r5 to r9, each naming `L3 spec edit` and the path. With the marker lines cut beside the region, r5 and r9 passed; with the pair count unread, r7 passed.
- AC5 — observed: the verb exited 1 for r10 to r13 and for the parentless commit, each naming `L3 spec edit` and the path, both paths for r12. With the mode unread, r13 passed.
- AC6 — observed: the `--red-fix-limits` verb's `L3 spec edit` line for r14 named the second spec and not the first.
- AC7 — observed: `GIT_SPAWNS` rose by 0, 1, 2 and 2. The one-call case graded r11, r12 and r13 together.
- AC8 — observed: the maps of `load_spec_paths` from this tree and from `3d6c1702` were equal over 3139 ids. A lane history was admitted, exit 0 counting two red-fix commits, with its `LEG_MANIFEST` file in the tree, and read `cannot be checked`, exit 1, with a name its tree does not hold. A batch stream cut before a header and one cut inside a body were each a refusal.
- AC9 — observed: the four names are the same objects in `tree_lib` and `gen_build_index`; the `grep -c` of the definition printed 0; the arm's grep exited 0 over `tree_lib.py`.
- AC10 — observed: `grep -c "gen:spec-records"` printed 3, 1 and 3 over the three files, each says what L3 no longer checks, and `any other exactly one` printed 0 in `routed_commits.py`.
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC2: the exemption removed, every spec path kept as a finding
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC3: the compare dropped, any pair on both sides exempting
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC3: CRLF folded before the compare
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC4: the marker lines cut with the region
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC4: the pair count dropped
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC5: the mode unread
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC5: an added or deleted spec, the parentless one included, exempt
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC6: one exempt path clears the commit, then one edited path puts an exempt one back
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC7: one blob read per call
- seen-red — `marker contracts` — red `e7cae18c0` — green `e7cae18c0` — AC9: the predicate in `tree_lib` made to strip every trailing CR

## Owed to the close

Every leg the spec's section 7 names, and the RED-first observation of its two arms. In the
`routed_commits.py` arm r8 stands on two tests at once, the whole-line match and the kept marker line, so no
single drop makes it pass; the break that reds its group is r5's, r7's or r9's.
