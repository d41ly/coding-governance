# Brief — aClearedLedger: unit 16, review round 4's medium and low findings as one batch

**Serves:** research TOOL-aClearedLedger-16

## The prompt

> follow `memory/guides/BUILD-METHOD.md` for specs, builders and the closing review.

The owner's prompt is recorded whole in `memory/builds/aClearedLedger/prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md`.

## The brief

### Goal
Round 4 of the closing diff review, `memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-14-diff-review-round4.md`, confirmed one MEDIUM and three LOW items, and the build method batches them into one unit. Write the spec of TOOL-aClearedLedger-16, order 16, from the record's items M1, L1, L2 and L3, each with the fix the record states and the skeptic judged sound.

### Items
1. M1: two `run_planted` deny arms in `tools/unattended/gate-guard.test.sh` for a quoted glued redirection target, `>"x.log"` and `2>"x.log"`, each with a `New arm:` line whose failing case is the drop test's predicate weakened to `q >= 0`.
2. L1: in `readTokenAt`, a word whose quoting is empty (`"">x.log`) ends at an unquoted `>` or `<` as any quoted word does, the record's first form.
3. L2: the unattended kit's README and the hook's header comment give `'>'>x.log` as the quoted-operator example where they now give `'>' x.log`.
4. L3: the `check_bar` docstring of `tools/check-spec-tokens.py` gives both reasons the lint over-reads a quoted operator character, in the record's wording; no code in that file changes, and a probe shows it.
5. This unit builds after TOOL-aClearedLedger-15, which changes `scanDenyHits` and adds two deny arms to the hook's suite: state each floor move as DERIVED from the floor that unit leaves, and write no figure that unit moves.
6. Section 6 numbers only criteria a builder's pass can observe with a probe of the changed code. Each suite run, leg run and RED-first observation the main loop owes is stated in the Gates section, on the `New arm:` lines and in prose there, never as a numbered criterion: hygiene check 23 wants a ledger line for every criterion a CLOSED spec numbers, and a builder cannot observe a suite.
7. The status header carries no `closes`. Tier-2, because it changes the hook's contract. Every figure beside a unit or a counted noun carries PINNED or a sha on its line; no bare path with a line number. TOOL-aClearedLedger-14 is CLOSED and frozen; this unit states its corrections itself.

### Acceptance
`python tools/check-spec-tokens.py --spec` over the new spec exits 0, and each of the four items maps to a numbered scope item and at least one criterion.

### Non-goals
Item H1 of the record, which is TOOL-aClearedLedger-15. Any change to the code of `tools/check-spec-tokens.py` or its suite. Any sibling spec, any commit, any index render, any floor lowered.

### Gates
The spec-token checker over this one spec.

### Limitations
The writer commits nothing and regenerates no index. A role agent's pass runs no suite. Round 4's confirmed count rose over round 3's, so by the build method's exit rule no fifth review round follows: this spec is the last word on its design before the bar, and every red-first observation it names must be one the main loop can stage.

### Reuse
`tools/unattended/gate-guard.js` (`readTokenAt`, `scanDenyHits`, `REDIRECT_RE`), and the spec of TOOL-aClearedLedger-14 as the worked form.
