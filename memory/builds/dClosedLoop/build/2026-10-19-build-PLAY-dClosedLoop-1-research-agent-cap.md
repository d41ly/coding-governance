# Research: agent-cap, measured, and the in-flight limit

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 136's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-17-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`.

---

## The question: what agent-cap actually does, and what should replace it

**Short answer:** agent-cap never counts agents in flight. Direct `Agent` spawns get 5 claims per (session, prompt id). Each claim frees 45 minutes after it was made, and every new prompt id starts a fresh budget. A new prompt id comes with every human turn and also with every task notification: 73 of the 143 prompt ids in this session were notifications. `Workflow` agents are never counted at runtime. The owner's "5 every 45 minutes" is right within one prompt id and wrong across them, because across prompt ids there is no bound at all.

Pick: put the limit in one Runtime policy key, enforced at three scopes. The harness's own concurrency settings cover one workflow run and one session's direct spawns. A Runtime hook pack built on SubagentStart/SubagentStop covers the session-wide total. The supervisor covers act sessions and nodes.

I wrote nothing in the repository. The probe copy lived under the scratchpad (system temp) and is deleted. Two probes read the real tree; the real ledger had 7 directories before and after.

---

### 1. Rule inventory (`tools/hooks/agent-cap.js`, v1.38, `:104`)

Wiring: `PreToolUse` matcher `Workflow|Agent` (`.claude/settings.json:4-12`). It blocks with exit 2 plus stderr. The calls run in this order (`main()`, `:2190-2425`):

| Rule | Code | What it enforces | What it protects | Config it reads |
|---|---|---|---|---|
| AGENT_CAP refusal | `:2245-2256` | Refuses every call while `AGENT_CAP` is set | No ceiling raise that "leaves no diff" (`:105-106`) | env `AGENT_CAP` |
| Declared cap | `:1633-1657`, `:2261-2267` | `EFFECTIVE_CAP = min(FANOUT_CAP, 5)`; a value outside 1..5 denies every call | A repo may only lower the cap (TOOL-aRepatriatedFork-7, `:68-72`) | `.agent-cap.conf` at the checkout root (absent in gov), `CAP=5` `:107`, `MAX_VERIFIERS=5` `:492` |
| `--print-cap` | `:2199-2211` | Query mode for shell readers; refuses if wired | One parser of the conf | Its readers: `tools/workflows/check-verifier-fanout.sh`, `check-protocol-parity.test.sh`, the renderer's `FANOUT_CAP` token (`tools/workflows/kit.toml:65-85`) |
| `--only=join\|scripts` | `:2222-2231` | Runs a subset of rules for the file gates | — | — |
| **Rule 6**, handoff spawn guard and harness admission | `:2273-2295`; Agent `:2089-2148`; Workflow `:2157-2188` | `Agent`: an `agent`-true role, the prompt byte-equal to marker + `## Task`, `task-sha`, and the description. `Workflow`: `scriptPath` must be in `harnesses`, no inline `script`, and `args.roles` valid | Handoff provenance; only registered harnesses run | `.claude/roles.json` (armed in gov; harnesses = tier2-review, unattended-build, unattended-unit) |
| **Rule 4**, direct-spawn slot ledger | `:1487-1752`, `:2299-2304` | O_EXCL `slot-1..N` under `<git-common>/agent-cap/<session>__<prompt>/` (`:1693-1709`). Same `tool_use_id` is idempotent (`:1699-1703`). A slot older than `SLOT_TTL_MS = 45 min` is re-claimable (`:1580`, `:1717-1727`). Turn directories are swept after 12 h (`:1542`, `:1664-1680`). **Fails open** when `session_id`, `prompt_id` or `tool_use_id` is missing, or the common dir or mkdir fails (`:1690-1695`). Fails closed when the token cannot be created (`:1730-1734`) | A burst of direct spawns | `EFFECTIVE_CAP` |
| **Rule 0**, spec-audit opt-in | `:1894-2027`, `:2310-2316` | A `Workflow` whose args carry `kind: spec-audit` or `specAudit` needs a dated README `spec-audit:`, else `SPEC_AUDIT_DEFAULT`, else the live run's pinned fact | The owner's opt-in to a pre-code audit (TOOL-aBlindedTrial-6/7, TOOL-aWardedAudit-2/6). Not a fan-out bound (`:29`) | Build README front matter, `.unattended.conf`, `RUN.md` |
| Script read | `:2322-2336` | Reads inline `script` or `scriptPath`; a `name:`-only run exits 0 unscanned | — | — |
| **Rule 2**, verifier arity, lens count, markers | `fanoutFindings` `:789-1265`, deny `:2338-2353` | `agent()` reached through iteration needs a provably bounded receiver: `gov:fixed-verifiers` (K ≤ cap), an array literal of ≤ `MAX_LENSES=5` elements (`:497`, `:635`, `:964-968`), or `gov:sequential-agents(K)` | Review protocol: verify stage ≤ 5 TOTAL; lens arrays ≤ 5 | `EFFECTIVE_CAP`, `MAX_LENSES` (fixed) |
| **Rule 3**, the bound is read | `capFindings` `:1382-1484`, deny `:2358-2371` | The call-site K, the helper default and the `gov:bounded-fanout` slice width must each resolve to ≤ cap; `x \|\| 5` never resolves | A cap that is enforced, not conventional | `EFFECTIVE_CAP` |
| **Rule 1**, raw-primitive ban | `offendingLines` `:452-465`, deny `:2379-2407` | Raw `parallel(`/`pipeline(` only on a `gov:bounded-fanout` line | Workflow concurrency hitting the harness's ~14–16 and the server rate limiter (`:5-13`) | — |
| **Rule 5**, ref-keyed join ban | `scanJoinFindings` `:1767-1811`, deny `:2410-2422` | No `.ref`-keyed verdict map, no `verdictByRef` | Review verdict correctness. Not a cap | — |

