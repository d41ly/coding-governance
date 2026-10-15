# Research: the runtime layer, sessions, context, scheduling, harnesses and nodes

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 33's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-14-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`.

---

# Research: sessions, context, scheduling, harnesses and nodes (PLAY-dClosedLoop-1)

Every probe here was read-only. Transcripts were read only from the 39 `C--projects-coding-governance*` directories under `~/.claude/projects`; the scan scripts are in my scratchpad (`scan.py` to `scan4.py`).

## Inventory

| Concern | As wired | Cite |
|---|---|---|
| startup / clear | `manifest-check.sh --card --write` writes `<git-common-dir>/orientation/<sid>.md`, capped at 8 KiB | `.claude/settings.json:34-41`; `manifest-check.sh:216,311-317` |
| resume / compact | `--card --replay`: prints the stored card plus one `now —` line, or writes a fresh one if none is stored | `settings.json:43-50`; `manifest-check.sh:721-725` |
| startup / resume / clear | `check-wiring.sh --session` and `procmon-hook.js` | `settings.json:52-63` |
| `fork` source | **no matcher covers it**, although the documentation lists `fork` as a SessionStart source | `settings.json:34,43,52`; [hooks](https://code.claude.com/docs/en/hooks) |
| PreCompact / PostCompact / SessionEnd | **not wired** (0 PreCompact entries across all transcripts) | `settings.json` |
| SubagentStart | `scratch-guard.js` only. It injects route facts, not the card. | `settings.json:111` |
| Keepalive | `CronCreate`/`CronDelete` every 10 minutes, plus `--beat` claim renewal | `.unattended.conf:123-130`; `unattended.sh:33` |
| Durable restart | `create_scheduled_task` (the desktop app's store, on disk), 1800 s delay, limit 6 | `.unattended.conf:141-153` |
| Remote CI schedule | `cron '23 4 * * *'` runs `held-plan`/`held` (the self-tests) only; `contents: read`; Windows runner | `.github/workflows/remote-ci.yml:30-41,125` |
| Node registry | a, b, c, d. Only node a declares a variance. | `tools/playbook/fleet.toml:21-46` |
| Harness kit | `AGENTS.md` canonical; `CLAUDE.md` = `@AGENTS.md`; Gemini, Copilot, Cursor and Windsurf get pointers or copies; Codex gets only a 32 KiB size warning | `tools/agent-instructions/README.md`; `adopt-agent-instructions.sh:31,66` |

## Sequence

**Session lifecycle as it runs today:**
1. **Startup** writes the card. The `claims —` cell is the only remote read (`manifest-check.sh:647`).
2. **Compact** replays the card into the compacted context. The documentation confirms that SessionStart `compact` output is added after compaction ([context-window](https://code.claude.com/docs/en/context-window)).
3. **Resume** should replay the card but often does not. This session's own transcript (`1799cb98`) has four `SessionStart:resume` events (2026-10-14 16:21 and 20:03, 2026-10-15 11:55 and 13:05). Each one recorded the procmon and check-wiring output but **no card**, while all three of its compact events carried one. The stored card exists (`.git/orientation/1799cb98…md`, 7312 B, written by `--card --write`), so storage worked and delivery failed. **I have not verified why.**
4. **Process death.** Session `b73dcb0a` died at 11:23:52–53Z. All 5 of its subagent transcripts stop mid-turn within that second (last entries are `tool_use`, `thinking` or an attachment), which confirms the "researchers died with their parent" lead. Its successor `1799cb98` carries the old history but a new session id, and got a new `--write` card at 14:30.

**What survives a process death:**

| State | Survives? | Basis |
|---|---|---|
| Transcript jsonl (main and subagents) | yes; subagents can be resumed by resuming the session | [sub-agents](https://code.claude.com/docs/en/sub-agents) |
| Subagents still running | **no** | `b73dcb0a` measurement above |
| Card file | yes, but it is keyed by session id, so a successor with a new id needs a new card | `manifest-check.sh:316` |
| CronCreate keepalive | restored only on `--resume`; recurring tasks expire after 7 days | [scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks) |
| Desktop scheduled task | yes (stored on disk; a missed fire runs at the next launch) | `.unattended.conf:133-137`; `~/.claude/scheduled-tasks/*/SKILL.md` (12 tasks) |
| Remote claim refs | yes, including stale ones (see Measurements) | `refs/gov/runs/*` |
| Uncommitted worktree edits / primary-tree index | yes, and the primary-tree index is shared by every session there | git |

## Measurements

**Session costs.** Input per assistant turn = `input_tokens` + `cache_creation_input_tokens` + `cache_read_input_tokens`, taken on the first assistant turn after each kind of start, across 64 main sessions.

| Event | n | Median | Range | Split |
|---|---|---|---|---|
| First turn after startup | 62 | **83,871** | 53,769–130,409 | about 42k created, 38k read |
| First turn after resume | 39 | **502,522** | 103,949–903,452 | mostly cache creation (for example 390k created / 34k read) |
| First turn after compaction | 27 | **100,955** | 0–131,025 | |
| First turn of a subagent | 147 | **12,822** | p90 79,725 | |

A resume costs about 6× a fresh start. The earlier figure was 467k against 146k fresh. My fresh median is lower; I counted only the first turn after `SessionStart:startup`. **This disagrees with the earlier record and the metric difference is the likely cause.**

**Compaction frequency.**

| Measure | Value |
|---|---|
| Compactions in main sessions | 27 (21 auto, 6 manual) |
| Sessions that ever compacted | 13 of 64 |
| Sessions under 1,000 turns that compacted | **0 of 48** |
| Sessions of 1,000–3,000 turns | 9 of 12 compacted (14 compactions) |
| Sessions over 3,000 turns | 4 of 4 compacted (13 compactions) |
| Turns between consecutive compactions | median **1,064** (286–1,550) |
| Tokens before compaction | median **969,959** (a 1M window) |
| Tokens after compaction | median 20,317 |
| Duration | median **116.9 s** (65–201 s) |
| Subagent compactions | **0** in 147 transcripts (longest is 409 turns) |

**Card delivery per SessionStart event** (grouped by transcript and tool-use id):

| Source | Before 2026-09-15 | Since 2026-09-15 |
|---|---|---|
| startup | 45, no card (card writer not yet wired) | 19, all with card |
| compact | 16, no card | 10, all with card |
| resume | 24, no card | **7 of 14 with card** |

The seven misses since 09-15 are in sessions `2588f719` (2), `b710e9c3` (1) and `1799cb98` (4), on CLI 2.1.271, 2.1.281 and 2.1.295.

**Remote claims.** `git ls-remote origin 'refs/gov/*'` shows 17 refs, all under `refs/gov/runs`. Read from the local cache, every sha is present:

```
aFrugalTurnstile | node: daily-agent status: live beat-utc: 2026-10-11T01:28:28Z | age 4d
aGraftedHelix    | node: daily-agent status: held beat-utc: 2026-10-07T02:02:17Z | age 8d
… 9 held, 7 landed, 1 live; beat ages 2–8 days
```

This confirms the lead that beats are days old. **It also disagrees with the settled design:** the `node:` field holds the OS user (`daily-agent`, `d41ly`), not the fleet tag (`a`, `d`) that `fleet.toml:21-24` maps it to. And landed claims are never removed.

**Node d:**

| Concern | Probe and output |
|---|---|
| Process creation | 200 runs of `/usr/bin/true` took `real 0m2.467s`, so **12.3 ms per exec** (the lead said about 22 ms, so it varies with load). In this session a plain grep also failed with `child_copy: cygheap read copy failed … Win32 error 299` and `fork: retry: Resource temporarily unavailable`. |
| Clock skew | `curl -sI` Date headers from google, github and cloudflare read 17:06:37, 17:06:33 and 17:06:38, against local `date -u` 17:06:25. **Node d runs about 8–13 s slow**, and no registry field records it. |
| Line endings | `core.autocrlf=true` in `~/.gitconfig` on node d, while CI forces `false` (`remote-ci.yml:53-56`). `.gitattributes` has `* text=auto` and 73 `eol=lf` lines. `fleet.toml` records no per-node autocrlf. |
| Lock file | `.claude/scheduled_tasks.lock` is absent in the primary tree, so the lead was not reproduced. |

## Gaps

**Compaction checks the task asked for:**

| Check | Answer |
|---|---|
| Are compaction instructions in the instruction file honoured? | The documentation says yes, via a `# Compact instructions` section in CLAUDE.md ([costs](https://code.claude.com/docs/en/costs)). gov has none: `grep -i compact CLAUDE.md AGENTS.md` matches nothing. Whether a section reached through the `@AGENTS.md` import counts is **unverified**. |
| Is there a pre-compaction hook? | Yes. `PreCompact` (matchers `manual`/`auto`) can block. It receives `trigger`, `custom_instructions` and `transcript_path`, and its `systemMessage` is discarded, so it cannot inject. A command hook can still flush work (commit, checkpoint) before the summary in a main session. The documentation does not say whether it fires inside a subagent: **unverified**. `PostCompact` receives `compact_summary` ([hooks](https://code.claude.com/docs/en/hooks)). |
| Does a subagent's compaction re-inject its brief? | Only the SubagentStart `additionalContext` is documented as re-injected after a subagent auto-compacts ([hooks](https://code.claude.com/docs/en/hooks)). The Agent prompt (the brief) is not documented either way. No transcript can show it: 0 subagent compactions. |
| Re-attachment rule | Up to **5** files read or edited, most recently modified first. A file over **5,000 tokens** comes back as a path only. Invoked skills are capped at **5,000 tokens each and 25,000 in total**, oldest dropped first. Root CLAUDE.md is re-injected; path-scoped rules are not ([context-window](https://code.claude.com/docs/en/context-window)). |
| Compaction against a fresh session | A compaction reads about 970k tokens (cheap only while the cache is warm), takes 117 s, then starts the next turn at 101k. A fresh start costs 84k and 0 s. |

**Other gaps:**
- Seven of 14 resumes since 09-15 delivered no card. The cause is unverified.
- No matcher covers `fork`.
- Claims are named by OS user, not fleet tag, and stale or landed claims persist.
- Clock skew and autocrlf are not recorded per node.
- The keepalive comment says the CronCreate store "dies with the session" (`.unattended.conf:118-120`). The documentation now says tasks are restored on `--resume`, with a 7-day expiry, so the record is partly stale.
- **The handed Codex fact is stale against both the repo and the vendor documentation.** No `AGENTS.override.md` and no Codex hook wiring exist anywhere in `tools/` or `WIRE-INTO-PROJECT.md` (grep is empty). Codex hooks are now on by default; `codex_hooks` survives only as a "deprecated alias". Codex now has `PreToolUse` (covering Bash, `apply_patch` and MCP tools), `SubagentStart`, `SubagentStop`, `PreCompact` and `SessionEnd` ([Codex hooks](https://learn.chatgpt.com/docs/hooks)).

**Harnesses: what each lacks today:**

| Harness | Lacks at runtime |
|---|---|
| Claude Code | No PreCompact flush is wired; the card misses on `fork` and on resume; nothing reaps subagents that die with their parent |
| Codex | Every gov hook (the platform has the events, gov wires none). No Workflow tool or desktop scheduled tasks, as far as I know (unverified). Its own documentation calls its hooks "a useful guardrail, not a complete enforcement boundary". |
| Gemini, Copilot, Cursor, Windsurf and others | Instruction file only. No spawn guard, write gate, schema-forced return or card. |

**Scheduling: what Maintain and a weekly Loop Review need from a scheduler:**
- It must survive the session and the machine being off, and catch up on a missed fire.
- It must have the gov toolchain (bash and python on Windows; greens are only earned there, `remote-ci.yml:19-21`).
- It must be able to write what it finds as witnessed state.
- A lease must stop two nodes firing the same run.
- The Loop Review needs an agent. Maintain's deterministic checks (drift-audit is stdlib and git, with no agents) do not.

## Candidates

**Session strategy**

| # | Mechanism | Test that would make it lose | Result |
|---|---|---|---|
| S1 | One long-lived driver session per build that compacts and resumes | Does it compact, resume or die within one build, and does each cost more than a restart? | **Loses.** A compaction is ~970k read plus 117 s and a resume is 502k, against an 84k fresh start. Resume dropped the card 7 of 14 times. A process death killed 5 in-flight subagents. |
| S2 | A fresh driver session per item; role agents are spawned per step; `next` derives position from witnessed state | A driver for one item reaching the measured compaction distance (p90 driver turns per item over about 1,000), or `next` failing to place a cold session | **Partly run.** 0 of 48 sessions under 1,000 turns compacted. The cold-`next` half is a build test I did not run. |
| S3 | A fresh session per step | Does a session per step cost more than a subagent per step with no extra isolation? | **Loses.** 84k per session start against 12.8k per subagent start. The always-spawn harness already gives each step a fresh context. |

**Where the scheduler lives**

| # | Mechanism | Test that would make it lose | Result |
|---|---|---|---|
| W1 | Remote CI `schedule` (the existing seam, `remote-ci.yml:33-34`) | Does the job need an agent or a write? | **Loses for Loop Review** (`contents: read`, no agent, `remote-ci.yml:16-17,38`). **Passes for deterministic Maintain checks.** |
| W2 | Desktop scheduled task on a declared node, firing `next` under a lease | Does it double-fire across two nodes, or miss a fire while the node is off? | The lease handles double fire. Catch-up at next launch is a recorded contract (`.unattended.conf:133-137`) that I did not test here; it is a build test. |
| W3 | Cloud routine | Can the bar run green in a routine's fresh, non-Windows clone? | Not run, since running it would launch a run. Remote CI pins Windows because no non-Windows green exists. Minimum interval is 1 hour. |
| W4 | In-session CronCreate (today's keepalive) | Does it outlive the session for a weekly cadence? | **Loses.** Session-scoped, 7-day expiry, and it fires only while the session is idle and open ([scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)). |

**How harnesses are adapted**

| # | Mechanism | Test that would make it lose | Result |
|---|---|---|---|
| H1 | One guard core (node scripts reading hook JSON on stdin) plus a thin per-harness wiring fragment: Claude `settings.json`, Codex `hooks.json` | Feed a Codex `apply_patch` PreToolUse payload to a scratch-guard fixture; it loses if the write path cannot be extracted | **Owed, not run.** Event names match one to one (above). |
| H2 | Enforcement at the git boundary only (pre-commit, pre-push, remote CI) for any harness | Any allowance breach that never reaches a commit, such as a Bash write outside the allowance or an over-budget spawn | **Loses as the only mechanism**: the spawn and write guards are tool-boundary by definition. It stays as the floor. |
| H3 | Claude Code only; other harnesses get instructions only | Any node running Codex as the driver | Not measured. Nothing in the repo records a Codex driver run, so the test decides it only if the owner requires one. |

## Pick

- **Session strategy: S2.** A fresh driver per item, with a role agent per step. On compaction it keeps the replayed card and adds a `PreCompact` command hook that flushes the item's partial work, as a safety net, not the plan. S1 loses on cost and reliability, and S3 on cost (measured above). The cold-`next` test is owed by the build.
- **Scheduler: W1 plus W2, split by kind, and both only fire `next`.**
  - W1, the remote CI cron, takes the deterministic Maintain checks.
  - W2, a desktop scheduled task on a node named in `fleet.toml` and guarded by a lease ref, takes the weekly Loop Review.
  - W3 is rejected until a routine shows a green bar. W4 is rejected by its documented 7-day, session-scoped lifetime.
- **Harness adaptation: H1 for Claude Code and Codex, with H2 kept as the floor for every harness.** H1's losing test is the `apply_patch` fixture, still owed.
- **Corrections owed to the handed facts:**
  - Codex hooks are now default-on, and gov wires no Codex override or hook today.
  - The claim holder field carries the OS user, not the fleet tag.
  - The resume card is dropped about half the time, cause unverified.
  - `fork` is unmatched.
  - Node d's clock is about 10 s slow.

Sources:
- [Claude Code hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code sub-agents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code costs](https://code.claude.com/docs/en/costs)
- [Claude Code prompt caching](https://code.claude.com/docs/en/prompt-caching)
- [Claude Code context window](https://code.claude.com/docs/en/context-window)
- [Claude Code scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks)
- [Codex hooks](https://learn.chatgpt.com/docs/hooks)
- [Codex CLI hooks deep dive](https://codex.danielvaughan.com/2026/03/26/codex-cli-hooks-deep-dive)
- Third-party guides that came back from a search; the official pages above superseded them: [morphllm compact](https://morphllm.com/claude-code-compact), [vincentqiao compact](https://blog.vincentqiao.com/en/posts/claude-code-compact/)
