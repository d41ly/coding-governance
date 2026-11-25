# TOOL-aPrunedIndex-1 — a read of the served rows starts from the reading worktree's own extractor versions

**Status:** SPECCED · rev-1 · 2026-11-25 · node a · Tier-2 · base 3d6c1702 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md](../build/2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md) | research | TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 |
| [2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md) | research | TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 |

<!-- /gen:spec-records -->

## 1. Goal

Every read of the whole served view scans the rows of every stored extractor version. On the node's
file that is 17.8 million rows to serve 423,156 (PINNED, the diagnosis, 2026-11-25). After this unit
such a read searches an index on the extractor version and visits the reading worktree's rows alone.
No row served, no order of rows and no verdict changes.

## 2. Scope (IN)

- **S1** — `tools/playbook/tag_index.py#SCHEMA` gains one statement, the index `path_row_version` over
  `path_row(extractor, version)`. `INDEX_SCHEMA` stays 3. An existing index file gains it at its next
  open, with no row changed. Observed by AC1 and AC3.
- **S2** — `tools/playbook/tag_index.py#VIEW_JOIN` starts from `view_version` and reaches `path_row` by
  `CROSS JOIN`, so SQLite may not reorder the two. `VIEW_ROWS` follows it with the same columns. Every
  read of the whole view is built on these two names and moves with them. Observed by AC1 and AC4.
- **S3** — Today's join text stays as a second name, `POINT_JOIN`, with `POINT_ROWS` beside it. The two
  reads that name one row set use `POINT_ROWS`: `tools/playbook/tag_index.py#read_rows` when its `tag`
  is given, and `tools/playbook/tag_bundle.py#read_node_spans`, which names a path. Observed by AC2 and
  AC5.
- **S4** — `tools/playbook/tag_index.py#read_defined` selects `p.tag` with no DISTINCT. Its caller gets
  the same set. Observed by AC6 and AC4.
- **S5** — A new plant, `dead-versions`, in `tools/playbook/gov_tag.py`, the helper `read_step_count` it
  counts with, and the plant's row in the tag resolver's plant table of
  `tools/playbook/adopt-playbook.sh`. Observed by AC1, AC2 and AC3.
- **S6** — The module docstring of `tools/playbook/tag_index.py` and the index paragraph of
  `tools/playbook/README.md` say that a whole-view read starts from the reading worktree's versions
  through `path_row_version`. The index paragraph of `help/tags.md` says that an open which finds an SQL
  index missing builds it once, under the write lock. Observed by AC6.

## 3. Non-goals (OUT)

- The name probe of a build, the parse ledger and the sweep. They are units 2 and 3.
- What `--gc` collects, and any automatic collection. The first is unit 4.
- A change to a row, to how a version is derived, to `INDEX_SCHEMA` or to the file's name.
- A temporary table holding the view, a write-ahead log, and planner statistics through `ANALYZE`.
- An edit to a caller of `read_rows`, `read_population`, `derive_namespace_state` or `read_defined`.
- A faster tag read. It keeps today's cost, which grows with the versions storing that one tag.
- Any open of either live index file. Every measurement runs on a private copy or a fixture.

### Edges

- **hands-off** `TOOL-aPrunedIndex-2` — the name probe of `_write_path_rows`. SQLite picks
  the version index for it once this unit lands, and the probe then walks the reading version's rows.
  Unit 2's partial index takes it back, so a tree holding this unit alone opens no shared index.
- **hands-off** external — the owner's word in the building session before this code first opens the
  live index.

## 4. Design

### Mechanism

The four builders of a whole-view read are `read_rows` with no tag, `read_population`,
`derive_namespace_state` and `read_defined`, all in `tools/playbook/tag_index.py`. A fifth read, the
`has_retired` probe of `tools/playbook/gov_tag.py#run_check`, takes `VIEW_ROWS` directly. A grep for
`path_row`, `VIEW_JOIN` and `VIEW_ROWS` over `tools/` found no other served read than these, the bundle's
`read_node_spans`, and one check inside the `extractor-edit` plant. So the two constants carry the change.

