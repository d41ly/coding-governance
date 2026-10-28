# TOOL-dIndexedDesign-15 — the planner's `design.streams` item: the planning workflow, its run decision under `design.streams-when`, and the stream plan checked against order, write sets and the overlap record

**Status:** DEFERRED · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 15 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0397@155d665e whole
**Carries:** node:item.design.streams
**Carries:** node:policy-key.design.streams-when

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-d.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-d.md) | research | TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

Design's roster orders units, and nothing groups them into streams several node units can take at
once (gap-design-12). The build-order region judges one step's units parallel or not
(`derive_parallel_step`, `tools/memory-tree/gen_build_index.py:1724`), and TOOL-dTotalRecall-25
registers the stream-plan kind with no writer. This unit builds the planner's `design.streams` item,
which runs after `design.overlaps` as `design.streams-when` says (`opt-in` by default, `always`, `off`):
a planning workflow whose agent, at the planner's effort, groups the roster's units into streams by
their declared order, write sets and the overlap record, writes the plan as the stream-plan kind, and
needs no head (v2:1946-1948). A check reds a plan that pairs two units whose write sets overlap, and
each value of the key is seen on its planted case (the owner's CL-3 and FK-3-3).

## 2. Scope (IN)

- **S1** — The one write-meet helper. `derive_write_meet(a, b)` in `tools/memory-tree/design_lib.py`,
  beside `check_writes_intersect` (:601): each of the write sets `a` and `b` filtered to words of two
  or more non-empty segments, the filter `derive_parallel_step` holds inline today
  (`gen_build_index.py:1732-1734`), and the first pair `(p, q)` for which `check_writes_intersect([p],
  [q])` holds, else `None`. `derive_parallel_step` calls it, its verdicts unchanged, so the build-order
  region and the planner hold one overlap rule. Observed by AC8.
- **S2** — The planner module `tools/memory-tree/plan_streams.py`. Its units are the build's specs
  under `memory/builds/<slug>/spec/` read by `gen_build_index.parse_spec` (`:488`), those whose status
  is not in `TERMINAL` (`tools/memory-tree/tree_lib.py:31`), each with its `id`, declared `order`,
  `writes` and `consumes`. Its overlap rows are the overlap record's (`record.overlap`, shared
  interface I7), taken from the join that writes that record, TOOL-dIndexedDesign-2 S1's
  `derive_design_overlaps(root, files, subjects)` with this build's spec paths as `subjects`, so they
  are the record's rows as they stand and never a second parse of its file. By that join every row
  pairs a unit of this build with a unit of another build. Verbs:
  - `python plan_streams.py when <slug>` prints `run — <why>` and exits 0, or `skip — <why>` and
    exits 1, from `read_design_policy("design.streams-when", root)` (TOOL-dIndexedDesign-16, I3) and
    the build's opt-in signal (S4): `always` runs, `off` skips, `opt-in` runs only where the signal is
    present. A policy refusal or an unknown slug exits 2 naming it.
  - `python plan_streams.py context <slug>` prints the newest overlap record's path, or `overlap
    record: none yet`, then one line per unit, `unit <id> · order <n|none> · writes <word> …`, one
    line per pair of this build's units whose write sets meet, `meets <id> · <id> · <path>`, and one
    line per overlap row, `foreign <id> · <other build's id> · <path> · acknowledged|unacknowledged`,
    the planning workflow's input.
  - `python plan_streams.py write <slug> --from <file>` reads a `[[stream]]` TOML file in
    TOOL-dTotalRecall-25 S2's schema, runs `check_stream_plan` (TOOL-dTotalRecall-25 S3) and S3's
    arms, and on no finding writes the record (S5) and prints its path; any finding exits 1 naming it,
    and nothing is written.
  - `python plan_streams.py check <slug>` re-derives the build's newest stream-plan record against the
    specs and the overlap rows as they stand, the item's witness: exit 0, or 1 naming each finding.
  Observed by AC1 to AC5 and AC7.
- **S3** — The plan's arms, `check_stream_pairing(plan, units, pairs)` in `plan_streams.py`, each a
  finding naming the units, their streams and the cause:
  - (a) coverage: every planned unit is a unit of the build exactly once, and every unit is planned;
  - (b) order: within one stream, a unit declared earlier is planned earlier, so the plan keeps the
    declared order and may split one declared step into several;
  - (c) pairing: two units that can run at once, the same stream at the same planned `order` or any
    two streams, whose write sets meet by `derive_write_meet` (§8 F1);
  - the overlap rows, printed after the findings as `foreign overlap — <unit> (<stream>) · <other
    unit> · <path> · acknowledged|unacknowledged`, never a finding: this build's plan cannot sequence
    another build's unit, and `design.overlap` already disposed each row at `design.overlaps`;
  - (d) unknown: a unit with no `### Files touched` sub-head that can run at once with another unit.
  Observed by AC1 to AC4.
