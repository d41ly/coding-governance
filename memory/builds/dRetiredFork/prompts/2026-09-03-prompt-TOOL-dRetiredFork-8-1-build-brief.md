# Build brief — TOOL-dRetiredFork-8

**Serves:** journal TOOL-dRetiredFork-8

## What the unit is

gov hardcodes `.claude/settings.json` in ten places. inCMS's live settings file sits OUTSIDE the
worktree on every one of its nodes by design, so gov's spelling resolves to nothing there and every
wiring check passes BY FINDING NO FILE. That is the worktree false-green inCMS recorded at
`ARCH-dBriskLanyard-1 S10`. gov's hardcoded path is the defect.

## What this pass does

1. S1 — `settings_json()` resolving the file rather than spelling one location, and REFUSING when
   resolution yields nothing. inCMS's version returns EMPTY on no match; gov's must refuse, because
   an empty string is exactly what let every downstream arm pass by absence. That inversion is the
   unit.
2. S2 — `check_settings_scope`, REPORTING (ratified F1) when the resolved file lies outside the repo
   root. A legitimate per-machine layout is that shape; a project that wants RED promotes it via
   `TOOL-dRetiredFork-16`'s extension point.
3. S3 — every arm reads through the resolver, so no caller keeps a second answer.
4. S4 — three arms: resolvable in-tree, resolvable out-of-tree that REPORTS, unresolvable that
   REFUSES, the third observed RED first.
5. S5 — bump `KIT_CHECK_WIRING_VERSION` and its `gov:kit check-wiring@` marker.
6. S6 — take this file's own six carried install-prefix literals through the `KIT_REL` idiom. rev-2
   moved this here because `TOOL-dRetiredFork-13`'s declared population is test and selftest files
   and therefore EXCLUDES this checker, so the sweep had no owner.

## A hazard the source itself records, worth carrying

inCMS's header notes that a printed remedy CREATES a decoy at the worktree root and the walk-up then
finds the decoy first, so the arm reports ok forever over a machine-global hook nothing wired.
Reproduced live there before their fix. Whatever gov's resolver does, it must not be defeated by a
file the tool's own remedy told someone to create.

## AC5 exists because byte-identity cannot catch this

§4 says gov's own settings file sits where the literal already points, so an arm left on the literal
produces IDENTICAL output. AC5 greps for the literal and permits it only at the resolver's own
preference rung.

## And the two legs my hand-picked subsets missed twice

`bash tools/check-install-prefix.sh` and `gen_build_index.py --check-format` before committing.
AC6 needs the first anyway: the carried count must fall BELOW 6 and be re-baselined in this commit.
