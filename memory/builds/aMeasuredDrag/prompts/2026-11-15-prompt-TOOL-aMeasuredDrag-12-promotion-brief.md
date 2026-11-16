# Brief — aMeasuredDrag: the closing review's minors, promoted into one repair unit

**Serves:** research TOOL-aMeasuredDrag-12

## The prompt

> Build quick wins

The closing diff review of this build, round 1 (`memory/builds/aMeasuredDrag/reviews/2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md`), exited CONVERGED and CLEAN WITH FIXES, with 0 blockers, 0 highs and 7 confirmed minor findings forming 6 items. doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it (owner ruling, DIFF 2026-10-04) promotes every minor into one batched unit.

## The brief

### Goal
`TOOL-aMeasuredDrag-12` closes the six items of the round-1 closing review, each fix being the one the review's skeptic judged sound or class-level, with no verdict, refusal or printed line moved for a correct input.

### Items
1. Item 2 (finding 1): only an ABSOLUTE launcher enters `GATE_RESOLVED_PY`. Fix it in `tools/run-gates/run-gates.sh`'s export and in the shared resolver block `tools/lib/resolve-python.sh#resolve_python` (re-synced to every inline copy the TOOL-aMeasuredDrag-11 S2 grep finds). A relative or bare-name launcher is never exported, so every leg re-probes as before.
2. Item 1 (findings 2 and 6): arm 1m in `tools/run-gates/run-gates.test.sh` tells a memo hit from a re-probe, using the skeptic's counting-wrapper fix from the review record, and goes red when the export no leg can match.
3. Item 3 (finding 3): `FLOOR_ASSERTIONS` in `tools/run-gates/run-gates.test.sh` rises by arm 1m's assertions (and item 1's), with a dated ledger line.
4. Item 4 (finding 4): an arm in the instructions-edit selftest pins both sides of `check_tree`'s `tags` switch: the write path runs the tag checks, the `check` verb does not.
5. Item 5 (finding 5): an arm in `.githooks/pre-commit.test.sh` goes red when the rewritten template-size trigger of TOOL-aMeasuredDrag-10 breaks.
6. Item 6 (finding 7): unit 11's AC5 red case (the export ahead of the digest) gets a lasting gate, or the spec §7 claim is narrowed to what arm 1m discharges, whichever the review record recommends.

### Acceptance
Per item, the observation the review record's fix names, and for each new arm a `New arm:` line whose RED-first observation is the main loop's at the close.

### Gates
The pass legs after the unit commit; the bar once, at the close.

### Non-goals
- Any change beyond the six items, and any other unit's spec.
- ANY SELF-TEST SUITE OR BAR INSIDE THE PASS, a sliced suite included.
