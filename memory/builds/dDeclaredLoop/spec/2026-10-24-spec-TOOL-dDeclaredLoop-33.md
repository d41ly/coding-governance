# TOOL-dDeclaredLoop-33 — the static termination check on every composition, at the push and at each step boundary

**Status:** INPROGRESS · rev-7 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 34 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0118@4c8ef789 whole

**Carries:** node:policy-key.flow.wait-ceiling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-33-deviation-331.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-33-deviation-331.md) | deviation | — |
| [2026-10-25-build-TOOL-dDeclaredLoop-33-deviation-332.md](../build/2026-10-25-build-TOOL-dDeclaredLoop-33-deviation-332.md) | deviation | — |
| [2026-11-05-build-TOOL-dDeclaredLoop-33-deviation-333.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-33-deviation-333.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-33-1-builder-return.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-33-1-builder-return.md) | journal | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-34 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-56 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-56 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks.md) | research | TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-56 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-33-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-33-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-33-2-spec-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-33-2-spec-brief.md) | research | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-33-3-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-33-3-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-33-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-33-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-33-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-33-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 |

<!-- /gen:spec-records -->

## 1. Goal

Every composition a build can run, gov's definition and packs with the repository's overlay, the
scenarios a build is placed under and its own applied flow changes, is checked before it runs: every
state reaches a terminal, every item is reachable, every cycle of the build table and of the item
routes passes a counted edge, every wait declares a deadline and the route past it, an applied loosening
names the owner's release, and every held loosening recommends the decline. Soundness alone failed on a
planted repository stage that routed back into itself with an exit (stall-and-loop.md:146-148), so the
counted-edge rule is its own. The check runs at the push and at each step boundary that applies a
build's change. Today nothing checks that a flow can finish (`gap-flow-24`, C2-F13, P39).

## 2. Scope (IN)

- **S1** — `check_termination(composition)` in `tools/loop/termination.py`, returning one finding per
  broken rule, each naming its rule, its row or item and why, and the CLI `python
  tools/loop/termination.py check [--build <slug>] [--selftest]`. `read_termination_inputs(root,
  build=None)` builds the composition §4 "Data model" gives. Without `--build` it reads gov's at HEAD:
  the definition through `tools/loop/loop_lib.py#read_definition`, the build table spliced with the
  composed stage rows through `tools/loop/splice.py#derive_spliced_table`, the composed items through
  `tools/loop/loop_items.py#read_composed_items` and the programs `tools/loop/loop_lib.py#check_program`
  returns. With `--build` it reads that build at its pin, `tools/loop/composition.py#read_step_composition`
  over `tools/loop/loop_transition.py#read_transitions`: its items through `read_build_items(repo, slug,
  moves, pin)` in `tools/loop/position.py`, which holds the lines `tools/loop/position.py#derive_position_into`
  composes them with today, its stages at the pin with its applied stage changes, and its flow rows
  through `tools/loop/adapt.py#read_flow_rows`. It prints every finding, the unchecked levels and the
  pending counts, and exits 1 on a finding. Observed by AC1 to AC5 and AC7 to AC11.
- **S2** — Rule `terminal`: every state of a level that declares a terminal set reaches it, by reverse
  reachability over that level's rows, a row into `@prior` or `@reentry` read as reaching every open
  state of its level; an empty state set is a finding and never passes. Today only the build level
  declares one, `[states]`'s `terminal` (`tools/loop/loop_table.py#read_transition_rows`); the feature and
  unit levels each print `loop: termination · terminal · <level> · unchecked — no terminal set`, never a
  pass, until `TOOL-dDeclaredLoop-54` declares theirs (§8 F11). Observed by AC2, AC4.
- **S3** — Rule `reachable`: every item of each program `check_program` returns, the five steps, each
  composed stage and, by `TOOL-dDeclaredLoop-50` S3, `review`, is reached by one walk from every
  program's entry, its items with no needs. The walk follows every item route to a declared item, and
  follows a need to the item needing it only where both items lie in one program. A route from another
  program's item enters this program, as `item.test.merge`'s `conflict` route enters
  `item.build.resolve`, whose one need lies in the test program. A need across programs is never
  followed: every item's needs lead back to some entry, so a walk along them could flag nothing (§8
  F12). Observed by AC3, AC10.
- **S4** — Rule `counted`: with every set-aside edge left out, the build table's rows and the item routes
  between declared items are acyclic, each cycle found by `scan_cycles`, the inline copy
  `tools/loop/loop_lib.py` carries of `tools/lib/needs_graph.py#scan_cycles`, and reported once. Set aside
  are a counted edge, an owner edge, an ending, a dynamic return and a declared wait, as §4 "The edges"
  defines each. A build row's count is derived, never typed (§8 F5). An item route is counted when the
  item's new field `draws`, an inline table from an outcome to one of
  `tools/loop/budget.py#CAUSES`, names its outcome, and a route into another step's item takes the class
  of the build row it fires. Gov's own item rows carry `draws`, `waits` and pending rows by §4 "Gov's own
  cycles at landing" (§8 F6). Observed by AC1.
- **S5** — Rule `wait`: an item's new field `waits`, a list of its outcomes, names the outcomes on which it
  waits on another party, and an item with an owner actor waits on the owner. Each such item declares
  `deadline`, a whole number of hours or `policy.<key>` naming a catalogue row
  `tools/policy/policy.py#derive_bounds` selects with a type of `DEADLINE_TYPES`, and `on-deadline`, an
  outcome of its set outside `waits` whose route it takes past the deadline. A wait whose deadline key
  belongs to a build that has not landed is a `wait` row of the shrink-only list
  `tools/loop/termination-pending.txt`, naming that build; a row whose build `derive_landed_owners` in
  `tools/policy/check_policy.py` reads landed, or whose item declares its deadline or is gone, is a
  stale finding. The check reads `flow.wait-ceiling` through the policy kit's `resolve` with the key as
  its literal, the reader `check_reader_coverage` counts, and prints its value. Observed by AC5.
