# TOOL-dDerivedDocket-61 — one lease record, and HELD known to every out-of-session actor

**Status:** SPECCED · rev-2 · 2026-09-22 · node d · Tier-2 · base 285701d5 · streams tooling · order 30

<!-- gen:spec-records -->

*No record names this unit.*

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
  `write_lease_refreshed`, `write_lease_released`, `remove_lease`, `resolve_lease_bound`,
  `build_folder_age` and `write_lease_for_record`; `stage_or_fail`'s call to the last; the
  `RB_LEASE_SLUG` and `RB_LEASE_ID` globals, `run_bounded`'s refresh and the three verbs that set
  them (`verb_preflight`, `run_takeover`, `verb_close`); `verb_preflight`'s take-or-refresh block;
  `run_takeover`'s `write_lease_taken`; the `remove_lease` calls in `verb_landed` and `verb_abort`;
  `run_hold`'s `read_lease` and `write_lease_released`; and `verb_status`'s `LEASE —` line. No verb
  reads or writes a `.lease` file. Observed by AC1.
- **S2** ONE staleness bound. `LEASE_STALE_AFTER` leaves the driver (its default constant, its
  initialiser and its `read_bound_key` call), `tools/unattended/check-unattended.sh` (initialiser and
  conf allow-list), `tools/unattended/kit.toml`'s `optional_keys`, the example conf, gov's
  `.unattended.conf`, the protocol key table (template and render), the stop contract and the driver
  suite's three `mkconf` declarations. `RESUME_STALE_BOUND` is the one bound: the resume matrix and
  `--status` act on the staleness `--liveness` grades against it. Observed by AC2 and AC4.
- **S3** One clock. `derive_last_move` is extracted verbatim from `print_liveness`: the two tree
  clocks of `read_tree_clocks`, the newest gate log under the worktree's git dir, and the recorded
  session's transcript. `print_liveness` calls it and keeps its `fail 52` on a dead probe;
  `check_lease_fresh` is re-keyed onto a run-state file and calls it, returning 0 fresh, 1 stale and
  2 unknown as before. Observed by AC4, AC5 and AC20.
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
  branch when the recorded pid is alive and is not `CLAUDE_PID`. Observed by AC3, AC4, AC11, AC12
  and AC20.
- **S8** `verb_resume` RE-BINDS the run-state lease for a pushed landing `--landed` has not yet
  observed: with an id, on a record whose recorded phase is `LANDING` and whose derived phase is
  `LANDED`, it runs `write_lease`, stages the record and prints the old and new values, which restores
  the remedy `fail 55` names. So that the re-bound record still lands, `read_landing_commit` in
  `tools/unattended/lib-unattended.sh` and `--landed`'s `primary` clean check both treat a difference
  from HEAD confined to the six lease-fact lines as no difference, through one new lib predicate,
  `check_lease_only_diff`. Observed by AC8.
- **S9** The keepalive reap READ-BACK runs under `LANDER_MODE=in-place`. The block at
  `tools/unattended/unattended.sh:4029` moves, with its message texts and check numbers unchanged,
  into `check_keepalive_reaped`, defined directly above `verb_landed`, and both branches call it
  before the anchor round-trip. Observed by AC9.
- **S10** The in-place landing OBSERVATION, which lived in the retired file as `released <iso>
  landed`, moves to an append-only line in `landed.<slug>.log`, in the `unattended` directory under
  the git COMMON dir. `write_landed_observation` appends it when an in-place `--landed` derives
  `LANDED`; `read_landed_observation` reads it for `--liveness` (S4), for `--status` and for the
  matrix's observed-landing row. It is not a lease: no reader asks it who drives the slug. Observed
  by AC10.
- **S11** The carriers say what the code now does. `UNATTENDED-STOPS.md` §7, §8, §9 step 5, §4
  item 3, §12 and its title describe the one lease record; `UNATTENDED-VERBS.md` gains `HELD` in
  `--liveness` and rewords `--resume`; the protocol takes the five edits §4 prices; the Skill's tick
  paragraph drops the check-51 note and the refresh claim, its what-wakes paragraph carves HELD out,
  its Resume section loses the `LEASE` line rule and the doubled `--resume`, and its Record-the-run
  placements are scoped by landing mode; the `unattended` dossier's three lease sentences, the
  driver's `--resume` header line, and the library's and the tick's "its four" comments follow. Every
  render is re-rendered. Observed by AC13.
