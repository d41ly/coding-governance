# TOOL-aGraftedHelix-23 — the `prior-session` fact is the set of sessions an incomplete holder write may have left the claim under, read by `check_claim_writable` itself and emptied by the next holder write that lands

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-20` records a `prior-session` lease fact when the `--resume` holder row's claim
CAS does not land, and widens the `mine` test to accept a claim under that session. The round-1
spec audit of units 20 to 22 confirmed five HIGH findings on that fact. Each ends in the outcome unit
20 exists to prevent: a live run reads its own claim as foreign, answers check 90, and is forced to
`--abort --code claim-lost`.

- Findings 6 and 12: unit 20 S2 keeps the fact sticky, but `--beat`, `--dispatch`, `--close` and the
  status writes land the claim under the new session without touching it. A second incomplete push
  then keeps a value the claim no longer carries.
- Finding 2: no criterion drives two incomplete holder calls in a row, so a build that writes the
  fact unconditionally passes, and an offline pid restart then locks the run out.
- Finding 7: the fact can hold the literal session `absent`, which unit 20 S3 reads as no fact.
- Finding 1: the widening is driven only at `--resume`, and no spec says where
  `check_claim_writable` gets the fact, so a build that supplies it from one caller passes.

This unit makes the fact a set that only grows until a holder write lands. It spells the cleared
state as the empty value, which no recorded session can be. It moves the read into
`check_claim_writable`, so no caller can omit it, and it drives every sequence the audit named. It
closes findings 6, 12, 2, 7 and 1 (all HIGH) of the round-1 spec audit of units 20 to 22.

## 2. Scope (IN)

- **S1** — `prior-session` holds a SET: zero or more session values, separated by one space, in the
  order they were added, none twice. The empty value and a missing line are both the empty set, the
  one cleared state. `absent` is a legal member and compares literally, as unit 1 §4 compares two
  absent sessions. This supersedes unit 20 S2's and S3's reading of `absent` as the cleared state.
  Observed by AC1 and AC3.
- **S2** — On a `--resume` holder-row call whose claim CAS did not complete, or whose claim could not
  be read, the row ADDS to the set, before its `stage_or_fail`: the record's `session` fact as it
  stood before the call, and, when the claim read succeeded, the claim's `session` field. A value
  already present is not added again, and every member stays in the set until S3 empties it. This
  replaces unit 20 S2's "written only while it reads `absent` or is missing". Observed by AC1 and
  AC2.
- **S3** — The next `--resume` holder-row claim write that lands empties the set by writing the fact
  with an empty value, only when the set is non-empty, and then runs `stage_or_fail` on the record
  itself. A lost race does not change the set. No other writer writes or empties the fact, as unit 20
  §3 already states for `--beat`, `--dispatch`, `--close`, the LANDING re-bind and the status writes.
  Observed by AC1, AC2 and AC4.
- **S4** — `check_claim_writable` reads the set from the run-state file itself, beside the
  `keepalive` and `session` facts it compares, whenever its mode is holder or status write; no caller
  passes the fact in. A claim whose `keepalive` equals the record's and whose `session` is any member
  reads `mine`. Every holder site of unit 1's call-site table, `--resume`, `--dispatch`, `--close`
  and `--beat`, and every status-write site, the LANDING re-bind, `--hold`, `--landed` and
  `--abort`, therefore gets the widening by construction. Observed by AC1 and AC4, which drive
  `--beat`, `--dispatch` and `--hold`. `--close`, `--landed`, `--abort` and the LANDING re-bind are
  NOT OBSERVED by a criterion here: the read's place inside the function is what reaches them.
- **S5** — The take-over column's restart widening, unit 20 S8, tests membership in the set: at the
  restart row, a claim whose `keepalive` equals the record's before the call and whose `session` is
  any member reads `same session`. Observed by AC5.
- **S6** — Every comment, and every line of the stops guide `tools/unattended/STOPS.template.md`
  with its render, that unit 20's build writes about what `prior-session` holds says it holds a set,
  that the empty value is the cleared state, and that the `--resume` holder row is its one writer.
  NOT OBSERVED by a criterion here: these are prose and comments, and AC1 to AC5 observe the readers
  that decide a verdict.
- **S7** — `tools/unattended/unattended.test.sh` gains the arms §7 names, over unit 20's fixture and
  arms, and every assertion unit 20's arms make on the fact's value follows S1: a `prior-session`
  reading `absent` after a landing becomes `fact` printing nothing, and one reading `s1` becomes a
  set holding `s1`. This supersedes unit 20 AC2's "leaves `prior-session: absent`" and its §5
  migration line's "reads `absent`" by name. NOT OBSERVED by a criterion here: the suite is the main
  loop's to run at VERIFYING, and each arm's red on a staged break is observed there (§7).
- **S8** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC6.

## 3. Non-goals (OUT)

- **Emptying the fact from other writers.** Unit 20 §3's non-goal stands. Emptying it on every claim
  write that lands, whatever its writer, would make the out-of-process tick's `--beat` write the
  session's run-state file, which unit 1 defines as writing nothing local, and would race the
  session's own `set_fact` writes in `write_lease`. It would also empty the fact after `--hold`,
  `--landed` and `--abort` have already staged or pushed the record. The audit's skeptics rejected
  it for those reasons.
- **Overwriting the fact with the read claim's session alone.** It loses the case where the claim
  could not be read, which §4's sequence d drives.
- **Removing the line to clear it.** That needs a new line-removing writer beside `set_fact`. The
  empty value reuses `set_fact` and the `hold-unpushed` precedent, and `fact` reads both alike.
- **Bounding the set.** A member is added only by a holder call whose push did not complete, and
  the first holder write that lands empties the set, so it grows only across one outage.
- **The `--replaces` block, `--preflight`, and every take-over other than the restart row.** They
  stay as unit 20 has them.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-20` — the `prior-session` fact, its write when the holder
  row's CAS does not land, the `mine` widening on the holder and status-write columns, the restart
  row's `same session` widening, §4 "The order", and the fixture and arms; without them there is no
  fact to re-encode and no arm to extend.
