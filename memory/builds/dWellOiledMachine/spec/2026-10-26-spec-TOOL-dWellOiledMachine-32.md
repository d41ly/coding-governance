# TOOL-dWellOiledMachine-32 — the act as the key: minted at launch with the harness session id, its record, its cost and duration, and the identity committed records may carry

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 15 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0310@6e643d4a whole
**Carries:** node:record-kind.act
**Carries:** node:policy-key.trace.identity
**Carries:** node:policy-key.trace.cost

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing keys a role act today: a session id keys only a per-session card and a run claim, the
per-agent ledger lines carry no cause, and the run log's schema refuses session ids outright
(gap-rt-25, gap-rt-27). P35 says every record names its cause and an act carries its own cost and
duration; P36 says no harness is the runtime
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1049-1056`).
This unit mints the act at launch with the harness session id, preset where the harness adapter's
row says so and else taken from its returned start event, holds `session: pending` and lets nothing
commit for the act until that id arrives, fails a launch whose start event never arrives, records the
act with its cost and duration from the session's JSON result as `trace.identity` and `trace.cost`
say, and makes the run log's closed-schema leg read the same key.

## 2. Scope (IN)

- **S1** — The act id (I15), `derive_act_id(node, instance_key, launch_utc)` in `tools/runtime/act.py`:
  `act-` and the first 12 hex digits of the SHA-256 of the three values joined by NUL, the instance
  key TOOL-dDeclaredLoop-7 S3's (I14). Deterministic for one input, distinct when any input differs.
  Observed by AC1.
- **S2** — The pending record, `<git-common-dir>/gov/acts/<act>.md`, node-local and never committed,
  one `key: value` line per field: `act`, `item`, `work-order` (the work order's key and `task-sha`),
  `harness`, `session`, `node`, `cause` (the instance key the act serves), `epoch` (the lease epoch, or
  `none`), `transcript=` (S6) and `state` (`launching`, `running`, `failed` or `ended`). Written by
  `write_act_pending` before the harness starts, with `session: pending` unless S3 presets it, and
  read by `read_act <act>`. Observed by AC2, AC3.
- **S3** — The session id at launch. `launch_act` (I2) mints the act and reads the harness adapter's
  `[[capability]]` row `preset-session-id` (I7): `true` makes it generate a version-4 UUID, pass it as
  `--session-id <uuid>` and write it into `session` before the spawn; `false` makes it read the
  harness's output stream line by line for the adapter's `start-event` row, a JSON object type and the
  field carrying the id, and write that id into `session` when it arrives. Observed by AC2, AC3.
- **S4** — No commit while pending. `check_act_ready <act>` exits 0 once `session` holds an id and 1
  while it reads `pending`, and it is the one predicate a committer asks before writing anything bound
  to the act: the commit queue and the binding writer read it (§3 Edges). Observed by AC3.
- **S5** — A start event that never arrives fails the launch. With `preset-session-id` `false`,
  `launch_act` waits at most `ACT_START_SECONDS` (60, read from `GOV_ACT_START_SECONDS` where set) for
  the start event; past it, it kills the process tree it launched, writes `state: failed`, prints
  `act — launch failed · <act> · no start event in <n>s` and returns exit 3. No committed record names
  the act. Seen on a Codex-shaped conformance row: an adapter table whose `preset-session-id` is
  `false`, planted over a stub binary that never prints its start event. Observed by AC4.
- **S6** — The transcript pointer, `transcript=<harness>:<session>`, which the binding (I16) carries
  and the act record copies; it resolves on the node holding the transcript through
  `resolve_session_tree` (`tools/runlog/extract.py:266`) and reads `not-local` on any other (P35).
  Observed by AC6.
- **S7** — The act record, kind `act`, a `[[record-kind]]` row in `tools/memory-tree/record-kinds.toml`
  (I1 of dTotalRecall): `tag = "record-kind.act"`, `layer = "runtime"`, `home` the build's `build/`
  folder, `id-rule = "<date>-build-<anchor id>-act-<act12>.md"`, `writer = "gov_record.py new act"`,
  its fields `Act`, `Item`, `Work-Order`, `Harness`, `Session`, `Node`, `Cause`, `Epoch`, `Transcript`,
  `Tokens-In`, `Tokens-Out` and `Wall`. `write_act_record <act> <result.json>` writes it once, at the
  act's exit, through TOOL-dTotalRecall-2's door `gov_record.py new act`, the anchor TOOL-dDeclaredLoop-3
  §8 F2's rule. Observed by AC5.
- **S8** — Cost and duration from the session's JSON result, never from a journal time of day (the
  owner's AP-21): `Tokens-In` and `Tokens-Out` from its `usage`, `Wall` from its `duration_ms`
  rendered by `render_wall` (`tools/roles/handoff.py:737`). `trace.cost`
  (`tools/policy/catalogue.toml:1572`) selects them: `tokens+wall` writes all three, `tokens` writes
  `Wall: withheld`, `none` writes all three `withheld`. Observed by AC5.
- **S9** — The identity committed records may carry, `trace.identity`
  (`tools/policy/catalogue.toml:1566`): under `trace.identity: session`, the default, the act record's
  `Session` and `Transcript` name the harness session id beside the act; under `act-only` both read
  `withheld`; under `salted` both read `withheld` until TOOL-dWellOiledMachine-33 supplies the keyed
  digest that value writes. Both keys are read through `resolve` (I31), run as
  `python <prefix>/policy/policy.py get <key>`. Observed by AC6.
- **S10** — The run log's closed-schema leg reads the same key. `RECORD_SCHEMA`
  (`tools/runlog/record.py`) gains the value classes `act-id` (`act-[0-9a-f]{12}`) and
  `harness-session` (the UUID shape of `SESSION_ID_RE`, `tools/roles/handoff.py:119`), and the record
  gains an `Acts` table, one row per act record of the run read through `record find`
  (TOOL-dTotalRecall-9): `act`, `session`, `tokens` and `wall`. `check_records` (`:1749`) reads
  `trace.identity` and refuses a `harness-session` value unless it is `session`, so the leg that
  refused every session id (`:8`) now refuses exactly what the key forbids. Observed by AC7.
- **S11** — The page `help/runtime.md` gains the act id, `session: pending`, the start-event bound, the
  act record's fields and the two keys' values. Observed by AC8.

## 3. Non-goals (OUT)

- The launcher, its argv and environment: `launch_act`, TOOL-dWellOiledMachine-1's; this unit adds the
  act and its session id to it.
- The binding record `refs/gov/bindings/<act>`: TOOL-dWellOiledMachine-39, which carries S6's pointer.
- The `Gov-Act:` and `Gov-Session:` trailers and `salted`'s per-node salt: TOOL-dWellOiledMachine-33.
- The supervisor launching acts and relaunching them: TOOL-dWellOiledMachine-6.
- Spend per build from the act records: TOOL-dWellOiledMachine-51. Admission charging an act:
  TOOL-dWellOiledMachine-53.
- Measuring `preset-session-id` and `start-event` on a real binary: the harness conformance fixture's
  rows; this unit reads them and plants its own.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-1` — `launch_act`, which S3 and S5 extend with the act's mint and its session id
