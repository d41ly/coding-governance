# TOOL-dTotalRecall-57 — a path-keyed keep row is admitted only for a file no pass may edit, so every editable file is kept by the one marker

**Status:** DEFERRED · rev-6 · 2026-11-23 · node d · Tier-2 · base 462d20f3 · streams tooling · order 30 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-57-deviation-571.md](../build/2026-10-26-build-TOOL-dTotalRecall-57-deviation-571.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-57-deviation-572.md](../build/2026-10-26-build-TOOL-dTotalRecall-57-deviation-572.md) | deviation | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-57-reground-brief.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-57-reground-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-57-reground-spec-writer.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-57-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-54 TOOL-dTotalRecall-59 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-58 TOOL-dTotalRecall-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
confirmed finding **id 4 at HIGH**. It shares item **H1** with ids 15, 24 and 37, which
`TOOL-dTotalRecall-56`, `TOOL-dTotalRecall-58` and `TOOL-dTotalRecall-55` close.
`TOOL-dTotalRecall-53` S34, built at `6db81d070`, makes one in-file marker,
`<lead> census: kept <census> <reason>` read by `id_grammar.py#read_kept_reason`, the keep for the
three code censuses under the tool root. A build-folder script cannot carry it: the pinned
instruments among them would move their blob, and all of them sit outside this build's write set. So
unit 53 left their rows in `record_causes.py#CAUSE_WRITER_KEPT` and
`record_kinds.py#ALIAS_COMPARE_KEPT`, and its AC34 reads every remaining row as a file under
`memory/builds/*/build/`. `TOOL-dTotalRecall-55` and `TOOL-dTotalRecall-56` move those rows to one
path-keyed table outside the files' bytes and end both constants. A path-keyed row is the very
exemption S34 retired under the tool root, though, and with no bound on the table any file could be
kept by a row again. This unit bounds the table to the files the marker cannot reach and re-observes
AC34 under that carve-out. It repairs `TOOL-dTotalRecall-53`.

## 2. Scope (IN)

- **S1** — The domain rule. `read_kept_rows` in `tools/memory-tree/tree_lib.py`, the table's one
  reader (`TOOL-dTotalRecall-55` S1, which `read_kept_path` reads through), raises `ValueError` for
  any row of the table it reads whose path does not match `KEPT_PATH_DOMAIN`,
  `memory/builds/*/build/*`, the files the README's write rule (README:49) and the packet's non-goals
  put outside every pass of this build. `check_cause_writers` (`tools/memory-tree/record_causes.py`)
  and `check_alias_compares` (`tools/memory-tree/record_kinds.py`) each call it once, before their
  build-folder walk, whatever hits that walk finds. On the refusal a census appends it to its reds,
  naming the row and the remedy `mark the kept line # census: kept <census> <reason>`, and walks on
  with an empty table, so every build-folder hit it finds reads unkept. So `--check` exits 1 with a
  finding, never 2 as a refusal (`record_causes.py#run_check` maps a `ValueError` out of the census
  to exit 2) nor a traceback (`record_kinds.py#check_record_kinds` catches no `ValueError` around the
  alias census). Observed by AC1 and AC3.
- **S2** — AC34 under the carve-out. At the tip no constant named `ALIAS_COMPARE_KEPT` or
  `CAUSE_WRITER_KEPT` exists under `tools`, and every row of `CENSUS_KEPT_PATHS` names a file under
  `memory/builds/*/build/`. So a file under `tools/` is kept by S34's marker only. Unit 53 already
  narrowed both constants to build-folder rows, and units 55 and 56 end them, so S2 writes nothing:
  it is an observation, AC2 kept as its check. Observed by AC2.
- **S3** — The planted row. `check_alias_compares` takes `kept`, defaulting to
  `tree_lib.CENSUS_KEPT_PATHS`, and passes it to the reader as `table`; its local count `kept` takes
  another name. `TOOL-dTotalRecall-55` S2 already threads `kept` through `check_cause_writers` and
  `run_check`, the way both take `pinned` (`record_causes.py#run_check`,
  `record_causes.py#check_pinned_plant`), so on that side S3 is an observation. A fixture or probe
  plants a row without writing the module. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- The table and its eight cause rows: `TOOL-dTotalRecall-55`'s; the alias row: `TOOL-dTotalRecall-56`'s.
- A marker written into a build-folder file: `TOOL-dTotalRecall-58`'s refusal.
- `CAUSE_WRITER_PINNED`, unit 50's draining row, whose ask the batch `TOOL-dTotalRecall-60` resolves
  for id 25.

### Edges

