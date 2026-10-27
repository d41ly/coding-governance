# TOOL-dLinkedLibrary-1 — decisions split by kind: reuse entries as level-3 units, the major-decision log, its rows routed by two raters, and the `[records]` rule reworded

**Status:** DEFERRED · rev-3 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 8 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0238@b2c1827b whole
**Carries:** node:policy-key.decisions.major
**Carries:** node:policy-key.reuse.propose
**Carries:** node:record-kind.decision

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-deviation-11.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-deviation-11.md) | deviation | — |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-fix-return.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-fix-return.md) | research | TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-a.md) | research | TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-b.md) | research | TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-c.md) | research | TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-d.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-d.md) | research | TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-23 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-1-reuse-scout.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-1-reuse-scout.md) | journal | — |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-2-reuse-scout.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-2-reuse-scout.md) | journal | — |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-3-reuse-scout.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-3-reuse-scout.md) | journal | — |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-4-reuse-scout.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-4-reuse-scout.md) | journal | — |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-5-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-5-spec-writer.md) | journal | — |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-6-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-6-spec-writer.md) | journal | — |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-fix-brief.md) | research | TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-1-owner-review-until-no-high.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-1-owner-review-until-no-high.md) | research | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-1-owner-stop-chain.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-1-owner-stop-chain.md) | research | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-1-spec-writer.md) | journal | TOOL-dLinkedLibrary-54 |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-86-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-86-1-spec-writer.md) | journal | TOOL-dLinkedLibrary-86 |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-87-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-87-1-spec-writer.md) | journal | TOOL-dLinkedLibrary-87 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 |

<!-- /gen:spec-records -->

## 1. Goal

The decision index holds the wrong things and instructs no one: 213 rows at `82a392696`, a few of
them major decisions or features others must reuse, none carrying a reuse instruction, and recall
opened the file 0 times in 121 opens (gap-mem-02). No reuse instruction reaches an agent: each
dossier's `## Reuse affordance` block holds the facts and no instruction carries them (gap-mem-03).
Layer-memory `[decisions]` (:620-715) splits the index by what each row is: a reuse entry becomes a
level-3 instruction unit beside its dossier, the log keeps major product decisions only, every other
row goes to its true home after two raters agree on it at kappa 0.8 or better, and the charter's
`[records]` rule says so. This unit lands those four, with `decisions.major` and `reuse.propose` and the
`decision` record kind.

## 2. Scope (IN)

- **S1** — The reuse entry (shared interface I1). A part file `memory/map/features/<feature>.reuse.toml`
  beside the dossier `<feature>.md`, or `memory/map/conventions/<name>.reuse.toml` for a convention
  that crosses features, holding one `[[unit]]` table in PLAY-dOrderedCharter-9 S1's field set and
  its `[unit.reuse]` table (§4 "The entry"): `tag` `unit.reuse.<stem>`, `level` 3, `type` `directive`,
  `budget` `line`, `text` opening `MUST`, `owner` the build that made it; and in `reuse` the six facts,
  `tag` (`feature.<name>`), `needs`, `anchors`, `date`, `build` and `decision`. One reader,
  `read_reuse_entries(root)` in `tools/memory-tree/reuse_entries.py`, returns every entry with its state
  (S3) for every later reader. Observed by AC1.
- **S2** — The entry check, `check_reuse_entries(root)`, run as `python reuse_entries.py check` and
  called once from `cmd_check` in `tools/memory-tree/gen_build_index.py` (:2865), its findings under
  `build-index VERDICT — reuse entry`: a part that does not parse, holds other than one `[[unit]]`, or
  whose `tag` is not `unit.reuse.<file stem>`; a `level` other than 3, a `type` other than `directive`
  or a `text` not opening `MUST`; a `reuse` table missing one of the six keys; a feature part whose
  `reuse.tag` is not `feature.<stem>` or with no dossier `<stem>.md` beside it; a `build` naming no
  build folder; a `decision` naming no row of the log or its archive and not reading `none — <why>`.
  Observed by AC2.
