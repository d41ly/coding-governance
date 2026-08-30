# TOOL-aScouredKit-8 — drift-audit stops printing a cardinality its own source retracted

**Status:** OPEN · rev-1 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 |

<!-- /gen:spec-records -->

## 1. Goal

Drop the cardinality claim from the `unarmed-branches.txt` gloss in
`tools/drift-audit/drift_signals.py`, which tells an operator the file is empty while the signal
printed beside it reports three rows.

## 2. Scope (IN)

- S1. The gloss at `tools/drift-audit/drift_signals.py:80` loses its "empty today and meant to stay
  so" claim. The count stays where it is derived and printed.
- S2. Every other gloss in that table is read in the same pass, and any sibling asserting a
  cardinality its own row derives is corrected too. The class, not the instance.

## 3. Non-goals (OUT)

- Arming the three unarmed branches the file lists. That is that file's subject, not this unit's.
- Changing what any signal MEASURES or the value it reports.

## 4. Design

The gloss is the surviving copy of a claim the source already retracted: the waiver file's own
header was corrected for this exact class, and the gloss was not. This is the charter's rule that a
value stated in prose beside the source that OWNS it rots — occurring inside the tooling that
polices the class, which is why the audit graded it worth fixing despite the small blast radius.

Blast radius is genuinely small: the gloss is a `what` label in `--json` detail rows and no verdict,
count or gate leg reads it. It is fixed because it is cheap and because an operator reading the JSON
is told the opposite of the truth.

## 5. Production-readiness checklist

- security — N/A. perf / scale — N/A. a11y — N/A. i18n — N/A.
- error / empty / loading states — N/A.
- observability — this IS the observability fix.
- risks — none identified; no reader consumes the string.
- testing + left-shift gates — `python tools/drift-audit/selftest.py`.
- migration / rollback — N/A. user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs, no `what` gloss states a
  cardinality contradicted by its own row's derived value, checked by reading every gloss in
  `tools/drift-audit/drift_signals.py` against the live row beside it.
- **AC2** — When `python tools/drift-audit/selftest.py` runs, it is green.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · the full bar at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.

## 10. Reuse audit

No new seam: one string in an existing declaration table that already owns the signal's reporting.
The build's reuse probe is recorded in `TOOL-aScouredKit-1` §10 and is not re-composed.
