# Research: role anatomy — each role's static instructions, its task, its allowance, and what enforces each

**Serves:** research PLAY-dClosedLoop-1

The gov-researcher's return for handoff `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-11-researcher.md`
(dispatch 16), verbatim. The harness escaped `<` and `>` in the returned text as HTML entities; they
are restored here, and nothing else is changed.

---

## 1. Inventory

- **Base roles.** There are ten role files, each with front matter and a body. `tools/roles/agents/*.agent.md`.
- **House overlays.** These are seeded per-adopter text appended as `## House rules`. All ten are 0 bytes today. `tools/roles/house/*.md`, `roles_lib.py:569-582`.
- **Effort and gate policy.** `[effort]` sets each role's effort and `[gates]` lists the gate legs a role may run (spec-writer has 2, builder has 1, every other role has none). `tools/roles/house/policy.toml`.
- **Workflow table.** Ten workflows, each with `roles`, `stages` and `enforced-by`. The `enforced-by` entries are descriptions. `tools/roles/workflows.toml`.
- **Library.** `roles_lib.py` is the only reader and composer of these files: `render_role` and `render_charter_blocks`. `tools/roles/roles_lib.py:279,569`.
- **Renderer.** `render_agents.py` writes `.claude/agents/<role>.md` and `.claude/roles.json`. It emits only the keys name, description, tools, model and maxTurns, plus effort, `omitClaudeMd`, workflow and writes. `render_agents.py:64,127-138`.
- **Role index.** `.claude/roles.json` holds `workflow`, `writes`, `agent` and `gates` per role, plus the harness list. The hooks read it.
- **Catalogue checker.** R0–R15 cover grammar and the cross-references between files. `tools/roles/check_roles.py:11-72`.
- **Handoff renderer.** `handoff.py` writes the `## Role` and `## Task` sections, a marker carrying `role-sha` and `task-sha`, and the spawn description. `check` re-hashes a file. `tools/roles/handoff.py:1-75`.
- **Adopter.** `adopt-roles.sh` renders on `--scaffold`, and `--check` is the "roles render wiring" gate leg. `tools/roles/kit.toml`.
- **Spawn guard (agent-cap rule 6).** It requires `subagent_type` to be a role with `agent: true`, the prompt to be exactly the marker plus the `## Task` section, the `task-sha` to match, and the description to match. `tools/hooks/agent-cap.js:39-58,2088-2148`.
- **Role write gate (scratch-guard).** Spec writes need `writes=spec` and routed product writes need `writes=product`. It reads the payload's `agent_type`. `scratch-guard.js:91-103,1057-1110`.
- **Role-gate arm (scratch-guard).** It textually matches a role agent's Bash command against the gate legs. `scratch-guard.js:105-125,1407-1450`.
- **format-guard.** A main-loop `Stop` hook that requires `agent` and `returned` lines. It never reads what a role returns. `format-guard.js:1-40`.
- **Platform fields gov does not render.** Claude Code agent files also accept `disallowedTools`, `permissionMode`, `hooks` (scoped to the agent; `Stop` becomes `SubagentStop`), `skills` and `isolation`. https://code.claude.com/docs/en/sub-agents

## 2. Sequence

1. **Authoring.** A role file plus its overlay plus `policy.toml` are graded by `check_roles.py` R2–R14. ENFORCED as structure only, by the "roles catalogue" leg. The header (`check_roles.py:62-72`) states that it does not check what a body means, whether `enforced-by` is true, the `tools` names, or whether `output` matches where the role actually writes.
2. **Rendering.** `render_agents.py --write` produces the agent types and `roles.json`. Drift is ENFORCED by the "roles render wiring" leg's byte comparison.
3. **Activation.** The agent registry is read when a session starts. STATED only: `--write` prints a restart line (README "Restart").
4. **Handoff.** `handoff.py render` assembles the task from the role's `reads` keys and refuses if a required key is missing. ENFORCED at render time only. The task holds the unit line, a "Not supplied" line, the `reads` inputs, and the charter blocks again. It carries nothing from `returns`, `writes` or `output`, and no allowance (probe 4).
5. **Spawn.** Rule 6 admits only a hashed, rendered task under a typed role. ENFORCED (`agent-cap.js:2095-2145`). Its own stated ceiling: it never compares `role-sha` with the agent type, and a self-consistent hand-written prompt passes (`agent-cap.js:56-58`).
6. **Static instructions.** The agent-type body plus `## Charter` arrive with `omitClaudeMd: true`. Whether the CLI honours `omitClaudeMd` is STATED only; the README says it depends on the CLI version and a server flag.
7. **Tools.** The front-matter `tools:` list is ENFORCED by the platform. But all nine agent types hold Bash, and a subagent's shell calls skip the scratch check (`scratch-guard.js:750,763`).
8. **Writes.** Two of the five `writes` classes (spec, product) are ENFORCED for Edit and Write calls. `none`, `review` and `records` are "read by nothing" (`scratch-guard.js:102-103`). Product writes are admitted at class level: any path under `ROUTED_PATHS` while any routed unit is buildable. The unit's own declared paths are STATED only, in the builder body.
9. **Gates.** ENFORCED textually by the role-gate arm. Live in this session, it refused my `check_roles.py` run as "row G1 leg". Its ceiling is that it "stops forgetting, not evasion".
10. **Return.** The task's free text sets the return shape for a direct spawn. Harness stages are ENFORCED by schema (for example `tier2-review.js:562-578`). For direct spawns it is STATED only: there is no `SubagentStop` hook (settings events are PreToolUse, SessionStart, PostToolUse, Stop, StopFailure and SubagentStart).
11. **Mandatory.** R13 only checks that a `.js` file is named as the enforcer. Whether the role really is mandatory is STATED only.

