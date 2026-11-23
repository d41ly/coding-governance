# KICK-dKeptSession-17 — the attendance rule: `attendance` adds only the owner's interactions, its arm refusing any that swaps an actor

**Status:** INPROGRESS · rev-6 · 2026-11-23 · node a · Tier-2 · base 689698a5 · streams kickoff · order 27 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0155@6d913746 whole
**Carries:** node:policy-key.attendance

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-18 KICK-dKeptSession-26 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-17-deviation-171.md](../build/2026-10-26-build-KICK-dKeptSession-17-deviation-171.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-17-reground-orders-27-29-returns.md](../build/2026-11-21-build-KICK-dKeptSession-17-reground-orders-27-29-returns.md) | research | KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-17-1-spec-reviewer.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-17-1-spec-reviewer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-11-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-11-precheck-brief.md) | research | KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 |
| [2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief.md) | research | KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-26 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-11 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-61 KICK-dKeptSession-18 |
| [2026-11-21-prompt-KICK-dKeptSession-17-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-17-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-17-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-17-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-17-orders-27-29-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-17-orders-27-29-reground-brief.md) | research | KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 |
| [2026-11-22-prompt-KICK-dKeptSession-17-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-17-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-17-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-17-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

Attendance is not one rule today: about thirty catalogue keys carry an owner-valued option, and nothing
stops a posture from swapping an item's actor for the owner (`gap-flow-16`,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md@cd15c089:122`). The
owner's rule is P4: attendance "adds only the owner's interactions: the announcement of each act's step
and role, the owner's confirmations at breakpoints, and owner questions asked live. It never changes an
item, its actor, the driver, a role's use or its enforcement"
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:860`).
This unit carries `attendance`, whose catalogue row stands, as one switch: its values place owner gates
through dDeclaredLoop's one breakpoint list, `tools/loop/breakpoints.py#derive_breakpoints`, its
interactions are a closed set declared as data, and its arm refuses any declaration that would select
an actor, the driver or a binding. The `step —` announcement and owner questions asked live are
stand-ins until dWellOiledMachine and dFurnishedOrders land them.

## 2. Scope (IN)

- **S1** — The key, standing. The catalogue row `attendance` (`tools/policy/catalogue.toml`,
  `name = "attendance"`, owner dKeptSession) holds the allowed values `unattended`, `announce`,
  `confirm-steps` and `confirm-acts` and the default `unattended`, and the mirror
  `.governance/policy.json` holds the key at that default. This unit writes neither file, runs no
  factory and moves no mirror: the row's `summary` and `usage` are KICK-dKeptSession-41's. Presets never
  touch the key: v2 lists it among the keys no preset sets
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1434`),
  and the `never` list of `tools/policy/presets.toml` carries it. Observed by AC7.
- **S2** — The declarations, `[[attendance]]` rows of `tools/loop/loop.toml` after its `[mail]` table,
  under one comment as `[mail]`'s, one row per value, each with exactly the keys `value` and `adds`,
  `adds` a list of members of the closed set `ATTENDANCE_INTERACTIONS` in `tools/loop/loop_lib.py`
  (§4). `read_attendance(kit_dir)` beside `read_mail_kinds` returns `{value: adds}` once the arm
  holds, and raises LoopError naming the first refusal, or a definition that declares no row, as
  `tools/loop/loop_lib.py#read_mail_kinds` does for `[mail]`. The shipped rows are §4's, from
  flow-steps' attendance rule
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@d73cb002:558`):
  every attended value announces each act and asks owner questions live, `confirm-steps` adds a gate at
  every step's exit, `confirm-acts` one before every act. Observed by AC1 to AC5.
- **S3** — The arm, `check_attendance_rows(rows)`, returning `(lines, refusals)` as
  `tools/loop/loop_lib.py#check_item_declarations` does: one `loop: attendance <value> · adds
  <members|none>` line per row, and one refusal per shape §4's refusal table names. `main`'s `--check`
  (`tools/loop/loop_lib.py#main`) prints its lines after the probe lines and before `loop: witness
  classes`, and joins its refusals to the item refusals, so each prints `loop: refused · <why>` and the
  read exits 1. No member of the set names an actor, the driver or a binding, so a declaration that
  swaps an actor can only be written as one of those refused shapes. The plants `attendance-actor`,
  `attendance-member` and `attendance-twice` join `PLANTS` and `PLANT_OWED`, each break made in memory by
  `tools/loop/loop_lib.py#write_loop_plant`. They move the `plants=<n>` token of the `loop definition
  fixtures` row, re-priced as §4's budget rows state. Observed by AC5, AC8.
- **S4** — The breakpoint source, in `tools/loop/breakpoints.py`. `read_policy_values` reads
  `attendance` beside `autonomy`, as a string literal at its `read_value` call
  (`tools/loop/breakpoints.py#read_policy_values`), so the catalogue default `unattended` answers where
  the policy file sets none. `read_breakpoints` hands `derive_breakpoints` two more facts: `attendance`,
  `read_attendance(KIT)`, and `acts`, the tags of the rows `read_build_item_rows` returns whose actor
  opens `role:` (`tools/loop/loop_lib.py#resolve_item_declaration`). `derive_breakpoints` checks
  `values["attendance"]` against the keys of `facts["attendance"]` beside its other keys, a ValueError
  `attendance is '<value>', which no [[attendance]] row of the loop definition declares`, which `list`
  prints as `breakpoints: refused · <why>`, exit 2 (`tools/loop/breakpoints.py#main`). After
  `autonomy`'s gates and before the `review.breakpoints` members, `confirm-step-exit` places an `owner
  gate` `at` each step's `exit` and `confirm-before-act` one `before` each tag of `acts`, each with
  cause `attendance`, through its `write_line`, which keeps the gate already standing at a position and
  disposer (§8 F3). Observed by AC1 to AC3 and AC6.
- **S5** — The hold is dDeclaredLoop's, and this unit adds no holding code: each gate S4 places reads
  `held` until the owner's disposition record of its tag releases it
  (`tools/loop/breakpoints.py#read_breakpoints`), the driver's `--close` refuses while one is held,
  and relays a refusing list through the same refusal (`tools/unattended/unattended.sh#read_held_gates`,
  `tools/unattended/unattended.sh#check_owner_gates`); a gate `at` a step exit also holds the `--phase`
  move across it (`tools/unattended/unattended.sh#check_phase_gates`); and `--plan` prints the module's
  lines verbatim (`tools/unattended/unattended.sh#print_breakpoint_lines`). Observed by AC6.
- **S6** — The stand-ins. `announce` answers `stand-in dWellOiledMachine`, the `step —` announcement of
  `cl-dClosedLoop-0304`; `ask-live` answers `stand-in dFurnishedOrders`, owner questions asked live of
  `cl-dClosedLoop-0207`. Under a value whose `adds` is not empty, `read_breakpoints` sets `attended`, the
  `(value, adds)` pair, on the plan gate's entry, which `derive_breakpoints` always writes, as it sets
  `unopened` on a held gate; `list` prints, after the breakpoint lines and before any `breakpoints:
  held` line, one line `breakpoints: attendance · <value> · adds <members> · <member>: stand-in <owner>
  …`, one clause per member whose `ATTENDANCE_INTERACTIONS` answer opens `stand-in `.
  `render_breakpoint_line` reads neither key. Under `unattended` no line prints, so a default list is
  unchanged byte for byte. Each owner build arms its member by changing its entry in
  `ATTENDANCE_INTERACTIONS` in the same landing as its mechanism. Observed by AC1 and AC4.
- **S7** — The page `help/loop.md`, section "Where a build stops for a review or for you": "four keys"
  reads "five keys", and an `attendance` bullet after `autonomy`'s states the four values, what each
  adds, that no value changes an actor, the driver or a binding, which positions hold `--close` and
  which the `--phase` move, and the two stand-ins, its first line carrying the anchor `<!-- usage:
  policy:attendance <fp8> -->`, the fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints
  at build time. The section's list bullet names the attendance line and the refusal of a value no row
  declares, and its fixture bullet the three S8 plants. The hold paragraph of "Which state and step each
  run phase reads" reads "Under the default `autonomy` and `attendance`". In "How to use it", "Read the
  loop" names the `loop: attendance` lines and the attendance refusal, and "See a refusal" the three S3
  plants. The row `policy:attendance` comes off `memory/project/docs-undocumented.txt` in the same commit,
  since the docs leg reds a listed member a page anchors. Observed by AC7, AC9.
- **S8** — The plants of `python tools/loop/breakpoints.py --fixture --plant <case>`, each in `PLANTS`
  and run by `--selftest`: `attendance-values` (AC1 to AC4) and `attendance-missing` (AC6) each over the
  scratch repository `write_transition_plant(top, "default")` builds, joining the `values` plant's
  branch, and `attendance-plan` (AC6) over the one `write_position_plant` builds, beside `driver-plan`
  (`tools/loop/breakpoints.py#run_breakpoint_plant`). `attendance-missing` runs `list` with
  `read_attendance` bound, for that run, to the shipped rows less `confirm-steps`, through
  `unittest.mock.patch.object(sys.modules[__name__], ...)` as `tools/loop/guard.py#run_guard_plant`
  binds its swaps. Each prints `breakpoints: fixture · <case> · held` and exits 0 where its owed lines
  hold, the line `run_selftest`'s one case per plant reads (`tools/loop/breakpoints.py#run_selftest`),
  and `MISSED <why>`, exit 1, where one does not; a `list` a plant runs inside it exits as the criteria
  say. They move the `plants=<n>` token of the `loop breakpoint fixtures` row, re-priced as §4's budget
  rows state. Observed by AC1 to AC4, AC6 and AC8.
- **S9** — The other shipped texts §4's table marks edited: the loop kit's `tools/loop/README.md`, the
  breakpoints comment of `tools/loop/kit.toml`, and the `--plan` entry of
  `tools/unattended/VERBS.template.md` with its byte-equal copy `memory/guides/UNATTENDED-VERBS.md`.
  Observed by AC9.

## 3. Non-goals (OUT)

- The attend and unattend requests, the `attendance override` record and `attendance.scope`:
  dWellOiledMachine's (`cl-dClosedLoop-0281`), which writes the value this unit reads.
- The `step —` line itself and `next`, which renders it: dWellOiledMachine's (`cl-dClosedLoop-0304`).
- Owner questions asked live, and holding an attended owner item until `run.owner-deadline`:
  dFurnishedOrders' (`cl-dClosedLoop-0207`) and dWellOiledMachine's.
- Holding a role item's dispatch at its `before` gate: the driver holds `--close` and the `--phase`
  move, and the dispatch of one item is dWellOiledMachine's executor.
- The breakpoint list's other sources, its hold and its `--plan` lines: TOOL-dDeclaredLoop-19's, landed.
- An item's actor and its declaration check: TOOL-dDeclaredLoop-9's; this unit reads the actor grammar only.
- `tools/unattended/unattended.sh`: no line moves, so no `fail`, `exit 1` or `status=1` site is added
  and its harness-arms ceiling is not touched. The loop and unattended kit versions are the lander's to
  mint at the push (`tools/push-main.sh@3a5bf825e879:27`).

### Edges

- **consumes-from** external — dDeclaredLoop's landed `derive_breakpoints`, `read_breakpoints` and its hold (TOOL-dDeclaredLoop-19, -52), the actor grammar (TOOL-dDeclaredLoop-9), `loop_lib.py --check` and its plants (TOOL-dDeclaredLoop-1, -67), and dGroundRules' standing `attendance` row
- **hands-off** `KICK-dKeptSession-41` — S1's standing `attendance` row, whose `summary` and `usage` that unit writes (id 45), and S7's anchor of `policy:attendance`, which that unit's reference page links to

## 4. Design

### Data model

```toml
# tools/loop/loop.toml, after [mail]
[[attendance]]
value = "unattended"
adds = []

[[attendance]]
value = "announce"
adds = ["announce", "ask-live"]

[[attendance]]
value = "confirm-steps"
adds = ["announce", "ask-live", "confirm-step-exit"]

[[attendance]]
value = "confirm-acts"
adds = ["announce", "ask-live", "confirm-before-act"]
```

### The closed interactions

| Member | Answers | Source |
|---|---|---|
| `announce` | `stand-in dWellOiledMachine`: the `step —` line before each act | P4; `cl-dClosedLoop-0304` |
| `ask-live` | `stand-in dFurnishedOrders`: owner questions asked live | P4; `cl-dClosedLoop-0207` |
| `confirm-step-exit` | an `owner gate` at each step's exit item | flow-steps' attendance rule |
| `confirm-before-act` | an `owner gate` before each role item | flow-steps' attendance rule |

`ATTENDANCE_INTERACTIONS` is a code constant mapping each member to its answer, never data, so a
definition cannot widen what attendance may do: deny by default. Every member is an owner interaction;
none is an item, an actor, the driver or a binding, which is the arm's whole predicate.

### The arm's refusals

| Shape | Refusal |
|---|---|
| `attendance` not an array of tables | `'attendance' is not an array of tables` |
| a row with no non-empty string `value` | `an attendance row carries no value` |
| a key but `value` and `adds` | `the attendance row <value> carries <key>, a key outside value and adds` |
| `adds` not a list of strings | `the attendance row <value> adds is not a list of members` |
| a member outside the set | `the attendance row <value> adds <member>, no member of ATTENDANCE_INTERACTIONS` |
| a value on two rows | `the attendance value <value> is given twice` |

The plants' breaks, on the `confirm-acts` row: `attendance-actor` sets `actor = {
"item.build.unit-pass" = "owner" }`, owed `(1, "loop: refused · ", "the attendance row confirm-acts
carries actor")`; `attendance-member` appends `driver:owner` to its `adds`, owed `(1, "loop: refused · ",
"adds driver:owner, no member of")`; `attendance-twice` appends a second `confirm-acts` row, owed `(1,
"loop: refused · ", "the attendance value confirm-acts is given twice")`.

### The list under each value

With no policy file `autonomy = "plan-only"` places one owner gate, at `item.plan.exit`, released by
`authorization`. Under `confirm-steps` the list adds a `held` gate with cause `attendance` at
`item.design.exit`, `item.build.exit`, `item.test.exit` and `item.deploy.close`, the four other step
exits of the `[[step]]` rows; under `autonomy = "every-stage"` each of those already holds `autonomy`'s
gate, so it adds none. Under `confirm-acts` the list adds one gate before each role item of the
composed rows, which in a tree with no composition are the definition's own
(`tools/loop/loop_items.py#read_composed_items`): 24 of the definition's 80 item rows (PINNED
2026-11-23 at `689698a5`, a `tomllib` read of `tools/loop/loop.toml`), the entry, review and probe
programs' role items among them, and unit 25's `item.entry.mailbox-answer`, a `command:` item, adds none.

