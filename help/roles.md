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
   where its output goes, under `output`. Its limits are under `never`, each paired with the hook,
   gate leg or stated absence that enforces it, and what it hands back is the typed template under
   `return`, which always holds a closed `outcome`. Its agent carries those rule lines and the
   charter's Protocols and Facts sections whole, and its role text closes with `## Never`,
   `## Ceiling` (its tools, its write class and the gate legs it may run) and `## Return`.
3. **The handoff renderer joins them.** `handoff.py render` writes one prompt file under the build's
   `prompts/` folder, with `## Role` and then `## Task`, filled from the card, the build's brief and
   any `--input` values. A spec writer's task also carries the brief's `## The prompt`, the owner's
   own words, as its `brief:prompt` block. A role reading `upstream:rows?` is handed, beside any
   `--input`, the rows file `--upstream` names: the commitments its upstream items established, which
   the loop kit's `upstream.py rows` prints, then the line telling the agent to answer each row
   `used`, `bypassed` or `not-applicable` in its return. Without `--upstream` the task names the key as
   not supplied; for a role not reading it, `--upstream` is refused. A required input that is missing
   or still a placeholder refuses by name. The prompt carries no charter text: the charter rides once, in the agent file.
   Every value is handed as its content, never as a path the agent must open: `--input spec=<path>`
   and `--input prompt=<path>` hand the file's text. Each block opens with one fact line,
   `<!-- gov:fact key=<key> class=<class> -->`. The key names what the value was cut from:
   `record:<path>@<12 hex>` for a record or the card, `blob:<path>@<12 hex>:1-<n>` for `input:code`,
   `cmd:` for a typed argument. The class, `witnessed`, `decided` or `claimed`, is derived from the key
   and its source, never typed. The content follows its fact line inside a fence of backticks one
   longer than any backtick run it holds, so a fact line or `gov:handoff` marker line the content
   quotes, as a spec often does, is read as text, never as a fact or a marker. A typed value,
   `--input question=` or `--input diff=`, is your own text and is written without a fence. A line
   of it that reads as a heading, a fact line, a `gov:handoff` marker line or a `Framed by:` line is
   refused, naming `input:<name>` and the line, and so is a fence it opens and never closes. To quote
   such lines, hand them in a file with `--input spec=<path>`. The task is checked block by block:
   a render in which a block would start inside a fence an earlier block left open, a handed block's
   content would be read outside its own fence, or the task would end inside an unclosed fence is
   refused, naming the block and the line, and nothing is written. `handoff.py facts --build <slug> --unit <id> --input prompt=<brief>
   --input spec=<spec>` prints the same cut as one JSON list for a caller that hands it on: the unit
   harness takes it as `facts` wherever `roles.builder` travels, and refuses a call without it.
   Its `gov:handoff` marker line names the item the work order was cut for as `item=`: pass
   `--item <tag>`, a tag in the `item.<step>.<name>` shape, or the marker reads `item=-`. A tag in
   any other shape is refused and nothing is written.

   With `--item`, the render reads that item's row from the loop definition and cuts the work order
   for it. The item must be declared there and its actor must be the role you render, else it is
   refused and nothing is written; so is a render with no loop kit installed. The task then ends
   with five blocks: `### item` (the tag, its step and its outcomes), `### inputs` (each input the
   item reads, handed as content under its own heading), `### allowance` (the paths the role may
   write), `### return` (what to hand back) and `### witness` (what proves the work was done). The
   allowance follows the role's write class: a role writing specs gets the build's `spec/` folder,
   one writing reviews its `reviews/` folder, one writing records the memory root, and an item
   narrowed to `none` writes nothing. A builder's item writes product files, and you grant each
   path with `--allowance <path>`, repeated: pass the files the unit's dispatch declared, never a
   whole product folder. With no `--allowance`, or a path outside the conf's `ROUTED_PATHS`, the
   render is refused. `handoff.py check <file>` refuses an item's work order missing any of the five
   blocks. The spawn guard admits that work order only in a session whose orientation card routes
   its unit; from any other session the `Agent` call is refused, naming the unit and the card.

   A research return records the work order it answers as `**Answers:** <work order path>
   task-sha=<12hex>`, beside its `**Serves:**` line, the `task-sha` copied from the work order's
   marker. `check_roles.py`'s R16 refuses a work order whose marker carries no `item=`, and a return
   with no such line, one naming another work order or one whose `task-sha` differs. The paths
   `work-order-legacy.txt` lists, the records written before the rule armed, are not refused.
