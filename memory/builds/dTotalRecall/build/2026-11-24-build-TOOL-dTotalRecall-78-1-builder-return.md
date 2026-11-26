**Serves:** journal TOOL-dTotalRecall-78
**Caused-by:** TOOL-dTotalRecall-78

# TOOL-dTotalRecall-78 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `32fad8345` from [2026-11-24-prompt-TOOL-dTotalRecall-78-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-78-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `07760b416`.

## Why

The spec builds as written. I checked its cited symbols, callers, gate-* home and population against the tree and found no divergence. The sweep output handed in the brief is in the acceptance ledger byte for byte (cmp equal).

## Summary

Built TOOL-dTotalRecall-78 rev-3: the S19 sweep's output is recorded in C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-78-1-acceptance-ledger.md, and the spec header is CLOSED. No code changed. RUN.md and the files gen_build_index.py rewrote are in the same commit; gen_build_index moved the build's status and the backlog row of TOOL-dTotalRecall-27 from INPROGRESS to DEFERRED, derived from the roster.

Checks run, each a probe of the recorded block:
- AC1: section 4's awk at the base lists 72 units (DERIVED 2026-11-24). The handed output has 72 verdict lines against `population 72`, and their first fields and order equal the awk list by cmp (DERIVED 2026-11-24). The red lines lead units 8, 37, 14, 15 and 26, each spec header DEFERRED, so no CLOSED unit prints a red.
- Beyond the spec: I ran unit 81's pass_of, from a script file, over every unit at this base. It printed the sha or named red the sweep prints for each, no line differing (DERIVED 2026-11-24). So the sweep run at f1b815ced answers this base; the only pass commit between them is unit 77's, at step 36 and outside the population.
- Every unit line of unit 76's block stands in this one; the new reads are units 76, 83 and 84 (DERIVED 2026-11-24).
- AC2: the git grep with --untracked found the ledger's block line, and `git worktree list --porcelain` names no gate-mc78.

These probes stand in for the kickoff-manifest ratchet leg's checker, which the main loop ran for the sweep. Owed to the close: section 7's legs, kickoff-manifest ratchet, memory hygiene, recall floor and recall floor arms. The unit declares no new arm, so no RED-first observation is owed. I ran no gate leg, suite or checker myself; the pre-commit hooks passed at the commit.

I read gotchas.py --for-diff HEAD~1..HEAD: the ledger's tokens are unwrapped and its fence is balanced, so nothing needed fixing. No command was skipped for its time bound. Some compound git commands were refused by the worktree isolation hook and re-run split up.
