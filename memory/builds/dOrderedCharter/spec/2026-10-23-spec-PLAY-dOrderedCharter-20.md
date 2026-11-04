# PLAY-dOrderedCharter-20 — the unit schema, the one renderer of record and its templates, the render gate with its legacy list, and one fact in one unit

**Status:** DEFERRED · rev-7 · 2026-11-04 · node d · Tier-2 · base ce13efbe · streams playbook · order 15 · advances PLAY-dOrderedCharter-38

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
| [2026-10-24-build-PLAY-dOrderedCharter-20-deviation-201.md](../build/2026-10-24-build-PLAY-dOrderedCharter-20-deviation-201.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-20-deviation-202.md](../build/2026-10-24-build-PLAY-dOrderedCharter-20-deviation-202.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 |
| [2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-25-build-PLAY-dOrderedCharter-20-deviation-203.md](../build/2026-10-25-build-PLAY-dOrderedCharter-20-deviation-203.md) | deviation | — |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-11-02-prompt-PLAY-dOrderedCharter-20-build-brief.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-20-build-brief.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md) | research | PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-11-03-prompt-PLAY-dOrderedCharter-9-drift-sweep-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-9-drift-sweep-brief.md) | research | PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-50 |
| [2026-11-04-prompt-PLAY-dOrderedCharter-20-1-spec-writer.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-20-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-PLAY-dOrderedCharter-20-divergence-brief.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-20-divergence-brief.md) | research | — |
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
one renderer absorbing the playbook and agent-instructions renders and playbook parity, the charter
and work-order templates' slot mechanism, the render gate under `instructions.legacy`, and the
instruction-unit kind's factory. The roles render stays on `render_agents.py` in this unit (F10).

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
  one key are red, the key a typed unit's type and its text under unit 24's one pin normaliser,
  `design_lib.derive_pin_hash` (`tools/memory-tree/design_lib.py:173`), reached as `edge_grammar.py`
  reaches `design_lib`, and a derived unit's type and `source`; and two active `definition` units defining one term, the text before ` — `, are red
  whatever their meanings. Observed by AC2.
- **S3** — Status derived from the change record (S13). `derive_status(tag, records)` returns one of
  S13's three status values from the records naming the tag, each a mapping of unit 15's fields `Unit`,
  `Action` and `Successor`; no row carries `status`, and S1 refuses one that does. A unit whose
  derived status is not `active` and that a template selects is red at render. Every tree read, S2's
  active, the render arm and S8, takes its records from `read_change_records(root)` in
  `instruction_units.py`, which reaches `tools/memory-tree/build_records.py#KINDS` as
  `tools/playbook/instruction_units.py#derive_unit_pin` reaches `design_lib`. While that table holds
  `change` as pending it returns no record, so every unit reads `active`, and the caller prints
  `status: unarmed · the change kind is pending on <unit>`. With the kind landed and this body
  unchanged it raises, which reds the caller; unit 15 gives it its reader (F7). Observed by AC3.
- **S4** — The renderer-of-record table, `tools/playbook/renderers.toml`: one `[[target]]` row per
  instruction-file population, `paths` (globs) and `renderer`, the instruction files being the closed
  pathspec list `INSTRUCTION_PATHSPECS` in `instruction_units.py`: the charter `.memory-tree.conf`'s
  `CHARTER` names, `CLAUDE.md`, `.claude/agents/*.md`, `.claude/rules/*.md`, `.claude/skills/*/SKILL.md`,
  `skills/*/SKILL.md`, `{memory_root}/guides/*.md`, `{memory_root}/TEMPLATE-SPEC.md` and
  `{memory_root}/HYGIENE.md`. A file two rows claim, or none, is red, so each instruction file has exactly
  one renderer of record. Every population has its row (§4 Data model): the two `playbook:*` scopes;
  `kit-adopter` for a file a kit's adopter renders from that kit's template or role files and holds
  by its own `--check`; and `hand` for a file no renderer writes, today `.claude/rules/product.md` (`git grep -l
  "rules/product.md" -- tools/` prints nothing), `skills/deploy-governance/SKILL.md`,
  `skills/session-kickoff/SKILL.md`, `{memory_root}/guides/MERGE-BAR.md` and
  `{memory_root}/guides/SESSION-KICKOFF.md`. Where one glob holds files of two renderers, the
  `kit-adopter` row names its files by path (§8 F5). Observed by AC4.