4. **The prompt writer frames the task: render it with `--for`, spawn it, render the role with `--framed-by`.**
   While the policy key `prompts.author` is `prompt-writer`, its default, a direct spawn of any role
   takes these three calls. First `handoff.py render --role gov-prompt-writer --for <role> --build <slug>
   --unit <id> --input question=<your details>`, adding the `--input` values the role reads, and spawn
   the prompt writer with that task and the name it prints. `--for` hands it your details under
   `input:question` and the role's whole work order under `input:work-order`: its role text, every input
   it reads, its allowance and its return template. Only `--for` fills that input, and
   `--input work-order=` is refused. The prompt writer writes nothing. It returns `framed` with `job` and
   `nostop`, and `population` and `added` where it has them, or `refused` with `why`. Then
   `handoff.py render --role <role> ... --framed-by <the prompt writer's agent id>` reads that return
   from the prompt writer's own transcript in your session, so you retype none of it, and you spawn the
   role with that task. The agent must be typed `gov-prompt-writer`, its first message a prompt writer's
   work order of the same build, and its return must pass the return check with `outcome` `framed`,
   `job` and `nostop`; anything else is refused, naming what failed. The role's task then ends with one
   block per field, `### framing:job`, `### framing:population`, `### framing:added` and
   `### framing:no-stop`, each holding the field as the prompt writer wrote it, and the job block closes
   with `Framed by: <the prompt writer's prompt path> task-sha=<12hex>`. The blocks sit inside the bytes
   the task-sha covers. The prompt writer's own task is your details as you gave them, and is never
   framed. Under `requesting-worker-rendered` you render the role's task yourself, with no
   `--framed-by`. A handoff to another session, `gov-session`, takes no prompt writer.
5. **The agent runs as a native type.** Each role is rendered into `.claude/agents/gov-<role>.md`,
   which starts without the full charter and at the reasoning effort the policy file sets. It
   carries the practices its role cites and the charter's Protocols and Facts sections, first.
   The dispatcher passes the level for the model in use: a harness call carries `efforts`, the JSON
   `handoff.py stage-efforts <workflow> --model <id>` prints, where `<id>` is the session's own
   model id as its environment states it. A harness call at another level is refused by the spawn
   guard, which names the stage, both levels and that command; pass what it prints. A stage that
   neither `roles` nor `efforts` names is refused too. A harness call also carries `retries`, what
   `policy.py get roles.retries` prints: a stage outside a fan that returns nothing is spawned again
   up to that many times, at most 4, and a value that is no integer in that range is refused.
6. **Each block carries its level.** With the playbook kit installed, every block a subagent gets
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

Each workflow has a reach word, the step its work orders load practices at: `entry`, `plan`, `design`,
`build`, `test`, `deploy`, `review`, or `none`. It is the loop definition's, `<prefix>/loop/loop.toml`,
and no key of the roles kit: the workflow's row there gives it as `reach` where it carries one, else as
the last word of its `step` ([the loop definition](loop.md)). A work order carries what each active
practice changes at its role's step: the handoff's task section ends with a `### Practices at <step>`
block, one `- [<name>] <reach>` line per practice that reaches that step. A builder's reads, for example,
`- [yagni] delete rather than disable`. The charter keeps one line per practice and carries no reach.

The active practices are the policy key `charter.practices`, the foundation set when unset. A step of
`none`, a step no active practice reaches, or an install with no playbook kit or no loop kit renders no block.
`python <prefix>/playbook/load_sets.py derive --reader role.<name>` lists the units as <!-- usage: script:tools/playbook/load_sets.py#derive c95f3b73 -->
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
  the workflows in the order the loop definition gives them, each workflow's `order` in
  `<prefix>/loop/loop.toml`, and calls the same harnesses `/unattended` uses.
