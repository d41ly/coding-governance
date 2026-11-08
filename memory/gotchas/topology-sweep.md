---
name: topology-sweep
description: a change to a file where a worktree, merge or concurrent-run trap already bit is swept for the whole domain, a linked worktree's git dir to a commit under a running suite, not only for the one instance recorded at that file
kind: class
universal: false
---

# Topology — the domain's sweep, at the files where its traps bit

## Symptom

A change that is right in the one checkout it was written in is wrong in the shape the repository
actually runs in: several linked worktrees on one node, merges of the default branch, and runs that
overlap. A walk from the root reads another worktree, a hooks path resolves into another checkout, an
inherited git dir pins the work tree to the cwd, a merge reads as additions, or a check merged in from
the default branch refuses a record pinned before it. Each instance has its own record, anchored where
it bit, and a reviewer handed one of them is handed none of the domain's others.

## The sweep

For a subject touching a file below, ask each question of the change, not only the one its member
record answers:

- a linked worktree's git dir: does a command here inherit GIT_DIR or GIT_WORK_TREE, or resolve the
  common dir where it meant the worktree's own, or the reverse?
- an absolute hooks path: does a configured path resolve into another checkout than the one running?
- a merge read as additions: does a diff or a count over a range treat a merge of the default branch
  as this branch's own work, or keep both sides of one derivation?
- a half-staged move: does a rename or a generated render land in the index without its other half?
- a lease outliving its holder: does a claim, a lock or a witness outlast the process or the fact it
  was graded against?
- a commit under a running suite: can a commit, a merge or another run move the tree a running check
  is reading?

## Members

- a-gate-that-walks-the-repo-root-reads-other-worktrees
- a-merge-of-the-default-branch-read-as-additions
- hookspath-resolves-into-another-checkout
- inherited-git-dir-pins-the-work-tree-to-the-cwd
- merge-keeps-both-sides-of-one-derivation
- witness-graded-against-a-fact-written-after-it
- a-merged-in-check-can-refuse-a-pinned-record

## Where it bit

Each file below is an anchor of at least one member, so the sweep reaches a review only where a
recorded defect of the domain already landed: `tools/gate-lint/sh_hygiene.py`,
`tools/codebase-map/map_lib.py`, `tools/unattended/unattended.sh`, `.githooks/pre-push`,
`tools/lib/kit-rel.sh`, `tools/process-monitor/adopt-process-monitor.sh` and `tools/push-main.sh`.

## Gate

This class has no machine gate: the sweep is a reviewer's question over a domain, and each member
names its own gate or documented check for its one instance.
