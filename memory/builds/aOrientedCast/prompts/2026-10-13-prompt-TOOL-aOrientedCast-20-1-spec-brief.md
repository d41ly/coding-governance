**Serves:** journal TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3

# Brief record — the spec work at the resume: two folds and the third addendum's three units

## The prompt

The owner's third addendum, verbatim, recorded with its four answers in
`memory/builds/aOrientedCast/prompts/2026-10-13-prompt-TOOL-aOrientedCast-1-6-owner-addendum.md`:

```text
Let's also bring another small addition to the build: when you emit an agent role in your output, it's also mandatory to show its EFFORT LEVEL and other technical information references (a link to the prompt it was oriented with? what else could be meaningful there? Currently, agent tasks are a black box in Claude Code).
```

## The brief

### Goal

Every agent a session dispatches or receives is shown in its output with its role, effort, model,
unit, the prompt it was oriented with, its write class and gate allowlist, and its run and agent ids;
on return, what it produced, its wall time and its tokens. The lines are derived, never typed; they
are kept in a generated per-build ledger; and the Stop hook `format-guard` refuses a final message
that omits one. Two specs already written are folded so the set agrees with these units.

### Items

1. **Fold `TOOL-aOrientedCast-19`**, status DEFERRED. Two changes. The spec-token checker reds it:
   its §4 touches `.claude/skills/build/SKILL.md`, which the `check-wiring self-test` leg guards,
   and §7 does not name that leg. Read `tools/check-spec-tokens.py` to learn the guard join, without
   running it, and name the leg. Second, its roles kit version bump moves to TOOL-aOrientedCast-20,
   now the last unit to touch `tools/roles/`. Bump the rev with its §9 line, and leave the status
   line alone: the main loop flips it.
2. **Fold `PLAY-aOrientedCast-2`.** Its template version bump moves to PLAY-aOrientedCast-3, now
   the last unit to touch the charter template. Bump the rev with its §9 line.
3. **Spec `PLAY-aOrientedCast-3`**, order 21, streams playbook. Two micro-formats join the
   charter's `<!-- microformats -->` fence in `coding-governance-agents.template.md`, beside a rule
   line making them mandatory for every agent a turn dispatches or receives. Draft shapes, settled
   against the fence's grammar rules `[grammar]` and `[r1]`:
   `agent — <role> · effort <level> · model <model> · <unit-id> · prompt [<name>](<path>) · writes <class> · gates <legs|none> · run <run-id>/<agent-id>`
   and `returned — <role> · <outcome> · <wall> · <tokens> out · run <run-id>/<agent-id>`.
   Read `tools/check-microformats.sh` for what grades the fence and its closed head set, and name
   every carrier the new heads touch. The template version bump is this unit's.
4. **Spec `TOOL-aOrientedCast-20`**, order 22, streams tooling. A roles-kit verb that prints those
   lines, derived:
   - for a direct spawn, from its rendered handoff file;
   - for a harness run, from its workflow transcript directory:
     - `journal.jsonl` gives each agent's id, label and stage;
     - each agent's `meta.json` gives its `agentType`;
     - each agent's transcript gives its `model`, its `usage` and its timestamps.
   No file records effort; it comes from `handoff.py stage-efforts` or the agent type's `effort:`
   line. The write class and the gate allowlist come from `.claude/roles.json`. The same verb
   appends each line to a generated per-build agent ledger whose name and grammar fit
   `memory/HYGIENE.md`. The roles kit version bump is this unit's.
5. **Spec `TOOL-aOrientedCast-21`**, order 23, streams tooling. Extend `tools/hooks/format-guard.js`:
   a final message that omits an agent line for an agent its turn dispatched or received is
   refused, with the shapes read from the fence as the hook already reads its others. Decide how the
   hook learns which agents the turn dispatched and received; its Stop payload carries the
   transcript path. The hooks kit version bump is this unit's.

### Acceptance

Each fold leaves `python tools/check-spec-tokens.py` with no hit on its spec. Each new spec carries
the full ten sections, a §6 whose every criterion is a direct check a builder may run, and a
`New arm:` line per new refusal, naming its staged break.

### Gates

The close runs `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1` once on the reconciled tree.
Each spec's §7 names the legs its change touches.

### Non-goals

- Re-opening the owner's answers recorded in the three addenda.
- Editing a CLOSED spec.
- A second Stop hook for this emission; the one to extend is `format-guard`.
- Grading chat prose beyond the agent lines and what `format-guard` already grades.
