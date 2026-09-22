# Build brief — DEPL-dRatifiedSeam-1

**Serves:** journal DEPL-dRatifiedSeam-1

Tier-2 · node d · 2026-09-03 · order 1 · streams deployer

## What this unit builds

The standing predicate stops asserting the tracked-file count is UNCHANGED and starts asserting it
NEVER FALLS, and `update` gains the ability to land a gov source the target's receipt does not
name. The owner ruled this (`DEPL-dRetiredFork-13`) over the run's own recommendation of a separate
verb; that trade-off is recorded and is not reopened here.

## Grounding, measured before the first edit

**The subject is smaller than every prior count of it.** The ruling says nineteen arms. `grep` for
`[-11]` says eighty lines. Both are wrong: `[-11]` is the UNIT tag of `DEPL-dCarriedReceipt-11`
and covers renames, refusals, seed rows and two other ACs. What actually exists is ONE predicate at
`tools/govkit/selftest.py:4946`, its two `git ls-files` snapshots at 4941 and 4943, and one
consumer at 4953 that reads `_files_after`. That is the whole surface. The nineteen were a CASCADE:
a single write run that added files, nineteen downstream arms in the same fixture failing as a
consequence.

**S3 is a genuine build, not a port.** `DEPL-dRetiredFork-2` diagnosed, built and measured the
landing capability in a working tree and committed NONE of it — its own commit says so, and only
the `--kits` scope fix landed. Confirmed against the tree: `govkit.py` has nine matches for
`no receipt row|unclaimed source|new source` and every one of them is RENAME machinery
(`old source -> new source`) from `DEPL-dCarriedReceipt-11`. There is no landing path. The
diagnosis is reusable; the implementation has to be written.

## The one thing this unit must not get wrong

S1 relaxes a direction. S4 binds the other one. Landing S1 without S4 leaves a predicate that
grades nothing in either direction and reads green forever — which is the class `dRetiredFork`
spent fifteen units removing, and it would be introduced by the unit that inherits that build's
records. They land together.

## Where the acceptance is weakest

rev-3 folded four M4 findings into this spec's own criteria, all of them ACs that could not fail.
AC1's antecedent did not exist (no fixture arm ADDS a tracked file, so the relaxed direction was
never taken); AC3 and AC6 were self-graded by comment or ledger prose. Those are now written to
demand an arm or an exit status. The audit that found them was SELF-review — five cold reviewers
died on server 529s — so a cold pass is still owed and this brief does not claim one.
