<!-- gov:kit unattended@1.91 -->
# The unattended stop contract — HELD, the hold codes and the lease

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
  test, an authorization to re-verify and a lease to take. The one exception is a hand-off its owner
  landed: it derives `LANDED (attended)` (§12), so `--preflight` retires it rather than refusing.

`--landed`, `--abort` and `--settle` write a terminal. The first two go through the working phase a
resume returns the run to; `--settle` writes one only over a hand-off its owner landed (§12). A
`LANDING` record the remote carries reads `LANDED` without any of them, and the next `--preflight` of
its slug writes that before it retires the record (§12).

## 2. The codes

Kit-owned core, extended by `HOLD_CODES_EXTRA` and pinned shrink-only by `HOLD_FLOOR`:

`host-degraded` · `platform-limit` · `platform-unavailable` · `host-owner-action` · `inherited-red` ·
`owner-landing` · `owner-decision`

These are a SECOND vocabulary beside the halt codes and never an extension of them. A halt code ends
a run and a hold code pauses one, and a single list would let a pause be recorded as an ending.

**`owner-landing` and `owner-decision` are the HAND-OFF codes, and `--handoff` is their only
producer.** A run whose work is sound and which an owner must land, or decide first, ends HELD under
one of them rather than `ABORTED`, which from `HANDOFF_CUTOFF` means DISCARD. `owner-landing` says
only the landing remains; `owner-decision` says a parked decision stands first. `--handoff` writes
the landing recipe as a `handoff` row in the parked region, `units-at-landing`, and
`asks-at-landing` wherever the freeze is non-empty, and prints the recipe after its HELD line. A
`--hold` naming either code is refused, because a hold written without the guard, the recipe and the
facts is a hand-off nothing can land or settle.

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
   store it cannot see; it can only record that somebody did. `--reaped` must name the record's
   `keepalive` fact, which a holder that replaced its own job re-recorded.
4. The tree must be clean and committed.
5. Under `ANCHOR_SCOPE=published`, the branch tip must be on its remote. Under `local` no push is
   owed, so a hold parks work that may exist on this node only, and `--scheduled` says so.
6. An optional `--pending-run <runId>` must be 1 to 64 letters, digits, `_` and `-`. It becomes a fact
   and a checkpoint line, and a separator or a newline inside it would forge a second of either.
7. The code may not be a hand-off code; `--handoff` writes those.

`--handoff` routes through these same refusals with the condition fixed at `owner`, and adds three
of its own, each before any write:

- **The attribution guard, on `owner-landing`.** The bar the record's `gates-run` fact names must
  read GREEN, on a clean tree that did not move, at HEAD or at a commit differing from HEAD in the
  run-state file alone; otherwise every red leg must read INHERITED, the refusal an override of
  `gates-green` meets at `--close`. An OWN red is the run's to fix, or to hand off as
  `owner-decision`.
- **A parked decision, under `owner-decision`.** The row is the question the owner is handed.
- **The landing facts and the recipe.** A freeze that cannot be derived refuses, and so does a
  recipe naming no lander or no branch.

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

The lease is the run-state facts `write_lease` writes together, `keepalive`, `session`, `pid`,
`host`, `pid-image` and `lease-utc`, and `prior-session`, a set the holder row writes beside them
when its claim push does not land. `lease-utc` says a record carries one: a
record without it predates the run-state lease and is graded by the newest commit touching its build
folder. The holder is the `keepalive` fact; freshness is `--liveness`'s clock against
`RESUME_STALE_BOUND`; `HELD` is the released lease. A leftover lease file is never read.

**The identity is the keepalive id**, because the scheduler store is SESSION-scoped: a session can
list its own jobs and no other session's, so a resume passing an id its own scheduler lists IS the
session that holds the lease. It prevents an accidental second driver, not a malicious one.

**Nothing refreshes it**: a refresh in the tracked record would restage it every tick and move
`lease-utc`, which `--landed` grades stop lines against. A clock that cannot answer reads UNKNOWN,
announced, and declines the take-over.

