# TOOL-dCalibratedLens-7 — the value ledger's shape rows, priced from the shape-run records `review.cost` and the journal reconcile write

**Status:** DEFERRED · rev-2 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 3 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0464@b1127f93 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-14 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing reads the review-shape line (gap-review-11), so a review's cost and yield are measured per run
and never per shape. This unit adds the value ledger's `kind=shape` rows: one row per shape, priced from
the shape-run records `review.cost` writes for review acts (TOOL-dDeclaredLoop-20 S3, recorded by
TOOL-dTotalRecall-11) and the journal reconcile writes for every other act (TOOL-dWellOiledMachine-19
S6), its cost their output tokens and its catches a review's confirmed findings.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`: TOOL-dCalibratedLens-2 (`PROVIDERS`,
`derive_ledger_rows`, `read_record_fields` and the `-` catches rule); TOOL-dTotalRecall-11 (the
`shape-run` kind, its record and its writer `gov_record.py new shape-run --review`);
TOOL-dDeclaredLoop-20 S3 (`review.cost`'s `trigger=`, `shape=`, `efforts=` and `role-sha=` fields on
the line); TOOL-dWellOiledMachine-19 S6 (the `--act` form, `Kind` `act`). The build run re-grounds on
each and stops the unit when one is absent.

- **S1** — The provider, `read_shape_rows(root, window)`, the `PROVIDERS` entry `shape` in
  `tools/loop/loop_review.py`. It reads every tracked shape-run record,
  `<MEMORY_ROOT>/builds/*/build/*-shape-run-*.md` listed by `git ls-files`, through
  `read_shape_records(root)`, each record's fields as `read_record_fields` returns them and its date the
  file name's `<date>`. A record missing `Kind` or `Out-tokens` is skipped and counted. Observed by AC1
  and AC4.
- **S2** — The row. `id` is `<Kind>/<Shape>`: `Kind` is `spec-audit` or `diff-review` for a review act
  and `act` for every other act; `Shape` is the record's `Shape` field, or `-` where it has none or reads
  `-`, which every review record written before dBoundRoles' shape registry carries (TOOL-dDeclaredLoop-20
  S3). `since` is the oldest record's date for the id, at any age; `cost` is the sum of the in-window
  records' numeric `Out-tokens`, spelled `<tokens>tok/<runs>`, `<runs>` the records summed, or `-` where
  every in-window record reads `unknown`. Observed by AC1, AC2 and AC4.
- **S3** — The catches. A review act's record contributes its `Confirmed` count as own events and its
  `Refuted` count as false events, each dated by the record, a `-` count contributing none; the row's
  `catches`, `false-reds` and `last-catch` then follow unit 2's join over the window. An `act` row is
  returned with `catches` `-`: no shape-run field records a non-review act's catch. Observed by AC1 and
  AC2.
- **S4** — The summary. `price` prints one more line, `shape — <n> record(s) · <r> review · <a> act ·
  <u> unknown tokens · <s> skipped`, so a population that priced nothing says so. Observed by AC3 and
  AC4.
- **S5** — The fixture cases `shape-review`, `shape-act`, `shape-unshaped`, `shape-unknown-tokens` and
  `shape-none` join `python loop_review.py --fixture`. Observed by AC1 to AC4.
- **S6** — The docs: the "The value ledger" section of `help/loop-review.md` gains the `shape` row: its
  id, its two writers, its cost and its catches. Observed by AC5.

## 3. Non-goals (OUT)

- The ledger, its grammar, its window, the snapshot and `price`: unit 2.
- The shape-run kind, its record, its writers and `check_shape_runs`: TOOL-dTotalRecall-11,
  TOOL-dDeclaredLoop-20 S3 and TOOL-dWellOiledMachine-19 S6. This unit reads the records and writes none.
- The shape registry that fills `Shape` for review acts: dBoundRoles'.
- Proposing a shape change from its row, or reading the noise between twin runs: unit 5's `propose`
  and the Loop Review's proposal rule. What `propose` does with an `act` row whose `catches` read `-` is
  that unit's.
