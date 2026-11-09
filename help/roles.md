# Role agents and `/build`

**What it is.** Every piece of LLM work in a governed repository runs as a declared workflow: <!-- usage: command:build 03924a5c -->
orientation, research, reuse, spec writing, spec review, building, the closing review, the gate bar,
handoffs and bookkeeping. Spec writing, spec review, building and the closing review run only inside
role agents. The main session orients, hands work off and keeps the records. Hooks refuse the
bypasses, so this holds without anyone remembering it. The charter states this as its `[roles]`
rule and lists every role under `## Agent roles`, a section generated from the role files.

The kit is `<prefix>/roles/`, which is `tools/roles/` in this repository. Its README is the full
reference; this page is the short version.

## How a task reaches an agent

1. **Kickoff writes the card.** Its `## task` block carries the goal, scope, cut-line, To-do, Reuse,
   acceptance check and gates.
2. **A role supplies the constant part.** Each role is one file under `<prefix>/roles/agents/`: its
   instructions, the inputs it reads, the file class it may write and the tags of the charter's
   practices it needs, under `rules`. It also says when the role is mandatory, under `mandatory`, and
   where its output goes, under `output`. Its agent carries those rule lines and the charter's
   Protocols and Facts sections whole.
3. **The handoff renderer joins them.** `handoff.py render` writes one prompt file under the build's
   `prompts/` folder, with `## Role` and then `## Task`, filled from the card, the build's brief and
   any `--input` values. A required input that is missing or still a placeholder refuses by name.
   The prompt carries no charter text: the charter rides once, in the agent file.
4. **The agent runs as a native type.** Each role is rendered into `.claude/agents/gov-<role>.md`,
   which starts without the full charter and at the reasoning effort the policy file sets. It
   carries the practices its role cites and the charter's Protocols and Facts sections, first.
5. **Each block carries its level.** With the playbook kit installed, every block a subagent gets
   sits in an envelope, `[<doc> · Level <n> · <direction>]` up to `[/<doc>]`, so it ranks them as
   the main session does. The agent file holds the charter at level 0 inside its own level 5. The
   task part holds the practices at its step at level 0, then the task at level 6.
   `handoff.py check <file>` refuses an envelope left open or a level that falls within a part.
   Without the playbook kit the render prints one `envelope — unarmed` note and ranks nothing.

## When a render checks a role's load set

Before it writes, the handoff renderer, and the agent-type render for every agent at once, asks the
playbook kit which instruction units the role loads. A unit can name the readers that must load it,
under `required-by`. When the role's set lacks such a unit, the policy key `instructions.checks`
decides:

- `refuse`, the default: nothing is written. The refusal reads
  `load-set — refused · role.<name> · missing <unit> · instructions.checks=refuse`, and the remedy is
  to scope the unit to that role, or to drop the role from its `required-by`.
- `warn`: the render is written with a `Missing required unit: <unit> · role.<name>` line where the
  agent reads it, in the handoff's task opening or the agent type's body.
- `record`: the render is written, and the handoff's prompt file gains a `**Load gaps:**` line under
  its `**Serves:**` line. The agent's text is unchanged.

No value skips the check, and `budgets.enforce` never softens it. The same render measures the role
block against its body ceiling: under `budgets.enforce = "warn"` an oversized block prints a
`BUDGET WARN` note, and under `refuse` the render is refused. With no playbook kit installed, the
render prints one `load-set — unarmed` note and proceeds.

## The practices at the work order's step

Each workflow names the step its work serves, under `step` in `<prefix>/roles/workflows.toml`: `entry`,
`plan`, `design`, `build`, `test`, `deploy`, `review`, or `none`. A work order carries what each active
practice changes at its role's step: the handoff's task section ends with a `### Practices at <step>`
block, one `- [<name>] <reach>` line per practice that reaches that step. A builder's reads, for example,
`- [yagni] delete rather than disable`. The charter keeps one line per practice and carries no reach.

The active practices are the policy key `charter.practices`, the foundation set when unset. A step of
`none`, a step no active practice reaches, or an install with no playbook kit renders no block.
`python <prefix>/playbook/load_sets.py derive --reader role.<name>` lists the units as
`practice.<name>.<step>`.

## The code input every role carries

