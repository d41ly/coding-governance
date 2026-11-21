# KICK-dKeptSession-17 — the attendance rule: `attendance` adds only the owner's interactions, its arm refusing any that swaps an actor

**Status:** DEFERRED · rev-3 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 27 · advances KICK-dKeptSession-29

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
| [2026-11-21-prompt-KICK-dKeptSession-17-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-17-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-17-orders-27-29-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-17-orders-27-29-reground-brief.md) | research | KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 |
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
through dDeclaredLoop's one breakpoint list, `derive_breakpoints` in `tools/loop/breakpoints.py`, its
interactions are a closed set declared as data, and its arm refuses any declaration that would select
an actor, the driver or a binding. The `step —` announcement and owner questions asked live are
stand-ins until dWellOiledMachine and dFurnishedOrders land them.

## 2. Scope (IN)

- **S1** — The key, standing at base. The catalogue row `attendance` (`tools/policy/catalogue.toml`,
  `name = "attendance"`, owner dKeptSession) holds the allowed values `unattended`, `announce`,
  `confirm-steps` and `confirm-acts` and the default `unattended`, and the JSON mirror
  `.governance/policy.json` holds the key. This unit writes neither file and runs no factory: the row's
  `summary` and `usage` are KICK-dKeptSession-41's. Presets never touch the key: v2 lists it among the
  keys no preset sets (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1434`),
  which KICK-dKeptSession-1's `never` list carries. Observed by AC7.
- **S2** — The declarations, `[[attendance]]` rows of `tools/loop/loop.toml`, one per value, each with
  exactly the keys `value` and `adds`, `adds` a list of members of the closed interaction set
  `ATTENDANCE_INTERACTIONS` in `tools/loop/loop_lib.py` (§4). `read_attendance(kit_dir)` beside
  `read_dispositions` returns `{value: adds}` once the arm holds. The shipped rows are §4's table, from
  flow-steps' attendance rule
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@d73cb002:558`):
  every attended value announces each act and asks owner questions live, `confirm-steps` adds a gate at
  every step's exit, `confirm-acts` one before every act. Observed by AC1 to AC4.
- **S3** — The arm, `check_attendance_rows(rows)`, run by `python tools/loop/loop_lib.py --check`
  (`tools/loop/loop_lib.py#main`), which prints one `loop: attendance <value> · adds <members|none>`
  line per row. A row carrying any key but `value` and `adds`, an `adds` member outside
  `ATTENDANCE_INTERACTIONS`, or two rows for one value is one refusal, printed `loop: refused ·` and
  naming `attendance`, the value and the key or member, exit 1. No member of the set names an actor,
  the driver or a binding, so a declaration that swaps an actor can only be written as one of those
  refused shapes. The plants `attendance-actor`, `attendance-member` and `attendance-twice` join
  `PLANTS` and `PLANT_OWED`, made in memory by `write_loop_plant`. Observed by AC5.
- **S4** — The breakpoint source, in `tools/loop/breakpoints.py`. `read_policy_values` reads
  `attendance` beside `autonomy`, as a literal at its `read_value` call
  (`tools/loop/breakpoints.py#read_policy_values`), so the catalogue default `unattended` answers where
  the policy file sets none. `read_breakpoints` hands `derive_breakpoints` two more facts: `attendance`,
  `read_attendance(KIT)`, and `acts`, the tags of the composed rows whose actor is `role:<slot>`
  (`tools/loop/breakpoints.py#read_build_item_rows`; the actor grammar of
  `tools/loop/loop_lib.py#check_item_declarations`). After `autonomy`'s gates, `confirm-step-exit`
  places an `owner gate` at each step's `exit` item and `confirm-before-act` one before each tag of
  `acts`, each with cause `attendance` and the disposer `owner`, through its `write_line`, which keeps
  the one gate already standing at a position (§8 F3). A value with no row is a ValueError naming
  `attendance` and the value, which `list` prints as its refusal, exit 2. Observed by AC1 to AC3 and
  AC6.
- **S5** — The hold is dDeclaredLoop's, and this unit adds no holding code: each gate S4 places reads
  `held` until the owner's disposition record of its tag releases it
  (`tools/loop/breakpoints.py#read_breakpoints`), the driver's `--close` refuses while one is held
  (`tools/unattended/unattended.sh#check_owner_gates`), a gate `at` a step exit also holds the `--phase`
  move across it (`tools/unattended/unattended.sh#check_phase_gates`), and `--plan` prints the module's
  lines verbatim (`tools/unattended/unattended.sh#print_breakpoint_lines`). Observed by AC6.
- **S6** — The stand-ins. `announce` answers `stand-in dWellOiledMachine`, the `step —` announcement of
  `cl-dClosedLoop-0304`; `ask-live` answers `stand-in dFurnishedOrders`, owner questions asked live of
  `cl-dClosedLoop-0207`. Under a value that adds a member, `python tools/loop/breakpoints.py list --build
  <slug>` ends its breakpoint lines with one line
  `breakpoints: attendance · <value> · adds <members> · <member>: stand-in <owner> …`, one stand-in
  clause per stand-in member; under `unattended` it prints no such line, so a default list is
  unchanged byte for byte. Each owner build arms its member by changing its entry in
  `ATTENDANCE_INTERACTIONS` in the same landing as its mechanism. Observed by AC1 and AC4.
