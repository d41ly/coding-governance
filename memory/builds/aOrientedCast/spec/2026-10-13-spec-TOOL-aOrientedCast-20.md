# TOOL-aOrientedCast-20 — the roles kit derives each agent's dispatch and return lines, and adds them to a generated per-build agent ledger

**Status:** CLOSED · rev-2 · 2026-10-13 · node a · Tier-2 · base 646d4a73 · streams tooling · order 22

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md](../build/2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 TOOL-aOrientedCast-21 TOOL-aOrientedCast-22 TOOL-aOrientedCast-23 |
| [2026-10-13-build-TOOL-aOrientedCast-20-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aOrientedCast-20-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-aOrientedCast-20-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-20-1-spec-brief.md) | journal | TOOL-aOrientedCast-19 TOOL-aOrientedCast-21 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 |
| [2026-10-13-prompt-TOOL-aOrientedCast-20-2-spec-writer.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-20-2-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The owner's third addendum asks that every agent a session dispatches or receives be shown with its
role, effort, model, unit, prompt, write class, gate allowlist and ids, and on return what it
produced, its wall time and its tokens, derived rather than typed and kept in a per-build ledger.
`PLAY-aOrientedCast-3` puts the two line shapes into the charter. This unit adds the roles kit verb
that fills them from what the session already recorded, prints them, and adds each complete one to
the build's agent ledger.

## 2. Scope (IN)

- **S1** — `python handoff.py agents (--handoff <path> | --run <run-id>) [--session <file>]` prints,
  for each agent its selector names, its `agent` line, then its `returned` line once it has
  returned, under §4 "The verb". Observed by AC1, AC2, AC3 and AC6.
- **S2** — `roles_lib.extract_microformat_shapes` reads the `agent` and `returned` definitions from
  the governing doc's micro-format fence, and the verb fills each placeholder by name from §4 "The
  fields". A missing definition, or a placeholder the verb does not derive, refuses. Observed by AC4.
- **S3** — Every field comes from the session's own records, the role index and the agent types,
  with the fallbacks of §4 "The fields"; a field nothing answers prints `unknown`. Observed by AC1,
  AC2 and AC3.
- **S4** — The verb adds each printed line holding no `unknown` field to the build's agent ledger,
  once, under §4 "The ledger": its name and head fit `memory/HYGIENE.md` checks 5 and 21, and its
  links resolve from its own folder. Observed by AC5 and AC6.
- **S5** — The `/build` Skill names the verb in its "Before stage 3" section, and the rendered Skill
  is re-rendered. Observed by AC8.
- **S6** — `tools/roles/adopt-roles.test.sh` gains arm 9 of §4 "The suite arm", and its
  `FLOOR_ASSERTIONS` rises by its three assertions. Observed by AC1 and AC5, whose break the arm
  stages at the close.
- **S7** — The prose follows: `handoff.py`'s docstring, the roles README's new section "The agent
  lines", a `help/roles.md` section and the roles dossier, each as §4 "Documentation" states.
  Observed by AC10 for the help page; the rest is NOT OBSERVED: prose, read by the closing review.
- **S8** — The roles kit moves from 1.2 to 1.3 with every carrier: this is the last unit of the set
  to touch `tools/roles/`. Observed by AC9.
- **S9** — The two location probes at `tools/roles/adopt-roles.test.sh:29-30` run with `GIT_DIR` and
  `GIT_WORK_TREE` unset, first in their substitutions, under §4 "The suite's location probes", and
  arm 9 adds no bare one. Observed by AC11.

## 3. Non-goals (OUT)

- The shapes and the rule that makes them mandatory: `PLAY-aOrientedCast-3`'s.
- Refusing a final message that omits a line: `TOOL-aOrientedCast-21`'s.
- A gate over the ledger. Its lines come from transcripts that live on one machine, so no other node
  can re-derive them; the docstring says a hand-edited line passes.
- A change to the unattended Skill or verbs, which ship in another kit. The charter rule binds those
  runs, and their main loop calls this verb as any other does.
- Printing any prompt, message or tool text, or reading a transcript beyond the fields §4 names.
- A merge driver for two worktrees adding to one ledger; they reconcile additively (§5 risks).
- Moving the transcript readers into a shared library, or calling the run-log kit (§8 F2).
- A `check_roles.py` rule, and any edit to `render_agents.py`, whose `AGENTS_REL` and `INDEX_REL`
  the verb imports as `print_roster` imports the checker's pattern.

### Edges

- **consumes-from** `PLAY-aOrientedCast-3` — the `agent` and `returned` definitions in the governing
  doc's micro-format fence, with the placeholders `<role>`, `<level>`, `<model>`, `<unit-id|label>`,
  `<name>`, `<path>`, `<class>`, `<legs|none>`, `<run-id|direct>`, `<agent-id>`, `<outcome>`,
  `<wall>` and `<tokens>`. Without them the verb refuses on gov's charter, and AC7 cannot be observed.
- **hands-off** `TOOL-aOrientedCast-21` — `handoff.py agents`, named in format-guard's refusal by
  its bare file name and verb as the route that passes; and the run field every line ends with,
  `/<agent-id>` after the run, which is what that hook matches an agent by.

## 4. Design

Line numbers were read at `1e89fa5cd`, the run branch's HEAD on 2026-10-13. The charter there is
v4.3 and carries neither shape; `PLAY-aOrientedCast-3`, order 21, lands before this unit.

### Evidence — what a session records

Measured on this build's own session on 2026-10-13, Claude Code 2.1.295, and on the forty most
recent sessions of node a for the `Agent` result keys. The transcript format is no contract, as the
run-log kit's extractor says of itself, so each fact below is a reading, not an interface.

| Record | Where | What the verb reads |
|---|---|---|
| the session file | `<projects>/<project>/<session id>.jsonl` | an `Agent` or `Workflow` `tool_use` block's `id` and `input`; the `tool_result` for it and that record's `toolUseResult`; a `<task-notification>` block in a `user` record, a `queued_command` attachment or a `queue-operation` record |
| `Agent` result | `toolUseResult` | `agentId`, `resolvedModel`, and `status`: `async_launched`, or `completed` for a foreground call |
| `Workflow` result | `toolUseResult` | `runId`, such as `wf_49d26cb6-a00` |
| notification | the user record's text | `<tool-use-id>` and `<status>`, such as `completed` |
| a direct spawn | `<session dir>/subagents/agent-<id>.jsonl` and `.meta.json` | the meta's `agentType` and `description` |
| a harness run | `<session dir>/subagents/workflows/<run id>/journal.jsonl` | `started` entries with `agentId` and `label`; `result` entries with `agentId` and `result`; `failed` entries with `agentId` |
| a harness agent | `agent-<id>.jsonl` and `.meta.json` beside the journal | as for a direct spawn |
| an agent's transcript | every `assistant` record | `message.model`, `message.id`, `message.usage.output_tokens`, `effort`, `timestamp`, and its `tool_use` blocks |

`<session dir>` is the session file's path without `.jsonl`. Two facts shape the design:

- Every `assistant` record of the four transcripts sampled carries a top-level `effort`: `xhigh` for
  both spec writers and `high` for the builder, each its level in the policy file, and `high` for
  the harness's untyped commit agent. The addendum's record says no file records effort; that held
  for the fields it read, and the field it missed decides §8 F1.
- One API response is split into several `assistant` records sharing a `message.id`, each carrying
  `usage` as it streamed: the TOOL-aOrientedCast-16 builder's 161 records carry 56 message ids, and
  summing every record overstates its output by 1141 tokens. The last, largest value per id is the
  response's count, the rule the run-log extractor applies per request id.

The spawn guard admits an `Agent` call only when line 1 of its prompt is the handoff's marker line
(`tools/hooks/agent-cap.js:2125`), so that line identifies a direct spawn's call exactly.

### The verb

`handoff.py agents` is a subparser beside `roster` (`tools/roles/handoff.py:493`), dispatched in
`main` (`:476`) after the `MEMORY_ROOT` and `CHARTER` reads, so both are required.
`print_agent_lines` sits beside `print_roster` (`:430`).

- `--handoff <path>` and `--run <run-id>` form a required mutually exclusive group. A relative
  `--handoff` is read from the repository root, as `check` reads its file.
- **The session.** `--session <file>` when given; else `CLAUDE_CODE_SESSION_ID`, which must be a
  lowercase UUID before it reaches a path, globbed as `<root>/*/<id>.jsonl` under
  `$CLAUDE_CONFIG_DIR/projects`, else `.claude/projects` under `USERPROFILE` on Windows and `HOME`
  elsewhere, the largest hit winning. That is the run-log kit's rule (`resolve_projects_root` and
  `resolve_session_tree`, `tools/runlog/extract.py:185`, `:266`, `:284`), spelled again in
  `resolve_session_file` because a kit file may not import a sibling; its comment names that kit in
  words, never by path.
- **The session's calls.** `load_session_calls` reads the session file once, line by line,
  JSON-parsing only a line whose bytes carry `"Agent"`, `"Workflow"`, `toolUseResult` or
  `task-notification`. Measured on this session's 11 MB file: 898 of 4654 lines parsed, 0.08 s. A
  line that does not parse is counted and named once on stderr. It returns each call's id, name,
  input and `toolUseResult`, and each notification's tool-use id and status.
- **`--handoff`.** The file's one `MARKER_RE` line (`:75`) is the key; none refuses. Every `Agent`
  call whose prompt's first line equals it byte for byte, and whose result carries an `agentId`, is
  one agent, in call order; none refuses, naming the handoff and the session file.
- **`--run`.** The journal under the session dir names the agents, one per `started` entry in
  journal order; no journal refuses. Zero `started` entries prints nothing, exits 0 and says on
  stderr that the run has started no agent yet. The `Workflow` call whose result's `runId` matches
  supplies the prompt link and the ledger's build; none leaves the link `unknown`, with a note, and
  the build to the session card (§4 "The ledger").
- A run id or agent id reaches a path only when it matches `^[A-Za-z0-9_-]{1,64}$`.
- **Returned.** A direct spawn has returned when any notification in the session file names its
  call's id, delivered or still queued, since either means the agent has finished, or when its
  call's own result has `status` `completed`. A harness agent has returned when its journal holds a
  `result` or `failed` entry for it.
- Output is UTF-8 through `sys.stdout.buffer`, as `print_roster` writes it. Every note is one
  `handoff: note — ` line on stderr.

Exits: 0 printed, notes or none; 1 on a refusal above, a missing definition, an underived
placeholder, or two ledgers in one build; 2 with no repository, `MEMORY_ROOT`, `CHARTER`, session
file or `.claude/roles.json`, the last because no line can name a write class without the role index
the hooks enforce.

### The fields

| Placeholder | Value | When nothing answers |
|---|---|---|
| `role` | the meta's `agentType`; else, for a direct spawn, the marker's `role` | `unknown` |
| `level` | the `effort` of the agent transcript's last `assistant` record carrying one; else the `effort:` line of `.claude/agents/<role>.md` | `unknown` |
| `model` | the `message.model` of its last `assistant` record; else, for a direct spawn, the call's `resolvedModel` | `unknown` |
| `unit-id\|label` | a direct spawn: the marker's `unit`, or the meta's `description` when the unit is `-`; a harness agent: the first `[A-Z]+-[A-Za-z]+-[0-9]+` in its journal `label`, else that label, else the meta's `description` | `unknown` |
| `name`, `path` | a direct spawn: the handoff's file name and the marker's `path`; a harness agent: the `Workflow` call's `args.briefPath` when it names a file in the repository, else its `scriptPath` made repository-relative | `unknown` |
| `class` | the role index's `writes` for the role; `none` for a type the index does not hold | none |
| `legs\|none` | the role index's `gates` list for the role joined by `, `; `none` when empty or not held | none |
| `run-id\|direct` | the run id; `direct` for a direct spawn | none |
| `agent-id` | the call's `agentId`, or the journal's | none |
| `outcome` | §4 "Outcome, wall and tokens" | none |
| `wall` | from the agent transcript's first `timestamp` to its last | `unknown` |
| `tokens` | the sum over its distinct `message.id` values of the largest `output_tokens` | `unknown` |

- `args` is read as an object or as a JSON string holding one, as the spawn guard reads it
  (`extractWorkflowArgs`, `tools/hooks/agent-cap.js:2029`).
- `none` for a type the index does not hold is what the hooks enforce on one: the write gate refuses
  its spec and product writes (`tools/hooks/scratch-guard.js:96-97`) and the gate arm admits it no
  leg (`:1415`).
- The role index is `INDEX_REL` and the agent types `AGENTS_REL` (`tools/roles/render_agents.py:65-66`).
  An agent type's `effort:` line is read inside `lib.FRONT_MATTER_RE`'s block by
  `^effort:[ \t]*(\S+)$`, since `parse_front_matter` refuses the rendered type's own keys.
- A value is joined into the line with each ` · ` replaced by `, ` and each line break by a space, so
  no value can add a field.
- **Observed first, declared second.** The transcript's `effort` and `model` are what the agent ran
  at; the agent type's line and `resolvedModel` are what it was given. The declared values answer at
  dispatch, before the agent's first reply exists (§8 F1).

### Outcome, wall and tokens

`render_outcome` takes the first that applies:

1. a journal `failed` entry: `failed`; a notification whose status is not `completed`: that status;
2. a journal `result` holding a boolean `committed`: `committed <sha>` when it is true and `sha` is
   a string, else `not committed`. That is the unit harness's result, which the `/build` Skill
   already reads by the same key (`tools/roles/SKILL.template.md:65`);
3. otherwise `wrote <n> files`, `wrote 1 file` for one: the distinct `file_path` values of the agent
   transcript's `Write`, `Edit`, `MultiEdit` and `NotebookEdit` tool uses.

`render_wall` prints `<s>s` under a minute, `<m>m<ss>s` under an hour and `<h>h<mm>m` beyond, as
`45s`, `7m47s` and `1h02m`. `render_tokens` prints a count under 1000 as is and one at or above it in
thousands to one decimal, as `812` and `41.2k`; the shape supplies ` out`.

### Reading the shapes

`roles_lib.extract_microformat_shapes(text)` returns `{head: definition}` for every line between the
first `<!-- microformats -->` and the `<!-- /microformats -->` after it that matches ``^- `(.*)`$``,
keyed by the text before the first ` — `: the selector both `format-guard.js` and the run-log prose
reader use. A missing pair returns `{}`. The library's docstring gains the fence among what it reads.

`render_shape_line(definition, fields)` replaces each `<name>` by `fields[name]` and prefixes `- `.
A name the dict does not hold refuses: `the governing doc's <head> shape names <name>, a field
handoff.py agents does not derive`. No head missing from the dict is guessed: `agent` or `returned`
absent refuses, naming it and the charter path. The definitions carry no `[ · …]` group, and one
that did would refuse as an underived name.

### The ledger

One file per build, under `<MEMORY_ROOT>/builds/<build>/build/`.

- **The build.** A direct spawn's is the marker's `build`. A harness run's is the `Workflow` call's
  `args.slug` when it matches `SLUG_RE` (`handoff.py:71`), else the `- build: <slug>` line under the
  session card's last `## route`, through `resolve_card_path` and `extract_card_section` (`:196`,
  `:93`). No build, or no folder for it, writes nothing and says why.
