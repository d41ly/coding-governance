# TOOL-dTotalRecall-21 — memory-recall's FTS5 tables moved into the one index file, keyed by blob

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 17 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0232@94a25816 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-b.md) | research | TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-21-deviation-211.md](../build/2026-10-26-build-TOOL-dTotalRecall-21-deviation-211.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-14 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |

<!-- /gen:spec-records -->

## 1. Goal

memory-recall keeps one cache per worktree under the git common dir and rebuilds it whole when
`corpus_digest`, an mtime-and-size hash over every corpus file, moves after any edit (gap-mem-41): 510 MB
for two worktrees on node d today, and each query after an edit pays a full rebuild (9.4 s and 14.0 s,
cause `corpus digest`, on this spec's own recall probes). The owner's NT-15 answer puts its FTS5 tables
into the one SQLite index at `<git-common-dir>/gov/index.db`, rows keyed by blob, so a commit
re-extracts only the blobs it changed, every worktree shares the rows, and the whole-corpus digest and
the per-worktree cache machinery are retired with them (night pass two, point 3).

## 2. Scope (IN)

Preconditions this unit calls and does not build, each cited by its parent spec: the index file, its
tables `tree_path`, `blob_row`, `path_row`, `dirty_path` and `tree_built`, its one writer
`build_index(root, tree)` and the worktree overlay in `tools/playbook/tag_index.py`, and
`tools/lib/common_dir.py` (PLAY-dOrderedCharter-19 S4, S5, S10); the moved recall names in
`tools/memory-tree/id_grammar.py`, `build_index`, `match_expr`, `terms`, `ALIAS_WEIGHT`,
`corpus_inputs`, `extract_records` and `extract_supersessions`, re-exported by `bench.py` and
`extract.py` (PLAY-dOrderedCharter-18 S1, S3).

- **S1** — The FTS builder re-spelled `build_fts_rows(db, table, docs, *, blob="", digest="", crumb=False)`
  in `id_grammar.py` (I14), creating `table` as today's `fts5(head, body, alias, tokenize='unicode61')`
  when absent, its three columns and `ALIAS_WEIGHT` unchanged, and adding `blob` and `digest` as
  `UNINDEXED` columns, so `tag_index.build_index` stays the one index writer. A benchmark caller passes
  `sqlite3.connect(":memory:")` and the table `d`. Departure from PLAY-dOrderedCharter-18's spelling:
  deviation record 211. Observed by AC1.
  **Readers:** by name: `tools/memory-recall/bench.py:88` and `:454`, `tools/memory-recall/check-recall.py:251`,
  `tools/memory-recall/query.py:385`, `tools/memory-recall/union.py:96`,
  `tools/memory-recall/test_recall_floor.py:558`, `tools/memory-recall/selftest.py:2061`, `:2085`, `:2088`,
  `:2144`, `:2151`, `:2160`, `tools/memory-tree/row_grammar.py:1301` and `:1415`,
  `tools/memory-recall/README.md:308`, `tools/memory-recall/extract.py:268`,
  `memory/map/features/row-grammar.md:107`, each re-pointed to the new name · by value:
  NO VALUE READERS — the name returns a connection, and no reader compares or counts the name itself.
- **S2** — The tables, added to `index.db` and written only inside `tag_index.build_index`: `fts_record`
  and `fts_chunk` (S1's shape), `fts_blob(blob, digest)` naming each blob extracted at a digest, and
  `fts_supersession(blob, digest, rec, superseded, whole)` holding each blob's `extract_supersessions`
  output. `digest` is the SHA-1 of `CACHE_VERSION`, `CHUNK_MAX`, `CONF.digest()` and `alias_digest()`,
  the four inputs today's manifest compares, so a grammar, alias or extraction change re-extracts every
  corpus blob once and a worktree with a different conf never thrashes another's rows. For each blob of
  a recall corpus path (`corpus_inputs`) that `fts_blob` lacks at the current digest, `build_index` runs
  today's record and chunk extraction and `build_fts_rows`. Observed by AC2 and AC3.
- **S3** — The overlay. A worktree's modified tracked corpus files and its untracked ones, which today's
  `include_untracked=True` (`tools/memory-recall/extract.py:288`) serves, are extracted from their
  working bytes, their blob ids from `git hash-object`, and recorded as `dirty_path` rows keyed by that
  worktree, served to it alone (PLAY-dOrderedCharter-19 S5). Observed by AC4.
- **S4** — `query.py` reads the index. `ensure_index(repo)` builds the worktree's HEAD tree through
  `tag_index.build_index` when `tree_built` lacks it, refreshes the overlay, and returns the served blob
  set: the tree's corpus blobs, each overlaid path's blob replacing its tree blob. `search` and
  `run_fusion` keep their ranking and read `fts_record` and `fts_chunk` restricted to that set, and the
  supersession map is `derive_supersession_map` over the set's `fts_supersession` rows. The playbook kit
  is reached through `resolve_kit_dir("playbook", "tag_index.py", here)`, and
  `tools/memory-recall/kit.toml`'s `requires` gains `playbook`. Observed by AC2 to AC5.
- **S5** — The whole-corpus digest and the per-worktree cache retired: `corpus_digest`, `cache_dir`,
  `ensure_cache` and its freshness clauses, `build_cache`, `_build_cache`, `_write_set`, `read_manifest`,
  `REBUILD_CAUSE`, `BUILD_MARKER` and `BUILD_TTL_S`. Observed by AC6.
  **Readers:** by name: `tools/memory-recall/query.py` (`:136`, `:154`, `:311`, `:366`, `:436`, `:437`,
  `:497`, `:527`, `:530`, `:542`, `:548`, `:667`, `:715`, `:722`, `:725`, `:737`, `:743`, `:838`, `:1622`,
  `:1638`, `:1657`), `tools/memory-recall/check-recall.py:33`, `:276`, `:282`, `:297`, `:569`,
  `tools/memory-recall/recall_conf.py:245`, `:253`, `tools/memory-recall/selftest.py:836`, `:1097`,
  `:1102`, `:1104`, `:1214`, `:2672`, `tools/memory-recall/README.md:209`, `:231`,
  `tools/memory-tree/row_grammar.py:1048` · by value: the manifest's `digest`, `version`, `chunk_max`,
  `conf_digest` and `alias_digest` fields, compared by `ensure_cache` (`:728-737`) and printed by
  `--stats` (`:1652`), whose comparison S2's `digest` column takes over.
- **S6** — Eviction and its budget retired: `evict_dead_siblings`, `evict_over_budget`,
  `check_dead_worktree`, `_dir_bytes`, `_mid_build`, `_remove_cache_dir`, `load_last_queries`, the conf
  key `RECALL_CACHE_BUDGET_MB` and `Conf.cache_budget_mb`. One file per node has no sibling to evict.
  Observed by AC6.
  **Readers:** by name: `tools/memory-recall/query.py` (`:477`, `:486`, `:501`, `:503`, `:545`, `:632`,
  `:657`, `:665`, `:685`, `:693`, `:696`, `:748`, `:751`), `tools/memory-recall/recall_conf.py:189`, `:210`,
  `:214`, `:233`, `:339`, `tools/memory-recall/selftest.py:335`, `:1036`, `:1199`, `:1200`, `:1222`,
  `:1223`, `:1230`, `:1240`, `:1322`, `:1332`, `:1334`, `:1340`, `tools/memory-recall/README.md:134`,
  `.memory-tree.conf:659`, `tools/memory-tree/.memory-tree.conf.example:270` · by value:
  `CONF.cache_budget_mb` read at `query.py:751`, the only comparison of the key's megabytes.
- **S7** — `query.common_git_dir` retired: `query.py` reads the index path from `tag_index`'s resolver,
  the `tools/lib/common_dir.py` block, and the query log, the export directory and `--used`'s reflog
  walk (`:302`, `:1288`, `:1374`) take the common dir from that resolver; the `common_git_dir` row of
  `PARITY_ROWS` drops `query.py` from its copies. Observed by AC6.
  **Readers:** by name: `tools/memory-recall/query.py:298`, `:302`, `:1288`, `:1374`, and the
  `PARITY_ROWS` row PLAY-dOrderedCharter-19 S10 adds in `tools/lib/resolve-python.test.sh` · by value:
  the query log `<common>/recall/queries.jsonl`, the export directory and the reflog root, each keeping
  its path.
- **S8** — `check-recall.py`'s `build_served_dir` builds a throwaway repository index in a scratch
  common dir through `tag_index.build_index` over tracked files only, as today, and `--data-dir` names an
  `index.db`. Observed by AC7.
- **S9** — The index line reads `index <n> records + <m> chunks · superseded … (tree <tree8>, extracted
  <k> blob(s) in <s>s)`, `k` the blobs this call extracted, never a rebuild cause. Observed by AC3.

## 3. Non-goals (OUT)

- `record find`, the reshape of `query.py` into it, and the `check-recall` leg's takeover:
  TOOL-dTotalRecall-9, which reads S1 and S2.
- The memory legs reading index rows: TOOL-dTotalRecall-23.
- An adopter's conf still setting `RECALL_CACHE_BUDGET_MB`: the key is read by nothing after this unit
  and is inert; its removal from an adopter's conf is an upgrade step's, not this unit's.
- Ranking, chunking, aliasing or supersession semantics: unchanged, AC2 compares them.

### Edges

- **hands-off** `TOOL-dTotalRecall-9` — `build_fts_rows` and the `fts_record`, `fts_chunk` and
  `fts_supersession` tables, which `record find` searches
- **hands-off** `TOOL-dTotalRecall-23` — `build_fts_rows` and `fts_blob`, the per-blob rows a memory leg
  reads for an unchanged blob

## 4. Design

### The rows

```sql
CREATE VIRTUAL TABLE fts_record USING fts5(head, body, alias, blob UNINDEXED, digest UNINDEXED,
                                           id UNINDEXED, line UNINDEXED, tokenize='unicode61');
CREATE VIRTUAL TABLE fts_chunk  USING fts5(head, body, alias, blob UNINDEXED, digest UNINDEXED,
                                           id UNINDEXED, line UNINDEXED, tokenize='unicode61');
CREATE TABLE fts_blob(blob TEXT, digest TEXT, PRIMARY KEY (blob, digest));
CREATE TABLE fts_supersession(blob TEXT, digest TEXT, rec TEXT, superseded TEXT, whole INTEGER);
```

`id` and `line` replace today's `meta` table, which joined by rowid; the path is never stored on a row,
because one blob may sit at two paths, and `tree_path` answers it at query time.

### The flow

```
query.py  -> ensure_index(repo)
          -> tag_index.build_index(root, HEAD tree)  # once per tree; new blobs only
               -> extractors (blob_row, path_row)
               -> recall corpus blob at digest absent -> extract -> build_fts_rows
          -> overlay: modified + untracked corpus files -> dirty rows for this worktree
          -> served set = tree corpus blobs, overlaid
          -> search / run_fusion over fts_* WHERE blob IN served AND digest = current
```

A query after an edit to one file re-extracts that file's blob as a dirty row and nothing else; a commit
of it lands the same blob in the next tree, whose row already exists.

### Inventory

Minted: `build_fts_rows` (renamed), `ensure_index`, the four tables. Retired: S5 to S7. Naming cells:
`ensure_index` is asked of the lexicon's `--suggest` under `--as py.function` at the pass.

### Migration

The first query after landing builds the HEAD tree's rows once, a full extraction, and deletes nothing
by itself. `<common>/recall/cache/` is left for its owner to remove; the README states the command. The
query log `queries.jsonl` keeps its path.

### Rollout

The move lands whole: a reader of the old cache and a reader of the index cannot coexist on one node,
because the old cache's freshness is the clause's defect.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`
- `tools/playbook/tag_index.py`
- `tools/memory-recall/query.py`
- `tools/memory-recall/check-recall.py`
- `tools/memory-recall/bench.py`
- `tools/memory-recall/union.py`
- `tools/memory-recall/extract.py`
- `tools/memory-recall/recall_conf.py`
- `tools/memory-recall/selftest.py`
- `tools/memory-recall/test_recall_floor.py`
- `tools/memory-recall/README.md`
- `tools/memory-recall/kit.toml`
- `tools/memory-tree/row_grammar.py`
- `tools/lib/resolve-python.test.sh`
- `.memory-tree.conf`
- `tools/memory-tree/.memory-tree.conf.example`
- `memory/map/features/row-grammar.md`

### Alternatives rejected

- **A second SQLite file beside `index.db` for recall.** I11 and NT-15 name one file; two files are two
  freshness rules.
- **Key the rows by tree.** A tree changes on every commit, so every row would be rewritten; the tree is
  only the freshness key (night pass two, `:265`).
- **Drop untracked notes from recall.** A session's records are untracked until its commit and are the
  ones most often asked for; S3 keeps them.

## 5. Production-readiness checklist

- security — no new write surface beyond the index the playbook kit owns; the index is never committed
  and opens read-write only inside `build_index`.
- perf / scale — one extraction per new blob; a query after one edit extracts one blob. The FTS tables
  for one tree replace one cache per worktree, 510 MB for two at `fb872a37` (PINNED, `du` on node d,
  2026-10-26).
- error / empty / loading states — a corrupt index raises `sqlite3.DatabaseError`; the query deletes no
  file and refuses, naming `gov_tag.py --rebuild` as the remedy, since the file is shared.
- observability — the index line names the tree and the blobs extracted (S9).
- risks — the recall kit now requires the playbook kit; an adopter installing recall alone is refused by
  govkit's `requires` join, which §8 F3 accepts under the grant.
- testing — AC1 to AC7 by a pass; the arms of §7 at the close.
- migration — one cold extraction, as §4 says.
- user docs — `tools/memory-recall/README.md` loses the cache and budget sections and states the index;
  no page under `help/` covers recall.

## 6. Acceptance criteria

- **AC1** — When `git grep -n "build_index(" -- tools/memory-recall tools/memory-tree/row_grammar.py`
  runs, it prints nothing, and `git grep -n "def build_fts_rows" -- tools` prints one line, in
  `id_grammar.py`.
  Red when: a caller keeps the old name through an alias, so two names reach one builder.
- **AC2** — When `query.py` answers the graded question set of the fixture
  `tools/memory-recall/recall-fixture.json` over a scratch clone under `%TEMP%`, its rendered hits
  equal, byte for byte, the hits the base `462d20f3` `query.py` renders over the same clone, and the
  clone's common dir holds `index.db` in its `gov` folder and no `recall/cache/`.
  Red when: the restriction to the served blob set drops or duplicates a row, so a hit moves.
  cost: two query runs over one clone, each a cold extraction, under a minute.
- **AC3** — When one tracked memory file of that clone is edited and committed and the same query runs,
  its index line reads `extracted 1 blob(s)`; when `FAMILIES` in the clone's conf is edited, the next
  query's count equals the corpus's file count.
  Red when: freshness is a whole-corpus hash, so the first count is the corpus size, or the digest omits
  the conf, so the second is 0.
- **AC4** — When an untracked record is written in worktree A of the clone, a `query.py` run from A returns it and
  the same query from worktree B does not; after A's commit lands on B's branch, B returns it.
  Red when: dirty rows are served across worktrees, or untracked files are dropped from the corpus.
- **AC5** — When `index.db` is truncated to zero bytes in the clone and a query runs, it exits non-zero
  naming `gov_tag.py --rebuild`, and the file is not deleted.
  Red when: the query deletes the shared file, as today's `shutil.rmtree(dirp)` deletes a cache.
- **AC6** — When `git grep -nE "corpus_digest|evict_dead_siblings|evict_over_budget|RECALL_CACHE_BUDGET_MB|cache_budget_mb|def common_git_dir|def cache_dir|def ensure_cache" -- tools .memory-tree.conf`
  runs, it prints nothing outside `common_dir.py`.
  Red when: a retired name survives in a reader or the conf.
- **AC7** — When `python check-recall.py --data-dir <the index.db of a scratch build>` runs from
  `tools/memory-recall/` against the clone, its graded rows equal those the base `462d20f3` script grades
  over the base's served sets.
  Red when: the served sets read a different corpus, such as untracked files, so a row's hit changes.

## 7. Gates

`memory-recall kit selftest` · `recall floor` · `recall floor arms` · `memory-recall skill wiring` · `row-grammar selftest` · `hook destinations self-test` · `row-keyed merge driver replay` · `govkit acceptance matrix` · `playbook render selftest` · `kit/dogfood doc parity` · `straggler-guard arms` · `transition-audit arms` · `python resolver (behaviour + inline parity + idiom ban)`

New arm: tools/memory-recall/selftest.py · covers AC2 AC3 AC4 AC5 · the cache arms replaced by index arms: one-blob re-extraction, the conf digest, the worktree overlay and the refused corrupt file, staged by a whole-corpus digest reinstated as the freshness rule · none
New arm: tools/memory-recall/test_recall_floor.py · covers AC7 · the floor arms over a throwaway index, staged by `build_served_dir` reading untracked files · none

## 8. Open questions

- **F1 — Two functions named `build_index` once PLAY-dOrderedCharter-18 and -19 land; which is re-spelled?**
  Options: (a) the FTS builder becomes `build_fts_rows`, `tag_index.build_index` staying the one index
  writer; (b) the index writer is renamed. (b) moves a parent's public verb that six chain units cite.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the brief's I14; recorded as deviation 211 from
  PLAY-dOrderedCharter-18@rev-3. widens: none · relaxes: none
- **F2 — Untracked corpus files: keep them in recall?** Options: (a) as dirty rows of their worktree;
  (b) drop them, the index holding tracked blobs only. (b) loses a session's unrecorded records, which
  today's `include_untracked=True` serves. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  most capable option, AC4 holding it. widens: none · relaxes: none
- **F3 — memory-recall writing through the playbook kit's index makes `playbook` a required kit of
  recall; may it?** Options: (a) `requires` gains `playbook`, recall reaching `tag_index` through
  `resolve_kit_dir`; (b) recall builds its own rows in a second file. (b) is the second file I11 and
  NT-15 refuse. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3 under the grant, the clause naming
  the one index file. grants: PLAY-dClosedLoop-3 the memory-recall kit requires the playbook kit ·
  widens: none · relaxes: none
- **F4 — Every surface this unit calls is specced and unbuilt at HEAD; whose spelling binds?**
  Options: (a) the parent specs' spellings as cited in §2, the build run re-grounding on the landed
  code and bumping this spec's rev before any code where they differ; (b) wait for the parents.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, BUILD-METHOD M2 ("to diverge, change the spec
  first") and the brief's rule that a spec calls each parent surface as its spec names it.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 21, the brief's I11 and I14, scout B's row
  for cl-0232, night pass two point 3, and `query.py`, `bench.py` and `check-recall.py` read at base
  `462d20f3`.

## 10. Reuse audit

The seams extended are `bench.build_index` (`tools/memory-recall/bench.py:88`), the one FTS5 builder,
renamed rather than copied, and `_write_set` (`tools/memory-recall/query.py:381`), whose `meta` join the
`id` and `line` columns absorb; PLAY-dOrderedCharter-19 S4's `build_index(root, tree)` is the writer the
rows go through, and its S5 overlay holds the untracked notes. The lookup,
`python tools/codebase-map/reuse_lookup.py "store full-text search rows keyed by blob in a shared sqlite index"`,
ranked `search` (`query.py`) and `build_index` (`bench.py`) in memory-recall, `read_blobs_at` and
`read_text` in `tools/memory-tree/tree_lib.py`, `build_reference_index` in codebase-map and generic
`row` and `key` stems; no other sqlite writer exists (`git grep -l sqlite3 -- tools` names
`bench.py`, `check-recall.py` and `query.py` alone). Disagreements with source: scout B places the freshness clauses at `query.py:712-740`,
and they run `:727-737` inside `ensure_cache` (`:712-756`); the gap register's 478 MB is 510 MB for two
worktrees at `fb872a37`. The recall probe returned the brief's row, scout B's row and this spec's own draft; night pass two
`:228-270` was read from scout B's citation. Each probe rebuilt the per-worktree cache, cause `corpus
digest`, the defect this unit retires.

Recall terms used: `python tools/memory-recall/query.py "how does memory-recall keep its full-text tables fresh across worktrees" --terms "memory-recall FTS5 corpus_digest cache_dir per-worktree evict RECALL_CACHE_BUDGET_MB index.db keyed blob NT-15"`