- **S6** — The scenario successor chains need no code here: `tools/loop/scenario.py#check_scenarios`
  already reports each cycle of the composed scenarios' `then` edges once, through the same `scan_cycles`,
  and its `then-cycle` plant runs under the leg `loop scenario fixtures` (`TOOL-dDeclaredLoop-27`).
  NOT OBSERVED — this unit builds nothing for it.
- **S7** — Rule `raise`: every `rescope · flow-state` row of a build reading `applied · class loosening`
  names the owner's release, ` · disposition <stem>`; one that names none is a loosening applied
  unattended, a finding naming its row tag. `held` and `refused` rows pass. A raise of a loop-bound field
  of a row reaches the record only as such a loosening (`tools/loop/adapt.py#derive_change_class`), and
  a raise of `flow.rework-budget`, `review.max-rounds` or `roles.retries` is a policy-file write, which
  is the guard's (§3, §8 F7). Observed by AC7.
- **S8** — `deadline` and `on-deadline` are fixed fields of the item kind until a numeric direction lands:
  their `[[field]]` rows in `tools/loop/item-schema.toml` declare no `widens`, so every overlay or flow
  patch of either is refused by the composition, naming the field (§8 F8, F9). `draws` and `waits` are
  fixed the same way, so a repository row sets its own and never patches gov's. Observed by AC8.
- **S9** — Rule `decline`: every `rescope · flow-state` row reading `held · class loosening` recommends the
  decline; one recommending anything else, or nothing, is a finding. `tools/loop/adapt.py#render_state_row`
  writes ` · recommend decline` after the mode on every such row, and `tools/loop/adapt.py#STATE_ROW`
  reads the field as an optional group, ahead of the disposition. Observed by AC9.
- **S10** — The push. A leg `loop termination` in `tools/gate-legs.json` runs `python
  {prefix}/loop/termination.py check --selftest`, which checks gov's composition and every live build's,
  then runs every plant; it declares no `guard` (§8 F10), carries `chunk = "selftests"`, `subject =
  "repo"`, `enforces = ["principle.p39"]` and `stage = ["step.test"]`, and is gov's own `[[exempt_leg]]`
  in `tools/govkit/registry.toml`, as `loop budget fixtures` is. A live build is a slug a
  `Gov-Transition` trailer reachable from HEAD or a transition log record names, whose newest move is
  into no terminal. Observed by AC10.
- **S11** — The step boundary. `tools/loop/loop_transition.py#write_transition`, after
  `tools/loop/adapt.py#write_flow_states` writes a state row reading `applied`, runs `check_termination`
  on the build's composition at HEAD with its scenarios and its applied changes, and refuses the move on
  a finding, naming it, inside the span whose refusal cuts `RUN.md` back to its length, so nothing is
  recorded. Observed by AC11.
- **S12** — The waits outside the composition, named. `tools/loop/README.md` gains a section listing
  the code-level waits the check does not grade, each with its declared deadline: the lander's wait on
  a claim lock, `tools/push-main.sh#CLAIM_WAIT_CEILING`. Observed by AC12.
- **S13** — The plants the `New arm:` line in §7 declares, one per planted break, run by `check
  --selftest` and one at a time by `--fixture --plant <case>`. Observed by AC1 to AC5, AC7 to AC9 and
  AC11 through that line, RED first at the close.

## 3. Non-goals (OUT)

- The tables, items, stages, scenarios and flow changes the check reads: `TOOL-dDeclaredLoop-13`, `-12`,
  `-24`, `-25`, `-27` and `-28`'s. The check reads the composition and refuses on it. It writes the
  four new item fields on gov's own rows, the pending list and the one field S9 names, and nothing else
  of theirs.
- The budget and the endings: `TOOL-dDeclaredLoop-30` and `-31`'s. The check reads `CAUSES`, the
  writer's backward draw and the ending rows, which make a counted edge and an ending.
- The feature and unit tables' cycles: the clause names the build table and the item routes, and a unit
  or feature move back mirrors a build route back the build table already counts.
- A run-time detector. Progress, leases and the wait graph across builds are dWellOiledMachine's
  (`TOOL-dWellOiledMachine-50`); this is the static half.
- Nested spawns drawing from a parent's reservation, which stall-and-loop.md:241 lists beside these rules:
  the clause does not name it, and the reservation is a later build's.
- A raise of `flow.rework-budget`, `review.max-rounds`, `roles.retries` or `flow.wait-ceiling` in the
  policy file: `tools/loop/guard.py#check_staged` grades every agent write of it, admitting a live run's
  branch by the owner's 2026-11-12 ruling, and `tools/loop/guard.py#check_push_range` owes each changed
  leaf its record and trailer. No flow change carries a policy value (§8 F7).
