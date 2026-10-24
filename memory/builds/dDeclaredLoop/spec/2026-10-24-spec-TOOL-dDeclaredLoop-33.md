# TOOL-dDeclaredLoop-33 — the static termination check on every composition, at the push and at each step boundary

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 34 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0118@4c8ef789 whole

**Carries:** node:policy-key.flow.wait-ceiling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-c.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-34 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-34 |

<!-- /gen:spec-records -->

## 1. Goal

Every composition a build can run, gov's packs with the repository's overlay, the scenarios it was placed
under and its own recorded changes, is checked before it runs: every state reaches a terminal, every item is
reachable, every cycle passes a counted edge, every wait declares an outcome and a deadline, scenario
successor chains are acyclic, a raise of a loop bound is a loosening, and every approval item that would
loosen a value recommends the decline. Soundness alone failed on a planted repository stage that routed back
into itself with an exit (stall-and-loop.md:146-148), so the counted-edge rule is its own. The check runs at
the push and at each step boundary a build moves. Today nothing checks that a flow can finish
(`gap-flow-24`, C2-F13, P39).

## 2. Scope (IN)

- **S1** — `check_termination(composition)` in `tools/loop/termination.py`, returning one finding per broken
  rule, each naming its rule, its row or item and why, and the CLI `python tools/loop/termination.py check
  [--build <slug>]`, which composes as `TOOL-dDeclaredLoop-28` S6 composes a build, dOrderedCharter-35's
  `compose_rows` over gov's packs, the overlay, the scenarios `compose_scenarios` (`TOOL-dDeclaredLoop-27`)
  places and the build's applied changes, prints every finding and the pending count, and exits 1 on a
  finding. Observed by AC1 to AC12.
- **S2** — Rule `terminal`: every state of the build, feature and unit transition tables reaches a terminal
  state, by reverse reachability from the terminal set; an empty state set is a finding and never passes.
  Observed by AC2, AC4.
- **S3** — Rule `reachable`: every item is reached from its step's entry by the item routes and the needs
  graph. Observed by AC3.
- **S4** — Rule `counted`: with every counted edge and every owner edge set aside, the transition tables and
  the item routes are acyclic, through `find_cycles` in `tools/lib/needs_graph.py`, the helper
  `TOOL-dDeclaredLoop-12` extracts (I14), with the reachability walk added beside it. A counted edge is a
  `[[transition]]` row or item route whose `draws`, the field `TOOL-dDeclaredLoop-31` adds, names one of
  I19's causes; an owner edge is a row carrying a `disposition` or a route taken by an owner actor. This unit
  sets `draws` on each existing row and route that repeats work, its cause the one `TOOL-dDeclaredLoop-30`'s
  draw site records for that repetition. Observed by AC1.
- **S5** — Rule `wait`: every `[[item]]` row (`TOOL-dDeclaredLoop-12`) or transition row whose outcome set
  holds `awaiting` declares `deadline`, a value or
  a policy tag such as `policy.flow.wait-ceiling`, and `on-deadline`, the route it takes past it. A wait whose
  deadline key belongs to a build that has not landed is a row of the shrink-only list
  `tools/loop/termination-pending.txt`, naming that build; a row whose key has landed is a finding as stale.
  `flow.wait-ceiling`, 72 hours by v2's catalogue default until dGroundRules' reader lands, is the deadline
  gov's own waits declare. Observed by AC5.
- **S6** — Rule `scenario`: the successor chains of the composition's scenarios, each scenario row's `then`
  (`TOOL-dDeclaredLoop-27`), are acyclic, through the same helper. Observed by AC6.
- **S7** — Rule `raise`: a row of a build's recorded changes (`TOOL-dDeclaredLoop-28` S3) that raises a field
  named by a key the catalogue's loop-bound and deadline rule selects, dGroundRules-11's `derive_bounds`, is
  a loosening: its `rescope · flow-state` row reading `applied` under `flow.adapt` is a finding, and
  `held` passes. The four populations are the budget (`route-back-count`), a round count, a retry count and
  a deadline. Observed by AC7.
- **S8** — Rule `widening`: a raise of a loop-bound field in the overlay appears in the composition's widening
  list, dOrderedCharter-36's `derive_widenings`, so the overlay's update report names it; a raise the list
  lacks is a finding. Observed by AC8.
- **S9** — Rule `decline`: every approval item holding a loosening for the owner, a `rescope · flow-state`
  row reading `held · class loosening` (`TOOL-dDeclaredLoop-28` S5), recommends the decline; a held loosening
  recommending anything else, or nothing, is a finding. `apply_changes` gains the field ` · recommend decline`
  on every such row it writes. Observed by AC9.
