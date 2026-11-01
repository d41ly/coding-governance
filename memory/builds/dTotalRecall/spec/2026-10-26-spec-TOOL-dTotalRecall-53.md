# TOOL-dTotalRecall-53 — the round-1 spec audit of units 36 to 43: its 41 minors, batched

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 29 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-53-deviation-531.md](../build/2026-10-26-build-TOOL-dTotalRecall-53-deviation-531.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-53-deviation-532.md](../build/2026-10-26-build-TOOL-dTotalRecall-53-deviation-532.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-crosscheck.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-40 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-59 TOOL-dTotalRecall-62 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-79 TOOL-dTotalRecall-81 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 |
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

## 2. Scope (IN)

Each item states its change to the unit it lands on, as that unit was built; a landed spec is frozen
and is not edited.

- **S1** — id 13 (M1). The flip probe's census check covers a reader whose value is named `i`:
  `id_grammar.py --flip-probe` gains the case `i-named-reader`, reverting `check-recall.py:511`'s
  re-point in the flipped clone and expecting the census failure. Observed by AC1.
- **S2** — id 23 (M1). The two family reads at index 0, `gen_build_index.py:3793` and `backlog.py:1683`,
  carry S16's kept marker with the reason `family index`, so the census and its record agree on
  them; `row_grammar.py:1116` is unit 45's. Observed by AC2.
- **S3** — id 2 (M2). Era parity: each reader units 38 and 45 re-pointed answers, for every flat-era and
  node-scoped id tracked under the memory root, what it answered at base; a reader that differs is
  fixed back to its base answer, so unit 38 §5's claim holds. Observed by AC3.
- **S4** — id 42 (M3). `check_causes`' finding for a causeless record written after the seed names its
  remedy, `record_causes.py --backfill`, so a pass landing before the writers' change is told the verb
  `TOOL-dTotalRecall-47` adds. Observed by AC4.
- **S5** — id 15 (M4). The view `DESIGN_VIEW` names keeps its bytes across the build: hygiene check 9's
  byte-drift arm is green at the tip with no README write rule naming the file. Observed by AC5.
- **S6** — id 51 (M5). The drain is per slice: when a record legacy for both checks gains its cause,
  `legacy_ledger.py`'s drain takes its `causes` row and leaves its `kind-schema` row. Observed by AC6.
- **S7** — id 5 (M6). `render_census` in `tools/memory-tree/migrate_backlog.py` (`:943-946`) writes
  `**Caused-by:** <unit_id>` on the line after its Serves line. Observed by AC7.
- **S8** — id 14 (M6). `tools/workflows/review_replay.py`, whose Serves literals are reader prefixes
  (`:65-66`) and fixtures (`:396`, `:449`), is kept off the cause census with the reason
  `reader prefix constant`, a reason the census admits from this item on. Observed by AC8.
- **S9** — id 28 (M6). The census grades each Serves literal, not each file: a literal is answered by a
  `Caused-by` spelled within the three lines below it, so `gen_build_index.py`'s fixture bullets
  (`:4718`, `:4934`, `:5022`) no longer take its other literals off the census. Observed by AC9.
- **S10** — id 41 (M6). `render_worksheet` (`migrate_backlog.py:934`) writes
  `# **Caused-by:** <unit_id>`, the comment form `TOOL-dTotalRecall-51` reads. Observed by AC10.
- **S11** — id 6 (M7). A refusal of `read_header_edges` is a per-record finding: `record_causes.py
  --check` collects it, names the record and both lines, and walks on. Observed by AC11.
- **S12** — id 45 (M7). `edge_grammar.py --cardinality` collects the same refusal per record, and a
  typed record carrying two bulleted `- **Caused-by:**` fields is reported against its source, never as
  one edge. Observed by AC12.
- **S13** — id 7 (M8). `unarmed` is legal on a `fields` and on a `fence` row, so the stream-plan row
  `TOOL-dTotalRecall-42` S3 marks passes `check_record_kinds`. Observed by AC13.
- **S14** — id 17 (M8). `unarmed` on any other form is red, naming the row: a plant makes the rule fail.
  Observed by AC14.
- **S15** — id 8 (M9). `TOOL-dTotalRecall-11` AC7 is re-observed at the tip: the `shape-run` row, narrowed
  and marked unarmed by unit 42, passes `check_record_kinds`. Observed by AC15.
- **S16** — id 9 (M10). `id_grammar.py --readers` and `--flip-probe` read the line marker
  `# slug-grammar: kept <reason>` (`TOOL-dTotalRecall-43` S14) for split hits too; each split kept in a
  `Decided:` trailer by units 38, 44 and 45 carries it, and the flip probe's census check skips a
  marked line. Observed by AC16.
- **S17** — id 18 (M11). Where `tools/playbook/edge_grammar.py` is tracked at this pass's base, its
  `--check` walk reaches `tree_lib.read_header_edges` for a record's header edges. Observed by AC17.
- **S18** — id 38 (M11). Where it is not, one ask row in `memory/builds/dOrderedCharter/BACKLOG.md` asks
  PLAY-dOrderedCharter-28's header site to bind `tree_lib.read_header_edges` and define none of its
  own. Observed by AC18.
- **S19** — id 19 (M12). The alias census `check_alias_compares` (`TOOL-dTotalRecall-40` S2) also lists a
  `KIND_ALIASES` key spelled as a word inside a regex literal or an unquoted `case` pattern, so
  `check-memory-hygiene.sh:3141`'s awk form is in its reach. Observed by AC19.
- **S20** — id 25 (M13). govkit writes a `linguist-generated` line for each `rendered` code row of a kit
  it installs into the adopter's attribute block, beside the `eol` lines `lf_pin_block`
  (`tools/govkit/govkit.py:5845`) writes. Observed by AC20.
- **S21** — id 27 (M14). `derive_record_kind(path, written_kind, rows)`: callers pass the kind
  `tree_lib.read_bindings` (`tools/memory-tree/tree_lib.py:471`) classified, read once, and no Serves
  line is parsed inside the function. Observed by AC21.
- **S22** — id 36 (M15). The alias census reads `memory/builds/*/build/*.py` below each file's binding
  head; the pinned `deviations.py` `!= "journal"` (`:380`) is kept with the reason `pinned instrument`,
  and one ask row in `memory/builds/dClosedLoop/BACKLOG.md` asks its owner to compare through
  `canonical_kind` and repin. Observed by AC22.
- **S23** — id 49 (M16). The `homeless records` arm (`TOOL-dTotalRecall-43` S1) selects every tracked
  file under the memory root outside `builds/` that no registry row homes and no declared non-record
  glob covers, prints its selected count, and reds an empty selection. Observed by AC23.
- **S24** — id 50 (M17). `derive_path_key` (`tools/runlog/model.py:282-293`) folds the whole path's case
  on Windows, and the memory-path match resolves a relative word against the command's cwd, so
  `./memory/x`, `../../memory/x` and a `/d/` path count. Observed by AC24.
- **S25** — id 4 (L1). `TOOL-dTotalRecall-36` AC4's view half, in its runnable spelling with every
  placeholder, shows no cause line, as unit 49 keeps it. Observed by AC25.
- **S26** — id 16 (L1). The same AC's run-record half is re-observed at the tip through unit 48's head.
  Observed by AC26.
- **S27** — id 10 (L2). `render_order` (`tools/memory-tree/gen_build_index.py:1715`) writes one line
  under the table: a step's `Parallel yes` means its units share an order, and BUILD-METHOD M6
  sequences two of them whose write sets intersect at dispatch. Observed by AC27.
- **S28** — id 11 (L3). The real-tree checks units 36, 39 and 42 changed are run at the tip and their
  output kept in this unit's acceptance ledger: `record_kinds.py --check`, `record_causes.py --check`
  and `edge_grammar.py --cardinality`. Observed by AC28.
- **S29** — id 12 (L4). `record_causes.py --fixture` registers its ledger under the merged name
  `record-kinds-legacy` with the `causes` slice, as unit 52 left the tree. Observed by AC29.
- **S30** — id 20 (L5). The `journal` population figure is derived, not stated: shipped prose naming
  that population cites the command that counts it, and the tip's count is kept in this unit's
  acceptance ledger beside `TOOL-dTotalRecall-18`'s frozen 1,443. Observed by AC30.
- **S31** — id 21 (L6). A class under `memory/gotchas/`: a cmd.exe `%VAR%` spelled in a bash command of
  a spec's criterion, which bash leaves literal; its anchors select spec paths. Observed by AC31.
- **S32** — id 24 (L7). `check_generated_attributes` (`TOOL-dTotalRecall-37` S2) gains its second row:
  each `[[lf_pin]]` pattern against `git check-attr eol`, through govkit's `resolve_tokens`.
  Observed by AC32.
- **S33** — id 26 (L8). `tools/runlog/memory_measure.py`'s path match calls `model.derive_path_key` on
  the word and on each worktree root, and spells no fold of its own. Observed by AC33.
- **S34** — id 29 (L9). One keep marker for the three code censuses, `# census: kept <census> <reason>`
  on the kept line: the slug census's marker is its `slug-grammar` census, and the file-keyed
  constants `ALIAS_COMPARE_KEPT` and `CAUSE_WRITER_KEPT` give way to it, each kept file's lines marked
  with the reason the constant held. Observed by AC34.
  **Readers:** by name: READER NOT IN TREE — both constants are minted by `TOOL-dTotalRecall-40` and
  `TOOL-dTotalRecall-36` in this build and are absent at base · by value: `check_alias_compares` and
  `check_cause_writers` read the markers, and unit 49's legacy test reads the reason, after this item.
- **S35** — id 34 (L10). `python record_causes.py --cause-writers` prints the census table, each file
  with its disposition, so the table a spec quotes is derived. Observed by AC35.
- **S36** — id 33 (L11). The two record-head examples of `tools/memory-tree/BUILD-METHOD.template.md`
  (`:140` and `:271`) name `**Caused-by:** <the first id, bare>` as line 2; the render reaches
  `memory/guides/BUILD-METHOD.md`, and `memory/guides/SESSION-KICKOFF.md`'s `last-audit` is re-stamped,
  its `watch:` naming that render. Observed by AC36.
- **S37** — id 39 (L12). `check_shape_runs` prints its unarmed line from the row's `unarmed` key, so the
  reason has one home. Observed by AC37.
- **S38** — id 43 (L13). The parity docstring (`asbuilt_view.py:14-18`) and the kit README's
  `asbuilt_view` row stay true: neither moves across the build. Observed by AC38.
- **S39** — id 46 (L14). The alias census compares only kind-bearing expressions, so
  `tools/runlog/model.py:1694`'s producer key is not a hit, and it lists an alias key assigned to a
  module constant, as `tools/runlog/record.py:82` was. Observed by AC39.
- **S40** — id 47 (L15). The ask door writes by compare-and-swap: it re-reads the file just before an
  atomic `os.replace` and exits 2 if the bytes moved since its parse; a failed after-write check
  restores the pre-read bytes and exits 3 naming the file. Observed by AC40.
- **S41** — id 52 (L16). `GIT_OWN` states its class, git's own transient and optional entries, and adds
  `SQUASH_MSG`, `TAG_EDITMSG`, `NOTES_MERGE_*`, `fsmonitor--daemon*` and `gitk.cache`. Observed by AC41.

## 3. Non-goals (OUT)

- The nine highs: units 44 to 52.
- Editing any landed spec's text, frozen at CLOSED, as §2's opening states.
- The spec lints the report suggests as gates over the set; this unit records the one class that
  cannot be gated in code (S31) and leaves the rest to the close's left-shift step (BUILD-METHOD M8).
- Closing TOOL-dScaffoldedMirror-20: S32 builds the arm its acceptance names, and its owner build
  disposes the ask.

### Edges

- **consumes-from** `TOOL-dTotalRecall-1` — `record_kinds.py --check`, run at the tip
- **consumes-from** `TOOL-dTotalRecall-11` — `check_shape_runs` and the shape-run row's AC7
- **consumes-from** `TOOL-dTotalRecall-19` — `read_header_edges`, `check_causes` and its fixture
- **consumes-from** `TOOL-dTotalRecall-22` — `edge_grammar.py --cardinality`
- **consumes-from** `TOOL-dTotalRecall-36` — the writer census, `CAUSE_WRITER_KEPT` and its writers
- **consumes-from** `TOOL-dTotalRecall-37` — `check_generated_attributes`
- **consumes-from** `TOOL-dTotalRecall-38` — `--readers`, `--flip-probe` and the re-pointed readers
- **consumes-from** `TOOL-dTotalRecall-39` — the edge grammar's header binding
- **consumes-from** `TOOL-dTotalRecall-40` — `check_alias_compares` and `ALIAS_COMPARE_KEPT`
- **consumes-from** `TOOL-dTotalRecall-41` — the ask door's read-back
- **consumes-from** `TOOL-dTotalRecall-42` — `unarmed` and `derive_record_kind`
- **consumes-from** `TOOL-dTotalRecall-43` — the kept marker, the homeless arm, the path match,
  `GIT_OWN` and the merged ledger
- **consumes-from** `TOOL-dTotalRecall-44` — the shape-keyed split census
- **consumes-from** `TOOL-dTotalRecall-45` — the three further re-pointed readers
- **consumes-from** `TOOL-dTotalRecall-46` — `parse_id_parts` on `build_id_token_re`
- **consumes-from** `TOOL-dTotalRecall-47` — `record_causes.py --backfill`
- **consumes-from** `TOOL-dTotalRecall-48` — the run record's head with its cause line
- **consumes-from** `TOOL-dTotalRecall-49` — the view's instrument bytes and its kept reason
- **consumes-from** `TOOL-dTotalRecall-50` — the widened census and `CAUSE_WRITER_PINNED`
- **consumes-from** `TOOL-dTotalRecall-51` — the comment-prefixed cause form
- **consumes-from** `TOOL-dTotalRecall-52` — the triple-keyed `record-kinds-legacy` registration
- **hands-off** `TOOL-dTotalRecall-55` — S34's retirement of `CAUSE_WRITER_KEPT` for the build-folder scripts, which S34 does not mark and that unit keeps by a path-keyed row (the round-1 audit of units 44 to 53, id 37)
- **hands-off** `TOOL-dTotalRecall-56` — S22's keep of the pinned `deviations.py:380`, which S34 does not mark and that unit keeps by a path-keyed row (the round-1 audit of units 44 to 53, id 15)
- **hands-off** `TOOL-dTotalRecall-57` — AC34's retirement of the file-keyed constants, which that unit re-observes with the path-keyed rows bounded to the build folders (the round-1 audit of units 44 to 53, id 4)
- **hands-off** `TOOL-dTotalRecall-58` — S34's marker reader, which that unit bounds to the tool root, and the instruments' bytes it holds (the round-1 audit of units 44 to 53, id 24)
- **hands-off** `TOOL-dTotalRecall-60` — S5's view parity, S2 and S16's marker spelling, S20's govkit block, S27's order line, S30's figure and §1's count, which that unit settles (the round-1 audit of units 44 to 53, ids 3, 5, 9, 11, 14, 21, 27, 33, 34 and 35)
- **consumes-from** `TOOL-dTotalRecall-61` — S34, S22 and AC34 as that unit amends them in step 19, keeping each build-folder row in its constant through this pass (the round-1 audit of units 54 to 60, id 1)
- **hands-off** `TOOL-dTotalRecall-66` — S34's marker reader, whose domain that unit sets per census and tests against the derived tool root (the round-1 audit of units 54 to 60, ids 15, 28 and 43)

## 4. Design

### How the batch builds

One pass, after every unit is terminal. The items share `record_causes.py`, `record_kinds.py` and
`id_grammar.py`, so their write sets intersect and BUILD-METHOD M6 keeps them one unit. Within the
pass the order is: the census marker (S34) first, since S2, S8, S16, S22 and S39 write or read it;
then code items in unit order; then the prose items S30, S31 and S36.

### Inventory

Minted: the flip case `i-named-reader`; the census reason `reader prefix constant`; the marker
`# census: kept <census> <reason>`; `--cause-writers` in `record_causes.py`; the alias plants
`awk-regex-alias` and `alias-constant`; the record-kinds plant `unarmed-on-disallowed-form`; the path
plants `msys-d-drive`, `dot-relative` and `parent-relative`; one gotcha class; two ask rows. Naming
cells: no new function is minted; a flag or plant name has no lexicon cell.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`, `tools/memory-tree/gen_build_index.py`, `tools/memory-tree/backlog.py`
- `tools/memory-tree/record_causes.py`, `tools/memory-tree/migrate_backlog.py`, `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_kinds.py`, `tools/memory-tree/record-kinds.toml`, `tools/memory-tree/shape_run.py`
- `tools/memory-tree/record_extract.py`, `tools/memory-tree/gov_record.py`, `tools/lib/legacy_ledger.py`
- `tools/memory-tree/BUILD-METHOD.template.md`, `memory/guides/BUILD-METHOD.md`, `memory/guides/SESSION-KICKOFF.md`
- `tools/playbook/edge_grammar.py`, `tools/govkit/govkit.py`, `tools/workflows/review_replay.py`
- `tools/runlog/model.py`, `tools/runlog/memory_measure.py`
- `memory/builds/dClosedLoop/BACKLOG.md`, `memory/builds/dOrderedCharter/BACKLOG.md` (S18, only where it applies)
- `memory/gotchas/` (S31's class)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Fold each minor into its unit's spec.** M4 refuses folding at the exit.
- **Split into two batches.** S34's marker is read by the slug, alias and cause censuses, which sit in
  three of the item groups, so no two halves have disjoint write sets.

## 5. Production-readiness checklist

- security — S40 narrows the ask door's write to a compare-and-swap; S20 adds attribute lines to a
  block govkit already writes; no other surface.
- perf / scale — each census reads one more glob (S22) or line window (S9); no new walk.
- error / empty / loading states — S23 reds an empty selection; S11 and S12 collect refusals instead
  of aborting a walk; S40 names its two failure states.
- observability — S35 prints the census table; S4 names the remedy.
- risks — S34 rewrites two constants as markers in one pass; S2 and S16 read the same marker.
- testing — AC1 to AC41 by the pass; the arms of §7 at the close.
- migration — S34's markers replace the constants' rows one for one.
- user docs — none under `help/`: S36's guide is a governance carrier, not a help page.

## 6. Acceptance criteria

- **AC1** — When `python id_grammar.py --flip-probe <clone>` runs with `i-named-reader`, the hyphenated
  row prints the census failure naming `check-recall.py`. Red when: the reverted `i` reader passes.
- **AC2** — When `python id_grammar.py --readers` runs at the tip, it lists neither `gen_build_index.py:3793`
  nor `backlog.py:1683`, and each carries the marker. Red when: an index-0 read is listed or unmarked.
- **AC3** — When a `python -c` probe runs each re-pointed reader over every flat-era and node-scoped id
  `git grep -ohE` finds under `memory/`, at the tip and in a worktree at base, the answers are equal.
  Red when: a reader answers one of those ids differently from base.
- **AC4** — When `python record_causes.py --check` runs in the unit 19 fixture with a causeless record,
  its finding names `--backfill`. Red when: the finding names no remedy.
- **AC5** — When `bash check-memory-hygiene.sh --only 9` runs at the tip, it exits 0, and `git diff
  462d20f3..HEAD` over `2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` is empty. Red when: the view's
  bytes moved.
- **AC6** — When `legacy_ledger.py`'s drain runs over a fixture record legacy for both checks that has
  gained its cause, its `kind-schema` row stays. Red when: the drain takes both slices.
- **AC7** — When `render_census` from `migrate_backlog.py` renders a fixture, line 2 is
  `**Caused-by:** <unit_id>`. Red when: the census record is written causeless.
- **AC8** — When `python record_causes.py --check` runs at the tip, it lists `review_replay.py` as kept
  with `reader prefix constant`. Red when: the file is red or unlisted.
- **AC9** — When `python record_causes.py --check` runs over the plant `literal-without-cause`, a file
  holding one Serves literal with a cause below it and one without, it lists the second literal's line. Red when: one cause spelling clears the file.
- **AC10** — When `render_worksheet` renders a fixture, line 2 is `# **Caused-by:** <unit_id>`, and
  `read_header_edges` reads it. Red when: the worksheet is written causeless or bare.
- **AC11** — When `python record_causes.py --check` walks a fixture with one record holding two bare
  `**Caused-by:**` lines and one causeless record, it reports both. Red when: the refusal aborts the walk.
- **AC12** — When `python edge_grammar.py --cardinality` reads a typed fixture record with two bulleted
  `- **Caused-by:**` fields, it reports that source, and the walk finishes. Red when: it counts one edge.
- **AC13** — When `python record_kinds.py --check` runs at the tip, the `stream-plan` row passes with its
  `unarmed` key. Red when: the fence row reds on the key.
- **AC14** — When the record-kinds fixture plants `unarmed-on-disallowed-form`, `--check` exits 1 naming
  the row. Red when: the key passes on a form that is neither fields nor fence.
- **AC15** — When `check_record_kinds` from `record_kinds.py` runs at the tip, the `shape-run` row passes.
  Red when: unit 11's AC7 is red.
- **AC16** — When `python id_grammar.py --flip-probe <clone>` runs at the tip, the census check skips each
  marked split and fails on an unmarked plant. Red when: a marked hit fails the probe.
- **AC17** — When a probe wraps `tree_lib.read_header_edges` with a counter and runs `edge_grammar.py
  --check` over a fixture record, the counter is above 0. Red when: the header site reads edges itself.
  fixture: only where `edge_grammar.py` is tracked; S18 holds otherwise.
- **AC18** — When `git ls-files tools/playbook` lists no `edge_grammar.py` at the pass base,
  `grep -c read_header_edges memory/builds/dOrderedCharter/BACKLOG.md` prints 1 at the tip.
  Red when: the module is absent and no ask is filed.
- **AC19** — When `check_alias_compares` reads the plant `awk-regex-alias`, it lists that line.
  Red when: a regex-form comparison passes.
- **AC20** — When `python govkit.py` installs the workflows kit into a scratch adopter, its
  `.gitattributes` names each of the four renders `linguist-generated`. Red when: an adopter gets none.
  fixture: a scratch adopter repository, made by the pass under the short temp path a clone needs.
- **AC21** — When `grep -n "def derive_record_kind" record_kinds.py` runs at the tip, the signature takes
  `written_kind`, and a fixture record `read_bindings` calls malformed returns `None`.
  Red when: the function parses Serves text.
- **AC22** — When `check_alias_compares` runs at the tip, it lists `deviations.py:380` as kept with
  `pinned instrument`, and `grep -c canonical_kind memory/builds/dClosedLoop/BACKLOG.md` prints at
  least 1. Red when: the census cannot see the instrument.
- **AC23** — When `python record_kinds.py --check` runs at the tip, the `homeless records` arm prints a
  selected count above 0; with a planted untracked-home file it names that file. Red when: it selects nothing.
- **AC24** — When `memory_measure.py`'s match reads the plants `msys-d-drive`, `dot-relative` and
  `parent-relative`, each counts. Red when: any of them counts zero.
- **AC25** — When a probe calls `VIEW_HEAD.format(serves="FIX-y-6", instrument="i", sha="s", count=0)`
  from `asbuilt_view.py`, the result holds no `Caused-by`. Red when: the call raises or holds the line.
- **AC26** — When `render_markdown` from `record.py` renders a record serving `FIX-y-6`, line 4 is
  `**Caused-by:** FIX-y-6`. Red when: the run record is written causeless.
- **AC27** — When `python gen_build_index.py --write` runs at the tip, the build README's `build-order`
  region carries S27's line. Red when: the region reads `Parallel yes` with no meaning stated.
- **AC28** — When `python record_kinds.py --check`, `python record_causes.py --check` and
  `python edge_grammar.py --cardinality` run at the tip, each exits 0, and their output is in the ledger.
  Red when: a changed check is red on the real tree.
- **AC29** — When `record_causes.py --fixture` builds a fixture, a `tomllib` probe of its kit file finds
  one ledger, `record-kinds-legacy`. Red when: the fixture registers `legacy-records`.
- **AC30** — When `git grep -nE "[0-9],[0-9]{3} .journal" -- tools memory/guides memory/HYGIENE.md` runs
  at the tip, each hit sits beside its counting command. Red when: a bare figure ships.
- **AC31** — When `python gotchas.py --for-paths` runs at the tip over a spec path in this build's spec
  folder, it lists S31's class. Red when: a spec path does not select it.
- **AC32** — When `govkit.py selfcheck` runs over a scratch copy whose `.gitattributes` drops one
  `[[lf_pin]]` line, it names that pattern. Red when: an `eol` gap passes.
- **AC33** — When `grep -c derive_path_key memory_measure.py` runs in the runlog kit at the tip, it prints
  at least 1, and the file spells no `/c/` fold. Red when: a second fold exists.
- **AC34** — When `git grep -nE "ALIAS_COMPARE_KEPT|CAUSE_WRITER_KEPT" -- tools` runs at the tip, it
  prints nothing, and an unmarked writer added to a kept file reds `record_causes.py --check`.
  Red when: a file-keyed exemption remains.
- **AC35** — When `python record_causes.py --cause-writers` runs at the tip, every census file prints
  with a disposition. Red when: a file prints with none.
- **AC36** — When `grep -c "Caused-by" memory/guides/BUILD-METHOD.md` runs at the tip, it prints at least
  2, and `bash manifest-check.sh` exits 0. Red when: a head example lacks the line or the stamp is stale.
- **AC37** — When `git grep -n "no writer calls gov_record.py new shape-run" -- tools` runs at the tip, it
  prints the registry row only. Red when: the reason is spelled in two homes.
- **AC38** — When `git diff 462d20f3..HEAD -- tools/memory-tree/README.md` runs at the tip, the
  `asbuilt_view` row is unchanged. Red when: the parity row moved.
- **AC39** — When `check_alias_compares` runs at the tip, it does not list `model.py:1694`, and the
  plant `alias-constant` is listed. Red when: either reading is wrong.
- **AC40** — When the ask door files into a fixture `BACKLOG.md` that a planted writer appends to between
  parse and write, it exits 2 and the planted row stays. Red when: the appended row is lost.
- **AC41** — When the pockets check runs with a planted `SQUASH_MSG` in a scratch clone's common dir, it
  names nothing. Red when: git's own state reds the leg.

## 7. Gates

`memory hygiene` · `build-index selftest` · `backlog migration selftest` · `row-grammar selftest` · `tier2-review self-test` · `review-replay selftest` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `kit/dogfood doc parity` · `build-method size` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `gotchas selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/record_causes.py · covers AC4 AC9 AC11 AC34 · the plants `literal-without-cause`, `duplicate-cause` and `unmarked-writer`, staged by restoring the file-keyed rule · none
New arm: tools/memory-tree/record_kinds.py · covers AC14 AC19 AC39 · the plants `unarmed-on-disallowed-form`, `awk-regex-alias` and `alias-constant`, staged by the line-level quoted predicate · none
New arm: tools/memory-tree/id_grammar.py · covers AC1 AC16 · the flip cases `i-named-reader` and an unmarked split, staged by skipping the marker read · none
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

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, its 41
  minors batched (24 MEDIUM, 17 LOW).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-55, TOOL-dTotalRecall-56, TOOL-dTotalRecall-57, TOOL-dTotalRecall-58, TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-61, TOOL-dTotalRecall-66, each the other end of an edge a unit the round-1 spec audit of units 54 to 60 promoted wrote; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names, cited in the item: unit 38's `--readers` and
`--flip-probe`, unit 36's census, unit 40's alias census, unit 42's `unarmed`, unit 43's marker, arm and
path match, `tree_lib.read_bindings` (`:471`), `model.derive_path_key` (`tools/runlog/model.py:282`),
govkit's `lf_pin_block` (`:5845`) and `render_order` (`gen_build_index.py:1715`). S34 is the one new
mechanism, and it replaces two file-keyed constants with the marker unit 43 minted, so the three
censuses read one keep grammar. `python tools/codebase-map/reuse_lookup.py "insert a cause line into a
record head after its binding line"` ranked name-stem neighbours and no seam these items bypass.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
