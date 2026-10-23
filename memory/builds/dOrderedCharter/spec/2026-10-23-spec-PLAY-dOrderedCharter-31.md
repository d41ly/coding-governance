# PLAY-dOrderedCharter-31 — this build's own upgrade steps: the agent-instructions wiring to the one renderer, adopter rules into the overlay, the seeded template's succession row, the census's change records and the `map_lib` deprecation

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 36 · advances PLAY-dOrderedCharter-38

**Carries:** cl-dClosedLoop-0061@bf1a53b5 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-c.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-c.md) | research | PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

Every adopter-visible surface this build takes away ships with the row that carries an adopter across
it, through dSafePassage's step kind (`cl-dClosedLoop-0018`), so `update` walks an adopter from today's
install to this build's and dSafePassage's step gate stays green only because each row exists. Five
surfaces move: the agent-instructions kit, whose wiring the one renderer absorbs (unit 20); the
repository's `[charter] adopter_rules`, which become level-0 `repo.` units of its overlay (unit 32); the
seeded charter template (unit 34 stops reading it); the practices the census moves out of the shipped
set (unit 34); and the names `map_lib` re-exports after unit 19 moves them. P38: "a build that changes
what an adopter can see ships its successor with an upgrade step that runs up and down".

## 2. Scope (IN)

- **S1** — The agent-instructions kit carried to its successor. Its registry entry
  (`tools/govkit/registry.toml:106-107`) and its `[[exempt_leg]]` row (`:523`) leave the registry, its
  directory `tools/agent-instructions/` leaves the tree, its two legs leave `tools/gate-legs.json`
  (`:293`, `:382`) with their rows in `tools/govkit/subject-pins.tsv`,
  `tools/run-gates/ceiling-evidence.txt` and `tools/run-gates/selftest-budgets.txt`, and a
  `[[retired]]` row names it: `id = "agent-instructions"`, `successor = "playbook-render"`, `surfaces`
  the members `step_gate.py --list` prints for the entry at the base. `CODEX_MAX` moves into the module
  unit 20 absorbed the wiring into, and unit 6's check and unit 34's render read it there.
  **Readers:** by name: `tools/govkit/registry.toml`, `tools/gate-legs.json`,
  `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt`,
  `tools/run-gates/selftest-budgets.txt`, `tools/govkit/selftest.py`, `tools/govkit/govkit.py`,
  `tools/template-size-limits.txt`, `README.md`, `WIRE-INTO-PROJECT.md`, `AGENTS.md`,
  `.governance/deploy.toml`, `.claude/rules/product.md`, `.lexicon.conf`, `.memory-tree.conf`,
  `memory/map/baseline.toml` and `memory/map/features/roles.md`, each a hit of §4's first query at
  the base · by value: `tools/check-template-size.sh`'s 32 KiB hold through `CODEX_MAX` (unit 6's)
  and `print_size_note`'s announce, which the render's harness-limit refusal replaces (unit 34).
  Observed by AC1, AC2 and AC3.
- **S2** — The by-value inventory, derived by §4's queries over the tree at the pass and never copied
  into a file; root `README.md`'s line 17 is among its hits. Each hit is re-pointed to the renderer,
  re-worded where it states where the wiring lives, or kept where it narrates history, and the pass
  commit's `Decided:` trailer names each kept hit. Observed by AC2.
- **S3** — The `map_lib` re-export declared as a deprecation. A `[[class]]` row `module-export` joins
  dSafePassage's class registry `tools/govkit/surface-classes.toml`: its reader returns each name
  `tools/codebase-map/map_lib.py` re-exports from the join factory unit 19 moves to `tools/lib/`, and its
  plant stages one re-export taken away, so the names leave only with a row naming them. How long they
  stay is unit 19's hold under `install.deprecation-window`. Observed by AC4.
