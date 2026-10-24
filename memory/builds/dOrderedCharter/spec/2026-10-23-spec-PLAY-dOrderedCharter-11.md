# PLAY-dOrderedCharter-11 — load sets derived per reader and item, budgeted, and refused when a required unit is missing

**Status:** DEFERRED · rev-3 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 21 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0041@29cae3c8 whole
**Carries:** node:policy-key.instructions.checks

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-27 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-build-PLAY-dOrderedCharter-11-deviation-111.md](../build/2026-10-24-build-PLAY-dOrderedCharter-11-deviation-111.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-11-deviation-112.md](../build/2026-10-24-build-PLAY-dOrderedCharter-11-deviation-112.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |
| [2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-25-build-PLAY-dOrderedCharter-11-deviation-113.md](../build/2026-10-25-build-PLAY-dOrderedCharter-11-deviation-113.md) | deviation | — |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-11-1-spec-writer.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-11-1-spec-writer.md) | journal | — |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

No load set is computed per reader, six load points carry budgets and the rest none, and no injected
load point is measured (gap-found-10); and the one switch that held the missing-unit refusal also held
the size budget, so loosening one loosened the other (gap-found-34). This unit derives each reader's
load set from the instruction-unit rows, refuses a set missing a unit its `required-by` names as
`instructions.checks` says, still refused under `budgets.enforce`'s `warn`, measures each rendered load
point against its cap under `budgets.*` and its harness's limit, and measures the injected load points
at session start (layer-instruction R-C, v2:973-981 P27, v2:1242, the owner's NT-22, the whole-design
audit's C1-F1 and C1-F14).

## 2. Scope (IN)

- **S1** — The load set. `derive_load_set(units, reader, item=None)` in a new module
  `tools/playbook/load_sets.py` returns, from S10's rows read through `tools/playbook/instruction_units.py`,
  the units whose `scope` selects every reader (`reader.every`), the reader's role (its `role.<name>`
  selector, or a practice tag its `rules:` value cites), and its item. The item and step selectors are
  dDeclaredLoop's namespaces: until it registers them the item part is reported `unarmed`, never empty
  and green. Observed by AC1.
- **S2** — The missing-unit refusal. `check_required(load_set, units, reader, item, mode)` names every
  unit whose `required-by` names the reader's role or its item and which the set lacks. `mode` is
  `instructions.checks`: `refuse` (default) leaves the render undone and exits 1 naming each unit;
  `warn` renders the whole set and puts a `Missing required unit: <tag>` line where the reader sees it;
  `record` renders and writes the gap into the prompt record's `**Load gaps:**` line only. No value
  skips the check (foundations C6, LR-1). `budgets.enforce` is never read here, so `warn` there leaves
  the refusal standing. The key is read with `policy.py get instructions.checks` through unit 9's
  `policy_reader`, the playbook kit's one subprocess reader of that verb, called with the key literal
  first, `policy_reader("instructions.checks", …)`, the call shape dGroundRules' reader-coverage arm
  counts (TOOL-dGroundRules-8, its Readers table). It reads the target's committed policy at its landed
  revision, and an unset key answers the catalogue default `refuse` with its reason
  (TOOL-dGroundRules-2 S7, TOOL-dGroundRules-3 S2); on the reader's exit 2, or with no policy kit
  found, the check runs as `refuse` and prints the reader's line once (§8 F4). The key's catalogue row
  lands with dGroundRules with no `summary` or `usage`, named on the shrink-only
  `tools/policy/unsummarised-keys.txt` (TOOL-dGroundRules-1 S3, S6): this unit adds no row; it fills that
  row's `summary` and its `usage`, a line the row admits (`instructions.checks = "warn"`), and drains the
  name with `python <prefix>/policy/policy.py lists --write` in the same commit. Observed by AC2, AC3
  and AC6.
