# TOOL-dTotalRecall-40 — the routing region reads every record kind through `canonical_kind`, so log records written after the rename route under logs

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 9 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-36 TOOL-dTotalRecall-39 TOOL-dTotalRecall-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
confirmed finding **id 36 at HIGH**, its item **H5**, alone in that item; its finding id 9 reports the
same defect at MEDIUM in item M8 and is disposed in `TOOL-dTotalRecall-43`. `TOOL-dTotalRecall-4` §4
"The routing region" routes "each build/ record whose kind is `journal`", read raw from the bindings
`plan()` reads once. `TOOL-dTotalRecall-18` (order 4) renames the kind `log` before unit 4 (order 8)
builds: every writer writes `log` from then on, `read_bindings` keeps the written token, and every
comparison goes through `canonical_kind` (`TOOL-dTotalRecall-18` S7, S8). Spec 4 never names
`canonical_kind`, so its region shows only the legacy `journal` records and drops every log record
written after the rename. This unit makes `render_routes` compare every kind through `canonical_kind`,
names the row `logs`, and adds a census arm that reds a raw comparison of a retired kind token
anywhere in the tool root. It repairs `TOOL-dTotalRecall-4`.

## 2. Scope (IN)

- **S1** — `render_routes` in `tools/memory-tree/gen_build_index.py` takes each record's kind as
  `canonical_kind(<the written token>)` from `tools/memory-tree/tree_lib.py`
  (`TOOL-dTotalRecall-18` S7) before it compares it, on every row: deviations against `deviation`,
  research against `research`, and the row whose purpose reads `logs` against `log`. A record bound
  `**Serves:** journal` and one bound `**Serves:** log` both route under `logs`. Every build README's
  `build-routes` region is re-rendered by `gen_build_index.py --write`. Observed by AC1 and AC2.
- **S2** — The alias census, `check_alias_compares(root)` in `tools/memory-tree/record_kinds.py`, run
  by `--check`. It lists every tracked `*.py`, `*.sh` or `*.js` line under the tool root that spells a
  key of `KIND_ALIASES` as a quoted literal inside a comparison (`==`, `!=`, ` in (`, ` in [`, a `case`
  arm), outside `tree_lib.py`'s `KIND_ALIASES` itself. A line is red unless the constant
  `ALIAS_COMPARE_KEPT` lists its file with a reason, for a fixture that plants a legacy record on
  purpose. The predicate is run over the real tree before the constant is written. Observed by AC3.
- **S3** — Unit 2's half of the finding, its S9 row list naming the `journal` row, is handed to
  `TOOL-dTotalRecall-43`, because the door `gov_record.py` is built at order 12, after this unit. S2's
  census reds that half at the close if the door compares the alias token raw. NOT OBSERVED by a
  criterion of this unit: `TOOL-dTotalRecall-43`'s item for id 9 observes it.

## 3. Non-goals (OUT)

- The routing region's other purposes, its bound of three records per purpose and its card row:
  `TOOL-dTotalRecall-4`'s, unchanged.
- The rename, `KIND_ALIASES` and `canonical_kind`: `TOOL-dTotalRecall-18`'s.
- Rewriting any record's Serves token: the alias is read, never normalised on disk.

### Edges

- **consumes-from** `TOOL-dTotalRecall-4` — `render_routes` and the `build-routes` region, whose kind
  comparisons this unit routes through `canonical_kind`
- **consumes-from** `TOOL-dTotalRecall-18` — `canonical_kind` and `KIND_ALIASES` in `tree_lib.py`, the
  one alias reader S1 calls and the alias set S2's census reads
- **consumes-from** `TOOL-dTotalRecall-1` — `record_kinds.py` and its `--check`, which the alias census
  joins
- **hands-off** `TOOL-dTotalRecall-43` — the door's S9 row list naming the retired `journal` row,
  `TOOL-dTotalRecall-2`'s half of this finding and of id 9, built at order 12 after this unit
- **hands-off** `TOOL-dTotalRecall-53` — `check_alias_compares` and `ALIAS_COMPARE_KEPT`, whose forms, population and keep grammar that unit widens (the round-1 audit of units 36 to 43, ids 19, 29, 36 and 46)

## 4. Design

### The region, after this unit

