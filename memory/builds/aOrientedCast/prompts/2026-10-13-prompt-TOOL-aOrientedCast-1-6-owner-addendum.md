**Serves:** research TOOL-aOrientedCast-1 TOOL-aOrientedCast-2

# The owner's third addendum — every agent the session runs is shown with its effort and its references

Sent by the owner in this build's session on 2026-10-13, while the spec stage for the second
addendum's units was running. Verbatim:

```text
Let's also bring another small addition to the build: when you emit an agent role in your output, it's also mandatory to show its EFFORT LEVEL and other technical information references (a link to the prompt it was oriented with? what else could be meaningful there? Currently, agent tasks are a black box in Claude Code).
```

## What a run leaves that a line can cite, measured on this run's own spec stage

- The workflow's `journal.jsonl`: each agent's id, label and stage.
- Each agent's `meta.json`: its `agentType`.
- Each agent's transcript: its `model`, its `usage` (output and thinking tokens) and its timestamps.
- No file records the EFFORT an agent ran at; it is the run's own `efforts` argument, which
  `handoff.py stage-efforts` derives from the policy file, or the agent type's `effort:` line.
- The transcripts live under the user's Claude projects folder, outside the repository, so a link
  to one does not open in the app; the line carries the run and agent ids, which `/workflows` finds.

## The owner's answers, each asked on its own

- **Fields:** the role and its effort, plus all four optional groups: the model, the unit and a
  link to the prompt it was oriented with; the run and agent ids; on return, what it produced, its
  wall time and its tokens; and its write class with the gate legs its allowlist admits.
- **Cadence:** a line at dispatch and a line at return. A harness run emits one line per agent it
  spawned, derived from its journal.
- **Record:** the same lines append to a generated per-build agent ledger.
- **Enforcement:** a verb derives the lines so nobody types them, the pre-send self-check names
  them, and the Stop hook `format-guard` (built by `TOOL-aHeardState-1`, from the session in the
  `blissful-khayyam-69a7df` worktree) is EXTENDED to refuse a final message that omits them.

## The draft shapes

- agent — <role> · effort <level> · model <model> · <unit-id> · prompt [<name>](<path>) · writes <class> · gates <legs|none> · run <run-id>/<agent-id>
- returned — <role> · <outcome> · <wall> · <tokens> out · run <run-id>/<agent-id>

The spec writer settles the field order and names against the charter's micro-format grammar.

## What the run must reconcile first

`format-guard` is not on local main: `branch/aHeardState` was landing onto `origin/main` when this
addendum arrived. The unit extending it is specced only once the run branch carries that landing.
A second Stop hook for the same emission, `TOOL-aDistilledCharter-10`, sits unlanded on
`branch/governance-template-restructure-b84b3d`; two guards on one emission are two answers to one
question, and that overlap is the owner's to settle, not this run's.
