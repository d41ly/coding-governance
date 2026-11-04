# PLAY-dConvergedCharter-1 — protocol text derived to facts only: each protocol document's load-bearing statements written as typed units, its rationale left for the explanation tree

**Status:** OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 15 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0475@2b542935 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md) | research | PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-19 |
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-1-reuse-scout.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-1-reuse-scout.md) | journal | — |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-2-reuse-scout.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-2-reuse-scout.md) | journal | — |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-3-reuse-scout.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-3-reuse-scout.md) | journal | — |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-4-reuse-scout.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-4-reuse-scout.md) | journal | — |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-5-spec-writer.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-5-spec-writer.md) | journal | — |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's CV2: "any protocol/method/runbook should only carry clear facts/definitions/policies/
descriptors", and prose that bears no load is gone
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md:808-829`; v2 P11,
v2:895-899). The protocol documents hold 424,697 bytes of guides and templates, and gap-spine-05 names
their volume. dOrderedCharter gives every chain build its own step's guides (IW-1) and lands the six
statement types, the checks and the envelopes; unit 13 moves the feature paragraphs. This unit derives
the residue: every load-bearing statement of each protocol document still on the legacy list becomes a
typed unit, graded by `check_statement`, and the document's source keeps only its envelope, its headings
and the rationale unit 7 moves into `help`, graded by `check_document`.

## 2. Scope (IN)

Build-run preconditions, each landed before this unit's pass: PLAY-dOrderedCharter-3 (`documents.toml`,
its `source` field, the envelopes), -9 (`[[unit]]` rows), -12 (`STATEMENT_TYPES`, `MODALS`,
`check_statement`, `check_document`), -15 (`instructions_edit.py check`, the change record), -20
(`core.py new unit`, `instructions-legacy.txt`), and this build's units 12, 13, 16 and 19.

- **S1** — The population, `derive_migrated_documents(root)` in `tools/playbook/guide_move.py`: every
  level-3 row of `documents.toml` whose path `instructions-legacy.txt` lists (shared interface I17),
  each edited at its `source`. DERIVED at the pass; once units 12 and 16 have taken theirs out, it is the six
  documents of §4 Evidence. A document is migrated once an active unit's `promoted-from` edge names one
  of its sections. Observed by AC4.
- **S2** — The residue route, `python tools/playbook/guide_move.py plan --residue --out <file>`, a
  second route of unit 13's mover over the same factory (shared interface I16, `derive_moves`): one
  entry per paragraph or list item of each section that unit 13's route left, holding `source`, the
  section's `doc.<name>#<seg>` tag (I12), the text, and the kit (the kit whose directory holds the
  `source`; for a source under the memory root, the kit unit 7's §4 "The guides" names), with blank
  `disposition`, `level`, `scope` and `text` the pass fills. `disposition` is one of `STATEMENT_TYPES`
  or `rationale`. Observed by AC1.
- **S3** — The apply, `python tools/playbook/guide_move.py apply --residue --plan <file>`. It refuses
  the whole plan, writing nothing, while an entry's `disposition` is blank, or a typed entry's `scope`
  or `text` is blank, or a composed row fails `check_statement` (PLAY-dOrderedCharter-12 S2). A typed
  entry becomes one row composed by `core.py new unit` and completed with `scope` (the selector tags
  that load it, a role, item or step tag, never `reader.every` unless the statement binds every reader,
  plus the section's own `doc.<name>#<seg>` tag for a unit promoted from `TEMPLATE-SPEC.md` or
  `HYGIENE.md`, the two documents unit 7 S10 keeps rendered and whose slot lines select by that tag),
  `help` empty, and the edge `promoted-from=doc.<name>#<seg>`; it is written by unit 13's route (its S4
  and §8 F2: the kit manifest edit and a change record through `build_records.py new change`), and its
  text leaves the source through `write_moves`. A `rationale` entry writes nothing and its text stays
  for unit 7. A second apply writes nothing. Observed by AC1 and AC2.
