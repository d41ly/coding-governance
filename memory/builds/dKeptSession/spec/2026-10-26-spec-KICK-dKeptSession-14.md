# KICK-dKeptSession-14 — what a session does as its window fills, by `context.on-full` and `context.threshold`

**Status:** CLOSED · rev-6 · 2026-11-22 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 12 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0152@da455c7f whole
**Carries:** node:policy-key.context.on-full
**Carries:** node:policy-key.context.threshold

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-1-fix-return.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-5 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-26 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-14-deviation-141.md](../build/2026-10-26-build-KICK-dKeptSession-14-deviation-141.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-14-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-14-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-KICK-dKeptSession-16-reground-orders-7-13-returns.md](../build/2026-11-21-build-KICK-dKeptSession-16-reground-orders-7-13-returns.md) | research | KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-30 KICK-dKeptSession-9 |
| [2026-10-26-prompt-KICK-dKeptSession-1-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-fix-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-5 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief.md) | research | KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-26 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-11 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 |
| [2026-11-21-prompt-KICK-dKeptSession-14-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-14-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-15-orders-11-12-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-15-orders-11-12-reground-brief.md) | research | KICK-dKeptSession-15 |
| [2026-11-21-prompt-KICK-dKeptSession-26-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-26-precheck-brief.md) | research | KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-30 KICK-dKeptSession-9 |
| [2026-11-22-prompt-KICK-dKeptSession-14-1-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-14-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-14-divergence-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-14-divergence-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

A session whose window fills is compacted by the harness, and a compaction costs more than a fresh
start. Measured, a compaction reads about 970k cached tokens over about 117 s (PINNED by RT-1),
and a fresh start's first turn reads 84k (layer-runtime RT-1,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md@c7422838cc6e:1349`).
The owner's answer made `fresh-at-boundary` the default: once `context.threshold` is crossed, the
session ends at the next item boundary and a fresh one reorients from the card
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:1238`).
dGroundRules landed both keys' catalogue rows with those defaults, but nothing measures the fill and
nothing reads either key (gap-orient-06). This unit measures the owner session's fill from its
transcript, reports it in the replay, and at an item boundary past the threshold tells the session
to go fresh there, by `context.on-full` and `context.threshold`.

## 2. Scope (IN)

- **S1** — The fill, I13. `measure_context_fill(transcript, until=None)` in
  `tools/runlog/extract.py`: the share of the window the transcript's last `usage` event with `src`
  `main` at or before `until` used (the end when `until` is `None`), or `None` with no such event. It
  reads the main file alone, as `SessionTree(sid=<stem>, main=<path>)` through `extract_session`
  (`tools/runlog/extract.py#SessionTree`, `#extract_session`), never `build_session_tree`, so no
  agent file is parsed. The share of one event is `derive_context_fill(ev)`, its `in`, `cache_read`
  and `cache_write` summed by `derive_context_tokens(ev)` over `CONTEXT_WINDOW_TOKENS = 200000`,
  exported so a reader holding events already, KICK-dKeptSession-9's per-stage rows among them,
  takes the share of any event without re-reading the transcript. `derive_context_tokens` is
  extracted from `measure_ready_tree`'s sum (`tools/runlog/extract.py#measure_ready_tree`), which
  then calls it, so the sum lives once. `python tools/runlog/runlog.py context <transcript>` prints
  `<n>%`, `<n>` the share times 100 rounded down, or `none`, exit 0. Observed by AC1, AC2.
- **S2** — The keys, each read once per verb by `read_card_policy`
  (`skills/session-kickoff/manifest-check.sh#read_card_policy`), which gains them as it holds its
  other keys: a default, one literal `get` line, and a value check, `context.on-full` against
  `compact-with-card` and `fresh-at-boundary`, `context.threshold` against the row's pattern
  `(100|[1-9]?[0-9])%`. Its comment names the keys it reads without counting them. A refused read
  prints `context — skipped: <key> refused: <why>` and acts on nothing, as `derive_resume_lines`
  prints its refusals; no policy kit resolving takes the catalogue default with the NOTE
  `read_card_policy` already prints. `context.threshold` is read only under `fresh-at-boundary`.
  Both rows stand in the landed catalogue, owner dKeptSession, defaults `fresh-at-boundary` and
  `60%` (`tools/policy/catalogue.toml`, rows `context.on-full` and `context.threshold`); this unit
  writes their `summary` and `usage` and drains them from `tools/policy/unsummarised-keys.txt` by
  `policy.py lists --write`. With both fields written, `help/reference/policy.md`, which
  `tools/playbook/render_playbook.py#render_reference_page` renders from the catalogue and whose `## Not yet
  summarised` list holds a row lacking either field, is re-rendered in the same commit by `python
  tools/playbook/render_playbook.py --reference`, never edited by hand, after S9's anchors stand.
  Observed by AC5, AC8, AC11.
- **S3** — The boundary act. `run_context_boundary`, inside KICK-dKeptSession-13 S6's `--card
  --boundary` verb, after `derive_item_boundary` reports a crossing and with the payload's
  `transcript_path` passed as `--transcript`: under `fresh-at-boundary`, a fill at or past the
  threshold prints `context — <n>% of window · past <threshold> · fresh now, at this item boundary
  (context.on-full: fresh-at-boundary)`. The verb runs detached and writes its lines to its `--out`
  file, which KICK-dKeptSession-13 S7's hook step hands the session as PreToolUse
  `additionalContext` at the session's next shell call after the verb finishes, never on the call
  that started it. A fill under the threshold, or any skip, prints nothing there, since a line
  injected at every boundary that changes no act teaches the session to skip it. Under
  `compact-with-card` nothing is measured and nothing printed: the harness compacts and the replay
  hook re-injects the card, as today. Observed by AC3, AC4, AC5.
- **S4** — The replay line, `render_context_line`, in I10's `context —` slot (KICK-dKeptSession-12
  S5), after KICK-dKeptSession-15's `position —` and `lead —` lines and before the `now —` line,
  which stays last, from `CARD_TRANSCRIPT`, which
  `read_session_id` already keeps from the payload (`#read_session_id`); that reader reads the
  payload only when no `--session` is given, so a replay run with one reads no transcript and prints
  the no-path skip. Under `fresh-at-boundary`
  it prints `context — <n>% of window · past <threshold> · fresh at next item boundary
  (context.on-full: fresh-at-boundary)` at or past the threshold, and `context — <n>% of window ·
  under <threshold>` below it; under `compact-with-card`, `context — <n>% of window (context.on-full:
  compact-with-card)`. No transcript path, a path naming no file, no main usage in it, no runlog kit
  resolving, no Python or no working `timeout -k`, or a call past its bound prints `context —
  skipped: <why>`. Observed by AC6, AC10.
- **S5** — The bound. Both calls of `runlog.py context` run as `derive_map_block` runs the map
  (`#derive_map_block`): `timeout -k 2` under `CARD_CONTEXT_BOUND=${CARD_CONTEXT_BOUND:-5}` seconds,
  stdin closed, output into a scratch file; the env override is the fixture's. Inside the detached
  boundary verb this is the transcript read's own bound, as each of that verb's steps runs under its
  own (KICK-dKeptSession-13 F4); the hook never waits on it. Observed by AC10.
- **S6** — The owner session only (layer-runtime,
  `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md@c7422838cc6e:783`).
  The boundary act runs only where KICK-dKeptSession-13 S7's step runs, which skips a payload carrying
  `agent_type` or `agent_id`, and the replay fires only on a main session's `resume` or `compact`. NOT OBSERVED
  here: this unit adds no role check of its own, and KICK-dKeptSession-13 AC5 observes the skip.
- **S7** — The plants `fill-fresh-past`, `fill-under`, `fill-compact`, `fill-replay` and `fill-slow` in
  `skills/session-kickoff/card-store.fixture.sh`, appended to its `PLANTS`, which the manifest-check
  suite's card-store block runs by `--list`. They are named apart from the fixture's `context-*`
  arm, which a `context-` name would fall into. `write_card_fixture`
  (`skills/session-kickoff/card-store.fixture.sh#write_card_fixture`) writes the runlog kit's
  `runlog.py` as a stub answering `context <path>` with the share and the delay a file outside the
  repository plants, plants `context.on-full` and `context.threshold` at their defaults in the stub
  policy kit, and has that stub append each key it is asked to a log beside `CARD_STUB_POLICY`. The
  boundary plants write a crossing's `--boundary` key into the plant file outside the repository
  that KICK-dKeptSession-13 S9's stub loop kit answers from, and add no second loop stub. The stub
  `runlog.py` is written at the path `resolve_kit_file runlog runlog.py` answers over the gov tree,
  as the stub `policy.py` is, since the fixture copies no runlog kit; the replay plants pipe their
  payload on stdin with no `--session`, as the fixture's `replay` plant does. The suite's
  `FLOOR_ASSERTIONS` rises by one per new plant
  (`skills/session-kickoff/manifest-check.test.sh@b771dadeb50a:2489`). Observed by AC3 to AC6, AC10.
- **S8** — The `context-fill` scenario in `tools/runlog/fixtures/transcripts.json`, written as the
  store's other scenarios are by `build_scenario` (`tools/runlog/selftest.py#build_scenario`), and
  one selftest case over it in `tools/runlog/selftest.py`, its `ASSERTION_FLOOR` raised by the case's
  checks and the three decoy checks `main` runs after every `test_` function, with a `RAISED` comment
  pricing them as the floor's others do (`tools/runlog/selftest.py#main`). Observed by AC1.
- **S9** — `help/orientation-card.md`'s section "When a session resumes" gains the `context —` lines,
  the two values and the threshold, and that the measure is the last turn's tokens over a pinned
  window; `tools/runlog/README.md`'s transcript-extractor block gains the `context` command. The help
  page shows no `runlog.py` command: `runlog.py` has no `[[usage]]` row, and the `docs` leg reds a
  page command naming a tracked entrypoint with none as `UNROWED`
  (`tools/govkit/docs_leg.py#check_page_command`). That paragraph carries the keys' usage anchors,
  `<!-- usage: policy:context.on-full <fp> -->` and `<!-- usage: policy:context.threshold <fp> -->`,
  as the page's `card.pointers` paragraph carries that key's, each `<fp>` the key's fingerprint as
  `python tools/govkit/docs_leg.py --fingerprints` prints it at build time, after S2's fields are
  written, since the fingerprint hashes the row's fields (`tools/govkit/docs_leg.py#derive_usage_fingerprint`). S2's
  re-render then shows each key as `Documented on` a link to `help/orientation-card.md`,
  and the same commit takes the rows `policy:context.on-full` and `policy:context.threshold` off
  `memory/project/docs-undocumented.txt`, since `read_docs_state` reds a listed row a page anchors as
  `DRAINED`. The re-render also carries `card.pointers` off the page's `## Not yet summarised` list,
  the stale row recorded in §4's Evidence. Observed by AC9, AC11.

## 3. Non-goals (OUT)

- Ending a session and starting its successor: an agent cannot end itself here, so the line tells the
  session; the act is dWellOiledMachine's Runtime, where the owner session's executor lives.
- Compaction itself and the card it re-injects: the harness's and the existing `orientation-replay`
  hook's.
- Act sessions' bounds, `--max-turns` and `runtime.act-ceiling`: Runtime's (layer-runtime RT-1).
- Orientation cost per stage: KICK-dKeptSession-9, which imports `measure_context_fill`.
- The window itself: KICK-dKeptSession-30 derives it per model at order 13 and retires the constant.
- TOOL-dPlacedRequest-2's non-goal "a context-size leg of `fresh-when-idle`" stands: this unit adds no
  leg to `resume.context`.

### Edges

- **consumes-from** `KICK-dKeptSession-12` — `print_replay`, with I10's order, whose last computed slot, after `position —` and before `now —`, the `context —` line fills
- **consumes-from** `KICK-dKeptSession-15` — `print_replay`'s `position —` line, the slot the `context —` line follows
- **consumes-from** `KICK-dKeptSession-13` — `## pointers`, the section a fresh session reorients from once this unit has ended its predecessor at a boundary
- **consumes-from** `KICK-dKeptSession-13` — `derive_item_boundary`, read inside the detached `--card --boundary` verb whose `--out` file the hook delivers, the only point S3 acts at, and its S9 stub loop kit's plant file; without it there is no boundary to go fresh at
- **hands-off** `KICK-dKeptSession-9` — `measure_context_fill`, with `derive_context_fill` for one event, the one context reader orientation cost per stage imports and never copies
- **consumes-from** external — dPlacedRequest's landed `read_card_policy`, `read_session_id`'s `CARD_TRANSCRIPT` and `card-store.fixture.sh` (TOOL-dPlacedRequest-2 S7, S11, S12), and dGroundRules' landed catalogue rows
- **hands-off** `KICK-dKeptSession-30` — `measure_context_fill`, `derive_context_fill` and `CONTEXT_WINDOW_TOKENS`, which that unit re-points to the derived window (id 16)
- **hands-off** `KICK-dKeptSession-44` — the AC7 withdrawal and the `context-fill` scenario, its S35 and S39 (ids 13, 41), which this unit lands so both reduce to observations

## 4. Design

### Evidence

- `measure_ready_tree` sums a main usage event's `in`, `cache_read` and `cache_write` as its context,
  the one such sum in the kit (`tools/runlog/extract.py#measure_ready_tree`); `extract_session`
  yields those fields on every `usage` event with its `src` (`#_build_events`), and a `SessionTree`
  holding only `main` parses that file alone.
- Parsing the largest main transcript on node a, 232 MB, took 1.5 s main-only (PINNED 2026-11-21),
  and 5.5 s through `build_session_tree` with its agent files (PINNED, the same run at c2a407b0).
  Its last main usage read 287468 tokens, past the pinned window, as id 16 found (PINNED 2026-11-21).
- TOOL-dPlacedRequest-2 says the hook payload carries no context size; true of the payload, but the
  payload's `transcript_path` names a transcript that does (scout C's disagreement), and
  `read_session_id` keeps it.
