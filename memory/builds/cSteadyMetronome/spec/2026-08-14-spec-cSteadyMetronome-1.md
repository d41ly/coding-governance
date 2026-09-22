# TOOL-cSteadyMetronome-1 — concurrency proved by rendezvous, not by elapsed time

**Status:** CLOSED · rev-4 · 2026-08-14 · node c · Tier-2 · base 790c1d24 · streams tooling · ratified 2026-08-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-14-review-TOOL-cSteadyMetronome-1-1.md](../reviews/2026-08-14-review-TOOL-cSteadyMetronome-1-1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

Make the run-gates canary's concurrency arm assert how many legs the runner had IN FLIGHT AT ONCE, by
a measurement that does not depend on the scheduler's punctuality, so a correct tree stops being
blocked by a busy node.

## 2. Scope (IN)

- **S1** — **Each leg is keyed by its LEG NAME, passed as an argv element.** Three of the four
  scratch legs run the byte-identical `fx/mid.sh` and the runner exposes no leg identity to the
  child, so a fixture cannot key on its own script. The scratch manifest gains a third argv element
  per leg and the fixture writes under that name, defaulting to its own basename when absent.
  `fx/mid.sh` stays ONE shared file, because arm 3d copies `bad.sh` over it to produce its red run.
- **S2** — **Each fixture RENDEZVOUS with its peers instead of being timed.** It announces itself,
  then polls for up to a bounded wait, recording the PEAK number of announced legs it ever saw at
  once, and only then sleeps its own duration. The scheduler's skew is absorbed by the wait rather
  than being the quantity under test.
- **S3** — **The arm asserts the PEAK equals the width.** At width 4 the peak across legs is exactly
  4; at width 1 it is exactly 1. Equality, not "at least one pair", because a pool clamped to width 2
  satisfies any at-least-one form while being exactly the regression this arm exists to catch.
- **S4** — **The width-1 run is the negative control and its observations are CAPTURED BEFORE the
  scratch directory is reused.** Both runs' peaks are read into variables at the moment each run
  ends; the arm compares them afterwards.
- **S5** — **A population guard.** The arm asserts it found exactly four peak records before
  comparing anything. A missing record is a refusal, never a smaller comparison that still passes.
- **S6** — **The elapsed-time ratio is REMOVED**, with its two wall-clock fences and both `ms`
  variables. Not kept alongside: two answers to one question is a class this repo records, and the
  weaker answer is the one that reds.
- **S7** — **The arm states what it does and does not claim**, in place: it asserts DISPATCH
  concurrency and makes no claim about execution speed, which is a property of the node. It also
  states the bound it still has — the rendezvous wait — and names lengthening that wait as the knob.
- **S8** — **The failure message prints what was measured**: the per-leg peaks and the wait, so a
  future red says whether the pool or the node produced it.

## 3. Non-goals (OUT)

- **Arms 3a, 3b and 3d.** Report equality across widths, manifest-order reporting, and the failing
  leg's exit code and durable row are untouched. `mid.sh` staying one shared file is what keeps 3d
  working, and S1 is written around that.
- **The runner itself.** `tools/run-gates.sh` does not change.
- **Changing `GATE_JOBS`, the pool width, or making the bar faster.**
- **Coordinating with other sessions on the node.** The fix is to stop depending on load, not to
  remove it.
- **Any other timing assertion in the tree.** Scoped to this arm.

## 4. Design

### The defect, stated precisely

The arm's subject and its measurement disagree. `run-gates.sh` is responsible for DISPATCHING legs
concurrently; whether the operating system then runs them simultaneously depends on free capacity,
which the runner neither owns nor influences. `par_ms * 2 < ser_ms` is only satisfiable when the
machine had capacity, so a correct runner on a busy node reds a correct tree and the operator's exits
are to wait or to bypass.

The arm already moved once for this reason and stopped short. Its comment records retiring an
absolute `par_ms < 5000` deadline because it "graded this leg against load it does not control", and
adopting a ratio on the premise that *uniform load and cold start cancel in a ratio*. That premise
fails in the direction that matters: the serial run has no overlap to lose, so contention costs it
only per-leg slowdown, while the concurrent run's entire advantage IS overlap. The ratio therefore
degrades under load rather than cancelling.

### Why a rendezvous and not interval intersection

Rev-1 proposed recording each leg's start and end and asserting the intervals intersect. The audit
refuted the immunity claim and the refutation holds: intersection is immune to per-leg SLOWDOWN but
depends entirely on the SKEW between start instants, which is almost pure process-spawn cost — the
most contention-sensitive component here. Measured at width 4 on this node, first-to-last start
spread was 504-935ms against `slow.sh`'s 2000ms sleep: 2.1x-3.3x headroom, visibly moving. The same
arm's own comment records the width-4 run dilating from 2.7-3.6s idle to 4.1-9.8s contended, and this
build's README records contended runs of 17146ms and 32649ms against the same 2s floor. Skew times
that dilation crosses the budget, and the arm would red a correct runner in a new way.

A rendezvous removes the dependency instead of bounding it. Each fixture ANNOUNCES itself and then
WAITS for peers, so arbitrary dispatch skew is absorbed by the wait rather than deciding the verdict.
What remains is a bound that is honest and tunable: the arm is sound while the whole batch is
dispatched within the rendezvous wait, and lengthening that wait costs only the width-1 run.

### Data model

One directory, `fx/ts/`, cleared before each scratch run. Per leg, keyed by LEG NAME:

| File | Written | Content |
|---|---|---|
| `fx/ts/<leg>.up` | first act of the fixture | empty; its presence is the announcement |
| `fx/ts/<leg>.peak` | after the rendezvous wait | the largest number of `*.up` files seen at once |

`.peak` is written BEFORE the fixture sleeps and before any exit, so the record survives a fixture
that exits non-zero without reaching a last line — `bad.sh` exits 3 and would never write an "end"
marker, which is why rev-1's end-of-fixture write was unimplementable.

### The rendezvous

```
announce                      -> fx/ts/<leg>.up
poll every 100ms, up to WAIT  -> peak = max(peak, count of fx/ts/*.up)
                                 stop early once peak reaches 4
write peak                    -> fx/ts/<leg>.peak
sleep <this leg's duration>   -> unchanged, so arm 3b still sees leg 1 finish last
```

At width 4 all four announce within the skew and every leg records 4, so the poll exits early and
costs nothing. At width 1 a leg can only ever see itself, records 1, and pays the full wait — four
times, which is the negative control's whole price and is why `WAIT` is a knob rather than a
constant tuned for speed.

### The assertion

| Run | Expected peak | What a violation means |
|---|---|---|
| width 4 | exactly 4 | the pool dispatched fewer than four at once |
| width 1 | exactly 1 | the serial path overlapped, so the control proves nothing |

Equality on both sides is what makes it strictly stronger than the retired ratio: a pool clamped to
width 2 passes any "at least one pair overlapped" form and fails this one.

### Inventory

| Change | Site |
|---|---|
| leg name passed as a third argv element | the scratch `gate-legs.json` heredoc |
| fixtures announce, poll, record peak, then sleep | the `slow.sh` / `mid.sh` writers |
| `fx/ts/` cleared before each run | `run_scratch` |
| peaks captured per run into variables | around each `run_scratch` call |
| population guard: exactly four peak records | arm 3c |
| width-4 peak equals 4 · width-1 peak equals 1 | arm 3c |
| the elapsed-time ratio, its two fences and both `ms` variables | removed |
| failure message prints the per-leg peaks and the wait | arm 3c |

### Files touched (estimate)

`tools/run-gates.test.sh` · `memory/backlog/TOOL.md` · `memory/DECISIONS.md`

### Alternatives rejected

**Interval intersection on recorded start/end instants.** Rev-1's design; refuted above on measured
skew, and separately unimplementable as specced because three legs share one script and `bad.sh`
never reaches a final line.

**Retry the arm N times, pass if any attempt succeeds.** Makes a flaky gate slower rather than sound,
still fails under sustained load, and keeps a wall-clock proxy for a property that can be measured
directly.

**Widen the ratio or scale it by observed load.** Re-decides the threshold per node, which is the
`pin-copied-from-another-corpus` class, and every load figure the arm could read is distorted by the
same contention.

**Skip the arm when the node looks busy.** A gate that switches itself off under the condition that
breaks it asserts nothing when it matters.

**Split `mid.sh` into three scripts to get per-leg identity.** Breaks arm 3d, whose `cp bad.sh
mid.sh` is what produces its red run; §3 keeps 3d untouched, so identity comes from argv instead.

## 5. Production-readiness checklist

- security — N/A — confined to a self-test's scratch fixtures; no new surface.
- perf / scale — the width-4 run gets cheaper (the poll exits early and both wall-clock fences go);
  the width-1 run gets DEARER by up to four rendezvous waits. That is the cost of the negative
  control and it is stated rather than hidden — rev-1 claimed "strictly cheaper", which was wrong.
- a11y — N/A — a shell self-test with no user interface.
- i18n — N/A — this repo's tooling is English-only by charter.
- error / empty / loading states — S5 makes a missing record a refusal; a fixture that exits non-zero
  still has its peak on disk because it is written before the sleep.
- observability — S8 prints the per-leg peaks and the wait on failure.
- risks — **dispatch skew exceeding the rendezvous wait** is the one bound that remains; the knob is
  `WAIT`, named in S7 and in the arm's comment. Secondary: a node whose `ls`/glob cost makes the
  100ms poll coarse, which lengthens rather than breaks the measurement.
- testing + left-shift gates — the width-1 equality is the left-shift: the same fixtures answer
  differently at the two widths, which the elapsed-time form never established.
- migration / rollback — none; rollback is a revert, after which the flake returns.
- user docs — none; no shipped document describes this arm.

## 6. Acceptance criteria

- **AC1** — When the scratch bar runs at width 4, every leg records a peak of 4 and the arm is
  silent.
- **AC2** — When the scratch bar runs at width 1, every leg records a peak of 1 and the arm is
  silent; this control is what gives AC1 its meaning.
- **AC3** — When the pool is clamped to width 2 while the arm expects 4, the arm reds naming the
  peaks it found — the partial-clamp regression that "at least one pair overlapped" cannot see.
- **AC4** — When a peak record is missing, the arm reds naming the count rather than comparing a
  smaller set.
- **AC5** — A grep of `tools/run-gates.test.sh` finds no `ser_ms`, no `par_ms`, and no
  elapsed-time comparison.
- **AC6** — The canary leg passes on this node WHILE a second full bar runs concurrently — the exact
  condition under which the retired assertion red three consecutive pushes.
- **AC7** — Arm 3b still observes manifest-order reporting and arm 3d still observes its red run,
  proving the fixture rework left them intact.
- **AC8** — `bash tools/run-gates.sh` is green.

## 7. Gates

`tools/run-gates.test.sh` is itself the gate leg this unit changes, and it is its own acceptance
harness. The full bar. The harness meta-gate `check-arms.py` is NOT in scope: it discovers tracked
`*.sh` files that define `fail() {` and call `fail <n> "`, and this file uses a plain `fail=1`
variable with `echo`, so it is outside that population — rev-1 named it in error. No new gate leg, so
the codebase-map inventories do not move.

## 8. Open questions

none — the one fork is RESOLVED below.

**F1 — replace the ratio or wrap it in a retry? RESOLVED (owner, 2026-08-14): replace.** The
recommendation put to the owner was to replace the wall-clock proxy because a retry makes a flaky
gate slower rather than sound; the instruction "spec the canary fix and build it" followed that
recommendation directly. Recorded with its provenance rather than as a bare signature, because the
owner answered the direction and not a menu.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, written after nine measurements and after the cause was found
  by reading the process table rather than inferred from the failures.
- rev-2 · 2026-08-14 · folded the M4 spec audit, `wf_b07869ce-99d`: 19 raw, 15 confirmed, 4 refuted,
  precision 0.79, verdict BLOCKED, 11 distinct. Both blockers were fatal to rev-1's mechanism and
  both were reproduced against the real runner rather than argued. R1: three legs run one script and
  the runner exposes no identity, so per-script timestamp files collide — and the survivor is the
  LAST leg to start, which HIDES a real overlap and reintroduces the false red. R2: intersection is
  immune to slowdown but not to dispatch SKEW, measured 504-935ms against a 2000ms sleep on a node
  whose non-sleep overhead dilates 10-20x. The mechanism is therefore replaced, not patched: a
  rendezvous makes skew irrelevant instead of bounding it. R4 forced equality rather than
  "at least one pair", R5 the per-run capture, R9 the write-before-sleep placement, R7 the corrected
  gate list, R11 the corrected perf claim.
- rev-3 · 2026-08-14 · BUILT. Every acceptance criterion verified by observation, two by injection.
  AC3: clamping the pool to width 2 reds with "width-4 peaked at 2 legs in flight, not 4" — the
  partial-clamp regression the retired ratio could not see, because a width-2 pool still beats half
  the serial time. AC6: the leg ran 9.5 minutes under a concurrently-running second bar and exited
  SILENT, which is the exact condition that red the retired form three times. The width-1 control
  earned itself on its first run by catching a real defect in this unit's own design: peaks read
  4 3 2 1 because a leg's announcement was never withdrawn, so later legs counted the dead. The
  fixture now drops its announcement on a trap, which also covers the fixture that exits 3. Status
  moves SPECCED to INPROGRESS: built and reviewed, not landed.
- rev-4 · 2026-08-14 · CLOSED. Landed at `d937411` with the bar green 54/54, the canary among them.
  It did not land by this session's push: a second session working the same repo won the race and
  carried these commits with it, while this session's own gate was KILLED at the caller's timeout and
  the pre-push hook correctly read a killed gate as red. Worth recording as a property rather than an
  anecdote -- a gate that cannot finish inside the caller's patience is indistinguishable from a red
  one, and on a contended node that is reachable.

## 10. Reuse audit

The seam is the canary's own scratch harness — the fixture writers, the scratch `gate-legs.json`,
`run_scratch` and the arm block — which already builds fixtures, already runs the bar at two widths,
and already owns the fences this unit removes. No new harness, and no other file gains a dependency.

Checked against source at this spec's base: `run-gates.sh` splits a leg's argv and execs it verbatim
with no per-leg variable, which is why identity has to arrive as an argv element; and its timing
cache records durations for scheduling, not start instants, so it cannot answer whether two legs were
in flight together.

This unit CLOSES the open row `TOOL-cFinalBerth-5`, which recorded the flake with its measurements
and is the record this spec is the answer to. Its wording — that the margin is overhead-dependent —
is the diagnosis carried forward here; the narrower "load-sensitive" reading was retired at commit
`9d371c0` after the leg flipped red-then-green on an unchanged tree.

Recall terms: canary, run-gates, concurrency, pool, overlap, width, ratio, wall-clock, timing, flake,
gate, leg, rendezvous. The probe returned this build's own predecessor rows and no earlier ruling on
timing assertions, so nothing is re-opened.
