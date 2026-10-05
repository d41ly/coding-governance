# TOOL-aGraftedHelix-26 — a failed `prior-session` add or `write_lease` fact fails the call through check 17, and both of the add's triggers reach one guarded call site, each observed

**Status:** SPECCED · rev-3 · 2026-10-05 · node a · Tier-2 · base 5266d22e · streams tooling · order 8

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-25` returns the holder row 1 when the `prior-session` add's own `set_fact`
fails, so `write_lease` never runs past a failed add. The round-1 spec audit of unit 25 confirmed
three HIGH findings, which are two defects.

- Findings 5 and 8: the row's return never reaches the process exit. The dispatcher runs
  `verb_resume` bare (`tools/unattended/unattended.sh:10561`), the script ends with
  `exit "$status"` (`:10576`), and only `fail` sets `status` (`:637`). `set_fact`'s `mktemp` branch
  returns 2 with no `fail` (`:5528`), and so does its trailing `mv`. A failed add therefore exits
  0: unit 25 AC1's "exits non-zero" reds a build made exactly as its S1 writes it, and the failure
  is invisible to every caller of `--resume`. Unit 24 AC1 rests on the same premise for a failed
  `write_lease`, whose return exits 0 the same way.
- Finding 6: unit 24 S1 gives the add two triggers, a CAS that did not complete and a claim that
  could not be read, and unit 25 AC1 drives only the first. A build that guards only the CAS path's
  add passes it, and on an unreachable remote with a failed add runs `write_lease`, so the next
  `s2` call answers check 108 and the run is forced to `--abort --code claim-lost`.

This unit makes a failed add and a failed `write_lease` fact each set the exit through check 17,
gives the add one call site for both triggers, pins that the row pushes no claim it could not read,
and drives the unreadable trigger with a leg of its own. It closes findings 5, 8 and 6 (all HIGH)
of the round-1 spec audit of unit 25.

## 2. Scope (IN)

- **S1** — The add's `set_fact` is written
  `|| { fail 17 "cannot record a run fact: prior-session in $rel"; return 1; }`, so a failed add
  exits the `--resume` call 1 with that line. Check 17 is `set_fact`'s own "cannot record a run
  fact" refusal (`:5525`), so no check number is minted. `set_fact`'s three earlier refusals
  (`:5512`, `:5516`, `:5525`) already call `fail 17`, so on those paths the call prints two check-17
  lines; a criterion asserts the line is present, never how many there are. This supersedes unit 25
  S1's `|| return 1` shape and its by-value readers line, and unit 25 §3 "A new message for the
  failed add". Observed by AC1 and AC3, one leg per trigger.
  - **Readers:** by name: `tools/unattended/unattended.sh` holds the add, and
    `tools/unattended/unattended.test.sh` holds the arms that drive it. by value: every caller of
    `--resume` reads the process exit, which a failed add now makes 1 where unit 25's build leaves
    0, and stdout, which now carries the check-17 line. A `--resume` that refuses already exits 1
    through `fail` on its other paths, so the value is not a new one to those callers.
- **S2** — The six `set_fact` lines in `write_lease` (`:5559` to `:5569`) become ONE `set_fact`
  in a loop over the six facts in their written order, `keepalive session pid host pid-image
  lease-utc`, each value computed in its arm exactly as before, the two probes included, and that
  one line is written `|| { fail 17 "cannot record the lease: $k in $rel"; return 1; }`, naming the
  fact through the loop's variable. One guarded site, for S3's reason: a seventh lease fact cannot
  skip the guard, and the harness-arms leg keys every `fail` call site by its literal text, so six
  literal fact names would be six branches of which §6 drives one. A
  failed lease fact then exits 1 at every caller, each of which returns on it already with no
  `fail` of its own: `--preflight` (`:5324`), `run_takeover` (`:6356`), the LANDING re-bind
  (`:6532`), the holder row (`:6599`) and `--replaces` (`:6658`). This makes unit 24 AC1's exit
  status, which that criterion no longer asserts, this unit's to observe. Observed by AC2.
  - **Readers:** by name: `tools/unattended/unattended.sh` holds `write_lease` and its five callers,
    and `tools/unattended/unattended.test.sh` holds the arm that drives it. by value: every caller
    of `--preflight` and `--resume` reads exit 1 and the check-17 line on a failed lease fact, where base gave 0 on the `mktemp` and `mv` branches and 1
    on `set_fact`'s three earlier refusals.
- **S3** — Both of the add's triggers reach ONE `set_fact` call site, the one S1 guards. The value
  it writes is computed per trigger as unit 23 S2 states; the write is one line. This supersedes
  any per-trigger add site a build of units 23 to 25 made. It already stands at this unit's
  start: the add is one `set_fact` under `cas != 0`, which both triggers take, because a claim
  that could not be read leaves `cw` empty, so no CAS runs and `cas` stays empty. No driver byte
  moves for S3. Observed by AC1 and AC3, one leg per
  trigger. The single site itself is NOT OBSERVED as a count by a criterion here: the clear writes
  the same fact, so a count of call sites cannot tell an add from a clear, and each trigger's leg
  observes the return that trigger takes, which is what the single site is for.
- **S4** — On a holder-row call whose claim read did not answer, the row pushes no claim. A
  `write_claim` CAS leases against the sha the read observed (unit 1 S3), and a read that did not
  answer observed none; an empty expected sha asserts a create, which a remote that answers the
  push but not the fetch reports as lost, and the holder row answers a lost race with check 108 on a
  claim this run holds. This narrows unit 20 S1's CAS to a call whose claim read answered. It
  already stands at this unit's start: the holder row's CAS runs only under `[ -n "$cw" ]`, and
  `cw` is set only when `read_claims` answered. No driver byte moves for S4. Observed
  by AC3.
- **S5** — `tools/unattended/unattended.test.sh` gains the arms §7 names. NOT OBSERVED by a
  criterion here: the suite is the main loop's to run at VERIFYING, and each arm's red on its
  staged break is observed there (§7).
- **S6** — The unattended kit version moves once after this unit's last move, in every carrier
  `tools/check-kit-versions.sh` pairs. Observed by AC4.

## 3. Non-goals (OUT)

- **A `fail` inside `set_fact`'s `mktemp` and `mv` branches.** The rotation copy
  (`tools/unattended/unattended.sh:5095` to `:5098`) chains `set_fact` with a fallback that
  tolerates its failure, and `:7662` writes `gates-run` best-effort. A `fail` there turns a
  tolerated miss into a failed verb. Each protecting caller states its own `fail` instead.
- **Every other `set_fact` caller.** Unit 25 §3 states why, and this unit adds a `fail` only at the
  add and inside `write_lease`, whose five callers all return on it.
- **The clear's own failure.** Unit 25 §3 states why a failed clear is the safe direction.
- **The `memory/gotchas/` class records the audit proposes**, that a verb's return is not the
  process exit, and that a scope item with more than one trigger names a criterion leg per trigger.
  They are the close's left-shift under BUILD-METHOD M8, recorded in a records commit.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-25` — the add's failure rule and its `|| return 1`, AC1's
  fixture and its once-only `mktemp` shim keyed on the `git` shim's 124 marker, and its arm; without
  the rule there is no return for the `fail` to stand beside.