- **S5** — The one renderer. `tools/playbook/render_playbook.py` is the renderer of record (the systems
  record's S11) for two scopes: `charter` (today's `render()`) and `entry-files` (`CLAUDE.md` and each
  other harness alias, the pointer or copy `adopt-agent-instructions.sh` writes today, its logic moved
  into the renderer). `python tools/playbook/render_playbook.py --render-scope <scope>` writes a scope
  and `--check-render --scope <scope>` compares its bytes; every write records the target's lock row
  (unit 12). `adopt-agent-instructions.sh` calls these for its render and its `--check`, so no second
  renderer writes an absorbed file. `--target` defaults to the repository root; the adopter passes its
  own, finds the renderer through the inline `resolve_kit_dir`, and exits 2 naming `playbook-render`
  where that finds none. The `entry-files` scope takes the adopter's `--aliases`, `--mode` and `--force`,
  and with none the aliases `renderers.toml` assigns it. Observed by AC5 and AC13.
- **S6** — The absorbed legs keep their names, the join key every leg-keyed file reads, and run the one
  gate scoped to the targets they covered: `playbook render wiring` the `charter` scope,
  `agent-instructions wiring` the `entry-files` scope, and `playbook parity` the `claims` scope, whose
  arms are `check-playbook-parity.sh`'s S1, S2 and S4, run by the gate until the charter's stated values
  render from sourced fact units. `playbook render selftest` keeps its argv and gains the scope arms in
  `render_playbook.py`'s selftest. `roles render wiring` and `roles render selftest` are not absorbed and
  keep their argvs, `bash {prefix}/roles/adopt-roles.sh --check` and `python
  {prefix}/roles/render_agents.py --selftest` (S11, F8). Observed by AC6.
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
  `refuse` reds every listed file. Read with `read_policy_value("instructions.legacy", root)`, unit
  19's `tools/playbook/policy_value.py:72` built to PLAY-dOrderedCharter-7 §4, `root` the tree under
  check, its first stdout line the value; unset, it answers the catalogue default, `shrink-only`
  (v2:1359; TOOL-dGroundRules-3 S2), and a refused read, the `PolicyRefused(key, line)` it raises
  (`policy_value.py:63-69`), reds the gate naming the key and the reader's line. The key's row in `tools/policy/catalogue.toml` lands with
  dGroundRules, owner dOrderedCharter, with no `summary` or `usage` and its name on the shrink-only
  `tools/policy/unsummarised-keys.txt` (TOOL-dGroundRules-1 S3, S6). This unit adds no row: it fills the
  row's `summary` and its `usage`, a line the row admits (`instructions.legacy = "refuse"`), and drains the
  name in the same commit with `python <prefix>/policy/policy.py lists --write`. Observed by AC8 and AC10.
- **S9** — The instruction-unit kind's factory and gate (deviation 71):
  `python tools/playbook/core.py new instruction-unit <name> --kit <kit> --type <t> --level <n> --text <line>`
  composes a row S1 passes and prints it with the unit-15 command that writes it, never writing a
  manifest itself; the kind's gate is S1's leg, and the kind's row in `tools/playbook/kinds.toml` names
  both, leaving `tools/playbook/core-pending.txt`. The row's factory is `python
  {prefix}/playbook/core.py new instruction-unit`, which `tools/playbook/core.py#run_new` serves in
  process through `OWN_FACTORY`, as it serves `skill`. No alias spells `unit`: a kind's name is never a
  namespace word (unit 65). The stale pending row `principle.p11` leaves that file in the same commit,
  since `instruction ladder (level is the one term)` and `instruction grammar (statement types,
  provenance lock)` enforce it now. Observed by AC9.
- **S10** — The legs and plants. Legs `instruction units (schema, one fact)` and `instruction render (one
  renderer of record)` in `tools/gate-legs.json`, each carrying `"enforces": ["principle.p11",
  "principle.p13"]`, the schema leg also `principle.p16` (F6), `"subject": "repo"`, and `"chunk"`
  `declarations` and `wiring` in that order; `python
  tools/playbook/instruction_units.py fixture --plant <case>` stages every case in a throwaway tree in the
  system temp directory. The legs' rows land in this pass, as unit 26 writes its leg's. Each leg gets:
  - an `[[exempt_leg]]` row in `tools/govkit/registry.toml` after the `edges` row (`:715`), in the shape
    of units 16, 19 and 28's (`:707`, `:711`, `:715`). An adopter cannot carry either leg: the schema
    leg grades the kit manifests gov authors, which an adopter copy-installs and never edits, the
    reason `layer dependencies` gives at `:708`. The render leg grades gov's own files against
    gov's `renderers.toml` and `instructions-legacy.txt`, while the absorbed wiring legs keep the
    adopter's renders (S6);
  - its `tools/govkit/subject-pins.tsv` row, which `python tools/govkit/govkit.py selfcheck --write`
    writes (`tools/govkit/govkit.py:2736-2742`);
  - its name in the `gate-legs` claim of `memory/map/features/playbook.md` (`:11`), with the files
    `python tools/codebase-map/gen_map.py --write` rewrites under `memory/map/generated/`.

  `python tools/run-gates/owed_rows.py --base HEAD` (unit 50) then prints none owed. Observed by AC1 to
  AC9 and AC11.
