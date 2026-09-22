# TOOL-aScouredKit-32 — an unresolvable probe answers for itself, not for its siblings

**Status:** CLOSED · rev-1 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling+deployer

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md) | spec-audit | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 TOOL-aScouredKit-30 TOOL-aScouredKit-31 |

<!-- /gen:spec-records -->

## 1. Goal

Stop `exempt_leg`'s fail-closed branch from vetoing exemption routes it knows nothing about, and
delete the dead fallback that preserved the hardcoded context the same function condemns.

## 2. Scope (IN)

- S1. The unresolved-token branch `continue`s to the next hole instead of returning from the whole
  function, so a later hole and the independent `red_after_land` window are still evaluated.
- S2. `deploy` becomes a REQUIRED parameter. The `None` default and its hardcoded
  `tools/` + `memory` context are removed.
- S3. The message says what it now means: this probe granted nothing, other routes are still checked.

## 3. Non-goals (OUT)

- The fail-closed DIRECTION. Refusing to grant an exemption from a probe that never ran is correct
  and is round 2's fix; only its SCOPE was wrong.
- `red_after_land`'s own window semantics, which this unit only stops short-circuiting.

## 4. Design

Round 2 made an unresolvable probe grant no exemption, which was right, and implemented it as
`return False` — exiting the whole function. That is an answer about every OTHER hole of that kit
and about `red_after_land`, neither of which the unresolved token says anything about. One probe's
inability to answer became an answer for all of them, in the restrictive direction, and it is
reachable through the very descriptor the previous unit had just edited.

S2 is smaller and of the same family. The `deploy is not None` fallback rebuilt exactly the
hardcoded four-key context the comment three lines above calls out as the defect being fixed, and no
caller ever passed `None` — so it was a dead branch whose only effect would have been to restore the
bug if anyone reached it. A parameter that must be supplied says so in its signature.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A; a `continue` where a `return` was.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — the unresolvable-probe case is the state, and it now reports and
  proceeds rather than reporting and stopping.
- observability — the message text, corrected by S3.
- risks — proceeding past a failed probe could grant an exemption a stricter reading would withhold.
  It cannot: the remaining routes each have their own evidence, and a hole that CAN run still
  decides on its own result.
- testing + left-shift gates — `python tools/govkit/selftest.py`.
- migration / rollback — no artifact changes.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `exempt_leg` is read in `tools/govkit/govkit.py`, its unresolved-token branch ends
  in `continue` and the function has no `deploy: dict | None = None` default.
- **AC2** — When `python tools/govkit/govkit.py selfcheck` and
  `python tools/govkit/govkit.py apply` run against the fixtures in the suite, no call passes
  `deploy=None` — proven by the signature change: a missing argument is a `TypeError` at call time,
  not a silent fallback.
- **AC3** — When `python tools/govkit/selftest.py` runs, all arms hold.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · the full bar at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft. PROMOTED from the closing review's round 3 after the loop went
  NON-CONVERGENT.

## 10. Reuse audit

No new seam: this narrows a branch and removes a parameter default inside an existing function.
`target_context` is the shared resolver it now always uses, which is the reuse the previous unit was
reaching for and only half took. Probe recorded in `TOOL-aScouredKit-1` §10.