- **consumes-from** `TOOL-aGraftedHelix-1` — `check_claim_writable`, its call-site table's holder and
  status-write columns, the `--beat` and `--hold` verbs, the tick fixture whose `--liveness` reads
  `LIVE`, and the lost-race `git` shim; without them there is no decision to move the read into and
  no site to drive.

## 4. Design

### Evidence

- `fact` returns the first matching line's value and prints nothing for a missing line or an empty
  value (`tools/unattended/unattended.sh:1117`). `set_fact` writes `key: value` under
  `## Run facts` and refuses only a newline or a carriage return (`:5509`).
- `hold-unpushed` is cleared by `set_fact` with an empty value, only when it is non-empty (`:6369`).
  S3 reuses that shape.
- `write_lease` records `${sid:-absent}` (`:5563`), so a recorded session is never empty, and the
  empty value lies outside the session value space.
- The holder row's `write_lease` is due on a changed pid as well as a changed session (`:6597`), so a
  process restart under an unchanged session is a second incomplete call with the same pre-call
  session.
- `check_lease_only_diff` matches a lease line by its key prefix
  (`tools/unattended/lib-unattended.sh:1182`), so unit 20 S4's admission of `prior-session` admits a
  set and the empty value alike.

### The set across one `--resume` holder-row call

| outcome | the set afterwards |
|---|---|
| CAS landed | empty, written only when it was non-empty |
| CAS lost | unchanged, and the call is check 90 |
| CAS not completed, the claim read | the set, plus the pre-call record session, plus the claim's session, each once |
| the claim unreadable | the set, plus the pre-call record session, once |
| no claim write due | unchanged |

### The sequences

Each starts from unit 20's fixture, record and claim both at `s1`. A sequence ends with a closing
`--resume` call under its last session and no shim.

| seq | calls before the closing one | set before it | claim before it |
|---|---|---|---|
| a | an `s2` call whose push exits 124, then a `--beat` that lands, then an `s3` call whose push exits 124 | `s1 s2` | `s2` |
| b | as a, with `--dispatch` as the writer that lands | `s1 s2` | `s2` |
| c | as a, with the remote unreachable on the `s3` call | `s1 s2` | `s2` |
| d | `s2` and then `s3`, each with the remote unreachable | `s1 s2` | `s1` |
| e | an `s2` call whose push exits 124, then an `s2` call under a new `CLAUDE_PID` whose push exits 124 | `s1 s2` | `s1` |
| f | an `s2` call whose push exits 124, then an `s3` call whose push exits 124 | `s1 s2` | `s1` |

