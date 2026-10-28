# TOOL-dIndexedDesign-33 — the scout record's `seams` kind binds as an untyped kind, so its reader, check 31 and unit 4's outcome join read a real population

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 10 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 |
| [2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-35-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md`)
confirmed finding **id 20 at HIGH**, one of three ids merged into report item **H1** with ids 19 and
21. `TOOL-dIndexedDesign-13` S1 binds the scout's record `**Serves:** seams <ids>` and registers the
kind only through `record_kinds.py new`; its S3 reads records bound `seams` through `read_bindings`.
`seams` is not in `RECORD_KIND_TOKENS` (`tools/memory-tree/tree_lib.py:406`), so every such record
reads `malformed`, and the widened `read_reuse_scouts`, check 31 and `TOOL-dIndexedDesign-4`'s outcome
join all grade an empty population. Unit 4 S2 then refuses every `**Outcome:**`, and units 4 and 14
inherit the break.

This unit adds `seams` to the untyped head of `RECORD_KIND_TOKENS`, never to `TYPED_RECORD_KINDS`, so
the record keeps its `-reuse-scout[-<x>].md` home outside the typed file-name join. It repairs
`TOOL-dIndexedDesign-13` and builds one step after it, at order 10.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: the untyped head of
`RECORD_KIND_TOKENS` and `TYPED_RECORD_KINDS` (PLAY-dOrderedCharter-42 S1, S3); the `seams` registry
row unit 13 S1 writes through `record_kinds.py new` (TOOL-dTotalRecall-1 S9); and unit 13's widened
`read_reuse_scouts` and check 31 (its S3, S8).

- **S1** — `seams`, an untyped kind. `seams` joins the untyped head of `RECORD_KIND_TOKENS` in
  `tools/memory-tree/tree_lib.py`, beside `spec-audit` and `research`, and never
  `TYPED_RECORD_KINDS`. The record's home stays TOOL-dLinkedLibrary-2 S6's
  `<date>-build-<unit id>-reuse-scout[-<x>].md`, which is not `-seams-<n>.md`, so the typed join
  never reads it. The registry row unit 13 S1 writes stays. Observed by AC1 and AC3.
- **S2** — The population, seen. A record bound `seams` with its `**Index:** <sha8>` line is
  returned by `read_reuse_scouts` with its sections parsed, and check 31 grades it; a
  `-reuse-scout` record bound `research`, every one in the tree at base, reads `bound` with kind
  `research` as before. Observed by AC2.

## 3. Non-goals (OUT)

- The reader, its sections, its caps and check 31: unit 13 S3, S4 and S8. This unit adds one token.
- A rename of the scout record's home, which would break TOOL-dLinkedLibrary-2 S6's name and its
  reader.
- `fork`, `feature-design`, `diff` and `inventory`: `TOOL-dIndexedDesign-32` and
  `TOOL-dIndexedDesign-34`, H1's other ids.
- The report's left-shift registry gate: TOOL-dTotalRecall-1 S3's, another build's gate.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-13` — the `seams` kind of its S1 and its widened `read_reuse_scouts`, which read through `read_bindings` and return no `seams` record until S1 binds the token (id 20)
- **consumes-from** external — PLAY-dOrderedCharter-42 S1's untyped head of `RECORD_KIND_TOKENS` and its S3 file-name join, DEFERRED at base and an ancestor's

## 4. Design

### Evidence

- `RECORD_KIND_TOKENS` holds five kinds at `tools/memory-tree/tree_lib.py:406`, read 2026-10-28, and
  `read_bindings` marks any other first token `malformed` (`:561-565`).
- The tree's scout records at base, among them
  `memory/builds/dIndexedDesign/build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-a.md`, are
  bound `research`; unit 13 S1 grades none of them.
- PLAY-dOrderedCharter-42 S3 marks a typed-kind record malformed when its file is not
  `-<kind>-<n>.md`, so a typed `seams` would refuse every `-reuse-scout` home.

### Inventory

Minted: one tuple member. Naming cells: none apply.

### Migration

None: records bound `research` keep their kind and reader.

### Rollout

Live at its pass, order 10, one above unit 13's 9, beside `TOOL-dIndexedDesign-5` and
`TOOL-dIndexedDesign-34`. `TOOL-dIndexedDesign-34` edits the same tuple, so the two write sets meet
and `--dispatch` sequences them.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`: S1

### Alternatives rejected

- **`seams` typed, the finder's fix.** Lost to the file-name join probe above: every
  `-reuse-scout[-<x>].md` record would read malformed, and "record why the join does not apply"
  changes no code.
- **Keep binding `research` and select by file name.** Lost to unit 13 S1, which makes the kind token
  the population selector so a misnamed section cannot escape the grader.

## 5. Production-readiness checklist

- security — N/A: no write path; one tuple member.
- perf / scale — none.
- error / empty / loading states — a build with no `seams` record is graded by nothing, as unit 13
  says; a `seams` record missing `**Index:**` is unit 13's finding.
- observability — the binding check names a malformed record with its reason.
- risks — none beyond the shared tuple's sequencing with `TOOL-dIndexedDesign-34`.
- testing — AC1 to AC3 by `python -c` over a scratch repository; the arm §7 declares.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When a `python -c` calls `tree_lib.read_bindings` over a scratch repository whose build
  folder holds `2026-10-28-build-TOOL-tFix-1-reuse-scout.md` bound `**Serves:** seams TOOL-tFix-1`
  with an `**Index:**` line, it reads `bound` with kind `seams`.
  Red when: it reads `malformed`.
  fixture: a scratch repository under `%TEMP%/<short-name>`.
- **AC2** — When a `python -c` calls `tree_lib.read_reuse_scouts` over the AC1 repository with a
  second record `-reuse-scout-b.md` bound `research`, it returns the `seams` record with its
  sections, and the `research` record reads `bound` with kind `research`.
  Red when: the `seams` record is absent from the return, or the `research` record changes kind.
- **AC3** — When `python -c "import tree_lib; print('seams' in tree_lib.TYPED_RECORD_KINDS)"` runs
  in the memory-tree kit, it prints `False`, and the same test on `RECORD_KIND_TOKENS` prints `True`.
  Red when: `seams` is typed, or absent from the tokens.

## 7. Gates

`policy fixtures` · `memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 · the `--selftest` arm reading a scratch `seams` record through `read_bindings` and `read_reuse_scouts`, staged by dropping `seams` from `RECORD_KIND_TOKENS` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, promoted from the round-1 spec audit of this build, id 20
  (HIGH, item H1, shared with ids 19 and 21), on the skeptic's corrected fix, repairing
  TOOL-dIndexedDesign-13 S1 and S3.

## 10. Reuse audit

The seam is PLAY-dOrderedCharter-42 S1's untyped head of `RECORD_KIND_TOKENS` in
`tools/memory-tree/tree_lib.py`, verified at `:406` at base. The probe
`python tools/codebase-map/reuse_lookup.py "register a new record kind token so a Serves line binds"`
ranked `records`, `resolve_prefix_token`,
`check_line` and `render_line`, none a kind registry, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "how does a new Serves kind token bind in read_bindings" --terms "Serves kind token RECORD_KIND_TOKENS TYPED_RECORD_KINDS read_bindings malformed reuse-scout seams untyped"`
