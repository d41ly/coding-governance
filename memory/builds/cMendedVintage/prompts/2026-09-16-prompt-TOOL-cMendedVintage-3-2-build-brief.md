# Build brief — TOOL-cMendedVintage-3

**Serves:** journal TOOL-cMendedVintage-3

`check-wiring.sh`'s `.git` boundary walk cannot produce the empty prefix its own comment declares
legal. Read the spec whole first.

*Standing note: briefs in this build have carried six claims measurement disproved. Anything below I
have not run is marked UNVERIFIED.*

## The defect, and why it is worse than a wrong string

The walk appends `basename "$_p"` to `KIT_REL` BEFORE testing `[ -e "$_parent/.git" ]`, so `$_p`
itself is never tested as the repo root. At a ROOT install the walk runs past the repository to the
filesystem root and every `${KIT_REL:+…}` rung downstream gets a prefix assembled from directories
ABOVE the tree.

This is already recorded open as the thirty-second dRetiredFork row, CONFIRMED there by lifting the
loop into a probe: at `<repo>/tools/` it yields `tools` correctly; at `<repo>/` it yields
`tmp/tmp.qUok.../repo`; outside any repo it yields a temp path. So the comment at `:41-42` describes
a state the derivation cannot reach.

What makes it worth a unit rather than a tidy-up: the consumer is the `agent-cap` probe, the fan-out
guard. A wrong prefix there makes the arm report `skip — not adopted` about a hook that IS adopted
and wired, which is a skip that reads as a pass over the most important guard in the repo.

## The fix is two statements swapping order — so the RED is the whole job

The change itself is small enough to get wrong by being too clever. What earns the unit is observing
the failing case. Lift the loop into a standalone probe, as the backlog row did, and run it at three
positions: a kit subdirectory, the repo root, and outside any repo. Record what it yields at each,
before and after. The middle one is the case that must change.

Do not restrict yourself to asserting the repo-root case improves — check the kit-subdirectory case
is UNCHANGED, because every other `${KIT_REL:+…}` rung in the file depends on it and this unit must
not move them.

## Bounds

The comment at `:41-42` is rewritten to describe the derivation as it then is. Do not leave prose
asserting a property the code has only just acquired and you have not observed.

Do not touch the eight `SMERGE` emission sites or the `first_of` rungs — those are
`TOOL-cMendedVintage-4`, which is sequenced after this unit precisely because its
`${KIT_REL:+$KIT_REL/}` spelling rests on this derivation being correct.

## Write the acceptance ledger — this is now required of every unit

Hygiene check 23 reds when a CLOSED unit numbers a criterion no journal record evidences. Ten units
of this build closed without one and I backfilled them; that will not happen again. Write
`memory/builds/cMendedVintage/build/<date>-build-TOOL-cMendedVintage-3-acceptance-ledger.md`, shape
per the "Acceptance ledger" section of `memory/HYGIENE.md`, and record a criterion you could NOT
observe as owed rather than claiming it.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`. Spell no `tools/<kit>/…` path in
shipped prose. Re-declare with `--dispatch` if your write set grows. The machine is heavily loaded:
bound every command at 900s or more and treat a timeout as contention to report, not a failing check.
