# TOOL-aOrientedCast-10 — every role runs at its declared effort, from one owner-editable policy file

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-2 · base 646d4a73 · streams tooling · order 8 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-10-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aOrientedCast-10-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aOrientedCast-10-0-owner-addendum.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-10-0-owner-addendum.md) | research | TOOL-aOrientedCast-11 |
| [2026-10-11-prompt-TOOL-aOrientedCast-10-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-10-1-spec-brief.md) | journal | TOOL-aOrientedCast-11 |

<!-- /gen:spec-records -->

## 1. Goal

The owner wants each kind of agent to run at a reasoning effort he sets once and can change freely:
medium for a generic agent, extra (`xhigh`) for prompt and spec writers, medium for spec review,
high for builders and for Tier-2 diff and closing reviews. Today every agent runs at the session's
effort. This unit adds one seeded policy file to the roles kit, writes the resolved `effort:` into
every rendered agent type, and lets the three harnesses pass a per-stage effort through `agent()`
options, so a role that serves two workflows runs at each workflow's level.

## 2. Scope (IN)

- **S1** — A policy file at `house/policy.toml` in the roles kit, shipped as govkit role `seed`, in
  the grammar of §4 "Data model": an `[effort]` table holding `default`, an `[effort.roles]` table of
  role entries and one `[effort.stages.<workflow>]` table per workflow that overrides a stage. Gov's
  copy carries the owner's defaults of §4 "The owner's defaults". Observed by AC1.
- **S2** — `load_policy(kit_dir, roles, workflows)` in `roles_lib.py` is the one reader and the one
  validator. It returns the parsed policy, or raises `RolesError` whose message holds one line per
  defect of §4 "Refusals". `resolve_effort(policy, slot)` and
  `resolve_stage_efforts(policy, workflow)` are the one resolution, in the precedence of §4
  "Resolution". Observed by AC1 and AC2.
- **S3** — `render_agents.py` writes `effort: <level>` into every rendered agent type, the line after
  the role's Claude keys and before `omitClaudeMd: true`, resolved by `resolve_effort`. Every mode
  reads the policy through `load_policy`, so a policy defect exits 2 naming it. Observed by AC2 and
  AC3.
- **S4** — `render_agents.py --selftest` gains arm 11: a role entry, the default and a refused value
  over its fixture catalogue, as §4 "Self-test arm 11" states. Observed by AC4.
- **S5** — `check_roles.py` gains rule R12, one defect line per line of `load_policy`'s refusal, so
  the catalogue checker and the render refuse the same policy for the same reason. Observed by AC2.
- **S6** — `handoff.py stage-efforts <workflow>` prints, as one line of sorted JSON, the resolved
  effort of every stage key of that workflow's `stages` table. Exit 1 on a workflow with no `stages`
  table, an unknown name or a policy defect, each named. Observed by AC5.
- **S7** — The three harnesses take an optional `efforts` argument, an object of stage key to level,
  as §4 "The harness argument" states: `tier2-review.template.js` and its render,
  `unattended-build.template.js` and its render, and `unattended-unit.js`. A stage it names passes
  `effort` in that stage's `agent()` options; a stage it does not name passes none and the harness
  logs that per stage, as it logs a `roles` fallback. A malformed `efforts` refuses before any spawn.
  Observed by AC6.
- **S8** — The callers pass it. The `/build` Skill template and its render, and the unattended verbs
  template and its render, say every harness call also carries `efforts`, the JSON
  `handoff.py stage-efforts <workflow>` prints for the workflow that call runs.
  `tools/workflows/README.md` documents the argument beside `roles`. Observed by AC7.
- **S9** — The descriptor and the deployer's pins: the roles kit's `kit.toml` names
  `house/policy.toml` in its seed list, and the default-plan arm of `tools/govkit/selftest.py` moves
  its seed figure by one. Observed by AC8.
- **S10** — Gov's own render is regenerated, and the map's generated symbols with it. The roles kit's
  README gains a section on the policy file: its tables, its precedence, that it is the adopter's to
  edit, and that a changed effort needs a re-render and a new session. NOT OBSERVED by a criterion:
  the README is prose, and the review reads it against §4. Gov's render is observed by AC3.
- **S11** — The live witness: the probe of §4 "The probe" shows a rendered type's effort and a
  per-stage override in the hook payload of the agent they spawned. Observed by AC9.