- **S11** — The agent render stays where it is (F10). `.claude/agents/*.md` and `.claude/roles.json` stay
  on `tools/roles/render_agents.py`, which keeps `--write`, `--check` and `--selftest`, and
  `adopt-roles.sh` calls it as it does today, with no lock row for those files. `renderers.toml` gives
  the agent files `kit-adopter`, `roles render wiring` holds them, and `render_playbook.py` has no
  `agents` scope. Observed by AC12.
- **S12** — The kit descriptors. `tools/agent-instructions/kit.toml` sets `requires =
  ["playbook-render"]` (F9), and the header of `adopt-agent-instructions.sh` names python and that kit in
  place of its no-hard-deps claim. `tools/roles/kit.toml` does not change: its `requires` and its two
  `[[generated]]` rows stand, since `adopt-roles.sh` reaches no renderer in this unit (F10). Observed by
  AC13.

## 3. Non-goals (OUT)

- The write command, `instructions.edit`, its manifest, its change record kind and the reader
  `read_change_records` gains: unit 15 (`cl-dClosedLoop-0045`), which S3 and S9 call.
- The charter's re-founded content: unit 2. Envelopes: unit 3. Load sets and budgets: unit 11. Step-scoped
  practice units in work orders: unit 21. The `code` slot: unit 27.
- Migrating the guides, the Skills and `.claude/rules/` onto units: each chain build migrates its own
  step's guides (IW-1); their renderers stay the record for them, beside the legacy list:
  `tools/lib/render-doc.sh`'s copies, kit/dogfood doc parity, review-protocol parity, each kit's skill wiring
  `--check` and govkit's placeholder render.
- The adopter upgrade step that moves agent-instructions' wiring: unit 31.
- The agent files' move onto the one renderer. `render_agents.py` keeps `--write` and `--check` for them,
  and `adopt-roles.sh` keeps calling it, until the owner rules on the default set (F10).
- The role static block template and the single carry: dBoundRoles; hook-message and harness-prompt
  templates: dWellOiledMachine.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-9` — `read_units`, `derive_unit_selection` and `render_units`, which every check and slot reads
- **consumes-from** `PLAY-dOrderedCharter-12` — `STATEMENT_TYPES` and the lock rows S8 reads and S5 writes
- **consumes-from** `PLAY-dOrderedCharter-7` — the record factory S3 reads change records through, the kinds register S9 updates, the `enforces` key with `principle` in the `enforces` row's `to` (`tools/playbook/edges.toml`), and the design of `read_policy_value`, its §4
- **consumes-from** external — dGroundRules, landed before this build run: `policy.py get` at the landed revision (TOOL-dGroundRules-2 S1, S7, `cl-dClosedLoop-0008`) with an unset key's catalogue default (TOOL-dGroundRules-3 S2), the `instructions.legacy` row and the shrink-only list S8 drains (TOOL-dGroundRules-1 S3, S6), and the mirror's `mirror --write` (TOOL-dGroundRules-5 S2, TOOL-dGroundRules-19 S1)
- **consumes-from** `PLAY-dOrderedCharter-24` — its S7 normaliser, `design_lib.derive_pin_hash`, the one-fact key's hash
- **consumes-from** `PLAY-dOrderedCharter-19` — the tag grammar and namespace registry S1 grades `tag`, `scope` and `required-by` against, and `read_policy_value` in `tools/playbook/policy_value.py`, which S8 reads `instructions.legacy` through
- **hands-off** `PLAY-dOrderedCharter-15` — the write command S9 prints, the change records S3 derives status from, and the body of `read_change_records`, which it replaces when it lands the `change` kind (F7)
- **hands-off** external — the `agents` scope, the agent files' move onto the one renderer, parked for the owner's ruling on widening the default set; until then `render_agents.py` keeps `--write` and `--check` for those files (F10)
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
paths = ["CLAUDE.md"]
renderer = "playbook:entry-files"

[[target]]   # each from its kit's template or role files, by that kit's adopter
paths = [".claude/agents/*.md", ".claude/skills/*/SKILL.md",
         "{memory_root}/TEMPLATE-SPEC.md", "{memory_root}/HYGIENE.md",
         "{memory_root}/guides/ANNOTATION-STYLE.md", "{memory_root}/guides/BUILD-METHOD.md",
         "{memory_root}/guides/PLAYBOOK-TEMPLATE.md", "{memory_root}/guides/REVIEW-PROTOCOL.md",
         "{memory_root}/guides/UNATTENDED-ASKS.md", "{memory_root}/guides/UNATTENDED-PROTOCOL.md",
         "{memory_root}/guides/UNATTENDED-STOPS.md", "{memory_root}/guides/UNATTENDED-VERBS.md"]
renderer = "kit-adopter"

[[target]]   # no renderer writes these; each is edited by hand
paths = [".claude/rules/*.md", "skills/*/SKILL.md", "{memory_root}/guides/MERGE-BAR.md",
         "{memory_root}/guides/SESSION-KICKOFF.md"]
renderer = "hand"
```

