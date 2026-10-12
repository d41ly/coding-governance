# TOOL-aHeardState-3 — the format-guard self-test leg gets its subject pin and its budget row

**Status:** CLOSED · rev-1 · 2026-10-13 · node a · Tier-1 · base 2f9dfaf0 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-TOOL-aHeardState-1-runlog-dd96ba88.md](../build/2026-10-12-build-TOOL-aHeardState-1-runlog-dd96ba88.md) | journal | TOOL-aHeardState-1 TOOL-aHeardState-2 TOOL-aHeardState-4 TOOL-aHeardState-5 TOOL-aHeardState-6 TOOL-aHeardState-7 TOOL-aHeardState-8 |
| [2026-10-13-build-TOOL-aHeardState-1-2-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aHeardState-1-2-acceptance-ledger.md) | journal | TOOL-aHeardState-1 TOOL-aHeardState-2 TOOL-aHeardState-4 TOOL-aHeardState-5 TOOL-aHeardState-6 TOOL-aHeardState-7 TOOL-aHeardState-8 |

<!-- /gen:spec-records -->

## 1. Goal

Closing review round 1 id 8 (HIGH): the new held leg has no row in `tools/govkit/subject-pins.tsv` and
none in `tools/run-gates/selftest-budgets.txt`, so `govkit selfcheck` and `run-selftests.sh --check`
red on every bar. Register the leg in both.

## 2. Scope (IN)

- **S1** — `python tools/govkit/govkit.py selfcheck --write` regenerates `tools/govkit/subject-pins.tsv`
  with a `format-guard self-test` row. Observed by AC1.
- **S2** — a `format-guard self-test` row in `tools/run-gates/selftest-budgets.txt` beside
  scratch-guard's, marked ESTIMATE until VERIFYING's reading re-declares it. Observed by AC2.

## 3. Non-goals (OUT)

- Measuring the suite inside this pass: a pass runs no suite, so the budget starts as an estimate.

### Edges

none

## 4. Design

Two registry rows, one regenerated and one authored, each in the shape scratch-guard's leg already
has in the same file.

### Files touched (estimate)

- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/selftest-budgets.txt`

## 5. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs, it reports no missing subject pin for
  `format-guard self-test`. Red when: the pin row is absent and selfcheck names the leg.
- **AC2** — When `tools/run-gates/selftest-budgets.txt` is read, it holds a `format-guard self-test`
  row beside scratch-guard's. Red when: the row is absent, which the held-leg budget check names.

## 6. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted from closing review round 1 id 8.
