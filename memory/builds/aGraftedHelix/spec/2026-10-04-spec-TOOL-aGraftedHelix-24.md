# TOOL-aGraftedHelix-24 — the `prior-session` add runs before `write_lease` moves the record's session, and the criteria that certify the set's readers start from the state and the session they need

**Status:** SPECCED · rev-3 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-review-TOOL-aGraftedHelix-24-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aGraftedHelix-24-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-23` makes the `prior-session` fact a set that a `--resume` holder-row call adds
to when its claim CAS does not land, and that `check_claim_writable` reads at every holder,
status-write and restart site. The round-1 spec audit of unit 23 confirmed three HIGH findings.

- Finding 11: unit 23 S2 places the add only "before its `stage_or_fail`", so under unit 20 §4
  "The order" it follows `write_lease`. `write_lease` writes `session` and then four more facts,
  each ending `|| return 1`. A failure or kill between its `session` line and the add leaves the
  record at `s2`, the claim at `s1` and no `s1` in the set. The next call answers check 90, or check
  89 at the restart row, and the live run is forced to `--abort --code claim-lost`.
- Finding 6: unit 23 AC5 runs its restart after sequence d's closing call. That call empties the
  set and leaves the claim at `s3`, so the restart is unit 1's plain same-session row and S5's
  membership test is never reached.
- Finding 1: unit 23 AC4's `--hold` names no session. Under the fixture's `s1` it writes through
  the same-session row, so it never exercises the status-write widening it is the only criterion
  for.

This unit moves the add ahead of `write_lease` and drives the interruption. It makes the restart
criterion stop short of sequence d's closing call and assert the state it needs, and it names the
session on every criterion call that is not `--resume`. It closes findings 11, 6 and 1 (all HIGH)
of the round-1 spec audit of unit 23.

## 2. Scope (IN)

- **S1** — On a `--resume` holder-row call whose `write_lease` is due, the add to the set runs once
  the claim read and the CAS outcome are known, and BEFORE `write_lease`'s first `set_fact`, on each
  of the add's two triggers: a CAS that did not complete, and a claim that could not be read. Both
  are known by then, because unit 20 S1 runs the claim read and the CAS ahead of `write_lease`. The
  `stage_or_fail` already inside the `write_lease`-due branch stages the add with the lease lines.
  The add's own failure rule is `TOOL-aGraftedHelix-25`'s (§3). This supersedes unit 23 S2's "before
  its `stage_or_fail`" and the `prior-session` row of unit 20 §4 "The order", which follows
  `write_lease`. Observed by AC1, one leg per trigger.
  The clear keeps its place after `write_lease`. An interruption before the clear leaves members the
  claim no longer carries, which widen `mine` only to this run's own keepalive, and the next
  `--resume` holder-row claim write that lands (unit 23 S3) empties them. NOT OBSERVED by a
  criterion here: after a landed CAS the claim carries the caller's own session, and unit 1 §4's
  holder column answers the next call under that session through its `mine` or `same session` row
  whatever the set holds, so no verdict depends on the clear's place.
  The comment at the row names this order. NOT OBSERVED by a criterion here: it is prose, and AC1
  observes run-state facts, the claim and exit codes.
  - **Readers:** by name: `tools/unattended/unattended.sh` holds the holder row whose add moves and
    the comment that states its order, and `tools/unattended/unattended.test.sh` holds unit 23's
    arms that drive the row. by value: `check_claim_writable`'s holder and status-write read and
    the restart row's membership test read `s1` after an interrupted `write_lease`, where they read
    nothing before. Neither changes, because each already reads the set (unit 23 S4, S5).
- **S2** — Every criterion call of unit 23 that is not `--resume` names its session. The `--beat`
  of sequences a and c runs with `CLAUDE_CODE_SESSION_ID` unset, because the OS-scheduled tick runs
  it that way. Sequence b's `--dispatch` and AC4's `--hold` run under `s2`, as AC4's `--dispatch`
  already does. Neither runs under `s1`: unit 1 §4's columns test `mine` before `same session`, so
  under `s1` a `--dispatch` or a `--hold` whose widening is absent reaches the `same session` row,
  which takes or writes, and neither call could red. This supersedes unit 23 AC1, AC4 and AC5's
  sequence-c leg for those calls, wherever they run. Observed by AC2 and AC3.
- **S3** — Unit 23 AC5's sequence-d leg starts from sequence d up to, but not including, its
  closing call. It asserts that the set reads `s1 s2` and the claim names `session: s1` immediately
  before the restart call. This supersedes unit 23 AC5's "When sequence d of §4 runs" and its §7
  restart arm's "after sequence d". Observed by AC4.
- **S4** — `tools/unattended/unattended.test.sh` gains the interruption arm, and the arms of unit 23
  that S2 and S3 name are rewritten, as §7 lists. NOT OBSERVED by a criterion here: the suite is the
  main loop's to run at VERIFYING, and each arm's red on a staged break is observed there (§7).
- **S5** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC5.

## 3. Non-goals (OUT)

- **Moving the clear ahead of `write_lease`.** No verdict depends on the clear's place (S1): after a
  landed CAS the claim carries the caller's own session, which the `mine` or `same session` row
  answers whatever the set holds. Moving it would supersede unit 20 §4's and unit 23 S3's order and
  change no verdict.
- **Staging the record on a holder call that writes nothing.** A continuing outage leaves an
  interrupted record unstaged until a claim write lands (§4). Staging on every holder call would
  spend a `git` spawn on every idle-wake tick against the row's "writes NOTHING unless" contract
  (`tools/unattended/unattended.sh:6592`), and the gap is unit 20's order's already: an interrupted
  `write_lease` returns before its `stage_or_fail` (`:6599`).
- **Writing the set and the lease in one atomic write.** `set_fact` rewrites one key per call
  through `mktemp` and `mv`, and a combined writer is a new function beside it. Ordering the add
  first closes the window without one.
- **The restart legs unit 23 AC5 already starts short of a closing call.** Its rev-3 legs after
  sequence c and over an `absent` lease state their own preconditions; this unit corrects the
  sequence-d leg's starting point only, and S2's session rule also reaches the `--beat` inside the
  sequence-c leg.
- **`--close`, `--landed`, `--abort` and the LANDING re-bind.** Unit 23 S4 labels them NOT
  OBSERVED, and the read's place inside `check_claim_writable` is what reaches them. This unit names
  sessions on the calls unit 23's criteria already make.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-23` — the set, its add and clear, the read inside
  `check_claim_writable`, the sequences of its §4, the criteria AC1, AC4 and AC5 this unit rewrites,
  and the fixture and arms; without them there is no add to move and no criterion to correct.
