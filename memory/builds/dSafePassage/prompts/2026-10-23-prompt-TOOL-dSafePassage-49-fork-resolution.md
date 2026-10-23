**Serves:** research TOOL-dSafePassage-49

# Brief — dSafePassage: TOOL-dSafePassage-49's F1 resolved under the mandate

## The prompt

> `unattended.sh --plan dSafePassage --paths` lists TOOL-dSafePassage-49 as FORKED: its §8 F1, "Who writes S4's
> order move, and when?", carries no resolution.

— the driver's plan, read by the run's main loop before the round-6 spec audit

## The brief

### Goal

Mark TOOL-dSafePassage-49's §8 F1 resolved, so the spec reads READY and the round-6 audit reads a settled design.

### Items

1. In `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md` §8, mark F1 in place, in the shape
   `memory/TEMPLATE-SPEC.md` §8 gives and both §8 readers grade:
   `RESOLVED (agent, 2026-10-23, delegated): (a)`. The reason is rung 3 of the execution plan's fork rule
   (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` lines 901-948): the
   mandate delegates the fork, and M3 takes the most feature-rich option that survives the vetoes. (a) is the only
   option AC2 admits. (b) fails AC2, which is veto 1. (c) changes `tools/workflows/unattended-build.js`, outside
   this build's goal, which is veto 2 with no grant naming it. Say in the mark that the run applying (a) is this
   build's build run, before it hands out the roster.
2. The mark is a rung-3 choice, so it carries no `widens:` or `relaxes:` field (README rule 6 asks those only of
   rungs 5 and 6).
3. Bump the spec to rev-2 with a §9 line naming F1's resolution. This is a material change (§8), so the rev moves.

### Acceptance

`bash tools/unattended/unattended.sh --plan dSafePassage --paths` prints TOOL-dSafePassage-49 as READY, not
FORKED. That verb is read-only, so you may run it.

### Gates

None beyond that read. A role agent runs no gate.

### Non-goals

No other section or spec changes, and nothing is committed or staged. The order moves themselves are option (a)'s
work, done by the build run, not here.

### Limitations

This is an unattended run, so nobody will answer a question.

### Reuse

The §8 mark shape in `memory/TEMPLATE-SPEC.md`.
