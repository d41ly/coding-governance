# TOOL-dFurnishedOrders-2 — prompt-writer calls batched by `prompts.batch`: one call frames a step's tasks of one role, split per task at render

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 19 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0193@a564937b whole

**Carries:** node:policy-key.prompts.batch

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-c.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-16 |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dBoundRoles-4 puts a prompt writer before every direct role dispatch: one prompt-writer call per
destination task. The owner's FR-10 answered how many calls a step costs when it sends several workers
of one role at once, "five spec writers, say": "One per batch (Recommended)"
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md:261-263`), kept as
`prompts.batch`, `per-batch` or `per-task`, default `per-batch` (v2:1237). This unit lets one
prompt-writer call frame every task of one role at one step, gives its return a per-task key, and
splits that return per task when each destination's work order is rendered.

## 2. Scope (IN)

- **S1** — The batch render. `handoff.py render --role gov-prompt-writer --for <dest> --item <tag>`
  takes `--unit` repeated (`tools/roles/handoff.py:945` today takes one). With two or more units under
  `prompts.batch = per-batch` it renders one work order whose `## Task` holds one
  `### input:work-order:<unit id>` block per unit, in the order given, each holding what
  TOOL-dBoundRoles-4 S1 hands for that unit; its marker carries `unit=-` and its opening names the
  batch's units. Under `per-task` a second `--unit` refuses, naming `prompts.batch`, its value and the
  route, one `--for` render per unit. One `--unit` renders TOOL-dBoundRoles-4's single
  `### input:work-order` block under either value. A second `--unit` on any other render refuses.
  Observed by AC1 and AC2.
- **S2** — The batch's bound: one step's fan of one role. Every unit of a batch is the `<dest>` role's
  task at the one `--item`, and the render refuses a batch whose `<dest>` does not act at that item:
  `derive_role_matrix` (TOOL-dFurnishedOrders-9), read as `python tools/loop/loop_items.py matrix --role
  <dest> --json` through `roles_lib.resolve_kit_dir("loop", "loop_items.py", KIT_DIR)`, must list the
  item's tag under its step in `roles[<dest>]`; the refusal names the item and the role. It refuses and a batch of more
  a batch of more units than `read_agent_limit(root)` (TOOL-dBoundRoles-22 S5), naming
  `runtime.agents-in-flight`. A
  batch with no `--item` refuses, naming the flag. Observed by AC3.
- **S3** — The per-task key. `gov-prompt-writer`'s `return` (TOOL-dBoundRoles-4 S2) becomes
  `outcome:framed|refused, job:text?, population:text?, added:text?, nostop:text?, why:text?,
  tasks:list?`. Handed a batch, the prompt writer returns `tasks`, one object per unit,
  `{"unit", "job", "nostop"[, "population"][, "added"]}`, and leaves the top-level `job` and `nostop`
  empty; its role body gains one sentence saying so. Observed by AC4.
- **S4** — The split. `handoff.py render --role <dest> --unit <id> --framed-by <agent-id>`
  (TOOL-dBoundRoles-4 S3) reads the prompt writer's work order through its transcript as that unit
  does; when the work order is a batch, read by `read_batch_units(text)` off its
  `### input:work-order:<unit id>` heads, `check_batch_tasks(tasks, units)` refuses a return whose
  `tasks` omits a batch unit, names one outside the batch, names one twice, or carries an entry
  lacking `job` or `nostop`, naming each; a `--unit` outside the batch refuses. The destination's
  `### framing:` blocks hold its own entry's fields verbatim, and its `Framed by:` line names the batch's
  prompt path and task-sha, the line TOOL-dBoundRoles-4 S4's rule-6 check reads. Observed by AC4 and
  AC5.
- **S5** — The key read. `prompts.batch` is read once per render through
  `read_policy_setting("prompts.batch", root)` (TOOL-dBoundRoles-21 S1), its catalogue row
  `tools/policy/catalogue.toml:610-614`; a None answer reads the catalogue default `per-batch`. With no
  policy kit resolved the render reads `per-task`, TOOL-dBoundRoles-4's cycle, and prints one note line
  naming the absent kit. Observed by AC2.
