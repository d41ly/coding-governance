# TOOL-dWellOiledMachine-45 — the admission queue: every spawn and Workflow call waits its turn under `runtime.agents-in-flight`, clamped to the share it can hold, and handed to the executor past the hook's hold

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 37 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0323@eafe421b whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

A direct spawn over the agent limit is refused by the harness with "Do not retry", and only the
agents inside one Workflow run queue, by the harness's own per-run setting (gap-rt-36). The
in-flight ledger (TOOL-dWellOiledMachine-43) and the supervisor's reservations
(TOOL-dWellOiledMachine-9) count every agent, but each caller re-asks for room on its own: nothing
keeps them in order, a fan larger than any share waits for room it can never have, and a call that
outlives the hook's hold is denied. This unit is Runtime's admission queue (I24): every agent spawn
and Workflow call a driver, an executor or an attended session makes takes a FIFO ticket and starts,
in order, when the agents in flight and the outstanding reservations leave room for its reservation
under `runtime.agents-in-flight`, the in-flight ledger's one admission rule; it is never refused for
want of a slot, never starts over the limit, and past the hold is carried to the executor, its return
carried back (the owner's NT-28, the answers' review).

## 2. Scope (IN)

- **S1** — The one admission call (I24), `admit(call, reservation, wait_s=None)` in
  `tools/runtime/admission.py`. `call` names its `kind` (`agent` or `workflow`), its `owner`
  (`session:<id>` or `act:<act>`), its `run` and its `origin` (`hook`, `driver` or `executor`).
  It takes a ticket (S2), then polls every `ADMIT_POLL_SECONDS` (1): only the head ticket asks for
  room, by `add_reservation` (TOOL-dWellOiledMachine-9 S3) under the room rule TOOL-dWellOiledMachine-43
  applies in the mode `derive_inflight_mode` answers (its S2 and S9: `ledger` counts every slot
  against the limit, `split` counts direct spawns against `ceil(L / 2)` and holds a session's second
  Workflow run). Admitted, it gives up its ticket and returns `("admitted", res)`; `SlotsShort` keeps
  it waiting; with `wait_s` set it returns `("held", ticket)` at that bound, its ticket kept. It never
  returns a refusal for want of a slot, and nobody overtakes, so a fan-one call behind a fan-four
  call starts after it. The limit is re-read at each attempt (TOOL-dWellOiledMachine-9 S2). Observed
  by AC1, AC2, AC3.
- **S2** — The tickets, the FIFO the turnstile already keeps (`tools/run-gates/run-gates.sh:1474-1515`,
  "only the ticket that sorts first may claim"), extracted beside I22's slots at their second instance:
  `add_ticket(ledger, owner, run, size, pid)`, `read_queue(ledger)` and `remove_ticket(ledger,
  ticket)` in `tools/runtime/slots.py` (TOOL-dWellOiledMachine-9), each ticket a file
  `queue/<epoch ns>-<nonce>` under the ledger holding `owner`, `run`, `size`, `pid` and `kind`, and
  `remove_stale_tickets(ledger)` clearing, nonce-guarded as `remove_stale_slots` clears a slot, every
  ticket whose `pid` has exited, as `ts_sweep_queue` (`:1804`) sweeps a dead waiter. Observed by
  AC2, AC3.
- **S3** — The clamp, `derive_reservation(call, fan, limit, mode)`: an `Agent` call reserves 1; a
  `Workflow` call its declared fan (TOOL-dBoundRoles-22 S1, as TOOL-dWellOiledMachine-43 S2 reads
  it) or, when that is larger, the largest share it can ever hold: the limit under `ledger`, the
  Workflow share `L - ceil(L / 2)` under `split`, a share of 0 reading as 1, so no call waits on room
  it can never have. The harness's per-run setting, which TOOL-dWellOiledMachine-43 S9 renders at the
  key under `ledger` and at the Workflow share under `split`, throttles the clamped run's agents to it,
  and the harness's own settings stay the backstop above the queue. Observed by AC3, AC5.
- **S4** — The attended entry. The in-flight ledger's hold (`run_spawn_hold`,
  TOOL-dWellOiledMachine-43 S3, in `tools/runtime/inflight.py`) waits through `admit` with `wait_s`
  the claude-code adapter's `hook-hold-seconds` row (TOOL-dWellOiledMachine-1 S5) less 10 s, so held
  calls start in their order. Past the hold, where that unit's pack answers `deny` with I24's notice,
  the pack first hands the call to the executor: it writes the call's tool input beside its ticket as
  `<git-common-dir>/gov/admission/handed/<ticket>.json`, starts this session's executor where it hosts
  none, and its deny adds `handed to this session's executor as ticket <ticket>; its return: python
  admission.py wait <ticket>`. Observed by AC4.
