# TOOL-dDeclaredLoop-13 — one transition table per level, the engine refusing a move it lacks

**Status:** CLOSED · rev-4 · 2026-11-14 · node d · Tier-2 · base ed497191 · streams tooling · order 10 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0098@89542705 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-05-build-TOOL-dDeclaredLoop-13-deviation-131.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-13-deviation-131.md) | deviation | — |
| [2026-11-14-build-TOOL-dDeclaredLoop-13-1-acceptance-ledger.md](../build/2026-11-14-build-TOOL-dDeclaredLoop-13-1-acceptance-ledger.md) | journal | — |
| [2026-11-14-build-TOOL-dDeclaredLoop-13-deviation-132.md](../build/2026-11-14-build-TOOL-dDeclaredLoop-13-deviation-132.md) | deviation | — |
| [2026-11-14-build-TOOL-dDeclaredLoop-13-red-fix-13.md](../build/2026-11-14-build-TOOL-dDeclaredLoop-13-red-fix-13.md) | red-fix | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-56 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md) | research | TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-13-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-13-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-13-build-brief.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-13-build-brief.md) | journal | — |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-13-reground-brief.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-13-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

The loop definition declares one transition table per level (build, feature, unit), and one engine
answers every proposed move from those rows alone. A move no row holds is refused. Each row names, by
its `item.<step>.<name>` tag, the item and the outcome that fire it. An item whose owning build has not
landed is a declared stand-in with a fixture witness, until that build lands and arms it (C2-F8,
`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-walk-return-c2.md:100-109`).
Today every cross-step route is declared on the `[[item]]` rows `TOOL-dDeclaredLoop-12` landed, as
`transition` or as an item of another step, and no table answers any of them. The only move record is
unattended's linear phase vocabulary, checked by membership alone
(`tools/unattended/unattended.sh#verb_phase`), and no feature or unit table exists (`gap-flow-15`).

## 2. Scope (IN)

- **S1** — The three tables, as `[[transition]]` rows of `tools/loop/loop.toml` (I1), each carrying
  `level`, `from`, `item`, `outcome`, `to` and `witness`, and optionally `disposition` and `when`
  (§4 "### Data model"). The new tables sit after the `[[checklist]]` rows and before the first
  `[[item]]` row, as the file's header asks of every table, so each item row's span, which the tag
  index reads up to the next header, keeps its bytes. Observed by AC1.
- **S2** — The states of each level in a `[states]` table of the same file: the build's open states
  `planning`, `designing`, `building`, `testing`, `deploying`, `paused` and `parked` (I3), and the
  feature's and the unit's states. Each step's state and exit item stay on
  `TOOL-dDeclaredLoop-1`'s `[[step]]` rows, read through `read_steps`. The terminal set is
  `TOOL-dDeclaredLoop-15`'s, and the `parked` and `incomplete` rows are `TOOL-dDeclaredLoop-31`'s.
  Observed by AC1.
- **S3** — The build table's rows, B1 to B25 in §4: every row of flow-steps' table
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:729-763`) that
  enters no terminal, touches no `parked` or `incomplete` state, is not the parent-withdrawal row (:746)
  and is not the best-effort descope (:751), one row per item and outcome that fires it, each outcome
  spelled as its `[[item]]` row's closed `outcomes` spells it. Observed by AC1 and AC2.
- **S4** — The feature and unit tables, F1 to F8 and U1 to U8 in §4, derived from the orientation
  record's unit steps (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md:130-132`).
  Observed by AC1.
- **S5** — The engine, `derive_move(level, state, item, outcome, facts, tables=None)` in
  `tools/loop/loop_table.py`. It returns the matching row and its resolved `to`, or raises
  `TransitionRefused` naming the level, state, item and outcome. It resolves `to = "@prior"` and
  `to = "@reentry"` from the facts, and holds a `when = "before-push"` row to the `pushed` fact. Its
  CLI is `python tools/loop/loop_table.py move`. Observed by AC2, AC3 and AC4.
- **S6** — Exit items by tag. Every row's `item` is an `item.<seg>.<seg>` tag that resolves, through
  `tools/loop/loop_lib.py#read_items`, to an `[[item]]` row, or, for an item outside the five steps'
  programs (`item.entry.*`, `item.life.*`, `item.review.*`), to its `[[stand-in]]` row; B11's `@any`
  resolves the `reenters` fact the same way. A declared item's `outcome` is a word of its closed set,
  read by `tools/loop/loop_lib.py#derive_outcome_set`, and a `disposition` is a member of the
  `[dispositions]` set (I9) the same file declares, read through `check_loop`. Observed by AC5.
- **S7** — The route join, owed beside the table (flow-steps.md:771-774), both ways, over every
  cross-step route: an outcome a declared item routes to `transition`, or to a declared item of
  another step. Forward, each such route has a build row for that item and outcome, or one
  `[[owed-row]]` naming the unit or build that writes its row, so a missing row is red. Backward,
  every build row whose item is declared fires on a cross-step route of it, and where that route
  names an item, the row's `to` is the `state` of that item's step. An owed row whose route is no
  cross-step route, or which a build row also covers, is red as stale. Observed by AC6.
