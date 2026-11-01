# TOOL-dScopedBuild-31 — `core-result` registered as a typed record kind through the registry factory, its records bound `**Serves:** core-result`

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 10 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md) | research | TOOL-dScopedBuild-25 TOOL-dScopedBuild-28 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-35 |
| [2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-30 TOOL-dScopedBuild-28 TOOL-dScopedBuild-34 TOOL-dScopedBuild-27 TOOL-dScopedBuild-29 TOOL-dScopedBuild-26 TOOL-dScopedBuild-25 TOOL-dScopedBuild-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
confirmed finding **id 20 at HIGH**, report item **H7**. `TOOL-dScopedBuild-7` S5 registers
`core-result` as a kind of `tools/memory-tree/build_records.py`, names its file
`-core-result-<n>.md`, and binds it `**Serves:** journal` "so no binding kind is minted". Under the
ancestor PLAY-dOrderedCharter-42, the factory's per-kind table is refused at import when its keys
differ from `TYPED_RECORD_KINDS` in `tree_lib.py` (S2), and a `-<kind>-<n>.md` file whose Serves kind
is not `<kind>` is malformed (S3); TOOL-dTotalRecall-1 S3's `record-kinds` leg reds a typed kind with
no registry row. Built as written, the factory refuses at import, taking `deviation_join.py` down
with it, or every core-result record reads as malformed.

This unit registers the kind the way the parents register theirs and binds the record to its own
kind. It repairs `TOOL-dScopedBuild-7` and builds one step after it (order 10).

## 2. Scope (IN)

- **S1** — The row. `python tools/memory-tree/record_kinds.py new core-result --tag
  record.core-result --writer "build_records.py new" --check "memory hygiene" --field Range --field
  Attributed --field Bar --field Core --field Verdict --field Reds --field "Decision rows"`
  (TOOL-dTotalRecall-1 S9) appends the kind's row to `tools/memory-tree/record-kinds.toml`, its
  fields unit 7 §4 "The record"'s seven, in that order. Observed by AC1.
- **S2** — The typed kind. `core-result` joins `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py`
  (PLAY-dOrderedCharter-42 S1), and the factory's per-kind table in `build_records.py` gains its row,
  the seven fields required and `Verdict`'s closed set unit 7 §4 "The verdict" names, so the import
  check of PLAY-dOrderedCharter-42 S2 holds. Observed by AC2.
- **S3** — The binding. The record's binding line reads `**Serves:** core-result <every roster unit
  id>`, superseding unit 7 S5's and §4 "The record"'s `**Serves:** journal` and the sentence "so no
  binding kind is minted". The file name stays `<date>-build-<first roster unit>-core-result-<n>.md`,
  so PLAY-dOrderedCharter-42 S3's file-name join reads it well-formed. Observed by AC3.
- **S4** — The grammar's list. `python tools/memory-tree/record_kinds.py --write` re-renders the
  `gen:record-kinds` region of `tools/memory-tree/HYGIENE.template.md` (TOOL-dTotalRecall-1 S6), and
  its render `memory/HYGIENE.md` carries it, so the record grammar names the kind. Observed by AC4.

## 3. Non-goals (OUT)

- The core run, its verdict and the record's fields: unit 7's.
- The `scope` kind's registration, id 21 of the same audit, a MEDIUM, which `TOOL-dScopedBuild-35`
  S7 takes through the same factory.
- The loose-stem reading of `-<kind>-<n>.md` that PLAY-dOrderedCharter-59 files against the typed
  join; no tracked file ends `-core-result-<n>.md` at base, so this kind adds no collision.
- The left-shift spec-lint rule the report names. No clause of this build names it.

### Edges

- **consumes-from** `TOOL-dScopedBuild-7` — S5's `core-result` record and §4 "The record", whose kind S1 to S4 register and whose binding S3 supersedes (id 20)
- **consumes-from** external — TOOL-dTotalRecall-1 S1, S6 and S9 (the registry, its HYGIENE region and its factory) and PLAY-dOrderedCharter-42 S1 to S3 (the typed tuple, the import check and the file-name join), DEFERRED at base and an ancestor's

## 4. Design

### Evidence

- PLAY-dOrderedCharter-42 S1 to S3 (`memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-42.md:34-50`).
- TOOL-dTotalRecall-1 S3 reds "a member of `TYPED_RECORD_KINDS` with no row", and S9 makes
  `record_kinds.py new` the factory (`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md:74-82`, `:101-105`).
- The parents register their kinds this way: TOOL-dIndexedDesign-13 S1 registers `seams` with
  `--check "memory hygiene"`, and TOOL-dIndexedDesign-10 S1 and -11 register theirs.
- `git ls-files | grep -cE -- '-core-result-[0-9]+\.md$'` printed 0 at `c891f007`, PINNED on
  2026-11-01.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `core-result` | typed record kind, registry row and `TYPED_RECORD_KINDS` member | none |
| `record.core-result` | registry tag | none |

### Migration

None: unit 7 writes no core-result record before this unit lands, since it builds one step earlier
and its records are written at the close.

### Rollout

Built at order 10, one step after unit 7 (order 9), tied with unit 15, whose files it does not write.

### Files touched (estimate)

- `tools/memory-tree/record-kinds.toml`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`
- `memory/HYGIENE.md`

### Alternatives rejected

- **A plain journal record whose name avoids the typed shape, the report's second way.** It keeps a
  kind unit 7 carries as `node:record-kind.core-result` out of the registry that is the one
  declaration of every kind, so the node names a kind nothing declares.
- **Keep `journal` and the typed name.** PLAY-dOrderedCharter-42 S3 reads that file as malformed.

## 5. Production-readiness checklist

- security — no new write path; the factory writes the record, as unit 7 planned.
- perf / scale — one more registry row and tuple member.
- error / empty / loading states — a record missing a field is refused by the factory's table.
- observability — the HYGIENE region lists the kind.
- risks — the parents land the registry first; this unit cannot run before them, which §3 names.
- testing — AC1 to AC4 by probe and through the factory's fixture.
- migration — none.
- user docs — `memory/HYGIENE.md` through its template.

## 6. Acceptance criteria

- **AC1** — When `python -c` loads the memory-tree kit's `record-kinds.toml` with `tomllib`, one
  `[[record-kind]]` row is named `core-result`, its `tag` `record.core-result`, its `writer`
  `build_records.py new` and its fields the seven S1 lists in order.
  Red when: the kind has no row, or a field is missing.
- **AC2** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import tree_lib,
  build_records; print('core-result' in tree_lib.TYPED_RECORD_KINDS)"` runs, it prints `True` and
  raises nothing.
  Red when: the factory refuses at import, or the tuple lacks the kind.
- **AC3** — When `build_records.py new core-result` writes a record in a scratch build folder,
  `tree_lib.read_bindings` reads it as kind `core-result` and well-formed; a planted
  `-core-result-1.md` bound `**Serves:** journal` reads malformed naming `core-result`.
  Red when: the written record is malformed, or the planted journal binding is admitted.
  fixture: a scratch memory root under the run's scratch directory.
- **AC4** — When `grep -n "core-result" tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md`
  runs, it prints the region's line in each file.
  Red when: the grammar's kind list omits the kind.

## 7. Gates

`policy fixtures` · `memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/build_records.py · covers AC3 · the factory's `--fixture --plant typed-kinds` over a `core-result` record and a journal-bound twin, staged by binding the record `journal` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 7's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none
- **F2 — Typed kind or plain journal?** Options: (a) register `core-result` as a typed kind; (b) a
  journal record with a non-typed name. (b) leaves unit 7's `node:record-kind.core-result` declared by
  no registry row, against TOOL-dTotalRecall-1's one declaration. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, the most feature-rich survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15, id 20
  (HIGH, item H7).

## 10. Reuse audit

The seam is the record-kind factory, TOOL-dTotalRecall-1 S9's `record_kinds.py new`, and the typed
tuple PLAY-dOrderedCharter-42 S1 adds, the route every parent unit registers a kind through.
`python tools/codebase-map/reuse_lookup.py "register a new typed record kind in the record kind
registry"` ranked `records`, `extract_records`, `measure_typed_counts`, `read_records` and
`render_record`; none registers a kind, and the factory is not in the tree at base, so the spec
corpus is where it was found. The recall probe surfaced PLAY-dOrderedCharter-59, the loose-stem ask
§3 names.

Recall terms used: `python tools/memory-recall/query.py "how is a new typed record kind registered" --terms "record_kinds.py new TYPED_RECORD_KINDS record-kinds.toml factory build_records typed kind Serves file-name join"`
