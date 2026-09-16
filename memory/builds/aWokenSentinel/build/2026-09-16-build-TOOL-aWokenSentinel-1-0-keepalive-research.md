# Keepalive alternatives — the research that precedes the specs

**Serves:** research TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6
**Commissions:** TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-4 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6

Run 2026-09-13 on node `a` as a four-agent workflow — three research lenses (harness docs, this
repo's records, a live probe of the node) and one skeptic prompted to refute — 106 tool uses, 581k
sub-agent tokens. The journal is a session artifact; every fact below carries its basis, and the
basis is the only thing that makes a line here worth more than the prose it replaces.

## 1. The question, and the rule that answers it

The owner's observation: the `CronCreate` keepalive fires only when it is the sole background task
in its session, so a run that stalls with anything else pending is never woken, and runs stall on
API unavailability and session limits and never resume.

The answering rule is the charter's own: **a guard that shares a variable with the thing it guards
is not a guard.** The cron job shares the run's process, event loop and account. So a mechanism
counts as covering a stall class only when it sits in a different failure domain for that class.
This is the ranking rule every verdict in §4 applies.

## 2. Stall classes

| Class | Shape |
|---|---|
| A | the turn ended on an error and the session sits idle — API 5xx after retries, a context error |
| B | mid-turn hang — a tool call or background task that never returns |
| C | app or process dead — crash, reboot, app closed |
| D | a usage-limit lockout lasting hours (weekly limit) |
| E | the agent stopped on purpose to wait for an owner who is absent (parked, then quiet) |

## 3. What was measured

### 3.1 The records (basis: documented in this tree; file:line as cited)

Six recorded stalls of unattended runs, one adopter hang, four sub-agent deaths:

| Run | Date | Class | What happened | Resumed by |
|---|---|---|---|---|
| aPromptedMandate | 2026-08-18 | C twice, then E | three keepalives across two process deaths; two recorded dead were still firing (`RUN.md:30`) | a human, twice |
| dCarriedReceipt | 2026-08-25 | D then E | node d's session ended on its weekly limit (`RUN.md:87`) | node a, by hand, cross-node |
| aGroundedOrientation | 2026-08-27 | E | parked a fix during orientation, no keepalive yet; re-parked after being told to proceed | the owner's turn |
| aUnblockedFleet | 2026-08-31 | E | parked a collision, reaped its keepalive, stopped at BUILDING (`RUN.md:42`) | never |
| aClosedDocket | 2026-08-31 | unknown | last rows a BLOCKED review and a dispatch; keepalive reaped; quiet at BUILDING | never |
| aQuenchedHarness | 2026-09-07 | tick fired | the one recorded cron tick that became a turn; spent asking the owner a question (`RUN.md:45`) | itself, later |
| dPinnedVintage (adopter) | 2026-08-27 | B then C | `--close` at 3h19m with parent gone, 0 s CPU; produced `GATE_BOUND` | killed by an operator |
| four Tier-2 reviews | 08-16..09-05 | D/A in sub-agents | verify or synthesis stages died on a usage or session limit | a human, from the journal |

**Zero recorded stalls were cleared by the CronCreate keepalive.** Every resume was a human-started
session. Four of six stalls are class E.

The driver records a `keepalive` id and no session id; no liveness, lease or heartbeat field
exists (`set_fact` keys measured: anchor-*, base, branch-*, grain, halt-code, keepalive,
landed-anchor, mode, phase, pieces, playbook, records, units-at-landing, unpushed-at-landing,
witness). Six `RUN.md` files are non-terminal today with CLOSED or DEFERRED READMEs, so a resumer
keyed on `phase:` alone would fire on all six forever.

Prior art outside the repo: two desktop-app scheduled tasks from July 2026 on this node
(`~/.claude/scheduled-tasks/resume-*`), fresh session per fire, git-signal collision check, and a
recorded refusal to self-delete. Neither records ever having resumed a build.

### 3.2 The harness (basis: documented, code.claude.com/docs)

- `CronCreate` fires "between your turns, not while Claude is mid-response", only while idle; the
  store is in-memory, session-scoped, 7-day expiry. The docs do not define idle against a pending
  background task; the owner's claim is unmeasured anywhere in this tree.
- `Stop` fires when Claude finishes responding and CAN block: `{"decision":"block","reason":…}`
  continues the conversation. `StopFailure` fires when the turn ends on an API error — matchers
  `rate_limit`, `overloaded`, `server_error`, `max_output_tokens`, `authentication_failed`, … —
  and its output is discarded; it can run a shell.
- Every hook event's stdin JSON carries `session_id` and `transcript_path`.
- Cross-session `SendMessage`: an idle receiver starts a new turn; a busy one reads the message
  between tool calls and a running tool is never interrupted.
- Desktop scheduled tasks: a fresh session per fire, only while the app is open, catch-up on launch
  for the most recent missed fire only, no self-deletion.

### 3.3 The node (basis: measured on node `a`, 2026-09-13)

- Inside a session's Bash env: `CLAUDE_CODE_SESSION_ID` equals the transcript uuid; `CLAUDE_PID`
  names a live `claude.exe`; `CLAUDE_CODE_HOST_SESSION_ID` is the app's separate `local_…` id.
  A sub-agent sees the PARENT's session id.
- The standalone CLI was NOT logged in; a nested `claude -p` does not inherit the app's in-process
  auth; `CLAUDECODE` is not a nesting guard (unsetting it changes nothing). The owner logged the CLI
  in on 2026-09-16, verified `loggedIn:true`.
- `claude -p --resume <uuid>` accepts `--dangerously-skip-permissions` and `--permission-mode
  bypassPermissions`; the session lookup runs BEFORE the auth check; `--session-id` with `--resume`
  needs `--fork-session`.
- A failed `-p` launch still writes a transcript jsonl whose last assistant entry carries
  `isApiErrorMessage:true`, `apiErrorStatus`, `error` — measured for an auth error only.
- `schtasks /create /sc minute /mo 10` works unelevated; the task is `Logon Mode: Interactive
  only`; `/ru SYSTEM` and `/rl HIGHEST` are refused without elevation.
- The desktop app's own task registry and `~/.claude/scheduled-tasks/` have diverged: two dirs
  the app does not list, one listed task whose dir is gone.
- No `Stop` hook is wired anywhere on the node.

## 4. Verdicts, by the failure-domain rule

| Mechanism | Covers | Does not | Verdict |
|---|---|---|---|
| 1 CronCreate (status quo) | A, idle-and-clean only | B (no turn end), C, D, E (reaped on park by design) | fallback: the idle-wake, not the keepalive |
| 2 ScheduleWakeup / loop | nothing beyond 1 | same domain | reject |
| 3 Stop hook, session-bound, bounded | E — the trigger IS the decision to stop; the aClosedDocket shape too | A, D (StopFailure fires there and cannot block), B, C | recommend, with the guard in §5 |
| 4 watchdog session, same app | A when idle; B only if `stop_session` unsticks a hung tool (unmeasured) | C (dies with the app), D (same account) | reject |
| 5 desktop scheduled task | A, E in principle; D by attrition | B (its own dirty-tree rule stops it silently), C when closed; cannot retire itself | reject |
| 6 OS scheduler tick + `claude -p --resume` | A, D (retries across the lockout), E (payload), C-app; B with a tree kill first | C-reboot without autologon | recommend, with the guard in §5 |
| 7 outer driver loop owning every turn | A, B, C-app, D, E | its own death; same auth prerequisite | collapse into 6: the OS is the loop |
| 8 cross-session SendMessage alone | A | it has no trigger of its own | reject: a payload, not a mechanism |
| 9 cloud routine | nothing local | no documented reach into a local session | reject |
| 10 PushNotification from the run | nothing | dead in exactly the state it is for (needs a turn) | fallback, sent by a hook or the tick |
| 11 another fleet node takes over | D uniquely (different user), C | A, B, E without a human; uncommitted state lost | fallback |

Claims the skeptic refuted, kept so nobody re-derives them: "CronCreate jobs survive process
death" — a registration re-listed in a human-resumed session is not a tick that fired; "the
transcript mtime is a liveness signal" — during a healthy 26-minute bar neither the transcript nor
the last commit moves, so a threshold under `GATE_BOUND` resumes into a healthy bar; "a schtasks
task runs whether or not the user is logged on" — measured false for the unelevated form.

## 5. The guards the two recommended mechanisms owe

- **Session binding.** Both act only on the run whose recorded `session:` is the caller's (hook) or
  whose recorded `pid:` and liveness are stale (tick). Without the recorded id, the hook would refuse
  every session in the repo its stop, and the tick has nothing to resume.
- **Terminal by predicate, in one place**, never `phase:` read by each consumer.
- **Liveness from what moves during a healthy silence**: the newest per-leg log under
  `<git-dir>/gate-logs/` during a bar, the transcript between bars; threshold above `GATE_BOUND`.
- **Tree kill before resume.** `TaskStop` and `timeout` leave trees (aReapedSpinner), so a resumer
  entering a class-B box must kill the recorded pid's tree or the resumed turn re-stalls on the
  same contention.
- **A bounded block count** for the hook, per session, honouring `stop_hook_active`.
- **The CONTINUE payload forbids re-parking** and states the absent-owner default: four of six
  stalls are E, and aGroundedOrientation re-parked after being told to proceed.
- **Attempts capped** for the tick, recorded per run, with the cap itself the fallback's trigger.

## 6. Unresolved, and what decides each

- Whether a pending Agent, Workflow or background Bash blocks the cron tick: owner-reported,
  unmeasured. Decided by one idle turn with a background sleep and a two-minute one-shot job.
- Two concurrent `claude -p --resume` writers on one transcript: unmeasured (auth blocked the
  probe on 09-13; the CLI is logged in as of 09-16). Decided by the probe in unit 5's spec.
- Whether `Stop` fires in a Workflow sub-agent (`SubagentStop` is documented as the sub-agent
  event): decided by unit 3's probe before its hook is wired.
- Which fields `StopFailure`'s stdin carries beyond `session_id`: unit 4's hook records the whole
  compact JSON line so it assumes none.
- Whether `stop_session` unsticks a hung tool call: not needed; the watchdog session is rejected.
