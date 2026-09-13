# Acceptance ledger — TOOL-dLoggedFlight-3

**Serves:** journal TOOL-dLoggedFlight-3

Tier-2 · node d · 2026-09-13 · the build pass of the gate runner's run-log line, against spec rev-5.
Every line is OBSERVED except AC6, which is written as owed. `<suite>` is
`tools/run-gates/run-gates.runlog.test.sh`, run directly and never through the gate runner. Its final
run printed `PASS (188 assertions)` against a floor of 188. No gate leg was run, per the owner's
instruction of 2026-09-13, and no suite that existed under `tools/unattended/` before this build ran.

## The criteria

**Evidences:** TOOL-dLoggedFlight-3

- AC1 — `bash <suite>` (`check_ac1_red`) — after a green bar, a bar with one passing and one failing
  leg under `GATE_RUN_ID=push-1-1` added one line reading `run=push-1-1`, `verdict=RED`, `ran=2`,
  `failed=1` and `fail.1=failing leg`, with no `fail.2`. The passing leg was named nowhere on it,
  `head` was the scratch HEAD and `started` was that run's own header value. RED seen four ways: the
  pinned id replaced, every leg's name taken, the verdict read from the previous run's record, and
  `failed` read from the wrong key.
- AC2 — `bash <suite>` (`check_ac2_paths`) — a green bar wrote `verdict=GREEN rc=0` with an empty
  `wall_breach`, a 30 s leg under a 3 s wall wrote `verdict=RED wall_breach=3 rc=1`, and an all-held
  bar wrote `verdict=REFUSED rc=2` with `held=1`. RED seen with `trap - EXIT` placed before each of
  the three exits, each on its own arm.
- AC3 — `bash <suite>` (`check_ac3_signals`) — TERM, INT and HUP, each sent to the runner's own pid
  once its leg reported ready, ended the bar with 143, 130 and 129 and exactly ONE line, reading
  `verdict=NONE` with that `rc`, an empty `stage` and the header's `head`. A fourth TERM, held behind
  a stubbed `$(fingerprint)` until it had been sent, still read 143, and its line read
  `stage=pre-header`. RED seen with the guard removed (two lines), with `RUNLOG_RC` dropped (the held
  TERM read 0), and with `timeout --foreground` removed from the launch (INT was ignored).
- AC4 — `bash -x` — traced through `RGRL_BEFORE=<the runner at 65369b28> RGRL_ARMS=AC4 bash <suite>`,
  a two-leg bar with the journal directory present made 19 external execs after its last leg on the
  base runner and 19 on this unit's. The recurring arm counts the same 19 against a copy whose
  `cleanup` no longer calls the writer, and a clone's first bar pays exactly one more, a `mkdir`.
  RED seen with a `date` added to the writer, and with an unconditional `mkdir -p`: 20 each.
- AC5 — `GOV_RUNLOG=0` (`check_ac5_write_failure`) — with the journal directory replaced by a file,
  a green and a red bar kept the switch-off `rc` and stdout, and stderr gained one
  `run-gates: run log` line naming `runlog/gates.log` and nothing else. `GOV_RUNLOG=0` wrote no line
  and `GOV_RUNLOG=1` wrote one. RED seen with the failed write ending in `exit 5`, with the warning
  sent to stdout, and with the switch test removed.
- AC6 — `GATE_SELFTESTS=1` — OWED to the post-build gate run, which records it: the
  `run-gates run-log line` leg at or above its floor and inside its 160 s budget row, the
  `kit version markers` leg green at 1.7, and the `govkit selfcheck` leg resolving the suite as
  `project-owned`. What this pass observed is the declarations, through `check_ac6_declarations`:
  the suite in the kit's project-owned list, a budget row, one held, guarded and bounded manifest leg,
  and the README marker at the runner's version. RED seen with each of those four undone on a mirror.
- AC7 — `bash <suite>` (`check_ac7_many_fails`) — 21 failing legs wrote `failed=21`, `fail.1=red 01`,
  `fail.20=red 20`, no `fail.21` and `fail_more=1`, on a line at or under 2048 bytes. RED seen with the
  cap raised to 21, and with the failing legs taken in glob order, where `fail.20` read `red 09`.