- **S3** — The budgets. `check_budget(load_point, size, mode)` measures a rendered load point's bytes,
  CR stripped, of the committed blob, against its cap under `budgets.*`, held in
  `.governance/policy.toml` since dSafePassage's step moved every row of the former limits file there
  (TOOL-dSafePassage-1 S7, S8). Each cap is named as the census `tools/policy/caps.toml` names it
  (TOOL-dGroundRules-9 S1): a load point's cap is the census row whose `name` is its repo-relative path,
  `AGENTS.md` for the charter and the path of each Skill that has one, read from the census with
  `tomllib` and never typed here; a role block's is `role-body`, a family cap whose value stays
  `BODY_CEILINGS` (`tools/roles/check_roles.py:85-89`) and whose mode alone is asked. One
  `python <prefix>/policy/budgets.py resolve <cap> …` subprocess per run, the policy kit found through
  the inlined `resolve_kit_dir`, answers each cap's value and its mode, `refuse` under
  `budgets.enforce = "refuse"` or a `budgets.pinned` name and `warn` otherwise (TOOL-dGroundRules-9 S2);
  over its cap a load point warns or refuses as that mode says. Per harness, a load point a harness
  reads whole carries that harness's limit as a second cap, today the charter under Codex's `CODEX_MAX`
  (32768), read through the census row `codex-instructions` (class `consumer`): its `home`,
  `constant:<path>:CODEX_MAX`, names the file whose `CODEX_MAX` assignment line is read, so the move
  unit 31 makes re-points the row and this read with it. A set over it is refused whatever the mode
  (R-C). A load point with no census row prints `no cap declared`, never a pass; on `budgets.py`'s
  exit 2 the render refuses printing the reader's line, and with no policy kit found the budget check
  prints `unarmed` naming it (§8 F4). Observed by AC4.
- **S4** — The render calls. `render_handoff` (`tools/roles/handoff.py:312`) and `render_agent_file`
  (`tools/roles/render_agents.py:144`) derive the role's load set and run S2 and S3 before writing;
  `render()` (`tools/playbook/render_playbook.py:979`) runs S3 over the charter. The roles kit finds
  `load_sets.py` through `resolve_kit_dir` and runs its `check` verb as a subprocess, as
  `derive_role_roster` finds and runs the roles kit's `roster` verb (`render_playbook.py:470-500`),
  since a kit may not import a sibling kit (TOOL-dGroundRules-1 §4 Evidence); with the playbook kit
  absent the check prints `unarmed` and the render proceeds. Observed by AC2.
- **S5** — The injected load points, measured. `python tools/playbook/load_sets.py injected` prints one
  line per injected load point the harness places from this repository, with its bytes and its cap or
  `no cap declared`, and a breach line when over: the agent list (each `description:` of
  `.claude/agents/*.md`), the Skill list (each `description:` of `.claude/skills/*/SKILL.md` and
  `skills/*/SKILL.md`) and the session-start hook's output (the card). The session-start card writer,
  `write_card` (`skills/session-kickoff/manifest-check.sh:706`), runs it and appends its breach lines,
  none when nothing is over. Observed by AC5.

## 3. Non-goals (OUT)

- The `budgets.*` keys, `budgets.enforce`, `budgets.pinned` and the policy reader: dGroundRules
  (v2:1346-1348). No cap value is set or moved here.
- The `code` slot in a role's load set: `PLAY-dOrderedCharter-27`.
- Each practice's reach for the step in a work order: `PLAY-dOrderedCharter-21`.
- The auto-memory index as an injected load point, and directives found in it:
  `PLAY-dOrderedCharter-14`.
- A composition over a harness's limit at update, and the project block's count:
  `PLAY-dOrderedCharter-34`.
- The item, step and policy selectors' joins: dDeclaredLoop. The work order's packet budget:
  dBoundRoles.