- **consumes-from** `TOOL-aGraftedHelix-20` — §4 "The order", which runs the claim read and the CAS
  ahead of `write_lease`, and whose `prior-session` row this unit moves ahead of it; without that
  order the CAS outcome is not known before `write_lease` and the add cannot precede it.
- **hands-off** `TOOL-aGraftedHelix-25` — the add's own failure rule: a non-zero return from the
  add's `set_fact` returns the holder row before `write_lease`, with a criterion leg whose shim
  fails the add itself and an arm staging the dropped return (finding 11 of the round-1 audit of
  this unit).

## 4. Design

### Evidence

- `write_lease` (`tools/unattended/unattended.sh:5557`) writes `keepalive`, then `session` at
  `:5563`, then `pid`, `host`, `pid-image` and `lease-utc`, each by `set_fact` and each ending
  `|| return 1`.
- `set_fact` (`:5509`) takes its temporary file with `tmp=$(mktemp) || return 2` (`:5528`), a
  `PATH` lookup, so a `mktemp` shim on `PATH` reaches every fact write.
- The holder row returns when `write_lease` fails (`:6599`), before its `stage_or_fail`.
- After an interruption between `write_lease`'s `session` and `pid` lines, the record names the
  harness's session and pid, so the next call's `write_lease` is not due (`:6597`). That call
  reaches the claim through the `mine` test alone, which is what makes the set's content decide it.
