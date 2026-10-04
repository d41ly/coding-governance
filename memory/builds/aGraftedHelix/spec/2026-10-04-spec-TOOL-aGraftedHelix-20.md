# TOOL-aGraftedHelix-20 — the holder row's claim CAS runs before its `write_lease` under one stamp, and a CAS that does not land leaves a `prior-session` fact the `mine` test accepts

**Status:** SPECCED · rev-3 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-review-TOOL-aGraftedHelix-20-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-20-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-21 TOOL-aGraftedHelix-22 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-18` orders the `--resume` holder row as: decide `mine` against the record's facts
before the call, run `write_lease`, then write the claim from the facts after it. Unit 1's call-site
table keeps a holder claim write that does not complete as "announce, continue". Take a holder call
whose session changed from `s1` to `s2` and whose claim push times out, or that runs offline, which
unit 1 supports on the holder path. Afterwards the record names `s2` and the claim names `s1`. On the
next `s2` call the claim is not `mine`, which needs the record's keepalive AND session, and not
`same session`, because the claim's `s1` differs from the environment's `s2`. It reads as foreign, the
holder column answers check 90, and a live run is forced to `--abort --code claim-lost`. A lost race
on that call likewise reaches check 90 only after `write_lease` has rewritten and staged the record,
which breaks unit 1's rule that the CAS precedes every local write. This unit moves the claim CAS
ahead of `write_lease` under one lease stamp, and records what the claim still carries when the CAS
does not land. It closes finding 9 (HIGH) of the round-1 spec audit of units 16 to 19.

## 2. Scope (IN)

- **S1** — At the `--resume` holder row, when `write_lease` is due, the claim read, the `mine` test
  and check 90 run against the record's facts as they stood before the call, as unit 18 S1 has
  them. The row then computes the lease stamp ONCE, writes the claim by CAS with the values the call
  is about to record (`session` from `CLAUDE_CODE_SESSION_ID`, `host` from `read_host_name`, the
  unchanged `keepalive`, and the stamp as `lease-utc`), and only then calls `write_lease` with that
  stamp as its third argument. A LOST race is check 90 with the run-state file's bytes and the index
  untouched. Observed by AC1 and AC3.
- **S2** — When the CAS does not complete, or the claim could not be read, the row still runs
  `write_lease`, and records a lease fact `prior-session` holding the record's `session` fact from
  before the call. The fact is written only while it reads `absent` or is missing, so a second call
  that also fails to land keeps the session the published claim still carries. The next holder-row
  claim write that lands sets it `absent`. The fact write runs before the row's `stage_or_fail`.
  The clearing write runs only when the fact reads a value other than `absent`, and then runs
  `stage_or_fail` on the record itself, because the row's existing `stage_or_fail` sits inside the
  `write_lease`-due branch (`tools/unattended/unattended.sh:6596-6600`) and a renewal that clears
  the fact has no `write_lease` due. `TOOL-aGraftedHelix-23` replaces this rule's encoding (§3).
  Observed by AC2 and AC3.
- **S3** — The `mine` test, wherever it compares the claim with the record's facts, also accepts a
  claim whose `keepalive` equals the record's and whose `session` equals the record's
  `prior-session` fact when that fact is not `absent`. Those are the holder and status-write
  columns of unit 1's table; `--preflight` and a take-over compare with the values they are about to
  record and are unchanged, except at the restart row S8 names. `TOOL-aGraftedHelix-23` makes the
  comparison a membership test and pins where the fact is read (§3). Observed by AC2.
- **S4** — `check_lease_only_diff` in `tools/unattended/lib-unattended.sh` admits `prior-session`
  as a lease-fact line, because it is written beside `write_lease`'s six. Observed by AC4.
- **S5** — `tools/unattended/unattended.test.sh` gains the arms §7 names over unit 18's
  changed-session arm: the claim push made to exit 124, the remote unreachable, and the lost race,
  each on the `s2` call, the single stamp under a `date` shim, and the two restart arms of S8.
  NOT OBSERVED by a criterion here: the suite is the main loop's to run at VERIFYING, and each arm's
  red on a staged break is observed there (§7).
- **S6** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC5.
- **S7** — Every other place that lists or counts the lease's lines names `prior-session` as one
  of them: the lease section and the landing paragraph of `tools/unattended/STOPS.template.md`,
  re-rendered into `memory/guides/UNATTENDED-STOPS.md` in the same commit, and the comments that
  list or count the six in `tools/unattended/unattended.sh` and `tools/unattended/lib-unattended.sh`
  (§4 Evidence). NOT OBSERVED by a criterion here: these are prose and comments, and AC4 observes
  the one reader that decides a verdict.
- **S8** — In the take-over column, at the restart row only, the `same session` test is widened.
  That row is the recorded session's own relaunch under a new keepalive, which the restart branch of
  `tools/unattended/unattended.sh` sends through `run_takeover` (`:6666-6680`), so it holds exactly
  when `CLAUDE_CODE_SESSION_ID` equals the record's `session` fact before the call. There, a claim
  whose `keepalive` equals the record's `keepalive` fact before the call and whose `session` equals
  the record's `prior-session` fact, when that is not `absent`, reads `same session`. Every other
  take-over and `--preflight` compare as unit 1 has them. Observed by AC6.

## 3. Non-goals (OUT)

- **The take sites' order.** `--preflight` and `run_takeover` already CAS before `write_lease`
  (unit 1's call-site table) and share one stamp (unit 11 S6). `--dispatch` and `--close` run no
  `write_lease`. S8 widens only the restart row's `same session` test, never the order.
- **`RUN_CLAIMS` off.** No claim is read or written, the row runs `write_lease` as it does at base,
  and `prior-session` is never written.
- **The `--replaces` block.** It moves the keepalive, not only the session, and an incomplete CAS
  there leaves a claim the holder's own `same session` row takes back while the session is
  unchanged. This unit does not reorder it; a session AND keepalive change with an incomplete push
  is a follow-up for that block's own order.
- **Clearing the fact from other writers.** `--beat`, `--dispatch`, `--close` and the status writes
  copy their identity from the record, so a write of theirs that lands publishes `s2` too, but they
  leave `prior-session` as it is. A stale value widens `mine` only to a claim carrying this run's
  own keepalive, and the next holder-row write that lands clears it.
- **The fact across repeated incomplete calls.** A second incomplete push after another writer
  landed the claim, two incomplete calls in a row, a recorded session reading `absent`, and the
  widening at every holder and status-write site are `TOOL-aGraftedHelix-23`'s. It makes the fact a
  set that only grows until a holder write lands, spells the cleared state as the empty value, and
  moves the read into `check_claim_writable` (findings 6, 12, 2, 7 and 1 of the round-1 audit of
  units 20 to 22).
- **Supersessions this unit records.** It supersedes unit 1 §4 "Who may write a claim"'s `mine`
  definition, and unit 11 §3's "The `mine` test ... is unchanged", for the holder and status-write
  columns (S3), and unit 1 §4's `same session` definition at the take-over column's restart row
  (S8). It swaps the second and third rows of unit 18 §4 "The order" (S1). It moves the
  `--resume` holder row of unit 11 §4 "The rule" from "the record's lease facts" to the values the
  call records, whenever `write_lease` is due.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-18` — the holder row's order with `mine` decided against the
  facts before the call, and its changed-session arm, which this unit's arms extend; without it the
  rows this unit swaps are not pinned.
