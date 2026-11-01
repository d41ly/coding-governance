# TOOL-dBoundRoles-23 — the prompt writer's default frame, bounded lists, upstream rows, and the medium effort floor

**Status:** DEFERRED · rev-4 · 2026-10-26 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 18 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0188@23b122f8 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-17 TOOL-dBoundRoles-24 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-23-deviation-231.md](../build/2026-10-26-build-TOOL-dBoundRoles-23-deviation-231.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-23-deviation-232.md](../build/2026-10-26-build-TOOL-dBoundRoles-23-deviation-232.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-23-deviation-233.md](../build/2026-10-26-build-TOOL-dBoundRoles-23-deviation-233.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-crosscheck.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-37 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-66 TOOL-dBoundRoles-69 |
| [2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-1-parents-reground.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-14 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-25 TOOL-dBoundRoles-43 TOOL-dBoundRoles-60 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 |

<!-- /gen:spec-records -->

## 1. Goal

aScoutedSeam measured that a task's shape moves recall and cost, and fixed a skeleton for a role
item's prompt: role and job kind, material, boundaries, population, upstream rows, row contract, added
rows, the no-stop line, and the return contract last
(`memory/builds/aScoutedSeam/build/2026-10-19-build-TOOL-aScoutedSeam-3-3-agent-prompt-principles.md:182-202`).
Today `render_handoff` appends blocks in the order it meets them (`tools/roles/handoff.py:381-416`),
no list it renders is bounded, and no edge hands its commitments on as rows the next step answers
(gap-roles-27, gap register `:179`). The owner also made effort the owner's setting: medium by default,
and below medium only by the owner's explicit write to the guarded policy file (the night pass two,
point 2, items 4 and 5, NT-10 and NT-12). This unit makes the skeleton the work order's one frame,
bounds every list the frame renders and every list its return may carry, places the upstream rows and
their answers in it, and holds every effort to the medium floor unless the owner's policy file sets
less.

## 2. Scope (IN)

- **S1** — The frame, shared interface I15. `FRAME_SLOTS` in `tools/roles/roles_lib.py` names the nine
  slots in the skeleton's order: `role`, `material`, `boundaries`, `population`, `upstream`, `contract`,
  `added`, `no-stop`, `return`. Every block `render_handoff` adds carries one slot, and the `## Task`
  section is assembled by `assemble_frame(blocks)`, a stable sort by slot; a block with no slot or an
  unknown one raises `RolesError` naming it. §4 "### The slots" maps every block kind to its slot.
  Observed by AC1 and AC2.
- **S2** — The prompt writer's parts in their slots: the `### framing:job` block TOOL-dBoundRoles-4
  renders goes to `role`, `### framing:population` to `population`, `### framing:added` to `added`, and
  `### framing:no-stop` to `no-stop`. A role item whose work order hands no population lister requires
  `### framing:population`, the needs-then-sketch steps, and the render refuses without it.
  Observed by AC1.
- **S3** — Every list bounded. The population block lists at most the bound and closes with an overflow
  line naming how many members it left out and where the full list is; the return contract
  (`return` slot, TOOL-dBoundRoles-3's `### return` block extended) states, for every `list` field of
  the role's `return` template, its bound: the population's size where the work order hands a
  population, else `FRAME_LIST_BOUND`. `validate_return` (TOOL-dBoundRoles-5) refuses a list field
  longer than the bound its work order's return contract states. Observed by AC3.
- **S4** — The upstream rows. Where the item declares `upstream`, TOOL-dDeclaredLoop-29 S5's
  `### upstream:rows` block sits in the `upstream` slot, and the return contract restates its row
  contract: every handed row id answered exactly once in the return's `## Upstream` section. The join at
  the return is TOOL-dDeclaredLoop-29 S6's `join_upstream`. Observed by AC1.
- **S5** — The floor. `EFFORT_FLOOR = "medium"` in `roles_lib.py` beside `EFFORT_LEVELS`
  (`roles_lib.py:45`), the one spelling of the floor, and `check_effort_floor(level, source)`: a level
  below the floor passes only when its source is the policy file `.governance/policy.toml`, read through
  `read_policy_setting` (TOOL-dBoundRoles-21 S1) as a `roles.effort.*` key, under the guard value S6
  names. It is applied at every
  place an effort is resolved or declared: steps 4 and 5 of TOOL-dBoundRoles-21's order in
  `resolve_stage_efforts` and `resolve_effort`; R12's `check_level` (`roles_lib.py:397-400`), so a house
  file `[effort]` value below medium is a defect while the house file stays a fallback; and R2's grade
  of a role's declared `effort`, so no role declares less than medium. Observed by AC4 and AC6.
- **S6** — The owner's write is the only path below medium. A `roles.effort.*` key reaches
  `.governance/policy.toml` only through TOOL-dDeclaredLoop-2's verdict, `tools/loop/guard.py --staged`
  (its S1, S11), which admits a guarded-path change on the owner's terminal proof and otherwise decides
  by `policy-file.guard`. Under `owner-only`, the default, it refuses every agent change but the one
  budget shape (TOOL-dGroundRules-6 S2 to S4), so an agent, a role's proposal, a scenario and a build's
  own change cannot carry a level below medium. Under `agents-with-reason` and `agents-within-mandate`
  it admits an agent's change to that file with its change record and decision row (its §4 "The
  verdict"), so the file no longer tells the owner's level from an agent's. There `check_effort_floor`
  refuses a policy-file level below medium, naming `policy-file.guard`, read through
  `read_policy_setting` from the same file, which only the owner's terminal commit changes (its S3).
  The floor's provenance is read from that file alone (§8 F3). Observed by AC5 and AC6.
- **S7** — Every refusal S5 adds names the level, its source, the floor, and the remedy's actor: the
  owner, who sets the key in the guarded policy file. The roles kit's own fixtures that plant `low`
  (`tools/roles/render_agents.py:448`) keep one floor plant and move the rest to `medium`.
  Observed by AC4.
- **S8** — `tools/roles/README.md` and the user page `help/roles.md` ("How a task reaches an agent",
  `:13-27`) state the frame's order and the floor. Observed by AC7.

## 3. Non-goals (OUT)

- The work order's blocks themselves, the item, its inputs, its allowance, its return template and its
  witness: TOOL-dBoundRoles-3's. This unit gives each a slot.
- The prompt writer's fields and the framing blocks: TOOL-dBoundRoles-4's.
- The effort keys, their order and their reader: TOOL-dBoundRoles-21's.
- The upstream field, its block and its join: TOOL-dDeclaredLoop-29 S5 and S6.
- The guard and the owner's terminal proof: TOOL-dGroundRules-6's and TOOL-dDeclaredLoop-2's verdict,
  observed here and not changed.
- An effort a caller types by hand into a harness's `efforts` argument. The harnesses grade its shape
  only (`tools/workflows/unattended-build.template.js:505-532`); a caller that reads
  `handoff.py stage-efforts` gets levels S5 has graded, and one that types a level is not seen.
- The anchor check over the framing: TOOL-dBoundRoles-24's, which reads the frame this unit assembles.

### Edges

- **consumes-from** `TOOL-dBoundRoles-3` — the work order's item, inputs, allowance, return template and witness blocks, each of which S1 places in its slot
- **consumes-from** `TOOL-dBoundRoles-4` — the `### framing:` blocks and the `Framed by:` line, which S2 places in the `role`, `population`, `added` and `no-stop` slots
- **consumes-from** `TOOL-dBoundRoles-5` — `validate_return`, which S3 extends with the bound a work order's return contract states
- **consumes-from** `TOOL-dBoundRoles-21` — `roles.effort.default` and the re-pointed `resolve_stage_efforts`, whose steps S5 holds to the floor
- **hands-off** `TOOL-dBoundRoles-24` — `render_handoff`, with the frame assembled, the one place a work order's task is composed and the point the anchor check runs
- **consumes-from** external — TOOL-dDeclaredLoop-29 S5's `### upstream:rows` block and S6's `join_upstream`, TOOL-dGroundRules-6's guard and TOOL-dDeclaredLoop-2's verdict `tools/loop/guard.py --staged`; the build run re-grounds on each and stops the unit if one is still absent
- **hands-off** `TOOL-dBoundRoles-43` — `check_effort_floor`, which unit 43 applies at unit 22's three steps (id 18 of the round-1 spec audit)
- **consumes-from** `TOOL-dBoundRoles-48` — `check_block_fences` and its call in `render_handoff`, which runs after this unit's frame places its `### framing:` blocks, so a framing field that leaves a fence open is refused (id 34 of the round-1 audit of units 37 to 44)

## 4. Design

### The slots

| # | Slot | Blocks placed there |
|---|---|---|
| 1 | `role` | the opening line (build, unit), `### item` (TOOL-dBoundRoles-3), `### framing:job` with its `Framed by:` line |
| 2 | `material` | every `reads` block (`### task:goal`, `### input:spec`, …), then `### inputs` (TOOL-dBoundRoles-3), the inputs as content |
| 3 | `boundaries` | `### allowance` (TOOL-dBoundRoles-3), the charter rule blocks `render_charter_blocks` returns where they are carried |
| 4 | `population` | the item lister's members, bounded, or `### framing:population` |
| 5 | `upstream` | `### upstream:rows` (TOOL-dDeclaredLoop-29 S5) |
| 6 | `contract` | `### row contract`: per member, id · evidence of search · a verdict from the closed set the role's `outcome` declares, with its escape · a one-line reason |
| 7 | `added` | `### framing:added` |
| 8 | `no-stop` | `### framing:no-stop`, and "incomplete" defined against the population |
| 9 | `return` | TOOL-dBoundRoles-3's `### return`, the role's `return` template, extended with each `list` field's bound, the `answers` value and the `## Upstream` answer rule; then its `### witness` |

A slot with no block is left out, never rendered empty; the order of the slots that remain is the
skeleton's. `assemble_frame` is stable, so two blocks of one slot keep the order they were added in,
which keeps every `reads` block in its role's `reads` order as today.

### The bound

`FRAME_LIST_BOUND = 12`, PINNED from the night pass two's reuse-scout contract, "at most twelve seams"
(`night-pass-two.md:194-196`, NT-10), the one measured bound a role return carries in the records. A
population longer than the bound renders its first `FRAME_LIST_BOUND` members by the lister's own order
and the line `… and <n> more; the full list is <path or command>`. The return contract writes each
`list` field as `<field>: at most <bound> entries`, and `validate_return` reads that line back from the
work order it already reads for `answers`, so the bound lives in the rendered work order and nowhere
else.

### The floor

```
check_effort_floor(level, source)
  EFFORT_LEVELS.index(level) >= EFFORT_LEVELS.index(EFFORT_FLOOR) -> pass
  source == policy file (steps 1-3 of the order, read_policy_setting)
    and policy-file.guard == owner-only -> pass   the owner's write
  source == policy file, any other guard value -> RolesError naming policy-file.guard and its value
  otherwise -> RolesError: "<level> from <source> is below the floor medium; only the owner sets a
               lower level, as a roles.effort.* key in the guarded policy file"
```

| Source of a level | Below medium |
|---|---|
| `roles.effort.<workflow>.<stage>`, `roles.effort.<role>`, `roles.effort.default` in `.governance/policy.toml` | admitted under `policy-file.guard = owner-only`, where only the owner's terminal commit writes there; refused under the two other values, where TOOL-dDeclaredLoop-2's verdict also admits an agent's recorded change (S6) |
| the house file's `[effort]` (step 4) | refused, by R12 at load and by S5 at resolve |
| the role's declared `effort` (step 5) | refused, by R2 |
| a stage row's own `effort`, a scenario's or an overlay's | refused at resolve, as a declared value |

### Inventory

Minted: `FRAME_SLOTS`, `assemble_frame`, `FRAME_LIST_BOUND`, `EFFORT_FLOOR`, `check_effort_floor`; the
`### row contract` block and the bound lines of the `### return` block; the bound check in
`validate_return`; the fixture plants of
§7's arm (`frame-order`, `frame-no-slot`, `frame-no-population`, `population-over-bound`,
`return-over-bound`, `house-low`, `role-declared-low`, `policy-low-owner`). Each name is asked of
`python tools/lexicon/lexicon.py --suggest <name>` at the pass.

### Migration

A rendered prompt's block order changes at landing; prompt files already written keep their bytes and
their task-sha, and rule 6 compares each spawn with its own file. An adopter whose house file sets a
level below medium meets an R12 defect naming the floor and the key to write instead.

### Rollout

Live at landing; no switch. The floor is the owner's NT-12 answer, and its one exception is the owner's
own key.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/check_roles.py`
- `tools/roles/render_agents.py`
- `tools/roles/README.md`
- `help/roles.md`

### Alternatives rejected

- **Blocks ordered by the order code appends them.** Every later block-adding unit would have to append
  in skeleton order by hand; one sort by declared slot cannot drift.
- **A floor checked against the commit that last touched the key.** The clause reads provenance "from
  that file alone"; the guard's value, which only the owner's terminal commit sets, decides whose write
  may land there, and a history read would be a second guard.

## 5. Production-readiness checklist

- security — the floor narrows what any non-owner source can set; the one path below it is the guarded
  file, whose guard this unit relies on and does not widen.
- perf / scale — one stable sort per render; one integer compare per resolved level.
- error / empty / loading states — a block with no slot, a missing population, a list over its bound and
  a level below the floor each refuse by name; an empty slot renders nothing.
- observability — each floor refusal names level, source, floor and the owner as the remedy's actor.
- risks — an adopter running a role at `low` from its house file is refused until the owner writes the
  key; a population over twelve renders truncated, with the overflow line naming where the rest is.
- testing — the plants of §4's inventory through `python -c` and the render verb; the arm in §7 is
  observed RED then GREEN by the main loop at the close.
- migration — as §4 says.
- user docs — `help/roles.md` and `tools/roles/README.md` (S8).

## 6. Acceptance criteria

- **AC1** — When `handoff.py render --role gov-builder --framed-by <id> --stdout` renders a fixture item
  with upstream rows, an allowance and a framing carrying `job`, `added` and `nostop`, the `## Task`
  headings run `### framing:job`, the `reads` blocks, the allowance, `### upstream:rows`,
  `### row contract`, `### framing:added`, `### framing:no-stop`, then `### return` and `### witness`
  last.
  Red when: blocks keep the order they were appended in, so the return contract is not last.
- **AC2** — When `python -c` calls `assemble_frame` with a block whose slot is `misc`, it raises
  `RolesError` naming the block; when the item hands no lister and the framing has no `population`, the
  render refuses naming `framing:population`.
  Red when: an unplaced block is appended silently, or a frame with no population renders.
- **AC3** — When the fixture item's lister yields 30 members, the population block lists 12 and closes
  with a line naming 18 more; the `### return` block states `at most 30 entries` for the builder's
  `checks` list; and when the item hands no population, it states `at most 12 entries`, and
  `validate_return` refuses a reply whose `checks` holds 13, naming `checks` and the bound.
  Red when: a list renders unbounded, or a return over its stated bound passes.
- **AC4** — When `load_policy` reads a fixture house file with `[effort.roles] gov-builder = "low"`, it
  raises R12 naming the floor `medium`; when R2 grades a role file declaring `effort: low`, it reports a
  defect; and a stage whose only level comes from the house file at `low` is refused by
  `resolve_stage_efforts` naming the source.
  Red when: a below-medium level from the house file or a role's declaration resolves.
- **AC5** — When `python tools/loop/guard.py --staged` reads a fixture repository whose staged change
  to its policy file sets `roles.effort.gov-builder = "low"`, then a stage key
  `roles.effort.build.builder = "low"`, then `roles.effort.default = "low"`, with no owner proof and
  `policy-file.guard` unset, it refuses each, exit 1. With `policy-file.guard = "agents-with-reason"`
  landed, the `roles.effort.default` change staged with a change record naming
  `policy.roles.effort.default` and a `memory/DECISIONS.md` row exits 0, and without the row exits 1;
  with `"agents-within-mandate"` landed, the same staged change on a branch no run-state file names
  exits 1.
  fixture: needs TOOL-dDeclaredLoop-2 built; the build run re-grounds on it.
  Red when: an agent's change below medium reaches the policy file under `owner-only`, or a value's
  outcome differs from what S6 states.
- **AC6** — When the fixture's committed policy file, `policy.toml`, sets `roles.effort.default = "low"`,
  `python tools/roles/handoff.py stage-efforts build` prints `"builder":"low"`, and
  `check_effort_floor` passes the level because its source is the policy file; with
  `policy-file.guard = "agents-with-reason"` committed beside it, the same command exits 1 naming
  `policy-file.guard`.
  Red when: the floor refuses the owner's own key under `owner-only`, so no role can run at low, or
  admits it under a value that lets an agent write the file.
- **AC7** — When `grep -n "medium" help/roles.md` and `grep -n "FRAME_SLOTS" tools/roles/README.md`
  run, the page states the floor and its one exception and the README names the frame's order.
  Red when: the page still says the effort is whatever the policy file sets, with no floor.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/render_agents.py · covers AC1 AC2 AC3 AC4 AC6 · its self-test renders the plants of §4's inventory, the failing case staged by an `assemble_frame` that keeps arrival order and a `check_effort_floor` that passes every level · none

## 8. Open questions

- **F1 — How is "every list in the output bounded" read?** Options: (a) every list the frame renders,
  the population above all, capped with an overflow line, and every `list` field of the return held to
  a bound the return contract states and `validate_return` enforces; (b) the rendered lists only; (c)
  the return's lists only. (b) leaves the return unbounded, the half NT-10's "at most twelve seams"
  bounds; (c) leaves the population, P2's "capped with an overflow line", unbounded. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the most feature-rich option. widens: none · relaxes: none
- **F2 — The bound where no population is handed.** Options: (a) `FRAME_LIST_BOUND`, 12, pinned from
  NT-10; (b) a policy key; (c) no bound. (b) is a key no build's `[policies]` row declares, so a new
  key outside this build's set; (c) fails F1. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3,
  veto 2 refusing (b). widens: none · relaxes: none
- **F3 — How does the floor read "the owner's explicit authorization" without a second guard?**
  Options: (a) a level's source is the provenance: steps 1 to 3 of the order read the guarded policy
  file, and every other source is held to the floor; (b) the floor reads each key's last commit and its
  proof, or the change record TOOL-dDeclaredLoop-2 requires; (c) as (a), a policy-file level below
  medium passing only while `policy-file.guard`, read from the same file, is `owner-only`. (b)
  re-implements the guard over history and reads more than "that file alone". The rev-1 pick, (a),
  rested on only the owner changing the file (TOOL-dGroundRules-6), which TOOL-dDeclaredLoop-2 §4 "The
  verdict" rules out under `agents-with-reason` and `agents-within-mandate`, so (a) would admit an
  agent's level there. RESOLVED (agent, 2026-10-26, delegated): (c), rung 1, naming
  TOOL-dDeclaredLoop-2: the clause's own words, "below medium only by the owner's explicit write" and
  "provenance from that file alone", hold under every value only when the floor reads the guard value
  beside the level; that unit's S3 keeps the value the owner's. widens: none · relaxes: none
- **F4 — Does the frame carry a slot for every block, or only the prompt writer's?** Options: (a) every
  block `render_handoff` adds carries a slot and one sort assembles the task; (b) the prompt writer's
  parts are placed and every other block keeps its arrival order. (b) leaves the work order's own blocks,
  the return template among them, outside the skeleton the clause orders "with the return contract
  last". RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the shape shared interface I15 states.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 23, the brief's shared interfaces I9, I15
  and I16, scout B's row for cl-0188, aScoutedSeam's skeleton, the night pass two's point 2, and
  `tools/roles/` at base `4ed9e567`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring the edges of TOOL-dBoundRoles-43, promoted by the round-1 spec audit of the 26 unit specs; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the **consumes-from** bullet mirroring TOOL-dBoundRoles-48's hands-off, a promotion of the round-1 audit of units 37 to 44; nothing else moved.
- rev-4 · 2026-10-26 · S5 · S6 · §3 · §4 The floor, Alternatives rejected · AC5 · AC6 · §8 F3 ·
  re-grounded on TOOL-dDeclaredLoop-2 by `build/2026-10-26-build-TOOL-dBoundRoles-1-parents-crosscheck.md`
  row 43: the verdict is `tools/loop/guard.py --staged`, which admits an agent's recorded policy change
  under the two non-default `policy-file.guard` values, so the floor admits a policy-file level below
  medium only under `owner-only`; AC5 plants each value; F3 re-resolved to (c).

## 10. Reuse audit

The seams extended are `render_handoff`'s blocks list (`tools/roles/handoff.py:381-416`), the one place
a task is assembled; `EFFORT_LEVELS` (`tools/roles/roles_lib.py:45`), the one level list, and R12's
`check_level` (`:397-400`), which grades every house level today and gains the floor; and
TOOL-dDeclaredLoop-29 S5's upstream block on the same function. The probe `reuse_lookup.py` over the
phrase "render the task block of a handoff in a fixed order with bounded lists and an effort floor"
ranked generic `render_*` functions and `boundedParallel`, a concurrency helper; none orders blocks by a
declared slot or bounds a rendered list, so no existing seam fits for `assemble_frame` or the bound,
and the floor extends the level check that exists. Scout B's row agreed with source; it cites
`check_level` at `:397`, which spans `:397-400`, and the low plant at `render_agents.py:448`, which
source holds there.

Recall terms used: `python tools/memory-recall/query.py "what is the default frame of a work order and the effort floor" --terms "default frame skeleton upstream rows bounded list effort floor medium owner authorization policy.toml provenance"`
