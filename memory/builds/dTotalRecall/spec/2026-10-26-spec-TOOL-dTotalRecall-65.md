# TOOL-dTotalRecall-65 — the census keep rows live in a project registry, so the memory-tree engine ships no path of this repository

**Status:** OPEN · rev-4 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 31 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 |
| [2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-66 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 54 to 60
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md`)
confirmed finding **id 27 at HIGH**, its item **H4**, alone in that item. `TOOL-dTotalRecall-55`
puts its keep table, `CENSUS_KEPT_PATHS`, in `tools/memory-tree/tree_lib.py`, with eight rows naming
build scripts that exist only in this repository, dClosedLoop's, aMendedFleet's and dDerivedDocket's,
and nine once `TOOL-dTotalRecall-56` adds the alias row for dClosedLoop's `deviations.py`. `tools/memory-tree/kit.toml` ships
`include = "**"` as role `engine` (`kit.toml:21-22`), so the file reaches every adopter, and unit 55
S4 reds a row whose file spells no Serves literal, which an absent file does not. An adopter running
`record_causes.py --check` therefore meets rows it cannot drain without editing gov's engine bytes,
and the literals break the rule `tree_lib.kit_rel()` states against hardcoded paths in shipped code
(`tree_lib.py:48-55`).

This unit moves the rows into a project registry under the memory root, the layer that already holds
this repository's own path lists, and leaves the engine reading it when present. It repairs
`TOOL-dTotalRecall-55`, at the step after it.

## 2. Scope (IN)

- **S1** — The registry. `memory/project/census-kept-paths.txt` holds one row per line,
  `<census>\t<path>\t<reason>`, `#` comments and blank lines skipped, with the rows units 55 and 56
  wrote, unchanged. `.memory-tree.conf` names it in `PROJECT_REGISTRY_EXTRA`, its comment block giving
  the member's reason. Observed by AC1 and AC2.
- **S2** — The reader. `read_kept_path(census, path, root)` in `tools/memory-tree/tree_lib.py` reads
  the registry at `<root>/<MEMORY_ROOT>/project/census-kept-paths.txt`, the memory root read from the
  conf, and answers `None` for every path when the file is absent. Its callers in
  `record_causes.py` and `record_kinds.py` pass their root. The domain rule `TOOL-dTotalRecall-57`
  set, `KEPT_PATH_DOMAIN`, and the drain unit 55 set run over the registry's rows as they ran over
  the table's. Observed by AC2 and AC3.
- **S3** — The engine table gives way. `CENSUS_KEPT_PATHS` leaves `tree_lib.py`, so the engine ships
  no row and no path of this repository. Observed by AC1.
  **Readers:** by name: READER NOT IN TREE — `CENSUS_KEPT_PATHS` is minted by `TOOL-dTotalRecall-55`
  in this build and is absent at base `462d20f3` · by value: `read_kept_path`, its one reader, which
  S2 points at the registry.

## 3. Non-goals (OUT)

- The rows' reasons, the drain test and the domain rule: units 55 and 57, re-keyed by the batch
  `TOOL-dTotalRecall-66`.
- `CAUSE_WRITER_PINNED`'s row: the batch `TOOL-dTotalRecall-66` folds it into this registry for id 23.
- A kit-shipped registry or a lint over engine files for build-folder literals: the close's
  left-shift step (BUILD-METHOD M8) takes the report's gate suggestion.

### Edges

- **consumes-from** `TOOL-dTotalRecall-55` — `CENSUS_KEPT_PATHS`, `read_kept_path` and the eight cause
  rows, which this unit moves into the registry
- **consumes-from** `TOOL-dTotalRecall-56` — the alias row, which moves with them
- **consumes-from** `TOOL-dTotalRecall-57` — `KEPT_PATH_DOMAIN`, the domain rule this unit keeps over
  the registry's rows
- **consumes-from** `TOOL-dTotalRecall-60` — the reasons its S26 grades per file, read from the
  registry after this unit
- **hands-off** `TOOL-dTotalRecall-66` — `census-kept-paths.txt` and `read_kept_path`'s root argument,
  over which that unit re-keys the drain and the domain
- **hands-off** `TOOL-dTotalRecall-68` — `census-kept-paths.txt`, its rows and `read_kept_path`, which that unit registers as a `[[ledger]]` population and re-points onto the factory's `read_rows` (the round-1 audit of units 61 to 66, id 16)
- **hands-off** `TOOL-dTotalRecall-69` — this unit's `.memory-tree.conf` edit, over which that unit re-stamps the kickoff manifest's `last-audit` (the round-1 audit of units 61 to 66, id 21)
- **hands-off** `TOOL-dTotalRecall-70` — the registry, its by-value carriers, the engine's literals and check 3's admission of the name, which that unit closes at the tip (the round-1 audit of units 61 to 66, ids 3, 4, 8, 13, 17, 18, 22, 24, 28, 29 and 30)
- **hands-off** `TOOL-dTotalRecall-76` — its plant `adopter-no-registry`, which that batch rewrites through the factory grammar (the round-1 audit of units 67 to 70, id 19)
- **hands-off** `TOOL-dTotalRecall-88` — its plant `adopter-no-registry`, which that batch keeps without a registry file and gives the tracked registration (the round-1 audit of units 71 to 76, ids 5, 25)

## 4. Design

### The registry

```text
# census-kept-paths.txt — a census hit kept by path, for a file no pass of this repository may edit.
check_cause_writers	memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py	pinned instrument
check_alias_compares	memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py	pinned instrument
# ... the remaining seven rows, as units 55 and 56 wrote them
```

The path is built as `transition_audit.resolve_registry` builds its own,
`root / memory_root / "project" / <name>` (`tools/memory-tree/transition_audit.py:759-760`), and the
row grammar follows `read_registry` there (`:763-774`): strip, skip `#` and blank, split. A missing
file is no rows, as that reader answers.

### Why the project layer

`memory/project/` holds this repository's own path lists, each named in `PROJECT_REGISTRY_EXTRA`
because the kit ships none of them (`.memory-tree.conf`, the comment above that key). An adopter
installing memory-tree receives the reader and no rows; one with build-folder scripts of its own
writes its own registry.

### Order inside step 31

Unit 60 also builds at order 31 and grades the rows' reasons, so this unit consumes it by a §3 edge
and BUILD-METHOD M6 sequences this pass after unit 60's.

### Inventory

Minted: `memory/project/census-kept-paths.txt`; the argument `root` of `read_kept_path`; the fixture
plant `adopter-no-registry` in `record_causes.py --fixture`. Naming cell: none, no function minted.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/record_kinds.py`
- `memory/project/census-kept-paths.txt` (new)
- `.memory-tree.conf`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **A `.memory-tree.conf` key holding the rows.** Nine tab-separated rows in one shell-sourced value is
  a grammar the conf readers do not share; a registry file has one already.
- **Ship the table empty and keep the gov rows in the engine on gov's tree only.** The engine bytes
  are the same file on both, so the rows would ship.

## 5. Production-readiness checklist

- security — no new write surface: a read of a tracked file under the memory root.
- perf / scale — one file read per census run, nine rows.
- error / empty / loading states — an absent registry is no rows; a malformed row (fewer than three
  fields) is a red finding naming its line.
- observability — each kept hit prints its row's reason, as before.
- risks — an adopter that had copied unit 55's table loses it; none exists, the table never left this
  run branch.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — the rows move one for one in the same commit.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `git grep -n CENSUS_KEPT_PATHS -- tools` and
  `git grep -nE "memory/builds/[A-Za-z]+/" -- tools/memory-tree/tree_lib.py` run at the pass tip, each
  prints nothing, and `grep -c census-kept-paths.txt .memory-tree.conf` prints at least 1.
  Red when: a row or a path of this repository stays in the engine, or the registry is unregistered.
- **AC2** — When `python record_causes.py --check` runs from `tools/memory-tree/` at the pass tip it
  lists the eight build-folder files kept with their rows' reasons, and `check_alias_compares` lists
  `deviations.py:380` kept `pinned instrument`.
  Red when: a row is lost in the move.
- **AC3** — When `python record_causes.py --fixture --plant adopter-no-registry` runs from
  `tools/memory-tree/` and builds a fixture with no `census-kept-paths.txt` and none of the nine files,
  `--check` names no kept row and no drained row.
  Red when: an engine-held row reaches an adopter.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC3 · the plant `adopter-no-registry`, staged by restoring an engine-held row naming an absent file · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 54 to 60, id 27
  (HIGH, item H4).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-68, TOOL-dTotalRecall-69, TOOL-dTotalRecall-70, each the other end of an edge a unit the round-1 spec audit of units 61 to 66 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-76, the other end of an edge a unit the round-1 spec audit of units 67 to 70 promoted wrote; nothing else moved.
- rev-4 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is the project-registry route: `resolve_registry` and `read_registry` in
`tools/memory-tree/transition_audit.py:759`, the one existing reader of a `memory/project/` path list
built from the memory root, and `PROJECT_REGISTRY_EXTRA`, the declared escape for a registry this
repository adds (`tools/memory-tree/check-memory-hygiene.sh:171`). `read_kept_path` keeps its role
and gains the root. `python tools/codebase-map/reuse_lookup.py "project registry of exempt paths read from the memory root"`
ranked `read`, `read_text` and `repo_root` by name stem and not the registry reader, which a read of
`transition_audit.py` found.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
