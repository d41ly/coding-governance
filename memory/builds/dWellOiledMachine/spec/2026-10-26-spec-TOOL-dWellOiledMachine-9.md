# TOOL-dWellOiledMachine-9 — agent slots reserved under `runtime.agents-in-flight`: the slot ledger and the supervisor's reservations

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 35 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0287@1aa49fdd whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

Fan-out is bounded per prompt, not in flight, and headless launches are outside every count
(gap-rt-05): the only bound at this base is the harness's own concurrency settings, rendered from
`runtime.agents-in-flight` (`tools/policy/policy.py:912`), which see one session at a time. This unit
builds the slot ledger, I22, a counting semaphore of nonce-named slots in the run-gates turnstile's
grammar, and makes the supervisor reserve each act's declared fan against it before a launch, hold the
launch when slots are short, beat its reservations while the act runs, release them when the act
session exits or its tree is killed, and rebuild them when a restarted supervisor adopts an act
(layer-runtime `[supervise]`, "Agents in flight").

## 2. Scope (IN)

- **S1** — The ledger (I22). `tools/runtime/slots.py` keeps `<git-common-dir>/gov/slots/`, one per
  clone, so every session and supervisor of the clone counts against one ledger. A slot is a directory
  `slot.<k>`, claimed by one `mkdir` in index order as the turnstile's `resolve_free_slot` claims
  (`tools/run-gates/run-gates.sh:1626`), holding one-line files: `nonce`, `res` (its reservation's id),
  `owner` (`act:<act>`, or `session:<id>` for TOOL-dWellOiledMachine-43), `run` (`act:<act>` here),
  `agent` (`-` while reserved), `pid`, `heartbeat` (epoch seconds) and `ttl` (seconds). A slot
  directory with no `nonce` is an unfinished claim and is counted. Observed by AC1.
- **S2** — The limit, `runtime.agents-in-flight` (`tools/policy/catalogue.toml:478`, an agent count, 6
  by default, owned by dGroundRules), read once per call through `resolve` (`tools/policy/policy.py:752`,
  I31); a refused read takes the catalogue default and prints why. Observed by AC1.
- **S3** — `add_reservation(ledger, owner, run, size, pid, ttl)` counts the slot directories present and,
  when that count plus `size` exceeds the limit, raises `SlotsShort(in_flight, reserved, limit)` and
  writes nothing. Otherwise it claims `size` free slots among `slot.1` to `slot.<limit>` under one new
  reservation id, all or nothing: a claim lost to a concurrent `mkdir` releases what it took and raises
  `SlotsShort`. It returns the id. Observed by AC1, AC2.
- **S4** — `remove_reservation(ledger, res)` clears each slot of the reservation, nonce-guarded in the
  turnstile's order (TOOL-aPairedSlots-15, `ts_try_reap`, `run-gates.sh:1734`): the `nonce` is read
  first, `res` is checked, the `nonce` is read again, and the directory is cleared only when both reads
  agree, so a slot re-claimed between judgement and removal survives. `write_heartbeat(ledger, res)` rewrites
  each slot's `heartbeat`. `remove_stale_slots(ledger)` clears, under the same guard, every slot whose `heartbeat`
  is older than its own `ttl`. Observed by AC3, AC4.
- **S5** — The supervisor reserves (TOOL-dWellOiledMachine-6 S1, S4). Before each `launch_act`,
  `supervise.py` runs `remove_stale_slots`, then `add_reservation` with owner and run `act:<act>`, the work order's `fan` as its size and
  three `SUPERVISOR_BEAT_SECONDS` as its `ttl`, the work order's `fan` being its stage's declared `fan`
  (TOOL-dBoundRoles-22 S1, TOOL-dWellOiledMachine-1 S2). On `SlotsShort` it launches nothing that beat
  and prints `slots — <slug> · short · <i> in flight · <r> reserved · need <n> · limit <k>`, and the
  act waits for a later beat. Once the session starts it writes the session's pid into each slot. Each
  beat calls `write_heartbeat` on every reservation it holds. Observed by AC5.
- **S6** — Released at the act's end. At each `act-exit`, and when S7 of TOOL-dWellOiledMachine-6 or
  its reconcile kills an act's tree, `supervise.py` calls `remove_reservation` on that act's reservation; a
  supervisor that died without releasing leaves slots whose `heartbeat` stops, reaped once `ttl`
  passes. Observed by AC5.
- **S7** — Rebuilt at adoption. `set_adopted_slots(ledger, act, size, pid)` beats the act's slots where they
  remain, and otherwise reserves `size` slots for it with no limit check, since the act already runs,
  printing `slots — <act> · rebuilt · over limit <k>` when that exceeds the limit. The reconcile before
  the first beat (TOOL-dWellOiledMachine-6 S6) calls it for each adopted act and `remove_reservation` for
  each killed one. Observed by AC6.
- **S8** — `python slots.py status` prints `slots — <i> in flight · <r> reserved · limit <k>` and one
  `slot.<k> · <owner> · <run> · <agent> · heartbeat <age>s` line per slot; `python slots.py reap`
  runs `remove_stale_slots`. `help/runtime.md` gains the ledger, the reservation and the status line. Observed
  by AC7.

## 3. Non-goals (OUT)

- Claiming a slot per agent at SubagentStart, converting a reservation by its run, the split fallback
  and the sweep keyed to a session's liveness: TOOL-dWellOiledMachine-43.
- The admission queue, FIFO and never refusing for want of a slot, and its held-call notice:
  TOOL-dWellOiledMachine-45 over this ledger. Until it lands a short launch waits a beat.
- Counting across every project a node serves, the node ledgers and `runtime.admission-scope`:
  TOOL-dWellOiledMachine-53.
- The run-gates turnstile itself: it keeps its bash instance (§8 F1).
- The key's catalogue row and the harness's own settings: dGroundRules', TOOL-dGroundRules-10.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-6` — `supervise.py`, whose launch and S6 reconcile reserve, beat, release and rebuild an act's slots
- **hands-off** `TOOL-dWellOiledMachine-43` — `slots.py`, the ledger the in-flight pack claims agents' slots in and converts reservations of
- **hands-off** `TOOL-dWellOiledMachine-47` — `slots.py`, the act's reservation a nested spawn is charged against
- **hands-off** `TOOL-dWellOiledMachine-45` — `slots.py`, the ledger the admission queue admits a call against
- **consumes-from** external — TOOL-dBoundRoles-22's stage `fan`, carried by the work order dBoundRoles renders

## 4. Design

### Evidence

- The turnstile is a counting semaphore of beacon directories claimed by `mkdir` in slot order
  (`run-gates.sh:1626`), each holding `nonce`, `pid`, `heartbeat` and `ttl`, reaped dead or stalled per
  slot with the nonce read first and again before removal (`:1734-1770`) and released only under its
  own nonce (`ts_release`, `:1654-1659`).
- No supervisor-side counter exists; the limit reaches only the harness's two settings
  (`SETTINGS_VARS`, `tools/policy/policy.py:912`), which bound one session's direct spawns and one
  Workflow run.
- The turnstile moved its key from the common dir to a host dir because three repositories starved
  each other (`run-gates.sh:1474-1479`); this ledger stays per clone, and the host-wide scope is
  TOOL-dWellOiledMachine-53's.

### Data model

```text
<git-common-dir>/gov/slots/
  slot.1/  nonce  res  owner=act:act-0a1b2c3d4e5f  run=act:act-0a1b2c3d4e5f  agent=-  pid  heartbeat  ttl=180
  slot.2/  ...
```

`ttl` is three supervisor beats, 180 s at `SUPERVISOR_BEAT_SECONDS` 60, DERIVED from that constant.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `slots.py` with `status`, `reap`, `--fixture` | runtime kit file | none |
| `add_reservation`, `remove_reservation`, `write_heartbeat`, `remove_stale_slots`, `set_adopted_slots` | Python functions | `add`, `remove`, `write`, `set`, OK |
| `SlotsShort` | exception | `py.type`, OK |
| `<git-common-dir>/gov/slots/` | node-local ledger | none |

### Files touched (estimate)

- `tools/runtime/slots.py` (new)
- `tools/runtime/supervise.py`: reserve before launch, beat, release at exit and kill, rebuild at
  adoption
- `tools/runtime/kit.toml`
- `help/runtime.md`

### Alternatives rejected

- **A count kept in one file under a lock.** A crashed holder leaves the count wrong forever; a slot
  per directory is judged and reaped alone, the property the turnstile's slot-by-slot reap bought.
- **The turnstile moved onto this module.** §8 F1.

## 5. Production-readiness checklist

- security — a node-local write path under the common git directory only; no slot holds a secret.
- perf / scale — one directory listing per reserve; at most `limit` slot directories.
- error / empty / loading states — a refused limit read takes the default, named; a short reserve
  writes nothing.
- observability — `slots.py status`, and one `slots —` line per short launch or over-limit rebuild.
- risks — a lowered limit leaves slots above it until they release; the count check, not the slot
  index, bounds new reservations then.
- testing — the fixture cases of §6 and the arms of §7.
- migration — none: an empty ledger is created at the first reserve.
- user docs — `help/runtime.md`.

## 6. Acceptance criteria

The fixture is `python slots.py --fixture --plant <case>`: a scratch repository under `%TEMP%` with a
short name whose policy file sets `runtime.agents-in-flight` as the case says.

- **AC1** — When `--plant reserve` sets the limit to 6 and reserves 3, then 3, then 1, the first two
  return ids and `slots.py status` prints `6 in flight` counting reserved slots, and the third raises
  `SlotsShort` naming `limit 6`, with no seventh directory.
  Red when: a reservation passes the limit.
- **AC2** — When `--plant race` pre-creates `slot.5` and `slot.6` mid-reserve of 3 at a limit of 6 with
  four slots free at the count, `add_reservation` raises `SlotsShort` and leaves the ledger as it found it.
  Red when: a partial reservation stays.
- **AC3** — When `--plant nonce-swap` rewrites a slot's `nonce` between `remove_reservation`'s two reads, the slot
  survives; with the nonce unchanged it is removed.
  Red when: a re-claimed slot is removed.
- **AC4** — When `--plant stale` plants one slot whose `heartbeat` is older than its `ttl` and one fresh,
  `slots.py reap` removes the first only.
  Red when: a fresh slot is reaped or a stale one kept.
- **AC5** — When `python supervise.py --fixture --plant slots-short` runs at a limit of 2 over an act
  of fan 3, the beat prints `slots — fx · short` and the stub records no launch; at fan 2 it launches
  with 2 slots owned by the act, and after the act's exit `slots.py status` prints `0 in flight`.
  Red when: an act launches over the limit, or its slots outlive its exit.
- **AC6** — When `python supervise.py --fixture --plant slots-adopt` kills the supervisor while an act
  of fan 2 runs and the tick restarts it, the ledger again holds exactly 2 slots owned by the act, with
  their slots removed before the restart and present after it.
  Red when: the adopted act holds zero or four slots.
- **AC7** — When `grep -n "runtime.agents-in-flight\|slots —" runtime.md` runs over the help page, both
  are named.
  Red when: the page omits either.

## 7. Gates

`policy fixtures` · `lexicon naming predicates` · `memory hygiene`

The broad guard `{prefix}/` leaves the line by the checker's floor; the bar at the close runs it.

New arm: tools/runtime/slots.py · covers AC1 AC2 AC3 AC4 · each plant staged against `add_reservation` with the count check removed, `remove_reservation` with the second nonce read removed, and `remove_stale_slots` ignoring `ttl` · none
New arm: tools/runtime/supervise.py · covers AC5 AC6 · the two plants staged against a supervisor that launches without reserving and adopts without rebuilding · none

## 8. Open questions

- **F1 — Is the run-gates turnstile moved onto `slots.py` in this unit?** (a) No: the ledger adopts the
  turnstile's grammar, `mkdir` slots in index order, a nonce read first and again before removal, a
  heartbeat judged against the holder's own ttl, in Python for a Python supervisor and its hook packs,
  and the bar's bash turnstile stays as it is; (b) re-point the turnstile's claim, reap and release
  onto `slots.py`, so the bar's runner shells to Python at every tick of its queue and the run-gates kit
  requires the runtime kit. (b) puts a kit dependency and a new process on the merge bar's critical
  path for a clause about agent slots, and the bar's FIFO queue is TOOL-dWellOiledMachine-45's to
  extract. Rung 3: (b) trips veto 2's new dependency, so (a) is the most capable survivor; I22's word
  "extracted" is taken as the grammar adopted, which this writer's return names to the main loop.
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — What is an act's reservation size?** (a) The work order's `fan`, its stage's declared `fan`;
  (b) the harness's agent cap, `cap`. (b) reserves for the worst case on every act and starves the
  ledger; layer-runtime `[supervise]` names "the act's declared fan". Rung 1. RESOLVED (agent,
  2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seam is the run-gates turnstile's grammar (`tools/run-gates/run-gates.sh:1474-1515`, `:1626`,
`:1654`, `:1734`), adopted slot for slot, and the supervisor's launch, beat and reconcile
(TOOL-dWellOiledMachine-6 S1, S4, S6), which call it. The limit is read through the one reader,
`resolve` (`tools/policy/policy.py:752`); TOOL-dBoundRoles-22 S5's `read_agent_limit` reads the same
key inside the roles kit, which the runtime kit does not require. The probe
`python tools/codebase-map/reuse_lookup.py "reserve agent slots against a counting semaphore with
nonce beacons"` ranked `counts`, `measure_typed_counts`, `renderAgentLabel` and `beacon`
(`tools/run-gates/run-gates.turnstile.test.sh`), the last the turnstile's own suite helper; scout A's
row 5 and its shared interface 4 hold at this base.

Recall terms used: `python tools/memory-recall/query.py "how does the supervisor reserve agent slots
before launching an act" --terms "supervisor reservation agents-in-flight slots fan turnstile beacon
nonce reap counting semaphore"`
