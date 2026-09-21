# Build brief — DEPL-cMendedVintage-7

**Serves:** journal DEPL-cMendedVintage-7

This is the highest-risk unit in the build. It flips `GOVKIT_RERENDER` on by default, which makes
`update` execute target-side code on every adopter, on every run, for the first time. Read the spec
whole first.

*Standing note: two briefs in this build asserted a mechanism measurement later disproved, and a
third reported a missing `eol=lf` pin that `git check-attr` refuted. Anything below I have not run
myself is marked UNVERIFIED.*

## Why the flip is safe to make NOW and was not before

The flag shipped dark deliberately, and its own comment records the reason: this is the first time
`update` runs target-side code, so it lands off and is flipped after in-place verification. Two
things had to be true first, and both now are.

**The data-loss defect is closed.** `DEPL-cMendedVintage-6` landed one unit ago. Before it, one
declared regenerate argv destroyed adopter files at any prefix but gov's own — `update` restored
gov's filename spelling as a `missing` row and the adopter renamed it over the target's copy. With
the flag off that argv never ran; flipping first would have armed it everywhere. It is now a
`rendered` row whose destination carries the prefix, verified by a staged red at prefix `scripts`.

**Every declared argv has been run for real.** `DEPL-cMendedVintage-5` ran lexicon's, drift-audit's
and memory-recall's in this tree — all exit 0, each rewrote its own rendered row.
`TOOL-cMendedVintage-1` built and ran memory-tree's. All six rendered-row kits now declare one, which
I verified directly.

## What the flip does NOT change, and must not be described as changing

The argv is always gov's, from a gov-authored descriptor, never from the target's `deploy.toml`. The
trust boundary is unchanged. What changes is the BLAST RADIUS: code that previously ran only when an
operator opted in now runs on every update. Say that distinction precisely in the spec and the
comment — conflating them would claim a safety property this unit does not buy.

## The selftest arms are the trap

Two shipped arms have the OFF path as their subject: they strip the variable from the environment
and assert the off-path behaviour. After the flip, an env-stripped run takes the ON path and those
arms grade the wrong thing.

They must be pinned to `GOVKIT_RERENDER=0` **in the same commit as the flip**. Spelling the off value
there is correct, because the off path is genuinely what they are about — this is not weakening a
test to make a change pass. Land the flip without them and the `govkit selftest` leg reds; land the
pins without the flip and they assert a default that has not moved yet.

Keep `=0` a readable escape so an operator can revert without a code change.

## Bounds

Do not touch any `[[regenerate]]` argv — they are correct and are other units' work. Do not widen
this into per-step scoping of `classify_outcome`; that was considered and left alone one unit ago.

Three carriers state the old default in prose and must move with it, or the repo says two things
about one flag. The spec names them.

## Standing bans in this build

Lead any new function with a declared verb from `.lexicon.conf`; the offender pin is a two-sided
equality and one bad name reds an unguarded merge-bar leg. Spell no `tools/<kit>/…` path in shipped
prose; the carried-prefix arm is a BAN where a count may fall and never rise. Both have already been
tripped here once each.

Re-declare with `--dispatch` if your write set grows, before you commit.
