# Role agents and `/build`

**What it is.** Every piece of LLM work in a governed repository runs as a declared workflow:
orientation, research, reuse, spec writing, spec review, building, the closing review, the gate bar,
handoffs and bookkeeping. Spec writing, spec review, building and the closing review run only inside
role agents. The main session orients, hands work off and keeps the records. Hooks refuse the
bypasses, so this holds without anyone remembering it.

The kit is `<prefix>/roles/`, which is `tools/roles/` in this repository. Its README is the full
reference; this page is the short version.

## How a task reaches an agent

1. **Kickoff writes the card.** Its `## task` block carries the goal, scope, cut-line, To-do, Reuse,
   acceptance check and gates.
2. **A role supplies the constant part.** Each role is one file under `<prefix>/roles/agents/`: its
   instructions, the inputs it reads, the file class it may write and the charter's section 1 rule
   tags it needs, under `rules`. Its agent carries those rule lines and the charter's Protocols and
   Facts sections whole.
3. **The handoff renderer joins them.** `handoff.py render` writes one prompt file under the build's
   `prompts/` folder, with `## Role` and then `## Task`, filled from the card, the build's brief and
   any `--input` values. A required input that is missing or still a placeholder refuses by name.
4. **The agent runs as a native type.** Each role is rendered into `.claude/agents/gov-<role>.md`,
   which starts without the full charter and at the reasoning effort the policy file sets.

## How to use it

- **Run an attended build:** after kickoff's READY card and the owner's go, invoke `/build`. It walks
  the workflows in stage order and calls the same harnesses `/unattended` uses.
- **Hand one task to one agent:**

  ```bash
  python tools/roles/handoff.py render --role gov-builder --build <slug> --unit <unit-id> --part task
  ```

  Pass that output, unchanged, as the prompt of an `Agent` call whose `subagent_type` is
  `gov-builder`. An edited prompt is refused.
- **Change how a role behaves:** edit `<prefix>/roles/house/<role>.md`, never the file under
  `agents/`. Your overlay is appended under `## House rules`, and updates never overwrite it.
- **Change a role's effort, or the gates a role may run:** edit `<prefix>/roles/house/policy.toml`.
  Its `[effort]` tables set levels per role and per harness stage; its `[gates]` table lists the
  only gate legs a role agent may run.
- **After any change to a role, overlay or policy:** run `python tools/roles/render_agents.py --write`,
  then start a new session. A running session cannot spawn an agent type written after it started.

## What the hooks refuse

- An `Agent` call whose type is not a `gov-*` role, or whose prompt is not a rendered handoff.
- A `Workflow` call that runs anything other than a listed harness with its `roles` argument.
- A spec write from anything but the spec writer, and a product write from anything but the builder
  on a specced unit. The main loop may still flip a spec's `**Status:**` line.
- A role agent running the bar, the self-test runner or any suite, beyond what `[gates]` allows.

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
- `/build`'s harnesses ship in the `review-harness` kit, which is not a default. Without it the role
  agents and handoffs still work, and each tool prints a note naming the missing harness.
