# TOOL-dScopedBuild-13 — the closing review handed each unit's acceptance criteria and MUST seams as rows every finder answers, recorded, gating once measured

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 15 · advances TOOL-dScopedBuild-16

**Carries:** cl-dClosedLoop-0411@78cc90dd whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-spec-stage-returns.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-build-TOOL-dScopedBuild-2-reuse-scout-c.md](../build/2026-11-01-build-TOOL-dScopedBuild-2-reuse-scout-c.md) | research | TOOL-dScopedBuild-2 TOOL-dScopedBuild-4 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-fix-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-3 TOOL-dScopedBuild-6 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-1-spec-brief.md) | research | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 |
| [2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-1 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 |

<!-- /gen:spec-records -->

## 1. Goal

The closing review is handed the build's range alone, never the criteria or seams its finders must
answer, though the verifier's packet allows them (gap-flow-22,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:128`).
`tier2-review.js` takes `specs` as free intent documents (`tools/workflows/tier2-review.template.js:116`)
and its `intent` lens asks for "an acceptance criterion with no code behind it" (`:798`) with nothing
handed and nothing required. This unit hands the closing review, beside its range, one row per
acceptance criterion and per MUST seam of each unit it covers, and the rows a fix pass disputed;
every finder answers every row; the answers are joined and recorded on every review; and the rows
gate only once a measurement passes, recorded at gate `record` until then (NT-10,
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:197-199`).

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: the row grammar, `join_upstream(rows,
answers, gate)`, its finding line `upstream · finding · <class> · <row id>` and the record of S8,
`memory/builds/<slug>/build/<date>-build-<unit id>-upstream-<n>.md` bound `**Serves:** journal <unit
id>` (TOOL-dDeclaredLoop-29 S3, S6, S8, of dDeclaredLoop, a parent of dIndexedDesign); the per-order
return schema `render_return_schema` and its CLI `handoff.py return-schema --role <slot> --upstream
<rows file> --part rows`, with the merge shape `addUpstreamSchema` gives the unit harness
(TOOL-dFurnishedOrders-19 S4, S7, S8, of dFurnishedOrders, a parent); `read_spec_musts` and
`read_reuse_records` (TOOL-dScopedBuild-12); `check_closing_review_recorded` (TOOL-dScopedBuild-4).

- **S1** — One acceptance reader. `AC_HEAD`, `AC_LABEL` and `extract_acceptance` move from
  `tools/check-spec-tokens.py` (`:365`, `:369`, `:539`) into `tools/memory-tree/design_lib.py` beside
  `read_spec_writes`, and the checker binds the three from the `design_lib` it already loads by path
  (`load_design_lib`, `:866`, as `SPEC_DATE` is bound, `:349-350`), so the checker, this unit and any other
  reader of a spec's §6 read one function. `read_spec_criteria(text)` in `design_lib.py` returns
  `[(label, first line)]`, split at `AC_LABEL`. Observed by AC1.
- **S2** — The rows. `python review_rows.py rows <slug> [--unit <id>]… --out <file>` in
  `tools/workflows/review_rows.py` writes the rows file in TOOL-dDeclaredLoop-29 §4's line form,
  `<row id> · <kind> · <text>`, for each unit named, or with no `--unit` each roster unit with an
  attributed commit in the review's range: `criterion-<unit id>-AC<n> · criterion · <the criterion's
  first line>` per `read_spec_criteria` row; `seam-<unit id>-<n> · seam · <path> :: <symbol>` per
  `read_spec_musts` row; and `dispute-<unit id>-<k> · finding · <path>::<name> disputed: <reason>`
  per `## Disputed` line `read_reuse_records` returns for the unit's newest head. A unit's spec with
  no acceptance section refuses, naming the unit, exit 2. Observed by AC2.
- **S3** — The hand-off (I14). `tier2-review.template.js`, rendered to `tier2-review.js`, takes
  `upstream: [{id, kind, text}]` beside `priorFindings` (`:293`), legal on the diff kind only and
  refused on a spec audit naming the field. Each finder prompt carries, after the prior-findings block
  (`:1161-1168`), an `UPSTREAM ROWS` block listing `- <id> · <kind> · <text>` and the contract: answer
  every row exactly once, `used`, `bypassed` or `not-applicable` with a reason, `used` meaning the
  range meets the criterion, calls the seam or upholds the dispute, and `bypassed` that it misses the
  criterion, builds beside the seam or leaves the duplicate standing. `upstream` joins `inputPrint`
  (`:985`) only when non-empty, so a review handed no rows keeps its key. Observed by AC3.
- **S4** — The schema. `tier2-review` takes `returnRows`, the `--part rows` line of TOOL-dFurnishedOrders-19
  S7, and merges its `upstream` property into `FINDING_SCHEMA` (`:630`) and its `required` list, as
  that unit's `addUpstreamSchema` merges into the unit harness's schema; `upstream` without
  `returnRows`, or a `returnRows` whose row ids differ from `upstream`'s, throws before any agent.
  The rule that renders the schema stays in `render_return_schema`; the harness only merges what it is
  handed. Observed by AC4.
- **S5** — The answers returned. The harness's return gains `upstream: [{lens, answers}]`, each finder
  lens's `upstream` array, on every exit path, `[]` when no rows were handed. Observed by AC4.
- **S6** — The join and the record. `python review_rows.py join <slug> --rows <file> --result <file>
  --write` reads the harness return, and for each unit and each lens calls `join_upstream` over that
  unit's rows and that lens's answers, at S7's gate; a row any lens left unanswered is a finding of
  that lens, in the unanswered-row class TOOL-dDeclaredLoop-29 S6 names. It writes each unit's answers and findings into TOOL-dDeclaredLoop-29 S8's record
  through that unit's writer, never a second one, prints each finding line, and exits 1 when a
  `measured` gate refuses, else 0. Observed by AC5 and AC6.
- **S7** — The gate. `derive_review_gate(root)` in `review_rows.py` returns `record`, unless its
  constant `MEASURED`, empty at landing, names `{"measured-by": <path>, "measured-line": <line>}`, a
  record git tracks at HEAD holding that line, when it returns `measured`; a `MEASURED` whose record
  lacks its line refuses, exit 2, as TOOL-dDeclaredLoop-29 S2's loader refuses such an entry. No gov
  value ships `measured`. Observed by AC6.
- **S8** — Recorded at the exit. `check_closing_review_recorded` gains a third term per owed subject:
  each unit the subject covers has a tracked `…-<unit id>-upstream-<n>.md` record committed inside the
  subject's range, and, where `derive_review_gate` reads `measured`, the newest such record holds no
  `upstream · finding · <class>` line, `<class>` any of the five classes TOOL-dDeclaredLoop-29 S6
  grades. The term reads `review_rows.py` through `resolve_kit_dir` and prints `rows: not-installed`
  where the workflows kit is absent. Observed by AC7.
- **S9** — Where it runs. M8's call (`tools/memory-tree/BUILD-METHOD.template.md:262-265`, rendered to
  `memory/guides/BUILD-METHOD.md`) gains one args line,
  `upstream: <rows>, returnRows: '<the rows line>',` at the call's indent (68 bytes with its
  newline), and after the call's paragraph one
  sentence, "Before the call `review_rows.py rows <slug> --out <file>` writes the rows handed as
  `upstream`; after it `review_rows.py join <slug> --rows <file> --result <file> --write` records
  each finder's answers." (203 bytes with its leading space): +271 bytes to the render, which with
  TOOL-dScopedBuild-2's +100 sums to 371 of the 1366 M1's 30720-byte budget leaves at 29354; the attended Skill's Stage 6
  (`tools/roles/SKILL.template.md:74-80`, rendered to `.claude/skills/build/SKILL.md`) says the same.
  Observed by AC8.
