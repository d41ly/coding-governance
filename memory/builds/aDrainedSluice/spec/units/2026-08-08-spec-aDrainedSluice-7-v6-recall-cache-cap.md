# TOOL-aDrainedSluice-7 — V6: the recall cache is bounded

**Status:** INPROGRESS · rev-1 · 2026-08-08 · node a · Tier-2 · base 76fcd09b · streams tooling

## 1. Goal

`memory-recall` writes one cache directory per worktree under the common git dir and evicts only
those whose worktree is GONE. Caches for live worktrees accumulate without limit — upstream measured
552.6 MB across five directories with only 37.9% evictable by the dead-worktree rule. Give the cache
a byte budget and evict least-recently-built first.

## 2. Scope (IN)

- **S1** — a byte budget over the whole `recall/cache/` tree, from `.memory-tree.conf`'s
  `RECALL_CACHE_BUDGET_MB`, defaulting to a value MEASURED against this repo with headroom. Blank
  disables the cap, matching every other knob in this kit.
- **S2** — eviction runs after a successful build, never before: a cache is only replaceable once its
  replacement exists. It evicts LEAST-RECENTLY-BUILT first, reading `built_at` from each manifest.
- **S3** — three things are NEVER evicted, and each has a reason that is not "it seemed safer":
  the CURRENT worktree's cache (evicting it makes the budget a rebuild loop); a directory with no
  READABLE manifest (that is the shape of a sibling mid-first-build, because the builder writes both
  databases before the manifest, atomically); and a manifest with no `built_at` (absence of evidence
  is not evidence of age).
- **S4** — eviction is REPORTED, one line per evicted directory with its worktree and `built_at`. A
  cache that vanishes silently is indistinguishable from one that was never built, and the next
  session pays a rebuild it cannot explain.
- **S5** — the existing dead-worktree eviction runs FIRST and unconditionally. It is free correctness;
  the budget is the second pass over whatever survives.
- **S6** — when the budget cannot be met without evicting a protected directory, the cap does NOT
  force it. It reports that the budget is exceeded and by how much, and leaves the tree alone. A cap
  that deletes the current worktree's cache to satisfy itself is worse than an unbounded cache.
- **S7** — the selftest arms: eviction order by `built_at`, the current cache surviving, an
  unreadable manifest surviving, a `built_at`-less manifest surviving, the report naming what went,
  and the cannot-satisfy case reporting instead of over-evicting.

## 3. Non-goals (OUT)

- A time-based expiry. Age alone does not make a cache useless — a worktree touched once a month is
  still live, and its cache is still correct. Size is the resource under pressure, so size is the
  budget.
- Capping `queries.jsonl`. It is a log, it is small, and it is the input to the kit's own bench.
- Evicting across repos. The cache tree is per common-git-dir; another repo's is not this repo's to
  delete.

## 4. Design

### Data model

```
budget      : RECALL_CACHE_BUDGET_MB from .memory-tree.conf; blank = uncapped
size        : recursive byte size of recall/cache/
protected   : the current dir · any dir with no readable manifest · any manifest without built_at
candidates  : the rest, sorted by built_at ASCENDING (oldest first)
```

### Inventory

| Concern | Today | After |
|---|---|---|
| dead-worktree eviction | `evict_dead_siblings` | unchanged, runs first |
| live-cache growth | unbounded | budgeted, LRU by `built_at` |
| reporting | dead evictions returned | both kinds reported, one line each |
| the knob | none | `RECALL_CACHE_BUDGET_MB`, measured |

### Migration

None. An existing cache is either under budget or is evicted on the next build, which is a rebuild
and not a loss.

### Rollout

One commit: the budget, the eviction pass, the report, the conf key, the selftest arms.

### Files touched (estimate)

`tools/memory-recall/query.py`, `tools/memory-recall/selftest.py`, `.memory-tree.conf`, the kit
README.

### Alternatives rejected

- **Evict by directory size, largest first.** Rejected: it frees the most bytes per deletion and
  destroys the most work per deletion. The largest cache is the largest corpus, which is the one
  most expensive to rebuild.
- **Evict before building.** Rejected: it can delete the only usable cache in the tree and then fail
  to build a replacement.
- **Cap per directory rather than over the tree.** Rejected: the resource under pressure is the git
  dir's total footprint, and a per-directory cap does not bound the number of directories.

## 5. Production-readiness checklist

- security — N/A. Deletes only inside the kit's own cache tree.
- perf / scale — one stat walk over the cache tree per build, which already happens for freshness.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an empty cache tree, a blank budget and an unreadable manifest are
  all handled without deleting anything.
- observability — every eviction is reported with its worktree and `built_at`.
- risks — DATA LOSS is the risk, bounded three ways: only inside `recall/cache/`, never the current
  or unreadable or ageless directory, and never past the budget's requirement.
- testing + left-shift gates — six selftest arms, including the two never-evict cases and the
  cannot-satisfy case.
- migration / rollback — one commit; the cache is derived data.
- user docs — the kit README states the budget, its default and what it deletes.

## 6. Acceptance criteria

- **AC1** — When the cache tree exceeds the budget, the oldest-`built_at` evictable directory goes
  first, and eviction stops as soon as the tree is under budget.
- **AC2** — When eviction runs, the current worktree's cache survives regardless of its age.
- **AC3** — When a sibling has no readable manifest, it survives — that is a build in progress.
- **AC4** — When a sibling's manifest has no `built_at`, it survives.
- **AC5** — When the budget cannot be met without touching a protected directory, nothing is deleted
  and the shortfall is reported with both numbers.
- **AC6** — When anything is evicted, each deletion is reported with its worktree and `built_at`.
- **AC7** — When `RECALL_CACHE_BUDGET_MB` is blank, no size-based eviction runs at all.
- **AC8** — When `python tools/memory-recall/selftest.py` runs, every arm above has a red and a green
  side and the pass line prints last.

## 7. Gates

`bash tools/run-gates.sh`; the `memory-recall kit selftest` leg carries this unit.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — the default budget.** Options: inherit upstream's measured 552.6 MB across five
  directories, or measure here. RESOLVED (owner, 2026-08-08): measure here. This repo's single cache
  is 1.9 MB; the default is set well above any plausible single-corpus cache so the cap protects an
  adopter with many worktrees without ever firing on a normal one, and the number is recorded.
- **Fork B — what happens when the budget cannot be met.** Options: evict anyway, or report.
  RESOLVED (owner, 2026-08-08): report. A cap that deletes the running session's own cache to satisfy
  itself turns a size problem into a rebuild loop, and the operator learns nothing.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.

## 10. Reuse audit

The eviction pass sits beside `evict_dead_siblings`, reuses `read_manifest`, and reuses that
function's never-evict-without-a-readable-manifest rule verbatim — the reasoning is already written
there and this unit extends it rather than restating it. The budget follows the measured-knob
convention (`.memory-tree.conf`, blank disables) that `corpus_ids.py` and `gotchas.py` already use;
memory-recall already reads that conf and declares none of its own, deliberately, so no new config
file appears. The arms go into the kit's existing selftest.
