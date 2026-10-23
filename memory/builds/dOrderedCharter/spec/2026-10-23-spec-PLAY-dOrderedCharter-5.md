# PLAY-dOrderedCharter-5 — ranked envelopes in every subagent handoff, the charter carried once

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base ce13efbe · streams playbook · order 24 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0035@0d7d32c8 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-27 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

A subagent loads no charter (`omitClaudeMd: true`, `tools/roles/render_agents.py:149`) and receives
charter fragments, its role and its task with nothing ranking them (gap-found-03); and every role
spawn carries the charter blocks twice, once in its agent file and once in its task, in 48 of 60
handoffs measured (research-instruction-writing-b:210, N1). This unit wraps each block a subagent
receives in the S16 envelope of its level, orders the blocks by level, and carries the charter blocks
once, in the agent file, so a subagent holds the same hierarchy the main loop does (foundations R2,
v2:953-957 P13).

## 2. Scope (IN)

- **S1** — The agent file, ranked. `render_agent_file` (`tools/roles/render_agents.py:144`) places the
  role's charter blocks first, inside a level-0 envelope whose doc is the charter's path and whose
  direction is the charter's registry row (`PLAY-dOrderedCharter-3`'s `doc.charter`), then the role's
  text, both inside the agent file's own level-5 envelope. The roles kit reads the document registry
  through `resolve_kit_dir`, the sibling resolver it already carries (`tools/roles/roles_lib.py:97`).
  Observed by AC1.
- **S2** — The handoff, ranked. `render_handoff` (`tools/roles/handoff.py:312`) wraps each block of the
  prompt file in its envelope through the inline `render_envelope` copy in `roles_lib.py`: the
  practices-at-step block (`PLAY-dOrderedCharter-21`) at level 0, doc `<charter>#practices-at-<step>`;
  the `## Role` section at level 5, doc the agent file's path; the `## Task` section at level 6, doc the
  prompt file's path. Blocks are emitted in level order, lowest number first. Observed by AC2.
- **S3** — The charter carried once. The charter blocks leave the task section (`handoff.py:397-407`
  today appends them there), so the task part a native agent type receives, `--part task`, carries no
  charter rule line and no carried section; the agent file carries them once (S1). A stand-in run is
  the main loop, which holds the whole charter at level 0, so its prompt file carries none either.
  Observed by AC3.
- **S4** — The check. `check_handoff` (`handoff.py:426`), the `check` verb, gains two arms after its
  hash compare: every envelope opened in the prompt file closes, through `read_envelopes`; and the
  envelopes' levels never decrease down the file. Each failure names the path and the envelope.
  Observed by AC4.

## 3. Non-goals (OUT)

- The envelope helper, the document registry and their gate: `PLAY-dOrderedCharter-3`.
- The role's drive line in the handoff: `PLAY-dOrderedCharter-6`, whose block sits inside the role's
  envelope.
- The work order's packet budget and handed facts as fenced data: dBoundRoles.
- The card's slice reaching a subagent through the subagent-start hook: `PLAY-dOrderedCharter-8`.
- Another harness's subagents: dWellOiledMachine's adapters.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-3` — `render_envelope`, `read_envelopes` and the charter's registry row
- **consumes-from** `PLAY-dOrderedCharter-21` — the practices-at-step block this unit wraps at level 0
- **consumes-from** `PLAY-dOrderedCharter-6` — the role's drive line inside the role section
- **consumes-from** `PLAY-dOrderedCharter-2` — the re-founded charter whose blocks the agent file carries
- **hands-off** `PLAY-dOrderedCharter-8` — the ranked envelope order in the handoff, where the card's slice takes its place

## 4. Design

### The task part a native agent receives

```text
<!-- gov:handoff role=gov-builder build=<slug> unit=<id> path=<prompt> role-sha=<h> task-sha=<h> -->

