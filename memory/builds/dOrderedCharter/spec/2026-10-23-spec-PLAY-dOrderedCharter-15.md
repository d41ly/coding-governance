# PLAY-dOrderedCharter-15 — the instruction manifest and its guarded write command, each change recorded, and the pack catalogue

**Status:** DEFERRED · rev-5 · 2026-10-25 · node d · Tier-2 · base ce13efbe · streams playbook · order 16 · advances PLAY-dOrderedCharter-38 · ratified 2026-10-25

**Carries:** cl-dClosedLoop-0045@f345dc78 whole

**Carries:** node:policy-key.instructions.edit

**Carries:** node:policy-key.instructions.proof

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return-2.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-edge-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-reuse-scout-a.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-27 |
| [2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md](../build/2026-10-23-build-PLAY-dOrderedCharter-1-token-fix-return.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-build-PLAY-dOrderedCharter-15-deviation-151.md](../build/2026-10-24-build-PLAY-dOrderedCharter-15-deviation-151.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-15-deviation-152.md](../build/2026-10-24-build-PLAY-dOrderedCharter-15-deviation-152.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |
| [2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-25-build-PLAY-dOrderedCharter-15-deviation-153.md](../build/2026-10-25-build-PLAY-dOrderedCharter-15-deviation-153.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-15-deviation-154.md](../build/2026-10-25-build-PLAY-dOrderedCharter-15-deviation-154.md) | deviation | — |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-edge-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-spec-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md](../prompts/2026-10-23-prompt-PLAY-dOrderedCharter-1-token-fix-brief.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md](../prompts/2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-46 |
| [2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md](../reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-37 |

<!-- /gen:spec-records -->

## 1. Goal

There is no write path for instructions (gap-found-15): the owner changes one only by editing a source or the
template by hand, with no manifest, no validating command, no recorded change and no pack beyond the
practice catalogue. R-I gives each kit a manifest and the repository an overlay, merged as row stores, and one
command that adds, edits, removes, lists, renders and checks units, proving its caller is the owner by
`instructions.proof` so an agent only proposes. This unit lands that command under `instructions.edit`, each
value with its arm, witness and planted red; `flow-only` refused at load until dDeclaredLoop lands (L3);
every write refused until dDeclaredLoop's guard lands (M11); the change record (S12, S13) each write
leaves; the command's checks as a leg over the tree; the manifests' row merge; and instruction packs
extending `charter.practices` into a pack catalogue, apart from the policy presets (C1-F19).

## 2. Scope (IN)

- **S1** — The manifest. The instruction manifests are each kit's `instructions.toml` (unit 9) and the
  repository's overlay `.governance/instructions.toml` (unit 32), listed by `read_manifests(root)` in
  `tools/playbook/instructions_edit.py`, the one list the one-door check and the write path read. Across
  nodes they are row stores: `tools/memory-tree/merge-rows.py` gains a TOML-table class keyed by each
  `[[unit]]` table's `tag`, with the driver's postconditions (no tag lost, none duplicated), and
  `.gitattributes` routes `**/instructions.toml` and `.governance/instructions.toml` to `merge=rows`.
  Observed by AC1.
- **S2** — The command, `python tools/playbook/instructions_edit.py <verb>`: the five write verbs of
  `WRITE_VERBS` (§4 Data model), each taking `--manifest <kit id>|overlay`, and the read verbs `list`,
  `render`, `check` and `propose`. A write validates the would-be tree with S6's checks, writes the row,
  writes its change record (S7) for the same commit, re-renders the targets unit 20's renderer assigns,
  and prints the paths it wrote. `propose` writes nothing and prints the row diff and the command that
  would apply it. Observed by AC2.
- **S3** — `instructions.edit`, each value with its arm, witness and planted red:

  | Value | Arm | Witness | Planted red |
  |---|---|---|---|
  | `owner-command-agents-propose` (default) | a write with `instructions.proof`'s proof writes; one without prints the proposal and writes nothing | the change record's `Proof` field | a non-terminal write call that writes a row |
  | `command-for-all` | any caller's write writes | the change record's `Proof: none — command-for-all` | a write whose would-be tree fails S6, admitted |
  | `flow-only` | the command writes nothing; writes come from the flow's item | the load refusal naming the absent flow component | the value loading while the flow component is absent |

  `flow-only` is refused at load, exit 2, as selecting an absent component, until the layer register
  (unit 16) holds a core row declaring the point `point.instructions.flow`, which dDeclaredLoop's flow
  declares when it lands (L3). Observed by AC3, AC4 and AC5.
- **S4** — Every write refused until dDeclaredLoop's guard lands (M11). Whatever the value, a write verb
  exits 1 naming the guard and the stand-in route while no core row of the layer register declares
  `point.instructions.guard`, the point dDeclaredLoop's guard declares; the refusal prints the row diff as
  `propose` would. dGroundRules' minimal guard (`cl-dClosedLoop-0012`) refuses agent writes to the
  overlay meanwhile. Observed by AC6.
- **S5** — `instructions.proof`. `tty-cli`, the default, is the owner's presence shown as standard error
  being an interactive terminal, the one stream dGroundRules' minimal guard tests for `policy-file.proof`
  (`[ -t 2 ]`, written inline in `.githooks/pre-commit`, TOOL-dGroundRules-6 S4 and its §8 F3). That
  test is shell with no callable, so the command tests `sys.stderr.isatty()` itself, stated as a second
  implementation of the guard's signal (§8 F4, the owner's pick). `signed` and `both` are refused at load as selecting an absent component, the layered
  proof v2 places in `[planned]`, until a core row declares `point.instructions.signed-proof`. Both keys
  are read with `policy_reader("instructions.edit")` and `policy_reader("instructions.proof")`,
  PLAY-dOrderedCharter-9's callable that runs `policy.py get <key>` as a subprocess through the inlined
  `resolve_kit_dir` (`tools/playbook/render_playbook.py:78-79`), since a kit never imports a sibling
  (TOOL-dGroundRules-1 §4): an unset key reads its catalogue default with its reason
  (TOOL-dGroundRules-3 S2), and each call is a shape the reader-coverage arm counts (TOOL-dGroundRules-8,
  the Readers table). An exit 2 from `get` refuses every verb at load, exit 2, naming the key and
  carrying the reader's line. Observed by AC3, AC7 and AC12.
- **S6** — The checks, run before every write and as a leg over the tree,
  `python tools/playbook/instructions_edit.py check`: unit 20's schema and one-fact checks, unit 12's
  grammar, unit 19's tag checks, and two of this unit's own: **conflicts at one level**, two active
  directives at one level whose texts differ only in an opposite modal (`MUST` against `NEVER`); and
  **references**, a pointer unit or an `edges` target naming a `unit.*` tag that resolves to no active unit
  and no change record's successor. The budgets join when unit 11 lands them. Observed by AC8.
- **S7** — The change record (S12, S13), the `change` kind of unit 7's factory
  (`tools/memory-tree/build_records.py`): `<date>-build-<unit id>-change-<n>.md` in the recording build's
  `build/` folder, `**Serves:** change <unit id>`, with the fields `Unit` (the tag), `Action` (one of
  `WRITE_VERBS`), `Before` and `After` (each `<tag>@<hash8>` under S7's normaliser,
  or `none`), `Mark` (`editorial` or `semantic`), `Successor` (a tag, a comma list for a split, or `none`,
  on every action but `add` and `edit`), `Proof` (`tty-cli` or `none — <value>`), `Promoted-from` (optional,
  the source a promotion names, written as the `promoted-from` edge) and `Caused-by`. Unit 20 derives each
  unit's `status` from these; unit 33 grades `Mark`. The factory's `new change` verb is the stand-in door
  a build's builder records a kit manifest change through while the command refuses writes. Observed by
  AC9.
- **S8** — The pack catalogue, `tools/playbook/packs.toml`: one `[[pack]]` row per instruction pack, with
  `name`, `kind` (`methodology`, `governance` or `language`), `practices` (practice tags of S15's
  catalogue, or the one selector `all`) and `description`, read by `read_packs`. `resolve_practices(value)`
  resolves a `charter.practices` value naming packs and practices into practice tags, for unit 1's key
  reader. One row ships, `foundation`, `kind = "governance"`, `practices = "all"`, the governance
  foundation set v2 names as the key's default. The check reds a pack naming a practice the catalogue
  lacks (`unarmed` until unit 1 writes the catalogue) and a pack whose name equals a practice's. The pack
  catalogue is no policy preset: no preset row sets `charter.practices`. Observed by AC10.
- **S9** — The change-record extractor unit 19 hands to this unit: `extract_change_records`, registered
  with the tag index, writes the index row unit 19's retirement check reads for each tag a change record
  ends, its redirect the record's `Successor` (one tag for a rename, none for a split, which redirects to
  no single successor, and none for a removal), so `gov_tag.py check` reads new text citing that tag.
  Observed by AC11.
