# TOOL-aPrunedIndex-3 — a build's and an overlay's sweep touch only the rows that the trees and edits they let go of held

**Status:** SPECCED · rev-1 · 2026-11-25 · node a · Tier-2 · base 3d6c1702 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md](../build/2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-4 |
| [2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-4 |

<!-- /gen:spec-records -->

## 1. Goal

Every build of an unbuilt tree ends by scanning the whole of `path_row`, `blob_row` and `blob_parsed`
for rows nothing holds. On the 12.6 GB copy two such sweeps took 537 s of one check, and the rows they
scan are mostly those of dead extractor versions (PINNED, the diagnosis, 2026-11-25). After this unit a
build and an overlay look only at the rows that the trees and uncommitted edits they let go of held.
`--gc` keeps the full sweep. No row any worktree is served changes.

## 2. Scope (IN)

- **S1** — A new function, `remove_dead_holders`, in `tools/playbook/tag_index.py` carries the first
  half of today's `remove_unheld_rows`: the trees no worktree's HEAD names, and the dirty rows of
  worktrees that are gone. It returns the set of (path, blob) pairs they held. Observed by AC1.
- **S2** — A new function, `remove_released_rows`, in the same module takes such a set and clears the
  rows of those pairs, and of those blobs, that no remaining tree or dirty row holds. It clears them
  at every version and every conf key. Observed by AC1, AC2 and AC5.
- **S3** — `tools/playbook/tag_index.py#build_index` ends its write block with S2 over S1's set.
  Observed by AC1 and AC2.
- **S4** — `tools/playbook/tag_index.py#build_overlay` reads the dirty pairs its worktree held, under
  the write lock and before it writes the new ones, and ends the block with S2 over them. Today those
  rows wait for the next build by any worktree. Observed by AC1 and AC2.
- **S5** — `remove_unheld_rows` keeps the full sweep alone, as `remove_unheld_rows(con)`, and
  `tools/playbook/tag_index.py#remove_dead_versions` calls S1 and then it. Observed by AC3.
- **S6** — Two new plants, `released-rows` and `released-cost`, in `tools/playbook/gov_tag.py`, each
  with its row in the tag resolver's plant table of `tools/playbook/adopt-playbook.sh`. Observed by
  AC1, AC2 and AC3.
- **S7** — The docstrings of the functions above, and the index paragraph of
  `tools/playbook/README.md`, say that a build and an overlay clear only what the trees and dirty rows
  they let go of held, and that `--gc` alone sweeps the row tables whole. Observed by AC6.

## 3. Non-goals (OUT)

- Which trees and dirty rows a build lets go of. The rule of `read_worktree_trees` and `keep` stays.
- The rows of a dead extractor version that a live tree still holds. `--gc` collects those.
- The served reads, the name probe and the parse ledger, which are units 1 and 2, and which worktrees
  `--gc` reads, which is unit 4.
- The `git rev-parse` per worktree inside `read_worktree_trees`, which runs under the write lock. Its
  cost follows the count of worktrees, not the stored versions.
- The `SELECT DISTINCT tree FROM tree_path` that lists the trees. It reads one key index, and its cost
  follows the trees held.
- A new SQL index, a schema change, or a stored table of released pairs.
- Any open of either live index file. Every measurement runs on a private copy or a fixture.

### Edges

- **hands-off** external — the owner's word in the building session before this code first opens the
  live index.

## 4. Design

### Evidence

`tools/playbook/tag_index.py@4b10fce5d:825-843` is the whole of today's sweep. It has two callers,
`build_index` and `remove_dead_versions` (`tools/playbook/tag_index.py@4b10fce5d:805,925`), and a grep
over `tools/` found no other. `build_overlay` replaces its worktree's dirty rows
(`tools/playbook/tag_index.py@4b10fce5d:875-876`) and sweeps nothing.

A row of the three tables can stop being held in four ways only. A `tree_path` row goes when its tree
is let go of. A `dirty_path` row goes when its worktree is gone. The same row goes when its own
worktree's overlay is recorded again. The fourth is the rewrite of one tree's `tree_path` rows at the
top of a build (`tools/playbook/tag_index.py@4b10fce5d:800-801`). A tree id is a content hash, so that
rewrite puts back the rows it took out. The first three are the sources S1 and S4 name.

### Mechanism

1. `remove_dead_holders(con, root, keep=())` is today's first half, with one line added to each arm.
   Before a tree's rows go, its (path, blob) pairs join a Python set, and so do a gone worktree's dirty
   pairs. It returns the set.
2. `remove_released_rows(con, released)` returns at once on an empty set. Otherwise it fills the temp
   table below, cleared first, and runs four steps:
   - it takes a pair out of `released` when any tree or dirty row still holds that path at that blob;
   - it clears the `path_row` rows of the pairs left;
   - it takes a pair out when any tree or dirty row still holds its blob at any path;
   - it clears the `blob_row` and `blob_parsed` rows of the blobs left.
3. `build_index` calls `remove_released_rows(con, remove_dead_holders(con, root, keep={tree}))`.
4. `build_overlay` reads its held pairs after `BEGIN IMMEDIATE` and before the rows are taken out. It
   calls `remove_released_rows` after `_write_path_rows`, so a pair that stays dirty is held again by
   then and keeps its rows.
5. `remove_dead_versions` calls `remove_dead_holders(con, root)` and then `remove_unheld_rows(con)`,
   whose statements are today's three, byte for byte.

```sql
CREATE TEMP TABLE IF NOT EXISTS released(path TEXT, blob TEXT, PRIMARY KEY(path, blob));
DELETE FROM released WHERE EXISTS (SELECT 1 FROM tree_path t WHERE t.path=released.path AND t.blob=released.blob)
   OR EXISTS (SELECT 1 FROM dirty_path d WHERE d.path=released.path AND d.blob=released.blob);
DELETE FROM path_row WHERE (path, blob) IN (SELECT path, blob FROM released);
DELETE FROM released WHERE EXISTS (SELECT 1 FROM tree_path t WHERE t.blob=released.blob)
   OR EXISTS (SELECT 1 FROM dirty_path d WHERE d.blob=released.blob);
DELETE FROM blob_row WHERE blob IN (SELECT blob FROM released);
DELETE FROM blob_parsed WHERE blob IN (SELECT blob FROM released);
```

`blob_row` and `blob_parsed` leave over one set of blobs inside one transaction, so a blob is never
parsed twice into rows that already stand. A deleted file's dirty pair carries blob `""`, which no row
of the three tables carries.

### The plans

Read on 2026-11-25 with SQLite 3.53.4, on a private copy holding 1,716,900 path rows in 4 versions and
42 trees, with the SQL indexes of units 1 and 2 added. The figures are PINNED, warm.

| Statement | Plan | Time | Rows |
|---|---|---|---|
| keep the held pairs | `SEARCH t USING INDEX tree_path_blob (blob=?)` per pair | 0.148 s | 15,732 pairs, 5 left |
| clear `path_row` | `SEARCH path_row USING COVERING INDEX path_row_key (path=? AND blob=?)` | 0.003 s | 172 |
| keep the held blobs | `SEARCH t USING COVERING INDEX tree_path_blob (blob=?)` | under 0.001 s | 0 |
| clear `blob_row` | `SEARCH blob_row USING COVERING INDEX blob_row_key (blob=?)` | 0.001 s | 152 |
| clear `blob_parsed` | a search of its primary key | under 0.001 s | 20 |
| the full sweep, run after them | three table scans | 4.255 s | 0 |

The last row is the equivalence read on that copy: the full sweep found nothing the five left behind.
The dirty half of each `EXISTS` scans `dirty_path`, once per pair no tree holds. That table holds the
uncommitted edits of the node's worktrees and no version, and a comment in the code names that ceiling
and an index on its blob as the way past it.

### What does not change

- What a worktree is served. `load_view` fills its view from `tree_path` and `dirty_path`, and a row is
  cleared only when neither table holds its pair.
- A worktree on older code. Its builds run the full sweep over the same file, which clears only rows
  nothing holds, under the same write lock.

### What it cannot see

- A row nothing held before this code ran, such as one an older worktree's overlay left. No set names
  it, so it stays until a `--gc` or an older worktree's build. No view holds its pair, so none serves
  it. If its pair is held again, its rows are right: they are keyed by content, version and conf.
- Two commands of one worktree with an edit to a file between them. The second command's overlay clears
  the first edit's rows while the first command still reads its own view. Today those rows last until
  the next build by any worktree. A commit between two such commands already opens the same window
  through the build's sweep.

### The plants

**`released-rows`** grades exactness, in the fixture's repository with two linked worktrees. After each
step below it opens the index, takes the write lock, reads two counts, and rolls back.

- `left`: how many rows of each table the full sweep `remove_unheld_rows` would clear now.
- `lost`: `path_row` rows whose blob, extractor and version have no `blob_parsed` row, and held paths
  under `memory/guides/` whose blob has a `blob_parsed` row no `path_row` row answers.

The steps: two guides of one text, then one of them committed apart, so a blob loses one path and keeps
another. The main worktree edits it. The second worktree makes that edit at both paths. The main one
edits again. The second one edits one path further, then reverts the other. The main one stages a
deletion, then resets. The third worktree edits, is removed and pruned, and the main one commits. Last,
a commit that both remaining worktrees stand on. Then `read_dump` must equal `read_cold_dump`, through
the plant runner's `print_equal`. It prints one line per step. It exits 0, with a last line ending
`nothing left and nothing lost`, only when every count is 0 and the dumps are equal.

Before that line it inserts one row into each of the three tables, at the fixture's live version, for a
blob no tree holds. A `rebuild` of a new commit must leave them, and `run_gc` must clear them.

**`released-cost`** grades cost. It counts virtual-machine steps with `set_progress_handler` at one
instruction, over one `load_view` that builds a new commit and records a changed dirty edit.
`set_trace_callback` splits the count in two:

- the build's sweep, every statement from the `tree_built` insert to its `COMMIT`;
- the overlay's, every statement outside that window opening `DELETE FROM` one of the three tables.

It counts a first commit, then pads the index with the rows of one held file under 40 further version
names in all three tables, then counts a second commit of the same shape. Each half of the second count
must be at most twice the first. Each half must have run a delete on all three tables in both counts,
which is what keeps a build that sweeps nothing from passing. The last line ends
`sweeps cost what was released`.

The prototype's counts are PINNED from 2026-11-25, as build half then overlay half.

| Code | before the pad | after it |
|---|---|---|
| this unit | 1429, 210 | 1426, 210 |
| the full sweep in the build | 1647, 215 | 6204, 215 |
| the full sweep in the overlay | 1429, 1203 | 1426, 5763 |

The prototype of `released-rows` was green on this design and red on each of eight breaks: no set from
the overlay, from a gone worktree or from a tree; the pair filter or the blob filter absent; each
filter's dirty half absent; and `blob_row` left uncleared. The step that inserts and collects three
rows was not prototyped. The existing plant rows for rebuilds, worktrees, dirty edits, versions and
conf keys, 25 of them, ran green on the prototype.

What the two do not check: wall time, disk reads, and a planner that holds `sqlite_stat` tables. In the
overlay half, a scan made by a SELECT ahead of the delete is not counted.

### Inventory

| Name | Kind | Naming cell |
|---|---|---|
| `remove_dead_holders` | function | `py.function`, answered OK by `lexicon.py --suggest` |
| `remove_released_rows` | function | `py.function`, answered OK by `lexicon.py --suggest` |
| `released` | temp table | none grades it |
| `released-rows`, `released-cost` | plants | none grades them |

### Migration

None. No stored table or key moves. The first build by this code clears what it releases.

### Files touched (estimate)

- `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`, `tools/playbook/adopt-playbook.sh`
- `tools/playbook/README.md`

### Alternatives rejected

- The full sweep moved to `--gc` alone, with a build clearing nothing. Every commit and edit would then
  leave rows behind, and the file would grow between collections.
- The overlay left as it is. Its replaced rows would stay until `--gc`, since no later set names them.
  The prototype's first break shows it: 5 path rows after one replaced edit and 20 after four.
- A Python loop asking per pair whether a holder remains. It makes the same seeks as the statements
  above, one call each.

## 5. Production-readiness checklist

- security: N/A — no new input, grant or write path. The index file stays derived and uncommitted.
- perf / scale: a sweep costs one seek per released pair and one per row it clears. An overlay whose
  worktree held no dirty row adds one read.
- error / empty / loading states: an empty set returns at once. The write lock, its 600 s wait and its
  refusal are unchanged, and a failed block rolls back whole.
- observability: unchanged. No line of `check` or of `--gc` moves.
- risks: clearing a row some worktree is served, which `released-rows` reds through its `lost` count.
  The second is the window between two commands of one worktree that section 4 names.
- testing: the two plants, each with its staged breaks, and the paired run of AC4.
- migration: none, as section 4 says.
- user docs: N/A — no command, line or refusal a user sees moves. The kit page gains S7's sentence.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant released-rows` runs, every step
  prints three zeros for `left` and two for `lost`, the dumps are equal, and it exits 0.
  Red when: `build_overlay` passes no set, so `left` counts 5 `path_row` rows after the second
  worktree's further edit, or the pair filter is absent, so `lost` is non-zero at the first step.
- **AC2** — When `python tools/playbook/gov_tag.py --fixture --plant released-cost` runs, each half's
  second count is at most twice its first, all three tables saw a delete in each half, and it exits 0.
  Red when: `build_index` or `build_overlay` calls `remove_unheld_rows`, so that half's count is about
  four times the first.
  figure: PINNED from the prototype; the plant derives its own counts.
- **AC3** — When `released-rows` inserts its three unheld rows, a `rebuild` of a new commit leaves them
  and `run_gc` clears them.
  Red when: `remove_dead_versions` calls `remove_released_rows` in place of the full sweep, so they stay.
- **AC4** — When `gov_tag.py check` runs four times, the BASE source and the unit's source in
  alternation, each from a fresh copy of one private index whose HEAD and compare-base trees are unbuilt
  and whose other trees include one no worktree stands on, the four outputs are byte-equal under `cmp`,
  and the unit's record names the seconds of every run, whole and inside the sweep.
  Red when: the unit's sweep clears a row the check is served, so a line of the output moves, or its
  seconds inside the sweep are no lower than BASE's.
  cost: about 4 GB of scratch disk and, from the diagnosis, some 15 minutes.
  fixture: the clean 270 MB copy the building session's scratch holds, padded with 12 dead versions for
  this criterion. Each source is loaded under the worktree's own `tag_index.py` path with
  `derive_index_path` answering the copy, so both derive one version and read one set of rows.
  figure: DERIVED at observation time.
- **AC5** — When `EXPLAIN QUERY PLAN` runs on that copy over the five statements of
  `remove_released_rows`, none names a scan of `tree_path`, `path_row`, `blob_row` or `blob_parsed`.
  Red when: the planner serves a clear from a scan of its table.
  fixture: the copy AC4 makes, opened through this code so units 1 and 2 are on it.
- **AC6** — When `grep -n "remove_unheld_rows" tools/playbook/tag_index.py` runs, its only lines that
  define or call it are the definition taking `con` alone and the call in `remove_dead_versions`. When
  `grep -c "let go of" tools/playbook/README.md` runs, it prints 1 or more.
  Red when: a build still calls the full sweep, or the kit page does not say what a build clears.
- **AC7** — When `python tools/playbook/gov_tag.py --fixture --plant <case>` runs for `two-paths`,
  `dirty-revert`, `worktree-recreate`, `worktree-spelling`, `charter-dirty`, `two-versions` and
  `queued-writers`, each exits 0.
  Red when: a pair two holders share loses its rows, a pruned worktree's dirty rows stay, or a write
  block no longer opens with the write lock.

## 7. Gates

`tags (the resolver's checks)` · `instruction edits (manifest checks)` · `edges (every declared edge parses, is registered and resolves)` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC3 · the `released-rows` row; staged red with `build_overlay` passing no set, with the pair filter absent, and with `remove_dead_versions` calling no full sweep · none
New arm: tools/playbook/adopt-playbook.sh · covers AC2 · the `released-cost` row; staged red with `remove_unheld_rows` called from `build_index`, and again from `build_overlay` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "delete index rows no tree or worktree holds any more"` named
`build_index`, `load_index` and `read_rows` of `tools/playbook/tag_index.py` and no other eviction seam.
The seams extended are `remove_unheld_rows`, split in two, `build_overlay`, `remove_dead_versions`, and
for the plants `write_commit`, `read_dump`, `run_gc`, `print_equal` and the plant table of
`tools/playbook/adopt-playbook.sh`. Unit 1's `read_step_count` does not fit `released-cost`: it counts
one read, and this plant counts the statements of two windows inside one `load_view`, where the parse
ledger a build reads would otherwise hide the sweep. Recall answered PLAY-dOrderedCharter-51 with its
deviation 513, TOOL-aQueuedIndex-1 and KICK-dKeptSession-87. The performance review of TOOL-aMeasuredDrag-1
proposed the sweep in `--gc` alone, which section 4 rejects.

Recall terms used: tag index sweep unheld rows tree_path dirty_path overlay path_row blob_row blob_parsed gc worktree eviction shared
