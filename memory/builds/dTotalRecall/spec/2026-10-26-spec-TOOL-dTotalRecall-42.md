# TOOL-dTotalRecall-42 — the shape-run home is its id-rule's glob, a kind with no record yet is declared `unarmed`, and a record is graded only by the row its Serves kind names

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 15 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-43 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-43 |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-36 TOOL-dTotalRecall-39 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 51 at HIGH**, its item **H7**, alone in that item. `TOOL-dTotalRecall-11` §4
"The row" sets the shape-run kind's `home` to `memory/builds/<slug>/build/`, the whole build folder, on
a `fields` row with fifteen required fields, and the unit lands with no record. Read as a glob, the home
holds every build record, so `TOOL-dTotalRecall-1` S4 grades deviation, log and research records
against the shape-run fields and reds them. Read literally, it matches no file, and unit 1 §5 and
`TOOL-dTotalRecall-18`'s column rule red the empty home of a `fields` kind. Either way
`record_kinds.py --check` reds or misgrades at unit 11's landing. This unit narrows the home to the
id-rule's glob, gives the registry one declared way for a kind with no record yet to read `unarmed`,
refuses a home that names a bare directory, and grades a record against a `fields` row only when its
Serves kind is that row's. It repairs `TOOL-dTotalRecall-11`.

## 2. Scope (IN)

- **S1** — The shape-run row's `home` in `tools/memory-tree/record-kinds.toml` is
  `memory/builds/*/build/*-shape-run-*.md`, the glob of its `id-rule`
  `<date>-build-<unit id>-shape-run-<n>.md`, the shape `TOOL-dTotalRecall-25` gives stream-plan.
  Observed by AC1.
- **S2** — The `unarmed` key. A `fields` row may carry `unarmed = "<reason naming the writer that
  will arm it>"`. `check_record_kinds` in `tools/memory-tree/record_kinds.py` then prints
  `<kind>: unarmed — <reason>` and passes that row while its home matches no tracked file, in place of
  unit 1's empty-home red and unit 18's "matches at least one tracked file" rule; and it reds the row,
  naming the key, once its home matches a file, so the declaration cannot outlive its population. The
  shape-run row carries `unarmed = "no writer calls gov_record.py new shape-run yet"`. Observed by
  AC2.
- **S3** — One mechanism for the empty population. The stream-plan row carries
  `unarmed = "no record yet; its writer is dIndexedDesign's planner"`, and `check_stream_plan`'s own
  unarmed line (`TOOL-dTotalRecall-25` S5) is printed from that key, so the line's text has one home.
  Observed by AC3.
- **S4** — A bare-directory home is refused. `check_record_kinds` reds a tracked `home` that ends in
  `/` or that names a tracked directory rather than a file glob, naming the row. Observed by AC4.
- **S5** — The kind decides, the home admits. `derive_record_kind(path, text, rows)` in
  `tools/memory-tree/record_kinds.py` returns the row whose `name` equals
  `canonical_kind(<the record's Serves kind>)` (`TOOL-dTotalRecall-18` S7) when that row's home also
  matches the path, and `None` otherwise. `check_record_kinds` grades a record's fields only against
  the row `derive_record_kind` returns, so a record under two homes is graded once, by its own kind, and a
  deviation record under `build/` is never graded as a shape-run. Observed by AC5.

## 3. Non-goals (OUT)

- The shape-run kind's parser, door handler and check: `TOOL-dTotalRecall-11`'s.
- The shape-run row's `layer`, `lifecycle`, `readers` and `purpose` cells: the round-1 audit's id 4, a
  MEDIUM, disposed in `TOOL-dTotalRecall-43`.
- The `record` extractor of `TOOL-dTotalRecall-9`, built at order 18: `TOOL-dTotalRecall-43` re-points
  it to S5's `derive_record_kind` for the audit's id 12.

### Edges

- **consumes-from** `TOOL-dTotalRecall-11` — the `shape-run` row of `record-kinds.toml`, whose home S1
  narrows and which S2's key arms
- **consumes-from** `TOOL-dTotalRecall-1` — `check_record_kinds` and its empty-home rule, which S2, S4
  and S5 extend
- **consumes-from** `TOOL-dTotalRecall-18` — the `home` column's grammar and `canonical_kind`, which S2
  relaxes for a declared `unarmed` row and S5 calls
- **consumes-from** `TOOL-dTotalRecall-25` — `check_stream_plan`'s unarmed line, which S3 prints from the
  row's key
- **hands-off** `TOOL-dTotalRecall-43` — `derive_record_kind`, which that unit's item for the audit's id 12
  makes the `record` extractor call
- **hands-off** `TOOL-dTotalRecall-53` — `unarmed` and `derive_record_kind`, which that unit makes legal on a fence row and feeds a classified kind (the round-1 audit of units 36 to 43, ids 7, 8, 17, 27 and 39)

## 4. Design

### The row, after this unit

```toml
[[record-kind]]
name = "shape-run"
home = "memory/builds/*/build/*-shape-run-*.md"
id-rule = "<date>-build-<unit id>-shape-run-<n>.md"
unarmed = "no writer calls gov_record.py new shape-run yet"
```

