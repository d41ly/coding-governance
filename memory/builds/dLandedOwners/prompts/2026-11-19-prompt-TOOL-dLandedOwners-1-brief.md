# Brief — dLandedOwners: the policy kit's landed-owner set and the reader scan behind it

**Serves:** research TOOL-dLandedOwners-1 TOOL-dLandedOwners-2 TOOL-dLandedOwners-3

## The prompt

> Fix the Ask 5, remove the ask TOOL-dTrackedAtlas-19

## The brief

### Goal
The policy kit counts a build run that landed with units carried forward as landed, and its reader-coverage arm then grades every landed owner's keys with no false finding, closing ask `TOOL-dTrackedAtlas-5`.

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

### Limitations
Role work in role agents at their rendered efforts; units run no gates; no hook bypass and no `git add -A`; merge and push wait for the owner's ask.

### Reuse
`tools/policy/check_policy.py#derive_landed_owners`, `#check_reader_coverage`, `#scan_reader_keys` and `READER_SHAPES`; `tools/memory-tree/tree_lib.py` `TERMINAL` and `CENSUS_TERMINAL`; the landed predicate in `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive_landings`; the unattended kit's landing derivation `tools/unattended/lib-unattended.sh#read_landing_commit`. Recall returned TOOL-dGroundRules-8 S1 (the landed-owner set) and TOOL-dTrackedAtlas-5 (this ask).

## Drawn from the session

> Fixing ask 5 makes the policy kit count dDeclaredLoop (and dSafePassage, dFairHearing, dTrueNorth) as landed, which turns reader-coverage red on 8 dDeclaredLoop keys: 7 are read by the loop kit in a shape the reader scan misses, and deviation.approval is read only by a dClosedLoop instrument under memory/builds/. How wide should the fix go?
— agent, the question put to the owner, 2026-11-19

## Owner confirmation

Asked: Fixing ask 5 makes the policy kit count dDeclaredLoop (and dSafePassage, dFairHearing, dTrueNorth) as landed, which turns reader-coverage red on 8 dDeclaredLoop keys: 7 are read by the loop kit in a shape the reader scan misses, and deviation.approval is read only by a dClosedLoop instrument under memory/builds/. How wide should the fix go?
Answer: Predicate + scan (Recommended)
