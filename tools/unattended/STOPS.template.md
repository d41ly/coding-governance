# The unattended stop contract — HELD, the hold codes and the per-slug lease

*Installed beside `UNATTENDED-PROTOCOL.md` from the unattended kit and byte-compared against the
shipped template by the same leg that compares that pair. The protocol is still the contract; this
is the half of it that governs a run which STOPS without finishing, and it is binding in exactly the
way the protocol is.*

A run that meets something it cannot fix — a usage limit, an overloaded API, a degraded host, a red
it inherited and may not absorb — used to have two endings. It could write `ABORTED`, which is a
false sentence about a run that could continue, or it could hand a paragraph of prose to whoever
came back, which is not a record. `HELD` is the third: a phase a run ENTERS with a code, a release
condition and a witness, and LEAVES by `--resume` with no owner turn.

## 1. The phase

`HELD` is a core, non-terminal phase, placed after `RUNNING` and before `VERIFYING`. Its position is
a decision rather than a reading order: a hook that restates the driver's phase tail from `VERIFYING`
as the phases it admits a flagged bar and the kit's self-test suites in must not admit them to a run
held from `BUILDING`, which has no work to verify. A run held from `VERIFYING` or `LANDING` regains
the bar at the resume that returns it there, which is the whole of what it needs.

Three consequences, and each of them is a refusal in the driver rather than a convention:

- `--close`, `--landed` and `--phase` all refuse a HELD record, numbered and before any write.
  `HELD` is not terminal, so a verb testing only `is_terminal` would reach its own write from a run
  that paused part-way for a cause outside itself.
- `--phase` also refuses `HELD` as a TARGET. The phase is PRODUCER-ONLY: `--hold` writes it together
  with the facts that make it mean something, and a phase move into it would be that record with
  none of them — a pause nothing can evaluate and `--resume` cannot release.
- `--preflight` over a HELD record refuses, naming `--resume`. The re-preflight the protocol
  sanctions after a compaction is for a run that is WORKING; a paused one has a release condition to
  test, an authorization to re-verify and a lease to take.

Only `--landed` and `--abort` still write a terminal, and both go through the working phase a resume
returns the run to.

## 2. The codes

Kit-owned core, extended by `HOLD_CODES_EXTRA` and pinned shrink-only by `HOLD_FLOOR`:

`host-degraded` · `platform-limit` · `platform-unavailable` · `host-owner-action` · `inherited-red`

These are a SECOND vocabulary beside the halt codes and never an extension of them. A halt code ends
a run and a hold code pauses one, and a single list would let a pause be recorded as an ending.

## 3. The release conditions

```
condition = "after " <utc-instant> | "probe " ("host" | "gate" | "api") | "owner"
```

`<utc-instant>` is ISO-8601 in UTC to the second with a trailing `Z`, the shape the `held-at` fact
records, so the two fields are comparable without a second parser. The grammar is CLOSED and is
validated at `--hold`, not at `--resume`: an unvalidated condition reaches a resume scheduler's
fire-instant computation as free prose.

What each means at `--resume`:

- **`after`** is met when the clock has passed it. Unmet, the resume prints `still held` and writes
  nothing — not the phase, not the lease. A clock that answers nothing is a DEAD PROBE and refuses,
  because a zero from a dead clock would read as released.
- **`probe host|gate|api`** is met on any resume. The resumed run's next act IS the probe; if it
  fails again the run holds again. This is the only reading a driver can honour — it cannot observe
  the API it runs under.
- **`owner`** is met on any resume, and nothing schedules one. A hold whose release needs a human act
  on the machine is released by whoever restarts it.

## 4. What `--hold` refuses

Every refusal is numbered and comes BEFORE any write. A `--hold` that wrote the phase and then found
a dirty tree would leave a HELD record standing over uncommitted work, with a witness naming a commit
that is not what the tree holds — and the take-over would re-verify a mandate against it.

