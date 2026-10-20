# Research: prior art — how other multi-agent systems define deterministic role workers, and what fits gov

**Serves:** research PLAY-dClosedLoop-1

The gov-researcher's return for handoff `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-14-researcher.md`
(dispatch 19), verbatim. The harness escaped `<` and `>` in the returned text as HTML entities; they
are restored here, and nothing else is changed.

---

## 1. Inventory

- **MetaGPT.** Each role has a profile, goal and constraints, plus role-specific skills. Roles exchange structured documents through a shared publish-subscribe pool, and the Engineer gets executable feedback with up to 3 retries. "`Code = SOP(Team)` is the core philosophy." Sources: https://arxiv.org/html/2308.00352 and https://github.com/FoundationAgents/MetaGPT
- **ChatDev.** A chat chain of phases; each subtask is an instructor/assistant pair set up by inception prompts. A subtask ends on a `<SOLUTION>` prefix, two unchanged code edits, or 10 rounds. Only phase solutions carry forward. https://arxiv.org/html/2307.07924
- **CrewAI.** An agent has a role, goal and backstory (static); a task has a description and expected_output (per-task). A task can override `tools`, take other tasks' outputs as `context`, and set `output_pydantic` and `guardrail` with `guardrail_max_retries` (default 3). Processes are sequential or hierarchical. https://docs.crewai.com/en/concepts/tasks and https://docs.crewai.com/en/concepts/agents
- **AutoGen AgentChat.** `RoundRobinGroupChat` (shared context), `SelectorGroupChat` (an LLM picks the next speaker), `Swarm` (`HandoffMessage`), and termination conditions. https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html
- **LangGraph.** `StateGraph` over a typed state with reducers. Routing is code: `add_edge`, `add_conditional_edges`, or `Command(goto, update)`. Adds a `checkpointer` and `interrupt`. https://docs.langchain.com/oss/python/langgraph/graph-api
- **OpenAI Agents SDK.** Handoffs are tools named `transfer_to_<agent>`, with a validated `input_type` schema, an `input_filter` and `on_handoff`. Agents take an `output_type`. Input, output and tool guardrails raise tripwire exceptions. https://openai.github.io/openai-agents-python/handoffs/ and https://openai.github.io/openai-agents-python/guardrails/
- **Anthropic research system.** Each subagent brief carries an objective, an output format, tool guidance and boundaries. Results come back as artifacts plus lightweight references. Retries and checkpoints are deterministic safeguards. https://www.anthropic.com/engineering/multi-agent-research-system
- **Claude Code subagents.** The file body is the system prompt. `tools`/`disallowedTools` scope tools, and `name` reaches hooks as `agent_type`. The parent gets "only the summary", and no schema option is documented. https://code.claude.com/docs/en/sub-agents
- **Claude Code hooks.** SubagentStop gets `last_assistant_message`; exit 2 "prevents the subagent from stopping". https://code.claude.com/docs/en/hooks
- **MAST.** 1600+ traces across 7 frameworks, 14 failure modes, kappa 0.88. https://arxiv.org/html/2503.13657
- **Gov role source.** The static half is the agent file's body plus `tools:`, `writes:` and `returns:`. `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/agents/gov-researcher.agent.md`
- **Gov per-task half.** `handoff.py` renders `## Role` and `## Task` with role-sha and task-sha. `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/handoff.py:30-31`
- **Gov spawn guard.** Admits an Agent call only with a matching marker and task-sha. `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/hooks/agent-cap.js:45-62`
- **Gov role write arm.** `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/hooks/scratch-guard.js:91-103`
- **Gov harness schema.** `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/workflows/unattended-unit.js:335` (`schema: UNIT_SCHEMA`)

## 2. Sequence

**Prior art**
- **Static vs per-task separation.** CrewAI splits the Agent (role, goal, backstory) from the Task (description, expected_output). Claude Code splits the agent-file body from the Agent prompt. ChatDev uses an inception system prompt per pair. All STATED only: nothing checks that the per-task text stays out of the role's scope.
- **Scope.** Claude Code `tools` is ENFORCED by the platform. `Bash(...)` specifiers still remove the whole tool, so command-level blocks need `permissions.deny`. OpenAI tool guardrails are ENFORCED by a tripwire exception. CrewAI and MetaGPT constraints are STATED only.
- **Exchange.**
  - Direct handoff: OpenAI handoff tool with a validated `input_type` (ENFORCED), and AutoGen `HandoffMessage`.
  - Shared state: LangGraph typed state with reducers, and MetaGPT's subscription pool.
  - Supervisor: CrewAI hierarchical, AutoGen Selector (an LLM picks, so STATED), Anthropic's lead agent.
