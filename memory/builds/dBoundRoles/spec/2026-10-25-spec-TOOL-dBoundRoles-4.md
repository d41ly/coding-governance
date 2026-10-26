# TOOL-dBoundRoles-4 — the prompt writer composing every role's task from the driver's details

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 17 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0169@60524f05 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-17 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-build-TOOL-dBoundRoles-4-deviation-41.md](../build/2026-10-25-build-TOOL-dBoundRoles-4-deviation-41.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 |

<!-- /gen:spec-records -->

## 1. Goal

The main session types most of every task it hands a role: 64.5% of a rendered task's bytes are typed
input, 71 of 126 direct spawns carried free-text prompts, and it wrote 74 task briefs in 60 days
(gap-roles-02, gap-roles-05, gap register `:154`, `:157`). The owner's RL-4 answer moves that work to a
prompt-writer role: "new prompt-writer roles receives only the details necessary to write a tight,
well-oriented prompt from the main session and passes it further along to its destination"
(`roles.md:324-329`). This unit builds that cycle on the existing renderer: the driver hands the
prompt writer its details and the destination's resolved work order, the prompt writer returns the
framing through its typed return, and the destination's work order carries that framing verbatim,
bound by hash, with the spawn guard refusing an unframed task while `prompts.author` is `prompt-writer`.

## 2. Scope (IN)

- **S1** — `input:work-order` joins `READ_KEYS` (`tools/roles/roles_lib.py:36-40`), the one `reads`
  vocabulary. `handoff.py render --for <role>` fills it: `render_handoff` (`tools/roles/handoff.py:312`)
  resolves the destination role's own blocks, every `reads` value it would render for that role, its
  `allowance` (TOOL-dBoundRoles-3) and its `return` template (TOOL-dBoundRoles-2), and hands them to
  the prompt writer as content under `### input:work-order`. Observed by AC1.
- **S2** — `gov-prompt-writer`'s fields, in the role file TOOL-dBoundRoles-1 creates: `reads` is
  `input:question, input:work-order`, the driver's details arriving as `input:question`; `writes` stays
  `none`; `return` is
  `outcome:framed|refused, job:text?, population:text?, added:text?, nostop:text?, why:text?`, one field
  per prose part of the frame TOOL-dBoundRoles-23 orders. Its body states the
  job: compose the destination's task from the details and the work order, pointing at handed facts
  rather than retyping them. Observed by AC1.
- **S3** — `handoff.py render --role <dest> … --framed-by <agent-id>`: the prompt writer's framing,
  read mechanically from that agent's transcript, never retyped by the driver. The transcript is found
  as `read_transcript` finds one (`handoff.py:825-828`), its agent type must be `gov-prompt-writer`, its
  final return must pass `validate_return` (TOOL-dBoundRoles-5) with `outcome` `framed` and carry `job`
  and `nostop`, and its first record's marker names the prompt writer's work order. The destination's
  `## Task` gains one block per field the return carries, `### framing:job`, `### framing:population`,
  `### framing:added` and `### framing:no-stop`, each holding its field verbatim, and
  `### framing:job` closes with the line `Framed by: <prompt path> task-sha=<12hex>`, all inside the
  bytes the task-sha covers. Any failed condition refuses the render by name. Observed by AC2.
- **S4** — Rule 6 under `prompts.author = prompt-writer` (TOOL-dBoundRoles-10's switch): an `Agent`
  spawn of any role but `gov-prompt-writer` is admitted only when its task carries exactly one
  `Framed by:` line, inside its one `### framing:job` block, and that line names a file under the
  build's `prompts/` folder holding exactly one `gov:handoff` marker with `role=gov-prompt-writer` and
  the named task-sha. Under
  `requesting-worker-rendered` the requirement is not applied. The prompt writer's own spawn is never
  framed: its task is the driver's details, rendered mechanically. The refusal names
  `prompts.author`, its value, and the route: render the prompt writer with `--for`, spawn it, render
  the destination with `--framed-by`. Observed by AC3.
- **S5** — `gov-session` and the `handoff` workflow's session-to-session route stay as they are: the
  session-handoff template's retirement is Runtime's (the brief's D3). Observed by AC4.
- **S6** — The user page `help/roles.md`, "How a task reaches an agent" (`:13-27`), gains the prompt
  writer's step, and the build Skill (`tools/roles/SKILL.template.md`) states the three-call route for a
  direct spawn. Observed by AC5.

## 3. Non-goals (OUT)

- The prompt writer's role file, its slot and its layer: TOOL-dBoundRoles-1's. This unit sets the
  fields S2 names and the body's job.
- Harness stage prompts. The harnesses compose their stages' prompts in their scripts; a prompt writer
  for a harness item is the executor's, dWellOiledMachine's, recorded as a departure (§8 F2).
- The frame's block order and the effort floor: TOOL-dBoundRoles-23's, which places this unit's four
  `### framing:` blocks in the frame's slots.
- The anchor check over the framing: TOOL-dBoundRoles-24's.
- The key `prompts.author` and its reader: TOOL-dBoundRoles-10's.
- `gov-session`'s retirement: dWellOiledMachine's (D3).

### Edges

- **consumes-from** `TOOL-dBoundRoles-1` — `gov-prompt-writer`, the role file whose fields S2 sets
- **consumes-from** `TOOL-dBoundRoles-3` — the work order's blocks, its `allowance` among them, which `--for` hands the prompt writer as content
- **consumes-from** `TOOL-dBoundRoles-5` — `validate_return`, which checks the prompt writer's return before its framing enters a work order
- **consumes-from** `TOOL-dBoundRoles-10` — `prompts.author` and `resolvePromptsAuthor`, the switch under which rule 6 applies S4
- **hands-off** `TOOL-dBoundRoles-23` — the `### framing:` blocks and the `Framed by:` line, which the default frame places in skeleton order
- **consumes-from** `TOOL-dBoundRoles-38` — the fence-aware `extractHandoffMarker`, through which S4's exactly-one-marker check reads the prompt writer's file, its `input:work-order` content now fenced (id 52 of the round-1 spec audit)
- **hands-off** `TOOL-dBoundRoles-43` — `gov-prompt-writer`, `--framed-by` and its transcript read, which unit 43 re-spells, guards against forged lines and lifts to a module-level resolver (ids 6, 15, 33, 40 and 55 of the round-1 spec audit)

## 4. Design

### The cycle

```
driver                         handoff.py render --role gov-prompt-writer --build S --unit U \
                                   --for gov-builder --input question="<the driver's details>"
                                 -> prompts/<…>-prompt-writer.md   (input:question, input:work-order)
driver                         Agent(subagent_type=gov-prompt-writer, prompt=<that task>)
gov-prompt-writer              returns {"outcome":"framed","job":"…","nostop":"…","answers":"<its prompt> task-sha=…"}
driver                         handoff.py render --role gov-builder --build S --unit U \
                                   --framed-by <the prompt writer's agent id>
                                 -> prompts/<…>-builder.md          (… ### framing:job, Framed by: …)
driver                         Agent(subagent_type=gov-builder, prompt=<that task>)
agent-cap rule 6               marker, bytes, task-sha (today) + framing (S4, prompts.author)
```

The driver types only its details, once, into `input:question`. The framing travels from the prompt
writer's return to the destination's task through the renderer reading the transcript, so no byte of
it passes through the driver's hands, which is RL-4's "keep as much of the noise out of its context
as possible". The destination's `### framing:` blocks are part of its `## Task` section, so its
task-sha binds the framing exactly as it binds every other block.

### The framing check at spawn

```
checkHandoffSpawn, after today's checks pass (agent-cap.js:2089-2148)
  resolvePromptsAuthor(root) == requesting-worker-rendered  -> admit
  subagent_type == gov-prompt-writer                        -> admit
  the task's "### framing:job" blocks != 1                  -> deny
  "Framed by: <path> task-sha=<12hex>" lines != 1, or outside that block -> deny
  <path> not under builds/<marker build>/prompts/, no file  -> deny
  that file's marker: not exactly one, role != gov-prompt-writer, task-sha differs -> deny
  otherwise                                                 -> admit
```

The marker of the named file is read with the hook's existing `extractHandoffMarker`
(`agent-cap.js:2048-2056`), so no second copy of the grammar enters the hook.

### Inventory

Minted: the `reads` key `input:work-order`; the render flags `--for` and `--framed-by`; the
four `### framing:` blocks and the `Framed by:` line; `checkFraming` in `agent-cap.js`; the fixture plants of
§7's arms (`for-builder`, `framed-valid`, `framed-invalid-return`, `framed-wrong-role`,
`spawn-unframed`, `spawn-framed`, `spawn-framed-by-researcher`, `spawn-prompt-writer`). Each name is
asked of `python tools/lexicon/lexicon.py --suggest <name>` at the pass.

### Migration

None stored. Prompts rendered before the landing carry no framing; rule 6 reads each spawn's own task,
so an old prompt file meets S4 only if it is spawned again under the default value.

### Rollout

Live at landing where the policy kit is installed and `prompts.author` is its default; an owner who
sets `requesting-worker-rendered` keeps today's rule 6.

### Files touched (estimate)

- `tools/roles/handoff.py`
- `tools/roles/roles_lib.py`
- `tools/roles/agents/gov-prompt-writer.agent.md` (rendered to `.claude/agents/gov-prompt-writer.md`)
- `tools/roles/README.md`
- `tools/roles/SKILL.template.md` (rendered to `.claude/skills/build/SKILL.md`)
- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `help/roles.md`

### Alternatives rejected

- **The prompt writer writes its framing as a record file.** It needs a write class for a role whose
  job writes nothing else, and a second path from the record to the task; the typed return already
  carries the text.
- **The driver pastes the framing into `--input`.** It retypes the prompt writer's output through the
  driver's context, the noise RL-4 removes.

## 5. Production-readiness checklist

- security — no new write path: the prompt writer writes `none`, the renderer writes the prompt file it
  writes today, and rule 6 reads one more file under the build's `prompts/` folder.
- perf / scale — one extra spawn per direct spawn under the default; the renderer reads one transcript.
- error / empty / loading states — a missing transcript, a wrong agent type, an invalid return or a
  `refused` outcome each refuse the render by name; the spawn refusal names the route.
- observability — the `Framed by:` line names the prompt writer's work order in every framed task.
- risks — a direct spawn costs a second agent; under `requesting-worker-rendered` the owner opts out.
- testing — the plants of §4's inventory through the render verb and `node -e` over rule 6; the arms in
  §7 are observed RED then GREEN by the main loop at the close.
- migration — none.
- user docs — `help/roles.md` and the build Skill (S6).

## 6. Acceptance criteria

- **AC1** — When `handoff.py render --role gov-prompt-writer --for gov-builder --input question=q`
  runs over a fixture build `x`, with `--unit X-1 --stdout`, its task carries
  `### input:question` and one `### input:work-order` block holding the builder's `return` template and
  its `allowance` block.
  Red when: `--for` is not read, so the prompt writer is handed references or nothing.
- **AC2** — When `handoff.py render --role gov-builder --build x --unit X-1 --framed-by <id>` reads a
  fixture prompt writer transcript whose final return is `outcome` `framed` with `job` and `nostop`,
  the task carries `### framing:job` and `### framing:no-stop` holding those texts byte for byte, and one
  `Framed by:` line naming the prompt writer's prompt path and task-sha; a transcript whose return lacks
  `nostop`, or whose agent type is `gov-researcher`, refuses naming the failed condition.
  Red when: the framing is taken from a return `validate_return` refuses, or from another role.
- **AC3** — When rule 6 reads a `gov-builder` spawn whose task has no `### framing:job`, with
  `prompts.author` unset, it returns a deny naming `prompts.author` and the three-call route; with a
  framing whose `Framed by:` names the fixture prompt writer's file, it admits; naming a file whose
  marker is `role=gov-researcher`, it denies; with `requesting-worker-rendered`, the unframed spawn
  admits; and a `gov-prompt-writer` spawn admits unframed.
  Red when: an unframed task is admitted under the default, or the prompt writer's own spawn is
  refused for lacking a framing.
- **AC4** — When `handoff.py render --role gov-session --build x --input question=q --stdout` runs, it
  renders as at base, with no `### framing:job` and no `--for`.
  Red when: the handoff workflow's session route is made to require the prompt writer.
- **AC5** — When `grep -n "prompt writer" help/roles.md tools/roles/SKILL.template.md` runs, each
  names the three-call route.
  Red when: the page still says the main session renders every task itself.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `check-wiring self-test` · `lexicon naming predicates` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/agent-cap.test.sh · covers AC3 · the `spawn-unframed` and `spawn-framed-by-researcher` plants, staged by a rule 6 whose framing check is cut · none
New arm: tools/roles/render_agents.py · covers AC1 AC2 · its self-test renders `--for` and `--framed-by` over the `for-builder`, `framed-valid` and `framed-invalid-return` plants, staged by a render that ignores `--framed-by` · none

## 8. Open questions

- **F1 — How does the prompt writer's output reach the destination's work order?** Options: (a)
  through its typed return, read from its transcript by `--framed-by`; (b) a record file the prompt
  writer writes; (c) the driver passes it as an `--input` value. (b) gives a role whose job writes
  nothing a write class; (c) puts the framing through the driver's context, the noise RL-4 removes.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most feature-rich option no veto refuses,
  tie-broken by reuse of the transcript reader and of `validate_return`. widens: none · relaxes: none
- **F2 — "Every role's task": do harness stage prompts pass through the prompt writer?** Options: (a)
  direct spawns only, harness stages left to the executor that renders their work orders; (b) every
  harness stage spawns a prompt writer first. (b) doubles every harness fan and puts a rendered work
  order where the harness scripts have none, which is dWellOiledMachine's executor. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3; it departs from "every role's task", recorded in
  `memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-4-deviation-41.md`.
  widens: none · relaxes: none
- **F3 — Is the prompt writer's own task framed?** Options: (a) no, it is the driver's details rendered
  mechanically; (b) yes, by another prompt writer. (b) regresses without end. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — The Carries pin of an amended clause: v2's baseline hash or the as-built view's?**
  `memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-4-deviation-41.md` amends
  `cl-dClosedLoop-0169`, so the as-built view hashes it `60524f05` where v2 hashes it `cdc1b7f9`.
  Options: (a) pin the view's hash, which the spec-tokens leg's carries join reads; (b) pin v2's
  baseline hash, which the packet's `carries.py --exit` reads. No pin satisfies both: (b) reds the merge
  bar's carries join as a stale pin, and (a) reds the packet instrument's Design-exit carries arm on
  this clause, the disagreement `PLAY-dClosedLoop-30` records. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 1, the spec fix brief's F3; the instrument's red on this clause is `PLAY-dClosedLoop-30`'s
  until its pin moves by the owner's `packet.py --repin`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 4, RL-4 and its settlement, the brief's
  shared interfaces I1, I12 and I16 and D3, scout B's row for cl-0169, TOOL-dBoundRoles-1's roster
  row, and `tools/roles/handoff.py` and `tools/hooks/agent-cap.js` at base `4ed9e567`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **consumes-from** and **hands-off** bullets mirroring the edges of TOOL-dBoundRoles-38, TOOL-dBoundRoles-43, promoted by the round-1 spec audit of the 26 unit specs; nothing else moved.

## 10. Reuse audit

The seams extended are `render_handoff` (`tools/roles/handoff.py:312-423`), its blocks list
(`:381-416`) and its transcript locator (`read_transcript`, `:825-828`); the `reads` vocabulary
`READ_KEYS` (`tools/roles/roles_lib.py:36-40`); and rule 6 (`checkHandoffSpawn`,
`tools/hooks/agent-cap.js:2089-2148`) with its marker reader `extractHandoffMarker` (`:2048-2056`).
`python tools/codebase-map/reuse_lookup.py "compose a role agent task prompt from the driver details"`
ranked `extract_prompt_marker`, `render_role`, `load_roles` and `renderPromptLine`, all handoff
plumbing; no role authors a task at base (scout B: "no seam fits for the role itself", 10 role files and
no prompt writer), so the role is new and every mechanism around it is an existing seam. Scout B's row
agreed with source; its blocks-list reference `:381-416` matches base.

Recall terms used: `python tools/memory-recall/query.py "who composes a role agent task prompt" --terms "prompt writer gov-prompt-writer task framing work order driver details handoff render gov-session"`
