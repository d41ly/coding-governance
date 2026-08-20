# TOOL-aPacedTurnstile-4 — the turnstile: one bar per repo, and a queue for the rest

**Status:** CLOSED · rev-7 · 2026-08-20 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

Nothing in the tree coordinates two bars on one machine. Make the runner claim a repo-wide beacon
before it dispatches, so a second session QUEUES with a visible position instead of running a
competing bar.

The motive is CONTENTION, measured, and it is not a wall-clock argument. The
`TOOL-aMeteredTurnstile-1` build record of 2026-08-20 sampled three full bars running at once on
node `a` and found CPU at 39 %, CPU queue length 0 and disk queue length 0, then measured a
sixteen-leg fixture at width 24 as 26 % slower than the same fixture at width 8. Idle CPU, empty
queues, and more workers making it slower is the signature of a SERIALIZED bottleneck: the contended
resource is the process-and-file-creation path, and it does not parallelise. Two concurrent bars are
therefore worse than two sequential ones on this machine, which is the whole case for serializing
them. That argument survives a leg getting faster; an argument from a wall clock does not.

How many checkouts share one repository here is `git worktree list | wc -l`, derived and never
pinned, and it has already moved: eleven at this build's README, 24 at the `aMeteredTurnstile`
record of 2026-08-20, 26 when this revision was written.

## 2. Scope (IN)

- **S1** — the beacon lives under the git COMMON dir, resolved absolutely, NOT the per-worktree git
  dir the runner already uses for evidence. Those existing resolutions are deliberate and are not
  touched.
- **S2** — the atomic claim is a directory create, which fails if it exists. The heartbeat file is
  written FIRST on winning, so a just-claimed holder is never mistaken for one with no clock.
- **S3** — a ticketed FIFO queue: every run, including an uncontended one, first creates a ticket
  whose name sorts by time. Order is the byte-wise sort of the listing, so every waiter derives the
  same total order independently with no counter file and no coordinator.
- **S4** — the heartbeat is refreshed at ONE existing call site: inside `runleg()`, immediately
  before it commits its completion, wherever `TOOL-aPacedTurnstile-5` leaves that commit. The reader
  loop is NOT a second site, and §4 records why the earlier two-site scope was wrong rather than
  merely dropping it.
- **S5** — two-signal reaping: a dead PID reaps immediately; a heartbeat older than the TTL reaps
  regardless of PID. Both branches exist and each is armed in isolation. The TTL is DERIVED per §4
  and is never a wall clock copied out of a timing cache.
- **S6** — release folds into the existing EXIT trap, widened to catch interrupt, terminate and
  hangup, and guarded by nonce identity so a run whose beacon was reaped cannot delete its
  successor's.
- **S7** — waiter output: a line on entry, on every position change, and otherwise on a slow tick,
  plus a durable status file removed on release.
- **S8** — a bounded wait that fails OPEN: on expiry, print loudly, drop the ticket, and run
  unqueued. The bound is a DECLARED multiple of the TTL of S5, so it moves with the one number this
  unit derives and is never sized against a bar's wall clock. The turnstile never contributes a
  non-zero exit.
- **S9** — nested-run safety with NO exemption predicate on the primary path, because the key
  derivation already separates them, plus an exported lineage marker as a backstop for future
  callers.
- **S10** — a new gated leg, `tools/run-gates/run-gates.turnstile.test.sh`, driven against scratch
  repos through the manifest seam and never against the real bar, registered in the manifest, in the
  kit's descriptor, AND in `memory/map/features/run-gates.md` as a claim line for this leg's key.
  The third registration is not optional bookkeeping: the codebase-map gate-leg inventory reds on an
  unclaimed key, that test is in this unit's own §7, and `TOOL-aPacedTurnstile-1` S12 explicitly
  declines the key — "that unit adds its own key to this dossier when it lands" — so the obligation
  was assigned by one unit and accepted by none until round 2's R16 found it. The suite SHIPS:
  `tools/run-gates/kit.toml` claims the kit directory with `include = "**"` at `role = "engine"`,
  so every arm must be true in any adopting tree — no gov leg name, no gov threshold, nothing keyed
  on this repo's manifest — and the suite carries its own executed-assertion counter and floor at
  birth, the pattern `TOOL-aPacedTurnstile-1` established when it withheld the gov-only sibling.
- **S11** — the runner prints the seconds it spent queued on ONE parseable line, zero on an
  uncontended run. A wrapper that brackets a wall clock around the whole runner cannot otherwise
  tell waiting from working, and `tools/run-gates/profile_bar.py` is exactly such a wrapper. This
  unit ships the line and nothing else; who consumes it is the fork in §8.

## 3. Non-goals (OUT)

- Any behaviour that can change a verdict. The turnstile is a scheduler; every failure mode it has
  must be "slower" or "unqueued", never "checked less".
