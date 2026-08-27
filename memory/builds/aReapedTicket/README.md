---
slug: aReapedTicket
node: a
opened: 2026-08-27
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aReapedTicket-1 TOOL-aReapedTicket-2 TOOL-aReapedTicket-3 TOOL-aReapedTicket-4
---

# aReapedTicket — the turnstile's queue gets the liveness its beacon already has

Node `a` · opened 2026-08-27 · streams tooling · base pinned at preflight.

Started from an owner prompt, recorded with every observation it leans on at
[the prompt record](prompts/2026-08-27-prompt-TOOL-aReapedTicket-1.md). **Read that first.** Both
halves of the bug were reproduced in scratch repositories before any unit was written, and no figure
in this file is authored twice.

## The goal

**A participant of the turnstile that has stopped existing must stop blocking the ones that still
do — on the QUEUE exactly as on the BEACON, and by the same two signals.**

That sentence is the build's immutable description. The turnstile asserts liveness on one of its two
participants. The holder has a dead-pid signal and a stale-heartbeat signal; a queue ticket has
neither, and the acquire predicate is a pure sort order over a directory nothing prunes. So the unit
that exists to stop two bars running at once is disabled, permanently, by any one bar that dies while
queued.

## What the grounding pass changed about the diagnosis

The prompt's mechanism is exactly right. Two things it does not reach, both observed:

**The root cause is one line earlier than "nothing reaps a dead waiter".** A queued waiter has no
signal handler at all — the only `ts_drop_ticket` trap is armed inside the branch that WINS the
beacon, at `run-gates.sh:502`. So the leak does not need the `SIGKILL` the prompt assumes. It needs
Ctrl-C, which is how a bar ordinarily dies, and that is why three of them accumulated.

**The standing damage outlives the incident.** A wedged bar expires after `TS_MAXWAIT` and drops only
its own ticket, so the immortal one stays. In production `TS_MAXWAIT` is 7200 s. Every future bar
pays two hours and then runs UNQUEUED — the turnstile is not slowed, it is defeated, and the
concurrent-bar condition it was built to prevent becomes the permanent state.

## Why the obvious answers are the wrong ones

**Not "shorten the bounded wait."** The wait is already a derived multiple of the one number this
unit derives, and shortening it makes every bar give up on a legitimately busy peer sooner. It treats
the symptom — the two hours — and leaves a queue that never drains.

**Not "clear the queue directory at startup."** A bar that prunes tickets it cannot prove are dead
deletes live waiters' places, and a waiter whose ticket is gone can never satisfy the acquire
predicate again. That converts a wedge affecting future bars into a wedge affecting the bar in front
of you, which is worse.

**Not "give tickets a heartbeat file."** The beacon needs one because a holder can be alive and
wedged, and only a clock distinguishes that. A waiter cannot be wedged — it does nothing but poll —
so the second signal it needs is not progress but AGE, and the ticket name already carries a UTC
timestamp. A heartbeat here would be a new file, a new refresh site and a new staleness constant to
buy a distinction that does not exist.

## The shape of the answer

Delete the leak where it happens, then reap what could not be deleted, then say so.

The waiter arms the handler it always should have had, which closes every catchable signal — the
common case, and the one that produced this incident. A queue sweep backstops the uncatchable ones
with the SAME two-signal shape the beacon reaper already has, reusing `ts_alive` and deriving its
staleness bound from `TS_MAXWAIT` rather than introducing a constant. And the acquire loop stops
waiting on conditions that cannot change, which is the charter's own "a probe that cannot move says
so" applied to the one loop in this repository that was observed spinning against nothing.

## Units

| id | delivers | tier | deps |
|---|---|---|---|
| TOOL-aReapedTicket-1 | a queued waiter drops its own ticket on every signal a trap can catch | 2 | — |
| TOOL-aReapedTicket-2 | the acquire loop asserts liveness on the QUEUE, and refuses to wait on what cannot change | 2 | 1 |
| TOOL-aReapedTicket-3 | arms for a dead waiter, which the suite has never had | 2 | 2 |

**TOOL-aReapedTicket-1 is the root-cause unit.** It is the smallest of the three and it removes the
leak rather than cleaning up after it. `run-gates.sh:491-501` already argues, at length and from a
measurement, why the beacon's release trap must be armed at the instant of the claim; the ticket is
created 24 lines earlier and got no such treatment. This is that same argument applied to the
participant it was not applied to.