- **S10** — The fixture and its leg. `python review_rows.py --fixture --plant <case>` builds a scratch
  build of two units and runs each case of §6 against its expected line; the leg `review rows fixtures`,
  argv `python {prefix}/workflows/review_rows.py --fixture`, guard `{prefix}/workflows/review_rows.py`,
  declared in `tools/workflows/kit.toml` and rendered into `tools/gate-legs.json`. Observed by AC2, AC5
  and AC6.
- **S11** — The docs. `tools/workflows/README.md`'s argument list names `upstream`, `returnRows` and
  the `upstream` return field, and `help/roles.md` says the closing review is handed each unit's
  criteria and MUST seams as rows. Observed by AC8.

## 3. Non-goals (OUT)

- No gating at landing: the rows gate only once a measurement passes, and that measurement, rank 2's
  plan of 20 to 30 past builds with a held-out set
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-scoutedseam-apply.md`
  §6), is not this unit's; arming `MEASURED` is a later commit citing its record.
- No new lens and no change to a lens brief: every finder answers the rows through the block and the
  schema, the `intent` lens's brief unchanged.
- No row deriver in the loop kit: the rows come from the specs and the reuse-check records, not from an
  upstream item's `## Establishes`, so no `upstream` entry is added to `tools/loop/loop.toml`, whose
  hand-on would refuse an item with no return (TOOL-dDeclaredLoop-29 S4).