- **S10** — The leg and plants. One leg `instruction edits (manifest checks)` in `tools/gate-legs.json`
  runs S6 over the tree and S8's check, carrying `"enforces": ["principle.p11", "principle.p13"]`;
  `python tools/playbook/instructions_edit.py fixture --plant <case>` builds a throwaway repository in the
  system temp directory, with its own layer register and a committed `.governance/policy.toml`, since the
  reader reads revisions only (TOOL-dGroundRules-2 S2), and runs the case. Observed by AC1 to AC11.
- **S11** — The two catalogue rows. `instructions.edit` and `instructions.proof` land with dGroundRules as
  `[[key]]` rows of `tools/policy/catalogue.toml`, owner dOrderedCharter (v2:1243-1244), with no
  `summary` or `usage` and their names on the shrink-only `tools/policy/unsummarised-keys.txt`
  (TOOL-dGroundRules-1 S3, S6). This unit adds no row: it fills each row's `summary` and `usage`, a line
  its row admits (`instructions.edit = "command-for-all"`, `instructions.proof = "tty-cli"`), and drains
  both names in the same commit with `python <prefix>/policy/policy.py lists --write`. Observed by AC12.

## 3. Non-goals (OUT)

- The guard itself and the flow's item that writes under `flow-only`: dDeclaredLoop's. This unit names
  the points each declares and refuses until they are declared.
