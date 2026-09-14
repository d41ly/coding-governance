# TOOL-aBatchedArm-5 — the evidence-derived pooled hang bound, and the flip

**Status:** OPEN · rev-4 · 2026-09-14 · node a · Tier-2 · base 1c736fd9 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round1.md](../reviews/2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round1.md) | spec-audit | — |
| [2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round2.md](../reviews/2026-09-14-review-TOOL-aBatchedArm-5-spec-audit-round2.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

`--pooled` exists (`TOOL-aBatchedArm-4`) and the eight shard rows exist (`TOOL-aBatchedArm-3`), and
the pooled run still bounds every row at `budget x sweep-ceiling-factor` — the shape that killed 14
of 58 suites in the full sweep of 2026-09-08 and that three records refused as a predictor. Replace
that bound with the evidence RULE the tree already owns, in the runner's own evidence file, with a
declared calibration mode that grades nothing; and land the DoD flip DARK, so the kit-work DoD moves
from a serial self-test pass to a hang-bounded pooled one plus `--checks` only as the build's landing
step, after the one gate pass has shown the pooled pass complete with every row's rc matching its
calibrated rc. The serial pass stays available on demand, declared, as the cost pass — never as a
DoD line.

## 2. Scope (IN)

- **S1** — a pooled row's HANG bound is derived from OBSERVED pooled readings, not from its serial
  budget: `max(<serial budget>, <worst reading>)` under this node and the runner's own condition
  token (`pooled@<outer>x<inner>` at the text `SWEEP_CONDITION=`), monotone, plus
  `tools/run-gates/ceiling-margin.txt`'s headroom of `max(<floor>, <fraction> x that)` READ from the
  file beside the runner (`$HERE/ceiling-margin.txt`; the runner refuses when it is absent — the
  refusal `derive-ceilings.py` makes, reused as a rule and not imported, because the runner is
  bash). The serial-budget floor is the guard against a fast red: a pooled row cannot legitimately
  need less than its serial budget, so a 0.3 s refusal recorded as a reading never bounds a repaired
  suite below what it costs alone; the verdict prints which term won. **A row with NO reading under
  (row, token, node) REFUSES the pooled run naming the row, the token and `--calibrate`, and executes
  no suite — the whole population `--pooled` or `--sweep` reaches, not only the filtered one.** There
  is no fallback: the `sweep-ceiling-factor:` header in `selftest-budgets.txt`, its refusal arm at
  the text `declares no sweep-ceiling-factor`, and the `at its <budget x factor>s bound` verdict text
  are RETIRED in the same commit, so no factor-derived bound survives to be fallen back on. **The
  graded run's WALL** is derived from the evidence bounds by the shape the runner already uses for
  the factor: `ceil(sum of bounds / OUTER)`, floored at the largest bound; `SELFTEST_WALL` still
  overrides and the existing below-the-largest refusal compares against the largest evidence bound.
  Every pooled verdict prints the reading, token, node and date it was bounded by, and the pooled
  summary line counts `killed` rows and `rc-mismatched` rows SEPARATELY — a row whose rc differs
  from the rc its evidence row recorded — so a landing can read completion off the summary without
  re-deriving it from the rows. Observed by **AC1**, **AC2** and **AC7**.
- **S2** — the bootstrap is DECLARED: `--pooled --calibrate` runs EVERY row the invocation selects
  (bare, or `--kit <dir>`), evidenced or not, under ONE wall, the SUM of the selected rows' serial
  budgets, undivided — the population fully serialised, the largest backstop derivable with no typed
  number; a pooled pass exceeding its own serial sum is a hang and not a cost — `SELFTEST_WALL`
  tightening it only, the derived wall and which term won printed. No per-row bound. It withholds
  every verdict and records a reading ONLY for a row that exited on its own: rc captured, not killed
  by the wall. A row the wall killed writes NO reading, is named, and makes the calibrate run exit
  RED. Readings are written AFTER the sweep's closing fingerprint (`FP_AFTER`, the text
  `read_tree_fingerprint`), in one pass over the collected verdicts, because the evidence file is
  tracked and a write inside the fingerprinted window reds the runner's own run as UNSOUND. Every
  reading raises its (row, token, node) row monotone — never lowers it — the `rc` column being the rc
  of the reading that set the max; the summary line is `calibrated <n> row(s), <r> red, graded none`
  on green and `calibrated <n> row(s), <r> red, <k> killed, graded none` on red, neither of which the
  kit runner's `sweep GREEN` / `WITHHELD` parser can read as a verdict. `--calibrate` with any verb
  or mode other than `--pooled` REFUSES naming the pair. Observed by **AC3** and **AC8**.
