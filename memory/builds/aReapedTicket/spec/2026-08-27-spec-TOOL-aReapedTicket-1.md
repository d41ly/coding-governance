# TOOL-aReapedTicket-1 — a queued waiter drops its own ticket on every signal a trap can catch

**Status:** CLOSED · rev-2 · 2026-08-27 · node a · Tier-2 · base f1be0b49 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aReapedTicket-1-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aReapedTicket-1-acceptance-ledger.md) | journal | TOOL-aReapedTicket-2 TOOL-aReapedTicket-3 |
| [2026-08-27-prompt-TOOL-aReapedTicket-1.md](../prompts/2026-08-27-prompt-TOOL-aReapedTicket-1.md) | research | TOOL-aReapedTicket-2 TOOL-aReapedTicket-3 |

<!-- /gen:spec-records -->

## 1. Goal

Give the queue ticket the same signal handling the beacon already has, from the instant the ticket
exists rather than from the instant the beacon is won — so that interrupting a queued bar removes its
place in the queue instead of leaving a file that blocks the repository forever.

## 2. Scope (IN)

- `tools/run-gates/run-gates.sh`, the turnstile block only: arming a trap that runs `ts_drop_ticket`
  across the whole queued life of a waiter, which today is unhandled.
- The interaction with the two traps that already exist — the claim-time trap at `:502` and the
  `cleanup` trap at `:603` — so that at no point is there no handler, and no handler undoes another's
  work.

## 3. Non-goals (OUT)

- Reaping a ticket whose owner died UNCATCHABLY. A trap cannot catch `SIGKILL`, an OOM kill or a
  power loss, and pretending otherwise is the whole reason a backstop is a separate unit.
  `TOOL-aReapedTicket-2` owns that.
- Anything about the beacon's own REAPING or its nonce. Untouched. Its release TRAP is in scope as
  of rev-2, for the reason §4 gives — it carries the identical defect this unit fixes, in the
  identical shape, ten lines away.
- The holder-reap race recorded in the build README's BUILD-LEVEL RULES. Out by an explicit ruling.
- Changing the acquire predicate, the wait bound, or the FIFO ordering.

## 4. Design

### The defect, stated precisely

`run-gates.sh:477-478` creates the ticket. `run-gates.sh:502` arms
`trap 'ts_release; ts_drop_ticket' EXIT INT TERM HUP`, and that statement is inside the `if` branch
that wins the beacon. `grep -n '^ *trap' tools/run-gates/run-gates.sh` returns exactly four sites:
`:502`, then `:603`, `:604`, `:605`, `:606` — all of which are after the turnstile block. A waiter
polling the acquire loop between `:480` and `:540` therefore runs with **no handler at all**, and the
ticket it created at `:478` outlives it.

This is the identical defect the comment at `:491-501` describes for the beacon, and that comment
already carries the measurement that justifies fixing it — "A signal in that window killed the run
and left the repository queueing behind nobody until the TTL expired." The ticket window is not a
few seconds like the beacon's; it is the entire queue wait, which is what this unit exists for.

### The mechanism

Arm a ticket-only handler immediately after the ticket is created, before the loop is entered:

```
trap 'ts_drop_ticket' EXIT INT TERM HUP
```

It is deliberately NOT `ts_release; ts_drop_ticket`. At this point no beacon is held, `TS_DIR` is
empty, and `ts_release` returns 0 on its first line — so including it would be inert code that reads
as though the waiter could release something it never claimed.

The two later traps SUPERSEDE it, which is safe because `trap` REPLACES rather than appends:

- `:502` replaces it with `ts_release; ts_drop_ticket` at the instant of the claim. Strictly wider —
  it still drops the ticket — so nothing is lost in the swap and there is no instant with no handler.
- `:603-606` replaces that with `cleanup`, which calls both. Also strictly wider.

`ts_drop_ticket` is already idempotent (`[ -n "$TS_TICKET" ] && rm -f …; TS_TICKET=""`), so a handler
firing after the ticket was dropped at `:530` or `:542` is a no-op.

### The signal arms MUST re-exit — and rev-1 of this spec had this wrong

