# TOOL-dTotalRecall-65 — the census keep rows live in a project registry, so the memory-tree engine ships no path of this repository

**Status:** INPROGRESS · rev-5 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 31 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-65-deviation-651.md](../build/2026-10-26-build-TOOL-dTotalRecall-65-deviation-651.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-65-deviation-652.md](../build/2026-10-26-build-TOOL-dTotalRecall-65-deviation-652.md) | deviation | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-65-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-65-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-65-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-65-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-65-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-65-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-66 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 54 to 60
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md`)
confirmed finding **id 27 at HIGH**, its item **H4**, alone in that item. `TOOL-dTotalRecall-55`
(`5b5895a49`) puts its keep table, `CENSUS_KEPT_PATHS`, in `tools/memory-tree/tree_lib.py`, and
`TOOL-dTotalRecall-56` (`798f98fc1`) adds the alias row. Every row names a build script that exists only
in this repository, dClosedLoop's, aMendedFleet's or dDerivedDocket's: eight cause rows and one alias
row (DERIVED 2026-11-24, `python -c "import tree_lib; print([r[0] for r in tree_lib.CENSUS_KEPT_PATHS])"`
from `tools/memory-tree/`). The kit ships `include = "**"` as role `engine`
(`tools/memory-tree/kit.toml@fa67a5614:30-31`), so the table reaches every adopter. An adopter carries
rows it can neither use nor drain without editing gov's engine bytes, and has no place of its own to
keep a build-folder script. The literals break the rule `tree_lib.py#kit_rel` states against hardcoded
paths in shipped code. The audit's red on an absent file does not stand as unit 55 built it: its drain
reds only a row whose file the walk reads (`record_causes.py#check_cause_writers`), so an absent file is
silent.

This unit moves the rows into a project registry under the memory root, the layer that already holds
this repository's own path lists, and leaves the engine reading it when present. It repairs
`TOOL-dTotalRecall-55`, at the step after it.

## 2. Scope (IN)

- **S1** — The registry. `memory/project/census-kept-paths.txt` holds one row per line,
  `<census>\t<path>\t<reason>`, `#` comments and blank lines skipped, with the rows
  `CENSUS_KEPT_PATHS` holds at the pass base, unchanged. `.memory-tree.conf` names it in
  `PROJECT_REGISTRY_EXTRA`, its comment block giving the member's reason. Hygiene check 3 admits it by
  that key alone: its `F:*` case is the last of its named `project/` cases and matches
  `PROJECT_REGISTRY_EXTRA` (`tools/memory-tree/check-memory-hygiene.sh@fa67a5614:1150-1160`).
  Observed by AC1 and AC2.
- **S2** — The reader. `read_kept_rows(census, root)` in `tools/memory-tree/tree_lib.py` reads the
  registry at `<root>/<MEMORY_ROOT>/project/census-kept-paths.txt`, the memory root read from the conf,
  and answers `{}` when the file is absent. `read_kept_path(census, path, root)` answers through it, as
  it answers through the table at HEAD. `check_cause_writers` in `record_causes.py` and
  `check_alias_compares` in `record_kinds.py` pass their root, and the `kept` argument leaves both and
  `record_causes.py#run_check`. The domain rule `TOOL-dTotalRecall-57` set, `KEPT_PATH_DOMAIN`, its
  refusal inside `read_kept_rows`, each census's catch of it, and the drain unit 55 set run over the
  registry's rows as they ran over the table's. Observed by AC2, AC3, AC4 and AC5.
- **S3** — The engine table gives way. `CENSUS_KEPT_PATHS` leaves `tree_lib.py`, so it ships no row and
  no path of this repository. Every finding, remedy, docstring and comment under `tools/` that named the
  table names the registry; the files are DERIVED 2026-11-24, `git grep -l CENSUS_KEPT_PATHS -- tools`.
  Observed by AC1.
  **Readers:** by name: `tools/memory-tree/tree_lib.py`, `tools/memory-tree/record_causes.py`,
  `tools/memory-tree/record_kinds.py`, `tools/memory-tree/check-memory-hygiene.test.sh` · by value:
  `read_kept_rows`, its one reader, which S2 points at the registry.
