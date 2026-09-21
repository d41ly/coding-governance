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
returns the run to. A `LANDING` record the remote carries reads `LANDED` without either, and the next
`--preflight` of its slug writes that before it retires the record (§12).

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
6. An optional `--pending-run <runId>` must be 1 to 64 letters, digits, `_` and `-`. It becomes a fact
   and a checkpoint line, and a separator or a newline inside it would forge a second of either.

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
| `resume-owed` | `<name> · fire <UTC instant>`, or `none · off`, `none · owner`, `none · limit`, `none · no carrier` |
| `hold-streak` | `<n> · at <sha8>` — consecutive holds between which nothing but this run's own records changed |
| `hold-run` | the Workflow runId `--pending-run` named — the review a second `deferred-platform` held on — or EMPTY, rewritten by every hold so none inherits an earlier stop's run |

and one history-class parked row, `hold · item <code> · reason until <cond> · reaped <id> · resume <name>`,
or `· unreachable <node>` in place of the reaped field and `none(<why>)` in place of the name.
`--status` counts it as noted rather than owed. A take-over writes its own history-class row,
`resume · item <slug> · reason held|working · keepalive <id> · scheduled|manual`, so a restart a durable
task issued can be told from one a person typed.

## 6. The checkpoint

`--status` DERIVES the checkpoint from those facts on every read. It is never stored: a stored copy
would sit in the generated region, which the `records-current` Definition-of-Done item requires
empty, so it would block the close it exists to lead to.

```
held · code <c> · until <cond> · since <iso> · from <phase>
checkpoint · witness <sha8> · next <unit> · last bar <path> · parked <n>[ · unpushed <sha8>]
resume · <resume-owed> · streak <n · at sha8>
pending run <runId>
reason · "<hold-reason>"
```

The `pending run` line is printed only while `hold-run` is set, and only on a HELD record.

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
own id. Released by `--hold`, and by an `in-place` `--landed` that observed the landing, as
`released <iso> landed` (§12); removed at a terminal the driver writes.

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
| LANDING | `released … landed` | nothing to resume and never the lander: `--landed` observed it on the remote, and the rotation waits for the advertised tip. Never `presumed-stopped` |
| terminal, recorded or derived | any | unchanged: nothing to resume, and never a re-drive of the lander |

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
8. a HELD record returns to its `held-from` phase, and one carrying `hold-run` prints the relaunch of
   that deferred review FIRST: re-run it with identical args, which reuses every lens and skeptic
   file it wrote and dispatches only what did not return.

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

## 10. The in-place landing, and the one that cannot complete

*Protocol section 6 states the ordered `in-place` sequence in four verbs. This section carries what
that order is FOR, what a reconcile may not go through, and what a run does when the landing cannot
be completed at all. It is here rather than there because the protocol is at its cap and this is the
half a run reads only when something stops.*

**Why the order is forced, and not merely recommended.** The merge bar writes its full-green stamp
only for a clean, unmoved run, and the push boundary reuses that stamp instead of paying a second
full bar. So the bar has to run on the PREPARED MERGE and before `--close` writes a byte: grade the
branch tip instead and the only grader of the merge is the push boundary's scoped bar, which is
scoped by a guard — two green changes that fail together then surface after the run has closed.
That is the shape of two aborts this kit already records.

**A reconcile comes from the REMOTE's default branch, onto the run branch.** Never through the
node's own default branch: that is a ref this session can move, and it carries whatever else on this
node has not been pushed. When `--prepare` reports a conflict, merge the remote's default branch
into the run branch, resolve, commit, and `--prepare` again.

**A landing that cannot COMPLETE merges nowhere.** The lander reporting the remote unreachable, its
race retries exhausted, or a `--close` refused because the lander could not make its observation are
all the same case: nothing is merged, anywhere. The run pushes its branch, so the prepared merge and
the committed close survive the session, and then holds under `--code platform-unavailable` with the
lander's own last line as the reason and `--reaped` naming the keepalive the close's attestation
already reaped. When the branch push fails too, because the remote answers nothing at all, the same
hold is taken over the unpublished tip — which is exactly the exception section 4 states, and the
only code it is stated for.

A RED bar at the push is a different thing and takes a different route. A red the run itself caused
is the run's work: fix it and `--prepare` again. It holds under this code only when the red is the
declared bound firing, which is a cause outside the run in the way every other hold code is.

**Why the `LANDED` anchor ORDER is a rule.** Listing two anchors without ordering them would permit
an implementation that always takes the cheaper one, retiring the observation while satisfying every
word of that section. The ordering is what preserves the strong claim wherever the strong claim is
available.

## 11. The durable restart a hold owes

*A run that ends HELD used to resume only when somebody typed `--resume`, so a usage limit that
resets at 03:00 cost the whole night. This section is the contract for the restart `--hold` files
instead. The protocol's section 5 points here and states none of it.*

### The five keys

