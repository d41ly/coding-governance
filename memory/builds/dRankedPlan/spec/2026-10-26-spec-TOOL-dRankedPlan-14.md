# TOOL-dRankedPlan-14 — the plan record's scenario field, set from the placement and re-picked at Plan with its reason

**Status:** OPEN · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 6 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0382@182ba9ba whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-a.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) | spec-audit | TOOL-dRankedPlan-16 TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-2 TOOL-dRankedPlan-13 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-15 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-7 |

<!-- /gen:spec-records -->

## 1. Goal

A build runs the scenarios it was placed under: the orientation scout names them, `placement.check`
re-evaluates them, and the claim pins them on the build's first transition record
(TOOL-dPlacedRequest-10 S5, TOOL-dPlacedRequest-21 S7, TOOL-dDeclaredLoop-27 S8). The owner's NT-2
adds the step nothing builds: "the planner may re-pick at Plan; a later re-pick happens only at a step
boundary" (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:99-106`).
TOOL-dPlacedRequest-10 §3 leaves that re-pick to dRankedPlan's Plan items. This unit gives the plan
record's `Scenario` field its meaning: set from the placement, revisable by the planner at Plan with a
`Scenario reason`, pinned at Plan's exit, and changed later only through a plan revision.

## 2. Scope (IN)

- **S1** — The read, shared interface I19: `read_plan_scenario(repo, slug)` in `tools/loop/scenario.py`
  returns `(scenario, reason, source)`. The plan record's `Scenario` and `Scenario reason` fields are
  read through TOOL-dRankedPlan-16's field reader, `python plan_record.py field <slug> <Name>`
  (`read_plan_fields`, its S4), the memory-tree kit found by `resolve_kit_dir`. The placement's pin is
  the `scenario` field of the build's first transition record into `planning`, read by
  `read_transitions` (TOOL-dDeclaredLoop-3 S7). A tag written without its namespace reads with it, so
  `feature` is `scenario.feature`, as `flow.scenario-default`'s value names one (TOOL-dDeclaredLoop-27
  S5); a `Scenario reason` of `none` is no reason. A `Scenario` that is absent, empty or equal to the
  pin answers the pin with source `placement`; a different one answers itself with source `plan`, a
  re-pick. `python tools/loop/scenario.py plan --build <slug>` prints `scenario — <tag>+<tag> · from
  <plan|placement> · reason <text|none>`. Observed by AC1, AC2.