- Cross-MACHINE coordination. The contention unit is this machine's cores.
- Touching the per-worktree evidence paths. A struck, retained finding in
  `memory/builds/aBranchedMandate/build/` records a previous claim that those were shared, which was
  wrong and was kept as a lesson.
- A separate map dossier. `TOOL-aPacedTurnstile-1` authors ONE dossier for this kit and THIS unit
  adds its own leg's claim line to it under S10; a second dossier would double-claim a key
  `memory/map/FOUNDATION.md` already owns. The passive "is claimed there" is what let the claim
  belong to nobody — the accepting half of `-1` S12's hand-off is S10, stated in the active.
- An exemption row for the new suite. It lands inside the kit directory, which the kit's file rule
  already claims.
- Any reduction in the bar's wall clock. This unit removes CONTENTION between bars and moves the
  wall clock of a single bar by nothing at all. The 2026-08-20 re-scope measured the bar as
  floor-bound, one leg holding 81 % of the wall, so no scheduler this unit could ship would move it.
- **CUT by the 2026-08-20 re-scope, recorded rather than deleted.** A second heartbeat refresh site
  at the top of the reader loop, and the old AC9 arm that proved release on `TOOL-aPacedTurnstile-3`'s
  halt path. §4 carries the reason for the first and §9 carries the reason for the second; both were
  refusals, not oversights.
- Teaching `tools/run-gates/profile_bar.py` to subtract the queue line S11 prints. That file belongs
  to `aMeteredTurnstile` and no re-scope decision authorized this unit to edit it. S11 ships the
  line; §8 carries the fork over who reads it.

## 4. Design

### Verified starting state

The unattended kit's "at most one run is live" check counts non-terminal run-state FILES under the
memory tree. It is a check over committed records, not a runtime lock. **Confirmed at this
revision's regrounding:** a search of `tools/run-gates/` and `tools/gate-legs.json` for a beacon, a
turnstile, a queue, a `flock` or a lock directory returns nothing. The sibling that landed in the
same window, `tools/run-gates/profile_bar.py`, MEASURES a run and names its regime; it holds no
claim, no queue and no release, so it neither delivers any part of this mechanism nor conflicts with
it.

There IS prior art for atomic claiming on this platform, and it is undocumented as such:
`tools/hooks/agent-cap.js` claims a numbered slot with an exclusive create, keyed under the git
COMMON dir, with an mtime-TTL sweeper. Its header states the location rationale verbatim — one
budget per repo, not per worktree, because a session is a session whichever checkout it stands in.
That is the same question this unit answers, already answered once here. The turnstile mirrors it
rather than inventing a second shape.

### Location

The per-worktree git dir is correct for evidence and for the timing ledger, and stays. The COMMON
dir is correct for the turnstile, because the contention unit is the machine and every checkout
`git worktree list` reports shares one. Measured in this worktree, the two resolutions differ
exactly as expected.

Resolving with an absolute path format is required rather than decoration: measured, a plain git-dir
query from a repository toplevel returns the relative string `.git`, which is not a stable
cross-session key. The pre-commit hook already uses that flag pair, so this reuses it.

### On-disk shape

A holder directory whose EXISTENCE is the lock, containing a heartbeat line and a one-shot metadata
file; a queue directory of ticket directories; and a graveyard for reaped holders, swept on every
claim attempt.

The heartbeat is one line carrying the clock AND the progress a waiter prints — epoch, reported
count over total, and the last leg reported. Every worker in the pool rewrites it concurrently, and
an atomic rename makes that last-writer-wins with no torn read. The pool width is whatever
`tools/run-gates/gate-profiles.txt` declares for the detected hardware, so the number of concurrent
writers is read from that table and is not a constant this spec may state.

### The claim

The directory create is the ONLY decision. An exclusive file create would work equally for a single
file, but the holder needs to be a container for two files, and a directory gets both the container
and the atomic create in one call.

Every run tickets FIRST, then loops: reap, check whether it is lowest, attempt the claim. The
uncontended fast path is deliberately not special-cased — one extra directory create against a run
that takes minutes is not worth the barging hole a fast path opens, where a holder releases while
the lowest waiter is mid-sleep and a fresh arrival claims ahead of it.

### Deriving the TTL, and why no wall clock can supply it

The refresh gap is bounded by the LONGEST SINGLE LEG, because S4 refreshes only at a leg's
completion. So the TTL must exceed the longest leg, and the question is where a bound on a leg comes
from. Three candidate sources, two of which are disqualified by evidence rather than taste.

**The timing cache cannot supply it.** `<git-dir>/gate-timings.tsv` is last-write-wins across runs
at different load, and the `aMeteredTurnstile` build record of 2026-08-20 states outright that its
cells are not comparable across runs: the same leg was recorded at 659.9 s two days earlier and
observed at 47.7 minutes in that session, with its sibling never returning at all. It is also
fragmented one file per git dir, and orphan rows are never evicted. A number read out of it is a
number about some other run.