[<charter>#practices-at-build · Level 0 · <the charter row's direction>]
### Practices at build
…
[/<charter>#practices-at-build]
[<prompt path> · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
## Task
…
[/<prompt path>]
```

The prompt file holds the role section at level 5 between the two. The marker stays the first line
and `MARKER_RE` (`roles_lib.py:79`) is unchanged; the section hashes are derived over the enveloped
sections, so `check_handoff` re-derives them as it does.

### Inventory

Minted: the section doc form `<charter>#practices-at-<step>`; the level-6 task direction string; the
two `check` arms. No new file.

### Migration

None. A prompt record rendered before this unit carries no envelope at all; the level arms report it
`unranked` and pass it, because a landed prompt record is frozen and is not rewritten. A file holding
any envelope is graded whole.

### Rollout

Live at landing, in one commit with the agent files' re-render, so no spawn gets a task part without
charter blocks from an agent file that also lacks them.

### Files touched (estimate)

- `tools/roles/handoff.py`
- `tools/roles/render_agents.py`
- `tools/roles/roles_lib.py`
- `tools/roles/README.md`
- `.claude/agents/*.md` (the role render, re-rendered, never edited)
- `help/roles.md`

### Alternatives rejected

- **The charter blocks kept in the task and dropped from the agent file.** The agent file is loaded once
  per agent type and cached by the harness; the task is rendered per spawn.
- **One envelope around the whole prompt.** It ranks nothing: the point is that the role and the task
  each carry their own level.

## 5. Production-readiness checklist

- security: an envelope is rendered from the registry, never from task input; handed task text cannot
  open an envelope the check accepts, since its doc must match a block's.
- perf / scale: no measurable change.
- error / empty / loading states: an unreadable document registry refuses the render naming it.
- observability: `check` prints each envelope's level in order.
- risks: a native spawn whose agent file was not re-rendered carries no charter; Rollout puts both in
  one commit, and the `roles render wiring` leg reds a stale agent file.
- testing: §6 and the `New arm:` line of §7.
- migration: §4 Migration.
- user docs: `help/roles.md`'s "How a task reaches an agent" says the charter rides in the agent file
  and each block carries its level.

## 6. Acceptance criteria

- **AC1** — When `python tools/roles/render_agents.py --write` runs over a fixture tree, the first
  envelope in the body of the fixture's builder agent file is level 0, holding the cited rule lines,
  and its last closer is the agent file's own level-5 closer.
  Red when: the charter blocks follow the role text or sit outside an envelope.
- **AC2** — When `python tools/roles/handoff.py render --role builder --build <fixture> --stdout` runs,
  the envelopes it prints carry levels 0, 5 and 6 in that order, each opened and closed once.
  Red when: a block is unenveloped or out of level order.
- **AC3** — When the same render runs with `--part task`, `grep -c "^### Charter rules"` over its output
  prints 0, and the count of `- [verify] ` lines across the output and the fixture's builder agent file
  is 1.
  Red when: the charter is carried twice, or not at all.
- **AC4** — When `python tools/roles/handoff.py check <copy>` runs over a scratch copy of a rendered
  prompt with its task envelope moved above its role envelope, and over one with a closer deleted (each
  with the marker's hashes re-stamped), it exits 1 naming the envelope; over the unedited prompt it
  exits 0.
  Red when: either planted defect passes.

## 7. Gates

`roles render wiring` · `roles render selftest` · `check-wiring self-test` · `lexicon naming predicates`

New arm: tools/roles/render_agents.py · covers AC1 AC2 AC3 AC4 · the selftest's fixture renders an agent file and a handoff and plants the reordered and the unclosed envelope · none

## 8. Open questions

- **F1 — Which copy of the charter blocks survives.** Options: (a) the agent file's; (b) the task's;
  (c) both, deduplicated by the harness. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3; the agent
  file is the static level-5 load point R-G puts the role's instructions in, (b) re-renders the same
  bytes per spawn, and (c) is the duplication N1 measured. widens: none · relaxes: none
- **F2 — A stand-in's charter.** Options: (a) none in the prompt, the main loop holding the whole
  charter; (b) the role's blocks in the prompt. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3;
  the main loop loads `AGENTS.md` at level 0 every session, so (b) is the second copy this clause
  removes. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.

## 10. Reuse audit

The seams extended: `render_handoff` (`tools/roles/handoff.py:312-423`), whose charter blocks
(`:397-407`) and Role and Task sections (`:415-422`) this unit reorders and wraps; `render_agent_file`
(`tools/roles/render_agents.py:144-155`), which renders the same charter blocks through
`render_charter_blocks` (`tools/roles/roles_lib.py:284`); `check_handoff` (`handoff.py:426`), the one
verifier of a prompt file; and `PLAY-dOrderedCharter-3`'s inline `render_envelope` copy in
`roles_lib.py`. `python tools/codebase-map/reuse_lookup.py "assemble a role handoff from the charter
rules and the task"` ranked `parse_charter`, `render_charter_blocks`, `render_role` and `load_roles`
from `tools/roles/roles_lib.py`, which agree with the source; it did not rank `render_handoff`, which
the source shows is the assembler, so the map and the source disagree on the top seam.

Recall terms used: `python tools/memory-recall/query.py "how are role agents handed charter rule lines and how is the handoff ordered" --terms "handoff role rules charter blocks render_charter_blocks omitClaudeMd subagent prompt marker"`
