# Brief — aClearedLedger: unit 12, review round 2's high finding

**Serves:** research TOOL-aClearedLedger-12

## The prompt

> follow `memory/guides/BUILD-METHOD.md` for specs, builders and the closing review.

The owner's prompt is recorded whole in `memory/builds/aClearedLedger/prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md`.

## The brief

### Goal
Round 2 of the closing diff review, `memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-11-diff-review-round2.md`, confirmed one HIGH item, H1: the word break TOOL-aClearedLedger-11 added to `readTokenAt` of `tools/unattended/gate-guard.js` also fires on the second character of a two-character redirection operator, so row D6 allows an over-bound suite it denied before when output is appended with a spaced operator. Write the spec of TOOL-aClearedLedger-12, order 12, Tier-2, that fixes it as the record states and the skeptics judged sound.

### Items
1. The guard in `readTokenAt` does not break while the word read so far is itself a redirection operator, in the record's form.
2. Deny arms in `tools/unattended/gate-guard.test.sh` over the planted manifest for the four appended spellings the record lists, each with a `New arm:` line naming its failing case, and the floor raised by their count, stated as DERIVED.
3. TOOL-aClearedLedger-11 is CLOSED and frozen; this unit states its correction itself. The status header carries no `closes`.
4. Every figure beside a unit or a counted noun carries PINNED or a sha on its line; no bare path with a line number.
5. Section 5 numbers only criteria a builder's pass can observe with a probe of the changed code. Each suite run, leg run and RED-first observation the main loop owes is stated in the Gates section, on the `New arm:` lines and in prose there, never as a numbered criterion: hygiene check 23 wants a ledger line for every criterion a CLOSED spec numbers, and a builder cannot observe a suite.

### Acceptance
`python tools/check-spec-tokens.py --spec` over the new spec exits 0, and the item maps to a numbered scope item and at least one criterion.

### Non-goals
The record's medium and low items, which are TOOL-aClearedLedger-13. Any change to `tools/check-spec-tokens.py` or its suite. Any sibling spec, any commit, any index render, any floor lowered.

### Gates
The spec-token checker over this one spec.

### Limitations
The writer commits nothing and regenerates no index. A role agent's pass runs no suite. Hygiene check 23 wants a ledger line for every criterion a CLOSED Tier-2 spec numbers, and a builder cannot observe a suite: so section 5 numbers only criteria a builder's pass can observe with a probe, and each suite run, leg run and RED-first observation the main loop owes is stated in the Gates section, on the `New arm:` lines and in prose there, never as a numbered criterion.

### Reuse
`tools/unattended/gate-guard.js` (`readTokenAt`, `checkSuiteLeg`), `tools/check-spec-tokens.py` (`check_bar`, `SIMPLE_COMMAND_SPLIT`), and the spec of TOOL-aClearedLedger-11 as the worked form, its spelling table included.
