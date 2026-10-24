# TOOL-dDeclaredLoop-47 — the stage factory writes a whole conforming stage: its witness, exit item, state and table rows

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 21 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-47-deviation-471.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-47-deviation-471.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 3 at HIGH**, its item **H3**, alone in that item. `TOOL-dDeclaredLoop-6` S5's
`new stage` appends only a `[[step]]` row and a stage claim. The `loop definition` leg it gates on also
runs `TOOL-dDeclaredLoop-5`'s check (a step needs a `witness`), `TOOL-dDeclaredLoop-12`'s (a step's `exit`
must be a declared item of that step) and `TOOL-dDeclaredLoop-13`'s (a state in `[states]`, an exit
routed to `transition` fired by a build row), all landed at orders 5, 6 and 10, before the factory at 20.
So its AC4 `stage-new` case cannot be green on a correct build: the restore rule undoes every stage
written, or the builder weakens the gate. This unit takes the report's first fix. It repairs
`TOOL-dDeclaredLoop-6`.

## 2. Scope (IN)

- **S1** — `new stage <name> --order <n> --state <state> --after <step tag> --exit <item tag>` writes, in
  `tools/loop/loop.toml`: the `[[step]]` row with `witness = { class = "history", by = "the transition
  record into the next step" }`, `TOOL-dDeclaredLoop-5` S2's form; the exit `[[item]]` row named by
  `--exit`, `step` the new step, `actor` `role:gov-builder` unless `--actor` names another (a non-role
  actor then requires `--inputs`, `--allowance` and `--returns`), `needs = []`, `outcomes = ["pass"]`,
  `routes = { pass = "transition" }`, its witness the transition record, `owner` the repository's own
  slug read from `.governance/install.json`'s kit row or `gov`; and `--state` appended to `[states]`'s
  `build` list. Observed by AC1.
- **S2** — The table rows, by insertion after `--after`: the build row leaving `--after`'s state through
  its exit item is re-targeted to `--state`, and one row is added from `--state` through the new exit
  item on `pass` to the state that row used to reach, both through `derive_inserted_rows(table, after,
  state, exit_item)` in `tools/loop/factories.py`. Observed by AC1, AC2.
- **S3** — The gate the factory runs is every check the `loop definition` leg and the
  `loop transition tables` leg run: `python tools/loop/loop_lib.py --check` and
  `python tools/loop/loop_table.py check`, both exit 0 or every written file is restored. This supersedes
  `TOOL-dDeclaredLoop-6` S5's gate of `loop_lib.py --check` alone. Observed by AC1, AC3.
- **S4** — `TOOL-dDeclaredLoop-6` AC4 is restated: `--plant stage-new` exits 0 with both checks green on
  the written stage, and `--plant stage-hand`, a hand row with no witness, is red under the same two.
  Observed by AC1, AC3.

## 3. Non-goals (OUT)

- An adopter's own stage: `TOOL-dDeclaredLoop-25`'s `[[splice]]` row in the overlay, expanded at
  composition by its `derive_splice_rows`, which never edits `tools/loop/loop.toml`.
- The other five factories: `TOOL-dDeclaredLoop-6`'s; the item factory of `TOOL-dDeclaredLoop-24` and
  its missing fields are the audit's id 13, batched into `TOOL-dDeclaredLoop-56`.
- Restoring created files and SIGINT handling in the factory contract: the audit's id 59, batched into
  `TOOL-dDeclaredLoop-56`.
