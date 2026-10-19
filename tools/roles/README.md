<!-- gov:kit roles@1.6 -->
# roles — the role catalogue: one agent definition per role, the workflow table, and the checker

A governed session runs its LLM work through ten declared WORKFLOWS — `orient`, `research`, `reuse`,
`handoff`, `spec-write`, `spec-review`, `build`, `closing-review`, `gate-bar` and `bookkeeping` —
each driven by an agent ROLE, a harness, a program or the main loop. A role is an agent-definition
file under `agents/`: a CONSTANT block its agent starts from, plus front matter saying which
workflow it serves, which inputs it reads, which path class it may write, which sections of the
governing doc it needs, when it is mandatory and where its output goes. The workflow table, `workflows.toml`, says which roles drive each workflow,
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
The `mandatory` and `output` keys ride the base file, as `writes` does, so an overlay cannot change
them.

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
[--input <key>=<value>]... [--out <path> | --stdout | --stand-in] [--part full|task]` turns a role and one task
into the prompt its agent is handed (TOOL-aOrientedCast-2). The file holds the role as `render_role`
renders it under `## Role`, then `## Task`: one block per key of the role's `reads`, in declared
order, then, as its last block, the role's charter blocks (described under "The agent types"),
whose library notes print on stderr as `handoff: note — `. A `task:` key is read from the session card's `## task`
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
carries. Outside `--stand-in`, `render` also prints one stderr line, `handoff: description — <name>`,
after its notes: the spawn's name, `<build> · <unit> · <workflow>` with the role's catalogue
`workflow`, or `<build> · <workflow>` with no `--unit`. The `Agent` call passes it as `description`,
and the hooks kit's spawn guard derives the same name from the marker and the role index and refuses
a call carrying any other (TOOL-aOrientedCast-27). stdout does not change in any mode.
`python handoff.py harness-args <harness>` prints the `roles` object a harness takes: the
union of the `stages` tables of every workflow whose harness is that script, as one line of JSON.
`python handoff.py stage-efforts <workflow>` prints the `efforts` object a harness call takes for one
workflow, as the next section states.
Exit 0, 1 on a refusal, 2 on usage or an unarmed tree; the script's header states what it does not
check.

`python handoff.py roster` prints the charter's roles section, one line per role, every role
included, `agent: false` too (TOOL-aOrientedCast-17):
``- `<slot>`: <description> <when>. Output: <output>.``, where `<when>` is `Optional` for a
`mandatory` of `no`, `Optional, <text>` for `no — <text>`, and `Mandatory <value>` otherwise, and
`{{MEMORY_ROOT}}` is the conf's value. The order is the workflow table's: by the file position of
the entry a role's `workflow` names, then by its place in that entry's `roles`, with a role naming
no entry last. A line past 200 characters, the playbook's one-line rule limit, refuses naming the
role and its length, as do a missing key and an empty catalogue, with nothing printed: exit 1. No
repository or no `MEMORY_ROOT` exits 2. It reads no charter, since on a first install the playbook
render writes the charter; the playbook kit's derived roster placeholder is its consumer.

## The agent lines

`python handoff.py agents (--handoff <path> | --run <run-id>) [--session <file>] [--write]` prints
the governing doc's `agent` line for each agent the selector names, then its `returned` line once
it has returned (TOOL-aOrientedCast-20). The two shapes are read from the doc's micro-format fence
by `roles_lib.extract_microformat_shapes`, each marker a whole line and the last definition of a
head winning, as the hooks kit's format guard reads the fence, and filled by placeholder name. A
missing shape, or a placeholder the verb does not derive, refuses. `--handoff` names a direct spawn:
every `Agent` call whose prompt opens with that file's marker line as the spawn guard reads it,
through `roles_lib.extract_prompt_marker`, and whose result names an agent. `--run`
names a harness run: one agent per `started` entry of its journal. The session is `--session`, else
the transcript `CLAUDE_CODE_SESSION_ID` names under the Claude projects folder, found by the run-log
kit's rule.

Every agent a declared harness spawns carries the label `<slug> · <scope> · <stage>`: a spec writer
serving a group names all its unit ids, so its line reads the label rather than one unit
(TOOL-aOrientedCast-27). A harness run's own title is not the agent's to set: the tool fixes it from
the script's `meta` block, so it reads `unattended-build`, `unattended-unit` or `tier2-review`. The
run's identity, its build, scope and action, is its first log line and the leading `identity` field
of its return.