The `kit-adopter` paths are the renders at HEAD: `tools/memory-tree/adopt-memory-tree.sh:566-569`
pairs four templates with `HYGIENE.md`, `TEMPLATE-SPEC.md` and two guides,
the unattended kit's five guide templates and `tools/workflows/REVIEW-PROTOCOL.template.md` give six
more guides, and each of the seven `.claude/skills/*/SKILL.md` is named by its kit's adopter. The agent
files are `adopt-roles.sh`'s, through `render_agents.py` (S11). The build pass
re-derives the list and the table holds it both ways.

The work-order template, `tools/playbook/templates/work-order.template.md`, holds two second-level
headings, `Role` and `Task`, and four slot lines, each `<!-- slot: <name> -->` on its own line:

| Slot | Under | Filled with |
|---|---|---|
| `role` | `Role` | the role's static block, `render_role`'s output today |
| `opening` | `Task` | the build and unit sentence and the optional-input line |
| `reads` | `Task` | one `### <key>` block per read key, in the order `reads` names |
| `charter-blocks` | `Task` | `render_charter_blocks`' output for the role's `rules:` |

### Inventory

Minted: the verbs `schema` and `one-fact`, `derive_status`, `read_change_records`,
`INSTRUCTION_PATHSPECS`, the files
`tools/playbook/renderers.toml`, `tools/playbook/instructions-legacy.txt` and
`tools/playbook/templates/work-order.template.md`, the renderer flags `--render-scope`, `--check-render`
and `--scope` with the scopes `charter`, `entry-files` and `claims`, the slot line grammar, the
factory verb `new instruction-unit`, and the legs `instruction units (schema, one fact)` and `instruction render (one
renderer of record)`. The legacy list's seed is DERIVED at the build pass from `INSTRUCTION_PATHSPECS`; at
`4e8f80cdf` it would hold 33 files (PINNED, 2026-10-23: `AGENTS.md`, `CLAUDE.md`, nine agent files, one
rule, seven installed Skills, two authored Skills, ten guides, `TEMPLATE-SPEC.md` and `HYGIENE.md`).

### Migration

The build pass seeds the legacy list and moves `adopt-agent-instructions.sh`'s pointer and copy writes into
the renderer, the script calling it. Rendered bytes do not change: the scopes reproduce today's outputs.

### Rollout