Rules 1, 2, 3 and 5 run over both the lexed and the frozen "shipped" views and union the denials (`runBothViews`, `:419-450`).

**Where records, code and outside docs disagree:**
- `:5-10` says the harness workflow cap "is NOT lowerable from userland". The workflows docs say it is: `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`, 1–256, v2.1.269+. This node runs 2.1.292, and the binary carries the string `workflow: concurrent agent gate = … (CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS)` (measured with `grep -a` on `~/.local/bin/claude.exe`).
- `:24` says the budget "resets on the next user prompt". It actually resets on every prompt id, notifications included (see §2).
- `:1566-1567` says `Agent` skips the tool events; `:1496-1497` says a sidechain holds no `Agent` tool. Current docs say otherwise on both. `research-runtime-spawn.md` (lines 30-31) already records both.
- The handed fact says "lenses fill five slots that agent-cap counts". It counts array-literal elements statically (`:635`, `:964-968`). A `Workflow` call touches no slot (probe I below).

### 2. Measured ledger behaviour

**Setup:** a copy of `agent-cap.js` and `scratch-guard.js` in a scratch dir, `git init` in a sibling `repo/`, and a probe script. With no `roles.json` and `CLAUDE_PROJECT_DIR` unset, rule 6 is unarmed. The probe script:
```
payload=$(printf '{"session_id":"%s","prompt_id":"%s","tool_use_id":"%s","cwd":"%s","hook_event_name":"PreToolUse","tool_name":"Agent","tool_input":{...}}' ...)
printf '%s' "$payload" | env -u CLAUDE_PROJECT_DIR -u AGENT_CAP node hooks/agent-cap.js
```