- **S4** — The adopter rules into the overlay, by a step whose down restores them. An `[[upgrade]]` row
  `playbook/adopter-rules-to-overlay` in `tools/govkit/entries/playbook.kit.toml`, its program
  `tools/govkit/steps/adopter_rules_to_overlay.py`: its up turns each `- ` line of
  `[charter] adopter_rules` in `.governance/deploy.toml` into one level-0 `repo.` unit of
  `.governance/instructions.toml` and takes the key out of the descriptor; its down restores both files
  byte-identical from the before-image; its witness holds when the key is absent and every line it held
  is a unit's text. The `ADOPTER_RULES` placeholder row (`tools/govkit/entries/playbook.kit.toml:273-277`)
  leaves the descriptor with it, and a `[[class]]` row `charter-key` (each `[[placeholder]]` key the
  playbook descriptor declares) arms the step gate for it. **Readers:** by name:
  `tools/govkit/entries/playbook.kit.toml`, `coding-governance-agents.template.md`,
  `tools/playbook/render_playbook.py` (its self-test fixtures), `tools/playbook/README.md`,
  `WIRE-INTO-PROJECT.md`, `.claude/rules/product.md` and `.governance/deploy.toml` · by value:
  `read_charter_table` (`tools/playbook/render_playbook.py:809`) reading `adopter_rules` into the
  rendered section, which unit 34's composition replaces with the overlay's level-0 units. Observed by
  AC5, AC6 and AC7.
- **S5** — The seeded charter template's succession row. A `[[retired]]` row in
  `tools/govkit/registry.toml`, `id = "playbook/seeded-template"`, `successor = "none"`, `surfaces` the
  members the step gate lists for the seed rule at the base, and the seed's `[[files]]` rule
  (`tools/govkit/entries/playbook.kit.toml:23-26`) and its hole leave the playbook descriptor. An
  adopter's seeded copy that it edited becomes `retired-edited`, kept and ordered as
  `install.retired-edits` says (TOOL-dSafePassage-9), never deleted; one it never edited reads
  `withdrawn`. Its readers are inventoried by path and by value by §4's second query.
  **Readers:** by name: `tools/govkit/entries/playbook.kit.toml`, `tools/govkit/govkit.py`, `tools/govkit/matrix.py`,
  `tools/govkit/selftest.py`, `tools/check-placeholders.sh`,
  `tools/govkit/entries/check-microformats.kit.toml`, `tools/playbook/README.md` and
  `WIRE-INTO-PROJECT.md`, each spelling `playbook_path` at the base · by value: the seed row's
  `reseed-available` grade (`tools/govkit/govkit.py:9989-9990`), which no longer has a row to grade.
  Observed by AC8 and AC9.
- **S6** — A change record for every unit the census moves out of the shipped set (unit 34, S8), in
  the change record kind unit 15 writes (S12, S13), each `mark = semantic` and `successor = none`, so
  the step gate's gov unit-tag class (joined by unit 33) is witnessed by its one witness, the record.
  Observed by AC10.
- **S7** — Gov first. Every step of S1, S4 and S5 runs on gov's own tree before any adopter meets it,
  as `cl-dClosedLoop-0025` runs every step in the lander's prepared merge, and gov's source-mode
  receipt lists each step id. Observed by AC11.