- **S6** — The docs. The build Skill (`tools/roles/SKILL.template.md`) states the batch route in its
  three-call sequence, and `help/roles.md` "How a task reaches an agent" and `tools/roles/README.md`'s
  handoff section name `prompts.batch`, the batch work order and the split. Observed by AC6.

## 3. Non-goals (OUT)

- The prompt writer, its cycle, `--for`, `--framed-by` and rule 6's framing check:
  TOOL-dBoundRoles-4. Rule 6 is unchanged: every destination of a batch names one prompt-writer file
  holding one marker, which it already admits.
- Harness stages. A harness's stage prompts do not pass through the prompt writer
  (TOOL-dBoundRoles-4 §8 F2), so a stage row's `fan` (TOOL-dBoundRoles-22 S1) bounds nothing here; the
  executor that frames a harness stage is dWellOiledMachine's.
- The role-by-step matrix and its arms: TOOL-dFurnishedOrders-9. The agent limit's key and reader:
  TOOL-dGroundRules-10 and TOOL-dBoundRoles-22.
- Validating the return's shape: TOOL-dBoundRoles-5's `validate_return`; this unit adds the batch's
  join over `tasks`, which a shape check cannot see.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-9` — `derive_role_matrix`, through its `matrix` verb, whose `roles` map must hold the batch's item under the destination role; without it a batch of a role the step does not seat passes
- **consumes-from** external — TOOL-dBoundRoles-4 S1 to S4 (`--for`, `gov-prompt-writer`'s `return`, `--framed-by`, the `Framed by:` line), TOOL-dBoundRoles-5's `validate_return`, TOOL-dBoundRoles-17 S1's `--item`, TOOL-dBoundRoles-21 S1's `read_policy_setting`, TOOL-dBoundRoles-22 S5's `read_agent_limit`; each specced and unbuilt at base
- **hands-off** `TOOL-dFurnishedOrders-29` — the batch render, whose join moves into the return schema and whose key read, matrix read and refusals unit 29 S13, S16, S24 and S27 settle (ids 33, 36, 57, 12)

## 4. Design

### The cycle, batched

```
driver   handoff.py render --role gov-prompt-writer --build S --item item.design.unit-spec \
             --for gov-spec-writer --unit U-1 --unit U-2 --unit U-3 --input question="<details>"
           -> prompts/<…>-prompt-writer.md     ### input:question
                                               ### input:work-order:U-1 … :U-3
driver   Agent(subagent_type=gov-prompt-writer, prompt=<that task>)            one call
writer   {"outcome":"framed","tasks":[{"unit":"U-1","job":"…","nostop":"…"}, … U-3]}
driver   handoff.py render --role gov-spec-writer --build S --unit U-2 --framed-by <writer id>
           -> ### framing:job (U-2's entry) … Framed by: <the batch prompt> task-sha=<12hex>
driver   Agent(subagent_type=gov-spec-writer, prompt=<that task>)              once per unit
```

Under `per-batch` a step's three spec writers cost one prompt-writer call where TOOL-dBoundRoles-4
costs three. The driver still types its details once; the framing still never passes through it.

### The bound

A batch is the tasks one step sends at once to one role. The step is the work order's `--item`, and
the role must act there by `derive_role_matrix`, the matrix TOOL-dFurnishedOrders-9 derives from the
item declarations; the count is bounded by the agent limit, the one every stage's `cap` sits under,
because the batch's destinations are spawned together.

### The join

`check_batch_tasks(tasks, units)` classes each entry by its `unit` as TOOL-dDeclaredLoop-29 S6 classes
rows: a batch unit with no entry is `dropped`, an entry outside the batch `invented`, a unit with two
entries `doubled`; each refuses the split for every destination, so no task is framed from a return
another task's entry contradicts. The refusal names the class and the unit, and the route: render
the prompt writer again.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tasks` | return field of `gov-prompt-writer` | none |
| `### input:work-order:<unit id>` | block head | none |
| `read_batch_units`, `check_batch_tasks` | functions in `handoff.py` | `py.function`, OK each |