## 3. Non-goals (OUT)

- The main session's own effort. It is the owner's setting for his session, and no file here can
  reach it. A brief the main loop writes by hand is written at that effort.
- An effort for `gov-session`. It declares `agent: false`, so no agent type carries a key, and the
  session that receives its handoff runs at that session's own setting (§8 F1).
- New roles, new workflows, or a `stages` key a harness does not already have (§8 F2).
- The gate allowlist the same file carries once `TOOL-aOrientedCast-11` adds it.
- An `effort` front-matter key in a role file. The policy file is the one source, and a second key
  in the role would be a second answer to one question.
- Joining `efforts` to the review harness's resume key. Effort moves how hard a judge reasons, not
  what it was asked, so a resumed run may reuse a lens file written at another level.
- A kit version bump. The roles, workflows and unattended kits move once, after this build's last
  unit touching each.

**What it is built on.** This unit extends what earlier units of this build landed:
`TOOL-aOrientedCast-1`'s role files, workflow table and library; `TOOL-aOrientedCast-3`'s renderer
and gov's render; the `roles` arguments `TOOL-aOrientedCast-4` and `TOOL-aOrientedCast-5` gave the
harnesses, whose key sets and refusal shape `efforts` follows; `TOOL-aOrientedCast-8`'s seed list and
default-plan pins; `KICK-aOrientedCast-2`'s `/build` Skill; and `TOOL-aOrientedCast-9`'s verbs
sentence. Their specs were written before this unit existed and declare no edge to it, and a
one-sided edge reds the hygiene gate's join, so the dependency is stated here rather than as an
edge. `TOOL-aOrientedCast-7`'s rule reads `roles` and no other `args` key, so a harness call carrying
`efforts` is judged by it as before.

### Edges

- **hands-off** `TOOL-aOrientedCast-11` — adding the gate allowlist table to the same policy file and
  to `load_policy`, so the owner adjusts both in one place.
- **consumes-from** external — Claude Code 2.1.292 or later, whose agent loader reads `effort` from
  an agent definition and whose `Workflow` runtime reads `opts.effort` (§4 "Evidence").

## 4. Design

### Evidence

Read at `646d4a73` plus this build's commits to `6ca3cb2d8`, on 2026-10-11, node a.

- The CLI on PATH answers `2.1.292 (Claude Code)`. Its binary (`~/.local/bin/claude.exe`, read as
  text) declares the agent-definition schema with
  `effort:$e([j(["low","medium","high","xhigh","max"]),k().int()]).optional()`, described "Reasoning
  effort level for this agent. Either a named level or an integer", and its markdown loader warns
  `has invalid effort '…'. Valid options: low, medium, high, xhigh, max or an integer`. A spawned
  agent takes `effort: w.effort` from its selected definition, for an `Agent` call and a `Workflow`
  `agent()` given `agentType` alike.
