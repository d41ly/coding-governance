# TOOL-aGraftedHelix-25 — the `prior-session` add's own failure returns the holder row before `write_lease`, observed by a criterion that fails the add itself

**Status:** SPECCED · rev-5 · 2026-10-05 · node a · Tier-2 · base 5266d22e · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-review-TOOL-aGraftedHelix-25-spec-audit-round1.md](../reviews/2026-10-05-review-TOOL-aGraftedHelix-25-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-24` moves the `prior-session` add ahead of `write_lease`, so an interruption
inside `write_lease` cannot leave the claim under a session no member names. The round-1 spec audit
of unit 24 confirmed one HIGH finding on that order.

- Finding 11: unit 24 S1 states no rule for the add's own failure. `set_fact` returns 2 without
  writing when `mktemp` fails, and returns `mv`'s status otherwise. A build that lets the row go on
  past a failed add runs `write_lease`, which moves the record to `s2` while the claim stays at
  `s1` and the set holds no `s1`. The next `s2` call answers check 108, or check 107 at the restart
  row, and the live run is forced to `--abort --code claim-lost`. Unit 24 AC1's shim fires only
  once the record reads `s2`, after the add, so no criterion separates that build from a correct
  one.

A protecting write placed ahead of the write it protects only protects if its own failure stops the
row. This unit states that rule and observes it with a criterion that fails the add itself. It
closes finding 11 (HIGH) of the round-1 spec audit of unit 24.

## 2. Scope (IN)

- **S1** — On a `--resume` holder-row call, on either of the add's two triggers, a CAS that did not
  complete and a claim that could not be read, a non-zero return from the add's `set_fact` returns
  the holder row 1 at once: before `write_lease`'s first `set_fact`, before `stage_or_fail`, and
  before the row's `lease recorded` line. The add is written `|| return 1`, the shape each of
  `write_lease`'s own facts takes (`tools/unattended/unattended.sh:5559` to `:5569`). `mv` is
  `set_fact`'s last command, so the one return covers a failed `mv` as well as a failed `mktemp`.
  The add's place is unit 24's; this adds its failure rule to unit 24 §4 "The order"'s add row.
  The return is already the code's: unit 23's build (`aeab6521`) wrote the add `|| return 1`, and
  unit 24's (`73dc1dbf`) moved it ahead of `write_lease` with the return kept, so this unit moves no
  driver byte. What it lands is the criterion: until AC1, no arm fails the add itself, so a later
  change dropping the return stays green.
  Observed by AC1 on the first trigger, which drives the `mktemp` half. The second trigger is NOT
  OBSERVED by a criterion here: `TOOL-aGraftedHelix-26` gives both triggers one call site and
  drives the unreadable one with a leg of its own (§3). The `mv` half is NOT OBSERVED by a criterion
  here, because both halves reach the row through the same return.
  - **Readers:** by name: `tools/unattended/unattended.sh` holds the holder row whose add takes the
    return, and `tools/unattended/unattended.test.sh` holds the arm that drives it. by value: NO
    VALUE READERS at this unit: the process exit is 0 with or without the rule, because the
    dispatcher discards the verb's return and only `fail` sets `status` (§4 Evidence), as a failed
    `write_lease` fact also exits 0 at `:6599`. What callers of `--resume` read on a failed add is
    `TOOL-aGraftedHelix-26`'s (§3).
- **S2** — `tools/unattended/unattended.test.sh` gains the arm §7 names. NOT OBSERVED by a criterion
  here: the suite is the main loop's to run at VERIFYING, and the arm's red on its staged break is
  observed there (§7).
- **S3** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs: the suite is an `engine` file of the kit
  (`python tools/govkit/govkit.py shipped`), so S2 alone moves the kit's shipped bytes. Observed by
  AC2.

## 3. Non-goals (OUT)

- **The clear's own failure.** A failed clear after a landed CAS leaves members the claim no longer
  carries, the safe direction unit 24 S1 states, and the next `--resume` holder-row claim write that
  lands writes it again (unit 23 S3).
- **The failed add's message and exit status.** Here `set_fact`, `mktemp` or `mv` names the failure
  on stderr, and the exit is not this unit's to set, because the dispatcher discards the verb's
  return. Both are `TOOL-aGraftedHelix-26`'s (§3).
- **Every other `set_fact` caller.** Base chains some with `&&` and no return (`:7662`), and their
  writes protect nothing that precedes them. This unit is the one protecting write the holder row
  places ahead of the write it protects.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-24` — the add's place ahead of `write_lease`, AC1's fixture
  and the interruption arm; the `mktemp` shim is re-keyed here on the `git` shim's 124 marker (§6).
  Without the add ahead of `write_lease` there is no protecting write whose failure could stop the
  row before it.
- **hands-off** `TOOL-aGraftedHelix-26` — `fail 17` beside the add's `return 1`, so a failed add
  exits the call 1; the add's one call site for both triggers; and the unreadable trigger's leg
  (findings 5, 8 and 6 of the round-1 audit of this unit).

## 4. Design

### Evidence

- `set_fact` (`tools/unattended/unattended.sh:5509`) takes its temporary file with
  `tmp=$(mktemp) || return 2` (`:5528`), before it writes anything, and ends with `mv`, whose
  status it returns.
- `write_lease` (`:5557`) ends every `set_fact` with `|| return 1` (`:5559` to `:5569`), and the
  holder row returns when `write_lease` fails (`:6599`), before its `stage_or_fail`.
- Unit 1 §4 "Call sites" gives the holder row's not-completed CAS "announce, continue", so the
  announce line is printed at the CAS outcome, which unit 24 §4 "The order" places ahead of the add.
- The dispatcher runs `verb_resume` and discards its return (`:10561`), the script ends with
  `exit "$status"` (`:10576`), and only `fail` sets `status` (`:637`). `set_fact`'s `mktemp` and
  `mv` branches call no `fail`, so the row's return reaches no caller's exit.

### The add row's failure rule

Unit 24 §4 "The order" owns the add row, its trigger and its place. This unit adds one thing to
it: when the add's `set_fact` returns non-zero, the row returns 1, and no step after the add runs.

### What a failed add leaves, on an `s2` call whose CAS did not complete or whose claim was unreadable

| record `session` | set | claim | `lease-utc` | the next `s2` call |
|---|---|---|---|---|
| `s1` | as before the call | `s1` | as before the call | `write_lease` due, the claim `mine` by the record's session |

A failed add writes nothing, so the record is as clean as before the call, and the next call
retries the CAS from the same state.

### Inventory

No new fact, function, check, conf key or file. The add's return already stands (S1); the suite
gains one arm. No lexicon cell and no codebase-map key is minted.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

### Alternatives rejected

- **A shell-hygiene scan flagging a holder-row `set_fact` with no `|| return` on its line.** The row
  has no boundary a line scanner can derive, and base carries `set_fact` calls chained with `&&`
  that protect nothing (`:7662`), so the scan needs a row marker or a waiver list. That is a gate of
  its own, a separate mechanism under the method's one-mechanism rule, and the arm below reds on
  the dropped return, which is this class's regression gate here.
- **Key the shim on a count of `mktemp` calls.** The claim read and the CAS take temporary files
  too, and a later change to either moves the count. The shim keys on the `git` shim's 124 instead.
- **Fold the rule into unit 24.** It is a HIGH finding of unit 24's audit, and the method promotes a
  HIGH to a unit whose mechanism closes it.

## 5. Production-readiness checklist

- security — No new surface. The row returns earlier on a failure it already could not survive.
- perf / scale — None: the add is the same one `set_fact`.
- error / empty / loading states — §4 "What a failed add leaves".
- observability — `set_fact`, `mktemp` or `mv` names the failure, and the record's `session` line
  still names the pre-call session, so the state reads as the call never having run.
- risks — A later change that drops the return reopens finding 11's window silently; §7's arm is
  observed red on exactly that break.
- testing — §7's arm, observed RED on its staged break first. The failure is staged by a `mktemp`
  shim keyed on the `git` shim's 124, never by a sleep or a count.
- migration — None: no stored value changes.
- user docs — None: the stops guide describes what the fact holds, which this unit does not change.

## 6. Acceptance criteria

The fixture is `TOOL-aGraftedHelix-24` AC1's: unit 23's fixture, whose record and claim both name
session `s1` and the recorded keepalive, with the claim push exiting 124 through unit 20 AC2's `git`
shim on `PATH`. Here the `git` shim also creates a marker file when it makes the claim push exit
124, and a `mktemp` shim on `PATH` forwards to the real `mktemp` until that marker exists, then
exits 1 once and forwards again. A holder call is `--resume <slug> --keepalive-id <recorded id>`
under the session named, with `CLAUDE_PID` unchanged from the fixture's. The claim is read with
`git ls-remote <bare> refs/gov/runs/<slug>` and `git cat-file -p`, and the set with the driver's
`fact` over the run-state file.

- **AC1** — When an `s2` holder call runs with the claim push exiting 124 and that `mktemp` shim,
  it prints unit 1's announce line for a holder claim write that did not land and leaves the
  run-state file reading `session: s1`, `fact` printing nothing for `prior-session`, and
  `lease-utc` at its pre-call value. The announce line and the empty set together are the leg's
  witness that the shim failed the add itself: a shim that fires inside the CAS step's outcome
  either stops the row before the announce or lets the add run and write `s1`, and one that fires
  after the add leaves `s1` in the set, so each reds this criterion. A second `s2` call with no shim
  exits 0, prints no `UNATTENDED check 108 FAILED`, leaves a claim naming `session: s2`, leaves
  `fact` printing nothing for `prior-session`, and leaves `git diff --name-only` naming no run-state
  file. The first call's exit status is not asserted here: the dispatcher discards the verb's
  return (§4 Evidence), and `TOOL-aGraftedHelix-26` AC1 asserts it as exactly 1.
  Red when: the add's failure does not stop the row, so `write_lease` moves the record to `s2` with
  no `s1` in the set and the second call answers check 108.
- **AC2** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the kit's shipped bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · an s2 holder call whose claim push exits 124 and whose add a mktemp shim keyed on the git shim's 124 marker fails, asserting the announce line, session s1 and an empty set, then a second s2 call with no check 108; stage the add's return dropped · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs its criteria
directly, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 11 (HIGH) of the round-1 spec audit of
  unit 24, grounded against `set_fact`, `write_lease` and the holder row at base `5266d22e`, and
  against units 1, 23 and 24 as specced.
- rev-2 · 2026-10-04 · §4 · from the bug-class checklist over the promoting commit, which selected
  `two-answers-to-one-question`. §4 no longer restates unit 24's add row as a table of its own; it
  points at that row and states only the failure rule it adds.
- rev-3 · 2026-10-04 · §2 §3 §4 §6 · S1 · AC1 · folded the round-1 spec audit of this unit. Findings
  1 and 10 (MEDIUM): S1 names both of the add's triggers and labels the unreadable one NOT OBSERVED
  here, pointing at `TOOL-aGraftedHelix-26`, whose leg drives it, and §4's table heading names the
  unreadable call. Finding 3 (LOW): AC1 no longer asserts "exits non-zero"; its exit is the
  promoted unit's to assert as exactly 1. Finding 7 (LOW): the Edges entry names the `mktemp` shim
  as re-keyed here, not consumed. Findings 5, 8 and 6 (all HIGH) are promoted to
  `TOOL-aGraftedHelix-26`: §3 gains its hands-off, §4 Evidence states why the row's return reaches
  no exit, and S1's by-value readers line and the failed-add non-goal point at it.
- rev-4 · 2026-10-04 · §2 · S1 · from the bug-class checklist over the promoting commit, which
  selected `retirement-inventory-misses-readers-by-value`. S1's by-value readers line spells the
  NO VALUE READERS answer the grammar names and says why: the exit is 0 with or without the rule.
- rev-5 · 2026-10-05 · §1 §2 §4 §6 §7 · S1 S3 · AC1 AC2 · the build pass's divergences, before the
  code. The claim refusals were renumbered before the reconciling merge at `909c5e0b`, because
  main's own driver already uses 89 to 106: check 90 reads as check 108 and check 89 as check 107
  throughout. The driver at this unit's start already returns the row on a failed add (unit 23's
  build wrote the `|| return 1`, unit 24's kept it), so S1 says so and §4 drops the driver from the
  files touched; the unit lands the arm. S3 and AC2 name the kit's shipped bytes rather than the
  driver's, since the suite is an `engine` file and moves the version alone.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "stop a row when a protecting run-fact write fails,
before the write it protects"` ranked name-stem neighbours only, `run` across the Python tools and
`write` in `tools/memory-tree/gotchas.py`, and printed `unscanned layers: .sh`, so its miss is no
evidence. The seam was read from source: `write_lease`'s `|| return 1` on each `set_fact`, and the
holder row's return when `write_lease` fails. That shape fits, and the change reuses it on the add.
The recall probe returned unit 20, the round-1 audit of unit 23's H1 row, unit 24, the round-1 audit
of unit 24's H1 row, unit 23 and unit 18.

Recall terms used: prior-session set_fact return failure holder write_lease mktemp add order interrupted claim-lost

The question passed with them: "when the prior-session add's own write fails, must the holder row
stop before write_lease".