### Migration

None stored. A single-unit render is byte-identical to TOOL-dBoundRoles-4's; a prompt file rendered
before this unit is never a batch.

### Rollout

Live at landing at the default `per-batch` where the policy kit is installed; an owner who sets
`per-task` keeps one call per task.

### Files touched (estimate)

- `tools/roles/handoff.py`
- `tools/roles/agents/gov-prompt-writer.agent.md`, rendered to `.claude/agents/gov-prompt-writer.md`
- `tools/roles/README.md`
- `tools/roles/SKILL.template.md`, rendered to `.claude/skills/build/SKILL.md`
- `tools/roles/adopt-roles.test.sh`
- `help/roles.md`

### Alternatives rejected

- **One prompt-writer call per batch whose framing every destination shares verbatim.** Five spec
  writers of one step write five different units; one shared `job` frames none of them well, so the
  return carries one entry per task.
- **The batch bounded by a stage row's `fan`.** No direct route has a stage row: rows exist on
  `workflow`-driver entries only (TOOL-dBoundRoles-22 S1), and those harnesses bypass the prompt
  writer.

## 5. Production-readiness checklist

- security — no new write path; a batch work order hands the same content `--for` hands per unit,
  and the split takes each destination's framing only from its own entry.
- perf / scale — one prompt-writer spawn per batch in place of one per task; the batch work order
  grows by one `### input:work-order:` block per unit, bounded by the agent limit.
- error / empty / loading states — every refusal names its cause: the key under `per-task`, the
  matrix cell, the limit, a missing `--item`, or the join's class and unit.
- observability — the batch's opening line names its units; each destination's `Framed by:` names
  the one batch file.
- risks — a prompt writer framing several tasks at once writes a weaker frame per task; `per-task`
  restores one call per task.
- testing — AC1 to AC6 by fixtures of the renderer and a planted transcript; the arm of §7 at the
  close.
- migration — none.
- user docs — `help/roles.md` names the key and the batch route (S6).

## 6. Acceptance criteria

- **AC1** — When `python handoff.py render --role gov-prompt-writer --build x --item item.build.unit-pass
  --for gov-builder --unit X-1 --unit X-2 --input question=q --stdout` runs over a fixture build with
  `prompts.batch` unset, it prints one work order whose task holds `### input:work-order:X-1` and
  `### input:work-order:X-2`, and a marker carrying `unit=-`.
  Red when: the render writes one work order per unit, or one block for both.
- **AC2** — When AC1's render runs with `prompts.batch = "per-task"` in the fixture's policy file, it
  exits 1 naming `prompts.batch` and the one-render-per-unit route; with one `--unit` it renders a
  single `### input:work-order` block under both values; with no policy kit resolved it refuses a
  second `--unit` and prints the note naming the absent kit.
  Red when: `per-task` still batches, or the absent kit reads as `per-batch`.
- **AC3** — When AC1's render runs over a fixture loop kit whose `loop_items.py matrix --role gov-builder
  --json` lists `item.build.unit-pass` under no step, it exits 1 naming the item and `gov-builder`;
  with a stubbed `read_agent_limit` of 1, it exits 1 naming `runtime.agents-in-flight`; with no `--item`
  it exits 1 naming `--item`.
  Red when: a batch of a role the step does not seat, or larger than the limit, renders.
- **AC4** — When `python handoff.py render --role gov-builder --build x --unit X-2 --framed-by <id>`
  reads a planted prompt-writer transcript whose work order is AC1's and whose return carries `tasks`
  for `X-1` and `X-2`, the task's `### framing:job` holds `X-2`'s `job` byte for byte and not `X-1`'s;
  a return whose `tasks` lacks `X-2` refuses naming `dropped` and `X-2`, one naming `X-9` refuses naming
  `invented`, one naming `X-1` twice refuses naming `doubled`.
  Red when: the split takes a sibling's entry, or frames a task from a return that drops another.
- **AC5** — When AC4's render runs for `X-1` and for `X-2`, both tasks' `Framed by:` lines name the one
  batch prompt path and the same task-sha.
  Red when: a destination names a per-unit file that does not exist, so rule 6 refuses its spawn.
