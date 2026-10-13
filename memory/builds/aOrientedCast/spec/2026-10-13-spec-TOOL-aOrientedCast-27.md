# TOOL-aOrientedCast-27 — every spawned agent is named for its build, unit and action, and the spawn guard refuses a misnamed spawn

**Status:** OPEN · rev-1 · 2026-10-13 · node a · Tier-2 · base 646d4a73 · streams tooling · order 28 · ratified 2026-10-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aOrientedCast-27-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-27-1-spec-brief.md) | journal | TOOL-aOrientedCast-25 |
| [2026-10-13-prompt-TOOL-aOrientedCast-27-2-spec-writer.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-27-2-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The owner's fifth addendum asks that every spawned agent's name say what it is doing now: the
build's slug, the unit id and the action. Today a `gov-spec-writer` spawn kept the description "Fold
two specs, spec three units" across later work, and harness agents carry labels such as `synth` that
name neither the build nor the round. This unit derives a direct spawn's name from its handoff,
prints it from the renderer, and has the spawn guard refuse an `Agent` call whose `description` is
not that name. It gives every agent of the three declared harnesses a label of the same three parts,
and the agents verb then reads a unit id from every harness label that names one unit.

## 2. Scope (IN)

- **S1** — `handoff.py render` prints on stderr one line, `handoff: description — <name>`, carrying
  the name of §4 "The spawn name", which `render_spawn_name` builds from `--build`, `--unit` and the
  role's catalogue `workflow`. It prints in every mode except `--stand-in`, after the library notes,
  and its stdout does not change in any mode. Observed by AC1 and AC5.
- **S2** — Rule 6 of `tools/hooks/agent-cap.js` gains a last step on an `Agent` call, §4 "The hook":
  the call's `description`, its ends trimmed, must equal the name `renderSpawnName` derives from the
  prompt's marker and the role index's `workflow` for the `subagent_type`. An index role with no
  `workflow` string refuses, naming the index. The refusal names the call's description and the
  expected name, and the rule's shared spawn route names the description. Observed by AC2, AC3, AC4
  and AC5.
- **S3** — Every `agent()` call of `unattended-build`, `unattended-unit` and `tier2-review` carries
  the label of §4 "Harness labels", in each template and its render alike. A harness's `pending`
  list and its log lines keep the stage keys they print today. Observed by AC6, AC7, AC8 and AC10.
- **S4** — `handoff.py agents` fills `<unit-id|label>` for a harness agent through
  `extract_label_unit`: the one distinct unit id its label names, else the label. Observed by AC9.
- **S5** — The suites follow §4 "The suites": the agent-cap suite's spawn payloads carry a
  description and gain the description arms; the roles suite's arm 6 sends the renderer's name, its
  new arm 12 grades `extract_label_unit`, and every `Agent` payload it hands the hook carries a
  description; the two harness suites' stub runners key on the stage and keep the whole label; and
  each floor rises by the assertions its suite gains. Observed by AC5 for arm 6. The rest is NOT
  OBSERVED by a criterion of its own: a pass runs no suite, and the main loop observes each suite
  edit at the close under §7's `New arm:` lines.
- **S6** — The prose of §4 "Documentation", the `help/roles.md` page among it. Observed by AC11.
- **S7** — The hooks, roles and review-harness kits each move one version step with every carrier,
  as §8 F1 resolved it. Observed by AC12.
- **S8** — The roles dossier gains this unit in `decisions` and a sentence, the review-harnesses
  dossier gains a sentence, and the generated map is re-rendered; the agent-cap dossier is left as it
  is. Observed by AC13.

## 3. Non-goals (OUT)

- Renaming an agent that already ran, or rewriting a past line of the agent ledger.
- A `Workflow` run's own title. The tool takes it from the script's static `meta.name`
  (`unattended-build`, `unattended-unit`, `tier2-review`), and a call carries only `scriptPath`,
  `script`, `name` and `args`, none of which sets a title (§4 "Evidence"). The run's agents carry
  the new names; the run keeps its script's.
- Re-opening an owner ruling of this build.
- Checking a harness agent's label at run time. An `agent()` call is a runtime call and not a tool
  call, so no hook sees it (`TOOL-aOrientedCast-7` §3). The two harness suites hold the labels.
- Labels in the workflow scripts that are not declared harnesses: the drift-audit workflows and the
  orientation counterfactual, which rule 6 already refuses to start.
- A message to an agent already running. It is not an `Agent` call, so a name is set by the spawning
  call alone.
- What a harness returns. The review harness's `pending` keeps its stage keys, so no caller changes.
- The `unattended-build@` and `unattended-unit@` identity markers, which this build's earlier
  harness units left as they were (§4 "Kit versions").

### Edges

- **consumes-from** external — the `Agent` tool's `description` input, which reaches a PreToolUse
  hook as `tool_input.description`, measured on Claude Code 2.1.295 (§4 "Evidence"). Without it
  every spawn in an armed tree is refused at S2's step, which fails closed.
- **hands-off** external — naming the agents of the workflow scripts that are not declared
  harnesses, once a later build declares them.

## 4. Design

Line numbers were read at `aa561ec9f`, the run branch's HEAD on 2026-10-13, where
`TOOL-aOrientedCast-24` and `TOOL-aOrientedCast-25` are OPEN and unbuilt. Both write files this unit
writes (§4 "Rollout"), so the builder finds each site by its content, not its number.

### Evidence

- The `Agent` tool input carries `description`, `prompt`, `run_in_background` and `subagent_type`,
  and every `Workflow` input carried `args` and `scriptPath`. Read from the 55 `Agent` and
  `Workflow` tool-use blocks of this build's own session transcript, Claude Code 2.1.293 to 2.1.295,
  PINNED on 2026-10-13. The `gov-spec-writer` spawn the owner quotes carried the description "Fold
  two specs, spec three units".
- Rule 6 on an `Agent` call is `checkHandoffSpawn` (`tools/hooks/agent-cap.js:2086-2135`). Its last
  step compares the task section's digest with the marker's `task-sha`, then admits (`:2132-2134`).
  The marker regex holds `build` and `unit` (`:2041`, `:2050`), `renderHandoffDeny` carries the one
  route every spawn refusal prints (`:2074-2083`), and the header states the rule (`:39-50`).
- `loadRoleIndex` grades a role's `writes`, `agent` and `gates`, never its `workflow`
  (`tools/hooks/scratch-guard.js:952-989`). The agent renderer copies every role's `workflow` from the
  catalogue into the index (`tools/roles/render_agents.py:168`), and the catalogue requires the key
  (`REQUIRED_ROLE_KEYS`, `tools/roles/check_roles.py:95`, and R7). Gov's index maps its ten roles to
  `build`, `closing-review`, `orient`, `research`, `reuse`, `handoff`, `spec-review` and `spec-write`.
- `render` reads the role's keys (`tools/roles/handoff.py:997`), writes the marker with
  `unit or "-"` (`:397-398`), prints the library notes on stderr (`:1019-1020`), and writes the path,
  the task part or the whole file on stdout (`:1028-1029`). The `/build` Skill tells the main loop to
  pass that stdout unchanged as `prompt` (`tools/roles/SKILL.template.md:22-26`).
- The agents verb takes a harness agent's unit as the first `LABEL_UNIT_RE` match in its journal
  label (`tools/roles/handoff.py:113`, `:862-863`), so a label naming two units reads as its first.
- No gate or hook reads an agent label: a search for `label` over the hooks, the workflows kit's
  gates and the unattended, run-log and memory-tree kits finds no reader. The review harness builds
  `pending` from its stage keys, apart from the labels (`tools/workflows/tier2-review.template.js:1155`,
  `:1278`, `:1568`).
- Both harness suites key their stubs and trace lines on the label: `runReview`
  (`tools/workflows/tier2-review.test.sh:252-273`) and `run_wf`
  (`tools/workflows/unattended-build.test.sh:157-231`). PINNED at `aa561ec9f` by `grep -oE` over the
  build suite: 74 trace reads spell a slug, a round, a group or a unit inside a label.
- The roles suite builds its one hook payload at base in arm 6
  (`tools/roles/adopt-roles.test.sh:106-143`), with no description. `TOOL-aOrientedCast-25` adds arm
  11, which sends more.
- Each harness's `meta.name` is a literal (`tools/workflows/unattended-build.template.js:2`,
  `tools/workflows/tier2-review.template.js:2`, `tools/workflows/unattended-unit.js:66`).

