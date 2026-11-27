**Serves:** journal TOOL-dTotalRecall-74
**Caused-by:** TOOL-dTotalRecall-74

# TOOL-dTotalRecall-74 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `377e10e61` from [2026-11-24-prompt-TOOL-dTotalRecall-74-build-brief](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-74-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `ff0bbc900`.

## Why

All three criteria were observed and the spec was buildable as written. §4's probe printed its pinned lines at the base.

## Summary

Two commits, both `Pass: TOOL-dTotalRecall-74`. 0114569d9558ebbd9440edadd97839306f60337b is the pass commit: the acceptance ledger, the spec header set to CLOSED, RUN.md, and the rendered README, LIVE and TOOL backlog. ff0bbc90048fa35d3d6311dbac9bde61ae70216a is the tip. It replaces an inline triple-backtick span in the ledger with a double-backtick one, the one hit I acted on from the bug-class checklist (inline-fence-swallows-the-rest-of-the-file; it was mid-line, so no fence opened). No code was edited and no deviation record written.

Checks that ran, as direct probes from script files in the scratch directory:
- AC1: §4's probe verbatim printed `s1-59 206422580b73 1`, `s1-46 254057fa6d5b 0`, `live-59 653bed738685 0`, `live-62 653bed738685 1`, `live-46 653bed738685 1`, then one `refused` line each for '' and '^' (DERIVED 2026-11-24). §4's `git log` command printed 63f283ddd first for unit 46 and 47afc8937 first for unit 59.
- AC2: the departure grep over unit 59's deviation records printed nothing, and its liveness grep printed deviation-591 alone. Both `absorbs` greps printed nothing, and a `git grep -c` over the same paths showed each file is read.
- AC3: the `Evidences` grep printed the ledger's block line, and the AC1 line under it names both labels and shas beside unit 70's recorded readings.

S3: `s1-59` is 1, so no deviation record of unit 59 is owed. S4: both counts agree with unit 70's ledger, so no false certification stands. Unit 70's AC1 line gives the first string no figure of its own, only that every row printed its wanted count, and the ledger says so. (DERIVED 2026-11-24, the pass)

Bug-class checklist: `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` ran over the pass commit and printed 23 anchored and 6 universal classes (DERIVED 2026-11-24). After the fix I read only its header lines over HEAD~2..HEAD.

Gates: these probes stand in for no gate's verdict. The legs `memory hygiene`, `recall floor` and `recall floor arms` are owed to the close. The spec declares no new arm, so no RED-first observation is owed. The pre-commit hook's own checks passed on both commits. Nothing was skipped and no command overran its bound; one read naming git was refused by the worktree guard and was split into plain reads.

Ledger: C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-24-build-TOOL-dTotalRecall-74-1-acceptance-ledger.md

The index render now derives the build's status as DEFERRED in README and LIVE, because unit 74 was the only INPROGRESS unit. The next flip to INPROGRESS re-derives it. (DERIVED 2026-11-24, the pass)