- **S3** — Proposed with the build, rendered once accepted. `python reuse_entries.py propose --name
  <n> (--feature | --convention) --text "<MUST …>" --need <phrase>… --anchor <site>… --build <slug>
  --unit <id> [--decision <id>]` composes the part, runs PLAY-dOrderedCharter-15 S2's `instructions_edit.py
  propose` over it, and writes the proposal record
  `memory/builds/<slug>/build/<date>-build-<unit id>-reuse-proposal-<n>.md` (`**Serves:** journal <unit
  id>`) holding the part in a `toml` fence and the apply command `propose` printed; it writes nothing
  under the map. `python reuse_entries.py accept <proposal>` runs that apply command, whose write
  `instructions.edit` admits only with the owner's proof (PLAY-dOrderedCharter-15 S3), and only on its
  success appends `- **Disposition:** accepted <date>` to the proposal; `reject <proposal> --why
  "<reason>"` appends `- **Disposition:** rejected <date> — <why>` and writes no part. An entry's state
  is `accepted` for a part on disk, `proposed` for a proposal with no disposition and `rejected` for a
  rejected one; only an accepted part is an instruction unit, so only it renders into work orders.
  Observed by AC3.
- **S4** — `reuse.propose`, read through `resolve` (`tools/policy/policy.py:752`):
  `derive_owed_units(root, slug)` and `python reuse_entries.py owed <slug>` print the units of a
  build that owe a reuse line when they close: under `new-seam`, the default, each unit whose
  spec's §10 records `no existing seam fits`; under `every-unit`, every unit of the build's roster; under `owner-asks`, none,
  with the line `reuse.propose: owner-asks — the owner names the features to enter`. Its catalogue row
  (`tools/policy/catalogue.toml:340`) gains `summary` and `usage`. Observed by AC4.
- **S5** — The rubric and the agreement (shared interface I2), `tools/memory-tree/decision_rubric.py`:
  `CLASSES`, the six classes of §4 "The rubric" with each one's home; `RUBRIC`, the questions a rater
  answers per row; `derive_kappa(rows_a, rows_b)`, Cohen's kappa over the class labels of two raters,
  refusing two label sets over different row ids or an empty set; `python decision_rubric.py rows`,
  printing each live row of `memory/DECISIONS.md` as `<id>\t<text>` through `row_grammar.parse_row`
  (`tools/memory-tree/row_grammar.py:598`); and `python decision_rubric.py agree <labels-a> <labels-b>`,
  printing `kappa <k> over <n> rows · pass` at 0.8 or above and exiting 0, else `· revise` and exiting
  1, then one line per split row. Observed by AC5.
- **S6** — The re-run. On `revise`, the pass revises `RUBRIC` in a commit, draws one row through
  TOOL-dDeclaredLoop-30 S3's `python tools/loop/budget.py draw --build dLinkedLibrary --cause
  re-dispatch --item TOOL-dLinkedLibrary-1`, and re-runs both raters; `decision_rubric.py redraw` is
  that draw, printing the budget line, and on `exhausted` (exit 3) it prints `rework budget spent`
  and the driver verb `unattended.sh --exhausted dLinkedLibrary`, and exits 3, so the run ends as
  `flow.on-exhausted` says, the ending TOOL-dDeclaredLoop-31 S3's.
  No row moves until `agree` prints `pass`. Observed by AC6.
- **S7** — `decisions.major`, read through `resolve` by `decision_rubric.py route`: under
  `author-rubric`, the default, the raters' agreed class settles a row; under `author-owner-ratifies`,
  an agreed `major` row is settled only by the owner's `ratified` mark on its line of the routing
  record; under `owner-only`, a row the raters class `major` or split on is settled only by the
  owner's ruling there. A split row is the owner's under every value (layer-memory :703-708). Its
  catalogue row (:364) gains `summary` and `usage`. Observed by AC7.
- **S8** — The move. `python decision_rubric.py route <labels-a> <labels-b> [--rulings <file>]`,
  refused unless `agree` passes, writes the routing record
  `memory/builds/dLinkedLibrary/build/<date>-build-TOOL-dLinkedLibrary-1-decision-routing.md`: one
  table row per log row, its two labels, its settled class or `awaiting the owner`, and its home. Each
  settled row of a class other than `major` whose home the raters both named leaves the log by the
  existing rotation, byte-identical, into `memory/archive/DECISIONS.<date>.md`, with the rotation note
  at the log's head that check 10 reads; the log gains one row, `TOOL-dLinkedLibrary-1`, naming the
  archive and the routing record, carrying one `decides=record-kind.decision` segment in
  TOOL-dLinkedLibrary-22's form (I6) and at most 300 characters. Major rows, unsettled rows and rows
  whose home the raters disagree on stay. Observed by AC8.
- **S9** — The `decision` record kind: a row appended to `tools/memory-tree/record-kinds.toml`
  through TOOL-dTotalRecall-1 S9's `python record_kinds.py new decision --tag record.decision --writer
  hand --check "memory hygiene"`, schema form `rows`, home `memory/DECISIONS.md`, node
  `record-kind.decision`; its writer stays `hand` until dScopedBuild's `build.distill` appends a
  major fork's row. Observed by AC9.
- **S10** — The map root admits the conventions folder: check 3's map arm in
  `tools/memory-tree/check-memory-hygiene.sh` (:850) adds `D:conventions`, and the "Codebase-map
  interop" prose of `tools/memory-tree/HYGIENE.template.md` names it, re-rendered into
  `memory/HYGIENE.md`. Observed by AC10.
- **S11** — The `[records]` rule reworded in `coding-governance-agents.template.md` (:36), rendered
  into `AGENTS.md` (:37) by `tools/playbook/render_playbook.py`: "Record each decision in its build as
  it is made, log a major one, make a reusable feature or convention a reuse entry, record each
  experiment's instruments beside its results, and commit them before the push and the wrap-up."
  Observed by AC11.
- **S12** — The fixtures: `python reuse_entries.py --fixture [--plant <case>]`, cases `entry`,
  `bad-tag`, `no-dossier`, `bad-decision`, `propose`, `accept-unproven`, `reject`, `owed-new-seam`,
  `owed-every-unit`, `owed-owner-asks`; and `python decision_rubric.py --fixture [--plant <case>]`,
  cases `kappa`, `kappa-perfect`, `revise`, `exhausted`, `route`, `ratifies`, `owner-only`. Each builds
  a throwaway repository with stub `instructions_edit.py` and `budget.py` answering as their specs
  state, and a planted `.governance/policy.toml` where a case sets a key. `gen_build_index.py
  --selftest` runs every case. Observed by AC1 to AC8.
- **S13** — The docs: `tools/memory-tree/README.md` names both modules and their verbs;
  `KIT_MEMORY_TREE_VERSION` moves. NOT OBSERVED by a criterion: prose, graded by `memory hygiene`.

## 3. Non-goals (OUT)

- The holds-now and reuse views: TOOL-dLinkedLibrary-5 renders both from S1's reader and the log.
- `build.distill`, `build.ratify` and `deploy.distill`, which append and confirm a major fork's row
  at landing: dScopedBuild's and dShippedRelease's, reading `decisions.major` there.
- The witness that a closing unit carries its reuse line: dScopedBuild's `build.unit-pass`, which
  calls S4's `derive_owed_units`.
- The `gov:feature` anchors and their both-ways check with entries: TOOL-dLinkedLibrary-4.
- Seeding proposals from the dossiers' seam lines: TOOL-dLinkedLibrary-19, through S3's verb.
- Rewriting the charter's facts line about `memory/DECISIONS.md`, which the layer names and the clause
  does not.
- Copying a routed row's text into its home: a row moves only where its home already holds the fact
  (§4 "The move").

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-22` — `decides`, the segment S8's pointer row carries in the form unit 22 gives every decision row
- **hands-off** `TOOL-dLinkedLibrary-5` — `reuse.toml`, the entries `read_reuse_entries` returns for the reuse view
- **hands-off** `TOOL-dLinkedLibrary-4` — `reuse.toml`, the entries whose `anchors` the both-ways check joins to `gov:feature` anchors
- **hands-off** `TOOL-dLinkedLibrary-2` — `reuse.toml`, the entries the house index digests
- **hands-off** `TOOL-dLinkedLibrary-8` — `derive_kappa`, the two-rater agreement `adopt.decisions` calls
- **hands-off** `TOOL-dLinkedLibrary-19` — `reuse.toml`, the `propose` verb each dossier's `seam:` line seeds an entry through
- **consumes-from** external — PLAY-dOrderedCharter-9 S1 and S4, -15 S2 and S3, -20 S1 (the unit row, `propose`, `add`, `instructions.edit`, the schema check); TOOL-dDeclaredLoop-30 S3 and -31 S3 (the draw and the ending); TOOL-dTotalRecall-1 S9 (the kind factory); each DEFERRED at base and built before this build run
- **hands-off** external — §8 F1's ask to dOrderedCharter, without which S3's `accept` refuses naming it
- **hands-off** `TOOL-dLinkedLibrary-38` — `check_reuse_entries` and `propose`, whose feature rule unit 38 keys on the part name's stem before its first dot (id 1 of the round-1 spec audit)
- **hands-off** `TOOL-dLinkedLibrary-52` — `decision_rubric.py`, whose labels reader and settler unit 52 exports for the adopt program, and the pointer row whose segment lead it fixes (ids 38, 19)
- **hands-off** `TOOL-dLinkedLibrary-59` — `decision_rubric.py` and S8's routing record, which unit 59's `log-diff` reads to class the log's removed lines (id 1 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-60` — `propose` and `--feature`, whose valued form unit 60 adds before unit 19's pass (id 2 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-64` — `accept`, which unit 64 guards with `--anchor-absent-ok` (id 6 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `memory/DECISIONS.md` holds 213 `- ` rows under four family sections at `82a392696` (PINNED), one
  rotation note (:3), and the rule that a landed row is never edited (:5-6). The clause says 200: the
  departure is `2026-10-26-build-TOOL-dLinkedLibrary-1-deviation-11.md`.
- The map root is sanctioned by name (`check-memory-hygiene.sh:850`), so `conventions/` reds today.
  `load_map_tree` reads `features/*.md` only (`tools/codebase-map/map_lib.py:1143`), so a `.reuse.toml`
  part beside a dossier is never read as one.
- The facts to carry: each dossier's `## Reuse affordance` block, parsed by `parse_affordance`
  (`map_lib.py:1290`), and its `decisions = [...]` key (`parse_dossier`, :1022).
- `decisions.major` (`catalogue.toml:364`) and `reuse.propose` (:340) are owned by dLinkedLibrary and
  listed in `tools/policy/unsummarised-keys.txt`.

### The entry

```toml
# memory/map/features/media-picker.reuse.toml
[[unit]]
tag = "unit.reuse.media-picker"
level = 3
type = "directive"
scope = ["reader.every"]
trigger = "always"
budget = "line"
text = "MUST reuse the media picker wherever an image, video or media selector is needed."
owner = "dExampleBuild"

[unit.reuse]
tag = "feature.media-picker"
needs = ["media selection", "a new page"]
anchors = ["gov:feature media-picker"]
date = "2026-10-26"
build = "dExampleBuild"
decision = "none — the build's own spec settles it"
```

`needs` is what `reuse.delivery` matches a build's needs against (TOOL-dLinkedLibrary-2); `anchors`
the sites TOOL-dLinkedLibrary-4 joins both ways; `decision` the log row that made it, or `none — <why>`.

### The rubric

| Class | Home | A row moves when |
|---|---|---|
| `major` | the log | never: it stays |
| `reuse` | a reuse entry, S1 | its proposal is recorded |
| `owner-ruling` | the policy value it set, `policy:<key>` | the key's catalogue row or policy file holds it |
| `process-rule` | the method or protocol text, a path | that text states it |
| `waiver` | the gate's row registry, a path | the registry holds the row |
| `minor` | the build's own records, or a gotcha | the named record holds it |

A rater's labels file is a record under this build, `…-decision-labels-a.md` or `-b.md`, holding in a
fence one line per row, `<id>\t<class>\t<home>`. The raters are two `gov-researcher` agents the
pass dispatches, each handed `RUBRIC` and `rows`'s output, neither the other's file.

### The agreement

`derive_kappa` computes `(p_o - p_e) / (1 - p_e)`, `p_o` the share of rows with one class from both
raters and `p_e` the sum over classes of the product of each rater's share; where `p_e` is 1 and the
labels agree it returns 1.0. A row two raters class alike but home differently is agreed on class
and stays in the log (S8).

### The move

```
- **TOOL-dLinkedLibrary-1** — the log keeps major decisions only: <n> rows rotated to archive/DECISIONS.<date>.md, each row's home in builds/dLinkedLibrary/build/<routing record>. decides=record-kind.decision
```

Rotation keeps every id resolvable: check 18 resolves a gotcha's `decision:` over the corpus, archive
included (`tools/memory-tree/gotchas.py:416`), and the rotation is byte-identical, as the 2026-08-10
rotation of 79 rows was. `ROTATION_MODE` is `cut` here, so check 24 grades that no rotated id stays in
the live index.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `reuse_entries.py`, `decision_rubric.py` | modules, `tools/memory-tree/` | none |
| `read_reuse_entries`, `check_reuse_entries`, `derive_owed_units` | functions, `reuse_entries.py` | `py.function`, asked at the pass |
| `propose`, `accept`, `reject`, `owed`, `check` | verbs of `reuse_entries.py` | none |
| `CLASSES`, `RUBRIC`, `derive_kappa` | names in `decision_rubric.py` | `py.function`, asked at the pass |
| `rows`, `agree`, `redraw`, `route` | verbs of `decision_rubric.py` | none |
| `<name>.reuse.toml`, `memory/map/conventions/` | file grammar and folder | none |
| `- **Disposition:**` | proposal record field | none |
| the pointer row | a log row under this unit's id | none |
| `decision` | registry row, node `record-kind.decision` | none |

### Migration

The routing is the migration, run in this unit's pass: `rows`, the two raters, `agree`, any
re-runs, `route`, the rotation and the pointer row, committed with the labels and the routing record.

### Rollout

Live at landing. A tree with no map has no entries and S2 reads none; `propose --convention` and
`--feature` refuse there, naming the map.

### Files touched (estimate)

- `tools/memory-tree/reuse_entries.py`: new, S1 to S4, S12
- `tools/memory-tree/decision_rubric.py`: new, S5 to S8, S12
- `tools/memory-tree/gen_build_index.py`: S2's call in `cmd_check`, S12's selftest arm
- `tools/memory-tree/record-kinds.toml`: S9's row, through its factory
- `tools/memory-tree/check-memory-hygiene.sh`: S10, `KIT_MEMORY_TREE_VERSION`
- `tools/memory-tree/HYGIENE.template.md` and its render `memory/HYGIENE.md`: S10
- `tools/memory-tree/README.md`: S13
- `tools/policy/catalogue.toml`: the two rows' `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`: drained by `policy.py lists --write`
- `coding-governance-agents.template.md` and its render `AGENTS.md`: S11
- `memory/DECISIONS.md`: the rotation note and the pointer row
- `memory/archive/`: the new archive file of the rotated rows

### Alternatives rejected

- **A pointer row per routed row.** Each would need its own id in a family that mints one per unit,
  and the log would grow by the rows it sheds; one row naming the archive and the routing record keeps
  every id resolvable.
- **The entry's facts as top-level unit keys.** PLAY-dOrderedCharter-20 S1 reds an unknown key; one
  nested table is one admission to ask for.
- **The proposal written straight into the part.** It would put an unaccepted instruction where the
  instruction layer reads, bypassing `instructions.edit`'s one door.

## 5. Production-readiness checklist

- security — the one new instruction write goes through PLAY-dOrderedCharter-15's command and its
  owner proof; an agent's `accept` writes nothing. A rater reads rows and writes its labels record only.
- perf / scale — `rows` reads one file; `derive_kappa` is linear in the rows; S2 reads the parts, 0
  at base.
- error / empty / loading states — `agree` refuses mismatched or empty label sets; `route` refuses
  before `pass`; `accept` refuses naming §8 F1's ask while the instruction layer lists no part.
- observability — the routing record lists every row, its labels and its fate; every budget draw is
  a transition row.
- risks — a mis-rated row leaves the log for the archive, where its id still resolves and the routing
  record names its home; the owner rules on every split.
- testing — S12's fixture cases, run by `gen_build_index.py --selftest`.
- migration — the routing, §4 "Migration".
- user docs — the memory-tree README; `help/policy.md` lists policy keys from the catalogue.

## 6. Acceptance criteria

- **AC1** — When `python reuse_entries.py --fixture --plant entry` runs over a feature part, a
  convention part and a proposal record, `read_reuse_entries` returns three entries with states
  `accepted`, `accepted` and `proposed`, each carrying the six `reuse` facts.
  Red when: an entry's state or a fact is lost.
- **AC2** — When the plants `bad-tag`, `no-dossier` and `bad-decision` run, `python reuse_entries.py
  check` exits 1 naming the part and the finding of S2 each plants; with no plant it exits 0.
  Red when: a part whose tag misnames its file, a feature part with no dossier, or a decision naming
  no row passes.
- **AC3** — When the plant `propose` runs `propose` against the stub `instructions_edit.py`, the build
  folder gains the proposal record and no file under the map changes; under `accept-unproven`, with
  the stub refusing the write as an unproven caller, `accept` leaves the proposal without a
  `Disposition` line and writes no part; under `reject`, the record gains `rejected` and no part.
  Red when: an unproven `accept` writes a part or marks the proposal accepted.
- **AC4** — When the plants `owed-new-seam`, `owed-every-unit` and `owed-owner-asks` each set
  `reuse.propose` in a planted `.governance/policy.toml` over a build of three units, one of whose
  §10 records `no existing seam fits`, `python reuse_entries.py owed tFix` prints that one unit, all
  three, and the `owner-asks` line in turn.
  Red when: a value's selection differs, or an unset key reads other than `new-seam`.
- **AC5** — When `python decision_rubric.py --fixture --plant kappa` runs `agree` over four rows
  labelled `major minor minor waiver` and `major minor waiver waiver`, it prints `kappa 0.636 over 4
  rows · revise`, names the third row, and exits 1; under `kappa-perfect` it prints `kappa 1.000` and
  `pass`.
  Red when: the kappa differs from Cohen's, or a split row is not named.
- **AC6** — When the plant `revise` runs `redraw` against a stub budget with draws left, the stub
  records one `re-dispatch` draw for `TOOL-dLinkedLibrary-1`; under `exhausted`, `redraw` prints `rework
  budget spent` naming `--exhausted dLinkedLibrary` and exits 3, and `route` still refuses.
  Red when: a re-run draws nothing, or rows move after the budget is spent.
- **AC7** — When the plants `ratifies` and `owner-only` set `decisions.major` to
  `author-owner-ratifies` and `owner-only` over a routing whose raters agree a row is `major`, `route`
  lists that row `awaiting the owner` until the rulings file marks it; with the key unset the same row
  is settled `major`.
  Red when: a value other than `author-rubric` settles a major row without the owner.
- **AC8** — When the plant `route` runs `route` over six rows, two `major`, two `waiver` with one home,
  one split and one `minor` with two homes, the archive holds the two waiver rows byte-identical, the
  log keeps the other four and gains one pointer row of at most 300 characters carrying
  `decides=record-kind.decision`, and the routing record lists all six with their fates.
  Red when: a major, split or home-disputed row leaves the log, or a moved row's bytes change.
- **AC9** — When `python record_kinds.py --check` runs at this unit's tip, it passes with the
  `decision` row present.
  Red when: the row is missing or names no leg.
  fixture: the registry is TOOL-dTotalRecall-1's, absent at base until it lands.
- **AC10** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 3` runs at this unit's tip
  with a convention part tracked, it prints no `unexpected entries` line naming `conventions`.
  Red when: check 3 refuses the folder.
- **AC11** — When `grep -n "^- \[records\]" AGENTS.md` runs after `python
  tools/playbook/render_playbook.py` renders the template, it prints S11's sentence, and the template's
  line at `coding-governance-agents.template.md` reads the same.
  Red when: the rendered rule differs from the template or keeps the old wording.
- **AC12** — When `python tools/policy/policy.py get decisions.major` and `get reuse.propose` run with
  no policy file setting them, they print `author-rubric` and `new-seam`, and after `policy.py lists
  --write` neither key is in `unsummarised-keys.txt`.
  Red when: a row lacks `summary` or `usage`.

## 7. Gates

`memory hygiene` · `build-index selftest` · `tier2-review self-test` · `policy fixtures` · `policy check` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `playbook render wiring` · `playbook parity` · `charter size` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the `--selftest` arm running both modules' `--fixture` cases, its failing case the `accept-unproven` plant writing a part · none

## 8. Open questions

- **F1 — How does a reuse entry beside its dossier become a unit the instruction layer reads?**
  Options: (a) an ask to dOrderedCharter that `read_manifests` list every `*.reuse.toml` part under
  `memory/map/features/` and `memory/map/conventions/` as an overlay part, that `instructions_edit.py
  add --manifest` take a part's path, and that the schema check admit the `reuse` table on a row whose
  tag opens `unit.reuse.`; (b) the unit row in the overlay `.governance/instructions.toml` and only
  the facts beside the dossier; (c) a writer of this unit's own that writes the part after its own
  proof test. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor:
  (b) puts the unit away from its dossier, failing the clause's "beside their dossiers" (veto 1), and
  (c) is a second door beside `instructions.edit` and a copy of its proof (veto 3, and `[core]`). The
  ask, for dOrderedCharter's `BACKLOG.md`: accept `python instructions_edit.py add --manifest
  memory/map/features/<f>.reuse.toml` writes a part whose row `instruction_units.py schema` passes and
  `derive_unit_selection` selects, seen on a fixture part. widens: none · relaxes: none
- **F2 — Where does a routed row go?** Options: (a) rotated byte-identical into an archive with one
  pointer row naming the archive and the routing record; (b) a pointer row per routed row; (c) the row
  left in place with a status. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1: layer-memory
  :687-689 says a row "leaves only by the existing rotation" and "a routed row is superseded by a
  pointer row"; (b) needs an id per pointer in a family minted per unit, and (c) edits a landed row,
  which the log's rule refuses (`memory/DECISIONS.md:5-6`). widens: none · relaxes: none
- **F3 — How is the `[records]` rule reworded?** Options: (a) the layer's point 4 folded into the one
  rule; (b) a second rule for reuse entries. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3:
  one rule keeps one fact in one place and adds about 60 bytes to `AGENTS.md` (16,732 bytes against
  its 20,480 ceiling, PLAY-aOrientedCast-3); a governance-carrier change the clause names, lifted by
  the README's grant.
  grants: PLAY-dClosedLoop-3 the `[records]` rule reworded · widens: none · relaxes: none
- **F4 — Which population do the raters route?** Options: (a) every live row at the routing's base,
  213 at `82a392696`; (b) the clause's 200, the first 200 rows. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3: (b) leaves 13 rows unrouted with no rule for them, and the clause's "today's
  200" names the live population at the time it was written; the departure is recorded as deviation
  11. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 1, layer-memory `[decisions]`,
  layer-library LB-2, LB-3, `[reuse-proposal]` and `[log]`, PLAY-dOrderedCharter-9, -15 and -20,
  TOOL-dDeclaredLoop-30 and -31, and scout A's row 1.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-38, TOOL-dLinkedLibrary-52, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-59, TOOL-dLinkedLibrary-60, TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seams extended are PLAY-dOrderedCharter-9 S1's unit row and -15 S2's `propose` and `add`, which an
entry is a row of and is written through; `row_grammar.parse_row` (`tools/memory-tree/row_grammar.py:598`)
for the rows; the log's existing rotation and its note, which check 10 and check 24 already grade;
TOOL-dDeclaredLoop-30's `budget.py draw` and -31's `--exhausted` for the re-run; TOOL-dTotalRecall-1
S9's factory; and `resolve` (`tools/policy/policy.py:752`). `python tools/codebase-map/reuse_lookup.py
"split decision log rows into major decisions and reuse entries rated by two raters with agreement"`
ranked test helpers first (`rows` with fan-in 128, `row` 123) and then `extract_row` and
`read_catalogue_row`; none rates or routes a row, and `git grep -i kappa` over `tools/` finds no
agreement measure, so no existing seam fits the rubric or the agreement and S5 adds them. Scout A
stated that no rule governs the map root's files (its disagreement 6, after layer-memory :638-639):
source disagrees, since check 3's map arm admits six names (`check-memory-hygiene.sh:850`), so S10
admits the folder. Its "today's 200 rows" is 213 at `82a392696`.

Recall terms used: `python tools/memory-recall/query.py "how are decision rows split into major decisions and reuse entries" --terms "decision log major decisions reuse entry kappa raters rubric routing records rule decisions.major reuse.propose"`
