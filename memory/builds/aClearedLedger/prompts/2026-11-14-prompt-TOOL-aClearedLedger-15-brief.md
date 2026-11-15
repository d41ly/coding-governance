# Brief — aClearedLedger: unit 15, review round 4's high finding

**Serves:** research TOOL-aClearedLedger-15

## The prompt

> follow `memory/guides/BUILD-METHOD.md` for specs, builders and the closing review.

The owner's prompt is recorded whole in `memory/builds/aClearedLedger/prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md`.

## The brief

### Goal
Round 4 of the closing diff review, `memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-14-diff-review-round4.md`, confirmed one HIGH item, H1: the drop test TOOL-aClearedLedger-14 added to `scanDenyHits` of `tools/unattended/gate-guard.js` measures the operator with `REDIRECT_RE` over the whole word, quoted characters included, so a quoted operator character at the start of a glued redirection target (`>'>x.log'`, `2>'>x.log'`) keeps a real redirection as an argument word and row D6 allows the suite the base denied. Write the spec of TOOL-aClearedLedger-15, order 15, that fixes it as the record states and the skeptic judged sound.

### Items
1. When a word holds quoting, `REDIRECT_RE` runs on the unquoted prefix before the quote alone, and the word is a redirection only if that prefix matches; the bare-operator step stays for an unquoted word that is the operator whole.
2. Two `run_planted` deny arms in `tools/unattended/gate-guard.test.sh`, `$M_FLAG >'>x.log'` and `$M_FLAG 2>'>x.log'`, each with a `New arm:` line whose failing case is the hook at 998b627aa; the floor moves by their count, DERIVED from 219, the value TOOL-aClearedLedger-14 left at 998b627aa.
3. Section 6 numbers only criteria a builder's pass can observe with a probe of the changed code. Each suite run, leg run and RED-first observation the main loop owes is stated in the Gates section, on the `New arm:` lines and in prose there, never as a numbered criterion: hygiene check 23 wants a ledger line for every criterion a CLOSED spec numbers, and a builder cannot observe a suite.
4. The status header carries no `closes`. Tier-2, because it changes the hook's contract. Every figure beside a unit or a counted noun carries PINNED or a sha on its line; no bare path with a line number. TOOL-aClearedLedger-14 is CLOSED and frozen; this unit states its corrections itself.

### Acceptance
`python tools/check-spec-tokens.py --spec` over the new spec exits 0, and the item maps to a numbered scope item and at least one criterion.

### Non-goals
The record's medium and low items, which are TOOL-aClearedLedger-16. Any change to `tools/check-spec-tokens.py`, the unattended kit's README or the hook's header comment. Any sibling spec, any commit, any index render, any floor lowered.

### Gates
The spec-token checker over this one spec.

### Limitations
The writer commits nothing and regenerates no index. A role agent's pass runs no suite. Round 4's confirmed count rose over round 3's, so by the build method's exit rule no fifth review round follows: this spec is the last word on its design before the bar, and every red-first observation it names must be one the main loop can stage.

### Reuse
`tools/unattended/gate-guard.js` (`readTokenAt`, `scanDenyHits`, `REDIRECT_RE`), and the spec of TOOL-aClearedLedger-14 as the worked form.