The other cells are `TOOL-dTotalRecall-11`'s as landed. The `unarmed` key is optional on every row and
legal only on a `fields` row; on another form it is red.

### The grading rule

| A tracked record at a path | Graded against |
|---|---|
| under one `fields` home, Serves kind equal to that row | that row |
| under two `fields` homes, Serves kind equal to one of them | that one row |
| under a `fields` home, Serves kind naming another row | no `fields` row; listed as `home-kind mismatch` in the check's counts, never red |
| under no `fields` home | no `fields` row |

A mismatch is counted rather than red because the homes of the free-form build kinds, log and
research, are filled by `TOOL-dTotalRecall-18` at its pass and may overlap; S5 makes overlap harmless
rather than refusing it.

### Inventory

Minted: the registry key `unarmed`; `derive_record_kind` in `tools/memory-tree/record_kinds.py`. Naming
cell: `derive_record_kind` is asked of `python tools/lexicon/lexicon.py --suggest derive_record_kind --as
py.function` at the pass.

### Files touched (estimate)

- `tools/memory-tree/record-kinds.toml`
- `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/HYGIENE.template.md` (the registry view's rows)
- `memory/HYGIENE.md` (the render)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Refuse two `fields` homes that match one path.** The free-form build kinds would share
  `memory/builds/*/build/*.md`, so the refusal reds the registry the moment unit 18 fills them;
  deciding by the Serves kind needs no disjoint homes.
- **The most specific glob wins.** Specificity cannot separate log from research, whose names are
  free-form, and it misgrades a deviation record whose name happens to carry `-shape-run-`.
- **Seed one fixture shape-run record so the home is never empty.** A record no review produced is a
  forged record of the kind the check grades.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one glob match and one dict lookup per record.
- error / empty / loading states — an `unarmed` row with records is red; a row without the key and an
  empty home stays red as unit 1 §5 states.
- observability — `--check` prints each unarmed kind with its reason and the mismatch count.
- risks — an `unarmed` reason left after the writer lands: S2's red at the first record ends it.
- testing — AC1 to AC5 by the pass; the arm of §7 at the close.
- migration — none: no record moves.
- user docs — none under `help/`; the registry view in `memory/HYGIENE.md` shows the new home.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe reads the `shape-run` row of `record-kinds.toml`
  with `tomllib`, its `home` is `memory/builds/*/build/*-shape-run-*.md`.
  Red when: the home is a directory or a glob wider than the id-rule.
- **AC2** — When `python record_kinds.py --check` runs at the pass tip, it prints
  `shape-run: unarmed — no writer calls gov_record.py new shape-run yet` and exits 0; in a scratch copy
  holding one planted shape-run record in the fixture build `tX`'s `build/` folder, it exits 1
  naming the row's `unarmed` key.
  Red when: the key is read as a permanent pass, or the empty home still reds.
  fixture: a scratch copy under `%TEMP%`; the pass makes it.
- **AC3** — When `git grep -n "dIndexedDesign's planner" -- '*record_kinds.py'` runs at the pass
  tip, it prints nothing, and `--check` still prints the stream-plan unarmed line read from the row.
  Red when: the line's text is kept in the module beside the registry key.
- **AC4** — When the fixture's shape-run row reads `home = "memory/builds/tX/build/"`
  (`record_kinds.py --fixture --plant home-directory`), `--check` exits 1 naming the row.
  Red when: a bare directory passes as a home.
- **AC5** — When `record_kinds.py --fixture --plant shared-home` plants a deviation record and a
  shape-run record under `memory/builds/tX/build/` with both rows' homes matching both paths,
  `--check` grades the deviation record against the deviation row alone, and
  `derive_record_kind` over it returns the `deviation` row.
  Red when: the deviation record is graded against the shape-run fields.

## 7. Gates

`memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_kinds.py · covers AC2 AC4 AC5 · the plants `unarmed-with-record`, `home-directory` and `shared-home`, staged by grading every record under a home against that row · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-11`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How does a path under two homes find its kind?** Options: (a) the Serves kind decides and the
  home admits; (b) the most specific glob; (c) refuse overlapping homes. (b) and (c) fail as §4
  "Alternatives rejected" records. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most
  criteria met and the reuse of `canonical_kind`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 51 (HIGH, item H7).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.

## 10. Reuse audit

The seams extended are `TOOL-dTotalRecall-1`'s `check_record_kinds` and registry, `TOOL-dTotalRecall-18`'s
`home` column and `canonical_kind`, and `TOOL-dTotalRecall-25`'s stream-plan row, whose narrow home
`memory/builds/*/build/*-stream-plan-*.md` S1 copies and whose unarmed line S3 moves onto the registry.
No registry key for an empty population exists: `python tools/codebase-map/reuse_lookup.py "empty
population of a registered kind reads unarmed"` ranked name-stem neighbours (`read`, `population` in
`tools/govkit/refusal_join.py`), and that `population` enumerates refusals, not record kinds.

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