rev-1 argued that a bare `trap 'ts_drop_ticket' EXIT INT TERM HUP` was sufficient because "this
covers a window in which bash's own default disposition for `INT`, `TERM` and `HUP` is already to
terminate." **That is false, and it was refuted by running it.** Setting a trap on a signal REPLACES
the default disposition. A handler that does not exit runs and then RESUMES the loop — so the run
drops its ticket and keeps polling, ticketless, with an acquire predicate that can never match
again, and spins to the full bound. That is precisely the "a waiter that can never acquire" state
this build exists to remove, re-created by this unit's own fix.

Observed: under `timeout -s INT -k 5`, the patched runner had to be escalated to `SIGKILL` on all
three signals, because it would not die. The corrected spelling follows the convention already in
this file at `:621-624` — a bare `EXIT` arm, and one arm per signal re-exiting with the conventional
`128+n`:

```
trap 'ts_drop_ticket' EXIT
trap 'ts_drop_ticket; exit 130' INT
trap 'ts_drop_ticket; exit 143' TERM
trap 'ts_drop_ticket; exit 129' HUP
```

**This is why the claim-time trap is now in scope.** `:520` was the same single-handler spelling —
`trap 'ts_release; ts_drop_ticket' EXIT INT TERM HUP` — so it carries the identical defect: an
interrupt in the window between claiming the beacon and the `cleanup` traps releases the beacon and
then RESUMES, leaving the run believing it holds a lock it has just given away and running the whole
bar beside whoever claims next. That is the two-bar condition the turnstile exists to prevent,
arriving through its own cleanup path — the same shape the nonce guard was written for. Fixing this
unit's trap and leaving an identical one ten lines below would be the fix-the-instance-not-the-class
failure §7 names, so both are corrected in one commit and to one convention.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh` — two trap sites, four statements each, with their comments. Under
  45 lines.

### Alternatives rejected

- **Move the `:502` trap earlier instead of adding one.** Rejected: `:502` must arm `ts_release` at
  the exact instant of the claim, and moving that line earlier would arm a release for a beacon not
  yet held — which is the failure the nonce guard at `:443` exists to prevent, reintroduced through
  the trap.
- **Create the ticket inside the loop, after a first acquire attempt.** Rejected: every run takes a
  ticket precisely so the FIFO order is total and derived identically by every waiter. Making ticket
  creation conditional breaks the ordering property the unit is built on.
- **Rely on `TOOL-aReapedTicket-2`'s sweep alone.** Rejected on cost, not on principle. The sweep's
  fast signal is a dead pid, and a pid can be RECYCLED — a leaked ticket whose pid has been reused by
  a live process falls through to the age signal, which is `TS_MAXWAIT` = 7200 s in production. Not
  leaking in the first place is two lines and removes that exposure for every catchable signal, which
  is the case that actually produced this incident.

## 5. Production-readiness checklist

- security — N/A. No new file, no new path, no widened surface; the handler deletes a file this
  process created under a directory it already writes.
- perf / scale — N/A. One `trap` builtin at startup, no per-tick cost.
- a11y — N/A, not a user interface.
- i18n — N/A, operator-facing stderr in the runner's existing voice.
- error / empty / loading states — `ts_drop_ticket` already tolerates an empty `TS_TICKET` and a
  failed `rm`; the case where `: > "$TS_TICKET"` failed and set `TS_TICKET=""` is handled by that
  same guard.
- observability — deliberately silent. A waiter dropping its ticket on a signal is the correct
  behaviour, not an event, and the runner's stderr on interrupt is already the interrupt itself.
- risks (concurrency, data-loss, rollback hazards) — the one real hazard is a handler that deletes a
  ticket still in use. It cannot: the handler is scoped to `$TS_TICKET`, which is this process's own
  ticket and is never another run's. Rollback is deleting one statement.
- testing + left-shift gates — `TOOL-aReapedTicket-3` arms it; the failing case is already observed
  and recorded in the prompt record.
- migration / rollback — none. A leaked ticket from BEFORE this lands is not removed by this unit;
  that is `TOOL-aReapedTicket-2`'s job and is why the two land together.
- user docs — N/A. Internal mechanism of one gate runner, no `help/` surface.

## 6. Acceptance criteria

- **AC1** — When a bar is queued behind a live holder and receives `SIGINT`, its ticket is gone from
  the queue directory afterwards, asserted in `tools/run-gates/run-gates.turnstile.test.sh` against
  the unmodified runner. The same observation on today's runner leaves the ticket behind, which is
  recorded in the prompt record.
- **AC2** — The same holds for `SIGTERM` and `SIGHUP`, so the arm cannot pass on `INT` alone while
  the other two members of the trap's signal list are unasserted.
- **AC3** — When a bar acquires the beacon uncontended and exits cleanly, its ticket is gone and the
  beacon is released — the existing arm 8 behaviour is unchanged, proving the added trap is
  superseded rather than competing with the claim-time trap and `cleanup`.
- **AC5** — When a queued bar is signalled, it EXITS rather than resuming the loop, observed as the
  absence of a `SIGKILL` escalation under `timeout -s <sig> -k`. rev-1's spelling failed this on all
  three signals, which is what produced rev-2.
- **AC6** — When a bar holding the beacon is signalled in the window before the `cleanup` traps arm,
  it releases and EXITS rather than continuing to run unqueued while believing it holds the lock.
  Same defect, same arm shape, at the claim-time trap.
- **AC4** — `grep -c "^ *trap" tools/run-gates/run-gates.sh` shows the new site, and the ticket is
  created at a line NUMBER lower than that site — the ordering property this unit is about, asserted
  structurally so a later edit that moves the trap back inside the win branch reds.

## 7. Gates

- `run-gates turnstile` — `tools/run-gates/run-gates.turnstile.test.sh`, the leg that owns this
  mechanism.
- `run-gates canary`, `run-gates evidence`, `run-gates adopter e2e` — the sibling legs guarded on
  `tools/run-gates/`, which this file's guard selects.
- `line-length` and `gate-lint` — repository-wide shape legs that select any edited shell file.
- Adds no new gate; `TOOL-aReapedTicket-3` extends an existing one.

## 8. Open questions

none — the mechanism is a two-line application of an argument already written into this file at
`:491-501` for the sibling participant, and its failing case was observed before the spec was
written.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft, written from the reproductions in the prompt record.
- rev-2 · 2026-08-27 · REFUTED rev-1's claim that the signal arms need no explicit `exit` — a trap
  replaces the default disposition, so the handler dropped the ticket and resumed the loop
  ticketless, and `timeout -s INT -k` had to escalate to `SIGKILL` on all three signals. Corrected to
  the `128+n` convention already in the file. The refutation came from running the change, not from
  re-reading it, which is why it is recorded rather than quietly amended. Scope widened to the
  claim-time beacon trap, which carried the identical defect in the identical shape; §3 and §4 say
  why leaving it was not an option, and AC5/AC6 were added. **The code for the sibling trap was
  written before this rev bump** — the divergence was found by verification mid-pass, and the spec
  is being corrected in the same pass rather than after it.

## 10. Reuse audit

**The seam is `ts_drop_ticket` at `tools/run-gates/run-gates.sh:446`, which already exists, is
already idempotent, and is already the body of the trap at `:502`.** This unit adds no function; it
arms the existing one over the window it was never armed over. That is the whole of the change, and
it is why this is the smallest of the three units.

`python tools/codebase-map/reuse_lookup.py "gate turnstile queue ticket liveness reaping a dead
waiter"` returned the `run-gates` kit's `KITDIR`/`ROOTN`/`LEGS_FILE` affordance seam and the
`run-gates turnstile` inventory key, and no ticket-lifecycle candidate — correctly, because none
exists.

`python tools/memory-recall/query.py "why does the gate turnstile reap only the beacon holder and not
queue tickets" --terms "turnstile beacon queue ticket reap liveness heartbeat holder waiter deadlock
nonce acquire predicate wedge"` returned 39 hits. **The load-bearing one is
`memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md:195`**, which specced
ticket reaping and justified its delete semantics, and whose unit is recorded `RE-SCOPED`. A hit can
be stale, so the claim was verified against source: `run-gates.sh` contains no code that reads
`$TS_Q` for liveness, and the only `trap` inside the turnstile block is at `:502`. The spec and the
shipped runner disagree, and the runner is the one that is wrong.