- **S8** — The stand-ins: one `[[stand-in]]` row per row item whose owning build has not landed, each
  naming `item` and `owner`, read by `read_stand_ins`. A move through such an item answers
  `stand-in <owner>`, and the fixture plants supply its fixture witness. A stand-in row naming no row
  item, or naming another owner than the item's `[[item]]` row declares, is red. Observed by AC7.
- **S9** — `check_transition_tables`, `python tools/loop/loop_table.py check`, whose `--selftest` runs
  the check, every plant and the moves of AC2 to AC4 and AC7 against their expected observations, and
  the leg `loop transition tables` running `check --selftest`, with the rows a new leg owes,
  `enforces = ["principle.p20"]` among them (dOrderedCharter-7 S2), the tag of the v2 `[enforcement]`
  row naming this unit's clause `cl-dClosedLoop-0098`. The pending list holds a `principle` row for
  that tag, armed by dDeclaredLoop, and this pass deletes it, as the meta-check reds it stale once a
  leg enforces the tag. Observed by AC1 to AC8, and through the `New arm:` line.
  **Readers:** by name: `tools/playbook/principles.toml`, which declares the tag the row names and
  keeps it · by value: `tools/playbook/core.py`, its meta-check verb, which reds a pending row whose
  item a leg's `enforces` holds and counts the rest.
- **S10** — The page `help/loop.md`, `TOOL-dDeclaredLoop-1`'s, gains a section on the three tables,
  the `move` verb's three answers, the owed rows and the stand-in list, and the kit's
  `tools/loop/README.md` gains the module's paragraph. Observed by AC9.
- **S11** — One in-process case runner, `run_selftest_cases(main, cases, label)` in
  `tools/loop/loop_lib.py`, which runs each case through a module's `main` with its output captured
  and grades its exit and a line by its opening and a needle. `loop_table.py`'s `check --selftest`
  is its second caller: the first, `tools/loop/loop_checklist.py#main`, calls it in place of its own
  loop, its printed lines byte for byte as before. Observed by AC10.

## 3. Non-goals (OUT)

- No terminal state and no row into one: `landed`, `withdrawn`, `superseded`, `deferred`, `retired`,
  `refused`, `merged` and `answered` are `TOOL-dDeclaredLoop-15`'s, and `incomplete` and `parked` rows
  `TOOL-dDeclaredLoop-31`'s. Their routes stand on the owed list until those rows land.
- No row for `item.plan.place`'s `unplaced`: its Then cell says "as `plan.unplaced` says"
  (flow-steps.md:186), whose values no record maps onto states; it stands on the owed list naming
  dRankedPlan, the key's owner.
- No witness evaluation. The engine answers whether a move is in the table. Whether the exit item's
  witness holds is the writer's precondition (`TOOL-dDeclaredLoop-3`) and the position engine's
  derivation (`TOOL-dDeclaredLoop-7`).
- No record of a move: `TOOL-dDeclaredLoop-3` writes it, and `TOOL-dDeclaredLoop-10` holds backward
  rows to the same record.
- No change to unattended's phase verb. `unattended.sh --phase` keeps its vocabulary check, and
  `TOOL-dDeclaredLoop-52` ships the phase-to-state map as rows.
- No counted-edge, reachability or termination rule: those are `TOOL-dDeclaredLoop-33`'s static
  check over these rows.
- No real witness for a stand-in item. Each owning build arms its own item and deletes its stand-in
  row in the same landing.
- No change to `loop_lib.py`'s checks or to `--check`'s output: the new tables are read by
  `loop_table.py` alone.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — `loop_lib.py`, the one reader of `tools/loop/loop.toml`, through which the tables and the items they name are read