Every role's load set has a `code` slot, so a handoff can carry code ranges, the definitions with
their callers, callees and tests, without any role file naming it. Pass a file with
`--input code=<path>`: the handoff gains an `### input:code` block holding that file's text. Leave it
out and the task opening names `input:code` among the optional inputs not supplied.

The slot's budget is the policy key `memory.code-budget`, `16k` by default, which is 16,000 bytes;
`python <prefix>/playbook/load_sets.py derive --reader role.<name>` prints it as
`code — slot · budget 16000 · memory.code-budget default 16k`. A block over it obeys the size switch
as the role block does: `BUDGET WARN · code · <bytes> bytes over code-slot <budget>` under `warn`, a
refused render under `refuse` or with `code-slot` in `budgets.pinned`. A value that is not `<n>k`
refuses the render, naming the key.

## How to use it

- **Run an attended build:** after kickoff's READY card and the owner's go, invoke `/build`. It walks
  the workflows in stage order and calls the same harnesses `/unattended` uses.
- **Hand one task to one agent:**

  ```bash
  python tools/roles/handoff.py render --role gov-builder --build <slug> --unit <unit-id> --part task
  ```

  Pass that output, unchanged, as the prompt of an `Agent` call whose `subagent_type` is <!-- usage: script:tools/roles/handoff.py#render 57cac9a7 -->
  `gov-builder`. An edited prompt is refused. Pass the name it prints on stderr after
  `handoff: description — ` as the call's `description`; any other name is refused.
- **Change how a role behaves:** edit `<prefix>/roles/house/<role>.md`, never the file under
  `agents/`. Your overlay is appended under `## House rules`, and updates never overwrite it.
- **Change a role's effort, or the gates a role may run:** edit `<prefix>/roles/house/policy.toml`.
  Its `[effort]` tables set levels per role and per harness stage; its `[gates]` table lists the
  only gate legs a role agent may run.
- **Render in this order.** After changing a role file, re-render the charter first with
  `bash tools/playbook/adopt-playbook.sh --target .`, because its Agent roles section is generated <!-- usage: script:tools/playbook/adopt-playbook.sh 814e2edf -->
  from the role files. After changing a role, an overlay, the policy or a charter rule, run
  `python tools/roles/render_agents.py --write`. Then start a new session: a running session cannot <!-- usage: script:tools/roles/render_agents.py ee6e2d2c -->
  spawn an agent type written after it started.

## How agents are named

Every agent's name says what it is doing now: the build, the unit and the action.

- **An agent the main session spawns** is named by `handoff.py render`, which prints the name on
  stderr as `handoff: description — <name>`. It reads `<build> · <unit> · <workflow>`, for example
  `aOrientedCast · TOOL-aOrientedCast-27 · build`, or `<build> · <workflow>` when the render names no
  unit. The workflow is the role's, from its role file. A spawn whose `description` is missing or
  differs is refused, and the refusal prints the right name.
- **An agent a harness spawns** carries the label `<build> · <scope> · <stage>`. The scope is the
  unit it serves, the units of a spec writer's group, or a review's kind and round, as in
  `aOrientedCast · diff-review round 1 · synth`.
- **A harness run** keeps its script's name, `unattended-build`, `unattended-unit` or `tier2-review`:
  the tool fixes a run's title from the script's `meta` block, and no call can change it. The run
  says what it is in its first log line, `<build> · <scope> · <action>`, and in the `identity` field
  that leads its return.

## What each agent line tells you

The main session reports every agent it dispatches or receives with two lines. It pastes them
unchanged from `handoff.py agents --handoff <path>` for an agent it spawned itself, or from
`handoff.py agents --run <run-id>` for a harness run.

- **The `agent` line** says which role ran and at what effort and model. It also gives the unit or
  label it worked on, the prompt file it was handed, the file class it may write and the gate legs
  it may run. A harness agent's unit comes from its label: the one unit id the label names, else the
  whole label. It ends with the run and the agent's id, or `direct` for an agent spawned without a
  harness.
- **The `returned` line** appears once the agent has finished. It says what the agent produced:
  `committed <sha>`, `not committed`, `failed`, or how many files it wrote. It then gives the wall
  time, the output tokens and the same run and agent id.
- **`unknown`** means nothing has recorded that field yet: for example, a model the agent has not
  replied with and its call did not report. Such a line is not added to the ledger until a later
  run fills the field.