| Probe | Command | Output |
|---|---|---|
| Six spawns in one prompt | `for u in u1..u6; ./probe.sh S1 P1 $u` | u1–u5 `rc=0`; u6 `rc=2 BLOCKED by agent-cap: the direct-Agent spawn budget for this prompt is exhausted — 5 of 5 claimed in this turn within the last 45 minutes` |
| A. Same `tool_use_id` again | `./probe.sh S1 P1 u5` | `rc=0` (idempotent) |
| B. New prompt id, same session | `./probe.sh S1 P2 v1..v6` | v1–v5 `rc=0`, v6 `rc=2`. **10 admitted to one session; P1's five are never consulted** |
| C. Another session | `./probe.sh S2 P1 w1` | `rc=0` (separate budget) |
| D. `prompt_id` empty | `./probe.sh S1 "" z1` | `rc=0`, no directory created (fails open) |
| F. All five slots aged 44 min (agents long finished) | `touch -d '-44 minutes' slot-{1..5}; ./probe.sh S1 P1 u7` | `rc=2`. It counts claims, not agents in flight |
| G. slot-1 aged 46 min | `touch -d '-46 minutes' slot-1; ./probe.sh S1 P1 u8; … u9` | u8 `rc=0` (slot-1 now `u8`); u9 `rc=2` |
| H. All five aged 46 min | `./probe.sh S1 P1 k1..k6` | k1–k5 `rc=0`, k6 `rc=2`. Five more in the same prompt, whether or not the first five still run |
| I. Three `Workflow` calls, five-lens bounded script | Payload `tool_name:"Workflow"` ×3 | All three `rc=0`. Ledger files `before=13 after=13`, no S9 directory. Up to 15 workflow agents admitted, none counted |
| J / K. Raw `parallel(items.map…)` / six-lens literal | — | Both `rc=2 … caps verify-stage agents at 5 TOTAL` |
| L. SubagentStop and PostToolUse[Agent] payloads | — | `rc=0`, ledger untouched. Nothing releases a slot. The hook also never reads `hook_event_name`, `agent_id` or `run_in_background` (grep: 0 hits) |
| M / N. Real tree (armed): inline script; unregistered `scriptPath` | `cwd` = this worktree | Both `rc=2 … rule 6 … an inline script is never a declared harness` / `… is not a declared harness`. Real ledger 7 → 7 directories |

**This session's real ledger (read-only).** Prompt `f2e8aa44…` had 5 slots at 04:26–04:28 local; its first record is `{'kind': 'task-notification'}` at 00:24:48Z. Prompt `4d92fde2…` had 5 slots at 04:34–04:42; it opened with a task notification at 01:33:36Z. Across the transcript: `distinct promptIds: 143 {'human': 63, 'task-notification': 73, 'src:None': 6, 'src:sdk': 1}`. All 106 `Agent` results this session were `async_launched`.