- **S4** — The planted rows. `kept-row-drained` (unit 55) and `kept-row-editable` (unit 57) write their
  one row into the fixture's own `census-kept-paths.txt`, since no `kept` argument is left to carry it,
  and their two arms in `tools/memory-tree/check-memory-hygiene.test.sh` hit the registry's name. Each
  keeps its exit 1 and its one red. Observed by AC4.

## 3. Non-goals (OUT)

- The rows' reasons, the drain test and the domain rule: units 55 and 57, re-keyed by the batch
  `TOOL-dTotalRecall-66`.
- `CAUSE_WRITER_PINNED`'s row and the `CLOSED_LOOP` prefix it is spelled with
  (`record_causes.py#CAUSE_WRITER_PINNED`), the one path of this repository the cause census still
  ships: the batch `TOOL-dTotalRecall-66` folds it into this registry for id 23.
- The refusal of a census marker in a build folder: `TOOL-dTotalRecall-58`'s `check_marker_domain`,
  which reads no row.
- A `[[ledger]]` registration: `TOOL-dTotalRecall-68`'s. No rule at HEAD reds a registry under
  `memory/project/` that no table registers: `tools/memory-tree/ratchet.py` reads registrations only.
- Check 3's admission by name and the kit README's paragraph: `TOOL-dTotalRecall-70` S12's. The re-stamp
  of the kickoff manifest, whose `watch:` line lists `.memory-tree.conf`: `TOOL-dTotalRecall-69`'s.
- A kit-shipped registry or a lint over engine files for build-folder literals: the close's
  left-shift step (BUILD-METHOD M8) takes the report's gate suggestion.

### Edges

- **consumes-from** `TOOL-dTotalRecall-55` — `CENSUS_KEPT_PATHS`, its one reader `read_kept_rows`,
  `read_kept_path` and the cause rows, which this unit moves into the registry
- **consumes-from** `TOOL-dTotalRecall-56` — the alias row, which moves with them
- **consumes-from** `TOOL-dTotalRecall-57` — `KEPT_PATH_DOMAIN`, the domain rule this unit keeps over
  the registry's rows, and the plant `kept-row-editable`, which it re-points
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
# ... the remaining rows, as units 55 and 56 wrote them, each `#` note above a row moving with it
```

### The reader

```python
CENSUS_KEPT_REGISTRY = "census-kept-paths.txt"

def read_kept_rows(census, root) -> dict:
    from design_lib import read_design_conf   # at call time: design_lib imports this module
    m = (read_design_conf(root).get("MEMORY_ROOT") or "memory").strip().strip("/") or "memory"
    path = pathlib.Path(root, m, "project", CENSUS_KEPT_REGISTRY)
    ...   # absent: {}; a row of fewer than three TAB fields: ValueError naming the registry and its line
    ...   # unit 57's domain refusal over every row, naming the registry; then {path: reason} for `census`

def read_kept_path(census, path, root):
    return read_kept_rows(census, root).get(path)
```

The path is built as `transition_audit.py#resolve_registry` builds its own, and the row grammar follows
`transition_audit.py#read_registry`: strip, skip `#` and blank, split, here on TAB, at most twice, so a
reason keeps its spaces. The text is read through `tree_lib.py#read_text`. The memory root comes from
the reader both censuses already take it from (`record_causes.py#read_conf`,
`record_kinds.py#read_memory_root`), so the registry sits under the root the walks read. The file is
read from the working tree, tracked or not, as `read_registry` reads its own.