- **consumes-from** `TOOL-dWellOiledMachine-14` — `[[capability]]`, the adapter's `preset-session-id` and `start-event` rows S3 reads
- **hands-off** `TOOL-dWellOiledMachine-39` — `act`, the act id the minimal binding names, and the readiness predicate it waits on while the session id is pending
- **hands-off** `TOOL-dWellOiledMachine-33` — `act`, the act record and its session field, from which the act and session trailers are written, and the salted digest S9 leaves withheld
- **hands-off** `TOOL-dWellOiledMachine-6` — `act`, minted at each launch the supervisor makes, and the act record writer it calls at the act's exit
- **hands-off** `TOOL-dWellOiledMachine-51` — `act`, the act records whose token and wall fields the spend reads
- **hands-off** `TOOL-dWellOiledMachine-35` — `act`, the act record whose session field joins an act to its session, and the act module where the act id grammar lives
- **hands-off** `TOOL-dWellOiledMachine-53` — `act`, the act whose launch admission charges
- **consumes-from** external — TOOL-dTotalRecall-2's `gov_record.py new` and `record-kinds.toml`, TOOL-dTotalRecall-9's `record find`, TOOL-dDeclaredLoop-7's instance key and TOOL-dDeclaredLoop-3's anchor rule, specced and unbuilt at base `0689e7fa`

## 4. Design

### Evidence

- A session id is matched by `SESSION_ID_RE` (`tools/roles/handoff.py:119`); a session's files are
  found by `resolve_session_tree` (`tools/runlog/extract.py:266`).
