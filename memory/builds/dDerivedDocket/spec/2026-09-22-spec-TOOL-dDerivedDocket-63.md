# TOOL-dDerivedDocket-63 — the holder keeps its own `--replaces`: row precedence in the re-keyed resume matrix

**Status:** SPECCED · rev-2 · 2026-09-22 · node d · Tier-2 · base 07997375 · streams tooling · order 33

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Unit 61 puts its new same-session row above the `--replaces` row of a first-match matrix, so as
specified the holder's own `--replaces` becomes a take-over, and a caller under the recorded session
and the recorded pid, which is the holder's own process or its sub-agent, takes the run over with no
freshness test (finding H1 of the G8 spec audit). Move the `--replaces` row above the same-session
row and admit to that row only a caller whose pid the record does not name, so `--replaces` means the
holder again and the driver suite's second-driver arms keep their verdicts under the one session and
pid its prologue exports.

## 2. Scope (IN)

- **S1** The `--replaces` row is evaluated BEFORE the same-session row, whatever the caller's session
  or pid, at a clock `check_lease_fresh` reads fresh or unknown. Naming the recorded keepalive, it
  runs `write_lease`, stages the record and prints `keepalive replaced`, and never reaches
  `run_takeover`. Naming another id, it refuses at check 58 and writes nothing. Unknown is included
  because `verb_resume` reads `--replaces` inside the branch where a return of 2 has already set
  `ls_fresh=1` (`tools/unattended/unattended.sh:5736`, `:5790-5791`). Unit 61's table writes that row
  "clock fresh" alone, which under this order would leave an unknown-clock `--replaces` from the
  recorded session matching no row. The row names the clock, so only a record carrying `lease-utc`
  reaches it; a record with no lease keeps unit 61's no-lease `--replaces` row, which enters the
  same block and keeps that entry when the block moves (§4). Observed by AC1, AC2 and AC4.
- **S2** The same-session row admits only a caller whose pid the record does not name. When
  `CLAUDE_PID` is set, the `pid` fact is present and is not `absent`, and the two are equal, the
  caller is the recorded process and not a restart. It then meets the rows below the same-session
  row, which carry the freshness test: at a fresh or unknown clock the catch-all check-58 refusal,
  whose text names `--replaces` (`tools/unattended/unattended.sh:5819` at `07997375`), and at a stale
  clock the announced `presumed-stopped` take-over. The catch-all is reached with no new branch, so
  no `fail` call is added. Observed by AC3.
- **S3** New driver-suite arms, each staged RED in the pass. They are the recorded session's
  `--replaces` naming the recorded keepalive under the recorded pid and under another dead pid; the
  same naming another id; the recorded session's new id with no `--replaces` under the recorded pid
  dead, under a live one, and with the clock aged past the bound; and the relaunch control under
  another pid. The driver suite's `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` each rise by exactly the
  assertions these arms carry, counted off their blocks, because they are written in region two
  beside unit 4's lease arms. Observed by AC1, AC2, AC3 and AC4.
- **S4** The existing second-driver arms keep their verdicts under the prologue's single exported
  `CLAUDE_CODE_SESSION_ID=fixture-session` and `CLAUDE_PID=999999999`, and none is given a session of
  its own. The three arms H1 names and unit 28's AC9 id refusal keep the assertions they carry, bar
  the lease-file ones unit 61's S13 retargets: unit 61's order would flip each to a take-over, this
  unit's order makes each hold again, and no unit re-asserts one. The driver suite's leaseless arms
  are not this unit's. Unit 61 keeps `build_folder_age` and its leaseless rows (its §8 F13) and makes
  those fixtures leaseless under its S13, and a record carrying no lease carries no `session`, so
  they reach none of the rows this unit moves and keep their check-59 and check-57 texts; any
  re-assertion they owe is unit 61's. The one arm this unit edits is unit 61's same-session
  relaunch, whose call it moves to a `CLAUDE_PID` the record does not name, the shape the tick's
  relaunch has, keeping every assertion unit 61 wrote. §4 lists every member. Observed by AC4.
- **S5** The stop contract's §8 table, template and render, records S1 and S2 in four rows: the
  `--replaces` row above the same-session row, reading "clock fresh or unknown"; the same-session
  row's caller cell carrying the pid clause and its refusal losing the clause that moved; the
  catch-all's caller cell reading "a new id"; and unit 61's no-lease `--replaces` row, whose pointer
  at the block of the leased row reads "above" where unit 61 wrote "below", since that row now sits
  above it. The net is −15 bytes and no line against unit 61's rows, so the contract does not grow.
  Observed by AC5.