- **The name.** An existing `*-agent-ledger.md` in that folder is the ledger, and two refuse. Else
  it is created as `<today>-build-<id>-agent-ledger.md`, `<id>` being the first of the Serves ids.
  That name is check 5's grammar with its optional tail
  (`tools/memory-tree/check-memory-hygiene.sh:495`, `:882`), and it carries a family-qualified id
  its own Serves line lists, which check 21 requires of a bound record (`:1411`, `:1468-1474`).
- **The head.** `# <build> — agent ledger`, a blank line, `**Serves:** journal <ids>`, a blank line,
  and one sentence: "Generated by the roles kit's `handoff.py agents`: one line per agent dispatch
  and return, each added once and never edited." The ids are every unit id a spec under the build's
  `spec/`, at any depth, defines on its first line, `^# ([A-Z]+-<build>-[0-9]+) — `, sorted by family
  and then number, so every id resolves (check 21's `B` rows). The Serves line is re-derived on every
  write; no spec yet writes nothing and says so.
- **The lines.** A printed line is added when no line of the file has its head and its last field,
  the `run <run>/<agent>` token, and when none of its fields is `unknown`. A line held back because
  of `unknown` is added by a later run, at the agent's return at the latest. In the ledger the prompt
  link's target is re-rooted at the ledger's folder, so `../prompts/<file>.md`, because check 2
  resolves a markdown link from the file holding it (`:621-677`); the rest is the printed line byte
  for byte.
- `write_agent_ledger` rewrites the file whole, UTF-8 with LF line ends, only when it changes, and
  prints `handoff: note — <path>: <n> line(s) added` on stderr.

### The `/build` Skill

A bullet after "You write no freeform agent prompt" (`tools/roles/SKILL.template.md:22-26`): every
agent the session dispatches or receives is reported by pasting, unchanged, what
`handoff.py agents --handoff <path>` prints for a direct spawn or `handoff.py agents --run <run-id>`
for a harness call, run once the call returns and again when its notification arrives; the same run
adds each complete line to the build's agent ledger. No stage heading moves, so the adopter's stage
check is untouched. The rendered `.claude/skills/build/SKILL.md` follows with `adopt-roles.sh --scaffold`.

### The suite arm

Arm 9 of `tools/roles/adopt-roles.test.sh`, after arm 8, on `build_fixture` (`:56`). It writes
the build folder and session S of §6 into the fixture with `"$PY"`, then asserts:

1. the fixture scaffolds and checks clean, as every arm opens;
2. `handoff.py agents --handoff <the fixture handoff> --session <S>` exits 0 and prints AC1's two
   lines exactly;
3. after a second identical run, the fixture's one `*-agent-ledger.md` holds each line exactly once.

The header's arm list gains the arm, and `FLOOR_ASSERTIONS` (`:52`) rises from 16 to 19 with a
comment naming this unit. Gov's charter is the fixture's charter, so the arm needs
`PLAY-aOrientedCast-3`'s shapes in gov's `AGENTS.md`.

### The suite's location probes

The leg `shell hygiene (a location probe asked from a moved directory)` flags
`tools/roles/adopt-roles.test.sh:29-30` at `1e89fa5cd`: `REPO=$(git -C "$HERE" rev-parse --show-toplevel …)`
and `KREL=$(git -C "$HERE" rev-parse --show-prefix …)` are asked bare. With `GIT_DIR` exported and
no `GIT_WORK_TREE`, as git exports it into a linked worktree's hooks, git takes `$HERE` itself for
the top of the work tree, so the toplevel reads as the kit's own directory and the prefix as empty
(`tools/gate-lint/sh_hygiene.py:22-28`). The one scrub the scanner accepts is the probe as the FIRST
command of a substitution opening `(unset GIT_DIR GIT_WORK_TREE;` (`PROBE_SCRUB` and `SCRUBBED`,
`:189-190`); a top-level `unset`, the other variable order or a third variable still grade bare
(`:1133-1134`). So each line becomes `$(unset GIT_DIR GIT_WORK_TREE; git -C "$HERE" rev-parse …)`,
the spelling `TOOL-aHeardState-8` gave the format-guard suite (`tools/hooks/format-guard.test.sh:19`),
with the rest of each line unchanged. No registry row is written: a waiver would keep a probe that a
scrub corrects. Arm 9 asks git nothing about its own location; any probe it adds takes the same scrub.

### Documentation

- `handoff.py`'s docstring: the usage line, one paragraph on the verb, the exits, and, under WHAT THIS
  DOES NOT CHECK, that the transcript format is not a contract; that an `effort` or a `model` is
  read, not proved to be what the API applied; that a file written through Bash is not counted; that
  a session it reads may not be the one the build ran in; and that a ledger line edited by hand
  passes.
- `tools/roles/README.md`: a section "The agent lines" after "The handoff renderer", holding the
  verb, the field table, the ledger and the exits.
- `help/roles.md`: a section "What each agent line tells you": the two lines field by field in plain
  words, that the main loop pastes them from `handoff.py agents`, that `unknown` means nothing has
  recorded that field yet, and where the ledger lives.
- `memory/map/features/roles.md`: `TOOL-aOrientedCast-20` joins `decisions`, and its prose gains a
  sentence on the verb and the ledger.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `agents`, `--handoff`, `--run`, `--session` | `handoff.py` verb and flags | none: a CLI verb carries no naming cell |
| `print_agent_lines`, `resolve_session_file`, `load_session_calls`, `load_agent_transcript`, `load_run_journal`, `render_shape_line`, `render_outcome`, `render_wall`, `render_tokens`, `write_agent_ledger` | functions in `handoff.py` | `py.function`; `lexicon.py --suggest <name> --as py.function` answered OK for each |
| `extract_microformat_shapes` | function in `roles_lib.py` | `py.function`, answered OK |
| `LEDGER_TAIL` = `"-agent-ledger.md"`, `UNKNOWN` = `"unknown"`, `WRITE_TOOLS` | constants in `handoff.py` | none: `py.constant` is undeclared |
| `<build>/build/<date>-build-<id>-agent-ledger.md` | a generated record | hygiene checks 5 and 21 |

### Files touched (estimate)

`tools/roles/handoff.py`
`tools/roles/roles_lib.py`
`tools/roles/README.md`
`tools/roles/SKILL.template.md`
`tools/roles/adopt-roles.test.sh`
`.claude/skills/build/SKILL.md`
`help/roles.md`
`memory/map/features/roles.md`
`memory/map/generated/`

### Rollout

- The roles kit moves from 1.2 to 1.3, the set's one move, as `TOOL-aOrientedCast-17` §4 "Rollout"
  states the rule; `TOOL-aOrientedCast-19`'s rev-2 handed the move here. Its carriers:
  `KIT_ROLES_VERSION` at `tools/roles/roles_lib.py:20`, which `tools/roles/kit.toml:22` reads; the
  `gov:kit roles@` markers at `tools/roles/README.md:1` and `tools/roles/SKILL.template.md:5`; and the
  rendered `.claude/skills/build/SKILL.md:5`. `tools/check-kit-versions.sh:387-393` pairs the
  constant with the README's marker.
- The pass re-renders the Skill with `bash tools/roles/adopt-roles.sh --scaffold` and the map with
  `python tools/codebase-map/gen_map.py --write`. The kickoff manifest's `watch:` list holds none of
  these files, so no `last-audit` re-stamp is owed.
- Adopters receive the verb at `govkit update`. The verb creates gov's own ledger the first time the
  main loop runs it, as a record of the session, not as part of this unit's commit. Rollback is a
  revert of the unit's commit and a re-render.

### Alternatives rejected

- Finding a direct spawn by scanning subagent transcripts for the marker instead of the session's
  `Agent` calls: it needs no 11 MB read, but loses `resolvedModel`, the notification and the
  foreground status, so a dispatch-time line could not carry a model and a killed agent would never
  return.
- A ledger in a generated region of the build README, a non-markdown file, or one per unit: §8 F4.
- Reading effort from the policy file instead of the agent type: the agent type's line is what
  Claude Code applied when the render is stale, and the brief names it.

## 5. Production-readiness checklist

- security — Reads files under the user's Claude projects folder, the repository's role index and
  agent types; writes one file under the build's `build/` folder. A session id, run id and agent id
  are shape-checked before any path sees them, and no prompt, message or tool text is printed or
  kept. A line carries ids, a model and a repository-relative path, never a secret. Claude Code's
  `Agent` result asks the main loop not to quote an agent id to the user; the owner's addendum asks
  for it, and this unit follows the owner.
- perf / scale — one prefiltered pass over the session file, 0.08 s on an 11 MB file, and one read
  per agent transcript and journal.
- error / empty / loading states — a run with no agent yet prints nothing and says so; a field
  nothing answers prints `unknown` and stays out of the ledger; a missing session, index, charter or
  shape refuses by name (§4 "The verb").
- observability — every note names its field, file or reason; the ledger note names its count.
- risks — the transcript format can change under a CLI update, and the arm's fixture would not see
  it: a renamed field reads as `unknown`, visible on the line. Two worktrees adding to one ledger
  conflict at their merge and reconcile additively. A run resumed in another session has no
  `Workflow` call here, so its prompt link is `unknown` and its build comes from the session card.
- testing — the fixture probes of §6 in the pass; arm 9, observed RED first at the close.
- migration — none; rollback is a revert.
- user docs — `help/roles.md` (S7).

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag. Each runs the unit's own verb on a
fixture, or reads a file.

Fixture T is a git repository under a short `%TEMP%` root holding a copy of `tools/roles/` at
`tools/roles`; a `.memory-tree.conf` declaring `MEMORY_ROOT=memory` and `CHARTER=AGENTS.md`; a copy
of gov's `AGENTS.md`, `.claude/roles.json` and `.claude/agents/`; and the build folder
`memory/builds/tFix` holding a spec whose first line is `# TOOL-tFix-1 — t` and the handoff H,
`prompts/2026-10-13-prompt-TOOL-tFix-1-1-builder.md`, whose one marker line names role `gov-builder`,
build `tFix`, unit `TOOL-tFix-1` and its own path. Session S is
`projects/p/11111111-1111-4111-8111-111111111111.jsonl` under the run's scratch path, with this tree:

| File | Records |
|---|---|
| the session file | an `Agent` call `toolu_A` whose prompt's first line is H's marker, its result `{"status": "async_launched", "agentId": "a0000000000000001", "resolvedModel": "claude-test-1"}`; a `Workflow` call `toolu_W` with `scriptPath` `tools/workflows/unattended-unit.js` and `args` `{"slug": "tFix", "briefPath": <H's path>}`, its result `{"runId": "wf_00000001-aaa"}`; a `task-notification` user record for `toolu_A` with status `completed` |
| `subagents/agent-a0000000000000001.jsonl` | a user record at `10:00:00`; `assistant` records with model `claude-test-1` and effort `medium`: two sharing message id `m1` with output tokens 300 then 700, one `m2` with 900, holding `Write` uses on two paths and an `Edit` on one of them; the last at `10:07:47` |
| its `.meta.json` | `{"agentType": "gov-builder", "description": "build one"}` |
| `subagents/workflows/wf_00000001-aaa/journal.jsonl` | `started` for `a0000000000000002` labelled `unit:TOOL-tFix-1`; its `result` `{"committed": true, "sha": "abc123def"}`; `started` for `a0000000000000003` labelled `commit:specs:tFix` |
| `…/agent-a0000000000000002.jsonl` and meta | records with model `claude-test-2`, effort `xhigh`, 1500 output tokens, 45 s apart; `{"agentType": "gov-builder"}` |
| `…/agent-a0000000000000003.jsonl` and meta | one record with model `claude-test-2`, effort `high`; `{"agentType": "workflow-subagent"}` |

The verb runs from T's root as `python tools/roles/handoff.py agents … --session <S>`. Every staged
break is restored before the next.

- **AC1** — When `handoff.py agents --handoff <H> --session <S>` runs, it exits 0 and prints exactly
  `- agent — gov-builder · effort medium · model claude-test-1 · TOOL-tFix-1 · prompt [<H's name>](<H's path>) · writes product · gates lexicon naming predicates · run direct/a0000000000000001`
  and `- returned — gov-builder · wrote 2 files · 7m47s · 1.6k out · run direct/a0000000000000001`.
  Red when: the effort is the agent type's `high` although the transcript says `medium`, the tokens
  read `1.9k` because every record was summed, a file is counted twice, or a field is out of place.
- **AC2** — When `handoff.py agents --run wf_00000001-aaa --session <S>` runs, it exits 0 and prints
  three lines: `a0000000000000002`'s `agent` line with `effort xhigh`, `model claude-test-2`,
  `TOOL-tFix-1`, H's link, `writes product` and `run wf_00000001-aaa/a0000000000000002`; its
  `returned` line `- returned — gov-builder · committed abc123def · 45s · 1.5k out · run wf_00000001-aaa/a0000000000000002`;
  and `a0000000000000003`'s `agent` line with `commit:specs:tFix`, `writes none · gates none` and no
  `returned` line.
  Red when: the unit is not read from the label, an unindexed type gets a class or a leg, or an agent
  with no result is reported as returned.
- **AC3** — When S's direct transcript keeps only its user record and the notification is deleted,
  `handoff.py agents --handoff <H> --session <S>` prints one `agent` line with `effort high`, from
  `.claude/agents/gov-builder.md`, and `model claude-test-1`, and no `returned` line. With
  `resolvedModel` also deleted, the line reads `model unknown`, stderr names `model`, and the
  ledger gains no line for the agent.
  Red when: a dispatch-time line refuses for want of a reply, invents a value, or is added to the
  ledger while it holds `unknown`.
- **AC4** — When T's `AGENTS.md` loses its `agent` definition, the AC1 command exits 1 naming
  `agent`; restored and given a `<colour>` field instead, it exits 1 naming `colour`.
  Red when: a line is printed from a guessed or partial shape.
- **AC5** — After AC1's run, `memory/builds/tFix/build/` holds one file whose name ends in
  `-build-TOOL-tFix-1-agent-ledger.md`, whose third line is `**Serves:** journal TOOL-tFix-1`, and
  which holds AC1's two lines once each, the link reading `../prompts/<H's name>`. A second AC1 run
  leaves `git hash-object` of the file unchanged, and AC2's run then adds its three lines.
  Red when: a rerun adds a line twice, a link resolves from the repository root inside the file, or
  the name or the Serves line falls outside checks 5 and 21.
- **AC6** — When each break below is staged, the AC1 command answers as stated: H without its marker
  line exits 1; no `Agent` call carrying H's marker exits 1 naming H; `--run wf_00000009-zzz` exits 1
  naming its journal; `--session` dropped with `CLAUDE_CODE_SESSION_ID` unset exits 2; T's
  `.claude/roles.json` removed exits 2; a second `*-agent-ledger.md` in the build folder exits 1
  naming both; and T's spec removed exits 0, prints the lines, writes no ledger and says why.
  Red when: a refusal prints a line, or a missing input reads as an empty one.
- **AC7** — When the main loop runs `python tools/roles/handoff.py agents --run <this unit's own unit-harness run id>`
  in the session that dispatched it, it exits 0 and prints the builder's `agent` and `returned`
  lines, and gov's `memory/builds/aOrientedCast/build/` gains its agent ledger holding them.
  Red when: a live transcript yields `unknown` where S yields a value.
  fixture: the live session, which only the node that ran the build holds; observed at the close.
- **AC8** — When `grep -c "handoff.py agents" tools/roles/SKILL.template.md` prints at least 1, and
  `bash tools/roles/adopt-roles.sh --scaffold` then leaves `git diff --quiet -- .claude/skills/build/SKILL.md`
  at exit 0, the committed Skill names the verb and equals a fresh render.
  Red when: the Skill never names the verb, or its render is stale.
- **AC9** — When `grep -c '^KIT_ROLES_VERSION = "1.3"' tools/roles/roles_lib.py` runs it prints 1,
  `grep -c "gov:kit roles@1.3" tools/roles/README.md tools/roles/SKILL.template.md .claude/skills/build/SKILL.md`
  prints 1 for each file, and `grep -rl "gov:kit roles@1.2" tools/roles .claude/skills/build` prints
  nothing.
  Red when: the constant or one carrier does not move.
  figure: PINNED at `1e89fa5cd`, where the kit reads 1.2.
- **AC10** — When `grep -n "## What each agent line tells you\|handoff.py agents\|agent-ledger\|unknown" help/roles.md`
  runs, it shows the section, the verb, the ledger's name and the meaning of `unknown`.
  Red when: the page omits the section, the verb, the ledger or `unknown`.
- **AC11** — When
  `python -c "import sys; sys.path.insert(0, 'tools/gate-lint'); import sh_hygiene as s; r = s.scan_probe_file(open(sys.argv[1], encoding='utf-8').read()); print(len(r['bare']), sorted(k for _, k, _ in r['scrubbed']))" tools/roles/adopt-roles.test.sh`
  runs on the unit's commit, it prints `0` and two scrubbed keys, one ending `--show-prefix` and one
  ending `--show-toplevel`; and `grep -c "=\$(unset GIT_DIR GIT_WORK_TREE; git -C" tools/roles/adopt-roles.test.sh`
  prints 2.
  Red when: either probe is still asked bare, or its scrub sits anywhere but first in its
  substitution, which the scanner grades bare.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `shell hygiene (a location probe asked from a moved directory)` · `govkit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC5 · arm 9, against a `handoff.py` whose per-message-id maximum is staged to a per-record sum, so the returned line reads `1.9k out` · `FLOOR_ASSERTIONS` raised from 16 to 19

The main loop observes the arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

- **F1 — Where does a line's effort come from?**
  (a) The agent transcript's `effort` field when present, else the agent type's `effort:` line;
  (b) the agent type's line, or `handoff.py stage-efforts`, as the brief states, never the transcript.
  (b) rests on the addendum's reading that no file records effort, which the transcripts sampled on
  2026-10-13 contradict. It also cannot place a harness agent's stage override, since a journal names
  no stage key, and `TOOL-aOrientedCast-10` §4 records that the CLI silently lowers `xhigh` and `max`
  for a model that lacks them, so a declared level can differ from the level that ran. (a) reports
  what ran and still answers at dispatch from the declared line.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The fields" states it.
- **F2 — Which code reads the transcripts?**
  (a) The roles kit, spelling the run-log kit's session-resolution rule again; (b) a new mode of the
  run-log kit's extractor, called by the verb through the inline kit resolver; (c) the verb itself in
  the run-log kit. (c) contradicts the brief's roles-kit verb: M3 veto 1. (b) widens the write set to
  a second kit and its version, and the extractor keeps no per-agent rows and drops prompt text the
  marker join needs. (a) costs about 15 lines spelled twice, named in the comment.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a).
- **F3 — What does a `returned` line say the agent produced?**
  (a) Only its status: done, failed or killed; (b) the status when it is not success, the unit
  harness's commit verdict, else the files it wrote; (c) every key of a harness result, rendered
  generically. (c) couples the line to every harness's result schema and grows without bound. (a)
  says nothing about what it produced, which the owner asked for. (b) reads one key the kit's Skill
  already reads and one count every transcript holds.
  Recommendation: (b).
  RESOLVED (agent, 2026-10-13, delegated): (b), as §4 "Outcome, wall and tokens" states it.
- **F4 — Where does the per-build ledger live?**
  (a) A dated record under the build's `build/` folder, named for the build's first specced unit and
  serving every one; (b) a generated region of the build README; (c) a non-markdown file under
  `build/`; (d) one ledger per unit. (b) puts a second writer into regions the build-index generator
  owns and check 9 compares. (c) is still a record check 21 grades, needs the same name, and drops
  the link. (d) contradicts the owner's per-build answer: veto 1.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The ledger" states it.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.
- rev-2 · 2026-10-13 · S9 · AC11 · §4 · §7 · the location-probe leg flags the two bare probes at
  `tools/roles/adopt-roles.test.sh:29-30`, a file this unit already edits: S9 and §4 "The suite's
  location probes" scrub both as the scanner accepts, AC11 observes it through the scanner's own
  `scan_probe_file`, and §7 names the leg.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read a Claude Code session transcript and its subagent
workflow journal to report each agent's model, usage and timestamps"` ranked the run-log kit's
`resolve_session_tree`, `extract_session` and `build_usage` (`tools/runlog/extract.py`) and its
`read_journal`, and the roles library's `load_workflows` and `read_conf_key`. The run-log extractor
is the nearest seam, and a kit may not import it, so §8 F2 ports its session rule and its per-request
usage rule and names both. The seams this unit extends are `handoff.py`'s verb dispatch beside
`print_roster` (`tools/roles/handoff.py:430-493`), its marker grammar and card readers, the roles
library's governing-doc reading (`tools/roles/roles_lib.py:110-150`), the role index and agent types
`render_agents.py` writes, and the micro-format fence that `format-guard.js` and the run-log prose
reader already key on. The recall probe surfaced the addendum's record, the brief and
`TOOL-aOrientedCast-10`'s effort evidence, read against source; the record's "no file records
effort" is stale on 2.1.295, and §8 F1 follows the measurement.

Recall terms used: `agent transcript journal workflow subagent usage effort model ledger format-guard microformat runlog`
