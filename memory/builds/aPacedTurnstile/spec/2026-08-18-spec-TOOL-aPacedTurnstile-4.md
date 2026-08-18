# TOOL-aPacedTurnstile-4 — the turnstile: one bar per repo, and a queue for the rest

**Status:** OPEN · rev-3 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

Nothing coordinates two bars on one machine, and `git worktree list` reports twelve checkouts sharing
one repository here. Make the runner claim a repo-wide beacon before it dispatches, so a second
session QUEUES with visible position instead of running a competing 873 s bar.

## 2. Scope (IN)

- **S1** — the beacon lives under the git COMMON dir, resolved absolutely, NOT the per-worktree git
  dir the runner already uses for evidence. Those existing resolutions are deliberate and are not
  touched.
- **S2** — the atomic claim is a directory create, which fails if it exists. The heartbeat file is
  written FIRST on winning, so a just-claimed holder is never mistaken for one with no clock.
- **S3** — a ticketed FIFO queue: every run, including an uncontended one, first creates a ticket
  whose name sorts by time. Order is the byte-wise sort of the listing, so every waiter derives the
  same total order independently with no counter file and no coordinator.
- **S4** — the heartbeat is refreshed at two EXISTING call sites: inside the worker just before it
  commits its completion, and at the top of the reader loop so the progress field advances while
  workers are quiet.
- **S5** — two-signal reaping: a dead PID reaps immediately; a heartbeat older than the TTL reaps
  regardless of PID. Both branches exist and each is armed in isolation.
- **S6** — release folds into the existing EXIT trap, widened to catch interrupt, terminate and
  hangup, and guarded by nonce identity so a run whose beacon was reaped cannot delete its
  successor's.
- **S7** — waiter output: a line on entry, on every position change, and otherwise on a slow tick,
  plus a durable status file removed on release.
- **S8** — a bounded wait that fails OPEN: on expiry, print loudly, drop the ticket, and run
  unqueued. The bound is a DECLARED value with its reasoning beside it, not an unnamed number, and it
  is stated against the measured 873 s full bar it must outlast. The turnstile never contributes a
  non-zero exit.
- **S9** — nested-run safety with NO exemption predicate on the primary path, because the key
  derivation already separates them, plus an exported lineage marker as a backstop for future
  callers.
- **S10** — a new gated leg, `tools/run-gates/run-gates.turnstile.test.sh`, driven against scratch
  repos through the manifest seam and never against the real bar, registered in the manifest and in
  the kit's descriptor.

## 3. Non-goals (OUT)

- Any behaviour that can change a verdict. The turnstile is a scheduler; every failure mode it has
  must be "slower" or "unqueued", never "checked less".
- Cross-MACHINE coordination. The contention unit is this machine's cores.
- Touching the per-worktree evidence paths. A struck, retained finding in
  `memory/builds/aBranchedMandate/build/` records a previous claim that those were shared, which was
  wrong and was kept as a lesson.
- A separate map dossier. `TOOL-aPacedTurnstile-1` authors one dossier for this kit and this leg's
  key is claimed there; a second dossier would double-claim a key `memory/map/FOUNDATION.md` already
  owns.
- An exemption row for the new suite. It lands inside the kit directory, which the kit's file rule
  already claims.

## 4. Design

### Verified starting state

The unattended kit's "at most one run is live" check counts non-terminal run-state FILES under the
memory tree. It is a check over committed records, not a runtime lock. **Confirmed: this repo has no
runtime lock.**

There IS prior art for atomic claiming on this platform, and it is undocumented as such:
`tools/hooks/agent-cap.js` claims a numbered slot with an exclusive create, keyed under the git
COMMON dir, with an mtime-TTL sweeper. Its header states the location rationale verbatim — one
budget per repo, not per worktree, because a session is a session whichever checkout it stands in.
That is the same question this unit answers, already answered once here. The turnstile mirrors it
rather than inventing a second shape.

### Location

The per-worktree git dir is correct for evidence and for the timing ledger, and stays. The COMMON
dir is correct for the turnstile, because the contention unit is the machine and twelve checkouts
share one. Measured in this worktree, the two resolutions differ exactly as expected.

Resolving with an absolute path format is required rather than decoration: measured, a plain git-dir
query from a repository toplevel returns the relative string `.git`, which is not a stable
cross-session key. The pre-commit hook already uses that flag pair, so this reuses it.

### On-disk shape

A holder directory whose EXISTENCE is the lock, containing a heartbeat line and a one-shot metadata
file; a queue directory of ticket directories; and a graveyard for reaped holders, swept on every
claim attempt.

The heartbeat is one line carrying the clock AND the progress a waiter prints — epoch, reported
count over total, and the last leg reported. Up to eight workers rewrite it concurrently, and an
atomic rename makes that last-writer-wins with no torn read.

### The claim

The directory create is the ONLY decision. An exclusive file create would work equally for a single
file, but the holder needs to be a container for two files, and a directory gets both the container
and the atomic create in one call.