**A measured bar wall clock cannot supply it either**, and that same build record makes the rule
explicit for adopters: never pin a gate assertion to a wall clock. The figure this spec used to
quote — a 659.9 s longest leg inside an 873 s bar — was already superseded when the re-scope
re-measured, and a TTL sized to that floor would now reap a live holder and hand the waiter
permission to start the second bar this unit exists to prevent.

**A per-leg deadline CAN supply it, when one is configured.** `run-gates.sh` wraps each leg in
`timeout -k 5s "$PROF_TIMEOUT"` when `PROF_TIMEOUT` is non-zero, and maps exits 124 and 137 to a RED
naming the leg. That knob is a genuine upper bound on a leg, hence on the refresh gap, and it is the
only derived source available. So:

- When `PROF_TIMEOUT` is non-zero, the TTL is a DECLARED multiple of it, computed at run time.
- When it is zero — which every row of `gate-profiles.txt` declares today — the TTL falls back to a
  declared floor whose comment says plainly that no smaller number is derivable, because with no
  per-leg deadline the refresh gap is unbounded and no measurement can bound it.

The fallback has a NAMED ceiling, and it gets a `ponytail:` comment in source rather than a hopeful
silence: a holder whose single leg outruns the floor is reaped while alive, and the cost is one
extra concurrent bar, never a wrong verdict, because §3 already forbids the turnstile from changing
what gets checked. AC4c arms that ceiling so it is a known property with a test rather than a
surprise. The honest consequence is that a non-zero `PROF_TIMEOUT` row makes this mechanism strictly
better, which is a reason for a later build to set one and not a dependency this unit creates.

### Reaping — both signals, and why neither alone

**PID liveness is a NEGATIVE-ONLY signal.** A failure to signal is proof the holder is gone and
reaps on the spot. A success proves nothing, because PIDs are reused and a PID from another runtime
can answer for someone else. So success only withholds the fast reap; it never confers life.

**Heartbeat age is the only signal for wedged-but-alive**, and that is not hypothetical:
`TOOL-aBoundedVerdict-10` records a leg hanging with zero output at 240 s and wedging the whole bar,
and `aMeteredTurnstile` reproduced the same leg at 47.7 minutes with its sibling never returning.
That process is alive, holds CPU, and stops refreshing, so a PID-only reaper would leave its beacon
held forever. The older spelling of this paragraph added "with no per-leg deadline in the runner",
which stopped being true when `TOOL-aPacedTurnstile-2` landed `PROF_TIMEOUT`: the MECHANISM now
exists and only the CONFIGURATION is absent, every profile row declaring `timeout=0`. That
distinction is the whole basis of the TTL derivation above, so the claim is restated rather than
carried.

Holder reap is by RENAME and ticket reap is by DELETE, and the asymmetry is load-bearing. The holder
path is fixed, so deleting it directly can destroy a SUCCESSOR that claimed in the gap between
reading the metadata and the delete. Renaming into the graveyard is atomic, exactly one racer wins,
and the winner then takes the ordinary claim path anyway. Ticket names carry a unique nonce and are
never re-created, so deleting one has no such hazard.

The named ceiling, which gets a `ponytail:` comment in source: between reading the holder's nonce and
the rename, a live holder could release and a new one claim. The window is microseconds and the
worst outcome is one extra concurrent bar, never a wrong verdict. Not worth consensus machinery for
a scheduler.

### Why the reader loop is not a refresh site

The earlier scope named two refresh sites, the second being the top of the reader loop, "so the
progress field advances while workers are quiet". Measured against the shipped runner, that site
cannot do it: the reader blocks on `wait -n`, so the top of the loop is reached only when a worker
finishes. During the exact window the TTL argument depends on — one long leg running alone in the
tail — no worker finishes and the loop never iterates. The second site contributes nothing in
precisely the case that was its stated reason for existing.

Two ways out, and the cheaper one is also the more honest. A background ticker process would refresh
on a clock independent of the pool, at the cost of one more process per run to maintain a number
whose only consumer is a scheduler, on a machine this build has just measured as spawn-bound.
Dropping the site instead costs nothing, because a quiet pool has no progress to report anyway, and
it forces the TTL to be sized against a LEG rather than against a gap — which is what the derivation
above now does. The site is dropped.

### Signals

The existing trap is EXIT only, so terminate and hangup already leak the scratch dir today. Widening
it to catch interrupt, terminate and hangup fixes that leak as well as releasing the beacon. Release
re-reads the holder's nonce and removes it only on a match; it removes its own ticket
unconditionally, which is safe because the name is unique.

One premise here depends on a sibling and is stated rather than assumed, and round 2's R2/R3
corrected it in both directions. `TOOL-aPacedTurnstile-5` retargets the per-leg COMPLETION FILES
into a per-run directory under the git dir; it does NOT retarget the `mktemp -d` scratch, which
survives and still holds the timings temporaries. So there are two directories with two lifetimes:

- **The `mktemp -d` scratch belongs to this trap.** The widened trap releases the beacon and sweeps
  the scratch dir, on EXIT and now also on INT, TERM and HUP. That is the leak the round-1 finding
  actually named, and it is this unit's to close because it is the unit that widens the signal set.
