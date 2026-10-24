# TOOL-dPlacedRequest-9 — the kickoff manifest's facts as level-2 instruction units the card reads

**Status:** OPEN · rev-1 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 11 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0127@4f0c1452 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |

<!-- /gen:spec-records -->

## 1. Goal

The kickoff manifest has no record kind and no instruction unit, and the card reads a guide
(gap-orient-20, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:151`).
The memory plan's `[pockets]` row places it as "node: units at level 2 that the card reads", keyed
by tag (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md:72`). This
unit moves the manifest's §B orientation facts into level-2 instruction units of the repository's
overlay, through an upgrade step whose down restores them, and renders those units into a
`## pockets` section of the orientation card, so the facts live once, as units, and the card reads
them.

## 2. Scope (IN)

- **S1** — The fact units. Each top-level `- ` bullet of a kickoff manifest's `## §B — Orientation`
  section, the run before its first `###` sub-head, becomes one `[[unit]]` row of the overlay
  `.governance/instructions.toml` (PLAY-dOrderedCharter-32 S1): `tag = "repo.kickoff.f<nn>"`, `<nn>`
  the bullet's two-digit position at conversion, minted once and never renumbered; `level = 2`;
  `type = "constraint"`; `scope = ["reader.card"]`; `trigger = "always"`; `budget` `line` for a text
  of at most 200 bytes and `block` otherwise; `text` the bullet without its `- `; and
  `enforced-by = "none — a fact the kickoff manifest front-loads"`. Observed by AC1.
- **S2** — The selector. `tools/playbook/readers.toml`, the `reader` namespace's declaring source
  (PLAY-dOrderedCharter-10 §4 "The eight"), gains the member `reader.card`, the orientation card as a
  reader of units. Observed by AC2.
- **S3** — The read. A `pockets` verb on `tools/playbook/instruction_units.py`'s command line,
  `python tools/playbook/instruction_units.py pockets [--root <tree>]`, prints `## pockets` and then
  `render_units(derive_unit_selection(units, "reader.card"))` (PLAY-dOrderedCharter-9 S4) over the
  composition `derive_unit_composition` returns (PLAY-dOrderedCharter-32 S4), keeping only level-2
  units, one `- <line>` per unit. Each line is cut at `POCKETS_LINE_BYTES = 160` with `…`; past
  `POCKETS_CAP_BYTES = 2048` the verb prints `- … (+<k>) — instruction_units.py pockets --all` and
  stops, and `--all` prints every line uncut. With no selected unit it prints `- none declared`.
  Observed by AC3 and AC4.
- **S4** — The card reads it. `render_card` in `skills/session-kickoff/manifest-check.sh` (:517)
  prints the verb's output immediately before its `recent —` line, through a new
  `derive_pockets_block` that resolves the module as an optional sibling
  (`resolve_kit_file playbook instruction_units.py`) and bounds the call as `derive_overlaps_line`
  (:555) bounds its own: a kill into a file, stdin from `/dev/null`. Every failure prints the one line
  `pockets — skipped: <why>` and the card still writes. The section sits inside the card's startup
  part, which `CARD_PARTS_AWK` (:984) ends at the `recent —` run, so the append and the citation
  check read it as startup. Observed by AC5.
- **S5** — The door. An `[[upgrade]]` row `kickoff-manifest/facts-to-overlay` in
  `tools/govkit/entries/kickoff-manifest.kit.toml` (TOOL-dSafePassage-1 S1), its program
  `tools/govkit/steps/kickoff_facts_to_overlay.py` with `up`, `down` and `witness`. `up` reads the
  manifest at the target's `{manifest_path}`, builds S1's rows, grades each with
  PLAY-dOrderedCharter-12's `check_statement` and PLAY-dOrderedCharter-20's `schema`, writes them
  through `write_overlay_units` (PLAY-dOrderedCharter-32 S8), and replaces §B's bullets with the one
  bullet S6 names. A row either check refuses aborts the step: both files stay byte-identical and the
  refusal names the bullet's position and the finding. `down` restores both files from the
  before-image; `witness` holds when §B holds only the S6 bullet and every `repo.kickoff.` row's text
  was a §B bullet. Gov runs the step first, on its own tree (P38). Observed by AC1, AC6 and AC7.