- **Determinism.**
  - Code-chosen transitions: LangGraph edges and `Command` (ENFORCED by code), ChatDev's fixed phase chain, CrewAI sequential.
  - Schema plus bounded retry: CrewAI `guardrail_max_retries`, OpenAI `output_type` with an output guardrail, MetaGPT's 3 executable-feedback retries.
  - Checkpoints: LangGraph and Anthropic.

**Gov today**
- The role file renders to `.claude/agents`, and its `tools:` list is ENFORCED by the platform.
- The handoff marker and task-sha are ENFORCED at spawn (agent-cap.js:45).
- Write class by `agent_type` is ENFORCED for Write and Edit only (scratch-guard.js:91). Bash writes escape it (scratch-guard.js:85).
- The return:
  - On the harness route, it is ENFORCED by a schema (unattended-unit.js:335).
  - On the direct route, it is STATED only. `returns:` is prose; check_roles.py:95 requires the key to exist and reads nothing in it.
  - SubagentStop is wired by nothing in `.claude/settings.json`.

## 3. Measurements

**Probe A: tool calls per typed `gov-*` subagent transcript, checked against each role's `tools:` allowlist** (python, streaming every `*/subagents/**/*.meta.json` and its `.jsonl`)

- Population: 142 transcripts, 7,425 tool calls.
- Off-allowlist calls:
  - Write or Edit: 0.
  - `StructuredOutput`: 98, all injected by the harness.
- By role:

| Role | Transcripts | Bash calls |
|---|---|---|
| gov-builder | 23 | 1,311 |
| gov-spec-writer | 56 | 2,211 |
| gov-researcher | 19 | 569 |
| gov-spec-reviewer | 20 | 895 |
| gov-skeptic | 20 | 203 |
| gov-synthesizer | 4 | 10 |

**Probe B: mutating commands in the `writes: none` roles** (researcher, skeptic, spec-reviewer). Population: 59 transcripts, 1,667 Bash calls.

- A raw regex for mutating words matched 39 times. Most were `mkdir`/`rm`/`tee` on temp paths; the rest were quoted text.
- Anchored to command position, the result was:
  - live `git commit`/`push`/`merge`: 0
  - `cp`, `touch` or `sed -i` outside temp: 0
  - one `git worktree list`

**Probe C: return route against return shape**, over all 142 typed transcripts:

| Spawn route | Structured return (`StructuredOutput`) | Free text |
|---|---|---|
| Harness | 94 | 0 |
| Direct | 0 | 48 |

**Probe D: heading count in the final message of direct-spawned role agents**

- gov-researcher (n=19): 11 returns carry 6 or 7 headings; 8 carry 0.
- gov-spec-writer (n=29): 2 carry 4 headings; 27 carry 0.
- Caveat: the shape each task asked for varied. This shows that no contract is checked, not a failure rate.

**Probe E: hook events and interactivity**

- Hook events in 64 main transcripts: SubagentStop 3, SubagentStart 15, PreToolUse 326, Stop 10.
- Project `.claude/settings.json` wires PreToolUse, PostToolUse, SessionStart, Stop and SubagentStart, and no SubagentStop.
- Harness agents: 1,181 carry `requestNonInteractive=True`; 1,528 carry None.
- Claude Code version: `claude --version` printed 2.1.292.

**Probe F: workflow drivers.** `workflows.toml` has 10 workflows: 4 workflow, 2 agent, 2 program and 2 main-loop.

**MAST mode prevalence**, read from the paper:

| Mode | Prevalence |
|---|---|
| FM-1.2 disobey role specification | 1.5% |
| FM-1.1 disobey task specification | 11.8% |
| FM-1.3 step repetition | 15.7% |
| FM-1.5 unaware of termination | 12.4% |
| FM-2.6 reasoning-action mismatch | 13.2% |
| FM-3.2 no or incomplete verification | 8.2% |
| FM-3.3 incorrect verification | 9.1% |

- Interventions: ChatDev +9.4% from better role specifications (the paper also credits +9.4% to a workflow change, which is inconsistent); a verification step +15.6%.
- ChatDev ablation, quality score: removing roles 0.2212 against 0.3953 for the full system.
- MetaGPT: executable feedback adds 4.2% (HumanEval) and 5.4% (MBPP).

## 4. Gaps

