# Research: preserving orientation — where a build's card lives, and how it reaches priority 1 beside the charter

**Serves:** research PLAY-dClosedLoop-1

The gov-researcher's return for handoff `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-10-researcher.md`
(dispatch 15), sent at the owner's request in orientation OR-5, verbatim. The harness escaped `<` and
`>` in the returned text as HTML entities; they are restored here, and nothing else is changed.

---

## 1. Inventory

- **Run-claim ref (seam 1).** Today `refs/gov/runs/<slug>` is a parentless commit written by compare-and-swap. It carries eight keys, a bounded fetch reads it, and its age is computed. `tools/unattended/unattended.sh:2077-2186`
- **Session card in the shared git dir (seam 3).** Stored at `<common-dir>/orientation/<sid>.md`, keyed by session id with an 8,192-byte cap. `skills/session-kickoff/manifest-check.sh:210-216,311-316,706-725`
- **SessionStart hooks.** `startup|clear` runs `--card --write`; `resume|compact` runs `--card --replay`. Their plain stdout becomes context. `.claude/settings.json` (SessionStart block)
- **SubagentStart hook.** Already puts the parent card's `## route` into each subagent as `additionalContext`. `tools/hooks/scratch-guard.js:1455-1545`
- **Committed record (seam 2).** A card re-rendered into `memory/builds/<slug>/`. No writer exists today; the closest is the orientation record, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md`.
- **CLAUDE.md `@import`.** The entry file is `CLAUDE.md` = `@AGENTS.md` (12 bytes). Imports go up to four hops deep and load "at launch alongside the CLAUDE.md". https://code.claude.com/docs/en/memory#import-additional-files
- **Unscoped `.claude/rules/*.md`.** These load at launch and are "re-injected from disk" after compaction. The only rule today is `.claude/rules/product.md`, and it is path-scoped. https://code.claude.com/docs/en/context-window#what-survives-compaction
- **CLAUDE.local.md.** Lives in one worktree only, and it suppresses the direct AGENTS.md read. https://code.claude.com/docs/en/memory#agents-md
- **PreCompact / PostCompact.** Neither can inject context; PreCompact can only block. https://code.claude.com/docs/en/hooks
- **UserPromptSubmit `additionalContext`.** Fires on every prompt and lands "alongside the submitted prompt". Same URL.
- **InstructionsLoaded.** Observe-only. Same URL.
- **`--append-system-prompt`.** Fixed at launch, at system-prompt level. https://code.claude.com/docs/en/memory (troubleshooting)
- **Skills.** A skill's body arrives through the Skill tool. Invoked bodies are re-injected after compaction, capped at 5,000 tokens each. A subagent's `skills:` field preloads them. https://code.claude.com/docs/en/sub-agents
- **Auto memory.** Per repo, shared across worktrees, first 200 lines or 25 KB. Not given to non-fork subagents. https://code.claude.com/docs/en/memory#auto-memory
- **Subagent `memory:` field and forks.** A fork inherits the parent's context; `omitClaudeMd` drops project and local CLAUDE.md. https://code.claude.com/docs/en/sub-agents. The roles renderer writes `omitClaudeMd: true` (`tools/roles/render_agents.py:132`).
- **Harness worktree notice.** The harness injects its own "You are operating in a git worktree…" context at compaction (transcript line 1853).
- **Codex.** Reads `AGENTS.override.md`/`AGENTS.md` from the root down to cwd, one file per directory, up to `project_doc_max_bytes` (32 KiB), once per run, with no documented `@import`. https://learn.chatgpt.com/docs/agent-configuration/agents-md. Its SessionStart and SubagentStart hooks sit behind a feature flag. https://developers.openai.com/codex/hooks
- **MCP resources/prompts, output styles, Agent SDK session store.** These reach the model as tool output or `@`-mention (evidence), as static system text, or as a transcript copy. None is re-keyed. Absent from this repository: no `.mcp.json`, no output style.

## 2. Sequence

| Event | Delivers the card today | Rank on arrival | Cost |
|---|---|---|---|
| New session | SessionStart `--card --write` stdout | system-reminder at the hook point, not the CLAUDE.md slot | 0 calls; 994–7,777 B (about 0.3–2.2k tokens) |
| Resume | `--card --replay`, keyed by session id | system-reminder | 0 calls when it fires. **Did not fire** at 16:21:01Z in this session |
| Compaction | `--card --replay` (7,239 chars); CLAUDE.md is re-read from disk | system-reminder; its `now —` line reported **main**, not the worktree | 0 calls, then the median 15 re-read calls the cost research measured |
| Process death | the file in the common dir survives; a new session id cannot find it by build | — | the full kickoff (median 35 calls, 146k tokens) |
| Another node | nothing: the card is local, and the run claims carry no position | — | full kickoff |
| Another harness | Codex reads AGENTS.md only; the card hooks are Claude-specific | — | full kickoff |
| Subagent | SubagentStart sends the `## route` lines only; no CLAUDE.md under `omitClaudeMd` | system-reminder | 0 calls; route only |

With an imported per-worktree file, the card would sit in the charter's own slot on new sessions and compactions (re-read from disk), would reach Codex only if rendered into a file Codex reads, and would reach no `omitClaudeMd` subagent.

## 3. Measurements

- `wc -c AGENTS.md CLAUDE.md` gave `16732 AGENTS.md`, `12 CLAUDE.md`.
- `claude --version` gave `2.1.292`. The card's `cli —` cell says the session itself runs 2.1.295.
- Sizes of the 20 cards in `.git/orientation/`, by `wc -c`: `994 … 7312 7777`. The largest is 7,633 characters, against the harness cap of 10,000 characters per hook output.
- Python over this session's transcript, filtered to SessionStart records:
  - `1852 SessionStart:compact 7239 chars` at 15:54:52, right after the compaction summary at line 1839.
  - Lines `2221-2222 SessionStart:resume` are procmon and check-wiring only. No card record.
- Compaction record, cells pulled out: `tree — …/gov-architecture-plan-e34297 · worktree · … dirty 11` sits next to `now — HEAD 97e782d5… · main · clean`.
- `git rev-parse --show-toplevel` from the primary tree gave `C:/projects/coding-governance` / `main`. The startup check-wiring line resolved `C:/projects/coding-governance/.claude/settings.json`, so the hooks ran in the primary tree.
- Tally over every transcript in this project's directories:
  - Card hook records: startup 19, compact 7, resume 7.
  - Other SessionStart hooks: resume 33, startup 71.
- `git status --porcelain | wc -l` gave `0`. The card still says `dirty 11`, a stale cell nobody marked.
- `time git ls-remote origin 'refs/gov/runs/*'` gave `real 0.563s` and listed 17 refs.
- `time` of rev-parse plus status (the local key recompute) gave `real 0.191s`.
- `git check-ignore -v CLAUDE.local.md .claude/rules/orientation.local.md .claude/orientation.md` exited 1: none of them is ignored. Only `.claude/worktrees/` and a few others are excluded (`.git/info/exclude`).
- `grep -n -i "rank\|ladder\|envelope" AGENTS.md` found no match. **The record and the code disagree here:** the instruction ladder is settled in the dClosedLoop records but absent from the charter.
- `grep omitClaudeMd tools/roles/render_agents.py` gave `:132 "omitClaudeMd: true"`.
- `git log --oneline --all -- memory/builds/dRedressedBar | wc -l` gave `23`, a proxy for how many commits a per-transition card would add.

## 4. Gaps

- **HIGH.** The card is keyed by session, not by build, so a new session, a dead process or another node cannot look it up. `manifest-check.sh:316`
- **HIGH.** The replay re-keys in the hook's tree, not the session's. Compaction reported `main · clean` for a worktree session. `manifest-check.sh:499,724`; transcript line 1852.
- **HIGH.** A resume delivered no card (16:21:01Z, lines 2221-2222). The cause is unknown.
- **HIGH.** No card exists on the remote. The run claims carry eight keys and no step or next item. `unattended.sh:2077-2079`
- **MED.** Hook context lands as a system-reminder at the hook point, never in the charter's slot. https://code.claude.com/docs/en/hooks. The ladder text is absent from AGENTS.md.
- **MED.** `omitClaudeMd: true` subagents get no import-based card, and SubagentStart passes on only the route. `render_agents.py:132`, `scratch-guard.js:1500`
- **MED.** The card's cells carry no freshness key: dirty went from 11 to 0 unmarked.
- **MED.** Codex has no `@import`, and its card hooks need a feature flag. Charter plus card (16,732 + 8,192 = 24,924 B) fits its 32 KiB.
- **LOW.** No ignore rule exists for a generated per-worktree card file, so it would count as dirty. `git check-ignore` exit 1.
- **LOW.** PostCompact cannot inject context. https://code.claude.com/docs/en/hooks

## 5. Candidates

**A. Hook-delivered card, with a remote truth.** The card is stored in a per-build ref `refs/gov/builds/<slug>/card`, written by compare-and-swap, with `.git/orientation/<slug>.md` as a cache keyed by that ref's object id. SessionStart (all four sources) re-keys it in the payload's `cwd` and prints it; SubagentStart prints its slice.
- **Seam it extends:** `unattended.sh:2087-2151` plus `manifest-check.sh --card` plus `scratch-guard.js:1536-1545`.
- **Losing test:** after a resume or compaction, the card is absent from context, or arrives outside the charter's slot.
- **Result:** it loses on both counts.
  - A resume delivered no card (line 2221).
  - The compaction card arrived as `hook_success` at line 1852, a system-reminder rather than the charter's slot.
  - On the size limb it passes: 7,633 characters is under the 10,000 cap.

**B. Instruction-slot file.** `next` regenerates an ignored per-worktree file at every transition and at SessionStart, from the remote ref (truth) and the `.git` cache. `CLAUDE.md` imports it beside `@AGENTS.md`, or it lives as an unscoped `.claude/rules/` file. SubagentStart and the brief carry it to subagents.
- **Seam it extends:** `CLAUDE.md` (`@AGENTS.md`) plus seam A's writers and readers.
- **Losing test:** a session launched in the primary tree moves into a worktree and compacts, and the file re-read from disk is the primary tree's, or none. Or a missing import breaks the load.
- **Result:** not runnable read-only, because it needs a written fixture.
  - Read-only evidence for: the docs say project-root CLAUDE.md and unscoped rules are "re-injected from disk" after compaction.
  - Read-only evidence against: the hooks ran with the primary tree as project dir (check-wiring line 11; `now —` read main).
  - That fixture is the test the build must run before relying on this path.
  - It loses the subagent arm on its own (`omitClaudeMd`), so it needs seam A's SubagentStart path.

**C. Committed card as the single store.** The card is re-rendered and committed in `memory/builds/<slug>/` at each transition and read at entry.
- **Seam it extends:** no seam fits. The records under `memory/builds/` are the closest.
- **Losing test:** whether it can reach another node without a branch push, and whether it can be trusted at rank 1.
- **Result:** it loses.
  - It travels only with a push, while the ref is a 0.56 s compare-and-swap.
  - Under the settled ladder, anything under `memory/` is evidence (rank 7).
  - It can never key itself to the commit that contains it.
  - It adds a commit per transition (23 commits already touch dRedressedBar's folder).

## 6. Pick

My pick is **B, with A's hooks as the re-keying and fallback path:**
- The ref per build on the remote, written by compare-and-swap, is the one source of truth. It survives process death and reaches other nodes, and a reader trusts it only while its object id and the HEAD, tree and remote keys recompute equal.
- That ref is rendered into an ignored per-worktree file that `CLAUDE.md` imports. This is the only mechanism that puts the card in the charter's own slot and gets it re-read from disk at compaction.
- SessionStart hooks (startup, resume, clear, compact) re-render that file in the payload's `cwd` and print a short key line, fixing the main-tree and missed-resume failures.
- SubagentStart and the rendered brief carry the build's slice to `omitClaudeMd` subagents. For Codex, a hook (behind its feature flag) or a generated `AGENTS.override.md` carries it, within 32 KiB.

What the three current places become:
- **(1) The remote ref:** the truth.
- **(3) `.git/orientation/`:** a cache keyed by build and by the ref's object id, no longer by session.
- **(2) The committed record:** written only at the build's terminal transition, as rank-7 evidence, never re-rendered per transition.

Before anyone counts on B, the primary-to-worktree compaction fixture in §5 B must pass.

Sources:
- [Claude Code hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code memory](https://code.claude.com/docs/en/memory)
- [Claude Code context window](https://code.claude.com/docs/en/context-window)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex hooks](https://developers.openai.com/codex/hooks)
- [Codex CLI hooks guide (third-party)](https://codex.danielvaughan.com/2026/04/15/codex-cli-hooks-complete-guide-events-policy-patterns/)
