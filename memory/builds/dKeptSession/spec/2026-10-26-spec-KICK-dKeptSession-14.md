# KICK-dKeptSession-14 — what a session does as its window fills, by `context.on-full` and `context.threshold`

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 12 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0152@da455c7f whole
**Carries:** node:policy-key.context.on-full
**Carries:** node:policy-key.context.threshold

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 |
| [2026-10-26-build-KICK-dKeptSession-1-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-1-fix-return.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-5 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-26 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-fix-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-5 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

A session whose window fills is compacted by the harness, and a compaction costs more than a fresh
start: measured, a compaction reads about 970k cached tokens over about 117 s, a fresh start's first
turn 84k (layer-runtime RT-1,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:1345-1366`).
The owner's answer made `fresh-at-boundary` the default: once `context.threshold` is crossed, the
session ends at the next item boundary and a fresh one reorients from the card (v2:1238-1239). Today
nothing measures the fill and nothing acts on it (gap-orient-06). This unit measures the owner
session's fill from its transcript, reports it in the replay, and at an item boundary past the
threshold tells the session to go fresh there, by `context.on-full` and `context.threshold`.

## 2. Scope (IN)

- **S1** — The fill, I13. `measure_context_fill(transcript, until=None)` in
  `tools/runlog/extract.py`: the share of the window the transcript's last main-session `usage`
  event at or before `until` used (the end when `until` is `None`), or `None` with no such event.
  The share of one event is `derive_context_fill(ev)`, its `in`, `cache_read` and `cache_write`
  summed by `derive_context_tokens(ev)` over `CONTEXT_WINDOW_TOKENS = 200000`, exported so a reader
  holding events already, KICK-dKeptSession-9's per-stage rows among them, takes the share of any
  event without re-reading the transcript. `derive_context_tokens` is extracted from
  `measure_ready_tree`'s sum (:1231), which then calls it, so the sum lives once. `python
  tools/runlog/runlog.py context <transcript>` prints `<n>%` or `none`, exit 0. Observed by AC1, AC2.
- **S2** — The keys, each read once per verb by `read_card_policy` (TOOL-dPlacedRequest-2 S11, I8):
  `context.on-full`, `compact-with-card` or `fresh-at-boundary`, default `fresh-at-boundary`
  (v2:1238, RT-1); and `context.threshold`, a share of the window as `<n>%`, default `60%`, read only
  under `fresh-at-boundary` (v2:1239). A refused read takes the catalogue default with one NOTE. Both
  rows stand in dGroundRules' catalogue (GR `catalogue.toml:616-626`, owner dKeptSession); this unit
  writes their `summary` and `usage` and drains them from `unsummarised-keys.txt`, and runs
  TOOL-dDeclaredLoop-6 S4's `python tools/playbook/core.py new policy-key <name> … --owner
  dKeptSession` only where the landed catalogue lacks a row. Observed by AC5, AC8.
- **S3** — The boundary act. Inside KICK-dKeptSession-13's `--card --boundary` verb, after
  `derive_item_boundary` reports a crossing and with the payload's `transcript_path` passed as
  `--transcript`: under `fresh-at-boundary`, a fill at or past the threshold prints `context — <n>% of
  window · past <threshold> · fresh now, at this item boundary (context.on-full: fresh-at-boundary)`,
  which KICK-dKeptSession-13 S7's hook step hands the session as PreToolUse `additionalContext`; a
  fill under it prints nothing. Under `compact-with-card` nothing is measured and nothing printed: the
  harness compacts and the replay hook re-injects the card, as today. Observed by AC3, AC4, AC5.
- **S4** — The replay line, I10's `context —` slot (KICK-dKeptSession-12 S5), from the replay
  payload's `transcript_path`: under `fresh-at-boundary`, `context — <n>% of window · past <threshold>
  · fresh at next item boundary (context.on-full: fresh-at-boundary)` at or past the threshold, and
  `context — <n>% of window · under <threshold>` below it; under `compact-with-card`, `context — <n>%
  of window (context.on-full: compact-with-card)`. No transcript, or no usage in it, prints `context —
  skipped: <why>`. Observed by AC6.
- **S5** — The owner session only (layer-runtime :783-787). The boundary act runs only where
  KICK-dKeptSession-13 S7's step runs, which skips a payload carrying `agent_type`; SubagentStart
  never reaches S3 or S4; and the replay fires only on a main session's `resume` or `compact`. An
  act session of dWellOiledMachine's Runtime reads neither key once Runtime marks it. Observed by AC7.
- **S6** — The plants `context-fresh-past`, `context-under`, `context-compact` and
  `context-replay` in `skills/session-kickoff/card-store.fixture.sh`, each over a transcript fixture
  whose last main usage the plant sets, with the stub policy kit recording which keys were read; and
  the transcript fixture `tools/runlog/fixtures/context-fill.jsonl` with a selftest case in
  `tools/runlog/selftest.py`. Observed by AC1, AC3 to AC6.
- **S7** — `help/orientation-card.md` gains the `context —` lines, the two values and the threshold,
  and that the measure is the last turn's tokens over a pinned window. Observed by AC9.

## 3. Non-goals (OUT)

- Ending a session and starting its successor: an agent cannot end itself here, so the line tells the
  session; the act is dWellOiledMachine's Runtime, where the owner session's executor lives.
- Compaction itself and the card it re-injects: the harness's and the existing `orientation-replay`
  hook's.
- Act sessions' bounds, `--max-turns` and `runtime.act-ceiling`: Runtime's (layer-runtime :786-787).
- Orientation cost per stage: KICK-dKeptSession-9, which imports `measure_context_fill`.
- TOOL-dPlacedRequest-2 §3's non-goal "a context-size leg of `fresh-when-idle`" stands: this unit
  adds no leg to `resume.context`.

### Edges

- **consumes-from** `KICK-dKeptSession-12` — `print_replay`, with I10's order, whose last slot the `context —` line fills
- **consumes-from** `KICK-dKeptSession-13` — `## pointers`, the section a fresh session reorients from once this unit has ended its predecessor at a boundary
- **consumes-from** `KICK-dKeptSession-13` — `derive_item_boundary`, read inside the `--card --boundary` verb, the only point S3 acts at; without it there is no boundary to go fresh at
- **hands-off** `KICK-dKeptSession-9` — `measure_context_fill`, with `derive_context_fill` for one event, the one context reader orientation cost per stage imports and never copies
- **consumes-from** external — dPlacedRequest's `read_card_policy` and `card-store.fixture.sh` (TOOL-dPlacedRequest-2 S11, S12), and the replay payload capture of S7
- **hands-off** `KICK-dKeptSession-30` — `measure_context_fill`, `derive_context_fill` and `CONTEXT_WINDOW_TOKENS`, which that unit re-points to the derived window (id 16)
- **hands-off** `KICK-dKeptSession-44` — AC7 and the fill fixture, the batch's S35 and S39 (ids 13, 41)

## 4. Design

### Evidence

- `measure_ready_tree` sums a main usage event's `in`, `cache_read` and `cache_write` as its context
  (`tools/runlog/extract.py:1229-1233`, the sum itself at :1231); `extract_session` (:843) yields
  those fields on every `usage` event (:835-836) with its `src`, and `build_session_tree` (:238)
  takes one transcript path.
- TOOL-dPlacedRequest-2 §3 says the hook payload carries no context size; true of the payload, but
  the payload's `transcript_path` names a transcript that does (scout C's disagreement).
- RT-1 moved the default to `fresh-at-boundary` in every preset, and v2's `[policies]` rows carry it
  (v2:1238-1239); the CX-1 settlement's `compact-with-card` default was the earlier answer RT-1
  revised.
- The harness on this node accepts `additionalContext` in a PreToolUse hook's output (§8 F1).

### The lines

```
context — 72% of window · past 60% · fresh now, at this item boundary (context.on-full: fresh-at-boundary)
context — 72% of window · past 60% · fresh at next item boundary (context.on-full: fresh-at-boundary)
context — 41% of window · under 60%
context — 41% of window (context.on-full: compact-with-card)
```

The first is the boundary act's, the other three the replay's.

### The window

`CONTEXT_WINDOW_TOKENS = 200000`, PINNED 2026-10-26 as the standard window of the models this harness
runs, UNVERIFIED against the platform's documentation in this tree, one constant beside the sum. A
session on a larger window reads a share above its true one, which errs towards going fresh.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `measure_context_fill`, `derive_context_fill`, `derive_context_tokens` | functions, `tools/runlog/extract.py` | `py.function`, asked at the pass |
| `CONTEXT_WINDOW_TOKENS` | constant, `tools/runlog/extract.py` | none declared |
| `context` | subcommand of `runlog.py` | none |
| `render_context_line`, `run_context_boundary` | shell functions, `manifest-check.sh` | `sh.function`, asked at the pass |
| `context —` | replay and boundary line | none |
| `context-fill.jsonl` | transcript fixture | none |

### Migration

None. Two catalogue rows gain their text; no stored state changes.

### Rollout

Live at landing for a session whose card routes a build and whose harness passes `transcript_path`.

### Files touched (estimate)

- `tools/runlog/extract.py`: S1, `measure_ready_tree` re-pointed to `derive_context_tokens`
- `tools/runlog/runlog.py`: the `context` subcommand
- `tools/runlog/selftest.py`: the fill case
- `tools/runlog/fixtures/context-fill.jsonl` (new)
- `skills/session-kickoff/manifest-check.sh`: S3, S4; `KIT_MANIFEST_VERSION` moved
- `skills/session-kickoff/manifest-check.test.sh`: the arm the §7 line declares
- `skills/session-kickoff/card-store.fixture.sh`: S6's plants
- `tools/policy/catalogue.toml`: the two rows' `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`: drained by `lists --write`
- `help/orientation-card.md`: S7

### Alternatives rejected

- **A copy of the sum in the shell.** The `[reuse]` rule and KICK-dKeptSession-9's import both need
  one reader.
- **The fill from the hook payload.** It carries none; the transcript it names does.
- **The act at every tool call.** The clause acts at an item boundary; a tool call mid-item would end
  an item half done.

## 5. Production-readiness checklist

- security — the transcript is read, never written, and only its usage counts leave it: no message
  text reaches a line.
- perf / scale — one transcript parse per boundary crossing and per replay; a crossing happens at most
  once per commit. The parse reads the whole transcript, so a long session's boundary costs more;
  reading from the end is the upgrade if it shows.
- error / empty / loading states — no transcript, an unreadable one or no usage prints `skipped:
  <why>` and acts on nothing.
- observability — every replay prints the fill and the value that decided it.
- risks — a window larger than the pinned constant overstates the share, so a session goes fresh
  early, the cheaper error by RT-1's measurement.
- testing — S6's plants and the selftest case, red and green.
- migration — none.
- user docs — `help/orientation-card.md`, S7.

## 6. Acceptance criteria

- **AC1** — When `python tools/runlog/runlog.py context context-fill.jsonl` runs from the runlog
  fixtures directory over a transcript whose last main usage is `in` 1000, `cache_read` 100000 and
  `cache_write` 19000, with a later subagent usage of 190000, it prints `60%`.
  Red when: a subagent's usage or an earlier turn decides the share.
- **AC2** — When `grep -n "derive_context_tokens" tools/runlog/extract.py` runs, it finds the
  definition and its calls from both `measure_ready_tree` and `measure_context_fill`, and `grep -c
  'ev\["in"\] + ev\["cache_read"\]' tools/runlog/extract.py` prints `1`.
  Red when: the sum is written twice.
- **AC3** — When `bash card-store.fixture.sh --plant context-fresh-past` runs `--card --boundary` on
  a crossing under `fresh-at-boundary` and `60%` with a transcript at 72%, it prints `context — 72% of
  window · past 60% · fresh now, at this item boundary (context.on-full: fresh-at-boundary)`.
  Red when: a crossing past the threshold prints no line.
- **AC4** — When the plant `context-under` runs the same crossing with a transcript at 41%, no
  `context —` line prints; with no crossing at 72%, none prints either.
  Red when: the line prints under the threshold, or away from a boundary.
- **AC5** — When the plant `context-compact` sets `context.on-full` to `compact-with-card`, the
  crossing at 72% prints no line and the stub policy kit's log shows `context.threshold` never read.
  Red when: `compact-with-card` acts, or reads the threshold.
- **AC6** — When the plant `context-replay` replays a compaction under `fresh-at-boundary` at 72%,
  the output's last computed line is `context — 72% of window · past 60% · fresh at next item
  boundary (context.on-full: fresh-at-boundary)`, after `position —`; under `compact-with-card` it
  reads `context — 72% of window (context.on-full: compact-with-card)`.
  Red when: the line is absent or out of I10's order.
- **AC7** — When `node tools/hooks/scratch-guard.js` reads a PreToolUse Bash payload carrying
  `agent_type` in a fixture whose session is past the threshold at a crossing, it prints no `context
  —` line.
  Red when: a role agent is told to go fresh.
- **AC8** — When `python policy.py get context.on-full` and `get context.threshold` run in a
  repository whose policy file sets neither, they print `fresh-at-boundary` and `60%`, and after
  `policy.py lists --write` the summary list names neither key.
  Red when: a default differs from v2:1238-1239, or a row stays unsummarised.
  fixture: the catalogue is dGroundRules', untracked at base until it lands.
- **AC9** — When `grep -n "context.on-full" orientation-card.md` runs over the help page, it finds S7's
  section naming `fresh-at-boundary`, `compact-with-card` and `context.threshold`.
  Red when: the page does not describe the line.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC3 AC5 AC6 · the boundary act and the replay line over a stub policy kit and a planted transcript, the failing case a crossing past the threshold that prints nothing · none

New arm: tools/runlog/selftest.py · covers AC1 · the fill over `context-fill.jsonl`, the failing case a later subagent usage read as the main session's · none

## 8. Open questions

- **FACT-QUESTION · F1 — Does a PreToolUse hook's output reach the model, so the boundary act's line
  is read?** Probe: read the installed harness's bundled hook-output schemas,
  `grep -a -o 'u({hookEventName:A("[A-Za-z]*")[^}]*})'` over the `claude` on PATH (`claude
  --version` 2.1.292 on this node, 2026-10-26), and classify each event's schema by whether it carries
  `additionalContext`. Observation: `PreToolUse` carries it, beside `permissionDecision`, and the
  harness yields it as a `hook_additional_context` message outside an agent context. Liveness: the
  same probe reads `CwdChanged`, `PermissionRequest`, `PreModelSwitch` and `WorktreeCreate` as
  lacking it, so it can return a negative. RESOLVED (agent, 2026-10-26, delegated): PreToolUse
  `hookSpecificOutput.additionalContext`, the channel KICK-dKeptSession-13 S7's step emits.
  widens: none · relaxes: none
- **F2 — What is the window `context.threshold` is a share of?** Options: (a) one pinned constant,
  200000 tokens; (b) a table from each usage event's model id to its window; (c) a new policy key.
  (c) is a key no clause names, a public surface outside this build's row; (b) needs a model-to-window
  table the tree cannot verify, a window being an account setting a model id need not show. Both (a)
  and (b) meet every criterion here. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, by the
  tie-break, fewer open questions, its error running towards a fresh start, which RT-1 measured as the
  cheaper one. widens: none · relaxes: none
- **F3 — Which default does `context.on-full` carry?** The CX-1 settlement says `compact-with-card`,
  and RT-1 later says `fresh-at-boundary`. RESOLVED (agent, 2026-10-26, delegated):
  `fresh-at-boundary`, rung 1, v2:1238, the baseline, which carries RT-1's answer.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 14, CX-1, RT-1 and layer-runtime
  :783-787, v2:1238-1239, and scout C's row and disagreement for this unit.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-30`, `KICK-dKeptSession-44`
  mirrored, the other ends of the edges the round-1 spec audit's promoted units declare; no other
  section moved.

## 10. Reuse audit

The seams extended are `measure_ready_tree`'s context sum (`tools/runlog/extract.py:1204`, the sum
at :1231, verified at base), extracted into `derive_context_tokens` and called by both readers;
`build_session_tree` (:238) and `extract_session` (:843) for one transcript; `runlog.py`'s subcommand
table (`tools/runlog/runlog.py:497`); and, for the act and the line, KICK-dKeptSession-13's boundary
verb and KICK-dKeptSession-12's replay order. `python tools/codebase-map/reuse_lookup.py "measure how
full the context window is from a session transcript"` ranked `extract_session`,
`resolve_session_tree` and `measure_ready_tree` in `tools/runlog/extract.py`, the seam this unit
extends, and `measure_typed_counts` in `tools/codebase-map/map_lib.py`, which counts map rows and is
unrelated. Scout C's row agrees with source on the sum's line and on the replay hook's matcher; its
disagreement with TOOL-dPlacedRequest-2 §3 is recorded in §4. The recall query returned scout C's row
and the CX-1 proposal it cites.

Recall terms used: `python tools/memory-recall/query.py "what does a session do when its context window fills past a threshold" --terms "context.on-full context.threshold fresh-at-boundary compact-with-card context fill window transcript item boundary RT-1"`