### The spawn name

```
<build> · <unit> · <workflow>     the marker names a unit
<build> · <workflow>              the marker's unit is -
```

The parts are joined by a space, U+00B7 MIDDLE DOT and a space, the separator the agent lines
already use. `<build>` and `<unit>` are the marker's. `<workflow>` is the role's `workflow` key: the
renderer reads it from the catalogue, and the hook reads it from the index the catalogue renders, so
one source has two readers. The unit-less form leaves the part out rather than print `-`. This
unit's own spawn is named `aOrientedCast · TOOL-aOrientedCast-27 · spec-write`.

Two functions build it, `render_spawn_name(slug, unit, workflow)` in `handoff.py` and
`renderSpawnName(marker, workflow)` in `agent-cap.js`, because a kit file imports no sibling kit.
Arm 6 of the roles suite holds them to one answer: the renderer's printed name must pass the hook.

### The renderer

In `main`, after the notes loop and before stdout is written, unless `--stand-in` was given, print
`handoff: description — ` and `render_spawn_name(a.build, a.unit, keys["workflow"])` as one stderr
line. stdout and the written file do not change in any mode. A refused render exits before this line,
and a stand-in spawns nothing, so neither prints one.

### The hook — rule 6, step 2.10

Inserted after the digest step of `checkHandoffSpawn`, so the remedy it names is the description
alone. The old step 10, which admits and lets rule 4 claim the slot, becomes step 11.

