# TOOL-dTendedCadence-10 — the maintainer's definition, registered through the observability layer's contract

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 1 · advances TOOL-dTendedCadence-19

**Carries:** cl-dClosedLoop-0451@8cb0a7a7 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-build-TOOL-dTendedCadence-1-reuse-scout-a.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-reuse-scout-a.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-6 TOOL-dTendedCadence-8 |
| [2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |

<!-- /gen:spec-records -->

## 1. Goal

Define the maintainer, the observability expansion's one role, whose item role is Maintain's filings
(layer-roles `[roster]`, `layer-roles.md:481`), as a role file of the roles kit, and make the layer
contract refuse a registered expansion role that no role file defines. TOOL-dBoundRoles-1 S5 registers
`gov-maintainer` on `layer.observability` and says no role file defines it (its §3 hands the
definition to this build, v2:419-421 and v2:1970); today a registration with no definition passes,
because no arm of `check_layer_roles` reads whether the slot exists.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `f4597719`: TOOL-dBoundRoles-1 (S1 the
`layer` and `acts-as` fields, S5 the `roles` list on `layer.observability` and `check_layer_roles` in
`tools/playbook/check_layers.py`, S6 the index carrying both fields), TOOL-dBoundRoles-2 (the `never`
and `return` fields), TOOL-dBoundRoles-15 (the ceiling as the `budget` field) and TOOL-dBoundRoles-20
(`WORKFLOW_NAMES` read from the workflow registry). dBoundRoles is an ancestor of this build, so each
lands first; the build run re-grounds on each called section and stops the unit when one is absent.

- **S1** — The role file `tools/roles/agents/gov-maintainer.agent.md`, per §4 "The role": slot
  `gov-maintainer` (TOOL-dBoundRoles-1 F3's name), `layer: layer.observability`, `acts-as: item`,
  `workflow: maintain`, `writes: none`, read-only tools, `mandatory: no — …`, its `never` and typed
  `return`, and a body stating the job and nothing a later unit decides. Observed by AC1 and AC3.
- **S2** — Its ceiling, priced at 2048 bytes of body: the `budget` field where TOOL-dBoundRoles-15
  has landed, else a `BODY_CEILINGS` row in `tools/roles/check_roles.py` (`:87-90` at base), per §8
  F6. Observed by AC1.
- **S3** — Its house overlay `tools/roles/house/gov-maintainer.md`, seeded empty, and its path added
  to the seed list of `tools/roles/kit.toml` (`:36-39` at base), so an adopter owns it after the
  first install as it owns every other overlay. Observed by AC1.
- **S4** — The workflow entry `maintain` in `tools/roles/workflows.toml`, per §4 "The workflow",
  `roles = ["gov-maintainer"]`, and its name admitted where `WORKFLOW_NAMES` (`check_roles.py:92-93`)
  still closes the set at the build run's base (§8 F6), so R6, R7 and R8 hold for the new slot
  (`check_roles.py:277`, `:325`, `:331-333`, `:349`). Observed by AC1.
- **S5** — The definition arm of `check_layer_roles`: an expansion row that a kit descriptor's `layer`
  key joins (PLAY-dOrderedCharter-16 S2), so the expansion is installed in this tree, and whose
  `roles` list names a slot `.claude/roles.json` does not hold, is a red naming the row and the slot;
  a slot registered by a row no descriptor joins prints one `note` line and owes nothing, per §4
  "The arm". Observed by AC2.
- **S6** — The renders: `.claude/agents/gov-maintainer.md` and `.claude/roles.json` by
  `render_agents.py --write`, the catalogue region of `tools/roles/README.md` by `check_roles.py
  --write`, and the roster region of `AGENTS.md` by the playbook render, which prints `handoff.py
  roster` (`tools/playbook/render_playbook.py:470-497`). Observed by AC3 and AC4.
- **S7** — The page `help/roles.md` names the maintainer and the `maintain` workflow in its opening
  list of workflows, as running only where observability is installed. Observed by AC5.

## 3. Non-goals (OUT)

- The registration itself, `roles = ["gov-maintainer"]` on `layer.observability`: TOOL-dBoundRoles-1
  S5's, landed before this unit. This unit defines the slot that row names.
- The lenses `maintenance-run` and `loop`: dCalibratedLens owns the `lens` namespace
  (TOOL-dBoundRoles-1 §3); no harness carries them and this unit defines neither.
- The deployer's definition: dShippedRelease's (v2:419), which is not an ancestor of this build, so
  S5's arm owes it nothing while no kit descriptor joins `layer.distribution` or `layer.integrations`.
- Which Maintain item spawns the maintainer and what its filings carry: the Maintain program
  (`tools/drift-audit/maintain.py`, TOOL-dTendedCadence-1), the filing route (TOOL-dTendedCadence-15)
  and the recurring security review (TOOL-dTendedCadence-13, whose findings' filing is the role's item
  role) hand it its input. This unit reads nothing of theirs: the role is complete without a caller. Running a
  `Workflow` harness is not in the definition: TOOL-dTendedCadence-13 S4's cadence program launches
  `tier2-review.js` as a Workflow act through `launch_act`, never through this role, whose read-only
  four tools grant no `Workflow` (§8 F4).
- A spawn guard or write arm for the role: `writes: none` is already enforced by the role arm of
  `scratch-guard.js` reading `.claude/roles.json`, and the house `[gates]` table grants it no leg.

### Edges

- **hands-off** `TOOL-dTendedCadence-13` — `gov-maintainer`, the item role the recurring security review's filing is (I15)
- **consumes-from** external — TOOL-dBoundRoles-1 S1, S5 and S6 (the two fields, the registration
  row, `check_layer_roles` and the index), TOOL-dBoundRoles-2 (`never`, `return`),
  TOOL-dBoundRoles-15 (`budget`) and TOOL-dBoundRoles-20 (the workflow registry), all DEFERRED at base
  and all of an ancestor build

## 4. Design

### The role

```markdown
---
name: gov-maintainer
description: Composes the text of one filing a Maintain run makes from the reading it is handed.
tools: Read, Grep, Glob, Bash
model: inherit
workflow: maintain
layer: layer.observability
acts-as: item
reads: input:prompt
writes: none
rules: verify, derive, security
mandatory: no — when a Maintain run renders a filing
output: the filing's text, to the Maintain program
---
```

`never` and `return` are written in the grammar TOOL-dBoundRoles-2 S2 and S4 land, with this
content: it never writes a file in the repository (enforcer: the role arm of `scratch-guard.js`), never
runs a gate, a suite or the bar (enforcer: the house `[gates]` table, which names no leg for it), and
never files anything itself (enforcer: the Maintain program's own command, the one writer of a
filing). Its `return` holds the required closed `outcome` (`composed` or `refused`), the problem text
and the acceptance text, each a string field.

The body states the job in four parts. It is handed one reading as content: the reading's name, the
sha it was read at, its value and denominator, its offender key, its pin, its band where the bands
apply, its owner layer as the program derived it, its fix route, and, in the diagnose band, the
read-only probe's record. It writes the problem statement, naming the reading and the offender key
verbatim, and the acceptance, the reading back under its pin for that key. It changes no value it was
handed and adds no claim the reading does not carry. Done means one problem and one acceptance, or a
refusal naming the field that was missing. `input:prompt` is the existing read key
(`tools/roles/roles_lib.py:40`), so no read key is minted.

`writes: none` is the narrowest class: the maintainer composes text and the Maintain program files it
(the charter's [security] rule, automation's narrowest grant).

### The workflow

```toml
[[workflow]]
name = "maintain"
stage = 0
driver = "program"
harness = "python {prefix}/drift-audit/maintain.py"
roles = ["gov-maintainer"]
enforced-by = "none — a filing is the Maintain program's command, and the role only composes its text"
trigger = "on each Maintain run, once per filing it renders"
```

A `program` driver's harness is never resolved as a script path (R9 grades `workflow`-driver
harnesses only, `check_roles.py:301-308`), so the entry is legal before TOOL-dTendedCadence-1 writes
that program. `stage = 0` marks an any-time workflow, as `research`, `handoff` and `bookkeeping` are.
The house effort table names no level for the slot, so it runs at the file's `default`
(`tools/roles/house/policy.toml:5-6`).

### The arm

`check_layer_roles` (TOOL-dBoundRoles-1 §4 "The registration") gains one red and one note:

```
for each [[layer]] row of kind expansion carrying a roles list:
    installed = some kit descriptor's `layer` key names the row (PLAY-dOrderedCharter-16 S2)
    for each slot of the row's roles:
        slot in .claude/roles.json         -> nothing
        installed and slot absent          -> red  "<row> registers <slot>, and no role file defines it"
        not installed and slot absent      -> note "<row> registers <slot>, not installed here: no role file owed"
```

At the build run's base, `layer.observability` is joined by the descriptors of `tools/runlog/`,
`tools/drift-audit/` and `tools/branch-reconcile/` (PLAY-dOrderedCharter-16 §4, layer-instruction's
`[layers]` table), so `gov-maintainer` is owed and defined; `layer.distribution`'s home `govkit` has
no descriptor (`tools/govkit/kit.toml` does not exist) and no descriptor joins `layer.integrations`,
so `gov-deployer` prints its note. The arm reads the index as JSON data, as the rest of the function
does, so the playbook kit still imports no roles module (TOOL-dBoundRoles-1 F6).

### Inventory

Minted: the slot file `gov-maintainer.agent.md` and its overlay; the workflow name `maintain`; one red
and one note text in `check_layer_roles`. No function, module or read key is minted, so the lexicon's
cells (`.lexicon.conf` `CELLS`, the code identifiers only) grade nothing new.

### Rollout

Live at landing on `roles catalogue` and `roles render wiring`; the agent type reaches a session at its
next start. An adopter receives the role file as engine and the overlay as a seed on its next update.

### Files touched (estimate)

- `tools/roles/agents/gov-maintainer.agent.md` (new)
- `tools/roles/house/gov-maintainer.md` (new, empty)
- `tools/roles/kit.toml` (the seed list)
- `tools/roles/check_roles.py` (a `BODY_CEILINGS` row and a `WORKFLOW_NAMES` member, only where §8 F6
  finds either still in the file)
- `tools/roles/workflows.toml` (the `maintain` entry; its header comment names no count of entries)
- `tools/roles/README.md` (its catalogue region, rendered by `check_roles.py --write`)
- `tools/playbook/check_layers.py` (S5's arm)
- `help/roles.md`
- `.claude/agents/gov-maintainer.md` and `.claude/roles.json` (rendered by `render_agents.py --write`)
- `AGENTS.md` (its roster region, rendered by the playbook render from
  `coding-governance-agents.template.md`, which this unit does not edit)

## 5. Production-readiness checklist

- security — the role writes nothing and runs no gate; its tools are the read-only four the reuse
  scout carries.
- perf / scale — one role file, one entry, one arm linear in registered slots.
- error / empty / loading states — with no index the arm's role half prints `unarmed`, as
  TOOL-dBoundRoles-1 §4 states; a register with no expansion row prints nothing for this arm.
- observability — the arm's note names every registered slot it owes nothing for, so an uninstalled
  expansion is visible rather than silent.
- risks — the charter's roster grows by one line, under `ROSTER_LINE_MAX` (`tools/roles/handoff.py:113`);
  an adopter without observability still receives the role file, which no item of theirs spawns.
- testing — each criterion is a probe over the tree or a scratch worktree; the new arm is observed
  RED then GREEN by the main loop at the close.
- migration — none: an adopter's overlay is seeded once; no existing role or key moves.
- user docs — `help/roles.md` (S7).

## 6. Acceptance criteria

- **AC1** — When `python check_roles.py` runs in `tools/roles/` over the tree, it exits 0, its summary
  counts the role at `layer.observability`, and `git grep -n "gov-maintainer" -- tools/roles/workflows.toml
  tools/roles/kit.toml` prints the `maintain` entry's roles line and the seed list's overlay path.
  Red when: the slot has no ceiling (R5), no `maintain` entry lists it (R7, R8), or the entry's name is
  refused as unknown (R6).
- **AC2** — When `python check_layers.py` runs in `tools/playbook/` in a scratch worktree of the tree
  whose `gov-maintainer.agent.md` is deleted and whose index is re-rendered by `render_agents.py --write`,
  it exits 1 with one line naming `layer.observability` and `gov-maintainer`; with the file restored and
  the index re-rendered it exits 0 and prints the note for `gov-deployer`.
  Red when: the arm reads no index, so the deleted file passes, or reds every registered slot, so
  `gov-deployer` reds the restored tree.
  fixture: a `git worktree add` at a short path under `%TEMP%`; `check_layers.py` is
  PLAY-dOrderedCharter-16's and TOOL-dBoundRoles-1's, absent at `f4597719`.
- **AC3** — When `python render_agents.py --write` and then `python render_agents.py --check` run in
  `tools/roles/`, the second exits 0, an agent file `gov-maintainer.md` exists under `.claude/agents/`, and
  `.claude/roles.json` holds `gov-maintainer` with `layer` `layer.observability`, `acts-as` `item` and `writes` `none`.
  Red when: the role carries `agent: false` or a key the renderer refuses, so no agent type is written.
- **AC4** — When `python handoff.py roster` runs in `tools/roles/`, it prints one line naming
  `gov-maintainer`, under 200 bytes, and `git grep -n "gov-maintainer" -- AGENTS.md` prints that line in
  the roster region after the playbook render.
  Red when: the role lacks `description`, `mandatory` or `output`, so the roster refuses it, or the
  rendered charter is left stale.
- **AC5** — When `git grep -n "gov-maintainer" -- help/roles.md` runs, it prints the line naming the
  maintainer and the `maintain` workflow.
  Red when: the page still lists the workflows without it.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `playbook render wiring` · `playbook render selftest` · `check-wiring self-test` · `lexicon naming predicates` · `policy fixtures` · `govkit acceptance matrix` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The layer contract's leg, `layer dependencies (the core never depends on an expansion)`
(PLAY-dOrderedCharter-16 S8), runs S5's arm once that build lands; it is not in the manifest at base,
so it is named here in prose.

New arm: tools/playbook/adopt-playbook.sh · covers AC2 · the playbook-render selftest runs `check_layers.py` over a fixture register whose installed expansion row registers a slot the fixture index lacks, and over one whose row no descriptor joins · none

## 8. Open questions

- **F1 — Which workflow does the maintainer run in?** Options: (a) a new `maintain` entry, driver
  `program`, harness the Maintain program, stage 0; (b) an existing entry such as `bookkeeping`. (b)
  states a route the role never takes, which R7 would then certify. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, the most feature-rich survivor and the brief's I15. widens: none · relaxes: none
- **F2 — Which kit ships the role file?** Options: (a) the roles kit, `tools/roles/agents/`; (b) the
  drift-audit kit, observability's engine kit. (b) needs a second role-file reader in the renderer.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 1, layer-roles `[more]` R3-A ("Each role is
  declared once, in the roles kit") and TOOL-dBoundRoles-1 §4, whose `check_layer_roles` reads role
  files under the roles kit. widens: none · relaxes: none
- **F3 — How is a registration with no definition seen red, when `check_layer_roles` as specced has no
  arm that reads it?** Options: (a) S5's arm, scoped to an expansion a kit descriptor joins; (b) the
  same arm unscoped; (c) no arm, the definition observed by `check_roles.py` alone. (b) reds the tree on
  `gov-deployer`, whose defining build is not an ancestor; (c) leaves the brief's seen case unobservable
  and a later deletion of the role file silent. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3,
  the only survivor meeting AC2 on a green tree. widens: none · relaxes: none
- **F4 — Which write class and tools does the maintainer carry?** Options: (a) `writes: none` with the
  read-only four tools; (b) `writes: records`, filing the ask itself. (b) adds a second writer of a
  filing beside the program's command. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the
  charter's [core] and [security] rules. widens: none · relaxes: none
- **F5 — Is the maintainer an item role or a cycle role?** RESOLVED (agent, 2026-11-01, delegated):
  an item role, `acts-as: item`, rung 1, layer-roles `[roster]` (`layer-roles.md:481`, "item role:
  Maintain's filings"). widens: none · relaxes: none
- **FACT-QUESTION · F6 — Does the build run's base still carry `BODY_CEILINGS` and `WORKFLOW_NAMES`,
  or have TOOL-dBoundRoles-15 and TOOL-dBoundRoles-20 replaced them?** Probe: `grep -c
  "BODY_CEILINGS\|WORKFLOW_NAMES" tools/roles/check_roles.py` at the build run's base. Observation: a
  count above 0 means the tables stand and S2 and S4 write a row and a member; 0 means S2 writes the
  `budget` field and S4's entry alone admits the name. Liveness: the probe prints 6 at `f4597719`, and
  TOOL-dBoundRoles-15 AC4 and TOOL-dBoundRoles-20 AC3 each assert the count falls to 0, so both answers
  are reachable. RESOLVED (agent, 2026-11-01, delegated): the build run takes whichever form the probe
  reads, rung 2. widens: none · relaxes: none
- **F7 — The charter's roster region and `help/roles.md` change, and the charter is a governance
  carrier.** RESOLVED (agent, 2026-11-01, delegated): render both, rung 3; the roster line is the
  generated region's own output of the role this clause defines. widens: none · relaxes: none ·
  grants: PLAY-dClosedLoop-3 the roster line `gov-maintainer` in the rendered `AGENTS.md`

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the packet's Items 10 (`cl-dClosedLoop-0451@8cb0a7a7`), the
  brief's I15, scout A's row for cl-0451, TOOL-dBoundRoles-1 §4, layer-roles `[roster]` and the roles kit
  at base `f4597719`.

## 10. Reuse audit

The seams extended are the role catalogue and its checker, `BODY_CEILINGS` and `WORKFLOW_NAMES`
(`tools/roles/check_roles.py:87-93`), R6 to R8 (`:277`, `:325`, `:331-333`, `:349`), the seed list
(`tools/roles/kit.toml:36-39`), `render_agent_file` and `render_roles_index`
(`tools/roles/render_agents.py:144`, `:207`) and `print_roster` (`tools/roles/handoff.py:491`), each
verified at `f4597719`; and the parent seam `check_layer_roles` (TOOL-dBoundRoles-1 S5, DEFERRED).
`python tools/codebase-map/reuse_lookup.py "define a role agent and register it on an expansion
layer"` ranked name stems only (`RolesError`, `load_roles`, `render_role`, `load_project_layer`), as
the brief warned, and named no layer join, the expected answer: no `tools/playbook/layers.toml` and no
`check_layers.py` exist at base. The recall probe returned scout A's row, TOOL-dBoundRoles-1 S5,
layer-roles `[roster]` at `:461` and the brief's row; scout A's citations of `check_roles.py:87`,
`:92`, `:97` and `kit.toml:36-40` agree with source (the seed list ends at `:39`).

Recall terms used: `python tools/memory-recall/query.py "where is the maintainer role defined and registered on the observability layer" --terms "maintainer gov-maintainer role file observability layer registration check_layer_roles BODY_CEILINGS WORKFLOW_NAMES expansion roles"`

### Alternatives rejected

- **The role file shipped by the drift-audit kit.** `render_agents.py` reads role files from the roles
  kit's `agents/` only, and layer-roles R3-A declares each role once, in the roles kit; a second home
  would need a second reader. Rejected by reading `render_agents.py:144` (`render_agent_file` takes
  the roles kit's directory) and layer-roles `[more]` R3-A.
- **The maintainer on an existing workflow** (`bookkeeping` or `research`). R7 would then state a route
  the role never takes, which TOOL-dBoundRoles-1 rejected for the planner and the architect.
- **An unscoped arm that reds every registered slot with no file.** Tested against the tree's
  registration rows as TOOL-dBoundRoles-1 §4 writes them: `gov-deployer` is registered on two rows and
  defined by a build that is not an ancestor, so the unscoped arm reds the tree from this landing until
  dShippedRelease's.
- **`writes: records`, the maintainer writing the ask row itself.** It would put a second writer of
  Maintain's filings beside the program's command, against the charter's [core] rule, and widen the
  role's write class beyond what composing text needs.