- **S4** — The residue arm, `check_residue_left(units, docs)` in `guide_move.py`, run as one more check
  of `instructions_edit.py check` beside unit 13's: over each migrated document's source, outside a
  fence and outside the envelope, a line opening with a modal of `MODALS` is red `STATEMENT LEFT
  <path>:<line>`, and every finding `check_document` (PLAY-dOrderedCharter-12 S3) returns is red under
  its own rule, a provenance paragraph, a numbered heading, a pointer to text never loaded or a typed
  fact. Observed by AC3.
- **S5** — Each document in its envelope. PLAY-dOrderedCharter-3 S5 writes each source's two envelope
  lines; `write_moves` never moves them, and the apply refuses a move whose span holds an envelope
  line. Observed by AC5.
- **S6** — The plants, on unit 13's `guide_move.py --fixture --plant <case>`: `residue-move`,
  `residue-untyped`, `residue-narrative` and `residue-left`, run by `guide_move.py --selftest`.
  Observed by AC1 to AC3.
- **S7** — The derivation at this unit's pass: `plan --residue` over the six documents, every entry's
  disposition, scope and text set by the pass, `apply`, and the units and change records committed
  together. Observed by AC4.

## 3. Non-goals (OUT)

- Envelope code and the document registry: PLAY-dOrderedCharter-3.
- Feature paragraphs: unit 13, earlier in order.
- Each section's rationale written into a unit's `help`, the `explains` edge, the guides retired and
  their rows leaving `instructions-legacy.txt`, and `TEMPLATE-SPEC.md` and `HYGIENE.md` rendered from
  slot lines: unit 7.
- The `protocols` scope that renders a document from its units: unit 10.
- The runbook `WIRE-INTO-PROJECT.md`: DEPL-dShippedRelease-9 derives it and unit 15 migrates it.
- The unattended guides and `SESSION-KICKOFF.md`: units 12 and 16 remove them first, so they are not
  in S1's population.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-13` — `dossier_move.py`'s plan and apply as the factory `prose_move.py`, and `guide_move.py` with its write route, which S2 and S3 add a route to; without them there is no mover and no write route
- **hands-off** `PLAY-dConvergedCharter-7` — `instructions-legacy.txt`, each listed guide's directive text drained into units, the rest left for unit 7 to move and retire
- **consumes-from** external — PLAY-dOrderedCharter-3, -9, -12, -15 and -20, each DEFERRED at base and landed before this build run

## 4. Design

### Evidence

- The documents at `d8a12f046` (`wc -c`, PINNED): `memory/guides/ANNOTATION-STYLE.md` 4,813,
  `BUILD-METHOD.md` 30,659, `MERGE-BAR.md` 7,884, `REVIEW-PROTOCOL.md` 16,004, `memory/HYGIENE.md`
  67,106 and `memory/TEMPLATE-SPEC.md` 39,749. The sources: `tools/memory-tree/ANNOTATION-STYLE.template.md`,
  `BUILD-METHOD.template.md`, `HYGIENE.template.md` and `SPEC-TEMPLATE.template.md`;
  `tools/workflows/REVIEW-PROTOCOL.template.md`; `MERGE-BAR.md` is hand-written, its own source.
- The other six guides at base leave first: the four unattended guides and `PLAYBOOK-TEMPLATE.md` with
  the kit (unit 12, rendered by `tools/unattended/adopt-unattended.sh:761-775`), `SESSION-KICKOFF.md`
  with the Skill (unit 16).
- None of the parents' files exists at base: `git ls-files` prints no `documents.toml`,
  `instruction_units.py`, `instructions_edit.py` or `instructions-legacy.txt` at `d8a12f046`.

### The manifests

| Document | Units land in |
|---|---|
| `ANNOTATION-STYLE.md`, `BUILD-METHOD.md`, `HYGIENE.md`, `TEMPLATE-SPEC.md` | `tools/memory-tree/instructions.toml` |
| `REVIEW-PROTOCOL.md` | `tools/workflows/instructions.toml` |
| `MERGE-BAR.md` | `tools/run-gates/instructions.toml` |

