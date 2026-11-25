# TOOL-aPrunedIndex-1 — a read of the served rows starts from the reading worktree's own extractor versions

**Status:** SPECCED · rev-2 · 2026-11-25 · node a · Tier-2 · base 3d6c1702 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aPrunedIndex-1-chain-rounds.md](../build/2026-11-25-build-TOOL-aPrunedIndex-1-chain-rounds.md) | journal | — |
| [2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md](../build/2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md) | research | TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 |
| [2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md) | research | TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 |
| [2026-11-25-prompt-TOOL-aPrunedIndex-3-revision.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-3-revision.md) | research | TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-4 |
| [2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1.md](../reviews/2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1.md) | spec-audit | TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 |

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
  counts with, and the plant's row in `SELFTEST_ROWS` of `tools/playbook/tag_bundle.py`. That runner's
  printed label becomes `tag plant`, since its rows now name more than bundle plants. Observed by AC1, AC2
  and AC3.
- **S6** — The module docstring of `tools/playbook/tag_index.py` and the index paragraph of
  `tools/playbook/README.md` say that a whole-view read starts from the reading worktree's versions
  through `path_row_version`. The index paragraph of `help/tags.md` says that an open which finds an SQL
  index missing builds it once, under the write lock, and names the command of section 4's Rollout that
  builds it outside any leg. Observed by AC6.
- **S7** — `tools/playbook/tag_index.py#load_index` prints one line on stderr,
  `tag-index — building: <names>, once, under the write lock`, when the file it opens holds `path_row` and
  lacks an SQL index `SCHEMA` creates. It prints nothing on a new file or a complete one. Observed by AC8.

## 3. Non-goals (OUT)

- The name probe of a build, the parse ledger and the sweep. They are units 2 and 3.
- What `--gc` collects, and any automatic collection. The first is unit 4.
- A change to a row, to how a version is derived, to `INDEX_SCHEMA` or to the file's name.
- A temporary table holding the view, a write-ahead log, and planner statistics through `ANALYZE`.
- An edit to a caller of `read_rows`, `read_population`, `derive_namespace_state` or `read_defined`.
- A faster tag read. It keeps today's cost, which grows with the versions storing that one tag.
- Any open of either live index file. Every measurement runs on a private copy or a fixture.
- Any run, from the building worktree before the owner's go, of what opens the live index: the legs
  `tags (the resolver's checks)`, `instruction edits (manifest checks)`,
  `edges (every declared edge parses, is registered and resolves)` and `instruction units selftest`, and a
  `gov_tag.py` verb outside `--fixture`. Each would add the SQL indexes to the live file, and each later
  edit of `tag_index.py` would write another full set of rows. This unit is verified by `--fixture` plants
  and private copies alone.

### Edges

- **hands-off** `TOOL-aPrunedIndex-2` — the name probe of `_write_path_rows`. SQLite picks
  the version index for it once this unit lands, and the probe then walks the reading version's rows.
  Unit 2's partial index takes it back, so a tree holding this unit alone opens no shared index. Unit 2's
  plant counts with `read_step_count`, its index is named by S7's line, and its rollout is this unit's.
- **hands-off** `TOOL-aPrunedIndex-3` — `path_row_version` and the new joins, which unit 3's AC5, AC9 and
  section 4 plans rest on.
- **hands-off** `TOOL-aPrunedIndex-4` — the `dead-versions` row, one of the six unit 4's AC8 times.
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
the fixture's index and fills the view. `read_step_count(con, read)` runs the read once uncounted, then
again through `set_progress_handler` at one instruction, and returns the virtual-machine steps of the
second run and its result. The handler fires while a statement compiles too, and the first run takes that
cost out of the count. A step count is the same on every machine, and it counts a scan however SQLite
names it.

1. It counts five reads: `read_defined`, `read_rows` over the definitions, the same under a LIKE
   pattern, `derive_namespace_state` and `read_population`. Each must return something. It drops
   `path_row_version`, counts `read_defined` again as the bare count, and runs `SCHEMA` to put the index
   back.
2. It writes the dead pad: the fixture's own `path_row` rows copied under 40 further version names. The
   pad must have written rows. It counts the five again. Each must return what it returned before, in at
   most twice its steps.
3. On the same rows it drops `path_row_version` and counts `read_defined`. That count must exceed twice
   the bare count, which proves the dead rows reach the read, and twice the count of step 2, which proves
   the index is what hides them. It closes the connection and opens the file through `load_index`. The
   index must be back, the `path_row` count unchanged and the stamp `INDEX_SCHEMA`.
