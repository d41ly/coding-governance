# Execution handoff brief: the chain's execution plan, written for the owner's walk

**Serves:** research PLAY-dClosedLoop-1

The execution plan's writer renders its goal, items, acceptance, gates and non-goals from this brief record, through
`handoff.py render --input prompt=<this file>`. The owner asked how the chain is executed under today's gov; five
researchers answered one facet each, the owner answered four questions, and this pass turns both into one plan
(`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md`).

## The prompt

Write the execution plan for the dClosedLoop chain under today's gov, from the five execution researchers' returns
and the owner's four answers, as one record the owner walks and every node's session reads.

## The brief

### Goal

Write the plan by which the 22 chain builds are specced, built and landed across nodes a, b and d by today's
`/unattended` driver: fully oriented handoffs, coordination, per-node steps, and every spec held to the design under
the owner's answers. Each step names who acts, the tool or record that carries it, and the fact it rests on. Nothing
the records can derive is typed, so the schedule comes from a script kept beside the plan.

### Items

The plan's sections and the schedule script, as the plan brief (`input:spec`) lists them.

### Acceptance

- Every owner answer in the execution record's `[answers]` binds where it applies, as `[readings]` reads it, and none
  is contradicted. Where the plan finds a reading wrong, it says so as a question for the owner and applies neither.
- Every step names its actor (a node, the owner, a run, a role), its tool or record, and the fact it rests on as
  `path:line`.
- Every limit the five returns name appears once: either designed around with today's tools, or listed under what
  today's gov cannot do with its smallest change and that change's kind (a chain build's unit, a policy, a manual
  step).
- Where two returns disagree, the plan says which it follows and why.
- The schedule table is the output of the schedule script run on the tree, pasted with its command line, never typed.
- The plan opens nothing and changes nothing: the steps that write a chain build's files, a policy line or product
  code are for after the owner approves the plan.

### Gates

None of the bar's legs. Run the schedule script on the tree and report its output and exit code.

### Non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or
  `WIRE-INTO-PROJECT.md`, no `AGENTS.md` re-render, and no edit to `.unattended.conf` or any other policy file.
- No chain build folder, README, roster, packet or spec, and no status change to an existing build or ask.
- No change to v2 or to any audit record. A departure the plan needs from v2 is written as a proposed deviation for
  the owner, never applied.
- No edit to the five returns, the instruments record, the execution record or the session log, which are the main
  loop's.
