# TOOL-aBoundedVerdict-22 — the promoted blockers: the fold's own defects, specced rather than re-reviewed

**Status:** CLOSED · rev-1 · 2026-08-21 · node c · Tier-2 · base 43a6c13e · streams tooling

## 1. Goal

This unit exists because the convergence predicate this build shipped fired on this build. Recorded
review rounds went 1 blocker then 3; the count did not shrink, so `--review` returned NON-CONVERGENT
and the loop STOPPED. The method's disposition at that exit is not another round and not a park: every
blocker still standing is PROMOTED to a unit, specced at its tier, built and closed. This is that unit.

Promoting is what makes the loop terminate. A promoted blocker is audited as a SPEC, so the build
cannot re-enter the review cycle it just exited — which is the whole reason the exit exists.

## 2. Scope (IN)

- The two blockers round 4 measured RED on the merge bar: a hygiene-engine change of eight
  behaviour-bearing lines with no `KIT_MEMORY_TREE_VERSION` bump, and a review record added without
  regenerating the build index.
- The three highs: `is_published`'s cannot-tell answer gated on presence rather than absence;
  `BUILD-METHOD` teaching a §8 rule both readers withdrew; and the none-form escape my own case
  alignment widened.
- The mediums and lows round 4 confirmed, worked in the same pass.

## 3. Non-goals (OUT)

- A fifth review round. The loop exited; re-reviewing is the behaviour the exit forbids.
- Re-opening the withdrawn per-item §8 walk, or `TOOL-aBoundedVerdict-21`. Both are settled.
- Any change to the convergence predicate itself. It behaved as specified and as F1 predicted.

## 4. Design

The defects are unrelated to each other, so there is no shared mechanism to build — the unit's content
is the fold. What it adds beyond the fixes is the standing left-shift round 4 asked for: the case,
denial and whitespace rows the marker contract lacked, so that reverting either §8 fix can no longer
leave that table green.

The one judgment worth recording: with items present, a §8 opening line no longer votes at all. Only a
conforming mark resolves a section. Measured before landing — twelve older terminal specs would newly
red and all twelve are already exempt by `FORK_MARK_CUTOFF`; zero at or after it.

## 5. Production-readiness checklist

- security — N/A: no new write path, no new surface, no credential or egress change.
- perf / scale — N/A: the readers already walked the section; the change is which predicate decides.
- a11y — N/A: no user-facing surface.
- i18n — N/A: no user-facing strings.
- error / empty / loading states — covered: the cannot-tell answer IS the empty-evidence state, and it
  now reports rather than guessing.
- observability — covered: the inert wall-clock bound announces itself, on stderr rather than sharing
  a channel with violations.
- risks — the §8 tightening could red an honest spec. Measured against the whole corpus before
  landing; the cutoff covers every case it would move.
- testing + left-shift gates — three new marker-contract rows, two new armed leg refusals, and the
  arms floors ratcheted.

## 6. Acceptance criteria

- `bash tools/memory-tree/check-verdict-epoch.sh` exits 0.
- `bash tools/memory-tree/check-memory-hygiene.sh` exits 0.
- `is_published` returns cannot-tell when ANY advertised tip is unreadable, not only when all are —
  exercised by a fixture advertising one present tip and one absent.
- A §8 opening with `None of the forks below are resolved.` above an unmarked fork reads FORKED in
  both readers, and `none - ...` above a marked fork still reads READY.
- The marker contract carries case, denial and N/A rows.
- The five suites pass, and `GATE_FULL=1 bash tools/run-gates/run-gates.sh` is green.

## 7. Gates

- `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1` at the push boundary.
- `python tools/memory-tree/check-arms.py --check`.
- `bash tools/memory-tree/kit-dogfood-parity.test.sh --check`.

## 8. Open questions

none — this unit resolves no fork of its own. Its content was fixed by an owner-independent rule: the
method says promote at a NON-CONVERGENT exit, and the promoted set is whatever round 4 confirmed.

## 9. Revision log

- rev-1 · 2026-08-21 · **created by the promotion rule, not by a plan.** The predicate exited
  NON-CONVERGENT and the leg check this build added then red the run for promoting nothing — the
  obligation and its enforcement both landing on their author in the same pass. Built and closed in
  the fold that created it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "promote a blocker to a unit at a non-convergent review
exit"` returns the unattended kit's own driver and protocol as the affordance seams, which is this
unit's subject rather than a reusable target. No symbol-level seam: the fixes are in five different
files with no shared mechanism, which is why §4 records that there is nothing to build once.