- RT-1 moved the default to `fresh-at-boundary` in every preset, and v2's `[policies]` rows and the
  landed catalogue carry it; the CX-1 settlement's `compact-with-card` default was the earlier answer
  RT-1 revised.
- The fixture's replay plants match `context-*|partial-*|terminal-route` in one `case` arm, so a plant
  named `context-…` would run that arm.
- KICK-dKeptSession-1's landed `tools/policy/presets.toml` assigns `context.on-full` and
  `context.threshold` their catalogue defaults in all four presets, so AC8's two reads hold whether
  or not a policy file names a preset; `policy.py get` printed `fresh-at-boundary` and `60%` here at
  `79144f3f`.
- The harness on this node accepts `additionalContext` in a PreToolUse hook's output (F1).
- `help/reference/policy.md` is stale at this unit's base: it lists `card.pointers` under `## Not yet
  summarised` although its catalogue row carries both fields and `help/orientation-card.md` anchors it,
  since KICK-dKeptSession-69's reconcile merge dropped KICK-dKeptSession-13's re-render (PINNED
  2026-11-22, builder run `wf_b7427991-64d`). An observation, not a clause: S2's re-render carries it
  to its `Documented on` section with the two `context.*` keys.

### The lines

```
context — 72% of window · past 60% · fresh now, at this item boundary (context.on-full: fresh-at-boundary)
context — 72% of window · past 60% · fresh at next item boundary (context.on-full: fresh-at-boundary)
context — 41% of window · under 60%
context — 41% of window (context.on-full: compact-with-card)
context — skipped: runlog.py did not answer within 5s
```

The first is the boundary act's, the other four the replay's.

### The window

`CONTEXT_WINDOW_TOKENS = 200000` is one constant beside the sum, unverified against the platform's
documentation in this tree. Id 16 measured this node's main sessions well past it, so on this node
the share overstates the fill and the default threshold fires early. KICK-dKeptSession-30 replaces
it at order 13, and the build run lands both together at its close, so the constant never reaches
the default branch alone (F2).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `measure_context_fill`, `derive_context_fill`, `derive_context_tokens` | functions, `tools/runlog/extract.py` | `py.function`, OK by `lexicon.py --suggest` |
| `CONTEXT_WINDOW_TOKENS` | constant, `tools/runlog/extract.py` | none declared |
| `context`, `cmd_context` | subcommand of `runlog.py` and its handler | `py.function`, OK |
| `render_context_line`, `run_context_boundary` | shell functions, `manifest-check.sh` | `sh.function`, OK |
| `CARD_CONTEXT_BOUND` | constant, its env override the fixture's | none declared |
| `context —` | replay and boundary line | none |
| `context-fill` | `transcripts.json` scenario | none |
| the five plants of S7 | fixture cases | none |

### Migration

None. Two catalogue rows gain their text; no stored state changes.

### Rollout

Live at landing for a session whose harness passes `transcript_path`; the boundary act also needs a
card routing a build.

### Files touched (estimate)

- `tools/runlog/extract.py`: S1, `measure_ready_tree` re-pointed to `derive_context_tokens`
- `tools/runlog/runlog.py`: the `context` subcommand
- `tools/runlog/selftest.py`: S8's case and its `ASSERTION_FLOOR` raise
- `tools/runlog/fixtures/transcripts.json`: S8's scenario
- `tools/runlog/README.md`: S9's command line
- `skills/session-kickoff/manifest-check.sh`: S2 to S5
- `memory/guides/SESSION-KICKOFF.md`: the kickoff manifest, `last-audit` re-stamped, as `watch:`
  names `manifest-check.sh`
- `skills/session-kickoff/card-store.fixture.sh`: S7's plants and stubs
- `skills/session-kickoff/manifest-check.test.sh`: `FLOOR_ASSERTIONS` raised by the five plants
- `memory/map/generated/symbols.json`: the new Python and shell functions, regenerated by
  `gen_map.py --write`, which the bar's codebase-map leg grades
- `tools/policy/catalogue.toml`: the two rows' `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`: drained by `lists --write`
- `help/orientation-card.md`: S9, its paragraph and the two keys' usage anchors
- `help/reference/policy.md`: S2, re-rendered by `render_playbook.py --reference` once S9's anchors
  stand, never hand-edited
- `memory/project/docs-undocumented.txt`: S9, the rows `policy:context.on-full` and
  `policy:context.threshold` taken off

### Alternatives rejected

- **A copy of the sum in the shell.** The `[reuse]` rule and KICK-dKeptSession-9's import both need
  one reader.
- **The fill from the hook payload.** It carries none; the transcript it names does.
- **The whole session tree parsed.** Its agent files cost most of the parse and none can decide the
  owner's share.
- **A standalone transcript file as the runlog fixture.** The scenario store already writes main and
  agent files (round-1 audit L5).
- **The act at every tool call.** The clause acts at an item boundary; a tool call mid-item would end
  an item half done.

## 5. Production-readiness checklist

- security — the transcript is read, never written, and only its usage counts leave it: no message
  text reaches a line; the share printed is an integer the shell matches before comparing it.
- perf / scale — one bounded main-file parse per boundary crossing and per replay, measured above; a
  crossing happens at most once per commit, and the parse runs in the detached verb, so it stalls no
  shell call.
- error / empty / loading states — every replay failure prints `context — skipped: <why>`; at a
  boundary a failure prints nothing and acts on nothing.
- observability — every replay prints the fill and the value that decided it.
- risks — until KICK-dKeptSession-30 lands, a window larger than the pinned constant overstates the
  share; the run lands the two together. The boundary line reaches the session one shell call after
  the verb finishes, so a session that makes no further call that turn reads it at its next one.
- testing — S7's plants and S8's case, red and green.
- migration — none.
- user docs — `help/orientation-card.md`, S9; `help/reference/policy.md`, re-rendered by S2.

## 6. Acceptance criteria

- **AC1** — When the selftest case writes the `context-fill` scenario under a scratch projects root
  and runs `python tools/runlog/runlog.py context` over its main file, whose last main usage is `in`
  1000, `cache_read` 100000 and `cache_write` 19000, after an earlier main usage summing 180000 and
  before an agent file's usage summing 190000, it prints `60%`.
  figure: PINNED, the scenario's planted counts.
  Red when: a subagent's usage or an earlier turn decides the share.
- **AC2** — When `grep -n "derive_context_tokens" tools/runlog/extract.py` runs, it finds the
  definition and its calls from both `measure_ready_tree` and `measure_context_fill`, and `grep -c
  'ev\["in"\] + ev\["cache_read"\]' tools/runlog/extract.py` prints `1`.
  Red when: the sum is written twice.
- **AC3** — When `bash card-store.fixture.sh --plant fill-fresh-past` runs `--card --boundary` on a
  crossing under `fresh-at-boundary` and `60%` with the stub runlog answering `72%`, it prints
  `context — 72% of window · past 60% · fresh now, at this item boundary (context.on-full:
  fresh-at-boundary)`.
  Red when: a crossing past the threshold prints no line.
- **AC4** — When the plant `fill-under` runs the same crossing with the stub answering `41%`, no
  `context —` line prints; with no crossing at `72%`, none prints either.
  Red when: the line prints under the threshold, or away from a boundary.
- **AC5** — When the plant `fill-compact` sets `context.on-full` to `compact-with-card`, the crossing
  at `72%` prints no line and the stub policy kit's log shows `context.threshold` never read.
  Red when: `compact-with-card` acts, or reads the threshold.
- **AC6** — When the plant `fill-replay` replays a compaction under `fresh-at-boundary` at `72%`, the
  output carries `context — 72% of window · past 60% · fresh at next item boundary (context.on-full:
  fresh-at-boundary)` at a line after `position —` and before `now —`; under `compact-with-card` it
  reads `context — 72% of window (context.on-full: compact-with-card)`.
  Red when: the line is absent or out of I10's order.
- **AC8** — When `python tools/policy/policy.py get context.on-full` and `get context.threshold` run in
  a repository whose policy file sets neither, they print `fresh-at-boundary` and `60%`, which holds
  at base by dGroundRules' rows; after `policy.py lists --write`, `grep -c '^context\.'
  tools/policy/unsummarised-keys.txt` prints `0`.
  Red when: a default differs from v2's rows, or a row stays unsummarised.
- **AC9** — When `grep -n "context.on-full" help/orientation-card.md` runs, it finds S9's paragraph
  naming `fresh-at-boundary`, `compact-with-card` and `context.threshold`.
  Red when: the page does not describe the line.
- **AC10** — When the plant `fill-slow` replays with the stub runlog sleeping past a
  `CARD_CONTEXT_BOUND` the plant lowers, the output carries `context — skipped: runlog.py did not
  answer within` and still ends with its `now —` line.
  Red when: a slow parse prints nothing, or holds the replay past its bound.
- **AC11** — When `python tools/playbook/render_playbook.py --reference --check` runs at the unit's
  commit it exits 0; `grep -n -A1 'context\.on-full\|context\.threshold' help/reference/policy.md`
  shows each key's section followed by a line opening with the fixed string `Documented on
  [help/orientation-card.md]`, and no `- ` row naming it; `grep -cP
  '^policy:context\.' memory/project/docs-undocumented.txt` prints `0`; and the two keys' rows of
  `python tools/govkit/docs_leg.py --fingerprints` name `help/orientation-card.md` as their page.
  Red when: the reference page differs from its render, a key stays unsummarised there, or a
  `policy:context.*` row stays listed.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `policy fixtures` · `routed-commits selftest` · `runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `docs` · `help reference pages`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC3 AC4 AC5 AC6 AC10 · the boundary act and the replay line of the `fill-*` plants of `card-store.fixture.sh` over the stub runlog and policy kits, run by the suite's card-store block, the failing case a crossing past the threshold that prints nothing · `FLOOR_ASSERTIONS`, raised by one per new plant

