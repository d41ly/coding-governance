# TOOL-aMendedFleet-54 — drift reports `live_builds_without_activity` from the dormant rows LIVE.md renders

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 54

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Idle builds read as live work: `memory/LIVE.md` lists every build with a non-terminal unit, and
unattended runs choosing work spend passes on rows nobody is working. Unit 12 renders the answer into
LIVE.md, an `Activity` column reading `active` or `dormant` against `LIVE_DORMANT_DAYS`. This unit
adds the drift signal `live_builds_without_activity`, which counts the `dormant` rows of that
rendered table, so the reading persists in the drift history, reaches the kickoff card and the close
through the channels other units build for drift, and moves when a dormant build is closed or
resumed. It defines no second dormancy rule.

## 2. Scope (IN)

- **S1** — A new builder `build_live_builds_without_activity` in
  `tools/drift-audit/drift_report.py`, listed in `SIGNALS`, reads `<memory root>/LIVE.md` from the
  working tree, finds the first markdown table, locates the `Activity` column BY HEADER NAME, and
  reads each body row's cell. `value` is the count of rows reading `dormant`, `of` the count reading
  `active` or `dormant`, and a cell reading anything else is counted in `unjudgeable` and never as
  active. Each detail row names a dormant build's slug, taken from the row's link text, and its
  `Last record` cell where that column exists. Observed by AC1, AC3.
- **S2** — The states. No LIVE.md, or a table with no `Activity` header, returns the
  `_build_not_asked` record with a note naming which, because a repo that leaves
  `LIVE_DORMANT_DAYS` blank does not ask the question. A table with the column and no row returns
  `live` false. The record is `gateable` false, with the pinless `tolerance` unit 51 introduces: a
  dormant build is a state to read, not a debt with a ceiling. Observed by AC2.
- **S3** — The drift-audit README's `## The signals` table gains the row for the new signal, in the
  same commit, so the hand-kept signal unit 52 re-arms keeps reading 0. Observed by AC4.
- **S4** — Self-test arms in `tools/drift-audit/selftest.py` over fixture LIVE.md files: two dormant
  rows of three read value 2 of 3; a table without the `Activity` header reads not asked; an
  unknown cell is unjudgeable; a column placed after `Activity` moves nothing. NOT OBSERVED by a
  criterion here: the suite runs once at the close, and the arms are declared under `New arm:` in
  §7.
- **S5** — `memory/map/generated/symbols.json` is regenerated for the new definition. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and
  §7 names the legs that read it.

## 3. Non-goals (OUT)

- Any second definition of dormancy, a git-history read or a clock. Unit 12's spec measured those
  and rejected them; this signal reads its output.
- Acting on a dormant build: retiring, deferring or filing an ask. The signal reports.
- A pin. The count moves with the calendar and with work, and a ceiling on it would red a tree
  nobody touched.
