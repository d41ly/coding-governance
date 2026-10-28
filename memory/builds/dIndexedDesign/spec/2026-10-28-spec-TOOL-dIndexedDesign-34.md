# TOOL-dIndexedDesign-34 — re-entry's `diff` and `inventory` kinds bind as typed kinds, and the diff record has one writer of the typed name

**Status:** DEFERRED · rev-3 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 10 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md`)
confirmed finding **id 21 at HIGH**, one of three ids merged into report item **H1** with ids 19 and
20. `TOOL-dIndexedDesign-20` S4 and S7 bind `**Serves:** diff` and `**Serves:** inventory` and register
both only through `record_kinds.py new`. Neither token is in `RECORD_KIND_TOKENS`
(`tools/memory-tree/tree_lib.py:406`), so both read `malformed` (`:561-565`), and unit 20 S8's
`check_inventory` finds no inventory record. Unit 20 S4 also names `design_lib.py --reentry --write`
as the writer of a `-diff-<n>.md` record with its own next-free `<n>`, a second writer of the typed
file-name grammar PLAY-dOrderedCharter-42 S1 and S2 give to `build_records.py`, so the two can
disagree on `<n>`.

Both homes fit the typed grammar, so this unit adds `diff` and `inventory` to `TYPED_RECORD_KINDS`
and the factory's per-kind table, and makes the re-entry writer take the record's name and `<n>` from
that factory. It repairs `TOOL-dIndexedDesign-20` and builds one step after it, at order 10.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: `TYPED_RECORD_KINDS` and the file-name
join (PLAY-dOrderedCharter-42 S1, S3); `tools/memory-tree/build_records.py`, its name grammar
`<date>-build-<unit id>-<kind>-<n>.md`, its `<n>` collision rule and its per-kind table checked
against `TYPED_RECORD_KINDS` at import (PLAY-dOrderedCharter-7 S7, PLAY-dOrderedCharter-42 S2); the
`diff` and `inventory` registry rows unit 20 S4 and S7 write; and unit 20's `--reentry --write` and
`check_inventory` (its S5, S8).

- **S1** — Two typed kinds. `diff` and `inventory` join `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py`, and `build_records.py`'s per-kind table gains their rows: `diff`
  requires `Feature`, `Base`, `Head`, `Change`, `Affected`, `Triggers`, `Level` and `Route`, with
  `Level` closed over `unit` and `feature`; `inventory` requires `Input`, `Of` and `Verdict`. The
  homes `-diff-<n>.md` and `-inventory-<n>.md` in a build's `build/` folder are the typed grammar, so
  the file-name join polices both ways. Observed by AC1, AC2 and AC4.
- **S2** — One writer of the typed name. `design_lib.py --reentry --write` (unit 20 S4, S5) imports
  `build_records.py` and takes each diff record's file name and `<n>` from the factory's name grammar
  and collision rule; `design_lib.py` derives no `<n>` of its own. Unit 20 S4's "the next number free
  for that unit" is the factory's number. Observed by AC3.

## 3. Non-goals (OUT)

- A `new diff` verb on the factory. The re-entry CLI stays the diff record's door, as unit 20 S4
  registers it; it now names its file through the factory.
- `inventory`'s writer, which unit 20 S7 registers as `hand`; S1 grades its fields and nothing writes
  it here.
- `fork`, `feature-design` and `seams`: `TOOL-dIndexedDesign-32` and `TOOL-dIndexedDesign-33`.
- The report's left-shift registry gate: TOOL-dTotalRecall-1 S3's, another build's gate.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-20` — the `diff` and `inventory` kinds of its S4 and S7, `--reentry --write` and `check_inventory`, which read through `read_bindings` and see nothing until S1 binds, and whose own next-free `<n>` S2 replaces with the factory's (id 21)
- **consumes-from** external — PLAY-dOrderedCharter-42 S1 to S3's `TYPED_RECORD_KINDS` and file-name join, and PLAY-dOrderedCharter-7 S7's `build_records.py`, each DEFERRED at base and an ancestor's
- **hands-off** `TOOL-dIndexedDesign-43` — S1's typed `inventory` row, to which that unit adds `Of` and `Verdict` as repeatable fields (id 13)
- **hands-off** `TOOL-dIndexedDesign-46` — S2's diff writer, whose number that unit scopes to the build and allocates over tracked and on-disk files, and AC3's fixture (ids 14, 35 and 34)
- **hands-off** `TOOL-dIndexedDesign-53` — this unit's pass commit also carries `TOOL-dIndexedDesign-43`'s S1 to S3 and that unit's S14 list shape, so `inventory` is typed and admits repeated `Of` and `Verdict` in one commit (ids 4 and 29)

## 4. Design

### Evidence