- **S6** The unit's hygiene: no function or other identifier is minted, no `fail` branch is added or
  removed, no row of `memory/project/unarmed-branches.txt` moves, no kit version moves, no added kit
  line spells a kit path literal, and no conf key is added or removed, so no protocol key-table row
  is owed. Observed by AC6.

## 3. Non-goals (OUT)

- The rows this unit does not move. The terminal, landing, re-bind and HELD rows above the working
  rows, the holder row "the recorded keepalive", and unit 61's four no-lease working rows, bar the
  one word S5 names, read as unit 61 specifies them. So does the worktree row
  `TOOL-dDerivedDocket-62` adds above the re-bind, HELD and working rows, which every call here
  passes on the record's own branch.
- The driver suite's leaseless arms, at `tools/unattended/unattended.test.sh:7216`, `:7228` and
  `:7426`, and any re-assertion they owe. They are unit 61's (S4, §4).
- `--replaces` at a stale clock. It keeps meeting the announced take-over, as at `07997375`, where
  `--replaces` is read only inside the fresh branch (§8 F3).
- A harness that exposes no pid. An `absent` pid on either side is no match, so such a caller keeps
  unit 61's same-session reading (§8 F5, §5 risk 1).
- Any refusal text. The recorded process meets the catch-all's existing text, which already names
  `--replaces`.
- Handing the second-driver arms sessions of their own, the review's S13 note (§8 F1).
- A documented first-match check over every table, and the Reacher column. `TOOL-dDerivedDocket-40`
  holds that class OPEN, and the arms S3 adds are this matrix's regression gate (§8 F4).
- The Skill, the protocol and the verb carrier. The Skill's "Replace your OWN job only through
  `--replaces`" (`tools/unattended/SKILL.template.md:843`) and the protocol's RESUME rule
  (`tools/unattended/PROTOCOL.template.md:415`) become true again with no edit, and unit 61's
  `--resume` entry makes no claim about row order.
- The per-slug answer across worktrees and the queued bar's clock, which are B1's and H2's own
  promoted units.
- Unit 61's spec text. Unit 61 builds its §4 table as it states it, the row order H1 names
  included, and that spec is not edited to pre-empt this unit. This unit then changes three of
  those working rows in code, and four in the contract, the fourth by one word (S5).

### Edges

- **consumes-from** `TOOL-dDerivedDocket-61` — the re-keyed matrix this unit re-orders: its
  same-session row with the check-58 branch naming both pids, its `--replaces` row, its no-lease
  `--replaces` row that enters the same block, its catch-all refusal, the stop contract §8 table it
  writes, and its S13 retargets of the lease-file assertions; and its §8 F13, which keeps
  `build_folder_age` and the leaseless rows this unit leaves as they are. Without it there is no
  same-session row to narrow and no table to edit. Its AC15 reads green at VERIFYING only with this
  unit built, because as specified it flips the four arms S4 keeps.
- **consumes-from** `TOOL-dDerivedDocket-4` — `--replaces` as the holder's own path (its §8 F9),
  identity by the keepalive the holder's own scheduler lists (its F3), the refusal-before-write
  property, and its AC6 and AC20 arms at the suite lines §4 names, whose verdicts this unit keeps.
- **consumes-from** `TOOL-dDerivedDocket-28` — its AC9 arm, a `--resume --keepalive-id B` refusal
  over a fresh record under the prologue's one session, which S4 keeps a refusal that reaps nothing.

## 4. Design

### What the finding rests on, at `07997375`

The driver reads `--replaces` only inside the fresh-lease branch of `verb_resume`, at
`tools/unattended/unattended.sh:5790-5812`, ahead of the id comparison at `:5818`. Naming the
lease's id, it records the new keepalive through `write_lease` and prints `keepalive replaced` at
`:5808`, with no remote observation, no mandate re-verify and no history row. A take-over is
`run_takeover` at `:5604`. It re-verifies the authorization, prints `lease replaced` at `:5642`,
appends the ` resume · item ` history row through `park` at `:5648`, and prints `taken over` at
`:5656` or `:5667`. The `taken over` line and the history row are how a reader, and the suite, tell
a take-over from a replacement.

Unit 61 §4 "The resume matrix, re-keyed" lists, for a working record, the same-session row "a new
id, the recorded session, which is not `absent`" ABOVE the `--replaces` row, with its four no-lease
rows between the two, and the first match wins. The same-session row's caller cell does not exclude
`--replaces`. Its only pid test refuses a recorded pid that is alive and is NOT `CLAUDE_PID`. `write_lease` (`:5121`) records the caller's own
`CLAUDE_CODE_SESSION_ID` and `CLAUDE_PID`, so the holder's own later call always carries the recorded
session and, from the same process, the recorded pid.

