# Brief — aClearedLedger: unit 13, review round 2's medium and low findings as one batch

**Serves:** research TOOL-aClearedLedger-13

## The prompt

> follow `memory/guides/BUILD-METHOD.md` for specs, builders and the closing review.

The owner's prompt is recorded whole in `memory/builds/aClearedLedger/prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md`.

## The brief

### Goal
Round 2 of the closing diff review, `memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-11-diff-review-round2.md`, confirmed four MEDIUM and two LOW items, and the build method batches them into one unit. Write the spec of TOOL-aClearedLedger-13, order 13, from the record's items M1 to M4, L1 and L2, each with the fix the record states and the skeptic's judgement of it; where the record carries a skeptic's corrected or class-level fix, that one is the design.

### Items
1. M1 and M2: `check_bar` of `tools/check-spec-tokens.py` reads a half-glued redirection and a quoted value holding a space as the hook does.
2. M3: an arm in `tools/unattended/gate-guard.test.sh` that feeds the head-less candidate branch and can fail. M4: an arm for the lint's `&` lookarounds, and the parity comment above them made true.
3. L1: the three texts that count the lint's over-reads agree with the code. L2: check 8's reworded clause of `tools/check-template-size.sh` is printed by an arm, in the skeptic's corrected form. A commit that moves a manifest-watched file re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`.
4. This unit builds after TOOL-aClearedLedger-12, which changes `readTokenAt` and adds four deny arms to the hook's suite: state each floor move as DERIVED from the floor that unit leaves, and write no figure that unit moves.
5. Every new or changed arm has a `New arm:` line naming its failing case. TOOL-aClearedLedger-11 is CLOSED and frozen; this unit states its corrections itself. The status header carries no `closes`. Tier-2 where it changes a kit's contract. Every figure beside a unit or a counted noun carries PINNED or a sha on its line; no bare path with a line number.
6. Section 5 numbers only criteria a builder's pass can observe with a probe of the changed code. Each suite run, leg run and RED-first observation the main loop owes is stated in the Gates section, on the `New arm:` lines and in prose there, never as a numbered criterion: hygiene check 23 wants a ledger line for every criterion a CLOSED spec numbers, and a builder cannot observe a suite.

### Acceptance
`python tools/check-spec-tokens.py --spec` over the new spec exits 0, and each of the six items maps to a numbered scope item and at least one criterion.

### Non-goals
Item H1 of the record, which is TOOL-aClearedLedger-12. Any sibling spec, any commit, any index render, any floor lowered.

### Gates
The spec-token checker over this one spec.

### Limitations
The writer commits nothing and regenerates no index. A role agent's pass runs no suite. Hygiene check 23 wants a ledger line for every criterion a CLOSED Tier-2 spec numbers, and a builder cannot observe a suite: so section 5 numbers only criteria a builder's pass can observe with a probe, and each suite run, leg run and RED-first observation the main loop owes is stated in the Gates section, on the `New arm:` lines and in prose there, never as a numbered criterion.

### Reuse
`tools/unattended/gate-guard.js` (`readTokenAt`, `checkSuiteLeg`), `tools/check-spec-tokens.py` (`check_bar`, `SIMPLE_COMMAND_SPLIT`), and the spec of TOOL-aClearedLedger-11 as the worked form, its spelling table included.