Live at landing, at order 15, after unit 9 (order 14); units 15 (order 16), 2 (order 20) and 3 (order 18)
build on it. S3's status arm prints `unarmed` from landing until unit 15 gives `read_change_records` its
reader. S8's row fill lands as two commits: the fill with the list drain, then
`.governance/policy.json` alone as `policy.py mirror --write` regenerates it, since a catalogue edit stales
the mirror (TOOL-dGroundRules-5 S1, S2) and the guard admits a mirror commit only when the policy file and
the catalogue equal HEAD (TOOL-dGroundRules-19 S1).

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
- `tools/agent-instructions/adopt-agent-instructions.sh`
- `tools/agent-instructions/kit.toml`, `requires`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`, the two `[[exempt_leg]]` rows
- `tools/govkit/subject-pins.tsv`, by `govkit.py selfcheck --write`
- `memory/map/features/playbook.md`, the legs' claim
- `memory/map/generated/`, the files `python tools/codebase-map/gen_map.py --write` rewrites
- `tools/policy/catalogue.toml`, the existing row filled
- `tools/policy/unsummarised-keys.txt`, drained by `lists --write`
- `.governance/policy.json`, the second commit

Not touched, under F10's (e): `tools/roles/render_agents.py` keeps `--write` and `--check` for the agent
files, and `tools/roles/adopt-roles.sh`, its fixture and `tools/roles/kit.toml` stand as they are.

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
- error / empty / loading states: an instruction file with no renderer row is red; a refused
  `instructions.legacy` read is red naming the key; an empty unit population prints `unarmed`, never
  green, and so does the status arm while the `change` kind is pending.
- observability: each red names the path or tag, the arm and the remedy.
- risks: `adopt-agent-instructions.sh` now reaches the playbook kit, an edge inside `layer.instruction`.
  Under AC5 that adopter keeps no fallback, so no target wires its aliases with an old renderer. Where
  `render_playbook.py` is absent it exits 2 naming `playbook-render`; where the renderer predates
  `--render-scope`, `tools/playbook/render_playbook.py#main`'s parser exits 2. Either way nothing is
  written. `requires` orders `playbook-render` first and makes `apply` refuse its absence (F9); a receipt
  that already holds the kit without it is unit 31's step. The roles adopter does not move, so a default
  install renders as it does today (F10).
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
  `retired:none` for a retirement over records the case passes in, a row typing `status` reds `schema`,
  and a retired unit a template selects reds the render. `read_change_records` over the tree returns no
  record and the render prints the `status: unarmed` line naming `PLAY-dOrderedCharter-15`; with the
  case's `KINDS` row for `change` landed, it raises and the render reds.
  Red when: a status is read from the row, a retired unit renders, or the read stays unarmed once the
  kind lands.
- **AC4** — When `python instruction_units.py fixture --plant renderers` plants a guide no
  `renderers.toml` row claims and an agent file two rows claim, `--check-render` exits 1 naming each.
  Red when: an instruction file has no renderer of record, or two.
- **AC5** — When `python tools/playbook/render_playbook.py --check-render --scope entry-files` runs over
  the tree, it exits 0 with the bytes `adopt-agent-instructions.sh` wrote before this unit;
  `git grep -n -e '--render-scope' -e '--check-render' -- tools/agent-instructions/adopt-agent-instructions.sh`
  prints a line; `git grep -n -F 'render_agents.py' -- tools/roles/adopt-roles.sh` still prints `:20` and
  `:323` among its lines; and `git grep -n -F '_wire_pointer_or_copy' -- tools/agent-instructions/adopt-agent-instructions.sh`
  prints nothing, where today it prints `:137`, `:139`, `:142`.
  Red when: an absorbed file is written by a second renderer, its bytes move, or the roles adopter leaves
  `render_agents.py` before the owner's ruling.
- **AC6** — When `python -c "import json, sys; print({l['name']: l['argv'] for l in json.load(open(sys.argv[1], encoding='utf-8')) if l['name'] in ('playbook render wiring', 'roles render wiring', 'agent-instructions wiring', 'playbook parity', 'roles render selftest')})" tools/gate-legs.json`
  runs, each of the five names is present; `playbook render wiring`, `agent-instructions wiring` and
  `playbook parity` each run `--check-render` with their scope, directly or through their kit's `--check`;
  and `roles render wiring` and `roles render selftest` print today's argvs, `adopt-roles.sh --check` and
  `render_agents.py --selftest`.
  Red when: a name is gone, an absorbed leg still runs its own renderer, or a roles leg moves before the
  owner's ruling.
- **AC7** — When `python instruction_units.py fixture --plant work-order` runs, `handoff.py
  render --stdout` over the case's fixture build prints bytes equal to the expected output the case pins
  from the render before the template, and
  `python instruction_units.py fixture --plant slots` expands a `<!-- units: role.builder -->`
  slot into the selected units' lines.
  Red when: the template changes a handoff's bytes, or a slot renders prose of its own.
- **AC8** — When `python instruction_units.py fixture --plant legacy` plants an instruction file neither
  rendered from units nor on `instructions-legacy.txt`, and a listed file whose lock row lists units, the
  gate reds both under `shrink-only`, and under `refuse`, set in the fixture's committed policy file,
  reds every listed file; with that file, the only commit, setting `instructions.legacy = "loose"`,
  which the row refuses and no valid revision precedes (TOOL-dGroundRules-4 S5), the gate reds naming
  `instructions.legacy`.
  Red when: an unlisted hand-written document passes, the list grows unseen, or a refused read grades
  under a default.
- **AC9** — When `python tools/playbook/core.py new instruction-unit demo --kit playbook-render --type directive
  --level 3 --text "MUST demo."` runs, it prints one row `schema` passes and the unit-15 command that writes
  it, the manifest is unchanged, and `core.py kinds` reads the instruction-unit kind with its factory and
  gate and exits 0. `git grep -n -F 'principle.p11' -- tools/playbook/core-pending.txt` prints nothing, and
  `python tools/playbook/core.py meta-check` prints no stale row naming that principle.
  Red when: the factory writes a manifest, its row fails the schema, its gate leg lacks a tag the kind
  binds, or the stale pending row stays.
