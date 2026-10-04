# TOOL-aMendedFleet-32 — recall cache eviction removes deleted worktrees first and orders the rest by last query

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 32

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The recall cache holds one index per worktree, about 113 MB each on this tree, under a 512 MB
budget. When the budget is passed the eviction pass removes the least-recently-BUILT live cache, so
a sibling that is queried all day from a warm cache is evicted ahead of one that was rebuilt once
and abandoned, and pays a rebuild on its next query, which the report measured at 6.5 to 15.5 s.
A worktree directory that git no longer knows, an empty husk left by `git worktree remove` on
Windows, still counts as live and keeps its cache. This unit evicts husks with the deleted worktrees, and orders the budget pass by
each cache's last logged query, falling back to its build time.

## 2. Scope (IN)

- **S1** — `check_dead_worktree(wt)` in `tools/memory-recall/query.py` is true when the recorded
  worktree path does not exist OR holds no `.git` entry. `evict_dead_siblings` uses it, so a husk
  is evicted on the dead-worktree pass, which already runs before the budget pass. The
  never-evict rule for a cache with no readable manifest is unchanged. Observed by AC2.
- **S2** — The dead-worktree pass deletes through `_remove_cache_dir`, the budget pass's
  manifest-last delete, and prints a `could NOT evict` line for a directory it could not remove, in
  place of `shutil.rmtree` with errors ignored. Observed by AC2.
  **Readers:** by name: `tools/memory-recall/query.py` alone calls `evict_dead_siblings`, from
  `ensure_cache`. by value: NO VALUE READERS — callers read only the list of evicted worktrees,
  whose shape is unchanged.
- **S3** — `load_last_queries(log)` reads `queries.jsonl` once and returns, per `worktree` string,
  the newest `at` of its `query` rows. A missing or unreadable log returns an empty map, never an
  error. Observed by AC4 and AC5.
- **S4** — `evict_over_budget` takes that map from `ensure_cache` and orders its candidates by the
  newest of the cache's last query and its `built_at`, oldest first, ties broken by `built_at`.
  Every protection and the whole-plan-first rule are unchanged. Observed by AC1 and AC3.
- **S5** — Each eviction line reads `evicted the least-recently-queried cache: <worktree> (last query
  <at>, built <built_at>, <size> MB)`, with `never` for a cache no query row names. The selftest arm
  `test_budget_lru`, which asserts the old wording, is updated to the new one, and a new arm pins
  S4; `SELFTEST_ARMS` moves by the arms added, with its dated provenance line, as unit 27's S5 moves
  it. Observed by AC1.
  **Readers:** by name: `tools/memory-recall/selftest.py`, which asserts the
  `least-recently-built` wording, and `tools/memory-recall/README.md` and `.memory-tree.conf`, which
  describe the order. by value: NO VALUE READERS — the line is printed to stderr and nothing parses
  it.
- **S6** — The README's eviction paragraph and the comment above `RECALL_CACHE_BUDGET_MB` in
  `.memory-tree.conf` describe the husk rule and the last-query order, and the comment's typed
  "one cache is 2.4 MB" goes, since a cache here measures about 113 MB. Observed by AC6.
  **Readers:** by name: `.memory-tree.conf` alone spells the figure. by value: NO VALUE READERS — a
  comment, which nothing parses.
- **S7** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Sharing one cache across worktrees. The corpus digest hashes mtimes, so it differs per checkout
  and a digest-keyed cache would share nothing.
- A new store: no per-cache stamp file and no new log field. The order is a join over the query log
  rows that already carry `worktree` and `at`.
- Changing `RECALL_CACHE_BUDGET_MB` or when eviction runs, which stays after a successful build.
- The repo-wide `--opened` attribution, a separate defect over the same log.
- The memory-recall kit version bump, owed once at this build's close after the last move.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`; `tools/memory-recall/` and `.memory-tree.conf` are byte-identical at
`580dc980e`, re-verified 2026-10-04 with `git diff --stat`.

