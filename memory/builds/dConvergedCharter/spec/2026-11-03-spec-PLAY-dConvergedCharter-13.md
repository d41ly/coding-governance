# PLAY-dConvergedCharter-13 — feature-specific guide prose migrated into feature-scoped units through one prose mover

**Status:** DEFERRED · rev-5 · 2026-11-04 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 14 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0487@ff29708d whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-reuse-scout-a.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-19 |
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 PLAY-dConvergedCharter-41 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-04-prompt-PLAY-dConvergedCharter-7-r4-fold-brief.md](../prompts/2026-11-04-prompt-PLAY-dConvergedCharter-7-r4-fold-brief.md) | research | PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-40 |
| [2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 |
| [2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-41 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-40 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 |
| [2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-39 |

<!-- /gen:spec-records -->

## 1. Goal

The night pass settled that "instructions attach to a tag": `feature` becomes an instruction selector,
and pulling a feature's tag brings its instructions with its regions (night pass point 4, item 5,
`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md:264-265`; NP-13).
dLinkedLibrary arms the selector and moves the dossiers' prose out with `dossier_move.py plan|apply`;
the guides still hold paragraphs about one feature that load for every reader. This unit extracts the
mover as one factory at its second instance and moves each feature paragraph of a guide into a unit
scoped `feature.<name>`, its prose verbatim in the unit's `help`, so the guide keeps only what every
reader needs and unit 1 sees the step-scoped residue alone (gap-found-12).

## 2. Scope (IN)

Build-run preconditions, each landed before this unit's pass: TOOL-dLinkedLibrary-19 (`dossier_move.py`,
`read_feature_nodes`, `gen_map.py --feature-nodes`), TOOL-dLinkedLibrary-20 (the `feature` row
`selects`), TOOL-dTotalRecall-9 (`extract_section`, the `feature` namespace), PLAY-dOrderedCharter-3
(`documents.toml` and its `source` field), -9 (`[[unit]]` rows, `read_units`), -15
(`instructions_edit.py`, the change record), -20 (`core.py new unit`, the schema check,
`instructions-legacy.txt`), and this build's unit 19 (§3 Edges).

- **S1** — The factory, shared interface I16: `tools/lib/prose_move.py`, canonical, with the type
  `ProseMove` (`source`, `section`, `start`, `end`, `text`, `destination`, `stub`) and two functions.
  `derive_moves(text, route)` walks the document's `##` sections by `extract_section`'s rule (an
  authored `## [section.<seg>] <Title>` gives the tag, any other heading `derive_anchor`'s fold, shared
  interface I12) and returns every move `route(section)` yields, in document order, writing nothing.
  `write_moves(path, moves, write, written)` is idempotent on the DESTINATION, never on the source
  alone: it skips `write(move)` wherever the caller's predicate `written(move)` reads the move already
  at its destination, so a run that died after some writes and before `path` was rewritten re-runs
  writing no second row or record. The guide caller's `written` holds only when both parts of S4's
  write stand, the row (S5's predicate: an active unit whose `help`, whitespace squeezed, equals the
  move's text) and its change record (`Promoted-from` the section tag, `After` that row's
  `<tag>@<hash8>`), and its `write` writes each part only where it is missing, so a run that died
  between a row and its record re-runs writing the record alone; the dossier caller's is its existing
  destination test. It then replaces each move's span in REVERSE document order, each span re-located by
  its text in the current buffer rather than by the offsets taken at plan time, so one replacement never
  shifts another, and writes `path` once. A move whose text no longer stands, or that `written` reads
  done, is skipped and printed with its reason (`skipped <section>: text gone` or `skipped <section>:
  already at <destination>`), so a second run writes nothing and says why. Each copy-installed kit carries the two
  functions inline as a `# >>> prose_move — canonical copy` block, gated by a `prose_move` row of
  `PARITY_ROWS` in `tools/lib/resolve-python.test.sh`. Observed by AC4.
- **S2** — The first caller. `tools/codebase-map/dossier_move.py`'s `plan` and `apply`
  (TOOL-dLinkedLibrary-19 S3) call the inline block: its route yields one move per `seam:` line (the
  proposal destination) and one per other `##` section (the record destination), and keeps the H1, the
  fence, the `Prose:` line and the affordance block. Its outputs on its own fixture cases are byte-
  identical before and after. Observed by AC5.
- **S3** — The second caller, `python tools/playbook/guide_move.py plan|apply`. Its population is
  every guide row of `instructions-legacy.txt` (shared interface I17), each edited at the `source` its
  `documents.toml` row names. Its route: a paragraph is feature-specific to `feature.<name>` when it
  cites at least one backticked path and every path it cites matches that feature's `globs` and no
  other feature's, read from `gen_map.py --feature-nodes` as a subprocess (§8 F1). `plan --out <file>`
  writes one TOML entry per such paragraph, holding `source`, the section's `doc.<name>#<seg>` tag, the
  paragraph, `feature`, the kit holding its first cited path, and blank `type`, `level` and `text`,
  which the pass fills; it prints the count. `apply --plan <file>` refuses an entry whose `type` or
  `text` is blank, composes each row with `core.py new unit` (PLAY-dOrderedCharter-20 S9) and completes
  it with `scope = ["feature.<name>"]`, `help` the paragraph verbatim and the edge
  `promoted-from=doc.<name>#<seg>`, writes it by S4's route, and moves the paragraph out through
  `write_moves`. The route is chosen by a flag, no flag being this feature route, so a second route is
  one more route function over the same factory and write route: PLAY-dConvergedCharter-1 adds
  `--residue` and PLAY-dConvergedCharter-7 `--rationale`. Observed by AC1 and AC2.
- **S4** — The write route (§8 F2). `apply` appends each row to the kit's `instructions.toml` as the
  pass's own kit edit, writes its change record through `python tools/memory-tree/build_records.py new
  change` (`Action add`, `Promoted-from` the section tag, PLAY-dOrderedCharter-15 S7), and refuses the
  whole plan, writing nothing, when `instructions_edit.py check` fails over the would-be tree. It is
  the one route an agent pass writes kit rows by under `instructions.edit`'s default
  `owner-command-agents-propose` (`tools/policy/catalogue.toml:647-649`), whose door prints a proposal
  for an agent and writes nothing: PLAY-dConvergedCharter-7 writes its rationale rows through this
  `apply`, and PLAY-dConvergedCharter-12, which builds before this unit, writes its own by the same
  route, citing §8 F2 as the ruling. Observed by AC1.
- **S5** — The residue arm, `check_feature_prose(units, guides)` in `guide_move.py`: a guide source
  paragraph whose text, whitespace squeezed, equals the `help` of an active unit scoped `feature.*` is
  red, `FEATURE PROSE LEFT <path> <tag>`. It runs as one more check of `instructions_edit.py check`
  (PLAY-dOrderedCharter-15 S6), the leg that already grades every unit row. Observed by AC3.
- **S6** — The plants, `python tools/playbook/guide_move.py --fixture --plant <case>` in a throwaway
  tree with one guide, two dossier headers and one kit manifest: `feature-move`, `feature-twice`,
  `feature-two-features`, `feature-no-path`, `feature-left`, `feature-two-in-one` (two feature
  paragraphs in one guide, both moved by one apply), `feature-interrupted` (the second `write`
  raises after the first row and record are written; the re-run completes with no second row) and
  `feature-record-interrupted` (the record write raises after its row is appended; the re-run writes
  that record and no second row). `guide_move.py --selftest` runs each and is called by
  `adopt-playbook.sh --selftest`. Observed by AC1 to AC3.
- **S7** — The migration at this unit's pass: `plan` over gov's guides, each entry typed by the pass,
  `apply`, and the units and change records committed together. Every guide stays on
  `instructions-legacy.txt`: unit 7 takes it off the list at its own pass. Observed by AC6.

## 3. Non-goals (OUT)

- The step-scoped residue of each guide, written as facts: unit 1, through this unit's factory.
- Rendering guides from units, and retiring guides: units 10 and 7.
- The `feature` namespace, its members and its selector role: TOOL-dTotalRecall-9, TOOL-dLinkedLibrary-19
  and -20.
- A pointer line left in the guide where a paragraph moved: §8 F3.
- Dossier prose: TOOL-dLinkedLibrary-19's migration; this unit changes how `dossier_move.py` is built,
  never what it moves.

### Edges

- **consumes-from** `PLAY-dConvergedCharter-19` — `extract_section`'s rule honoured for guide headings, through which S1 reads a guide's sections; without it a retagged guide heading folds to a third spelling
- **hands-off** `PLAY-dConvergedCharter-1` — `guide_move.py`, the guide caller of the factory `prose_move.py`, with S4's write route, to which unit 1 adds `--residue`
- **hands-off** `PLAY-dConvergedCharter-7` — `guide_move.py`, the guide caller of the factory `prose_move.py` with S4's write route, to which unit 7 adds `--rationale` to move each retired guide section's rationale into a unit's `help` with an `explains=` edge
- **hands-off** `PLAY-dConvergedCharter-40` — `guide_move.py apply` and S4's write route, which that unit extends with an amend route for an entry whose target tag the kit manifest already holds, since S4 only appends
- **consumes-from** external — TOOL-dLinkedLibrary-19 and -20, TOOL-dTotalRecall-9, PLAY-dOrderedCharter-3, -9, -15 and -20, each DEFERRED at base and landed before this build run

## 4. Design

### Evidence

- None of the seams exists at base: `git ls-files` prints no `dossier_move.py`, `instructions.toml`,
  `documents.toml` or `instructions-legacy.txt` at `d8a12f046` (scout A's bottom line, re-run).
- The guides, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md` hold 424,697 bytes at `d8a12f046`
  (`wc -c`, PINNED), the figure scout A measured; the population this unit reads is DERIVED at the
  pass from the legacy list, after unit 12 removes the four unattended guides.
- The precedent for a shared block in copy-installed kits is a live `PARITY_ROWS` row,
  `resolve_bash_py` (`tools/lib/resolve-python.test.sh:369`): canonical `tools/lib/resolve_bash.py`,
  carried inline in `tools/policy/check_policy.py:896`; the table is `:351-370`.
  PLAY-dOrderedCharter-3 S3's `render_envelope` specifies the same shape and is unbuilt at base.

### The plan entry

```toml
[[move]]
source  = "tools/memory-tree/BUILD-METHOD.template.md"
section = "doc.build-method#recall-and-reuse"
feature = "feature.codebase-map"
kit     = "codebase-map"
help    = """<the paragraph, verbatim>"""
type    = ""     # filled by the pass: one of STATEMENT_TYPES
level   = ""     # filled by the pass: an S8 level
text    = ""     # filled by the pass: the typed line, within its budget
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/lib/prose_move.py` | canonical module | none |
| `ProseMove` | type | `py.type`, `OK` by `--suggest` |
| `derive_moves`, `write_moves`, `check_feature_prose` | functions | `py.function`, each `OK` by `--suggest` |
| `tools/playbook/guide_move.py` with `plan`, `apply`, `--fixture`, `--selftest` | module and verbs | none |
| `prose_move` | `PARITY_ROWS` marker | none |
| `FEATURE PROSE LEFT` | the arm's red prefix | none |

`plan` and `apply` keep `dossier_move.py`'s verb names: the lexicon grades function cells, and the
verbs are the first caller's interface, unchanged.

### Migration

S7, at this unit's pass. Its write set is DERIVED from the plan: each guide source and each kit
manifest the plan names, plus the change records, recorded as this unit's `--dispatch --writes`.

### Rollout

Live at landing in gov. `guide_move.py` ships with the playbook kit; an adopter's guides are kit
renders and move when the kit's own templates move, so an adopter runs nothing.

### Files touched (estimate)

- `tools/lib/prose_move.py`: new, S1
- `tools/lib/resolve-python.test.sh`: S1's parity row
- `tools/codebase-map/dossier_move.py`: S2
- `tools/playbook/guide_move.py`: new, S3 to S6
- `tools/playbook/instructions_edit.py`: S5's check
- `tools/playbook/adopt-playbook.sh`: S6's selftest call
- `tools/playbook/README.md`: the user docs of §5
- `tools/memory-tree/BUILD-METHOD.template.md`, `tools/memory-tree/ANNOTATION-STYLE.template.md`, `tools/workflows/REVIEW-PROTOCOL.template.md` and the other guide sources the plan names, with their renders under `memory/guides/`: S7
- each kit's `tools/<kit>/instructions.toml` the plan names: S7

### Alternatives rejected

- **A copy of `dossier_move.py`'s walk in the guide mover.** The charter's `[reuse]` rule extracts
  the factory at a kind's second instance. Test: both movers walk `##` sections, route each to a
  destination and must not write twice, the three properties S1 holds.
- **The factory imported from the codebase-map kit.** A kit imports no sibling kit
  (TOOL-dGroundRules-1 §4), and the playbook kit does not require codebase-map. Test:
  `tools/playbook/kit.toml` `requires = ["playbook"]` at base (`:16`).
- **Paragraphs routed by an authored marker in the guide.** It types beside the dossier globs that
  already say which paths a feature owns. Test: §8 F1.

## 5. Production-readiness checklist

- security — no new write surface: `apply` writes the guide sources and kit manifests a plan names,
  under the repository, and refuses a plan the checks fail.
- perf / scale — one `--feature-nodes` subprocess per run, one glob match per cited path.
- error / empty / loading states — an empty legacy list prints `guide-move: no guide listed` and exits
  0; a paragraph citing no path is not routed and is counted on the plan's summary line.
- observability — `plan` prints each entry's source, section and feature, and a summary count.
- risks — a feature whose globs overlap another's routes nothing; that paragraph stays for unit 1, and
  the plan prints it as `shared`.
- testing — AC1 to AC6 and the arms of §7.
- migration — S7.
- user docs — `tools/playbook/README.md` gains the mover's two verbs and the residue arm.

## 6. Acceptance criteria

- **AC1** — When `python guide_move.py --fixture --plant feature-move` runs, `plan` writes one entry
  under `feature.alpha` for the planted paragraph, and `apply` over that entry typed writes one
  `[[unit]]` row with `scope = ["feature.alpha"]`, `help` byte-equal to the paragraph and the edge
  `promoted-from=doc.<guide>#<seg>`, one change record, and the guide without the paragraph; under
  `feature-twice` a second `apply` writes nothing; under `feature-two-in-one` one apply writes two rows
  and the guide holds neither paragraph; under `feature-interrupted` the re-run after the raise leaves
  each paragraph's tag on exactly one row with one change record, prints the skipped move with `already
  at`, and the guide holds neither paragraph; under `feature-record-interrupted` the re-run leaves the
  row once and writes its one change record.
  Red when: the paragraph stays, the `help` differs from it, a second apply writes a byte, a span shifted
  by an earlier replacement drops a move with no line, or an interrupted run's re-run writes a duplicate
  row or record, or skips a move whose record is missing.
- **AC2** — When `python guide_move.py --fixture --plant feature-two-features` runs, `plan` writes no
  entry for the paragraph citing paths of two features, and under `feature-no-path` none for the
  paragraph citing no path; `apply` refuses an entry whose `text` is blank, writing nothing.
  Red when: a shared or pathless paragraph is routed, or an untyped entry is written.
- **AC3** — When `python guide_move.py --fixture --plant feature-left` runs,
  `python instructions_edit.py check` exits 1 naming `FEATURE PROSE LEFT` and the guide; with the
  planted paragraph removed it exits 0.
  Red when: a guide still holding a paragraph its feature unit carries passes the check.
- **AC4** — When the `prose_move` blocks in `dossier_move.py` and `guide_move.py` are compared with
  `prose_move.py` by the extraction `PARITY_ROWS` uses, both match.
  Red when: a copy drifts from the canonical block and the compare stays silent.
- **AC5** — When `python dossier_move.py --fixture --plant move` runs before and after S2, its outputs
  are byte-identical, and under its `twice` case a second `apply` writes nothing.
  Red when: the extraction changes what the dossier mover writes.
- **AC6** — When `python guide_move.py plan --out <file>` runs at this unit's pass BASE over gov's
  guides, the pass records the entry count `<n>` it prints, and `python gen_map.py --feature-nodes`
  there prints at least one feature with `globs`; at the pass tip the same `plan` writes no entry, `git
  grep -c 'scope = \["feature\.' -- 'tools/*/instructions.toml'` has grown by `<n>`, `build_records.py`
  lists `<n>` change records with `Promoted-from` a guide section, and `python instruction_units.py
  schema` and `python instructions_edit.py check` each exit 0 over the rows the pass wrote. Where `<n>`
  is 0, the pass records the probe that shows it: the plan's summary line counting every paragraph as
  pathless or `shared`, never an empty `--feature-nodes` read.
  Red when: a feature paragraph is left in a guide, a written row fails the schema, or the tip's empty
  plan is read as a migration when the base's plan moved nothing it should have.
  figure: DERIVED at the pass, `<n>` from the base's plan.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `govkit acceptance matrix` · `playbook render selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `python resolver (behaviour + inline parity + idiom ban)`

New arm: tools/playbook/guide_move.py · covers AC1 AC2 AC3 · its `--selftest` running the eight plants of S6 under `adopt-playbook.sh --selftest`, the residue's failing case `feature-left` and the idempotence cases `feature-interrupted`, staged red with `written` returning false, and `feature-record-interrupted`, staged red with `written` reading the row alone · none
New arm: tools/lib/resolve-python.test.sh · covers AC4 · the `prose_move` parity row, its failing case one byte changed in the guide mover's copy · none

## 8. Open questions

- **F1 — Which guide paragraph is feature-specific?** Options: (a) every backticked path it cites
  matches one feature's dossier `globs`, read from `gen_map.py --feature-nodes`; (b) an authored
  `gov:feature <tag>` marker beside each paragraph; (c) a list the owner curates. RESOLVED (agent,
  2026-11-03, delegated): (a), rung 3, the most feature-rich survivor: it derives from the dossier
  headers that already declare a feature's paths (TOOL-dLinkedLibrary-19 S1), routes nothing it cannot
  prove, and its two refusals are plants; (b) and (c) type a fact beside its owner ([derive]).
  widens: none · relaxes: none
- **F2 — How does an unattended pass write kit units when `instructions.edit` is
  `owner-command-agents-propose`, under which an agent's write through `instructions_edit.py` writes
  nothing?** Options: (a) `apply` calls `instructions_edit.py add` and files the proposals, the prose
  staying until the owner applies them; (b) the pass appends each kit row as its own kit edit and
  records it through the change record's stand-in door, refused unless `instructions_edit.py check`
  passes over the would-be tree, the route PLAY-dOrderedCharter-40 S2 takes for gov's first rows; (c)
  plant `instructions.edit = "command-for-all"` in gov's policy file for the pass. RESOLVED (agent,
  2026-11-03, delegated): (b), rung 3: (a) leaves the clause's migration undone at landing (veto 1),
  (c) widens the write grant of every caller (veto 3), and (b) writes only product files the pass owns,
  each with the record PLAY-dOrderedCharter-15 S7 names for a builder's kit-manifest change, the diff
  reviewed at the build's close. widens: none · relaxes: none
