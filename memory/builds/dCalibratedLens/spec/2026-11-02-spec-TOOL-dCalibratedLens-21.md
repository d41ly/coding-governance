# TOOL-dCalibratedLens-21 — one carrier for a multi-line reading: the record's Metrics lines, one per entry, never a `fields`-form field

**Status:** OPEN · rev-3 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 8 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-21-deviation-211.md](../build/2026-11-02-build-TOOL-dCalibratedLens-21-deviation-211.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 |
| [2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 2, HIGH, item H3 of the round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`), whose fix item M25
(id 45, MEDIUM, batched in `TOOL-dCalibratedLens-30`) shares. Unit 3 defines the `loop-review`
record's fields as single `**Key:**` lines and its writer refuses a value carrying a line break
(spec-3 §4 "The record"), while units 4, 6 and 16 add `fields`-form fields whose values are one line
per cap, role or tuple (`caps`, `item-budgets`, `stall-trend`, `bound-evidence`), and every other
reading of the set rides the record's `## Metrics` lines. Under unit 3 S2 the refused write exits the
walk 1, so no period ever writes its record. This unit fixes ONE carrier, the Metrics lines, with a
reading allowed to answer several lines under its name, and proves it on unit 4's caps step, the
first multi-line reading to land. It repairs `TOOL-dCalibratedLens-4`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text (each at rev-2,
  its §4 "Amendments (round-1 spec audit)", id 2): unit 3 S5 and §4 "The record" admit a `METRICS`
  reader answering a LIST of `(value, source)` pairs, each written as its own Metrics line
  `<name>: <value> · <source>` in list order, and a reading never adds a `fields`-form field; unit 4
  S7/S8 make `caps` such a `METRICS` entry, one line per cap; unit 6 S4 and S6 make `item-budgets` one,
  one line per role, and `read_measured_item_budget` reads the role's `item-budgets:` Metrics line;
  unit 16 S6 and S7 make `stall-trend` and `bound-evidence` two, one line per tuple and per kept row.
  None of units 4, 6 and 16 edits `tools/memory-tree/record-kinds.toml`, and each one's criterion that
  read "the field holds the lines" reads the Metrics lines. Read back, those lines are unit 3's
  `read_metrics_lines` answer: a list of `(name, value, source)` triples in line order, a repeated
  name kept once per line, never a mapping (round-2 id 27, `TOOL-dCalibratedLens-39`). A list reading
  that answers no pair writes one line `<name>: searched-none · <source>`, the spelling unit 3's
  id-11 amendment gives a source holding nothing (round-2 id 40). Observed by AC2.
- **S2** — The proof, a `--fixture` plant `metrics-multi` in `tools/loop/loop_review.py`: it runs the
  walk's `gather` and `record` over unit 4's planted caps (the `caps-raise` population of spec-4 AC2)
  and one planted `METRICS` entry answering three pairs, one of them a value holding a `·`; the written
  record carries one `caps:` line per cap and three lines of the planted entry, in list order; the
  writer refuses nothing; and `read_metrics_lines` over the written record returns every
  `(name, value, source)` triple as planted, in order (round-2 id 21). A second planted entry answers
  an empty list and the record carries its one `searched-none` line (round-2 id 40). Observed by AC2.
- **S3** — The registry stays four fields: `tomllib` over `tools/memory-tree/record-kinds.toml` gives the
  `loop-review` row the schema `{ form = "fields", fields = ["Key", "Base", "Window", "Ledger"] }`
  after this unit's pass. Observed by AC3.
- **S4** — A reader answering one value carrying a line break is never handed to the writer: the
  walk's isolation boundary writes `<name>: unread · refused value` for it (round-2 id 31,
  `TOOL-dCalibratedLens-40`), so the list form is the only way a reading writes several lines and a
  multi-line answer cannot exit the walk. For a list answer the refusal is per entry: the entry
  carrying the break is written `<name>: unread · refused value` in its place and the other entries as
  answered (round-3 id 32, unit 3's r3 id-32 bullet, held by `TOOL-dCalibratedLens-40`'s case).
  Observed by AC4.

## 3. Non-goals (OUT)

- A section form or a `schema` form for multi-line fields, the other carrier the review names. It
  adds a second carrier beside the Metrics lines every other reading of the set already uses.
- Units 6 and 16's own readings: each lands its lines under its amended spec; this unit observes unit
  4's, the only one built before it.
- Unit 14's `scenario-proposals`, which takes the same carrier under id 47 (`TOOL-dCalibratedLens-30`).
- The splitter's answer shape and its own plant: `TOOL-dCalibratedLens-39` (round-2 id 27).
- AC1 observes only the disposal's text in sibling specs and is green at writing; it is a
  precondition, not an observation of this unit's build (the round-2 audit's ids 4, 18 and 29).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-4` — the caps step `derive_cap_readings` as a `METRICS` entry, whose lines the plant writes; without it there is no multi-line reading built at this order
- **consumes-from** `TOOL-dCalibratedLens-3` — `measure_loop_metrics`, `render_loop_record`, `read_metrics_lines` and the isolation boundary, the writer the plant writes through and the splitter it reads back with
- **hands-off** `TOOL-dCalibratedLens-39` — the list-form `METRICS` answer, whose repeated names that unit's `metrics-repeat` plant reads through the splitter (round-2 id 27)

## 4. Design

### Evidence

- The audited carriers: spec-3 §4 "The record" (the four `**Key:**` lines are the `fields` form, "The
  writer refuses a value carrying a line break"); spec-4 S8, spec-6 S4, spec-16 S6 and S7 (one line per
  cap, role, tuple and kept build), each listing `tools/memory-tree/record-kinds.toml` in Files touched.
- Units 9, 11, 15 and 17 already write their readings as Metrics lines (spec-15 §4 "The metrics": "One
  Metrics line per entry, the shape TOOL-dCalibratedLens-3 §4 'The record' gives").

### The lines

```
## Metrics