- **S4** — The opt-in signal, the build README front-matter key `stream-plan: <date>`, an ISO date, read by
  `when` through `gen_build_index.parse_front_matter` (`:405`) and added to `FRONT_MATTER_KEYS`
  (TOOL-dTotalRecall-4 S1) as an authored, optional key (§8 F2). Under `opt-in` its presence is "the
  brief or the owner asks"; under `always` and `off` it is not read. Build-run precondition:
  TOOL-dTotalRecall-4 landed. Observed by AC5.
- **S5** — The record. `write` names it `memory/builds/<slug>/build/<date>-build-<unit id>-stream-plan-<n>.md`,
  `<unit id>` the build's unit with the lowest declared order, ids ordered as `gen_build_index` orders
  them, and `<n>` one past the highest `<n>` already tracked for that build; the record opens with
  `**Serves:** stream-plan <every planned id>`, then an H1, then one `toml` fence of `[[stream]]`
  tables (TOOL-dTotalRecall-25 §4 "Data model"). The `stream-plan` row's `writer` cell in
  `tools/memory-tree/record-kinds.toml` moves from `hand` to `python plan_streams.py write <slug>
  --from <file>` through TOOL-dTotalRecall-18's landed verb; the row's `unarmed` key
  (TOOL-dTotalRecall-42 S3) stays until a build writes the first plan. Build-run precondition:
  TOOL-dTotalRecall-25 and -42 landed. Observed by AC7.
