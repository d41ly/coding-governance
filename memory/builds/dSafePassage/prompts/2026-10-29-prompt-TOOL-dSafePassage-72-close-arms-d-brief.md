**Serves:** research TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-78 TOOL-dSafePassage-84

# Close observation brief — batch d, govkit selftest arms of the promoted units

## The prompt

> Every buildable unit of dSafePassage is terminal again (TOOL-dSafePassage-81 at 1dba52743 was the last of the units the closing review promoted; TOOL-dSafePassage-61 stays held on TOOL-dGroundRules-13). BUILD-METHOD M8 owes each `New arm:` line a RED-first observation at the close, recorded in the unit's ledger.

## The brief

### Goal
For each of TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-78 TOOL-dSafePassage-84: read its CLOSED spec's `New arm:` lines (in `memory/builds/dSafePassage/spec/`) that name tools/govkit/selftest.py, or tools/govkit/upgrade_steps.py as a selftest-run plant; skip lines naming any other suite, which another batch observes. Observe each line at the close as BUILD-METHOD M8 asks: RED on the line's own staged break, then GREEN once restored. A line counts observed when its break reds at least one of its arms. Work only in a `git clone --shared` of this worktree at `b634d60e5` under `/tmp/<short-name>` (never under the session scratchpad, whose path breaks MAX_PATH and false-reds temp-root arms; never in a linked worktree, where govkit selftest grades the primary's HEAD). For govkit selftest, run one check function at a time (`python -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.<check_fn>(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`), never the whole suite; a shell suite may be sliced to the arm's block, the slice written beside the suite in the clone and never in this worktree. Return one ledger paragraph per unit in the grammar of `memory/builds/dGroundRules/build/2026-10-25-build-TOOL-dGroundRules-83-ledger.md`'s close paragraph: the suite, the break staged, one or two FAIL lines quoted and the GREEN result restored, or the reason a line could not be observed (a red at the clone's HEAD on arms the break does not touch is inconclusive, and said so). Bound every command to 900 s; the upgrade-walk leg and the closing review share the machine, so a slow case is load, not a red.

### Non-goals
Any write to a tracked file of this worktree; any commit; the merge bar; a whole govkit selftest run.

### Acceptance
One ledger paragraph per unit in the grammar of `memory/builds/dGroundRules/build/2026-10-25-build-TOOL-dGroundRules-83-ledger.md`'s close paragraph: the suite, the break staged, one or two FAIL lines quoted, and the GREEN result restored; or the reason a line could not be observed (a red at the clone's HEAD on arms the break does not touch is inconclusive, said so).

### Gates
No gate runs in this pass.

### Limitations
The upgrade-walk leg and the closing review share the machine; a slow case is load, not a red.

### Reuse
Each unit's own acceptance ledger in `memory/builds/dSafePassage/build/` records how its builder staged the break in its pass.
