# TOOL-dWellOiledMachine-43 — the in-flight ledger: a slot per agent at SubagentStart and SubagentStop, Workflow reservations converted by run, a sweep keyed to the session's liveness, and its split fallback

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 36 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0321@f02a952d whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

Until an in-flight ledger arms, `runtime.agents-in-flight` binds direct spawns and each Workflow run
separately, so one session holds the limit in direct agents plus the limit per Workflow run, and a
direct spawn over it is refused with "Do not retry" rather than queued (gap-rt-35, gap-rt-36). The
harness's two concurrency settings are the only in-flight counters today (`tools/policy/policy.py:912`;
agent-cap's claim window retired with TOOL-dGroundRules-10, so gap-rt-05's 45-minute window no longer
exists at this base). This unit adds the hook pack that bounds the session's total: a direct or
Workflow spawn admitted only while agents in flight and reservations stay under the limit, a Workflow
call reserving its harness's declared fan, each agent's SubagentStart claim converting one slot of its
run's reservation, release at SubagentStop and at the run's saved result, and a sweep keyed to the
session's liveness. It arms only on the spike's four SubagentStop facts, and otherwise splits the limit
(night pass two `[p7-agent-cap]`; layer-runtime `[supervise]`, "Agents in flight").

## 2. Scope (IN)

- **S1** — The arming. `derive_inflight_mode(root)` in the new `tools/runtime/inflight.py` reads the
  rows `subagent-stop`, `subagent-stop-owner-stopped`, `subagent-stop-stalled` and
  `subagent-stop-killed` of `tools/runtime/harnesses/claude-code.toml`, written by
  TOOL-dWellOiledMachine-1 S5, through `read_capability` (TOOL-dWellOiledMachine-14 S3): all four
  `yes` is `ledger`, any other value `split`. `python inflight.py mode --write` writes the answer as
  the one line of the tracked `tools/runtime/inflight.mode`, and `mode --check` exits 1 when the file
  and a fresh derivation differ, so the mode is derived and checked both ways. Observed by AC1.
- **S2** — Admission, both modes. The pack `tools/runtime/inflight-admit.fragment.json` (I9:
  `PreToolUse`, matcher `Agent|Workflow`, class `refuse`, failure `open`, `budget-ms` 600000, key
  `runtime.agents-in-flight`) runs `inflight.py admit` through `pyrun.sh` (TOOL-dWellOiledMachine-8
  S3). An `Agent` call asks `add_reservation` (TOOL-dWellOiledMachine-9 S3) for one slot, run
  `call:<tool_use_id>`; a `Workflow` call asks for its harness's declared fan, the largest stage `fan`
  of the workflow whose `harness` is its `scriptPath` (TOOL-dBoundRoles-22 S1), except in an act
  session whose act already holds a supervisor reservation, which `set_reservation_run` re-keys to the
  call instead of reserving twice. Each slot's `owner` is `session:<session id>`. Observed by AC2, AC5.
- **S3** — The hold. A reservation refused by `SlotsShort`, or in `split` mode a `Workflow` call while
  the session's previous run has no saved result (S7), is held inside the entry: `run_spawn_hold`
  re-asks every 2 s and admits the call when it fits, for at most the `hook-hold-seconds` row
  (TOOL-dWellOiledMachine-1 S5) less 10 s, never a silent denial and never a start over the limit.
  Past that bound it answers `deny` with I24's notice
  `admission — waiting · <i> in flight · <r> reserved · limit <k>` and the hold it outlived; that answer is the place TOOL-dWellOiledMachine-45's
  queue takes over. Observed by AC3, AC4.
- **S4** — The run joined. `tools/runtime/inflight-launched.fragment.json` (`PostToolUse`, matcher
  `Workflow`, class `record`, failure `open`) runs `inflight.py launched`, which re-keys the call's
  reservation from `call:<tool_use_id>` to `run:<run id>`, the run id the tool's response names.
  Observed by AC5.
- **S5** — The claim at SubagentStart, `ledger` mode. `tools/runtime/inflight-start.fragment.json`
  (`SubagentStart`, class `record`, failure `open`) runs `inflight.py start`: `add_agent_slot`
  converts one unconverted slot of the agent's run's reservation by writing its `agent` id, so the
  agent is counted once. The run is the directory the agent's transcript sits in under
  `subagents/workflows/`, read from the payload where it names the path, else from the session's run
  journals' `started` line naming `agent_id` (`load_run_journal`, `tools/roles/handoff.py:686`); a
  direct agent converts its `Agent` call's slot, matched by `agent_type`; an agent matched to no
  reservation claims a fresh slot at the first free index, past the limit if it must, since a
  SubagentStart cannot refuse a start. Observed by AC3, AC5.