The driver suite exports one session and one dead pid for every call
(`tools/unattended/unattended.test.sh:409-410`), and `build_hold_fixture` (`:7002`) preflights under
them. To unit 61's matrix, every second-driver call over a fixture that keeps its lease facts is
therefore the recorded session under the recorded, dead, pid, and each one reaches the same-session
row. A fixture the suite makes leaseless carries no `session` fact once unit 61's S13 deletes its
lease-fact lines, so its calls reach unit 61's no-lease rows instead, and this unit moves none of
those.

Measured on node `d` 2026-09-22, PINNED, inside a workflow sub-agent of this build's orchestrator:
`CLAUDE_CODE_SESSION_ID` is the orchestrating session's own id, whose transcript is the one file of
that name in the project's transcript directory. `CLAUDE_PID` names a live `claude.exe`, the nearest
one above the sub-agent's own shell. That it is also the orchestrator's `CLAUDE_PID` is UNVERIFIED,
because the orchestrator's environment was not read. Under either answer, unit 61's same-session row
is reached with a new id: an equal live pid passes its pid test, and only an unequal live pid is
refused.

### The working rows, in their new order

| # | Record and clock | Caller | `--resume` | Change |
|---|---|---|---|---|
| 1 | working | the recorded keepalive | the holder, as unit 61 specifies | none |
| 2 | working, clock fresh or unknown | a new id with `--replaces` naming the recorded keepalive | `write_lease`, staged, `keepalive replaced`; naming another id refuses 58 | moved from below N4 to above row 3; "or unknown" |
| 3 | working | a new id, the recorded session, which is not `absent`, under a pid the record does not name | the restart: take-over; refuses 58 first when the recorded pid is alive | caller narrowed |
| N1 | working, no lease, build-folder age unanswerable | a new id, or none | the status block, then check 57 | none |
| N2 | working, no lease, build folder inside the bound | a new id with `--replaces` naming the recorded keepalive | through row 2's block: `write_lease`, staged, all six facts; naming another id refuses 58 | the block it names now sits above it |
| N3 | working, no lease, build folder inside the bound | any other new id, or none | the status block, then check 59 | none |
| N4 | working, no lease, build folder past the bound | an id, or none | `presumed-stopped`: take-over; with no id the status block, then check 59 | none |
| 4 | working, clock fresh or unknown | a new id | refuses 58, the text naming `--replaces` | "another session" dropped |
| 5 | working, clock fresh or unknown | no id | the status block, then check 59 | none |
| 6 | working, clock stale | an id | `presumed-stopped`, announced: take-over | none |
| 7 | working, clock stale | no id | the status block, then check 59 | none |

Rows 1 to 7 are the leased rows rev-1 of this spec numbered, kept so that every reference below
still names the same row. N1 to N4 are unit 61's no-lease rows, which its rev-3 returned to the
matrix (its §8 F13). They stand where unit 61 puts them, between its same-session row and its
leased clock rows, in unit 61's words, which the cells above abbreviate. Every row of unit 61's
table above row 1, the terminal, landing, re-bind and HELD rows, stands as unit 61 states it, and
so does the worktree row `TOOL-dDerivedDocket-62` adds above the re-bind row, which every call here
passes because each runs on the record's own branch.

The first-match audit H1's left-shift proposes, run once over this table: for each row, the rows
above it whose caller cell also matches its callers.

- Row 2: row 1 matches only a `--replaces` call whose `--keepalive-id` IS the recorded keepalive,
  which row 1 answers as the holder, as unit 61 specifies.
- Row 3: row 2 takes every call carrying `--replaces` at a fresh or unknown clock, which is the
  point of the move; row 1 takes none, because row 3 requires a new id.
- N1 to N4: of the rows above them, row 2 names the clock, which only a record carrying `lease-utc`
  reaches, and row 3 needs a recorded `session`, which a record carrying no lease does not carry,
  because `write_lease` writes the lease facts together. So neither move reaches a record with no
  lease: row 1 still takes its holder, and N1 to N4 answer every other call exactly as unit 61
  specifies. That is why the leaseless arms keep their check-57 and check-59 texts.
- Row 4: N1 to N4 take no record carrying a lease, so what reaches it with a new id is another
  session, the recorded session under the recorded pid, or a record whose session is `absent`. All
  three are refused, and that is the property H1 found missing.