Every run tickets FIRST, then loops: reap, check whether it is lowest, attempt the claim. The
uncontended fast path is deliberately not special-cased — one extra create against an 873 s run is
not worth the barging hole a fast path opens, where a holder releases while the lowest waiter is
mid-sleep and a fresh arrival claims ahead of it.

### Why a naive TTL kills a live run

A full bar is 873 s and the longest leg is 659.9 s. The worst-case refresh gap is bounded by the
longest leg, because the ledger dispatches long poles first so the heavy leg overlaps everything
else and runs alone only in the tail. A 60 s or 300 s TTL would reap live runs. The default is
therefore well above that floor, with the 659.9 s measurement written beside the constant so a
future sharding build can lower it against a number rather than a feeling.

### Reaping — both signals, and why neither alone

**PID liveness is a NEGATIVE-ONLY signal.** A failure to signal is proof the holder is gone and
reaps on the spot. A success proves nothing, because PIDs are reused and a PID from another runtime
can answer for someone else. So success only withholds the fast reap; it never confers life.

**Heartbeat age is the only signal for wedged-but-alive**, and that is not hypothetical:
`TOOL-aBoundedVerdict-10` records a leg hanging with zero output at 240 s, wedging the whole bar,
with no per-leg deadline in the runner. That process is alive, holds CPU, and stops refreshing. A
PID-only reaper would leave its beacon held forever.

Holder reap is by RENAME and ticket reap is by DELETE, and the asymmetry is load-bearing. The holder
path is fixed, so deleting it directly can destroy a SUCCESSOR that claimed in the gap between
reading the metadata and the delete. Renaming into the graveyard is atomic, exactly one racer wins,
and the winner then takes the ordinary claim path anyway. Ticket names carry a unique nonce and are
never re-created, so deleting one has no such hazard.

The named ceiling, which gets a `ponytail:` comment in source: between reading the holder's nonce and
the rename, a live holder could release and a new one claim. The window is microseconds and the
worst outcome is one extra concurrent bar, never a wrong verdict. Not worth consensus machinery for
a scheduler.

### Signals

The existing trap is EXIT only, so terminate and hangup already leak the scratch dir today. Widening
it to catch interrupt, terminate and hangup fixes that leak as well as releasing the beacon. Release
re-reads the holder's nonce and removes it only on a match; it removes its own ticket
unconditionally, which is safe because the name is unique.

One premise here depends on a sibling and is stated rather than assumed: `TOOL-aPacedTurnstile-5`
retargets the scratch directory into the git dir and drops the cleanup this trap performs. The
widened trap therefore releases the beacon and sweeps the run directory, and the two units must agree
on which of them owns the cleanup line — this one does, because it is the unit that widens the
signal set.

A hard kill runs no trap at all. That case is exactly what the reaper exists for, and an arm proves
recovery within one poll tick rather than after the TTL.

**The interaction with `TOOL-aPacedTurnstile-3`'s halt is explicit:** that unit kills live workers
before cleanup, so release must be proven to run on that path too. An arm asserts the beacon is free
after a halted run, which is why this unit is sequenced after it.

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

The exported lineage marker rides on top as a backstop for a future caller that does not have this
property, and it is a backstop rather than the mechanism.

### Rollout