- **S12** NO capped carrier grows: the protocol template and render, the stop contract and the verb
  carrier with their renders, the `unattended` dossier and `memory/guides/SESSION-KICKOFF.md` each
  end the pass no larger in bytes or in lines than they began it, funded by the trims §4 names.
  Observed by AC14.
- **S13** The suite arms follow the code. Every assertion in the driver suite that reads or writes a
  lease file is retargeted to the run-state facts or the landed log, one for one, so the executed
  count does not fall; the one-line `--status` counts stop filtering the retired `LEASE —` line; the
  new arms §7 names are written and each is staged RED. No floor moves in the pass. Observed by AC15.
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
  works from every place that refusal fires (§8 F8).
- A one-spawn gate-log clock. `derive_last_move` keeps `print_liveness`'s one `stat` per log
  verbatim; §5 prices the cost and a single read is a follow-up.
- Wiring a declared gate wall into `RESUME_STALE_BOUND`, §8 F1's declined option (c). A bar that
  runs past the bound while its legs keep landing stays fresh through its gate logs instead, which
  AC20 observes.
- The sidecar-root derivation `check 32` counts, the durable restart, the `--scheduled` refusals and
  `TOOL-dDerivedDocket-40`'s declined matrix-reacher column. None moves.
- Any kit version constant. The unattended kit stands unreleased at 1.29 on this branch.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-4` — HELD, `run_hold`, the resume matrix with its
  refusal-before-write property, `run_takeover`'s step order and the tri-state `check_lease_fresh`.
  This unit re-keys the matrix and keeps every row's property.
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
  leaves that directory in place.

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
| does this record carry a lease | a `lease-utc` fact is present; a record without one predates the run-state lease |
| who holds it | the `keepalive` fact; for the same-session row, the `session` fact against `CLAUDE_CODE_SESSION_ID` |
| is its holder alive | `check_lease_fresh`: `derive_last_move` for the recorded session, against `RESUME_STALE_BOUND` |
| is it released | the phase: HELD is the released state, and a terminal is the removed one |

Freshness is DERIVED, never written. The retired file was refreshed by every writing verb, by the
start of `run_bounded` and by the holder's tick, and every one of those moves a signal `--liveness`
already reads: a dirty write or a commit, a gate log per leg, and the session's own transcript, which
a tick's turn appends to. A refresh written into the tracked record instead would restage it on
every tick and move `lease-utc`, which `--landed` grades stop lines against (§8 F3). A dead probe
reads UNKNOWN, announced, and is treated as fresh, which declines a take-over rather than inviting
one, as the file's clock did.

### The resume matrix, re-keyed

Evaluated after `check_asks_pinned`, the `--scheduled` refusals and the recorded-terminal refusal,
all unchanged, in this order. "Clock" is `check_lease_fresh`; "working" is any non-terminal phase but
HELD, a LANDING the derivation leaves at LANDING included.

| Record | Caller and clock | `--resume` |
|---|---|---|
| recorded terminal | any | unchanged: nothing to resume, and check 26 with an id |
| LANDING derived LANDED, not observed | an id | RE-BIND: `write_lease`, staged, old and new values printed, whatever the clock or session (S8) |
| LANDING derived LANDED, not observed | no id | nothing to resume, as today |
| LANDING, observed in the landed log | any | nothing to resume and never the lander, whatever the remote answers; never `presumed-stopped` |
| HELD, condition unmet | any | `still held`, writes nothing |
| HELD, `lease-utc` after `held-at`, clock fresh, another session and keepalive | an id | refuses 58: a take-over recorded its lease and has not yet moved the phase |
| HELD, otherwise | an id, or none | take-over; with no id the status block, then check 59 |
| working | the recorded keepalive | the holder: writes nothing, unless the record has no `lease-utc` or names another session or pid than the harness exposes, when `write_lease` records it and stages |
| working | a new id, the recorded session, which is not `absent` | the holder's process restarted: take-over through `run_takeover`; refuses 58 first when the recorded pid is alive and is not `CLAUDE_PID` |
| working, clock fresh | a new id with `--replaces` naming the recorded keepalive | the holder replaces its job: `write_lease`, staged; `--replaces` naming another id refuses 58 |
| working, clock fresh or unknown | a new id, another session | refuses 58: a live session drives this slug |
| working, clock fresh or unknown | no id | the status block, then check 59 |
| working, clock stale | an id | `presumed-stopped`, announced: take-over |
| working, clock stale | no id | the status block, then check 59 naming `--keepalive-id` |

The four leaseless rows of the retired matrix collapse: a record with no `lease-utc` is judged by the
same clock, and its holder is the first working row. "Observed" is `read_landed_observation` naming
the commit `read_landing_commit` returns for this record, so an observation left by an earlier run of
the same slug never marks a new landing.

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
makes the reason readable in the scheduler's log.

### The pushed landing, re-bound, and the tolerance it needs

The re-bind row sits inside `verb_resume`'s derived-terminal branch at `:5746`. Past
`refuse_if_terminal --recorded` at `:5745`, a non-terminal recorded phase whose derived phase is
terminal can only be LANDING read LANDED, so the row needs no second phase read and `check 39`'s
recorded-phase allow-list is unchanged. It carries no identity test. Nothing is left to drive but the
observation, so the double drive the matrix exists to stop cannot happen there, and a freshness test
would refuse `fail 55`'s own remedy minutes after a push, while the landing commit still keeps the
clock fresh (§8 F7).

`check_lease_only_diff <file>` holds when `git diff -U0 HEAD -- <file>` changes only lines of the six
lease facts, added, removed or rewritten. `read_landing_commit` replaces its byte-equality test at
`tools/unattended/lib-unattended.sh:823` with that predicate; the phase line and every other byte
must still match a HEAD copy reading LANDING, so a staged or uncommitted LANDING still has no landing
commit. `check_clean` gains an optional run-state file argument exempting that file when the
predicate holds for it, and only `verb_landed`'s `primary` branch passes it, at `:4028`.

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
and leaves the landing FINISHED-UNSTAMPED until `--landed` is re-run.

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

The stop contract's §7 keeps its heading and says what the one-lease-record table above says: the
lease is the run-state facts, its presence is `lease-utc`, its identity the keepalive, its freshness
`--liveness`'s over `RESUME_STALE_BOUND`, and nothing refreshes it. It loses the file-format block,
the released and absent paragraphs, the refresh paragraph and the two-term bound, which together are
the 2010 bytes over 36 lines at `tools/unattended/STOPS.template.md:145`. §8's table becomes the
matrix above. §9 step 5 says the lease facts are recorded; §4's third precondition names the
`keepalive` fact alone; §12 says the observation is logged; the title drops "per-slug". The contract
stands at 29105 bytes in 441 lines, and AC14 reads it against its parent.

The Skill carries no size row, and it changes where S11 says. Its tick paragraph at
`tools/unattended/SKILL.template.md:29` replaces the check-51 sentence with the merge skeptic's text
— a tick issued before `--preflight` refuses at its first act, `--resume` naming check 10 when no
run-state file exists or check 26 on a re-run build whose previous record is terminal — and replaces
the sentence claiming the tick refreshes the lease with this one: for the holder the first act
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
takes the one lease record at its first matching-id resume. This build's own run is such a record:
at `285701d5` its run-state file carries `keepalive` and no `session`, `pid` or `lease-utc`.

### Rollout

The unit lands inside this build's own run. The orchestrator's first `--resume <slug> --keepalive-id
<own id>` after the merge records the six facts and stages the run-state file, which rides its next
records commit; from then on the stop-guard and the tick bind that session, which is main's dark
landing lighting up as its contract says it should (§8 F9). Gov's take-over bound moves from the
retired 7200 seconds to `RESUME_STALE_BOUND`'s declared 5400.

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
  The landed log carries validated shapes only, is written by one verb, and decides only whether a
  landing reads finished. The tolerance names six fact lines, and a difference anywhere else keeps
  the landing commit unfound.
- perf / scale — `--status` and `--resume` on a working record now pay `--liveness`'s clock. PINNED,
  node `d` 2026-09-22: `--liveness` over the scratch fixture took 0.68 s with no gate logs and 2.60 s
  with 90, the count this worktree's git dir holds, at one `stat` spawn per log. The tick's first act
  pays it every ten minutes.
- error / empty / loading states — A dead clock probe reads UNKNOWN and declines a take-over,
  announced. An unwritable landed log is a NOTE and leaves the landing FINISHED-UNSTAMPED until
  `--landed` is re-run. Every refusal still writes nothing.
- observability — `state: held` and `verdict: HELD`; `state: terminal` for an observed in-place
  landing; the stop-guard's `held` sidecar reason; the tick's `skip · HELD` decision; and `--status`'s
  `presumed-stopped` naming the one bound, beside its `landed · observed` line.
- risks — (1) A holder whose transcript does not derive and which moves nothing for
  `RESUME_STALE_BOUND` is presumed stopped, after 5400 s in gov where the file allowed 7200. (2) One
  bar leg running past the bound with no other signal reads stale; the longest leg recorded is
  1565 s, measured 2026-08-23 and cited in `AGENTS.md`. (3) The landing re-bind admits any session
  that passes an id. (4) An in-place landing whose lease was re-bound leaves a lease-only staged
  difference, which the next `--preflight` in that worktree refuses at check 2 until the file is
  restored from HEAD. (5) A landing observed on another node is not in this node's log, and the tick
  stands off it by `host`.
- testing — The arms §7 names, each staged RED in the pass and executed once at VERIFYING under
  attribution; the direct observations in §6 are fixture runs of the driver, the hook and the tick.
- migration — §4 Migration: a population measured empty, no shim, and a pre-lease record taking the
  one lease record at its holder's first matching-id resume.
- user docs — The stop contract's §7, §8, §9 and §12, the verb carrier's two entries, the protocol's
  §5 and §7 lines, the Skill's tick, what-wakes, Resume and Record-the-run text, and the dossier.

## 6. Acceptance criteria

- **AC1** — When `grep -cE '^[^#]*(resolve_lease_path|read_lease|write_lease_taken|write_lease_refreshed|write_lease_released|remove_lease|resolve_lease_bound|build_folder_age|write_lease_for_record|RB_LEASE_)' tools/unattended/unattended.sh`
  runs at the build commit it prints 0, counting code lines only so a comment recording the retirement
  is not a reader, and after every fixture run of AC3 to AC11,
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
  Red when: the matrix and `--liveness` grade staleness with two predicates or two bounds, so one
  fixture reads STALE to the tick and fresh to the matrix, which is the measured state at `285701d5`.
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
  `--status` prints `phase LANDED (derived:`, with `session` `S`. `CLAUDE_CODE_SESSION_ID=T`
  `--resume <slug> --keepalive-id k2` records `session` `T` and `keepalive` `k2`, prints both changes
  and stages the file, and `--status` still prints `phase LANDED (derived:`. Then under
  `LANDER_MODE="primary"` a `--landed` from `T` passes check 2 and check 55, and under `in-place` it
  reaches the derivation. The same fixture with its `witness` hand-edited instead prints `not
  committed as it stands`.
  Red when: `fail 55`'s remedy writes nothing, as measured at `285701d5`; or the re-bound record stops
  deriving LANDED, so in-place `--landed` refuses at check 80 and `primary` at check 2; or the
  tolerance admits a difference outside the six lease-fact lines.
- **AC9** — Under `in-place`, on AC8's fixture with `session` `S` and a hand-written stop-guard
  sidecar line in phase LANDING younger than `lease-utc`: a listing naming the recorded keepalive makes
  `--landed` refuse at check 53; a listing free of it prints `keepalive-reaped: checked` before
  `phase LANDED (derived`; and `CLAUDE_CODE_SESSION_ID=T` refuses at check 55.
  Red when: the in-place branch returns before the read-back, the state measured at `285701d5`, where
  a session the record does not name landed with no `keepalive-reaped` line at all.
- **AC10** — After AC9's passing in-place `--landed`, `landed.<slug>.log` in the fixture's common-dir
  `unattended` directory holds one line naming the landing commit; `--liveness` prints
  `state: terminal` and `verdict: TERMINAL`; `node tools/unattended/stop-guard.js` allows with reason
  `terminal`; `--status` prints `landed · observed by --landed at`; and with `origin` pointed at a
  missing path and the commits aged past the bound, `--status` prints no `presumed-stopped` while
  `--resume --keepalive-id C` prints nothing to resume and writes nothing. A later LANDING record of
  the same slug, whose log names only the earlier landing commit, still reads `FINISHED-UNSTAMPED`.
  Red when: the observation lands where `--liveness` does not read it, so every observed in-place
  landing is blocked as unstamped and relaunched by the tick, as measured at `285701d5`; or an earlier
  run's observation marks a new landing finished.
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
- **AC13** — At the build commit, `grep -c 'REPLACES the lease' tools/unattended/VERBS.template.md`,
  `grep -c 'nineteen verb entries' tools/unattended/PROTOCOL.template.md`,
  `grep -c 'check 51' tools/unattended/SKILL.template.md`,
  `grep -c 'Then record the new id' tools/unattended/SKILL.template.md` and
  `grep -c 'per-slug' tools/unattended/STOPS.template.md` each print 0; the Skill's tick paragraph
  names check 10 and check 26; `grep -c 'non-terminal and not' tools/unattended/SKILL.template.md` and
  the same over `tools/unattended/PROTOCOL.template.md` each print at least 1; the Skill names no
  `LEASE` line; and placements 2 and 3 of Record the run name `primary`, beside an in-place placement
  that names `--prepare`.
  Red when: a carrier still describes the retired file, the refresh, the unscoped placements or the
  wrong refusal, so an agent following it acts on a mechanism that is gone.
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
  executed ones and every retargeted lease-file assertion executed.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it; or a
  lease-file assertion was deleted rather than retargeted, so the executed count falls under a floor
  nobody moved.
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
  Red when: a bar that runs past the bound while its legs keep landing reads STALE, so the resume
  tick kills a healthy bar and a second session takes the slug over mid-bar, the property
  `TOOL-dDerivedDocket-27` AC9 guarded before §8 F1 withdrew it there; or the gate-log term drops
  out of the one clock unnoticed, because AC4 ages the commit and the transcript only.
  fixture: AC3's authorized record, with the gate-log file planted by hand under that worktree's
  own git dir and dated with `touch -d`, so no bar runs.
  permission: the arm is written and staged RED in the pass; the driver suite that executes it is a
  held kit suite on no bar leg, so it runs in the orchestrator's attributed VERIFYING run beside
  AC15's arms and never in this pass.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `codebase-map coverage + freshness` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `kickoff-manifest ratchet` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · the same-session relaunch over a fresh and a stale clock, two live processes of one session, another session on a fresh clock, the holder with and without a moved identity, a pre-lease holder, the HELD crash window, the pushed unobserved landing under both modes with its witness-edit control, the in-place read-back's three refusals and its pass, the observation with an unanswered remote and with an earlier run's line, and a fresh gate log keeping an otherwise aged run out of STALE; every lease-file assertion retargeted one for one · no floor moved in the pass
New arm: `tools/unattended/stop-guard.test.sh` · a HELD record bound to the payload's session, and an observed in-place landing · none
New arm: `tools/unattended/resume-tick.test.sh` · a HELD record with a stale clock, and an observed in-place landing with a stale clock · none

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
  gate-log term already moves while a bar runs. That unit's rev-8 withdraws S11 and AC9, the one
  criterion that observed only S11, and keeps the pinned fact, by which `gates-green` still bounds
  `$GATE_CMD`; this unit's consumes-from edge to it existed for S11 alone and is removed. The
  property AC9 guarded, that a bar running past the bound never reads stale and a second session
  cannot take the slug over mid-bar, is now this unit's to deliver, through the gate-log term of
  `derive_last_move`. No existing criterion observed it, because AC4 ages the commit and the
  transcript only, so AC20 does, over a fixture. Its residual is §5 risk (2): one leg that itself
  runs past the bound with no other signal still reads stale.
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
- **F8 — extending `fail 55`'s text with `--replaces`.** RESOLVED (agent, 2026-09-22, delegated): no.
  With F4 and F7 its present remedy works wherever it fires, and the extension would name a flag that
  no row it reaches needs.
- **F9 — does a pre-lease holder's resume record the facts.** RESOLVED (agent, 2026-09-22,
  delegated): yes, which is main's contract that `--resume --keepalive-id` re-records the lease. The
  consequence is §4 Rollout: this build's own orchestrator becomes bound to the stop-guard and the
  tick at its first resume after the merge.
- **F10 — the in-place Record-the-run placement.** Options: (a) a records commit on the run branch
  before `--prepare`; (b) none. RESOLVED (agent, 2026-09-22, delegated): (a), the merge skeptic's
  proposal, because the in-place order forbids every later commit.
- **F11 — the DECISIONS row.** RESOLVED (agent, 2026-09-22, delegated): it ships. Under BUILD-METHOD
  M6 condition 3 it makes this pass run alone, which `TOOL-dDerivedDocket-60` records.
- **F12 — a shim for leftover lease files.** RESOLVED (agent, 2026-09-22, delegated): none. The
  population is measured empty on the node that runs this driver, and a leftover file is inert.

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
