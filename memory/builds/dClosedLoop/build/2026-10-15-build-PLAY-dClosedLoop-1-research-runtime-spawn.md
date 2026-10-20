# Research: the runtime layer, the spawn harness

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 31's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-12-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`.

---

## Spawn harness research: PLAY-dClosedLoop-1-12

I measured on one node only (host `Compeeto`), using the 60-day transcripts under `~/.claude/projects/C--projects-coding-governance*`. That is 64 main sessions, 2,708 agent transcripts and 341 Workflow run records (journals). All 64 sessions ran in the desktop app; none was a `claude -p` session. Whatever happened on other nodes is not in these numbers.

### 1. Inventory

**[paths] How an agent is spawned today**

| Path | What admits it | What it is handed | How the return comes back |
|---|---|---|---|
| **Direct `Agent` call** from a session | `agent-cap.js` rule 6: the role must be marked `agent`-true, the prompt must be exactly the `gov:handoff` marker plus the `## Task` section, and the description must match (`tools/hooks/agent-cap.js:40-58`, `:2136`). The slot ledger then allows 5 per (session, prompt) with a 45-minute expiry per slot (`:107`, `:1580`, `:1683-1755`). | The role file `.claude/agents/<role>.md`, the prompt file from `handoff.py render` (`tools/roles/handoff.py:1-28`), and the route context injected by the SubagentStart `scratch-guard` hook (`.claude/settings.json`). | Free text, held in the parent's context. A background agent reports through a task notification. The transcript stays on disk as `subagents/agent-*.jsonl`, deleted after 30 days. |
| **Workflow `agent()`** | The Workflow tool call only. Rules 1-3 scan the script and require fan-out to go through the bounded helpers (at most 5). Rule 6 requires `scriptPath` to be in `.claude/roles.json` `harnesses`. Rule 0 handles spec-audits. The `agent()` calls themselves are invisible to every hook (`agent-cap.js:20-27`, `:1495-1497`). | A prompt the script builds from `args`, plus `agentType` (the role) and `effort` (`tools/workflows/unattended-unit.js:333-336`). | Schema-forced (`UNIT_SCHEMA`). It is held in the journal `workflows/wf_*.json` on that machine, and `resumeFromRunId` replays it (`unattended-build.js:564-581`). `tier2-review` also writes each result to a file before returning, but only when no role type is set (`tier2-review.js:274`, `:1149`). |
| **Nested spawn** | `workflow()` called from inside a script (`unattended-build.js:1329-1335`, `:1585`). It is not a tool call, so no hook sees it. | Same as a Workflow `agent()` call. | It returns as a value inside the parent script. |
| **Headless `claude -p`** | Only `resume-tick.sh`, and only when: the lease is STALE, fewer than 6 attempts have been made (`RESUME_ATTEMPTS`), and the CLI is logged in (`tools/unattended/resume-tick.sh:20-44`, `:121`). | A free-text continue instruction (`:367`), launched as `claude -p --resume <sid> --dangerously-skip-permissions --max-turns N` (`:385`), detached through `Start-Process` or `setsid` (`:191-213`). | Text written to a `.out` file. It uses neither `--output-format json` nor `--json-schema`. |
| **Scheduled run** | Session-scoped `CronCreate` and `ScheduleWakeup` for the keepalive and idle-wake, plus the OS-scheduled `resume-tick` that the owner registers (`resume-tick.sh:3-6`). | The cron prompt, which goes into the same session. | Nothing comes back. Each fire starts a new prompt. |

**Where the records disagree with the code or the docs**

1. A handed fact says the spawn guard compares `role-sha`. The code compares `task-sha` only, and its own header says it "never compares `role-sha`" (`agent-cap.js:58`, `:2136`).
2. `agent-cap.js:1570-1575` says the public docs claim the `Agent` tool skips PostToolUse. The current hooks docs say a foreground `Agent` call fires PostToolUse with `tool_response.status`, and a background launch returns at once as `async_launched`.
3. `agent-cap.js:1496-1497` says a sidechain holds no `Agent` tool (measured 2026-08-15). The current docs say a subagent can spawn subagents up to 3 layers deep. I measured 0 `Agent` calls made from inside a sidechain in 60 days.

### 2. Sequence

1. The owner's turn, or the executor, renders a work order with `handoff.py render`.
2. A direct path then goes through the `Agent` call, PreToolUse `agent-cap` (rule 6, then the slot), SubagentStart (`scratch-guard` context), the role agent's run, and a free-text return. **Nothing validates that return:** no SubagentStop, PostToolUse[Agent] or PreCompact hook is wired.
3. A Workflow path goes through the Workflow call, the PreToolUse script scan, then `agent()` calls the hooks cannot see. Each call returns schema-checked JSON (or `null`), which is written to the journal.
4. An unattended build loops: `unattended-build` hands out a roster, the caller makes one `unattended-unit` call per unit (1 agent each), and the builder's commit is the durable artefact (`unattended-unit.js:302-348`).
5. When a lease goes stale, `resume-tick` kills the tree and runs `claude -p --resume`.