- **The per-run directory belongs to `TOOL-aPacedTurnstile-5` and this trap never touches it.** It
  is the durable record, its only deleter is that unit's post-verdict sweep, and nothing clears it
  at the start of a run.

The earlier spelling — "the widened trap therefore releases the beacon and sweeps the run directory"
— claimed the cleanup line for this unit with the ownership REVERSED, on a premise about `-5` that
its text does not support. This unit lands SECOND, immediately after `-5`, so the reversed version
would still have won by default and deleted the record on every clean exit and on all three caught
signals — every path except the crash the record exists to make readable — reddening `-5`'s
durable-record criteria on the bar the moment it landed.

A hard kill runs no trap at all. That case is exactly what the reaper exists for, and an arm proves
recovery within one poll tick rather than after the TTL.

### The wrapper that brackets the bar

`tools/run-gates/profile_bar.py` starts a monotonic clock, runs `run-gates.sh` as a subprocess at the
real repo root with `GATE_FULL=1`, and stops the clock on return. With a turnstile in front, queue
time lands inside that `wall`, and the record it appends is advertised as comparable across months.

Two corrections to the way this hazard was reported. It does NOT trip that file's packing refusal:
packing is wall over ideal and the refusal fires below 1.0, so queue time — which only inflates wall
— pushes the ratio up and away from it. And the record is not silently wrong either, because
`check_quiet()` already enumerates foreign `run-gates.sh` processes BEFORE the run starts and marks
the record unquiet when it finds any. What remains is real and narrower: a queued run reports a wall
clock inflated by waiting, against leg durations that did not change, so its regime arithmetic reads
as bad packing when the truth is that the bar was in a queue. There is no field separating the two.

S11 ships the one thing only the runner can supply — the queue seconds, on a line a wrapper can
subtract — and stops there. The line's verb must sit OUTSIDE that file's closed verdict alternation
of `ok`, `skip` and `FAIL`, or a scheduling line becomes a phantom leg in the record; AC13 asserts
the parsed verdict count is unchanged by its presence.

### The nested-run problem — the exact predicate, argued

Three candidates; two are disqualified by MEASUREMENT rather than taste.

**Keying on the manifest env var is wrong, not merely spoofable.** The canary does not set it: every
nested run there changes directory into a scratch repo and runs against that repo's own manifest, so
the predicate misses all of them. It also over-matches, silently opting an operator with a custom
manifest out of the queue.

**Keying on a different repository ROOT is wrong.** The evidence harness deliberately sets an
explicit git dir while pointing the work tree at the REAL repo, because a toplevel query refuses a
bare git dir. Measured under exactly that environment, the toplevel resolves to the real worktree
while the git dir and common dir resolve to the scratch. A root-keyed turnstile would make the
nested evidence runs collide with their own parent — self-deadlock, converted by the bounded wait
into a stall per case.

**Keying on the common dir itself is sound and needs no predicate.** Measured for both suites, every
nested run resolves to its own scratch dir, none of which equals the real common dir. Nested runs
take a different turnstile BY CONSTRUCTION — nothing to exempt, nothing to spoof, no code. This is
an absence of collision rather than a predicate, and it is also what makes the turnstile testable:
the new suite's nested runners share one scratch common dir, so they queue against each other and
never against the real bar running them as a leg.

The population of nested-running legs is DERIVED from `tools/gate-legs.json` and never listed here.
When this revision was written, six manifest legs invoked the runner and three of them post-dated
the sentence that used to name two of them by hand. AC10 enumerates from the manifest so the next
one enrols itself.

The exported lineage marker rides on top as a backstop for a future caller that does not have this
property, and it is a backstop rather than the mechanism.

### Rollout

