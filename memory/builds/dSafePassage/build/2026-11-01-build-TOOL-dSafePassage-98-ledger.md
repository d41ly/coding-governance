**Serves:** journal TOOL-dSafePassage-98

# TOOL-dSafePassage-98 — acceptance ledger

The unit as built, at spec rev-1. It writes no product code: its correction to TOOL-dSafePassage-97's
S3 is the one row of the spec's §4 "Correction to 97's text", and the skeptic's write-set probe is
pasted under §4 "The write-set probe". This ledger is the build output. The build commit also
carries 98's status flip and the generated renders. 96's and 97's authored text is as it was at
`e3038fea6`, and no file under the tools directory moves.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Every criterion was observed
on node a (Windows 11) from this worktree's root, by the spec's own command, run as written. Each
red case the spec names was re-observed by the same command with its stated substitution.

Owed at the close: the §7 legs at the bar. §7 declares no `New arm:` line, so no RED-first
observation is owed.

**Evidences:** TOOL-dSafePassage-98
- AC1 — printed `[('1', '4')] 3 []`. Red: with the row's `line 34:` read as `line 35:` in memory, it printed `[('1', '4')] 3 [('35', 'Observed by AC3.')]`.
- AC2 — printed `True 4 []`. Red: with `cc668aa42` in place of `e3038fea6`, it printed `False 5` and a third field naming 96's ledger, 96's spec and `tools/govkit/selftest.py`.
- AC3 — exited 0. Red: with `744d2551` in place of `ab71837da`, it exited 1.
- AC4 — printed `[True, True]`; `git diff --numstat e3038fea6 -- tools` printed nothing. Red: with `2ec06177f` in place of `e3038fea6`, it printed `[True, False]`; `git diff --numstat 744d2551 -- tools` printed one line, for `tools/govkit/selftest.py`.