1. `index.roles[type].workflow` is not a non-empty string → deny: `<index> declares no workflow for
   <type>, so this spawn's name cannot be derived; re-render the role index.`
2. `want` is `renderSpawnName(m, workflow)`. `ti.description` is not a string, or its trimmed value
   is not `want` → deny: `the call's description <its JSON, or null> is not this handoff's name
   <JSON of want>: the marker's build and unit and the <type> role's workflow. Pass description
   exactly as handoff.py render prints it.`

`JSON.stringify` keeps the middle dot as written, so the name in a refusal can be copied. The shared
`Agent` route of `renderHandoffDeny` gains "and `description` the name it prints on stderr" after its
`subagent_type` clause. A refusal sits inside rule 6, so it claims no slot (`TOOL-aOrientedCast-7`
S1). The header's rule 6 paragraph gains the description clause.

The step stops a stale or freeform name, never a forged one: any caller can copy the right name. That
is the posture rule 6 already states for its prompt check.

### Harness labels

Every label is `<slug> · <scope> · <stage>`. The scope is the unit id where the stage serves one
unit, the ids of its group where a spec writer serves several, and else the stage's scope.

| Harness | Stage | Label at base | Label after |
|---|---|---|---|
| `unattended-build` | spec writer, group g | `spec:<slug>:g<g>` (`:995`) | `<slug> · <the group's unit ids> · spec-write` |
| | spec commit | `commit:specs:<slug>` (`:1212`) | `<slug> · specs · commit` |
| | audit subjects | `audit:subjects:r<n>` (`:1422`) | `<slug> · audit round <n> · subjects` |
| | audit record | `audit:record:r<n>` (`:1810`) | `<slug> · audit round <n> · record` |
| | disposal | `dispose:<slug>` (`:2045`) | `<slug> · audit round <n> · dispose` |
| `unattended-unit` | builder | `unit:<unitId>` (`:329`) | `<slug> · <unitId> · build` |
| `tier2-review` | resume probe | `resume:probe` (`:944`) | `<slug> · <kind> round <n> · resume:probe` |
| | finder | `find:<lens>` (`:1139`) | `<slug> · <kind> round <n> · find:<lens>` |
| | verify batch | `verify:ids-<a>-<b>` (`:1278`) | `<slug> · <kind> round <n> · verify:ids-<a>-<b>` |
| | synthesis | `synth` (`:1812`) | `<slug> · <kind> round <n> · synth` |

Line numbers are the templates'; each render holds the same lines.

- **`unattended-build`** defines `renderAgentLabel(scope, stage)`, returning
  `[slug, scope, stage].filter(Boolean).join(' · ')`. `slug` is the required argument (`:297`), the
  group's unit ids are joined by single spaces in roster order, and `<n>` is `roundNo` (`:349`).
- **`tier2-review`** defines the same function over `reviewSlug`: the segment after a `builds/`
  segment of the slash-folded `reviewDir` (`:529`), when it matches `[A-Za-z]+`, else empty, so a
  review outside a build folder carries no slug part. The scope is `reviewScope`, the run's `kind`,
  ` round ` and `round` (`:184`, `:307`). The stage is today's label, so `pending`, the log lines
  and every suite read of a stage keep their spelling.
- **`unattended-unit`** defines nothing, under its header's one-definition rule (`:20-26`). Its call
  carries `cfg.slug + ' · ' + cfg.unitId + ' · build'`.

A spec-writer group serving several units names them all, which is what the owner asked for. The
agents verb then reads a unit only from a label naming exactly one (S4).

### The agents verb

`extract_label_unit(label)` returns the one distinct `LABEL_UNIT_RE` match of `label`, else `None`.
`print_agent_lines` takes a harness agent's unit as `extract_label_unit(label)`, else the label, else
the meta's `description`, replacing the first-match read at `:862-863`. A label written before this
unit, such as `unit:TOOL-tFix-1`, still names one unit and reads as it did.

### The suites

- **The agent-cap suite.** `run_spawn` puts `description` into its payload, by default the name of
  the handoff its variant carries: `bx · T-1 · research`, or `bx · research` for a new unit-less
  variant `nounit` that `write_handoff` adds. `HO_DESC` overrides the default, and `HO_DESC=-` leaves
  the key out. New arms after AC5's block: the unit-less name is admitted; a missing, a freeform
  `Fold two specs, spec three units`, a wrong-action `bx · T-1 · build` and a wrong-unit
  `bx · T-2 · research` description each exit 2 naming `"bx · T-1 · research"`; `bx · - · research`
  on the unit-less handoff exits 2; and an index whose `gov-researcher` carries no `workflow` exits 2
  naming `workflow`. Each present admitted spawn carries the right name by default, so no present
  verdict moves.