- Field loads measured from the roles' runs (R-C): no run measurement exists to read.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-9` — S10's unit rows and their `required-by` and `scope` fields
- **consumes-from** `PLAY-dOrderedCharter-1` — the practice tags a role's `rules:` value cites
- **hands-off** `PLAY-dOrderedCharter-27` — the `code` slot added to the load set and its budget
- **hands-off** `PLAY-dOrderedCharter-21` — the step's practice reach added to the load set
- **hands-off** `PLAY-dOrderedCharter-34` — the composition's count against each budget, reusing the budget check
- **consumes-from** external — dGroundRules, landed before the build run: `policy.py get` at the landed revision (TOOL-dGroundRules-2 S7) with an unset key's default and reason (TOOL-dGroundRules-3 S2), the `instructions.checks` row and the shrink-only list this unit drains (TOOL-dGroundRules-1 S3, S6), `budgets.py resolve` and the cap census (TOOL-dGroundRules-9 S1, S2), `budgets.enforce` in gov's policy file at `warn` (TOOL-dGroundRules-1 S1), and the reader-coverage arm's call shapes (TOOL-dGroundRules-8)
- **consumes-from** external — dSafePassage, landed before the build run: the step that moved every row of the former limits file under `budgets.*` in `.governance/policy.toml` (TOOL-dSafePassage-1 S7, S8)
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 12 and 40, which that batch unit corrects after this unit lands, each by the item its report id names

## 4. Design

### Data model