- **F3 — Does the guide keep a pointer where a feature paragraph left?** Options: (a) nothing; (b) a
  line naming `feature.<name>`. RESOLVED (agent, 2026-11-03, delegated): (a), rung 1: v2 P11 admits no
  prose that bears no load, and the feature's bundle lists its instructions (night pass point 4, item
  4), so a pointer would be a second route to one fact that unit 1 must then migrate.
  widens: none · relaxes: none
- **F4 — Where does the factory live?** Options: (a) canonical in `tools/lib/prose_move.py`, inline in
  each copy-installed caller under a parity row; (b) in the codebase-map kit, imported by playbook; (c)
  in the playbook kit, imported by codebase-map. RESOLVED (agent, 2026-11-03, delegated): (a), rung 3:
  (b) and (c) import a sibling kit, which TOOL-dGroundRules-1 §4 forbids, and (a) is the
  `resolve_bash_py` row's shape (§4 Evidence). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, the spec run's carrier of `cl-dClosedLoop-0487`.
- rev-2 · 2026-11-04 · S3 S4 §3 · folded `2026-11-04-review-PLAY-dConvergedCharter-1-spec-audit-round1` findings
  34 (the hands-off edge to PLAY-dConvergedCharter-7 names `guide_move.py` and the rationale route unit 7
  adds, not `dossier_move.py`; S3 names the route argument) and 33 (S4's write route, ruled in §8 F2, is
  the one units 7 and 12 write their rationale rows by).
