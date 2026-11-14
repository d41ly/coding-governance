# Brief — aClearedLedger: unit 14, review round 3's two low findings as one batch

**Serves:** research TOOL-aClearedLedger-14

## The prompt

> follow `memory/guides/BUILD-METHOD.md` for specs, builders and the closing review.

The owner's prompt is recorded whole in `memory/builds/aClearedLedger/prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md`.

## The brief

### Goal
Round 3 of the closing diff review, `memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-11-12-13-diff-review-round3.md`, confirmed two LOW items and no BLOCKER, HIGH or MEDIUM; the build method batches them into one unit. Write the spec of TOOL-aClearedLedger-14, order 14, from the record's items L1 and L2, each with the fix the record states; for L2 the skeptic's class-level fix is the design.

### Items
1. L2: `readTokenAt` of `tools/unattended/gate-guard.js` reads on past `>` or `<` only while the word read so far is made entirely of unquoted characters matching the operator pattern, so a quoted `&`, `>` or digit glued before a `>` ends the word as bash does. Two `run_planted` arms in `tools/unattended/gate-guard.test.sh`, one with a quoted `&` and one with a quoted `>`, each glued before a `>`, each with a `New arm:` line naming its failing case; the floor moves by their count, DERIVED from 217, the value TOOL-aClearedLedger-13 left at 64673441a.
2. L1: TOOL-aClearedLedger-13's spec is CLOSED and frozen, so its table cell is not edited. This unit's spec restates that unit's quoted-read regex in a fenced block, as the correction of record, and says why the frozen cell renders split.
3. The status header carries no `closes`. Tier-2, because it changes the hook's contract. Every figure beside a unit or a counted noun carries PINNED or a sha on its line; no bare path with a line number.
4. Section 5 numbers only criteria a builder's pass can observe with a probe of the changed code. Each suite run, leg run and RED-first observation the main loop owes is stated in the Gates section, on the `New arm:` lines and in prose there, never as a numbered criterion: hygiene check 23 wants a ledger line for every criterion a CLOSED spec numbers, and a builder cannot observe a suite.

### Acceptance
`python tools/check-spec-tokens.py --spec` over the new spec exits 0, and each of the two items maps to a numbered scope item and at least one criterion.

### Gates
The spec-token checker over this one spec.

### Non-goals
Any change to `tools/check-spec-tokens.py` or its suite; any edit to a CLOSED spec; any sibling spec, any commit, any index render, any floor lowered.

### Limitations
The writer commits nothing and regenerates no index. A role agent's pass runs no suite.

### Reuse
`tools/unattended/gate-guard.js` (`readTokenAt`), and the specs of TOOL-aClearedLedger-12 and TOOL-aClearedLedger-13 as the worked form.