- **Check a spec before it is committed:** a spec writer runs
  `unattended.sh --check-specs <slug> <unit>` before returning, and the spec commit refuses on it. <!-- usage: verb:unattended.sh:--check-specs 131e24bd -->
  It prints each refusal `--dispatch` would make from the spec files, in its words, so a defect is
  fixed before the spec commit rather than after a builder was dispatched.
- **Hand one task to one agent:**

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and placeholders -->
  ```bash
  python tools/roles/handoff.py render --role gov-builder --build <slug> --unit <unit-id> --part task
  ```

  Pass that output, unchanged, as the prompt of an `Agent` call whose `subagent_type` is <!-- usage: script:tools/roles/handoff.py#render 6d672651 -->
  `gov-builder`. An edited prompt is refused. Pass the name it prints on stderr after
  `handoff: description — ` as the call's `description`; any other name is refused.
  That `Agent` call also carries `effort`: the role's value in the JSON
  `handoff.py role-efforts --model <id>` prints. A spawn at another level is refused, and the
  refusal names the level to pass and that command. The guard reads the model from the call's
  `model`, else from the session's transcript. When it cannot read one, or two profiles match it,
  or `CLAUDE_CODE_EFFORT_LEVEL` is set, the call goes through with one line saying the level was not
  checked. It does not check the agents a harness spawns itself, the `committer` and `probe`
  stages, which workflow a call to a harness serving two runs, a default subagent model or an
  effort ceiling in your settings, or a role index edited by shell.
- **Change how a role behaves:** edit `<prefix>/roles/house/<role>.md`, never the file under
  `agents/`. Your overlay is appended under `## House rules`, and updates never overwrite it.
- **Change a role's effort or model:** set a key in `.governance/policy.toml` and commit it:
  `roles.effort.<role>`, `roles.effort.<workflow>.<stage>` for one harness stage,
  `roles.effort.default` for every role, or `roles.model.<role>.claude-code`. A set key wins over
  `<prefix>/roles/house/policy.toml`, whose `[effort]` tables set levels per role and per harness stage
  where no key is set; with neither, a role runs at the `effort` its role file declares.
- **Change the gates a role may run:** a role's `gates` field lists the only gate legs its agent may
  run, and a `[gates]` row of the house file applies only to a role carrying no such field.
  `gov-spec-writer` and `gov-builder` carry theirs as fields, so a house row does not change them.
- **Give a model its own levels:** add one `[effort.profiles.<name>]` table to the same file, with
  `match`, the words of the model id it answers, and `default`; `roles` and `stages.<workflow>`
  tables under it are optional. No code changes. The seeded `[effort.profiles.fable]` runs every
  role, and every stage a workflow's `stages` table keys, at `medium` on any Claude Fable version. A profile reaches an agent only through
  the two calls above, never through its rendered agent type, so it takes effect on the next call
  with no re-render and no new session.
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
- **The record.** So that a call reads only what the session added since the last one, the verb
  keeps one record per session file in `handoff-calls/` under the repository's git common dir, the
  `.git` folder every worktree shares. The folder may be deleted at any time: the next call reads
  the whole session again and prints the same lines. A record from another version of the verb, or
  for a session file that was edited, is never used.

The `gov-tester` role judges a red the bar attributed to this build: the Test step hands it an OWN or
blocking MIXED red, and it answers whether the code missed or the spec was wrong, with an outcome of
`code-miss` or `spec-wrong`. It writes nothing. <!-- usage: agent:gov-tester -->

The `gov-reviewer` role reviews a spec set or a diff through one lens, read-only; it replaced the
separate spec and diff reviewer roles, and both review stages spawn it. It writes nothing.
<!-- usage: agent:gov-reviewer -->

The `gov-prompt-writer` role frames the task a role agent is handed. It is a cycle role: the
driver calls it around an item, and no checklist item names it as its actor. It writes nothing: the
prompt writer's route, `--for`, its spawn, then `--framed-by`, is step 4 of "How a task reaches an agent".
<!-- usage: agent:gov-prompt-writer -->

