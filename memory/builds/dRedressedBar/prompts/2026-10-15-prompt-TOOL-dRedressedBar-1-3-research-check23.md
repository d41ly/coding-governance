# Research — dRedressedBar: does hygiene check 23 red on other builds' ledgers at the base?

**Serves:** research TOOL-dRedressedBar-1

## The brief

### Goal
A full `bash tools/memory-tree/check-memory-hygiene.sh` at the build tip reds check 23 on eight dRedressedBar units with no acceptance ledger (owed at the close) and ALSO on ledger lines in builds aSparedSpawn and aOrientedCast, which this branch never touched. The full bar at the base `ebce889c7d7104fe4811707d6f17b2a486bf0fd6` recorded only check 17 as the hygiene red. Find out whether those foreign check 23 failures exist at the base or were made to bind by something on this branch, because that decides whether the close owes fixes outside this build's records.

### Items
1. Make a fresh clone into a SHORT path under `%TEMP%` (a long path breaks clones on Windows), check out the base sha, run `bash tools/memory-tree/check-memory-hygiene.sh` there, and capture its exit code and every `HYGIENE check N FAILED` line, quoting any check 23 line naming `TOOL-aSparedSpawn-` or `TOOL-aOrientedCast-`.
2. Run the same command in the worktree (it only reads) and capture the same.
3. If the foreign check 23 entries appear at the tip only, read check 23's code and `git diff --stat ebce889c7d7104fe4811707d6f17b2a486bf0fd6 HEAD -- memory/ tools/memory-tree/ .memory-tree.conf`, and name the change that makes them bind. If they appear at both, say whether the bar's `memory hygiene` leg runs this same command (read `tools/gate-legs.json`) and why the base bar's record shows only check 17.
4. Remove the clone.

### Acceptance
A short factual report: the exit code and failing check headers at each commit, where the foreign check 23 entries appear, and the cause if they appear only at the tip.

### Gates
none

### Non-goals
- No edit, stage or commit in the worktree. No gate leg beyond the one hygiene command.