- Row 6: at a stale clock rows 2 and 4 do not match, and row 3 still takes the recorded session
  under another pid, the tick's relaunch. A `--replaces` call and the recorded process each meet
  row 6, as a `--replaces` call does at `07997375`.

In code the change is two edits inside unit 61's working branch. Its `--replaces` block moves above
its same-session block, under the fresh-or-unknown condition. Unit 61 writes no second `--replaces`
branch: its N2 row enters that same block from the no-lease rows, so the move keeps that entry, and
a record with no lease inside the bound still reaches the block through N2 and never through the
clock condition. The same-session condition gains the pid clause below. Row 4 needs no edit in
code, because the catch-all is whatever falls past the rows above it.

### What "a pid the record names" means

The record names the caller's pid when `CLAUDE_PID` is set, the `pid` fact is present and is not
`absent`, and the two are byte-equal. Anything else is a pid the record does not name. A harness
exposing no pid therefore keeps unit 61's reading (§8 F5).

Equality is not a restart, because a restart is a new process. The tick kills the recorded pid's
tree and then launches `claude -p --resume <session>` detached
(`tools/unattended/resume-tick.sh:30-32`, `:319`), and a restart by hand is a new process as well.
What shares both the recorded session and the recorded pid is the process that wrote the lease, or a
sub-agent inside it. A dead pid equal to `CLAUDE_PID` is the suite's fixture, or a number the OS
handed the relaunch, which §5 risk 2 prices.

The recorded process is not refused outright. It meets rows 4 and 6, where the clock decides. A
refusal at every clock would leave a holder whose clock reads stale no way to re-key, because row 2
is read only at a fresh or unknown clock (§8 F2, F3).

### The arms, under the one exported session

Every call below runs under the prologue's session and pid, over a working record preflighted under
the same pair; unit 4's arms sit from `tools/unattended/unattended.test.sh:7180` onward and use
`build_hold_fixture`. Unit 61's S13 retargets the lease-file assertions of each. No unit rewrites
their verdict assertions, which stand as each arm carries them; this unit's order is what makes them
hold again after unit 61's.

| Arm at `07997375` | Call | Under unit 61 as specified | With this unit |
|---|---|---|---|
| unit 4 AC6, `:7180-7183` | `--keepalive-id kB` | take-over through row 3 | row 4 refuses; assertions unchanged |
| unit 4 AC20, `:7235-7240` | `--replaces k1` | take-over: `lease replaced` and `taken over`, no `keepalive replaced` | row 2: `keepalive replaced`; unchanged |
| unit 4 AC20, `:7245-7249` | `--replaces kX` | take-over | row 2 refuses 58; unchanged |
| unit 28 AC9, once built | `--keepalive-id B` | take-over, which reaps | row 4 refuses and reaps nothing, as that arm asserts |

The first three are the arms H1 names. Each of the four is asserted once, where it stands, and this
unit adds no assertion to any of them and removes none.

Rev-1 of this spec listed three more arms here, on the premise that unit 61 deletes
`build_folder_age` and the leaseless rows. Unit 61 rev-3 keeps both (its §8 F13), so none of the
three is this unit's:

| Arm at `07997375` | Call | Under unit 61 rev-3 | Owner of any re-assertion |
|---|---|---|---|
| unit 4 AC19, `:7215-7218` | `--keepalive-id kC`, inside the bound | N3: the check-59 text its hit reads | unit 61 |
| unit 4 AC22, `:7227-7232` | `--keepalive-id kB`, inside the bound | N3: the status block and the check-59 text its two hits read | unit 61 |
| the dead-clock refusal, `:7425-7427` | `--keepalive-id kC`, build-folder age unanswerable | N1: the check-57 text its hit reads | unit 61 |

Each fixture is made leaseless under unit 61's S13 by deleting its lease-fact lines, so it carries
no `session`, and the first-match audit above keeps rows 2 and 3 off it. This unit edits none of the
three. Unit 61's N3 text names `--replaces` and the recorded keepalive beside what these hits read,
and if that rewording moves a hit, re-asserting it is unit 61's under its S13 and AC22, never this
unit's.

One arm changes its call and not its expectation: unit 61's same-session relaunch, its AC3 first
call among them. The tick's relaunch is a new process, so the arm must run under a `CLAUDE_PID` the
record does not name. Where unit 61's pass wrote that call under the prologue's pid, which the
record names, this unit's pass sets that call's `CLAUDE_PID` to another dead pid and keeps every
assertion unit 61 wrote. Unit 61 owns the arm and its assertions, this unit owns that one value, and
neither unit asserts the arm twice.

### Where the text goes