4. It fills the view again and counts one tag read. It writes 500 rows of the reading version at a path of
   the view under other tags, and counts again. The second count must be at most twice the first and the
   tag's row the same.

Step 4 comes last because its rows alone would carry step 3's count past twice the first. It prints one
line per count, and a last line ending `reads cost their own version's rows` only when every condition
holds. It exits 0 then, and 1 otherwise.

The counts of a prototype run in this sequence on the `none` fixture, 16 path rows before the pad, are
PINNED from 2026-11-25 with SQLite 3.53.4. Each cell is the count before the pad, then after it. The bare
column is `read_defined` with the index dropped. The plant took 8 to 22 s on a machine running other bars.

| Code | `read_defined` | definitions | LIKE | namespace state | bare | one tag, own pad |
|---|---|---|---|---|---|---|
| this unit | 303, 304 | 447, 448 | 310, 311 | 300, 301 | 463, 9184 | 1025, 1025 |
| BASE | 380, 11900 | 461, 10621 | 262, 7582 | 314, 10474 | 380, 11900 | 1025, 1025 |
| today's join, index present, no DISTINCT | 317, 10477 | 461, 10621 | 267, 7587 | 314, 10474 | 317, 10477 | 1025, 1025 |
| the new join, no index | 463, 9184 | 613, 9694 | 336, 7417 | 457, 9178 | 463, 9184 | 1025, 1025 |
| one join for every read | 303, 304 | 447, 448 | 310, 311 | 300, 301 | 463, 9184 | 151, 3651 |
| this unit, no dead pad | 303, 303 | 447, 447 | 310, 310 | 300, 300 | 463, 463 | 65, 65 |

The span population read 194 steps, then 193. What the plant does not check: wall time, disk reads, and a
planner that holds `sqlite_stat` tables. Under the new join a restored DISTINCT is as cheap after the pad
as before it, so AC6 greps it.

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

Each CREATE INDEX commits alone. An opener killed inside one, by a leg's ceiling or by hand, rolls that one
back with no row changed, keeps any index it finished, and leaves the next opener to start it again.

### Rollout

On each node, before the first bar that runs this code there, one command opens the index outside any leg:
`python tools/playbook/gov_tag.py where doc.build-method`, run from a worktree holding this code. No
ceiling binds it. It prints S7's line and builds both SQL indexes, in seconds on a small file and in some
minutes on a large one. It then builds that worktree's tree at its new extractor versions, as any first
command after such an edit does. `--rebuild` is not that command, since it drops every table. On the
building node the owner's go comes first, and until then the building worktree runs nothing that section 3
lists. A node that skips the step still converges: a leg that reaches its ceiling loses one index build and
the next opener starts it again. The legs section 3 lists have ceilings from 180 s to 420 s.

### Files touched (estimate)

- `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`, `tools/playbook/tag_bundle.py`
- `tools/playbook/README.md`, `help/tags.md`
- `memory/map/generated/symbols.json`, regenerated by `gen_map.py --write` for the new function

### Alternatives rejected

- An index on `(extractor, version, tag)`, which would serve the tag read as well. It loses the row order
  inside a version, and the whole-view read of the definitions took 1.622 s against 0.163 s on a copy of
  the same rows, warm. A cold disk makes those lookups dearer still.
- `INDEXED BY path_row_version` in place of the order. The plan is the same, and a reader whose index an
  older worktree's `--rebuild` dropped would refuse instead of reading slowly.
- One join for every read, for the table above.
- The plant's row in the tag resolver's plant table of `tools/playbook/adopt-playbook.sh`. The leg that runs
  it, `playbook render selftest`, has a 300 s ceiling, and the review's nine timed plants, at a mean of 4.5
  s, put its 95 rows at about 430 s. `tags bundle selftest` has the same ceiling, one reading of 22 s alone,
  and one run per plant however many rows read it.
- `ANALYZE`. Its statistics bind every reader of the shared file, older code included, and go stale.

## 5. Production-readiness checklist

- security: N/A — no new input, grant or write path. The index file stays derived and uncommitted.
- perf / scale: a whole-view read costs the view's rows. A write to `path_row` maintains one more index.
- error / empty / loading states: an empty view returns nothing, as today. A first open that cannot take
  the lock within 600 s raises the `cannot be opened` refusal that exists.