**The claim on the remote** is where two NODES learn of each other, which the lease cannot do
because it lives on the run's own branch. Where `RUN_CLAIMS` is `on` (absent or blank is `off`), the
ref `refs/gov/runs/<slug>` on the remote the landing push goes to names a parentless commit over the
empty tree whose message is `gov-claim <slug>`, a blank line, and eight `key: value` lines: `slug`,
`node`, `host`, `session`, `keepalive`, `status` (`live`, `held`, `landed` or `aborted`),
`lease-utc` and `beat-utc`. Every write is a compare-and-swap, `--force-with-lease` on the sha the
same call read, empty for a create, and leaves the ref in place; a terminal claim is taken over by
the slug's next run and never deleted. `--claims` lists every claim. The beat renewing it is a
remote fact and never restages the record, so nothing above changes. It stops an accidental second
driver, as the lease does; a run holding the push credential can force or delete the ref.

| claim | verdict |
|---|---|
| `live`, beat at most `RESUME_STALE_BOUND` old | `live` |
| `live`, beat older | `stale` |
| `held`, any age | `held` |
| `landed` or `aborted` | `terminal` |
| a key missing, a slug other than the ref's, a status outside the set, a beat that does not parse | `unknown`, age `-` |

A claim is `mine` when its `keepalive` AND `session` equal the run's lease (`absent` compares
literally); `same session` when its `session` is this harness's session; `foreign` otherwise, read
by its verdict. The rows are tested in that order. A holder or status write also reads `mine` a
claim of the lease's `keepalive` whose `session` is ANY member of the record's `prior-session`, and
the restart row's take-over reads such a claim `same session`. That fact is a SET: members separated
by one space, `absent` a member like any other, and the empty value or a missing line the empty set.

| claim read | `--preflight` | take-over | holder | status write |
|---|---|---|---|---|
| none | create | create | create | create |
| mine | renew | renew | renew when due | write |
| same session | rewrite | take | take | write |
| foreign `live` | check 107 | check 107 | check 108 | announce |
| foreign `held` | check 107 | take | check 108 | announce |
| foreign `stale` | take, announced | take, announced | check 108 | write |
| foreign `terminal` | take | check 107 | check 108 | write |
| `unknown` | check 107 | check 107 | check 108 | announce |

The holder is `--resume`'s holder row and its `--replaces` block, `--dispatch` and `--close`; it
renews when the beat is a quarter of the bound old or a field it writes differs, and otherwise only
reads, so a lost claim is found on every call. A race lost between the read and the push is check
108; a push refused for any other reason, or not answered, is check 109 at `--preflight`, at a
take-over and at `--close`, and one announced line at the holder's `--resume` and `--dispatch`, which
work offline. The holder row whose `write_lease` is due pushes first, under the values and the one
stamp `write_lease` then records, so a lost race leaves the record untouched; a push that does not
land, or a claim it could not read, ADDS to `prior-session` the record's session from before the
call and the read claim's session, each once. That row is the set's one writer: the next claim
write of that row that lands empties it, writing the empty value only when the set is non-empty, and
a landed `--beat`, `--dispatch` or status write leaves it as it is. A holder refused at check 108
ends with `--abort <slug> --code claim-lost`. The status
writes are `--hold` (`held`), `--landed` (`landed`), `--abort` (`aborted`), `--settle` (`landed`
over a landed hand-off, `aborted` over an abandoned working record, and none over a legacy
`ABORTED` one) and the landing re-bind (`live`, its new keepalive), each after its own staging
and never failing its verb. A `--settle` re-run over a record it already settled rewrites no record
and retries that status write, only over a claim of the record's own lease still `held` or `live`,
so a first write that did not complete is retried by running the verb again. The resume tick
renews a `LIVE` run's claim through `--beat`, which writes only the none and `mine` rows.

## 8. The resume matrix