- **S6** — The release at SubagentStop, `ledger` mode. `tools/runtime/inflight-stop.fragment.json`
  (`SubagentStop`, class `record`, failure `open`, printing nothing) runs `inflight.py stop`:
  `remove_agent_slot` clears a direct or fresh slot, and returns a converted slot to its reservation by
  writing `agent` back to `-`, since a run may start more agents. Observed by AC5.
- **S7** — Released at the run's saved result. A run's saved result is the task notification its
  `Workflow` call receives in the session's transcript, read through `load_session_calls` and
  `NOTIFICATION_RE` (`tools/roles/handoff.py:576`, `:125`) from a byte cursor kept per session in the
  ledger, by `read_saved_result(transcript, run_id)`. Every pack run clears, nonce-guarded, the
  reservation of each run of its session whose result is saved. Observed by AC4, AC5.
- **S8** — The sweep keyed to the session's liveness, in place of a claim's expiry. Slots this unit
  writes carry `ttl` 0, which TOOL-dWellOiledMachine-9's `remove_stale_slots` never judges.
  `derive_harness_pid` walks the hook's ancestors through `scan_processes` and `build_self_chain`
  (`tools/process-monitor/census.py:260`, `scope.py:254`) to the first harness binary and caches its
  pid and image once per session under the ledger's `sessions/`; `remove_dead_session_slots`, run at
  most once a minute by any pack, clears every slot of a session whose cached pid no longer runs that
  image. Observed by AC6.
- **S9** — The split, when S1 answers `split`. The limit `L` divides as `ceil(L / 2)` for direct
  spawns and `L - ceil(L / 2)` for one live Workflow run per session. `render_settings` and
  `cmd_settings` in `tools/policy/policy.py` (TOOL-dGroundRules-10) render
  `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` as the first and `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`
  as the second when `inflight.mode` reads `split`, found through `resolve_kit_dir` as the policy kit
  already reaches the runtime kit (TOOL-dWellOiledMachine-1 S7), and as `L` each when it reads
  `ledger` or no runtime kit resolves. The settings check of the spawn guard, rule 7 in
  `tools/roles/spawn-guard.js` (TOOL-dBoundRoles-25 S2), compares against `policy.py settings --check`'s
  answer rather than against `L` twice. S2's admission counts direct slots against the first half
  and S3 holds the second Workflow call. Observed by AC7.
- **S10** — `python inflight.py status` prints
  `inflight — <mode> · <i> in flight · <r> reserved · limit <k>` and one line per session; `help/runtime.md` gains the ledger, the arming, the hold, the
  sweep and the split. Observed by AC8.

## 3. Non-goals (OUT)

- The admission queue past the hook's hold, FIFO and never refusing: TOOL-dWellOiledMachine-45.
- The supervisor's reservations for act sessions and the ledger's grammar: TOOL-dWellOiledMachine-9.
- Node-wide and pool scopes and the node ledgers: TOOL-dWellOiledMachine-53.
- The count of `agent()` calls inside a run between journal lines, and an adopter with no roles file:
  the harness's own per-run setting bounds both (night pass two, Left open).
- Measuring the four SubagentStop facts: TOOL-dWellOiledMachine-1's spike, re-measured by
  TOOL-dWellOiledMachine-36.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-1` — `hook-hold-seconds` and the four `subagent-stop` rows the ledger arms on
- **consumes-from** `TOOL-dWellOiledMachine-14` — `[[capability]]`, the four rows read through `read_capability`
- **consumes-from** `TOOL-dWellOiledMachine-10` — `dispatch.js`, on which the four packs register at `PreToolUse`, `PostToolUse`, `SubagentStart` and `SubagentStop`
- **consumes-from** `TOOL-dWellOiledMachine-9` — `slots.py`, the ledger whose slots the packs reserve, convert, return and clear
- **consumes-from** `TOOL-dWellOiledMachine-8` — `pyrun.sh`, through which every pack runs `inflight.py`
- **hands-off** `TOOL-dWellOiledMachine-45` — `admit`, which takes a held call past the hook's hold where S3 now answers with the admission notice, and `derive_inflight_mode`, whose mode decides the room `admit` asks for
- **consumes-from** external — TOOL-dBoundRoles-22's stage `fan`; TOOL-dBoundRoles-25's spawn guard and its settings rule; TOOL-dGroundRules-10's settings render

## 4. Design

### Evidence

- The limit is rendered into `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` and
  `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (`SETTINGS_VARS`, `tools/policy/policy.py:912`),
  `render_settings` setting both to `n` (`:915`), and agent-cap's rule 7 refuses a call while
  either differs from the limit (`checkSettingsInForce`, `tools/hooks/agent-cap.js:1779-1801`).