The unit row fields this unit reads are S10's: `scope` (a list of selector tags), `required-by` (a list
of `role.<name>` or `item.<tag>`), `budget` (its class). The load set is a list of unit tags, in the
unit registry's order. A refusal line: `load-set — refused · <reader> · missing <tag>[, <tag>] ·
instructions.checks=refuse`.

### Inventory

Minted: `tools/playbook/load_sets.py`; `derive_load_set`, `check_required`, `check_budget`; the CLI
verbs `derive`, `check` and `injected`; the prompt record line `**Load gaps:**`; the reader-visible
line `Missing required unit: <tag>`; the printed states `unarmed` and `no cap declared`. The policy key
`instructions.checks` and its three values are v2's.

### Migration

None. The gate legs that measure a cap at the bar, `charter size` and the roles kit's body ceilings,
keep the mode `budgets.py` answers them (TOOL-dGroundRules-9 S5); this unit adds the render-time
measurement beside them.

### Rollout

Live at landing. On gov's tree the roles carry no `required-by` row naming them until units are
registered with one, so the refusal is first exercised by the fixture; the derive verb prints each
role's set and its required count, a zero printed as a count and never as a pass.

Two commits. The first lands the unit with the row's fill and the list's drain. The second stages only
`.governance/policy.json` as `policy.py mirror --write` regenerates it, because the mirror records the
catalogue's blob id and the fill stales it (TOOL-dGroundRules-5 S1), and the guard admits a mirror
commit only when the policy file and the catalogue equal HEAD (TOOL-dGroundRules-19 S1).

### Files touched (estimate)

- `tools/playbook/load_sets.py`
- `tools/playbook/instruction_units.py`
- `tools/playbook/render_playbook.py`
- `tools/roles/handoff.py`
- `tools/roles/render_agents.py`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `help/roles.md`
- `tools/policy/catalogue.toml` (the `instructions.checks` row's `summary` and `usage`)
- `tools/policy/unsummarised-keys.txt` (drained by `lists --write`)
- `.governance/policy.json` (the second commit, regenerated by `mirror --write`)

### Alternatives rejected

- **One switch for both refusals**, as `instructions.checks` held before the night pass two: the owner
  split them (NT-22), and gap-found-34 is that coupling.
- **The load-set code inside the roles kit.** The charter and Skills are load points too, and the
  playbook kit already holds S10's reader.
- **A third SessionStart hook for the injected measure.** The card writer already runs at session
  start, and a third entry is what `check_card` (`tools/check-wiring.sh:1044`) refuses.

## 5. Production-readiness checklist

- security: no write path beyond the prompt record's gap line, written by the renderer that writes the
  record.
- perf / scale: one registry read per render; the injected measure reads about 20 small files.
- error / empty / loading states: an unreadable unit registry refuses the render naming it; an empty
  population prints its count.
- observability: every refusal and breach is one line naming the reader, the load point and the value.
- risks: a role's set refused at a spawn stops that pass, by design; `warn` is the owner's lever.
- testing: §6 and the `New arm:` lines of §7.
- migration: none.
- user docs: `help/roles.md` gains what a refused handoff says and the three `instructions.checks`
  values.

## 6. Acceptance criteria

- **AC1** — When `python load_sets.py derive --reader role.gov-builder --units <fixture>`
  runs over a fixture registry with units scoped `reader.every`, `role.gov-builder` and `role.gov-skeptic`,
  it prints the first two and not the third, and the item part `unarmed`.
  Red when: a unit scoped to another role loads, or the item part reads as empty.
- **AC2** — When `python load_sets.py check --reader role.gov-builder --units <fixture>`
  runs over a planted registry whose unit `required-by = ["role.gov-builder"]` is scoped only to
  `role.gov-skeptic`, it exits 1 naming the unit under `--checks refuse`; and `handoff.py render` for
  the builder over that fixture writes no prompt file.
  Red when: the set missing the required unit renders.
- **AC3** — When the AC2 fixture runs under `--checks warn` and `--checks record`, both exit 0: `warn`
  puts `Missing required unit:` in the rendered text, `record` writes `**Load gaps:**` in the prompt
  record and nothing in the text; under `--checks refuse --budgets-enforce warn` it still exits 1.
  Red when: either value skips the check or `budgets.enforce` softens the refusal.
- **AC4** — When `check_budget` runs through `load_sets.py check --load-point AGENTS.md` over a scratch
  charter of 40000 bytes with a scratch cap of 50000, it exits 1 naming `CODEX_MAX` under
  `--budgets-enforce warn`; over a scratch role block 10 bytes past its body ceiling it prints a warning
  and exits 0 under `warn`, and exits 1 under `refuse`.
  Red when: a harness-limit breach passes under `warn`, or a cap breach refuses under `warn`.
- **AC5** — When `python load_sets.py injected` runs in gov, it prints a line for the
  agent list, the Skill list and the card, each with its bytes; with a scratch cap below the agent
  list's bytes it prints a breach line naming the agent list.
  Red when: a load point is missing or a breach prints nothing.
  figure: the bytes are DERIVED on each run.
- **AC6** — When `python "tools/policy/policy.py" lists --check` runs after the first commit, it exits 0;
  `git grep -n -x -F "instructions.checks" -- "tools/policy/unsummarised-keys.txt"` finds no line; and
  `git grep -n -F '("instructions.checks"' -- tools/playbook/load_sets.py` finds one line.
  Red when: the row keeps no summary or usage, the name stays on the shrink-only list, or the key is
  read in a shape the reader-coverage arm does not count.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `roles render wiring` · `roles render selftest` · `govkit acceptance matrix` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates`

New arm: tools/playbook/load_sets.py · covers AC1 AC2 AC3 AC4 · its selftest plants the fixture registry with a required unit scoped away from its role, and the oversized charter and role block · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC5 · a fixture card write with a scratch cap below the agent list's bytes · none

## 8. Open questions

- **F1 — Where `record` writes a gap.** R-C says "the gap is recorded" and names no record. Options: (a)
  a `**Load gaps:**` line in the prompt record the render writes; (b) a journal line; (c) an ask.
  RESOLVED (agent, 2026-10-23, delegated): (a), rung 3; the prompt record is the one record every
  rendered work order already has, (b) has no journal for a main-loop render, and (c) is what R-C gives
  the caller on a refusal, not on `record`. widens: none · relaxes: none
