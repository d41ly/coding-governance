**Serves:** diff-review TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4

# Closing diff review, round 2 — the round that could not grade itself

*Node d, 2026-08-26, base `c80d9233` (round 1's recorded tip) to HEAD. Four lenses, five batched
skeptics, the shipped harness. Round 1's six confirmed findings passed as `priorFindings`.*

## Verdict: BLOCKED

**This round produced no verdict, and that is the finding.** All four skeptic batches AND the
synthesis pass died on the same error: `You've hit your session limit · resets 1:30pm
(Europe/Bucharest)`. The harness reported `raw 17, confirmed 0, refuted 1, unverified 16,
precision 0` and wrote no report.

Four finder lenses DID complete. Their 17 findings exist in the run journal and are transcribed
below **ungraded** — no skeptic saw them, so every severity here is the finder's own claim and not a
verified one. They are recorded because discarding them would lose the only evidence this round
produced, and because several are corroborated by more than one lens, which is weak evidence but not
none.

## Why the run ABORTED rather than landed

The build's four units are built, closed and gate-green. Round 1's blocker and its five highs are
folded. What is missing is M8's second half — *fix every blocker, then re-review the FIX* — and the
capacity to do that is gone until the limit resets.

Landing here would mean merging and pushing, with no owner turn, a tree carrying **17 ungraded
findings of which at least four are claimed HIGH**, three of them corroborated by three or four
independent lenses. That is the decision an unattended run must not take for its owner, and the
protocol's answer to a state like this is a terminal that neither merges nor pushes.

Halt code: `external-prerequisite`.

## The ungraded findings, and why three of them are almost certainly real

I read these myself rather than relaying them. Three describe defects I can confirm by inspection,
and I say which.

**Corroborated by three lenses — my new `--plan` arms are broken, for the third time.**
`units()` APPENDS a `gen:build-units` pair to a README that `readme()` already gave one, so all three
fixtures I added are DUPLICATED-pair READMEs. Every one of them hits the malformed-pair refusal
instead of the branch it claims to assert. **Confirmed by inspection**: `units()` is a `>>` append and
`readme()` writes a pair. The H2 arm — the one for the vacuity shape that shipped broken — is among
them, so the arm written to cover the regression cannot reach it.

This is the third distinct defect found in arms written for a suite a standing owner instruction
forbids running. The first two were caught by `check-arms` and the python-resolver leg. This one was
caught by a review that then could not finish. The pattern is not bad luck: **authoring test code you
cannot execute produces test code that does not work**, and every instance here was found by
something other than the tests themselves.

**Corroborated by four lenses — the marker check still does not mirror the driver.** The
almost-a-marker trigger I added for round 1's H4 tests `m in s`, containment anywhere on the line,
while `region()`'s `bad` arm fires only at column 0. **Confirmed by inspection.** So the fix for a
two-answers-to-one-question defect introduced a narrower version of the same defect — the third
iteration of that class in this build.

**Claimed HIGH, and I believe it — the H3 fix over-narrowed.** Scoping `--plan`'s row-to-id
extraction to the build FOLDER's slug makes any rendered row whose id carries a DIFFERENT slug
invisible. That is exactly the id/folder split this build renamed away from at its start, so the
corpus has no instance today — but the driver now silently drops such a row rather than naming it,
which is the failure mode `unit_ids_of` was already criticised for.

**The read-path justification contradicted the tree.** `corpus_ids.py --report` gives 135411 B where
the narrative claimed 135719. **Confirmed and corrected** in the same commit as this record: the
per-unit measurements were each right when made, and later passes shrank the path, leaving 461 B of
slack against a 153 B convention. Recorded rather than trimmed mid-flight.

The rest, ungraded and untriaged: the empty-region guard is ordered above the spec-file pass and
swallows the diagnostic that would explain it; the same guard precedes the no-tracked-spec check, so
a build with zero specs gets a repair instruction that will not help it; the `build-complete` guard's
message names an ABSENT pair it cannot actually reach; tightening the marker comparison makes the
DUPLICATED message reachable for counts where nothing is duplicated; `mkspec` writes every spec to
one path so a two-spec fixture overwrites itself; `roster_ids`' status is still discarded twelve
lines above the site round 1's H1 fixed; and the `tPlanEmpty` arm's fixture is destroyed by a
`reset_tree` before the assertion runs.

## What the next session inherits

Everything is committed on `branch/build-readme-governance-e1c044`. Nothing was merged and nothing
was pushed beyond that branch. The work to do, in order:

1. ~~Fix the three broken `--plan` arms~~ — DONE at `abf5fc22`. `setunits` replaces the rendered
   body where `units` appended a second pair, and it was verified STANDALONE — an empty body leaves
   one pair with zero rows, a two-row body leaves one pair in order — which is the property the
   broken arms needed and is checkable without running the suite the owner instruction covers. That
   matters beyond this fix: the three earlier defects in blind-written arms were all found by other
   gates, and this is the first one that could have been caught here.
2. ~~Fix the almost-a-marker trigger~~ — DONE at `abf5fc22`. A column-0 prefix test now, matching
   `region()`.
3. **STILL OPEN — a judgement, not a fix.** Whether `--plan`'s id extraction should be slug-scoped
   at all. Scoping fixed the digit case and the unscoped case together, and it also makes a rendered
   row carrying another build's slug invisible rather than named. No instance exists in the corpus
   today, so nothing is broken; the question is whether silence is the right answer if one appears.
4. ~~Re-derive `READ_PATH_CEILING`~~ — DONE at `abf5fc22`, 135872 → 135564 against a measured 135411.
5. **STILL OPEN — the one this round could not do.** Re-run the closing review from `c80d9233`,
   round 1's recorded tip, and grade the fourteen findings that remain ungraded.

Also fixed on the way: `mkspec` pinned every spec to `-1.md`, so any two-unit fixture silently
collapsed to one — the class, not just this instance. And the kit constant reached 2.43, its third
bump discovered only after a red bar, now filed as `TOOL-dHonouredPark-9`.

The full bar is GREEN at 85/85 over all of it.