| Key | Meaning |
|---|---|
| `RESUME_SCHEDULE` | `on` or `off`. Absent or blank is `on`, announced as defaulted; any other value is a numbered refusal at conf load |
| `RESUME_SCHEDULE_CREATE` | the DURABLE scheduler's create tool, named for the AGENT to call. REQUIRED while the switch is on |
| `RESUME_SCHEDULE_DELETE` | its delete tool, on the same terms |
| `RESUME_SCHEDULE_DELAY` | seconds: how long after a `probe` hold its restart fires. OPTIONAL, and the kit default is ANNOUNCED on stderr by the run that takes it rather than written here; not a positive integer is a refusal |
| `RESUME_SCHEDULE_LIMIT` | holds: how many consecutive holds with no progress a run may take before it stops owing restarts. Same terms, same announcement |

**The carrier may not be the keepalive's.** A `RESUME_SCHEDULE_CREATE` equal to `KEEPALIVE_CREATE` is
a numbered refusal in the kit gate: that store is session-scoped by its own contract, so a restart
filed there dies with the session it exists to outlive. The carrier must be DURABLE — a filed task
outlives the session that filed it — and must accept a caller-chosen name.

### The fire rule

| Condition | Owed | Fire instant |
|---|---|---|
| `after <instant>` | yes | the instant, or `held-at` plus 60 s when it has already passed |
| `probe host`, `probe gate`, `probe api` | yes | `held-at` plus `RESUME_SCHEDULE_DELAY` |
| `owner` | no | — |

An `after` hold fires AT ITS INSTANT and never at `held-at` plus the delay: a usage limit that
resets at a named time restarts into the same limit otherwise. Each schedule is ONE-SHOT. A `probe`
resume whose probe fails holds again, and that hold owes a new one-shot; there is no recurring task
to outlive the run, and the chain ends at the streak limit.

### The name, and the no-progress bound

The name is `unattended-resume-` followed by the slug in LOWER CASE. It is DERIVED and recorded
nowhere, so any session holding only the slug can reap it and no write on a HELD record is needed to
remember a carrier id. Lower case, because a carrier that sanitises names to kebab case would
otherwise store a name a later delete does not match; two slugs differing only in case therefore map
to one name, which is the stated cost of the choice.

`hold-streak` counts consecutive holds between which no path changed other than the run's own
records: the run-state file, and the build folder's `BACKLOG.md`, where the asks, SEV rows and KEEP
rows filed ABOUT a stop are recorded and committed before `--hold`. A hold after any other path
changed resets the count to 1. The hold and resume writes move HEAD, and the stop's own ask filing
changes that `BACKLOG.md`, and neither is progress — a bare HEAD comparison would reset on the
hold's own commit and the limit would never bind. It carries its OWN sha because `witness` is
rewritten by every later phase write and so cannot say where the previous hold stood. At
`RESUME_SCHEDULE_LIMIT` the hold still SUCCEEDS and `resume-owed` reads `none · limit`, so a run
that cannot move stops spawning sessions.

**`--hold` never refuses for a missing carrier.** The hold is the safe state, and refusing it would
push the run back toward the ABORTED ending HELD exists to replace. It records `none · no carrier`
and says so, and the kit gate and the adopter check red the missing declaration instead.

### What `--hold` prints, and what the agent files

`--hold` prints the schedule name, the fire instant in UTC, and a three-line prompt, and the agent
files that prompt VERBATIM. Every interpolated value has a validated shape: the slug passed the
driver's own slug check, the toplevel came from `git rev-parse --show-toplevel`, and `held-at`
matched the hold's timestamp grammar. **The hold REASON never reaches the prompt** — it is free text,
and a durable prompt executes later in a session nobody watches.

The prompt's `--keepalive-id` is fixed prompt text, not an interpolated value: the scheduled session
fills it with the keepalive its own scheduler created, because the take-over refuses a missing id.

The prompt's last line reaps that keepalive whenever the resume refuses or prints `still held`,
because nothing else would: a keepalive left firing ticks `--resume <slug> --keepalive-id <own id>`
as its first act, and on a HELD record that call takes the take-over row with NO `--scheduled`, past
the four refusals below. The same line LEAVES THE NAMED TASK IN PLACE. A session refused because a
later hold began would otherwise delete, under the one name every hold of the slug shares, the
restart that later hold filed.

Every hold of a slug files under that one name, so the hold step DELETES the name before it files,
going on when no task has it: a fired one-shot can stay listed, disabled, under its id. The delete
loses nothing a hold owes, because `--hold` refuses on a HELD record, so a task under the name
belongs to a hold that has already ended — and refusal 2 below catches it on `held-at`.

### `--resume <slug> --scheduled <held-at>`

The only restart a schedule issues. Four refusals, in order, before the take-over writes anything:

| # | Refuses when | Why |
|---|---|---|
| 1 | the record is not HELD | a working phase belongs to the resume matrix, which refuses a session that cannot show the lease's keepalive, and a schedule is filed only for a hold |
| 2 | `held-at` differs from `--scheduled` | the hold this task was filed for has ended and a later one began |
| 3 | the remote-advertised run-branch tip is neither HEAD nor an ancestor of it, under `ANCHOR_SCOPE=published` | another session pushed work after the hold; a pushed hold commit of this worktree's own is an ancestor and passes |
| 4 | the remote does not answer | freshness cannot be shown, and a restart that might double-drive is worse than one that waits for a human |

