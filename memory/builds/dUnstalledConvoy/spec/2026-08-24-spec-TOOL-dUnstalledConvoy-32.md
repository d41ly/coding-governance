# TOOL-dUnstalledConvoy-32 — a fully skipped chunk cannot close green, which is the shape its own comment refuses

**Status:** CLOSED · rev-1 · 2026-08-24 · node d · Tier-1 · base b164a296 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dUnstalledConvoy-26-2-acceptance-ledger.md](../build/2026-08-24-build-TOOL-dUnstalledConvoy-26-2-acceptance-ledger.md) | journal | TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-27 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-29 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-31 |
| [2026-08-24-build-TOOL-dUnstalledConvoy-32-1-red-first.md](../build/2026-08-24-build-TOOL-dUnstalledConvoy-32-1-red-first.md) | journal | — |
| [2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md](../reviews/2026-08-24-review-TOOL-dUnstalledConvoy-26-closing-diff.md) | journal | TOOL-dUnstalledConvoy-26 TOOL-dUnstalledConvoy-27 TOOL-dUnstalledConvoy-28 TOOL-dUnstalledConvoy-29 TOOL-dUnstalledConvoy-30 TOOL-dUnstalledConvoy-31 TOOL-dUnstalledConvoy-33 |

<!-- /gen:spec-records -->

## 1. Goal

The on-demand skip never reaches `chunk_close`, so the chunk holding the kit-subject legs closes
`green (0 ran, 0 failed, 0 skipped, 0 reused)`. That is green-by-absence — a chunk reporting success
over nothing — and the comment three lines above that code refuses it by name for the guard case.

## 2. Scope (IN)

- **S1 — the on-demand skip reaches `chunk_close`**, so a chunk's counts describe what happened in it.
- **S2 — a chunk whose every leg was skipped closes SKIPPED, never green**, matching the existing rule
  for a chunk whose every leg was guard-skipped.
- **S3 — every change lands with its arm, observed failing first.**

## 3. Non-goals (OUT)

- The run total — `TOOL-dUnstalledConvoy-31`.
- The counter, the verb, or the stamp — the parent unit.
- Chunk membership or ordering.

## 4. Design

The runner already has the right rule and already states it: a chunk whose every leg skipped reports
skipped rather than green. The defect is that a new skip kind does not reach the code that applies it,
so the rule is correct and unreachable — which is worse than absent, because the comment asserts it.

## 5. Production-readiness checklist

- **security** — a green chunk is read as coverage.
- **perf/scale** — none.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — this IS the empty case.
- **observability** — the chunk line is the per-area verdict a reader scans first.
- **testing/gates** — `run-gates`' own self-tests, plus the full bar.
- **migration/rollback** — revert.
- **help/ docs** — none.

## 6. Acceptance criteria

- **AC1** — a chunk whose every leg is on-demand-skipped closes SKIPPED with its counts, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC2** — a chunk with a mix closes green and its counts include the skips, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC3** — the arm was observed RED before the fix, observed in
  `2026-08-24-build-TOOL-dUnstalledConvoy-32-1-red-first.md`.
- **AC4** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. Tier 1.

## 8. Open questions

- **F1 — reuse the guard-skip chunk rule, or add one?** RESOLVED (agent, 2026-08-24): reuse. The rule
  is right and already written; only its reachability is broken.

## 9. Revision log

- rev-1 · 2026-08-24 · promoted from round 2's NON-CONVERGENT spec audit.

## 10. Reuse audit

`chunk_close` already distinguishes a fully skipped chunk from a green one. This makes the new skip
kind reach it.
