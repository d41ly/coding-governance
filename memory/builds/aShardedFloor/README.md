---
slug: aShardedFloor
node: a
opened: 2026-08-21
streams: tooling
roster: TOOL
ids: TOOL-aShardedFloor-1 TOOL-aShardedFloor-2 TOOL-aShardedFloor-3 TOOL-aShardedFloor-4
---

# aShardedFloor — move the floor, then see the queue

Node `a` · opened 2026-08-21 · streams tooling.

`aScannedThrottle` measured this repo's merge bar and landed a report; it changed nothing, by design.
This build lands the recommendations that report ranked. Its own headline finding binds everything
here: **the bar is FLOOR-bound.** One leg exceeds leg-seconds ÷ width on every reconstructed bar, so
no width change, no extra worker and no faster sibling leg moves the span. Only the floor moves it.

## What this build does, in landing order

**The order is authored here and is not a preference.** `TOOL-aShardedFloor-1`, then
`TOOL-aShardedFloor-2` and `TOOL-aShardedFloor-3` as ONE landing, then `TOOL-aShardedFloor-4`.
The mechanism behind the last step, not just the sequence: the runner sorts dispatch by negative
cached duration and a leg the cache does not know scores 0 and sorts LAST, so a new shard name
dispatches dead last on a warm ledger — and unit 4's whole job is warming every worktree's ledger.
Landing 4 before 2 and 3 makes the shard rename penalty worse, not better.

**Sharding the two `unattended` selftests is the whole win on the measured bar's span at the
floor** — 292 s (27.6 %) on one bar and 282 s (30.5 %) on another. **Both must move together**:
sharding the driver alone buys 3.7 %, because the gate selftest simply becomes the new floor. Two
shards each is sufficient, and past that the bar is throughput-bound at ~766 s and further splitting
buys exactly zero. The measured driver seam splits 63/37, so the headline is what a 63/37 split
buys, not what an even one would.

**Unit 4 is a separate, additive scheduling win** and belongs in this section rather than only in
the exclusions below: 15.6–16.3 % of span on any cold worktree, measured as a controlled pair with
the floor leg's dispatch rank moving from 55/87 to 1/87. **The two wins are measured over different
populations and adding them is not honest.**

The queue key buys **0 s of span** and ships anyway: a lander queueing behind one peer experiences
~31–35 min where every span the report measured reads ~16, and today that wait is printed to stdout
and recorded nowhere.

## How it closed

Three units landed, one went WONTDO, and the reason the fourth did is the most useful thing this
build produced: **its own siblings destroyed its business case.** Sharding took the bar from
FLOOR-bound to THROUGHPUT-bound, and `TOOL-aShardedFloor-4`'s entire mechanism is starting the
FLOOR leg earlier. Re-measured as a controlled pair it buys 38.5 s / 8.9 %, not the 15.6–16.3 %
it was approved on. The design is intact and `TOOL-aScannedThrottle-8` now carries the re-priced
figure, so a later session prices it from 8.9 % rather than from a number this build invalidated.

The measured end state, from the bar's own run record: **span 393 s, leg-seconds 3085, longest leg
336 s** against a throughput bound of 386 s. The floor was ~660 s before this build.

**A finding this build did not set out to make.** Every figure it corrected was wrong the same
way — measured once, in conditions that did not hold, and written where it read as authoritative.
That includes one of its own: the charter pair landed at `e78da2b` came from a worktree bar that
did not reproduce, and was corrected one landing later. The rule the charter already states —
point at the source, or gate the pair — is the one this build kept re-learning.

## Owner decision, as it stood

**`TOOL-aShardedFloor-4` cannot land until this is answered, which is why its spec reads BLOCKED.**

Sharing the dispatch hint takes time-to-first-signal from **5.1 s to 669.1 s** — a 131x swing,
measured, decided solely by ledger warmth. Today most worktrees are ACCIDENTALLY protected by having
no hint at all; the unit removes that protection everywhere at once. So a real 16 % span win reads as
a large regression to the person who filed the complaint that started `aScannedThrottle`, and that
complaint was about PERCEIVED latency.

- **Wait** for a reserved short-leg slot (`TOOL-aMeteredTurnstile-5`) — dispatch longest-first into
  width-1 workers while one worker pulls shortest-first, which leaves makespan unchanged because the
  floor leg still starts at t=0. Nobody has designed it.
- **Ship** unit 4 with the regression documented, and take the coverage line as the explanation. It
  explains the silence; it does not remove it.

A second question rides with it: does the legacy filename fallback expire, or stay permanent?
Measured at 78.4 % coverage today, so it is worth something now and worth nothing once every worktree
has run a bar.

The design, its measurements and every gate pin each unit moves are in
[the research record](build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md). The specs cite it rather
than restating it.

## What this build does NOT do

It does not widen the pool, shard a third time, or touch `gate-profiles.txt` — all three are measured
dead ends in that report. It does not fix `input_key`'s tree-not-commit hole, which
`TOOL-aShardedFloor-4` would make routine rather than rare; that is its own unit and its own risk.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aShardedFloor-1` | 2 | record the turnstile queue wait in the run record |
| 2 | `TOOL-aShardedFloor-2` | 2 | the shard contract, and the driver selftest split by it |
| 3 | `TOOL-aShardedFloor-3` | 2 | the gate selftest, split by the same contract |
| 4 | `TOOL-aShardedFloor-4` | 2 | the dispatch hint reads a repository-wide store |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 4 unit(s) · node a · opened 2026-08-21 · streams tooling
ids TOOL-aShardedFloor-1 TOOL-aShardedFloor-2 TOOL-aShardedFloor-3 TOOL-aShardedFloor-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aShardedFloor-1 — record the turnstile queue wait in the run record](spec/2026-08-21-spec-TOOL-aShardedFloor-1.md) | — | 2 | CLOSED | rev-2 | 2026-08-21 |
| [TOOL-aShardedFloor-2 — the shard contract, and the driver selftest split by it](spec/2026-08-21-spec-TOOL-aShardedFloor-2.md) | — | 2 | CLOSED | rev-4 | 2026-08-21 |
| [TOOL-aShardedFloor-3 — the gate selftest, split by the same contract](spec/2026-08-21-spec-TOOL-aShardedFloor-3.md) | — | 2 | CLOSED | rev-4 | 2026-08-21 |
| [TOOL-aShardedFloor-4 — the dispatch hint reads a repository-wide store](spec/2026-08-21-spec-TOOL-aShardedFloor-4.md) | — | 2 | WONTDO | rev-4 | 2026-08-21 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->


<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->