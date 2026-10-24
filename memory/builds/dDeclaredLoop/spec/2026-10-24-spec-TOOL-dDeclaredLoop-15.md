# TOOL-dDeclaredLoop-15 — the build table's terminal states, and `deps.on-parent-withdrawn` routing a withdrawn parent

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 12 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0100@4771709c whole
**Carries:** node:policy-key.deps.on-parent-withdrawn

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |

<!-- /gen:spec-records -->

## 1. Goal

The build table gains the terminal states flow-steps' `[transitions]` declares, with the rows into
them and a refusal of any move out of one. And a parent's `withdrawn` post read at an item boundary
routes the build as `deps.on-parent-withdrawn` says (v2:1252, the owner's FK-4-3): `replan` by a plan
revision back to planning, `adopt-parent-work` by that revision taking the parent's kept units in
through `design.inventory` at the parent's kept branch's tip, and `withdraw-too` by an owner item
proposing the build's withdrawal, never withdrawing it by a command. Today a parent's end reaches no
child: terminal phases are LANDED and ABORTED only (`tools/unattended/unattended.sh:853`), and
`parents:` is read for the index's edges alone (`tools/memory-tree/gen_build_index.py:1204`).

## 2. Scope (IN)

- **S1** — The terminal set, `terminal` in `[states]` of `tools/loop/loop.toml`: the nine states
  flow-steps' table names terminal
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:765`), listed in
  §4 "### The terminal set". Observed by AC1.
- **S2** — The refusals over it, added to `check_transition_tables`: a terminal in any row's `from`, a
  terminal also in a level's open states, and `@open` expanding to a terminal are each red, so no
  move leaves a terminal. Observed by AC1.
- **S3** — The rows into each terminal but `incomplete`, T1 to T12 in §4, from flow-steps.md:732-734,
  :737-740, :755 and :762-763, including the Deploy exit's row that `TOOL-dDeclaredLoop-13`'s step-exit
  join leaves to this unit. Observed by AC2.
- **S4** — The parent row P1, from flow-steps.md:746: designing, building or deploying, before the
  push, to `planning` on the plan revision, which `replan` and `adopt-parent-work` both take.
  Observed by AC3 and AC4.
- **S5** — The parent read: `read_withdrawn_parents(build, root)` in `tools/loop/loop_parents.py`
  over the slugs of the build README's `parents:` front matter. The `withdrawn` post and the mailbox
  are dPlacedRequest's and dWellOiledMachine's, so the read takes today's stand-in: a parent whose
  `memory/builds/<parent>/RUN.md` holds `phase: ABORTED`, which `TOOL-dDeclaredLoop-1`'s mapping reads
  as `withdrawn`. Observed by AC3 and AC6.
- **S6** — The route: `derive_parent_route(build, state, root)` and `python
  tools/loop/loop_parents.py route --build <slug> --state <state>`, reading `deps.on-parent-withdrawn`
  through dGroundRules-2's `resolve` with the catalogue default `replan` until it lands. Each value's
  answer is §4's table: a move through P1, the same move with the parent's kept tip as
  `design.inventory`'s input, or an owner item and no move. Observed by AC3, AC4, AC5 and AC7.
- **S7** — The leg `loop parent routes`, running `loop_parents.py --selftest`, with the rows a new
  leg owes, and a section of `help/loop.md`. Observed by AC8.

## 3. Non-goals (OUT)

- No `incomplete` or `parked` row: `TOOL-dDeclaredLoop-31`'s endings. `incomplete` is in the set
  here, so its rows are checked once they land.
- No `withdrawn` post, mailbox or item-boundary reader: dPlacedRequest's and dWellOiledMachine's. The
  executor calls the route at each item boundary; until it lands, `route` is the stand-in a mover
  calls.
- No `design.inventory`: dIndexedDesign's item. The route names its input, and the item stays on
  `TOOL-dDeclaredLoop-13`'s stand-in list.
- No withdrawal by a command, under any value: `withdraw-too` proposes it to the owner.
- No write: the route prints its answer, and the caller records the move through
  `TOOL-dDeclaredLoop-3`'s writer or files the owner item.
- No `superseded` link move: flow-steps' `[rules]` gives it to `deploy.parents`, not to this clause.
- No catalogue row: dGroundRules-1 S3 writes `deps.on-parent-withdrawn`'s (I10).

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-13` — the `loop.toml` transition rows and `[states]`, to which the terminal set, T1 to T12 and P1 are added, and `derive_move`, which P1's move goes through
- **consumes-from** `TOOL-dDeclaredLoop-16` — `record-kind.disposition`, the owner's record that alone leaves the owner item `withdraw-too` raises

## 4. Design

### The terminal set

```toml
[states]
terminal = ["landed", "withdrawn", "superseded", "incomplete", "deferred", "retired", "refused", "merged", "answered"]
```

### The terminal rows

| Row | From | Item | Outcome | To | Source |
|---|---|---|---|---|---|
| T1 | none | `item.plan.dedupe` | a patch re-placed: continue, amend or patch | merged | :732 |
| T2 | none | `item.plan.dedupe` | a patch re-placed: ask | deferred | :733 |
| T3 | none | `item.plan.dedupe` | a patch re-placed: none | answered | :734 |
| T4 | planning | `item.plan.triage-rule` | defer | deferred | :737 |
| T5 | planning | `item.plan.triage-rule` | retire | retired | :737 |
| T6 | planning | `item.plan.triage-rule` | refuse | refused | :737 |
| T7 | planning | `item.plan.dedupe` | re-placed: continue, amend or patch | merged | :738 |
| T8 | planning | `item.plan.dedupe` | re-placed: ask | deferred | :739 |
| T9 | planning | `item.plan.dedupe` | re-placed: none | answered | :740 |
| T10 | deploying | `item.deploy.close` | pass | landed | :755 |
| T11 | `@open`, when before-push | `item.life.close` | withdrawn | withdrawn | :762 |
| T12 | `@open`, when before-push | `item.life.close` | superseded | superseded | :763 |

The re-placement rows carry the placement's value as `disposition`, a value of
`record-kind.disposition`'s closed set (I9). The outcome words are the flow record's, and the build
pass takes the spelling `TOOL-dDeclaredLoop-12`'s item rows carry, as `TOOL-dDeclaredLoop-13` §4 says.

### The parent row and the route

```toml
[[transition]]            # P1
level = "build"
from = ["designing", "building", "deploying"]
item = "item.plan.record"
outcome = "revised"
to = "planning"
when = "before-push"
witness = "the parent's post or the hold's record, and the plan revision"
```

| `deps.on-parent-withdrawn` | The route's answer | What it never does |
|---|---|---|
| `replan` (default) | `route replan · move <state> → planning · item.plan.record` | keep building on the withdrawn parent's interface |
| `adopt-parent-work` | the same move, and `inventory <parent> <sha>`: the parent's kept branch tip, the input `design.inventory` takes the parent's kept units from | adopt units from any other tree |
| `withdraw-too` | `owner-item · propose item.life.close withdrawn · left by record-kind.disposition`, and no move | withdraw the build, or move its state |

The kept branch is the ref the parent's RUN.md fact `run-branch:` names, resolved to its tip; a parent
with no such ref answers `adopt-parent-work` with exit 2, `no kept branch`, rather than an empty
inventory. A state P1 does not admit, `planning` or `testing`, answers `route <value> · held:
<state> admits no parent row`, so a withdrawal read in Test waits for its next row. The owner item is
the proposal only; its disposition is the owner's record, so no value of this key ends the build.
The flow record's other trigger for P1, a parent hold past `flow.wait-ceiling`, is
`TOOL-dDeclaredLoop-33`'s wait and is not read here.

```
python tools/loop/loop_parents.py route --build <slug> --state <state> [--root <path>]
python tools/loop/loop_parents.py --selftest
python tools/loop/loop_parents.py --fixture --plant <case> [--value <v>]
```

`route` exits 0 with its answer, or `route none` when no parent reads withdrawn; 2 on an unreadable
`parents:` slug, an unknown state, or a policy value the reader refuses.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/loop_parents.py` | module | none declared for files |
| `read_withdrawn_parents` | function | `py.function`, OK |
| `derive_parent_route` | function | `py.function`, OK |
| `terminal` | key of `[states]` | none |
| T1 to T12, P1 | `[[transition]]` rows | none |
| `loop parent routes` | leg | none |

### Migration

None: no build has a recorded state yet.

### Rollout

Live on landing, read-only. Nothing acts on a route until a mover records the move it names.

### Files touched (estimate)

- `tools/loop/loop.toml`
- `tools/loop/loop_table.py`: the terminal refusals in `check_transition_tables`
- `tools/loop/loop_parents.py`
- `tools/loop/kit.toml`: the module and the leg declared
- `tools/gate-legs.json`: the leg `loop parent routes`, argv `python {prefix}/loop/loop_parents.py --selftest`
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `tools/run-gates/ceiling-evidence.txt`, the new leg's row
- `memory/map/features/loop.md`: the module's claim and the leg in its `gate-legs` list
- `help/loop.md`: the terminal states and the parent route

### Alternatives rejected

- **Reading the parent's derived phase through unattended's `read_derived_phase`**
  (`tools/unattended/unattended.sh:1439`). It is a shell function of another kit; the stand-in needs
  only the producer-written terminal fact, which `--abort` alone writes.
- **`withdraw-too` filing a parked decision itself.** That makes a read-only route a write path into
  another kit's record; the caller files the owner item it prints.

## 5. Production-readiness checklist

- security — read-only: the route reads front matter, run-state facts and the policy value, and
  writes nothing.
- perf / scale — one front-matter read and one run-state read per parent.
- error / empty / loading states — no `parents:` key answers `route none`; an unreadable parent slug
  or a refused policy value exits 2, never `none`.
- observability — every answer names the parent, the value it read and the move or proposal.
- risks — the ABORTED stand-in reads a run's record, not a post: a parent aborted for a reason it
  later resumes from reads withdrawn until its next run, and the post of dPlacedRequest replaces it.
- testing — the plants of §6 under the new leg.
- migration — none.
- user docs — `help/loop.md` (S7).

## 6. Acceptance criteria

- **AC1** — When `python loop_table.py check` runs on the built tree, it prints the nine terminals and
  exits 0, and under `python loop_table.py --fixture --plant terminal-from`, a row whose `from` is
  `landed`, and `--plant terminal-open`, `landed` also in the build's open states, it exits 1 naming
  each.
  Red when: a move out of a terminal passes the check.
- **AC2** — When `python loop_table.py move --level build --from deploying --item item.deploy.close
  --outcome pass` runs, it names `landed`; `--from planning --item item.plan.triage-rule --outcome
  retire` names `retired`; and `--from building --item item.life.close --outcome withdrawn --fact
  pushed=no` names `withdrawn`, the same with `pushed=yes` exiting 1.
  Red when: a terminal row admits a move after the landing push, or a terminal is unreachable.
- **AC3** — When `python loop_parents.py --fixture --plant withdrawn-parent --value replan` runs, whose
  build sits in `designing` with a parent whose RUN.md reads `phase: ABORTED`, it prints `route
  replan · move designing → planning · item.plan.record`.
  Red when: the parent's withdrawal is not read in Design, so the route prints `route none`.
- **AC4** — When the same plant runs with `--value adopt-parent-work`, it prints the AC3 move and
  `inventory` naming the parent and the tip of the parent's `run-branch:` ref, and with that ref
  deleted it exits 2 printing `no kept branch`.
  Red when: the parent's kept units are taken from any tip but its kept branch's.
- **AC5** — When the same plant runs with `--value withdraw-too`, it prints `owner-item` proposing
  `item.life.close withdrawn`, prints no `move`, and the fixture's commit count and RUN.md bytes are
  unchanged.
  Red when: the value withdraws the build or moves its state.
- **AC6** — When the fixture runs with `--plant live-parent`, the parent's RUN.md reading `phase:
  BUILDING`, `route` prints `route none`, and with `--plant no-parents` it prints the same.
  Red when: a live parent reads withdrawn.
- **AC7** — When the plant runs with no `--value` and no policy file, the answer is AC3's, the
  catalogue default `replan`; with the policy file setting `deps.on-parent-withdrawn = "bogus"`, it
  exits 2 naming the key.
  Red when: an unknown value falls back to a route instead of refusing.
  fixture: the clone carries dGroundRules' reader and the key's catalogue row.
- **AC8** — When `grep -n '"loop parent routes"' tools/gate-legs.json` runs, it finds the leg row and
  its argv naming `loop_parents.py`, and `grep -n 'deps.on-parent-withdrawn' loop.md` in `help/` finds
  the section.
  Red when: the leg row is absent or names another command, so no bar runs the check.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest`

New arm: tools/loop/loop_table.py · covers AC1 AC2 · the `loop transition tables` leg's `--selftest`, its failing case staged by the `terminal-from` plant · none

New arm: tools/loop/loop_parents.py · covers AC3 AC4 AC5 AC6 AC7 AC8 · the `loop parent routes` leg, its failing case staged by a `withdrawn-parent` plant whose reader skips the parent's run-state file · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-24: the tuple
  does not hold `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it. RESOLVED (agent,
  2026-10-24, delegated): `OPEN`.
- **F2 — Which item fires the parent row, when the flow record names an event, not an item?** The row's
  witness is "the parent's post or the hold's record, and the plan revision" (flow-steps.md:746), and
  `replan` routes "by a plan revision back to planning" (v2:1252). RESOLVED (agent, 2026-10-24,
  delegated): `item.plan.record`'s `revised` outcome, the plan revision, rung 1.
- **F3 — Does the route write the move or the owner item?** Options: (a) print the answer, the caller
  recording it; (b) record the move and file the owner item itself. (b) adds a write path into two
  other units' doors. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, and the clause's "never
  withdrawing it by a command" holds by construction.
- **F4 — What stands in for the parent's `withdrawn` post?** RESOLVED (agent, 2026-10-24, delegated):
  the parent's RUN.md `phase: ABORTED`, the brief's named stand-in and `TOOL-dDeclaredLoop-1`'s
  mapping of ABORTED to `withdrawn`, rung 1.

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 15, flow-steps' `[transitions]` and
  `[rules]` at base `ed497191`, v2:1252 and FK-4-3.

## 10. Reuse audit

The seams extended are `TOOL-dDeclaredLoop-13`'s tables and check, by rows and three refusals, and the
`parents:` front-matter key the index already reads (`tools/memory-tree/gen_build_index.py:1204`,
inverted for children at :2615), both verified at base. The terminal stand-in is the run-state fact
`--abort` alone writes: `PHASES_TERMINAL="LANDED ABORTED"` at `tools/unattended/unattended.sh:853`, and
`verb_phase` refuses a terminal target (:6177-6180). `python tools/codebase-map/reuse_lookup.py "route a
build when its parent build is withdrawn"` ranked name stems only (`build`, `build_commit`,
`build_fixture`), so no seam fits the route, which is new. `python tools/memory-recall/query.py "what
happens to a build when its parent build is aborted or withdrawn"` returned the scout row, v2's row
for the key, FK-4-3's options and `TOOL-dHonouredPark-10`'s note that an ABORTED run's record stays in
the tree; none disagrees with source. The scout cited `read_derived_phase --prime` at :1443; the
function opens at :1439 and its prime branch at :1443.

Recall terms used: parents front matter withdrawn ABORTED terminal replan adopt-parent-work withdraw-too owner item read_derived_phase