- **S6** — The manifest after the move. §B keeps one bullet,
  `- The orientation facts are level-2 units the card prints under ## pockets; change one with tools/playbook/instructions_edit.py.`
  `skills/session-kickoff/MANIFEST-TEMPLATE.md`'s §B paragraph says a new fact is proposed with
  `instructions_edit.py propose --manifest overlay` (PLAY-dOrderedCharter-15 S2), and
  `skills/session-kickoff/SKILL.md`'s ratchet sentence that writes deltas back into §B says the same,
  the owner's NP-22 ruling that the manifest ratchet becomes the guarded instruction manifest
  (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:703`). The
  manifest's other §B sub-sections stay guide text. Observed by AC8.
- **S7** — The fixture, `python tools/govkit/steps/kickoff_facts_to_overlay.py --fixture --plant
  <case>`, builds a throwaway repository in the system temp directory holding a manifest, a policy
  file and stub playbook and kickoff kits, and runs the case. Observed by AC1 to AC7.

## 3. Non-goals (OUT)

- The unit schema, the one-fact check, `read_units`, `derive_unit_selection`, `render_units`, the
  overlay's reader, composer and writer, and the write command: PLAY-dOrderedCharter-9, -20, -32 and
  -15, called and never re-specced.
- The build's card at level 1, its remote ref, cache and snapshot: TOOL-dPlacedRequest-2, which
  carries this unit's `## pockets` section into the build card.
- The manifest's sub-sections below §B (the pointer map, gate commands, tier rule, id protocol, dated
  corrections and traps): guides, migrated to protocol slices by dConvergedCharter (`[pockets]`,
  "protocols and guides").
- A record kind for the manifest: the units are the node `[pockets]` names; the kickoff manifest's
  audit block keeps its keys.
- No `card:pockets` read key: the work order's `reads` vocabulary (`tools/roles/roles_lib.py:36-40`)
  is dBoundRoles'.

### Edges

- **hands-off** `TOOL-dPlacedRequest-2` — `## pockets`, the card section S4 renders, which the build card carries through every store
- **consumes-from** external — dOrderedCharter, built before this build run: `read_units`, `derive_unit_selection`, `render_units` (PLAY-dOrderedCharter-9 S2, S4), `check_statement` (PLAY-dOrderedCharter-12 S2), the `schema` check (PLAY-dOrderedCharter-20 S1), the `reader` namespace's source (PLAY-dOrderedCharter-10), and the overlay's `read_overlay`, `derive_unit_composition` and `write_overlay_units` (PLAY-dOrderedCharter-32 S1, S4, S8)
- **consumes-from** external — dSafePassage's `[[upgrade]]` row grammar and its reader `tools/govkit/upgrade_steps.py` (TOOL-dSafePassage-1 S1, S3)

## 4. Design

### Data model

```toml
# .governance/instructions.toml, written by the step
[[unit]]
tag = "repo.kickoff.f01"
level = 2
type = "constraint"
scope = ["reader.card"]
trigger = "always"
budget = "line"
text = "A build of more than one pass runs on `memory/guides/BUILD-METHOD.md`; it is in `watch:`, so editing it re-audits this manifest."
enforced-by = "none — a fact the kickoff manifest front-loads"
```

```toml
# tools/govkit/entries/kickoff-manifest.kit.toml
[[upgrade]]
id = "kickoff-manifest/facts-to-overlay"
up = ["python", "{gov}/govkit/steps/kickoff_facts_to_overlay.py", "up", "{target}"]
down = ["python", "{gov}/govkit/steps/kickoff_facts_to_overlay.py", "down", "{target}"]
witness = ["python", "{gov}/govkit/steps/kickoff_facts_to_overlay.py", "witness", "{target}"]
surfaces = []
needs-target = false
```

