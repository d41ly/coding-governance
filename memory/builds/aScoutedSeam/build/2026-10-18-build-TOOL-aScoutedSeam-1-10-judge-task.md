**Serves:** research TOOL-aScoutedSeam-3 TOOL-aScoutedSeam-1

# The blind judge's instructions for the diff-time arms

The instrument handed to each `gov-skeptic` judge as `input:spec`. The judge's `input:diff` is the path
of one packet that `-1-10-d1v2.py packets` wrote. This is the bench judge's prompt from
`-1-6-judge.js`, worded for a diff in place of a request. The rubric fields are unchanged, so the verdicts
file under `judge` beside the pre-spec arms'.

## Your task

You are a BLIND JUDGE in a benchmark of diff-time reuse reviewers, not a refuter of one finder. The
`input:diff` line names a packet file. Read it.

The packet holds:
- the request the diff built;
- the case tree(s), which you may open read-only to verify claims;
- the DIFF under review and its pre-diff tree;
- the GROUND TRUTH: the existing seams the diff should have reused, numbered from 0, each with why.
  Item 0 is the primary;
- any DECOYS: tempting seams that are wrong;
- several anonymous ARM outputs. Each is a numbered list of seams, each with a binding (MUST or SHOULD)
  and a how, that a reviewer says the diff should have reused instead of re-implementing.

For EACH arm:
- **covered:** the ground-truth item numbers it covers. Covering means a seam names that item, or names
  something that routes the build through it, so following the arm's instruction would reuse it. Merely
  naming a file that happens to contain it does not.
- **primary:** whether item 0 is covered at MUST or SHOULD.
- **wrong:** the seam numbers whose instruction would MISLEAD the build, each with why. That means a
  decoy, a lure for a different need, a stale copy where a canonical one exists, something that does not
  exist, or a seam the diff did not in fact duplicate.
- **valid_extra:** how many MUST and SHOULD seams outside the ground truth are genuine. A seam is genuine
  when the diff really re-implements or copies that existing code and reusing it would be correct.
  Verify against the tree and the diff when unsure.
- **score:** 1 to 5, how well a builder following ONLY this arm's output would undo the reinvention.
  5 means every essential seam and nothing misleading. 1 means it misses the primary or misleads.
- **note:** one sentence.

Never consult git history. Never read anything outside the tree(s), the diff and the packet. Judge each
arm on its own, and do not let arm order, length or seam count bias you.

RETURN CONTRACT. End your reply with ONE ```json block holding `{"arms": [...]}`, with one entry per ARM
label in the packet. Each entry has the keys `label`, `covered`, `primary`, `wrong` (a list of
`{"seam", "why"}`), `valid_extra`, `score` and `note`.