- **The roles suite.** Arm 6 reads the text after `handoff: description — ` from its render's stderr
  into the payload's `description`, asserts the hook admits it, and asserts that the same payload
  carrying the role's slot name, `bx · TOOL-bx-1 · researcher`, exits 2 naming the rendered name.
  Every other `Agent` payload the suite hands `agent-cap.js`, arm 11's once `TOOL-aOrientedCast-25`
  lands it, carries the description its render printed. A new arm 12 asserts `extract_label_unit`
  over AC9's four labels. `FLOOR_ASSERTIONS` rises by the assertions arms 6 and 12 add.
- **The review suite.** In `runReview` the whole label is kept as `full` on each trace entry, and
  `label` becomes the text after its last ` · `. The stub lookup and `scanSpawned` read `label`, so
  every present assertion reads the stage as before. New assertions read `full`, as AC8 states, each
  with a count so an empty trace cannot pass. `FLOOR_ASSERTIONS` rises by them.
- **The build suite.** In `run_wf` the same split, plus one `label:<full>` trace line before each
  `agent:` line; the `agent:`, `type:`, `effort:`, `prompt:` and `promptjson:` lines and the returns
  lookup key on the stage. The 74 trace reads of §4 "Evidence" move to the stage words of the table
  above, or to the `label:` line where they tell two spawns of one stage apart, as the fan-out arms'
  writer counts do. New assertions are AC6's and AC7's labels. `FLOOR_ASSERTIONS` rises by the new
  assertions; a moved read is already counted.

### Documentation

- `handoff.py`'s docstring: `render` prints the `handoff: description — ` line outside
  `--stand-in`, and `agents` reads a harness agent's unit as the one unit id its label names.
- `tools/roles/README.md`: the `--part task` paragraph (`:56-64`) names the description line, and
  the field table's unit row (`:96`) reads "the one unit id its journal label names, else the label".
- `tools/roles/SKILL.template.md`, the spawn bullet (`:22-26`): the call's `description` is the name
  `render` prints on stderr. The rendered Skill follows.
- `help/roles.md`: "Hand one task to one agent" (`:33-39`) passes the name as `description`; a new
  section `## How agents are named` gives both shapes, says a `Workflow` run keeps its script's name,
  and says a missing or different name is refused with the right one printed; "What each agent line
  tells you" says a harness agent's unit comes from its label; "What the hooks refuse" (`:82-96`)
  adds the misnamed spawn.
- `tools/hooks/README.md`, rule 6 (`:207-225`): the description clause, and under "What it does not
  stop", a forged name and a harness agent's label.
- `tools/workflows/README.md`: a section `## Agent labels — slug, scope, stage` after "roles — stage
  agents spawned as catalogue roles", holding the shape `<slug> · <scope> · <stage>`, the table
  above, the review harness's slug rule, and that `pending` keeps stage keys.
- The roles dossier: `TOOL-aOrientedCast-27` joins `decisions`, and its prose gains one sentence on
  the spawn name and the label reading. The review-harnesses dossier gains one sentence giving the
  label shape `<slug> · <scope> · <stage>`. The agent-cap dossier read 20474 bytes against a 20480
  cap on 2026-10-13, PINNED, so it is left as it is: its prose stays true, short of the new step,
  which the hooks README carries.

### Kit versions

As §8 F1 resolved: one step for each kit, from its value at this unit's parent commit.

- **Hooks**: `KIT_AGENT_CAP_VERSION` and its same-line marker (`tools/hooks/agent-cap.js:101`), and
  the `gov:kit agent-cap@` markers of `tools/hooks/format-guard.js:7` and
  `tools/hooks/scratch-guard.js:144`, which `tools/check-kit-versions.sh:192-220` holds equal. That
  is 1.37 to 1.38 once `TOOL-aOrientedCast-24` has landed its step.
- **Roles**: `KIT_ROLES_VERSION` (`tools/roles/roles_lib.py:25`), the markers of
  `tools/roles/README.md:1` and `tools/roles/SKILL.template.md:5`, and the rendered
  `.claude/skills/build/SKILL.md:5`. That is 1.4 to 1.5 after `TOOL-aOrientedCast-25`'s step.
- **Review harness**: the `version:` line and both markers at the head of `tier2-review.template.js`
  and its render, 1.49 to 1.50, since every file under the kit ships under this entry
  (`tools/workflows/kit.toml:8-14`).
- The `unattended-build@` and `unattended-unit@` identity markers stay: this build's harness units,
  `TOOL-aOrientedCast-4`, `TOOL-aOrientedCast-10` and `TOOL-aOrientedCast-11`, moved neither.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `renderSpawnName` | function in `agent-cap.js` | `js.function`; `lexicon.py --suggest renderSpawnName --as js.function` answered OK |
