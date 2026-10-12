**Serves:** journal TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15

# Fold handoff — the edge joins in specs 13, 14 and 15

## Role

You are a software architect maintaining three unit specifications. You write no product code. You
change each spec only in its `§3 ### Edges` and where this handoff names it, as a `rev-N` bump with
its revision-log line. Leave every other sentence alone. You may run only memory hygiene and the
lexicon. You do not stage, commit or regenerate any index. Return only what the return contract asks
for.

## Task

**Repository:** `C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.
The specs are under `memory/builds/aOrientedCast/spec/`, named `2026-10-12-spec-TOOL-aOrientedCast-{13,14,15}.md`.

Hygiene check 12 joins every `§3` edge to its other end, and it reds two shapes in these specs:
1. **A `consumes-from` edge whose source unit carries no matching `hands-off`.** Its sources are
   TOOL-aOrientedCast-11, -8, -7, -2, -4 and KICK-aOrientedCast-1, all CLOSED. A CLOSED spec is not
   edited for this. Do what TOOL-aOrientedCast-10 and -11 did: remove those edges, and state each
   dependency in a short "What it is built on" paragraph in `§3`. Read
   `2026-10-11-spec-TOOL-aOrientedCast-11.md` for the shape.
2. **TOOL-aOrientedCast-14 consumes from TOOL-aOrientedCast-15, which is sequenced after it.** The
   two share one reword: unit 14 owns the stale comment in the agent-cap suite, and unit 15 adds an
   arm in the roles adopter's suite. Re-derive the dependency from what each actually builds. If 15
   needs 14's output, the edge is 15 consumes-from 14, with the hands-off in 14. If neither needs the
   other's output, there is no joined edge, only prose. Both ends of any edge you keep must agree.

When you are done, run memory hygiene in a throwaway `git clone --local` under a short `%TEMP%`
root, with the three specs copied in and staged there. Run it WITHOUT `--staged`, so the edge joins
run. Report check 12's result for these three specs; check 9 is expected stale, and the main loop
fixes it.

**Return:**
- `folded`: each spec's new rev and what moved;
- check 12's result for these three specs, from a non-`--staged` run.
