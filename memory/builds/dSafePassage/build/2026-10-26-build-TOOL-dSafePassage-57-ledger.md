**Serves:** journal TOOL-dSafePassage-57

# TOOL-dSafePassage-57 — acceptance ledger

The unit as built, at spec rev-2. The arm's guard line in `tools/push-main.test.sh` (line 1406) reads
`if [ -n "$_mt_rc" ] && [ -f "$HERE/$_mt_rc/check-arms.py" ]; then`: a bare `"$_mt_rc"`, never
`${_mt_rc:-`, so §4's Files-touched condition does not hold and the suite is not written. S4 is a
reading: TOOL-dSafePassage-52 AC1 is observed by this unit's AC1 and AC2 below, and its AC2's
`grep -c` stays a count of scan lines. This pass writes only this ledger and the spec's status header.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node d
(Windows, bash under Git for Windows) over this worktree at d3e027ba, by §4's arm probe written
verbatim to the run's scratchpad, with `f` defaulting to `tools/push-main.test.sh`.

Owed at the close: the `New arm:` line of §7 (tools/push-main.test.sh, covers AC1 AC2), observed RED
on a suite copy whose arm block sits above the `^_mt_rc=` scan run under `env -u _mt_rc`, and GREEN
in gov's own tree. The §7 legs `push-main self-test`, `foreign-prefix parity (every self-test at
three prefixes)`, `harness arms (fail branches armed or pinned)` and `spec tokens (a spec's own names
resolve)` run at the close's bar.

**Evidences:** TOOL-dSafePassage-57
- AC1 — `ok-branch` — the probe over `tools/push-main.test.sh` found the guard `if [ -n "$_mt_rc" ] && [ -f "$HERE/$_mt_rc/check-arms.py" ]; then`, holding `"$_mt_rc"` and no `${_mt_rc:-`, and its first half printed `ok-branch`.
- AC2 — `alone rc=127` — the probe's last two lines were `_: line 1: _mt_rc: unbound variable` and `alone rc=127`; no line read `after`; the probe exited 0.
- AC3 — `no arm` — with `f` set to the output of `git show "3708a705:tools/push-main.test.sh"`, the probe printed `no arm` and exited 1.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: One `New arm:` line, `tools/push-main.test.sh`. The same copy, run under `env -u _mt_rc`, printed `_mt_rc: unbound variable` and exited 1 with no `push-main.test: all cases ok` line. Restored as in unit 50.