- The layered, signed proof: v2 `[planned]`.
- The overlay's file, home and `repo.` units: unit 32; the overlay's row mechanism over every kind: unit 35.
- The `editorial` and `semantic` mark's admission rules, pins and drift: unit 33.
- Instruction-effectiveness records (R-J) and the Loop Review's pruning: later builds.
- The policy presets and their catalogue: dKeptSession's; packs never enter them.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-9` — `read_units`, the rows every verb reads
- **consumes-from** `PLAY-dOrderedCharter-20` — the schema and one-fact checks, the renderer a write re-renders through, and `derive_status`
- **consumes-from** `PLAY-dOrderedCharter-12` — the grammar check S6 runs
- **consumes-from** `PLAY-dOrderedCharter-7` — the record factory and its stand-in door, which S7's kind joins
- **consumes-from** `PLAY-dOrderedCharter-16` — the layer register whose declared points S3, S4 and S5 read
- **consumes-from** `PLAY-dOrderedCharter-19` — the tag checks S6 runs, and the index whose `retired` rows S9's extractor writes
- **consumes-from** `PLAY-dOrderedCharter-24` — S7's shared normaliser for `Before` and `After`
- **consumes-from** external — dGroundRules, built before this build run: `policy.py get` at the landed revision (TOOL-dGroundRules-2 S1, S7), the two catalogue rows and the shrink-only list S11 fills and drains (TOOL-dGroundRules-1 S3, S6), the mirror's `mirror --write` (TOOL-dGroundRules-5 S2), and the stderr signal its minimal guard's hook tests (TOOL-dGroundRules-6 S4, `cl-dClosedLoop-0012`)
- **hands-off** `PLAY-dOrderedCharter-1` — `resolve_practices`, which the `charter.practices` reader calls
- **hands-off** `PLAY-dOrderedCharter-14` — the command a promotion goes through, and the `Promoted-from` field
- **hands-off** `PLAY-dOrderedCharter-32` — the overlay as the command's `--manifest overlay` target
- **hands-off** `PLAY-dOrderedCharter-33` — the `Mark`, `Successor` and `Proof` fields its checks read
- **hands-off** `PLAY-dOrderedCharter-35` — the command that writes and re-pins an overlay row
- **hands-off** `PLAY-dOrderedCharter-31` — the change record kind its census records are written in
- **consumes-from** `PLAY-dOrderedCharter-28` — the `promoted-from` edge type and the one site it admits, this command's change record
- **hands-off** external — dDeclaredLoop declares `point.instructions.guard` and `point.instructions.flow`, which arm writes and `flow-only`
- **consumes-from** `PLAY-dOrderedCharter-42` — the change kind's token in the bindings reader, without which S7's record reads malformed (finding 31)
- **hands-off** `PLAY-dOrderedCharter-40` — the change records of gov's first four unit rows, written through S7's stand-in door (finding 2)
- **hands-off** `PLAY-dOrderedCharter-45` — S1's table class given its whole conflict envelope and a parse postcondition (finding 79)
- **hands-off** `PLAY-dOrderedCharter-46` — S2's re-render pointed at the overlay the write verb has just written, through the candidate read (finding 80)
- **hands-off** `PLAY-dOrderedCharter-49` — the round-1 spec audit's minors on this spec, findings 5, 14, 67 and 85, which that batch unit corrects after this unit lands, each by the item its report id names
- **consumes-from** `PLAY-dOrderedCharter-50` — the owed-rows probe: this pass runs `python tools/run-gates/owed_rows.py --base HEAD` before its commit and writes every row it names in that commit (round-2 id 23)