- SubagentStart is wired today only for `scratch-guard.js` context (`.claude/settings.json:111-117`),
  and its payload carries `agent_id` and `agent_type` (`tools/hooks/scratch-guard.test.sh:1193`);
  SubagentStop is unwired (gap-rt-07).
- A Workflow run journals `launched`, `started` and `result` lines and no run-level end
  (`journal.jsonl` of runs `wf_7c0507f0-43d` and `wf_82c1695c-11d` on this node, read 2026-10-26), so
  a run's end is read from its call's task notification, as `print_agent_lines` reads it
  (`tools/roles/handoff.py:848-870`).
- Night pass two measured 466 Workflow and 89 direct SubagentStart events in one session, and left
  open whether SubagentStop fires for a killed, stopped or stalled agent.

### The two modes

| | `ledger` | `split` |
|---|---|---|
| direct spawn | admitted while total + 1 ≤ `L` | admitted while direct ≤ `ceil(L/2)` - 1 |
| Workflow call | admitted while total + fan ≤ `L` | one live run per session, held while the last has no saved result |
| harness settings | `L` and `L` | `ceil(L/2)` and `L - ceil(L/2)` |
| agent slot | claimed at start, returned at stop | none: the harness's per-run setting bounds the run |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `inflight.py` with `admit`, `launched`, `start`, `stop`, `mode`, `status`, `--fixture` | runtime kit file | none |
| `derive_inflight_mode`, `derive_harness_pid`, `read_saved_result` | Python functions | `derive`, `read`, OK |
| `run_spawn_hold`, `add_agent_slot`, `remove_agent_slot`, `set_reservation_run`, `remove_dead_session_slots` | Python functions | `run`, `add`, `remove`, `set`, OK |
| `inflight.mode` | tracked one-line file | none |
| four `inflight-*.fragment.json` | hook packs | none |

### Files touched (estimate)

- `tools/runtime/inflight.py`, `tools/runtime/inflight.mode`, `tools/runtime/inflight-admit.fragment.json`,
  `tools/runtime/inflight-launched.fragment.json`, `tools/runtime/inflight-start.fragment.json`,
  `tools/runtime/inflight-stop.fragment.json` (new)
- `tools/runtime/slots.py`: `add_agent_slot`, `remove_agent_slot`, `set_reservation_run`
- `tools/policy/policy.py`: the split render
- `tools/roles/spawn-guard.js`: rule 7 compares against the render's own check
- `.claude/settings.json`, rendered by `policy.py settings --write` and the settings merge
- `tools/runtime/kit.toml`
- `help/runtime.md`

### Alternatives rejected

- **A claim's expiry, as agent-cap's 45-minute window had.** It admitted five more agents while the
  first five ran and refused a sixth over five idle claims (night pass two `[p7-agent-cap]`).
- **The split enforced by admission alone, settings left at `L`.** A Workflow run's agents are bounded
  only by the harness's per-run setting, so a five-lens review would run five agents beside
  `ceil(L/2)` direct ones.

## 5. Production-readiness checklist

- security — no new write surface beyond the node-local ledger; a held call never starts over the
  limit, and a call outliving the hold is denied with its reason, never run.
- perf / scale — one bash and one Python start per spawn and per agent start and stop; the census for
  the sweep at most once a minute; the hold polls every 2 s.
- error / empty / loading states — an unreadable capability row arms `split`; an unknown run claims a
  fresh slot, so the total is never undercounted.
- observability — `inflight.py status`, the held call's notice, and the mode line.
- risks — an agent mis-matched to another run's reservation returns its slot when that run's result
  arrives, so the total can read low until the agent stops; a direct slot whose stop never fires in
  `split` mode is held until the sweep, which under-admits and never over-admits.
- testing — the fixture cases of §6 and the arms of §7.
- migration — none: the mode file is written once from the landed rows; a node with no runtime kit
  renders the settings as today.
- user docs — `help/runtime.md`.

## 6. Acceptance criteria

The fixture is `python inflight.py --fixture --plant <case>`: a scratch repository under `%TEMP%` with
a short name whose policy file sets `runtime.agents-in-flight`, a stub capability table, a session
directory with run journals and a transcript, and hook payloads piped through each pack.

- **AC1** — When `--plant mode` sets all four rows `yes`, `inflight.py mode` prints `ledger`; with
  `subagent-stop-killed` `unmeasured` it prints `split`; and `mode --check` exits 1 over a mode file
  that disagrees with the rows.
  Red when: the ledger arms on an unmeasured row.