The `gov-planner` role drafts and judges a build's plan, and the `gov-architect` role inventories a
build's scope and decomposes it into units. Both write records only, under the build's folder.
<!-- usage: agent:gov-planner --> <!-- usage: agent:gov-architect -->

## When no role agent can be spawned

Inline work is refused: the main session does not write a spec, review one, build a unit or run the
closing review itself. A stand-in declares itself by rendering the role's handoff with
`handoff.py render ... --stand-in`, and the policy key `roles.no-spawn` decides whether that render
is admitted at all:

- `executor-role-session`, the default: every `--stand-in` is refused. The refusal names the route
  that is always open, spawning the role through an `Agent` call or a listed harness. An item no
  agent can take goes to a role session that an executor starts, and that executor is
  dWellOiledMachine's, not yet built.
- `refuse`: every `--stand-in` is refused, naming the key.
- `recorded-stand-in`: a stand-in is admitted only where an owner has waived it in
  `role-stand-in-waiver.txt` under `<memory root>/project/`, which holds an owner's row per build
  and role.

So under the default a waiver row alone admits nothing: set `roles.no-spawn = "recorded-stand-in"`
through the policy file's one door, `policy_edit.py`, first. Where the policy kit is not installed,
the waiver row decides, as before the key. A waiver never admits a write the hooks refuse. For the
row grammar, read the roles README's "Standing in for a role" section; no tree holds the registry
until an owner writes its first row.

## What the hooks refuse

- An `Agent` call whose type is not a `gov-*` role, or whose prompt is not a rendered handoff. Each
  such refusal ends by naming the policy key `prompts.author` and its value: `prompt-writer`, the
  default, or `requesting-worker-rendered`. Under both, the prompt must be a handoff that
  `handoff.py render` produced.
- An unframed spawn under `prompt-writer`: an `Agent` call of any role but `gov-prompt-writer` whose
  task carries no single `### framing:job` block, no single `Framed by:` line inside it, or a
  `Framed by:` line naming anything but a prompt writer's work order under the build's `prompts/`
  folder whose marker holds that task-sha. The refusal names the key, its value and the prompt
  writer's three calls: render it with `--for`, spawn it, render the role with `--framed-by`.
- A misnamed spawn: an `Agent` call whose `description` is not the name `handoff.py render` printed.
- A stale handoff: an `Agent` call whose handoff was rendered from role text other than the text its
  agent type was rendered from. The marker's `role-sha` must equal the `role-sha` the role index
  holds for that role; the refusal names both values. Re-render the handoff, or the index with
  `render_agents.py --write` where the role changed after it. An index holding no `role-sha` for the
  role, as one rendered before the key existed does, refuses every spawn of it until it is re-rendered.
- A handoff whose handed fact moved: a `blob:` or `record:` key whose source now holds other bytes
  than the ones it was cut from, or none. The refusal names the key and both blob ids. Re-render the
  handoff, which cuts it fresh. A handoff rendered before fact lines existed carries none and passes.
  A fact line or marker line inside a fence is content and is neither re-cut nor counted.
- A handoff whose `## Task` section ends inside a fence that never closes. The refusal names the line
  of the file the fence opened at. Re-render the handoff.
- A handoff whose typed block, `### input:question` or `### input:diff`, holds a fact line, a
  `gov:handoff` marker line or a `Framed by:` line, inside a fence or not, or leaves a fence open. The
  refusal names the block and the line of the file. Correct the value and re-render the handoff.
- A handoff whose fences were moved across its blocks: a fact line that does not sit two lines below
  its block's heading, or a handed block whose content does not sit inside its own fence, or whose
  fence is followed by anything but blank lines before the next block. The task envelope's closing
  line may follow the last one. The refusal names the block and the line of the file. Re-render the
  handoff.
- A tool write to `.claude/roles.json`, or to the agent file `.claude/agents/<role>.md` of a role the
  index names, from any writer, the main session included. `render_agents.py --write` is their one
  writer. Your own files under `.claude/agents/` are not affected. The policy kit's commit guard also
  admits a commit of these files only as `render_agents.py --write` leaves them.