The stop contract's §8 table becomes unit 61's matrix, and this unit edits four of its rows in
`tools/unattended/STOPS.template.md` and its render. Measured against the rows as unit 61 §4 writes
them, PINNED at `07997375`, where unit 61 stood at rev-2, and re-read against its rev-3, which
leaves the three leased rows byte-identical and adds the no-lease one. Each row is one line, in the
table's new order:

```
| working, clock fresh or unknown | a new id with `--replaces` naming the recorded keepalive | the holder replaces its job: `write_lease`, staged; `--replaces` naming another id refuses 58 |
| working | a new id, the recorded session, which is not `absent`, under a pid the record does not name | the holder's process restarted: take-over; refuses 58 first when the recorded pid is alive |
| working, no lease, build folder inside the bound | a new id with `--replaces` naming the recorded keepalive | the holder replaces its job, through the `--replaces` block of the leased row above: `write_lease`, staged, all six facts recorded; `--replaces` naming another id refuses 58 |
| working, clock fresh or unknown | a new id | refuses 58: a live session drives this slug |
```

The first row gains 11 bytes and moves above the second. The second loses 9 net: it gains the pid
clause and drops "through `run_takeover`", which no other take-over cell in the table spells, and
"and is not `CLAUDE_PID`", which the pid clause now carries. The no-lease row keeps its place among
unit 61's no-lease rows and trades "below" for "above", five bytes for five. The last loses 17. The
net is −15 bytes and no line. The contract stood at 29105 bytes in 441 lines at `07997375`; unit 61
and `TOOL-dDerivedDocket-62`, whose worktree row and three moved rows touch none of these four, both
move that before this unit builds, so AC5 reads the build commit against its parent rather than
against either figure.

The driver is not a capped carrier. It gains the pid clause, the block move, and one comment line
citing this unit's id and H1.

### Inventory

This unit mints no identifier: no function, global, reason, verdict, file or conf key. The pid
comparison is an inline test in `verb_resume`'s same-session condition, so no lexicon cell is asked.

### Migration

None. No fact, file, key or record shape changes, so a record in flight reads the same until a
call meets rows 2 to 4.

### Rollout

The unit lands inside this build's own run, after unit 61. Between unit 61's merge and this one, the
orchestrator's driver carries unit 61's order. In that window a sub-agent of the orchestrating
session that ran `--resume <slug> --keepalive-id <new>` would take the run over, and the
orchestrator's own `--replaces` would run a take-over rather than a replacement. The orchestrator's
ordinary resume passes its recorded keepalive and meets row 1, which neither order changes. A unit
agent that runs the driver does so over a scratch fixture of its own and never over this run's
record. Unit 61's own Rollout call, a `--replaces` resume of this build's record while it still
carries no lease, meets N2 or N4, which neither order changes either.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/STOPS.template.md` · `memory/guides/UNATTENDED-STOPS.md`

### Alternatives rejected

- Excluding `--replaces` from row 3's caller cell and keeping unit 61's order. At a fresh clock the
  effect is the same, but row 2's predicate is then written twice, once as a row and once as an
  exception in the row above it, and the copy is the one a later edit forgets.
- A new check-58 branch with its own text for the recorded process. The catch-all's text already
  names `--replaces`, and a new branch owes an arm and a message signature for no difference a
  reader sees.
- Refusing the recorded process at every clock (§8 F2 b).
- Refusing only a LIVE recorded pid equal to `CLAUDE_PID` (§8 F2 c).
- A distinct session per second-driver arm (§8 F1 b).
- `--replaces` at every clock (§8 F3 b).

## 5. Production-readiness checklist

- security — Identity still keys on values any session on the node can read, so the matrix stops an
  accidental second driver and not a malicious one, as unit 61 §5 states. This unit closes one
  accidental path: the holder's own process, or its sub-agent, taking the run over with a new id and
  no freshness test. Any session may still pass `--replaces` naming the recorded keepalive, as at
  `07997375`.
- perf / scale — One comparison of an environment value against one fact the matrix already reads.
  No spawn and no probe is added.
- error / empty / loading states — Every refusal still precedes any write. No refusal text is added
  or changed. An `absent` pid on either side is no match.
- observability — The holder's replacement prints `keepalive replaced` again and never
  `taken over`. The recorded process's new id prints the catch-all check-58 text, which names
  `--replaces`.
- risks — (1) Under a harness exposing no pid, the recorded process cannot be told from its
  restart, so its sub-agent still reaches row 3 there, as unit 61 specifies. (2) If the OS hands the
  tick's relaunch the killed holder's pid number, row 3 reads the relaunch as the recorded process.
  At a fresh clock it is refused at 58, the attempt counts against `RESUME_ATTEMPTS`, and the next
  tick's relaunch draws another number.
- testing — The arms §7 names, each staged RED in the pass and executed once at VERIFYING under
  attribution; the direct observations in §6 are fixture runs of the driver and greps.
- migration — N/A: no fact, file, key or record shape changes (§4 Migration).
- user docs — The stop contract's §8 table, template and render.

## 6. Acceptance criteria

- **AC1** — On the working fixture `build_hold_fixture` leaves, whose lease facts name the session
  `fixture-session`, the keepalive `k1` and the dead pid `999999999`, `--resume tRun --keepalive-id
  kB --replaces k1` under the prologue's session and pid prints `keepalive replaced` and no
  `taken over`, records `keepalive: kB`, stages the record, and leaves the count of
  `grep -c ' resume · item tRun · '` over the record unchanged. The same call under
  `CLAUDE_PID=999999998`, another dead pid, does the same.
  Red when: the same-session row is evaluated first, so the holder's own replacement runs
  `run_takeover`, printing `lease replaced` and `taken over` and writing a history row, which unit
  61's order does under both pids; or only S2's pid clause is built, which the second call catches,
  because a pid the record does not name still reaches row 3.
  fixture: the authorized record the driver suite's prologue and `build_hold_fixture` build over a
  local bare remote; the tree holds none outside that suite.
  permission: the arm is written and staged RED in the pass, against a driver copy carrying unit
  61's row order; the driver suite that executes it is a held kit suite on no bar leg, so it runs in
  the orchestrator's attributed VERIFYING run and never in this pass.
- **AC2** — On AC1's fixture, `--resume tRun --keepalive-id kB --replaces kX` under the prologue's
  pid, and again under `CLAUDE_PID=999999998`, each refuses at check 58 with `--replaces names an id
  this slug's lease does not hold`, and `git hash-object` of the record and
  `git diff --cached --name-only` read as they did before the call.
  Red when: the same-session row takes the call first, so a `--replaces` naming a job that is not
  the one driving the run takes the slug over instead of refusing.
  fixture: AC1's.
  permission: as AC1, staged RED against the same copy.
