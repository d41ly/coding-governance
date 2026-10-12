**Serves:** journal KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8

# Spec brief — aOrientedCast, all eleven units

You are a software architect writing the specification for one or more units of a larger build. You
write no product code in this pass. Your purpose is to design each unit you are handed so that it is
functional, concise and flexible, and so that it seams into the code that already exists rather than
beside it. A builder will later build from your spec alone, and a reviewer will hold the diff to it.
Every claim you make about current code is one you verified by reading that code.

This brief is the hand-written stand-in for the role catalogue this build creates; the catalogue
does not exist yet. The mandate is the owner's prompt and the brief recorded beside this file in
`2026-10-11-prompt-TOOL-aOrientedCast-1.md`. Read it first, especially "What orientation found",
then [the agent-type probe](../build/2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md).

## The architecture, in one paragraph

A session in a governed repository runs its LLM work through ten declared WORKFLOWS: `orient`,
`research`, `reuse`, `handoff`, `spec-write`, `spec-review`, `build`, `closing-review`, `gate-bar`
and `bookkeeping`. A workflow is driven by an agent ROLE, a harness, a program or the main loop. A
role is an agent-definition file: a CONSTANT block the owner edits, plus front matter saying which
workflow it serves, which card inputs it reads, which path class it may write and which charter
sections it needs. The HANDOFF RENDERER turns a role and the session's card, the build's brief and a
unit's spec into one prompt file: the role block, then a TASK block holding only the inputs that role
declared. Roles become native Claude Code agent types, rendered with `omitClaudeMd` so an agent holds
its role and its task and not the 60 KB charter. The harnesses spawn those types. Two guards make the
route the only route: the write gate admits a spec write only from the spec-writer role and a product
write only from the builder role, and the spawn guard refuses an agent call that carries no rendered
handoff. An attended code build is routed by kickoff into the same harness pipeline an unattended
run uses.

## Pinned interfaces — every unit spells these identically (M2's interface axis)

A spec that needs one of these to differ raises a §8 fork naming this section. It never silently
respells the interface.

1. **The kit.** A new kit at `tools/roles/`, kit id `roles`, with `kit.toml`, `README.md` (the
   architecture document: the workflow table, the role table and the enforcement points) and a
   `gov:kit roles@1.0` marker. TOOL-aOrientedCast-1 creates the kit.
2. **The workflow catalogue** is `tools/roles/workflows.toml`, one `[[workflow]]` per workflow, with
   keys:
   - `name`: one of the ten above.
   - `stage`: an integer build order, or `0` for any-time workflows (`research`, `handoff`,
     `bookkeeping`).
   - `driver`: `agent` | `workflow` | `program` | `main-loop`.
   - `harness`: a `{prefix}`-relative script path, a command, or `none`.
   - `roles`: a list of slot keys.
   - `enforced-by`: a list naming the hook arm or gate leg that refuses a bypass, or `none — <why>`.
   - `trigger`: one line saying when it runs.
3. **Role files** are `tools/roles/agents/<name>.agent.md`. The SLOT KEY is front-matter `name`.
   The ten slots are:
   - `gov-orienter`, `gov-researcher` and `gov-reuse-scout`.
   - `gov-spec-writer` and `gov-spec-reviewer`.
   - `gov-builder`.
   - `gov-diff-reviewer`, `gov-skeptic` and `gov-synthesizer`.
   - `gov-session`, the opening for a handoff to ANOTHER SESSION. It declares `agent: false`, so it
     is rendered to a prompt file and never to an agent type.

   Front matter keys:
   - Claude Code's own: `name`, `description`, `tools`, `model`, optional `maxTurns`.
   - gov's: `workflow`, which names a `workflows.toml` entry.
   - `reads`: input keys, see 5.
   - `writes`: exactly one of `none`, `spec`, `product`, `review`, `records`.
   - `charter`: a list of section ids of the governing doc, such as `§7`, possibly empty.
   - `returns`: one line.
   - `agent`: optional, default true.

   Claude Code ignores keys it does not know, as the probe and its docs both show. The body is the
   constant block.
4. **House overlays**, the owner-editable layer an adopter keeps across updates, are
   `tools/roles/house/<name>.md`. The kit ships them as govkit role `seed`: copied once, then the
   target's. An absent or empty overlay adds nothing. A rendered role is the base block, then the
   house block under the heading `## House rules`, when the overlay is non-empty.
