# Build brief — DEPL-cMendedVintage-10

**Serves:** journal DEPL-cMendedVintage-10

`update --write` gains its second install effect: it writes the `.gitattributes` block and takes the
renormalize with it. Read the spec whole first.

*Standing note: seven briefs in this build carried a figure or a mechanism that measurement
disproved — most recently a count of 11 that was live 2, because the unit sequenced ahead of it had
deleted the other 8. Anything below I have not run is marked UNVERIFIED. Re-measure.*

## What makes this the riskiest unit since the flag flip

Every unit since `DEPL-cMendedVintage-7` has added a check, a declaration or a deletion. This one adds
a WRITE to a verb that currently only reports there, and the renormalize touches the index of files
the write did not name. Three things follow, and the spec states each:

**The snapshot ordering is load-bearing.** The `.gitattributes` row must enter the pre-write snapshot
BEFORE its bytes move, or a rolling-back run restores every other path and leaves gov's new block
staged. That is the failure the snapshot exists to prevent, and this is the first row that can
trigger it.

**The renormalize subtracts this run's own writes.** Get the subtraction wrong and it either refuses
a clean run or renormalizes a path the operator was editing. `missing_wt` is computed with `deleted`
removed on purpose — a path withdrawn under `--write-withdrawals` is legitimately absent, and
`apply`'s spelling would refuse for it.

**Two shipped selftest arms assert the OPPOSITE of what you are building.** They say `update` NEVER
edits `.gitattributes` and that it writes an ORDER instead. Rewriting them is correct and is the
unit; leaving them is a red bar. Say in your return that you flipped an assertion by name, because a
reviewer should see that stated rather than discover it.

## The remedy you are deleting is actively dangerous

`update-pins.md` today tells the operator to re-run `govkit apply`. `apply` overwrites engine bytes
unconditionally and ignores `deploy["inert"]` entirely — the only reader of that key in the whole
engine is the re-render decline. So the printed remedy destroys exactly the local forks that
`update`'s unattributed skip declined to touch. Delete that sentence; keep the order only on the
refused-because-dirty branch.

UNVERIFIED by me: whether `apply`'s inert-blindness has been fixed since I read it. It is
`DEPL-cMendedVintage-12`, which is sequenced AFTER you, so assume it has not.

## Do not add a second dirty check

`update` already runs its write preconditions, and `.gitattributes` is a receipt-claimed path, so
`dirty_claimed_paths` already refuses. A second check there is a second answer to one question.

## Required of every unit now

Write the acceptance ledger at
`memory/builds/cMendedVintage/build/<date>-build-DEPL-cMendedVintage-10-acceptance-ledger.md` per the
"Acceptance ledger" section of `memory/HYGIENE.md`. Record any criterion you could not observe as
OWED — this unit has several that only a suite can reach, and saying so is worth more than a claim.
Keep every backticked span whole on its own line.

## Standing bans

Lead any new function with a declared verb from `.lexicon.conf`. Spell no `tools/<kit>/…` path in
shipped prose, and check your own new comments against the predicate — it was widened one unit ago
and a comment quoting a path is itself a carried literal. Re-declare with `--dispatch` if your write
set grows. Bound every command at 900s or more; the machine is loaded.
