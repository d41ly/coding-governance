# KICK-dKeptSession-47 — a compaction counts towards a model's window only when the session's last main usage before it is on that model

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 14 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 |
| [2026-10-26-build-KICK-dKeptSession-47-deviation-471.md](../build/2026-10-26-build-KICK-dKeptSession-47-deviation-471.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 16 at HIGH**, report item **H2**, which no other HIGH id shares. Id 44 is the
same defect at MEDIUM, item M25, batched into `KICK-dKeptSession-56`, whose item observes this fix.

`KICK-dKeptSession-30` S1 folds "the largest `pre_tokens` of the `compact` events" into every
model's observation, with no model filter. `extract_session` builds a compact event as `{t, kind,
src, trigger, pre_tokens}` and carries no `model` (`tools/runlog/extract.py:818-821`), while a usage
event carries one (`:834-836`). So one 1M compaction among the newest 20 transcripts puts every model
on the node on the 1M rung, the 95946-maximum `claude-opus-4-8` of unit 30 §4 included, and a
200k-window session of that model reads a fifth of its true fill. This unit ties each compaction to
the model it compacted. It repairs `KICK-dKeptSession-30` and builds one step after it (order 14).

## 2. Scope (IN)

- **S1** — id 16. The attribution. In `derive_context_window(model, root)`, a `compact` event joins
  `model`'s observation only when the newest main-source `usage` event before it in the same
  transcript's event list is on `model`. A compaction with no main usage before it joins no model.
  Observed by AC1 and AC2.
- **S2** — id 16. The fixture. One scenario in `tools/runlog/fixtures/transcripts.json`,
  `context-window-compact-other`: one main usage of 50000 tokens on `other-model`, then a compaction
  whose `compactMetadata.preTokens` is 900000, written the way the store's other scenarios are; and
  `context-window-compact-own`, the same with the usage on `fixture-model`. Observed by AC1 and AC2.
- **S3** — id 16. The sibling text superseded by name. `KICK-dKeptSession-30` S1 step 2's "and the
  largest `pre_tokens` of the `compact` events" reads as S1 here, and unit 30 §4 Evidence's "so the
  scan needs no new parser field" holds: the attribution reads only fields `extract_session` already
  yields. Answered in unit 30's acceptance ledger. Observed by AC1.

## 3. Non-goals (OUT)

- A `model` field on the compact event. The attribution is a fold over events the extractor already
  yields, so no parser field and no change to `extract_session`'s output.
- Two windows on one model: id 43, `KICK-dKeptSession-48`.
- The report's left-shift checklist entry, that an aggregate keyed by a field names where each folded
  event kind gets it. No clause of this build names that checklist; AC1 is its arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-30` — `derive_context_window`'s observation, whose compact events this unit attributes to a model (id 16)
- **hands-off** `KICK-dKeptSession-56` — the model-attributed compactions, which the batch's item for id 44, the same defect at MEDIUM, observes
- **hands-off** `KICK-dKeptSession-62` — the fold's compaction rule and its criteria, which the batch's S6, S11, S12, S25 and S26 bound by source and by a missing `pre_tokens` (ids 4, 12, 35, 34, 37)

## 4. Design

### Evidence

- The compact event: `events.append({"t": t, "kind": "compact", "src": src, "trigger": trigger,
  "pre_tokens": pre})` (`tools/runlog/extract.py:818-821`); the usage event carries `"model":
  model` (`:834-836`). Events are sorted by `t` (`:837`), so "the newest main usage before it" is a
  walk of one sorted list.
- Unit 30 §4 records eight compactions on this node between 834709 and 949239 `preTokens`, beside a
  95946 maximum on `claude-opus-4-8`: an unfiltered fold lifts that model to the 1M rung.

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
- `tools/runlog/selftest.py`: the cases of §6

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
- testing — the cases of §6 and the arm in §7.
- migration — none.
- user docs — none beyond unit 30 S5's paragraph, which names no compaction rule.

## 6. Acceptance criteria

The fixture is a scratch projects root under `%TEMP%` holding unit 30's `context-window` transcript
and S2's scenarios as each criterion says.

- **AC1** — When `runlog.py context` reads `context-window`, a 150000-token turn on `fixture-model`,
  from a root that also holds `context-window-compact-other`, it prints `75%` and the source
  `observed 150000 on fixture-model`.
  Red when: the other model's 900000 compaction lifts `fixture-model` to the 1M rung, printing `15%`.
- **AC2** — When the same read runs from a root that holds `context-window-compact-own` instead, it
  prints `15%` and the source `observed 900000 on fixture-model`.
  Red when: a copy dropping compactions entirely prints `75%`, so the filter removed the evidence
  along with the leak.

## 7. Gates

`runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/runlog/selftest.py · covers AC1 AC2 · an other-model compaction and an own-model one beside the 150000 turn, staged red by a copy of `extract.py` folding every compaction · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H2 (id 16).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is `extract_session`'s sorted event list (`tools/runlog/extract.py:818-837`), read
inside unit 30's `derive_context_window`; no parser field is added. `python
tools/codebase-map/reuse_lookup.py "attribute a compaction event to the model of the session it ran
in"` ranked `add_health_event`, `build_run_model` (`tools/runlog/model.py`), `extract_session` and
`resolve_session_tree`; `build_run_model` assembles a run's rows and attributes no compaction, and
`extract_session` is the seam named here.

Recall terms used: `python tools/memory-recall/query.py "which model does a compaction's
preTokens belong to" --terms "compact pre_tokens preTokens model usage window rung observation
extract_session derive_context_window attribution"`
