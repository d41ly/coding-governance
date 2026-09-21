# Build brief — DEPL-cMendedVintage-5

**Serves:** journal DEPL-cMendedVintage-5

Three kits gain a `[[regenerate]]` argv so `update` can refresh their rendered artifacts. Read the
spec whole first; this brief carries the two things it cannot.

## Why these three and not the fourth

`update`'s re-render step is real and has been for several vintages — what it lacks is anything to
run. Six kits ship `rendered` rows and only two declare a `[[regenerate]]`, so eight rendered rows
across four kits go one vintage stale on every update and the run says nothing about it.

lexicon, drift-audit and memory-recall are in this unit because their adopters ALREADY re-render with
no adoption guard to trip over: `adopt-lexicon.sh` under `--render`, `adopt-drift-audit.sh` on a bare
invocation, `adopt-memory-recall.sh` under `--scaffold`. So each is a TOML declaration pointing at an
entrypoint that already works. memory-tree is deliberately NOT here — its adopter accepts only
`--scaffold` and exits 0 with "already scaffolded, nothing to do" on an adopted tree, so it needs a
real render mode first. That is `TOOL-cMendedVintage-1` and it is the next unit but one.

Everything you declare here stays INERT until `DEPL-cMendedVintage-7` flips `GOVKIT_RERENDER`, which
is four units away and gated behind a data-loss fix. So this unit cannot be observed end to end yet,
and its acceptance should not pretend otherwise.

## THE OUTCOME BLOCK YOU ARE SHIPPING HAS A CONFIRMED DEFECT — do not widen it, do not fix it

S4 has you declare a lexicon `[[outcome]]` of `code = 1` plus `must_not_exist = ".lexicon.conf"`
plus `ok = true`. The spec audit confirmed this accepts a FAILED FIRST SCAFFOLD as adopted:
`adopt-lexicon.sh` exits 1 with `.lexicon.conf` absent when the scaffold fails, because the conf is
precisely what the failing program was trying to write. The intended accepted state is the
unconfigured POSTURE; the failure is shape-identical to it.

And it is not confined to the re-render path. `classify_outcome` reads the kit-level `outcome` list
with no per-step scoping, so `apply`'s CONFIGURE consults it too — which means the defect is live the
moment this unit lands, not when the flag flips.

`DEPL-cMendedVintage-16` owns narrowing that probe and has been MOVED to run immediately after you,
for exactly this reason. Ship S4 as written, say in your return that it is provisional and why, and
do not invent a narrower probe here — taking that work would leave `-16` with nothing to close and
would be an unreviewed design change besides.

## Bounds

A version bump per kit is in scope and is the point: an adopter cannot detect a vintage whose version
did not move. Do not touch the adopters themselves — every entrypoint you name already exists, and if
one turns out not to, that is a finding to report rather than a script to write.

## Traps the landed units measured

A fixture can stage a condition the tool does not actually refuse, so confirm any RED is the red you
meant. A first cut can be vacuously green when the artifact is absent — assert it exists first. And a
derived count written into prose beside its source is the two-answers class; this build's checklist
has caught it twice already, once in a comment and once in a spec.