- **AC10** — When `python -c "import tomllib; print([(r['owner'], bool(r.get('summary')), bool(r.get('usage'))) for r in tomllib.load(open( 'tools/policy/catalogue.toml' , 'rb'))['key'] if r['name'] == 'instructions.legacy'])"`
  runs after the pass, it prints one row, `dOrderedCharter`, `True`, `True`; `git grep -n -x -F
  "instructions.legacy" -- "tools/policy/unsummarised-keys.txt"` finds no line; `python
  "tools/policy/policy.py" lists --check` exits 0; and `git grep -n -F
  'read_policy_value("instructions.legacy"' -- tools/playbook/render_playbook.py` finds one line.
  Red when: a row is added, the row keeps no summary or usage, the name stays on the shrink-only list,
  or the key is read in a shape the reader-coverage arm does not count.
- **AC11** — When
  `git grep -n -F -e "instruction units (schema, one fact)" -e "instruction render (one renderer of record)" -- tools/govkit/subject-pins.tsv tools/govkit/registry.toml memory/map/features/playbook.md memory/map/generated/MAP.md`
  runs after the pass, each name is printed in each of the four files, the registry's a `name =`
  line of an `[[exempt_leg]]` row.
  Red when: a leg lands unpinned, unclaimed, missing from the dossier, or claimed with the map not
  regenerated.
- **AC12** — When `python tools/roles/render_agents.py --check` runs, it exits 0;
  `python -c "import tomllib; print([t['renderer'] for t in tomllib.load(open('tools/playbook/renderers.toml', 'rb'))['target'] if '.claude/agents/*.md' in t['paths']])"`
  prints `['kit-adopter']`; and `python tools/playbook/render_playbook.py --render-scope agents` exits 2
  naming the scope and writes nothing.
  Red when: an agent file gains a second renderer of record, or the kept render stops holding it.
- **AC13** — When `python -c "import tomllib; d = lambda k: tomllib.load(open(f'tools/{k}/kit.toml', 'rb')); print(d('agent-instructions')['requires'], {g['generator'] for g in d('roles')['generated']})"`
  runs, it prints `['playbook-render']` and `{'render_agents.py'}`; `git grep -n -F 'No hard deps' --
  tools/agent-instructions/adopt-agent-instructions.sh` prints nothing; `python tools/govkit/govkit.py
  selfcheck` names no finding on `agent-instructions`; and `python instruction_units.py fixture --plant
  no-renderer` runs that adopter in a tree holding no playbook kit, where it exits 2 naming
  `playbook-render` and writes no target.
  Red when: the agent-instructions adopter rests on a kit its descriptor does not name, a generated row
  names a generator no file backs, or an adopter with no renderer writes a target.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `agent-instructions self-test` · `playbook render wiring` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `core meta-check` · `core kinds` · `core selftest` · `govkit selfcheck` · `docs` · `agent-instructions wiring` · `playbook parity` · `roles catalogue` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `spec tokens (a spec's own names resolve)` · `policy fixtures` · `govkit selftest` · `govkit refusal join` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness`

New arm: tools/playbook/instruction_units.py · covers AC1 AC2 AC3 AC4 AC7 AC8 AC13 · the `schema`, `one-fact`, `status`, `renderers`, `work-order`, `legacy` and `no-renderer` fixture cases, each failing case staged by its plant · none

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
- **F5** — S4 reds an instruction file no row claims, and five have no renderer: `.claude/rules/product.md`,
  the two authored Skills and two guides. Which row claims a hand-written file? Options: (a) a
  `renderer = "hand"` row naming them, the `kit-adopter` row naming its guides by path; (b) a listing
  on `instructions-legacy.txt` is the claim; (c) S4 exempts a file no renderer writes.
  RESOLVED (agent, 2026-11-03, delegated): (a), rung 3. (b) lost on the seed: the list holds every file
  not rendered from units, 33 at `4e8f80cdf` with `AGENTS.md`, `CLAUDE.md` and nine agent files, all
  with renderers, so a listing cannot say which renderer, and one list would answer two questions. (c)
  lost to `[gate]`: an exemption is a population nobody grades, so a new instruction file would pass
  unclaimed. Under (a) a new guide reds until a row names it, which is the check. widens: none ·
  relaxes: none
- **F6** — `kind.instruction-unit` binds `principle.p13` and `principle.p16`, S10 gave its gate leg p11
  and p13, and `tools/playbook/core.py#check_kind_row` reds a gate leg lacking a bound tag. Options: (a)
  the schema leg adds `principle.p16`; (b) the kind's `binds` loses it.
  RESOLVED (agent, 2026-11-04, delegated): (a). All 17 rows of `tools/playbook/kinds.toml` bind p16
  (PINNED, 2026-11-04), so (b) would make this kind the one exception and amend a register this unit
  does not own. Under (a) the leg joins `core skills conformance` and `core practices conformance`, each
  a kind's gate carrying p16, and it earns the tag: a row S1 refuses reaches no manifest by any route.
  widens: none · relaxes: none
