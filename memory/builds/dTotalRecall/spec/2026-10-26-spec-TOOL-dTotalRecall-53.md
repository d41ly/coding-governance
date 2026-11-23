# TOOL-dTotalRecall-53 — the round-1 spec audit of units 36 to 43: its 41 minors, batched

**Status:** INPROGRESS · rev-5 · 2026-11-23 · node d · Tier-2 · base 7b27f765 · streams tooling · order 29 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-53-deviation-531.md](../build/2026-10-26-build-TOOL-dTotalRecall-53-deviation-531.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-53-deviation-532.md](../build/2026-10-26-build-TOOL-dTotalRecall-53-deviation-532.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
| [2026-11-23-prompt-TOOL-dTotalRecall-53-build-brief.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-53-build-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-53-reground-brief.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-53-reground-brief.md) | journal | — |
| [2026-11-23-prompt-TOOL-dTotalRecall-53-reground-spec-writer.md](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-53-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
exited CONVERGED with 50 confirmed findings. Its nine highs, ids 1, 3, 22, 30, 31, 32, 35, 37 and 40,
are units 44 to 52. This unit is the batch BUILD-METHOD M4 makes of the rest: the 24 MEDIUM findings,
ids 2, 5, 6, 7, 8, 9, 13, 14, 15, 17, 18, 19, 23, 25, 27, 28, 36, 38, 41, 42, 45, 49, 50 and 51 (items M1
to M17), and the 17 LOW findings, ids 4, 10, 11, 12, 16, 20, 21, 24, 26, 29, 33, 34, 39, 43, 46, 47 and
52 (items L1 to L16). Each keeps its report id and its own scope item. The minors land on eight units,
so this unit repairs none in particular and builds after every unit (order 29, above the 28 that
`TOOL-dTotalRecall-52` holds). The review record holds each item's text.

Five minors report at a lower grade a defect a high unit closes: ids 13 and 23 (unit 44 and 45's), id 2
(unit 46's), id 42 (unit 47's), ids 15, 4 and 43 (unit 49's) and ids 51 and 12 (unit 52's). Each item
for them adds what the finding asks beyond that unit's mechanism, or re-observes that unit's fix at
this tip where the finding asks nothing more. The report's refuted ids 44 and 48 are not in the
disposal population.

Re-grounded at `7b27f765`. An item HEAD already satisfies keeps its criterion as a check and builds
nothing: S2, S6, S7, S8, S11, S13, S15, S17, S25, S26, S29 and S38, and the built halves of S12, S14,
S16 and S39. S18 does not apply. S20 and S32 ride with `TOOL-dTotalRecall-37` (§8 F3).

## 2. Scope (IN)

Each item states its change to the unit it lands on, as that unit was built; a landed spec is frozen
and is not edited.

- **S1** — id 13 (M1). `id_grammar.py --flip-probe` gains the case `i-named-reader`: it reverts
  `tools/memory-recall/check-recall.py#derive_probe_labels`'s re-point to `i.split("-")[1]` in the
  flipped clone and expects the census failure. The split predicate unit 44 keyed by shape,
  `tools/memory-tree/id_grammar.py#_READER_SPLIT_SHAPE`, reads no value name, so the case adds no
  predicate. Observed by AC1.
- **S2** — id 23 (M1). Holds at HEAD. The two family reads at index 0, now
  `tools/memory-tree/gen_build_index.py#cmd_asks` and `tools/memory-tree/backlog.py#render_family_view`,
  are outside the census by its shape (`(?!\[0\])`), and unit 45's trailer at `c6fcf603b` keeps them as
  the family at index 0, so census and record agree with no marker. `row_grammar.py#scan_records` is
  unit 45's re-point. Observed by AC2.
- **S3** — id 2 (M2). Era parity: each reader unit 38 re-pointed (its build commit `2f59e5acb`) and the
  three unit 45 re-pointed, `branch_reconcile.py#derive_names`, `row_grammar.py#scan_records` and
  `check_policy.py#derive_run_kind` (DERIVED 2026-11-23, `git show -s --format=%B c6fcf603b | grep -c
  "re-pointed onto parse_id_parts"`), answers for every flat-era and node-scoped id tracked under the
  memory root what it answered at base `462d20f3`; a reader that differs is fixed back. Observed by AC3.
- **S4** — id 42 (M3). `tools/memory-tree/record_causes.py#ABSENT_CAUSE`, the absent-cause finding's
  text, gains its remedy, `run record_causes.py --backfill`. The constant stays the one spelling
  `write_missing_causes` selects by, so the backfill's selection does not move. Observed by AC4.
- **S5** — id 15 (M4). The view `DESIGN_VIEW` names keeps its head across the build: its first three
  lines, through its `**Serves:**` line, are byte-identical to base `462d20f3`'s with no `Caused-by`
  line, and hygiene check 9's byte-drift arm is green at the tip. Its later lines move with each
  deviation record, as check 9's render demands (659 deviation records at base, 2364 at HEAD, DERIVED
  2026-11-23, the view's `Generated by` line). Observed by AC5.
- **S6** — id 51 (M5). Holds at HEAD by unit 52's key. `record-kinds-legacy` is keyed (`path`,
  `section`, `check`) with `drain = "key"` in `tools/govkit/registry.toml`, so a record legacy for both
  checks drains its `causes` row alone and keeps its `kind-schema` row, another key, and
  `tools/lib/legacy_ledger.py#compare_to_base` reads a shrink as no finding. This unit writes no byte of
  `legacy_ledger.py`. Observed by AC6.
- **S7** — id 5 (M6). Holds at HEAD: `tools/memory-tree/migrate_backlog.py#render_census` writes
  `**Caused-by:** <unit_id>` as line 2, after its Serves line. Observed by AC7.
- **S8** — id 14 (M6). Holds at HEAD: `tools/workflows/review_replay.py` is off the cause census as
  kept, its reason opening `reader-prefix:` (`record_causes.py#CAUSE_WRITER_KEPT`). S34 moves that
  reason onto the file's kept lines. Observed by AC8.
- **S9** — id 28 (M6). `record_causes.py#check_cause_writers` grades each Serves literal, not each file:
  a literal is answered by a `Caused-by` within the three lines below it, else by S34's marker on its
  line, so `gen_build_index.py`'s fixture bullets no longer clear its other literals.
  At HEAD 116 lines stand unanswered (DERIVED 2026-11-23, every `**Serves:** ` line of
  `record_kinds.read_code_paths`' population, test-named files excepted, its window probed), in the
  24 census files §4 lists (DERIVED 2026-11-23, the same probe). Each takes
  its cause where the file writes that record, else the marker with its reason. Observed by AC9.
- **S10** — id 41 (M6). `migrate_backlog.py#render_worksheet` writes `# **Caused-by:** <unit_id>` as
  line 2, after its `# **Serves:** log <unit_id>`, the comment form unit 51 reads. Observed by AC10.
- **S11** — id 6 (M7). Holds at HEAD: `record_causes.py#derive_record_cause` turns a
  `read_header_edges` refusal into that record's finding, `its header is refused`, naming both lines,
  and `check_causes` walks on. Observed by AC11.
- **S12** — id 45 (M7). `tools/playbook/edge_grammar.py#check_edge_cardinality` already counts no edge
  for a line `read_tree_edges` refuses and finishes, printing only how many it refused. It now prints
  each refused line, naming its record, so a typed record carrying two bulleted `- **Caused-by:**`
  fields is reported against its source. Observed by AC12.
- **S13** — id 7 (M8). Holds at HEAD, built by unit 42 (its §3): `unarmed` is legal on a `fields` or a
  `fence` row (`record_kinds.py#NEW_FORMS`), and the `stream-plan` row carries it. Observed by AC13.
- **S14** — id 17 (M8). Unit 42 built the rule, `unarmed` on any other form red naming the row
  (`record_kinds.py#check_record_kinds`); its plants `unarmed-reason`, `unarmed-with-record` and
  `unarmed-untyped` reach the other branches. The fixture gains `unarmed-on-disallowed-form`, a typed
  kind's row set to the `header` form and carrying the key. Observed by AC14.
- **S15** — id 8 (M9). Holds at HEAD: `TOOL-dTotalRecall-11` AC7 is re-observed at the tip, the
  `shape-run` row, marked unarmed by unit 42, passing `check_record_kinds`. Observed by AC15.
- **S16** — id 9 (M10). `id_grammar.py#scan_readers` already skips a marked line of any shape, and
  `run_flip_probe` reads the census through it (`TOOL-dTotalRecall-43` S14). What stays is the marking:
  HEAD's 34 split hits carry none (DERIVED 2026-11-23, the `--readers` lines `_READER_SPLIT_SHAPE`
  matches). Each split a `Decided:` trailer of units 38, 44 or 45 keeps carries S34's marker with the
  trailer's reason. A split no trailer keeps, such as `record_causes.py#derive_reached`'s, is
  re-pointed onto `parse_id_parts` where it reads a unit id's slug, else marked with its reason. The flip
  probe's census check then skips each marked line and fails on an unmarked plant. Observed by AC16.
- **S17** — id 18 (M11). Holds at HEAD: `tools/playbook/edge_grammar.py` is tracked, and its `--check`
  walk reaches `tree_lib.read_header_edges` through `edge_grammar.py#check_header_edges` (unit 39 S1).
  Observed by AC17.
- **S18** — id 38 (M11). Does not apply: it files an ask only where `edge_grammar.py` is untracked, and
  HEAD tracks it, so `memory/builds/dOrderedCharter/BACKLOG.md` gains no row. Observed by AC18.
- **S19** — id 19 (M12). `record_kinds.py#check_alias_compares` also lists a `KIND_ALIASES` key spelled
  as a word inside a regex literal or an unquoted `case` pattern, so the awk line
  `tools/memory-tree/check-memory-hygiene.sh@e623620c7:3654`, matching `(log|journal)`, is in reach and
  carries S34's marker. Observed by AC19.
- **S21** — id 27 (M14). Unit 42 built `record_kinds.py#derive_record_kind(path, text, rows)`, which
  parses the Serves line itself, and left this item here (its §3). It becomes
  `derive_record_kind(path, written_kind, rows)`: each caller passes the kind
  `tools/memory-tree/tree_lib.py#read_bindings` classified, read once, and `None` for a record whose
  binding state is not `bound`; no Serves line is parsed inside the function. Its three call sites move
  with it, `record_kinds.py#scan_legacy_records`, `tools/playbook/record_extract.py#derive_kind_row` and
  `record_extract.py#extract_record` (DERIVED 2026-11-23, `git grep -n "derive_record_kind("`).
  Observed by AC21.
- **S22** — id 36 (M15). The alias census reads `memory/builds/*/build/*.py` below each file's binding
  head; the pinned `deviations.py` `!= "journal"`
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py@30a1f15bf:380`) is
  kept by an `ALIAS_COMPARE_KEPT` row keyed by its repository path with the reason `pinned instrument`,
  never by a marker in its bytes, until `TOOL-dTotalRecall-56` moves that row to the path-keyed table.
  One ask row, filed through `gov_record.py new ask` in `memory/builds/dClosedLoop/BACKLOG.md`, asks its
  owner to compare through `tree_lib.resolve_kind` and repin. No other build-folder line is a hit at HEAD
  (DERIVED 2026-11-23, `git grep -nE "[\"']journal[\"']"` over the build folders' code). Observed by AC22.
- **S23** — id 49 (M16). The `homeless records` arm, `record_kinds.py#check_homeless_records`, selects
  only files carrying a Serves binding and selects none at HEAD (DERIVED 2026-11-23, its line reads
  `0 bound file(s)`). Its population becomes every tracked file under the memory root outside `builds/`
  (309 at HEAD, DERIVED 2026-11-23, `git ls-files memory` outside `memory/builds/`). Each is homed by a
  row, covered by a glob of the registry's `not-records` list (§8 F4), or red by path, and the arm prints
  the population count and reds an empty population. The list covers HEAD's 196 unhomed files
  (DERIVED 2026-11-23, that walk against every row's tracked-path globs): `memory/gotchas/`,
  `memory/guides/`, `memory/map/` and four root documents. Observed by AC23.
- **S24** — id 50 (M17). `tools/runlog/model.py#derive_path_key` folds the whole path's case on Windows,
  not the drive letter alone, and the memory-path match resolves a relative word against the command's
  cwd, so `./memory/x`, `../../memory/x` and a `/d/` path count. Its callers are `model.py`'s own two
  worktree-hold reads; `measure_legs.py` and `replay_scorer.py` define their own function of that name
  (DERIVED 2026-11-23, `git grep -n derive_path_key`). Observed by AC24.
- **S25** — id 4 (L1). Holds at HEAD: `TOOL-dTotalRecall-36` AC4's view half, `VIEW_HEAD.format` with
  every placeholder, shows no cause line, as unit 49 keeps it. Observed by AC25.
- **S26** — id 16 (L1). Holds at HEAD: the same AC's run-record half, `tools/runlog/record.py#render_markdown`
  writing the cause line as line 4 (unit 48). Observed by AC26.
- **S27** — id 10 (L2). `gen_build_index.py#render_order` writes one line under the table: a step's
  `Parallel yes` means its units share an order, and BUILD-METHOD M6 sequences two of them whose write
  sets intersect at dispatch. Observed by AC27.
- **S28** — id 11 (L3). The real-tree checks units 36, 39 and 42 changed are run at the tip and their
  output kept in this unit's acceptance ledger: `record_kinds.py --check`, `record_causes.py --check`
  and `edge_grammar.py --cardinality`. At HEAD `check_alias_compares` lists five red hits, which S34
  disposes. Observed by AC28.
- **S29** — id 12 (L4). Holds at HEAD: `record_causes.py --fixture` registers its ledger as
  `record-kinds-legacy`, keyed (`path`, `section`, `check`), home
  `memory/project/record-kinds-legacy.txt`, as unit 52 left the tree. Observed by AC29.
- **S30** — id 20 (L5). The `journal` population figure is derived, not stated: AC30's grep finds no
  bare figure at HEAD, and the pass keeps the tip's count in its acceptance ledger beside
  `TOOL-dTotalRecall-18`'s frozen 1,443, with its command, the `S` rows of
  `gen_build_index.py --print-bindings` whose kind cell is `journal` (5080 at HEAD, DERIVED 2026-11-23).
  Observed by AC30.
- **S31** — id 21 (L6). A class under `memory/gotchas/`: a cmd.exe `%VAR%` spelled in a bash command of
  a spec's criterion, which bash leaves literal; its anchors select spec paths. Observed by AC31.
- **S33** — id 26 (L8). `tools/runlog/memory_measure.py#check_memory_word` folds the word and the main
  worktree through `model.derive_path_key`, the kit's one fold, so the module spells no fold of its own;
  `memory_measure.py#derive_folded_path`, whose one caller is `check_memory_word`, goes with it.
  Observed by AC33.
- **S34** — id 29 (L9). One keep marker for the three code censuses, `<lead> census: kept <census>
  <reason>` on the kept line. The lead is `#` or `//`, as `id_grammar.py#READER_KEPT` admits today, so a
  JavaScript line carries it as a `//` comment. `<census>` is `slug-grammar`, `alias-compare` or
  `cause-writer`, the heads the censuses print. `id_grammar.py` holds its one reader,
  `read_kept_reason(line, census)`, which `scan_readers`, `check_alias_compares` and `check_cause_writers`
  call. The file-keyed constants `ALIAS_COMPARE_KEPT` and `CAUSE_WRITER_KEPT` give way to it for every
  file under the tool root, each such kept line marked with the reason the constant held, and a line
  kept for `KEPT_INSTRUMENT` keeps unit 49 S3's liveness check. A row naming a file under
  `memory/builds/*/build/` stays in its constant at this pass, because no pass may write that file's
  bytes: unit 50 §4's eight cause rows and S22's alias row. `TOOL-dTotalRecall-55` and
  `TOOL-dTotalRecall-56` move them to the path-keyed table, and each constant ends there. Observed by AC34.
  **Readers:** by name: READER NOT IN TREE — both constants are minted by `TOOL-dTotalRecall-40` and
  `TOOL-dTotalRecall-36` in this build and are absent at base · by value: `check_alias_compares` and
  `check_cause_writers` read the markers, and unit 49's legacy test reads the reason, after this item.
  **The alias hits at HEAD** (DERIVED 2026-11-23, a `python -c` call of `check_alias_compares`):
  - seven kept, of which two sit in `tools/govkit/shims.py`'s `JS_TEMPLATE`
    (`tools/govkit/shims.py@4aae24de2:164` and `:168`): a `#` there renders into JavaScript, so those
    two carry the `//` lead, a JavaScript comment in every forwarder the template renders;
  - five red: four lines of the `verb` blocks `shims.py --write` renders into `gen_build_index.py` from
    `PY_PRELUDE_BODY` (`shims.py@4aae24de2:212` and `:216`), marked in that template and re-rendered,
    never by hand; and `tools/govkit/steps/memory_journal_alias.py@2b4f436ae:64`, which counts the
    records still spelling the alias and is marked with that reason.
- **S35** — id 34 (L10). `python record_causes.py --cause-writers` prints `check_cause_writers`' lines
  alone, each census file and marked line with its disposition, so the table a spec quotes is derived.
  Observed by AC35.
- **S36** — id 33 (L11). The two record-head examples of `tools/memory-tree/BUILD-METHOD.template.md`
  (`tools/memory-tree/BUILD-METHOD.template.md@e11b530ac:140` and `:276`) name
  `**Caused-by:** <the first id, bare>` as the next line; the render reaches
  `memory/guides/BUILD-METHOD.md`, and `memory/guides/SESSION-KICKOFF.md`'s `last-audit` is re-stamped,
  its `watch:` naming that render and the other watched paths this pass edits. Observed by AC36.
- **S37** — id 39 (L12). `tools/memory-tree/shape_run.py#check_shape_runs` prints its unarmed line from
  the `shape-run` row's `unarmed` key, read through `record_kinds.read_record_kinds`. Today
  `shape_run.py#UNARMED` spells its own reason, `no writer calls the verb yet`, beside the row's, so the
  reason has two homes. Observed by AC37.
- **S38** — id 43 (L13). Holds at HEAD: the module docstring of `tools/memory-tree/asbuilt_view.py` and
  the kit README's `asbuilt_view` row are unchanged since base `462d20f3`. Observed by AC38.
- **S39** — id 46 (L14). Unit 40's operand predicate already lists no subscript key, so
  `model.py#build_run_model`'s producer key `journals["gates"]["journal"]` is not a hit. The census also
  lists an alias key assigned to a module constant: at HEAD `tree_lib.py#KIND_ALIASES` and
  `tools/runlog/record.py#SERVES_ALIASES` (DERIVED 2026-11-23, `git grep -nE "^[A-Z_][A-Z0-9_]* =
  .*[\"']journal[\"']"` over the tool root's code), each the alias's own table, marked with that reason.
  Observed by AC39.
- **S40** — id 47 (L15). `tools/memory-tree/gov_record.py#write_new_ask` already puts the file back as
  it was when its read-back fails (unit 41) and refuses with exit 2. It now writes by compare-and-swap:
  it re-reads the file just before writing through `legacy_ledger._write_atomic`, a temp file and
  `os.replace`, and exits 2 if the bytes moved since its parse; a failed read-back exits 3 naming the
  file. A refusal after the mint leaves the minted id unused, as the read-back refusal does today.
  Observed by AC40.
- **S41** — id 52 (L16). `record_kinds.py#GIT_OWN` states its class, git's own transient and optional
  entries, and adds `SQUASH_MSG`, `TAG_EDITMSG`, `NOTES_MERGE_*`, `fsmonitor--daemon*` and `gitk.cache`.
  Observed by AC41.

## 3. Non-goals (OUT)

- The nine highs: units 44 to 52.
- Editing any landed spec's text, frozen at CLOSED, as §2's opening states.
- The spec lints the report suggests as gates over the set; this unit records the one class that
  cannot be gated in code (S31) and leaves the rest to the close's left-shift step (BUILD-METHOD M8).
- S20 and S32 with AC20 and AC32: govkit's `linguist-generated` line for each `rendered` code row of
  a kit it installs, and the `[[lf_pin]]` row of `check_generated_attributes`. Both extend
  `TOOL-dTotalRecall-37`'s S1 and S2, unbuilt, so they ride with that unit under owner ask
  TOOL-dTotalRecall-109 (§8 F3), and so does closing TOOL-dScaffoldedMirror-20, whose acceptance names
  S32's arm.
- `tools/lib/legacy_ledger.py` and its inline copies: S6 holds by unit 52's key.

### Edges

- **consumes-from** `TOOL-dTotalRecall-1` — `record_kinds.py --check`, run at the tip
- **consumes-from** `TOOL-dTotalRecall-11` — `check_shape_runs` and the shape-run row's AC7
- **consumes-from** `TOOL-dTotalRecall-19` — `read_header_edges`, `check_causes` and its fixture
- **consumes-from** `TOOL-dTotalRecall-22` — `edge_grammar.py --cardinality`
- **consumes-from** `TOOL-dTotalRecall-36` — the writer census, `CAUSE_WRITER_KEPT` and its writers
- **consumes-from** `TOOL-dTotalRecall-38` — `--readers`, `--flip-probe` and the re-pointed readers
- **consumes-from** `TOOL-dTotalRecall-39` — the edge grammar's header binding
- **consumes-from** `TOOL-dTotalRecall-40` — `check_alias_compares` and `ALIAS_COMPARE_KEPT`
- **consumes-from** `TOOL-dTotalRecall-41` — the ask door's read-back
- **consumes-from** `TOOL-dTotalRecall-42` — `unarmed` and `derive_record_kind`
- **consumes-from** `TOOL-dTotalRecall-43` — the kept marker, the homeless arm, the path match and
  `GIT_OWN`
- **consumes-from** `TOOL-dTotalRecall-44` — the shape-keyed split census
- **consumes-from** `TOOL-dTotalRecall-45` — the three readers it re-pointed
- **consumes-from** `TOOL-dTotalRecall-46` — `parse_id_parts` on `build_id_token_re`
- **consumes-from** `TOOL-dTotalRecall-47` — `record_causes.py --backfill`
- **consumes-from** `TOOL-dTotalRecall-48` — the run record's head with its cause line
- **consumes-from** `TOOL-dTotalRecall-49` — the view's instrument bytes and its kept reason
- **consumes-from** `TOOL-dTotalRecall-50` — the widened census and `CAUSE_WRITER_PINNED`
- **consumes-from** `TOOL-dTotalRecall-51` — the comment-prefixed cause form
- **consumes-from** `TOOL-dTotalRecall-52` — the `record-kinds-legacy` registration keyed by `path`, `section` and `check`, home `memory/project/record-kinds-legacy.txt`
- **hands-off** `TOOL-dTotalRecall-55` — S34's retirement of `CAUSE_WRITER_KEPT` for the build-folder scripts, which S34 leaves in `CAUSE_WRITER_KEPT` and that unit keeps by a path-keyed row (the round-1 audit of units 44 to 53, id 37)
- **hands-off** `TOOL-dTotalRecall-56` — S22's keep of the pinned `deviations.py:380`, which S34 leaves in `ALIAS_COMPARE_KEPT` and that unit keeps by a path-keyed row (the round-1 audit of units 44 to 53, id 15)
- **hands-off** `TOOL-dTotalRecall-57` — AC34's retirement of the file-keyed constants, which that unit re-observes with the path-keyed rows bounded to the build folders (the round-1 audit of units 44 to 53, id 4)
- **hands-off** `TOOL-dTotalRecall-58` — S34's marker reader, which that unit bounds to the tool root, and the instruments' bytes it holds (the round-1 audit of units 44 to 53, id 24)
- **hands-off** `TOOL-dTotalRecall-60` — S5's view parity, S2 and S16's marker spelling, S27's order line, S30's figure and §1's count, which that unit settles (the round-1 audit of units 44 to 53, ids 3, 5, 9, 11, 14, 21, 27, 33, 34 and 35)
- **consumes-from** `TOOL-dTotalRecall-61` — S34, S22 and AC34 as that unit amends them in step 19, keeping each build-folder row in its constant through this pass (the round-1 audit of units 54 to 60, id 1)
- **hands-off** `TOOL-dTotalRecall-66` — S34's marker reader, whose domain that unit sets per census and tests against the derived tool root (the round-1 audit of units 54 to 60, ids 15, 28 and 43)

## 4. Design

### How the batch builds

One pass, after every unit is terminal. The items share `record_causes.py`, `record_kinds.py` and
`id_grammar.py`, so their write sets intersect and BUILD-METHOD M6 keeps them one unit. Within the
pass the order is: the census marker and its reader (S34) first, since S9, S16, S19, S22 and S39 write
or read it; then the code items in unit order; then the prose items S30, S31 and S36. A marker sits
only where its lead opens a comment in that line's language; a Serves literal inside text a writer
renders into a record takes its cause line instead.

### The legacy ledger, and unit 59

This unit writes no byte of `tools/lib/legacy_ledger.py` or of its inline copies under
`tools/memory-tree/` and `tools/gate-lint/`: S6 observes unit 52's key, and S40 calls memory-tree's
copy of `_write_atomic` unchanged. `TOOL-dTotalRecall-59` builds over HEAD's file. The two units still
share `memory/map/generated/`, so M6 sequences them at order 29, this unit first.

### Inventory

Minted: the flip case `i-named-reader`; the marker `<lead> census: kept <census> <reason>` and its
reader `read_kept_reason` in `id_grammar.py`; `--cause-writers` in `record_causes.py`; the registry list
`not-records` and its reader `read_not_record_globs` in `record_kinds.py`; the plants
`literal-without-cause`, `duplicate-cause` and `unmarked-writer` (causes), `unarmed-on-disallowed-form`,
`awk-regex-alias`, `alias-constant` and `homeless-empty` (record kinds), `cardinality-refused` (edges),
and `msys-d-drive`, `dot-relative` and `parent-relative` (runlog); one gotcha class; one ask row.
Naming cells: `read_kept_reason` and `read_not_record_globs` each open on the VERBS table's `read`; a
flag or plant name has no lexicon cell.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`, `tools/memory-tree/record_causes.py`, `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/record-kinds.toml`, `tools/memory-tree/migrate_backlog.py`, `tools/memory-tree/shape_run.py`
- `tools/memory-tree/gov_record.py`, `tools/memory-tree/tree_lib.py`, `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/row_grammar.py`, `tools/memory-tree/gov-claim.sh`
- `tools/memory-tree/build_records.py`, `tools/memory-tree/deviation_join.py`, `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/record_find.py`, `tools/memory-tree/ratchet.py`, `tools/memory-tree/seen_red.py`
- `tools/memory-tree/adopt-memory-tree.sh`, `tools/memory-tree/BUILD-METHOD.template.md`
- `tools/playbook/edge_grammar.py`, `tools/playbook/record_extract.py`, `tools/playbook/gov_tag.py`
- `tools/playbook/instruction_units.py`, `tools/policy/check_policy.py`, `tools/loop/placement.py`, `tools/loop/upstream.py`
- `tools/govkit/shims.py`, `tools/govkit/selftest.py`, `tools/govkit/steps/memory_journal_alias.py`
- `tools/runlog/model.py`, `tools/runlog/memory_measure.py`, `tools/runlog/record.py`, `tools/runlog/selftest.py`
- `tools/workflows/review_replay.py`, `tools/workflows/replay_scorer.py`
- `tools/workflows/tier2-review.template.js`, `tools/workflows/tier2-review.js`
- `tools/workflows/unattended-build.template.js`, `tools/workflows/unattended-build.js`
- `tools/memory-recall/selftest.py`, `skills/session-kickoff/manifest-check.sh`, `.githooks/pre-push.runlog.test.sh`
- `tools/run-gates/measure_legs.py`, `tools/run-gates/run-gates.sh`, `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.evidence.test.sh`, `tools/run-gates/run-gates.runlog.test.sh`
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`, `tools/unattended/lib-unattended.sh`
- `tools/unattended/pass-tree.sh`
- `memory/guides/BUILD-METHOD.md`, `memory/guides/SESSION-KICKOFF.md` (its `last-audit` re-stamped, S36)
- `memory/builds/dClosedLoop/BACKLOG.md` (S22's ask), `memory/gotchas/` (S31's class)
- `memory/builds/dTotalRecall/README.md` and each build README `gen_build_index.py --write` renders (S27)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

The marker sites are HEAD's (S9, S16, S34), each list re-derived at the pass base by the census that
reads it.

### Alternatives rejected

- **Fold each minor into its unit's spec.** M4 refuses folding at the exit.
- **Split into two batches.** S34's marker is read by the slug, alias and cause censuses, which sit in
  three of the item groups, so no two halves have disjoint write sets.
- **Keep the two `JS_TEMPLATE` lines in `ALIAS_COMPARE_KEPT`.** The constant would then hold a
  tool-root row S34 exists to end; the `//` lead `READER_KEPT` already reads keeps them in-line.

## 5. Production-readiness checklist

- security — S40 narrows the ask door's write to a compare-and-swap; no other surface.
- perf / scale — each census reads one more glob (S22) or a three-line window (S9); no new walk.
- error / empty / loading states — S23 reds an empty population; S12 prints each refusal it already
  collects; S40 names its two failure states.
- observability — S35 prints the census table; S4 names the remedy.
- risks — S9, S16 and S34 mark lines across the files §4 lists; a marker in `PY_PRELUDE_BODY`
  re-renders every forwarder `shims.py` writes.
- testing — AC1 to AC41 by the pass, AC20 and AC32 excepted (§3); the arms of §7 at the close.
- migration — S34's markers take the constants' tool-root rows one for one.
- user docs — none under `help/`: S36's guide is a governance carrier, not a help page.

## 6. Acceptance criteria

- **AC1** — When `python id_grammar.py --flip-probe <clone>` runs with `i-named-reader`, the hyphenated
  row prints the census failure naming `check-recall.py`. Red when: the reverted `i` reader passes.
- **AC2** — When `python id_grammar.py --readers` runs at the tip, it lists neither the index-0 read of
  `gen_build_index.py#cmd_asks` nor that of `backlog.py#render_family_view`. It holds at HEAD.
  Red when: an index-0 read is listed.
- **AC3** — When a `python -c` probe runs each re-pointed reader over every flat-era and node-scoped id
  `git grep -ohE` finds under `memory/`, at the tip and in a worktree at base, the answers are equal.
  Red when: a reader answers one of those ids differently from base.
- **AC4** — When `python record_causes.py --check` runs in the unit 19 fixture with a causeless record,
  its finding names `--backfill`, and `--backfill` there writes that record's cause.
  Red when: the finding names no remedy, or the backfill selects nothing.
- **AC5** — When `bash check-memory-hygiene.sh --only 9` runs at the tip, it exits 0, and `git diff
  462d20f3..HEAD` over `2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` touches none of its first three
  lines. Red when: the view's head moved.
- **AC6** — When a `python -c` probe writes a fixture home holding one record's `causes` and
  `kind-schema` rows, takes the `causes` row, and calls `legacy_ledger.read_ledger` and
  `compare_to_base`, the `kind-schema` row reads and no finding prints. It holds at HEAD.
  Red when: the drain takes both slices.
- **AC7** — When `render_census` from `migrate_backlog.py` renders a fixture, line 2 is
  `**Caused-by:** <unit_id>`. It holds at HEAD. Red when: the census record is written causeless.
- **AC8** — When `python record_causes.py --check` runs at the tip, it lists `review_replay.py` as kept
  with a reason opening `reader-prefix`. Red when: the file is red or unlisted.
- **AC9** — When `python record_causes.py --check` runs over the plant `literal-without-cause`, a file
  holding one Serves literal with a cause below it and one without, it lists the second literal's line. Red when: one cause spelling clears the file.
- **AC10** — When `render_worksheet` renders a fixture, line 2 is `# **Caused-by:** <unit_id>`, and
  `read_header_edges` reads it. Red when: the worksheet is written causeless or bare.
- **AC11** — When `python record_causes.py --check` walks a fixture with one record holding two bare
  `**Caused-by:**` lines and one causeless record, it reports both. It holds at HEAD.
  Red when: the refusal aborts the walk.
- **AC12** — When `python edge_grammar.py --cardinality` reads the plant `cardinality-refused`, a typed
  record with two bulleted `- **Caused-by:**` fields, it prints that record's refused line, counts no
  edge for it, and finishes. Red when: it counts one edge, or names no source.
- **AC13** — When `python record_kinds.py --check` runs at the tip, the `stream-plan` row passes with its
  `unarmed` key. Red when: the fence row reds on the key.
- **AC14** — When the record-kinds fixture plants `unarmed-on-disallowed-form`, `--check` exits 1 naming
  the row. Red when: the key passes on a form that is neither fields nor fence.
- **AC15** — When `check_record_kinds` from `record_kinds.py` runs at the tip, the `shape-run` row passes.
  Red when: unit 11's AC7 is red.
- **AC16** — When `python id_grammar.py --flip-probe <clone>` runs at the tip, the census check skips each
  marked split and fails on an unmarked plant, and `--readers` lists no line `_READER_SPLIT_SHAPE`
  matches. Red when: a marked hit fails the probe, or an unmarked split is listed.
- **AC17** — When a probe wraps `tree_lib.read_header_edges` with a counter and runs `edge_grammar.py
  --check` over a fixture record, the counter is above 0. It holds at HEAD.
  Red when: the header site reads edges itself.
- **AC18** — When `git ls-files tools/playbook/edge_grammar.py` runs at the pass base, it prints the
  path, so S18 files nothing. Red when: the module is untracked and no ask is filed.
- **AC19** — When `check_alias_compares` reads the plant `awk-regex-alias`, it lists that line, and at
  the tip it lists `check-memory-hygiene.sh`'s awk line as kept. Red when: a regex-form comparison passes.
- **AC21** — When `grep -n "def derive_record_kind" record_kinds.py` runs at the tip, the signature takes
  `written_kind`, and a probe passing a record `read_bindings` calls malformed gets `None`.
  Red when: the function parses Serves text.
- **AC22** — When `check_alias_compares` runs at the tip, it lists `deviations.py:380` as kept with
  `pinned instrument`, and `grep -c resolve_kind memory/builds/dClosedLoop/BACKLOG.md` prints at least 1.
  Red when: the census cannot see the instrument.
- **AC23** — When `python record_kinds.py --check` runs at the tip, the `homeless records` line prints a
  population above 0 and none homeless; the plant `homeless-record` names its file, and the plant
  `homeless-empty` reds. Red when: the arm selects nothing and passes.
- **AC24** — When `memory_measure.py`'s match reads the plants `msys-d-drive`, `dot-relative` and
  `parent-relative`, each counts. Red when: any of them counts zero.
- **AC25** — When a probe calls `VIEW_HEAD.format(serves="FIX-y-6", instrument="i", sha="s", count=0)`
  from `asbuilt_view.py`, the result holds no `Caused-by`. It holds at HEAD.
  Red when: the call raises or holds the line.
- **AC26** — When `render_markdown` from `record.py` renders a record serving `FIX-y-6`, line 4 is
  `**Caused-by:** FIX-y-6`. It holds at HEAD. Red when: the run record is written causeless.
- **AC27** — When `python gen_build_index.py --write` runs at the tip, the build README's `build-order`
  region carries S27's line. Red when: the region reads `Parallel yes` with no meaning stated.
- **AC28** — When `python record_kinds.py --check`, `python record_causes.py --check` and
  `python edge_grammar.py --cardinality` run at the tip, each exits 0, and their output is in the ledger.
  Red when: a changed check is red on the real tree.
- **AC29** — When `record_causes.py --fixture` builds a fixture, a `tomllib` probe of its kit file finds
  one ledger, `record-kinds-legacy`, its `fields` `path`, `section` and `check`. It holds at HEAD.
  Red when: the fixture registers `legacy-records` or a key without `check`.
- **AC30** — When `git grep -nE "[0-9],[0-9]{3} .journal" -- tools memory/guides memory/HYGIENE.md` runs
  at the tip, it prints nothing, and the ledger holds the tip's count beside its command.
  Red when: a bare figure ships.
- **AC31** — When `python gotchas.py --for-paths` runs at the tip over a spec path in this build's spec
  folder, it lists S31's class. Red when: a spec path does not select it.
- **AC33** — When `grep -c derive_path_key memory_measure.py` runs in the runlog kit at the tip, it prints
  at least 1, and `grep -c "def derive_folded_path" memory_measure.py` prints 0.
  Red when: a second fold exists.
- **AC34** — When a `python -c` probe reads `CAUSE_WRITER_KEPT` and `ALIAS_COMPARE_KEPT` at the tip, every row
  names a file under `memory/builds/*/build/`, and `git grep -c "census: kept"` over those files
  prints nothing; an unmarked writer added to a kept file under the tool root reds
  `record_causes.py --check`. Red when: a row naming a file under the tool root survives, or a
  build-folder file carries the marker.
- **AC35** — When `python record_causes.py --cause-writers` runs at the tip, every census file prints
  with a disposition. Red when: a file prints with none.
- **AC36** — When `grep -c "Caused-by" memory/guides/BUILD-METHOD.md` runs at the tip, it prints at least
  2, and `bash manifest-check.sh` exits 0. Red when: a head example lacks the line or the stamp is stale.
- **AC37** — When a probe calls `check_shape_runs` over a fixture with no shape-run record, its unarmed
  line ends with the `shape-run` row's `unarmed` value, and `git grep -c "no writer calls the verb yet"
  -- tools` prints nothing. Red when: the reason is spelled in two homes.
- **AC38** — When `git diff 462d20f3..HEAD -- tools/memory-tree/README.md` runs at the tip, the
  `asbuilt_view` row is unchanged. It holds at HEAD. Red when: the parity row moved.
- **AC39** — When `check_alias_compares` runs at the tip, it lists no line of `tools/runlog/model.py`,
  lists `KIND_ALIASES` and `SERVES_ALIASES` as kept, and lists the plant `alias-constant`.
  Red when: either reading is wrong.
- **AC40** — When the ask door files into a fixture `BACKLOG.md` that a planted writer appends to between
  parse and write, it exits 2 and the planted row stays; with a planted read-back failure it exits 3
  naming the file, the bytes as before. Red when: the appended row is lost or the exit is 2.
- **AC41** — When the pockets check runs with a planted `SQUASH_MSG` in a scratch clone's common dir, it
  names nothing. Red when: git's own state reds the leg.

## 7. Gates

`memory hygiene` · `build-index selftest` · `backlog migration selftest` · `row-grammar selftest` · `tier2-review self-test` · `review-replay selftest` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `kit/dogfood doc parity` · `build-method size` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `gotchas selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `drift-audit selftest` · `memory-recall kit selftest` · `policy fixtures` · `routed-commits selftest` · `scratch-guard self-test` · `branch-guard self-test` · `manifest-check self-test`

New arm: tools/memory-tree/record_causes.py · covers AC4 AC9 AC11 AC34 · the plants `literal-without-cause`, `duplicate-cause` and `unmarked-writer`, staged by restoring the file-keyed rule · none
New arm: tools/memory-tree/record_kinds.py · covers AC14 AC19 AC23 AC39 · the plants `unarmed-on-disallowed-form`, `awk-regex-alias`, `alias-constant` and `homeless-empty`, staged by the line-level quoted predicate and the bound-only population · none
New arm: tools/memory-tree/id_grammar.py · covers AC1 AC16 · the flip cases `i-named-reader` and an unmarked split, staged by skipping the marker read · none
New arm: tools/playbook/edge_grammar.py · covers AC12 · the plant `cardinality-refused`, staged by printing the refusal count alone · none
New arm: tools/runlog/selftest.py · covers AC24 · the three path plants, staged by the drive-only case fold · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of one unit's clause, which would split a clause that unit carries whole. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — May S36 change `BUILD-METHOD.template.md`, a governance carrier?** Options: (a) yes, under the
  grant `TOOL-dTotalRecall-36` §8 F2 used for the Record bindings section, the cause line being
  cl-dClosedLoop-0230's "each record's header (Serves, Made-by, Caused-by)", within `build-method size`'s
  ceiling; (b) no, leaving a hand-written review record copied from the guide causeless. (b) leaves the
  guide's own example red under the causes leg. RESOLVED (agent, 2026-10-26, delegated): (a), rung 5,
  the grant the README's `may:` line names. grants: PLAY-dClosedLoop-3 BUILD-METHOD.template.md's two
  record-head examples carry the cause line · widens: none · relaxes: none
- **F3 — Do S20 and S32 stay in scope while TOOL-dTotalRecall-37 is held unbuilt?** Unit 37 is DEFERRED
  to owner ask TOOL-dTotalRecall-109, so neither its `check_generated_attributes` arm nor the four
  renders' `linguist-generated` lines exist for S20 and S32 to extend. Options: (a) S20, S32, AC20 and
  AC32 ride with unit 37 under that ask, and this unit consumes nothing from it; (b) hold all of this
  unit, and every unit that consumes from it, until unit 37 builds. (b) parks the other items for two
  that extend an unbuilt arm. RESOLVED (agent, 2026-11-23, delegated): (a), M3, per
  `2026-11-23-prompt-TOOL-dTotalRecall-53-reground-brief` item 7. widens: none · relaxes: none
- **F4 — Where are S23's non-record globs declared?** HEAD declares none, so the widened arm would red
  every unhomed file. Options: (a) a top-level `not-records` list in
  `tools/memory-tree/record-kinds.toml`, each entry `{ glob, why }`, read beside the rows' homes;
  (b) a constant in `record_kinds.py`; (c) a `.memory-tree.conf` key. (b) declares half a partition in
  code and half in the registry (`[one-fact]`); (c) puts the kit's own partition among the adopter's
  values. RESOLVED (agent, 2026-11-23, delegated): (a), M3, the one option keeping a path's home and
  its non-home in one declared file; `2026-11-23-prompt-TOOL-dTotalRecall-53-reground-brief` item 4.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, its 41
  minors batched (24 MEDIUM, 17 LOW).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-55, TOOL-dTotalRecall-56, TOOL-dTotalRecall-57, TOOL-dTotalRecall-58, TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-61, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.
- rev-4 · 2026-11-23 · S34 S22 AC34 §3 §7 · amended by TOOL-dTotalRecall-61 (id 1, item H1) per
  `2026-11-22-prompt-TOOL-dTotalRecall-61-build-spec-writer`: each row naming a file under
  `memory/builds/*/build/` stays in `CAUSE_WRITER_KEPT` or `ALIAS_COMPARE_KEPT` through this pass, S22's
  row keyed by repository path, and units 55 and 56 end the constants; the hands-off lines to those
  units say so. §7's leg line gains `drift-audit selftest`, `memory-recall kit selftest` and
  `policy fixtures`, the guards `check-spec-tokens.py --spec` names for §4's `backlog.py` and
  `gen_build_index.py`.
- rev-5 · 2026-11-23 · §1 §2 S1-S19 S21-S41 §3 §4 §5 AC2 AC4-AC8 AC11 AC12 AC16-AC19 AC21-AC23 AC25
  AC26 AC28-AC30 AC33 AC37-AC40 §7 §8 F3 F4 §10 · re-grounded at base `7b27f765` per
  `2026-11-23-prompt-TOOL-dTotalRecall-53-reground-brief`: S2, S6, S7, S8, S11, S13, S15, S17, S25,
  S26, S29 and S38 hold at HEAD and keep their criteria as checks; S18 does not apply; S20, S32, AC20
  and AC32 ride with TOOL-dTotalRecall-37 (F3), which this unit no longer consumes from; the merged
  ledger is unit 52's `record-kinds-legacy`; S34's marker takes the `//` lead for `JS_TEMPLATE` and
  disposes HEAD's five red alias hits; S23 declares its non-records (F4); this unit writes no
  `legacy_ledger.py` (§4); §7's leg line gains the four legs the guard join names for §4's new paths;
  citations by symbol or blob.

## 10. Reuse audit

Each item extends the seam its finding names, cited in the item: unit 38's `--readers` and
`--flip-probe`, unit 36's census, unit 40's alias census, unit 42's `unarmed`, unit 43's marker
`tools/memory-tree/id_grammar.py#READER_KEPT`, arm and path match,
`tools/memory-tree/tree_lib.py#read_bindings`, `tools/runlog/model.py#derive_path_key`,
`tools/memory-tree/gen_build_index.py#render_order`, `tools/memory-tree/record_kinds.py#check_homeless_records`
and, for S40, the ledger factory's atomic write `tools/memory-tree/legacy_ledger.py#_write_atomic`. S34
is the one new mechanism, and it widens the marker unit 43 minted to the two file-keyed constants, so
the three censuses read one keep grammar. `python tools/codebase-map/reuse_lookup.py "insert a cause line into a
record head after its binding line"` ranked name-stem neighbours and no seam these items bypass.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