1. The record must exist, be live, and not already be HELD. A second hold overwrites `held-from`
   with `HELD`, which is the one field `--resume` reads to find the way back.
2. `--code`, `--until` and `--reason` are all required. The code is what every machine reader joins
   on; the reason is the only sentence the owner gets in place of the turn nobody took, and it may
   not spell the declared bypass flag, which the gate greps this file whole for.
3. Exactly one of `--reaped <id>` and `--keepalive-unreachable <node>`. A keepalive still firing into
   a HELD run re-dispatches its units at the next tick. The driver cannot reap a job in a session
   store it cannot see; it can only record that somebody did. `--reaped` must name the keepalive the
   slug currently runs under — the lease's id when there is one, the record's `keepalive` fact
   otherwise — because a holder that replaced its own job records the new id in the lease first.
4. The tree must be clean and committed.
5. Under `ANCHOR_SCOPE=published`, the branch tip must be on its remote.

### The unpublished-tip exception

A design rule ends a stop HELD only with the branch pushed. In a sustained outage that push fails
too, which would leave the outage with no ending but `ABORTED` — the ending `HELD` exists to replace.
So `--code platform-unavailable` alone may hold an unpublished tip, and ONLY when the remote does not
ANSWER. A remote that answers still requires the push, and no other code is excepted.

The tip is then recorded as `hold-unpushed`, `--status` prints it on the checkpoint line, and a
take-over prints the push as its first act. Work that exists on one node only is never silent.

## 5. The facts and the history row

`--hold` writes, in the authored region of the run-state file:

| Fact | Value |
|---|---|
| `phase` | `HELD` |
| `witness` | HEAD's sha, which the clean-and-committed precondition makes meaningful |
| `held-from` | the working phase the run was in |
| `hold-code` | one member of the effective code set |
| `hold-until` | the condition, verbatim after validation |
| `hold-reason` | free text, stored and printed as a quotation only |
| `held-at` | UTC, ISO-8601 with a trailing `Z` |
| `hold-unpushed` | HEAD's sha, only where the exception above fired; absent otherwise |

and one history-class parked row, `hold · item <code> · reason until <cond> · reaped <id>`, or
`· unreachable <node>`. `--status` counts it as noted rather than owed.

## 6. The checkpoint

`--status` DERIVES the checkpoint from those facts on every read. It is never stored: a stored copy
would sit in the generated region, which the `records-current` Definition-of-Done item requires
empty, so it would block the close it exists to lead to.

```
held · code <c> · until <cond> · since <iso> · from <phase>
checkpoint · witness <sha8> · next <unit> · last bar <path> · parked <n>[ · unpushed <sha8>]
reason · "<hold-reason>"
```

**Every gate claim in it is a POINTER at a run record.** `last bar` is a PATH and never a verdict
word. The reason sits on its own line, quoted, and is never parsed — a prose reason on a checkpoint
once stated a gate verdict and a reader took it for one.

## 7. The lease

One file per slug, under the git COMMON dir so every worktree on the node reads the same one:

```
taken <iso> keepalive <id> host <hostname>
refreshed <iso>
```

or a single `released <iso> held|landed` line. It is deliberately NOT in the tree: it is per-node
runtime state, it must be writable while the tree is clean, and a tracked lease would make taking
one a commit.

**The identity is the keepalive id**, because the scheduler store is SESSION-scoped: a session can
list its own jobs and no other session's, so a resume passing an id its own scheduler lists IS the
session that holds the lease. It prevents an accidental second driver, not a malicious one.

ABSENT is a third state and not a synonym for released. On a working phase it means the run predates
the lease, or its holder never took one.

**The staleness bound** is the larger of `GATE_BOUND` and `LEASE_STALE_AFTER`. The first term exists
because a live bar holds a session silent for the whole bar, and a bound under it would hand the slug
away mid-gate. A clock that cannot answer reports the age as UNKNOWN and the lease is read as FRESH,
which declines the take-over rather than inviting one.

