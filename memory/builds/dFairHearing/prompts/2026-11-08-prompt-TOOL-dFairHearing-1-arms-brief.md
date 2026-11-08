# Research brief — which run observed each New arm red

**Serves:** research TOOL-dFairHearing-1

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
For every `New arm:` line of this build's specs, find the suite log line that shows that arm RED on its staged break, and the log that shows it GREEN at the tip. Return one row per arm. Write nothing in the repository.

### Items
1. The arm list is the scratch file `all-arms.tsv` in the run's scratch directory, `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f/scratchpad/arms/`. It has 104 rows, each the unit number and its spec's `New arm:` line, which names the suite, the criteria it covers and the break it is staged on.
2. The logs sit in two folders beside it.
   - `out/` holds the run at the tip `4896589bc`. `u0-<suite>.log` is the GREEN baseline, and all twelve exited 0. `u<n>-<suite>.log` is that suite run in a clone of the tip with every non-test file unit `<n>`'s pass commits changed restored to the commit before its first pass; its second line lists what was restored.
   - `out-948/` holds the baseline at `948e4141b`, before unit 50, where six suites read red. Unit 50's arms are moved or repaired arms, so that baseline is their RED.
3. Match each arm to its RED line. Read the arm's own label and text in the suite (search the suite file in the worktree for its label, or for words of its description), then find that label's `FAIL` or `arm FAIL` line in the right log. A whole-unit revert also strips code later units added, so a log reds many arms: name the one line that is this arm's, never the log's first red.
4. An arm staged against another unit's code is observed in that unit's log. For example, units 26, 28 and 29 cut a rule out of a gate that unit 16 created, so the `u16-...` log is their RED; unit 27's `tier2-review` arm is staged against unit 23's harness, so `u23-...` is its RED. Say which log you used.
5. Arms in `tools/workflows/replay_scorer.py`, `tools/memory-tree/gotchas.py` and `tools/policy/check_policy.py` are in-file arms. No log here observes them; mark them `HAND`, with the break their line names.
6. When no log shows the arm red, mark it `UNSEEN` and say what break the main loop must stage by hand, from the arm's line and the suite's code.

### Acceptance
A return of exactly one row per arm in `all-arms.tsv` order: `<unit> · <suite> · <covers> · RED <log>:<line no> "<the FAIL line, at most 120 chars>" | HAND <break> | UNSEEN <break> · GREEN <u0 log>:<line no> "<the ok line>"`. Then a count line: RED, HAND and UNSEEN totals. A GREEN cell names the arm's own `ok` line in the tip baseline.

### Gates
None you run. Read files and grep; run no suite, no bar and no gate.

### Non-goals
No writes, in the repository or the scratch directory. No judging whether an arm is well designed.
