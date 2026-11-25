# TOOL-aPrunedIndex-2 — a build finds an already-named path through a partial index, and reads no parse ledger without a blob

**Status:** SPECCED · rev-1 · 2026-11-25 · node a · Tier-1 · base 3d6c1702 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md](../build/2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 |
| [2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 |

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
  Observed by AC1, AC2 and AC5.
- **S2** — `tools/playbook/tag_index.py#_write_parsed` returns before it reads `blob_parsed` when
  `blobs` is empty. Observed by AC3 and AC4.
- **S3** — A new plant, `named-probe`, in `tools/playbook/gov_tag.py`, and its row in the tag
  resolver's plant table of `tools/playbook/adopt-playbook.sh`. Observed by AC1, AC2 and AC3.
- **S4** — The module docstring of `tools/playbook/tag_index.py` and the index paragraph of
  `tools/playbook/README.md` each say that the `parsed` rows are found through `path_row_named`.
  The index paragraph of `help/tags.md` says that an open which finds an SQL index missing builds it
  once, under the write lock. Where unit 1 already wrote that sentence, this unit adds none.
  Observed by AC6.

## 3. Non-goals (OUT)

- A unique index. A file holding two equal `parsed` rows would refuse to open.
- A change to what `_write_path_rows` writes, or to its query. The query already fits the index.
- A narrower ledger read for a build that has blobs. No measurement isolated its cost.
- Dropping `path_row_key`. The sweep searches by path and blob.
- The served reads, the sweep and `--gc`, which are units 1, 3 and 4.
- Any open of the live index files. Every measurement runs on a private copy or a fixture.

### Edges

- **consumes-from** `TOOL-aPrunedIndex-1` — its index on the extractor version. On that index alone
  the probe gets slower, as the table in section 4 shows, so a tree carrying unit 1 without this unit
  must open no shared index.
- **consumes-from** external — the owner's word in the building session before this code first opens
  the live index.

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
`_derive_applicable`, and counts the steps of one `_write_path_rows` call over them with
`set_progress_handler` at one instruction.

1. It counts with no pad, with the dead pad, and with the own pad added to that. The dead pad copies
   the fixture's own `path_row` rows under 50 version names. The own pad copies the rows of the
   versions the fixture derives to 20 new paths each. All three counts must be equal and above 0, and
   each pad must have written rows.
2. It drops `path_row_named` and counts again. That count must be higher, which proves the pads reach
   the probe.
3. It closes the connection and opens the file through `load_index`. The index must be back, the
   `path_row` count unchanged, and the stamp still `INDEX_SCHEMA`.
4. It traces the statements of `build_overlay` with `set_trace_callback`, and counts those that open
   with `SELECT` and read `blob_parsed`. The clean worktree must give 0, and the same worktree with
   one edited guide must give 1.

It prints each count on its own line. Its last line is printed only when every condition holds, carries
the two ledger counts, and ends `equal under every pad`. It exits 0 then, and 1 otherwise.

### Migration

The first open after landing builds this index and unit 1's. The diagnosis measured the pair at about
205 s under the write lock and 1 GB on the 12.6 GB copy, and `BUSY_TIMEOUT` is 600 s, so a waiting
writer outlasts it. An edit to `tag_index.py` is a new extractor version, so each worktree also
re-parses once. A rebuild of the file under a stale stamp runs the new statement too, since it splits
`SCHEMA` on `;` and the statement holds none.

### Inventory

One SQL index, `path_row_named`, and one plant, `named-probe`. No function is added, so no naming cell
grades either.

### Files touched (estimate)

- `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`, `tools/playbook/adopt-playbook.sh`
- `tools/playbook/README.md`, `help/tags.md`

### Alternatives rejected

- The five columns over every row rather than the `parsed` rows: 17.8 million entries on the live file,
  where the probe reads only the `parsed` ones.
- One bulk read of the reading version's `parsed` rows into a set: it needs the same index to avoid the
  scan, and adds a structure beside it.

### Reuse

The seams extended are `SCHEMA`, `_write_parsed` and the `--fixture --plant` runner. The probe
`tools/codebase-map/reuse_lookup.py "find whether a path's rows are already named in the shared tag
index"` returned `read_rows` and `build_index` of `tag_index.py` and no other row-index seam. The recall
answered KICK-dKeptSession-87 and PLAY-dOrderedCharter-44.
Recall terms used: tag index path_row parsed sentinel blob_parsed ledger probe partial index build overlay versions dead freshness

## 5. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant named-probe` runs, its three step
  counts are equal and above 0, and it exits 0.
  Red when: the `path_row_named` statement is removed from `SCHEMA`, whether or not unit 1's index is
  beside it.
- **AC2** — When `named-probe` drops `path_row_named`, its count rises. When it reopens the file
  through `load_index`, the index is back, the `path_row` count is unchanged and the stamp is 3.
  Red when: the pads touch no probed path, so the count stays, or `INDEX_SCHEMA` moves.
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
  `tools/playbook/README.md`, the first prints 2 or more and the second 1 or more. When
  `grep -n "SQL index" help/tags.md` runs, it prints the sentence S4 names.
  Red when: the docstring or a page still describes only the sentinel row.

## 6. Gates

`tags (the resolver's checks)` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 · the `named-probe` row; staged red three times, with the `path_row_named` statement removed from `SCHEMA`, with the early return removed, and with the early return unconditional · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-25 · initial draft.