- **S6** — The planning workflow, `tools/workflows/plan-streams.template.js`, rendered to
  `tools/workflows/plan-streams.js` by `check-protocol-parity.test.sh --render` with the token
  `MEMORY_TREE_DIR`, declared by a `[[files]]` row of `tools/workflows/kit.toml` and a row of the render
  table in `tools/workflows/README.md`. Its args are `repo`, `slug`, `when`, and optional `roles` and
  `efforts` keyed `planner`. Before any spawn it refuses a missing `repo` or `slug`, and returns
  `{ skipped: <when> }` with no spawn unless `when` begins `run — `, the line `plan_streams.py when`
  printed. Its one stage, `planner`, spawns one agent labelled `<slug> · streams · planner`, as
  `roles.planner` (default `gov-planner`, TOOL-dBoundRoles-1's slot) and at `efforts.planner` when
  given, else at that agent type's own level, which `tools/roles/house/policy.toml` resolves to its
  `[effort] default`, `medium`, until the owner names the role (`roles_lib.resolve_effort`, :590). The
  agent runs `context`, groups the units, writes its plan to a scratch file, runs `write`, and on a
  finding revises and runs `write` again, at most three times; it returns `{ record: <path> }` or
  `{ findings: [<line>] }`. Observed by AC6.
- **S7** — The item. `item.design.streams` is the row TOOL-dDeclaredLoop-12 S2 transcribes into
  `tools/loop/loop.toml` from flow-steps.md:242: needs `item.design.overlaps`, actor the planner
  through the planning workflow, witness the stream plan re-derived, then `item.design.unit-spec`.
  This unit is that row's body: `when` is the predicate its route from `design.overlaps` reads
  ("where `policy.design.streams-when` holds for the build"), the workflow is its actor, `check` its
  witness, and its `returns` names `record-kind.stream-plan`; where the landed row names another
  actor or return, the pass amends that one row in place and records it as a rev. Build-run
  precondition: TOOL-dDeclaredLoop-12 landed. Observed by AC10.
- **S8** — The key's catalogue row. `design.streams-when` in `tools/policy/catalogue.toml` (:931-935)
  gains `summary = "Whether Design's planner runs the planning workflow to group a build's units into
  streams: only where the build asks, on every build, or never."` and `usage = 'design.streams-when =
  "always"'`, its allowed values and default unchanged, and `python tools/policy/policy.py lists
  --write` drains it from `tools/policy/unsummarised-keys.txt`. S2's `when` is its literal reader, the
  call the reader-coverage arm counts (`tools/policy/check_policy.py:423-426`). Observed by AC9.
- **S9** — The docs. `tools/memory-tree/README.md` gains a section naming `plan_streams.py`, its four
  verbs, the opt-in key and the record; `KIT_MEMORY_TREE_VERSION` in
  `tools/memory-tree/check-memory-hygiene.sh` moves. NOT OBSERVED by a criterion: prose and a version,
  graded by the `memory hygiene` and `kit/dogfood doc parity` legs at the close.

## 3. Non-goals (OUT)

- The overlap record, its kind and `design.overlaps`: TOOL-dIndexedDesign-2. This unit reads them.
- The pick that takes a stream, and a head: dWellOiledMachine's, and the head's where one exists.
  Each reads the record; a cross-stream `consumes-from` edge is the pick's to wait on, since check 12
  already holds every edge to an earlier `order`.
- Running the planning workflow from a driver verb: the item's route reads `when`, and until the loop
  runs items the main loop that reaches `design.overlaps` runs `when` and launches the workflow on
  `run`.
- The `plan` workflow entry's harness, driver and stages in `tools/roles/workflows.toml`: an ask in
  dBoundRoles' `BACKLOG.md` (§8 F3), never an edit here.
- A guard on who writes `stream-plan:`. Opting in costs one agent and writes one record; a guard like
  check 89's for `spec-audit:` is not this clause's.
- Choosing a minimal or balanced stream count: the agent groups, the check refuses only a plan that
  pairs what cannot run at once.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-16` — `read_design_policy`, through which `when` reads `design.streams-when` by its literal key
- **consumes-from** `TOOL-dIndexedDesign-2` — `record.overlap`, the overlap record whose rows, taken from `derive_design_overlaps`, `context` hands the planner and `check` prints beside its findings
- **consumes-from** external — TOOL-dTotalRecall-25's `stream-plan` row and `check_stream_plan`, TOOL-dTotalRecall-4's `FRONT_MATTER_KEYS`, TOOL-dTotalRecall-18's column verb and -42's `unarmed` key; TOOL-dBoundRoles-1's `gov-planner` slot; TOOL-dDeclaredLoop-12's `item.design.streams` row; each DEFERRED at base and an ancestor's
- **hands-off** external — dWellOiledMachine's pick and a head read the stream plan; dDeclaredLoop's route evaluator reads `plan_streams.py when` for the route out of `design.overlaps`
- **hands-off** `TOOL-dIndexedDesign-37` — S1's `derive_write_meet` and arm (c), whose filter that unit replaces with `check_meet_path` so root files meet (report id 39, HIGH)
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 4, 34 and 51, each a scope item of that batch unit

## 4. Design

### Evidence

- `derive_parallel_step` (`gen_build_index.py:1724-1745`) is the one place that judges two units
  parallel: a shared `consumes` or a write meet over words of two or more segments, through
  `design_lib.check_writes_intersect`. It judges one step only, never two units at different orders on
  two nodes, which a stream plan makes concurrent.
- `check_stream_plan` (TOOL-dTotalRecall-25 S3) grades a plan's shape alone and has no write-set arm
  (scout D, disagreement 9), so the clause's red is this unit's to build, over the existing rule.
- `streams:` is already a front-matter key, the build's disciplines (this build's README, line 5;
  TOOL-dTotalRecall-4 derives it), so the scout's proposed `streams: plan` signal would overload it.
- The key's row exists, `design.streams-when`, allowed `opt-in`, `always`, `off`, default `opt-in`,
  owner dIndexedDesign (`tools/policy/catalogue.toml:931-935`), and is named on
  `tools/policy/unsummarised-keys.txt` (:58).

### Concurrency, which arm (c) grades

| Two units | Can run at once | Why |
|---|---|---|
| one stream, different planned `order` | no | a stream's units run in order on one node unit |
| one stream, same planned `order` | yes | the stream's parallel group (TOOL-dTotalRecall-25 §4) |
| two streams, any orders | yes | streams are taken at once by different node units, and no head orders them (v2:1946-1948) |

### The run decision

| `design.streams-when` | `stream-plan:` absent | `stream-plan:` present |
|---|---|---|
| `off` | skip | skip |
| `opt-in` (default) | skip | run |
| `always` | run | run |

### A plan, and a refused one

```toml
[[stream]]
name = "unattended"
units = [{ id = "TOOL-dIndexedDesign-10", order = 1 }, { id = "TOOL-dIndexedDesign-11", order = 2 }]

[[stream]]
name = "planner"
units = [{ id = "TOOL-dIndexedDesign-15", order = 1 }]
```

Units 10 and 11 both estimate `tools/unattended/check-playbook.sh`, so the plan keeps them in one
stream in their declared order. Moving unit 11 into the second stream reds arm (c):
`pairing — TOOL-dIndexedDesign-10 (unattended) · TOOL-dIndexedDesign-11 (planner) · tools/unattended/check-playbook.sh`.
Units 10 and 11 each estimate `tools/memory-tree/record-kinds.toml`, as unit 15 does, so this plan
reds too, the finding the agent revises against.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_write_meet` | function, `design_lib.py` | `py.function`, asked at the pass |
| `plan_streams.py` | module | none |
| `check_stream_pairing` | function, `plan_streams.py` | `py.function`, asked at the pass |
| `when`, `context`, `write`, `check`, `--fixture` | verbs of `plan_streams.py` | none |
| `plan-streams.template.js`, `plan-streams.js` | workflow harness and its render | none |
| `stream-plan` | README front-matter key | none declared |

### Fixture

`python plan_streams.py --fixture --plant <case>` builds a scratch repository under the system temp
directory: a build of four specs with orders and Files touched estimates, a second live build whose
spec meets one of them on a path, and a
committed `.governance/policy.toml` where the case sets the key. Cases: `pair-same-order`,
`pair-cross-stream`, `foreign-row`, `order-reversed`, `unit-missing`, `unit-twice`,
`unit-foreign`, `unknown-writes`, `when-off`, `when-always`, `when-opt-in-asked`, `when-opt-in-silent`,
`write`, `recheck`, `parallel-step`, `harness-skip` and `harness-run`; the two harness cases run
`node` over the rendered `plan-streams.js` with an `agent` stub that records each spawn's label, type,
effort and prompt. No plant is green. `gen_build_index.py --selftest` runs every case.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S1
- `tools/memory-tree/gen_build_index.py`: S1's call, S4's `FRONT_MATTER_KEYS` entry, the selftest arm
- `tools/memory-tree/plan_streams.py`: new, S2, S3, S5 and the fixture
- `tools/memory-tree/record-kinds.toml`: S5's `writer` cell
- `tools/workflows/plan-streams.template.js`: new, S6
- `tools/workflows/plan-streams.js`: the render of S6, never the edit
- `tools/workflows/check-protocol-parity.test.sh`, `tools/workflows/kit.toml`, `tools/workflows/README.md`: S6's render row
- `tools/loop/loop.toml`: S7's row, only where the landed row differs
- `tools/policy/catalogue.toml`: S8
- `tools/policy/unsummarised-keys.txt`: the render of `policy.py lists --write`, never the edit
- `tools/memory-tree/README.md`, `tools/memory-tree/check-memory-hygiene.sh`: S9

### Alternatives rejected

- **Derive streams with no agent**, the connected components of the write-meet graph each a stream.
  The clause names "a planning workflow, its agents at the planner's effort"; a deterministic grouping
  would carry the clause in part, and the check of S3 already makes any agent's plan safe.
- **Extend `check_stream_plan` with the pairing arm.** It is TOOL-dTotalRecall-25's shape check over
  one record and holds no spec reader; the pairing needs the build's specs and their write sets,
  which a kind's validator should not open.
- **Read the opt-in from the planning workflow's arguments alone.** An ask passed at launch leaves no
  trace a later `check`, the pick or an audit can re-read.

## 5. Production-readiness checklist

- security — `write` composes the record from a parsed TOML file and writes one path under the
  build's `build/` folder; `--from` reads one file; the harness spawns one agent with no write grant
  beyond the planner role's.
- perf / scale — one `parse_spec` per unit and one write-meet test per concurrent pair; this build's
  16 units make 120 pairs (DERIVED: n(n-1)/2).
- error / empty / loading states — a build with no unit refuses `write`; a build no overlap record
  names yet makes `context` print `overlap record: none yet` beside the rows the join derives; a policy
  refusal is exit 2, never a `skip`.
- observability — `when` says why it runs or skips; every finding names both units, both streams and
  the meeting path or record row.
- risks — a stale plan once a spec's write set changes; `check` re-derives it, the item's witness.
- testing — the fixture cases, run by the pass and by `gen_build_index.py --selftest` at the close.
- migration — none: no stream plan exists, and the key's default is unchanged.
- user docs — the catalogue row's `summary` and `usage`, which `help/policy.md` points readers at, and
  the memory-tree README (S9).

## 6. Acceptance criteria

- **AC1** — When `python plan_streams.py --fixture --plant pair-same-order` runs, `write` exits 1
  printing `pairing —` with both units, their one stream and the meeting path, and writes no record;
  with no plant `write` exits 0.
  Red when: two units whose write sets overlap pass as one stream's parallel group.
- **AC2** — When `python plan_streams.py --fixture --plant pair-cross-stream` runs, two units at
  different orders in two streams whose estimates name one file make `write` exit 1 printing
  `pairing —` and both stream names.
  Red when: a stream pairing two units whose write sets overlap passes because their orders differ.
- **AC3** — When `--plant foreign-row` runs, where a second live build's spec meets one fixture unit
  on a path, `context` prints a `foreign` line naming both units and the path, and `write` and
  `check` print `foreign overlap —` with that unit's stream and exit 0.
  Red when: the overlap rows are not read, or a row naming another build's unit reds a plan that
  cannot sequence it.
  fixture: `derive_design_overlaps` is TOOL-dIndexedDesign-2's, built earlier in this build run.
- **AC4** — When `--plant order-reversed`, `unit-missing`, `unit-twice`, `unit-foreign` and
  `unknown-writes` run in turn, `write` exits 1 for each, naming `order`, `coverage`, `coverage`,
  `coverage` and `unknown`.
  Red when: a plan reverses a declared order, misses or repeats a unit, or pairs a unit whose write
  set nobody declared.
- **AC5** — When `--plant when-off` (README carrying `stream-plan:`), `when-always` (README silent),
  `when-opt-in-asked` and `when-opt-in-silent` run, `plan_streams.py when` prints `skip —`, `run —`,
  `run —` and `skip —`, exiting 1, 0, 0 and 1; with no `.governance/policy.toml` it reads `opt-in`.
  Red when: `off` runs a planning workflow, `always` skips a build, or `opt-in` runs where nothing asks.
- **AC6** — When `--plant harness-skip` runs `plan-streams.js` under the `agent` stub with `when` set to
  a `skip —` line, it records no spawn and returns `skipped`; `--plant harness-run` with a `run —` line
  and `efforts.planner` `high` records one spawn labelled `streams · planner`, typed `gov-planner`, at
  `high`, its prompt naming `plan_streams.py context`.
  Red when: a skip still spawns the planner, or the stage spawns untyped or at another effort.
- **AC7** — When `--plant write` runs `write` twice over a valid plan, the fixture build gains
  `-stream-plan-1.md` and `-stream-plan-2.md`, each opening `**Serves:** stream-plan` with every
  planned id and holding one fence that `check_stream_plan` passes, and `check` exits 0; `--plant
  recheck` then plants a spec estimate meeting a unit of another stream and `check` exits 1 naming it.
  Red when: the record misses its Serves kind or a unit, a second plan overwrites the first, or a
  stale plan re-derives green.
- **AC8** — When `--plant parallel-step` calls `gen_build_index.derive_parallel_step` over a step whose
  units' estimates meet, one that is disjoint and one with an undeclared write set, it returns `no`,
  `yes` and `unknown`, and `design_lib.derive_write_meet` returns the meeting pair for the first.
  Red when: the extracted helper changes a build-order verdict.
- **AC9** — When `grep -c '^design.streams-when$' tools/policy/unsummarised-keys.txt` runs at the pass
  tip it prints 0, `python tools/policy/policy.py get design.streams-when` prints `opt-in`, and
  `grep -c 'read_design_policy("design.streams-when"' plan_streams.py` prints at least 1.
  Red when: the row keeps no summary, its default moves, or no literal call reads the key.
- **AC10** — When `grep -A12 'tag = "item.design.streams"' loop.toml` runs in the loop kit's
  directory, it prints `item.design.overlaps` among the needs and `record-kind.stream-plan` as the return.
  Red when: the item's row returns another record than the plan this unit writes.
  fixture: `loop.toml` is TOOL-dDeclaredLoop-12's, absent at base until it lands.

## 7. Gates

`build-index selftest` · `memory hygiene` · `policy check` · `policy fixtures` · `review-join self-test` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `kit/dogfood doc parity` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the `--selftest` arm running `plan_streams.py --fixture` per case, its failing case staged by arm (c) testing only same-order units · none

## 8. Open questions

- **F1 — What does "a stream pairing two units" mean?** Options: (a) two units of one stream at the
  same `order`, its parallel group; (b) two units in different streams; (c) both, every two units the
  plan lets run at once. RESOLVED (agent, 2026-10-28, delegated): (c), rung 1: the clause groups units
  "into streams that several node units can take at once" and the plan needs no head, so units of two
  streams run at once whatever their orders (v2:1946-1948), and TOOL-dTotalRecall-25 §4 makes one
  stream's same-order units its parallel group; (a) passes a cross-stream overlap and (b) a same-order
  one, each a plan two node units cannot both follow. widens: none · relaxes: none
- **F2 — What is the opt-in signal, "where the brief or the owner asks"?** Options: (a) a build README
  front-matter key `stream-plan: <date>`, the shape `spec-audit:` gives an owner's opt-in; (b)
  `streams: plan`, scout D's proposal; (c) an argument of the planning workflow alone; (d) a per-build
  policy value. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, the most feature-rich survivor:
  it is read from the tree, so `when`, the pick and an audit agree on it; (b) overloads `streams:`,
  the build's disciplines, which TOOL-dTotalRecall-4 derives; (c) leaves nothing to re-read; (d) has
  no grammar, since `.governance/policy.toml` is repo-wide. The key is the surface the clause itself
  names, so veto 2 does not discard it. widens: none · relaxes: none
- **F3 — The `plan` workflow entry gives the planner `harness none` and driver `agent`
  (TOOL-dBoundRoles-1 S4, its §8 F1), where the clause needs a planning workflow.** Options: (a) an
  ask in dBoundRoles' `BACKLOG.md`; (b) edit that spec; (c) leave the entry stale. RESOLVED (agent,
  2026-10-28, delegated): (a), rung 3: a parent's spec is never edited here, and the harness spawns as
  `gov-planner` whatever the entry says, so the ask is not a precondition of this unit. Target build:
  dBoundRoles. Text: "THE `plan` WORKFLOW HAS A HARNESS. dIndexedDesign's `design.streams` runs the
  planning workflow `tools/workflows/plan-streams.js`, and TOOL-dBoundRoles-1 S4 declares the `plan`
  entry `harness none`, driver `agent`, so `handoff.py stage-efforts plan` and `harness-args` name no
  stage for it (TOOL-dIndexedDesign-15 §8 F3)." Accept line: "accept the `plan` entry of
  `tools/roles/workflows.toml` declares driver `workflow`, harness `{prefix}/workflows/plan-streams.js`
  and stages `{ planner = "gov-planner" }`, seen as `python handoff.py stage-efforts plan` printing a
  `planner` key". widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 15, v2:1289 and :1946-1948, flow-steps.md
  :241-242, scout D's row 15, shared interfaces 8 to 13 and disagreements 3, 6 and 9, and the sources
  read at `4bf0f400d`.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from edges of TOOL-dIndexedDesign-37, TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.