## 3. Measurements

| Probe (as run) | Population | Output |
|---|---|---|
| python: bytes of base body and rendered type; count of `- [tag]` lines in AGENTS.md and in each rendered type | 10 roles, AGENTS.md | Charter is 16,732 B with 46 rule tags. Body / rendered bytes / rule lines carried: builder 2,258 / 6,310 (37.7%) / 10; spec-writer 2,376 / 6,800 (40.6%) / 13; diff-reviewer 1,372 / 5,191 / 8; orienter 1,833 / 5,063 / 5; spec-reviewer 1,728 / 5,254 / 6; researcher 1,619 / 4,731 / 4; skeptic 1,290 / 4,294 / 3; synthesizer 1,207 / 4,239 / 3; reuse-scout 647 / 3,331 / 1; session 626 / no type / 2 declared |
| `sed -n '/^## Charter$/,$p' … \| wc -c` | 9 types | Duplicated charter block per typed spawn: 2,487 to 4,220 B |
| python: sentences in each body containing never/not/no/nothing/none, then those naming a hook, `refuse`, or a hook or checker name | 10 bodies | **59 prohibitions, 1 names an enforcer** (builder: "a hook refuses the rest") |
| `grep -cE "^(returns\|reads\|rules\|output\|mandatory\|agent):"` on each rendered type; grep of the hooks for these fields | 9 types, 3 hooks | 0 in every type; no hook reads `returns`, `output` or `mandatory` |
| `handoff.py render --role gov-skeptic --build dClosedLoop --stdout` | 1 render | Sections: marker, `## Role`, `## Task` (unit line, Not supplied line, `reads` inputs, Charter rules, Protocols, Facts). No return shape and no allowance |
| Field-by-field reading of check_roles R2–R14, the hooks and the renderer | 13 fields | **Checked both ways: 2** (`name`: file stem ↔ subagent_type; `workflow`: R7/R8 role ↔ entry). **One way only:** `reads` (vocabulary, then render refuses), `writes` (2 of 5 classes), `rules` (tags resolve), `effort` and `gates` (R12), `agent`, `mandatory`, `output` (spelling). **Presence only:** `tools`, `model`, `returns` |
| `grep -c "^ROUTED_PATHS" .memory-tree.conf` | conf | `tools/ skills/ coding-governance-agents.template.md WIRE-INTO-PROJECT.md`. Neither `.claude/` nor non-spec `memory/` paths are under any role gate |
| Live refusal of `python tools/roles/check_roles.py` in this agent | 1 call | BLOCKED: G1 leg "roles catalogue", allowlist empty |

## 4. Gaps

- **HIGH.** 58 of 59 body prohibitions name no enforcer. Of the 6 roles with `writes=none`, all 6 hold Bash, and a subagent's Bash write is never gated (probe 3; `scratch-guard.js:763`).
- **HIGH.** There is no per-item allowance. `writes` is a class, and product writes are admitted for any `ROUTED_PATHS` path while any routed unit is buildable. "Write only the paths your unit declared" is prose (`scratch-guard.js:74,1097`; `gov-builder.agent.md`).
- **HIGH.** `returns` reaches no agent and no validator. It is absent from all 9 types and from the task, and no `SubagentStop` hook exists. Direct-spawn returns are free text (probe 4; `.claude/settings.json`).
- **HIGH.** The guard shares state with what it guards. `.claude/roles.json` and `.claude/agents/` lie outside `ROUTED_PATHS`, so a role holding Write (builder, spec-writer, synthesizer) can edit the index the hooks trust. `scratch-guard.js:101` names a hand-edited index as an escape (conf line 9).
- **MED.** The role is not bound to its rendering. `role-sha` is minted but never compared with the agent type (`agent-cap.js:58`).
- **MED.** There is no item identity. The marker holds role, build, unit and path, but no checklist item and no witness key (`roles_lib.py:77`).
- **MED.** The charter blocks are carried twice per typed spawn (2.5–4.2 KB), an "accepted cost" (README "The agent types").
- **MED.** `enforced-by` and `mandatory` are not checked for truth (`check_roles.py:62-68`). Record against code: the README says the write gate enforces `spec-write`, but `none`, `review` and `records` are unenforced.
- **LOW.** Platform fields that could carry the scope (`disallowedTools`, scoped `hooks`, `permissionMode`, `isolation`) are not rendered (`render_agents.py:64`).
- **LOW.** All overlays are empty and gov-session has no type. Session-to-session handoffs are `enforced-by none` (`workflows.toml` handoff).
- **Hand-offs to the other researchers.** Role work done outside roles goes to the coverage researcher. Return-to-next-role exchange goes to the interactions researcher.

