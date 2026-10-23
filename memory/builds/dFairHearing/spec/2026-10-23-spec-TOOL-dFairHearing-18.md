# TOOL-dFairHearing-18 — the whole-design walk as a preset of the design audit, and its recall grade

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 18 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0085@796d40aa whole

**Carries:** node:policy-key.review.design-audit.runs

**Carries:** node:policy-key.review.design-audit.seed

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-token-fix-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-12 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-17 |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/tier2-review.js` gains a `whole-design` preset of the spec-audit kind. Its five walkers
walk every item of a design through every scenario, sliced by scenario on one run and by step on
another under `review.design-audit.runs`. Each returns its findings and a walk table, the harness reds
the run on an empty cell, and the skeptics also try to refute a sample of clean cells. The scorer
factory reads `[tag]` addresses and grades the runs' recall on seeded past escapes as
`review.design-audit.seed` says. Today the walk exists only as build-folder instruments that dispatched
agents by hand, because the harness's lens briefs, output schema and agent-cap dialect did not fit it
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-final-audit.md:221`), and no
audit measures its recall (`gap-review-22`).

## 2. Scope (IN)

- **S1** — `whole-design` joins the closed set of the `preset` argument, and a `walk` argument is
  validated once at the argument boundary: required under that preset and refused under any other,
  with `review.design-audit.runs` and `review.design-audit.seed` arriving as its `runs` and `seed`.
  Observed by AC1.
- **S2** — `deriveWalkSlices(items, scenarios, run)`, a pure function that slices every cell of the
  item-by-scenario grid among the five walker slots: by scenario on run 1, by contiguous step band on
  run 2, and diagonally on run 3. Observed by AC2.
- **S3** — five catalogue rows, `walk-1` to `walk-5`, in `tools/workflows/lenses.toml`, each a default
  lens of `whole-design` only, and the walk's shared instructions held once in the harness as
  `WALK_RULES`, interpolated into every walker prompt with that walker's slice. Observed by AC6, AC10.
- **S4** — the walker's return carries `walk` rows beside its findings; `deriveWalkGaps` checks each
  walker's rows against its slice and the run's joined table against the grid; a gap reds the run, so
  the synthesis is told the verdict is BLOCKED and lists each gap first. Observed by AC3, AC4.
- **S5** — the joined walk table rendered in the whole-design audit's `[walk-table]` grammar, and a
  `walk-seed` line, both handed to the synthesis to copy verbatim; `walkTable` and `walkGaps` on the
  return. Observed by AC4.
- **S6** — a sample of eight clean cells per skeptic batch, drawn deterministically from the cells whose
  verdict is `holds`; a refuted cell becomes an UNVERIFIED finding of the lens `cell-sample`; a run
  with no finding still dispatches one skeptic batch and still synthesizes; `cellsSampled` and
  `cellsRefuted` on the return. Observed by AC4, AC5.
- **S7** — the scorer factory `tools/workflows/replay_scorer.py` gains `extract_tag_ref`, which reads a
  `[tag]` address, and a `--design-recall` grade through its entry, which scores each run's confirmed
  findings against a seeded key as `review.design-audit.seed` says. Observed by AC7, AC8, AC9.
- **S8** — the args header and `tools/workflows/README.md` name the preset, the `walk` argument, the
  return fields, the two record lines and the grade. Observed by AC10.
- **S9** — the suite arms the `New arm:` lines in §7 declare. Observed by AC1, AC2, AC3, AC4, AC5,
  AC7, AC8, AC9 through those lines, RED-first at the close.

## 3. Non-goals (OUT)

- No seeding: making the sealed copy and its key stays the caller's, as the build-folder instrument
  `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-walk-seed.py` does it today
  (§8 F6).
- No Stage 0: the mechanical checks the whole-design audit ran first belong to their owning builds
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-research-final-audit.md:254-260`).
- No build or principle verdicts, which the audit's walkers gave: they are gov's design vocabulary,
  and the clause's table is item by scenario.
- No failure-mode or trust-boundary column in the walk table. The audit routed that kit defect to
  this preset (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md:325-326`),
  and the clause at the baseline names five columns; `WALK_RULES` asks for both readings as
  instructions, and the slot is handed off.
- No read audit of what a walker opened, and no second skeptic on refutations: the audit's own
  additions after its first run, neither in the clause.
