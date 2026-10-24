# TOOL-dDeclaredLoop-27 — the scenario kind and namespace: gov's five scenarios, admission, conflicts and the pin per step

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 24 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0112@de8c6c54 whole
**Carries:** node:tag-namespace.scenario
**Carries:** node:policy-key.flow.scenario-default
**Carries:** node:policy-key.flow.scenario-conflict

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-b.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |

<!-- /gen:spec-records -->

## 1. Goal

A build records what kind of work it is, and the flow it runs follows: a `scenario` is a registered
kind whose row activates rows of other kinds, a build runs the scenarios it was placed under, and two
builds of one repository can run two variants at once (the owner's NT-1, NT-6 and NT-7,
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:99-120`). Today
six seams vary the flow with no common selector and no build records its variant (`gap-flow-20`;
research-scenarios-design's question 8, six seams, no selector).

## 2. Scope (IN)

- **S1** — The kind. A `[[kind]]` row `kind.scenario` in `tools/playbook/kinds.toml` (dOrderedCharter-7
  S4, I15), its population gov's pack `tools/loop/scenarios.toml` and the overlay's `[[scenario]]`
  rows, its factory arm `python tools/playbook/core.py new scenario <name>` (dOrderedCharter-7 S6), and
  its `schema` naming `tools/loop/scenario-schema.toml` (dOrderedCharter-36 S1). Observed by AC7.
- **S2** — The namespace. A `[[namespace]]` row `scenario` in `tools/playbook/namespaces.toml`
  (dOrderedCharter-19 S4) whose extractor reads every `tag` of the population: gov's rows tagged
  `scenario.<name>`, a repository's `scenario.adopter.<name>` in the owner seat (I2). Observed by AC7.
- **S3** — The row. Each scenario row names `extends` (a scenario tag or `none`), `admits` (its
  admission predicate, a table from a fact name to the list of values that admit), `entry` (the step tag
  a build enters at), `activates` (a table from a kind tag to that kind's rows, in the overlay row
  grammar of dOrderedCharter-35) and `then` (a list of `{ at = <step tag>, scenario = <tag> }`, the
  scenario that takes over at that step's exit). The kinds a scenario may activate are the schema's
  `activatable` list, `kind.item` (TOOL-dDeclaredLoop-24) and `kind.splice` (TOOL-dDeclaredLoop-25), a set field
  declared `widens = "add"`, so each later build admits its own kind's rows by adding its kind.
  Observed by AC4 and AC7.
- **S4** — Gov's shipped scenarios in `tools/loop/scenarios.toml`: `scenario.feature`,
  `scenario.amendment`, `scenario.patch`, `scenario.playbook-run` and `scenario.design-only` (NT-6),
  each admitting the request's `entry` fact of its own name, `scenario.design-only` admitting
  `entry = feature` with `design-only = true`. `scenario.design-only` passes all five stages, so P20
  stands; the record-unit rows it would activate are admitted by the build that registers the unit
  kind. Observed by AC1 and AC7.
- **S5** — Admission. `select_scenarios(facts, composition)` in the new module
  `tools/loop/scenario.py` returns every scenario whose predicate holds over the request's facts, in
  the declared order the placement gives, and `flow.scenario-default`'s value when none holds.
  The facts are a request's, which placement hands (dPlacedRequest's `entry.place`); until it lands the
  CLI takes them as `--fact <name>=<value>`, and a build with no facts runs `flow.scenario-default`.
  The key is read through dGroundRules-2's `resolve`, default `feature`, and a value naming no
  registered scenario is refused naming the key. Observed by AC1 and AC6.
- **S6** — The composition. A build's composition is gov's packs, the repository's overlay, the rows its
  scenarios activate in their declared order, then its own recorded changes (TOOL-dDeclaredLoop-28),
  composed by dOrderedCharter-35's `compose_rows`, so every check reads the composed result. A scenario
  whose activated rows take out, reorder or swap a gov stage is refused by those checks. Observed by AC3.
- **S7** — Conflicts, as `flow.scenario-conflict` says (default `refuse`): two placed scenarios setting
  one field of one row to different values refuse the composition under `refuse`, naming both
  scenarios, the row and the field; under `declared-order` the later scenario in the declared order
  wins, and the settlement is recorded on the transition record into the step. Observed by AC4 and AC5.
- **S8** — The pin and the switch. `scenario` and `scenario-settled` join `TRANSITION_FIELDS` in
  `tools/loop/loop_transition.py` (TOOL-dDeclaredLoop-3 S1), so every transition record into a step
  carries ` · scenario=<tag>+<tag>…`, the placed scenarios in declared order joined by `+`, and, when
  S7 settled a conflict, ` · scenario-settled=<row tag>:<field>:<winner>:<loser>+…`, each written
  through `write_transition`'s `--field` and inside the value grammar that record admits, beside the
  composition revision TOOL-dDeclaredLoop-26 pins. The build's first record,
  into `planning`, stands in for its claim until dPlacedRequest's `entry.claim` lands. A scenario
  changes only at a step boundary, and at a step's exit the scenario a placed scenario's `then` names
  for that step takes over on the next record. Observed by AC2 and AC8.
- **S9** — Successor chains. The `then` edges and the `extends` edges are each acyclic, checked by
  TOOL-dDeclaredLoop-12's needs-graph helper in `tools/lib/` (I14), a cycle refusing the pack and
  naming it. Observed by AC9.
- **S10** — The fixture: `python tools/loop/scenario.py --fixture --plant <case>` builds a scratch
  repository with gov's pack, an overlay scenario and builds' transition records, each plant run
  against its expected observation by `--fixture` alone; the leg `loop scenario fixtures` in
  `tools/gate-legs.json`, argv `python {prefix}/loop/scenario.py --fixture`, declared in
  `tools/loop/kit.toml`. Observed by AC1 to AC9.
- **S11** — The page `help/loop.md` (TOOL-dDeclaredLoop-1 S7) gains a section on scenarios: gov's
  five, how one is admitted, the default, a conflict under each value and the switch at a step
  boundary. Observed by AC10.

## 3. Non-goals (OUT)

- No placement: `entry.place` naming the scenarios, `placement.check` witnessing them and the planner's
  re-pick are dPlacedRequest's. This unit ships the selection function and the default.
- No preset slot and no caps on a scenario row: a scenario's policy scope (NT-3) needs presets that
  scope per build, which dKeptSession's preset kind lands.
- No promotion of a change into a scenario: the Loop Review proposing one (NT-5) is a later program.
- No scenario per feature or per unit: they wait on the feature and unit tables (NT-7, `gap-flow-15`).
- No workflow shapes as data (NT-8).
- No reference page of the kind's rows: dOrderedCharter-37 renders those from each registry.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-3` — `Gov-Transition`, whose `TRANSITION_FIELDS` the `scenario` and `scenario-settled` fields join and whose `write_transition` records them
- **consumes-from** `TOOL-dDeclaredLoop-26` — composition revision, the pin beside which the `scenario` field is recorded and at which a build's composition is read
- **consumes-from** `TOOL-dDeclaredLoop-12` — `needs`, the needs-graph helper whose acyclicity check runs over the `then` and `extends` chains
- **hands-off** `TOOL-dDeclaredLoop-28` — `scenario`, the placed scenarios whose composition a build's recorded changes apply over
- **hands-off** `TOOL-dDeclaredLoop-33` — `scenario`, the successor chains and composed scenarios the termination check reads
- **hands-off** external — dPlacedRequest's `entry.place` and `entry.claim` take over the facts and the claim pin this unit stands in for

## 4. Design

### Data model

```toml
# tools/loop/scenarios.toml, gov's pack
[[scenario]]
tag = "scenario.design-only"
extends = "scenario.feature"
admits = { entry = ["feature"], design-only = ["true"] }
entry = "step.plan"
activates = {}
then = []
```

A repository's row in `.governance/instructions.toml` has the same keys and an `adopter` tag:

```toml
[[scenario]]
tag = "scenario.adopter.mobile"
extends = "scenario.feature"
admits = { entry = ["feature"], platform = ["mobile"] }
entry = "step.plan"
activates = { "kind.item" = [ { tag = "item.test.adopter.device-farm", needs = ["item.test.unit-pass"] } ] }
then = []
```

`extends` means the scenario's `admits`, `entry`, `activates` and `then` start from its parent's and
override the keys it sets. The facts are a closed set per request: `entry` (feature, amendment, patch,
playbook-run) and `design-only` from gov, and any fact a repository's predicate names, which
placement must supply or the predicate does not hold.

### Composition and conflicts

`compose_scenarios(placed, mode)` turns the placed scenarios into one ordered list of overlay-shaped
rows. Two rows from two scenarios addressing one row tag and one field with different values is a
conflict; `refuse` raises it, `declared-order` keeps the later and returns the settlement
`<row tag>:<field>:<winner>:<loser>`, the entry S8 writes into `scenario-settled`. The list then enters `compose_rows` after the
overlay's own rows and before TOOL-dDeclaredLoop-28's recorded changes.

### The switch at a step boundary

At a transition into a step, the writer asks `derive_step_scenarios(build)`: the scenarios of the
previous record, each replaced by the scenario its `then` names for the step just exited, and the
settlement recomputed. Between boundaries the scenario is read from the latest record into the current
step, so two builds pinned to different scenarios each derive their own composition at once.

### Inventory

| Minted | Kind |
|---|---|
| `kind.scenario` | `[[kind]]` row |
| `scenario` | `[[namespace]]` row, its extractor in `tools/loop/scenario.py` |
| `scenario.feature`, `scenario.amendment`, `scenario.patch`, `scenario.playbook-run`, `scenario.design-only` | gov's scenario rows |
| `extends`, `admits`, `entry`, `activates`, `then`, `activatable` | scenario row and schema keys |
| `select_scenarios`, `compose_scenarios`, `derive_step_scenarios` | functions, `tools/loop/scenario.py` |
| `scenario`, `scenario-settled` | transition record fields (I8), in `TRANSITION_FIELDS` |

The policy keys' catalogue rows already exist (dGroundRules-1 S3 writes one per v2 row, v2:1264-1265),
so this unit adds their reader only (I10). Each function name is put to
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` in the build pass.

### Migration

None. A build with no recorded scenario reads `flow.scenario-default` at its next boundary and pins it.

### Rollout

Live at landing. Every gov build runs `scenario.feature` until placement supplies other facts, and that
scenario activates nothing, so no gov build's flow moves.

### Files touched (estimate)

- `tools/loop/scenario.py` (new)
- `tools/loop/scenarios.toml` (new)
- `tools/loop/scenario-schema.toml` (new)
- `tools/playbook/kinds.toml`
- `tools/playbook/namespaces.toml`
- `tools/playbook/core.py`: the `new scenario` arm
- `tools/loop/loop_transition.py`: the two fields in `TRANSITION_FIELDS`, and `derive_step_scenarios`
  called before `write_transition` writes
- `tools/loop/kit.toml`: the module and the leg declared
- `tools/gate-legs.json`: the leg `loop scenario fixtures`
- `help/loop.md`: the section of S11

### Alternatives rejected

Research-scenarios-design's candidates A to G, each with the losing test it records: presets as
scenarios (presets assign keys only), playbooks as scenarios (a content recipe), the composition alone
(one composition per repository), conditional rows (nothing to name or pin), chains of builds only
(no in-build variation) and shape variants (a role item's slot). D, the kind over the composition, is
what this unit builds; F survives as `then` and as cross-build `depends-on`.

## 5. Production-readiness checklist

- security — a repository's scenario reaches the composition only through the overlay, whose write is
  guarded (dOrderedCharter-15); no new write path but the record field.
- perf / scale — one predicate pass per placement and one compose per transition.
- error / empty / loading states — no admitting scenario runs the default; an unregistered default, a
  conflict under `refuse` and a cycle each refuse by name.
- observability — the placed scenarios and every settlement are on every transition record into a step.
- risks — a repository predicate naming a fact placement never supplies never admits, silently; the
  selection prints the facts it read.
- testing — the fixture plants of S10, run by the pass; the suite arm in §7 at the close.
- migration — none.
- user docs — `help/loop.md` gains the scenarios section; the reference page renders from the
  registry rows (dOrderedCharter-37).

## 6. Acceptance criteria

- **AC1** — When `python scenario.py select --fact entry=patch` runs over gov's pack it prints
  `scenario.patch`, with `--fact entry=feature --fact design-only=true` it prints
  `scenario.feature scenario.design-only` in declared order, and with no fact it prints the value of
  `flow.scenario-default`, `scenario.feature`.
  Red when: a request no predicate admits returns an empty list and the build runs no scenario.
- **AC2** — When `python scenario.py --fixture --plant two-builds` positions a build pinned to
  `scenario.feature` and one pinned to `scenario.adopter.mobile` at once, only the second's
  composition carries `item.test.adopter.device-farm`, and each build's position reads its own.
  Red when: the scenario is read repository-wide, so both builds carry the activated item.
- **AC3** — When `python scenario.py --fixture --plant drops-stage`, `--plant reorders-stage` and
  `--plant replaces-stage` each place a scenario whose activated rows take out, reorder or replace
  `step.test`, each composition is refused naming the scenario and the stage.
  Red when: the checks read the overlay text and not the composed rows, so a scenario's rows pass.
- **AC4** — When `python scenario.py --fixture --plant conflict` places two scenarios setting one item's
  `actor` differently under `flow.scenario-conflict` = `refuse`, the composition is refused naming both
  scenarios, the item and `actor`.
  Red when: the later scenario silently wins under `refuse`.
- **AC5** — When the same plant runs under `declared-order`, the later scenario's `actor` stands, and the
  transition record into the step carries the settlement naming the item, `actor`, the winner and the
  loser.
  Red when: the settlement is applied and not recorded, so the record cannot say which variant ran.
- **AC6** — When `python scenario.py --fixture --plant bad-default` sets `flow.scenario-default` to
  `scenario.nowhere`, selection with no admitting scenario refuses naming the key and the value.
  Red when: an unregistered default falls back to `scenario.feature` without a word.
- **AC7** — When `python core.py new scenario adopter.trial` runs in the fixture
  repository, the row it writes carries every key S3 names and the kind's gate reads it clean, and the
  tag index lists `scenario.adopter.trial` under the `scenario` namespace.
  Red when: the namespace row is missing, so the tag's first segment is no registered namespace.
- **AC8** — When `python scenario.py --fixture --plant mid-step-switch` changes a build's placed
  scenario between two boundaries, the position inside the step still reads the old scenario, and
  `python scenario.py --fixture --plant then` hands over to the scenario `then` names on the record
  after that step's exit.
  Red when: a placement change applies at once, inside the step.
- **AC9** — When `python scenario.py --fixture --plant then-cycle` and `--plant extends-cycle` load a
  pack whose `then` or `extends` edges form a cycle, each refuses naming the cycle's scenarios.
  Red when: the cycle check runs over `extends` only, so a pipeline loops for ever.
- **AC10** — When `grep -n "flow.scenario-conflict" loop.md` runs over the help page at this unit's
  commit, it finds the section naming gov's five scenarios, `refuse` and `declared-order`.
  Red when: the kind ships and the page says nothing of how a build's variant is chosen.

## 7. Gates

`govkit acceptance matrix` · `playbook render selftest` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/scenario.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC8 AC9 · the `loop scenario fixtures` leg's plants, its failing case staged by `conflict` with the later scenario winning under `refuse` · none
New arm: the kinds register's conformance gate dOrderedCharter-7 S5 runs · covers AC7 · the register before the `kind.scenario` row · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation,
  2026-10-24: `DRAFT` is not in the tuple. Liveness: the tuple would list it if the vocabulary admitted
  it. RESOLVED (agent, 2026-10-24, delegated): `OPEN`.
- **F2 — Under `declared-order`, which scenario wins a conflict?** Options: (a) the later in the declared
  order, as every later layer of the composition overrides an earlier one; (b) the earlier. v2:1265
  says "settled by the repository's declared order"; the composition's layering already gives later
  rows precedence (overlay over gov, recorded changes last). RESOLVED (agent, 2026-10-24, delegated):
  (a), by rung 1 read with dOrderedCharter-35's layering. widens: none. relaxes: none.
- **F3 — Where is the scenario pinned before `entry.claim` exists?** Options: (a) the build's first
  transition record stands in for the claim; (b) a new front-matter key on the build README; (c) no
  claim pin until dPlacedRequest. (b) adds a key the index generator refuses
  (`tools/memory-tree/gen_build_index.py:450`); (c) drops a clause bound. RESOLVED (agent,
  2026-10-24, delegated): (a), by rung 3. widens: none. relaxes: none.
- **F4 — What facts does an admission predicate read?** Options: (a) a closed gov set, `entry` and
  `design-only`, plus any fact a repository predicate names, supplied by placement; (b) build README
  front matter; (c) free text. (b) has no entry field and (c) cannot be evaluated. RESOLVED (agent,
  2026-10-24, delegated): (a), by rung 3, the CLI's `--fact` standing in for placement.

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 27, the night pass two's point 1,
  research-scenarios-design's option D and v2:1264-1265, read at base `ed497191`.

## 10. Reuse audit

No existing seam selects a scenario: `python tools/codebase-map/reuse_lookup.py "select a scenario by admission predicate over request facts and resolve field conflicts"`
ranked name stems (`resolve`, `field`, `resolve_kit_dir`) with no predicate or variant selector, and
research-scenarios-design records that no record defines a scenario. The unit extends its parents'
registers: the `[[kind]]` row and factory (dOrderedCharter-7 S4, S6), the `[[namespace]]` row
(dOrderedCharter-19 S4), the row grammar and `compose_rows` (dOrderedCharter-35) and the row checks
(dOrderedCharter-36), with TOOL-dDeclaredLoop-12's acyclicity helper for the chains.
`python tools/memory-recall/query.py` returned scout B's row, the night pass instruments' catalogue
rows for the two keys and the brief's row; scout B's v2:1264-1265 citation agrees with the packet's
Obligations at base.

Recall terms used: scenario kind admission predicate feature amendment patch playbook-run design-only conflict declared-order refuse
