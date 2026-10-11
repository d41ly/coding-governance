<!-- gov:kit roles@1.0 -->
# roles — the role catalogue: one agent definition per role, the workflow table, and the checker

A governed session runs its LLM work through ten declared WORKFLOWS — `orient`, `research`, `reuse`,
`handoff`, `spec-write`, `spec-review`, `build`, `closing-review`, `gate-bar` and `bookkeeping` —
each driven by an agent ROLE, a harness, a program or the main loop. A role is an agent-definition
file under `agents/`: a CONSTANT block its agent starts from, plus front matter saying which
workflow it serves, which inputs it reads, which path class it may write and which sections of the
governing doc it needs. The workflow table, `workflows.toml`, says which roles drive each workflow,
which harness stage spawns as which role, and what refuses a bypass. The library, `roles_lib.py`, is
the one reader of all of it and the one composition of a role with its house overlay
(`render_role`): every route that hands a role to an agent goes through it, so a role reaches an
agent the same way by every route.

## Editing a role

Edit the role's HOUSE OVERLAY, `house/<role>.md`, never the base file under `agents/`. The base
block is the kit's and is overwritten on update; the overlay is yours and is kept. A non-empty
overlay is appended to the base block under a `## House rules` heading when the role is rendered;
an empty or absent one adds nothing. An overlay carries no `#` or `##` heading of its own and no
render token but `{{MEMORY_ROOT}}`. Its size is printed on every check run and never graded.

A base block POINTS at the document that owns a rule — the spec format, the build method, the
review protocol, all under `{{MEMORY_ROOT}}` — and never restates it. Stage protocol (return
schemas, driver verbs, commit trailers, the severity rubric, the probe rules) stays in the harness
that parses the return, because the harness owns its return contract.

## Where the enforcement points live

Each workflow's `enforced-by` names, by description, what refuses a bypass once the catalogue is
wired: the kickoff kit's card writer for `orient`; the hooks kit's write gate, keyed on a role's
`writes`, for `spec-write` and `build`, beside the routed-commits leg for `build`; the hooks kit's
spawn guard for `research`, `spec-review` and `closing-review`; the pre-push hook for `gate-bar`;
the memory-tree hygiene leg for `bookkeeping`. `handoff` and `reuse` read `none` with the reason.
The checker grades that each entry names something, not that the thing exists.

## The handoff renderer

`python handoff.py render --role <name> --build <slug> [--unit <id>] [--card <path>]
[--input <key>=<value>]... [--out <path> | --stdout] [--part full|task]` turns a role and one task
into the prompt its agent is handed (TOOL-aOrientedCast-2). The file holds the role as `render_role`
renders it under `## Role`, then `## Task`: one block per key of the role's `reads`, in declared
order, then one block per `charter` id. A `task:` key is read from the session card's `## task`
field by the kickoff checker's field grammar, a `card:` key from that card's section, a `brief:` key
from the build's brief record, and an `input:` key from `--input`. A required key that resolves to
nothing, an empty value or a placeholder refuses by name and writes nothing; an optional one is named
on the task block's `Not supplied` line.

The card is `--card`, else the file the kickoff checker's `--card --path` prints for
`CLAUDE_CODE_SESSION_ID`, so the card's location stays that checker's rule. The brief record is
`--input prompt=`, else the one file under the build's `prompts/` folder carrying both a
`## The prompt` and a `## The brief` line; two such files refuse.

The file is written under the build's `prompts/` folder as
`<date>-prompt-<id>-<n>-<role without gov->.md`, and its `gov:handoff` marker line carries a hash of
each section. `python handoff.py check <file>` re-derives both hashes and the marker's path;
`--part task` prints the marker and the task section alone, which is what a typed agent spawn
carries. `python handoff.py harness-args <harness>` prints the `roles` object a harness takes: the
union of the `stages` tables of every workflow whose harness is that script, as one line of JSON.
`python handoff.py stage-efforts <workflow>` prints the `efforts` object a harness call takes for one
workflow, as the next section states.
Exit 0, 1 on a refusal, 2 on usage or an unarmed tree; the script's header states what it does not
check.

## The effort policy

`house/policy.toml` sets the reasoning effort every role agent runs at (TOOL-aOrientedCast-10). It is
seeded: an adopter receives it once and owns it, and `update` never rewrites it, so it is yours to
edit. `roles_lib.load_policy` is its one reader and validator; `check_roles.py` reports its defects as
R12 and every render refuses it with exit 2, so no level falls back silently.