- No Mills or Chapman estimate: the audit reported both as a trend, never the gate.
- No reading of `review.design-audit.runs` or `review.design-audit.seed` from a policy file: no route
  exists, and both arrive through `review.pin`'s arguments, the stand-in TOOL-dFairHearing-3 builds
  until dDeclaredLoop's `review.trigger` lands.
- No change to the diff kind or to any other preset: every prompt, schema and exit of a run that is not
  `whole-design` stays byte-identical.
- No help page: `help/` holds no page on the review harness.
- No kit version constant moved: the lander mints them.

### Edges

- **consumes-from** `TOOL-dFairHearing-2` — the `preset` argument, its closed set and its refusal
  beside the diff kind; without it `whole-design` has no argument to join
- **consumes-from** `TOOL-dFairHearing-13` — `tools/workflows/lenses.toml` and its render into the
  five-slot literal; without it the five walker rows have no catalogue to live in
- **consumes-from** `TOOL-dFairHearing-3` — `review.pin`, the stand-in that carries
  `review.design-audit.runs` and `review.design-audit.seed` into the `walk` argument
- **consumes-from** `TOOL-dFairHearing-4` — `deriveAddressKey`, whose spec-kind address the scorer's
  `[tag]` reading agrees with field for field
- **consumes-from** `TOOL-dFairHearing-12` — the scorer factory's one entry and its refusal of a
  partial population, which the design grade runs through
- **consumes-from** `TOOL-dFairHearing-1` — the known-set row shape, `address`, `grade`, `escaped` and
  `tag`, and `parse_known_set`, its reader, which a seeded key reuses
- **consumes-from** `TOOL-dFairHearing-17` — `roundState` and `roundCount`, which a whole-design round
  carries as every spec-audit round does
- **hands-off** external — the sealed copy and its key, a failure-mode and trust-boundary slot in the
  walk table, and a read audit of the walkers, filed as one ask at this build's close
- **hands-off** `TOOL-dFairHearing-20` — finding id 37 (item H1) of the round-1 spec audit: a gapped walk nulls `blockers`, `highs`, `roundCount` and `roundState` and notes BLOCKED, the red §4 The gaps states only in the synthesis prompt
- **hands-off** `TOOL-dFairHearing-23` — finding ids 1, 3, 8, 16, 18, 19, 21, 22, 32, 34 and 53 of the round-1 spec audit: the tag reader consumed from `TOOL-dFairHearing-12` with its integer section, AC7 included (its S1 to S3, AC1), review.pin's per-run route for runs and seed (its S5, S6, AC3), AC10's render-diff clause replaced (its S9, S10, AC4), the `WHOLE_DESIGN_LENSES` literal and receiver branch (its S15, AC8), AC7's drive-letter literal as a raw string (its S41, AC32), the design grade through `measure_recall` (its S43, AC34) and the walk grid's ceilings (its S49, AC40)

## 4. Design

### The argument

`preset: 'whole-design'` requires `kind: 'spec-audit'`, which S1's refusal beside the diff kind already
gives, and a `walk` object. `walk` under any other preset is refused naming `walk`. Its fields:

| Field | Shape | Absent |
|---|---|---|
| `items` | non-empty array of `{ tag, step }`, each a string matching `^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$`, tags unique | refused |
| `scenarios` | non-empty array of `{ id, name, walks }`, `id` matching `^[A-Za-z0-9][A-Za-z0-9._-]{0,31}$` and unique, `name` and `walks` non-empty strings | refused |
| `runs` | `review.design-audit.runs`: 1, 2 or 3 | 2, v2's default (v2:1256) |
| `run` | an integer from 1 to `runs`: which run this invocation is | refused |
| `seed` | `review.design-audit.seed`: `reverted-escapes`, `synthetic` or `none` | `reverted-escapes` (v2:1257) |
| `keySha` | 64 lower-case hex, the key's SHA-256 | refused unless `seed` is `none` |

Each refusal names its field and runs before the resume probe, the first agent. The anchored shapes
keep a newline, a pipe and a backtick out of every prompt line and table cell an item or scenario
reaches; `name` and `walks` reach prompts through `renderPromptLine`'s line-break fold. `walk` joins
the review key's input print, since the walker prompts interpolate it. The subjects are the design
records walked, DESIGN subjects by path (`tools/workflows/tier2-review.js:317`), and under a seeded
mode `repo` is the sealed copy, outside the repository.