- **S3** — pooled readings live in their OWN tracked file, `tools/run-gates/selftest-pooled-evidence.txt`,
  one row per (row name, condition token, node): `<row>\t<condition>\t<node>\t<max seconds>\t<rc>\t<readings>\t<date>`.
  The node is the charter's §2 registry TAG: `GOV_NODE` when set, else `USERNAME`/`USER` resolved
  against the registry table the way `tools/drift-audit/drift_report.py`'s `_resolve_node_tag` does,
  REFUSING by name when no row matches — never a hostname, which the registry does not know. The
  file is written by `--pooled --calibrate` and lowered only by `--reset <row>` on the same
  invocation, which is a decision somebody made and prints as one. Its SHAPE is graded by
  `run-selftests.sh --check`, the unguarded bar leg: every non-comment line has seven tab fields,
  seconds and readings parse, readings is at least one, the node is a registry tag, no (row, token,
  node) key repeats, and every row names a row the budget file declares — a hand-edited, truncated
  or orphaned row reds on the bar, and an orphan is the right red: a deleted budget row takes its
  evidence with it or the file lies. It ships to no adopter: `tools/run-gates/kit.toml` gains a
  `project-owned` rule for it beside the three it already carries for the same reason. NOT in
  `ceiling-evidence.txt` and NOT in `selftest-budgets.txt`'s fourth column, so `--rank`'s refusal of
  `pooled@` readings (`TOOL-aQuenchedHarness-6` S3a) is untouched and shard budgets stay serial.
  Observed by **AC4** and **AC9**.
