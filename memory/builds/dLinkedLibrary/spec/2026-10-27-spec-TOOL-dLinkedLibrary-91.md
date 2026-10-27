# TOOL-dLinkedLibrary-91 — the spec audit of units 81 to 86: its medium and low findings, batched

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 35 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |
| [2026-10-27-build-TOOL-dLinkedLibrary-87-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-87-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-90 |
| [2026-10-27-build-TOOL-dLinkedLibrary-91-deviation-911.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-91-deviation-911.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-87-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-87-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-90 |
| [2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-87-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-90 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 81 to 86
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md`) confirmed
19 MEDIUM and 11 LOW findings. BUILD-METHOD M4 promotes them into one batch unit, and this is it; each
finding is its own scope item below, by report id:

- MEDIUM: 2 (item M1), 3 and 32 (M2), 5 (M3), 6 and 29 (M4), 8 (M5), 13 and 34 (M6), 14 and 23 (M7),
  15 (M8), 18 (M9), 21 (M10), 22 (M11), 24 (M12), 28 (M13), 35 (M14), 36 (M15).
- LOW: 4 (L1), 7 and 25 (L2), 9 (L3), 11 (L4), 12 (L5), 16 and 26 (L6), 17 (L7), 19 (L8), 37 (L9).

Three items are the lower-grade half of a defect the report also binds higher or twice. M13 (id 28) is
H1's gap seen through 81's "Observed by" claims, and H1 is closed by `TOOL-dLinkedLibrary-87`, so the
item here builds only the record 87 leaves. L1 (id 4) is M7's conflict at the skeptic's low grade, and
L9 (id 37) is M11's selector at a low grade; all four ids are here. The findings land on six units, 81
to 86, so this unit repairs none in particular and builds after every unit of the build (order 35).

One unit and not two. The census items write `adopt_program.py` and `help/adopt.md`; the tooling items
write `tools/memory-tree/gotchas.py` and `tools/lib/resolve-python.test.sh`. Both halves add functions,
so both re-render the generated map with its generator, a shared generated index BUILD-METHOD M6's
clause 3 forbids across concurrent passes, and both write amendment lines into the same units'
acceptance ledgers. No split leaves two disjoint write sets.

## 2. Scope (IN)

Each item lands at the pass of the unit it amends, as §4 "Where each item lands" states.

### Units 81 and 82: the Azure `variables:` item forms

- **S1** — id 2, M1. 81 S4's first two trees nest no credential carrier: the `${{ if }}` item holds `-
  name: CONFIG` with `value: Release`, and the `${{ if }}` key holds `CONFIG: Release`, so only 81 S2's
  expression branch can fire on them and 81 AC1's reason is the one they read. Observed by AC1.
- **S2** — id 28, M13. 81 S2's unknown-key branch and S3's interim template refusal are observed by
  `TOOL-dLinkedLibrary-87` AC1 to AC3, and 81's acceptance ledger says so in an amendment line, so
  81 S3's "Observed by AC3" points at a criterion whose plant holds a template item. Observed by AC2.
- **S3** — id 7, L2. `help/adopt.md`'s census section carries the sentence "An Azure `variables:` item
  the census reads is `- name:`, `- group:`, `- template:` or a plain mapping key; any other item, a
  template expression or a flow-style value refuses the jobs its block applies to as `unreadable
  variables item <form>`, and a `- template:` item as `unreadable credentials template <path>`."
  Observed by AC3.
- **S4** — id 25, L2. That sentence lands at 81's pass: 81's files gain `help/adopt.md`, and the page at
  81's pass start holds no `unreadable variables item`. Observed by AC4.
- **S5** — id 11, L4. The map re-render that 80 and 86 each claimed as the build's last is this unit's,
  at order 35, covering every function units 81 to 90 add; and 82's arm covers AC4 beside AC1 to AC3, AC4
  being observed by the same plant, recorded in 82's ledger. Observed by AC5.

### Units 83 and 84: the GitLab indirection test

- **S6** — id 14, M7. One `<child>` rule, in 83 S2, for block and flow style alike: `<child>` is the
  innermost key, other than the block's own, that holds the token. In block style that is the key on the
  token's own line, or, for a line holding no key, the nearest key above it at a shallower indentation;
  in flow style the nearest key before the token at the token's own flow depth; empty when the token is
  the block's whole value. 84 AC3's `workflow:variables` follows from it unchanged. Observed by AC6.
- **S7** — id 23, M7. 86 S5 reads the same rule, and the rule gives one reason for one nesting in either
  style: the flow tree `default: { cache: { key: !reference [.ck, key] } }` over a hidden `.ck` reads as
  its block twin in S8 does. Observed by AC7.
- **S8** — id 4, L1. A depth-2 block plant under `default:`: `default:` over `cache:` over `key:
  !reference [.ck, key]`, beside two plain jobs, `test` running `npm test` and `lint` running `npm run
  lint`. It tells the innermost reading, `default:key`, from the direct-child reading, `default:cache`.
  Observed by AC8.
- **S9** — id 6, M4. 83's flow read across continuation lines is planted: a tree whose `default:` line
  is `default: { before_script:` and whose next line is `  !reference [.publish, script] }`, over a hidden
  `.publish` running `npm publish` and the two plain jobs, so `<child>` comes only from reading the flow
  mapping across the line break. Observed by AC9.
- **S10** — id 29, M4. 83 §5's unclosed flow collection is planted: a hidden `.base: &base` running
  `npm publish` and the two plain jobs, then, last in the file, the line `default: { image: node:20,`
  and below it, indented two spaces, `before_script: *base`, with no closing brace. The census reads it
  to the end of the file and does not raise. Observed by AC10.
- **S11** — id 24, M12. 83 S1's alias token opens a node: a `*` counts only at the start of a value, or
  after `[`, `{`, `,` or `- `, with whitespace allowed between, so a glob in a plain scalar is not an
  alias. Two plants hold globs and no token: `default: { before_script: [cp build/*.jar out] }`, and a
  top-level `cache: { paths: [vendor/*.so] }` read by 84 S2, each beside the two plain jobs. Observed by
  AC11.
- **S12** — id 3, M2. 84 S5 plants a token in four more blocks of 84 S1, one tree each beside two plain
  jobs: `image: *img` after a hidden `.img: &img node:20`; `services: !reference [.svc, services]`;
  `cache: *c` after a hidden `.c: &c` over `paths: [node_modules/]`; and `before_script: !reference [.p,
  script]`. Each reads `refused: opaque step <key> <block>:`, `<child>` empty by S6. Observed by AC12.
- **S13** — id 32, M2. 84 AC4's row-name list covers all eight blocks of 84 S1: no tree has a census row
  named `default`, `variables`, `workflow`, `image`, `services`, `cache`, `before_script` or
  `after_script`. Observed by AC13.
- **S14** — id 19, L8. 84 S2, 84 §10 and 83 S2 route a hit through `TOOL-dLinkedLibrary-71` S2's one
  file-wide function from 84's own pass, passing only the reason text, as 86 S7 words it; 76 S2 restates
  that refusal for `default:` and is not the seam. Observed by AC14.
- **S15** — id 12, L5. 84's pass follows 83's: 84 consumes 83's whole-value reading, and the shared
  order 25 does not sequence them. 84's pass starts only once 83's last pass commit is on the run
  branch. Observed by AC15.

### Unit 85: the `- run: |` step

- **S16** — id 5, M3. 85 S4's third plant gains, after the `- run: |` block holding `npm test` and before
  the step `- run: echo done`, the sibling key `        name: npm publish` at the key's column, column 8,
  so a dash-measured extent would take it as script. Observed by AC16.

### Unit 86: the census

- **S17** — id 8, M5. 86 S7's one-function claim is observed by structure, not by a reason string: an
  `ast` walk over `adopt_program.py` lists every function holding a `for` loop whose body stores a job's
  `refused` reason, and lists that function's call sites. Observed by AC17.
- **S18** — id 9, L3. 86 AC26's spec-text half is dropped, because the build pass never writes the text
  it reads; its ledger half stands. Observed by AC18.

### Unit 86: the harness and tooling items

- **S19** — id 35, M14. 86 S14's pure function takes the `/proc/<pid>/exe` reading as a path or as
  absent, absent being any `OSError` the readlink raises, `ENOENT`, `EACCES` or `ESRCH`. An absent `exe`
  falls back to S15's `comm` comparison; an absent `comm` too, or a pid gone before either read, returns
  `cannot look`. No `OSError` leaves the function. Observed by AC19.
- **S20** — id 15, M8. 86 AC19's argv is `bash -c "(echo s > <started>; sleep 3; echo x > <done>) &
  wait"`, so bash outlives the 1-second bound, and each run must report status `TIMEOUT` before any
  marker is read. Observed by AC20.
- **S21** — id 36, M15. 86 AC19 meets at a rendezvous, not a clock: after the bound it requires the
  `started` marker, failing `harness: grandchild never started` without it, then polls for the `done`
  marker every 100 ms for up to 5 seconds. Observed by AC21.
- **S22** — id 13, M6. 86 S25 gains a third container: a `-c '...'` argument, sliced from its opening
  quote to its closing quote, with a `"$VAR"` concatenated before it read as that variable's heredoc in
  the same file. The hosts are `tools/run-gates/run-gates.sh:2740`, in the `-c` opened at `:2711`
  after `"$RKD_PROGRAM"`, whose body is the `<<'RKD'` heredoc at `:178-217`; `run-gates.sh:4972`, in the
  `-c` opened at `:4959`; and `tools/run-gates/run-gates.test.sh:631` and `:669`, in the `-c` arguments
  opened at `:629` and `:667`. Observed by AC22.
- **S23** — id 34, M6. A host whose container the slicer does not recognise is printed as unread and
  fails the read, never skipped; and 86 AC21's staged red includes a `-c` host. Observed by AC23.
- **S24** — id 18, M9. 86 S25 slices a heredoc with `extract_heredoc_body`
  (`tools/gate-lint/sh_hygiene.py:274`), called by `python -I` with `tools/gate-lint` on `sys.path`, and
  finds the runbook's fenced program as the lines `unfenced_lines` (`tools/memory-tree/tree_lib.py:149`)
  does not yield; it mints no slicer of its own. Observed by AC24.
- **S25** — id 16, L6. 86 S20's Readers line is the set its stated grep prints, the
  `2026-10-27-build-TOOL-dLinkedLibrary-86-promoted-fix-return.md` record included, DERIVED at 86's pass
  and written into 86's ledger as an amendment line. Observed by AC25.
- **S26** — id 26, L6. That amendment line names the grep it ran, `git grep -l` for the phrase S20 quotes,
  and says that 80 AC1 carries the phrase wrapped across `2026-10-27-spec-TOOL-dLinkedLibrary-80.md`
  lines 256 and 257, so the grep does not print 80's spec and the line does not list it as a hit.
  Observed by AC26.
- **S27** — id 22, M11. 86 S27 moves the memory-tree carriers with `python tools/govkit/govkit.py
  selfcheck --fix`, whose writer `write_version_carriers` (`tools/govkit/govkit.py:801`) rewrites the set
  `derive_marker_basis` (`:767`) derives, `*.test.sh` excluded, and then the kit's `[[regenerate]]`
  render; the fixture marker in `tools/memory-tree/check-verdict-epoch.test.sh:118` is never rewritten.
  Observed by AC27.
- **S28** — id 37, L9. 86 S27's selector is `git grep -l -E 'gov:kit memory-tree@[0-9]'` over its
  pathspec with `':!*.test.sh'`, matching S28's: a carrier holds a versioned marker, not the bare prefix.
  Observed by AC28.
- **S29** — id 21, M10. 86 AC23's codebase-map half reads the real carriers: `git grep -h -o -E
  'codebase-map@[0-9][0-9.]*[0-9]' -- tools memory/map/generated`, which spans `map_lib.py` and the four
  renders under `memory/map/generated/`, prints one distinct value equal to `KIT_CODEBASE_MAP_VERSION`
  (`tools/codebase-map/map_lib.py:49`). Observed by AC29.

### Across units 81, 83, 84 and 86

- **S30** — id 17, L7. Each stale cite is read by section and criterion id, with its line PINNED at base
  on 2026-10-27: 84's "79 S1's GitLab row" is `2026-10-27-spec-TOOL-dLinkedLibrary-79.md:43`; 83's and
  84's 76 §1 example is `2026-10-27-spec-TOOL-dLinkedLibrary-76.md:25-26`; 86's 76 AC2 is `76.md:125-127`;
  86's 77 AC1 is `2026-10-27-spec-TOOL-dLinkedLibrary-77.md:123-126`; 81's 79 S2 is `79.md:47-54`. Each
  of those units' ledgers carries the corrected cite in an amendment line. Observed by AC30.

## 3. Non-goals (OUT)

- The HIGH findings of the same audit: units 87 to 90, one per id.
- Re-opening any unit's design: each item corrects a plant, a criterion's observation, a reading rule a
  spec left ambiguous, or a record.
- A gate per left-shift the report proposes: every item lands on an existing arm, plant, comment, render
  or record.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-81` — S4's plant trees, S3's "Observed by" claim, §5's user docs, its Rollout and §4's 79 cite, which S1 to S5 and S30 correct (ids 2, 28, 7, 25, 11, 17)
- **consumes-from** `TOOL-dLinkedLibrary-82` — S2's template reason and §7's `covers` list, which S3 and S5 name and complete (ids 7, 11)
- **consumes-from** `TOOL-dLinkedLibrary-83` — S1's whole-value reading and alias search, S2's `<child>` and seam, and §4's 76 cite, which S6 to S11, S14, S15 and S30 settle and plant (ids 14, 23, 4, 6, 29, 24, 19, 12, 17)
- **consumes-from** `TOOL-dLinkedLibrary-84` — S2's reason and seam, S5's plants, AC3, AC4, its order and §4's 79 cite, which S6, S12 to S15 and S30 settle and plant (ids 14, 3, 32, 19, 12, 17)
- **consumes-from** `TOOL-dLinkedLibrary-85` — S4's third plant, which S16 completes (id 5)
- **consumes-from** `TOOL-dLinkedLibrary-86` — S5, S7, S14 to S16, S20, S22, S25, S27, S28 with AC6, AC19, AC21, AC23 and AC26, and §4's cites, which S7 and S17 to S30 correct (ids 23, 8, 9, 35, 15, 36, 13, 34, 18, 16, 26, 22, 37, 21, 17)
- **consumes-from** `TOOL-dLinkedLibrary-87` — the plants and criteria that observe 81 S2 and S3, which S2 records in 81's ledger (id 28)
- **consumes-from** `TOOL-dLinkedLibrary-88` — the `flow` item form, which S3's page sentence names (ids 7, 25)
- **hands-off** `TOOL-dLinkedLibrary-95` — S11's node-start alias positions and S6's `<child>` rule, which unit 95 plants one position each and widens for a token inside a flow sequence; §5's risks line, that existing trees hold a real alias in each position, is false, and unit 95's trees are the ones it names (id 23)
- **hands-off** `TOOL-dLinkedLibrary-96` — S2 to S4, S17, S18, S22, S24 and S29 with AC4, AC17, AC18, AC22 and AC29, which unit 96 re-lands at 87's and 88's passes and restates: S2's line at 87's pass, S3's sentence at 88's, AC17's predicate, AC18's scoped grep, the runbook host and AC29's constant (ids 2, 3, 19, 10, 9, 6, 13)

## 4. Design

### Where each item lands

Units 81 to 88 are unbuilt and sit at orders 25 to 33, ahead of this unit. Each reads its hands-off edge
to this unit, builds the item that lands on it as part of its own pass, and writes an amendment line in
its acceptance ledger citing this unit and the item, as 86 S19 states for an amended criterion. This
unit's own pass, the last of the build, observes every item at the tip with AC1 to AC30, completes any
item an earlier pass left, and re-renders the generated map.

| Lands at the pass of | Items |
|---|---|
| `TOOL-dLinkedLibrary-81` | S1 to S4, S30 |
| `TOOL-dLinkedLibrary-82` | S5's covers half |
| `TOOL-dLinkedLibrary-83` | S6, S8 to S11, S14, S30 |
| `TOOL-dLinkedLibrary-84` | S6, S11's `cache:` plant, S12 to S15, S30 |
| `TOOL-dLinkedLibrary-85` | S16 |
| `TOOL-dLinkedLibrary-86` | S7, S17 to S30 |
| this unit | S5's re-render, and every observation |

### Evidence

- S1: 81 S4 nests `- group: release-vars` and `NUGET_API_KEY: $(nugetKey)`; 79 S2
  (`2026-10-27-spec-TOOL-dLinkedLibrary-79.md:47-54`) reads `- group:` at any level and the word `key`.
- S6 to S8: 76 S2 (`2026-10-27-spec-TOOL-dLinkedLibrary-76.md:38-41`) says "the key of `default:` that holds
  it"; 84 AC3 expects `workflow:variables`; every 76 plant holds its token one level down.
- S12, S13: 84 S5 plants a token only in `variables:` and `workflow:`, and 84 AC4 names four rows.
- S15: `tools/memory-tree/check-memory-hygiene.sh:2813` tests a consumes-from order with a strict `>`, so
  equal orders pass.
- S20: `tools/run-gates/regen.py:297` waits on the bash process alone, and the report's skeptic measured
  status 0 in 0 s for the argv with no `wait`.
- S22: `git grep -n '^# >>> resolve_prefix_token'` prints `run-gates.sh:2740` and `:4972` and
  `run-gates.test.sh:631` and `:669`; `run-gates.sh:177-178` reads the `RKD` heredoc into `RKD_PROGRAM`.
- S24: `extract_heredoc_body`'s docstring records the `.strip()` early-terminator bug and the CRLF
  terminator it fixed.
- S25, S26: `git grep -l` for the phrase S20 quotes printed, on 2026-10-27 at base, the 86 spec, the
  86 fix-return record and the 75 spec-audit review, and not 80's spec.
- S27: `derive_marker_basis` (`tools/govkit/govkit.py:767-775`) excludes `*.test.sh` because
  `check-verdict-epoch.test.sh:118` holds `memory-tree@1.5` inside a `sed`.
- S28: the versioned selector with the exclusion printed nine files on 2026-10-27 at base (PINNED), the
  four dogfood carriers under `memory/`, the four kit templates and `check-memory-hygiene.sh`.
- S29: the `gov:kit codebase-map@` grep matches only `map_lib.py:47`; the four renders spell
  `codebase-map@1.30` with no prefix.

### Inventory

No identifier is minted. S17's walk reads a field the census already stores, and S21's `started` and
`done` markers are scratch files of one run.

### Rollout

The plants of S1 and S8 to S16 add cases to `adopt_program.py`, and units 87 to 90 add functions after
86's re-render at order 33, so this pass re-renders the generated map with `python
tools/codebase-map/gen_map.py --write` where its `--check` exits 1.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1, S6 to S17
- `help/adopt.md`: S3, S4
- `tools/memory-tree/gotchas.py`: S19 to S21
- `tools/lib/resolve-python.test.sh`: S22 to S24
- `memory/builds/dLinkedLibrary/build/`: the amendment lines of S2, S5, S15, S18, S25 to S27 and S30
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: the Rollout re-render

### Alternatives rejected

- **One unit per finding.** M4 forbids it.
- **Folding each item into its unit's spec.** The owner's 2026-10-05 ruling promotes every minor and
  folds none.
- **S6 by the direct-child reading.** It changes 84 AC3 to `workflow:rules`, a criterion already
  written; §8 F2 records the veto.
- **S11 by excluding quoted strings only.** A glob in a plain scalar carries no quotes; the node-start
  rule is YAML's own.
- **S24 by a new slicer.** It would re-learn the two terminator bugs `extract_heredoc_body` already fixed.

## 5. Production-readiness checklist

- security — S1, S8 to S13 and S16 make the census's refusals observable on plants that discriminate them;
  S11 stops a glob refusing a file; S19 stops an unreadable `exe` reading as a missing grandchild.
- perf / scale — S22 adds one slice per `-c` host, four at base.
- error / empty / loading states — S10 reads an unclosed flow collection to the end of the file; S19
  and S23 each fail naming the cause.
- observability — each refusal names its key and block; S23 names an unread host.
- risks — S11 narrows the alias search, which a plant with a real alias in each position keeps honest
  through 83's and 84's existing trees.
- testing — AC1 to AC30 by plant, scratch copy, pure-function call, `ast` walk and probe.
- migration — S27's carrier move, in 86's commit.
- user docs — `help/adopt.md`, S3 and S4.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both jobs of 81's
  `${{ if }}` item tree and of its `${{ if }}` key tree read `refused: unreadable variables item
  expression`; over a scratch copy with 81's expression branch removed, run by `python -I`, they read
  `importable`.
  Red when: a nested line trips 79's credential rule, so another reason fires or the jobs stay refused.
- **AC2** — When `grep -n 'TOOL-dLinkedLibrary-91'` runs over 81's acceptance ledger, it prints the line
  naming `TOOL-dLinkedLibrary-87` AC1 to AC3 as the observation of 81 S2's unknown-key branch and S3.
  Red when: 81 S3 is certified by a criterion that exempts its template item.
- **AC3** — When `grep -n 'unreadable variables item'` runs over the help page `adopt.md` (its path in Files
  touched) at this tip, it prints S3's sentence, which also names `flow` and `unreadable credentials
  template`.
  Red when: a census refusal ships with no line on the page.
- **AC4** — When the same grep runs over the page at 81's pass start, read with `git show`, it prints
  nothing, and over the page at 81's last pass commit it prints S3's sentence.
  Red when: the sentence arrives after the pass that adds the refusal.
- **AC5** — When `python tools/codebase-map/gen_map.py --check` runs at this tip it exits 0; and `grep -n
  'AC4'` over 82's acceptance ledger prints AC4 observed by 82's arm, with an amendment line citing this
  unit.
  Red when: a function units 81 to 90 add is missing from the map, or 82 AC4 is tied to no arm.
- **AC6** — When the plant runs, both plain jobs of 84's `workflow:` tree read `refused: opaque step
  !reference workflow:variables`.
  Red when: 83 S2's rule and 84 AC3 disagree on the key the reason names.
- **AC7** — When the plant runs, both plain jobs of S7's flow tree read `refused: opaque step !reference
  default:key`, the reason AC8 requires of its block twin.
  Red when: one nesting reads two reasons by style.
- **AC8** — When the plant runs, both plain jobs of S8's depth-2 block tree read `refused: opaque step
  !reference default:key`.
  Red when: the direct-child reading prints `default:cache`.
- **AC9** — When the plant runs, both plain jobs of S9's split flow tree read `refused: opaque step
  !reference default:before_script`; over a scratch copy whose flow read stops at the end of the
  `default:` line, they do not.
  Red when: the continuation line is read without its flow mapping.
- **AC10** — When the plant runs, it exits 0 and both plain jobs of S10's unclosed tree read `refused:
  opaque step alias default:before_script`.
  Red when: the reader stops at the unclosed brace or raises.
- **AC11** — When the plant runs, both plain jobs of each glob tree read `importable`, while 83's
  `default: *base` tree still reads `refused: opaque step alias default:`.
  Red when: a glob in a plain scalar reads as an alias.
- **AC12** — When the plant runs, both plain jobs of the four S12 trees read, in turn, `refused: opaque step
  alias image:`, `refused: opaque step !reference services:`, `refused: opaque step alias cache:` and
  `refused: opaque step !reference before_script:`.
  Red when: a walk hardcoded to `variables:` and `workflow:` leaves a block's token unread.
- **AC13** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, no tree's
  output holds a census row named `default`, `variables`, `workflow`, `image`, `services`, `cache`,
  `before_script` or `after_script`, the eight blocks S13 lists.
  Red when: a job-wide block is graded as a job.
- **AC14** — When `python -I -c` walks, with `ast`, the `adopt_program.py` of 84's last pass commit, read
  with `git show`, 84's block hits call the one function 71 S2's `include:` hit calls.
  Red when: 84 builds a second file-wide loop before 86 merges them.
- **AC15** — When `git merge-base --is-ancestor` runs with 83's last pass commit and 84's first, each
  found by `git log --format=%H --grep` on its `build(dLinkedLibrary): <unit> ` subject, it exits 0.
  Red when: 84's pass ran before 83's reading existed.
- **AC16** — When the plant runs, the job whose `- run: |` block is followed by `name: npm publish`
  reads `importable`; over a scratch copy measuring the extent from the dash it reads `refused: npm
  publish`.
  Red when: the staged break cannot turn 85 AC3 red.
- **AC17** — When `python -I -c` walks `adopt_program.py` with `ast` at this tip, it prints one function
  holding a `for` loop that stores a job's `refused` reason, and its call sites for 71 S2's `include:`, 76
  S2's `default:` and 84 S2's blocks; over a scratch copy inlining a second such loop for `default:`, it
  prints two.
  Red when: a second loop over a file's jobs assigns a file-wide refusal.
- **AC18** — When `grep -c 'census refuse a ci'` runs over 86's acceptance ledger it prints 0, and `grep -n
  'TOOL-dLinkedLibrary-91'` over it prints the line grading AC26 by its ledger half alone.
  Red when: a criterion half that reads the spec's own text is certified.
- **AC19** — When `python -I -c` imports `gotchas.py` and calls S19's function with literal readings, an
  absent `exe` with `comm` `python3.12` against an executable whose basename is `python3.12` matches; an
  absent `exe` with `comm` `sleep` does not; an absent `exe` and an absent `comm` return `cannot look`.
  Red when: an `OSError` escapes, or an unreadable `exe` reads `grandchild not visible`.
- **AC20** — When `python -I -c` loads a scratch copy of `tools/run-gates/regen.py` and calls `run_command`
  with S20's argv under a 1-second bound, it returns status `TIMEOUT`, for the `run_tree_kill` copy and
  for the `proc.kill()` copy alike.
  Red when: bash exits before the bound and the run returns 0 with no kill.
  cost: about 12 seconds for the two runs and their polls.
- **AC21** — When the same runs complete, each finds its `started` marker; the `run_tree_kill` copy finds
  no `done` marker within the 5-second poll and the `proc.kill()` copy finds one; and a run whose argv is
  `bash -c "sleep 3"` fails `harness: grandchild never started`.
  Red when: a grandchild that never started passes the `run_tree_kill` arm.
- **AC22** — When S24's free-name read runs by hand with `python -I` at this tip, it prints each of S22's
  four hosts as read and names no unbound name in them.
  Red when: a `-c` host is skipped, or the `:2711` literal is read without the `RKD` heredoc.
- **AC23** — When the same read runs over a scratch copy of the gate runner, the file holding S22's
  first two hosts, whose `resolve_prefix_token` literal in the `:2711` host loses an import, it names
  that name, the row and the file; over a scratch host holding the block in a container no rule slices, it prints the host as unread and exits non-zero.
  Red when: an unrecognised container passes by being skipped.
- **AC24** — When `grep -n 'extract_heredoc_body\|unfenced_lines'` runs over the parity suite (its path in
  Files touched) it prints the slicer's calls; over a scratch heredoc host holding an indented line
  equal to its tag and a CRLF terminator, the read still names a free name planted below that line.
  Red when: a rebuilt slicer cuts the body short and hides the name.
- **AC25** — When `git grep -l` for the phrase S20 quotes runs at 86's last pass commit, every file it
  prints is named in 86's ledger amendment line, the fix-return record included.
  Red when: the Readers line omits a file the grep prints.
  figure: DERIVED at 86's pass from the grep.
- **AC26** — When `grep -n 'git grep -l'` runs over that amendment line, it prints the grep and the note
  that 80 AC1 wraps the phrase across lines 256 and 257, and the line lists 80's spec as no hit.
  Red when: the line claims a file the stated grep does not print.
- **AC27** — When `grep -n 'memory-tree@1.5'` runs over the verdict-epoch suite S27 names at this tip, it
  prints the fixture line, and `grep -n 'selfcheck --fix'` over 86's ledger prints the
  carrier move.
  Red when: the move rewrote the decoy fixture or bypassed the carrier writer.
- **AC28** — When S28's selector runs at this tip, every file it prints holds one memory-tree marker equal
  to `KIT_MEMORY_TREE_VERSION`, and it prints no suite fixture file.
  Red when: the selector takes in a fixture or a file holding only the prefix.
  figure: DERIVED at this pass; nine files at base, PINNED 2026-10-27.
- **AC29** — When S29's grep runs at this tip it prints one distinct value, equal to the constant; in a
  scratch clone under `%TEMP%/cm91` with only the constant moved, it prints two.
  Red when: the criterion reads no carrier the renders hold.
- **AC30** — When `sed -n` prints each line S30 pins, it shows the cited row, section or criterion: 79's
  GitLab row at `:43`, 76 §1's `default: {` example at `:25-26`, 76 AC2 opening at `:125`, 77 AC1
  opening at `:123` and 79 S2 opening at `:47`; and `grep -n 'TOOL-dLinkedLibrary-91'` over the ledgers
  of 81, 83, 84 and 86 prints each corrected cite.
  Red when: a cite lands on a different row or criterion.
  figure: PINNED at base, 2026-10-27.

## 7. Gates

`gotchas selftest` · `policy fixtures` · `python resolver (behaviour + inline parity + idiom ban)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC6 AC7 AC8 AC9 AC10 AC11 AC12 AC13 AC16 · the `ci-census` plant's de-credentialed expression trees, depth-2 block and flow trees, split and unclosed flow trees, glob trees, four job-wide token trees and key-column step, the failing case staged by the direct-child reading, a one-line flow read, a substring alias search and a dash-measured extent · none
New arm: tools/memory-tree/gotchas.py · covers AC19 · the absent-`exe` and absent-both readings, the failing case staged by a readlink `OSError` reaching `realpath` · none
New arm: tools/lib/resolve-python.test.sh · covers AC22 AC23 AC24 · the free-name read over every `-c` host, the failing case staged by a `-c` literal losing an import and an indented tag line · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. (b) splits clauses the
  repaired units carry whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — Which key does `<child>` name for a token two or more levels below its block?** Options: (a) the
  innermost key holding the token, which 83 S2's flow rule already gives; (b) the block's direct child,
  76 S2's literal wording, with 84 AC3 changed to `workflow:rules`. (b) fails 84 AC3 as written; veto 1
  discards it. RESOLVED (agent, 2026-10-27, delegated): (a), S6. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 81 to 86, 19 MEDIUM and 11 LOW
  findings batched in one unit.
- rev-2 · 2026-10-27 · §3 · the hands-off edges to units 95 and 96, the mirrors of the
  consumes-from edges their specs declare, promoted from the spec audit of units 87 to 91;
  no scope or criterion moved.

## 10. Reuse audit

Every item extends the seam its finding names: the census's reader and plants in
`tools/memory-tree/adopt_program.py`, 71 S2's file-wide refusal, 83 S2's flow `<child>` rule,
`extract_heredoc_body` in `tools/gate-lint/sh_hygiene.py`, `unfenced_lines` in
`tools/memory-tree/tree_lib.py`, the parity loop of `tools/lib/resolve-python.test.sh`, `selfcheck --fix`
with `derive_marker_basis` in `tools/govkit/govkit.py`, and 80 S13's pidfile rendezvous; no item mints a
second implementation of any. `python tools/codebase-map/reuse_lookup.py "slice a heredoc body from a
shell file"` ranked `slice`, `corpus_files`, `ask_filed_in` and `asks_filed_in` and did not surface
`extract_heredoc_body`, which `grep -n 'def extract_heredoc_body'` finds at `sh_hygiene.py:274`; the
lookup's miss is recorded here and the grep is the evidence S24 rests on.

Recall terms used: `python tools/memory-recall/query.py "how does the census refuse an azure variables item form it cannot read" --terms "census ci-job azure variables item deny-by-default refused unknown key expression template plant"`, and for the tooling items `python tools/memory-recall/query.py "how is a heredoc or fenced program sliced before a free name read" --terms "heredoc extract_heredoc_body unfenced_lines parity loop resolve_prefix_token free name symtable host slice"`
