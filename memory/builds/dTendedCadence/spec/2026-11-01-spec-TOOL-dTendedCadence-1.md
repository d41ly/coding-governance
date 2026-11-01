# TOOL-dTendedCadence-1 — the Maintain run as its step checklist: `[[item]]` rows walked in `needs` order by `maintain.py` under the period lease, never a recipe-mode playbook

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 8 · advances TOOL-dTendedCadence-19

**Carries:** cl-dClosedLoop-0442@d7b64b62 whole
**Carries:** node:item.maintain.lease
**Carries:** node:item.maintain.read
**Carries:** node:item.maintain.levels

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-build-TOOL-dTendedCadence-1-deviation-11.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-deviation-11.md) | deviation | — |
| [2026-11-01-build-TOOL-dTendedCadence-1-reuse-scout-a.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-reuse-scout-a.md) | research | TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-6 TOOL-dTendedCadence-8 TOOL-dTendedCadence-10 |
| [2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md) | research | TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-1-reuse-scout.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-1-reuse-scout.md) | journal | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-2-reuse-scout.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-2-reuse-scout.md) | journal | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-3-reuse-scout.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-3-reuse-scout.md) | journal | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-4-reuse-scout.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-4-reuse-scout.md) | journal | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-5-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-5-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md) | research | TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md) | research | TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing runs maintenance on a cadence today (gap-maint-01): the drift report, the reap and the cleanup are each run by
hand, and the one design that ran them, a recipe-mode playbook, is superseded. This unit makes the Maintain run a step
checklist: its items declared as `[[item]]` rows in the item schema the flow's steps use, walked in their `needs`
order by one program, `tools/drift-audit/maintain.py`, which the cadence runs under its period lease. It builds the
three items it owns, `maintain.lease`, `maintain.read` and `maintain.levels`, and composes the items its siblings
build into one run.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `f4597719`: TOOL-dDeclaredLoop-12 S5 (`order_by_needs` in
`tools/lib/needs_graph.py` and its inline `needs_graph_py` block); TOOL-dWellOiledMachine-13 S6 (`run_cadence_period`)
with ask TOOL-dTendedCadence-27 of §8; TOOL-dTendedCadence-6 (the maintenance record's writer), TOOL-dTendedCadence-8 (the `[[reading]]`
registry and the I6 patch filer), TOOL-dTendedCadence-14 (the bands), TOOL-dTendedCadence-15 (`maintain.file`) and
TOOL-dTendedCadence-18 (the reading pass, its tree and liveness), TOOL-dTendedCadence-4 (`read_policy_value`);
TOOL-dWitnessedBar-9 S1 (the `level` key on a leg).

- **S1** — The rows. Six `[[item]]` rows in `tools/drift-audit/kit.toml` (settled 1), in TOOL-dDeclaredLoop-12's
  data model, the keys of its §4 "Data model" spelled as that unit spells them, `step = "cadence.maintain"` and
  `owner = "dTendedCadence"`, as §4 "The rows" tabulates: `item.maintain.lease`, `item.maintain.read`,
  `item.maintain.patch`, `item.maintain.file`, `item.maintain.levels` and `item.maintain.record`. The seventh,
  `item.maintain.direct`, is TOOL-dTendedCadence-3's, which adds its row. Observed by AC1.
- **S2** — The walk. `python maintain.py [--check] [--dry-run] [--key <key>]`. `read_maintain_items(kit_dir)` reads
  the rows with `tomllib`; the walk orders them with `order_by_needs` (the inline `needs_graph_py` block) and refuses,
  exit 2 with one line each, a need naming no row, a cycle, an outcome with no route and a route naming no row nor a
  `stand-in:<path>`. `--check` stops there and prints `maintain — <n> item(s) · ok`. Otherwise `run_maintain(root,
  key, dry_run)` runs each item in that order once every item it needs has run, handing it the outcomes routed to
  it, an empty hand-off answering `none`, and prints
  `maintain — <key> · <item tag> · <outcome>` per item and per reading, and exits 0 once `item.maintain.record` has
  run; an item body that raises or refuses exits 1, so `run_cadence_period` releases the lease as a hand-over and the
  next wake runs the period again (TOOL-dWellOiledMachine-13 S6 step 5). Observed by AC1 and AC2.