### 3. Measurements

**Workflow journals**

```
$ python wf.py ; python wf2.py        # read-only scans of workflows/*.json, mtime < 60 d
journals 341 · status {'completed': 331, 'failed': 9, 'killed': 1}
agent states {'done': 2148, 'error': 67, 'progress': 1}
errors {'session/weekly limit': 57, 'overloaded/5xx/conn': 9, 'schema retry cap': 1}
ALL-ERR completed wf_2c820bf1-2fb unattended-unit result= {"committed": false, "sha": "", "why": "", "summary": ""}
  (and wf_9137922e, wf_adc633cb, wf_d8841dbd identical)
```

**Main transcripts**

```
$ python tx.py                         # 64 main + 2,708 sidechain transcripts
('Agent','main','bg') 69 · ('Agent','main','fg') 99 · ('Workflow','main',*) 463
('CronCreate') 45 · ('ScheduleWakeup') 7 · ('SendMessage') 4 · sidechain Agent calls: 0
('Agent','agent-cap other deny') 4 · ('Workflow','agent-cap other deny') 28 · direct-budget refusals 0
notifications: failed agent 2 ("529 Overloaded" a6d954d0; "4 background agents didn't finish
  before the previous session ended" 1799cb98), stopped 1
compactions: main 27 (13 files) · sidechain 0
```

**Slot ledger, resumes and launches**

```
$ for d in .git/agent-cap/*/; do ls $d | wc -l; done | sort -rn | head -1   ->  5   (1799cb98__a22d026d)
resumeFromRunId relaunches: 6 · attempt:2 (stall restart): 1 of 2,712 agent records
resume.*.log files: 0 · entrypoint sdk-cli sessions: 0 · all 64 sessions: claude-desktop
```

**Prompt ids in one long driver session (b710e9c3)**

```
{'human': 12, 'task-notification': 82, 'no-origin string': 91}
```

Every notification starts a new prompt id, and each new prompt id resets the 5-slot direct-spawn budget.

**[failures] Summary**

| Failure | Count in 60 days | Example |
|---|---|---|
| Refused by the 5-slot direct-spawn budget | **0** (one turn reached 5/5) | `.git/agent-cap/1799cb98__a22d026d` |
| Refused by another agent-cap rule | 4 `Agent` (rule 6: wrong handoff marker or task text), 28 `Workflow` (script-scan rules) | dTracedLedger: "prompt line 80 differs" |
| Died with the parent process | 4 background researchers, 1 killed Workflow, 1 agent left in `progress` | session 1799cb98; `wf_c0495e91` ("authored 6/6 specs", then killed) |
| Killed by a session or weekly limit | 57 agents in 16 runs. The whole fan died in 10 runs (4 of them with 4-9 agents). Part of the fan died in 6 runs, up to 10 of 20. | `wf_13b651eb` 9/9; `wf_7118930b` 10/20 |
| Empty result that reads as clean | 7 of 12 runs where every agent errored still show `completed`, and 4 of them are `unattended-unit` returning `committed:false, why:""` | `unattended-unit.js:339-348` turns a `null` into `false` |
| Lost return | All 67 errored agents. Judges run under a role type write no file, so `durable:false` (`tier2-review.js:274`). | `gov-researcher` has no Write tool (`.claude/agents/gov-researcher.md:4`) |
| Compaction inside an agent | **0** of 2,708 | — |
| Retries | 1 stall restart, 1 schema retry cap exceeded (5 tries), 6 `resumeFromRunId` relaunches, 0 `resume-tick` launches | `wf_94a50dde` |

The limit-killed runs date from 2026-08-25 to 2026-09-22, on CLI 2.1.237 to 2.1.281. None has occurred since. `autoContinueAtUsageLimit` is not set in any settings file I read.

**[platform] What the documentation offers**