| Purpose | Read |
|---|---|
| deviations | each record whose `canonical_kind` is `deviation` |
| research | each `build/` record whose `canonical_kind` is `research` |
| logs | each `build/` record whose `canonical_kind` is `log`, a `journal` binding read as its alias |

The other rows of `TOOL-dTotalRecall-4` §4 are unchanged. The kinds still come from `binds_all`, read
once; only the comparison changes.

### The census at base

`git grep -nE "['\"]journal['\"]" -- tools` at base `462d20f3` lists the writers and readers
`TOOL-dTotalRecall-18` S7's Readers clause names, which that unit re-points before this one builds. At
this unit's pass base the census therefore reads the comparisons unit 18 left, and a hit outside the
kept fixtures is a comparison to re-point in this pass, by the same rule as S1.

### Inventory

Minted: `check_alias_compares` and `ALIAS_COMPARE_KEPT` in `tools/memory-tree/record_kinds.py`; the
`logs` purpose. Naming cell: `check_alias_compares` is asked of
`python tools/lexicon/lexicon.py --suggest check_alias_compares --as py.function` at the pass.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/record_kinds.py`
- `memory/builds/` (each README's `build-routes` region, re-rendered by `gen_build_index.py --write`)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Route on the written token and list both `journal` and `log` in the row.** Two spellings of one
  kind in one renderer, which is the comparison class `canonical_kind` exists to end.
- **Normalise the token on read in `read_bindings`.** `TOOL-dTotalRecall-18` §8 rejected it: every
  records region would change bytes.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one dict lookup per record kind; the census is one `git grep` per check run.
- error / empty / loading states — a build with no log record renders no `logs` row, as before.
- observability — the census names each file and line.
- risks — every build README's routes region changes once, which the re-render commits.
- testing — AC1 to AC3 by the pass; the arms of §7 at the close.
- migration — the one re-render of S1.
- user docs — none under `help/`: no page describes the routing region.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --write` runs in a scratch clone under
  `%TEMP%` holding one build folder with a `build/` record bound `**Serves:** log X-a-1` and another
  bound `**Serves:** journal X-a-1`, its README's `build-routes` region names both under `logs`.
  Red when: the region compares the written token, so the `log` record is absent.
  fixture: the scratch clone; the pass makes it.
- **AC2** — When `git grep -n "journal" -- tools/memory-tree/gen_build_index.py` runs at the pass tip,
  no line inside `render_routes` spells it.
  Red when: the renderer keeps a raw comparison beside the `canonical_kind` call.
- **AC3** — When `python record_kinds.py --check` runs in a scratch copy where a
  planted file under the tool root spells `if kind == "journal":`, it exits 1 naming that file and line
  under the alias census; at the pass tip it names no line outside `ALIAS_COMPARE_KEPT`.
  Red when: the census reads only `gen_build_index.py`, so a comparison in another module escapes.

## 7. Gates

`build-index selftest` · `build README slot contract` · `tier2-review self-test` · `memory hygiene` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 · the routes plant with a `log` and a `journal` record, staged by comparing the written token · none
New arm: tools/memory-tree/record_kinds.py · covers AC3 · the alias census plant `raw-alias-compare`, staged by cutting `check_alias_compares` from `--check` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-4`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Is the row's purpose label `journals` or `logs`?** Options: (a) `logs`, the canonical kind's
  name; (b) `journals`, keeping the region's bytes for legacy-only builds. (b) labels the canonical
  kind by its alias, the reading `TOOL-dTotalRecall-18` S9 re-spells in every prose carrier.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the report's fix text and unit 18's S9.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's id 36 (HIGH, item H5).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted.

## 10. Reuse audit

The seams extended are `TOOL-dTotalRecall-4`'s `render_routes` in `tools/memory-tree/gen_build_index.py`
and `TOOL-dTotalRecall-18`'s `canonical_kind`, the one alias reader, which this unit calls rather than
re-spelling the alias; the census joins `TOOL-dTotalRecall-1`'s `record_kinds.py --check`. No existing
census compares code against an alias table: `python tools/codebase-map/reuse_lookup.py "route build
records into README by kind"` ranked name-stem neighbours (`build`, `records`, `readme`), none of which
reads kinds.

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
