---
name: inherited-git-dir-pins-the-work-tree-to-the-cwd
description: with GIT_DIR set and no GIT_WORK_TREE, git takes the current directory for the work tree's top, so a `git -C <dir>` probe answers about <dir> as if it were the root; git exports GIT_DIR into a linked worktree's hooks, so a location probe that passed in a shell answers wrong inside one
kind: class
universal: false
---

# An inherited GIT_DIR makes `git -C <dir>` answer about `<dir>` as if it were the root

## Symptom

A script asks git where something sits: its repository prefix, the top of the tree, the root a
conf lives under. In a shell it answers correctly. Run by a git hook or a merge driver in a LINKED
worktree, the same probe comes back empty, or names the probed directory as the repository root,
and whatever the answer fed silently reads nothing. Nothing errors: an empty prefix is a legal
answer, and every reader downstream treats it as one.

## Why

When `GIT_DIR` is set and `GIT_WORK_TREE` is not, git does no discovery: it takes the CURRENT
directory as the top of the work tree. `git -C <dir>` changes that directory first, so every
`--show-prefix`, `--show-toplevel` or `--show-cdup` asked from `<dir>` answers about `<dir>` as if
it were the root. Git exports an absolute `GIT_DIR` into the hooks and merge drivers of a linked
worktree or a submodule, and into none of the primary-tree hooks measured, which is why each
instance passed where it was written: its author ran it in a shell, or from a primary tree.

Measured on node `a`, 2026-10-05, git 2.54.0.windows.1, in a fixture repository whose `commit-msg`
printed its `GIT_*` variables: a primary tree's hook got a relative `GIT_INDEX_FILE` and no
`GIT_DIR`; a linked worktree's hook got both, absolute, `GIT_DIR` naming the worktree's own git
dir. On a partial commit that index was a `next-index` lock file while another path stayed staged
in the real index, so scrubbing `GIT_INDEX_FILE` as well makes a commit-time check grade the wrong
index.

## Where it bit

- TOOL-aCollapsedScan-7, filed three times before it was fixed, as TOOL-aPacedTurnstile-10,
  TOOL-aCandidStub-4 and TOOL-aSealedCaravan-5: the memory-tree kit's row-keyed merge driver went
  inert in a linked worktree, because its conf lookup asked git for the top from inside the kit dir.
- TOOL-dScrubbedConduit-1 measured that a primary clone exports no `GIT_DIR` into a hook while a
  linked worktree does; TOOL-dRetiredFork-2 stopped the same leak reaching the subprocesses of two
  legs; TOOL-aRepatriatedFork-46 scrubbed it inside the substitution of two workflow-kit probes.
- TOOL-aGraftedHelix-27: `resolve_generated_indexes` in `tools/unattended/lib-unattended.sh` asked
  git for its kit's prefix, got an empty one under `.githooks/commit-msg`, and resolved no kit's
  generated outputs, so `--check-commit` refused an index the pass's own generator had rewritten.
  The `--dispatch` remedy that `tools/unattended/unattended.sh` prints named the driver by an
  absolute path for the same reason.

## What to do

Two fixes are in use, and they answer different questions.

- **The question is where a FILE sits** — a kit's own directory, its tool root. Walk up from the
  file's LOGICAL path to the first ancestor holding a `.git` entry, as `derive_self_rel` in
  `tools/lib/kit-rel.sh` does. It reads no environment, and through a junction or a symlink it
  anchors to the ADOPTING repository, where git answers with the link's target.
- **The question needs git** — the git dir, the common dir, an object. Run the probe from the
  repository root the caller already derived, or unset `GIT_DIR` and `GIT_WORK_TREE` inside the
  substitution that asks. From the worktree root, an inherited `GIT_DIR` answers `--git-dir`,
  `--git-common-dir` and `--show-toplevel` the way a shell does; it is only `-C` into a
  subdirectory that moves the answer.

Never unset them once, for the whole process: a check that reads `GIT_DIR` on purpose (the
driver's injected-config tripwire) goes blind, and an unset `GIT_INDEX_FILE` grades the wrong
index on a partial commit.

## The probes left, and why

The unattended kit's on-demand suite runner, `tools/unattended/run-unattended-gates.sh`, derives
its root and its kit path by asking git from its own directory, and under an inherited `GIT_DIR` it
would take the kit directory for the root. The main loop runs it on demand and no hook does. The
adopter, `tools/unattended/adopt-unattended.sh`, compares the kit's repository identity with the
adopting repository's by asking git from each; an inherited `GIT_DIR` would make both answer the
same id. An owner runs it by hand. The resume tick asks git from the root it already holds, so it
can only agree with how that root was derived. None of the three runs under a hook, which is the
whole of why they are left.

## Its gate

The driver's instance is **gated by** three arms in the driver's self-test: a real commit through
a `commit-msg` hook in a linked worktree, staging a kit-declared output beside its declared
generator; the resolver reached through a directory link from a second repository; and the
resolver called from a library copy outside any repository. The CLASS has **no machine gate**. The
predicate that finds the probes, a `git -C <dir> rev-parse --show-...` line in shell, printed 26
lines tree-wide at `f0971667`, and telling which of them a hook can reach is a question about
callers, not about the line. A gate over them is a mechanism of its own, handed off rather than
implied here. Until then it is a documented check: a reviewer of a diff that adds a location probe
asks whether a hook or a merge driver can run it.

## What this does NOT say

It does not say every `git -C` is wrong. A probe that asks for the git dir or the common dir from
the repository root answers correctly under an inherited `GIT_DIR`, and so does one that no hook,
merge driver or submodule operation can reach.