- **S4** — the flip lands DARK, the population it grades is DERIVED, and the DoD it replaces is
  named. The kit-work DoD today is `kit.toml:122-126`'s two pasted lines, and its second,
  `--all --serial`, runs the self-tests serially AND the checks (`ONLY=""` at the text `--all)`), so a
  flip that kept it would ADD a pooled pass to a serial one; after the flip the DoD is
  `run-unattended-gates.sh --pooled` plus `run-unattended-gates.sh --checks`, the block's
  `not done until` sentence re-worded to bind those two, and `--selftests --serial` is the declared
  cost pass ON DEMAND, per the owner's 2026-08-23 standing instruction at
  `memory/guides/SESSION-KICKOFF.md:169`, never a DoD line. The carrier set is the predicate `a line
  spelling --selftests --serial, run-unattended-gates.sh --serial, or run-unattended-gates.sh --all
  --serial`, which excludes the runner's own usage grammar at `:142`; it yields eight lines in six
  files at this base, re-derived at build time and pasted in the ledger: `.githooks/gate-env.sh:27`,
  `AGENTS.md:519`, `tools/unattended/kit.toml:125` and `:126`, `tools/unattended/README.md:66`,
  `tools/unattended/run-unattended-gates.sh:27` and `:233`, `memory/guides/SESSION-KICKOFF.md:169`.
  Inside this unit seven of them gain, beside `--serial`, the words `--pooled after calibration` —
  `land dark`, unit 4 r2 B1's rule — and `AGENTS.md:519` takes NO dark spelling, because
  `bash tools/check-template-size.sh AGENTS.md` measures it 9 bytes under its declared cap and the
  flip there is `--serial` for `--pooled`, eight bytes for eight. **The flip itself is the BUILD's
  landing step, not this unit's**, in this order on the MERGED tree (`TOOL-aLoosenedCeiling-3`: a
  ceiling is re-derived on the merged tree, never carried): (1) `run-selftests.sh --kit
  tools/unattended --pooled --calibrate` over the population `run-selftests.sh --kit
  tools/unattended --list` resolves (fourteen rows at this base — the list's number); on a red, the
  killed rows are named in the landing record, the build lands WITHOUT the flip, and AC3's real-row
  half is ledgered amended naming them; (2) the evidence file is committed; (3)
  `run-unattended-gates.sh --pooled` runs and its pooled summary is pasted — the witness is NOT the
  driver's exit status, which folds the oracle's red into the verdict (unit 3 AC11: the eight shard
  rows are RED by design, 21 `FAIL` lines, and `check-unattended.test.sh` exits 1 on any), but the
  summary's `killed 0`, `rc-mismatched 0` and `fingerprint MATCHED`; (4) ONLY THEN the flip commit:
  the seven dark lines drop `--serial`, `kit.toml:126` becomes `--checks`, the block's binding
  sentence and `SESSION-KICKOFF.md:169` are re-worded, `AGENTS.md:519` swaps eight bytes, and
  `last-audit` is re-stamped. On a red at step (3) the carriers stay as landed, AC5's landing half is
  ledgered amended naming the red, and the build lands without the flip. Observed by **AC5** and
  **AC6**.

## 3. Non-goals (OUT)

- **A contention model that makes a pooled COST verdict sound.** Still withheld under `--pooled`.
  The evidence bound is a HANG bound; it says when a run has stopped answering, never what it cost.
- **Observing the host's LOAD.** `pooled@8x1` names a width and a node, not whether another
  worktree's bar is running. Taking the turnstile or recording beacon state is named and not built;
  the evidence shape tolerates it by being monotone over whatever was observed, and `--calibrate`
  re-run on a loaded day raises the row rather than being refused.
- **Calibrating any row outside the population the DoD command resolves.** A bare `--pooled` over
  the whole declaration refuses until every row it reaches is calibrated, by name; nobody is
  obliged to calibrate them by this unit, and the refusal is the announced-unarmed state. The count
  of those rows is the budget file's to report.
- **Deciding the arity or the 20-minute question.** Unit 3's AC4 arm two is read at the same final
  pass; this unit's bound grades whatever that reading is.
- **A per-row FAIL-set oracle in the runner.** The landing reads rc parity against the calibrated
  rc; the FAIL-set equivalence unit 3 established is unit 3's, observed there, not re-derived by the
  pooled pass.

### Edges

- **consumes-from** `TOOL-aBatchedArm-4` — the `--pooled` mode, the kit runner's pooled path, and
  the carriers it landed dark.
- **consumes-from** `TOOL-aBatchedArm-3` — the eight shard rows, part of the population this unit's
  S2 calibrates at the final pass.
- **hands-off** `none`

## 4. Design

### Why the evidence shape and not a factor

Three records and one measurement. `TOOL-dRetiredFork-40` measured 443 s under load against 583 s
quiet and refused to predict one from the other by multiplying. `TOOL-aPooledSweep-2` §3 refused a
factor "derived from one suite … applied to fifty-eight it was never measured on". The full-sweep
record's own remedy is re-sizing against pooled readings. And `derive-ceilings.py` already owns the
rule: worst observed under the condition, monotone, floor-plus-fraction headroom, refusing to report
with no evidence, `--reset` as the one lowering path. Its fifth part — readings from `ok` runs only,
because "a leg that FAILED may have failed fast" — is DEPARTED from here, deliberately: the eight
shard rows are red by design and exit 1 when complete, so an ok-only reader would refuse them
forever. What replaces it is the serial-budget floor under the bound, which makes a fast red
harmless without having to tell it from a slow one.

### Why the calibrate wall is the serial SUM and not a division

Round 2 did the arithmetic the fold had not: `ceil(sum / OUTER)` floored at the largest serial
budget gives 3860 s for the fourteen-row population at width 8, and the tree's own sweep record
(`TOOL-aPooledSweep-1`'s full-sweep rows, slot 54) shows the driver suite alive at 7722 s under that
width — the divided wall is killed by the record this spec cites as its motivation. The bootstrap's
wall is a backstop against a HANG and not a prediction of cost, so it is the population fully
serialised: nothing pooled can honestly need longer than everything run one after another. It is
derivable, prints itself, and puts no typed number in the DoD.

### Why the bootstrap is a declared mode, and why it refuses in three places

The evidence shape cannot bound a row that has never been observed, and `--sweep`'s own S7 forbids
an unbounded pooled row. So the first observation is taken under the serial-sum wall, in a mode that
says it is calibrating and grades nothing. It refuses a killed row (a truncation is not a reading —
the `ab-arm` class), refuses any mode but `--pooled` (a `--serial --calibrate` that ran the serial
loop and wrote nothing would be silent in a mode whose point is announcing itself), and refuses a
file that does not parse.

### Why the flip is the build's landing step and not this unit's

`TOOL-aBatchedArm-4` landed `--pooled` dark because the bound it inherits killed five of the seven
current unattended rows. Re-pointing the carriers is the act that makes the fast path the recorded
DoD verdict, and it happens only after the bound that would grade it is the evidence one and has
been seen to COMPLETE over every row the DoD command resolves — fourteen at this base, not the
eight a draft of this spec typed — with each row's rc matching its calibrated rc. "GREEN" is not
the criterion and cannot be: the oracle for eight of those rows is a red-by-design `FAIL` set, so
the driver's exit is 1 on a perfect pass. Two owner rulings (2026-09-13, 2026-09-14) defer every
gate run to one pass when every unit is built, so the observation that licenses the flip cannot
happen inside this unit; landing the flip as text before it would record a DoD command with no
completing run, which is the false-green shape one level up and what unit 4's AC7 reds by name.
Hence dark: both spellings on every carrier but the one at its byte cap, the pooled one marked, and
the flip commit ordered after the pasted summary.

### Why the node is the registry tag

Unit 3 measured a checker invocation at 47 to 60 s on node `a` against the ~2 s another host
records; a 2x headroom cannot absorb that spread, so the key carries the node. It carries the
REGISTRY tag and not a hostname because `GOV_NODE` is set nowhere in the tree, so a hostname would
be what every real invocation wrote — a name the charter's §2 table does not know and the sibling
`ceiling-evidence.txt` does not use. `_resolve_node_tag` already maps this machine's user to `a`.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` (the fixture rebuild:
`build_repo` gains a fixture `ceiling-margin.txt` with a small floor and a seeded, TRACKED evidence
file covering every token the arms produce — `pooled@2x1` by default, since `W` falls to 2 without
`run-gates.sh`, and `pooled@1x2` under the arms that set `SELFTEST_OUTER_WIDTH=1` — and every row an
arm appends at run time seeded in that arm's setup under the token it runs at; the readings seeded
are sized so the `SELFTEST_WALL=10` kill arm and the `SELFTEST_WALL=5` below-largest arm stay
reachable) · `tools/run-gates/selftest-pooled-evidence.txt` (new, tracked, names row NAMES and no
path, so it takes no `install-prefix-carried.txt` row) · `tools/run-gates/kit.toml` (the
`project-owned` rule) · `tools/run-gates/selftest-budgets.txt` (the retired factor header) · the
seven dark carrier lines above · `tools/unattended/run-unattended-gates.sh` (the pooled summary's
`killed` / `rc-mismatched` counts) · `memory/guides/SESSION-KICKOFF.md` (`run-selftests.sh` is on
its `watch:` line, so `last-audit` is re-stamped in the same commit; `:169` is re-worded only at the
flip) · this build's records.

## 5. Production-readiness checklist

- security — N/A. Bound derivation and verdict wording.
- perf / scale — the pooled path becomes the recorded kit-work DoD only at the build's landing; its
  wall clock is whatever the final pass measures, graded rather than hand-run from then on. The
  flip REMOVES the serial self-test pass from the DoD (`--all --serial` becomes `--checks`) rather
  than adding a pooled one beside it.
- error / empty / loading states — a row with no evidence under this node and token REFUSES the
  pooled run by name; a calibration run prints that it graded nothing and reds on a killed row; an
  evidence file that will not parse refuses rather than defaulting; `--calibrate` off `--pooled`
  refuses; a node with no registry row refuses; `--check` reds a malformed, duplicated or orphaned
  evidence row.
- observability — every pooled verdict names the reading, token, node and date it was bounded by
  and which term of the bound won; the pooled summary counts killed and rc-mismatched rows
  separately; the calibrate prints its derived wall and which term won.
- risks — the evidence is monotone over whatever was observed, so a calibration taken on a loaded
  box sets a loose bound for that row until `--reset`; a first reading taken on a quiet box is
  raised by the next `--calibrate`, which runs every row; a fast red cannot bound a row below its
  serial budget. The direction NOT covered: a reading taken on a day slower than any later day is
  never lowered except by `--reset`, and that is the monotone rule's price, stated.
- testing — the runner's self-test gains arms for: the no-evidence refusal; the foreign-node
  refusal; the calibrate mode grading nothing; a bound derived from a staged evidence row, with the
  serial-budget floor taking over for a tiny reading; the killed-row RED with no reading written;
  the monotone raise and the `--reset` lowering; `--calibrate` off `--pooled` refusing; the
  unparseable file refusing; `--check` redding a duplicated key and an orphaned row; the wall
  derived from evidence bounds and the below-largest refusal against it; a calibrate over a clean
  fixture reporting `fingerprint MATCHED` with the file changed; the pooled summary counting a
  killed row and an rc-mismatched row separately. Each observed RED first.
- migration — the seven carriers gain the dark spelling in this unit, reversible by one line each;
  the flip is the build's landing step and reverts the same way.
- user docs — the runner's `--help` names `--calibrate` and `--reset`; the kit runner's names the
  dark spelling, the landing order, and that `--selftests --serial` is the cost pass on demand.

## 6. Acceptance criteria

- **AC1** — When a fixture row has a reading in `selftest-pooled-evidence.txt` under the fixture's
  condition token and node, `run-selftests.sh --pooled` bounds it at `max(serial budget, reading)`
  plus the fixture `ceiling-margin.txt`'s headroom, prints the reading, token, node, date and which
  term won, and the run's wall line is `ceil(sum of bounds / OUTER)` floored at the largest bound;
  and a fixture row whose seeded reading is far below its serial budget is bounded from the budget.
  `fixture:` the runner's own test fixture with staged evidence rows, run by
  `bash tools/run-gates/run-selftests.test.sh`; no real suite runs.
  Red when: the bound or the wall is the serial budget times any factor, the verdict names no
  reading, or a tiny reading bounds a row below its serial budget.
- **AC2** — When a fixture row has NO reading under this node and token, `run-selftests.sh --pooled`
  REFUSES naming the row, the token and `--calibrate`, and executes no suite; a row evidenced under
  a FOREIGN node refuses the same way; and a node that resolves to no registry row refuses naming
  the user.
  `fixture:` as AC1.
  Red when: it runs the row under any bound, which is a factor wearing a refusal's name.
- **AC3** — When `run-selftests.sh --pooled --calibrate` runs over the fixture rows, each is bounded
  by the serial-sum wall only, no `OVER BUDGET` and no `TIMEOUT` verdict is printed, each completed
  row's reading is written with its token, node and rc after `fingerprint MATCHED`, an existing row
  is raised and never lowered, and the summary says `calibrated <n> row(s), <r> red, graded none`;
  and when one fixture row sleeps past the wall, that row writes NO reading, is named, and the run
  exits RED with `<k> killed` in its summary.
  `fixture:` as AC1, inside this unit; the real population at the build's landing, step (1) of S4.
  `cost:` at the landing, one pooled pass of the population `--kit tools/unattended --list`
  resolves under the serial-sum wall, its longest row the floor of that pass.
  Red when: a calibration prints a verdict, a killed row's seconds land in the file, a second
  calibrate with a lower reading lowers a row, the write lands inside the fingerprinted window, or
  the real pass kills a row and the landing has no record naming it.
- **AC4** — When `run-selftests.sh --rank` runs in the fixture after a calibrate, it exits 0; and on
  the real tree `grep -c pooled@ tools/run-gates/selftest-budgets.txt` is 0 before and after the
  unit, and `--rank`'s unbacked list is the same list before and after.
  `fixture:` as AC1 for the first half; a grep and a diff on the real tree for the second.
  Red when: a `pooled@` token appears in the budget file, or the unbacked list moved.
- **AC5** — When the carrier lines the S4 predicate yields are read as text after this unit's
  commit, seven name `--pooled after calibration` beside `--serial` and `AGENTS.md:519` is
  unchanged; and at the build's landing, `bash tools/unattended/run-unattended-gates.sh --pooled` on
  the merged tree over the population `--kit tools/unattended --list` resolves prints a pooled
  summary with `killed 0`, `rc-mismatched 0` and `fingerprint MATCHED`, pasted, and the flip commit
  follows it — that half owed until then, in the amended form.
  `figure:` the carrier count is DERIVED by the S4 predicate at build time and pasted in the ledger.
  `cost:` one real pooled pass on the merged tree, at the landing.
  Red when: a DoD line names `--pooled` alone before the pasted summary, `AGENTS.md` moved, the
  landing pass kills or rc-mismatches a row and the flip lands anyway, or after the flip
  `kit.toml:126` still runs the self-tests.
- **AC6** — When the existing `--serial` arms of `run-selftests.test.sh` run after this unit, they
  are GREEN unchanged: the serial mode still issues `OVER BUDGET` cost verdicts, because this unit
  touched no serial path.
  `fixture:` as AC1.
  Red when: any pre-existing serial arm moved.
- **AC7** — When `selftest-budgets.txt` is read after this unit, it carries no
  `sweep-ceiling-factor:` header, and `run-selftests.sh --pooled` over the fixture with a factor
  header staged back in ignores it — the bound and wall are the evidence ones.
  `fixture:` as AC1.
  Red when: any factor-derived bound or wall prints.
- **AC8** — When `run-selftests.sh --serial --calibrate`, `--check --calibrate` or bare `--calibrate`
  runs, each REFUSES naming the pair and executes no suite.
  `fixture:` as AC1.
  Red when: any of them runs a row or writes a reading.
- **AC9** — When `run-selftests.sh --check` runs over an evidence file with a duplicated
  (row, token, node) key, a six-field row, a row whose node is no registry tag, or a row naming no
  declared budget row, it REDS naming the line; and `--pooled` over a file that will not parse
  REFUSES naming the file.
  `fixture:` as AC1.
  Red when: `--check` is green over any of the four, or `--pooled` defaults past the parse.

## 7. Gates

`memory hygiene` · `run-selftests self-test` · `every held leg is budgeted, every budget row resolves`
· `install-prefix (shipped surface)` · `charter size` · `kickoff-manifest ratchet` · `run-gates canary`
· `run-gates gov canary` · `run-gates evidence` · `run-gates turnstile` · `run-gates adopter e2e`
· `profile-bar selftest` · `lexicon naming predicates` · `govkit selfcheck` · `push-main self-test`
· `check-wiring self-test`

The list names the legs whose SUBJECT this unit changes; the full bar at the final pass decides the
rest by its own guards. **This is KIT work, and nine of these legs are HELD** under the run's
declared `GATE_CMD` (`bash tools/run-gates/run-gates.sh`, bare): `run-selftests self-test`,
`run-gates canary`, `run-gates gov canary`, `run-gates evidence`, `run-gates turnstile`,
`run-gates adopter e2e`, `profile-bar selftest`, `push-main self-test`, `check-wiring self-test` —
`chunk: selftests` or `subject: kit`, written `ondemand` by the bare bar since the owner's 2026-08-27
ruling. `run-selftests self-test` is the ONLY leg that executes the fixture arms behind AC1, AC2,
AC6, AC7, AC8, AC9 and the fixture halves of AC3 and AC4, so the build's final gate pass runs the
kit-work DoD `AGENTS.md` names, `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`,
and pastes its verdict beside `gates-green` in the landing record rather than assuming it inside.

New arm: `tools/run-gates/run-selftests.test.sh` · the arms §5 testing lists, each staged RED then
unstaged, over the rebuilt fixture · every pooled arm the factor arithmetic reached is RE-CUT to the
evidence shape and enumerated in the ledger: the factor `TIMEOUT` arm, `run wall 140s`, the UNRUN
arm (its appended rows seeded), the `SELFTEST_WALL=10` kill arm, the `SELFTEST_WALL=5`
below-largest arm; the factor-absent refusal arm is RETIRED with the header · floor to move: the
suite's own, up by the arms added and down by the one retired, both counts derived at build time.

## 8. Open questions

- **F1 · Does the evidence file take a per-row condition token, or one per run?** Per row.
  RESOLVED (agent, 2026-09-14, delegated): per (row, token, node) in the runner's OWN evidence file;
  rev-1 named `derive-ceilings.py`'s reader as the seam and that was wrong at source — its file has
  no condition column, is generated from bar leg files, and refuses hand rows by its header.
- **F2 · What if unit 3's AC4 measurement misses 20 minutes?** Then the flip still happens if the
  bound is sound — the goal is the owner's target and the flip is about correctness, not speed — and
  the miss is recorded against the host's spawn path per `TOOL-aBatchedArm-4` §4. RESOLVED (agent,
  2026-09-13, delegated): the flip is gated on the bound, not on the 20 minutes.