- A headless session's JSON result carries `session_id`, `duration_ms`, `total_cost_usd` and `usage`
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-floor-probes.md:313`).
- The run log's record is closed-schema and admits no session id by construction
  (`tools/runlog/record.py:5-9`); its schema leg is `check_records` (`:1749`).
- `trace.identity` and `trace.cost` have catalogue rows (`:1566`, `:1572`) and no reader at this base.
- The only per-agent cost today is `write_agent_ledger`'s line (`tools/roles/handoff.py:755`), keyed by
  nothing an act can join.
- v2's `trace.identity` row: "dLoggedFlight's run log keeps the closed schema whose leg refuses session
  ids … until dWellOiledMachine's act-key unit makes that leg read this key" (v2:1393).

### The pending record

```
act: act-3f9a1c0e2b7d
item: item.build.unit@pass-2#3f9a1c0e
work-order: wo-5d1e·task-sha 7c2a91b04e13
harness: claude-code
session: pending
node: d
cause: item.build.unit@pass-2#3f9a1c0e
epoch: 4
transcript=claude-code:pending
state: launching
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `derive_act_id`, `write_act_pending`, `read_act`, `check_act_ready`, `write_act_record` | functions | `tools/runtime/act.py` |
| `ACT_START_SECONDS`, `GOV_ACT_START_SECONDS` | constant, override | `tools/runtime/act.py` |
| `<git-common-dir>/gov/acts/` | node-local home | the pending records |
| `act` | record kind row | `tools/memory-tree/record-kinds.toml` |
| `act-id`, `harness-session` | value classes | `RECORD_SCHEMA`, `tools/runlog/record.py` |
| `Acts` | record table | `tools/runlog/record.py` |
| `act — launch failed` | output line | `tools/runtime/launch.py` |

Naming cells: each function is asked of `python tools/lexicon/lexicon.py --suggest <name> --as
py.function` at the pass.

### Migration

Additive: the record kind, the classes and the table are new, and a run with no act record renders
the table empty and says so in the record's own words. The leg's refusal narrows from every session
id to session ids under `act-only` and `salted`, so no landed record turns red.

### Files touched (estimate)

- `tools/runtime/act.py`
- `tools/runtime/launch.py`
- `tools/memory-tree/record-kinds.toml`
- `tools/runlog/record.py`
- `tools/runlog/selftest.py`
- `help/runtime.md`

### Alternatives rejected

- **Committing the act record at launch and amending it at exit.** The door is content-addressed and
  refuses a different value under one id (TOOL-dTotalRecall-2 S5); one write at exit carries every
  field.
- **The act id as the harness session id.** A Codex-shaped harness does not know its id until the
  start event, and one act may be relaunched into a second session (TOOL-dWellOiledMachine-6).

## 5. Production-readiness checklist

- security — under `act-only` and `salted` no harness session id reaches a committed record; the
  pending record is node-local under the git common dir.
- perf / scale — one record per act, written once; one door call.
- error / empty / loading states — a missing start event fails the launch with a named line and exit
  3; a missing JSON result writes `withheld` for cost and wall and says so.
- observability — every act is one pending file while live and one committed record after.
- risks — a harness whose start event shape changes reads as a failed launch until its `start-event`
  row is re-measured.
- testing — the fixture cases under AC1 to AC7 and the arms in §7.
- migration — §4 Migration.
- user docs — `help/runtime.md`, S11.

## 6. Acceptance criteria

`python act.py --fixture` builds a scratch repository under `%TEMP%` with a short name, two planted
adapter tables (`claude-shaped`, `preset-session-id = true`; `codex-shaped`, `preset-session-id =
false` with a `start-event` row) and three stub binaries: one printing its start event after one
second, one never printing it, one printing a JSON result.

- **AC1** — When `derive_act_id` is called twice with one input and once with another launch time, the first
  two return the same `act-` id of 12 hex digits and the third a different one.
  Red when: one input yields two ids, or two inputs one.
- **AC2** — When `launch_act` launches through the `claude-shaped` table, its argv carries
  `--session-id <uuid>` and the pending record reads that UUID in `session` before the stub starts.
  Red when: a preset adapter launches without `--session-id`, or its record reads `pending`.
