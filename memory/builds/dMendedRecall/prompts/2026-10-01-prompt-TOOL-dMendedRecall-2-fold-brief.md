**Serves:** journal TOOL-dMendedRecall-2

# Fold brief — the closing review's round 1 into TOOL-dMendedRecall-2

The closing diff review, round 1, is
`memory/builds/dMendedRecall/reviews/2026-10-01-review-TOOL-dMendedRecall-1-closing-diff-round1.md`.
Read it WHOLE. Its one confirmed item, M1, is MEDIUM and sits in this unit's `write_ask_views`. The
round recorded CONVERGED, so M1 is FOLDED into this unit's spec as a rev-N bump with a section 9 line,
and fixed, in ONE pass and one commit. The shared build brief
`2026-10-01-prompt-TOOL-dMendedRecall-1-build-brief.md` still binds every rule it states. The spec
stays CLOSED.

## The fork, resolved

Record it in the spec's section 8 as a new F-item, `RESOLVED (agent, 2026-10-01, delegated)`: the
review's option **(a)**. When any tracked input of the views, a path under the memory root or
`.memory-tree.conf`, has an unstaged or untracked change before the render, `write_ask_views` stages
NO rendered view. It names the dirty inputs and the repair, which is to stage or discard them and run
`gen_build_index.py --write`, and returns 1 without refusing the close. It never commits a view
derived from a change the operator has not staged. The reason: (b), rendering against the index in a
scratch checkout, adds a write surface outside the tree, which veto 3 prices, to rescue a case the
operator can repair in one command.

## What the fold owes

- The code change above, with its message spelled once.
- AC4's tracked arms flip as the review describes. A new criterion covers an unstaged spec
  status-header edit under `primary`: no view is staged, and the miss line names the input.
- AC2 and AC4's `--check` observations run over a CLEAN CHECKOUT of the commit the close made, never
  over the worktree. That is the review's left-shift, because hygiene check 9 grades the worktree and
  passed the stale commit.
- Every new suite arm is written in `tools/unattended/unattended.test.sh`; its run is not observed.
- Append ledger lines for every new or changed section 6 criterion.
- Commit subject: `fold(dMendedRecall): TOOL-dMendedRecall-2 — the closing review's round 1`.