caps: AGENTS.md · bytes · current 20480 (default) · rows 30 · p90 27000 · raise · cost 4433344B/212 · measure.py caps
caps: skills/session-kickoff/SKILL.md · bytes · current 18432 (default) · rows 8 · p90 - · refused: 8 of 30 rows · cost - · measure.py caps
```

A value may carry ` · `; the split takes the name before the first `: ` and the source after the LAST
` · `, so a source never carries ` · `, which each reader's source string already obeys.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `metrics-multi` | `--fixture` plant name | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2 and S4, the plant

### Alternatives rejected

- **A `## <Name>` section per multi-line reading.** The test: count the readers of the record the set
  specs, units 5 S7, 6 S6, 15 S6, 16 S6 and 17 S5; each would need a second parser beside the Metrics
  splitter for four readings, against one carrier read one way.
- **A separator inside one field line.** It keeps the registry field and makes every reader parse a
  second grammar inside a value.

## 5. Production-readiness checklist

- security — the writer's refusal of a line break stays; the list form adds lines only through the
  writer, each held to the same refusal.
- perf / scale — one Metrics line per cap, role, tuple or kept row, at most a few hundred per period.
- error / empty / loading states — an empty list writes one `<name>: searched-none · <source>` line
  (round-2 id 40); a refusing or multi-line reader is the `unread` line of the isolation boundary.
- observability — every reading is a named line in the period's record.
- risks — a source string carrying ` · ` would split wrongly; S2's plant holds the rule.
- testing — the plant of S2 and the staged break of S4.
- migration — N/A: no record exists at base.
- user docs — N/A: `help/loop-review.md` describes Metrics lines already (TOOL-dCalibratedLens-3 S11).

## 6. Acceptance criteria

- **AC1** — When `grep -c 'record-kinds.toml'` runs over the specs of units 4, 6 and 16
  (`memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-4.md`, `-6.md`, `-16.md`),
  each prints 0, and `grep -n 'answering a LIST' memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-3.md`
  prints the amendment.
  Red when: a sibling still adds a `fields`-form field for a reading.
  A precondition read at writing: it greps the disposal's text.
- **AC2** — When `python loop_review.py --fixture --plant metrics-multi` runs, the record holds one
  `caps:` line per planted cap, three planted lines in order and one `searched-none` line for the
  empty entry, and `read_metrics_lines` returns each triple as planted.
  Red when: the writer refuses the multi-line reading, a line is lost or reordered, an empty list
  writes nothing, or a splitter cutting at the first ` · ` passes.
- **AC3** — When `python -c "import tomllib;r=[k for k in tomllib.load(open('record-kinds.toml','rb'))['record-kind'] if k['name']=='loop-review'][0];print(r['schema']['fields'])"`
  runs from the memory-tree kit directory after this unit's pass, it prints `['Key', 'Base', 'Window', 'Ledger']`.
  Red when: a reading added a field to the row.
- **AC4** — When the plant `metrics-multi` runs a reader answering one value carrying a line break,
  the walk exits 0 and the record carries `<entry>: unread · refused value` for it.
  Red when: a raw multi-line value reaches the record, or the writer's refusal exits the walk.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/loop_review.py · covers AC2 AC4 · the `metrics-multi` plant, staged red by a writer that joins a list answer into one line and by a `read_metrics_lines` that cuts at the first ` · ` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 2 (HIGH, item H3) of the round-1 spec audit;
  units 3, 4, 6 and 16 amended at the disposal (their rev-2).
- rev-2 · 2026-11-02 · §3 §5 §7 §10 S1 S2 S4 AC1 AC2 AC4 · amended at the disposal of the round-2 spec
  audit `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`: the splitter's answer shape (id 27,
  `TOOL-dCalibratedLens-39`); a multi-line answer read as `unread · refused value` (id 31,
  `TOOL-dCalibratedLens-40`); the plant parsing through `read_metrics_lines` (id 21), the empty list's
  `searched-none` line (id 40) and AC1 stated a precondition (ids 4, 18, 29), all
  `TOOL-dCalibratedLens-41`; §3 gains the hands-off to unit 39.
- rev-3 · 2026-11-03 · S4 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, from `TOOL-dCalibratedLens-48`: the
  refusal's scope for a list answer is the entry (id 32).

## 10. Reuse audit

The seam extended is unit 3's `METRICS` table and its Metrics-line writer, the carrier units 9, 11,
15 and 17 already use; this unit widens a reader's answer from one pair to a list and adds no
carrier. The plant writes through `render_loop_record` and reads back through `read_metrics_lines`,
both unit 3's, and copies neither (round-2 id 21). `python tools/codebase-map/reuse_lookup.py "isolate each reader so one failure becomes an
unread line, never the walk's exit"`, run once for the set, ranked name stems only; the loop kit is
absent at base, so no existing code seam fits beyond the sibling specs. The recall probe returned
TOOL-cMendedVintage-19, the placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