- **S3** — `maintain.lease`. Its actor is the executor: `run_cadence_period` takes the period lease, or the event's,
  `refs/gov/leases/run/maintain/<key>`, before it runs the program and releases it after
  (TOOL-dWellOiledMachine-13 S6), so a held or witnessed key never reaches the program. The program reads its key from `GOV_CADENCE_KEY`, which
  ask TOOL-dTendedCadence-27 asks `run_cadence_period` to set; a key read there reaches the item as `taken`. `--key <key>` is admitted only
  with `--dry-run`, which reads and routes and writes, files and fixes nothing; no key at all exits 2,
  `maintain — refused: no key; run under cadence.py run maintain`. The node pass `maintain.py --scope node` and
  `maintain.node-readings: lease-holder` are TOOL-dTendedCadence-16's (§3). Observed by AC3.
- **S4** — `maintain.read`, `measure_readings(root, key)`. It runs the reading pass, `python drift_report.py
  --readings` (TOOL-dTendedCadence-18 S8), as a bounded subprocess: the registered readings (TOOL-dTendedCadence-8's
  `[[reading]]` rows), a repo-scoped one taken in the tree `maintain.reading-tree` says, each record carrying the
  `band` TOOL-dTendedCadence-14 S3 derives under `maintain.tiers` (`in-pin`, `log`, `diagnose`, `act`) or `dead`, dead
  past `maintain.dead-after` readings with the source it is filed to (TOOL-dTendedCadence-18 S8), and its `over` and
  `keys` (TOOL-dTendedCadence-8 S5). The period run reads the `scope = "repo"` records; the `scope = "node"` ones are
  the node pass's (TOOL-dTendedCadence-16 S6). Under an event key `<event>.<sha12>`, the period segment `derive_event_key` returns (TOOL-dTendedCadence-8 S6), it runs `--readings --event
  <event>`, which reads only the rows whose `events` name that event (TOOL-dTendedCadence-8 S5,
  layer-expansions:230-231). Each record's band is its outcome. `in-pin` and `log` route to `item.maintain.record`,
  each `log` record counted for the record's `log-band:` field (TOOL-dTendedCadence-14 S4). For a `diagnose` record
  the walk calls `run_band_probe(record, offender_key, root)` (TOOL-dTendedCadence-14 S5) per offender and carries the
  probe record it returns. `diagnose`, `act` and `dead` route to `item.maintain.file` as breaches
  (TOOL-dTendedCadence-15 S1). Which fix an `act` record takes first is TOOL-dTendedCadence-3's re-route of the `act`
  outcome. Observed by AC2, AC4 and AC5.
- **S5** — `maintain.levels`, `run_held_levels(root, key, dry_run)`. It reads `tests.landing-levels` and
  `verdict.held` through `read_policy_value("tests.landing-levels", root)` and
  `read_policy_value("verdict.held", root)` (TOOL-dTendedCadence-4 S6); a `PolicyRefused` takes that key's catalogue
  default with one `NOTE:` line. The legs assigned to Maintain are each manifest leg whose `level` (TOOL-dWitnessedBar-9 S1) is outside `tests.landing-levels`, and,
  under `verdict.held: peer-or-cadence`, each leg the runner holds as `kit` (TOOL-dWitnessedBar-5 S1). With none it
  prints `levels — none assigned` and routes `green`. Otherwise it runs the bar in the reading tree with
  `GATE_SELFTESTS=1` and a `GATE_SELECTION` file holding no `level` row (TOOL-dWitnessedBar-5 S2), its witness the
  verdict record the runner writes; `green` routes to `item.maintain.record`, and `red` routes each red leg to
  `item.maintain.file` as a breach of the reading `maintain.levels` keyed by the leg's name, owned by Test.
  `--dry-run` prints `levels — <n> assigned · <leg>…` and runs nothing. Observed by AC6.
- **S6** — The record and what follows it. `item.maintain.record` runs `write_maintenance_record(root, key, base,
  read, readings, fields)` (TOOL-dTendedCadence-6 S6), the readings and routes the run reached as its input and the
  `log` count as its `log-band:` field, which writes the record or, under `maintain.record-when: on-finding` with
  nothing found, nothing. The walk then passes the written record's path to `run_breach_report`
  (TOOL-dTendedCadence-15 S7) when any breach routed `reported`, and files the record's landing: one cadence intake,
  `python <runtime>/intake.py file --origin cadence --filer item.maintain.record`, its stable text the record's key,
  its base and its readings as JSON, so the records-only patch build that takes it re-writes the record with
  `python maintenance.py write --key <key> --base <sha>` and lands it (§8 F4). The walk commits nothing. Observed by
  AC7.
- **S7** — Never a recipe-mode playbook: `maintain.py` reads no `PLAYBOOK` file, calls no `check-playbook.sh` and
  records no piece; §4 "Why not recipe mode" states the reason. Observed by AC8.
- **S8** — The arms of §7's `New arm:` line in `tools/drift-audit/selftest.py`. Observed by AC1 to AC7.
- **S9** — The docs: `help/maintain.md` gains a section "The Maintain run" naming the items, their order, the key,
  `--check` and `--dry-run`; `tools/drift-audit/README.md` names `maintain.py`. Observed by AC9.

## 3. Non-goals (OUT)

- The cadence row at `point.cadence-items`, its host and its event runs: TOOL-dTendedCadence-2, which names this
  program's argv.
- `item.maintain.direct`, the fix routes and `maintain.fixes`: TOOL-dTendedCadence-3.
- The bodies of `item.maintain.patch`, `item.maintain.file` and `item.maintain.record`: TOOL-dTendedCadence-8, -15
  and -6. This unit declares their rows and calls them.
- The node-scoped half of `maintain.lease`, the node pass `maintain.py --scope node` and `maintain.node-readings`:
  TOOL-dTendedCadence-16, which owns that key and the readings it governs.
- The band derivation, the diagnose probe, the reading pass and its tree: TOOL-dTendedCadence-14 and -18.
- The loop kit reading these rows through `check_program`: ask TOOL-dTendedCadence-25. The flow's executor walking a cadence program by
  (cadence, period): ask TOOL-dTendedCadence-28, §8 F2.
- dCalibratedLens's Loop Review program, a second cadence program of the same shape.

### Edges

- **consumes-from** `TOOL-dTendedCadence-4` — `read_policy_value`, drift-audit's one policy adapter, which S5 reads `tests.landing-levels` and `verdict.held` through
- **consumes-from** `TOOL-dTendedCadence-6` — `maintenance-record`, the writer `item.maintain.record` runs and whose written path S6 hands on; with no writer the run never reaches its exit
- **consumes-from** `TOOL-dTendedCadence-8` — `item.maintain.patch` and `[[reading]]`, the registry S4 reads every reading from and the filer the patch row runs, and `derive_event_key`, whose `<event>.<sha12>` S4 reads as an event key
- **consumes-from** `TOOL-dTendedCadence-14` — `edges`, the band S4 routes each record by, the `log` count for the record, and `run_band_probe`, the diagnose probe S4 calls
- **consumes-from** `TOOL-dTendedCadence-15` — `item.maintain.file`, the body `run_breach_route` S4 and S5 route breaches to, and `run_breach_report`, which S6 calls
- **consumes-from** `TOOL-dTendedCadence-18` — `maintain.reading-tree`, through the reading pass `drift_report.py --readings` S4 runs, and the liveness that makes a reading `dead`
- **hands-off** `TOOL-dTendedCadence-3` — `maintain.py`, whose `act` outcome that unit re-routes by fix and to which it adds the `item.maintain.direct` row
- **hands-off** `TOOL-dTendedCadence-2` — `maintain.py`, the argv the cadence row's `run` names, reading its key from `GOV_CADENCE_KEY`
- **hands-off** `TOOL-dTendedCadence-16` — `item.maintain.lease` and `maintain.py`'s walk, whose node-scoped half, the node pass and `lease-holder`, that unit adds
- **consumes-from** external — dDeclaredLoop's `order_by_needs`, dWellOiledMachine's `run_cadence_period` with ask TOOL-dTendedCadence-27, and dWitnessedBar's `level` key and selection record, each specced and unbuilt at base

## 4. Design

### Evidence

No program runs on a schedule here. The only scheduled actors are the resume tick, the desktop restart task and
CI's read-only cron (gap-maint-01). The item schema is TOOL-dDeclaredLoop-12's `[[item]]` row (its S1, §4 "Data
model"), read only from `tools/loop/loop.toml`, which holds the five core steps (TOOL-dDeclaredLoop-1 S2); no parent
gives an expansion's rows a home, so they live in the engine kit's descriptor (settled 1, scout A open point 1) and
ask TOOL-dTendedCadence-25 asks the loop kit to read them. The flow's executor is the supervisor (TOOL-dWellOiledMachine-6 S1), which asks
`position.py <slug>` (TOOL-dDeclaredLoop-7 S7) and so walks a build, keyed by slug; a cadence program is keyed by
(cadence, period) and no parent walks one (scout A row 1). `run_cadence_period` takes the lease and runs one argv
(TOOL-dWellOiledMachine-13 S6). So this unit's walk runs the items inside that argv, a departure recorded in
`2026-11-01-build-TOOL-dTendedCadence-1-deviation-11.md` until ask TOOL-dTendedCadence-28 lands. drift-audit is copy-installed
(`tools/drift-audit/kit.toml`, `include = "**"`), so the needs helper rides inline between its markers, discovered by
marker in `tools/lib/resolve-python.test.sh`'s parity arm.

### Why not recipe mode

Research-maintain's candidate A was a maintenance recipe in recipe mode (research-maintain:97-108). It lost on its
own test: the kit's crons live only as long as a session, a mutating action needs an owner-free mandate, and recipe
mode is still `building`. The owner then ruled that unit 1 is "the Maintain step's checklist on the flow's executor,
not a playbook in recipe mode, whose build is SPECCED and dormant" (walkthrough:686-687), and the coordination record
states recipe mode "is not a seam" for Maintain's run (coordination:48). A checklist of declared items is graded
item by item, its witnesses checked, and shares the flow's schema; a recipe is one mandate over free steps.

### The rows

| Item | Actor | Needs | Outcomes → route | Witness |
|---|---|---|---|---|
| `item.maintain.lease` | `executor` | none | `taken` → `item.maintain.read` | the lease record on `refs/gov/leases/run/maintain/<key>` |
| `item.maintain.read` | `command:maintain.read` | lease | `in-pin`, `log` → `item.maintain.record`; `diagnose`, `act`, `dead` → `item.maintain.file` | the journal lines I9 |
| `item.maintain.patch` | `command:maintain.patch` | read | `filed`, `seen`, `none` → `item.maintain.record`; `survivor` → `item.maintain.file` | the intake, keyed by (reading, offender key) |
| `item.maintain.levels` | `command:maintain.levels` | lease | `green` → `item.maintain.record`; `red` → `item.maintain.file` | the verdict record |
| `item.maintain.file` | `command:maintain.file` | read, patch, levels | `filed`, `seen`, `held`, `reported`, `none` → `item.maintain.record` | the ask, keyed by (reading, offender key) |
| `item.maintain.record` | `command:maintain.record` | read, patch, file, levels | `closed` → `stand-in:tools/runtime/cadence.py` | the maintenance record, or the lease witness alone, as `maintain.record-when` says |

The `closed` route hands back to the executor, whose release `--as landed` on exit 0 is the period's witness
(TOOL-dWellOiledMachine-13 S6 step 5). Each command row's `inputs`, `allowance` and `returns` name its layer input,
its write (`none` for `read` and `levels`) and its record kind, as TOOL-dDeclaredLoop-12 requires of a non-role actor.
The walk maps each row's tag to its body: `measure_readings` and `run_held_levels` here, `run_breach_route` in
`maintain_file.py`, `write_patch_intake` in `readings.py` (TOOL-dTendedCadence-8 S7) and `write_maintenance_record` in
`maintenance.py` (TOOL-dTendedCadence-6 S6), each imported from the same kit.
`order_by_needs` orders lease, read, levels, patch, file, record, ties broken by the helper's own rule.

### Inventory

Names this unit mints, each asked of `lexicon.py --suggest <name> --as py.function` at this base and answered OK:
`run_maintain`, `read_maintain_items`, `measure_readings`, `run_held_levels`. The intake filer tag
`item.maintain.record` for the record's landing. The module `maintain.py`, the step
value `cadence.maintain`, the environment key `GOV_CADENCE_KEY` (ask TOOL-dTendedCadence-27), and the CLI flags `--check`, `--dry-run`
and `--key`.

### Files touched (estimate)

- `tools/drift-audit/maintain.py` (new)
- `tools/drift-audit/kit.toml`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `help/maintain.md`

### Alternatives rejected

- **A recipe-mode playbook.** Rejected by the clause and §4 "Why not recipe mode".
- **The rows in `tools/loop/loop.toml` under a sixth step.** Rejected: an expansion meets the core only at a core
  point (EX-1), and a sixth `[[step]]` row puts Maintain in the build's own loop, its `order` and `state` read by
  every
  build.
- **A hand-typed item order in `maintain.py`.** Rejected by the charter's [derive] rule: the order is the rows'
  `needs`, read through the one needs helper.
- **Taking the lease inside the program.** Rejected: `run_cadence_period` already reads the witness, takes the lease
  and releases it (TOOL-dWellOiledMachine-13 S6); a second take would contend with the first.

## 5. Production-readiness checklist

- security — the walk itself commits nothing: its one write is the record's landing intake, every other write is an
  item body's, and `--dry-run` and a missing key write nothing; `levels` runs the bar the repository already runs,
  in the reading tree.
- perf / scale — one pass over the registered readings per key; `levels` runs only when a leg is assigned to it, the
  bar's cost then (gov assigns none today: no leg carries `level` and `verdict.held` reads `on-demand`).
- error / empty / loading states — no reading registered: `read` routes nothing and the record still closes; a
  refused key read: the default with its `NOTE:` line; a malformed row: `--check`'s exit 2.
- observability — one `maintain —` line per item and per reading; the item witnesses.
- risks — a failing item body hands the lease over each wake until the period's budget ends it
  (TOOL-dWellOiledMachine-59 S5).
- testing — §7's `New arm:` line.
- migration — N/A: nothing exists to move.
- user docs — `help/maintain.md` (S9).

## 6. Acceptance criteria

The walk fixture is a scratch git repository under `%TEMP%` with a short name holding copies of
`tools/drift-audit/`, `tools/policy/`, `tools/memory-tree/` and `tools/lib/`, two registered readings, `rA` in its pin
and `rB` over it with `events = ["default-branch-red"]`, and stub bodies for the patch, file and record rows that
print their tag. Each command runs with the fixture as its working directory.

- **AC1** — When `python maintain.py --check` runs, it prints `maintain — 6 item(s) · ok` and exits 0; with a planted
  `needs` on `item.maintain.levels` naming `item.maintain.record` it exits 2 naming the cycle; with a need naming
  `item.maintain.gone` it exits 2 naming it.
  Red when: a cycle or a dangling need passes.
- **AC2** — When `GOV_CADENCE_KEY=2026-11-01 python maintain.py --dry-run` runs, it prints the item lines in the
  order lease, read, levels, patch, file, record, `rA` routed `in-pin` to the record and `rB` routed `act` to
  `item.maintain.file`, and exits 0.
  Red when: an item runs before its needs, or `rB` reaches the record without reaching the file row.
- **AC3** — When `python maintain.py` runs with no `GOV_CADENCE_KEY` it exits 2 with `refused: no key`; with
  `--key 2026-11-01` and no `--dry-run` it exits 2; with `--dry-run --key 2026-11-01` it walks as AC2 and the stubs
  are called in dry mode.
  Red when: a run with no key writes, or `--key` writes outside `--dry-run`.
- **AC4** — When `GOV_CADENCE_KEY=default-branch-red.0123456789ab python maintain.py --dry-run` runs, it reads `rB`
  and not `rA`; with the period key it reads both.
  Red when: an event run reads a reading its event does not name.
- **AC5** — When a planted reading `rC` sits in its log band and a planted reading `rD` is dead past
  `maintain.dead-after`, `GOV_CADENCE_KEY=2026-11-01 python maintain.py --dry-run` routes `rC` `log` to the record
  with nothing handed to the file row and `rD` `dead` to the file row.
  Red when: a log-band reading is filed, or a dead one is not.
  fixture: needs TOOL-dTendedCadence-14 and -18 landed.
- **AC6** — When the fixture's `tools/gate-legs.json` carries one leg with `"level": "e2e"`, `python maintain.py
  --dry-run --key 2026-11-01` prints `levels — 1 assigned` naming it; with no `level` it prints `levels — none
  assigned` and routes `green`; with `[tests]` `landing-levels = ["unit", "integration", "e2e"]` committed in
  `.governance/policy.toml` it prints `none assigned`.
  Red when: a landing level is assigned to Maintain, or an assigned leg is missed.
- **AC7** — When the stub file body returns `reported` for `rB`, `GOV_CADENCE_KEY=2026-11-01 python maintain.py`
  calls `run_breach_report` once after the record stub with the record's path, and not at all when it returns
  `filed`; either way it files one intake with filer `item.maintain.record` whose text names the key, and the
  fixture's `git rev-list --count HEAD` is unchanged by the run.
  Red when: the report is sent before the record exists, the record's landing is not filed, or the walk commits.
- **AC8** — When `grep -c "check-playbook\|PLAYBOOK" maintain.py` runs in `tools/drift-audit/`, it prints 0.
  Red when: the program reaches recipe mode.
- **AC9** — When `grep -n "The Maintain run\|GOV_CADENCE_KEY" maintain.md` runs in `help/`, each matches.
  Red when: the page omits one.

## 7. Gates

`drift-audit selftest` · `drift-audit wiring` · `policy fixtures` · `memory hygiene`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the walk fixture's rows and readings, a planted cycle, a dangling need, an event key, a log-band and a dead reading and a level-tagged leg, staged against a `maintain.py` absent at this base · none

## 8. Open questions

- **F1 — Where do Maintain's item rows live?** (a) `[[item]]` rows in `tools/drift-audit/kit.toml`, the engine kit
  observability names for its cadence programs (layer-expansions:211), in TOOL-dDeclaredLoop-12's schema; (b) a sixth
  step in `tools/loop/loop.toml`; (c) a new observability kit. (b) puts an expansion in the core's loop, against EX-1;
  (c) is a new install location (veto 2). Settled 1 of the spec brief, rung 3. Ask TOOL-dTendedCadence-25 applies: TOOL-dDeclaredLoop-12's
  `read_items` reads only `tools/loop/loop.toml`, and its `check_program` grades each step's `exit` against a
  `[[step]]` row, which a cadence program has none of, so the loop kit cannot read these rows as specced. RESOLVED (agent, 2026-11-01, delegated): (a), with ask TOOL-dTendedCadence-25. widens: none · relaxes: none
- **F2 — What walks the items?** (a) `maintain.py`, ordering its rows by `order_by_needs` inside the argv
  `run_cadence_period` runs, until the flow's executor walks a cadence program; (b) the supervisor, which asks
  `position.py <slug>` and so walks only a build (TOOL-dWellOiledMachine-6 S1, TOOL-dDeclaredLoop-7 S1). (b) has no
  key for a period; (a) runs the checklist on the executor's lease and launch and departs from "on the flow's
  executor" in what walks the items, a departure recorded in
  `2026-11-01-build-TOOL-dTendedCadence-1-deviation-11.md`. Ask TOOL-dTendedCadence-28 for dDeclaredLoop: `position.py` answers a cadence
  program's next item keyed by (cadence, period) from its `[[item]]` rows and their witnesses · accept a fixture
  cadence program of two items, the second needing the first, answered first-then-second across two wakes of one
  period, and the supervisor running the answer, so `maintain.py`'s walk retires into it. Rung 3. RESOLVED (agent, 2026-11-01, delegated): (a), with ask TOOL-dTendedCadence-28. widens: none · relaxes: none
- **F3 — How does the program learn its key?** (a) `GOV_CADENCE_KEY` in its environment, set by `run_cadence_period`;
  (b) a `{period}` token in the cadence row's `run` argv; (c) reading back the lease this node holds. (b) needs a
  substitution rule in the row check (TOOL-dWellOiledMachine-59 S2) for one consumer; (c) parses a lease record
  format TOOL-dPlacedRequest-1 owns. Ask TOOL-dTendedCadence-27 for dWellOiledMachine: `run_cadence_period` runs its argv with
  `GOV_CADENCE=<cadence>` and `GOV_CADENCE_KEY=<period key>` in its environment · accept a stub argv run by
  `cadence.py run nightly-audit --period 2026-W44 -- <stub>` printing `nightly-audit 2026-W44` from its environment.
  Rung 3. RESOLVED (agent, 2026-11-01, delegated): (a), with ask TOOL-dTendedCadence-27. widens: none · relaxes: none
- **F4 — How is the record committed and landed?** TOOL-dTendedCadence-6 §3 hands it to this unit. (a) The walk
  files the record's landing as a records-only patch intake, the patch build re-writing and landing it; (b) the walk
  commits the record in a scratch worktree and lands it through the lander from the cadence; (c) the record left
  uncommitted in the node's worktree. (c) is never committed, so the red leg of TOOL-dTendedCadence-15 reads a dead
  probe for ever (veto 1); (b) lands to the default branch with no owner turn from a tick, a write surface the risk
  tier did not price (veto 3), while (a) survives at the cost of one patch build per written record, which
  `maintain.record-when: on-finding` bounds. Rung 3. RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none
- **F5 — Which legs are "the held legs assigned to Maintain"?** (a) The legs whose `level` the landing does not run,
  and under `verdict.held: peer-or-cadence` the kit-held legs; (b) every held leg, always. TOOL-dWitnessedBar-5 S6
  makes `peer-or-cadence` the value that hands held legs to a cadence, and S5 holds a leg by `level` outside
  `tests.landing-levels`; (b) runs the kit self-tests under `on-demand`, the owner's value that holds them. v2
  answers it through those parents' keys, rung 1. RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.

## 10. Reuse audit

The seams extended: TOOL-dDeclaredLoop-12's `[[item]]` schema and its needs helper `order_by_needs`, called through
its inline block and never copied; `run_cadence_period`'s lease and launch (TOOL-dWellOiledMachine-13 S6); the
siblings' bodies, called by name; and dWitnessedBar's `level` key and selection record for `levels`. The probe
`python tools/codebase-map/reuse_lookup.py "walk a cadence program's declared items in needs order under a period
lease"` ranked name stems only (`walk`, `need`, `declares`, `resolveLease`, `build_walk`, `declared_list`), and
`declared_list` is recipe mode's own reader in `tools/unattended/check-playbook.sh`, the seam the clause rules out;
so no existing seam fits a period-keyed walk, as scout A found (`derive_position` is keyed by build), and it is new
over the seams above. Where scout A's record disagrees with source at this base: none of its paths for this unit
exist yet (`tools/loop/`, `tools/runtime/`), as it says; its research-maintain:97-108 and layer-expansions:218-235
hold.

Recall terms used: `python tools/memory-recall/query.py "how is the Maintain run walked as its item checklist on the
executor rather than a recipe playbook" --terms "maintain.lease maintain.read maintain.levels item needs
order_by_needs
run_cadence_period recipe playbook executor cadence"`
