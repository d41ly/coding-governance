# TOOL-dIndexedDesign-32 — the feature level's Serves kinds bind: `fork` a typed kind, `feature-design` an untyped one, and `roster` a region that binds nothing

**Status:** DEFERRED · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 9 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-32-deviation-321.md](../build/2026-10-28-build-TOOL-dIndexedDesign-32-deviation-321.md) | deviation | — |
| [2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md`)
confirmed finding **id 19 at HIGH**, one of three ids merged into report item **H1** with ids 20 and
21. `TOOL-dIndexedDesign-8` S1 and S6 bind `**Serves:** feature-design` and `**Serves:** fork`, and
register both only through `record_kinds.py new`, which TOOL-dTotalRecall-1 S9 says only "appends a
conforming row". Neither token joins `RECORD_KIND_TOKENS` (`tools/memory-tree/tree_lib.py:406`), and
`read_bindings` marks any other first token `malformed` (`tree_lib.py:561-565`). Built as written,
every feature design and fork record reads malformed, `read_feature_designs` sees no feature,
`check_fork_records` sees no fork, and the hygiene binding check reds each record.

This unit makes both kinds bind by the seam the parents use for a new kind, choosing per kind by its
home name: `fork` joins `TYPED_RECORD_KINDS`, whose file-name join its `-fork-<n>.md` home fits, and
`feature-design` joins the untyped head, because its `-feature-<seg>.md` home does not. It repairs
`TOOL-dIndexedDesign-8` and builds one step after it, at order 9. Ids 20 and 21, the other two ids of
H1, are `TOOL-dIndexedDesign-33` and `TOOL-dIndexedDesign-34`.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: `TYPED_RECORD_KINDS`, the untyped head of
`RECORD_KIND_TOKENS` and the file-name join both ways (PLAY-dOrderedCharter-42 S1, S3); the typed
record factory `tools/memory-tree/build_records.py` with its per-kind table of required fields and
closed sets, refused at import when its keys differ from `TYPED_RECORD_KINDS`
(PLAY-dOrderedCharter-7 S7, PLAY-dOrderedCharter-42 S2); the `typed-kinds` plant
(PLAY-dOrderedCharter-42 S4); and the `feature-design`, `roster` and `fork` registry rows unit 8 S1,
S4 and S6 write through `record_kinds.py new` (TOOL-dTotalRecall-1 S9).

- **S1** — `fork`, a typed kind. `fork` joins `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py`, and `build_records.py`'s per-kind table gains its row: required
  fields `Fork`, `Level`, `Class`, `Resolver`, `Options` and `Pick`, with the closed sets unit 8 S6
  states, `Level` over `unit` and `feature`, `Class` over `fact`, `preference` and `goal`, and
  `Resolver` over `agent` and `owner`. Its home, `<date>-build-<unit id>-fork-<n>.md` in a build's
  `build/` folder, is the typed grammar, so the file-name join polices it both ways. Observed by AC1,
  AC2 and AC3.
- **S2** — `feature-design`, an untyped kind. `feature-design` joins the untyped head of
  `RECORD_KIND_TOKENS` beside `spec-audit`, `diff-review`, `journal` and `research`, and never
  `TYPED_RECORD_KINDS`: its home `<date>-build-<first unit id>-feature-<seg>.md` names a segment, not a
  number, so the typed join would mark every such record malformed. A `feature-design` record is
  selected by its binding, as unit 8 S2's `read_feature_designs` already selects it. Observed by AC1
  and AC4.
- **S3** — `roster` binds nothing. Unit 8 S4's `roster` kind lives in the build README's
  `<!-- roster:units -->` region, which carries no `**Serves:**` line, so no token is added for it and
  its registry row stays as unit 8 S4 writes it. Observed by AC4.

## 3. Non-goals (OUT)

- The registry rows themselves and their factory: unit 8 S1, S4 and S6 write them, TOOL-dTotalRecall-1
  owns the factory. This unit adds token membership and one per-kind table row.
- `seams`, `diff` and `inventory`, H1's other kinds: `TOOL-dIndexedDesign-33` and
  `TOOL-dIndexedDesign-34`.
- `coverage-lens` and `overlap`, the same class at MEDIUM: report ids 18 and 22, batched into
  `TOOL-dIndexedDesign-38`.
- The report's left-shift gate, a registry check that reds a row whose token `read_bindings` would not
  bind. It extends TOOL-dTotalRecall-1 S3, another build's gate; no clause of this build names it.
- A hand edit of `memory/HYGIENE.md`'s kind list: TOOL-dTotalRecall-1 S6 renders it from the registry.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-8` — the `feature-design` and `fork` kinds of its S1 and S6, their `-feature-<seg>.md` and `-fork-<n>.md` homes, and `read_feature_designs` and `check_fork_records`, which read through `read_bindings` and see nothing until S1 and S2 bind (id 19)
- **consumes-from** external — PLAY-dOrderedCharter-42 S1 to S4's `TYPED_RECORD_KINDS`, untyped head, file-name join and `typed-kinds` plant, and PLAY-dOrderedCharter-7 S7's `build_records.py`, each DEFERRED at base and an ancestor's
- **hands-off** `TOOL-dIndexedDesign-42` — S1's typed `fork` kind, under whose per-build collision that unit numbers fork files within the build (id 12)
- **hands-off** `TOOL-dIndexedDesign-46` — S1's closed sets in the per-kind table, which that unit makes the fork join's one source (id 8)

## 4. Design

### Evidence

- `RECORD_KIND_TOKENS = ("spec-audit", "diff-review", "journal", "research", "deviation")` at
  `tools/memory-tree/tree_lib.py:406`, read 2026-10-28. `read_bindings` (`:471`) sets `malformed` with
  "first token ... is not one of" any other kind (`:561-565`).
- The deviation join (`tree_lib.py:566-576`) is the both-ways file-name rule PLAY-dOrderedCharter-42
  S3 generalises to every member of `TYPED_RECORD_KINDS`: a `-<kind>-<n>.md` file bound to another
  kind, or a typed-kind record not so named, is malformed.
- `record_kinds.py` and `record-kinds.toml` are absent at base; `TYPED_RECORD_KINDS` appears nowhere
  under `tools/` at base. Both are specced parents, built before this build run.
- Unit 8 S6's closed sets are the fork record's own field values; the per-kind table is where
  PLAY-dOrderedCharter-7 S7 puts each typed kind's required fields and closed sets.

### Inventory

Minted: two tuple members and one per-kind table row. No function, flag, file or constant. Naming
cells: none apply.

### Migration

None: no fork or feature design record exists at base, and unit 8's checks grade only from its
`SPEC_FORK_RECORD_CUTOFF`.

### Rollout

Live at its pass, order 9, one above unit 8's 8, beside `TOOL-dIndexedDesign-13` and
`TOOL-dIndexedDesign-20`. `TOOL-dIndexedDesign-13` also writes `tree_lib.py` (its S3 reader), so
the two write sets meet and `--dispatch` sequences them; `TOOL-dIndexedDesign-33` and
`TOOL-dIndexedDesign-34` at order 10 edit the same tuple after this one.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`: S1, S2
- `tools/memory-tree/build_records.py`: S1's per-kind table row

### Alternatives rejected

- **Both kinds typed, the finder's fix.** Lost to the file-name join: `-feature-<seg>.md` is not
  `-feature-design-<n>.md`, so PLAY-dOrderedCharter-42 S3 would mark every feature design record
  malformed. Renaming the home to `-feature-design-<n>.md` loses the feature segment unit 8 S1 keys
  the file by.
- **Both kinds untyped.** Lost to the same join read the other way: a `-fork-<n>.md` file bound
  `feature-design` would pass, and no factory row would grade the fork's closed sets.

## 5. Production-readiness checklist

- security — N/A: no write path, no input surface; two tuple members.
- perf / scale — none: a tuple membership test.
- error / empty / loading states — a misnamed record reads `malformed` naming the kind; a build with
  no such record is graded by nothing, as unit 8 S5 says.
- observability — the binding check names each malformed record with its reason.
- risks — the import-time check of PLAY-dOrderedCharter-42 S2 refuses `build_records.py` if S1 adds
  the tuple member without the table row, so the two land in one commit.
- testing — AC1 to AC4 by `python -c` over a scratch repository; the arm §7 declares.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` calls `tree_lib.read_bindings` over a scratch repository whose build
  folder holds `2026-10-28-build-TOOL-tFix-1-feature-record-door.md` bound
  `**Serves:** feature-design TOOL-tFix-1` and `2026-10-28-build-TOOL-tFix-1-fork-1.md` bound `**Serves:** fork TOOL-tFix-1`, both
  read `bound`, with kinds `feature-design` and `fork`.
  Red when: either reads `malformed`.
  fixture: a scratch repository under `%TEMP%/<short-name>`.
- **AC2** — When the same `read_bindings` call reads `2026-10-28-build-TOOL-tFix-1-fork-2.md` bound
  `feature-design`, and `2026-10-28-build-TOOL-tFix-1-feature-x.md` bound `fork`, each reads
  `malformed` and its reason names `fork`.
  Red when: either binds.
- **AC3** — When `python -c "import build_records"` runs with `fork` in `TYPED_RECORD_KINDS` and in the
  per-kind table, it imports; with the table row staged away, the import refuses naming `fork`; and
  reading a fork record whose `Class` is `preferences` is refused naming the closed set.
  Red when: the module loads with the two lists apart, or the misspelled class reads clean.
- **AC4** — When a `python -c` calls `design_lib.read_feature_designs` over the AC1 repository, it
  returns `feature.record-door`; and `grep -c '"roster"' tree_lib.py` prints 0.
  Red when: the feature is not seen, or a `roster` token is added.

## 7. Gates

`policy fixtures` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/build_records.py · covers AC1 AC2 AC3 · the `typed-kinds` plant now writing a fork record beside the other typed kinds and a `feature-design` record beside them, staged by dropping `fork` from `TYPED_RECORD_KINDS` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of this build, id 19
  (HIGH, item H1, shared with ids 20 and 21), on the skeptic's corrected fix, repairing
  TOOL-dIndexedDesign-8 S1, S2 and S6.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dIndexedDesign-42 and TOOL-dIndexedDesign-46, promoted by the round-1 spec audit of
  units 31 to 38; nothing else moved.

## 10. Reuse audit

The seam is the parents' own route for a new kind: PLAY-dOrderedCharter-42 S1's `TYPED_RECORD_KINDS`
and untyped head in `tools/memory-tree/tree_lib.py`, its S3 file-name join and PLAY-dOrderedCharter-7
S7's per-kind table, the way TOOL-dTotalRecall-25 S6 and TOOL-dLinkedLibrary-8 S1 make their kinds
bind. The probe
`python tools/codebase-map/reuse_lookup.py "register a new record kind token so a Serves line binds"`
ranked `records`, `resolve_prefix_token`, `check_line` and `render_line`, none a kind
registry; the tuple at `tree_lib.py:406` is the one seam, verified at base.

Recall terms used: `python tools/memory-recall/query.py "how does a new Serves kind token bind in read_bindings" --terms "Serves kind token RECORD_KIND_TOKENS TYPED_RECORD_KINDS read_bindings malformed record factory file-name join"`
