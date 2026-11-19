# Revision — dLandedOwners: TOOL-dLandedOwners-4 diverged at its first build pass

**Serves:** research TOOL-dLandedOwners-4

## The prompt

> Fix the Ask 5, remove the ask TOOL-dTrackedAtlas-19

The owner's go for this build, of 2026-11-19; this record carries the builder's divergence back to the spec writer, its Goal the builder's `why` verbatim.

## The brief

### Goal
DIVERGENCE: the spec contradicts itself between §4 "The docs" (second bullet) and AC11 in §6. §4 says the module docstring's `arm_reader_coverage` clause should read "reds a catalogue key whose owner build has landed by `derive_landed_builds` (every spec terminal at the landed revision, or a build-kind run record with a first-parent landing merge, TOOL-dLandedOwners-1)". That text contains the exact substring "terminal at the landed revision". The same bullet then says `git grep` for "terminal at the landed revision" over tools/, help/ and README.md must find no copy of the old clause. AC11 requires its probe `'terminal at the landed revision' in d` to print False and that git grep to print nothing. I checked this with python: `'terminal at the landed revision' in <the prescribed clause>` prints True. So if the docstring is written as §4 says, AC11 stays red. The spec has to change one of two things. Option one: reword the parenthetical so the phrase is not in it, for example "every spec's status header terminal at L". Option two: point AC11 and §4's grep sentence at a phrase only the old clause holds, for example "every spec in its build folder terminal". Today that phrase appears only at tools/policy/check_policy.py@782ffc07:20-21. A smaller point for the same revision: the Files touched estimate does not list memory/LIVE.md or memory/builds/dLandedOwners/README.md. The commit hooks re-rendered both in unit 3's build commit b8297f701, so they should probably be listed. No other claim I probed failed.

### Items
1. `derive_landed_owners` in `tools/policy/check_policy.py` reads a build run that landed with a unit carried forward, DEFERRED against an ask, as landed, by the predicate the schedule's derivation took (its spec's fork F1, option g: a build-kind run record with a first-parent landing merge on the default branch), in a form a shipped kit can hold [planned TOOL-dLandedOwners-1]
2. The reader scan (`READER_SHAPES`, `scan_reader_keys`) reads a key passed to a reader call through a module-level constant, the shape the loop kit uses for seven dDeclaredLoop keys [planned TOOL-dLandedOwners-2]
3. A key whose only reader sits outside the scanned code, `deviation.approval`, read by a dClosedLoop instrument under the memory root, takes a declared disposition with its reason, never a silent pass [planned TOOL-dLandedOwners-3]
4. Ask TOOL-dTrackedAtlas-19 withdrawn on the owner's word [stale landed at `51971579a` before this build opened]

### Acceptance
At the build's tip, `derive_landed_owners` names dDeclaredLoop, dSafePassage, dFairHearing and dTrueNorth among the landed owners; reader coverage grades the keys of every landed owner and reports no finding; each new arm is observed red before green; the merge bar is green.

### Gates
The merge bar, `bash tools/run-gates/run-gates.sh`, once after the last unit; per unit, the direct check its spec names. The policy kit's own self-test arms are the owner's flagged bar, waived for this build as for dTrackedAtlas.

### Non-goals
Any other policy key; the loop kit's code, beyond what a reader shape needs to see; the chain builds' specs; the flagged bar.