- **AC3** — On AC1's fixture with no `--replaces`, `--resume tRun --keepalive-id kB` under the
  prologue's session and its pid `999999999`, which the record names, refuses at check 58 with the
  text naming `--replaces` and leaves `git hash-object` of the record unchanged. So does the same
  call on a fixture preflighted, and then resumed, under `CLAUDE_PID` set to the suite shell's own
  live pid, which is the sub-agent shape §4 measured. With the first fixture's commit and transcript
  aged past `RESUME_STALE_BOUND`, as unit 61's AC4 ages them, the same call prints
  `presumed-stopped` and takes the run over. Under `CLAUDE_PID=999999998` on the fresh fixture it
  takes the run over through row 3, printing `lease replaced` and no check 58.
  Red when: a caller under the recorded session and the recorded pid, whether the holder's own
  process or its sub-agent, takes the run over with no freshness test, which unit 61's row 3 does for
  a dead pid and for a live one equal to `CLAUDE_PID`; or the clause refuses at every clock, so a
  holder whose clock reads stale cannot re-key; or the tick's relaunch, a new pid over a dead
  recorded one, is refused.
  fixture: AC1's; the live pid is found the way the driver suite's lease arm finds its `OWN_PID`.
  permission: as AC1; the first two calls are staged RED against the copy, and the last two are its
  controls.
- **AC4** — When the orchestrator's attributed unattended run at VERIFYING reports on the driver
  suite, it reads `verdict clean`, with the four arms of §4's first arms table executed under the
  prologue's session and pid. The three at `tools/unattended/unattended.test.sh:7181`, `:7236` and
  `:7246` carry their assertions as at `07997375`, and unit 28's AC9 arm as that unit writes it,
  each bar the lease-file ones unit 61 retargets. The three leaseless arms of §4's second table read
  unit 61's check-59 and check-57 texts, and unit 61's AC22 arm, whose `--replaces` call on a record
  with no lease prints `keepalive replaced`, is among the executed ones. In the pass,
  `grep -c 'export CLAUDE_CODE_SESSION_ID=fixture-session' tools/unattended/unattended.test.sh` and
  `grep -c 'export CLAUDE_PID=999999999' tools/unattended/unattended.test.sh` each print 1; the
  suite's diff against the parent adds no `CLAUDE_CODE_SESSION_ID=` assignment and removes no
  `hit`, `miss` or `same` line, so no existing assertion is rewritten; and `FLOOR_ASSERTIONS` and
  `FLOOR_SHARD_2` each read their first-parent figure plus exactly the assertions S3's blocks carry,
  read with `git show` at both, while `FLOOR_SHARD_1` is unchanged.
  Red when: an arm keeps its verdict only because it was handed a session of its own, so the suite
  stops exercising the one shape a holder's sub-agent has; or an arm still expects a take-over from
  the recorded process; or this unit re-asserts an arm unit 61 owns, so one arm carries two units'
  expectations; or the block's move leaves unit 61's no-lease `--replaces` row without its entry, so
  that unit's AC22 arm stops printing `keepalive replaced`; or a floor is left where the arms found
  it, or moves by a number no arm of S3 accounts for.
  permission: the verdicts are the driver suite's, a held kit suite on no bar leg, run in the
  orchestrator's attributed VERIFYING run and never in this pass; the greps are this pass's direct
  check.