| `renderAgentLabel` | function in the two harness templates and their renders | `js.function`; answered OK |
| `render_spawn_name`, `extract_label_unit` | functions in `handoff.py` | `py.function`; answered OK for each |
| `reviewSlug`, `reviewScope` | constants in the review harness | none: `js.constant` is undeclared |
| `HO_DESC`, the `nounit` variant | agent-cap suite variable and fixture key | none: no shell-variable cell is declared |

### Files touched (estimate)

`tools/hooks/agent-cap.js`
`tools/hooks/agent-cap.test.sh`
`tools/hooks/README.md`
`tools/hooks/format-guard.js`
`tools/hooks/scratch-guard.js`
`tools/roles/handoff.py`
`tools/roles/roles_lib.py`
`tools/roles/README.md`
`tools/roles/SKILL.template.md`
`tools/roles/adopt-roles.test.sh`
`.claude/skills/build/SKILL.md`
`help/roles.md`
`tools/workflows/unattended-build.template.js`
`tools/workflows/unattended-build.js`
`tools/workflows/unattended-unit.js`
`tools/workflows/tier2-review.template.js`
`tools/workflows/tier2-review.js`
`tools/workflows/unattended-build.test.sh`
`tools/workflows/tier2-review.test.sh`
`tools/workflows/README.md`
`memory/map/features/roles.md`
`memory/map/features/review-harnesses.md`
`memory/map/generated/`

`format-guard.js` and `scratch-guard.js` move their version marker line and nothing else.

### Rollout

- **Order 28, after both open units it overlaps.** With `TOOL-aOrientedCast-24`, order 26, it shares
  `tools/hooks/agent-cap.js`, `tools/hooks/README.md`, `tools/hooks/format-guard.js` and
  `tools/hooks/scratch-guard.js`. With `TOOL-aOrientedCast-25`, order 27, it shares
  `tools/roles/handoff.py`, `tools/roles/roles_lib.py`, `tools/roles/README.md`,
  `tools/roles/SKILL.template.md`, `tools/roles/adopt-roles.test.sh`, `.claude/skills/build/SKILL.md`,
  `help/roles.md`, the roles dossier and the generated map. The write sets are not disjoint, so this
  unit builds once both have landed. `TOOL-aOrientedCast-26` writes none of these files.
- **Renders.** The builder re-renders the two harness renders with the workflows kit's parity script
  in its `--render` mode, which the role gate admits (`tools/hooks/scratch-guard.js:1228`), and the
  map with `python tools/codebase-map/gen_map.py --write`. The main loop's second pass re-renders the
  Skill with `bash tools/roles/adopt-roles.sh --scaffold`, as `TOOL-aOrientedCast-25` does.
- **Binding.** A hook script is read afresh on every call, so the step binds every session whose
  hooks run from a tree holding this commit, from its next spawn; for this run, once the landing
  merge is in the primary tree (`TOOL-aOrientedCast-7` §3). From then each direct spawn of the main
  loop passes the name, and a refusal prints it. Harness labels take effect at the next `Workflow`
  call that reads the new scripts.
- No settings, matcher or kickoff-manifest `watch:` path moves. Adopters receive the step, the labels
  and the renderer's line at `govkit update`; an adopter's index already carries every role's
  `workflow`. Rollback is a revert of the unit's commits and a re-render of the Skill, the harness
  renders and the map.

### Alternatives rejected

- **`<build> · - · <workflow>` for a unit-less handoff.** A `-` in a name tells the reader nothing.
- **The name on stdout, or inside the prompt file.** Under `--part task` stdout is the prompt the
  hook compares line by line, and the default prints the one path callers capture; a name inside
  the task section would move `task-sha` and the prompt with it.
- **A separate `handoff.py name` verb.** A second route to one string, where the brief puts it on
  `render`.
- **Matching the description by prefix or containment.** It admits the freeform tail the owner
  named.
- **Today's harness labels with a slug and scope prefixed.** It writes the slug, the round or the
  unit twice in the one string the owner reads.
- **A group index, or the first unit id, for a spec-writer group.** The index names no unit, and
  the first id makes the agents verb report one unit for an agent serving several.
- **A `slug` argument for the review harness.** Every governed caller already passes `reviewDir`
  under `builds/<slug>/`, M8's call and the build harness's default
  (`tools/workflows/unattended-build.template.js:300`) alike. An argument is a second answer to one
  question and moves every caller.
- **Whole labels in `pending`.** A return-shape change for every caller, which no reader needs.
- **One shared label helper.** A workflow script has no filesystem and imports nothing. Each copy is
  one line, and the suites' stage split reds a drifted separator.

## 5. Production-readiness checklist

- security — The description is display text: the hook compares it with a string it derives and
  never parses it. The step stops a stale or freeform name, not a forged one, and the hooks README
  says so. No new write path; the renderer adds one stderr line.
