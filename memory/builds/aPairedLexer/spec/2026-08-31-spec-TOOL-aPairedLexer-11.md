# TOOL-aPairedLexer-11 — rule 2 calls the same merge as rule 3

**Status:** SPECCED · rev-3 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-diff-round3.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-diff-round3.md) | diff-review | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round4.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round4.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-12 |

<!-- /gen:spec-records -->

## 1. Goal

`fanoutFindings` calls `const { consts } = intConsts(code)` on the same kind of possibly-fallback view
with **no** cross-check at all. `intConsts` matches anywhere in the text and the LATER binding wins,
so a fabricated `const K = 5` — in a block comment, say — still lowers a real `const K = 500`, and
`boundedK` then blesses a 500-wide chunk, which is one agent per finding.

Round-2 review **D6**. Not a regression: 1.9, 1.10, the tip and both candidate lexer patches all
admit it. It is the exact defect the diff fixed next door in rule 3 and left standing here, which is
why it is HIGH rather than MEDIUM — the impact is D5's, the novelty is not.

## 2. Scope (IN)

- **S1** — hoist `TOOL-aPairedLexer-10`'s corrected merge into ONE helper. **It takes both views as
  PARAMETERS**, because `fanoutFindings` has no `_bl` in scope and a helper written against one
  caller's locals is not hoisted, it is moved. Signature: the trusted view, the fallback view, and
  whether the trusted view is clean.
- **S2** — both `capFindings` and `fanoutFindings` call it. Same code, same rationale, two consumers.
- **S3** — an arm asserting the two rules resolve the SAME const table for a given script, so they
  cannot diverge again.

## 3. Non-goals (OUT)

- Not changing the merge RULE — that is `TOOL-aPairedLexer-10`, and this unit only shares it.
- Not unifying the two SCANNERS (`TOOL-aPairedLexer-5`); this is the const table, not the lexer.

## 4. Design

**Rule 2's trigger is not rules 3 and 5's trigger, and one phrase hides that.** Rule 2 falls back on
`renderCodeView.unterminated`; rules 3 and 5 fall back on `blankLiterals.clean`. So "an
ambiguous-position declined slash" names two different mechanisms depending on which rule reads it,
and the audit measured the sibling specs' spelling exiting `2` here — a green DENY proving nothing
about D6. Only a trigger carrying a BACKTICK reproduces for rule 2.

One helper, two callers. The whole content of this unit is removing a second answer to one question
— which is the class the bug checklist selected for these paths before any of it was written, and the
class that produced two of this file's three prior fail-opens.

S3 is the durable half. An arm pinning the two INSTANCES would go stale the moment a third consumer
appears; an arm asserting the two rules AGREE holds whatever either does next.

## 5. Production-readiness checklist

- security — closes the same fabricated-cap path in the verifier-arity rule.
- perf / scale — no change; the same work, called from one place.
- a11y · i18n — N/A.
- error / empty / loading states — unchanged.
- observability — rule 2's denial gains the unresolvable-form message rule 3 already had.
- risks — more denials in rule 2 on non-clean views, the fail-closed direction, as `-10`.
- testing + left-shift gates — S3 gates the AGREEMENT, not the instances.
- migration / rollback — revert restores rule 2's uncrossed table.
- user docs — dossier gap list refreshed.

## 6. Acceptance criteria

- **AC1** — When the D6 fixture is fed to the hook, it exits `2`. The trigger is an
  ambiguous-position declined slash **HOLDING A BACKTICK** — not the `if (a) /won't/.test(s)`
  spelling `TOOL-aPairedLexer-9` §4 uses. Measured verdicts for THIS fixture: tip `0`, 1.9 `0`,
  1.10 `0`, and `0` under simulated `-6`+`-7`+`-8`. The rest of the fixture is `const K = 500`, a
  block comment whose prose contains `const K = 5`, a
  `chunk(args.findings, Math.ceil(...)) // gov:fixed-verifiers` split, and
  `boundedParallel(groups.map(...), 5)`.
- **AC2** — When only the block comment is deleted, it exits `2` with the message naming the
  unbounded split — the review's control, and proof the prose is what buys the pass.
- **AC3** — When a script is run through both rules, `fanoutFindings` and `capFindings` resolve the
  SAME const table. **The fixture must be one where the two scanners AGREE**, or the criterion
  selects the wrong answer: measured on `tools/workflows/drift-audit-state.js`, this repo's own
  shipped harness, `renderCodeView.unterminated` is `false` while `blankLiterals.clean` is `false`
  — the two views disagree, so rule 2 and rule 3 legitimately read different views and an
  equality assertion over that script would demand they not. Assert equality of the CONST TABLE
  given the same view, and pin the disagreement separately as `-6` AC8 does.
- **AC4** — When `grep -c` finds the merge logic in `agent-cap.js`, there is exactly ONE occurrence.
- **AC5** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm green before this unit is green
  after it, except any `TOOL-aPairedLexer-10` re-baselines by name.

## 7. Gates

Legs read from `tools/gate-legs.json` at emission time. Direct: `bash tools/hooks/agent-cap.test.sh`.

## 8. Open questions

none — the fix is a hoist, and AC3 pins the agreement it exists to create.

## 9. Revision log

- rev-1 · 2026-08-31 · authored on promotion from the round-2 closing review, finding D6.
- rev-2 · 2026-08-31 · folded spec-audit finding 37. AC1 borrowed "an ambiguous-position declined
  slash" from a sibling spec, but rule 2 keys on `renderCodeView` while rules 3 and 5 key on
  `blankLiterals` — two mechanisms behind one phrase — so every verdict AC1 stated was false for the
  fixture the phrase admits. The trigger is now named literally, with its measured verdicts, and §4
  says why it differs from its siblings'.
- rev-3 · 2026-08-31 · folded round-2 audit H1. The hoisted merge was written against `_bl` and
  handed to `fanoutFindings`, which has no `_bl` — a move rather than a hoist. S1 now states the
  signature. AC3's equality assertion also needed a fixture where the two scanners agree, since
  they measurably diverge on this repo's own drift-audit harness.

## 10. Reuse audit

Probes as `TOOL-aPairedLexer-6` §10, same session, same terms. **This unit IS the reuse act**: the
seam is `TOOL-aPairedLexer-10`'s corrected merge, and the whole scope is giving it a second caller
instead of a second copy. The probe reports `capFindings` and `fanoutFindings` at `fan-in 0` in one
file, which is the shape that lets two rules drift apart — and did.
