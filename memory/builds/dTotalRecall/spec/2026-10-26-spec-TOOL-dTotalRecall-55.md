# TOOL-dTotalRecall-55 — the cause census keeps the build folders' scripts by a path-keyed row held outside their bytes

**Status:** CLOSED · rev-5 · 2026-11-23 · node d · Tier-2 · base 462d20f3 · streams tooling · order 30 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-55-deviation-551.md](../build/2026-10-26-build-TOOL-dTotalRecall-55-deviation-551.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-55-deviation-552.md](../build/2026-10-26-build-TOOL-dTotalRecall-55-deviation-552.md) | deviation | — |
| [2026-11-23-build-TOOL-dTotalRecall-55-1-acceptance-ledger.md](../build/2026-11-23-build-TOOL-dTotalRecall-55-1-acceptance-ledger.md) | log | — |
| [2026-11-23-build-TOOL-dTotalRecall-55-1-builder-return.md](../build/2026-11-23-build-TOOL-dTotalRecall-55-1-builder-return.md) | journal | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-55-build-brief.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-55-build-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-55-reground-brief.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-55-reground-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-55-reground-spec-writer.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-55-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-54 TOOL-dTotalRecall-59 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-60 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 44 to 53
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md`)
confirmed finding **id 37 at HIGH**. It shares item **H1** with ids 4, 15 and 24, which
`TOOL-dTotalRecall-57`, `TOOL-dTotalRecall-56` and `TOOL-dTotalRecall-58` close.
`TOOL-dTotalRecall-53` S34, as built at `6db81d070`, keeps a hit under the tool root by one marker on
its line, `<lead> census: kept <census> <reason>`, read by `tools/memory-tree/id_grammar.py#read_kept_reason`.
It narrowed `tools/memory-tree/record_causes.py#CAUSE_WRITER_KEPT` to the build folders' scripts,
and `TOOL-dTotalRecall-61` amended its AC34 so those rows stand until this pass. At HEAD `69d8787a3`
the constant holds eight rows, and the census's build-folder count line reads
`9 census file(s) · 8 kept · 1 pinned · 0 red` (DERIVED: `python record_causes.py --cause-writers`
from `tools/memory-tree/`). The eight are dClosedLoop's `asbuilt.py`, `packet.py`, `walk.py`,
`fold-inventory.py` and `walk-seed.py`, aMendedFleet's `harness.py` and `ab.py`, and dDerivedDocket's
`signer.py`; the ninth census file, dClosedLoop's `deviations.py`, is `CAUSE_WRITER_PINNED`'s. None
of the eight can take a marker. `asbuilt.py` and `packet.py` are pinned instruments
(`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py#INSTRUMENTS`), and a
moved instrument blob is a stop (`memory/builds/dTotalRecall/README.md@69d8787a3:37`). All eight sit
outside the write set the README gives this build (`memory/builds/dTotalRecall/README.md@69d8787a3:49`),
and `TOOL-dTotalRecall-58` refuses the marker in a build-folder file. This unit declares their keep
outside their bytes, in one path-keyed table the censuses read, and ends `CAUSE_WRITER_KEPT`. It
repairs `TOOL-dTotalRecall-53`.

## 2. Scope (IN)

- **S1** — The table. `CENSUS_KEPT_PATHS` in `tools/memory-tree/tree_lib.py` holds one row per
  census and file as `(census, path, reason)`. The census is named by its function,
  `check_cause_writers` or `check_alias_compares`. The path is one tracked file, and the reason is
  printed beside the hit. `read_kept_rows(census, table=CENSUS_KEPT_PATHS)` in the same module
  returns the census's rows as `{path: reason}` and is the table's one reader; `read_kept_path(census,
  path, table=CENSUS_KEPT_PATHS)` returns one row's reason or `None` through it (§8 F2). Observed by
  AC1.
- **S2** — The cause census reads it. `check_cause_writers` in `tools/memory-tree/record_causes.py`
  takes `kept`, defaulting to `tree_lib.CENSUS_KEPT_PATHS`, and `run_check` threads it, as both take
  `pinned` today. A census file under `memory/builds/*/build/` is kept only when `read_kept_path`
  answers for it, printed `kept <reason>`, and is red otherwise, its remedy naming
  `CENSUS_KEPT_PATHS`. The departures instrument stays under `CAUSE_WRITER_PINNED`
  (`TOOL-dTotalRecall-50` S2) and takes no row here. The eight rows move out of `CAUSE_WRITER_KEPT`,
  its last after unit 53, so the constant ends at this pass, with `KEPT_PINNED` and `KEPT_OUTSIDE`,
  which only its rows read (`git grep -n "KEPT_PINNED\|KEPT_OUTSIDE" -- tools` at `69d8787a3`), and
  every docstring and remedy line naming it. Observed by AC1.