- **S10** — The push. A leg `loop termination` in `tools/gate-legs.json` runs `python
  tools/loop/termination.py check` over gov's composition and over every live build's, its guard
  `{prefix}/loop/`, carrying `enforces = ["principle.p39"]` and the `stage` claim every leg carries.
  Observed by AC10.
- **S11** — The step boundary. `apply_changes` (`TOOL-dDeclaredLoop-28` S5), which runs before the transition
  into a step is recorded, calls `check_termination` on the build's composition with its newly applied
  changes, and the transition is refused on a finding, naming it. Observed by AC11.
- **S12** — The waits outside the composition, named. `tools/loop/README.md` lists the code-level waits the
  check does not grade, with each one's declared deadline: `CLAIM_WAIT_CEILING=120` seconds at
  `tools/push-main.sh:303`, the lander's wait on a claim lock. Observed by AC12.
- **S13** — The suite arm the `New arm:` line in §7 declares, one case per planted break. Observed by AC1 to
  AC9 through that line, RED first at the close.

## 3. Non-goals (OUT)

- The tables, items, scenarios and recorded changes the check reads: `TOOL-dDeclaredLoop-13`, `-12`, `-27`
  and `-28`'s. The check reads the composition and refuses on it; it writes no row of any of them, except the
  one default S9 names.
- The budget and the endings: `TOOL-dDeclaredLoop-30` and `-31`'s. The check reads `draws` and the ending
  rows, which make a counted edge and a terminal path.
- A run-time detector. Progress, leases and the wait graph across builds are a later build's supervisor; this
  is the static half.
- Nested spawns drawing from a parent's reservation, which stall-and-loop.md:241 lists beside these rules:
  the clause does not name it, and the reservation is a later build's.
- Re-pointing `CLAIM_WAIT_CEILING` or the driver's process ceilings (`WIRING_CEILING`, `PREFLIGHT_CEILING`,
  `tools/unattended/unattended.sh:697-698`). The first is a wait with a declared deadline already; the others
  bound a process, not a wait on another party.
- The overlay's update report itself and the widening classifier: dOrderedCharter's. S8 joins to them.
- No help page: `help/` does not document the loop kit.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-12` — `needs`: `find_cycles` in `tools/lib/needs_graph.py`, which the
  counted-edge and scenario rules call, and the needs graph the reachable rule walks
- **consumes-from** `TOOL-dDeclaredLoop-27` — `scenario`: `compose_scenarios` and each scenario's `then`, the
  successor chain the scenario rule walks
- **consumes-from** `TOOL-dDeclaredLoop-28` — `flow.adapt`: the recorded changes, their `rescope · flow-state`
  rows and `apply_changes`, the step boundary the check is called from
- **consumes-from** `TOOL-dDeclaredLoop-30` — `flow.rework-budget`: the `draws` causes that make an edge
  counted, and the budget a raise loosens
- **consumes-from** `TOOL-dDeclaredLoop-31` — `flow.on-exhausted`: the ending rows that give every open state a
  path to `incomplete`, and the owner edge out of `parked`

## 4. Design

### The rules

| Rule | Reads | Finding |
|---|---|---|
| `terminal` | each transition table's states and rows, and its terminal set | a state with no path to a terminal; an empty state set |
| `reachable` | each step's items, routes and needs | an item no route or need reaches from the step's entry |
| `counted` | the tables and item routes, with `draws` and owner triggers | a cycle left after counted and owner edges are dropped |
| `wait` | every row or item whose outcomes hold `awaiting` | no `deadline` or no `on-deadline`; a stale pending row |
| `scenario` | each scenario's successor | a successor cycle |
| `raise` | the build's recorded changes, the catalogue's bounds | a raise applied without the owner |
| `widening` | the overlay's loop-bound fields, `derive_widenings` | a raise the widening list lacks |
| `decline` | each held loosening's recommendation | a held loosening not recommending `decline` |

Each rule is one function, `check_<rule>(composition)`, so each is its own arm and a fixture that breaks one
rule reds that rule alone. The planted repository stage that routes back into itself with an exit passes
`terminal` and `reachable` and is caught only by `counted`, which is the clause's discriminating case
(stall-and-loop.md:146-148, P5).

### Counted and owner edges

```
counted(edge) = edge.draws in {route-back, fix-pass, review-round, re-dispatch, research, patch:<slug>}
owner(edge)   = edge.on == "record-kind.disposition" or edge.actor == "owner"
check_counted: graph = every edge not counted and not owner; acyclic(graph) or a finding per cycle
```

A counted edge draws on a budget that ends at `flow.on-exhausted`, so a loop through it terminates; an owner
edge waits on the owner, which the `wait` rule bounds. A row marked `draws = "none"`, such as
`TOOL-dDeclaredLoop-31`'s revert row, is not counted. The cycle is reported with the helper's canonical
rotation, so one cycle found from three entries is one finding, as `_scan_cycles` reports it today
(`tools/memory-tree/backlog.py:1271-1291`).

### The raise

```
bounds = derive_bounds(catalogue rows)          # dGroundRules-11: LOOP_BOUND_TYPES and DEADLINE_TYPES
for change in the build's recorded changes:
  if change.key in bounds and change.value > gov's value:
    change.state == applied      -> finding (raise applied unattended)
    change.state == held-owner   -> pass
