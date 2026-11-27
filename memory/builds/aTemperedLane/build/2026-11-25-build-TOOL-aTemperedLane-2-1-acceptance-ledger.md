# TOOL-aTemperedLane-2 — acceptance ledger

**Serves:** journal TOOL-aTemperedLane-2

One builder pass from `77659d938`, on node a. It ran no merge bar, no self-test suite and no gate leg. The
fixture is the spec's g1 to g10 and a root commit with 30 fix commits on it, built under the temp folder by
`build_fixture` from a probe script of its own. Each staged break below replaced a function in the probe's
process, never an edit of this tree.

**Evidences:** TOOL-aTemperedLane-2
- AC1 — observed: `--red-fix-limits be10c468` exited 0, and 0 again with `read_guarded_paths` answering the run branch's list, which holds the agent file. With no parent list read, the second form exited 1 naming `L2` and that file.
- AC2 — observed: `--red-fix-limits` exited 1 for g5 and g6, each naming `L2` and its one path. With the working list read, both passed.
- AC3 — observed: `--red-fix-limits` exited 0 for g4, g8 and g9. With the two lists joined, g4 and g9 were refused; with the commit's own tree read, g9 was.
- AC4 — observed: `--red-fix-limits` exited 1 for g7 naming `L2` and `src/b.txt`. With the commit's own tree read, it passed.
- AC5 — observed: `--red-fix-limits` exited 1 for g2 and for the root commit, each with an `L2` line naming `src/a.txt`. With an absent list read as empty, both passed L2.
- AC6 — observed: `--red-fix-limits` exited 0 for g10 and, with the disk copy of `guarded-paths.txt` removed, 1 naming `L2` and `.governance/policy.toml`.
- AC7 — observed: `check_routed_commits` named `L2` for g2, g5, g6 and g7 alone, and `GIT_SPAWNS` rose by 0, 1, 2, 2 and 1 over no fix commit, the root, one, 30, and 30 with `KIT` outside. A read per commit reds the count. Answers paired with commits by position pass the whole-history run, which reads newest first, and red the same eight commits read oldest first, so the arm reads both orders.
- AC8 — observed: an unpinned read answered the replacing blob, and `--red-fix-limits` for g5 still exited 1 naming `L2`. With the batch read unpinned, it passed.
- AC9 — observed: 259 fix commits reachable from HEAD, 259 first parents holding a list, 0 `L2` findings by `check_red_fix_limits`.
- AC10 — observed: `grep -n "first parent"` answered the L2 row and a bullet of "What it does not check" in `help/red-fix-lane.md`, and `grep -c "itself shortened"` printed 0 over both files.
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC2 AC3 AC4 AC8: the working list read alone
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC2: a path under the agent folder exempt
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC3 AC4: the list read in the commit's own tree
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC3: the parent's and the working list joined
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC5 AC6: an absent parent list read as empty
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC6: an unresolved list turns L2 off
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC7: a read per commit
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC7: the answers paired with the commits by position
- seen-red — `routed-commits selftest` — red `7654f9db2` — green `7654f9db2` — AC8: the replace-refs pin dropped

A directory at the list's path and a list that is not UTF-8 each read as no list. The eight commits
of TOOL-aTemperedLane-1's AC1 still exit 0 under the verb.

## Owed to the close

Every leg the spec's section 7 names, and the RED-first observation of its four arms. The position
break of the AC7 arm reds its oldest-first half alone.