This is the table unit 7 §4 "The guides" holds for the rationale, so a section's statements and its
rationale land in one manifest.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_migrated_documents`, `check_residue_left` | functions, `guide_move.py` | `py.function`, both `OK` by `--suggest` |
| `--residue` | route flag of `plan` and `apply` | none |
| `STATEMENT LEFT` | the arm's red prefix | none |
| `residue-move`, `residue-untyped`, `residue-narrative`, `residue-left` | fixture plants | none |

### Migration

S7, at this unit's pass. Its write set is DERIVED from the plan: the six sources, the three kit
manifests and the change records, recorded as this unit's `--dispatch --writes`. The renders under
`memory/` follow their sources through `adopt-memory-tree.sh --render`.

### Rollout

Live at landing. An adopter receives the shrunken templates and the kits' units with the kit update;
the units load where their `scope` selects them once unit 7's slices and the loaders read them.

### Files touched (estimate)

- `tools/playbook/guide_move.py`: S1 to S4, S6
- `tools/playbook/instructions_edit.py`: S4's check
- `tools/playbook/README.md`: the user docs of §5
- `tools/memory-tree/ANNOTATION-STYLE.template.md`, `tools/memory-tree/BUILD-METHOD.template.md`, `tools/memory-tree/HYGIENE.template.md`, `tools/memory-tree/SPEC-TEMPLATE.template.md`: S7
- `tools/workflows/REVIEW-PROTOCOL.template.md`: S7
- `memory/guides/MERGE-BAR.md`: S7
- `memory/guides/ANNOTATION-STYLE.md`, `memory/guides/BUILD-METHOD.md`, `memory/guides/REVIEW-PROTOCOL.md`, `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`: the renders of S7
- `tools/memory-tree/instructions.toml`, `tools/workflows/instructions.toml`, `tools/run-gates/instructions.toml`: S7

### Alternatives rejected

- **The residue rewritten as condensed prose.** CV2 removes prose that bears no load rather than
  condensing it, and P11 types every loaded unit. Test: `check_statement` reds untyped text.
- **A second mover for the residue.** Unit 13's factory already walks a guide's sections and moves a
  span once. Test: unit 13 S1's `derive_moves` and `write_moves` take any `route`.
- **Rationale moved here too.** Unit 7 owns `help.explanation` and the no-lost-rationale arm, which
  key each section to its `explains` edge; moving rationale here would write that edge from two units.
  Test: unit 7 S5 to S7.

## 5. Production-readiness checklist

- security — no new write surface: the apply writes the sources and kit manifests a plan names, by
  unit 13's route, and refuses a plan any check fails.
- perf / scale — one pass over six documents; `check_residue_left` reads each source once.
- error / empty / loading states — an empty population prints `guide-move: no protocol document
  listed` and exits 0; an untyped entry refuses the whole apply, naming it.
- observability — `plan` prints each entry's source, section and kit, and a count per document.
- risks — a statement typed with a scope that loads it nowhere would be lost to every reader: the plan
  refuses `scope` blank, and unit 7's slices read the scopes at its pass.
- testing — AC1 to AC5 and the arm of §7.
- migration — S7.
- user docs — `tools/playbook/README.md`'s mover section gains `--residue`.

## 6. Acceptance criteria

- **AC1** — When `python guide_move.py --fixture --plant residue-move` runs, `plan --residue` writes one
  entry per paragraph and list item of the planted guide, and `apply --residue` over the entries typed
  writes one `[[unit]]` row per typed entry carrying its `scope` and `promoted-from=doc.<guide>#<seg>`,
  one change record each, removes those texts from the source, and leaves the `rationale` entry's text in
  place; a second apply writes nothing.
  Red when: a typed statement stays in the source, a rationale text leaves it, or a second apply writes.
- **AC2** — When `python guide_move.py --fixture --plant residue-untyped` runs, `apply --residue`
  refuses the plan naming the entry whose `disposition` is blank, and under `residue-narrative` the
  plan whose `directive` text opens with no modal, naming the rule `check_statement` returns; each
  writes nothing.
  Red when: an untyped or narrative statement is written as a unit.
