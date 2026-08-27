# TOOL-aReapedTicket-2 — the acquire loop asserts liveness on the QUEUE, and refuses to wait on what cannot change

**Status:** INPROGRESS · rev-2 · 2026-08-27 · node a · Tier-2 · base f1be0b49 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-prompt-TOOL-aReapedTicket-1.md](../prompts/2026-08-27-prompt-TOOL-aReapedTicket-1.md) | research | TOOL-aReapedTicket-1 TOOL-aReapedTicket-3 |

<!-- /gen:spec-records -->

## 1. Goal

Make the turnstile's acquire loop unable to wait forever on a condition that can never become true:
sweep a queue ticket whose owner has stopped existing, using the same two-signal shape the beacon
reaper already uses, and stop reporting a holder that does not exist.

## 2. Scope (IN)

- `tools/run-gates/run-gates.sh`, the turnstile block: a queue sweep run on the same tick as
  `ts_try_reap`, with two signals — a dead pid, and an age past `TS_MAXWAIT`.
- The two reporting defects observed alongside the wedge: `ts_try_reap` returning immediately when no
  beacon exists, so the only liveness machinery in the unit cannot look at what is actually blocking;
  and the waiter's stderr line claiming another bar holds the repository when nothing holds it.
- The `TS_TICKET=""` path, where a failed ticket write makes the acquire predicate permanently false
  and the run burns the entire `TS_MAXWAIT` before failing open.

## 3. Non-goals (OUT)

- Preventing the leak. `TOOL-aReapedTicket-1` does that; this unit is the backstop for the deaths no
  trap can catch, and the two are complementary rather than alternative.
- Giving a ticket a heartbeat file. A waiter cannot be alive-but-wedged — it does nothing but poll —
  so the second signal it needs is age, and the ticket name already carries a UTC timestamp. A
  heartbeat would add a file, a refresh site and a staleness constant to buy a distinction that does
  not exist.
- The holder-reap race. Out by the build README's ruling.
- Changing `TS_TTL`, `TS_MAXWAIT`, `TS_TICK` or the FIFO ordering. This unit introduces **no new
  constant**.

## 4. Design

### What was observed

With **no beacon at all** and one planted ticket from a killed run, a bar prints
`another bar holds this repository — queued at position 2`, waits the full bound, prints
`turnstile WAIT EXPIRED`, and runs UNQUEUED — leaving the ticket in place for the next bar. The full
transcript is in the prompt record. Three separate defects are visible in it, and they share one
root: the loop's exit conditions are "I sorted first" and "the clock ran out", and neither of them
can be reached by anything the loop itself observes.

### Signal 1 — a dead pid

The ticket name is `$TS_Q/$(date -u +%Y%m%dT%H%M%S)-$$-$RANDOM`. The timestamp field contains no
hyphen, so the name splits on `-` into exactly three fields and the pid is field 2. `ts_alive` at
`:445` already wraps `kill -0`. So the signal costs a `cut` and an existing helper.

It is **negative-only**, exactly as the beacon spec argues at
`aPacedTurnstile/spec/…-4.md` under "Reaping — both signals, and why neither alone": a failure to
signal proves the owner is gone; a success proves nothing, because pids are recycled. So success
withholds the sweep and never confers life.

### Signal 2 — an age past `TS_MAXWAIT`

This is the recycled-pid case, and the bound is DERIVED rather than chosen. A live waiter fails open
at `TS_MAXWAIT` and drops its own ticket at `:530`. Therefore a ticket older than `TS_MAXWAIT`
**cannot** belong to a live waiter — the property is a consequence of the fail-open rule already in
the file, not a guess about how long a bar takes. `TS_MAXWAIT` is `TS_TTL * 4` and is already
computed at `:410`.

The age is read from the ticket's own name, not from its mtime: the name is what the ordering is
derived from, and a name and an mtime that disagree would give the sweep and the sort two different
opinions about the same ticket. `date -u -d` on the parsed stamp, falling back to skipping the ticket
if the stamp does not parse — a ticket whose name we cannot read is one we must not delete.

### The safety property this unit must not violate

`:526-529` states the standing constraint: the turnstile fails open, loudly, and never contributes to
the exit code. **A sweep that deletes a live waiter's ticket violates it**, because that waiter can
then never satisfy the acquire predicate and spins to the bound — converting a wedge that affects
future bars into one that affects the bar in front of you. Both signals above are therefore chosen so
they cannot be true of a live waiter, and neither is a heuristic:

| signal | why a live waiter cannot match it |
|---|---|
| `kill -0` fails | a live waiter's own pid answers, by definition |
| name older than `TS_MAXWAIT` | a live waiter drops its ticket at that bound, at `:530` |

**A sweep never touches this run's own ticket.** Guarded explicitly rather than left to the two
signals above, because our own pid is alive and our own ticket is young, so the guard is redundant
today — and it is exactly the redundancy that stops a future edit to either signal deleting the
ticket of the process doing the sweeping.

### The reporting defects