- **S2** — The check, `check_plan_scenario(repo, slug)` in `tools/loop/scenario.py`, run as `python
  tools/loop/scenario.py plan --build <slug> --check`, refusing, each naming the build:
  `scenario re-picked without a reason` when `Scenario` differs from the placement's pin and
  `Scenario reason` is `none` or empty; `scenario not registered <tag>` for a tag the scenario kind's
  population (`scenario.py members`, TOOL-dDeclaredLoop-27) does not hold; `scenario order <tags>`
  when the tags are not in that population's declared order; and `scenario re-picked after Plan · only
  through a plan revision` when the build's latest transition leaves it outside `planning` and
  `Scenario` differs from the scenario its latest move out of `planning` pinned. Exit 0 admitted, 1
  refused, 2 on an unknown build. Observed by AC3, AC4, AC5, AC6.
- **S3** — The pin at the step boundary: TOOL-dDeclaredLoop-27's `derive_step_scenarios(build)`, which
  every transition into a step asks, runs S2 first and refuses on its refusal; for a move out of
  `planning` it starts from S1's answer instead of the previous record's scenarios, then applies each
  scenario's `then` successor for the step exited and recomputes the settlement as that unit states.
  So the record of Plan's exit pins the re-pick, and a scenario still changes only at a step
  boundary. Observed by AC1, AC2, AC3, AC5, AC6.
- **S4** — The plants of §6, joined to `scenario.py --fixture` (TOOL-dDeclaredLoop-27 S10):
  `plan-placement`, `plan-repick`, `plan-repick-no-reason`, `plan-unknown`, `plan-order`,
  `plan-after-exit` and `plan-revised`. Observed by AC1 to AC6.
- **S5** — The scenarios section of `help/loop.md` (TOOL-dDeclaredLoop-27 S11) gains a paragraph: the
  planner's re-pick at Plan, its reason, the pin at Plan's exit, and the plan revision as the only
  later route. Observed by AC7.

## 3. Non-goals (OUT)

- The plan record kind, its file, its writer and its field reader: TOOL-dRankedPlan-16's (I3). This
  unit gives two of its fields their meaning and check.
- The scenario kind, its rows, `select_scenarios`, composition and conflicts: TOOL-dDeclaredLoop-27's.
- The placement's selection and its re-evaluation: TOOL-dPlacedRequest-10's `placement.check`. A
  re-pick is not re-admitted over the placement's facts (§8 F2).
- The plan revision, its record region, its ratification and the move back to `planning`:
  TOOL-dRankedPlan-15's. This unit refuses a re-pick outside `planning` and admits one once a
  revision has moved the build back.
- Ratifying the re-pick: it rides in the plan record, ratified with the plan (TOOL-dRankedPlan-9,
  TOOL-dRankedPlan-10).

### Edges

- **consumes-from** `TOOL-dRankedPlan-16` — `record-kind.plan`, the plan record whose `Scenario` and `Scenario reason` fields S1 reads through `read_plan_fields`; without it there is no field to re-pick in
- **hands-off** `TOOL-dRankedPlan-15` — `Scenario reason`, the reason a later re-pick carries once that unit's plan revision moves the build back to `planning`, where S2 admits the re-pick and S3 pins it at the next exit
- **consumes-from** external — dDeclaredLoop's `derive_step_scenarios`, `members` and `scenario.py --fixture` (TOOL-dDeclaredLoop-27 S5, S8, S10) and `read_transitions` (-3 S7); dPlacedRequest's placement pin on the first transition record (TOOL-dPlacedRequest-10 S5, -21 S7)
- **hands-off** `TOOL-dRankedPlan-20` — `read_plan_scenario` and `check_plan_scenario`, whose reading of `none` and whose pin for a build with no move into `planning` that unit corrects (round-1 spec audit, id 2)
- **hands-off** `TOOL-dRankedPlan-29` — `read_plan_scenario`'s field read, which that unit holds to the field verb's exit codes (round-1 spec audit, id 40)
- **hands-off** `TOOL-dRankedPlan-36` — `check_plan_scenario` and S3's call of it in `derive_step_scenarios`, which that unit gives the first move's own pin (spec audit of units 19 to 29, id 29)

## 4. Design

### Evidence

- The pin: every transition record into a step carries ` · scenario=<tag>+<tag>…`, the placed
  scenarios in declared order, and "a scenario changes only at a step boundary" (TOOL-dDeclaredLoop-27
  S8); at a transition the writer asks `derive_step_scenarios(build)`, "the scenarios of the previous
  record, each replaced by the scenario its `then` names for the step just exited" (its §4 "The switch
  at a step boundary").
- The placement: the placement record's `scenarios:` reaches the claim commit and the build's first
  transition record (TOOL-dPlacedRequest-10 S5; TOOL-dPlacedRequest-21 S2, S7).
- The fields: `Scenario` and `Scenario reason` are I3's, in `deviation_join.py`'s `FIELD` form, whose
  regex admits one lowercase second word (`tools/memory-tree/deviation_join.py:145`).
- No re-pick exists anywhere: TOOL-dPlacedRequest-10 §3 names "the planner's re-pick at Plan (NT-2's
  third clause)" as dRankedPlan's.

### The reading

| Plan record `Scenario` | Build's state | `Scenario reason` | Answer |
|---|---|---|---|
| absent, empty or equal to the placement's pin | any | any | the pin, `from placement` |
| different | `planning` | a reason | admitted, `from plan`, pinned at Plan's exit |
| different | `planning` | `none` or empty | refused, `scenario re-picked without a reason` |
| different from Plan's exit pin | past `planning` | any | refused, `only through a plan revision` |

Past `planning` the field is compared with the scenario Plan's exit pinned, not the placement's, so a
re-pick ratified at Plan stays valid through Design and Build, and an edit after it is refused at the
next boundary until a revision moves the build back.

```
derive_step_scenarios(build)
  check_plan_scenario(repo, build)            # S2; a refusal stops the move
  if the move leaves planning: start = read_plan_scenario(repo, build).scenario
  else:                        start = the previous record's scenarios
  then each tag's `then` for the step exited; settlement recomputed      # TOOL-dDeclaredLoop-27, unchanged
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_plan_scenario`, `check_plan_scenario` | functions, `tools/loop/scenario.py` | `py.function`, asked at the pass |
| `plan` | verb of `scenario.py`, with `--build` and `--check` | none |
| `plan-placement`, `plan-repick`, `plan-repick-no-reason`, `plan-unknown`, `plan-order`, `plan-after-exit`, `plan-revised` | `scenario.py` fixture plants | none |

### Migration

None. A build with no plan record, or a plan record with no `Scenario`, reads its placement's pin,
which is what `derive_step_scenarios` reads today.

### Rollout

Live at landing. A build placed before it keeps its pinned scenario unless its planner re-picks in
`planning` with a reason.

### Files touched (estimate)

- `tools/loop/scenario.py`: S1 to S4
- `help/loop.md`: S5's paragraph

### Alternatives rejected

- **The re-pick as its own record.** NT-2 places it at Plan, in the plan the owner ratifies; a second
  record would be a second home for the build's scenario.
- **Copying the placement's pin into the field at drafting.** A copy restates a fact the transition
  record owns; an empty field reads the pin, and an equal copy is admitted without a reason, so the
  record kind may require the field either way.

## 5. Production-readiness checklist

- security — no new write path: the field is written by the plan record's door and read here; the
  check only refuses.
- perf / scale — one record read and one population read per transition into a step.
- error / empty / loading states — every refusal names the build and the tag or reason; an unknown
  build exits 2.
- observability — `scenario.py plan` prints the answer and its source; the trailer carries the pin.
- risks — a stray edit to `Scenario` after Plan holds the build's next transition until it is
  restored or a revision moves the build back; that is the clause's "only through a plan revision".
- testing — the seven plants, red and green.
- migration — none.
- user docs — `help/loop.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python scenario.py --fixture --plant plan-placement` runs, a plan record reading
  `Scenario: feature` and `Scenario reason: none` over a first transition pinning `scenario.feature`,
  `scenario.py plan --build tFix` prints `scenario — scenario.feature · from placement · reason none`,
  `--check` exits 0, and Plan's exit record carries `scenario=scenario.feature`.
  Red when: a field equal to the placement's pin is read as a re-pick owing a reason.
- **AC2** — When the plant `plan-repick` sets `Scenario` to `scenario.design-only` with a reason in
  `planning`, `scenario.py plan --build tFix` prints `from plan` with the reason, and Plan's exit
  record carries `scenario=scenario.design-only`.
  Red when: the re-pick is not the scenario Design runs under.
- **AC3** — When the plant `plan-repick-no-reason` leaves `Scenario reason` at `none`,
  `scenario.py plan --build tFix --check` exits 1 printing `scenario re-picked without a reason`,
  and the move out of `planning` is refused.
  Red when: a re-pick lands with no reason.
- **AC4** — When the plants `plan-unknown` and `plan-order` set `scenario.nosuch` and two registered
  tags out of declared order, `--check` exits 1 printing `scenario not registered scenario.nosuch`
  and `scenario order`, respectively.
  Red when: an unregistered or reordered scenario reaches Plan's exit.
- **AC5** — When the plant `plan-after-exit` edits `Scenario` on a build in `designing`, `--check`
  exits 1 printing `only through a plan revision`, and the build's next transition is refused.
  Red when: a scenario changes after Plan without a plan revision, or between step boundaries.
- **AC6** — When the plant `plan-revised` records row B6's move back to `planning` and then the same
  edit with a reason, `--check` exits 0 and the next exit from `planning` pins the edited scenario.
  Red when: the revision's route cannot re-pick.
- **AC7** — When `grep -n "Scenario reason" loop.md` runs over the help page, it finds S5's paragraph
  naming the re-pick at Plan and the plan revision.
  Red when: the page does not describe the re-pick.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/scenario.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the seven `plan-*` plants in `--fixture`, the failing case `plan-repick-no-reason` reaching Plan's exit · none

## 8. Open questions

- **F1 — Is the re-pick at Plan a field pair or a revision record?** RESOLVED (agent, 2026-10-26,
  delegated): the field pair `Scenario` and `Scenario reason` in the plan record, rung 1: NT-2 lets the
  planner re-pick at Plan, the plan the owner ratifies, and sends a later re-pick through a plan
  revision (`cl-dClosedLoop-0382`). widens: none · relaxes: none
- **F2 — Does a re-pick re-run the admission predicates?** Options: (a) the tags checked for
  registration and declared order only, the reason its witness and the plan's ratification its
  approval; (b) every predicate re-run over the placement's facts, a failing one refused; (c) the
  predicates re-run over facts the planner supplies. (b) makes a re-pick unable to correct the
  placement, the case NT-2 adds it for; (c) adds a facts field no clause names. Scout A read NT-2's
  "re-evaluates every predicate" as binding the re-pick; that sentence is `placement.check`'s, of the
  scout's pick. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Where does the scenario's value live when the planner keeps the placement's?** Options: (a)
  the transition record's pin is the home, and a field absent, empty or equal to it reads as the pin;
  (b) the field is the home, copied at drafting and read alone. (b) makes the record a second home for
  a fact the transition record owns (`cl-dClosedLoop-0498`). RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3; TOOL-dRankedPlan-16's schema requires the field, and its example `Scenario: feature`
  with `Scenario reason: none` reads as the pin. widens: none · relaxes: none
- **F4 — How is "a later re-pick only at a step boundary through a plan revision" held?** Options: (a)
  S2's refusal past `planning`, run at every transition into a step; (b) the field read only at Plan's
  exit, an edit past it inert until the next. (b) leaves the record naming one scenario while the
  build runs another. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 14, NT-1 and NT-2, TOOL-dDeclaredLoop-27
  S5, S8 and §4, TOOL-dPlacedRequest-10 and -21 at base, and scout A's row for unit 14.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-20`, the hands-off edge to `TOOL-dRankedPlan-29`, each the reciprocal of that promoted unit's own edge (round-1 spec audit, `reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-36`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam is TOOL-dDeclaredLoop-27's `derive_step_scenarios`, the one place a build's scenario moves,
extended by one starting point for a move out of `planning` and one check before it, with the
population read through that unit's `members`; the placement's pin is read through
TOOL-dDeclaredLoop-3's `read_transitions`, and the fields through TOOL-dRankedPlan-16's reader.
`python tools/codebase-map/reuse_lookup.py "the scenario a build runs re-picked by the planner with a
reason and pinned at the next step boundary"` ranked name stems (`run`, `build`, `step`,
`build_commit`); none reads a scenario, because the loop kit is absent at base, so no existing seam
fits in source and the parent's specced function is the seam. The recall query returned scout A's row,
NT-2 and KICK-dKeptSession-20's reading of `derive_step_scenarios`, which agree with
TOOL-dDeclaredLoop-27. Where records disagree: scout A's F14b reads the re-pick as re-admitted (F2);
TOOL-dDeclaredLoop-27's Files touched names `loop_transition.py` beside `derive_step_scenarios`, which
its Inventory places in `scenario.py`, the caller and the definition respectively.

Recall terms used: `python tools/memory-recall/query.py "how does the planner re-pick a build's scenario at Plan and when may it change later" --terms "scenario re-pick NT-2 placement scenarios plan record Scenario reason step boundary derive_step_scenarios plan revision"`
