---
slug: dMispairedQuote
node: d
opened: 2026-09-01
streams: tooling
roster: TOOL
ids: TOOL-dMispairedQuote-1 TOOL-dMispairedQuote-2 TOOL-dMispairedQuote-3
authorized-by: prompt
---

# dMispairedQuote — a quote pairs with the wrong partner, and rule 1's view loses the fan-out between them

## The problem this build exists to solve

`agent-cap.js` rule 1 bans the raw fan-out primitives. It scans a view of each line with string
literals blanked, so prose mentioning `parallel(` is not read as a call. The blanker pairs a quote
with the next quote of the same kind on the line. When an apostrophe sits in prose earlier on that
line, the pair it forms is the prose apostrophe and the quote opening `agent('a'` — and everything
between them, `parallel(` included, is blanked out of the view. The guard then admits an unbounded
fan-out at exit 0. The owner's prose is the mandate and is recorded under
[prompts/](prompts/2026-09-01-prompt-TOOL-dMispairedQuote-1.md).

The reported instance is a regex literal, `/won't/`. Reproduced at HEAD, and the class is wider than
the report: a double-quoted string, a block comment and a template literal carrying the same
apostrophe each admit the same fan. The `addc6169` repair this file carries demands a matching pair
before it blanks; a pair exists, and it is the wrong one.

## Expected improvements

- A raw `parallel(` or `pipeline(` sharing its line with an apostrophe is DENIED, whichever
  construct the apostrophe sits in.
- One quote-opening decision serves every view in the file, so the next repair cannot fix one rule
  and leave its sibling reading a different string model.
- The file's own stated ceiling describes what it now does, so the next reader is not told the class
  is closed by the sentence that closed the last one.

## Detriments if this is not built

- The only mechanical control against an agent burst is defeated by an apostrophe, which is the
  cheapest possible entry and needs no intent.
- Two review rounds have now prescribed a repair for this line and both stopped at "a pair exists".
  A third will too, because the precondition they read is the one that is wrong.
- Every adopter that copy-installs the kit carries the same hole.

## Build-level rules

- **Classification (M2)**: two units, MISSING at open, authored this run. Unit 1 is the code view;
  unit 2 is the prose that describes it. One mechanism each.
- **The regression arms belong to unit 1, not to a unit of their own.** They go into an existing
  gate, `tools/hooks/agent-cap.test.sh`, and are §7's observed failing case for unit 1's mechanism
  rather than a second mechanism. Staged RED against the tip before they land.
- **The fix is judged in BOTH directions.** A change to this file that only ever adds denials is not
  obviously safe: rule 1's documented ceiling is fail-closed and a wider one costs false refusals an
  operator cannot act on. Every candidate is measured against the shipped suite and against
  `tools/workflows/*.js`, the real corpus this hook reads.
- **This build does not take `TOOL-aLexedStripper-3` or `-4`.** Both are OPEN rows about rule 1's and
  rule 3's views, and both are about FALSE POSITIVES. Unit 1 may close `-3` as a consequence of
  sharing one view; it may not widen into rule 3, whose `blankLiterals` mode leak is a separate
  mechanism with its own arms.
- **`.claude/hooks/agent-cap.js` is a verbatim deploy copy.** Every byte of unit 1 lands in both, and
  the suite's own parity arm is the check.
- **The spec-audit loop over unit 1 exited NON-CONVERGENT, and unit 3 is the promotion that exit
  calls for.** Round 1 confirmed 2 blockers; round 2, over the fold, confirmed 4. The count did not
  shrink, so per M4 the loop STOPPED and every standing blocker was disposed rather than re-reviewed.
  Three were one property — correcting what counts as a string literal un-hides delimiters as well as
  fan-outs, and rules 2 and 3 walk across lines — and closing it needs a mechanism unit 1 does not
  have. The fourth was folded. Unit 2 converged at round 1 and is not re-reviewed.
- **Unit 1 may not land without unit 3.** The two are one behaviour change split across two
  mechanisms, and unit 1 alone was measured to move three scripts from DENY to ADMIT.
- **`--disposition` could not be recorded.** The rendered unattended Skill documents
  `--review … --disposition fold|promote` and `unattended 1.14` refuses the flag. The disposition is
  recorded here, in each spec's revision log, and as a parked decision in `RUN.md`.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dMispairedQuote-1` | OPEN | one quote-opener rule, shared by every view, so a mispaired apostrophe cannot blank a fan-out |
| 2 | `TOOL-dMispairedQuote-2` | OPEN | the file's stated ceiling and the dossier's residual describe what the view now does |
| 3 | `TOOL-dMispairedQuote-3` | OPEN | every rule is evaluated over both views, so no denial can be lost |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 3 unit(s) · node d · opened 2026-09-01 · streams tooling
ids TOOL-dMispairedQuote-1 TOOL-dMispairedQuote-2 TOOL-dMispairedQuote-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dMispairedQuote-1 — one quote-opening decision, shared by every view in `agent-cap.js`](spec/2026-09-01-spec-TOOL-dMispairedQuote-1.md) | 1 | 2 | OPEN | rev-3 | 2026-09-01 |
| [TOOL-dMispairedQuote-3 — every rule is evaluated over both views, so no denial can be lost](spec/2026-09-01-spec-TOOL-dMispairedQuote-3.md) | 2 | 2 | OPEN | rev-4 | 2026-09-01 |
| [TOOL-dMispairedQuote-2 — the carriers that describe `agent-cap.js`'s string views describe what they now do](spec/2026-09-01-spec-TOOL-dMispairedQuote-2.md) | 3 | 1 | OPEN | rev-3 | 2026-09-01 |
<!-- /gen:build-units -->

Records: 6 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dMispairedQuote-1` | no |
| 2 | `TOOL-dMispairedQuote-3` | no |
| 3 | `TOOL-dMispairedQuote-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