- **The ledger.** A run with `--write` adds every complete line once to the build's agent ledger,
  `<memory root>/builds/<slug>/build/<date>-build-<unit id>-agent-ledger.md`. One ledger per build
  holds every agent of that build, in the order the lines were added. A run without it writes
  nothing, so a mid-pass call leaves your tree clean; pass `--write` only at a bookkeeping step,
  when no pass is running.

## When no role agent can be spawned

Inline work is refused: the main session does not write a spec, review one, build a unit or run the
closing review itself. The one exception is a tool or run that cannot spawn a role agent at all, and
only where an owner has waived it in `role-stand-in-waiver.txt` under `<memory root>/project/`,
which holds an owner's row per build and role. A stand-in declares itself by rendering the role's
handoff with `handoff.py render ... --stand-in`. A waiver never admits a write the hooks refuse. For
the row grammar, read the roles README's "Standing in for a role" section; no tree holds the registry
until an owner writes its first row.

## What the hooks refuse

- An `Agent` call whose type is not a `gov-*` role, or whose prompt is not a rendered handoff.
- A misnamed spawn: an `Agent` call whose `description` is not the name `handoff.py render` printed.
- A `Workflow` call that runs anything other than a listed harness with its `roles` argument.
- A spec write from anything but the spec writer, and a product write from anything but the builder
  on a specced unit. The main loop may still flip a spec's `**Status:**` line.
- A role agent running the bar, the self-test runner or any suite, beyond what `[gates]` allows.
- In a session routed to a live build, a final message that leaves out the `agent` or `returned`
  line of an agent its turn dispatched or received. It is refused once per turn end, and
  `handoff.py agents` prints the lines to paste. This one switches on with the route, not with
  `roles.json`, and only where the governing doc's micro-formats define both lines.

All of these switch on only where `.claude/roles.json` exists. They do not see writes made through
Bash or PowerShell, `--bare` runs, agents a harness spawns internally, session-to-session messages,
or a hand-edited `roles.json`.

## In a repository that adopts the kit

`govkit apply` installs it by default, and `govkit update --write` adds it to older installs. It
needs the kickoff and memory-tree kits.

- The base roles, workflow table and scripts are the kit's and are replaced on every update.
- The overlays and `policy.toml` are seeded once and then belong to the adopter.
- `adopt-roles.sh --scaffold` renders the `/build` Skill, the agent types and `roles.json`. With no
  governing doc at the memory-tree conf's `CHARTER`, it renders the Skill alone and exits 3, and no
  hook check turns on.
- The `/build` Skill names each harness where the install holds it. Only
  a `workflow`-driver harness of the workflow table resolves as the role index does, from the tool
  root, so a kit govkit landed under its id is named there. Every other tool-root citation of the
  template, the merge bar's among them, resolves from the roles kit directory as `derive_kit_paths`
  resolves a rendered guide's: a receipt row can place it, and at a prefixed install a file at the
  repository root never answers it. The plain prefix fills whatever neither holds. `apply` runs the
  adopter before the harnesses are rendered, so a first install names the plain path until the next
  `--scaffold`, which `govkit update` runs; `--check` reads the Skill out of sync until then.
- `/build`'s harnesses ship in the `review-harness` kit, which is not a default. Without it the role
  agents and handoffs still work, and three tools print a note naming the missing harness: the
  catalogue checker `check_roles.py`, `render_agents.py`, and check-wiring's session-start report.
  `render_agents.py`, run by `adopt-roles.sh --check` and the `roles render wiring` leg, is the one
  reader that prints `misplaced`. It does so for a harness the index lists where it is absent, while
  a file of its name sits directly inside a directory under the tool root beside the harness's
  template or a `kit.toml` declaring its home: its kit holds it elsewhere, and the leg fails on it.
  A harness its kit ships with no template, `unattended-unit.js`, is marked by `kit.toml` alone. A
  file of its name beside neither mark is not counted as its kit's, and reads as the note.
  check-wiring's note names `adopt-roles.sh --check` as the command that says which.
- The `[roles]` rule and the Agent roles section ship with template v4.4. The render reads the
  template the renderer kit ships beside its engine, so an update brings them; a copy seeded earlier
  at `playbook_path` is no longer read. Without the playbook renderer,
  fill `{{ROLE_ROSTER}}` from `python <prefix>/roles/handoff.py roster`. <!-- usage: script:tools/roles/handoff.py#roster 739c5825 -->