`surfaces = []`: no step-gate class reads a manifest bullet, and the witness is what proves the move.
The row copies `playbook/adopter-rules-to-overlay`'s shape (PLAY-dOrderedCharter-31 §4).

### The card section

```
## pockets
- A build of more than one pass runs on `memory/guides/BUILD-METHOD.md`; it is in `watch:`, so …
- … (+19) — instruction_units.py pockets --all
recent —
```

The bound keeps the card under `CARD_CAP_BYTES` (8192, `skills/session-kickoff/manifest-check.sh:216`):
a card holding a READY body measured 4936 bytes on this node (PINNED, 2026-10-25), and §B's 27 bullets
measure 4717 bytes (PINNED, 2026-10-25, `awk` over the section at `1fce223e5`), so the facts whole
would overflow the cap and `write_card` would refuse the card. The verb re-derives both counts at
every render.

### Type

Every bullet converts as a `constraint`. The manifest's own rule is "a pointer or a trap, never a
procedure" (`memory/guides/SESSION-KICKOFF.md:46-47`), and a `pointer` names no whole document
(PLAY-dOrderedCharter-12 S2) while most bullets do; a `constraint` carries a value in its text and
names its enforcer, which `enforced-by` states as none. A bullet `check_statement` refuses as a
constraint aborts the step (S5), so the gov pass fixes the bullet's text and re-runs the step; no
bullet is left behind half-moved.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `reader.card` | `reader` namespace member | none |
| `pockets` | verb of `instruction_units.py` | none |
| `POCKETS_LINE_BYTES`, `POCKETS_CAP_BYTES` | constants | none declared |
| `derive_pockets_block` | shell function | `sh.function`, asked at the pass |
| `kickoff-manifest/facts-to-overlay` | upgrade step id | none |
| `tools/govkit/steps/kickoff_facts_to_overlay.py` | module | none declared for files |
| `repo.kickoff.f<nn>` | unit tags | graded by `gov_tag.py check` |
| `## pockets` | card section | none |

### Migration

The step is the migration: gov's §B moves at the build pass, an adopter's at its next `govkit
update`. Its down restores the manifest and the overlay byte-identical.

### Rollout

Live at landing. A card written before the step ran prints `- none declared` under `## pockets`, and
§B still holds its bullets, so nothing is lost before the move.

### Files touched (estimate)

- `tools/playbook/instruction_units.py`: the `pockets` verb
- `tools/playbook/readers.toml`: `reader.card`
- `tools/govkit/entries/kickoff-manifest.kit.toml`: the `[[upgrade]]` row
- `tools/govkit/steps/kickoff_facts_to_overlay.py`
- `skills/session-kickoff/manifest-check.sh`: `derive_pockets_block` and its call in `render_card`
- `skills/session-kickoff/manifest-check.test.sh`: the arm the §7 line declares
- `skills/session-kickoff/MANIFEST-TEMPLATE.md`: §B's paragraph
- `skills/session-kickoff/SKILL.md`: the ratchet sentence; the installed skill is its machine-scoped link
- `memory/guides/SESSION-KICKOFF.md`: §B, written by the step's `up`
- `.governance/instructions.toml`: the `repo.kickoff.` rows, written by the step's `up`
- `help/orientation-card.md`: new, the card's page, with its `## pockets` section
- `help/README.md`: the index line for that page

### Alternatives rejected

- **A kit manifest beside the kickoff engine.** `read_units` reads `<prefix>/*/instructions.toml`
  (PLAY-dOrderedCharter-9 S2), and the kickoff engine's home is `skills/session-kickoff`, outside the
  tool root (`tools/govkit/entries/kickoff-manifest.kit.toml:6-9`); the facts are also the
  repository's, not the kit's.