```

`flow.rework-budget`'s `<base>+<per-unit>` compares base and per-unit each; a raise of either is a raise.
Every row of the bound population carries `direction = "raise-loosens"` (dGroundRules-11 S4), which is the
reason a raise can never be "only stricter" under `flow.adapt`'s `additive-recorded`.

### The pending list

```
# tools/loop/termination-pending.txt — shrink-only
wait · <row or item> · <deadline key> · <build that lands it>
```

An owner gate's deadline is `run.owner-deadline`, a later build's key; until it lands, every owner wait is a
pending row naming that build, and the check prints the count on every run. A row whose key the catalogue now
marks landed is stale and is a finding, so the list only shrinks.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_termination` and the eight `check_<rule>` functions | Python functions, `tools/loop/termination.py` | `py.function`, verb-first |
| `tools/loop/termination-pending.txt` | shrink-only list | none |
| `deadline`, `on-deadline` | item and row fields | none |
| `recommend` | `rescope · flow-state` row field, `decline` on a held loosening | none |
| `loop termination` | gate leg | leg name |

### Migration

None. The rules read rows other units declare; a composition the check reds is one no build could finish.

### Rollout

The leg lands with the check. Gov's own composition must be green at landing with every owner wait on the
pending list, which AC10 observes.

### Files touched (estimate)

- `tools/loop/termination.py`
- `tools/loop/termination-pending.txt`
- `tools/loop/selftest.py`
- `tools/loop/README.md`
- `tools/gate-legs.json`
- `tools/loop/adapt.py`
- `tools/loop/loop.toml`

The step-boundary call and the ` · recommend decline` field sit in `apply_changes`, in
`TOOL-dDeclaredLoop-28`'s `tools/loop/adapt.py`, and the `draws` values in the `[[transition]]` rows and item
routes of `tools/loop/loop.toml`.

### Alternatives rejected

- **Soundness alone: every state reaches a terminal and every item is reachable.** A planted stage with an
  exit passed it while its uncounted self-loop survived (P5).
- **Default a wait with no deadline to `flow.wait-ceiling`.** The clause requires each wait to declare one;
  a silent default makes a forgotten deadline indistinguishable from a chosen one.
- **A third cycle primitive here.** `TOOL-dDeclaredLoop-12` extracts the one helper from
  `derive_install_order` and `_scan_cycles`; this unit adds the counted-edge filter and the reachability walk
  beside it.

## 5. Production-readiness checklist