| Field | From | When nothing answers |
|---|---|---|
| role | the agent's meta `agentType`; for a direct spawn, else the marker's `role` | `unknown` |
| effort | the agent transcript's last `effort`; else the agent type's `effort:` line | `unknown` |
| model | the transcript's last `message.model`; for a direct spawn, else the call's `resolvedModel` | `unknown` |
| unit or label | the marker's `unit`, else the meta's `description`; for a harness agent, the one unit id its journal label names, else the label | `unknown` |
| prompt | the handoff and its marker's `path`; for a harness agent, the call's `briefPath`, else its `scriptPath` | `unknown` |
| writes, gates | the role index's `writes` and `gates` for the role | `none` |
| outcome | `failed`, a notification status that is not `completed`, `committed <sha>` or `not committed` from the unit harness's result, else `wrote <n> files` | — |
| wall | the transcript's first `timestamp` to its last, as `45s`, `7m47s` or `1h02m` | `unknown` |
| tokens | the sum, over distinct message ids, of the largest `output_tokens`, as `812` or `41.2k` | `unknown` |

A direct spawn has returned when a notification names its call or its result says `completed`; a
harness agent when its journal holds a `result` or `failed` entry for it.

**The ledger.** Only with `--write`, each printed line holding no `unknown` field is added to the
build's one `<MEMORY_ROOT>/builds/<build>/build/<date>-build-<id>-agent-ledger.md`, created on first
use; without it the verb writes nothing and one note names the held lines and `--write`, so a call
made mid-pass leaves the tree as it found it. Pass `--write` only at a bookkeeping step, when no pass
is running (TOOL-aOrientedCast-25). It is
added only if no line already carries the same head and the same last field, its `run` token. A line
held back for an `unknown` field is added by a later run. In the ledger the prompt link is re-rooted
at the ledger's folder. The ledger's `**Serves:**` line lists every unit id the build's specs define
on their first line, and it is re-derived on every write. The build is the marker's `build`, else the
`Workflow` call's `slug`, else the session card's last `## route`. A build with no folder or no
specced id writes nothing and says why.

Exit 0 on lines printed, notes or none; 1 on a refusal: no marker in the handoff, no matching call,
no run journal, a missing shape, an underived placeholder, or two ledgers in one build. Exit 2 with
no repository, `MEMORY_ROOT`, `CHARTER`, session file or `.claude/roles.json`.

## Standing in for a role

Work goes to its role agent. The one exception is a tool or run that cannot spawn a sub-agent at all:
there the main loop does the role's work itself, as a stand-in, and the owner grants that by a dated
waiver row (TOOL-aOrientedCast-19). A waiver relaxes the `[roles]` rule for one role in one build. It
never admits a write a hook refuses and never removes a leg from the bar; in Claude Code a sub-agent
can always be spawned, so the hooks read no waiver row.

**The registry** is `<MEMORY_ROOT>/project/role-stand-in-waiver.txt`, written by the owner and by
nobody else. No tree holds it until the first row, and an absent registry waives nothing. Blank lines
and lines opening `#` are ignored; every other line is one row of five TAB-separated fields, split at
the first four TABs so the reason may hold anything:

```
<date>	owner <who>	<role>	<build>	<reason>
```

The date is a `YYYY-MM-DD` calendar date, the attribution `owner ` and one token, the role a role
file whose `agent` is not `false`, the build a slug of letters, and the reason non-empty. A second row
for the same build and role is a defect naming the line it repeats.

**The declaration.** A stand-in renders its role's handoff with
`python handoff.py render --role <role> --build <slug> ... --stand-in` and follows it, so the role's
text reaches it exactly as it would reach an agent. With no valid row for that build and role the
render exits 1, naming the registry and the row the owner writes, and writes nothing; otherwise the
file takes the derived name with a `-stand-in` tail before `.md`. `--stand-in` excludes `--out` and
`--stdout`: a handoff printed to stdout declares nothing.

**R15** in the checker joins the two both ways: a `*-stand-in.md` file under a build's `prompts/`
whose marker's build and role no row covers is a defect, a tailed file with no marker is a defect,
and a row no declaration consumes is stale and a defect, as the sibling registries red a stale row.
Every valid row prints as one `roles: note: stand-in waiver` line on every run, green included, and
the summary carries both counts. R15 does not check that the tool truly could not spawn, that the
signer is the owner, or that the reason says anything, and it cannot see a stand-in nobody declared.

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

