# KICK-dKeptSession-17 — the attendance rule: `attendance` adds only the owner's interactions, its arm refusing any that swaps an actor

**Status:** DEFERRED · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 27 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0155@6d913746 whole
**Carries:** node:policy-key.attendance

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-18 KICK-dKeptSession-26 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

Attendance is not one rule today: about 30 catalogue keys carry an owner-valued option, and nothing stops a
posture from swapping an item's actor for the owner (`gap-flow-16`,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:122`). The owner's rule
is P4: attendance "adds only the owner's interactions: the announcement of each act's step and role, the
owner's confirmations at breakpoints, and owner questions asked live. It never changes an item, its actor,
the driver, a role's use or its enforcement" (v2:860-862). This unit carries `attendance` (v2:1149) as one
switch: its values place owner breakpoints through dDeclaredLoop's one breakpoint list, its interactions
are a closed set declared as data, and its arm refuses any value whose declaration would select an actor,
the driver or a binding. The `step —` announcement and owner questions asked live are stand-ins until
dWellOiledMachine and dFurnishedOrders land them.

## 2. Scope (IN)

- **S1** — The catalogue row `attendance`, allowed `unattended`, `announce`, `confirm-steps`,
  `confirm-acts`, default `unattended` (v2:1149), through
  `python tools/playbook/core.py new policy-key attendance --allowed <toml> --default <toml> --summary <text> --usage <text> --owner dKeptSession`
  (TOOL-dDeclaredLoop-6 S4). Presets never touch it (v2:1434; I1's `never`, KICK-dKeptSession-1's). Observed
  by AC7.
