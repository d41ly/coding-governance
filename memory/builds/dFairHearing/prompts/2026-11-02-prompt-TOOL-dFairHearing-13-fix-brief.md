# Fix brief — TOOL-dFairHearing-13: criteria a correct build can pass on today's tree

**Serves:** research TOOL-dFairHearing-13

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-13.md` so a correct build of it can pass every criterion on the tree it is built on, and so every line it cites still points where it says. The builder's return is `memory/builds/dFairHearing/build/2026-11-02-build-TOOL-dFairHearing-13-1-builder-return.md`. Commit nothing; the main loop commits.

### Items
1. AC2 diffs `tools/workflows/tier2-review.js` against base `3708a705`, and other builds have since changed non-comment lines of that file (its version line, the `boundedParallel` cap, `addressOwed`), so AC2 reds before this unit is built. Re-pin each such comparison to the tree the build pass starts from, spelled as the pass's parent commit (`HEAD~1` of the unit's commit), never a moving ref. AC1's pinned lens keys and briefs may stay at `3708a705` only where they are still byte-identical at the current HEAD; check.
2. AC4 asks for a `slots` line naming every marked literal, while §4's format line gives only a count. Make the two agree, in one place.
3. Re-ground every `path:line` citation in §1, §2, §4, §5 and §7 against the current tree; earlier builds moved lines. Fix the line numbers, not the design.
4. The whole-tree "no lens-slot literal" red breaks `check-verifier-fanout.test.sh`'s mkfix arms AC2 and AC3, as the hands-off note to TOOL-dFairHearing-23 already expects. Confirm the note stands and that §7 names those arms as owed at the close, after unit 23.
5. Leave the status header's state as it is; bump the rev and add one §9 line per item, naming this brief.

### Acceptance
The spec at the next rev: no criterion reads a base-pinned comparison that today's tree already reds; every cited line resolves; §9 lines for each item. `python tools/check-spec-tokens.py` over the spec, run bounded, names no new finding.

### Gates
`python tools/check-spec-tokens.py memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-13.md` only. No gate leg, suite or bar.

### Non-goals
No design change: scope, data model and the slot count stay. No other spec, no code, no write outside that one spec file.