- **consumes-from** `TOOL-dTotalRecall-55` — `CENSUS_KEPT_PATHS` and its one reader `read_kept_rows`,
  with the `kept` argument of `check_cause_writers` and `run_check`, whose rows this unit bounds
- **consumes-from** `TOOL-dTotalRecall-53` — S34's marker as built, `id_grammar.py#read_kept_reason`, and AC34's narrowing of both constants to build-folder rows, which this unit re-observes under the carve-out
- **consumes-from** `TOOL-dTotalRecall-56` — S2's end of `ALIAS_COMPARE_KEPT`, since AC2 reads both constants gone (the round-1 audit of units 54 to 60, id 1)
- **consumes-from** `TOOL-dTotalRecall-61` — the edge to unit 56 that unit writes in step 19, since AC2 reads both constants gone (the round-1 audit of units 54 to 60, id 1)
- **hands-off** `TOOL-dTotalRecall-65` — `KEPT_PATH_DOMAIN`, which that unit keeps over its registry's rows (the round-1 audit of units 54 to 60, id 27)
- **hands-off** `TOOL-dTotalRecall-66` — `KEPT_PATH_DOMAIN` and its refusal, which that unit derives from the memory root, anchors by segment and reports in the alias census (the round-1 audit of units 54 to 60, ids 5, 8, 14, 18, 29 and 42)
- **consumes-from** `TOOL-dTotalRecall-67` — its edge to unit 56 and its sequencing line as unit 61 amends them, read by their own text at step 20 and written there if absent (the round-1 audit of units 61 to 66, id 1)
- **consumes-from** `TOOL-dTotalRecall-72` — its consumes-from edge to unit 56, read by that unit at step 21 by a probe no shell quotes and written there if absent (the round-1 audit of units 67 to 70, id 10)

## 4. Design

### The rule

```python
KEPT_PATH_DOMAIN = "memory/builds/*/build/*"

def read_kept_rows(census, table=CENSUS_KEPT_PATHS) -> dict:
    for _c, p, _reason in table:
        if not fnmatch.fnmatchcase(p, KEPT_PATH_DOMAIN):
            raise ValueError(f"CENSUS_KEPT_PATHS row {p}: an editable file is kept by "
                             "marking its line `# census: kept <census> <reason>`")
    ...   # unit 55's body: the census's rows as {path: reason}
```

The whole table is read on every call, whatever census asked, so a bad row is refused by both. Each
census asks once, before its build-folder walk:

```python
try:
    tree_lib.read_kept_rows("check_alias_compares", kept)
except ValueError as exc:
    reds.append(f"alias-compare {exc}")
    kept = ()
```

`check_cause_writers` does the same under its own census name and head. `tree_lib.py` imports
`fnmatch` for the rule. What it does not check: whether a build-folder row's file exists, is tracked
or is pinned (unit 55 S4 and unit 66 drain such rows); a row in the domain filed under the wrong
census; and whether the README's write rule still names the build folders (unit 66 derives the
domain from the memory root).

### Inventory

Minted: `KEPT_PATH_DOMAIN` in `tools/memory-tree/tree_lib.py`; the `kept` argument of
`check_alias_compares`; the fixture plant `kept-row-editable` in `record_causes.py`, whose table is
one `check_cause_writers` row naming a Python file in the `planted` folder under the fixture's tool
root, passed to `run_check` as `kept`. Naming cell: none, no function being minted.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/record_kinds.py`

`TOOL-dTotalRecall-55`, `-56` and `-58` also write these modules at order 30, so BUILD-METHOD M6
sequences the passes; this one follows units 55 and 56.

### Alternatives rejected

- **Bound the rows by a list of pinned instruments.** Five of the eight cause files are unpinned
  (`record_causes.py#CAUSE_WRITER_KEPT` keys them `outside the write set`) and still outside this
  build's write set; the folder glob is the rule the README states.
- **Leave the table unbounded.** A row would again keep an editable file without a marker, the
  two-grammar state S34 removed.
- **Let the refusal leave the census.** `run_check` turns it into exit 2, a refused run naming no
  finding, and the alias census would raise through `check_record_kinds`.
- **Refuse only in `read_kept_path`, per hit.** A bad row would go unread in a walk that finds no
  build-folder hit, and would red once per hit where it is read.
- **Rebind `tree_lib.CENSUS_KEPT_PATHS` in the fixture.** The plant would share state with the table
  it guards; a passed table is the shape `pinned` already has.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one glob match per row per call; the table holds nine rows (DERIVED: the eight
  `CAUSE_WRITER_KEPT` rows and the one `ALIAS_COMPARE_KEPT` row at HEAD `69d8787a3`).
