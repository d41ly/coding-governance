**Serves:** journal TOOL-dScriptedRepeat-5

# What this build did to the merge bar's wall clock, measured

Node `d`, 2026-08-23. Read from `<git-dir>/gate-ledger.tsv`, which the runner writes one row per leg
with its own seconds. Nothing here is estimated.

## The headline

**The bar is no longer throughput-bound. It is FLOOR-bound on one leg, and that leg is mine.**

| | 2026-08-21, before this build's review rounds | 2026-08-23, after round 6 |
|---|---|---|
| wall clock, warm | 393 s | ~40 min |
| leg-seconds total | 3085 s | 4926 s |
| longest single leg | 336 s | **1565 s** — `unattended gate selftest shard B` |

The 2026-08-21 pair is the controlled measurement recorded in `AGENTS.md`; the 2026-08-23 column is
this run's ledger. Wall clock cannot go below the longest leg however wide the pool is, so a 1565 s
leg puts a 26-minute floor under every full bar on this machine.

## Where the time is

    1565.4  unattended gate selftest shard B
     692.6  unattended gate selftest
     554.8  unattended driver selftest shard B
     278.4  unattended driver selftest
     243.6  run-gates canary
     166.0  playbook validity selftest
     139.2  run-gates evidence
     138.8  run-gates turnstile

The unattended and playbook legs together are **3412 s of 4926 s — 69% of all leg-seconds**. Fifty of
the ninety-two legs finish in under five seconds each.

## Why a microscopic repo costs this

Nothing here scales with source size. The bar is not reading this repo; it is RUNNING the kits against
hermetic fixtures, and the cost is arm count multiplied by process spawns per arm:

- Every arm in `check-unattended.test.sh` stages a break, runs `check-unattended.sh` end to end, and
  resets a scratch git tree. One check run is **22 s** on this machine.
- That suite carries roughly eighty arms. 80 × 22 s is the leg, near enough.
- One check run was **13 s** before the round-6 gate rewrite. The +69% is 28b's widened population:
  ten template keys against seven kit scripts is seventy `grep` invocations that did not exist before,
  and MSYS process spawn is tens of milliseconds each.

So the growth has two multiplicands and this build pushed both. Rounds 4 through 6 added about fifty
arms to that one suite while making each arm's check 69% slower.

## What that buys, stated plainly so the trade is visible

Those arms are the twelve staged breaks and two controls behind check 28's three structural rules,
plus six liveness statements. Rounds 4, 5 and 6 each found the previous round's gate vacuous, and the
arms are what stopped that. The cost is real and so is the coverage; this record exists so the next
person deciding what to prune knows which is which.

## The levers, cheapest first

1. **Shard that suite further.** It is already `--shard i/2`; the ledger shows shard B at 1565 s
   against shard A at 692 s, so the split is badly unbalanced before it is even widened. Rebalancing
   alone would take the floor to roughly 1100 s; going to four shards takes it near 550 s.
2. **Stop re-running the whole checker per arm.** Most arms only need one check's verdict, not all
   twenty-eight. A `--only 28` argument would cut the dominant term directly, and is the single
   biggest win available.
3. **Cache the scratch tree.** Each arm reconstructs a git fixture; a template reused across arms in
   one process would remove most of the spawn count.

None of these is in scope for this build. Filed rather than done.