- No spec-audit rows: the clause names the closing review.
- No skeptic or synthesis answers: the clause names the finders.

### Edges

- **consumes-from** `TOOL-dScopedBuild-12` — `read_spec_musts`, the one MUST-seam reader, and `read_reuse_records`, whose `## Disputed` rows become finding rows; without them the review is handed criteria alone
- **consumes-from** `TOOL-dScopedBuild-4` — `check_closing_review_recorded`, the predicate both exits run, which this unit extends with the rows' record term
- **consumes-from** external — TOOL-dDeclaredLoop-29 S3, S6, S8 (`join_upstream` and the record) and TOOL-dFurnishedOrders-19 S4, S7, S8 (`render_return_schema`, `handoff.py return-schema`), specced and DEFERRED at base
- **hands-off** `TOOL-dScopedBuild-35` — S8's third term against the earlier exits' fixtures, S2; S10's leg claimed in `memory/map/features/review-harnesses.md`, S16; and the two suites of `tools/check-spec-tokens.py` this unit's pass owes, `memory-hygiene self-test` and `spec-tokens self-test`, S38 (ids 5, 32, 35)

## 4. Design

### The flow

```
closing review owed (TOOL-dScopedBuild-4's subjects)
  -> review_rows.py rows <slug> [--unit <id>] --out rows.txt
  -> handoff.py return-schema --role gov-diff-reviewer --upstream rows.txt --part rows   # returnRows
  -> Workflow tier2-review.js { base, head, upstream: <rows as objects>, returnRows, ... }
       each finder: the UPSTREAM ROWS block, its schema requiring one answer per row
  -> review_rows.py join <slug> --rows rows.txt --result <return json> --write
       per unit, per lens: join_upstream -> the upstream record, finding lines
  -> --build-exit / --close: check_closing_review_recorded, its third term the record per unit
```

### The rows

```
criterion-TOOL-dScopedBuild-3-AC1 · criterion · When `routed_commits.py` runs over a planted stray commit under `refuse`, it exits 1.
seam-TOOL-dScopedBuild-3-1 · seam · tools/memory-tree/design_lib.py :: check_guard_trips
dispute-TOOL-dScopedBuild-3-1 · finding · tools/memory-tree/routed_commits.py::check_scope disputed: grades a pass, not a push
```

A row id is qualified by its unit, because one per-build review hands several units' `AC1` and
`seam-1`; the I14 spellings `criterion-<unit id>-AC<n>` and `seam-<n>` are kept, the second qualified
as `seam-<unit id>-<n>`, a refinement this unit owns. The text is the criterion's first line, which
carries its ledger token before the line wraps (hygiene check 23), so a row names its observation.

### The answers