- `[effort]` holds `default`, the level of every role and stage the file does not name.
- `[effort.roles]` holds one entry per role slot whose `agent` is true. `render_agents.py` writes the
  resolved level into that agent type as `effort: <level>`, the line before `omitClaudeMd: true`.
- `[effort.stages.<workflow>]` overrides a stage of one workflow, keyed by that workflow's `stages`
  keys. `handoff.py stage-efforts <workflow>` prints each stage's level, its entry here else its
  slot's, and a harness call passes that JSON as `efforts`, which wins over the agent type's level.
  That is how `gov-skeptic` runs at `medium` in spec review and `high` in closing review.

The levels are `low`, `medium`, `high`, `xhigh` and `max`, the names Claude Code 2.1.292 reads on both
an agent type and a `Workflow` `agent()` call; the integer form only the agent loader takes is
refused. The CLI silently runs `xhigh` and `max` as `high` on a model that lacks them. A changed level
reaches an agent type after `render_agents.py --write` and a NEW session, since a session reads its
agent registry at start; a harness `efforts` takes effect on the next call. The main session's own
effort is the owner's setting, which no file here reaches.

## The agent types

`python render_agents.py --write | --check | --selftest` renders each role whose `agent` is true
into a Claude Code agent type, `.claude/agents/<name>.md` (TOOL-aOrientedCast-3). Its front matter
is the role's Claude keys, then `omitClaudeMd: true`, then the role's `workflow` and `writes` for
the hooks to read. Its body is `render_role`'s output, then, under `## Charter`, one
`### charter §<n>` block per id of the role's `charter` key, in the order the key names them, spelled
as a handoff spells its blocks. An agent started with the charter omitted holds only its system
prompt and its task, so a harness that hands it no handoff would otherwise give it no charter section
at all; a typed spawn that IS handed a handoff carries those sections twice, which is the accepted
cost. Beside the types sits `.claude/roles.json`, the generated index the hooks read: every role
with its `workflow`, `writes` and `agent`, `agent: false` roles included, and `harnesses`, the
repo-relative scripts of every workflow whose `driver` is `workflow`. A harness the tree does not
hold is listed where the resolver places it and printed on a `note` line; it refuses nothing.

**Ownership.** The renderer owns the types its catalogue names plus every name the on-disk index
lists, which is the set a previous render wrote. `--write` unlinks an owned type the catalogue no
longer renders and rewrites the index last; it never touches any other file under
`.claude/agents/`, where your own definitions may live. `--check` writes nothing, names every
`missing`, `drift` or `stale` owned path and the remedy, and strips carriage returns from the
on-disk side, so a CRLF checkout of a correct render reads fresh. The adopter's `--check` runs it
beside the Skill's compare as the `roles render wiring` leg, so editing a role, an overlay or a
cited charter section without a re-render reds the bar.
`--selftest` runs the renderer's arms over a catalogue it builds in a temporary directory and is the
`roles render selftest` leg. Exit 0, 1 on drift or a failed arm, 2 on usage, a library refusal or a
zero-role catalogue.

**Restart.** Claude Code reads its agent registry when a session starts, so a type written, changed
or unlinked is not spawnable as changed by a session started before the write. `--write` prints one
line saying so whenever an agent type moved, and `unchanged` when nothing did. After a re-render or
a pull that moved a type, start a new session before spawning one.

**The CLI floor.** The trim was measured on Claude Code 2.1.292: a type with `omitClaudeMd: true`
reports its own name as `agent_type` in the hook payloads and starts without the governing doc. The
CLI omits it only while a server flag it reads stays on and the caller supplies no user context of
its own, so a later CLI or a flag flip can re-admit the charter silently; the agent-type probe
record in the build that shipped this renderer is the instrument to re-run.

## Adopting

`roles` is in govkit's default selection (TOOL-aOrientedCast-8), so `govkit apply` installs it and
`govkit update --write` installs it where a receipt predates it, printing `default-gained`. It
requires the kickoff kit, whose card writer every `task:` and `card:` input is read from, and the
memory-tree kit, whose `.memory-tree.conf` names the memory root and, by `CHARTER`, the governing
doc the roles' charter ids resolve against.

