# TOOL-aRuledFrontispiece-2 — build order and parallel groups become a header verb and a region

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Make a build's execution order a derived fact instead of a paragraph. Today the order lives in
authored prose — this build's own README argues it across two sections — and nothing compares that
prose to the units it describes. A unit declares its position in its own status header, and the
build README renders the total order and the parallel groups from those declarations.

## 2. Scope (IN)

- **S1** — the status header's pointer tail admits one new verb, `· order <n>`, where `<n>` is one or
  more decimal digits, at least 1, with no leading zero. The verb is PERMITTED and never required,
  which is fork 5's resolution: this unit ships no required-arm and no dated cutoff key.
- **S2** — units sharing an `order` value ARE the build's parallel group at that step. The group is
  the tie itself, not a second verb, so a group cannot contradict the position it sits in.
- **S3** — `gen_build_index.py` reads the verb with a second regex over the same header line `HDR_RE`
  already matched. `HDR_RE` is not widened. `parse_spec` gains one key, `order`, holding an `int` or
  `None`.
- **S4** — a generated region, `<!-- gen:build-order -->` and `<!-- /gen:build-order -->`, renders one
  row per unit as `| Step | Unit |`, sorted by step and then by the id's sequence component. A unit
  carrying no verb renders last, at step `—`, so the region accounts for every unit the index region
  lists.
- **S5** — the region is opt-in by presence. A README carrying neither marker renders exactly as it
  does at `base 96141aed`. A README carrying one marker of the pair keeps every refusal `apply_region`
  makes today.
- **S6** — a header carrying `order` with a value outside S1's shape is a named refusal naming the
  spec path and the offending value. A silent skip would make the region under-report an order the
  author believes they declared.
- **S7** — `memory/TEMPLATE-SPEC.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md` gain the verb
  in their status-header section, as one byte-paired edit. That section states today that the tail
  holds pointers only, which the verb contradicts until it is amended.

## 3. Non-goals (OUT)

- Requiring the verb, or dating a cutoff for it. Fork 5 put the requirement in a follow-up commit.
- A second `group` verb. §4's Alternatives rejected records why one verb carries both facts.
- Rendering a unit that has no spec. The authored plan inside the `roster:units` pair is where a
  pending unit lives, and unit 1 forbids the generator writing there.
- Ordering the generated regions relative to one another. Each pair is spliced where the author put
  it; pinning a canonical sequence is the leg in unit 6.
- Enforcing the verb's shape on the merge bar. This unit ships the refusal and its arms; unit 6 makes
  it binding.
- Rewriting M6's parallelism clause. Unit 9 owns that, and this unit only supplies the data it needs.
- Changing `LIVE.md` or the ledger shards (fork 8), and retrofitting any existing README (unit 10).

## 4. Design

### Data model

A unit's position is authored once, in the unit's own file, and read from there:

| Fact | Where it lives | Who writes it |
|---|---|---|
| the unit's step | `· order <n>` in the spec status header | the spec's author |
| the parallel group at a step | every unit carrying the same `<n>` | nobody — it is the tie |
| the row key | the id's sequence component, e.g. `1` in `TOOL-aRuledFrontispiece-1` | the id |
| the rendered order | `<!-- gen:build-order -->` in the build README | `gen_build_index.py --write` |

The row key is the sequence component because the build README requires the order to key on something
that exists before a spec does, and the authored plan's `#` column is exactly that handle. The two
line up only where a build mints ids in plan order. That is not universal: measured at
`base 96141aed`, `memory/builds/aFoldedQuarry/spec/units/2026-08-08-spec-aFoldedQuarry-2-u6-indexed-join.md`
is the build's unit 6 at sequence 2, and its `-3-u1-flatten` sibling is unit 1 at sequence 3. This
build mints in plan order; making that binding belongs to unit 9.

`HDR_RE` at `tools/memory-tree/gen_build_index.py:74-78` ends at `base (?P<base>[0-9a-f]{8,})` with no
`$` and no trailing group, so it matches a PREFIX of the header line. Verified against source. Every
tracked spec therefore parses unchanged today, and a header carrying the new verb parses unchanged
too — the verb costs nothing at the parse site and is read separately.

