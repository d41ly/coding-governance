# TOOL-dLoggedFlight-3 — the gate runner writes one verdict line per bar run

**Status:** CLOSED · rev-6 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-build-TOOL-dLoggedFlight-3-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-dLoggedFlight-3-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md](../reviews/2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-16-review-TOOL-dLoggedFlight-1-closing-diff-review-round2.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-1-closing-diff-review-round2.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

A bar's verdict survives today only in the last five run records of one worktree's git dir, and the
ledger keeps one row per leg. So a run that ran the bar seventeen times keeps no structured history of
which bars were red. Make every bar append exactly one line to `gates.log` under the journal root, from
the one seam every exit path after startup passes through, with no added process spawn.

## 2. Scope (IN)

- **S1** `tools/run-gates/run-gates.sh`'s exit handler, `cleanup`, appends one `ev=once` line to
  `gates.log` in the grammar of `TOOL-dLoggedFlight-1`, before its existing work. A guard flag makes
  the append happen once per process, because a signal runs `cleanup` twice (§4). Observed by AC1 and
  AC3.
- **S2** The line carries the run id as `run=`, the worktree, `head` and `started` read back from the
  run's own header, `full`, `selftests`, and the verdict with `ran`, `failed`, `skipped`, `held` and
  `reused` read back from the run's own verdict file. It also carries `rc`, and up to 20 failing leg
  names as `fail.<i>=` keys taken from the `.leg` rows with `st=fail`, with `fail_more=<n>` beyond 20.
  Observed by AC1 and AC7.
- **S3** Every exit after the EXIT trap is installed at `:1041` writes a line. That covers GREEN, RED,
  the wall breach, the all-held REFUSED path, the two startup refusals after the trap, and a run
  killed by INT, TERM or HUP. A killed run has no verdict file, so it writes `verdict=NONE` with `rc`
  130, 143 or 129. A startup refusal writes `verdict=NONE` with `stage=pre-header` and `rc=2`.
  Observed by AC2, AC3 and AC8.
- **S4** The common dir is resolved from the runner's existing `GD` with builtin reads only:
  `<GD>/<commondir contents>` when that file exists, else `GD` itself, which is the primary tree's
  case. The append is a builtin `printf >>`. The verdict path runs exactly as many external processes
  as before, apart from the first-ever `mkdir` of the journal directory. Observed by AC4 and AC9.
- **S5** A failed write never changes the runner's exit code or its stdout; it prints one stderr line.
  `GOV_RUNLOG=0` turns the line off. Observed by AC5.
- **S6** A new small suite, `tools/run-gates/run-gates.runlog.test.sh`, with its held leg and budget
  row. It is added to `tools/run-gates/kit.toml`'s `project-owned` list and its leg is carried by an
  `[[exempt_leg]]` registry row, per TOOL-aQuenchedHarness-3. That row raises the
  `tools/govkit/registry.toml` row of `tools/install-prefix-carried.txt` by hand, with its reason, per
  TOOL-dRetiredFork-17. The kit version moves from 1.6 to 1.7 across its carriers, and the README's
  run-record section names the line. Observed by AC6.
- **S7** A gotcha record under `memory/gotchas/` for the shape a signal trap takes when it calls the
  exit handler and then exits: the handler runs twice. It is anchored on `tools/run-gates/run-gates.sh`
  and claimed by a dossier. Observed by AC10.

## 3. Non-goals (OUT)

- No change to the run record, the ledger, the retention of five runs, or any verdict.
- No session field. The gate runner is its own kit and reads no unattended declaration. The run model
  joins a gate line to a run by run id where a push line it joined pinned one, and otherwise by the
  run's worktree and time. The landing bar runs in the primary tree, and its line joins through the
  landing push's pinned id (`TOOL-dLoggedFlight-8` S3).
- Exits before the EXIT trap is installed write no line: not a repo, no python, a bad profile, the
  profile print, the turnstile queue and beacon traps, and the work-dir `mktemp`. §4 lists them.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-1` — the line grammar and the journal location contract.
- **hands-off** `TOOL-dLoggedFlight-8` — the run model joins these lines to a run's window.

## 4. Design

At base the traps are `trap cleanup EXIT` at `:1041`, then `trap 'cleanup; exit 130' INT`,
`trap 'cleanup; exit 143' TERM` and `trap 'cleanup; exit 129' HUP` at `:1042-1044`. A signal runs
`cleanup` from its own trap, and the `exit` then fires the EXIT trap, which runs `cleanup` again. The
round-1 audit reproduced both entries on node `d`. So the signal traps become
`trap 'RUNLOG_RC=143; cleanup; exit 143' TERM` and their INT and HUP siblings. The writer takes `rc`
from `RUNLOG_RC` when it is set, else `$?`, and sets a guard so its second entry appends nothing. The
existing work in `cleanup` is unchanged.

The writer reads `$RUNDIR/header` and `$RUNDIR/verdict` with a `while read` loop and takes the keys it
needs. It globs `$RUNDIR/*.leg` and reads each row's name and state with builtin `read`. No `cat`,
`awk` or `git` is added.

The failing legs are ordered by manifest index, the number each `.leg` file is named by, so `fail.1`
is the first failing leg in the manifest and not the first in glob order, where `10.leg` sorts before
`2.leg`. `stage` is `pre-header` when the record holds no header and empty otherwise, so a killed
run's `verdict=NONE` with an empty stage says it died after its header was written. `wall_breach` is
the verdict file's own key and is empty on every other path. `selftests` is `1` or empty, the
full-green stamp's spelling. Every read is defaulted, because `set -u` holds inside a trap, and a handler that aborts on
an unset name writes nothing for exactly the run it exists to record. A line over the cap is fitted by
the runlog kit's reference rule, both steps. Whole `fail.<i>` fields drop highest first into
`fail_more`, and only then is the longest other value cut. The run id is the value that reaches the
second step, because `GATE_RUN_ID` is the caller's and has no bound.

The exits before `:1041` are `:35`, `:36`, `:75`, `:186`, `:518`, `:804-806`, `:867-869` and `:979`.
They leave no line, because each refuses before a bar exists or runs `--print-profile`. The exits after
it and before the header is written are `:1093`, the run-dir `mkdir`, and `:1182`, the manifest
parse. Each writes `verdict=NONE stage=pre-header rc=2` with the header keys empty. The suite enumerates
every `exit` after `:1041` and fails if one has no arm or no named exemption. It keys a site on its line
text AND the number of sites carrying that text, so a third `exit 1` is a count that moved rather than
a match. The two named exemptions are the `exit 0`s at `:1601-1602`, inside the wall watcher's
`( … ) &` subshell, which exit that subshell and run no trap of the runner's.

Two arms need a harness detail the criteria do not state. AC3 launches each bar through
`timeout --foreground`, because an `&` job of a non-interactive shell starts with SIGINT ignored and
bash cannot trap a signal that was ignored at entry. `set -m` helps only while the suite itself did not
start with INT ignored, and a leg of the bar always does. The signal goes to the runner's own pid, the
tail of its default run id, and never to `timeout`. A signal that interrupts `wait -n` leaves `$?` at
128+n when the trap starts, so those three bars read the right status even without `RUNLOG_RC`. A
fourth TERM therefore lands while the runner waits on its first `$(fingerprint)`, held open by a stub,
where the trap runs only after the command ends and `$?` is the command's 0. That is the case the
explicit status decides, and its line also shows a run killed before its header.

AC4 counts from the first depth-one `remove_wall_watcher` trace line, which follows the last leg's
`wait`, to the end of the trace, with the wall and the turnstile off so no background subshell traces
into that window. Its recurring arm compares a copy of the same runner whose `cleanup` no longer calls
the writer, which is the base teardown byte for byte. `GOV_RUNLOG=0` would not do: the writer runs its
guard before it reads the switch, so an exec placed there would be counted on both sides.
`RGRL_BEFORE=<runner>` traces a named runner in that arm's place, and that is how the landing
observation compares against the base.

### Data model

`v t p=gates ev=once run wt head started full selftests verdict stage ran failed skipped held reused
wall_breach rc fail.1..fail.20 fail_more kit`.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `write_runlog_verdict`, `read_record_keys` | shell functions | `sh.function`, verb-led |
| `RUNLOG_RC`, `GOV_RUNLOG` | a signal's status, the environment's switch | runner variables |
| `RGRL_BEFORE` | the runner AC4 traces as its baseline | suite environment seam |
| `RGRL_ARMS` | the arms a selected run grades, never against the floor | suite environment seam |
| `run-gates run-log line` | leg, `kit` / `selftests` | manifest |

### Files touched (estimate)

`tools/run-gates/{run-gates.sh,README.md,kit.toml,run-gates.runlog.test.sh}` with its version carriers,
`tools/gate-legs.json`, `tools/govkit/{registry.toml,subject-pins.tsv}`,
`tools/run-gates/selftest-budgets.txt`, `tools/install-prefix-carried.txt`, one `memory/gotchas/` record
with its index and dossier claim,
`memory/map/features/run-gates.md` and the regenerated map.

### Alternatives rejected

- A writer at each of the three verdict sites: rejected because it misses the killed run, which has no
  verdict site, and repeats itself three times.
- Reducing the signal traps to a bare `exit N`: rejected, because it changes when `cleanup`'s existing
  work runs relative to the signal, which this unit does not own.
- Arms in `tools/run-gates/run-gates.evidence.test.sh`: rejected by cost. Its worst reading is 1500 s
  and its budget row is 2250 s. A focused suite observes the same line in seconds.

## 5. Production-readiness checklist

- security — no free text. Leg names come from the manifest, and the worktree path is the local root
  on a machine-local file that is never pushed.
- perf / scale — zero added spawns (AC4). Reading at most one `.leg` row per executed leg is builtin
  I/O, under 1 ms per row.
- error / empty / loading states — an absent header or verdict writes the line with those keys
  empty, and `verdict=NONE` when there is no verdict file.
- observability — the killed-bar signature is `verdict=NONE` with a signal `rc`, once.
- risks — the gov canary pins the runner's knobs. `GOV_RUNLOG` is read by name, and the build checks
  that the canary's knob scan does not red on it.
- testing — the new suite stages each AC RED before landing.
- migration — none.
- user docs — the README run-record section.

## 6. Acceptance criteria

`<suite>` below is `tools/run-gates/run-gates.runlog.test.sh`, which this unit creates. It copies the
runner into a scratch repo with a small manifest, the way `tools/run-gates/run-gates.evidence.test.sh`
builds `rec_repo`.

- **AC1** — When `bash <suite>` runs a bar with one passing and one failing leg under
  `GATE_RUN_ID=push-1-1`, `gates.log` gains one line with `run=push-1-1`, `verdict=RED`, `ran=2`,
  `failed=1`, the failing leg's name in `fail.1`, and `head` equal to the scratch repo's HEAD.
  Red when: the writer reads a stale key, names the passing leg, or ignores the pinned id.
- **AC2** — When `bash <suite>` runs a green bar, a wall-breached bar and an all-held bar, their lines
  read `verdict=GREEN rc=0`, `verdict=RED wall_breach=<n> rc=1` and `verdict=REFUSED rc=2`.
  Red when: any path skips the trap.
- **AC3** — When `bash <suite>` sends TERM, INT and HUP to three running bars in turn, each bar writes
  exactly ONE line, reading `verdict=NONE` with `rc` 143, 130 and 129.
  Red when: the guard is removed and a killed bar writes two lines, or the explicit status is dropped.
- **AC4** — When `bash -x` traces a two-leg bar before and after the unit, with the journal
  directory present, the count of external execs after the last leg is identical.
  Red when: the writer adds a `cat`, `awk`, `date` or `git` call.
  figure: DERIVED at observation time.
- **AC5** — When the journal directory is a file, the runner's exit code and stdout are unchanged and
  stderr carries one `run-gates: run log` line. With `GOV_RUNLOG=0` no line is written.
  Red when: a failed write changes `rc`, or the switch is ignored.
- **AC6** — When `GATE_SELFTESTS=1` runs the `run-gates run-log line` leg, it passes at or above
  `FLOOR_ASSERTIONS` and inside its budget, and `bash tools/check-kit-versions.sh` is green at 1.7.
  `python tools/govkit/govkit.py selfcheck` resolves the suite as `project-owned`.
  Red when: the suite is unbudgeted, uncounted, ships to adopters, or the version carriers disagree.
- **AC7** — When `bash <suite>` runs a bar with 21 failing legs, its line carries `fail.20` and no
  `fail.21`, with `fail_more=1`, and stays at or under 2048 bytes.
  Red when: the cap is not applied, or the line overflows.
- **AC8** — When `bash <suite>` runs a bar over a malformed manifest, it writes one line with
  `verdict=NONE stage=pre-header rc=2`. The suite enumerates every `exit` after the EXIT trap line in
  `tools/run-gates/run-gates.sh` and fails on one with no arm and no named exemption.
  Red when: a post-trap exit writes nothing, or a new exit site appears without an arm.
- **AC9** — When `bash <suite>` runs a bar from a linked worktree of its scratch repo and from the
  scratch repo's primary tree, both lines land in `<common-dir>/runlog/gates.log`.
  Red when: the linked worktree writes under `.git/worktrees/`, or the primary tree finds no journal.
- **AC10** — When `python tools/memory-tree/gotchas.py --for-paths tools/run-gates/run-gates.sh`
  runs, it selects the new double-handler class.
  Red when: the record is unregistered or unanchored.

## 7. Gates

`run-gates gov canary` · `run-gates wiring` · `kit version markers` · `testsuite counts (every bar self-test prints one)` · `every held leg is budgeted, every budget row resolves` · `govkit selfcheck` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `gotchas selftest` · `memory hygiene`

New arm: `tools/run-gates/run-gates.runlog.test.sh` · each AC staged RED by removing the property it observes · floor set at landing

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S1 S2 S3 S4 S7 · §3 · §4 · AC1 AC3 AC7 AC8 AC9 AC10 · folded round-1 spec audit
  H1 (a signal runs `cleanup` twice; a guard and an explicit status make the line single, and AC3
  counts lines for all three signals), M1 (`:1093` and `:1182` come after the trap and write a
  pre-header line), M2 (the pinned run id and the 21-leg cap are observed), H2 (the primary tree has no
  `commondir` file; the git dir itself is the common dir) and H3 (a linked-worktree arm).
- rev-3 · 2026-09-13 · S6 · AC6 · folded round-2 spec audit M1 (the suite is withheld from adopters, per
  TOOL-aQuenchedHarness-3, and AC6 observes it).
- rev-4 · 2026-09-13 · S6 · §3 · §4 · folded round-3 spec audit H3 (a gate line joins through the push
  line that pinned it, so the landing bar joins from the primary tree) and M10 (the carried-prefix row is
  raised by hand).
- rev-5 · 2026-09-13 · §4 · Inventory · written by the build pass before its code. Section 4 now states
  the failing-leg order, the `stage` rule, the keys left empty, the two-step fit, the text-and-count key
  of the exit enumeration with its two subshell exemptions, INT delivered through `timeout`, and AC4's
  trace window and baseline seam. The inventory gains the two variables and the seam.
- rev-6 · 2026-09-13 · §4 Inventory · the fold of the bug-class checklist over the build commit. The
  rev-5 line above names less than rev-5's section 4 says: that section also carries the TERM held
  behind a command substitution and AC4's baseline as a copy that never calls the writer, both added
  when their first staged breaks came back green. The build also recorded a second gotcha class,
  `async-job-starts-with-sigint-ignored`, beside the one S7 names. The inventory gains `RGRL_ARMS`,
  which rev-5 left out.

## 10. Reuse audit

The seam is the runner's own EXIT trap, `cleanup`, at `tools/run-gates/run-gates.sh:1040-1041`, found
by reading the exit-path table the acquisition probe built. `tools/codebase-map/reuse_lookup.py`
cannot see it because the `.sh` layer is unscanned. The keys are read back from the run record the
runner already writes at `:1288-1333` and `:1823-1838`, so nothing is recomputed.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
