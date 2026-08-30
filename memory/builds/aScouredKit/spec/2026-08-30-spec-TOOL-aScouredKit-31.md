# TOOL-aScouredKit-31 — the container guard reaches every caller, and two arms stop lying

**Status:** CLOSED · rev-2 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling+deployer

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md) | spec-audit | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 TOOL-aScouredKit-30 TOOL-aScouredKit-32 |

<!-- /gen:spec-records -->

## 1. Goal

Make `cmd_adopt` route its target-authored kit list through the same grader `plan` and `apply` use,
and make the two selftest arms this build added actually observe what they claim.

## 2. Scope (IN)

- S1. `cmd_adopt` passes `deploy` and stops pre-coercing the list with `list(...)`, so the grader
  sees the raw value.
- S2. The `a later apply RECOVERS` arm stops restoring the receipt's `emitted` by hand. It undoes
  the TAMPER only, in whatever rows the production code left.
- S3. A new arm covers the `kind != "manifest"` carry-forward, which had none anywhere.
- S4. Each of S2 and S3 is proven DISCRIMINATING by staging the production line away and observing
  the arm fail. Recorded in §9.

## 3. Non-goals (OUT)

- The grader's own text or the shapes it refuses. Round 2 built that and round 3 confirmed it works
  where it runs; only its REACH was wrong.
- Any other vacuous arm in this suite. Two were found and two are fixed; a sweep is its own unit.

## 4. Design

Round 2 hoisted the shape guard above the branch split and round 3 found `cmd_adopt` still bypassing
it: `list(deploy.get("kits") or [])` consumed the value at the call site, before `resolve_selection`
could grade its container. So `kits = 5` and `kits = true` raised a raw `TypeError` — `main` catches
only `Refusal` — and `kits = "memory-tree"`, the likeliest typo of all, was iterated into eleven
single characters and refused as eleven unknown entries. The same defect, surviving one caller over,
twice in a row.

The fix removes the call site's own mode decision entirely. `"default"` plus `deploy` lets the
declared-list branch do the work, which is exactly what `plan` and `apply` already do, so three
callers stop being three implementations.

**S2 is the sharper half.** The recovery arm overwrote the on-disk receipt's `emitted` with the
pre-run rows before re-applying — the very thing the production fix exists to do — so it passed
whether or not the fix was there. Round 3 proved it by staging the break: with `emitted = []`
restored, the suite reported exactly ONE failure, the field arm, while the arm billed as covering
the wedge end to end printed `ok`. An arm that cannot fail is the defect this whole build has been
finding in other people's code.

## 5. Production-readiness checklist

- security — the grader now sees target-authored values on one more path, which is the point; no
  value reaches an argv.
- perf / scale — N/A.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an absent or empty `kits` still falls through to the registry
  default on every caller.
- observability — four bad shapes now produce named refusals instead of tracebacks.
- risks — `cmd_adopt` no longer chooses its own mode, so a future caller adding a mode must not
  reintroduce a per-site decision. Stated in the comment at that call site.
- testing + left-shift gates — `python tools/govkit/selftest.py`, plus the four shapes driven
  through both `plan` and `adopt` by hand.
- migration / rollback — no artifact changes.
- user docs — the refusal text is the operator-facing doc.

## 6. Acceptance criteria

- **AC1** — When `.governance/deploy.toml` declares `kits = 5`, `kits = true`,
  `kits = "memory-tree"` or `kits = [1]`, both `python tools/govkit/govkit.py plan` and
  `python tools/govkit/govkit.py adopt` print a named refusal and neither emits a traceback.
- **AC2** — When the `emitted` carry-forward line in `tools/govkit/govkit.py` is staged away, the
  `a later apply RECOVERS` arm FAILS. Observed and recorded in §9.
- **AC3** — When the `kind != "manifest"` carry-forward line is staged away, the new
  `AC-ordered` arm FAILS. Observed and recorded in §9.
- **AC4** — When `python tools/govkit/selftest.py` runs unmodified, all arms hold.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · the full bar at the push
boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft. PROMOTED from the closing review's round 3 after the loop went
  NON-CONVERGENT at 4 → 3 → 4.
- rev-2 · 2026-08-30 · built, with AC2 and AC3 OBSERVED as separate staged breaks rather than
  assumed. Break 1 replaced the withheld path's carry-forward with `emitted = []`: the suite
  reported 4 failures including `a later apply RECOVERS`, which had printed `ok` under the same
  break before this unit rewrote it — that is AC2, and it is the direct refutation of round 3's
  vacuity finding. Break 2 removed ONLY the `kind != "manifest"` carry-forward: exactly the two
  `AC-ordered` arms failed and every `AC-withheld` arm held, so each arm reacts to its own line.
  Both breaks were restored from a saved copy and the unmodified suite holds 1001 arms.
  ONE HONEST LIMIT: under break 1 the `AC-ordered` arms also failed, because they run after the
  withheld arms and inherit the blanked receipt. That is state dependency between arms, not
  independent discrimination, and break 2 is what settles it — said here because a single
  combined break would have looked like proof and would not have been one.

## 10. Reuse audit

The seam is `resolve_selection`'s own `_graded` helper, added by `TOOL-aScouredKit-13` and hoisted
by round 2's fold; this unit only widens its REACH and writes no new validator. The arm work reuses
the suite's existing `check()` and its throwaway-repo fixtures. Probe recorded in
`TOOL-aScouredKit-1` §10.