Each census keeps unit 57's shape: it calls `read_kept_rows` once before its build-folder walk and
appends a `ValueError` to its reds. At HEAD it then empties its `kept` table. With no table to empty, it
holds the refusal in a local flag: the walk asks `read_kept_path(census, path, root)` only where the
rows were admitted, and the drain loop of `check_cause_writers` runs over the mapping the first call
returned, `{}` after a refusal. So every hit still reads unkept and the run still exits 1. A malformed
row takes the same path as a row outside the domain.

Where unit 58's or unit 60's pass changes these two walks before this one, the builder re-derives the
readers with S3's command and keeps their edits.

### Why the project layer

`memory/project/` holds this repository's own path lists, each named in `PROJECT_REGISTRY_EXTRA`
because the kit ships none of them (`.memory-tree.conf`, the comment above that key). An adopter
installing memory-tree receives the reader and no rows; one with build-folder scripts of its own
writes its own registry.

### Order inside step 31

Unit 60 also builds at order 31 and grades the rows' reasons, so this unit consumes it by a §3 edge
and BUILD-METHOD M6 sequences this pass after unit 60's.

### What it does not check

That a registered file exists or is tracked, and that a pair is unique: units 66 and 70 add those. That
the registry's absence is meant: in this repository an absent file reds every hit its rows kept.

### Inventory