- AC8 — `bash <suite>` (`check_ac8_pre_header`, `check_ac8_exits`) — a malformed manifest and a file
  where the run root belongs each wrote one line reading `verdict=NONE stage=pre-header rc=2`, with
  the pinned id and the header's keys empty. The enumeration over `tools/run-gates/run-gates.sh` found
  eight exit sites below the trap, every text in its table at its count, every row live, and every
  arm the table names run with its line seen; on every run it stages an unarmed exit, a second
  `exit 2` and a comment-and-string control into copies. RED seen with `trap - EXIT` before each
  refusal, and with an unarmed `exit 7` added below the trap line of the runner itself.
- AC9 — `bash <suite>` (`check_ac9_worktree`) — a bar run from a linked worktree and one from the
  primary tree both landed in `<common-dir>/runlog/gates.log`, each naming its own tree, with nothing
  under the worktree's git dir in `.git/worktrees/`. RED seen with the `commondir` read skipped, and
  with the primary tree's own branch removed, where it wrote no line.
- AC10 — `python tools/memory-tree/gotchas.py --for-paths tools/run-gates/run-gates.sh` — selected
  `signal-trap-runs-the-exit-handler-twice`. RED seen with the record's two backticked anchors
  removed on the working tree, which it then did not select; the record was restored from a copy and
  compared byte for byte.

## The fit

The runlog grammar asks any producer that truncates to produce what `render_line` produces, and the
suite's CAP arm holds the runner to it on both steps, byte for byte. Step one: 21 failing legs with
117-character names, where whole `fail.<i>` fields dropped into the `fail_more` already there. Step
two: a run id over the filesystem's name limit, which also drives the run-directory refusal, in ASCII,
behind three-byte characters where a cut landed inside one, and behind TABs where a cut halved an
escape. RED seen with the fit off, with the character repair removed, with the escape repair removed,
and with the lowest index dropped first.

## Staged RED

30 breaks, each applied to a MIRROR of the kit's files in a scratch dir, never to the working tree,
and each run through the mirror's own copy of the suite with only its target arm selected. All 30
went RED, each on a FAIL line carrying the text its break was aimed at, and an unmodified mirror
printed `PASS (188 assertions)` before and after the batch. The mirrors were copied before one
comment-only edit to the runner. AC10's break was made on the working tree's record and restored
from a copy, never with a checkout.

Two breaks first came back NOT RED, and each changed the suite before the final batch. Dropping
`RUNLOG_RC` passed the three signal bars, because a signal that interrupts `wait -n` leaves `$?` at
128+n, so the held TERM was added. An exec placed ahead of the switch test ran on both sides of a
`GOV_RUNLOG=0` baseline, so AC4's baseline became a copy that never calls the writer. Both are in the
spec's rev-5 section 4.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `run-gates gov canary`, `run-gates wiring` and `kit version markers`;
- `testsuite counts (every bar self-test prints one)`;
- `every held leg is budgeted, every budget row resolves`;
- `govkit selfcheck`, `codebase-map coverage + freshness` and `lexicon naming predicates`;
- `install-prefix (shipped surface)`;
- `shell hygiene (a loop fed by a command substitution)`;
- `gotchas selftest` and `memory hygiene`.

## Residue

- A second gotcha class, `async-job-starts-with-sigint-ignored`, which the spec did not name. The INT
  launch this suite first planned used `set -m`, and a probe showed it drops INT once the suite is
  itself started as an `&` job, which is how the bar starts every leg. The class is claimed beside the
  first one by the run-gates dossier.
- The kit's other suites, the canary among them, pin `cleanup`'s single-line shape and its order of
  work. The line keeps both, but those suites run only after the build.
- `tools/govkit/subject-pins.tsv` was extended by hand with the one row the generator writes for the
  new leg, in its sorted place, rather than by running `govkit selfcheck --write`, since that verb
  runs the selfcheck gate as it writes.