- **Tags in place on the §B bullets, read by a second parser.** Two readers of instruction rows is
  the one-fact class PLAY-dOrderedCharter-9 S3 closes.
- **Raising `CARD_CAP_BYTES`.** Every card cell is sized against it; one bounded section keeps the
  other cells whole.

## 5. Production-readiness checklist

- security — the overlay is a guarded file: only the step door writes it (PLAY-dOrderedCharter-32
  S8), and an agent's new fact is a proposal the owner applies (S6).
- perf / scale — one bounded subprocess per card write; the verb reads the composition once.
- error / empty / loading states — no playbook kit, a refused policy read or a timeout each prints
  `pockets — skipped: <why>`; no selected unit prints `- none declared`; a refused bullet aborts the
  step with both files unchanged.
- observability — the step names each refused bullet by position and finding; the cut line names the
  hidden count and the verb that prints it.
- risks — an adopter manifest whose §B bullets fail `check_statement` keeps them until fixed, and
  its card says `none declared`; the witness reports it.
- testing — S7's plants, red and green.
- migration — the step, with its down.
- user docs — `help/orientation-card.md`, a new page indexed in `help/README.md`, names the card's
  `## pockets` section and the verb; TOOL-dPlacedRequest-2 adds the build card's sections to it.

## 6. Acceptance criteria

- **AC1** — When `python kickoff_facts_to_overlay.py --fixture --plant up` runs over a manifest whose
  §B holds three bullets, the fixture's overlay holds `repo.kickoff.f01` to `repo.kickoff.f03` at
  `level = 2` with `scope = ["reader.card"]`, each `text` equal to its bullet, and §B holds only the
  S6 bullet.
  Red when: a bullet is left in §B, copied rather than moved, or a row's text differs from its bullet.
- **AC2** — When `grep -n 'reader.card' readers.toml` runs in the playbook kit's directory, it prints the member's
  row, and `python gov_tag.py show reader.card` resolves it to that row.
  Red when: the selector is absent, so no unit can name the card as its reader.
- **AC3** — When `python instruction_units.py pockets --root <fixture>` runs after AC1's plant, it
  prints `## pockets` and three `- ` lines in tag order; with the plant `pockets-level`, a fourth
  `reader.card` unit at level 3 is not printed.
  Red when: a unit of another level, or one not naming `reader.card`, reaches the section.
- **AC4** — When the plant `pockets-cap` holds 30 units of 150 bytes, the verb's output is at most
  2048 bytes and ends with a `- … (+<k>)` line whose `<k>` plus the printed lines equals 30, and
  `--all` prints all 30.
  Red when: the section grows past the cap, or the hidden count is wrong.
- **AC5** — When the plant `card` runs `bash skills/session-kickoff/manifest-check.sh --card --write
  --session t1` in the fixture tree, the card holds `## pockets` and its lines immediately before
  `recent —`; with the plant `card-no-playbook`, the card holds `pockets — skipped:` and still writes.
  Red when: the section lands after the READY anchor, or a failed read refuses the card.
- **AC6** — When the plant `refused` holds a bullet `check_statement` refuses, `up` exits 1 naming
  the bullet's position, and `git status --porcelain` in the fixture prints nothing.
  Red when: a refused bullet half-moves the section.
- **AC7** — When the plant `down` runs `up` then `down`, both files equal their before-image byte for
  byte, and `witness` exits 1 after the down and 0 after the up.
  Red when: the down leaves a row or loses a bullet.