- The widening join: it needs the numeric direction §8 F4 asked for, which no build provides (F8, F9).
- Re-pointing `tools/push-main.sh#CLAIM_WAIT_CEILING`, a wait with a declared deadline already, or
  `tools/unattended/unattended.sh#WIRING_CEILING` and `#PREFLIGHT_CEILING`, which bound a process.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-12` — `needs`: `scan_cycles`, the helper's inline copy in `tools/loop/loop_lib.py`, which the counted rule calls, and the needs graph and routes the reachable rule walks
- **consumes-from** `TOOL-dDeclaredLoop-27` — `scenario`: `read_scenario_rows` and `read_activated_rows`, the scenario rows a build's composition holds; its own `check_scenarios` grades the successor chains
- **consumes-from** `TOOL-dDeclaredLoop-28` — `flow.adapt`: the flow and state rows `read_flow_rows` reads, `read_flow_layer`, and `write_flow_states`, after which the step boundary runs the check
- **consumes-from** `TOOL-dDeclaredLoop-30` — `flow.rework-budget`: `CAUSES`, the words a counted route names, and the writer's `route-back` draw that makes a build row counted
- **consumes-from** `TOOL-dDeclaredLoop-31` — `flow.on-exhausted`: the ending rows E1 to E5 and their `draws = "none"`, set aside as endings
- **hands-off** `TOOL-dDeclaredLoop-54` — the terminal set per level, which that unit declares and the terminal rule reads; until then the feature and unit levels print unchecked (the round-1 spec audit's id 5)
- **hands-off** `TOOL-dDeclaredLoop-55` — the termination leg's guard: the row lands with none, so that unit's S1 holds at this landing (§8 F10, the round-1 spec audit's id 55)
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 26, 39, 58, each a scope item of that unit
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 2 and 46: AC10's guard clause is superseded by unit 55's guard-free row, and the no-guard property gets its lasting arm there
- **hands-off** external — the numeric direction §8 F4 asked for, filed in this build's `BACKLOG.md` by the run (§8 F9), and the widening join that waits on it

## 4. Design

### The rules

| Rule | Reads | Finding |
|---|---|---|
| `terminal` | each level's states, rows and declared terminal set | a state with no path to a terminal; an empty state set |
| `reachable` | every program's entries and items, every route, each need within one program | an item the walk from every entry does not reach |
| `counted` | the build table and the item routes, less the set-aside edges | a cycle, once, rotated to its smallest member |
| `wait` | each item with `waits` or an owner actor, the pending list | no `deadline` or `on-deadline`; a deadline of the wrong type; a stale pending row |
| `raise` | the build's state rows | an `applied · class loosening` row naming no disposition |
| `decline` | the build's state rows | a `held · class loosening` row not recommending `decline` |

Each rule is one function, `check_<rule>(composition)`, so a plant that breaks one rule reds that rule
alone. The planted repository stage that routes back into itself with an exit passes `terminal` and
`reachable` and is caught only by `counted`, which is the clause's discriminating case
(stall-and-loop.md:146-148, P5). `raise` and `decline` read a build's rows, so over gov's composition
alone they grade nothing and print `0 build(s)`, never a pass.

### The edges

```
build row r, from s to t (each `@open` from expanded, `@prior` and `@reentry` to read as dynamic):
  ending   r.outcome in loop_table.ENDING_OUTCOMES          # fires only on a spent budget (unit 31)
  dynamic  r.to in ("@prior", "@reentry")                   # a resume, a park's continue, a re-entry
  owner    the actor of r.item is owner or owner:<name>
  counted  derive_direction(s, t) == "backward" and r.draws != "none"   # write_transition draws route-back
item route a --o--> b, b a declared item:
  counted  a.draws[o] in budget.CAUSES; or b is another step's, and the build row it fires is counted
  owner    a's actor is owner or owner:<name>
  wait     o in a.waits and a == b