- Probe cost and compactions: unit 9's `probe` rows. Cost per item kind from trace rows: unit 12's.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-2` — `PROVIDERS`, `derive_ledger_rows`, `read_record_fields`, the `-` catches rule an `act` row takes, and `price`, which prints this provider's rows and its summary line
- **consumes-from** external — TOOL-dTotalRecall-11 (the shape-run record), TOOL-dDeclaredLoop-20 S3 (`review.cost`'s fields) and TOOL-dWellOiledMachine-19 S6 (the act form), each DEFERRED at base
- **hands-off** `TOOL-dCalibratedLens-30` — the `[[usage]]` row of any verb it adds, which the minors batch's `docs_leg.py --list` observation reads (id 39)

## 4. Design

### Evidence

- The line `renderShapeLine` writes (`tools/workflows/tier2-review.template.js:78-83`) carries `kind`,
  `round`, `intensity`, `at`, the eight finding counts, `agents` and `out-tokens`, a count the stage has
  not produced printed `-` (`:74-76`); TOOL-dDeclaredLoop-20 S3 appends `trigger=`, `shape=`,
  `efforts=` and `role-sha=`, `shape=` reading `-` until dBoundRoles lands its registry.
- TOOL-dTotalRecall-11 §4 "The record" turns each review exit's line into a typed build-folder record,
  `<date>-build-<unit id>-shape-run-<n>.md`, with `- **Kind:**` to `- **Out-tokens:**` and `Caused-by`
  required and `Trigger`, `Shape`, `Efforts` and `Role-sha` present only when the line carries them.
- TOOL-dWellOiledMachine-19 S6 writes the same kind for each non-review act through `gov_record.py new
  shape-run --act`, `Kind` `act`, with `Workflow`, `Shape`, `Shape-match`, `Agents`, `Efforts`,
  `Out-tokens` and `Caused-by`; the act form is its §8 F2 ask of dTotalRecall.
- Both record forms are committed in a build's `build/` folder, so the rows re-derive from history on
  every node, unlike the node-journal source unit 2 also reads.

### The row, from two records

| Record | `Kind` | `Shape` | `Out-tokens` | `Confirmed` | `Refuted` | Date |
|---|---|---|---|---|---|---|
| review exit 1 | `spec-audit` | `panel-5` | 1000 | 3 | 1 | in window |
| review exit 2 | `spec-audit` | `panel-5` | 2000 | 0 | 2 | in window |
| act 1 | `act` | `builder-1` | 500 | (none) | (none) | in window |

```text
| shape | act/builder-1 | <act 1's date> | 500tok/1 | - | - | - | 60d | new |
| shape | spec-audit/panel-5 | <exit 1's date> | 3000tok/2 | 3 | 3 | <exit 1's date> | 60d | catching |
```

A confirmed finding is the review's catch and a refuted one its false red, the same pair a leg's own
red and its flake are: a refutation is a reported defect the verify stage found not to hold. The
`unverified` count is neither and is not read.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_shape_rows`, `read_shape_records` | functions in `loop_review.py` | `py.function`, each answered OK by `lexicon.py --suggest` at base |
| `shape` | `PROVIDERS` key and ledger kind | none |

### Amendments (round-1 spec audit)

The round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Each bullet supersedes the text it
names; the unit it names owns the finding and its proof.

- **id 39 · Files touched (M19, `TOOL-dCalibratedLens-30`)** — Every `loop_review.py` verb or flag
  this unit adds to `help/loop-review.md` gets its `[[usage]]` row in `tools/govkit/usage.toml`, and
  the page's `<!-- usage: … -->` anchor is re-fingerprinted, so
  `python tools/govkit/docs_leg.py --list` names it and the `docs` leg reads no `UNROWED` line.

### Files touched (estimate)

- `tools/loop/loop_review.py`: the provider, its summary line and five fixture cases (S1 to S5)
- `help/loop-review.md`: the `shape` row (S6)
- `tools/govkit/usage.toml` — the `[[usage]]` row of each verb or flag added (id 39)

### Alternatives rejected

- **Parse the review-shape line out of each review record directly.** TOOL-dTotalRecall-11 S1 makes
  `shape_run.py` the line's one parser and its record the line read once, compared by
  `check_shape_runs`; a second parser here would be a second answer to that grammar, and it would miss
  every non-review act, which writes no line.
- **`id` the `Shape` alone.** A review panel and a builder act may share no name today, but nothing
  forbids it, and the two kinds' catches mean different things (an act's are `-`). The test: two
  records `spec-audit` and `act`, both `Shape` `x`, would price one row whose `catches` mixes a number
  and an absence.
- **Dropping a record with no `Shape`.** Every review record before dBoundRoles carries none, so the
  review cost gap-review-03 names (about 0.81 M tokens an audit) would price as nothing until then.
- **Counting `High` and `Blocker` rather than `Confirmed`.** A confirmed medium is still a catch; the
  severity split is a reading `propose` may weigh, and it stays on the record.

## 5. Production-readiness checklist

- security — read-only: tracked files listed by `git ls-files` and read as text; no field value
  reaches a shell or a path.
- perf / scale — one read per shape-run record, one per review exit and act; the population grows with
  the trail and is read once a period.
- error / empty / loading states — no record: no `shape` row and the summary's zero line; `unknown`
  tokens: cost `-` with the count on the summary; a malformed record: skipped and counted.
- observability — the summary line; the rows in the period's snapshot.
- risks — `Out-tokens` counts output tokens only (`tier2-review.template.js:84-86`), so a shape's cost
  understates its input reads; the row names what it measures and no more.
- testing — the plants of §6 and §7's arm.
- migration — N/A: a new provider over records that already exist once their writers land.
- user docs — `help/loop-review.md` (S6).

