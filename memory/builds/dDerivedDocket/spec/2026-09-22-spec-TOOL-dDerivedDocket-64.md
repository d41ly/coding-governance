# TOOL-dDerivedDocket-64 — the turnstile queue's heartbeat, a move the liveness clock sees

**Status:** SPECCED · rev-4 · 2026-09-22 · node d · Tier-2 · base 07997375 · streams tooling · order 34

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-22-review-TOOL-dDerivedDocket-62-spec-audit-g9-round1.md](../reviews/2026-09-22-review-TOOL-dDerivedDocket-62-spec-audit-g9-round1.md) | spec-audit | TOOL-dDerivedDocket-62 TOOL-dDerivedDocket-63 TOOL-dDerivedDocket-61 |

<!-- /gen:spec-records -->

## 1. Goal

A bar waiting in the gate turnstile's queue moves none of the signals `--liveness` reads. Once
`TOOL-dDerivedDocket-27` lets a close queue for up to `TS_MAXWAIT`, 7200 s in gov, past gov's 5400 s
`RESUME_STALE_BOUND`, the resume tick kills and relaunches a healthy queued close, and under
`TOOL-dDerivedDocket-61` another session may take its slug over mid-queue. That is H2 of
`memory/builds/dDerivedDocket/reviews/2026-09-22-review-TOOL-dDerivedDocket-61-spec-audit-g8-round1.md`.
Here the waiter writes a per-worktree heartbeat on every tick it does not acquire, and unit 61's
`derive_last_move` reads that file's mtime as one more term, so a queued bar is a move.

## 2. Scope (IN)

- **S1** The runner's wait loop writes `gate-queue-heartbeat` into its own worktree's git dir. The
  write is one builtin `printf` of `waited<TAB><seconds>` into `$gd/gate-queue-heartbeat`, placed
  directly after the unconditional `TS_WAITED` refresh at `tools/run-gates/run-gates.sh:933` and
  before the `TS_MAXWAIT` test at `:934`. It is guarded and error-swallowed exactly as the status
  file's write at `:956` is, and it adds no process spawn. Observed by AC4 and AC5.
- **S2** Nothing removes the heartbeat. The removal at `:962` keeps removing `gate-queue-status`
  alone, and neither the queued-phase traps at `:840-843` nor the holder's traps at `:903-906` gain a
  line. A leftover is read by its mtime, so it ages out as an old gate log does. `gate-queue-status`
  keeps its lifecycle, its cadence and its arm. Observed by AC4 and AC5.
- **S3** `derive_last_move`, as unit 61 S3 extracts it from `print_liveness`, gains a term after its
  gate-log term: the mtime of `gate-queue-heartbeat` under the git dir the gate-log term already
  derives from `resolve_sidecar_dir`, with source label `gate-queue`. An absent file contributes
  nothing. A present file that `stat -c %Y` cannot date is a dead probe, named as the gate-log term
  names one, and reaches the existing `fail 52`. `--liveness` prints no new key. Observed by AC1,
  AC2 and AC3.
- **S4** The carriers stop saying four signals. The driver's `--liveness` header and its in-body
  signal comment name the heartbeat. The `RESUME_STALE_BOUND` row of the protocol key table, in the
  template and its render, replaces its enumeration with the pointer "when no signal `--liveness`
  reads has moved within it". The comments above `RESUME_STALE_BOUND` in `.unattended.conf` and in
  `tools/unattended/.unattended.conf.example` point at `--liveness` the same way. The turnstile
  section of `tools/run-gates/README.md` and the write site's own comment say what the file is for
  and that it is never removed. Observed by AC6.
- **S5** No capped carrier grows. The protocol template and its render each change by −67 bytes and
  0 lines, the pointer being that much shorter than the enumeration it replaces. No other capped
  carrier is edited. Observed by AC7.
- **S6** The suite arms follow the code, each staged RED. The driver suite gains the heartbeat in its
  `--liveness` signals block and over unit 61's AC20 fixture, the resume-tick suite gains a queued
  record, and the turnstile suite gains the heartbeat in its position fixture. Each suite's
  `FLOOR_ASSERTIONS`, and the driver suite's `FLOOR_SHARD_2` beside it, rises by exactly the
  assertions its new arms carry, counted off their blocks and never read off a run; the driver arms
  are written in region two, so `FLOOR_SHARD_1` does not move. Observed by AC8.
- **S7** The unit's hygiene: no kit version moves, no added line in a shipped kit file spells a
  `tools/<kit>/` literal, no function is minted and no `fail` branch is added. Observed by AC9.

## 3. Non-goals (OUT)

- A running leg that outlasts the bound. Once the waiter acquires, only its legs' logs move, so one
  leg running past `RESUME_STALE_BOUND` with no other leg landing still reads STALE. That is unit
  61's §5 risk (2), unchanged here. The holder's ticker could write the same file every
  `TS_TICK_EVERY`, which is §8 F5's declined option and the first follow-up the hands-off edge names.