`--resume` is orientation or take-over, and the lease separates them. Rows apply in order, after the
`--scheduled` refusals (§11). "Working" is any non-terminal phase but HELD; "no lease" lacks
`lease-utc`.

| Record | Caller and clock | `--resume` |
|---|---|---|
| carrying `abandoned` | any, ahead of the `--scheduled` refusals | refuses 106, writing nothing, naming `--preflight`, which retires the record to its archive and starts the next run on a fresh one under the id it is handed |
| recorded terminal | any | nothing to resume; with an id, check 26 |
| HELD under a hand-off code, derived `LANDED (attended)` | any | nothing to resume, naming `--settle`; writes nothing, never the take-over or the re-bind |
| LANDING derived LANDED, not observed | an id, on a branch where that landing's `--landed` does not run, the record naming a branch fact | nothing to resume, naming the record's run branch; writes nothing |
| LANDING derived LANDED, not observed | an id | RE-BIND: `write_lease`, staged, never committed, whatever the clock or session; a record naming neither branch fact re-binds anywhere, announced as not scoped |
| LANDING derived LANDED, not observed | no id | nothing to resume |
| LANDING, observed in the landed log | any | nothing to resume, never the lander, never `presumed-stopped` |
| any other carrying lease-utc | from a worktree not on the run's branch | refuses, numbered, naming the branch and its worktree; writes nothing |
| HELD, condition unmet | any | `still held`, writes nothing |
| HELD, `lease-utc` after `held-at`, clock fresh, another session and keepalive | an id | refuses 58: a take-over recorded its lease and has not moved the phase |
| HELD, otherwise | an id, or none | take-over; no id, the status block then check 59 |
| working | the recorded keepalive | the holder: writes nothing to the record unless it lacks `lease-utc` or names another session or pid than the harness exposes, then records and stages; with `RUN_CLAIMS` on, first reads its claim (§7), renewing it when due and refusing at check 108 one another session holds; reaps orphans (§14) |
| working, clock fresh or unknown | a new id with `--replaces` the recorded keepalive | the holder replaces its job: `write_lease`, staged; another `--replaces` id refuses 58 |
| working | a new id, the recorded session (not `absent`), under a pid the record does not name | the holder's process restarted: take-over; refuses 58 first if the recorded pid lives |
| working, no lease, age unanswerable | a new id, or none | the status block, then check 57 |
| working, no lease, inside the bound | a new id, `--replaces` the recorded keepalive | the holder replaces its job, through the `--replaces` block of the leased row above |
| working, no lease, inside the bound | any other new id, or none | the status block, then check 59 naming the folder's age and `--replaces` with the recorded keepalive |
| working, no lease, past the bound | an id, or none | `presumed-stopped`, announced: take-over |
| working, clock fresh or unknown | a new id | refuses 58: a live session drives this slug |
| working, clock fresh or unknown | no id | the status block, then check 59 |
| working, clock stale | an id, or none | `presumed-stopped`, announced: take-over; no id, the status block then check 59 |

The no-id rows print the `--status` block FIRST, so any caller that spells `--resume` without an id
reads its phase and witness before it is told to pass the keepalive id its own scheduler lists.
`--status` carries the verdicts those rows reach first, the holder worktree of check 58 and the
pinned `asks:` line of check 73, as fields on its one line, pass included, so a session regrounding
with `--status` loses neither. The re-bind stays uncommitted, since a commit would move HEAD off the
pushed tip: a difference confined to the seven lease-fact lines reads as none to the landing commit
and to `--landed`'s `primary` clean check, and to no other clean check. `presumed-stopped` is
ANNOUNCED, never a refusal. The run's branch is `run-branch`, else `branch-ref`, and git checks a
branch out in one worktree at most; a record naming neither is graded where it is read.

## 9. The take-over

In order, and the order is the correctness rather than the tidiness — every refusal runs BEFORE the
lease is taken, so a refused take-over writes nothing at all:

1. the condition test, on a HELD record;
2. a missing `--keepalive-id` refuses, numbered, after the `--status` block;
3. the authorization is re-verified at the pinned BASE, through the same pair `--close` uses, so the
   two verbs cannot disagree about which base authorizes this run;
4. interrupted acts are NAMED — a non-empty index, the newest gate window with no verdict, a
   turnstile ticket whose pid is dead — and never repaired;
5. the run's own orphaned processes are reaped (§14);
6. the lease facts are recorded, the new id in the `keepalive` fact;
7. the history row is written;
8. a HELD record returns to its `held-from` phase, and one carrying `hold-run` prints the relaunch of
   that deferred review FIRST: re-run it with identical args, which reuses every lens and skeptic
   file it wrote and dispatches only what did not return. The files exist only where the review ran
   under `workerType: 'none'`, as the build harness's spec audit does; a review under a named type,
   the default of a direct call, wrote none and its re-run dispatches every judge again. A hold can
   name any deferred review, the closing diff review included.

**The reap ordering, which used to live in the protocol's keepalive section.** A resumed session did
not schedule the job the run-state file names and cannot assume it died with the process that did.
So a take-over REAPS that recorded id first, reads the result back and reports it, and only THEN
schedules a replacement: the reverse leaves the run holding two jobs and a record naming neither
correctly. A take-over records the new id, and a holder replacing its own job records it with
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
be completed at all.*

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

A hand-off owes no durable restart. `--handoff` holds with the condition `owner`, so its
`resume-owed` reads `none · owner` and nothing is filed: the way out is the owner's landing or
decision, never a scheduled resume.

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
`LANDING` record or a HELD one under a hand-off code, quietly; an unanswered remote, or a tip this
clone lacks, leaves the recorded phase and `--status` prints the reason for a `LANDING`.

**A hand-off its owner landed reads `LANDED (attended)`.** A HELD record under `owner-landing` or
`owner-decision` whose own commit — found by the same content rule, HEAD's copy reading HELD under a
hand-off code — is on the advertised tip derives `LANDED` everywhere a reader derives, and `--status`
prints `LANDED (attended)`. The hand-off commit is the run's last act on its branch, so a landing that
carries it carries the work. A HELD record under any other code never derives and never observes the
remote: a paused run whose branch somebody merged was not handed off, and a terminal derived under a
live lease would end it through check 26. `--liveness` takes no network: it tests the same commit
against the ref its `finished-unstamped` test resolves, and reads `terminal`. `--resume` writes
nothing and names `--settle`; `--preflight` retires it, its copy gaining `landed-by: attended`.

**`--settle <slug>` writes what git proves.** Over a landed hand-off it writes `phase: LANDED`, the
landing commit as `witness`, `landed-derived` and `landed-by: attended`. Over an `ABORTED` record
first committed before `HANDOFF_CUTOFF` — a blank cutoff refuses every one — it writes one fact,
`work-landed-at: <witness> <tip>`, the only write a terminal record admits. Over a working record
whose `--liveness` verdict is `STALE` or `UNBOUND` it writes `work-landed-at` and `abandoned: <utc>`
under the current phase; `--preflight`'s announcement and the leg's check 7 report exclude a record
carrying `abandoned`, `--resume` refuses it (§8), and the next `--preflight` retires it to
`RUN.<phase>.<blob8>.md`, so the settle evidence is archived and the next run starts fresh. It refuses, numbered and before any write, a HELD record under another code, a
`LANDING` or `LANDED` record, a record differing from HEAD's copy beyond its lease lines, a live
lease, an unanswered remote and an undecidable predicate; it STAGES the record and never commits,
so the settle commit rides the next landing from that tree or a batched owner pass. A live `RUN.md`
only: an archived record is immutable.