- **AC3** — When `python guide_move.py --fixture --plant residue-left` runs, `python instructions_edit.py
  check` exits 1 naming `STATEMENT LEFT` for the planted `MUST` line and the pointer rule for the planted
  `the marker below`; with both removed it exits 0.
  Red when: a non-fact statement planted in a migrated document passes the check.
- **AC4** — When `python instructions_edit.py check` runs at this unit's pass tip, it exits 0, and
  `derive_migrated_documents` names each of the six documents of §4 Evidence.
  Red when: a migrated source keeps a modal line, or a document of the population is left unmigrated.
  figure: DERIVED at the pass.
- **AC5** — When `python instruction_units.py envelopes --check` runs at the pass tip, it exits 0 over
  the six sources.
  Red when: a move took an envelope line out of a source.

## 7. Gates

`govkit acceptance matrix` · `playbook render selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test`

The parents' legs `instruction units (schema, one fact)`, `instruction envelopes` and the leg that runs
`instructions_edit.py check` carry AC3 to AC5 once dOrderedCharter lands them; none is in the manifest
at base.

New arm: tools/playbook/guide_move.py · covers AC1 AC2 AC3 · the four `residue-*` plants of S6 in its `--selftest`, the residue's failing case a planted `MUST` line in a migrated guide · none

## 8. Open questions

- **F1 — What becomes of a section's prose that bears no load?** Options: (a) delete it, CV2's "should
  be gone"; (b) leave it in the source as `rationale` for unit 7 to move into `help`; (c) write it into
  the unit's `help` here. RESOLVED (agent, 2026-11-03, delegated): (b), rung 3, the most feature-rich
  survivor: (a) fails the owner's FQ-6 that no guide is retired while a section maps to no unit's
  rationale (veto 1 against cl-dClosedLoop-0481, which unit 7 carries), (c) writes unit 7's `explains`
  edge from a second unit, and (b) keeps the rationale where unit 7's mover reads it.
  widens: none · relaxes: none
- **F2 — Who sets a unit's `scope`?** Options: (a) the pass, per entry, refused blank; (b) every unit
  `reader.every`; (c) the document's own section tag alone. RESOLVED (agent, 2026-11-03, delegated):
  (a), rung 3: (b) loads every statement for every reader, the volume gap-spine-05 names; (c) reaches
  only a reader of that document, and the four guides unit 7 retires take their section tags with them;
  (a) is the judgment the derivation is, with the section tag added for the two documents unit 7 keeps
  rendered, whose slot lines select by it.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, the spec run's carrier of `cl-dClosedLoop-0475`.

## 10. Reuse audit

The seam extended is unit 13's `tools/playbook/guide_move.py` over the factory `prose_move.py` it
extracts from TOOL-dLinkedLibrary-19's `dossier_move.py` (I16), with PLAY-dOrderedCharter-12's
`check_statement` and `check_document` called and never copied, PLAY-dOrderedCharter-20 S9's `core.py
new unit` composing each row, and PLAY-dOrderedCharter-3's envelopes; every one is DEFERRED at base.
`python tools/codebase-map/reuse_lookup.py "derive protocol prose into typed statements and grade a
rendered document for non-fact lines"` ranked name-stem hits (`prose`, `check_line` in
`tools/runlog/runlog_lib.py`, `fact` in `tools/unattended/unattended.sh`, `unfenced_lines` in
`tools/memory-tree/tree_lib.py`): `unfenced_lines` is the fence walk S4 reads a source through, the
rest grade other text, so no live seam grades a statement type. Scout A's row says this unit "drains
whatever that legacy list still holds"; the guides leave the list only when unit 7 retires them and
`TEMPLATE-SPEC.md` and `HYGIENE.md` when unit 7 renders them (unit 7 S8, S10), so this unit drains
their directive text and hands the rows to unit 7. Each rejected candidate and its test are in §4.

Recall terms used: `python tools/memory-recall/query.py "how is protocol text derived to facts only and each document graded in its envelope" --terms "statement types facts-only check_document envelope legacy list instructions.edit residue guide"`