## 4. Design

### Data model

```toml
# tools/playbook/packs.toml
[[pack]]
name = "foundation"
kind = "governance"
practices = "all"
description = "The governance foundation set, every catalogue practice until the census narrows it."
```

```
WRITE_VERBS = ("add", "edit", "remove", "rename", "split")

write(verb, row, manifest):
  value  = policy("instructions.edit")      # refused at load if it selects an absent component
  proof  = policy("instructions.proof")     # likewise
  if not declared("point.instructions.guard"):  refuse: guard absent, print the proposal
  if value == "flow-only":                       refuse: writes come from the flow's item
  if value == "owner-command-agents-propose" and not proven(proof):  print the proposal, write nothing
  if check(would_be_tree) is red:                refuse, naming each red
  write row; write change record; re-render; print paths
```

### Inventory

Minted: the module `tools/playbook/instructions_edit.py` with `read_manifests`, `WRITE_VERBS`, the verbs of S2 and the
fixture cases; the points `point.instructions.guard`, `point.instructions.flow` and
`point.instructions.signed-proof`; the record kind `change` and its fields; the file
`tools/playbook/packs.toml` with `read_packs` and `resolve_practices`; `extract_change_records`; merge-rows'
TOML-table class; the leg
`instruction edits (manifest checks)`.

### Migration

None: no manifest exists before unit 9's rows; the `.gitattributes` lines take effect on the next merge.

### Rollout

Live at landing, at order 16, refusing every write until dDeclaredLoop's guard declares its point; `list`,
`render`, `check` and `propose` run from landing. S11 lands as two commits: the first fills the two rows
and drains the list; the second stages only `.governance/policy.json` as `policy.py mirror --write`
regenerates it, because a catalogue edit stales the mirror and the guard admits a mirror commit only
when the policy file and the catalogue equal HEAD (TOOL-dGroundRules-5 S1, TOOL-dGroundRules-19 S1).

