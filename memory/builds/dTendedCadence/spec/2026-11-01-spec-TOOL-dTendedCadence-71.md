# TOOL-dTendedCadence-71 — the siblings that defined the old landing grammar corrected in place to the carried four-line landing, before they build

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 22 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-71-deviation-711.md](../build/2026-11-01-build-TOOL-dTendedCadence-71-deviation-711.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 28 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, item H7. Units 49, 50 and 52 replace the landing grammar but correct none of the siblings that
define the old one: spec-39 S2, §4 "The intake", its Inventory row and AC2 still name the review's own
three-line filer and a re-write "from the text alone" (:35-40, :63-71, :81, :119); spec-1 S6 still
carries the readings as JSON for re-writing (:96-99); spec-48 S24 still re-derives with
`drift_report.py --readings` (:107-110) and AC20's second half lands a re-derived set (:312-314).
Spec-39 AC2 and spec-52 AC1 cannot both pass, and units 39 (order 18) and 48 (order 20) build first.
This unit makes the text each builder reads the grammar that ships.

## 2. Scope (IN)

- **S1** — Spec-39. S2 reads: after unit 13 S6 writes the record, `security_review.py` lands it
  through `write_record_landing` as TOOL-dTendedCadence-52 S1 states, with filer `security-review`,
  and files no text of its own. §4 "The intake" points at unit 49 §4's four lines. The Inventory row
  for the review's own filer function is not kept. AC2 reads "whose text is unit 49 §4's four lines
  opening `land maintenance-record security-<H12>`", AC3's landing runs `maintenance.py land`, and the
  §5 observability line prints `landing <commit12>`. Corrected in place, a rev bump with a §9 line
  naming review id 28. Observed by AC1.
- **S2** — Spec-1. S6's landing sentence reads: the walk passes the written record's path to
  `write_record_landing` (TOOL-dTendedCadence-49 S4), whose intake names the payload commit and its
  digest, and the records-only patch build lands it with `maintenance.py land`
  (TOOL-dTendedCadence-50); no readings JSON. AC7's "whose text names the key" reads "whose first
  line is `land maintenance-record <key>`". Corrected in place, as S1. Observed by AC2.
- **S3** — Spec-48. S24 keeps only its stdin refusals, `maintenance.py write` exiting 2 on stdin that
  is empty, not JSON, or missing `read` or `readings`; its digest and re-derivation sentence points at
  TOOL-dTendedCadence-49 and -50. AC20 keeps its first half; its second half, the 70 KiB set landing
  with every `over-pin:` line, reads as landed through TOOL-dTendedCadence-51's round trip. Corrected
  in place, as S1. Observed by AC3.
- **S4** — The timing. Each correction is written in this unit's build pass, and each corrected spec
  carries the §3 consumes-from edge this disposal writes toward this unit, so a builder of unit 39 at
  order 18 or unit 48 at order 20 reads that the grammar it would otherwise build is corrected here.
  NOT OBSERVED by a criterion of its own: the edges are this disposal's, and the hygiene gate's edge
  join grades them.

## 3. Non-goals (OUT)

- The landing seam, verb and round trip: TOOL-dTendedCadence-49, -50 and -51.
- Spec-52's own text: unchanged; its S1 already says the review's own filer is not built.

### Edges

- **consumes-from** `TOOL-dTendedCadence-52` — S1's security landing through the one seam, the grammar spec-39 is corrected to
- **hands-off** `TOOL-dTendedCadence-39` — S2, §4 "The intake", the Inventory row, AC2, AC3 and the observability line, corrected in place to the four-line landing
- **hands-off** `TOOL-dTendedCadence-1` — S6's landing sentence and AC7, corrected in place to `write_record_landing`
- **hands-off** `TOOL-dTendedCadence-48` — S24's digest and re-derivation and AC20's second half, corrected in place to units 49 to 51

## 4. Design

Each correction moves the cited prose and nothing else: no scope item is added to a corrected spec
and none changes status. The pattern is TOOL-dTendedCadence-59's (its §1): a correction no file
carries is observed by nothing, so the text is changed where each builder reads it.

### Files touched (estimate)

- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-39.md`: S1
- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md`: S2
- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-48.md`: S3

## 5. Acceptance criteria

- **AC1** — When `grep -c "write_review_landing\|from the text alone\|three lines"
  2026-11-01-spec-TOOL-dTendedCadence-39.md` runs in the spec folder, it prints 0, and `grep -c
  "write_record_landing"` over the same file prints at least 2.
  Red when: spec-39 still specifies the review's own filer or a re-write from the text.
- **AC2** — When `grep -n "readings as JSON" 2026-11-01-spec-TOOL-dTendedCadence-1.md` runs in the spec
  folder, it prints nothing, and `grep -n "land maintenance-record <key>"` over the same file matches
  in AC7.
  Red when: unit 1's landing text still carries the readings.
- **AC3** — When `awk '/^- \*\*S24\*\*/,/Observed by AC20/' 2026-11-01-spec-TOOL-dTendedCadence-48.md`
  runs in the spec folder, piped to `grep -c "drift_report.py --readings"`, it prints 0; and the
  same range piped to `grep -c "TOOL-dTendedCadence-49"` prints at least 1.
  Red when: unit 48 still re-derives the readings at the landing.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 28 (HIGH, item H7) of the round-1 spec
  audit of units 49 to 59.

## 9. Reuse audit

No code is written; the seam is the corrected siblings' own text, the in-place correction
TOOL-dTendedCadence-59 established. `python tools/codebase-map/reuse_lookup.py "carry a written record
to another node under a git ref and land it"` named no second landing grammar in the tree, unit 52
§10's reading, so no existing seam fits.

Recall terms used: `python tools/memory-recall/query.py "how does a records-only patch build land a
maintenance record the walk wrote" --terms "records-only patch intake landing four lines
write_record_landing maintenance.py land re-derive superseded grammar"`
