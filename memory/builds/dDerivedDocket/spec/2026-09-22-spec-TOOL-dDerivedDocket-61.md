# TOOL-dDerivedDocket-61 — one lease record, and HELD known to every out-of-session actor

**Status:** SPECCED · rev-5 · 2026-09-22 · node d · Tier-2 · base 285701d5 · streams tooling · order 31

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-22-review-TOOL-dDerivedDocket-61-spec-audit-g8-round1.md](../reviews/2026-09-22-review-TOOL-dDerivedDocket-61-spec-audit-g8-round1.md) | spec-audit | TOOL-dDerivedDocket-27 |

<!-- /gen:spec-records -->

## 1. Goal

The merge of origin/main at `c23d5701` kept two lease models, and on the merged tree they disagree in
measured ways: a record `--liveness` reads STALE is refused as freshly leased, a HELD run is blocked
from stopping and relaunched by the resume tick, a pushed landing cannot be re-bound, and an observed
in-place landing reads unstamped to every actor for ever. Reconcile them in the direction the owner
ruled on 2026-09-22, as the orchestrator's brief relays that ruling: ONE lease record, the run-state
facts main already writes, read by this build's resume matrix through `--liveness`'s own clock and
bound, with HELD carved out of the stop-guard, `--liveness` and the resume tick.

## 2. Scope (IN)

- **S1** The per-slug lease FILE retires. Deleted from `tools/unattended/unattended.sh`:
  `resolve_lease_path`, `read_lease` with its `LEASE_*` globals, `write_lease_taken`,
  `write_lease_refreshed`, `write_lease_released`, `remove_lease`, `resolve_lease_bound` and
  `write_lease_for_record`; `stage_or_fail`'s call to the last; the
  `RB_LEASE_SLUG` and `RB_LEASE_ID` globals, `run_bounded`'s refresh and the three verbs that set
  them (`verb_preflight`, `run_takeover`, `verb_close`); `verb_preflight`'s take-or-refresh block;
  `run_takeover`'s `write_lease_taken`; the `remove_lease` calls in `verb_landed` and `verb_abort`;
  `run_hold`'s `read_lease` and `write_lease_released`; and `verb_status`'s `LEASE —` line. No verb
  reads or writes a `.lease` file. `build_folder_age` STAYS, as the clock of a record that carries
  no lease (§8 F13). Observed by AC1 and AC22.
- **S2** ONE staleness bound. `LEASE_STALE_AFTER` leaves the driver (its default constant, its
  initialiser and its `read_bound_key` call), `tools/unattended/check-unattended.sh` (initialiser and
  conf allow-list), `tools/unattended/kit.toml`'s `optional_keys`, the example conf, gov's
  `.unattended.conf`, the protocol key table (template and render), the stop contract and the driver
  suite's three `mkconf` declarations. `RESUME_STALE_BOUND` is the one bound: the resume matrix and
  `--status` act on the staleness `--liveness` grades against it, and a record carrying no lease
  grades its build folder's age against the same number (§8 F13). Observed by AC2, AC4 and AC22.
- **S3** One clock for the lease. `derive_last_move` is extracted verbatim from `print_liveness`:
  the two tree clocks of `read_tree_clocks`, the newest gate log under the worktree's git dir, and
  the recorded session's transcript. `print_liveness` calls it and keeps its `fail 52` on a dead
  probe; `check_lease_fresh` is re-keyed onto a run-state file and calls it, returning 0 fresh, 1
  stale and 2 unknown as before. Fresh and stale are observed by AC4, AC5 and AC20, and unknown by
  AC21.
- **S4** `--liveness` knows HELD and the observed in-place landing. A recorded `HELD` prints
  `state: held` and `verdict: HELD`; a recorded `LANDING` whose landing commit the node's landed log
  names (S10) prints `state: terminal` and `verdict: TERMINAL`. The verdict order becomes TERMINAL,
  FINISHED-UNSTAMPED, HELD, UNBOUND, STALE, LIVE, so HELD is never STALE, and every key still prints on
  every run that reaches a verdict. Observed by AC5 and AC10.
- **S5** `tools/unattended/stop-guard.js` ALLOWS a stop whose liveness verdict is `HELD`, with reason
  `held`, placed directly after the `terminal` row; `REASONS` and the header's decision table gain the
  row. Observed by AC6.
- **S6** `tools/unattended/resume-tick.sh` SKIPS a run whose verdict is `HELD` with its own named
  decision, because the durable restart `--hold` prints under `RESUME_SCHEDULE` is HELD's restart; its
  header's decision table gains the row. Observed by AC7.
- **S7** The resume matrix is RE-KEYED onto the run-state lease facts (§4 table): identity is the
  `keepalive` fact, or the `session` fact matched against `CLAUDE_CODE_SESSION_ID` for the
  same-session row; freshness is `check_lease_fresh`. The holder's matching-id resume writes NOTHING
  unless the record carries no `lease-utc` or names another session or pid than the harness exposes.
  The same-session row takes the run over without the staleness test, refused by a new check-58
  branch when the recorded pid is alive and is not `CLAUDE_PID`. A record carrying no `lease-utc`
  keeps unit 4's leaseless rows, graded by `build_folder_age` against `RESUME_STALE_BOUND`, and gains
  a `--replaces` row through the leased row's block, so a holder whose scheduler lists another job
  than the record names can still take the one lease record (§8 F13). Observed by AC3, AC4, AC11,
  AC12, AC20, AC21 and AC22.
- **S8** `verb_resume` RE-BINDS the run-state lease for a pushed landing `--landed` has not yet
  observed: with an id, on a record whose recorded phase is `LANDING` and whose derived phase is
  `LANDED`, it runs `write_lease`, stages the record and prints the old and new values, which restores
  the remedy `fail 55` names. It re-binds only on a branch where that landing's own `--landed` runs,
  the record's run branch or, under `primary`, the default branch, and from any other branch it
  writes nothing (§4). So that the re-bound record still lands, `read_landing_commit` in
  `tools/unattended/lib-unattended.sh` and `--landed`'s `primary` clean check both treat a difference
  from HEAD confined to the six lease-fact lines as no difference, through one new lib predicate,
  `check_lease_only_diff`, and no other caller of the clean check is exempted. Observed by AC8 and
  AC23.
- **S9** The keepalive reap READ-BACK runs under `LANDER_MODE=in-place`. The block at
  `tools/unattended/unattended.sh:4029` moves, with its message texts and check numbers unchanged,
  into `check_keepalive_reaped`, defined directly above `verb_landed`, and both branches call it
  before the anchor round-trip. Observed by AC9.
- **S10** The in-place landing OBSERVATION, which lived in the retired file as `released <iso>
  landed`, moves to an append-only line in `landed.<slug>.log`, in the `unattended` directory under
  the git COMMON dir. `write_landed_observation` appends it when an in-place `--landed` derives
  `LANDED`; `read_landed_observation` reads it for `--liveness` (S4), for `--status` and for the
  matrix's observed-landing row. It is not a lease: no reader asks it who drives the slug. Observed
  by AC10, which reads it from a second linked worktree.
- **S11** The carriers say what the code now does. `UNATTENDED-STOPS.md` §7, §8, §9 step 5, §4
  item 3, §12 and its title describe the one lease record; `UNATTENDED-VERBS.md` gains `HELD` in
  `--liveness` and rewords `--resume`; the protocol takes the five edits §4 prices; the Skill's tick
  paragraph names checks 10, 26 and 51 for a tick issued before `--preflight` and drops the refresh
  claim, its what-wakes paragraph carves HELD out, its Resume section loses the `LEASE` line rule and
  the doubled `--resume`, and its Record-the-run placements are scoped by landing mode; the
  `unattended` dossier's three lease sentences, the driver's `--resume` usage line, and the
  library's and the tick's "its four" comments follow, in the texts §4 quotes. Every render is
  re-rendered. Observed by AC13.
- **S12** NO capped carrier grows: the protocol template and render, the stop contract and the verb
  carrier with their renders, the `unattended` dossier and `memory/guides/SESSION-KICKOFF.md` each
  end the pass no larger in bytes or in lines than they began it, funded by the trims §4 names.
  Observed by AC14.
- **S13** The suite arms follow the code. Every assertion in the driver suite that reads or writes a
  lease file is retargeted to the run-state facts or the landed log, one for one, so the executed
  count does not fall; a fixture the suite makes leaseless by deleting the lease file is made
  leaseless by deleting the six lease-fact lines instead, so the leaseless arms keep their expected
  texts, the dead-clock `fail 57` one included; the one-line `--status` counts stop filtering the
  retired `LEASE —` line; the new arms §7 names are written and each is staged RED. Each suite's
  executed-assertion floor rises by exactly the assertions its new arms carry, counted off their
  blocks and never read off a run: the driver suite's `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2`, its
  new arms written in region two beside the arms they extend, and the stop-guard and
  resume-tick suites' `FLOOR_ASSERTIONS`. A retargeted assertion is one for one and moves no floor.
  Observed by AC15.
- **S14** One `memory/DECISIONS.md` row under the TOOL heading, keyed by this unit's id, records the
  reconciliation and names the ruling as relayed. Observed by AC16.
- **S15** The kickoff manifest's dated correction saying two lease models coexist is pruned, its own
  prune condition being this unit. Observed by AC17.
- **S16** The unit's hygiene: no kit version moves, no kit file gains a kit-path literal, every new
  function name passes the lexicon, the new `fail` branch is armed, and no pinned row of
  `memory/project/unarmed-branches.txt` moves. Observed by AC18 and AC19.

## 3. Non-goals (OUT)

- The lease-fact SET and `write_lease`'s contract. `keepalive`, `session`, `pid`, `host`,
  `pid-image` and `lease-utc` keep their names, their writer and their `absent` spelling; this unit
  changes who reads them.