- **S3** — The eight rows. `asbuilt.py` and `packet.py` carry the reason `pinned instrument`, being
  in the packet's `INSTRUMENTS`. The other six carry `outside the write set`. Each row is written
  from the census's output at the pass base, whose reasons `CAUSE_WRITER_KEPT` holds today, and the
  pass commit's `Decided:` trailer names the eight. Observed by AC1.
- **S4** — A row cannot outlive its hit. A `check_cause_writers` row of `kept` whose file the
  build-folder walk reads (`record_causes.py#read_build_code_paths`) and which spells no
  `**Serves:** ` literal past its `tree_lib.BIND_HEAD_LINES` binding window is red, named
  `CENSUS_KEPT_PATHS` and its path, so the table drains as the owners add cause lines. Observed by
  AC2.

## 3. Non-goals (OUT)

- The marker and its reader for files under `tools/`: `TOOL-dTotalRecall-53` S34's.
- The alias census's row for `deviations.py`: `TOOL-dTotalRecall-56`'s.
- Refusing a row that names an editable file: `TOOL-dTotalRecall-57`'s.
- Refusing a marker written into a build-folder file: `TOOL-dTotalRecall-58`'s.
- A row whose file is untracked or gains a `Caused-by` line: `TOOL-dTotalRecall-66` S1 keys the drain
  on those.
- A row's falsity test against the records its file writes, and `CAUSE_WRITER_PINNED`'s ask
  resolution: the batch `TOOL-dTotalRecall-60` holds those for ids 44 and 25.
- Editing any build-folder script, or filing an ask for its cause line.

### Edges

- **consumes-from** `TOOL-dTotalRecall-53` — S34's marker, which leaves `CAUSE_WRITER_KEPT` holding only
  the build-folder rows this unit moves
- **consumes-from** `TOOL-dTotalRecall-50` — the census widened to the build folders' `*.py`, `*.sh`
  and `*.js` files (`record_causes.py#read_build_code_paths`) and `CAUSE_WRITER_PINNED`, whose eight
  other hits this unit disposes
- **hands-off** `TOOL-dTotalRecall-56` — `CENSUS_KEPT_PATHS` and `read_kept_path`, which the alias
  census reads for its build-folder hit
- **hands-off** `TOOL-dTotalRecall-57` — `CENSUS_KEPT_PATHS` and its one reader `read_kept_rows`, whose
  rows that unit holds to files no pass may edit
- **hands-off** `TOOL-dTotalRecall-60` — the table's rows and reasons, which that unit keys to the
  records each file writes (id 44) and beside which it resolves the pinned row's ask (id 25)
- **consumes-from** `TOOL-dTotalRecall-61` — S2 as that unit amends it in step 19, so this pass moves the last rows of `CAUSE_WRITER_KEPT` into the table (the round-1 audit of units 54 to 60, id 1)
- **hands-off** `TOOL-dTotalRecall-65` — `CENSUS_KEPT_PATHS` and `read_kept_path`, whose rows that unit moves into a project registry (the round-1 audit of units 54 to 60, id 27)
- **hands-off** `TOOL-dTotalRecall-66` — S4's drain, which that unit keys on the census's own hit (the round-1 audit of units 54 to 60, ids 4 and 40)
- **consumes-from** `TOOL-dTotalRecall-67` — S2 and AC1 as unit 61 amends them, read by their own text at step 20 and written there if unit 61's pass left them out (the round-1 audit of units 61 to 66, id 1)

## 4. Design

### The table

```python
CENSUS_KEPT_PATHS = (
    ("check_cause_writers", "memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py",
     "pinned instrument"),
    ("check_cause_writers", "memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py",
     "pinned instrument"),
    ("check_cause_writers", "memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-walk.py",
     "outside the write set"),
    # ... fold-inventory.py, walk-seed.py, the two aMendedFleet scripts and dDerivedDocket's signer.py
)


def read_kept_rows(census, table=CENSUS_KEPT_PATHS) -> dict:
    """`{path: reason}`: the rows of `table` naming `census`; the table's one reader."""
    return {path: reason for c, path, reason in table if c == census}


def read_kept_path(census, path, table=CENSUS_KEPT_PATHS):
    """The reason `table` keeps `path` by for `census`, or None."""
    return read_kept_rows(census, table).get(path)
```

