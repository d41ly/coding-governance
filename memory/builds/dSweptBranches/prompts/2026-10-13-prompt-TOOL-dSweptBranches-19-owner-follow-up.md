# Owner follow-up — dSweptBranches: the skill is `/cleanup`, and the two asks are built

**Serves:** research TOOL-dSweptBranches-19 TOOL-dSweptBranches-20 TOOL-dSweptBranches-21

node d · 2026-10-13 · attended. The owner answered the run's hand-off, in the session, with the
instruction below. The run was HELD `owner-decision` at `c07585e7`; it was resumed to VERIFYING
under keepalive `ca711d31` to carry the instruction on the same build.

## The prompt

```text
rename the skill and all its references from /branch-reconcile into /cleanup instead first, then build out the asks
```

## The brief

### Goal
The kit's skill is `/cleanup`: its name, its rendered path, its adopter, its descriptor rows, its
wiring leg and every live document that names it. Then the build's two open asks are built:
`TOOL-dSweptBranches-6` and `TOOL-dSweptBranches-18`.

### Items
1. Rename the skill `/branch-reconcile` to `/cleanup` and every live reference to it, the wiring leg's name included. [planned TOOL-dSweptBranches-19]
2. Audit gov's checks that read a range's added files for the merge blind spot inCMS's check 21 has. [planned TOOL-dSweptBranches-20]
3. Make the process-monitor census suite's live-tree arm wait for its staged tree instead of a fixed three seconds. [planned TOOL-dSweptBranches-21]

### Acceptance
Item 1: no live file names `/branch-reconcile` or `.claude/skills/branch-reconcile/`, the skill
renders at `.claude/skills/cleanup/SKILL.md`, and its wiring leg is green. Item 2: each gov site that
lists added files over a range is named with its invocation shape, a fixture merges the default
branch into a feature branch, and each shape is observed either to ignore the merged-in additions
or to red. Item 3: the live-tree arm is green with a staged slow spawn that the fixed wait reds.

### Gates
`bash tools/run-gates/run-gates.sh` at the close, with the kit self-tests.

### Non-goals
The kit's directory, CLI, module and remaining leg names keep `branch-reconcile`: they name the
kit, not the skill. Closed specs and run records keep the old name, because they record history.
No landing without the owner's ask.

### Limitations
The CI log of the census suite's red needs authentication this session does not hold, so item 3's
cause is the best-evidenced one, not a proven one; its proof is the next daily held job.

### Reuse
The skill's adopter and descriptor rows from `TOOL-dSweptBranches-5`. The process-monitor kit's
`test_live_tree_dies_completely` and `read_live_census` in `tools/process-monitor/selftest.py`. The
gotcha `fixed-sleep-does-not-place-a-signal`.

## Drawn from the session

> rename the skill and all its references from /branch-reconcile into /cleanup instead first, then build out the asks
— owner, 2026-10-13, after the hand-off

## Owner confirmation

Asked: not asked — the instruction names the rename, its scope and the asks
Answer: the instruction itself, quoted above
