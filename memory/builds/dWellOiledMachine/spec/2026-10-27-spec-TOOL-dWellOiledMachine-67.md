# TOOL-dWellOiledMachine-67 — launch_act branches on the measured values of `preset-session-id`, and `start-event` becomes a measured row

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 16 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-67-deviation-671.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-67-deviation-671.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 6, item H4, at HIGH. TOOL-dWellOiledMachine-32 S3 branches `launch_act` on
`preset-session-id` reading `true` or `false`, but TOOL-dWellOiledMachine-36 S2 measures that row as
`yes`, `returned` or `no`, and an unseeded row reads `unmeasured`; S3 also reads a `start-event` row
no unit names in `CAPABILITY_NAMES` or measures. On the shipped tables `launch_act` matches neither
branch, so whether a launch presets `--session-id` is undefined while the fixture, planting `true`
and `false`, passes. This unit spells the branch in the measured values, makes `start-event` a
measured row, and proves the launch through the shipped table.

## 2. Scope (IN)

- **S1** — The branch, in `launch_act` (`tools/runtime/launch.py`), on
  `read_capability("claude-code", "preset-session-id", <version>)` (TOOL-dWellOiledMachine-14 S3):
  `yes` generates the version-4 UUID and passes `--session-id <uuid>`, as 32 S3's preset half;
  `returned` reads the stream for the `start-event` row, as 32 S3's read half; `no`, `None`
  (`unmeasured` or absent) or any other value refuses the launch, returning nothing and printing
  `launch — refused · preset-session-id <value> · the act's session cannot be known`, since a pending
  record no reader can fill blocks every commit bound to the act (32 S4). A `returned` row whose
  `start-event` row reads `None` refuses the same way, naming `start-event`. Observed by AC1, AC2.
- **S2** — The `start-event` row. `CAPABILITY_NAMES` (`tools/runtime/harness.py`, 14 S1) gains
  `start-event`, whose value is `<type>:<field>`: the JSON object `type` of the first stream line that
  carries the harness session id, and the field that carries it. Both shipped tables seed it
  `unmeasured` (14 S2). Observed by AC3.
- **S3** — The measurement. `derive_conformance_rows` (`tools/runtime/conformance.py`,
  TOOL-dWellOiledMachine-36 S3) derives `start-event` from the recorded stream of its launch case, the
  first line whose object carries the session id the run reported, through the one derivation the
  live and replay arms share, and `--write` lands it beside `preset-session-id` (36 S4). Observed by
  AC3.
- **S4** — The fixture's tables re-spelled. `python act.py --fixture` plants `preset-session-id = "yes"`
  in its claude-shaped table and `"returned"` with a `start-event` row in its codex-shaped table, never
  `true` or `false`, and gains `--case shipped-table`, which runs `launch_act` against the shipped
  `tools/runtime/harnesses/claude-code.toml` and prints which branch it took. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- No new measurement of `preset-session-id`: TOOL-dWellOiledMachine-36 measures it.
- No change to the act record, its `session: pending` or `check_act_ready`.
- No harness other than `claude-code` launched: TOOL-dWellOiledMachine-1 S2's refusal of others
  stands.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-32` — `launch_act`'s session-id branch and `act.py`'s fixture, which this unit re-spells
- **consumes-from** `TOOL-dWellOiledMachine-36` — `derive_conformance_rows` and its value set for `preset-session-id`, which this unit's branch reads and which gains the `start-event` row
- **consumes-from** `TOOL-dWellOiledMachine-14` — `CAPABILITY_NAMES`, `read_capability` and the seeded tables `start-event` joins

## 4. Design

### Evidence

- 32 S3 branches on `true` and `false` (`spec-32.md:45-49`), and its fixture plants both
  (`spec-32.md:199-203`).
- 36 S2 measures `preset-session-id` as `yes`, `returned` or `no` (`spec-36.md:43`); 14 S2 seeds every
  unmeasured name `unmeasured`, which `read_capability` returns as None (`spec-14.md:44-50`).
- `start-event` appears in no spec but 32, and `CAPABILITY_NAMES` (`spec-14.md:33-41`) does not hold it.

### The branch

| `preset-session-id` | `start-event` | `launch_act` |
|---|---|---|
| `yes` | any | presets `--session-id <uuid>` |
| `returned` | a `<type>:<field>` value | reads the id from the stream |
| `returned` | None | refuses, naming `start-event` |
| `no`, None, other | any | refuses, naming `preset-session-id` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `start-event` | capability name | none |
| `shipped-table` | `act.py --fixture` case | none |

### Files touched (estimate)

- `tools/runtime/launch.py`
- `tools/runtime/harness.py`
- `tools/runtime/conformance.py`
- `tools/runtime/harnesses/claude-code.toml`, `tools/runtime/harnesses/codex.toml`
- `tools/runtime/act.py`

### Alternatives rejected

- **Reading `no` or `unmeasured` as "read the stream anyway".** A harness that returns no id would
  leave the act `pending` forever and refuse every commit bound to it later, where a refusal at launch
  names the cause once.

## 5. Production-readiness checklist

- security — deny by default: an unmeasured capability refuses the launch rather than guessing.
- perf / scale — none.
- error / empty / loading states — S1's refusal line names the row and its value.
- observability — `--case shipped-table` prints the branch the shipped table selects.
- risks — a node whose table was never measured launches no act until TOOL-dWellOiledMachine-36's live
  run writes the rows; that is the measured-facts rule of 14 S2.
- testing — AC1 to AC3 and the arm in §7.
- migration — none: the rows are added `unmeasured`.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

- **AC1** — When `python act.py --fixture --case shipped-table` runs, it prints
  `launch — branch preset`, `launch — branch returned` or `launch — refused · preset-session-id`,
  naming the value the shipped claude-code table holds, and never a fourth outcome.
  Red when: the shipped value selects neither branch and the launch proceeds undefined, as 32 S3's
  `true`/`false` compare does on a `yes` row.
- **AC2** — When `python act.py --fixture` runs its claude-shaped case with `yes`, its codex-shaped
  case with `returned` and a `start-event` row, and a planted `unmeasured`, the first argv carries
  `--session-id`, the second writes the stub's start-event id into the act record, and the third
  prints `launch — refused · preset-session-id unmeasured`.
  Red when: an unmeasured row launches.
- **AC3** — When `python conformance.py run --replay claude-code-2.1.292`
  runs, its rows include `start-event` with a `<type>:<field>` value, and `python harness.py --check`
  exits 0 over both tables.
  Red when: `start-event` is refused as an unknown name, or the replay derives no value.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/runtime/act.py · covers AC1 AC2 · the shipped-table and unmeasured cases staged against a branch comparing `true` and `false` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 6 (H4).

## 10. Reuse audit

The seam extended is TOOL-dWellOiledMachine-36's one derivation `derive_conformance_rows` and
TOOL-dWellOiledMachine-14's `read_capability`, both re-used as they stand; the branch stays in
`launch_act`. The probe
`python tools/codebase-map/reuse_lookup.py "choose the session id launch branch from a capability row value"`
ranked `rows`, `row`, `branches` and `extract_row` by name stem, none a capability reader, which is
unit 14's and unbuilt at this base: no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "how does launch_act preset or read the
harness session id" --terms "preset-session-id start-event capability row launch_act conformance
fixture measured value unmeasured"`
