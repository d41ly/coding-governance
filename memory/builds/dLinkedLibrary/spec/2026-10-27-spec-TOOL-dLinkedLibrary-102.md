# TOOL-dLinkedLibrary-102 — the spec audit of units 92 to 96: its medium and low findings, batched

**Status:** DEFERRED · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 39 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 |
| [2026-10-27-build-TOOL-dLinkedLibrary-102-deviation-1021.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-102-deviation-1021.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 92 to 96
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md`) confirmed
13 MEDIUM and 8 LOW findings. BUILD-METHOD M4 promotes them into one batch unit, and this is it; each
finding is its own scope item below, by report id:

- MEDIUM: 1 (item M1), 2 (M2), 3 (M3), 4 and 26 (M4), 11 and 23 (M5), 12 (M6), 15 (M7), 17 (M8), 25 (M9),
  28 (M10), 31 (M11).
- LOW: 5, 13 and 22 (L1), 6 (L2), 7 (L3), 8 (L4), 19 (L5), 20 (L6).

Three items share a defect with another grade. M8 (id 17) is H3's defect at the skeptic's grade, and H3
(id 24) is `TOOL-dLinkedLibrary-99`; S10 observes 99's rule over 81's and 82's trees. M10 (id 28) is part
of H1's defect, and H1 (id 9) is `TOOL-dLinkedLibrary-97`; S17 observes 97's table end to end. L1 (ids 5,
13, 22) is M7's stale premise at low; S11 to S14 make the one edit, an item per id. The findings land on
units 92 to 96, so this unit repairs none in particular and builds after every unit of the build (order
39).

One unit and not two. The census items write `adopt_program.py` and re-render the generated map with its
generator, a shared generated index BUILD-METHOD M6's clause 3 forbids across concurrent passes; the
records items write amendment lines into the acceptance ledgers of 92, 93, 94 and 96, which the census
items' amendment lines also write. No split leaves two disjoint write sets.

## 2. Scope (IN)

Each item lands at the pass §4 "Where each item lands" states. An item landing at an earlier unit's pass
is built by that pass, which writes an amendment line in its acceptance ledger citing this unit and the
item. No item lands at a pass ordered before the pass that builds what it names.

### Unit 92: the round-trip proof

- **S1** — id 1, M1. Every tree of the `ci-census` plant carries a tree id, `<unit>-<label>-<dialect>`,
  `<label>` being the scope item or criterion of the spec that plants it and `<dialect>` one of
  `gitlab`, `github` and `azure`, with `-<n>` appended in the item's order where one item plants several
  trees of a dialect. 92 S2's lines print it: `fixture: blob kept <plant> <tree> <path> bom=<0|1> cr=<n>`
  and `fixture: committed blob differs from planted bytes <plant> <tree> <path>`. Every tree is compared
  and each mismatch printed before the fixture exits non-zero, grading no plant. 92 AC1 reads the trees
  `90-S3-gitlab`, `90-S3-azure` and `90-S3-github`, and 92 AC2 reads `90-S3-gitlab` among the mismatches.
  Observed by AC1.
- **S2** — id 11, M5. 92 S2's compare hashes the bytes the plant intended, held in memory, with `git
  hash-object --no-filters --stdin`, and compares the result with `git rev-parse HEAD:<path>`; `bom=` and
  `cr=` count the intended bytes. The file on disk is never the reference. Observed by AC2.
- **S3** — id 23, M5. The fixture writes every file it commits with `write_bytes`, never a text-mode
  write, so a Windows newline translation cannot reach a plant. A scratch copy of `adopt_program.py` that writes one
  CRLF plant's bytes with every `\r\n` written as `\r\r\n` through `write_bytes` exits non-zero printing
  `committed blob differs from planted bytes` and that tree's id, on every node. Observed by AC2.

### Unit 93: the line-break refusal

- **S4** — id 4, M4. 93 S3's GitHub plant's lone-CR comment line is followed by `on: push`, and its Azure
  plant's by `trigger: none`, never by `jobs:`. A further GitLab plant holds a job `test` whose
  `script: [npm test]` line ends in a lone CR directly before the header `lint:`, over `script: [npm run
  lint]` indented two spaces. Observed by AC3.
- **S5** — id 26, M4. 93 S2 prints one file-level row whenever `ci_lines` reports an unreadable break,
  whatever the number of jobs found: the file's path, the job field `(file)`, reading `refused: unreadable
  line break U+<hex>`. A plant holds a `.gitlab-ci.yml` whose `test` and `lint` jobs are separated only by
  lone CRs, with no LF in the file. 93 §5's risks line reads, in an amendment line in 93's ledger, that a
  file saved by a legacy Mac editor prints its file-level row and refuses every job found. Observed by AC3.
- **S6** — id 19, L5. The break scan runs first: a file whose `ci_lines` returns a break is refused with
  `unreadable line break U+<hex>` through 71 S2's file-wide function before any other file-wide or per-job
  reader runs, and the six readers 96 S5 names unpack `ci_lines`' (lines, first break) return. A plant
  holds a `.gitlab-ci.yml` with a top-level `include: remote.yml` on its own line, a comment line ending in
  a lone CR and the two plain jobs `test` and `lint`. Observed by AC4.
- **S7** — id 12, M6. 93's pass follows 92's. 93 AC3 is read only after 92's `fixture: blob kept` lines
  print `bom=1` and a non-zero `cr=` for each of 90 S3's three trees, and 93's ledger records that
  precondition in an amendment line. Observed by AC5.

### Unit 94: the next-line value

- **S8** — id 3, M3. 81's item read classifies a line inside a `variables:` block as a mapping key only
  when, outside quotes and outside a `${{ ... }}` span, it holds `: ` or ends with `:`. A colon-less line
  that does not open `- ` is reached only through 94 S1's locator: as the located value it is 94 S3's
  scalar, and anywhere else in the block it continues the value above it or is a line YAML refuses, so the
  item read passes over it. 94 S3's "disjoint by their first characters" reads as "disjoint by this rule",
  in an amendment line in 94's ledger. Observed by AC6.
- **S9** — id 25, M9. A case of the plant with two stages, each holding the two plain jobs `publish` and
  `test`: the first holds a stage-level `variables:` alone over `    [ { group: stage-vars } ]`, the
  second none. 94 AC5's staged copy also runs over this tree. Observed by AC7.

### Unit 99: the same-indent list, over 81's and 82's forms

- **S10** — id 17, M8. Two cases of the plant, each with the two plain jobs: `variables:` at column 0
  over `- ${{ if eq(variables['Build.SourceBranchName'], 'main') }}:` at column 0 over `  - group:
  release-vars`; and `variables:` at column 0 over `- template: release-vars.yml` at column 0. 99 S5's
  staged copy also runs over both. Observed by AC8.

### Unit 92: the raw read its goal rests on

- **S11** — id 15, M7. 92's goal, exercising 90's per-line CR strip, rests on 96 S8: `ci_lines` takes its
  bytes from `read_blobs_at` with `raw=True`. 92's ledger records that in an amendment line naming 96 S8.
  Two scratch copies of `adopt_program.py` make it observable: one whose `ci_lines` strips no CR, which
  must turn 90 AC2's Azure tree red, and one whose `ci_lines` also reads without `raw`, which must leave it
  green, the CR folded before the strip. Observed by AC9.
- **S12** — id 5, L1. 92 §3's second non-goal reads, in an amendment line in 92's ledger: S2 reads no
  blob because the object-id compare needs none, and `read_blobs_at` with `raw=True` is the kit's bytes
  read from 90's pass. Observed by AC10.
- **S13** — id 13, L1. 92 §4's second rejected alternative reads, in an amendment line in 92's ledger: a
  bytes read-back is rejected because S2's hash of the intended bytes reads no blob, not because no bytes
  reader exists. Observed by AC10.
- **S14** — id 22, L1. 92 §10's seam sentence reads, in an amendment line in 92's ledger: `read_blobs_at`
  decodes and folds by default and returns bytes under `raw=True`, and S2 compares object ids. Observed by
  AC10.

### Unit 96: the file-wide refusal class

- **S15** — id 2, M2. 79 S3's pipeline-level and top-level hit, GitLab's top-level `variables:`, GitHub's
  workflow `env:` and Azure's pipeline `variables:`, refuses through 71 S2's file-wide function with 79's
  reason text, and joins 96 S4's hit sites as the sixth. 79 S3's stage-level branch stays its own loop and
  is named in the walk's exclusion list, `JOB_LOOP_EXCLUSIONS`, beside its reason. 96 S4's predicate is
  stated over syntax: a member is a function, other than 71 S2's file-wide function and those
  `JOB_LOOP_EXCLUSIONS` names, holding a store into the refusal map 91 S17 reads of one reason for every
  element of an iterable, the stored reason reading no name the iteration binds. Observed by AC11.
- **S16** — id 31, M11. The store forms S15's predicate counts: a `for` statement; a list, set, dict or
  generator comprehension; `dict.fromkeys(<iterable>, <reason>)`; `map` over an iterable; and an
  `update` call on the refusal map taking any of these. Observed by AC11.

### Unit 97: the subprocess twins, end to end

- **S17** — id 28, M10. Two scratch copies of the real `adopt_program.py`, whose Azure reader calls a
  helper of the module that takes its text from `subprocess.run` over `git show`, once with `errors="strict"`
  alone and once with `universal_newlines=True`, each make the structural check name the Azure reader
  through the helper. Observed by AC12.

### Unit 96: the ledger lines on 89

- **S18** — id 6, L2. 96 AC20 is a scoped grep: over 89's ledger, `grep 'TOOL-dLinkedLibrary-96'` piped
  to `grep -c '91 S17'` prints `1`. Observed by AC13.
- **S19** — id 7, L3. 96 S20's line at 89's pass names only 71 S2's file-wide function. The line recording
  89 S3's call as a call site 91 S17 enumerates lands at 96's pass, in 89's ledger, as an amendment line
  citing 96. Observed by AC13.

### Units 93 to 96: the cites

- **S20** — id 8, L4. Each drifted cite is read by section and item id, its line PINNED at `9d556a8b` on
  2026-10-27, per §4 "The corrected cites", and the ledgers of 93, 94, 95 and 96 each carry their
  corrected cites in an amendment line. Observed by AC14.

### Units 92 to 96: the naming leg

- **S21** — id 20, L6. At the passes of 92, 93, 94, 95 and 96, and at this one, a pass adding a function
  to `adopt_program.py` names it after `python3 tools/lexicon/lexicon.py --suggest <name>`, runs `python
  tools/lexicon/lexicon.py` after `gen_map.py --write`, and names the `lexicon naming predicates` leg in an
  amendment line in its ledger. 96's ledger lists, in an amendment line, the functions S5 to S9 add.
  Observed by AC15.

## 3. Non-goals (OUT)

- The HIGH findings of the same audit: units 97 to 101, one per id.
- Re-opening any unit's design: each item corrects a plant, a printed line, a reading rule a spec left
  ambiguous, a landing pass, a criterion's observation or a record.
- A gate per left-shift the report proposes, among them a records check of landing rows against unit
  orders and a resolver of line cites: every item lands on an existing arm, plant, reader, criterion or
  record.
- Folding any item into its unit's spec: the owner's 2026-10-05 ruling promotes every minor and folds
  none.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-71` — S2's one file-wide function, which S15 routes 79 S3's pipeline-level hit through and S6 calls first (ids 2, 19)
- **consumes-from** `TOOL-dLinkedLibrary-79` — S3's scoping, whose pipeline-level branch S15 routes through 71 S2 and whose stage-level loop it names as excluded (id 2)
- **consumes-from** `TOOL-dLinkedLibrary-89` — its pass and ledger, where S19 narrows 96 S20's line to 71 S2's function and 96's pass adds the 91 S17 line (ids 7, 6)
- **consumes-from** `TOOL-dLinkedLibrary-90` — AC2's BOM-led CRLF Azure tree, which S11's two scratch copies turn red and leave green (id 15)
- **consumes-from** `TOOL-dLinkedLibrary-92` — S1 to S3 with AC1 and AC2, §3, §4 and §10, which S1 to S3 and S11 to S14 settle and record, and the naming leg at its pass, by S21 (ids 1, 11, 23, 15, 5, 13, 22, 20)
- **consumes-from** `TOOL-dLinkedLibrary-93` — S1 to S3, §5 and AC3, which S4 to S7 plant, order and record, §4's cites, by S20, and the naming leg at its pass, by S21 (ids 4, 26, 19, 12, 8, 20)
- **consumes-from** `TOOL-dLinkedLibrary-94` — S1, S3 and AC5, which S8 and S9 settle and plant, §4's cites, by S20, and the naming leg at its pass, by S21 (ids 3, 25, 8, 20)
- **consumes-from** `TOOL-dLinkedLibrary-95` — §4's cites, which S20 corrects, and the naming leg at its pass, by S21 (ids 8, 20)
- **consumes-from** `TOOL-dLinkedLibrary-96` — S4, S8, S20, AC4 and AC20, which S11 and S15 to S19 restate and re-land, §4's cites and Inventory, by S20 and S21 (ids 2, 31, 15, 6, 7, 8, 20)
- **consumes-from** `TOOL-dLinkedLibrary-97` — S2's subprocess keyword row, which S17 observes end to end (id 28)
- **consumes-from** `TOOL-dLinkedLibrary-99` — S1's same-indent sequence start and S5's staged copy, which S10 runs over 81's and 82's forms (id 17)

## 4. Design

### Where each item lands

| Lands at the pass of | Items |
|---|---|
| `TOOL-dLinkedLibrary-89` (order 26) | S19's narrowed line |
| `TOOL-dLinkedLibrary-94` (order 34) | S8, S9, S21 |
| `TOOL-dLinkedLibrary-92` (order 35) | S1 to S3, S21 |
| `TOOL-dLinkedLibrary-93` (order 35) | S4 to S7, S21 |
| `TOOL-dLinkedLibrary-95` (order 36) | S21 |
| `TOOL-dLinkedLibrary-96` (order 37) | S15, S16, S18, S19's 91 S17 line, S21's Inventory line |
| this unit (order 39) | S10 to S14, S17, S20, S21, and every observation |

S15 and S16 land at 96's pass because 96 AC4 is read there: a pipeline-level loop of 79's would make AC4
print two members on a correct build. S10 follows 99 (order 35) and S17 follows 97 (order 38). S11 to S14
name 96 S8, which 96's table builds at 90's pass, and are recorded here.

### The corrected cites

PINNED at `9d556a8b`, 2026-10-27, each the opening line of the cited item.

| Spec citing | Cited | Was | Is |
|---|---|---|---|
| 95 §4 | 91 S11's `before_script: *base` plant | `91.md:84` | `91.md:85` |
| 95 §4 | 91 S12's `image: *img` and `cache: *c` plants | `:92-93` | `:93-94` |
| 95 §4 | 91 §5 risks | `:274-275` | `:277` |
| 95 §4 | 91 S11 | `:86-90` | `:87` |
| 95 §4 | 91 S6 | `:66-70` | `:67` |
| 94 §4 | 88 S1 | `88.md:35-38` | `88.md:36` |
| 94 §4 | 88 S5 | `:46-51` | `:47` |
| 93 §4 | 90 S1 | `90.md:36-39` | `90.md:37` |
| 93 §4 | 90 §5 | `:99-110` | `:103` |
| 96 §4 | 88 S3 | `88.md:41-43` | `88.md:42` |
| 96 §4 | 91 S17 | `91.md:113-115` | `91.md:114` |
| 96 §4 | 90 S2 | `90.md:40-42` | `90.md:41` |
| 96 §4 | 90 AC4 | `:124-128` | `:128` |
| 96 §4 | 89 S1 to S3 | `89.md:35-46` | `89.md:36` |
| 96 §4 | 89 §10 | `:167-171` | `:170` |

### Evidence

- S1: 92 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-92.md`, S2) prints `<case> <path>`, `<case>` the
  `--plant` value; 86 AC2 and 96 S7 plant further CRLF `.gitlab-ci.yml` trees in the same plant.
- S2, S3: the report's skeptic wrote `'\ufeffjobs:\r\n  t:\r\n'` by `write_text` on this node and read
  back `jobs:\r\r\n` (finding id 23); `tools/govkit/matrix.py:440-465` passes `newline=` beside its
  autocrlf call, and 92 copies the autocrlf half only.
- S4, S5: 93 S1 splits on LF alone; the skeptic split `test:\r  script: [npm test]\rlint:\r  script: [npm
  run lint]\r` on `\n` and got one line (finding id 26).
- S8: 81 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-81.md`, S2) refuses "a mapping key opening with `${{`";
  YAML reads a plain multi-line scalar's continuation only deeper than its key.