- **S2** — The declarations, `[[attendance]]` rows of `tools/loop/loop.toml`, one per value, each with
  exactly the keys `value` and `adds`, `adds` a list of members of the closed interaction set
  `ATTENDANCE_INTERACTIONS` in `tools/loop/loop_lib.py` (§4), read by `read_attendance(value)`. The shipped
  rows are §4's table, from flow-steps' `[breakpoint]`
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:558-560`): every
  attended value announces each act and asks owner questions live, `confirm-steps` adds a gate at every
  step's exit, `confirm-acts` one before every act. Observed by AC1 to AC4.
- **S3** — The arm, `check_attendance_rows(rows)`, run by `python tools/loop/loop_lib.py --check`: a row
  carrying any key but `value` and `adds`, an `adds` member outside `ATTENDANCE_INTERACTIONS`, two rows for
  one value, or a value with no row, is refused, naming `attendance`, the value and the key or member. No
  member of the set names an actor, the driver or a binding, so a planted value that swaps an actor can
  only be written as one of those refused shapes. Observed by AC5.
- **S4** — The breakpoint source, in `derive_breakpoints(policy, definition, build)`
  (TOOL-dDeclaredLoop-19 S1, `tools/loop/breakpoints.py`): `attendance` is read through the policy reader
  as `autonomy` is (TOOL-dDeclaredLoop-19 S3), with the catalogue default `unattended` until dGroundRules'
  reader lands. `confirm-step-exit` places an `owner gate` at each `[[step]]` row's `exit` item,
  `confirm-before-act` an `owner gate` before each item whose actor is `role:<slot>`
  (TOOL-dDeclaredLoop-9 S1's grammar), each with cause `attendance` and the disposer `owner`. A position
  that already holds an owner gate keeps its one gate. A value with no `[[attendance]]` row refuses the list,
  naming `attendance` and the value. Observed by AC1 to AC3 and AC6.
- **S5** — The hold is dDeclaredLoop's: each gate S4 places is held and released through
  TOOL-dDeclaredLoop-19 S6's one mechanism and printed by its `--plan` `breakpoint:` line (S9); this unit adds
  no holding code. Observed by AC6.
- **S6** — The stand-ins. `announce` answers `stand-in dWellOiledMachine`, the `step —` announcement of
  `cl-dClosedLoop-0304`; `ask-live` answers `stand-in dFurnishedOrders`, owner questions asked live of
  `cl-dClosedLoop-0207`. `python breakpoints.py list` prints one line
  `attendance — <value> · adds <members> · <member>: stand-in <owner> …`, and `adds none` under
  `unattended`. Each owner build arms its member by changing its entry in `ATTENDANCE_INTERACTIONS` in the
  same landing as its mechanism. Observed by AC4.
- **S7** — The page `help/loop.md` (TOOL-dDeclaredLoop-1's) gains an attendance section: the four values,
  what each adds, that no value changes an actor, the driver or a binding, and the two stand-ins.
  Observed by AC7.

## 3. Non-goals (OUT)

- The attend and unattend requests, the `attendance override` record and `attendance.scope`:
  dWellOiledMachine's (`cl-dClosedLoop-0281`), which writes the value this unit reads.
- The `step —` line itself and `next`, which renders it: dWellOiledMachine's (`cl-dClosedLoop-0304`).
- Owner questions asked live, and holding an attended owner item until `run.owner-deadline`:
  dFurnishedOrders' (`cl-dClosedLoop-0207`) and dWellOiledMachine's.
- The breakpoint list's other sources, its hold and its `--plan` lines: TOOL-dDeclaredLoop-19's.
- An item's actor and its declaration check: TOOL-dDeclaredLoop-9's; this unit reads the actor grammar only.

### Edges

- **consumes-from** external — dDeclaredLoop's `derive_breakpoints` and its hold (TOOL-dDeclaredLoop-19 S1, S3, S6, S9), the actor grammar (TOOL-dDeclaredLoop-9 S1), `loop_lib.py --check` (TOOL-dDeclaredLoop-1), the policy-key factory (TOOL-dDeclaredLoop-6 S4)
- **hands-off** `KICK-dKeptSession-41` — S1's `attendance` row, which that unit grounds on the standing catalogue row (id 45)

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
| `announce` | `stand-in dWellOiledMachine`: the `step —` line before each act | v2:860-861; `cl-dClosedLoop-0304` |
| `ask-live` | `stand-in dFurnishedOrders`: owner questions asked live | v2:861; `cl-dClosedLoop-0207` |
| `confirm-step-exit` | an `owner gate` at each step's exit item | flow-steps.md:560 |
| `confirm-before-act` | an `owner gate` before each role item | flow-steps.md:560 |

`ATTENDANCE_INTERACTIONS` is a code constant, never data, so a definition cannot widen what attendance may
do: deny by default. Every member is an owner interaction; none is an item, an actor, the driver or a
binding, which is the arm's whole predicate.

### What the arm does not check

It holds the declarations, not the rest of the tree: a key outside the loop kit that swaps an actor under
an owner-valued option (gap-flow-16's thirty) is not read here. It does not join the rows' values to the
catalogue's allowed set; S4's refusal of a value with no row is the runtime half of that join.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `ATTENDANCE_INTERACTIONS`, `read_attendance`, `check_attendance_rows` | Python constant and functions, `tools/loop/loop_lib.py` | `py.function`, asked at the pass |
| `[[attendance]]` | table of `tools/loop/loop.toml` | none |
| `attendance —` | line of `breakpoints.py list` | none |
| plants `attendance-actor`, `attendance-member`, `attendance-twice`, `attendance-missing` | fixture definitions | none |

### Migration

None. The default `unattended` adds nothing, so every build's breakpoint list is unchanged.

### Rollout

Live at landing; an owner who sets a value sees its gates on the next `--plan`.

### Files touched (estimate)

- `tools/loop/loop.toml`: the four rows
- `tools/loop/loop_lib.py`: the constant, the reader and the arm
- `tools/loop/breakpoints.py`: the attendance source and its line
- `tools/loop/selftest.py`: the arms the §7 line declares
- `tools/policy/catalogue.toml`: one row, through the factory
- `help/loop.md`

### Alternatives rejected

- **Attended as a kind of session.** Dispatch 100's candidate, lost to the runtime text: it let the owner's
  session become the driver (night-pass.md:88).
- **A bundle of owner-valued keys.** Lost too: `placement: owner-places` swaps an item's actor (:89).
- **`[[stand-in]]` rows for the two stand-ins.** TOOL-dDeclaredLoop-13 S8 reds a stand-in row naming no row
  item, and neither interaction is an item; the stand-in rides on its member instead.

## 5. Production-readiness checklist

- security — attendance can only add owner gates and interactions from a closed code set; it cannot take away
  a gate, change an actor or loosen a hold.
- perf / scale — one policy read and four rows per `derive_breakpoints` call.
- error / empty / loading states — a value with no row refuses the list; a reader refusal reads the default.
- observability — the `attendance —` line on every list and each gate's `breakpoint:` line with cause
  `attendance`.
- risks — a confirm value set while the owner is away holds the build at each gate; that is the value's
  meaning, and the deadline that ends such a wait is dWellOiledMachine's.
- testing — the plants and fixtures by a pass; the arms in §7 observed RED then GREEN by the main loop.
- migration — none.
- user docs — `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python breakpoints.py list` runs over DL-19's AC1 fixture with no policy file, it prints
  the same breakpoints as without this unit and the line `attendance — unattended · adds none`.
  Red when: the default adds a gate or prints no `attendance —` line.
- **AC2** — When the fixture sets `attendance = "confirm-steps"`, the list adds an `owner gate` with cause
  `attendance` at each step's exit item but `item.plan.exit`, which `autonomy`'s gate already holds, and
  under `autonomy = "every-stage"` it adds none.
  Red when: a step exit holds two gates, or one lacks its gate.
- **AC3** — When the fixture sets `attendance = "confirm-acts"`, the list adds one `owner gate` with cause
  `attendance` before each item whose actor is `role:<slot>`, their count equal to the count of such rows
  `python loop_lib.py --check` prints.
  figure: the count is DERIVED from the definition at observation time.
  Red when: a role item is not gated, or a command item is.
- **AC4** — When the fixture sets `attendance = "announce"`, the list adds no gate and prints
  `attendance — announce · adds announce ask-live · announce: stand-in dWellOiledMachine · ask-live: stand-in dFurnishedOrders`.
  Red when: `announce` places a gate, or a stand-in prints as armed.
- **AC5** — When `python loop_lib.py --check` runs over a fixture definition with the plant `attendance-actor`
  (`actor = { "item.build.unit-pass" = "owner" }` on the `confirm-acts` row), it exits 1 naming
  `attendance`, `confirm-acts` and `actor`; with `attendance-member` (`adds = ["driver:owner"]`) it names
  the member; with `attendance-twice` it names the value; and over the shipped rows it exits 0.
  Red when: a planted value that swaps an actor passes the check.
- **AC6** — When the fixture's policy file sets `attendance = "confirm-steps"` and the plant
  `attendance-missing` leaves that row out of the definition, `python breakpoints.py list` exits non-zero
  naming `attendance` and `confirm-steps`; restored, `unattended.sh --plan tFix` prints one `breakpoint:`
  line per gate the list prints, each attendance gate's cause `attendance`.
  Red when: a value with no declaration reads as `unattended`, or `--plan` derives its own list.
- **AC7** — When `python -c "import tomllib, sys; r=[k for k in tomllib.load(open(sys.argv[1], 'rb'))['key'] if k['name'] == 'attendance']; print(r[0]['owner'], r[0]['default'])" catalogue.toml`
  runs in the policy kit's directory, it prints `dKeptSession unattended`, and `grep -c 'attendance' loop.md`
  in `help/` prints at least 1.
  Red when: the key has no row, or the page omits the rule.
  fixture: the catalogue is dGroundRules', untracked at base until it builds.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC1 AC2 AC3 AC4 AC5 · each attendance value over the breakpoint list and each planted declaration under the check, staged against the base kit, which reads no `attendance` · none

The loop kit's own legs, `loop definition` among them, are TOOL-dDeclaredLoop-1's and absent from the
manifest at base; the arm above is read by the leg that runs `selftest.py` once it lands.

## 8. Open questions

- **F1 — Where is the "never selects an actor" rule enforced?** Options: (a) a closed interaction set in
  code, the declarations' members checked against it; (b) an invariance probe comparing each item's actor
  under every value with `unattended`; (c) both. (b) passes for every candidate, since no actor is ever read
  from `attendance`, so it cannot be seen red on the clause's planted value: a rehearsal, not a test.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the survivor that is seen red.
- **F2 — What is "an act" for `confirm-acts`?** Options: (a) an item whose actor is a role, the role act
  night-pass point 1 binds; (b) every item; (c) every tool call. (b) gates command and hook items the
  owner never sees run; (c) is a hook's surface and dWellOiledMachine's executor. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1: v2:861 names "each act's step and role".
- **F3 — Does an attendance gate stack on a position `autonomy` already gates?** Options: (a) one gate per
  position; (b) one per source. (b) asks the owner twice at one boundary for one confirmation.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3.

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 17, P4 (v2:858-863), v2:1149 and :1434,
  flow-steps.md:543-560, night-pass point 1, and TOOL-dDeclaredLoop-19, -9 and -13 read at origin's main.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-41` mirrored, the other ends of
  the edges the round-1 spec audit's promoted units declare; no other section moved.