- `ensure_cache` runs `evict_dead_siblings` and then `evict_over_budget` after every successful
  rebuild. `evict_dead_siblings` keeps any cache whose recorded worktree path exists, and deletes
  with `shutil.rmtree(d, ignore_errors=True)`, the call whose win32 failure mode the docstring of
  `_remove_cache_dir` documents. `evict_over_budget` sorts candidates by `built_at` alone.
- The cache tree on node a, 2026-10-04, PINNED: four caches of 113 to 115 MB, about 455 MB under a
  512 MB budget, for seven registered worktrees; a fifth cache passes the budget, and every
  candidate is then a live sibling. All four recorded worktrees hold a `.git` file today, so S1 has
  no live husk to evict; the husk shape is the one the auto-memory note on `git worktree remove`
  records.
- The query log, 432 `query` rows on 2026-10-04: every row carries `worktree`, spelled as
  `str(repo)` by the same resolver that writes the manifest's `worktree`, and each of the four
  caches' worktrees names at least one row. The two strings join exactly. PINNED; AC5 re-derives it.
- Today each cache's last query is within minutes of its `built_at`, because every one was rebuilt
  on its last corpus move. The orders differ when a warm cache serves many queries without a
  rebuild, which is the case the report measured as a 6.5 to 15.5 s rebuild cost.
- `test_budget_lru` and `test_budget_protections` build siblings recording the current worktree,
  so with S4 those siblings share the run's own last query and the `built_at` tie-break keeps both
  arms' verdicts. `test_eviction` records a vanished path and the live repo, both unchanged by S1.

### Inventory

- `check_dead_worktree(wt)` and `load_last_queries(log)`, functions of `query.py`. The lexicon's
  `--suggest` answered `check_dead_worktree` as the replacement for an `is_` name and
  `load_last_queries` OK, both for cell `py.function`. A name the lexicon leg refuses at build
  time is replaced with its `--suggest` answer and this list amended with a rev bump.

### Files touched (estimate)

- `tools/memory-recall/query.py`
- `tools/memory-recall/selftest.py`
- `tools/memory-recall/README.md`
- `.memory-tree.conf`
- `memory/map/generated/symbols.json`

### Rollout

Units 31, 32 and 33 all write `tools/memory-recall/README.md`, so they build in order and never
concurrently. `.memory-tree.conf` is written by other units of this build; this unit touches only
the comment block above `RECALL_CACHE_BUDGET_MB`.

### Alternatives rejected

- **A last-query stamp file in each cache directory.** It adds a write to every query and a second
  record of a fact the log already holds.
- **Read `opened` rows too.** An `opened` row follows a `query` row of the same worktree, so it
  moves no cache's order.

## 5. Production-readiness checklist

- security — N/A — deletes only under `<git-common-dir>/recall/cache/`, through the existing
  manifest-last delete.
- perf / scale — one read of the query log per eviction pass, which runs only after a rebuild and
  only over budget; 1.4 MB today.
- error / empty / loading states — an absent or corrupt log falls back to `built_at` order; a
  failed dead-worktree delete is reported and its manifest kept for a later pass.
- observability — every eviction line names the last query and the build time it was ordered by.
- risks — a husk that is a worktree's directory mid-`git worktree add` has no `.git` yet. The
  dead pass runs only after this tree's own rebuild, and a cache directory exists only after a
  query from a tree that had one, so a mid-add directory holds no cache to lose.
- testing — new arms in `tools/memory-recall/selftest.py`, and direct in-process runs.
- migration — N/A — no stored data changes; old caches are read as they are.
- user docs — the README eviction paragraph and the conf comment, S6.

## 6. Acceptance criteria

- **AC1** — When a scratch script under the session scratchpad, run from the repo root, imports
  `query` from the kit directory and calls `evict_over_budget` on a scratch cache tree of a kept
  cache and three siblings whose `built_at` order is A, B, C and whose last queries put A newest,
  with a budget that forces one eviction, B is evicted, A and C survive, and the line names B's last
  query.
  Red when: A, the least-recently-built, is evicted.
- **AC2** — When the same script calls `evict_dead_siblings` on siblings recording a vanished path,
  an existing empty directory and the repo root, the first two are evicted and reported and the
  third survives; on win32, a sibling holding an open sqlite handle is reported `could NOT evict`
  and keeps its manifest.
  Red when: the husk survives, or a failed delete leaves a manifest-less directory.