- **consumes-from** `TOOL-aGraftedHelix-24` — the add's two triggers and its place ahead of
  `write_lease`, and AC1's first leg and unreachable leg, whose exit status this unit asserts;
  without the place there is no add ahead of `write_lease` whose failure could stop the row.
- **consumes-from** `TOOL-aGraftedHelix-20` — §4 "The order"'s claim CAS step, which S4 narrows to a
  call whose claim read answered; without that order the read's outcome is not known before the add.

## 4. Design

### Evidence

- The dispatcher runs `--resume) verb_resume "$SLUG" "$KID" ;;` and discards its return
  (`tools/unattended/unattended.sh:10561`); the script's last statement is
  `RUNLOG_CLEAN=1; exit "$status"` (`:10576`). The script sets only `set -u` (`:48`).
- `fail` (`:637`) prints `UNATTENDED check <n> FAILED — <why>` and sets `status=1`.
- `set_fact` (`:5509`) calls `fail 17` before each of its three early refusals (`:5512`, `:5516`,
  `:5525`), then returns 2 with no `fail` when `mktemp` fails (`:5528`) and returns `mv`'s status
  with no `fail`.
- `write_lease` (`:5557`) ends each `set_fact` with `|| return 1` (`:5559` to `:5569`), and its five
  callers each write `write_lease ... || return 1` with no `fail`: `:5324`, `:6356`, `:6532`, `:6599`
  and `:6658`.