- **consumes-from** `TOOL-dDeclaredLoop-16` — the `[dispositions]` closed set, which a row fired by a placement disposition names a member of
- **consumes-from** `TOOL-dDeclaredLoop-12` — each `[[item]]` row's closed `outcomes` and its `routes`, whose cross-step routes S7 joins to the rows both ways
- **hands-off** `TOOL-dDeclaredLoop-3` — the `loop.toml` transition rows and `derive_move`, which the writer calls before it records a move
- **hands-off** `TOOL-dDeclaredLoop-10` — the `loop.toml` transition rows, whose backward rows that unit holds to the record
- **hands-off** `TOOL-dDeclaredLoop-15` — the `loop.toml` transition rows and `[states]`, to which that unit adds the terminal set and its rows, deleting the owed row of each route it rows
- **hands-off** `TOOL-dDeclaredLoop-24` — the `loop.toml` transition rows, whose exit items that unit's fixed set keeps whole
- **hands-off** `TOOL-dDeclaredLoop-25` — the `loop.toml` transition rows, between which a repository stage's splice rows sit
- **hands-off** `TOOL-dDeclaredLoop-31` — the `loop.toml` transition rows and `[states]`, to which that unit adds the `parked` and `incomplete` rows
- **hands-off** `TOOL-dDeclaredLoop-52` — the phase-to-state-and-step map, which that unit ships as rows with one reader (the round-1 spec audit's id 4)
- **hands-off** external — the row for `item.plan.place`'s `unplaced`, owed to dRankedPlan, whose `plan.unplaced` values decide the state it enters

## 4. Design

### Data model

```toml
[states]
build = ["planning", "designing", "building", "testing", "deploying", "paused", "parked"]
feature = ["decomposed", "designed", "built", "tested", "deployed"]
unit = ["designed", "built", "tested", "deployed"]

[[transition]]
level = "build"           # build | feature | unit
from = ["planning"]       # states of the level, "none" for a level's entry, or "@open"
item = "item.plan.exit"   # the item whose outcome fires the row, by tag
outcome = "recorded"      # one word of that item's closed outcome set
to = "designing"          # a state, "@prior" or "@reentry"
witness = "the transition record"
# disposition = "new"     # optional: a member of the [dispositions] set
# when = "before-push"    # optional: the row holds only while the build's landing is unpushed

[[stand-in]]
item = "item.plan.exit"
owner = "dRankedPlan"

[[owed-row]]
item = "item.deploy.close"
outcome = "closed"
by = "TOOL-dDeclaredLoop-15"   # the unit or build whose row covers this route
```

`@open` expands to the level's open states. `none` is the entry of a level, never a state. Every
outcome below is a word of its item's `outcomes` at HEAD; an item no `[[item]]` row declares has no
set, and its row's word is the flow record's.

### The build table

| Row | From | Item | Outcome | To | Source |
|---|---|---|---|---|---|
| B1 | none | `item.entry.claim` | claimed, disposition `new` | planning | :729-730 |
| B2 | none | `item.plan.dedupe` | patch | designing | :731, :181 |
| B3 | none | `item.entry.claim` | claimed, disposition `repeat` | designing | :735 |
| B4 | planning | `item.plan.exit` | recorded | designing | :736 |
| B5 | designing | `item.design.exit` | recorded | building | :741 |
| B6 | designing | `item.design.decompose` | goal-fork | planning | :742 |
| B7 | building | `item.build.exit` | recorded | testing | :743 |
| B8 | building | `item.build.unit-pass` | spec-wrong | designing | :744, :289 |
| B9 | building | `item.build.core` | own-red | designing | :744, :298 |
| B10 | building | `item.review.dispose` | unit | designing | :745 |
| B11 | the five step states, when before-push | `@any` | admitted | `@reentry` | :747 |
| B12 | testing | `item.test.exit` | recorded | deploying | :748 |
| B13 | testing | `item.test.attribute` | code-miss | building | :749, :360 |
| B14 | testing | `item.test.merge` | conflict | building | :749, :356 |
| B15 | building | `item.build.resolve` | resolved | testing | :750, :300 |
| B16 | testing | `item.test.attribute` | spec-wrong | designing | :752, :360 |
| B17 | deploying | `item.deploy.current` | stale | testing | :753 |
| B18 | deploying | `item.deploy.land` | refused | testing | :754 |
| B19 | `@open` | `item.life.request` | pause | paused | :756 |
| B20 | paused | `item.life.request` | resume | `@prior` | :757 |
| B21 | building | `item.build.unit-pass` | interface-change | designing | :744, :289 |
| B22 | building | `item.build.distill` | unclassed | designing | :744, :297 |
| B23 | building | `item.build.resolve` | interface-clash | designing | :744, :300 |
| B24 | testing | `item.test.seen-red` | missing | building | :749, :362 |
| B25 | testing | `item.test.route` | inherited | designing | :752, :359 |

B1 to B20 keep the meaning their numbers had at rev-3, which `TOOL-dDeclaredLoop-10` cites by number,
each now keyed on the item and outcome the landed routes declare. B21 to B25 are the cross-step routes
rev-3's prose rows held without a row of their own. B2 fires on `item.plan.dedupe`'s `patch`, routed
`transition`, since `plan.dedupe` needs `item.entry.claim` and its Then cell sends "none, on a patch"
to Design, so a patch build holds no state until the dedupe answers. B13, B14, B15 and B24 are the
four cross-step routes that name an item of another step rather than `transition`.

B11 is one row written with `from` the five step states, `item = "@any"`, `outcome = "admitted"` and
the fact `reenters` naming the re-entered item; `@reentry` resolves to the `state` of the `[[step]]`
row that item's `step` names. It is the one row whose `item` is not a tag, and S6 grades it through
the fact instead. Its `from` is :747's list, the five step states, never `@open`.

### The feature and unit tables

A unit is designed when its spec is committed and derived READY, built when its pass commits and
acceptance record hold, tested when the verdict for the build's prepared merge holds, and deployed
when the landing contains it (orientation.md:130-132). A feature holds its least-advanced unit's step,
the rule the record gives the build (:132), so a feature row fires on its last unit's outcome, which
the mover judges and the engine does not.

| Row | Level | From | Item | Outcome | To |
|---|---|---|---|---|---|
| U1 | unit | none | `item.design.ready` | ready | designed |
| U2 | unit | designed | `item.build.acceptance` | pass | built |
| U3 | unit | built | `item.test.exit` | recorded | tested |
| U4 | unit | tested | `item.deploy.land` | landed-gated | deployed |
| U5 | unit | built | `item.test.attribute` | spec-wrong | designed |
| U6 | unit | tested | `item.deploy.current` | stale | built |
| U7 | unit | tested | `item.deploy.land` | landed-ungated | deployed |
| U8 | unit | tested | `item.deploy.land` | already-held | deployed |
| F1 | feature | none | `item.design.decompose` | decomposed | decomposed |
| F2 | feature | decomposed | `item.design.ready` | ready | designed |
| F3 | feature | designed | `item.build.acceptance` | pass | built |
| F4 | feature | built | `item.test.exit` | recorded | tested |
| F5 | feature | tested | `item.deploy.land` | landed-gated | deployed |
| F6 | feature | designed, built | `item.design.reentry` | breaking | decomposed |
| F7 | feature | tested | `item.deploy.land` | landed-ungated | deployed |
| F8 | feature | tested | `item.deploy.land` | already-held | deployed |

F6 is the feature re-entry the builder's route names for a breaking interface change (flow-steps.md
:289, `build.unit-pass`'s Then cell), and `item.design.reentry`'s `breaking` is the architect's call
on it. Its `from` holds `designed` too, since an interface change arises in a unit pass, before F3.
U5 and U6 follow from the step definitions above (§8 F7).

### The engine

```python
class TransitionRefused(Exception): ...

def derive_move(level, state, item, outcome, facts, tables=None):
    """The row the table holds for this move, and its resolved `to`. `tables` is what
    read_transition_rows returns, the shipped definition's when None. Raises TransitionRefused when
    no row matches; raises ValueError on an unknown level, state, or a fact a row's guard needs."""
```

The match is exact on `level`, membership of `state` in the expanded `from`, `item`, `outcome`, and
`disposition` where the row declares one. Two matching rows are a table defect, refused by `check`.
`when = "before-push"` matches only with `facts["pushed"]` `no`, and an absent `pushed` fact, or a
value other than `yes` or `no`, is a `ValueError`, never a default. `@prior` takes `facts["prior"]`,
which must be an open state of the level. The CLI:

```
python tools/loop/loop_table.py move --level build --from planning --item item.plan.exit --outcome recorded [--fact k=v]...
python tools/loop/loop_table.py check [--selftest]
python tools/loop/loop_table.py --fixture --plant <case>
```

`move` exits 0 printing `move — <level> · <from> → <to> · <item>`, and `· stand-in <owner>` after it
when the item is a stand-in; 1 printing `refused — <level> · <from> · <item> · <outcome>: no row`; 2
on a malformed argument or a `ValueError`. `check` prints one `loop: table <level> · <n> row(s) · <m>
state(s)` line per level, one `loop: owed <item> · <outcome> · <by>` line per owed row, one `loop:
stand-in <item> · <owner>` line per stand-in, and each refusal as `loop: refused · ...`, and exits 1
on a refusal. An absent definition or an empty `[[transition]]` table exits 2 naming it, never
admitting a move. `--fixture --plant <case>` runs `check` with one break of `PLANTS` made in memory by
`write_table_plant`, never on disk. `check --selftest` runs its cases through `run_selftest_cases`.

### The checks

`check_transition_tables(data, where, items)` reads the rows through `read_transition_rows` and
`read_stand_ins`, the items through `read_items`, and reds: an undeclared level or state, a `to`
outside the level's states and the two dynamic forms, two rows matching one move, a row `item` that
is not an item tag or resolves neither to a declared item nor to a stand-in row, an `outcome` outside
that item's set, a `disposition` outside the `[dispositions]` set, each S7 finding, and a stale or
mis-owned stand-in row (S8). Each `[[step]]` row's `exit` item fires a build row out of that step's
`state`, B4, B5, B7 and B12, or stands on the owed list: the Deploy exit, `item.deploy.close`, enters
`landed`, a terminal, and `TOOL-dDeclaredLoop-15`'s row covers it.

What the check does not check: whether a witness holds; whether a stand-in's owner has landed; that
every row item owned by an unlanded build has a stand-in row; reachability, termination and counted
edges (`TOOL-dDeclaredLoop-33`); the feature rows' last-unit rule; the routes of the feature and unit
rows, which S7 joins for the build table alone; that an owed row's `by` names a real unit or build.

### The owed rows

| Item | Outcome | By | Why no row here |
|---|---|---|---|
| `item.plan.triage-rule` | refuse | TOOL-dDeclaredLoop-15 | enters `refused`, a terminal (:737) |
| `item.plan.triage-judge` | refuse | TOOL-dDeclaredLoop-15 | enters `refused`, a terminal (:737) |
| `item.plan.place` | unplaced | dRankedPlan | as `plan.unplaced` says (:186), which no record maps onto states |
| `item.deploy.parents` | withdrawn | TOOL-dDeclaredLoop-15 | its parent row, from :746 |
| `item.deploy.close` | closed | TOOL-dDeclaredLoop-15 | enters `landed`, a terminal (:755) |

The list only shrinks: the unit that writes a route's row deletes its owed row in the same landing,
and the check reds the pair until it does (§8 F6).

### The stand-ins

| Item | Owner |
|---|---|
| `item.entry.claim` | dPlacedRequest |
| `item.plan.dedupe`, `item.plan.exit` | dRankedPlan |
| `item.design.decompose`, `item.design.exit`, `item.design.ready`, `item.design.reentry` | dIndexedDesign |
| `item.build.unit-pass`, `item.build.acceptance`, `item.build.distill`, `item.build.core`, `item.build.exit`, `item.build.resolve` | dScopedBuild |
| `item.review.dispose` | dDeclaredLoop |
| `item.test.merge`, `item.test.seen-red`, `item.test.attribute`, `item.test.route`, `item.test.exit` | dWitnessedBar |
| `item.deploy.current`, `item.deploy.land` | dShippedRelease |
| `item.life.request` | dWellOiledMachine |

One `[[stand-in]]` row per item, its fixture witness the mover naming the witnessing commit, as
`tools/unattended/unattended.sh#verb_phase` requires today. Every row item is on the list at HEAD,
no owning build having landed: the build pass derives it from the `[[item]]` rows' `owner` field. `item.entry.claim` and `item.life.request` have no
`[[item]]` row (`TOOL-dDeclaredLoop-12` §3), so their stand-in rows are the one place their owners are
declared. `item.review.dispose` is this build's own, declared by `TOOL-dDeclaredLoop-20` at a later
order, so it carries a stand-in row naming dDeclaredLoop until then; a stand-in row whose item is
declared with the same owner stays legal, and the list is pruned when the owner lands. The list
shrinks only: an owning build arms its item by landing its witness reader and deleting the row
together. It is authored rather than derived from the owning build's status because a copy-installed
loop kit carries no other build's folder to read (§8 F5).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/loop_table.py` | module | none declared for files |
| `derive_move` | function | `py.function`, OK |
| `check_transition_tables` | function | `py.function`, OK |
| `read_transition_rows` | function | `py.function`, OK |
| `read_stand_ins` | function | `py.function`, OK |
| `write_table_plant` | function | `py.function`, OK |
| `run_selftest_cases` | function of `loop_lib.py` | `py.function`, OK |
| `TransitionRefused` | type | `py.type`, OK |
| `[[transition]]`, `[[stand-in]]`, `[[owed-row]]`, `[states]` | tables of `tools/loop/loop.toml` | none |
| `loop transition tables` | leg | none |

Each name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as <cell>` on 2026-11-14
and answered OK. The module says `loop_table`, never bare `transition`, because
`tools/memory-tree/transition_audit.py` already holds that word for the transition-merge audit.

### Migration

None: the tables are new rows, and no record reads a state yet.

### Rollout

Live on landing. Nothing calls `move` until the writer of `TOOL-dDeclaredLoop-3` lands, so no run's
behaviour moves here.

### Files touched (estimate)

- `tools/loop/loop.toml`: the four tables before the `[[item]]` rows, and their header lines
- `tools/loop/loop_table.py`
- `tools/loop/loop_lib.py`: `run_selftest_cases`; its docstring's sentence on a `transition` route
  points at `loop_table.py`
- `tools/loop/loop_checklist.py`: its `check --selftest` through `run_selftest_cases`
- `tools/loop/kit.toml`: the leg as a `[[gate_leg]]`, and the comment naming the module
- `tools/loop/README.md`: the module's paragraph
- `tools/gate-legs.json`: the leg `loop transition tables`, argv `python
  {prefix}/loop/loop_table.py check --selftest`, `declarations`, `repo`, `enforces` `principle.p20`
- `tools/govkit/usage.toml`: the module's three usage rows, its bare entry, `#move` and `#check`
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `tools/playbook/core-pending.txt`: the `principle` row of S9's tag
- `memory/map/features/loop.md`: the leg in its `gate-legs` list
- `memory/map/generated/`, re-rendered by the codebase-map kit's `gen_map.py --write`
- `memory/guides/SESSION-KICKOFF.md`: `last-audit` re-stamped, its watch list holding the manifest
- `help/loop.md`: the tables' section

### Alternatives rejected

- **A linear stage list with backward moves inferred.** It is today's shape and cannot hold a row
  such as B6 or B17, each a declared route with its own witness.
- **The engine evaluating witnesses.** It would duplicate the position engine's derivation and make
  a table lookup depend on every witness kind's reader.
- **Stand-ins derived from each owner's build status.** An adopter's copy of the kit holds no gov
  build folder, so the derivation would read nothing there.
- **`outcome` as a list.** U4, U7 and U8 would be one row, but the engine's exact match and S7's
  join, both per item and outcome, would each need a list branch for three rows' saving.

## 5. Production-readiness checklist

- security — no write path: the engine and the check read the definition only, and the plants
  break only what was read into memory.
- perf / scale — 41 rows, PINNED 2026-11-14 from §4's tables; every move is a linear scan. The leg's
  ceiling is 120 seconds, PINNED 2026-11-14 beside `loop definition`'s, and no
  `tools/run-gates/ceiling-evidence.txt` row is typed, that file being generated by the runner.
- error / empty / loading states — an absent definition or an empty table exits 2 naming it, never
  admitting a move; an absent guard fact exits 2.
- observability — every refusal names the level, state, item and outcome, every stand-in move
  names its owner, and `check` prints each owed row.
- risks — every row item is a stand-in until its owner lands, so the table refuses but witnesses
  nothing yet. The loop kit ships changed bytes, so its version moves where the lander mints it
  (`tools/govkit/govkit.py#cmd_epoch`); no file of this change is a delegate of the verdict-epoch
  gate, whose list is the memory-tree kit's own modules.
- testing — what the change could newly red, and what keeps each green:
  - `loop definition`: `tools/loop/loop_lib.py#check_loop` reads only the `step`, `workflow` and
    `disposition-alias` tables and refuses no other table, and `--check` runs none of the new
    functions, so it stays 0 with its output unchanged.
  - `loop checklist tags`: its cases run through `run_selftest_cases` with the same label, so each
    printed line and the exit are as before; AC10 compares them.
  - the readers that copy the definition, `tools/unattended/check-unattended.test.sh`,
    `tools/unattended/cross-component.test.sh`, `tools/roles/adopt-roles.test.sh`,
    `tools/playbook/instruction_units.py#render_drive_loop` and
    `tools/playbook/gov_tag.py#build_tags_fixture`: they read the `step`, `workflow` and `item`
    tables, none of which this unit edits.
  - `tags (the resolver's checks)`: `tools/playbook/tag_index.py#read_toml_tags` reads `[[item]]`
    rows' `tag` key alone, and S1 keeps each item row's span; citations are read from tracked
    Markdown only (`tools/playbook/tag_index.py#extract_citations`), so the page and the kit README
    backtick only declared item tags, and spell the entry, life and review items and every plant tag
    inside a fence or unbackticked.
  - `core meta-check`: the leg's `enforces` holds a registry tag, it carries no `guard`, which
    `core.bypass` `never` would red, and the pending row of that tag is deleted in the same commit.
  - `govkit selfcheck`, `govkit selftest`, `govkit refusal join` and `govkit acceptance matrix`: the
    leg is the loop kit's `[[gate_leg]]`, as `loop definition` is, with subject `repo`, its manifest
    row mirroring the descriptor's, and `tools/govkit/subject-pins.tsv` regenerated in the same commit.
  - `every held leg is budgeted, every budget row resolves`: the leg is `repo` and `declarations`, so
    it is no held leg and owes no `tools/run-gates/selftest-budgets.txt` row.
  - `docs` and `help page commands`: each command the page shows has its usage row and its
    `<!-- usage: <id> <fp8> -->` marker from `python tools/govkit/docs_leg.py --fingerprints`; a fenced
    block naming the gov path is fenced `run: no` with the reason `loop_checklist.py`'s section gives.
  - `codebase-map coverage + freshness` and `codebase-map gate coverage`: the dossier's paths glob
    covers the module, its `gate-legs` list gains the leg, and `gen_map.py --write` re-renders
    `memory/map/generated/`; `recall floor` and `recall floor arms` carry `memory/` in their guard,
    so the re-render owes both a run.
  - `kickoff-manifest ratchet`: `last-audit` is re-stamped with a `manifest-audit:` delta line in the
    commit that edits `tools/gate-legs.json`.
  - `install-prefix (shipped surface)`: the module, the kit README, the descriptor and the definition
    spell `{prefix}`, `<prefix>` or a path relative to the kit, never a kit path under the tool root.
  - `method carriers (every pointer declared)`: no file this unit writes names the build method's
    path, so `memory/project/method-carriers.txt` gains no row.
  - `python resolver (behaviour + inline parity + idiom ban)`: no resolver copy is added.
  - `playbook render selftest` and `policy fixtures`: their guards hold `core-pending.txt` and the
    manifest; one row leaves the one, one leg row joins the other, and neither changes a fixture.
- migration — none.
- user docs — `help/loop.md` gains the tables' section (S10).

## 6. Acceptance criteria

- **AC1** — When `python loop_table.py check` runs in `tools/loop/` on the built tree, it exits 0
  and prints a `loop: table` line per level with its row and state counts, and `--fixture --plant bad-state`
  exits 1 naming the planted row whose `to` is `reviewing`, and `--plant two-rows` exits 1 naming B7's
  move matched by two rows.
  Red when: a row naming an undeclared state, or a second row for one move, passes the check.
- **AC2** — When `python loop_table.py move --level build --from planning --item
  item.design.exit --outcome recorded` runs in `tools/loop/`, it exits 1 printing `refused` with the level, state, item
  and outcome, and `--from designing` with the same item and outcome exits 0 naming `building`.
  Red when: the engine admits a move by stage order with no row.
- **AC3** — When `python loop_table.py move --level build --from paused --item
  item.life.request --outcome resume --fact prior=testing` runs there, it names `testing`, and the same move
  with no `prior` fact exits 2.
  Red when: `@prior` resolves to a default state.
- **AC4** — When `python loop_table.py move --level build --from building --item @any
  --outcome admitted --fact reenters=item.plan.input --fact pushed=no` runs there, it names `planning`; with
  `pushed=yes` it exits 1; with no `pushed` fact it exits 2.
  Red when: a `before-push` row matches after the landing push.
- **AC5** — When `python loop_table.py --fixture --plant bad-exit` runs there, the check exits 1
  naming three rows: one whose `item` is the bare `plan.exit`, one naming `item.plan.nosuch`, and one
  whose `outcome` is outside its item's set.
  Red when: a row's exit item is accepted without resolving its tag.
- **AC6** — When `python loop_table.py --fixture --plant dropped-row` runs there, the fixture
  deletes B7 while `item.build.exit` keeps routing `recorded` to `transition`, and the check exits 1
  naming `item.build.exit`; under `--plant unrouted-row`, a row on `item.build.acceptance`'s `pass`,
  which routes to `item.build.scope` in its own step, exits 1 naming the row; under `--plant
  owed-stale`, an owed row for `item.build.exit`'s `recorded`, which B7 covers, exits 1 naming it; and
  `check` on the tree prints `loop: owed item.deploy.close · closed · TOOL-dDeclaredLoop-15`.
  Red when: a cross-step route with no row and no owed row, a row no route reaches, or an owed row a
  row covers, passes.
- **AC7** — When `python loop_table.py move --level build --from planning --item
  item.plan.exit --outcome recorded` runs there, it exits 0 printing `stand-in dRankedPlan`, and `--fixture
  --plant stand-in` exits 1 naming a planted stand-in row for an item no row names and one whose
  `owner` differs from the item's.
  Red when: a stale or mis-owned stand-in row survives the check.
- **AC8** — When `grep -n '"loop transition tables"' tools/gate-legs.json` runs, it finds the leg row
  and its argv naming `loop_table.py check`; `python -m json.tool tools/gate-legs.json` read for that
  row shows `enforces` holding `principle.p20`; `grep -c 'principle.p20' tools/playbook/core-pending.txt`
  prints 0; and `python tools/playbook/core.py meta-check` on this unit's pass exits 0, naming neither
  that leg nor a stale pending row.
  Red when: the leg row is absent or names another command, so no bar runs the check, or carries no
  `enforces`, which dOrderedCharter-7 S3's meta-check reds, or the pending row survives.
- **AC9** — When `grep -n 'loop_table.py move' loop.md` runs in `help/`, it finds the section naming the
  verb, and the section names `refused`, `stand-in` and the owed rows.
  Red when: the tables land and the page still describes the steps alone.
- **AC10** — When `python tools/loop/loop_checklist.py check --selftest` runs on the built tree, it
  exits 0 printing the same lines it prints at HEAD before this pass, and `python loop_table.py check
  --selftest` in `tools/loop/` exits 0 printing one `PASS` line per case and a `PASS`
  summary.
  Red when: the shared runner changes a line or an exit of the checklist's self-test, or passes a case
  whose exit or line does not match.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `loop definition` · `loop checklist tags` · `core meta-check` · `govkit selfcheck` · `docs` · `help page commands` · `tags (the resolver's checks)` · `install-prefix (shipped surface)` · `method carriers (every pointer declared)` · `every held leg is budgeted, every budget row resolves` · `python resolver (behaviour + inline parity + idiom ban)` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `codebase-map gate coverage` · `kickoff-manifest ratchet` · `playbook render selftest` · `policy fixtures` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest`

New arm: tools/loop/loop_table.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the `loop transition tables` leg over the tree, its failing case staged by deleting row B7 · none
New arm: tools/loop/loop_checklist.py · covers AC10 · the `loop checklist tags` leg, its case loop now `run_selftest_cases`, its failing case staged by one case owing exit 0 set to owe 1 · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `tools/memory-tree/tree_lib.py#STATUS_TOKENS`. Observation, 2026-10-24: the tuple
  holds `OPEN`, `SPECCED`, `INPROGRESS`, `BLOCKED`, `DEFERRED`, `CLOSED`, `WONTDO` and not `DRAFT`,
  so a `DRAFT` header parses as none. Liveness: the tuple would show `DRAFT` if the vocabulary held
  it. RESOLVED (agent, 2026-10-24, delegated): `OPEN`, the token `memory/TEMPLATE-SPEC.md` gives a
  spec in drafting.
- **F2 — What do the feature and unit tables hold, which no record drafts?** Options: (a) the unit
  steps the orientation record defines, with the feature holding its least-advanced unit's step;
  (b) a copy of the build table per level. (b) gives a unit a `planning` state no unit has. RESOLVED
  (agent, 2026-10-24, delegated): (a), rung 1, orientation.md:130-132.
- **F3 — Does the engine evaluate the exit item's witness?** The clause asks the engine to refuse a
  move the table lacks. RESOLVED (agent, 2026-10-24, delegated): no, rung 1; the witness is the
  writer's precondition and the position engine's derivation, each its own unit.
- **F4 — Does the route join read `TOOL-dDeclaredLoop-12`'s `routes`, an edge the brief's table does
  not list?** `gap-flow-15` names the join of each item's routes to the table as unbuilt, and
  this unit closes that gap. RESOLVED (agent, 2026-10-24, delegated): yes, rung 3, the option
  closing the gap; the edge is declared in §3 and returned to that unit's writer for its reverse.
- **F5 — Is the stand-in list authored or derived from each owner's landing?** Options: (a) an
  authored, shrink-only list; (b) derived from the owner build's derived status. (b) reads gov's
  build folders, which an adopter's copy of the kit does not hold. RESOLVED (agent, 2026-10-24,
  delegated): (a), rung 3.