- **S7** — The page `help/loop.md` gains, in its section "Where a build stops for a review or for
  you", an `attendance` bullet: the four values, what each adds, that no value changes an actor, the
  driver or a binding, which positions hold `--close` and which the `--phase` move, and the two
  stand-ins, with the docs anchor `<!-- usage: policy:attendance <fp8> -->`, the fingerprint
  `python tools/govkit/docs_leg.py --fingerprints` prints. The member `policy:attendance` comes off
  `memory/project/docs-undocumented.txt` in the same commit, since the docs leg reds a listed member a
  page anchors. Its fixture list names the plants S8 adds. Observed by AC7.
- **S8** — The plants of `python tools/loop/breakpoints.py --fixture --plant <case>`, each in `PLANTS`
  and run by `--selftest`: `attendance-values` (AC1 to AC4), `attendance-missing` (the `[[attendance]]`
  rows read with `confirm-steps` taken out, in memory) and `attendance-plan` (the driver's `--plan`
  under `attendance = "confirm-steps"`), each over the scratch repository `write_transition_plant`
  builds for the `values` plant. Observed by AC1 to AC4 and AC6.

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

### Edges

- **consumes-from** external — dDeclaredLoop's landed `derive_breakpoints`, `read_breakpoints` and its hold (TOOL-dDeclaredLoop-19, -52), the actor grammar (TOOL-dDeclaredLoop-9), `loop_lib.py --check` and its plants (TOOL-dDeclaredLoop-1, -67), and dGroundRules' standing `attendance` row
- **hands-off** `KICK-dKeptSession-41` — S1's standing `attendance` row, whose `summary` and `usage` that unit writes (id 45), and S7's anchor of `policy:attendance`, which that unit's reference page links to

## 4. Design

### Data model

