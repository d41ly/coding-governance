# Revision — TOOL-aPrunedIndex-17: AC7 as interleaved A/B pairs on one tree

**Serves:** research TOOL-aPrunedIndex-17
**Caused-by:** TOOL-aPrunedIndex-17

## The prompt

> DIVERGENCE: spec section 6, AC7 … AC7 reds a correct build whenever load drifts between the before block and the after block.

The unit 17 builder returned this on 2026-11-26 in run `wf_2525b635-518`. It built the code exactly as sections 2 and 4 say, and AC1 to AC5 were green. The spawn counts after the edit matched section 4's pinned "with" column exactly: 20, 17, 207, 31 and 86, with `rebuild` at 32.

AC7 compares three before-edit rounds with three after-edit rounds, taken as two separate blocks:
- Before, the five plants summed 108.4, 151.6 and 127.9 s.
- After, they summed 131.6, 119.2 and 79.1 s.
- Between the blocks the load gauge swung from 0.041 to 0.324 s per spawn.

The builder also ran an interleaved A/B probe of `gc-predates` on the edited tree, with HELD_PLANTS emptied for A:
- A took 39.1, 31.8 and 30.9 s.
- B took 16.9, 18.0 and 22.2 s.
- The spreads separate cleanly, at a ratio near 0.56.

Everything above ran on node a.

## The brief

### Goal
Spec 17's AC7 measures the saving in a way the node's load cannot turn red on a correct build.

### Items
1. AC7 at rev-3 alternates before and after on ONE built tree. "Before" is the same code with `HELD_PLANTS` emptied, and "after" is the code as built. It takes at least three interleaved A/B pairs, per plant or per five-plant set, with the load gauge beside each reading.
2. AC7 is red in two cases: a pair's "after" is not faster than its own "before", or the median after/before ratio is above a bound the spec justifies from the 0.56 probe and section 4's 0.71 estimate. The spec states that AC4's spawn counts remain the stable measure.
3. Section 4's text, any `New arm:` line and any section 7 line that name AC7's method follow the change. The status header goes to rev-3 and stays INPROGRESS.
4. One revision-log line: "rev-3 · 2026-11-26 · AC7 reworded to interleaved A/B pairs on one tree, after the builder's divergence (two-block rounds red under a 0.041 to 0.324 s gauge swing)".

### Acceptance
Spec 17 at rev-3 carries the reworded AC7 and the revision-log line. A diff against rev-2 touches only AC7 and the lines items 3 and 4 name.

### Gates
memory hygiene; spec tokens (a spec's own names resolve)

### Non-goals
No edit to any file but spec 17, no commit, and no code. AC7's observation runs fixture plants only, never the live index.
