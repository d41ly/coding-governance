**Serves:** research TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2

# Two disjoint units, built serially and in parallel — the measurement

Node a, 2026-11-15, one frozen commit, the unit harness `tools/workflows/unattended-unit.js` at
`60dfb66ba` run through the Workflow runtime in attended mode, `gov-builder` at effort high.

## The bench

`aBenchedTwin`, a throwaway build on two local bench branches cut from `ae61a35cd`, never merged:
unit 1 adds `bench/twin/count_lines.py`, unit 2 `bench/twin/count_words.py`, disjoint, Tier-1, each a
small stdlib script with a self-check. Both arms start from `ae61a35cd`.

- **Serial**, `bench/aTwinnedPass-serial`: unit 1, then unit 2, each a harness call without
  `passBase`, building and committing in the main loop's own tree, as every run does today.
- **Parallel**, `bench/aTwinnedPass-parallel`: both units in one turn, each a harness call with
  `passBase` `ae61a35cd`, each in its own runtime worktree, then both merged back `--no-ff` by the
  main loop with the generated outputs re-rendered, the steps `pass-tree.sh --merge` takes.

## The figures (PINNED 2026-11-15)

| Phase | Serial | Parallel |
|---|---|---|
| unit 1's harness call (PINNED 2026-11-15) | 225 s | 282 s |
| unit 2's harness call (PINNED 2026-11-15) | 86 s | 322 s, run beside unit 1 |
| unit 2's status flip, by the main loop (the card routed no bench unit yet) (PINNED 2026-11-15) | 100 s | none |
| merge back, two passes (PINNED 2026-11-15) | none | 255 s: 128 s and 127 s, each about 55 s regeneration and 70 s commit hooks |
| wall, first launch to last commit (PINNED 2026-11-15) | 489 s (07:39:00 to 07:47:09Z) | 602 s (07:47:20 to 07:57:22Z) |

The serial wall holds the main loop's own turn gaps, about 50 s (PINNED 2026-11-15); the parallel
wall holds about 25 s (PINNED 2026-11-15).

## What it says

- On units this small the parallel route loses, by 113 s (PINNED 2026-11-15). Its cost is fixed per
  merged pass, about two minutes on node a (PINNED 2026-11-15): one regeneration and one commit's
  hooks. Its gain is the shorter unit's build time, which here was under two minutes for one arm.
- The break-even is a shorter unit longer than the merge-back, about two minutes per extra pass
  (PINNED 2026-11-15). This build's own units took 20.5, 25.8, 39.6, 20.3 and 13.8 minutes
  (PINNED 2026-11-15), and dDeclaredLoop's take 15 to 50 (PINNED 2026-11-15, from the task). Two
  such units at once save roughly the shorter one, less about four minutes of merge-back
  (PINNED 2026-11-15).
- A builder in a runtime worktree ran slower than one in the main tree, 282 s and 322 s against (PINNED 2026-11-15)
  225 s and 86 s (PINNED 2026-11-15). The two ran together on one node, and each first resets its
  tree and re-renders the index the commit hook demands. Two samples per arm separate none of these.
- Cutting a worktree is not the cost it looked: the runtime's cut is inside the harness call above,
  where a hand `git worktree add` of this repository took about three minutes per tree
  (PINNED 2026-11-15) at 02:36 to 02:42Z.

## The defect the bench found

Inside a Workflow, `agent()`'s worktree is cut at `.claude/worktrees/wf_<run id>-<n>` on the branch
`worktree-wf_<run id>-<n>`, here `wf_0d688c69-edb-1` and `wf_b6dff716-2a3-1`. The Agent tool's
worktree, the only spelling observed when `TOOL-aTwinnedPass-4` was specified, is `agent-<id>` on
`worktree-agent-<id>`. Unit 4 holds `BRANCH_SHAPE`, `TREE_SHAPE` and `pass-tree.sh`'s branch and
holder checks to that one spelling, so both bench passes returned `branch` and `worktree` blank and
`pass-tree.sh --merge` would refuse their branches. The harness runs inside a Workflow in every
unattended run, so the parallel route cannot merge back as built. It is fixed as its own unit before
any landing.

## Not measured

- Under unattended mode: `--dispatch`, `--brief` and the records commit before the cut are each one
  driver call, measured by `aBriskDeclaration` at about 125 s per dispatch (PINNED 2026-11-14)
  on a frozen clone.
- More than two passes at once, and two real units at once.