- **consumes-from** `TOOL-aGraftedHelix-11` — `write_lease`'s optional third argument, the lease
  stamp, and the rule that a claim write copies its identity from the lease; without the argument
  the claim's stamp and the record's cannot be one value.
- **consumes-from** `TOOL-aGraftedHelix-1` — `check_claim_writable`'s `mine` test, the holder row's
  claim read and check 90, the "announce, continue" row for an incomplete holder write, and the
  lost-race `git` shim of its suite; without them there is no test to widen and no fixture to drive.
- **hands-off** `TOOL-aGraftedHelix-23` — the `prior-session` fact's encoding and its reader: a set
  that every incomplete holder-row call adds to and the next landed holder write empties, `absent`
  a legal member, the empty value the cleared state, and the read inside `check_claim_writable` for
  every holder and status-write site, with the interleaved sequences that drive it (findings 6, 12,
  2, 7 and 1 of the round-1 audit of units 20 to 22).

## 4. Design

### Evidence

- `write_lease` takes the run-state file and the keepalive id at base, and stamps `lease-utc` with
  `date -u` itself (`tools/unattended/unattended.sh:5557-5572`). Unit 11 S6 gives it an optional
  third argument, the stamp, read in place of the clock when present; that is how the shared stamp
  reaches it.
- The holder row runs `write_lease` and `stage_or_fail` only when `lease-utc` is absent or the
  recorded session or pid differs from the harness's (`tools/unattended/unattended.sh:6591-6600`).