- perf / scale — One string comparison per `Agent` call, after rule 6's existing reads, and one
  join per harness spawn.
- error / empty / loading states — A missing `description` refuses as a mismatch naming `null`; an
  index role with no `workflow` refuses naming the index; a review outside a build folder carries no
  slug part rather than an empty one.
- observability — Each refusal prints the expected name verbatim. Each harness agent's label shows
  its build, scope and stage in the Workflow view and in the run journal, where the agents verb
  reads it.
- risks — A main loop that skips the stderr line is refused once and shown the name. The build
  suite's label reads move to the stage words and are verified only at the close, while the review
  suite's reads stay as they are. Two kits take a second step within this build (§8 F1).
- testing — The direct probes and fixtures of §6 in the pass; the `New arm:` lines of §7, observed
  RED then GREEN by the main loop at the close.
- migration — None: no stored shape changes, and past ledger lines keep their unit fields.
- user docs — `help/roles.md` (S6).

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag. Each runs the unit's own code on a
scratch fixture or a stub, or searches a file.

Fixture H is a directory under the run's scratch path holding an empty `.git` directory, a copy of
this repository's role index as `.claude/roles.json`, and two prompt files under
`memory/builds/bx/prompts/`, written with python as the agent-cap suite's `write_handoff` writes its
`ok` file. P1's marker reads role `gov-spec-writer`, build `bx`, unit `TOOL-bx-1` and its own path;
P2's is the same with unit `-`. The payload for P and D is the JSON
`{"tool_name": "Agent", "cwd": <H>, "session_id": "h-s", "prompt_id": <fresh>, "tool_use_id": <fresh>,
"tool_input": {"subagent_type": "gov-spec-writer", "prompt": <P's marker line, a blank line and its
task section>, "description": D}}`, the key left out where D is "none". It is piped to the hook, run
from the scratch path with `CLAUDE_PROJECT_DIR` unset.

Fixture F is the repository the roles suite's `build_fixture` scaffolds, cut out of the suite and made
in the run's scratch path, as `TOOL-aOrientedCast-25` §6 makes it.

Stub T is the build suite's `run_wf` runner, copied into a scratch script and changed only as §4
"The suites" changes it: it looks its returns up by the text after the label's last ` · `, and prints
`label:` and the whole `opts.label` before each `agent:` line. Stub R is the review suite's
`runReview`, copied and changed the same way, keeping each spawn's whole label in its trace. Each
evaluates a render with `node`.

- **AC1** — When
  `python tools/roles/handoff.py render --role gov-diff-reviewer --build aOrientedCast --unit TOOL-aOrientedCast-27 --input diff=HEAD~1..HEAD --stdout --part task`
  runs in this repository, it exits 0, its stdout opens with the marker line and carries no
  `handoff: description` line, and its stderr holds exactly one line opening
  `handoff: description — `, reading `handoff: description — aOrientedCast · TOOL-aOrientedCast-27 · closing-review`.
  Without `--unit` that line reads `handoff: description — aOrientedCast · closing-review`, and
  `git status --porcelain` prints the same before and after both runs.
  Red when: the line is absent, reaches stdout, names the role's slot `diff-reviewer` instead of its
  workflow, or prints a `-` part.
- **AC2** — When `node tools/hooks/agent-cap.js` reads, in fixture H, the payload for P1 with D
  `bx · TOOL-bx-1 · spec-write` and the payload for P2 with D `bx · spec-write`, each exits 0 with
  empty stderr, and the fixture's slot ledger then holds each call's `tool_use_id`.
  Red when: a rendered handoff carrying its right name is refused.
- **AC3** — When the payload for P1 carries D none, `Fold two specs, spec three units`,
  `bx · TOOL-bx-1 · spec-trim`, `bx · TOOL-bx-2 · spec-write` or `bx · spec-write`, and the payload
  for P2 carries `bx · - · spec-write`, `node tools/hooks/agent-cap.js` exits 2 for each, its stderr
  naming `rule 6`, the call's description and `"bx · TOOL-bx-1 · spec-write"`, or
  `"bx · spec-write"` for P2, and no slot holds a refused call's `tool_use_id`. With P1's task section
  one character off and D `Fold two specs`, the refusal names the differing prompt line and not the
  description.
  Red when: a misnamed spawn is admitted or claims a slot, or the name is judged before the prompt.
- **AC4** — When fixture H's `.claude/roles.json` loses the `workflow` key of `gov-spec-writer`, the
  AC2 payload for P1 makes `node tools/hooks/agent-cap.js` exit 2 naming `workflow` and
  `gov-spec-writer`.
  Red when: the spawn is admitted, or the refusal names a thrown error instead of the missing key.
