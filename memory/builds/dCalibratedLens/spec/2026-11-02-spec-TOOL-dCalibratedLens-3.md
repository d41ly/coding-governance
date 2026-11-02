# TOOL-dCalibratedLens-3 — the Loop Review: a cadence step run as `review.loop.cadence` says, its lease keyed by the selected period, its walk and its record

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 2 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0460@401ecbd8 whole
**Carries:** node:record-kind.loop-review
**Carries:** node:item.loop.lease
**Carries:** node:item.loop.gather
**Carries:** node:item.loop.file
**Carries:** node:item.loop.record
**Carries:** node:policy-key.review.loop.cadence
**Carries:** node:policy-key.review.loop.window-days

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |

<!-- /gen:spec-records -->

## 1. Goal

No retrospective reads the loop's own metrics (gap-review-02). This unit lands the Loop Review,
registered as a cadence step of the observability expansion and run as `review.loop.cadence` says,
`weekly`, `monthly` or `every-n-landings`, its lease keyed by the selected period, each value seen on its
planted case. It is one program, `python tools/loop/loop_review.py run`, walking the six `item.loop.*`
rows in `needs` order under the period lease, every reading taking the one window
`review.loop.window-days` sets (default 60), and writing one `loop-review` record per period.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`: TOOL-dCalibratedLens-2 (the module,
`read_loop_policy`, `derive_loop_window`, `price` and the home `loop-review/`); TOOL-dWellOiledMachine-59
S1 to S3 (`point.cadence-items`, `check_cadence_row`, the tick) and -13 S5, S6 (`derive_period`,
`run_cadence_period`), with asks TOOL-dTendedCadence-27 (`GOV_CADENCE_KEY`), TOOL-dTendedCadence-29
(`period-key`) and TOOL-dTendedCadence-30 (the `session-start` host) and this unit's ask of §8 F2;
TOOL-dDeclaredLoop-12 (the item rows, `check_program`, `order_by_needs` and its inline `needs_graph_py`
block); TOOL-dWellOiledMachine-27 S1 (`intake.py file --origin cadence`); TOOL-dTotalRecall-1 (the
registry); DEPL-dShippedRelease-1 (the landing records `every-n-landings` counts). The build run
re-grounds on each and stops the unit when one is absent.

- **S1** — The rows. Four `[[item]]` rows in `tools/loop/loop.toml`, in TOOL-dDeclaredLoop-12's data
  model, `step = "cadence.loop"`, `owner = "dCalibratedLens"`, as §4 "The items" tabulates:
  `item.loop.lease`, `item.loop.gather`, `item.loop.file` and `item.loop.record`. This unit re-points
  unit 2's `item.loop.price` row: `needs = ["item.loop.gather"]` and `routes = { priced =
  "item.loop.file" }`; unit 5 inserts `item.loop.propose` between them. Observed by AC7.
- **S2** — The walk, `run_loop_walk(root, key, dry_run)`, run as `python loop_review.py run [--check]
  [--dry-run] [--key <key>]`. `read_loop_items(kit_dir)` reads the `step = "cadence.loop"` rows with
  `tomllib` and orders them with `order_by_needs`; a need naming no row, a cycle, an outcome with no
  route and a route naming no row nor a `stand-in:<path>` each exit 2 with one line. `--check` stops
  there, printing `loop — <n> item(s) · ok`. Otherwise each item runs once every item it needs has run,
  handed the outcomes routed to it, and prints `loop — <key> · <item tag> · <outcome>`; the walk exits 0
  once `item.loop.record` has run, and exits 1 when an item raises or refuses, so `run_cadence_period`
  releases the lease as a hand-over and the next wake runs the period again
  (TOOL-dWellOiledMachine-13 S6 step 5). This is TOOL-dTendedCadence-1 S2's walk over another step's rows.
  Observed by AC7.
- **S3** — `loop.lease`, `read_loop_key(root)`. Its actor is the executor: `run_cadence_period` takes
  `refs/gov/leases/run/loop-review/<period>` before it runs the walk and releases it after, so a held or
  witnessed period never reaches the program. The item reads the key from `GOV_CADENCE_KEY` and holds
  it to the form the value of `review.loop.cadence` (read through `read_loop_policy`) names, per §4 "The
  periods": a key of another form exits 2, `loop — refused: key <key> is not a <value> period`, and no
  key at all exits 2, `loop — refused: no key; run under cadence.py run loop-review`. A key that holds
  reaches the walk as `taken`. `--key <key>` is admitted only with `--dry-run`. Each value is seen on its
  planted case. Observed by AC1.
- **S4** — The cadence row: one `[[adapter]]` row at `point.cadence-items` in
  `tools/runtime/points.toml`, `name = "loop-review"`, `host-key = "maintain.host"`, `period-key =
  "review.loop.cadence"`, `landings = 21`, `run = ["python", "tools/loop/loop_review.py", "run"]`,
  `events = []`, with the grant, tenancy, retention and region fields the point's rows carry. The
  observability expansion's one host key is `maintain.host` (§8 F1). The tick derives the period from
  the key's value through `derive_period`, whose `monthly` and `every-n-landings` forms are this unit's
  ask of §8 F2. Observed by AC1 and AC2.
- **S5** — `loop.gather`, `measure_loop_metrics(root, window)`: each entry of `METRICS`, a list of
  `(name, reader)` pairs, read over the one window `derive_loop_window` returns, each answering `(value,
  source)` and a reader whose source holds nothing answering `searched-none` with the path or glob it
  searched. This unit's two entries are `surface`, `<legs> legs · <gotchas> gotchas · <keys> keys`
  counted from `tools/gate-legs.json`, the tracked `<MEMORY_ROOT>/gotchas/*.md` and the `[[key]]` rows
  of `tools/policy/catalogue.toml`; and `review-yield`, `<clean>/<fixes>/<blocked>`, the
  `## Verdict:` lines (`CLEAN`, `CLEAN WITH FIXES`, `BLOCKED`) of the tracked
  `<MEMORY_ROOT>/builds/*/reviews/*.md` records whose file date falls in the window. Every later unit
  whose clause says the Loop Review reads something appends one entry and names its line here. Observed
  by AC3 and AC4.
- **S6** — The window every reading uses. The walk calls `derive_loop_window(root, at)` once and hands
  the same `(start, end, days)` to `price` and to `gather`; the record's `**Window:**` field and the
  snapshot's are therefore one value. Observed by AC3.
- **S7** — `loop.file`, `run_loop_file(root, key, proposals, dry_run)`. A proposal is `{"kind", "id",
  "action", "accept", "row"}`, handed by the walk from the item routed to it (unit 5's `propose`), or
  by `--proposals <path>` with `--dry-run`. Each is keyed by the first 16 hex of the SHA-256 of
  `<ledger kind>\t<id>`, the key hash, and filed with `python <runtime kit>/intake.py file --origin
  cadence --filer item.loop.file`, its stable text on stdin carrying no period, `loop key <key hash> ·
  <kind> <id> · <action>`, and the clause tail `accept <accept>`: the content key is then the filing
  key's, so a recurrence appends its receipt to the open intake, route `seen`, and a new key is route
  `filed` (TOOL-dWellOiledMachine-4's content-key rule, the route TOOL-dTendedCadence-15 S2 takes). A
  proposal with an empty `accept` is refused, `loop — refused: <kind> <id> carries no accept line`, and
  nothing is filed for it. `--dry-run` prints each text and route and files nothing. No proposal: `loop —
  <key> · item.loop.file · 0 proposal(s)`. Observed by AC5.
- **S8** — `loop.record`, `render_loop_record(key, base, window, ledger, metrics, filed)` and
  `write_loop_record(root, ...)`, per §4 "The record", at `<MEMORY_ROOT>/loop-review/<date>-loop-review-<key>.md`,
  through a temp file and `os.replace`, contained under the home, the key held to §4 "The periods"
  before a path is built. The walk commits nothing: it files one records-only intake, `intake.py file
  --origin cadence --filer item.loop.record`, its stable text the record's and the snapshot's content as
  JSON, so the patch build that takes it re-writes both with `python loop_review.py record --key <key>
  --base <sha>`, the JSON on stdin, and lands them, as TOOL-dTendedCadence-1 S6 lands a maintenance
  record. Observed by AC6.
- **S9** — The registry row `loop-review` in `tools/memory-tree/record-kinds.toml`, §4 "The registry
  row". Observed by AC8.
- **S10** — The catalogue rows `review.loop.cadence` (`tools/policy/catalogue.toml:1283-1287`) and
  `review.loop.window-days` (`:1295-1300`) gain `summary` and `usage`, and `python
  tools/policy/policy.py lists --write` drains both from `tools/policy/unsummarised-keys.txt` (`:190`,
  `:193`); values and defaults stay the rows'. Observed by AC8.
- **S11** — The docs: `help/loop-review.md` gains the section "The Loop Review": the six items, the
  three periods and their keys, the `landings` field, the window, `run`, `--check` and `--dry-run`, and
  the record. Observed by AC9.
- **S12** — The fixture cases of §6 join `python loop_review.py --fixture`, which unit 2's leg `loop-review
  selftest` runs. Observed by AC1 and AC3 to AC7.

## 3. Non-goals (OUT)

- The ledger, its rows, its snapshot and `price`: unit 2.
- `loop.propose`, the keep record and `review.loop.retire`: unit 5. Until it lands the walk files the
  proposals nothing yet makes, so a period files none.
- The metrics other clauses name: delivery metrics (unit 11), instruction effectiveness (unit 5), the
  not-in-view share (unit 8), breach trends (unit 15) and the stall trend (unit 16), each a `METRICS`
  entry of its unit.
- The tick, the lease, the period witness, `derive_period` itself and the host adapters:
  dWellOiledMachine's, with the asks of §2 and §8 F2.
- The landing record: DEPL-dShippedRelease-1's. This unit counts it and writes none.
- A host key of the Loop Review's own: `maintain.host` serves both cadence programs (§8 F1).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-2` — the module `tools/loop/loop_review.py`, `read_loop_policy`, `derive_loop_window`, the `price` verb and its `item.loop.price` row, the snapshot path the record's `**Ledger:**` field names, and the home `loop-review/` check 3 admits
- **hands-off** `TOOL-dCalibratedLens-5` — the slot between `item.loop.price` and `item.loop.file`, which `item.loop.propose` takes, and the proposal shape `run_loop_file` reads
- **hands-off** `TOOL-dCalibratedLens-11` — `METRICS`, which gains the delivery metrics and the owner queue's depth
- **consumes-from** external — TOOL-dWellOiledMachine-59 and -13 with asks TOOL-dTendedCadence-27, -29 and -30 and §8 F2's ask; TOOL-dDeclaredLoop-12; TOOL-dWellOiledMachine-27 S1; TOOL-dTotalRecall-1; DEPL-dShippedRelease-1; each DEFERRED at base
- **hands-off** external — dWellOiledMachine builds §8 F2's ask, `derive_period`'s `monthly` and `every-n-landings` forms

## 4. Design

### Evidence

- The three keys exist and answer at base: `python tools/policy/policy.py get review.loop.cadence`
  prints `weekly` and `review.loop.window-days` prints `60` (`catalogue.toml:1283-1300`); both names
  sit in `unsummarised-keys.txt` (`:190`, `:193`).
- `derive_period` takes `daily` and `weekly` only (TOOL-dWellOiledMachine-13 S5), and ask
  TOOL-dTendedCadence-29 adds `every-session`: neither `monthly` nor `every-n-landings` has a key.
- Landings on the default branch: 180 first-parent merge commits in the 60 days to `8bec4cef`
  (`git rev-list --first-parent --merges --count --since=2026-09-03 8bec4cef`), 21 a week (PINNED,
  2026-11-02); 614 first-parent commits in the same days, so a first-parent count is not a landing count.
- No memory-root folder holds a period-keyed record but this build's: `loop-review/` is unit 2's (S8 of
  that spec).

### The periods

| `review.loop.cadence` | Period key | Form held by `read_loop_key` | Example at `2026-11-02T09:00:00Z` |
|---|---|---|---|
| `weekly` | the ISO week of `at` | `^\d{4}-W\d{2}$` | `2026-W45` |
| `monthly` | the UTC year and month of `at` | `^\d{4}-\d{2}$` | `2026-11` |
| `every-n-landings` | `n<k>.<sha12>`: `k` the count of landing records on the default branch's first-parent chain divided by `n`, rounded down, and `<sha12>` the first 12 hex of the `(k·n)`-th of them in chain order; `n` the row's `landings` | `^n\d+\.[0-9a-f]{12}$` | `n8.<sha12>` after 170 landings |

Under `every-n-landings` with fewer than `n` landings, `k` is 0 and no period is due: the tick prints
`cadence — loop-review · every-n-landings · <count> of <n> landings · not due` and runs nothing. Each
key passes the lease grammar's period segment, which admits a dot (TOOL-dPlacedRequest-18 S1, as
TOOL-dTendedCadence-2's `<event>.<sha12>` keys do).

### The items

| Item | Actor | Needs | Outcomes → routes | Witness |
|---|---|---|---|---|
| `item.loop.lease` | the executor, spelled as `item.maintain.lease` is (TOOL-dTendedCadence-1 S1) | none | `taken` → `item.loop.gather` | the period lease |
| `item.loop.gather` | `command:loop.gather` | `item.loop.lease` | `measured` → `item.loop.price` | the record's Metrics lines |
| `item.loop.price` (unit 2's, re-pointed) | `command:loop.price` | `item.loop.gather` | `priced` → `item.loop.file` | the snapshot |
| `item.loop.file` | `command:loop.file` | `item.loop.price` | `filed` → `item.loop.record` | one intake per (ledger kind, id) |
| `item.loop.record` | `command:loop.record` | `item.loop.file` | `recorded` → `transition` | the record |

### The record

```markdown
# Loop Review — 2026-W45

**Key:** 2026-W45
**Base:** <40-hex sha the walk read>
**Window:** 2026-09-03..2026-11-02 · 60d
**Ledger:** memory/loop-review/2026-11-02-value-ledger-2026-W45.md

## Metrics

surface: 148 legs · 152 gotchas · 270 keys · tools/gate-legs.json, memory/gotchas/, tools/policy/catalogue.toml
review-yield: 3/9/12 · memory/builds/*/reviews/*.md

## Filed

leg memory hygiene: seen · loop key 3f0c2a9b1e4d7a60
```

`<date>` is the UTC day of the write. The four `**Key:**` lines are the kind's `fields` form; each
Metrics line is `<name>: <value> · <source>`, one per `METRICS` entry in list order; each Filed line is
`<kind> <id>: <filed|seen> · loop key <key hash>`, or the single line `none`. The writer refuses a value
carrying a line break. The surface counts are the tree's at `8bec4cef` (PINNED, 2026-11-02) and the
rest of the sample is illustrative; every value is DERIVED at the walk.

### The registry row

```toml
[[record-kind]]
name = "loop-review"
tag = "record.loop-review"
layer = "layer.observability"
home = "<MEMORY_ROOT>/loop-review/"
id-rule = "<date>-loop-review-<key>.md"
schema = { form = "fields", fields = ["Key", "Base", "Window", "Ledger"] }
writer = "loop_review.py record"
readers = []
lifecycle = "written once per Loop Review period, never edited"
check = "record-kinds"
```

The home is the record home `point.memory.record-home` names for this layer's period-keyed kinds, the
`maintenance-record` sibling (TOOL-dTendedCadence-6 S6, S8).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `run_loop_walk`, `read_loop_items`, `read_loop_key`, `measure_loop_metrics`, `run_loop_file`, `render_loop_record`, `write_loop_record` | functions in `loop_review.py` | `py.function`, each answered OK by `lexicon.py --suggest` at base |
| `METRICS` | table in `loop_review.py` | none |
| `run`, `lease`, `gather`, `file`, `record` | `loop_review.py` verbs | none |
| `item.loop.lease`, `item.loop.gather`, `item.loop.file`, `item.loop.record` | item tags | none |
| `cadence.loop` | step value | none |
| `loop-review` | cadence row, its cadence segment, and record kind | none |
| `landings` | cadence-row field, §8 F2's ask | none |

### Files touched (estimate)

- `tools/loop/loop_review.py`: the walk, the four verbs and the fixture cases (S2, S3, S5 to S8, S12)
- `tools/loop/loop.toml`: four rows and the re-pointed `item.loop.price` (S1)
- `tools/runtime/points.toml`: the `loop-review` row (S4)
- `tools/memory-tree/record-kinds.toml`: the row (S9)
- `tools/policy/catalogue.toml` and `tools/policy/unsummarised-keys.txt` (S10)
- `help/loop-review.md` (S11)

### Alternatives rejected

- **Three literal rows, `loop-review-weekly`, `-monthly` and `-every-n`, each exiting when the key
  names another.** Each period's witness would certify a run that ran nothing, the test
  TOOL-dTendedCadence-2 §4 already ran for Maintain: a weekly key on the monthly row leaves four witnesses
  a month for one review.
- **A first-parent count as the landing count.** 614 first-parent commits against 180 landing merges in
  the 60 days to base: the period would turn about three times as often as the owner's `n` says.
- **The walk computing its own period.** The tick derives the period it leases; a program deriving a
  second one can disagree with its lease (ask TOOL-dTendedCadence-27's severity line).
- **A `seen` clause written into a backlog row.** The intake's content key already appends a receipt per
  recurrence (TOOL-dWellOiledMachine-4), so a second writer of the backlog row would be two answers to one
  question.

## 5. Production-readiness checklist

- security — every key is held to three anchored patterns before a path or ref is built from it, both
  writes are contained under the home and atomic, the intake text is passed on stdin with an argument
  list, and nothing read from a record reaches a shell; the walk commits and pushes nothing.
- perf / scale — once per period across the fleet, by the lease; gather is three file reads and one
  glob of review records, price unit 2's cost.
- error / empty / loading states — no key: exit 2 naming the route; a key of another form: exit 2; no
  review record in the window: `searched-none`; no proposal: the zero line; fewer than `n` landings: not
  due.
- observability — one line per item; the record is the period's history, the lease record its witness.
- risks — `maintain.host`'s default `session-start` runs the review at session start; under
  `os-scheduler` it moves to the node tick with Maintain.
- testing — §6's plants and §7's arm.
- migration — N/A: new rows and a new record kind; the catalogue values are unchanged.
- user docs — `help/loop-review.md` (S11).

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/loop_review.py --fixture --plant cadence-weekly` runs `lease --dry-run
  --key 2026-W45`, it prints `loop — 2026-W45 · item.loop.lease · taken`, and `--key 2026-11` exits 2
  naming the key and `weekly`; `cadence-monthly` takes `2026-11` and refuses `2026-W45`;
  `cadence-every-n-landings` takes `n2.0123456789ab` and refuses `2026-W45`; with no key and no
  `--dry-run` it exits 2 printing `run under cadence.py run loop-review`.
  Red when: a key of another value's form is taken, or a missing key runs the walk.
- **AC2** — When the plants `cadence-weekly`, `cadence-monthly` and `cadence-every-n-landings` run
  `python tools/runtime/cadence.py tick --dry-run --now 2026-11-02T09:00:00Z`, the `loop-review` row's
  period keys are `2026-W45`, `2026-11` and, over five planted landing records with `landings = 2`,
  `n2.` and the first 12 hex of the fourth; with one landing record it prints the not-due line.
  Red when: the row's period ignores `review.loop.cadence`, or a first-parent count stands for landings.
  permission: `cadence.py` is TOOL-dWellOiledMachine-59's, built with §8 F2's ask before this unit's build run.
  figure: keys DERIVED from the fixed `--now` and the planted refs.
- **AC3** — When the plant `window-30` commits `review.loop.window-days = 30` and runs `run --dry-run
  --key 2026-W45 --at 2026-11-02T09:00:00Z`, the record it prints and the snapshot price prints both read
  `2026-10-03..2026-11-02 · 30d`, and `review-yield` counts only the review records dated in that range.
  Red when: gather and price take different windows, or a review record outside it is counted.
- **AC4** — When the plant `no-reviews` runs `gather --dry-run`, it prints `review-yield: searched-none ·
  memory/builds/*/reviews/*.md` and a `surface` line with its three counts and sources.
  Red when: an empty source prints `0/0/0` and no `searched-none`.
- **AC5** — When the plant `file-proposals` runs `file --dry-run --proposals <path>` over two proposals
  for one `(kind, id)` and one with an empty `accept`, it prints one intake text whose key hash is the
  first 16 hex of SHA-256 over `leg\talpha`, the same hash for the second, carrying no period, and the
  refusal line for the third.
  Red when: a period enters the text, so each period files a second ask, or a proposal without an
  accept line is filed.
- **AC6** — When the plant `record` runs `record --key 2026-W45 --base <sha>` with the walk's JSON on
  stdin, it writes `<MEMORY_ROOT>/loop-review/<date>-loop-review-2026-W45.md` with the four fields of §4
  "The record", its `**Ledger:**` the snapshot path price wrote; `--key ../x` exits 2, writing nothing.
  Red when: a malformed key reaches a path, or the record names no snapshot.
- **AC7** — When `python tools/loop/loop_review.py run --check` runs over the tree, it prints `loop — 5
  item(s) · ok`; `run --dry-run --key 2026-W45` in the fixture prints the items in the order lease,
  gather, price, file, record, each with its outcome; the plant `dangling-route`, a route naming no row,
  exits 2 naming it.
  Red when: the walk runs out of `needs` order, or a dangling route passes.
- **AC8** — When `grep -n 'name = "loop-review"' tools/memory-tree/record-kinds.toml` and `grep -n -A8
  'name = "review.loop.cadence"' tools/policy/catalogue.toml` run, the first prints the row and the second
  shows `summary` and `usage`; `grep -cxE 'review\.loop\.(cadence|window-days)'
  tools/policy/unsummarised-keys.txt` prints `0`.
  Red when: either row lacks a field, or a name stays undrained.
- **AC9** — When `grep -n 'every-n-landings' help/loop-review.md` runs, it prints the section's line
  naming the period key form and the `landings` field.
  Red when: the section is absent.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `memory-hygiene self-test` · `build-index selftest` · `policy check` · `policy fixtures` · `docs` · `lexicon naming predicates` · `check-wiring self-test`

The fixture cases run in unit 2's leg `loop-review selftest`, which the manifest does not hold at base.

New arm: tools/loop/loop_review.py · covers AC1 AC3 AC4 AC5 AC6 AC7 · the `--fixture` plants, staged red by a key check that accepts any form, a gather that reads its own window, a filer whose text carries the period, and a walk that runs rows in file order · none

## 8. Open questions

- **F1 — Which host runs the Loop Review?** A cadence row requires a `host-key` naming a catalogue key
  (TOOL-dWellOiledMachine-59 S1), and no `review.loop.host` exists. (a) `maintain.host`, the observability
  expansion's host key, which the clause's "a cadence step of the observability expansion" names; (b) a
  new key, a public surface no clause names (veto 2); (c) `run.host`, the build runs' host. Rung 1, the
  clause names the expansion. RESOLVED (agent, 2026-11-02, delegated): (a), S4. widens: none · relaxes:
  none
- **F2 — How do `monthly` and `every-n-landings` get a period key?** `derive_period` knows `daily` and
  `weekly`, and the clause asks every value seen on its planted case. (a) Ask dWellOiledMachine for both
  forms of §4 "The periods", `n` a row field `landings`; (b) literal rows that exit when the key names
  another, which certify empty periods (§4); (c) the program deriving its own period, which can disagree
  with its lease. Rung 3, (a) the only option keeping one period per lease. RESOLVED (agent, 2026-11-02,
  delegated): (a), a new ask the main loop files · dWellOiledMachine · THE PERIOD KEY HAS NO MONTH AND NO
  LANDING COUNT: `derive_period` gains `monthly`, the UTC `YYYY-MM` of `at`, and `every-n-landings`,
  `n<k>.<sha12>` over the landing records (DEPL-dShippedRelease-1) on the default branch's first-parent
  chain, `n` the cadence row's `landings` field, which `check_cadence_row` admits as a positive integer
  on a row whose `period-key` admits `every-n-landings`, and fewer than `n` landings is not due · accept
  the tick over a `period-key` row prints `2026-11` under `monthly` at `2026-11-02T09:00:00Z`, and under
  `every-n-landings` with `landings = 2` over five landing records `n2.` and the fourth's sha12, seen on
  three plants. Build-run precondition. widens: none · relaxes: none
- **F3 — What is `n`?** No record states it: the owner's R1 answer is "Weekly by default,
  owner-adjustable" (walkthrough:735). (a) A row field set from the measured landings per week, 21 at
  base (PINNED, 2026-11-02), so the value's default cadence matches the key's default and the owner edits
  one tracked number; (b) a new catalogue key, a public surface no clause names (veto 2); (c) a constant
  in the tick, which the owner cannot adjust without a code change. Rung 3. RESOLVED (agent, 2026-11-02,
  delegated): (a), S4's `landings = 21`. widens: none · relaxes: none
- **F4 — Which unit ships the module?** The brief's S3 gives it to this unit and its order puts unit 2
  first. RESOLVED (agent, 2026-11-02, delegated): unit 2 creates it with `price`, and this unit adds its
  verbs, as unit 2's §8 F1 settles. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft.

## 10. Reuse audit

The seams extended: unit 2's module and `derive_loop_window`; the cadence row, tick and period witness
of TOOL-dWellOiledMachine-59 S1 to S3 and -13 S5, S6 with asks TOOL-dTendedCadence-27, -29, -30 and §8
F2's; the walk TOOL-dTendedCadence-1 S2 gives Maintain, over TOOL-dDeclaredLoop-12's `order_by_needs`;
`intake.py file --origin cadence` (TOOL-dWellOiledMachine-27 S1) for the asks and the records-only
landing, as TOOL-dTendedCadence-15 S2 and -1 S6 use it; the record shape and contained atomic write of
the maintenance record (TOOL-dTendedCadence-6 S6, `tools/runlog/record.py:1179-1201`); the registry of
TOOL-dTotalRecall-1. The probe `python tools/codebase-map/reuse_lookup.py "run a review program once per
period under a lease, gather metrics from committed records and write one record per period"` ranked
name stems only (`run`, `write`, `records`, `build_run_model`, `resolveLease` in
`tools/unattended/run-lease.js`, the run lease and not a period lease), so no existing seam fits the walk
at base and it is new over the parent seams above. Where the brief and source disagree at this base: the
brief's period form `n<k>.<landing-sha12>` counts landing records, and a first-parent commit count is
not one (§4 Evidence), so S4 and F2 count DEPL-dShippedRelease-1's records.

Recall terms used: `python tools/memory-recall/query.py "how is a gate leg priced by its catches and
cost, and how does a periodic loop review retire what catches nothing" --terms "value ledger loop review
catches false reds window retire price leg cadence lease snapshot"`