## 10. Reuse audit

The seams extended are `derive_parallel_step` (`tools/memory-tree/gen_build_index.py:1724`), whose
inline segment filter and write test become `design_lib.derive_write_meet` over the one rule
`check_writes_intersect` (`design_lib.py:601`), at their second instance; the unit records
`parse_spec` builds (:488-549), `read_spec_writes` (`design_lib.py:528`) and `read_spec_edges` (:543)
included; `parse_front_matter` (:405) for the signal; TOOL-dTotalRecall-25's kind and validator for the
record; and the build harness's `roles` and `efforts` arguments
(`tools/workflows/unattended-build.template.js:449-534`) as the shape of the planner stage's typing.
`python tools/codebase-map/reuse_lookup.py "group roster units into streams by order and write sets"`
ranked name stems (`write` in `gotchas.py`, `units` and `roster` in `unattended.test.sh`) and named
`check_writes_intersect` and `read_spec_writes`, both reused; no harness, role or workflow entry plans
streams, so no existing seam fits the planning workflow, and S6 adds it. Scout D's lines held at
`4bf0f400d` except `ORDER_RE`, at :213, as it says; its shared interface 12 proposed `streams: plan`,
rejected by §8 F2; its product list named `tools/roles/workflows.toml` and `tools/roles/house/policy.toml`,
neither written here, the first an ask (§8 F3) and the second already resolving `medium` through
`[effort] default`.

Recall terms used: `python tools/memory-recall/query.py "how does a planner group a build's units into parallel streams" --terms "stream-plan planner design.streams design.streams-when derive_parallel_step check_writes_intersect overlap gov-planner order write sets"`
