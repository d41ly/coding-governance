# TOOL-aSparedSpawn-18 — the width A/B instrument counts only executed verdicts and fails on a red bar

**Status:** OPEN · rev-1 · 2026-10-12 · node a · Tier-1 · base 8444f597 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close HIGH finding 6 (H2) of the round-1 closing review
(`memory/builds/aSparedSpawn/reviews/2026-10-12-review-TOOL-aSparedSpawn-1-15-closing-diff-round1.md`).
The width A/B instrument runs held self-test legs without asking for them, so every arm prints
`GATE held` lines, the bar refuses with exit 1, and the artifact still reads `yes`. A width picked
from those rows would be picked from noise.

## 2. Scope (IN)

- **S1** — `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh` sets
  `GATE_SELFTESTS=1` in each arm's environment (`:50`), so its held legs execute. Observed by AC1.
- **S2** — The positive artifact (`:59`) counts only executed verdict lines, `^GATE (ok|FAIL) `.
  That excludes every non-executing verb the runner prints, `held`, `skip` and `reuse`, and the
  `retry` interim. It requires exactly one such line per manifest leg. Observed by AC1.
- **S3** — An arm whose bar exits non-zero records `artifact` as `no`, and the rows file gains an
  `rc` column carrying the bar's exit, so a red arm is never picked as a best wall. Observed by AC1.
- **S4** — The script's header states the instrument's rule: an arm is a figure only when it executed
  one verdict per leg and its bar exited 0. Observed by AC2.

## 3. Non-goals (OUT)

- Re-running the width A/B. The owner runs it, or authorises the main loop to, before any width
  knob moves.
- A gate over every A/B instrument in this repository, the review's documented-check left-shift,
  which is carried to the build's exit as an ask.
- Running any suite or the bar inside the build pass.

## 4. Design

Three edits to one record script. The arm's `env` gains the self-test knob beside `GATE_FULL=1`. The
bar's exit is captured where line 51 discards it. `gl` counts `^GATE (ok|FAIL) ` lines, and `art`
reads `yes` only when `gl` equals the manifest's leg count and the exit is 0.

### Files touched (estimate)

- `memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh`

## 5. Production-readiness checklist

- security: N/A — a record script run by hand; no input, write path or authority moves.
- perf / scale: an arm now executes its legs, which is the cost the instrument always claimed to measure.
- error / empty / loading states: a red or empty arm reads `no` and is never picked.
- observability: the `rc` column records each arm's bar exit beside its counts.
- risks: none beyond the A/B's own; its rows were never used to move a knob.
- testing: the fixture run in AC1, observed red at f479ba42's script first.
- migration: none; no rows file was ever committed from the broken instrument.
- user docs: N/A — the script's header is its documentation.

## 6. Acceptance criteria

- **AC1** — When `2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh` runs with `AB_LOAD=0` on a frozen
  clone of the tree and a one-leg manifest whose leg sits in the `selftests` chunk, every row's
  `artifact` reads `yes` for a leg exiting 0 and `no` for a leg exiting 1. Red when: the exit-1 leg
  reads `yes`, which it does at f479ba42 because the `GATE held` lines are counted.
  cost: six one-leg bars and one calibration per manifest, about two minutes each on node a.
- **AC2** — When `grep -n 'one verdict per leg' memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh`
  runs, it prints the header's rule. Red when: the header still certifies an arm by any `GATE` line.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft, from `TOOL-aSparedSpawn-16` rev-1's S8 and AC8, promoted to a
  unit of its own by the converged closing review under the owner rulings of 2026-10-04, with the
  review's left-shift on the artifact pattern and the bar's exit.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "count executed verdict lines in a bar's output"` ranks generic
`counts` and `check_line` helpers from other kits and no verdict reader. The one reader of these
lines, `parse_verdicts` in `tools/run-gates/profile_bar.py`, is Python; no existing seam fits a bash
record script, whose one `grep -c` is the whole count.

Recall terms used: width A/B GATE_JOBS held selftests artifact executed verdict ab-arm-never-did-the-work
calibrate-width CALIBRATE_THETA frozen clone positive artifact