- `RECORD_KIND_TOKENS` holds five kinds at `tools/memory-tree/tree_lib.py:406`, read 2026-10-28;
  `diff` and `inventory` are not among them.
- PLAY-dOrderedCharter-7 S7 extracts the typed factory from `deviation_join.py` with "the name
  grammar ... the tracked population and the `<n>` collision", so the factory already owns the
  number a second writer would re-derive.
- Unit 20 §4 "A diff record" spells the fields S1's table requires; its S7 spells the inventory
  fields.

### Inventory

Minted: two tuple members and two per-kind table rows. No function, flag, file or constant. Naming
cells: none apply.

### Migration

None: no diff or inventory record exists at base.

### Rollout

Live at its pass, order 10, one above unit 20's 9, beside `TOOL-dIndexedDesign-5` and
`TOOL-dIndexedDesign-33`, which edits the same tuple, so `--dispatch` sequences the two.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`: S1
- `tools/memory-tree/build_records.py`: S1's table rows
- `tools/memory-tree/design_lib.py`: S2

### Alternatives rejected

- **Keep `--reentry --write`'s own `<n>` and state in §8 why it is a second door.** Lost to the
  disagreement the finding names: two derivations of one number over one folder can collide, and the
  factory's collision rule is the one the file-name join was written beside.
- **Both kinds untyped.** Lost to the join read the other way: a `-diff-<n>.md` file bound to another
  kind would pass, and no table row would grade the closed `Level`.

## 5. Production-readiness checklist

- security — the write path is unit 20's; S2 narrows it to the factory's one name grammar.
- perf / scale — none.
- error / empty / loading states — a misnamed record reads `malformed` naming its kind; a field
  outside `Level`'s set is refused by the factory's reader.
- observability — the binding check names each malformed record.
- risks — PLAY-dOrderedCharter-42 S2 refuses `build_records.py` at import if the tuple and the table
  differ, so S1's two edits land in one commit.
- testing — AC1 to AC4 by `python -c` and the CLI over a scratch repository; the arm §7 declares.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` calls `tree_lib.read_bindings` over a scratch repository holding
  `2026-10-28-build-TOOL-tFix-1-diff-1.md` bound `**Serves:** diff TOOL-tFix-1 TOOL-tFix-2` and
  `2026-10-28-build-TOOL-tFix-1-inventory-1.md` bound `**Serves:** inventory TOOL-tFix-1`, both read
  `bound` with kinds `diff` and `inventory`.
  Red when: either reads `malformed`.
  fixture: a scratch repository under `%TEMP%/<short-name>`.
- **AC2** — When the same call reads `2026-10-28-build-TOOL-tFix-1-diff-2.md` bound `research`, it
  reads `malformed` naming `diff`.
  Red when: the misnamed record binds.
- **AC3** — When `python design_lib.py --reentry tFix --base <rev> --write` runs over a scratch build
  whose unit already holds `-diff-1.md`, the record it writes is named `-diff-2.md`, and
  `grep -n "build_records" design_lib.py` prints its import.
  Red when: it writes `-diff-1.md` over the existing record, or `design_lib.py` derives the number
  without the factory.
- **AC4** — When `python -c "import build_records"` runs with both kinds in the tuple and the table, it
  imports; with the `inventory` row staged away, it refuses naming `inventory`.
  Red when: the module loads with the two lists apart.

## 7. Gates

`policy fixtures` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/build_records.py · covers AC1 AC2 AC4 · the `typed-kinds` plant now writing a `diff` and an `inventory` record, staged by dropping `diff` from `TYPED_RECORD_KINDS` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of this build, id 21
  (HIGH, item H1, shared with ids 19 and 20), on its sound fix, repairing TOOL-dIndexedDesign-20 S4
  and S7.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dIndexedDesign-43 and TOOL-dIndexedDesign-46, promoted by the round-1 spec audit of
  units 31 to 38; nothing else moved.
- rev-3 · 2026-10-28 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dIndexedDesign-53, promoted by the round-1 spec audit of units 39 to 46; nothing else
  moved.

## 10. Reuse audit

The seams are PLAY-dOrderedCharter-42 S1's `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py`
and PLAY-dOrderedCharter-7 S7's `build_records.py` name grammar and `<n>` collision, which S2 imports
instead of re-deriving. The probe
`python tools/codebase-map/reuse_lookup.py "register a new record kind token so a Serves line binds"`
ranked `records`, `resolve_prefix_token`, `check_line` and `render_line`,
none a kind registry or a record namer, so no other seam fits; the factory is unbuilt at base.

Recall terms used: `python tools/memory-recall/query.py "who names a typed build record file and its number" --terms "typed record factory build_records TYPED_RECORD_KINDS diff inventory next-free number collision file-name join"`