Rule 3 reuses the bounded `ls-remote` the driver already runs at preflight. Under another anchor
scope `--hold` does not require the push, so rule 3 is SKIPPED with an announcement rather than
faked. On success the take-over runs unchanged, and it still requires the session's own
`--keepalive-id`.

**The cross-node window is open and is stated rather than closed.** A take-over on another node that
has not pushed its record yet is invisible to rule 3, so for that window two nodes can drive one
slug. The Skill's take-over step pushes the record FIRST to shrink it.

### The Skill's half, and the close

Filing and reaping are AGENT obligations, exactly as the keepalive's are: no script reaches a
harness scheduler store. The hold step deletes the printed name and then files the printed schedule
under it. The Resume section deletes that name only AFTER a take-over's `--resume` succeeds and its
record is pushed — never before that `--resume`, and never when it refuses or prints `still held`,
scheduled or manual, because a manual resume before an `after` hold's instant would otherwise leave
the run HELD with the one thing that could restart it deleted.

`--close` and `--abort` name every schedule the record's hold history owed, beside the keepalive id,
so the `keepalive-reaped` attestation is made over a list the agent was SHOWN. There is no new
Definition-of-Done item: a durable task outliving the run under a green attestation is the failure
that item already exists to catch.

## 12. The derived terminal

*Protocol section 6 states it in one sentence citing owner ruling D12-i2. This is the rest.*

**A `LANDING` record whose own commit is on the tip the remote advertises is landed.** Four gaps
made a written `LANDED` unreliable: a kill after the push and before the lander's marker, a marker
naming the `--no-ff` merge rather than the witness, a marker another landing overwrote, and a
`LANDED` commit written after the push, which no bar ever grades. Deriving closes all four.

**The landing commit is found by CONTENT.** The record must be byte-identical to HEAD's copy, and
that copy must read `LANDING`; the commit that last changed it is the landing commit. Not by the
close commit's subject, which only one mode fixes, and never by walking the path's history back to
an older `LANDING`: the path is reused after a rotation, and that walk would find an EARLIER run's
landing on the remote and call a staged, unpushed record landed.

**Who derives, and who reads the recorded phase.** `--status`, the terminal guard of every writing
verb, `--resume`, `--audit` and `--preflight`'s rotation test derive; so do the gate leg's check 7
exclusion, its fact-set arm and its cross-run grant arm. The committed live index does NOT: it is
freshness-gated, and the remote tip moves while the index does not. `--landed`'s own guard reads the
RECORDED phase, because its postcondition is the terminal. The remote is observed only for a
`LANDING` record, quietly; an unanswered remote, or a tip this clone lacks, leaves `LANDING` and
`--status` prints the reason.

**Under `in-place`, `--landed` is an OBSERVATION.** It writes nothing to the tree, prints the
derivation, and keeps what it saw in the lease, `released <iso> landed`, so a later reader that
cannot see the remote still does not presume the run stopped. It refuses, numbered, when no
`LANDING` record is committed, when the landing commit reached only the LOCAL default branch, and
when the push has not carried it. Under `primary` it writes `LANDED` as before, and its lander
marker check is ANCESTRY: the marker's commit is on the advertised tip, and the witness is that
commit or an ancestor of it.

**The facts move to the close.** Under `in-place`, `--close` writes `units-at-landing`, and
`asks-at-landing` wherever the ask contract applies, beside `LANDING` in the record it commits; a
witness that cannot answer refuses before any write.

**The next `--preflight` retires a derived-`LANDED` record, WRITTEN `LANDED` first.** It edits a
scratch copy under the git dir to `phase: LANDED`, `witness: <landing commit>` and
`landed-derived: <landing commit> <advertised tip>`, derives the archive name from that copy,
and refuses, numbered and with nothing moved, when the copy lacks a fact the leg's fact-set arm
requires. After the write gate it puts the copy in place, STAGES it and checks the index blob is the
one the name encodes — `git mv` carries the staged blob, so an unstaged edit would ride the move as
the old bytes — and only then moves it. Check 15 reads `landed-derived` as that record's anchor
evidence and tests the commit it names against the advertised tip.

**The fact-set arm, graded by `LANDER_MODE` from `LANDED_FACTS_CUTOFF`.** A recorded `LANDED` that
`--landed` wrote carries `landed-anchor`, `units-at-landing` and `unpushed-at-landing`; a rotated
derived one carries `units-at-landing` and `landed-derived`; under `in-place` a committed `LANDING`
carries `units-at-landing`. Under `primary`, a committed `LANDING` the remote already carries is
REPORTED naming `--landed` and never graded, since that is the verb that completes it. Each record is
dated by its FIRST commit read with `--follow`, floored at a rotated folder's newest archive, so a
rotation does not re-date it. Blank turns the arm off, announced.
