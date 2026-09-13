# TOOL-cGradedDebt-2 — the six status-token faults the TOOL.md row was hiding

**Status:** CLOSED · rev-3 · 2026-09-13 · node c · Tier-1 · base 09a22d2b · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-cGradedDebt-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-cGradedDebt-1-acceptance-ledger.md) | journal | TOOL-cGradedDebt-1 |
| [2026-09-13-review-TOOL-cGradedDebt-1-diff-review-round1.md](../reviews/2026-09-13-review-TOOL-cGradedDebt-1-diff-review-round1.md) | diff-review | TOOL-cGradedDebt-1 |

<!-- /gen:spec-records -->

## 1. Goal

`memory/backlog/TOOL.md` carries six rows that check 8 would red, hidden behind its
`curation-debt.txt` listing. Four lead with `WITHDRAWN`, which is not in the closed status
vocabulary, and two carry a second token because they quote a backticked markdown table predicate in
prose. Fix the rows rather than widening the vocabulary.

## 2. Scope (IN)

- **S1** The four rows leading with `WITHDRAWN` are rewritten to `WONTDO`, the vocabulary's existing
  term for an abandoned or superseded unit. Their body prose is untouched, including the sentences
  that say why each was withdrawn. Observed by AC1.
- **S2** The two rows quoting a backticked table predicate are reworded so the quoted form no longer
  matches check 8's token slot, without changing what the sentence says. Observed by AC1.
- **S3** The registry note for `memory/backlog/TOOL.md` in `memory/project/curation-debt.txt` drops
  its now-false sentence that check 8 is hiding one real fault on one named line, and records that
  the faults were six and are fixed. The row itself stays, because it still earns check 6 and its
  remedy is the open owner call. Observed by AC2.

## 3. Non-goals (OUT)

- `WITHDRAWN` is not added to the status vocabulary. It is a synonym for `WONTDO`, the seven tokens
  are enumerated at nine sites across three kits and two docs, and `TOOL-aRuledFrontispiece-7`
  scoped out changing them in writing.
- No change to check 8's `nmatch` to make it skip backticked inline code. The shape occurs on two
  rows in the whole corpus, archives included, and that parser is validated per-row against an
  upstream tree.
- No rotation, split or curation sweep of `memory/backlog/TOOL.md`. That is
  `TOOL-aWeighedCompass-3`, and it is the owner's call.
- No edit to any other row's status, and no edit to a rotated archive.

### Edges

- **consumes-from** `TOOL-cGradedDebt-1` — that unit is what makes check 8 grade these rows at all,
  as waived findings. This unit is a records change and passes with or without it, so the
  consumption is of the OBSERVATION, not of a precondition.

## 4. Design

The four `WITHDRAWN` rows sit at four line numbers in `memory/backlog/TOOL.md`, each leading its row
in the status slot immediately after the id. A fifth occurrence of the word is prose inside a
`CLOSED` row and is not in a token slot, so it is left alone — check 8 counts a token only in the
middot, pipe or leading-dash slot, and that occurrence is in none of them.

The two double-token rows each quote a markdown table cell inside backticks, in the form of a pipe,
a space, a status word and a space. Check 8's matcher sees the pipe as a DELIMITER and whatever
follows the word as a boundary, so the quoted cell reads as a second status token. The reword
therefore has to drop the PIPE, not the spaces: `|WONTDO|` still matches, because the pipe is the
delimiter and the closing pipe is a non-word character. Measured — closing the spaces first left
both rows red. What lands is the cell named rather than drawn, as `` `WONTDO` cell``.

Measured at `09a22d2b` with the waiver lifted: 6 findings over 438 graded rows in this file, and 0
findings over the 61 rows of the other three shards.

### Files touched (estimate)

| Path | Change |
|---|---|
| `memory/backlog/TOOL.md` | six rows |
| `memory/project/curation-debt.txt` | the note for that row |

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs at the landing commit, check
  8 names no row in `memory/backlog/TOOL.md`, and the report line from unit 1 shows that file
  earning checks 6 and 7 and no longer 8.
  Red when: a rewritten row keeps a second token, or the reword of a quoted table cell leaves the
  pipe-space-token shape intact.
  figure: DERIVED — the finding count comes from the same run, not from this spec.
- **AC2** — When `memory/project/curation-debt.txt` is read, its note for this row no longer claims
  that check 8 reds on one named line, and the row itself is still present.
  Red when: the row is drained along with its stale sentence, which would pre-empt
  `TOOL-aWeighedCompass-3`.

## 7. Gates

`memory hygiene` · `drift-audit records`

No new arm: this unit changes records, not a checker.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-12 · initial draft.
- rev-2 · 2026-09-12 · §4 · S2 · the reword for a quoted table cell must drop the PIPE, not the
  spaces inside the backticks. The rev-1 design claimed the spaces, and the measured result was
  both rows still red.
- rev-3 · 2026-09-13 · §8 · added the Open questions section, which a terminal status requires and
  a Tier-1 spec does not otherwise owe. Silence and a resolved fork are the same byte without it.