- **AC5** — At the build commit, `grep -n 'fresh or unknown | a new id with' tools/unattended/STOPS.template.md`
  prints a smaller line number than `grep -n 'process restarted' tools/unattended/STOPS.template.md`;
  `grep -c 'a pid the record does not name' tools/unattended/STOPS.template.md` prints 1;
  `grep -c 'a new id, another session' tools/unattended/STOPS.template.md` prints 0;
  `grep -c 'block of the leased row above' tools/unattended/STOPS.template.md` prints 1 and
  `grep -c 'block of the leased row below' tools/unattended/STOPS.template.md` prints 0;
  `cmp tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md` prints nothing; and
  `git cat-file -s` and `wc -l` over both files are not greater than at the first parent.
  Red when: the contract keeps unit 61's order, so a reader following it believes the holder's
  `--replaces` is a take-over; or the no-lease `--replaces` row still points below, at a block whose
  row now sits above it; or the edit is written without the trims that fund it, so a capped carrier
  grows.
  permission: the render's byte identity, as a verdict, is the `unattended kit gate` and
  `unattended skill wiring` legs at the VERIFYING bar; `cmp` is this pass's direct check.
  figure: the −15 bytes is PINNED against unit 61 §4's rows at `07997375`, which its rev-3 left
  byte-identical, the no-lease row's one-word edit being byte-neutral; the not-greater test is
  derived at the build commit.