```sql
FROM view_version w CROSS JOIN path_row p ON p.extractor=w.extractor AND p.version=w.version
JOIN view_path v ON p.path=v.path AND p.blob=v.blob
JOIN view_conf c ON p.conf=c.conf
```

Both the index and the order are needed. With the index and today's join, SQLite still scans `path_row`.
With the `CROSS JOIN` and no index, it builds an automatic index over the whole table at each read.

`tools/playbook/tag_index.py#load_view` fills `view_version` before any read, and that temp table is keyed
by the extractor, so each extractor contributes one version and no row is served twice.

### Why a tag read keeps today's join

Under the `CROSS JOIN`, SQLite serves a read of one tag from `path_row_version` too, and walks the whole
view for it. On a private copy of 3,004,575 path rows in 7 versions, whose view holds 15,732 paths, the
times and plans below were read on 2026-11-25 with SQLite 3.53.4, warm. They are PINNED.

| Read | today | `CROSS JOIN` with the index |
|---|---|---|
| every definition, sorted | 1.117 s, `SCAN p` | 0.163 s, `SEARCH p USING INDEX path_row_version` |
| tags under a LIKE pattern | 0.852 s, `SCAN p` | 0.125 s, the same search |
| span population | 1.178 s, `SCAN p` | 0.177 s, the same search |
| `read_defined` with DISTINCT | 12.558 s, `SCAN p USING INDEX path_row_tag` | 0.168 s, the same search |
| one tag | 0.001 s, `SEARCH p USING INDEX path_row_tag` | 0.164 s, the same search |
| one path | under 0.001 s, `path_row_key` | 0.003 s, `path_row_key` once per extractor |

`tools/playbook/edge_grammar.py#read_tag_rows` makes one tag read per edge target that is a tag. This tree
holds 430 such targets (PINNED, 2026-11-25, counted through `read_tree_edges`). One join for every read
would add about 70 s to that leg, whose ceiling is 180 s. `POINT_JOIN` is today's text, and its plan is
unchanged on the copy that holds the index. A LIKE read is no point read, because `path_row_tag` cannot
serve it.

### What does not change

- The rows: both joins are inner joins over the same four conditions.
- The order: the sorted reads keep `ORDER BY +p.tag, p.path, p.line`. Rows equal on all three could come
  back in another order, so ties were counted on the clean copy. No two rows of the view that are neither
  spans nor bookkeeping share a tag, a path and a line. Tied spans are identical rows.
- The unsorted reads feed a count, a set, a truth test and a `max` whose ties are equal.
- A worktree on older code: the index sits in the file, SQLite maintains it for any writer, and the plans
  of today's whole-view reads did not move on the copy that holds it.

### The plant

`dead-versions` adds one citation of a declared tag to the fixture's guide, commits it, rebuilds, opens
the fixture's index and fills the view. `read_step_count(con, read)` returns the virtual-machine steps
of one read and the read's result, through `set_progress_handler` at one instruction. A step count is
the same on every machine, and it counts a scan however SQLite names it.

1. It counts five reads: `read_defined`, `read_rows` over the definitions, the same under a LIKE
   pattern, `derive_namespace_state` and `read_population`. Each must return something.
2. It writes the dead pad: the fixture's own `path_row` rows copied under 40 further version names. The
   pad must have written rows. It counts the five again. Each must return what it returned before, in at
   most twice its steps.
3. It counts one tag read, writes 500 rows of the reading version at a path of the view under other
   tags, and counts again. The two counts must be equal and the tag's row the same.
4. It drops `path_row_version` and counts `read_defined`. That count must exceed twice the first, which
   proves the pad reaches the read. It closes the connection and opens the file through `load_index`.
   The index must be back, the `path_row` count unchanged and the stamp `INDEX_SCHEMA`.

