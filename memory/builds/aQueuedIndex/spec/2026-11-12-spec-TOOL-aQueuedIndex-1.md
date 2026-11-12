# TOOL-aQueuedIndex-1 — writers of the shared tag index queue instead of failing

**Status:** CLOSED · rev-2 · 2026-11-12 · node a · Tier-2 · base 6f5d27a20 · streams tooling · order 1 · ratified 2026-11-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aQueuedIndex-1-deviation-11.md](../build/2026-11-12-build-TOOL-aQueuedIndex-1-deviation-11.md) | deviation | — |
| [2026-11-12-build-TOOL-aQueuedIndex-1-ledger.md](../build/2026-11-12-build-TOOL-aQueuedIndex-1-ledger.md) | journal | — |
| [2026-11-12-prompt-TOOL-aQueuedIndex-1-1-spec-writer.md](../prompts/2026-11-12-prompt-TOOL-aQueuedIndex-1-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-TOOL-aQueuedIndex-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aQueuedIndex-1-brief.md) | research | — |
| [2026-11-12-prompt-TOOL-aQueuedIndex-1-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aQueuedIndex-1-build-brief.md) | journal | — |
| [2026-11-12-prompt-TOOL-aQueuedIndex-1-spec-brief.md](../prompts/2026-11-12-prompt-TOOL-aQueuedIndex-1-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Two bar legs that write the node's shared tag index on one unbuilt tree must both exit green. Today
SQLite refuses one of them at once with `database is locked`, well inside the busy timeout. After
this unit every write takes the index's write lock before it reads, the busy timeout outlasts a full
tree build, and a writer that queued re-reads whether its tree was built and reuses it.

## 2. Scope (IN)

- **S1** — `load_index` opens the index connection in autocommit, `isolation_level=None`, so no
  statement opens a transaction implicitly and a connection holds a lock only inside an explicit
  write block. Observed by AC1 and AC3.
- **S2** — Each of the three write blocks opens with `BEGIN IMMEDIATE` as its first statement inside
  its `with con:`: the tree build in `build_index`, the overlay in `build_overlay` and the collection
  in `remove_dead_versions`. The schema-reset block in `load_index` already does. Observed by AC1
  and AC3.
- **S3** — `build_index` re-reads `tree_built` for its tree and digest once it holds the lock, and
  returns with no write when another writer built the tree while it queued. The unlocked read above
  the block stays, so a built tree never takes the lock. Observed by AC2.
- **S4** — `BUSY_TIMEOUT` goes from 60 to 600 seconds, its comment saying it outlasts a full tree
  build. Observed by AC4 and AC3.
- **S5** — A new plant `queued-writers` in `tools/playbook/gov_tag.py` races two writers over one
  unbuilt tree in the plant's own scratch repository, with its row in the tag resolver's plant table
  of `tools/playbook/adopt-playbook.sh`. Observed by AC1 and AC2.
- **S6** — `help/tags.md` says a second writer queues behind the first, how long it waits, and that
  it reuses a tree built while it waited. Observed by AC5.

## 3. Non-goals (OUT)

- No change to what the index stores, how a tree's rows are parsed, the file's name, its schema
  version `INDEX_SCHEMA = 3` or its `journal_mode=DELETE`. No write-ahead log: every worktree opens
  the one file, and the brief rules it out.
- No lock file or process mutex beside SQLite's own lock.
- No change to the per-open `PRAGMA user_version` write in `load_index`, which makes every open
  queue behind a running write block. It is a separate question of open cost.
- No change to a leg's `ceiling` in `tools/gate-legs.json`.
- No change to `tools/memory-tree/id_grammar.py`, whose SQLite connection opens its own FTS file,
  never this index.

### Edges

- **hands-off** external — a leg whose ceiling the waiter's queued time outgrows has that ceiling
  re-derived from its own ceiling evidence, outside this build. Section 5 names the one leg near it.

## 4. Design

### The fault, reproduced

Reproduced by this writer on 2026-11-12, PINNED, in a scratch clone at `97e0841d7` with no
`.git/gov/` directory, starting `python tools/playbook/gov_tag.py check` and
`python tools/playbook/instructions_edit.py check` together. Race one: the tags check exited 2 at
30 s with `tags: refused · the tag index is locked or unwritable: database is locked`, and the
instruction-edits check exited 0 at 93 s. Race two, with a probe printing the connection's
`in_transaction` before each write block: the tags check exited 2 at 29 s, refused inside the tree
build's write block of `build_index`, and the probe printed `True`.

The mechanism, read from the code and confirmed by a two-connection probe:

1. `load_index` opens the connection with Python's default `isolation_level=""`
   (`tools/playbook/tag_index.py@f1d7712e6:517`). On the bar's Python 3.15.2 the connection's
   `autocommit` reads `LEGACY_TRANSACTION_CONTROL`, so the module opens a deferred transaction
   implicitly before any INSERT, UPDATE, DELETE or REPLACE, and never before a SELECT.
2. `load_view` fills three temp tables (`tools/playbook/tag_index.py@f1d7712e6:803-818`). Its first
   DML, the DELETE of `view_version`, opens that implicit transaction, and
   `INSERT INTO view_path SELECT ... FROM tree_path` then reads the main database inside it, taking
   a shared lock. Nothing commits it: the connection keeps the shared lock until it closes or its
   next commit.
3. The next write block on that connection begins inside that open transaction, so its first DML
   upgrades a shared lock the connection already holds. When another connection holds the reserved
   lock, SQLite returns `SQLITE_BUSY` at once and does not call the busy handler: waiting would
   deadlock, because the holder's commit waits on this connection's shared lock. The busy timeout
   never applies, which is why the red came at 30 s inside a 60 s timeout.
4. `gov_tag.py check` serves a second view on one connection: `run_kit_verb` serves HEAD
   (`tools/playbook/gov_tag.py@f1d7712e6:110-112`), then `run_check` serves the base tree and HEAD
   again (`tools/playbook/gov_tag.py@f1d7712e6:240-244`). The base tree's build, and the overlay of
   the third view, are write blocks on a connection already holding a view's shared lock.

The probe, run on 2026-11-12 with SQLite 3.53.4: connection B fills a temp table from the main
database, connection A holds `BEGIN IMMEDIATE` for 3 s, and B then writes with a 30 s timeout. Under
`isolation_level=""` B was refused after 0.0 s. Under `isolation_level=None`, B opening
`BEGIN IMMEDIATE` itself, B wrote after 2.7 s.

A second fault sits behind the first. `build_index` reads `tree_built` once, before its write block
(`tools/playbook/tag_index.py@f1d7712e6:642`). A writer that queued behind another writer's build of
the same tree builds that tree again once it gets the lock.

### The transaction rule

After this unit a connection to the index holds a lock in exactly two places. One is a single
autocommit statement, which takes and drops a shared lock inside one step. The other is an explicit
`BEGIN IMMEDIATE` block, which takes the reserved lock at its first statement and keeps it until
`with con:` commits or rolls back.

1. `load_index` passes `isolation_level=None` to `sqlite3.connect`
   (`tools/playbook/tag_index.py@f1d7712e6:517`). Its schema-reset block keeps its explicit
   `BEGIN IMMEDIATE` with `con.commit()` and `con.rollback()`
   (`tools/playbook/tag_index.py@f1d7712e6:520-534`), which behave the same under autocommit. The
   temp-table statements of `load_view` now each commit alone, and every later read is its own
   statement.
2. The first statement inside each `with con:` write block becomes `con.execute("BEGIN IMMEDIATE")`:
   - the tree build, `tools/playbook/tag_index.py@f1d7712e6:663-672`;
   - the overlay, `tools/playbook/tag_index.py@f1d7712e6:737-744`;
   - the collection, `tools/playbook/tag_index.py@f1d7712e6:775-790`.
   Under autocommit, `with con:` commits the open transaction when the block ends and rolls it back
   on an exception, so each block stays one transaction. A busy wait at `BEGIN IMMEDIATE` holds no
   lock, so the busy handler runs and the writer queues.
3. Why this cannot deadlock: a write block waits only at `BEGIN IMMEDIATE`, holding nothing, or at
   its commit, for readers' shared locks that each end with one statement and wait on nothing. A
   write block opens no second connection: `build_index`, `build_overlay` and `remove_dead_versions`
   call git and the registered extractors, and none of the ten extractors
   `tools/playbook/namespaces.toml` names, nor `extract_citations`, opens the index.
4. The `load_index` docstring (`tools/playbook/tag_index.py@f1d7712e6:509-513`) gains one sentence:
   the connection runs in autocommit, and every write block takes the write lock first.

### The busy timeout

`BUSY_TIMEOUT` (`tools/playbook/tag_index.py@f1d7712e6:115-116`) becomes 600, and its comment says
that a second writer waits this long for the first, which outlasts a full tree build, before the verb
exits 2.

A waiter must outlast the longest write block it can queue behind, which is one cold build of a
whole tree. The brief measured that at 77 to 100 s on node a. In this writer's prototype race it was
35 s. Both figures are PINNED on 2026-11-12. The brief's race with IMMEDIATE and 600 s passed 3 of
3, the second writer taking about 150 s against the first's 95 s, and 600 s is six times the longest
build measured. Every leg that opens the index carries a lower `ceiling` in `tools/gate-legs.json`,
such as 420 s for the tags leg and 180 s for the instruction-edits leg (DERIVED: re-read that file).
So inside a bar a pathological wait ends at the leg's ceiling, and the 600 s refusal only surfaces
outside one. Section 8 F1 holds the one alternative value.

The timeout is per lock attempt. Writers queued behind one tree's build each re-read and return in
milliseconds, so a queue of several writers costs one build and not one build per writer.

### The waiter's re-read

Inside the tree build's write block, right after `BEGIN IMMEDIATE`, `build_index` runs the same
`tree_built` query as its unlocked read (`tools/playbook/tag_index.py@f1d7712e6:642`) and returns
when it finds the row. The `with con:` then commits an empty transaction. The query's SQL and
parameters are bound once to a local `built` before the unlocked read, and both reads execute it, so
the query is spelled once. The early return leaves `stats` untouched, so the waiter's `load_view`
reports `parsed` 0.

The `git ls-tree` and the applicability walk stay before the lock, as today. They read git and no
index row, so a writer holds the lock only for the parse and the row writes.

### The arm: plant `queued-writers`

The plant lives in the `run_plant` chain of `tools/playbook/gov_tag.py`
(`tools/playbook/gov_tag.py@f1d7712e6:649`). Its name joins `PLANTS`
(`tools/playbook/gov_tag.py@f1d7712e6:380-392`), and `run_fixture` builds its scratch repository
under a fresh `tempfile.mkdtemp`, so the plant opens only that repository's own index, never the
node's. Its files ride the per-plant branch of `build_tags_fixture`
(`tools/playbook/gov_tag.py@f1d7712e6:600-607`), as `tagless` does.

1. **A slow parse.** The base commit's `fixture_tags.py` is `FIXTURE_EXTRACTOR` with one line added
   inline, as `EDITED_EXTRACTOR` derives its text (`tools/playbook/gov_tag.py@f1d7712e6:407`): when
   the text it reads holds the word `pause`, it sleeps 3 s. No base file holds that word, so the
   base tree builds at full speed.
2. **Two trees.** `run_verb(root, "rebuild", None, sets=sets)` builds the base tree P. Then
   `write_commit` adds `tools/corekit/pause.tags` holding `pause`, so HEAD's tree H is unbuilt and
   its one new blob holds the lock for at least 3 s while it parses.
3. **Writer two's first view.** On the main thread, writer two opens `ti.load_index(root)` and
   serves P with `ti.load_view(con, root, ctx, tree=P, overlay=False)`, as `run_check` serves its
   base tree. At BASE this leaves the view's shared lock held.
4. **Writer one.** A `concurrent.futures.ThreadPoolExecutor(max_workers=1)` submits
   `run_verb(root, "rebuild", None, sets=sets)`, which opens its own connection in its own thread and
   builds H. The fan-out bound is two writers: this thread and the main thread.
5. **Wait for the lock.** The main thread polls the index file every 0.05 s, for at most 30 s, with
   a raw `sqlite3.connect(path, timeout=0)` that runs `BEGIN IMMEDIATE` and rolls back at once.
   The first `database is locked` is not enough. Writer one's `load_index` writes
   `PRAGMA user_version` on every open, holding the lock for milliseconds before its build starts,
   so the poll reads writer one as inside its write block only once every poll has seen the lock
   held for 0.5 s in a row. The tree build holds it for the staged 3 s parse, which leaves writer two
   most of that parse to reach its unlocked read. At BASE, writer one's open waits on writer two's
   held view, so the refusal in step 6 still comes first. The `held-open` plant
   already holds the index through a raw `sqlite3` connection
   (`tools/playbook/gov_tag.py@f1d7712e6:754-777`). At the bound, the plant prints
   `writer one never took the write lock` and returns 1.
6. **Writer two writes.** The main thread serves H on the same connection with
   `ti.load_view(con, root, ctx)`. A `TagError` prints `writer two refused: <exc>` and returns 1
   after joining writer one. Otherwise the plant reads writer one's `parsed` from the future and
   writer two's from its state.
7. **The verdict.** The plant prints
   `writer one parsed <a> blob(s), writer two parsed <b>; both writers green`, then
   `print_equal(read_dump(root), read_cold_dump())`. It returns 0 when `a` is above 0, `b` is 0 and
   the dumps are equal, and 1 otherwise.

What the plant cannot see: if writer two reaches its unlocked read only after writer one commits, it
reads the tree as built without queueing. It then passes without exercising the re-read. Writer two
has 3 s of writer one's parse to pass that read, against two git calls. A busy timeout shorter than
the hold is not staged either, since 3 s sits inside both 60 and 600.

Its row joins the `run_plant_rows tags` table
(`tools/playbook/adopt-playbook.sh@f1d7712e6:292-376`) beside the `held-open` rows:

```
queued-writers|0|writer two parsed 0; both writers green|DIFFER
```

### Data model

Unchanged: one file at `derive_index_path`, `PRAGMA user_version` 3, `journal_mode=DELETE`, and the
six tables the module docstring lists. Only the connection's transaction control and the timeout
change.

### Inventory

This unit mints no function, constant, type or file. The new names are the plant string
`queued-writers`, which no lexicon cell grades, and the local variable `built` inside `build_index`.
The lexicon's `--suggest` grades only the surfaces `function`, `type`, `file` and `constant`, checked
on 2026-11-12, so neither name has a cell to run through.

### Migration

None. The file, its schema stamp and its rows are untouched, so an index written before this unit is
read as it is, and reverting the commit restores the old transaction control over the same file.

### Rollout

Lit at landing, with no switch. The behaviour this replaces is the defect, and a default-off switch
would keep every parallel bar on the coin-flip red the build exists to end. The two arms in section
6 observe the change before it lands.

### Files touched (estimate)

`tools/playbook/tag_index.py`
`tools/playbook/gov_tag.py`
`tools/playbook/adopt-playbook.sh`
`help/tags.md`

### Alternatives rejected

- **`isolation_level="IMMEDIATE"` on the connection alone**, the brief's measured fix. The implicit
  transaction then opens as `BEGIN IMMEDIATE` at `load_view`'s first temp-table DML: the probe of
  2026-11-12 printed `in_transaction` `True` there, and another connection's write was refused. So
  every connection that has served a view holds the write lock until it closes. `load_resolver`
  keeps its connection for the whole process in `RESOLVERS`
  (`tools/playbook/instruction_units.py@f1d7712e6:726-737`). Every other writer then waits out a
  whole process, consistent with the 150 s the brief's second writer took.
- **The default transaction control with a commit before each write block.** It ends the snapshot
  only at a write, so a connection that served a view still holds a shared lock between blocks, and
  any writer's commit waits on it for that connection's lifetime.
- **A write-ahead log.** Ruled out by the brief, since every worktree opens the one file.
- **A lock file beside the index.** A second lock that has to agree with SQLite's own, where one
  lock already serialises the writers.

## 5. Production-readiness checklist

- security: N/A — no new input, write path or grant. The index stays a derived, uncommitted file.
- perf / scale: a waiter's wall clock grows by the holder's remaining build, at most one cold build,
  measured 35 to 100 s. It no longer pays a second build, and a waiter used to exit 2 instead.
- error / empty / loading states: a wait past 600 s still raises `TagError` with
  `the tag index is locked or unwritable`, exit 2, and the message is unchanged.
- observability: unchanged. The waiter prints the build line it prints today, with 0 blobs parsed.
- risks: (1) A reader now reads each statement alone and holds no snapshot across a view. Another
  worktree's build can sweep a tree no worktree's HEAD names between two of a reader's statements,
  through `remove_unheld_rows` (`tools/playbook/tag_index.py@f1d7712e6:690-708`). In this tree only
  `run_check`'s base view serves such a tree. The window was already open between its build's
  commit and its `view_path` fill, and it now also spans the two base reads that follow, which run
  milliseconds after. (2) The instruction-edits leg's ceiling is 180 s, and the brief measured a
  waiter at about 150 s, so a slower machine could reach its ceiling. That is the hands-off edge in
  section 3.
- testing: plant `queued-writers` (AC1, AC2) and five real races in a scratch clone (AC3).
- migration: N/A — no data, schema or file change.
- user docs: `help/tags.md` gains the queueing sentence (S6, AC5).

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant queued-writers` runs, it exits 0
  and prints `both writers green`.
  Red when: writer two, holding its first view, is refused at once and the plant prints
  `writer two refused` with `the tag index is locked or unwritable`, as it does over BASE's
  `tag_index.py`.
  cost: about 10 s. Two sibling plants measured 3.5 s and 7.7 s on node a on 2026-11-12, plus the
  3 s staged parse, PINNED.
  fixture: the plant builds its own scratch repository under the system temp directory, so the tree
  needs none.
- **AC2** — When `python tools/playbook/gov_tag.py --fixture --plant queued-writers` runs, it prints
  `writer two parsed 0` and a non-zero count for writer one.
  Red when: the waiter skips the re-read under the lock and builds the tree again, printing a
  non-zero count for writer two.
- **AC3** — When `python tools/playbook/gov_tag.py check` and
  `python tools/playbook/instructions_edit.py check` start together in a scratch clone of the
  unit's commit with no `.git/gov/` directory, five races in a row, all ten runs exit 0.
  Red when: either run exits 2 printing `database is locked`, as the tags check did in 2 races of 2
  at the anchor on 2026-11-12.
  cost: about 100 s a race, so 8 to 10 minutes. The prototype race ran 101 s on 2026-11-12, PINNED.
  fixture: a fresh clone made by the observer outside the repository, its `.git/gov/` absent before
  each race. The tree holds none today.
  figure: the five races are PINNED by the brief, and the BASE count is PINNED at 2 of 2.
- **AC4** — When `grep -n "^BUSY_TIMEOUT = 600$" tools/playbook/tag_index.py` runs, it prints one
  line.
  Red when: the constant keeps 60, or a second assignment shadows it.
- **AC5** — When `grep -c "queues behind" help/tags.md` runs, it prints 1, on the sentence naming the
  600 s wait and the reuse of a tree built while waiting.
  Red when: the help page still says nothing of two writers meeting.

## 7. Gates

`tags (the resolver's checks)` · `instruction edits (manifest checks)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `playbook render selftest` · `govkit acceptance matrix`

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 · the `queued-writers` row run over BASE's tag_index.py, where writer two is refused at once · none

The arm runs in the `playbook render selftest` leg, adding about 10 s inside that leg's 300 s
ceiling. What it does not check: the real legs' race, which AC3 observes by hand, and a wait longer
than the busy timeout.

## 8. Open questions

- **F1 — What value does `BUSY_TIMEOUT` take?**
  - (a) 600 s. Measured green 3 of 3 in the brief's race, and six times the longest build measured.
    Every leg's ceiling ends a bar's wait first, so the lock refusal shows only outside a bar.
  - (b) 150 s. That sits under the smallest ceiling of a leg that opens the index, 180 s, so a stuck
    wait inside a bar exits 2 naming the lock rather than being killed at the ceiling. It is 1.5
    times the longest build measured, and nothing has measured it green.
  - Recommendation: (a). It is the only value measured green, and a slower machine's cold build
    stays inside it.
  - RESOLVED (agent, 2026-11-12, delegated): (a) 600 s. The main loop took the recommendation
    under the owner's prompt and accepted brief, which delegate forks to recommendations.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · §4 · §8 · base moved to 6f5d27a20. §4 Design step 5 folds the builder's
  deviation 11 (`2026-11-12-build-TOOL-aQueuedIndex-1-deviation-11`): the poll reads writer one as
  inside its write block only once the lock has been held for 0.5 s in a row, because
  `load_index` writes `PRAGMA user_version` on every open. §8 F1 is marked resolved, delegated,
  on (a) 600 s.

## 10. Reuse audit

`reuse_lookup.py` names `load_index` and `build_index` in `tools/playbook/tag_index.py` as seams, and
this unit extends them. The connection, its timeout and the three write blocks all live there, each
block already wrapped to raise `the tag index is locked or unwritable`. The same probe names
`build_tags_fixture` and `write_commit` in `tools/playbook/gov_tag.py`, which the plant reuses with
`run_plant`, `print_equal`, `read_dump` and `read_cold_dump`. Its other `build_index`, in
`tools/memory-tree/id_grammar.py`, builds an FTS file of its own and is not this index. A grep for
`sqlite3.connect` and `load_index` over `tools/` found no other writer of the index: every caller
goes through `load_index`, and the `held-open` plant's raw connections stay inside its own scratch
repository.

Recall terms used: `python tools/codebase-map/reuse_lookup.py "tag index sqlite connection busy timeout write lock BEGIN IMMEDIATE tree_built rebuild queue writers database locked"`
