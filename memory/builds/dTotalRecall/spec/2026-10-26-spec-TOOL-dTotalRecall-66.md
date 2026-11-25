# TOOL-dTotalRecall-66 — the round-1 spec audit of units 54 to 60: its 40 minors, batched

**Status:** CLOSED · rev-5 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 32 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-66-deviation-661.md](../build/2026-10-26-build-TOOL-dTotalRecall-66-deviation-661.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-66-deviation-662.md](../build/2026-10-26-build-TOOL-dTotalRecall-66-deviation-662.md) | deviation | — |
| [2026-11-24-build-TOOL-dTotalRecall-66-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-66-1-acceptance-ledger.md) | log | — |
| [2026-11-24-build-TOOL-dTotalRecall-66-1-builder-return.md](../build/2026-11-24-build-TOOL-dTotalRecall-66-1-builder-return.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-66-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-66-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-66-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-66-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-66-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-66-reground-spec-writer.md) | log | — |
| [2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-65 |
| [2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md](../reviews/2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md) | diff-review | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-36 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 TOOL-dTotalRecall-114 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 54 to 60
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-54-spec-audit-round1.md`)
exited CONVERGED with 45 confirmed findings. Its five highs, ids 1, 2, 3, 22 and 27, are units 61 to
65. This unit is the batch BUILD-METHOD M4 makes of the rest: the 27 MEDIUM findings, ids 4, 5, 6, 7,
8, 12, 13, 14, 15, 16, 24, 25, 28, 31, 32, 33, 34, 37, 39, 40, 41, 42, 43, 44, 45, 46 and 47 (items
M1 to M21), and the 13 LOW findings, ids 9, 10, 11, 18, 19, 20, 21, 23, 29, 35, 38, 48 and 50 (items
L1 to L11). Each keeps its report id and its own scope item. The minors land on units 54 to 60, so
this unit repairs none in particular and builds after every unit: order 32, above the 31 that units
60 and 65 hold. The review record holds each item's text.

Two minors report at a lower grade a defect another finding also carries: id 32 is the AC2 half of
H2, which `TOOL-dTotalRecall-62` amends, and id 29 is M7's literal memory root at its narrower
consequence. Their items re-observe that fix or add what the finding asks beyond it.

Re-grounded at `2ec3df383`, over `TOOL-dTotalRecall-65` rev-5 and `TOOL-dTotalRecall-68` rev-3, whose passes
precede this one. Built here: S1 to S4, S11, S13, S22, S24 to S27, S35 to S37, and the plants of S6 and S23.
S17, S18 and S38 are cut with their reasons. Every other item holds at HEAD or is a ledger line, and keeps its
criterion as a check.

## 2. Scope (IN)

Each item states its change to the unit it lands on, as that unit was built; a landed spec is frozen
and is not edited. "The registry" is `census-kept-paths.txt`, `TOOL-dTotalRecall-65`'s, in the factory grammar
`TOOL-dTotalRecall-68` converts it to; "the reader" is `tree_lib.py#read_kept_rows(census, root)`, whose rows are
read by named field.

- **S1** — id 4 (M1). Unit 55's drain is keyed on the census's own hit: a `check_cause_writers` row of
  the registry is red, naming it, when the build-folder walk does not list its file as a hit, because the
  file spells a cause line past its binding window, spells no Serves literal there, or is not walked. At HEAD
  only the second reds, and an unwalked file is silent (`record_causes.py#check_cause_writers`, S4).
  Observed by AC1.
- **S2** — id 40 (M1). The two ways a hit leaves that unit 55 AC2 never planted are planted:
  `kept-row-caused`, a kept script that gains a `Caused-by` line, and `kept-row-untracked`. Observed by
  AC1.
- **S3** — id 24 (M2). The drain reaches the alias census: a `check_alias_compares` row is red when the
  build-folder walk of `record_kinds.py#check_alias_compares` lists no raw compare in its file, because the
  compare is gone or the file is not walked. Observed by AC2.
- **S4** — id 41 (M2). The plant `alias-row-drained` keeps its row while its raw compare is cut.
  Observed by AC2.
- **S5** — id 13 (M3). Holds at HEAD. Unit 56's AC3 is read against the pin the packet records at the tip, so
  an owner's `--repin` that moves the deviations blob satisfies it. Observed by AC3.
- **S6** — id 5 (M4). Holds at HEAD by unit 57 S3, which unit 65 keeps: `check_alias_compares` reports the
  reader's refusal as one red finding and never aborts its walk. This unit adds the plant
  `alias-row-outside-domain`, which no suite holds. Observed by AC4.
- **S7** — id 6 (M5). Holds at HEAD: `absorbs` is absent from the canonical ledger factory, both inline
  copies, `tools/memory-tree/kit.toml` and `tools/govkit/registry.toml`, where unit 52 put the one
  registration. Observed by AC5.
- **S8** — id 31 (M5). Holds at HEAD: unit 59's plant `merged-home-gained` is in section `2o` of
  `tools/lib/resolve-python.test.sh`, the factory's behaviour arm. This unit edits no `legacy_ledger.py`.
  Observed by AC5.
- **S9** — id 7 (M6). Holds at HEAD: `gen_build_index.py#cmd_new_spec` refuses `TOOL-dFoo1-3` as a
  `Problem` naming the id, by its own match bound to the slug grammar's class, before
  `render_spec_skeleton`. `gov_record.py new spec` and the `--new-spec` forwarder reach it. Observed by AC6.
- **S10** — id 16 (M6). That refusal is observed red first: with the match's two slug patterns admitting
  the id in a probe process, over a scratch repository tracking a `dFoo1` README, the same call writes the
  spec file, and the ledger records both runs. Observed by AC6.
- **S11** — id 8 (M7). A row's domain is built from the conf's `MEMORY_ROOT`, the root
  the reader already takes its registry's path from, and the literal constant
  `KEPT_PATH_DOMAIN` is retired. Observed by AC7.
  **Readers:** by name: `tools/memory-tree/tree_lib.py`, `tools/memory-tree/record_causes.py`,
  `tools/memory-tree/record_kinds.py`, the last two in docstrings · by value: the reader's domain refusal and its
  message, which §4 rebuilds over `build_kept_path_re`.
- **S12** — id 12 (M8). Holds at HEAD. Unit 58's AC2 is read over this run's own commits: `git log --no-merges
  --first-parent` from the run's pinned base, and each instrument's blob against the packet's pin at
  the tip. A pin moved on `main` is the owner's to repin. Observed by AC8.
- **S13** — id 14 (M9). A registry row's path is matched segment by segment,
  `^<memory_root>/builds/[^/]+/build/[^/]+$`, and a row with a `..` segment is refused; `fnmatch` is
  not used, since its `*` crosses `/`. The walk's own glob crosses none (`record_kinds.py#read_tracked`), so
  no row it could keep is lost. Observed by AC9.
- **S14** — id 42 (M9). No registry row this build adds names a file in its own build folder, which
  README:50 puts inside its write set; the engine admits that folder for an adopter, and this pass's
  rule refuses it here. Observed by AC9.
- **S15** — id 15 (M10). Holds at HEAD by unit 58 rev-4: the bound is `id_grammar.py#check_marker_domain`,
  called in the cause and alias censuses' build-folder walks and never in `read_kept_reason`, so a
  `slug-grammar` marker is honoured wherever the slug census reads. Observed by AC10.
- **S16** — id 43 (M10). The slug census's population is stated in the ledger as `scan_readers` has it, the
  tool root, `skills/` and `.githooks/`, correcting unit 58's non-goal, and markers planted under
  `skills/` and `.githooks/` are honoured. Observed by AC10.
- **S17** — id 25 (M11). Cut to what HEAD can observe: unit 60 rev-3 S23 cut the `govkit:generated` block to
  ride owner ask TOOL-dTotalRecall-109 with the held `TOOL-dTotalRecall-37`, so no block hand-spells a
  marker. `marker_pair`, `find_block` and `write_block` building it ride that ask (§8 F4). Observed by AC11.
- **S18** — id 33 (M12). Cut as S17 is: with one block, every govkit site that reads gov's `.gitattributes`
  region reads the one it must, and `WIRE-INTO-PROJECT.md` describes one region. The carve-out keyed by path
  and block, the two withdrawals and the second region ride ask TOOL-dTotalRecall-109 (§8 F4). Observed by
  AC12.
- **S19** — id 28 (M13). Holds at HEAD: no reader tests a marker's path. The tool-root censuses walk the root
  `record_kinds.py#derive_tool_rel` derives from where the kit sits, and the build-folder walks refuse every
  marker. Observed by AC13.
- **S20** — id 37 (M14). The first-seed window is bounded: at the tip every `causes` key of the merged
  home is a key of `legacy-records.txt` at unit 51's pass `30d1901d6`, re-keyed by unit 52's triple, so a row
  added to quiet the causes check reds. Unit 19's seed commit `6ea003891` is no longer the bound: unit 51's
  S3 widened the graded set, and its pass added 139 rows (DERIVED 2026-11-24, `git show --stat 30d1901d6`),
  each a non-Markdown record's. Observed by AC14.
- **S21** — id 32 (M15). Holds at HEAD: unit 52's AC2, as unit 62 rev-3 restated it to the home absent at its
  base, the reading the ratchet prints `new at`, is recorded green in unit 52's acceptance ledger. Observed by
  AC15.
- **S22** — id 34 (M16). Section `2o`'s fixture, unit 59's plant in it, runs with `GOV_REMOTE`,
  `GOV_DEFAULT_BRANCH` and every `GIT_*` variable out of its environment, as
  `tools/branch-reconcile/selftest.py#seed_env` scrubs, its bare remote made with `-b main`. At HEAD `run_ll`
  clears the two `GOV_*` names alone, and every `git -C` call inherits a `GIT_*` one; `origin/HEAD` is set already.
  Observed by AC16.
- **S23** — id 39 (M17). Holds at HEAD by unit 5 S13: `parse_id_parts` refuses a seq-bearing id whose slug the
  grammar refuses. `TOOL-x-3` and `TOOL-9-3` join the refused list of the parser arm. Observed by AC17.
- **S24** — id 44 (M18). One cause-line rule, keyed on the Serves line's prefix, holds at HEAD: units 51 and 60
  made `BIND_RE` capture `prefix` and `record_causes.py#write_missing_causes` write behind the lead. A
  `.json` or `.js` record under `//` gains `// **Caused-by:**`. A non-Markdown record whose head is bare
  is never graded, so it is neither written nor listed `not backfilled`. The plant `backfill-selection` gains the
  three records. Observed by AC18.
- **S25** — id 45 (M19). `record_causes.py --backfill --build <slug>` refuses with exit 2, naming it, a value the
  slug grammar's `BUILD_SLUG_RE` (`TOOL-dTotalRecall-5` S1) does not match whole, or that names no
  tracked build README. At HEAD `--build ..` writes nothing and exits 0. Observed by AC19.
- **S26** — id 46 (M20). Holds at HEAD by unit 50: `record_causes.py#check_ask_filed` reads the asks of the
  `BACKLOG.md` of the build the id names before `check_ask_live` is asked, so an open spec id is refused as no
  filed ask. It keeps that order over S36's row, and the plant `pinned-ask-is-spec` arms it. Observed by AC20.
- **S27** — id 47 (M21). Built by unit 60 S24: an `rsplit` with a maxsplit of 2 or more is listed whatever its
  index. The plant `rsplit-maxsplit-two` joins `_SPLIT_PLANTS` and `_SPLIT_LISTED`. Observed by AC21.
- **S28** — id 9 (L1). Holds at HEAD: unit 60's AC32 is read where the citation lives, the acceptance-ledger
  line of its S32, which cites `tree_lib.py@462d20f3:410-412` and `:421`. Observed by AC22.
- **S29** — id 20 (L1). Those cited lines are confirmed at `462d20f3` to hold `BIND_RE` and
  `def record_paths`. Observed by AC22.
- **S30** — id 50 (L1). A ledger line citing other lines is red whatever the base holds, so the base
  read alone is never the criterion. Observed by AC22.
- **S31** — id 10 (L2). Unit 60 rev-3's AC10 is decided by its ancestry half; the ledger records its grep half
  as certifying nothing. Observed by AC23.
- **S32** — id 11 (L3). Unit 56's AC1 is observed with `grep -c`, which prints `0` on no match.
  Observed by AC24.
- **S33** — id 18 (L4). The unpinned count is derived, six at HEAD (DERIVED 2026-11-24, the rows against
  `packet.py#INSTRUMENTS`), and the ledger cites it for units 57 and 58. Observed by AC25.
- **S34** — id 19 (L5). Holds at HEAD: unit 59's fixture sits under its suite's own temporary directory, unit
  60's AC14 ran in a scratch clone and its AC23 has no fixture, and no arm of the two files spells `%TEMP%`.
  Observed by AC26.
- **S35** — id 21 (L6). `parse_id_parts` keeps its compiled regex in a module dict keyed by the
  resolved root and the caller's `alt` (§4). Observed by AC27.
- **S36** — id 23 (L7). One keep table: `CAUSE_WRITER_PINNED`'s row joins the registry, its
  `records` field the record glob and its disposition `keep:<ask id>`, and the constant gives way to
  that row (§8 F3). Observed by AC28.
  **Readers:** by name: `tools/memory-tree/record_causes.py`, `tools/memory-tree/check-memory-hygiene.test.sh`
  · by value: `read_pinned_records`, `read_grading`, `check_cause_writers` and `run_check`, which read the rows through
  `read_pinned_rows` (§4) and lose their `pinned` argument; the `PINNED_PLANTS` and `check_pinned_plant`, which
  write the row into the fixture's registry; and the arms that spell the constant's name in a hit.
- **S37** — id 29 (L8). The domain is `re.escape(memory_root)` followed by the anchored build-folder
  segments, so a fixture with `MEMORY_ROOT=docs/memory` admits its build-folder row. Observed by AC7.
- **S38** — id 35 (L9). Cut: its premise is gone, since unit 60 rev-3 S14 did not re-point `cmd_new_spec`'s match
  onto `parse_id_parts`, so no refusal carries the parser's `ValueError` text. The ledger names
  the path that refuses S9's id, `cmd_new_spec`'s own match. Observed by AC6.
- **S39** — id 38 (L10). Holds at HEAD: `parse_id_parts` lets `ConfError` propagate unchanged from a root with
  no usable conf (§8 F2). S35's dict keeps it so, and unit 54's error states gain it in the ledger. Observed
  by AC29.
- **S40** — id 48 (L11). The figure guard of unit 60's AC18 is run by this pass over joined paragraphs, matching
  a single digit, `[0-9][0-9,]*`, and the ledger judges each hit. No suite holds that guard. Observed by AC30.

## 3. Non-goals (OUT)

- The five highs: units 61 to 65.
- Editing any landed spec's text, frozen at CLOSED, as §2's opening states.
- The `govkit:generated` block of S17 and S18, its writer and its sites: owner ask TOOL-dTotalRecall-109 (§8 F4).
- The registry's registration, grammar and base compare: `TOOL-dTotalRecall-68`, the ratchet pack's.
- A column rule for the census, the unique pair and the engine's other build-folder literals: `TOOL-dTotalRecall-70`.
- The spec lints and checklist entries the report suggests as gates; the close's left-shift step
  (BUILD-METHOD M8) takes them.

### Edges

- **consumes-from** `TOOL-dTotalRecall-5` — `slug_grammar` and its `BUILD_SLUG_RE` (id 45)
- **consumes-from** `TOOL-dTotalRecall-19` — the seed commit of the legacy home (id 37)
- **consumes-from** `TOOL-dTotalRecall-50` — `CAUSE_WRITER_PINNED` and its ask (ids 23, 46)
- **consumes-from** `TOOL-dTotalRecall-53` — the marker reader of its S34 (ids 15, 28, 43)
- **consumes-from** `TOOL-dTotalRecall-54` — `parse_id_parts` and its arm (ids 21, 38, 39)
- **consumes-from** `TOOL-dTotalRecall-55` — the drain and `read_kept_path` (ids 4, 40)
- **consumes-from** `TOOL-dTotalRecall-56` — the alias row and its criteria (ids 11, 13, 24, 41)
- **consumes-from** `TOOL-dTotalRecall-57` — `KEPT_PATH_DOMAIN` and its refusal (ids 5, 8, 14, 18, 29,
  42)
- **consumes-from** `TOOL-dTotalRecall-58` — the marker's domain and its AC2 (ids 12, 15, 18, 28, 43)
- **consumes-from** `TOOL-dTotalRecall-59` — the fixture and its plant (ids 6, 19, 31, 34, 37)
- **consumes-from** `TOOL-dTotalRecall-60` — S8, S13, S19, S20, S23, S24 and AC10, AC18, AC32 (ids 7,
  9, 10, 16, 19, 20, 25, 33, 35, 44, 45, 46, 47, 48, 50)
- **consumes-from** `TOOL-dTotalRecall-62` — unit 52's restated AC2 (id 32)
- **consumes-from** `TOOL-dTotalRecall-65` — `census-kept-paths.txt` and `read_kept_path`'s root
- **consumes-from** `TOOL-dTotalRecall-68` — S36's pinned-writer row in the factory grammar, told apart by its `records` field and `keep:` disposition, its amendment taken in at rev-5 (the round-1 audit of units 61 to 66, id 16)
- **hands-off** external — S17's and S18's `govkit:generated` block, on owner ask TOOL-dTotalRecall-109
- **hands-off** `TOOL-dTotalRecall-70` — S18's attributes sites, cut here (§8 F4), S34's fixtures, S36's pinned row and AC14, AC22, AC23 and AC28, which that unit re-reads and completes at the tip (the round-1 audit of units 61 to 66, ids 6, 11, 12, 25, 26, 27 and 30)
- **hands-off** `TOOL-dTotalRecall-76` — its seven registry plants, its docs-root plant and its S26 ask read with `pinned-ask-is-spec`, which that batch re-stages and re-reads at the tip (the round-1 audit of units 67 to 70, ids 19, 20, 28)
- **hands-off** `TOOL-dTotalRecall-88` — its registry plants, which that batch rebuilds on one fixture base with a tracked registration and a remote (the round-1 audit of units 71 to 76, ids 25, 26)

## 4. Design

### How the batch builds

One pass, after units 65 and 68, whose commits this unit's edges put first; `TOOL-dTotalRecall-69` shares the
step and writes no file of this one. The items share `tree_lib.py`, `record_causes.py`, `record_kinds.py` and
`id_grammar.py`, and every half would regenerate `memory/map/generated/` with its generator, so BUILD-METHOD M6
keeps them one unit. Within the pass the order is: S11, S37 and S13; S36, then S26's plant; S1 to S4 and S6's
plant; S24 and S25; S35, S23 and S27; S22; then the ledger items S12, S16, S20, S21, S28 to S33, S38, S39 and
S40, and the observations.

### The registry row after S36

```text
check_cause_writers	<deviations.py path>	pinned instrument	<record glob>	1	<sha>	keep:<ask id>
```

A row whose `records` field is `-` is a plain keep. A row whose `records` field is a glob is a pinned
writer, its ask the id of its `keep:` disposition, which S26 resolves. `read_kept_path` returns the row by its
named fields, and no reader counts fields. The glob is `DEPARTURES_GLOB`'s value, the ask `PLAY-dClosedLoop-1002`
and the SHA this pass's base; the home is rewritten through the factory's `write_rows`.
`ratchet (never gains)` reads the home `new at` this run's base, so the row reds nothing
(`ratchet.py#check_new_at_base`).

`read_pinned_rows(root)` in `record_causes.py` returns `[(instrument, glob, ask)]`, one per `check_cause_writers`
row whose `records` is not `-`, `ask` the text after `keep:`, or None under any other disposition, which the
census reds naming the row. Where the reader refuses the registry it returns `[]`, since the census already
reds that refusal, so the causes check grades and `--check` keeps exit 1. `read_grading`,
`check_cause_writers` and `run_check` call it, and the `pinned` argument leaves all three, as unit 65 took `kept`.
Findings and lines name the registry and the path. `CAUSE_WRITER_PINNED` and `CLOSED_LOOP` leave the module;
`DEPARTURES_GLOB` stays as the fixture's glob.

### The drain of S1 and S3

Each build-folder walk collects the paths it lists as hits, whatever disposition it prints, into one set. The
drain loop then reds each row of its census, pinned rows included, whose path is not in that set. The message says
which: `is no file the build-folder walk reads`, `spells Caused-by past its binding window` (the cause
census's), or today's `spells no Serves line past its binding window`, and for the alias census `holds no raw
compare`. A pinned row keeps unit 50's two messages and its ask tests, and a row's drain prints one red, never two.
The `KEPT_INSTRUMENT` test of unit 60 S26 runs first, as at HEAD. A refused registry runs no drain. A fixture that
writes no registry has no rows, as unit 65 rev-5 leaves it, so no other plant reds.

### The domain after S11, S13 and S37

```python
def build_kept_path_re(memory_root: str):
    return re.compile(r"^" + re.escape(memory_root) + r"/builds/[^/]+/build/[^/]+$")
```

It is a sibling of `tree_lib.py#build_spec_path_re`, which builds the spec folder's selector the same way. The
reader refuses, with unit 57's `ValueError`, a row whose path holds a `..` segment or fails `fullmatch` over the
memory root it read. The message spells the domain from that root.

### The plants

- `kept-row-caused`, `kept-row-untracked`, `kept-row-traversal` and `kept-row-nested` each write one row into the
  fixture's registry as unit 68 S6 leaves `kept-row-drained` writing its own, and exit 1 with one `RED` line. The
  first's script spells a Serves literal and a cause line past its window, and the second's file is never added to
  git. The last two name a path with a `..` segment and one under a folder inside `build/`.
- `kept-row-docs-root`: `write_fixture` takes the memory root, `memory` by default, and spells every path, home
  glob and conf line from it. The plant passes `docs/memory`, plants `KEPT_SCRIPT` spelling its hit under a row
  naming it, and passes when `--check` exits 0 and prints its line ending `kept outside the write set`.
- `pinned-ask-is-spec` joins `PINNED_PLANTS`, its row's disposition naming `FIXTURE_UNIT`, an open spec.
- `build-slug-traversal` and `build-slug-absent` join `BACKFILL_PLANTS` with one causeless `fRoot` record and the
  builds `..` and `absentBuild`. Each passes when `write_missing_causes` answers exit 2 naming the value and the
  fixture's status is clean.
- `backfill-selection` gains `-json-prefixed.json` and `-js-prefixed.js`, which `BACKFILL_EXPECTED` lists written,
  and `-html-bare.html`, which it lists nowhere. The grade asserts one `// **Caused-by:**` line under each
  prefixed Serves line. Its paths written are compared as a set, since the run writes in path order.
- `alias-row-drained` and `alias-row-outside-domain` join `record_kinds.py`'s `PLANTS` and its self-test's
  `want`, each row written into the fixture's registry.
- `marker-in-build-script` (unit 58) gains its arm in `tools/memory-tree/check-memory-hygiene.test.sh`, which no
  suite holds at HEAD.

The fixtures write their registry home in the grammar the reader reads, with no registration, which the reader
does not read; units 76 and 88 rebuild them on a registered base.

### The regex dict of S35

`_token_cache` in `id_grammar.py` maps `(resolved root or "", alt or None)` to the compiled
`build_id_token_re`. A hit resolves no conf and no family set. `run_flip_probe` clears it wherever it clears
`_slug_cache`, in both module copies, since a flip changes the slug class under one root. A root with no conf
raises before anything is stored. One call costs 1.1 ms at HEAD with the default `alt` (DERIVED 2026-11-24, node a,
a repeated-call probe).

### The scrub of S22

At the head of section `2o`, two lines: one exporting `GOV_REMOTE=nope` and a `GIT_DIR` naming no repository, the
caller's environment the arm plants, then `unset GOV_REMOTE GOV_DEFAULT_BRANCH ${!GIT_@}`. The bare remote's
`git init` gains `-b main`. Each later block of the section that exports a `GIT_*` name of its own does so after the
scrub, as at HEAD.

### What it does not check

That a row's `records` glob names the records its instrument writes. That S40's guard runs again after this pass.

### Inventory

Minted: `build_kept_path_re` in `tools/memory-tree/tree_lib.py`; `read_pinned_rows` in
`tools/memory-tree/record_causes.py`; `_token_cache` in `tools/memory-tree/id_grammar.py`; the pinned row's
`records` glob and `keep:` disposition; the plants `kept-row-caused`, `kept-row-untracked`,
`alias-row-drained`, `alias-row-outside-domain`, `kept-row-traversal`, `kept-row-nested`,
`kept-row-docs-root`, `build-slug-traversal`, `build-slug-absent`, `pinned-ask-is-spec` and
`rsplit-maxsplit-two`, and the three records of `backfill-selection`. Naming cells: both functions satisfy
`py.function` (`python tools/lexicon/lexicon.py --suggest <name> --as py.function`, 2026-11-24); plants and a dict
have none.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py`
- `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/id_grammar.py`
- `tools/memory-tree/check-memory-hygiene.test.sh` (the arms of S1, S2, S13, S24 to S26, S36 and S37)
- `tools/memory-recall/selftest.py` (the arms of S23, S27 and S35)
- `tools/lib/resolve-python.test.sh` (S22)
- `memory/project/census-kept-paths.txt`
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

### Alternatives rejected

- **Fold each minor into its unit's spec.** M4 refuses folding at the exit.
- **Split into two batches.** Both halves would regenerate `memory/map/generated/` with its generator,
  which M6 clause 3 forbids two concurrent passes to share, and the domain items are read by the drain
  items on both sides.
- **Keep the `pinned` argument, None reading the registry.** Its only passers are plants, and unit 65 refused the
  same for `kept`.
- **Plant a marker under `skills/` and under `vendor/gov/` in a suite.** Unit 58 built no path test to guard, so
  the plants would arm nothing.

## 5. Production-readiness checklist

- security — S13 refuses a traversal row; S25 validates a path-forming argument at its boundary.
- perf / scale — S35 resolves and compiles once per root. Each plant costs about 8 s (DERIVED 2026-11-24, node a,
  one `kept-row-drained` run). Nine arms are new in the hygiene suite, under its ceiling of 4800 s (DERIVED,
  `tools/gate-legs.json`).
- error / empty / loading states — a refused registry is one red and no drain; S25 exits 2 naming the value;
  S39 lets a misconfigured tree's `ConfError` name its conf.
- observability — every new red names its row, file or value, and the registry.
- risks — S36 changes the pinned row's home; its readers move in the same commit. S35's dict could serve a stale
  class inside one process whose conf changes, which the flip probe clears and no other caller does. An adopter's
  row whose file it deleted reads red from here on, the remedy being to drain it.
- testing — AC1 to AC30 by the pass; the arms of §7 at the close.
- migration — S36 adds one row to the home unit 68 wrote; no record is rewritten.
- user docs — none: no `help/` page covers the censuses, and the kit README's paragraph is unit 70's.

## 6. Acceptance criteria

Where a criterion reads "as at HEAD", the pass observes it and builds nothing for it. Fixture commands run from
`tools/memory-tree/`.

- **AC1** — When `python record_causes.py --fixture --plant kept-row-caused` and `--plant
  kept-row-untracked` run, each exits 1 with one `record causes: RED ` line naming `census-kept-paths.txt` and
  the row's path. Red when: a row with no hit behind it passes.
- **AC2** — When `python record_kinds.py --fixture --plant alias-row-drained` runs, it exits 1 naming the row's
  path, and at the tip `python -c "import record_kinds as k; print(*k.check_alias_compares('../..', 'tools')[0], sep='\n')"`
  lists `deviations.py line 380 · kept pinned instrument`. Red when: a drained alias row passes, or the live one reds.
- **AC3** — When `git hash-object` runs on the deviations instrument at the tip, it prints the `blob`
  the Pins line of `memory/builds/dTotalRecall/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`
  names at HEAD. Red when: the two differ.
- **AC4** — When `python record_kinds.py --fixture --plant alias-row-outside-domain` runs, a row naming a file under
  the fixture's tool root, it exits 1 naming that path and prints no traceback.
  Red when: the census aborts or keeps the row.
- **AC5** — When `git grep -n absorbs -- '*legacy_ledger.py' tools/memory-tree/kit.toml tools/govkit/registry.toml` runs
  at the tip it prints nothing, as at HEAD, and `grep -c "2o merged-home-gained" resolve-python.test.sh` run from
  `tools/lib/` prints at least 1. Red when: a copy keeps the field, or the plant leaves the factory's arm.
- **AC6** — When `python tools/memory-tree/gov_record.py new spec TOOL-dFoo1-3 --tier 2` runs at the tip it exits 2
  naming the id, writes no file and prints no traceback, as at HEAD. In a probe process over a scratch repository
  tracking a build README for the slug `dFoo1`, `cmd_new_spec` raises a `Problem` naming the id, and with
  `backlog.SLUG_RE` and the slug class it reads both admitting `dFoo1`, it writes the file; the ledger records the
  runs and which path refused. Red when: the refusal comes from another check.
  fixture: the scratch repository under the run's scratch directory; the pass makes it.
- **AC7** — When `python record_causes.py --fixture --plant kept-row-docs-root` runs over a fixture with
  `MEMORY_ROOT=docs/memory` and a row under its build folder, it exits 0 and prints the row's line ending
  `kept outside the write set`, and `git grep -n KEPT_PATH_DOMAIN -- tools` prints nothing at the tip.
  Red when: the row is refused for its root, or the literal stays.
- **AC8** — When `git log --no-merges --first-parent --name-only 462d20f3..HEAD -- 'memory/builds/*/build/*.py'`
  runs at the tip it prints no path, and `python tools/chain-packet.py --check dTotalRecall` exits 0, each
  instrument's blob at its Pins line, as at HEAD. Red when: a pass of this run wrote an instrument.
- **AC9** — When the plants `kept-row-traversal` and `kept-row-nested` run through
  `python record_causes.py --fixture --plant <name>`, each exits 1 naming its path, and
  `grep -c "memory/builds/dTotalRecall/" census-kept-paths.txt` run from `memory/project/` prints `0`.
  Red when: a traversal or nested row is admitted, or the build keeps a file of its own folder by row.
- **AC10** — When `python id_grammar.py --readers <tree>` runs over a scratch git tree holding, under `skills/` and
  under `.githooks/`, one hyphen split marked `# census: kept slug-grammar y` and one unmarked, it lists the two
  unmarked lines and neither marked one, as at HEAD.
  Red when: a slug-grammar keep outside the tool root is refused, or either folder is not read.
  fixture: the scratch tree under the run's scratch directory; the pass makes it.
- **AC11** — When `git grep -n "govkit:generated" -- tools .gitattributes` runs at the tip it prints nothing, as at
  HEAD. Red when: a block is hand-spelled while unit 37 is held.
- **AC12** — When `grep -c 'GA_BLOCK_ID = ' govkit.py` runs from `tools/govkit/` it prints `1` and
  `grep -n 'GA_BLOCK_ID' govkit.py` names no second block id, as at HEAD.
  Red when: a second block lands with sites reading one.
- **AC13** — When `tools/` is copied to `vendor/gov/` of a scratch git repository,
  `python record_causes.py --fixture --plant unmarked-writer` run from the copy's `memory-tree/` prints `PASS`, its marked
  line kept under `vendor/gov/`, and `--plant marker-in-build-script` prints `PASS`, a build-folder script's marker
  refused, as at HEAD. Red when: the literal `tools/` decides.
  fixture: the copy under the run's scratch directory; the pass makes it.
- **AC14** — When a `python -c` probe compares the `causes` keys of `record-kinds-legacy.txt` at the tip with
  `git show 30d1901d6` of `legacy-records.txt`, the revision spelled with `:./` and run from `memory/project/`, both
  read as text with universal newlines, by path and section, it prints no key that revision lacked, as at HEAD.
  Red when: a `causes` row added after it passes.
- **AC15** — When `grep -n "the merged home absent at" 2026-11-23-build-TOOL-dTotalRecall-52-2-acceptance-ledger.md`
  runs from `memory/builds/dTotalRecall/build/`, it prints the AC2 line recorded at unit 52's tip, as at HEAD.
  Red when: unit 52's AC2 was not observed there.
- **AC16** — When a scratch script runs the lines of section `2o` from its head to its `AC4` comment, over `bad` and
  `ok` functions of its own and with `GOV_REMOTE=nope` and a `GIT_DIR` naming no repository exported by its
  caller, no `bad` line prints and the `merged-home-gained` case names its planted key `gained`; with the scrub line
  cut, a `bad` line prints. Red when: the fixture reads the caller's environment.
  fixture: the script and its temporary directory under the run's scratch directory; the pass makes them.
- **AC17** — When a probe calls `parse_id_parts` with `TOOL-x-3` and `TOOL-9-3`, each raises
  `ValueError`, as at HEAD. Red when: either returns a tuple.
- **AC18** — When `python record_causes.py --fixture --plant backfill-selection` runs, its `-json-prefixed.json` and
  `-js-prefixed.js` records each hold one `// **Caused-by:** TOOL-fRoot-1` line under their Serves line, its
  `-html-bare.html` record is in no backfill or `causes` line and byte-identical, and the plant prints `PASS`.
  Red when: a prefixed record is skipped or a bare one is written.
- **AC19** — When `python record_causes.py --fixture --plant build-slug-traversal` and `--plant build-slug-absent` run,
  `--backfill --build ..` and `--build absentBuild` there each answer exit 2 naming the value, the fixture's status
  is clean, and each plant prints `PASS`. Red when: either writes, or exits 0.
- **AC20** — When `python record_causes.py --fixture --plant pinned-ask-is-spec` runs, a row whose ask is an
  open spec id, its `--check` exits 1 naming the row and `which is not a filed ask`, and the plant prints `PASS`.
  Red when: a spec id passes as an ask.
- **AC21** — When `python id_grammar.py --readers <tree>` runs over a scratch git tree whose `skills/` holds
  `x.rsplit("-", 2)[0]`, it lists that line, as at HEAD. Red when: the census exempts it.
- **AC22** — When `git grep -n "tree_lib.py@462d20f3:410-412" -- memory/builds/dTotalRecall/build` runs at the tip it
  prints the ledger line for unit 60's S32, which also cites `:421`, and `git show 462d20f3` of `tree_lib.py`, the
  revision spelled with `:./` and run from `tools/memory-tree/`, holds `BIND_RE` and `def record_paths` there, as at HEAD.
  Red when: the ledger cites other lines.
- **AC23** — When `git merge-base --is-ancestor 74af3faa4 c6fcf603b` runs it exits 0, unit 54's pass before unit 45's,
  and the ledger names AC10's grep half void. Red when: unit 45 built first.
- **AC24** — When `grep -c "census: kept"` runs over the deviations instrument at the tip it prints `0`, as at HEAD.
  Red when: a marker sits in the instrument.
- **AC25** — When a `python -c` probe counts the registry paths of both censuses that `packet.py`'s `INSTRUMENTS` does
  not pin, it prints `6`, the figure the ledger cites. Red when: the ledger cites another count.
  figure: DERIVED 2026-11-24 over `2ec3df383`'s nine rows; S36's row adds a pinned path and moves no count.
- **AC26** — When `git grep -n "%TEMP%" -- tools/lib/resolve-python.test.sh tools/govkit/selftest.py`
  runs at the tip it prints nothing, as at HEAD. Red when: an arm spells a cmd.exe variable.
- **AC27** — When a probe calls `parse_id_parts("TOOL-dFoo-3", "../..")` twice, `len(id_grammar._token_cache)` reads
  one, and one `python id_grammar.py --flip-probe <clone>` prints the same `flip ` lines as at the pass base.
  Red when: the regex compiles per call, or a flip reads a stale one.
  fixture: a scratch clone with no remote under the run's scratch directory; the pass makes it.
- **AC28** — When `git grep -n CAUSE_WRITER_PINNED -- tools` runs at the tip it prints nothing, and
  `python record_causes.py --cause-writers` keeps the pinned writer's records by its registry row's `records`
  glob: its `pinned` line names `PLAY-dClosedLoop-1002`, `filed` and the same record count as at the pass base, and
  the build-folder count line reads `0 red`. The plants `pinned-writer-drained` and `departures-pinned` print `PASS`
  over a registry row. Red when: two keep tables remain, or a reader still takes the constant.
- **AC29** — When the probe calls `parse_id_parts("TOOL-dFoo-3", root)` with a root holding no
  `.memory-tree.conf`, it raises `ConfError` naming the missing conf, as at HEAD. Red when: it raises another class.
- **AC30** — When a probe joins each paragraph's lines and matches `[0-9][0-9,]* .?journal`, over a scratch file whose
  figure `9` wraps onto the line before `journal` it lists the figure, and over
  `git ls-files -- tools memory/guides memory/HYGIENE.md` each hit is named in the ledger with what it is.
  Red when: a wrapped or single-digit figure escapes, or a record figure ships with no command beside it.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `record-kinds` · `record causes (causes and orphans over the legacy population)` · `ratchet (never gains)` · `ratchet (key shape)` · `memory-recall kit selftest` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `shell-hygiene selftest` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC7 AC9 · the five `kept-row-` plants of §4, staged by skipping the hit test, by the literal root and by skipping the domain match · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC18 AC19 · the `backfill-selection` records and the two `build-slug-` plants, staged by a lead of `# ` whatever the line wears and by skipping the slug test · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC13 AC20 AC28 · `marker-in-build-script`, `pinned-ask-is-spec` and the moved arms of the pinned plants, staged by skipping `check_marker_domain`, the filed-ask test and the pinned-row read · none
New arm: tools/memory-tree/record_kinds.py · covers AC2 AC4 · `alias-row-drained` and `alias-row-outside-domain` in the self-test's `want`, staged by skipping the drain and the refusal · none
New arm: tools/memory-recall/selftest.py · covers AC17 AC21 AC27 · `TOOL-x-3` and `TOOL-9-3`, `rsplit-maxsplit-two` and the dict's one entry, staged by a looser slug class, by exempting every `[0]` and by compiling per call · none
New arm: tools/lib/resolve-python.test.sh · covers AC16 · section `2o` under the planted `GOV_REMOTE` and `GIT_DIR`, staged by cutting the scrub line · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of one unit's clause, which would split a clause that unit carries whole. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How does `parse_id_parts` answer a root with no usable conf (S39)?** Options: (a) let
  `ConfError` propagate, its message naming the conf; (b) re-raise it as `ValueError`, which the readers
  catch as a malformed id. (b) reports a misconfigured tree as a bad id and hides the refusal the error
  carries. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the option that keeps both refusals
  distinct. widens: none · relaxes: none
- **F3 — Which table holds the pinned writer's row (S36)?** Options: (a) the registry, its `records` field
  and `keep:` disposition; (b) `CAUSE_WRITER_PINNED`, widened with a census column for the other rows. (b) keeps a
  constant in engine bytes naming a path of this repository, the defect unit 65 closes. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — What do S17 and S18 build with no `govkit:generated` block in the tree?** Unit 60 rev-3 F4 cut the
  block. Options: (a) cut both to the observation that HEAD holds no such block, the rest riding owner ask
  TOOL-dTotalRecall-109; (b) build the second region and its sites now, with no line to write. (b) is
  scaffolding for a held unit. RESOLVED (agent, 2026-11-24, delegated): (a), rung 3, as unit 60 rev-3 ruled for
  its S23. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 54 to 60, its 40
  minors batched (27 MEDIUM, 13 LOW).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-68, TOOL-dTotalRecall-70, each the other end of an edge a unit the round-1 spec audit of units 61 to 66 promoted wrote; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-76, the other end of an edge a unit the round-1 spec audit of units 67 to 70 promoted wrote; nothing else moved.
- rev-4 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-88, each the other end of an edge a
  unit the round-1 spec audit of units 71 to 76 promoted wrote; nothing else moved.
- rev-5 · 2026-11-24 · §1 S1 to S40 §3 §4 §5 AC1 to AC30 §7 §8 §10 · re-grounded at HEAD `2ec3df383` per
  `2026-11-24-prompt-TOOL-dTotalRecall-66-reground-spec-writer`, over unit 65 rev-5 and unit 68 rev-3: S36, §4, AC28, the
  Inventory and F3 amended by TOOL-dTotalRecall-68 (id 16, item H2); S17 and S18 cut to what HEAD observes (F4) and S38
  cut for its gone premise; S5 to S10, S12, S15, S16, S19, S21, S23, S26 to S34 and S39 hold and are re-observed, some
  with a plant; S20's bound is unit 51's pass; S24's bare record is never graded; S8's section is `2o`; AC5, AC14, AC15,
  AC22 and AC23 read where the tree holds the fact; the arm of unit 58's `marker-in-build-script` joins; the govkit and
  build-index files leave Files touched.

## 10. Reuse audit

Each item extends the seam its finding names, re-read at `2ec3df383`: unit 55's drain in
`record_causes.py#check_cause_writers`, unit 57's refusal and unit 65's `root` in `tree_lib.py#read_kept_rows`, unit
68's rows and `legacy_ledger.py#write_rows`, unit 58's `id_grammar.py#check_marker_domain`,
`record_causes.py#check_ask_filed`, `record_causes.py#read_readme_slugs`, `id_grammar.py#derive_slug_grammar`, whose
`_slug_cache` S35's dict sits beside, and `tools/branch-reconcile/selftest.py#seed_env`. `build_kept_path_re` and
`read_pinned_rows` are the two new functions, the first beside `tree_lib.py#build_spec_path_re`.
`python tools/codebase-map/reuse_lookup.py "project registry of exempt paths read from the memory root"`
ranked name-stem neighbours, and the registry reader it missed is unit 65's; the same probe over "anchored regex
over a build folder path built from the memory root" ranked none nearer.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
