# Fix brief — TOOL-dFairHearing-1: an address rule run B's calibration can meet

**Serves:** research TOOL-dFairHearing-1

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md` so a correct build reproduces the baseline's own figures. The builder's DIVERGENCE is `memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-1-1-builder-return.md`, and the probe it ran is in the run scratch at `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dfairhearing-fe4e9c/db957487-b5c0-4a88-ab27-88dd90bc468f/scratchpad/calib.py`. Commit nothing; the main loop commits.

### Items
1. Mark the choice in §8 as a new fork in the shape `memory/TEMPLATE-SPEC.md` states, `RESOLVED (agent, 2026-11-03, delegated)`, with M3's reason. The options are the builder's three: (a) the §4/S1 address rule becomes "the first `[tag]` of that finding which at least one confirmed finding of every round that found the defect also cites"; (b) an address may hold more than one tag; (c) AC3's run-B figure restated as 43/59 with a recorded departure. The resolution is (a): it meets AC3 as written, the probe shows it moves only `executor-map` and `inflight-count` (both to `[supervise]`) and leaves every row a qualifying tag; (c) fails AC3 as written, so M3 veto 1 discards it; (b) widens the row grammar TOOL-dFairHearing-18 reuses through its hands-off edge.
2. Write (a) into §4 "The known set" and S1, and make §4 "Scoring"'s claim that the scorer reproduces 46 and 45 true under it. Name the two rows it moves.
3. Record the side note: A22's and B13's refs spell `[\harness]`, which `TAG_REF` does not read, so `codex-events` takes `[policies]`; no figure moves. Say so in §4, so the build does not treat it as a defect to fix.
4. Rev bump and one §9 line per change, naming this brief. Leave the status header's state as it is.

### Acceptance
The spec at its next rev: §8 carries the resolved mark, §4 and S1 state rule (a), and AC3's figures (A 46/59 high 6/8, B 45/59 high 8/8) follow from it.

### Gates
None you run: the spec-token checker is the main loop's.

### Non-goals
No change to the clause the unit carries, to replay 2 to 4, or to the two-pass split in the build brief. No other spec, no code.