**TOOL-aReapedTicket-2 is the backstop and the honesty.** A trap cannot catch `SIGKILL`, an OOM kill
or a power loss, so the queue still needs a reaper — two signals, mirroring `ts_try_reap`: a dead pid
(the ticket name already carries it) and an age past `TS_MAXWAIT` (past which no live waiter can
still hold a ticket, because a live one fails open and drops it at that bound). It also closes the
two observations that make the wedge undiagnosable: `ts_try_reap` returning immediately when there is
no beacon to look at, and the waiter reporting that another bar holds a repository nothing holds.

**TOOL-aReapedTicket-3 is why this does not come back.** The suite has 15 arms and every liveness arm
among them is about the holder. The arms this unit adds are the two reproductions from the prompt
record, plus the one that stops a sweep-everything reaper passing them: a LIVE waiter's ticket must
survive.

## BUILD-LEVEL RULES

**Scoped OUT, with its reason, and filed as `TOOL-aReapedTicket-4` rather than left as a silence:**
the unguarded holder reap. `ts_try_reap` does `rm -rf "$TS_DIR_C"` directly at two sites, which the
`aPacedTurnstile` spec explicitly prescribed a RENAME for and explained — a second reaper that
claimed in the gap has its fresh beacon destroyed, and two bars run. That is a different failure from
a different predicate, its failing case is a sub-millisecond race needing its own arm design, and
§7's rule is that a guard whose failing case has not been observed is not landed. The row carries the
spec citation and the observation that the property is testable WITHOUT racing it — two concurrent
reapers against one dead beacon must produce exactly one reap line — so the next session does not
re-derive either.

**One scope AMENDMENT, made while building and recorded rather than absorbed:** the beacon's own
release TRAP came into `TOOL-aReapedTicket-1`, which had declared the beacon out of scope. Verifying
the ticket trap refuted the spec's reasoning about it — a trap on `INT` replaces the default
disposition, so a handler that does not `exit` drops the ticket and resumes the loop ticketless — and
the claim-time trap carried that identical spelling ten lines away, where it releases the beacon and
then keeps running the bar. Fixing one and leaving the other is the fix-the-instance-not-the-class
failure §7 names. Spec rev-2 carries the refutation.

**No unit may make the turnstile able to wedge a bar.** `run-gates.sh:526-529` states the standing
constraint: the turnstile fails open, loudly, and contributes nothing to the exit code, ever. A
reaper that can delete a live waiter's ticket violates this by making that waiter unable to acquire,
so every sweep predicate must be one that cannot be true of a live waiter.

### Classification (M2)

All three units were MISSING at open. They are authored this run and therefore unreviewed by
definition until M4 runs.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aReapedTicket-1` | 2 | a queued waiter drops its own ticket on every signal a trap can catch |
| 2 | `TOOL-aReapedTicket-2` | 2 | the acquire loop asserts liveness on the QUEUE, and refuses to wait on what cannot change |
| 3 | `TOOL-aReapedTicket-3` | 2 | arms for a dead waiter, which the suite has never had |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 3 unit(s) · node a · opened 2026-08-27 · streams tooling
ids TOOL-aReapedTicket-1 TOOL-aReapedTicket-2 TOOL-aReapedTicket-3 TOOL-aReapedTicket-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aReapedTicket-1 — a queued waiter drops its own ticket on every signal a trap can catch](spec/2026-08-27-spec-TOOL-aReapedTicket-1.md) | 1 | 2 | INPROGRESS | rev-2 | 2026-08-27 |
| [TOOL-aReapedTicket-2 — the acquire loop asserts liveness on the QUEUE, and refuses to wait on what cannot change](spec/2026-08-27-spec-TOOL-aReapedTicket-2.md) | 2 | 2 | INPROGRESS | rev-2 | 2026-08-27 |
| [TOOL-aReapedTicket-3 — arms for a dead waiter, which the suite has never had](spec/2026-08-27-spec-TOOL-aReapedTicket-3.md) | 3 | 2 | INPROGRESS | rev-2 | 2026-08-27 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aReapedTicket-1 TOOL-aReapedTicket-2 TOOL-aReapedTicket-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aReapedTicket-1` | no |
| 2 | `TOOL-aReapedTicket-2` | no |
| 3 | `TOOL-aReapedTicket-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
