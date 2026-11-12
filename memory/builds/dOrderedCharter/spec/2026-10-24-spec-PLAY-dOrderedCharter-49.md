# PLAY-dOrderedCharter-49 — the round-1 spec audit's 73 minors: criteria that can pass, rows a new leg owes, one reader per fact, and seams in build order

**Status:** CLOSED · rev-9 · 2026-11-11 · node d · Tier-2 · base ce13efbe · streams playbook · order 39 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 |
| [2026-10-24-build-PLAY-dOrderedCharter-49-deviation-491.md](../build/2026-10-24-build-PLAY-dOrderedCharter-49-deviation-491.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-49-deviation-492.md](../build/2026-10-24-build-PLAY-dOrderedCharter-49-deviation-492.md) | deviation | — |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 |
| [2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-reground-returns.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-25-build-PLAY-dOrderedCharter-49-deviation-493.md](../build/2026-10-25-build-PLAY-dOrderedCharter-49-deviation-493.md) | deviation | — |
| [2026-11-02-build-PLAY-dOrderedCharter-49-ledger.md](../build/2026-11-02-build-PLAY-dOrderedCharter-49-ledger.md) | journal | — |
| [2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md](../build/2026-11-10-build-PLAY-dOrderedCharter-1-runlog-8d3cc031.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 |
| [2026-11-11-build-PLAY-dOrderedCharter-49-1-builder-return.md](../build/2026-11-11-build-PLAY-dOrderedCharter-49-1-builder-return.md) | journal | — |
| [2026-11-11-build-PLAY-dOrderedCharter-49-deviation-494.md](../build/2026-11-11-build-PLAY-dOrderedCharter-49-deviation-494.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md) | research | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |
| [2026-11-02-prompt-PLAY-dOrderedCharter-49-build-brief.md](../prompts/2026-11-02-prompt-PLAY-dOrderedCharter-49-build-brief.md) | journal | — |
| [2026-11-03-prompt-PLAY-dOrderedCharter-19-divergence-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-19-divergence-brief.md) | research | PLAY-dOrderedCharter-19 |
| [2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md](../prompts/2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md) | research | PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-55 |
| [2026-11-08-prompt-PLAY-dOrderedCharter-39-drift-fold-brief.md](../prompts/2026-11-08-prompt-PLAY-dOrderedCharter-39-drift-fold-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |
| [2026-11-10-prompt-PLAY-dOrderedCharter-49-1-spec-writer.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-49-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-49-2-spec-writer.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-49-2-spec-writer.md) | journal | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-49-ac26-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-49-ac26-brief.md) | research | — |
| [2026-11-10-prompt-PLAY-dOrderedCharter-49-precheck-brief.md](../prompts/2026-11-10-prompt-PLAY-dOrderedCharter-49-precheck-brief.md) | research | — |
| [2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md](../reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit, its record in the table above, confirmed 83 findings; its ten highs are
units 39 to 48, and this unit is BUILD-METHOD M4's batch of every MEDIUM and LOW. Each item names the
part of one of 35 units' specs it supersedes, and that unit's §3 hands the part here.

Each §2 item names one report id and its criterion, in the report's order; MEDIUM M<n>'s is AC<n>, LOW
L<n>'s AC<45+n>, and merged ids share one. Ids 12, 28, 41, 50 and 86 are built from the skeptic's
corrected fix.

At `974700af5` every repaired unit is CLOSED but unit 31, which builds first: a CLOSED unit's
criterion is observed here in its corrected form, never edited into its frozen spec (unit 55 S2).

## 2. Scope (IN)

Met marks an item the built code or a landed spec already holds at `974700af5`; its criterion
observes it at this pass.

- **S1** — id 3, met by unit 37: each `[[reference]]` row names a `reader` mapping its registry's own
  fields onto `summary` and `usage`, as `tools/playbook/render_playbook.py#read_unit_reference_rows`
  maps `text`; no `summary-from` key is minted (section 8 F2). Observed by AC1.
- **S2** — id 4, met: both `KNOWN` sets of `tools/run-gates/run-gates.test.sh` carry `enforces`.
  Observed by AC2.
- **S3** — id 66, met: `tools/govkit/govkit.py#write_gate_legs` builds rows from named keys and writes
  no `enforces`. Observed by AC2.
- **S4** — id 5, met: unit 50's `tools/run-gates/owed_rows.py` finds every new leg's pin row, and its
  ceiling row is the close's measured bar run's to write. Observed by AC3.
- **S5** — id 67, met: the same probe finds each new leg's `[[gate_leg]]` or `[[exempt_leg]]` row and
  dossier claim. Observed by AC3.
- **S6** — id 6, met: rows read `scope` and `trigger`
  (`tools/playbook/instruction_units.py#UNIT_STRINGS`), never `select` or `when`. Observed by AC4.
- **S7** — id 7, met: `edges` is a list in `tools/playbook/instruction_units.py#UNIT_LISTS`. Observed
  by AC4.
- **S8** — id 45, met in unit 31's rev-13: its level-0 rows are `directive` rows. Observed by AC4.
- **S9** — id 8, met: `tools/playbook/edge_grammar.py#read_unit_edges` reads through
  `parse_unit_rows`. Observed by AC5.
- **S10** — id 9, met: `tools/playbook/overlay.py#read_excluded_tags` and
  `tools/playbook/overlay.py#check_fixed_sources` are unit 32's late reads. Observed by AC6.
- **S11** — id 10: `tools/playbook/practice_census.py` moves no unit (PINNED at `974700af5`), as
  unit 31 rev-13's S6 states, so no census step or program is minted (section 8 F3); a census moving
  a unit at the pass is a hand-back. Observed by AC7.
- **S12** — id 11, met: the `kit` row sits at `layer.distribution`, an expansion layer, which
  `tools/playbook/tag_index.py#check_owned` never grades. Observed by AC8.
- **S13** — id 12, met: no `role` or `item` namespace is registered, gov's unit rows carry no `scope`,
  and the schema check reds an unregistered one. Observed by AC9.
- **S14** — id 13, met by unit 22: `tools/playbook/namespaces.toml`'s header states the
  purpose-source grammar, `#h1` the `doc` row's. Observed by AC10.
- **S15** — id 14. `tools/playbook/packs.toml`'s `foundation` pack reads `practices = "foundation"`,
  which `tools/playbook/instructions_edit.py#resolve_practices` resolves to the catalogue's
  `foundation` array and `tools/playbook/instructions_edit.py#check_packs` admits; at `974700af5` the
  array holds 35 of 39 rows (PINNED). Observed by AC11.
- **S16** — id 16. Unit 18 AC1 is observed here scoped `-- tools/memory-recall tools/memory-tree`.
  Observed by AC12.
- **S17** — id 34. The namesakes `tools/codebase-map/map_lib.py#repo_root`,
  `tools/drift-audit/drift_report.py#repo_root` and `tools/govkit/govkit.py#repo_root` stay. Observed
  by AC12.
- **S18** — id 70. Within that scope every hit is in `tools/memory-tree/id_grammar.py`. Observed by
  AC12.
- **S19** — id 17. Unit 18 AC3 is observed here as "every hit is a keep row or a trailer-named
  history comment": `tools/codebase-map/scen-adversarial.json@974700af5:180` and
  `tools/govkit/selftest.py@974700af5:12089`. Observed by AC13.
- **S20** — id 33, met: unit 18 AC7's grep prints nothing, comments included, so no `ast` walk is
  owed. Observed by AC13.
- **S21** — id 18. Unit 1 AC1 is observed here against the one-line region of the charter's
  `## Practices`, never every `RULE_LINE_RE` match: 35 tags each, in order (PINNED at `974700af5`).
  Observed by AC14.
- **S22** — id 19. Unit 5 AC3 is observed here counting `- [verify] ` inside `### Charter rules`
  only. Observed by AC15.
- **S23** — id 20, met in unit 30's rev-6. Observed by AC16.
- **S24** — id 21. The report's pathspecs are observed here rooted: `tools/playbook/fixtures/row_kind.py`
  (unit 36 AC11), `help/overlay-rows.md` (unit 36 AC12; unit 35 AC14, with `help/README.md`),
  `help/charter.md` (units 1, 2 and 6, AC7), `help/upgrade-steps.md` (unit 31 AC12),
  `help/composition.md` (unit 34 AC11). Unit 35 AC14's rooted grep finds both lines at `974700af5`.
  Observed by AC17.
- **S25** — id 22, met in unit 3's spec. Observed by AC18.
- **S26** — id 32. `tools/playbook/edge_grammar.py#read_trailer_edges` reads a `serves` value as edges
  only when `tools/playbook/edge_grammar.py#derive_target_fault` passes every target; prose or `none`
  is counted unread, never an edge or a refusal, and `--check` prints the count. Observed by AC19.
- **S27** — id 35, met: `tools/memory-recall/recall_conf.py` and `tools/memory-recall/bench.py` reach
  `id_grammar` through the `resolve_kit_dir` block. Observed by AC20.
- **S28** — id 36. `tools/memory-recall/query.py` writes `KIT_MEMORY_RECALL_VERSION` into its cache
  manifest, and `tools/memory-recall/query.py#ensure_cache` yields a clause comparing it. Observed by
  AC21.
- **S29** — id 37. Unit 18 AC5 is observed here with one limb more: with no `.memory-tree.conf`,
  importing `id_grammar`, `corpus_ids` and `gotchas` exits 0. Observed by AC22.
- **S30** — id 38, met in unit 3's spec. Observed by AC23.
- **S31** — id 65, met at unit 3's pass, its leg line naming `unattended skill size`. Observed by AC23.
- **S32** — id 39, met: `tools/playbook/instruction_units.py#check_lock` hashes with
  `git hash-object -- <path>`, whose clean filter folds a CRLF checkout to its LF blob (probed at
  `974700af5`). Observed by AC24.
- **S33** — id 83. `.gitattributes` routes `.governance/instructions.lock` to `merge=ours`; the
  lander's `regen.py --write` re-renders it through the playbook `[[regenerate]]` row (section 8 F5).
  Observed by AC24.
- **S34** — id 40. `tools/playbook/core.py#read_front_matter` is the one `description` reader, which
  `tools/playbook/load_sets.py` reads through, its `tools/playbook/load_sets.py#extract_description`
  deleted. `kind.skill`'s `population` in `tools/playbook/kinds.toml` becomes `*skills/*/SKILL.md`,
  read through `git ls-files` by `tools/playbook/core.py#run_skills` and by the measure's Skill list
  (section 8 F10); it grades `.claude/skills/memory-recall/SKILL.md`, 1275 characters against 1024
  (PINNED at `974700af5`), so `tools/memory-recall/SKILL.template.md` is cut under the cap and
  re-rendered. Observed by AC25. **Readers:** by name: `tools/playbook/load_sets.py` · by value:
  NO VALUE READERS — the measure reads the same text through the kept reader.
- **S35** — id 41, met by unit 27: `tools/roles/handoff.py#render_handoff` carries `input:code`.
  Observed by AC26.
- **S36** — id 42, met: `tools/playbook/instruction_units.py#read_unit_rows` lists manifests under
  `root`. Observed by AC27.
- **S37** — id 43, met: `tools/playbook/check_layers.py#derive_edges` counts no edge for a module beside
  the importer or in a core home. Observed by AC28.
- **S39** — id 46, met: `tools/govkit/docs_leg.py#run_page_commands` spawns through `resolve_bash`.
  Observed by AC30.
- **S40** — id 51. `tools/playbook/edges.toml` registers `consumes-from` and `hands-off`, declared
  types from `family-id` to `family-id` sited in a spec's `### Edges` block, with inverses
  `consumed-by` and `receives-from` (section 8 F11); the hygiene gate and
  `tools/check-spec-tokens.py#scan_handoffs` keep parsing the block. Observed by AC31.
- **S41** — id 52, met by unit 25: no edge-checks module exists (section 8 F6). Observed by AC32.
- **S42** — id 53, met: `tools/playbook/instruction_units.py#read_practice_catalogue` grades no line
  length. Observed by AC33.
- **S43** — id 54. `tools/playbook/writing_practice.py#check_one_owner` reads its owner set through
  `tools/playbook/tag_index.py#read_chain_registry`, never `memory/builds/` (section 8 F7). Observed
  by AC34.
- **S44** — id 55, met: `one-subject` slugs with `tools/playbook/tag_index.py#derive_heading_seg`.
  Observed by AC35.
- **S45** — id 59, met: `tools/playbook/overlay.py#check_fixed_sources` is the one `fixed-by`
  resolver, which `tools/playbook/overlay_rows.py` imports (section 8 F8). Observed by AC36.
- **S46** — id 60, met: `tools/playbook/overlay_rows.py#derive_row_composition` walks pins through
  `tools/playbook/pins.py#derive_pin_state`. Observed by AC37.
- **S47** — id 68, met: `tools/memory-tree/id_grammar.py#git` names its encoding. Observed by AC38.
- **S48** — id 69. `WIRE-INTO-PROJECT.md`'s memory-recall step says the grammar ships in
  memory-tree's `id_grammar.py`, not that the kits must be SIBLINGS; the other two docs already do.
  Observed by AC39.
- **S49** — id 71, met in unit 31's rev-13, whose S1 Readers name the three registries; a row naming
  `tools/agent-instructions/` after its pass is a hand-back. Observed by AC40.
- **S50** — id 77, met: `tools/playbook/tag_index.py#build_overlay` swaps a worktree's dirty rows on
  every call, and `tools/playbook/tag_index.py#remove_unheld_rows` clears a gone worktree's. Observed
  by AC41.
- **S51** — id 78, met for fences: `tools/playbook/tag_index.py#extract_doc` reads through the one
  fence reader; its docstring states the limits section 8 F12 and F13 keep. Observed by AC42.
- **S52** — id 84. `tools/govkit/docs_leg.py#run_page_commands` runs a block's commands as one script,
  and a runnable block holding a `<word>` placeholder is a `RUN` finding; `help/docs-leg.md` says
  both. Observed by AC43.
- **S53** — id 85. `tools/memory-tree/build_records.py#write_record` refuses a value holding CR or LF
  or opening `**<Word>:**`, before any write, in place of each door's own check, and
  `tools/memory-tree/build_records.py#write_override` refuses a `--rule` the practice catalogue lacks.
  Observed by AC44.
- **S54** — id 86. `skills/session-kickoff/manifest-check.sh#write_card_file` writes
  `card-owner — <session id>` as the card file's second line and skips a card another session owns,
  printing `card-file — skipped: another live session <sid> owns this tree`. Observed by AC45.
- **S55** — id 15, met: `tags (the resolver's checks)` enforces `practice.writing.address`. Observed
  by AC46.
- **S56** — id 23, met: `tools/playbook/edge_grammar.py#check_edges` reds a declared `cites`.
  Observed by AC47.
- **S57** — id 24. `one-owner` reads no layer set: no registry header admits a layer owner at
  `974700af5`. Observed by AC48.
- **S58** — id 25, met: the selects join skips `tools/playbook/tag_index.py#UNIT_EXTRACTORS`, `repo`'s
  among them, so it grades two selector namespaces. Observed by AC49.
- **S59** — id 26, met in unit 23's rev-5, whose table holds the Landing paragraph; its `/build` line
  still reads in `coding-governance-agents.template.md` at `974700af5`. Observed by AC50.
- **S60** — id 27, met: `tools/playbook/instruction_units.py#STATEMENT_TYPES` has one definition;
  unit 12 AC1 is observed here by it. Observed by AC51.
- **S61** — id 28, met at unit 26's pass (unit 55 S2). Observed by AC52.
- **S62** — id 29. `govkit update` prints a gov unit's `stale` or `orphaned` line once: the relay omits
  a line of `tools/govkit/govkit.py#derive_composition_lines` naming a tag
  `tools/govkit/govkit.py#read_unit_drift`'s report printed. Observed by AC53.
- **S63** — id 47. A charter-section citation stating where a rule lives names its tag or heading, a
  history comment kept and named in the `Decided:` trailer: `WIRE-INTO-PROJECT.md@974700af5:728`,
  `tools/unattended/unattended.sh@974700af5:794` and `tools/unattended/unattended.sh@974700af5:8625`.
  Observed by AC54.
- **S64** — id 50. `tools/playbook/instruction_units.py#check_renderers` reds a playbook
  `[[regenerate]]` `writes` path in `INSTRUCTION_PATHSPECS` that no `playbook:` row of
  `tools/playbook/renderers.toml` claims. Observed by AC55.
- **S65** — id 57, met: the envelope gate reads
  `tools/playbook/instruction_units.py#derive_instruction_files`. Observed by AC56.
- **S66** — id 61, met: `tools/playbook/core.py` reaches `coverage_join` through `resolve_kit_dir`.
  Observed by AC57.
- **S67** — id 63, met: `tools/playbook/check_layers.py#read_descriptors` reads tracked files
  (section 8 F9). Observed by AC58.
- **S68** — id 64. The `auto_memory` block calls `tools/lib/common_dir.py#common_git_dir`, never its
  own `rev-parse`, in `tools/lib/auto_memory.py` and its copies in `tools/drift-audit/drift_report.py`
  and `tools/playbook/memory_index.py`, each beside that block. Observed by AC59.
- **S69** — id 72, met by S20. Observed by AC60.
- **S70** — id 73, met in unit 18's spec. Observed by AC61.
- **S71** — id 74. Unit 12 AC5 is observed here with its marker derived by
  `sed -n 's/.*governance-template: \(v[0-9.]*\).*/\1/p' coding-governance-agents.template.md`.
  Observed by AC62.
- **S72** — id 75, met: `tools/playbook/render_playbook.py#TEMPLATE_MAJOR` is 5 beside the template's
  v5.0. Observed by AC63.
- **S73** — id 87. `skills/session-kickoff/manifest-check.sh#derive_map_block` passes
  `--root "$CARD_TREE"`. Observed by AC64.

## 3. Non-goals (OUT)

- Any high of the same audit: units 39 to 48.
- Re-ordering any unit: it is order 39, after every unit whose code an item edits; units 54 and 55
  follow it.
- Changing a repaired unit's clause or carries line, or the text of a CLOSED unit's spec.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-1` — S21, S42
- **consumes-from** `PLAY-dOrderedCharter-2` — S53, S63, S72
- **consumes-from** `PLAY-dOrderedCharter-3` — S25, S30, S31, S65
- **consumes-from** `PLAY-dOrderedCharter-4` — S73
- **consumes-from** `PLAY-dOrderedCharter-5` — S22
- **consumes-from** `PLAY-dOrderedCharter-6` — S24
- **consumes-from** `PLAY-dOrderedCharter-7` — S2, S3, S34, S53, S66
- **consumes-from** `PLAY-dOrderedCharter-8` — S54
- **consumes-from** `PLAY-dOrderedCharter-9` — S13, S36
- **consumes-from** `PLAY-dOrderedCharter-10` — S58
- **consumes-from** `PLAY-dOrderedCharter-11` — S13, S34
- **consumes-from** `PLAY-dOrderedCharter-12` — S32, S33, S60, S71
- **consumes-from** `PLAY-dOrderedCharter-13` — S4, S5
- **consumes-from** `PLAY-dOrderedCharter-14` — S68
- **consumes-from** `PLAY-dOrderedCharter-15` — S15, S53
- **consumes-from** `PLAY-dOrderedCharter-16` — S37, S67
- **consumes-from** `PLAY-dOrderedCharter-18` — S16 to S20, S27 to S29, S47, S48, S69, S70
- **consumes-from** `PLAY-dOrderedCharter-19` — S12, S44, S50, S51
- **consumes-from** `PLAY-dOrderedCharter-20` — S13, S64
- **consumes-from** `PLAY-dOrderedCharter-22` — S14, S43
- **consumes-from** `PLAY-dOrderedCharter-23` — S59
- **consumes-from** `PLAY-dOrderedCharter-24` — S40, S41
- **consumes-from** `PLAY-dOrderedCharter-25` — S41, S56
- **consumes-from** `PLAY-dOrderedCharter-26` — S61, S45
- **consumes-from** `PLAY-dOrderedCharter-27` — S35
- **consumes-from** `PLAY-dOrderedCharter-28` — S6, S9, S26, S41
- **consumes-from** `PLAY-dOrderedCharter-29` — S43, S44, S55, S57
- **consumes-from** `PLAY-dOrderedCharter-30` — S23
- **consumes-from** `PLAY-dOrderedCharter-31` — S49, S11, S8
- **consumes-from** `PLAY-dOrderedCharter-32` — S6 to S8, S10
- **consumes-from** `PLAY-dOrderedCharter-33` — S46, S62
- **consumes-from** `PLAY-dOrderedCharter-34` — S11, S62
- **consumes-from** `PLAY-dOrderedCharter-35` — S7, S46
- **consumes-from** `PLAY-dOrderedCharter-36` — S45, S24
- **consumes-from** `PLAY-dOrderedCharter-37` — S1, S39, S52
- **consumes-from** `PLAY-dOrderedCharter-50` — S2 to S5, S30, S31, S49 (round-2 id 23)
- **hands-off** `PLAY-dOrderedCharter-54` — S54's owner liveness and takeover (round-2 id 39)
- **hands-off** `PLAY-dOrderedCharter-55` — round-2 ids 2, 6, 8, 16, 24, 40 and 41, that unit's S2, S7, S9, S14, S20, S21 and S27; its S9 finds no census step, since S11 mints none while the census moves no unit

## 4. Design

### Evidence

Re-read at `974700af5`: each citation, the owed-rows probe, the census, each Skill's description,
`git hash-object` under `core.autocrlf=true`, and the `--legs-for` query over Files touched.

### Inventory

Minted: S33's attribute line, S15's `foundation` value, S40's two types and inverses, S28's manifest
key, S54's owner line, and the plants the New arm lines name; no Python name. Naming cells:
`lexicon naming predicates`.

### Files touched (estimate)

- `tools/playbook/packs.toml`, `tools/playbook/instructions_edit.py` (S15)
- `tools/playbook/edge_grammar.py`, `tools/playbook/edges.toml`, `help/tags.md` (S26, S40)
- `tools/memory-recall/query.py` (S28)
- `.gitattributes` (S33)
- `tools/playbook/core.py`, `tools/playbook/load_sets.py`, `tools/playbook/kinds.toml`, `tools/memory-recall/SKILL.template.md`, `.claude/skills/memory-recall/SKILL.md` (S34)
- `tools/playbook/writing_practice.py` (S43, S57)
- `WIRE-INTO-PROJECT.md` (S48, S63), `tools/unattended/unattended.sh` (S63)
- `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`, `tools/playbook/adopt-playbook.sh` (S51, AC41)
- `tools/govkit/docs_leg.py`, `help/docs-leg.md` (S52)
- `tools/memory-tree/build_records.py` (S53)
- `skills/session-kickoff/manifest-check.sh`, `skills/session-kickoff/manifest-check.test.sh` (S54, S73)
- `tools/govkit/govkit.py`, `tools/govkit/fixtures/stale_edges.py` (S62)
- `tools/playbook/instruction_units.py` (S64)
- `tools/lib/auto_memory.py`, `tools/drift-audit/drift_report.py`, `tools/playbook/memory_index.py` (S68)

### Rollout

Live at landing, alone, at order 39, after units 31 and 78 (orders 36 and 37), whose edits to the
shared files are this pass's base.

### Alternatives rejected

- **Folding each minor into its unit's spec.** The disposition rule batches every minor (BUILD-METHOD M4).
- **Two batches.** No split has disjoint write sets; nearly every item touches `tools/playbook/`.

## 5. Production-readiness checklist

- security: S53 holds record values to one line at the write boundary; nothing widens.
- perf / scale: S28 adds a manifest key; S34 one `git ls-files` per Skill gate run.
- error / empty / loading states: each item keeps its unit's refusals.
- observability: S26 prints unread trailer values by count; S54 its skip line.
- risks: S34's widened gate reds a live Skill, which this pass fixes.
- testing: AC1 to AC64, probes or plants.
- migration: S33's attribute takes effect on the next merge.
- user docs: `help/docs-leg.md` (S52), `help/tags.md` (S26, S40), `WIRE-INTO-PROJECT.md` (S48).

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --reference --check` runs, it exits 0.
  Red when: a registry with no `summary` field refuses a correct build.
- **AC2** — When `git grep -n "^KNOWN = .*enforces" -- tools/run-gates/run-gates.test.sh` runs, it
  prints two lines, and `git grep -n -F 'row["enforces"]' -- tools/govkit/govkit.py` prints nothing.
  Red when: a key set lacks `enforces`, or the leg writer copies it to a target.
- **AC3** — When `python tools/run-gates/owed_rows.py --base ce13efbe` runs, it prints no `owed —` line.
  Red when: a new leg misses a row it owes.
  figure: DERIVED, the population read at the pass.
- **AC4** — When `git grep -n -E "^(select|when) =" -- tools/playbook/` runs, it prints nothing.
  Red when: a row field is spelled `select` or `when`.
- **AC5** — When `git grep -n "parse_unit_rows" -- tools/playbook/edge_grammar.py` runs, the unit
  adapter's import prints.
  Red when: a second parser of the manifest exists.
- **AC6** — When `python tools/playbook/overlay.py --fixture --plant exclude` runs, it passes.
  Red when: a late read is unwired.
- **AC7** — When `python tools/playbook/practice_census.py` runs at the pass, its summary reads
  `moves 0 · moves, row kept 0`.
  Red when: the census moves a unit and the pass writes it nowhere.
- **AC8** — When `git grep -n -A3 '^ns = "kit"' -- tools/playbook/namespaces.toml` runs, it prints
  `layer.distribution`, an `expansion` row of `tools/playbook/layers.toml`.
  Red when: an optional kit's `kit.<id>` reds `owned`.
- **AC9** — When `python tools/playbook/instruction_units.py schema` runs over gov's tree, it exits 0.
  Red when: a gov-tree row relies on an unregistered namespace.
- **AC10** — When `python tools/playbook/gov_tag.py --fixture --plant bad-purpose-source` runs, it
  exits 1 naming the `doc` row.
  Red when: a declared purpose source fails the grammar.
- **AC11** — When `python tools/playbook/instructions_edit.py fixture --plant packs` runs, the
  `foundation` pack resolves to the fixture's narrower `foundation` array.
  Red when: the pack and the array differ.
- **AC12** — When `git grep -n -E "def (repo_root|grammar_for|anchor_at)" -- tools/memory-recall tools/memory-tree`
  runs, every hit is in `tools/memory-tree/id_grammar.py`, and the three namesakes still define it.
  Red when: a namesake is moved, or a moved name keeps a second definition.
- **AC13** — When unit 18's second query runs at the pass, every hit is a keep row or a comment a
  `Decided:` trailer names.
  Red when: a criterion demands empty output from a population the rule keeps.
- **AC14** — When `python tools/playbook/instruction_units.py practices --list` runs, its `foundation`
  tags equal the `## Practices` one-line region's of `AGENTS.md`, in order.
  Red when: the comparison reads the micro-format tags.
  figure: DERIVED by the probe at the pass.
- **AC15** — When unit 5's AC3 counts `- [verify] Verify before claiming done` inside
  `### Charter rules` only, it reads 1.
  Red when: the practices-at-step line is counted.
- **AC16** — When unit 30's AC6 grep runs at the pass, it prints the one line of
  `tools/playbook/practices.toml` it names.
  Red when: the grep hits prose or matches nothing for want of a path.
- **AC17** — When `git grep -n -e "instructions.stale" -- help/overlay-rows.md help/README.md` runs,
  it finds the section and the index line, and `git ls-files` lists S24's other paths.
  Red when: a criterion's pathspec matches no file.
- **AC18** — When `python tools/playbook/instruction_units.py envelopes --check` runs, it exits 0.
  Red when: a population member's source is outside unit 3's write set.
- **AC19** — When `python tools/playbook/edge_grammar.py --check --base ce13efbe` runs, it exits 0 and
  prints the count of unread trailer values.
  Red when: a prose `Pass:` value reds or is read as an edge.
- **AC20** — When `git grep -n "resolve_kit_dir — canonical copy" -- tools/memory-recall/recall_conf.py tools/memory-recall/bench.py`
  runs, each file carries the block.
  Red when: a re-exporter reaches the grammar through the extractor.
- **AC21** — When a probe bumps only `KIT_MEMORY_RECALL_VERSION` in a scratch copy, `ensure_cache`
  rebuilds naming that cause.
  Red when: a warm cache is served after a recall-only bump.
- **AC22** — When S29's imports run in a scratch tree with no `.memory-tree.conf`, they exit 0, and
  fail with a module-level `resolve()` planted.
  Red when: the no-conf import is unobserved.
- **AC23** — When `git grep -n "unattended skill size" -- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md`
  runs, unit 3's leg line prints.
  Red when: a crossed file's cap leg is off that line.
- **AC24** — When a `core.autocrlf=true` scratch repository checks an LF lock target out CRLF,
  `check_lock` stays green, and `git check-attr merge -- .governance/instructions.lock` prints `ours`.
  Red when: line endings red a clean tree, or a merged lock is kept unrendered.
- **AC25** — When `python tools/playbook/core.py fixture --plant skill` runs, a `.claude/skills/`
  member whose folded description runs past the cap reds.
  Red when: a folded description reads short, or a rendered Skill is ungraded.
- **AC26** — When `python tools/roles/handoff.py render --role gov-builder --build dOrderedCharter --unit PLAY-dOrderedCharter-49 --input spec=$(git ls-files memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md ) --input prompt=$(git ls-files memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-49-precheck-brief.md ) --input code=AGENTS.md --stdout`
  runs from the repository root, it exits 0 and its output carries `### input:code`; the same command
  without `--input code=AGENTS.md` prints the `Not supplied, optional` line naming `input:code`.
  Red when: the code input is dropped silently.
- **AC27** — When `read_units` runs from gov's checkout on a fixture root, it returns only the
  fixture's rows.
  Red when: gov's manifests are read instead.
- **AC28** — When `python tools/playbook/check_layers.py` runs, it reports no edge for the measure's
  `census` import.
  Red when: a namesake becomes a non-core edge.
- **AC30** — When `git grep -n "resolve_bash()" -- tools/govkit/docs_leg.py` runs, the spawn names it.
  Red when: a bare `bash` is spawned.
- **AC31** — When `python tools/playbook/edge_grammar.py --list` runs, `consumes-from` and `hands-off`
  print with their inverses.
  Red when: the vocabulary stays outside the closed set.
- **AC32** — When `git ls-files -- '*edge_checks.py'` runs, it prints nothing.
  Red when: two checkers of one predicate exist.
- **AC33** — When `read_practice_catalogue` reads a planted row whose line runs past the one-line
  cap, it accepts it.
  Red when: the reader and the gate disagree on size.
- **AC34** — When `python tools/playbook/writing_practice.py --fixture --plant owner-faults` runs, a
  row naming a build folder no registry row holds reds.
  Red when: `one-owner` and unit 22 give two verdicts.
- **AC35** — When `one-subject` slugs `M5 — Recall and reuse`, it yields `m5-recall-and-reuse`.
  Red when: GitHub's slug is used.
- **AC36** — When `git grep -n -e "def resolve_fixed_by" -e "def check_fixed_sources" -- tools/playbook/`
  runs, it prints one line.
  Red when: a second resolver exists.
- **AC37** — When `git grep -n "derive_pin_state" -- tools/playbook/overlay_rows.py` runs, it prints
  the composer's call.
  Red when: the walk is restated.
- **AC38** — When `git grep -n "extract.py" -- memory/project/encoding-posture-sites.txt` runs, it
  prints nothing.
  Red when: the moved `git()` names no encoding.
- **AC39** — When `git grep -n -e "requires that kit" -e "SIBLINGS" -- WIRE-INTO-PROJECT.md tools/memory-tree/README.md`
  runs after the pass, it prints nothing.
  Red when: a doc still says memory-tree needs memory-recall.
- **AC40** — When `git grep -n "tools/agent-instructions/" -- memory/project/spawn-idiom-sites.txt memory/project/unarmed-branches.txt memory/project/testsuite-count-waivers.txt`
  runs after unit 31's pass, it prints nothing.
  Red when: a registry row outlives its directory.
- **AC41** — When `python tools/playbook/gov_tag.py --fixture --plant dirty-revert` and
  `--plant worktree-recreate` run, each passes.
  Red when: a dirty row outlives its edit, or a re-created worktree inherits one.
- **AC42** — When `python tools/playbook/gov_tag.py show doc.template-spec#1-goal` runs, it serves no
  row.
  Red when: a fenced heading mints a row.
- **AC43** — When `python tools/govkit/docs_leg.py --fixture --plant run-placeholder` and
  `--plant run-one-script` run, each passes.
  Red when: a placeholder runs, or a block's lines run apart.
- **AC44** — When `python tools/memory-tree/build_records.py new exception --build dOrderedCharter --unit PLAY-dOrderedCharter-49 --principle principle.p1 --excuses x --reason $'a\nExpires: 2099-01-01'`
  runs, it exits 1 and writes no file.
  Red when: a newline forges a field.
- **AC45** — When `write_card_file` runs for two session ids in one scratch tree, the first's card
  survives and S54's skip line prints.
  Red when: a second session overwrites the first's card.
- **AC46** — When `git grep -n "practice.writing.address" -- tools/gate-legs.json` runs, it prints the
  resolver leg's `enforces` line.
  Red when: the rule names a leg no unit mints.
- **AC47** — When `python tools/playbook/edge_grammar.py --fixture --plant declared-cites` runs, it
  reds.
  Red when: unit 25's arm and `check_edges` disagree on `cites`.
- **AC48** — When `python tools/playbook/writing_practice.py check one-owner` runs, it exits 0.
  Red when: `memory/builds/` or a layer is read as an owner.
- **AC49** — When `git grep -n "^UNIT_EXTRACTORS" -- tools/playbook/tag_index.py` runs, it names
  `extract_repo`.
  Red when: the prose count and the join disagree.
- **AC50** — When unit 23's AC4 grep, for `explicit ask or the unattended protocol` and `[land]`,
  runs at the pass, every hit is a row of its table.
  Red when: a Landing line is unlisted.
- **AC51** — When `git grep -n "STATEMENT_TYPES *=" -- tools` runs, it prints one line.
  Red when: a fixture literal counts as a definition.
- **AC52** — When `python tools/playbook/positional.py check` runs at the pass, it exits 0.
  Red when: the list and the tree's citations differ.
- **AC53** — When `python tools/govkit/fixtures/stale_edges.py --plant order` runs, it passes with the
  `stale` line printed once.
  Red when: two sources print it.
- **AC54** — When `git grep -n -i -E "charter'?s? section [0-9]|section 1 rule" -- WIRE-INTO-PROJECT.md tools/unattended/unattended.sh`
  runs after the pass, every hit is named in the trailer.
  Red when: a charter-section citation is missed.
- **AC55** — When `python tools/playbook/instruction_units.py fixture --plant regenerate-unclaimed`
  runs, it passes.
  Red when: an instruction file's writer is declared twice with no join.
- **AC56** — When `git grep -n "derive_instruction_files(" -- tools/playbook/instruction_units.py`
  runs, the envelope check is a caller.
  Red when: two populations of instruction files exist.
- **AC57** — When `git grep -n "def compute_coverage" -- tools/playbook/core.py` runs, it prints nothing.
  Red when: an ungated third copy exists.
- **AC58** — When `git grep -n "ls-files" -- tools/playbook/check_layers.py` runs, the read prints.
  Red when: a reader of untracked descriptors is minted.
- **AC59** — When `git grep -n -e "--path-format=absolute" -- tools/lib/auto_memory.py tools/playbook/memory_index.py`
  runs, it prints nothing.
  Red when: a second common-dir derivation exists.
- **AC60** — When S20's grep, `git grep -nE "recall_conf|KIT_MEMORY_RECALL_VERSION" -- tools/memory-tree/`,
  runs, it prints nothing.
  Red when: a history comment reds the criterion.
- **AC61** — When `git grep -n "check-verdict-epoch.test" -- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-18.md`
  runs, it prints the suite.
  Red when: a new arm's suite is outside the write set.
- **AC62** — When unit 12's AC5 derives its marker with S71's `sed`, it matches the lock's `template`.
  Red when: a literal version pins the criterion.
- **AC63** — When `sed -n 's/^TEMPLATE_MAJOR = \([0-9]*\).*/\1/p' tools/playbook/render_playbook.py`
  runs, it prints the template marker's major.
  Red when: the marker moves alone.
- **AC64** — When unit 4's replay runs with a payload `cwd` in a fixture worktree holding its own
  registry row, the map names that row.
  Red when: the replay reads the hook's working directory.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `run-gates canary` · `codebase-map coverage + freshness` · `memory hygiene` · `encoding posture (text IO names its encoding)` · `python resolver (behaviour + inline parity + idiom ban)` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)` · `kit/dogfood doc parity` · `manifest-check self-test` · `scratch-guard self-test` · `check-wiring self-test` · `drift-audit selftest` · `spec tokens (a spec's own names resolve)` · `policy fixtures` · `tags (the resolver's checks)` · `edges (every declared edge parses, is registered and resolves)` · `one-owner` · `writing practice (records and units)` · `instruction units (schema, one fact)` · `instruction render (one renderer of record)` · `instruction edits (manifest checks)` · `core skills conformance` · `docs` · `help page commands`

New arm: tools/playbook/adopt-playbook.sh · covers AC41 · plants `dirty-revert` and `worktree-recreate` · none
New arm: tools/playbook/instructions_edit.py · covers AC11 · the `packs` plant's narrower `foundation` array · none
New arm: tools/playbook/core.py · covers AC25 · the `skill` plant's rendered member over the cap · none
New arm: tools/playbook/edge_grammar.py · covers AC19 · a plant commit whose `Pass:` is prose · none
New arm: tools/govkit/docs_leg.py · covers AC43 · the `run-placeholder` and `run-one-script` plants · none
New arm: tools/govkit/fixtures/stale_edges.py · covers AC53 · the `order` plant's one `stale` line · none
New arm: tools/playbook/instruction_units.py · covers AC55 · the `regenerate-unclaimed` plant · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC45 · two session ids, one card file · none
New arm: tools/playbook/writing_practice.py · covers AC34 · the `owner-faults` plant · none

## 8. Open questions

- **F1 — Which binding line does a promoted unit carry?** Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) none; (c) parts of 35 units' clauses. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — How a reference page reads `summary` and `usage` (id 3).** Options: (a) a per-registry field
  map in `references.toml`; (b) the fields in four owners' schemas; (c) the `reader` adapter unit 37
  built per registry. (a) would be a second map beside (c). RESOLVED (agent, 2026-11-10, delegated): (c), rung 2, re-resolved from (a). widens: none · relaxes: none
- **F3 — Which door writes the census units into gov's overlay (id 10).** Options: (a) a verb of
  unit 31's step; (b) unit 15's command; (c) an agent's edit; (d) its own step; (e) none while the
  census moves no unit. At `974700af5` (d) is a program with nothing to write. RESOLVED (agent, 2026-11-10, delegated): (e), rung 1, re-resolved from (d). widens: none · relaxes: none
- **F4 — Do `role` and `item` register now (id 12).** Options: (a) no, as unit 10 S5 rules; (b)
  register `role`. RESOLVED (agent, 2026-10-24, delegated): (a), rung 1. widens: none · relaxes: none
- **F5 — How the whole-file lock merges (id 83).** Options: (a) `merge=ours` plus the re-render; (b) a
  regenerating driver, which `merge-rows.py` withdraws. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F6 — Who owns the two edge arms (id 52).** Options: (a) unit 28's leg; (b) unit 25's module, the
  duplicate. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F7 — Which owner set `one-owner` reads (id 54).** Options: (a) unit 22's registry; (b)
  `memory/builds/` plus layers, a second answer. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F8 — Where the `fixed-by` resolver lives (id 59).** Options: (a) a new `resolve_fixed_by` in
  `instruction_units.py`; (b) `overlay.py`; (c) the `check_fixed_sources` unit 32 built there, which
  the row checks import. (a) is a second resolver. RESOLVED (agent, 2026-11-10, delegated): (c), rung 2, re-resolved from (a). widens: none · relaxes: none
- **F9 — Unit 16's descriptor reader (id 63).** Options: (a) extend `regen.py`'s reader; (b) a glob
  reader; (c) unit 16's reader of the tracked files. (c) reads (a)'s population without the playbook
  kit importing run-gates. RESOLVED (agent, 2026-11-10, delegated): (c), rung 2, re-resolved from (a). widens: none · relaxes: none
- **F10 — Which Skills the Skill gate grades (id 40).** Options: (a) every tracked `SKILL.md` under a
  `skills/` directory, the measure's population too; (b) those plus each `SKILL.template.md`; (c)
  `skills/*/SKILL.md`. (b) grades unrendered tokens; (c) leaves a live Skill over the cap ungraded. RESOLVED (agent, 2026-11-10, delegated): (a), rung 3. widens: none · relaxes: none
- **F11 — How the Edges verbs join the closed set (id 51).** Options: (a) two types, each its own
  inverse; (b) one mutual-inverse pair; (c) no rows. The grammar declares no inverse at a site, and
  the hygiene gate wants both ends declared, so (b) reds every pair. RESOLVED (agent, 2026-11-10, delegated): (a), rung 3. widens: none · relaxes: none
- **F12 — Does a duplicate heading slug get a `-2` row (id 78).** Options: (a) yes; (b) no, since
  `one-subject` reds a duplicate in every document `extract_doc` reads. RESOLVED (agent, 2026-11-10, delegated): (b), rung 1. widens: none · relaxes: none
- **F13 — Is a section's `#<seg>` held to the tag cap (id 78).** Options: (a) red it, renaming the
  live headings over it; (b) cap the tag head alone and say so. Eight live headings fold past it,
  the charter's among them (DERIVED at `974700af5`). RESOLVED (agent, 2026-11-10, delegated): (b), rung 1. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-1 spec audit's 54 MEDIUM and 19 LOW findings batched by
  report id.
- rev-2 · 2026-10-24 · §3 · Edges mirror those units 50, 54 and 55 declare against this unit.
- rev-3 · 2026-10-24 · §1 · §2 · §3 · §4 · §6 · §7 · §8 · re-grounded by `../build/2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck.md`, row 50, U1 and U7: S1 follows unit 37's policy page, S30 and S31 read `budgets.*` caps, and the census is a step of its own (F3); trimmed under its cap: §1's id map, the edge glosses, §2's subheadings and §4 Order go, each fact kept.
- rev-4 · 2026-11-03 · §2 · §3 · §6 · from `2026-11-03-prompt-PLAY-dOrderedCharter-19-divergence-brief.md` Item 3: S38 and AC29 (id 44) go, folded into PLAY-dOrderedCharter-19's S9 and AC17 under BUILD-METHOD M4, since unit 19 moves `derive_baseline_additions` before this unit runs; the edge to unit 19 drops S38, every other item and its id kept.
- rev-5 · 2026-11-03 · §7 · from `2026-11-03-prompt-PLAY-dOrderedCharter-19-latent-hits-brief.md` Item 2: the leg line names `policy fixtures`, whose guard a §4 Files touched path trips, the guards hit the spec-token check reads with DEFERRED as live.
- rev-6 · 2026-11-08 · sections 1 to 7 · from `2026-11-08-prompt-PLAY-dOrderedCharter-39-drift-fold-brief.md`
  at `05aeb20a`: S31 reads enveloped files, not registry rows; the items unit 2's or 3's spec, the
  tree or their own pass met are observations, ids and criteria kept; S1 maps unit 37 F9's fields;
  units 54 and 55 follow this one.
- rev-7 · 2026-11-09 · S46 · from `2026-11-09-prompt-PLAY-dOrderedCharter-35-repair-brief.md` item
  1: PLAY-dOrderedCharter-35's composer is `derive_row_composition`, the name the naming lexicon
  passes, and S46 spells it.
- rev-8 · 2026-11-10 · sections 1 to 8 · S1 to S73 · AC1 to AC64 · F2 F3 F8 F9, new F10 to F13 · from
  `2026-11-10-prompt-PLAY-dOrderedCharter-49-precheck-brief.md`, pre-checked at `974700af5`: a
  correction to a CLOSED spec is observed here; the items met by built code or a landed spec say so;
  S11 mints no census step; S34 widens the Skill gate and fixes the Skill it reds; S40, S51 per F11 to
  F13; S48, S53, S63 and S68 cut to what HEAD lacks; citations are symbols or pinned lines;
  `tools/playbook/pins.py` leaves Files touched, unit 77 having renamed its two names at `26eda4214`;
  the leg line follows `--legs-for`; spec 23's `/build` line and spec 35's rooted AC14 confirmed (S59, S24).
- rev-9 · 2026-11-10 · AC26 · from `2026-11-10-prompt-PLAY-dOrderedCharter-49-ac26-brief.md`, observed
  at `8a9c55b65`: AC26's command passed no `--input spec=`, so the render refused before it could carry
  `input:code`; it now names the spec and the pre-check brief, each through `git ls-files` so every
  path is a tracked word of its own, and it renders over HEAD.
- 2026-11-10 · section 2 S34 · AC13 AC50 AC60 · from `2026-11-10-prompt-PLAY-dOrderedCharter-55-hygiene-fix-brief.md` item 2: S34's
  by-value escape opens on one line, so the check reads it; AC13 names the `Decided:` trailer, AC50
  unit 23's AC4 patterns and AC60 S20's grep, each the witness it already observed; a records fix,
  so the status line keeps its rev.

## 10. Reuse audit

Each item extends the seam its finding names, cited in section 2.
`python tools/codebase-map/reuse_lookup.py "one reader of a fact that two checks read twice"` ranked
`read`, `read_text` and `check` by name stem, no seam; the batch mints no reader a finding did not ask
for. The recall query returned TOOL-aDistilledCharter-7, TOOL-aGraftedHelix-32 and
TOOL-dSafePassage-35, precedent batches of a review's minors, whose per-id items this spec follows.

Recall terms used: `python tools/memory-recall/query.py "how were a round-one spec audit's medium and low findings batched into one unit" --terms "minors batch promoted MEDIUM LOW report id scope item round-1 spec audit disposition"`