- **F3 · Refuse or fall back for an uncalibrated row?** RESOLVED (agent, 2026-09-14, delegated):
  REFUSE, and retire the factor so nothing survives to fall back on. A fallback is the bound that
  killed 14 of 58, and a refusal names what to type.
- **F4 · Where does the flip land?** RESOLVED (agent, 2026-09-14, delegated): dark in this unit,
  flipped as the build's landing step after the pasted pooled summary on the merged tree. The
  alternative — a DoD line naming a command with no completing run — is the shape unit 4 AC7 reds.
- **F5 · Which wall bounds a calibration?** RESOLVED (agent, 2026-09-14, delegated): the SUM of the
  selected rows' serial budgets, undivided, `SELFTEST_WALL` tightening only. The divided form,
  `ceil(sum / OUTER)` floored at the largest budget, was rejected at round 2 because the tree's own
  sweep record kills it (3860 s against a 7722 s driver row at width 8); the profile row is the
  borrow `TOOL-aPooledSweep-1` rev-3 refused; a REQUIRED `SELFTEST_WALL` would put a typed number
  in the DoD.
- **F6 · Is GREEN the landing criterion?** RESOLVED (agent, 2026-09-14, delegated): no — eight of
  the fourteen rows are red by design (unit 3 AC11), so the driver exits 1 on a perfect pass. The
  criterion is the pooled summary's `killed 0`, `rc-mismatched 0` and `fingerprint MATCHED`.

