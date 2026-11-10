# TOOL-aGuardedEffort-2 — rule 8 grades an unset stage at the level of the role the call names, and the closing review's arms land

**Status:** INPROGRESS · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aGuardedEffort-1-agent-ledger.md](../build/2026-11-10-build-TOOL-aGuardedEffort-1-agent-ledger.md) | journal | TOOL-aGuardedEffort-1 |
| [2026-11-10-build-TOOL-aGuardedEffort-2-1-acceptance-ledger.md](../build/2026-11-10-build-TOOL-aGuardedEffort-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-10-prompt-TOOL-aGuardedEffort-2-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aGuardedEffort-2-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aGuardedEffort-2-bar-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-aGuardedEffort-2-bar-fix-brief.md) | research | — |
| [2026-11-10-prompt-TOOL-aGuardedEffort-2-round1-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-aGuardedEffort-2-round1-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Rule 8 of `tools/hooks/agent-cap.js` grades a `Workflow` stage that carries no `efforts` value at
the level of the role the call's own `args.roles` names for it, and no longer at the level of the
slot the policy maps the stage to. The same pass closes the other eight items the closing review
confirmed at round 1: a stage-key population the tables must agree on, and the arms the rule's
suites lack. The review record is
`memory/builds/aGuardedEffort/reviews/2026-11-10-review-TOOL-aGuardedEffort-1-diff-review-round1.md`
and the brief is
`memory/builds/aGuardedEffort/prompts/2026-11-10-prompt-TOOL-aGuardedEffort-2-round1-fix-brief.md`.

## 2. Scope (IN)

Each item names the review item it closes.

- **S1** — Item 1. In the `Workflow` loop of `checkEffortLevel`, a stage key with no `efforts`
  value takes its seen level from `effort.default.roles` at the role `args.roles` names for that
  key. A key that neither `efforts` nor `roles` names counts as differing for that workflow, and
  the call is still admitted when one whole workflow has no differing key. Per §4 "The Workflow
  verdict". Observed by AC1 and AC2.
- **S2** — Item 3, the hook half. The stage keys of a workflow are the keys of `effort.unset` for
  it joined with the keys of the matched table's `stages` for it, and a key one side holds and the
  other lacks throws. A workflow with no stage key never admits a call while a sibling workflow of
  the same harness has one. A harness none of whose workflows has a stage key is admitted with the
  not-checked line. Observed by AC3.
- **S3** — Item 3, the renderer half. `derive_effort_index` in `tools/roles/render_agents.py`
  writes an explicit empty entry in every `stages` map and in `unset` for a `workflow`-driver
  workflow that has no `stages` table, and keeps that workflow in `harnesses`. The bytes of
  `.claude/roles.json` do not move, since every driven workflow of this tree has a `stages` table.
  Observed by AC4.
- **S4** — The refusal lines and the new not-checked reason read as §4 "The texts" gives them.
  Observed by AC1, AC2 and AC3.
- **S5** — Items 1, 2, 3, 4, 5, 7 and 9: the arms and the fixture moves of §4 "The arms" land in
  the hook's suite. NOT OBSERVED by a criterion: an arm is a declaration under §7, and the main
  loop sees each red and then green at the close. AC5 observes the one half of item 7 a payload on
  this tree can show.
- **S6** — Item 6: arm 6 of the roles adopter suite sends `Workflow` payloads through the hook
  over a rendered index and compares the rendered tables with the verbs and the agent files, per
  §4 "The arms". NOT OBSERVED by a criterion, for the reason S5 gives.
- **S7** — One arm of `render_agents.py --selftest` holds S3. NOT OBSERVED by a criterion, for the
  reason S5 gives; AC4 observes S3 itself.
- **S8** — Item 8: the six sites that say the hook runs rules 6 and 7 say rules 6, 8 and 7, per
  §4 "The six sites". Observed by AC6.
- **S9** — The hook's header, the "Rule 8" section of `tools/hooks/README.md` and step 4 of
  `help/roles.md` say what S1 and S2 changed, per §4 "The documents". Observed by AC7.

## 3. Non-goals (OUT)

- The agents a running harness spawns through its own `agent()`. No hook sees them.
- The `committer` and `probe` stages, which no `stages` table keys. That is ask
  `TOOL-aProfiledEffort-5`.
- Any change to a level, a profile, `resolve_profile`, `resolve_effort`, `resolve_stage_efforts`
  or `handoff.py`.
- A second matching rule, a refusal when the model cannot be read, and a model read from anywhere
  but the call and the transcript.
- The `Agent` verdict, `readSessionModel`, `resolveModelProfile` and `loadRoleIndex`. Items 5 and
  9 add arms over them and move no line of them.
- The left-shift paragraphs of the review record: the checklist entries and the wider
  `agent-cap restatement` leg. Each is a separate document or gate, so a separate unit.
- The `unset` values in the index. The hook stops reading them as levels and keeps reading the
  map's keys; §4 "Alternatives rejected" says why the key stays.
- Which workflow a call to a harness serving two workflows runs. A call whose `roles` names every
  key of both, as `handoff.py harness-args` prints them, is still admitted when it is right for
  one. AC2's `r-union` line pins that ceiling.
- Any edit to the text of `TOOL-aGuardedEffort-1`, which is CLOSED and stays as it landed. Item
  7's criterion is AC5 of this spec.
- `memory/map/features/agent-cap.md`. Its rule 8 sentence stays true, and the file is at its byte
  cap.
- A by-hand move of any kit version. The lander's mint moves them.

### Edges

- **consumes-from** external — the first unit of this build, CLOSED and so declaring no edge back:
  rule 8, the index's `effort` key and the two suites' rule 8 sections, at `27e6aead`. Without them
  there is nothing to repair.
- **hands-off** external — the checklist entries and the restatement leg the review's left-shift
  paragraphs name, and the version moves of the hooks and roles kits.

## 4. Design

### Evidence

Read at `df29bfe3` on 2026-11-10, node a.

- The `Workflow` loop reads an unset stage's level from `e.unset[w][key]` and never reads
  `a.roles` (`tools/hooks/agent-cap.js:889-901`). Rule 6 asks only that each `args.roles` value be
  an `agent`-true role, under any key (`:766-774`).
- A harness types a stage from `roles[key]` and falls back to an untyped spawn, and passes a level
  only where `efforts[key]` is set (`tools/workflows/tier2-review.js:540-542`, `:565-567`;
  `tools/workflows/unattended-build.js:581`).
- `const stages = (table.stages && table.stages[w]) || {}` yields no key for a missing entry, and
  `if (!differing.length) return null` then admits (`tools/hooks/agent-cap.js:890`, `:899`).
- `derive_effort_index` builds `harnesses` from every `workflow`-driver workflow and `stages` and
  `unset` from those with a `stages` table (`tools/roles/render_agents.py:219-236`).
  `resolve_stage_efforts` answers `{}` for a workflow with none (`tools/roles/roles_lib.py:655-662`).
- `handoff.py harness-args` prints the union of the `stages` tables of every workflow a harness
  runs (`tools/roles/handoff.py:468-485`), so a call built from it names every key of both review
  workflows.
- The hook suite's one rule 8 index maps one harness to one workflow with one stage, `high` in
  both `default.stages` and `unset` (`tools/hooks/agent-cap.test.sh:748`). Its `e8.tfam.jsonl`
  holds one main-chain model, on line 1 (`:751-753`). Its `effort` shape arms plant a list alone
  (`:819-821`).
- Arm 6 of the roles adopter suite sends `Agent` payloads only
  (`tools/roles/adopt-roles.test.sh:187-239`), and the suite's floor is a minimum (`:900`).
- `main()` runs rule 6, then rule 8, then rule 7 (`tools/hooks/agent-cap.js:1001-1060`).
- PINNED, run 2026-11-10 at `df29bfe3`: "The observation" below prints `admit` for every line but
  `r-swap-fable`, which reads `deny:` naming `high`. "The renderer probe" prints
  `['build', 'nostage'] [None, None, None]`.

### The Workflow verdict

The steps before the loop do not move: the harness entry, the `efforts` shape test, the model and
the matched table. For each workflow `w` of the harness:

1. `keys` is the keys of `e.unset[w]` joined with the keys of `table.stages[w]`, a missing entry
   reading as no keys. A key one side holds and the other lacks throws, naming `w` and the key,
   and the catch in `main()` refuses with the re-render remedy.
2. No key: `w` is unkeyed. It adds no line and never admits.
3. For each key, sorted, the seen level is `efforts[key]` when the call's `efforts` has the key.
   Else, when `a.roles` has the key, it is `e.default.roles[a.roles[key]]`, and a role that map
   lacks throws. Else the key is differing, with no level: the stage would spawn untyped at the
   session's level, which no table holds.
4. A seen level not strictly equal to `table.stages[w][key]` is differing.
5. A keyed workflow with no differing key admits the call, `return null`, as today.

After the loop, when no workflow of the harness was keyed, the call is admitted with the
not-checked line. Otherwise it is refused, with one line per keyed workflow, and the remedy names
`stage-efforts` for the keyed workflows only.

The `unset` values are no longer read. A call that names the policy's role for a stage is graded
exactly as before, because the renderer derives both values from one `resolve_effort` call.

### The texts

A differing stage reads one of three ways. The first is unmoved, the second gains the role, and
the third is new.

```
stage builder would run at high (the call's own `efforts.builder`), expected medium
stage builder would run at medium (gov-skeptic, its agent type's level; the call's `efforts` names no builder), expected high
stage diffFinder would run untyped at the session's level (the call's `roles` and `efforts` name no diffFinder), expected medium
```

The new not-checked reason, after `agent-cap: rule 8 did not check this Workflow call's effort
level — `:

```
the effort tables of <index> hold no stage key for <workflow>[ and <workflow>], which the harness <entry> runs
```

The throw of step 1 reads `the effort tables of <index> disagree on stage <key> of <workflow>`.

### The observation

Run from the worktree root after S1 to S4, with `EFFORT_PROBE_DIR` naming an existing scratch
directory the caller owns. It calls rule 8 alone over the tree's own index, as the first unit's
observation does, and prints one line per case.

```bash
node -e '
const fs = require("fs"), path = require("path")
const cap = require("./tools/hooks/agent-cap.js")
const index = require("./tools/hooks/scratch-guard.js").loadRoleIndex(process.cwd())
delete process.env.CLAUDE_CODE_EFFORT_LEVEL
const dir = process.env.EFFORT_PROBE_DIR
if (!dir) throw new Error("set EFFORT_PROBE_DIR to an existing scratch directory")
const put = (name, model) => { const p = path.join(dir, name); fs.writeFileSync(p, JSON.stringify({ type: "assistant", message: { model } }) + "\n"); return p }
const fable = put("fable.jsonl", "claude-fable-5-2"), other = put("other.jsonl", "claude-opus-5")
const call = (h, tp, roles, efforts) => ({ tool_name: "Workflow", cwd: process.cwd(), transcript_path: tp, tool_input: { scriptPath: "tools/workflows/" + h, args: Object.assign({ roles }, efforts ? { efforts } : {}) } })
const spec = { specFinder: "gov-spec-reviewer", skeptic: "gov-skeptic", synthesis: "gov-synthesizer" }
const cases = {
  "r-swap": call("unattended-unit.js", other, { builder: "gov-skeptic" }),
  "r-swap-high": call("unattended-unit.js", other, { builder: "gov-skeptic" }, { builder: "high" }),
  "r-swap-fable": call("unattended-unit.js", fable, { builder: "gov-researcher" }),
  "r-omit": call("tier2-review.js", other, { skeptic: "gov-skeptic" }),
  "r-omit-spec": call("tier2-review.js", other, spec),
  "r-omit-spec-efforts": call("tier2-review.js", other, spec, { specFinder: "medium", skeptic: "medium", synthesis: "medium" }),
  "r-union": call("tier2-review.js", other, Object.assign({ diffFinder: "gov-diff-reviewer" }, spec)),
  "r-remap": call("tier2-review.js", fable, { diffFinder: "gov-builder", skeptic: "gov-builder", synthesis: "gov-synthesizer" }, { synthesis: "medium" }),
}
const say = (name, f) => { let v; try { v = f() } catch (e) { return console.log(name + " -> throw: " + e.message) }
  console.log(name + " -> " + (v === null ? "admit" : v.deny ? "deny: " + v.deny.trim().split(/\r?\n/).join(" | ") : "note: " + v.note)) }
for (const [name, data] of Object.entries(cases)) say(name, () => cap.checkEffortLevel(data, index, process.cwd()))
const edit = (f) => { const e = JSON.parse(JSON.stringify(index.effort)); f(e); return Object.assign({}, index, { effort: e }) }
const unit = "tools/workflows/unattended-unit.js", review = "tools/workflows/tier2-review.js"
say("s-entry", () => cap.checkEffortLevel(call("unattended-unit.js", fable, { builder: "gov-builder" }, { builder: "medium" }), edit((e) => { delete e.profiles.fable.stages.build }), process.cwd()))
say("s-key", () => cap.checkEffortLevel(call("unattended-unit.js", other, { builder: "gov-builder" }, { builder: "high" }), edit((e) => { delete e.unset.build.builder }), process.cwd()))
say("s-sibling", () => cap.checkEffortLevel(cases["r-omit"], edit((e) => { e.harnesses[review].push("nostage") }), process.cwd()))
say("s-alone", () => cap.checkEffortLevel(cases["r-swap"], edit((e) => { e.harnesses[unit] = ["nostage"] }), process.cwd()))
'
```

The levels are the policy's own, PINNED 2026-11-10 from `.claude/roles.json`: `gov-skeptic` and
`gov-researcher` render at `medium`, `gov-builder` and `gov-synthesizer` at `high`, the default
`build.builder` stage is `high`, and the default `spec-review.synthesis` stage is `medium`.

### The renderer probe

```bash
python -c '
import sys, json; sys.path.insert(0, "tools/roles")
import roles_lib as l, render_agents as r
roles = l.load_roles("tools/roles"); wfs = l.load_workflows("tools/roles")
p = l.load_policy("tools/roles", roles, wfs)
unit = next(w for w in wfs if w["name"] == "build")
bare = {k: v for k, v in unit.items() if k != "stages"}
e = r.derive_effort_index(p, roles, wfs + [dict(bare, name="nostage")], "tools", ".")
print(e["harnesses"]["tools/workflows/unattended-unit.js"], [t.get("nostage") for t in (e["default"]["stages"], e["profiles"]["fable"]["stages"], e["unset"])])
print(json.load(open(".claude/roles.json"))["effort"] == r.derive_effort_index(p, roles, wfs, "tools", "."))
'
```

### The arms

The hook suite's rule 8 section keeps every arm it has, at its verdict. Its index gains what the
arms below need, and the builder says in the section's comment which existing payload grew. The
constraints are the fixture's, not a layout: one declared harness serving one workflow, one
serving two workflows that share their stage keys at different levels, one role whose
`default.roles` level is not the default stage level of the stage the index maps it to, and one
role at another level than `gov-builder`.

| Item | Arm, on a call rule 6 admits unless said | Verdict |
|---|---|---|
| 1 | unmatched model, one-workflow harness, the stage's role swapped for one at another level, no `efforts` | exit 2, naming that role and its level |
| 1 | the same call on the two-workflow harness | exit 2 |
| 1 | profiled model, the stage's role swapped for one at the profile's level, no `efforts` | exit 0 |
| 1 | `roles` under a key no stage has, no `efforts`, on each harness | exit 2, `name no <key>` |
| 1 | the same omission with the key's right level in `efforts` | exit 0 |
| 2 | unmatched model, the policy's own roles, no `efforts`, a stage whose role level is not its default stage level | exit 2, `its agent type's level` and both levels |
| 2 | the same call with that stage's default stage level in `efforts` | exit 0 |
| 3 | an index whose matched table lacks one workflow's `stages` entry | exit 2, `render_agents.py --write` |
| 3 | an index whose `unset` lacks one stage key | exit 2, `render_agents.py --write` |
| 3 | a harness with a keyed and an unkeyed workflow, levels wrong for the keyed one | exit 2 |
| 3 | a harness whose only workflow is unkeyed | exit 0, `hold no stage key` |
| 4 | two-workflow harness, `efforts` right for the second workflow only | exit 0 |
| 4 | `efforts` right for neither | exit 2, a line per workflow and ` or ` in the remedy |
| 4 | `efforts` taking one key's level from each workflow | exit 2 |
| 7 | the rule 8 index and the profiled transcript, a `general-purpose` spawn with no `effort` | exit 2, opens `BLOCKED by agent-cap: rule 6`, holds `is not an agent-true role`, no `rule 8` |
| 7 | a hook copy beside a policy kit, settings above the landed limit, a harness call whose level differs | exit 2, holds `rule 8 (TOOL-aGuardedEffort-1) refused`, no `rule 7` |
| 9 | an `effort` holding three of its four keys, and one whose `default` is a list | each exit 2, `effort is not` |

Item 5 adds no arm. `e8.tfam.jsonl` gains a first line, a main-chain assistant entry naming
`maker-other-9`, and a `user` record carrying `message.model` `maker-other-9` after the `tfam`
entry. The AC1 arms of the first unit then fail under a forward walk or a missing `type` test.

The second item 7 arm builds on the suite's armed rule 7 section, which already puts a policy kit
beside a hook copy in a real repository (`tools/hooks/agent-cap.test.sh:415-427`). It writes its
own role index there after that section's arms, so their verdicts hold.

Arm 6 of the roles adopter suite gains two groups, on its existing SKIP path.

- Three `Workflow` payloads for the fixture's unit harness, as the rendered index spells it, with
  `roles` from `handoff.py harness-args`. With `efforts` from `stage-efforts build --model
  vendor-tfam-9` on the `tfam` transcript: exit 0. With none there: exit 2 naming the stage. With
  the default verb's `efforts` on an unmatched model's transcript: exit 0.
- For every workflow with a `stages` table, read from the fixture kit's `workflows.toml` by the
  suite's own `tomllib` read: `effort.default.stages` equals what `stage-efforts` prints,
  `effort.profiles.tfam.stages` equals that verb with `--model vendor-tfam-9`, and for each stage
  key both `effort.unset` and `effort.default.roles` at its slot equal the `effort:` line of that
  slot's rendered agent file.

The render selftest gains one arm: a fixture catalogue holding a `workflow`-driver workflow with
no `stages` table renders an index whose `effort` holds that workflow in `harnesses` and as `{}`
in `default.stages` and in `unset`.

### The six sites

Each reads `rules 6, 8 and 7` where it read the old pair: `tools/hooks/agent-cap.js:75`, `:988`
and `:1114`, `tools/hooks/README.md:237`, `tools/workflows/README.md:164` and
`tools/hooks/agent-cap.test.sh:269`. Line `:988` is the printed `--only=` refusal, and no arm pins
its wording.

### The documents

- The hook's header, rule 8's paragraph (`tools/hooks/agent-cap.js:39-58`): the stage level is the
  `args.efforts` value, or with none the level of the agent type the call's `roles` names for the
  stage, and a stage neither names counts as differing. The not-checked list gains a harness whose
  workflows hold no stage key. The comment at `:886-887` and the function's head comment follow.
- `tools/hooks/README.md:312-320`: the same two sentences, in the header's words.
- `help/roles.md:28-31`: one sentence saying a stage that neither `roles` nor `efforts` names is
  refused too.

The header and the README each carry the words `neither names counts as differing`, and the help
page the words `is refused too`.

### Rollout

1. S3 and its selftest arm, then "The renderer probe" and `render_agents.py --check`.
2. S1, S2 and S4, then "The observation".
3. The arms of S5 and S6, then S8 and S9, then `python tools/codebase-map/gen_map.py --write`.
4. A session's next tool call runs the new hook, since a hook is a fresh process. A call built
   from `harness-args` and `stage-efforts`, as the build skill instructs, names every key and
   passes as before.

### Files touched (estimate)

`tools/hooks/agent-cap.js` · `tools/hooks/agent-cap.test.sh` · `tools/hooks/README.md` ·
`tools/workflows/README.md` · `tools/roles/render_agents.py` · `tools/roles/adopt-roles.test.sh` ·
`help/roles.md` · `memory/map/generated/symbols.json` · `memory/map/generated/MAP.md`

### Alternatives rejected

- **Refuse at once when `roles` omits a stage key.** It refuses every call to the review harness:
  a spec-review call carries no `diffFinder` and a closing-review call no `specFinder`. The review
  record's item 1 rejects it for that reason.
- **Take `unset` out of the index.** Item 3's population test needs a second map to compare the
  matched table's keys with, and `default.stages` is that table itself on an unmatched model. The
  loader's four-key rule and item 9's arm also name it.
- **Throw only when `unset` has an entry and the table has none.** It skips a table entry that
  lacks one key, and a stageless sibling still admits. The review record's item 3 rejects it.
- **Build `harnesses` from the staged workflows alone.** A harness with only stageless workflows
  would then throw at the harness lookup and be refused on every call.
- **Say `this hook's call rules` at the six sites.** The brief asks that the sites name rule 8.

## 5. Production-readiness checklist

- security: the change narrows what the rule admits and grants nothing. It reads two more values
  of the call, both already shape-checked by rule 6. A role name reaches stderr only after rule 6
  matched it against the index. It still stops forgetting, not evasion.
- perf / scale: N/A — a few more object lookups per `Workflow` call.
- error / empty / loading states: tables that disagree on a stage key throw and refuse with the
  re-render remedy; a harness with no stage key is the not-checked line; a role the level map
  lacks throws.
- observability: the refusal now names the role a stage would run as, and the new reason prints on
  stderr.
- risks: a call that omits a stage key and passes no level for it was admitted on an unmatched
  model and is now refused. The refusal's remedy, the full `stage-efforts` output, admits it. The
  two-workflow ceiling of §3 stands.
- testing: the arms of §7, each with its staged break.
- migration: none. The index's shape is unmoved and this tree's index bytes do not change. The
  first unit has not reached the default branch, so no adopter holds its hook.
- user docs: `help/roles.md`, S9.

## 6. Acceptance criteria

"The observation" and "the renderer probe" are the blocks of §4.

- **AC1** — When the observation runs, `r-swap` reads `deny:` naming `builder`, `gov-skeptic`,
  `medium` and `expected high`, and `r-swap-high` and `r-swap-fable` read `admit`.
  Red when: an unset stage is graded at the level of the slot the policy maps it to, or at the
  default stage table's level.
  figure: the levels are PINNED from `.claude/roles.json`, 2026-11-10.
- **AC2** — When the observation runs, `r-omit` reads `deny:` holding a `closing-review:` and a
  `spec-review:` part, each with `untyped`. `r-omit-spec` reads `deny:` naming `synthesis`,
  `expected medium` and `name no diffFinder`. `r-omit-spec-efforts` and `r-union` read `admit`,
  and `r-remap` reads `deny:` naming `diffFinder` and `gov-builder`.
  Red when: a stage key the call omits is graded at that workflow's `unset` level, or is refused
  at once without the other workflow being graded.
- **AC3** — When the observation runs, `s-entry` and `s-key` read `throw:` naming `build`,
  `s-sibling` reads `deny:` with no `nostage:` part, and `s-alone` reads `note:` naming `nostage`.
  Red when: a missing `stages` entry reads as no keys and admits, the loop walks one map's keys
  alone, or an unkeyed workflow admits beside a keyed one.
- **AC4** — When the renderer probe runs, its first line is `['build', 'nostage'] [{}, {}, {}]`
  and its second is `True`, and `python tools/roles/render_agents.py --check` exits 0 with no
  re-render.
  Red when: a stageless workflow gets no entry, leaves `harnesses`, or the change moves the tree's
  index.
- **AC5** — When an `Agent` payload whose `subagent_type` is `general-purpose`, with a
  `transcript_path` naming the observation's `fable.jsonl` and no `effort`, is piped to
  `node tools/hooks/agent-cap.js`, the exit is 2, stderr opens `BLOCKED by agent-cap: rule 6`,
  and stderr holds no `rule 8`.
  Red when: rule 8's block in `main()` runs before rule 6's verdict, which answers this call with
  rule 8's thrown refusal.
  fixture: the half of the order that puts rule 8 before rule 7 needs settings rule 7 refuses,
  which this checkout does not hold; the second item 7 arm of §7 carries it.
- **AC6** — When `git grep -c "rules 6 and 7" -- . ":(exclude)memory/builds"` runs, it prints
  nothing and exits 1.
  Red when: one of the six sites keeps the old pair.
  figure: six lines in four files at `df29bfe3`, PINNED 2026-11-10.
- **AC7** — When `grep -c "neither names counts as differing" tools/hooks/agent-cap.js
  tools/hooks/README.md` and `grep -c "is refused too" help/roles.md` run, each file's count is
  one or more.
  Red when: a document still says an unset stage runs at the stage's own agent type's level and
  nothing more. It reads tokens, never whether the account is right.
  figure: each count is `0` at `df29bfe3`, PINNED 2026-11-10.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `hook destinations (every declared hook path ships)` · `hook destinations self-test` · `agent-cap self-test` · `scratch-guard self-test` · `check-wiring self-test` · `verifier fan-out self-test` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `recall floor` · `recall floor arms` · `policy fixtures` · `codebase-map coverage + freshness` · `docs` · `kit/dogfood doc parity` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/agent-cap.test.sh · covers AC1 AC2 · the five item 1 rows of §4 "The arms"; staged by reading an unset stage's level from the `unset` map again, in the hook copy · none
New arm: tools/hooks/agent-cap.test.sh · covers AC1 · the two item 2 rows; staged by reading an unset stage's level from `default.stages` · none
New arm: tools/hooks/agent-cap.test.sh · covers AC3 · the four item 3 rows; staged by the empty-object default on the `stages` lookup with the loop over the table's keys alone · none
New arm: tools/hooks/agent-cap.test.sh · covers AC2 · the three item 4 rows; staged by returning the first workflow's verdict from the loop · none
New arm: tools/hooks/agent-cap.test.sh · covers none · item 5, the first unit's AC1 arms moved onto a transcript whose first main-chain model is another; staged by walking the transcript from its first line · none
New arm: tools/hooks/agent-cap.test.sh · covers none · item 5, the same arms with a `user` record naming a model after the last assistant entry; staged by dropping the `type` test from the read · none
New arm: tools/hooks/agent-cap.test.sh · covers AC5 · the first item 7 row; staged by moving rule 8's block, with the index read it needs, above rule 6's verdict · none
New arm: tools/hooks/agent-cap.test.sh · covers none · the second item 7 row; staged by moving rule 8's block below rule 7's · none
New arm: tools/hooks/agent-cap.test.sh · covers none · the item 9 row; staged by reducing the loader's rule to the outer plain-object test · none
New arm: tools/roles/adopt-roles.test.sh · covers AC1 · arm 6, the three `Workflow` payloads over the rendered index; staged by a renderer that keys `effort.harnesses` by workflow name · none, the floor is a minimum and these sit on arm 6's SKIP path
New arm: tools/roles/adopt-roles.test.sh · covers none · arm 6, the rendered tables against the verbs and the agent files; staged by a renderer that resolves a profile's `stages` with no model · none
New arm: tools/roles/render_agents.py · covers AC4 · the selftest's next arm, a stageless driven workflow; staged by building `stages` and `unset` from the staged workflows alone · none

What no leg checks: which workflow a two-workflow harness call runs, that a harness still types a
stage from `roles` and falls back as §4 "Evidence" reads it, and a rule list in prose that omits
a rule the header names.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft, from the round 1 closing review, the fix brief and the code
  read at `df29bfe3`.

## 10. Reuse audit

The seam is `checkEffortLevel` in `tools/hooks/agent-cap.js`, whose `Workflow` loop is rewritten
in place, with `extractWorkflowArgs` already giving it `a.roles`. The renderer half extends
`derive_effort_index` in `tools/roles/render_agents.py` through `resolve_stage_efforts`, which
already answers an empty map for a stageless workflow. The arms extend the rule 8 section and the
armed rule 7 section of the hook's suite, arm 6 of the roles adopter suite and the render
selftest. `python tools/codebase-map/reuse_lookup.py "the spawn guard grades an unset Workflow
stage at the level of the role the call's roles names, and refuses a harness workflow whose stage
keys the effort tables disagree on"` ranked `loadRoleIndex`, `resolve_effort`,
`resolve_stage_efforts` and `resolve_harness_path`, all already in use here, and no second reader
of a call's roles. The unit mints no identifier.

Recall terms used: spawn guard agent-cap rule 8 checkEffortLevel unset stage level args.roles efforts role index derive_effort_index stages harnesses stage-efforts harness-args