**Where an `ABORTED` run's work went is decided by CONTENT, never by witness ancestry.** `--abort`
commits the record on top of its witness, so every record read from the tip has its witness there.
Landed is all three: the witness is not an ancestor of the record's `base` and `base..witness` holds a
commit naming the slug in its subject or touching its build folder; every such commit is on the tip;
and no commit on the tip's first-parent line since the witness carries `This reverts commit` naming
one, or naming a merge that brought one onto the tip. A missing or unresolvable `base` is
undecidable. `--settle` and check 15 ask the one library predicate. Check 15 grades `work-landed-at`
at the tip it records: it reds one that does not name the witness, whose tip is not on the advertised
tip, or whose work the predicate does not read landed there, and REPORTS a later revert, since no verb
rewrites the record, and a tip whose line it cannot read as not re-judged, never as a revert. It reds one on an `ABORTED` record not predating `HANDOFF_CUTOFF`, and an
`abandoned` standing without it.

**Under `in-place`, `--landed` is an OBSERVATION.** It writes nothing to the tree, prints the
derivation, and logs it, per landing commit, to `landed.<slug>.log` under the git common dir, so no
reader in any worktree presumes the run stopped. It reads the keepalive reap back first. It refuses, numbered, when no
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
derived one carries `units-at-landing` and `landed-derived`; an `attended` one, carrying
`landed-by: attended`, carries those and `landed-by`; under `in-place` a committed `LANDING`
carries `units-at-landing`. Under `primary`, a committed `LANDING` the remote already carries is
REPORTED naming `--landed` and never graded, since that is the verb that completes it. Each record is
dated by its FIRST commit read with `--follow`, floored at a rotated folder's newest archive, so a
rotation does not re-date it. Blank turns the arm off, announced.

## 13. The inherited red — land, park, or absorb

*`TOOL-dDerivedDocket-24`, by owner rulings D12-i4 and D12-i5; the age as an escalation and the kit
default `land` by ruling `TOOL-dUnstuckLanding-22`, which supersedes that part of D12-i4. The hold
code is §2's.*

**The bar says whose a red is, and a policy says what happens next.** `gates-green` attributes a
red against R, the tip `observe_anchor` saw the remote advertise, and ages each INHERITED leg against
R's last `INHERITED_RED_MAX_AGE` first-parent landings: red with the same offenders at the far end
is `aged`, and otherwise a bisection names the landing that introduced it. A probe that cannot
answer reads `age unproven` and is never escalated: a leg with no `signature` whose far end is red
WITHOUT every non-blank line of this run's output is one, since text cannot tell a fixed offender
from a moved count line; red carrying all of them is `aged`. **The age decides the escalation, never
the landing.** The policy is the pair of keys in the file `GATE_POLICY_FILE` names, both read at R
and parsed, never sourced. A blank `GATE_POLICY_FILE`, or a conf absent at R, reads the file the
pre-push hook reads, `.githooks/gate-env.sh` at R, so the two readers cannot disagree. The kit
default is `land`: that file absent too, a named policy file absent at R, and an absent or blank
`INHERITED_RED` all read it, and `land` with no positive bound reads `land` with no bound. A value
outside `park land` reads `park`. The item announces which.

- **`land`, every red INHERITED at any age, on a bar whose verdict reads `tree_moved no`:** MET, and
  the record gains `gates-inherited: <R8> <legs>`; the MET line names the legs read `aged`. The
  pre-push hook reads the same policy at the same R and lands the push, printing the legs. An
  attended push lands over it too.
- **`park`, declared:** UNMET, printing
  `hold · inherited-red · until probe gate · <legs> red at <R8>, INHERITED; INHERITED_RED=<policy>`.
  Take that hold in this order: commit the staged records, push the branch, reap the keepalive, then
  `--hold` with that code, condition and reason and `--reaped`. It refuses a dirty tree otherwise.
- **Any leg OWN, MIXED, DEAD PROBE or CONTENDED, or a moved tree:** UNMET with the attribution
  lines. That red is the run's, and so is every red on a bar whose diff edited its own grader (KF3).