- Re-recording `session` and `pid` as `absent` at `--hold`, the merge skeptic's alternative to the
  carve-outs. The ruled direction is the carve-outs, and the facts stay the record of who held.
- The stall-recorder. It records and cannot block, and a stall of a held run is still a stall.
- The resume tick's CONTINUE payload. It already tells the resumed session to pass the idle-wake it
  schedules now, which the same-session row admits.
- `fail 55`'s remedy text. With S7 and S8 the `--resume <slug> --keepalive-id <id>` it already names
  works from every place that refusal fires (§8 F8), the re-bind's branch scope included, because
  that scope is the branch where the refusal fires.
- A one-spawn gate-log clock. `derive_last_move` keeps `print_liveness`'s one `stat` per log
  verbatim; §5 prices the cost and a single read is a follow-up.
- Wiring a declared gate wall into `RESUME_STALE_BOUND`, §8 F1's declined option (c). A bar that
  runs past the bound while its legs keep landing in the run's own worktree stays fresh through its
  gate logs instead, which AC20 observes. A bar queued at the turnstile writes no gate log and is not
  kept fresh by anything here: that is G8 H2, promoted (§8).
- The sidecar-root derivation `check 32` counts, the durable restart, the `--scheduled` refusals and
  `TOOL-dDerivedDocket-40`'s declined matrix-reacher column. None moves.
