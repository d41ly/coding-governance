# PLAY-dConvergedCharter-10 — the protocols and skills scopes of the one renderer: protocol slices and Skill entries rendered from units

**Status:** DEFERRED · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 16 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0484@7e1eaeeb whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md](../build/2026-11-03-build-PLAY-dConvergedCharter-6-reuse-scout-b.md) | research | PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-15 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 PLAY-dConvergedCharter-41 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |

<!-- /gen:spec-records -->

## 1. Goal

R-A makes the unit the atom and every document a rendering of units, and dOrderedCharter's renderer of
record renders three scopes, `charter`, `agents` and `entry-files`, leaving the guides, the templates and
the Skills to their own renderers beside the legacy list (PLAY-dOrderedCharter-20 S5 and §3). At base
seven adopt scripts each render one Skill from its own template (`render_skill` or `render` in
`tools/branch-reconcile/adopt-branch-reconcile.sh:58`, `tools/lexicon/adopt-lexicon.sh:272`,
`tools/roles/adopt-roles.sh:251`, `tools/runlog/adopt-runlog.sh:252`,
`tools/drift-audit/adopt-drift-audit.sh:309`, `tools/memory-recall/adopt-memory-recall.sh:258`,
`tools/unattended/adopt-unattended.sh:801`), and gap-found-13 names Skills as parallel procedures. This
unit adds the two scopes the rest of the convergence renders through: `protocols`, which renders a
protocol document's slot lines into the slices of units they select, and `skills`, which renders each
Skill entry from the units its `[[drive]]` rows derive, each scope a `[[target]]` renderer under
render parity.

## 2. Scope (IN)

Build-run preconditions, each landed before this unit's pass: PLAY-dOrderedCharter-3 (`documents.toml`,
its `source` field, `render_envelope`), -6 (`[[drive]]` rows and `instruction_units.py drive --check`),
-9 (`read_units`, `derive_unit_selection`, `render_unit`, `render_units`), -12 (`write_lock_row`,
`read_lock`), and -20 (`renderers.toml`, `--render-scope`, `--check-render --scope`, the slot line
`<!-- units: <selector> -->`, the legacy list).

- **S1** — The `protocols` scope, shared interface I18. `python tools/playbook/render_playbook.py
  --render-scope protocols [--target <tree>]` renders every path a `[[target]]` row with `renderer =
  "playbook:protocols"` claims: `render_protocol_target(doc_row, units)` reads the `source` its
  `documents.toml` row names and expands each slot line `<!-- units: <selector> -->` to
  `render_units(derive_unit_selection(units, selector))` (PLAY-dOrderedCharter-20 S7), every other
  source line copied byte for byte, the source's envelope lines included (PLAY-dOrderedCharter-3 S5),
  and writes the target's lock row through `write_lock_row`, its `units` the selected units. A claimed
  path with no `documents.toml` row, or a row with no `source`, refuses the scope, exit 2, naming the
  path. Observed by AC3 and AC6.
- **S2** — The `skills` scope, shared interfaces I18 and I19. `python
  tools/playbook/render_playbook.py --render-scope skills [--target <tree>]` renders one
  `.claude/skills/<skill>/SKILL.md` per distinct `skill` value of every selected kit's `[[drive]]`
  rows, through `render_skill_entries(rows)`: `derive_skill_units(rows)` builds, for each row in row
  order, one pointer unit (PLAY-dOrderedCharter-9 S1: `type = "pointer"`, `trigger` the row's `when`,
  `text` the sentence `Use when <when>, runs <command>.`), never written to a manifest; the entry is
  front matter `name` the `skill` value and `description` those sentences joined by one space, then the
  envelope of the Skills class row of `documents.toml` (level 4) around a body of one line per row
  naming its command and the `stage` and `role` it enters, as `render_unit` renders each unit, with no
  procedure. The lock row lists the derived units (§8 F1). Observed by AC1, AC2 and AC5.
- **S3** — The `skill` key. A `[[drive]]` row gains the optional key `skill`, a Skill directory name
  matching `[a-z][a-z0-9-]*`; rows sharing a value are one entry. `instruction_units.py drive --check`
  (PLAY-dOrderedCharter-6 S4) admits the key and reds a malformed value naming the kit and the row. The
  `gov-` prefix on a gov-rendered entry is unit 9's arm. Observed by AC4.
