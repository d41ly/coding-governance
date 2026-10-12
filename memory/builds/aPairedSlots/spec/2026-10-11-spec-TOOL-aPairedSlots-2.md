# TOOL-aPairedSlots-2 — the turnstile is a counting semaphore of `slots` beacons, each reaped and released on its own

**Status:** CLOSED · rev-3 · 2026-10-12 · node a · Tier-2 · base b6cd02bc · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPairedSlots-2-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPairedSlots-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 TOOL-aPairedSlots-11 TOOL-aPairedSlots-12 TOOL-aPairedSlots-13 TOOL-aPairedSlots-14 TOOL-aPairedSlots-15 |
| [2026-10-11-prompt-TOOL-aPairedSlots-1.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1.md) | research | TOOL-aPairedSlots-1 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 |
| [2026-10-12-review-TOOL-aPairedSlots-1-9-diff-review-round1.md](../reviews/2026-10-12-review-TOOL-aPairedSlots-1-9-diff-review-round1.md) | diff-review | TOOL-aPairedSlots-1 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 |

<!-- /gen:spec-records -->

## 1. Goal

The host turnstile admits up to `PROF_SLOTS` bars instead of one. Each admitted bar holds its own
beacon directory with its own pid, nonce, heartbeat and holder fields, a waiter reaps a dead or
stalled holder slot by slot, a release frees only the slot it took, and the queue stays one FIFO.
At one slot, every line a bar prints and every file it writes is what TOOL-aFrugalTurnstile-5's
runner prints and writes.

## 2. Scope (IN)

- **S1 — the slot paths.** Slot 1 is `$TS_DIR_C`, the existing `gate-bar-beacon`, so a runner
  older than this unit, and every reader that names that path, still sees the first holder. Slot
  `k` for `k` of 2 or more is `$TS_DIR_C.$k`. The count is `TS_SLOTS`, set from `PROF_SLOTS`
  (TOOL-aPairedSlots-1) before the turnstile block. Observed by AC1, AC6.
- **S2 — the claim.** The acquire predicate keeps its head-of-queue half unchanged: only the run
  whose ticket sorts first may claim. Its second half tries `mkdir` on slots 1 to `TS_SLOTS` in
  order and takes the first that succeeds; that path becomes `TS_DIR`, and the beacon's six files
  are written into it exactly as today. The head then gives up its ticket, so the next ticket is head
  on the next tick and claims any slot still free. Observed by AC1, AC2.
- **S3 — the reap, per slot.** `ts_try_reap` walks slots 1 to `TS_SLOTS`, judging each by its own
  `pid` and its own `ttl`, and reaps every dead or stalled one it finds, printing the existing
  reap line once per slot reaped. The removal is guarded by the nonce read when the slot was judged:
  a slot whose `nonce` changed between the judgement and the removal is left alone. A live slot is
  never touched while a neighbour is reaped. Observed by AC3.
- **S4 — release and ticker stay per slot.** `ts_release` and the ticker already act on `TS_DIR`
  under its nonce; they now act on whichever slot `TS_DIR` names, and on nothing else. Observed by
  AC4.
- **S5 — nesting reads every slot.** The nested test compares an inherited `GATE_TURNSTILE_HOLDER`
  with the nonce of every slot beacon directory present on the host, slot 1 and every `.<k>` beside
  it whatever this runner's own count, and names the matching slot's holder in its line. Reading
  every one present, not 1 to `TS_SLOTS`, is what nests a fixture bar whose own table declares fewer
  slots than the holder that started it. Observed by AC5.
- **S6 — the queue line at two or more slots.** At `TS_SLOTS` 1 the two queue lines are unchanged.
  Above 1 the leading clause names how many slots are held and each holder, in the shape §4's
  Messages table gives; the tail `queued at position N (waited Ns)` is unchanged at every count.
  Observed by AC2, AC6.
- **S7 — the record.** At `TS_SLOTS` above 1 the run record's header gains `slot` (the slot this
  run held, or `-`) and `slots` (the count); at 1 it gains neither. Observed by AC2, AC6.
- **S8 — the suite.** `tools/run-gates/run-gates.turnstile.test.sh` gains arms 29 to 33 for AC1 to
  AC5, its `mk_repo` clears every slot path, and arms 1 to 28 run unchanged at the default count.
  NOT OBSERVED in a pass — the suite runs sliced, arm by arm, as each criterion's direct check.

