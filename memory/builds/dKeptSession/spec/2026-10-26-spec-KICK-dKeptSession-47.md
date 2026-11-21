# KICK-dKeptSession-47 — a compaction counts towards a model's window only when the session's last main usage before it is on that model

**Status:** DEFERRED · rev-5 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 14 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-47-deviation-471.md](../build/2026-10-26-build-KICK-dKeptSession-47-deviation-471.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-1 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-28-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-28-precheck-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-48 |
| [2026-11-21-prompt-KICK-dKeptSession-45-orders-14-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-45-orders-14-reground-brief.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-48 |
| [2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief.md) | research | KICK-dKeptSession-50 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-61 |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 16 at HIGH**, report item **H2**, which no other HIGH id shares. Id 44 is the
same defect at MEDIUM, item M25, batched into `KICK-dKeptSession-56`, whose item observes this fix.

`KICK-dKeptSession-30` S1 folds "the largest integer `pre_tokens` of its `compact` events" into
every model's observation, with no model filter. `_build_events` builds a compact event as `{t,
kind, src, trigger, pre_tokens}` and carries no `model`, while a usage event carries one
(`tools/runlog/extract.py#_build_events`). So one 1M compaction among the newest 20 transcripts
puts every model on the node on the 1M rung, the `claude-opus-4-8` of unit 30's 2026-10-26 probe
included, and a 200k-window session of that model reads a fifth of its true fill. This unit ties
each compaction to the model it compacted. It repairs `KICK-dKeptSession-30`, unbuilt at base
`c2a407b0` and built at order 13, and builds one step after it (order 14).

## 2. Scope (IN)

- **S1** — id 16. The attribution. In `derive_context_window(model, root=None, held=None)`, a
  `compact` event joins `model`'s observation only when the newest main-source `usage` event before
  it in the same transcript's event list is on `model`, the `held` events standing in for their file
  as unit 30 S1 has them. A compaction with no main usage before it joins no model. Observed by AC1
  and AC2.
- **S2** — id 16. The fixture. One scenario in `tools/runlog/fixtures/transcripts.json`,
  `context-window-compact-other`: one main usage of 50000 tokens on `other-model`, then a compaction
  whose `compactMetadata.preTokens` is 900000, written the way the store's other scenarios are, a
  key of its `scenarios` table holding an `about` string and a `main` list of records, the
  compaction a `system` record of subtype `compact_boundary` whose `timestamp` is later than the
  usage record's; and `context-window-compact-own`, the same with the usage on `fixture-model`.
  Observed by AC1 and AC2.
- **S3** — id 16. The sibling text superseded by name. `KICK-dKeptSession-30` S1 step 2's "and the
  largest integer `pre_tokens` of its `compact` events" reads as S1 here, and unit 30's Evidence
  bullet "so the scan needs no new parser field" holds: the attribution reads only fields
  `extract_session` already yields. Answered in this unit's own acceptance ledger,
  `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-47-1-acceptance-ledger.md`,
  which quotes unit 30 S1 step 2's passage, states S1 supersedes it, and quotes the Evidence bullet
  as standing. Unit 30 builds at order 13 and is CLOSED when this unit builds, so neither its spec
  nor its ledger is written (F1). Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- A `model` field on the compact event. The attribution is a fold over events the extractor already
  yields, so no parser field and no change to `extract_session`'s output.
- Two windows on one model: id 43, `KICK-dKeptSession-48`.
- The compaction's own `src`, a sidechain record and a non-integer `pre_tokens`:
  `KICK-dKeptSession-62` S11, S12 and S25.
- The report's left-shift checklist entry, that an aggregate keyed by a field names where each folded
  event kind gets it. No clause of this build names that checklist; AC1 is its arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-30` — `derive_context_window`'s observation, whose compact events this unit attributes to a model (id 16)
- **hands-off** `KICK-dKeptSession-56` — the model-attributed compactions, which the batch's item for id 44, the same defect at MEDIUM, observes
- **hands-off** `KICK-dKeptSession-62` — the fold's compaction rule and its criteria, which the batch's S6, S11, S12, S25 and S26 bound by source and by a missing `pre_tokens` (ids 4, 12, 35, 34, 37)

## 4. Design

### Evidence

- `_build_events` appends the compact event as `{"t": t, "kind": "compact", "src": src, "trigger":
  trigger, "pre_tokens": pre}` and the usage event with `"model": model`, then sorts every event by
  `t` (`tools/runlog/extract.py#_build_events`), so "the newest main usage before it" is a walk of
  one sorted list. Usage events are appended after every other kind and the sort is stable, so a
  compaction at the same instant as a usage sorts before it and finds no usage; S2's compaction is
  therefore timed after its usage. `_scan_record` reads `pre` from a `compact_boundary` record's
  `compactMetadata.preTokens` (`tools/runlog/extract.py#_scan_record`).
- No import is added: `record.py`, which the `policy fixtures` leg's runlog-record plant imports,
  imports `extract` at module level (`tools/runlog/record.py`).
- Unit 30's Evidence, as rev-3 pins it, holds 76 compaction records on this node (PINNED, 2026-11-21)
  whose `preTokens` lie between 208465 and 988875 (PINNED, 2026-11-21), and a 95946 main maximum on
  `claude-opus-4-8` from its earlier probe (PINNED, 2026-10-26): an unfiltered fold lifts that model
  to the 1M rung.
- `derive_context_window` is not in the tree at `c2a407b0` nor at the run's tree of 2026-11-21: unit
  30 mints it at order 13, so this unit edits unit 30's landed fold.

### The fold

```
for ev in events (sorted by t):
  usage, src main  -> last_model := ev.model ; observe(ev.model, derive_context_tokens(ev))
  compact          -> if last_model == model: observe(model, ev.pre_tokens)
```

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `context-window-compact-other`, `context-window-compact-own` | fixture scenarios | `tools/runlog/fixtures/transcripts.json` |

### Migration

None: no stored state holds a window.

### Files touched (estimate)

- `tools/runlog/extract.py`: S1 in `derive_context_window`
- `tools/runlog/fixtures/transcripts.json`: S2
- `tools/runlog/selftest.py`: the cases of the Acceptance criteria, one `test_` function, and the
  `ASSERTION_FLOOR` raise with its `RAISED` comment
- `memory/map/generated/symbols.json`: the case's `test_` function, regenerated by `gen_map.py
  --write`, which the bar's codebase-map leg grades
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-47-1-acceptance-ledger.md`:
  S3's answer beside the criteria observed

### Alternatives rejected

- **Dropping `pre_tokens` from the observation.** A compaction is the strongest evidence a window
  is large, and a fresh 1M session that compacted at 949k would lose it.
- **Counting compactions only from transcripts whose every usage is on `model`.** A session that
  switched model once would contribute nothing, and the newest-usage rule already answers which
  model was compacted.

## 5. Production-readiness checklist

- security — transcripts read only.
- perf / scale — one comparison per compact event, inside the walk unit 30 already makes.
- error / empty / loading states — a compaction with no prior main usage joins no model.
- observability — the source line still names the observation that set the rung.
- risks — a model switch inside one turn could attribute a compaction to the model switched to; the
  harness compacts between turns, so the newest usage is the compacted context's.
- testing — the cases of the Acceptance criteria and the arm on the Gates line.
- migration — none.
- user docs — none beyond unit 30 S5's paragraph, which names no compaction rule.

## 6. Acceptance criteria

The fixture is a scratch projects root under `%TEMP%` holding unit 30's `context-window` transcript
and S2's scenarios as each criterion says, each written by `build_scenario`
(`tools/runlog/selftest.py#build_scenario`). Every read runs with `CLAUDE_CODE_MAX_CONTEXT_TOKENS`
removed, as the selftest's `main` pops it since unit 30 S4, so unit 30's rung 1 decides nothing.

- **AC1** — When `runlog.py context` reads `context-window`, a 150000-token turn on `fixture-model`,
  from a root that also holds `context-window-compact-other`, it prints `75%` and the source
  `observed 150000 on fixture-model`.
  Red when: the other model's 900000 compaction lifts `fixture-model` to the 1M rung, printing `15%`.
- **AC2** — When the same read runs from a root that holds `context-window-compact-own` instead, it
  prints `15%` and the source `observed 900000 on fixture-model`.
  Red when: a copy dropping compactions entirely prints `75%`, so the filter removed the evidence
  along with the leak.
- **AC3** — `tr -s ' \r\n' ' '` over this unit's acceptance ledger piped into `grep -c "the largest
  integer"` prints `1`, and into `grep -c "so the scan needs no new parser field"` prints `1`; and
  `git diff --name-only <pass base> HEAD --` over unit 30's spec and its acceptance ledger prints
  nothing.
  Red when: S3's answer lands in a record of unit 30, or this unit's ledger quotes neither passage.

## 7. Gates

`runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `policy fixtures` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/runlog/selftest.py · covers AC1 AC2 · an other-model compaction and an own-model one beside the 150000 turn, staged red by a copy of `extract.py` folding every compaction · `ASSERTION_FLOOR`, raised by the case's checks and its three decoy checks

## 8. Open questions

- **F1 — Where is S3's answer to unit 30's superseded wording recorded?** Unit 30 builds at order
  13, one step before this unit, so it is CLOSED when this unit builds, and its ledger is in neither
  this unit's Files touched nor its write set. (a) Unit 30's acceptance ledger, a record of a closed
  unit written by a later one; (b) this unit's own acceptance ledger, quoting the unit 30 spec text
  it supersedes. Recommendation (b). RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a CLOSED
  unit's records are never written by a later unit, as KICK-dKeptSession-49 rev-6 ruled. Rejected:
  (a), writing the earlier unit's ledger. The main loop's ruling, in
  `2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H2 (id 16).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared
- rev-3 · 2026-11-21 · §1 · S2 · S3 · §3 · §4 · §5 · §6 · §7 · §10 · re-grounded on the run's BASE
  `c2a407b0` under the brief `2026-11-21-prompt-KICK-dKeptSession-45-orders-14-reground-brief`.
  Every line-number citation re-cited by symbol; the Gates line names `policy fixtures`, which
  `extract.py` trips; S3 quotes unit 30 S1 as rev-3 words it; the Evidence's compaction figures
  re-read from unit 30 rev-3 and pinned; S2 names the store's record shape; every read drops the
  ambient window variable. Narrowed: §3 hands the compaction's source and a missing `pre_tokens` to
  unit 62. No landed unit satisfies an item: unit 30 is unbuilt.
- rev-4 · 2026-11-21 · S1 · S2 · §4 · §6 · §7 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-28-precheck-brief`: S1 carries unit 30 rev-4's `held`
  events; S2's compaction timed after its usage, since `_build_events` sorts a same-instant usage
  after it and the compaction would then join no model; the policy fixture's import of `extract`
  shown unbroken; the floor raise and `symbols.json`, with the `recall floor` legs its path trips,
  added. No landed unit since base touched a cited symbol.
- rev-5 · 2026-11-21 · S3 · §4 · AC3 · §8 · S3's answer to unit 30 moves to this unit's own
  acceptance ledger, which joins Files touched, F1 resolved (b) and AC3 observing the quoted
  passages, under the brief `2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief`; the class of
  `KICK-dKeptSession-50`'s divergence, which unit 49's rev-6 first resolved.

## 10. Reuse audit

The seam extended is `_build_events`'s sorted event list (`tools/runlog/extract.py#_build_events`),
returned by `extract_session` and read inside unit 30's `derive_context_window`; no parser field is
added. Re-run at `c2a407b0`, `python tools/codebase-map/reuse_lookup.py "attribute a compaction
event to the model of the session it ran in"` ranked `add_health_event`, `build_run_model`
(`tools/runlog/model.py`), `extract_session` and `resolve_session_tree`; `build_run_model`
assembles a run's rows and attributes no compaction, and `extract_session` is the seam named here.
The recall query below returned this build's own specs 47 and 30; no landed unit attributes a
compaction to a model.

Recall terms used: `python tools/memory-recall/query.py "which model does a compaction's
preTokens belong to" --terms "compact pre_tokens preTokens model usage window rung observation
extract_session derive_context_window attribution"`