## 5. Candidates

**A. A fuller static role contract.** Extend the role file with more static fields (an allowance as tool and path globs, a return schema), render them into `roles.json` and the agent type, and have the hooks enforce them by `agent_type`.
- Seam: `tools/roles/agents/*.agent.md` → `roles.json` → `scratch-guard.js` role arm.
- Losing test: can a per-role static field express a per-item scope? The builder's paths differ per unit.
- Result: **LOSES.** The index is keyed by role only (`render_agents.py:161-170`). The narrowest static grant is the class, which admits every routed path today (`scratch-guard.js:1097`). A static role cannot also be the per-item allowance the loop requires.

**B. A static role (job and ceiling) plus a keyed item work order (allowance and return schema).**
- The role file stays the system instructions: the job, the prohibitions, and a ceiling of tools, write classes and gates.
- `next` renders each checklist item as a work order: item id, an allowance (paths, verbs) that is the role ceiling intersected with the item, and a return schema. The work order is hashed into the marker.
- Hooks bind each subagent call to its item through the platform's own agent id. The transcript's agent id ↔ prompt-marker link already exists in `handoff.py agents --handoff` (TOOL-aOrientedCast-25), and hook payloads carry `agent_id` (`scratch-guard.js:750`).
- Writes outside the allowance refuse. A `SubagentStop` check validates the return against the schema before the witness resolves.
- Seam: `handoff.py` marker and `task-sha`, agent-cap rule 6, the scratch-guard role arm, and the harness schemas (`tier2-review.js:562`).
- Losing test: is there a binding from a subagent's calls to its handoff that no agent typed?
- Result: **survives with a caveat.** `agent_id` is in every subagent payload and the marker-to-agentId join exists, but it rides the transcript, which "is no contract" (`handoff.py:63`). The build must run the failing case: a write outside the allowance from a typed agent, observed RED.

**C. Confinement in the platform.** Render each role's scope into platform fields: `disallowedTools`, `permissionMode`, scoped `hooks` with a Stop-time return check, and `isolation: worktree` for read-only roles. The platform bounds the agent instead of repo-level hooks.
- Seam: `render_agents.py` `CLAUDE_KEYS` (`:64`).
- Losing test: does it fail closed when the hooks or the isolation do not apply?
- Result: **LOSES as the sole mechanism.** The docs say project frontmatter hooks are skipped until the folder is trusted, and plugin agents ignore `hooks` (fails open). A worktree does not sandbox Bash, which can write absolute paths in the main checkout. The fields are still worth carrying as a second layer.

## 6. Pick

I recommend **B**. A role should be an individual worker defined by static system instructions: its job, its stated prohibitions, and a ceiling of tools, write classes, gates and charter rules. Each checklist item hands it a hashed work order with its own allowance and return schema, and an enforced intersection of the two is what makes the owner's split between "system instructions" and per-session "tasks" mechanical rather than prose.

**Carried over from today:** name and workflow (already checked both ways), reads and the refusing renderer, the `task-sha` spawn guard, the write classes, the gate allowlist, effort, the rules tags, and the render-drift leg.

**Missing:**
- an item id and allowance in the marker;
- a validated `returns` schema;
- `role-sha` checked against the rendered agent type;
- Bash writes inside the allowance;
- the index and agent types placed beyond any role's write reach.

C's platform fields should be rendered as a second layer of defence, never as the guarantee.

Relevant files:
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/render_agents.py
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/roles_lib.py
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/handoff.py
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/check_roles.py
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/workflows.toml
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/roles/house/policy.toml
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/hooks/agent-cap.js
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/hooks/scratch-guard.js
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/hooks/format-guard.js
- C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/.claude/roles.json

Sources:
- [Claude Code subagents documentation](https://code.claude.com/docs/en/sub-agents)
