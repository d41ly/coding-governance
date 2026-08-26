---
name: degradation-known-but-unreported
description: a pipeline computes how badly its own run degraded and then fails to say so where it matters, so a degraded run produces a clean bill
kind: class
universal: false
---

# The degradation is known and goes unreported

## Symptom

A pipeline counts what went wrong with its own run — dead lenses, dead verifiers, verdicts it had to
discard — and then the artifact a human reads says nothing about any of it. The counters exist. The
run knows. The reader does not.

Two shapes, one family.

**ORDERING.** A chained conditional tests the lesser degradation first, so the branch naming the
WORST outcome is reachable only in the combination where nothing else also went wrong — which is the
rarest combination there is. The most serious message a function can emit becomes its least
reachable one.

**REACH.** A counter is computed, returned to the caller, and never handed to the agent that writes
the durable artifact. The caller could tell. The record cannot.

The tell to hand a reviewer is one question, and it fits on a line: **does the thing that PERSISTS
carry the degradation, or only the thing that RETURNS?**

## Where it bit

Both shapes were confirmed by the closing diff review of build `dTieredTribunal`, whose record is
`memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-closing-diff.md` and
which states them as its two HIGH findings.

The ORDERING shape was live in all three review harnesses at once —
`tools/workflows/tier2-review.js`, `tools/workflows/drift-audit-state.js` and
`tools/workflows/drift-audit-code.js`. Each wrote its `note` with the degraded-otherwise arm above
the synthesis-death arm, so the string announcing that NO REPORT EXISTS was emitted only when no lens
had died, no verifier had died, and no finding was unverified. Two details make it worse than it
looks. It was PRE-EXISTING in the reference harness and got COPIED into the other two by the very
unit that was porting the trust accounting in. And the demote-on-conflict rule that landed in that
same unit makes the unverified count non-zero more often, so the port narrowed the path to its own
honest message while adding it. All three now test the synthesis death first, each under a comment
naming the unit that reordered it.

The REACH shape is the one still half-open, which is why this record is worth reading rather than
filing. The two drift-audit siblings now interpolate a run-integrity line into their synthesis
prompts. `tools/workflows/tier2-review.js` does not: its synthesis prompt names the raw, confirmed,
refuted and unverified counts and the precision, and no line in it hands the agent a liveness
counter. So the record that harness writes cannot state that half its lenses died — in the file the
closing review called the reference implementation.

## The fix

**No machine gate**, and this is a documented check rather than an unwritten one. Neither shape has a
static predicate that is obviously safe. A ban on conditional ordering would red every legitimate
chain in the tree, and a rule that "every returned counter must appear in a prompt string" is
satisfiable by a comment. The owner ruled the left-shift a record and not a scanner, at
`TOOL-dTieredTribunal-9` in this repo's decision log.

So the remedy is that the class is NAMED and reaches the checklist of the diffs that can carry it,
which is what `python tools/memory-tree/gotchas.py --for-diff` is for.

Two practices, one per shape:

- **Order a degradation chain worst-outcome-first.** The test is mechanical: for each branch, ask
  which combinations of the other counters let it be reached. If the most serious branch is reachable
  only when every other counter is clean, the chain is inverted.
- **Follow every counter to the ARTIFACT, not to the return.** A counter that reaches only the caller
  is invisible the moment anybody reads the file instead of the transcript, and the file is what
  survives the session.

## The anchors, and the width that was refused

The taken set is the harness surface: the directory token `tools/workflows/` plus the three harness
citations above, which are subsets of it. Measured by importing the shipped module and calling
`selectable()` over `git ls-files`, the set selects a little over one percent of the tracked tree.

The spelling refused is the bare tools directory — written here WITHOUT backticks on purpose, since
anchors are derived from backticked path tokens and naming it as a token would adopt the very width
this paragraph rejects. It selects about one tracked file in five. That is
near-universal selection bought under an anchor's name, and noise on a checklist is how reviewers
learn to skip the checklist. No absolute figure is written here: every one is derived from the
tracked path set, and a number typed beside the source that owns it is wrong on the next commit. The
width claim is a ratio, and the unit's own acceptance observes it with a negative rather than
asserting it.

Two more spellings are deliberately absent, and neither is refused on principle. The build-method
guide would put this class on every diff that edits the method, and a rule edit is not a harness
diff. The drift-audit kit already ships its own dead-probe doctrine. Both are absent because no
observed instance of this class sits there, and both are named in prose rather than as tokens, for
the reason the paragraph above gives.

## What this does NOT say

It does not say a counter must be returned — the ORDERING shape has nothing to do with what a
function returns, and the REACH shape is about the artifact and not the signature. And it does not
say a degraded run is a failed run. A run with two dead lenses that SAYS SO is doing its job; the
defect is only ever the silence.
