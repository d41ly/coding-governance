# TOOL-dDeclaredLoop-13 — one transition table per level, the engine refusing a move it lacks

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 10 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0098@89542705 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

The loop definition declares one transition table per level (build, feature, unit), and one engine
answers every proposed move from those rows alone. A move no row holds is refused. Each row names, by
its `item.<step>.<name>` tag, the exit item whose outcome fires it. An item whose owning build has not
landed is a declared stand-in with a fixture witness, until that build lands and arms it (C2-F8,
`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-walk-return-c2.md:100-109`).
Today the only move record is unattended's linear phase vocabulary, checked by membership alone
(`tools/unattended/unattended.sh:6140-6143`), and no feature or unit table exists (`gap-flow-15`).

## 2. Scope (IN)

- **S1** — The three tables, as `[[transition]]` rows of `tools/loop/loop.toml` (I1), each carrying
  `level`, `from`, `item`, `outcome`, `to` and `witness`, and optionally `disposition` and `when`
  (§4 "### Data model"). Observed by AC1.
- **S2** — The states of each level in a `[states]` table of the same file: the build's open states
  `planning`, `designing`, `building`, `testing`, `deploying`, `paused` and `parked` (I3), and the
  feature's and the unit's states. Each step's state and exit item stay on
  `TOOL-dDeclaredLoop-1`'s `[[step]]` rows, read through `read_steps`. The terminal set is
  `TOOL-dDeclaredLoop-15`'s, and the `parked` and `incomplete` rows are `TOOL-dDeclaredLoop-31`'s.
  Observed by AC1.
- **S3** — The build table's rows: every row of flow-steps' table
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:729-763`) that
  enters no terminal, touches no `parked` or `incomplete` state, is not the parent-withdrawal row (:746)
  and is not the best-effort descope (:751). §4 lists them as B1 to B20. Observed by AC1 and AC2.
- **S4** — The feature and unit tables, F1 to F6 and U1 to U6 in §4, derived from the orientation
  record's unit steps (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md:130-132`).
  Observed by AC1.
- **S5** — The engine, `derive_move(level, state, item, outcome, facts)` in
  `tools/loop/loop_table.py`. It returns the matching row and its resolved `to`, or raises
  `TransitionRefused` naming the level, state, item and outcome. It resolves `to = "@prior"` and
  `to = "@reentry"` from the facts, and holds a `when = "before-push"` row to the `pushed` fact. Its
  CLI is `python tools/loop/loop_table.py move`. Observed by AC2, AC3 and AC4.
- **S6** — Exit items by tag. Every row's `item` is an `item.<step>.<name>` tag that resolves, through
  `loop_lib.py`'s `read_items`, to an `[[item]]` row, or, for an item outside the five steps'
  programs (`item.entry.*`, `item.life.*`), to its stand-in row; B11's `@any` resolves the `reenters`
  fact the same way. A declared item's `outcome` is a value of its closed `outcomes`, and a
  `disposition` is a value of `record-kind.disposition`'s closed set (I9), read by
  `TOOL-dDeclaredLoop-16`'s `read_dispositions`. Observed by AC5.
- **S7** — The route join, owed beside the table (flow-steps.md:771-774), both ways. Every outcome a
  declared item routes to `transition`, `TOOL-dDeclaredLoop-12`'s route value for a cross-step move,
  has a build row for that item and outcome, so a missing row is red; and every build row whose item
  is declared is routed `transition` on its outcome. Observed by AC6.
- **S8** — The stand-ins: one `[[stand-in]]` row per row item whose owning build has not landed, each
  naming `item` and `owner`, read by `read_stand_ins`. A move through such an item answers
  `stand-in <owner>`, and the fixture plants supply its fixture witness. A stand-in row naming no row
  item, or naming another owner than the item declares, is red. Observed by AC7.
- **S9** — `check_transition_tables`, `python tools/loop/loop_table.py check`, whose `--selftest`
  runs every plant against its expected observation, and the leg `loop transition tables` running
  both, with the rows a new leg owes. Observed by AC1 to AC8, and through the `New arm:` line.
- **S10** — The page `help/loop.md`, `TOOL-dDeclaredLoop-1`'s, gains a section on the three tables,
  the `move` verb's three answers and the stand-in list. Observed by AC9.