## 9. Revision log

- rev-4 · 2026-09-14 · §1 · §2 S1 through S4 · §3 · §4 · §5 · §6 AC1 through AC9 · §7 · F5 · F6 ·
  §10 · folded spec-audit round 2 (BLOCKED, 2 blockers, 15 highs, 7 mediums, 1 low, 25 confirmed
  rows in 11 defects, precision 0.49, CONVERGING from 3). The landing criterion is no longer GREEN,
  which the red-by-design oracle forbids, but the pooled summary's `killed 0` / `rc-mismatched 0` /
  `fingerprint MATCHED`, the kit runner's pooled branch gaining those two counts (B1). The calibrate
  wall is the serial SUM undivided, since the divided form is killed by slot 54 of the sweep record
  the spec cites; the step-one red lands without the flip (B2, H1). The flip REMOVES the serial DoD
  pass: `kit.toml:126` becomes `--checks`, the binding sentence and `SESSION-KICKOFF.md:169` are
  re-worded at the flip, `--selftests --serial` is the cost pass on demand (H2, M1). `AGENTS.md:519`
  takes no dark spelling, eight bytes for eight at the flip, measured 9 under its cap (H3). The
  reading witness is rc captured with the bound floored at the serial budget, `derive-ceilings`'
  ok-only clause DEPARTED from by name (H4, M3). Readings are written after `FP_AFTER`; the fixture
  evidence file is tracked (H5). The seed covers both tokens the arms produce and the rows arms
  append; every pooled arm re-cut is enumerated (H6, M4). §7 marks the nine held legs and names
  `GATE_FULL=1 GATE_SELFTESTS=1` as the final pass's kit-work invocation (H7, M5). The carrier set
  is a stated predicate whose output is the list, `:142` excluded by it (H8, M2). The node is the
  registry tag via `_resolve_node_tag`'s rule (M6). The `unattended skill wiring` claim is dropped
  and the parity arm's home is `govkit selfcheck` (M7); §7's derivation sentence corrected (L1).


