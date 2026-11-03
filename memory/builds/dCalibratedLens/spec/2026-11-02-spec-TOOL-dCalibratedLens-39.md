# TOOL-dCalibratedLens-39 — `read_metrics_lines` answers an ordered list of `(name, value, source)` triples with every repeated name kept, held by a plant against a dict-shaped splitter

**Status:** DEFERRED · rev-2 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 9 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-39-deviation-391.md](../build/2026-11-02-build-TOOL-dCalibratedLens-39-deviation-391.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md) | journal | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 |
| [2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md](../reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 27, HIGH, item H6 of the round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`); id 21 (MEDIUM, item M10,
batched in `TOOL-dCalibratedLens-41`) shares its fix. Unit 21 makes repeated Metrics names normal:
one `caps:` line per cap, one `item-budgets:` line per role, one `stall-trend:` and `bound-evidence:`
line per tuple or kept row. Those lines are read back through unit 3's `read_metrics_lines(text)`,
which units 5, 6, 15, 16 and 17 call and whose return shape no spec states. Built as the natural
name-to-pair mapping, it keeps only the last line of a repeated name, so unit 6 keeps one role's
budget and unit 16 one kept row, while unit 21's plant, which splits with its own code, stays green.
This unit states the return shape and holds it with a plant that reads through the shared splitter.
It repairs `TOOL-dCalibratedLens-21`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text. Unit 3's
  id-30 bullet (rev-3, r2 id 27): `read_metrics_lines(text)` returns a list of `(name, value,
  source)` triples, one per line of the record's `## Metrics` section in the order the lines appear,
  a repeated name kept as one triple per line, each line split on its first `: ` and its last ` · `;
  no caller reads it as a mapping. The section is the lines after the `## Metrics` heading up to the
  next line opening `## ` or the end of the text, and a blank line inside it is skipped; unit 3's
  record template puts one after the heading and one before `## Filed` (round-3 id 33, unit 3's r3
  id-33 bullet). Unit 21 S1 (rev-2, id 27) states the same answer for the lines
  its list-form readings write. Observed by AC1.
- **S2** — The plant `metrics-repeat` of `python loop_review.py --fixture` in
  `tools/loop/loop_review.py`. It renders one record through `render_loop_record` with a planted
  Metrics list of `surface: a · src`, `caps: one · bytes · measure.py caps`, `caps: two · bytes ·
  measure.py caps` and `review-yield: 1/2/3 · src`, reads the text back through
  `read_metrics_lines`, and holds when the answer equals those four triples in that order. The plant
  first asserts that the rendered text carries the template's blank line after `## Metrics` and a
  `## Filed` heading after the four lines, so the bounds are exercised on a real record (round-3 id
  33). It prints `metrics-repeat — ok`, and otherwise `metrics-repeat — FAIL` with the triples it read.
  Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- Unit 21's own `metrics-multi` plant: id 21, `TOOL-dCalibratedLens-41`, which makes that plant parse
  through `read_metrics_lines` too.
- A `by_name` helper over the list. Each caller filters the triples by name in one line; a second
  reader would be the duplication unit 3's id-30 bullet closed.
- The values' own grammar after the split: each caller's line parser, unchanged.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-3` — `read_metrics_lines` and `render_loop_record`, the splitter whose answer the plant holds and the writer whose text it reads
- **consumes-from** `TOOL-dCalibratedLens-21` — the list-form `METRICS` answer, the one source of a repeated name; without it no reading writes two lines under one name

## 4. Design

### Evidence

- Unit 3's id-30 bullet at rev-2: `read_metrics_lines(text)` "splits a record's Metrics section on
  the first `: ` and the last ` · `", with no return shape.
- Unit 21 S1 at rev-1: a reading answers a list of `(value, source)` pairs, each its own line.
- Callers named for the splitter: units 5 S7, 15 S6, 16 S6 and 17 S5 (unit 3's id-30 bullet), and
  unit 6's `read_measured_item_budget` once id 10 of this audit routes it there.

### The answer, by example

```
[("surface", "a", "src"), ("caps", "one · bytes", "measure.py caps"),
 ("caps", "two · bytes", "measure.py caps"), ("review-yield", "1/2/3", "src")]
```

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `metrics-repeat` | `--fixture` plant name | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2, the plant

### Alternatives rejected

- **A mapping of name to a list of pairs.** It answers the same lines but loses the order across
  names, which a reader comparing two records line by line needs.
- **Test the shape in each caller's plant.** Five plants would each hold one name; one plant over the
  splitter holds them all.

## 5. Production-readiness checklist

- security — N/A: a pure read of a rendered text.
- perf / scale — one render and one split per plant run.
- error / empty / loading states — a record with no Metrics line answers `[]`; a blank line is
  skipped, the section ends at the next `## ` heading or the end of the text, and any other line with
  no `: ` or no ` · ` is a `ValueError` naming the line, never skipped.
- observability — the plant prints the triples it read on failure.
- risks — a caller written as `dict(read_metrics_lines(...))`: the review of that caller's diff is
  handed this unit's plant as the contract.
- testing — AC1 to AC3 by the pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python loop_review.py --fixture --plant metrics-repeat` runs from the loop kit
  directory, it prints `metrics-repeat — ok`, both `caps` triples read in order.
  Red when: a repeated name keeps one line, or the order changes.
- **AC2** — When the plant runs with `read_metrics_lines` staged as a name-to-pair mapping turned back
  into triples, it prints `metrics-repeat — FAIL` and three triples, the first `caps` line lost.
  Red when: a dict-shaped splitter passes the plant.
- **AC3** — When the plant runs with `read_metrics_lines` staged to read every line after the heading
  without skipping a blank line, it prints `metrics-repeat — FAIL` naming the `ValueError` on the blank
  line, and with the section's end staged out it reads the `## Filed` lines as Metrics and fails.
  Red when: a splitter that raises on a real record, or reads past its section, passes the plant.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/loop_review.py · covers AC1 AC2 AC3 · the `metrics-repeat` plant, staged red by a `read_metrics_lines` built as a name-to-pair mapping · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 27 (HIGH, item H6) of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; units 3 and 21 amended at the disposal
  (their rev-3 and rev-2).
- rev-2 · 2026-11-03 · §5 §7 §10 S1 S2 AC3 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, from `TOOL-dCalibratedLens-48`: the Metrics
  section's bounds and its blank lines, with AC3 staging both (id 33); §10 records this unit's own
  probe phrase (id 21).

## 10. Reuse audit

The seam extended is unit 3's `read_metrics_lines`, the one Metrics splitter of the set, and its
writer `render_loop_record`; the plant reads through both and copies neither. `python
tools/codebase-map/reuse_lookup.py "split a record's Metrics section into name value source
triples"` ranked name stems only (`records` in `tools/memory-tree/gotchas.py`, `extract_records`,
`read_records` in `tools/memory-tree/deviation_join.py` and `tools/runlog/extract.py`); none splits a
Metrics section, and the loop kit is absent at base, so no code seam fits beyond the sibling specs. The recall probe returned TOOL-cMendedVintage-19,
the placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
