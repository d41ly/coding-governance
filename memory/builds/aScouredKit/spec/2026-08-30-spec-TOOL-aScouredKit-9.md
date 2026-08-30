# TOOL-aScouredKit-9 — drift-audit-state.js gains its sibling's run-integrity fields

**Status:** OPEN · rev-1 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 |

<!-- /gen:spec-records -->

## 1. Goal

Give `tools/workflows/drift-audit-state.js` the aggregate downgrade counter on its RUN INTEGRITY log
line and `severityCorrections` in its return value, both of which its sibling harness already has,
so the two report their own degradation identically.

## 2. Scope (IN)

- S1. The three stations `tools/workflows/drift-audit-code.js` carries at `:377`, `:415` and `:467`,
  ported to the matching stations in the state harness.
- S2. The kit version marker moves in EVERY carrier `tools/check-kit-versions.sh` asserts for this
  kit, not only the three that a remedy message names.

## 3. Non-goals (OUT)

- Any change to what either harness FINDS or how it verifies. This is reporting parity only.
- `tools/workflows/tier2-review.js`, whose verdict vocabulary is binary rather than ternary, so the
  counter has no meaning there.

## 4. Design

The state harness serializes `judged` wholesale into its synthesis prompt, so the per-finding
correction already reaches the writer — the earlier claim that it "never reads it" was refuted. What
is missing is the AGGREGATE an operator sees without opening the report, which is exactly what a run
integrity line is for. One counter short of parity, not a missing block.

The version-marker population is the risk, not the edit: this repo has already spent two builds on a
remedy message naming three carriers where the checker wants five, and that gap is tracked as
`TOOL-aSiftedFork-5` and `TOOL-aBoundedVerdict-29`. S2 exists so this unit does not become a third
instance.

## 5. Production-readiness checklist

- security — N/A. perf / scale — N/A. a11y — N/A. i18n — N/A.
- error / empty / loading states — a run with zero corrections prints a zero rather than omitting
  the line, which is the whole point of a run-integrity report.
- observability — this IS the observability fix.
- risks — the version-marker carriers; S2 addresses it and AC2 proves it.
- testing + left-shift gates — `node tools/workflows/check-workflow-syntax.js` ·
  `bash tools/workflows/check-verifier-fanout.sh` · `bash tools/check-kit-versions.sh`.
- migration / rollback — N/A. user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `grep -c severityCorrections tools/workflows/drift-audit-state.js` runs, it is
  non-zero, and that file's RUN INTEGRITY log line names a downgrade count.
- **AC2** — When `bash tools/check-kit-versions.sh` runs, it is green — the marker moved in every
  carrier that checker asserts.
- **AC3** — When `bash tools/workflows/check-verifier-fanout.sh` and
  `node tools/workflows/check-workflow-syntax.js` run, both are clean.

## 7. Gates

`workflow syntax` · `verifier fan-out` · `kit version markers` · the full bar at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.

## 10. Reuse audit

The seam IS `tools/workflows/drift-audit-code.js` — this ports three of its lines rather than
inventing a second reporting shape, and the two files are deliberate siblings under one kit id. The
build's reuse probe is recorded in `TOOL-aScouredKit-1` §10 and is not re-composed.
