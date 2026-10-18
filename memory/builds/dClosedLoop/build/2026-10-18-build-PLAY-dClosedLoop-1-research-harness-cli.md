# Research: the harness, its CLI, and session ids

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 108's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-11-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md`.

---

1. **Verdict**

Yes, gov benefits from using more of the CLI, and the runtime design already rests on it: act sessions are `claude -p` processes. I ran one headless session: it returned a session id and structured JSON, and a resume by that id remembered the earlier turn. The same check found four costs: a failure when the nested session refreshed its OAuth token, a resume that cost 51 times the fresh run, a nested process that recorded the wrong origin in its transcript, and different CLI versions in the app and on PATH. The way to stay independent of the owner's app is candidate C: harness adapters, each passing a conformance fixture, with the CLI as the first adapter and the apps as viewers. Codex can match Claude on session ids. It has no equivalent of Claude's messages between sessions that I could find. Two records are out of date: Codex now documents 12 hook events, and the app's Claude Code is 2.1.299.

2. **Today: what gov depends on, per harness surface**

Paths are relative to `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\`.

| Surface | What it depends on (measured with `git grep`, outside `memory/`) |
|---|---|
| Calls to `claude` | One launch line, `tools/unattended/resume-tick.sh:385` (`claude -p --resume %q --dangerously-skip-permissions --max-turns`), which has never run. One version probe, `skills/session-kickoff/manifest-check.sh:416-427`. Six files in all, counting tests and docs. |
| Hook wiring | `.claude/settings.json` has 13 entries over 7 events (PreToolUse ×3, SessionStart ×4, PostToolUse ×2, Stop ×2, StopFailure, SubagentStart). None sets `onFailure`. `permissions` is `{}`. |
| Hook payload fields | `session_id` is read in 6 scripts (for example `tools/unattended/stop-guard.js:183` and `tools/hooks/scratch-guard.js:774`, which keys the card by session). `transcript_path` at `tools/hooks/format-guard.js:494`. `last_assistant_message` at `format-guard.js:485`. `agent_type` and `agent_id` at `scratch-guard.js:1168` and `1423`. `stop_hook_active` in 2 scripts. `tool_input` in 4. |
| Environment variables | `CLAUDE_PROJECT_DIR`: 17 files, 101 lines. `CLAUDE_CODE_SESSION_ID`: 12 files, 126 lines (run claims at `unattended.sh:8901`). `CLAUDE_CONFIG_DIR`: 7 files. `CLAUDE_PID`: 4 files. |
| The transcript store, `~/.claude/projects/<cwd>/<id>.jsonl` | `tools/runlog/extract.py:186-198`, `tools/roles/handoff.py:537-562`, `tools/unattended/unattended.sh:8493`, `tools/drift-audit/drift_signals.py:474` (the auto-memory directory). |
| `.claude/` writers | 17 files outside the test suites. The main ones are `tools/roles/render_agents.py:65-66` (`.claude/agents`, `.claude/roles.json`, written with Claude-only keys at `:132`) and each kit's `adopt-*.sh`. |
| `Workflow` scripts | 10 under `tools/workflows/`: 6 live and 4 templates. Their runtime has no shell (`check-workflow-syntax.js:41` lists the only globals it injects). The gov transcripts hold 545 `Workflow` calls. |
| Desktop-only features | `RESUME_SCHEDULE_CREATE="create_scheduled_task"` in `.unattended.conf`, and `.claude/skills/unattended/SKILL.md:178`. That tool was called 0 times in the 66 gov transcripts I scanned. Desktop tool calls in those transcripts: browser pane 138; `ccd_session` 69 (`spawn_task` 20, `mark_chapter` 44); `visualize` 22; `ccd_session_mgmt` 3 (list and search sessions); `ccd_host` keep-awake 1. |
| Other harnesses | `tools/agent-instructions/` wires file names only. Codex's 32 KiB limit is at `adopt-agent-instructions.sh:31`. No Codex hook, agent or config is wired anywhere. |

3. **The CLI and Codex, tested**

Every command below ran from the scratch directory `…/scratchpad/away/d108/`, so no project hook fired in the repository.

| Command | Output |
|---|---|
| `claude --version` | `2.1.292 (Claude Code)` at `/c/Users/d41ly/.local/bin/claude` |
| Environment of this session | `CLAUDE_CODE_ENTRYPOINT=claude-desktop`. `CLAUDE_CODE_EXECPATH=…\Claude\claude-code\2.1.299\…\claude.exe`. `CLAUDE_AGENT_SDK_VERSION=0.3.299`. `CLAUDE_CODE_MESSAGING_SOCKET=\\.\pipe\LOCAL\cc-msg-…`. The desktop app runs the same engine through the SDK. |
| Owner's transcript `1799cb98….jsonl` | Versions `{'2.1.295': 6772, '2.1.299': 15984}`. **The handed fact says 2.1.295; the app has since updated to 2.1.299.** |
| `claude --help` (saved to `help.txt`) | Flags present: `-p`; `--output-format text\|json\|stream-json`; `--input-format stream-json`; `--json-schema`; `--session-id <uuid>`; `-r/--resume`; `--fork-session`; `--no-session-persistence`; `--agent`, `--agents`; `--permission-mode acceptEdits\|auto\|bypassPermissions\|manual\|dontAsk\|plan`; `--permission-prompts host\|none` ("none: anything that would prompt is denied automatically"); `--setting-sources`, `--settings`; `--mcp-config`, `--strict-mcp-config`; `--bare` (skips hooks); `--safe-mode`; `--restricted`; `--bg`; `--desktop`; `--remote-control`; `--cloud`; `-w/--worktree`; `--chrome`. Subcommands: `agents`, `attach`, `logs`, `stop`, `rm`, `respawn`, `auth`, `mcp`, `setup-token`. **`--max-turns` is not listed but is accepted**, which disagrees with `layer-runtime.md:166`. |
| `claude auth status` | `"authMethod": "claude.ai"`, `"subscriptionType": "max"`, `projectsDirectory C:\Users\d41ly\.claude\projects` |
| `claude agents --json` | 6 sessions with fields `cwd, id, kind, name, pid, sessionId, startedAt, state/status`. 5 are `interactive`: the desktop app's sessions, this one included, as `busy`. 1 is `background`. A script can read the app's session list. |
| Run 1: `claude -p "Reply with one word: pong" --output-format json --max-turns 1 --tools ""` | rc=1 after 8.4 s. `"is_error":true,"terminal_reason":"api_error","result":"Failed to refresh OAuth token: another Claude Code process is refreshing it or exited mid-refresh…"`. It still returned `session_id afe07e7a…` and wrote a transcript. |
| Run 2: the same command, retried minutes later as the message asked | rc=0 after 12.2 s. `result 'pong'`, `session_id 35392afb-55f6-4eee-a278-c231283e3644`, `num_turns 1`, `$0.0217`, `cache_creation 2,690` |
| Resume: `claude -p "What exact word did you reply with…" --resume 35392afb-… --output-format json --max-turns 1 --tools ""` | rc=0 after 5.7 s. `result 'pong'`, the same `session_id`. **`$1.108`, `cache_creation 135,786`**: 51 times the fresh run, cause unknown. This agrees with `layer-runtime.md:215` (median 503k tokens after a resume). |
| Transcript | `~/.claude/projects/C--Users-d41ly-…-scratchpad-away-d108/35392afb-….jsonl`, 30 lines with both turns. Every line says **`entrypoint claude-desktop`, version 2.1.292**: the nested process inherited the app's entrypoint variable, so that field cannot be trusted for attribution. |
| `codex --version` | `codex-cli 0.139.0`. The Codex desktop package `OpenAI.Codex_2p2nqsd0c76g0` is also installed. |
| `codex exec --help`, `codex exec resume --help`, `codex fork --help` | `exec` has `--json`, `--output-schema <FILE>`, `--ephemeral`, `-o`, `--sandbox`, `--ask-for-approval`. `exec resume [SESSION_ID] [PROMPT]` and `--last` exist. `fork` is interactive only (no `exec fork`). No flag sets a session id in advance. `app-server` and `remote-control` are marked experimental. |
| `codex features list` | 81 flags. `hooks stable true`, `multi_agent stable true`, `memories experimental false`. None concerns workflows or messaging between sessions. |
| `~/.codex/sessions/…/rollout-<ts>-<uuid>.jsonl` | 20 files. Each has a `session_meta.id` (UUIDv7) and records `originator` (all 20 are `Codex Desktop`). The app and the CLI share one store. |

**Documented, not tested.**
- Claude Code's messages between sessions: the model tools `ListAgents` and `SendMessage`, and a per-session inbox (a named pipe on Windows). A `-p` session binds one; `--bare` does not. Messages are plain text, capped near 1M characters, and at most 50 are queued. On Windows a connection must authenticate with `CLAUDE_CODE_MESSAGING_TOKEN`, and a script can post into its *own* session.
- Codex hooks now cover 12 events, SessionStart, PermissionRequest, UserPromptSubmit, Stop and PostCompact among them. The payload carries `session_id` and `transcript_path` ("not a stable interface"). Hooks are trusted by hash, so a new project hook is skipped until the owner trusts it. The docs say hooks are "not a complete enforcement boundary". **`layer-runtime.md:796-798` lists five events and says Codex has "no SessionStart, PostToolUse, Stop or PostCompact"; that is now stale.**

**What the apps add, and what does the same job from a script:**

| App feature | gov uses it | Equivalent a script can drive |
|---|---|---|
| Session list and search | runlog skill (`SKILL.md:100`); 3 calls | `claude agents --json` (tested); the transcript store (tested) |
| Spawning a task or session, with a worktree | 21 calls | `claude --bg`, `-w`, `claude agents` (help) |
| Scheduled tasks | the `RESUME_SCHEDULE_*` keys | the OS scheduler plus `claude -p`. Runtime already retires these keys (`layer-runtime.md:1032`). |
| Browser pane | 138 calls | `--chrome` (help); the design's `visual.capture` command adapter |
| Widgets, chapters, split views | 66 calls | none. These are for viewing only. |
| Opening a CLI session in the app | none | `claude --desktop --resume <id>` (help, not run) |

4. **Agnosticism: the candidates, their losing tests and results**

| Candidate | Mechanism | What it changes in Runtime's design | Harnesses it covers | Losing test, then its result |
|---|---|---|---|---|
| **A. The desktop app as the runtime, the CLI as a fallback** | The owner's app session hosts the driver and starts acts through the app's session tools. | It reverses `[supervise]`: the supervisor would live inside a model session. | Claude desktop only | **Test:** a program with no model can start an act in the app and receive a schema-checked return that carries an id. **Result: LOST.** The app's only launch paths are model-called tools (`ccd_session__start_session` and `spawn_task`, 21 calls, all made by a model). `--desktop` opens an interactive session, while `--output-format` and `--json-schema` are documented "only with --print". `layer-runtime.md:370` already rules that "a desktop scheduled task wakes a model session… never the supervisor", and agents die with their parent process (`:159`). |
| **B. The CLI or SDK as the one runtime, any app as a viewer** | The supervisor launches `claude -p` per act. The app sees the same transcript store, session list and ids. | None: this is today's `[supervise]` and `[spawn]`. | Claude Code in the CLI, the desktop app and an IDE (one engine and one store). No Codex. | **Test:** a headless run returns an id, a resume by that id remembers, and the owner's surface can see the session. **Result: passes for Claude.** Run 2, the resume and `agents --json` all held. Whether the app's sidebar shows a `-p` session was not observed. **It loses on agnosticism:** an owner working in the Codex app gets nothing from B. |
| **C. Harness adapters, each passing a conformance fixture; the owner's app chosen by policy** (extends `[harness]` and `[extend]`, `layer-runtime.md:788-869`) | Each harness is a registered adapter whose capability rows are measured by one fixture and stored in the node registry. The supervisor picks the act backend by those rows. The owner's surface is a viewer adapter. | It adds the fixture, a `runtime.owner-harness` key and an act-harness key. It changes no core code (`extension` fixture, `:868`). | All five: Claude Code CLI, desktop and IDE; Codex CLI and app. Each is covered at its measured rows. | **Test:** the fixture must separate every pair of harnesses (if all pass, it is a rehearsal), and a stub adapter must register without editing Runtime. **Result: passes on the measured rows.** Claude CLI against Codex CLI: an id preset at launch (`--session-id` versus none), headless fork (`--fork-session` versus interactive only), `Workflow` (yes versus none in features), messaging between sessions (documented versus not found). CLI against desktop: launch by a program (yes versus no). The stub-registration half is owed to the build. |
| **D. gov as an MCP server for every harness** | gov's verbs are exposed as MCP tools (`claude mcp`, `codex mcp`). | It adds a client surface. | Any harness with MCP | **Test:** it must give a target harness something the CLI verbs (P15) do not. **Result: LOST.** Both harnesses have shells. MCP neither launches a session nor returns an id. The Workflow runtime has neither shell nor MCP (`check-workflow-syntax.js:41`). Codex docs say MCP hook errors do not block. |

Cloud and remote-control runtimes (`--cloud`, `--remote-control`, Codex cloud) differ only in where the session runs. They are `host-adapters` under C (`run.host: cloud-routine`), not a further mechanism.

**What headless runs, ids, structured output and the SDK give, and what they cost:**

| What they give | What they cost (measured) |
|---|---|
| The supervisor sets an id before launch (`--session-id`) and gets a schema-forced return (`--json-schema`) and a JSON result carrying cost, turns and `terminal_reason`. | **Auth:** run 1 died on OAuth refresh contention. A fresh relaunch needs a transient class that does not count against `RESUME_ATTEMPTS`. |
| The unattended path needs no skip flag: `--permission-prompts none` plus ask rules (whether they combine is untested). | **Resume price:** 51 times the fresh run. This supports `runtime.relaunch: fresh`. |
| Observability: session status from `agents --json`, and `--include-hook-events` in `stream-json`. | **Nesting:** a child inherits `CLAUDE_CODE_ENTRYPOINT`, the parent's session variables and `CLAUDE_CODE_MESSAGING_TOKEN`, a secret that authenticates posts back into the parent's inbox (documented). |
| `--input-format stream-json` gives a live channel into a session the supervisor launched. | **Version drift:** PATH has 2.1.292, which lacks `onFailure` (needs 2.1.295, `layer-runtime.md:179`); the app has 2.1.299 at a path that changes on every update. |
| | **Silent bypass:** a launch with `--bare` or `--safe-mode` skips hooks. |

5. **Session ids as memory**

**What an id gives:**

| What it gives | Claude Code | Codex |
|---|---|---|
| Set at launch | `--session-id` (help) | no; read from the JSON stream's start event (third-party docs, not tested) |
| Resume | `-p --resume <id>` (tested; remembered) | `exec resume <id>` (help) |
| Fork | `--fork-session` (help) | interactive `fork` only |
| Transcript | `~/.claude/projects/<cwd>/<id>.jsonl` (tested), with `subagents/` and `workflows/` beside it | `~/.codex/sessions/…/rollout-…-<id>.jsonl` (tested) |
| Live address | inbox plus `SendMessage` (documented); `agents --json` maps id to status (tested) | none found |
| Attribution | the transcript's `entrypoint` is wrong when nested (tested) | `originator` (tested) |

**Who can drive each kind of communication between sessions:**
- **A script:** resume, fork, the transcripts, `agents --json`, `stream-json` input, and posting into its own session's inbox.
- **Only a model, in the app or the CLI:** `SendMessage`, `ListAgents`, and the app's `spawn_task` and `list_sessions`.
- **Not tested:** a script posting into *another* session's inbox, because testing it would message the owner's live sessions.

**What the design's mailbox assumes.** Messages are durable on `refs/gov/mail/<slug>`, and live delivery is a second copy "where the harness can message another session… citing the message id" (`coordination.md:99-113`, `deps.messaging`, v2:839). Claude's inbox satisfies that live channel. Codex has none, so it uses the mailbox only.

**How ids join the relational syntax.** Today an id keys the per-session card (`<git-common-dir>/orientation/<sid>.md`, 22 files, read at `scratch-guard.js:774`) and run claims (`unattended.sh:8901`). No commit carries one: the trailers in the last 500 commits are Co-Authored-By 492, Pass 246, Decided 106 and manifest-audit 7. v2's 12+1 edge set (night-pass:253) and its tag namespaces have no `session` node.

The proposed join:
- The act record is the key that does not depend on the harness. The supervisor mints it and records beside it `harness`, `node` and `harness-session`. A transcript never leaves its node (`layer-runtime.md:854`), so an id is only a pointer that resolves on its own node.
- Journal lines, returns and the commit queue's trailers carry `act=`.
- A `session` namespace is derived from binding records, never typed, with `part-of` (to the act or build) and `after` (lineage through resume and fork). No new edge type is needed.

**A harness without ids** (Gemini, Copilot, Cursor) gets the act id alone. It is carried in the launch environment and the commit trailer, its return comes through a git-boundary witness, and a relaunch is always fresh.

6. **Chain, gaps and forks**

**Units to add, by owning build:**

| Build | Unit |
|---|---|
| dWellOiledMachine | Add a `harness-conformance` fixture to unit 11. Its rows: launch by a program, id preset or returned, resume, headless fork, schema return, the hook events and fields the packs read, the fail-closed path, the live inbox, where transcripts live, settings-source injection. Each is measured per binary into unit 12's node registry. |
| dWellOiledMachine | The spike also runs on the app's bundled binary, and tests `--permission-prompts none` together with the dispatcher's ask rules. |
| dWellOiledMachine | Preflight refuses `--bare`, `--safe-mode`, `bypassPermissions` and the skip flag. |
| dWellOiledMachine | A launch-environment allowlist that scrubs `CLAUDE_CODE_MESSAGING_TOKEN`, `CLAUDE_CODE_ENTRYPOINT` and the parent's session variables. |
| dWellOiledMachine | A transient-auth relaunch class. |
| dWellOiledMachine | The act id minted at launch (`--session-id`) and recorded, and the `act=` commit trailer. |
| dWellOiledMachine | A `session-inbox` notification adapter. |
| dWellOiledMachine | Codex's capability row re-measured at 0.139: unit 11's "measured floor" and DA-M14's prompt-submit drain now apply to Codex. |
| dKeptSession | Live delivery through `session-inbox` where the fixture row passes. |
| dKeptSession | The `session` namespace derived from bindings, with `part-of` and `after`. |
| dKeptSession | The card's session list read from `claude agents --json`. |
| dTotalRecall | `act` and `harness-session` fields in the return and journal record kinds. |
| dShippedRelease | Codex install targets (`.codex/hooks.json`, `.codex/config.toml`), with the hook-trust step surfaced. A planted project hook must be seen to fire after trust and skipped before it. |

**Gaps to register (proposed numbers, continuing each family):**

| Gap | Owner |
|---|---|
| `gap-rt-25`: the Codex capability record is stale (`layer-runtime.md:796-798` against the current docs). | dWellOiledMachine |
| `gap-rt-26`: an act session inherits the parent's messaging token and entrypoint. | dWellOiledMachine |
| `gap-rt-27`: the PATH binary and the app binary drift apart; PATH lacks `onFailure`. | dWellOiledMachine |
| `gap-rt-28`: no preflight refusal of `--bare` or `--safe-mode`. | dWellOiledMachine |
| `gap-orient-19`: no session node in the relational syntax; no commit names its act. | dKeptSession |
| `gap-deploy-15`: Codex project hooks are skipped until trusted. | dShippedRelease |
| `gap-rt-29`: `--max-turns` is used but not listed in help (an undocumented flag). | dWellOiledMachine |

**The owner's forks:**

| Fork | Options | Recommendation |
|---|---|---|
| F1. Mechanism for staying independent of the app (a structural decision) | A; B; C with B as its first adapter | **C with B as its first adapter.** Only C covers Codex, and it extends the existing seam. |
| F2. `runtime.binary` | `newest-conforming`, `path`, `app-bundled`, a pinned path | **Default `newest-conforming`**, read from the node registry |
| F3. `runtime.owner-harness` | `auto` or any registered adapter | **Default `auto`**, taken from the binding at a top-level session |
| F4. `runtime.act-harness` | registered adapters that pass the act rows | **Default `claude-code`**. A Codex act backend registers only once its rows pass. |
| F5. Where sessions sit in memory (a structural decision) | a derived node with existing edges; a field only; new edge types | **A derived node with existing edges.** |
| F6. `runtime.act-auth` | `oauth-shared`, `setup-token`, `api-key` | **Default `oauth-shared`**, with transient retries |

**What I wrote.** One scratch directory with `help.txt`, `codex-help.txt`, `codex-exec-help.txt`, `agents.json` and `run1.json` to `run3.json`, under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/away/d108/`. The CLI also wrote two transcripts under `C:\Users\d41ly\.claude\projects\C--Users-d41ly-AppData-Local-Temp-claude-…-away-d108\`. Nothing was written in the repository.

**Sources:**
- [Claude Code: messaging your other sessions](https://code.claude.com/docs/en/cross-session-messaging.md)
- [Codex hooks](https://learn.chatgpt.com/docs/hooks)
- Third-party, not official: [Codex session management](https://codex.danielvaughan.com/2026/04/13/codex-cli-session-management-resume-fork-transcripts), [codex exec JSONL reference](https://codex.danielvaughan.com/2026/04/08/codex-exec-jsonl-reference/), [Codex SDK](https://wikidocs.net/371047)