Under unit 20 S2's absent-only rule, a, b and c end in check 90. A set holding only the read claim's
session ends d in check 90. A fact written with the pre-call session unconditionally ends d, e and f
in check 90.

### Inventory

No new fact, function, check, conf key or file: `prior-session` is unit 20's, and its value changes
shape. No lexicon cell and no codebase-map key is minted.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/STOPS.template.md`, where unit 20's build describes the fact's value
- `memory/guides/UNATTENDED-STOPS.md`, by the render
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

### Alternatives rejected

- **Clear the fact on every landed claim write.** §3: it writes the record from the tick and after
  a status write has staged or pushed it.
- **Keep one value and overwrite it with the read claim's session.** §3: sequence d has no readable
  claim.
- **A sentinel word for the cleared state.** Any word is a value `CLAUDE_CODE_SESSION_ID` could hold,
  which is finding 7's shape; the empty value is the one `write_lease` never records.

## 5. Production-readiness checklist

- security — No new surface. Every member is a session id the run branch already publishes in the
  record's `session` line, and the widening still requires this run's own keepalive.
- perf / scale — One membership test per decision, in-process. The set grows by at most two values
  per incomplete call and empties on the first landed holder write.
- error / empty / loading states — §4 "The set across one `--resume` holder-row call".
- observability — The record's `prior-session` line lists every session the published claim may
  still carry.
- risks — A session id carrying a space would split into members none of which equals the claim's
  session, so such a run reads its claim as foreign, as it did before unit 20. Harness session ids
  carry no space.
- testing — §7's arms, each observed RED on its staged break first. The lost race is staged by unit
  1's `git` shim on `PATH`, never by a sleep.
- migration — A record unit 20's build wrote with `prior-session: absent`, its cleared spelling,
  reads here as the one-member set `absent`. That widens `mine` only to a claim under this run's own
  keepalive and session `absent`, and the next holder write that lands empties it.
- user docs — The stops guide, through S6, wherever unit 20's build says what the fact holds,
  re-rendered in the same commit.

## 6. Acceptance criteria

The fixture is unit 20's: a `git clone --local` of this repository under `%TEMP%`, its one remote
re-pointed at a bare repository, `RUN_CLAIMS` on, and a run whose record and claim both name session
`s1` and the recorded keepalive. A holder call is `--resume <slug> --keepalive-id <recorded id>`
under the session named. "Exits 124" is unit 20 AC2's `git` shim on `PATH`, which makes the claim
push exit 124; "unreachable" is the bare repository renamed away for that call and restored after
it. The claim is read with `git ls-remote <bare> refs/gov/runs/<slug>` and `git cat-file -p`, and
the set with the driver's `fact` over the run-state file. After every call, `git diff --name-only`
names no run-state file.

- **AC1** — When sequences a, b, c and d of §4 run, the set reads `s1 s2` before each closing `s3`
  call, and each closing call exits 0, prints no `UNATTENDED check 90 FAILED`, leaves a claim naming
  `session: s3`, and leaves `fact` printing nothing for `prior-session`. In a, `--beat <slug>` runs
  over unit 1's tick fixture, whose run `--liveness` reads `LIVE` on this host, and prints
  `unattended: beat — <slug> · renewed`. In b, `--dispatch <slug> --pass <a unit id of the fixture
  build> --writes <a path>` exits 0. After either, the claim names `session: s2` and the set still
  reads `s1`.
  Red when: a closing call answers check 90, or `--beat` or `--dispatch` changes the set.
- **AC2** — When sequences e and f of §4 run, the set reads `s1 s2` after the second incomplete
  call. The closing call, under `s2` for e and `s3` for f, exits 0, prints no
  `UNATTENDED check 90 FAILED`, leaves a claim naming that session, and leaves `fact` printing
  nothing for `prior-session`. Over the fixture as it starts, whose record carries no
  `prior-session` line, with the run-state file committed and the claim re-seeded at a `beat-utc`
  older than a quarter of `RESUME_STALE_BOUND`, an `s1` call with no shim moves the claim ref and
  leaves `git status --porcelain` empty.
  Red when: the second incomplete call loses `s1` from the set, which a build writing the pre-call
  session unconditionally does, or a landed holder write over a record without the fact writes it.
- **AC3** — When the fixture's record and claim both name session `absent`, written with
  `CLAUDE_CODE_SESSION_ID` unset, an `s2` holder call that exits 124 exits 0 and leaves the set
  reading `absent`. A closing `s2` call exits 0, prints no `UNATTENDED check 90 FAILED`, leaves a
  claim naming `session: s2`, and leaves `fact` printing nothing for `prior-session`.
  Red when: the reader treats a set holding `absent` as no fact, so the closing call answers
  check 90.
- **AC4** — When one `s2` holder call exits 124 and a `--dispatch` follows under `s2` with no shim,
  the dispatch exits 0, prints no `UNATTENDED check 90 FAILED`, and leaves a claim naming
  `session: s2`. In a second copy of the fixture, whose branch tip is pushed, the same incomplete
  call is followed by `--hold <slug> --code <a declared hold code> --until owner --reason <text>
  --reaped <the recorded keepalive>` with no shim. It prints no `unattended: claim not written` line
  and leaves a claim whose `status` reads `held`. In both copies the set still reads `s1`.
  Red when: the widening reaches only the `--resume` row, so `--dispatch` answers check 90 or
  `--hold` announces instead of writing.
- **AC5** — When sequence d of §4 runs and the next call is under `s3` with `CLAUDE_PID` changed, a
  new `--keepalive-id` and the remote restored, it takes the run over, prints no
  `UNATTENDED check 89 FAILED`, and leaves a claim naming the new keepalive and `session: s3`.
  Red when: the restart widening compares the whole value of the set with the claim's session.
- **AC6** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · sequences a, b and c of section 4, each ending in a closing s3 call with no check 90; stage unit 20's absent-only write rule · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · sequence d, two unreachable pushes, ending in a closing s3 call with no check 90; stage the set written as the read claim's session alone · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · sequences e and f, two incomplete calls in a row, ending in a closing call with no check 90; stage the fact written with the pre-call session unconditionally · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · an absent session leased, then an s2 call that exits 124, then a closing s2 call with no check 90; stage the reader treating absent as no fact · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · after one incomplete s2 call, --dispatch writes and --hold writes held with no announce; stage the set supplied to check_claim_writable from the --resume row only · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · after sequence d, the s3 restart under a new keepalive takes over with no check 89; stage the restart widening comparing the whole value · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs its criteria
directly, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from findings 6, 12, 2, 7 and 1 of the round-1 spec
  audit of units 20 to 22, grounded against `fact`, `set_fact`, `write_lease`, the holder row and
  the `hold-unpushed` clear at base `5266d22e`, and against units 1 and 20 as specced.
- rev-2 · 2026-10-04 · §2 §4 §5 §6 · S1 S4 S6 S7 · AC2 · from the bug-class checklist over the
  promoting commit, which selected `observed-by-claim-no-arm-discharges`,
  `retirement-inventory-misses-readers-by-value` and `a-folded-field-leaves-its-row-shape-docs-behind`.
  S4 names the sites its criteria drive and the four they do not; S7 rewrites unit 20's arms that
  assert the fact's old value; S6 reaches the stops guide; AC2 observes S3's "only when non-empty".

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "remember every session a published claim may still carry
when a push does not land, and clear it when one lands"` ranked name-stem neighbours only, `claims`
in `tools/codebase-map/selftest.py` and `extract_session` in `tools/runlog/extract.py`, and printed
`unscanned layers: .sh`, so its miss is no evidence. The seams were read from source: `set_fact` and
`fact`, and the `hold-unpushed` clear at `tools/unattended/unattended.sh:6369`, which already spells
a cleared run fact as the empty value written only when non-empty. No existing seam holds a set of
values in one run fact; the space-separated value is new. The recall probe returned unit 20, the
audit's H1 row, the round-2 audit's row that promoted unit 20, unit 18, and unit 1's `mine`
definition.

Recall terms used: prior-session claim CAS incomplete push holder mine session set cleared absent sticky fact

The question passed with them: "when a claim push does not complete twice, which sessions may the
published claim still carry and how is the cleared state spelled".
