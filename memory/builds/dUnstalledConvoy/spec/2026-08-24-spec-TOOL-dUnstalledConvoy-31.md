# TOOL-dUnstalledConvoy-31 — an on-demand skip reaches the run total, so a partial bar cannot print a whole one

**Status:** CLOSED · rev-1 · 2026-08-24 · node d · Tier-1 · base b164a296 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dUnstalledConvoy-26-2-acceptance-ledger.md](../build/2026-08-24-build-TOOL-dUnstalledConvoy-26-2-acceptance-ledger.md) | journal | TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-27 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-29 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-32 |
| [2026-08-24-build-TOOL-dUnstalledConvoy-31-1-red-first.md](../build/2026-08-24-build-TOOL-dUnstalledConvoy-31-1-red-first.md) | journal | — |
| [2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md](../reviews/2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md) | journal | TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-27 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-29 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-32 TOOL-dUnstalledConvoy-33 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dUnstalledConvoy-26` gives the on-demand skip its own counter so it stays out of `skips`, which
the `gate-full-green` stamp conjoins. That counter never reaches the run total, so a bar that skipped
the kit-subject legs still prints `gates GREEN — 85/85 legs passed` and records `ran 85`.

## 2. Scope (IN)

- **S1 — the total subtracts the on-demand skips**, so the printed count is the count that ran.
- **S2 — the summary NAMES the skipped population** alongside the total, so the difference is legible
  rather than inferred from a smaller number.
- **S3 — the recorded `ran` figure agrees with the printed one.**
- **S4 — every change lands with its arm, observed failing first.**

## 3. Non-goals (OUT)

- The counter itself, the verb, or the stamp field — the parent unit.
- The chunk close line — `TOOL-dUnstalledConvoy-32`.

## 4. Design

A total that counts legs which did not run is the green-by-absence class stated as arithmetic. The
figure a reader trusts most on a bar is the one this defect falsifies.

S2 is what keeps S1 from being a smaller lie: `82/82` with no explanation reads as a bar that shrank
for unknown reasons. The skipped population is named in the same line.

## 5. Production-readiness checklist

- **security** — the push boundary and every human reader take the total at face value.
- **perf/scale** — arithmetic.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — a run where every leg is skipped prints zero ran and says so.
- **observability** — this unit IS an observability fix.
- **testing/gates** — `run-gates`' own self-tests, plus the full bar.
- **migration/rollback** — revert.
- **help/ docs** — none; the summary is self-describing.

## 6. Acceptance criteria

- **AC1** — a bar with the switch off prints a total equal to the legs that ran, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC2** — the summary names the skipped population, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC3** — the recorded `ran` figure equals the printed total, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC4** — with the switch on, the total is the whole manifest, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC5** — every arm was observed RED before its fix, observed in
  `2026-08-24-build-TOOL-dUnstalledConvoy-31-1-red-first.md`.
- **AC6** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. Tier 1.

## 8. Open questions

- **F1 — subtract, or print both figures?** RESOLVED (agent, 2026-08-24): subtract AND name the
  skipped set. The total must be true on its own, because it is the figure that gets quoted.

## 9. Revision log

- rev-1 · 2026-08-24 · promoted from round 2's NON-CONVERGENT spec audit.

## 10. Reuse audit

The runner already tracks `fails`, `skips` and `reuses` and already prints a summary line; this is
arithmetic over counters that exist.
