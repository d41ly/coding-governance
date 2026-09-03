# Build brief — DEPL-dRetiredFork-8

**Serves:** journal DEPL-dRetiredFork-8

The instructions this build pass was handed, recorded before the pass, so "which brief produced
this diff" has an answer on disk.

## What the unit is

Round 2 promoted this blocker: `DEPL-dRetiredFork-6` §6 AC2 requires `contribute` to propose
`TOOL-dRetiredFork-4`, and that unit was rescoped to absorb nothing. A correct verb proposes five
and reds AC2 — a criterion a correct implementation fails, which is round 1's H2 shape reintroduced
by the commit that fixed H2.

## What this pass does

1. Amend this unit's OWN spec first, per M2's rule that divergence changes the spec before the code.
   Two gaps found while reading, neither of them design changes:
   - S3 enumerates `§1, §4 Rollout (both sites) and §5`, but a fifth `nine` sits in §4's
     *Alternatives rejected* subsection and AC2 would flag it. S3 gains that site.
   - AC2 demands no surviving hit describing the absorption count, and §9's revision log carries
     one. A revision log records what rev-1 SAID; rewriting it would falsify history. AC2 gains an
     explicit scope clause excluding §9.
2. Then make the edits S1-S5 name, each as a WHOLESALE rewrite of its sentence, never a prepend —
   round 2 measured that 21 of its 30 defects came from patch-in-place folding.

## The count, stated once so the pass does not substitute blindly

Order 1 holds NINE units and EIGHT absorptions: `TOOL-dRetiredFork-4` absorbs nothing until it has.
The README's `Order 1 is nine independent absorptions` is false in the ABSORPTION half only, so the
rewrite must keep the unit count true rather than swap one number for another.

## Acceptance

The spec's AC1-AC4, run rather than asserted.