- **HIGH.** On the direct route, an exchange between roles is never structured: Probe C, 48 of 48 free text, against 94 of 94 structured on the harness route. Claude Code documents no schema for subagent returns.
- **HIGH.** A role's `returns:` is prose that no code parses; check_roles.py:95 checks only that the key exists. Every surveyed framework that has a contract types it (`output_pydantic`, `output_type`, MetaGPT documents).
- **HIGH.** The transition between items is not chosen by code where the main loop drives. Two of 10 workflows are main-loop-driven. LangGraph, ChatDev and CrewAI sequential all fix transitions in code, and MAST's largest classes are of that kind (step repetition 15.7%, unaware of termination 12.4%).
- **MED.** No SubagentStop gate exists: it is absent from the hook events wired in `.claude/settings.json`. This is the platform's only documented point that can hold a role agent until its return conforms.
- **MED.** A session launched as a role carries that role's write rights (scratch-guard.js:100-101). So a main thread run with `--agent` is indistinguishable from the role it is launched as.
- **LOW.** Platform tool scoping already holds inside role agents (Probes A and B: 0 off-allowlist writes, 0 live commits in read-only roles), which fits MAST's 1.5% for role disobedience. Role adherence inside roles is not the problem; role work outside roles is.

## 5. Candidates

**A. Program-driven graph.** Draws on LangGraph edges, ChatDev's chat chain, CrewAI sequential and MetaGPT's SOP.
- **Mechanism.** The driver runs `next`, then dispatches each item to its role through a harness `agent()` call. The call carries a schema compiled from the item, and a bounded retry if validation fails. Code picks the next item from the resolved witness; the LLM never chooses the route.
- **Seam.** `tools/workflows/unattended-unit.js:335`, `tools/roles/workflows.toml` and `handoff.py`.
- **Losing test.** A role item that needs the owner's turn mid-item, since harness agents run non-interactive. A second test: any harness-typed return that is not structured.
- **Result.**
  - 94 of 94 harness-typed returns are structured (Probe C).
  - 1,181 harness agents are flagged non-interactive (Probe E).
  - The 2 main-loop workflows (orient, plus one more) still need an owner turn. A holds for role items only if owner turns are their own items, with the actor set to the owner.

**B. Return contract gated at the role boundary.** Draws on the CrewAI guardrail with retries, the OpenAI output guardrail and Claude Code SubagentStop.
- **Mechanism.** A SubagentStop hook keyed on `agent_type` validates `last_assistant_message` against a schema derived from the role's `returns:`. Exit 2 makes the agent continue; the hook enforces a retry cap.
- **Seam.** `tools/hooks/` (the SubagentStart fragment pattern in `scratch-guard-subagent.fragment.json`) and the roles kit's `returns:` key.
- **Losing test.**
  - SubagentStop does not fire on this node.
  - Or the direct returns cannot be shaped because `returns:` cannot be schematized.
  - Or one contract ends up in two schemas: the harness schema plus the hook's.
- **Result.**
  - The event fires on this node: 3 SubagentStop events on 2.1.292 (Probe E).
  - `returns:` is prose, but 9 of 10 roles name enumerable fields; gov-session returns nothing.
  - Without one single source, B duplicates A's schema, which breaks [reuse].
  - B also checks shape, not truth, so a witness still needs a key that recomputes.

**C. Driver as a scoped main-thread agent.** Draws on Claude Code `--agent` with an `Agent(type)` allowlist and the OpenAI handoff-as-tool.
- **Mechanism.** The session itself runs as a driver agent whose tools leave out Write and Edit, and whose `Agent(...)` allowlist names only role types. Role functions therefore exist only as role tools.
- **Seam.** `tools/roles/agents/` and `render_agents.py`.
- **Losing test.**
  - The driver still needs Bash to run `next` and probes, and Bash writes escape every gate (scratch-guard.js:85-86).
  - The write arm reads a session launched as a role as that role (scratch-guard.js:100-101).
- **Result: LOSES as a standalone mechanism.** Both escapes are confirmed by reading the code. C is viable only as a layer once the Bash write gate exists, and that gate belongs to the role-anatomy and enforcement researcher.

## 6. Pick

I recommend A, the program-driven graph. The harness route is the one seam in gov where exchanges between roles are already 94 of 94 structured. Code-chosen transitions are what LangGraph, ChatDev and CrewAI sequential use against MAST's largest failure classes, which are repetition and termination errors rather than role disobedience (1.5%). Adopt B only as the direct-spawn arm of the same contract, with both arms compiled from one typed `returns:` source; otherwise it copies A's schema. Defer C until the Bash write gate exists, because today it loses on scratch-guard.js:85 and :100.

Hand-offs:
- Bash write gating and launching as a role: the role-anatomy and enforcement researcher.
- Main-loop role work: the coverage researcher.
- Exchange topology: the interactions researcher.