**Every inherited leg gets an owner on the record, and its age escalates it.** Once `ASKS_CMD` is
declared, the item files one ask per INHERITED leg in the closing build's `BACKLOG.md`: a `seen`
locator pinned at R with the leg's `run` command, an `accept` clause, a SEV HIGH row and a KEEP row,
staged and read back through `ASKS_CMD`. An `aged` leg's ask is SEV BLOCKER instead, its text
`inherited red: leg <leg> red at <R8>, older than the <n>-landing age bound`, and the memory tree's
generated LIVE index lists every OPEN BLOCKER ask under `## Open BLOCKER asks`. Rows the generator
does not read back as one OPEN ask of the SEV owed are removed and named. An OPEN ask this build
already filed for the same leg at the same R, read back at the SEV owed, is reused and named, so a
repeated close files nothing twice. With `ASKS_CMD` blank the item prints the rows it would file and
writes nothing.

**The daily held job's reds get an owner too.** After the bar returns, on every return code and
without touching the verdict, the item reads the latest completed scheduled run of the workflow
`HELD_CI_WORKFLOW` names, read from the conf at R, through the public API with no credential, and
files one ask per held suite whose job concluded `failure` or `timed_out`, in the same grammar and
through the same read-back and rollback: SEV HIGH, a KEEP row, and an `accept` clause asking for the
suite green on the daily held job. An OPEN HIGH ask for the same suite in ANY build's `BACKLOG.md`
is reused and named. A name carrying a backtick, a control character, ` · ` or ` → `, and a head sha
R does not descend from, are refused and named. Every way the read can fail is a `DEAD PROBE` line
that files nothing, and blank `HELD_CI_WORKFLOW` is DARK, announced, with no request made.

**The two escape routes are backed or refused.** `--close --override gates-green` and
`--abort --code gate-red-out-of-scope` are refused, numbered, unless the record the `gates-run` fact
names reads every red leg INHERITED, on a bar whose header shows `head` equal to HEAD and
`tree_clean yes` and whose verdict shows `tree_moved no`. The refusal names the condition that
failed, and the remedy is `gates-green` on HEAD first.

**ABSORB — the red fixed in-run.** An inherited red may be fixed beyond the declared write set when
all FOUR hold: the attribution names its owner; no M3 veto is tripped; the fix is its OWN commit,
subject `absorb(<slug>): <leg> inherited at <R8>`, naming no unit id; and the fix is recorded CLOSED
against the ask filed for that leg. KF3 still binds, so a fix that edits the grader makes every red
OWN. The gate leg's check 23 reads that subject as an ABSORB, reports the commit's paths on an
`ABSORB` line, and counts it as neither a dodged join nor an undeclared write; the same paths under a
subject that names a unit id are still the anomaly.

## 14. The process ledger — nothing is killed that this run did not start

*`TOOL-dDerivedDocket-28`. One run found an earlier bar's legs still running beside its own; another
found six abandoned processes matching this kit's commands, and five were another repository's.*

**A process not in the ledger is never killed**, whatever its command line says: it is reported, by
the process-monitor kit where one is adopted, and left to a person. The ledger is what makes a
process this run's. Every command the driver starts through its bounded runner is appended, by
identity, to `<git-common-dir>/unattended/<slug>.procs`, beside the landed log (§12):

```
<msys pid> <start token|-> <driver pid> <driver token|-> <keepalive|-> <iso-utc> <argv0> [argv1] [argv2]
```

The start token is field 22 of `/proc/<pid>/stat`, read at record time and again before any reap, so
a reused pid is told apart from the process it once named. Where procfs cannot answer, the token is
`-`, and that record is counted and never reaped.

**An orphan** is a recorded process alive with its recorded token while its recorded driver is not.
The driver waits on every command it starts, so a live driver is a live consumer; a driver pid reused
by another process reads as alive and withholds the reap, so the error direction is a process left
running, never one killed.

