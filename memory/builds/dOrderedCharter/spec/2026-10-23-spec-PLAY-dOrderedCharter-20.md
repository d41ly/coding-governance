# PLAY-dOrderedCharter-20 — the unit schema, the one renderer of record and its templates, the render gate with its legacy list, and one fact in one unit

**Status:** OPEN · rev-3 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 15 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0050@13d9192b whole

**Carries:** node:policy-key.instructions.legacy

**Carries:** node:system.instruction-writing

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-27 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

Four renderers write instruction files today, each behind its own leg (`playbook render wiring`, `roles
render wiring`, `agent-instructions wiring` and the inline copies of `tools/lib/render-doc.sh`), and one
fact in one place is policed per instance, never as a class (gap-found-23). The instruction-writing system
(systems `[design-instruction-writing]`) gives units one schema, documents one renderer of record and
templates of slots, and arms a render gate at this build with a shrink-only list of today's hand-written
documents (IW-1). This unit builds that system over the rows unit 9 reads: the schema check, the one-fact
check, each unit's status derived from its change record, the renderer-of-record table and its check, the
one renderer absorbing the playbook, roles and agent-instructions renders and playbook parity, the charter
and work-order templates' slot mechanism, the render gate under `instructions.legacy`, and the
instruction-unit kind's factory.

## 2. Scope (IN)

- **S1** — The schema check, `python tools/playbook/instruction_units.py schema`, over every row
  `read_units` returns: a row missing `tag`, `level` or `type`; an unknown key; a `tag` outside the `unit`
  namespace or breaking S4's grammar; a `type` outside `STATEMENT_TYPES`; a `budget` outside `line` and
  `block`, or `text` over its budget's bytes (200 or 600); a typed type with no `text` or a `fact` or
  `policy-value` with no `source`; a `class` outside `fixed` and `open`; a `scope` or `required-by` entry
  that is not a tag of a registered namespace; and an `enforced-by` that is neither a list of non-empty
  descriptions nor one string `none — <why>`. Each red names the manifest, the tag and the field.
  Observed by AC1.
- **S2** — The one-fact check, `python tools/playbook/instruction_units.py one-fact`: two active units with
  one key are red, the key a typed unit's type and its text under S7's normaliser and a derived unit's type
  and `source`; and two active `definition` units defining one term, the text before ` — `, are red
  whatever their meanings. Observed by AC2.
- **S3** — Status derived from the change record (S13). `derive_status(tag, records)` returns one of
  S13's three status values from the change records naming the tag, read through unit 7's record factory
  as the kind unit 15 registers; no row carries `status`, and S1 refuses one that does. A unit whose
  derived status is not `active` and that a template selects is red at render. Observed by AC3.
- **S4** — The renderer-of-record table, `tools/playbook/renderers.toml`: one `[[target]]` row per
  instruction-file population, `paths` (globs) and `renderer`, the instruction files being the closed
  pathspec list `INSTRUCTION_PATHSPECS` in `instruction_units.py`: the charter `.memory-tree.conf`'s
  `CHARTER` names, `CLAUDE.md`, `.claude/agents/*.md`, `.claude/rules/*.md`, `.claude/skills/*/SKILL.md`,
  `skills/*/SKILL.md`, `{memory_root}/guides/*.md`, `{memory_root}/TEMPLATE-SPEC.md` and
  `{memory_root}/HYGIENE.md`. A file two rows claim, or none, is red, so each instruction file has exactly
  one renderer of record. Observed by AC4.
