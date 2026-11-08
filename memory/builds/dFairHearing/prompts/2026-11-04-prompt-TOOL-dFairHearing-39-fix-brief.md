# Fix brief — TOOL-dFairHearing-39: the class anchor dGroundRules already moved

**Serves:** research TOOL-dFairHearing-39

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-39.md` so a correct build of it passes on today's tree, before its builder is dispatched. An earlier pass of this run found that dGroundRules' unit 42 (`TOOL-dGroundRules-42`) already anchored the gotcha class this spec's S4 re-anchors to `memory/builds/`, so AC1's half that reads the class's parent anchor as `/spec/` is red today. The resolution the run recorded is option (a): drop S4's `/spec/` anchor and AC1's parent half, and have AC3 derive its count from the tree; option (b) fails M3's first veto because its own AC1 half fails. Verify that finding against today's tree and the dGroundRules records first; if it does not hold, say so and change nothing. Commit nothing; the main loop commits.

### Items
1. Read the class record S4 names, its `## Anchors` (or equivalent) as committed today, and `TOOL-dGroundRules-42`'s spec and commit, and state in §1 or §4 what is already anchored.
2. Record the choice as a §8 fork marked by M3 and resolved `RESOLVED (agent, 2026-11-04, delegated)`, naming the veto that discards (b), in the shape this build's README rule 5 states.
3. Carry it through S4, AC1 and AC3, so each criterion a correct build can pass on today's tree still reds on the defect it names.
4. Re-ground every `path:line` citation and every `New arm:` break in §1 to §7 against the tree after units 25 to 38 (their CLOSED specs and builder returns are in this build's folder); a break against code an earlier unit already fixed cannot fail. Check §6's backticked words against `tools/check-spec-tokens.py`'s `BAR` pattern (:419-424).
5. Rev bump and one §9 line per change, naming this brief. Leave the status header's state as it is.

### Acceptance
Every criterion a correct build can pass on today's tree; every `New arm:` line names a break that reds on today's code; the §8 fork in README rule 5's shape.

### Gates
None you run.

### Non-goals
No other spec, no code.