- The kickoff card line and the close delta, which read every signal through units 76 and 49.
- The drift-audit kit version bump, owed once at the close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-12` — the `Activity` column of `memory/LIVE.md`; without it
  the signal reads not asked on this repo.
- **consumes-from** `TOOL-aMendedFleet-51` — the pinless `tolerance` form S2 uses.
- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at worktree HEAD `725b1449`, whose `tools/` and `memory/LIVE.md` bytes equal base `7af5f564`'s.

- `memory/LIVE.md` today renders `| Build | Status | Node | Opened | Streams | Ids (n) |` and no
  activity column; unit 12 appends `Last record` and `Activity` and keeps ONE table, and unit 13
  appends its column after those two. Reading by header name survives both.
- Unit 12 measured 20 of 23 live rows dormant at 21 days. PINNED, measured 2026-10-04 by unit 12.
- `read_asks_projection` shows the kit's existing convention for reading another kit's generated
  output: the generator owns the rule, and drift counts what it renders.

### Inventory

- `build_live_builds_without_activity` — cell `py.function`; answered OK by
  `python tools/lexicon/lexicon.py --suggest build_live_builds_without_activity --as py.function`.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Re-derive each build's last record date in drift.** A second copy of unit 12's rule, which its
  own hands-off line asks this unit not to write.
- **Ask the generator for a JSON projection of live builds.** No such projection exists; adding one is
  a change to the memory-tree kit's surface for a reader the committed table already serves.
- **Count commits naming each slug, the source synthesis's measure.** Unit 12 rejected git history
  for this question on two recorded tests.

## 5. Production-readiness checklist

- security — N/A: reads one tracked generated file.
- perf / scale — one file read, no spawn.
- error / empty / loading states — S2's three states; a malformed row is unjudgeable.
- observability — the detail names each dormant slug and its last record date.
- risks — a hand-edited LIVE.md would mislead the signal; memory hygiene check 9 reds a stale
  render, so the committed table is the rendered one.
- testing — AC1 to AC4 here; the arms in S4.
- migration — N/A: nothing stored changes.
- user docs — S3.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs on this repo after unit 12
  has landed, the `live_builds_without_activity` record has `live` true and `gateable` false, its
  `of` equals the count `grep -c '](builds/' memory/LIVE.md` prints, and its `value` equals the count
  `grep -c '| dormant |' memory/LIVE.md` prints.
  Red when: either count disagrees with the rendered table.
  figure: DERIVED at observation time; 20 of 23 by unit 12's measure at writing.
- **AC2** — When the `Activity` header cell of `memory/LIVE.md` is renamed in the working tree and
  `python tools/drift-audit/drift_report.py` runs, the signal's row prints the not-asked status and
  the `--json` detail note names the missing column; `git checkout -- memory/LIVE.md` restores AC1.
  Red when: a table without the column reads as a clean 0.
- **AC3** — When one `dormant` cell of `memory/LIVE.md` is edited to an unknown word in the working
  tree and `python tools/drift-audit/drift_report.py --json` runs, the record's `unjudgeable` is 1,
  its `value` falls by one and its `of` falls by one; restoring the file restores AC1.
  Red when: an unknown cell is read as active.
- **AC4** — When `grep -c "live_builds_without_activity" tools/drift-audit/README.md` runs it reports
  at least 1, and the `handkept_inventories_disagreeing_with_source` record of
  `python tools/drift-audit/drift_report.py --json` reads `value` 0.
  Red when: the README table omits the new signal.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `encoding posture (text IO names its encoding)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · fixture LIVE.md tables with dormant rows, without the column, with an unknown cell and with a later column · `CHECK_FLOOR` moves by the checks the arm adds

## 8. Open questions

- **F1** — Where does the signal get each build's activity?
  Options: re-derive the dates; read a generator projection; read the rendered LIVE.md column.
  Re-deriving is a second rule and the projection does not exist.
  RESOLVED (agent, 2026-10-04, delegated): read the rendered column by header name, per S1.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#59] and unit 12's hands-off.
- rev-2 · 2026-10-04 · S5 · §4 · §7 · M2 cross-read: the new definition owes `symbols.json`, which
  units 57, 59 and 90 regenerate for theirs and this spec omitted.

## 10. Reuse audit

The seams extended are the `SIGNALS` list and the record shape of
`tools/drift-audit/drift_report.py`, `_build_not_asked` for the unadopted case, and unit 12's
rendered `Activity` column, read rather than re-derived. `python tools/codebase-map/reuse_lookup.py
"read the dormant activity column of the generated work-state index"` returned name-stem neighbours
only: `read_text` in the memory-tree generator and migrator, `build_reference_index` in the map kit
and `test_generated_artifacts_are_fresh` in the map tests, none of which reads LIVE.md's columns; no
existing seam fits the table read, so it lives in the builder. The scan names `.sh` as unscanned;
the one shell reader of LIVE.md, the kickoff card's row count, counts rows and reads no column.
Recall returned unit 12, whose hands-off names this signal, unit 13, which appends the next column,
and unit 51, whose pinless form this uses. Where the report and the tree disagree: the synthesis
measured inactivity by commits naming a slug; this signal takes unit 12's record-date measure.

Recall terms used: `python tools/memory-recall/query.py "should drift report builds that are live
but have had no activity" --terms "live_builds_without_activity LIVE.md dormant last-touch
INPROGRESS phantom claims idle residue drift signal report-only LIVE_DORMANT_DAYS"`
