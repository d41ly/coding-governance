# TOOL-aPrunedIndex-2 — a build finds an already-named path through a partial index, and reads no parse ledger without a blob

**Status:** SPECCED · rev-4 · 2026-11-26 · node a · Tier-1 · base 3d6c1702 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md](../build/2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 |
| [2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 |
| [2026-11-25-prompt-TOOL-aPrunedIndex-3-revision.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-3-revision.md) | research | TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-4 |
| [2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1.md](../reviews/2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1.md) | spec-audit | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 |
| [2026-11-26-review-TOOL-aPrunedIndex-1-2-3-spec-audit-round1.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-3 |

<!-- /gen:spec-records -->

## 1. Goal

A tag-index build asks, for each path, blob and extractor, whether a `parsed` row already names it.
Each question walks every stored version's rows of that path, and an overlay with no blob loads the
whole parse ledger to look nothing up. After this unit each question is one seek, and a build or
overlay with no blob reads no ledger. No row and no verdict changes.

## 2. Scope (IN)

- **S1** — `tools/playbook/tag_index.py#SCHEMA` gains one statement, the partial index
  `path_row_named` over `path_row(path, blob, extractor, version, conf)` where `kind='parsed'`.
  `INDEX_SCHEMA` stays 3. An existing index file gains it at its next open, with no row changed.
  Observed by AC1, AC2, AC5 and AC9.
- **S2** — `tools/playbook/tag_index.py#_write_parsed` returns before it reads `blob_parsed` when
  `blobs` is empty. Observed by AC3 and AC4.
- **S3** — A new plant, `named-probe`, in `tools/playbook/gov_tag.py`, and its row in `SELFTEST_ROWS` of
  `tools/playbook/tag_bundle.py`. Observed by AC1, AC2, AC3 and AC8.
- **S4** — The module docstring of `tools/playbook/tag_index.py` and the index paragraph of
  `tools/playbook/README.md` each say that the `parsed` rows are found through `path_row_named`. The help
  page's sentence on a missing SQL index is unit 1's and covers this one. Observed by AC6.

## 3. Non-goals (OUT)

- A unique index. A file holding two equal `parsed` rows would refuse to open.
- A change to what `_write_path_rows` writes, or to its query. The query already fits the index.
- A narrower ledger read for a build that has blobs. No measurement isolated its cost.
- Dropping `path_row_key`. The sweep searches by path and blob.
- The served reads, the sweep and `--gc`, which are units 1, 3 and 4.
- Any open of either live index file before the owner's go. The owner gave it on 2026-11-25, in
  `2026-11-25-prompt-TOOL-aPrunedIndex-3-revision`, on three conditions: all four units are built and
  measured on private copies, the closing review is clean, and the open comes before the bar. Every
  measurement here runs on a private copy or a fixture.
- Any run, from the building worktree before that go, of what opens the live index: the legs
  `tags (the resolver's checks)`, `instruction edits (manifest checks)`,
  `edges (every declared edge parses, is registered and resolves)` and `instruction units selftest`, and a
  `gov_tag.py` verb outside `--fixture`. This unit is verified by `--fixture` plants and private copies.

### Edges

- **consumes-from** `TOOL-aPrunedIndex-1` — its index on the extractor version. On that index alone
  the probe gets slower, as the table in section 4 shows, so a tree carrying unit 1 without this unit
  must open no shared index. The plant counts with its `read_step_count`, and this index is built by its
  Rollout step and named by its stderr line.
- **hands-off** `TOOL-aPrunedIndex-3` — `path_row_named`, which unit 3's AC5, AC9 and section 4 plans rest
  on.
- **hands-off** `TOOL-aPrunedIndex-4` — the `named-probe` row, one of the five unit 4's AC8 times.
- **consumes-from** external — the owner's go for this code's first open of the live index, on the
  conditions the list above states.

## 4. Design

### Mechanism

`tools/playbook/tag_index.py#_write_path_rows` already filters on all five columns and on the literal
`kind='parsed'`, so SQLite can serve it from the partial index with no change to the query. The plan
becomes a search of a covering index. `tools/playbook/tag_index.py#load_index` runs `SCHEMA` at every
open, and each of its statements is `IF NOT EXISTS`, so an existing file gains the index in place. A
worktree on older code maintains the index without naming it, because the index lives in the file.

`_write_parsed` loads `held` from the whole ledger, finds nothing to do, and returns. With no blob it
writes nothing and leaves `stats` alone, so the early return above the load changes no result.
`tools/playbook/tag_index.py#build_overlay` reaches it with no blob for a clean worktree, and for one
whose only edits are deletions.

### Why the two indexes land together

With no planner statistics, unit 1's index wins over `path_row_key` for this query, so each probe then
walks every row of one extractor at the reading version. The counts below are virtual-machine steps of
one `_write_path_rows` call over 40 named pairs, on an in-memory database built from the module's own
`SCHEMA`. They are PINNED, measured 2026-11-25 on SQLite 3.53.4. The dead pad is 50 more versions of
the same paths. The own pad is the reading version's rows at 20 times as many other paths.

| indexes added | no pad | dead pad | own pad | both pads |
|---|---|---|---|---|
| none | 4575 | 148575 | 4575 | 148575 |
| the version index only | 50164 | 50164 | 506164 | 506164 |
| `path_row_named` only | 878 | 878 | 878 | 878 |
| both | 887 | 887 | 887 | 887 |

A plant with the dead pad alone stays green on the second row, so the plant carries both pads. On a
private 1.4 GB file holding the version index, `EXPLAIN QUERY PLAN` named that index for this query,
and the file held no `sqlite_stat` table. That read is PINNED, 2026-11-25.

### The plant

`named-probe` builds its fixture's index with `rebuild`. It derives the pairs of the HEAD tree through
`_derive_applicable`. It counts one probe as
`read_step_count(con, lambda: ti._write_path_rows(con, pairs, versions, conf))`, the helper unit 1 adds,
whose uncounted first run takes the compile out. A step of drift remains between two counts, so the bounds
below are ratios. A count "without" an index drops it, counts, and runs `SCHEMA` to put it back.

1. It counts with no pad, as the first count, which must be above 0. It also counts without
   `path_row_named`, and without `path_row_named` and `path_row_version` together.
2. It writes the dead pad, the fixture's own `path_row` rows under 50 version names, and counts. That
   count must be at most 1.1 times the first. Without both indexes the count must exceed twice the same
   count of step 1, which proves the dead rows stand on the probed paths. While `path_row_version` stands
   the dead pad is invisible, so dropping `path_row_named` alone would prove nothing about it.
3. It adds the own pad, the rows of the versions the fixture derives at 20 new paths each, and counts. That
   count must be at most 1.1 times the first. Without `path_row_named` the count must exceed twice the same
   count of step 1 and twice the first, which proves the own rows are what that index hides. Each pad must
   have written rows.
4. It drops `path_row_named`, closes the connection and opens the file through `load_index`. The index must
   be back, the `path_row` count unchanged, and the stamp still `INDEX_SCHEMA`.
5. It traces the statements of `build_overlay` with `set_trace_callback`, and counts those that open
   with `SELECT` and read `blob_parsed`. The clean worktree must give 0, and the same worktree with
   one edited guide must give 1.

It prints each count on its own line. Its last line is printed only when every condition holds, carries
the two ledger counts, and ends `within a tenth under every pad`. It exits 0 then, and 1 otherwise. A
prototype of steps 1 to 3 over the `none` fixture's 6 pairs read these counts on 2026-11-25 with SQLite
3.53.4. They are PINNED. The plant took 3 to 5 s.

| Code | first, dead pad, both pads | dead pad's proof | own pad's proof |
|---|---|---|---|
| this unit | 125, 126, 126 | 317, 7817 | 346, 3348 |
| `path_row_named` out of `SCHEMA`, the version index present | 346, 348, 3348 | 317, 7817 | 346, 3348 |
| the dead pad on unprobed paths | 125, 126, 126 | 317, 318 | 346, 3348 |
| the own pad under another extractor | 125, 126, 126 | 317, 7817 | 346, 348 |

### Migration

The first open after landing builds this index and unit 1's. The diagnosis measured the pair at about
205 s under the write lock and 1 GB on the 12.6 GB copy, and `BUSY_TIMEOUT` is 600 s, so a waiting
writer outlasts it. An edit to `tag_index.py` is a new extractor version, so each worktree also
re-parses once. Unit 1's Rollout step builds both indexes outside any leg. Each CREATE INDEX commits
alone, so an opener killed in this one keeps unit 1's, rolls this one back with no row changed, and leaves
the next opener to start it again. A disk that fills inside this one raises the `cannot be opened` refusal,
with every row intact and unit 1's index kept, as unit 1's Migration records. Its Rollout checks the free
space for both. A rebuild of the file under a stale stamp runs the new statement too,
since it splits `SCHEMA` on `;` and the statement holds none.

### Inventory

One SQL index, `path_row_named`, and one plant, `named-probe`. No function is added, so no naming cell
grades either.

### Files touched (estimate)

- `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`, `tools/playbook/tag_bundle.py`
- `tools/playbook/README.md`
- `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-2-1-acceptance-ledger.md`, the unit's
  record, which holds the figures AC5 and AC7 ask for

### Alternatives rejected

- The five columns over every row rather than the `parsed` rows: 17.8 million entries on the live file,
  where the probe reads only the `parsed` ones.
- One bulk read of the reading version's `parsed` rows into a set: it needs the same index to avoid the
  scan, and adds a structure beside it.

### Reuse

The seams extended are `SCHEMA`, `_write_parsed`, unit 1's `read_step_count`, the `--fixture --plant`
runner and the row table of `tools/playbook/tag_bundle.py#run_selftest`. The probe
`tools/codebase-map/reuse_lookup.py "find whether a path's rows are already named in the shared tag
index"` returned `read_rows` and `build_index` of `tag_index.py` and no other row-index seam. The recall
answered KICK-dKeptSession-87 and PLAY-dOrderedCharter-44.
Recall terms used: tag index path_row parsed sentinel blob_parsed ledger probe partial index build overlay versions dead freshness

## 5. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant named-probe` runs, its padded counts
  are each at most 1.1 times the first, which is above 0, and it exits 0.
  Red when: the `path_row_named` statement is removed from `SCHEMA` with unit 1's index beside it, so the
  count under both pads is about ten times the first.
- **AC2** — When `named-probe` takes each pad's proof, the dead pad's count without both indexes and the
  own pad's without `path_row_named` each exceed twice the unpadded count taken without the same indexes.
  When it reopens the file through `load_index`, the index is back, the `path_row` count is unchanged and
  the stamp is 3.
  Red when: a pad touches no probed path or version, so its proof count stays, or `INDEX_SCHEMA` moves.
- **AC3** — When `named-probe` traces `build_overlay`, a clean worktree reads `blob_parsed` 0 times and
  a worktree with one edited guide reads it once.
  Red when: the early return is removed, so the clean count is 1, or it is unconditional, so the edited
  count is 0.
- **AC4** — When `python tools/playbook/gov_tag.py --fixture --plant <case>` runs for `two-paths`,
  `tagless`, `new-extractor`, `dirty` and `charter-dirty`, each exits 0.
  Red when: the early return skips a blob that has rows to write.
- **AC5** — When `_write_path_rows` runs over the HEAD tree's pairs on one private copy padded with 12
  dead versions, with `path_row_named` present and dropped in alternation, two passes each and unit 1's
  index present throughout, the unit's record names the wall and CPU seconds of every pass, and each
  pass with the index is the faster of its pair.
  Red when: SQLite serves the probe from another index on a file of that size.
  cost: about 4 GB of scratch disk and some minutes; the two slow passes may be stopped at ten minutes
  each and recorded as that floor.
  fixture: a padded copy of the clean 270 MB copy the building session's scratch holds, made for this
  criterion.
  figure: DERIVED at observation time.
- **AC6** — When `grep -c path_row_named` runs over `tools/playbook/tag_index.py` and
  `tools/playbook/README.md`, the first prints 2 or more and the second 1 or more.
  Red when: the docstring or the page still describes only the sentinel row.
- **AC7** — When a child process opening AC5's copy through `load_index`, with both SQL indexes dropped, is
  killed after its `tag-index — building:` line and before it returns, and the file is then opened again
  through `load_index`, both indexes are present and the `path_row` count is the one read before the kill.
  The unit's record names which index stood after the kill.
  Red when: a kill leaves a half-built index or moves a row.
  fixture: the copy AC5 makes.
- **AC8** — When a Python probe imports `tag_bundle` from `tools/playbook` and prints the lines of
  `SELFTEST_ROWS` whose first field is `named-probe`, it prints one, whose second field is 0 and whose last
  is `within a tenth under every pad`.
  Red when: the row is missing or misspelled, so no leg runs the plant.
- **AC9** — When unit 1's AC9 probe runs with both index statements in `SCHEMA`, both SQL indexes dropped
  and the cap at 35 pages above the file's `page_count`, `load_index` raises a `TagError` holding `cannot be
  opened`, `path_row_version` stands, `path_row_named` does not, and the row count is 5,000.
  Red when: the two indexes share one transaction, so the finished one goes too.
  figure: the 35 pages are PINNED, 2026-11-26, SQLite 3.53.4; the probe moves the cap until one index stands
  if the page count of either has moved.

## 6. Gates

`tags (the resolver's checks)` · `instruction edits (manifest checks)` · `edges (every declared edge parses, is registered and resolves)` · `instruction units selftest` · `tags bundle selftest` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

Those of the line that open the live index, the four section 3 lists, are owed at the close, once the go
section 3 states holds, and by no pass before it.

New arm: tools/playbook/tag_bundle.py · covers AC1 AC2 AC3 · the `named-probe` row; staged red five times, with the `path_row_named` statement removed from `SCHEMA` while `path_row_version` stands, with the dead pad on unprobed paths, with the own pad under another extractor, with the early return removed, and with the early return unconditional · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-25 · initial draft.
- rev-2 · 2026-11-25 · §2 §3 §4 §5 §6 S3 S4 AC1 AC2 AC6 AC7 · folded
  `2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1`: finding 2 (each pad proved against an
  unpadded count that lacks the same indexes), 4 (the help sentence leaves this unit), 5 (the edge to unit
  3), 8 and 11 (`read_step_count` is the counter), 9 (the uncounted first run and the 1.1 bound), 12 (the
  plant's row moves to `tags bundle selftest`), 13 and 17 (the killed build and AC7), 14 (the legs that open
  the live index).
- rev-3 · 2026-11-26 · §3 · TOOL-aPrunedIndex-3's revision on finding 16 of
  `2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1` leaves five rows for unit 4's AC8
  to time.
- rev-4 · 2026-11-26 · §2 §3 §4 §5 §6 S1 S3 AC8 AC9 · folded
  `2026-11-26-review-TOOL-aPrunedIndex-1-2-3-spec-audit-round1`: finding 3 (AC8 reads the plant's row), 4
  (the owner's go with its conditions, stated once in section 3), 5 (the three legs that open the live index
  and the lexicon leg), 10 (the acceptance ledger is the unit's record, with the two legs its path owes), 14
  (the disk-full behaviour and AC9).