- Re-pricing the stale-bound NOTE at `tools/unattended/unattended.sh:545`, H2's proposed left-shift.
  It would compare the bound against the pinned backstop. After this unit a queued bar is not silent,
  so that comparison would announce a gap this unit closes. The silence left is one leg, and pricing
  the bound against the largest leg ceiling is the second follow-up.
- `gate-queue-status`: its lifecycle, its content, its position-change cadence and its arm.
- How long a bar may take. `TOOL-aUnblockedFleet-8`'s contended-bar bound and unit 27's backstop are
  untouched; this unit changes only when a queued bar reads STALE.
- Which worktree's copy of a record is graded, and whether the clock joins moves across a slug's
  worktrees. That is `TOOL-dDerivedDocket-62`, promoted from B1 of the same review, which takes that
  finding's route (a): only the worktree whose checked-out branch is the record's run branch acts,
  every other copy reads ELSEWHERE, and `derive_last_move` keeps the per-worktree scope unit 61
  extracts it with, the clock joined across worktrees being that unit's rejected §8 F1 option (b).
  This term reads the directory the gate-log term reads, so its scope is per worktree too, and a
  run's queued close writes its heartbeat in the worktree its own `gates-green` runs from, which by
  that unit's contract is the one it lets act. This unit extends nothing that unit writes, but its
  criteria run the tick that unit changes: on that unit's driver a verdict that would act meets
  `holder-ref: absent` as `skip · NO RUN BRANCH`, so every fixture here that feeds the tick carries
  a `run-branch` fact naming the branch its HEAD has checked out, and the consumes-from edge below
  says so. A holder waiting on a Workflow, whose sub-agents and wave-worktree units move nothing
  the run worktree's clock reads, is not this unit's either: it is G9 H1, promoted to
  `TOOL-dDerivedDocket-65`.
- `--audit`'s unit stall probe, which stays on `read_tree_clocks`.
- A `--liveness` key saying whether the queue term is live.
- Rewording unit 27's AC9, §3 non-goal and rev-8 entry to cite this unit for the queued-bar half.
  That is the orchestrator's fold of M1.
- Any kit version constant. On this branch unattended stands at 1.29 and run-gates at 1.9, both
  above origin/main's 1.28 and 1.8 and unreleased, so neither move is owed.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-61` — `derive_last_move`, the one clock `print_liveness`,
  `check_lease_fresh` and `--status` share once that unit lands, which S3 extends by one term; its
  re-keyed resume matrix, whose check-58 refusal on a fresh clock AC2 reads; and its AC20 fixture,
  which AC2 reuses with the heartbeat in place of the gate log. Without it the term reaches
  `--liveness` alone, and the matrix keeps grading the retired lease file's clock.
- **consumes-from** `TOOL-dDerivedDocket-62` — the tick's `skip · NO RUN BRANCH` row, which a
  verdict that would act meets on `holder-ref: absent`, and its rule that only the worktree whose
  checked-out branch is the record's run branch acts, every other copy reading `ELSEWHERE`. AC1's
  and AC3's fixture carries a `run-branch` fact because of the first, and §5 risk (4) rests on the
  second.
- **hands-off** external — making a running bar beat as a queued one now does, through the holder's
  ticker; pricing `RESUME_STALE_BOUND` against the largest leg ceiling in the stale-bound NOTE; and a
  gotcha for the class, that a clock built on completion-time artefacts goes dark while a process
  waits or runs one long step. No unit in this build carries them.
- **hands-off** `TOOL-dDerivedDocket-65` — the term-per-signal shape of `derive_last_move`, after
  which that unit's sub-agent term is placed, last, beside `LM_TRANSCRIPT`.

## 4. Design

### What the merged tree does, measured

Measured on node `d` 2026-09-22 at `07997375` (PINNED), over a scratch repository holding only a conf
in the shape of the driver suite's `mkconf`, which declares `RESUME_STALE_BOUND="5400"`, and one
committed BUILDING run-state file carrying the six lease facts with `host: absent`, its commit dated
2000-01-01, under an empty `CLAUDE_CONFIG_DIR`, so no transcript derives:

| Fixture | Observation |
|---|---|
| nothing fresh | `--liveness` prints `last-move-source: commit`, `stale: yes`, `verdict: STALE`, `stale-bound: 5400` |
| `gate-queue-heartbeat` written just now under the git dir | unchanged, because the driver reads no such file |
| `gate-queue-status` written just now under the git dir | unchanged, because nothing reads that file's mtime either |
| one gate log touched under `gate-logs/` | `last-move-source: gate-log`, `stale: no`, `verdict: LIVE` |
| `resume-tick.sh --dry-run`, the heartbeat fresh | `resumed · attempt 1`: the tick would kill and relaunch |
| `resume-tick.sh --dry-run`, the gate log fresh | `skip · verdict LIVE` |

