# TOOL-aBatchedArm-5 — the evidence-derived pooled hang bound, and the flip

**Status:** OPEN · rev-1 · 2026-09-13 · node a · Tier-2 · base c2db2f5d · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`--pooled` exists (`TOOL-aBatchedArm-4`) and the eight shard rows exist (`TOOL-aBatchedArm-3`), and
the pooled run still bounds every row at `budget x sweep-ceiling-factor` — the shape that killed 14
of 58 suites in the full sweep of 2026-09-08 and that three records refused as a predictor. Replace
that bound with the evidence shape the tree already owns, then re-point the DoD carriers from
`--serial` to `--pooled`. This is the unit that makes the fast path the recorded one.

## 2. Scope (IN)

- **S1** — a pooled row's HANG bound is derived from OBSERVED pooled readings, not from its serial
  budget: the worst reading recorded under the runner's own condition token (`pooled@<outer>x<inner>`,
  node, date), monotone, plus `tools/run-gates/ceiling-margin.txt`'s headroom of
  `max(120 s, 1.0 x max)`. That is `tools/run-gates/derive-ceilings.py`'s shape, reused. A row with
  NO pooled observation REFUSES the pooled run naming itself, never falls back to a factor. Observed
  by **AC1** and **AC2**.
- **S2** — the bootstrap is DECLARED: `--pooled --calibrate` runs rows that have no pooled
  observation under the profile's whole-run wall only, withholds every verdict including the hang
  kill, records each row's reading with its condition token into the evidence file, and prints that
  it calibrated rather than graded. It is how the first reading gets taken at all, and it is never
  the default. Observed by **AC3**.
- **S3** — pooled readings live in the ceiling-evidence file beside the bar's, keyed by row name and
  condition token, NOT in `selftest-budgets.txt`'s fourth column — so `--rank`'s refusal of
  `pooled@` readings (`TOOL-aQuenchedHarness-6` S3a) is untouched and shard budgets stay serial.
  Observed by **AC4**.
- **S4** — once every row the kit runner's self-test half resolves has a pooled observation, the
  four DoD carriers `TOOL-aBatchedArm-4` S6 names are re-pointed from `--serial` to `--pooled`, and
  a declared `--selftests --serial` remains the cost pass. The flip is this unit's LAST act and is
  gated on S1 through S3 being green over the real rows. Observed by **AC5** and **AC6**.

## 3. Non-goals (OUT)

- **A contention model that makes a pooled COST verdict sound.** Still withheld under `--pooled`.
  The evidence bound is a HANG bound; it says when a run has stopped answering, never what it cost.
- **Observing the host's condition.** `pooled@8x1` still names a width and not whether another
  worktree's bar is running. Taking the turnstile or recording beacon state is named and not built;
  the evidence shape tolerates it by being monotone over whatever was observed.
- **Re-sizing any row outside the unattended kit.** The evidence file is populated only for rows
  a `--pooled --calibrate` run touched; the other 54 rows keep their inherited bound until someone
  calibrates them, and this unit says so rather than pretending to have.

### Edges

- **consumes-from** `TOOL-aBatchedArm-4` — the `--pooled` mode, the kit runner's pooled path, and
  the carriers it landed dark.
- **consumes-from** `TOOL-aBatchedArm-3` — the eight shard rows, whose first pooled run is the
  calibration this unit's S2 takes.
- **hands-off** `none`

## 4. Design

### Why the evidence shape and not a factor

Three records and one measurement. `TOOL-dRetiredFork-40` measured 443 s under load against 583 s
quiet and refused to predict one from the other by multiplying. `TOOL-aPooledSweep-2` §3 refused a
factor "derived from one suite … applied to fifty-eight it was never measured on". The full-sweep
record's own remedy is re-sizing against pooled readings. And `derive-ceilings.py` already exists:
worst observed under the condition, monotone, floor-plus-fraction headroom, refusing to report with
no evidence. Nothing here is invented; the runner's pooled path learns to read the file the bar
already writes.

### Why the bootstrap is a declared mode

The evidence shape cannot bound a row that has never been observed, and `--sweep`'s own S7 forbids
an unbounded pooled row. So the first observation is taken under the whole-run wall and nothing else,
in a mode that says it is calibrating and grades nothing. A calibration that looked like a verdict
would be the false-green shape one level up.

### Why the flip is last

