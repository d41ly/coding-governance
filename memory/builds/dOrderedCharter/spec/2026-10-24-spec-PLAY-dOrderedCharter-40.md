# PLAY-dOrderedCharter-40 — gov's first instruction unit rows, one per reference page, and the pages' registry tags declared

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 38 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-build-PLAY-dOrderedCharter-40-deviation-401.md](../build/2026-10-24-build-PLAY-dOrderedCharter-40-deviation-401.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md](../reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-49 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`)
confirmed **finding 2 at HIGH**, its item **H2**. `PLAY-dOrderedCharter-9` §3 says "the first gov rows
land with the units that render documents from them, unit 2 the first", but unit 2 never names an
`instructions.toml`, no unit's Files touched names a kit manifest, and the `unit.*` tags unit 37
cites (`unit.kinds-register` among them) are declared by nobody. Unit 37's `doc.reference.*` registry
tags are not derived by unit 19's doc extractor either. So unit 37 S3 refuses its units page as an
empty population, its AC1 and AC8 cannot pass, unit 19's resolver reds `references.toml`, and the
`unit` namespace stays `unarmed` through the close. This unit writes gov's first `[[unit]]` rows, one
per reference page, declares the `unit.*` tags those pages cite, and makes the doc extractor mint each
page's `doc.reference.*` tag from its declaring row. It repairs unit 37 and is built right after it.

## 2. Scope (IN)

- **S1** — The rows. `tools/playbook/instructions.toml` gains four `[[unit]]` rows in unit 9 S1's
  grammar, one per page unit 37 S1 declares: `unit.policy-schema`, `unit.drive-table`,
  `unit.kinds-register` and `unit.unit-registry`. Each is a level-4 `directive` with one-line `text`
  naming where the registry lives and how a row joins it, a `usage` holding the command a user runs,
  a `help` line, `owner = "dOrderedCharter"` and `enforced-by` naming the leg that grades the
  registry; none carries a `scope` (§8 F2), so no slot and no load set selects them. Observed by AC1,
  AC2 and AC4.
- **S2** — Each row recorded through the stand-in door. The pass writes one change record per row
  through `python tools/memory-tree/build_records.py new change` (unit 15 S7), `Action add`,
  `Mark semantic`, in this build's `build/` folder, because unit 15's command refuses every write until
  dDeclaredLoop's guard lands (its S4). This makes this unit the writer unit 9 S5's `unarmed` line
  names. Observed by AC2.
- **S3** — The pages' unit tags. Each of unit 37's four `[[reference]]` rows in
  `tools/playbook/references.toml` carries its `unit` value from S1, so every page's
  `<!-- unit: <tag> -->` line resolves. Observed by AC3.
- **S4** — The pages' registry tags. Unit 19's `extract_doc` in `tools/playbook/tag_index.py` also
  reads `tools/playbook/references.toml`, minting each `[[reference]]` row's `registry` value, which
  must open `doc.reference.`, as a `doc` tag declared at that row; the `doc` namespace row's `source`
  in `tools/playbook/namespaces.toml` names the file. Observed by AC3.

## 3. Non-goals (OUT)

- The reference render, the docs leg's flags and the authored pages: unit 37's.
- The unit row's grammar, its reader and its schema: units 9 and 20.
- Rows for any other document: each chain build migrates its own step's guides (unit 20 §3).
- Loading these units into any reader's load set: §8 F2.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-37` — the four reference rows, their pages and the render, which S3 completes and AC3 observes; without them there is no page for a row to document
- **consumes-from** `PLAY-dOrderedCharter-9` — the row grammar and `read_units`, which the four rows are written in and read through
- **consumes-from** `PLAY-dOrderedCharter-19` — `extract_doc` and the `doc` namespace row, which S4 extends
- **consumes-from** `PLAY-dOrderedCharter-15` — the change record kind and its stand-in door, which S2 records each row through
- **hands-off** `PLAY-dOrderedCharter-55` — round-2 ids 3, 5 and 12: AC1's filter on `playbook-render`, and unit 37's AC1 and AC8 observed at this pass

## 4. Design

### Evidence

Read at `ce13efbe`; the seams are designs. Unit 9 §3 says "the first gov rows land with the units that
render documents from them, unit 2 the first"; unit 9 S5 prints `unarmed` "naming the unit that writes
the first rows". `git ls-files '*instructions.toml'` prints nothing at the base. Unit 37 S1 ships four
`[[reference]]` rows whose `unit` values are "named at the build run"; its data model shows
`registry = "doc.reference.kinds"` and `unit = "unit.kinds-register"`. Unit 19 S3's `doc` namespace
covers the charter, `memory/guides/*.md`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`, so no
`doc.reference.*` tag is minted. Unit 20 S1 requires `tag`, `level` and `type`, and no `scope`.

### Data model

```toml
# tools/playbook/instructions.toml
[[unit]]
tag = "unit.kinds-register"
level = 4
type = "directive"
budget = "line"
text = "MUST add a new kind as one row of tools/playbook/kinds.toml through core.py new <kind>, never by hand."
owner = "dOrderedCharter"
usage = "python tools/playbook/core.py new <kind> <name>"
help = "One register of kinds keeps each kind's factory and gate findable from one row."
enforced-by = ["core kinds"]
```

The other three rows take the same shape; their `text`, `usage` and `enforced-by` are written at the
pass from the registry each documents, as unit 37 names its readers there.

### Inventory

Minted: the tags `unit.policy-schema`, `unit.drive-table`, `unit.kinds-register` and
`unit.unit-registry`; the file `tools/playbook/instructions.toml`; four change records. The
`doc.reference.*` tags are unit 37's, declared here. Naming cells: the tag grammar's shape check (unit
10) grades the tags.

### Files touched (estimate)

- `tools/playbook/instructions.toml` (new)
- `tools/playbook/references.toml`
- `tools/playbook/tag_index.py`
- `tools/playbook/namespaces.toml`
- `memory/builds/dOrderedCharter/build/` (four change records, through the factory)

### Rollout

Live at landing, order 38, after unit 37 at order 37, so the four pages exist when their rows land.

### Alternatives rejected

- **Dropping the units page until rows exist**, the review's other fix: the build's goal names
  documents rendered from units, and an empty registry page is what unit 37 S3 refuses.
- **Unit 2 writing the rows**, as unit 9's sentence says: unit 2 renders the charter, and none of the
  charter's lines is one of these four.

## 5. Production-readiness checklist

- security: no new write path; the rows are a kit file edited by the pass and recorded through the
  stand-in door.
- perf / scale: four rows; one more file read by `extract_doc`.
- error / empty / loading states: a `registry` value outside `doc.reference.` is refused by S4 naming
  the row; the `unit` namespace prints its member count instead of `unarmed`.
- observability: `gov_tag.py show unit.kinds-register` names the row and its page.
- risks: the four `text` lines are new rules; with no `scope` they load nowhere, so they cannot move a
  load set or the charter's size.
- testing: AC1 to AC4 by probe at the pass.
- migration: none.
- user docs: the four reference pages unit 37 renders now carry resolving unit tags.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0,'tools/playbook'); import instruction_units as u; print(sorted(x.tag for x in u.read_units('.') if x.origin == 'playbook'))"`
  runs after the pass, it prints the four tags, and `python instruction_units.py schema`
  exits 0.
  Red when: a row is missing, or fails the schema.
  figure: PINNED, four rows, one per page unit 37 S1 declares.
- **AC2** — When `python gov_tag.py check` runs, the `unit` namespace is no longer printed
  `unarmed`, and `git ls-files 'memory/builds/dOrderedCharter/build/*-change-*.md'` lists one record per
  row.
  Red when: the namespace stays empty, or a row lands with no change record.
- **AC3** — When `python tools/playbook/render_playbook.py --reference --check` and
  `python gov_tag.py show doc.reference.kinds` run, the check exits 0 over the four pages
  and the tag resolves to its `[[reference]]` row.
  Red when: a page's unit tag or registry tag resolves to nothing.
- **AC4** — When `python tools/playbook/render_playbook.py --target . --check` runs, `AGENTS.md`'s region
  is byte-identical to its render before this unit.
  Red when: a row is selected into the charter.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `govkit acceptance matrix` · `memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 37's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Which readers load the four rows.** Options: (a) none, no `scope`; (b) `reader.driver`, so a
  driver's load set points at the pages; (c) `reader.every`. (b) and (c) move every affected load set
  and possibly the charter's size, which units 6 and 11 cap and no criterion here prices. RESOLVED
  (agent, 2026-10-24, delegated): (a), rung 3; a later build that wants the pointers loaded scopes them
  through unit 15's command. widens: none · relaxes: none
- **F3 — Where the `doc.reference.*` tags are declared.** Options: (a) by `extract_doc` reading each
  `[[reference]]` row; (b) by `extract_doc` reading the rendered pages under `help/reference/`; (c) by a
  new namespace. (b) mints `doc.<stem>` and not the `doc.reference.<name>` unit 37 writes, and (c)
  adds a namespace for four tags. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, the row is the
  declaring site. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's finding 2 (HIGH, item H2).
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-55.

## 10. Reuse audit

The seams are unit 9's row grammar and reader (its S1, S2), unit 19's `extract_doc` and `doc`
namespace row (its S2, S3) and unit 15's stand-in change-record door (its S7); this unit writes data
in the first and extends the second by one source file. `python tools/codebase-map/reuse_lookup.py
"declare a tag for a rendered reference page from its registry row"` ranked `rows`, `row` (two suites'
helpers) and `build_reference_index` (`tools/codebase-map/map_lib.py`, the map's own reference index)
by name stem; none is a tag extractor, which does not exist in code at the base, so none fits beyond
unit 19's designed one. The recall query returned unit 37's spec, the
spec brief's unit 37 row and the review's H2 text.

Recall terms used: `python tools/memory-recall/query.py "where are the first instruction unit rows written for the reference pages" --terms "instructions.toml unit row first rows reference page usage tag unit namespace unarmed"`