New arm: tools/runlog/selftest.py · covers AC1 · the fill over the `context-fill` scenario, the failing case a later subagent usage read as the main session's · `ASSERTION_FLOOR`, raised by the case's checks and its three decoy checks

## 8. Open questions

- **FACT-QUESTION · F1 — Does a PreToolUse hook's output reach the model, so the boundary act's line
  is read?** Probe: read the installed harness's bundled hook-output schemas, `grep -a -o` over the
  `claude` on PATH for each `hookEventName` schema, and classify each event's schema by whether it
  carries `additionalContext`. Observation, `claude --version` 2.1.319 on node a, 2026-11-21:
  `PreToolUse` carries it, beside `permissionDecision`, and the harness yields it as a
  `hook_additional_context` message named `PreToolUse:<tool>`. Liveness: the same probe reads
  `CwdChanged` as lacking it, so it can return a negative. RESOLVED (agent, 2026-11-21, delegated):
  PreToolUse `hookSpecificOutput.additionalContext`, rung 2; the channel KICK-dKeptSession-13 S7's
  step emits, re-probed on the CLI this run uses. widens: none · relaxes: none
- **F2 — What is the window `context.threshold` is a share of?** Options: (a) one pinned constant,
  `CONTEXT_WINDOW_TOKENS`, until KICK-dKeptSession-30 derives it; (b) the derivation built here; (c) a new
  policy key. (c) is a key no clause names, a public surface outside this build's row; (b) is
  KICK-dKeptSession-30's whole unit, specced and audited at order 13. RESOLVED (agent, 2026-11-21,
  delegated): (a), rung 3; the round-1 audit's id 16 refutes the earlier reason, that the error runs
  towards the cheaper fresh start, and the choice now rests on the run landing unit 30 with this one,
  so no default branch carries the constant alone. widens: none · relaxes: none