A finder's return keeps `lens`, `path` and `findings`, and gains the `upstream` array its schema
requires, `{id, answer, reason}` per row, `id` one of the handed ids (TOOL-dFurnishedOrders-19 S4). A
`bypassed` answer is also a finding through `join_upstream` (TOOL-dDeclaredLoop-29 S7) and is recorded;
it is not merged into the review's own findings, which its skeptics verify by file and line.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_spec_criteria` | function, `design_lib.py` | `py.function`, `--suggest` OK |
| `AC_HEAD`, `AC_LABEL`, `extract_acceptance` | moved into `design_lib.py`, unchanged | as at base |
| `derive_review_rows`, `derive_review_gate`, `check_review_answers` | functions, `review_rows.py` | `py.function`, `--suggest` OK |
| `MEASURED` | constant, `review_rows.py`, empty | none declared |
| `rows`, `join`, `--fixture` | `review_rows.py` CLI modes | none |
| `upstream`, `returnRows` | `tier2-review` arguments; `upstream` also a return field | none |
| `renderUpstream` | JS function, the prompt block | `js.function`, `--suggest` OK |
| `review rows fixtures` | gate leg, `tools/workflows/kit.toml` | none |

### Migration

None. A review handed no `upstream` renders byte-identical prompts, keeps its input print and returns
`upstream: []`. The checker's three names keep their values and its output does not move.

### Rollout

Live at landing for every closing review composed through M8 or the Skill after it; the exit's
third term refuses a build closing after landing whose review handed no rows.

### Files touched (estimate)

- `tools/workflows/review_rows.py` (new)
- `tools/workflows/tier2-review.template.js`, rendered to `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/kit.toml`: the module and the leg `review rows fixtures`
- `tools/gate-legs.json`: rendered from the kits' declarations
- `tools/workflows/README.md`
- `tools/memory-tree/design_lib.py`
- `tools/check-spec-tokens.py`
- `tools/unattended/unattended.sh`: the third term of `check_closing_review_recorded`
- `tools/unattended/unattended.test.sh`
- `tools/memory-tree/BUILD-METHOD.template.md`, rendered to `memory/guides/BUILD-METHOD.md`
- `tools/roles/SKILL.template.md`, rendered to `.claude/skills/build/SKILL.md`
- `help/roles.md`

### Alternatives rejected

- **Deriving the rows through `derive_upstream_rows` and a `tools/loop/loop.toml` entry.** Rejected by
  reading TOOL-dDeclaredLoop-29 S4: it reads an upstream item's return's `## Establishes` section and
  refuses a named item with no return, and no item's return carries a spec's criteria; the rows here
  are read from the specs.
- **Building the answer schema in JavaScript from the rows.** A second copy of
  `render_return_schema`'s rule in another language; the harness merges the property the Python
  renderer hands it.
- **Answering only in the `intent` lens.** Rank 2's measurement plan isolates the intent finder to
  measure it (`research-scoutedseam-apply.md` §6); the clause says each finder answers.
- **Loading `extract_acceptance` from `tools/check-spec-tokens.py` by path.** The checker sits at the
  tool root and no kit ships it, so an adopter's review would hand no criterion rows; the move puts
  the reader in the kit both callers already load.
