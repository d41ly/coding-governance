# TOOL-dLinkedLibrary-96 — the spec audit of units 87 to 91: its medium and low findings, batched

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 37 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-96-deviation-961.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-96-deviation-961.md) | deviation | — |
| [2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dLinkedLibrary-1-parents-crosscheck.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-95 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 87 to 91
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md`) confirmed
14 MEDIUM and 7 LOW findings. BUILD-METHOD M4 promotes them into one batch unit, and this is it; each
finding is its own scope item below, by report id:

- MEDIUM: 1 and 25 (item M1), 2 (M2), 3 (M3), 4, 18 and 28 (M4), 8 and 14 (M5), 9 (M6), 10 (M7), 11
  (M8), 24 (M9), 26 (M10).
- LOW: 5 (L1), 6 (L2), 13 (L3), 15 (L4), 19 (L5), 20 (L6), 27 (L7).

L2 (id 6) is M6's defect at the low grade a second skeptic bound; each id takes its own item, and S10
and S16 each stage one half of the corrected criterion. The findings land on five units, 87 to 91, so
this unit repairs none in particular and builds after every unit of the build (order 37).

One unit and not two. The census items write `adopt_program.py` and `help/adopt.md`, and S8 writes
`tools/memory-tree/tree_lib.py`, whose `read_blobs_at` the census then reads as a contract, which
BUILD-METHOD M6's clause 2 forbids across concurrent passes. S11 writes
`tools/lib/resolve-python.test.sh` alone, but every half adds functions and re-renders the generated
map with its generator, a shared generated index clause 3 forbids, and the halves write amendment lines
into the same units' acceptance ledgers. No split leaves two disjoint write sets.

## 2. Scope (IN)

Each item lands at the pass §4 "Where each item lands" states. An item landing at an earlier unit's
pass is built by that pass, which writes an amendment line in its acceptance ledger citing this unit
and the item; no item lands at a pass ordered before a unit it names.

### Unit 88: the order of the flow test and the scalar branch

- **S1** — id 1, M1. At 88's pass, 88 S1's flow test and S4's empty-collection test run before
  `TOOL-dLinkedLibrary-81` S2's scalar branch, and the scalar branch reads only a `variables:` value
  opening neither `[` nor `{`. 88's ledger records that order in an amendment line naming 81 S2 as the
  branch 88 narrows. Observed by AC1.
- **S2** — id 25, M1. 88 AC4's staged copy keeps 81's scalar branch and lacks only 88 S1's flow test,
  so AC1's tree reads `importable` because nothing reads a flow value; a second scratch copy that runs
  the scalar branch first gives the same tree `refused: unreadable variables item expression`. Observed
  by AC2.

### Units 87 and 88: where 91's Azure items land

- **S3** — id 2, M2. 91 S2's amendment line in 81's acceptance ledger lands at 87's pass, written by
  87, whose AC1 to AC3 it names. 91 S3's page sentence, which 91 S4 placed at 81's pass, lands at 88's
  pass, the latest of 81, 82 and 88: 88's files gain `help/adopt.md`, and 91 AC4 reads the page at 88's
  pass start and at its last pass commit. Observed by AC3.

### Unit 91: the file-wide function's population

- **S4** — id 3, M3. 91 S17's predicate, stated: the file-wide function is the one each file-wide hit
  site calls, 71 S2's `include:`, 76 S2's `default:`, 84 S2's blocks, 89 S3's out-of-job `$[[` and
  `TOOL-dLinkedLibrary-93` S2's line break. The class 91 AC17 counts is every function holding a `for`
  loop over a file's whole job list whose body stores a refusal reason reading no name the loop target
  binds. The per-job grader of 63 and 51, whose reason reads the job, and 79 S3's stage-scoped loop,
  whose iterable is one stage's jobs, are outside the class. Observed by AC4.

### Unit 90: one decode, every reader

- **S5** — id 4, M4. At 90's pass, 90 S2's one path names its readers: the GitHub, GitLab and Azure job
  readers, 71 S2's `include:` reader, 84's job-wide block reader and 89's header split, each taking its
  lines from `ci_lines` and decoding a CI file nowhere else. Observed by AC5.
- **S6** — id 18, M4. 90 AC4's walk covers exactly S5's named functions and every function they call
  inside `adopt_program.py`, and finds a decode in any spelling outside `ci_lines`: a `.decode(` call, an
  `encoding=` keyword, `text=True`, `read_text`, `open` in text mode, `str` with an encoding argument, or
  `codecs.decode`. The walk runs on `adopt_program.py`'s arm. Observed by AC6.
- **S7** — id 28, M4. At 90's pass, a case of `adopt_program.py --fixture --plant ci-census`: a BOM-led
  CRLF `.gitlab-ci.yml` whose first line is `include: remote.yml`, over two plain jobs, `test` running
  `npm test` and `lint` running `npm run lint`. Observed by AC7.
- **S8** — id 8, M5. At 90's pass, `read_blobs_at` (`tools/memory-tree/tree_lib.py:328`) gains an opt-in
  `raw` keyword. With it a blob's body comes back as bytes, neither decoded nor CRLF-folded, and None
  stays only for an object the rev does not hold or one that is not a blob. 90 S1's `ci_lines` takes its
  bytes from `read_blobs_at` with `raw` set, so the kit keeps one `<rev>:<path>` bytes reader. Observed
  by AC8.
- **S9** — id 14, M5. A CI file that is not valid UTF-8 is graded, not lost: at 90's pass, a case of the
  same plant holds a `.gitlab-ci.yml` whose comment line carries the byte `FF`, over the two plain jobs,
  and 90's ledger names `read_blobs_at` as the seam 90 §10 left out, in an amendment line. Observed by
  AC9.

### Unit 91: the codebase-map criterion

- **S10** — id 9, M6. 91 AC29 reads the constant it claims to equal: S29's grep prints one distinct
  value, compared with the value of `KIT_CODEBASE_MAP_VERSION` parsed from
  `tools/codebase-map/map_lib.py:49`. Staged in a scratch clone with only the constant moved, the one
  printed value differs from the constant. Observed by AC10.
- **S16** — id 6, L2. 91 AC29's second staged half: in a scratch clone with only the `map_lib.py:47`
  marker moved, the grep prints two distinct values. Observed by AC16.
- **S17** — id 13, L3. 91 AC29's scratch clone lives in a directory made by `mktemp -d` under an absolute
  short scratch root that bash expands, never `%TEMP%`, which Git Bash leaves literal, and `rm -rf`
  clears the directory after the read. Observed by AC17.

### Unit 91: the runbook host

- **S11** — id 10, M7. 91 S24's free-name read slices the runbook host in two steps: the fenced block
  as the lines `unfenced_lines` (`tools/memory-tree/tree_lib.py:149`) does not yield, then the `<<'PY'`
  heredoc inside it with `extract_heredoc_body` (`tools/gate-lint/sh_hygiene.py:274`). The fence plus
  heredoc container joins 91 S22's container list, and the host at `WIRE-INTO-PROJECT.md:1686` joins 91
  AC22's hosts. Observed by AC11.

### Units 87 to 90: the map freshness leg

- **S12** — id 11, M8. At the passes of 87, 88, 89 and 90, a pass that adds a function to
  `adopt_program.py` re-renders the generated map with `python tools/codebase-map/gen_map.py --write`
  where its `--check` exits 1, in the same pass commit, and its ledger names the `codebase-map coverage
  + freshness` leg in an amendment line. Units 92 to 95 name the leg in their own section 7. Observed by
  AC12.

### Unit 87: the quoted scalar

- **S13** — id 24, M9. At 87's pass, a case of the same plant: an Azure file whose pipeline-level line
  is `variables: '${{ parameters.vars }}'`, beside a `parameters:` list holding `- name: vars` with
  `type: object` and the two plain jobs, `publish` running `./publish.sh` and `test` running `npm test`.
  87 S4's scalar red is staged with a scratch copy whose scalar test matches only values opening `${{`.
  Observed by AC13.

### Unit 89: the header document and its interpolations

- **S14** — id 26, M10. At 89's pass, 89 S1's separator is a column-0 `---` followed by the end of the
  line, whitespace or ` #`, and 89 S3 refuses a `$[[` on any non-job line outside a detected header
  document, whether or not the file has one. A case of the same plant repeats 89 AC2's tree with its
  separator spelled `--- # end of header`. Observed by AC14.
- **S15** — id 5, L1. At 89's pass, a case of the same plant holds a top-level `spec:` block whose
  `inputs:` gives `stage` the default `test`, with no `---` after it, over the two plain jobs `release`
  running `./release.sh` and `test` running `npm test`. Observed by AC15.
- **S18** — id 15, L4. At 89's pass, 89 S2's test is one more key of 71 S1's per-job test, spelled
  `inputs`, not a second per-job scan. A job holding both a 71 S1 token and a `$[[` reads the reason of
  the first in its line order. 89's ledger names 71 S1 as the seam 89 §10 left out, in an amendment line.
  A case of the same plant holds a job `release` whose `extends: .base` line precedes a `script:` running
  `"$[[ inputs.cmd ]]"`, over a hidden `.base` running `./release.sh`, and a plain job `test`. Observed by
  AC18.
- **S20** — id 20, L6. 89 S3's call into 71 S2's file-wide function is a call site 91 S17 enumerates:
  S4 lists it, and 89's ledger records it in an amendment line citing this unit. Observed by AC4 and
  AC20.
- **S21** — id 27, L7. At 89's pass, the first `$[[` in file order names `<name>`, and a job's own-line
  hit (89 S2) wins over a file-wide one (89 S3). A case of the same plant holds the header of 89 S6, a
  top-level `variables:` mapping `DEPLOY_CMD: $[[ inputs.cmd ]]`, a job `release` whose `script:` runs
  `"$[[ inputs.env ]] $[[ inputs.cmd ]]"`, and a plain job `test` running `npm test`. Observed by AC21.

### Unit 91: the ledger absence grep

- **S19** — id 19, L5. 91 AC18's absence grep reads only lines that are not this build's amendment
  lines: `grep -v 'TOOL-dLinkedLibrary-91'` over 86's acceptance ledger, then `grep -c 'census refuse a
  ci'`, so the line recording the set-aside half of 86 AC26 cannot turn it red. Observed by AC19.

## 3. Non-goals (OUT)

- The HIGH findings of the same audit: units 92 to 95, one per id.
- Re-opening any unit's design: each item corrects a plant, a criterion's observation, a reading rule a
  spec left ambiguous, a landing pass or a record.
- A gate per left-shift the report proposes, among them a spec-tokens refusal of `%[A-Z_]+%` in a
  criterion and a records check of landing rows: every item lands on an existing arm, plant, reader,
  criterion or record.
- The `%TEMP%` spellings of units 23, 37 and 80: outside the audited set; S17 corrects 91's.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-71` — S1's per-job test and S2's one file-wide function, which S4, S18 and S20 name as the seams 89 and 91 extend (ids 3, 15, 20)
- **consumes-from** `TOOL-dLinkedLibrary-87` — its pass, which writes 91 S2's line into 81's ledger, the quoted-scalar plant and its restaged red, and the map re-render, by S3, S12 and S13 (ids 2, 11, 24)
- **consumes-from** `TOOL-dLinkedLibrary-88` — S1, S3 and S4 with AC4, which S1 and S2 order and restage, and its pass, which lands 91 S3's page sentence and the map re-render, by S3 and S12 (ids 1, 25, 2, 11)
- **consumes-from** `TOOL-dLinkedLibrary-89` — S1 to S3 and S6, which S14, S15, S18, S20 and S21 settle and plant, and the map re-render, by S12 (ids 26, 5, 15, 20, 27, 11)
- **consumes-from** `TOOL-dLinkedLibrary-90` — S1, S2, S3, AC4, §7 and §10, which S5 to S9 widen, plant and seam, and the map re-render, by S12 (ids 4, 18, 28, 8, 14, 11)
- **consumes-from** `TOOL-dLinkedLibrary-91` — S2 to S4, S17, S18, S22, S24, S29 with AC4, AC17, AC18, AC22 and AC29, which S3, S4, S10, S11, S16, S17 and S19 re-land and restate (ids 2, 3, 9, 10, 6, 13, 19)
- **consumes-from** `TOOL-dLinkedLibrary-93` — S2's call into 71 S2's file-wide function, which S4 lists among the call sites 91 AC17 prints (id 3)
- **hands-off** `TOOL-dLinkedLibrary-97` — S6's walk and AC6's structural check, which unit 97 gives a closed decode table and one planted red per spelling (id 9)
- **hands-off** `TOOL-dLinkedLibrary-98` — S8's `raw` keyword and AC8's probe, which unit 98 observes over a blob written filter-free and proved to hold its CRs (id 10)
- **hands-off** `TOOL-dLinkedLibrary-100` — S6's walk, S8's `raw` keyword and AC6's structural check, which unit 100 extends to every helper the walked readers import (id 27)
- **hands-off** `TOOL-dLinkedLibrary-101` — S8's `raw` keyword and AC8's red clause, whose two named breaks unit 101 stages (id 29)
- **hands-off** `TOOL-dLinkedLibrary-102` — S4, S8, S20, AC4 and AC20, which unit 102 restates and re-lands, its S15, S16, S18 and S19 at this unit's pass, and §4's cites and Inventory, by its S20 and S21 (ids 2, 31, 15, 6, 7, 8, 20)

## 4. Design

### Where each item lands

| Lands at the pass of | Items |
|---|---|
| `TOOL-dLinkedLibrary-87` (order 33) | S3's ledger line, S12, S13 |
| `TOOL-dLinkedLibrary-88` (order 33) | S1, S2, S3's page sentence, S12 |
| `TOOL-dLinkedLibrary-89` (order 26) | S12, S14, S15, S18, S20's ledger line, S21 |
| `TOOL-dLinkedLibrary-90` (order 34) | S5 to S9, S12 |
| this unit (order 37) | S4, S10, S11, S16, S17, S19, and every observation |

S3's two halves land where every unit they name is already built: 87's line names 87's own criteria,
and the page sentence names 82's template reason and 88's `flow` form. S4, S10 and S16 to S19 restate
91's criteria and are observed here, after 93's call site exists. S11 changes the parity suite 86 S25
builds, at this unit's pass, before the close runs the suite.

### Evidence

- S1, S2: 81 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-81.md`, S2) refuses "a scalar on its own line"
  and gives no test telling a scalar from a flow value; 88 S3 (`2026-10-27-spec-TOOL-dLinkedLibrary-88.md:41-43`)
  orders the flow test before the item readings only.
- S3: 91 §4's table puts S1 to S4 at 81's pass (order 32), while 87 and 88 sit at order 33 and 82 shares
  order 32 (README build order, steps 32 and 33).
- S4: 91 S17 (`2026-10-27-spec-TOOL-dLinkedLibrary-91.md:113-115`) counts every loop storing a job's
  `refused` reason; 79 S3 scopes a stage-level hit to that stage's jobs.
- S5 to S7: 90 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-90.md:40-42`) names no function list; 90 AC4
  (`:124-128`) counts `decode` calls only; 90 S3's plants open with `before_script:` and `jobs:`.
- S8, S9: `read_blobs_at` (`tools/memory-tree/tree_lib.py:328-367`) is the kit's one `<rev>:<path>` bytes
  reader; it decodes strict UTF-8, folds CRLF and returns None for a blob that is not UTF-8.
- S10, S16, S17: `tools/codebase-map/map_lib.py:47` holds `#: gov:kit codebase-map@1.30` and `:49` holds
  `KIT_CODEBASE_MAP_VERSION = "1.30"`, which no `codebase-map@` grep matches; 91 AC29 spells
  `%TEMP%/cm91`.
- S11: `WIRE-INTO-PROJECT.md:1686` holds the runbook's `# >>> resolve_prefix_token` host, inside the
  `cat > "$G/harness-migration.py" <<'PY'` heredoc opened at `:1649` and closed at `:1869`, inside the
  bash fence opened at `:1642` and closed at `:1897`; `tools/lib/resolve-python.test.sh:226` includes
  `WIRE-INTO-PROJECT.md` in the parity population.
- S12: the `codebase-map coverage + freshness` leg (`tools/gate-legs.json:833-842`) carries no `guard`
  key, so no Files-touched join owes it, and it byte-compares the four renders.
- S14, S15, S18, S20, S21: 89 S1 to S3 (`2026-10-27-spec-TOOL-dLinkedLibrary-89.md:35-46`) and 89 §10
  (`:167-171`); 71 S1 (`2026-10-27-spec-TOOL-dLinkedLibrary-71.md`, S1) defines `refused: opaque step
  <key> <value>` per job.
- S19: 86 AC26's set-aside half is exactly the `census refuse a ci` grep.

### Inventory

S8 mints the `raw` keyword of `read_blobs_at`. No other identifier is minted.

### Rollout

The plants of S7, S9, S13 to S15, S18 and S21 add cases to `adopt_program.py` at the passes §4 names,
each re-rendering the map by S12 where it adds a function. This unit's own pass re-renders the
generated map with `python tools/codebase-map/gen_map.py --write` where its `--check` exits 1.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1, S2, S5 to S7, S9, S13 to S15, S18, S21
- `tools/memory-tree/tree_lib.py`: S8
- `help/adopt.md`: S3
- `tools/lib/resolve-python.test.sh`: S11
- `memory/builds/dLinkedLibrary/build/`: the amendment lines of S1, S3, S9, S12, S18 and S20
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: S12 and the Rollout re-render

### Alternatives rejected

- **One unit per finding.** M4 forbids it.
- **Folding each item into its unit's spec.** The owner's 2026-10-05 ruling promotes every minor and
  folds none.
- **S8 by a second bytes reader beside `read_blobs_at`.** It breaks the kit's one-reader rule
  (TOOL-dTrueNorth-20 S33); an opt-in keyword keeps one.
- **S19 by forbidding the amendment line to quote the pattern.** It lands at 86's pass and relies on a
  writer's wording; the scoped grep holds whatever the line says.
- **S3 by moving 91 S2 and S3 to 91's own pass.** 81's ledger would certify 81 S2 and S3 by nothing
  until order 35; 87's pass is the first at which the plants exist.

## 5. Production-readiness checklist

- security — S5 to S9 close a BOM-led or non-UTF-8 file escaping a file-wide refusal; S13 and S14 close
  a quoted expression and a commented separator grading `importable`.
- perf / scale — S6 adds one `ast` walk to the arm; S8 skips a decode.
- error / empty / loading states — S9 grades a file holding a stray byte; S11 fails naming a host whose
  container chain it cannot slice.
- observability — each refusal names its reason as its unit states; S1, S3, S9, S12, S18 and S20 leave
  a ledger line naming what moved.
- risks — S8 changes a shared reader; its default stays the decoded text every existing caller reads.
- testing — AC1 to AC21 by plant, scratch copy, `ast` walk, probe and ledger grep.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — `help/adopt.md`, S3's sentence at 88's pass.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both jobs of
  88's `variables: [ { group: release-vars } ]` tree read `refused: unreadable variables item flow`, both
  of its `variables: {}` tree read `importable`, and `grep -n 'TOOL-dLinkedLibrary-96'` over 88's
  ledger prints the line naming 81 S2 as the branch 88 narrows.
  Red when: the scalar branch catches a flow value first.
- **AC2** — When the scratch copy of `adopt_program.py` lacking 88 S1's flow test runs the same plant by
  `python -I`, both jobs of 88 AC1's tree print `importable`; when the copy running 81's scalar branch
  first runs it, they print `refused: unreadable variables item expression`.
  Red when: neither copy changes the reason, so 88 AC4 cannot tell S1 from the scalar branch.
- **AC3** — When `git show` reads the help page `adopt.md` at 88's pass start and at its last pass commit, each
  commit found by `git log --format=%H --grep` on its `build(dLinkedLibrary): TOOL-dLinkedLibrary-88 `
  subject, `grep -c 'unreadable variables item'` prints 0 and then 1; and `git log --format=%s` over
  81's ledger names a `TOOL-dLinkedLibrary-87` pass commit as the one adding 91 S2's line.
  Red when: a sentence or ledger line lands before the units it names.
- **AC4** — When `python -I -c` walks `adopt_program.py` with `ast` at this tip, it prints, for each of
  S4's five hit sites, the function it calls, one distinct name; it prints S4's class as exactly that
  function; and it prints the per-job grader and 79 S3's stage-scoped loop as `not counted`. Over a
  scratch copy inlining a second loop that refuses every job for `default:`, the class prints two.
  Red when: a correct build prints two members, or the inlined loop is missed.
- **AC5** — When `python -I -c` walks with `ast` the `adopt_program.py` of 90's last pass commit, read
  with `git show`, it prints a `ci_lines` call inside each of S5's six named readers.
  Red when: a file-wide reader takes its text from another path.
- **AC6** — When `python adopt_program.py --fixture --plant ci-census` runs its structural check, it walks
  S5's readers and their callees and prints no decode outside `ci_lines`; over a scratch copy whose
  Azure reader takes text from `subprocess.run` with `git show` and `text=True`, it names that reader.
  Red when: a decode in a spelling other than `.decode(` passes the walk.
- **AC7** — When the same plant runs, both plain jobs of S7's BOM-led CRLF `include:` tree read `refused:
  opaque step include remote.yml`; over a scratch copy whose file-wide `include:` check decodes its own
  bytes with `utf-8`, they read `importable`.
  Red when: the BOM hides the first line's `include:` from a file-wide reader.
- **AC8** — When `python -I -c` imports `tree_lib` and calls `read_blobs_at` over a scratch repository's
  blob holding `EF BB BF`, CR LF line ends and a byte `FF`, with `raw` set it returns exactly the
  committed bytes, and without it returns None, as before.
  Red when: the raw mode decodes or folds, or the default changes for an existing caller.
- **AC9** — When the same plant runs, both plain jobs of S9's `FF` tree print rows reading `importable`,
  and `grep -n 'read_blobs_at'` over 90's ledger prints the amendment line.
  Red when: a non-UTF-8 CI file reads None and its jobs print no row.
- **AC10** — When S29's grep runs at this tip it prints one distinct value, equal to the constant parsed
  from `map_lib.py:49`; in a scratch clone with only the constant moved, the printed value differs from
  the constant.
  Red when: the criterion stays green on a constant that moved alone.
- **AC11** — When 91 S24's free-name read runs by hand with `python -I` at this tip, it prints the
  `WIRE-INTO-PROJECT.md:1686` host as read, with its container chain, fence at `:1642` then heredoc at
  `:1649`, and no unbound name; over a scratch copy of the runbook whose heredoc body loses an import
  the host uses, it names that name.
  Red when: the host is read as bash, raises, or is skipped.
- **AC12** — When `python tools/codebase-map/gen_map.py --check` runs in a scratch worktree at the last
  pass commit of each of 87, 88, 89 and 90, it exits 0, and `grep -n 'codebase-map coverage'` over each
  of their ledgers prints the amendment line.
  Red when: a pass adds a function and leaves the map stale for the bar.
  cost: four scratch worktrees under a short scratch root, deleted after the read.
- **AC13** — When the plant runs, both jobs of S13's quoted tree read `refused: unreadable variables item
  expression`; over the scratch copy whose scalar test matches only values opening `${{`, they read
  `importable`.
  Red when: a quoted expression scalar reads as an empty block.
- **AC14** — When the plant runs, both plain jobs of S14's `--- # end of header` tree read `refused:
  opaque step inputs cmd`.
  Red when: a commented separator hides the header and the out-of-job `$[[` refuses nothing.
- **AC15** — When the plant runs, S15's separator-less tree prints no row named `spec` or `inputs`, and
  its two plain jobs read `importable`.
  Red when: a separator-less `spec:` is graded as a job.
- **AC16** — When S29's grep runs in a scratch clone with only the `map_lib.py:47` marker moved, it
  prints two distinct `codebase-map@` values.
  Red when: the staged half cannot fire on a correct build.
- **AC17** — When AC10's and AC16's probes run, each clone directory path begins with the expanded
  scratch root, and `git status --porcelain` at the worktree afterwards prints no path holding `%TEMP%`.
  Red when: the probe writes a literal `%TEMP%` directory into the worktree.
- **AC18** — When the plant runs, the job `release` of S18's tree reads `refused: opaque step extends
  .base`, and `grep -n 'TOOL-dLinkedLibrary-96'` over 89's ledger prints the line naming 71 S1 as the
  seam.
  Red when: a second per-job scan gives the job a reason by its own order.
- **AC19** — When S19's scoped grep, `grep -v 'TOOL-dLinkedLibrary-91'` piped to `grep -c 'census refuse a ci'`,
  runs over 86's acceptance ledger at this tip it prints `0`.
  Red when: the retirement record itself turns the absence check red.
- **AC20** — When `grep -n '71 S2'` runs over 89's ledger, it prints the amendment line naming S3's call
  as a call site 91 S17 enumerates.
  Red when: 89's routing stays invisible from 91's population.
- **AC21** — When the plant runs, the job `release` of S21's tree reads `refused: opaque step inputs
  env`, and the plain job `test` reads `refused: opaque step inputs cmd`.
  Red when: the printed name depends on the builder's order.

## 7. Gates

`policy fixtures` · `python resolver (behaviour + inline parity + idiom ban)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC6 AC7 AC9 AC13 AC14 AC15 AC18 AC21 · the `ci-census` plant's flow-order, BOM-led `include:`, stray-byte, quoted-scalar, commented-separator, separator-less, extends-before-input and two-input trees, and the one-decode walk, the failing case staged by a scalar branch run first, a self-decoding file-wide reader and a `text=True` Azure reader · none
New arm: tools/lib/resolve-python.test.sh · covers AC11 · the free-name read over the runbook's fence-plus-heredoc host, the failing case staged by a heredoc body losing an import · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. (b) splits clauses the
  repaired units carry whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — Which reason wins when one job holds a 71 S1 token and a `$[[`?** Options: (a) the first in the
  job's line order; (b) 71 S1's keys always; (c) `$[[` always. (a) is the rule the report's corrected
  fix for id 27 states for two `$[[` hits, so one rule covers both; (b) and (c) each add a precedence no
  spec states. RESOLVED (agent, 2026-10-27, delegated): (a), S18. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 87 to 91, 14 MEDIUM and 7 LOW
  findings batched in one unit.
- rev-2 · 2026-10-27 · §3 · the hands-off edges to units 97, 98, 100, 101 and 102, the mirrors of the
  consumes-from edges their specs declare, promoted from the spec audit of units 92 to 96;
  no scope or criterion moved.

## 10. Reuse audit

Every item extends the seam its finding names: the census's reader and plants in
`tools/memory-tree/adopt_program.py`, 71 S1's per-job test and S2's file-wide function, 90 S1's
`ci_lines`, `read_blobs_at` in `tools/memory-tree/tree_lib.py`, `unfenced_lines` in the same module,
`extract_heredoc_body` in `tools/gate-lint/sh_hygiene.py`, the parity loop of
`tools/lib/resolve-python.test.sh`, and `gen_map.py --write`; no item mints a second implementation of
any. `python tools/codebase-map/reuse_lookup.py "read a blob at a revision as bytes"` ranked `read`,
`read_text`, `read_conf` and `read_journal` and did not surface `read_blobs_at`, which `grep -n 'def
read_blobs_at'` finds at `tree_lib.py:328`; the lookup's miss is recorded here and the grep is the
evidence S8 rests on.

Recall terms used: `python tools/memory-recall/query.py "how does the census read a ci blob at a sha and which readers decode it" --terms "census read_blobs_at ci_lines decode bom one reader blob sha codebase-map freshness"`