- rev-3 · 2026-09-14 · §1 · §2 S1 through S4 · §3 · Edges · §4 · §5 · §6 AC1 through AC9 · §7 ·
  F3 · F4 · F5 · §10 · folded spec-audit round 1 (BLOCKED, 3 blockers, 13 highs, 11 mediums, 1
  low, 28 confirmed rows in 11 defects, precision 0.52). The four scope decisions first: the
  population is the DoD command's RESOLVED one (`--kit tools/unattended --list`, fourteen rows at
  this base, never typed — B1, B2, H1, M1); the flip lands DARK here and flips as the build's
  landing step on the merged tree after the pasted GREEN, with the landing order and the red
  outcome written (B3, H2, M2); an uncalibrated row REFUSES and the factor header, its arm and its
  verdict text are retired, the graded wall derived from the evidence bounds and the calibrate wall
  from the serial budgets (H3 through H7); the rule is reused WHOLE — readings only from rows that
  exited on their own with a RED calibrate on a killed one, every row raised monotone on every
  calibrate, `--reset <row>` as the lowering path, node in the key (H8 through H11, M10). Then the
  mechanical set: the fixture rebuild with a seeded margin and evidence file and the two factor-shape
  arms re-cut (H12); AC4's witness is the fixture's `--rank` plus the real tree's `pooled@` grep and
  an unchanged unbacked list, since `--rank` exits 1 at this base for unit 3's derived shard-8 row
  (H13, M3); the carriers enumerated by grep as eight lines in six files with `kit.toml:126`
  declared the cost line and AC5's red-when corrected (M4, M5); the `kit.toml` `project-owned` rule
  and the manifest re-stamp in Files touched (M6 through M9); §7 re-derived over `gate-legs.json`
  (M11); the unparseable-file arm and the `--calibrate`-off-`--pooled` refusal (L1). AC6 is no
  longer a flip diff, since no flip lands here; it is the existing serial arms unchanged.