One invocation is one run (§8 F3). `review.pin` invokes the harness `runs` times, `run` 1 to `runs`,
one after the other, so no run's report exists while the next one walks.

### The slices

`deriveWalkSlices(items, scenarios, run)` returns five slices, each a list of `[itemTag, scenarioId]`
cells, and every cell of the grid is in exactly one slice:

| Run | Sliced by | Walker slot `w` of 5 takes |
|---|---|---|
| 1 | scenario | every item, through the scenarios `deriveChecklistShares` deals it, round-robin in the order given |
| 2 | step | every scenario, through one contiguous band of steps, the steps in first-seen item order and cut so each band's item count is as even as whole steps allow |
| 3 | diagonal | each cell whose item index plus scenario index, mod 5, is `w - 1` |

Run 1 reuses `deriveChecklistShares` (`tools/workflows/tier2-review.js:907-912`), keyed by the five
walker lens keys. Run 3 is §8 F4's. A slot whose slice is empty, as when a design has fewer than five
scenarios, is not dispatched: it joins `skippedLenses`, whose RUN INTEGRITY clause reads, on this
preset, as walker slots with no slice rather than as a light run.

### The walkers

Five rows in `tools/workflows/lenses.toml`, `walk-1` to `walk-5`, each a default lens of `whole-design`
alone, of the spec-audit kind, in the row grammar TOOL-dFairHearing-13 defines. Each row's `brief`
says only which slot it is (§8 F2). `WALK_RULES`, a constant beside `PROBE_RULES`
(`tools/workflows/tier2-review.js:715-727`), holds what every walker is told:

- its run's slicing and its own cells, each scenario with its `name` and `walks`;
- open with a pre-mortem reading: the design shipped and failed in this slice, and why;
- read each item a failure reaches for its failure mode, effect and detection, and each data flow
  crossing a trust boundary for its threats;
- for each cell, write the actor, needs, witness and route the scenario finds there, `=` where it
  reads as declared and never empty, and the verdict;
- address each finding by `file` and a `where` naming the `[section tag]`, with the clause id or item
  tag that carries it;
- when seeded, the key's SHA-256, and that the key is never to be read.

The walker schema is `SPEC_FINDING_SCHEMA` (`:735-760`) plus a required `walk` array, one row per
cell: `item`, `scenario`, `actor`, `needs`, `witness`, `route`, all strings; `verdict`, one of
`holds`, `finding` or `not-on-path`; `findings`, the zero-based indexes of the row's findings in the
walker's own `findings` array; and `reason`, for `not-on-path`. The harness maps each index to the
finding's assigned id. Every other preset keeps `SPEC_FINDING_SCHEMA` itself.

### The gaps

`deriveWalkGaps(slices, returns)` is pure and returns one string per gap, `<item> · <scenario> — <what>`:

- a cell of the walker's slice with no row, or with two;
- a row for a cell outside its slice;
- an `actor`, `needs`, `witness` or `route` that is empty once trimmed;
- a `verdict` outside the three;
- `finding` with no index, or an index past the walker's findings;
- `not-on-path` with an empty `reason`, or `holds` carrying an index.

A run with any gap is red: the synthesis prompt says the walk table has that many gaps, that the report
lists each first, and that the `## Verdict:` token is BLOCKED. That is the clause's synthesis red on an
empty cell, decided by the harness and stated by the agent. A walker that died defers the run before
any synthesis, as every lens death does today.

### The record

The pure `renderWalkTable` renders the joined table in the whole-design audit's `[walk-table]` grammar
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md:133-151`):

```
## Walk table — run <r> of <runs>, sliced by <scenario|step|diagonal>
walk-seed mode=<seed> key-sha256=<keySha|->

