# TOOL-dDeclaredLoop-45 — a unit reads `built` from its pass commit while no acceptance writer is armed

**Status:** INPROGRESS · rev-3 · 2026-11-15 · node d · Tier-2 · base ed497191 · streams tooling · order 18 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-45-deviation-451.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-45-deviation-451.md) | deviation | — |
| [2026-11-15-build-TOOL-dDeclaredLoop-45-deviation-452.md](../build/2026-11-15-build-TOOL-dDeclaredLoop-45-deviation-452.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-45-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-45-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-45-build-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-45-build-brief.md) | journal | — |
| [2026-11-15-prompt-TOOL-dDeclaredLoop-45-reground-brief.md](../prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-45-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md`)
confirmed finding **id 6 at HIGH**, its item **H6**, alone in that item. `TOOL-dDeclaredLoop-7` S2
marks a unit `built` only when an attributed pass commit sits on the run branch and a well-formed
acceptance record names the unit and that commit. The only writer of that record is
`TOOL-dDeclaredLoop-17`'s stand-in `loop_witness.py acceptance`, which writes only when a caller runs it,
and `TOOL-dDeclaredLoop-17` §3 says there is no executor and that the stand-in parses no spec. So once
`--plan` reads the engine, every unit with its pass commit reads `designed`, and the `next:` line keeps
naming built units as live; the fixtures plant acceptance records, so `TOOL-dDeclaredLoop-7` AC1 and
AC10 stay green over the gap. This unit takes the report's second fix: while the declared writer is a
stand-in, a unit no acceptance record names reads `built` from its pass commit, tagged
`acceptance unarmed`. It repairs `TOOL-dDeclaredLoop-7`.

## 2. Scope (IN)

- **S1** — The armed state. The acceptance half of `built` is armed unless the definition's
  `[[computed-witness]]` row named `acceptance` has a `writer` of the stand-in form, the pattern
  `ROUTE_STAND_IN` against which `check_computed_witnesses` in `tools/loop/loop_lib.py` already grades
  every writer. The engine grades the rows with `check_computed_witnesses` over the definition it already
  read, `read_computed_witnesses` being that call over the shipped one, so a fixture's in-memory
  definition decides for its own call. The shipped writer, `stand-in:{prefix}/loop/loop_witness.py`,
  reads unarmed. A writer of the actor form, such as the item's own actor `executor:build.acceptance`,
  reads armed, and so does a definition holding no `acceptance` row: the relaxation needs a
  declaration. A refusal of the rows is the engine's `invalid-input`. Observed by AC1, AC2.
- **S2** — The unarmed reading, in `derive_unit_step`. Unarmed, a unit that has
  `TOOL-dDeclaredLoop-7` S2's attributed pass commit and that no acceptance record names in `Caused-by`
  reads `built`. A unit some record names is decided by `TOOL-dDeclaredLoop-7` S2's record rule exactly
  as when armed: `built` where one such record is well-formed and names the pass commit in `Sha`,
  `designed` otherwise (§8 F3). Armed, `TOOL-dDeclaredLoop-7` S2 stands unchanged. Observed by AC1, AC2.
- **S3** — The tag. A unit whose step is `built` or later, read unarmed with no record naming it, prints
  its line as `unit — <id> · <step> · acceptance unarmed`. Every other unit line keeps
  `TOOL-dDeclaredLoop-7`'s bytes. Observed by AC1, AC2.
- **S4** — The plants. `built-unarmed`, `built-unheld` and `built-armed` join `PLANTS` in
  `tools/loop/position.py` and run under its `--selftest` (§4 "The plants"); `built-unarmed` also runs
  the driver's `--plan` over its repository, as `TOOL-dDeclaredLoop-7`'s `plan-line` plant does, and
  holds its `next:` line. Observed by AC1, AC2, AC3.

## 3. Non-goals (OUT)

- Wiring the stand-in into the pass path: `TOOL-dDeclaredLoop-17` §3 refuses any parse of a spec's
  acceptance commands, so no caller can name them for it; the executor's build arms the writer.
- Grading a record's run exits: a record keeps no expected exit (§8 F3).
- The `tested` and `deployed` witnesses: `TOOL-dDeclaredLoop-7` S2's, unchanged.
- The armed predicate's named constant, the line grammar in `TOOL-dDeclaredLoop-7` §4, the `--json`
  field and the driver reading the optional field: `TOOL-dDeclaredLoop-67` S16 and S50.
- The `next:` shape printed for an `act` whose unit is past `designed`: `TOOL-dDeclaredLoop-7` §4's
  mapping, unchanged here.
- The witness sentence of the unit table's row into `built` in `tools/loop/loop.toml`, which names the
  armed reading and decides no step.
- A spec-set join of record kinds with readers and no writer, the finding's left-shift: not named by any
  clause of this build; the class is recorded at the close.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-7` — `derive_unit_step` in `tools/loop/position.py`, its record rule, its unit line, its `PLANTS` and the `--plan` `next:` line it renders, whose `built` witness this unit arms by state
- **consumes-from** `TOOL-dDeclaredLoop-17` — `read_computed_witnesses` and the `acceptance` row's writer, which say whether the acceptance half of `built` is armed
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 11, 44 and 48: this pass keeps the loop position fixtures leg green; the armed predicate's named constant, the amended line grammar and its `--json` field are scope items of that unit

## 4. Design

### Evidence

Every claim below was read on `branch/unattended-declared-loop-d56bf0` at `f395dba68`; the worktree's
main lacks the loop kit.

- The shipped `acceptance` row serves `item.build.acceptance` with writer
  `stand-in:{prefix}/loop/loop_witness.py`, armed by dWellOiledMachine
  (`tools/loop/loop.toml@86ccb031eca7:154`), and the item's actor is `executor:build.acceptance`
  (`tools/loop/loop.toml@86ccb031eca7:1291`).
- `check_computed_witnesses` (`tools/loop/loop_lib.py#check_computed_witnesses`) admits a writer only
  as `ROUTE_STAND_IN` or as `<kind>:<name>` with a kind of `ACTOR_KINDS`, and the two forms are
  disjoint, since `ACTOR_FORM`'s kind is lowercase letters alone and `stand-in` carries a hyphen
  (`tools/loop/loop_lib.py@3ac2c9502a12:156`, `tools/loop/loop_lib.py@3ac2c9502a12:203`). A definition
  with no such table holds no row. `read_computed_witnesses`
  (`tools/loop/loop_lib.py#read_computed_witnesses`) is that grading over the shipped definition.
- `TOOL-dDeclaredLoop-17` §4 says this unit reads that row's writer, a `stand-in:` value leaving the
  acceptance half of `built` unarmed.
- An acceptance record carries `Sha`, `Writer` and `Caused-by` and one run line per command, and
  `read_acceptance` (`tools/memory-tree/build_records.py#read_acceptance`) reports a malformed record in
  its `malformed` list rather than raising. The stand-in grades no exit against an expectation
  (`tools/loop/loop_witness.py@1a88f8fa6525:37`), and its own acceptance plant owes a record whose
  second run exits nonzero (`tools/loop/loop_witness.py#check_acceptance_plant`).
- `TOOL-dDeclaredLoop-7` rev-4 S2 reads `built` from the pass commit and a well-formed record naming the
  unit in `Caused-by` and that commit in `Sha`. Its §4 maps every `act` whose unit's spec is tracked to
  the live-unit shape, and its build step is the least-advanced unit's, ties broken by the hand-over's
  row order, so a built unit misread `designed` and listed first takes the `next:` line.
  `tools/loop/position.py` is not in the tree; this unit is written on that committed spec.
- Today's ladder, `NEXT_RUNGS` and `derive_next_shape`
  (`tools/unattended/unattended.sh#derive_next_shape`), reads the roster's typed state and no acceptance
  record.

### The rule

| Acceptance row's writer | A record naming the unit | Pass commit | Step |
|---|---|---|---|
| stand-in form | none | present | `built`, tagged `acceptance unarmed` |
| stand-in form | one holds | present | `built` |
| stand-in form | none holds | present | `designed` |
| actor form, or no row | none, or none holds | present | `designed` |
| actor form, or no row | one holds | present | `built` |
| any | any | absent | `TOOL-dDeclaredLoop-7` S2 unchanged |

A record holds when `TOOL-dDeclaredLoop-7` S2's record rule says so; this unit adds no second reading of
a record. The armed state is read once per engine call.

### The plants

Each builds its repository as `TOOL-dDeclaredLoop-7`'s plants do, units A then B in roster order.

| Case | Plant | Owed |
|---|---|---|
| `built-unarmed` | A has an attributed pass commit and no record; B is designed, no pass commit; the shipped `acceptance` row | `unit — A · built · acceptance unarmed` and `unit — B · designed`; the driver's `--plan` `next:` line names B and not A |
| `built-unheld` | the `built-unarmed` repository and a well-formed record with `Caused-by` A whose `Sha` is a commit not attributed to A | `unit — A · designed`, no tag |
| `built-armed` | the `built-unarmed` repository with the in-memory row's writer set to `executor:build.acceptance`, then with the row absent | `unit — A · designed`, no tag, each time |

Against `TOOL-dDeclaredLoop-7`'s rule `built-unarmed` is red: A reads `designed` and, listed first,
takes the `next:` line. The other two are green there and red against an unarmed reading that ignores a
record or outlives its declaration.

### Files touched (estimate)

- `tools/loop/position.py`
- `help/loop.md`: the position section names the tag and what lifts it
- `tools/loop/README.md`: where its position section spells the unit line
- `tools/run-gates/selftest-budgets.txt`: the `loop position fixtures` row re-priced

### Alternatives rejected

- **Wiring `loop_witness.py acceptance` into `--dispatch`'s close.** The caller would have to extract the
  criterion commands from a spec, which `TOOL-dDeclaredLoop-17` §3 rejects: a criterion carries several
  backticked tokens and prose, so any parse guesses.
- **Reading the pass commit alone while unarmed.** A record that names the unit and does not hold would
  read `built` while unarmed and `designed` once armed, so arming would move units whose records exist
  (§8 F3).
- **The record's own `Writer` field as the armed state.** It says who wrote one record, not which writer
  is declared, and a unit with no record has none to read.

## 5. Production-readiness checklist

- security — read-only, no new surface. `tools/loop/position.py` spells no install prefix, since the
  stand-in form is the imported `ROUTE_STAND_IN`, so `install-prefix (shipped surface)` stays green.
- perf / scale — no new file read and no new spawn: the rows are graded from the definition the engine
  already parsed, and the records are those it already reads, so the `unattended-status` row of
  `memory/project/fork-ceilings.txt` holds.
- error / empty / loading states — unarmed is printed on the unit line, never silent; a refused row is
  `invalid-input`; a definition with no `acceptance` row reads armed.
- observability — the `acceptance unarmed` tag on each unit read that way.
- risks — until the executor lands, `built` rests on the pass commit for a unit no record names. The
  `--json` output carries no armed field until `TOOL-dDeclaredLoop-67` S50. A built unit that is the
  least-advanced still takes the `next:` line in the live-unit shape through `TOOL-dDeclaredLoop-7`
  §4's `act` mapping; this unit corrects only the misreading of such a unit as `designed`.
- dependency — `tools/loop/position.py` is `TOOL-dDeclaredLoop-7`'s, order 17, built before this unit
  at order 18. This unit is written on its committed spec at rev-4 and starts from its landed bytes,
  `derive_unit_step`, the unit line and `PLANTS` included. Units 8 and 59, built beside it, change the
  claim key and the policy guard's merge arm, neither of which this unit reads.
- registry and pins — no leg, flag or kit is added, so `tools/gate-legs.json`'s rows,
  `tools/govkit/registry.toml`, `tools/govkit/subject-pins.tsv` and `tools/govkit/usage.toml` do not
  move. The leg's `ceiling` stays as `TOOL-dDeclaredLoop-7` sets it; only if
  `leg ceilings clear their evidenced maximum` reds on the re-priced budget does it move, and then
  `memory/guides/SESSION-KICKOFF.md`'s audit block is restamped, since the kickoff manifest watches
  `tools/gate-legs.json`. The budget row is re-priced from a direct-CLI reading of the three plants
  added to `TOOL-dDeclaredLoop-7`'s reading, x1.5, as the loop legs' rows are. The verdict-epoch gate's
  delegate list holds memory-tree modules and no file of this unit. The rule mints no top-level name,
  so `memory/map/generated/symbols.json` holds; a name a plant does mint regenerates it with
  `python tools/codebase-map/gen_map.py --write`.
- fixtures — a `TOOL-dDeclaredLoop-7` plant whose unit has a pass commit and no record and owes
  `designed` newly reds; the builder reads `PLANTS` at that unit's landed bytes and plants a
  well-formed record for each such unit, keeping its owed step. The `next:` shapes keep their bytes, so
  check 30 of `tools/unattended/check-unattended.sh` and the shape readers `TOOL-dDeclaredLoop-7` S8
  names are untouched. `tools/unattended/unattended.test.sh`'s engine arms are waived for this build's
  landing (the build README's waiver, owner 2026-10-20). `loop_witness.py --selftest` and its reader
  plants read `tools/loop/loop.toml` and `tools/loop/loop_lib.py`, which this unit does not edit.
- testing — the three plants under `--selftest`, each also run alone by `--plant`.
- migration — none; no record changes shape.
- user docs — a sentence in `help/loop.md`'s position section naming the tag and the executor's build
  that lifts it.

## 6. Acceptance criteria

- **AC1** — When `python position.py --fixture --plant built-unarmed` runs in the loop kit,
  unit A prints `unit — <A> · built · acceptance unarmed` and unit B prints `unit — <B> · designed`.
  Red when: the missing record keeps A `designed`, or A's line lacks the tag.
- **AC2** — When `python position.py --fixture --plant built-unheld` runs, A prints
  `designed` with no tag; and with `--plant built-armed`, A prints `designed` with no tag both with the
  row's writer set to `executor:build.acceptance` and with the row absent.
  Red when: the unarmed reading ignores a record that names the unit, or outlives the writer being
  armed or undeclared.
- **AC3** — When `python position.py --fixture --plant built-unarmed` runs, the driver's
  `--plan` `next:` line over the plant's repository names B and not A.
  Red when: the line names the built unit as live, the regression the finding records.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `memory hygiene` · `docs` · `install-prefix (shipped surface)` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `spawn budget (forks per hot entrypoint)` · `unattended kit gate` · `spec tokens (a spec's own names resolve)`

The plants run in the leg `loop position fixtures`, which `TOOL-dDeclaredLoop-7` adds.

New arm: tools/loop/position.py · covers AC1 AC2 AC3 · the `built-unarmed`, `built-unheld` and `built-armed` plants, staged against `TOOL-dDeclaredLoop-7`'s rule, which reads A `designed` and names it on the `next:` line · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Wire the stand-in, or read `built` from the pass commit while unarmed?** Options: (a) the stand-in
  run by the pass path; (b) S2's state-armed rule. (a) violates `TOOL-dDeclaredLoop-17` §3's non-goal,
  veto 1. RESOLVED (agent, 2026-10-24, delegated): (b), rung 3. It relaxes nothing against base, whose
  ladder reads the roster's typed state and no acceptance record. widens: none · relaxes: none
- **F3 — While unarmed, what does a record that names the unit decide?** A record keeps its run lines'
  exits and no expected exit, and a criterion may owe a nonzero exit. (a) `TOOL-dDeclaredLoop-7` S2's
  record rule decides wherever a record names the unit, and the pass commit alone decides only where
  none does; (b) the pass commit alone decides while unarmed, records unread; (c) (a), and a run line
  with a nonzero exit keeps the unit `designed`. (b) moves every unit with a record that does not hold
  when the writer is armed, and (c) reads a refutation the record cannot state. Recommendation (a), the
  body's: the record rule lives once, in `TOOL-dDeclaredLoop-7`.
  RESOLVED (agent, 2026-11-15, delegated): (a), rung 3: a record that names the unit is read as when
  armed, and the pass commit stands alone only where no record names it
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 6 (HIGH, item H6).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-15 · §1 · S1 S2 S3 S4 · §3 · §4 · §5 · AC1 AC2 AC3 · §7 · §8 F2 F3 · §10 ·
  re-grounded on the run branch at `f395dba68` by the brief
  2026-11-15-prompt-TOOL-dDeclaredLoop-45-1-spec-writer; mechanism, order and status kept. The armed state is the row's writer form graded by
  `check_computed_witnesses`, a missing row reading armed; a record that names the unit is decided by
  unit 7's record rule, since a record keeps no expected exit (F3), so `built-refuted` becomes
  `built-unheld` and `built-armed` joins it; AC3 is a plant of `position.py` rather than a probe, and
  `tools/unattended/unattended.sh` leaves the estimate; the audit record's path, F2's ladder reading
  and the write set are corrected.

## 10. Reuse audit

The seams are `check_computed_witnesses` (`tools/loop/loop_lib.py#check_computed_witnesses`), the one
declaration of which computed witness has which writer, with the `ROUTE_STAND_IN` form it grades; and
`TOOL-dDeclaredLoop-7`'s `derive_unit_step` with its record rule, which the unarmed reading calls rather
than restating, and its plant table with the `plan-line` driver run. The rule adds a table read, never a
second list of armed witnesses. `python tools/codebase-map/reuse_lookup.py "the acceptance half of a
unit's built step, armed when the computed witness writer is no stand-in"`, run over the run branch's
tree at `f395dba68`, ranked name-stem hits only (`write`, `arm`, `armed` in
`tools/memory-tree/corpus_ids.py#armed`, `read_steps` in `tools/loop/loop_lib.py#read_steps`), none of
which grades a witness by its writer; `tools/loop/position.py` is unbuilt, so the map holds none of its
names.

Recall terms used: built acceptance record unarmed stand-in executor computed-witness writer position next plan pass commit
