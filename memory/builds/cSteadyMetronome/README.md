---
slug: cSteadyMetronome
node: c
opened: 2026-08-14
streams: tooling
roster: TOOL
ids: TOOL-cSteadyMetronome-1
---

# cSteadyMetronome — the canary measures the runner, not the machine

Node `c` · opened 2026-08-14 · streams tooling.

The run-gates canary's arm 3c times two runs of a scratch bar and asserts the concurrent one beat
half the serial one. It blocked three consecutive pushes of a records-only commit on this node, and
it has never once been red for a reason inside the tree it gates.

This README is the master overview and the owner decision menu, per `memory/TEMPLATE-SPEC.md`.

## Start here

**What the arm is trying to prove is right; what it measures is not.** It wants to know that the
runner DISPATCHES legs concurrently. It measures whether the operating system EXECUTED them
concurrently, which is a fact about the machine. On a node with nothing free to run them on, the pool
dispatches perfectly and the legs still do not overlap — so a correct runner reds a correct tree.

**Measured, on `790c1d2` and its ancestors, nine runs.** Fixtures are `sleep 2` plus three ×
`sleep 1.5`: serial 6.5s of sleep, concurrent 2s, and the assertion is `par*2 < ser`.

| Condition | width-4 | width-1 | ratio | verdict |
|---|---|---|---|---|
| quiet node | — | — | — | pass, four times |
| contended | 17146 | 28813 | 0.60 | red |
| contended | 32649 | 55622 | 0.59 | red |
| in-bar | 7705 | 14753 | 0.52 | red |
| in-bar, later | 9960 | 18407 | 0.54 | red |
| in-bar, later still | 18798 | 30726 | 0.61 | red |

Red then GREEN on a byte-identical tree with no edit between, so it is not a property of the diff.
The width-4 figure tripled across the session against a fixed 2s sleep floor, which is the shape of
a machine losing capacity rather than a gate finding something.

**The cause was identified by looking, not by inference.** The process table showed a SECOND active
session in a sibling worktree running its own full bar, its own self-tests and a workflow poller. Two
53-leg bars on one node cannot both demonstrate a pool overlapping. Nothing was killed: those were
another session's live processes, and an earlier reading of them as this session's orphans was wrong.

**The arm already moved once for this exact reason and did not move far enough.** Its own comment
records retiring an absolute `par_ms < 5000` deadline because it "graded this leg against load it does
not control", and replacing it with a ratio on the stated premise that *uniform load and cold start
cancel in a ratio*. That premise is false in the direction that matters: contention removes the
concurrent run's advantage while leaving the serial run — which never overlapped — untouched. The
ratio therefore degrades under load rather than cancelling.

## The unit

| Unit | Subject | Obligation |
|---|---|---|
| **Unit 1** | `TOOL-cSteadyMetronome-1` — overlap asserted as intersection | the canary proves two legs were IN FLIGHT AT ONCE, by a measurement no amount of machine load can change, and still reds a pool degraded to serial |

## Owner decision menu

**F1 — replace the ratio, or add a retry around it? · RESOLVED (owner, 2026-08-14): replace.** A
retry makes a flaky gate slower rather than sound and keeps a wall-clock proxy on the bar. The owner
answered the direction — "spec the canary fix and build it" — immediately after that recommendation.

## Review record

`reviews/2026-08-14-review-TOOL-cSteadyMetronome-1-1.md` — M4 spec audit, 3 lenses, 19 raw, 15 confirmed,
4 refuted, precision 0.79, no dead lens; 11 distinct — 2 blockers. Verdict **BLOCKED**, and rev-2 is
the fold. Both blockers were fatal to rev-1's mechanism and both were reproduced against the real
runner rather than argued: three legs run one script so per-script timestamps collide (and the
survivor HIDES an overlap), and interval intersection is immune to slowdown but not to dispatch skew,
measured 504-935ms against a 2000ms sleep. The mechanism was replaced rather than patched.

## What this build hit and did not fix

`memory/backlog/TOOL.md` sits at 20276 of its 20480-byte cap — 99% full, and it was at 99.7% before
this build touched it. The documented remedy is rotation to `archive/`, and rotation was ATTEMPTED
here and reverted: backlog rows DEFINE ids, `archive/` is not scanned for definitions, and moving 34
terminal rows orphaned every id they defined against hygiene check 14. So the remedy the gate names
does not work for this index, and the next row to land will breach the cap. It needs its own unit and
has no backlog row, because there is no room to write one.

The table below is GENERATED from the status header of
every spec in this folder — do not hand-edit it.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-cSteadyMetronome-1` | 2 | concurrency proved by rendezvous, not by elapsed time |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node c · opened 2026-08-14 · streams tooling
ids TOOL-cSteadyMetronome-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-cSteadyMetronome-1 — concurrency proved by rendezvous, not by elapsed time](spec/2026-08-14-spec-cSteadyMetronome-1.md) | — | 2 | CLOSED | rev-4 | 2026-08-14 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->