One commit, after `TOOL-aPacedTurnstile-3`. Rollback is removing the claim call; the bounded wait
already fails open, so the degraded state and the rollback state are the same and both are armed.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/run-gates.sh` | the common-dir derivation, ticket, claim, refresh at two sites, release in the widened trap |
| `tools/run-gates/run-gates.turnstile.test.sh` | new — the suite, driven against scratch repos |
| `tools/gate-legs.json` | the new leg |
| `tools/run-gates/kit.toml` | the fifth gate-leg row |
| `AGENTS.md` | the turnstile bullet |

### Alternatives rejected

- **A lock file with an exclusive create.** Works, but the holder needs a container for two files.
- **Per-worktree keying.** Rejected by the contention unit: the cores are the machine's.
- **A counter file for queue order.** Rejected: it needs its own atomic update. Time-sortable ticket
  names let every waiter derive the same order independently.
- **Refusing to run when the beacon is held.** Rejected: the turnstile must never contribute a
  non-zero exit, and a bar that refuses is a bar people bypass.

## 5. Production-readiness checklist

- security — everything lives in the git dir, already trusted; a hostile beacon can delay a run or
  be reaped, never change a verdict.
- perf / scale — one directory create per run, plus a poll tick while waiting.
- a11y — N/A: no user interface.
- i18n — N/A: operator-facing English in shell.
- error / empty / loading states — waiting IS the loading state and is the thing this unit makes
  visible; expiry falls back to running unqueued.
- observability — S7, on the stream and in a durable file another session can read.
- risks (concurrency, data-loss, rollback hazards) — the reap race is named with its ceiling in
  source; the worst outcome is one extra concurrent bar. The widened trap fixes an existing scratch
  leak rather than adding a hazard.
- testing + left-shift gates — each reap branch is armed in isolation, which is what stops one
  branch masking the other's absence.
- migration / rollback — an existing beacon directory from an older run is reaped by TTL on first
  contact.
- user docs — the charter bullet and the waiter's own output.

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
- **AC4b** — When a holder's legs run longer than the TTL while it keeps refreshing, it is still
  held at the end of the run and a waiter polling across that whole window never claims — driven at a
  scaled-down TTL in `tools/run-gates/run-gates.turnstile.test.sh`. Without this, every reaping arm is
  satisfied by a reaper that reaps everything.
- **AC5** — When three runners queue, they acquire in ticket order, asserted in
  `tools/run-gates/run-gates.turnstile.test.sh` against the recorded acquisition sequence.
- **AC6** — When a waiter is queued, it prints its position on entry and again on every change, and
  `<git-dir>/gate-queue-status.txt` carries the same position while it waits and is gone after it
  releases.
- **AC7** — When the bounded wait expires, the runner prints a loud notice, drops its ticket, runs
  every leg, and exits with the bar's own verdict — the turnstile contributing nothing to the exit
  code, asserted in `tools/run-gates/run-gates.turnstile.test.sh`.
- **AC8** — When a run is interrupted or terminated, the beacon is released, asserted in
  `tools/run-gates/run-gates.turnstile.test.sh` for each signal the widened trap catches.
- **AC9** — When a run halts at a chunk boundary under `TOOL-aPacedTurnstile-3`'s fail-fast path,
  the beacon is released — the kill path that unit introduces.
- **AC10** — When the canary and the evidence suite run as legs of the real bar, neither queues
  against the real beacon: `tools/run-gates/run-gates.turnstile.test.sh` asserts each nested run
  resolved a `--git-common-dir` different from the real one.
- **AC11** — When a run whose beacon was already reaped exits, it does NOT remove the successor's
  beacon, asserted by nonce mismatch in `tools/run-gates/run-gates.turnstile.test.sh`.
- **AC12** — When `bash tools/check-testsuite-counts.sh` runs, the new suite reports its executed
  assertion count at or above its floor with no waiver row.

## 7. Gates

`bash tools/run-gates/run-gates.turnstile.test.sh` · `bash tools/run-gates/run-gates.test.sh` ·
`bash tools/run-gates/run-gates.evidence.test.sh` · `bash tools/check-testsuite-counts.sh` ·
`python tools/govkit/govkit.py selfcheck` · `python tools/codebase-map/test_codebase_map.py` ·
`bash tools/check-playbook-parity.sh` · `python tools/memory-tree/check-arms.py --check`.

## 8. Open questions

none — the forks below are RESOLVED. Every pick is the M3 ratification of the fork's own
recommendation; the reason each survived the veto order is recorded with it.

- **Whether the TTL should be lowered once the heavy legs are sharded.** The default is set well
  above the 659.9 s floor deliberately. Recommendation: leave it, with the measurement written beside
  the constant, and let the sharding build lower it against its own number.
  RESOLVED (agent, 2026-08-18, delegated): leave it, with the measurement written beside the
  constant. Lowering it against a floor this build does not move would be tuning to a number the
  sharding build is about to invalidate, and the constant's comment is what carries the reason
  forward to that build.
- **Whether an uncontended run should skip the ticket for speed.** Recommendation: no, as argued
  above — the barging hole costs more than the create.
  RESOLVED (agent, 2026-08-18, delegated): no - every run takes the ticket. The barging hole
  costs more than the create, and section 3 rules that every failure mode of this unit must be
  "slower" or "unqueued" and never "checked less"; a skip path is the one shape that can
  violate it.

## 9. Revision log

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

## 10. Reuse audit

The seam this extends is `tools/hooks/agent-cap.js`'s slot claim: an exclusive create keyed under the
git common dir with an mtime-TTL sweeper, and a header that already argues the per-repo location this
unit needs. That file is the prior art, cited by path, and this unit mirrors its shape in shell
rather than inventing a second discipline. The absolute path-format flag pair comes from
`.githooks/pre-commit`. The refresh points are the runner's existing worker completion site and its
existing reader loop, so no new call site is created. The trap widening repairs a scratch-dir leak
that exists today on terminate and hangup.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL, guard, skip. The probe returned no prior runtime-LOCK record,
which is the answer recorded rather than a failure to retry. It did return prior art this unit is
bound by, and the first draft's flat "no prior record" line was wrong: `TOOL-cSteadyMetronome-1`
retired timestamp-interval concurrency assertions by name and supplies the rendezvous shape AC1 and
AC2 now use, and `TOOL-cFinalBerth-5` records the same class as a ratio arm flipping run to run.
`TOOL-aBoundedVerdict-10` supplied the observed wedged-but-alive case that makes the heartbeat branch
necessary, and the aBranchedMandate struck finding supplied the per-worktree-versus-common-dir
lesson.