- The rotation copy at `:5095` to `:5098` and the `gates-run` write at `:7662` tolerate a failed
  `set_fact`, so the `fail` belongs at the protecting callers and not inside `set_fact`.
- Unit 1 S3: `write_claim` pushes `--force-with-lease=refs/gov/runs/<slug>:<observed sha>`, with an
  empty expected sha for a create. Unit 1 S8: `--close` refuses with check 109 when the claim cannot be
  read, before any write. Unit 1 §5: a remote that does not answer is check 109 or an announcement,
  never an empty list.

### The rule

| the holder row's write that fails | what it prints | the process exit |
|---|---|---|
| the add, on either trigger | `UNATTENDED check 17 FAILED — cannot record a run fact: prior-session in <file>` | 1 |
| a fact inside `write_lease` | `UNATTENDED check 17 FAILED — cannot record the lease: <fact> in <file>` | 1 |

The record each leaves is unit 25 §4's for the add and unit 24 §4's for `write_lease`; this unit
changes what the call reports, never what it writes.

### The unreadable trigger's leg

The leg must fail the add's temporary file and no other. Between the failed claim fetch and the add
the row takes none: a read whose fetch failed yields no list to parse (unit 1 §5), and S4 pushes
nothing. So the `git` shim creates the marker when the claim fetch exits non-zero, and unit 25's
once-only `mktemp` shim fails the first temporary file after it, which is the add's. The check-17
line naming `prior-session` and the empty set are the leg's witness: a shim spent anywhere else lets
the add run and write `s1`, and a shim never spent does the same. The announce line unit 20 §4
gives the unreadable row is not asserted: no source pins its text, and the check-17 line is printed
only by the add, which runs after the claim outcome is handled.

### What units 24 and 25 stop asserting

Unit 24 AC1 and unit 25 AC1 drop their "exits non-zero" on the interrupted calls, each as a rev
bump, because each runs at an order before this unit and neither unit's build sets the exit. Their
record assertions stay, and they discriminate their own staged breaks. AC1 and AC2 here assert the
exit those criteria dropped, as exactly 1, with its line.

### Inventory

No new fact, function, check, conf key or file. Two `fail 17` messages are added, at the add and in
`write_lease`'s one guarded write. No lexicon cell and no codebase-map key is minted.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- every other carrier of the unattended version marker, which `tools/check-kit-versions.sh`
  enumerates

### Alternatives rejected

- **Remove the exit assertions and leave the exit at 0.** A failed add or lease fact is then
  invisible to every caller: exit 0, no line, no `RUNLOG_CHECKS` entry, so the tick and the session
  read a successful resume while the record still names the old session.
- **A `fail` inside `set_fact`.** §3: it fails callers that tolerate a miss on purpose.
- **A `fail` at the holder row's `write_lease` call alone.** Four other callers return on the same
  function the same way, and the lease is one function, so the `fail` goes where they all route.
- **One guarded add site per trigger.** It is one edit away from an unguarded one; a single site
  makes the per-trigger split impossible rather than merely detected.
- **Six literal guards in `write_lease`, one per fact.** Each is a `fail` branch with its own
  literal text, and §6 fails one fact, so five branches stand unarmed: the harness-arms leg reds
  them, and a pin row for code this unit writes is a waiver of its own criterion. A seventh fact is
  one edit away from an unguarded line, the add's argument above.