## 3. Non-goals (OUT)

- The width a bar takes beside another holder (TOOL-aPairedSlots-3).
- Doc-only bars and their own key (TOOL-aPairedSlots-4).
- The two-waiter reap race recorded as TOOL-aReapedTicket-4. S3's nonce guard narrows its window to
  the instant between a read and a removal; it does not close it, and the residual is stated in the
  block's header comment.
- Admitting out of queue order. A head that cannot claim because the slot it can see is held keeps
  the waiters behind it waiting, even where they could claim a slot it cannot, which is the mixed
  count case §4's Rollout states.
- The TTL, `TS_MAXWAIT`, the ticker cadence and the fail-open rule.

### Edges

- **consumes-from** `TOOL-aPairedSlots-1` — `PROF_SLOTS`, the resolved count.
- **hands-off** `TOOL-aPairedSlots-3` — the number of slots held at dispatch, which this unit
  makes countable as the slot paths that exist.
- **hands-off** `TOOL-aPairedSlots-4` — the doc-only key, which sits beside the slots, not in them.
- **hands-off** `TOOL-aPairedSlots-5` — the slot paths and their `repo` files, which the
  one-slot-per-worktree rule reads.
- **consumes-from** external — TOOL-aFrugalTurnstile-5's host turnstile, which this unit widens.

## 4. Design

The turnstile was a mutex built from a `mkdir` claim, a FIFO of named tickets and a beacon whose
pid and heartbeat let a waiter reap a holder that cannot still be holding. A counting semaphore
keeps all three and multiplies only the claim target. Keeping the head-only claim is what keeps the
queue order unchanged: no waiter ever overtakes a ticket that sorts before it, and the head drops its
ticket the instant it claims, so a second free slot is taken one tick later by the next ticket.

Slot 1 keeps its name because three things read it by name: a runner older than this unit, which
claims only it; the turnstile suite's `beacon()` helper; and any operator looking for "who holds
the host". An older runner and a new one therefore interoperate. The older one serializes against
slot 1 only, so the host admits at most the larger of the two counts.

### Messages

| Event | Line at `TS_SLOTS` above 1 |
|---|---|
| queued, slots held | `run-gates: <k> of <n> bar slots on this host are held — <repo> run <run> pid <pid>[; <repo> run <run> pid <pid>…] — queued at position N (waited Ns)` |
| queued, a slot free but a ticket ahead | `run-gates: <k> of <n> bar slots on this host are held, and a ticket sorts ahead of this one — queued at position N (waited Ns)` |
| nested | `gate queue: nested under <run> — <repo> pid <pid>`, unchanged, naming the matched slot's holder |

### Inventory

New shell variables: `TS_SLOTS` (the count) and `TS_SLOT` (the slot this run holds, or empty).
Minted functions, each leading with a declared verb in the `sh.function` cell:
`resolve_free_slot` (the claim: an `mkdir` on each slot path in order, setting `TS_DIR` and
`TS_SLOT` on the first that succeeds) and `measure_held_slots` (the count of slot paths that
exist, into `TS_HELD_N`, read by TOOL-aPairedSlots-3). The slot paths are built once into the
array `TS_SLOT_DIRS`, so neither function forks per slot. New header keys `slot` and `slots`, written above one slot
only.

### Rollout

A host whose repositories declare different counts admits at most the largest count, because each
runner claims among its own slots and all of them share slot 1 and the queue. Every runner older
than this unit claims slot 1 alone. A `slots=2` row therefore takes effect host-wide only once every
repository on the host runs this unit's runner, which the run-gates README states beside the knob.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/run-gates/README.md`

### Alternatives rejected

- **One beacon directory holding a count file.** Incrementing a count needs a lock this platform
  lacks; `flock` does not exist here, and a read-modify-write on a file is the race the `mkdir`
  claim was chosen to avoid.
- **Any waiter may claim any free slot.** It admits out of order, and with two waiters racing two
  slots the later ticket can win, which turns a FIFO into a lottery the queue line then misreports.
- **Slot 1 renamed to `gate-bar-beacon.1`.** It breaks the interoperation above for no gain.

## 5. Production-readiness checklist