| Item | Scenario | Actor | Needs | Witness | Route | Verdict |
|---|---|---|---|---|---|---|
| `plan.input` | S1 | = | = | = | = | holds |
```

Rows run item by item in the order given, each item through the scenarios in order. A verdict reads
`holds`, the finding ids `<R><w>-F<id>` joined by `, ` (`R` is `A`, `B` or `C` for runs 1 to 3, `w` the
walker slot and `id` the harness's integer id, the audit's id shape), or `not on path: <reason>`. Cells
pass through `renderCell` (`:1624-1626`). The block reaches the synthesis between `<<<WALK TABLE` and
`WALK TABLE>>>` marker lines, to be copied verbatim directly before the appendix; the return's
`walkTable` holds the rows, and the copy is not verified, as the appendix's is not.

### The clean cells

Every skeptic batch of a `whole-design` run is handed eight clean cells to attack, the audit's number
(`...-whole-audit.md:190-192`). The sample is drawn from the cells whose verdict is `holds`, sorted by
`<item> · <scenario>`, at an even stride over the sorted list, `8 × batches` cells or every clean cell
when fewer exist, and dealt round-robin to the batches. The draw is a pure function of the table, so a
re-run hands the same cells, and the cells join each batch's reuse print.

When the walkers raise no finding, the batch list is one cell-only batch, labelled `verify:cells`, a
label neither batch-label scheme produces; the batches line keeps its `// gov:fixed-verifiers` receiver
shape (`:1353`). The skeptic schema is `VERDICT_SCHEMA` (`:672-695`) plus an optional `cells` array of
`{ cell, verdict, reason, file, where, severity }`, `verdict` either `holds` or `refuted`, used on this
preset alone. A refuted cell becomes a finding of the lens `cell-sample`, with the skeptic's address,
reason as its claim, and grade, its id after every walker finding's. No second skeptic judges it, so it
is UNVERIFIED (§8 F8). `cellsSampled` and `cellsRefuted` count the cells handed and refuted, and RUN
INTEGRITY states both.

Under this preset neither clean early exit returns (`:1321-1342`, `:1654-1679`): a run with no finding
still samples its clean cells and still synthesizes, because the record is where the walk table lives.

### The grade

`replay_scorer.py`, the factory TOOL-dFairHearing-12 extracts from `tools/workflows/review_replay.py`,
gains:

- `extract_tag_ref(text)`, returning `(path, key)` for a spec ref `<file>:<where>`, where `key` is the
  first `[<tag>]` in `<where>`, written `[tag]`, or else the `§<n>` the factory's section reader gives
  (`tools/workflows/review_replay.py:100-115` today). It folds paths as that reader does, so it gives
  the file and tag `deriveAddressKey` gives for the same ref;
- `measure_design_recall(records, plants, seed)` and its flag on the factory's entry:

```
python tools/workflows/replay_scorer.py --design-recall --key <known-set file> --seed <mode> <record-run-1> [<record-run-2> …]
```

Each record is one run's review record. The grade reads its `## Walk table — run <r> of <runs>` heading
and `walk-seed` line, and the confirmed rows of its appendix, scoring each row's `ref` through
`extract_tag_ref`. Each plant is one known-set row as `parse_known_set` reads the key, its `address`
read the same way and matched on the
same file and the same key. A plant counts once per run. It prints, for each run and for the union of
the runs, the hits over the plants, then each missed plant by its `tag`.

| Case | Exit |
|---|---|
| `--seed none` | prints that recall is not graded under `review.design-audit.seed` `none`, reads no key, 0 |
| every run finds at least two thirds of the plants, and with two or more runs the union at least five sixths | 0 |
| a run or the union under its bar | 1 |
| the key's SHA-256 over its bytes differs from any record's `walk-seed` pin | 2 |
| records disagreeing on `runs`, a run missing or repeated, or a record whose `walk-seed` mode is not `--seed` | 2 |
| a plant whose `escaped` is false under `reverted-escapes`, or true under `synthetic` | 2 |
| a confirmed row or a plant with no file and key to score | 2, as the factory's unscorable refusal |

The bar is the audit's, fixed before its walk (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md:126-128`),
eight of twelve a run and ten of twelve together, written as fractions so a key of another size grades
alike (§8 F5).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `whole-design` | a `preset` value | none |
| `walk` | harness argument | none |
| `deriveWalkSlices`, `deriveWalkGaps` | functions, `tools/workflows/tier2-review.js` | `js.function`, OK |
| `renderWalkTable` | function, `tools/workflows/tier2-review.js` | `js.function`, OK |
| `WALK_RULES` | constant, `tools/workflows/tier2-review.js` | none: `.lexicon.conf` declares no JS constant cell |
| `walk-1` to `walk-5`, `cell-sample` | lens keys | none |
| `walkTable`, `walkGaps`, `cellsSampled`, `cellsRefuted` | harness return fields | none |
| `walk-seed`, `## Walk table` | record line and heading | none |
| `<<<WALK TABLE`, `WALK TABLE>>>` | synthesis prompt markers | none |
| `verify:cells` | batch label | none |
| `extract_tag_ref`, `measure_design_recall` | functions, `tools/workflows/replay_scorer.py` | `py.function`, OK |
| `--design-recall` | scorer flag | none |

