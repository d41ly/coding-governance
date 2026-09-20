# The first full-population sweep, and the claim it refutes

**Serves:** journal TOOL-aPooledSweep-1

**Evidences:** TOOL-aPooledSweep-1

- AC6 — AMENDED rev-3 — the overlap criterion is met and the criterion was never the problem. What
  this run refutes is the BUILD's framing, not a numbered criterion, so it is recorded here rather
  than by flipping a MET line: `bash tools/run-gates/run-selftests.sh --sweep` over all 59 rows ran
  4h39m and did not finish, against a build that called 2.5h a success.

Node `a`, started 2026-09-07T17:13:39Z, killed by the owner's call at 4h39m with 58 of 59 verdicts
written. Per-row data: `2026-09-08-build-TOOL-aPooledSweep-1-full-sweep-rows.tsv` beside this file.

## The result

| | |
|---|---|
| wall at the kill | **16772 s (4h39m)**, still running slot 55 of 59 |
| green | 40 |
| **killed at their own derived bound (`rc=124`)** | **14** |
| genuinely failed (`rc=1`) | 4 |

**Fourteen suites were killed by the bound this build derived for them**, including four recorded in
seconds: `line-length gate selftest` (recorded 8 s, killed at 121 s), `run-selftests self-test`
(28 s → 122 s), `unattended adopter e2e` (38 s → 122 s), `codebase-map adopter e2e` (46 s → 143 s).
Three to fifteen times their serial readings. `sweep-ceiling-factor: 2` sits on budgets measured
under the SERIAL runner, and at width 8 on a node whose spawn path is serialised that headroom is
not close to enough. The mode as shipped kills a quarter of its own population and reports RED for
it. Part of the window also carried another worktree's `run-selftests --kit tools/unattended`, and
this run cannot separate that from pool contention.

## The claim it refutes, which is this build's own

The ledger beside this file says "roughly ten hours to two and a half" as though that were the win.
It is not: 2.5 h is not a check anybody runs either, so the build reached a target that was already
too slow and I wrote it up as success.

**And the ceiling was never about width.** One suite is 25.1% of the whole population, so
`floor = max(total/width, largest)` is pinned by the second term at every width:

| width | total/width | largest | floor |
|---|---|---|---|
| 8 | 4518 s | 9067 s | **2.52 h** |
| 16 | 2259 s | 9067 s | **2.52 h** |
| 32 | 1129 s | 9067 s | **2.52 h** |

Buying more parallelism buys nothing. Pooling was necessary and is nowhere near sufficient, and no
amount of scheduling reaches minutes while one member is 2.5 hours long.

## What the cost actually is

`run-unattended-gates.sh` already measured it and nobody joined it to this: one invocation of
`check-unattended.sh` inside its own fixture reported `real 14.4s user 0.33s sys 0.62s` — **93% of
it waiting, not working** — and the suite invokes the checker **243 times** at **220 spawns each**
after `TOOL-dNarrowedAnchor-1` cut it from 469. That is about **53,000 process creations**. Measured
on this node this session, a bare `bash -c :` costs **190 ms**.

    53,000 x 0.19 s = 10,070 s     against a recorded 9067 s

The model accounts for the whole reading within 12%. **The population costs ten hours because it
forks, and on this node a fork costs 190 ms.**

That also explains the fourteen kills: a pool contends on precisely the resource the work is made
of, so widening it inflates every member. Scheduling and the bottleneck are the same resource.

## The lever, and the one this build picked

Two mechanisms, and this build conflated them:

- **SCHEDULING** — run suites, or arms, concurrently. Measured here: 1.72x for the pool over nine
  suites, 4.03x for the one suite ported onto `lib-selftest.sh` (31.9 s to 7.9 s, the budgets header
  records both). Ceiling is the width, eroded by the contention above, and floored by the largest
  member.
- **DE-SPAWNING** — stop forking per item inside the checker; read each file once. Measured here:
  `check-pass-order.sh` 10184 s to 111 s as the portability survey records it (an earlier reading in
  session notes says 510 s — one to two orders of magnitude either way), and
  `TOOL-aQuenchedHarness-7` 5420 processes to 2321 on the longest leg. No width ceiling, no arm
  rewrite, no assertion vocabulary, and it removes the contention rather than fighting it.

`TOOL-aPooledSweep-7` records the port programme as "superseded for cost". That is wrong and this
record supersedes it. The port's GOAL was right — take work out — and only its VEHICLE was wrong:
porting onto a parallel harness is scheduling wearing a work-reduction costume, which is why it
measured 4x and why its assertion contract fought every suite it touched. De-spawning is the same
goal without the vehicle.

## What that makes the next build

Cutting `check-unattended.sh` from 220 spawns per invocation to roughly 20 — the same act
`274aa39b` performed on `check-pass-order.sh` — takes its suite from 9067 s to about 900 s. The
population's floor then falls to 2569 s, the next-largest member, and the same act on the next two
takes it under 2547 s. Only then does width matter, and only then is the pool worth the wall it
already buys.

Order, by share: `unattended gate selftest` 25.1%, then `unattended driver selftest`,
`manifest-check self-test`, `run-gates canary`, `run-gates turnstile` — the top five are 52.7%.

## What stays true

`--sweep` is not withdrawn. It is correct, it is bounded, its verdicts matched the serial mode's on
every suite of the nine-suite A/B, and it is the right consumer of a de-spawned population. It is
simply the second-order lever, applied before the first-order one, and the bound it derives needs
re-sizing against pooled rather than serial readings before it is usable at width 8.