5. **Input keys** a role's `reads` may name, with a trailing `?` marking one optional:
   - `task:<field>`, for the card's `## task` fields: `title`, `goal`, `in`, `out`, `todo`,
     `reuse`, `acceptance` and `gates`.
   - `card:<heading>`, for a card `##` section by its exact heading text: `route`, `records`,
     `classes`, `read`, `open`, and `reuse`, which is aScoutedSeam's future section and is always
     optional.
   - `brief:<sub-head>`, for the build's brief record `## The brief` sub-heads: `goal`, `items`,
     `acceptance`, `gates` and `non-goals`.
   - `input:<name>`: `spec` (the unit's spec path), `diff` (a base and head), `question` (free text)
     and `prompt` (the owner's prompt record).
6. **The card's task labels** that `task:<field>` maps from, as written by
   `manifest-check.sh --task-skeleton` once KICK-aOrientedCast-1 lands:

   | Field | Label |
   |---|---|
   | `title` | `**Title:**` |
   | `goal` | `**Goal (1–2 sentences):**` |
   | `in` | `**IN scope:**` |
   | `out` | `**OUT / non-goals**` |
   | `todo` | `**To-do:**` |
   | `reuse` | `**Reuse:**` |
   | `acceptance` | `**Acceptance check**` |
   | `gates` | `**Gates it must pass:**` |

   A field is matched by its label up to the first `:**` or `**`, and its value runs to the next
   field line.
7. **The rendered prompt file** lives under `memory/builds/<slug>/prompts/`. Its name is
   `<date>-prompt-<unit-id>-<n>-<role-without-gov->.md`, or the build's first id when no unit is
   named. Its shape:
   - Line 1: `**Serves:** journal <ids>`.
   - Then `# <role> handoff — <unit id>`.
   - Then the marker line:
     `<!-- gov:handoff role=<name> build=<slug> unit=<id|-> path=<repo-relative path> role-sha=<12 hex> task-sha=<12 hex> -->`.
   - Then `## Role`, holding the rendered role verbatim.
   - Then `## Task`, holding one `### <input key>` block per input the role read, each verbatim from
     its source, then `### charter <§id>` blocks.

   `role-sha` and `task-sha` are the first 12 hex digits of the SHA-256 of the two sections' bytes,
   LF-normalized.
8. **The renderer CLI** is `python tools/roles/handoff.py`:
   - `render --role <name> --build <slug> [--unit <id>] [--card <path>] [--input <key>=<value>]... [--out <path>|--stdout] [--part full|task]`
     writes the file and prints its path, exits 1 on a refusal that names the missing input key, and
     exits 2 on usage.
   - `harness-args <harness>` prints the JSON `roles` object a harness takes, see 10.
   - `check <file>` re-derives both hashes.
9. **The rendered agent types** are `.claude/agents/<name>.md`, one per role with `agent` true:
   - Claude keys, plus `omitClaudeMd: true`.
   - gov's `workflow` and `writes`, carried for the hooks to read.
   - The rendered role as the body.

   Beside them sits `.claude/roles.json`, a GENERATED index: `{ "roles": { <name>: { "workflow",
   "writes", "agent" } }, "harnesses": [<repo-relative script path>] }`. The hooks kit reads only
   these two `.claude/` paths, never a `tools/roles/` file, so no kit names a sibling by literal.
10. **The harness `roles` argument** is an object mapping a harness's stage key to an agent type:
    - `unattended-build`: `specWriter`, `committer` and `disposal`.
    - `unattended-unit`: `builder`.
    - `tier2-review`: `diffFinder`, `specFinder`, `skeptic` and `synthesis`.

    A stage absent from it keeps today's spawn options, and the harness logs that per stage.

## Invariants for every unit

- Status `OPEN`, `rev-1`, `node a`, `base <sha>`, where `<sha>` is the pinned BASE that
  `bash tools/unattended/unattended.sh --status aOrientedCast` prints. Every unit is Tier-2: the full ten sections of
  `memory/TEMPLATE-SPEC.md`, including `§3 ### Edges` and `§10 Reuse audit`. `streams tooling` for
  TOOL, `kickoff` for KICK, `playbook` for PLAY. Give the header the `order` verb this table names.
  An `order` you cannot keep because of a write-set overlap you found is a §8 fork, never a silent
  change.

  | Order | Unit |
  |---|---|
  | 1 | TOOL-aOrientedCast-1 |
  | 1 | KICK-aOrientedCast-1 |
  | 2 | TOOL-aOrientedCast-2 |
  | 3 | TOOL-aOrientedCast-3 |
  | 4 | TOOL-aOrientedCast-4 |
  | 5 | TOOL-aOrientedCast-5 |
  | 6 | KICK-aOrientedCast-2 |
  | 7 | PLAY-aOrientedCast-1 |
  | 8 | TOOL-aOrientedCast-8 |
  | 9 | TOOL-aOrientedCast-6 |
  | 10 | TOOL-aOrientedCast-7 |

- A pass runs no merge bar, no self-test suite and no whole `*.test.sh`. Each criterion is observed
  by a DIRECT check, and §6 names its command: a checker on a staged break, one sliced arm, a
  fixture, a `--selftest`/`--check` flag, or a `python -c` / `node -e` probe. §7 names the legs the
  close's bar runs.
- Every new or moved arm is observed RED on a staged break, then GREEN once restored.
- §6 never names, as a backticked path, a file the unit itself creates: `check-spec-tokens.py` joins
  those against `git ls-files`. Name the observing command or the gate leg instead.
- Run `python tools/check-spec-tokens.py --list`, and put every `NEAR [guards]` leg it prints for
  your §4 `### Files touched (estimate)` on the §7 leg line.
- A kit file names nothing outside itself by literal (`tools/hooks/README.md`, "The authoring rule
  for kit files"; `tools/check-install-prefix.sh`). A sibling kit is reached by a render token or a
  derived path.
- Ask the naming question before writing a function name:
  `python3 tools/lexicon/lexicon.py --suggest <name> --as <cell>`. `VERB_OFFENDER_PIN` is an
  equality, so a definition outside the verb table reds the bar.
- No kit-version bump inside a unit; each touched kit moves once, after its last unit. Do not edit
  `memory/DECISIONS.md` or any backlog. Note discoveries in §8 or §3 Edges.
- **aRoutedQuill is landed and is reused, never re-specced**:
  - the card's `## route` and `--brief-skeleton` (KICK-aRoutedQuill-1);
  - `checkRouted`, `checkBuildable`, `readConfKey` and `ROUTED_PATHS` in the hooks kit's scratch
    guard (TOOL-aRoutedQuill-2);
  - the `SubagentStart` route context (TOOL-aRoutedQuill-4);
  - the routed-commits push leg (TOOL-aRoutedQuill-3).

  Read each before extending it, at its landed path.
- **aScoutedSeam owns the reuse-scout's content**, the card's `## reuse` section and the kickoff
  opt-in that triggers the scout. This build ships the `gov-reuse-scout` slot with a minimal body
  that defers to `tools/codebase-map/reuse-lookup.agent.md`, and edits no file under
  `tools/codebase-map/`.
- `§10` recall terms already used by the main loop:
  `role preamble GROUND brief spec writer builder lens skeptic synthesis handoff agentType workerType`.
  Run your own probe per unit as well (M5), and record the terms and what they surfaced.

## TOOL-aOrientedCast-1 — the role catalogue

**What.** Create the kit, `workflows.toml`, the ten role files, ten empty house overlays and a
checker. The checker is `python tools/roles/check_roles.py`, gated as a leg. It grades both
directions:
- every role's front matter against interface 3;
- every `workflow` against `workflows.toml`;
- every `roles` entry of a workflow against a role file;
- every `reads` key against interface 5's vocabulary;
- `writes` against its closed set;
- every `charter` id against a heading that exists in the governing doc;
- a body that is empty, or over a byte ceiling you price per role.

It also reds a role file no workflow names, and a workflow naming no existing role unless its
driver is `program` or `main-loop`. It prints the counts it graded and reds on zero.

**The role blocks are the substance.** Write each as the constant opening its agent should start
from. It says who the agent is, what it is producing, what it is NOT doing in this pass, what "done"
means, how it must return, and that it leaves owner prose and anything outside its task out. The
owner's own example, quoted in the prompt, sets the register: "You're a code architect, writing a
feature specification. You are not writing any code right now...".

A block POINTS at the sources that own a rule (`memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`,
the review protocol); it never restates them. The rule "a value stated beside its owner rots" binds
here.

Mine the harnesses for each role's craft text, the role-shaped prose only:
- `unattended-build.template.js`: the spec writer, the committer and the disposal agent.
- `unattended-unit.js`: the builder.
- `tier2-review.template.js`: the lenses, the skeptic and the synthesis.

The stage protocol a harness parses (schemas, `authored` naming, driver verbs) stays in the harness,
because the harness owns its return contract.

**`charter` per role.** Name the governing doc's sections each role needs once
`omitClaudeMd` removes the charter: the builder needs the cross-OS and commit-attribution rules, for
instance. Measure the governing doc's headings; do not guess them.

**Not here:** the renderer (unit 2), the agent render (unit 3) and any harness edit.

## KICK-aOrientedCast-1 — the card's `## task` gains To-do and Reuse, and a READY body must fill it

**Seam.** `TASK_SKELETON` in `skills/session-kickoff/manifest-check.sh` and `add_card_body` /
`--card --append`, which today grade only that cited tokens exist. Insert `**To-do:**` after OUT and
`**Reuse:**` after To-do, with the labels of interface 6. `--card --append` refuses, exit 1 with the
card left byte-identical, a body that carries a real READY line and a `## task` in which any of the
eight fields is absent, empty, `…` or a placeholder. The refusal names the field. Measure what a
"placeholder" is against the cards under `.git/orientation/` and against the skeleton itself, and
record hits and near-misses in §10.

**The adopter contract.** Check 10 byte-compares every manifest's sealed region with
`TASK_SKELETON`, so changing the skeleton reds every adopter manifest at its next `govkit update`
until the region is re-pasted. Design that migration: what the update does to an adopter's manifest,
or what the refusal says, and how gov's own `memory/guides/SESSION-KICKOFF.md` moves in the same
commit. Re-stamping `last-audit` and `last-body-change` there is owed (the memory note "stamps are
not one stamp" names five carriers).

**Interim reuse.** `**Reuse:**` holds the seams cited by path, or `no seam fits` with its evidence.
aScoutedSeam's later unit makes it a pointer to its `## reuse` section, so say that in §3 Edges as
`hands-off`.

**Not here:** the route, the brief skeleton, the engine's Step 5 (KICK-aOrientedCast-2).

## TOOL-aOrientedCast-2 — the handoff renderer

**What.** `tools/roles/handoff.py`, per interfaces 7 and 8.

- `render` resolves the role, appends its house overlay, then gathers each `reads` key from its
  source:
  - `task:*` and `card:*` from the card at `--card`. Default is the session's card, found the way
    `manifest-check.sh --card --path` finds it. The renderer may call that verb, or the hooks' own
    reader, but it never re-implements the card's location rule. Decide which, and record it.
  - `brief:*` from the build's prompt record carrying `## The prompt`, or the kickoff-written brief
    record, under `memory/builds/<slug>/prompts/`.
  - `input:*` from `--input`.
  - `charter` ids from the governing doc, by heading. Locate the doc the way the agent-instructions
    kit wires it; never assume `AGENTS.md`.
- A required key that resolves to nothing REFUSES, naming the key and its source. A missing
  optional key is listed on one line in `## Task` and never silently dropped.
- `--part task` prints only the marker and `## Task`, which is what a native-typed spawn passes as
  its prompt: the role is already its system prompt.
- Stdlib only. MEMORY_ROOT comes from `.memory-tree.conf` the way the hooks kit reads it. Lowercase
  hex hashes, with LF-normalized input so a CRLF working copy hashes like its blob.

**Fixtures.** A fixture card, brief and spec under a scratch root render a byte-stable file. The
missing-required refusal and the `?`-optional announcement are observed.

**Not here:** spawning anything, and the hooks.

## TOOL-aOrientedCast-3 — native agent types, trimmed of the charter

**What.** `python tools/roles/render_agents.py --write|--check`, per interface 9. Gov's
`.claude/agents/` and `.claude/roles.json` are generated and committed. `--check` byte-compares them
and is a gate leg. The `harnesses` list in `roles.json` is derived from `workflows.toml`. Pin the
`.claude/agents/` files `eol=lf` in `.gitattributes` (memory note "MSYS awk and grep drop CR").

**Evidence.** The agent-type probe decided both questions on CLI 2.1.292. This unit's acceptance
RE-RUNS that probe against the RENDERED `gov-builder` and `gov-spec-writer` files, with the
instrument the record describes, and does not cite the record as proof. Two open edges go in §3:
- whether a definition created in a RUNNING session is spawnable;
- the CLI version floor, which is 2.1.292.

`TOOL-aReplayedCard-5` measured "not spawnable" mid-session, so say what a session that just ran
`--write` must do.

**Rollout inside this run.** This session's agent registry was read before `.claude/agents/` existed,
so this run's own later passes cannot spawn the rendered types. Say so in §3. Units 4 and 5 keep
working by passing no `roles` arg here.

**Not here:** govkit wiring for adopters (unit 8).

## TOOL-aOrientedCast-4 — the build harnesses take roles

**What.** `unattended-build.template.js`, its rendered `.js` and `unattended-unit.js` take
interface 10's `roles`:
- every `agent()` in a named stage carries `agentType: roles.<stage>`;
- `unattended-build` passes `roles.builder` on through `dispatch.args`.

Delete from the prompts the role-shaped prose unit 1 moved into role files, and keep the stage
protocol. Today's text is the fallback when `roles` is absent, and the harness LOGS that fallback
per stage. Refuse an agent type that fails the `workerType` shape
`tier2-review.template.js` already enforces; reuse that check rather than writing a second one.

**The builder no longer writes specs.** `unattended-unit.js` tells the builder two things that
unit 6 forbids:
- on a divergence, to change the spec first (a rev bump);
- to flip its spec's status header to CLOSED in the pass commit.

Design the hand-back. On a divergence, the builder returns `committed: false` with a `why` naming
it, and the parent dispatches a `gov-spec-writer` rev bump before re-dispatching the unit. Unit 6's
fork decides how the status flip happens, and this unit's prompt follows whatever it decides. Write
the dependency as an `Edges` line both ways.

**Owner turn.** The unattended Skill's verbs (`memory/guides/UNATTENDED-VERBS.md` and its kit template)
tell the main loop how to compose the `Workflow` call. Say in §3 Edges whether the caller's
composition must change, and if it must, which kit file owns that text. The render step is
`check-protocol-parity.test.sh --render`, and its `--check` is the freshness observation.

**Not here:** the review harness (unit 5).

## TOOL-aOrientedCast-5 — the review harness takes roles

**What.** `tier2-review.template.js` and its render take interface 10's `roles`:
- finders spawn as `diffFinder` or `specFinder` by subject kind;
- skeptics as `skeptic`;
- the synthesis as `synthesis`.

`workerType` stays and keeps its meaning. Decide precedence when both are given, as an M3 fork with
its decision marked. The roles object JOINS `inputPrint` (the resume key), or a resumed run reuses
lens files written under different roles.

Lens texts stay two sibling top-level array literals: `agent-cap.js` denies a registry of lens sets.
The lens content is the per-lens VARIABLE part. The finder role block carries what every lens
shares, which today is the severity rubric and the probe rules.

**Not here:** `drift-audit-*.js`. Say in §3 whether they should follow, as a hands-off.

## KICK-aOrientedCast-2 — the attended router

**What.** A Skill `/build` at `.claude/skills/build/SKILL.md`, rendered by the roles kit from a
template in `tools/roles/`, with a byte-compare `--check` as the unattended kit renders its Skill.
It is the attended counterpart of `/unattended`, and the kickoff engine's Step 5 hands a code build
to it after the owner's go. Its steps run the workflows in `workflows.toml` stage order:
1. the card and the brief;
2. a rendered `gov-reuse-scout` handoff when the scout exists, otherwise the card's `**Reuse:**`;
3. `Workflow unattended-build.js` with `mode: attended` and `roles` from
   `handoff.py harness-args`, the audit only where the owner declared one;
4. one `Workflow unattended-unit.js` per unit, the card's `## route` appended per unit as
   aRoutedQuill requires;
5. `tier2-review.js`, then the bar once;
6. the wrap-up derivation (BUILD-METHOD M9).

Every agent prompt it writes is a rendered handoff.

**Converge, don't fork.** Name every step `/unattended` and `/build` share. Where one already
exists, point at it; where a step must differ, say why in one line. A second copy of the procedure
is the defect.

**The kickoff edit** is one clause in Step 5, inside the engine's byte headroom, with the
manifest stamps.

**Not here:** the reuse scout's trigger (aScoutedSeam's later unit).

## PLAY-aOrientedCast-1 — the charter

**What.** `coding-governance-agents.template.md` states the rule, in the fewest bullets that carry
it: agents are handed rendered roles; the main loop orients, hands off and keeps the books; and spec
writing, spec review, building and closing review run in their role agents. Fit §1's Definition of
Ready or §8 by what each already says (aRoutedQuill's DoR bullet is there). POINT at
`tools/roles/README.md` through the renderer's token convention; do not restate the catalogue.

Price the bytes against `tools/check-template-size.sh` and its recorded high-water, and prefer
externalizing to spending headroom (`.claude/rules/product.md`). Re-render this repo's `AGENTS.md`
through the playbook kit's renderer, and name in §7 the parity legs that grade the pair.

## TOOL-aOrientedCast-8 — adopter defaults

**What.**
- The `roles` kit enters `tools/govkit/registry.toml` and its default selection.
- `kit.toml` declares each file's role: `engine` for the base roles and scripts, `seed` for the
  house overlays, `project-owned` for tests.
- An adopter script renders `.claude/agents/`, `.claude/roles.json` and the `/build` Skill at
  install and at update, and its `--check` is a gate leg.
- `check-wiring.sh` reports an unrendered install.

Follow `TOOL-aRoutedQuill-5`'s shape for a default that is wired at install. Fixture targets go
through `tools/govkit/selftest.py`: ONE function or a slice, never the suite (memory note
"govkit slices and the guards that bite them"; the suite pins the common dir's HEAD in a linked
worktree).

## TOOL-aOrientedCast-6 — role-owned writes on the write gate

**What.** `checkRouted` in the hooks kit's scratch guard gains a ROLE arm, evaluated after
aRoutedQuill's buildable-unit arm and never instead of it:
- a write under `<MEMORY_ROOT>/builds/*/spec/` is admitted only when the payload's `agent_type`
  names a role whose `writes` is `spec`;
- a write under `ROUTED_PATHS` only when it names a role whose `writes` is `product`.

The writer's role is read from `.claude/roles.json` at the target's toplevel. The main loop, which
has no `agent_type`, is refused both. So is `workflow-subagent`, which is what a harness agent
spawned without `agentType` reads, as the probe shows. The refusal names the role that may write
and the handoff that reaches it.

**The status flip.** A unit's spec status header moves under two existing rules:
- aRoutedQuill admits a Tier-2 product write only at INPROGRESS;
- the unit harness has the builder set CLOSED in its pass commit.

Both are spec writes, which this arm gives to the spec-writer alone. Decide, as an M3 fork, how a
status flip reaches a spec. The options include:
- an Edit the hook can prove touches only the status header line, admitted from the routed unit's
  builder;
- a driver or renderer verb that a Bash call makes, which this gate never sees;
- a `writes` value allowing both classes.

Measure what each lets through.

**Arming.** The arm is armed when `.claude/roles.json` exists and parses; an absent index adds no
arm. Decide, as an M3 fork:
- whether an index that exists but names no `spec` or `product` writer is UNARMED and refuses, which
  is aRoutedQuill's rule for its conf;
- what a repository whose roles kit is not installed sees.

Enforcement starts at landing with no warn phase, by the owner's ruling. State the gate's ceiling in
its header, as aRoutedQuill's does: Bash writes and a hook-less run pass it.

**Rollout inside this run.** This session's hooks run from the PRIMARY tree, which the orientation
card's `tree —` line shows, so a scratch-guard edit on this branch binds this session only once it
reaches local `main`. Say so in §3, together with what the close's repairs then do.

## TOOL-aOrientedCast-7 — the spawn guard

**What.** `agent-cap.js` (matcher `Workflow|Agent`) gains a rule:
- An `Agent` call is admitted only when `tool_input.subagent_type` is a role in `.claude/roles.json`
  with `agent` true, and `tool_input.prompt` carries a `gov:handoff` marker whose `role` equals it.
  The marker's `path` must name a tracked or working-tree file whose own marker and `task-sha` match
  the prompt's `## Task` bytes.
- A `Workflow` call is admitted only when its `scriptPath` is in `roles.json`'s `harnesses` and its
  `args` carry a `roles` object of known types; an inline `script` is refused.

Measure, before choosing, what that means for the built-ins:
- `Explore`, `Plan` and `claude-code-guide`: route them through `gov-researcher`, or name what is
  lost;
- the drift-audit workflows;
- `orient-counterfactual.js`.

Record hits and near-misses over this repo's last week of spawns where the transcripts allow. The
same arming question as unit 6, the same no-warn ruling, and the same ceiling sentence apply.
SendMessage to another session is NOT gated here: say so in §3 as a hands-off. The `gov-session`
role and the renderer are its workflow today.

**Not here:** the write gate (unit 6).
