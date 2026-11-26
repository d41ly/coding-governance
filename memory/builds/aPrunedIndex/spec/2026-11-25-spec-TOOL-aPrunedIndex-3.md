# TOOL-aPrunedIndex-3 — a build's sweep touches only the rows that the trees and gone worktrees' edits it lets go of held

**Status:** CLOSED · rev-4 · 2026-11-26 · node a · Tier-2 · base 3d6c1702 · streams tooling · order 3 · ratified 2026-11-25

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md](../build/2026-11-25-build-TOOL-aPrunedIndex-1-diagnosis.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-4 |
| [2026-11-26-build-TOOL-aPrunedIndex-1-timings.md](../build/2026-11-26-build-TOOL-aPrunedIndex-1-timings.md) | journal | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 |
| [2026-11-26-build-TOOL-aPrunedIndex-3-1-acceptance-ledger.md](../build/2026-11-26-build-TOOL-aPrunedIndex-3-1-acceptance-ledger.md) | journal | — |
| [2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-1-brief.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-4 |
| [2026-11-25-prompt-TOOL-aPrunedIndex-3-1-spec-writer.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-3-1-spec-writer.md) | journal | — |
| [2026-11-25-prompt-TOOL-aPrunedIndex-3-revision.md](../prompts/2026-11-25-prompt-TOOL-aPrunedIndex-3-revision.md) | research | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-4 |
| [2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1.md](../reviews/2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1.md) | spec-audit | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-4 |
| [2026-11-26-review-TOOL-aPrunedIndex-1-2-3-4-diff-review-round1.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-1-2-3-4-diff-review-round1.md) | diff-review | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-4 |
| [2026-11-26-review-TOOL-aPrunedIndex-1-2-3-spec-audit-round1.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-1-2-3-spec-audit-round1.md) | spec-audit | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 |

<!-- /gen:spec-records -->

## 1. Goal

Every build of an unbuilt tree ends by scanning the whole of `path_row`, `blob_row` and `blob_parsed`
for rows nothing holds. On the 12.6 GB copy two such sweeps took 537 s of one check, and the rows they (PINNED, 2026-11-25)
scan are mostly those of dead extractor versions (PINNED, the diagnosis, 2026-11-25). After this unit a
build looks only at the rows that the trees and the gone worktrees' edits it lets go of held. An overlay
clears none of those three tables, as today. The rows only a replaced edit held wait for `--gc`, which
keeps the full sweep. No row that a tree or an edit holds is cleared. Because those rows are kept, an
overlay now keys each edit by the very bytes it parses, so a kept row is right when its content comes back.

## 2. Scope (IN)

- **S1** — A new function, `remove_dead_holders`, in `tools/playbook/tag_index.py` carries the first
  half of today's `remove_unheld_rows`: the trees no worktree's HEAD names, and the dirty rows of
  worktrees that are gone. It returns the set of (path, blob) pairs they held. Observed by AC1.
- **S2** — A new function, `remove_released_rows`, in the same module takes such a set and clears the
  rows of those pairs, and of those blobs, that no remaining tree or dirty row holds. It clears them
  at every version and every conf key. Observed by AC1, AC2 and AC5.
- **S3** — `tools/playbook/tag_index.py#build_index` ends its write block with S2 over S1's set.
  Observed by AC1 and AC2.
- **S4** — `tools/playbook/tag_index.py#build_overlay` reads each changed file's bytes once, before the
  write lock, keys the file by the blob of those bytes, and parses those bytes. A file whose bytes cannot be
  read refuses the overlay, naming it, and no row moves. Bytes that are not UTF-8 are recorded with no text,
  as today. What the overlay clears is unchanged: it takes out its own worktree's dirty rows and nothing
  else, and the rows only an old edit of that worktree held stay until the full sweep of a collection.
  Observed by AC1, AC3, AC8 and AC10.
- **S5** — `remove_unheld_rows` keeps the full sweep alone, as `remove_unheld_rows(con)`, and
  `tools/playbook/tag_index.py#remove_dead_versions` calls S1 and then it. Observed by AC3.
- **S6** — Two new plants, `released-rows` and `released-cost`, in `tools/playbook/gov_tag.py`, each with
  its row in `SELFTEST_ROWS` of `tools/playbook/tag_bundle.py`. Observed by AC1, AC2, AC3, AC8, AC10 and AC11.
- **S7** — The docstrings of S1, S2, S3 and S5's functions, and the index paragraph of
  `tools/playbook/README.md`, say that a build clears only what the trees and the gone worktrees' dirty
  rows it lets go of held, and that the rows of an old edit wait for `--gc`, which alone sweeps the row
  tables whole. The `--gc` sentence of `help/tags.md` says that it collects the rows of old uncommitted
  edits too. Observed by AC6.

## 3. Non-goals (OUT)

- Which trees and dirty rows a build lets go of. The rule of `read_worktree_trees` and `keep` stays.
- Clearing a replaced edit's rows when it is replaced, which section 8's F1 rules out.
- The rows of a dead extractor version that a live tree still holds. `--gc` collects those.
- The served reads, the name probe and the parse ledger, which are units 1 and 2, and which worktrees
  `--gc` reads, which is unit 4.
- Any change to a command that reads a view, and a lock or a transaction held across its reads.
- The `git rev-parse` per worktree inside `read_worktree_trees`, which runs under the write lock. Its
  cost follows the count of worktrees, not the stored versions.
- The `SELECT DISTINCT tree FROM tree_path` that lists the trees. It reads one key index, and its cost
  follows the trees held.
- A new SQL index, a schema change, or a stored table of released pairs.
- A retry of a file the overlay cannot read, and a held or locked file. It refuses, as a failed
  `git hash-object` does today.
- A content filter that changes more than line ends between the working file and its blob. The overlay
  parses the working bytes with CRLF folded, as today, and this repository declares no such filter.
- Any open of either live index file before the owner's go. The owner gave it on 2026-11-25, in
  `2026-11-25-prompt-TOOL-aPrunedIndex-3-revision`, on three conditions: all four units are built and
  measured on private copies, the closing review is clean, and the open comes before the bar. Every
  measurement here runs on a private copy or a fixture.
- Any run, from the building worktree before that go, of what opens the live index: the legs
  `tags (the resolver's checks)`, `instruction edits (manifest checks)`,
  `edges (every declared edge parses, is registered and resolves)` and `instruction units selftest`, and a
  `gov_tag.py` verb outside `--fixture`. This unit is verified by `--fixture` plants and private copies.

### Edges

- **consumes-from** `TOOL-aPrunedIndex-1` — `path_row_version` and the new joins. AC5's copy, the plans of
  section 4 and AC9's whole check rest on them, and `released-cost` proves its pad with that unit's
  `read_step_count`. Section 4's Rollout adds one step to that unit's.
- **consumes-from** `TOOL-aPrunedIndex-2` — `path_row_named`, for AC5, the plans and AC9.
- **hands-off** `TOOL-aPrunedIndex-4` — `remove_dead_holders` and `remove_unheld_rows(con)`, which its
  `--gc` runs through, and the `released-rows` and `released-cost` rows its AC8 times.
- **consumes-from** external — the owner's go for this code's first open of the live index, on the
  conditions the list above states.

## 4. Design

### Evidence

`tools/playbook/tag_index.py@4b10fce5d:825-843` is the whole of today's sweep. It has two callers,
`build_index` and `remove_dead_versions` (`tools/playbook/tag_index.py@4b10fce5d:805,925`), and a grep
over `tools/` found no other. `build_overlay` replaces its worktree's dirty rows
(`tools/playbook/tag_index.py@4b10fce5d:875-876`) and sweeps nothing.

Today's `tools/playbook/tag_index.py#build_overlay` reads each file twice. It hashes the path in its entries loop, takes the write lock, which
can wait 600 s, and only then reads the bytes it parses. A save in between stores one text under another (PINNED, 2026-11-25)
text's blob, and a failed read stores the blob as parsed with no rows. Today the next build of an unbuilt
tree clears such rows once the edit is replaced. Under S3 they would stay, and no later run would parse the
blob again, so S4 closes the gap that made them.

A row of the three tables can stop being held in four ways only.

1. A `tree_path` row goes when its tree is let go of. S1 names its pair.
2. A `dirty_path` row goes when its worktree is gone. S1 names its pair.
3. A `dirty_path` row goes when its own worktree's overlay is recorded again. No set names its pair, and
   its rows wait for `--gc`.
4. A build rewrites one tree's `tree_path` rows at its top
   (`tools/playbook/tag_index.py@4b10fce5d:800-801`). A tree id is a content hash, so that rewrite puts
   back the rows it took out.

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
4. `remove_dead_versions` calls `remove_dead_holders(con, root)` and then `remove_unheld_rows(con)`,
   whose statements are today's three, byte for byte.
5. `build_overlay` takes each changed file's bytes with one `read_bytes` in its entries loop. The blob is what
   memory-tree's `tools/memory-tree/tree_lib.py#read_git_output` answers for
   `git hash-object --stdin --path <path>` over those bytes, so the path's filters apply. It decodes the held
   bytes there too, folding CRLF, and `_write_parsed` is handed that map. Its own `read_text` goes, and no
   file is opened again. An `OSError` from either call becomes a `TagError` naming the path. Both forms of
   `hash-object` answered one id on 2026-11-26 over CRLF text, `eol=lf`, `-text` and `ident` files and one in a
   subfolder, under `core.autocrlf` true, false and input, and under true over an index blob holding CRLF. The
   overlay still makes one git call per changed file.

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

The last row is the equivalence read on that copy, which held no edit: the full sweep found nothing the
five left behind. The dirty half of each `EXISTS` scans `dirty_path`, once per pair no tree holds. That
table holds the uncommitted edits of the node's worktrees and no version, and a comment in the code names
that ceiling and an index on its blob as the way past it.

### What does not change

- What a worktree is served. `load_view` fills its view from `tree_path` and `dirty_path`, and a row is
  cleared only when neither table holds its pair.
- A command that reads while others write. A build clears a subset of what today's clears and an overlay
  clears nothing, so a reader keeps every row it keeps today. A reader of a tree or a worktree that a
  build elsewhere lets go of can still read no row, as today.
- A worktree on older code. Its builds run the full sweep over the same file, which clears only rows
  nothing holds, under the same write lock. That wait is a cost, and Rollout prices it.

### What it leaves

Three kinds of row that nothing holds stay until a `--gc`, or until a build by a worktree on older code.

- The rows of a replaced edit: an edit some command recorded, which its worktree then edited again,
  reverted or committed over. They stand in all three tables at that worktree's versions and conf key.
  Today the next build of an unbuilt tree by any worktree clears them.
- The `path_row` rows alone of a replaced edit whose blob a tree held at another path and then let go of.
  That build clears the blob's `blob_row` and `blob_parsed` rows.
- A legacy orphan: a row nothing held before this code ran, such as one an older worktree's overlay left.

No view holds such a pair, so none serves its rows. When the pair is held again its rows are right. They
are keyed by content, version and conf, S4 makes the content the bytes that were parsed, and a blob with no
`blob_parsed` row is parsed again. A row an overlay of older code stored wrongly is not served here: it
stands at that code's versions, and every extractor's import closure holds `tag_index.py`, so this unit's
edit moves every version (read through `import_walk.derive_module_closure`, 2026-11-26). A build that lets go
of a tree or a gone worktree holding the same pair clears it sooner.

The cost is one file's rows per replaced edit that some command recorded. An edit no command saw costs
nothing. Read from the clean copy on 2026-11-26, PINNED, at one version of each extractor:

| File | `path_row` | `blob_row` | `blob_parsed` |
|---|---|---|---|
| `AGENTS.md`, the charter | 96 | 94 | 2 |
| `memory/guides/BUILD-METHOD.md` | 49 | 47 | 2 |
| `memory/guides/UNATTENDED-PROTOCOL.md` | 144 | 142 | 2 |

Over the paths of that copy's HEAD tree, not over edits, `path_row` alone has a mean of 28 a path and 2,010
for the largest. How many edits a day are recorded and then replaced is unmeasured, since the index keeps no
count of them. Unit 4 lets the `--gc` that clears the rows run on this node.

### The plants

**`released-rows`** grades exactness, in the fixture's repository with two linked worktrees. After each
step it opens the index, takes the write lock, reads two counts, and rolls back.

- `left`: how many rows of each table the full sweep `remove_unheld_rows` would clear now.
- `lost`: `path_row` rows of a held pair whose blob, extractor and version have no `blob_parsed` row, and
  held paths under `memory/guides/` whose blob has a `blob_parsed` row no `path_row` row answers.

`lost` is zero after every step. `left` is zero after steps 1 to 7, 14 and 17, and after each other step but
15 it equals the rows named there, which the plant counts by blob while the edit is held. Those must be above
zero in each table, but for the bytes of step 16, which leave no `blob_row` row. ALPHA and BETA are two
guides, and a short word is the text a guide then holds. Each step but 15 ends with a `rebuild` by the
worktree that moved.

| Step | What moves | `left` |
|---|---|---|
| 1 | the two guides stand at one text, then ALPHA is committed apart | zero |
| 2 | the two worktrees are added, and the main one commits ALPHA at `e1` | zero |
| 3 | the second edits ALPHA to `e1`, the third edits BETA to `f1` | zero |
| 4 | the main one commits ALPHA at `f1`, so only an edit holds ALPHA at `e1` | zero |
| 5 | the main one commits ALPHA at `f2`, so only BETA's edit holds the blob of `f1` | zero |
| 6 | the third is removed and pruned, and the main one commits ALPHA | zero |
| 7 | the main one edits ALPHA to `g1`, and a connection loads that view and reads `doc.alpha#intro` | zero |
| 8 | the main one edits ALPHA to `g2` | `g1` |
| 9 | the second reverts `e1`, commits and builds | `g1`, `e1` |
| 10 | the main one reverts ALPHA and commits BETA at `g1` | `g2`, `e1`, and the path rows of `g1` |
| 11 | the main one commits BETA on | the same |
| 12 | the main one edits ALPHA to `g1` again | `g2`, `e1` |
| 13 | it reverts, one row is put in each table at the live version for a blob nothing holds, and it commits ALPHA | `g1`, `g2`, `e1`, and those three rows |
| 14 | the second is moved onto the main one's commit, and `run_gc` runs | zero |
| 15 | the main one edits ALPHA three times, and each time a second text is saved while the overlay runs: just before it reads the file, just after, and as it takes the write lock. Each of the six texts is then put back and read | not read |
| 16 | the main one edits ALPHA to `k1` and its read fails, then ALPHA holds bytes that are not UTF-8, then `h3` | the six texts of step 15, and the rows of those bytes |
| 17 | it reverts, commits ALPHA at the first text of step 15's last race and BETA at `k1`, the second is moved onto that commit, and `run_gc` runs | zero |

After step 9 the connection of step 7 reads `doc.alpha#intro` again, and must be served the text of `g1`
as before. After steps 14 and 17 `read_dump` must equal `read_cold_dump`, through the plant runner's
`print_equal`. The dump follows the collection because it counts a row nothing holds.

Step 15 wraps `pathlib.Path.read_bytes` for ALPHA and sets a trace callback that acts on `BEGIN IMMEDIATE`,
so it stages a race against any order of hash, read and lock. Each put-back text must be the text
`doc.alpha#intro` is served. In step 16 the failed read is a `PermissionError` from the same wrapper. The
view must raise a `TagError` naming ALPHA, the three tables' counts and the dirty rows must not move, and
the bytes must be recorded with a `blob_parsed` row and no refusal. It prints one line per step. It exits 0,
with a last line ending `only replaced edits left, and nothing lost`, only when every condition holds.

A prototype was green on 2026-11-26, with both SQL indexes in its `SCHEMA`. Steps 1 to 14 took 30 s and all (PINNED, 2026-11-25)
17 took 85 s, on a busy machine. It was red on each of fifteen breaks: (PINNED, 2026-11-25)

| Break | First step that reds |
|---|---|
| the overlay releases the pairs it replaces | 8, `left` zero, and the open view of step 9 emptied |
| the full sweep in the build | 9, `left` short of `g1`, and the open view emptied |
| no pair filter | 1, `lost` |
| no blob filter | 1, `lost` |
| the pair filter without its dirty half | 4, `lost` |
| the blob filter without its dirty half | 5, `lost` |
| no set from a gone worktree | 6, `left` |
| no set from a tree | 1, `left` |
| `blob_row` left uncleared | 6, `left` |
| `--gc` without the full sweep | 14, `left` |
| today's overlay, whole | 15, the first texts of the save before the read and of the save at the lock served wrong; 16 and 17 red too |
| the path hashed, then the bytes read, both before the lock | 15, the save before the read |
| the bytes read, then the path hashed | 15, the save after the read |
| a failed read recorded with no text | 16, no refusal, and 17, the dump |
| bytes that are not UTF-8 refused | 16, the refusal |

Twenty existing plants over rebuilds, worktrees, dirty edits, versions, schemas and conf keys, AC7's seven
among them, ran green on the prototype of S1 to S3. `dirty`, `dirty-revert`, `dirty-rename`,
`charter-dirty`, `worktree-recreate` and `queued-writers` ran green on the one that holds S4 too.

**`released-cost`** grades cost. It counts virtual-machine steps with `set_progress_handler` at one
instruction, over the statements of one `load_view` of a new commit that `set_trace_callback` shows from
the `tree_built` insert to its `COMMIT`. That window is the build's sweep.

It counts a first commit, then pads the index with the rows of one held file under 40 further version
names in all three tables, then counts a second commit of the same shape. The second count must be at most
twice the first. Each must have run a delete on all three tables, which is what keeps a build that sweeps
nothing from passing. Ahead of each it counts `remove_unheld_rows` through `read_step_count` in a block it
rolls back, and that count after the pad must exceed twice the one before it, which proves the pad is
rows a sweep can walk. The last line ends `a sweep costs what was released`.

The prototype's counts are PINNED from 2026-11-26. The full sweep alone read 469, then 5,029, and the
plant took 6 s. (PINNED, 2026-11-25)

| Code | before the pad | after it |
|---|---|---|
| this unit | 1395 | 1395 |
| the full sweep in the build | 1228 | 5788 |

What the two do not check: wall time, disk reads, and a planner that holds `sqlite_stat` tables.

### Inventory

| Name | Kind | Naming cell |
|---|---|---|
| `remove_dead_holders` | function | `py.function`, answered OK by `lexicon.py --suggest` |
| `remove_released_rows` | function | `py.function`, answered OK by `lexicon.py --suggest` |
| `released` | temp table | none grades it |
| `released-rows`, `released-cost` | plants | none grades them |

### Migration

None. No stored table or key moves. The first build by this code clears what it releases.

### Rollout

One step follows unit 1's: the worktrees of the node that run bars are brought onto this code. A worktree on
older code still runs the full sweep inside the write lock when it builds an unbuilt tree, and every check
takes that lock at its overlay, with no edit to record too, and waits up to `BUSY_TIMEOUT`, 600 s. The (PINNED, 2026-11-25)
diagnosis measured two such sweeps at 537 s, and the leg's ceiling is 420 s. On 2026-11-26 100 of the node's (PINNED, 2026-11-25)
104 worktrees held the old sweep (PINNED, the count of `2026-11-26-review-TOOL-aPrunedIndex-1-2-3-spec-audit-round1`). So
the leg fits its ceiling on a machine whose other writers run this code, and until the active worktrees do,
a check beside an older build can still be killed waiting. No row and no verdict is wrong in either state.

### Files touched (estimate)

- `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`, `tools/playbook/tag_bundle.py`
- `tools/playbook/README.md`, `help/tags.md`
- `memory/map/generated/symbols.json`, regenerated by `gen_map.py --write` for the new functions
- `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-3-1-acceptance-ledger.md`, the
  acceptance ledger, one line per criterion

### Alternatives rejected

- The full sweep moved to `--gc` alone, with a build clearing nothing. Every commit would then leave rows
  behind, and the file would grow between collections by far more than replaced edits.
- The overlay releasing the rows of the edit it replaces. It opens a window in which a running check of
  the same worktree reads no row for that file, the audit's finding 16, and section 8's F1 rules it out.
- The overlay's release put off by a generation, so a running command keeps its rows. It needs a stored
  table of released pairs, which section 3 rules out.
- The plants' rows in `tools/playbook/adopt-playbook.sh`, for the leg time unit 1 states.
- Re-hashing the path after the bytes are read. A save between the read and the second hash still parts
  them, and an overlay that wrote no rows on a mismatch would serve the file as defining nothing.
- A read that fails retried, or recorded with no text. The first hides a held file behind a wait, and the
  second marks the blob parsed with no rows, which nothing parses again.
- A Python loop asking per pair whether a holder remains. It makes the same seeks as the statements
  above, one call each.

## 5. Production-readiness checklist

- security: N/A — no new input, grant or write path. The index file stays derived and uncommitted.
- perf / scale: a sweep costs one seek per released pair and one per row it clears. The file grows by one
  file's rows per replaced edit, in all three tables, until a `--gc`. Section 4 sizes one edit, and the rate of
  them is unmeasured. A whole-view read walks those of its own version alone, and drops them in its join.
- error / empty / loading states: an empty set returns at once. The write lock, its 600 s wait and its (PINNED, 2026-11-25)
  refusal are unchanged, and a failed block rolls back whole. A changed file that cannot be read refuses
  before the write block, naming the file.
- observability: N/A — no line of `check` or of `--gc` moves.
- risks: clearing a row some worktree is served, which `released-rows` reds through its `lost` count. The
  second is a node whose `--gc` nobody runs, where replaced edits accumulate as dead versions do today. The
  third is the wait behind a worktree on older code, whose sweep can hold the write lock past the leg's
  ceiling. Section 4's Rollout prices it and names the step that ends it. The fourth is a leg that is the
  first to parse at a new version, which AC9 records apart.
- testing: the two plants, each with its staged breaks, and the runs of AC4 and AC9.
- migration: none, as section 4 says.
- user docs: the `--gc` sentence of `help/tags.md` and the kit page, as S7 says.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant released-rows` runs, every step of
  section 4's table prints its `left` and two zeros for `lost`, the dumps are equal, and it exits 0.
  Red when: `build_overlay` releases the pairs it replaces, so `left` is zero at step 8, or the pair filter
  is absent, so `lost` is non-zero at step 1, or no set comes from a gone worktree, so `left` is non-zero
  at step 6.
  cost: 85 s for the prototype, on a machine running other bars. (PINNED, 2026-11-25)
- **AC2** — When `python tools/playbook/gov_tag.py --fixture --plant released-cost` runs, the sweep's
  second count is at most twice its first, each saw a delete on all three tables, the full sweep's own
  count more than doubled over the pad, and it exits 0.
  Red when: `build_index` calls `remove_unheld_rows`, so the second count is over four times the first, or
  the pad writes rows no sweep walks.
  figure: PINNED from the prototype; the plant derives its own counts.
- **AC3** — When `released-rows` reaches step 13, a `rebuild` of a new commit leaves the rows of the three
  replaced edits and the three inserted rows. After `run_gc` in step 14 `left` is zero.
  Red when: `remove_dead_versions` calls `remove_released_rows` in place of the full sweep, so they stay.
- **AC4** — When `gov_tag.py check` runs four times, the BASE source and the unit's source in
  alternation, each from a fresh copy of one private index whose HEAD and compare-base trees are unbuilt
  and whose other trees include one no worktree stands on, the four outputs are byte-equal under `cmp`,
  and the unit's record names the seconds of every run, whole and inside the sweep.
  Red when: the unit's sweep clears a row the check is served, so a line of the output moves, or its
  seconds inside the sweep are no lower than BASE's.
  cost: about 4 GB of scratch disk and, from the diagnosis, some 15 minutes.
  fixture: the clean 270 MB copy the building session's scratch holds, padded with 12 dead versions for (PINNED, 2026-11-25)
  this criterion. Each source is loaded under the worktree's own `tag_index.py` path with
  `derive_index_path` answering the copy, so both derive one version and read one set of rows.
  figure: DERIVED at observation time.
- **AC5** — When `EXPLAIN QUERY PLAN` runs on that copy over the five statements of
  `remove_released_rows`, none names a scan of `tree_path`, `path_row`, `blob_row` or `blob_parsed`.
  Red when: the planner serves a clear from a scan of its table.
  fixture: the copy AC4 makes, opened through this code so the indexes of units 1 and 2 are on it.
- **AC6** — When `grep -n "remove_unheld_rows" tools/playbook/tag_index.py` runs, its only lines that
  define or call it are the definition taking `con` alone and the call in `remove_dead_versions`. When
  `grep -c "let go of" tools/playbook/README.md` runs, it prints 1 or more. When
  `grep -c "old edit" tools/playbook/README.md` and
  `grep -c "old uncommitted" help/tags.md` run, each prints 1 or more.
  When a Python probe reads `ast.get_docstring` of each function of `tools/playbook/tag_index.py`, runs of
  whitespace collapsed to one space, the docstring of `build_index` holds `let go of` and not
  `rows no tree or worktree holds are removed`. Those of `remove_dead_holders` and `remove_released_rows`
  each hold `let go of`. Those of `remove_unheld_rows` and `remove_dead_versions` each hold `old edit`, and the
  last does not hold `as a build's sweep does`.
  Red when: a build still calls the full sweep, or a page or a docstring does not say what a build clears and
  what waits for `--gc`.
- **AC7** — When `python tools/playbook/gov_tag.py --fixture --plant <case>` runs for `two-paths`,
  `dirty-revert`, `worktree-recreate`, `worktree-spelling`, `charter-dirty`, `two-versions` and
  `queued-writers`, each exits 0.
  Red when: a pair two holders share loses its rows, a pruned worktree's dirty rows stay, or a write
  block no longer opens with the write lock.
- **AC8** — When `released-rows` reads `doc.alpha#intro` through the connection of step 7 again after step
  9, once its edit is replaced and another worktree has built a new tree, it is served the text it was
  served in step 7, which holds `g1`.
  Red when: the overlay releases the pair it replaces, or the build runs the full sweep, so the connection
  is served nothing.
- **AC9** — When `gov_tag.py check` runs twice with the unit's source over a private copy of the 12.6 GB index
  on which both SQL indexes stand, the second run finishes below 420 s of wall. Before the first run the (PINNED, 2026-11-25)
  HEAD and compare-base trees are unbuilt and no `blob_parsed` row stands at the unit's version, so it parses
  every blob. Before the second the two trees' `tree_path` and `tree_built` rows at that digest are taken out
  again, so it builds both trees and its summary prints 0 blobs parsed. The unit's record names, for each
  run, its wall and CPU seconds, the `blobs parsed` and `skipped as fresh` figures of its summary, and the
  load of the machine.
  Red when: a read, a name probe or a sweep still walks the dead versions, so the second run passes the
  ceiling, or the second run's summary counts a parsed blob, so the two runs timed one workload.
  cost: 12.6 GB of scratch disk, about 205 s for the two indexes, and from the diagnosis about 122 s for the (PINNED, 2026-11-25)
  second run, which skipped 15,106 blobs as fresh. The first run's cost has no measured basis.
  fixture: the 12.6 GB copy the building session's scratch holds, copied once more or restored after, with
  `derive_index_path` answering it as in AC4.
  figure: the ceiling is DERIVED from the `ceiling` of the leg in `tools/gate-legs.json`; the seconds are
  DERIVED at observation time. The ceiling binds the second run. The first run is recorded and bound by
  nothing, because unit 1's Rollout command does that parse outside any leg. A later edit of an extractor's
  import closure brings it back, to the first command at the new version. Neither run observes the wait
  behind a worktree on older code, since a private copy has no other writer.
- **AC10** — When `released-rows` runs steps 15 to 17, each of the six texts is served as itself once it is
  put back, the failed read raises a `TagError` naming ALPHA with no row moved, the bytes that are not UTF-8
  are recorded, and after step 17 the dumps are equal.
  Red when: the blob comes from another read than the text, so a text is served under another's blob at step
  15, or a failed read is recorded as parsed, so the cold dump holds rows the index lacks at step 17.
- **AC11** — When a Python probe imports `tag_bundle` from `tools/playbook` and prints the lines of
  `SELFTEST_ROWS` whose first field is `released-rows` or `released-cost`, it prints one of each, whose second
  field is 0 and whose last is `only replaced edits left, and nothing lost` for the first and
  `a sweep costs what was released` for the second.
  Red when: a row is missing or misspelled, so no leg runs that plant.

## 7. Gates

`tags (the resolver's checks)` · `instruction edits (manifest checks)` · `edges (every declared edge parses, is registered and resolves)` · `instruction units selftest` · `tags bundle selftest` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

Those of the line that open the live index, the four section 3 lists, are owed at the close, once the go
section 3 states holds, and by no pass before it.

New arm: tools/playbook/tag_bundle.py · covers AC1 AC3 AC8 AC10 · the `released-rows` row; staged red with the overlay releasing the pairs it replaces, with the pair filter absent, with no set from a gone worktree, with `remove_dead_versions` calling no full sweep, with today's overlay, with the path hashed before the bytes are read, with the path hashed after, with a failed read recorded with no text, and with bytes that are not UTF-8 refused · none
New arm: tools/playbook/tag_bundle.py · covers AC2 · the `released-cost` row; staged red with `remove_unheld_rows` called from `build_index`, and with the pad written for a blob no table holds · none

## 8. Open questions

- **F1 — What happens to the rows only a replaced edit held?** The overlay could release them at once,
  which opens the window of the audit's finding 16 and needs a check in every command that reads a view.
  Or they could stay until `--gc`'s full sweep, which opens no window and lets the file grow by one file's
  rows per replaced edit. The recommendation was the second. RESOLVED (owner, 2026-11-25): keep until
  `--gc`, in the record `2026-11-25-prompt-TOOL-aPrunedIndex-3-revision`.

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft.
- rev-2 · 2026-11-25 · §1 §2 §3 §4 §5 §6 §7 §10 S6 S8 S9 S10 AC8 AC9 AC10 · folded
  `2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1`: finding 16 (a reader whose view
  moved refuses, the class-level fix, with its plant), 3 (AC9 measures the whole check against its ceiling),
  5 (the edges to units 1 and 2), 12 (the plants' rows move to `tags bundle selftest`), 14 (the legs that
  open the live index), 15 (the symbol map).
- rev-3 · 2026-11-26 · §1 §2 §3 §4 §5 §6 §7 §8 §10 S4 S6 S7 AC1 AC2 AC3 AC6 AC8 · the owner's answer in
  `2026-11-25-prompt-TOOL-aPrunedIndex-3-revision`: the overlay releases nothing, so a replaced edit's rows
  wait for `--gc`. Finding 16 of `2026-11-25-review-TOOL-aPrunedIndex-1-2-3-4-spec-audit-round1` is answered
  by its window not opening, which AC8 now observes, and rev-2's reader refusal leaves with S8, S9, S10 and
  AC10. `released-rows` grades what stays, `released-cost` counts the build's sweep alone and proves its
  pad, and section 4 names the acceptance ledger.
- rev-4 · 2026-11-26 · §1 §2 §3 §4 §5 §6 §7 §10 S4 S6 AC1 AC6 AC9 AC10 AC11 · folded
  `2026-11-26-review-TOOL-aPrunedIndex-1-2-3-spec-audit-round1`: findings 8 and 12 (the overlay keys an
  edit by the bytes it parses and refuses a file it cannot read, with steps 15 to 17 and AC10), 1 (AC9 states
  both workloads, and which one 420 s binds), 3 (AC11 reads both plants' rows), 4 (the owner's go with its (PINNED, 2026-11-25)
  conditions, stated once in section 3), 6 (AC6 reads the docstrings), 7 (the owner's go is taken, not handed
  off), 13 (the wait behind older worktrees, in Rollout, in the risks and in AC9), 15 (the growth figure, its
  denominator and all three tables).

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "delete index rows no tree or worktree holds any more"` named
`build_index`, `load_index` and `read_rows` of `tools/playbook/tag_index.py` and no other eviction seam.
The seams extended are `remove_unheld_rows`, split in two, `build_index`, `remove_dead_versions`, and
for the plants `write_commit`, `read_dump`, `run_gc`, `print_equal` and the row table of
`tools/playbook/tag_bundle.py#run_selftest`. Unit 1's `read_step_count` counts the full sweep that proves
the pad of `released-cost`. It does not fit that plant's own count: it counts one whole read, and the plant
counts one window inside a `load_view`, where the parse ledger a build reads would otherwise hide the
sweep. Recall answered PLAY-dOrderedCharter-51 with its deviation 513, TOOL-aQueuedIndex-1 and
KICK-dKeptSession-87. The performance review of TOOL-aMeasuredDrag-1 proposed the sweep in `--gc` alone,
which section 4 rejects. For S4,
`tools/codebase-map/reuse_lookup.py "git blob id of bytes held in memory, hash-object from stdin"` named
`read_git_output` of `tools/memory-tree/tree_lib.py`, which takes bytes on stdin and answers bytes, and
that is the seam. `read_git` takes no stdin.

Recall terms used: tag index sweep unheld rows tree_path dirty_path overlay path_row blob_row blob_parsed gc worktree eviction shared