The table lives in `tree_lib.py` because both censuses already import it: `record_causes.py` the
module whole (`import tree_lib`, for `tools/memory-tree/tree_lib.py#BIND_HEAD_LINES` and
`tree_lib.py#read_header_edges`), and `record_kinds.py#check_alias_compares` its `BIND_HEAD_LINES`.
Unit 53's marker reader keys by line in `id_grammar.py`; this table keys by path, for the files no
marker may enter. One table and one reader give the two censuses one keep grammar for a file they
may not edit, beside S34's one marker for a file they may.

### The census

`check_cause_writers`'s build-folder loop (`record_causes.py#check_cause_writers`) keeps today's
order: a `pinned` instrument first, then `read_kept_path("check_cause_writers", path, kept)` in the
place of the `CAUSE_WRITER_KEPT` lookup, then red. After the loop, each path of
`read_kept_rows("check_cause_writers", kept)` that `read_build_code_paths` lists and that spells no
Serves literal past its window prints `cause-writer · kept row · <path> · red · drained` and adds
the red `cause-writer CENSUS_KEPT_PATHS <path>: spells no Serves line past its binding window, so
the row keeps nothing; drain the row`. The build-folder count line keeps its shape.

### The fixture

`FIXTURE_KEPT` holds one `check_cause_writers` row naming `KEPT_SCRIPT`,
`memory/builds/fRoot/build/2026-01-01-build-TOOL-fRoot-1-kept.py`, a one-line docstring with no
Serves literal. `run_fixture` passes `FIXTURE_KEPT` to `run_check` for the plant `kept-row-drained`;
every other plant reads the default table, whose rows name files no fixture tracks, so S4 reads
none of them. The plant joins `PLANTS`.

### Inventory

Minted: `CENSUS_KEPT_PATHS`, `read_kept_rows` and `read_kept_path` in `tools/memory-tree/tree_lib.py`;
the `kept` argument of `check_cause_writers` and `run_check`; `FIXTURE_KEPT`, `KEPT_SCRIPT` and the
plant `kept-row-drained` in `record_causes.py`; its arm in `check-memory-hygiene.test.sh`. Retired:
`CAUSE_WRITER_KEPT`, `KEPT_PINNED` and `KEPT_OUTSIDE`. Naming cells: `python tools/lexicon/lexicon.py
--suggest <name> --as py.function` printed OK for `read_kept_rows` and `read_kept_path` on 2026-11-23,
each leading with `read`; the constants have no cell.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

`TOOL-dTotalRecall-56`, `-57` and `-58` also write these modules at order 30, so BUILD-METHOD M6
sequences the four passes, this one first, since two of them read its table.

### Alternatives rejected

- **Mark the eight files.** Two are pinned, all eight are outside this build's write set, and
  `TOOL-dTotalRecall-58` refuses the marker there.
- **Keep `CAUSE_WRITER_KEPT` for build-folder rows.** It leaves two file-keyed constants,
  `CAUSE_WRITER_KEPT` and `record_kinds.py#ALIAS_COMPARE_KEPT`, for one case. A kind's second
  instance extracts one table, read by both censuses.
- **A `[[ledger]]` population with `keep:<ask>` rows.** No owner ask exists for the seven files
  outside the pinned departures writer, and the ledger factory (`TOOL-dWitnessedBar-13`) is a
  baseline of counted sites, not a keep list.

## 5. Production-readiness checklist

- security — no new surface: a read-only census over tracked files.
- perf / scale — one tuple lookup per build-folder hit.
- error / empty / loading states — an unkept build-folder hit and a drained row are each red and
  named.
- observability — each kept hit prints its row's reason.
- risks — a reason is an author's statement; the batch `TOOL-dTotalRecall-60` keys its falsity test
  per file (id 44).
- testing — AC1 and AC2 by the pass; the arm of §7 at the close.
- migration — none: the rows replace `CAUSE_WRITER_KEPT`'s one for one, with the same reasons.
- user docs — none under `help/`: no page covers the census.

## 6. Acceptance criteria

- **AC1** — When `python record_causes.py --cause-writers` runs from `tools/memory-tree/` at the pass
  tip, it lists each of the eight files of §1 as `kept` with its row's reason and `deviations.py` as
  `pinned CAUSE_WRITER_PINNED`, red on none of the nine; `python record_causes.py --check` exits 0;
  and `git grep -n "CAUSE_WRITER_KEPT\|KEPT_PINNED\|KEPT_OUTSIDE" -- tools` prints nothing.
  Red when: a build-folder hit is red, unlisted, or kept by a marker in its own bytes, or a retired
  constant survives.
  figure: the census lines are DERIVED at observation. At `69d8787a3` they read the same with
  `CAUSE_WRITER_KEPT` holding the rows, so the grep is what tells the pass tip from HEAD.