check_counted: graph = every edge none of these; scan_cycles(graph); one finding per cycle
```

A counted edge draws on a budget that ends at `flow.on-exhausted`; an ending fires only on a spent
budget and ends the build or descopes a unit; a dynamic return and an owner edge wait on the owner or a
new request; a declared wait is bounded by the deadline the `wait` rule grades. `scan_cycles` rotates
each cycle to its smallest member, so one cycle found from three entries is one finding.

### Gov's own cycles at landing

Gov's composition must exit 0 at landing (AC10), so each cycle of gov's own rows gets its bound by these
rules, in order, recorded per cycle in the acceptance ledger:

1. A route of an item to itself on which the item waits on another party is a wait: the item lists the
   outcome in `waits` and declares `deadline = "policy.flow.wait-ceiling"` and an `on-deadline`.
2. A route into a repetition whose draw site exists names, in `draws`, the cause that site draws. A
   route into an item the unattended driver dispatches again as the same unit's pass, an item whose
   actor is `role:gov-builder`, names `fix-pass` (`verb_dispatch`'s draw in
   `tools/unattended/unattended.sh`, where the unit's earlier pass committed). `item.review.fold`'s
   `next-round` route into `item.review.trigger` names `review-round`, which
   `tools/unattended/unattended.sh#verb_review` draws on every round of a subject after its first
   (`tools/loop/loop.toml@44ea9acb:1935`). That route bounds unit 50's cycle `item.review.dispose ->
   item.review.fold -> item.review.trigger -> item.review.pin -> item.review.report`.
3. Every other cycle, of the build table or the item routes, is a `cycle` row of the pending list naming
   the owner of the item whose row or route re-enters it, by its `[[item]]` or `[[stand-in]]` row, the
   build that declares its bound when it lands that item. Unit 50's cycle `item.review.dispose ->
   item.review.fold` is one: `item.review.fold`'s `at-bound` route re-enters `item.review.dispose` and
   no site draws on it, so its row names `dDeclaredLoop`, the owner of `item.review.fold`'s row.
4. An item with an owner actor is a `wait` row naming `run.owner-deadline` and dWellOiledMachine.

Measured over gov's `[[item]]` rows at the branch tip `e8018d94f` by `scan_cycles` over every route
between declared items: 23 cycles over 45 edges, PINNED on 2026-11-16 at that tip. The count was 21
over 39 at `250b236f`, and the two added are unit 50's review cycles that rules 2 and 3 name above.
Rule 1 covers four items, `item.build.unit-lease` on `waiting`, `item.deploy.core` on `running`,
`item.deploy.land` on `unreachable` and `item.deploy.parents` on `held` and `moved`. Units 52 and 53,
beside this unit at order 34, may land rows, so the population is re-derived at the builder's base by
the module's own `check` before rule 1 to 4 are applied, never read off this paragraph.

Over the same rows the `reachable` rule prints no finding, PINNED on 2026-11-16 at `e8018d94f` and
re-derived by the same `check` at the builder's base. `item.build.resolve` needs only
`item.test.merge` (`tools/loop/loop.toml@44ea9acb:1567`) and is reached through that item's
`conflict` route (`tools/loop/loop.toml@44ea9acb:1589`), which the walk follows across programs. No
pending row is owed for reachability.

### The pending list

```
# tools/loop/termination-pending.txt — shrink-only
wait · <item tag> · <deadline key> · <build that lands it>
cycle · <tag> -> <tag> -> ... · <owner build of the re-entering item>
```

A `wait` row is stale once `derive_landed_owners` reads its build landed, or once its item declares its
deadline or is gone. A `cycle` row is stale once the graph `check_counted` builds no longer holds that
cycle. A stale row is a finding, so the list only shrinks, and the check prints both counts on every run.

### Data model

```
composition = {
  "label":    "gov" | "<slug>@<pin8>",
  "states":   {level: [state]}, "terminal": {level: [state]},       # build only, until unit 54
  "rows":     the spliced build rows, the feature rows, the unit rows,
  "items":    [composed item row], "programs": {program: [item tag]},
  "flow":     read_flow_rows(root, build) | [],                     # raise and decline
  "pending":  [{"kind", "subject", "key", "build"}],
}
[[item]] fields, each optional, each fixed in item-schema.toml:
  draws        { <outcome> = "<cause of CAUSES>" }
  waits        [<outcome>]
  deadline     <whole hours> | "policy.<key>"
  on-deadline  <outcome of its set outside waits>
state row      ... · flow.adapt <value>[ · recommend <option>][ · disposition <stem>]
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_termination`, `check_terminal`, `check_reachable`, `check_counted`, `check_wait`, `check_raise`, `check_decline` | Python functions, `tools/loop/termination.py` | `py.function`, verb-first, each `OK` by `--suggest` |
| `read_termination_inputs`, `read_termination_pending` | Python functions, `tools/loop/termination.py` | `py.function`, `OK` |
| `read_build_items` | Python function, `tools/loop/position.py` | `py.function`, `OK` |
| `tools/loop/termination-pending.txt` | shrink-only list | none |
| `draws`, `waits`, `deadline`, `on-deadline` | item fields | none |
| `recommend` | state row field, `decline` on a held loosening | none |
| `loop termination` | gate leg | leg name |

### Migration

None. The four item fields are optional and additive, an adopter row without them reads as before, and
no upgrade step is owed. A composition the check reds is one no build could finish.

### Rollout

The leg lands with the check. Gov's own composition must be green at landing, every gov cycle bounded by
§4 "Gov's own cycles at landing", which AC10 observes.

### Files touched (estimate)

- `tools/loop/termination.py`
- `tools/loop/termination-pending.txt`
- `tools/loop/loop.toml`
- `tools/loop/item-schema.toml`
- `tools/loop/adapt.py`
- `tools/loop/loop_transition.py`
- `tools/loop/position.py`
- `tools/loop/kit.toml`, the module's comment paragraph, its leg gov's own `[[exempt_leg]]`
- `tools/loop/README.md`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`
- `tools/govkit/usage.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/selftest-budgets.txt`
- `help/loop.md`
- `memory/map/features/loop.md`
- `memory/map/generated/`, rendered, never typed
- `memory/guides/SESSION-KICKOFF.md`, its `last-audit` re-stamp, since `tools/gate-legs.json` is on its `watch:` line

### Alternatives rejected

- **Soundness alone: every state reaches a terminal and every item is reachable.** A planted stage with an
  exit passed it while its uncounted self-loop survived (P5).
- **Default a wait with no deadline to `flow.wait-ceiling`.** The clause requires each wait to declare one;
  a silent default makes a forgotten deadline indistinguishable from a chosen one.
- **A third cycle primitive here.** `scan_cycles` is the one helper; this unit builds the graph it is
  handed and the reachability walk beside it.
- **Copying the build's item composition out of `derive_position_into`.** It is the second reader of the
  same composition, so `read_build_items` is extracted and both call it.

## 5. Production-readiness checklist

- security — read-only over composed rows; its writes are the item fields on gov's rows, the pending
  list and the one state row field S9 names. The new item fields are fixed, deny by default, so no
  overlay or flow change patches gov's bound.
- perf / scale — each rule is linear in rows and edges; the push composes gov's once and each live
  build's at its pin, a scratch worktree per pin not HEAD; live builds number 0 PINNED at `250b236f` on
  2026-11-16 (`git log --grep=Gov-Transition:` prints none). The step boundary composes only on a move
  that applies a change. The leg's ceiling is 300 PINNED; its budget row is a proxy of each plant alone.