- **F3 — Which default does `context.on-full` carry?** The CX-1 settlement says `compact-with-card`,
  and RT-1 later says `fresh-at-boundary`. RESOLVED (agent, 2026-10-26, delegated):
  `fresh-at-boundary`, rung 1, v2's row, the baseline, which carries RT-1's answer and the landed
  catalogue's default. widens: none · relaxes: none
- **F4 — Does this unit land the round-1 audit's L2 and L5 fixes, or leave them to
  KICK-dKeptSession-44?** Options: (a) here: AC7 withdrawn and S6 citing KICK-dKeptSession-13 AC5,
  and the `context-fill` scenario in place of a standalone transcript file; (b) as written, a
  standalone file and AC7 built here, deleted and withdrawn at order 30. RESOLVED (agent, 2026-11-21,
  delegated): (a), rung 3; it builds no file and no criterion only to remove it, and
  KICK-dKeptSession-44's AC34 holds on the scenario as built. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 14, CX-1, RT-1 and layer-runtime's
  owner-session rows, v2's two `[policies]` rows, and scout C's row and disagreement for this unit.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-30`, `KICK-dKeptSession-44`
  mirrored, the other ends of the edges the round-1 spec audit's promoted units declare; no other
  section moved.
- rev-3 · 2026-11-21 · §1 · S1 to S9 · §3 · §4 · §5 · AC1 · AC3 to AC6 · AC8 to AC10 · §7 · §8 F1 F2
  F4 · §10 · re-grounded on the landed dPlacedRequest, dDeclaredLoop and dGroundRules at base c2a407b0
  by 2026-11-21-prompt-KICK-dKeptSession-15-orders-11-12-reground-brief: every line citation
  re-cited by symbol or blob pin; S1 narrowed to the main file alone, parse cost pinned; S2 narrowed
  to the landed rows, the `core.py new policy-key` fallback dropped, the refusal made the landed
  `skipped` form; S3 prints nothing on a skip at a boundary; S4 reads `CARD_TRANSCRIPT`, no capture
  built, its slot before `now —`, which stays last (unit 12 rev-4 S5); S5, the bound, and AC10
  added after the replay's bounded-sibling rule; AC7 withdrawn and S6
  made NOT OBSERVED, and the standalone fixture replaced by S8's scenario, landing
  KICK-dKeptSession-44 S35 and S39 (F4); the plants renamed `fill-*` off the fixture's `context-*`
  arm and backed by a stub runlog kit; the manifest-check test file left out of Files touched, the
  suite running every listed plant; the runlog README added; F1 re-probed; F2's reason replaced; the
  edge from unit 15 added; `policy fixtures` and `routed-commits selftest` named.
- rev-4 · 2026-11-21 · S3 · S5 · S6 · S7 · §3 · §5 · fold of KICK-dKeptSession-13 rev-4 under
  2026-11-21-prompt-KICK-dKeptSession-15-orders-11-12-reground-brief: the boundary verb runs
  detached, so S3's line goes to its `--out` file and reaches the session at the next shell call
  after the verb finishes; S5's bound is the transcript read's own inside that verb, the hook bound
  gone; S6 names unit 13's `agent_id` skip beside `agent_type`; S7's boundary plants write their key
  into unit 13's stub plant file, no second loop stub; the edge and §5's perf and risks follow.
- rev-5 · 2026-11-21 · S4 · S7 · S8 · S9 · §4 · §7 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-26-precheck-brief`: `CARD_TRANSCRIPT` is read only with no
  `--session`, so the replay plants pipe their payload as the `replay` plant does; the stub
  `runlog.py` placed where the engine's resolver finds it, the fixture copying no runlog kit; the
  help page kept free of a `runlog.py` command, which the `docs` leg reds as `UNROWED`; AC8
  re-grounded on KICK-dKeptSession-1's presets; the kickoff manifest's re-stamp, both suites'
  floor raises and `symbols.json` added, the version bump left to the lander, and the plant arm
  homed in the suite that runs it.