It prints one line per count, and a last line ending `reads cost their own version's rows` only when
every condition holds. It exits 0 then, and 1 otherwise. The prototype's counts on the `none` fixture,
15 path rows before the pad, are PINNED from 2026-11-25. Each cell is the count before the pad, then
after it.

| Code | `read_defined` | definitions | LIKE | namespace state | one tag, own pad |
|---|---|---|---|---|---|
| today | 378, 11538 | 460, 10300 | 265, 7254 | 312, 10152 | 820, 820 |
| this unit | 308, 309 | 455, 456 | 324, 301 | 305, 306 | 820, 820 |
| the join, no index | 467, 8868 | 620, 9381 | 347, 7089 | 461, 8862 | 820, 820 |
| one join for every read | 308, 309 | 455, 456 | 324, 301 | 305, 306 | 146, 3646 |

The fixture without the citation gave an empty population, so that read is not in the table and the plant
adds the citation. What the plant does not check: wall time, disk reads, and a planner that holds
`sqlite_stat` tables. Under the new join a restored DISTINCT costs 339 steps before the pad and 340 after,
so AC6 greps it.

### Inventory

| Name | Kind | Naming cell |
|---|---|---|
| `path_row_version` | SQL index | none grades it |
| `POINT_JOIN`, `POINT_ROWS` | module constants | none grades them |
| `read_step_count` | function | `py.function`, answered OK by `lexicon.py --suggest` |
| `dead-versions` | plant | none grades it |

### Migration

`tools/playbook/tag_index.py#load_index` runs `SCHEMA` at every open and each statement is
`IF NOT EXISTS`, so the first open after landing builds the index in place. The diagnosis measured this
index and unit 2's together at about 205 s under the write lock and 1 GB, on the 12.6 GB copy. A second
opener waits. Two openers of one 3,000,000-row file without the index both returned with it, the second
after 3.9 s (PINNED, 2026-11-25). `BUSY_TIMEOUT` is 600 s. The rebuild of a stale stamp splits `SCHEMA` on
`;`, and the statement holds none. An older worktree's `--rebuild` drops the index with its table, and the
next open under this code adds it back.

### Files touched (estimate)

- `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`, `tools/playbook/tag_bundle.py`
- `tools/playbook/adopt-playbook.sh`
- `tools/playbook/README.md`, `help/tags.md`

### Alternatives rejected

- An index on `(extractor, version, tag)`, which would serve the tag read as well. It loses the row order
  inside a version, and the whole-view read of the definitions took 1.622 s against 0.163 s on a copy of
  the same rows, warm. A cold disk makes those lookups dearer still.
- `INDEXED BY path_row_version` in place of the order. The plan is the same, and a reader whose index an
  older worktree's `--rebuild` dropped would refuse instead of reading slowly.
- One join for every read, for the table above.
- `ANALYZE`. Its statistics bind every reader of the shared file, older code included, and go stale.

## 5. Production-readiness checklist

- security: N/A — no new input, grant or write path. The index file stays derived and uncommitted.
- perf / scale: a whole-view read costs the view's rows. A write to `path_row` maintains one more index.
- error / empty / loading states: an empty view returns nothing, as today. A first open that cannot take
  the lock within 600 s raises the `cannot be opened` refusal that exists.
- observability: unchanged. No line of `check` moves.
- risks: the first open holds the write lock for minutes on the live file, and a leg with a 180 s or
  420 s ceiling that meets it would time out. The owner is asked before it runs. The second risk is unit
  2's probe, the first edge of section 3.