- **S4** — The targets, in `tools/playbook/renderers.toml`: one `[[target]]` row
  `paths = [".claude/skills/gov-*/SKILL.md"]`, `renderer = "playbook:skills"`; and the renderer value
  `playbook:protocols`, which no row names at this pass, a row moving to it when its document's source
  holds slot lines (unit 7 moves `TEMPLATE-SPEC.md` and `HYGIENE.md`). Where a row at the pass claims a
  path the `skills` row claims, that row is narrowed to its own paths, so no file has two renderers of
  record (PLAY-dOrderedCharter-20 S4). Observed by AC5.
- **S5** — Render parity. `--check-render --scope protocols` and `--check-render --scope skills`
  render to memory and compare bytes with each claimed path, red naming the path, the first differing
  line and the remedy, the `--render-scope` command; with no claimed path each prints `<scope>:
  unarmed — no target names playbook:<scope>` and exits 0, never a bare green. The no-scope
  `--check-render` gate (PLAY-dOrderedCharter-20 S8) runs both. Observed by AC2, AC3 and AC5.
- **S6** — The plants, on PLAY-dOrderedCharter-20 S10's `python tools/playbook/instruction_units.py
  fixture --plant <case>`: `skill-entry`, `skill-entry-edited`, `skill-key-malformed`,
  `protocol-slice`, `protocol-slice-edited` and `protocol-no-source`. Observed by AC1 to AC4 and AC6.

## 3. Non-goals (OUT)

- Which Skills render through `skills`, their `gov-` names, their `[[drive]]` rows and the renames:
  unit 9. Each per-kit render arm is retired by its owner: units 9 and 8 for the five kits' Skills, units
  17 and 12 for `build` and `unattended`.
- Which documents render through `protocols`, their slot lines and the `record-template` slot: unit 7
  (its S10), over the units unit 1 writes.
- The `explanation` scope: unit 7. The `readme` scope: unit 15.
- Retiring `render-doc`, kit/dogfood parity and review-protocol parity: unit 8, each with its last
  document.
- Tag slices returned by `gov_tag.py bundle`: PLAY-dOrderedCharter-25; this unit renders files.

### Edges

- **hands-off** `PLAY-dConvergedCharter-7` — `renderers.toml`, with the `playbook:protocols` renderer its documents move to and the scope grammar its `explanation` row follows
- **hands-off** `PLAY-dConvergedCharter-9` — `renderers.toml`, the `skills` scope's `[[target]]` row and the `skill` key of `[[drive]]` its entries render from
- **hands-off** `PLAY-dConvergedCharter-8` — `renderers.toml`, the `protocols` and `skills` rows it joins the legacy list against before retiring a renderer
- **hands-off** `PLAY-dConvergedCharter-15` — `renderers.toml`, the scope grammar its `readme` rows follow
- **consumes-from** external — PLAY-dOrderedCharter-3, -6, -9, -12 and -20, each DEFERRED at base and landed before this build run

## 4. Design

### Evidence

- `render_playbook.py` renders the charter alone at base (`render` at `tools/playbook/render_playbook.py:1024`);
  `render_agent_file` (`tools/roles/render_agents.py:144`) is the slot-renderer shape the `agents`
  scope calls (PLAY-dOrderedCharter-20 S5).
- The seven per-kit Skill renderers are at the lines §1 cites, each verified at `d8a12f046`; seven
  `SKILL.template.md` files sit under `tools/branch-reconcile`, `drift-audit`, `lexicon`,
  `memory-recall`, `roles`, `runlog` and `unattended`, and `.claude/skills/` holds seven rendered
  Skills (`build`, `cleanup`, `drift-audit`, `lexicon`, `memory-recall`, `runlog`, `unattended`).
- PLAY-dOrderedCharter-20 §4 seeds `renderers.toml` with the `charter`, `agents` and `entry-files`
  rows and a `render-doc` row for the guides and both templates; `INSTRUCTION_PATHSPECS` (its S4)
  names `.claude/skills/*/SKILL.md`, so each rendered Skill sits on the legacy list until its entry
  renders from units.

### A Skill entry

```markdown
---
name: gov-recall
description: Use when <when of row 1>, runs `gov why`. Use when <when of row 2>, runs `record find`.
---

[<doc> · Level 4 · <direction>]
- `gov why` — enters <stage> as <role>
- `record find` — enters <stage> as <role>
[/<doc>]
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `render_protocol_target`, `render_skill_entries`, `derive_skill_units` | functions, `render_playbook.py` | `py.function`, each `OK` by `--suggest` |
| `protocols`, `skills` | values of `--render-scope` and `--scope` | none |
| `playbook:protocols`, `playbook:skills` | `renderer` values of `renderers.toml` | none |
| `skill` | optional key of a `[[drive]]` row | none |
| the six plants of S6 | fixture cases | none |

### Rollout

Live at landing, and unarmed in gov until unit 9 writes the first `skill` rows and unit 7 moves the
first documents to `playbook:protocols`; both land in the same build run, so the landed tree renders
through both scopes. An adopter renders a Skill entry when its kit's adopter calls
`--render-scope skills` (unit 9 S3).

### Files touched (estimate)

- `tools/playbook/render_playbook.py`: S1, S2, S5
- `tools/playbook/instruction_units.py`: S3's key in `drive --check`, S6's plants
- `tools/playbook/renderers.toml`: S4
- `tools/playbook/README.md`: the two scopes and the `skill` key

### Alternatives rejected

- **A renderer per Skill kind kept in each adopt script.** Seven copies of one render is the defect
  the one renderer exists to end (PLAY-dOrderedCharter-20 §1). Test: the seven functions §1 cites each
  substitute tokens into a template and differ only in their tokens.
- **An authored `[[unit]]` row per Skill entry beside its `[[drive]]` row.** The trigger and the
  command would be typed twice. Test: §8 F1.
- **A `source` column on each `[[target]]` row.** `documents.toml` already names each document's
  `source` (PLAY-dOrderedCharter-3 S1), so a second column types one fact twice. Test: §8 F2.

## 5. Production-readiness checklist

- security — no new write surface: each scope writes only the paths its `[[target]]` rows claim, under
  the target tree, the renderer of record's existing rule.
- perf / scale — one `read_units` and one descriptor read per run; a Skill entry is a few lines.
- error / empty / loading states — an empty scope prints its `unarmed` line; a missing source refuses
  exit 2 naming the path; a malformed `skill` value reds the drive check.
- observability — each red names the path, the first differing line and the command that re-renders.
- risks — a derived unit has no manifest row; §8 F1's ask makes the lock and status arms read it.
- testing — AC1 to AC6 and the arm of §7.
- migration — none at this pass: units 7 and 9 move documents and Skills onto the scopes.
- user docs — `tools/playbook/README.md`.

## 6. Acceptance criteria

- **AC1** — When `python instruction_units.py fixture --plant skill-entry` runs, `--render-scope skills`
  writes the fixture's `gov-alpha` entry from two `[[drive]]` rows sharing `skill = "gov-alpha"`:
  `name: gov-alpha`, a `description` holding both `Use when …, runs …` sentences in row order, the
  level-4 envelope and one body line per row; and the target's lock row lists two units.
  Red when: a sentence is missing, out of row order, or typed anywhere but the drive rows.
- **AC2** — When `python instruction_units.py fixture --plant skill-entry-edited` hand-edits the
  rendered entry, `python render_playbook.py --check-render --scope skills` exits 1 naming the path
  and the first differing line.
  Red when: a hand edit to a rendered Skill entry passes render parity.
- **AC3** — When `python instruction_units.py fixture --plant protocol-slice` runs, `--render-scope
  protocols` expands the planted source's `<!-- units: role.alpha -->` line to the two units scoped
  `role.alpha`, keeps the envelope and every other line, and writes a lock row listing both; under
  `protocol-slice-edited`, `--check-render --scope protocols` exits 1 naming the path.
  Red when: a hand edit to a rendered protocol slice passes render parity, or a slot line survives.
- **AC4** — When `python instruction_units.py fixture --plant skill-key-malformed` runs, `python
  instruction_units.py drive --check` exits 1 naming the kit, the row and `skill`; with the value
  `gov-alpha` it exits 0.
  Red when: a malformed `skill` value passes, or a well-formed one is refused.
- **AC5** — When `python render_playbook.py --check-render` runs at this unit's pass tip, it exits 0,
  printing `protocols: unarmed` and `skills: unarmed`, and `grep -n "playbook:skills"` over
  `renderers.toml` finds the row of S4.
  Red when: a scope reports green over no target, or a path has two renderers of record.
- **AC6** — When `python instruction_units.py fixture --plant protocol-no-source` runs,
  `--render-scope protocols` exits 2 naming the claimed path that has no `documents.toml` source.
  Red when: the scope renders a path from a guessed source, or exits 0.

## 7. Gates

`govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `playbook render wiring`

The parents' legs `instruction render (one renderer of record)` and `instruction units (schema, one
fact)` run S5 and S6 once dOrderedCharter lands them; neither is in the manifest at base.

New arm: tools/playbook/instruction_units.py · covers AC1 AC2 AC3 AC4 AC6 · the six plants of S6 under its `fixture --plant`, each scope's failing case a hand edit to its rendered target · none

## 8. Open questions

- **F1 — What does a Skill entry render from, when the clause says units and SK-2 says the drive row
  (cl-dClosedLoop-0483)?** Options: (a) pointer units derived from each `[[drive]]` row at render, the
  lock row listing them, with an ask that dOrderedCharter's lock and status arms read a derived unit;
  (b) an authored `[[unit]]` row per entry beside its drive row, with a parity arm comparing the two;
  (c) the entry rendered from the drive row with no unit, a departure from this clause. RESOLVED (agent,
  2026-11-03, delegated): (a), rung 3, the most feature-rich survivor: it meets both clauses with one
  authored fact, where (b) types the trigger and command twice and (c) fails this clause (veto 1).
  widens: none · relaxes: none · Ask, target dOrderedCharter: "PLAY-dOrderedCharter-12 S4's lock row and PLAY-dOrderedCharter-20 S3's derived status admit a unit a renderer derives from a `[[drive]]` row, its tag `unit.<kit>.<skill>`, read `active` while that row stands", accept "a Skill entry rendered by the `skills` scope leaves `instructions-legacy.txt` with its lock row listing its derived units and the status arm green, seen on a fixture entry".
- **F2 — Where does the `protocols` scope find a target's source?** Options: (a) the `source` field of
  the target's `documents.toml` row; (b) a `source` column on the `[[target]]` row; (c) each kit's
  `rendered` rows. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3: one declaration already names
  every document's source (PLAY-dOrderedCharter-3 S1), and (b) and (c) type it a second time.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, the spec run's carrier of `cl-dClosedLoop-0484`.

## 10. Reuse audit

The seam extended is PLAY-dOrderedCharter-20's renderer of record, `render_playbook.py` with
`--render-scope`, `--check-render --scope` and `renderers.toml` (S4, S5, S8), its slot line (S7) and
PLAY-dOrderedCharter-9's `derive_unit_selection`, `render_unit` and `render_units`, every one DEFERRED
at base; the live anchors are `render` (`tools/playbook/render_playbook.py:1024`) and
`render_agent_file` (`tools/roles/render_agents.py:144`), both read at source. `python
tools/codebase-map/reuse_lookup.py "render a Skill entry from a command row and render a protocol slice
from units with a byte parity check"` ranked name-stem hits (`rows`, `row`, `check`, `render` across
the seven adopt scripts, `render_cards_md`), which are the seven per-kit renderers this scope serves
and the map's own renders, so no live seam renders from units. Scout B's row agrees with source on the
seven renderers' lines and on `render` at `:1024` (its finding 3 corrected PLAY-dOrderedCharter-6's
`:979`). Scout B proposed `splice_region` for these scopes; neither scope renders a region inside a
hand-written file, so S1 and S2 write whole targets as the `charter` scope does, and the region rule
stays the runbook's (DEPL-dShippedRelease-9 S2). Each rejected candidate and its test are in §4.

Recall terms used: `python tools/memory-recall/query.py "how are Skill entries and protocol slices rendered from units by one renderer scope" --terms "renderer scope target renderers.toml slot units Skill entry drive row protocols skills render parity"`