- rev-6 · 2026-11-22 · S2 · S9 · §4 · §5 · AC11 · §7 · the builder's divergence resolved under
  `2026-11-22-prompt-KICK-dKeptSession-14-divergence-brief`: the two keys' usage anchors homed in
  S9's paragraph of `help/orientation-card.md`, their fingerprints taken at build time; the
  reference page re-rendered by S2 and the two `policy:context.*` rows of
  `memory/project/docs-undocumented.txt` drained by S9, both added to Files touched and observed by
  AC11; the stale `card.pointers` row kept in §4's Evidence as an observation; `docs` and `help reference
  pages` named.

## 10. Reuse audit

The seams extended are `measure_ready_tree`'s context sum (`tools/runlog/extract.py#measure_ready_tree`),
extracted into `derive_context_tokens` and called by both readers; `extract_session` over a
`SessionTree` holding one main file (`#extract_session`, `#SessionTree`); `runlog.py`'s subcommand
table (`tools/runlog/runlog.py#main`); the scenario store and its writer
(`tools/runlog/selftest.py#build_scenario`); `read_card_policy`, `read_session_id`'s
`CARD_TRANSCRIPT` and `derive_map_block`'s bounded call in `manifest-check.sh`; the card-store
fixture's stub kits (`skills/session-kickoff/card-store.fixture.sh#write_card_fixture`); and, for the
act and the line, KICK-dKeptSession-13's boundary verb and KICK-dKeptSession-12's replay order.
`python tools/codebase-map/reuse_lookup.py "measure how full the context window is from a session
transcript"` ranked `extract_session`, `resolve_session_tree` and `measure_ready_tree` in
`tools/runlog/extract.py`, the seam this unit extends, and `derive_context` in
`tools/playbook/tag_index.py` and `measure_typed_counts` in `tools/codebase-map/map_lib.py`, which
are unrelated name stems. Scout C's row agrees with source on the sum and on the replay hook's
matcher; its disagreement with TOOL-dPlacedRequest-2 is recorded in §4. The recall query returned
scout C's row, the CX-1 proposal it cites and KICK-dKeptSession-30's spec.

Recall terms used: `python tools/memory-recall/query.py "what does a session do when its context window fills past a threshold" --terms "context.on-full context.threshold fresh-at-boundary compact-with-card context fill window transcript item boundary RT-1"`