Taken by `--preflight`, by a take-over, and by a leaseless record's own holder resuming with the
keepalive the record names. Refreshed by every writing verb past its own write gate, by a bounded
command run under a lease this verb's own keepalive holds, and by a `--resume` passing the lease's
own id. Released by `--hold`; removed at a terminal.

A refresh is a WRITE and obeys the rule every other write obeys: it happens only when the lease reads
`taken` naming the keepalive the CALLING verb acts for. A released, absent or foreign lease is never
written by a bounded command, so a refused preflight cannot renew a lease it does not hold — which
would lock that lease's own holder out for the whole bound.

## 8. The resume matrix

`--resume` is two verbs in one, orientation and take-over, and the lease is what separates them.

| Record | Lease | `--resume` |
|---|---|---|
| HELD | released, stale or absent | take-over; with no `--keepalive-id`, prints the `--status` block, then refuses, numbered, and writes nothing |
| HELD | fresh and taken | refuses, numbered: another session already resumed it |
| working | fresh, taker equals the `--keepalive-id` passed | orientation; refreshes the lease |
| working | fresh, a different `--keepalive-id` passed | refuses, numbered — unless `--replaces <old>` names the lease's id, which records the new id in the lease and the `keepalive` fact |
| working | fresh, no id passed | prints the `--status` block, then refuses, numbered; writes nothing |
| working | stale | `presumed-stopped`: take-over, refusing a missing id as the first row does |
| working | absent, and the id passed equals the record's `keepalive` fact | orientation that TAKES the lease: the holder of a run that predates one |
| working | absent, any other id or none | `presumed-stopped` once the newest commit touching the build folder is older than the bound, and taken over; inside the bound, prints the `--status` block and refuses, naming that commit's age |
| terminal | any | unchanged: nothing to resume, and never a re-drive of the lander |

The no-id rows refuse rather than orienting, because `--resume` is the only point at which a second
session can be stopped at all. They print the `--status` block FIRST, so a session regrounding by the
build method's no-id spelling still reads its phase and witness before it is told what to pass. It
then resumes with its own keepalive id, taken from its own scheduler's listing and never from the
`LEASE` line.

`presumed-stopped` is ANNOUNCED, never a refusal.

## 9. The take-over

In order, and the order is the correctness rather than the tidiness — every refusal runs BEFORE the
lease is taken, so a refused take-over writes nothing at all:

1. the condition test, on a HELD record;
2. a missing `--keepalive-id` refuses, numbered, after the `--status` block;
3. the authorization is re-verified at the pinned BASE, through the same pair `--close` uses, so the
   two verbs cannot disagree about which base authorizes this run;
4. interrupted acts are NAMED — a non-empty index, the newest gate window with no verdict, a
   turnstile ticket whose pid is dead — and never repaired;
5. the lease is taken, naming the new id;
6. the run's own orphaned processes are reaped;
7. the new id is recorded in the `keepalive` fact;
8. a HELD record returns to its `held-from` phase.

**The reap ordering, which used to live in the protocol's keepalive section.** A resumed session did
not schedule the job the run-state file names and cannot assume it died with the process that did.
So a take-over REAPS that recorded id first, reads the result back and reports it, and only THEN
schedules a replacement: the reverse leaves the run holding two jobs and a record naming neither
correctly. What changed is the sentence that followed it — `--keepalive-id` was once accepted by
`--preflight` alone, so the new id could not be recorded and the `keepalive` fact kept naming the old
job. A take-over now records the new id, and a holder replacing its own job records it with
`--replaces`.

If that `--resume` refuses or prints `still held`, the session reaps only the job it just scheduled,
reads the result back, and stops. It removes nothing else — a durable restart filed under the slug's
name is deleted only after a take-over's `--resume` SUCCEEDS, or a manual resume before an `after`
hold's instant would delete the one thing left to restart the run.

A cross-node take-over cannot reap a job in another node's session, so `--hold` accepts
`--keepalive-unreachable <node>` and records it.