- S11 to S14: `tools/memory-tree/tree_lib.py:364` folds CR LF on the default path; 96 S8 adds `raw` at
  90's pass, order 34, before 92's, order 35.
- S15, S16: 79 S3 (`2026-10-27-spec-TOOL-dLinkedLibrary-79.md`, S3) refuses every job a block applies to
  and scopes only a stage-level hit; 96 S4 counts only `for` loops.
- S18, S19: 89's own hands-off edge already reads "71 S2's file-wide function", so an unscoped grep
  matches it.
- S21: `.lexicon.conf:327` pins `VERB_OFFENDER_PIN="1212"`; the `lexicon naming predicates` leg
  (`tools/gate-legs.json:1455`) runs `lexicon.py`, and 92 to 96 §7 omit it while units 8 and 86 name it.

### Inventory

S1 mints the tree id grammar and its `(plant, tree)` fields in the two fixture lines; S5 mints the job
field `(file)`; S15 mints the module constant `JOB_LOOP_EXCLUSIONS`. A function a pass adds is named
after `python3 tools/lexicon/lexicon.py --suggest <name>`, the lexicon's cell for a function name.

### Rollout

The plants of S4 to S6 and S8 to S10 add cases to `adopt_program.py` at the passes §4 names. This unit's
own pass re-renders the generated map with `python tools/codebase-map/gen_map.py --write` where its
`--check` exits 1, then runs `python tools/lexicon/lexicon.py`.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S11, S15 to S17
- `memory/builds/dLinkedLibrary/build/`: the amendment lines of S5, S7, S8, S11 to S14 and S18 to S21
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: the Rollout re-render