- error / empty / loading states — an empty state set is a finding; a level with no terminal set prints
  unchecked; an unreadable composition or an unresolved kit exits 2 naming the reader's refusal, never 0.
- observability — each finding names its rule and row; the pending counts and the ceiling print.
- risks — the check trusts `draws` and `waits` as declared, so a false mark hides a loop; the ledger's
  per-cycle line is what a reviewer reads. A loop through a dynamic return or an ending is bounded by
  the owner or `flow.on-exhausted`, not by this check.
- testing — the pass probes each `check_<rule>` on a plant; the main loop observes §7's arm RED, GREEN.
- migration — none.
- user docs — `help/loop.md` gains a section on the check, its verbs anchored, and its "Each step's
  program" names the four item fields; `tools/loop/README.md` gains the module's section and S12.

### The sweep: what the change reaches, and what keeps each green

Read on `branch/unattended-declared-loop-d56bf0` at `250b236f`, extracted by `git archive`; the
lexicon ran on this worktree's main at `179486e8`.

| Reached | Readers and populations | What keeps it green |
|---|---|---|
| `render_state_row`, `STATE_ROW` | writer `write_flow_states`; reader `read_flow_rows`, and through it `read_pending_rows` and `read_flow_layer`; `grep -rn "flow-state" tools skills` names `tools/loop/adapt.py` alone | the group is optional, before `disposition`, so every landed row reads; the `loosening` plant expects it; `help/loop.md`'s row grammar gains it |
| `write_transition` | the `record` verb, `budget.py`'s plants, the driver through `record` | the call runs only after an `applied` row; `adapt.py`'s `additive`, `owner-approves` and `loosening` plants compose gov's green composition; `loop adapt fixtures`' budget row, 225 PINNED, is re-read |
| `derive_position_into` | `derive_position`, `write_path_orders`, the driver through `position.py` | `read_build_items` holds the same lines |
| gov's `[[item]]` rows | `check_program`, which reads no unknown key; `read_composed_items`; `splice.py`; `upstream.py` | each new key is optional; the rows' pins move, and the plants amending a gov row compute the pin live (`adapt.py`'s `act-mismatch`, `scenario.py`'s `write_scenario_plant`); `.governance/instructions.toml` holds no `[[item]]` |
| `item-schema.toml` | `read_kind_schema`, `check_rows`, `loop_items.py check` | four `[[field]]` rows, no `widens`; no `[[fixed-row]]` moves |
| the new leg | `run-gates canary`, `run-gates gov canary`, `measure-legs selftest`, `govkit selfcheck`, `govkit selftest`, `policy fixtures`, `codebase-map coverage + freshness`, `help page commands`, `kickoff-manifest ratchet` | its `[[exempt_leg]]` row; `subject-pins.tsv` row `loop termination`, `repo`, `selftests`; its budget row; `usage.toml` rows `script:{prefix}/loop/termination.py` and `#check` with their help anchors; the dossier's `gate-legs` claim; the rendered map; the manifest re-stamp |
| `principle.p39` | `tools/playbook/core-pending.txt` | graded live already, `loop budget fixtures` enforcing it |
| `VERB_OFFENDER_PIN` | `lexicon naming predicates` | the eleven names each `OK` by `--suggest <name> --as py.function` on 2026-11-16 |
| the refusal census and families | `REFUSAL_CEILINGS`, `ARMS_FLOORS`, `tools/unattended/unattended.families.txt`, `tools/memory-tree/check-arms.py` | no shell script is edited; `git diff --name-only <base>.. -- '*.sh'` prints nothing |
| `SHARED_RECORDS` | `memory/DECISIONS.md`, the readme contract | no decision row is owed: no census or ceiling moves |
| the verdict-epoch `DELEGATES` | `tools/memory-tree/check-verdict-epoch.sh` | the memory-tree modules it lists are not edited |
| reader coverage | `check_reader_coverage` over `flow.wait-ceiling` | `termination.py`'s literal `resolve` call |
| the install-prefix ban | `check-install-prefix.sh` | the kit's files spell `<prefix>` or `{prefix}`, never the tool root |

Rev-7 re-read what its change reaches at `e8018d94f`: gov's `[[item]]` rows, the review program's among
them, `tools/loop/loop_lib.py#check_program`, `tools/loop/position.py#derive_next_item`,
`tools/loop/budget.py#CAUSES` and `tools/unattended/unattended.sh#verb_review`. Outside
`tools/loop/loop.toml`, `item.review.fold` is named only in prompt text, in
`tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js` and that
workflow's test, none of which reads a row field, so its `draws` reaches no reader the table lacks. The walk S3 gives reads the rows `check_program` already
grades and adds no reader.

Sibling code this spec is written on: units 50, 19 and 51 landed by `e8018d94f`, unit 50's review
program adding the two cycles §4 bounds; units 52 and 53 beside this one at order 34, unit 52
INPROGRESS and unit 53 DEFERRED at `a737706a7`, either of which may edit `tools/loop/loop.toml`. The builder re-derives gov's cycles and the
reachable walk at its base (§4).

## 6. Acceptance criteria

- **AC1** — When `python termination.py --fixture --plant stage-self-loop` runs a planted
  composition holding a repository stage whose exit item routes `pass` to `transition` and `retry` back
  to the stage's first item with no `draws`, it prints one finding, rule `counted`, naming that cycle,
  and no `terminal` or `reachable` finding; with `--plant stage-self-loop-drawn`, the same route under
  `draws = { retry = "route-back" }`, it holds.
  Red when: the counted-edge rule is absent, so the planted stage passes on soundness alone.