### Files touched (estimate)

- `tools/playbook/instructions_edit.py`
- `tools/playbook/packs.toml`
- `tools/playbook/tag_index.py`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/merge-rows.py`
- `.gitattributes`
- `tools/gate-legs.json`
- `tools/policy/catalogue.toml`, the two existing rows filled
- `tools/policy/unsummarised-keys.txt`, drained by `lists --write`
- `.governance/policy.json`, the second commit

### Alternatives rejected

- **The command as a verb of `govkit`.** govkit is the distribution layer, an expansion (scout B), and the
  write path is the instruction layer's.
- **Packs as policy presets.** The presets never touch `charter.practices` (v2's `[presets]`), and C1-F19
  names a pack catalogue apart from them.
- **A command that writes now and lets dDeclaredLoop's guard tighten it later.** M11 refuses every write
  until the guard lands; a write path with no guard is the surface the clause closes.

## 5. Production-readiness checklist

- security: deny by default: every write refused until the guard declares its point, and a refused policy
  read refuses every verb; the proof tests the one stream the minimal guard's hook tests, stderr (§8 F4);
  `tty-cli` proves owner presence against a cooperative agent only, the
  threat the owner accepted (v2 `[witnesses]`, SA-1).
- perf / scale: one read of every manifest per call; the merge class parses two TOML files per conflict.
- error / empty / loading states: a refused write prints the proposal so the change is never lost; an
  absent component exits 2 at load naming it; the pack check reads `unarmed` until the catalogue exists.
- observability: every refusal names the value, the missing point or the failing check, and the remedy.
- risks: a builder who edits a kit manifest by hand without a change record is caught by unit 20's status
  derivation and unit 33's step gate, not by this command.
- testing: S10's plants both ways.
- migration: none.
- user docs: N/A — unit 37 renders the command's reference page from its rows.

## 6. Acceptance criteria

- **AC1** — When `python instructions_edit.py fixture --plant merge` merges two branches
  that each add a `[[unit]]` table to one `instructions.toml`, the merged file holds both tags once, and a
  branch pair adding one tag twice is a conflict the driver names.
  Red when: a tag is lost or duplicated by the merge.
- **AC2** — When `python instructions_edit.py fixture --plant propose` runs, `propose`
  prints the row diff and the command that applies it, and `git status --porcelain` in the fixture prints
  nothing.
  Red when: `propose` writes a file.
- **AC3** — When `python instructions_edit.py fixture --plant owner-propose` runs with the
  guard's point declared, a write from a terminal writes the row and a change record whose `Proof` reads
  `tty-cli`, and the same write with standard error not a terminal prints the proposal and writes nothing.
  Red when: a non-terminal call writes a row.
- **AC4** — When `python instructions_edit.py fixture --plant command-for-all` runs, a
  non-terminal write writes the row and a change record whose `Proof` reads `none — command-for-all`, and a
  write whose would-be tree fails `schema` is refused.
  Red when: a failing write is admitted, or the record's proof is blank.
- **AC5** — When `python instructions_edit.py fixture --plant flow-only` sets
  `instructions.edit` to `flow-only` with no `point.instructions.flow` declared, every verb exits 2 naming
  the absent flow component; with the point declared, a write verb exits 1 naming the flow as the writer.
  Red when: `flow-only` loads while the flow is absent, or the command writes under it.
- **AC6** — When `python tools/playbook/instructions_edit.py add --manifest playbook --tag unit.demo --type
  directive --level 3 --text "MUST demo."` runs on the tree at landing, it exits 1 naming
  `point.instructions.guard` and dDeclaredLoop, prints the proposal, and the manifest is unchanged.
  Red when: any write lands before the guard declares its point.
- **AC7** — When `python instructions_edit.py fixture --plant proof-values` sets
  `instructions.proof` to `signed`, then `both`, each load exits 2 naming the absent signed proof, and
  `tty-cli` loads.
  Red when: an unbuilt proof is accepted.
- **AC8** — When `python instructions_edit.py fixture --plant checks` runs, two level-3
  directives `MUST push after each pass.` and `NEVER push after each pass.` red the conflict arm, and a
  pointer to `unit.gone` with no successor reds the references arm; renaming `unit.gone` with a change
  record naming its successor clears it.
  Red when: a contradiction at one level or a stranded reference passes.
- **AC9** — When `python instructions_edit.py fixture --plant record` runs a rename, the
  change record names `Unit`, `Action: rename`, both pins, `Mark`, `Successor` and `Proof`,
  `build_records.py read` grades it clean, and a record missing `Successor` on a rename is red.
  Red when: a write leaves no record, or a record omits its successor.
- **AC10** — When `python instructions_edit.py fixture --plant packs` runs,
  `resolve_practices(["foundation"])` returns every catalogue practice tag, a pack naming `practice.nosuch`
  reds the check, and with no catalogue the check prints `unarmed`.
  Red when: a pack names an unknown practice, or an absent catalogue reads green.
- **AC11** — When `python instructions_edit.py fixture --plant retired-rows` records a rename
  of `unit.old` to `unit.new` and a split of `unit.both`, `python gov_tag.py show unit.old`
  prints the redirect to `unit.new`, `unit.both` shows no single successor, and new text citing
  `unit.old` reds `gov_tag.py check` under `tags.retired-cites`' default.
  Red when: a retired tag resolves as live, or a split redirects to one successor.
- **AC12** — When `python -c "import tomllib; k = ('instructions.edit', 'instructions.proof'); print([(r['name'], r['owner'], bool(r.get('summary')), bool(r.get('usage'))) for r in tomllib.load(open( 'tools/policy/catalogue.toml' , 'rb'))['key'] if r['name'] in k])"`
  runs after the pass, it prints exactly two tuples, each owned by `dOrderedCharter` with both flags
  `True`; `python "tools/policy/policy.py" lists --check` exits 0; `grep -c -e instructions.edit -e instructions.proof "tools/policy/unsummarised-keys.txt"`
  prints `0`; and `git grep -n -e 'policy_reader("instructions.edit"' -e 'policy_reader("instructions.proof"' -- tools/playbook/instructions_edit.py`
  prints both lines.
  Red when: a key keeps no summary or usage, stays on the list, gains a second row, or is read in a shape
  the reader-coverage arm does not count.
  fixture: the catalogue and the list are dGroundRules', untracked until it builds, so their paths are
  quoted.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/instructions_edit.py · covers AC1 AC2 AC3 AC4 AC5 AC7 AC8 AC9 AC10 AC11 · a leg running every `fixture --plant` case, each failing case staged by its plant · none

New arm: tools/gate-legs.json · covers AC6 · the `instruction edits (manifest checks)` leg over the tree, its failing case a write admitted while the guard's point is undeclared · none

## 8. Open questions

- **F1** — How does the command know dDeclaredLoop's guard and flow have landed, given neither exists and
  no S-interface names them?
  RESOLVED (agent, 2026-10-23, delegated): rung 3, the most feature-rich survivor: a point a core row of
  the layer register declares (S3, S4), read through unit 16's register, which P28 makes the one place a
  component attaches; dDeclaredLoop declares `point.instructions.guard` and `point.instructions.flow` when
  it lands, and a fixture repository declares them in its own register to stage each arm, so no test
  switch ships.
- **F2** — `instructions.proof` allows `signed` and `both`, and v2 places the layered proof in `[planned]`.
  Options: build a signed proof here; refuse both at load as an absent component.
  RESOLVED (agent, 2026-10-23, delegated): rung 1, v2 `[witnesses]` answers it: the owner keeps `tty-cli`
  and the layered proof waits in `[planned]`. Both refused at load (S5), the mechanism L3 gives
  `flow-only`.
- **F3** — With every write refused until the guard lands, how does a build's builder record a kit
  manifest change?
  RESOLVED (agent, 2026-10-23, delegated): rung 1, memory-plan `[doors]` answers it: `instructions.edit`
  writes change records, and a stand-in door serves until the record door adopts it; the S12 factory's
  `new change` verb is that door (S7), and the command uses the same kind once it writes.
- **F4 — How does the command prove `tty-cli`, when the guard's test is inline shell?** dGroundRules'
  minimal guard tests `[ -t 2 ]` inside `.githooks/pre-commit` (TOOL-dGroundRules-6 S4, its §8 F3) and
  lands no callable a Python command can run, so rev-3's "called through that guard's one
  implementation" has nothing to call, and rev-3 named the other stream, standard input. Options:
  (a) this unit's own proof, `sys.stderr.isatty()`, testing stderr as the hook does, stated in S5 and on
  the command's page as the second implementation of one signal; (b) an ask to dGroundRules to move
  the hook's test into a callable in `tools/policy/` that the hook and this command both run; (c) wait
  for dDeclaredLoop's TTY CLI and refuse every write until then. (b) is the one-implementation shape,
  but it moves a landed parent's hook seam for one consumer; (c) leaves `tty-cli` with no
  implementation, so AC3's owner arm has nothing to observe even with the guard's point declared.
  Recommendation (a): one stream, stderr, named once, and the second spelling is one call.
  RESOLVED (owner, 2026-10-25): (a). PLAY-dOrderedCharter-7's `core.exceptions: owner-only-expiring`
  proof is this check.

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the spec run's carrier of `cl-dClosedLoop-0045`.
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-1 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-40, PLAY-dOrderedCharter-42, PLAY-dOrderedCharter-45, PLAY-dOrderedCharter-46, PLAY-dOrderedCharter-49.
- rev-3 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-50.
- rev-4 · 2026-10-24 · §2 S5, S10, S11 (new) · §3 Edges · §4 Rollout, Files touched · §5 security · AC3, AC12 (new) · §8 F4 (new, open for the owner) · §10 · re-grounded on the parents' landed specs by `2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck` row 40, U3 and U4: the proof tests stderr, the guard's stream, and how it is run is F4's; both keys are read through `policy_reader`, and a refused read refuses; the two landed rows are filled and drained, never added.
- rev-5 · 2026-10-25 · Status (ratified) · §2 S5 · §8 F4 · §10 · the owner's answer to F4, item 1 of `2026-10-25-prompt-PLAY-dOrderedCharter-1-owner-forks`: (a), the command's own check that stderr is a terminal, stated directly where S5 and the reuse audit pointed at the open fork.

## 10. Reuse audit

The seams extended are `tools/memory-tree/merge-rows.py`, the row-keyed driver R-I and the research's
pick name for manifest merges (its `key` at line 271 anchors a markdown row; S1 adds a TOML-table class
beside its three), the `.gitattributes` `merge=rows` lines (61-78), unit 7's record factory for the
`change` kind, and the stream dGroundRules' minimal guard tests for the TTY proof. No TTY proof exists
in the tree today (scout A: no `isatty` under `tools`), and the guard's lands as `[ -t 2 ]` inline in
`.githooks/pre-commit` (TOOL-dGroundRules-6 S4), no callable, so this unit writes a second test of the
same stream (§8 F4, the owner's pick).
`python tools/codebase-map/reuse_lookup.py "an owner-only command that adds edits and removes instruction rows
and records each change"` ranked name-token matches (`rows`, `records`, `changed`), none a guarded write
path, so no existing seam fits the command itself.

Recall terms used: `python tools/memory-recall/query.py "how does the owner change an instruction and how is an agent kept to proposing" --terms "instructions.edit instructions.proof tty-cli owner command propose change record manifest guard flow-only pack"`
