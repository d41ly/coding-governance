# TOOL-aUnblockedFleet-4 — the arms, each with its failing case observed

**Status:** SPECCED · rev-1 · 2026-08-31 · node a · Tier-1 · base 117de044 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Units 1 and 2 each convert a refusal into a report. A report is the easiest thing in this kit to
build wrong, because a report that never fires and a report with nothing to say are the same output.
Arm both halves so a regression is loud, and observe each arm's failing case before it lands.

## 2. Scope (IN)

- **S1** — `tools/unattended/unattended.test.sh`: the existing check-5 arm is REWRITTEN, not deleted.
  Its fixture already builds two tracked non-terminal records (`tRun` and `tTwo`); it keeps that
  fixture and swaps its assertion from the refusal text to the announcement text, plus a `same` arm
  asserting `--preflight` now CREATES the run-state file where it previously wrote nothing.
- **S2** — a new arm in the same file asserting SILENCE at one live run: a `miss` on the announcement
  text over the ordinary single-run fixture. This is the green control, and without it S1 passes
  over a driver that announces unconditionally.
- **S3** — `tools/unattended/check-unattended.test.sh`: the check-7 RED arm becomes a report arm
  (`hit` on the report text, and the leg exits 0), keeping its existing GREEN control that a
  TERMINAL second record produces no report.
- **S4** — a `miss` arm asserting an EXCLUDED `LANDING` record does not appear in the report. The
  exclusion and the report are two populations and a record must be in exactly one; without this arm
  a report that ignored the exclusion would pass every other arm.
- **S5** — every arm's FAILING CASE IS OBSERVED before the unit closes, per template §7: stage the
  break, confirm RED, unstage. The observation is recorded in this build's acceptance ledger, naming
  what was broken and what text the suite printed.

## 3. Non-goals (OUT)

- New arms for leg check 4, the review-round loop, the halt-code loop or the population guard. All
  four are untouched by units 1 and 2 and all four already have arms.
- Raising or lowering the `check-arms` armed-branch floors. The rewrites are one-for-one on branch
  count, so the pins should hold unchanged — if one moves, that is a finding, not a pin to edit.
- A fixture proving two runs can land concurrently end to end. That needs two clones and a real
  push, it would be the only test in this kit doing so, and the lander-marker race it would exercise
  is explicitly out of scope for this build.

## 4. Design

The `staged-break-substitutes-a-synthetic-value` gotcha binds S5 directly: an arm proved by replacing
the shipped predicate with a simpler one proves it for the simpler one. So each break is made in the
SHIPPED source — delete the announcement's printf, or restore the `fail` — never in a copy shaped to
be easy to break.

The `fixture-passes-by-finding-nothing` gotcha binds S2 and S4: both are `miss` arms, and a `miss`
over a fixture that never had the thing anyway proves nothing. Each is therefore paired with the
`hit` arm over the fixture that DOES have it, which is what makes the pair discriminating.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/unattended.test.sh` | check-5 arm rewritten; silence arm added |
| `tools/unattended/check-unattended.test.sh` | check-7 arm rewritten; exclusion-not-reported arm added |

## 5. Production-readiness checklist

- security — N/A. perf / scale — two arms in suites that already build their fixtures; negligible.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — S2 and S4 ARE the empty cases; that is the unit's point.
- observability — a failing arm prints what it got, which this harness's `hit` already does.
- risks — the arms are the mitigation for units 1 and 2's risks; this unit's own risk is a `miss`
  arm that passes vacuously, answered by S2/S4's pairing rule above.
- testing + left-shift gates — this unit IS the left-shift for both confirmed changes.
- migration / rollback — revert. user docs — N/A, test files.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.test.sh` runs, it prints `PASS` and exits 0 with
  the rewritten check-5 arm and the new silence arm included in its assertion count.
- **AC2** — When `bash tools/unattended/check-unattended.test.sh` runs, it prints `PASS` and exits 0
  with the rewritten check-7 arm and the new exclusion arm included.
- **AC3** — When the announcement `printf` is deleted from `check_single_live()` and
  `unattended.test.sh` is re-run, it FAILS naming the missing announcement text. Observed and
  recorded, then unstaged.
- **AC4** — When check 7's report is deleted from `check-unattended.sh` and
  `check-unattended.test.sh` is re-run, it FAILS naming the missing report text. Observed and
  recorded, then unstaged.
- **AC5** — When the announcement is made UNCONDITIONAL (printed even at zero concurrent runs) and
  `unattended.test.sh` is re-run, the S2 silence arm FAILS. This is the arm that proves S2 is not
  vacuous, and it is the one most likely to be silently useless. Observed, recorded, unstaged.
- **AC6** — When `python tools/memory-tree/check-arms.py` runs as part of the bar, both suites still
  meet their armed-branch pins with no pin edited.

## 7. Gates

`bash tools/run-gates/run-gates.sh`. Binding: `unattended kit gate`, the `check-arms` legs for both
suites. The kit's own `*.test.sh` legs are NOT on the bar by owner ruling (2026-08-23), so they run
on demand via `bash tools/unattended/run-unattended-gates.sh`, and this unit runs them explicitly.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-08-31 · authored under the aUnblockedFleet mandate.

## 10. Reuse audit

The seams are the two existing suites and their `hit` / `miss` / `same` helpers, reused verbatim —
no new harness, no new fixture builder. Both fixtures needed for the two-live-record state already
exist: `unattended.test.sh`'s check-5 arm builds `tTwo`, and `check-unattended.test.sh`'s check-7 arm
builds `tTwo` with a witness and base. This unit changes assertions, not scaffolding.

Recall terms are unit 1's. The gotcha records that bind this unit are
`memory/gotchas/fixture-passes-by-finding-nothing.md` and
`memory/gotchas/staged-break-substitutes-a-synthetic-value.md`, both selected by
`gotchas.py --for-paths` over the four files this build touches, and both cited in §4.

**Verified at writing time**: both suites' fixtures build the second record as described, and both
existing arms assert the exact failure strings units 1 and 2 remove.