**`ts_try_reap` cannot move when there is no beacon.** Its first line is
`[ -d "$TS_DIR_C" ] || return 1`. That is correct for the beacon and is left alone; the queue sweep
is a SEPARATE function called on the same tick, so it runs whether or not a beacon exists. This is
the charter's "a probe that cannot move says so" — today the reaper reports nothing in exactly the
state where something needs reaping.

**The waiter's line names a holder that may not exist.** The message is emitted from the failure of
the acquire predicate, which conflates "someone is ahead of me in the queue" with "someone holds the
beacon". The two are distinguishable with a `[ -d "$TS_DIR_C" ]` the loop can already afford, and the
line reports whichever is true. A reader diagnosing a wedge must not be sent to look for a holder
that does not exist, which is what happened in the reproduction.

**`TS_TICKET=""` spins the whole bound.** `: > "$TS_TICKET" || TS_TICKET=""` at `:478` is the only
place this is set, and every subsequent iteration's predicate begins `[ -n "$TS_TICKET" ]`, which is
false forever. The run cannot acquire and cannot ever acquire, so it must fail open AT ONCE with that
reason, rather than burning `TS_MAXWAIT` first to reach the same outcome. Same class as the two
above: a loop waiting on a condition that cannot change.

**And it needs its own `queued_from` state — `unticketed` — which rev-1 did not foresee.** The
existing comment above that block reasons explicitly that "an `expired` run has burned at least
`TS_MAXWAIT` … and therefore never 0", and leans on it to conclude that a `queued 0` is unambiguous.
A run that fails open on the first tick has a wait of exactly 0, so recording it as `expired` would
falsify that invariant silently — the `amendment-leaves-its-other-half-standing` class, in the very
paragraph that states the rule. A fourth state word keeps the sentence true as written instead. The
key is read BY NAME by the suite's `hdrkey` helper, and that file's own header records that an arm
counting keys or reading them by position would red on every future addition, so a new member is
additive by design.

### Where the sweep is called