- **F2 — Which budget mode applies at render.** Options: (a) `budgets.enforce`'s catalogue default
  `warn`, read with no reader; (b) `refuse`; (c) no render-time budget; (d) the mode `budgets.py resolve`
  answers per cap. The first pick was (a), on the premise that the key did not exist yet, which the
  parents' landed specs remove: `budgets.enforce` sits in gov's policy file at `warn`
  (TOOL-dGroundRules-1 S1), and `budgets.py` answers each cap's mode from it and `budgets.pinned`
  (TOOL-dGroundRules-9 S2). RESOLVED (agent, 2026-10-24, delegated): (d), rung 1, the parents' landed
  specs; (a) would ignore a pin, and (b) and (c) set aside the owner's switch. widens: none · relaxes:
  none
- **F3 — Which harness limit applies per load point.** R-K gives harness limits to dWellOiledMachine's
  adapters. Options: (a) Codex's `CODEX_MAX` for the charter alone, read from
  `tools/agent-instructions/adopt-agent-instructions.sh:31`; (b) wait for the adapters. RESOLVED (agent,
  2026-10-23, delegated): (a), rung 3; it is the one harness limit the tree measures today (C1-F14's
  fix plants it), and the adapters add theirs as they land. widens: none · relaxes: none
- **F4 — What the checks do when a policy reader cannot answer.** `policy.py get` and `budgets.py
  resolve` exit 2 on a refusal (TOOL-dGroundRules-2 S7, TOOL-dGroundRules-9 S2), and an adopter may hold
  the playbook kit without the policy kit. Options: (a) the missing-unit check runs as `refuse` and
  prints the reader's line once; the budget check refuses the render on `budgets.py`'s exit 2 and prints
  `unarmed` naming the policy kit when the kit is absent; (b) every such case refuses the render; (c)
  every such case reads the catalogue default. (c) reads a value no reader resolved, and (b) reds every
  render of an adopter that has not installed a kit nothing else requires; TOOL-dGroundRules-9 §8 F4
  rules out both for its own enforcers. RESOLVED (agent, 2026-10-24, delegated): (a), rung 1, that
  fork's (a): a missing reader never loosens a refusal, and says so once. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · S2 S3 S4 · §3 Edges · §4 Migration, Rollout, Files touched · AC6 · §8 F2 F4 · §10 ·
  re-grounded on the parents' landed specs by `2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck.md`
  row 33 and U1 to U4: caps are read with `budgets.py resolve`, named as the census names them, and
  `CODEX_MAX` through its census row; `instructions.checks` is read with `policy.py get` in a shape the
  reader-coverage arm counts, its landed row filled and drained, the mirror in a second commit; F2
  re-resolved on rung 1 and F4 added; the roles kit runs `load_sets.py` as a subprocess.

## 10. Reuse audit

The seams extended: `render_handoff`'s `reads` walk (`tools/roles/handoff.py:337-396`), where a
handoff's blocks are assembled and where the load set joins; `BODY_CEILINGS`
(`tools/roles/check_roles.py:85-89`), the role block's one carrier, read and not copied; the policy
kit's one cap reader, `budgets.py resolve` (TOOL-dGroundRules-9 S2), with each cap named from the census
`tools/policy/caps.toml` (its S1), in place of the former limits file, which dSafePassage's step removes
(TOOL-dSafePassage-1 S8); `resolve_kit_dir`, the sibling resolver (`render_playbook.py:79`,
`roles_lib.py:97`); and `write_card` (`skills/session-kickoff/manifest-check.sh:706`) as the one
session-start writer. `python tools/codebase-map/reuse_lookup.py "budget the bytes a role's handoff
loads"` ranked `load`, `load_conf`, `load_workflows`, `load_text`, `load_policy` and
`derive_budget_cut` (`tools/codebase-map/reuse_lookup.py`), name-stem matches on "load" and "budget";
none derives a load set, and `derive_budget_cut` cuts a shortlist, not a load point, so the map and
the source disagree on fit.

Recall terms used: `python tools/memory-recall/query.py "how are load sets budgeted per role and refused when a required unit is missing" --terms "load set budget required-by instructions.checks budgets.enforce BODY_CEILINGS role render refuse warn"`