`[gates]` (TOOL-aOrientedCast-11) names, per role slot whose `agent` is true, the gate legs that role
may run, by their name in the tool root's `gate-legs.json`; every other role runs none, because gates
are the main session's at the merge or push threshold. `load_policy` refuses a key naming no role
file or an `agent: false` role, a value that is not a list of strings, and a name the manifest holds
no leg for, which it checks only when the manifest reads. A name ending in `?` is optional
(TOOL-aOrientedCast-13): a leg the manifest lacks is then a note rather than a refusal, for a leg
whose kit a target may not install, and the `?` is taken off before anything reads the name; a bare
name still refuses, so a misspelt required leg is caught. `render_agents.py` writes each role's list
into the index as `gates`, empty where this table names none, and the manifest's path as
`gates.manifest`; the hooks kit's scratch guard reads both and refuses a role agent any other gate.
An adopter that received this file before the table existed gains it only by its own edit, and until
then every role's list is empty, the strict reading.

## The agent types

`python render_agents.py --write | --check | --selftest` renders each role whose `agent` is true
into a Claude Code agent type, `.claude/agents/<name>.md` (TOOL-aOrientedCast-3). Its front matter
is the role's Claude keys, then `omitClaudeMd: true`, then the role's `workflow` and `writes` for
the hooks to read. Its body is `render_role`'s output, then `## Charter` and
`render_charter_blocks` for the role (TOOL-aOrientedCast-16): a `### Charter rules` block holding the
section 1 rule lines whose tag the role's `rules` key cites, in charter order, then the charter's
`## Protocols` and `## Facts` sections whole, each under a `### ` heading — the same text a handoff
appends to its task. `parse_charter` reads only the span between the `gov:playbook` region markers
when the doc holds them, so an adopter's own sections around the region never reach an agent. An
agent started with the charter omitted holds only its system prompt and its task, so a harness that
hands it no handoff would otherwise give it no charter at all; a typed spawn that IS handed a
handoff carries the blocks twice, which is the accepted cost. A pre-tag (v3.x) charter, with
`## §<n> — ` headings and no rule tag, renders every type with no `## Charter` and prints one note
asking for a reseed; a doc of neither shape refuses. Beside the types sits `.claude/roles.json`, the generated index the hooks read: every role
with its `workflow`, `writes` and `agent`, `agent: false` roles included, and `harnesses`, the
repo-relative scripts of every workflow whose `driver` is `workflow`. The kit resolver finds a
harness govkit rendered from its template through that file's `rendered` receipt row, so a kit
landed under its id rather than its home is listed where it sits. A harness the tree does not hold
is listed where the resolver places it. Where a file of its name sits directly inside a directory
under the tool root beside a mark of its kit, the harness's template `<stem>.template<suffix>` or a
`kit.toml` declaring the home its listed path names, its kit holds it where the index does not look:
it prints on a `misplaced` line naming each such file, and `--check` exits 1 (TOOL-dRenderedAnchor-1,
TOOL-dRenderedAnchor-2). The scan reads the disk, never the receipt. A file of its name beside
neither mark is the adopter's own, so like no file at all it prints on a `note` line and refuses
nothing.

**Ownership.** The renderer owns the types its catalogue names plus every name the on-disk index
lists, which is the set a previous render wrote. `--write` unlinks an owned type the catalogue no
longer renders and rewrites the index last; it never touches any other file under
`.claude/agents/`, where your own definitions may live. `--check` writes nothing, names every
`missing`, `drift` or `stale` owned path and the remedy, and strips carriage returns from the
on-disk side, so a CRLF checkout of a correct render reads fresh. The adopter's `--check` runs it
beside the Skill's compare as the `roles render wiring` leg, so editing a role, an overlay, a
cited rule line or a carried section without a re-render reds the bar: a rule edit stales exactly
the types whose role cites its tag, and a carried-section edit stales every type.
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
doc the roles' rule tags resolve against.

**A role's `rules` tags.** A tag every v4.x charter template carries outside any `when:` or `kit:`
block is cited bare. A tag a target's charter may lack is cited with a trailing `?` — `cross-os`,
fenced by `when:cross-os`, and `spec`, which v4.0 and the first v4.1 template lack — so a charter
without it prints a note instead of refusing. Write the tags in charter order, and name a protocol
in a body by its name ("the build method's M6"), never by its file: the checker refuses the file
name of any protocol the charter's Protocols section lists.

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
  The agent render is the one reader that prints `misplaced`, for a harness its kit holds elsewhere
  under the tool root; `check-wiring.sh`'s note names `adopt-roles.sh --check` as the command that
  says which.

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

