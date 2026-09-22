# Build brief — DEPL-cMendedVintage-2

**Serves:** journal DEPL-cMendedVintage-2

The pass this brief is handed to builds the unit that stops a FAILED restore reverting the receipt
row whose file did not revert. Read the spec whole first; this brief carries what the spec cannot.

## The defect, stated as the code does it

The rollback restore loop has four failure branches — the containment refusal, the `git rm --cached`
failure, the `update-index` failure and the `checkout-index` failure. Every one of them `continue`s
the per-path loop and falls through to an UNCONDITIONAL tail that reverts `ROLLBACK_FIELDS` on the
row and removes it from `withdrawn_rows`.

So the file stays exactly as this run wrote it while the receipt claims the pre-run `sha256`, and the
run then persists that receipt. Tree and record disagree, silently, and the next run classifies from
a base that describes bytes that are not there.

The predicate you need already exists thirty lines up: the `origin == "landed"` branch computes
exactly "which of this entry's paths actually restored" for its own case. This unit is that same
gating one level out — not a new idea, an existing one applied where it was missed.

## The half-restored case, which must be stated and not smoothed over

When `checkout-index` is what failed, the index was ALREADY reverted by the `update-index` call
above it. So after this fix that row's `sha256` matches the worktree and its `oid` does not. That is
a true and ugly state. Say it in the order file and in the spec's §5; do not invent a third field or
a repair that pretends the two halves moved together.

## What the order file owes

Its "Every path marked `restored` below was put back to the index entry it had" sentence becomes
false the moment one path fails. A failed path today appears in NONE of `restored`, `removed` or
`left alone` — it is simply absent, which reads as if it were never touched. It needs its own block.

## The fixture

Do not mock git. The spec names the cheapest manufacturable failure: make the worktree path a
DIRECTORY where the receipt names a file, so `checkout-index -f` cannot write it. That reproduces
the real branch with a fixture edit, and `govkit.py:7556`'s own header records that no arm reaches
these three branches today — so this fixture is new by necessity, not by preference.

Observe the RED first: without the fix, the row's `sha256` reverts while the file does not. An arm
that only ever sees the fixed engine is an assertion about nothing.

## Bounds

Do not widen this into the `r.fail` text of the other three branches beyond what §2 names, and do
not touch the `origin == "landed"` branch itself — it is already correct and is the model here.

`DEPL-cMendedVintage-1` has already landed and changed the same function: a kit in `_rr_stale` now
takes an exit that skips the restore loop entirely. Read that exit before you edit, so your
conditional lands on the path that still restores rather than on the one that no longer does.
