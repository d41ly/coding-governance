# TOOL-dLoggedFlight-3 — the gate runner writes one verdict line per bar run

**Status:** SPECCED · rev-1 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

A bar's verdict survives today only in the last five run records of one worktree's git dir, and the
ledger keeps one row per leg. So a run that ran the bar seventeen times keeps no structured history of
which bars were red. Make every bar append one line to `gates.log` under the journal root, from the
one seam every exit path after startup passes through, with no added process spawn.

## 2. Scope (IN)

- **S1** `tools/run-gates/run-gates.sh`'s EXIT trap, `cleanup` (installed at `:1041`), appends one
  `ev=once` line to `gates.log` in the grammar of `TOOL-dLoggedFlight-1`, before its existing work.
  Observed by AC1.
- **S2** The line carries the run id, worktree, `head` and `started` read back from the run's own
  header, `full`, `selftests`, and the verdict with `ran`, `failed`, `skipped`, `held` and `reused`
  read back from the run's own verdict file. It also carries `rc`, and up to 20 failing leg names as
  `fail.<i>=` keys taken from the `.leg` rows with `st=fail`, with `fail_more=<n>` beyond 20.
  Observed by AC1 and AC2.
- **S3** Every exit after the trap is installed writes a line: GREEN, RED, the wall breach, the
  all-held REFUSED path, and a run killed by INT, TERM or HUP. A killed run has no verdict file, so it
  writes `verdict=NONE` with `rc` 130, 143 or 129. Observed by AC2 and AC3.
- **S4** The common dir is resolved from the runner's existing `GD` with builtin reads only, and the
  append is a builtin `printf >>`. The verdict path runs exactly as many external processes as before,
  apart from the first-ever `mkdir` of the journal directory. Observed by AC4.
- **S5** A failed write never changes the runner's exit code or its stdout; it prints one stderr line.
  `GOV_RUNLOG=0` turns the line off. Observed by AC5.
- **S6** A new small suite, `tools/run-gates/run-gates.runlog.test.sh`, with its held leg and budget
  row. The kit version moves from 1.6 to 1.7 across its carriers, and the README's run-record section
  names the line. Observed by AC6.

## 3. Non-goals (OUT)

- No change to the run record, the ledger, the retention of five runs, or any verdict.
- No session field. The gate runner is its own kit and reads no unattended declaration. The run model
  joins a gate line to a run by worktree and time, and by run id where the pre-push hook of
  `TOOL-dLoggedFlight-4` pinned one.
