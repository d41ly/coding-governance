# TOOL-dLinkedLibrary-52 — the code half of the round-1 audit's minors: 53 findings closed where the built code holds them

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 27 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |
| [2026-10-26-build-TOOL-dLinkedLibrary-52-deviation-521.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-52-deviation-521.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
50 MEDIUM and 14 LOW findings. BUILD-METHOD M4 batches them; they split into two disjoint write sets by
M6 (§4 "Why two units"), so this unit takes the 53 that change built code, a kit file, a generated map
artifact or the decision log, and `TOOL-dLinkedLibrary-53` takes the 11 that touch none of these.

This unit's findings, each its own scope item, by report id: MEDIUM 5, 24, 6, 7, 9, 40, 63, 11, 14, 15,
21, 60, 23, 25, 28, 31, 32, 33, 34, 37, 39, 44, 74, 45, 46, 47, 48, 52, 53, 55, 62, 61, 68, 69, 70, 71,
72, 73, 75, 78, 79, 80; LOW 17, 18, 19, 29, 41, 36, 38, 42, 54, 66, 81. Each item names its id and the
report item it shares (R16 to R71). It lands after every unit (order 27): its items land on many units,
so it repairs none in particular.

## 2. Scope (IN)

Where an item corrects what a unit's criterion asserts, that unit's acceptance ledger answers the
criterion AMENDED, naming this unit and the item.

- **S1** — id 5, R16. `adopt_program.py --fixture --plant split` (`TOOL-dLinkedLibrary-8` AC3) rates 20
  candidates: 18 agreed (5 `major`, 5 `minor`, 4 `waiver`, 4 `process-rule`) and 2 split, (`major`,
  `minor`) and (`waiver`, `process-rule`); p_o 0.9, p_e 0.25. Observed by AC1.
- **S2** — id 24, R16. The plant pins `kappa 0.867 over 20 rows · pass`, both split rows settle `split`
  with `Major` `no`, `--ratify` lists none under `author-rubric` and the 5 major and 2 split under
  `docs-owner-ratifies`. Observed by AC1.
- **S3** — id 38, R66. `decision_rubric.py` exports `read_labels(path)` and `derive_settled_rows(rows_a, rows_b,
  split_major=True)`, the reader and settler `agree` and `route` use; `adopt decisions --rate` calls both
  with `split_major=False`, holding no labels parser of its own. Observed by AC1.
- **S4** — id 6, R17. `derive_decision_rows` (`tools/memory-tree/row_grammar.py`, `TOOL-dLinkedLibrary-22`
  S6) takes a row whose current text no commit added from the first commit adding its id,
  `git log --reverse -m -S'<id> ·'` over the log and its archives; TOOL-aMendedLedger-8, -9 and
  TOOL-aFoldedQuarry-9 are that population at base. Observed by AC2.
- **S5** — id 19, R63. A row's segment is `· decides=<target>[,<target>]` at the row's end, the one lead
  `derive_decision_rows` parses; `TOOL-dLinkedLibrary-1`'s pointer row carries it in that form. Observed by
  AC2.
- **S6** — id 32, R31. One producer of a `Decided:` trailer's `decides` edge: the trailer half of
  `derive_decision_rows` reads PLAY-dOrderedCharter-28 S5's `read_trailer_edges`; one ask row in
  `memory/builds/dOrderedCharter/BACKLOG.md` asks that adapter to read through
  `commit_trailers.decided`. Observed by AC3.
- **S7** — id 34, R33. The decision log's rule (`memory/DECISIONS.md:6`) holds: the rows
  `TOOL-dLinkedLibrary-25` S3 moved and the ids its S4 re-keyed return to their bytes and positions at
  base `5fede642`; each misfiled row and each duplicated id is recorded by an appended note (I26), and
  `ROW_DUPLICATE_PIN` reads its base value, so the log's diff against base is additive. Observed by AC4.
- **S8** — id 28, R29. Check 27 over this unit's commit carrying S7 reports no unsatisfied near match for
  the five ids S4 of unit 25 re-keyed; the lines are recorded in this unit's ledger. Observed by AC4.
- **S9** — id 7, R18. `tools/memory-tree/ANNOTATION-STYLE.template.md` and its render
  `memory/guides/ANNOTATION-STYLE.md` name, in A1, the `annotations` leg's resolve arm and its
  `annotation-resolve-legacy` population where `TOOL-dLinkedLibrary-25` S7 named the drift signal unit 11
  takes out of the tree. Observed by AC5.
- **S10** — id 9, R19. `adopt_instructions.py` writes and parses the paragraph ruling `drop`, the value
  `TOOL-dLinkedLibrary-8` §4 closes the set with, in place of `discard`.
  **Readers:** by name: READER NOT IN TREE, since `discard` is spelled only by `TOOL-dLinkedLibrary-23`'s
  module and help page, which land with that unit · by value: the door's `Ruling` field check, `--rule`'s
  parser and `help/adopting-instructions.md`'s option list, each reading the value. Observed by AC6.
- **S11** — id 40, R19. The `ruling` kind's row holds `TOOL-dLinkedLibrary-8`'s values alone; where
  unit 23's pass wrote three values again, they are cut from the row.
  **Readers:** by name: READER NOT IN TREE, the row lands with TOOL-dTotalRecall-1's registry · by value:
  NO VALUE READERS — the door's field check that reads the row lands with TOOL-dTotalRecall-1, absent at HEAD. Observed by AC6.
- **S12** — id 63, R19. `core.py adopt instructions --rule <key> drop` passes the door's field check and
  writes its `ruling` record.
  **Readers:** by name: READER NOT IN TREE, as S10 · by value: `gov_record.py new ruling`'s field check.
  Observed by AC6.
- **S13** — id 21, R26. A harness file carrying the `gov:playbook` marker pair, or byte-equal to the
  charter at any revision of its history, is stale wiring: the capture re-wires it and holds no pair for
  it. Observed by AC7.
- **S14** — id 60, R26. A captured body holding a line `is_marker_line` reads as a registered region
  marker is refused, naming the file and line; the `stale-copy` plant keeps `--check-render` green.
  Observed by AC7.
- **S15** — id 62, R47. The capture reads tracked regular files, and symlinks resolving inside the
  repository; an ignored or untracked harness file is refused naming it, and a dangling symlink is named
  and left for S2's refusal. Observed by AC7.
- **S16** — id 61, R48. A repeated paragraph's key carries an ordinal, `<src>#p<hash>.<n>`, so each
  occurrence is ruled; a plant of two identical `---` paragraphs under `refuse` drains to zero. Observed by
  AC8.
- **S17** — id 36, R65. The paragraph key is `<src>#p` + `derive_pin_hash(text)`
  (`tools/memory-tree/design_lib.py`, PLAY-dOrderedCharter-24 S7), read through `resolve_kit_dir`.
  Observed by AC8.
- **S18** — id 11, R20. `reuse_entries.py --fixture --plant convention-part` tracks
  `memory/map/conventions/x.reuse.toml` in a scratch clone; hygiene check 3 names it without
  `D:conventions` and is silent with it. Observed by AC9.
- **S19** — id 14, R23. `annotations.py`'s selftest composes each planted word at run time,
  `"gov:" + "planted-word"`, so no tracked file spells it and the census sees none. Observed by AC10.
- **S20** — id 15, R24. Where `TOOL-dLinkedLibrary-17`'s deviation record 171 exists, the `ARMS` table
  holds no `span` entry and `check` prints `annotations: span: not built — hybrid loses`. Observed by
  AC10.
- **S21** — id 31, R30. `check_resolve` takes its defined set from `corpus_ids.walk(...)['defs']` as
  `gotchas.load_defined_ids` does (`tools/memory-tree/gotchas.py:162`), and honours the `missing:`
  citation form; `derive_defined_ids` is deleted with its one caller re-pointed.
  **Readers:** by name: READER NOT IN TREE, the function lands with `TOOL-dLinkedLibrary-4` · by value:
  `check_resolve`'s verdicts and the legacy population `TOOL-dLinkedLibrary-11` seeds from them.
  Observed by AC11.
- **S22** — id 68, R49. The citation cut: a `memory/` path loses trailing punctuation and a
  `:<line>[,<line>]` tail; a token holding `*`, `<` or `{` is not a citation; a directory resolves when
  `git ls-files <dir>/` lists anything. Observed by AC11.
- **S23** — id 69, R50. With no compare base, `resolve_compare_base` answering `(None, why)`, the budget
  and `required` print `annotations: budget: unarmed — <why>` and exit 0, never a green count. Observed by
  AC12.
- **S24** — id 70, R51. `derive_block_anchor` keys a block by its first line that is not a banner, a
  comment line of one repeated punctuation character, so a banner block inserted above shifts no key.
  Observed by AC12.
- **S25** — id 23, R27. The holds-now view's `<build>` cell links only where
  `memory/builds/<slug>/README.md` is tracked, else prints the bare slug. Observed by AC13.
- **S26** — id 52, R43. `LIBRARY_VIEWS` moves to the catalogue key `memory.library-views`, read through
  `read_policy_value`; gov's `.governance/policy.toml` sets it, and `.memory-tree.conf` and its example
  hold no `LIBRARY_VIEWS` line.
  **Readers:** by name: `.memory-tree.conf` · by value: `library_views.py`'s switch and the
  `gen_build_index.py` calls `TOOL-dLinkedLibrary-6` S3 adds, re-pointed. Observed by AC13.
- **S27** — id 53, R44. `GOTCHA_FIELDS` moves to the catalogue key `gotchas.fields`, read through
  `read_policy_value`; `.memory-tree.conf` and its example hold no `GOTCHA_FIELDS` line.
  **Readers:** by name: `.memory-tree.conf` · by value: `gotchas.py`'s required-field check and
  `memory/HYGIENE.md`'s sentence, re-pointed. Observed by AC14.
- **S28** — id 17, R61. `GOTCHA_KEYS` in `gotchas.py` is the admitted set, `gotchas.fields` its required
  subset; `TOOL-dLinkedLibrary-24`'s `gate:`, `planted:`, `shape:` and `observed:` join `GOTCHA_KEYS`.
  Observed by AC14.
- **S29** — id 18, R62. `parse_front_matter`'s `kind: note` refusal names `kind: class` alone. Observed
  by AC14.
- **S30** — id 25, R28. The leg-named classes are a derived population: `gotchas.py --report` prints
  `leg-named classes — <n>: <stems>`, the classes whose prose holds a backticked leg name of
  `LEG_MANIFEST` in a sentence matching `gated by|in|at`; each carries `gate:` or reads `partly-gated`.
  Observed by AC15.
- **S31** — id 33, R32. One class-to-leg fact read twice and compared: a class whose `gate:` names a leg
  whose `tests` (TOOL-dWitnessedBar-22) lacks `class.<name>`, and a `class.<name>` in a leg's `tests`
  whose record's `gate:` names another leg, each red; one ask row in `memory/builds/dWitnessedBar/BACKLOG.md`
  proposes recording `observed:` as a seen-red record (TOOL-dWitnessedBar-7). Observed by AC15.
- **S32** — id 37, R35. The legs units 7, 9, 10 and 23 wrote into `tools/gate-legs.json` are declared
  through `leg_factory.py new` in `tools/memory-tree/kit.toml`, `tools/hooks/kit.toml` and
  `tools/playbook/kit.toml`; `leg_factory.py --check` exits 0. Observed by AC16.
- **S33** — id 45, R39. `TOOL-dLinkedLibrary-9`'s two legs carry chunk, subject and ceiling, and rows in
  `tools/govkit/subject-pins.tsv`, `tools/run-gates/selftest-budgets.txt`,
  `tools/run-gates/ceiling-evidence.txt`, `tools/run-gates/foreign-prefix.gov.test.sh`
  (`WHOLE_RUN`) and the claiming dossier. Observed by AC16.
- **S34** — id 46, R40. `TOOL-dLinkedLibrary-10`'s `retrofit progress selftest` leg: argv `python
  {prefix}/memory-tree/retrofit_progress.py --selftest`, its chunk, subject, guard and ceiling, and S33's
  meta rows. Observed by AC16.
- **S35** — id 47, R41. `TOOL-dLinkedLibrary-23`'s `adopt instructions selftest` leg, declared in
  `tools/playbook/kit.toml`, with S33's meta rows and the playbook dossier's claim. Observed by AC16.
- **S36** — id 48, R42. `TOOL-dLinkedLibrary-7`'s `annotations selftest` and `annotations-read
  self-test` legs gain `WHOLE_RUN` rows; the map's generated artifacts are re-rendered. Observed by AC16.
- **S37** — id 55, R45. `tools/codebase-map/gen_map.py:121` (render `memory/map/README.md:30`) and
  `tools/codebase-map/INVENTORY-DERIVATION.md:67`, :105 point at the moved prose record and the reuse
  entries in place of `## Shared seams` prose. Observed by AC17.
- **S38** — id 80, R59. `gen_map.py --write` renders `memory/map/README.md` only where its bytes equal a
  past render of `_README`; otherwise it prints `README.md is authored — not rendered` and leaves it.
  Observed by AC17.
- **S39** — id 66, R70. `dossier_move.py apply` writes one dossier's proposals and record, then shrinks
  it; a re-run skips a seam whose proposal exists, keyed `<feature>.<n>`. Observed by AC18.
- **S40** — id 44, R38. The rows of `memory/project/encoding-posture-sites.txt` for `rank_harness.py`
  and `replay-phrases.py` (:20-21) are drained in the deletion's commit. Observed by AC19.
- **S41** — id 74, R38. `tools/codebase-map/kit.toml`'s two `[[files]]` rows (:48, :57) and the arms of
  `tools/codebase-map/selftest.py` (:1905, :2129, :2535, :2577) that load the three deleted files are
  deleted.
  **Readers:** by name: `tools/codebase-map/kit.toml`, `tools/codebase-map/selftest.py` · by value: govkit's
  install walk over `[[files]]` and the selftest's arm count. Observed by AC19.
- **S42** — id 29, R64. `house_index.py` reads the legs through `gotchas.load_leg_names`, loaded by
  `resolve_kit_dir("memory-tree", "gotchas.py", here)`; it holds no manifest reader of its own.
  Observed by AC20.
- **S43** — id 41, R64. The scout role's body is measured as `check_roles.py` measures it; this unit's
  ledger records the figure against the 1536-byte ceiling. Observed by AC20.
- **S44** — id 54, R68. `HOUSE_INDEX_DIRS` and `HOUSE_INDEX_KINDS` move to catalogue keys
  `reuse.house-index-dirs` and `reuse.house-index-kinds`; one ask row in
  `memory/builds/aScoutedSeam/BACKLOG.md` names them; `memory/map/features/review-harnesses.md` claims
  `reuse-bench.js` in `workflow-scripts`.
  **Readers:** by name: READER NOT IN TREE, both keys land with `TOOL-dLinkedLibrary-2` · by value:
  `house_index.py`'s directory and kind lists. Observed by AC20.
- **S45** — id 81, R71. The `matched` slot keeps only lines matching the scout's `## Matches` grammar,
  at most 2 KiB then `… <n> more`; a malformed section renders `not searched — the Matches section is
  malformed`. Observed by AC20.
- **S46** — id 71, R52. `grep_words` returns `({}, None)` without calling git when the stripped word list
  is empty, in every copy under its parity row; `gov_code.py where ""` exits 2. Observed by AC21.
- **S47** — id 72, R53. `show <bare name>` resolving to no key, with an extractor-`none` language listed or
  the record degraded, prints the floor's line and `where`'s hits. Observed by AC21.
- **S48** — id 39, R36. `derive_source_purpose` reads a non-Python header from
  `extract_comment_spans`, the span ending at `line - 1`. Observed by AC22.
- **S49** — id 79, R58. `extract_ctags_defs` writes each blob as `<blob>/<original basename>`, and a file
  ctags names no language for is listed under extractor `none`. Observed by AC22.
- **S50** — id 73, R54. The read hook takes at most 50 tracked files from a directory, nearest first,
  passes paths to the launcher on stdin, reads a pathless Grep as its working directory, and appends to
  the pushed list only the paths it emitted. Observed by AC23.
- **S51** — id 42, R67. One definition of a shell read, `derive_read_paths(command)` in
  `tools/runlog/extract.py` over `_derive_program` and `_derive_segment` (:479, :506); the code replay's
  `measure_read_files` and the hook's `annotations.py lookup --command` call it, the latter printing
  `shell reads — runlog not installed` where it is absent. Observed by AC23.
- **S52** — id 78, R57. `splice_region` raises `RegionError` naming the body line when a body line is a
  marker line for the call's marks, labelled or not, in every `region_py` copy. Observed by AC24.
- **S53** — id 75, R55. `drained` is derived per key after `carry_renames` maps period-start keys to
  their keys now. Observed by AC25.

## 3. Non-goals (OUT)

- The 11 minors that touch no code, kit file, map artifact or decision log: `TOOL-dLinkedLibrary-53`'s.
- The report's left-shift gates: each is a checker change outside this build's clauses.
- Rewriting a closed spec's prose: each item lands in code, a kit file, a record or a ledger answer.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-8` — `adopt_program.py` and its `split` plant, which S1 to S3 resize and re-point (ids 5, 24, 38)
- **consumes-from** `TOOL-dLinkedLibrary-1` — `decision_rubric.py` and its pointer row, which S3 exports from and S5 re-spells (ids 38, 19)
- **consumes-from** `TOOL-dLinkedLibrary-22` — `derive_decision_rows`, which S4 to S6 complete (ids 6, 19, 32)
- **consumes-from** `TOOL-dLinkedLibrary-25` — the S3 and S4 edits of `memory/DECISIONS.md`, the guide sentence and the `kind: note` refusal, which S7 to S9 and S29 restore or re-point (ids 7, 18, 28, 34)
- **consumes-from** `TOOL-dLinkedLibrary-11` — the deleted drift signal and `derive_block_anchor`, which S9 and S23 to S24 follow (ids 7, 69, 70)
- **consumes-from** `TOOL-dLinkedLibrary-23` — `adopt_instructions.py`, its capture, its paragraph key and its leg, which S10 to S17 and S35 harden (ids 9, 40, 63, 21, 60, 62, 61, 36, 47)
- **consumes-from** `TOOL-dLinkedLibrary-12` — `annotations.py`'s selftest plants, which S19 composes at run time (id 14)
- **consumes-from** `TOOL-dLinkedLibrary-17` — deviation record 171's route, which S20 reads (id 15)
- **consumes-from** `TOOL-dLinkedLibrary-4` — `check_resolve` and `derive_defined_ids`, which S21 and S22 re-point (ids 31, 68)
- **consumes-from** `TOOL-dLinkedLibrary-44` — `scan_comment_lines`, the population S22's citation cut reads (id 68)
- **consumes-from** `TOOL-dLinkedLibrary-5` — the holds-now view's `<build>` cell, which S25 corrects (id 23)
- **consumes-from** `TOOL-dLinkedLibrary-6` — `LIBRARY_VIEWS`, which S26 moves to the catalogue (id 52)
- **consumes-from** `TOOL-dLinkedLibrary-24` — `GOTCHA_KEYS`, `gate:` and `--observe`, which S28, S30 and S31 settle (ids 17, 25, 33)
- **consumes-from** `TOOL-dLinkedLibrary-7` — the legs and the read hook, which S32, S36 and S50 complete (ids 37, 48, 73)
- **consumes-from** `TOOL-dLinkedLibrary-9` — the two `record origin` legs, which S32 and S33 declare (ids 37, 45)
- **consumes-from** `TOOL-dLinkedLibrary-10` — the `retrofit progress selftest` leg and `drained`, which S34 and S53 define (ids 46, 75)
- **consumes-from** `TOOL-dLinkedLibrary-19` — the dossier move's readers and `apply`, which S37 and S39 complete (ids 55, 66)
- **consumes-from** `TOOL-dLinkedLibrary-38` — the `<feature>.<n>` proposal names S39 keys its re-run on (id 66)
- **consumes-from** `TOOL-dLinkedLibrary-50` — `apply`'s `--build` and `--unit`, under which S39's re-run writes (id 66)
- **consumes-from** `TOOL-dLinkedLibrary-3` — the deletion of the three harness files, whose readers S40 and S41 drain (ids 44, 74)
- **consumes-from** `TOOL-dLinkedLibrary-2` — `house_index.py`, its conf keys and its slot, which S42 to S45 re-point (ids 29, 41, 54, 81)
- **consumes-from** `TOOL-dLinkedLibrary-14` — `grep_words` and `show`, which S46 and S47 guard (ids 71, 72)
- **consumes-from** `TOOL-dLinkedLibrary-15` — `derive_source_purpose`, which S48 re-points (id 39)
- **consumes-from** `TOOL-dLinkedLibrary-21` — `extract_ctags_defs`, whose temp names S49 fixes (id 79)
- **consumes-from** `TOOL-dLinkedLibrary-16` — `measure_read_files`, which S51 re-points (id 42)
- **consumes-from** `TOOL-dLinkedLibrary-18` — `splice_region` and its copies, which S52 guards (id 78)
- **consumes-from** external — the asks S6, S31 and S44 file in dOrderedCharter, dWitnessedBar and aScoutedSeam
- **hands-off** `TOOL-dLinkedLibrary-59` — S7's restoration and AC4, which unit 59's `log-diff` measures relative to unit 1's rotation (id 1 of the spec audit of units 37 to 53)
- **hands-off** `TOOL-dLinkedLibrary-64` — S39's re-run, S33 to S36's legs, S41's deletion, S44's key move and S52's `splice_region`, which unit 64 completes (ids 7, 9, 14, 19, 23, 33 of the spec audit of units 37 to 53)

## 4. Design

### Why two units

M6 admits two units only over disjoint write sets. Every item here writes a kit file, which moves that
kit's version constant, or the map's generated artifacts, or `memory/DECISIONS.md`; any two such items
share a path, so they are one unit. `TOOL-dLinkedLibrary-53`'s eleven items write none of those: its
paths are `.gitattributes`, `tools/dead-path-waivers.txt`, `WIRE-INTO-PROJECT.md`, one spec's §7 line, the
template high-water row and its own ledger, none of which this unit writes, and neither reads the other's
output.

### Evidence

- S1: with the four planted rows of unit 8 AC3, p_o 0.5 and p_e 0.25 give kappa 0.333, under the 0.8
  floor; S1's twenty give (0.9 − 0.25) / 0.75 = 0.867.
- S7: `memory/DECISIONS.md:6` reads "the file is never re-sorted and a landed row is never edited";
  `ROW_DUPLICATE_PIN="3"` at `.memory-tree.conf:693`.
- S37: `tools/codebase-map/gen_map.py:121` and `tools/codebase-map/INVENTORY-DERIVATION.md:67`, :105 tell
  authors to write `## Shared seams` prose.
- S40, S41: `memory/project/encoding-posture-sites.txt:20-21`, `tools/codebase-map/kit.toml:48`, :57.
- S51: `_derive_program` (`tools/runlog/extract.py:479`) and `_derive_segment` (:506).

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`, `tools/memory-tree/decision_rubric.py`: S1 to S3
- `tools/memory-tree/row_grammar.py`, `memory/DECISIONS.md`, `.memory-tree.conf`: S4 to S8, S26, S27
- `tools/memory-tree/ANNOTATION-STYLE.template.md`, `memory/guides/ANNOTATION-STYLE.md`: S9
- `tools/playbook/adopt_instructions.py`, `tools/memory-tree/record-kinds.toml`, `help/adopting-instructions.md`: S10 to S17
- `tools/memory-tree/reuse_entries.py`: S18
- `tools/memory-tree/annotations.py`: S19 to S24, S51's `--command`
- `tools/memory-tree/library_views.py`, `tools/memory-tree/gen_build_index.py`: S25, S26
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`, `.governance/policy.toml`, `.governance/policy.json`, `tools/memory-tree/.memory-tree.conf.example`: S26, S27, S44
- `tools/memory-tree/gotchas.py`, `tools/memory-tree/HYGIENE.template.md`, `memory/HYGIENE.md`, `memory/gotchas/INDEX.md`: S27 to S31
- `tools/run-gates/leg_factory.py`'s declarations in `tools/memory-tree/kit.toml`, `tools/hooks/kit.toml`, `tools/playbook/kit.toml`; `tools/gate-legs.json`: S32 to S36
- `tools/govkit/subject-pins.tsv`, `tools/run-gates/selftest-budgets.txt`, `tools/run-gates/ceiling-evidence.txt`, `tools/run-gates/foreign-prefix.gov.test.sh`: S33 to S36
- `tools/codebase-map/gen_map.py`, `tools/codebase-map/INVENTORY-DERIVATION.md`, `memory/map/README.md`: S37, S38
- `tools/codebase-map/dossier_move.py`, `tools/codebase-map/house_index.py`: S39, S42 to S45
- `memory/project/encoding-posture-sites.txt`, `tools/codebase-map/kit.toml`, `tools/codebase-map/selftest.py`: S40, S41
- `memory/map/features/memory-tree-hygiene.md`, `memory/map/features/review-harnesses.md`, `memory/map/generated/MAP.md`, `memory/map/generated/inventories.json`, `memory/map/generated/symbols.json`: S33 to S36, S44, regenerated
- `tools/memory-tree/gov_code.py`, `tools/drift-audit/drift_report.py` (the `grep_words` copy): S46, S47
- `tools/memory-tree/code_enrich.py`, `tools/memory-tree/code_ctags.py`: S48, S49
- `tools/hooks/annotations-read.js`, `tools/runlog/extract.py`, `tools/workflows/replay_scorer.py`: S50, S51
- `tools/lib/region.py` and every `region_py` copy `TOOL-dLinkedLibrary-18` S6 placed: S52
- `tools/memory-tree/retrofit_progress.py`: S53
- `memory/builds/dOrderedCharter/BACKLOG.md`, `memory/builds/dWitnessedBar/BACKLOG.md`, `memory/builds/aScoutedSeam/BACKLOG.md`: one ask row each
- the kit version constants of memory-tree, playbook, codebase-map, drift-audit, hooks, runlog and workflows, with their markers

### Alternatives rejected

- **One unit per report item.** M4 forbids it.
- **Folding each item into its unit's spec.** The owner's 2026-10-05 ruling (TOOL-aEvidencedLens-17)
  promotes every minor and folds none.

## 5. Production-readiness checklist

- security — S13 to S15 narrow what install captures; S45 caps agent text copied into a prompt; S52
  refuses a write that would leave an unreadable pair.
- perf / scale — S50 bounds the hook's argv; the rest change no complexity.
- error / empty / loading states — S23, S20 and S45 print a named line where an arm cannot run.
- observability — each refusal names its file, line or row.
- risks — S7 reverts bytes unit 25 moved; its AC compares the log to base, row by row.
- testing — AC1 to AC25 by fixture, plant and probe.
- migration — S7's restoration and S26, S27 and S44's key moves, each in its own commit.
- user docs — S9's guide, S10's help page, `memory/HYGIENE.md` for S27 and S31.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant split` runs, it prints
  `kappa 0.867 over 20 rows · pass`, both split rows read `split` and `Major` `no`, the `--ratify` listings match S2, and
  `grep -n "def read_labels\|def derive_settled_rows" decision_rubric.py` in `tools/memory-tree` prints both.
  Red when: the plant cannot reach the floor, or the router parses labels itself.
- **AC2** — When `python row_grammar.py --decisions` runs at this pass's tip, it prints
  `0 with no decides target`, the three edited rows each with a commit, and a planted row ending `· decides=feature.roles`
  yields that target.
  Red when: an edited row has no target, or a segment with another lead is read.
- **AC3** — When `grep -c "read_trailer_edges" row_grammar.py` runs in `tools/memory-tree`, it prints 1 or
  more, and the dOrderedCharter backlog holds the ask row.
  Red when: the trailer half keeps its own parse.
- **AC4** — When `git diff 5fede642 -- memory/DECISIONS.md` runs at this pass's tip, every changed line is
  an added line, `grep -n "^ROW_DUPLICATE_PIN" .memory-tree.conf` prints `3`, and the ledger records check
  27's lines for the five ids.
  Red when: a landed row is moved or edited relative to base.
- **AC5** — When `grep -n "annotation-resolve-legacy" memory/guides/ANNOTATION-STYLE.md` runs, it prints
  A1, and `grep -c "source_cited_ids_resolving_to_no_record" memory/guides/ANNOTATION-STYLE.md` prints 0.
  Red when: the guide names a deleted signal.
- **AC6** — When `python adopt_instructions.py --fixture --plant rule-drop` runs `--rule <key> drop`, it
  writes a `ruling` record; `--rule <key> discard` exits 2.
  Red when: the two spellings both pass, or `drop` is refused.
- **AC7** — When `--plant stale-copy`, `--plant ignored-file` and `--plant marker-body` run, the stale copy
  is re-wired with no pair, the ignored `.cursorrules` is refused by name, a body holding a region marker
  is refused naming its line, and `--check-render` stays green on the first.
  Red when: a stale copy or an untracked file is captured, or a marker-bearing body is written.
- **AC8** — When `--plant repeat-under-refuse` rules both `---` paragraphs, the pair drains to zero; each
  key ends with `derive_pin_hash`'s eight hex and an ordinal on the repeat.
  Red when: a repeated paragraph cannot be ruled.
- **AC9** — When `python reuse_entries.py --fixture --plant convention-part` runs, check 3 names the
  part with `D:conventions` absent and is silent with it.
  Red when: the staged probe cannot fail.
- **AC10** — When `git grep -n "gov:planted-word" -- tools` runs, it prints nothing; with record 171 planted
  in a scratch clone, `python annotations.py check` prints `span: not built — hybrid loses`.
  Red when: a tracked file spells a plant word, or the leg's arm set is undefined on `lose`.
- **AC11** — When `python annotations.py --fixture --plant citation-shapes` runs `check --only resolve`,
  a glob, a `<placeholder>`, a `:12` tail, a trailing period and a tracked directory each yield no finding,
  and an id defined only as a backlog row resolves.
  Red when: an ordinary citation shape reds, or the defined set differs from `corpus_ids`'.
- **AC12** — When `--plant no-remote` runs the budget arm in a repository with no remote, it prints
  `budget: unarmed —` and exits 0; `--plant banner-insert` adds a `# ----` block above and the rows keep
  their keys.
  Red when: a missing base grades every block or none silently, or a banner moves a key.
- **AC13** — When `python library_views.py --fixture --plant no-readme` renders, the slug cell is bare;
  `python policy.py get memory.library-views` prints gov's value, and
  `grep -c "LIBRARY_VIEWS" .memory-tree.conf` prints 0.
  Red when: a dead link renders, or the key stays in the conf.
- **AC14** — When `python policy.py get gotchas.fields` prints gov's value,
  `grep -c "GOTCHA_FIELDS" .memory-tree.conf` prints 0, `python -c` prints `GOTCHA_KEYS` holding `gate`, and a `kind: note` record
  is refused naming `kind: class` alone.
  Red when: a required field sits outside the admitted set, or the remedy names a retired prose arm.
- **AC15** — When `python gotchas.py --report` runs, it prints the `leg-named classes` line, every class it
  names carries `gate:` or reads `partly-gated`, and a planted class whose `gate:` leg's `tests` omits it
  reds `--check`.
  Red when: the population is not derived, or the two spellings disagree silently.
- **AC16** — When `python leg_factory.py --check` runs in `tools/run-gates`, it exits 0, and for each leg
  of S33 to S36 `grep -c "<leg>" tools/govkit/subject-pins.tsv tools/run-gates/selftest-budgets.txt tools/run-gates/foreign-prefix.gov.test.sh`
  prints 1 or more per file.
  Red when: a leg is hand-written or owes a meta row.
- **AC17** — When `grep -n "Shared seams" tools/codebase-map/gen_map.py tools/codebase-map/INVENTORY-DERIVATION.md`
  runs, it prints no instruction to write that prose; an edited map README survives `gen_map.py --write`
  with the `authored` line.
  Red when: an instruction to write refused prose remains, or authored bytes are overwritten.
- **AC18** — When `python dossier_move.py --fixture --plant fail-third` fails the stub on its third
  `propose` and `apply` runs again, no proposal is filed twice.
  Red when: a re-run after a partial failure duplicates a proposal.
- **AC19** — When
  `grep -c "rank_harness\|replay-phrases" memory/project/encoding-posture-sites.txt tools/codebase-map/kit.toml` runs at this pass's tip, it prints 0 for each.
  Red when: a reader of a deleted file remains.
- **AC20** — When `grep -c "LEG_MANIFEST" house_index.py` runs in `tools/codebase-map`, it prints 0;
  `python house_index.py --slot` over a 9 KiB `## Matches` section prints at most 2 KiB and `… <n> more`;
  and `python policy.py get reuse.house-index-dirs` prints a value.
  Red when: the index re-reads the manifest, copies agent text uncapped, or keeps conf keys.
- **AC21** — When `python gov_code.py where ""` runs, it exits 2; `show Run` over the `x.go` plant prints
  the floor's line and `where`'s hits.
  Red when: an empty word matches every line, or a bare name answers a false `none`.
- **AC22** — When `python code_enrich.py --fixture` reads a `#` line inside a heredoc above a function, it
  is no purpose; the ctags plant's `Makefile` rule is listed or its file is listed under `none`.
  Red when: a string reads as a header, or an extensionless file degrades silently.
- **AC23** — When the hook's fixture pipes a pathless Grep payload over a 200-file tree, the launcher call
  carries at most 50 paths on stdin and the pushed list holds only the emitted paths; `python -c` calls
  `derive_read_paths("git show HEAD:a.py")` and gets `a.py`.
  Red when: argv grows with the tree, or the two counters read reads two ways.
- **AC24** — When `splice_region` is called with a body holding the open marker line, it raises naming
  the body line, in the canonical and in each copy the parity discovery finds.
  Red when: a body can write its own marker.
- **AC25** — When `python retrofit_progress.py --fixture --plant rename` renames a file holding three rows,
  `drained` reads 0.
  Red when: a rename reads as a drain.

## 7. Gates

`policy check` · `policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `foreign-prefix parity (every self-test at three prefixes)` · `every held leg is budgeted, every budget row resolves` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `encoding posture (text IO names its encoding)` · `drift-audit selftest` · `playbook render selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `marker contracts` · `gotchas selftest` · `kit/dogfood doc parity` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `agent-cap self-test` · `format-guard self-test` · `hook destinations self-test` · `pre-push run-log line` · `review-join self-test` · `run-gates run-log line` · `runlog selftest` · `scratch-guard self-test` · `straggler-guard arms` · `tier2-review self-test` · `transition-audit arms` · `unattended-build self-test` · `verifier fan-out self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/annotations.py · covers AC10 AC11 AC12 · the `citation-shapes`, `no-remote` and `banner-insert` plants, the failing case staged by the rev-1 cut and ordinal key · none
New arm: tools/playbook/adopt_instructions.py · covers AC6 AC7 AC8 · the `rule-drop`, `stale-copy`, `ignored-file`, `marker-body` and `repeat-under-refuse` plants, the failing case a captured marker-bearing body · none
New arm: tools/memory-tree/marker-contract.test.sh · covers AC24 · the marker-bearing body case, the failing case a `splice_region` that writes it · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. (b) splits clauses the
  repaired units carry whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3,
  the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — How is the log's rule restored after unit 25's S3 and S4?** Options: (a) restore the moved and
  re-keyed rows to their base bytes and positions, record each by an appended note; (b) keep them with a
  deviation naming the lifted rule. (b) needs an owner grant this run does not hold (veto 2). RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the one survivor. widens: none · relaxes: none
- **F3 — Where do `LIBRARY_VIEWS`, `GOTCHA_FIELDS` and the two house-index keys live?** Options: (a)
  catalogue keys read through `read_policy_value`; (b) conf keys, red under `policy check`'s shrink-only
  legacy list. (b) fails that leg (veto 1). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  report's sound fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, 42
  MEDIUM and 11 LOW findings batched, split by write set from `TOOL-dLinkedLibrary-53`.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-59, TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

Every item extends the seam its finding names: `derive_kappa`'s module, `derive_decision_rows`,
`read_trailer_edges`, `corpus_ids.walk` through `gotchas.load_defined_ids` (`tools/memory-tree/gotchas.py:162`),
`derive_pin_hash`, `resolve_compare_base` (`tools/lib/compare_base.py:16`), `carry_renames`, the leg
factory, `read_policy_value`, `load_leg_names` (`tools/memory-tree/gotchas.py:191`), `extract_comment_spans`,
`_derive_program` and `_derive_segment` (`tools/runlog/extract.py:479`, :506) and `splice_region`; no item
mints a second implementation of any. `python tools/codebase-map/reuse_lookup.py "read the paths a shell
command reads"` ranked `read`, `read_text`, `read_conf` and `read_journal`, none a shell-read classifier,
so no existing seam fits S51's function beyond runlog's segment classifier it extends.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