- **F6 — How does the forward route join hold at this landing, when five cross-step routes enter
  states whose rows other units write?** The routes are `item.plan.triage-rule` and
  `item.plan.triage-judge` on `refuse`, `item.deploy.parents` on `withdrawn` and `item.deploy.close` on
  `closed`, all `TOOL-dDeclaredLoop-15`'s at order 12, and `item.plan.place` on `unplaced`, whose
  target no record states. Options: (a) an authored, shrink-only `[[owed-row]]` list naming the unit
  or build that writes each row, printed by `check` and red once a row covers it; (b) the forward arm
  prints those routes and stays green until `TOOL-dDeclaredLoop-15` lands, a gate that cannot red on
  them; (c) this unit writes the rows into terminals too, which needs the terminal set
  `TOOL-dDeclaredLoop-15` declares and is that unit's scope. Recommendation (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 3: the [gate] practice, an exemption declared,
  printed and red when stale, never read as coverage. widens: none · relaxes: none
- **F7 — Which outcomes fire the unit rows U5 and U6, whose rev-3 outcomes no item declares?** Rev-3
  keyed U5 on `item.design.reentry`'s "spec wrong" and U6 on `item.build.fix-pass`'s "a code miss";
  the landed sets are `additive` and `breaking`, and `committed`. Options: (a) U5 on
  `item.test.attribute`'s `spec-wrong`, built to designed, and U6 on `item.deploy.current`'s `stale`,
  tested to built, since a unit is tested only while the verdict holds; (b) U5 on
  `item.build.unit-pass`'s `spec-wrong`, which fires while the unit is still designed and moves
  nothing, and U6 dropped. Recommendation (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 1, the step definitions at
  orientation.md:130-132. widens: none · relaxes: none
- **F8 — Where is the leg declared?** Options: (a) a `[[gate_leg]]` of the loop kit's descriptor, as
  `loop definition` is; (b) gov's own `[[exempt_leg]]` of `tools/govkit/registry.toml`, as `loop
  checklist tags` and `loop computed witness` are. Those two reach a kit the loop kit takes no edge to;
  this module reads the loop kit's own definition, and `read_items` reads the playbook kit's layer tags
  only where they resolve, so every holder of the kit can run it. Recommendation (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 3: the [gate] practice, a leg every holder can
  run ships with the kit. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 13, flow-steps' `[transitions]` table
  at base `ed497191`, the orientation record's unit steps and C2-F8.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-52, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-11-05 · S9 · §4 Files touched · AC8 · TOOL-dDeclaredLoop-56 §8 F5 (a), per the brief
  `2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade`: the leg `loop transition tables` carries
  `principle.p20`, its clause's `[enforcement]` row; its own pass writes it, so the core meta-check never
  reds the leg.
- rev-4 · 2026-11-14 · §1 · S1 S3 S4 S5 S6 S7 S8 S9 S10 S11 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 AC5 AC6
  AC7 AC8 AC9 AC10 · §7 · §8 F1 F6 F7 F8 · §10 · re-grounded at HEAD `deb9c4976` by the brief
  2026-11-14-prompt-TOOL-dDeclaredLoop-13-reground-brief; mechanism, carries, order and status kept.
  Each row is keyed on an outcome its item's landed set spells, B21 to B25 added for routes rev-3's
  prose rows held; S7 joins item-named cross-step routes and an owed list (F6); U5 and U6 re-keyed
  (F7); `item.life.close` left the stand-in list; B11's `from` is :747's; S9 deletes the landed
  pending row with its readers; the leg is the kit's (F8); `ceiling-evidence.txt` left the write set
  and the usage, map and kickoff rows joined it; S11 shares the case loop; code cited by symbol.

## 10. Reuse audit

The seam this unit extends is the loop kit's reader, `tools/loop/loop_lib.py`: `read_definition`,
`check_loop`, `read_items`, `derive_outcome_set` and `read_steps`. Its command shape is
`tools/loop/loop_checklist.py#main`'s, whose in-process case loop becomes the shared
`run_selftest_cases` at this, its second instance, rather than a copy. No existing seam fits the
table itself: `python tools/codebase-map/reuse_lookup.py "refuse a state transition that the declared
transition table lacks"`, run 2026-11-14, ranked name stems only, `PolicyRefused`, `declares` and
`read_step_states` among them, none a move table. The closed-set refusal it follows as a pattern is
`tools/unattended/unattended.sh#verb_phase`'s membership test over
`tools/unattended/unattended.sh#phases`, read at HEAD. `python tools/memory-recall/query.py "how is a
phase transition refused when it is not in the vocabulary"` with the terms below returned the scout
rows and `TOOL-aStandingWrit-1`'s review of `verb_phase`, each agreeing with source now.

Recall terms used: transition table phase vocabulary refuse verb_phase PHASES_CORE terminal fixture witness exit item stand-in route