- **S5** — The executor. `python supervise.py serve --session <id>` (I21's file,
  TOOL-dWellOiledMachine-6), its pid at `<git-common-dir>/gov/supervisors/session-<id>.pid`: for each
  handed ticket of its session, in order, it calls `admit` with no bound, launches the call as one act
  session through `launch_act(item, work_order, harness, env)` (I2), an `Agent` call as a work order
  of its `subagent_type` and `prompt` and a `Workflow` call as one of its script and clamped fan, and at
  the act's exit writes the session result's `structured_output`, or the failure, into the ticket's
  `return` and calls `remove_reservation`. It prints I24's notice while a ticket waits and exits after
  `EXECUTOR_IDLE_SECONDS` (300) with none. `python admission.py wait <ticket>` blocks until `return`
  is written and prints it, exit 0, or prints `admission — <ticket> · failed · <reason>`, exit 1. So
  no held call is silently denied, none starts over the limit, and its return reaches the session.
  Observed by AC4.
- **S6** — The driver's calls. The supervisor's reservation before each `launch_act`
  (TOOL-dWellOiledMachine-9 S5), which on `SlotsShort` launches nothing that beat, goes through
  `admit(call, reservation, wait_s=0)` with owner `act:<act>`: its ticket is kept across beats, so an act
  that found no room keeps its place and is launched, in order, at the first beat with room.
  Observed by AC6.
- **S7** — The notice, I24's spelling, `render_wait_notice(state)`: `admission — waiting · <n> in
  flight · <m> reserved · limit <k>`, printed by the executor and the supervisor while a call waits,
  and by `python admission.py status`, which adds one `ticket <t> · <owner> · <kind> · size <r>` line
  per waiting ticket, exit 0. Observed by AC7.
- **S8** — The entry's timeout. `settings-merge.py` writes `"timeout"` on each dispatcher entry whose
  packs' largest `budget-ms` exceeds 60000, as that budget in seconds rounded up, so the `PreToolUse`
  entry holding a call is not cut short by the harness's default; `inflight-admit`'s 600000 renders
  600. Observed by AC8.
- **S9** — The pages: `help/agent-limit.md` gains the queue, its order, the clamp, the executor and the
  `wait` remedy; `help/runtime.md` gains `admission.py` and its verbs. Observed by AC9.

## 3. Non-goals (OUT)

- The ledger's arming, its claims and releases at SubagentStart and SubagentStop, the split, the sweep
  keyed to the session's liveness and the per-run setting's render: TOOL-dWellOiledMachine-43. This
  unit orders the asking and clamps the size; the room rule stays that unit's.
- The slots themselves and the supervisor's reservation size: TOOL-dWellOiledMachine-9.
- The node's plan and hardware ledgers and `runtime.admission-scope`: TOOL-dWellOiledMachine-53,
  which grows `admit`.
- Hold ceilings and the deadlines of waits: TOOL-dWellOiledMachine-47.
- Showing the notice inside the harness while a hook still runs: whether a running hook's standard
  error is shown is the harness's, UNVERIFIED at this base; the notice reaches the deny, `status` and
  the executor's output.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-1` — `hook-hold-seconds`, the longest the hook may hold a call before handing it on
- **consumes-from** `TOOL-dWellOiledMachine-9` — `slots.py`, whose slots `admit` reserves and beside which the tickets live
- **consumes-from** `TOOL-dWellOiledMachine-43` — `admit`, which that unit's held call is taken into, and `derive_inflight_mode` with the room rule `admit` asks in each mode
- **consumes-from** `TOOL-dWellOiledMachine-10` — `dispatch.js`, whose entries' timeout S8 renders from the packs' `budget-ms`
- **consumes-from** `TOOL-dWellOiledMachine-6` — `supervise.py`, which gains the session executor and whose launches go through `admit`
- **hands-off** `TOOL-dWellOiledMachine-53` — `admit`, which that unit grows with the node ledgers' charge and the scope's checks
- **hands-off** `TOOL-dWellOiledMachine-47` — `admit`, whose held calls that unit gives a deadline and an outcome
- **consumes-from** external — TOOL-dBoundRoles-22's `[[workflow.stages]]` `fan`, the declared fan a Workflow call reserves

## 4. Design

### The queue

```
admit(call, reservation, wait_s)
  t = add_ticket(ledger, call.owner, call.run, reservation, pid)
  loop every ADMIT_POLL_SECONDS:
    remove_stale_tickets(ledger)
    mode = derive_inflight_mode(root); limit = resolve("runtime.agents-in-flight")
    r = derive_reservation(call, reservation, limit, mode)
    t is head of read_queue(ledger):
      try add_reservation(ledger, owner, run, r, pid, ttl) (43's room rule) -> remove_ticket; admitted
      except SlotsShort -> wait
    wait_s and waited >= wait_s -> held (ticket kept)
```