- **AC3** — When `evict_over_budget` receives an empty map, it evicts in `built_at` order exactly as
  `test_budget_lru` expects.
  Red when: an empty or absent log changes the order.
- **AC4** — When `load_last_queries` reads a scratch log holding a malformed line, an `opened` row
  and two `query` rows for one worktree, it returns the newer `at` for that worktree and nothing
  else; for a path that does not exist it returns an empty map.
  Red when: it raises, counts the `opened` row, or keeps the older `at`.
- **AC5** — When `load_last_queries` reads the live log under `git rev-parse --git-common-dir` and the
  script reads each `manifest.json` under that directory's `recall/cache/`, every manifest's
  `worktree` is a key of the map.
  Red when: a live cache's worktree joins no row, which would silently fall back to `built_at`.
  figure: the cache and row counts DERIVED at observation time.
- **AC6** — When `grep -n "least-recently-queried" tools/memory-recall/README.md .memory-tree.conf`
  runs, it hits the README eviction paragraph and the conf comment, and
  `grep -n "2.4 MB" .memory-tree.conf` prints nothing.
  Red when: either text still says least-recently-built, or the typed figure survives.

## 7. Gates

`kit/dogfood doc parity` · `recall floor` · `transition-audit arms` · `straggler-guard arms` · `lexicon naming predicates` · `memory hygiene` · `recall floor arms` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-recall/selftest.py · siblings whose last-query order inverts their built_at order, a husk worktree, and an empty log, against today's built_at-only order · `SELFTEST_ARMS` moves by the arms added, with its dated `N -> M` provenance line

The first four are owed by `.memory-tree.conf`. `memory-recall kit selftest` and
`recall floor arms` run at the close: their guard, `tools/memory-recall/`, is excluded as broad.

## 8. Open questions

- **F1 — Where does "last query" come from?**
  Options: a stamp file each query touches in its cache directory; the query log's newest `query`
  row per `worktree`. Both order the same; the stamp adds a write per query and a second record of a
  fact the log holds, and every log row already carries the join key.
  RESOLVED (agent, 2026-10-04, delegated): the log join, S3.
- **F2 — Is a worktree with no `.git` dead?**
  Options: path existence only, today's rule; existence plus a `.git` entry. A primary tree holds a
  `.git` directory and a linked worktree a `.git` file, and an emptied husk holds neither.
  RESOLVED (agent, 2026-10-04, delegated): existence plus a `.git` entry, S1.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `ensure_cache`, both eviction passes and the live cache
  tree and query log.
- rev-2 · 2026-10-04 · §2 S7 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.
  S5 and the §7 arm line also move `SELFTEST_ARMS` with the new arms, as
  `TOOL-aMendedFleet-27` S5 moves it; the arm line said the floor moves by none.

## 10. Reuse audit

The seams extended are `evict_dead_siblings`, `evict_over_budget` and `_remove_cache_dir` in
`tools/memory-recall/query.py`, and the query log `log_event` writes. `python
tools/codebase-map/reuse_lookup.py "evict a per-worktree cache directory by least recent use when a
size budget is exceeded"` returned `cache_dir` and `ensure_cache` of this same file and
affordance-prose neighbours, none of which orders by use, so no existing seam fits beyond these.
Recall named `TOOL-aDrainedSluice-7`, which introduced the budget with least-recently-built order and
the whole-plan-first rule this unit keeps, `TOOL-aBatchedTribunal-6d`, the re-check at deletion it
keeps, and `TOOL-aQuarriedLantern-3`, the closed ask for the cap. Where the report and the tree
disagree: dead-worktree eviction already runs first, so "deleted worktrees first" is realised by
widening what counts as deleted, not by reordering the passes.

Recall terms used: `python tools/memory-recall/query.py "why does the recall cache evict the least
recently built sibling and not the least recently queried one" --terms "evict_over_budget
evict_dead_siblings RECALL_CACHE_BUDGET_MB built_at worktree manifest cache eviction
least-recently-built live sibling rebuild"`