## 3. Non-goals (OUT)

- No terminal state and no row into one: `landed`, `withdrawn`, `superseded`, `deferred`, `retired`,
  `refused`, `merged` and `answered` are `TOOL-dDeclaredLoop-15`'s, and `incomplete` and `parked` rows
  `TOOL-dDeclaredLoop-31`'s.
- No witness evaluation. The engine answers whether a move is in the table. Whether the exit item's
  witness holds is the writer's precondition (`TOOL-dDeclaredLoop-3`) and the position engine's
  derivation (`TOOL-dDeclaredLoop-7`).
- No record of a move: `TOOL-dDeclaredLoop-3` writes it, and `TOOL-dDeclaredLoop-10` holds backward
  rows to the same record.
- No change to unattended's phase verb. `unattended.sh --phase` keeps its vocabulary check, and
  `TOOL-dDeclaredLoop-1` maps each run phase onto a state.
- No counted-edge, reachability or termination rule: those are `TOOL-dDeclaredLoop-33`'s static
  check over these rows.
- No real witness for a stand-in item. Each owning build arms its own item and deletes its stand-in
  row in the same landing.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — `loop_lib.py`, the one reader of `tools/loop/loop.toml`, through which the tables and the items they name are read
- **consumes-from** `TOOL-dDeclaredLoop-16` — `record-kind.disposition`'s closed set, which a row fired by a placement disposition names a value of
- **consumes-from** `TOOL-dDeclaredLoop-12` — each `[[item]]` row's closed `outcomes` and its `routes`, whose `transition` value S7 joins to the rows both ways
- **hands-off** `TOOL-dDeclaredLoop-3` — the `loop.toml` transition rows and `derive_move`, which the writer calls before it records a move
- **hands-off** `TOOL-dDeclaredLoop-10` — the `loop.toml` transition rows, whose backward rows that unit holds to the record
- **hands-off** `TOOL-dDeclaredLoop-15` — the `loop.toml` transition rows and `[states]`, to which that unit adds the terminal set and its rows
- **hands-off** `TOOL-dDeclaredLoop-24` — the `loop.toml` transition rows, whose exit items that unit's fixed set keeps whole
- **hands-off** `TOOL-dDeclaredLoop-25` — the `loop.toml` transition rows, between which a repository stage's splice rows sit
- **hands-off** `TOOL-dDeclaredLoop-31` — the `loop.toml` transition rows and `[states]`, to which that unit adds the `parked` and `incomplete` rows
- **hands-off** `TOOL-dDeclaredLoop-52` — the phase-to-state-and-step map, which that unit ships as rows with one reader (the round-1 spec audit's id 4)

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
item = "item.plan.exit"   # the exit item whose outcome fires the row, by tag
outcome = "pass"          # one value of that item's closed outcome set
to = "designing"          # a state, "@prior" or "@reentry"
witness = "the transition record"
# disposition = "new"     # optional: a value of record-kind.disposition's set
# when = "before-push"    # optional: the row holds only while the build's landing is unpushed

[[stand-in]]
item = "item.plan.exit"
owner = "dRankedPlan"
```

`@open` expands to the level's open states. `none` is the entry of a level, never a state. `pass`
stands for the single outcome of an exit item whose flow record names none (flow-steps.md's Then
cell for `plan.exit` reads only "Design"). Every outcome word below is the flow record's Then-cell
word, and the build pass takes the spelling `TOOL-dDeclaredLoop-12`'s item rows carry.

### The build table

| Row | From | Item | Outcome | To | Source |
|---|---|---|---|---|---|
| B1 | none | `item.entry.claim` | claimed, disposition `new` | planning | :729-730 |
| B2 | none | `item.entry.claim` | claimed, disposition `patch` | designing | :731 |
| B3 | none | `item.entry.claim` | claimed, disposition `repeat` | designing | :735 |
| B4 | planning | `item.plan.exit` | pass | designing | :736 |
| B5 | designing | `item.design.exit` | pass | building | :741 |
| B6 | designing | `item.design.decompose` | a fork the goal cannot survive | planning | :742 |
| B7 | building | `item.build.exit` | pass | testing | :743 |
| B8 | building | `item.design.reentry` | a unit or feature re-entry | designing | :744 |
| B9 | building | `item.build.core` | an own red: a fix unit | designing | :744 |
| B10 | building | `item.review.dispose` | built: a new unit | designing | :745 |
| B11 | `@open`, when before-push | the re-entered item | an amendment admitted | `@reentry` | :747 |
| B12 | testing | `item.test.exit` | pass | deploying | :748 |
| B13 | testing | `item.build.fix-pass` | a code miss | building | :749 |
| B14 | testing | `item.build.resolve` | a conflict | building | :749 |
| B15 | building | `item.build.resolve` | resolved | testing | :750 |
| B16 | testing | `item.test.route` | a new unit through Design | designing | :752 |
| B17 | deploying | `item.deploy.current` | stale | testing | :753 |
| B18 | deploying | `item.deploy.land` | refused before the push | testing | :754 |
| B19 | `@open` | `item.life.request` | pause | paused | :756 |
| B20 | paused | `item.life.request` | resume | `@prior` | :757 |

B11 is one row written with `from = "@open"`, `item = "@any"` and the fact `reenters` naming the
re-entered item; `@reentry` resolves to the `state` of the `[[step]]` row that item's `step` names.
Row B11 is the one row whose `item` is not a fixed tag, and S6 grades it through the fact instead.

### The feature and unit tables

A unit is designed when its spec is committed and derived READY, built when its pass commits and
acceptance record hold, tested when the verdict for the build's prepared merge holds, and deployed
when the landing contains it (orientation.md:130-132). A feature holds its least-advanced unit's step,
the rule the record gives the build (:132).

| Row | Level | From | Item | Outcome | To |
|---|---|---|---|---|---|
| U1 | unit | none | `item.design.ready` | pass | designed |
| U2 | unit | designed | `item.build.acceptance` | pass | built |
| U3 | unit | built | `item.test.exit` | pass | tested |
| U4 | unit | tested | `item.deploy.land` | landed | deployed |
| U5 | unit | built | `item.design.reentry` | spec wrong | designed |
| U6 | unit | tested | `item.build.fix-pass` | a code miss | built |
| F1 | feature | none | `item.design.decompose` | decomposed | decomposed |
| F2 | feature | decomposed | `item.design.ready` | pass, its last unit | designed |
| F3 | feature | designed | `item.build.acceptance` | pass, its last unit | built |
| F4 | feature | built | `item.test.exit` | pass | tested |
| F5 | feature | tested | `item.deploy.land` | landed | deployed |
| F6 | feature | built | `item.design.reentry` | breaking | decomposed |

F6 is the feature re-entry the builder's route names for a breaking interface change (flow-steps.md
:289, `build.unit-pass`'s Then cell).

### The engine

```python
class TransitionRefused(Exception): ...

def derive_move(level, state, item, outcome, facts):
    """The row the table holds for this move, and its resolved `to`. Raises TransitionRefused when
    no row matches; raises ValueError on an unknown level, state, or a fact a row's guard needs."""
```

The match is exact on `level`, membership of `state` in the expanded `from`, `item`, `outcome`, and
`disposition` where the row declares one. Two matching rows are a table defect, refused by `check`.
`when = "before-push"` matches only with `facts["pushed"]` false, and an absent `pushed` fact is a
`ValueError`, never a default. The CLI:

```
python tools/loop/loop_table.py move --level build --from planning --item item.plan.exit --outcome pass [--fact k=v]...
python tools/loop/loop_table.py check [--selftest]
python tools/loop/loop_table.py --fixture --plant <case>
```

`move` exits 0 printing `move — <level> · <from> → <to> · <item>`, and `stand-in <owner>` beside it
when the item is a stand-in; 1 printing `refused — <level> · <from> · <item> · <outcome>: no row`; 2
on a malformed argument. `check` exits 1 naming each finding.

### The checks

`check_transition_tables` reads every row through `loop_lib.py` and reds: an undeclared level or
state, a `to` outside the level's states and the two dynamic forms, two rows matching one move, a row
`item` that is not an item tag or resolves neither to a declared item nor to a stand-in row, an `outcome` outside that item's set,
a `disposition` outside I9's set, an outcome routed `transition` with no build row or a build row
whose declared item does not route its outcome `transition` (S7), and a stale or mis-owned stand-in
row (S8). Each `[[step]]` row's `exit` item fires a build row
out of that step's `state`: B4, B5, B7 and B12; the Deploy exit's row enters `landed`, a terminal,
and `TOOL-dDeclaredLoop-15`'s check holds it.

### The stand-ins

| Item | Owner | Today's stand-in |
|---|---|---|
| `item.plan.exit` | dRankedPlan | the mover names the witnessing commit, as `unattended.sh --phase` requires a witness today (`tools/unattended/unattended.sh:6191`) |
| `item.design.exit` | dIndexedDesign | the same |
| `item.build.exit` | dScopedBuild | the same |
| `item.test.exit` | dWitnessedBar | the same |
| `item.deploy.close` | dShippedRelease | the same |

Every other row item whose owning build has not landed gets its row the same way: the build pass
derives the list from the `[[item]]` rows' `owner` field, so every row item owned outside
dDeclaredLoop is on it. An item outside the five programs, `item.entry.claim`, `item.life.request`
and `item.life.close`, has no `[[item]]` row (`TOOL-dDeclaredLoop-12` §3), so its stand-in row is the
one place its owner, dPlacedRequest or dWellOiledMachine, is declared. B10's `item.review.dispose`
is this build's own, declared by `TOOL-dDeclaredLoop-20` at a later order, so it carries a stand-in
row naming dDeclaredLoop until then; a stand-in row whose item is declared with the same owner stays
legal, and the list is pruned when the owner lands. The list shrinks only: an owning build arms its item by landing its witness reader and
deleting the row together. It is authored rather than derived from the owning build's status
because a copy-installed loop kit carries no other build's folder to read (§8 F5).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/loop_table.py` | module | none declared for files |
| `derive_move` | function | `py.function`, OK |
| `check_transition_tables` | function | `py.function`, OK |
| `read_transition_rows` | function | `py.function`, OK |
| `read_stand_ins` | function | `py.function`, OK |
| `TransitionRefused` | type | `py.type`, OK |
| `[[transition]]`, `[[stand-in]]`, `[states]` | tables of `tools/loop/loop.toml` | none |

Each name was asked of `python tools/lexicon/lexicon.py --suggest <name> --as <cell>` and answered
OK. The module says `loop_table`, never bare `transition`, because `tools/memory-tree/transition_audit.py`
already holds that word for the backlog-mode merge audit.

### Migration

None: the tables are new rows, and no record reads a state yet.

### Rollout

Live on landing. Nothing calls `move` until the writer of `TOOL-dDeclaredLoop-3` lands, so no run's
behaviour moves here.

### Files touched (estimate)

- `tools/loop/loop.toml`
- `tools/loop/loop_table.py`
- `tools/loop/kit.toml`: the module and the leg declared
- `tools/gate-legs.json`: the leg `loop transition tables`, argv `python {prefix}/loop/loop_table.py check --selftest`
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `tools/run-gates/ceiling-evidence.txt`, the new leg's row
- `memory/map/features/loop.md`: the module's claim and the leg in its `gate-legs` list
- `help/loop.md`: the tables' section

### Alternatives rejected

- **A linear stage list with backward moves inferred.** It is today's shape and cannot hold a row
  such as B6 or B17, each a declared route with its own witness.
- **The engine evaluating witnesses.** It would duplicate the position engine's derivation and make
  a table lookup depend on every witness kind's reader.
- **Stand-ins derived from each owner's build status.** An adopter's copy of the kit holds no gov
  build folder, so the derivation would read nothing there.

## 5. Production-readiness checklist

- security — no write path: the engine and the check read the definition only.
- perf / scale — about forty rows; every move is a linear scan.
- error / empty / loading states — an absent definition or an empty table exits 2 naming it, never
  admitting a move.
- observability — every refusal names the level, state, item and outcome, and every stand-in move
  names its owner.
- risks — outcome words are spelled by `TOOL-dDeclaredLoop-12`'s item rows, and a disagreement surfaces
  as an S6 red at the build pass, never silently.
- testing — the plants of §6, each run by `--selftest` under the new leg.
- migration — none.
- user docs — `help/loop.md` gains the tables' section (S10).

## 6. Acceptance criteria

- **AC1** — When `python loop_table.py check` runs on the built tree, it exits 0 and prints each
  level's row and state counts, and `python loop_table.py --fixture --plant bad-state` exits 1 naming
  the planted row whose `to` is `reviewing`.
  Red when: a row naming an undeclared state passes the check.
- **AC2** — When `python loop_table.py --fixture --plant missing-row` runs, `move --level build
  --from planning --item item.design.exit --outcome pass` exits 1 printing `refused` with the level,
  state, item and outcome, and `--from designing` with the same item exits 0 naming `building`.
  Red when: the engine admits a move by stage order with no row.
- **AC3** — When `python loop_table.py --fixture --plant dynamic` runs, `move --from paused --item
  item.life.request --outcome resume --fact prior=testing` names `testing`, and the same move with no
  `prior` fact exits 2.
  Red when: `@prior` resolves to a default state.
- **AC4** — When the AC3 fixture runs B11 from `building` with `--fact reenters=item.plan.input
  --fact pushed=no`, the move names `planning`; with `pushed=yes` it exits 1; with no `pushed` fact it
  exits 2.
  Red when: a `before-push` row matches after the landing push.
- **AC5** — When `python loop_table.py --fixture --plant bad-exit` runs, the check exits 1 naming
  three rows: one whose `item` is the bare `plan.exit`, one naming `item.plan.nosuch`, and one whose
  `outcome` is outside its item's set.
  Red when: a row's exit item is accepted without resolving its tag.
- **AC6** — When `python loop_table.py --fixture --plant dropped-row` runs, the fixture deletes B7
  while `item.build.exit` keeps routing its outcome to `transition`, and the check exits 1 naming
  `item.build.exit`; under `--plant unrouted-row` a row whose declared item routes that outcome to
  another item exits 1 naming the row.
  Red when: a `transition` route with no row, or a row no route reaches, passes.
- **AC7** — When `python loop_table.py --fixture --plant stand-in` runs, a B4 move prints
  `stand-in dRankedPlan`, and the check exits 1 naming a planted stand-in row for an item no row names
  and one whose `owner` differs from the item's.
  Red when: a stale stand-in row survives the check.
- **AC8** — When `grep -n '"loop transition tables"' tools/gate-legs.json` runs, it finds the leg row
  and its argv naming `loop_table.py check`.
  Red when: the leg row is absent or names another command, so no bar runs the check.
- **AC9** — When `grep -n 'loop_table.py move' loop.md` runs in `help/`, it finds the section naming the
  verb, and the section names `refused` and `stand-in`.
  Red when: the tables land and the page still describes the steps alone.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest`

New arm: tools/loop/loop_table.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the `loop transition tables` leg over the tree, its failing case staged by deleting row B7 · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-24: the tuple
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

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 13, flow-steps' `[transitions]` table
  at base `ed497191`, the orientation record's unit steps and C2-F8.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-52, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.

## 10. Reuse audit

No existing seam fits a declared transition table. `python tools/codebase-map/reuse_lookup.py "refuse
a state transition that the declared transition table lacks"` ranked name stems only: `declares`,
`CensusRefused`, `plan_state` and `derive_transition` in `tools/memory-tree/transition_audit.py`. The
last is the backlog-mode merge audit, a name collision this unit's module name avoids. The closed-set
refusal it extends as a pattern is unattended's: the phase membership test in `verb_phase`
(`tools/unattended/unattended.sh:6140-6143`), `phases()` at :1069 and `refuse_if_terminal` at :4387,
each verified at base. The scout record's line range for the flow table, 721-775, is the section's;
its rows sit at flow-steps.md:729-763, which this spec cites. The query `python
tools/memory-recall/query.py "how is a phase transition refused when it is not in the vocabulary"`
returned the scout rows, `TOOL-aStandingWrit-1`'s review of `verb_phase` admitting any terminal, and
`TOOL-cFinalBerth-1`'s finding that it never read the current phase; both agree with source now.

Recall terms used: transition table phase vocabulary refuse verb_phase PHASES_CORE terminal fixture witness exit item stand-in
