# TOOL-dTotalRecall-56 — the alias census keeps the pinned departures instrument's `journal` compare by its path-keyed row, never by a marker in its bytes

**Status:** OPEN · rev-4 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 30 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-54 TOOL-dTotalRecall-59 TOOL-dTotalRecall-55 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
confirmed finding **id 15 at HIGH**. It shares item **H1** with ids 4, 24 and 37, which
`TOOL-dTotalRecall-57`, `TOOL-dTotalRecall-58` and `TOOL-dTotalRecall-55` close.
`TOOL-dTotalRecall-53` S22 widens the alias census to `memory/builds/*/build/*.py` and keeps the
pinned departures instrument's compare,
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py:380`
(`if read_serves(text, fam_re)[0] != "journal":`, read at base `462d20f3`), with the reason
`pinned instrument`. S34 then makes that keep an in-file marker, and AC22 observes it. The file's
blob, `30a1f15b`, is one of the packet's instrument pins, which only the owner's
`packet.py --repin` moves, and the file sits outside this build's write set. Marking line 380 moves
a pinned blob; leaving it unmarked leaves the census with no disposition for it. This unit keeps
that hit by the path-keyed row `TOOL-dTotalRecall-55` mints. It repairs `TOOL-dTotalRecall-53`.

## 2. Scope (IN)

- **S1** — The alias census reads the table. `check_alias_compares` in
  `tools/memory-tree/record_kinds.py` keeps a hit in a file under `memory/builds/*/build/` only when
  `tree_lib.read_kept_path("check_alias_compares", path)` answers for it, and prints `kept <reason>`.
  Such a hit is red otherwise. Observed by AC1 and AC2.
- **S2** — The row. `CENSUS_KEPT_PATHS` gains
  `("check_alias_compares", "<the deviations.py path>", "pinned instrument")`. The ask S22 files in
  `memory/builds/dClosedLoop/BACKLOG.md`, asking the owner to compare through `canonical_kind` and
  repin, stands as written. Observed by AC1.

## 3. Non-goals (OUT)

- The table, its accessor and the cause census's rows: `TOOL-dTotalRecall-55`'s.
- The ask row and the widened alias population: `TOOL-dTotalRecall-53` S22's.
- The marker for a file under `tools/`: S34's.
- Editing `deviations.py` or moving its pin: the owner's.

### Edges

- **consumes-from** `TOOL-dTotalRecall-53` — S22's alias census over the build folders and its ask,
  and S34's marker, which cannot be written into this pinned file
- **consumes-from** `TOOL-dTotalRecall-55` — `CENSUS_KEPT_PATHS` and `read_kept_path`; without them the
  hit has no keep outside the file's bytes
- **consumes-from** `TOOL-dTotalRecall-61` — S2 as that unit amends it in step 19, so this pass moves the last row of `ALIAS_COMPARE_KEPT` into the table (the round-1 audit of units 54 to 60, id 1)
- **hands-off** `TOOL-dTotalRecall-65` — the alias row, which moves into that unit's registry (the round-1 audit of units 54 to 60, id 27)
- **hands-off** `TOOL-dTotalRecall-66` — AC1, AC3 and the alias row's drain, which that unit re-observes and adds (the round-1 audit of units 54 to 60, ids 11, 13, 24 and 41)
- **consumes-from** `TOOL-dTotalRecall-67` — S2, its added criterion and its hands-off to unit 57 as unit 61 amends them, read by their own text at step 20 and written there if absent (the round-1 audit of units 61 to 66, id 1)
- **consumes-from** `TOOL-dTotalRecall-72` — its hands-off mirror to unit 57, written by that unit at step 21 when unit 57's edge to this unit is absent (the round-1 audit of units 67 to 70, id 10)

## 4. Design

### The census read

`check_alias_compares` asks `read_kept_path` for any hit whose path matches `memory/builds/*/build/`
before it reports the hit red, exactly as `check_cause_writers` does after `TOOL-dTotalRecall-55`.
A hit under `tools/` is kept by S34's marker alone; the table is consulted only for the build
folders.

### Inventory

Minted: one row of `CENSUS_KEPT_PATHS`; the fixture plant `unkept-build-alias` in the record-kinds
fixture. Naming cell: none, no function being minted.

### Files touched (estimate)

- `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/tree_lib.py`

`TOOL-dTotalRecall-55`, `-57` and `-58` also write these modules at order 30, so BUILD-METHOD M6
sequences the passes; this one follows unit 55.

### Alternatives rejected

- **Keep `ALIAS_COMPARE_KEPT` for the one row.** It is a second file-keyed constant for the case unit
  55's table already holds.
- **Exclude the build folders from the alias census.** It drops the population S22 added for id 36,
  so a future build-folder compare against `journal` would pass unread.

## 5. Production-readiness checklist

- security — no new surface: a read-only census.
- perf / scale — one tuple lookup per build-folder hit.
- error / empty / loading states — an unkept build-folder compare is red and named.
- observability — the kept hit prints `pinned instrument`.
- risks — the row stands until the owner repins; S22's ask carries the change that drains it.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `check_alias_compares` from `record_kinds.py` runs at the pass tip, it lists
  `deviations.py:380` as `kept pinned instrument`, and `git grep -c "census: kept"` over that file
  prints `0`.
  Red when: the hit is red, or is kept by a marker written into the instrument.
- **AC2** — When the record-kinds fixture plants `unkept-build-alias`, a build-folder script that
  compares a `KIND_ALIASES` key raw with no row, `python record_kinds.py --check` run from
  `tools/memory-tree/` exits 1 naming that line.
  Red when: a build-folder hit with no row passes.
- **AC3** — When `git hash-object` runs on the deviations instrument at the pass tip, it prints
  `30a1f15bf67566aeaf5b7e1628483c630b23b416`, the packet's pin.
  Red when: the pass wrote into the pinned file.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/record_kinds.py · covers AC2 · the plant `unkept-build-alias`, staged by skipping the table read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-18`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, id 15
  (HIGH, item H1 shared with ids 4, 24 and 37).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-61, TOOL-dTotalRecall-65, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-67, the other end of an edge a unit the round-1 spec audit of units 61 to 66 promoted wrote; nothing else moved.
- rev-4 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-72, the other end of an edge a unit the round-1 spec audit of units 67 to 70 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is `check_alias_compares` (`TOOL-dTotalRecall-40` S2, widened by
`TOOL-dTotalRecall-53` S22), read through `TOOL-dTotalRecall-55`'s `read_kept_path`, the one table of
keeps outside a file's bytes. `python tools/codebase-map/reuse_lookup.py "keep a census hit in a file that cannot be edited"`
ranked name-stem neighbours (`hit`, `census`, `corpus_files`) and no path-keyed keep list, so the
table unit 55 mints is the seam and no other fits.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