- **AC5** — When, in fixture F, arm 6's render of `gov-researcher` for build `bx` and unit
  `TOOL-bx-1` runs by hand and its task part goes to `node tools/hooks/agent-cap.js` with
  `description` the text after `handoff: description — ` on the render's stderr, the hook exits 0
  with empty stderr. With `description` `bx · TOOL-bx-1 · researcher` it exits 2 naming
  `"bx · TOOL-bx-1 · research"`.
  Red when: the renderer and the hook derive two different names for one handoff.
  fixture: F holds the renderer, the hooks kit and an index rendered from the kit's own catalogue,
  and needs `node` on PATH.
- **AC6** — When stub T runs `tools/workflows/unattended-build.js` with slug `tB`, units `A-tB-1`
  and `A-tB-2` at order 1 and `A-tB-3` at order 2, no `specAudit`, and returns under which every unit
  is authored and committed once, its `label:` lines read `tB · A-tB-1 A-tB-2 · spec-write`,
  `tB · A-tB-3 · spec-write` and `tB · specs · commit`, one each. In unattended mode, with
  `specAudit` declared and returns keyed by the new stage words that reach the subjects, record and
  disposal agents at round 1, as the build suite's audit doubles do today, those agents read
  `tB · audit round 1 · subjects`, `tB · audit round 1 · record` and `tB · audit round 1 · dispose`.
  Red when: a spec writer leaves out a unit of its group, or a build-harness label lacks its slug,
  scope or stage.
- **AC7** — When stub T runs `tools/workflows/unattended-unit.js` with the build suite's
  `CHILD_ARGS` in each mode, its one `label:` line reads `tB · A-tB-1 · build` both times.
  Red when: the unit harness's label lacks the slug, the unit id or `build`.
- **AC8** — When stub R runs `tools/workflows/tier2-review.js` over the review suite's `DIFF` args
  with `reviewDir` `memory/builds/tB/reviews`, every label opens `tB · diff-review round 1 · `, and
  at least one ends in each of `resume:probe`, `find:<lens>`, `verify:ids-<a>-<b>` and `synth`. With
  `reviewDir` `memory/reviews` every label opens `diff-review round 1 · `; over the suite's `SPEC`
  args every label opens `spec-audit round 1 · `; and with the `find:seams` stub dead the result's
  `pending` is `["find:seams"]`.
  Red when: a review label lacks its scope or stage, carries a slug outside a build folder, or
  `pending` carries a whole label.
- **AC9** — When
  `python -c "import sys; sys.path.insert(0, 'tools/roles'); import handoff as h; print([h.extract_label_unit(x) for x in sys.argv[1:]])" "aOrientedCast · TOOL-aOrientedCast-27 · build" "aOrientedCast · TOOL-aOrientedCast-26 TOOL-aOrientedCast-27 · spec-write" "aOrientedCast · diff-review round 1 · find:security" "unit:TOOL-tFix-1"`
  runs, it prints `['TOOL-aOrientedCast-27', None, None, 'TOOL-tFix-1']`, and
  `grep -n "extract_label_unit" tools/roles/handoff.py` shows its call in `print_agent_lines`.
  Red when: a label naming two units reads as its first, or a label written before this unit stops
  yielding its unit.
- **AC10** — When, on the unit's commit `<c>`, the added and removed lines of
  `git diff -U0 <c>~1 <c> -- tools/workflows/tier2-review.template.js` are compared with those of the
  same command over `tools/workflows/tier2-review.js`, they are identical, and so are those of
  `tools/workflows/unattended-build.template.js` and `tools/workflows/unattended-build.js`.
  Red when: a label edit reached a template and not its render, or the reverse.
- **AC11** — When
  `grep -c "handoff: description" help/roles.md tools/roles/README.md tools/roles/SKILL.template.md tools/hooks/README.md tools/roles/handoff.py`
  runs it prints at least 1 for each file; `grep -c "^## How agents are named" help/roles.md` and
  `grep -c "^## Agent labels" tools/workflows/README.md` each print 1; and
  `grep -n "one unit id" tools/roles/README.md` shows the field table's unit row.
  Red when: a page that tells a caller how to spawn leaves out the description, or no page explains
  the names.
- **AC12** — When `KIT_AGENT_CAP_VERSION` is read from `git show <c>~1:tools/hooks/agent-cap.js` and
  from `tools/hooks/agent-cap.js`, the second is one minor step above the first, and
  `git grep -l "gov:kit agent-cap@<the second>" -- '*.js'` lists `agent-cap.js`, `format-guard.js`
  and `scratch-guard.js`. `KIT_ROLES_VERSION` in `tools/roles/roles_lib.py` moves the same way, and
  `grep -c "gov:kit roles@<the second>" tools/roles/README.md tools/roles/SKILL.template.md .claude/skills/build/SKILL.md`
  prints 1 for each file. `grep -c "version: '1.50'" tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js`
  prints 1 for each file.
  Red when: a kit's shipped bytes move with no step, a carrier keeps the old value, or a kit steps
  twice in this unit.
  permission: the rendered Skill reads the roles step only after the main loop's second pass.
  figure: DERIVED for the hooks and roles kits, as the parent's value plus one step; PINNED for the
  review harness at 1.49 on `aa561ec9f`, where no open unit ordered before this one moves it.
