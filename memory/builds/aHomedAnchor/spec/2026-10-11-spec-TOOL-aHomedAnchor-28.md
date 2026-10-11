# TOOL-aHomedAnchor-28 — the unattended-build self-test's budget is re-declared from readings

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 6 · closes TOOL-aHomedAnchor-21

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The held job killed the unattended-build self-test at its 180 s bound after 742 passing assertions,
so the suite was cut, not failed. Its 60 s budget was sized from an estimate when the suite carried
103 `run_wf` sites. It now runs 853 assertions, which no 60 s budget covers on any machine this repo
has measured.

## 2. Scope (IN)

- S1. The `unattended-build self-test` row of `tools/run-gates/selftest-budgets.txt` declares 500 s:
  the 332 s quiet reading `tools/run-gates/ceiling-evidence.txt` records, times the file's own 1.5.
  Its reason names that reading, the held job's 742 assertions in 180 s, and this unit's 1853 s
  contended reading on node a. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

Making the suite faster. That is a separate cost question, and the budget file names re-declaring
with a reason as the other legal answer.

### Edges

none

## 4. Design

The brief is `memory/builds/aHomedAnchor/prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md`.
The held job's bound is the budget plus `max(floor, fraction x budget)`, read by `held-plan`, so a
500 s budget bounds a held run well above the roughly 210 s a full CI run needs at the observed rate.

### Files touched (estimate)

- `tools/run-gates/selftest-budgets.txt`

## 6. Acceptance criteria

- **AC1** — When the budgeted-population leg reads `tools/run-gates/selftest-budgets.txt`, it passes
  with the row at 500. Red when: the row is malformed or the population check refuses it.
- **AC2** — When the suite runs alone on node a, it prints `PASS (853 assertions)`.
  Red when: an assertion fails, which a budget change cannot cause.

## 7. Gates

`every held leg is budgeted, every budget row resolves`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

No existing seam fits beyond the budget file's own calibration rule, applied to its own evidence
file. Recall terms used: `--terms "selftest budget held bound unattended-build run_wf calibrated reading ceiling-evidence cost verdict"`.