Minted: `memory/project/census-kept-paths.txt`; the constant `CENSUS_KEPT_REGISTRY` in `tree_lib.py`; the
argument `root` of `read_kept_rows` and of `read_kept_path`, replacing `table`; the fixture plant
`adopter-no-registry` in `record_causes.py --fixture`. Retired: `CENSUS_KEPT_PATHS`, the `kept` argument
of `check_cause_writers`, `run_check` and `check_alias_compares`, and `FIXTURE_KEPT`'s tuple form. Naming
cell: none, no function minted.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/project/census-kept-paths.txt` (new)
- `.memory-tree.conf`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **A `.memory-tree.conf` key holding the rows.** Tab-separated rows in one shell-sourced value are
  a grammar the conf readers do not share; a registry file has one already.
- **Ship the table empty and keep the gov rows in the engine on gov's tree only.** The engine bytes
  are the same file on both, so the rows would ship.
- **Keep the `kept` argument, None reading the registry.** Its only passers are plants, and a fixture
  repository holds a registry file as this one does, so the plants read through the reader they grade.

## 5. Production-readiness checklist

- security — no new write surface: a read of a tracked file under the memory root.
- perf / scale — a small file read once per walk and once per build-folder hit.
- error / empty / loading states — an absent registry is no rows; a malformed row (fewer than three
  fields) is a red finding naming its line, and the walk reads every hit unkept.
- observability — each kept hit prints its row's reason, as before; a red names the registry.
- risks — an adopter that had copied unit 55's table loses it; none exists, the table never left this
  run branch. The `kickoff-manifest ratchet` leg is red from this pass to unit 69's re-stamp, by that
  unit's §1.
- testing — AC1 to AC5 by the pass; the arms of §7 at the close.
- migration — the rows move one for one in the same commit.
- user docs — none under `help/`; the kit README's paragraph is unit 70's.

## 6. Acceptance criteria

- **AC1** — When `git grep -n CENSUS_KEPT_PATHS -- tools` and
  `git grep -nE "memory/builds/(dClosedLoop|aMendedFleet|dDerivedDocket)/" -- tools/memory-tree/tree_lib.py`
  run at the pass tip, each prints nothing, and
  `grep -c '^PROJECT_REGISTRY_EXTRA=.*census-kept-paths' .memory-tree.conf` prints `1`.
  Red when: a row, a path of this repository or a message naming the table stays in the engine, or the
  registry is unregistered.
  figure: the module's fixture paths under `memory/builds/tOne/` are no path of this repository, so
  the pattern names the three slugs the rows name (DERIVED 2026-11-24, §1's table).
- **AC2** — When `python record_causes.py --cause-writers` runs from `tools/memory-tree/` at the pass
  tip it lists the same build-folder files `kept`, each with the same reason, as at the pass base, and
  its `code files under memory/builds/*/build` line reads `0 red`; `python record_kinds.py --check`
  there lists `deviations.py:380` `kept pinned instrument`. `grep -c '^check_' census-kept-paths.txt`
  from `memory/project/` prints the row count §1's command gives at the pass base.
  Red when: a row is lost or reworded in the move.
  figure: DERIVED 2026-11-24 at `fa67a5614`: `8 kept · 1 pinned · 0 red` and nine rows. The second
  command may exit 1 for a stray entry of the host's common git dir, so its line is read, not its exit.
- **AC3** — When `python record_causes.py --fixture --plant adopter-no-registry` runs from
  `tools/memory-tree/`, its fixture holds no `census-kept-paths.txt`, its `--check` exits 0 and names no
  kept or drained row, `read_kept_rows` answers `{}` there for both censuses, and the run prints one
  `fixture adopter-no-registry · PASS` line and exits 0.
  Red when: an engine-held row reaches an adopter, which prints `FAIL` and exits 1.
- **AC4** — When `python record_causes.py --fixture --plant kept-row-drained` and
  `--plant kept-row-editable` run from `tools/memory-tree/`, each exits 1 with exactly one
  `record causes: RED ` line, naming `census-kept-paths.txt` and the planted row's path.
  Red when: the drain or the domain rule reads no registry row, or a finding names no registry.
- **AC5** — When a `python -c` probe from `tools/memory-tree/` writes a `tempfile.TemporaryDirectory()`
  tree whose `census-kept-paths.txt` under `memory/project/` holds a comment line and then a row of two
  TAB fields, and calls `tree_lib.read_kept_rows("check_cause_writers", <the tree>)`, it raises
  `ValueError` naming `census-kept-paths.txt` and `line 2`.
  Red when: a malformed row is skipped or read as a keep.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `record-kinds` · `record causes (causes and orphans over the legacy population)` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC3 · the plant `adopter-no-registry`, its PASS line and exit 0, staged by returning one engine-held row beside the registry's, which exits the plant 1 · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC4 · the moved arms of `kept-row-drained` and `kept-row-editable`, their rows in the fixture's registry, staged by skipping the drain test and the domain match, which exits each plant 0 · none

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
- rev-5 · 2026-11-24 · §1 S1 S2 S3 S4 §3 §4 §5 AC1 AC2 AC3 AC4 AC5 §7 §10 · re-grounded at HEAD `fa67a5614` per
  `2026-11-24-prompt-TOOL-dTotalRecall-65-reground-spec-writer`: the reader as built is
  `read_kept_rows(census, table)`, so `root` replaces `table` in it and in `read_kept_path`, and the
  `kept` arguments of units 55 and 57 leave; the absent-file red of §1 does not hold as unit 55 built its
  drain; S4 and AC4 re-point the two plants and their arms, so `check-memory-hygiene.test.sh` joins Files
  touched; AC1's path pattern matched the module's fixtures and is narrowed; AC3 tells an engine-held
  row apart by the rows the reader answers; AC5 observes the malformed row; §7 names the legs that run
  both censuses and the suite holding the arms; citations are re-derived.

## 10. Reuse audit

The seam extended is `read_kept_rows`, the keep rows' one reader (`TOOL-dTotalRecall-55` S1), pointed at
the project-registry route: `transition_audit.py#resolve_registry` and `transition_audit.py#read_registry`,
whose shape it takes, and `PROJECT_REGISTRY_EXTRA`, the declared escape for a registry this repository
adds (`tools/memory-tree/check-memory-hygiene.sh@fa67a5614:188`). The ledger factory's `read_rows` reads
a row grammar of its own, with a count and a SHA, and `TOOL-dTotalRecall-68` moves this registry onto it. `python tools/codebase-map/reuse_lookup.py "project registry of exempt paths read from the memory root"`
ranked `read_text`, `read` and `repo_root` by name stem and not the registry reader, which a read of
`transition_audit.py` found.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
