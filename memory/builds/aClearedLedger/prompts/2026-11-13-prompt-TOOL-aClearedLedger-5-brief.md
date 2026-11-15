# Brief — aClearedLedger: unit 5's spec, one clause the hygiene gate asks for

**Serves:** research TOOL-aClearedLedger-5

## The prompt

> This is a new build with its own slug and build folder, not more units of aNimbleMend; follow `memory/guides/BUILD-METHOD.md` for specs, builders and the closing review.

The owner's prompt is recorded whole in `memory/builds/aClearedLedger/prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md`.

## The brief

### Goal
The spec commit was refused by hygiene check 25 on `memory/builds/aClearedLedger/spec/2026-11-13-spec-TOOL-aClearedLedger-5.md`: its item S3 retires named things, three members of `PARITY_EXEMPT` and the branch that counted a leg neither graded nor exempt, and carries no `**Readers:**` clause. Add the clause to S3 in the grammar `memory/TEMPLATE-SPEC.md` states, `by name:` and `by value:` on their own lines, each reader verified in source, as a rev bump with its revision-log line. Change nothing else in the spec.

### Items
1. S3 of the spec gains its `**Readers:**` clause; the header moves to rev-2 with a revision-log line naming check 25.
2. `bash tools/memory-tree/check-memory-hygiene.sh --only 25` names this spec no longer, and `python tools/check-spec-tokens.py --spec` over it exits 0.

### Acceptance
Hygiene check 25 prints no line naming the spec.

### Gates
The hygiene gate's check 25 and the spec-token checker over this one spec.

### Non-goals
Any other edit to the spec, any sibling spec, any commit, any index render.

### Limitations
The writer commits nothing and regenerates no index; the main loop commits the nine specs once.

### Reuse
The spec itself, and the Readers clauses of `memory/builds/aNimbleMend/spec/` as worked examples.