The breakpoint plants owe, `<a>` an attendance gate line ending `· owner · attendance · held`:

| Plant, policy | Lines `list` owes |
|---|---|
| `attendance-values`, none | the `values` plant's default, the plan gate and the closing review, and no attendance line |
| `attendance-values`, `confirm-steps` | the plan gate, `<a>` at `item.design.exit`, the closing review, `<a>` at `item.build.exit`, `item.test.exit` and `item.deploy.close`, then `breakpoints: attendance · confirm-steps · adds announce ask-live confirm-step-exit · announce: stand-in dWellOiledMachine · ask-live: stand-in dFurnishedOrders` |
| `attendance-values`, `every-stage` and `confirm-steps` | the `values` plant's `every-stage` lines, then that attendance line |
| `attendance-values`, `confirm-acts` | one `<a>` `before` each role tag, their count the count of role items `read_items` reads in process |
| `attendance-values`, `announce` | the default lines, then AC4's attendance line |
| `attendance-missing`, `confirm-steps` | exit 2 and one line opening `breakpoints: refused · ` naming `attendance` and `confirm-steps` |
| `attendance-plan`, `confirm-steps` | `--plan`'s lines after `frontier:` equal to the list's, then the sourced `check_phase_gates <slug> SPECCING BUILDING` exit 1 naming `item.design.exit` in a check 82 refusal |