- The same binary documents the `Workflow` script API: "opts.effort overrides the reasoning effort for
  this agent call ('low' | 'medium' | 'high' | 'xhigh' | 'max') — omit to inherit the session
  effort". Its `agent()` applies it over the definition: `lt=SU(ke?.effort),Ze=lt!==void 0?{...Be,
  effort:lt}:Be`. The integer form is not documented there.
- The CLI downgrades silently: `if(r==="xhigh"&&!ynt(n))r="high"` and the same for `max`, per model.
  The UI labels `xhigh` "Extra", which is the owner's word.
- The `PreToolUse` hook payload carries `effort: { level }`, "Active effort level for the current
  turn … Also exposed to hook commands and Bash as the CLAUDE_EFFORT env var".
- `render_agents.py` emits the Claude keys in `CLAUDE_KEYS` order, then `omitClaudeMd`, `workflow` and
  `writes` (`tools/roles/render_agents.py:58`, `:108-123`); every mode renders in memory first and
  exits 2 on a `RolesError` (`:199-212`). Its self-test builds a fixture catalogue in a temporary
  directory (`:241-264`) and counts arms 1 to 10 (`:274-367`).
- `roles_lib.py` is the one reader of the kit's files (`tools/roles/roles_lib.py:1-11`), and its
  front-matter keys are a closed tuple split from one string (`:22-23`).
- `workflows.toml` maps each workflow-driver harness's stage keys to slots: `spec-write` names
  `specWriter`, `disposal`, `builder`, `specFinder`, `skeptic` and `synthesis`; `spec-review` names
  `specFinder`, `skeptic` and `synthesis`; `build` names `builder`; `closing-review` names
  `diffFinder`, `skeptic` and `synthesis` (`tools/roles/workflows.toml:37`, `:47`, `:57`, `:67`).
  So `gov-skeptic` and `gov-synthesizer` serve both spec review and closing review.
- `handoff.py harness-args` unions the `stages` tables of every workflow a harness serves and refuses
  a key that maps to two slots (`tools/roles/handoff.py:350-368`). The review harness serves two
  workflows, so a per-harness union cannot carry two efforts for one key.
- The review harness reads `roles` per stage, picks the finder key by subject kind, and builds one
  options object per stage (`tools/workflows/tier2-review.template.js:225-244`); its args header
  documents each key (`:112-125`). The build harness's stage keys are `ROLE_KEYS`
  (`tools/workflows/unattended-build.template.js:443`); it forwards the audit's three review keys
  into the review call (`:485-488`, `:1546-1547`) and `roles.builder` into `dispatch.args`
  (`:2365-2370`). The unit harness's one key is `builder` (`tools/workflows/unattended-unit.js:147-173`)
  and it spawns once (`:291`).
- The house overlays are seeded and named one by one, because a list include claims literal paths
  only (`tools/roles/kit.toml:31-39`). `check_roles.py` grades `house/*.md` alone (R10,
  `tools/roles/check_roles.py:249`), so a `.toml` there is not an overlay.
- The default-plan arm pins the seed rows at 13 (`tools/govkit/selftest.py:6157`, the line holding
  `marks.get("write|seed", 0) + marks.get("KEEP|seed", 0) == 13`), read in a working copy where
  another pass is editing that file.

### Data model

`house/policy.toml`, read with `tomllib`:

```toml
# policy.toml — this repository's own settings for its role agents. Seeded: yours to edit.
# A changed value reaches an agent after `render_agents.py --write` and a new session.

[effort]
default = "medium"            # every role and stage this file does not name

[effort.roles]                # one entry per role slot
gov-orienter = "xhigh"
gov-spec-writer = "xhigh"
gov-spec-reviewer = "medium"
gov-builder = "high"
gov-diff-reviewer = "high"
gov-skeptic = "high"
gov-synthesizer = "high"

[effort.stages.spec-review]   # one table per workflow; keys are that workflow's stage keys
skeptic = "medium"
synthesis = "medium"

[effort.stages.spec-write]
skeptic = "medium"
synthesis = "medium"
```

The level vocabulary is `EFFORT_LEVELS` in `roles_lib.py`, split from the one string
`"low medium high xhigh max"`, with a comment citing the CLI version it was read from. The integer
form the agent loader also accepts is refused: the `Workflow` runtime documents only the five names,
and one vocabulary must serve both carriers.

### The owner's defaults

| Owner's words | Carrier | Level |
|---|---|---|
| generic agent | `default`: `gov-researcher`, `gov-reuse-scout` | `medium` |
| prompt writers | `gov-orienter` (§8 F1) | `xhigh` |
| spec writers | `gov-spec-writer` | `xhigh` |
| spec reviewers and their workflows | `gov-spec-reviewer`; the `spec-review` and `spec-write` review stages | `medium` |
| code builders | `gov-builder` | `high` |
| Tier-2 diff and closing reviews | `gov-diff-reviewer`, `gov-skeptic`, `gov-synthesizer` | `high` |

### Resolution

- A role's effort, `resolve_effort(policy, slot)`: its `[effort.roles]` entry, else `default`.
- A stage's effort, `resolve_stage_efforts(policy, workflow)`: for each key of the workflow's
  `stages` table, its `[effort.stages.<workflow>]` entry, else the effort of the slot that table maps
  it to.

With gov's file, `stage-efforts spec-review` prints `{"skeptic":"medium","specFinder":"medium",
"synthesis":"medium"}` and `stage-efforts closing-review` prints `{"diffFinder":"high",
"skeptic":"high","synthesis":"high"}`.

### Refusals

`load_policy` collects every defect, then raises once. Each line names the file, the dotted key and
the rule:

- the file absent, or not valid TOML (§8 F3);
- a top-level key other than `effort`, or an `effort` key other than `default`, `roles` and `stages`;
- `default` absent;
- a level outside `EFFORT_LEVELS`, naming the five;
- a `roles` entry naming no role file, or naming a role whose `agent` is false, since no agent type
  carries its key;
- a `stages` table naming no workflow, or a workflow with no `stages` table;
- a stage key that workflow's `stages` table does not hold, naming the keys it does.

### The harness argument

`efforts` is optional, and absent means `{}`. It is refused, with a message opening
``<harness>: `efforts` `` as each harness's `roles` refusal opens, when it is not a plain object,
when a key is not one of that harness's own stage keys, or when a value is not a string of lower-case
letters. The level vocabulary is the library's; a harness grades only the shape, so no second copy of
the vocabulary exists in JavaScript. The keys are the ones `roles` takes, read from the same list in
each file:

| Harness | Keys | Where `effort` goes |
|---|---|---|
| review | `diffFinder`, `specFinder`, `skeptic`, `synthesis` | the finder options by the kind's finder key, the skeptic and synthesis options; never the resume probe |
| build | `ROLE_KEYS` | the spec-writer, committer and disposal spawns; the audit's three review keys forwarded as the review call's `efforts`; `builder` forwarded in `dispatch.args` as `efforts: { builder }` |
| unit | `builder` | the one builder spawn |

`efforts` is independent of `roles` and `workerType`: an untyped stage still takes its level. Each
harness logs one line per stage, `effort <key>: <level> — efforts.<key>` or `effort <key>: the agent
type's own, else the session's — no efforts.<key>`.

### Self-test arm 11

`build_fixture` writes a policy file into every fixture kit, `default = "medium"` and nothing else,
so arms 1 to 10 render as they do today apart from the new line, and an absent file cannot read as
the fixture's normal state. Arm 11's fixture writes one whose `default` is `low` and whose
`[effort.roles]` sets `r-one` to `high`. After `--write`, `r-one.md` carries `effort: high` and `r-two.md` carries `effort: low`, each
on the line before `omitClaudeMd: true`. With `r-two` set to `extra`, `--write` exits 2 naming
`r-two` and the five levels, and writes nothing.

### The probe

The instrument of `TOOL-aOrientedCast-3`'s probe re-run (its spec §4 "The probe re-run"), with these
changes. The clone is taken at this unit's pass commit, under a short `%TEMP%` root. The logger hook
writes `agent_type` and `effort.level` from each `PreToolUse` payload. The task text is: "This is a
probe. Run `echo probe` once, then stop." Arms, one session:

- a1: `Agent`, `general-purpose`, the control, which reads the session's level.
- a2: `Agent`, `gov-builder`; a3: `Agent`, `gov-spec-writer`.
- w1: `Workflow`, `agentType: 'gov-skeptic'` with no `effort`; w2: the same with `effort: 'medium'`.

An arm is VALID when its log holds one `PreToolUse` line on one `agent_id` carrying an
`effort.level`. The record names the CLI version, the model, the clone's commit and the session's own
level, and carries the logger and the `Workflow` script as fenced blocks.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `load_policy` | function, the one reader and validator of the policy file | `py.function`; `lexicon.py --suggest load_policy --as py.function` answered OK |
| `resolve_effort` | function, a role's level | `py.function`; answered OK |
| `resolve_stage_efforts` | function, a workflow's stage levels | `py.function`; answered OK |
| `print_stage_efforts` | function, the `stage-efforts` verb | `py.function`; answered OK |
| `EFFORT_LEVELS` | tuple constant | none: no constant cell is declared in `.lexicon.conf` |
| `stage-efforts` | `handoff.py` subcommand | none: `harness-args` is the precedent spelling |
| `efforts` | harness argument key | none: argument keys are not a declared cell |

### Rollout

Lands at order 8, beside `PLAY-aOrientedCast-1`, whose write set it does not touch. The pass commit
carries the policy file, the library, the checker, the renderer, the handoff verb, the three harnesses
and their renders, the two caller templates and their renders, the README, the descriptor row, the
selftest pin and the regenerated symbols. Gov's re-render of `.claude/agents/` follows in a second
commit of the same pass under its own `--dispatch`, because `--dispatch` refuses a declaration naming
a generated index together with its generator (check 49), as `PLAY-aOrientedCast-1`'s re-render did. `gen_map.py --write` runs before the
commit, because new functions stale `symbols.json`. The renderer's restart line then states the
truth for this session: its registry predates every changed type, so no later pass of this run
spawns at the new levels, and `TOOL-aOrientedCast-3`'s §4 "Rollout" already says what a new session
does. At an adopter the next `govkit update` seeds the file once and the re-render writes the levels.

### Files touched (estimate)

`tools/roles/house/policy.toml` · `tools/roles/roles_lib.py` · `tools/roles/render_agents.py` · `tools/roles/check_roles.py` · `tools/roles/handoff.py` · `tools/roles/kit.toml` · `tools/roles/README.md` · `tools/roles/SKILL.template.md` · `.claude/skills/build/SKILL.md` · `.claude/agents/` · `tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` · `tools/workflows/tier2-review.test.sh` · `tools/workflows/unattended-build.template.js` · `tools/workflows/unattended-build.js` · `tools/workflows/unattended-build.test.sh` · `tools/workflows/unattended-unit.js` · `tools/workflows/README.md` · `tools/unattended/VERBS.template.md` · `memory/guides/UNATTENDED-VERBS.md` · `tools/govkit/selftest.py` · `memory/map/features/roles.md` · `memory/map/features/review-harnesses.md` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **An `effort` key in each role file.** The owner asked for one file he edits; nine keys across nine
  engine files are overwritten by every update, and a seeded file is the layer an update keeps.
- **Effort carried in `.claude/roles.json`.** No hook reads it, and the agent type already carries it
  where the CLI reads it.
- **A harness reading the policy itself.** A workflow script holds no file read and names no sibling
  kit, so the level must arrive in `args`, as `roles` does.
- **Extending `harness-args` to print efforts.** Its union over the review harness's two workflows is
  exactly where `skeptic` carries two levels; a verb keyed by workflow has no union to refuse.
- **Accepting the integer form.** The `Workflow` runtime does not document it, and one stage's level
  must be legal on both carriers.

## 5. Production-readiness checklist

- security — No new write path: the policy file is read, and the render writes the owned paths it
  already writes. A hostile edit raises a role's spend, not its reach.
- perf / scale — One TOML parse per render and per `stage-efforts`; nothing on a hook path.
- error / empty / loading states — Every policy defect exits 2 from the render and 1 from the
  checker and the verb, each line naming file, key and rule; a malformed `efforts` refuses before any
  spawn.
- observability — Each harness logs every stage's level and its source; the restart line names a
  changed type.
- risks — The CLI downgrades `xhigh` and `max` to `high` on a model that lacks them, silently; the
  probe records the model, and the README states it. Higher levels spend more tokens per agent, which
  is the owner's trade. A caller that omits `efforts` runs a shared role at its type's level, which
  for a spec audit is `high` rather than `medium`, and the per-stage log says so.
- testing — Arm 11 of the render self-test, the harness suites' new arms, and the direct probes of
  §6.
- migration — None in gov beyond the re-render. An adopter receives the seed at its next update.
- user docs — The roles kit's README section of S10, and the comment at the head of the policy file.

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag: each is a probe of this unit's own
code, a fixture, or the product's own command outside the leg's argv. Every new suite arm is listed
under `New arm:` in §7, and the main loop observes it RED and then GREEN at the close (M8).

- **AC1** — When `python -c` imports `roles_lib` from the roles kit and calls `load_policy` over the
  kit with its own roles and workflows, then `resolve_effort` for every role whose `agent` is true,
  the nine levels equal §4 "The owner's defaults" row for row.
  Red when: a role reads the default where the owner named a level, or the policy file is not read.
  figure: PINNED to the owner's table of 2026-10-11.
- **AC2** — When a scratch copy of the roles kit holds each staged break of §4 "Refusals" in turn
  (`extra` as a level, `gov-nobody` as a role, `gov-session` as a role, `orient` as a stages table,
  `diffFinder` under `spec-review`, `default` absent, the file absent), a `python -c` call of
  `load_policy` raises `RolesError` naming the key, and a `python -c` call of `check_roles.check_roles`
  over that copy returns one `R12` defect naming the same key.
  Red when: a defect passes, or the checker and the loader name different causes.
  fixture: a scratch copy of the kit directory under the session scratchpad; nothing in the tree
  holds a broken policy.
- **AC3** — When `python tools/roles/render_agents.py --write` runs in gov, each of the nine files
  under `.claude/agents/` carries one `effort:` line equal to AC1's level for its role, on the line
  before `omitClaudeMd: true`, and `python tools/roles/render_agents.py --check` then exits 0. With
  `gov-builder` staged to `max` in the policy and no re-render, `--check` exits 1 naming
  `gov-builder.md`; restored, it exits 0.
  Red when: a type lacks the key, carries another level, or a policy edit leaves the render fresh.
- **AC4** — When a scratch driver imports `render_agents` and calls `build_fixture` and `run_mode`
  over the arm-11 catalogue of §4 "Self-test arm 11", `r-one.md` carries `effort: high`, `r-two.md`
  carries `effort: low`, and with `r-two` set to `extra` the call returns 2 and the fixture's agent
  directory is unchanged.
  Red when: the fixture renders without the policy, or a refused value writes a file.
- **AC5** — When `python tools/roles/handoff.py stage-efforts spec-review` runs it prints
  `{"skeptic":"medium","specFinder":"medium","synthesis":"medium"}`, `closing-review` prints the
  three keys at `high`, and `build` prints `{"builder":"high"}`; `orient` and `nope` each exit 1
  naming the workflow.
  Red when: a shared role reads one level in both review workflows, or a stage-less workflow prints
  an empty object.
- **AC6** — When the stub run of `TOOL-aOrientedCast-5`'s §6, extended to each harness, evaluates
  spec-audit args carrying `efforts: { specFinder: 'medium', skeptic: 'medium', synthesis: 'medium' }`,
  every `find:`, `verify:` and `synth` spawn's options carry `effort: 'medium'` and the resume probe's
  carry none; diff args with `{ diffFinder: 'high' }` give `find:` spawns `high` and `verify:` spawns no
  key. The unit harness with `{ builder: 'max' }` spawns its builder with `effort: 'max'`, and the build
  harness forwards `{ skeptic: 'medium' }` into its review call's `efforts` and `{ builder: 'high' }`
  into `dispatch.args`. Each of `efforts: []`, `{ finder: 'high' }` and `{ skeptic: 'High' }` throws a
  message opening with the harness name and `` `efforts` `` before any spawn.
  Red when: a named stage spawns without its level, an unnamed stage gains one, or a malformed
  argument reaches a spawn.
  fixture: scratch drivers under the session scratchpad, each copying the stub shape of its harness's
  suite; nothing in the tree holds one.
- **AC7** — When `grep -c "stage-efforts"` runs over the `/build` Skill template, its render, the
  unattended verbs template, its render and `tools/workflows/README.md`, each prints at least 1, and
  the Skill's render equals a fresh render from its template.
  Red when: a caller composes a harness call with no source for `efforts`.
- **AC8** — When `grep -c policy.toml tools/roles/kit.toml` runs it prints 1, the line inside the
  seed rule's include list, and `grep -n "seed\", 0) == 14" tools/govkit/selftest.py` prints the
  default-plan arm's seed comparison.
  Red when: the policy previews as an engine write, which an update would overwrite.
- **AC9** — When the probe of §4 "The probe" runs once, a2 reads `high`, a3 reads `xhigh` or reads
  `high` with the record naming the model the CLI downgrades, w1 reads `high` and w2 reads `medium`,
  and the control a1 is valid and reads the session's level.
  Red when: a rendered type's level does not reach its agent, or `opts.effort` does not override it.
  cost: one nested `claude -p` session of five spawns, minutes and its tokens.
  permission: it launches a nested session in a throwaway clone; a pass refused that launch returns
  this criterion to the main loop.
  fixture: the clone and its logger hook exist only for the run.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `tier2-review self-test` · `unattended-build self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `review-join self-test` · `verifier fan-out self-test` · `unattended skill wiring` · `unattended kit gate` · `check-wiring self-test` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/render_agents.py --selftest · covers AC4 · arm 11, against a renderer whose effort line or policy refusal is staged out · none
New arm: tools/workflows/tier2-review.test.sh · covers AC6 · an `efforts:` block over the stub runner, against a render whose refusal or routing is staged out · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/workflows/unattended-build.test.sh · covers AC6 · an `efforts:` block over both harnesses' stubs, against a render whose forwarding or refusal is staged out · `FLOOR_ASSERTIONS` raised by the assertions added

The three arms are written in the pass and run first at the close, where the main loop observes each
RED on its staged break and GREEN restored (M8). No pass runs a leg above.

## 8. Open questions

- **F1 — Which role is a "prompt writer"?**
  No role in the catalogue is named for it. Options:
  - (a) `gov-orienter`. It derives the card's task block, which is the source of every rendered
    handoff's `## Task`, so it writes the substance of every prompt a role agent receives.
  - (b) `gov-orienter` and `gov-session`. `gov-session` declares `agent: false`: no agent type carries
    a key, and the session receiving its handoff runs at its own setting, so its entry would reach
    nothing. A key that reaches nothing fails this unit's goal and is refused by §4 "Refusals".
  - (c) A new role `gov-prompt-writer`. It needs a workflow outside the ten `TOOL-aOrientedCast-1`
    pinned, a slot, a ceiling, a seed overlay and a route that spawns it, and nothing spawns it today.
    That is a new public surface, M3's veto 2, and it leaves the route open as a follow-up.
  Recommendation: (a). (b) carries a dead entry and (c) is vetoed; the main loop's own hand-written
  briefs are out of any file's reach (§3).
  RESOLVED (agent, 2026-10-11, delegated): (a), `gov-orienter` at `xhigh`, and an entry for an
  `agent: false` role is refused.
- **FACT-QUESTION · F2 — How do `gov-skeptic` and `gov-synthesizer` run at `medium` in spec review and
  `high` in closing review?**
  Options: (a) a per-stage effort the harnesses pass through `agent()` options, which holds only if the
  `Workflow` runtime accepts one; (b) per-workflow role types, `gov-spec-skeptic` and
  `gov-spec-synthesizer`, with their own files, overlays and ceilings.
  Probe: read the 2.1.292 binary as text for the `Workflow` script API's documentation of `opts.effort`
  and for its application in `agent()`. Liveness: the same read must find the documented
  `opts.agentType` string, which this build's agent-type probe observed working; a read that misses it
  is blind. Observation (§4 "Evidence"): both are present, and `agent()` applies `opts.effort` over the
  definition's. So (a) holds.
  Between the two survivors M3 decides. (a) gives every stage of every workflow an owner-settable
  level, which the brief's "one entry per role or workflow stage" asks for, with one body per role.
  (b) covers two stages only, duplicates two role bodies that then drift, adds two slots, two seeds and
  two pins every adopter's install counts, and still needs `harness-args` to split by workflow.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a). The rendered type carries the role's level, and a
  workflow's `[effort.stages]` table overrides it through `efforts`, `stage-efforts` and `opts.effort`.
- **F3 — What does an absent policy file mean?**
  Options: (a) refuse, naming the file, so every render and the checker exit non-zero until it is
  restored; (b) fall back to `medium` for every role with a `note` line. Under (b) an adopter who deletes
  the seed silently loses every level the owner set, and a note is a skip that reads as coverage.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a), a §4 "Refusals" line.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · §4 Rollout: gov's re-render of the agent types lands in a second commit of the pass, since `--dispatch` refused declaring `.claude/agents` beside `render_agents.py` (check 49); status CLOSED.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read an owner-editable config of per-role reasoning
effort and write it into rendered agent definitions and per-stage harness agent options"` ranked
generic readers first: `read_text`, `read_conf` and `read_conf_key`, and `RolesError` and `load_roles`
in `tools/roles/roles_lib.py`. No existing seam reads an effort; the seams extended are this kit's
own: `roles_lib.py` as the one reader, `render_agent_file` and `run_selftest` in
`tools/roles/render_agents.py`, `print_harness_args`'s shape in `tools/roles/handoff.py`, and each
harness's `roles` parse and per-stage options, which `efforts` follows key for key. The level
vocabulary was read from the CLI binary, the external owner of it.

`python tools/memory-recall/query.py "how does a role agent get its reasoning effort, and which
harness stages pass agent options"` surfaced this unit's handoff, `TOOL-aOrientedCast-4` and
`TOOL-aOrientedCast-5`'s `roles` arguments, the agent-type probe record, and `TOOL-aMendedFleet-67`'s
record of `agentType` in a workflow `agent()` call. No record had settled an effort before.

Recall terms used: `effort agentType workerType roles harness-args render_agents omitClaudeMd agent type stage spawn options Workflow`
