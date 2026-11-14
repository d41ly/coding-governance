# Brief — aClearedLedger: unit 11, the closing review's medium and low findings as one batch

**Serves:** research TOOL-aClearedLedger-11

## The prompt

> follow `memory/guides/BUILD-METHOD.md` for specs, builders and the closing review.

The owner's prompt is recorded whole in `memory/builds/aClearedLedger/prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md`.

## The brief

### Goal
The closing diff review, `memory/builds/aClearedLedger/reviews/2026-11-13-review-TOOL-aClearedLedger-1-2-3-4-5-6-7-9-10-diff-review-round1.md`, confirmed seven MEDIUM and two LOW items and the build method promotes them, batched, into one unit. Write that unit's spec, TOOL-aClearedLedger-11, order 11, from the record's items M1 to M7, L1 and L2, each with the fix the record states and the skeptic's judgement of it.

### Items
1. M1 to M4: row D6 of `tools/unattended/gate-guard.js` and `check_bar` of `tools/check-spec-tokens.py` answer one command alike. The record's class-level fixes are the design: the script is matched at any word of the simple command; a candidate whose words after the direct-check word are all options is a hit; leading `./` is stripped and a shorter trailing path matches; a word breaks at an unquoted redirection operator; `check_bar` splits on the hook's separator set and removes quotes. Where the spec keeps a gap, the hook's header and the unattended kit's README name it.
2. M5: two arms in `tools/unattended/gate-guard.test.sh` that tell an absent or unparsable manifest from the outer catch. M6: two command-line arms in `tools/check-spec-tokens.test.sh` over a scratch manifest carrying a ceiling. M7: the redirected, piped and backslash spellings in the staged assertion, with the skeptic's caution on the backslash literal. L1: one arm for row D6's backslash and case fold.
3. L2: check 8 of `tools/check-template-size.sh` says `The policy reader refused:`; the record says why the guard on the source was set aside. This file is manifest-watched, so the closing commit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`.
4. Every new or changed arm has a `New arm:` line naming its failing case, and each `FLOOR_ASSERTIONS` moves by the count the arms add, stated as DERIVED. Units 3 and 5 are CLOSED and frozen; this unit states its corrections itself.
5. Tier-2 where it changes a kit's contract. The status header carries no `closes`: the unit closes review findings, not asks. Every figure beside a unit or a counted noun carries PINNED or a sha on its line; no bare path with a line number; a criterion needing a suite is the main loop's and says so.

### Acceptance
`python tools/check-spec-tokens.py --spec` over the new spec exits 0, and each of the nine items maps to a numbered scope item and at least one criterion.

### Gates
The spec-token checker over this one spec.

### Non-goals
Finding H1 of the record, which is the main loop's observation record. Any sibling spec, any commit, any index render, any floor lowered.

### Limitations
The writer commits nothing and regenerates no index. A role agent's pass runs no suite.

### Reuse
`tools/unattended/gate-guard.js` (`readSuiteLegs`, `checkSuiteLeg`, `readTokenAt`), `tools/check-spec-tokens.py` (`check_bar`, `derive_flag_suites`, `SIMPLE_COMMAND_SPLIT`), and the specs of units 3 and 5 as the worked form.
