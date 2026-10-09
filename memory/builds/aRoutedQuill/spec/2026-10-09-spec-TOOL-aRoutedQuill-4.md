# TOOL-aRoutedQuill-4 — every subagent starts holding the card's route, stated as facts

**Status:** INPROGRESS · rev-6 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aRoutedQuill-2-subagent-payload-probe.md](../build/2026-10-09-build-TOOL-aRoutedQuill-2-subagent-payload-probe.md) | research | TOOL-aRoutedQuill-2 |
| [2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md) | journal | TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-5 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-6 TOOL-aRoutedQuill-7 |
| [2026-10-09-prompt-TOOL-aRoutedQuill-4-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-4-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A subagent inherits the charter and the hooks, but not the parent session's orientation card, so it
meets `TOOL-aRoutedQuill-2`'s write gate without knowing which build, unit, spec and brief the
session is routed to. This unit wires `scratch-guard.js` on `SubagentStart` so every subagent starts
with the card's `## route` lines and what the gate will admit, worded as facts and within the
harness's 10,000-character cap.

## 2. Scope (IN)

- **S1** — A third fragment, `scratch-guard-subagent.fragment.json`, beside the shipped one: event
  `SubagentStart`, matcher `*`, marker `scratch-guard.js`, hook path `{kit}/hooks/scratch-guard.js`,
  no arguments. `tools/hooks/kit.toml` gains its one `[[files]]` rule, one rule per file as the home
  already keeps them. Gov's `.claude/settings.json` is re-merged with it. Observed by AC6.
- **S2** — `main` sends a payload whose `hook_event_name` is `SubagentStart` to `renderRouteContext`
  before its `tool_name` test, prints
  `{"hookSpecificOutput":{"hookEventName":"SubagentStart","additionalContext":<text>}}` on stdout and
  exits 0. With nothing true to say it prints nothing. Observed by AC1, AC2 and AC3.
- **S3** — With a route, the text is: one line naming the card; the `## route` heading and its lines
  byte-identical to the card; one line per unit giving the `checkBuildable` verdict; one line giving
  the `ROUTED_PATHS` value and what `scratch-guard.js` refuses under it. Observed by AC1.
- **S4** — Exactly one line when the session's card is absent, holds no `## route`, or routes no
  unit; exactly one line when the conf is UNARMED or unreadable by `TOOL-aRoutedQuill-2`'s rule.
  Nothing when the session directory is under no repository or its toplevel holds no conf, since
  the gate admits every write there. Observed by AC2 and AC3.
- **S5** — Every sentence states a fact: what the card holds, what each unit's spec reads, and what
  the gate refuses. None directs the subagent. Observed by AC4.
- **S6** — The text never exceeds `ROUTE_CONTEXT_CAP`, 10,000 characters. Past it, route lines are
  cut at a line boundary and a closing line names the card and how many lines it left out.
  Observed by AC5.
- **S7** — The branch never blocks and never surfaces an error: a throw exits 0 with nothing
  printed. Observed by AC7.
- **S8** — The codebase-map dossier `agent-cap.md` claims the new key
  `SubagentStart tools/hooks/scratch-guard.js`, and the generated map artifacts are regenerated in
  the same commit. Observed by AC6.
- **S9** — The arms live in `tools/hooks/scratch-guard.test.sh` over its orientation fixture, each
  observed RED before it lands, and `FLOOR_ASSERTIONS` moves by the count added. Observed by AC1,
  AC2, AC3, AC4, AC5 and AC7.
- **S10** — The file header and the `tools/hooks/README.md` section on the write gate state the third
  event, its silence rules and its cap. NOT OBSERVED by a criterion: prose.

## 3. Non-goals (OUT)

- Blocking or delaying a subagent. `SubagentStart` cannot block, and this unit adds no exit 2.
- Remedies, instructions or the brief's text. The context carries the brief's path from the route,
  and the deny the subagent may later meet carries the remedy.
- Filtering by `agent_type`. Read-only agent types receive the same few lines; a filter would be a
  second list of which agents write.
- Re-injecting the card into the main loop. The SessionStart card writer and replay already do it.
- Filling the route, which is `KICK-aRoutedQuill-1`'s, and evaluating writes, which is
  `TOOL-aRoutedQuill-2`'s.
- An adopter's wiring of this fragment, a `check-wiring.sh` arm for it, and a kit version bump.

### Edges

- **consumes-from** `TOOL-aRoutedQuill-2` — `checkBuildable`, `extractRouteUnits`, `readConfKey`,
  the `ROUTED_PATHS` grammar and the UNARMED rule this context states as facts. Without them the
  context would restate a rule it cannot evaluate, and both units edit `scratch-guard.js`.
- **consumes-from** `KICK-aRoutedQuill-1` — the card's `## route` section and its line shapes, which
  this context copies byte for byte.
- **hands-off** `TOOL-aRoutedQuill-5` — wiring this fragment in an adopter at install, and the
  check-wiring arm that reports it unwired.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- `procmon-hook.js` runs one script on two events and tells them apart by `hook_event_name`
  (`tools/process-monitor/procmon-hook.js:101`). That is this home's precedent for one marker on two
  events.
- `set_group` re-matches only within one event's groups (`tools/settings-merge.py:406-408`). Merged
  in memory at `6473ae38` over gov's `.claude/settings.json`, the widened PreToolUse fragment of
  `TOOL-aRoutedQuill-2` and this fragment, in either order and twice over, gave one
  `scratch-guard.js` entry per event and the same bytes on the second pass.
- `matchers_of` flattens the whole settings file and ignores the event
  (`tools/check-wiring.sh:341-346`), so any arm joining this fragment by marker sees the PreToolUse
  group's matcher beside `*`. That is for `TOOL-aRoutedQuill-5`'s arm to account for.
- A `SubagentStart` hook fired for a `Workflow` sidechain agent on 2026-08-15, its text arriving as
  its own message under the header `SubagentStart hook additional context:`
  (`memory/builds/cBriefedPilot/build/2026-08-15-build-TOOL-cBriefedPilot-15-2-parallelism-routes.md:49-50`).
  Its payload was not logged.
- The aReplayedCard design record found that hook-injected text should be factual, not imperative,
  because imperative hook text can trip prompt-injection defences
  (`memory/builds/aReplayedCard/build/2026-09-13-build-KICK-aReplayedCard-1-0-orientation-design.md:228`
  and `:515`).
- The card writer caps a card at `CARD_CAP_BYTES`, 8192 by default and overridable from the
  environment (`skills/session-kickoff/manifest-check.sh:128`), so the route section fits under the
  cap by default and not by construction.
- `SubagentStart` output is `additionalContext` alone, and the harness caps it at 10,000 characters:
  Claude Code's documentation as the shared contract records it on 2026-10-09; UNVERIFIED on this
  node, and the probe of §8 F1 logs one live payload.
- The codebase map keys a wiring as `<event> <script path>`; `agent-cap.md` claims the two
  PreToolUse keys today (`memory/map/features/agent-cap.md:24`).

### Data model

The fragment:

```json
{
  "name": "scratch-guard-subagent",
  "event": "SubagentStart",
  "matcher": "*",
  "marker": "scratch-guard.js",
  "hook_path": "{kit}/hooks/scratch-guard.js"
}
```

The text with a route, every line a statement:

```text
The parent session's orientation card, <card path>, holds this route:
## route
- build: <slug>
- unit: <unit id> · spec <repo-relative path>
- brief: <repo-relative path>
<unit id> is buildable: Tier-2 at INPROGRESS.
ROUTED_PATHS in .memory-tree.conf is: <value>
scratch-guard refuses an Edit, Write, MultiEdit or NotebookEdit under those paths unless a routed unit is buildable.
```

A unit that is not buildable reads `<unit id> is not buildable: <reason>.`, with the reason
`checkBuildable` gives the deny, such as `Tier-2 at SPECCED, and a Tier-2 unit admits writes at
INPROGRESS`. The one-line forms:

| State | The one line |
|---|---|
| no card, no `## route`, or no `- unit:` line | `No unit is routed in this session: <card path> is absent` (or `holds no route`, or `the route in <card path> names no unit`; with no `session_id`, `the payload carries no session_id`), `so scratch-guard refuses an Edit, Write, MultiEdit or NotebookEdit under ROUTED_PATHS (<value>).` |
| UNARMED | `<conf> leaves the write gate UNARMED: <reason>, so scratch-guard refuses every Edit, Write, MultiEdit or NotebookEdit in this repository except to that file.` The reason is `checkUnarmed`'s own text, the one the deny prints, so the two cannot word the rule twice: `TOOL-aRoutedQuill-2`'s S6, a blank or absent key, or a `ROUTED_PATHS` entry that is absolute, climbs through `..` or covers `MEMORY_ROOT`, the entry named. |
| conf unreadable | `<conf> could not be read (<code>), so scratch-guard refuses every Edit, Write, MultiEdit or NotebookEdit in this repository.` |

### The evaluation order

`renderRouteContext(data, env)` returns the text, or the empty string to print nothing.

1. `hook_event_name` is not `SubagentStart` → `main` goes on to its `tool_name` dispatch.
2. The session directory is `env.CLAUDE_PROJECT_DIR`, else the payload `cwd`. Under no `.git` → ''.
3. No `.memory-tree.conf` at its toplevel → ''.
4. The conf unreadable, or UNARMED → its one line.
5. `session_id` missing, no card under the common dir, no `## route`, or no `- unit:` line → the
   unrouted line.
6. Otherwise the block of §4 "Data model", cut to `ROUTE_CONTEXT_CAP`.

Past the cap, the closing line reads `<n> more route lines of <card path> are left out of this
context, which is capped at 10000 characters.` A unit line that is kept keeps its verdict line, and
one that is cut takes its verdict with it. The verdict reasons are `checkBuildable`'s; its two
Tier-1 SPECCED reasons ended in a remedy, `— flip it to INPROGRESS`, which S5 forbids here, so they
now end in the fact `a Tier-1 unit at INPROGRESS admits`, and the deny keeps its own remedy.

A throw anywhere in the branch exits 0 with nothing printed. The card is located exactly as
`TOOL-aRoutedQuill-2` locates it, so the context and the gate cannot disagree about which card a
subagent has.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `renderRouteContext` | function | `js.function`; `lexicon.py --suggest renderRouteContext --as js.function` answered OK |
| `ROUTE_CONTEXT_CAP` | number constant, 10000 | none: no constant cell is declared in `.lexicon.conf` |
| `scratch-guard-subagent.fragment.json` | fragment file | none: file names carry no cell here |
| `SubagentStart tools/hooks/scratch-guard.js` | codebase-map inventory key | claimed in `agent-cap.md` |

### Rollout

Lands at order 4, after `TOOL-aRoutedQuill-2`, because both units edit `scratch-guard.js` and this
one calls the readers that unit adds. A settings edit is live on the next tool call
(`memory/gotchas/settings-edit-takes-effect-mid-session.md`, measured 2026-08-10), so subagents
spawned after the merge, in the landing session too, receive the context. No kit version moves here: the hooks kit bumps once, after the build's last unit
touching it, and until then `govkit.py epoch` reports the move as owed at the lander.

### Files touched (estimate)

`tools/hooks/scratch-guard.js` · `tools/hooks/scratch-guard.test.sh` · `tools/hooks/scratch-guard-subagent.fragment.json` · `tools/hooks/kit.toml` · `tools/hooks/README.md` · `.claude/settings.json` · `memory/map/features/agent-cap.md` · `memory/map/generated/`

### Alternatives rejected

- **Arguments on the fragment, such as `--subagent`, to pick the branch.** The payload already names
  its event, as `procmon-hook.js` relies on, and an argument would add a second marker to keep in
  step for no gain in the merger, which scopes by event.
- **The route lines alone, without verdicts.** A subagent whose routed unit is still SPECCED at
  Tier-2 would learn that only from its first refused write.
- **Silence when no unit is routed.** The owner's mechanism asks for one line, and silence reads the
  same as a hook that never fired.
- **An imperative block such as the remedy list the deny carries.** Rejected on the design record's
  finding that injected text should be factual.
- **A `SubagentStop` check that the subagent wrote only under its unit.** Nothing in this build
  asks for it, and the write gate already judges each write as it happens.

## 5. Production-readiness checklist

- security — Reads the conf, the card and at most one spec per routed unit, all inside the session's
  repository; no spawn and no write. The emitted text copies card bytes the kickoff wrote and
  verified; it adds no instruction a hostile card could smuggle past the factual frame, because the
  frame is the hook's own sentences and the route lines are quoted as the card holds them.
- perf / scale — One node spawn per subagent start, measured at 0.8–1.1 s on node a (PINNED:
  verdict 13 of the aReplayedCard design record, 2026-09-13); no git spawn.
- error / empty / loading states — No repository or no conf prints nothing; an unrouted, UNARMED or
  unreadable state prints its one line; a throw prints nothing.
- observability — The subagent's own transcript carries the context under the harness's header,
  which is where the probe of §8 F1 reads it.
- risks — A wrong context misleads a subagent about what the gate admits; AC1 asserts the verdict
  line agrees with `checkRouted` on the same fixture. A route line carrying hostile text reaches
  the subagent verbatim; the card is written by the kickoff, never by a subagent.
- testing — The arms in §7 over `scratch-guard.test.sh`'s orientation fixture, feeding
  `SubagentStart` payloads and parsing stdout as JSON.
- migration — Gov's re-merge in this unit's commit; adopters move with `TOOL-aRoutedQuill-5`.
- user docs — The `tools/hooks/README.md` section.

## 6. Acceptance criteria

- **AC1** — When the self-test feeds a `SubagentStart` payload whose card routes one buildable unit,
  the hook exits 0, stdout parses as JSON whose `hookSpecificOutput.hookEventName` is
  `SubagentStart`, and `additionalContext` holds the card path, every `## route` line byte-identical
  to the card, a line naming the unit buildable and the `ROUTED_PATHS` value; for a `Tier-2` spec at
  `SPECCED` the verdict line names it not buildable and names `INPROGRESS`.
  Red when: a route line is paraphrased or missing, or the verdict disagrees with what `checkRouted`
  decides for a `Write` under that route on the same fixture.
- **AC2** — When the card is absent, or holds no `## route`, `additionalContext` is exactly one line
  naming the card path and the `ROUTED_PATHS` value.
  Red when: a subagent with no route is told nothing, or is told more than one line.
- **AC3** — When the fixture's conf declares `ROUTED_PATHS=""`, `additionalContext` is one line
  naming `ROUTED_PATHS`, the conf and the blank value; when it declares a `ROUTED_PATHS` entry
  climbing through `..`, the one line names `ROUTED_PATHS`, the conf, that entry and the `..` rule;
  when the fixture holds no conf, or `cwd` sits under no repository, the hook exits 0 with empty
  stdout.
  Red when: an UNARMED repository is described as routed or left silent, or a repository the gate
  admits every write in is told that writes are refused.
- **AC4** — When the arm scans the texts of AC1, AC2 and AC3, no line opens with a word from its
  closed list of imperatives (`Run`, `Write`, `Use`, `Read`, `Do`, `Don't`, `Never`, `Always`,
  `Append`, `Ask`, `Stop`), and no line carries `must`, `should` or `do not`.
  Red when: the injected text directs the subagent instead of stating what holds.
- **AC5** — When the fixture card's route section is padded past 12,000 characters,
  `additionalContext` is at most `10000` characters, every route line it keeps is whole, and its
  last line names the card path and the count of route lines left out.
  Red when: the context exceeds the harness's cap, or a line is cut mid-way.
  figure: PINNED — 10,000 is the harness cap the shared contract recorded from Claude Code's
  documentation on 2026-10-09; the padding is DERIVED from it in the arm.
- **AC6** — When `settings-merge.py --check --fragment` runs here over
  `scratch-guard-subagent.fragment.json` after the rewire, it exits 0, and `.claude/settings.json`
  holds `scratch-guard.js` once under `SubagentStart` with matcher `*` and once under `PreToolUse`;
  `python tools/codebase-map/gen_map.py --check` exits 0 with `SubagentStart tools/hooks/scratch-guard.js`
  in `agent-cap.md`'s `harness-hooks` row.
  Red when: the merge moves or duplicates the PreToolUse entry, or the new wiring is an unclaimed
  inventory key.
- **AC7** — When a `SubagentStart` payload carries a `cwd` that is not a string and
  `CLAUDE_PROJECT_DIR` is unset, the hook exits 0 with stdout and stderr both empty.
  Red when: an error in the branch surfaces to the subagent, or the hook exits non-zero.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `settings-merge selftest` · `hook destinations (every declared hook path ships)` · `install-prefix (shipped surface)` · `govkit selfcheck` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC7 · the HEAD hook after TOOL-aRoutedQuill-2, which exits 0 with empty stdout for every SubagentStart payload · FLOOR_ASSERTIONS

AC6 is a direct observation of this repository after the rewire and adds no arm.

## 8. Open questions

- **FACT-QUESTION · F1 — Does `SubagentStart` fire for a `Workflow` sidechain agent, and does its payload carry the parent session's `session_id`?**
  The firing half has one observation, 2026-08-15, and the payload half none (§4 Evidence). If the
  payload carries the subagent's own id, the card lookup misses and the context tells a routed
  subagent that nothing is routed.
  Probe: the one harness `TOOL-aRoutedQuill-2`'s F1 names, a throwaway clone under a short TEMP
  root whose settings log one JSON line per `SubagentStart` and per PreToolUse `Write`, holding
  `hook_event_name`, `session_id`, `agent_id`, `agent_type` and the hook's own
  `CLAUDE_CODE_SESSION_ID`. One `claude -p` session, never `--bare`, has the main loop Write one
  scratch file, spawn one `Agent` subagent and run one `Workflow` script with one agent, each of
  which writes one scratch file.
  Deciding observation: a `SubagentStart` line exists for each spawn kind, and its `session_id` is
  byte-equal to the main loop's Write line.
  Liveness: the log holds the main loop's Write line and each subagent's own Write line. A spawn
  kind whose Write line is present and whose `SubagentStart` line is absent is a real "does not
  fire"; a kind with neither line is a DEAD PROBE, never an answer.
  Options if it does not fire for `Workflow` agents: (a) accept it, since those agents still meet
  the write gate's refusal, which names the card, and the unattended unit harness already hands its
  builder the spec and brief paths; (b) also put the route into the Workflow harnesses' prompts,
  which is the unattended kit's change and not this unit's.
  Options if the id is the subagent's own: follow whichever key `TOOL-aRoutedQuill-2`'s F1 settles
  on, so the context and the gate read one card.
  Recommendation: run the probe once for both units before either build pass; take (a) on a
  "does not fire".
  RESOLVED (agent, 2026-10-09, delegated): it fires for both. `SubagentStart` fired for an `Agent`
  subagent and for a `Workflow` agent (`agent_type: workflow-subagent`), each with the main loop's
  `session_id` byte-equal, so the context hook and the gate read one card. Evidence: `memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-2-subagent-payload-probe.md`.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §3 · §4 · cross-read fold: order 3 to 4, because `KICK-aRoutedQuill-1` moved
  from order 1 to 2, which shifts every later step by one.
- rev-3 · 2026-10-09 · §4 · Rollout corrected: hooks are re-read on the next tool call, per the
  gotcha catalogue's measurement, so subagents get the context inside the landing session.
- rev-4 · 2026-10-09 · §4 · AC3 · the M2 cross-read of 2026-10-09 found the UNARMED line said the
  conf declares no key, true only for a blank or absent key, while `TOOL-aRoutedQuill-2`'s UNARMED
  also covers an entry that is absolute, climbs through `..` or covers `MEMORY_ROOT`; the line now
  names the key and the rule it broke, and AC3 adds a `..` entry case.
- rev-5 · 2026-10-09 · §8 F1 · resolved by the stated probe, run by the unattended run before step 3; the record is `memory/builds/aRoutedQuill/build/2026-10-09-build-TOOL-aRoutedQuill-2-subagent-payload-probe.md`.
- rev-6 · 2026-10-09 · §4 · the build pass: the UNARMED line quotes `checkUnarmed`'s reason rather than a second wording of it; the unrouted line gains the no-unit and no-`session_id` forms; the closing line past the cap is spelled; and `checkBuildable`'s two Tier-1 SPECCED reasons lose their imperative tail, which S5 would have refused in the context.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "SubagentStart hook emits additionalContext JSON carrying
the orientation card route section to every subagent"` found no emitter of hook context to extend:
its ranked symbols are rendering and JSON helpers of other kits. It listed the harness-hooks keys,
among them `PreToolUse tools/hooks/scratch-guard.js` and `SessionStart tools/process-monitor/procmon-hook.js`,
and those are the seams extended: the first is the script this unit wires on a second event, and
the second is the precedent for one script dispatching on `hook_event_name`. The readers reused are
`TOOL-aRoutedQuill-2`'s `checkBuildable`, `extractRouteUnits` and `readConfKey`, and `readCard` and
`resolveCommonDir` in `tools/hooks/scratch-guard.js`.

Recall terms used: `SubagentStart additionalContext sidechain subagent orientation card injected
factual imperative hook Workflow build pass re-injection` — which surfaced the cBriefedPilot
parallelism-routes record where a `SubagentStart` hook fired in a `Workflow` sidechain, and the
aReplayedCard design record's finding that injected text should be factual.