The criteria below run that fixture with one fact more, a `run-branch` naming the branch its HEAD
has checked out. No driver at `07997375` reads it, so the measurement stands, and on
`TOOL-dDerivedDocket-62`'s driver it is what lets the tick act on that worktree's copy rather than
print `skip · NO RUN BRANCH` (G9 M6).

Read at `07997375`, nothing the runner writes during a wait moves a signal `--liveness` reads:

| Site in `tools/run-gates/run-gates.sh` | What it does while a bar waits |
|---|---|
| the ticket, `:815` | created once and empty, named by a UTC stamp, the runner's pid and a random number; never touched again |
| the beacon heartbeat, `:647` and the ticker at `:683-712` | the HOLDER's, refreshed every `TS_TICK_EVERY` under the git common dir |
| `gate-queue-status`, written at `:956` inside the branch at `:944` | rewritten only when the position changes; removed at `:962` when the loop ends; left behind by the queued-phase traps |
| the position lines at `:952` and `:954` | on a position change only, to stderr, which `run_bounded` captures into a `mktemp -d` file outside the tree |
| `gate queue: waited` at `:1014` | once, after the loop |
| a gate log, `:1741` | when a leg finishes, which no waiter reaches |

The numbers are DERIVED from source at `07997375` and re-derived by reading the same lines. Every gov
profile row sets `timeout=0` and `GATE_TURNSTILE_TTL` is set nowhere outside the turnstile suite, so
`TS_TTL` is its 1800 s fallback (`:632-633`), `TS_MAXWAIT` is four TTLs, 7200 s (`:638`),
`TS_TICK_EVERY` is a sixth, 300 s (`:642`), and `TS_TICK` defaults to 2 s (`:639`). Gov declares
`GATE_BOUND="3600"` and `RESUME_STALE_BOUND="5400"` (`.unattended.conf:52` and `:74`).

At `07997375` the harm is latent: `gates-green` runs `$GATE_CMD` under `GATE_BOUND` through
`run_bounded`, which kills a bar whose queue passes 3600 s before its silence reaches 5400 s. Unit
27 S4 replaces that bound with the backstop, and from then a healthy wait may run 1800 s past the
stale bound.

### Why the queue writes a file and the clock does not read the queue

The clock cannot read the queue's own state, for three reasons.

1. **Nothing in it moves while a bar waits**, as the table above shows. A clock over it would read
   presence, and presence cannot age. A waiter killed by SIGKILL, or by a signal its queued-phase
   traps answer, leaves `gate-queue-status` behind until the next wait in that worktree, so a dead
   run would read LIVE for as long as nobody queued there again. That is the reassuring-zero class,
   and it is the defect the round-2 audit of `TOOL-aUnblockedFleet-6` found in that file (its M4).
2. **It is not this run's state.** The queue and the beacon live under the git COMMON dir, which
   every worktree shares, and a ticket names a time, a pid and a random number but no worktree. A
   live ticket proves only that SOME bar in the repository waits, so every stale run on the node
   would read LIVE while any bar queued. That is B1's class run backwards: B1 grades one slug from
   many copies, and this would grade many runs from one queue.
3. **It is another kit's private lock.** The driver already reads one runner output, at the place
   the runner leaves it for readers: `<git-dir>/gate-logs/`, per worktree. A heartbeat beside it is
   one more name on that contract, not a new reach into the turnstile's internals.

So the queue writes a file the clock reads. The waiter writes it into its own worktree's git dir on
every tick, which answers all three: it moves while the waiter lives, it belongs to the worktree
whose `--liveness` reads it, and it sits where the gate-log term already looks. `$gd` is `GD`,
`git rev-parse --git-dir` at `:139`; `resolve_sidecar_dir` in `tools/unattended/lib-unattended.sh`
derives the same directory, and the driver runs `$GATE_CMD` from `$ROOT`
(`tools/unattended/unattended.sh:431`). Read by mtime, a leftover ages out exactly as an old gate log
does, so the writer needs to guarantee no lifecycle. This also avoids the other mechanism the
`TOOL-aUnblockedFleet-6` audit refuted: that spec read the status file under the common dir, where
nothing writes it.

After this unit the relation between `TS_MAXWAIT` and `RESUME_STALE_BOUND` no longer decides the
verdict for a queued bar. The heartbeat's age during a wait is bounded by the loop's own period, one
`TS_TICK` plus one iteration's probes, whatever either bound is.

### The runner half

One line, between `:933` and `:934`:

```sh
    [ -n "$gd" ] && printf 'waited\t%s\n' "$TS_WAITED" > "$gd/gate-queue-heartbeat" 2>/dev/null || true
```

