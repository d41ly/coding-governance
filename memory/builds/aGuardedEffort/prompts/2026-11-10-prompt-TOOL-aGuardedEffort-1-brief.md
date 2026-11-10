# Brief — aGuardedEffort: the spawn guard refuses a spawn at the wrong level for its model

**Serves:** research TOOL-aGuardedEffort-1

## The prompt

> Build the guard

## The brief

### Goal
The hooks kit's spawn guard, `tools/hooks/agent-cap.js`, refuses a direct role spawn whose effort, and a harness call whose `efforts`, differ from the levels the effort policy gives the session's model, so a session that forgets the model argument is stopped at the tool call instead of shown on the `agent` line afterwards. This discharges ask `TOOL-aProfiledEffort-6`.

### Items
1. The guard learns the model a call will run on: an `Agent` call's own `model` argument where it carries one, else the `message.model` of the last main-chain assistant entry of the transcript the payload's `transcript_path` names. [planned TOOL-aGuardedEffort-1]
2. The guard learns the levels from the role index `.claude/roles.json`, which `render_agents.py` extends with the default role and stage levels and each profile's match words and resolved levels; the hook spawns no interpreter. [planned TOOL-aGuardedEffort-1]
3. An `Agent` call rule 6 admits is refused when the level it will run at, its `effort` argument or, with none, its role's default level, is not the level the model's profile gives that role. [planned TOOL-aGuardedEffort-1]
4. A `Workflow` call rule 6 admits is refused when, for any stage key of a workflow that harness runs, the level it will run at, the `args.efforts` value or, with none, the stage's default level, is not the profile's. [planned TOOL-aGuardedEffort-1]
5. The refusal names the role or stage, the level seen, the level expected, the model, and the `handoff.py role-efforts --model` or `stage-efforts --model` call that prints the right value. [planned TOOL-aGuardedEffort-1]
6. Where no model can be read, the call is admitted and one stderr line says the level was not checked and why. [planned TOOL-aGuardedEffort-1]
7. The hook's header, the roles README sentence `The spawn guard reads no`, the codebase-map dossier and the `help/` page say what the guard now checks and what it does not. [planned TOOL-aGuardedEffort-1]

### Acceptance
1. A payload whose transcript's last assistant model is `claude-fable-5-2` and whose `Agent` call for `gov-builder` carries no `effort`, or `effort: high`, exits 2 naming `medium`; the same call with `effort: medium` exits 0.
2. With a model no profile matches, the same call with no `effort` exits 0, and with an `effort` that is not the role's default exits 2.
3. A `Workflow` call for the unit harness on a Fable transcript exits 2 with no `efforts` and with `{"builder":"high"}`, and 0 with `{"builder":"medium"}`.
4. An `Agent` call carrying `model: fable` on a transcript of another model is graded against the `fable` profile.
5. A payload with no `transcript_path`, an unreadable one, or one with no assistant entry exits 0 and prints the not-checked line.
6. The word match in the hook and `roles_lib.resolve_profile` agree over one shared list of model ids, the non-matching `affable-1` among them, in a parity arm.
7. `render_agents.py --check` reds on a role index whose effort section differs from the policy's.
8. Every arm above is in `tools/hooks/agent-cap.test.sh` or the roles adopter self-test, and each was seen red before green.

### Gates
harness arms · roles catalogue · roles render wiring · roles render selftest · roles adopter self-test · hook destinations · codebase-map coverage + freshness · docs · kit/dogfood doc parity · lexicon naming predicates · kit epoch · kit version markers · memory hygiene · spec tokens; then the bar once at the close.

### Non-goals
The agents a running harness spawns through its own `agent()`, which no hook sees. The `committer` and `probe` stages, which take no level (ask `TOOL-aProfiledEffort-5`). Any change to a level, a profile, or the resolver's rules. A second matching rule: the hook's match is the resolver's, proved by parity. A refusal when the model cannot be read. Reading the model from anywhere but the call and the transcript.

### Limitations
The guard stops forgetting, not evasion, as rule 6's ceiling says: a hook-less run, a forged transcript and a hand-edited index pass it. A session reads hooks from its launch tree, so the guard arms in sessions started after it lands. The transcript is large; the hook reads its tail, never the whole file. An adopter with no profile tables in its policy gets an index whose effort section holds the defaults alone. Kit versions move through the lander's `mint`. The builder runs the two suites it adds arms to, once each, and no bar.

### Reuse
`tools/hooks/agent-cap.js` rule 6 (`checkHandoffSpawn`, `checkHarnessCall`, `extractWorkflowArgs`, `renderHandoffDeny`) is the seam, and the new check runs after it on the calls it admits. `tools/hooks/format-guard.js` already reads the payload's `transcript_path`. `tools/roles/render_agents.py` renders `.claude/roles.json` and `--check` grades it; `roles_lib.resolve_profile`, `resolve_effort` and `resolve_stage_efforts` are the one resolver the index is rendered through. The reuse probe returned `resolve_effort`, `resolve_stage_efforts` and `extractWorkflowArgs`. Records: `TOOL-aProfiledEffort-1` to `-4`, `TOOL-aOrientedCast-7`, `-14` and `-27` (rule 6).

## Drawn from the session

> Nothing enforces it. A session that omits `--model` silently runs at the default levels; only the `agent` line shows it afterwards. Filed as `TOOL-aProfiledEffort-6` (MED).
— agent, the aProfiledEffort wrap-up, 2026-11-10

## Owner confirmation

Asked: Build the spawn guard that refuses a role spawn at the wrong level for its model?
Answer: Build the guard

Asked: The guard will read the session's model from the transcript the hook payload names (the hook payload itself carries no model). When that transcript is missing or holds no model, what should the guard do with an Agent or Workflow call?
Answer: Admit, with a note (Recommended)

Asked: This is one Tier-2 unit in a new build folder (aGuardedEffort). Declare a spec audit for it, so a reviewer round audits the spec before any code?
Answer: No audit (Recommended)
