# TOOL-dDeclaredLoop-15 — the build table's terminal states, and `deps.on-parent-withdrawn` routing a withdrawn parent

**Status:** DEFERRED · rev-4 · 2026-11-14 · node d · Tier-2 · base ed497191 · streams tooling · order 12 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0100@4771709c whole
**Carries:** node:policy-key.deps.on-parent-withdrawn

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-05-build-TOOL-dDeclaredLoop-15-deviation-151.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-15-deviation-151.md) | deviation | — |
| [2026-11-14-build-TOOL-dDeclaredLoop-15-deviation-152.md](../build/2026-11-14-build-TOOL-dDeclaredLoop-15-deviation-152.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md) | research | TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-15-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-15-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-15-reground-brief.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-15-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-33 |

<!-- /gen:spec-records -->

## 1. Goal

The build table gains the terminal states flow-steps' `[transitions]` declares, with the rows into
them that a declared route sends to `transition`, and a refusal of any move out of one. And a
parent's withdrawal, read by today's stand-in, routes the build as `deps.on-parent-withdrawn` says
(v2:1252, the owner's FK-4-3): `replan` by the parent row back to planning, `adopt-parent-work` by
that move with the parent's kept branch tip named as `design.inventory`'s input, and `withdraw-too`
by an owner item proposing the build's withdrawal, never withdrawing it by a command. Today no row
enters a terminal: the four routes this unit answers stand on `[[owed-row]]` rows of
`tools/loop/loop.toml`, and `parents:` is read for the index's edges alone
(`tools/memory-tree/gen_build_index.py#plan` inverts it into the child set).

## 2. Scope (IN)

- **S1** — The terminal set, the key `terminal` in `[states]` of `tools/loop/loop.toml`: the nine
  states flow-steps' table names terminal
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:765`), listed in
  §4 "### The terminal set" and read as the build level's (F6). `read_transition_rows` in
  `tools/loop/loop_table.py` returns it beside the levels, never as a level, and `check` prints it.
  Observed by AC1.
- **S2** — The refusals over it, in `check_transition_tables`: a terminal in any row's `from`, and a
  terminal also listed among the build level's open states, are each red, so no move leaves a
  terminal. A build row may enter a terminal. `derive_move` answers a move asked from a terminal with
  `TransitionRefused`, never a ValueError. Observed by AC1 and AC2.
- **S3** — The rows into a terminal, T1 to T5 in §4, each on a route the item rows send to
  `transition` or on `item.life.close`, with one `[[stand-in]]` row per new row item. The four
  `[[owed-row]]` rows whose `by` is this unit are answered by T1, T2, T3 and P1, and this pass deletes
  each. Observed by AC2 and AC3.
  **Readers:** by name: `tools/loop/loop_table.py`, its selftest's case `owed close`, which spells the
  owed row of `item.deploy.close`, rewritten by this pass as §4 says; `help/loop.md` and
  `tools/loop/README.md`, whose owed-row prose names the Deploy exit entering landed, rewritten by this
  pass · by value: `tools/loop/loop_table.py`, its function check_transition_tables, whose owed-row
  join compares each owed row with the cross-step routes and the build rows, and reds a row left
  beside the build row that covers it.
- **S4** — The parent row P1, from flow-steps.md:746: designing, building or deploying, on
  `item.deploy.parents`'s `withdrawn`, to `planning` (F5). Observed by AC2 and AC4.
- **S5** — The parent read: `read_withdrawn_parents(build, root)` in `tools/loop/loop_parents.py`, over
  the slugs of the build README's `parents:` front matter, read by the memory-tree kit's
  `parse_front_matter`. The `withdrawn` post and the mailbox are dPlacedRequest's and
  dWellOiledMachine's, so the read takes today's stand-in: a parent whose run-state file
  `<MEMORY_ROOT>/builds/<parent>/RUN.md` holds the run fact `phase: ABORTED`, which
  `TOOL-dDeclaredLoop-1` §4's phase table maps to `withdrawn`. Observed by AC4 and AC7.
- **S6** — The route: `derive_parent_route(build, state, root)` and `python
  tools/loop/loop_parents.py route --build <slug> --state <state>`, reading `deps.on-parent-withdrawn`
  through the policy kit's `resolve`, its catalogue default `replan`. Each value's answer is §4's
  table: P1's move, the same move with each withdrawn parent's kept tip as `design.inventory`'s input,
  or an owner item and no move. Observed by AC4, AC5, AC6 and AC8.
- **S7** — The leg `loop parent routes`, running `loop_parents.py --selftest`, gov's own
  `[[exempt_leg]]` (F8), with the rows a new leg owes, and a section of `help/loop.md`. The leg carries
  `enforces = ["principle.p21"]` (dOrderedCharter-7 S2). No v2 `[enforcement]` row names
  `cl-dClosedLoop-0100`, so the tag is settled by TOOL-dDeclaredLoop-3 §8 F7's rule, what the leg
  checks: a dependent build's route on its parent's withdrawal, which P21's "waits for its parent's
  landing only when it cannot reach them" (v2:927) governs. P20, whose text names the terminal states,
  fits the clause's first half, which `TOOL-dDeclaredLoop-13`'s leg `loop transition tables` checks.
  The pending list `tools/playbook/core-pending.txt` holds the row `principle principle.p21
  dKeptSession`, and this pass deletes it, as the meta-check reds a pending row whose item a leg now
  enforces. Observed by AC9.
  **Readers:** by name: `tools/playbook/core.py`, its meta-check verb, which reads the pending list
  and prints each row's arming build in its pending count · by value: NO VALUE READERS — a pending
  row's value is its arming build, which no reader compares, counts or derives from beyond that count.

## 3. Non-goals (OUT)

- No `incomplete` or `parked` row: `TOOL-dDeclaredLoop-31`'s endings. `incomplete` is in the set
  here, so its rows are checked once they land.
- No row into `deferred`, `retired`, `merged` or `answered`. Triage's `defer` and `retire` route to
  the backlog stand-in, and `item.plan.dedupe` routes no re-placement to `transition`, so a row on any
  of them reds the route join's backward arm (`check_transition_tables`). Each lands with the route
  dRankedPlan sends to `transition`. The states stay in the set (F9).
- No `withdrawn` post, mailbox or item-boundary reader: dPlacedRequest's and dWellOiledMachine's. Until
  the executor calls the route at each item boundary, `route` is the stand-in a mover calls.
- No `design.inventory`: dIndexedDesign's item. The route names its input.
- No withdrawal by a command, under any value: `withdraw-too` proposes it to the owner.
- No write: the route prints its answer, and the caller records the move through
  `TOOL-dDeclaredLoop-3`'s writer or files the owner item.
- No `superseded` link move: flow-steps' `[rules]` gives it to `deploy.parents`, not to this clause.
- No catalogue row: `deps.on-parent-withdrawn`'s row is in `tools/policy/catalogue.toml` already.
- No reading of a parent's planning ending (deferred, retired, refused or answered) as withdrawn,
  which `deploy.parents` names: those endings have no run-state fact today.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-13` — the `loop.toml` transition rows, `[states]`, the stand-in and owed lists, `derive_move` and `check_transition_tables`, to which the terminal set, T1 to T5, P1 and the refusals are added
- **consumes-from** `TOOL-dDeclaredLoop-16` — `record-kind.disposition`, the owner's record that alone leaves the owner item `withdraw-too` raises
- **hands-off** `TOOL-dDeclaredLoop-54` — the terminal set per level, which that unit declares and the termination rule reads (the round-1 spec audit's id 5)
- **hands-off** `TOOL-dDeclaredLoop-56` — the minors of the round-1 spec audit that land on this unit, ids 17, 62, each a scope item of that unit
- **hands-off** external — dRankedPlan: the rows into `deferred`, `retired`, `merged` and `answered`, once its triage and dedupe items route those outcomes to `transition`
- **hands-off** external — dWellOiledMachine: the item-boundary read of a parent's post, whose own row joins or replaces P1's `designing` and `building`

## 4. Design

### Evidence at HEAD

- `[states]` holds one key per level, `build`, `feature` and `unit`, and `read_transition_rows`
  (`tools/loop/loop_table.py#read_transition_rows`) reads every key as a level, so a `terminal` key is
  split out there before `check` and `derive_move` read the levels.
- `check_transition_tables` (`tools/loop/loop_table.py#check_transition_tables`) refuses a `to` that
  is neither a state of the row's level nor `@prior` or `@reentry`, and a row item that resolves to no
  `[[item]]` row and no `[[stand-in]]` row. Its backward join refuses a build row on a declared item
  whose outcome is no cross-step route, and its owed-row join refuses an owed row a build row covers.
- The item rows route these outcomes to `transition`: `item.plan.triage-rule` and
  `item.plan.triage-judge` on `refuse`, `item.deploy.parents` on `withdrawn`, `item.deploy.close` on
  `closed`, and `item.plan.place` on `unplaced` (dRankedPlan's owed row). Triage's `defer` and
  `retire` route to `stand-in:{prefix}/memory-tree/backlog.py`. `item.plan.dedupe`'s outcomes are
  `none`, `patch` and `duplicate`, and `duplicate` routes to the orienter stand-in.
- `item.plan.record`'s outcomes are `drafted`, `research` and `owner-question`, none routed to
  `transition`, so rev-3's P1 on its `revised` would red twice. `item.life.close` has no `[[item]]`
  row; flow-steps.md:689 gives it to dWellOiledMachine.
- `tools/loop/loop_table.py#main`'s selftest case `owed close` expects `loop: owed item.deploy.close ·
  closed · TOOL-dDeclaredLoop-15`, which S3 takes away.

### The terminal set

```toml
[states]
build = ["planning", "designing", "building", "testing", "deploying", "paused", "parked"]
feature = ["decomposed", "designed", "built", "tested", "deployed"]
unit = ["designed", "built", "tested", "deployed"]
terminal = ["landed", "withdrawn", "superseded", "incomplete", "deferred", "retired", "refused", "merged", "answered"]
```

`read_transition_rows` returns `terminal` as its own entry, an absent key reading as no terminal, and
the levels without it; a `terminal` that is no list of state words is the same LoopError a level's
list draws. `check` prints `loop: terminal build · <the states, space-separated>` after the level
lines. A row's `to` is admitted when it is a terminal and the row's level is `build`. A `from` naming
a terminal is refused as `<row> leaves <state>, a terminal: no move leaves one`, and a terminal in
the build list as `<state> is both an open build state and a terminal`. `@open` expands to the
level's list, so the second refusal is what keeps `@open` off a terminal. `derive_move` admits a
terminal as the asked state; since no row leaves one, it raises `TransitionRefused`, and `move` exits 1.

### The terminal rows

Each row sits in the transition block before the first `[[item]]` row, as `TOOL-dDeclaredLoop-13`'s
rows do. The outcome words are the item rows' own.

| Row | From | Item | Outcome | When | To | Source |
|---|---|---|---|---|---|---|
| T1 | planning | `item.plan.triage-rule` | refuse | | refused | :737 |
| T2 | planning | `item.plan.triage-judge` | refuse | | refused | :737 |
| T3 | deploying | `item.deploy.close` | closed | | landed | :755 |
| T4 | `@open` | `item.life.close` | withdrawn | before-push | withdrawn | :762 |
| T5 | `@open` | `item.life.close` | superseded | before-push | superseded | :763 |

Witnesses: T1 and T2 "the triage record", T3 "the transition record", T4 and T5 "the transition
record". The stand-in rows added: `item.plan.triage-rule` and `item.plan.triage-judge` owned by
dRankedPlan, `item.deploy.parents` and `item.deploy.close` by dShippedRelease, each its `[[item]]`
row's owner, and `item.life.close` by dWellOiledMachine. The four owed rows naming this unit are
deleted, leaving `item.plan.place`'s.

### The parent row and the route

```toml
# P1
[[transition]]
level = "build"
from = ["designing", "building", "deploying"]
item = "item.deploy.parents"
outcome = "withdrawn"
to = "planning"
witness = "the parent's post or the hold's record, and the plan revision"
```

No `when`: Design and Build precede the landing push, and in Deploy `item.deploy.parents` runs before
`item.deploy.land`, which needs it, so the row never holds after the push.

| `deps.on-parent-withdrawn` | The route's answer | What it never does |
|---|---|---|
| `replan` (default) | `route replan · parent <p> · move <state> → planning · item.deploy.parents` | keep building on the withdrawn parent's interface |
| `adopt-parent-work` | the same line, then `inventory <p> <sha>` per withdrawn parent: its kept branch tip, the input `design.inventory` takes its kept units from | adopt units from any other tip |
| `withdraw-too` | `route withdraw-too · parent <p> · owner-item · propose item.life.close withdrawn · left by record-kind.disposition`, and no move | withdraw the build, or move its state |

`<p>` names each withdrawn parent, space-separated, in `parents:` order. The move comes from
`derive_move("build", state, "item.deploy.parents", "withdrawn", {})`, so the route holds no list of
states of its own: a state P1 does not admit, `planning` or `testing`, answers `route <value> · parent
<p> · held: <state> admits no parent row`, and a withdrawal read in Test waits for its next row. The
owner item is the proposal only; its disposition is the owner's record, so no value ends the build.
The flow record's other trigger for P1, a parent hold past `flow.wait-ceiling`, is
`TOOL-dDeclaredLoop-33`'s wait and is not read here.

The kept branch is the ref the parent's run fact `run-branch:` names, else `branch-ref:` for a record
older than that fact, the order `resolve_holder_worktree` in `tools/unattended/unattended.sh` reads
them in, resolved to its commit by `git rev-parse --verify <ref>^{commit}` in `--root`. A parent with
neither fact, or a ref naming no commit, answers `adopt-parent-work` with exit 2, `no kept branch`,
never an empty inventory.

The reads, each through a seam that exists:

- The builds folder is `<root>/<MEMORY_ROOT>/builds`, `MEMORY_ROOT` from the memory-tree kit's
  `read_design_conf` (`tools/memory-tree/design_lib.py#read_design_conf`), `memory` where unset. Not
  `read_builds_dir`, whose `DESIGN_RECORD` condition marks the chain's tree, not every tree a
  `parents:` key lives in.
- `parents:` is read by `parse_front_matter` (`tools/memory-tree/gen_build_index.py#parse_front_matter`),
  imported through `read_memory_tree`, the one front-matter parser; its `Problem` exits 2. A slug
  naming no build folder exits 2, as the index's own inversion refuses it.
- A run fact is read by the policy kit's `read_run_fact` (`tools/policy/guard.py#read_run_fact`), the
  driver's `fact` grammar (F7). A parent with no run-state file reads live.
- The policy value is `resolve("deps.on-parent-withdrawn", root)`
  (`tools/policy/policy.py#resolve`), the landed revision's. Its `Refusal`, such as an invalid file with
  no valid revision before it (`tools/policy/policy.py#read_last_valid_value`), exits 2 naming the key.
- The policy kit is found by `resolve_kit_dir("policy", "policy.py", KIT)`; where it does not resolve,
  `route` exits 2 `unarmed`, never a default (F8).

```
python tools/loop/loop_parents.py route --build <slug> --state <state> [--root <path>]
python tools/loop/loop_parents.py --selftest
python tools/loop/loop_parents.py --fixture --plant <case> [--value <v>] [--state <s>]
```

`route` exits 0 with its answer, or `route none` when no parent reads withdrawn or the README has no
`parents:` key; 2 on an unreadable `parents:` slug, a state outside the build's open states, a policy
refusal, `no kept branch`, or an unresolved policy kit.

`--fixture` builds a scratch repository by `run_fixture_git` and `write_fixture_files`
(`tools/loop/loop_witness.py#run_fixture_git`, `tools/loop/loop_witness.py#write_fixture_files`): on
the branch `main`, a `.memory-tree.conf`, the child build `tChild` whose README's front matter names
`parents: tParent`, the parent's folder and README, and the parent's run-state file. `--value <v>`
commits `.governance/policy.toml` setting the key to `<v>` as the file's one revision; without it the
scratch holds no policy file. `--state` defaults to `designing`. The cases:

| Plant | The parent's run-state file |
|---|---|
| `withdrawn-parent` | `phase: ABORTED`, `run-branch:` naming `refs/heads/branch/tParent-run`, a branch the scratch holds |
| `no-kept-branch` | `phase: ABORTED`, its `run-branch:` ref deleted from the scratch |
| `live-parent` | `phase: BUILDING` |
| `no-parents` | the child README carries no `parents:` key |

It prints `loop: fixture · plant <case>`, `loop: fixture · kept <ref> <sha>` where the plant holds the
ref, then the route's lines, then `loop: fixture · tree unchanged` or `loop: fixture · tree changed`,
comparing `HEAD` and `git status --porcelain` before and after the route, and removes the scratch by
`remove_tree`. It exits as the route does. `--selftest` runs every case below through
`run_selftest_cases` (`tools/loop/loop_lib.py#run_selftest_cases`), the case loop
`loop_table.py` and `loop_checklist.py` share.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/loop_parents.py` | module | none declared for files |
| `read_withdrawn_parents` | function | `py.function`, OK |
| `derive_parent_route` | function | `py.function`, OK |
| `terminal` | key of `[states]` | none |
| T1 to T5, P1 | `[[transition]]` rows | none |
| `terminal-from`, `terminal-open` | plants of `loop_table.py` | none |
| `loop parent routes` | leg | none |

### Migration

None: no build has a recorded state yet.

### Rollout

Live on landing, read-only. Nothing acts on a route until a mover records the move it names.

### Files touched (estimate)

- `tools/loop/loop.toml`: `terminal`, T1 to T5, P1, five stand-in rows, four owed rows deleted, and the
  build-table comment that says no row enters a terminal
- `tools/loop/loop_table.py`: the split, the refusals, the terminal `to`, the terminal asked state, the
  two plants, the selftest cases, and its docstring
- `tools/loop/loop_parents.py`
- `tools/loop/kit.toml`: the comment block names the module, its reads and why it takes no edge
- `tools/loop/README.md`: the transition tables section, and the parent route
- `tools/gate-legs.json`: the leg `loop parent routes`, argv `python {prefix}/loop/loop_parents.py --selftest`, chunk `selftests`, subject `kit`, its `enforces` holding `principle.p21`
- `tools/govkit/registry.toml`: the leg's `[[exempt_leg]]` row
- `tools/govkit/usage.toml`: the module's usage rows
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `tools/run-gates/selftest-budgets.txt`: the leg's budget row
- `tools/playbook/core-pending.txt`: the row of `principle.p21`
- `memory/map/features/loop.md`: the leg in its `gate-legs` list
- `memory/map/generated/`, regenerated by the codebase-map kit's `gen_map.py --write`
- `memory/guides/SESSION-KICKOFF.md`: the manifest's audit stamp, since its watch list holds `tools/gate-legs.json`
- `help/loop.md`: the terminal states and the parent route

### Alternatives rejected

- **Reading the parent's derived phase through unattended's `read_derived_phase`**
  (`tools/unattended/unattended.sh#read_derived_phase`). It is a shell function of another kit; the
  stand-in needs only the producer-written terminal fact, which `--abort` alone writes:
  `PHASES_TERMINAL="LANDED ABORTED"` at `tools/unattended/unattended.sh@4344df262ed6:993`, and
  `verb_phase` refuses a terminal target (`tools/unattended/unattended.sh#verb_phase`).
- **`withdraw-too` filing a parked decision itself.** That makes a read-only route a write path into
  another kit's record; the caller files the owner item it prints.
- **Rows into `deferred`, `retired`, `merged` and `answered` now.** Each would be a build row on no
  cross-step route, which `check_transition_tables` reds; widening the triage and dedupe routes is
  dRankedPlan's program, not this unit's.

## 5. Production-readiness checklist

- security — read-only: the route reads front matter, run-state facts, a ref's tip and the policy
  value, and writes nothing; the fixture writes only its own scratch.
- perf / scale — one front-matter read, one run-state read per parent, one `rev-parse` per withdrawn
  parent under `adopt-parent-work`, and one policy read.
- error / empty / loading states — no `parents:` key answers `route none`; an unreadable slug, a state
  outside the open states, a refused policy value, a missing kept branch or an unresolved policy kit
  exits 2, never `none`.
- observability — every answer names the value read, each withdrawn parent and the move, the hold or
  the proposal.
- risks — the ABORTED stand-in reads a run's record, not a post: a parent aborted for a reason it
  later resumes from reads withdrawn until its next run, and dPlacedRequest's post replaces it. The
  policy value is the landed revision's, so a value set on an unlanded branch is not read. P1 fires
  on a Deploy item from Design and Build until dWellOiledMachine's boundary item lands (F5).
- testing — the plants of §4 under the new leg, and the two `loop_table.py` plants under
  `loop transition tables`. What each write could newly red, and what keeps it green:
  - `loop transition tables`: its `owed close` case is rewritten as a case on the line
    `loop: owed item.plan.place · unplaced · dRankedPlan`; the cases of AC1 and AC2 are added.
  - `loop definition` and `loop item kind`: neither reads `[states]`, the transition rows or the stand-in
    list, and no `[[item]]` row moves, since every new row sits before the first one.
  - `tags (the resolver's checks)`: its `resolves` arm reds a whole backticked span of tracked Markdown,
    outside fences, naming no row (`tools/playbook/tag_index.py#check_resolves`,
    `tools/playbook/tag_index.py#extract_citations`). `item.life.close` has no `[[item]]` row, so
    `help/loop.md` and `tools/loop/README.md` never write it as a bare backticked span; they spell it in
    a fenced block, as `help/loop.md` spells `item.life.request` today.
  - `install-prefix (shipped surface)`: the module and every kit-file edit spell `<prefix>` or a
    kit-relative name, never `tools/`, as `loop_table.py`'s docstring does.
  - `govkit selftest`, `govkit selfcheck` and `govkit refusal join`: the usage rows, the `[[exempt_leg]]`
    row and the regenerated subject pins answer the new leg and module.
  - `run-gates gov canary` and `measure-legs selftest`: the leg row carries a ceiling and the budget row
    its price; the ceiling is 120 seconds PINNED (an estimate at writing, 2026-11-14), re-priced from the
    main loop's first reading of the leg alone, as `TOOL-dDeclaredLoop-17`'s budget row was.
  - `core meta-check`: the leg's `enforces` and the deleted pending row move together.
  - `kickoff-manifest ratchet`: the pass commit carries a `manifest-audit:` trailer and the restamp.
  - `help page commands`: the new commands sit under `<!-- run: no -->` markers, as the section above
    them does, since they run a kit by its path in gov's checkout.
  - `codebase-map coverage + freshness`: the generated map is rewritten by `gen_map.py --write`.
  - Not touched: the memory-tree kit, so the verdict-epoch gate's delegate list moves nothing; no file
    names the build method, so `memory/project/method-carriers.txt` gains no row.
- migration — none.
- user docs — `help/loop.md` (S7).

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/loop_table.py check` runs on the built tree, it prints `loop:
  terminal build · landed withdrawn superseded incomplete deferred retired refused merged answered`
  and exits 0. Under `python tools/loop/loop_table.py --fixture --plant terminal-from`, a build row
  whose `from` is `landed`, it exits 1 printing `leaves landed, a terminal`, and under `--plant
  terminal-open`, `landed` appended to the build's open states, it exits 1 printing `landed is both`.
  Red when: a move out of a terminal passes the check, or `terminal` is read as a level.
- **AC2** — When `python tools/loop/loop_table.py move --level build --from deploying --item
  item.deploy.close --outcome closed` runs, it prints `move — build · deploying → landed ·
  item.deploy.close · stand-in dShippedRelease`. `--from planning --item item.plan.triage-judge
  --outcome refuse` names `refused`; `--from building --item item.life.close --outcome withdrawn --fact
  pushed=no` names `withdrawn`, the same with `pushed=yes` exiting 1; `--from designing --item
  item.deploy.parents --outcome withdrawn` names `planning`; and `--from landed --item item.life.request
  --outcome resume --fact prior=testing` exits 1 printing `refused — build · landed`.
  Red when: a terminal row admits a move after the landing push, a move leaves a terminal, or a
  routed terminal is unreachable.
- **AC3** — When `grep -c 'by = "TOOL-dDeclaredLoop-15"' tools/loop/loop.toml` runs, it prints `0`,
  and `python tools/loop/loop_table.py check` prints `loop: owed item.plan.place · unplaced ·
  dRankedPlan` as its one owed line and `loop: stand-in item.life.close · dWellOiledMachine`.
  Red when: an owed row stands beside the build row that answers it, or `item.life.close`'s rows stand
  on no stand-in row.
- **AC4** — When `python loop_parents.py --fixture --plant withdrawn-parent --value replan` runs in the
  loop kit, the child in `designing` and its parent's run-state file reading `phase: ABORTED`, it prints
  `route replan · parent tParent · move designing → planning · item.deploy.parents`; with `--state
  testing` it prints `held: testing admits no parent row`.
  Red when: the parent's withdrawal is not read in Design, so the route prints `route none`.
- **AC5** — When the same plant runs with `--value adopt-parent-work`, it prints the AC4 route line and
  `inventory tParent <sha>`, the sha its `loop: fixture · kept` line names, and `--plant no-kept-branch
  --value adopt-parent-work` exits 2 printing `no kept branch`.
  Red when: the parent's kept units are taken from any tip but its kept branch's.
- **AC6** — When the same plant runs with `--value withdraw-too`, it prints `owner-item · propose
  item.life.close withdrawn`, prints no `move`, and prints `loop: fixture · tree unchanged`.
  Red when: the value withdraws the build, moves its state or writes the tree.
- **AC7** — When `python loop_parents.py --fixture --plant live-parent` runs, the parent's
  run-state file reading `phase: BUILDING`, it prints `route none`, and `--plant no-parents` prints the
  same.
  Red when: a live parent reads withdrawn.
- **AC8** — When the `withdrawn-parent` plant runs with no `--value`, the scratch holding no policy
  file, its answer is AC4's, the catalogue default `replan`; with `--value bogus` it exits 2 naming
  `deps.on-parent-withdrawn`.
  Red when: an unknown value falls back to a route instead of refusing.
  fixture: the policy kit beside this kit, resolved by `resolve_kit_dir`; the scratch's one policy
  revision holds the bogus value, so no valid revision precedes it.
- **AC9** — When `grep -n '"loop parent routes"' tools/gate-legs.json` runs, it finds the leg row, its
  argv naming `loop_parents.py` and its `enforces` holding `principle.p21`; `grep -n
  'deps.on-parent-withdrawn' help/loop.md` finds the section; `grep -c 'principle.p21'
  tools/playbook/core-pending.txt` prints `0`; and `python tools/playbook/core.py meta-check` on this
  unit's pass prints `meta-check · green`.
  Red when: the leg row is absent or names another command, so no bar runs the check, or carries no
  `enforces`, which dOrderedCharter-7 S3's meta-check reds.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `loop transition tables` · `loop definition` · `loop item kind` · `tags (the resolver's checks)` · `core meta-check` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `playbook render selftest` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `kickoff-manifest ratchet` · `help page commands`

New arm: tools/loop/loop_table.py · covers AC1 AC2 AC3 · the `loop transition tables` leg's `--selftest`, its failing case staged by the `terminal-from` plant with the terminal branch of the `from` refusal taken out · none

New arm: tools/loop/loop_parents.py · covers AC4 AC5 AC6 AC7 AC8 · the `loop parent routes` leg, its failing case staged by the `withdrawn-parent` plant with `read_withdrawn_parents` reading no `phase` fact · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py#STATUS_TOKENS`). Observation, 2026-10-24: the
  tuple does not hold `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it. RESOLVED
  (agent, 2026-10-24, delegated): `OPEN`.
- **F2 — Which item fires the parent row, when the flow record names an event, not an item?** The row's
  witness is "the parent's post or the hold's record, and the plan revision" (flow-steps.md:746), and
  `replan` routes "by a plan revision back to planning" (v2:1252). RESOLVED (agent, 2026-10-24,
  delegated): `item.plan.record`'s `revised` outcome, the plan revision, rung 1. Re-settled at rev-4
  by F5: that item declares no `revised` and routes nothing to `transition`.
- **F3 — Does the route write the move or the owner item?** Options: (a) print the answer, the caller
  recording it; (b) record the move and file the owner item itself. (b) adds a write path into two
  other units' doors. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3, and the clause's "never
  withdrawing it by a command" holds by construction.
- **F4 — What stands in for the parent's `withdrawn` post?** RESOLVED (agent, 2026-10-24, delegated):
  the parent's RUN.md `phase: ABORTED`, the brief's named stand-in and `TOOL-dDeclaredLoop-1`'s
  mapping of ABORTED to `withdrawn`, rung 1.
- **F5 — Which item fires P1, now that `item.plan.record` declares no `revised`?** The one declared
  item whose `withdrawn` routes to `transition` is `item.deploy.parents`, a Deploy item that reads each
  parent's state. Options: (a) P1 on `item.deploy.parents`'s `withdrawn` from designing, building and
  deploying, the flow record's three states, the route verb standing in for the boundary read until
  dWellOiledMachine's item lands; (b) the same item from `deploying` alone, Design and Build answering
  held until that item lands, which leaves the brief's "seen red on a planted withdrawn parent read in
  Design" unobservable; (c) a new stand-in tag for the boundary read, a name no record declares;
  (d) B11, the `@any` re-entry row, whose witness is an admission record a parent's withdrawal never
  writes. Recommendation (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 1, flow-steps.md:746's three states and
  `item.deploy.parents`'s route at HEAD. widens: none · relaxes: none
- **F6 — Where does the terminal set live, now that every key of `[states]` is read as a level?**
  Options: (a) `terminal` in `[states]`, split out by `read_transition_rows`, the key
  `TOOL-dDeclaredLoop-54` consumes and keys by level beside it; (b) a separate `[terminal]` table keyed
  by level, which moves the key that unit's unbuilt spec names. Recommendation (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 2: the sibling's consumes-from edge holds as
  written. widens: none · relaxes: none
- **F7 — Which reader parses the parent's run facts?** Two copies of the driver's `fact` grammar exist:
  `read_run_fact` in `tools/policy/guard.py`, the faithful one (section-scoped, CR-stripped, first
  match), and a regex in `tools/branch-reconcile/branch_reconcile.py`. Options: (a) import the policy
  kit's, found beside the `resolve` this module already reads; (b) a third copy; (c) extract one into
  `tools/lib/`, a unit of its own. Recommendation (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 2: the [reuse] practice, no third copy, and the
  extraction stays a separate mechanism. widens: none · relaxes: none
- **F8 — Does the loop kit take an edge to the policy kit, and where is the leg declared?** The module
  reads the policy kit, to which the loop kit's `requires` takes no edge. Options: (a) no edge: `route`
  exits 2 where that kit does not resolve, and the leg is gov's own `[[exempt_leg]]`, as `loop computed
  witness`, `loop checklist tags` and `loop item kind` are for the kits they reach; (b) `requires`
  gains `policy`, so govkit's update refuses a loop claim without it, and the leg is the kit's
  `[[gate_leg]]`. Recommendation (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 3: the loop kit's own precedent in
  `tools/loop/kit.toml`, and deny by default where the reader is absent. widens: none · relaxes: none
- **F9 — Does the set keep the four terminals no row enters yet?** Options: (a) keep the flow record's
  nine, the set `TOOL-dDeclaredLoop-54` and `TOOL-dDeclaredLoop-31` read, a state with no row in being
  inert; (b) declare only the five a row enters or `TOOL-dDeclaredLoop-31` owes, dRankedPlan adding the
  rest with its routes. Recommendation (a).
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 1: flow-steps.md:765 is the one source of the
  set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 15, flow-steps' `[transitions]` and
  `[rules]` at base `ed497191`, v2:1252 and FK-4-3.
- rev-2 · 2026-10-24 · §3 · the Edges block gains a hands-off TOOL-dDeclaredLoop-54, a hands-off TOOL-dDeclaredLoop-56, the mirror of each unit the round-1 spec audit
  promoted (reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md); no scope moved.
- rev-3 · 2026-11-05 · S7 · §4 Files touched · AC8 · TOOL-dDeclaredLoop-56 §8 F5 (a), per the brief
  `2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade`: the leg `loop parent routes` carries
  `principle.p21`, settled here by TOOL-dDeclaredLoop-3 §8 F7's rule; its own pass writes it, so the core
  meta-check never reds the leg.
- rev-4 · 2026-11-14 · §1 · S1 S2 S3 S4 S5 S6 S7 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 ·
  §7 · §8 F2 F5 F6 F7 F8 F9 · §10 · re-grounded at HEAD `a5cc8dc37` by the brief
  2026-11-14-prompt-TOOL-dDeclaredLoop-15-reground-brief; mechanism, carries, order and status kept.
  The terminal rows are the five a declared route or `item.life.close` fires, T1 to T5, the dedupe
  re-placements and triage's defer and retire leaving scope; P1 is keyed on `item.deploy.parents`'s
  `withdrawn` (F5); `terminal` is split out of the levels (F6); the four owed rows naming this unit
  and the landed pending row of `principle.p21` are deleted with their readers; the run fact is read
  by the policy kit's reader (F7); the policy read is the landed `resolve`, and the leg is gov's
  `[[exempt_leg]]` (F8); `ceiling-evidence.txt` left the write set and the registry, usage, budget,
  map and kickoff rows joined it; code cited by symbol.

## 10. Reuse audit

The seams extended are `TOOL-dDeclaredLoop-13`'s tables and check, by rows, a split key and two
refusals (`tools/loop/loop_table.py#read_transition_rows`, `tools/loop/loop_table.py#check_transition_tables`,
`tools/loop/loop_table.py#derive_move`), and `derive_move` again as the route's one source of P1's
states. The parent read reuses the memory-tree kit's front-matter parser
(`tools/memory-tree/gen_build_index.py#parse_front_matter`) and conf reader
(`tools/memory-tree/design_lib.py#read_design_conf`), the policy kit's reader
(`tools/policy/policy.py#resolve`) and run-fact reader (`tools/policy/guard.py#read_run_fact`), the
loop kit's kit finder (`tools/loop/loop_lib.py#resolve_kit_dir`), case loop
(`tools/loop/loop_lib.py#run_selftest_cases`) and scratch helpers
(`tools/loop/loop_witness.py#run_fixture_git`, `tools/loop/loop_witness.py#remove_tree`), each read at
HEAD. `python tools/codebase-map/reuse_lookup.py "route a build when its parent build is withdrawn"`
and `"read a run-state fact from a build's RUN.md"` ranked name stems only (`build`, `read_text`,
`run_git`, `read_design_conf`), so no existing seam fits the route itself, which is new; the two
`read_run_fact` copies were found by grep, not by the lookup. `python tools/memory-recall/query.py
"what happens to a build when its parent build is aborted or withdrawn"` with the terms below returned
the scout row, this spec, DEPL-dShippedRelease-11's scout noting no reader reads another build's
landing, and the original brief's "seen red on a planted withdrawn parent read in Design", which F5
keeps; none disagrees with source.

Recall terms used: parents front matter withdrawn ABORTED terminal replan adopt-parent-work withdraw-too deploy.parents owed-row run-branch