## 6. Acceptance criteria

- **AC1** — When `python loop_review.py --fixture --plant shape-review` writes the two review
  records of §4 and a third `spec-audit` `panel-5` record dated before the window, `price --dry-run`
  prints `spec-audit/panel-5` with cost `3000tok/2`, `catches` 3, `false-reds` 3 and `last-catch` the
  first record's date, and `since` the old record's date.
  Red when: an out-of-window record is summed, or a refuted finding is counted a catch.
- **AC2** — When the plant `shape-act` writes one `act` record, `Shape` `builder-1`, `Out-tokens` 500,
  `price --dry-run` prints `act/builder-1` with cost `500tok/1` and `-` in `catches`, `false-reds` and
  `last-catch`; the plant `shape-unshaped`, a review record with no `Shape` field, prints
  `spec-audit/-`.
  Red when: an act row reads `0` catches, or an unshaped review record prices nowhere.
- **AC3** — When the plant `shape-none` holds no shape-run record, `price --dry-run` prints no `shape`
  row and the line `shape — 0 record(s) · 0 review · 0 act · 0 unknown tokens · 0 skipped`.
  Red when: an empty population prints nothing at all.
- **AC4** — When the plant `shape-unknown-tokens` writes one review record whose `Out-tokens` reads
  `unknown` and one missing `Kind`, `price --dry-run` prints that row's cost `-` and the summary's
  `1 unknown tokens` and `1 skipped`.
  Red when: `unknown` is summed as 0, or a malformed record raises.
- **AC5** — When `grep -n 'spec-audit/' loop-review.md` runs, it prints the line naming the shape
  row's id form.
  Red when: the line is absent.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `docs` · `lexicon naming predicates` · `check-wiring self-test` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

The fixture cases run in unit 2's leg `loop-review selftest`, which the manifest does not hold at base.

New arm: tools/loop/loop_review.py · covers AC1 AC2 AC3 AC4 · the five shape plants, staged red by a provider that sums every record whatever its date, counts `Refuted` as catches, returns `0` for an act row and sums `unknown` as zero · none

## 8. Open questions

- **F1 — What is a shape row's id?** (a) `<Kind>/<Shape>`; (b) `Shape` alone, which merges a review
  panel and an act sharing a name (§4); (c) `Workflow` for acts, which review records do not carry.
  Rung 3. RESOLVED (agent, 2026-11-02, delegated): (a), S2. widens: none · relaxes: none
- **F2 — What is a shape's catch?** The ledger's `catches` column is a leg's own red (unit 2), and a
  shape is a review's cost. (a) `Confirmed` as own and `Refuted` as false events, an act `-`; (b) only
  `Blocker` and `High`, which leaves a confirmed medium uncounted; (c) no catches for shapes, so every
  shape reads `idle` and unit 5 would propose retiring every review. (a) is the only option giving a
  shape row both of the ledger's verdict columns. Rung 3. RESOLVED (agent, 2026-11-02, delegated): (a),
  S3. widens: none · relaxes: none
- **F3 — Where does a record with no `Shape` price?** (a) Under `<Kind>/-`, so review cost is priced
  before dBoundRoles; (b) dropped. Rung 3, (a) the more capable. RESOLVED (agent, 2026-11-02,
  delegated): (a), S2. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft.
- rev-2 · 2026-11-02 · §3 §4 §7 · amended at the disposal of the round-1 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4 "Amendments (round-1 spec
  audit)": ids 39 (`TOOL-dCalibratedLens-30`); §3 gains the hands-off to unit 30.

## 10. Reuse audit

The seams extended: unit 2's `PROVIDERS`, `derive_ledger_rows` and `read_record_fields`; the shape-run
record of TOOL-dTotalRecall-11 (§4 "The record"), the one parsed form of `renderShapeLine`'s line
(`tools/workflows/tier2-review.template.js:78-83`), with its review writer and TOOL-dWellOiledMachine-19
S6's act writer. The probe `python tools/codebase-map/reuse_lookup.py "sum review cost tokens and
confirmed findings per review shape from the review-shape line records"` ranked name stems only (`sum`,
`records`, `shape` in `tools/govkit/matrix.py`, an acceptance-matrix shape, `render_line` in
`tools/runlog/runlog_lib.py`, the journal's line), so no existing seam reads the line or its records at
base, which is gap-review-11 itself; the provider is new over the seams above. Where the brief and source
disagree: the brief names TOOL-dTotalRecall-11's `shape_run.py` as the parser this unit reads through,
and its CLI parses lines (`--parse-line`, `--parse-file`), not records, so S1 reads the records' fields,
which `check_shape_runs` holds equal to their lines.

Recall terms used: `python tools/memory-recall/query.py "how is a gate leg priced by its catches and
cost, and how does a periodic loop review retire what catches nothing" --terms "value ledger loop review
catches false reds window retire price leg cadence lease snapshot"`