- Unit 1's §5 risks line names the class: "the CAS precedes every local write". Unit 18 §4
  "Alternatives rejected" cites the same premise.
- `check_lease_only_diff` (`tools/unattended/lib-unattended.sh:1172`) accepts a working-copy
  difference confined to the six lines `write_lease` writes, and `read_landing_commit` relies on it
  for a re-bind of a pushed landing. A seventh fact written beside them would read as a non-lease
  difference without S4.
- The six are also listed or counted in prose S7 names: `tools/unattended/STOPS.template.md:147`
  and `:193`, `tools/unattended/lib-unattended.sh:1168` and `:1188`, and
  `tools/unattended/unattended.sh:1227`, `:1970` and `:4425`. Predicate:
  `git grep -nE "six lease|lease-fact lines|pid-image. and .lease-utc" -- tools ':!*.test.sh'`.
- The claim carries no pid, so a pid-only change still moves `lease-utc`, and the claim follows the
  record's stamp (unit 18 §3). Whenever `write_lease` is due, a claim write is due too.

### The order

| step | reads | writes |
|---|---|---|
| claim read, `mine` test, check 90 | the record's facts before the call, `prior-session` included | nothing |
| the stamp, when `write_lease` is due | the clock, once | nothing |
| claim CAS, when due | the values `write_lease` is about to record, and the stamp | the claim |
| `write_lease`, when due | the environment, and the stamp as its third argument | the record's lease facts |
| `prior-session` | the CAS outcome | set or cleared per the table below |
| `stage_or_fail` | nothing | the index, when `write_lease` ran or the fact was written |

The fact write precedes `stage_or_fail`, so a call that writes it leaves no unstaged record. A
clear on a call whose `write_lease` is not due runs its own `stage_or_fail`, and a fact that is
missing or reads `absent` is not written at all, so a renewal over a record without it still writes
nothing, as the row's existing contract and its suite arms require.

### What each outcome leaves

| CAS outcome on the `s2` call | claim | record `session` | record `prior-session` | the call |
|---|---|---|---|---|
| landed | `s2` | `s2` | `absent` | continues |
| lost | another writer's | `s1`, untouched | untouched | check 90 |
| not completed, or the claim unreadable | `s1` | `s2` | `s1` | announces, continues |

After the third row, the next `s2` call reads the claim as `mine` through `prior-session`, finds the
`session` field differing, writes, and on landing sets the fact `absent` and stages the record.
A crash after the third row, and the session's relaunch under a new keepalive, reach the restart
row, where S8 reads the claim as `same session` and takes it over.

### Inventory

One new run-state fact, `prior-session`. No new function, check, conf key or file. A fact key is
not a lexicon cell here, and no codebase-map key is minted.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/STOPS.template.md`
- `memory/guides/UNATTENDED-STOPS.md`, by the render
- `tools/unattended/unattended.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

### Alternatives rejected

- **Keep `write_lease` first and let the next call's `same session` row take the claim.** The
  `same session` row compares the claim's session with the environment's. After the incomplete call
  the claim names `s1` and the environment `s2`, so it misses; that is finding 9.
- **Skip `write_lease` when the CAS does not complete.** The lease record is what the hooks and the
  tick bind to, so an outage would leave `--liveness` reading the old session for as long as it lasts.
  Unit 18 rejects skipping it for the same reason.
