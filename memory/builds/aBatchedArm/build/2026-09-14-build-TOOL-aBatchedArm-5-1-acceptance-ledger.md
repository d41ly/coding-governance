# TOOL-aBatchedArm-5 — acceptance ledger

**Serves:** journal TOOL-aBatchedArm-5

Two commits under two owner rulings — 2026-09-13 (build agents run no self-test per step) and
2026-09-14 (no gate until every unit of the build is built). This unit ran NO suite, NO fixture,
NO self-test leg, NO bar and NO `run-unattended-gates.sh` in any mode. What it ran, because each
executes no suite and costs seconds: `bash -n` over both `.sh` files; `run-selftests.sh --help`,
`--list --kit tools/unattended` and `--check` on the real tree; a `bash -c` snippet that sourced the
runner's two registry functions and resolved this box's tag against the real charter (`a`, and
`nobody` refused); `bash tools/check-install-prefix.sh` and `bash tools/check-line-length.sh`; the
record gates the pre-commit hook runs. Every criterion below is therefore AMENDED, naming the
command the build's final gate pass observes it by. Every new arm in `run-selftests.test.sh` states
its red case in its comment and carries `NOT YET OBSERVED RED — owner ruling 2026-09-14`.

## What the final pass runs, once

- The kit-work DoD, `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, whose
  `run-selftests self-test` leg runs `bash tools/run-gates/run-selftests.test.sh` — the one leg
  that executes the fixture arms behind AC1, AC2, AC6 through AC11 and the fixture halves of AC3
  and AC4. That leg was already killed at its 300 s ceiling before this unit (ledger `300.333
  fail`, exit 124); the final pass pastes its new ledger row and re-declares the ceiling in
  `tools/gate-legs.json` and the budget row in `selftest-budgets.txt` from the observed wall.
- Then, on the MERGED tree, S5's landing order: (1) `bash tools/run-gates/run-selftests.sh --kit
  tools/unattended --pooled --calibrate`; (2) commit `tools/run-gates/selftest-pooled-evidence.txt`;
  (3) `bash tools/unattended/run-unattended-gates.sh --pooled` printing parity GREEN; (4) only
  then the flip commit, which is the BUILD's and not this unit's.

## The arm population, derived at build time

`grep -c '^arm ' tools/run-gates/run-selftests.test.sh`: 55 at BASE, 99 after — one retired (the
factor-absent refusal, `declares no sweep-ceiling-factor`), 45 added under the divider `the
evidence bound, TOOL-aBatchedArm-5 S1`. `SELFTEST_FLOOR` moved 55 to 99.

The parity-reached arms, every `--pooled`/`--sweep` arm the file carried at BASE, by
`grep -n -- '--pooled\|--sweep' tools/run-gates/run-selftests.test.sh` over the BASE file:
- RE-CUT to the parity wording: `a RED pooled run points at the --serial re-run` — now wants
  `one calibrate away: bash tools/run-gates/run-selftests.sh --pooled --calibrate`.
- RE-LABELLED as MISMATCH reds against a (0, 0, -) seed, want-strings kept by the beneath-row
  grep: `--sweep reds on a failing suite` (`FAIL something`) and `each pooled suite gets its own
  TMPDIR` (`FAIL scratch-under-tmpdir`).
- RE-CUT to the evidence shape, want-strings unchanged because the seeds are sized to reproduce the
  factor's numbers: the TIMEOUT arm (budget 1, seed 1: bound 2 s against a 3 s sleep), the
  `suite-mid` pair arm (budget 4, seed 1: bound 8 s against a 5 s sleep), the `SELFTEST_WALL=10`
  WALL arm (budget 5, seed 1 under `pooled@1x2`: bound 10 s), the UNRUN arm (its appended rows
  `three` and `four` seeded under `pooled@1x2` in its setup), the `SELFTEST_WALL=5` below-largest
  arm (largest evidence bound 120 s), and `run wall 140s` ((10 + 10) + (60 + 60) over one slot).
- RETIRED: `a declaration with no sweep-ceiling-factor REFUSES`.
- UNCHANGED, because S4 keeps both emissions: the arms wanting `NO cost verdict was issued`,
  `cost withheld`, `cost verdict(s) WITHHELD under pooled@`, `for a cost verdict, run the serial
  mode`, `(outer `, `peak concurrency`, `tree fingerprint MATCHED`, `THE SWEEP IS UNSOUND`,
  `Re-run the SERIAL mode, which can`, `a sweep would be UNGRADED`, `found none of`, `Use --serial,
  which reports each suite`, `so this run graded NOTHING at all`, `which is not a positive`, `which
  is not a number of seconds`, `peak concurrency 1 of outer 1`, and the three `--rank` arms whose
  `roundtrip.sh` sweep runs green over the seeds.

## The two S5 predicates, run at build time

Both were run over the tree BEFORE the first edit (at `e82d4053`, whose `tools/` is byte-identical
to BASE `1c736fd9`) and again after the S5 commit. The carrier predicate,
`git grep -nE -- '--selftests --serial|run-unattended-gates\.sh --serial|run-unattended-gates\.sh --all --serial' -- .githooks/gate-env.sh AGENTS.md memory/guides/SESSION-KICKOFF.md tools/unattended/`,
yielded eight lines before, the spec's eight — DoD carriers `.githooks/gate-env.sh:27`,
`tools/unattended/kit.toml:125`, `:126`, `tools/unattended/run-unattended-gates.sh:27`; pointers
`AGENTS.md:519`, `memory/guides/SESSION-KICKOFF.md:169`, `tools/unattended/README.md:66`,
`run-unattended-gates.sh:233` — and after the S5 commit the same eight, the four carriers each now
ending in `--pooled after calibration` beside their `--serial`, and the four pointers byte-identical
to BASE (`git diff 1c736fd9 -- AGENTS.md tools/unattended/README.md` empty; the
`SESSION-KICKOFF.md` diff is the `last-audit` line and nothing else; the kit runner's `:233` line is
byte-identical and now sits at `:238`, because five usage lines this unit added above it name the
parity verdict, the landing order and the serial cost pass — §5 user docs). The phrase predicate,
`git grep -nE 'GREEN verdict|not done until|DoD path|DoD command|landed dark' -- .githooks/gate-env.sh tools/unattended/ tools/run-gates/run-selftests.sh`,
yielded SIX lines before, not rev-6's "eight" (rev-7 corrects the word; the enumeration was
right): `.githooks/gate-env.sh:26`, `tools/run-gates/run-selftests.sh:15`, `tools/unattended/kit.toml:123`,
`:130`, `tools/unattended/run-unattended-gates.sh:27` and `:187` — and the same six after, `:27`
carrying the dark spelling and `:187` byte-identical at `:192`. The dark spelling deliberately
contains none of the phrase predicate's words, so the flip's yield is still those six lines.

The manifest re-stamp rode in the S1–S4 commit `50d95523`, not the S5 one the brief paired it
with: `run-selftests.sh` is on the manifest's `watch:` line and `manifest-check.sh --staged` grades
the commit that stages the watched change, as unit 3's checkpoint `cbf8ebce` shows; the S5 commit
touches no watched file.

## Fixture changes (`build_repo`)

The charter stub `AGENTS.md` with one registry row mapping `${USERNAME:-$USER}` to tag `t`; the
margin `tools/run-gates/ceiling-margin.txt` at floor 1 s, fraction 1.0 (so a bound is 2x the larger
of budget and reading, and a budget-60 row seeds to 120 s); the seeded, `git add`ed evidence file
under both tokens `pooled@2x1` and `pooled@1x2` for `held one` and `free one` at (1 s, rc 0, 0 FAIL,
-); `tools/seed.sh` as the per-arm upsert; `suite-ok.sh`, `suite-slow.sh`, `suite-mid.sh` and
`suite-mark.sh` print `PASS (1 assertions)` so a completion is a reading; new `suite-shard.sh`
(three FAIL lines, `81 assertions executed`, exit 1), `suite-crash.sh` (`set -u` unbound, exit 1
at once, no FAIL line, no trailer) and `suite-quiet.sh` (exit 0, prints nothing); the
`sweep-ceiling-factor` header line removed.

**Evidences:** TOOL-aBatchedArm-5
- AC1 — amended rev-7 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/run-gates/run-selftests.test.sh`, whose fixture arms are `a pooled row is
  bounded from its serial BUDGET when the seeded reading is far below it` (wants `bounded at 120s:
  budget won (budget 60s; reading 1s over 1 reading(s) under pooled@2x1 on node t, 2026-09-14)`),
  `... bounded from its READING when the seeded reading exceeds its budget` (seed 200 s: `bounded
  at 400s: reading won`), `the run wall is ceil(sum of evidence bounds / outer) floored at the
  largest evidence bound` (`run wall 400s`), `a run wall below the largest EVIDENCE bound refuses`
  (`SELFTEST_WALL=300`, rc 2), and `a pooled run with the margin file absent REFUSES naming it`
  (rc 2, `no margin declared at`). Red when the bound is budget x anything: the first arm reads
  the TERM (`budget won`) because 60 x 2 is also 120.
- AC2 — amended rev-7 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/run-gates/run-selftests.test.sh`, arms `a row with NO reading under this
  token and node REFUSES the pooled run by name, naming --calibrate, and executes no suite` (rc 2,
  `NO pooled reading under pooled@2x1 on node t`, the marker suite on the row that HAS a reading
  and no `ran.marker` after), `a row evidenced only under a FOREIGN node tag refuses the same way`
  (every node column `t` rewritten to `z`), and `with the charter's registry row deleted, a pooled
  run refuses naming the user, never a hostname` (rc 2, `no registry row matches user`). The
  refusal names `--calibrate` by the runner's own path.
- AC3 — amended rev-7 — the fixture half NOT OBSERVED under the 2026-09-14 ruling; owed at the
  build's final gate pass by `bash tools/run-gates/run-selftests.test.sh`, arms `--pooled
  --calibrate runs every selected row under the serial-sum wall and grades nothing` (the subject
  exits 99 on any `OVER BUDGET`, `TIMEOUT` or `sweep GREEN|RED` line; wants `calibrated 2 row(s),
  0 red, graded none`), `the calibrate wall is the serial SUM of the selected budgets` (`run wall
  120s = the serial sum`), `SELFTEST_WALL above the serial sum tightens nothing`, `a calibrate over
  a clean fixture reports the fingerprint MATCHED and has still changed the evidence file` (wants
  `tree fingerprint MATCHED before and after`, exits 99 if `git diff --quiet` finds the file
  unchanged), `a calibrate prints each reading it wrote with its token, tag, rc and FAIL count`,
  `a second calibrate with a LOWER reading and a different rc updates rc, fails and executed and
  NOT seconds` (seed 50 s re-read by `suite-shard.sh`: the row reads `50 1 3 81 2`), `a calibrate
  with a HIGHER reading raises that row's seconds` (`raised from 1s`), and `a row the calibrate
  wall kills writes NO reading, is named, and the calibrate exits RED counting it walled`
  (`SELFTEST_WALL=3` over `suite-long.sh`, its seed removed first; wants `calibrated 1 row(s), 0
  red, 1 walled, 0 untrailed, graded none`, exits 99 if a `free one` row appears). The real-row
  half is owed at the build's landing, step (1) of S5: `bash tools/run-gates/run-selftests.sh --kit
  tools/unattended --pooled --calibrate` over the fourteen rows `--list` resolves, under the
  serial-sum wall of 20530 s; on a red, the walled rows are named in the landing record and the
  build lands without the flip.
- AC4 — amended rev-7 — the fixture half NOT OBSERVED under the 2026-09-14 ruling; owed at the
  build's final gate pass by `bash tools/run-gates/run-selftests.test.sh`, arm `--rank still exits
  0 after a calibrate, because pooled readings never enter the budget file`. The real-tree half
  OBSERVED now, since it is a grep and a diff and runs nothing: `grep -c pooled@
  tools/run-gates/selftest-budgets.txt` is 0 before and after the unit (the retired header carried
  no such token either), and `--rank`'s unbacked list is untouched because this unit wrote no
  fourth-column reading — the budget file's only edit is the deleted `sweep-ceiling-factor` block.
- AC5 — amended rev-7 — the read-as-text half OBSERVED now, since it is a grep and runs nothing:
  after the S5 commit the carrier predicate returns the four DoD carriers each spelling
  `--pooled after calibration` beside `--serial` — `.githooks/gate-env.sh:27`,
  `tools/unattended/kit.toml:125`, `:126`, `tools/unattended/run-unattended-gates.sh:27` — and
  the four pointers byte-identical to BASE, pasted above. The landing half is owed at the build's
  landing on the merged tree, in S5's order: `bash tools/unattended/run-unattended-gates.sh
  --pooled` over the population `--kit tools/unattended --list` resolves must print GREEN with
  `killed 0 · walled 0 · unrun 0 · unstarted 0 · mismatched 0` and `fingerprint MATCHED`, pasted;
  only then the flip commit, with both predicate hit lists and the post-commit phrase re-run's
  empty result pasted; on a red at step (3) the carriers stay as they are here and the build lands
  without the flip.
- AC6 — amended rev-7 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/run-gates/run-selftests.test.sh`: every pre-existing `--serial` arm is
  byte-unchanged in the file and touches no line this unit edited (the serial loop is untouched;
  `git diff BASE -- tools/run-gates/run-selftests.sh` shows no hunk below the sweep block's
  `exit "$st"`), and every pre-existing `--pooled`/`--sweep` arm not enumerated above is
  byte-unchanged. Red when any of them moves at the final pass.
- AC7 — amended rev-7 — the read-as-text half OBSERVED now, since it is a grep and runs nothing:
  `grep -c 'sweep-ceiling-factor' tools/run-gates/selftest-budgets.txt` is 0 after the unit (the eight header lines 49-56 at BASE
  deleted; the runner's factor read, its refusal arm and its `at its <budget x factor>s bound`
  text retired in the same commit — `grep -c SWEEP_FACTOR tools/run-gates/run-selftests.sh` is 0).
  The fixture half NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate pass
  by `bash tools/run-gates/run-selftests.test.sh`, arm `a sweep-ceiling-factor header staged back
  in is IGNORED` — a factor of 3 is staged (60 x 2 would be the evidence bound's own 120) and the
  arm wants `bounded at 120s: budget won`.
- AC8 — amended rev-7 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/run-gates/run-selftests.test.sh`, three arms: `--serial --calibrate REFUSES
  naming the pair and executes no suite` (rc 2, the marker suite leaving no `ran.marker`),
  `--check --calibrate REFUSES naming the pair` and `a bare --calibrate REFUSES naming the pair`,
  each wanting `--calibrate modifies --pooled and nothing else, and was given with '<mode>'`. The
  refusal sits directly under the argument loop, before the declaration is even opened.
- AC9 — amended rev-7 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/run-gates/run-selftests.test.sh`, arms `--check reds an evidence row whose
  (row, token, node) key repeats, naming the line`, `--check reds a seven-field evidence row,
  naming the line` (`7 field(s), not 9`), `--check reds an evidence row whose node is no tag the
  registry table carries`, `--check reds an ORPHAN evidence row naming no declared budget row`,
  `--check over a well-formed evidence file is green and counts its rows` (`4 pooled evidence
  row(s) well-formed`), and `--pooled over an evidence file that will not parse REFUSES naming the
  file` (rc 2, `will not parse`). On the real tree now, `bash tools/run-gates/run-selftests.sh
  --check` prints `declaration clean — 68 row(s), every held leg budgeted, every row resolvable, 0
  pooled evidence row(s) well-formed`, rc 0, with the factor header gone and the new file present.
- AC10 — amended rev-7 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/run-gates/run-selftests.test.sh`, arms `--reset <row> narrows the calibrate
  to that row, runs no other, and prints the decision` (the other row is the marker suite; wants
  `RESET free one under pooled@2x1 on node t: dropped its 500s reading`), `--reset lowers exactly
  that row's seconds to the new reading, readings back at 1` (an awk over the file: seconds below
  500, readings 1), `--reset moves no other row` (`held one` still at 500), `--reset off
  --calibrate REFUSES by name` and `--reset naming a row the evidence file lacks REFUSES by name`
  (`--reset names 'ghost', and`).
- AC11 — amended rev-7 — NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate
  pass by `bash tools/run-gates/run-selftests.test.sh`, arms `a red-by-design row whose (rc,
  fails, executed) matches its baseline renders ok ... matched and the run exits 0` (seed (1, 3,
  81) against `suite-shard.sh`; wants `ok (rc 1, 3 FAIL, 81 executed matched)`), `a row whose
  triple differs from its baseline renders MISMATCH naming both triples and the acceptance, and
  exits 1` (seed (1, 2, 81)), `a row exiting 1 in under a second with zero FAIL lines against a
  baseline of three is MISMATCH` (`suite-crash.sh`: `(rc 1, 0 FAIL, - executed) against baseline
  (rc 1, 3 FAIL, 81 executed), and NO trailer in its output`), `a suite that exits 0 with no
  trailer is MISMATCH at grade against a seeded green row`, `a GREEN pooled summary prints killed,
  walled, unrun, unstarted and mismatched, each 0`, and one arm per class with the run RED on each:
  `killed 1` (budget-1 `suite-slow.sh`), `walled 1` (the `SELFTEST_WALL=10` pair), `unrun 2` (the
  UNRUN fixture), `unstarted 2` (the fixture's copy of the runner staged with `:
  "$SELFTEST_STAGED_UNBOUND"` before `run_sweep_one` makes its scratch, so every worker dies under
  `set -u` before its verdict file — `killed 0 · walled 0 · unrun 0 · unstarted 2 · mismatched 0`),
  and `mismatched 1` (`suite-red.sh`); plus `a matched red-by-design row still counts as a WITHHELD
  cost verdict` (`2 cost verdict(s) WITHHELD under pooled@2x1`), the line the kit runner parses.