**Peak in flight, from subagent transcripts** (first to last timestamp per agent transcript; this is an approximation of each agent's life):
- This session: direct-only 5, workflow-only 5, **all 8** (2026-10-19T00:20Z).
- Across 55 gov sessions: direct-only peak never above 5. Five sessions exceeded 5 in flight overall, at 6, 6, 7, 8 and 11. I did not check whether the 11 (2026-08-08) predates rule 4.

### 3. Why it counts per window, and which hook events could count in flight

- **A `PreToolUse` hook cannot see an agent end.** The hook fires before the call, and agent-cap is wired only there (`:1545-1547`). The docs say subagents run in the background by default, and a background `Agent` call's PostToolUse "returns immediately" with `status: "async_launched"`. So PostToolUse cannot release either. Source: https://code.claude.com/docs/en/hooks (read 2026-10-19).
- **SubagentStart** receives `agent_id` and `agent_type`, and can return context only; exit 2 "shows stderr to user only", so it cannot block. (hooks, read 2026-10-19.)
  - Measured: it fires for Workflow agents. All 466 workflow-agent transcripts in this session's `subagents/workflows/` carry a SubagentStart attachment (the 43 `journal.jsonl` files are not agent transcripts). All 89 direct-agent transcripts carry it too.
  - Wired today only for scratch-guard (`.claude/settings.json:111-121`).
- **SubagentStop** receives `agent_id`, `agent_type`, `agent_transcript_path`, `last_assistant_message`, and the parent session's `background_tasks`. Exit 2 keeps the subagent running.
  - It has no `tool_use_id`. Correlating by `agent_id` works, and PostToolUse's `tool_response.agentId` bridges a `tool_use_id` to it.
  - **The docs do not say whether it fires on a kill, interrupt, stall-failure or for Workflow agents.** Nothing here wires it, so this is unmeasured. (hooks, read 2026-10-19.)
- **`prompt_id`** is the "UUID identifying the user prompt currently being processed". UserPromptSubmit also fires when "a background subagent reporting back" or a scheduled task arrives. (hooks, read 2026-10-19.) That fits the measured reset on notifications, but the docs never say outright that `prompt_id` changes then.
- **SessionEnd** exists; it can serve a ledger sweep.
- **The harness's own counters** (https://code.claude.com/docs/en/sub-agents, /workflows, /env-vars, read 2026-10-19):
  - `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`: default 20, v2.1.217+. It applies "only to subagents spawned with the Agent tool", and the tool refuses with "Do not retry". It is not enforced under ultracode.
  - `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`: per single run, default 16 or fewer by CPU. Queued `agent()` calls wait for a free slot.
  - Ambiguous: whether workflow agents count toward the Agent-tool total. The binary shows only `getConcurrentSubagents`.

### 4. Replacement candidates

Each candidate below is a different mechanism. There is more than one.

**A. The harness's own caps, rendered from policy into tracked `.claude/settings.json` `env`.** The harness counts, and it knows exactly when each agent ends.
- *Test that would make it lose:* with both variables at N, can one session hold more than N agents in flight?
- *Result:* it loses as the only enforcer, per the docs (not measured). The workflow cap applies per run, so two runs give 2N. The Agent cap covers Agent-tool spawns only, and ultracode exempts it.
- It wins within one run and for direct spawns. The 2.1.292 binary carries both names.
- *Owed test:* a fixture repo with `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS=2` in settings `env` runs a four-agent workflow; red if its journal shows more than 2 overlapping.

**B. A Runtime hook pack keeping an in-flight ledger.**
- SubagentStart claims an O_EXCL slot keyed by `agent_id`; SubagentStop releases it. This reuses agent-cap's slot seam, `:1683-1752`.
- `PreToolUse[Agent|Workflow]` admits only while in-flight plus pending reservations stay under N. A Workflow call reserves its harness's declared fan from the shapes registry.
- A sweep tied to session liveness (SessionEnd, transcript age) replaces the 45-minute TTL.
- *Test 1:* does SubagentStart fire for every agent, Workflow agents included? **Passes, measured** (466/466 and 89/89).
- *Test 2, decisive:* does SubagentStop fire for every end — Workflow agents, an agent stopped with `x`, one that fails after 6 stalls, and a killed session? **Unmeasured.** If it does not, the ledger leaks and B falls back to a heuristic. This test belongs in dWellOiledMachine's `spike` (`layer-runtime.md` `[tests]`, lines 1047-1050), extended to those four end kinds.
- *Test 3:* SubagentStart cannot block (docs). So agents inside a run are bounded only by the reservation at the call plus A's per-run cap. That is accepted, not a loss.

**C. The supervisor reserves each act's declared fan under the lease** (`layer-runtime.md` `[supervise]`, lines 428-438; dWellOiledMachine unit 6, line 984).
- *Test:* can it refuse a spawn in the owner's attended session?
- *Result:* no. The record itself sends the attended case to a PreToolUse entry (lines 434-437), and the supervisor is not built. So C is the layer for act sessions and nodes, not a replacement on its own.

**D. Keep agent-cap's ledger, re-keyed per session, TTL kept.**
- *Test:* five short agents finish, then a sixth spawns. **Loses, measured:** probe F denies the sixth with every slot idle, and probe H admits five more at 46 minutes regardless of whether the first five still run.
- Rejected: it measures claims, not agents in flight.

**E. Derive in-flight from the harness's own files** (`subagents/workflows/*/journal.jsonl` started/result pairs, task notifications in the main transcript).
- *Test:* is there a documented end signal for every agent kind?
- *Result:* rejected. The journal does carry `{"type":"started"|"result","agentId",…}` pairs (measured 12/12 in one journal), but no timestamps. The docs publish hook payloads, not this format, so a guard built on it can break silently on an upgrade.

### 5. Where each of agent-cap's rules goes on retirement

| Rule | Destination | Owner |
|---|---|---|
| Rule 4 and the `FANOUT_CAP` conf, `--print-cap`, AGENT_CAP refusal | The key `runtime.agents-in-flight` in `.governance/policy.toml`, as its **one** carrier. `.agent-cap.conf` retires in the same unit, because a second carrier was already refused once (`runtime-reviews-compared.md` line 188; `layer-runtime.md` line 952 retired `runtime.fanout` for that reason). `--print-cap` readers re-point to the policy reader. Enforced by A + B + C. The key name is my proposal. | Key: dGroundRules (schema) and Runtime's catalogue. Enforcement: dWellOiledMachine |
| Rule 1 and the concurrency half of rule 3 (call-site, default and marker widths) | Retire. The harness's per-run cap rendered from the key replaces them, and it queues rather than refuses. The premise at `:8` is now false. | dWellOiledMachine (settings-merge renders `env`) |
| Rule 2 (verify total ≤ 5, loop markers) and the lens count `MAX_LENSES` | The harness checks at the merge bar (`check-verifier-fanout.sh`, re-hosted) plus the shapes registry's declared fan and five lens slots (`flow-roles-adoption.md` `[design]` lines 166-167 and 198). Probes M/N show that in an armed repo the call-time population is only registered harness files, which the bar already scans. | dBoundRoles (shapes), dFairHearing (harness/lens) |
| Rule 5 (join ban) | The review kit's file gate (`check-review-join.sh`) only | dFairHearing |
| Rule 6 (handoff and harness admission) | The roles pack, per the owner-pack table (`layer-runtime.md` line 593); later folded into act binding (lines 469-478) | dBoundRoles; binding: dWellOiledMachine |
| Rule 0 (spec-audit opt-in) | Its own review-kit PreToolUse[Workflow] pack now. It cannot move into the harness, because workflow scripts have "no direct filesystem" access (workflows docs). Later into act binding. | dFairHearing, then dWellOiledMachine |

Two gaps remain after retirement:
- **An edited harness runs before the bar sees it.** A harness file edited but not committed runs at call time without being scanned. Fix: admission compares the harness to its landed blob, as v2's composition reads landed revisions.
- **Unarmed adopters lose the inline-script total check.** An adopter with no `roles.json` can still run inline scripts. Their concurrency stays bounded by A, but the verifier total goes unchecked.

### 6. Pick

The limit belongs to **Runtime**: one key, enforced at three scopes.
1. **The harness's own settings (A)** for one workflow run and one session's direct spawns. These are the only reliable in-flight counters available today.
2. **Runtime's SubagentStart/SubagentStop pack (B)** for the session-wide total. It depends on SubagentStop test 2 above, which is owed to the spike. If test 2 fails, the fallback is A with the key split between direct and workflow budgets, plus admitting one live run per session.
3. **The supervisor's lease reservation (C)** for act sessions and nodes, as already designed.

agent-cap.js then retires, with its other rules moved as in §5.

**A fork for the owner:**
- **Today the cap is lower-only.** It cannot go above 5 (`:61-72`, TOOL-aRepatriatedFork-7), and v2's shapes fix "`FANOUT_CAP`'s bound".
- **The owner's ask conflicts with that.** "Owner-adjustable" means the key can be raised.
- **The reason for lower-only does not apply here.** The env knob was refused because it "leaves no diff" (`:105-106`). A tracked policy write does leave a diff, so it does not block a raisable key.

**Records to correct:**
- `layer-runtime.md` lines 429-438 and 935: they bind Runtime to "agent-cap's lower-only cap" and keep "agent-cap's per-prompt total unchanged".
- `architecture-v2.md` `[policies]` line 919 and `[owed]` line 1614: they keep `FANOUT_CAP` in its kit conf.
- `gap-rt-05` (`gap-register.md` line 247) is accurate. It should add that the 45-minute claim expiry also admits a sixth agent while five still run.

Sources (all read 2026-10-19): https://code.claude.com/docs/en/hooks · https://code.claude.com/docs/en/sub-agents · https://code.claude.com/docs/en/workflows · https://code.claude.com/docs/en/env-vars

Files: `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\hooks\agent-cap.js`, `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\.claude\settings.json`, `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\workflows\check-verifier-fanout.sh`, `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`, `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`, `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md`