- **AC6** — When `grep -n 'prompts.batch' help/roles.md` runs at the root and
  `grep -n 'per-batch' SKILL.template.md` in `tools/roles/`, each names the key and the batch route.
  Red when: the driver meets the batch flag with no route on its page.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 AC4 · a batch render and its split over a planted transcript, staged by a render that ignores `prompts.batch` and by a split that takes the first entry · none

## 8. Open questions

- **F1 — What bounds a batch on the direct route?** The brief's J-list reads a batch as "one stage's
  fan of one role". Options: (a) the destination role's tasks at one item, the role checked against
  `derive_role_matrix` and the count against the agent limit; (b) a stage row's `fan`, named by a
  `--stage` flag; (c) no bound but the units the driver names. (b) names rows that exist only on
  harness entries, whose stages never pass through the prompt writer (TOOL-dBoundRoles-4 §8 F2), so it
  bounds nothing a batch can be; (c) lets one call frame tasks of several steps, which FR-10 does not
  ask. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor, its step
  FR-10's own word; the brief's "stage" is read as the item's step. widens: none · relaxes: none
- **F2 — One framing for the batch, or one per task?** Options: (a) a `tasks` list, one entry per
  unit; (b) the top-level fields shared by every destination; (c) both, a shared frame plus per-task
  deltas. (b) frames five different units with one job; (c) adds a merge rule for no stated need.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the brief's "the prompt writer's return gains a
  per-task key". widens: none · relaxes: none
- **F3 — With no policy kit, batch or not?** Options: (a) `per-task`, TOOL-dBoundRoles-4's cycle with
  a note; (b) the catalogue default `per-batch`, which only the absent kit can read. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3; the roles kit cannot read the catalogue without the policy kit,
  and the unbatched cycle is the parent's behaviour. widens: none · relaxes: none
- **F4 — The parents this unit calls.** TOOL-dBoundRoles-4, -5, -17, -21 and -22 are specced and
  unbuilt at base `2193e25d`, and `gov-prompt-writer.agent.md` does not exist yet; TOOL-dBoundRoles-4
  cites the transcript reader at `handoff.py:825-828`, which sits at `:835` at base. RESOLVED (agent,
  2026-10-26, delegated): the build run re-grounds on each section and stops the unit if one is still
  absent then, rung 1, the brief's rule for every deferred parent. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 2, FR-10, v2:1237 and :1559, the brief's
  J1 and J13, scout C's row for cl-0193, TOOL-dBoundRoles-4 and -22, and `tools/roles/handoff.py` at
  base `2193e25d`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullet mirroring TOOL-dFurnishedOrders-29, promoted from the round-1 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: TOOL-dBoundRoles-4's cycle on `render_handoff` (`tools/roles/handoff.py:312`), its
`--unit` flag (`:945`) and its transcript read (`read_transcript`, `:835`); the `return` template
grammar of TOOL-dBoundRoles-2 S4, whose `list` type carries the per-task key; TOOL-dDeclaredLoop-29
S6's dropped, invented and doubled classes, which the batch join reuses by name; and
`derive_role_matrix` for the step's role. `python tools/codebase-map/reuse_lookup.py "frame several
same-role tasks in one prompt writer call and split its return per task"` ranked stem matches
(`write`, `write_record`, `extract_prompt_marker`, `render_role`); no batching exists at base, and
nothing renders one work order for several units, so the two functions are new beside the parent's
cycle. Scout C cites `--unit` at `:945` and its check at `:990`, both matching source; TOOL-dBoundRoles-4
cites the transcript reader at `:825-828`, which F4 records at `:835`. The recall probe returned the
brief's and scout C's rows, FR-10 (flow-roles.md:274) and TOOL-dBoundRoles-4; none disagreed with source
beyond that line.

Recall terms used: `python tools/memory-recall/query.py "how many prompt writer calls does a batch of
same-role tasks cost" --terms "prompt writer batch per-batch per-task framing work order fan stage role
FR-10"`