### Migration

None. The preset is opt-in by argument, and a run naming any other preset is unchanged.

### Rollout

The landing ships the preset and the grade; the first whole-design audit is the next build's whose
Design breakpoint asks for one, through `review.pin`.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/lenses.toml`
- `tools/workflows/replay_scorer.py`
- `tools/workflows/README.md`

`tools/workflows/tier2-review.js` is the render of its template (`check-protocol-parity.test.sh
--render`): the template is the edit and the render its copy.

### Alternatives rejected

- **Keep the walk as build-folder instruments.** It ran that way once, with 38 direct dispatches the
  hooks admitted only because no harness existed (`...-final-questions.md:119-123`), and every brief,
  batch and check lived in a build folder no other build reads.
- **The synthesis agent finds the empty cells.** The audit's synthesizer was told to and its tables
  were then checked by a script (`...-whole-audit.md:149-151`); the harness checks them itself, so the
  red is a computed fact the agent states.
- **The audit's matcher, which also wants an anchor and a word of the plant in the finding.** It reads
  more than an address, and the brief's S4 fixes the address key as file and first `[tag]` for every
  reader; the audit read each hit by hand for the neighbour case that matcher was for.

## 5. Production-readiness checklist

- security — no new write path; the harness writes nothing. Every item, step and scenario field is
  shape-checked before any agent, so no control character, pipe or backtick reaches a prompt or a
  table cell. The grade reads files it is handed and writes nothing.
- perf / scale — the same agent shape as any spec audit: five finders, at most five skeptic batches and
  one synthesis. A large grid makes a large walk table in each walker's return and in the record, which
  the audit measured at 812 cells.
- error / empty / loading states — a malformed `walk` refuses before the first agent; an idle walker
  slot is announced; a walker death defers; a gap reds the record; a moved key or a partial population
  refuses the grade.
- observability — RUN INTEGRITY states idle slots, cells sampled and refuted; the return carries the
  table and its gaps; the grade names every missed plant.
- risks — the record's copy of the table is the agent's and is not verified; the return is the source
  of record. A hit can be a neighbour of its plant at the same address, as the audit found by hand, so
  recall is an upper bound. The key's hash is over its bytes as the grade reads them, so a CRLF checkout
  of a committed key moves it, as the audit recorded.
- testing — the pass probes the slicer, the gap check, the boundary and a stub run with scratch node
  scripts, and the grade with scratch python fixtures; the arms in §7 are observed RED then GREEN by the
  main loop at the close.
- migration — none, as §4 Migration says.
- user docs — `tools/workflows/README.md`; §3 says why no help page changes.

## 6. Acceptance criteria

- **AC1** — When a scratch node probe evaluates the prelude of `tools/workflows/tier2-review.js`, cut as
  `tools/workflows/tier2-review.test.sh:70-92` cuts it, `preset: 'whole-design'` with no `walk` throws
  naming `walk`; `walk` under `preset: 'unit-spec'` throws naming `walk`; `walk.runs` of 0 or 4,
  `walk.run` above `walk.runs`, `walk.seed` of `'x'`, a seeded `walk` with no `keySha` or a 63-hex one,
  an item tag carrying a newline, two scenarios sharing an id and an empty `items` each throw naming
  their field; a valid `walk` proceeds, reading `runs` 2 and `seed` `reverted-escapes` when both are
  absent.
  Red when: the run-past-runs check is missing, so `run: 3` with `runs: 2` proceeds.
- **AC2** — When the same probe calls `deriveWalkSlices` over ten items in five steps of two and seven
  scenarios `S1` to `S7`, run 1 gives slot 1 `S1` and `S6`, slot 2 `S2` and `S7`, and slots 3 to 5 one
  scenario each, every slice holding all ten items; run 2 gives each slot one step's two items through
  all seven scenarios; run 3 gives cell (i, j) to slot `(i + j) mod 5 + 1`; and in each run every one of
  the 70 cells sits in exactly one slice. Over three scenarios, run 1 leaves slots 4 and 5 empty.
  Red when: a run drops a cell or deals one to two slots, so the exactly-one count fails.
- **AC3** — When the same probe calls `deriveWalkGaps` on a walker return whose table is complete, it
  returns `[]`. With the planted empty cell, a `witness` of `'  '`, it returns one gap naming the item,
  the scenario and `witness`. A missing row, two rows for one cell, a row outside the slice, the verdict
  `maybe`, a `finding` index past the findings, and `not-on-path` with an empty reason each return one
  gap.
  Red when: a whitespace-only cell is read as filled, so the planted empty cell returns `[]`.
- **AC4** — When a scratch AsyncFunction run of `tools/workflows/tier2-review.js`, the shape
  `tools/workflows/tier2-review.test.sh:321-340` uses, runs `whole-design` with five walker stubs
  returning complete tables, the synthesis prompt carries the `<<<WALK TABLE` block opening
  `## Walk table — run 1 of 2, sliced by scenario`, the `walk-seed` line and the header
  `| Item | Scenario | Actor | Needs | Witness | Route | Verdict |`, and the return carries `walkGaps: []`.
  With one stub's planted empty cell, the prompt names the gap and says the verdict is BLOCKED, and
  `walkGaps` has one entry. With stubs raising no finding, one skeptic batch labelled `verify:cells` is
  dispatched and the synthesis runs.
  Red when: the no-finding run returns at the `allFindings.length === 0` exit, so no skeptic and no
  synthesis is dispatched.
  cost: a scratch harness of about 100 lines, modelled on that suite's stub agents.