Before the plain `{{TOOL_ROOT}}` substitution, every `{{TOOL_ROOT}}<home>/<file>` citation the kit
resolver holds is replaced by the path it resolves, through `roles_lib.resolve_cited_paths`, the
resolver the role index calls (TOOL-dRenderedAnchor-2). So the Skill names each harness where the
install holds it, a kit govkit landed under its id behind a `rendered` receipt row included, and the
plain substitution answers only a citation the resolver does not hold. In this repository every
citation is held at `<tool root>/<home>/`, so the render is unchanged. The answer reads the disk at
render time: `apply` runs the adopter before the harnesses are rendered, so a first install names
the plain path, `--check` reads the Skill out of sync, and the next `--scaffold`, which `govkit
update` runs, corrects it. A failed citation pass exits 2.

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
`rules` tag against the section 1 rule tags of the governing doc, which it locates through the
memory-tree conf's `CHARTER` key; a body or an overlay spelling a protocol's file name reds as R5 or
R10. A role called mandatory under a workflow whose `enforced-by` names no hook script, without an
`unenforced — <why>` clause, reds as R13, and a writer role whose `output` lacks its class's folder
as R14. A stand-in declaration and the owner's waiver rows are joined as R15, under "Standing in for
a role". It prints one line per defect naming the file and the rule (the rules are listed in its
header, with what it does not check), then a summary of every count it graded, the charter's shape among
them. Exit 0 clean, 1 on a defect or an empty catalogue (DEAD PROBE), 2 when the conf, its
`CHARTER` or its `MEMORY_ROOT` is missing, or the doc is no charter this kit reads. `--write` re-renders the region below from the table and the front matter, and nothing
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

| role | workflow | writes | reads | rules | agent | returns |
|---|---|---|---|---|---|---|
| `gov-builder` | build | product | input:spec, card:route?, brief:non-goals? | yagni, reuse, core, derive, verify, gate, security, bytes, cross-os?, tools | true | whether the unit was committed, the commit, why when it was not, and which check ran for which gate |
| `gov-diff-reviewer` | closing-review | none | input:diff, input:spec? | verify, gate, class, left-shift, security, risk, bytes, cross-os? | true | concrete findings, each with its file and line, the input that reaches it, the consequence and a proposed fix |
| `gov-orienter` | orient | none | input:question, input:prompt? | small, ids, memory, tokens, tools | true | the orientation card body: the derived task, the manifest audit line, the rows read, the records found, the bug classes and the open rows |
| `gov-researcher` | research | none | input:question, brief:goal?, brief:non-goals? | reuse, verify, class, memory | true | the candidates, each with its mechanism, the smallest test that would make it lose and that test's result, then the pick and its reason |
| `gov-reuse-scout` | reuse | none | input:question, task:in?, card:reuse? | reuse | true | the seam to extend, cited by path, or "no existing seam fits" with the evidence |
| `gov-session` | handoff | none | input:question, brief:goal?, task:todo?, card:route? | ids, memory | false | nothing to the sender; the receiving session acts on the task block and reports in its own session |
| `gov-skeptic` | closing-review | none | input:diff?, input:spec? | verify, class, risk | true | a verdict per finding, confirmed or refuted, with the reason observed and, for a confirmed one, its severity |
| `gov-spec-reviewer` | spec-review | none | input:spec, brief:goal?, brief:non-goals? | spec?, verify, gate, class, security, risk | true | concrete findings, each with the spec and section, the evidence probed, the consequence and a proposed fix |
| `gov-spec-writer` | spec-write | spec | brief:goal, brief:items, brief:acceptance, brief:gates, brief:non-goals, input:spec?, task:reuse?, card:route? | yagni, reuse, core, contract, derive, one-fact, spec?, verify, gate, class, small, docs, security | true | the units authored, already present and refused, each by its unit id, with the reason for every refusal |
| `gov-synthesizer` | closing-review | review | input:diff?, input:spec? | left-shift, risk, signal | true | the report's path and the items it adjudicated, each with its severity and the ids of the findings it covers |

<!-- /gen:roles-catalogue -->