- Any kit version constant. The unattended kit stands unreleased at 1.29 on this branch.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-4` — HELD, `run_hold`, the resume matrix with its
  refusal-before-write property, `run_takeover`'s step order, the tri-state `check_lease_fresh`, and
  §8 F8's build-folder clock for a record with no lease, which this unit keeps (§8 F13). This unit
  re-keys the matrix and keeps every row's property but two reaches the G8 audit found lost, one
  record per slug across worktrees (G8 B1) and `--replaces` as the holder's own path (G8 H1), both
  promoted (§8).
- **consumes-from** `TOOL-dDerivedDocket-5` — `RESUME_SCHEDULE` as HELD's restart, which is why the
  tick skips HELD, and the `--scheduled` refusals evaluated ahead of the matrix, unchanged.
- **consumes-from** `TOOL-dDerivedDocket-22` — `read_derived_phase`'s LANDED, `read_landing_commit`,
  whose comparison S8 narrows by the lease-fact lines, and the in-place `--landed` observation with
  the matrix row that reads it, which S10 moves out of the retired file.
- **consumes-from** `TOOL-dDerivedDocket-3` — the in-place landing sequence and its rule that nothing
  is committed after the push, against which S11 scopes the Record-the-run placements.
- **consumes-from** `TOOL-dDerivedDocket-1` — the attributed criterion `verdict clean` over the
  unattended suites at VERIFYING, which AC15 reads.
- **consumes-from** `TOOL-dDerivedDocket-28` — ordered 27, before this unit. If it lands first: its
  reap step in `run_takeover` and on the holder rows of `verb_resume`, and its ledger beside the lease
  under the git common dir. This unit keeps each reap on the re-keyed row that holds the lease and
  leaves that directory in place. Whether that unit's prune-race argument survives one lease copy
  per worktree is G8 B1's, promoted (§8), and is not examined here.
- **hands-off** `TOOL-dDerivedDocket-62` — the re-keyed resume matrix, whose re-bind row and
  observed-landing row place that unit's two `check_holder_worktree` calls in `verb_resume`;
  `--liveness`'s HELD verdict and the verdict order its ELSEWHERE joins; the tick's named HELD arm
  and the stop-guard's `held` row; and the landed log under the git common dir. `derive_last_move`
  keeps this unit's per-worktree scope there, because that unit takes route (a) of G8 B1.
- **hands-off** `TOOL-dDerivedDocket-63` — the working rows of the re-keyed matrix as §4 writes
  them: the same-session row through `run_takeover` with its check-58 branch naming both pids and
  `CLAUDE_PID`, the leased `--replaces` row, the no-lease `--replaces` row that enters the same
  block, and the catch-all refusal, with the stop contract's §8 table that carries them and S13's
  retarget of the lease-file assertions. That unit re-orders and narrows them after this unit
  builds; §4's table is built here as it stands.
- **hands-off** `TOOL-dDerivedDocket-64` — `derive_last_move`, the one clock `print_liveness`,
  `check_lease_fresh` and `--status` share, which that unit extends by a `gate-queue` term after
  the gate-log term; and AC20's fixture, which that unit's AC2 reuses with a heartbeat in place of
  the gate log.

## 4. Design

### What the merged tree does, measured

Measured on node `d` 2026-09-22 at `285701d5` (PINNED), each over a scratch repository holding only a
conf and one committed run-state file carrying the six lease facts, dated 2000-01-01:

| Fixture | Observation |
|---|---|
| HELD, commit aged | `--liveness` prints `state: live`, `verdict: STALE` |
| the same, `stop-guard.js` fed a Stop payload for its session | blocks with reason `run-open`, telling it to `--plan` or `--abort` |
| the same, `resume-tick.sh --dry-run` | `resumed · attempt 1`: the tick would kill and relaunch it |
| BUILDING, a fresh lease file naming `k1`, commit aged | `--liveness` reads `verdict: STALE`; `--resume --keepalive-id k2` from the SAME session is refused at check 58 |
| LANDING pushed to a local bare `origin`, session `S-held` | `--status` reads `phase LANDED (derived`; `--resume --keepalive-id k2` from `S-new` prints `nothing to resume` and writes nothing; `primary` `--landed` from `S-new` refuses at check 55 |
| the same under `in-place` | `--landed` from `S-new` prints `phase LANDED (derived` with no `keepalive-reaped` line at all |
| the same, witness on the tip, `--landed` observed | `--liveness` still reads `FINISHED-UNSTAMPED`, and the stop-guard blocks with `landing-unstamped` |
| the same with `session:` hand-edited and staged | in-place `--landed` refuses at check 80: `read_landing_commit` finds no committed LANDING |

The last row is why S8 carries a tolerance: the merge skeptic's proposed re-bind alone would rewrite
the record the push carried, and both landing modes would then refuse it.

### The one lease record

The lease IS the run-state facts `write_lease` (`tools/unattended/unattended.sh:5121`) writes at
`--preflight`, at a take-over, and on the rows below that re-record it:

| Question | Answered by |
|---|---|
| does this record carry a lease | a `lease-utc` fact is present; a record without one predates the run-state lease and keeps unit 4's build-folder clock (§8 F13) |
| who holds it | the `keepalive` fact; for the same-session row, the `session` fact against `CLAUDE_CODE_SESSION_ID` |
| is its holder alive | `check_lease_fresh`: `derive_last_move` for the recorded session, against `RESUME_STALE_BOUND` |
| is it released | the phase: HELD is the released state, and a terminal is the removed one |

Freshness is DERIVED, never written. The retired file was refreshed by every writing verb, by the
start of `run_bounded` and by the holder's tick. All but one of those move a signal `--liveness`
already reads: a writing verb moves a dirty write or a commit, and a tick's turn appends to the
session's own transcript. The one that does not is `run_bounded`'s start. Once a bar's legs run,
each finished leg writes a gate log, which AC20 observes; but a leg writes its log only when it
finishes, and a bar waiting in the turnstile queue writes none, so nothing here replaces that
refresh for a queued bar or a long silent leg. That is G8 H2, promoted (§8), and §5 risk (2). A
refresh written into the tracked record instead would restage it on every tick and move
`lease-utc`, which `--landed` grades stop lines against (§8 F3). A dead probe reads UNKNOWN,
announced, and is treated as fresh, which declines a take-over rather than inviting one, as the
file's clock did (AC21).

### The resume matrix, re-keyed

Evaluated after `check_asks_pinned`, the `--scheduled` refusals and the recorded-terminal refusal,
all unchanged, in this order. "Clock" is `check_lease_fresh`, and only a record carrying `lease-utc`
reaches a row that names it. "No lease" is a record carrying none, whose rows grade
`build_folder_age` against `RESUME_STALE_BOUND` (§8 F13). "Working" is any non-terminal phase but
HELD, a LANDING the derivation leaves at LANDING included.

| Record | Caller and clock | `--resume` |
|---|---|---|
| recorded terminal | any | unchanged: nothing to resume, and check 26 with an id |
| LANDING derived LANDED, not observed | an id, on a branch where the landing's own `--landed` does not run | nothing to resume, naming the record's run branch; writes nothing (S8) |
| LANDING derived LANDED, not observed | an id | RE-BIND: `write_lease`, staged, old and new values printed, whatever the clock or session (S8) |
| LANDING derived LANDED, not observed | no id | nothing to resume, as today |
| LANDING, observed in the landed log | any | nothing to resume and never the lander, whatever the remote answers; never `presumed-stopped` |
| HELD, condition unmet | any | `still held`, writes nothing |
| HELD, `lease-utc` after `held-at`, clock fresh, another session and keepalive | an id | refuses 58: a take-over recorded its lease and has not yet moved the phase |
| HELD, otherwise | an id, or none | take-over; with no id the status block, then check 59 |
| working | the recorded keepalive | the holder: writes nothing, unless the record has no `lease-utc` or names another session or pid than the harness exposes, when `write_lease` records it and stages |
| working | a new id, the recorded session, which is not `absent` | the holder's process restarted: take-over through `run_takeover`; refuses 58 first when the recorded pid is alive and is not `CLAUDE_PID` |
| working, no lease, build-folder age unanswerable | a new id, or none | the status block, then check 57, as unit 4 built it |
| working, no lease, build folder inside the bound | a new id with `--replaces` naming the recorded keepalive | the holder replaces its job, through the `--replaces` block of the leased row below: `write_lease`, staged, all six facts recorded; `--replaces` naming another id refuses 58 |
| working, no lease, build folder inside the bound | any other new id, or none | the status block, then check 59 naming the folder's age, `--keepalive-id`, and `--replaces` with the recorded keepalive |
| working, no lease, build folder past the bound | an id, or none | `presumed-stopped`, announced as a record with no lease: take-over; with no id the status block, then check 59 |
| working, clock fresh | a new id with `--replaces` naming the recorded keepalive | the holder replaces its job: `write_lease`, staged; `--replaces` naming another id refuses 58 |
| working, clock fresh or unknown | a new id, another session | refuses 58: a live session drives this slug |
| working, clock fresh or unknown | no id | the status block, then check 59 |
| working, clock stale | an id | `presumed-stopped`, announced: take-over |
| working, clock stale | no id | the status block, then check 59 naming `--keepalive-id` |

The leaseless rows of the retired matrix do NOT collapse into the clock rows (§8 F13, G8 M3).
`write_lease` writes the six facts together, so a record with no `lease-utc` names no session
either: `--liveness` grades it UNBOUND, the tick never acts on it, and the one clock that belongs to
its run, rather than to whichever worktree calls, is the newest commit touching its build folder,
which unit 4 §8 F8 chose. Only the bound moves, from the retired `resolve_lease_bound` to
`RESUME_STALE_BOUND`. Its holder is still the first working row. The no-lease `--replaces` row is
new: it is how a holder whose scheduler lists another job than the record names takes the one lease
record, which is this build's own Rollout (G8 M2). No second `--replaces` branch is written, so the
row adds no `fail` branch. "Observed" is `read_landed_observation` naming the commit
`read_landing_commit` returns for this record, so an observation left by an earlier run of the same
slug never marks a new landing.

### The relaunched session

The resume tick launches `claude -p --resume <session>`: the SAME session, whose first turn appends
to the transcript `--liveness` reads before that session reaches `--resume <slug> --keepalive-id
<new>`. A freshness test alone would therefore read the run live and refuse the relaunch at check
58: the measured shape above, reached through a different signal. So the same-session row carries no
freshness test, and it goes through `run_takeover`, because an unwatched relaunch is exactly where
the mandate must be re-verified and interrupted acts named. The tick's own trigger and the matrix's
staleness are now the same function over the same bound, so a different session reaching `--resume`
after a STALE verdict meets the take-over row. The pid refusal is what stops two live processes of
one session: the tick kills the recorded pid's tree before it launches, so its relaunch passes, and
a hand-started second copy while the first still runs does not.

### HELD in the three actors

`print_liveness` (`tools/unattended/unattended.sh:5509`) sets `state=held` from the recorded phase it
already reads through `read_recorded_phase`, before the finished-unstamped test, and the verdict chain
at `:5578` gains `HELD` after `FINISHED-UNSTAMPED`. `checkStop` in `tools/unattended/stop-guard.js`
returns an allow with reason `held` on that verdict, directly after the `terminal` row at `:137`, so a
held session's stop is allowed before `background-tasks` is consulted and no block is spent on it.
The tick's case at `tools/unattended/resume-tick.sh:269` gains a `HELD` arm printing its own skip,
`skip · HELD · its restart is the durable schedule --hold printed, never this tick`, before the
generic verdict skip. A HELD verdict would fall to that generic skip anyway; the named arm is what
makes the reason readable in the scheduler's log. Each of the three actors reads the copy of the
record in the worktree it runs in. One answer per slug across worktrees is G8 B1's, promoted (§8),
and nothing in this section claims it.

### The pushed landing, re-bound, and the tolerance it needs

The re-bind row sits inside `verb_resume`'s derived-terminal branch at `:5746`. Past
`refuse_if_terminal --recorded` at `:5745`, a non-terminal recorded phase whose derived phase is
terminal can only be LANDING read LANDED, so the row needs no second phase read and `check 39`'s
recorded-phase allow-list is unchanged. It carries no identity test. Nothing is left to drive but the
observation, so the double drive the matrix exists to stop cannot happen there, and a freshness test
would refuse `fail 55`'s own remedy minutes after a push, while the landing commit still keeps the
clock fresh (§8 F7).

The row re-binds only on a branch where that landing's own `--landed` runs (G8 M5). Under
`in-place` that is the record's run branch: its `run-branch` fact, which `--preflight` writes on
both anchors whenever HEAD is a branch, or, on a record preflighted before that fact existed, its
`branch-ref`. Under `primary` it is also the default branch, because that mode's lander runs there
and `fail 55` fires there. HEAD's branch is read with `git symbolic-ref -q HEAD` and compared with
the fact as a full ref. From any other branch the row prints nothing to resume, names the record's
run branch and writes nothing. A re-run build's fresh worktree is the case this closes. Under
`in-place` its previous record stays LANDING until the next `--preflight` retires it, the
keepalive's first tick is issued before that `--preflight`, and a re-bind there would stage the
previous run's record and make that `--preflight` refuse at check 2 (§5 risk 4). A re-run that
checks out the landed run's own branch again is not covered by this, and stays §5 risk (4). A
record naming neither branch fact re-binds as before and says the re-bind was not scoped, because
refusing there would refuse `fail 55`'s own remedy on the population that carries no branch fact.
The scope is this row's alone. It is not an identity test (§8 F7), and it is not the per-slug
answer across worktrees that G8 B1 asks for.

`check_lease_only_diff <file>` holds when `git diff -U0 HEAD -- <file>` changes only lines of the six
lease facts, added, removed or rewritten. `read_landing_commit` replaces its byte-equality test at
`tools/unattended/lib-unattended.sh:823` with that predicate; the phase line and every other byte
must still match a HEAD copy reading LANDING, so a staged or uncommitted LANDING still has no landing
commit. `check_clean` gains an optional run-state file argument exempting that file when the
predicate holds for it, and only `verb_landed`'s `primary` branch passes it, at `:4028`. Neither
`run_hold`'s clean check nor `--preflight`'s passes it, so both still refuse a lease-only difference
at check 2 (§5 risk 4, AC8).

### The read-back under in-place, and the observation

`check_keepalive_reaped <slug> <file>` is the block at `:4029` to `:4077`, moved whole: the `fail 53`,
`fail 54` and `fail 55` texts, the `lease-utc` age test and the three `unchecked` announcements are
unchanged. The in-place branch at `:4008` calls it first, before `observe_anchor`; the `primary` branch
calls it where the block stood. Defined directly above `verb_landed`, the moved branches keep their
line order among the other branches of checks 53, 54 and 55, none of which is pinned.

On a derived LANDED the in-place branch appends `<utc> landed <landing sha> on <ref> at <tip sha>`
to `landed.<slug>.log` in the `unattended` directory under the git common dir, where the retired file
lived, so every worktree on the node reads it. The tick walks every worktree, and a worktree whose
HEAD carries the landed record is any that later merged the default branch. The directory is resolved
by `resolve_landed_log` with `rev-parse --git-common-dir`, the derivation `resolve_lease_path` used,
which therefore moves rather than multiplies; `check 32` counts the per-worktree `rev-parse --git-dir`
literal, and its header states it cannot see this spelling
(`tools/unattended/check-unattended.sh:4938`). An unwritable log is a NOTE, as the file rewrite was,
and leaves the landing FINISHED-UNSTAMPED until `--landed` is re-run. AC10 lands from one linked
worktree and reads from a second, because in a main worktree `rev-parse --git-dir` and
`--git-common-dir` answer one directory, and a per-worktree log would pass there unseen (G8 M6).

### Where the text goes

Every figure below is PINNED, measured at `285701d5` on node `d` with a greedy re-wrap at 100 columns
of each touched paragraph.

| Carrier | Edit | Bytes | Lines |
|---|---|---|---|
| protocol, template and render | the `LEASE_STALE_AFTER` key-table row at `tools/unattended/PROTOCOL.template.md:487`, removed | −138 | −1 |
| protocol | "The nineteen verb entries" becomes "The verb entries", at `:445` | −9 | 0 |
| protocol | "with its own id, refreshing the lease, then `--audit`" loses its middle clause, at `:388` | −22 | 0 |
| protocol | the stop-guard refuses a turn end "while the run is non-terminal and not `HELD`", at `:394` | +15 | 0 |
| protocol | the absent-owner default: "…builds the next READY unit, aborts with a code, or holds with `--hold`.", at `:408` | +21 | 0 |
| verb carrier, template and render | `--liveness` gains `HELD` in its verdict list | +8 | 0 |
| verb carrier | `--resume` rewritten as quoted below, dropping the refusal list `UNATTENDED-STOPS.md` §11 already carries and the "only restart" clause the merge resolver flagged as readable against the tick | −93 | −1 |
| dossier | the three lease sentences at `memory/map/features/unattended.md:84`, `:91` and `:102`, below | −13 | 0 |
| kickoff manifest | the correction at `memory/guides/SESSION-KICKOFF.md:219`, pruned | negative | −4 |
| stop contract, template and render | §7 and §8 rewritten, below | not greater | not greater |

The protocol nets −133 bytes and −1 line, and its curation-debt row stays exactly as wide as it was.
The `--resume` entry, at 800 bytes in 9 lines against 893 in 10:

> - `--resume` — re-enters the run from the run-state file; must agree with `--status`. With
>   `--keepalive-id <id>` it applies the resume matrix: the holder's own id writes nothing, while a
>   take-over, `--replaces`, the holder's restarted process and a pushed landing not yet observed
>   re-record keepalive, session and pid and stage the record; refused on a recorded terminal.
>   `--scheduled <held-at>` marks it as the restart a DURABLE schedule issued. It refuses, numbered
>   and before any write, unless the exact hold that schedule was filed for is still the record's
>   state, and on success the take-over runs unchanged, still requires the session's own
>   `--keepalive-id`, and writes `scheduled` rather than `manual` on its history row.
>   `UNATTENDED-STOPS.md` §8 and §11 are the contract.

The dossier's three edits read: "its prompt runs `--resume --keepalive-id`, then `--audit`"; "The
LEASE is the run-state file's facts, judged fresh by `--liveness`, which reads `HELD` as its own
verdict, so a resume tells orientation from take-over."; and "In-place `--landed` only observes, and
logs that;". The dossier stands at 20234 of its 20480-byte cap, so these are the whole of its change.

The two "its four" comments stop counting the driver's bound keys, a count unit 27's `GATE_WALL`
moves again. The library's, at `tools/unattended/lib-unattended.sh:71`, reads "the resume tick
reads its knobs through this function, and the driver its bound keys, so it lives where both source
it"; the tick's, at `tools/unattended/resume-tick.sh:76`, reads "exactly as the driver reads its
bound keys". The driver's usage line for `--resume`, at `tools/unattended/unattended.sh:11`, ends
"with the id, the resume matrix decides who drives".

The stop contract's §7 keeps its heading and says what the one-lease-record table above says: the
lease is the run-state facts, its presence is `lease-utc`, its identity the keepalive, its freshness
`--liveness`'s over `RESUME_STALE_BOUND`, and nothing refreshes it. It loses the file-format block,
the released and absent paragraphs, the refresh paragraph and the two-term bound, which together are
the 2010 bytes over 36 lines at `tools/unattended/STOPS.template.md:145`. §8's table becomes the
matrix above. §9 step 5 says the lease facts are recorded; §4's third precondition names the
`keepalive` fact alone; §12 says the observation is logged; the title drops "per-slug". The contract
stands at 29105 bytes in 441 lines, and AC14 reads it against its parent.

The Skill carries no size row, and it changes where S11 says. Its tick paragraph at
`tools/unattended/SKILL.template.md:29` rewrites the check-51 sentence so that it names every
refusal a tick issued before `--preflight` meets. `--resume` names check 10 when no run-state file
exists, or check 26 on a re-run build whose previous record is recorded terminal. Under `in-place`,
where a landed record stays LANDING until the next `--preflight` retires it, `--resume` prints
nothing to resume and `--audit` then refuses at check 51 (G8 M5, AC23). The merge skeptic's text
dropped that last case, and it is gov's own landing mode. The paragraph also replaces the sentence
claiming the tick refreshes the lease with this one: for the holder the first act
writes nothing, because whether a run is live is derived from what `--liveness` reads, which this
very tick moves, so the act is there to refuse a session that no longer holds the slug before the
second act runs. The what-wakes paragraph at `:75` has the stop-guard refuse a turn end "while the
run is non-terminal and not HELD". The Resume rule at `:835` keys on the `keepalive` fact alone and
adds that a session the harness resumed, the one the `session` fact names, relaunched by the tick or
restarted by hand, whose scheduler no longer lists that job, schedules a new one and resumes with
its id. The paragraph at `:876` leads "**What that `--resume` records.**" and opens "The take-over
`--resume` above", as the merge skeptic proposed. Placements 2 and 3 at `:1001` read "Under
`primary`"; a new in-place placement renders and commits the record on the run branch before the
lander's `--prepare`; and "no path gains a commit it did not have" is scoped to `primary`.

### Inventory

| Identifier | Kind | Cell, and the lexicon answer at writing |
|---|---|---|
| `derive_last_move` | driver function | `sh.function`: OK, leads with `derive` |
| `check_keepalive_reaped` | driver function | `sh.function`: OK, leads with `check` |
| `resolve_landed_log` | driver function | `sh.function`: OK, leads with `resolve` |
| `read_landed_observation` | driver function | `sh.function`: OK, leads with `read` |
| `write_landed_observation` | driver function | `sh.function`: OK, leads with `write` |
| `check_lease_only_diff` | library function | `sh.function`: OK, leads with `check` |
| `LM_NEWEST`, `LM_SOURCE`, `LM_DEAD`, `LM_TRANSCRIPT`, `LO_SHA`, `LO_UTC` | driver globals | no shell variable cell is declared |
| `held` | stop-guard reason and `--liveness` state | a value, beside `terminal` |
| `HELD` | `--liveness` verdict | a value, beside `TERMINAL` |
| `landed.<slug>.log` | a file under the git common dir | beside the lander marker that directory already holds |

`check_lease_fresh` keeps its name and changes its argument from a slug to a run-state file. No
retired name sits on a lexicon pin: each was asked with `--suggest` and each answered OK, so deleting
them moves no pin row.

### Migration

The population holding a lease file is MEASURED EMPTY on the only node that runs this branch's
driver: on node `d`, 2026-09-22, the git common dir holds no `unattended` directory at all. The kit is
unreleased, so no adopter holds one either. A file left anywhere else is inert, because nothing reads
it, and no shim ships (§8 F12). A run that held one keeps what every `--preflight` on the merged
driver also wrote, the run-state facts, and a record with neither is a pre-lease record whose holder
takes the one lease record at its first matching-id resume, or at its first `--replaces` resume when
its scheduler lists another job than the record names. This build's own run is such a record, and
it is the second case (§4 Rollout, §10).

### Rollout

The unit lands inside this build's own run, and the Rollout does not assume that the record names
the job the run holds. Measured on node `d` on 2026-09-22 (§10), the run-state file records
`keepalive: 00c7d786` and no `session`, `pid` or `lease-utc`, while the scheduler lists `b5b0b444`
as the run's live keepalive. So once the unit lands, the orchestrator reads its scheduler's listing,
compares it with the record's `keepalive` fact, and makes one of two calls.

- When the two match, `--resume <slug> --keepalive-id <that id>` takes the holder row and records
  the six facts.
- When they differ, as they do at writing, the call is
  `--resume <slug> --keepalive-id <live id> --replaces <recorded id>`. It takes the no-lease
  `--replaces` row while the build folder is inside the bound, and the no-lease take-over row past
  it, and either records the live id with the six facts. The same call without `--replaces` is
  refused at check 59 inside the bound, naming `--replaces` and the recorded id.

This is the orchestrator's own act, made because it knows it holds the run. The Skill's Resume
section cannot know that: it sends a session whose scheduler does not list the recorded job down the
take-over path, which inside the bound meets that check-59 refusal and stops. So the Rollout does
not rely on that section for its first resume.

Either way the run-state file is staged and rides the next records commit. From then on the
stop-guard and the tick bind that session, which is main's dark landing lighting up as its contract
says it should (§8 F9). Gov's take-over bound moves from the retired 7200 seconds to
`RESUME_STALE_BOUND`'s declared 5400. That records commit also gives every worktree branched after
it a copy of those facts, which the tick grades on that worktree's own clocks until
`TOOL-dDerivedDocket-62` lands (G8 B1, §8). This Rollout claims nothing about those copies.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/lib-unattended.sh` ·
`tools/unattended/stop-guard.js` · `tools/unattended/resume-tick.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/kit.toml` ·
`tools/unattended/.unattended.conf.example` · `.unattended.conf` ·
`tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` ·
`tools/unattended/STOPS.template.md` · `memory/guides/UNATTENDED-STOPS.md` ·
`tools/unattended/VERBS.template.md` · `memory/guides/UNATTENDED-VERBS.md` ·
`tools/unattended/SKILL.template.md` · `.claude/skills/unattended/SKILL.md` ·
`memory/map/features/unattended.md` · `memory/guides/SESSION-KICKOFF.md` · `memory/DECISIONS.md` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/stop-guard.test.sh` ·
`tools/unattended/resume-tick.test.sh`

### Alternatives rejected

- Keeping the lease file and re-keying main's actors onto it. It is the second record the ruling
  retires, and the tick cannot stand off it, because the tick trusts only a lease the INDEX holds.
- A `refreshed` fact in the run-state file. It restages a tracked file on every tick, dirties the tree
  `--hold` requires clean, and moves the stop-line age test `--landed` depends on.
- Passing `--replaces <recorded keepalive>` in the tick's payload. The tick reads that id from the
  record, so any session could pass it, and `--replaces` would stop meaning the holder.
- `--hold` re-recording `session` and `pid` as `absent`. The ruled direction is the carve-outs, and a
  HELD record should still say which session held it.
- Committing the pushed landing's re-bind. HEAD then leaves the pushed tip, which both landing modes
  read as not landed.

## 5. Production-readiness checklist

- security — The identity rows trust the caller's own keepalive id and the harness environment's
  `CLAUDE_CODE_SESSION_ID` and `CLAUDE_PID`, all readable by any session on the node, so the lease
  still prevents an accidental second driver and not a malicious one, as the HELD unit's §5 states.
  The no-lease `--replaces` row trusts the recorded keepalive, which the record prints, exactly as
  the no-lease holder row always has (unit 4 §8 F11). It is a deliberate act naming the job being
  retired, which an accidental second driver has no reason to pass. The tick passing `--replaces`
  on every relaunch, which §4 rejects, would pass it for every session, which is the difference.
  The landed log carries validated shapes only, is written by one verb, and decides only whether a
  landing reads finished. The tolerance names six fact lines, and a difference anywhere else keeps
  the landing commit unfound.
- perf / scale — `--status` and `--resume` on a leased working record now pay `--liveness`'s clock,
  and on a record with no lease the one `git log` of `build_folder_age` they paid before. PINNED,
  node `d` 2026-09-22: `--liveness` over the scratch fixture took 0.68 s with no gate logs and 2.60 s
  with 90, the count this worktree's git dir holds, at one `stat` spawn per log. The tick's first act
  pays it every ten minutes.
- error / empty / loading states — A dead clock probe reads UNKNOWN and declines a take-over,
  announced (AC21). A record with no lease whose build-folder age is unanswerable refuses at check
  57, as unit 4 built it. An unwritable landed log is a NOTE and leaves the landing
  FINISHED-UNSTAMPED until `--landed` is re-run. Every refusal still writes nothing.
- observability — `state: held` and `verdict: HELD`; `state: terminal` for an observed in-place
  landing; the stop-guard's `held` sidecar reason; the tick's `skip · HELD` decision; and `--status`'s
  `presumed-stopped` naming the one bound, beside its `landed · observed` line.
- risks — (1) A holder whose transcript does not derive and which moves nothing for
  `RESUME_STALE_BOUND` is presumed stopped, after 5400 s in gov where the file allowed 7200. (2) One
  bar leg running past the bound with no other signal reads stale; the longest leg recorded is
  1565 s, measured 2026-08-23 and cited in `AGENTS.md`. A bar waiting in the turnstile queue writes
  no gate log at all, and its wait may reach 7200 s against gov's 5400: that is G8 H2, open here and
  promoted (§8). (3) The landing re-bind admits any session that passes an id on a branch where the
  landing's own `--landed` runs. (4) An in-place landing whose lease was re-bound leaves a
  lease-only staged difference, which the next `--preflight` in that worktree refuses at check 2
  until the file is restored from HEAD. (5) A landing observed on another node is not in this
  node's log, and the tick stands off it by `host`. (6) A leased record's clock is the calling
  worktree's, so a dead holder whose worktree other work keeps moving reads fresh until that work
  stops. The no-lease rows keep the build-folder scope (§8 F13), and the leased clock's reach across
  worktrees is G8 B1's (§8).
- testing — The arms §7 names, each staged RED in the pass and executed once at VERIFYING under
  attribution; the direct observations in §6 are fixture runs of the driver, the hook and the tick.
- migration — §4 Migration: a population measured empty, no shim, and a pre-lease record taking the
  one lease record at its holder's first matching-id or `--replaces` resume.
- user docs — The stop contract's §7, §8, §9 and §12, the verb carrier's two entries, the protocol's
  §5 and §7 lines, the Skill's tick, what-wakes, Resume and Record-the-run text, and the dossier.

## 6. Acceptance criteria

- **AC1** — When `grep -cE '^[^#]*(resolve_lease_path|read_lease|write_lease_taken|write_lease_refreshed|write_lease_released|remove_lease|resolve_lease_bound|write_lease_for_record|RB_LEASE_)' tools/unattended/unattended.sh`
  runs at the build commit it prints 0, counting code lines only so a comment recording the retirement
  is not a reader, and after every fixture run of AC3 to AC11 and AC21 to AC23,
  `find "$(git rev-parse --git-common-dir)" -name '*.lease'` inside the fixture prints nothing.
  Red when: a reader or a writer of the file survives, so a second record answers who drives the slug
  beside the run-state facts; or a verb still writes one.
- **AC2** — When `grep -c 'LEASE_STALE_AFTER'` runs over `tools/unattended/unattended.sh`,
  `tools/unattended/check-unattended.sh`, `tools/unattended/kit.toml`,
  `tools/unattended/.unattended.conf.example`, `.unattended.conf`,
  `tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md`,
  `tools/unattended/STOPS.template.md`, `memory/guides/UNATTENDED-STOPS.md` and the driver suite,
  each prints 0 at the build commit.
  Red when: a declaration survives without its key-table row, the `undocumented` or `proj_extra` half
  of check 22's join, or the row survives without a declaration, its `phantom` half.
  permission: the join itself is check 22 of the `unattended kit gate` leg over the real tree,
  observed at the VERIFYING bar; the greps are this pass's direct check.
- **AC3** — Take the authorized fixture at a working phase with lease facts naming session `S`,
  keepalive `k1` and a dead pid, and touch `S`'s transcript under `CLAUDE_CONFIG_DIR` so `--liveness`
  reads `verdict: LIVE`. With `CLAUDE_CODE_SESSION_ID=S`, `--resume <slug> --keepalive-id k2` prints
  `lease replaced`, records `k2` and prints no check 58. With the recorded pid replaced by a live
  process that is not `CLAUDE_PID`, the same call refuses at check 58 naming both pids, and the
  run-state file is byte-unchanged; with `CLAUDE_CODE_SESSION_ID=T` it refuses at check 58, unchanged.
  Red when: the tick's relaunch — the same session, a new keepalive, a clock its own first turn moved —
  meets the fresh-lease refusal and spends its attempts, as measured at `285701d5`; or two live
  processes of one session can both drive the run.
  fixture: an authorized record at a pinned BASE over a local bare remote, the shape the driver
  suite's prologue builds; the tree holds none outside that suite.
- **AC4** — When the fixture of AC3's third call has its commit and its transcript aged past
  `RESUME_STALE_BOUND`, `--liveness` prints `stale: yes`, `--status` prints `presumed-stopped`
  naming the number `--liveness` prints as `stale-bound`, and `--resume --keepalive-id C` from
  session `T` takes the run over; aged back inside the bound, `--liveness` prints `stale: no` and
  that resume refuses at check 58.
  Red when: the matrix and `--liveness` grade a leased record's staleness with two predicates or two
  bounds, so one fixture reads STALE to the tick and fresh to the matrix, which is the measured state
  at `285701d5`. A record with no lease is §8 F13's and AC22's: `--liveness` grades it UNBOUND and
  the tick never acts on it.
- **AC5** — When `--liveness` runs over the minimal HELD fixture of §4 with its commit aged past
  `RESUME_STALE_BOUND`, it prints `state: held` and `verdict: HELD`, and every other key it printed at
  `285701d5`, in the same order.
  Red when: a HELD record reads `state: live` and `verdict: STALE`, the verdict the tick acts on.
  fixture: a scratch repository holding a conf and one committed run-state file with the six lease
  facts and no remote, as §4's measurement used.
- **AC6** — When `node tools/unattended/stop-guard.js` is fed a Stop payload whose `session_id` is the
  HELD fixture's `session` fact, it exits 0, prints nothing on stdout, and its sidecar line carries
  `"reason":"held"`; the same fixture moved to BUILDING is blocked with `run-open`.
  Red when: a session that held correctly and stops is told to `--plan` or `--abort`, as measured at
  `285701d5`, so the Skill's "file nothing and stop" and the hook contradict each other.
- **AC7** — When `bash tools/unattended/resume-tick.sh --repo <fixture> --dry-run` runs over the HELD
  fixture it prints a `skip · HELD` decision and no `resumed ·` decision; over the same fixture moved
  to BUILDING it prints `resumed · attempt 1`.
  Red when: the tick's STALE row reaches a paused run and would kill and relaunch it, as measured at
  `285701d5`.
- **AC8** — Take a fixture whose committed LANDING record is pushed to a local bare `origin`, so
  `--status` prints `phase LANDED (derived:`, with `session` `S`, checked out on the record's run
  branch. `CLAUDE_CODE_SESSION_ID=T`
  `--resume <slug> --keepalive-id k2` records `session` `T` and `keepalive` `k2`, prints both changes
  and stages the file, and `--status` still prints `phase LANDED (derived:`. Then under
  `LANDER_MODE="primary"` a `--landed` from `T` passes check 2 and check 55, and under `in-place` it
  reaches the derivation. The same fixture with its `witness` hand-edited instead prints `not
  committed as it stands`, and under `primary` the re-bound fixture with its `witness` also
  hand-edited refuses `--landed` at check 2. The tolerance reaches no other caller of the clean
  check: `--preflight` over the re-bound fixture, and `--hold` over a working fixture that meets
  every other precondition and differs from HEAD only in a re-recorded `session` line, each still
  refuse at check 2.
  Red when: `fail 55`'s remedy writes nothing, as measured at `285701d5`; or the re-bound record stops
  deriving LANDED, so in-place `--landed` refuses at check 80 and `primary` at check 2; or the
  tolerance admits a difference outside the six lease-fact lines, at either of its two sites; or the
  clean check exempts the whole run-state file, so a hand-edited witness reaches `primary`
  `--landed`'s terminal write; or the exemption reaches another caller than that branch, so
  `--preflight` or `--hold` accepts a dirty tree.
- **AC9** — Under `in-place`, on AC8's fixture with `session` `S` and a hand-written stop-guard
  sidecar line in phase LANDING younger than `lease-utc`: a listing naming the recorded keepalive makes
  `--landed` refuse at check 53; a listing free of it prints `keepalive-reaped: checked` before
  `phase LANDED (derived`; and `CLAUDE_CODE_SESSION_ID=T` refuses at check 55.
  Red when: the in-place branch returns before the read-back, the state measured at `285701d5`, where
  a session the record does not name landed with no `keepalive-reaped` line at all.
- **AC10** — Run AC9's passing in-place `--landed` in a LINKED worktree `W1` of the fixture, made
  with `git worktree add`, because in the main worktree `git rev-parse --git-dir` and
  `--git-common-dir` answer one directory. Afterwards `landed.<slug>.log` sits in the `unattended`
  directory under the path `git -C W1 rev-parse --git-common-dir` prints, holding one line naming the
  landing commit, and no file of that name exists under the path `git -C W1 rev-parse --git-dir`
  prints. From a second linked worktree `W2`, detached at the landing commit: `--liveness` prints
  `state: terminal` and `verdict: TERMINAL`; `node tools/unattended/stop-guard.js` allows with reason
  `terminal`; `--status` prints `landed · observed by --landed at`; and with `origin` pointed at a
  missing path and the commits aged past the bound, `--status` prints no `presumed-stopped` while
  `--resume --keepalive-id C` prints nothing to resume and writes nothing. A later LANDING record of
  the same slug, whose log names only the earlier landing commit, still reads `FINISHED-UNSTAMPED`.
  Red when: the observation lands where `--liveness` in another worktree does not read it, the
  per-worktree sidecar directory §8 F5 rejected included, so every observed in-place landing is
  blocked as unstamped and relaunched by the tick in every worktree but the one that landed it, as
  measured at `285701d5`; or an earlier run's observation marks a new landing finished.
  fixture: AC8's pushed LANDING record, landed from `W1` and read from `W2`, both linked worktrees
  of the one scratch repository.
- **AC11** — On a working fixture whose lease facts name `k1`, session `S` and pid `P`,
  `CLAUDE_CODE_SESSION_ID=S CLAUDE_PID=P` with `--resume <slug> --keepalive-id k1` exits 0 and
  `git status --porcelain` prints nothing; with `CLAUDE_PID=Q` it records pid `Q` and stages; and a
  fixture with no `lease-utc` resumed with its recorded keepalive gains all six lease facts.
  Red when: the tick's first act restages the record every ten minutes and moves `lease-utc`, pushing
  `--landed`'s stop-line test back; or a pre-lease holder stays invisible to the hooks.
- **AC12** — On a HELD fixture whose condition is met, `--resume --keepalive-id C` from another
  session takes it over and returns the phase to `held-from`; with `lease-utc` hand-set after
  `held-at` and a fresh clock, the same call refuses at check 58 and writes nothing. On a working
  fixture whose `keepalive` is `k1` and whose common dir holds a leftover `<slug>.lease` reading
  `taken … keepalive k9`, the migration case, `--hold --reaped k9` refuses at check 56 naming `k1`,
  `--resume --keepalive-id k1` takes the holder row and writes nothing, and the leftover file is
  byte-unchanged.
  Red when: a take-over's crash window admits a second take-over; or a verb still reads the retired
  file, so a leftover id outranks the fact, which is what `run_hold` does at `285701d5`.
- **AC13** — At the build commit each of these prints 0 for each file it reads, and each counts at
  least 1 at the build commit's first parent, so none passes unmoved:
  `grep -c 'REPLACES the lease' tools/unattended/VERBS.template.md`;
  `grep -c 'nineteen verb entries' tools/unattended/PROTOCOL.template.md` and
  `grep -c 'refreshing the' tools/unattended/PROTOCOL.template.md`;
  `grep -c 'Then record the new id' tools/unattended/SKILL.template.md`; `grep -c` over
  `tools/unattended/STOPS.template.md` for `per-slug`, `released <iso>`, `refreshes the lease`,
  `in the lease first` and `keeps what it saw in the lease`; `grep -c` over
  `memory/map/features/unattended.md` for `refreshes the lease`, `per-slug LEASE` and
  `in the lease`;
  `grep -c 'its four' tools/unattended/lib-unattended.sh tools/unattended/resume-tick.sh`; and
  `grep -c 'with the id, the lease is replaced' tools/unattended/unattended.sh`. Beside those, the
  Skill's tick paragraph names check 10, check 26 and check 51, the last for an in-place previous
  record; the `--liveness` entry of `tools/unattended/VERBS.template.md` lists `HELD` among its
  verdicts; `grep -c 'non-terminal and not' tools/unattended/SKILL.template.md` and the same over
  `tools/unattended/PROTOCOL.template.md` each print at least 1; the Skill names no `LEASE` line;
  and placements 2 and 3 of Record the run name `primary`, beside an in-place placement that names
  `--prepare`.
  Red when: a carrier still describes the retired file, its refresh or its release, the unscoped
  placements or the wrong refusal, so an agent following it acts on a mechanism that is gone; or a
  pass edits only the phrases a narrower witness list named, and the stop contract's §8 table, the
  matrix agents actually follow, still describes the retired file; or the tick paragraph drops the
  check-51 case, which gov's in-place landing makes true (AC23).
  permission: that each render is byte-identical to its template is the `unattended skill wiring` and
  `unattended kit gate` legs over the real tree, observed at the VERIFYING bar.
- **AC14** — When `git cat-file -s` and `wc -l` read `tools/unattended/PROTOCOL.template.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md`, `tools/unattended/STOPS.template.md`,
  `memory/guides/UNATTENDED-STOPS.md`, `tools/unattended/VERBS.template.md`,
  `memory/guides/UNATTENDED-VERBS.md`, `memory/map/features/unattended.md` and
  `memory/guides/SESSION-KICKOFF.md` at the build commit and at its first parent, no build-commit
  figure is greater than its parent's; the guide and dossier caps are resolved from the lines of
  `tools/memory-tree/check-memory-hygiene.sh` that declare `GUIDE_CAP_BYTES` and
  `DOSSIER_CAP_BYTES`, never retyped; and the protocol's delta is −133 bytes and −1 line.
  Red when: an addition is written without its trim, so a carrier already under a curation-debt
  waiver grows; or the reading is taken against the figures in this spec instead of the parent commit.
  figure: the −133 is PINNED at `285701d5`; the not-greater test is derived at the build commit.
- **AC15** — When the orchestrator's attributed unattended run at VERIFYING reports on the driver,
  stop-guard and resume-tick suites, it reads `verdict clean`, with the new arms §7 names among the
  executed ones and every retargeted lease-file assertion executed; and each floor S13 names reads,
  at the build commit, its figure at the first parent plus exactly the assertions this unit's new
  blocks carry, read with `git show` at both.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it; or a
  lease-file assertion was deleted rather than retargeted, so the executed count falls while the
  floors rose by the new arms alone; or a floor is left where the arms found it, or moves by a
  number no new arm accounts for.
  permission: the three suites are held kit suites on no bar leg, so they run in the orchestrator's
  attributed VERIFYING run and never in this pass.
- **AC16** — When `memory/DECISIONS.md` is read, its TOOL heading carries one row keyed by
  `TOOL-dDerivedDocket-61` that names the one lease record, the one bound and the HELD carve-outs,
  within the 300-character entry budget.
  Red when: the retirement of a lease design two units specified ships with no record of it.
- **AC17** — When `grep -c 'one lease and one restart path' memory/guides/SESSION-KICKOFF.md` runs at
  the build commit it prints 0.
  Red when: the correction keeps overriding a claim this unit made true, so every kickoff front-loads
  a trap that no longer exists.
- **AC18** — When `grep -c 'KIT_UNATTENDED_VERSION=1.29'` runs over `tools/unattended/unattended.sh`
  and over `tools/unattended/check-unattended.sh`, each prints 1, and `grep -c 'unattended@1.29'`
  over every kit template prints what it printed at the parent; and the added lines of every shipped
  kit file this unit edits carry no `tools/<kit>/` literal.
  Red when: the unit moves a version the unreleased kit does not owe, or a new line spells a path the
  install-prefix ban forbids.
  permission: the ban's own verdict is the `install-prefix (shipped surface)` leg, observed at
  VERIFYING.
- **AC19** — When `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` runs for each
  name §4's Inventory mints, each prints `OK`; the new check-58 branch has an arm; and the rows of
  `memory/project/unarmed-branches.txt` for `tools/unattended/unattended.sh`, which pin checks 9, 27,
  29, 49 and 56, are unchanged, with no `fail 9`, `fail 27`, `fail 29`, `fail 49` or `fail 56` line
  added to or removed from the driver.
  Red when: a name leads with a verb the table does not carry, so the naming leg reds; or a pinned
  row's ordinal moves under it unnoticed.
  permission: the armed-or-pinned verdict is the `harness arms (fail branches armed or pinned)` leg,
  observed at VERIFYING.
- **AC20** — Take AC4's fixture with its commit and its transcript aged past `RESUME_STALE_BOUND`,
  so `--liveness` prints `stale: yes`, and plant one file under that worktree's
  `<git-dir>/gate-logs/` dated inside the bound, the trace a bar still running leaves each time a
  leg lands. `--liveness` then prints `stale: no`, `last-move-source: gate-log` and
  `verdict: LIVE`; `--status` prints no `presumed-stopped`; and `--resume --keepalive-id C` from
  session `T` refuses at check 58 and leaves the run-state file byte-unchanged. With that file
  dated past the bound as well, `--liveness` prints `stale: yes` again. The arm is staged RED by a
  copy of `derive_last_move` with its gate-log term removed, under which the planted file changes
  nothing and the first reading stays `stale: yes`.
  Red when: a bar that runs past the bound while its legs keep landing in the run's own worktree
  reads STALE, so the resume tick kills a healthy bar and a second session takes the slug over
  mid-bar, which is the half of the property `TOOL-dDerivedDocket-27` AC9 guarded that this unit
  carries; or the gate-log term drops out of the one clock unnoticed, because AC4 ages the commit
  and the transcript only. This criterion does not observe a bar queued at the turnstile or a leg
  silent past the bound, which write no gate log (G8 H2), nor a read from a second worktree (G8 B1).
  Both are promoted (§8), and neither is claimed here.
  fixture: AC3's authorized record, with the gate-log file planted by hand under that worktree's
  own git dir and dated with `touch -d`, so no bar runs.
  permission: the arm is written and staged RED in the pass; the driver suite that executes it is a
  held kit suite on no bar leg, so it runs in the orchestrator's attributed VERIFYING run beside
  AC15's arms and never in this pass.
- **AC21** — Take AC3's fixture, whose lease facts name session `S`, and put first on `PATH` a
  `date` that exits 1, the dead-clock stub the driver suite already stages. With
  `CLAUDE_CODE_SESSION_ID=T`, `--resume <slug> --keepalive-id C` prints the UNKNOWN announcement,
  `the lease age is UNKNOWN on this node`, refuses at check 58 and leaves the run-state file
  byte-unchanged; `--resume <slug>` with no id refuses at check 59; and `--status` prints its own
  UNKNOWN line and no `presumed-stopped`. The arm is staged RED by a copy of `check_lease_fresh`
  that returns 1 on a dead `derive_last_move`, under which the first call takes the run over. The
  arm is new: the suite's leaseless dead-clock arm keeps its `fail 57` expectation, because
  `build_folder_age` stays (§8 F13), and moves only in how its fixture is made leaseless (S13).
  Red when: a dead clock probe reads as stale, so a probe that answered nothing invites a take-over
  of a live run; or it reads as fresh with no announcement, so the reassuring zero `print_liveness`
  refuses with `fail 52` is accepted in silence by the matrix. Every other criterion here runs a live
  clock, and none reaches return 2.
  fixture: AC3's authorized record, with the `date` stub on `PATH` for these three calls only.
  permission: the direct fixture runs above are this pass's check; the arm that repeats them is
  written and staged RED in the pass, and the driver suite that executes it is a held kit suite on no
  bar leg, so it runs in the orchestrator's attributed VERIFYING run beside AC15's arms.
- **AC22** — Take AC3's authorized record with its six lease-fact lines deleted, so it carries no
  lease and its `keepalive` fact names `k1`, and commit the deletion dated past `RESUME_STALE_BOUND`
  with `GIT_COMMITTER_DATE`; then commit one file outside the build folder at the present time, so
  HEAD's committer epoch is fresh. `--status` prints `presumed-stopped` naming `NO LEASE` and the
  build folder's age, and `--resume <slug> --keepalive-id C` announces `presumed-stopped` and takes
  the run over. With the deletion committed at the present time instead, three calls in this order:
  `--resume <slug> --keepalive-id k2` prints the status block and refuses at check 59, naming the
  folder's age, `--replaces` and `k1`, and the run-state file is byte-unchanged;
  `--resume <slug> --keepalive-id k3 --replaces k9` refuses at check 58 and writes nothing; and
  `--resume <slug> --keepalive-id k2 --replaces k1` records `k2` with all six lease facts, stages
  the file and prints `keepalive replaced`.
  Red when: a record with no lease is judged by the calling worktree's unrelated activity, so an
  abandoned pre-lease run, the population backlog row `TOOL-aReapedTicket-5` names, is refused as
  live for as long as that worktree stays busy, which unit 4 §8 F8 decided against; or a pre-lease
  holder whose scheduler lists another job than the record names has no path but waiting out the
  bound, which is this build's own Rollout (§4).
  fixture: AC3's authorized record, its lease facts removed and the build-folder commit dated by
  `GIT_COMMITTER_DATE`, so no clock is faked.
  permission: the direct fixture runs above are this pass's check; the arm that repeats them is
  written and staged RED in the pass, and the driver suite that executes it is a held kit suite on no
  bar leg, so it runs in the orchestrator's attributed VERIFYING run beside AC15's arms.
- **AC23** — Take AC8's pushed LANDING fixture under `LANDER_MODE="in-place"`, its landing not yet
  observed, and switch to a new branch at the pushed tip, as a re-run build's fresh worktree is.
  `--resume <slug> --keepalive-id k3` prints nothing to resume and names the record's run branch,
  `git status --porcelain` prints nothing, and `--audit <slug>` then refuses at check 51. Back on
  the record's run branch the same call re-binds, as AC8 reads; and under `LANDER_MODE="primary"`,
  on a default branch fast-forwarded to the pushed tip, it re-binds too.
  Red when: the re-bind writes on any branch, so a re-run build's keepalive tick, issued before its
  `--preflight`, stages the previous run's record and that `--preflight` refuses at check 2; or the
  scope drops the default branch under `primary`, so `fail 55`'s remedy writes nothing where that
  mode's lander runs; or the Skill's check-51 sentence, which S11 keeps, is false.
  fixture: AC8's, with one extra branch. The record's run branch is its `run-branch` fact, or its
  `branch-ref` where the fixture's `--preflight` wrote only that.
  permission: the direct fixture runs above are this pass's check; the arm that repeats them is
  written and staged RED in the pass, and the driver suite that executes it is a held kit suite on no
  bar leg, so it runs in the orchestrator's attributed VERIFYING run beside AC15's arms.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `codebase-map coverage + freshness` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `kickoff-manifest ratchet` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · the same-session relaunch over a fresh and a stale clock, two live processes of one session, another session on a fresh clock, the holder with and without a moved identity, a pre-lease holder, the HELD crash window, the pushed unobserved landing under both modes with its witness-edit and clean-check controls, the re-bind from another branch, the in-place read-back's three refusals and its pass, the observation written in one linked worktree and read from a second, with an unanswered remote and with an earlier run's line, a fresh gate log keeping an otherwise aged run out of STALE, a dead clock on a leased record, and a record with no lease beside an unrelated fresh commit, with its replaces path; every lease-file assertion retargeted one for one · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2`, each raised by exactly the new arms' assertions, counted off their blocks; a retargeted assertion moves neither
New arm: `tools/unattended/stop-guard.test.sh` · a HELD record bound to the payload's session, and an observed in-place landing read from a linked worktree other than the one that landed it · `FLOOR_ASSERTIONS`, raised by exactly the new arms' assertions, counted off their blocks
New arm: `tools/unattended/resume-tick.test.sh` · a HELD record with a stale clock, and an observed in-place landing with a stale clock, in a worktree other than the one that landed it · `FLOOR_ASSERTIONS`, raised by exactly the new arms' assertions, counted off their blocks

Every floor follows this build's practice, set by the CLOSED units 25, 30, 49 and 54: a unit raises
its suite's executed-assertion floor by exactly the arms it adds, derived from the blocks rather than
read off a run, which this pass does not make. The driver's new arms are written in region two, so
`FLOOR_SHARD_1` does not move.

The `kickoff-manifest ratchet` leg is named because S15 edits the manifest; its `last-audit` re-stamp
is the post-merge audit this build already takes after each wave, as `c361e347` did.

## 8. Open questions

- **F1 — the declared-wall unit re-terms a bound this unit deletes.** `TOOL-dDerivedDocket-27` S11
  moved `resolve_lease_bound`'s first term to the pinned `gate-backstop`, at order 28, two steps
  before this unit's 30. Options: (a) rescope S11 out of that unit before it builds, because the
  one bound here needs no bar term, the gate-log clock moving during a bar; (b) keep S11 and let this
  unit delete what it built; (c) carry the backstop into `RESUME_STALE_BOUND`'s derived default.
  RESOLVED (agent, 2026-09-22, delegated), decided by the orchestrator: (a). It amends another
  unit's scope, so it was the orchestrator's rescope act under the delegated M3 rule and not this
  spec's. (b) builds a term this unit deletes two orders later, and (c) would put the bar's whole
  backstop, about eight hours in gov, into the bound the tick and the matrix act on, when the
  gate-log term moves as a running bar's legs land. That unit's rev-8 withdraws S11 and AC9, the one
  criterion that observed only S11, and keeps the pinned fact, by which `gates-green` still bounds
  `$GATE_CMD`; this unit's consumes-from edge to it existed for S11 alone and is removed. The
  property AC9 guarded, that a bar running past the bound never reads stale and a second session
  cannot take the slug over mid-bar, passed to this unit, through the gate-log term of
  `derive_last_move`. No existing criterion observed that term, because AC4 ages the commit and the
  transcript only, so AC20 does, over a fixture. Its residual is §5 risk (2): one leg that itself
  runs past the bound with no other signal still reads stale. The G8 audit found the premise false
  for a bar that queues, because the turnstile's wait writes no gate log, so AC20 observes legs
  landing in the run's own worktree and nothing more. The queued or silent bar and the
  second-worktree read are G8 H2 and G8 B1 below, both promoted, and re-opening this fork on the
  corrected premise goes with H2.
- **F2 — which bound survives.** RESOLVED (agent, 2026-09-22, delegated): `RESUME_STALE_BOUND`,
  within the ruling's one staleness bound, because three actors already read it and `--liveness`
  prints it as `stale-bound`; gov's take-over bound moves from 7200 to 5400 seconds.
- **F3 — what the one record's freshness reads.** Options: (a) `--liveness`'s four-signal clock;
  (b) a `refreshed` fact in the run-state file; (c) a refresh file. RESOLVED (agent, 2026-09-22,
  delegated): (a). (b) restages a tracked file every tick and moves `lease-utc`, and (c) is the file
  the ruling retires.
- **F4 — how the tick's relaunch avoids the fresh refusal.** Options: (a) a same-session row through
  `run_takeover`, refused only for two live processes; (b) `--replaces <recorded keepalive>` in the
  tick's payload; (c) freshness alone. RESOLVED (agent, 2026-09-22, delegated): (a), which is how the
  ruling's third item is met. (c) fails because the relaunched session moves the recorded transcript
  before it resumes, and (b) lets any session name the holder's job.
- **F5 — where the in-place observation goes once the file retires.** Options: (a) an append-only
  `landed.<slug>.log` under the git common dir; (b) the per-worktree sidecar directory; (c) derive
  TERMINAL from the offline test alone; (d) nowhere. RESOLVED (agent, 2026-09-22, delegated): (a).
  (d) is measured to block and relaunch every landed in-place run, (c) drops the post-push enforcement
  the ruling's fifth item restores, and (b) is invisible to the other worktrees the tick walks.
- **F6 — how a re-bound landing still lands.** Options: (a) a tolerance confined to the six
  lease-fact lines in `read_landing_commit` and the `primary` clean check; (b) commit the re-bind;
  (c) `--landed` restores the record from HEAD. RESOLVED (agent, 2026-09-22, delegated): (a). (b)
  moves HEAD off the pushed tip, and (c) is a verb silently reverting a write.
- **F7 — the landing re-bind's identity test.** RESOLVED (agent, 2026-09-22, delegated): none, as the
  merge skeptic proposed, because a freshness test would refuse `fail 55`'s remedy just after a push.
  The branch scope the row gained in the G8 fold (M5) is not an identity test: it names where the
  re-bind runs, which is where that landing's `--landed` runs, and not who runs it.
- **F8 — extending `fail 55`'s text with `--replaces`.** RESOLVED (agent, 2026-09-22, delegated): no.
  With F4 and F7 its present remedy works wherever it fires, and the extension would name a flag that
  no row it reaches needs.
- **F9 — does a pre-lease holder's resume record the facts.** RESOLVED (agent, 2026-09-22,
  delegated): yes, which is main's contract that `--resume --keepalive-id` re-records the lease. The
  consequence is §4 Rollout: this build's own orchestrator becomes bound to the stop-guard and the
  tick at its first resume after the merge. Which resume that is, matching-id or `--replaces`, is
  read from the scheduler at the time and never assumed (G8 M2).
- **F10 — the in-place Record-the-run placement.** Options: (a) a records commit on the run branch
  before `--prepare`; (b) none. RESOLVED (agent, 2026-09-22, delegated): (a), the merge skeptic's
  proposal, because the in-place order forbids every later commit.
- **F11 — the DECISIONS row.** RESOLVED (agent, 2026-09-22, delegated): it ships. Under BUILD-METHOD
  M6 condition 3 it makes this pass run alone, which `TOOL-dDerivedDocket-60` records: at an order of
  its own, in a step holding no other unit. The status header's order 30 is also
  `TOOL-dDerivedDocket-32`'s, which is G8 M9. This spec does not move its own order: the orchestrator
  re-declares the orders, as it did for `TOOL-dDerivedDocket-27` at that spec's rev-7.
- **F12 — a shim for leftover lease files.** RESOLVED (agent, 2026-09-22, delegated): none. The
  population is measured empty on the node that runs this driver, and a leftover file is inert.
- **F13 — the clock of a record with no lease.** Options: (a) keep unit 4 §8 F8's clock, the age of
  the newest commit touching the record's build folder, with its leaseless rows, against
  `RESUME_STALE_BOUND`; (b) collapse those rows into `check_lease_fresh`'s clock, superseding F8 and
  naming the regression; (c) scope the commit term of the one clock to the build folder for every
  record. RESOLVED (agent, 2026-09-22, delegated): (a), folding G8 M3. (b) refuses an abandoned
  pre-lease record as live for as long as the calling worktree's unrelated commits, writes or bars
  keep it inside the bound. That is the population backlog row `TOOL-aReapedTicket-5` names, which F8
  cited, and `--liveness` grades the same record UNBOUND, so the refusal's "a live session drives
  this slug" would be false. (c) changes the commit term `--liveness` reads for every record, the
  clock the ruling names, and the leased clock's per-worktree reach is G8 B1's, promoted below. (a)
  keeps `build_folder_age`, so AC1 no longer greps for it, and keeps the one bound, because the
  leaseless rows read `RESUME_STALE_BOUND` where they read `resolve_lease_bound`. A leased record's
  clock is the ruled `--liveness` clock unchanged, and its widening by unrelated activity in the
  calling worktree is §5 risk (6).
- **G8 B1 — the lease is one copy per worktree, so the tick and the matrix grade one slug many
  times.** Promoted at the G8 bounded exit to `TOOL-dDerivedDocket-62`, which consumes from this unit
  and builds after it. Nothing in this unit closes it. Every criterion here runs in one worktree,
  except AC10, which crosses two only for the landed log and the terminal readings it produces; the
  re-bind's branch scope (§4, G8 M5) is that one row's. Until that unit lands, a sibling worktree
  whose HEAD carries a copy of this build's record with the Rollout's facts is graded on its own
  clocks by the tick, `--liveness` and the matrix.
- **G8 H1 — the same-session row shadows `--replaces`, so the holder can no longer replace its own
  job.** Promoted at the G8 bounded exit to `TOOL-dDerivedDocket-63`, which consumes from this unit
  and builds after it. Nothing in this unit closes it: the matrix keeps the row order rev-2 wrote,
  S13's retarget reaches lease-file assertions only, and AC15 is read at VERIFYING, after that unit
  has built. The no-lease `--replaces` row (§4, G8 M2) is not shadowed, because a record with no
  lease carries no `session` for the same-session row to match.
- **G8 H2 — the turnstile queue writes no gate log, so F1's premise is false and a healthy queued
  bar reads STALE.** Promoted at the G8 bounded exit to `TOOL-dDerivedDocket-64`, which consumes from
  this unit and builds after it, with the re-opening of F1 on the corrected premise. Nothing in this
  unit closes it: AC20 observes legs that land and never a queue, and §5 risk (2) names the queued
  bar as open.

## 9. Revision log

- rev-1 · 2026-09-22 · initial draft, grounded on `285701d5` and on the merge findings for the lease,
  HELD and landing seam, with every defect the brief names re-measured over scratch fixtures.
- rev-2 · 2026-09-22 · §2 S3 S7 · §3 · §6 AC20 · §7 · §8 F1 · F1 RESOLVED by the orchestrator under
  the delegated M3 rule, as option (a): `TOOL-dDerivedDocket-27` withdraws its S11 and AC9 and
  keeps the pinned `gate-backstop` fact for `gates-green`. The consumes-from edge to unit
  27, which existed only for S11, is removed, and every other edge is kept. New AC20 observes, over
  a fixture, the property unit 27's AC9 guarded: a bar running past the bound is kept out of STALE
  by its gate logs, and a clock without its gate-log term reds it. S3 and S7 name AC20, §7's driver
  arm line carries it, and §3's non-goal on wiring a declared wall into `RESUME_STALE_BOUND` now
  names it as F1's declined option (c).
- rev-3 · 2026-09-22 · §2 S1 S2 S3 S7 S8 S10 S11 S13 · §3 · §4 · §5 · §6 AC1 AC4 AC8 AC10 AC13 AC20
  AC21 AC22 AC23 · §7 · §8 F1 F7 F9 F11 F13 · §10 · G8 spec audit round 1 fold of its nine mediums.
  B1, H1 and H2 are NOT folded: §8 records each as promoted at the G8 bounded exit to
  `TOOL-dDerivedDocket-62` (B1), `-63` (H1) and `-64` (H2), and no S-item or criterion here claims
  to close one. §3's edges, §4's lease-record paragraph, HELD section and Rollout, F1 and AC20 now
  say what this unit does not carry, where rev-2 claimed it.
  - M1 is unit 27's and is folded there, in that spec's next revision.
  - M2: the Rollout reads the scheduler and compares it with the record's `keepalive` before it
    relies on the holder row, and prescribes `--replaces <recorded id>` when they differ, as they do
    at writing (`00c7d786` recorded, `b5b0b444` live, §10). A new no-lease `--replaces` row makes
    that call land; the no-lease inside-the-bound refusal names `--replaces`; AC22 observes both.
  - M3: §8 F13 keeps unit 4 F8's build-folder clock for a record with no lease rather than
    superseding it unrecorded. `build_folder_age` stays (S1, AC1), the leaseless rows return to the
    matrix against `RESUME_STALE_BOUND` (S2, S7, §4), and AC22 reads an old leaseless record beside a
    fresh unrelated commit as `presumed-stopped`.
  - M4: AC21 grades the UNKNOWN third state over a dead `date`, and S3 names it.
  - M5: the re-bind row runs only on a branch where the landing's own `--landed` runs (S8, §4, F7),
    so a re-run's pre-preflight tick writes nothing; the Skill keeps its check-51 case beside checks
    10 and 26 (S11), AC13 drops the `check 51` zero-count, and AC23 observes it.
  - M6: AC10 lands from one linked worktree and reads from a second, asserting where the log is.
  - M7: AC8 grades the clean-check half at both sites, where it must hold and where it must not.
  - M8: AC13 witnesses the retired-lease phrases the audit named in the stop contract, the
    protocol and the dossier, the verb carrier's `HELD`, the driver's `--resume` usage line and the
    "its four" comments, whose replacement texts §4 now quotes.
  - M9: F11 states that this unit runs alone at an order of its own; the header's order 30 is
    unchanged, because the orchestrator re-declares the orders.
  - After each fold the spec was grepped for every other passage relying on what it changed, and S13,
    §5 and §7 moved with them.
- rev-4 · 2026-09-22 · order re-declared from 30 to 31 in the status header only, derived
  from the §3 edges: the G8 bounded exit promoted TOOL-dDerivedDocket-62, -63 and -64 to run
  after TOOL-dDerivedDocket-61, so this unit runs at order 31, alone. No criterion, design or edge moved.
- rev-5 · 2026-09-22 · §3 · §2 S13 · §6 AC15 · §7 · three hands-off edges added, to
  `TOOL-dDerivedDocket-62`, `-63` and `-64`, answering the consumes-from each declares on this
  unit, each payload naming only what that spec's own text names. S13, AC15 and §7 raise each
  suite's executed-assertion floor by exactly the arms this unit adds, counted off their blocks and
  never read off a run, where rev-4 moved none: the practice the CLOSED units 25, 30, 49 and 54 set.
  The §4 matrix, the order, every other edge and every other criterion are unchanged.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "decide whether the session holding a run is alive from
the newest of several clocks"` returns no seam for this work: its candidates are name-stem matches in
the runlog and govkit Python kits, and its header prints `unscanned layers: .sh`, the layer this unit
is written in. So no existing seam fits in the corpus the probe reads. The seams this unit extends
were found by reading source: `read_tree_clocks`, already shared by `print_audit` and
`print_liveness`; `print_liveness`'s gate-log and transcript clocks; `write_lease`;
`read_landing_commit` and `check_pid_alive` in the library; and the lander marker's common-dir
resolution in `verb_landed`.

Recall terms used: `python tools/memory-recall/query.py "which record decides who drives an
unattended run, and how is staleness of the holding session judged" --terms "lease keepalive session
pid take-over resume matrix liveness stale bound held stop-guard resume-tick"`. It returned the
backlog row for the reap read-back, the stop contract's matrix, `TOOL-dDerivedDocket-40`'s declined
reacher column, the kickoff manifest correction S15 prunes, and the spec that added the lease facts.

Live run state, measured for §4 Rollout (G8 M2) on node `d` on 2026-09-22 at `07997375`:
`memory/builds/dDerivedDocket/RUN.md` records `keepalive: 00c7d786` and carries no `session`, `pid`
or `lease-utc` fact, and the git common dir holds no `unattended` directory. The run's live
keepalive, read from the scheduler's listing by the orchestrator and relayed in its fold brief the
same day, is `b5b0b444`. The two ids differ, so the Rollout's `--replaces` call is the one that
applies at writing.