- rev-2 · 2026-09-14 · §2 S1 · S3 · S4 · §3 · §4 · §6 AC1 · AC3 · AC5 · AC6 · §7 · F1 · §10 · base ·
  pre-audit correction of a seam claim verified false at source, plus the owner rulings. rev-1 put
  pooled readings in `ceiling-evidence.txt` keyed by name and condition token; that file is
  GENERATED from `<git-dir>/gate-run/*/*.leg` by `derive-ceilings.py --write`, has five columns and
  no condition, says `Do not hand-edit`, and its `--check` prints a stale-row note for every row
  naming no manifest leg — so a self-test row there is a second writer to a generated artifact. The
  store is now the runner's own `selftest-pooled-evidence.txt`, same monotone/margin RULE, the
  margin READ from `ceiling-margin.txt`. The 2026-09-14 ruling (no gate until every unit is built)
  moves AC3's and AC5's real-row observations to the build's final gate pass; AC6 becomes a diff.
  The `ceiling evidence` gate leaves §7, since this unit no longer touches its file. Base bumped to
  `1c736fd9`, where units 3 and 4 are CLOSED and the eight rows exist.
- rev-1 · 2026-09-13 · initial draft, from `TOOL-aBatchedArm-4`'s three audit rounds, which
  specified this unit's shape while refusing it inside that one: the evidence-derived bound (r1 B5),
  the flip landed dark and owned here (r2 B1), and the declared bootstrap. Authored now rather than
  after unit 3 because memory hygiene check 14 reds on a cited id with no spec, and the id was cited
  at `9b00bc7b`.