### What the arm does not check

It holds the declarations, not the rest of the tree: a key outside the loop kit that swaps an actor under
an owner-valued option (gap-flow-16's thirty) is not read here. It does not join the rows' values to the
catalogue's allowed set; S4's refusal of a value with no row is the runtime half of that join, and the
policy kit's reader refuses a value outside the catalogue's set before it. Whether a member's mechanism
has landed is not checked: the stand-in answer is typed in `ATTENDANCE_INTERACTIONS`.

### The shipped texts

| Text | Disposition |
|---|---|
| `tools/loop/breakpoints.py` docstrings: the module's THE LIST, THE READS and Exit paragraphs, `derive_breakpoints`, `read_policy_values`, `read_breakpoints` | edited with S4 and S6: each names `attendance`, the `[[attendance]]` rows, the attendance line and the refusal |
| `tools/loop/loop_lib.py` docstring, which gives `[mail]` a paragraph | edited with S2 and S3: a paragraph for `[[attendance]]`, its reader and arm |
| `tools/loop/loop.toml` header comment, one block per table | S2's comment above the rows, as `[mail]` carries |
| `tools/loop/kit.toml`, "breakpoints.py lists a build's reviews and owner gates from `autonomy`, `decisions.major`, `review.<stage>` and `review.breakpoints`" | edited, S9: `attendance` added, and the definition's `[[attendance]]` rows |
| `tools/loop/README.md`, its per-table sections, reader table, `--check` bullet and plant list | edited, S9: a section `## The attendance rows` after `## The mail kinds`, two reader-table rows, the `loop: attendance` line and the three S3 plants |
| `help/loop.md`, "four keys in", the hold paragraph's "Under the default `autonomy`", the list, fixture, "Read the loop" and "See a refusal" bullets | edited, S7 |
| `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`, `--plan`'s "the owner gates `autonomy` places" | edited, S9: "the owner gates `autonomy` and `attendance` place", and one sentence naming the attendance line before any `breakpoints: held` line; the two files stay byte-equal, as check 10 compares |
| `help/reference/policy.md`, `attendance` under "Not yet summarised" | stays: `tools/playbook/render_playbook.py#render_reference_page` lists a row lacking `summary` before it reads any anchor, and this unit writes no summary |
| `tools/policy/catalogue.toml`, `.governance/policy.json`, `tools/policy/unsummarised-keys.txt` | stay: no row or summary moves, so the mirror does not move |
| `tools/policy/presets.toml`'s `never` list | stays: the key is still on it |
| `tools/govkit/registry.toml`, the `loop breakpoint fixtures` exempt leg's `why` | stays: its list names examples, already not every plant, and each new plant builds its own scratch repository as it says |
| `tools/unattended/unattended.sh` comments above `print_breakpoint_lines` | stay: the lines are relayed verbatim, and under the default `unattended` a default build holds nothing new |
| `help/loop.md`, "Under the defaults nothing new is held" and the release paragraph | stay: true under the default `unattended`, and an attendance gate is released as every owner gate is |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `ATTENDANCE_INTERACTIONS`, `read_attendance`, `check_attendance_rows` | Python constant and functions, `tools/loop/loop_lib.py` | `py.function`, asked at the pass |
| `[[attendance]]` | table of `tools/loop/loop.toml` | none |
| `loop: attendance`, `breakpoints: attendance ·` | lines of `loop_lib.py --check` and `breakpoints.py list` | none |
| `attended`, `acts` | a breakpoint entry's key and a `facts` key of `breakpoints.py` | none |
| plants `attendance-actor`, `attendance-member`, `attendance-twice` | `PLANTS` cases of `loop_lib.py` | none |
| plants `attendance-values`, `attendance-missing`, `attendance-plan` | `PLANTS` cases of `breakpoints.py` | none |

### Migration

None. The default `unattended` adds nothing and prints no line, so every build's breakpoint list is
unchanged.

### Rollout

Live at landing; an owner who sets a value sees its gates on the next `--plan`.

### The budget rows

`check_plant_tokens` holds the `plants=<n>` token of each loop-kit row equal to `len(PLANTS)` of the
module its argv runs, once imported (`tools/run-gates/run-selftests.sh#check_plant_tokens`). Two rows
move, and no unit ordered before this one adds a plant to either module. `loop definition fixtures`
runs `loop_lib.py --selftest`, and S3's three plants move its token from 56 to 59 (DERIVED:
`len(PLANTS)` read at `689698a5`, 56, unit 5's `mail-kinds-repeated` landed). `loop breakpoint
fixtures` runs `breakpoints.py --selftest`, and S8's three plants move its token from 14 to 17
(DERIVED: `len(PLANTS)` read at `689698a5`, 14). The builder re-reads both counts at the unit's base
and sets each token three above it.

| Figure | `loop definition fixtures` | `loop breakpoint fixtures` |
|---|---|---|
| proxy reading `r` now, the row's note (PINNED 2026-11-22 and 2026-11-21) | 21.4 s over 56 plants | 88.3 s over 14 plants |
| this unit's plants, estimates (PINNED 2026-11-23) | 1 s each, 3 s | 4 s, 4 s and 20 s, 28 s |
| `r` after this unit (PINNED 2026-11-23, the sum) | 24.4 s | 116.3 s |
| budget, max of the row's value and 1.5 `r` | 60 stands over 37 | 317 stands over 175 |
| the leg's ceiling in `tools/gate-legs.json` (PINNED 2026-11-23) | 120, above 24.4 s | 300, above 116.3 s |

The `loop_lib.py` estimates are the `witness-actor-listed` plant's 0.2 s rounded up, each plant made
in memory (PINNED 2026-11-22). The `breakpoints.py` estimates are the `values` plant's 3.7 s for
`attendance-values` and `attendance-missing` (PINNED 2026-11-22), each over the scratch repository
`values` builds, and the `driver-plan` plant's 17.2 s for `attendance-plan`, which runs the driver's
`--plan` and one sourced `check_phase_gates`, rounded up to 20 s (PINNED 2026-11-22, by direct CLI at
`7df6a1dac`). The builder reads each new plant alone by direct CLI and appends `Then re-read by
KICK-dKeptSession-17 as PINNED proxy r <s>` to each row's note, each budget the row's value or 1.5 `r`
rounded up, whichever is higher. Neither leg has a row in `tools/run-gates/ceiling-evidence.txt`, so no
evidenced maximum moves.

### Files touched (estimate)

- `tools/loop/loop.toml`: the four rows and their comment
- `tools/loop/loop_lib.py`: the constant, the reader, the arm, its `--check` lines, its plants and the
  docstring paragraph
- `memory/map/generated/symbols.json`: `read_attendance` and `check_attendance_rows` added, the
  commit hook's regeneration; the plants are branches of `write_loop_plant` and
  `run_breakpoint_plant`, so they add none
- `tools/loop/breakpoints.py`: the read, the two facts, the attendance source, its line, its plants and
  the docstrings
- `tools/loop/kit.toml`: the breakpoints comment (S9)
- `tools/loop/README.md`: S9
- `tools/run-gates/selftest-budgets.txt`: the `loop definition fixtures` row's `plants=` token 56 to
  59 and the `loop breakpoint fixtures` row's 14 to 17, each note's re-read (DERIVED: `len(PLANTS)`
  at the unit's base), each token moved in place: the check refuses a note carrying two `plants=`
  tokens
- `help/loop.md`: S7, the attendance bullet and its anchor
- `memory/project/docs-undocumented.txt`: the `policy:attendance` row, taken off
- `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`: S9, the same bytes

### Alternatives rejected

- **Attended as a kind of session.** Dispatch 100's candidate, lost to the runtime text: it let the owner's
  session become the driver
  (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md@4f5e5809:88`).
