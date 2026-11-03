# TOOL-dCalibratedLens-35 — every record the `three-homes` plant writes is graded by a registry row, and the keep joins the plant when unit 5 lands its row

**Status:** DEFERRED · rev-2 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 4 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-35-deviation-351.md](../build/2026-11-02-build-TOOL-dCalibratedLens-35-deviation-351.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md) | journal | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 |
| [2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md](../reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1, HIGH, item H2 of the round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`). Unit 19's `three-homes` plant
writes a keep record and AC3 expects the check to name the keep when its `Words` line is cut. The
`keep` row lands with unit 5 at order 11, and unit 19 builds at order 3 with no edge to unit 5, so at
unit 19's order no row grades the keep, the check never names it, and AC3 cannot pass on a correct
build. The class is a plant record no row grades, which a field check passes by finding nothing.
This unit makes the plant assert that every record it writes is graded by a row, takes the keep out
of the plant until its row exists, and hands the keep's case to unit 5. It repairs
`TOOL-dCalibratedLens-19`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text: unit 19
  (rev-2, id 1) writes one snapshot and one record and no keep, and its criteria name no keep; unit 5
  (rev-3, id 1) adds its keep to the `three-homes` plant in the pass that lands the `keep` row, so the
  case below grades it from that order on. Observed by AC1 and AC3.
- **S2** — The case `graded-by-a-row` of the `three-homes` plant in `tools/loop/loop_review.py`. For
  each record the plant writes it reads the record's written kind and calls
  `derive_record_kind(path, written_kind, rows)` of the shipped `record_kinds.py`
  (TOOL-dTotalRecall-42 S5, in the form TOOL-dTotalRecall-53 S21 gives it) over the scratch
  registry's rows, and holds when the answer is a row whose `name` is that kind; the kind's read and
  the check of the function's signature are `TOOL-dCalibratedLens-42`'s (round-3 id 1). It prints
  `graded-by-a-row — ok · <n> records · <path>, …`, naming each record it graded, and otherwise one
  `graded-by-a-row — FAIL · <path> · graded by no row` line per record. A plant that wrote no record
  prints `graded-by-a-row — FAIL · 0 records` (round-3 id 5). A `record_kinds.py` with no
  `derive_record_kind` prints `graded-by-a-row — unread · derive_record_kind absent` and fails the
  plant, never passes it. Observed by AC1, AC2 and AC4.

## 3. Non-goals (OUT)

- A scratch `keep` row written by the plant, the review's second option. It would be a second copy of
  unit 5's row that can drift from it, and it grades a record against a row the build has not landed.
- The keep record's own field check: unit 5 AC9, unchanged.
- The disjoint homes and the bare-folder red twin: `TOOL-dCalibratedLens-33` and
  `TOOL-dCalibratedLens-32`.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-19` — the `three-homes` plant and the records it writes, which the case grades; without them there is no record to look up
- **hands-off** `TOOL-dCalibratedLens-5` — the `graded-by-a-row` case, which grades the keep unit 5 adds to the plant with its `keep` row
- **hands-off** `TOOL-dCalibratedLens-42` — the written-kind read and the signature check that run ahead of the `graded-by-a-row` case (round-3 id 1)
- **consumes-from** external — TOOL-dTotalRecall-42 S5 and TOOL-dTotalRecall-53 S21 (`derive_record_kind` and its `written_kind` form), DEFERRED at base; a build-run precondition, as unit 20's external edge states

## 4. Design

### Evidence

- Unit 19 §4 "The keep" at rev-1: the plant writes the keep itself "because `loop_review.py keep`
  is unit 5's and lands later (order 11)"; its §3 Edges name units 2 and 3 only.
- Unit 5 S8 and §4 "The registry row" (its id-1 and id-37 amendments): the `keep` row, home
  `memory/loop-review/*-keep-*.md`, lands at order 11.
- TOOL-dTotalRecall-42 S5 (`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-42.md:53-58`):
  `derive_record_kind` returns the row whose `name` is the record's canonical Serves kind when that
  row's home matches the path, and `None` otherwise; `check_record_kinds` grades only against it.
- TOOL-dTotalRecall-53 S21 (`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-53.md:94-96`):
  the signature is `derive_record_kind(path, written_kind, rows)`, the caller passing the kind it
  read, and no Serves line is parsed inside; unit 20 §3 consumes the same form (round-3 id 1).
- `memory/gotchas/fixture-passes-by-finding-nothing.md`, the class: a check over an empty graded set
  is green.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `graded-by-a-row` | case of the `three-homes` plant | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2

### Alternatives rejected

- **Move unit 19 after unit 5.** The review's first option. Unit 19 then builds at order 12, eight
  steps after the homes it narrows land, and units 20 and 22 to 27 at order 3 or 4 meet the
  overlapping homes meanwhile.
- **Count the check's graded records from its output.** TOOL-dTotalRecall-42 states the check prints
  the unarmed kinds and the mismatch count only, so a per-record grading line is not an output it
  promises.

## 5. Production-readiness checklist

- security — reads only; one import of the shipped checker.
- perf / scale — one lookup per planted record.
- error / empty / loading states — a plant that wrote no record fails the case, since "every record
  graded" over none is the vacuous pass this unit closes.
- observability — each ungraded record is named.
- risks — a record kind renamed in its row and not in its template: the case reds naming the record.
- testing — AC1, AC2 and AC4 by the pass; AC3 at unit 5's pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python loop_review.py --fixture --plant three-homes` runs from the loop kit
  directory, it prints `graded-by-a-row — ok · 2 records` naming the snapshot and the record, and the
  plant writes no keep before unit 5's row exists.
  Red when: a planted record is graded by no row, or the plant writes zero records.
  fixture: `record_kinds.py` is a build-run precondition, absent at `8bec4cef`.
- **AC2** — When the plant runs with a keep record carrying `**Serves:** keep TOOL-dCalibratedLens-5`
  added before any `keep` row exists, the case prints `graded-by-a-row — FAIL` naming the keep's path.
  Red when: an ungraded record passes the case.
- **AC3** — When the same plant runs after unit 5's pass, it prints `graded-by-a-row — ok · 3 records`
  naming the keep's path among them.
  Red when: unit 5 lands its row and the keep is not graded, or the case's record list misses it.
  permission: observed at unit 5's pass, which owns the keep's case.
- **AC4** — When the plant runs with its record writes staged out, so it writes no record, the case
  prints `graded-by-a-row — FAIL · 0 records` and the plant exits 1.
  Red when: an empty graded set passes the case (round-3 id 5).

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/loop_review.py · covers AC1 AC2 AC4 · the `graded-by-a-row` case, staged red by a planted keep written before the `keep` row exists and by a plant that writes no record · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 1 (HIGH, item H2) of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; units 19 and 5 amended at the disposal
  (their rev-2 and rev-3).
- rev-2 · 2026-11-03 · §3 §4 §5 §7 §10 S2 AC1 AC3 AC4 · amended at the disposal of the round-3 spec
  audit `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`: S2 calls `derive_record_kind` in
  TOOL-dTotalRecall-53 S21's form, with the kind's read and the signature check handed to
  `TOOL-dCalibratedLens-42` (id 1); from `TOOL-dCalibratedLens-48`, the pass line counts and names
  its records, AC1 and AC3 read the count and AC4 stages the zero-record red (id 5), and §10 records
  this unit's own probe phrase (id 21); §3 gains the hands-off to unit 42.

## 10. Reuse audit

The seam extended is unit 19's `three-homes` plant, and the grading answer is TOOL-dTotalRecall-42
S5's own `derive_record_kind`, called rather than re-derived. `python
tools/codebase-map/reuse_lookup.py "grade each planted record against the registry row its Serves
kind names"` ranked name stems only (`rows` and `row` in the hygiene and merge-rows suites,
`records` in `tools/memory-tree/gotchas.py`, `extract_row`); none grades a record against a row,
and `record_kinds.py` is absent at base, so no code seam fits beyond the plant and the ancestor's
spec. The recall probe returned
TOOL-cMendedVintage-19, the placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