- **AC2** — When `--plant six` sets the limit to 6 with a three-agent Workflow running and admits one
  direct spawn, the spawn is admitted at once and `inflight.py status` prints `4 in flight`, in both
  modes.
  Red when: the direct spawn is held or refused.
- **AC3** — When `--plant total` with three Workflow agents in flight sends six direct spawns at a limit
  of 6, three are admitted and the fourth is held, and the session's total never passes 6; with the
  admission pack unwired the same plant reaches 9.
  Red when: the total passes the limit with the pack wired, or the unwired plant does not, which would
  make the case vacuous.
- **AC4** — When `--plant second-run` in `split` mode sends a second `Workflow` call while the first
  run has no saved result, the call is held, and once the plant appends the first run's task
  notification it is admitted within one poll; with `hook-hold-seconds` planted at 20 and no
  notification, it is denied after 10 s with the `admission — waiting` notice.
  Red when: the second call is refused while the hold lasts, or starts beside a live run.
- **AC5** — When `--plant convert` reserves a Workflow call of fan 3, re-keys it at `PostToolUse` and
  starts three of its agents, `status` reads `3 in flight · 0 reserved`, never 6; stopping one reads
  `2 in flight · 1 reserved`; appending the run's notification reads `0 in flight · 0 reserved`.
  Red when: an agent is counted twice, or the reservation outlives its run's result.
- **AC6** — When `--plant dead-session` caches a session's harness pid that no longer runs, the next
  pack run clears that session's slots and keeps a live session's.
  Red when: a dead session's slots stay, or a live one's are cleared.
- **AC7** — When `--plant split-render` at a limit of 6 then 5 runs
  `python tools/policy/policy.py settings --check` over a scratch settings file, `split` expects `3` and `3`, then `3` and `2`, and
  `ledger` expects `6` and `6`; with the runtime kit absent it expects the limit twice.
  Red when: the split mode renders the limit twice.
- **AC8** — When `grep -n "inflight\|hook-hold-seconds" runtime.md` runs over the help page, both are
  named.
  Red when: the page omits either.

## 7. Gates

`policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene`

The broad guard `{prefix}/` leaves the line by the checker's floor; the bar at the close runs it.

New arm: tools/runtime/inflight.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · each plant staged against an unwired admission pack, a start that claims fresh slots only, and a sweep keyed to a claim's expiry · none
New arm: tools/policy/check_policy.py · covers AC7 · the split plant staged against today's render, which writes the limit twice · none

## 8. Open questions

- **F1 — How is a Workflow run's budget held in `split` mode?** (a) The harness's per-run setting
  rendered as `L - ceil(L/2)`, the direct setting as `ceil(L/2)`, with the policy kit's render and the
  spawn guard's settings rule reading the mode; (b) admission alone, the settings left at `L`. (b)
  lets one run hold `L` agents beside `ceil(L/2)` direct ones, failing the clause's split. Rung 3, the
  only option meeting AC3 and AC7; the cross-kit read is the optional sibling read the policy kit
  already makes for the spike's launcher. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none ·
  relaxes: none
- **F2 — What happens to a call that outlives the hook's hold before TOOL-dWellOiledMachine-45 lands?**
  (a) A deny carrying I24's notice and the hold it outlived, the spot 45's queue replaces; (b) hold
  past the measured bound, where the spike records what the harness does to a timed-out hold. (b) is
  undefined behaviour by the spike's own row, `hook-hold-timeout`. Rung 3. RESOLVED (agent,
  2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended: TOOL-dWellOiledMachine-9's slot ledger, its grammar the run-gates turnstile's;
TOOL-dGroundRules-10's settings render (`tools/policy/policy.py:912-990`), given the split; the spawn
guard's settings rule, compared against that render; the platform's run journal and the session's
task notifications through `load_run_journal` and `load_session_calls` (`tools/roles/handoff.py:686`,
`:576`); and process-monitor's census for a session's liveness (`census.py:260`, `scope.py:254`).
Scout A's correction holds: GR:270 and GR:301 describe agent-cap's claim window, which is gone at this
base, and this spec cites the render instead. The probe `python tools/codebase-map/reuse_lookup.py
"claim a slot at SubagentStart and release it at SubagentStop"` ranked `claims`, `derive_run_starts`,
`write_claim` and `check_claim_push_lock_stale`; each is a run-claim or map-claim reader, none an
agent slot.

Recall terms used: `python tools/memory-recall/query.py "how does the in-flight ledger count agents
across direct and Workflow spawns" --terms "in-flight ledger SubagentStart SubagentStop agent_id
reservation convert sweep split fallback agents-in-flight"`