- **The verbs `met|missed|not-applicable` for criterion rows** (rank 2's plan). A second answer set
  `join_upstream` grades as `bad-answer`; one vocabulary, its meaning per kind stated in the contract.

## 5. Production-readiness checklist

- security: row text is copied from tracked specs and records into a prompt and a record; the record is
  written through TOOL-dDeclaredLoop-29's writer, and answers are held to the handed ids by the schema.
- perf / scale: rows grow with criteria, about 10 to 20 per unit; every finder answers every row, five
  lenses on a full review.
- error / empty / loading states: no rows hands nothing and changes nothing; a spec with no §6 refuses;
  a refused finder return comes back null and is handled as a lens that returned nothing is today.
- observability: each finding line printed; one record per unit per review.
- risks: M8 sits near its byte budget (29354 of 30720 at base); S9 adds 271 bytes and
  TOOL-dScopedBuild-2 100, 371 in all, and the build run measures the rendered file before the commit.
- testing: `review_rows.py --fixture`; the tier2-review suite's stubbed-agent arms; the driver arm.
- migration: none (§4).
- user docs: `tools/workflows/README.md`, `help/roles.md` (S11).

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe loads `tools/check-spec-tokens.py` by path beside `design_lib`,
  the checker's `extract_acceptance`, `AC_HEAD` and `AC_LABEL` are the very objects `design_lib`
  holds, the checker defines none of the three itself, and `design_lib.read_spec_criteria` over a
  fixture spec of three criteria returns three `(label, line)` pairs.
  Red when: the checker keeps a second `AC_LABEL`, or the move changes a verdict.
- **AC2** — When `python review_rows.py --fixture --plant rows` derives the rows of a fixture unit
  whose spec has three criteria, one `MUST` line and one `SHOULD` line, and whose reuse-check record
  disputes one row, it writes three `criterion-` rows, one `seam-` row and one `dispute-` row; over a
  spec with no acceptance section it exits 2 naming the unit.
  Red when: a SHOULD seam is handed, or a missing §6 hands zero rows silently.
- **AC3** — When a `node -e` probe evaluates `tier2-review.js` with a stub `agent` and `upstream`
  holding two rows on the diff kind, every finder prompt carries `UPSTREAM ROWS` with both ids and the
  three answers; with no `upstream` the prompts and the input print equal base's; on the spec-audit
  kind `upstream` throws naming the field.
  Red when: a review handed no rows changes its key, so a resume reuses no lens file.
- **AC4** — When the same probe passes a `returnRows` line from `handoff.py return-schema --part rows`,
  the schema the stub receives requires `upstream` with an `id` enum of exactly the two ids, the
  harness's return carries `upstream` with each lens's answers, and a `returnRows` naming a third id
  throws before any agent.
  Red when: the schema is built in the harness from the rows, or a mismatched pair reaches a finder.
- **AC5** — When `python review_rows.py --fixture --plant unanswered` joins a planted finder return
  that answers one of two handed rows, it prints `upstream · finding · dropped ·` naming the unanswered
  row and the lens, writes the record holding it, and exits 0 at gate `record`.
  Red when: the unanswered row is silent, which is the clause's planted case.
- **AC6** — When the same plant runs with `MEASURED` set to a fixture record holding its line, the
  join exits 1 on the `dropped` row; with the record lacking the line it exits 2 naming
  `measured-line`.
  Red when: the gate reads `measured` from the constant alone, with no measurement behind it.
- **AC7** — When `bash unattended.sh --close tRun` runs in a fixture whose closing review is met and
  one covered unit has no upstream record in range, `closing-review-recorded` is unmet naming the unit
  and `upstream`; with the record it is met; with `MEASURED` armed and the record holding a `dropped`
  finding line it is unmet.
  Red when: a review that recorded no rows meets the exit.
  fixture: the driver suite's preflighted slug fixture, the workflows kit beside it.
- **AC8** — When `grep -n "review_rows.py" memory/guides/BUILD-METHOD.md .claude/skills/build/SKILL.md
  tools/workflows/README.md` and `grep -n "criteria" help/roles.md` run, each prints the sentence S9
  or S11 names, and `wc -c memory/guides/BUILD-METHOD.md` prints at most 30720.
  Red when: the render and its template differ, or M8 passes its budget.

## 7. Gates

`tier2-review self-test` · `review-join self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `kit/dogfood doc parity` · `check-wiring self-test` · `lexicon naming predicates` · `measure-legs selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `build-index selftest` · `unattended kit gate` · `memory hygiene` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/review_rows.py · covers AC2 AC5 AC6 · the leg `review rows fixtures`, `review_rows.py --fixture` over each plant, staged by joining only the answered ids · none

New arm: tools/workflows/tier2-review.test.sh · covers AC3 AC4 · the stubbed-agent runs with and without `upstream`, staged by leaving `upstream` out of the input print · none

New arm: tools/unattended/unattended.test.sh · covers AC7 · the fixture close with a covered unit lacking its upstream record, staged by removing the third term · none

## 8. Open questions

- **F1 — Which finders answer the rows?** Options: (a) every finder lens; (b) the `intent` lens alone;
  (c) the synthesis. (b) is rank 2's measurement arm, not the clause, and (c) answers after the
  skeptics, with no lens's reading behind it. RESOLVED (agent, 2026-11-01, delegated): (a), rung 1,
  the clause's "rows each finder answers". widens: none · relaxes: none
- **F2 — Where is the gate declared until a measurement exists?** Options: (a) a `MEASURED` constant
  in `review_rows.py`, empty at landing, armed by a later commit naming a tracked record and its line;
  (b) an `upstream` entry on `item.review.lens` in `tools/loop/loop.toml`; (c) a new policy key. (b)
  makes the loop's hand-on derive rows from returns that hold none and refuse (TOOL-dDeclaredLoop-29
  S4); (c) is a public surface no clause of this build names (veto 2). RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, the survivor, the arming checked as TOOL-dDeclaredLoop-29 S2 checks a
  `measured` entry. widens: none · relaxes: none