Immediately beside `ts_try_reap && continue` at `:523`, and on the same tick. Not before the acquire
attempt: an uncontended run must keep its current fast path, and arm 13's `^gate queue: waited 0s$`
assertion is sensitive to work added ahead of the claim — the comment at `:507-515` records that four
of sixty first-iteration acquires already straddle a second boundary with the five processes there
today.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh` — one new function (~15 lines), its call site, the two reporting
  changes, and the `TS_TICKET=""` early exit. Under 70 lines with comments.

### Alternatives rejected

- **Sweep the whole queue at startup, before taking a ticket.** Rejected: it does not help the run
  that is already queued when a peer dies, and it moves the sweep off the tick where the wedge is
  actually observed.
- **Reap the ticket by renaming it to a graveyard, as the holder path was specced to do.** Rejected,
  and the original spec gives the reason: "Ticket names carry a unique nonce and are never
  re-created, so deleting one has no such hazard." A rename buys atomicity against a successor
  re-creating the same name, which cannot happen for a ticket.
- **Let the first waiter sweep and the others trust it.** Rejected: it elects a coordinator, which is
  the property the ticket design deliberately avoids — every waiter derives the same order
  independently, and the same must be true of the sweep.
- **Shorten `TS_MAXWAIT` so the wedge costs less.** Rejected as a symptom fix: it makes every bar give
  up on a legitimately busy peer sooner and still leaves a queue that never drains.

## 5. Production-readiness checklist

- security — N/A. Deletes files under a directory in the git common dir that this runner already
  creates and writes; no new path, no untrusted input. The ticket NAME is parsed, and it is a name
  this runner authored — but the parse is defensive anyway (an unparseable stamp skips the ticket)
  because the directory is writable by anything running as this user.
- perf / scale — one `ls`, one `cut` and one `kill -0` per queued ticket per tick, on a queue
  measured at single digits. Runs only on the contended path, so an uncontended bar pays nothing.
- a11y — N/A, not a user interface.
- i18n — N/A, operator-facing stderr in the runner's existing voice.
- error / empty / loading states — an empty queue directory sweeps nothing; an unparseable ticket
  name is skipped, not deleted; a `rm` that fails is ignored, exactly as `ts_drop_ticket` does.
- observability — every sweep prints its reason to stderr, in the shape `ts_try_reap` already uses
  (`reaping the beacon of a dead holder (pid %s)`). This is required, not optional: a reaper that
  works silently is indistinguishable from one that never fires, which is the liveness rule §7
  states.
- risks (concurrency, data-loss, rollback hazards) — the material risk is deleting a live waiter's
  ticket, addressed by the table above and by the own-ticket guard; two waiters sweeping the same
  dead ticket concurrently both issue `rm -f`, and the loser's failure is ignored. No data is at
  risk: a ticket is an empty file. Rollback is deleting the function and its call site.
- testing + left-shift gates — `TOOL-aReapedTicket-3`, including the arm that stops a
  sweep-everything reaper passing.
- migration / rollback — this unit is what clears tickets leaked BEFORE it lands, which is why it and
  `TOOL-aReapedTicket-1` land together. No state format changes.
- user docs — N/A. Internal mechanism of one gate runner, no `help/` surface.

## 6. Acceptance criteria

- **AC1** — When a queue holds a ticket whose pid is dead and no beacon exists, the next bar sweeps
  it and acquires within one `TS_TICK` rather than waiting for the bound, asserted in
  `tools/run-gates/run-gates.turnstile.test.sh`. The same fixture on today's runner reaches
  `turnstile WAIT EXPIRED`, which is recorded in the prompt record.
- **AC2** — When a queue holds a ticket whose pid is ALIVE but whose name is older than
  `TS_MAXWAIT`, it is swept, and the stderr reason names the age rather than the pid — so the second
  signal is asserted against the unmodified runner and not satisfied by the first.
- **AC3** — When a waiter is queued behind a LIVE waiter that is ahead of it, that live waiter's
  ticket is still present after several ticks. This is the arm that stops a reaper which sweeps
  everything from passing `AC1` and `AC2`.
- **AC4** — When a bar sweeps a ticket, it says so on stderr with the reason, in the shape
  `ts_try_reap` already uses — so a sweep that never fires is distinguishable from one that fires
  silently, which is the liveness assertion §7 requires. Asserted on the stderr text in
  `tools/run-gates/run-gates.turnstile.test.sh`.
- **AC5** — When no beacon exists and a ticket is ahead of the waiter, the queued line does NOT claim
  another bar holds the repository; it reports the queue. Asserted on the stderr text against the
  fixture from `AC1`.
- **AC6** — When `TS_TICKET` is empty because the ticket write failed, the run fails open immediately
  with a reason naming the ticket, rather than after `TS_MAXWAIT`; asserted by a fixture that makes
  the ticket write impossible and bounds the observed wall clock well under the bound. The portable
  way to force it is to create `gate-bar-queue` as a FILE — `mkdir -p` then fails and the write
  cannot succeed — rather than by changing a mode, which a directory this user owns often ignores.
- **AC7** — The same run records `queued_from` as `unticketed`, distinct from `expired`, so a
  `queued 0` never has to be disambiguated by guesswork and the existing "an expired run is never 0"
  invariant stays true. Read from the run-record header by name.

## 7. Gates

- `run-gates turnstile` — the leg that owns this mechanism.
- `run-gates canary`, `run-gates evidence`, `run-gates adopter e2e` — the sibling legs this file's
  guard selects.
- `line-length` and `gate-lint`.
- Adds no new gate leg; `TOOL-aReapedTicket-3` extends the existing one.

## 8. Open questions

- **F1 — is the age signal read from the ticket NAME or its mtime?** FACT-QUESTION · The probe is
  whether the two can disagree: a `touch` on an existing ticket changes the mtime and not the name,
  and a copied or restored queue directory changes both independently, whereas the SORT that decides
  acquisition order reads the name only. The observation that decides it is that the sort key and the
  staleness key must be the same field, or a ticket can be simultaneously first-in-order and
  stale-by-clock, which is two mechanisms disagreeing about one ticket. The liveness assertion is
  that the probe can produce a negative: if the runner ordered by mtime, the answer would be mtime.
  It orders by name (`ls -1 | LC_ALL=C sort`, `:483`).
  RESOLVED (agent, 2026-08-27, delegated): the NAME, per the observation above.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft, written from the reproductions in the prompt record.
- rev-2 · 2026-08-27 · added the `unticketed` `queued_from` state and AC7. rev-1 specced the early
  fail-open without noticing that recording it as `expired` would falsify the invariant the existing
  comment beside that block states in prose — found while building, by reading the comment the change
  sat next to rather than by a gate. Also pinned in AC6 the portable way to force a ticket-write
  failure, after a mode change proved useless on a directory this user owns.

## 10. Reuse audit

**The seam is `ts_try_reap` at `tools/run-gates/run-gates.sh:451` — not to be extended, but to be
MIRRORED.** Its two-signal structure, its negative-only pid reasoning and its stderr reason line are
the shape this unit copies for the other participant. Extending it in place was considered and
rejected in §4: its first line is a beacon-existence guard that is correct for the beacon and fatal
for the queue, and the two probes must run on the same tick but under different preconditions.

Three existing pieces are reused rather than re-implemented: `ts_alive` (`:445`) for pid liveness,
`TS_MAXWAIT` (`:410`) for the staleness bound, and `ts_now` (`:444`) for the clock. **This unit
introduces no new constant**, which is the property that keeps the bound derived rather than typed.

The recall pass is the one recorded in `TOOL-aReapedTicket-1` §10 — the obligation is satisfied once
for the SET, per M5, and the terms are recorded there so a regrounding pass can re-run the query. Its
load-bearing hit,
`memory/builds/aPacedTurnstile/spec/2026-08-18-spec-TOOL-aPacedTurnstile-4.md:195`, is the sentence
this unit implements: "ticket reap is by DELETE… Ticket names carry a unique nonce and are never
re-created, so deleting one has no such hazard." Verified against source rather than trusted: the
shipped runner has no code reading `$TS_Q` for liveness.