- The base role files, the workflow table, the library, the checker, the renderers, the adopter and
  this README are the kit's, overwritten on every update.
- The ten house overlays under `house/` are SEEDED: you receive each once and own it afterwards,
  and an update never rewrites one. They are where your project's rules for a role go.
- The adopter, `bash adopt-roles.sh --scaffold`, runs at install and again at every update unless
  `GOVKIT_RERENDER=0` declines it. It renders the `/build` Skill, one agent type per agent role
  under `.claude/agents/` and the role index `.claude/roles.json`, the file the role-aware write
  gate and spawn guard arm on. `--check` grades all three and is the `roles render wiring` leg.
- Start a new session after an install or an update that moved an agent type: a running session
  cannot spawn a type written after it started.
- `/build` drives the three harnesses the workflow table names, which ship in the `review-harness`
  kit, not a default. Without it the role agents, the handoffs and the gates still work, and the
  catalogue checker, the agent render and `check-wiring.sh` each print a `note` per absent harness.

With no governing doc at `CHARTER` the adopter renders the Skill alone and exits 3, naming the doc
and the key; the descriptor accepts that exit as `no-governing-doc`, so the install succeeds and no
agent type or role index is written until the doc exists and `--scaffold` runs again.

`check-wiring.sh` reports an install whose render is absent as `UNWIRED  roles`, naming the
`--scaffold` remedy, a missing governing doc by its path and the `CHARTER` key, and a CRLF agent
type or role index on its eol line.

## The `/build` Skill

`bash adopt-roles.sh --scaffold | --check` renders `SKILL.template.md` into
`.claude/skills/build/SKILL.md`, the router an ATTENDED session follows after kickoff's READY card
and the owner's go (KICK-aOrientedCast-2). It walks this catalogue's workflows in stage order and
points at the carriers `/unattended` already follows (the build method, the verbs guide, the two
build harnesses' attended mode, the review harness) instead of restating them; every agent it orders
is spawned from a `handoff.py render` and every harness call carries `handoff.py harness-args` and
`handoff.py stage-efforts`.

The render substitutes three tokens literally: `{{KIT_DIR}}` and `{{TOOL_ROOT}}`, derived by the
same `.git` walk the unattended adopter uses, and `{{MEMORY_ROOT}}`, read from `.memory-tree.conf`.
An empty derivation, an absent conf or a blank key exits 2; a `{{` surviving the render exits 1
naming its line.

The render also BINDS the Skill's stages to `workflows.toml`: each `## Stage <n> — <workflow>`
heading must name a workflow whose `stage` is `<n>`, the headings ascend strictly, and every
workflow of stage 1 or more is named by exactly one heading. A disagreement exits 1 naming the
heading and the entry; a catalogue read yielding zero workflows exits 2 as a dead probe. `--check`
renders in memory and byte-compares with the file on disk, carriage returns stripped from both, so
it grades exactly what `--scaffold` would write.

**Restart.** Whether a running session lists a Skill written after it started is unverified on this
CLI. `--scaffold` prints one line saying so when it creates the file: start a new session before
invoking `/build`.

## The checker

`python check_roles.py [--root <dir>] [--write]`, run as the `roles catalogue` gate leg. It grades
the role files, the overlays and the workflow table against each other in both directions, and every
`charter` id against a `## §<n> — ` heading of the governing doc, which it locates through the
memory-tree conf's `CHARTER` key. It prints one line per defect naming the file and the rule (R0 to
R11, listed in its header with what it does not check), then a summary of every count it graded.
Exit 0 clean, 1 on a defect or an empty catalogue (DEAD PROBE), 2 when the conf or its `CHARTER`
is missing. `--write` re-renders the region below from the table and the front matter, and nothing
else; the check compares the two on every run.

<!-- gen:roles-catalogue -->
**Workflows**, from `workflows.toml`:

