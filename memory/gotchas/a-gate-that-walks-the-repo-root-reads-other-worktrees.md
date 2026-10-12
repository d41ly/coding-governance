---
name: a-gate-that-walks-the-repo-root-reads-other-worktrees
description: a gate that lists its files by walking the disk from the repo root also reads every untracked worktree an adopter parks inside the tree, so it reds on files the commit does not hold, and an attribution re-run in a fresh worktree calls that red OWN
kind: class
---

# A gate that walks the repo root reads other worktrees

## Symptom

A scanner builds its population with `rglob`, `os.walk` or `find` from the repository root. Some
adopters keep their linked worktrees INSIDE the primary tree, at .claude/worktrees/<name>/, untracked.
The walk descends into each one, so the gate grades one copy of every file per live worktree, each at
another commit. It reds on findings the commit under test does not contain.

The red cannot be reproduced where it was written. A gate is developed in a worktree, and a worktree
holds no nested worktrees, so it is green there for its whole life. It reds only in the primary tree,
which is where landings run, so it surfaces at the worst moment and looks like the landing broke it.
The run-gates red-leg attribution re-runs a red leg in a fresh worktree too, so it sees green and
labels the red OWN: an OWN verdict on a walking leg is not evidence.

## Where it bit

`tools/gate-lint/ps-hygiene.py` walked the root with `root.rglob("*.ps1")` and a `SKIP_DIRS` prune.
On 2026-10-11 NicoCares' lander went red on 6 findings, every one in an untracked worktree copy of a
script, and the attribution called it OWN. nc's first local fix, `PKG-bStitchedFerry-3`, pruned
`worktrees` from the walk; a govkit pull overwrote it with gov's bytes, because the file is gov's.
nc's second fix, `PKG-bIndexedHarrow-1`, is the one gov took as `TOOL-cListedCensus-1`.

## The fix

When the question is about the COMMIT, take the population from the index: `git ls-files -z` with
`cwd` at the root, as `tools/gate-lint/sh_hygiene.py`, `encoding_posture.py` and now `ps-hygiene.py`
do. Pruning one directory name from the walk fixes one adopter's layout and still grades every other
untracked file.

The listing must be at least as wide as the walk it replaces. A git pathspec glob is case-sensitive
even under `core.ignorecase`, so `-- '*.ps1'` dropped a tracked `Deploy.PS1` that `rglob` graded on
Windows, and the scanner certified the narrower population clean. List with no pathspec and match
the suffix case-insensitively. `sh_hygiene.py` (`*.sh`) and `encoding_posture.py` (`.endswith(".py")`)
still match case-sensitively; that is `TOOL-cListedCensus-2`.

Converting a walk brings new failure modes, and each needs a refusal rather than a green: a dead
`git ls-files`, a listing that does not decode, and an empty listing each yield zero files. Observe
four cases: a tracked violation reds, the same bytes untracked do not, an upper-case suffix reds,
and an empty tracked set refuses.

A walk is still right when the question is about the disk, such as a generated artifact that is
never committed. Say which question the gate asks.

## Gated by

The instance has a check and no gate. `ps-hygiene.py --selftest` stages a BOM-less copy untracked
under a nested worktree path and asserts it is not graded, with the same bytes staged as the red
control, and tracks a sub/ü.PS1 that must red. No leg runs it, held or otherwise, because the kit
declares no ps-hygiene leg and wiring one is a later unit. Run it by hand after editing the scanner.

The class: no machine gate, because a walk is legitimate wherever the question is about the disk. The
documented check is a survey: grep the tracked tools for `rglob(`, `os.walk(` and a `find` over a
root, and for each hit ask whether it starts at the root and whether its question is about the
commit. At `6e8f8b1d` that survey found `tools/codebase-map/map_lib.py`, whose layer count already
lists from git and walks only when git fails (with `.claude` pruned), and
`tools/workflows/check_by_design_parity.py`, which walks two kit directories and never the root.
Neither was changed.