- security — N/A — no new input; the slot paths sit in the host turnstile directory the base
  already writes.
- perf / scale — one `mkdir` attempt per slot on the head's tick, and one `pid`/`heartbeat` read per
  slot on a waiter's reap; at two slots that is the cost of one more slot, on ticks of two seconds.
- error / empty / loading states — a slot path that cannot be created is simply not claimed; a
  slot with no readable pid or heartbeat is judged exactly as today's beacon is.
- observability — the queue line names every holder; the header names the slot.
- risks — over-admission through the residual reap race (S3) and through mixed counts (Rollout);
  both are stated, neither exceeds the larger declared count by more than the race already allows.
- testing — arms 29 to 33, each staged RED first on a runner copy with its mechanism removed.
- migration — none; a host with no slot-2 path is a host at one slot.
- user docs — the README's turnstile section names the count, the slot paths and the rollout.

## 6. Acceptance criteria

The fixtures are the turnstile suite's own: scratch repositories built by `mk_repo`, the occupancy
leg, one `GATE_TURNSTILE_DIR` shared by every bar of an arm.

- **AC1** — When three bars start together under `GATE_TURNSTILE_SLOTS=2`, the occupancy peak is 2,
  and the third bar's output carries `queued at position`.
  Red when: the claim tries slot 1 only, so the peak is 1.
- **AC2** — When slots 1 and 2 are held and a third bar queues, its line opens with
  `2 of 2 bar slots on this host are held`, names both holders' pids, and its header records
  `slots` 2; the two holders' headers record different `slot` values.
  Red when: the queue line names one holder, as at one slot.
- **AC3** — When slot 2's beacon names a dead pid while slot 1 is held by a live bar, the next bar
  prints `reaping the beacon of a dead holder` once, claims, and slot 1's `nonce` is unchanged.
  Red when: the reap walks slot 1 only, so the bar queues behind a dead slot.
- **AC4** — When a run holding slot 2 releases, slot 1's directory, held by another run, still
  exists with its nonce; and a run whose own slot was reaped and re-claimed does not remove the
  successor's directory on release.
  Red when: `ts_release` removes by path without the nonce guard.
- **AC5** — When a leg of the bar holding slot 2 starts a runner with `GATE_TURNSTILE_HOLDER`
  inherited, that runner prints `gate queue: nested under`.
  Red when: the nested test compares slot 1's nonce only, and the inner runner queues.
- **AC6** — When a fixture bar runs at the default count, its stdout from the profile line to the
  `gate queue: acquired` line, its queue lines under contention and its header's key set equal the
  base runner's on the same fixture, and arms 1 to 28 of the turnstile suite pass.
  Red when: a slot-count field is written unconditionally.
  cost: the suite's arms 1 to 28 take minutes; they run sliced.

## 7. Gates

`run-gates turnstile` · `run-gates canary` · `run-gates gov canary`

New arm: tools/run-gates/run-gates.turnstile.test.sh · covers AC1 AC2 AC3 AC4 AC5 · a runner copy whose claim tries slot 1 only, whose reap walks slot 1 only, and whose nested test reads slot 1 only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S5 · §4 · nesting reads every slot beacon present rather than 1 to the count;
  the claim helper is `resolve_free_slot` over a once-built `TS_SLOT_DIRS`, replacing a per-slot
  path function that would fork on every call.
- rev-3 · 2026-10-12 · §3 · the hands-off edge to TOOL-aPairedSlots-5 that its consumes-from
  edge names, which the close's memory hygiene found missing.

## 10. Reuse audit

The seam is TOOL-aFrugalTurnstile-5's turnstile block in `tools/run-gates/run-gates.sh`:
`ts_try_reap`, `ts_release`, `ts_tick_start`, the `mkdir` claim and the ticket queue, which this
unit widens and does not replace. `reuse_lookup.py` named no counting-semaphore seam. Recall
returned TOOL-aReapedTicket-4, the reap race S3 narrows, and TOOL-aQuenchedHarness-8, the ticker
design S4 keeps.

Recall terms used: `python tools/memory-recall/query.py "why does the gate turnstile serialize bars and admit only one at a time" --terms "turnstile beacon queue ticket serialize concurrent bars width contended CPU host-wide nonce heartbeat reap slots"`