- **F3 — How are the answers enforced at the finder?** Options: (a) the per-order schema
  TOOL-dFurnishedOrders-19 renders, merged into `FINDING_SCHEMA`, and the join after; (b) the join
  alone; (c) a JavaScript schema built from the rows. (b) lets a finder skip the rows until the record
  shows it, and (c) copies a rule another kit owns. RESOLVED (agent, 2026-11-01, delegated): (a), rung
  3, the most feature-rich survivor, reusing the parent's renderer. widens: none · relaxes: none
- **F4 — Does TOOL-dDeclaredLoop-29 S8's writer take rows and answers a caller derived?** Options: (a)
  call its writer with this unit's rows and answers, and ask dDeclaredLoop that the writer accept them;
  (b) write the record here. (b) is a second writer of one record kind. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, with an ask for the main loop to file once, target dDeclaredLoop's
  `BACKLOG.md`: "THE UPSTREAM RECORD'S WRITER TAKES ONLY ITEM RETURNS. TOOL-dDeclaredLoop-29 S8 writes
  `…-upstream-<n>.md` from `upstream.py join --write <slug> <unit id>`, and TOOL-dScopedBuild-13 joins
  rows it derives from the specs and answers a review harness returns, which no item return holds",
  accept "the S8 writer is callable with a rows file and an answers file a caller supplies, seen on a
  fixture join whose rows came from no item return". widens: none · relaxes: none
- **F5 — Where does `extract_acceptance` live once two readers need it?** Options: (a) moved into
  `design_lib.py` with `AC_HEAD` and `AC_LABEL`, the checker binding them; (b) loaded from the checker
  by path; (c) a copy in `review_rows.py`. (b) hands an adopter no criteria, the checker shipping in no
  kit; (c) is a second copy. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the factory at the
  kind's second instance. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 13, night-pass-two:197-199, :214 and
  :349-350, research-scoutedseam-apply §6 rank 2, gap-register:128, scout C's row 13 and its interfaces
  7 to 11, and the spec brief's I13, I14 and I15.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-35, promoted by the round-1 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams extended are `tier2-review.template.js`'s `priorFindings` input (`:293`), its prompt block
(`:1161-1168`), `inputPrint` (`:985`) and `FINDING_SCHEMA` (`:630`); `extract_acceptance`
(`tools/check-spec-tokens.py:539`) with `AC_HEAD` (`:365`) and `AC_LABEL` (`:369`), moved to
`design_lib.py` beside `read_spec_writes` (`tools/memory-tree/design_lib.py:528`); the parents'
`join_upstream` and `render_return_schema`; and `check_closing_review_recorded`. `python
tools/codebase-map/reuse_lookup.py "hand the closing review each unit's acceptance criteria as rows
every finder answers"` scanned every layer and ranked name-token helpers (`rows`, `units`,
`extract_row`, `read_cap_answer`); none hands rows to a review, so the hand-off extends the harness's
existing inputs. The recall probe surfaced TOOL-dFurnishedOrders-19, a parent whose per-order schema
§8 F3 reuses, and TOOL-aSightedSkeptic-3, which put intent into `specs` and is unchanged here; scout
C's lines hold at `5f0b11f12`, the `intent` brief at `:798` included.

Recall terms used: `python tools/memory-recall/query.py "how does the closing review receive the acceptance criteria and seams each finder must answer" --terms "closing review rows upstream criterion seam finder answers priorFindings tier2-review intent lens measured"`
