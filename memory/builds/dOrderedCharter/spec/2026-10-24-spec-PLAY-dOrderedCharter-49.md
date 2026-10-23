# PLAY-dOrderedCharter-49 — the round-1 spec audit's 73 minors: criteria that can pass, rows a new leg owes, one reader per fact, and seams in build order

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 39 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 |
| [2026-10-24-build-PLAY-dOrderedCharter-49-deviation-491.md](../build/2026-10-24-build-PLAY-dOrderedCharter-49-deviation-491.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |
| [2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md](../reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`) exited
with 83 confirmed findings; its ten highs are units 39 to 48. This unit is BUILD-METHOD M4's batch of
the rest, every MEDIUM and LOW, each report id its own §2 item, merged ids keeping the item's
criterion. The minors land on 35 units, so this unit is built last; each item names the part of a
unit's spec it supersedes, and that unit's §3 hands the part here.

The report's items and their ids, MEDIUM as M and LOW as L: M1 3 · M2 4, 66 · M3 5, 67 · M4 6, 7, 45 ·
M5 8 · M6 9 · M7 10 · M8 11 · M9 12 · M10 13 · M11 14 · M12 16, 34, 70 · M13 17, 33 · M14 18 · M15 19 ·
M16 20 · M17 21 · M18 22 · M19 32 · M20 35 · M21 36 · M22 37 · M23 38, 65 · M24 39, 83 · M25 40 ·
M26 41 · M27 42 · M28 43 · M29 44 · M30 46 · M31 51 · M32 52 · M33 53 · M34 54 · M35 55 · M36 59 ·
M37 60 · M38 68 · M39 69 · M40 71 · M41 77 · M42 78 · M43 84 · M44 85 · M45 86 · L1 15 · L2 23 · L3 24 ·
L4 25 · L5 26 · L6 27 · L7 28 · L8 29 · L9 47 · L10 50 · L11 57 · L12 61 · L13 63 · L14 64 · L15 72 ·
L16 73 · L17 74 · L18 75 · L19 87. S1 to S73 take these ids in order; M<n>'s criterion is AC<n> and
L<n>'s AC<45+n>, and each scope item names both.

Ids 12, 28, 41, 50 and 86 are built from the skeptic's corrected fix, as the report states it.

## 2. Scope (IN)

### Reference pages, leg keys and the rows a new leg owes

- **S1** — id 3. Each `[[reference]]` row of `tools/playbook/references.toml` gains `summary-from`
  and `usage-from`, naming the registry field unit 37's render reads for each (the kinds register's and
  drive table's from their owners' schemas at the pass, the unit registry's `help` and `usage`); an
  absent field refuses as unit 37 S2 says. This supersedes unit 37 S2's fixed names and settles its S5
  (§8 F2). Observed by AC1.
- **S2** — id 4. Both closed key sets of `tools/run-gates/run-gates.test.sh` (`:244`, `:580`) gain
  `enforces`, which unit 7 S2 adds to `tools/gate-legs.json`. Observed by AC2.
- **S3** — id 66. `enforces` never reaches a target's manifest: govkit's leg writer builds each row from
  named keys (`row = {"name": nm, "argv": argv}`, `tools/govkit/govkit.py:4422`), so no
  `ENFORCES_FLOOR_RUN_GATES` is owed beside `SUBJECT_FLOOR_RUN_GATES` (`:6010`); this item asserts it,
  and `tools/run-gates/run-gates.test.sh` joins unit 7's write set. Observed by AC2.
- **S4** — id 5. Every leg units 3, 7, 12, 13, 15, 20, 25 and 26 add to `tools/gate-legs.json`, DERIVED
  as the names absent at `ce13efbe`, gets its `tools/govkit/subject-pins.tsv` row (`govkit selfcheck
  --write`) and a measured `tools/run-gates/ceiling-evidence.txt` row. Observed by AC3.
- **S5** — id 67. Each such leg has a descriptor `[[gate_leg]]` or a `tools/govkit/registry.toml`
  `[[exempt_leg]]` row, as check 7h requires (`tools/govkit/govkit.py:2944-2946`), and a line in its
  kit's dossier under `memory/map/features/`; unit 16 S8's owed-rows sentence is the rule. Observed by
  AC3.

### Unit rows, overlay rows and build order

- **S6** — id 6. The placement fields are `scope` and `trigger`, never `select` and `when`, in unit 28
  S5's adapter, unit 32 S3, data model and AC9, unit 33 S6 and unit 34 S1 and §4 step 1, as unit 9 S1
  and unit 20 S1 name them; unit 32 F1 alone maps the clause's wording. Observed by AC4.
- **S7** — id 7. `edges` is a TOML list of S6 strings, `edges = ["amends=<tag>@<hash8>"]`, in unit 32's
  and unit 35's data models and readers, as unit 9 and unit 24 S2 write it. Observed by AC4.
- **S8** — id 45. Unit 32's level-0 example row is a `directive` with typed `text`, never a typed
  `fact`, which unit 12 S2 reds. Observed by AC4.
- **S9** — id 8. Unit 28's unit edge site, `read_unit_edges` and `read_text_history`, is built here
  over `read_units` (unit 9); unit 28's pass builds no parser of `instructions.toml`, which unit 9 AC4
  forbids. Observed by AC5.
- **S10** — id 9. Unit 32's reads of later units are wired here: its S4 reads `instructions.exclude`
  through unit 35's reader, its S5 resolves `fixed-by` through S45. Observed by AC6.
- **S11** — id 10. Unit 34's S8 census writes, and its AC1 and AC10, happen here, after unit 31's step
  creates gov's overlay: `write_overlay_units` (unit 32 S8) writes them from a `census` verb of
  `tools/govkit/steps/adopter_rules_to_overlay.py`, run once in gov's prepared merge (§8 F3). Observed
  by AC7.

### Tags, namespaces and their checks

- **S12** — id 11. Unit 19 S14's `owned` arm judges a tag by its namespace row's declaring extractor and
  registry location, never its minting file, so optional kits' `kit.<id>` tags do not red the core `kit`
  namespace. Observed by AC8.
- **S13** — id 12, from the skeptic's corrected fix. `role` and `item` stay unregistered (unit 10 S5):
  units 9 and 11 keep role-scoped and `required-by` rows fixture-only, unit 9's gov-tree sample row is
  scoped `reader.every`, and unit 20's schema check reds a gov-tree row scoped `role.gov-builder` (§8
  F4). Observed by AC9.
- **S14** — id 13. Unit 22 S2's purpose-source grammar admits `<path>#h1` and a whole-source path:
  `doc` is `<document path>#h1`, `unit` is `tools/playbook/instruction_units.py` read whole, and
  `level` is `tools/playbook/instruction_units.py#LEVELS`; unit 19's `doc` row and unit 22's table
  agree. Observed by AC10.
- **S15** — id 14. Unit 15's `foundation` pack resolves to unit 1's `foundation` array (`practices =
  "foundation"`), never `all`, which unit 15 AC10 asserts. Observed by AC11.

### Criteria that can pass on a correct build

- **S16** — id 16. Unit 18 AC1's grep is scoped `-- tools/memory-recall tools/memory-tree`. Observed by
  AC12.
- **S17** — id 34. The namesakes `def repo_root()` at `tools/codebase-map/map_lib.py:114`,
  `tools/drift-audit/drift_report.py:109` and `tools/govkit/govkit.py:126` stay, named in unit 18's §4.
  Observed by AC12.
- **S18** — id 70. Within that scope every hit is in `tools/memory-tree/id_grammar.py`, as unit 18 AC1
  says. Observed by AC12.
- **S19** — id 17. Unit 18 AC3 reads "every hit is a keep row of §4's table or a history comment named
  in the pass's `Decided:` trailer", as its AC2 does, naming the keep rows
  `tools/codebase-map/scen-adversarial.json:180` and `tools/govkit/selftest.py:9330`. Observed by AC13.
- **S20** — id 33. Unit 18 AC7 is an `ast` walk of every `*.py` under `tools/memory-tree/` finding no
  `recall_conf` import and no `KIT_MEMORY_RECALL_VERSION` attribute. Observed by AC13.
- **S21** — id 18. Unit 1 AC1 compares the 36 `foundation` tags with section 1's one-line region before
  `### Micro-formats`, never every `RULE_LINE_RE` match (46). Observed by AC14.
- **S22** — id 19. Unit 5 AC3 counts `- [verify] ` lines inside `### Charter rules` only, never unit
  21's `### Practices at build` line. Observed by AC15.
- **S23** — id 20. Unit 30 AC6 greps `\[bytes\]`, `\[cross-os\]`, `practice.bytes`,
  `practice.cross-os` and the `rules:` values `bytes` and `cross-os?` over
  `tools/playbook/practices.toml` and the role sources, never `-w bytes`. Observed by AC16.
- **S24** — id 21. Every criterion pathspec the report lists is spelled from the root:
  `tools/playbook/fixtures/row_kind.py` (unit 36 AC11), `help/overlay-rows.md` (unit 36 AC12, unit 35
  AC14), `help/charter.md` (units 1, 2 and 6, AC7), `tools/playbook/edge_grammar.py` (unit 28 AC3),
  `help/upgrade-steps.md` (unit 31 AC12), `help/composition.md` (unit 34 AC11); unit 35 AC14 greps
  `help/README.md` for the link. Observed by AC17.
- **S25** — id 22. Unit 3's envelope population includes `.claude/skills/cleanup/SKILL.md` and
  `skills/deploy-governance/SKILL.md`, whose sources `tools/branch-reconcile/SKILL.template.md` and
  `skills/deploy-governance/SKILL.md` join unit 3's write set. Observed by AC18.
- **S26** — id 32. Unit 28's commit site reads only id-shaped `Pass:` values, as `serves` edges, and
  counts `none` or prose as unread; `Decided:` is no edge site yet. Units 28's and 25's §4 Migration
  lose "already parse" and `**Caused-by:**`. Observed by AC19.

### The moved grammar (unit 18)

- **S27** — id 35. `tools/memory-recall/recall_conf.py` and `tools/memory-recall/bench.py` each carry
  the canonical `resolve_kit_dir` block, gated in `tools/lib/resolve-python.test.sh`, and reach
  `id_grammar` through it, never through `extract.py`, which imports `recall_conf` at module level
  (`tools/memory-recall/extract.py:60`). Observed by AC20.
- **S28** — id 36. `KIT_MEMORY_RECALL_VERSION` joins `query.py`'s cache manifest beside `conf_digest`,
  so a recall-only bump rebuilds a warm cache once `Conf.digest` hashes `id_grammar.py` (unit 18 S4).
  Observed by AC21.
- **S29** — id 37. Unit 18 AC5 gains a limb in a scratch tree with no `.memory-tree.conf`:
  `python -c "import sys; sys.path.insert(0,'tools/memory-tree'); import id_grammar, corpus_ids, gotchas"`
  exits 0. Observed by AC22.

### Sizes, locks and readers of real shapes

- **S30** — id 38. Unit 3 S7's crossed rows and AC7 name `.claude/skills/unattended/SKILL.md` (10237
  bytes at `ce13efbe` against its 10240 row, `tools/template-size-limits.txt:151`). Observed by AC23.
- **S31** — id 65. The crossed set is DERIVED at the pass, each enveloped file plus its two envelope
  lines against its size row, and each crossed row's leg, `unattended skill size` among them, joins
  unit 3's gates. Observed by AC23.
- **S32** — id 39. Unit 12's `lock --check` compares a row's blob with `git hash-object --path=<path>
  <file>`, so a CRLF checkout of an LF blob stays green. Observed by AC24.
- **S33** — id 83. `.gitattributes` routes `.governance/instructions.lock` to `merge=ours`, and the
  prepared merge's re-render rewrites every lock row, so a merged lock is never kept (§8 F5). Observed
  by AC24.
- **S34** — id 40. One reader of a Skill's `description`, folded scalars included, lifted from
  `tools/runlog/selftest.py:8172` into `tools/playbook/core.py`, serves unit 7 S6's gate and unit 11
  S5's measure; kind.skill's population is every tracked `SKILL.md` and `SKILL.template.md`. Observed
  by AC25.
- **S35** — id 41, from the skeptic's corrected fix. `render_handoff` (`tools/roles/handoff.py:312`)
  appends a `### input:code` block of the file's text, whatever the role's `reads`, after the read blocks
  and before the charter blocks; an unsupplied slot joins the `Not supplied, optional` line (`:412-414`). Unit 27's §10 calls
  it new code. Observed by AC26.
- **S36** — id 42. `read_units(root)` finds manifests under `root`'s install prefix, never `__file__`'s
  kit parent. Observed by AC27.
- **S37** — id 43. Unit 16's `import` detector resolves a module through the importer's `sys.path`;
  failing that, a name also in a core home or beside the importer is no non-core edge
  (`tools/run-gates/measure_legs.py:1001-1006` imports process-monitor's `census`). Observed by AC28.
- **S38** — id 44. `derive_baseline_additions` moves to `tools/lib/coverage_join.py` taking the baseline
  text; `map_lib`'s wrapper supplies `map_root(root)/'baseline.toml'`
  (`tools/codebase-map/map_lib.py:214-216`, `:1530`), so the core reads no optional kit's conf (unit
  19 S9, F2). Observed by AC29.
- **S39** — id 46. Unit 37's run arm spawns through govkit's `resolve_bash()`
  (`tools/govkit/govkit.py:1144`), never a bare `bash`. Observed by AC30.

### One predicate, one reader

- **S40** — id 51. Unit 24's `tools/playbook/edges.toml` registers `consumes-from` and `hands-off` as
  inverses sited in a spec's `### Edges` block, which check 12
  (`tools/memory-tree/check-memory-hygiene.sh:2474`, `:2714`) and `HANDOFF_BULLET`
  (`tools/check-spec-tokens.py:376`) keep parsing. Observed by AC31.
- **S41** — id 52. `tools/playbook/edge_checks.py` is not built; `gov_tag.py check --only
  type-registered|target-resolves` calls unit 24's `check_edges` and unit 28's resolver, and unit 28's
  `edges` leg owns both arms (§8 F6). Observed by AC32.
- **S42** — id 53. Unit 1's `read_practice_catalogue` refuses only what it cannot parse; a line's shape
  and size are unit 7's gate's, on the rendered line via `render_playbook.py`'s one-line check.
  Observed by AC33.
- **S43** — id 54. Unit 29's `one-owner` calls unit 22's owner predicate, which reads
  `memory/project/chain.toml`, for namespace, unit and kind rows, never `memory/builds/` (§8 F7).
  Observed by AC34.
- **S44** — id 55. Unit 29's `one-subject` and S8's retirement arm slug headings with unit 19's slug
  function from `tools/playbook/tag_index.py`. Observed by AC35.
- **S45** — id 59. One `resolve_fixed_by(source)` in `tools/playbook/instruction_units.py`, on unit 26's
  symbol finder, serves unit 32's `derive_unit_class` and unit 36's row checks (§8 F8). Observed by
  AC36.
- **S46** — id 60. Unit 33's `derive_pin_state` takes a canonicaliser, and unit 35's `compose_rows`
  calls it for steps 4 and 5, as unit 35's §10 says. Observed by AC37.

### Moves, docs and registries the move leaves

- **S47** — id 68. The moved `git()` in `tools/memory-tree/id_grammar.py` passes `encoding="utf-8"`;
  `memory/project/encoding-posture-sites.txt:29` loses or re-counts its `extract.py` row. Observed by
  AC38.
- **S48** — id 69. The adopter docs say the grammar ships in memory-tree's `id_grammar.py`:
  `tools/memory-tree/HYGIENE.template.md` (its memory-recall paragraphs, rendered into `memory/HYGIENE.md`), `WIRE-INTO-PROJECT.md`
  (the SIBLINGS paragraph) and `tools/memory-tree/README.md`. Observed by AC39.
- **S49** — id 71. Unit 31 S1's Readers add `memory/project/spawn-idiom-sites.txt`,
  `memory/project/testsuite-count-waivers.txt` and `memory/project/unarmed-branches.txt`, whose
  `tools/agent-instructions/` rows leave with the directory; the `shell hygiene`, `testsuite counts` and
  `harness arms` legs join unit 31's gates. Observed by AC40.

### The index's edges

- **S50** — id 77. Each resolver call replaces the worktree's dirty rows with the current dirty set
  keyed by blob, and drops rows of a worktree `git worktree list` no longer names. Observed by AC41.
- **S51** — id 78. `extract_doc` skips fenced headings by CommonMark's rules, numbers a duplicate slug
  `-2`, `-3`, and reds a `#<seg>` over the 64-byte `TAG_MAX_BYTES`. Observed by AC42.
- **S52** — id 84. Unit 37's run arm runs one fenced block, indented ones included, as one script; a
  `<…>` placeholder is a finding unless its block is marked `<!-- run: no — placeholder -->`, which
  `help/measure-legs.md:79-80` and `help/roles.md:35-37` take. Observed by AC43.
- **S53** — id 85. Each value the record factory writes into a `**Key:**` line is one line: CR, LF and a
  value opening `**<Word>:**` refuse, `Words` is one escaped string, unit 2's `--rule` is checked
  against the catalogue, and a refusal leaves no file. Observed by AC44.
- **S54** — id 86, from the skeptic's corrected fix. `write_card_file` records the owning session id in
  the card's header and refuses a card another live session owns, printing
  `card-file — skipped: another live session <sid> owns this tree`. Observed by AC45.

### The lows

- **S55** — id 15. Unit 29's rule-to-check row for `practice.writing.address` names
  `tags positional selftest`, unit 26 S7's leg. Observed by AC46.
- **S56** — id 23. Unit 25 S5 follows unit 24 S4: a declared `cites` is graded; the duplicated arms are
  S41's. Observed by AC47.
- **S57** — id 24. `one-owner` reads the owner set from unit 22's chain registry, plus layers only for
  row kinds admitting a layer owner. Observed by AC48.
- **S58** — id 25. Unit 10's `repo` row has role `describes`, so S4's "two selector namespaces" holds;
  an `empty-ns` plant covers `repo`. Observed by AC49.
- **S59** — id 26. Unit 23's §4 table adds `memory/guides/BUILD-METHOD.md:286` and its source
  `tools/memory-tree/BUILD-METHOD.template.md:286`. Observed by AC50.
- **S60** — id 27. Unit 12 AC1 asserts `STATEMENT_TYPES` from `tools/playbook/instruction_units.py`
  equals the closed set, and `git grep -n "STATEMENT_TYPES *=" -- tools` prints one line. Observed by
  AC51.
- **S61** — id 28, from the skeptic's corrected fix. Unit 26 AC10 compares the list's file:line row
  count with `git grep -I -oE '[A-Za-z0-9_./-]+\.(py|sh|js|mjs|ts|toml|json):[0-9]+' -- .
  ':!tools/playbook/positional-refs.txt' | sort -u | wc -l` at the pass, with no `-h`. Observed by AC52.
- **S62** — id 29. Unit 33's `run_unit_drift` is the one printer of stale and orphaned units at
  `update`; unit 34's relay filters them out. Observed by AC53.
- **S63** — id 47. Unit 2 S6's re-point list is a grep at the pass, re-pointing
  `WIRE-INTO-PROJECT.md:122`, `tools/roles/roles_lib.py:202`, `tools/roles/check_roles.py:15` and
  `tools/unattended/unattended.sh:655` and `:8447`, kept hits named in the `Decided:` trailer.
  Observed by AC54.
- **S64** — id 50, from the skeptic's corrected fix. Unit 20 §10 names `[[regenerate]].writes`
  (`tools/playbook/kit.toml:53-55`), and every `writes` instruction file falls under a
  `tools/playbook/renderers.toml` row of the same kit's renderer. Observed by AC55.
- **S65** — id 57. Unit 3 S6 reads `INSTRUCTION_PATHSPECS` (unit 20 S4) and types no population; its "from
  then on" non-goal goes. Observed by AC56.
- **S66** — id 61. `tools/playbook/core.py` imports `compute_coverage` from
  `tools/memory-tree/coverage_join.py` through `resolve_kit_dir`, as unit 10 does, with no copy.
  Observed by AC57.
- **S67** — id 63. Unit 16's descriptor reader extends `read_descriptors`
  (`tools/run-gates/regen.py:108`) for `tools/govkit/entries/*.kit.toml`, minting no glob reader (§8
  F9). Observed by AC58.
- **S68** — id 64. Unit 14's `resolve_auto_memory_dir` calls `common_git_dir`
  (`tools/lib/common_dir.py`, unit 19 S10) in one parity group, never its own `git rev-parse --git-common-dir`. Observed by
  AC59.
- **S69** — id 72. Unit 18 AC7's comment hits are S20's code check. Observed by AC60.
- **S70** — id 73. Unit 18's write set names `tools/memory-tree/check-verdict-epoch.test.sh`, and its
  gates the verdict-epoch, merge-rows, memory-hygiene, corpus-ids, row-grammar, gotchas, check-wiring
  and memory-recall legs whose suites its S9 rewrites. Observed by AC61.
- **S71** — id 74. Unit 12 AC5 and its lock example derive the marker with
  `sed -n 's/.*governance-template: \(v[0-9.]*\).*/\1/p' coding-governance-agents.template.md`, and
  its S5 Readers add `memory/map/features/session-kickoff.md:153`. Observed by AC62.
- **S72** — id 75. Unit 2's Inventory names `TEMPLATE_MAJOR = 5` (`tools/playbook/render_playbook.py:343`)
  beside the v5.0 marker and the pair at `tools/check-playbook-parity.sh:273`; its Migration reads v4.x
  as older for the reseed note and the legacy-placeholder refusal. Observed by AC63.
- **S73** — id 87. Unit 4's replay passes `--root "$CARD_TREE"` to `instruction_units.py map`, the tree
  unit 8 resolves from the payload's `cwd`. Observed by AC64.

## 3. Non-goals (OUT)

- Any high of the same audit: units 39 to 48.
- Re-ordering any unit: a seam in the wrong order (S9, S10, S11) is built here, last (§4 Order).
- Changing a repaired unit's clause or carries line.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-1` — the catalogue reader and its AC1 (S21, S42)
- **consumes-from** `PLAY-dOrderedCharter-2` — the override writer, its re-point list and its v5.0 marker (S53, S63, S72)
- **consumes-from** `PLAY-dOrderedCharter-3` — the envelope population and its size rows (S25, S30, S31, S65)
- **consumes-from** `PLAY-dOrderedCharter-4` — the replay's map call (S73)
- **consumes-from** `PLAY-dOrderedCharter-5` — its AC3 count (S22)
- **consumes-from** `PLAY-dOrderedCharter-6` — its page criterion (S24)
- **consumes-from** `PLAY-dOrderedCharter-7` — the enforces key, the Skill gate, the factory and the core module (S2, S3, S34, S53, S66)
- **consumes-from** `PLAY-dOrderedCharter-8` — the card file writer (S54)
- **consumes-from** `PLAY-dOrderedCharter-9` — the unit reader and its sample row (S13, S36)
- **consumes-from** `PLAY-dOrderedCharter-10` — the repo row's role (S58)
- **consumes-from** `PLAY-dOrderedCharter-11` — the role-scoped load set and the Skill measure (S13, S34)
- **consumes-from** `PLAY-dOrderedCharter-12` — the provenance lock and its criteria (S32, S33, S60, S71)
- **consumes-from** `PLAY-dOrderedCharter-13` — the ladder leg (S4, S5)
- **consumes-from** `PLAY-dOrderedCharter-14` — the auto-memory resolver (S68)
- **consumes-from** `PLAY-dOrderedCharter-15` — the foundation pack and the change writer (S15, S53)
- **consumes-from** `PLAY-dOrderedCharter-16` — the import detector and the descriptor reader (S37, S67)
- **consumes-from** `PLAY-dOrderedCharter-18` — the moved grammar, its criteria and its docs (S16 to S20, S27 to S29, S47, S48, S69, S70)
- **consumes-from** `PLAY-dOrderedCharter-19` — the owned arm, the moved baseline function, the dirty rows and the doc extractor (S12, S38, S44, S50, S51)
- **consumes-from** `PLAY-dOrderedCharter-20` — the schema check and the renderer-of-record table (S13, S64)
- **consumes-from** `PLAY-dOrderedCharter-22` — the purpose-source grammar and the owner predicate (S14, S43)
- **consumes-from** `PLAY-dOrderedCharter-23` — its readers table (S59)
- **consumes-from** `PLAY-dOrderedCharter-24` — the edge registry and its check (S40, S41)
- **consumes-from** `PLAY-dOrderedCharter-25` — the two edge checks and its cites rule (S41, S56)
- **consumes-from** `PLAY-dOrderedCharter-26` — its AC10 and the symbol finder (S61, S45)
- **consumes-from** `PLAY-dOrderedCharter-27` — the code slot (S35)
- **consumes-from** `PLAY-dOrderedCharter-28` — the unit site, the commit site and the edges leg (S6, S9, S26, S41)
- **consumes-from** `PLAY-dOrderedCharter-29` — the owner and subject checks and the rule-to-check row (S43, S44, S55, S57)
- **consumes-from** `PLAY-dOrderedCharter-30` — its AC6 (S23)
- **consumes-from** `PLAY-dOrderedCharter-31` — its readers and its step program (S49, S11)
- **consumes-from** `PLAY-dOrderedCharter-32` — the overlay's data model and its two late reads (S6 to S8, S10)
- **consumes-from** `PLAY-dOrderedCharter-33` — the pin walk and the drift printer (S46, S62)
- **consumes-from** `PLAY-dOrderedCharter-34` — the census writes and the relay (S11, S62)
- **consumes-from** `PLAY-dOrderedCharter-35` — the row composer and its data model (S7, S46)
- **consumes-from** `PLAY-dOrderedCharter-36` — the fixed-by resolution and its criteria (S45, S24)
- **consumes-from** `PLAY-dOrderedCharter-37` — the reference render and the run arm (S1, S39, S52)
- **consumes-from** `PLAY-dOrderedCharter-50` — the owed-rows probe, whose rows S2 to S5, S30, S31 and S49 observe (round-2 id 23)
- **hands-off** `PLAY-dOrderedCharter-54` — S54's owner liveness and takeover (round-2 id 39)
- **hands-off** `PLAY-dOrderedCharter-55` — round-2 ids 2, 6, 8, 16, 24, 40 and 41: the corrected criteria observed here, `edge_checks.py` deleted, the census render, AC26's flags, this spec's size, the lock's merge and the dirty-row key

## 4. Design

### Evidence

Read at `ce13efbe`; each finding's evidence is the report's appendix row, every §2 citation re-read
there, with govkit's floors (`tools/govkit/govkit.py:6010-6017`), `render_handoff`'s
read loop (`tools/roles/handoff.py:382-396`), `git()` (`tools/memory-recall/extract.py:282`) and govkit's
own descriptor reader (`tools/govkit/govkit.py:13238`).

### Order

Order 39, last: each item edits code its unit built; the late halves S9, S10 and S11 stay out of
their units' passes.

### Inventory

Minted: the `[[reference]]` fields `summary-from` and `usage-from`; `resolve_fixed_by`; the
`description` reader in `tools/playbook/core.py`; the `census` verb of the adopter-rules step program;
the `.gitattributes` line for `.governance/instructions.lock`; the plant names each criterion stages.
Naming cells: `lexicon naming predicates` grades the Python names.

### Files touched (estimate)

- `tools/playbook/references.toml`
- `tools/playbook/render_playbook.py`
- `tools/playbook/instruction_units.py`
- `tools/playbook/overlay.py`
- `tools/playbook/overlay_rows.py`
- `tools/playbook/row_checks.py`
- `tools/playbook/pins.py`
- `tools/playbook/edge_grammar.py`
- `tools/playbook/edges.toml`
- `tools/playbook/gov_tag.py`
- `tools/playbook/tag_index.py`
- `tools/playbook/namespaces.toml`
- `tools/playbook/packs.toml`
- `tools/playbook/core.py`
- `tools/playbook/check_layers.py`
- `tools/playbook/writing_practice.py`
- `tools/playbook/positional.py`
- `tools/playbook/load_sets.py`
- `tools/playbook/kit.toml`
- `tools/playbook/renderers.toml`
- `tools/run-gates/run-gates.test.sh`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/govkit/govkit.py`
- `tools/govkit/docs_leg.py`
- `tools/govkit/steps/adopter_rules_to_overlay.py`
- `tools/run-gates/ceiling-evidence.txt`
- `memory/map/features/playbook.md`
- `tools/memory-tree/id_grammar.py`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/HYGIENE.template.md`
- `tools/memory-tree/README.md`
- `memory/HYGIENE.md` (its render)
- `tools/memory-recall/recall_conf.py`
- `tools/memory-recall/bench.py`
- `tools/memory-recall/query.py`
- `tools/lib/resolve-python.test.sh`
- `tools/lib/auto_memory.py`
- `tools/roles/handoff.py`
- `tools/branch-reconcile/SKILL.template.md`
- `skills/deploy-governance/SKILL.md`
- `skills/session-kickoff/manifest-check.sh`
- `memory/project/encoding-posture-sites.txt`
- `memory/project/spawn-idiom-sites.txt`
- `memory/project/testsuite-count-waivers.txt`
- `memory/project/unarmed-branches.txt`
- `.gitattributes`
- `.governance/instructions.toml` (by S11's step verb)
- `WIRE-INTO-PROJECT.md`
- `help/measure-legs.md`
- `help/roles.md`
- `tools/roles/roles_lib.py`
- `tools/roles/check_roles.py`
- `tools/unattended/unattended.sh`

### Rollout

Live at landing; its write set meets nearly every unit's, so it runs last and alone.

### Alternatives rejected

- **Folding each minor into its unit's spec.** The disposition rule batches every minor (BUILD-METHOD M4).
- **Two batches.** No split has disjoint write sets: nearly every repaired unit's items touch
  `tools/playbook/`.

## 5. Production-readiness checklist

- security: S53 holds the factory to one-line values; S39 drops a shell resolving elsewhere; nothing
  widens.
- perf / scale: S50 adds one `git worktree list` per resolver call; the rest are reads.
- error / empty / loading states: each item keeps its unit's refusals; S11's verb writes nothing when
  no row moved.
- observability: S26 prints unread trailers by count; S54 prints its skip line.
- risks: built last, it carries each repaired unit's late half and re-observes its criteria.
- testing: AC1 to AC64, probes or plants of each repaired unit's fixture.
- migration: S33's attribute takes effect on the next merge.
- user docs: S48's three adopter docs; S24's page paths.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --reference --check` runs, it exits 0 over
  the four pages, and a planted row missing its mapped `usage-from` field refuses naming the registry.
  Red when: a registry with no `summary` field refuses a correct build.
- **AC2** — When `git grep -n '"enforces"' -- tools/run-gates/run-gates.test.sh` runs, both key sets
  carry it, and a probe of `govkit apply` over a fixture target shows no `enforces` key in its manifest.
  Red when: a leg carrying `enforces` reds the canary, or the key reaches a target.
- **AC3** — When a probe lists the legs in `tools/gate-legs.json` absent at `ce13efbe`, each is named in
  `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt`, a descriptor `[[gate_leg]]`
  or `[[exempt_leg]]` row, and a dossier under `memory/map/features/`.
  Red when: a new leg misses one of the four.
  figure: DERIVED, the population read at the pass.
- **AC4** — When a probe parses every TOML data-model block of units 28, 32, 33, 34 and 35 through
  `read_units` or `read_overlay`, each parses, and `git grep -n -e "select =" -e "when =" -- tools/playbook/`
  prints no row field.
  Red when: a spec's example row fails its reader.
- **AC5** — When `git -C tools/playbook grep -n "instructions.toml" -- edge_grammar.py` runs, it prints no
  parse of the file, and the unit site's adapter reads rows through `read_units`.
  Red when: a second parser of the manifest exists.
- **AC6** — When unit 32's `--plant` cases for its AC5 and AC6 run after units 35 and 36 land, both
  pass.
  Red when: either late read is unwired.
- **AC7** — When gov's prepared merge runs the step's `census` verb, gov's overlay holds one level-0
  `repo.` unit per moved row, and unit 34's AC1 and AC10 hold over gov's tree.
  Red when: a moved line is lost from gov's charter.
- **AC8** — When `python gov_tag.py check` runs over gov's tree, the `kit` namespace reads
  clean with its full membership.
  Red when: an optional kit's `kit.<id>` reds `owned`.
- **AC9** — When `python instruction_units.py schema` runs over a fixture row scoped
  `role.gov-builder`, it reds naming the unregistered `role` namespace, and over gov's tree it exits 0.
  Red when: a gov-tree row relies on an unregistered namespace.
- **AC10** — When unit 22's purpose arm runs over gov's ten namespace rows, it exits 0, and a planted
  `doc` row spelled as a section anchor reds.
  Red when: a declared purpose source fails the grammar.
- **AC11** — When `python instructions_edit.py fixture --plant packs` resolves
  `foundation`, the result equals unit 1's `foundation` array.
  Red when: the pack and the array differ.
- **AC12** — When `git grep -n -E "def (repo_root|grammar_for|anchor_at)" -- tools/memory-recall tools/memory-tree`
  runs, every hit is in `id_grammar.py`, and the three namesakes outside that scope
  are unchanged.
  Red when: a namesake is moved, or a moved name keeps a second definition.
- **AC13** — When unit 18's second query runs, every hit is a keep row or a trailer-named comment, and
  the `ast` walk finds no `recall_conf` import under `tools/memory-tree/`.
  Red when: a criterion demands empty output from a population the rule keeps.
- **AC14** — When unit 1's `practices --list` runs, its 36 `foundation` tags equal the one-line tags of
  section 1 before `### Micro-formats` in `AGENTS.md`.
  Red when: the comparison reads the micro-format tags.
- **AC15** — When unit 5's AC3 counts `- [verify] ` inside `### Charter rules`, it reads 1 with unit 21's
  reach line present.
  Red when: the reach line is counted.
- **AC16** — When unit 30's corrected grep runs over `practices.toml`, it prints no
  retired spelling.
  Red when: the grep hits prose or matches nothing for want of a path.
- **AC17** — When `git ls-files` runs after the pass over S24's six paths, each is listed, and every
  corrected criterion names it so.
  Red when: a criterion's pathspec matches no file.
- **AC18** — When unit 3's `envelopes --check` runs, it exits 0 with both Skills enveloped.
  Red when: a population member's source is outside the write set.
- **AC19** — When unit 28's `edges` leg runs over `ce13efbe..HEAD`, it exits 0 and prints the count of
  unread trailers.
  Red when: a prose `Decided:` value reds or is read as an edge.
- **AC20** — When `git grep -n "resolve_kit_dir — canonical copy" -- tools/memory-recall/recall_conf.py tools/memory-recall/bench.py`
  runs, each file carries the gated block, and importing both in a scratch tree raises no cycle.
  Red when: a re-exporter reaches the grammar through `extract.py`.
- **AC21** — When a probe bumps only `KIT_MEMORY_RECALL_VERSION` in a scratch copy, `ensure_cache`
  rebuilds and names the cause.
  Red when: a warm cache is served after a recall-only bump.
- **AC22** — When S29's limb runs in a scratch tree with no `.memory-tree.conf`, it exits 0; with a
  module-level `resolve()` planted in `id_grammar.py`, it fails.
  Red when: the no-conf import is unobserved.
- **AC23** — When the pass measures each enveloped file against its row, the crossed set includes
  `.claude/skills/unattended/SKILL.md` and unit 3's gates name `unattended skill size`.
  Red when: a crossed row is missed.
  figure: DERIVED at the pass.
- **AC24** — When unit 12's fixture plants a CRLF checkout of an LF target, `lock --check` stays green,
  a one-byte change reds, and `git -C .governance check-attr merge -- instructions.lock` prints `ours`.
  Red when: line endings red a clean tree, or a merged lock is kept unrendered.
- **AC25** — When `core.py fixture --plant skill-folded` plants a folded `description` over 1024 bytes,
  the Skill gate reds it.
  Red when: a folded description reads as two bytes.
- **AC26** — When `python tools/roles/handoff.py render --role gov-builder --input code=<file> --stdout`
  runs, the output carries a `### input:code` block with the file's text; without the input the
  `Not supplied, optional` line names `input:code`.
  Red when: the code input is dropped silently.
- **AC27** — When `read_units(fixture_root)` runs from gov's checkout, it returns only the fixture's rows.
  Red when: gov's manifests are read instead.
- **AC28** — When unit 16's leg runs with a same-name plant (`census` in a core and a non-core home), it
  reports no edge for `measure_legs.py`'s import.
  Red when: a namesake becomes a non-core edge.
- **AC29** — When `git -C tools/lib grep -n "map_root\|load_conf" -- coverage_join.py` runs, it prints
  nothing, and unit 19's codebase-map arm stays green.
  Red when: the core reads codebase-map's conf.
- **AC30** — When the run arm runs with a PATH whose first `bash` is a planted stub, the stub is never
  called.
  Red when: a bare `bash` is spawned.
- **AC31** — When `python edge_grammar.py --list` runs, `consumes-from` and `hands-off`
  print as mutual inverses with the spec Edges block as their site.
  Red when: the vocabulary stays outside the closed set.
- **AC32** — When `git ls-files -- '*edge_checks.py'` runs, it prints nothing, and both `--only`
  arms red the same planted edge as unit 28's leg.
  Red when: two checkers of one predicate exist.
- **AC33** — When `read_practice_catalogue` reads a planted row whose raw line is 190 bytes, it accepts
  it, and unit 7's gate decides on the rendered line.
  Red when: the reader and the gate disagree on size.
- **AC34** — When a namespace row owned by a layer is checked, `one-owner` and unit 22 give one verdict.
  Red when: the two legs disagree.
- **AC35** — When `one-subject` runs over `memory/guides/BUILD-METHOD.md`, it slugs `## M5 — Recall and
  reuse` as `m5-recall-and-reuse`.
  Red when: GitHub's slug is used.
- **AC36** — When `git grep -n "def resolve_fixed_by" -- tools/playbook/` runs, it prints one line, and a
  row and a unit with one source resolve alike.
  Red when: a second resolver exists.
- **AC37** — When unit 35's composer runs, a probe records `derive_pin_state` called for each pinned row.
  Red when: the walk is restated.
- **AC38** — When the encoding-posture scanner runs, it prints no site for `id_grammar.py`, and the
  registry's set equality holds.
  Red when: the moved `git()` names no encoding.
- **AC39** — When `git grep -n -e "requires that kit" -e "SIBLINGS" -- tools/memory-tree/HYGIENE.template.md WIRE-INTO-PROJECT.md tools/memory-tree/README.md`
  runs, it prints nothing.
  Red when: a doc still says memory-tree needs memory-recall.
- **AC40** — When unit 31's first query runs after the pass, no row of the three registries names
  `tools/agent-instructions/`.
  Red when: a registry row outlives its directory.
- **AC41** — When `gov_tag.py --fixture --plant dirty-revert` and `--plant worktree-recreate` run, `show`
  serves the reverted text, and a re-created worktree inherits no row.
  Red when: a dirty row outlives its edit.
- **AC42** — When `extract_doc` runs over `memory/TEMPLATE-SPEC.md`, no row comes from a fenced
  heading, and a planted duplicate heading yields `-2`.
  Red when: a fenced or duplicate heading mints a row.
- **AC43** — When `docs_leg.py --run --page help/roles.md` runs, the placeholder block is counted as
  `run: no` with its reason, and a planted unmarked placeholder is a finding.
  Red when: a placeholder runs or is silently skipped.
- **AC44** — When the factory's `new exception --reason $'a\nExpires: 2099-01-01'` runs, it exits 1 and
  writes no file.
  Red when: a newline forges a field.
- **AC45** — When `write_card_file` runs in a fixture for two live session ids in one tree, the first
  session's card survives and the `card-file — skipped:` line prints.
  Red when: a second session overwrites the first's card.
- **AC46** — When `git -C tools/playbook grep -n "tags positional selftest" -- writing_practice.py` runs, the
  row names the leg unit 26 mints.
  Red when: the row names a leg no unit mints.
- **AC47** — When a declared `cites` edge is planted, unit 25's arm and unit 24's `check_edges` give one
  verdict.
  Red when: the two disagree on `cites`.
- **AC48** — When `one-owner` checks a namespace row, its owner set equals the builds of unit 22's
  `chain.toml`.
  Red when: `memory/builds/` is read as the owner set.
- **AC49** — When `gov_tag.py --fixture --plant empty-ns` runs over `repo`, it prints `unarmed`, and
  `repo`'s row has role `describes`.
  Red when: the prose count and the table disagree.
- **AC50** — When unit 23's AC4 grep runs, every hit is a row of its table, `memory/guides/BUILD-METHOD.md`
  among them.
  Red when: the two BUILD-METHOD lines are unlisted.
- **AC51** — When `git grep -n "STATEMENT_TYPES *=" -- tools` runs, it prints one line.
  Red when: a fixture literal counts as a definition.
- **AC52** — When S61's `git grep -I -oE` count runs at the pass, it equals the list's file:line row
  count.
  Red when: the counts differ on a correct build.
- **AC53** — When `govkit update` runs over a fixture with one stale unit, the stale line prints once.
  Red when: two sources print it.
- **AC54** — When `git grep -n -i -E "charter's section [0-9]|section 1" -- WIRE-INTO-PROJECT.md tools/roles/roles_lib.py tools/roles/check_roles.py tools/unattended/unattended.sh`
  runs after the pass, every hit is re-pointed or named in the trailer.
  Red when: a charter-section citation is missed.
- **AC55** — When the render gate runs with a planted `writes` path no `renderers.toml` row claims, it
  reds naming the path.
  Red when: an instruction file's writer is declared twice with no join.
- **AC56** — When `git grep -n "INSTRUCTION_PATHSPECS" -- tools/playbook/` runs, unit 3's envelope gate is
  among the readers, and no typed population remains there.
  Red when: two populations of instruction files exist.
- **AC57** — When `git -C tools/playbook grep -n "def compute_coverage" -- core.py` runs, it prints nothing.
  Red when: an ungated third copy exists.
- **AC58** — When `git grep -n "def read_descriptors" -- tools/playbook/` runs, it prints nothing, and the
  layer check reads descriptors through `regen.py`'s reader.
  Red when: a third reader of one population is minted.
- **AC59** — When `git -C tools/lib grep -n "git-common-dir" -- auto_memory.py` runs, it prints nothing.
  Red when: a second common-dir derivation exists.
- **AC60** — When S20's `ast` walk runs over `tools/memory-tree/`, comment lines are not counted.
  Red when: a history comment reds the criterion.
- **AC61** — When `git grep -n "check-verdict-epoch.test" -- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-18.md`
  runs, the suite is named under unit 18's Files touched.
  Red when: a new arm's suite is outside the write set.
- **AC62** — When unit 12's AC5 derives its marker with S71's `sed` over the template, it matches after
  units 1 and 2 move the marker.
  Red when: a literal version pins the criterion.
- **AC63** — When a probe reads `TEMPLATE_MAJOR` from `tools/playbook/render_playbook.py` and the marker
  from `coding-governance-agents.template.md`, the two majors agree.
  Red when: the marker moves alone.
- **AC64** — When unit 4's replay runs with a payload whose `cwd` is a fixture worktree carrying a
  different registry row, the map names the worktree's row.
  Red when: the replay reads the hook's working directory.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `playbook parity` · `govkit acceptance matrix` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `codebase-map coverage + freshness` · `memory hygiene` · `memory-hygiene self-test` · `encoding posture (text IO names its encoding)` · `python resolver (behaviour + inline parity + idiom ban)` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `roles render selftest` · `roles render wiring` · `cleanup skill wiring` · `unattended skill size` · `lexicon naming predicates` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)` · `kit/dogfood doc parity` · `branch-reconcile selftest` · `manifest-check self-test` · `scratch-guard self-test` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC8 AC10 AC41 AC42 AC49 · the playbook-render selftest runs the tree-level tag probes and the index plants, each failing case staged by the repaired unit's base rule · none
New arm: tools/run-gates/run-gates.test.sh · covers AC2 · the canary's key sets with `enforces`, staged by removing it from one set · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) parts of 35 units'
  clauses. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — How a reference page reads `summary` and `usage` (id 3).** Options: (a) a per-registry field
  map in `references.toml`; (b) the two fields in four owners' schemas, one a dGroundRules catalogue
  this build does not own. RESOLVED (agent, 2026-10-24, delegated): (a),
  rung 3. widens: none · relaxes: none
- **F3 — Which door writes the census units into gov's overlay (id 10).** Options: (a) a `census` verb
  of unit 31's step program, run once on gov's tree in the prepared merge; (b) unit 15's command once
  dDeclaredLoop's guard lands; (c) an agent's edit. (b) leaves gov's charter short until a later
  build; the minimal guard refuses (c). RESOLVED (agent, 2026-10-24, delegated): (a),
  rung 3. widens: none · relaxes: none
- **F4 — Do `role` and `item` register now (id 12).** Options: (a) keep them unregistered and the
  feature fixture-only, as unit 10 S5 rules; (b) register `role` here with the roster as its source.
  (b) re-opens unit 10's settled scope. RESOLVED (agent, 2026-10-24, delegated): (a), rung 1, unit 10
  S5. widens: none · relaxes: none
- **F5 — How the whole-file lock merges (id 83).** Options: (a) `merge=ours` plus the prepared merge's
  re-render; (b) a regenerating merge driver, withdrawn for the structural reason `merge-rows.py`'s
  docstring records. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3.
  widens: none · relaxes: none
- **F6 — Who owns the two edge arms (id 52).** Options: (a) unit 28's leg owns both, `gov_tag.py check
  --only` calls the same functions; (b) unit 25's module owns them. (b) is the duplicate. RESOLVED
  (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F7 — Which owner set `one-owner` reads (id 54).** Options: (a) unit 22's predicate over
  `memory/project/chain.toml`, extended to unit and kind rows; (b) `memory/builds/` plus layers. (b) is
  the second answer. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F8 — Where `resolve_fixed_by` lives (id 59).** Options: (a) `tools/playbook/instruction_units.py`,
  which both callers import; (b) `tools/playbook/overlay.py`. (b) makes the row checks import the
  overlay module for a grammar. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none ·
  relaxes: none
- **F9 — Unit 16's descriptor reader (id 63).** Options: (a) extend `regen.py`'s tracked-file reader
  for `tools/govkit/entries/*.kit.toml`; (b) keep a glob reader under another name. (a) reads tracked
  files, the population the gates grade. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens:
  none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the round-1 spec audit's 54 MEDIUM and 19 LOW findings batched by
  report id.
- rev-2 · 2026-10-24 · §3 · Edges mirror those units 50, 54 and 55 declare against this unit.

## 10. Reuse audit

Each item extends the seam its finding names, cited in §2 and §4.
`python tools/codebase-map/reuse_lookup.py "one reader of a fact that two checks read twice"` ranked
`read`, `read_text` and `check` by name stem, no seam beyond those; the batch mints no reader a finding
did not ask for. The recall query returned TOOL-aDistilledCharter-7, TOOL-aGraftedHelix-32 and
TOOL-dSafePassage-35, precedent batches of a review's minors, whose per-id items this spec follows.

Recall terms used: `python tools/memory-recall/query.py "how were a round-one spec audit's medium and low findings batched into one unit" --terms "minors batch promoted MEDIUM LOW report id scope item round-1 spec audit disposition"`
