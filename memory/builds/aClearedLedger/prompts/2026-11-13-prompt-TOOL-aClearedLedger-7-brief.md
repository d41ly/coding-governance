# Brief — aClearedLedger: unit 7's spec, the manifest re-stamp its pass commit owes

**Serves:** research TOOL-aClearedLedger-7

## The prompt

> a moved `tools/gate-legs.json` owes a `last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md` in the same commit.

The owner's prompt is recorded whole in `memory/builds/aClearedLedger/prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md`.

## The brief

### Goal
DIVERGENCE: spec section 3 (Non-goals) puts the `last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md` OUT of this unit and gives it to the main loop "after the pass", but the pre-commit hook refuses the pass commit without it. The commit attempt failed with `MANIFEST check 5 FAILED — staged changes touch watched files: tools/check-template-size.sh, tools/gate-legs.json but the staged manifest's audit block does not update last-audit ... bundle the re-stamp into THIS commit`. The only ways past it are `--no-verify`, which is a bypass I am not authorized to take, or writing a path the spec excludes. Section 3 would have to drop that non-goal, and section 2 plus "Files touched" would have to put the re-stamp of `memory/guides/SESSION-KICKOFF.md` IN the unit's closing commit (re-verify the section B claims the two watched files feed, then stamp `last-audit`), which is how 29c9024c7 (TOOL-aNimbleMend-27) actually landed it; alternatively the spec must name who makes that commit and how. Every path I changed was restored; the tree is clean at 96827eb76 and nothing was committed.

### Items
1. Drop the non-goal. Scope and Files touched put the `last-audit` re-stamp of `memory/guides/SESSION-KICKOFF.md` in the unit's closing commit: the builder re-verifies the section B claims the two watched files feed, stamps `last-audit` under that file's stamp rule, and names the delta in the commit message, as `memory/builds/aClearedLedger/spec/2026-11-13-spec-TOOL-aClearedLedger-10.md` already states for its own commit. One criterion observes it with a probe the builder can run.
2. The header moves to the next rev with a revision-log line naming the builder's divergence. The builder's return also settles the spec's UNVERIFIED note on the recall export: say so where the note stands.
3. `python tools/check-spec-tokens.py --spec` over the spec exits 0. Change nothing else, commit nothing, render no index.

### Acceptance
The spec's closing commit can pass the pre-commit hook's manifest check without a bypass.

### Gates
The spec-token checker over this one spec.

### Non-goals
Any other edit to the spec, any sibling spec, any commit, any index render.

### Limitations
The writer commits nothing and regenerates no index; the main loop commits the revision and dispatches the unit again.

### Reuse
The spec itself, and section S4 of unit 10's spec as the worked wording.