- An unreachable remote leaves the claim unreadable, and the holder path keeps working offline (unit
  1 §4 "Call sites"), so the add's second trigger reaches the add with no CAS attempted.
- `run_hold` (`:4837`) never calls `check_keepalive_reaped`, so `--hold` binds to no lease session
  and its claim verdict is decided by the environment's session against the claim's.
- The restart row holds when the recorded session equals the environment's and the recorded pid
  does not (`:6612-6615`).

### The order

| step | reads | writes |
|---|---|---|
| claim read, `mine` test, check 90 | the record's facts before the call, the set included | nothing |
| the stamp, when `write_lease` is due | the clock, once | nothing |
| claim CAS, when due | the values `write_lease` is about to record, and the stamp | the claim |
| the add, when `write_lease` is due and the CAS did not complete or the claim was unreadable | the CAS outcome, the claim read, the record's `session` before the call | `prior-session` |
| `write_lease`, when due | the environment, and the stamp as its third argument | the record's lease facts |
| the clear, when the claim write landed and the set is non-empty | the CAS outcome | `prior-session`, then its own `stage_or_fail` when `write_lease` was not due |
| `stage_or_fail` | nothing | the index, when `write_lease` ran or `prior-session` was written |

Every row but the add's is unit 20 §4's, restated so the add's place reads in context; unit 20 §4
owns them. The add's own failure rule is `TOOL-aGraftedHelix-25`'s (§3).

### What an interruption leaves, on an `s2` call whose CAS did not complete or whose claim was unreadable

| stopped after | record `session` | set | claim | the next `s2` call |
|---|---|---|---|---|
| the add | `s1` | holds `s1` | `s1` | `write_lease` due, the claim `mine` by the record's session |
| `write_lease`'s `session` line | `s2` | holds `s1` | `s1` | `write_lease` not due, the claim `mine` through the set |
| `write_lease` | `s2` | holds `s1` | `s1` | as the row above |

Each interrupted call leaves the record unstaged. In row 1 the record's session (`s1`) differs
from the next call's (`s2`), so that call's `write_lease` is due and the `stage_or_fail` inside its
branch stages the record. In rows 2 and 3 the claim (`s1`) differs from the record's session
(`s2`), so the next call whose claim write lands renews it, and unit 23 S3's clear stages the
record. A call in rows 2 and 3 whose `write_lease` is not due and whose claim write does not land,
which is what a continuing outage gives, stages nothing: unit 23's set table writes nothing for it,
and the `stage_or_fail` inside the due branch (`tools/unattended/unattended.sh:6597` to `:6600`) is
the row's only other staging point. The record stays unstaged until a claim write lands or another
writer stages the file, and §3 says why this unit leaves that gap. AC1's unreachable leg drives
the still-incomplete call for its verdict and the restored call for the staging.

### Inventory

No new fact, function, check, conf key or file. The add moves within the holder row. No lexicon
cell and no codebase-map key is minted.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

### Alternatives rejected

- **Count `mktemp` calls in the shim.** The claim CAS and the add take temporary files too, and a
  later change to either moves the count. The shim keys on the record's own `session:` line instead.
- **Run the interruption arm with a kill.** A kill is timed against a running process and needs a
  sleep or a poll. A shim that fails one `set_fact` stops the row at the same line every time.
- **Correct unit 23's criteria in its own spec.** They are HIGH findings of its audit, and the method
  promotes a HIGH to a unit whose mechanism closes it.

## 5. Production-readiness checklist

- security — No new surface. The add writes the same members unit 23 defines, earlier in the row.
- perf / scale — None added: the add was already one `set_fact` on the same calls.
- error / empty / loading states — §4 "What an interruption leaves", with the continuing outage in
  its closing paragraph.
- observability — The record's `prior-session` line names the claim's session at every point an
  interruption can stop the row.
- risks — A future fact written in `write_lease` ahead of `session` does not reopen the window,
  because the add precedes the whole function. A reader that assumes the set is written after the
  lease would read the order wrong; unit 20 §4 states the order, and §4's table restates it with
  the add moved.
- testing — §7's arms, each observed RED on its staged break first. The interruption is staged by a
  `mktemp` shim keyed on the record's state, never by a sleep.