- rev-3 · 2026-11-04 · S1 S6 AC1 AC6 §7 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1` findings 11 (AC6 records the plan's count at
  the pass base and requires that many feature rows and change records at the tip, a 0 stated with its
  probe) and 42 (`write_moves` skips on the destination through the caller's `written` predicate,
  replaces spans in reverse order re-located by text and prints each skip; the plants
  `feature-two-in-one` and `feature-interrupted`).
- rev-4 · 2026-11-04 · §3 · sibling edit by the repair unit PLAY-dConvergedCharter-40 for
  `2026-11-04-review-PLAY-dConvergedCharter-22-spec-audit-round1` finding 27: the hands-off edge to that
  unit, which adds `apply`'s amend route beside S4's append.
- rev-5 · 2026-11-04 · S1 S6 §3 §4 §8 AC1 §7 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1` findings 37, the skeptic's
  corrected fix (the guide caller's `written` holds only when the row and its change record both stand,
  and `write` writes the missing part alone; the plant `feature-record-interrupted` and its AC1 clause),
  10 (the hands-off edge to PLAY-dConvergedCharter-1 names `guide_move.py` and the `--residue` route
  unit 1 adds) and 19 (§4 Evidence and F4 cite the live `resolve_bash_py` row, `render_envelope` marked
  unbuilt).

