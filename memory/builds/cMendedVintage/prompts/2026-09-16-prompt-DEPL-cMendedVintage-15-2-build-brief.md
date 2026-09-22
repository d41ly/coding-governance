# Build brief — DEPL-cMendedVintage-15

**Serves:** journal DEPL-cMendedVintage-15

This is the spec audit's BLOCKER, and it is the first promoted unit to run in its re-sequenced
position — immediately after the unit whose work it corrects. Read the spec whole first.

*Standing note: eight briefs in this build carried a figure or mechanism measurement disproved.
Anything below I have not run is marked UNVERIFIED.*

## Why it sits here and not at the end of the roster

The disposal appended every promoted unit after the whole roster, which is right for the five that
repair already-built code and wrong for the two that repair `DEPL-cMendedVintage-10`. That unit
landed one commit ago and introduced the very snapshot entry you are fixing. I moved you to order 18
so the window between the defect and its repair is one unit rather than thirteen.

## The defect, in the shape the audit found it

`apply` stamps the `.gitattributes` receipt row with the synthetic kit id `(govkit)`, which no
registry entry claims. Both consumers of a snapshot entry's `kit` key then reject it: the restore
loop selects entries whose `kit` matches an id in `touched_kits`, which holds claimed ids only, and
the orphan sweep flags every snapshot entry whose kit is not in `claimed`.

So the entry `DEPL-cMendedVintage-10` now adds can never be restored by a rollback, and it prints a
spurious orphan line on every run that writes it. Its own AC4 cannot pass as things stand.

## What makes this a blocker rather than a high

A rolling-back run restores every other path and leaves gov's new `.gitattributes` block staged in a
repository gov does not own. That is the exact failure the pre-write snapshot exists to prevent, and
`-10` is the first unit to put a row in it that the restore cannot reach.

## The two halves must land together

A restore stage that reaches the entry, AND removal from the orphan sweep. Do one and the run either
restores the block while still calling it an orphan, or stops calling it an orphan while still
leaving it staged. Neither half is coherent alone.

## Observe the failing case

`-10`'s own AC4 was recorded OWED precisely because nothing in the tree could stage a green-to-red
check across the run. If you can build that fixture, you close AC4 for that unit as well as your own
criteria — say so explicitly if you do, because its ledger currently records the mechanism as built
and unexecuted. If you cannot, record yours as owed rather than claiming it.

## Standing bans — note the widened wording

Lead any new function with a declared verb from `.lexicon.conf`, **including helpers you add to
`tools/govkit/selftest.py` or `matrix.py`**. That exact class has now landed twice in this build,
both times in a test-side helper a unit did not think to check: `_dr_render` and `_eol_of`. The
offender pin is a two-sided equality and one name reds two unguarded merge-bar legs.

Spell no `tools/<kit>/…` path in shipped prose, and check your own new comments — the predicate was
widened two units ago and a comment quoting a path is itself a carried literal.

## Required of every unit

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-15-acceptance-ledger.md` per
`memory/HYGIENE.md`. Record any criterion only a suite can reach as OWED. Keep every backticked span
whole on its own line. Re-declare with `--dispatch` if your write set grows. Bound every command at
900s or more.