- **Retry the push inside the call until it lands.** A bounded call cannot wait out an outage, and
  unit 1 keeps the holder path working offline on purpose.

## 5. Production-readiness checklist

- security — No new surface. The fact names a session id the run branch already publishes in the
  record's `session` line.
- perf / scale — None added: the claim write was already due on a call whose `write_lease` ran.
- error / empty / loading states — The three outcomes of §4 "What each outcome leaves". An
  incomplete push keeps unit 1's announce line.
- observability — The announce line names the write that did not land, and `prior-session` in
  the run-state file shows which session the published claim still carries.
- risks — A reader matching the lease's lines by an explicit list. `check_lease_only_diff` is the
  one in the tree and S4 extends it; the builder greps the kit for the six-name list before landing.
  A stale `prior-session` widens `mine` only to a claim under this run's own keepalive.
- testing — §7's arms, each observed RED on a staged break first. The 124 arm stages S3's widening
  removed and the unreachable arm stages `prior-session` left unwritten, since the CAS's place does
  not change the third outcome row. The CAS moved back after `write_lease` is the lost-race arm's
  break only. AC3's arm runs under a `date` shim, so a second clock read differs every time. The
  restart arms stage S8's widening removed and its session condition removed. The lost race is
  staged by unit 1's `git` shim on `PATH`, never by a sleep.
- migration — None: no claim exists before unit 1 lands, and a record without the fact reads
  `absent`.
- user docs — The lease section of the stops guide, re-rendered in the same commit.

## 6. Acceptance criteria

The fixture is unit 18's: a `git clone --local` of this repository under `%TEMP%`, its one remote
re-pointed at a bare repository, `RUN_CLAIMS` on, and a run whose record and claim both name session
`s1` and the recorded keepalive. Each call below is `--resume <slug> --keepalive-id <recorded id>`
with `CLAUDE_CODE_SESSION_ID` set to `s2`.

- **AC1** — When the call runs with unit 1's lost-race `git` shim on `PATH`, which moves the claim
  ref before forwarding the push, it prints `UNATTENDED check 90 FAILED`, the run-state file's
  `session:` fact still reads `s1`, and `git diff --name-only` and `git diff --cached --name-only`
  name no run-state file.
  Red when: `write_lease` ran before the refusal, so the record moved on a call that lost its claim.
  fixture: the shim is unit 1's and exists once unit 1 is built.
- **AC2** — When the call runs with a `git` shim on `PATH` that makes the claim push exit 124, it
  exits 0, the run-state file reads `session: s2` and `prior-session: s1`, and the claim read with
  `git ls-remote <bare> refs/gov/runs/<slug>` and `git cat-file -p` still names `session: s1`. A
  second call with no shim exits 0, prints no `UNATTENDED check 90 FAILED`, leaves a claim naming
  `session: s2`, and leaves `prior-session: absent`. The same holds when the bare repository is
  renamed away for the first call and restored for the second. After each call,
  `git diff --name-only` names no run-state file.
  Red when: the second call refuses its own claim with check 90, or a call leaves the record
  unstaged.
- **AC3** — When the call runs with no shim but a `date` shim on `PATH`, and the push lands, the
  claim's `lease-utc` equals the record's `lease-utc` byte for byte, and the record's
  `prior-session` is missing or reads `absent`. The shim forwards every invocation to the real
  `date` unchanged, except one asking for the `+%Y-%m-%dT%H:%M:%SZ` format, which it answers with
  the real UTC time advanced by one more second for each such request so far, counted in a file
  under the fixture. With the run-state file then committed in the fixture, a second `s2` call with
  no shim, whose `write_lease` and claim renewal are both not due, leaves `git status --porcelain`
  empty.
  Red when: the claim and the record carry stamps read from two clocks, which the shim makes differ
  on every such build, or a renewal over a record without the fact writes it.
- **AC4** — When `check_lease_only_diff`, sourced from `tools/unattended/lib-unattended.sh`, runs in
  a scratch repository whose committed run-state file differs from its working copy only by an added
  `prior-session: s1` line, it returns 0. With a `phase:` line changed as well, it returns 1.
  Red when: the new fact reads as a non-lease difference, so a re-bind of a pushed landing stops
  finding its landing commit.
