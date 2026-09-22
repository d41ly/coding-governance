# Build brief — DEPL-cMendedVintage-1

**Serves:** journal DEPL-cMendedVintage-1

The pass this brief is handed to builds the unit that stops `update` rolling a kit back for a step
the same run declined to perform. Read the spec whole first; this brief carries what the spec cannot
— why this unit exists at all, and the two ways it can be built wrong.

## The live failure this closes

`govkit update --write` performs none of the install effects a new vintage needs, then runs each
kit's own `[check]` — the program that asks whether those effects happened — and rolls the kit back
on the red it caused. Because a rolled-back run takes the `if r.problems:` branch and withholds the
`gov_commit` re-stamp, the next run classifies identically and decides identically. Observed at two
adopter repos: five rollbacks, and three kits that cannot advance at any number of retries.

This unit does not make the renders happen. It stops the run punishing a kit for their absence, so
the loop breaks and the operator gets a report naming the declined step instead of a silent revert.

## The two ways to build this wrong

**Widening `_rr_stale` past the two render-staleness declines.** The inert decline is NOT one of
them. A target holding a kit deliberately inert chose that posture, and a check that reds because the
kit is inert is telling the truth. Fold that in and the unit starts suppressing real rollbacks.

**Suppressing the `r.fail` along with the rollback.** The run must still fail. What changes is that
the writes STAND and the order names the declined step as its first sentence; the verdict does not
become green. A build that makes the run pass has converted a wedge into a silent data problem, which
is strictly worse than the wedge.

## What the order file must say

Today its text tells the operator that "most often the clean three-way merge that produced this is
plausible and wrong". For every kit this unit covers that sentence is false — the merge was fine and
the cause was a step the run declined. The decline string goes FIRST, ahead of any merge advice.

## Bounds

The unconditional decline print is part of this unit: today the declines only print under
`GOVKIT_RERENDER=1`, so a default run creates the gap and says nothing. A decline that can decide a
rollback must not be invisible.

Do not touch the flag's default — that is `DEPL-cMendedVintage-7` and it is sequenced after
`DEPL-cMendedVintage-6` for a data-loss reason recorded there. Do not touch the restore loop's
receipt-row handling; that is `DEPL-cMendedVintage-2`.

## Gotcha classes this pass has already been warned about

`fixture-passes-by-finding-nothing` is the one to watch: the spec's own §4 records that `_rr_stale`
is empty in every existing rollback fixture, so an arm that merely re-runs those proves nothing about
this change. The new arms need a fixture kit that actually ships a `rendered` row with a check that
reds on staleness, and the red case has to be observed before the fix is wired.