Check 12's header predicate at `tools/memory-tree/check-memory-hygiene.sh:559` is unanchored in the
same way, ending at the eighth spelled-out `[0-9a-f]`. Verified against source. Its `streams`
extraction matches `streams [A-Za-z0-9]+(\+[A-Za-z0-9]+)*`, which stops at the first byte outside that
class, so a tail reading `· streams tooling · order 2` still yields `tooling`. The consequence is
worth stating because it is easy to assume otherwise: **check 12 needs no edit for the verb to be
legal**. What does need editing is `memory/TEMPLATE-SPEC.md`, which tells an author the tail holds
pointers only.

### Inventory

| Site | Change |
|---|---|
| `HDR_RE` | none — verified unanchored, so it already admits the tail |
| new `ORDER_RE` | one regex over the matched header line, extracting the digits after `· order ` |
| `parse_spec` | one added key, `order`; the refusal in S6 fires here, where the value is read |
| new `MARK_ORDER_OPEN` / `MARK_ORDER_CLOSE` | the second generated pair's two constants |
| new `render_order_region` | the table, mirroring `render_region`'s shape |
| new `apply_optional_region` | presence probe, then delegation to `apply_region` |
| `plan` | one added splice per build |

`apply_optional_region` counts the pair's opening and closing markers with the same column-0 equality
`apply_region` uses. Both counts zero means the pair is absent and the text is returned untouched;
anything else delegates, so a half-present pair still meets the unequal-counts refusal and an inverted
pair still meets the ordering refusal. It does NOT make the existing pair optional: `gen:build-index`
keeps its own direct call and its no-marker-pair refusal, which is the branch that stops a README
leaving the index silently.

Unit 4 writes this same module. It adds a renderer and one more `apply_optional_region` call and it
extends `collect`; it does not touch `parse_spec`, `ORDER_RE` or `render_order_region`. The two units
overlap at exactly two sites — the module's constant block and the per-build body of `plan` — and
`apply_optional_region` is introduced here so unit 4 adds no second presence probe.

### Migration

None for the corpus. No tracked README carries a `gen:build-order` pair at `base 96141aed`, so every
one of the 38 takes S5's absent branch and renders byte-identically. No tracked spec carries the verb
either, so every unit renders at step `—` until an author declares one. Unit 10 owns the retrofit and
verifies both claims over the whole corpus rather than trusting this paragraph.

### Files touched (estimate)

`tools/memory-tree/gen_build_index.py` · its `--selftest` arms · `memory/TEMPLATE-SPEC.md` and
`tools/memory-tree/SPEC-TEMPLATE.template.md` as one byte-paired edit.

### Alternatives rejected

A second `group <label>` verb beside `order` was rejected. Two verbs create a contradiction class the
tie does not have — two units at the same step with different labels, or one label spanning two steps
— and each shape needs its own refusal branch. Neither buys a fact the tie fails to carry, and the
rendered region is identical either way. The build README's unit-2 label reads "status-header verbs
and their region" in the plural; this unit ships one verb and records the reduction here rather than
leaving the second one for a reviewer to find unused.

Widening `HDR_RE` with an optional trailing group was rejected. That regex decides what a valid header
IS for the 113 specs that parse at `base 96141aed`, and a widened pattern that fails to match returns
`None` for the whole header rather than for the verb, which would silently drop a unit from the index
region as well.

Deriving the order from the id sequence alone, with no verb, was rejected on measured evidence: the
`aFoldedQuarry` files named under Data model mint sequence 2 for unit 6, so the sequence is a mint
order and not a build order.

Reading the order out of the authored `roster:units` plan block was rejected. The module's docstring
pins three sources and names reading its own output as the defect it exists to remove; the plan is not
an output, but adding a fourth source would make the region's population depend on a table shape no
gate validates until unit 6.

## 5. Production-readiness checklist

- security — N/A. The verb is read from tracked files the renderer already opens; no new trust
  boundary.
