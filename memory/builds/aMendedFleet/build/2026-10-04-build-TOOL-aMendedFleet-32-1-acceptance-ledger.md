# TOOL-aMendedFleet-32 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-32

**Evidences:** TOOL-aMendedFleet-32
- AC1 — `evict_over_budget` — a scratch script under the session scratchpad, run from the repo root with the kit directory on `sys.path`, built a kept cache and siblings A, B, C of 150 KB built in that order, gave it last queries with A newest, and called it at 0.4 MB: B was evicted, A and C survived, and the line read `last query 2020-06-01T00:00:00+00:00, built 2020-02-01T00:00:00+00:00`. RED first against the parent's `query.py` in a fixture repository under `%TEMP%/a32o`: A was evicted on the least-recently-built line
- AC2 — `evict_dead_siblings` — the same script's siblings recording a vanished path, an existing empty directory and the repo root: the first two were evicted and returned, the root's survived; a fourth sibling of a vanished worktree holding an open sqlite handle printed `could NOT evict the cache of dead worktree` and kept its `manifest.json`. RED first on the parent: the husk survived
- AC3 — `evict_over_budget` — with an empty map, a 400 KB sibling built 2020 was evicted before a 100 KB one built 2021, the order `test_budget_lru` expects, on the parent and on the change alike, the line naming `last query never`
- AC4 — `load_last_queries` — over a scratch log of a malformed line, an `opened` row and two `query` rows for one worktree it returned that worktree's newer `at` alone, and an empty map for an absent path. RED on the parent: no such function
- AC5 — `git rev-parse --git-common-dir` — the live log's map, read at observation time, held 57 worktrees, and each of the 4 `manifest.json` files under `recall/cache/` named one of them
- AC6 — `grep -n "least-recently-queried"` — hit `tools/memory-recall/README.md` line 106 in the eviction list and `.memory-tree.conf` line 581 in the comment above `RECALL_CACHE_BUDGET_MB`; `grep -n "2.4 MB" .memory-tree.conf` printed nothing and exited 1

## The arms

- `test_budget_lru` and `test_budget_blank` assert the new `least-recently-queried` wording.
  Three arms are new: `test_budget_orders_by_last_query`, `test_eviction_husk` and
  `test_last_queries_and_empty_log`, and `SELFTEST_ARMS` moves 77 -> 80 with its provenance line.
  The seven eviction arms ran alone through a scratch script that compiled only those functions
  out of `selftest.py`: all seven passed on the change, and the three new ones failed against the
  parent's `query.py` in the `%TEMP%/a32o` fixture. The suite itself did not run.

## Owed at the close

- `memory-recall kit selftest`, `recall floor` and `recall floor arms`, whose guard is the kit
  directory, and the arm-count pin and its provenance chain, which only the suite grades.
- `kit/dogfood doc parity`, `transition-audit arms`, `straggler-guard arms`, `lexicon naming
  predicates`, `memory hygiene`, `codebase-map coverage + freshness` and `spec tokens`.
  `gen_map.py --check` exited 0 after `--write`; `lexicon.py --suggest` answered OK for both new
  functions and the three new arms; `encoding_posture.py` reported no undeclared site.
- The memory-recall kit version bump owed by the README and code edits, per the brief.