- **F7** — S3 reads change records as the kind unit 15 registers, unit 15 builds after this unit, and
  `tools/memory-tree/build_records.py#KINDS` holds the kind as pending. What do the tree reads take
  until then? Options: (a) no records, every unit active with an `unarmed` line, unit 15 wiring the
  reader; (b) this unit registers the kind; (c) this unit builds after unit 15.
  RESOLVED (agent, 2026-11-04, delegated): (a). (b) lost to section 3, which gives the kind to unit 15,
  whose S7 owns its fields and its action set. (c) lost to a cycle: unit 15 consumes S1, S2 and the
  renderer from this unit. (a) loses nothing, since no change record can exist before unit 15 lands the
  kind, so `active` is the true status and not a default. The raising branch keeps `unarmed` from
  outliving the pending row, so the empty population is never read as coverage. widens: none ·
  relaxes: none
- **F8** — Does `roles render selftest` keep its `render_agents.py --selftest` argv or move to
  `render_playbook.py`? Options: (a) it keeps it, and `render_playbook.py`'s selftest gains only the
  scope arms; (b) its arms and argv move.
  RESOLVED (agent, 2026-11-04, delegated): (a). (b) lost to `playbook render selftest`, a leg of subject
  `kit` that ships to a target holding no roles kit, where the moved arms could not run; making
  `playbook-render` require `roles` would be a cycle if the owner later takes F10's (a), which
  `tools/govkit/govkit.py#derive_install_order` refuses. The arms drive `run_mode` over a roles catalogue,
  so they stay beside it, and under F10's (e) `run_mode` does not move either. widens: none · relaxes:
  none
- **F9** — The agent-instructions adopter will call `render_playbook.py`, and its kit declares `requires
  = []`. Options: (a) `requires = ["playbook-render"]`; (b) a `requires_if` row, the adopter keeping its
  shell writes where the renderer is absent; (c) no edge, the adopter refusing at run time alone.
  RESOLVED (agent, 2026-11-04, delegated): (a). (b) fails AC5, which greps those writes gone. (c) lets
  `apply` land a kit its adopter cannot run, the state
  `tools/govkit/govkit.py#derive_unsatisfied_requires` exists to refuse. The kit is outside the default
  set, so the edge refuses no default install, and unit 31 names `playbook-render` its successor. The
  cost is stated: a target taking this kit alone now selects `playbook-render` and `playbook` too.
  widens: none · relaxes: none
