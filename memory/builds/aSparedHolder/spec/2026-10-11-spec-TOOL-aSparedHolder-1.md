# TOOL-aSparedHolder-1 — the resume tick kills only what it launched, and a resumed session waits for its background work

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node a · Tier-1 · base 69e0ff0f · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aSparedHolder-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aSparedHolder-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The resume tick killed aFrugalTurnstile's live interactive session on 2026-10-10 and relaunched it
headless seven times, losing its background work at every turn end. This unit makes the tick report
a live session it did not launch instead of killing it. It also makes a resumed `claude -p` wait for
its background Workflows and agents, and makes a resumed session delete the idle-wakes it inherited.

## 2. Scope (IN)

- **S1 — a live recorded pid the tick did not launch is reported.** In `resume-tick.sh`, a STALE (or
  FINISHED-UNSTAMPED, stale) run whose `pid-alive` is `yes`, with no live launch of the tick's own,
  prints `skip · STALE OVER A LIVE PID · pid <pid> is alive and this tick did not launch it, so
  nothing is killed or launched`. It appends one `stale-live-pid` health line and probes no login.
  `--dry-run` prints the line and appends nothing. A live launched pid keeps its kill, since a
  resumed session that hung is the tick's own. Observed by AC1.
- **S2 — the resumed CLI waits for its background work.** The launcher exports
  `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0`. Observed by AC2.
- **S3 — a resumed session reaps the idle-wakes it inherited.** The CONTINUE payload opens by
  deleting every idle-wake job the scheduler lists, before the one it schedules. Observed by AC3.
- **S4 — the protocol states the idle-wake's silence as measured** and names the tick's new rule, in
  §5. It stays byte-identical to its render, at or under its size row. Observed by AC4.

## 3. Non-goals (OUT)

- **New liveness signals.** The evidence in §4 shows no signal was there to add: no bar ran, no
  task was registered, and the gate-logs directory was empty. A new signal would have kept the run
  STALE, so `derive_last_move` and the verdict every reader shares stay as they are.
- **The stop-guard.** With the ceiling off, the CLI keeps the process alive past the turn end, so
  allowing that turn end is right in both modes. A guard that refused it in `-p` would spend turns
  against `--max-turns` while waiting.
- **The idle-wake's delivery.** The harness owns it, and the docs do not promise it fires in the
  desktop Code tab. The protocol already demotes it from keepalive; this unit corrects its stated
  evidence.
- **The aFrugalTurnstile build**, which closes in its own session.
- **An `unattended.test.sh` arm.** The driver does not change, so no driver fixture can go red.

### Edges

- A recorded pid that is alive but sits outside the launched tree, while the launch is also alive,
  is still killed with the launched tree. That pair means the tick's own resumer is the lease holder,
  because `--resume --keepalive-id` re-records the pid.

## 4. Design

### The evidence (session c43608a7, its transcript and its sidecar)

- 02:24Z — the main loop launched Workflow `w14k1r7r6` and ended its turn. The main transcript
  stayed silent from then until 04:38Z.
- 02:31:49Z — the Workflow's agent entered one Bash call. Its transcript under
  `subagents/workflows/wf_4c570d2b-e94/` never moved again, and the gate-logs directory held nothing.
- 04:38:44Z — attempt 1. `--liveness` read STALE with `pid-alive yes`, and the tick killed pid
  34476, the owner's interactive desktop session, then launched `claude -p --resume`.
- Every `.out` from attempts 1 to 7 opens with the CLI's own line: background tasks were still
  running 10 minutes after the last turn, so it stopped them, and
  `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0` waits indefinitely. Attempts 2 to 7 found `pid-alive no`.
- Across every transcript on node a, 150 CronCreate prompts were scheduled and 444 deliveries were
  found. Session c43608a7 scheduled ten and received none in 30 hours, with a background task pending
  through every idle gap. The peer session counted nine still listed and deleted them.

### Measured on node a, 2026-10-11, CLI 2.1.292, `claude -p --model haiku`

- A background Bash `sleep 40` with the ceiling at 0 and at 5000 ms: both waited and took the
  follow-up turn. The ceiling does not hold back a shell the main conversation started.
- A background agent running `sleep 45`: at 5000 ms the CLI printed the stop line and exited after
  `WAITING`. At 0 it waited and took the follow-up turn, and the marker file was written.

### The rule

The tick kills only processes it launched. A live session it did not launch belongs to whoever
started it, and the tick cannot tell idle-on-error from waiting on a hung agent. The owner can, and
the health log carries the line the orientation card counts. The STALE verdict stays: it is
accurate, since nothing moved.

### Files touched (estimate)

- `tools/unattended/resume-tick.sh`
- `tools/unattended/resume-tick.test.sh`
- `tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md`

### Alternatives rejected

- **Count a running bar's beacon or a task heartbeat as a move.** Neither existed in the incident.
- **Refuse a `-p` turn end in the stop-guard.** The CLI already has the switch, and the guard cannot
  see the session's task list.
- **Forbid background spawns in the payload.** The unit builder is a Workflow, so a resumed run
  could not build at all.

## 5. Production-readiness checklist

- security — narrows a destructive action; no new write path.
- perf / scale — N/A — one comparison per bound run per tick.
- error / empty / loading states — dry-run names the report and writes nothing.
- observability — one `stale-live-pid` health line per tick while the condition holds.
- risks — a genuinely hung interactive session is no longer auto-recovered; the health line is its
  signal. A resumed `-p` whose Workflow hangs never exits, and the tick's hung-launch row kills it
  past the stale bound.
- testing — RED then GREEN arms in `resume-tick.test.sh` (§6).
- migration — N/A.
- user docs — the protocol's §5 and the tick's header table.

## 6. Acceptance criteria

- **AC1** — When `resume-tick.test.sh` runs its AC4 arm, a STALE fixture whose recorded pid is a live
  `sleep` prints the `STALE OVER A LIVE PID` line, the sleep is still listed, the stub saw nothing,
  no attempt line exists, and the health log holds one `stale-live-pid` line naming the pid.
  Red when: the arm passes against the tick at BASE, which kills the sleep and launches attempt 1.
  cost: about three minutes on node a, where one tick takes up to a minute.
- **AC2** — When the AC1 arm launches the stub, the stub logs `bgwait 0`, the value of
  `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` it inherited. Red when: the tick at BASE launches it and the
  stub logs `bgwait unset`.
- **AC3** — When the AC1 arm launches the stub, its argv carries
  `delete every idle-wake job your scheduler lists`. Red when: the payload at BASE lacks it.
- **AC4** — When `cmp` compares the protocol template with its render, they match, and
  `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` passes against its row.
  Red when: either differs or the size exceeds the row.

## 7. Gates

`unattended kit gate` · `kit version markers` · `memory hygiene` · `unattended protocol size`

New arm: tools/unattended/resume-tick.test.sh · covers AC1 · the tick at BASE kills the live sleep · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the owner's prompt and the evidence in §4.

## 10. Reuse audit

No new helper. The report reuses `add_health_event`, `resolve_health_log` and `print_decision`
from the tick and its library; the launcher keeps its three lines and gains one export.