### Alternatives rejected

- **One unit per finding.** M4 forbids it.
- **S1 by stopping at the first mismatch.** The trees' order would decide which tree a failure names;
  comparing all and printing each names every folded tree.
- **S8 by changing 94 AC5 to require any reason other than AC1's to AC3's.** It leaves 94 S3's
  disjointness claim false; the colon rule makes it true and keeps AC5's `importable`.
- **S15 by excluding 79 S3's scoping helper at every level.** A pipeline-level credential refusal would
  then stay a second file-wide path whose reason and scope can drift, the defect 86 S7's one function
  closes; §8 F2 records the choice.

## 5. Production-readiness checklist

- security — S4 to S6 close jobs hidden by a lone CR going unreported; S8 to S10 keep the next-line and
  same-indent `variables:` refusals discriminated; S15 and S16 keep every file-wide refusal on one path.
- perf / scale — six more scratch trees in the plant; two git calls per planted file, as before.
- error / empty / loading states — S5's file-level row prints for a file whose jobs cannot be found; S1
  prints every mismatch before exiting.
- observability — S1's lines name the tree; S5's row names the file; each ledger line names what moved.
- risks — S15 moves 79's pipeline-level branch onto 71 S2's function at 96's pass; its verdicts and
  reasons are unchanged, which AC11 and 79's own criteria observe.
