# TOOL-aMeasuredDrag-7 — the recall cache budget sized above two gov indexes, so two worktrees stop evicting each other

**Status:** SPECCED · rev-2 · 2026-11-15 · node a · Tier-1 · base aebbb4a7 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-2 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-8 |
| [2026-11-15-prompt-TOOL-aMeasuredDrag-7-1-builder.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-7-1-builder.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

One gov recall cache now outgrows half of `RECALL_CACHE_BUDGET_MB`, so a query in a second worktree
evicts the first worktree's cache, and that worktree's next query rebuilds it from scratch (finding
derived-1). This unit raises gov's own budget above two caches, so the two hottest worktrees keep
their caches. It also records the disk this costs and keeps the kit README's size claim true.

## 2. Scope (IN)

- **S1** — `.memory-tree.conf` sets `RECALL_CACHE_BUDGET_MB="2048"` in place of `"512"` (the value is
  F1's, see §7). Observed by AC1 and AC2.
- **S2** — The comment block above that key states the current measurement, the reason for the value
  and the disk it costs, and every other sentence in it stays as it is. Observed by AC4.
- **S3** — `tools/memory-recall/README.md` stops stating the stale upstream size, and points at the
  comment block S2 writes instead. Observed by AC4.
- **S4** — The same commit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`, because
  `.memory-tree.conf` is on its `watch:` list. Observed by AC5.

## 3. Non-goals (OUT)

- The kit default. `DEFAULT_CACHE_BUDGET_MB` in `tools/memory-tree/id_grammar.py` and the
  `.memory-tree.conf.example` value stay 512, so no adopter's budget moves.
- `evict_over_budget`, `ensure_cache` and every other line of `tools/memory-recall/query.py`.
- The content-keyed shared store the review names as the real fix, and `TOOL-dTotalRecall-21`, which
  would retire this key. That unit is DEFERRED and this one is its stopgap.
- A kit version bump. The lander mints it (`tools/govkit/govkit.py@37f075e4e93e:14044-14047`), so a
  branch owes none.
- Any page under `help/`. No page names this key or the cache size (grep over `help/` at `6d98c39ca`).
- Any `.memory-tree.conf` line outside the key's own comment block, so the `REFUSAL_CEILINGS` edit
  on the live run's branch (`.memory-tree.conf` line 653) still merges cleanly.

## 4. Design

### Evidence

Read at `6d98c39ca`. Every file cited here has the same blob at the base `aebbb4a7`.

- The key is `.memory-tree.conf@35c3d111603d:663`, under its comment block at `:655-662`. The block
  says a cache measured about 113 MB per worktree at `6e7022f3f`, which is no longer true.
- The budget reads through `tools/memory-tree/id_grammar.py@790b06816d0c:134-145` into
  `Conf.cache_budget_mb`. `Conf.digest` hashes the resolved values the budget is not part of
  (`:203-206`), so a new value invalidates no warm cache.
- `tools/memory-recall/query.py@807bb2decb8d:632-706` (`evict_over_budget`) runs after each build.
  It sums every cache under `recall/cache/` and, over budget, evicts the least-recently-queried
  sibling, never the current cache (`:741-757`).
- The one cache in this repo measured 402 MB, PINNED at `6d98c39ca` (`du -sm` over
  `<git-common-dir>/recall/cache`). Two caches are about 804 MB, PINNED at `6d98c39ca`, over the
  512 budget, so the second build evicts the first.
- The corpus under `memory/` grew from 46 MB at `6e7022f3f` (2026-10-05) to 173 MB at `6d98c39ca`
  (`git ls-tree -r -l`, PINNED). The cache grew from 113 MB to 402 MB over those same shas, so it
  grows at about 7 MB a day, PINNED over `6e7022f3f..6d98c39ca`.
- A rebuild took 32 s and 62 s, PINNED at `6d98c39ca` (the manifest's `built_s`, two builds that
  night). A warm query took 1.66 s beside 0.31 s for ten `/usr/bin/true`, PINNED at `6d98c39ca`.
- `tools/memory-recall/README.md@8eb805a81f25:126` states an upstream cache size and corpus size.
  Both are stale against the measurements above, PINNED at `6d98c39ca`.
- `memory/guides/SESSION-KICKOFF.md@a2190c75f7ef:7` lists `.memory-tree.conf` under `watch:`. The
  staged ratchet leg refuses a commit that stages a watched file without changing the block's
  `last-audit` value (`skills/session-kickoff/manifest-check.sh@4d3d63c0fad1:1971-1985`). No §B line
  of the manifest names this key or the cache size.

### The change

1. `.memory-tree.conf:663` becomes `RECALL_CACHE_BUDGET_MB="2048"`.
2. In the comment block at `:656-657`, the clause that gives the cache size measured at `6e7022f3f`
   is replaced by the facts below, wrapped at 100 columns. Each figure in the conf carries its sha on
   the same line, as every figure in this list does:
   - a cache here measured 402 MB at `6d98c39ca` (2026-11-15), up from 113 MB at `6e7022f3f`;
   - the old value held one cache at `6d98c39ca`, so two worktrees evicted each other
     (TOOL-aMeasuredDrag-7);
   - the new value holds two caches until each passes half of it, which is about three months at
     the growth rate over `6e7022f3f..6d98c39ca`;
   - the new value is also the most disk the cache tree may hold, four times the old ceiling.
   The rest of the block stays byte-identical.
3. `tools/memory-recall/README.md:126` loses the clause that gives upstream's cache size and corpus
   size. In its place it says the cache runs to more than twice the corpus it indexes, and that
   upstream keeps its measured size beside `RECALL_CACHE_BUDGET_MB` in its `.memory-tree.conf`.
   The 37.9% clause and the rest of the paragraph stay. Line 137's statement of the kit default
   stays true, because the kit default does not move.
4. `memory/guides/SESSION-KICKOFF.md:6` gets a new `last-audit` value, `<ISO datetime> @ <HEAD sha>`.
   The sha is the parent of the unit's commit, and the datetime is later than the current one. The
   commit message carries a delta line naming `.memory-tree.conf` and stating that no §B claim moved.

### What this does not check

- That each cache stays under half the budget. At the growth rate over `6e7022f3f..6d98c39ca`, two
  caches outgrow the recommended value in about three months. After that the eviction this unit
  stops comes back, and the shared store is the fix.
- Which two worktrees are the hottest. Eviction stays least-recently-queried first, so a third live
  worktree still evicts the oldest one.

### Sequencing

`memory/guides/SESSION-KICKOFF.md` is a shared record. Every unit in this build that changes a
watched file re-stamps it. So this unit's write set intersects theirs, and its pass runs in sequence
with them, never beside them (BUILD-METHOD M6 clause 3). Two unlanded branches also move the same
stamp line. The manifest's stamp-conflict rule reconciles that line at their landing.

### Alternatives rejected

- Raising the kit default in `id_grammar.py`. It moves every adopter's budget and is a kit contract
  change, which the build's non-goals exclude.
- Blank, which means uncapped. 34 worktrees exist (`git worktree list` at `6d98c39ca`), so the
  ceiling would be what every worktree's cache adds up to, and only the dead-worktree pass would
  bound it.

### Files touched (estimate)

- `.memory-tree.conf`
- `tools/memory-recall/README.md`
- `memory/guides/SESSION-KICKOFF.md`

## 5. Acceptance criteria

All commands run from the worktree root in Git Bash. `$SCRATCH` is the run's scratch directory,
spelled absolute. Each figure below is for 2048, the value F1 resolved.

- **AC1** — When the block below runs after the change, it prints `budget_mb 2048.0`, `lines []` and
  `sibling_kept True`. Before the change it printed `budget_mb 512.0`, one
  `evicted the least-recently-queried cache: sib` line and `sibling_kept False`, in this writer's run
  at `6d98c39ca`.
  Red when: the key still reads the old value, so the eviction line prints and `sibling_kept False`;
  or the line no longer parses, so `_budget` returns `None` and `budget_mb None` prints.
  fixture: two stub cache directories under `$SCRATCH/bp`, each with a manifest, and `_dir_bytes`
  stubbed to one gov cache's size. The probe deletes nothing outside `$SCRATCH/bp`.
  figure: PINNED. The stubbed size is the `du -sm` at `6d98c39ca`.

  ```bash
  rm -rf "$SCRATCH/bp" && python - "$SCRATCH/bp" <<'EOF'
  import json, pathlib, sys
  sys.path.insert(0, "tools/memory-recall")
  import query as q
  root = pathlib.Path(sys.argv[1]) / "cache"
  for name, at in (("hot", "2026-11-15T01:00:00+00:00"), ("sib", "2026-11-15T00:00:00+00:00")):
      (root / name).mkdir(parents=True, exist_ok=True)
      (root / name / "manifest.json").write_text(json.dumps({"built_at": at, "worktree": name}))
  q._dir_bytes = lambda d: 402 * 1048576
  print("budget_mb", q.CONF.cache_budget_mb)
  print("lines", q.evict_over_budget(root / "hot", q.CONF.cache_budget_mb, {}))
  print("sibling_kept", (root / "sib").is_dir())
  EOF
  ```

- **AC2** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-recall'); import query as q; c = q.CONF; print(c.digest(), sorted((s, str(getattr(c, s))) for s in type(c).__slots__ if s != 'cache_budget_mb'))"`
  runs before and after the change, the two outputs are byte-identical, and the digest is
  `718d6dd8e2cc`. So no other resolved recall value moved and no warm cache is invalidated by the key.
  Red when: the edit breaks the line above the key or the key itself, so another value or the digest
  differs.
  figure: PINNED. The digest is this writer's run at `6d98c39ca`.
- **AC3** — When the main loop times the warm query below twice after the pass commit, beside
  `time (for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done)`, the second run is the after figure.
  The `built_s` that `python -c "import json, sys; print(json.load(open(sys.argv[1]))['built_s'])" <cache>/manifest.json`
  prints is the before figure, the cost an evicted sibling pays. Both go in the acceptance ledger.
  The query is `python tools/memory-recall/query.py "recall cache budget" --terms "RECALL_CACHE_BUDGET_MB evict_over_budget cache worktree byte budget recall built_at husk" --k 3`.
  Red when: the second run still rebuilds, so it prints a rebuild cause and costs about `built_s`.
  cost: one rebuild, about 32 s to 62 s, PINNED at `6d98c39ca`, because the conf is a recall source.
  figure: DERIVED at observation time.
- **AC4** — At `6d98c39ca` `grep -n "measured about 113 MB\|~115 MiB" .memory-tree.conf tools/memory-recall/README.md`
  prints the two stale clauses, `:656` and `:126`. After the change it prints nothing, so the new
  text must not say "measured about" before the old figure. When
  `grep -n "402 MB" .memory-tree.conf` runs, it prints one comment line that also carries `6d98c39ca`. `git diff HEAD~1 -- .memory-tree.conf` shows changed lines only between
  the block's first line and the key.
  Red when: the stale figure survives in either file, or the edit reaches line 653 or 664.
- **AC5** — When `git diff HEAD~1 HEAD -- memory/guides/SESSION-KICKOFF.md` runs on the unit's commit,
  it shows exactly one changed line, `last-audit:`, and its sha equals `git rev-parse HEAD~1`.
  Red when: the stamp is missing, so the staged ratchet leg refuses the commit, or the line names
  another sha.

## 6. Gates

`kickoff-manifest ratchet` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms`

`python tools/check-spec-tokens.py --legs-for` over the three files touched, run at `6d98c39ca`,
names the last five. The other legs it names sit under the broad `tools/` guard. The ratchet leg is
unguarded and is a pass leg, and it is AC5's leg. `recall floor` reads the conf, which is a recall
source, so the comment edit is one chunk it ranks. No arm is added or moved.

## 7. Open questions

- **F1 — Which value does `RECALL_CACHE_BUDGET_MB` take?**
  RESOLVED (agent, 2026-11-15, delegated): (b) 2048 — the longest-lasting bounded value; no veto
  applies.
  The brief asks for a value above two gov caches. Two caches are 804 MB, PINNED at `6d98c39ca`, and
  each grows about 7 MB a day, PINNED over `6e7022f3f..6d98c39ca`.
  - (a) `1024`. Two caches fit for about 16 days at the rate PINNED over `6e7022f3f..6d98c39ca`, and
    the disk ceiling doubles. Eviction between two worktrees returns soon after the unit lands.
  - (b) `2048`. Two caches fit for about 89 days at the rate PINNED over `6e7022f3f..6d98c39ca`, and
    five fit at the size PINNED at `6d98c39ca`. The disk ceiling is four times the old one.
  - (c) Blank, uncapped. Nothing is evicted by size, and the disk is bounded only by the number of
    live worktrees, 34 at `6d98c39ca`.
  Recommendation: (b). It keeps the goal true longest. The budget is also the disk ceiling, so its
  cost is stated and bounded, and (c) has no bound. Every AC above is written for (b).

## 8. Revision log

- rev-1 · 2026-11-15 · initial draft from the build brief
  `2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief`, item 7, grounded at `6d98c39ca`, whose cited files
  match the base `aebbb4a7`.
- rev-2 · 2026-11-15 · §5 · §7 · F1 resolved as (b) 2048 under the run's delegation
  (`2026-11-15-prompt-TOOL-aMeasuredDrag-1-ruling-brief`), so the §5 preamble drops the option (a)
  figure. S1 to S4 and AC1 to AC5 were already written for 2048. The status moves to SPECCED, as
  the build's other Tier-1 specs read.

## 9. Reuse audit

The seam is the key itself, `.memory-tree.conf` `RECALL_CACHE_BUDGET_MB`, read by
`tools/memory-tree/id_grammar.py#_budget` and spent by `tools/memory-recall/query.py#evict_over_budget`.
Nothing is built. `python tools/codebase-map/reuse_lookup.py "recall cache byte budget eviction across worktrees"`
ranked `evict_over_budget`, `ensure_cache` and `build_cache` in `tools/memory-recall/query.py`, the
mechanism this value feeds. Recall returned TOOL-aDrainedSluice-7, which set the 512 default, and
TOOL-aMendedFleet-32, which made eviction least-recently-queried. It also returned
TOOL-dTotalRecall-21 (DEFERRED), which would retire the key, so this value is its stopgap.

Recall terms used: `python tools/memory-recall/query.py "what decided the recall cache byte budget and how large a worktree cache may grow" --terms "RECALL_CACHE_BUDGET_MB evict_over_budget least-recently-queried cache worktree byte budget recall built_at husk"`