## 10. Reuse audit

The seam extended is TOOL-dDeclaredLoop-19's `derive_breakpoints`, which lists every breakpoint and holds
each owner gate through one mechanism, and which leaves `attendance` to a later build in so many words
(its §3); its owner declarations from `autonomy` are the shape S4 follows. The arm sits in
TOOL-dDeclaredLoop-1's `loop_lib.py --check` beside TOOL-dDeclaredLoop-9's declaration check, and the
data sits in `tools/loop/loop.toml` beside the `[dispositions]` and `[[stand-in]]` tables. None of
`tools/loop/` exists at base: each cite is the parent spec read as `git show origin/main:<path>` at
`e5de11e9e`. Scout C's row named `stand-in <owner>` rows of TOOL-dDeclaredLoop-13 S8 for the two
stand-ins; that spec reds a row naming no item, so they ride on their members (§4). Night-pass's NP-23
gave the key to dDeclaredLoop and v2:1149 names dKeptSession; v2 is the baseline.
`python tools/codebase-map/reuse_lookup.py "place owner confirmation gates at each step exit while the
owner attends"` ranked `step`, `owners_of` and `check_gate_wall` by name stem, none a breakpoint list, so
no further seam fits. `python tools/memory-recall/query.py` returned scout C's row, flow-steps'
`[breakpoint]` and dDeclaredLoop's brief row for unit 19, which agree with the parent spec.

Recall terms used: `python tools/memory-recall/query.py "how does attendance add owner gates without changing an item's actor" --terms "attendance unattended announce confirm-steps confirm-acts derive_breakpoints owner gate actor step announcement stand-in"`