- migration — None: no record carries a set before unit 23 lands, and the add's place changes no
  stored value.
- user docs — None: unit 23 S6's lines describe what the fact holds, which this unit does not change.

## 6. Acceptance criteria

The fixture is unit 23's: a `git clone --local` of this repository under `%TEMP%`, its one remote
re-pointed at a bare repository, `RUN_CLAIMS` on, and a run whose record and claim both name session
`s1` and the recorded keepalive. A holder call is `--resume <slug> --keepalive-id <recorded id>`
under the session named. "Exits 124" is unit 20 AC2's `git` shim on `PATH`, which makes the claim
push exit 124; "unreachable" is unit 23's, the bare repository renamed away for that call, and
"restored" renames it back. The claim is read with `git ls-remote <bare> refs/gov/runs/<slug>` and
`git cat-file -p`, and the set with the driver's `fact` over the run-state file.

- **AC1** — When an `s2` holder call runs with the claim push exiting 124 and a `mktemp` shim on
  `PATH` that forwards to the real `mktemp` until the run-state file's `session:` line reads `s2`,
  then exits 1 once, the call exits non-zero and the run-state file reads `session: s2` and
  `prior-session: s1`, with its `lease-utc` line still at its pre-call value. That unmoved stamp is
  the arm's witness that the shim stopped `write_lease` after its `session` line; a call that ran
  `write_lease` whole proves nothing about the order and reds this criterion. A second `s2` call
  with no shim exits 0, prints no `UNATTENDED check 90 FAILED`, leaves a claim naming
  `session: s2`, leaves `fact` printing nothing for `prior-session`, and leaves
  `git diff --name-only` naming no run-state file. Over a fresh copy of the fixture, an `s2` holder
  call with the remote unreachable and the same shim exits non-zero and leaves `session: s2`,
  `prior-session: s1` and `lease-utc` unmoved, as above. A second `s2` call with the remote still
  unreachable and no shim exits 0, prints no `UNATTENDED check 90 FAILED`, and leaves the set
  reading `s1`. A third `s2` call with no shim and the remote restored makes the second call's
  assertions of the first leg.
  Red when: the add runs after `write_lease` on either trigger, so the interrupted call leaves no
  `s1` in the set and the next call that reads the claim answers check 90.
- **AC2** — When unit 23's sequences a and c run with their `--beat` under `CLAUDE_CODE_SESSION_ID`
  unset, and sequence b with its `--dispatch` under `s2`, each `--beat` prints
  `unattended: beat — <slug> · renewed` and the `--dispatch` exits 0 with no
  `UNATTENDED check 90 FAILED`. After either, the claim names `session: s2` and the set reads `s1`.
  Red when: `--beat` prints a skipped line or `--dispatch` answers check 90, which a build reading
  the set only at the `--resume` row does once the call cannot take the same-session row.
- **AC3** — When unit 23 AC4's second fixture copy runs its incomplete `s2` call and the commit and
  push of its setup, and its `--hold` then runs under `CLAUDE_CODE_SESSION_ID` `s2`, the `--hold`
  prints no `unattended: claim not written` line and leaves a claim whose `status` reads `held`.
  Red when: the set is read in holder mode only, so `--hold` announces instead of writing.
- **AC4** — When unit 23's sequence d runs up to, but not including, its closing call, the set
  reads `s1 s2` and the claim names `session: s1`. The next call, under `s3` with `CLAUDE_PID`
  changed, a new `--keepalive-id` and the remote restored, takes the run over, prints no
  `UNATTENDED check 89 FAILED`, and leaves a claim naming the new keepalive and `session: s3`.
  Red when: the restart widening compares the whole value of the set with the claim's session, so
  the call answers check 89.