**Who reaps**: `--preflight` once its lease is recorded, `gates-green` before it starts a bar, `--hold`
before it moves the phase, and the two `--resume` rows that hold it — the take-over and the holder
passing the lease's own id. Every other `--resume` row only counts. Each orphan goes through
`PROCMON_CMD --kill-msys <pid>`, one at a time, and success is read back from the recorded pid,
never from the reaper's exit. One line per record acted on:

```
unattended: reaped orphan <pid> (<argv>), started <iso> by driver <pid>, now gone
unattended: NOT reaped <pid> — <exited, pid reused | no procfs token | fence refused: <why>>
```

The same pass prunes a record whose process is gone or whose pid now names another process. A fence
refusal keeps its record, so a later reap can succeed. A blank `PROCMON_CMD` turns reaping off,
announced, and the orphans are still counted. The runner's wrapper carries the repository root as an
argument, which is what lets the fence admit a tree whose parent is gone.

`--status` prints `orphans <n>` when n is positive and kills nothing. `--hold` refuses, numbered,
while any recorded process of the slug is alive after its reap, naming it: a run does not hold while
its own bar runs. At a terminal, and at an `in-place` `--landed` that observed the landing, the
ledger is removed — or KEPT, naming each live pid, while a recorded process is still alive.

**What it cannot see**: a process the agent starts in its own shell, such as a suite at `VERIFYING`.
The driver did not start it, so it is not recorded and never reaped here.

## 15. The close-decision table

*`TOOL-dUnstuckLanding-18`, by owner ruling `TOOL-dUnstuckLanding-23`, which supersedes D8 as
`build-complete` applies it. The hand-off codes are §2's.*

**At the close a park is never an abort.** A decision a run reaches at the close is recorded and
then takes the exit this table names. The rows are CLOSED: each is one decision KIND the closing-time
census found, with its exit and the record that exit writes.

| Decision kind | Exit | Record |
|---|---|---|
| land a partial build | LAND, when `build-complete`'s carry-forward term meets; otherwise HAND OFF `owner-decision` | one `rescope · item defer` row per carried unit |
| move a shrink-only pin | none owed: the kit's history legs grade only the run's own range, so they no longer ask it; a pin the run's own diff must move is HAND OFF `owner-decision` | the decision park row |
| act on another run's record | no act: concurrent runs are permitted, and a landed record derives its terminal (§12) | none |
| publish another session's commits | does not arise under `in-place`; under `primary`, HAND OFF `owner-landing` | the handoff row |
| land in a dependency order across repositories | HAND OFF `owner-landing`, the recipe naming each repository in order | the handoff row |
| land from a node `LANDING_NODES` does not declare able to land | HAND OFF `owner-landing`, after the close records the bar | the handoff row |
| choose a fix where every option touches a carrier | HAND OFF `owner-decision` | the decision park row |
| a question the default branch already answered | observe the advertised tip first, and take the exit the answer selects; unanswered, HAND OFF `owner-decision` | the park row |

**A kind this table does not list is a HAND OFF under `owner-decision`**, because the work is sound
and only a turn is missing. **ABORT is reserved for work that must not land as it stands** — the
halt codes, never a decision the owner could take in one read.

**The carry-forward term.** `build-complete`'s fifth term carries a non-terminal unit forward, and
prints one `carried forward` line naming it and its ask, only when ALL FIVE hold, checked in this
order and each unmet one named with its unit:

1. its spec status is `DEFERRED`;
2. the roster this run started with carries it, so a unit the run added — a promoted finding, an
   adopted discovery — is never carried;
3. the run-state file carries its `rescope · item defer <unit>` row, written by
   `--rescope <slug> --act defer` and owed to the owner at the wrap-up;
4. its spec header `closes` or `advances` an ask this build's own `BACKLOG.md` files under this
   build's slug, and `ASKS_CMD` reads that ask neither CLOSED nor WONTDO — a blank `ASKS_CMD` is
   unmet, naming the missing contract;
5. no CLOSED unit's spec declares a `consumes-from` edge onto it, because a closed half that needs
   the open half is not landable, and that build is a HAND OFF instead.