- **Key the unreachable leg's marker on the failed fetch and leave the push unpinned.** If the row
  attempted a CAS there, the once-only shim would spend itself on the CAS's temporary file, the add
  would write `s1`, and the leg would red on a correct build.
- **Attempt the CAS on an unreadable claim.** S4: it has no observed sha to lease against, and an
  empty one turns a fetch-only outage into check 108.
- **A line-scan gate for a `return` with no `fail`.** Over `verb_resume` at base it hits ten lines,
  most of them callees that call `fail` themselves, so the predicate needs callee knowledge: a gate
  of its own, under the method's one-mechanism rule.

## 5. Production-readiness checklist

- security — No new surface. Two refusals print a line and set the exit on failures the row already
  could not survive; S4 removes a push.
- perf / scale — None added; S4 spends no push on a call whose claim read did not answer.
- error / empty / loading states — §4 "The rule".
- observability — The check-17 line names the fact and the file, and the exit is 1, so the tick, the
  idle-wake and the session each see the failure.
- risks — A caller that read exit 0 after a failed lease write now reads 1. Every such caller already
  meets exit 1 from `set_fact`'s three earlier refusals on the same call, so none meets a new value.
- testing — §7's arms, each observed RED on its staged break first, failures staged by shims keyed
  on a marker, never by a sleep or a count.
- migration — None: no stored value changes.
- user docs — None: the stops guide describes the lease and the fact, which this unit does not change.

## 6. Acceptance criteria

The fixtures are unit 25 AC1's and unit 24 AC1's, as named per criterion: unit 23's fixture, whose
record and claim both name session `s1` and the recorded keepalive. A holder call is
`--resume <slug> --keepalive-id <recorded id>` under the session named. "Unreachable" is unit 23's,
the bare repository renamed away for that call, and "restored" renames it back. The claim is read
with `git ls-remote <bare> refs/gov/runs/<slug>` and `git cat-file -p`, and the set with the
driver's `fact` over the run-state file.

- **AC1** — When unit 25 AC1's first call runs, an `s2` holder call whose claim push exits 124 under
  that criterion's once-only `mktemp` shim, it exits 1, prints a line beginning
  `UNATTENDED check 17 FAILED — cannot record a run fact: prior-session in`, and leaves the
  run-state file reading `session: s1`, `fact` printing nothing for `prior-session`, and `lease-utc`
  at its pre-call value.
  Red when: the add's return carries no `fail`, so the call exits 0 and prints no such line.
- **AC2** — When unit 24 AC1's first call runs, an `s2` holder call whose claim push exits 124 under
  that criterion's `mktemp` shim that fails once after the record's `session:` line reads `s2`, it
  exits 1, prints a line beginning `UNATTENDED check 17 FAILED — cannot record the lease:`, and
  leaves `session: s2`, `prior-session: s1` and `lease-utc` at its pre-call value. The first call of
  unit 24 AC1's unreachable leg exits 1 and prints the same line.
  Red when: a `set_fact` that fails inside `write_lease` returns with no `fail`, so the call exits 0.
- **AC3** — Over a fresh copy of unit 25 AC1's fixture, an `s2` holder call runs with the remote
  unreachable, a `git` shim on `PATH` that forwards every call, appends each argument list to a log,
  and creates the marker when the claim fetch of `refs/gov/runs/*` exits non-zero, and unit 25's
  once-only `mktemp` shim keyed on that marker. The call exits 1, prints a line beginning
  `UNATTENDED check 17 FAILED — cannot record a run fact: prior-session in`, and leaves
  `session: s1`, `fact` printing nothing for `prior-session`, and `lease-utc` at its pre-call value,
  and the shim's log names no `push` for that call. A second `s2` call with the remote restored and
  the `mktemp` shim removed exits 0, prints no `UNATTENDED check 108 FAILED`, leaves a claim naming
  `session: s2`, leaves `fact` printing nothing for `prior-session`, and leaves
  `git diff --name-only` naming no run-state file.
  Red when: the unreadable trigger reaches an add whose failure does not stop the row, so
  `write_lease` moves the record to `s2` with no `s1` in the set and the restored call answers check
  90; or the row pushes a claim it could not read.
