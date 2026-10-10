# TOOL-aRoutedQuill-3 — acceptance ledger

**Serves:** journal TOOL-aRoutedQuill-3

No merge bar and no self-test suite ran in this pass. The leg's own `--selftest` ran from the kit on
node a and held all 27 arms in 44 s on a contended box. Three staged breaks were each observed red
against a scratch copy before the file landed: the path predicate returning nothing redded 17 arms,
reading the subject alone redded the trailer arms, and a batch answer that always said present
redded the spec-order arms. The lander half ran as a scratch-clone fixture of `push-main.test.sh`
case 26, against the built lander and against `HEAD`'s. The close still owes `push-main self-test`
run whole, with case 26 added under a budget that predates it, and `routed-commits selftest` under
the bar, plus the other legs §7 names.

**Evidences:** TOOL-aRoutedQuill-3
- AC1 — `routed_commits.py --selftest` — a commit naming `TOOL-tFix-1` after its spec passed; `TOOL-tFix-2` landing its spec with its code exited 1 naming its sha, the spec path and the parent's short sha. Staged break: a predicate grading nothing redded this arm.
- AC2 — `Pass: none` — an id-less commit and one whose only attribution is `Pass: none` each redded `no unit id`; a trailer naming the unit passed; a subject naming it with `Pass: none` passed. Staged break: the subject-only reading redded this arm.
- AC3 — `GATE_PUSH_BASE` — set to a fixture commit, the summary read `RANGE`, only later commits were graded, and a pushed violation listed in `ROUTED_COMMIT_WAIVED` still redded with `0 waived`. Unset, all zeros and a sha naming no commit each read `WHOLE` with its reason and redded a commit before that base.
- AC4 — `ROUTED_PATHS` — blank, an entry naming nothing tracked, `../src/`, `/src/` and `memory/` each exited 2 naming the key or entry; a blank cutoff and `yesterday` exited 2 naming `ROUTED_COMMIT_CUTOFF`; a `.git/shallow` file exited 2 naming `fetch-depth: 0`.
- AC5 — `graded 0` — a range of one exempt and two docs-only commits exited 0 printing `graded 0 — the range holds 3 commit(s)` and `ROUTED_PATHS src/`.
- AC6 — `git` — the spawn counter read 7 over 3 routed commits and 7 over 30, both exiting 0.
- AC7 — `GIT_COMMITTER_DATE` — two commits dated 2000 counted `2 exempt`, a merge counted `1 merge(s)`, and an id-less commit moving `src/m.txt` to `docs/m.txt` was the only red.
- AC8 — `ROUTED_COMMIT_WAIVED` — listing the three violations in WHOLE mode exited 0 with `3 waived`; adding a passing sha exited 1 naming it as stale.
- AC9 — `FAMILIES` — blank exited 2 naming the empty id map, a tracked spec whose H1 defines no id exited 2 naming it, a prefix `T|X` exited 2, and a log stream cut by one record exited 2 naming `parsed 2 commit(s)` against `git rev-list --count`'s 3.
- AC10 — `python tools/govkit/govkit.py selfcheck` — after `git add` and the subject-pin rows it reported no problem for either memory-tree leg. `routed_commits.py` over this repository printed `WHOLE (GATE_PUSH_BASE is unset)` naming the `2026-10-09` cutoff and exited 0, with 15 graded and the 5 commits other sessions landed earlier that day waived.
- AC11 — `tools/push-main.sh` — the selftest passed a `mint: kit versions onto origin/main at <sha8>` subject naming the unit with `Pass: none` in RANGE and redded the id-less one `no unit id`. The scratch-clone landing whose range named `TOOL-tFix-26` and moved the runlog kit committed `mint: kit versions onto origin/main at aaa4c3d0 for TOOL-tFix-26` with trailer `Pass: none` and landed. `HEAD`'s lander, same fixture, wrote a subject with no id and no trailer.