- testing: the plant, with three staged breaks, and the paired run of AC4.
- migration: the index is added at the next open, as the Migration part of section 4 says.
- user docs: `help/tags.md` gains the sentence S6 names.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant dead-versions` runs, each of its five
  whole-view reads returns the same before and after the dead pad, in at most twice the steps, and it
  exits 0.
  Red when: `VIEW_JOIN` takes back today's order, so `read_defined` goes from 378 steps to about 11,500,
  or `path_row_version` leaves `SCHEMA`, so it goes to about 8,900.
  figure: the two break counts are PINNED from the prototype; the plant derives its own.
- **AC2** — When `dead-versions` counts its tag read before and after 500 further rows of the reading
  version, the two counts are equal and the row is the same.
  Red when: `read_rows` builds a tag read on `VIEW_ROWS`, so the second count is about 25 times the first.
- **AC3** — When `dead-versions` drops `path_row_version`, its count of `read_defined` exceeds twice the
  first. When it reopens the file through `load_index`, the index is back, the `path_row` count is
  unchanged and the stamp is 3.
  Red when: the pad reaches no read, so the count stays, or `INDEX_SCHEMA` moves.
- **AC4** — When `gov_tag.py check` runs four times, the BASE source and the unit's source in alternation,
  over one private copy of the index whose HEAD and compare-base trees are built and which 12 dead
  versions pad, the four outputs are byte-equal under `cmp`, and the unit's record names the wall and the
  CPU seconds of every run.
  Red when: a join serves a row more or less, or a tie changes a printed line.
  cost: about 4 GB of scratch disk and, from the diagnosis, some 10 minutes.
  fixture: a padded copy of the clean 270 MB copy the building session's scratch holds, made for this
  criterion. Each source is loaded under the worktree's own `tag_index.py` path with
  `derive_index_path` answering the copy, so both derive one version and read one set of rows.
  figure: DERIVED at observation time.
- **AC5** — When `EXPLAIN QUERY PLAN` runs on that copy over `POINT_ROWS` with `p.tag=?` and with
  `p.path=?`, and over `VIEW_ROWS` with `p.kind='tag'`, it names `path_row_tag`, `path_row_key` and
  `path_row_version`. When `grep -n "POINT_ROWS" tools/playbook/tag_bundle.py` runs, it prints the query of
  `read_node_spans`.
  Red when: a narrowed read is served from `path_row_version`, or the bundle keeps `VIEW_ROWS`.
  fixture: the copy AC4 makes.
- **AC6** — When `grep -c "DISTINCT p.tag" tools/playbook/tag_index.py` runs, it prints 0. When
  `grep -c path_row_version` runs over `tools/playbook/tag_index.py` and `tools/playbook/README.md`, the
  first prints 2 or more and the second 1 or more. When `grep -n "SQL index" help/tags.md` runs, it prints
  the sentence S6 names.
  Red when: `read_defined` asks for DISTINCT again, or a page still describes the join alone.
- **AC7** — When `python tools/playbook/gov_tag.py --fixture --plant <case>` runs for `two-versions`,
  `served-across`, `extractor-edit`, `charter-dirty` and `bundle-manifest`, each exits 0.
  Red when: the new join serves another version's or another conf's rows, or drops one of its own.

## 7. Gates

`tags (the resolver's checks)` · `instruction edits (manifest checks)` · `edges (every declared edge parses, is registered and resolves)` · `tags bundle selftest` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 · the `dead-versions` row; staged red three times, with `VIEW_JOIN` in today's order, with the `path_row_version` statement removed from `SCHEMA`, and with `read_rows` building a tag read on `VIEW_ROWS` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "read the served rows of the tag index through an index on the
extractor version"` named `read_rows` and `build_index` of `tools/playbook/tag_index.py` and no row-index
or planner seam. The seams extended are `SCHEMA`, `VIEW_JOIN`, `VIEW_ROWS`, `read_rows` and
`read_defined`, and for the plant `build_tags_fixture`, `write_commit`, `run_plant` and the plant table of
`tools/playbook/adopt-playbook.sh`. No existing seam fits the step count. A grep for
`set_progress_handler` and `EXPLAIN QUERY` over `tools/` found nothing at BASE, so `read_step_count` is
new. Recall answered KICK-dKeptSession-87, PLAY-dOrderedCharter-51 and TOOL-aQueuedIndex-1. Commit
`0200dd0cc` put `+p.tag` in two of the three sorted reads, and this unit keeps it.

Recall terms used: tag index shared worktree gc dead versions path_row tree_built sweep read_rows ceiling view_version