- **AC4** — When `bash tools/check-kit-versions.sh` runs at the pass's commit it exits 0, and
  `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` names no unattended carrier
  left behind.
  Red when: the driver's bytes moved and the unattended version did not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · unit 25's 124 leg asserting exit 1 and the check-17 line naming prior-session; stage the add's fail 17 removed with its return 1 kept, observed red by the exit · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · unit 24's first leg and unreachable leg asserting exit 1 and the check-17 lease line; stage the fail 17 removed from write_lease's one guarded write with its return 1 kept, observed red by the exit · the suite's floor rises by its new arm count

New arm: tools/unattended/unattended.test.sh · an s2 holder call with the remote unreachable whose add a mktemp shim keyed on the failed claim fetch fails, asserting exit 1, the check-17 prior-session line, session s1, an empty set and no claim push in the git shim's log, then a restored s2 call with no check 108; stage the unreadable path rerouted to a second add whose set_fact carries no guard, and separately that path routed into a CAS with an empty expected sha, each observed red through this leg · the suite's floor rises by its new arm count

The unattended suites are not on the bar (`tools/unattended/README.md`). A pass runs its criteria
directly, and the main loop runs the suite once at VERIFYING.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from findings 5, 8 and 6 (all HIGH) of the round-1
  spec audit of unit 25, grounded against the dispatcher, `fail`, `set_fact`, `write_lease` and its
  five callers at base `5266d22e`, and against units 1, 20, 23, 24 and 25 as specced. S4 pins the
  question the audit left open, whether the row attempts a CAS on an unreadable claim, from unit 1
  S3's lease.
- rev-2 · 2026-10-04 · §5 · from the bug-class checklist over the promoting commit, which selected
  `two-answers-to-one-question`. §5 perf no longer says S4 saves a push, which presumed a build that
  pushes on an unreadable claim; it says what S4 spends. Unit 23's sequence-d arm, which said
  "two unreachable pushes", is corrected in its own spec.
- rev-3 · 2026-10-05 · §1 §2 §4 §7 · S2 S3 S4 · the build pass's divergences, before the code. The
  claim refusals were renumbered before the reconciling merge at `909c5e0b`, because main's own
  driver already uses 89 to 106: check 90 reads as check 108 and check 91 as check 109 throughout.
  S2's six guarded lines become one guarded write in a loop over the same facts in the same order,
  because the harness-arms leg keys a `fail` branch by its literal text and §6 fails one fact; the
  message a caller reads is unchanged. S3 and S4 already stand in the driver at this unit's start
  (the add's single site under `cas != 0`, the CAS under `[ -n "$cw" ]`), so they move no byte and
  AC3 observes them. The `:<line>` citations in §1 to §4 are the driver at base `5266d22e`; the
  driver has moved since, and each names the same statement.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a verb's failed write must set the process exit status,
not only return from the function"` ranked symbol definitions across the Python tools only and
printed that the `.sh` layer has no symbol extractor, so its miss is no evidence. The seam was read
from source: `fail` is the one writer of `status`, and `set_fact`'s early refusals already pair
`fail 17` with their return. That shape fits, and the change reuses it at the add and in
`write_lease`. The recall probe returned unit 20, unit 25, the round-1 audit of unit 25's id 5 row,
unit 23, unit 25's own reuse audit and unit 24. `memory/gotchas/status-set-in-a-subshell.md` is the
recorded class nearest the exit half, and `memory/gotchas/observed-by-claim-no-arm-discharges.md`
the nearest to the trigger half.

Recall terms used: set_fact fail status exit return write_lease prior-session holder resume check-17 dispatcher verb

The question passed with them: "when a fact write fails inside the resume holder row, how does the
failure reach the process exit status".
