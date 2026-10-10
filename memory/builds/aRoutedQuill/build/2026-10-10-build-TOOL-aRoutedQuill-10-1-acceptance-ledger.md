# TOOL-aRoutedQuill-10 — acceptance ledger

**Serves:** journal TOOL-aRoutedQuill-10

No merge bar and no held suite ran in this pass. The criteria were observed directly on node a in
the run's worktree, on the working tree at parent 620ab2f8 before the commit, through the module's
own `--selftest`, which is the direct check §6 names (31 arms held, 13.5 s). Two staged breaks were
observed red and restored byte-identical: with the WHOLE half never appended, which is the code
before this unit, five arms failed (AC1, both AC2 arms, the resolvable-base stale arm and the spawn
arm); with the WHOLE half appended in every context and the waiver read by both halves, five arms
failed (the unset, all-zeros and unresolvable-base arms, the RANGE no-waiver arm and the waived AC2
arm). On gov's own tree, `GATE_PUSH_BASE` at origin/main printed the RANGE line and a `WHOLE beside
RANGE` line (graded 45, 11 waived) and exited 0 in 2.7 s; unset, it printed the one WHOLE line. The
close still owes the `routed-commits selftest` and `routed commits name a specced unit` legs inside
the bar.

**Evidences:** TOOL-aRoutedQuill-10
- AC1 — `routed_commits.py` — a remote-side `remote: no id` commit merged into HEAD, `GATE_PUSH_BASE` at that remote tip: exit 1, the RANGE line at graded 1, a `WHOLE beside RANGE` line, the remote sha under `FAILED in WHOLE` and no RANGE FAILED heading; red against the unchanged leg.
- AC2 — `routed_commits.py` — a linear range at `0 merge(s)` with the needed sha unwaived exited 1 naming it under `FAILED in WHOLE`; with it listed it exited 0 with `1 waived` on the second line, the `WHOLE beside RANGE` line.
- AC3 — `routed_commits.py` — a pushed violation listed in `ROUTED_COMMIT_WAIVED` exited 1 under the RANGE heading with `0 waived` on the RANGE line; a waiver naming a clean commit at a resolvable base exited 1 with the stale line.
- AC4 — `routed_commits.py` — the spawn arm ran 3 and 30 routed commits unset and at the first commit; the `GIT_SPAWNS` deltas were equal within each context, and the arm failed when the WHOLE half was removed.
- AC5 — `routed_commits.py` — the unset, all-zeros and unresolvable-base arms assert no `WHOLE beside RANGE` line, and all three failed when the half ran in every context.
- AC6 — `.memory-tree.conf` — the three `grep -n` probes printed nothing, and `grep -c "beside"` counted 6 in the kit README and 5 in the dossier.
