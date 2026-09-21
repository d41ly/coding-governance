# TOOL-dDerivedDocket-54 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-54

One predicate in the unattended kit's shared library, `check_touching_commit_reachable`, answering
whether a commit since BASE that touched a path is reachable from a given commit. It walks
unsimplified, answers by status alone (yes, no, or cannot answer with a stderr line naming the
commit and the path), refuses a BASE that does not resolve to a commit before any walk, and refuses
a shallow clone, a walk git itself rejects and a blank path the same way. Nothing calls it at this
commit; the terminal-record exclusion is its first caller, at a later order.

No merge bar, no gate leg and no `*.test.sh` suite was run in this pass. What was run instead: the
predicate sourced from the library over a scratch fixture repository; and the new arm block, sliced
out of the suite by its own markers and executed standalone in a replica of that suite's prologue —
thirty-two assertions, green in about 3 s, and RED under each of eleven staged breaks applied to a
copy of the library: `--full-history` dropped, the BASE refusals removed under the range spelling,
the same under the caret spelling, a non-empty test in place of resolves-to-a-commit, the `^BASE`
exclusion dropped, the shallow refusal dropped, `--literal-pathspecs` dropped, the header sentence
deleted, the commit's resolve test removed, the blank-path refusal removed, and a refused walk
folded into a no. Both tables in the spec's §4 were re-measured on the fixture, rows 1 to 7 and all
five BASE rows, and each answered as tabled.

**Evidences:** TOOL-dDerivedDocket-54
- AC1 — `tools/unattended/lib-unattended.sh` — over a fixture whose witness merge takes as its
  first parent a nested merge that resolves the run-state path back to BASE's content (asserted
  directly: that merge's diff for the path is empty against its default-branch parent and not
  against its run-branch parent), the sourced predicate answers status 0 for that nested-merge
  parent with no reason line and no stdout, and the arm asserts beside it that the simplified
  spelling answers nothing for the same parent while the unsimplified one answers the nested merge
  — rows 5 and 6. Staged RED: with `--full-history` dropped the same call answers status 1. The
  check-19 verdict half and the suite's own run are this criterion's `permission:` line.
- AC2 — `tools/unattended/lib-unattended.sh` — the witness's other parent, a side branch off BASE
  that never touched the path, answers status 1 with no reason line — row 7 — so exactly one side
  reads as touched. Staged RED: with the `^BASE` exclusion dropped it answers status 0, because the
  BASE commit itself touched the path.
- AC3 — `tools/unattended/lib-unattended.sh` — a BASE that is not an object, an EMPTY BASE, a blob
  sha and a tree sha each answer status 2 with the stderr line naming the commit and the path; the
  empty-BASE arm also asserts through git's own trace that no `rev-list` ran, and a control over the
  same trace shows the counter counts the one walk a yes makes. A second control shows a blob BASE
  under the raw spelling answers a commit here, so the wrong-type arm grades a live hazard. Staged
  RED, as the criterion requires: with the refusals removed and the RANGE spelling in place the empty
  BASE answers status 1 and one walk ran; under the caret spelling the status arm passes for free and
  the no-walk arm reds; and with a non-empty test in place of resolves-to-a-commit the blob and tree
  BASEs answer status 0. rev-2 added arms for an unknown commit, a blank path, a walk git refuses, a
  glob-shaped path read as one literal path, and a shallow clone, each seen RED against its own break.
- AC4 — `git grep -c` — the header sentence opening `THE WALK IS UNSIMPLIFIED ON PURPOSE` counts 1 in
  `tools/unattended/lib-unattended.sh` in the index of this commit and 0 at its parent `3cb364d3`;
  the arm asserts the count and that the same sentence names the TREESAME shape and the
  existence-only limit within its next four lines. Staged RED: with the sentence's opening changed
  the arm reads 0.
- AC5 — amended rev-2 — `FLOOR_ASSERTIONS` — the floor rev-1 named cannot move: `ARMS_FLOORS`
  counts `fail` branches and this unit adds none. The suite's own floors moved instead, read with
  `git show` at the parent `3cb364d3` against this commit's index: `FLOOR_ASSERTIONS` 517 → 549 and
  `FLOOR_SHARD_2` 426 → 458, with `FLOOR_SHARD_1` unchanged at 91 because every new assertion sits
  at the end of region two. The raise is the block's thirty-two assertions, counted by executing the
  block standalone. That the suite still passes AT the raised floor is this criterion's
  `permission:` line and belongs to the build's one post-build bar.
