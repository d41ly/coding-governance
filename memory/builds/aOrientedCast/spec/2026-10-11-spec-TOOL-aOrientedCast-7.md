# TOOL-aOrientedCast-7 — the spawn guard refuses an Agent or Workflow call that carries no rendered handoff

**Status:** CLOSED · rev-3 · 2026-10-12 · node a · Tier-2 · base 646d4a73 · streams tooling · order 10 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md](../build/2026-10-11-build-TOOL-aOrientedCast-1-cross-read.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-8 |
| [2026-10-11-build-TOOL-aOrientedCast-7-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aOrientedCast-7-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-2-build-brief.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-3-cross-read.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-1.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-1.md) | research | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-8 |
| [2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-9-1-fold-brief.md) | journal | KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-6 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's mandate says every agent prompt is a rendered handoff, never freeform, and today
`agent-cap.js` bounds how many agents run while reading nothing about what they are told. This unit
gives it a sixth rule. An `Agent` call is admitted only when its `subagent_type` is a role the
repository's index declares spawnable and its `prompt` is exactly the task part of a rendered handoff
file for that role. A `Workflow` call is admitted only when its `scriptPath` is a declared harness and
its `args` hand that harness a `roles` object of known roles.

## 2. Scope (IN)

- **S1** — Rule 6 runs in `main` after the `AGENT_CAP` refusal and the declared-cap read, which deny
  every call, and before rule 4 on an `Agent` call and rule 0 on a `Workflow` call. A spawn rule 6
  refuses therefore claims no slot. It runs only when no `--only=` selector is given, as rules 0 to 3
  do. Observed by AC3 and AC5.
- **S2** — The index is `.claude/roles.json` at the checkout root of the payload `cwd`, read through
  `loadRoleIndex`, which `TOOL-aOrientedCast-6` exports from `scratch-guard.js`. Arming, as §8 F3
  resolved it: an absent index adds no rule; a broken one refuses every `Agent` and `Workflow` call
  naming the file; an index with no `agent`-true role refuses every `Agent` call as UNARMED, and one
  with an empty `harnesses` list refuses every `Workflow` call as UNARMED. Observed by AC5.
- **S3** — An `Agent` call's `tool_input.subagent_type` must name a role whose `agent` is true. A
  built-in type, an absent type and an `agent`-false role are refused, as §8 F1 resolved it. Observed
  by AC2 and AC7.
- **S4** — Its `tool_input.prompt` must carry exactly one `gov:handoff` marker line, in the grammar of
  §4 "Data model", whose `role` equals the `subagent_type`. The marker's `path` must be repo-relative,
  hold no `..`, sit under `builds/<the marker's build>/prompts/`, and name a file under the checkout
  root whose own single marker line is byte-equal to the prompt's. Observed by AC2.
- **S5** — The prompt, line endings folded and its ends trimmed, must be that marker line, blank lines,
  then the file's `## Task` section and nothing else, as §8 F4 resolved it. The section's digest must
  equal the marker's `task-sha`, so a file whose section was edited after rendering is refused too.
  Observed by AC1, AC2 and AC6.
- **S6** — A `Workflow` call carrying an inline `script`, or naming no `scriptPath`, is refused. Its
  `scriptPath`, resolved against the payload `cwd` and taken relative to the checkout root, must equal
  an entry of `harnesses` in `buildComparablePath`'s form. Its `args`, parsed by `extractWorkflowArgs`,
  must carry a `roles` plain object with at least one entry, every value naming an `agent`-true role.
  Rule 0 parses `args` through the same helper, and its existing arms re-observe that its verdicts do
  not move. Observed by AC4 and AC7.
- **S7** — A throw anywhere inside rule 6 refuses with the error named, the fail-closed posture rule 0
  already keeps. NOT OBSERVED by a criterion of its own: once every input is guarded no payload reaches
  a throw, so the catch is a backstop, and the builder stages a throw once when the arm goes RED first.
- **S8** — Every refusal names the call, the reason, the `agent`-true roles or the harnesses, and the
  route that passes: `handoff.py render --role <name> --build <slug> --part task` for a spawn, and
  `roles` from `handoff.py harness-args <harness>` for a harness. Observed by AC2 and AC4.
- **S9** — The file header gains rule 6, its order and its ceiling, and `tools/hooks/README.md` gains a
  section stating the same. NOT OBSERVED by a criterion: prose. The review reads it against §4.
- **S10** — The arms live in `tools/hooks/agent-cap.test.sh` over a fixture repository the suite
  builds, each observed RED on a staged break first. Every arm that exists today runs with no index,
  which is S2's absent case observed unchanged. Observed by AC1 to AC5.
- **S11** — The `--only=` selector's closed set gains `scripts`: rules 1, 2, 3 and 5, the rules that
  read a script, and never rule 0 or rule 6, which judge the call. `check-verifier-fanout.sh` passes
  it, because that gate feeds every committed workflow script to the hook as an inline `script` from
  the checkout root, and rule 6 refuses an inline script wherever an index exists, gov's tree
  included. The `unattended-build.test.sh` arm that asks the hook to admit the build harness passes
  `roles` in its `args`. A wired command still carries no `--only=`, which `check-wiring.sh` already
  asserts for any value. Observed by AC5.

## 3. Non-goals (OUT)

- `SendMessage` to another session. It is not an `Agent` or `Workflow` call and this matcher never sees
  it. The `gov-session` slot and the renderer are that handoff's workflow today; gating it is a
  follow-up.
- The agents a running harness spawns. Its `agent()` is a runtime call and not a tool call, so the hook
  judges only the call that starts the harness, never the `agentType` the harness passes inside. An
  untyped harness agent reads `workflow-subagent`, which `TOOL-aOrientedCast-6` refuses spec and product
  writes.
- Proving the renderer wrote a prompt file. The digest proves the prompt equals a file on disk whose
  section matches its marker. A hand-written file that agrees with itself passes, and
  `handoff.py check` plus the build's records are where provenance shows.
- Checking `role-sha` against the role block an agent type was rendered with. A handoff rendered before
  a role edit is admitted; the render leg's byte-compare of `.claude/agents/` owns staleness.
- Making the drift-audit workflows and `orient-counterfactual.js` declared harnesses that take `roles`.
  §8 F2 refuses them until they do, and that conversion is a follow-up outside this build.
- Changing rules 0 to 5, the slot ledger, the cap or the wiring. The matcher already covers both tools.
- A waiver, an environment knob or a warn phase. Enforcement starts at landing, by the owner's ruling.

**This run is not bound by this rule until it lands.** This session's hooks run from the PRIMARY tree
(the mandate record's orientation finding), so this rule binds this session only once the landing
merge is in the primary tree's working copy. Every `Workflow` call the close makes before that moment,
its closing review included, runs under today's rules. After it, this session can spawn nothing: its
agent registry was read before `.claude/agents/` existed, so it holds no role type, and every built-in
type is refused. A repair owed after the landing merge therefore belongs to a fresh session.

### Edges

- **consumes-from** `TOOL-aOrientedCast-2` — the marker grammar, the `--part task` output and the span
  `task-sha` hashes. Without them no prompt can pass, and AC6 has no renderer to agree with.
- **consumes-from** `TOOL-aOrientedCast-3` — the generated `.claude/roles.json`, its `agent` flags and
  its `harnesses` list. Without it gov's tree is unarmed and AC7 has nothing to observe.
- **consumes-from** `TOOL-aOrientedCast-6` — `loadRoleIndex`, exported from `scratch-guard.js`, so the
  two hooks read the index once and identically.
- **consumes-from** `TOOL-aOrientedCast-4` — the build and unit harnesses' `roles` argument, which this
  rule requires on every call to them. Without it every build and unit call, attended or not, is
  refused at landing.
- **consumes-from** `TOOL-aOrientedCast-5` — the review harness's `roles` argument, which this rule
  requires on every closing-review call. Without it no closing review can run.
- **consumes-from** `KICK-aOrientedCast-2` — the attended router, which composes every agent prompt as
  a rendered handoff and every harness call with `roles`. Without it an attended build has no route
  this rule admits.
- **consumes-from** `TOOL-aOrientedCast-9` — the unattended Skill and verbs passing `roles` on every
  harness call. Without it every unattended build is refused from this rule's landing, gov's own
  concurrent runs included.
- **hands-off** external — making the drift-audit workflows and the orientation counterfactual into
  declared harnesses that take a roles argument, so the drift-audit Skill's two tiers and the stage-2
  matrix ask run again in an armed repository.
- **hands-off** external — gating a session-to-session message, which this matcher never sees.
- **hands-off** external — every other running session of this repository on the landing node, which
  meets this rule the moment the landing merge is in the primary tree and must restart before it can
  spawn a role.

## 4. Design

### Evidence

Read at `646d4a73` on 2026-10-11; nothing under `tools/` or `.claude/` moved between it and `744e55db2`.

- `main` (`tools/hooks/agent-cap.js:2010`) refuses a set `AGENT_CAP` and reads the declared cap before
  any rule (`:2062`, `:2078`). An `Agent` payload runs rule 4 alone (`:2088`), and `guardAgentSpawn`
  (`:1661`) claims a slot with an exclusive create on the first spawn it admits.
- Rule 0 runs above the script read and only when no `--only=` selector is set (`:2099`). It parses
  `tool_input.args` from a string first and admits on a string that does not parse (`:1885-1889`).
- A `scriptPath` is read from disk when no inline `script` is given (`:2111-2124`), and a call with
  neither, a `name:` run, exits 0 (`:2125`).
- `resolveCheckoutRoot` (`:1563`) and `extractBuildSlug` (`:1848`) are the walk and the build-folder
  read this rule reuses. On win32 rule 0 folds an MSYS drive spelling before `path.resolve` (`:1940`).
- The file requires `scratch-guard.js` lazily for `readConfKey` and `readFrontMatterKey` (`:1865`,
  `:1947`), and it ends in a bare `main()` (`:2216`), so it exports nothing.
- `.claude/settings.json:5` wires it on `Workflow|Agent`, so no wiring changes.
- Two callers outside the hooks kit run the hook on a payload no tool call sends: the
  `verifier fan-out` leg (`tools/workflows/check-verifier-fanout.sh`) pipes each committed workflow
  script as an inline `script` with no `cwd`, from the checkout root, and an arm of
  `tools/workflows/unattended-build.test.sh` pipes the build harness's `scriptPath` with no `args`.
  Found at the build pass, 2026-10-12, by grepping every caller of `agent-cap.js`; `check-review-join.sh`
  already passes `--only=join` and never meets rule 6.
- The `Agent` tool input carries `subagent_type` and `prompt`, and the `Workflow` tool input carries
  `scriptPath`, `script`, `name` and `args`: verified 2026-10-11 on node a from the tool-use blocks the
  measurement below reads.
- Both drift-audit tiers are run by `scriptPath` (`.claude/skills/drift-audit/SKILL.md:66-67`), and the
  unattended verbs compose every harness call by `scriptPath` (`memory/guides/UNATTENDED-VERBS.md:725`).
- `orient-counterfactual.js` runs one arm per call under agent type `orient` or `Explore` (its header,
  `tools/workflows/orient-counterfactual.js:4`), and the open ask `TOOL-aReplayedCard-9` asks for its
  eight-arm matrix to be run.
- A definition created in a running session is not spawnable (`TOOL-aReplayedCard-5`), and a custom type
  reports its own name as `agent_type`
  (`memory/builds/aOrientedCast/build/2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md:39-51`).

### Measurement — last week's spawns against this rule

PINNED, measured 2026-10-11 on node a by a read-only scratch instrument over 5157 transcript files
under the Claude projects directories whose name carries `coding-governance`. It reads every
`tool_use` block named `Agent`, `Task` or `Workflow` timestamped 2026-10-04 to 2026-10-11, deduplicated
by its id: 412 calls from 25 sessions.

| Call | Count | Rule 6 at landing |
|---|---|---|
| `Agent`, `general-purpose` | 67 | refused, the target class: a freeform prompt |
| `Agent`, `Explore` | 19 | refused, the target class: 14 mapped or researched, 5 reviewed |
| `Agent`, `claude-code-guide` | 3 | refused, the target class: CLI capability questions |
| `Agent`, a type that does not exist | 1 | refused, and the CLI refuses it anyway |
| `Workflow`, a harness by `scriptPath` | 304 | near-miss: 236 unit, 45 build, 23 review calls, none carrying `roles` |
| `Workflow`, a non-harness `scriptPath` | 8 | refused: 7 bench scripts in a scratchpad, 1 trial instrument in a build folder |
| `Workflow`, an inline `script` | 10 | refused, the target class |

No `Agent` prompt carried a `gov:handoff` marker, and no call used `Plan`, the drift-audit workflows or
`orient-counterfactual.js`. The 304 near-misses pass once `TOOL-aOrientedCast-4` and
`TOOL-aOrientedCast-5` have the harnesses take `roles` and their callers pass it.

### Data model

The marker line, interface 7 of this build's spec brief, read and never written here:

```
<!-- gov:handoff role=<name> build=<slug> unit=<id|-> path=<repo-relative path> role-sha=<12 hex> task-sha=<12 hex> -->
```

`extractHandoffMarker(text)` returns every line, carriage returns stripped, that matches this whole
line with the six fields in that order, each value free of spaces and each digest twelve lowercase hex.
Rule 6 requires exactly one in the prompt and exactly one in the file.

`extractTaskSection(text)` returns the text from the line that is exactly `## Task` to the end, line
endings folded to LF. `buildTaskDigest(section)` is the first twelve hex digits of its SHA-256, through
node's `crypto`. The span and the folding are `TOOL-aOrientedCast-2`'s definition, as interface 7 states
it: the section's bytes, LF-normalized. This spec reads that as the heading line through the end of the
file. AC6 is the observation that the two readings agree, and a disagreement found there is a defect in
exactly one of the two specs, fixed by a rev bump before the code.

The index is interface 9's `{ "roles": { <name>: { "workflow", "writes", "agent" } }, "harnesses":
[<repo-relative script path>] }`, through `loadRoleIndex`. The harness `roles` argument is interface
10's object of stage key to agent type; this rule reads only its values, because the stage keys belong
to each harness and a hook naming them would restate them.

### The evaluation order — rule 6

Rule 6 returns null to admit or a deny string. Every step below allows only on its own condition.

1. `loadRoleIndex(resolveCheckoutRoot(cwd))`, required lazily inside a try: absent → null. Broken →
   deny naming the index. A sibling that cannot be required → deny, as rule 0 treats it.
2. An `Agent` call:
   1. no `agent`-true role in the index → deny, UNARMED;
   2. `subagent_type` not a string naming an `agent`-true role → deny naming the type and those roles;
   3. `prompt` not a string, or not carrying exactly one marker → deny;
   4. the marker's `role` differs from `subagent_type` → deny;
   5. its `path` absolute, `~`-rooted, holding `..`, or not under `builds/<build>/prompts/` by
      `extractBuildSlug` and the segment after it → deny;
   6. no regular file at that path under the checkout root → deny naming it;
   7. the file not holding exactly one marker byte-equal to the prompt's → deny;
   8. the prompt, folded and trimmed, not the marker line, blank lines and the file's section, trailing
      whitespace aside → deny naming the first line that differs;
   9. `buildTaskDigest` of the file's section differing from `task-sha` → deny naming both;
   10. otherwise null, and rule 4 then claims its slot as today.
3. A `Workflow` call:
   1. `harnesses` empty → deny, UNARMED;
   2. a non-empty inline `script` → deny; no `scriptPath` → deny, naming a `name:` run;
   3. the `scriptPath`, MSYS-folded on win32, resolved against `cwd`, realpath'd and taken relative to
      the realpath'd checkout root, matching no `harnesses` entry in comparable form → deny naming both;
   4. `extractWorkflowArgs` yielding no plain object → deny;
   5. `roles` absent, not a plain object, or empty → deny naming `handoff.py harness-args`;
   6. a `roles` value not a string naming an `agent`-true role → deny naming it;
   7. otherwise null, and rule 0 then rules 1 to 5 run as today.

### Refusal text

`renderHandoffDeny` opens `BLOCKED by agent-cap: rule 6`, names the tool and the step that refused,
and ends with what passes. A spawn refusal lists the `agent`-true roles and says to render the handoff
with `handoff.py render --role <name> --build <slug> --part task`, then pass its output unchanged as
`prompt` with `subagent_type` that role; a built-in type is told that research runs as the researcher
role. A harness refusal lists `harnesses` and says to pass `roles` from `handoff.py harness-args
<harness>`. The renderer is named by its bare file name, because a kit file names no sibling kit by
literal.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `checkHandoffSpawn` | function, rule 6 on an `Agent` call | `js.function`; `lexicon.py --suggest checkHandoffSpawn --as js.function` answered OK |
| `checkHarnessCall` | function, rule 6 on a `Workflow` call | `js.function`; answered OK |
| `extractHandoffMarker` | function, the marker lines of a text | `js.function`; answered OK |
| `extractTaskSection` | function, the `## Task` section | `js.function`; answered OK |
| `buildTaskDigest` | function, twelve hex of SHA-256 | `js.function`; answered OK |
| `extractWorkflowArgs` | function, `args` parsed once for rules 0 and 6 | `js.function`; answered OK |
| `renderHandoffDeny` | function, the refusal text | `js.function`; answered OK |
| `write_roles`, `write_handoff`, `run_spawn`, `run_harness` | self-test helpers | `sh.function`; answered OK |
| `HANDOFF_MARK` | string constant, `gov:handoff` | none: no constant cell is declared in `.lexicon.conf` |

### Rollout

Lands at order 10, the build's last unit. It needs `TOOL-aOrientedCast-2`'s renderer, gov's index from
`TOOL-aOrientedCast-3`, `TOOL-aOrientedCast-4` and `TOOL-aOrientedCast-5` having the three harnesses take
`roles`, and both callers passing it, both at order 6: `KICK-aOrientedCast-2`'s attended router and
`TOOL-aOrientedCast-9`'s unattended Skill and verbs. Without them gov's own builds are refused at
landing. One commit carries the hook, its arms and its README section; no settings change.
A hook script is read afresh on every call, so the rule binds every session whose hooks run from a tree
holding this commit, from its next spawn, as §3 says for this one. This is the hooks kit's last unit in
the build: its version and five carriers move once after it, and `govkit.py epoch` reports the move as
owed until then.

### Files touched (estimate)

`tools/hooks/agent-cap.js` · `tools/hooks/agent-cap.test.sh` · `tools/hooks/README.md` · `tools/workflows/check-verifier-fanout.sh` · `tools/workflows/unattended-build.test.sh` · `memory/map/features/agent-cap.md` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **Shelling out to `handoff.py check` from the hook.** It names a sibling kit's file by path, which
  the kit authoring rule bans, and spends a Python spawn on every `Agent` call. One SHA-256 in node is
  the same check.
- **Matching only the marker and the digest, and admitting other text around them.** §8 F4: a freeform
  preamble before a valid marker is the freeform prompt the mandate forbids.
- **Counting `Workflow` calls in the slot ledger to reach harness agents.** The README already states
  why the two mechanisms stay apart; and a harness's runtime agents are invisible to any tool hook.
- **Reading the stage keys of each harness to require a full `roles` object.** The keys live in each
  harness, and a hook spelling them would be a second copy that rots; a partial object leaves the
  missing stages untyped, and the write gate refuses an untyped agent's spec and product writes.

## 5. Production-readiness checklist

- security — Per `Agent` call: one index read, one prompt-file read under the checkout root, one
  SHA-256. Per `Workflow` call: one index read and one realpath. The payload's `path` is checked for
  containment before it is joined, and nothing is put into a shell or a regex. The rule stops
  forgetting, not evasion, and the header says what passes it: a hook-less or `--bare` run, a harness's
  runtime agents, a session-to-session message, a self-consistent hand-written prompt file and a
  hand-edited index.
- perf / scale — The hook already spawns once per call, and the slot ledger already reads and creates
  files per spawn. A prompt file is tens of kilobytes at most. No git spawn.
- error / empty / loading states — An absent index admits as today; a broken index, an UNARMED tool,
  each malformed field and a throw refuse with the cause named.
- observability — Each refusal names the step and the route that passes; a prompt that drifted from its
  file names the first differing line, so the caller can resend the file's bytes.
- risks — A model copying a long task block into `prompt` may change a character and be refused;
  reading the file and passing its task part verbatim is the remedy the refusal names. From landing,
  ad-hoc `Workflow` instruments and inline scripts are refused, 18 of 322 calls last week, so a research
  build declares its instrument as a harness first. Gov's index missing a harness refuses that harness at
  landing, which AC7 observes before the close.
- testing — The arms in §7 over a fixture repository the suite builds; every existing arm runs with no
  index, so their verdicts at base are S2's absent case.
- migration — None in gov beyond landing. An adopter receives the rule with the hooks kit and is
  unaffected until `TOOL-aOrientedCast-8` renders its index.
- user docs — The `tools/hooks/README.md` section; the refusal text is the in-session documentation.

## 6. Acceptance criteria

- **AC1** — When `node tools/hooks/agent-cap.js` reads an `Agent` payload whose `subagent_type` is
  `gov-researcher` and whose `prompt` is the fixture prompt file's marker line and `## Task` section, it
  exits 0 with empty stderr and the turn's slot ledger holds the call's `tool_use_id`. The same prompt
  with CRLF line endings and surrounding blank lines exits 0.
  Red when: a correctly rendered handoff is refused, or line-ending or end-whitespace drift refuses it.
- **AC2** — When `subagent_type` is `general-purpose`, `Explore`, absent, or the `agent`-false
  `gov-session`, the hook exits 2 naming the type and `gov-researcher`. It exits 2 naming the cause for a
  prompt with no marker or two, a marker whose `role` differs from the type, a `path` holding `..` or
  outside `builds/bx/prompts/`, a `path` naming no file, a task section one character off, a freeform
  line before the marker or after the section, and a file whose section no longer matches its
  `task-sha`.
  Red when: any of those spawns is admitted.
- **AC3** — When five refused `Agent` calls and then one admitted call arrive under one `session_id`
  and `prompt_id`, the admitted call exits 0 and `slot-1` of that turn holds its `tool_use_id`.
  Red when: rule 6 runs after rule 4, so a refused spawn spends the turn's budget.
- **AC4** — When a `Workflow` payload names the fixture's listed harness as `scriptPath` and passes
  `args` carrying `roles` `{"builder":"gov-builder"}`, as an object and as a JSON string, the hook exits
  0. It exits 2 for an inline `script`, a `name`-only call, a `scriptPath` not in `harnesses`, `args`
  that do not parse, and the harness with no `roles`, with `{}`, or with a value naming an unknown or
  `agent`-false role.
  Red when: a call outside a declared harness, or a harness call handing it no known role, is admitted.
- **AC5** — With no `roles.json` in the fixture, a `general-purpose` `Agent` call exits 0 and claims a
  slot, and an inline `script` that passes rules 1 to 5 exits 0, as at base. With `roles.json` holding
  `{`, both exit 2 naming the index. With no `agent`-true role, the `Agent` call exits 2 naming
  `UNARMED`; with `harnesses` empty, the `Workflow` call exits 2 naming `UNARMED`. Under `--only=join`
  neither call meets rule 6, and under `--only=scripts` the inline `script` exits 0 with the index
  broken while a raw `parallel(` in it exits 2.
  Red when: a broken or empty index admits, an absent index moves a verdict, or either selector runs
  rule 6, or the `scripts` selector skips the fan-out rules.
- **AC6** — When the `--part task` output of `handoff.py render` for a fixture card, brief and spec is
  passed as `prompt` with `subagent_type` its role, the hook exits 0, and the hook's digest of that
  file's `## Task` section equals the `task-sha` that `handoff.py check` re-derives.
  Red when: the hook hashes a span or a line-ending fold other than the renderer's.
  fixture: the renderer `TOOL-aOrientedCast-2` builds at order 2; the tree holds none at `646d4a73`.
- **AC7** — When the hook reads, from this repository, a `Workflow` payload whose `scriptPath` is
  `tools/workflows/unattended-unit.js` and whose `roles` is `{"builder":"gov-builder"}`, it passes rule
  6, and the same payload with no `roles` exits 2. An `Agent` payload with `subagent_type` `Explore`
  exits 2 naming `gov-researcher`.
  Red when: gov lands an index whose `harnesses` omits the unit harness or whose roles lack the
  researcher, so the build's own route is refused or a built-in admitted.
  fixture: this repository once `TOOL-aOrientedCast-3` has committed its index; the tree holds none at
  `646d4a73`.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `verifier fan-out` · `tier2-review self-test` · `unattended-build self-test` · `recall floor` · `recall floor arms` · `agent-cap restatement` · `hook destinations (every declared hook path ships)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/agent-cap.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the base hook, which admits every Agent call under the slot cap and every Workflow call whose script passes rules 0 to 5 · none

AC6 runs the renderer against the hook once, at the build pass; AC7 is a direct observation of this
repository after `TOOL-aOrientedCast-3` lands. Neither adds an arm. The close's bar runs the legs above
once; no pass runs them.

## 8. Open questions

- **F1 — What happens to the built-in agent types: `Explore`, `Plan`, `claude-code-guide` and
  `general-purpose`?**
  §4 "Measurement": 90 `Agent` calls last week, 67 `general-purpose`, 19 `Explore`, 3
  `claude-code-guide`, none `Plan`, and none carried a handoff. Options:
  - (a) Refuse every type that is not an `agent`-true role. Research and mapping run as
    `gov-researcher`, review as the review roles. What is lost: the built-in `Explore`'s own model and
    fixed read-only tool set, which the researcher's `tools` and `model` front matter can reproduce,
    and `claude-code-guide`'s built-in documentation prompt, which nothing in this repository can read
    (UNVERIFIED what it holds); the researcher reaches the same public pages only if its `tools` grant
    web access.
  - (b) Admit a fixed list of read-only built-ins without a handoff. The list is either typed in a kit
    file, where it rots as the CLI's built-in set moves, or a new key in the index, which changes
    interface 9 and needs a fork naming it. 22 of last week's 90 spawns stay freeform.
  - (c) Admit a built-in type when its prompt carries a valid handoff for some role. The marker's role
    would no longer equal the type, which is the brief's own rule, and the role block never reaches the
    agent, because a built-in carries its own system prompt.
  Recommendation: (a). It is the brief's rule with no interface change, and its losses are named.
  RESOLVED (agent, 2026-10-11, delegated): (a). S3 refuses every type that is not an `agent`-true role,
  and the refusal tells a built-in caller that research runs as the researcher role.
- **F2 — What happens to `Workflow` scripts that are not declared harnesses?**
  Last week: 304 harness calls, 8 non-harness `scriptPath` calls and 10 inline scripts, and no call to
  the drift-audit workflows or `orient-counterfactual.js`. Options:
  - (a) Refuse them all. The drift-audit Skill's two tiers, the stage-2 matrix ask and ad-hoc trial
    instruments run again once declared as harnesses taking `roles`, which is a follow-up.
  - (b) Admit any tracked `scriptPath` without `roles`. The one tracked trial instrument last week would
    pass, and so would any committed script spawning untyped agents with freeform prompts.
  - (c) Admit a declared exemption list from the index. It changes interface 9, and every exempt
    script runs freeform agents, which is the defect the mandate names.
  Recommendation: (a). It costs 18 calls a week, none of them the drift-audit tiers, and every option
  that keeps them running admits the freeform prompt the rule exists to stop.
  RESOLVED (agent, 2026-10-11, delegated): (a), with the conversion recorded in §3 as an external
  hands-off.
- **F3 — How is the rule armed, and what does a repository without the roles kit see?**
  Options, as for the write gate: (a) an absent index adds no rule; a broken one refuses both tools; an
  index with no `agent`-true role, or no harness, refuses that tool as UNARMED. (b) An index with no
  spawnable role leaves the tool unarmed and admitted. (c) An absent index where the roles kit is
  installed refuses, which needs this hook to read govkit's install receipt, a sibling kit's file.
  (b) makes deleting a role a silent off, which the owner's no-bypass ruling forbids, and (c) names a
  sibling by literal. Under (a) an uninstalled kit is untouched, and an installed-but-unrendered one is
  reported by `TOOL-aOrientedCast-8` at session start.
  Recommendation: (a), the arming `TOOL-aOrientedCast-6` resolved, so the two hooks agree.
  RESOLVED (agent, 2026-10-11, delegated): (a), as S2 is written.
- **F4 — How much of the prompt must be the rendered handoff?**
  Options: (a) all of it: the marker line and the file's `## Task` section, line endings and the two
  ends aside. (b) The marker and a section whose digest matches, with any other text around them. (c)
  The marker alone. Under (b) a freeform preamble before a valid marker passes, and under (c) any task
  text does; both are the freeform prompt the mandate forbids. (a) refuses a model that alters a long
  block while copying it, and the refusal names the first differing line so the caller resends the
  file's bytes.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a), as S5 is written.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S8 · §3 · §4 · the M2 cross-read's findings 3, 4 and 8. S8's render command
  spells `--build <slug>`, as §4's refusal text already did. The Edges gain consumes-from lines for
  `TOOL-aOrientedCast-4`, `TOOL-aOrientedCast-5`, `KICK-aOrientedCast-2` and `TOOL-aOrientedCast-9`,
  and the Rollout's precondition on the unattended verbs is that last unit at its order 6, not an
  unscheduled owner turn.
- rev-3 · 2026-10-12 · S11 · §4 Evidence · Files touched · AC5. The build pass found that the
  `verifier fan-out` merge-bar leg pipes every committed workflow script to the hook as an inline
  `script` from the checkout root, which rule 6 refuses under gov's index, and that an
  `unattended-build.test.sh` arm asks the hook to admit the build harness with no `roles`. S11 adds
  `--only=scripts` for the leg and `roles` for the arm; AC5 observes the selector. §7 gains the
  `verifier fan-out` leg and the two self-tests whose guards the two new paths trip.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse an Agent tool call whose subagent_type is not a
declared role or whose prompt carries no rendered handoff marker with a matching task hash, and a
Workflow call whose scriptPath is not a declared harness"` ranked no seam that fits: its candidates
were name-stem matches such as `declares` in `gotchas.py`, `CensusRefused` and `deriveSidecarPath`, none
reading a tool payload. The seams extended are in this kit: `main`'s rule order, `extractBuildSlug`,
`resolveCheckoutRoot` and rule 0's `args` parse in `tools/hooks/agent-cap.js`, and `loadRoleIndex` and
`buildComparablePath` from `tools/hooks/scratch-guard.js`, which this file already requires. The digest
reuses node's own `crypto`; no hashing helper exists in the kit.

Recall terms used: `agent-cap PreToolUse Workflow Agent subagent_type scriptPath inline script Explore
Plan workerType agentType handoff` — which surfaced this build's spec brief, `TOOL-aBatchedTribunal-1b`,
which put enforcement at the `Workflow` tool call because inline scripts were the failing modality,
`TOOL-aReplayedCard-9`, the open ask to run `orient-counterfactual.js`'s matrix that §8 F2 now refuses,
and `TOOL-aMendedFleet-67`'s record of `agentType` in a workflow `agent()` call.