- **F10** — `roles` is in the default set of `tools/govkit/registry.toml` and `playbook-render` is not, so
  moving the agent render onto `render_playbook.py` would leave a default install with no renderer for
  its agent types or for `.claude/roles.json`, the index the hooks kit's write gate arms on. What does
  this unit do? Options: (a) the `requires` of `tools/roles/kit.toml` gains `playbook-render` and the
  default set gains that entry; (b) it gains `playbook-render` alone; (c) a `requires_if` row, the adopter
  writing no agent type where the renderer is absent; (d) `adopt-roles.sh` falls back to `render_agents.py`
  there; (e) a later unit takes the `agents` scope, and the agent files take the `kit-adopter` row until
  it lands.
  RESOLVED (agent, 2026-11-04, delegated): (e), the main loop's ruling, which re-scopes S5, S6, AC5 and
  AC6 and keeps `render_agents.py --write` and `--check` for the agent files. (a) is the owner's and
  stays parked: widening the default set changes what every install lands
  (`tools/govkit/govkit.py#derive_default_gained`), and this run does not widen it. Whether a default
  `apply` would complete under (a) is UNVERIFIED: the default-install shape in `tools/govkit/matrix.py`
  declares five answers, and the render refuses on an absent `asked` key. (b) fails `govkit acceptance
  matrix`: `tools/govkit/govkit.py#derive_unsatisfied_requires` makes `apply` refuse, and that shape
  asserts `apply` completes. (c) unarms the role-aware write gate on default installs, widening a write
  surface this tier did not price. (d) keeps two writers behind one scope. The cost of (e) is stated:
  `cl-dClosedLoop-0050` names `roles render wiring` among the legs absorbed, so that half stays undone
  under this spec's `whole` carry until the owner rules. widens: none · relaxes: the roles half of the
  clause, until the owner rules

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the spec run's carrier of `cl-dClosedLoop-0050`.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-43, PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-50, PLAY-dOrderedCharter-55.
- rev-4 · 2026-10-24 · §2 S8 · §3 Edges · §4 Rollout, Files touched · §5 · AC8, AC10 · re-grounded on the parents' landed specs by `2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck` U3 and U4: `instructions.legacy` is read with `policy.py get` through PLAY-dOrderedCharter-7's `read_policy_value`, a refused read reds the gate, and the landed row is filled and drained, never added.
- rev-5 · 2026-11-03 · §7 · from `2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md` Item 2: the leg line names `policy fixtures`, whose guard a §4 Files touched path trips, the guards hit the spec-token check reads with DEFERRED as live.
- rev-6 · 2026-11-03 · S2 S4 S8 S10 · §3 Edges · §4 · AC5 AC9 AC10 AC11 (new) · §7 · §8 F5
  (new) · §10 · from `2026-11-03-prompt-PLAY-dOrderedCharter-9-drift-fold-brief.md` items 20-1 to
  20-7: the two new legs' exempt, pin and dossier rows land in this pass with the legs they trip; every
  instruction population has its renderer row, a hand-written file `hand`'s; AC5 greps the calls and
  the removed writes; the kit id is `playbook-render`; the reader is unit 19's `read_policy_value`
  refusing by `PolicyRefused` and the normaliser `design_lib.derive_pin_hash`; AC10's untracked note
  goes; and §10's line is re-read.
- rev-7 · 2026-11-04 · S3 S5 S6 S9 S10 S11 (new) S12 (new) · section 3 · section 4 · section 5 · AC3 AC6 AC9
  AC12 (new) AC13 (new) · section 7 · section 8 F6 to F10 (new) · section 10 · from
  `2026-11-04-prompt-PLAY-dOrderedCharter-20-divergence-brief.md` items 1 to 7: the factory is `core.py new
  instruction-unit`; the schema leg enforces p16; the tree reads are unarmed until unit 15 wires
  `read_change_records`; agent-instructions requires `playbook-render`, the roles `requires` stays open at
  F10, and the section 5 risk is rewritten; `render_agents.py` loses its writer, the fixture, generators
  and usage row follow, and `roles render selftest` keeps its argv; the stale `principle.p11` row goes.
- rev-7 · 2026-11-04 · S4 S5 S6 S11 S12 · section 1 · section 3 · section 4 · section 5 · AC5 AC6 AC12 AC13 ·
  section 8 F8 F10 · section 10 · the main loop's ruling on F10, option (e), over the entry above: the
  `agents` scope stays on `render_agents.py`, which keeps `--write` and `--check`, the agent files take
  `kit-adopter`, and the roles adopter, its fixture, its generators, its usage row and `help/roles.md` stand;
  the owner's option (a) is parked; F9 stands.

## 10. Reuse audit

The seams extended are `render()` in `tools/playbook/render_playbook.py` (line 1024), the renderer of record
the systems record's S11 names; `render_handoff` (`tools/roles/handoff.py:312`), whose
section order becomes the work-order template; and `_wire_pointer_or_copy` in
`tools/agent-instructions/adopt-agent-instructions.sh`, whose pointer and copy writes move into the
renderer. `render_agent_file` (`tools/roles/render_agents.py:144`) and `run_mode` (line 269) stay the roles
render, which this unit leaves in place (F10). The legacy list follows the shrink-only list idiom of `tools/dead-path-waivers.txt`. S9 extends
`tools/playbook/core.py#run_new` through `OWN_FACTORY`, and S3's reader reads
`tools/memory-tree/build_records.py#KINDS`. `python
tools/codebase-map/reuse_lookup.py "refuse an instruction file whose bytes differ from its render or that no
renderer produces"` ranked `render` (ten sites, `render_playbook.py` among them) and name-token matches,
which confirms the four renderers scout A listed and finds no renderer-of-record table, so none fits that.

Recall terms used: `python tools/memory-recall/query.py "which renderer of record writes each instruction file and how is the render gate armed with a legacy list" --terms "renderer of record render gate legacy list shrink-only IW-1 playbook parity render wiring one-fact schema"`