- **AC5** — When the same harness runs a table of 40 clean cells over two skeptic batches, each skeptic
  prompt carries eight clean cells, the two sets disjoint and identical on a second render; with one
  skeptic stub refuting one cell, the return carries `cellsSampled: 16` and `cellsRefuted: 1`, and the
  ledger holds an `unverified` entry whose lens is `cell-sample`.
  Red when: the sample draws a cell whose verdict is not `holds`, or a second render draws other cells.
- **AC6** — When the same harness renders the walker prompts, each names its own scenarios and items
  and no other slot's, carries the `WALK_RULES` block, and carries the key's SHA-256 under
  `reverted-escapes` and no SHA-256 under `none`; and `grep -c 'WALK_RULES'` over
  `tools/workflows/tier2-review.js` finds the constant defined once.
  Red when: a walker prompt carries another slot's cells.
- **AC7** — When a scratch python probe imports the factory `replay_scorer.py`,
  `extract_tag_ref('x.md:[walk-table] plan.input')` returns `('x.md', '[walk-table]')`,
  `extract_tag_ref('C:\x.md:[a] then [b]')` returns the key `'[a]'` and the path with its drive
  letter dropped and its root slash kept, as the section reader folds it, and
  `extract_tag_ref('x.md:§3 S2')` returns `('x.md', '§3')`; and a scratch node probe of
  `deriveAddressKey` in `tools/workflows/tier2-review.js` gives the same file and tag for the first
  ref.
  Red when: a ref carrying two tags reads the second.
- **AC8** — When `measure_design_recall` runs over a scratch fixture of three plants, each a known-set
  row with `escaped` true, and two run records pinning the key's SHA-256, where both runs confirm hits
  on the first two plants and miss the planted third, it prints 2 of 3 for each run and for the union,
  names the third plant's `tag` as missed, and the `--design-recall` entry exits 1. When run 2 also
  confirms a hit on the third plant, the union reads 3 of 3 and the entry exits 0.
  Red when: the union bar is not applied, so a plant every run missed exits 0.
  fixture: built under the run's scratch directory; the tree holds none today.
- **AC9** — When the same fixture's key has one byte changed, the entry exits 2 naming the key's
  SHA-256; with only run 1 of 2 handed it exits 2 naming the missing run; with a plant whose `escaped`
  is false under `--seed reverted-escapes` it exits 2 naming the plant; and with `--seed none` it prints
  that recall is not graded and exits 0 without opening the key.
  Red when: a moved key is scored, so the changed byte exits 0 or 1.