- **AC13** — When `grep -c "TOOL-aOrientedCast-27" memory/map/features/roles.md` runs it prints at
  least 1; `grep -c "<slug> · <scope> · <stage>" memory/map/features/review-harnesses.md tools/workflows/README.md`
  prints at least 1 for each file; and
  `git diff --quiet <c>~1 <c> -- memory/map/features/agent-cap.md` exits 0.
  Red when: a dossier misses the change, or the agent-cap dossier is pushed past its cap.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `roles adopter self-test` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `verifier fan-out` · `review-join ban (no ref-keyed join)` · `agent-cap restatement` · `hook destinations (every declared hook path ships)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a location probe asked from a moved directory)` · `codebase-map coverage + freshness` · `govkit selfcheck` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/agent-cap.test.sh · covers AC2 AC3 AC4 · the description arms, against `checkHandoffSpawn` with its description step cut out, so every misnamed spawn is admitted · none
New arm: tools/roles/adopt-roles.test.sh · covers AC5 · arm 6's named spawn, against `render_spawn_name` staged to print the role's slot instead of its workflow · `FLOOR_ASSERTIONS` raised by the assertions arm 6 gains
New arm: tools/roles/adopt-roles.test.sh · covers AC9 · arm 12, against `extract_label_unit` staged back to the first unit id a label holds · `FLOOR_ASSERTIONS` raised by its assertions
New arm: tools/workflows/tier2-review.test.sh · covers AC8 · the whole-label assertions, against `renderAgentLabel` staged to return the stage alone · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/unattended-build.test.sh · covers AC6 AC7 · the `label:` assertions, against the spec writer's scope staged to its group's first unit id and the unit harness's label staged back to `unit:` and its unit id · `FLOOR_ASSERTIONS` raised by the assertions added

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

- **F1 — Which unit moves the hooks and roles kits' versions, now that this unit follows the two
  units specced as each kit's last?**
  Options: (a) this unit moves each kit it touches one more step: the hooks kit after
  `TOOL-aOrientedCast-24`'s step, the roles kit after `TOOL-aOrientedCast-25`'s, and the review
  harness once; (b) `TOOL-aOrientedCast-24` and `TOOL-aOrientedCast-25` drop their steps in a rev
  fold, and this unit makes the build's one step per kit; (c) this unit moves no version and leaves
  its moves to the lander's mint.
  (b) rewrites two specs this writer was not handed, one of them under a concurrent trim. (c) breaks
  the build rule that a kit's last unit steps it, and leaves the kit epoch leg owing a step at the
  push boundary until the lander mints. (a) keeps that rule's intent, that no shipped byte moves
  after a kit's last step, at the cost of two steps of one kit in one build, which this build has
  already taken: the hooks kit stepped at `TOOL-aOrientedCast-14` (`791ee13e5`) and again at
  `TOOL-aOrientedCast-21` (`6fb62ffa5`). No veto applies: no new dependency, surface or carrier.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "Kit versions" states it.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "name a spawned agent by its build slug, unit id and
action, and refuse an Agent call whose description is not that name"` and `"compose a workflow
harness agent label from the build slug, the unit it serves and its stage"` ranked name-stem
neighbours only: a `slug` symbol in `tools/hooks/agent-cap.js`, the `build_*` helpers and
`load_workflows`, none of which composes a name or reads a description. No existing seam composes an
agent's name, so this unit extends the seams that already hold its inputs: rule 6's
`checkHandoffSpawn`, its marker reader and `renderHandoffDeny` in `tools/hooks/agent-cap.js`;
`render`'s `main` and the role keys in `tools/roles/handoff.py`, with the catalogue `workflow` key
that `tools/roles/render_agents.py` already copies into the index; `print_agent_lines`'s label read;
and each harness's existing `label` option. The recall probe surfaced the addendum's brief,
`TOOL-aOrientedCast-7`'s spawn guard, `TOOL-aOrientedCast-20`'s field table, whose first-match label
read S4 narrows, and `TOOL-aHoistedPass-34`, which records that nothing grades a workflow script's
`meta`, in line with §3's title non-goal. `python tools/memory-tree/gotchas.py --for-paths` over the
write set selected `fixture-passes-by-finding-nothing`, `staged-break-substitutes-a-synthetic-value`
and `two-answers-to-one-question`, which AC8's counts, §7's code-level staged breaks and arm 6's
renderer-to-hook check answer.

Recall terms used: `agent description label spawn-guard handoff marker harness journal slug unit-id stage name`