## 10. Reuse audit


- **The seam is the RULE in `tools/run-gates/derive-ceilings.py`** — worst-observed, monotone,
  `max(floor, fraction x max)`, refusing with no evidence — and the margin file it reads,
  `tools/run-gates/ceiling-margin.txt`, verified at source. Its FILE, `ceiling-evidence.txt`, is
  NOT reused: verified at source on 2026-09-14, it is generated from bar leg files, keyed by leg
  name with no condition column, and its header forbids hand rows; rev-1's claim that it was the
  seam was wrong. The condition token `pooled@<outer>x<inner>` is the runner's own at the text
  `SWEEP_CONDITION=`. The `--rank` refusal of `pooled@` at the text `REFUSED = [re.compile(r"pooled@")]`
  is REUSED by keeping pooled readings OUT of the budget file. The
  reuse probe was run —
  `python tools/codebase-map/reuse_lookup.py "derive a pooled hang bound from observed readings under a condition token with monotone evidence and declared headroom"`
  — and returned `read_text`, `read` and `derive_scope`, none of which is this seam; it reports
  `unscanned layers: .sh` and `derive-ceilings.py` is Python it did not rank, so its result is not
  evidence either way. The seam was found by reading `derive-ceilings.py` and the two files beside
  it.
- **The parts of that rule this spec now carries by name**, because round 1 found the reuse was
  the file's header and not the rule: `read_runs` counts completed runs only (`derive-ceilings.py`,
  the text `may have failed fast`); `--write` raises every measured row monotone; `--reset <leg>` is
  the one lowering path; `GOV_NODE` is its node spelling, which the runner reuses with the hostname
  as the fallback the script does not have (it defaults to `a`, which is wrong on every other node
  and is not reused).
- **The `ok`-only clause of that rule is DEPARTED from**, by name: unit 3's shard rows exit 1 when
  complete, so an ok-only reader refuses them forever; the replacement is the serial-budget floor
  under the bound, which makes a fast red harmless. Round 2 caught the paraphrase claiming the
  clause was reused; it is not.
- **The node resolver is `tools/drift-audit/drift_report.py`'s `_resolve_node_tag`** — `USERNAME`
  or `USER` against the charter's §2 registry table — whose rule S3 reuses; `TOOL-aCollapsedScan-9`
  (OPEN) names the per-node reading as a candidate. `derive-ceilings.py`'s `GOV_NODE ... or "a"`
  default is the same class and is a backlog follow-up, not this unit's.
- **The carrier-parity arm** round 1 asked for has its home in `govkit selfcheck`, the one reader of
  every `kit.toml`, or `tools/check-playbook-parity.sh`, whose job is retyped constants against the
  source that owns them — named here and not built by this unit. The `unattended skill wiring` leg
  is `adopt-unattended.sh --check` and reads neither carrier, so rev-3's claim that it did is
  withdrawn.
- **The retrieval arguments, verbatim:**
  `python tools/memory-recall/query.py "why does the self-test runner run suites serially by default and pool only under sweep, and what was measured about cost attribution under contention" --terms "run-selftests OUTER pool sweep serial budget contention dilation attribution width verdict withheld mode declared"`.
  Run for unit 4; it surfaced `TOOL-dRetiredFork-40`, `TOOL-aPooledSweep-2` and the full-sweep record
  this unit's §4 rests on.
