---
slug: aReapedTicket
node: a
opened: 2026-08-27
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aReapedTicket-1 TOOL-aReapedTicket-2 TOOL-aReapedTicket-3 TOOL-aReapedTicket-4 TOOL-aReapedTicket-5
---

# aReapedTicket — the turnstile's queue gets the liveness its beacon already has

## The problem this build exists to solve

**A participant of the turnstile that has stopped existing must stop blocking the ones that still
do — on the QUEUE exactly as on the BEACON.** That sentence is this build's immutable description.

The turnstile asserts liveness on one of its two participants. A holder has a dead-pid signal and a
stale-heartbeat signal; a queue ticket has neither, and the acquire predicate is a pure sort order
over a directory nothing prunes. So a bar killed while queued leaks a ticket that sorts first
forever, and the unit that exists to stop two bars running at once is disabled — permanently, by one
death. Grounded and reproduced before any unit was written:
[the prompt record](prompts/2026-08-27-prompt-TOOL-aReapedTicket-1.md).

## Expected improvements

- A killed bar stops wedging the repo: every later one burned `TS_MAXWAIT` (7200 s) then ran
  UNQUEUED, so the turnstile was defeated rather than slowed.
- Both deaths covered — a trap for catchable signals, a sweep for the rest — reusing the beacon's
  two-signal shape with no new constant.
- The suite gains the queue arms it never had: 11 of their 20 are RED at BASE.

## Detriments if this is not built

- One SIGINT on a queued bar leaves the repository permanently unable to serialize its bars.
- The symptom points at the wrong thing: the runner names a holder that is not there, so a reader
  hunts a process that does not exist.
- Every bar silently pays two hours and then runs concurrently anyway — the exact condition the
  turnstile was built to prevent.

## Build-level rules

**Scoped OUT, filed as `TOOL-aReapedTicket-4`, not left as a silence:** the unguarded holder reap.
`ts_try_reap` deletes the beacon with a bare `rm -rf` where the `aPacedTurnstile` spec prescribed a
RENAME and said why — a second reaper can destroy a successor's fresh beacon and two bars run.
Different failure, different predicate, and its failing case is a sub-millisecond race needing its
own arm, so §7 forbids landing a guard for it here.

**One scope AMENDMENT, made while building:** the beacon's release TRAP came into
`TOOL-aReapedTicket-1`, which had declared the beacon out of scope. Verification refuted the spec —
a trap on `INT` replaces the default disposition, so a handler that does not `exit` drops the ticket
and resumes the loop ticketless — and the claim-time trap carried that identical spelling ten lines
away. Fixing one and leaving the other is the fix-the-instance-not-the-class failure. Spec rev-2
carries it.

**No unit may make the turnstile able to wedge a bar.** It fails open, loudly, and contributes
nothing to the exit code. So every sweep predicate is one that cannot be true of a LIVE waiter.

## Parked decisions

**The closing Tier-2 diff review did not run.** This session's operating instructions forbid
invoking the agent and workflow tools unrequested, and `BUILD-METHOD.md` M8's review is exactly
that. The units are gate-verified and self-reviewed; the adversarial pass is owed.

**This build has no run-state file.** `--preflight` refused — two other builds held non-terminal
records — so there is no phase witness and no `--close`, and the merge was made on an explicit owner
instruction rather than under the unattended mandate. Cause recorded as `TOOL-aReapedTicket-5`.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aReapedTicket-1` | 2 | a queued waiter drops its own ticket on every signal a trap can catch |
| 2 | `TOOL-aReapedTicket-2` | 2 | the acquire loop asserts liveness on the QUEUE, and refuses to wait on what cannot change |
| 3 | `TOOL-aReapedTicket-3` | 2 | arms for a dead waiter, which the suite has never had |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node a · opened 2026-08-27 · streams tooling
ids TOOL-aReapedTicket-1 TOOL-aReapedTicket-2 TOOL-aReapedTicket-3 TOOL-aReapedTicket-4 TOOL-aReapedTicket-5

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aReapedTicket-1 — a queued waiter drops its own ticket on every signal a trap can catch](spec/2026-08-27-spec-TOOL-aReapedTicket-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-08-27 |
| [TOOL-aReapedTicket-2 — the acquire loop asserts liveness on the QUEUE, and refuses to wait on what cannot change](spec/2026-08-27-spec-TOOL-aReapedTicket-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-08-27 |
| [TOOL-aReapedTicket-3 — arms for a dead waiter, which the suite has never had](spec/2026-08-27-spec-TOOL-aReapedTicket-3.md) | 3 | 2 | CLOSED | rev-2 | 2026-08-27 |
<!-- /gen:build-units -->

Records: 2 bound to this build, across 3 record folder(s).

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
