# TOOL-aScouredKit-4 — a shrink-only list seeded empty stops being a permanent offender

**Status:** OPEN · rev-2 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make the `shrink_only_lists_not_shrinking` drift signal able to report zero, so its own declared
tolerance is a target rather than a permanently-red decoration.

## 2. Scope (IN)

- S1. `tools/drift-audit/drift_report.py` — the offender test EXCLUDES a list seeded empty and
  still empty, and keeps `shrunk_by <= 0` for every other row.
- S2. A list seeded EMPTY and still empty is reported separately from a list that GREW. The two are
  different facts and the signal currently prints one token for both.
- S3. The failing case is OBSERVED before the change lands: a shrink-only list staged with a row
  ADDED must still select as an offender. Recorded in §9.

## 3. Non-goals (OUT)

- Promoting the signal to `gateable`. That is an owner decision; this only removes the reason it
  could never be promoted.
- Draining the two REAL offenders the signal reports. Those are the signal working.

## 4. Design

`shrunk_by = seed - now`. For a list seeded at zero, `now` cannot fall below `seed`, so `shrunk_by`
is pinned at 0 and a `<= 0` offender test marks it forever. `memory/project/corpus-path-unresolved.txt`
is exactly that list: seeded empty, and its own header says empty is the SUCCESS state. The signal
therefore reports 3 of 5 out of tolerance where 2 are real, and can never reach the 0 it declares.

This is the vacuous-selector family inverted: not a check that cannot fire, but a check that cannot
STOP firing. Both make the number uninformative, and this one additionally blocks its own promotion.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A, one comparison.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — the empty-seed case is the state this unit adds.
- observability — the signal's own report line is the observation.
- risks — loosening `<=` to `<` could hide a list that grew. It cannot: growth makes `shrunk_by`
  negative, which is why S3 stages that exact case before the change.
- testing + left-shift gates — `python tools/drift-audit/selftest.py`.
- migration / rollback — N/A, one predicate. user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py` runs on this tree, the
  `shrink_only_lists_not_shrinking` row reports 2 offenders and
  `memory/project/corpus-path-unresolved.txt` is not among them.
- **AC2** — When a shrink-only list named in `.drift-audit.conf`'s `SHRINK_ONLY_LISTS` is staged
  with a row ADDED, `python tools/drift-audit/drift_report.py` still selects it as an offender — the
  failing case, observed and recorded in §9 before the fix landed.
- **AC3** — When `python tools/drift-audit/selftest.py` runs, it is green.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · the full bar at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.
- rev-2 · 2026-08-30 · S1 rewritten. It restated the wave-1 report's proposed `shrunk_by < 0`,
  which is WRONG: it drops the seed>0, now==seed case, the one case this signal exists for, and no
  row in this corpus exercises that case so the loss would have been invisible. Caught by the M6
  bug-class checklist under `amendment-leaves-its-other-half-standing` after the code was already
  written correctly — the spec was the half left standing. The code carries the same reasoning.

## 10. Reuse audit

No new seam: this edits one predicate inside an existing signal in `tools/drift-audit/drift_report.py`,
which already owns the seed/now derivation and the reporting row. The build's reuse probe is recorded
in `TOOL-aScouredKit-1` §10 and is not re-composed.
