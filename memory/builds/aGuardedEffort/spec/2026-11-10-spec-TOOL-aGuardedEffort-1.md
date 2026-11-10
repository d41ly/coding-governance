# TOOL-aGuardedEffort-1 — the spawn guard refuses a role spawn or a harness call at a level the model's effort profile does not give

**Status:** INPROGRESS · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 1 · closes TOOL-aProfiledEffort-6 · ratified 2026-11-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aGuardedEffort-1-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aGuardedEffort-1-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aGuardedEffort-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aGuardedEffort-1-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/hooks/agent-cap.js` gains rule 8. On an `Agent` or `Workflow` call that rule 6 admits, it
compares the level the call will run at with the level the effort policy gives the model the call
will run on, and refuses a difference at the tool call. Today a session that forgets the model
argument runs every role at the default tables' level, and only the `agent` line shows it
afterwards. The brief is
`memory/builds/aGuardedEffort/prompts/2026-11-10-prompt-TOOL-aGuardedEffort-1-brief.md`.

## 2. Scope (IN)

- **S1** — `tools/roles/render_agents.py` writes an `effort` key into the role index, in the shape
  of §4 "Data model", and `.claude/roles.json` is re-rendered by
  `python tools/roles/render_agents.py --write`. Observed by AC7.
- **S2** — `loadRoleIndex` in `tools/hooks/scratch-guard.js` returns the index's `effort` value, or
  null when the key is absent, and answers `broken` when the key is present and not the shape of
  §4. Observed by AC8.
- **S3** — `readSessionModel` in `tools/hooks/agent-cap.js` reads the model of the last main-chain
  assistant entry of a transcript, per §4 "The model". Observed by AC1 and AC5.
- **S4** — `resolveModelProfile` in the same file answers which profiles of the index match a model
  id, by the resolver's word rule, and is exported. Observed by AC6.
- **S5** — `checkEffortLevel` grades an `Agent` call per §4 "The Agent verdict". Observed by AC1,
  AC2 and AC4.
- **S6** — `checkEffortLevel` grades a `Workflow` call per §4 "The Workflow verdict", and the
  harness match of `checkHarnessCall` is extracted as `resolveHarnessEntry` so both callers share
  it. Observed by AC3.
- **S7** — A refusal names the role or stage, the level seen and where it came from, the level
  expected, the model and where it was read, and the `handoff.py` call that prints the right
  value, per §4 "The texts". Observed by AC1 and AC3.
- **S8** — Where no model can be read the call is admitted and one stderr line says the level was
  not checked and why. Observed by AC5.
- **S12** — A model id two profiles match is admitted with the not-checked line naming both
  profiles. An `Agent` call made where the hook's environment holds a non-empty
  `CLAUDE_CODE_EFFORT_LEVEL` is admitted with the not-checked line naming the variable, and a
  `Workflow` call there is graded as usual. Observed by AC11.
- **S9** — `main()` runs rule 8 after rule 6 admits and before rule 7, inside a try whose catch
  refuses. Observed by AC9.
- **S10** — The arms of §7 are added, and arm 6 of `tools/roles/adopt-roles.test.sh` stops
  asserting an empty stderr on its admitted spawn. NOT OBSERVED by a criterion: an arm is a
  declaration under §7, and the main loop sees each red and then green at the close.
- **S11** — The hook's header, the hooks README, the roles README sentence
  `The spawn guard reads no`, the map dossier `memory/map/features/agent-cap.md` and `help/roles.md`
  say what rule 8 checks and what it does not, per §4 "The documents". Observed by AC10.

## 3. Non-goals (OUT)

- The agents a running harness spawns through its own `agent()`. No hook sees them.
- The `committer` and `probe` stages, which no `stages` table keys. That is ask
  `TOOL-aProfiledEffort-5`.
- Any change to a level, a profile, `roles_lib.resolve_profile`, `resolve_effort` or
  `resolve_stage_efforts`, or to `handoff.py`.
- A second matching rule. The hook's match is the resolver's, held by the parity arm.
- A refusal when the model cannot be read, and a model read from anywhere but the call and the
  transcript.
- Which workflow a call to a harness serving two workflows runs. §4 "The Workflow verdict" states
  the ceiling this leaves.
- An `[[upgrade]]` row. No adopter-visible member disappears (`help/step-gate.md:3-8`).
- A by-hand move of `KIT_AGENT_CAP_VERSION` or any kit version. The lander's mint moves them.
- The many-megabyte transcript. The read is the whole file, as `format-guard.js` reads it.

### Edges

- **consumes-from** external — build `aProfiledEffort`, merged at `b12a9c81` on this branch and
  not yet on the default branch: the profile tables, `resolve_profile` and the two `--model`
  verbs. Without it there is no profile to grade against.
- **consumes-from** external — a Claude Code whose hook payload names `transcript_path` and whose
  transcript writes `message.model` on an assistant entry (§4 "Evidence").
- **hands-off** external — the version moves of the hooks and roles kits, written by the lander.

## 4. Design

### Evidence

Read at `4dca62ad` on 2026-11-10, node a. The header's base is the default-branch commit under it.

- Rule 6 runs first in `main()` and returns null to admit (`tools/hooks/agent-cap.js:865-887`).
  `checkHandoffSpawn` reads `subagent_type`, `prompt` and `description` (`:667-726`), and
  `checkHarnessCall` matches `scriptPath` against the index's `harnesses` and reads `args.roles`
  (`:735-766`). Neither reads `effort`, `efforts` or `model`.
- The index is read through `loadRoleIndex`, which returns `state`, `shown`, `roles`, `harnesses`
  and `gates` and no other key (`tools/hooks/scratch-guard.js:952-989`).
- `render_roles_index` writes `gates`, `harnesses` and `roles` (`tools/roles/render_agents.py:209-218`),
  and `--check` compares the index's bytes with the render (`:231-239`), so any key the render
  writes is graded with no new check code.
- `resolve_profile` lower-cases the id, splits it into runs of `[a-z0-9]`, and answers the one
  profile whose `match` holds a word; two hits raise (`tools/roles/roles_lib.py:630-644`).
  `load_policy` refuses one word in two profiles (`:502-516`).
- A rendered agent type carries the default tables' level (`tools/roles/render_agents.py:278-280`),
  and every role file is `model: inherit` (`tools/roles/agents/gov-builder.agent.md:5`).
- A harness applies a level only where its caller passed one, else the agent type's own
  (`tools/workflows/tier2-review.js:565`). So a stage with no `efforts` value runs at its slot's
  rendered level, which is not always the default tables' stage level: `gov-synthesizer` is `high`
  as a role and `medium` as a spec-review stage (`tools/roles/house/policy.toml:17`, `:19-21`).
- `tier2-review.js` is the harness of both `spec-review` and `closing-review`
  (`tools/roles/workflows.toml:45`, `:65`).
- `format-guard.js` reads `transcript_path` whole and skips a sidechain record
  (`tools/hooks/format-guard.js:282-324`, `:496-502`). `handoff.py agents` skips the model
  `<synthetic>` (`tools/roles/handoff.py:688-690`).
- PINNED, measured 2026-11-10 on this node. The 2.1.321 binary's `Agent` schema holds an optional
  `model` over `sonnet`, `opus`, `haiku` and `fable` that "takes precedence over the agent
  definition's model frontmatter", and an optional `effort`. Across the 40 newest local
  transcripts, `"model":"<synthetic>"` appears 164 times beside three real ids.
- Arm 6 of the roles adopter suite asserts an empty stderr on an admitted spawn whose payload
  carries no `transcript_path` (`tools/roles/adopt-roles.test.sh:206-208`). Every rule 6 allow arm
  of the hook's own suite asserts one too, over a hand-written index
  (`tools/hooks/agent-cap.test.sh:560-564`).

### Data model

The index gains one top-level key. Every value is resolved by the renderer, so the hook only looks
up.

```json
"effort": {
  "default":   { "roles":  { "<slot>": "<level>" },
                 "stages": { "<workflow>": { "<stage key>": "<level>" } } },
  "profiles":  { "<name>": { "match": ["<word>"], "roles": {}, "stages": {} } },
  "harnesses": { "<harness, as the harnesses list spells it>": ["<workflow>"] },
  "unset":     { "<workflow>": { "<stage key>": "<level>" } }
}
```

| Key | Value | Derived by |
|---|---|---|
| `default.roles` | every `agent`-true role's level | `resolve_effort(policy, slot)` |
| `default.stages` | each stage key's level, for every `workflow`-driver workflow with a `stages` table | `resolve_stage_efforts(policy, entry)` |
| `profiles.<name>.match` | the profile's words | the policy table |
| `profiles.<name>.roles`, `.stages` | the same two maps under that profile | the same two calls with `model` set to the profile's first `match` word |
| `harnesses` | the workflow names each listed harness runs, sorted | the resolved path `derive_harness_paths` computes, grouped by workflow |
| `unset` | the level a stage runs at when the call names none: its slot's rendered level | `resolve_effort(policy, slot)` for the slot the `stages` table maps the key to |

A profile's first word resolves to that profile alone, because `load_policy` refuses a word two
profiles hold. So the renderer calls the resolvers as they are and no resolver changes.

`loadRoleIndex` returns `effort: d.effort` or null. Present, it must be a plain object whose four
keys are plain objects; anything else is `broken`, which refuses both tools as a broken index does
today. An index with no `effort` key adds no rule and prints nothing, so an adopter whose roles kit
is older than its hooks kit sees no change, and the existing allow arms keep their empty stderr.

### The model

1. An `Agent` call whose `tool_input.model` is a non-empty string runs on that. The source is
   named `the call`.
2. Else the payload's `transcript_path` is read whole and its lines walked from the end. The first
   line that parses, has `type` `assistant`, is not `isSidechain: true`, and carries a
   `message.model` that is a non-empty string other than `<synthetic>`, gives the model. A line
   that does not parse is skipped. The source is named `the transcript`.
3. No `transcript_path`, a read that throws, or no such entry gives no model. `readSessionModel`
   returns `{ model }` or `{ why }` and never throws.

A `Workflow` call carries no model argument, so step 1 is the `Agent` call's alone.

`resolveModelProfile(profiles, model)` returns the names of every profile whose `match` holds a
word of the id, the words being `String(model).toLowerCase().match(/[a-z0-9]+/g)`. None is the
default tables, one is that profile, and two or more admits the call with the not-checked line
naming every matching profile (§8 F1). The resolver refuses such an id, so no expected level
exists and no `handoff.py` call would print one.

### The Agent verdict

`checkEffortLevel(data, index, root)` returns null when the call was graded and admitted,
`{ deny }` with the refusal text, or `{ note }` with the not-checked line.

- First, where `process.env.CLAUDE_CODE_EFFORT_LEVEL` is a non-empty string, the call is admitted
  with the not-checked line naming the variable (§8 F2). The `Agent` tool then offers no `effort`,
  so no call could pass. This step is the `Agent` call's alone and comes before the model is read.
- seen: the call's own `effort` property when it has one, whatever its type, else
  `default.roles[subagent_type]`.
- expected: `roles[subagent_type]` of the matched profile, else of `default`.
- seen strictly equal to expected admits. Anything else refuses.
- A role the tables do not hold throws, and the catch in `main()` refuses, naming a re-render.

### The Workflow verdict

`resolveHarnessEntry(data, index, root)` is lines `:744-751` of `checkHarnessCall` moved into a
function that returns the matched `harnesses` entry or null. `checkHarnessCall` calls it and keeps
its refusal.

- `CLAUDE_CODE_EFFORT_LEVEL` is not read here: a `Workflow` call is graded whatever it holds.
- The workflows are `harnesses[entry]`. An entry the map does not hold throws.
- `args.efforts` absent reads as `{}`. Present and not a plain object, it refuses, saying so.
- For one workflow, each key of its `stages` map is graded: seen is the call's own `efforts[key]`
  when it has one, else `unset[workflow][key]`; expected is the matched table's
  `stages[workflow][key]`.
- The call is admitted when at least one workflow of the harness has no differing key. Otherwise
  it is refused, naming every differing key of every workflow.
- An `efforts` key no `stages` table holds is not read.

CEILING. For a harness serving two workflows the hook cannot tell which one a call runs. A
spec-review call that passes no `efforts` on an unmatched model is admitted because it is right for
closing review, while its synthesis stage runs at `high` against the policy's `medium`. A harness
serving one workflow has no such gap.

The brief's item 4 says a stage with no value runs at "the stage's default level". This spec reads
that as the level the stage does run at, the `unset` map, on the evidence above. Read as the
default tables' stage level, a Fable call to the review harness with no `efforts` would be admitted
while its synthesis stage ran at `high`.

### The texts

A refusal, one per call, on stderr with exit 2:

```
BLOCKED by agent-cap: rule 8 (TOOL-aGuardedEffort-1) refused this Agent call — gov-builder would run at high (its agent type's level; the call carries no `effort`), and the fable profile gives it medium on the model "claude-fable-5-2" (read from the transcript).
Pass `effort` as `handoff.py role-efforts --model "claude-fable-5-2"` prints it for gov-builder.
```

A `Workflow` refusal has the same first clause, then one line per workflow:
`build: stage builder would run at high (...), expected medium`, and the remedy
`handoff.py stage-efforts <workflow> --model "<id>"`. An unmatched model reads `the default tables
give it`. The model is printed through `JSON.stringify` and cut at 80 characters, because it is
text from a file the hook does not own.

The not-checked line, on stderr, after which rule 7 runs as before:

```
agent-cap: rule 8 did not check this Agent call's effort level — the payload carries no transcript_path
```

The other reasons are `the transcript <path> is unreadable (<code>)`, `the transcript <path>
holds no main-chain assistant entry naming a model`, `the model "<id>" matches the profiles <a> and
<b>, so no one profile's levels are its own`, and `CLAUDE_CODE_EFFORT_LEVEL is set, so this session's
Agent tool carries no effort`.

### The documents

- The hook's header: rule 8's paragraph after rule 6's, and the order sentence at `:11` reads
  rule 6, rule 8, rule 7.
- `tools/hooks/README.md`: one section after "Rule 6", in the header's words.
- `tools/roles/README.md:69-70`: the sentence is replaced by one saying the spawn guard refuses a
  call whose level is not the one this verb prints for the model in use.
- `memory/map/features/agent-cap.md`: one sentence after rule 6's at `:212-214`. The file is
  20545 bytes at this commit against a `DOSSIER_CAP_BYTES` of 20480, so the builder keeps the edit
  to that sentence and reads what the hygiene gate says of the file before and after.
- `help/roles.md`: one sentence at the "Hand one task to one agent" bullet (`:45-46`) and one at
  step 4 (`:28-29`), each holding the words `at another level is refused` and naming the fix.

Each says what rule 8 does not check: a harness's own `agent()` spawns, the two unkeyed stages, the
workflow of a two-workflow harness, a model no transcript names or two profiles match, an `Agent`
call under a set `CLAUDE_CODE_EFFORT_LEVEL`, a configured default subagent model, an effort ceiling in settings, and a hand-edited index.

### The observation

Run from the worktree root after S1 to S9. It calls rule 8 alone, over the tree's own index, so
rules 6 and 7 do not decide. It prints one line per case.

```bash
node -e '
const fs = require("fs"), os = require("os"), path = require("path")
const cap = require("./tools/hooks/agent-cap.js")
const index = require("./tools/hooks/scratch-guard.js").loadRoleIndex(process.cwd())
delete process.env.CLAUDE_CODE_EFFORT_LEVEL
const dir = fs.mkdtempSync(path.join(os.tmpdir(), "ge-"))
const put = (name, rows) => { const p = path.join(dir, name); fs.writeFileSync(p, rows.map((r) => JSON.stringify(r) + "\n").join("")); return p }
const said = (model) => ({ type: "assistant", message: { model } })
const fable = put("fable.jsonl", [said("claude-fable-5-2"), said("<synthetic>")])
const other = put("other.jsonl", [said("claude-opus-5")])
const empty = put("empty.jsonl", [{ type: "user", message: { content: "hi" } }])
const agent = (tp, ti) => ({ tool_name: "Agent", cwd: process.cwd(), transcript_path: tp, tool_input: Object.assign({ subagent_type: "gov-builder" }, ti) })
const unit = (tp, efforts) => ({ tool_name: "Workflow", cwd: process.cwd(), transcript_path: tp, tool_input: { scriptPath: "tools/workflows/unattended-unit.js", args: Object.assign({ roles: { builder: "gov-builder" } }, efforts ? { efforts } : {}) } })
const cases = {
  "a-none": agent(fable, {}), "a-high": agent(fable, { effort: "high" }), "a-medium": agent(fable, { effort: "medium" }),
  "o-none": agent(other, {}), "o-medium": agent(other, { effort: "medium" }),
  "w-none": unit(fable), "w-high": unit(fable, { builder: "high" }), "w-medium": unit(fable, { builder: "medium" }),
  "m-fable": agent(other, { model: "fable" }), "m-fable-medium": agent(other, { model: "fable", effort: "medium" }), "m-opus": agent(fable, { model: "opus" }),
  "n-path": agent(undefined, {}), "n-unreadable": agent(path.join(dir, "absent.jsonl"), {}), "n-empty": agent(empty, {}),
}
const say = (name, v) => console.log(name + " -> " + (v === null ? "admit" : v.deny ? "deny: " + v.deny.split("\n")[0] : "note: " + v.note))
for (const [name, data] of Object.entries(cases)) say(name, cap.checkEffortLevel(data, index, process.cwd()))
say("x-no-key", cap.checkEffortLevel(cases["a-none"], Object.assign({}, index, { effort: null }), process.cwd()))
const two = Object.assign({}, index.effort.profiles, { second: Object.assign({}, index.effort.profiles.fable, { match: ["claude"] }) })
say("f1-two", cap.checkEffortLevel(cases["a-none"], Object.assign({}, index, { effort: Object.assign({}, index.effort, { profiles: two }) }), process.cwd()))
process.env.CLAUDE_CODE_EFFORT_LEVEL = "high"
say("f2-agent", cap.checkEffortLevel(cases["a-none"], index, process.cwd()))
say("f2-workflow", cap.checkEffortLevel(cases["w-none"], index, process.cwd()))
'
```

The levels it reads are the policy's own, PINNED 2026-11-10: `gov-builder` is `high` in the
default tables and `medium` under `fable` (`tools/roles/house/policy.toml:14`, `:27-29`). The
suite arms use their own fixtures, so a policy edit moves these lines and no arm.

### The parity probe

```bash
IDS="claude-fable-5-2 fable FABLE-5 affable-1 fable5 claude-opus-5 us.vendor/claude-fable-5-2:0 ---"
python -c '
import sys; sys.path.insert(0, "tools/roles"); import roles_lib as l
p = l.load_policy("tools/roles", l.load_roles("tools/roles"), l.load_workflows("tools/roles"))
for m in sys.argv[1:]:
    try: print(m, l.resolve_profile(p, m) or "-")
    except l.RolesError: print(m, "!")' $IDS > "$TMPDIR/ge.py.txt"
node -e '
const cap = require("./tools/hooks/agent-cap.js")
const e = require("./tools/hooks/scratch-guard.js").loadRoleIndex(process.cwd()).effort
for (const m of process.argv.slice(1)) { const n = cap.resolveModelProfile(e.profiles, m); console.log(m, n.length > 1 ? "!" : n[0] || "-") }' $IDS > "$TMPDIR/ge.js.txt"
diff <(tr -d '\r' < "$TMPDIR/ge.py.txt") <(tr -d '\r' < "$TMPDIR/ge.js.txt"); grep affable "$TMPDIR/ge.js.txt"
```

The tree's policy holds one profile, so this probe never prints `!`. The arm of §7 runs the same
comparison over a fixture with two profiles, where one id matches both, and adds the empty id.

### Inventory

| Identifier | Home | Kind |
|---|---|---|
| `readSessionModel` | `tools/hooks/agent-cap.js` | function, the `read` verb |
| `resolveModelProfile` | the same, exported | function, the `resolve` verb |
| `resolveHarnessEntry` | the same | function, the `resolve` verb |
| `checkEffortLevel` | the same, exported | function, the `check` verb |
| `renderEffortDeny` | the same | function, the `render` verb |
| `derive_effort_index` | `tools/roles/render_agents.py` | function, the `derive` verb |
| `effort` and its four keys | `.claude/roles.json` | index keys |
| rule 8 | the hook's header and refusals | a rule number |

`lexicon naming predicates` grades the six function names.

### Rollout

1. S1 and S2 first, with the re-render: the contract lands before its reader.
2. S3 to S9, then the observation and the parity probe.
3. The arms of S10, then the documents of S11, then `python tools/codebase-map/gen_map.py --write`.
4. The guard takes effect at the next tool call of any session, since a hook is a fresh process.
   A session on Fable that passes no level is refused from then on, which is the point.

### Files touched (estimate)

`tools/hooks/agent-cap.js` · `tools/hooks/agent-cap.test.sh` · `tools/hooks/scratch-guard.js` ·
`tools/hooks/README.md` · `tools/roles/render_agents.py` · `tools/roles/adopt-roles.test.sh` ·
`tools/roles/README.md` · `.claude/roles.json` · `memory/map/features/agent-cap.md` ·
`memory/map/generated/symbols.json` · `memory/map/generated/MAP.md` · `help/roles.md`

### Alternatives rejected

- **The hook spawns `handoff.py`.** A Python launcher per spawn, on a node where resolving one
  means running candidates, inside a hook whose timeout admits. The brief rules it out.
- **The hook reads `policy.toml`.** A TOML reader in a hook and a second resolver.
- **`scanTurnRecords` of `format-guard.js` for the model.** It returns the final turn only, and a
  turn's first tool call can precede any assistant entry of that turn. The read idiom and the
  sidechain rule are reused; the turn bound is not.
- **The index carries the stage-to-slot map and the hook resolves levels.** It moves
  `resolve_stage_efforts`'s fallback into JavaScript, which is the second resolver again.
- **Admit a stage when any workflow's level matches, key by key.** It admits a mix no single
  workflow gives. Whole-workflow agreement costs the same lookup.

## 5. Production-readiness checklist

- security: the rule only refuses or admits, and grants nothing. It reads one path the harness
  names, as `format-guard.js` does, and prints a model string capped and quoted. A throw refuses;
  an unreadable model admits, by the owner's ruling in the build README. It stops forgetting, not
  evasion: a hand-edited index or a forged transcript passes.
- perf / scale: one whole-file read and a walk from the end, per `Agent` or `Workflow` call. The
  walk stops at the first assistant entry. A tail read is the upgrade if a call is measured slow.
- error / empty / loading states: no key in the index adds no rule; a wrong-shaped key is a broken
  index; no model is the not-checked line; a role or harness the tables lack throws and refuses.
- observability: the refusal and the not-checked line, both on stderr. The `agent` line still
  prints the effort and model each agent ran at.
- risks: the transcript's shape is Claude Code's and unversioned, so a renamed field reads as no
  model and the rule goes quiet with its line. Whether the hook's process inherits
  `CLAUDE_CODE_EFFORT_LEVEL` is UNVERIFIED: where it does not, such a session's mismatched direct
  spawns are refused with no call that passes, until the variable is unset. A session that switched model mid-turn is graded on
  the last entry written. A configured default subagent model, and a settings ceiling on effort,
  change what an agent runs at and are invisible here.
- testing: the arms of §7. The staged break for each is on its line.
- migration: additive. An old index with a new hook adds no rule; a new index with an old hook is
  read as before, since the old reader takes named keys only. An adopter's
  `adopt-roles.sh --check` reds on the stale index and prints the `--write` remedy
  (`tools/roles/render_agents.py:296`).
- user docs: `help/roles.md`, S11.

## 6. Acceptance criteria

"The observation" and "the parity probe" are the blocks of §4.

- **AC1** — When the observation runs, its `a-none` and `a-high` lines read `deny:` and each names
  `gov-builder`, `medium`, `claude-fable-5-2` and `role-efforts --model`, and `a-medium` reads
  `admit`.
  Red when: the level is not compared, the `<synthetic>` entry written last is taken as the model,
  or a call with no `effort` is read as carrying none to grade.
  figure: `high` and `medium` are PINNED from the policy file, 2026-11-10.
- **AC2** — When the observation runs, `o-none` reads `admit` and `o-medium` reads `deny:` naming
  `high`.
  Red when: an unmatched model is not graded against the default tables.
- **AC3** — When the observation runs, `w-none` and `w-high` read `deny:` naming `builder`,
  `medium` and `stage-efforts build --model`, and `w-medium` reads `admit`.
  Red when: a harness call's `efforts` is not read, or a stage with no value is taken to run at
  the profile's level.
- **AC4** — When the observation runs, `m-fable` reads `deny:` naming `medium` and `the call`,
  `m-fable-medium` reads `admit`, and `m-opus` reads `admit`.
  Red when: the call's own `model` does not win over the transcript's.
- **AC5** — When the observation runs, `n-path`, `n-unreadable` and `n-empty` each read `note:`
  with its own reason, and `x-no-key` reads `admit`.
  Red when: an unreadable model refuses or throws, two reasons share one text, or an index with no
  `effort` key is graded.
- **AC6** — When the parity probe runs, its `diff` prints nothing and its last line reads
  `affable-1 -`.
  Red when: the hook matches a substring, folds case another way, or splits words on another set.
- **AC7** — When `python tools/roles/render_agents.py --check` runs after the re-render it exits
  0. The index's `effort.default.roles` equals the JSON `python tools/roles/handoff.py role-efforts`
  prints, `effort.profiles.fable.roles` equals that verb's output with `--model fable`, and
  `effort.default.stages.build` equals `python tools/roles/handoff.py stage-efforts build`. With
  `effort.profiles.fable.roles.gov-builder` then hand-set to `high` in `.claude/roles.json`, the
  same `--check` exits 1 and prints `drift .claude/roles.json`; `--write` restores it.
  Red when: the render writes no `effort` key, or writes levels the verbs do not print.
- **AC8** — When `loadRoleIndex` is called through `node -e` on a scratch directory whose
  `.claude/roles.json` is the tree's index with `effort` set to `[]`, its `state` is `broken`; on
  the tree's own index its `effort.profiles.fable.match` is `["fable"]`.
  Red when: the reader drops the key, or passes a wrong-shaped one to the rule.
- **AC9** — When the `w-none` payload of the observation, with a transcript file naming
  `claude-fable-5-2`, is piped to `node tools/hooks/agent-cap.js`, the exit is 2 and stderr opens
  `BLOCKED by agent-cap: rule 8`. The same payload without `transcript_path` prints a stderr line
  holding `rule 8 did not check`.
  Red when: `main()` never calls the rule, or calls it before rule 6 decided.
  fixture: the second half's exit code is rule 7's, which reads this checkout's settings.
- **AC10** — When `grep -c "The spawn guard reads no" tools/roles/README.md` runs it prints `0`,
  and `grep -c "rule 8" tools/hooks/agent-cap.js tools/hooks/README.md` and
  `grep -c "TOOL-aGuardedEffort-1" memory/map/features/agent-cap.md` and
  `grep -c "at another level is refused" help/roles.md` each print one or more per file.
  Red when: a document still says the guard reads no `effort`, or never names the rule. It reads
  tokens, never whether the account is right.
  figure: the `help/roles.md` count is `0` at `4dca62ad`, PINNED 2026-11-10.
- **AC11** — When the observation runs, `f1-two` reads `note:` naming `fable` and `second`,
  `f2-agent` reads `note:` naming `CLAUDE_CODE_EFFORT_LEVEL`, and `f2-workflow` reads `deny:`.
  Red when: a two-profile id is refused or graded against the first profile, the variable is not
  read on an `Agent` call, or it also silences a `Workflow` call.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `hook destinations (every declared hook path ships)` · `hook destinations self-test` · `agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `check-wiring self-test` · `verifier fan-out self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `policy fixtures` · `codebase-map coverage + freshness` · `docs` · `kit/dogfood doc parity` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/agent-cap.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC9 AC11 · a section after rule 6's, over a hand-written index carrying an `effort` key and transcripts it writes, each payload a valid rule 6 call run through the hook copy, the two-profile id and the set `CLAUDE_CODE_EFFORT_LEVEL` on both tools among them, every other arm run with that variable unset; staged by removing the rule 8 call from `main()` in the copy, which turns every refusal to exit 0 and drops every not-checked line · none
New arm: tools/hooks/agent-cap.test.sh · covers AC8 · an index whose `effort` is a list refuses both tools as broken; staged by `loadRoleIndex` returning the key unread · none
New arm: tools/roles/adopt-roles.test.sh · covers AC6 · arm 20, one list of model ids, the empty id, `affable-1` and the two-profile `vendor-tfam-9` among them, read by `resolve_profile` over arm 19's fixture policy and by `resolveModelProfile` over the index rendered from it; SKIPs without node or a hooks kit; staged by a substring match in the hook · none, it stays out of `FLOOR_ASSERTIONS` as arms 6 and 11 do
New arm: tools/roles/adopt-roles.test.sh · covers AC7 · arm 21, a profile level edited in the fixture policy with no re-render makes the adopter's check exit 1 naming the index; staged by a render that writes no `effort` key · `FLOOR_ASSERTIONS` rises by this arm's count
New arm: tools/roles/adopt-roles.test.sh · covers AC1 · arm 6 moved: its admitted spawn's stderr is exactly the not-checked line, and one added payload with a Fable transcript and no `effort` is refused over the rendered index, so the hook is held to the renderer's shape and not only to a hand-written one; staged by the same removal as the first arm · none

What no leg checks: that the transcript format still holds, which workflow a two-workflow harness
call runs, and that a session's `Agent` tool offers `effort` at all.

## 8. Open questions

- **F1 — A model id that two profiles match.** `resolve_profile` raises for it, so
  `handoff.py role-efforts --model` exits 1 and no expected level exists.
  - (a) Admit, with the not-checked line naming both profiles. The policy defect is already loud
    at dispatch, and a refusal could name no level and no working remedy.
  - (b) Refuse, naming both `match` keys. Stricter, and it stops every spawn until the policy file
    is fixed.
  - Recommendation: (a). Item 5 of the brief requires a refusal to name the expected level.
  - RESOLVED (owner, 2026-11-10): (a), admit with the not-checked line naming both profiles.
- **F2 — A session whose `Agent` tool offers no `effort`.** `TOOL-aProfiledEffort-3` §4 pins that
  the schema omits the parameter when `CLAUDE_CODE_EFFORT_LEVEL` is set. On Fable every direct
  spawn of a role whose default level is not the profile's would then be refused with no call that
  passes. Whether the hook's process inherits that variable is UNVERIFIED.
  - (a) Where the hook's environment holds a non-empty `CLAUDE_CODE_EFFORT_LEVEL`, an `Agent` call
    is admitted with the not-checked line naming the variable. `Workflow` calls are graded as
    usual.
  - (b) Refuse as written, and name the variable in the refusal as the thing to unset.
  - (c) Do not read the variable. The refusal stands and says nothing of it.
  - Recommendation: (a), since the level is then the environment's and the call cannot carry one.
  - RESOLVED (owner, 2026-11-10): (a), an `Agent` call is admitted with the not-checked line naming
    the variable, and `Workflow` calls are graded as usual.

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft, from the brief and the code read at `4dca62ad`. The owner
  resolved F1 and F2 on 2026-11-10, before the first commit, and both are folded in as S12, AC11
  and the first arm of §7.

## 10. Reuse audit

The seam is rule 6 of `tools/hooks/agent-cap.js`: `checkHandoffSpawn` and `checkHarnessCall` admit
the calls rule 8 grades, `extractWorkflowArgs` reads `args`, and the harness match is extracted
and shared. The index is extended through its one writer, `render_roles_index` in
`tools/roles/render_agents.py`, and its one reader, `loadRoleIndex` in
`tools/hooks/scratch-guard.js`. Levels come from `resolve_effort` and `resolve_stage_efforts`
unchanged. The transcript read follows `format-guard.js` and the `<synthetic>` skip follows
`handoff.py`. `python tools/codebase-map/reuse_lookup.py "a PreToolUse hook reads the session model
from the transcript and compares a spawn's reasoning effort with the level the effort policy
profile gives"` ranked `load_policy` of `tools/roles/roles_lib.py` and generic readers, and no
transcript-model reader in JavaScript, so `readSessionModel` is new: no existing seam fits that one
function, for the reason "Alternatives rejected" gives for `scanTurnRecords`.

Recall returned ask `TOOL-aProfiledEffort-6`, which this unit closes, `TOOL-aProfiledEffort-5`,
which stays open, and `TOOL-dBoundRoles-21`, DEFERRED, which later re-points the policy's readers.
The checklist `python tools/memory-tree/gotchas.py --for-paths` printed shaped the arms: each
refusal arm runs a call that reaches the rule, the rendered index is exercised beside the
hand-written one, and the levels live in the policy alone.

Recall terms used: spawn guard agent-cap rule 6 effort profile role index roles.json transcript model stage-efforts role-efforts resolve_profile