- **AC3** — When `launch_act` launches the delayed stub through the `codex-shaped` table, the pending
  record reads `session: pending` and `check_act_ready` exits 1 within the first second, and after the
  start event the record holds its id and `check_act_ready` exits 0.
  Red when: a committer is told ready while `session: pending` holds.
- **AC4** — When the silent stub launches through the `codex-shaped` table with
  `GOV_ACT_START_SECONDS=2`, `launch_act` prints `act — launch failed · <act> · no start event in 2s`,
  exits 3, leaves no stub process alive and writes no committed record; `read_act` reads `state:
  failed`.
  Red when: the launch hangs, succeeds, or leaves the stub running.
  figure: the 2-second bound is PINNED for the fixture; the default 60 is the constant's.
- **AC5** — When `write_act_record` reads the stub's JSON result under `trace.cost = "tokens+wall"`,
  the committed `-act-<act12>.md` record carries `Tokens-In`, `Tokens-Out` and a `Wall` rendered from
  `duration_ms`; under `tokens` its `Wall` reads `withheld`; under `none` all three do.
  Red when: a cost field is filled from a journal time, or `none` leaves one filled.
- **AC6** — When the planted policy sets `trace.identity = "session"`, the record's `Session` holds
  the UUID and `Transcript` reads `transcript=claude-code:<uuid>`; under `act-only` and under `salted`
  both read `withheld`.
  Red when: a session id reaches the committed record under `act-only` or `salted`.
- **AC7** — When `python runlog.py check-records` grades a planted record whose `Acts` row carries a
  UUID under `trace.identity = "act-only"`, it refuses naming the `harness-session` class; under
  `session` it passes; and a planted act id of 11 hex digits is refused under either.
  Red when: the leg admits a session id the key forbids, or still refuses one the key allows.
- **AC8** — When `grep -n "session: pending\|trace.identity\|trace.cost" runtime.md` runs over the
  runtime kit's help page, each matches.
  Red when: the page omits one.

## 7. Gates

`runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene`

The record-kind registry's leg (TOOL-dTotalRecall-1) joins the manifest with dTotalRecall; the close
runs it where it exists.

New arm: tools/runtime/act.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the two adapter tables and three stubs, staged against a launcher that mints no act · none
New arm: tools/runlog/selftest.py · covers AC7 · a session id in an `Acts` row under each `trace.identity` value, staged against the base schema, which refuses every session id · none

## 8. Open questions

- **F1 — What does the pending record's session field spell?** (a) `session`, the clause's own token
  `session: pending`; (b) `harness-session`, I15's proposed spelling. (b) leaves the clause's token in no
  carrier; the I15 owner refines the spelling. Rung 1, the clause text. RESOLVED (agent, 2026-10-26,
  delegated): (a), and the committed field is `Session`. widens: none · relaxes: none
- **F2 — When is the act record committed?** (a) Once, at the act's exit, with every field; (b) at
  launch, then amended at exit. (b) is refused by the door, which never writes a different value under
  one id. Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a); S4's predicate is what holds a commit
  while the id is pending. widens: none · relaxes: none
- **F3 — What does `salted` write before its salt exists?** (a) `withheld`, until TOOL-dWellOiledMachine-33
  lands the per-node salt and the digest; (b) an unsalted hash. (b) is a guessable digest of a
  128-bit id with no key, which the row's "keyed hash" rules out (v2:1393). Rung 1. RESOLVED (agent,
  2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended are `launch_act` (I2), the harness adapter's capability rows (I7), TOOL-dTotalRecall-2's
record door and kind registry, the run log's closed schema and its leg (`tools/runlog/record.py:1749`),
`SESSION_ID_RE` (`tools/roles/handoff.py:119`), `resolve_session_tree` (`tools/runlog/extract.py:266`)
and `render_wall` (`tools/roles/handoff.py:737`). The probe
`python tools/codebase-map/reuse_lookup.py "mint an id for a launched headless session and record its
cost and duration"` ranked `records`, `extract_session` and `render_record` by name stem: the last is
the run log's renderer this unit extends, and none mints an act, so no existing seam fits the mint.
Scout A's line cites `record.py:8`, `:1749`, `handoff.py:737`, `:748` and `:755` hold at this base; its
`check_policy.py` launcher is unit 1's to extract.

Recall terms used: `python tools/memory-recall/query.py "how is a headless act session keyed and its
cost recorded" --terms "act id session pending start event harness session trace identity trace cost
act record"`
