**Serves:** research TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-26 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36

# Close observation brief — batch b, govkit selftest, first half

## The prompt

> Every buildable roster unit of dSafePassage is terminal (TOOL-dSafePassage-59 at 321ead788 was the last; TOOL-dSafePassage-61 stays held on TOOL-dGroundRules-13). BUILD-METHOD M8 owes each `New arm:` line a RED-first observation at the close, recorded in the unit's ledger.

## The brief

### Goal
For each of TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-26 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36: read its CLOSED spec's `New arm:` lines (in `memory/builds/dSafePassage/spec/`) that name tools/govkit/selftest.py; skip lines naming any other suite, which another batch observes. Observe each line at the close as BUILD-METHOD M8 asks: RED on the line's own staged break, then GREEN once restored. A line counts observed when its break reds at least one of its arms. Work only in a `git clone --shared` of this worktree at `83817478f` under `/tmp/<short-name>` (never under the session scratchpad, whose path breaks MAX_PATH and false-reds temp-root arms; never in a linked worktree, where govkit selftest grades the primary's HEAD). For govkit selftest, run one check function at a time (`python -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.<check_fn>(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`), never the whole suite; a shell suite may be sliced to the arm's block, the slice written beside the suite in the clone and never in this worktree. Return one ledger paragraph per unit in the grammar of `memory/builds/dGroundRules/build/2026-10-25-build-TOOL-dGroundRules-83-ledger.md`'s close paragraph: the suite, the break staged, one or two FAIL lines quoted and the GREEN result restored, or the reason a line could not be observed (a red at the clone's HEAD on arms the break does not touch is inconclusive, and said so). Bound every command to 900 s; the upgrade-walk leg and the closing review share the machine, so a slow case is load, not a red.

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