## 10. Reuse audit

The seam extended is TOOL-dLinkedLibrary-19 S3's `dossier_move.py plan|apply`, the first instance,
extracted here at its second as `tools/lib/prose_move.py` (S1), with PLAY-dOrderedCharter-20 S9's
`core.py new unit` composing each row and PLAY-dOrderedCharter-15 S7's change record recording it; the
parity table at `tools/lib/resolve-python.test.sh:351-370` is live and read at source. `python
tools/codebase-map/reuse_lookup.py "move a document's prose sections into units and records with a
plan then apply"` ranked name-stem hits (`records`, `prose` in `merge-rows.test.sh`, `plan` in
`gen_build_index.py`, `read_plan_destinations` in `govkit.py`), none a section mover: `merge-rows.py`
merges conflicting rows and `read_plan_destinations` reads govkit's install plan, so no live seam fits
beyond the deferred parent. The scout row agrees with source on every point checked: no
`dossier_move.py` exists at base, and the parents' specs spell `plan`, `apply` and `scope =
["feature.<x>"]` as scout A cites them. Each rejected candidate and its test are in §4.

Recall terms used: `python tools/memory-recall/query.py "how is feature-specific guide prose moved into feature-scoped instruction units with its rationale in help" --terms "feature selector instruction unit scope help rationale guide prose dossier move plan apply"`