- testing — AC1 to AC15 by plant, scratch copy, `ast` walk, `sed -n` and ledger grep.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — none under `help/`: no refusal reason changes; 93 S5's page sentence stands.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs on a node whose global
  `core.autocrlf` is `true`, it prints `fixture: blob kept ci-census 90-S3-gitlab`, `90-S3-azure` and
  `90-S3-github` lines, each with `bom=1` and a non-zero `cr=`; and the scratch copy of 92 AC2, under its
  scratch gitconfig, prints a `committed blob differs` line for every CRLF tree, `90-S3-gitlab` among them,
  before it exits non-zero.
  Red when: a line cannot name 90's trees, or the fixture stops at the first mismatch.
- **AC2** — When the scratch copy of S3 runs the same plant by `python -I`, it exits non-zero printing
  `committed blob differs from planted bytes` and the tree id of the corrupted plant, on Linux as on
  Windows; and a `python -I -c` walk with `ast` over the functions the `--fixture` path calls prints no
  `write_text` call and no `open` call in a text mode.
  Red when: a plant corrupted on disk is reported `blob kept`.
- **AC3** — When the same plant runs, both jobs of 93 S3's GitHub and Azure trees read `refused:
  unreadable line break U+000D`; S4's GitLab tree prints the `(file)` row and its `test` job reads that
  reason, and no row reads `lint` `importable`; and S5's all-CR tree prints the `(file)` row and no row
  reading `importable`.
  Red when: a job after a lone CR drops out with no row, or the comment line swallows `jobs:`.
- **AC4** — When the same plant runs, both jobs of S6's `include:` tree read `refused: unreadable line
  break U+000D`, not `refused: opaque step include remote.yml`.
  Red when: a file-wide reader runs over lines 93 calls unreadable and its reason wins.
- **AC5** — When `git log --format=%s` lists the pass commits, 92's pass commit precedes 93's, and
  `grep 'TOOL-dLinkedLibrary-102'` over 93's ledger prints the precondition line naming 90's three trees.
  Red when: 93 AC3 is certified before 92 keeps CR LF in the fixture.
- **AC6** — When 94 AC5's scratch copy, whose locator reads only the key's line, runs the plant by
  `python -I`, both jobs of 94 AC3's `  ${{ parameters.vars }}` tree print `importable`, and 81's own
  `${{ if ... }}:` key tree still reads `refused: unreadable variables item expression`.
  Red when: 81's item read takes a colon-less `${{` line for a key and AC5 cannot tell S1 from it.
- **AC7** — When the plant runs, both jobs of S9's first stage read `refused: unreadable variables item
  flow` and both of its second stage read `importable`; under 94 AC5's scratch copy, the first stage's
  jobs print `importable`.
  Red when: a locator wired only at pipeline level passes.
- **AC8** — When the plant runs, both jobs of S10's `${{ if }}` tree read `refused: unreadable variables
  item expression` and both of its template tree read `refused: unreadable credentials template
  release-vars.yml`; under 99 S5's scratch copy, both trees print `importable`.
  Red when: a column-0 list under `variables:` reads as an empty block.
- **AC9** — When S11's first scratch copy runs the plant by `python -I`, 90 AC2's `publish` job no longer
  reads `refused: npm publish`; when its second copy runs it, the job reads `refused: npm publish` again;
  and `grep 'TOOL-dLinkedLibrary-102'` over 92's ledger prints the line naming 96 S8.
  Red when: the CR strip is exercised whether or not `ci_lines` reads with `raw`.
- **AC10** — When `grep 'TOOL-dLinkedLibrary-102'` runs over 92's ledger, piped to `grep -c 'raw=True'`, it
  prints `3`, one line each for §3, §4 and §10.
  Red when: 92's record still rests on `read_blobs_at` having no bytes read.
- **AC11** — When `python -I -c` walks `adopt_program.py` with `ast` at this tip, it prints six hit
  sites, each calling one function, and a class of exactly that function, with 79 S3's stage-level loop
  printed `not counted` from `JOB_LOOP_EXCLUSIONS`; over a scratch copy adding a dict comprehension that
  refuses every job for `default:`, and over one adding `dict.fromkeys(jobs, reason)`, the class prints
  two.
  Red when: a correct build prints two members, or a comprehension or `dict.fromkeys` refuser is missed.
- **AC12** — When each of S17's two scratch copies runs the structural check by `python -I`, it exits
  non-zero naming the Azure reader, once for `errors` and once for `universal_newlines`.
  Red when: a subprocess twin of `text=True` passes the walk through a helper.
- **AC13** — When `grep 'TOOL-dLinkedLibrary-96'` runs over 89's ledger at this tip, piped to `grep -c '91
  S17'`, it prints `1`, and `git log --format=%s` names a `TOOL-dLinkedLibrary-96` pass commit as the one
  adding that line.
  Red when: the grep matches 89's own text, or the line lands before 91 exists.
- **AC14** — When `sed -n` prints each line §4 "The corrected cites" pins, it shows the cited item's
  opening; and `grep 'TOOL-dLinkedLibrary-102'` over the ledgers of 93, 94, 95 and 96 prints each corrected
  cite.
  Red when: a cite lands on a different line or item.
  figure: PINNED at `9d556a8b`, 2026-10-27.
- **AC15** — When `grep -c 'lexicon naming predicates'` runs over the ledgers of 92 to 96 it prints at
  least `1` for each pass that added a function, and `python tools/lexicon/lexicon.py` at this tip exits
  0; and `grep 'TOOL-dLinkedLibrary-102'` over 96's ledger prints the function list of S5 to S9.
  Red when: a pass names a function the lexicon refuses and the leg reds only at the lander.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC4 AC7 AC8 · the `ci-census` plant's tree ids and intended-bytes compare, its lone-CR, all-CR and include-beside-break trees, its two-stage next-line tree and its column-0 expression and template trees, the failing case staged by a `\r\r\n` plant, an LF-only reader and a deeper-only locator · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. (b) splits clauses the
  repaired units carry whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — How does 96 S4's class leave 79 S3's pipeline-level scoping out?** Options: (a) exclude 79 S3's
  scoping helper at every level by name; (b) route the pipeline-level hit through 71 S2's file-wide
  function and exclude only the stage-level loop. Both are the report's. (a) leaves a second file-wide
  refusal path, a follow-up against 86 S7's one function; (b) closes it and reuses 71 S2's seam.
  RESOLVED (agent, 2026-10-27, delegated): (b), S15. widens: none · relaxes: none
- **F3 — Does a mismatch stop the fixture?** Options: (a) stop at the first; (b) compare every tree and
  print each mismatch. (a) lets the trees' order decide which tree 92 AC2 names, failing it on a correct
  build; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (b), S1. widens: none · relaxes:
  none
- **F4 — How does 94 AC5 tell the locator from 81's key rule?** Options: (a) state that a key needs a
  colon outside quotes and `${{ }}`; (b) relax AC5 to any reason other than AC1's to AC3's; (c) plant
  AC3's scalar without `${{`. (b) and (c) leave 94 S3's disjointness claim false; (a) satisfies every
  criterion and leaves none open. RESOLVED (agent, 2026-10-27, delegated): (a), S8. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 92 to 96, 13 MEDIUM and 8 LOW
  findings batched in one unit.

## 10. Reuse audit

Every item extends the seam its finding names: the census's reader, plants and fixture in
`tools/memory-tree/adopt_program.py`, 92 S2's object-id compare, 93 S1's `ci_lines` split, 94 S1's
locator and 81 S1's item read, 71 S2's file-wide function, 96 S4's `ast` walk, 97's decode table,
`read_blobs_at` in `tools/memory-tree/tree_lib.py` and `gen_map.py --write`; no item mints a second
implementation of any. `python tools/codebase-map/reuse_lookup.py "write a git blob without line ending
conversion"` ranked `git`, `write`, `write_text` and `run_git`, none a byte-preserving plant writer, and
`tools/govkit/matrix.py:440-465` is the precedent S3 copies the `newline` half of; no existing seam fits
beyond the fixture being extended.

Recall terms used: `python tools/memory-recall/query.py "how does the census fixture prove a planted ci file kept its bytes" --terms "census fixture plant blob kept write_bytes autocrlf crlf tree id ci_lines line break locator"`
