# TOOL-dCalibratedLens-3 — the Loop Review: a cadence step run as `review.loop.cadence` says, its lease keyed by the selected period, its walk and its record

**Status:** DEFERRED · rev-7 · 2026-11-04 · node a · Tier-2 · base 8bec4cef · streams tooling · order 2 · advances TOOL-dCalibratedLens-18

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
| [2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md) | journal | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |
| [2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-42 |
| [2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-reground-returns.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-reground-returns.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-42 |
| [2026-11-03-build-TOOL-dCalibratedLens-1-crosscheck-returns.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-crosscheck-returns.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 |
| [2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-parents-crosscheck.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46 |
| [2026-11-03-build-TOOL-dCalibratedLens-1-reground-returns.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-reground-returns.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46 |
| [2026-11-03-build-TOOL-dCalibratedLens-3-deviation-32.md](../build/2026-11-03-build-TOOL-dCalibratedLens-3-deviation-32.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-3-deviation-33.md](../build/2026-11-03-build-TOOL-dCalibratedLens-3-deviation-33.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-3-deviation-34.md](../build/2026-11-03-build-TOOL-dCalibratedLens-3-deviation-34.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-3-deviation-35.md](../build/2026-11-03-build-TOOL-dCalibratedLens-3-deviation-35.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-3-deviation-36.md](../build/2026-11-03-build-TOOL-dCalibratedLens-3-deviation-36.md) | deviation | — |
| [2026-11-04-build-TOOL-dCalibratedLens-1-audit-disposal-returns.md](../build/2026-11-04-build-TOOL-dCalibratedLens-1-audit-disposal-returns.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-24 |
| [2026-11-04-build-TOOL-dCalibratedLens-3-deviation-37.md](../build/2026-11-04-build-TOOL-dCalibratedLens-3-deviation-37.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-edge-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-edge-fix-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-15 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-48 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-42 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-29 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-crosscheck.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-crosscheck.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-46 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-3-1-spec-reviewer.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-3-1-spec-reviewer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-3-2-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-3-2-spec-writer.md) | journal | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-3-3-spec-writer.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-3-3-spec-writer.md) | journal | — |
| [2026-11-04-prompt-TOOL-dCalibratedLens-1-crosscheck-audit-disposal.md](../prompts/2026-11-04-prompt-TOOL-dCalibratedLens-1-crosscheck-audit-disposal.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-24 |
| [2026-11-04-prompt-TOOL-dCalibratedLens-3-1-spec-writer.md](../prompts/2026-11-04-prompt-TOOL-dCalibratedLens-3-1-spec-writer.md) | journal | — |
| [2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-14 |
| [2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit.md](../reviews/2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-46 |

<!-- /gen:spec-records -->

## 1. Goal

No retrospective reads the loop's own metrics (gap-review-02). This unit lands the Loop Review,
registered as a cadence step of the observability expansion and run as `review.loop.cadence` says,
`weekly`, `monthly` or `every-n-landings`, its lease keyed by the selected period, each value seen on its
planted case. It is one program, `python tools/loop/loop_review.py run`, walking the five `item.loop.*`
rows in `needs` order under the period lease, every reading taking the one window
`review.loop.window-days` sets (default 60), and writing one `loop-review` record per period. Unit 5 adds the sixth row, `item.loop.propose` (id 13).

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`: TOOL-dCalibratedLens-2 (the module,
`read_loop_policy`, `derive_loop_window`, `price` and the home `loop-review/`); TOOL-dWellOiledMachine-59
S1 to S3 (`point.cadence-items`, `check_cadence_row`, the tick) and -13 S5, S6 (`derive_period`,
`run_cadence_period`), with asks TOOL-dTendedCadence-27 (`GOV_CADENCE_KEY`), TOOL-dTendedCadence-29
(`period-key`) and TOOL-dTendedCadence-30 (the `session-start` host) and TOOL-dWellOiledMachine-128 (§8 F2);
TOOL-dDeclaredLoop-12 (the item rows, `check_program`, `order_by_needs` and its inline `needs_graph_py`
block) with ask TOOL-dDeclaredLoop-110 (§8 F5), each ask filed in its build's `BACKLOG.md`; TOOL-dWellOiledMachine-27 S1 (`intake.py file --origin cadence`); TOOL-dTotalRecall-1 (the
registry); DEPL-dShippedRelease-1 (the landing records `every-n-landings` counts). The build run
re-grounds on each and stops the unit when one is absent.

- **S1** — (amended, id 26) The rows. Four `[[item]]` rows in `tools/loop/loop.toml`, in TOOL-dDeclaredLoop-12 §4's row
  form, `step = "cadence.loop"`, `owner = "dCalibratedLens"`, as §4 "The items" tabulates:
  `item.loop.lease`, `item.loop.gather`, `item.loop.file` and `item.loop.record`. This unit re-points
  unit 2's `item.loop.price` row: `needs = ["item.loop.gather"]` and `routes = { priced =
  "item.loop.file" }`; unit 5 inserts `item.loop.propose` between them. Observed by AC7.
- **S2** — (amended, ids 25, 49) The walk, `run_loop_walk(root, key, dry_run)`, run as `python loop_review.py run [--check]
  [--dry-run] [--key <key>]`. `read_loop_items(kit_dir)` reads the `step = "cadence.loop"` rows with
  `tomllib` and orders them with `order_by_needs`; a need naming no row, a cycle, an outcome with no
  route and a route naming no row nor a `stand-in:<path>` each exit 2 with one line. `--check` stops
  there, printing `loop — <n> item(s) · ok`. Otherwise each item runs once every item it needs has run,
  handed the outcomes routed to it, and prints `loop — <key> · <item tag> · <outcome>`; the walk exits 0
  once `item.loop.record` has run, and exits 1 when an item raises or refuses, so `run_cadence_period`
  releases the lease as a hand-over and the next wake runs the period again
  (TOOL-dWellOiledMachine-13 S6 step 5). It keeps no re-run journal, the one TOOL-dTendedCadence-48 S28
  gives Maintain's walk: the record is checked before the first filing (TOOL-dCalibratedLens-27 S1), so a
  re-run after a filing follows a failed final write and re-files each proposal as one `seen` receipt on
  the intake already open, never a second intake.
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
  the key's value through `derive_period`, whose `monthly` and `every-n-landings` forms are ask
  TOOL-dWellOiledMachine-128 (§8 F2). Observed by AC1 and AC2.
- **S5** — (amended, ids 2, 49) `loop.gather`, `measure_loop_metrics(root, window)`: each entry of `METRICS`, a list of
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
- **S7** — (amended, id 3) `loop.file`, `run_loop_file(root, key, proposals, dry_run)`. A proposal is `{"kind", "id",
  "action", "accept", "row"}`, handed by the walk from the item routed to it (unit 5's `propose`), or
  by `--proposals <path>` with `--dry-run`. Each is keyed by the first 16 hex of the SHA-256 of
  `<ledger kind>\t<id>`, the key hash, and filed with `python <runtime kit>/intake.py file --origin
  cadence --filer item.loop.file`, its stable text on stdin carrying no period, `loop key <key hash> ·
  <kind> <id> · <action>`, and the clause tail `accept <accept>`: the content key is then the filing
  key's, so a recurrence appends its receipt to the open intake, route `seen`, and a new key is route
  `filed` (TOOL-dWellOiledMachine-4's content-key rule, the route TOOL-dTendedCadence-15 S2 takes). A
  proposal with an empty `accept` is refused, `loop — refused: <kind> <id> carries no accept line`, and
  nothing is filed for it; (r2 id 7) that line is the proposal's own refusal and not the file item's,
  so the walk goes on, the other proposals are filed once, and the period records. `--dry-run` prints each text and route and files nothing. No proposal: `loop —
  <key> · item.loop.file · 0 proposal(s)`. Observed by AC5.
- **S8** — (amended, id 30) `loop.record`, `render_loop_record(key, base, window, ledger, metrics, filed)` and
  `write_loop_record(root, ...)`, per §4 "The record", at `<MEMORY_ROOT>/loop-review/<date>-loop-review-<key>.md`,
  through a temp file and `os.replace`, contained under the home, the key held to §4 "The periods"
  before a path is built. The walk commits nothing: it files one records-only intake, `intake.py file
  --origin cadence --filer item.loop.record`, its stable text the record's and the snapshot's content as
  JSON, so the patch build that takes it re-writes both with `python loop_review.py record --key <key>
  --base <sha>`, the JSON on stdin, and lands them; the commit landing the first period's record and its
  snapshot also edits both the `loop-review` row and unit 2's `value-ledger` row to carry no `unarmed`
  key (TOOL-dTotalRecall-42 S2), which AC8 observes on both. The JSON is never cut: the pre-render
  (TOOL-dCalibratedLens-27 S1) builds it with every route `pending`, the longest route word, and over
  `INTAKE_CAP_BYTES` (65536, TOOL-dWellOiledMachine-4 S2) exits 1, `loop — refused: record text <n>
  bytes over INTAKE_CAP_BYTES`, filing nothing. A span `render_redacted` replaces lands as its
  placeholder, and no digest covers the text (TOOL-dTendedCadence-49 rejects the JSON for its digest);
  `record` exits 2 on stdin that is not JSON. Observed by AC6 and AC10.
- **S9** — (amended, ids 1, 36, 37) The registry row `loop-review` in `tools/memory-tree/record-kinds.toml`, §4 "The registry
  row". Observed by AC8.
- **S10** — The catalogue rows `review.loop.cadence` (`tools/policy/catalogue.toml:1283-1287`) and
  `review.loop.window-days` (`:1295-1300`) gain `summary` and `usage`, and `python
  tools/policy/policy.py lists --write` drains both from `tools/policy/unsummarised-keys.txt` (`:190`,
  `:193`); values and defaults stay the rows'. Observed by AC8.
- **S11** — (amended, id 39) The docs: `help/loop-review.md` gains the section "The Loop Review": the six items, the
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
- **hands-off** `TOOL-dCalibratedLens-4` — `tools/loop/loop_review.py`, its `gather`, `record` and `file` verbs and the `loop-review` record kind, which carry its caps step, its `caps` field and its proposals
- **hands-off** `TOOL-dCalibratedLens-6` — `tools/loop/loop_review.py`, its `gather`, `record` and `file` verbs and the `loop-review` record kind, which carry its field and its proposals
- **hands-off** `TOOL-dCalibratedLens-8` — `METRICS`, which the `not-in-view-share` entry joins, `run_loop_file` and the `loop-review` record
- **hands-off** `TOOL-dCalibratedLens-9` — `METRICS`, which gains the `compactions` entry, and the window the walk hands every reading
- **hands-off** `TOOL-dCalibratedLens-10` — `METRICS` and `run_loop_file`, through which its proposal is filed
- **hands-off** `TOOL-dCalibratedLens-12` — the window the walk hands `price`
- **hands-off** `TOOL-dCalibratedLens-14` — the `loop-review` record and the `gather` and `file` verbs, which it extends and hands its proposals to
- **hands-off** `TOOL-dCalibratedLens-15` — `METRICS`, which gains `cap-breaches` and `cap-counted`; `run_loop_walk` and the proposal shape `run_loop_file` reads; the record's Metrics lines and its home
- **hands-off** `TOOL-dCalibratedLens-16` — `tools/loop/loop_review.py`, its `gather`, `record` and `file` verbs and the `loop-review` record kind, which carry its fields and its proposals
- **hands-off** `TOOL-dCalibratedLens-17` — `METRICS`, which gains four entries, the record whose Metrics lines carry them, its home the trend reads, and the `--fixture` plants its cases join
- **consumes-from** external — TOOL-dWellOiledMachine-59 and -13 with asks TOOL-dTendedCadence-27, -29 and -30 and §8 F2's ask; TOOL-dDeclaredLoop-12; TOOL-dWellOiledMachine-27 S1; TOOL-dTotalRecall-1; DEPL-dShippedRelease-1; each DEFERRED at base
- **hands-off** external — dWellOiledMachine builds §8 F2's ask, `derive_period`'s `monthly` and `every-n-landings` forms
- **hands-off** `TOOL-dCalibratedLens-19` — `write_loop_record`, the `loop-review` row and the `--fixture` frame that unit's `three-homes` plant joins (id 1)
- **hands-off** `TOOL-dCalibratedLens-20` — `render_loop_record`, `write_loop_record` and the `--fixture` frame, which that unit's `serves-kinds` plant grades (id 36)
- **hands-off** `TOOL-dCalibratedLens-21` — `measure_loop_metrics` and `render_loop_record`, the list-answer writer that unit's `metrics-multi` plant writes through (id 2)
- **hands-off** `TOOL-dCalibratedLens-22` — `run_loop_walk` and `run_loop_file`, the one proposal route that unit's `every-proposer` plant proves (id 3)
- **hands-off** `TOOL-dCalibratedLens-27` — `run_loop_walk` and `render_loop_record`, the isolated readers and the pre-render that unit's `reader-raises` and `record-refuses` plants prove (id 49)
- **hands-off** `TOOL-dCalibratedLens-30` — `read_loop_records` and the walk's window, which the minors batch's `keep-after-review` and `at-year-back` arms run (ids 6, 30)
- **hands-off** `TOOL-dCalibratedLens-39` — `read_metrics_lines` and `render_loop_record`, whose list-of-triples answer that unit's `metrics-repeat` plant holds (round-2 id 27)
- **hands-off** `TOOL-dCalibratedLens-40` — the walk's isolation boundary and `read_metrics_lines`, whose folded `<why>` that unit's `reader-raises-multiline` case reads (round-2 id 31)
- **hands-off** `TOOL-dCalibratedLens-43` — `read_loop_records` and the `--fixture` frame, whose prefix listing that unit's `records-listed` plant holds (round-3 id 11)

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

Each of the four rows also carries the keys TOOL-dDeclaredLoop-12 §4 requires of a non-role actor
(TOOL-dDeclaredLoop-9 S1, S4), in the form unit 2 S9 uses: `returns = "record-kind.loop-review"`;
`allowance = "none"` on `lease` and `gather` and `allowance = "records"` on `file` and `record`, each one
word of `WRITES` (`tools/roles/check_roles.py:96`); and `witness = { class = "<class>", by = "<the
table's Witness cell>" }`. The class is `history` on `lease` (a ref), `gather` and `record` (a tracked
file), and `hook-record` on `file`: its intake is node-local and never committed
(TOOL-dWellOiledMachine-4 S1), so it is no `history` fact, and it is written through that hook's one
writer `write_intake` (TOOL-dWellOiledMachine-27 S1), the class TOOL-dDeclaredLoop-5's table gives a
record a hook writes. `inputs` is `["layer.runtime:GOV_CADENCE_KEY"]` on `lease`, and
`["layer.observability:<what it reads>"]` on the others: the `METRICS` sources, the proposals, the walk's
readings. `python loop_lib.py --check` passes the four rows (AC7).

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

§6 runs a sibling's file by its basename: `cadence.py` is `tools/runtime/cadence.py` (TOOL-dWellOiledMachine-59).

### Amendments (round-1 spec audit)

The round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Each bullet supersedes the text it
names; the unit it names owns the finding and its proof.

- **id 1 · §4 "The registry row" (H1, `TOOL-dCalibratedLens-19`)** —
  `home = "memory/loop-review/*-loop-review-*.md"`, the glob of the row's id-rule, as
  TOOL-dTotalRecall-42 S1 spells the shape-run home.
- **id 36 · §4 "The record" (H2, `TOOL-dCalibratedLens-20`)** — The record's third line is
  `**Serves:** loop-review TOOL-dCalibratedLens-3`, and `loop-review` joins the untyped part of
  `RECORD_KIND_TOKENS` in `tools/memory-tree/tree_lib.py` (TOOL-dTotalRecall-18 S7), an untyped kind as
  TOOL-dTotalRecall-1 S2 registers them, and HYGIENE's closed `<kind>` list in this pass: PLAY-dOrderedCharter-42
  S2 and S3 tie `TYPED_RECORD_KINDS` to the factory's table and its `-<kind>-<n>.md` name.
- **id 2 · S5, §4 "The record" (H3, `TOOL-dCalibratedLens-21`)** — A `METRICS` reader may answer a
  single pair or a reader answering a LIST of `(value, source)` pairs, each written as its own
  Metrics line `<name>: <value> · <source>` in list order; a reading never adds a `fields`-form
  field, so the row's fields stay `Key`, `Base`, `Window` and `Ledger`, and the writer's refusal of
  a value carrying a line break stands.
- **id 3 · S7 (H4, `TOOL-dCalibratedLens-22`)** — Every item's step answers `(outcome, proposals)`;
  the walk appends each item's proposals in item order, and `item.loop.file` files the whole list. A
  gather-time proposal and a `propose`-time one take this one route, and TOOL-dCalibratedLens-15
  F5's extension is an instance of it.
- **id 49 · S2, S5 (H9, `TOOL-dCalibratedLens-27`)** — Each `METRICS` reader and each proposer runs
  under its own `try`; a raise or a refusal becomes that entry's Metrics line
  `<name>: unread · <why>`, or for a proposer the line `loop — <key> · <proposer> · unread · <why>`
  and no proposal, never the walk's exit. Before `item.loop.file` files anything the walk renders
  the record once through `render_loop_record` with every proposal marked `pending`, so a writer
  refusal exits 1 before any intake is filed. S2's exit 1 on a raise or refusal now applies to the
  lease, price, file and record items only.
- **id 11 · §4 "The record" (L1, `TOOL-dCalibratedLens-30`)** — Two states, one spelling each, for
  every reading of the set: `searched-none · <path or glob>` is a source read that holds nothing (an
  absent runlog journal file included, which the runlog kit reads as nothing written yet), and
  `unread · <reason>` a source that could not be read (a refused or timed-out read, an absent kit,
  an unparsable answer).
- **id 30 · S8 (M14, `TOOL-dCalibratedLens-30`)** — The one reader of earlier records:
  `read_loop_records(root, window=None)` in `loop_review.py` lists the committed
  `memory/loop-review/*-loop-review-*.md` with `git ls-files`, orders them by file-name date and
  then key, reads each at `HEAD` through `git show`, and keeps those in the window when one is
  given; `read_metrics_lines(text)` splits a record's Metrics section on the first `: ` and the last
  ` · `. Units 5 S7, 15 S6, 16 S6 and 17 S5 call these two and keep only their own line parsers.
- **id 25 · S2, §4 Inventory (M9, `TOOL-dCalibratedLens-30`)** — The rows are read through
  `loop_lib.read_items(kit_dir, step="cadence.loop")` (TOOL-dDeclaredLoop-12 S1), and every refusal
  `check_program` grades comes from it; `read_loop_items` is not minted. The refusals it cannot
  grade for a stepless cadence program stay in the walk under a `ponytail:` comment naming ask
  TOOL-dTendedCadence-25 as the upgrade (§8 F5).
- **id 26 · S1, §8 F5 (M10, `TOOL-dCalibratedLens-30`)** — §8 gains F5, which places the rows
  against TOOL-dTendedCadence-1 F1 and ask TOOL-dTendedCadence-25, and states the ask on
  dDeclaredLoop that admits `cadence.loop`, filed as TOOL-dDeclaredLoop-110.
- **id 37 · §4 "The registry row", AC8 (M17, `TOOL-dCalibratedLens-30`)** — The row carries
  `unarmed = "no record yet; its writer is loop_review.py record"` (TOOL-dTotalRecall-42 S2). The
  commit that lands S8's first record and its snapshot drops `unarmed` from both the `loop-review` and
  the `value-ledger` rows, and AC8 observes both drops; AC8 also runs `python tools/memory-tree/record_kinds.py --check` after the
  pass: exit 0.
- **id 38 · Files touched, §7 (M18, `TOOL-dCalibratedLens-30`)** — After the row edit the pass runs
  `python tools/memory-tree/record_kinds.py --write`, then `adopt-memory-tree.sh --render`;
  `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md` land in the same commit.
- **id 39 · S11 (M19, `TOOL-dCalibratedLens-30`)** — `tools/govkit/usage.toml` gains a `[[usage]]`
  row for each of `run`, `lease`, `gather`, `file` and `record`, with their flags, and the page's
  usage anchor is re-fingerprinted.
- **id 13 · §1 (L3, `TOOL-dCalibratedLens-30`)** — Corrected in place: the walk covers five rows at
  this unit's landing, and unit 5 adds the sixth.
- **id 12 · AC6 (L2, `TOOL-dCalibratedLens-30`)** — Corrected in place: AC6's `**Ledger:**` is the
  snapshot path `record` writes beside the record.

### Amendments (round-2 spec audit)

The round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Its ids restart at 1, so each bullet
spells `r2 id`; each supersedes the text it names, and the unit it names owns the finding and its
proof.

- **r2 id 27 · S8, id 30's bullet (H6, `TOOL-dCalibratedLens-39`)** — `read_metrics_lines(text)`
  returns a list of `(name, value, source)` triples, one per line of the `## Metrics` section in the
  order the lines appear, a repeated name kept as one triple per line, each line split on its first
  `: ` and its last ` · `; a line with no `: ` or no ` · ` is a `ValueError` naming it. No caller reads
  the answer as a mapping.
- **r2 id 31 · S2, S5, id 49's bullet (H7, `TOOL-dCalibratedLens-40`)** — At the isolation boundary
  `<why>` is `<exception class>: <message>` with every line break made a space and every ` · ` made
  `, `; and a reading whose answered value or source carries a line break is written
  `<name>: unread · refused value`, never handed to the writer. No isolation path exits the walk.
- **r2 id 7 · S2, S7, id 49's bullet (M4, `TOOL-dCalibratedLens-41`)** — An empty-`accept` refusal is
  a per-proposal line and not the file item's refusal, so S2's exit 1 does not follow from it.
- **r2 id 22 · S2, S5, id 49's bullet (M11, `TOOL-dCalibratedLens-41`)** — The gather item's outcome
  line counts its unread readings: `loop — <key> · item.loop.gather · measured · <n> unread:
  <names>`, the plain `measured` when n is 0.
- **r2 id 20 · id 30's bullet (M5, `TOOL-dCalibratedLens-41`)** — The callers of
  `read_loop_records` and `read_metrics_lines` are units 5 S7, 6 S6, 15 S6, 16 S6 and 17 S5.
- **r2 id 38 · id 30's bullet (M5, `TOOL-dCalibratedLens-41`)** — `read_loop_records` lists
  `git ls-tree -r --name-only HEAD -- 'memory/loop-review/*-loop-review-*.md'`, the revision it reads
  each record at, never `git ls-files`, so a record staged and not committed is neither listed nor
  read.

### Amendments (round-3 spec audit)

The round-3 spec audit
(`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`) confirmed the
findings below, and its disposal amended this text. Its ids restart at 1, so each bullet spells
`r3 id`; each supersedes the text it names, and the unit it names owns the finding and its proof.

- **r3 id 11 · r2 id 38's bullet, id 30's bullet (H2, `TOOL-dCalibratedLens-43`)** —
  `read_loop_records` lists `git ls-tree -r --name-only HEAD -- memory/loop-review/`, the folder
  prefix, and keeps a name only when `fnmatch.fnmatchcase(name,
  "memory/loop-review/*-loop-review-*.md")` holds: `git ls-tree` matches a path as a literal prefix
  and never as a glob, so the r2 bullet's glob form lists nothing. It still reads the revision and
  never the index, so a record staged and not committed is neither listed nor read.
- **r3 id 33 · r2 id 27's bullet (L7, `TOOL-dCalibratedLens-48`)** — `read_metrics_lines(text)` reads
  the lines after the `## Metrics` heading up to the next line opening `## ` or the end of the text,
  and skips a blank line; every other line is one triple or a `ValueError` naming it.
- **r3 id 32 · r2 id 31's bullet (M15, `TOOL-dCalibratedLens-48`)** — For a reading that answers a
  list of pairs, the refusal of a value or source carrying a line break is per entry: that entry is
  written `<name>: unread · refused value` in its place in list order, and the reading's other
  entries are written as answered. A scalar answer is the one-entry case.

### Files touched (estimate)

- `tools/loop/loop_review.py`: the walk, the four verbs and the fixture cases (S2, S3, S5 to S8, S12)
- `tools/loop/loop.toml`: four rows and the re-pointed `item.loop.price` (S1)
- `tools/runtime/points.toml`: the `loop-review` row (S4)
- `tools/memory-tree/record-kinds.toml`: the row (S9)
- `tools/policy/catalogue.toml` and `tools/policy/unsummarised-keys.txt` (S10)
- `help/loop-review.md` (S11)
- `tools/memory-tree/tree_lib.py` — `RECORD_KIND_TOKENS`' untyped part gains `loop-review` (id 36)
- `tools/memory-tree/HYGIENE.template.md` and its render `memory/HYGIENE.md` — the kind list and the re-rendered registry region (ids 36, 38)
- `tools/govkit/usage.toml` — the `[[usage]]` row of each verb or flag added (id 39)

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
  review record in the window: `searched-none`; a record text over `INTAKE_CAP_BYTES`: exit 1, nothing filed; no proposal: the zero line; fewer than `n` landings: not
  due.
- observability — one line per item; the record is the period's history, the lease record its witness.
- risks — `maintain.host`'s default `session-start` runs the review at session start; under
  `os-scheduler` it moves to the node tick with Maintain.
- testing — §6's plants and §7's arm.
- migration — N/A: new rows and a new record kind; the catalogue values are unchanged.
- user docs — `help/loop-review.md` (S11).

## 6. Acceptance criteria

- **AC1** — When `python loop_review.py --fixture --plant cadence-weekly` runs `lease --dry-run
  --key 2026-W45`, it prints `loop — 2026-W45 · item.loop.lease · taken`, and `--key 2026-11` exits 2
  naming the key and `weekly`; `cadence-monthly` takes `2026-11` and refuses `2026-W45`;
  `cadence-every-n-landings` takes `n2.0123456789ab` and refuses `2026-W45`; with no key and no
  `--dry-run` it exits 2 printing `run under cadence.py run loop-review`.
  Red when: a key of another value's form is taken, or a missing key runs the walk.
- **AC2** — When the plants `cadence-weekly`, `cadence-monthly` and `cadence-every-n-landings` run
  `python cadence.py tick --dry-run --now 2026-11-02T09:00:00Z`, the `loop-review` row's
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
- **AC6** — (amended, id 12) When the plant `record` runs `record --key 2026-W45 --base <sha>` with the walk's JSON on
  stdin, it writes `<MEMORY_ROOT>/loop-review/<date>-loop-review-2026-W45.md` with the four fields of §4
  "The record", its `**Ledger:**` the snapshot path `record` writes beside it (id 12); `--key ../x` exits 2, writing nothing.
  Red when: a malformed key reaches a path, or the record names no snapshot.
- **AC7** — When `python loop_review.py run --check` runs over the tree, it prints `loop — 5
  item(s) · ok`; `run --dry-run --key 2026-W45` in the fixture prints the items in the order lease,
  gather, price, file, record, each with its outcome; the plant `dangling-route`, a route naming no row,
  exits 2 naming it; `python loop_lib.py --check` over the tree exits 0, refusing none of the four rows.
  Red when: the walk runs out of `needs` order, a dangling route passes, or a row's allowance is not a
  word of `WRITES` or its witness carries no class.
  permission: `loop_lib.py` is TOOL-dDeclaredLoop-12's, built with ask TOOL-dDeclaredLoop-110 before this unit's build run.
- **AC8** — (amended, id 37) When `grep -n 'name = "loop-review"' record-kinds.toml` and `grep -n -A8
  'name = "review.loop.cadence"' tools/policy/catalogue.toml` run, the first prints the row and the second
  shows `summary` and `usage`; `grep -cxE 'review\.loop\.(cadence|window-days)'
  tools/policy/unsummarised-keys.txt` prints `0`; in a scratch worktree committing one record and one
  snapshot, `record_kinds.py --check` exits 1 naming `unarmed` while either the `loop-review` or the
  `value-ledger` row keeps the key, and 0 only once that commit drops it from both.
  Red when: either row lacks a field, a name stays undrained, or the key outlives the first record on
  either row.
- **AC9** — When `grep -n 'every-n-landings' loop-review.md` runs, it prints the section's line
  naming the period key form and the `landings` field.
  Red when: the section is absent.
- **AC10** — When the plant `over-cap`, a planted ledger whose snapshot is over 64 KiB, runs `run` with
  `GOV_CADENCE_KEY=2026-W45` and a counting stub for the intake filer, it exits 1 printing `over
  INTAKE_CAP_BYTES`, and the stub's count reads 0.
  Red when: a text over the cap is filed, and cut.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `memory-hygiene self-test` · `build-index selftest` · `policy check` · `policy fixtures` · `docs` · `lexicon naming predicates` · `check-wiring self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

The fixture cases run in unit 2's leg `loop-review selftest`, which the manifest does not hold at base.

New arm: tools/loop/loop_review.py · covers AC1 AC3 AC4 AC5 AC6 AC7 AC10 · the `--fixture` plants, staged red by a key check that accepts any form, a gather that reads its own window, a filer whose text carries the period, a record text filed at any length, and a walk that runs rows in file order · none

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
  with its lease. Rung 3, (a) the only option keeping one period per lease. RESOLVED (agent, 2026-11-03,
  delegated): (a), ask TOOL-dWellOiledMachine-128 in `memory/builds/dWellOiledMachine/BACKLOG.md`, THE
  PERIOD KEY HAS NO MONTH AND NO LANDING COUNT, whose row holds the forms and the accept. Build-run
  precondition. widens: none · relaxes: none
- **F3 — What is `n`?** No record states it: the owner's R1 answer is "Weekly by default,
  owner-adjustable" (walkthrough:735). (a) A row field set from the measured landings per week, 21 at
  base (PINNED, 2026-11-02), so the value's default cadence matches the key's default and the owner edits
  one tracked number; (b) a new catalogue key, a public surface no clause names (veto 2); (c) a constant
  in the tick, which the owner cannot adjust without a code change. Rung 3. RESOLVED (agent, 2026-11-02,
  delegated): (a), S4's `landings = 21`. widens: none · relaxes: none
- **F4 — Which unit ships the module?** The brief's S3 gives it to this unit and its order puts unit 2
  first. RESOLVED (agent, 2026-11-02, delegated): unit 2 creates it with `price`, and this unit adds its
  verbs, as unit 2's §8 F1 settles. widens: none · relaxes: none
- **F5 — Where do the `item.loop.*` rows live, given `step = "cadence.loop"`?** TOOL-dTendedCadence-1 F1 put
  Maintain's rows in its engine kit's descriptor and rejected the core `loop.toml` "against EX-1", citing ask
  TOOL-dTendedCadence-25 (`read_items` reads only `loop.toml`, and `check_program` needs a `[[step]]` exit row a
  cadence program lacks); TOOL-dDeclaredLoop-50 S3 admits only `step = "none"`, on `item.review.*` rows. Options:
  (a) the rows in a kit descriptor of the observability expansion, read under ask 25's reader; (b) the rows in
  `tools/loop/loop.toml`, beside the module `tools/loop/loop_review.py` the brief's shared interface S3 places in the
  loop kit, with an ask on dDeclaredLoop to admit `cadence.loop`; (c) a `[[step]]` row `cadence.loop`, a public surface
  no clause names (veto 2). (a) has no kit to hold the rows: the Loop Review's module is the loop kit's and no
  observability kit exists, a new install location (veto 2). Rung 3, spec audit id 26. RESOLVED (agent, 2026-11-03,
  delegated): (b), ask TOOL-dDeclaredLoop-110 in `memory/builds/dDeclaredLoop/BACKLOG.md`, THE LOOP KIT REFUSES A
  CADENCE STEP VALUE, whose row holds the accept. A build-run precondition of unit 2's AC8 and of S2. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft.
- rev-2 · 2026-11-02 · §1 §3 §4 §7 §8 S1 S2 S5 S7 S8 S9 S11 AC6 AC8 · amended at the disposal of the
  round-1 spec audit `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4
  "Amendments (round-1 spec audit)": ids 1 (`TOOL-dCalibratedLens-19`), 36
  (`TOOL-dCalibratedLens-20`), 2 (`TOOL-dCalibratedLens-21`), 3 (`TOOL-dCalibratedLens-22`), 49
  (`TOOL-dCalibratedLens-27`), and 11, 30, 25, 26, 37, 38, 39, 13 and 12
  (`TOOL-dCalibratedLens-30`); §8 gains F5 (id 26); §3 gains the hands-offs to units 19, 20, 21, 22,
  27 and 30.
- rev-3 · 2026-11-02 · §3 §4 S2 S5 S7 S8 · amended at the disposal of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`, §4 "Amendments (round-2 spec audit)": r2 ids
  27 (`TOOL-dCalibratedLens-39`) and 31 (`TOOL-dCalibratedLens-40`), and r2 ids 7, 22, 20 and 38
  (`TOOL-dCalibratedLens-41`); §3 gains the hands-offs to units 39 and 40.
- rev-4 · 2026-11-03 · §3 §4 S2 S5 S8 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, §4 "Amendments (round-3 spec audit)": r3 id
  11 (`TOOL-dCalibratedLens-43`), the prefix listing; r3 ids 33 and 32 (`TOOL-dCalibratedLens-48`),
  the Metrics section's bounds and the per-entry refusal; §3 gains the hands-off to unit 43.
- rev-5 · 2026-11-03 · §5 §6 §7 §10 S2 S8 · re-grounded against the parents' specs, the walk no longer
  called TOOL-dTendedCadence-1 S2's and why a re-run's `seen` receipt stands, and the record's JSON
  capped at `INTAKE_CAP_BYTES` with AC10 over 64 KiB, by the brief
  prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-parents-reground.md (cross-check rows 41, 46)
- rev-6 · 2026-11-03 · §2 §4 §6 §8 S1 S4 S8 AC8 · re-grounded against dTotalRecall's and dDeclaredLoop's
  specs, the item rows given dl12's non-role keys, F2 and F5 re-marked to name the filed asks
  TOOL-dWellOiledMachine-128 and TOOL-dDeclaredLoop-110, id 37's `unarmed` naming its writer and dropped
  by the first record's commit, and `loop-review` bound through `RECORD_KIND_TOKENS`, by the brief
  prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-reground.md (cross-check rows 24, 26, 30, 31)
- rev-7 · 2026-11-04 · §4 S8 AC7 AC8 · the cross-check folds' spec audit disposed, the four item rows'
  `allowance` held to `WRITES` and each given a classed `witness`, `loop_lib.py --check` observed by AC7,
  and the first period's commit dropping `unarmed` from both the `loop-review` and `value-ledger` rows
  with AC8 committing a snapshot beside the record, by the brief
  prompts/2026-11-04-prompt-TOOL-dCalibratedLens-1-crosscheck-audit-disposal.md (review
  2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit, items M1 M5)

## 10. Reuse audit

The seams extended: unit 2's module and `derive_loop_window`; the cadence row, tick and period witness
of TOOL-dWellOiledMachine-59 S1 to S3 and -13 S5, S6 with asks TOOL-dTendedCadence-27, -29, -30 and §8
F2's; a walk over TOOL-dDeclaredLoop-12's `order_by_needs`, as Maintain's is, without TOOL-dTendedCadence-48 S28's re-run journal (S2);
`intake.py file --origin cadence` (TOOL-dWellOiledMachine-27 S1) for the asks and the records-only
landing, as TOOL-dTendedCadence-15 S2 uses it, where Maintain's record lands through TOOL-dTendedCadence-49 (S8); the record shape and contained atomic write of
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
