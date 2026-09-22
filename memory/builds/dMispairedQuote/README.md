---
slug: dMispairedQuote
node: d
opened: 2026-09-01
streams: tooling
roster: TOOL
ids: TOOL-dMispairedQuote-1 TOOL-dMispairedQuote-2 TOOL-dMispairedQuote-3 TOOL-dMispairedQuote-4 TOOL-dMispairedQuote-5 TOOL-dMispairedQuote-6 TOOL-dMispairedQuote-7 TOOL-dMispairedQuote-8
authorized-by: prompt
---

# dMispairedQuote — a quote pairs with the wrong partner, and rule 1's view loses the fan-out between them

## The problem this build exists to solve

`agent-cap.js` blanks quoted spans so prose naming `parallel(` is not read as a call. It pairs a
quote with the next quote of the same kind on the line, so an apostrophe in prose earlier on that
line pairs with the quote opening `agent('a'` and the span blanked between them carries the fan-out.
The guard then admits an unbounded fan-out at exit 0.

The reported instance is a regex literal. The class is wider: a double-quoted string, a block comment
and a template literal each admit the same fan, and four of the file's five rules are defeated. The
`addc6169` repair demands a matching pair; a pair exists, and it is the wrong one. The owner's prose
is the mandate, recorded under [prompts/](prompts/2026-09-01-prompt-TOOL-dMispairedQuote-1.md).

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
- **The fix is judged in BOTH directions.** A change that only ever adds denials is not obviously
  safe: this file's ceiling is fail-closed and a wider one costs refusals an operator cannot act on.
  Every candidate is measured against the shipped suite and the real tracked corpus.
- **This build does not take `TOOL-aLexedStripper-3` or `-4`.** Both are OPEN rows about FALSE
  POSITIVES in rule 1's and rule 3's views. The backlog rows record what this build did and did not
  touch.
- **Both spec-audit loops exited NON-CONVERGENT, and the dispositions are recorded here** because the
  driver has no flag for them. Unit 1's exit at 4 blockers PROMOTED three to unit 3 and folded one.
  Unit 3's exit at 2 FOLDED both, on the review's own reading that neither needed a mechanism this
  build lacks. Unit 2 converged at round 1 and was not re-reviewed.
- **Unit 1 may not land without unit 3.** One behaviour change across two mechanisms: unit 1 alone
  was measured moving three scripts from DENY to ADMIT.
- **Six review runs is more than this warranted.** Rounds 1 and 2 over unit 1 each reproduced a
  fail-open the fix itself introduced and were worth their cost. Unit 3's rounds 2 and 3 returned
  spec prose. Recorded because the next build reading this should stop a round earlier.

## Parked decisions

**LANDED BY HAND after the abort, at the owner's instruction (2026-09-01).** `RUN.md` records
phase ABORTED with halt code `gate-red-out-of-scope`, which was true when it was written: the run
could not merge itself. The owner then read the three options in the parked entry below and chose
the first. The merge is `f0eb3239`, a `--no-ff` merge of `branch/agent-cap-apostrophe-bug-46c953`,
pushed to `origin/main` at `bd62d866`. The full bar was run twice, on the branch tip and again on
merged main, 85 of 86 legs green both times; the push used `--no-verify` because that is the only
mechanism there is, and it skipped a bar that had already been run rather than one that had not.

**MAIN WAS RED UNTIL `TOOL-aClosedDocket-4` LANDED — and it never did.** That unit is WONTDO as of
2026-09-02, superseded by `TOOL-dFoldedVerdict-1`, `-2` and `-3`, which cleared this red instead. The
paragraph below is kept as the cost this build recorded at the time.

**THE ORIGINAL ENTRY**, and that is this build's cost to the fleet: the
`unattended kit gate` leg is `subject = repo` with no guard, and this run's `RUN.md` is now on main,
so every push from this repo meets it. That unit is RATIFIED and is `aClosedDocket`'s next READY
unit; its own section 1 predicted this and its N4 premise is falsified by this record.

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dMispairedQuote-1` | OPEN | one quote-opener rule, shared by every view, so a mispaired apostrophe cannot blank a fan-out |
| 2 | `TOOL-dMispairedQuote-2` | OPEN | the file's stated ceiling and the dossier's residual describe what the view now does |
| 3 | `TOOL-dMispairedQuote-3` | OPEN | every rule is evaluated over both views, so no denial can be lost |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node d · opened 2026-09-01 · streams tooling
ids TOOL-dMispairedQuote-1 TOOL-dMispairedQuote-2 TOOL-dMispairedQuote-3 TOOL-dMispairedQuote-4 TOOL-dMispairedQuote-5 TOOL-dMispairedQuote-6 TOOL-dMispairedQuote-7 TOOL-dMispairedQuote-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dMispairedQuote-1 — one quote-opening decision, shared by every view in `agent-cap.js`](spec/2026-09-01-spec-TOOL-dMispairedQuote-1.md) | 1 | 2 | CLOSED | rev-4 | 2026-09-01 |
| [TOOL-dMispairedQuote-3 — every rule is evaluated over both views, so no denial can be lost](spec/2026-09-01-spec-TOOL-dMispairedQuote-3.md) | 2 | 2 | CLOSED | rev-6 | 2026-09-01 |
| [TOOL-dMispairedQuote-2 — the carriers that describe `agent-cap.js`'s string views describe what they now do](spec/2026-09-01-spec-TOOL-dMispairedQuote-2.md) | 3 | 1 | CLOSED | rev-4 | 2026-09-01 |
<!-- /gen:build-units -->

Records: 10 bound to this build, across 4 record folder(s).

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