- **AC10** — When `grep -c` runs over the catalogue `lenses.toml` for each of `walk-1` to `walk-5`,
  each prints 1, and each row names `whole-design`; over `tools/workflows/README.md` for each of `walk`,
  `walkTable`, `walkGaps`, `cellsSampled`, `cellsRefuted`, `walk-seed` and `--design-recall`, each prints
  at least 1; the args header of `tools/workflows/tier2-review.js` carries `walk:` as a key line; and
  `sed 's/{{FANOUT_CAP}}/5/g' tools/workflows/tier2-review.template.js` piped to `diff -` against the
  render prints nothing.
  Red when: the template is edited and the render is not re-rendered, so the diff prints the hunk.
  figure: the cap `5` is PINNED at base `3708a705`; read the render's own `boundedParallel` default if
  `.agent-cap.conf` moved it.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `verifier fan-out` · `review-replay selftest` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `lexicon naming predicates` · `testsuite counts (every bar self-test prints one)` · `spec tokens (a spec's own names resolve)`

The scorer factory's own self-test leg is the one TOOL-dFairHearing-12 adds; the arm below lands in it.

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 AC3 AC4 AC5 · a whole-design call with no walk, a slicer that drops a cell, a planted empty cell, a no-finding walk and a clean-cell sample, each staged against the base harness, which has no whole-design preset · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/workflows/replay_scorer.py selftest · covers AC7 AC8 AC9 · a two-tag ref, a planted plant both runs miss, a moved key and a partial population, staged against the factory without the design grade · that self-test's declared arm count, raised by the arms added

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` in `tools/memory-tree/tree_lib.py:28`, which the header regex
  at `tools/memory-tree/tree_lib.py:377` joins. Observation: the set is `OPEN SPECCED INPROGRESS
  BLOCKED DEFERRED CLOSED WONTDO`, so a `DRAFT` header parses as no header and the unit reads MISSING.
  Liveness: the probe reads a tuple that would carry `DRAFT` if the vocabulary admitted it. RESOLVED
  (agent, 2026-10-23, delegated): `OPEN`, the token `memory/TEMPLATE-SPEC.md` gives drafting.
- **F2 — How do five walkers fill the catalogue's five slots?** Options: (a) five rows, `walk-1` to
  `walk-5`, each brief naming its slot, with the shared instructions held once as `WALK_RULES`; (b) one
  `walk` row the render expands into five slots; (c) one row with a slot-count field. (b) and (c)
  change the row grammar and render the brief's S3 fixes for TOOL-dFairHearing-13, and the slot check
  of the brief's S13 counts slots that would no longer be rows. (a) changes neither. RESOLVED (agent,
  2026-10-23, delegated): (a), rung 3.
- **F3 — One invocation per run, or every run in one invocation?** Options: (a) one per run, `walk.run`
  naming it and `review.pin` invoking `runs` times; (b) one invocation running every run. (b) puts up
  to fifteen walkers and three syntheses in one review's shape, and the audit's runs were independent:
  run A's report stayed out of the tree while run B walked
  (`...-final-questions.md:108-109`), which one invocation writing both reports cannot keep. RESOLVED
  (agent, 2026-10-23, delegated): (a), rung 3.
- **F4 — How does the third run slice, under `review.design-audit.runs` = 3?** Options: (a) diagonally,
  cell (i, j) to slot (i + j) mod 5, a third way through the same grid; (b) the audit's run C, a clause
  walk sliced by build (`...-whole-audit.md:383-391`), whose table is clause by build, not the clause's
  item-by-scenario table; (c) refuse 3. (b) fails the clause's walk table and (c) fails the key's
  allowed value 3 (v2:1256), whose text says each run is "sliced its own way". RESOLVED (agent,
  2026-10-23, delegated): (a), rung 3.
- **F5 — What bar does the recall grade hold the runs to?** v2's key text names the grade and no bar;
  the owner's FQ-1 design fixes one: each run at least two thirds of the plants, the runs together at
  least ten of twelve (`...-final-questions.md:126-128`), the bar the audit scored against. Options:
  (a) that bar, as fractions; (b) a bar the caller passes; (c) no bar, a report only, which cannot red
  on the clause's planted miss. RESOLVED (agent, 2026-10-23, delegated): (a), rung 1, the design
  record behind v2's FQ-1 rows answering it.
- **F6 — Who seeds the sealed copy?** Options: (a) this unit, adopting the audit's seeding script;
  (b) a unit of its own; (c) the caller, as a precondition the grade checks through the key's pin. The
  clause asks for the recall graded, not for the copy made; (a) puts a second mechanism in this spec
  against BUILD-METHOD M2, and (b) adds a roster unit outside this writer's group. RESOLVED (agent,
  2026-10-23, delegated): (c), rung 3, with the seeding tool handed off in §3 Edges.
- **F7 — How large is the clean-cell sample?** The clause says a sample. The audit's
  `review.design-audit.cell-refute` key, proposed with `sampled` as its default
  (`...-research-final-audit.md:278`), did not join v2's policies, so the size is no policy value.
  Options: (a) eight per batch, the audit's number; (b) every clean cell; (c) a caller argument. (b)
  multiplies each skeptic's load by the grid, and (c) is a knob no key backs. RESOLVED (agent,
  2026-10-23, delegated): (a), rung 3.
- **F8 — What does a refuted clean cell become?** Options: (a) an UNVERIFIED finding, raised by one
  skeptic and judged by none; (b) a confirmed finding; (c) a count only. (b) grades a claim nobody
  checked, and (c) drops the address the report needs. RESOLVED (agent, 2026-10-23, delegated): (a),
  rung 3.
- **F9 — One unit, or the grade split from the preset (BUILD-METHOD M2)?** Options: (a) one unit, as
  the roster row and the clause bind them; (b) two. The grade is the clause's own recall half and reads
  only what the preset writes; (b) adds a roster unit, a deviation record and a split carry. RESOLVED
  (agent, 2026-10-23, delegated): (a), by M3's tie-break on fewer open questions, rung 3.
- **F10 — The preset value, the `walk` argument, the return fields, the two record lines and the
  scorer flag change public surfaces; does the build's grant cover them?** The clause names the walk
  preset, its table, its skeptics, the `[tag]` scorer and the graded recall, and `PLAY-dClosedLoop-3`
  grants the public-surface changes a build's own clauses name. RESOLVED (agent, 2026-10-23,
  delegated): covered, rung 3.
  grants: PLAY-dClosedLoop-3 the whole-design preset value and walk argument of tier2-review.js, its walkTable, walkGaps, cellsSampled and cellsRefuted return fields, the walk table and walk-seed lines of the review record, and the --design-recall flag of replay_scorer.py

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, from the packet's Items 18, the brief's S1, S3, S4, S10, S11, S12
  and S14, the whole-design audit's records, and the harness and replay scorer read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-20 and TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.

## 10. Reuse audit

The seams are the harness's own: the spec-audit kind and its subjects, the lens catalogue's five slots,
`deriveChecklistShares` for run 1's deal (`tools/workflows/tier2-review.js:907-912`), the verify batches
and their reuse print (`:1347-1370`), `renderCell` and the appendix's copy instruction for the table
(`:1624-1635`, `:1904-1908`), and the factory's appendix reader and unscorable refusal for the grade.
The walk's grammar, slicing and bar are the whole-design audit's instruments, carried over:
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-walk.py` (its `cells_of` and
`check`) and `...-score.py`. No new agent stage, record writer or scorer.

`python tools/codebase-map/reuse_lookup.py` over "walk every item through every scenario and check
the walk table has no empty cell" ranked generic stems (`check`, `has`, `walk` in
`tools/memory-tree/corpus_ids.py`) and over "score review recall against seeded known defects by
section tag address" ranked `score` in `tools/memory-recall/bench.py` and `seed`; neither named the
walk kit or the replay scorer, because the map does not scan build folders and the review kit's
scorer is matched by no stem of those phrases, so the seams were found by reading the source.
`python tools/memory-recall/query.py` returned the two runs' review records
(`memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-whole-walk-a.md`, `-b.md`),
whose slicing agrees with the audit's `[slicing]`, and `TOOL-aSightedSkeptic-9`, the replay
benchmark's spec. One record disagrees with source: the audit's research says today's scorer refuses a
design report because it reads only `§<n>` at `tools/workflows/review_replay.py:36-44`; that text is
the docstring, and the reader is `extract_section_ref` at `tools/workflows/review_replay.py:100-115`.

Recall terms used: whole-design walk walker scenario step band walk-table empty cell clean cells sealed copy plants recall tag scorer
