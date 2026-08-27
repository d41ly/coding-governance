# The owner's prompt — a lander wedged for hours behind three dead landers

**Serves:** research TOOL-aReapedTicket-1 TOOL-aReapedTicket-2 TOOL-aReapedTicket-3

Handed to `/unattended --prompt` on 2026-08-27, node `a`. The value carried whitespace and named no
readable file, so it is the prompt itself and is recorded here verbatim. The bytes travel rather than
the reference: the build folder is the authorization and may not point at a file the run can edit.

## Verbatim

> A bug is discovered in the lander's queue beacon: another session's lander has been stuck in queue
> for hours behind three DEAD landers (they were hung and killed previously) and the queue would have
> never moved. There isn't a liveliness check, nor a check if a lander's making progress: the acquire
> predicate is "my ticket sorts first in the queue directory" — and there is no liveness check on
> queue tickets at all. The beacon reaps a dead holder; nothing reaps a dead waiter. So a killed bar
> leaves an immortal ticket that sorts first forever and wedges every future bar. Ground in the bug
> and systemically fix it.

## What the grounding pass OBSERVED, before any unit was written

Everything below was run against this tree at base `f1be0b49`, node `a`, in scratch repositories
built the way `run-gates.turnstile.test.sh` builds its fixtures. Nothing here is argued.

### The prompt's diagnosis is correct, and the mechanism is exactly as described

`tools/run-gates/run-gates.sh:483-485` — the acquire predicate is
`ls -1 "$TS_Q" | sort | head -1` equals my ticket's basename, `&& mkdir "$TS_DIR_C"`. A ticket is a
plain empty file at `$TS_Q/$(date -u +%Y%m%dT%H%M%S)-$$-$RANDOM`. `ts_try_reap` at `:451` reaps the
BEACON on two signals — dead pid, stale heartbeat — and reads nothing in the queue directory at all.

### The ROOT CAUSE is one line further back than the prompt reaches: a waiter has NO trap

The ticket is created at `:477-478`. The only handler that drops it is
`trap 'ts_release; ts_drop_ticket' EXIT INT TERM HUP` at `:502`, and that line is **inside the branch
that wins the beacon**. `grep -n '^ *trap' run-gates.sh` returns `:502` and then nothing until `:603`,
which is the scratch-dir trap AFTER the turnstile block. So for the entire queued life of a waiter —
which is the state this bug is about — there is no handler of any kind.

The leak therefore does not need `SIGKILL`. It needs **Ctrl-C**, which is how a bar most often dies.

**Observed.** A scratch repo, a beacon held by a live pid with a fresh heartbeat so it is never
reaped, one waiter queued behind it, then `timeout -s INT` straight to the runner:

```
queued tickets while waiting: 1
tickets left behind: 1 -> 20260827T140052-3536838-7367
```

The comment block at `:491-501` explains at length why the beacon's trap has to be armed at the
instant of the claim — "A signal in that window killed the run and left the repository queueing behind
nobody until the TTL expired." That is the same defect, one participant over, and the ticket did not
get the same treatment.

### The CONSEQUENCE is worse than "stuck behind three dead landers"

**Observed.** A scratch repo with **no beacon at all** — nothing holds the lock — and ONE planted
ticket from a killed run. `GATE_TURNSTILE_TTL=1` scales `TS_MAXWAIT` to 4 s so the wait is watchable:

```
queue before:  20200101T000000-999999-1
beacon before: NONE
run-gates: another bar holds this repository — queued at position 2 (waited 1s)
run-gates: turnstile WAIT EXPIRED after 9s (bound 4s) — running UNQUEUED alongside whatever holds the beacon
queue after:   20200101T000000-999999-1
```

Three facts in that transcript, none of them the reported one:

1. **The runner says another bar holds the repository. Nothing holds it.** The message is emitted
   from the failure of the *acquire* predicate, which conflates "someone is ahead of me in the queue"
   with "someone holds the beacon". A reader diagnosing the wedge is sent to look for a holder that
   does not exist.
2. **`ts_try_reap` cannot move.** Its first line is `[ -d "$TS_DIR_C" ] || return 1`. With no beacon
   there is nothing to reap, so the only liveness machinery in the unit returns immediately every
   tick and the loop spins. The reaper is not weak here; it is structurally unable to look at the
   thing that is actually blocking.
3. **The ticket survives the wedge it caused.** The expiring waiter drops only its OWN ticket
   (`ts_drop_ticket` at `:530`). So this is not a delay that drains — it is permanent. Every future
   bar on that repository takes a ticket that sorts after the immortal one, waits the full
   `TS_MAXWAIT`, and then runs UNQUEUED.

In production `PROF_TIMEOUT` is 0 on every row of `gate-profiles.txt`, so `TS_TTL` falls back to 1800
and `TS_MAXWAIT` is `TS_TTL * 4` = **7200 seconds**. Two hours per bar, forever, and the turnstile is
permanently defeated afterwards — every bar runs unqueued, which is precisely the concurrent-bar
condition the unit exists to prevent. "Stuck in queue for hours" is the observation; the standing
state is worse than the incident.

### The design intent EXISTED and was not built

`memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md:195`, in the section
titled "Reaping — both signals, and why neither alone":

> Holder reap is by RENAME and ticket reap is by DELETE, and the asymmetry is load-bearing. […]
> Ticket names carry a unique nonce and are never re-created, so deleting one has no such hazard.

So ticket reaping was specced, its delete semantics were justified, and the shipped runner has no
code for it. This is not an unforeseen case; it is a dropped mechanism. The unit is recorded
`RE-SCOPED` in that build's README, which is where it went.

### A SECOND mechanism from that same paragraph was also not built

The same sentence prescribes the holder half by RENAME, and gives the reason:

> The holder path is fixed, so deleting it directly can destroy a SUCCESSOR that claimed in the gap
> between reading the metadata and the delete.

The shipped `ts_try_reap` does `rm -rf "$TS_DIR_C"` directly, twice, with no guard. Two waiters that
both read a dead pid can both proceed to delete; the second delete lands on the fresh beacon of a
successor that claimed in between, and two bars then run. The `nonce` guard at `:443` protects
*release*, not *reap*, so it does not cover this.

**This is a different failure — two concurrent bars, not a wedge — from a different predicate.** It
is recorded here because it was found here and shares an origin, and it is scoped OUT of this build:
its failing case is a sub-millisecond race that needs its own arm design, and the charter forbids
landing a guard whose failing case has not been observed. It leaves as a backlog row citing the spec
paragraph above, so the next session does not re-derive it.

### What the existing arms cover

`tools/run-gates/run-gates.turnstile.test.sh` carries 15 arms. Arms 3, 4, 4b, 4c and 11 are all about
the HOLDER beacon; arms 5/6, 6b, 7, 7b, 7c are about FIFO order and the bounded wait, and every one
of them is driven by a fixture with a live holder. **Not one arm puts a ticket in the queue whose
owner is gone.** The suite is exactly as blind as the runner, which is why the bar has been green
across every landing since `aPacedTurnstile`.

## What the owner is NOT being asked

Nothing in this record needs an answer. Title, goal, scope, cut-line, acceptance and gates all derive
from the observations above, so the prompt path's single owner turn was not spent.
