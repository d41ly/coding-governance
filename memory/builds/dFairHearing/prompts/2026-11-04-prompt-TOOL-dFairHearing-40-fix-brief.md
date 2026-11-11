# Fix brief — TOOL-dFairHearing-40: re-grounded on the built units, and S30 on a unit 37 that changes no code

**Serves:** research TOOL-dFairHearing-40

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-40.md` so a correct build of it passes on today's tree, before its builder is dispatched. The spec was written at rev-4 against the plans of units 25, 30, 32, 35, 36, 37, 38 and 39; all of them are now CLOSED, and several built differently from their plans. Commit nothing; the main loop commits.

### Items
1. S30 says "after unit 37 S15 changes `check_ungated`'s sentence end". Unit 37 closed at rev-6, and its S15 changes no code: unit 32 (fb755fa80) had already built that closer. Restate S30 and its criterion on the function as it stands today, so the re-derivation and comparison still run and still red on the defect they name.
2. Every other item that consumes unit 37 (the spec's consumes-from row names S10, S15, S17, S20, S23, S31, S33 and S34) is read against unit 37's rev-6 spec and its two builder returns. Rev-6 restated AC1, moved the AC5 and AC14 arm breaks, and corrected S4, S5 and S15. An item that corrects a unit 37 criterion which no longer reads that way is restated or dropped, with a one-line reason.
3. Every item that consumes units 25, 30, 35, 38 or 39 is read against their CLOSED specs, verdict records and builder returns in this build's folder. For example: unit 25's replay was a MISS, unit 30's verdict lives in its verdict record and manifest, unit 35's decision was selected 26/59 over ungated 25/59, and unit 39 added no anchor to the class record. The kept attempt clones are `$TEMP/f1s1` to `$TEMP/f4u1` and `$TEMP/f2s2`, with `f2s1` void.
4. Re-ground every `path:line` citation and every `New arm:` break against today's tree. A break against code that an earlier unit already fixed cannot fail, so name one that reds on today's code. Check every backticked word of the acceptance section against `tools/check-spec-tokens.py`'s `BAR` pattern (lines 419 to 424). A clone-only path is spelled with a `$TEMP/<clone>/` prefix.
5. Where an item's fork has more than one answer a correct build could take, record it in the open-questions section in the shape this build's README rule 5 states, resolved `RESOLVED (agent, 2026-11-04, delegated)`, naming the veto that discards each other option.
6. Bump the rev and add one change-log line per change, each naming this brief. Leave the status header's state as it is.

### Acceptance
Every criterion is one a correct build can pass on today's tree, and every `New arm:` line names a break that reds on today's code.

### Gates
None you run.

### Non-goals
No other spec, and no code.