- observability: S7's line on stderr when an open builds an index. No line of `check` moves.
- risks: the first open holds the write lock for minutes on a large file, and a leg that meets it can reach
  its ceiling, whose killed build rolls back. The Rollout part of section 4 opens the file outside any leg
  first, and the owner is asked before that runs on the live file. The second risk is unit 2's probe, the
  first edge of section 3.
- testing: the plant, with four staged breaks, and the paired run of AC4. Unit 2's AC7 kills an opener.
- migration: the index is added at the next open, as the Migration and Rollout parts of section 4 say.
- user docs: `help/tags.md` gains the sentence S6 names.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant dead-versions` runs, each of its five
  whole-view reads returns the same before and after the dead pad, in at most twice the steps, and it
  exits 0.
  Red when: `VIEW_JOIN` alone takes back today's order, so `read_defined` goes from 317 steps to 10,477,
  or `path_row_version` leaves `SCHEMA`, so it goes from 463 to 9,184.
  figure: the break counts are PINNED from the prototype, each measured as staged; the plant derives its
  own.
- **AC2** — When `dead-versions` counts its tag read before and after 500 further rows of the reading
  version, the second count is at most twice the first and the row is the same.
  Red when: `read_rows` builds a tag read on `VIEW_ROWS`, so the second count is about 24 times the first.
- **AC3** — When `dead-versions` drops `path_row_version` over the dead pad, its count of `read_defined`
  exceeds twice the bare count and twice the count with the index. When it reopens the file through
  `load_index`, the index is back, the `path_row` count is unchanged and the stamp is 3.
  Red when: the dead pad reaches no read, so the count stays at the bare one, or `INDEX_SCHEMA` moves.
- **AC4** — When `gov_tag.py check` runs four times, the BASE source and the unit's source in alternation,
  over one private copy of the index whose HEAD and compare-base trees are built and which 12 dead
  versions pad, the four outputs are byte-equal under `cmp`, and the unit's record names the wall and the
  CPU seconds of every run.
  Red when: a join serves a row more or less, a tie changes a printed line, or the unit's CPU seconds are
  not below BASE's in each pair.
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
- **AC8** — When `dead-versions` reopens the file whose index it dropped, stderr carries one
  `tag-index — building:` line naming `path_row_version`. When it opens the complete file again, and when
  the fixture first creates its file, stderr carries none.
  Red when: `load_index` prints on every open, or builds a missing index in silence.

## 7. Gates

`tags (the resolver's checks)` · `instruction edits (manifest checks)` · `edges (every declared edge parses, is registered and resolves)` · `instruction units selftest` · `tags bundle selftest` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

Those of the line that open the live index, the four section 3 lists, are owed at the close, after the
owner's go, and by no pass before it.

New arm: tools/playbook/tag_bundle.py · covers AC1 AC2 AC3 AC8 · the `dead-versions` row; staged red four times, with `VIEW_JOIN` alone in today's order, with the `path_row_version` statement removed from `SCHEMA`, with `read_rows` building a tag read on `VIEW_ROWS`, and with the dead pad rolled back after its rows are counted · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft.
- rev-2 · 2026-11-25 · §2 §3 §4 §5 §6 §7 §10 S5 S6 S7 AC1 AC2 AC3 AC4 AC8 · folded
  `2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1`: finding 1 (step 3 proves the dead pad
  before the own rows land), 3 (AC4 reds on CPU), 5 and 8 and 11 (the edges to units 2 and 3), 7 (the
  break figure as staged), 10 (the uncounted first run, the bound and the re-pinned table), 12 (the plant's
  row moves to `tags bundle selftest`), 13 and 17 (S7, Rollout and the killed build), 14 (the legs that open
  the live index), 15 (the symbol map).

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "read the served rows of the tag index through an index on the
extractor version"` named `read_rows` and `build_index` of `tools/playbook/tag_index.py` and no row-index
or planner seam. The seams extended are `SCHEMA`, `VIEW_JOIN`, `VIEW_ROWS`, `read_rows` and
`read_defined`, and for the plant `build_tags_fixture`, `write_commit`, `run_plant` and the row table of
`tools/playbook/tag_bundle.py#run_selftest`. No existing seam fits the step count. A grep for
`set_progress_handler` and `EXPLAIN QUERY` over `tools/` found nothing at BASE, so `read_step_count` is
new. Recall answered KICK-dKeptSession-87, PLAY-dOrderedCharter-51 and TOOL-aQueuedIndex-1. Commit
`0200dd0cc` put `+p.tag` in two of the three sorted reads, and this unit keeps it.

Recall terms used: tag index shared worktree gc dead versions path_row tree_built sweep read_rows ceiling view_version