- Exits before the trap is installed write no line: not a repo, no python, a bad profile, or a failed
  `mkdir` of the run dir. §4 lists them and the reason.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-1` — the line grammar and the journal location contract.
- **hands-off** `TOOL-dLoggedFlight-8` — the run model joins these lines to a run's window.

## 4. Design

`cleanup` runs on every exit after `:1041`. The signal traps at `:1042-1044` exit with 130, 143 and
129, so `$?` on entry to `cleanup` is the real status on those paths. The writer reads `$RUNDIR/header`
and `$RUNDIR/verdict` with a `while read` loop and takes the keys it needs. It globs
`$RUNDIR/*.leg` and reads each row's name and state with builtin `read`. No `cat`, `awk` or `git` is
added.

The exits before `:1041` are `:35`, `:36`, `:75`, `:186`, `:518`, `:804-806`, `:867-869`, `:979` and
`:1093`. They leave no line. Every one of them either refuses before a bar exists or runs
`--print-profile`, so no verdict exists to record. That is the same reason they leave no run record
today.

### Data model

`v t p=gates ev=once run wt head started full selftests verdict ran failed skipped held reused
wall_breach rc fail.1..fail.20 fail_more kit`.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `write_runlog_verdict`, `read_record_keys` | shell functions | `sh.function`, verb-led |
| `run-gates run-log line` | leg, `kit` / `selftests` | manifest |

### Files touched (estimate)

`tools/run-gates/{run-gates.sh,README.md,kit.toml,run-gates.runlog.test.sh}` with its version carriers,
`tools/gate-legs.json`, `tools/govkit/{registry.toml,subject-pins.tsv}`,
`tools/run-gates/selftest-budgets.txt`, `memory/map/features/run-gates.md` and the regenerated map.

### Alternatives rejected

- A writer at each of the three verdict sites: rejected because it misses the killed run, which has no
  verdict site, and repeats itself three times.
- Arms in `tools/run-gates/run-gates.evidence.test.sh`: rejected by cost. Its worst reading is 1500 s
  and its budget row is 2250 s. A focused suite observes the same line in seconds.

## 5. Production-readiness checklist

- security — no free text. Leg names come from the manifest, and the worktree path is the local root
  on a machine-local file that is never pushed.
- perf / scale — zero added spawns (AC4). Reading at most one `.leg` row per executed leg is builtin
  I/O, under 1 ms per row.
- error / empty / loading states — an absent header or verdict writes the line with those keys
  empty, and `verdict=NONE` when there is no verdict file.
- observability — the killed-bar signature is `verdict=NONE` with a signal `rc`.
- risks — the gov canary pins the runner's knobs. `GOV_RUNLOG` is read by name, and the build checks
  that the canary's knob scan does not red on it.
- testing — the new suite stages each AC RED before landing.
- migration — none.
- user docs — the README run-record section.

## 6. Acceptance criteria

`<suite>` below is `tools/run-gates/run-gates.runlog.test.sh`, which this unit creates. It copies the
runner into a scratch repo with a two-leg manifest, the way `tools/run-gates/run-gates.evidence.test.sh`
builds `rec_repo`.

- **AC1** — When `bash <suite>` runs a bar with one passing and one failing leg, `gates.log` gains one
  line with `verdict=RED`, `ran=2`, `failed=1`, the failing leg's name in `fail.1`, and `head` equal to
  the scratch repo's HEAD.
  Red when: the writer reads a stale key, or names the passing leg.
- **AC2** — When `bash <suite>` runs a green bar, a wall-breached bar and an all-held bar, their lines
  read `verdict=GREEN rc=0`, `verdict=RED wall_breach=<n> rc=1` and `verdict=REFUSED rc=2`.
  Red when: any path skips the trap.
- **AC3** — When `bash <suite>` sends TERM to a running bar, its line reads `verdict=NONE rc=143`.
  Red when: the line is missing or reads `rc=0`.
- **AC4** — When `bash -x` traces a two-leg bar before and after the unit, with the journal
  directory present, the count of external execs after the last leg is identical.
  Red when: the writer adds a `cat`, `awk`, `date` or `git` call.
  figure: DERIVED at observation time.
- **AC5** — When the journal directory is a file, the runner's exit code and stdout are unchanged and
  stderr carries one `run-gates: run log` line. With `GOV_RUNLOG=0` no line is written.
  Red when: a failed write changes `rc`, or the switch is ignored.
- **AC6** — When `GATE_SELFTESTS=1` runs the `run-gates run-log line` leg, it passes at or above
  `FLOOR_ASSERTIONS` and inside its budget, and `bash tools/check-kit-versions.sh` is green at 1.7.
  Red when: the suite is unbudgeted, uncounted, or the version carriers disagree.

## 7. Gates

`run-gates gov canary` · `run-gates wiring` · `kit version markers` · `testsuite counts (every bar self-test prints one)` · `every held leg is budgeted, every budget row resolves` · `govkit selfcheck` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene`

New arm: `tools/run-gates/run-gates.runlog.test.sh` · each AC staged RED by removing the property it observes · floor set at landing

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

The seam is the runner's own EXIT trap, `cleanup`, at `tools/run-gates/run-gates.sh:1040-1041`, found
by reading the exit-path table the acquisition probe built. `tools/codebase-map/reuse_lookup.py`
cannot see it because the `.sh` layer is unscanned. The keys are read back from the run record the
runner already writes at `:1288-1333` and `:1823-1838`, so nothing is recomputed.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
