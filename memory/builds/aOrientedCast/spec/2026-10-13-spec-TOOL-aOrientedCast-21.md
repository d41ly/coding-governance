# TOOL-aOrientedCast-21 — format-guard refuses a final message that omits an agent line for an agent its turn dispatched or received

**Status:** CLOSED · rev-1 · 2026-10-13 · node a · Tier-2 · base 646d4a73 · streams tooling · order 23

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md](../build/2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-22 TOOL-aOrientedCast-23 |
| [2026-10-13-build-TOOL-aOrientedCast-21-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aOrientedCast-21-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-build-TOOL-aOrientedCast-25-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aOrientedCast-25-1-acceptance-ledger.md) | journal | TOOL-aOrientedCast-25 TOOL-aOrientedCast-22 |
| [2026-10-13-prompt-TOOL-aOrientedCast-20-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-20-1-spec-brief.md) | journal | TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 |
| [2026-10-13-review-TOOL-aOrientedCast-16-closing-diff-round1.md](../reviews/2026-10-13-review-TOOL-aOrientedCast-16-closing-diff-round1.md) | diff-review | TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-22 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's third addendum makes the `agent` and `returned` lines mandatory and asks that the Stop
hook `format-guard` be extended to refuse a final message that omits them. The hook already grades
the BUILD/SPEC pair and the commit lines of a session routed to a live build. This unit adds one arm:
it reads the turn from the transcript the Stop payload names, finds every agent the turn dispatched
or received, and refuses a final message missing a bare line for one, with the shapes read from the
charter's fence as the hook reads its others.

## 2. Scope (IN)

- **S1** — `scanTurnRecords` reads the payload's `transcript_path` and returns the final turn's
  records under §4 "The turn". Observed by AC1, AC4 and AC5.
- **S2** — `extractTurnAgents` derives the required lines from those records, under §4 "What the
  turn requires": an `agent` line per agent dispatched and a `returned` line per agent received,
  a harness run's agents read from its journal by `readJournalAgents`. Observed by AC1 to AC4.
- **S3** — `checkAgentLines` reports one defect per required line no bare line meets, and the block
  reason lists them with the `agent` and `returned` definitions and the route naming
  `handoff.py agents`. Observed by AC1, AC2 and AC3.
- **S4** — `readCharterShapes` keeps requiring its four heads and reads `agent` and `returned` when
  the fence holds them. Absent, the arm requires nothing and writes one witness line when the turn
  holds an agent. Observed by AC6.
- **S5** — Every unreadable input of the arm allows with one witness line, under §4 "Degraded
  inputs", and the suite's payload builder names an empty transcript by default. Observed by AC5.
- **S6** — `tools/hooks/format-guard.test.sh` gains the arms of §4 "The suite arms" and its
  `FLOOR_ASSERTIONS` rises by their count. Observed by AC1 to AC6, whose breaks the arms stage.
- **S7** — The prose follows: the hook's header, the hooks README's format-guard section, one
  bullet under "What the hooks refuse" in `help/roles.md`, and the agent-cap dossier. Observed by
  AC8 for the help page; the rest is NOT OBSERVED: prose, read by the closing review.
- **S8** — The hooks kit moves from 1.35 to 1.36 with every carrier. Observed by AC9.

## 3. Non-goals (OUT)

- A second Stop hook, or any new wiring: the arm lives in `format-guard.js` and rides its fragment.
- Grading a session the hook does not arm for. The arm runs only where the pair arm runs: a session
  whose card routes a build `LIVE.md` lists, as the header's WHEN IT ARMS states
  (`tools/hooks/format-guard.js:16-19`).
- Grading a line's field values. A well-formed line naming the right agent with a wrong model passes;
  the values are the verb's to derive.
- Reading the agent ledger (§8 F1), and any edit to the roles kit, whose verb this hook names only
  by its bare file name.
- Mirroring the arm in the run-log kit's prose reader, whose parity arm compares pair verdicts only.
- Grading an agent a sub-agent spawned: a sub-agent's stop carries `agent_id`, which the hook skips.

### Edges

- **consumes-from** `PLAY-aOrientedCast-3` — the `agent` and `returned` definitions in the
  micro-format fence of `AGENTS.md`. Without them the arm requires nothing, and AC1 to AC4 cannot red.
- **consumes-from** `TOOL-aOrientedCast-20` — `handoff.py agents`, the route the refusal names, and
  the run field every line ends with, `/<agent-id>` after the run, by which the arm matches an agent.

## 4. Design

Line numbers were read at `1e89fa5cd` on 2026-10-13.

### Evidence — what the main transcript records

Measured on this build's session, Claude Code 2.1.295, 4654 records in 11 MB, and on the forty most
recent sessions of node a. The format is no contract; each fact is a reading.

| Event | Record |
|---|---|
| an `Agent` or `Workflow` call | an `assistant` record holding a `tool_use` block with that `name`, its `id` and `input` |
| its result | a `user` record holding a `tool_result` block whose `tool_use_id` is that id, and a top-level `toolUseResult` |
| a background `Agent` spawn | `toolUseResult.status` `async_launched`, with `agentId` |
| a foreground `Agent` call | `toolUseResult.status` `completed`, with `agentId` |
| a `Workflow` call | `toolUseResult.runId`, `status` `async_launched` when it runs in the background |
| a delivered notification | a `user` record whose `origin.kind` is `task-notification` (80 here), or an `attachment` record of type `queued_command` whose `prompt` carries one (7), each holding `<tool-use-id>` and `<status>` |
| a queued notification | `queue-operation` records, `enqueue` (139) and `remove` (59): not a delivery |
| a harness run's agents | `<session dir>/subagents/workflows/<run id>/journal.jsonl`: `started`, `result` and `failed` entries, each with `agentId` |

`<session dir>` is `transcript_path` without `.jsonl`. The run-log prose reader opens a TURN at
any main-file `user` record carrying typed text, and treats back-to-back openers as one turn
(`tools/runlog/prose.py:5-8`, `:121-149`); typed text is a string content, or text blocks with no
`tool_result` block (`tools/runlog/extract.py:566-584`). This arm uses the same rule.

### The turn

`scanTurnRecords(transcriptPath)` reads the file once and walks its lines from the end, parsing each
until it passes the turn's opener: the earliest of the last run of consecutive typed `user` records.
It returns the turn's records in file order. A line that does not parse is skipped and counted.

### What the turn requires

`extractTurnAgents(turn, transcriptText, sessionDir)` returns `{ head, agentId, why }` items:

| In the turn | Required |
|---|---|
| an `Agent` call whose result carries an `agentId` | `agent` for it; `returned` too when the result's `status` is `completed` |
| a `Workflow` call whose result carries a `runId` | `agent` for every `started` entry its journal holds at this stop; when the result's `status` is not `async_launched`, also `returned` for every `result` or `failed` entry |
| a delivered notification whose `<tool-use-id>` is an `Agent` call | `returned` for that call's `agentId` |
| a delivered notification whose `<tool-use-id>` is a `Workflow` call | `agent` for every `started` entry of its run's journal, and `returned` for every `result` or `failed` entry |

A notification's call can sit in an earlier turn. Its result is found by scanning the transcript's
raw lines for one carrying both the tool-use id and `toolUseResult`, and parsing only that line. A
tool-use id naming any other tool, such as a background `Bash`, requires nothing. The same
`(head, agentId)` pair is required once however many routes reach it.

`readJournalAgents(sessionDir, runId)` reads `<sessionDir>/subagents/workflows/<runId>/journal.jsonl`.
The run id must match `^[A-Za-z0-9_-]{1,64}$`, and the path is built from it, never from the
result's own `transcriptDir`, so the arm reads nothing outside the session's directory.

### Meeting a requirement

`checkAgentLines(rows, shapes, required)` reads the rows `scanMessageLines` already returns
(`tools/hooks/format-guard.js:173`). A required pair is met by a row that is not fenced, starts with
`- <head> — `, matches that head's derived shape, and whose text after its last ` · ` ends with
`/<agentId>`. Otherwise it is one defect:

- no row carries `/<agentId>` under that head: `no <head> line for agent <id>, which this turn <dispatched|received>`;
- a row carries it and is not bare: `the <head> line for agent <id> is not a bare list item at column 0 (rule r1)`;
- a bare row carries it off its shape: `the <head> line for agent <id> does not match its charter shape`.

The defects join the pair and commit defects in one refusal. `renderBlockReason` (`:236`) quotes the
`agent` and `returned` definitions after its three when any agent defect is present, and adds one
sentence: for each agent, paste unchanged the lines `handoff.py agents --handoff <path>` or
`handoff.py agents --run <run-id>` prints. The hook names that script by its bare file name only, as
the spawn guard names the renderer (`tools/hooks/agent-cap.js:2037-2039`).

### The shapes

`readCharterShapes` (`:147-166`) keeps its required four (`:162`) and refuses nothing new. The arm
runs when the returned shapes hold `agent` and `returned`. When either is absent and the turn holds
at least one requirement, it writes `format-guard: this turn dispatched or received <n> agent(s), and
AGENTS.md's micro-format fence defines no <head> shape, so no agent line is required`, which is the
state of every charter rendered from a template before v4.4 and of every target without the roles kit.

### Degraded inputs

Each allows the arm's part of the stop and writes one witness line naming its input; the pair and
commit arms are unaffected. The payload carries no `transcript_path`; the transcript cannot be read;
a run id fails its shape; a journal cannot be read. A parse failure inside the turn is counted into
one witness line. Every witness is one entry of `checkStop`'s existing `witnesses` list (`:249-297`),
so two degraded inputs in one stop write two lines.

### The bound and the cost

The hook still refuses at most once per turn end: `stop_hook_active` returns before the arm. The
transcript is read once; the turn's lines are parsed from the end, and an earlier line only when its
raw text carries a notification's tool-use id. On this session's 11 MB file that is one read and a
few hundred parses. Every failure path allows, as the hook's header promises.

### The header and the reason

The header's WHAT BLOCKS list (`:27-39`) gains the arm; WHEN IT ARMS is unchanged; WHAT THIS DOES NOT
CHECK (`:44-53`) gains: a line's field values; an agent a sub-agent spawned; an agent a harness starts
after this stop; a notification queued but not yet delivered; and whether the transcript format still
holds, a renamed field reading as no agent at all.

### The suite arms

In `tools/hooks/format-guard.test.sh`, after the TOOL-aHeardState-8 block. `run_stop` (`:137-151`)
gains a default `transcript_path` naming an empty file under `$TMP`, so every existing arm runs
with a transcript and AC4's empty-stderr arm (`:206`) still holds. A helper writes a fixture
transcript under `$TMP/sess/<sid>.jsonl` and its session dir, built by `node` from JSON objects so no
byte crosses a shell quote. The fixture charter is gov's `AGENTS.md` (`:182-184`), which carries
both shapes once `PLAY-aOrientedCast-3` lands. The arms:

1. a turn whose `Agent` call returned `agentId` `a1`, and a message with the pair and no agent line,
   blocks; the reason names `a1` and `handoff.py agents`;
2. the same message with a bare `agent` line ending `run direct/a1` allows;
3. that line in backticks blocks, naming rule r1;
4. an `Agent` call in an earlier turn and a turn opened by its notification block without a bare
   `returned` line for `a1`, and allow with one; the earlier turn's dispatch requires no `agent` line;
5. a `Workflow` call whose journal holds `started` entries for `a2` and `a3`: both `agent` lines
   allow, and `a3`'s missing blocks naming `a3` alone;
6. a turn opened by that run's notification, the journal holding a `result` for `a2` and a `failed`
   for `a3`, requires all four lines;
7. the fixture charter's `agent` definition deleted: arm 1's message allows, with the witness naming
   `agent`;
8. a payload with no `transcript_path` allows with its witness, and a run id `../x` is never read.

`FLOOR_ASSERTIONS` (`:342`) rises by the arms' assertions, counted at build time, with a comment naming
this unit beside the earlier ones.

### Kit version

The hooks kit moves from 1.35 to 1.36, the last unit of the set to touch `tools/hooks/`. Its
carriers are `KIT_AGENT_CAP_VERSION` with its same-line marker at `tools/hooks/agent-cap.js:101`,
which `tools/hooks/kit.toml:6` reads, and the `gov:kit agent-cap@` markers at
`tools/hooks/format-guard.js:6` and `tools/hooks/scratch-guard.js:144`.
`tools/check-kit-versions.sh:195-220` compares every tracked `*.js` carrying the marker to the
constant.

### Documentation

- `tools/hooks/README.md`, its format-guard section (`:410`): "What blocks" gains the arm, a
  paragraph says how the turn and its agents are read, and "The ceiling" gains the header's new
  limits.
- `help/roles.md`, "What the hooks refuse" (`:46`): a bullet saying that in a session routed to a
  live build, a final message that leaves out the `agent` or `returned` line of an agent its turn
  dispatched or received is refused once, and that `handoff.py agents` prints the lines.
- `memory/map/features/agent-cap.md`: `TOOL-aOrientedCast-21` joins `decisions`, and its prose gains
  a sentence on the arm.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `scanTurnRecords`, `extractTurnAgents`, `readJournalAgents`, `checkAgentLines` | functions in `format-guard.js`, each added to `module.exports` | `js.function`; `lexicon.py --suggest <name> --as js.function` answered OK for each |
| `AGENT_HEADS` = `['agent', 'returned']`, `RUN_ID_RE` | constants in `format-guard.js` | none, as the file's existing constants |

### Files touched (estimate)

`tools/hooks/format-guard.js`
`tools/hooks/format-guard.test.sh`
`tools/hooks/agent-cap.js`
`tools/hooks/scratch-guard.js`
`tools/hooks/README.md`
`help/roles.md`
`memory/map/features/agent-cap.md`
`memory/map/generated/`

### Rollout

The pass runs `python tools/codebase-map/gen_map.py --write`, since four new functions stale the
map. Adopters receive the arm with the hooks kit at `govkit update`; a target whose charter lacks the
two shapes sees only the witness, and only in a turn that dispatched or received an agent. No
`watch:` path of the kickoff manifest moves. Rollback is a revert of the unit's commit.

### Alternatives rejected

- Grading every session rather than a routed one: it would refuse unrouted conversation, which the
  hook was built never to touch.
- Requiring a harness run's `agent` lines only at its dispatch: agents a background run starts after
  that stop would never be required, so a received run requires both lines for every agent (§8 F2).
- Counting a `queue-operation` enqueue as a delivery: a notification queued during one turn and
  delivered as the next turn's opener would be required twice, once before the main loop has it.

## 5. Production-readiness checklist

- security — Reads the transcript the harness names and files under its session directory only; a
  run id is shape-checked before it reaches a path, and the result's own `transcriptDir` is never
  followed. It writes nothing new, and the reason quotes no transcript text.
- perf / scale — one read of the transcript and a few hundred parses, on an 11 MB file; the journal
  reads are one per run the turn touched.
- error / empty / loading states — §4 "Degraded inputs": each allows with a witness; a turn with no
  agent requires nothing and writes nothing.
- observability — every witness names its input, and each defect names its agent id and head.
- risks — the transcript format may change under a CLI update; a renamed field reads as a turn with
  no agent, which is silent, and the header says so. A main loop that cannot run the verb is refused
  once and then allowed by the bound.
- testing — the suite arms of §4, observed RED first at the close.
- migration — none.
- user docs — `help/roles.md` (S7).

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag. Each feeds `node tools/hooks/format-guard.js`
a hand-built payload in a fixture repository, as the suite's arms do, and reads its stdout and
stderr. The fixture is the suite's own: a repository under a short `%TEMP%` root with a copy of
gov's `AGENTS.md`, a `LIVE.md` naming build `tBuild`, an orientation card routing it, and a
transcript T under `sess/` beside its session dir. "Blocks" means stdout holds
`{"decision":"block"…}`; "allows" means stdout is empty. Each staged break is restored before the
next.

- **AC1** — When T's last turn holds an `Agent` call whose result carries `agentId` `a1` and the
  final message holds the pair and no agent line, the hook blocks, and its reason names `a1`,
  `which this turn dispatched` and `handoff.py agents`. With a bare line
  `- agent — gov-builder · effort high · model m · TOOL-tBuild-1 · prompt [x.txt](x.txt) · writes product · gates none · run direct/a1`
  added, it allows.
  Red when: a dispatched agent with no line passes, or a correct line still blocks.
- **AC2** — When that line is wrapped in backticks, `node tools/hooks/format-guard.js` blocks and its
  reason carries `rule r1`; with its last field cut, it blocks and the reason carries
  `does not match its charter shape`.
  Red when: a non-bare or off-shape line meets the requirement.
- **AC3** — When T's last turn holds a `Workflow` call whose result carries `runId` `wf_t-1` and its
  journal holds `started` entries for `a2` and `a3`, a message with both `agent` lines allows, and one
  without `a3`'s blocks naming `a3` and not `a2`.
  Red when: a harness agent is not required, or one line satisfies two agents.
- **AC4** — When the `Agent` call sits in an earlier turn and the last turn opens with its
  notification, the hook blocks without a bare `returned` line ending `/a1` and allows with one, and
  no `agent` line for `a1` is required; when the last turn opens with the run's notification and the
  journal holds a `result` for `a2` and a `failed` for `a3`, it requires both `agent` and both
  `returned` lines.
  Red when: an earlier turn's dispatch is required again, a received agent is not required, or a
  received run's agents need only one head.
- **AC5** — When the payload carries no `transcript_path`, the hook allows and its stderr names
  `transcript_path`; when a `Workflow` result's `runId` is `../x`, it allows, its stderr names the
  run id, and no file outside the session dir is opened; when the suite's empty default transcript
  is named, AC4 of the existing suite still writes nothing to stderr.
  Red when: a degraded input blocks, reads outside the session dir, or allows without a witness.
- **AC6** — When the fixture charter's `agent` definition is deleted, AC1's first message allows,
  and stderr carries one line naming `agent` and `1 agent(s)`; with no agent in the turn, it writes
  nothing.
  Red when: a charter without the shape refuses, or the skip is silent while an agent was in the turn.
- **AC7** — When `stop_hook_active` is true in AC1's first payload, the hook allows.
  Red when: the arm refuses a chained stop.
- **AC8** — When `grep -n "handoff.py agents\|returned" help/roles.md` runs, the "What the hooks
  refuse" list shows the new bullet naming both heads and the verb.
  Red when: the page omits the refusal.
- **AC9** — When `grep -c "KIT_AGENT_CAP_VERSION = '1.36'" tools/hooks/agent-cap.js` prints 1 and
  `git grep -l "gov:kit agent-cap@1.35" -- '*.js'` prints nothing, every carrier moved.
  Red when: the constant or one marker keeps 1.35.
  figure: PINNED at `1e89fa5cd`, where the kit reads 1.35; a mint another build lands first moves
  the expected value by the same one step.

## 7. Gates

`format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `hook destinations (every declared hook path ships)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/format-guard.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 · the arms of §4 "The suite arms", against a hook whose `checkAgentLines` is staged to return no defect, then whose turn scan is staged to start at the file's first line · `FLOOR_ASSERTIONS` raised by the arms' count

The main loop observes the arms RED on each staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

- **F1 — How does the hook learn which agents the turn dispatched and received?**
  (a) From the main transcript the Stop payload names: the turn's `Agent` and `Workflow` calls and
  their results, the notifications delivered in it, and each run's journal; (b) from the agent
  ledger, the lines `handoff.py agents` added this turn; (c) from a sidecar a new PreToolUse or
  PostToolUse arm writes on every `Agent` and `Workflow` call.
  (b) grades the verb's output against itself, a guard sharing state with what it guards, and never
  sees an agent the main loop did not run the verb for. (c) adds wiring, and a sidecar records only
  what the hook was running to see, missing calls made while it was not wired. (a) reads the
  harness's own record of every call, needs no new state, and is the payload field the brief points
  at.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "The turn" and "What the turn requires" state it.
- **F2 — What does a received harness run require?**
  (a) An `agent` and a `returned` line for every agent its journal records; (b) a `returned` line
  per agent only. Under (b), an agent a background run started after its dispatch turn's stop is
  never shown with its `agent` line, which the owner's answer asks for every agent. (a) costs one
  more line per agent, and the verb prints both together.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read a Claude Code session transcript and its subagent
workflow journal to report each agent's model, usage and timestamps"` ranked the run-log kit's
`resolve_session_tree` and `read_journal` and the hook's own `readCharterShapes` among its
candidates. The seam this unit extends is `format-guard.js` itself: `checkStop`'s arming, its row
scan `scanMessageLines`, its shape builder `buildShapeRegex` and `readCharterShapes`, its witness
list and `renderBlockReason` (`tools/hooks/format-guard.js:129-297`). The turn rule is the run-log
prose reader's (`tools/runlog/prose.py:121-149`), spelled again in JavaScript because a hook may not
import a sibling kit's Python; no existing reader of a workflow journal is JavaScript. The recall
probe surfaced the addendum's record, whose ruling extends this hook and refuses a second one, and
`TOOL-aHeardState-1`'s spec, read against source: the hook still arms and bounds as it says.

Recall terms used: `agent transcript journal workflow subagent usage effort model ledger format-guard microformat runlog`