| Mode (`derive_inflight_mode`) | An `Agent` call's room | A `Workflow` call's room | A `Workflow` call's clamp |
|---|---|---|---|
| `ledger` | limit − slots held | the same | the limit |
| `split` | `ceil(L / 2)` − direct slots held | `L − ceil(L / 2)`, one live run per session | `L − ceil(L / 2)`, at least 1 |

### The attended path past the hold

```
PreToolUse Agent|Workflow -> dispatch.js -> inflight-admit (TOOL-dWellOiledMachine-43)
  run_spawn_hold -> admit(call, r, wait_s = hook-hold-seconds - 10)
    admitted -> allow
    held     -> handed/<ticket>.json ; supervise.py serve --session <id> unless live
             -> deny: I24 notice + "handed … ticket <t>; its return: python admission.py wait <t>"
supervise.py serve: admit(no bound) -> launch_act -> return into the ticket -> remove_reservation
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `admit` | function, `tools/runtime/admission.py` | I24's spelling; `admit` is no declared verb, one `VERB_OFFENDER_PIN` arrival in `.lexicon.conf`, as TOOL-dWellOiledMachine-1 kept `launch_act` |
| `derive_reservation`, `render_wait_notice` | functions, `admission.py` | `derive`, `render`, OK |
| `add_ticket`, `read_queue`, `remove_ticket`, `remove_stale_tickets` | functions, `tools/runtime/slots.py` | `add`, `read`, `remove`, OK |
| `wait`, `status`, `fixture` | `admission.py` verbs | none |
| `serve --session` | `supervise.py` verb | none |
| `ADMIT_POLL_SECONDS`, `EXECUTOR_IDLE_SECONDS` | constants | none |

### Files touched (estimate)

- `tools/runtime/admission.py` — S2, S3, S7 (new)
- `tools/runtime/slots.py` — S1
- `tools/runtime/inflight.py` — S4
- `tools/runtime/supervise.py` — S5, S6
- `tools/settings-merge.py` — S8
- `tools/runtime/selftest.py` — the arm in §7
- `.lexicon.conf` — the pin
- `help/agent-limit.md`, `help/runtime.md` — S9

### Alternatives rejected

- **A second admission pack beside `inflight-admit`.** Two `PreToolUse` packs would each count and hold
  the same call; the queue orders the one pack's asking instead.
- **Refusing past the hold with a retry hint.** The clause forbids a silent denial and a refusal for want
  of a slot; a retry hint leaves the model to poll, the refusal by another name.
- **The executor as a new process kind.** I21 is the executor; a session-keyed `serve` verb reuses its
  launch and its pid file, where a second launcher would duplicate both.

## 5. Production-readiness checklist

- security — no new write surface beyond node-local tickets under the git common dir; a handed call
  runs as an act session through the one launcher, under its preflight (TOOL-dWellOiledMachine-37).
- perf / scale — one poll a second per waiting call; the hold is bounded by the measured hook hold.
- error / empty / loading states — an `unmeasured` hold hands off at once; a dead waiter's ticket is
  swept so it blocks nobody; a failed act writes its failure into the ticket.
- observability — the notice from the deny, `status`, the executor and the supervisor.
- risks — a clamped Workflow run relies on the per-run setting to throttle its agents; a session
  started before a render keeps its settings (UNVERIFIED, `tools/hooks/agent-cap.js:1775`).
- testing — the criteria of §6 and the arms in §7.
- migration — none: an empty queue admits as the ledger does today.
- user docs — `help/agent-limit.md` and `help/runtime.md` (S9).

## 6. Acceptance criteria

Each fixture case runs `python admission.py fixture --case <name>` from the runtime kit directory
over a scratch git common dir, with `inflight.mode` and `runtime.agents-in-flight` planted as the case
names and SubagentStart and SubagentStop simulated through the ledger's own claim and release.

- **AC1** — When `--case seventh` runs with the limit at 6 and six agents in flight across three
  direct spawns and a three-agent Workflow run, a seventh direct `Agent` call and a seventh
  `Workflow` call each print `held`, never `refused`, and each prints `started` only after a planted
  SubagentStop frees a slot.
  Red when: `--case seventh --plant no-queue` passes both calls straight to the simulated harness,
  which prints `refused · direct spawn over 6`.
- **AC2** — When `--case two-fan-four` submits two fan-four `Workflow` calls under a limit of 6
  before the first run's first SubagentStart, the first prints `started · size 4` and the second
  `held`, and the second prints `started` only after the first run's four slots free.
  Red when: the second starts while the first holds its four, eight against six.
- **AC3** — When `--case clamp` enqueues a fan-four call under a limit of 3 with three agents in
  flight, then a fan-one call behind it, the first prints `size 3 · clamped from 4` and starts when
  the three free, and the fan-one call starts after it.
  Red when: the fan-four call waits past the fixture's bound for room of four, or the fan-one call
  starts first.
- **AC4** — When `--case outlives-hold` plants `hook-hold-seconds` at 12 and a first agent that
  outlives the hold, the held call's deny names its ticket, I24's notice and `admission.py wait`, the
  executor stub starts it only once a slot frees, and `wait` prints its return.
  Red when: the held call starts over the limit, or is denied with no reason line.
- **AC5** — When `--case split` plants `inflight.mode` as `split` under a limit of 6, a fan-five
  `Workflow` call prints `size 3 · clamped from 5`, and a fourth direct spawn prints `held` while the
  Workflow share stands free.
  Red when: the Workflow call reserves five, or the fourth direct spawn starts.
- **AC6** — When `--case driver` gives the supervisor a second fan-two act under a limit of 3 with a
  fan-two act in flight, the first beat prints I24's notice and keeps the act's ticket, and the beat
  after the first act's exit launches it ahead of a later act queued behind it.
  Red when: the waiting act loses its place to the later one.
- **AC7** — When `python admission.py status` runs during `--case seventh --pause-held`, it prints
  `admission — waiting · 6 in flight · 0 reserved · limit 6` and one `ticket` line per held call.
  Red when: a waiting ticket prints no notice.
- **AC8** — When `python tools/settings-merge.py` renders a pack table holding a `PreToolUse` pack
  of `budget-ms` 600000, the dispatcher entry carries `"timeout": 600`, and an event whose packs stay
  under 60000 carries none.
  Red when: the holding entry carries no timeout, or one below the pack's budget.
- **AC9** — When `grep -n "admission.py wait" help/agent-limit.md` runs, it names the remedy, and
  `grep -n "admission.py" runtime.md` over the runtime help page names its three verbs.
  Red when: either page omits them.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `straggler-guard arms` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/runtime/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · each fixture case, staged by its planted break: the queue passed through, a second call started early, an unclamped size, a held call started with no room, the split read as `ledger`, a ticket dropped across beats · none
New arm: tools/settings-merge.py · covers AC8 · its `--selftest` pack table with `budget-ms` 600000, staged by the timeout write removed · none

## 8. Open questions

- **F1 — How does a held call's return reach the session past the hold?** Options: (a) the deny names
  the ticket and the remedy `admission.py wait <ticket>`, which prints the return the executor wrote;
  (b) a Stop pack refusing the session's stop while a handed ticket is open; (c) the return injected at
  the session's next prompt. (b) adds a second refusal surface to every session and (c) delivers it a
  turn late. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the fewest new surfaces with the
  return delivered on the session's own call. widens: none · relaxes: none
- **F2 — Where do the tickets live?** Options: (a) beside I22's slots in `slots.py`, the turnstile's
  queue extracted at its second instance; (b) a queue of `admission.py`'s own. (b) is a second
  counting store beside the ledger the room is judged on, so a ticket and a slot could disagree.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the reuse rule's factory at the second
  instance. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended: I22's ledger `tools/runtime/slots.py` (TOOL-dWellOiledMachine-9), which gains the
turnstile's FIFO tickets (`tools/run-gates/run-gates.sh:1474-1515`, `ts_sweep_queue` at `:1804`), the
second instance of that queue; the in-flight ledger's hold (TOOL-dWellOiledMachine-43 S3), which now
waits through `admit`; the supervisor `supervise.py` (I21) as the executor; `launch_act` (I2) for the
handed act; settings-merge's render for the entry's timeout. `python
tools/codebase-map/reuse_lookup.py "hold an agent spawn in a FIFO queue until a slot frees instead of
refusing it"` ranked `queue` in `tools/run-gates/run-gates.turnstile.test.sh` first, the turnstile's
test helper, which confirms the turnstile as the shape; the rest were lexical neighbours. Scout A's
note holds against source: agent-cap counts no claims at this base and the limit is rendered into the
two variables at `tools/policy/policy.py:912`, so gap-rt-05's "45-minute window" is not today's code.
The brief's I22 names tickets that TOOL-dWellOiledMachine-9 did not ship; S1 adds them there.

Recall terms used: `python tools/memory-recall/query.py "how does an agent spawn over the limit wait
instead of being refused" --terms "admission queue agents in flight reservation fan hold case
PreToolUse executor Workflow share split fallback"`