- **AC5** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.
- **AC6** — When AC2's first call, with the claim push exiting 124, is followed by a call under
  `s2` with `CLAUDE_PID` changed and `--keepalive-id` naming a new keepalive, that call takes the run
  over, prints no `UNATTENDED check 89 FAILED`, and leaves a claim naming the new keepalive and
  `session: s2`. Over a second copy of the same record and claim, a call under `s3` and a new
  keepalive that reaches `run_takeover` through the presumed-stopped row, with the fixture's
  `RESUME_STALE_BOUND` lowered so the lease and the claim's beat both read stale, prints unit 1's
  `claim taken over` line naming session `s1`.
  Red when: the restart reads the claim as foreign and answers check 89, or the `s3` take-over reads
  the claim as `same session` and takes it without that line.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · the s2 holder call whose claim push exits 124, then a second s2 call; stage S3's widening removed · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · the s2 holder call with the remote unreachable, then a second s2 call with it restored; stage prior-session left unwritten · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · the s2 holder call that loses the race leaves the run-state file and the index untouched; stage the CAS moved back after write_lease · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · the landing s2 call under a date shim that advances each stamp-format read, claim and record lease-utc equal; stage the claim CAS reading its own clock · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · after an incomplete s2 push, the s2 restart under a new keepalive takes over with no check 89; stage S8's widening removed · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · after an incomplete s2 push, an s3 take-over through the presumed-stopped row announces the claim taken over from s1; stage S8's session condition removed · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs its criteria
directly, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 9 of the round-1 spec audit of units 16
  to 19, grounded against `write_lease`, the holder row and `check_lease_only_diff` at base
  `5266d22e`, and against units 1, 11 and 18 as specced.
- rev-2 · 2026-10-04 · §2 §4 · S4 S7 · from the bug-class checklist over the promoting commit, which
  selected `observed-by-claim-no-arm-discharges` and `a-folded-field-leaves-its-row-shape-docs-behind`.
  S4 claimed AC4 observed the stops guide, which AC4 never reads; the guide moves to S7, NOT
  OBSERVED, with every comment that lists or counts the six lease lines, found by the §4 predicate.
- rev-3 · 2026-10-04 · §2 §3 §4 §5 §6 §7 · S2 S3 S5 S8 · AC2 AC3 AC6 · folded the round-1 spec audit
  of units 20 to 22 on this unit. Finding 5: AC3 runs under a `date` shim that advances each
  stamp-format read by one more second, so a second clock read differs on every such build, with
  its own arm. Finding 8: the 124 arm stages S3's widening removed, and the CAS moved back after
  `write_lease` is the lost-race arm's break only. Finding 13: the fact write precedes the row's
  `stage_or_fail`, a clear runs only on a fact other than `absent` and stages the record itself,
  AC2 reads the index after each call and AC3 asserts a renewal writes nothing. Finding 14: S8
  widens the take-over column's `same session` test at the restart row only, observed by AC6 with
  two arms. Findings 6, 12, 2, 7 and 1 are promoted to `TOOL-aGraftedHelix-23`: §3 gains its
  hands-off and a non-goal, and S2 and S3 point at it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "write the claim before the lease record and remember the
replaced session when the push does not complete"` ranked name-stem neighbours only, `write` in
`tools/memory-tree/gotchas.py` and `records`, and printed `unscanned layers: .sh`, so its miss is no
evidence. The seams were read from source: `write_lease` with unit 11 S6's stamp argument, the
holder row in `tools/unattended/unattended.sh`, and `check_lease_only_diff` in
`tools/unattended/lib-unattended.sh`. No existing seam records what a published record still carries
when its push did not land. The recall probe returned unit 18, the audit's H1 row, unit 11, and
`TOOL-dDerivedDocket-61`, the ruling that the lease is one record of run-state facts.

Recall terms used: claim CAS write_lease incomplete push announce continue lease record session holder mine order

The question passed with them: "when a compare-and-swap push of a claim does not complete, what does
the local lease record hold".