| Feature | What the docs say |
|---|---|
| **Workflow** | Replay works within the same session, or after `claude --resume`. A failed agent re-runs along with every agent started after it. A fresh session has "nothing to resume". Runs stop with the session unless it is backgrounded. Usage-limit pausing needs ≥2.1.271, an interactive session, `autoContinueAtUsageLimit`, a reset within 24 h and at most 2 waits, and it never applies under `-p` or in background sessions. `agent()` resolves to `null` on an unrecoverable error. Schemas get 5 retries (`MAX_STRUCTURED_OUTPUT_RETRIES`). Limits: 16 concurrent agents and 1,000 agents per run. Scripts have no filesystem access. ([workflows](https://code.claude.com/docs/en/workflows)) |
| **Worktree isolation** | Branches "from your default branch rather than the parent session's `HEAD`". This confirms the lead for subagents; it is not stated for workflow `agent()`. ([sub-agents](https://code.claude.com/docs/en/sub-agents)) |
| **Background agents and SendMessage** | Results arrive as a completion notification. SendMessage resumes an agent "with full conversation history", including after the session is resumed. 20 concurrent subagents per session. No limit on the total. ([sub-agents](https://code.claude.com/docs/en/sub-agents)) |
| **SubagentStart / SubagentStop** | SubagentStart gives `agent_id`, `agent_type` and `additionalContext`, and cannot block. SubagentStop gives `agent_transcript_path` and `last_assistant_message`; exit 2 or `block` keeps the agent running. PostToolUse[Agent] fires for foreground calls. ([hooks](https://code.claude.com/docs/en/hooks)) |
| **Pre-compaction** | PreCompact has `manual` and `auto` matchers, and exit 2 blocks compaction. PostCompact gives `compact_summary` but cannot affect the result. ([hooks](https://code.claude.com/docs/en/hooks)) |
| **Cron** | Session-scoped. Fires only while the session runs and is idle. Recurring tasks expire after 7 days. Up to 50 tasks. Durable alternatives are Desktop scheduled tasks and Routines. ([scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)) |
| **`claude -p`** | Has `--output-format json`, `--json-schema` (returns `structured_output`), `--resume <id or path>`, `--session-id`, `--max-turns` and `--max-budget-usd`. `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` controls how long it waits for background work. ([headless](https://code.claude.com/docs/en/headless), [cli-reference](https://code.claude.com/docs/en/cli-reference)) |
| **Background sessions** | `claude --bg --agent <role>` runs under a supervisor that restarts a crashed session. Sessions stop on reboot. Results are read by polling `claude agents --json`. `--bg` cannot be combined with `-p`. ([agent-view](https://code.claude.com/docs/en/agent-view)) |
| **Agent SDK** | `resume` and `fork` work by session id. Sessions are local to the machine unless a `SessionStore` is used. ([agent-sdk/sessions](https://code.claude.com/docs/en/agent-sdk/sessions)) |

**[budget] The fan-out bound**

| Spawner | What bounds it | What it means for N units with r role-items each |
|---|---|---|
| Direct `Agent` | 5 per prompt id. It counts total spawns, not concurrency (`agent-cap.js:1533-1540`). Prompt ids reset on every notification or cron fire. | N·r spawns need at least ⌈N·r/5⌉ wakes. Concurrency is bounded only by the platform's 20. One owner turn stalls after 5. |
| Workflow | At most 5 concurrent per script (static scan). Workflow calls are deliberately left out of the ledger (`:1523-1531`). | One call per item gives N·r calls and no refusal. k concurrent background Workflow calls give 5k concurrent agents. Nothing bounds the total except 1,000 agents per run. |
| `claude -p` / `--bg` | No hook sees the launch. | Only the executor can bound it. |

### 4. Gaps

- Nothing turns an `agent()` `null` into a deferral at the unit level. Only `tier2-review` and `unattended-build` do (`unattended-build.js:1652-1700`).
- Returns made under a role are not durable, and no SubagentStop hook persists or validates them.
- No bound covers Workflow calls across a session, or processes launched outside a session.
- Usage-limit pausing appears unconfigured, and cannot apply under the `-p` resumer.
- The `claude -p` launcher has never run on this node, so it is unproven at volume.
- Release on PostToolUse[Agent] is now documented, but the ledger still relies on the 45-minute expiry.
- I did not verify whether SubagentStop fires for Workflow sidechain agents.

### 5. Candidates

The four losing tests are the same for every candidate:

- **T1:** kill the parent process tree in the middle of an item.
- **T2:** a session limit hits in the middle of a fan.
- **T3:** two concurrent dispatches of 5 agents each.
- **T4:** the return survives both T1 and T2, with its schema checked.

| Candidate | How it works | T1: process death | T2: session limit | T3: bounded fan-out | T4: durable return |
|---|---|---|---|---|---|
| **A. Workflow runtime as the spawner.** Extends `unattended-build`/`unattended-unit` and the `tier2` durability seam. | A script spawns agents with `agent()`, `schema` and a role type, and `resumeFromRunId` replays the journal. | **Loses on its own.** The run stops with the session (`wf_c0495e91`). It can only be recovered from a resumed session. | **Loses as measured** (10 whole fans; the 4 unit runs read clean). The platform pause does not apply under `-p`. | **Passes** within one script (≤5). **Loses** across concurrent calls, which the ledger leaves out. | **Partial.** The schema and the on-machine journal pass. **Loses** under roles (`durable:false`). |
| **B. Headless sessions the executor launches.** Extends the `resume-tick` launcher. | A detached `claude -p --resume/--session-id --output-format json --json-schema`, supervised by the executor through the lease. | **Passes by design**: detached, a session file on disk, and resume by id. Detaching was measured on node a (`resume-tick.sh:191-196`). | **Passes, on condition.** `-p` fails the agent outright, but the executor has a clock and can hold, then relaunch. | **Passes** if the executor holds a counter tied to the lease; no hook sees the launch. | **Passes**: `structured_output` lands in a file the executor owns. |
| **C. Direct subagents from a long-lived driver session.** Extends rule 6 and `handoff.py`. | Background `Agent` calls, task notifications and `SendMessage`. | **Loses (measured):** 4 researchers lost in 1799cb98. | **Loses (measured):** 529 on a6d954d0, and no pause is documented. | **Loses.** The 5-slot budget resets on every notification, so it bounds a burst, not concurrency. | **Loses.** Returns are free text with no schema, and nothing writes them to disk. |
| **D. Platform-supervised background sessions.** No existing seam; 0 uses in the repo. | `claude --bg --agent <role>`, polled through `claude agents --json`. | **Passes** a crash (the supervisor restarts it). **Loses** on reboot. The Windows reconnect behaviour is undocumented. | Untested; the docs are silent. | Must be bounded by the executor. | **Loses.** `--bg` cannot take `-p` or `--json-schema`, so there is no schema-forced channel. |

I folded the Agent SDK host into B. It drives the same session process with the same `resume` semantics, and differs only by adding a package dependency outside the bash plus python3 toolchain. I found no fifth mechanism: Cron and SendMessage re-enter an existing session rather than spawn.

**Rejected:**
- **C** loses T1, T2 and T4 on measured evidence.
- **D** loses T4 under the docs (no schema-forced channel). It also loses T1 on reboot, and nothing in this repo has ever exercised it.
- **A on its own** loses T1 and T2 as measured, and T3 across concurrent calls.

### 6. Pick

**I recommend B as the supervisor, driving A as the spawner inside it.** This is RL-8's "already exists" read literally: both seams are already in the tree.

- **The outer layer is B.** The executor is a process outside any session. It launches each build's driver session as `claude -p`, holds its lease, and relaunches it after a process death or limit reset. This generalises `resume-tick.sh:385`, adding `--output-format json --json-schema` and a counter tied to the lease. This is what passes T1, T2 and T3.
- **The inner layer is A.** Item agents spawn through the role-typed `unattended-unit` harness (86 completed runs) and are replayed with `resumeFromRunId`.
- **Returns are persisted by a SubagentStop hook,** not by agent Write. The hook writes `last_assistant_message` keyed by `agent_id` and checks it against the item's schema; exit 2 holds the agent. That keeps role agents write-less, and keeps the guard's state apart from what it guards.
- **One shared deferral factory.** The unit harness must return `deferred-platform` on a `null`, rather than `committed:false`. Per the reuse rule, extract that as one factory shared with `tier2-review`, not a third copy.

**Tests the build must run (each could still make the pick lose):**
1. Kill the driver's process tree in the middle of a unit. The executor relaunches it, and the replay re-spends no tokens on agents that already completed (compare the journal's `totalTokens`).
2. Put a stub `claude` that prints "hit your session limit" ahead of the real one on `PATH`, the way the `resume-tick` suite already does (`:376-380`). The unit must come back `deferred-platform`, and the executor must hold rather than move on.
3. Issue two concurrent dispatches of 5 agents each under one lease. The second must queue; today it is admitted.
4. Does SubagentStop fire for a Workflow sidechain agent running under a role type? If it does not, the pick falls back to the journal plus `--json-schema` at the session level, and returns from role agents stay non-durable within a run.
5. The cost of starting one `-p` session per build, on Windows: never measured on this node.

My scratch scripts (`wf.py`, `wf2.py`, `wf3.py`, `tx.py`) are in `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\`. Nothing in the repository was written.

Sources:
- [Workflows](https://code.claude.com/docs/en/workflows)
- [Sub-agents](https://code.claude.com/docs/en/sub-agents)
- [Hooks](https://code.claude.com/docs/en/hooks)
- [Headless](https://code.claude.com/docs/en/headless)
- [CLI reference](https://code.claude.com/docs/en/cli-reference)
- [Scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks)
- [Agent view](https://code.claude.com/docs/en/agent-view)
- [Agent SDK sessions](https://code.claude.com/docs/en/agent-sdk/sessions)
