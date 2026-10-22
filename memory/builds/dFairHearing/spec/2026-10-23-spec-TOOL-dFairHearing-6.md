# TOOL-dFairHearing-6 — items carrying a grade per id, ranked by the highest

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 7 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0073@242e109b whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

One defect makes one synthesis item whatever its findings' grades: each item carries the grade of
every confirmed id it holds, its severity is the highest of them, and the harness counts `blockers`
and `highs` from those per-id grades. Today the synthesis prompt says "merge findings of one binding
grade only", and it binds completely: same-address pairs with different binding grades were merged 0
times in 110, against 76% of same-grade pairs, and synthesizers named the split 29 times
(`gap-review-05`; PINNED 2026-10-15,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-review-adjudication.md:65-68`).

## 2. Scope (IN)

- **S1** — the synthesis schema's item gains `grades`, required, an object mapping each confirmed id
  the item holds, as a string key, to `BLOCKER`, `HIGH`, `MEDIUM` or `LOW`, in
  `tools/workflows/tier2-review.template.js`. Observed by AC5.
- **S2** — the synthesis prompt drops "merge findings of one binding grade only" and states one item
  per defect, each id's grade in `grades`, the item's `severity` the highest of its grades, and the
  report ranked by it. Observed by AC5.
- **S3** — the tally places each confirmed id at its own grade from `grades`, so `blockers`, `highs`
  and `regraded` are counted per id; an id whose grade is absent or illegal is placed at its item's
  `severity` and named in a warning. Observed by AC1, AC2, AC3.
- **S4** — an item whose `severity` is not the highest grade it places is named in a warning, and the
  counts stay per id. Observed by AC4.
- **S5** — the suite arms the `New arm:` line in §7 declares. Observed by AC1, AC2, AC3, AC4, AC5
  through that line, RED-first at the close.

## 3. Non-goals (OUT)

- No change to TOOL-dMergedTally-1's agreement rule: every confirmed id still sits in exactly one item,
  and a missing or repeated id still nulls both counts (template :1940-1946, :1972-1978).
- No grade applied to a whole item: that reverses `TOOL-aSightedSkeptic-6` §8 F2, as the research's
  candidate 5a measured (`…-research-review-adjudication.md:106`).
- No change to the binding grade or to `deriveBindingSeverity` (template :1507-1510); the skeptic's
  grade still binds, and a placement off it is still reported in `regraded`.
- No new field on the harness's return. The items are not returned today, and the two counts and
  `regraded` are what callers read; the new conditions are logged.
- No edit to `tools/roles/agents/gov-synthesizer.agent.md`. Its rule "One item per defect" already
  agrees with this unit, and its `returns:` line, each item with its severity and its ids, stays
  true. Its input line is `TOOL-dFairHearing-10`'s clause.
- No synthesis replay of the runtime rounds: the clause states no seen-red case, and the replays
  `TOOL-dFairHearing-1`'s clause owes do not include one.
- No help page: no page under `help/` describes the review harness.
- No kit version moved: the lander mints them (`tools/push-main.sh:26-32`).

### Edges

none

## 4. Design

### The schema and the prompt

The synthesis schema's item (template :1923-1933) becomes:

```js
required: ['severity', 'ids', 'grades'],
properties: {
  severity: { type: 'string', enum: ['BLOCKER', 'HIGH', 'MEDIUM', 'LOW'] },
  ids: { type: 'array', items: { type: 'integer' } },
  grades: { type: 'object' },
},
```

`grades` is typed only as an object, as the platform's schemas in this kit use no
`additionalProperties` map (`git grep additionalProperties -- 'tools/workflows/*.js'` finds only
`additionalProperties: true`), so the harness checks each entry itself, as it already does for
`severity` (template :1957-1962).

The grade sentence at template :1746-1748 is replaced. The new text says: make one item per defect,
the findings on one defect forming one item whatever their grades; give the item `grades`, mapping
each confirmed id to the grade it takes, its binding grade unless the synthesizer judges another grade
right, with the reason written beside that finding; set the item's `severity` to the highest of its
grades; and rank the report's items by that severity, blockers first. The item instruction at template
:1889-1897 names `grades` beside `ids`, says the harness counts `blockers` and `highs` from the per-id
grades, and keeps its exactly-one-item sentence. The report instruction at template :1749 keeps
"severity-ranked, blockers first".

### The tally

In the loop at template :1960-1971, for each item whose `severity` is legal and each confirmed id it
lists, the id's grade is `String(it.grades[String(id)]).toUpperCase()` when that is one of the four,
else the item's `severity`, and the id joins `gradesDefaulted`. `severityById` stores that per-id grade,
so `perRaw`, `blockers`, `highs` and `regraded` (template :1979-1991) read per id with no other change.
`perItem` still counts items by `severity`. An item whose `severity` differs from the highest grade it
placed joins `itemsMisranked`, named by its first confirmed id.

Two `WARNING:` log lines name them when non-empty:
`the synthesis gave <k> confirmed finding(s) no legal grade in their item's grades — placed at the
item's severity: ids <…>` and `<k> synthesis item(s) carry a severity other than the highest grade
they place — counts read the per-id grades: items holding ids <…>`.

`deriveLensYield` (template :1256-1277) still reads each item's `severity` for its legality and the
item's `ids` for ownership, so `defects` and `unique` stay counts of items.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `grades` | synthesis item field | none |
| `gradesDefaulted`, `itemsMisranked` | local arrays in the tally | none |

No function is minted.

### Migration

None. A synthesis written before this unit returned no `grades`; a stub or replay handing such items
to the new harness has each id placed at its item's severity and named, which is today's count.

### Rollout

Live on landing, not dark: the brief's S9 names units 2, 4, 7 and 8, and today's counts are what a
missing grade falls back to.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`, its render
- `tools/workflows/tier2-review.test.sh`

The render comes from `bash tools/workflows/check-protocol-parity.test.sh --render`. The suite's
synthesis stubs (`tools/workflows/tier2-review.test.sh:377-379` and the tally arms that hand `items`)
gain `grades` where an arm asserts a per-id count, and keep none where an arm asserts the fallback.

### Alternatives rejected

- **The item's grade applied to every id.** Raw highs rise by 4 and 6 on the two runtime runs and the
  off-binding warning fires on every mixed item (the research's candidate 5a).
- **Grades as an array of `{id, grade}`.** It spells S6 of the brief another way, and a JSON object keyed
  by id cannot name one id twice.
- **The harness deriving `severity` from the grades and ignoring the agent's.** The report the agent
  wrote ranks by the agent's value, so a silent override would leave the record and the return
  disagreeing; the warning names the disagreement instead.

## 5. Production-readiness checklist

- security — no new write path; one more agent-returned field, checked against a closed set before
  it is counted.
- perf / scale — one lookup per confirmed id in the existing loop.
- error / empty / loading states — a missing or illegal grade falls back to the item's severity and is
  named; a missing or repeated id still nulls both counts; no synthesis still returns no counts.
- observability — the two warnings name every defaulted id and every misranked item.
- risks — a mixed-grade item reports one severity for findings of several, so a reader ranking by item
  sees the highest; the per-id counts and `regraded` keep the rest visible.
- testing — the pass probes S1 to S4 by a stub-agent run; the suite arm in §7 is observed RED then
  GREEN by the main loop at the close.
- migration — none, as §4 Migration says.
- user docs — none owed: no page under `help/` describes the review harness.

## 6. Acceptance criteria

- **AC1** — When a scratch stub-agent run of `tools/workflows/tier2-review.js`, shaped as
  `tools/workflows/tier2-review.test.sh:333-357`, has a diff review's skeptics confirm id 1 at
  `blocker` and id 2 at `medium` and refute the rest, and its synthesis stub returns one item
  `{severity: 'BLOCKER', ids: [1, 2], grades: {'1': 'BLOCKER', '2': 'MEDIUM'}}`, the return reads
  `blockers` 1, `highs` 0 and `regraded` `[]`, and no log line names a placement off the binding
  grade. The same stub with id 1 also listed in a second item returns `blockers` and `highs` null.
  Red when: the tally still places every id at its item's severity, so `blockers` reads 2 and
  `regraded` reads `[2]`.
  cost: a scratch runner of about 60 lines, modelled on that suite's stubs.
- **AC2** — When the AC1 stub gives id 2 the grade `HIGH`, the return reads `highs` 1 and `regraded`
  `[2]`.
  Red when: `regraded` compares the item's severity, so id 2 is not named.
- **AC3** — When the AC1 stub returns the item with `grades` `{'1': 'BLOCKER'}`, and again with
  `{'1': 'BLOCKER', '2': 'severe'}`, id 2 is placed at `BLOCKER`, `blockers` reads 2, and a
  `WARNING:` line names `ids 2` as given no legal grade.
  Red when: an id with no legal grade is left unplaced, so the tally fault fires and both counts
  read null.
- **AC4** — When the AC1 stub returns `{severity: 'MEDIUM', ids: [1, 2], grades: {'1': 'BLOCKER',
  '2': 'MEDIUM'}}`, `blockers` reads 1 and a `WARNING:` line names the item holding id 1 as carrying a
  severity other than its highest grade.
  Red when: the misranked item passes unannounced.
- **AC5** — When `grep -c 'merge findings of one binding grade only'` runs over
  `tools/workflows/tier2-review.template.js` and `tools/workflows/tier2-review.js`, each prints 0; the
  AC1 run's synthesis prompt carries `one item per defect` and `grades`; and its synthesis call's
  schema lists `grades` among the item's required keys.
  Red when: the new sentence is added and the old one kept, so the prompt asks for both.

## 7. Gates

`tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `review-join ban (no ref-keyed join)` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the base harness, whose tally places each id at its item's severity and whose prompt still merges findings of one binding grade only · FLOOR_ASSERTIONS in that suite, raised by the arms added

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`, joined by the header
  regex at `tools/memory-tree/tree_lib.py:377`. Observation, 2026-10-23: `DRAFT` is not in the set, so
  a `DRAFT` header parses as no header and the unit reads MISSING. Liveness: the tuple would carry it
  if the vocabulary admitted it. RESOLVED (agent, 2026-10-23, delegated): `OPEN`, the token
  `memory/TEMPLATE-SPEC.md` gives a spec in drafting.
- **F2 — What does the tally do with a confirmed id whose grade is absent or illegal?** Options: (a)
  place it at its item's severity, today's count, and name it; (b) treat it as unplaced, so the tally
  fault nulls both counts. (b) returns no count for a run whose every id is placed, over one omitted
  field, and the disposal guard then refuses an honest synthesis; (a) is the item's own stated grade,
  never one the harness invents. RESOLVED (agent, 2026-10-23, delegated): (a), by fewer open
  questions, rung 3.
- **F3 — What does the harness do with an item whose `severity` is not its highest grade?** Options:
  (a) warn and count per id; (b) a tally fault; (c) overwrite the severity. The counts do not read the
  item's severity, so (b) withholds a count nothing is wrong with, and (c) makes the return disagree
  with the report the agent wrote. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3.
- **F4 — The brief's S6 says `TOOL-dFairHearing-7` reads `grades`; does it?** That unit hands the
  synthesis refuted claims and same-address pairs and validates the twins it flags by id and verdict,
  and no part of it reads a grade. RESOLVED (agent, 2026-10-23, delegated): no reader, so no edge, by
  rung 3.

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, from the packet's Items 6, the review system record's
  grade-per-id change, and the synthesis prompt and tally read at base `3708a705`.

## 10. Reuse audit

The seams extended are the synthesis's own: its item schema (`tools/workflows/tier2-review.template.js:1914-1936`),
its grade and item instructions (:1746-1748, :1889-1897) and the per-id tally TOOL-dMergedTally-1 built
(:1940-1992), whose `severityById` already holds one grade per id and only needs it read from the
item's `grades`. No second tally. `python tools/codebase-map/reuse_lookup.py "tally blockers and
highs from synthesis items placing each confirmed finding"` ranked name stems
(`render_charter_blocks`, `build_baseline_findings`, `confirm_blobs`) and named no seam in the review
harness, so the seam was found by reading the source. `python tools/memory-recall/query.py` returned
TOOL-dMergedTally-1's ask, the research's synthesis measures, `TOOL-aSightedSkeptic-6` and a closing
review that names the split by grade (`memory/builds/aOrientedCast/reviews/2026-10-12-review-TOOL-aOrientedCast-1-closing-diff-round1.md:24`).
Each agrees with source; the research cites the merge sentence at `:1678`, which sits at template
:1746-1748 at base, the file having grown since.

Recall terms used: synthesis item binding grade merge one defect split tally blockers highs regraded items ids
