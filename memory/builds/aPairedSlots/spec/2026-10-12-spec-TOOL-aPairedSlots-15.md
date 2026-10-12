# TOOL-aPairedSlots-15 — the closing review's mediums and lows, batched

**Status:** CLOSED · rev-2 · 2026-10-12 · node a · Tier-2 · base d3354597 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-TOOL-aPairedSlots-15-1-acceptance-ledger.md](../build/2026-10-12-build-TOOL-aPairedSlots-15-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9 TOOL-aPairedSlots-11 TOOL-aPairedSlots-12 TOOL-aPairedSlots-13 TOOL-aPairedSlots-14 |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's round 1 confirmed fifteen MEDIUM and eleven LOW findings, reported as items M1
to M9 and L1 to L8 of `2026-10-12-review-TOOL-aPairedSlots-1-9-diff-review-round1.md`. The build
method promotes them as one unit. Three items are a HIGH's duplicate and close with it: M6 with
TOOL-aPairedSlots-11, M7 with TOOL-aPairedSlots-14 and L8 with TOOL-aPairedSlots-12. M8's drift
self-test name is rewritten by TOOL-aPairedSlots-11's arm. Every other item closes here.

## 2. Scope (IN)

- **S1 — a reap judges the holder whose nonce guards the removal (M1).** `ts_try_reap` and
  `scan_dead_docs_beacons` read a beacon's nonce before its pid, heartbeat and ttl, and re-read it
  before the removal, so a successor that claimed the slot after the judgement survives it. The
  header comment states the window that is left. Observed by AC1.
- **S2 — the worktree rule reads every beacon present, at every count (M2, M3, L5).**
  `check_worktree_unheld` scans slot 1 and every `.<k>` beside it, whatever this runner's own count,
  and every docs beacon, and refuses on any whose `repo` is this run's top level. A doc-only bar whose
  worktree has a live holder waits for it, bounded as the queue is; it never waits for another
  worktree's bar. The queue line of a bar held back this way names that holder, from `TS_SAME`, at
  every count. Observed by AC2, AC3.
- **S3 — the slot count has a ceiling (M9, L1).** A row's `slots` above 64 is refused beside the
  refusal of 0, and an override above 64 is ignored with the existing NOTE. Observed by AC4.
- **S4 — a docs beacon interrupted before it was complete is swept (L2).** A docs beacon with neither
  a pid nor a numeric heartbeat, whose directory is older than the waiter's ttl, is swept under the
  same nonce guard. Observed by AC5.
- **S5 — the turnstile suite pins the slot count and arms what it was missing (M5, L4, M8).** The
  suite exports `GATE_TURNSTILE_SLOTS=1` beside its private turnstile directory. Arm 32's inner runner
  runs at one slot, so it builds the case the nesting glob exists for. The arms that read a table
  default select a fixture table with no `slots` key. A new arm plants a stalled docs holder. Its two
  helpers outside the declared verbs are renamed. Observed by AC6.
- **S6 — both floors count this build's arms (M4, L3).** The turnstile and canary suites' assertion
  floors rise by the assertions this build added to each, with a dated comment line. Observed by AC7.
- **S7 — the README states the worktree rule, and the records point where the code is (L6, L7).** The
  run-gates README's turnstile section states one slot per worktree, the doc-only bar's wait, and the
  queue line. The shared-path audit's health log row, the build README's roster row for unit 7 and
  spec 7's checklist point at ask TOOL-aPairedSlots-10 for the trim. Observed by AC8.
- **S8 — each new class reaches the checklist.** Every finding whose class no gate and no checklist
  entry covers gains a `memory/gotchas/` entry. Observed by AC8.

## 3. Non-goals (OUT)

- A doc-only bar that runs beside its own worktree's bar with its per-worktree files moved aside. The
  review's alternative to a wait; it touches every per-worktree path the runner writes.
- A slack-floor gate that reds when a suite counts more assertions than its floor (M4's left-shift).
  It moves every suite's contract, which is its own unit.
- A reader of `TS_SAME` beyond the queue line.

### Edges

none

## 4. Design

### The nonce comes first (S1)

A reap is safe when the facts it judges belong to the holder its removal is guarded by. Reading the
nonce last let a successor that claimed the slot between the pid read and the nonce read lend its
nonce to the dead holder's judgement, and the re-read then matched. Reading it first ties the
judgement to one holder. What is left is the instant between the re-read and the `rm`, which only a
lock closes.

### Every beacon, at every count (S2)

The worktree rule asked only the slots this runner counts, so a bar run at a lower count than a
neighbour in its own worktree saw nothing, and the docs key was never asked at all. The nesting test
already reads every beacon present for the same reason (TOOL-aPairedSlots-2 S5). At one slot, with no
neighbour at a higher count and no docs bar, the rule finds slot 1 alone, which is the claim's own
test, so a bar at the kit default prints and waits exactly as before.

The doc-only bar's wait answers a fork the review left to the owner, resolved under the run's
delegated mandate: see §8. The wait is a loop on `check_worktree_unheld`, reaping dead slot holders
and dead docs beacons on each tick, bounded by the queue's own bound and failing open as the queue
does.

### Inventory

No function is minted. `ts_try_reap`, `scan_dead_docs_beacons`, `check_worktree_unheld`, the profile
validator, the override parse, the docs branch and the queue line change. Spec 5's §4 inventory
omitted `check_worktree_unheld` and `TS_SAME`; both exist since TOOL-aPairedSlots-5.

### Messages

| When | Line |
|---|---|
| a bar is held back by its own worktree's holder, at one slot | `run-gates: no bar holds this host's first slot, but this worktree's bar holds <key> — <repo> run <run> pid <pid> — queued at position <n> (waited <s>s)` |
| the same, above one slot | `run-gates: <k> of <n> bar slots on this host are held, and this worktree's bar holds <key> — <repo> run <run> pid <pid> — queued at position <n> (waited <s>s)` |
| a doc-only bar waits for its worktree's holder | `gate queue: docs-only — this worktree's bar holds <key> — <repo> run <run> pid <pid> — waiting for it` |
| an unfinished docs beacon is swept | `run-gates: sweeping the docs beacon of an unfinished holder (no pid or heartbeat, <s>s old)` |

`<key>` is `slot <k>` or `the docs key`.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/README.md`
- `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md`
- `memory/builds/aPairedSlots/README.md`
- `memory/builds/aPairedSlots/spec/2026-10-11-spec-TOOL-aPairedSlots-7.md`

### Alternatives rejected

- **A wait on every doc-only bar while any slot is held.** It is the queue the docs key exists to skip.
- **A scan bounded by this runner's count.** It is M2's defect.

## 5. Production-readiness checklist

- security — N/A — the cooperative local lock's own model, unchanged.
- perf / scale — a builtin glob per claim tick; one `date -r` fork per unfinished docs beacon only.
- error / empty / loading states — the doc-only wait fails open at the queue's bound, as the queue does.
- observability — every new wait names its holder.
- risks — a doc-only bar now waits behind its own worktree's bar, which it did before
  TOOL-aPairedSlots-4 and not since; §8 records why.
- testing — arms per item, each staged red.
- migration — none.
- user docs — the run-gates README's turnstile section.

## 6. Acceptance criteria

- **AC1** — When the turnstile suite's reap-guard arm swaps a slot's nonce while `ts_try_reap` reads
  its pid, and does the same to a docs beacon under `scan_dead_docs_beacons`, both survive.
  Red when: the nonce is read after the pid, or the re-read is removed, and the beacon is deleted.
- **AC2** — When a bar at one slot reaches the head while its worktree holds slot 2 under a two-slot
  neighbour, it waits and its queue line reads `this worktree's bar holds slot 2` with that holder's pid.
  Red when: the rule reads only this runner's own count, and the bar claims slot 1.
- **AC3** — When a doc-only bar starts in a worktree whose slot is held, it waits until that holder
  releases and prints `gate queue: docs-only — this worktree's bar holds`; a non-doc bar in a worktree
  with a live docs beacon waits too, its queue line reading `this worktree's bar holds the docs key`.
  Red when: either bar runs while its worktree's holder runs.
- **AC4** — When a row declares `slots=65`, the runner refuses the table, and `GATE_TURNSTILE_SLOTS=65`
  prints the NOTE and keeps the row's count.
  Red when: either value is accepted.
- **AC5** — When a docs beacon with no pid and no heartbeat, older than the ttl, is planted, the next
  doc-only bar prints `sweeping the docs beacon of an unfinished holder` and the beacon is gone.
  Red when: the beacon survives.
- **AC6** — When arm 32 runs, its inner runner prints `gate queue: nested under` at one slot under a
  two-slot holder, and the stalled docs holder arm sees `sweeping the docs beacon of a stalled holder`
  and the beacon gone.
  Red when: arm 32 is green against a runner whose nesting reads only its own slot paths.
- **AC7** — When the turnstile suite runs whole, its assertion count equals its raised
  `FLOOR_ASSERTIONS`, and the canary's raised floor equals its old floor plus the checks of section 11s
  counted off the arm.
  Red when: an arm this build added is removed and the suite stays green.
- **AC8** — When the records are read, the audit's health log row names ask TOOL-aPairedSlots-10, the
  roster row for unit 7 names no health log trim, and each new class has a `memory/gotchas/` entry.
  Red when: a record still names the scope item spec 7 removed.

## 7. Gates

`run-gates turnstile` · `run-gates canary` · `memory hygiene` · `gotchas selftest` · `recall floor` · `recall floor arms`

## 8. Open questions

- **F1 — Does a doc-only bar wait for its own worktree's holder?** The review found it
  runs beside that holder and shares its git dir, which TOOL-aPairedSlots-5 promised no two bars do.
  Options: wait for the same worktree only; or run beside it with its per-worktree files moved aside.
  The owner's ruling was that a doc-only bar never queues behind a non-doc bar, made about the host
  queue. Recommendation: wait for the same worktree only. RESOLVED (agent, 2026-10-12, delegated): a
  doc-only bar waits for a holder in its own worktree and never for another worktree's; the host
  queue is still never joined. Reversible by deleting the wait, and surfaced in the wrap-up for the
  owner.

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft, promoted from the closing review's round 1.
- rev-2 · 2026-10-12 · Messages · AC7 · the above-one-slot line names the key its worktree's holder
  holds, as the one-slot line does, since that holder may be a docs bar; the canary's floor is counted
  off its arm, because the canary runs whole only at the close's bar.

## 10. Reuse audit

Every change extends the turnstile's existing functions; the nesting test's every-beacon glob is the
seam S2 reuses. `reuse_lookup.py "reap a dead lock holder guarded by a nonce"` ranked the runner's own
leg reaps and the unattended kit's push lock, neither of which judges a beacon; no other seam fits. The functional reap arm sources the runner's functions the way the canary's
TOOL-aReapedSpinner-7 arm does. Recall named TOOL-aReapedTicket-4, the reap race this guard narrows,
and TOOL-aPairedSlots-2, -4 and -5.

Recall terms used: `python tools/memory-recall/query.py "how does the turnstile reap a dead holder's beacon safely" --terms "turnstile beacon reap nonce guard dead holder stalled heartbeat slot docs key worktree"`