`TOOL-aBatchedArm-4` landed `--pooled` dark because the bound it inherits killed five of the seven
current unattended rows. Re-pointing the carriers is the act that makes the fast path the recorded
DoD verdict, and it happens only after the bound that would grade it is the evidence one and has been
seen green over every row it will grade.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh`, `tools/run-gates/run-selftests.test.sh`,
`tools/run-gates/ceiling-evidence.txt`, the four carriers `TOOL-aBatchedArm-4` S6 names, and this
build's records.

## 5. Production-readiness checklist

- security — N/A. Bound derivation and verdict wording.
- perf / scale — the pooled path becomes the recorded one; its wall clock is whatever unit 3's AC4
  measured, now graded rather than hand-run.
- error / empty / loading states — a row with no pooled evidence REFUSES the pooled run by name; a
  calibration run prints that it graded nothing; an evidence file that will not parse refuses rather
  than defaulting.
- observability — every pooled verdict names the evidence it was bounded by, with its condition
  token and date, so a kill can be read against the reading that set the bound.
- risks — the evidence is monotone over whatever was observed, so a calibration taken on a loaded
  box sets a loose bound for that row until re-observed. Stated, and it errs toward not killing.
- testing — the runner's self-test gains arms for the refusal-without-evidence, the calibrate mode
  grading nothing, and the bound derived from a staged evidence row; each observed RED first.
- migration — the carriers move from `--serial` to `--pooled` as the unit's last commit, reversible
  by one line each.
- user docs — the runner's `--help` names `--calibrate` and the kit runner's names the flip.

## 6. Acceptance criteria

- **AC1** — When a row has a pooled reading in `ceiling-evidence.txt` under the current condition
  token, `run-selftests.sh --pooled` bounds it at that reading plus `ceiling-margin.txt`'s headroom,
  and prints the reading and token it used.
  Red when: the bound is the serial budget times any factor, which is the refused shape.
- **AC2** — When a row has NO pooled reading, `run-selftests.sh --pooled` REFUSES naming the row and
  `--calibrate`, and executes no suite.
  Red when: it runs the row under a fallback bound, which is a factor wearing a refusal's name.
- **AC3** — When `run-selftests.sh --pooled --calibrate` runs over rows with no evidence, each is
  bounded by the profile wall only, no `OVER BUDGET` and no `TIMEOUT` verdict is printed, each
  reading is appended to `ceiling-evidence.txt` with its condition token, and the summary says
  `calibrated <n> row(s), graded none`.
  `cost:` one pooled pass of the eight shard rows at the wall bound, which is unit 3's AC4 run.
  Red when: a calibration prints a verdict, or a reading lands without its token.
- **AC4** — When `run-selftests.sh --rank` runs after calibration, it exits 0 and no `pooled@`
  token appears in `selftest-budgets.txt`.
  Red when: `--rank` refuses, which means a pooled reading leaked into the budget file.
- **AC5** — When the four carriers are read as text after the flip commit, each names `--pooled`
  beside `run-unattended-gates.sh`, and `bash tools/unattended/run-unattended-gates.sh --pooled`
  completes GREEN over the real rows with the longest row inside its evidence bound.
  `cost:` one real pooled pass.
  Red when: any carrier still names `--serial`, or the real pass kills a row.
- **AC6** — When `bash tools/unattended/run-unattended-gates.sh --selftests --serial` runs after the
  flip, it still issues cost verdicts and is byte-identical to its pre-flip output.
  Red when: the cost pass changed, which would mean the flip touched more than the carriers.

## 7. Gates

`memory hygiene` · `run-selftests self-test` · `every held leg is budgeted, every budget row resolves`
· `install-prefix (shipped surface)` · `charter size` · `kickoff-manifest ratchet` · `ceiling evidence`

New arm: `tools/run-gates/run-selftests.test.sh` · the no-evidence refusal, the calibrate mode grading
nothing, and a bound derived from a staged evidence row, each observed RED then unstaged · floor to
move: the suite's own, up by the arms added.

## 8. Open questions

- **F1 · Does the evidence file take a per-row condition token, or one per run?** Per row, because
  the bar already writes per-leg rows and a shard row is one leg. RESOLVED (agent, 2026-09-13,
  delegated): per row, keyed by name and token; `derive-ceilings.py`'s reader is the seam.
- **F2 · What if unit 3's AC4 measurement misses 20 minutes?** Then the flip still happens if the
  bound is sound — the goal is the owner's target and the flip is about correctness, not speed — and
  the miss is recorded against the host's spawn path per `TOOL-aBatchedArm-4` §4. RESOLVED (agent,
  2026-09-13, delegated): the flip is gated on the bound, not on the 20 minutes.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft, from `TOOL-aBatchedArm-4`'s three audit rounds, which
  specified this unit's shape while refusing it inside that one: the evidence-derived bound (r1 B5),
  the flip landed dark and owned here (r2 B1), and the declared bootstrap. Authored now rather than
  after unit 3 because memory hygiene check 14 reds on a cited id with no spec, and the id was cited
  at `9b00bc7b`.

## 10. Reuse audit

- **The seam is `tools/run-gates/derive-ceilings.py`** and the file it writes,
  `tools/run-gates/ceiling-evidence.txt`, with the headroom rule in `ceiling-margin.txt` — verified at
  source: worst-observed, monotone, `max(floor, fraction x max)`, refusing with no evidence. S1 reads
  that file from the runner's pooled path rather than inventing a second store. The condition token
  `pooled@<outer>x<inner>` is the runner's own at `run-selftests.sh:525`. The `--rank` refusal of
  `pooled@` at `:134` and `:172` is REUSED by keeping pooled readings OUT of the budget file. The
  reuse probe was run —
  `python tools/codebase-map/reuse_lookup.py "derive a pooled hang bound from observed readings under a condition token with monotone evidence and declared headroom"`
  — and returned `read_text`, `read` and `derive_scope`, none of which is this seam; it reports
  `unscanned layers: .sh` and `derive-ceilings.py` is Python it did not rank, so its result is not
  evidence either way. The seam was found by reading `derive-ceilings.py` and the two files beside
  it.
- **The retrieval arguments, verbatim:**
  `python tools/memory-recall/query.py "why does the self-test runner run suites serially by default and pool only under sweep, and what was measured about cost attribution under contention" --terms "run-selftests OUTER pool sweep serial budget contention dilation attribution width verdict withheld mode declared"`.
  Run for unit 4; it surfaced `TOOL-dRetiredFork-40`, `TOOL-aPooledSweep-2` and the full-sweep record
  this unit's §4 rests on.