- A factory selftest arm running every check of every gated leg over each kind's fresh instance, the
  finding's left-shift: S3 is that rule for this kind; the general arm is id 59's neighbour and not a
  clause of this build.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-6` — `write_stage` in `tools/loop/factories.py` and its fixture cases, whose instance this unit makes conform

## 4. Design

### Evidence

- `TOOL-dDeclaredLoop-5` S2 requires every `[[step]]` row to carry a classed witness; `TOOL-dDeclaredLoop-12`
  S3 requires each step's `exit` to be a declared item of that step, every outcome routed and every need
  declared; `TOOL-dDeclaredLoop-13` S2 and S7 require the state in `[states]` and every `transition`
  route matched by a build row. Each is a check under the gated legs.
- The two-row insertion is the shape `TOOL-dDeclaredLoop-25` S2 states for an adopter splice: from
  `after`'s state to the new state on the same item and outcome, and from the new state through its exit
  item to `before`'s state.

### The written stage

```toml
[[step]]
tag = "step.<name>"
order = <n>
state = "<state>"
exit = "<exit item>"
witness = { class = "history", by = "the transition record into the next step" }

[[item]]
tag = "<exit item>"
step = "step.<name>"
actor = "role:gov-builder"
needs = []
outcomes = ["pass"]
witness = { class = "history", by = "the transition record" }
owner = "<owner>"
[item.routes]
pass = "transition"
```

### Files touched (estimate)

- `tools/loop/factories.py`

### Alternatives rejected

- **Narrowing the kind to a `[[step]]` row alone.** Such a row cannot conform under the landed checks, so
  the kind would have a factory that never succeeds.
- **Calling `TOOL-dDeclaredLoop-25`'s `derive_splice_rows`.** That unit sits in the same parallel group
  (order 21), so this one cannot consume it, and it expands an overlay splice against a composed table
  rather than editing gov's definition. The shared rule is the two rows S2 names.

## 5. Production-readiness checklist

- security — no new surface; the factory writes only `tools/loop/loop.toml`, the file its kind names.
- perf / scale — two checks per factory call.
- error / empty / loading states — a red check restores the file and prints the check's output; an
  `--after` naming no step refuses before any write.
- observability — the factory prints every row it wrote.
- risks — inserting before Deploy re-targets one gov row; both checks run before the write is kept.
- testing — AC1 to AC3 as fixture plants; the arm under §7, observed at the close.
- migration — none.
- user docs — `help/loop.md`'s factory section, `TOOL-dDeclaredLoop-6`'s, names the new flags.

## 6. Acceptance criteria

- **AC1** — When `python factories.py --fixture --plant stage-new` runs `new stage audit
  --order 4 --state auditing --after step.build --exit item.audit.exit`, it exits 0, and in its
  scratch repository `python loop_lib.py --check` and `python loop_table.py check`
  both exit 0.
  Red when: the factory writes the `[[step]]` row alone, so `loop_lib.py --check` refuses its missing
  witness and the factory restores.
- **AC2** — When the same plant's scratch `loop.toml` is read, the build row leaving `building` through
  `item.build.exit` reaches `auditing`, and one row leaves `auditing` through `item.audit.exit`
  on `pass` to `testing`.
  Red when: the new state is unreachable from the build table.
- **AC3** — When `--plant stage-hand` runs, a hand-written `[[step]]` row with no witness, both checks
  exit non-zero naming the row.
  Red when: the gate runs only the factory's own arm, so a hand row passes.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/factories.py · covers AC1 AC2 AC3 · the `stage-new` and `stage-hand` plants under both checks, staged against the step-row-only factory · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — A whole stage, or a narrower kind?** Options: (a) the factory writes the whole stage; (b) the
  kind narrowed to what a factory alone can make conform. (b) has no member: a step row cannot conform
  without its item, state and rows. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none
  · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 3 (HIGH, item H3).

## 10. Reuse audit

The seam is `TOOL-dDeclaredLoop-6`'s factory contract and `write_stage`; the checks are the landed ones
under the two legs, run as their CLIs. `python tools/codebase-map/reuse_lookup.py "insert a state into a
transition table after an existing step"` ranked `step` (govkit), `plan_state`, `resolve_state_dir`,
`check_run_state` and `derive_table`, none of which edits a transition table, so no existing seam fits
the insertion, and the one in this build that shares its rule is a parallel peer (§4).

Recall terms used: stage factory step witness exit item states transition row insert loop definition conform