- A `Workflow` call that runs anything other than a listed harness with its `roles` argument.
- A role agent's direct return that fails its role's `return` template: no `json` block or
  `key: value` fields to read, a required field missing, a field the template does not name, a value
  of the wrong type or outside its set, a `sha` naming no commit, a `path` naming no file, or an
  `answers` naming another work order. The stop is sent back to the agent with every defect named, up
  to `roles.retries` times (3 unless your policy file sets it); after that the stop goes ahead and the
  record under `.git/return-check/` says the return stayed invalid. A failed check never blocks a stop.
  <!-- usage: hook:return-check 2329c48d -->
- A spec write from anything but the spec writer, and a product write from anything but the builder
  on a specced unit. The main loop may still flip a spec's `**Status:**` line.
- Any file write from a role declaring `writes = none`: such a role writes nothing in the repository.
- A write from a role declaring `writes = review` outside a build's reviews folder,
  `<MEMORY_ROOT>/builds/<slug>/reviews/`. A review harness run with its default `reviewDir` is
  refused there; pass `reviewDir` under that folder. Where `roles.json` was rendered before it held
  the `classes` map that spells the folder, every such write is refused until
  `render_agents.py --write` re-renders it.
- A role agent running the bar, the self-test runner or any suite, beyond what its grant allows.
  A gate run by its full path from a directory outside every checkout is judged by the index of the
  checkout that holds the script. Where neither sits in a checkout, no grant can be read, so the bar
  runners and the suites are refused there with or without `roles.json`.
- A role agent's polling wait: a `tail` that follows a file, a `sleep` inside a `while`
  or `until` loop, or a `sleep` of 5 s or more.
- In a session routed to a live build, a final message that leaves out the `agent` or `returned`
  line of an agent its turn dispatched or received. It is refused once per turn end, and the
  refusal prints the lines to paste, derived for it by `handoff.py agents`; where it cannot derive
  one, it names that verb instead. This one switches on with the route, not with
  `roles.json`, and only where the governing doc's micro-formats define both lines.

All of these switch on where `.claude/roles.json` exists. Where it is missing but `.claude/agents/`
still holds an agent file the kit rendered, the hooks refuse every spec and product write, every
other file write from a role agent, every role agent's gate run and every `Agent` and `Workflow` call, naming the index, until
`render_agents.py --write` restores it. In a repository that never adopted the kit, a missing index
switches nothing on.

The main session's reads are held too, by the policy key `driver.reads`, wherever the policy kit is
installed, with or without `roles.json`. Under its default, `state-reads-only`, the main session's
`Grep` and `Glob` are refused: a search is a scout's task. The refusal names the key, its value and
the remedy, dispatching the `gov-researcher` role through a rendered handoff. Its `Read` of a named
file is still admitted. Under `none-scout-only` its `Read` is refused too. Under `read-only-probes`
all three are admitted. A role agent's reads are never refused by this key. Without the policy kit,
every read is admitted with one stderr line saying `driver.reads unarmed`. To change the value, set
it through the policy file's one door, `policy_edit.py`.

A role agent's writes made through Bash or PowerShell are held too. A redirect, `tee`, `touch`,
`mkdir`, `cp`, `mv`, `sed -i`, `perl -i`, `git apply`, or a literal write call inside `python -c`,
`node -e` or a `python -` heredoc meets the same refusal an `Edit` of that file would. Where the
agent's work order hands an allowance, the write must also lie under one of its paths; an allowance
of `none` admits no write in the repository. With no allowance found, the write is held to the
role's write class alone. The refusal names the file, the shell shape and the allowance, and leaves
the remedy to whoever dispatched the agent: re-scope the work order, or route the write to a role
whose class covers it.

The hooks do not see the main session's shell writes, its `grep`, `find` or `cat` run through
Bash, a write made from inside a script file a command runs, a path built at run time (a variable
or a joined path), `rm`, `git checkout`, `git restore`, `git stash`, a patch piped into
`git apply`, `--bare` runs, agents a harness spawns internally, session-to-session messages, or a
`roles.json` the main session edited by shell and never committed. A word such as `install` or
`touch` left unquoted as an argument, as in `grep -n install notes.md`, reads as a write; quote it.

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