- security — read-only over composed rows; no write path beyond the one default field S9 names.
- perf / scale — each rule is linear in rows and edges, O(V+E), per composition (stall-and-loop's prior art);
  the leg composes gov's and each live build's.
- error / empty / loading states — an empty state set is a finding; an unreadable composition exits 2 naming
  the reader's refusal, never 0.
- observability — every finding names its rule and row; the pending count prints on every run.
- risks — the check trusts `draws` as declared; a row that should draw and is marked `none` hides a loop,
  which is `TOOL-dDeclaredLoop-30`'s draw sites to keep honest.
- testing — the pass probes each `check_<rule>` on a planted composition; the arm in §7 is observed RED then
  GREEN by the main loop.
- migration — none.
- user docs — `tools/loop/README.md`; no help page covers the loop kit.

## 6. Acceptance criteria

- **AC1** — When `python termination.py check` runs over a planted composition holding a repository stage
  whose exit leads to a terminal and whose other row routes back into itself with no `draws`, it prints one
  finding, rule `counted`, naming that row, and no `terminal` or `reachable` finding; with the self-row marked
  `draws = "route-back"` it exits 0.
  Red when: the counted-edge rule is absent, so the planted stage passes on soundness alone.
- **AC2** — When the planted composition holds a stage with no path to a terminal, the check prints a
  `terminal` finding naming the stage.
  Red when: reachability is computed forward from the entry, so a dead-end stage still passes.
- **AC3** — When the planted composition declares an item no route or need reaches, the check prints a
  `reachable` finding naming the item.
  Red when: the walk starts from every item rather than the step's entry, so the orphan reaches itself.
- **AC4** — When the planted composition's build table declares no states, the check exits 1 with a
  `terminal` finding naming the empty set.
  Red when: an empty table passes because no state fails.
- **AC5** — When a planted item whose outcomes hold `awaiting` declares no `deadline`, the check prints a
  `wait` finding; with `deadline = "policy.flow.wait-ceiling"` and an `on-deadline` route it passes; and a
  pending-list row whose key the planted catalogue marks landed prints a stale finding.
  Red when: a wait with no deadline passes.
- **AC6** — When two planted scenarios each name the other as successor, the check prints one `scenario`
  finding naming both.
  Red when: the cycle is reported twice, once from each entry.
- **AC7** — When a planted build's recorded changes apply, unattended, a raise of `flow.rework-budget` from
  `4+2` to `6+2`, of `review.max-rounds` from 3 to 5, of `roles.retries` from 2 to 4 and of
  `flow.wait-ceiling` from 72 to 96, each in its own fixture, the check prints one `raise` finding per fixture
  naming the key; the same four held for the owner pass.
  Red when: a deadline raise is missed because only count types are read.
  figure: the four gov values are PINNED to v2's catalogue defaults at base `ed497191`.
- **AC8** — When a planted overlay raises a loop-bound field of an item and the planted widening list omits
  it, the check prints a `widening` finding; with `derive_widenings` listing it, it passes.
  Red when: the join reads the overlay text instead of the composition.
  permission: `derive_widenings` is a parent build's, landed before this unit's build run.
- **AC9** — When a planted held change raising `review.max-rounds` recommends `apply`, the check prints a
  `decline` finding; recommending `decline` it passes; and one with no recommendation prints the finding.
  Red when: a held loosening with no recommendation passes.
- **AC10** — When `python -c` loads `tools/gate-legs.json`, it finds a leg named `loop termination` whose
  command runs `termination.py check`, whose guard holds the loop kit's path and whose `enforces` holds
  `principle.p39`; and `python termination.py check` over this repository's composition exits 0 and prints the
  pending count.
  Red when: gov's own composition reds at landing, an owner wait off the pending list.
- **AC11** — When a planted build whose recorded change creates an uncounted cycle reaches its step boundary
  through `TOOL-dDeclaredLoop-28`'s `apply_changes`, the transition is refused naming the `counted` finding;
  without the change it is recorded.
  Red when: the step boundary moves without calling the check.
- **AC12** — When `grep -c 'CLAIM_WAIT_CEILING'` runs over the loop kit's README, it prints at least 1.
  Red when: the code-level wait is not named, so a reader takes the check to grade it.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 · one planted composition per rule and one per raised population, each staged against the base tree, which has no termination check · none

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

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 33, stall-and-loop.md:146-148 and :236-245,
  dGroundRules-11's bound population, dOrderedCharter-36's widening list, and the two cycle primitives and
  the push wait read at base `ed497191`.

## 10. Reuse audit

For the counted-edge rule no existing seam fits: `git grep -n -i "def .*cycle\|tarjan\|def .*reachab" --
tools` finds two cycle primitives, `_scan_cycles` (`tools/memory-tree/backlog.py:1271-1291`) and Kahn's order
in `derive_install_order` (`tools/govkit/govkit.py:911`), neither handling counted or owner edges, reachability
or a terminal. Both are what `TOOL-dDeclaredLoop-12` extracts into one helper, which this unit calls and
extends beside, never copies. The loosening population is dGroundRules-11's `derive_bounds`, the widening join
dOrderedCharter-36's `derive_widenings`, and the pending list the shape of dOrderedCharter-7's.

`python tools/codebase-map/reuse_lookup.py "check a state machine graph that every state reaches a terminal
and every cycle is counted"` ranked `check` and `counts` by name stem across self-test suites, and
`plan_state` (`tools/unattended/unattended.sh`); none walks a graph, so the probe confirms the gap.
`python tools/memory-recall/query.py "does anything check that a flow terminates and every loop is counted"`
returned the scout record's row for this unit, agreeing with source on both primitives and on
`CLAIM_WAIT_CEILING=120` at `tools/push-main.sh:303`, and the stall prior-art record's O(V+E) check, which §5
follows.

Recall terms used: termination counted edge cycle reachable terminal wait deadline CLAIM_WAIT_CEILING _scan_cycles derive_install_order acyclic