- perf / scale — one regex per spec header already in memory, and one extra splice per README.
- a11y — N/A. No user-facing surface.
- i18n — N/A. The verb and the markers are ASCII literals; the `·` separator is already in the header.
- error / empty / loading states — a build where no unit carries the verb renders every row at step
  `—`; a build with no units renders the region with no table. Both are arms.
- observability — the S6 refusal names the spec path and the value; the region's header line reports
  how many units carry a verb and how many do not.
- risks — the tie-is-the-group rule means an author who mistypes a step silently joins another group
  rather than failing. The rendered region is the mitigation: a wrong tie is visible as two units on
  one row, which prose never made visible at all.
- testing + left-shift gates — arms in `gen_build_index.py --selftest`, one per S1 through S6; the
  binding leg is unit 6.
- migration / rollback — revert is a single-file revert plus the paired doc edit; no corpus bytes
  change in this unit.
- user docs — the verb lands in `memory/TEMPLATE-SPEC.md` and its kit template together.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --check` runs at this unit's tip, it
  reports clean at the same artifact count it reports at `base 96141aed`.
- **AC2** — When a spec header carries `· order 3` and its README carries the pair, `--write` renders
  that unit at step `3` inside `<!-- gen:build-order -->`.
- **AC3** — When two specs in one build both carry `· order 3`, `--write` renders both at step `3` and
  emits no additional row, proved by a `--selftest` fixture.
- **AC4** — When a spec carries no `order` verb, `--check` stays clean and that unit renders at step
  `—` after every row carrying a step.
- **AC5** — When a header carries `· order 0x2`, `--check` fails naming the spec path and the value
  `0x2`.
- **AC6** — When a README carries no `<!-- gen:build-order -->` marker, `--write` leaves it
  byte-identical to its render at `base 96141aed`, proved by a fixture asserting byte equality.
- **AC7** — When a README carries a `<!-- gen:build-order -->` opening marker and no closing marker,
  `--check` fails with the wording `apply_region` already uses for an unequal marker count.
- **AC8** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs after the doc edit, it
  passes, so `memory/TEMPLATE-SPEC.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md` moved
  together.
- **AC9** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, it passes and its arm
  count is strictly greater than at `base 96141aed`.

## 7. Gates

`python tools/memory-tree/gen_build_index.py --selftest` · `bash tools/memory-tree/check-memory-hygiene.sh`,
whose check 12 grades every status header this build writes · `bash tools/memory-tree/kit-dogfood-parity.test.sh`
for the paired doc edit · `bash tools/memory-tree/marker-contract.test.sh`, because a second generated
pair enters the contract that test drives · `bash tools/memory-tree/check-verdict-epoch.sh`, which unit
10 discharges for the whole build.

## 8. Open questions

none — fork 5 resolved the rollout to permitted-now and required-later, and fork 1 resolved what the
authored plan may hold. The one design choice left open by those forks, how many verbs carry the two
facts, is decided in §4's Alternatives rejected rather than parked here.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `status header verb pointer
tail order parallel group marker region apply_region opt-in presence sequence key derived render`.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| splice into a named marker pair | `apply_region` at `gen_build_index.py:493` | REUSE the parameterised form unit 1 ships; add only the presence probe |
| render a table from unit records | `render_region` at `gen_build_index.py:358` | REUSE THE SHAPE — same row grammar and same relative-link form |
| sort units by numeric sequence | `_roster_sort_key` at `gen_build_index.py:254` | REUSE unchanged — it already splits an id and coerces the sequence to `int` |
| read a field out of a status header | `parse_spec` at `gen_build_index.py:200` | EXTEND — one added key, read from the line `HDR_RE` already matched |

The `tools/codebase-map/reuse_lookup.py` probe for "parse a verb out of a spec status header and
render a build order table" returned `render_region`, `render_live` and `render_shards` in
`gen_build_index.py` as the only marker-region renderers in the corpus, and returned no seam that reads
a named field out of a status header — `parse_spec` is the sole reader. The claims that `HDR_RE` and
check 12's header predicate are both unanchored at the end, and that `_roster_sort_key` coerces the
sequence numerically, were each verified against source at writing time.
