# TOOL-dRankedPlan-2 — the planner and triager role, the Plan workflow, and the plan's order as `plan.authority` says

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 5 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0370@23b0ac8f whole
**Carries:** node:policy-key.plan.authority
**Carries:** node:item.plan.input
**Carries:** node:item.plan.dedupe
**Carries:** node:item.plan.research
**Carries:** node:item.plan.place
**Carries:** node:item.plan.lease

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-fix-return.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-fix-return.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md) | research | TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-15 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |

<!-- /gen:spec-records -->

## 1. Goal

Plan has items and a planner slot on paper and nothing that runs them or bounds the planner: no
workflow row places the planner in the loop, the Plan command items are stand-ins, and nothing
decides who may reorder the plan (`gap-plan-01`, `gap-plan-02`). The owner's R2.4 answer makes the
order's authority a per-repo policy, `plan.authority`: `planner-drafts-owner-ratifies` (the default),
`planner-within-themes` and `owner-orders`, "flexible and configurable"
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md:110-121`;
v2:1283). This unit gives the planner, which is also the triager, its job and its limits, places the
Plan workflow in the loop definition, arms the Plan command items this build owns, and refuses an
agent's commit that changes the plan's order beyond what `plan.authority` grants, each value seen on
its planted case.

## 2. Scope (IN)

- **S1** — The planner's body. `tools/roles/agents/gov-planner.agent.md`, which TOOL-dBoundRoles-1 S2
  creates under its 3072-byte `BODY_CEILINGS` row, gains two paragraphs: the triager's job, judging
  what no declared rule decides at `plan.triage-judge` in the same slot (flow-steps.md:183-184), and
  the order's authority, one sentence per value of `plan.authority`, ending with the rule that a
  reorder the planner may not commit is proposed, never written. The render `.claude/agents/gov-planner.md`
  is its copy, by `render_agents.py --write`. Observed by AC1.
- **S2** — The Plan workflow in the loop: the row `[[workflow]] name = "plan" order = 0 step =
  "step.plan"` in `tools/loop/loop.toml`, written only where the definition at the build run's base
  lacks it, so `read_workflow_order` (TOOL-dDeclaredLoop-1 S3) and the roles check's join of every
  roles workflow to a loop row (-1 S4) both hold for the `plan` entry TOOL-dBoundRoles-1 S4 adds.
  Observed by AC2.
- **S3** — The order check, shared interface I11: `check_ratified_order(head, staged, authority,
  ratified)` in `tools/memory-tree/gen_build_index.py`, run as `gen_build_index.py --ratified-order
  --staged`, compares `derive_plan_order` (TOOL-dRankedPlan-1 S2), the order `PLAN.md` renders, over
  the build READMEs at HEAD with the same order over the staged READMEs, each parsed by
  `parse_front_matter`, under the value of `plan.authority` read once
  through the policy kit's `resolve` (I14), as `read_slot_mode` reads its cap. A row is ratified when
  TOOL-dRankedPlan-9's `read_plan_ratification` answers a witness for its build. The rule per value is
  §4 "### The authority"; a refusal names both builds, the value and the remedy. Exit 0 admitted, 1
  refused, 2 when git cannot say what is staged or the policy read refuses. Observed by AC3, AC4, AC5.
- **S4** — The commit point: `.githooks/pre-commit` gains a block beside the policy guard's, run when
  a staged `memory/builds/*/README.md` is among the changes: the owner's terminal proof, `[ -t 2 ]`,
  admits with one line, as the policy guard block admits; otherwise it runs S3 and refuses on exit 1
  or 2. A commit staging no build README spawns no Python. Observed by AC6.
- **S5** — The Plan command items armed, as TOOL-dDeclaredLoop-13 §4 "The stand-ins" says an owning
  build arms its item, by landing its witness reader and deleting its row together:
  `read_plan_item_witness(repo, slug, item)` in `tools/loop/plan_items.py`, run as `python
  tools/loop/plan_items.py witness <item> --build <slug>`, answers `item.plan.input`,
  `item.plan.research`, `item.plan.place` and `item.plan.lease` by §4 "### The witnesses", and the
  four `[[stand-in]]` rows naming those items are deleted from `tools/loop/loop.toml`.
  **Readers:** by name: READER NOT IN TREE — the loop kit is absent at base 0689e7fa; the rows'
  readers are TOOL-dDeclaredLoop-13's stand-in reader in its `loop_table.py`, specced and unbuilt ·
  by value: the `[[stand-in]]` list TOOL-dDeclaredLoop-13 S8 grades and TOOL-dDeclaredLoop-7's
  `derive_position`, which reads an item's witness; each reads the armed reader from this pass.
  Observed by AC7, AC9.
- **S6** — The dedupe check for `item.plan.dedupe`: `check_plan_dupes(repo, slug)` in
  `tools/loop/plan_items.py`, run as `python tools/loop/plan_items.py dedupe --build <slug>`, compares
  the content key the build's claim carries (TOOL-dPlacedRequest-21 S2) with every other claim's and
  with `derive_request_content_key` (TOOL-dPlacedRequest-19 S1) of every open ask's text, printing
  `dupes — none` or one `dupes — duplicate <build|ask> <id> · <key>` line per match. Overlap, which
  needs dIndexedDesign's design index, prints `overlap — unmeasured` (flow-steps.md:194-195). The
  dupes record and the item's stand-in row are TOOL-dRankedPlan-3's, which owns `record-kind.dupes`.
  Observed by AC8.
- **S7** — `help/plan.md` (TOOL-dRankedPlan-16 S9) gains a section, "The planner and the plan's
  order": the planner and triager, the Plan workflow, `plan.authority`'s three values with
  what each refuses, and the owner's terminal commit. Observed by AC10.
- **S8** — The plants of §6: `gen_build_index.py --ratified-order --plant <case>` and `python
  tools/loop/plan_items.py --fixture --plant <case>`, each building a scratch repository under a
  short `%TEMP%` path. Observed by AC3 to AC9.

## 3. Non-goals (OUT)

- The planner's file, its slot, the `plan` entry in `tools/roles/workflows.toml` and
  `WORKFLOW_NAMES`: TOOL-dBoundRoles-1 S2 and S4's. This unit writes the body's two paragraphs only.
- The Plan item rows themselves: TOOL-dDeclaredLoop-12 S2 declares all eleven, owner dRankedPlan.
  This unit arms five and adds no row.
- `plan.record`, `plan.triage-rule`, `plan.triage-judge` and `plan.exit`: TOOL-dRankedPlan-16, -3 and
  -10's nodes. The planner's body names the triager's job; the item is TOOL-dRankedPlan-3's.
- The dupes record kind, its writer and `item.plan.dedupe`'s stand-in row: TOOL-dRankedPlan-3's.
- Overlap detection against the design index: dIndexedDesign's (`cl-dClosedLoop-0384`).
- The priority grammar, the plan view and `plan.unplaced`: TOOL-dRankedPlan-1's. S3 reads its order.
- The ratification predicate: TOOL-dRankedPlan-9's. S3 asks it which rows are ratified.
- Holding a reorder at push time or across `--no-verify`: the hook stops forgetting, not evasion, as
  the policy guard's header says (`tools/policy/guard.py:18-23`).

### Edges

- **consumes-from** `TOOL-dRankedPlan-1` — `PLAN.md`, the plan view whose order, `derive_plan_order`, S3 compares and whose rows `item.plan.place`'s witness reads; without it there is no order to hold and no placement to witness
- **consumes-from** `TOOL-dRankedPlan-9` — `read_plan_ratification`, which tells S3 which rows the owner has ratified, so the planner adds between ratifications and never reorders a ratified row
- **hands-off** `TOOL-dRankedPlan-3` — `gov-planner`, the triager's slot whose body names the `plan.triage-judge` job that unit arms
- **hands-off** `TOOL-dRankedPlan-3` — `check_plan_dupes`, the dedupe finding that unit records as the dupes record, arming `item.plan.dedupe` with its witness reader and deleting its stand-in row
- **hands-off** `TOOL-dRankedPlan-15` — `gov-planner`, the slot that records a plan revision with `revise`, ratified as the plan is
- **hands-off** `TOOL-dRankedPlan-6` — `gov-planner`, the author whose plan record and revision Plan Review reviews
- **consumes-from** external — dBoundRoles' `gov-planner.agent.md` and `plan` workflow entry (TOOL-dBoundRoles-1 S2, S4); dDeclaredLoop's `loop.toml`, `read_workflow_order` and stand-in rows (TOOL-dDeclaredLoop-1, -12, -13); dPlacedRequest's claim, request record, content key and `--claims` lease rows (TOOL-dPlacedRequest-1, -19, -21)

## 4. Design

### Evidence

- `plan.authority` is catalogued with its three values, default `planner-drafts-owner-ratifies`,
  owner dRankedPlan (`tools/policy/catalogue.toml:895-899`); its presets set `planner-within-themes`,
  the default, `owner-orders` and `planner-within-themes` (v2:1600).
- The owner's terminal proof is the policy guard block's: `[ -t 2 ]` in a hook reads whether a person
  sits at a terminal, since git leaves a hook's stderr as the committer's (`.githooks/pre-commit:186-224`).
- The generator already imports a policy-kit module through `backlog.resolve_kit_dir`, asked once per
  run (`read_slot_mode`, `tools/memory-tree/gen_build_index.py:2283-2306`), and parses front matter in
  one place (`parse_front_matter`, :405).
- TOOL-dDeclaredLoop-12 S2 declares one `[[item]]` row per flow-steps item, the Plan program's eleven
  among them with owner dRankedPlan; TOOL-dDeclaredLoop-13 S8 lists each as a stand-in until this
  build arms it.
- TOOL-dDeclaredLoop-1 S2 ships ten `[[workflow]]` rows and S4 makes the roles check join every roles
  workflow to one; TOOL-dBoundRoles-1 S4 adds `plan` and `design` to `tools/roles/workflows.toml` and
  names no loop row, so the join reds on both at whichever landing comes second (scout B, "Missing
  loop.toml row").
- The roles render requires a `## Stage <n>` heading for every workflow of stage 1 or more
  (`tools/roles/adopt-roles.sh:46`), which an order of 0 does not.

### The authority

An agent's commit is one without the owner's terminal proof. Rows are the builds `PLAN.md` orders;
a row is ratified when its build's plan ratification holds (I6).

| `plan.authority` | An agent's commit may | It is refused when it |
|---|---|---|
| `planner-drafts-owner-ratifies` | add `priority:` to a build carrying none; change any line of an unratified row | changes the relative order of two ratified rows |
| `planner-within-themes` | change `parents:`, reordering rows within one `priority:` value | adds, changes or removes a `priority:` line, or moves a row across another priority's rows |
| `owner-orders` | change `parents:` where no row moves | adds, changes or removes a `priority:` line, or changes the relative order of any two rows |

The owner's terminal commit is admitted under every value, and is how a drafted reorder of ratified
rows becomes binding. The refusal reads `plan order — refused · <a> before <b> at HEAD, after it
staged · <value>: <remedy>`, the remedy `the planner proposes, the owner commits from a terminal`.
The themes of `planner-within-themes` are the owner's `priority:` values: no theme grammar exists in
any record, and the priority band is the unit the owner sets (§8 F8).

### The witnesses

| Item | Witnessed when | Evidence printed |
|---|---|---|
| `item.plan.input` | the build's claim `refs/gov/claims/<slug>` resolves and carries a `content-key` | the key, and the request record `refs/gov/requests/<key>`'s sha where one exists |
| `item.plan.research` | a record of kind `research` under the build's folder serves one of its ids, read by `read_bindings` (`tools/memory-tree/tree_lib.py:471`) | its path |
| `item.plan.place` | `PLAN.md` lists the build | `placed · priority <n>`, or `unplaced`, the outcome `plan.unplaced` routes |
| `item.plan.lease` | `unattended.sh --claims` prints a live row for the build held by this node | the row; `unarmed` while it prints `claims: off` (`tools/unattended/unattended.sh:2082`) |

Each answer is one line, `<item> — witnessed · <evidence>` or `<item> — unwitnessed · <why>`, exit 0
on either and 2 on an item this unit does not arm, naming it.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_ratified_order` | function, `tools/memory-tree/gen_build_index.py` | `py.function`, asked at the pass |
| `--ratified-order` | flag of `gen_build_index.py`, with `--staged` and `--plant` | none |
| `read_plan_item_witness`, `check_plan_dupes` | functions, `tools/loop/plan_items.py` | `py.function`, asked at the pass |
| `witness`, `dedupe` | verbs of `plan_items.py` | none |
| the `plan` `[[workflow]]` row | loop definition row | none |
| `drafts-reorder-ratified`, `drafts-add-row`, `drafts-reorder-drafted`, `themes-priority`, `themes-parents`, `orders-priority`, `orders-parents-still` | `--ratified-order` plants | none |
| `input`, `research`, `place-placed`, `place-unplaced`, `lease-off`, `lease-live`, `dupes-ask`, `dupes-none` | `plan_items.py` plants | none |

### Migration

None. No README declares `priority:` at base (scout A), so the first commit that adds one is an
addition under every value but `planner-within-themes` and `owner-orders`, where it is the owner's.

### Rollout

Live at landing for gov's own hook. An adopter's hook gains the block with the hook it installs; a
repository whose plan view lists no row admits every commit.

### Files touched (estimate)

- `tools/roles/agents/gov-planner.agent.md`: S1's two paragraphs
- `.claude/agents/gov-planner.md`: its render, by `render_agents.py --write`
- `tools/loop/loop.toml`: the `plan` workflow row where absent; four stand-in rows deleted
- `tools/loop/plan_items.py` (new): S5, S6 and their plants
- `tools/memory-tree/gen_build_index.py`: S3 and its plants
- `.githooks/pre-commit`: S4's block
- `.githooks/pre-commit.test.sh`: the arm §7 declares
- `help/plan.md`: S7's section

### Alternatives rejected

- **The planner's limits as prose only.** A body sentence binds nothing at the commit an agent makes;
  the check is what makes `owner-orders` mean agents only propose.
- **A second reader of the plan order in the loop kit.** The order lives in the generator beside
  `PLAN.md`; a copy in `tools/loop/` would drift from the view the owner reads.
- **A reorder admitted by any plan ratification in the session.** A ratification is per build; a
  reorder spans two, and no record binds a ratification to the rows it fixed beyond the build's own.

## 5. Production-readiness checklist

- security — S4 narrows agent writes and widens none; the policy value is read from the guarded
  policy file at the landed revision, so an agent cannot loosen it in the same commit. The block stops
  forgetting, not evasion: `--no-verify`, another clone and a rebase pass it, as they pass the policy
  guard.
- perf / scale — the check runs only when a build README is staged: two order computations and one
  predicate call per ratified row.
- error / empty / loading states — a refused policy read or an unreadable index exits 2 and the
  commit is refused, never admitted silently; a plan view with no rows admits.
- observability — every refusal names both builds and the value; every witness answer names its
  evidence or its reason.
- risks — under `planner-within-themes` and `owner-orders` an agent cannot place a new build, so the
  planner's draft waits for the owner; that is the values' stated intent.
- testing — the plants of §6, and the hook arm; the terminal-proof admission is not fixture-observable,
  as the policy guard's is not, and is the same `[ -t 2 ]` line.
- migration — none.
- user docs — `help/plan.md`, S7.

## 6. Acceptance criteria

- **AC1** — When `grep -oE "planner-drafts-owner-ratifies|planner-within-themes|owner-orders|plan.triage-judge"`
  runs over the rendered `gov-planner.md` and the output is sorted unique, it prints the four names,
  and `python tools/roles/check_roles.py` exits 0 with the body under its ceiling.
  Red when: the body omits a value or the triager's job, or grows past `BODY_CEILINGS`.
- **AC2** — When `python loop_lib.py --check` and `python tools/roles/check_roles.py` run at the pass
  tip, both exit 0 and `read_workflow_order` lists `plan` with order 0 and step `step.plan`.
  Red when: the roles kit lists a `plan` workflow the loop definition holds no row for.
- **AC3** — When `python3 tools/memory-tree/gen_build_index.py --ratified-order --plant <case>` runs
  under `planner-drafts-owner-ratifies` with the stub predicate ratifying `dA` and `dB`: the plant
  `drafts-reorder-ratified`, an agent commit putting `dB` before `dA`, exits 1 naming both builds and
  `planner-drafts-owner-ratifies`; `drafts-add-row` and `drafts-reorder-drafted` exit 0.
  Red when: the planner reorders ratified rows between ratifications, or cannot add a row.
- **AC4** — When the plants run under `planner-within-themes`: `themes-priority`, an agent commit
  changing one `priority:` value, exits 1 naming `planner-within-themes`; `themes-parents`, a
  `parents:` change reordering two rows of one priority, exits 0.
  Red when: the planner changes a priority the owner set, or cannot order within one.
- **AC5** — When the plants run under `owner-orders`: `orders-priority`, an agent commit adding a
  `priority:` line, exits 1 naming `owner-orders`; `orders-parents-still`, a `parents:` change that
  moves no row, exits 0.
  Red when: an agent writes the plan's order under `owner-orders`.
- **AC6** — In a scratch clone of the pass tip with `git config core.hooksPath .githooks`, whose
  `.governance/policy.toml` gains a `[plan]` table setting `authority = "owner-orders"`, committed with
  `--no-verify` as the fixture's setup: when `git commit -m probe > out.txt 2>&1` runs with one build
  README staged that adds a `priority: 1` line, stderr a file and so not a terminal, it exits non-zero,
  `grep "plan order — refused" out.txt` prints the S3 line naming that build and `owner-orders`, and
  the README is not committed; when the same commit runs with only a non-README file staged,
  `grep -c "plan order" out.txt` prints 0.
  Red when: an agent's reordering commit lands, or an unrelated commit pays for the check.
- **AC7** — When `python plan_items.py --fixture --plant <case>` runs: `input` prints
  `item.plan.input — witnessed` with the claim's key and the request record's sha; `research` prints
  its record's path; `place-placed` prints `placed · priority 1` and `place-unplaced` prints
  `unplaced`; `lease-live` prints the held row and `lease-off` prints `unarmed`; each with its source
  removed prints `unwitnessed` and its reason.
  Red when: an item reads witnessed with no claim, record, plan-view row or lease behind it.
- **AC8** — When the plant `dupes-ask` holds an open ask whose text keys equal to the build's claim,
  `python plan_items.py dedupe --build tFix` prints `dupes — duplicate ask <id>` and `overlap —
  unmeasured`; the plant `dupes-none` prints `dupes — none`.
  Red when: an equal key is missed, or a distinct one is reported.
- **AC9** — When `grep -cE 'item = "item\.plan\.(input|research|place|lease)"'` runs over the pass
  tip's `loop.toml`, it prints 0.
  Red when: a stand-in row survives beside its armed reader.
- **AC10** — When `grep -n "plan.authority" plan.md` runs over the help page, it finds S7's section
  naming the three values and the owner's terminal commit.
  Red when: the page does not describe the planner's authority.

## 7. Gates

`check-wiring self-test` · `lexicon naming predicates` · `policy fixtures` · `tier2-review self-test` · `build-index selftest` · `branch-guard self-test` · `roles catalogue` · `roles render wiring` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC3 AC4 AC5 · the seven `--ratified-order` plants in `--selftest`, the failing case `drafts-reorder-ratified` admitted · none

New arm: .githooks/pre-commit.test.sh · covers AC6 · the plan-order block, the failing case an agent's reordering commit admitted · none

New arm: tools/loop/plan_items.py · covers AC7 AC8 · the `--fixture` plants, the failing case `input` witnessed with no claim · none

## 8. Open questions

- **F1 — Where is "the planner adds but never reorders between ratifications" enforced?** Options:
  (a) an arm on dDeclaredLoop's guard over `guarded-paths.txt`, which lists exact owner-only paths and
  is itself an owner-guarded file, so every build README would become owner-only; (b) a staged check
  beside the plan order in the generator, run by a hook block shaped as the policy guard's; (c) the
  generator's `--check` against the order at the last ratification, which cannot tell the owner's
  commit from an agent's, so `owner-orders` has no observable case. (a) widens a guarded surface
  past the key, (c) fails AC5. RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the most
  feature-rich survivor, reusing the policy guard block's terminal proof. widens: none · relaxes: none
- **F2 — Who writes the `plan` workflow's loop row, which no parent owes?** Options: (a) this unit
  writes it where absent, and an ask asks dBoundRoles to write it with its S4; (b) the ask alone; (c)
  this unit alone. (b) leaves this build's Plan workflow unplaced if the ask is not taken; (c) leaves
  dBoundRoles' landing red on the join. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. The ask,
  for the main loop to file once in dBoundRoles' `BACKLOG.md`: target dBoundRoles, TOOL-dBoundRoles-1
  S4 writes a `[[workflow]]` row in `tools/loop/loop.toml` for each entry it adds, `plan` with step
  `step.plan` and `design` with step `step.design`. Accept: the roles check's join of every roles
  workflow to a loop row exits 0 at dBoundRoles' landing tip, seen red on a fixture whose
  `workflows.toml` lists `plan` with no loop row. widens: none · relaxes: none
- **F3 — Are the planner and the triager one slot or two?** RESOLVED (agent, 2026-10-26, delegated):
  one, `gov-planner`, rung 1: flow-steps.md:183-184 names the actor of `plan.triage-judge` and
  `plan.record` `planner`. widens: none · relaxes: none
- **F4 — What `order` does the `plan` workflow take?** Options: (a) 0, with step `step.plan`; (b) an
  integer between `orient` and `reuse`, which renumbers every later stage and owes a new `## Stage`
  heading in the roles Skill. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, tie-broken by
  fewer open questions: the step field places it, as `research` is placed by its items. widens: none ·
  relaxes: none
- **F5 — Which rows are "ratified" between ratifications?** Options: (a) the rows whose build's plan
  ratification holds, read through TOOL-dRankedPlan-9's predicate; (b) every row at HEAD, so only the
  owner's terminal commit reorders. (b) refuses the planner's own drafted order before the owner has
  seen it, against "drafted by the planner and binding once the owner ratifies it". RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F6 — Are the Plan item rows registered by this unit, as I10 proposes?** RESOLVED (agent,
  2026-10-26, delegated): no, rung 1: TOOL-dDeclaredLoop-12 S2 declares all eleven Plan rows and
  TOOL-dDeclaredLoop-13 §4 has an owning build arm each by its witness reader and its stand-in row, so
  `loop_items.py new` would mint a second row. widens: none · relaxes: none
- **F7 — Who arms `item.plan.dedupe`, whose witness is the dupes record TOOL-dRankedPlan-3 owns at a
  later order?** Options: (a) the check here, the record, its witness reader and the stand-in row
  there; (b) all of it there, leaving this owned node unbuilt here; (c) all of it here, writing a
  record kind before its owner registers it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  build order kept. widens: none · relaxes: none
- **F8 — What are the "themes" of `planner-within-themes`?** Options: (a) the owner's `priority:`
  values; (b) a new theme key in front matter. (b) adds a key no clause names. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3: R2.4 offers "the owner sets themes and priorities", and the
  priority band is the one the plan view orders by. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 2, R2.4, v2:1283 and :1600, flow-steps
  .md:164-206, the walkthrough's P1 to P4, TOOL-dBoundRoles-1, TOOL-dDeclaredLoop-1, -12 and -13,
  TOOL-dPlacedRequest-1, -19 and -21 at base, and scout B's row -2.

## 10. Reuse audit

The seams: the policy guard block's terminal proof (`.githooks/pre-commit:186-224`), which S4 copies
in shape and does not widen; the generator's front-matter parser and its policy-kit import
(`parse_front_matter` :405, `read_slot_mode` :2283), beside which S3 sits so the order is computed
once; TOOL-dBoundRoles-1's planner file and entry; TOOL-dDeclaredLoop-12's rows and -13's stand-in
list; dPlacedRequest's claim, request record and content key; `read_bindings`; and `unattended.sh
--claims`. `python tools/codebase-map/reuse_lookup.py "refuse an agent commit that reorders the
ratified build priority order unless the owner commits from a terminal"` ranked name stems (`build`,
`build_commit`, `CensusRefused`, `owners_of`); none judges an order, so no existing seam fits the
order rule itself and S3 is new beside the order TOOL-dRankedPlan-1 adds. The recall query returned
the packet's clause and the scout rows, which agree with source. Where records and source disagree:
the brief's I10 has `loop_items.py new` register the Plan rows, which TOOL-dDeclaredLoop-12 S2 already
declares (F6); TOOL-dBoundRoles-1 S4 cites `check_roles.py:90` for `WORKFLOW_NAMES`, at :92 at base.

Recall terms used: `python tools/memory-recall/query.py "who may reorder the plan between ratifications and how is the planner's authority enforced" --terms "plan.authority planner-drafts-owner-ratifies planner-within-themes owner-orders priority parents ratify reorder gov-planner workflow"`
