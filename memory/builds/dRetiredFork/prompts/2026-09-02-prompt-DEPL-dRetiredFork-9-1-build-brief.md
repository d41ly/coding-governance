# Build brief — DEPL-dRetiredFork-9

**Serves:** journal DEPL-dRetiredFork-9

## What the unit is

Two criteria written in the same fold round cannot both be satisfied. `DEPL-dRetiredFork-3` AC10
calls itself the build's done-condition and requires a `gov_commit` re-stamp;
`DEPL-dRetiredFork-1` AC6 accepts a non-zero `unattributed` count. `govkit.py:6566-6573` withholds
that stamp whenever any row is `unattributed`, and AC10's argv carries neither escape it names. So
the build can pass every unit and fail its own README.

## The decision, already made

§8 F1 is RESOLVED (owner, 2026-09-02) by its own stated Recommendation: **zero at NicoCares,
`--allow-ungraded` at inCMS until its receipt is repaired, both stated in AC10.**

## What this pass does

1. Write ONE shared sentence, verbatim, into both `DEPL-dRetiredFork-3` AC10 and
   `DEPL-dRetiredFork-1` AC6, so AC2's diff finds them identical and neither can be read alone.
2. Add the scope item S3 requires to `DEPL-dRetiredFork-1`, since the decision is ZERO at NicoCares
   and no unit drives that population today — an acceptance criterion with no scope item behind it
   is the shape this build keeps finding.
3. Record S4's rule in the README: a criterion labelled the build's done-condition is read against
   every other spec's §2 before the set closes.
4. Every edit is a WHOLESALE rewrite of the criterion it touches, per S5.

## Acceptance

AC1-AC5, run rather than asserted. AC4 in particular: the two escape names appear in BOTH criteria
or in NEITHER, never in one.