- **S8** — The page: `help/upgrade-steps.md` (TOOL-dSafePassage-1's) gains one section naming this
  build's steps and what each does to an adopter's tree. Observed by AC12.

## 3. Non-goals (OUT)

- The step kind, its reader, the walk, the before-image helpers, the step gate and its nine classes,
  `retired-edited` and the order writer: dSafePassage's (TOOL-dSafePassage-1, -2, -9, -10). This unit
  writes rows in their grammar and two class rows through their extension point.
- Absorbing the wiring into the renderer and the render gate: unit 20's. Composing the project block
  and dropping the seeded template as the render's input: unit 34's. The census's rulings: unit 34's.
- The `map_lib` re-export itself, its window and the shim for the moved module import: unit 19's.
- Taking a re-export away when its window closes: dConvergedCharter.
- A legacy block for an adopter's own instruction files: dLinkedLibrary.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-20` — the renderer that absorbed the agent-instructions wiring, which the kit's successor ships
- **consumes-from** `PLAY-dOrderedCharter-32` — the overlay file and the level-0 `repo.` unit grammar the adopter-rules step writes, through `write_overlay_units`
- **consumes-from** `PLAY-dOrderedCharter-34` — the seeded template no longer read and the census's moved units
- **consumes-from** `PLAY-dOrderedCharter-15` — the change record kind S6 writes
- **consumes-from** `PLAY-dOrderedCharter-33` — the step gate's gov unit-tag class, witnessed by the change record
- **consumes-from** `PLAY-dOrderedCharter-19` — the join factory's move and `map_lib`'s re-export
- **consumes-from** `PLAY-dOrderedCharter-6` — the check that reads `CODEX_MAX`, re-pointed with the constant
- **consumes-from** external — dSafePassage's step kind, step gate, class registry and `retired-edited` (TOOL-dSafePassage-1, -9, -10), built before this build's build run; and dGroundRules' minimal guard (`cl-dClosedLoop-0012`)
- **hands-off** `PLAY-dOrderedCharter-39` — S1's leg removal and moving list: the agent-instructions wiring leg keeps its name on the renderer, and the card import moves by name beside CODEX_MAX (finding 1)
- **consumes-from** `PLAY-dOrderedCharter-46` — the candidate read, which S4's step re-renders through over the overlay it has just written (finding 80)
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 10, 21 and 71, which that batch unit corrects after this unit lands, each by the item its report id names

## 4. Design

### The rows

```toml
# tools/govkit/registry.toml
[[retired]]
id = "agent-instructions"
successor = "playbook-render"
surfaces = ["entry:agent-instructions"]          # plus every member `step_gate.py --list` prints for it

[[retired]]
id = "playbook/seeded-template"
successor = "none"
surfaces = []                                     # every member the gate lists for the seed rule at BASE

# tools/govkit/entries/playbook.kit.toml
[[upgrade]]
id = "playbook/adopter-rules-to-overlay"
up = ["python", "{gov}/govkit/steps/adopter_rules_to_overlay.py", "up", "{target}"]
down = ["python", "{gov}/govkit/steps/adopter_rules_to_overlay.py", "down", "{target}"]
witness = ["python", "{gov}/govkit/steps/adopter_rules_to_overlay.py", "witness", "{target}"]
surfaces = ["charter-key:ADOPTER_RULES"]
needs-target = false

# tools/govkit/surface-classes.toml
[[class]]
id = "charter-key"
reader = "govkit/steps/adopter_rules_to_overlay.py:read_charter_keys"
plant = "govkit/steps/adopter_rules_to_overlay.py:write_charter_key_plant"
summary = "each [[placeholder]] key the playbook descriptor declares, which a target answers in deploy.toml"

[[class]]
id = "module-export"
reader = "codebase-map/map_lib.py:read_reexports"
plant = "codebase-map/map_lib.py:write_reexport_plant"
summary = "each name map_lib re-exports from the join factory, held for install.deprecation-window"
```

The `surfaces` lists are written from `python tools/govkit/step_gate.py --list` run at the base, so
every member is spelled as the gate spells it and none is typed from memory.

### The adopter-rules step

The up reads `.governance/deploy.toml` with `tomllib`. No `[charter]` table or no `adopter_rules` key:
exit 0. Otherwise it writes the before-image of both files (TOOL-dSafePassage-1's helpers in
`tools/govkit/upgrade_steps.py`, imported by its own file's path), then, per `- ` line in order, one
overlay row:

```toml
[[unit]]
tag = "repo.<seg>"        # seg: the line lowercased, every run outside [a-z0-9] folded to "-", cut at 40 bytes, "-2" etc. on a collision
level = 0
type = "directive"
text = "<the line, its leading '- ' cut>"
```

in S10's row grammar, validated by unit 32's overlay reader before it is written, and it then takes the
`adopter_rules` key out of `deploy.toml` by a line edit that leaves every other byte in place. A line
over the one-line cap or failing the reader refuses with exit 1 and writes nothing. The down restores
both files from the before-image under its refusal rule: a file whose bytes are neither the image's
before nor its after is named and left.

**Who writes.** The step writes the overlay and `deploy.toml` as `update` runs it, which is the write
the clause names ("by a step whose down restores it"), not an agent's edit through unit 15's command.
The minimal guard refuses agent writes to both files (`cl-dClosedLoop-0012`); a step run by `update`
in the lander's prepared merge is not one, and where the landed guard reads otherwise the build run
files the admission ask, as TOOL-dGroundRules-13 did for dSafePassage's budgets step.

### The inventory queries

Run at the pass, before the first edit and after the last:

```bash
git grep -n -F -e "agent-instructions" -e "adopt-agent-instructions" -e "CODEX_MAX" -- . \
  ':!memory/builds' ':!memory/ledger' ':!memory/map/generated' ':!tools/agent-instructions/'
git grep -n -F -e "playbook_path" -e "coding-governance-agents.template.md" -e "reseed-available" -- . \
  ':!memory/builds' ':!memory/ledger' ':!memory/map/generated'
```

The first is the agent-instructions kit's population, by path and by value; at `ce13efbe` it returns
the files S1's Readers line lists, `README.md:17` among them. The second is the seed's; its hits that
read the gov-root template unit 20 keeps are kept, and the ones that read a seeded copy are re-pointed
or re-worded. The generated map is re-rendered by `python tools/codebase-map/gen_map.py --write`, never
edited. Both counts are DERIVED by the query at the pass.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| the `[[retired]]` ids `agent-instructions` and `playbook/seeded-template` | `tools/govkit/registry.toml` | none |
| the step id `playbook/adopter-rules-to-overlay` | `tools/govkit/entries/playbook.kit.toml` | none |
| `tools/govkit/steps/adopter_rules_to_overlay.py` (step program) | govkit kit | the lexicon's naming predicates |
| `read_charter_keys`, `write_charter_key_plant`, `read_reexports`, `write_reexport_plant` | their modules | the lexicon's naming predicates |
| the class ids `charter-key` and `module-export` | `tools/govkit/surface-classes.toml` | none |

### Files touched (estimate)

- `tools/govkit/registry.toml`
- `tools/govkit/entries/playbook.kit.toml`
- `tools/govkit/surface-classes.toml`
- `tools/govkit/steps/adopter_rules_to_overlay.py` (new)
- `tools/codebase-map/map_lib.py` (the class's reader and plant)
- `tools/gate-legs.json`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/ceiling-evidence.txt`
- `tools/run-gates/selftest-budgets.txt`
- `tools/agent-instructions/` (leaves the tree)
- `tools/check-template-size.sh` (re-pointed to `CODEX_MAX`'s new home)
- `.governance/deploy.toml` and `.governance/instructions.toml` (gov first, written by the step)
- `README.md`, `WIRE-INTO-PROJECT.md`, `.claude/rules/product.md`, `.lexicon.conf`, `.memory-tree.conf`
- `coding-governance-agents.template.md` (source; `AGENTS.md` is its render)
- `memory/map/baseline.toml`, `memory/map/features/roles.md`
- `help/upgrade-steps.md`

### Alternatives rejected

- **A `[[shim]]` row of kind `module` for `map_lib`** (TOOL-dSafePassage-6 S1): its forwarder replaces
  the file at `from`, and `map_lib.py` stays with every other name it defines (§8 F2).
- **Deleting an adopter's seeded template**: refused by the clause ("never deleted") and by the owner's
  FK-1-4 with FK-3-1, which dropped `delete` from `install.retired-edits`.
- **One step per adopter rule**: the rules are one key, read and written together, and one before-image
  restores them together.

## 5. Production-readiness checklist

- security: the step writes only the two `.governance/` files of the target it runs on, under the walk's
  containment, and validates every row through unit 32's reader before writing; nothing it writes runs.
- perf / scale: one TOML read and two file writes per adopter; the queries are two `git grep` runs.
- error / empty / loading states: no `adopter_rules` key, the step is a no-op with exit 0; a line the
  reader refuses fails the up with nothing written; a down over a later edit names the file and leaves
  it.
- observability: the walk prints each step's id and outcome; the step gate prints each member and the
  row that witnesses it.
- risks: an adopter whose `CLAUDE.md` holds more than the import line keeps it, and the render's
  `--check` names it (unit 34, S4); the `playbook/seeded-template` id is a step-shaped id no step
  declares, legal by the parent's grammar today (§8 F1).
- testing: AC1 to AC11, each observing the step gate or the step program directly on a scratch clone.
- migration: this unit is the migration; §4.
- user docs: `help/upgrade-steps.md` (S8).

## 6. Acceptance criteria

- **AC1** — When `python step_gate.py --base ce13efbe` runs on a scratch clone of the
  pass's tip with the `agent-instructions` `[[retired]]` row taken out, it exits 1 naming
  `entry:agent-instructions`; with the row back it exits 0 for that member.
  Red when: the kit leaves with no succession row and the gate stays green.
  fixture: a clone under `%TEMP%`; dSafePassage's step gate landed.
- **AC2** — When the first query of §4 "### The inventory queries" runs after the pass, every hit is a
  kept hit the pass commit's `Decided:` trailer names, and `README.md`'s kit line names the renderer.
  Red when: a reader still names `tools/agent-instructions/` as where the wiring lives.
  figure: the count is DERIVED by the query at the pass.
- **AC3** — When `python upgrade_steps.py list` runs, it prints the `agent-instructions`
  succession row with `playbook-render`; and on a scratch adopter installed at `ce13efbe` with
  `agent-instructions` claimed, `python tools/govkit/govkit.py update --target <scratch adopter>` carries
  the claim to `playbook-render` and its `CLAUDE.md` import line is unchanged.
  Red when: the update refuses the whole run on the retired kit, or rewrites a working import.
- **AC4** — When `python step_gate.py --fixture --plant module-export` runs, it exits 1
  naming the re-exported name the plant took away; with `--with-row` it exits 0.
  Red when: a re-exported name leaves `map_lib` with no row naming it.
- **AC5** — When `python adopter_rules_to_overlay.py up <scratch>` runs on a target
  whose `deploy.toml` holds three rules, the overlay holds three level-0 `repo.` units with the rules'
  text, the key is gone, and `witness` exits 0; `down` restores both files byte-identical, and `up`
  again reproduces the first result byte for byte.
  Red when: the down leaves a byte different, or a rule is lost or doubled.
- **AC6** — When the same program's `up` runs on a target with no `adopter_rules` key, it exits 0 and
  writes nothing; on a target whose rule exceeds the one-line cap it exits 1 and writes nothing.
  Red when: a refused rule leaves a half-written overlay.
- **AC7** — When `python step_gate.py --base ce13efbe` runs on a scratch clone with the
  `playbook/adopter-rules-to-overlay` row taken out, it exits 1 naming `charter-key:ADOPTER_RULES`;
  with it, 0 for that member; and `--fixture --plant charter-key` exits 1, `--with-row` 0.
  Red when: the placeholder leaves with no row and the gate stays green.
- **AC8** — When `python step_gate.py --base ce13efbe` runs on a scratch clone with the
  `playbook/seeded-template` row taken out, it exits 1 naming each seed member; with it, 0.
  Red when: the seed rule leaves with no succession row and the gate stays green.
- **AC9** — When `python tools/govkit/govkit.py update --target <scratch adopter>` runs on an adopter
  installed at `ce13efbe` whose seeded template it edited, the row reads `retired-edited`, one order is
  written and the file's bytes are unchanged; on one it never edited, the row reads `withdrawn`.
  Red when: an edited seeded copy is deleted or graded `patched` with no order.
- **AC10** — When `python step_gate.py --base ce13efbe` runs on a scratch clone with one
  census change record taken out, it exits 1 naming that unit's tag; with it, 0.
  Red when: a unit leaves the shipped set with no change record.
- **AC11** — When `python upgrade_steps.py list` and gov's source-mode receipt are read
  after the lander's prepared merge, the receipt's `steps` holds `playbook/adopter-rules-to-overlay`
  and its witness exits 0 on gov's tree.
  Red when: an adopter meets a step gov never ran on itself.
- **AC12** — When `git grep -n -e "adopter-rules-to-overlay" -- upgrade-steps.md` runs, it finds
  the section.
  Red when: the steps ship with no page under `help/`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `recall floor` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `agent-instructions self-test` · `lexicon naming predicates` · `straggler-guard arms` · `kit/dogfood doc parity` · `transition-audit arms` · `check-wiring self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The `step-gate`, `step-rows-frozen` and `upgrade walk` legs dSafePassage lands keep green over this
unit's rows; they are named here in prose because the manifest at `ce13efbe` holds none of them.

New arm: tools/govkit/surface-classes.toml · covers AC4 AC7 · the step gate's own fixture runs each new class row's plant with and without `--with-row` · none

## 8. Open questions

- **FACT-QUESTION · F1 — Whether a `[[retired]]` row can name the seeded template.** Scout C's
  interface 10: a `[[retired]]` row's `id` is an entry id or a step id, and the seed is a file inside
  the `playbook` entry. Probe: TOOL-dSafePassage-1 §4 "### Data model", read at `ce13efbe`. Observation:
  the grammar refuses a retired id that is still a live entry or declared step and a successor that is
  not live, and states no rule that a retired step id was once declared; `surfaces` takes any
  `<class>:<name>`. Liveness: the same reader refuses `id = "playbook"`, a live entry, so the probe can
  read a refusal. RESOLVED (agent, 2026-10-23, delegated): a `[[retired]]` row with the step-shaped id
  `playbook/seeded-template`, `successor = "none"` and the seed's members in `surfaces`, rung 2; the
  build run re-grounds against the landed reader, and if it refuses the id, the row becomes an
  `[[upgrade]]` row whose `surfaces` names the same members, recorded as a deviation. widens: none ·
  relaxes: none
- **FACT-QUESTION · F2 — Whether the `map_lib` deprecation fits a `[[shim]]` row.** Probe:
  TOOL-dSafePassage-6 S1 and S3, read at `ce13efbe`. Observation: a `module` row's forwarder is written
  at its `from` path and "stands in for itself in `sys.modules`", so a row whose `from` is
  `codebase-map/map_lib.py` would replace a module that keeps every name it does not re-export.
  Liveness: a row whose `from` is a moved whole module would fit, so the probe can read a fit.
  RESOLVED (agent, 2026-10-23, delegated): no fit; the deprecation is declared by S3's `module-export`
  class row, the parent's own extension point ("a later build's class joins by adding its own row"),
  rung 2. widens: none · relaxes: none
- **F3 — How the step gate sees the adopter rules leave.** None of the parent's nine classes reads a
  playbook placeholder or a `[charter]` key. Options: (a) a `charter-key` class row; (b) no class, so
  the clause's "seen red at the step gate" has no member; (c) folding the key into the `conf` class.
  (b) fails the clause, and (c) changes the parent's class reader. RESOLVED (agent, 2026-10-23,
  delegated): (a), rung 3, through the parent's extension point. widens: none · relaxes: none
- **F4 — Who writes gov's overlay and `deploy.toml` when the step runs on gov.** The minimal guard
  refuses agent writes to both until dDeclaredLoop, and unit 15's command refuses every write until
  then. Options: (a) the step, run by `update` in the lander's prepared merge (`cl-dClosedLoop-0025`);
  (b) unit 15's command; (c) the owner by hand. (b) refuses by its own clause, and (c) is no step.
  RESOLVED (agent, 2026-10-23, delegated): (a), rung 1, the clause naming the step as the converter;
  the build run re-grounds against the landed guard and files the admission ask if it reads the step's
  write as an agent's. widens: none · relaxes: none
- **F5 — The agent-instructions kit's successor.** Options: (a) `playbook-render`, the renderer that
  absorbed the wiring; (b) `none`, the files withdrawn; (c) `playbook`. (b) leaves an adopter's alias
  files with no owner, and (c) is the seed entry whose template this build stops reading. RESOLVED
  (agent, 2026-10-23, delegated): (a), rung 1, v2's "agent-instructions' wiring moved to the one
  renderer". widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-39, PLAY-dOrderedCharter-46, PLAY-dOrderedCharter-49.

## 10. Reuse audit

No seam in the tree takes these rows yet: `grep -rn '\[\[upgrade\]\]' tools` returns nothing at
`ce13efbe`, as scout C found (`memory/builds/dOrderedCharter/build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-c.md:14`);
the step kind, the class registry, `retired-edited` and the step gate are dSafePassage's specs,
deferred to its build run, and this unit writes rows in their grammar. The built seams it reads, each
verified at source: `[charter] adopter_rules` (`.governance/deploy.toml:59-70`) and `read_charter_table`
(`tools/playbook/render_playbook.py:809`); the `ADOPTER_RULES` placeholder
(`tools/govkit/entries/playbook.kit.toml:273-277`); the seed rule (`:23-26`) and its
`reseed-available` grade (`tools/govkit/govkit.py:9989-9990`); the kit's registry entry
(`tools/govkit/registry.toml:106-107`) and `CODEX_MAX` (`tools/agent-instructions/adopt-agent-instructions.sh:31`).
`reuse_lookup.py "retire a shipped file with a successor at update"` ranked name-token hits only
(`corpus_files`, `parse_file`, `hash_file`); none carries a file to a successor. The reader-inventory
query follows unit 18's stated-query form (its §4 "### The inventory query"), never a typed list. Where
a record and the source disagree: the scout cites the seed row at `entries/playbook.kit.toml:23-26`, which
matches, and `README.md:17` as the kit's by-value reader, which spells its path and is a by-path hit
too. The recall probe found the clause, TOOL-dSafePassage-1 and -5, and TOOL-dGroundRules-13
(`memory/builds/dGroundRules/BACKLOG.md:6`), the guard-admission ask a step run on gov's own tree
needed, which F4 follows.

Recall terms used: `python tools/memory-recall/query.py "how does gov ship its own upgrade step that retires the seeded charter template" --terms "upgrade step retired row seeded template adopter_rules overlay down restores successor change record"`
