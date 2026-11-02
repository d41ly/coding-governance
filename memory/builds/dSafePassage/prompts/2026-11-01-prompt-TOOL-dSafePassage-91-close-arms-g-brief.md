**Serves:** research TOOL-dSafePassage-91 TOOL-dSafePassage-92 TOOL-dSafePassage-93 TOOL-dSafePassage-94 TOOL-dSafePassage-95 TOOL-dSafePassage-96

# Close observation brief — batch g, the govkit selftest arms of TOOL-dSafePassage-91 to -96 in check_floor_bash, the rename and snapshot blocks of check_upgrade_steps, and the upgrade-walk graders

## The prompt

> Every buildable unit of dSafePassage is terminal (TOOL-dSafePassage-98 at 390033278 was the last of the review chain's promotions; TOOL-dSafePassage-61 stays held on TOOL-dGroundRules-13). BUILD-METHOD M8 owes each `New arm:` line a RED-first observation at the close, recorded in the unit's ledger.

## The brief

### Goal
For each of TOOL-dSafePassage-91 TOOL-dSafePassage-92 TOOL-dSafePassage-93 TOOL-dSafePassage-94 TOOL-dSafePassage-95 TOOL-dSafePassage-96: read its CLOSED spec's `New arm:` lines (in `memory/builds/dSafePassage/spec/`) in every suite they name; most sit in govkit selftest's check_floor_bash. 95's and 96's specs name breaks that must run several times (N = 6) because one run can go green by chance; run each the stated number of times. Observe each line at the close as BUILD-METHOD M8 asks: RED on the line's own staged break, then GREEN once restored. A line counts observed when its break reds at least one of its arms. Work only in a `git clone --shared` of this worktree at `390033278` under `/tmp/<short-name>` (never under the session scratchpad, whose path breaks MAX_PATH and false-reds temp-root arms; never in a linked worktree, where govkit selftest grades the primary's HEAD). For govkit selftest, run one check function at a time (`python -c "import sys,pathlib,tempfile; sys.path.insert(0,'tools/govkit'); import selftest as s; s.<check_fn>(pathlib.Path(tempfile.mkdtemp())); print(s.FAILURES)"`), never the whole suite; a shell suite may be sliced to the arm's block, the slice written beside the suite in the clone and never in this worktree. Return one ledger paragraph per unit in the grammar of `memory/builds/dGroundRules/build/2026-10-25-build-TOOL-dGroundRules-83-ledger.md`'s close paragraph: the suite, the break staged, one or two FAIL lines quoted and the GREEN result restored, or the reason a line could not be observed (a red at the clone's HEAD on arms the break does not touch is inconclusive, and said so). Bound every command to 900 s; the upgrade-walk leg and the closing review share the machine, so a slow case is load, not a red.

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