- **A bundle of owner-valued keys.** Lost too: `placement: owner-places` swaps an item's actor
  (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md@4f5e5809:89`).
- **`[[stand-in]]` rows for the two stand-ins.** The table check reds a stand-in row naming no row item
  (`tools/loop/loop_table.py#check_transition_tables`), and neither interaction is an item; the stand-in
  rides on its member instead.
- **The `breakpoints: attendance` line under `unattended` too**, as rev-2 wrote. Every plant that
  compares a list's lines whole, and every default `--plan`, would gain a line that says nothing new.
- **`read_breakpoints` returning a pair, or `list` reading the policy again for the line.** The first
  moves every caller, `tools/loop/placement.py` among them; the second doubles the policy read per
  `list`. The `attended` key follows the landed `unopened` key's route to `main`.

## 5. Production-readiness checklist

- security — attendance can only add owner gates and interactions from a closed code set; it cannot take away
  a gate, change an actor or loosen a hold.
- perf / scale — one more policy key in the one read, one more definition read and four rows, per `list`.
- error / empty / loading states — a value with no row refuses the list, and the driver's `--close`
  with it; an unset key reads the catalogue default.
- observability — the `breakpoints: attendance` line under an attended value, and each gate's
  `breakpoint:` line with cause `attendance`.
- risks — a confirm value set while the owner is away holds the build at each gate; that is the value's
  meaning, and the deadline that ends such a wait is dWellOiledMachine's.
- testing — the plants and fixtures by a pass; the arms in §7 observed RED then GREEN by the main loop.
- migration — none.
- user docs — `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python breakpoints.py --fixture --plant attendance-values` runs `list` with no policy
  file, the list prints the same lines as the `values` plant's default and no `breakpoints:
  attendance` line, and the plant, once AC2 to AC4 hold too, prints `breakpoints: fixture ·
  attendance-values · held` and exits 0.
  Red when: the default adds a gate or a line.
- **AC2** — When the plant sets `attendance = "confirm-steps"`, the list adds an `owner gate` with cause
  `attendance` at each step's exit item but `item.plan.exit`, which `autonomy`'s gate already holds, and
  beside `autonomy = "every-stage"` it adds none.
  Red when: a step exit holds two gates, or one lacks its gate.
- **AC3** — When the plant sets `attendance = "confirm-acts"`, the list adds one `owner gate` with cause
  `attendance` before each item whose actor is `role:<slot>`, their count equal to what
  `python -I -c "import sys, pathlib; sys.path.insert(0, 'tools/loop'); import loop_lib as m; print(sum(str(r.get('actor', '')).startswith('role:') for r in m.read_items(pathlib.Path('tools/loop'))))"`
  prints at the repository's top level.
  figure: the count is DERIVED from the definition at observation time; PINNED 2026-11-23 at `689698a5`, 24.
  Red when: a role item is not gated, or a command item is.
- **AC4** — When the plant sets `attendance = "announce"`, the list adds no gate and ends with
  `breakpoints: attendance · announce · adds announce ask-live · announce: stand-in dWellOiledMachine · ask-live: stand-in dFurnishedOrders`.
  Red when: `announce` places a gate, or a stand-in prints as armed.
- **AC5** — When `python loop_lib.py --fixture --plant attendance-actor` runs, it exits 1 naming
  `attendance`, `confirm-acts` and `actor`; `attendance-member` names the member; `attendance-twice`
  names the value; and at the repository's top level
  `python -I -c "import sys, tomllib; sys.path.insert(0, 'tools/loop'); import loop_lib as m; print(m.check_attendance_rows(tomllib.load(open(sys.argv[1], 'rb'))['attendance']))" tools/loop/loop.toml`
  prints the four `loop: attendance` lines and an empty refusal list.
  Red when: a planted declaration that swaps an actor passes the check.
- **AC6** — When `python breakpoints.py --fixture --plant attendance-missing` runs `list` under
  `attendance = "confirm-steps"` with that row left out, the list exits 2 printing `breakpoints:
  refused · ` naming `attendance` and `confirm-steps`, and the plant prints its `held` line and exits
  0; and `--plant attendance-plan` has the driver's `--plan` print the list's lines after its
  `frontier:` line, each attendance gate's cause `attendance`, and the sourced `check_phase_gates`
  refuse the move across `item.design.exit`.
  Red when: a value with no declaration reads as `unattended`, or `--plan` derives its own list.
- **AC7** — When `python -c "import tomllib, sys; r=[k for k in tomllib.load(open(sys.argv[1], 'rb'))['key'] if k['name'] == 'attendance']; print(r[0]['owner'], r[0]['default'])" catalogue.toml`
  runs in the policy kit's directory, it prints `dKeptSession unattended`, true before this unit since
  S1 stands; `grep -c 'usage: policy:attendance ' loop.md` in `help/` prints 1; and at the repository's
  top level `grep -cP '^policy:attendance\t' memory/project/docs-undocumented.txt` prints 0.
  Red when: the key has no row, the page omits the rule, or the member is both anchored and listed.
- **AC8** — When, at the unit's commit,
  `python -I -c "import sys; sys.path.insert(0, 'tools/loop'); import loop_lib as m; print(len(m.PLANTS))"`
  runs, it prints the number that
  `grep -oP '^loop definition fixtures\t.*\Kplants=\d+' tools/run-gates/selftest-budgets.txt`
  prints after `plants=`; the same probe importing `breakpoints` prints the number
  `grep -oP '^loop breakpoint fixtures\t.*\Kplants=\d+' tools/run-gates/selftest-budgets.txt`
  prints after `plants=`; and S3's and S8's six plants are keys of the two `PLANTS`.
  Red when: either row still carries the count from before this unit's plants.
  figure: PINNED 2026-11-23 at `689698a5`, the probes print `56` and `14`, the greps `plants=56`
  and `plants=14`.
- **AC9** — When, at the repository's top level, `cmp tools/unattended/VERBS.template.md
  memory/guides/UNATTENDED-VERBS.md` runs it exits 0, and
  `grep -c 'owner gates .autonomy. and .attendance. place' tools/unattended/VERBS.template.md`,
  `grep -c '^## The attendance rows' tools/loop/README.md`,
  `grep -c 'five keys in' help/loop.md` and `grep -c 'Under the default .autonomy. and .attendance.' help/loop.md`
  each print 1, and `grep -c 'attendance' tools/loop/kit.toml` prints a count above 0, each 0 before
  this unit.
  Red when: a shipped text still names `autonomy` as the only source of owner gates.

## 7. Gates

`loop definition` · `loop definition fixtures` · `loop breakpoint fixtures` · `every held leg is budgeted, every budget row resolves` · `policy check` · `policy fixtures` · `unattended kit gate` · `docs` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_lib.py · covers AC5 · the three planted declarations under `--selftest`'s `PLANT_OWED`, staged against the base module, which reads no `[[attendance]]` row · the `loop definition fixtures` row's `plants=<n>` token rises by three

New arm: tools/loop/breakpoints.py · covers AC1 AC2 AC3 AC4 AC6 · each attendance value over the list, the missing row and the driver's `--plan`, under `--selftest`, staged against the base module, which reads no `attendance` · the `loop breakpoint fixtures` row's `plants=<n>` token rises by three

`policy check` reads the new literal read of `attendance` through its reader coverage, `docs` the
anchor and the list row S7 moves, and `unattended kit gate` the two VERBS files check 10 compares.

## 8. Open questions

- **F1 — Where is the "never selects an actor" rule enforced?** Options: (a) a closed interaction set in
  code, the declarations' members checked against it; (b) an invariance probe comparing each item's actor
  under every value with `unattended`; (c) both. (b) passes for every candidate, since no actor is ever read
  from `attendance`, so it cannot be seen red on the clause's planted value: a rehearsal, not a test.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the survivor that is seen red.
- **F2 — What is "an act" for `confirm-acts`?** Options: (a) an item whose actor is a role, the role act
  night-pass point 1 binds; (b) every item; (c) every tool call. (b) gates command and hook items the
  owner never sees run; (c) is a hook's surface and dWellOiledMachine's executor. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1: P4 names "each act's step and role".
- **F3 — Does an attendance gate stack on a position `autonomy` already gates?** Options: (a) one gate per
  position; (b) one per source. (b) asks the owner twice at one boundary for one confirmation.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3; the landed `write_line` keeps the gate already
  standing at a position and disposer, so autonomy's, written first, is the one kept.

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 17, v2's P4, its `attendance` row and
  its list of keys no preset sets, flow-steps' attendance rule, night-pass point 1, and
  TOOL-dDeclaredLoop-19, -9 and -13 read at origin's main.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-41` mirrored, the other ends of
  the edges the round-1 spec audit's promoted units declare; no other section moved.
- rev-3 · 2026-11-21 · §1 · S1 to S8 · §3 · §4 · §5 · AC1 to AC7 · §7 · §8 F2 F3 · §10 · re-grounded on
  the landed tree at `c2a407b0` by `2026-11-21-prompt-KICK-dKeptSession-17-orders-27-29-reground-brief`:
  narrowed S1 to its observation, the catalogue row and mirror entry standing, so no factory call and
  no catalogue file; S4 seamed into the landed `derive_breakpoints(values, steps, tags, facts)`, the key
  read by `read_policy_values` and the role tags handed as a fact; the reader spelled
  `read_attendance(kit_dir)` as the definition's other readers are; the line spelled with the module's
  `breakpoints:` head and printed only under an attended value; S5 states which driver checks hold
  which gate; S7 gains the docs anchor and its list row; S8 the plants, the arms moved from the absent
  `tools/loop/selftest.py` to the two modules' plants; every line citation re-cited by blob pin or
  symbol, and the leg line names the loop and docs legs.
- rev-4 · 2026-11-22 · S3 · S8 · §4 · §4 Files touched · AC8 · §7 · by
  `2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief`: S3's and S8's plants move two
  `plants=<n>` tokens `check_plant_tokens` grades, so `tools/run-gates/selftest-budgets.txt` joins
  Files touched, §4 states both rows' re-price over unit 5's plant, AC8 observes the tokens, and §7
  names the budget leg and `policy fixtures`, whose guard `tools/loop/loop.toml` trips.
- rev-5 · 2026-11-22 · S1 · S8 · §4 Files touched · AC1 · AC6 · §9 rev-1 · checked for behaviour by
  `2026-11-21-prompt-KICK-dKeptSession-11-precheck-brief`: the two new functions move
  `memory/map/generated/symbols.json`, which joins Files touched; each breakpoint plant's own verdict
  line and exit, which `run_selftest`'s one case reads, told apart from the exit of the `list` it
  runs; the `never` list re-cited to `tools/policy/presets.toml`; the `plants=` tokens moved in
  place; rev-1's line-number citations described, no positional token left standing.
- rev-6 · 2026-11-23 · §1 · S1 to S8 · S9 · §3 · §4 · §4 Files touched · §5 · AC3 · AC5 · AC6 · AC8 ·
  AC9 · §7 · §10 · re-grounded on `689698a5` under `2026-11-22-prompt-KICK-dKeptSession-17-reground-brief`,
  handed off by `2026-11-23-prompt-KICK-dKeptSession-17-1-spec-writer`: unit 5 landed, so the definition
  row reads 56 plants and its token 56 to 59; S3 states the arm's `(lines, refusals)` return, where
  `--check` prints it and §4 its refusal texts and plant needles; S4 states the ValueError and the
  `acts` fact; S6 the `attended` key and the line's place before `breakpoints: held`; S8 moves
  `attendance-plan` to the `write_position_plant` scratch `--plan` needs and binds `attendance-missing`'s
  rows by `patch.object`; S7 and S9 rewrite every shipped text the clauses made false, §4 listing the
  ones that stay; AC3 and AC5 observe by probe, not by the `loop definition` leg; AC9 is new; §7 names
  `unattended kit gate`; §3 states that `unattended.sh` does not move.

## 10. Reuse audit

The seam extended is the landed breakpoint list, `tools/loop/breakpoints.py#derive_breakpoints`, which
lists every breakpoint and keeps one gate per position through its `write_line`, with the policy read
`tools/loop/breakpoints.py#read_policy_values` and the hold the driver already reads
(`tools/unattended/unattended.sh#read_held_gates`); `autonomy`'s owner gates are the shape S4 follows,
and the `unopened` key's route to `main` the shape S6's `attended` follows. The arm sits in
`tools/loop/loop_lib.py#main`'s `--check` beside the declaration check
`tools/loop/loop_lib.py#check_item_declarations`, its reader beside
`tools/loop/loop_lib.py#read_mail_kinds`, its plants in `PLANTS` and `PLANT_OWED`, and the data in
`tools/loop/loop.toml` beside the `[mail]` table; all read at `689698a5`. Scout C's row named
`stand-in <owner>` rows for the two stand-ins; the landed table check reds a row naming no item, so
they ride on their members (§4). Night-pass's NP-23 gave the key to dDeclaredLoop and v2's catalogue
row names dKeptSession; v2 is the baseline. `python tools/codebase-map/reuse_lookup.py "place owner
confirmation gates at each step exit while the owner attends"`, re-run at `689698a5`, ranked `step`,
`read_steps`, `owners_of` and `read_step_composition` by name stem; `read_steps` is the step reader
`read_breakpoints` already calls, `check_gate_wall` is the driver's wall-clock ceiling, and none is a
breakpoint list, so no further seam fits.

Recall terms used: `python tools/memory-recall/query.py "how does attendance add owner gates without changing an item's actor" --terms "attendance unattended announce confirm-steps confirm-acts derive_breakpoints owner gate actor step announcement stand-in"`