- **AC6** — When `grep -oE '^[a-z_]+[(][)] [{]' tools/unattended/unattended.sh` runs at the build
  commit and at its first parent, the two lists are identical; `grep -cE '^[^#]*fail 58 '` and
  `grep -cE '^[^#]*fail 59 '` over the driver print the same at both; the diff of
  `memory/project/unarmed-branches.txt` against the parent is empty;
  `grep -c 'KIT_UNATTENDED_VERSION=1.29'` prints 1 over the driver and over
  `tools/unattended/check-unattended.sh`; and no added line of the driver or of
  `tools/unattended/STOPS.template.md` spells a `tools/<kit>/` literal.
  Red when: the recorded process's case is given a new `fail` branch with no arm, an insertion moves
  a pinned ordinal, a function is minted past the lexicon, or a version moves that the unreleased kit
  does not owe.
  permission: the verdicts are the `harness arms (fail branches armed or pinned)`,
  `kit version markers` and `install-prefix (shipped surface)` legs at VERIFYING; the greps are this
  pass's direct check.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `codebase-map coverage + freshness` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · the recorded session's `--replaces` naming the recorded keepalive under the recorded pid and under another dead pid, and naming another id under both; the recorded session's new id with no `--replaces` under the recorded pid dead, under a live one, and with the clock aged; the relaunch control under another pid; unit 61's same-session relaunch call moved to a pid the record does not name, its assertions untouched · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2`, each raised by exactly the new arms' assertions, counted off their blocks; the relaunch call's pid moves neither

Both floors follow this build's practice, set by the CLOSED units 25, 30, 49 and 54: a unit raises
its suite's executed-assertion floor by exactly the arms it adds, derived from the blocks rather than
read off a run, which this pass does not make. The arms are written in region two beside unit 4's
lease arms, so `FLOOR_SHARD_1` does not move.

`recall floor` and `recall floor arms` are owed by the render's path under `memory/`; every other
guard the estimate trips is broad and leaves the join.

## 8. Open questions

- **F1 — how the second-driver arms keep their verdicts.** Options: (a) under the prologue's one
  exported session and pid, through S2's pid clause; (b) the review's note that every second-driver
  arm set a distinct `CLAUDE_CODE_SESSION_ID`. RESOLVED (agent, 2026-09-22, delegated), decided by
  the orchestrator's brief for this unit: (a). Under (b) the arms would pass while no arm exercises
  the recorded session under the recorded pid, the shape every sub-agent of a holder has (§4), so
  the class H1 found would lose its regression.
- **F2 — what the recorded process's new id meets.** Options: (a) the rows below row 3, so the clock
  decides; (b) a refusal at every clock; (c) the review's narrower fix, refusing only a LIVE recorded
  pid equal to `CLAUDE_PID`. RESOLVED (agent, 2026-09-22, delegated): (a). (b) leaves a holder whose
  clock reads stale no way to re-key, because row 2 is read only at a fresh or unknown clock. (c) lets
  the suite's dead fixture pid, equal to `CLAUDE_PID`, through row 3, so unit 4 AC6's refusal becomes
  a take-over, which F1 rules out.
- **F3 — `--replaces` at a stale clock.** Options: (a) it meets row 6, the announced take-over, as at
  `07997375`; (b) row 2 at every clock. RESOLVED (agent, 2026-09-22, delegated): (a). The driver
  reads `--replaces` only inside its fresh branch (`tools/unattended/unattended.sh:5790-5791`), (b)
  changes a row unit 4 decided, and no finding names it.
- **F4 — the documented first-match check H1's left-shift proposes.** RESOLVED (agent, 2026-09-22,
  delegated): not built here. The review names this unit's arms as the regression gate for the class
  in this matrix, and §4 runs the check once over the new table. A check over every first-match table
  is the class `TOOL-dDerivedDocket-40` holds OPEN in `memory/backlog/TOOL.md`.
- **F5 — an `absent` pid.** RESOLVED (agent, 2026-09-22, delegated): no match on either side, which
  keeps unit 61's relaunch reading for a harness that exposes no pid. §5 risk (1) states the cost.

## 9. Revision log

- rev-1 · 2026-09-22 · initial draft, promoted from H1 of the G8 spec audit round 1 at its bounded
  exit, grounded on `07997375` and on unit 61 as specified at that commit.
- rev-2 · 2026-09-22 · §2 S1 S3 S4 S5 · §3 · §4 · §6 AC4 AC5 · §7 · re-grounded on unit 61 rev-3,
  whose §8 F13 keeps `build_folder_age` and its leaseless rows, where rev-1 assumed unit 61 deleted
  them. S4, §4's arms tables and AC4 no longer claim the arms at `:7216`, `:7228` and `:7426` meet
  the check-58 refusal: they keep their check-59 and check-57 texts, and any re-assertion they owe
  is unit 61's. AC4's zero-count grep for the leaseless check-59 text, which rested on the deletion,
  is withdrawn, and so is the `miss` on `taken over` rev-1 added to the last four arms of its table.
  §4's table places unit 61's four no-lease rows between rows 3 and 4 in unit 61's words and says
  every other row of unit 61's table stands as unit 61 states it. The one word this unit changes
  among them, the no-lease `--replaces` row's pointer, is S5's fourth contract row and AC5's two new
  greps. S1 and §4 keep that row's entry into the moved block, observed through unit 61's AC22 arm
  at AC4. §3 says unit 61 builds its own table unedited. S3, AC4 and §7 raise the driver suite's
  `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` by exactly the new arms, counted off their blocks, where
  rev-1 moved no floor.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "choose which resume matrix row a call reaches by first
match, keyed on the caller's replaces flag, session and pid"` returns no seam for this work. Its
candidates are name-stem matches on `key`, `row` and `ses` in the Python kits, and its header prints
`unscanned layers: .sh`, the layer this unit is written in. So no existing seam fits in the corpus
the probe reads. The seam this unit extends was found by reading source: the working branch of
`verb_resume` in `tools/unattended/unattended.sh`, as unit 61 re-keys it, whose `--replaces` block
and catch-all check-58 branch stand at `:5791` and `:5819`; `run_takeover` and `write_lease` are
reused unchanged.

Recall terms used: `python tools/memory-recall/query.py "which resume matrix row does the lease
holder's own --replaces reach, and how is a restarted process told from the holder itself" --terms
"replaces keepalive holder same-session take-over resume matrix row order pid session sub-agent
refusal"`. It returned `TOOL-dDerivedDocket-40`'s OPEN row on matrix rows nobody names a reacher for,
unit 61's re-keyed matrix, the G8 finding itself, the stop contract's current §8 table, unit 4's
F12, and the protocol's RESUME rule that a holder replacing its own job records it with `--replaces`.