- **AC2** — When `--plant dead-end` plants a build state no row leaves, the check prints a `terminal`
  finding naming the state, and the feature and unit levels each print `unchecked — no terminal set`.
  Red when: reachability is computed forward from the entry, so a dead-end state still passes.
- **AC3** — When `--plant orphan-item` adds to gov's composition an item of the build program whose one
  need is `item.test.merge` and which no route names, the check prints one `reachable` finding, naming
  that item, and none naming `item.build.resolve`, which holds the same need and which
  `item.test.merge`'s `conflict` route names.
  Red when: the walk follows a need across programs, so the orphan is reached through
  `item.test.merge`, as every item then is.
- **AC4** — When `--plant empty-states` plants a build level declaring no states, the plant prints a
  `terminal` finding naming the empty set and its exit as 1.
  Red when: an empty table passes because no state fails.
- **AC5** — When `--plant wait-no-deadline` plants an item whose `waits` holds `waiting` and that declares
  no `deadline`, the check prints a `wait` finding; `wait-declared`, with `deadline =
  "policy.flow.wait-ceiling"` and `on-deadline = "refused"`, holds; `wait-stale` plants a pending row
  whose build the planted landed set names and prints a stale finding.
  Red when: a wait with no deadline passes.
- **AC7** — When `--plant raise-unattended` plants a build's state row `applied · class loosening ·
  flow.adapt additive-recorded` naming no disposition, the check prints one `raise` finding naming its
  tag; `raise-released`, the row with ` · disposition <stem>`, and `raise-held`, the row reading
  `held`, each hold.
  Red when: an applied loosening passes because only its class is read.
- **AC8** — When `--plant deadline-patch` runs `tools/loop/loop_items.py check` in a scratch repository
  whose overlay amends `item.build.unit-lease`'s `deadline` to `96`, it exits 1 naming the field
  `deadline` as fixed.
  Red when: the field declares a `widens`, so the raise composes.
- **AC9** — When `--plant decline` plants a held loosening recommending `apply`, the check prints a
  `decline` finding; one recommending `decline` holds; one with no recommendation prints the finding.
  When `python tools/loop/adapt.py --fixture --plant loosening` runs, the held state row it checks in
  the scratch `RUN.md` ends `· recommend decline`.
  Red when: a held loosening with no recommendation passes.
- **AC10** — When a probe loads `tools/gate-legs.json` with `json.load`, it finds one row named `loop
  termination` whose argv runs `termination.py check --selftest`, carrying no `guard` key, `enforces`
  holding `principle.p39` and `stage` holding `step.test`; and `python termination.py check` over
  this repository's composition exits 0 and prints both pending counts.
  Red when: gov's own composition reds at landing, on a gov cycle with no bound or on an item such as
  `item.build.resolve` that only another program's route reaches.
- **AC11** — When `--plant boundary` records a forward move in a scratch repository whose build holds an
  additive flow change adding an item that routes back into itself with no `draws`, the move is refused
  naming the `counted` finding and `RUN.md` keeps its length; without the change the move records.
  Red when: the step boundary moves without calling the check.
  cost: a scratch repository and two composition reads, tens of seconds.
- **AC12** — When `grep -c 'CLAIM_WAIT_CEILING'` runs over `tools/loop/README.md`, it prints at least 1.
  Red when: the code-level wait is not named, so a reader takes the check to grade it.

## 7. Gates

`loop definition` · `loop item kind` · `loop transition tables` · `loop adapt fixtures` · `loop transition record` · `loop position fixtures` · `loop budget fixtures` · `loop splice check` · `loop upstream fixtures` · `loop scenario fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `policy check` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `help page commands` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/termination.py · covers AC1 AC2 AC3 AC4 AC5 AC7 AC8 AC9 AC11 · one plant per rule and per break, each in memory but deadline-patch and boundary, which build a scratch repository; the module is absent at base · none

## 8. Open questions

- **F1 — How does the check tell a counted edge, when no row field marks one today?** Options: (a) the row's
  `draws` field naming one of I19's causes, which `TOOL-dDeclaredLoop-31`'s rows already carry as `none`;
  (b) a separate `counted = true` flag. (b) is a second fact beside the draw cause it restates. RESOLVED
  (agent, 2026-10-24, delegated): (a), rung 3.
- **F2 — What does a wait whose deadline key has not landed do?** Options: (a) a shrink-only pending row
  naming the build that lands the key, the house pattern of dOrderedCharter-7 S3's pending list; (b) a red on
  gov's own composition until that build lands; (c) default it to `flow.wait-ceiling`. (b) reds every push
  between now and that landing; (c) is the silent default §4 rejects. RESOLVED (agent, 2026-10-24,
  delegated): (a), rung 3.
- **F3 — Where does "the approval item's recommendation" live?** Options: (a) a ` · recommend <option>` field
  on `TOOL-dDeclaredLoop-28`'s `rescope · flow-state` row, written `decline` for a held loosening; (b) the
  owner item's text. (b) is prose no check can read. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.
  grants: PLAY-dClosedLoop-3 the loop termination gate leg, the deadline, on-deadline and recommend fields and the termination-pending list