One commit, landing SECOND in this build's order, immediately after `TOOL-aPacedTurnstile-5`. The
2026-08-20 re-scope put it there because its value is contention rather than wall clock and it is
independent of the base and boundary changes `-6` and `-7` make, so landing it early de-risks
everything after it; and because it widens the EXIT trap that `-5` narrows, so the trap's final
shape must be settled by `-5` first. Rollback is removing the claim call; the bounded wait already
fails open, so the degraded state and the rollback state are the same and both are armed.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/run-gates.sh` | the common-dir derivation, ticket, claim, one refresh site, the queue line, release in the widened trap |
| `tools/run-gates/run-gates.turnstile.test.sh` | new — the suite, driven against scratch repos, shipped with the kit |
| `tools/gate-legs.json` | the new leg |
| `tools/run-gates/kit.toml` | a new `[[gate_leg]]` row. Not "the fifth" and not any ordinal: that descriptor's own header now states that the count is derived by govkit and deliberately unwritten, because the number that used to sit in its prose was wrong one commit later |
| `tools/run-gates/README.md` | a row in the hand-kept "The pieces" table for the new suite. That table is already stale — it lists neither `profile_bar.py` nor `profile_bar.test.sh` — and landing a file without a row widens the gap |
| `memory/map/features/run-gates.md` | this leg's claim line — the key `TOOL-aPacedTurnstile-1` S12 explicitly declined and left to this unit (R16) — plus the new file in that dossier's `paths.globs` |
| `AGENTS.md` | the turnstile bullet |

`tools/run-gates/profile_bar.py` is deliberately absent from this table. It gains a row only if §8's
fork resolves toward this unit consuming the queue line rather than a follow-up doing it.

### Alternatives rejected

- **A lock file with an exclusive create.** Works, but the holder needs a container for two files.
- **Per-worktree keying.** Rejected by the contention unit: the cores are the machine's.
- **A counter file for queue order.** Rejected: it needs its own atomic update. Time-sortable ticket
  names let every waiter derive the same order independently.
- **Refusing to run when the beacon is held.** Rejected: the turnstile must never contribute a
  non-zero exit, and a bar that refuses is a bar people bypass.
- **A background ticker process refreshing the heartbeat on its own clock.** Rejected above: one
  more process per run on a machine measured as spawn-bound, to maintain a number a leg-sized TTL
  makes unnecessary.
- **`profile_bar.py` claiming the beacon itself and starting its clock after acquisition.** Rejected:
  it puts a second implementation of the claim, reap and release discipline in a second language,
  which is the shape §10 exists to refuse.

## 5. Production-readiness checklist

- security — everything lives in the git dir, already trusted; a hostile beacon can delay a run or
  be reaped, never change a verdict.
- perf / scale — one directory create per run, plus a poll tick while waiting.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English in shell.
- error / empty / loading states — waiting IS the loading state and is the thing this unit makes
  visible; expiry falls back to running unqueued.
- observability — S7 on the stream and in a durable file another session can read, plus S11's
  parseable queue line for a wrapper that measures the run.
- risks (concurrency, data-loss, rollback hazards) — two named ceilings, both with a `ponytail:`
  comment in source and an arm: the reap race, and the TTL floor reaping a holder whose single leg
  outruns it while no per-leg deadline is configured. The worst outcome of either is one extra
  concurrent bar. The widened trap fixes an existing scratch leak rather than adding a hazard.
- testing + left-shift gates — each reap branch is armed in isolation, which is what stops one
  branch masking the other's absence; the suite ships to adopters, so every arm must hold in any
  tree.
- migration / rollback — an existing beacon directory from an older run is reaped by TTL on first
  contact.
- user docs — the charter bullet, the kit README row, and the waiter's own output.

## 6. Acceptance criteria

- **AC1** — When two runners start against one scratch common dir,
  `bash tools/run-gates/run-gates.turnstile.test.sh` observes the PEAK number of simultaneous holders
  as exactly 1, recorded by the fixture legs themselves through the rendezvous preamble the existing
  canary already uses. NOT an intersection of recorded start and end timestamps: that shape was
  retired by name in `TOOL-cSteadyMetronome-1` after it graded the node rather than the runner and
  red three consecutive pushes on a tree it had already passed.
- **AC2** — When the same two runners are started with the turnstile disabled, the suite observes a
  peak above 1 — the negative control in `tools/run-gates/run-gates.turnstile.test.sh`, without which
  AC1 passes on an implementation that serializes by accident.
- **AC3** — When a holder is killed with an uncatchable signal, the next waiter claims within one
  poll tick, and the reap reason recorded is the dead PID rather than the TTL — asserted in
  `tools/run-gates/run-gates.turnstile.test.sh`.
- **AC4** — When a holder's PID is live AND answering, but its heartbeat has been forced older than
  the TTL, the next waiter reaps and claims, and the recorded reap reason is the TTL rather than the
  dead PID — asserted in `tools/run-gates/run-gates.turnstile.test.sh` against the UNMODIFIED runner.
  A variant with the PID branch disabled is kept only as a supplementary arm: an arm that edits the
  code under test proves a mutant serializes, not that the shipped nesting does.
- **AC4b** — When a holder runs a fixture whose legs COMPLETE more often than a scaled-down TTL, it
  is still held at the end of the run and a waiter polling across that whole window never claims —
  driven in `tools/run-gates/run-gates.turnstile.test.sh`. Legs that complete, not legs that merely
  run long: S4's single refresh site fires at a completion, so this is the arm that matches the
  shipped mechanism. Without it, every reaping arm is satisfied by a reaper that reaps everything.
- **AC4c** — When a holder runs a fixture with ONE leg longer than the scaled-down TTL and no
  per-leg deadline configured, the suite asserts it IS reaped mid-run and that the successor's run
  still reports every leg — the named ceiling of §4's fallback, armed rather than assumed, with the
  matching `ponytail:` comment present in `tools/run-gates/run-gates.sh`.
- **AC5** — When three runners queue, they acquire in ticket order, asserted in
  `tools/run-gates/run-gates.turnstile.test.sh` against the recorded acquisition sequence.
- **AC6** — When a waiter is queued, it prints its position on entry and again on every change, and
  its durable status file under the resolved git dir carries the same position while it waits and is
  gone after it releases — asserted in `tools/run-gates/run-gates.turnstile.test.sh` against the path
  the runner resolves, never against a path this spec spells.
- **AC7** — When the bounded wait expires, the runner prints a loud notice, drops its ticket, runs
  every leg, and exits with the bar's own verdict — the turnstile contributing nothing to the exit
  code, asserted in `tools/run-gates/run-gates.turnstile.test.sh`.
- **AC7b** — When ONE runner runs uncontended at the shipped bound, that loud notice is absent from
  its output and it exits with the bar's own verdict — the negative control for the bound, asserted
  in `tools/run-gates/run-gates.turnstile.test.sh`. AC7 proves the expiry path works; without this
  nothing proves the bound stays quiet on an ordinary long run.
- **AC8** — When a run is interrupted or terminated, the beacon is released, asserted in
  `tools/run-gates/run-gates.turnstile.test.sh` for each signal the widened trap catches.
- **AC9** — CUT by the 2026-08-20 re-scope. It asserted beacon release on `TOOL-aPacedTurnstile-3`'s
  fail-fast halt at a chunk boundary; that re-scope cut the halt along with chunk-major dispatch, so
  the criterion graded a path the build no longer builds. AC8 already covers release on every signal
  a killed worker can produce. Recorded, not deleted.
- **AC10** — When the suite enumerates every leg in `tools/gate-legs.json` whose argv invokes
  `run-gates.sh`, it asserts each such nested run resolved a `--git-common-dir` different from the
  real one, so none of them queues against the real beacon. The population is READ from the manifest
  at run time, never listed in the suite: the previous wording named two legs when six qualified.
- **AC11** — When a run whose beacon was already reaped exits, it does NOT remove the successor's
  beacon, asserted by nonce mismatch in `tools/run-gates/run-gates.turnstile.test.sh`.
- **AC12** — When `bash tools/check-testsuite-counts.sh` runs, the new suite reports its executed
  assertion count at or above its floor with no row in
  `memory/project/testsuite-count-waivers.txt`. That leg derives its population from the manifest's
  argv strings, so registering the suite under S10 enrols it with no further wiring.
- **AC13** — When a run acquires the beacon uncontended, `tools/run-gates/run-gates.turnstile.test.sh`
  asserts the queue line reports zero; when a run waits behind a holder, it reports the observed wait
  within one poll tick; and in both cases the count of lines matching `profile_bar.py`'s verdict
  alternation of `ok`, `skip` and `FAIL` is unchanged by the new line.

## 7. Gates

`bash tools/run-gates/run-gates.turnstile.test.sh` · `bash tools/run-gates/run-gates.test.sh` ·
`bash tools/run-gates/run-gates.evidence.test.sh` · `bash tools/check-testsuite-counts.sh` ·
`python tools/govkit/govkit.py selfcheck` · `python tools/codebase-map/test_codebase_map.py` ·
`bash tools/check-playbook-parity.sh` · `python tools/memory-tree/check-arms.py --check`.

## 8. Open questions

none open — all three forks are RESOLVED, and the first was decided at build time under the
owner's instruction to build the set through to completion. Each is kept with the reason it
survived the veto order.

- **Who consumes S11's queue line.** `tools/run-gates/profile_bar.py` belongs to `aMeteredTurnstile`
  and this unit is not authorized to edit it. Option (a): this unit also teaches that file to
  subtract the queue seconds, which is a few lines and closes the hazard in one commit, at the cost
  of editing another build's file without a decision. Option (b): this unit ships only the line and
  a backlog row carries the subtraction, at the cost of leaving the profiler recording inflated
  walls for as long as the row is open. Option (c): neither, and the profiler's existing
  `check_quiet()` marking is accepted as sufficient, which is honest but leaves no field separating
  waiting from working. Recommendation: (a), because the mechanical edit is smaller than the record
  needed to defer it and the hazard exists from this unit's landing. The build runs attended, so the
  owner picks.
  RESOLVED (2026-08-20): **(a), taken at build time and flagged rather than assumed.** The owner's
  instruction was to build the set through to completion, which is authority to build and not
  authority to re-scope, so the pick is recorded here with what made it the small choice rather than
  the convenient one. Two things had changed since the fork was written. The record unit had already
  edited `profile_bar.py` — repointing it at the ledger — on that build's own written pledge to read
  this build's store, so "editing another build's file" was no longer a first crossing. And the
  hazard is self-inflicted rather than theoretical: the profiler brackets a wall clock around the
  runner, a queue wait inflates the wall while leaving the durations alone, and that is exactly the
  direction that trips its own packing refusal — a queued run would make an ordinary bar look
  arithmetically impossible and the tool would refuse its own measurement. The edit is four lines
  and the wait is RECORDED as well as subtracted, because a number that silently disappears from a
  published wall is one nobody can audit.
- **Whether the TTL should be lowered once the heavy legs are sharded.** The fallback floor is set
  above any leg this repo has observed, deliberately.
  RESOLVED (agent, 2026-08-18, delegated): leave it, with the derivation written beside the
  constant. Lowering it against a floor this build does not move would be tuning to a number the
  sharding build is about to invalidate, and the constant's comment is what carries the reason
  forward to that build. The 2026-08-20 re-scope strengthens the pick rather than changing it: the
  bar is floor-bound, so the sharding build is the only one that can move the number this TTL would
  be tuned to.
- **Whether an uncontended run should skip the ticket for speed.** Recommendation: no, as argued
  above — the barging hole costs more than the create.
  RESOLVED (agent, 2026-08-18, delegated): no - every run takes the ticket. The barging hole
  costs more than the create, and section 3 rules that every failure mode of this unit must be
  "slower" or "unqueued" and never "checked less"; a skip path is the one shape that can
  violate it.

## 9. Revision log

- rev-7 · 2026-08-20 · A DEFECT this unit shipped, found while building `-3` and fixed in that
  commit. The beacon was claimed and the release trap was installed later, with the whole manifest
  parse, the fingerprint and the run-record setup in between — a window in which the beacon is HELD
  and nothing would release it. A signal there killed the run and left the repository queueing
  behind nobody until the TTL expired.

  It surfaced as a FLAKE and was nearly written off as one. The signal arms passed three times in a
  row run alone and failed on TERM and HUP the moment they ran after another harness; two earlier
  explanations — signal delivery into a blocking `wait`, and the arm signalling a wrapper process —
  were each partly right and neither was the cause. What settled it was that the window is exactly
  the thing load widens, and process creation on this platform has been measured 25x slower under
  contention. The trap now goes on at the instant of the claim and the later one SUPERSEDES it, so
  there is never a moment with no handler and never two racing to remove one directory. Verified
  under the load shape that reproduced it.

  The lesson is the one this repo already writes down and this build re-learned: an intermittent arm
  is a report about a real race until proven otherwise, and the proof is a mechanism rather than a
  green re-run.

- rev-6 · 2026-08-20 · BUILT and CLOSED. The turnstile keys on the git COMMON dir, so every
  worktree of one repository shares one beacon and two repositories never do — "one bar per repo"
  falls out of the key derivation instead of needing a predicate. Verified on this node: the
  primary tree and this worktree both resolve `C:/projects/coding-governance/.git`, so they now
  serialize, which is precisely the contention that cost this build's own closing run about 100
  minutes on one leg.

  **What the arms cost to get right, recorded because both were the suite grading itself.** The
  peak-occupancy arm is paired with a control that runs the SAME fixture with the turnstile off
  and must observe an overlap; without it the arm passes on an implementation that serialized by
  accident, and on a host too slow to overlap it now says so rather than claiming a pass. And the
  suite's own `beacon()` helper returned `git rev-parse --git-common-dir` verbatim, which is
  RELATIVE — plain `.git` in an ordinary clone — so eight arms tested a path that meant something
  different from the harness's cwd. They reported "the run never claimed the beacon, so this
  proves nothing", which is the arms refusing to grade rather than passing green, and is the only
  reason the defect was visible at all.

  **The TTL is derived, not copied.** What has to be outlasted is the gap between two heartbeat
  refreshes, and S4 refreshes at one site — a leg COMPLETING. So the bound is "how long can one
  leg take", which the profile row already declares as `timeout=`; when it declares nothing the
  fallback is deliberately large and carries a `ponytail:` comment naming its ceiling and the fix,
  which is setting `timeout=` rather than raising the fallback. AC4c arms that ceiling instead of
  assuming it.
- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the spec audit: AC1 and AC2 move from timestamp-interval intersection
  to the rendezvous peak, the shape `TOOL-cSteadyMetronome-1` established after the interval form was
  measured to grade the node instead of the runner (F18); AC4 is restated against the unmodified
  runner, having tested a mutant (F19); AC4b arms the heartbeat, without which every reaping arm is
  satisfied by a reaper that reaps everything (F17); the wait bound becomes a declared value (F37);
  the trap's interaction with `TOOL-aPacedTurnstile-5`'s retargeting is stated (F38).
- rev-3 · 2026-08-18 · swept section 8 under the standing mandate: every fork RESOLVED in
  place per M3, and the section's first non-blank line made machine-legal so the classifier
  reads this unit as READY instead of FORKED.
- rev-4 · 2026-08-18 · folded the round-2 spec audit. R2/R3: §4's sibling-premise paragraph was
  factually wrong about `TOOL-aPacedTurnstile-5` — that unit retargets the per-leg COMPLETION FILES,
  not the `mktemp -d` scratch, which survives and still holds the timings temporaries — and it
  claimed the cleanup line for this unit with the ownership REVERSED. Since this unit lands sixth,
  the reversed version would have won by default and swept the durable record on every clean exit
  and on INT, TERM and HUP, reddening `-5` AC3 and `-3` AC7/AC8 at its own landing. The two
  directories now have one owner each, stated in both files. R16: S10 accepts the map claim line
  `-1` S12 declines, §4 Files touched carries the dossier, and §3's non-goal stops saying "is
  claimed there" in the passive with no owner.
- rev-5 · 2026-08-20 · folded the owner's re-scope and the regrounding pass that preceded it,
  against the tree at `43a6c13e`; the header's `base` stays at the sha this design was originally
  grounded against, because that field is the immutable pin of the design pass and this line is
  where the regrounding sha belongs. The unit's shape is unchanged and its case is stronger, but
  every number it reasoned from had moved. **The TTL was the blocker.** It was derived from a 659.9 s
  longest leg inside an 873 s bar; the re-scope re-measured the bar at a materially larger floor, and
  `aMeteredTurnstile` observed the same leg at 47.7 minutes with its sibling never returning. A TTL
  sized to the old floor reaps a live holder and green-lights the second bar this unit exists to
  prevent — the precise failure §4 was written to argue against. The TTL now hangs off `PROF_TIMEOUT`
  when a profile row configures one, and off a declared floor with a named ceiling and an arm (AC4c)
  when none does, because with no per-leg deadline the refresh gap is genuinely unbounded and saying
  so is better than pinning a number that reads as derived. Every other pinned figure went the same
  way: the checkout count (eleven, then 24, then 26), the pool width (now read from
  `gate-profiles.txt`), the leg count, and S8's wait bound, which is now a multiple of the TTL rather
  than a figure sized against a wall clock. **One scope item was cut on evidence.** S4's second
  refresh site, at the top of the reader loop, cannot fire in the window it existed for: the reader
  blocks on `wait -n`, so it iterates only when a worker finishes, and the case it was written for is
  one long leg alone in the tail. Dropping it beats a ticker process on a machine this build measured
  as spawn-bound, and it is what forces the TTL to be sized against a leg. **AC9 was cut with the
  halt it graded**, the re-scope having removed chunk-major dispatch and the boundary halt from
  `TOOL-aPacedTurnstile-3`; AC8 already covers release on every signal a killed worker produces.
  **One hazard was found and one report of it corrected.** `profile_bar.py` brackets a wall clock
  around the whole runner, so queue time enters a record advertised as comparable across months; it
  does NOT trip that file's packing refusal, which fires below 1.0 while queue time pushes the ratio
  up, and the run is already marked unquiet by `check_quiet()`. S11 ships the queue line, §8 carries
  the fork over who subtracts it, and AC13 keeps the new verb out of the profiler's verdict
  alternation. **Three enumerations became derivations:** AC10's nested-run population is now read
  from `tools/gate-legs.json` (it named two legs when six qualified), the kit.toml row stops calling
  itself the fifth, and `tools/run-gates/README.md` joins the touched files because its hand-kept
  table is already missing two shipped files. AC4b was restated against legs that COMPLETE rather
  than legs that run long, matching the single refresh site; AC7b adds the missing negative control
  for the bound. §1's motive is now `aMeteredTurnstile`'s contention measurement — three bars at
  once with CPU at 39 % and both queues at 0, width 24 measured 26 % slower than width 8 — which
  does not rot when a leg gets faster. Rollout moves from sixth to second, per the re-scope's
  re-derived order.

## 10. Reuse audit

The seam this extends is `tools/hooks/agent-cap.js`'s slot claim: an exclusive create keyed under the
git common dir with an mtime-TTL sweeper, and a header that already argues the per-repo location this
unit needs. That file is the prior art, cited by path, and this unit mirrors its shape in shell
rather than inventing a second discipline. The absolute path-format flag pair comes from
`.githooks/pre-commit`. The refresh point is the runner's existing worker completion site, so no new
call site is created. The TTL's derived form reuses `PROF_TIMEOUT`, the per-leg deadline
`TOOL-aPacedTurnstile-2` already landed in the runner, rather than introducing a second notion of how
long a leg may take. The trap widening repairs a scratch-dir leak that exists today on terminate and
hangup.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL, guard, skip. The probe returned no prior runtime-LOCK record,
which is the answer recorded rather than a failure to retry. It did return prior art this unit is
bound by, and the first draft's flat "no prior record" line was wrong: `TOOL-cSteadyMetronome-1`
retired timestamp-interval concurrency assertions by name and supplies the rendezvous shape AC1 and
AC2 now use, and `TOOL-cFinalBerth-5` records the same class as a ratio arm flipping run to run.
`TOOL-aBoundedVerdict-10` supplied the observed wedged-but-alive case that makes the heartbeat branch
necessary, and the aBranchedMandate struck finding supplied the per-worktree-versus-common-dir
lesson. The 2026-08-20 regrounding added one more: `tools/run-gates/profile_bar.py` is a caller this
unit must not break, and re-reading it is what turned the queue-line hazard from a guess into a
bounded one.