It is reached on every iteration that neither acquires nor makes reap or sweep progress, which is
every iteration that sleeps. It is also reached on the iteration that fails open, before its break,
so the move nearest the first unqueued leg is written. `printf` and the redirect are builtins and
`TS_WAITED` is already computed, so the loop gains no process. A comment at the write site states
the file's reader by role, as an out-of-process liveness reader, and names no other kit's path.

### The clock half

The term takes the shape of the transcript term beside it. The path is `gate-queue-heartbeat` under
the directory the gate-log term derives. An absent file contributes nothing. A present one is dated
by `stat -c %Y`; an empty or non-numeric reading sets the dead probe to `stat -c %Y on <path>`; and
a reading newer than the newest move so far takes the move with source `gate-queue`. The comparison
is `-gt`, as for every other term, so a tie keeps the earlier source.

No key is added and no reader changes. `print_liveness` reports the term through `last-move` and
`last-move-source`, and `check_lease_fresh` grades it through the same function, so for a record
carrying a lease the tick, the stop-guard, the resume matrix and `--status` all see it at once. The
tick reads `last-move` and never `last-move-source` (`tools/unattended/resume-tick.sh:244`). At `07997375` the value is parsed nowhere
but four `hit` arms of the driver suite, from `tools/unattended/unattended.test.sh:5999` to `:6026`.

### What the heartbeat does not cover

- One leg running past the bound, as §3 states.
- A `GATE_CMD` that is not this runner, `GATE_TURNSTILE=0`, and an unresolvable common dir. Nothing
  queues in any of them, so there is nothing to beat.
- An orphaned bar whose session died. Its heartbeat keeps the run LIVE for at most `TS_MAXWAIT` of
  queue, exactly as its legs already keep it LIVE while they land, because the verdict chain does not
  consult `pid-alive`.
- A record carrying no lease. Unit 61 keeps its matrix rows on `build_folder_age` rather than on
  this clock (its §8 F13), and `--liveness` grades it UNBOUND, so the tick never acts on it and the
  heartbeat changes no answer the matrix gives it.
- A holder waiting on a background Workflow with no commit of its own. Its sub-agents write under
  the session's own transcript directory and its units in wave worktrees, neither of which this
  clock reads, so the run worktree can read STALE while it waits; the heartbeat beats only while a
  bar queues. That is G9 H1, promoted to `TOOL-dDerivedDocket-65`.

### Inventory

| Identifier | Kind | Cell, and the lexicon answer at writing |
|---|---|---|
| `gate-queue-heartbeat` | a file under each worktree's git dir, written by the runner | a file name; no naming cell declares file names |
| `gate-queue` | a `last-move-source` value | a value, beside `gate-log` |

The unit mints no function, so no name is owed to `python tools/lexicon/lexicon.py --suggest`. It
adds no `fail` branch and moves no `fail` line in either file, and the rows of
`memory/project/unarmed-branches.txt` key on a check number and an ordinal, so none is re-keyed.

### Migration

None. The unit adds no record fact, conf key or persisted state. A worktree whose git dir holds no
heartbeat reads exactly as at `07997375`, and a `gate-queue-status` left by any runner is still not
read.

### Rollout