- **AC5** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · an s2 holder call whose claim push exits 124 and whose write_lease a mktemp shim stops after its session line, then a second s2 call with no check 90; over a fresh copy, the same shim on an s2 call with the remote unreachable, a still-unreachable s2 call with no check 90, and a restored s2 call with no check 90; stage the add moved back after write_lease, and separately the unreadable-claim path's add alone moved back, observed red through the unreachable leg · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · unit 23's a/b/c arm and its sequence-c restart arm with every --beat under CLAUDE_CODE_SESSION_ID unset and --dispatch under s2; stage the set supplied to check_claim_writable from the --resume row only, observed red through the --beat and --dispatch calls · none, the arm is unit 23's and is rewritten

New arm: tools/unattended/unattended.test.sh · unit 23's --hold arm with --hold under s2; stage the set supplied to check_claim_writable in holder mode only, observed red through the --hold leg alone · none, the arm is unit 23's and is rewritten

New arm: tools/unattended/unattended.test.sh · unit 23's sequence-d restart arm started short of d's closing call, asserting the set reads s1 s2 and the claim s1 before the restart; stage the restart widening comparing the whole value · FLOOR_ASSERTIONS rises by the assertions the rewrite adds, and FLOOR_SHARD_2 with it where the arm sits in region two, counted off the block

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs its criteria
directly, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from findings 11, 6 and 1 (all HIGH) of the round-1
  spec audit of unit 23, grounded against `write_lease`, `set_fact`, the holder row, `run_hold` and
  the restart row at base `5266d22e`, and against units 20 and 23 as specced.
- rev-2 · 2026-10-04 · §6 · AC1 · from the bug-class checklist over the promoting commit, which
  selected `fixture-passes-by-finding-nothing`. AC1 asserts the interrupted call leaves `lease-utc`
  at its pre-call value, so a shim that never fires cannot pass the criterion.
- rev-3 · 2026-10-04 · §2 §3 §4 §5 §6 §7 · S1 S2 S3 · AC1 · folded the round-1 spec audit of this
  unit. Finding 2 (MEDIUM): S1 names both of the add's triggers, §4 Evidence the unreadable one,
  and AC1 gains a leg on the unreachable remote, with the first arm staging that path's add moved
  back. Finding 10 (MEDIUM): §4's closing paragraph names when the next call stages the record and
  states the continuing-outage gap, §3 gains the non-goal that leaves it, and AC1's unreachable leg
  drives a still-unreachable call. Finding 5 (LOW): that paragraph gives row 1 its own reason.
  Findings 1 and 3 (LOW): S1's clauses on the clear's place and on the comment are labelled NOT
  OBSERVED with their reasons, and §3's rationale for keeping the clear is corrected. Finding 4
  (LOW): S1 names the `--resume` holder-row claim write as the one that empties the set. Finding 6
  (LOW): S1's by-value readers line names the readers the add changes. Finding 7 (LOW): §3 and S2's
  supersession reach AC5's sequence-c leg. Finding 13 (LOW): S2's rationale cites unit 1 §4's row
  order. Finding 8 (LOW): S3 quotes unit 23 AC5 as written. Finding 14 (LOW): §4 "The order"
  restores unit 20's two staging qualifiers and points at unit 20 §4, and §5 risks follows. Finding
  15 (LOW): the fourth arm's floor field counts the assertions it adds. Finding 11 (HIGH) is
  promoted to `TOOL-aGraftedHelix-25`: §3 gains its hands-off, and S1 and §4 point at it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "record which sessions a published claim may carry
before the lease record is rewritten, so an interrupted write leaves no gap"` ranked name-stem
neighbours only, `write` in `tools/memory-tree/gotchas.py` and `resolveLease` in
`tools/unattended/run-lease.js`, and printed `unscanned layers: .sh`, so its miss is no evidence.
The seams were read from source: `write_lease` and `set_fact` in `tools/unattended/unattended.sh`,
and the holder row's `write_lease`-due branch. No existing seam fits a new writer, and none is
needed: the change is the position of unit 23's one `set_fact`. The recall probe returned unit 20,
the round-1 audit of unit 23's H1 row, unit 18's order table, unit 11, and `TOOL-dDerivedDocket-61`,
the ruling that the lease is one record of run-state facts.

Recall terms used: prior-session write_lease set_fact interrupted crash window holder mine claim session order

The question passed with them: "when the lease write is interrupted after the session line, which
session does the published claim still carry".