| name | stage | driver | harness | roles | stages | enforced-by | trigger |
|---|---|---|---|---|---|---|---|
| orient | 1 | main-loop | /session-kickoff | gov-orienter | — | manifest-check.sh --card --append | once per session, at kickoff, before the first work-unit is opened |
| reuse | 2 | agent | none | gov-reuse-scout | — | none — the scout's trigger is the kickoff opt-in that aScoutedSeam owns | before a new behaviour is designed, when kickoff asks for a scout |
| spec-write | 3 | workflow | {prefix}/workflows/unattended-build.js | gov-spec-writer, gov-builder, gov-spec-reviewer, gov-skeptic, gov-synthesizer | specWriter → gov-spec-writer, disposal → gov-spec-writer, builder → gov-builder, specFinder → gov-spec-reviewer, skeptic → gov-skeptic, synthesis → gov-synthesizer | scratch-guard.js role arm | once per build, after orientation, for every unit whose spec is missing or thin |
| spec-review | 4 | workflow | {prefix}/workflows/tier2-review.js | gov-spec-reviewer, gov-skeptic, gov-synthesizer | specFinder → gov-spec-reviewer, skeptic → gov-skeptic, synthesis → gov-synthesizer | agent-cap.js spawn guard, on the build harness's Workflow call whose roles carry the audit's review keys | after the spec set is written, where the build or its project declares a spec audit |
| build | 5 | workflow | {prefix}/workflows/unattended-unit.js | gov-builder | builder → gov-builder | scratch-guard.js role arm, routed commits name a specced unit | once per unit, in stage order, after its spec is READY |
| closing-review | 6 | workflow | {prefix}/workflows/tier2-review.js | gov-diff-reviewer, gov-skeptic, gov-synthesizer | diffFinder → gov-diff-reviewer, skeptic → gov-skeptic, synthesis → gov-synthesizer | agent-cap.js spawn guard | once per build, after the last unit is terminal, over the cumulative diff |
| gate-bar | 7 | program | bash {prefix}/run-gates/run-gates.sh | — | — | the pre-push hook | once, after the closing review, at the close or the push boundary |
| research | 0 | agent | none | gov-researcher | — | agent-cap.js spawn guard | any time a design must choose between candidates that no existing seam decides |
| handoff | 0 | program | python {prefix}/roles/handoff.py render | gov-session | — | none — a session-to-session message is no tool call the spawn guard sees | any time work passes to another session of this repository |
| bookkeeping | 0 | main-loop | none | — | — | memory hygiene | any time a record, an index or the run state is updated |

**Roles**, from `agents/*.agent.md`:

| role | workflow | writes | reads | charter | agent | returns |
|---|---|---|---|---|---|---|
| `gov-builder` | build | product | input:spec, card:route?, brief:non-goals? | §3, §7, §9, §11, §12 | true | whether the unit was committed, the commit, why when it was not, and which check ran for which gate |
| `gov-diff-reviewer` | closing-review | none | input:diff, input:spec? | §7, §8, §9, §10 | true | concrete findings, each with its file and line, the input that reaches it, the consequence and a proposed fix |
| `gov-orienter` | orient | none | input:question, input:prompt? | §1, §2, §5 | true | the orientation card body: the derived task, the manifest audit line, the rows read, the records found, the bug classes and the open rows |
| `gov-researcher` | research | none | input:question, brief:goal?, brief:non-goals? | §5, §12 | true | the candidates, each with its mechanism, the smallest test that would make it lose and that test's result, then the pick and its reason |
| `gov-reuse-scout` | reuse | none | input:question, task:in?, card:reuse? | §12 | true | the seam to extend, cited by path, or "no existing seam fits" with the evidence |
| `gov-session` | handoff | none | input:question, brief:goal?, task:todo?, card:route? | §2, §3 | false | nothing to the sender; the receiving session acts on the task block and reports in its own session |
| `gov-skeptic` | closing-review | none | input:diff?, input:spec? | §8, §10 | true | a verdict per finding, confirmed or refuted, with the reason observed and, for a confirmed one, its severity |
| `gov-spec-reviewer` | spec-review | none | input:spec, brief:goal?, brief:non-goals? | §7, §8, §9, §10 | true | concrete findings, each with the spec and section, the evidence probed, the consequence and a proposed fix |
| `gov-spec-writer` | spec-write | spec | brief:goal, brief:items, brief:acceptance, brief:gates, brief:non-goals, input:spec?, task:reuse?, card:route? | §1, §7, §9, §12 | true | the units authored, already present and refused, each by its unit id, with the reason for every refusal |
| `gov-synthesizer` | closing-review | review | input:diff?, input:spec? | §8, §16 | true | the report's path and the items it adjudicated, each with its severity and the ids of the findings it covers |

<!-- /gen:roles-catalogue -->