- **S5** — The one renderer. `tools/playbook/render_playbook.py` is the renderer of record (S11) for three
  scopes: `charter` (today's `render()`), `agents` (each `.claude/agents/*.md`, rendered by the roles kit's
  `render_agent_file` as the scope's slot renderer, reached through `resolve_kit_dir`), and `entry-files`
  (`CLAUDE.md` and each other harness alias, the pointer or copy `adopt-agent-instructions.sh` writes
  today, its logic moved into the renderer). `python tools/playbook/render_playbook.py --render-scope
  <scope>` writes a scope and `--check-render --scope <scope>` compares its bytes; every write records the
  target's lock row (unit 12). `adopt-roles.sh` and `adopt-agent-instructions.sh` call these for their
  render and their `--check`, so no second renderer writes an absorbed file. Observed by AC5.
- **S6** — The absorbed legs keep their names, the join key every leg-keyed file reads, and run the one
  gate scoped to the targets they covered: `playbook render wiring` the `charter` scope, `roles render
  wiring` the `agents` scope, `agent-instructions wiring` the `entry-files` scope, and `playbook parity`
  the `claims` scope, whose arms are `check-playbook-parity.sh`'s S1, S2 and S4, run by the gate until the
  charter's stated values render from sourced fact units. The two render selftests fold into
  `render_playbook.py`'s selftest. Observed by AC6.
- **S7** — The templates. A template holds slot lines and no prose: `<!-- units: <selector> -->` on its own
  line expands, at render, to `render_units(derive_unit_selection(units, selector))` (unit 9). `render()` expands
  slots in the charter template; the work-order template `tools/playbook/templates/work-order.template.md`
  holds today's handoff sections as slots (`role`, `opening`, `reads`, `charter-blocks`), and
  `render_handoff` (`tools/roles/handoff.py`) fills them, its output byte-identical to today's for the same
  inputs. The charter's own units are unit 2's. Observed by AC7.
- **S8** — The render gate, `python tools/playbook/render_playbook.py --check-render` with no scope: every
  scope's bytes, S4's table, S3's status arm, and the legacy list `tools/playbook/instructions-legacy.txt`,
  one path per instruction file not yet rendered from units, a file whose lock row (unit 12) lists units
  being rendered from units. Under `instructions.legacy`: `shrink-only`, the default, reds an instruction
  file neither rendered from units nor listed, and a listed file now rendered from units as stale;
  `refuse` reds every listed file. Read through dGroundRules' one reader (`cl-dClosedLoop-0008`) once it
  lands, and until then with v2's default, `shrink-only` (v2:1359). Observed by AC8.
- **S9** — The instruction-unit kind's factory and gate (deviation 71):
  `python tools/playbook/core.py new unit <name> --kit <kit> --type <t> --level <n> --text <line>` composes a
  row S1 passes and prints it with the unit-15 command that writes it, never writing a manifest itself;
  the kind's gate is S1's leg, and the kind's row in `tools/playbook/kinds.toml` names both, leaving
  `tools/playbook/core-pending.txt`. Observed by AC9.
- **S10** — The legs and plants. Legs `instruction units (schema, one fact)` and `instruction render (one
  renderer of record)` in `tools/gate-legs.json`, each carrying `"enforces": ["principle.p11",
  "principle.p13"]`; `python tools/playbook/instruction_units.py fixture --plant <case>` stages every case in a throwaway
  tree in the system temp directory.
  Observed by AC1 to AC9.

## 3. Non-goals (OUT)

- The write command, `instructions.edit`, its manifest and its change record kind: unit 15
  (`cl-dClosedLoop-0045`), which S3 and S9 call.
- The charter's re-founded content: unit 2. Envelopes: unit 3. Load sets and budgets: unit 11. Step-scoped
  practice units in work orders: unit 21. The `code` slot: unit 27.
- Migrating the guides, the Skills and `.claude/rules/` onto units: each chain build migrates its own
  step's guides (IW-1); their renderers stay the record for them, beside the legacy list:
  `tools/lib/render-doc.sh`'s copies, kit/dogfood doc parity, review-protocol parity, each kit's skill wiring
  `--check` and govkit's placeholder render.
- The adopter upgrade step that moves agent-instructions' wiring: unit 31.
- The role static block template and the single carry: dBoundRoles; hook-message and harness-prompt
  templates: dWellOiledMachine.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-9` — `read_units`, `derive_unit_selection` and `render_units`, which every check and slot reads
- **consumes-from** `PLAY-dOrderedCharter-12` — `STATEMENT_TYPES` and the lock rows S8 reads and S5 writes
- **consumes-from** `PLAY-dOrderedCharter-7` — the record factory S3 reads change records through, the kinds register S9 updates, and the `enforces` key
- **consumes-from** `PLAY-dOrderedCharter-24` — S7's shared normaliser, the one-fact key's hash
- **consumes-from** `PLAY-dOrderedCharter-19` — the tag grammar and namespace registry S1 grades `tag`, `scope` and `required-by` against
- **hands-off** `PLAY-dOrderedCharter-15` — the write command S9 prints, and the change records S3 derives status from
- **hands-off** `PLAY-dOrderedCharter-2` — the charter's units, rendered through S7's slots
- **hands-off** `PLAY-dOrderedCharter-3` — `INSTRUCTION_PATHSPECS`, the instruction-file population its load-bearing population reads
- **hands-off** `PLAY-dOrderedCharter-21` — the work-order template's slots, which step-scoped units join
- **hands-off** `PLAY-dOrderedCharter-31` — the renderer-of-record move an adopter's upgrade step makes
- **hands-off** `PLAY-dOrderedCharter-1` — the renderer of record the practice expansion lives in
- **hands-off** `PLAY-dOrderedCharter-6` — the renderer of record the drive expansion lives in
- **hands-off** `PLAY-dOrderedCharter-32` — the renderer of record, which takes its unit list from the overlay's composition
- **hands-off** `PLAY-dOrderedCharter-34` — the renderer of record and the absorbed agent-instructions wiring composition renders through
- **hands-off** `PLAY-dOrderedCharter-37` — the renderer of record its reference mode lives in
- **hands-off** `PLAY-dOrderedCharter-43` — the card option and its check in the entry-files scope, which the absorbed wiring leg and the render leg carry for gov (finding 49)
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 5, 12, 50 and 67, which that batch unit corrects after this unit lands, each by the item its report id names
- **consumes-from** `PLAY-dOrderedCharter-50` — the owed-rows probe: this pass runs `python tools/run-gates/owed_rows.py --base HEAD` before its commit and writes every row it names in that commit (round-2 id 23)
- **hands-off** `PLAY-dOrderedCharter-55` — the `instruction render (one renderer of record)` leg, whose argv carries `--card` in gov's manifest (round-2 id 29)

## 4. Design

### Data model

```toml
# tools/playbook/renderers.toml
[[target]]
paths = ["{charter}"]
renderer = "playbook:charter"

[[target]]
paths = [".claude/agents/*.md"]
renderer = "playbook:agents"

[[target]]
paths = ["CLAUDE.md"]
renderer = "playbook:entry-files"

[[target]]
paths = ["{memory_root}/guides/*.md", "{memory_root}/TEMPLATE-SPEC.md", "{memory_root}/HYGIENE.md"]
renderer = "render-doc"
```

The work-order template, `tools/playbook/templates/work-order.template.md`, holds two second-level
headings, `Role` and `Task`, and four slot lines, each `<!-- slot: <name> -->` on its own line:

| Slot | Under | Filled with |
|---|---|---|
| `role` | `Role` | the role's static block, `render_role`'s output today |
| `opening` | `Task` | the build and unit sentence and the optional-input line |
| `reads` | `Task` | one `### <key>` block per read key, in the order `reads` names |
| `charter-blocks` | `Task` | `render_charter_blocks`' output for the role's `rules:` |

### Inventory

Minted: the verbs `schema` and `one-fact`, `derive_status`, `INSTRUCTION_PATHSPECS`, the files
`tools/playbook/renderers.toml`, `tools/playbook/instructions-legacy.txt` and
`tools/playbook/templates/work-order.template.md`, the renderer flags `--render-scope`, `--check-render`
and `--scope` with the scopes `charter`, `agents`, `entry-files` and `claims`, the slot line grammar, the
factory verb `new unit`, and the legs `instruction units (schema, one fact)` and `instruction render (one
renderer of record)`. The legacy list's seed is DERIVED at the build pass from `INSTRUCTION_PATHSPECS`; at
`4e8f80cdf` it would hold 33 files (PINNED, 2026-10-23: `AGENTS.md`, `CLAUDE.md`, nine agent files, one
rule, seven installed Skills, two authored Skills, ten guides, `TEMPLATE-SPEC.md` and `HYGIENE.md`).

### Migration

The build pass seeds the legacy list and moves `adopt-agent-instructions.sh`'s pointer and copy writes into
the renderer, the script calling it. Rendered bytes do not change: the scopes reproduce today's outputs.

### Rollout

Live at landing, at order 15, after unit 9 (order 14); units 15 (order 16), 2 (order 20) and 3 (order 18)
build on it.

### Files touched (estimate)

- `tools/playbook/instruction_units.py`
- `tools/playbook/render_playbook.py`
- `tools/playbook/core.py`
- `tools/playbook/kinds.toml`
- `tools/playbook/core-pending.txt`
- `tools/playbook/renderers.toml`
- `tools/playbook/instructions-legacy.txt`
- `tools/playbook/templates/work-order.template.md`
- `tools/roles/handoff.py`
- `tools/roles/render_agents.py`
- `tools/roles/adopt-roles.sh`
- `tools/agent-instructions/adopt-agent-instructions.sh`
- `tools/gate-legs.json`

### Alternatives rejected

- **Deleting the absorbed legs.** Their names key the ceiling evidence, the selftest budgets, the house
  policy's `[gates]`, each kit's `silenced_legs` and the run-log history; the systems record keeps a leg's
  name and changes what it runs.
- **Typing `status` on the row.** It is derived from the change record and never typed (the systems
  record, the audit's L7).
- **Migrating the guides now.** IW-1 has each chain build migrate its own step's guides; the legacy list
  holds them until then.

## 5. Production-readiness checklist

- security: the renderer writes only the targets `renderers.toml` assigns it and their lock rows; the
  factory never writes a manifest, which stays unit 15's guarded command.
- perf / scale: one render per scope; the checks read the rows once.
- error / empty / loading states: an instruction file with no renderer row is red; an empty unit
  population prints `unarmed`, never green.
- observability: each red names the path or tag, the arm and the remedy.
- risks: the roles kit's render now reaches the playbook kit, a core-to-core edge unit 16's check admits;
  an adopter whose roles kit updates before its playbook kit renders with the old renderer until unit 31's
  step runs.
- testing: S10's plants both ways, and the byte-identity of every scope and the handoff.
- migration: §4 Migration.
- user docs: `help/roles.md` names the leg that holds the agent files (its line 141), unchanged in name.

## 6. Acceptance criteria

- **AC1** — When `python instruction_units.py fixture --plant schema` runs, a row missing
  `level`, a row typed `prose`, a `line` text of 201 bytes, a `fact` with `text` and no `source`, an unknown
  key `prio` and `enforced-by = ""` each red `schema` naming the field, and a well-formed row passes.
  Red when: a malformed row passes.
- **AC2** — When `python instruction_units.py fixture --plant one-fact` runs, two active
  directives with one normalised text and two definitions of `level` with different meanings each red
  `one-fact`, and the same pair with one retired passes.
  Red when: one fact held twice passes.
- **AC3** — When `python instruction_units.py fixture --plant status` runs, `derive_status`
  returns `active` with no record, `retired:unit.b` for a rename, `retired:unit.b,unit.c` for a split and
  `retired:none` for a retirement, a row typing `status` reds `schema`, and a retired unit a template
  selects reds the render.
  Red when: a status is read from the row, or a retired unit renders.
- **AC4** — When `python instruction_units.py fixture --plant renderers` plants a guide no
  `renderers.toml` row claims and an agent file two rows claim, `--check-render` exits 1 naming each.
  Red when: an instruction file has no renderer of record, or two.
- **AC5** — When `python tools/playbook/render_playbook.py --check-render --scope agents` and `--scope
  entry-files` run over the tree, each exits 0 with the bytes `adopt-roles.sh` and
  `adopt-agent-instructions.sh` wrote before this unit, and `git grep -n "render_agent_file\|@AGENTS.md" --
  tools/roles/adopt-roles.sh tools/agent-instructions/adopt-agent-instructions.sh` shows each script
  calling the renderer rather than writing the file.
  Red when: an absorbed file is written by a second renderer, or its bytes move.
- **AC6** — When `python -c "import json, sys; print({l['name']: l['argv'] for l in json.load(open(sys.argv[1], encoding='utf-8')) if l['name'] in ('playbook render wiring', 'roles render wiring', 'agent-instructions wiring', 'playbook parity')})" tools/gate-legs.json`
  runs, each of the four names is present and each argv runs `--check-render` with its scope, directly or
  through its kit's `--check`.
  Red when: a name is gone, or a leg still runs its own renderer.
- **AC7** — When `python instruction_units.py fixture --plant work-order` runs, `handoff.py
  render --stdout` over the case's fixture build prints bytes equal to the expected output the case pins
  from the render before the template, and
  `python instruction_units.py fixture --plant slots` expands a `<!-- units: role.builder -->`
  slot into the selected units' lines.
  Red when: the template changes a handoff's bytes, or a slot renders prose of its own.
- **AC8** — When `python instruction_units.py fixture --plant legacy` plants an instruction file neither
  rendered from units nor on `instructions-legacy.txt`, and a listed file whose lock row lists units, the
  gate reds both under `shrink-only`, and under `refuse` reds every listed file.
  Red when: an unlisted hand-written document passes, or the list grows unseen.
- **AC9** — When `python tools/playbook/core.py new unit demo --kit playbook --type directive --level 3
  --text "MUST demo."` runs, it prints one row `schema` passes and the unit-15 command that writes it, the
  manifest is unchanged, and `core.py kinds` reads the instruction-unit kind with its factory and gate.
  Red when: the factory writes a manifest, or its row fails the schema.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `agent-instructions self-test` · `playbook render wiring` · `roles render wiring` · `roles render selftest` · `agent-instructions wiring` · `playbook parity` · `roles catalogue` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/instruction_units.py · covers AC1 AC2 AC3 AC4 AC7 AC8 · the `schema`, `one-fact`, `status`, `renderers`, `work-order` and `legacy` fixture cases, each failing case staged by its plant · none

New arm: tools/playbook/render_playbook.py · covers AC5 · the render selftest re-renders each scope over a fixture target and compares bytes, its failing case a scope writing one byte differently · none


## 8. Open questions

- **F1** — The clause names "the write command" beside the templates. Is it this unit's?
  RESOLVED (agent, 2026-10-23, delegated): rung 1, v2 answers it: `cl-dClosedLoop-0045` carries the
  instruction manifest and its guarded write command, built by unit 15; this unit calls it (S9).
- **F2** — What does "absorbing" a leg mean here: deleting it, or re-pointing it?
  RESOLVED (agent, 2026-10-23, delegated): rung 1, the systems record answers it: "A leg keeps its name"
  (`[design-tags]`, the audit's M26), and the name is the join key of the files keyed by leg name. Each
  absorbed leg runs the one gate scoped to its targets (S6).
- **F3** — `playbook parity` grades claims, not render bytes, and the charter's stated values do not yet
  render from sourced fact units. Options: run its arms inside the gate's `claims` scope until then;
  retire it now.
  RESOLVED (agent, 2026-10-23, delegated): rung 3, the most feature-rich survivor: the `claims` scope
  (S6). Retiring it now drops S2's value parity before anything derives those values.
- **F4** — Where is the instruction-file population declared, given unit 3 derives a load-bearing
  population after this unit?
  RESOLVED (agent, 2026-10-23, delegated): rung 3: once, as `INSTRUCTION_PATHSPECS` (S4), which unit 3's
  population reads; two derivations of one population are the one-fact class this unit gates.

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the spec run's carrier of `cl-dClosedLoop-0050`.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-43, PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-50, PLAY-dOrderedCharter-55.

## 10. Reuse audit

The seams extended are `render()` in `tools/playbook/render_playbook.py` (line 979), the renderer of record
S11 names; `render_agent_file` (`tools/roles/render_agents.py:144`) and `run_mode` (line 269), which become
the `agents` scope's slot renderer; `render_handoff` (`tools/roles/handoff.py`, around line 312), whose
section order becomes the work-order template; and `_wire_pointer_or_copy` in
`tools/agent-instructions/adopt-agent-instructions.sh`, whose pointer and copy writes move into the
renderer. The legacy list follows the shrink-only list idiom of `tools/dead-path-waivers.txt`. `python
tools/codebase-map/reuse_lookup.py "refuse an instruction file whose bytes differ from its render or that no
renderer produces"` ranked `render` (ten sites, `render_playbook.py` among them) and name-token matches,
which confirms the four renderers scout A listed and finds no renderer-of-record table, so none fits that.

Recall terms used: `python tools/memory-recall/query.py "which renderer of record writes each instruction file and how is the render gate armed with a legacy list" --terms "renderer of record render gate legacy list shrink-only IW-1 playbook parity render wiring one-fact schema"`