- **AC8** — When `grep -n "instructions_edit.py propose --manifest overlay" skills/session-kickoff/MANIFEST-TEMPLATE.md skills/session-kickoff/SKILL.md`
  runs, each file prints one line; and when `awk '/^## §B/{f=1;next} f&&/^###/{exit} f&&/^- /' memory/guides/SESSION-KICKOFF.md`
  runs after the pass, it prints the S6 bullet alone.
  Red when: the ratchet still tells a kickoff to write a fact into §B.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/steps/kickoff_facts_to_overlay.py · covers AC1 AC3 AC4 AC6 AC7 · the step's `--fixture` cases run by the `govkit selftest` leg, the failing case staged by the `refused` plant · none

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC5 · a stub playbook module printing a `## pockets` block, the failing case a stub that exits 2 · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that
  legal?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-25:
  the tuple holds `OPEN`, `SPECCED`, `INPROGRESS`, `BLOCKED`, `DEFERRED`, `CLOSED` and `WONTDO`, and
  not `DRAFT`. Liveness: it would show `DRAFT` if the vocabulary held it. RESOLVED (agent,
  2026-10-25, delegated): `OPEN`, as TOOL-dDeclaredLoop-3's F1 resolved the same brief line.
- **F2 — Where do the fact units live?** Options: (a) the overlay `.governance/instructions.toml`,
  written by an upgrade step; (b) a kit manifest beside the kickoff engine; (c) tags on §B's bullets,
  read by a second parser. (b) is outside `read_units`' population and holds the repository's facts
  in a kit; (c) adds a second reader of instruction rows. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3, the one survivor, and the overlay is where the repository's own units live
  (PLAY-dOrderedCharter-32 S1, level 2 admitted by its S3).
- **F3 — The facts whole overflow the card's 8192-byte cap; how does the card read them?** Options:
  (a) a bounded section with the rest one verb away; (b) raise `CARD_CAP_BYTES`; (c) tags only, no
  text. (b) moves a constant every cell is sized against; (c) drops the text the card exists to
  front-load. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, following PLAY-dOrderedCharter-4
  S3's bound on the instruction map.
- **F4 — Does the build's grant cover the kickoff skill's ratchet text and the manifest template?**
  Both are governance carriers, and the clause names the kickoff manifest's facts. RESOLVED (agent,
  2026-10-25, delegated): covered, rung 3, under the owner's NP-22 ruling that reshapes the manifest
  ratchet into the guarded instruction manifest.
  grants: PLAY-dClosedLoop-3 the §B ratchet sentence in skills/session-kickoff/SKILL.md and §B's paragraph in skills/session-kickoff/MANIFEST-TEMPLATE.md

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 9, the memory plan's `[pockets]` row,
  gap-orient-20 and PLAY-dOrderedCharter-9, -20, -31 and -32.

## 10. Reuse audit

The seams extended are the overlay and its writer (PLAY-dOrderedCharter-32 S1, S8), the step kind's
`[[upgrade]]` row (TOOL-dSafePassage-1 S1) in the shape PLAY-dOrderedCharter-31 S4 gives
`playbook/adopter-rules-to-overlay`, the unit selection and renderer (PLAY-dOrderedCharter-9 S4), and
the card's optional-sibling call, which PLAY-dOrderedCharter-4 S4 gives `derive_map_block` and
`derive_overlaps_line` already makes (`skills/session-kickoff/manifest-check.sh:555`). The scout's
`read_block` and `getval` (`skills/session-kickoff/manifest-check.sh:363-364`) read only the audit
block's keys, verified at base; §B is outside that block, so they are not the seam. `python
tools/codebase-map/reuse_lookup.py "render a manifest's facts as instruction units into the
orientation card"` ranked name-stem hits (`manifest`, `units`, `render`, `render_cards_md`), none a
unit reader, so no existing code seam fits the read; the parents' specs hold it. `python
tools/memory-recall/query.py` returned scout B's row, the brief's I14 and the memory plan's
`[pockets]` row; none disagrees with source.

Recall terms used: `python tools/memory-recall/query.py "how does the orientation card read the kickoff manifest facts as instruction units" --terms "kickoff manifest pockets level-2 instruction units card render_card read_block getval registry SESSION-KICKOFF"`