- **AC2** — When `python record_causes.py --fixture --plant kept-row-drained` runs from
  `tools/memory-tree/`, its fixture keeps one build-folder script by a `FIXTURE_KEPT` row while the
  script spells no `**Serves:** ` literal, and the run exits 1 with one red naming
  `CENSUS_KEPT_PATHS` and the script's path.
  Red when: a row with no hit behind it still passes.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 · the plant `kept-row-drained`, its exit 1 and its named red, staged by skipping S4's drain test, which exits the plant 0 · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How does S4's drain read every row, and the fixture plant its own?** Rev-4 made
  `read_kept_path(census, path)`, a one-path lookup, the table's only reader, while the drain needs
  every row; and `record_causes.py#run_check` threads only `pinned`, so a fixture's row cannot reach
  a census reading the live constant. Options: (a) `read_kept_rows(census, table)` is the one reader,
  `read_kept_path` answers through it, and `check_cause_writers` and `run_check` take `kept` as they
  take `pinned`; (b) the drain walks `CENSUS_KEPT_PATHS` itself, a second reader that
  `TOOL-dTotalRecall-57`'s domain refusal and `TOOL-dTotalRecall-65`'s re-point must each find, and
  the fixture plants its script at a live row's path, which breaks when that row drains; (c)
  `read_kept_path` returns every row when `path` is None, one function with two return shapes. (a)
  meets both criteria with fewest follow-ups and reuses the `pinned` seam unit 50 set. RESOLVED
  (agent, 2026-11-23, delegated): (a), per `2026-11-23-prompt-TOOL-dTotalRecall-55-reground-brief`
  item 2(d), the feature-rich option after M3's vetoes. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 44 to 53, id 37
  (HIGH, item H1 shared with ids 4, 15 and 24).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-61, TOOL-dTotalRecall-65, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-67, the other end of an edge a unit the round-1 spec audit of units 61 to 66 promoted wrote; nothing else moved.
- rev-4 · 2026-11-23 · S2 AC1 §3 · amended by TOOL-dTotalRecall-61 (id 1, item H1) per
  `2026-11-22-prompt-TOOL-dTotalRecall-61-build-spec-writer`: the eight rows move out of
  `CAUSE_WRITER_KEPT`, its last after unit 53, so the constant ends at this pass; AC1 reads it gone, and
  the consumes-from line to unit 53 says S34 leaves only these rows in it.
- rev-5 · 2026-11-23 · §1 S1 S2 S3 S4 §3 §4 §5 AC1 AC2 §7 §8 F2 §10 · re-grounded at HEAD
  `69d8787a3` per `2026-11-23-prompt-TOOL-dTotalRecall-55-reground-brief`: unit 53 narrowed
  `CAUSE_WRITER_KEPT` to the eight rows rather than retiring it, the census re-derived; the table
  gains its one row reader and a `kept` argument (F2); the retired `KEPT_PINNED` and `KEPT_OUTSIDE`
  join AC1's grep; the arm's suite is `check-memory-hygiene.test.sh`; bare line citations are
  re-pinned.

## 10. Reuse audit

The seam extended is `record_causes.py#check_cause_writers` (`TOOL-dTotalRecall-36` S7, widened by
`TOOL-dTotalRecall-50` S1 and narrowed to S34's marker by `TOOL-dTotalRecall-53`), whose build-folder
keep test reads the table in the place of `CAUSE_WRITER_KEPT`, and whose `pinned` argument is the
shape `kept` takes. The table is the extraction a kind's second instance owes:
`record_causes.py#CAUSE_WRITER_KEPT` and `record_kinds.py#ALIAS_COMPARE_KEPT` are two file-keyed keep
dicts for one case, which this unit and `TOOL-dTotalRecall-56` fold into one. It sits beside
`tools/memory-tree/tree_lib.py#BIND_HEAD_LINES`, in the module both censuses import.
`python tools/codebase-map/reuse_lookup.py "keep a census hit in a file that cannot be edited"`,
re-run on 2026-11-23, ranked name-stem neighbours (`hit`, `census`, `write_fixture_files`) and no
path-keyed keep list; `id_grammar.py#read_kept_reason` keys by line, so it cannot hold a file no
marker may enter; `backlog.py#check_hold_live` resolves asks, and no row here names one.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