- error / empty / loading states — a row outside the domain is a red finding naming it; an empty
  table fails AC2's probe rather than passing it.
- observability — the finding prints the row's path and the remedy.
- risks — an adopter's own build-folder scripts are admitted by the same glob, which is the folder
  shape the memory tree declares for every build.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python record_causes.py --fixture --plant kept-row-editable` runs from
  `tools/memory-tree/`, its `--check` reading a table whose one row names a Python file in the
  `planted` folder under the fixture's tool root, it exits 1 and prints one `RED` line naming that row's path and
  `census: kept`.
  Red when: a row naming an editable file is read as a keep, or the refusal exits 2 or raises.
- **AC2** — When `git grep -nE "ALIAS_COMPARE_KEPT|CAUSE_WRITER_KEPT" -- tools` runs at the pass tip it
  prints nothing, and `python -c "import fnmatch, tree_lib as t; bad = [p for _, p, _ in t.CENSUS_KEPT_PATHS if not fnmatch.fnmatchcase(p, 'memory/builds/*/build/*')]; print(bad); raise SystemExit(bool(bad) or not t.CENSUS_KEPT_PATHS)"`
  run from `tools/memory-tree/` prints `[]` and exits 0. The glob is spelled, never read from
  `KEPT_PATH_DOMAIN`, so the probe shares no state with the rule.
  Red when: either retired constant survives, a row names a file outside the build folders, or the
  table is empty.
- **AC3** — When `python -c "import record_kinds as rk, tree_lib as t; from id_grammar import repo_root; _, reds = rk.check_alias_compares(repo_root(), rk.derive_tool_rel(rk.derive_kit_rel()), kept=t.CENSUS_KEPT_PATHS + (('check_alias_compares', 'tools/memory-tree/tree_lib.py', 'x'),)); print(len([r for r in reds if 'tools/memory-tree/tree_lib.py' in r and 'census: kept' in r]))"`
  runs from `tools/memory-tree/` at the pass tip, it prints `1`.
  Red when: the alias census honours, skips or raises on a row naming an editable file.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `record-kinds` · `record causes (causes and orphans over the legacy population)` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 · the plant `kept-row-editable` of `record_causes.py --fixture --plant <case>`, staged by skipping the domain match · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, id 4
  (HIGH, item H1 shared with ids 15, 24 and 37).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-61, TOOL-dTotalRecall-65, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-67, the other end of an edge a unit the round-1 spec audit of units 61 to 66 promoted wrote; nothing else moved.
- rev-4 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-72, the other end of an edge a unit the round-1 spec audit of units 67 to 70 promoted wrote; nothing else moved.
- rev-5 · 2026-11-23 · §3 §4 · amended by TOOL-dTotalRecall-61 (id 1, item H1) per
  `2026-11-22-prompt-TOOL-dTotalRecall-61-build-spec-writer`: §3 gains the consumes-from edge to unit 56,
  whose pass ends `ALIAS_COMPARE_KEPT` that AC2 reads gone, and §4's sequencing line follows units 55
  and 56.
- rev-6 · 2026-11-23 · §1 S1 S2 S3 §3 §4 §5 AC1 AC2 AC3 §7 §10 · re-grounded at HEAD `69d8787a3` per
  `2026-11-23-prompt-TOOL-dTotalRecall-57-reground-spec-writer`: the remedy spells unit 53's marker as
  built; README:50 is README:49; the rule sits in unit 55's one reader `read_kept_rows`, asked once per
  census before its build-folder walk, and each census catches it (a `ValueError` is exit 2 in
  `run_check` and uncaught in the alias census), so `record_kinds.py` joins Files touched and AC3 observes
  the alias side; S2 is an observation, unit 53 having narrowed both constants; S3 gives
  `check_alias_compares` the `kept` argument unit 55 threads through the cause census; AC2's probe is
  spelled; the arm names its suite and §7 the legs that run it and both censuses.

## 10. Reuse audit

The seam extended is `read_kept_rows` (`TOOL-dTotalRecall-55` S1), the one reader of the keep table,
which `read_kept_path` reads through, so the bound lives once and both censuses inherit it; the
planted table rides the `kept` argument unit 55 threads beside `pinned` (`record_causes.py#run_check`). `python tools/codebase-map/reuse_lookup.py "bound a path-keyed keep table to the files a census marker cannot reach"`
ranked name-stem neighbours (`key`, `census`, `write_fixture_files`) and no existing bound on an
exemption list; no existing seam fits for the domain rule beyond the accessor it sits in.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