The unit lands after unit 61 in this build's own run, in the serial order of the promoted units. A
bar beats only when the runner that runs it is this unit's copy, so the first bar to feed the clock
is the first one run from a worktree holding the build commit, this build's VERIFYING bar included.
It ships live rather than dark: its only effect is to withhold a kill for at most `TS_MAXWAIT` of
queue, and a default-off flag would switch the kill of a healthy queued bar back on.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/run-gates/run-gates.turnstile.test.sh` ·
`tools/run-gates/README.md` · `tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh`
· `tools/unattended/resume-tick.test.sh` · `tools/unattended/PROTOCOL.template.md` ·
`memory/guides/UNATTENDED-PROTOCOL.md` · `tools/unattended/.unattended.conf.example` ·
`.unattended.conf`

### Alternatives rejected

- The clock reading the queue's own state under the common dir, for the three reasons above.
- Refreshing `gate-queue-status` on every tick. Its lifecycle is that it exists only while a bar
  waits, pinned by the arm at `tools/run-gates/run-gates.turnstile.test.sh:338` and stated in
  `tools/run-gates/README.md`. Keeping its removal at `:962` drops the clock's newest move at the
  acquire, before the first leg lands; dropping the removal reds that arm and breaks what readers
  were told.
- A heartbeat under `gate-logs/`. It needs no driver change, but `resolve_newest_gate_log` would name
  it as the last bar's record on `--status`'s HELD checkpoint, and `last-move-source` would say
  `gate-log` for a bar that has landed no leg.
- The driver recording the bar's pid at `run_bounded`'s start, for `--liveness` to grade alive.
  Existence is not progress, as the verb carrier says of `pid-alive`: a hung runner stays alive to
  that probe until the backstop kills it, about eight hours in gov, while its heartbeat stops at
  once. It also sees only the bars the driver starts, and it is a freshness write at one instant,
  the shape unit 61 retires.
- Raising `RESUME_STALE_BOUND` above `TS_MAXWAIT`. It delays every presumed-stopped verdict on a
  genuinely dead run by the queue bound, and it types beside the stale bound a number another kit
  derives.
- Removing the heartbeat when the bar ends. It costs the clock nothing, because the bar's legs land
  after the wait, but it adds a line to trap sets the turnstile suite pins, to save one `stat` per
  `--liveness` call.

## 5. Production-readiness checklist

- security — The heartbeat lives under the worktree's own git dir, is written by the runner and is
  read by mtime only; its content is never parsed. Any process that can write the git dir can keep a
  run LIVE by touching it, which is the reach it already has over the gate logs, the index and the
  commit clock. The lease stops an accidental second driver and not a malicious one, as unit 61's §5
  states.
- perf / scale — The runner adds one builtin write per non-acquiring tick and no spawn, so at most
  3600 writes over gov's 7200 s wait bound at the 2 s tick. The driver adds one `stat` spawn per
  `--liveness` call in a worktree that has ever queued, because the file persists; unit 61 PINNED
  that clock at 0.68 s with no gate logs and 2.60 s with 90 on node `d`, one `stat` per log.
- error / empty / loading states — An absent file contributes nothing. A present file `stat` cannot
  date is the dead probe `fail 52` already refuses on. An unwritable git dir swallows the write, as
  the status file's is swallowed, and the runner already announces `evidence capture OFF` when it
  cannot make `gate-logs/` there; the run then reads as it does at `07997375`.
- observability — `last-move-source: gate-queue` while a bar waits; the file's content is the
  seconds waited, readable by hand; the tick prints `skip · verdict LIVE` for a queued close.
- risks — (1) An orphaned bar keeps its dead session's run LIVE for up to `TS_MAXWAIT` of queue.
  (2) One leg past the bound still reads STALE; the longest leg recorded is 1565 s, measured
  2026-08-23 and cited in `AGENTS.md`, under gov's 5400. (3) The basename is spelled in two kits and
  no standing gate joins the two spellings, as none joins `gate-logs` today; AC5 checks the pair at
  the build commit. (4) The term inherits the gate-log term's per-worktree reach. After
  `TOOL-dDerivedDocket-62`, ordered before this unit, only the worktree on the run's branch acts on
  either, and a heartbeat written in a sibling worktree moves only that sibling's copy, which reads
  ELSEWHERE.
- testing — The arms §7 names, each staged RED and executed once at VERIFYING; the direct
  observations in §6 are fixture runs of the driver and the tick, and greps over tracked files.
- migration — none, per §4 Migration.
- user docs — The turnstile section of `tools/run-gates/README.md`, the protocol's
  `RESUME_STALE_BOUND` row, both confs' comments and the driver's `--liveness` header.

## 6. Acceptance criteria

- **AC1** — When `--liveness` runs over the minimal fixture with its commit aged past
  `RESUME_STALE_BOUND`, no gate log and no transcript, and `gate-queue-heartbeat` under the fixture's
  git dir is dated inside the bound, it prints `last-move-source: gate-queue`, `stale: no` and
  `verdict: LIVE`, with the same keys in the same order as without the file. With that file dated
  past the bound by `touch -d` it prints `stale: yes` and `verdict: STALE`. With no such file, the
  tree a bar leaves that neither queues nor lands a leg, it prints `stale: yes` and `verdict: STALE`,
  the residual §3 states. With a `stat` stub first on `PATH` that fails for that one path, it refuses
  at check 52 naming `stat -c %Y on` that path and prints no `verdict:` line.
  Red when: a fresh heartbeat reads `stale: yes` with `last-move-source: commit`, as measured at
  `07997375`, so the tick kills a queued close; or a heartbeat older than the bound keeps a dead run
  LIVE, which a presence test would do; or an undatable heartbeat reads as absent. The fresh reading
  is staged RED by a copy of `derive_last_move` with the queue term removed.
  fixture: the scratch repository of §4's measurement, its record carrying a `run-branch` fact that
  names the branch its HEAD has checked out, with the file planted by hand, so no bar runs.
- **AC2** — Take `TOOL-dDerivedDocket-61` AC20's fixture with its commit and transcript aged past
  `RESUME_STALE_BOUND`, and plant `gate-queue-heartbeat` dated inside the bound in place of that
  criterion's gate log. `--status` prints no `presumed-stopped`, and `--resume --keepalive-id C` from
  session `T` refuses at check 58 and leaves the run-state file byte-unchanged. With the heartbeat
  dated past the bound, `--status` prints `presumed-stopped` and the same call takes the run over.
  Red when: a second session takes the slug over from a close still waiting in the queue, the take-over
  H2 names as new with unit 61; or the matrix and `--liveness` disagree about one queued bar because
  one of them reads a clock without the term.
  fixture: that unit's AC3 authorized record at a pinned BASE over a local bare remote, the shape the
  driver suite's prologue builds; the tree holds none outside that suite.
  permission: the arm lives in the driver suite, a held kit suite on no bar leg, so it runs in the
  orchestrator's attributed VERIFYING run and never in this pass.
- **AC3** — When `bash tools/unattended/resume-tick.sh --repo <fixture> --dry-run` runs over AC1's
  fixture with the heartbeat dated inside the bound, it prints `skip · verdict LIVE` and no
  `resumed ·` decision; with the heartbeat dated past the bound it prints `resumed · attempt 1`.
  Red when: the tick decides `resumed · attempt 1` for a record whose only fresh signal is the
  heartbeat, as measured at `07997375`, which on a live node kills the recorded pid's tree and
  relaunches a close that was waiting in the queue; or the aged half is made to pass by bending the
  tick to act on a record naming no run branch, which undoes `TOOL-dDerivedDocket-62`'s skip.
  fixture: AC1's, whose `run-branch` fact names the branch its HEAD has checked out, so on
  `TOOL-dDerivedDocket-62`'s driver the worktree holds the slug and the aged half reaches
  `resumed · attempt 1` rather than `skip · NO RUN BRANCH`; the resume-tick suite's arm runs over
  its `build_fixture`, which that unit makes write `run-branch: refs/heads/main`.
  permission: the fixture run is this pass's direct check; the arm that keeps it lives in the
  resume-tick suite, a held kit suite, executed at VERIFYING beside AC2's.
- **AC4** — When the `run-gates turnstile` leg runs its position fixture, where a planted live holder
  makes the waiter queue, `gate-queue-heartbeat` exists under the fixture's git dir while the waiter
  waits, and its `stat -c %Y` reading advances between two reads. Once the holder is released and the
  waiter has acquired and exited, the heartbeat still exists while `gate-queue-status` is gone, as
  that file's own arm already asserts.
  Red when: the waiter writes the heartbeat once, or only when its position changes, so a wait at one
  position is silent past the bound; or the runner removes it when the wait ends, so the move is lost
  at the acquire before the first leg lands. Staged RED by a runner copy with the write line deleted,
  and by one that removes the file beside `gate-queue-status`.
  permission: the turnstile suite is a held kit suite, so it runs at the build's one post-build bar
  with self-tests and never in this pass.
- **AC5** — When `grep -cE '^[^#]*gate-queue-heartbeat'` runs at the build commit over the gate
  runner and over `tools/unattended/unattended.sh`, each prints 1. The loop-scoped count,
  `awk '/^  while \[ -n "\$TS_TICKET" \]; do$/,/^  done$/' tools/run-gates/run-gates.sh | grep -cE '^[^#]*gate-queue-heartbeat'`,
  prints 1, and `grep -nE '^[^#]*(gate-queue-heartbeat|-ge "\$TS_MAXWAIT")' tools/run-gates/run-gates.sh`
  prints the heartbeat's line above the `TS_MAXWAIT` test.
  Red when: the writer and the reader spell the basename differently, so the term reads absent for
  ever while each suite plants its own literal and passes; or a second code line removes the file; or
  the write sits outside the wait loop or after its fail-open break, so the last tick before the
  bound is silent.
- **AC6** — When `grep -ci 'four signals'` runs at the build commit over `.unattended.conf`,
  `tools/unattended/.unattended.conf.example` and `tools/unattended/unattended.sh`, and
  `grep -c 'the newest gate log and the session transcript'` over
  `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md`, each prints 0;
  and `grep -c 'gate-queue-heartbeat' tools/run-gates/README.md` prints at least 1.
  Red when: a carrier still says four signals, so a reader sizing `RESUME_STALE_BOUND` against a
  queued bar is told that bar is silent; or the runner writes a file another kit reads and its own
  README never names it.
  permission: that each render stays byte-identical to its template is the `unattended skill wiring`
  and `unattended kit gate` legs over the real tree, observed at the VERIFYING bar.
- **AC7** — When `git cat-file -s` and `wc -l` read `tools/unattended/PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md` at the build commit and at its first parent, neither
  build-commit figure is greater than its parent's, and each file's delta is −67 bytes and 0 lines.
  Red when: the pointer is written without the enumeration's removal, so a carrier already under a
  curation-debt waiver grows; or the reading is taken against this spec's figure instead of the
  parent commit.
  figure: the −67 is PINNED at `07997375`, the difference between the removed enumeration and the
  pointer S4 quotes; the not-greater test is derived at the build commit.
- **AC8** — When the orchestrator's attributed unattended run at VERIFYING reports on the driver and
  resume-tick suites, and the build's post-build bar with self-tests reports the `run-gates turnstile`
  leg, each reads clean with this unit's arms among the executed ones, and each suite's
  `FLOOR_ASSERTIONS`, with the driver suite's `FLOOR_SHARD_2`, reads at the build commit its figure
  at the first parent plus exactly the assertions those arms' blocks carry, read with `git show` at
  both, while the driver suite's `FLOOR_SHARD_1` is unchanged.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it, above all the
  status-file arm at `tools/run-gates/run-gates.turnstile.test.sh:338` and the key-order arm at
  `tools/unattended/unattended.test.sh:5882`; or a floor moves by a number no arm accounts for.
  permission: all three are held kit suites on no plain bar leg, so they run at VERIFYING and never
  in this pass.
- **AC9** — When `grep -c 'KIT_UNATTENDED_VERSION=1.29' tools/unattended/unattended.sh` and
  `grep -c 'KIT_RUN_GATES_VERSION=1.9' tools/run-gates/run-gates.sh` run at the build commit, each
  prints 1. The lines this unit adds to every shipped kit file it edits, read by `git diff -U0` of
  the build commit, carry no `tools/<kit>/` literal. `grep -cE '^[a-z_]+\(\) *\{'` over the driver
  and over the gate runner prints what it printed at the parent, and so does
  `grep -cE '^[^#]*\bfail [0-9]+'` over the driver.
  Red when: the unit moves a version the unreleased kits do not owe; or an added line spells a path
  the install-prefix ban forbids; or a function or a `fail` branch arrives unpriced, so the naming leg
  or a pinned row of `memory/project/unarmed-branches.txt` moves under it.
  permission: the ban's verdict is the `install-prefix (shipped surface)` leg, and the armed-or-pinned
  verdict is the `harness arms (fail branches armed or pinned)` leg, both observed at VERIFYING.

## 7. Gates

`run-gates turnstile` · `run-gates canary` · `run-gates gov canary` · `unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `recall floor` · `recall floor arms` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a driver copy whose `derive_last_move` lacks the queue term, under which the signals block's fresh heartbeat reads `stale: yes` and unit 61's AC20 fixture with a fresh heartbeat is taken over · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2`, each raised by exactly the new arms' assertions, counted off their blocks
New arm: `tools/unattended/resume-tick.test.sh` · the same driver copy, under which a BUILDING record with a fresh heartbeat, over the suite's `build_fixture` and the `run-branch` fact it writes, decides `resumed · attempt 1` · `FLOOR_ASSERTIONS`, raised by exactly the new arm's assertions, counted off its block
New arm: `tools/run-gates/run-gates.turnstile.test.sh` · a runner copy with the heartbeat write deleted, and one removing the file beside `gate-queue-status` · `FLOOR_ASSERTIONS`, raised by exactly the new arm's assertions, counted off its block

Every floor follows this build's practice, set by the CLOSED units 25, 30, 49 and 54: a unit raises
its suite's executed-assertion floor by exactly the arms it adds, derived from the blocks rather than
read off a run, which this pass does not make. The driver's new arms are written in region two, so
`FLOOR_SHARD_1` does not move.

The two `recall floor` legs are owed by `memory/guides/UNATTENDED-PROTOCOL.md` under the guards
join. `tools/run-gates/` is a broad guard, so the runner's legs are named here by choice: the turnstile
suite carries AC4's arm, and both canaries run the edited runner.

## 8. Open questions

- **F1 — where a queued bar's move lives.** Options: (a) the waiter writes a per-worktree heartbeat
  and the clock reads its mtime; (b) the clock reads the queue's own state under the git common dir;
  (c) the waiter refreshes `gate-queue-status` on every tick; (d) a heartbeat under `gate-logs/`;
  (e) the driver records the bar's pid and `--liveness` grades it alive. RESOLVED (agent,
  2026-09-22, delegated): (a), settled by this spec's author under the build's delegated rule on the
  first route of H2's proposed fix. §4 carries the reasons against (b) to (e).
- **F2 — how often the heartbeat is written.** Options: (a) every tick that does not acquire;
  (b) every `TS_TICK_EVERY`; (c) on a position change, as the status file is. RESOLVED (agent,
  2026-09-22, delegated): (a), by the same author. (c) is exactly the silence H2 names, and (b) needs
  a second counter in the loop to save writes that cost no spawn.
- **F3 — when the heartbeat is removed.** Options: (a) never; (b) when the wait ends; (c) when the
  bar ends. RESOLVED (agent, 2026-09-22, delegated): (a), by the same author. (b) loses the move at
  the acquire, and (c) edits pinned trap sets to save one `stat`.
- **F4 — the source label.** Options: (a) `gate-queue`; (b) fold it into `gate-log`. RESOLVED (agent,
  2026-09-22, delegated): (a), by the same author, so a reader of `--liveness` tells a queued bar from
  a landing leg; no reader outside the driver suite parses the value.
- **F5 — does this unit also make a RUNNING bar beat.** Option: the holder's ticker, `ts_tick_start`,
  writes the same file every `TS_TICK_EVERY`, closing unit 61's §5 risk (2). RESOLVED (agent,
  2026-09-22, delegated): no, by the same author, because the brief scopes this unit to the one
  mechanism that closes H2, and the review names that silence as H2's residual rather than as a
  finding of its own. It is handed off external.
- **F6 — a `memory/DECISIONS.md` row.** RESOLVED (agent, 2026-09-22, delegated): none, by the same
  author. The decision is F1 above and the write site's comment, and unit 61's row already records the
  lease reconciliation this unit completes.

## 9. Revision log

- rev-1 · 2026-09-22 · initial draft, promoted from H2 of the G8 spec audit, round 1, grounded on
  `07997375`, the merged tree, and on `TOOL-dDerivedDocket-61` as specified at rev-2, with the
  current behaviour measured over a scratch fixture.
- rev-2 · 2026-09-22 · §2 S6 · §3 · §4 · §5 · §6 AC8 · §7 · re-read against unit 61 rev-3 and
  `TOOL-dDerivedDocket-62` rev-1. §3 and §5 risk (4) now state the scope that unit gives the clock
  instead of deferring to it: route (a) leaves `derive_last_move` per worktree and lets only the
  worktree on the run's branch act, so this term consumes nothing that unit writes and no edge to it
  is declared. §4 adds a record with no lease, whose rows unit 61 §8 F13 keeps on
  `build_folder_age`, to what the heartbeat does not cover, and scopes the four readers to a record
  carrying one. S6, AC8 and §7 name the driver suite's `FLOOR_SHARD_2` beside `FLOOR_ASSERTIONS`,
  each raised by exactly the new arms and counted off their blocks. Unit 61 now answers this unit's
  consumes-from with a hands-off line. No design, other criterion, edge or order moved.
- rev-3 · 2026-09-22 · §3 · §4 · §6 AC1 AC3 · §7 · G9 spec audit round 1 fold of M6, and of this
  spec's halves of M8 and H1. M6: AC1's and AC3's fixture carries a `run-branch` fact naming the
  branch its HEAD has checked out, so AC3's aged half reaches `resumed · attempt 1` on
  `TOOL-dDerivedDocket-62`'s driver rather than `skip · NO RUN BRANCH`, and §4 says why the
  measurement did not need one. §3 now declares a consumes-from edge to that unit, which answers
  it with a hands-off line, and its non-goal no longer says no edge is owed. M8: unit 61's F1, AC20
  and §5 risk (2) now agree with §3 and F5 here that a leg silent past the bound is carried by no
  unit and handed off external, so nothing here moved for it. H1 is not folded: §3 and §4 name a
  holder waiting on a Workflow as G9 H1, promoted to `TOOL-dDerivedDocket-65`. No order moved.
- rev-4 · 2026-09-22 · §3 · one hands-off edge added, to `TOOL-dDerivedDocket-65`, answering that unit's
  consumes-from. Edges only; nothing this unit specifies moved.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a waiting process refreshes a heartbeat file so an
out-of-process liveness clock sees it move"` returns no seam for this work: its candidates are
name-stem matches such as `corpus_files` and `parse_cpu_clock` in the Python kits, and its header
prints `unscanned layers: .sh`, the layer both halves are written in. So no existing seam fits in
the corpus the probe reads. The seams this unit extends were found by reading source: the gate-log
term of `print_liveness`, which unit 61 moves into `derive_last_move`, with its directory from
`resolve_sidecar_dir`; the runner's per-worktree `gd`; the wait loop's unconditional `TS_WAITED`
refresh; and the status file's guarded write, whose shape the heartbeat copies.

Recall terms used: `python tools/memory-recall/query.py "how does the liveness clock see a merge bar
that is waiting in the turnstile queue, so a queued close is not read stale and killed" --terms
"turnstile queue wait liveness stale bound gate-logs heartbeat resume-tick kill queued close
TS_MAXWAIT"`. It returned `TOOL-aUnblockedFleet-8`'s backlog row and `TOOL-aUnblockedFleet-6`'s
retired spec, whose audit refuted a driver reading the status file; the G8 review's H2 itself;
`TOOL-aScannedThrottle-2`, which put the queue wait into the run record; `TOOL-aBoundedCeiling-12`;
and the aReapedTicket build, whose README records that a queue ticket carries no liveness signal of
its own.