- **F4 — Which direction does a loop-bound field declare?** dOrderedCharter-36 S5 offers `add` and
  `remove` on a set and an ordered list of values on a scalar, and refuses an open field with no
  declared direction; none of the three orders an unbounded number. Options: (a) each such field
  declares `widens` an ordered list of its admitted values, smallest first, in its kind's schema
  (`TOOL-dDeclaredLoop-24`'s `tools/loop/item-schema.toml` for `deadline`), a value off the list
  refused; (b) an ask to dOrderedCharter for a numeric direction on a scalar, such as `widens = "raise"`
  over numbers and durations, a policy-tag value compared at its value; (c) every such field left
  undeclared, so fixed (dOrderedCharter-36 S2) and every patch of one refused. (a) closes each field to
  a typed list and cannot place a policy-tag deadline such as `policy.flow.wait-ceiling`, the value
  gov's own waits declare (S5), among numbers. (c) refuses the raise the clause has the update report
  name as a widening. Recommendation: (b), the one form that orders the values these fields hold.
  RESOLVED (owner, 2026-11-05): (b) a numeric direction asked of dOrderedCharter. The build run files
  in dOrderedCharter's `BACKLOG.md` the ask for that direction on dOrderedCharter-36 S1 and S5.
- **F5 — How does a build row read counted, when `TOOL-dDeclaredLoop-31` admits `draws = "none"` alone?**
  At the tip, `tools/loop/loop_transition.py#write_transition` draws `route-back` on every move
  `tools/loop/loop_table.py#derive_direction` reads backward unless its row reads `draws = "none"`, and
  no check reads another value. Options: (a) derived: counted where the direction is backward and the
  row does not read `draws = "none"`, the moves the writer draws on, with endings, dynamic returns and
  owner rows set aside as §4 "The edges" gives; (b) every backward row typed `draws = "route-back"`.
  (b) is a second fact beside the derived direction, and a row typed wrong would pass while the writer
  drew otherwise. F1's field stays the marker on item routes, which have no direction. Measured at the
  tip, (a) leaves one build cycle, `paused` re-entered by B19's pause from `@open`, whose item is
  dWellOiledMachine's stand-in, a `cycle` row by §4's rule 3. Recommendation (a); the body is written on it.
- **F6 — How do gov's own item-route cycles pass the counted rule at landing?** 23 cycles PINNED at
  `e8018d94f` on 2026-11-16: waits on a lease, the remote and a parent, fix passes, review rounds, and
  design, test and disposal loops no draw site records. Options: (a) §4 "Gov's own cycles at
  landing"'s four rules; (b) every
  cycle a pending row; (c) the item routes left out of the rule. (b) leaves the waits this unit's key
  bounds unbounded and the fix-pass loops pending though their draw site exists. (c) cannot catch the
  clause's discriminating case. Recommendation (a); the spec body is written on it.
- **F7 — Where can a build raise the budget, a round count or a retry count?** The clause plants an
  unattended raise of each. At the tip a build's recorded changes are row changes of a composed kind
  (`tools/loop/adapt.py#write_flow_proposal`), no row kind holds one of those three counts, and an agent's
  write to the policy file is graded by `tools/loop/guard.py#check_staged`, which admits a live run's
  branch by the owner's 2026-11-12 ruling, each changed leaf owing its change record and trailer.
  Options: (a) the `raise` rule grades the record's applied loosenings, the deadline an item field that
  lands fixed (S8), the three policy populations left to the guard (§3); (b) a flow change carrying a
  policy value, a second write path into the guarded file and another unit's mechanism. Under (a) a
  run's raise on its own branch is the guard's admission, recorded but not held for the owner, a
  departure from the clause's three policy plants the run records. Recommendation (a); the body is
  written on it.
- **FACT-QUESTION · F8 — Is F4's ask filed, and does the classifier order a number?** Probe: `git grep -n
  -i "numeric" branch/unattended-declared-loop-d56bf0 -- memory/builds/dOrderedCharter/BACKLOG.md` and
  `tools/playbook/row_checks.py#derive_patch_class`, read at `250b236f`. Observation, 2026-11-16: the
  grep prints nothing; dOrderedCharter's README reads `CLOSED`; and `derive_patch_class` reads `add` or
  `remove` on a set and a listed value on a scalar, refusing any value off its order. Liveness: the grep
  finds the ask once filed, and `derive_patch_class` gains a numeric branch once it lands. RESOLVED
  (agent, 2026-11-16, delegated): neither holds.
- **F9 — With the direction unlanded, what does this unit build of S8?** Options: (a) `deadline` and
  `on-deadline` land fixed, so every patch of either is refused, and the widening join waits on F4's ask,
  which the run files in this build's `BACKLOG.md` as it filed `TOOL-dDeclaredLoop-113` for unit 34's:
  "a numeric direction on a scalar field, `widens = "raise"` over whole numbers and durations, a
  policy-tag value compared at its value, in `tools/playbook/row_checks.py#derive_patch_class`, so a raise
  of an item's `deadline` composes held as a loosening and is listed by `derive_widenings`"; (b) the
  whole unit deferred against that ask, as unit 34 is; (c) F4's (a), which the owner declined. (a) is
  deny by default, stricter than the clause until the pick lands; (b) holds every rule and units 54
  and 55 behind one join. Recommendation (a); the spec body is written on it.
- **F10 — Does the leg declare a guard?** No `loop` leg at the tip declares one, and
  `TOOL-dDeclaredLoop-55` S1 rules this one carries none, since `{prefix}/loop/` misses the overlay, the
  scenarios and a build's changes. Options: (a) no `guard`, that unit's S1 holding at this landing; (b)
  guarded, that unit taking the key away one order later, a leg that meanwhile skips what it grades.
  Recommendation (a); the spec body is written on it.
- **F11 — How does the terminal rule read the feature and unit levels before `TOOL-dDeclaredLoop-54`
  declares their sets?** Options: (a) it walks each level that declares a set and prints the others
  unchecked, never a pass; (b) it walks them toward the build's terminals, every feature and unit state a
  finding, so gov's composition reds at landing; (c) this unit declares the sets, that unit's S1. (c)
  moves a sibling's scope. Recommendation (a); the spec body is written on it.
- **F12 — How does the reachable rule count an item that only another program reaches?**
  `item.build.resolve`, of the build program, needs only `item.test.merge`, a test item, and only that
  item's `conflict` route names it (`tools/loop/loop.toml@44ea9acb:1567` and `:1589`). Inside its own
  step that need is met only by a recorded move naming `item.test.merge`
  (`tools/loop/position.py#derive_next_item`). Rev-6's walk from each program's own entry, along every
  route and every need, leaves it unreached, so gov's composition reds and AC10 cannot hold, as the
  builder return 2026-11-16-build-TOOL-dDeclaredLoop-33-1-builder-return measured. Options: (a) one walk
  from every program's entries grading each program's items, following a route across programs and a
  need only between two items of one program, with AC3's orphan rebuilt as a build item needing
  `item.test.merge` that no route names; (b) rev-6's walk, with `item.build.resolve` and any item like
  it carrying a declared bound, a `reach` row as a third kind of the pending list. Measured at
  `e8018d94f` on 2026-11-16 over gov's rows, bare and with that orphan added: (a) prints nothing on gov
  and the orphan alone on the plant; (b) prints nothing on gov beside one pending row, and the orphan
  on the plant. Following every need across programs under (a), or counting an item whose needs all
  leave its program as an entry, prints nothing on either: every item's needs lead back to some entry,
  so the rule could never red. (b) adds a pending kind and its staleness rule for a row no build
  retires, since the route from the test program is `item.build.resolve`'s design, and a standing
  exemption read as coverage. RESOLVED (agent, 2026-11-16, delegated): (a), the smallest change that
  keeps the rule able to red; S3, AC3, AC10 and §4 are written on it.

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 33, stall-and-loop.md:146-148 and :236-245,
  dGroundRules-11's bound population, dOrderedCharter-36's widening list, and the two cycle primitives and
  the push wait read at base `ed497191`.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-54, a hands-off TOOL-dDeclaredLoop-55, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-25 · S1 S8 · §4 The rules · §8 F4 · re-grounded on dOrderedCharter's specs at
  `462d20f35` per `build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md` rows 112
  and 114: `check --build` composes through TOOL-dDeclaredLoop-26's `compose_at` at the build's pin
  (its §8 F4); a loop-bound field's widening direction is F4 here, open for the owner, since unit 36
  S5 orders no unbounded number.
- rev-5 · 2026-11-05 · S8 · §8 F4 · the owner resolved F4 to (b), the numeric direction ask, per the
  brief `2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks`; S8 names the direction.
- rev-6 · 2026-11-16 · §1 · S1 · S2 · S3 · S4 · S5 · S6 · S7 · S8 · S9 · S10 · S11 · S12 · S13 · §3 · §4 ·
  §5 · AC1 · AC2 · AC3 · AC4 · AC5 · AC6 · AC7 · AC8 · AC9 · AC10 · AC11 · §7 · §8 F5 F6 F7 F8 F9 F10 F11 ·
  §10 · re-grounded at the tip of branch/unattended-declared-loop-d56bf0 (`250b236f`), per the brief
  prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-33-1-spec-writer.md: symbol citations; the landed
  composition readers and `read_build_items`; `scan_cycles`; F5 to F11; S6 and AC6 out, built by unit
  27; the help page that now exists; §5's sweep.
- rev-7 · 2026-11-16 · S3 · §4 · §5 · AC3 · AC10 · §8 F6 F12 · per the builder return
  2026-11-16-build-TOOL-dDeclaredLoop-33-1-builder-return: the reachable walk starts from every
  program's entry and follows a need only within one program (F12), so `item.build.resolve` holds and
  AC3's orphan still reds; gov's cycles re-pinned at 23 at `e8018d94f`, unit 50's two review cycles
  bounded by §4's rules 2 and 3.

## 10. Reuse audit

The seams: `scan_cycles` (`tools/lib/needs_graph.py#scan_cycles`, inline in `tools/loop/loop_lib.py`),
which the counted rule calls over the graph it builds; `check_program`'s programs and
`read_transition_rows`' tables, which the reachable and terminal rules walk; the position engine's item
composition, extracted as `read_build_items` at its second reader; `derive_bounds` and
`derive_landed_owners` in the policy kit; and the pending-list shape of dOrderedCharter-7's. For the
counted-edge rule itself no existing seam fits: `grep -rn -i -E "def [a-z_]*cycle|tarjan|def
[a-z_]*reachab" tools` over the tip's tree finds `scan_cycles` in its four copies and
`check_truth_reachable` in `tools/codebase-map/replay-phrases.py`, none reading counted or owner edges
or a terminal, and `loop_table.py`'s docstring lists "reachability, termination and counted edges" under
what it does not check.

`python tools/codebase-map/reuse_lookup.py "check that every state of a transition table reaches a
terminal and every cycle passes a counted edge"`, run on this worktree's main, ranked `check`, `counts`
and `check_line` by name stem; none walks a graph. `python tools/memory-recall/query.py "does anything
check that a flow terminates and every loop is counted"` with the terms below returned the scout
record's row for this unit and this spec, none a check.

Recall terms used: termination counted edge scan_cycles derive_direction draws route-back flow.wait-ceiling termination-pending check_program reachable terminal
