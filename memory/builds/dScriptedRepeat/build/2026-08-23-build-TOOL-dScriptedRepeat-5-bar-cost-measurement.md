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
  **SUPERSEDED** by TOOL-dScriptedRepeat-15's S1: 22 s was a REAL-REPO reading, which includes a
  network observation of `origin` that the fixture does not make. In the fixture, where all 243 of the
  suite's invocations actually happen, it is 10.7 s on a quiet node.
- That suite carries roughly eighty arms. 80 × 22 s is the leg, near enough.
  **SUPERSEDED**: the suite makes **243** checker invocations, not eighty. Eighty was the arm count of
  one region. `grep -c '$(run)' tools/unattended/check-unattended.test.sh` → 243.
- One check run was **13 s** before the round-6 gate rewrite. The +69% is 28b's widened population:
  ten template keys against seven kit scripts is seventy `grep` invocations that did not exist before,
  and MSYS process spawn is tens of milliseconds each.
  **SUPERSEDED as a measurement, upheld as a mechanism.** The 13.2 s was a QUOTIENT — 3199 s ÷ 243 —
  presented as a reading, and its divisor disagreed with the ledger's own 846.0 + 2013.7 = 2859.7 s
  for the sharded pair. The mechanism it named was right, and S1 below measures it directly.
- Two further claims made in this build's prose and never in this file are recorded here so they die
  where the rest of the model lives. **"~28× more work than the question needs"**: not measured, and
  wrong — `--skip 28` costs 6.8 s against a 21.7 s full run in the same fixture, so the ratio is about
  2×. **"~23 min of per-arm fixture reset"**: `reset_tree` is **0.123 s**, so 248 of them are 30 s,
  not 23 minutes.

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

## S1 — the profile TOOL-dScriptedRepeat-15 took before changing one line

Node `d`, 2026-08-23. Every figure below carries the command that produced it, because the four
superseded claims above were all produced by reasoning instead. The probes are built by taking the
suite's own setup — `sed -n '1,226p' tools/unattended/check-unattended.test.sh` — and appending a
measurement tail, so every reading is taken **inside the fixture the 243 invocations actually run in**.

### The invocation is not compute-bound, and that is the whole finding

```
time bash "$SCRIPT"          # inside the fixture
real 14.4s   user 0.33s   sys 0.62s
```

Under one second of CPU in a fourteen-second run. The leg spends 93% of its life waiting, and what it
waits on is **process creation**. An on-access antivirus scanner sits in front of every `exec` on this
node — `ekrn`, ESET's scanning service, was the top CPU consumer on the box at 4529 s while these
readings were taken, with the machine at 80% load. Measured directly:

```
i=0; while [ $i -lt 100 ]; do grep -q x /dev/null; i=$((i+1)); done   # 0.019-0.039 s per spawn
i=0; while [ $i -lt 20 ]; do o=$(bash -c 'f(){ :; }; f'); i=$((i+1)); done   # 0.032 s per spawn
i=0; while [ $i -lt 100 ]; do o=$(echo hi); i=$((i+1)); done          # 0.010 s per fork, no exec
```

A spawn costs roughly a millisecond on a machine without an on-access scanner. Here it is twenty to
forty times that, and the leg makes 469 of them.

### The spawn count, which is the term this repo owns

```
PS4='+ ${EPOCHREALTIME} ${LINENO} ' bash -x "$SCRIPT" 2>trace.txt   # inside the fixture
```

469 external process spawns per invocation before this unit; 220 after. Counted from the trace both
ways, not estimated. 469 × 0.022 s = 10.3 s against a 10.7 s measured invocation — the model
reproduces the reading, which is why it is worth trusting for the projection below.

### Where they were, and where the time actually was

Per-region timestamps, by inserting `printf "MARK %s %s\n" <tag> "$EPOCHREALTIME" >&2` before each
`# ---- N` header and before each parser loop, then running once in the fixture. On a quiet node,
total 10.74 s:

| region | seconds | note |
|---|---|---|
| preamble → check 14 | 1.03 | conf parse, remote-observation setup |
| check 14 region | 0.88 | includes the `ls-remote` observation |
| checks 7–25 | 2.32 | |
| check 26 | 0.13 | after this unit; three greps per verb before it |
| check 28a/28b | 1.10 | |
| 28c + sha scan | 0.47 | |
| **the four parser specimen loops** | **5.02** | 34 `bash -c` spawns at 0.148 s each |

**A LINE-LEVEL `set -x` PROFILE LIED ABOUT THIS AND THE LIE IS INSTRUCTIVE.** Its seconds attributed
4.33 s to 28b's two grep lines and 8.35 s to the parser loops, out of a traced 28.5 s against an
untraced 11 s. Tracing writes one line per command to a file, so its overhead lands on whichever line
comes next and is therefore proportional to CALL COUNT. It was a call-count profile wearing a time
profile's clothes, and acting on its seconds produced a change that cut 231 greps and moved the wall
clock by nothing measurable. The per-region timestamps above cost 18 writes and are what the decision
was finally made on.

### The three suite wall readings S1 asked for, and why only one exists

The unsharded reading and the two `--shard i/2` readings were NOT taken. The owner stopped these
suites after two days of repeated runs and that instruction stands, so this unit derives the suite
cost from the two things it did measure — the spawn count and the per-spawn cost — rather than
running the thing again to time it. The one recorded suite reading remains `<git-dir>/gate-ledger.tsv`'s
sharded pair, 846.0 + 2013.7 = 2859.7 s, from before the removal.

Scaled by the spawn ratio: 2859.7 × 220/469 = **1342 s**. From the other direction, 243 invocations
× 5.2 s projected + about 40 s of fixture work lands in the same place. That is the number the
re-declared ceiling in `tools/unattended/run-unattended-gates.sh` is written against, and that file
says in its own words that the figure is derived and not observed.

### What was measured instead of the suite

17 staged breaks, 16 of them red, run through the pre-unit and post-unit checker over the same tree:
output and exit status byte-identical in every case, including both shapes of broken parser — an
emptied body and a syntax error — which are the two the batched harness had to keep indistinguishable
from the unbatched one.