```toml
# tools/loop/loop.toml
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

### The list under each value

At base `autonomy = "plan-only"` places one owner gate, at `item.plan.exit`, released by
`authorization`. Under `confirm-steps` the list adds a `held` gate with cause `attendance` at
`item.design.exit`, `item.build.exit`, `item.test.exit` and `item.deploy.close`, the four other step
exits of the `[[step]]` rows; under `autonomy = "every-stage"` each of those already holds `autonomy`'s
gate, so it adds none. Under `confirm-acts` the list adds one gate before each role item of the
composed rows, which in a tree with no composition are the definition's own (`read_composed_items`).

### What the arm does not check

It holds the declarations, not the rest of the tree: a key outside the loop kit that swaps an actor under
an owner-valued option (gap-flow-16's thirty) is not read here. It does not join the rows' values to the
catalogue's allowed set; S4's refusal of a value with no row is the runtime half of that join, and the
policy kit's reader refuses a value outside the catalogue's set before it.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `ATTENDANCE_INTERACTIONS`, `read_attendance`, `check_attendance_rows` | Python constant and functions, `tools/loop/loop_lib.py` | `py.function`, asked at the pass |
| `[[attendance]]` | table of `tools/loop/loop.toml` | none |
| `loop: attendance`, `breakpoints: attendance ·` | lines of `loop_lib.py --check` and `breakpoints.py list` | none |
| plants `attendance-actor`, `attendance-member`, `attendance-twice` | `PLANTS` cases of `loop_lib.py` | none |
| plants `attendance-values`, `attendance-missing`, `attendance-plan` | `PLANTS` cases of `breakpoints.py` | none |

### Migration

None. The default `unattended` adds nothing and prints no line, so every build's breakpoint list is
unchanged.

### Rollout

Live at landing; an owner who sets a value sees its gates on the next `--plan`.

### Files touched (estimate)

- `tools/loop/loop.toml`: the four rows
- `tools/loop/loop_lib.py`: the constant, the reader, the arm and its plants
- `tools/loop/breakpoints.py`: the read, the attendance source, its line and its plants
- `help/loop.md`: the attendance bullet and its anchor
- `memory/project/docs-undocumented.txt`: the `policy:attendance` row, taken off

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

## 5. Production-readiness checklist

- security — attendance can only add owner gates and interactions from a closed code set; it cannot take away
  a gate, change an actor or loosen a hold.
- perf / scale — one more policy key in the one read, and four rows, per `list`.
- error / empty / loading states — a value with no row refuses the list; an unset key reads the
  catalogue default.
- observability — the `breakpoints: attendance` line under an attended value, and each gate's
  `breakpoint:` line with cause `attendance`.
- risks — a confirm value set while the owner is away holds the build at each gate; that is the value's
  meaning, and the deadline that ends such a wait is dWellOiledMachine's.
- testing — the plants and fixtures by a pass; the arms in §7 observed RED then GREEN by the main loop.
- migration — none.
- user docs — `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python breakpoints.py --fixture --plant attendance-values` runs `list` with no policy
  file, it prints the same lines as the `values` plant's default and no `breakpoints: attendance` line.
  Red when: the default adds a gate or a line.
- **AC2** — When the plant sets `attendance = "confirm-steps"`, the list adds an `owner gate` with cause
  `attendance` at each step's exit item but `item.plan.exit`, which `autonomy`'s gate already holds, and
  beside `autonomy = "every-stage"` it adds none.
  Red when: a step exit holds two gates, or one lacks its gate.
- **AC3** — When the plant sets `attendance = "confirm-acts"`, the list adds one `owner gate` with cause
  `attendance` before each item whose actor is `role:<slot>`, their count equal to the count of
  `loop: item <tag> · role:` lines `python loop_lib.py --check` prints.
  figure: the count is DERIVED from the definition at observation time.
  Red when: a role item is not gated, or a command item is.
- **AC4** — When the plant sets `attendance = "announce"`, the list adds no gate and ends with
  `breakpoints: attendance · announce · adds announce ask-live · announce: stand-in dWellOiledMachine · ask-live: stand-in dFurnishedOrders`.
  Red when: `announce` places a gate, or a stand-in prints as armed.
- **AC5** — When `python loop_lib.py --fixture --plant attendance-actor` runs (`actor = {
  "item.build.unit-pass" = "owner" }` on the `confirm-acts` row), it exits 1 naming `attendance`,
  `confirm-acts` and `actor`; `attendance-member` (`adds = ["driver:owner"]`) names the member;
  `attendance-twice` names the value; and `python loop_lib.py --check` over the shipped rows exits 0.
  Red when: a planted declaration that swaps an actor passes the check.
- **AC6** — When `python breakpoints.py --fixture --plant attendance-missing` runs `list` under
  `attendance = "confirm-steps"` with that row left out, it exits 2 naming `attendance` and
  `confirm-steps`; and `--plant attendance-plan` has the driver's `--plan` print one `breakpoint:` line
  per gate the list prints, each attendance gate's cause `attendance`.
  Red when: a value with no declaration reads as `unattended`, or `--plan` derives its own list.
- **AC7** — When `python -c "import tomllib, sys; r=[k for k in tomllib.load(open(sys.argv[1], 'rb'))['key'] if k['name'] == 'attendance']; print(r[0]['owner'], r[0]['default'])" catalogue.toml`
  runs in the policy kit's directory, it prints `dKeptSession unattended`, true at base since S1 stands;
  `grep -c 'usage: policy:attendance ' loop.md` in `help/` prints 1; and at the repository's top level
  `grep -cP '^policy:attendance\t' memory/project/docs-undocumented.txt` prints 0.
  Red when: the key has no row, the page omits the rule, or the member is both anchored and listed.

## 7. Gates

`loop definition` · `loop definition fixtures` · `loop breakpoint fixtures` · `policy check` · `docs` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_lib.py · covers AC5 · the three planted declarations under `--selftest`'s `PLANT_OWED`, staged against the base module, which reads no `[[attendance]]` row · none

New arm: tools/loop/breakpoints.py · covers AC1 AC2 AC3 AC4 AC6 · each attendance value over the list, the missing row and the driver's `--plan`, under `--selftest`, staged against the base module, which reads no `attendance` · none

`policy check` reads the new literal read of `attendance` through its reader coverage, and `docs` the
anchor and the list row S7 moves.

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

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 17, P4 (v2:858-863), v2:1149 and :1434,
  flow-steps.md:543-560, night-pass point 1, and TOOL-dDeclaredLoop-19, -9 and -13 read at origin's main.
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

## 10. Reuse audit

The seam extended is the landed breakpoint list, `tools/loop/breakpoints.py#derive_breakpoints`, which
lists every breakpoint and keeps one gate per position through its `write_line`, with the policy read
`tools/loop/breakpoints.py#read_policy_values` and the hold the driver already reads
(`tools/unattended/unattended.sh#read_held_gates`); `autonomy`'s owner gates are the shape S4 follows.
The arm sits in `tools/loop/loop_lib.py#main`'s `--check` beside the declaration check
`tools/loop/loop_lib.py#check_item_declarations`, its plants in `PLANTS` and `PLANT_OWED`, and the data in
`tools/loop/loop.toml` beside the `[dispositions]` and `[[stand-in]]` tables; all read at `c2a407b0`. Scout
C's row named `stand-in <owner>` rows for the two stand-ins; the landed table check reds a row naming no
item, so they ride on their members (§4). Night-pass's NP-23 gave the key to dDeclaredLoop and v2's
catalogue row names dKeptSession; v2 is the baseline. `python tools/codebase-map/reuse_lookup.py "place
owner confirmation gates at each step exit while the owner attends"` ranked `step`, `read_steps`,
`owners_of` and `read_step_composition` by name stem; `read_steps` is the step reader `read_breakpoints`
already calls, and none is a breakpoint list, so no further seam fits.

Recall terms used: `python tools/memory-recall/query.py "how does attendance add owner gates without changing an item's actor" --terms "attendance unattended announce confirm-steps confirm-acts derive_breakpoints owner gate actor step announcement stand-in"`
