# TOOL-dLinkedLibrary-86 — the spec audit of units 75 to 80: its medium and low findings, batched

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 33 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |
| [2026-10-27-build-TOOL-dLinkedLibrary-86-deviation-861.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-86-deviation-861.md) | deviation | — |
| [2026-10-27-build-TOOL-dLinkedLibrary-86-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-86-promoted-fix-return.md) | research | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-86-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-86-1-spec-writer.md) | journal | TOOL-dLinkedLibrary-1 |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-86-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-86-promoted-fix-brief.md) | research | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-81-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 75 to 80
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md`) confirmed
22 MEDIUM and 10 LOW findings. BUILD-METHOD M4 promotes them into one batch unit, and this is it; each
finding is its own scope item below, by report id:

- MEDIUM: 1 (item M1), 2, 16, 22 and 40 (M2), 3 (M3), 4 (M4), 5 (M5), 12 (M6), 14 (M7), 15 and 39 (M8),
  17 (M9), 23 (M10), 25 (M11), 26 (M12), 27 (M13), 28 (M14), 29 (M15), 37 (M16), 38 (M17), 41 (M18).
- LOW: 6 and 18 (L1), 7 (L2), 8, 19 and 42 (L3), 10 (L4), 11 (L5), 21 (L6), 24 (L7).

Four items are the lower-grade half of a defect the report also binds higher or twice. M1 is H4's, closed
by `TOOL-dLinkedLibrary-85`, and M5 is H3's, closed by `TOOL-dLinkedLibrary-84`; each item here builds
only what its higher-grade unit leaves. L4 is M13's and L5 is M10's, all four here. The findings land on
ten units, so this unit repairs none in particular and builds after every unit of the build (order 33).

One unit and not two. The census items write `adopt_program.py` and `help/adopt.md`, and the item for id
28 reads that page as its acceptance input, which BUILD-METHOD M6's clause 2 forbids across concurrent
passes; and the version items of ids 27 and 10 move the memory-tree kit that `adopt_program.py` ships in.
No split leaves two disjoint write sets.

## 2. Scope (IN)

### The CI census: units 76 to 79 and their repairs

- **S1** — id 1, M1. 77 AC1's GitHub plant is a list-item step: the `ci-census` plant gains a GitHub job
  whose step is `      - run: !!str |2-` holding `npm publish`, read by unit 85's third header form.
  Observed by AC1.
- **S2** — id 17, M9. The census reads each line of a CI file with its trailing CR stripped, before 77's
  header, 73's extent, 78 S2's continuation and every refusal pattern apply, so a CRLF file reads as its
  LF twin. Observed by AC2.
- **S3** — id 29, M15. 78 S3's split-scalar refusal skips blank and comment-only continuation lines and
  reads only the line keys of 63 S1, so `- npm test` followed by a deeper `# note` reads `importable`; and
  `help/adopt.md`'s census section names the refusal `unreadable multi-line scalar <key>` in one sentence.
  Observed by AC3 and AC4.
- **S4** — id 8, L3. A line carrying a merge key and an alias at once, `<<: *publish`, reports `<<`: one
  key per line, the merge key first. Observed by AC5.
- **S5** — id 42, L3. `<child>` of 76 S2 for an indirection key directly under `default:` is that key
  itself, so `<<: *publish` under `default:` reads `default:<<`. Observed by AC5.
- **S6** — id 19, L3. 76 AC2's plain job reads the full string `refused: opaque step << default:<<`, the
  form 76 S2 states. Observed by AC5.
- **S7** — id 24, L7. A `default:` hit, and each hit unit 84 adds, routes through `TOOL-dLinkedLibrary-71`
  S2's file-wide refusal, one function in `adopt_program.py` that both call; only the reason text is the
  caller's. Observed by AC6.
- **S8** — id 37, M16. Each refusing tree of 76 S4 and 79 S4 holds two plain jobs, one before and one after
  the block where YAML allows, and 79's refusing Azure stages hold two jobs each; the refusal is required
  on both. Observed by AC7.
- **S9** — id 5, M5. The global `after_script:` that unit 84 S3 reads is planted: one tree whose top-level
  `after_script: [npm publish]` sits beside two plain jobs, and one whose top-level `after_script:
  !reference [.cleanup, script]` does. `help/adopt.md`'s census section carries the sentence "A top-level
  `variables:`, `workflow:`, `image:`, `services:`, `cache:`, `before_script:` or `after_script:` applies
  to every job: its script lines are read for every job, and an indirection in it refuses every job in
  the file." Observed by AC8 and AC9.

### The reuse-tag sweep: unit 75

- **S10** — id 38, M17. 75 S2 resolves a tag only when the remainder after `<stem>-` matches
  `^[1-9][0-9]*$`; otherwise the tag is unresolved and named. Every rewrite 75's acceptance ledger lists is
  re-read at this pass against that rule, and one whose remainder is not a part number is restored to its
  original tag and named. Observed by AC10.
- **S11** — id 21, L6. A tag inside a `memory/map/features/*.reuse.toml` part is `unit.reuse.<file stem>`,
  read through `check_reuse_entries`' own stem reader (`TOOL-dLinkedLibrary-1` S2, as
  `TOOL-dLinkedLibrary-38` S1 reads a part's stem); the longest-stem rule reads only tags outside part
  files. A part 75 rewrote to another value is rewritten to its file stem at this pass. Observed by AC11.
- **S12** — id 25, M11. The `hyphen-tag` plant's tag is composed at run time from its parts, `'unit.reuse.'
  + stem + '-1'`, so no tracked line under `tools` spells a hyphenated tag and 75 AC1's predicate keeps
  its population free of the fixture. Observed by AC12.
- **S13** — id 7, L2. 75 AC2's population is recorded: the count of tags 75 S1's predicate printed at 75's
  pass start, read from that pass's first parent with `git show`, zero allowed, is written in this unit's
  acceptance ledger. Observed by AC13.

### The minors of unit 80

- **S14** — id 2, M2. 80 S12's POSIX arm takes no image from `/proc/<pid>/cmdline`. Where `/proc` exists it
  compares `os.path.realpath` of `/proc/<pid>/exe` with `os.path.realpath(sys.executable)`. The comparison
  is one pure function of the observed readings and `sys.executable`, so a criterion can call it on
  literal strings. Observed by AC14.
- **S15** — id 16, M2. Where `/proc` is absent it compares `os.path.basename` of `ps -o comm= -p <pid>`
  with `os.path.basename(sys.executable)`, unresolved; a `comm` of exactly 15 characters matches when it
  is the first 15 characters of that basename, which is the kernel's truncation. It never compares `comm`
  with the basename of the realpath. Observed by AC14.
- **S16** — id 22, M2. A POSIX host where neither probe can look, no `/proc` and no runnable `ps`, or `ps`
  exiting non-zero, fails the case `harness: cannot look`, never `grandchild not visible`; the POSIX arms
  carry the word UNVERIFIED in their comment, as `read_pid_image` does. Observed by AC15.
- **S17** — id 40, M2. The case's comment cites `read_pid_image` (`tools/unattended/lib-unattended.sh:595-619`)
  for the Windows half only, and states the POSIX rule as its own, naming where it departs from
  `read_pid_image`'s `kill -0` and `ps -o comm=` arm. Observed by AC15.
- **S18** — id 3, M3. 80 S23's guard is a `decision_rubric.py --fixture --plant no-local-row-predicate`
  case, the fixture mode `TOOL-dLinkedLibrary-1` defines (`2026-10-26-spec-TOOL-dLinkedLibrary-1.md:132`),
  run by the build-index selftest arm unit 1 declares; the module gains no `--selftest` mode. Observed by
  AC16.
- **S19** — id 4, M4. An earlier unit's criterion that a later item amends is graded at the earlier pass
  as amended, with an amendment line in that unit's acceptance ledger: `TOOL-dLinkedLibrary-74`'s pass
  grades its AC12 over `-- tools skills`, as 80 S1 scopes it, citing this item;
  `TOOL-dLinkedLibrary-64`'s pass lands no `resolve_bash` call of its own, re-observing unit 67's. At
  this pass both ledgers carry their line, and `tools/memory-tree/gotchas.py` holds exactly one
  `resolve_bash` call, the one inside `resolve_observed_argv`. Observed by AC17.
- **S20** — id 18, L1. 80 AC1's "lists no file under `memory/`" half is dropped, and the scoped listing
  carries a floor: `git grep -l '^# >>> region_py' -- tools skills` is non-empty and lists every kit copy
  74 S16 names. Observed by AC18.
  **Readers:** by name: `2026-10-27-spec-TOOL-dLinkedLibrary-80.md` (AC1, the half's text) and
  `2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md` (L1, which quotes it), the only files besides
  this spec that a git grep over the tree for its phrase prints.
  by value: NO VALUE READERS, because the half is criterion prose that no code, gate or fixture reads,
  and 80's acceptance ledger, the one record that would grade it, is not written until 80's pass.
- **S21** — id 6, L1. The record red is shown by the unscoped `git grep -l '^# >>> region_py'`, which lists
  unit 18's spec record, and no path it prints outside `tools` and `skills` is a site S20 lists. Observed
  by AC18.
- **S22** — id 12, M6. 80 AC22's staged red is the kill not reaching the grandchild: the planted argv's
  grandchild writes a marker file after its sleep, and the scratch copy calling `run_tree_kill` leaves no
  marker while the copy calling `proc.kill()` leaves one. No elapsed-time arm is read, because `run_command`
  writes to a file (`tools/run-gates/regen.py:289`). Observed by AC19.
- **S23** — id 14, M7. 80 S10's floor figure is counted off the arms: each of 74's arm calls traced
  through its suite's helper to the assertions it executes, the micro-format suite's `arm` making one
  `say_ok` or `say_fail` call per call and the canary counting `n=$((n+1))` per executed check, with
  `HAVE_TIMEOUT`-gated arms excluded as the canary's floor comments exclude them. Each raise carries a
  comment naming the arms counted, in the canary's convention. Observed by AC20.
- **S24** — id 15, M8. 80 S11's population is quoted from the parity loop it extends,
  `tools/lib/resolve-python.test.sh:221-241`: every host the loop reads, `'*.sh'`, `'*.py'`,
  `'.githooks/*'` and `WIRE-INTO-PROJECT.md`, holding a block of a Python-language parity row. Observed by
  AC21.
- **S25** — id 39, M8. In a host that is not `*.py`, the program holding the block is sliced first, a
  shell heredoc's body or the runbook's fenced block, and `symtable` runs over that program as the host,
  so a free name the program never binds is named with its row, file and line. Observed by AC21.
- **S26** — id 26, M12. When 80 S9 moves the roles marker in `tools/roles/SKILL.template.md`, the render
  `.claude/skills/build/SKILL.md` moves with it by `bash tools/roles/adopt-roles.sh --scaffold`, and 80
  AC5's grep reads `-- tools help .claude`. Observed by AC22.
- **S27** — id 27, M13. When 80 S4 moves `KIT_MEMORY_TREE_VERSION`
  (`tools/memory-tree/check-memory-hygiene.sh:69`), every carrier `git grep -l 'gov:kit memory-tree@' --
  tools help memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides` lists moves with it, the four
  dogfood renders by the kit's `[[regenerate]]` row, `bash tools/memory-tree/adopt-memory-tree.sh
  --render`, which rewrites their marker line and nothing else. Observed by AC23.
- **S28** — id 10, L4. 80 AC5's kit list gains `memory-tree` and `codebase-map`
  (`KIT_CODEBASE_MAP_VERSION`, `tools/codebase-map/map_lib.py:49`), and its grep excludes the test
  fixtures, `':!*.test.sh'`, so `memory-tree@1.5` at `tools/memory-tree/check-verdict-epoch.test.sh:118`
  is out of its population. Observed by AC23.
- **S29** — id 28, M14. 80 AC24 is anchored to 80 S30's own text: its baseline is the page at 80's pass
  start, after 76 and 79 wrote theirs, and it reads the job-level phrasing S30 adds. Observed by
  AC24.
- **S30** — id 41, M18. 80 S4's range fails naming the missing bound when no commit's subject opens
  `build(dLinkedLibrary): TOOL-dLinkedLibrary-74 `, or 74's last pass commit cannot be found: never green,
  never a fallback to 5fede642. The re-observation prints the two SHAs it compared. Observed by AC25.
- **S31** — id 23, M10. The recall query for each subject of 75 and 80, recorded in §10 below, is re-run at
  this pass and every record it surfaces is reconciled with the scope items in this unit's acceptance
  ledger. Observed by AC26.
- **S32** — id 11, L5. The ledger names the query and terms used for each subject, so a reader can tell
  what was searched; this spec's §10 spells no line of the CI-census query. Observed by AC26.

## 3. Non-goals (OUT)

- The HIGH findings of the same audit: units 81 to 85, one per id.
- Re-opening any unit's design: each item corrects the built code, a plant, a criterion's observation or
  a record, or states how an earlier pass grades an amended criterion.
- A gate per left-shift the report proposes: every item lands on an existing arm, plant, comment, render
  or record.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-75` — S1's predicate, S2's rewrite, S3's plant and AC2's ledger, which S10 to S13 correct (ids 38, 21, 25, 7), and §10's recall line, which S31 and S32 replace (ids 23, 11)
- **consumes-from** `TOOL-dLinkedLibrary-76` — S2's reason and file-wide refusal and S4's plant trees, which S4 to S8 complete (ids 8, 42, 19, 24, 37)
- **consumes-from** `TOOL-dLinkedLibrary-77` — AC1's GitHub plant and the header reader, which S1 and S2 complete (ids 1, 17)
- **consumes-from** `TOOL-dLinkedLibrary-78` — S2's continuation and S3's split-scalar refusal, which S2 and S3 correct (ids 17, 29)
- **consumes-from** `TOOL-dLinkedLibrary-79` — S4's plant trees, which S8 gives two jobs each (id 37)
- **consumes-from** `TOOL-dLinkedLibrary-80` — S1, S4, S9 to S12, S23, S28 and S30 with their criteria, and §10's recall line, which S14 to S32 correct (ids 2, 16, 22, 40, 3, 4, 18, 6, 12, 14, 15, 39, 26, 27, 10, 28, 41, 23, 11)
- **consumes-from** `TOOL-dLinkedLibrary-84` — S3's global `after_script:` reading, which S9 plants and documents (id 5)
- **consumes-from** `TOOL-dLinkedLibrary-85` — the third header form, which S1's `- run: !!str |2-` plant is graded against (id 1)
- **consumes-from** `TOOL-dLinkedLibrary-74` — AC12's population, which its pass grades as S19 amends it (id 4)
- **consumes-from** `TOOL-dLinkedLibrary-64` — S6's `--observe` resolution, which its pass re-observes and S19 holds to one call (id 4)
- **hands-off** `TOOL-dLinkedLibrary-90` — S2's per-line CR strip and AC2's CRLF plants, which unit 90 moves into one decoder that also drops a BOM, in every dialect (id 33)
- **hands-off** `TOOL-dLinkedLibrary-91` — S5, S7, S14 to S16, S20, S22, S25, S27 and S28 with AC6, AC19, AC21, AC23 and AC26, and §4's cites, which unit 91's S7 and S17 to S30 correct at this unit's pass (ids 23, 8, 9, 35, 15, 36, 13, 34, 18, 16, 26, 22, 37, 21, 17)

## 4. Design

### Evidence

- S1: 77 AC1 (`2026-10-27-spec-TOOL-dLinkedLibrary-77.md:120-123`) names a GitHub `run: !!str |2-` header,
  and unit 85's §4 records that 77's pattern refuses `      - run: !!str |2-`.
- S2: no census spec states a line-ending rule; the report's probe of 77's pattern gave `'script: |\r'`
  False.
- S3: 78 S3 (`2026-10-27-spec-TOOL-dLinkedLibrary-78.md:47-50`) exempts no comment line, and 78 §5 says no
  page change is needed.
- S4 to S6: 71 S1 lists `!reference`, `alias` and `<<` with no precedence; 76 AC2 (`:121-123`) expects
  `refused: opaque step <<` while AC1 spells the full form.
- S10, S11: `ls memory/map/features/` lists the prefix pairs `run-gates` and `run-gates-turnstile`, and
  `playbook` and `playbook-mode`.
- S14 to S17: `read_pid_image` (`tools/unattended/lib-unattended.sh:595-619`) uses `tasklist` under MSYS and
  `kill -0` with `ps -o comm=` elsewhere, the latter marked UNVERIFIED; unit 67 S3 starts the grandchild by
  the full quoted path of `sys.executable`, so its `cmdline[0]` is a full path.
- S22: `tools/run-gates/regen.py:286-289` routes output through `tempfile.TemporaryFile()`, and the report's
  probe returned `TIMEOUT` in 1.01 s with `proc.kill()` against 1.13 s with `run_tree_kill`.
- S23: `tools/check-microformats.test.sh:17-18` defines `say_ok` and `say_fail` and its `arm` helper calls
  one per arm; `tools/run-gates/run-gates.test.sh:136-146` records each raise as "counted off the arms".
- S24, S25: `tools/check-wiring.sh:491-495` holds `def resolve_kit_dir` inside a bash heredoc, and the
  report counted 54 non-`.py` hosts of that row.
- S26: `.claude/skills/build/SKILL.md:5` reads `<!-- gov:kit roles@1.9 -->`.
- S27, S28: `git grep -l 'gov:kit memory-tree@' -- tools help memory/HYGIENE.md memory/TEMPLATE-SPEC.md
  memory/guides` lists 14 files at base (PINNED, 2026-10-27), Files touched below.

### Rollout

The plants of S1 to S9 add functions to `adopt_program.py` and `gotchas.py`, so the generated map is
re-rendered at this tip with `python tools/codebase-map/gen_map.py --write` where its `--check` exits 1,
as 80 S7 states for its own pass.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S9
- `help/adopt.md`: S3, S9
- `memory/map/features/`: S10, S11
- `tools/memory-tree/reuse_entries.py`: S12
- `tools/memory-tree/gotchas.py`: S14 to S17, S19
- `tools/memory-tree/decision_rubric.py`: S18
- `memory/builds/dLinkedLibrary/build/`: S13, S19, S31, S32, the acceptance ledgers
- `tools/check-microformats.test.sh`, `tools/run-gates/run-gates.test.sh`: S23
- `tools/lib/resolve-python.test.sh`: S24, S25
- `.claude/skills/build/SKILL.md`: S26
- `tools/memory-tree/ANNOTATION-STYLE.template.md`, `tools/memory-tree/BUILD-METHOD.template.md`,
  `tools/memory-tree/HYGIENE.template.md`, `tools/memory-tree/SPEC-TEMPLATE.template.md`,
  `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/adopt-memory-tree.sh`,
  `tools/memory-tree/kit.toml`, `tools/check-kit-versions.sh`, `memory/HYGIENE.md`,
  `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`, `memory/guides/ANNOTATION-STYLE.md`: S27
- `tools/codebase-map/map_lib.py`: S28
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: the Rollout re-render

### Alternatives rejected

- **One unit per finding.** M4 forbids it.
- **Folding each item into its unit's spec.** The owner's 2026-10-05 ruling promotes every minor and folds
  none.
- **S22 by keeping the elapsed-time arm.** No pipe read exists to block, so the arm can never be observed.
- **S15 by comparing `comm` with the basename of the realpath.** It fails when `sys.executable` is a
  symlink, which the skeptic of id 16 measured as the corrected fix's reason.
- **S23 by running each suite and reading its printed count.** A pass runs no suite (BUILD-METHOD M6); the
  canary's convention counts off the arms, and the staged red is the close's.

## 5. Production-readiness checklist

- security — S1 to S3 and S9 close census read gaps on CRLF files, a step header and the global
  `after_script:`; S14 to S16 stop a POSIX host misreading a live grandchild.
- perf / scale — S25 adds one slice and one `symtable` read per embedded copy.
- error / empty / loading states — S16, S20 and S30 each fail naming the cause on a probe that cannot look,
  an empty listing or a missing bound.
- observability — each refusal names its key, file, row, pid or bound.
- risks — S10 can restore a tag 75 rewrote; the ledger lists it, unresolved.
- testing — AC1 to AC26 by plant, fixture, scratch copy, pure-function call and probe.
- migration — S10 and S11's tag corrections and S27's render, each in this unit's commit.
- user docs — `help/adopt.md`, S3 and S9.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the GitHub job
  whose step is `- run: !!str |2-` reads `refused: npm publish`.
  Red when: the step form leaves 77 AC1's GitHub block unread.
- **AC2** — When the same plant runs over a tree whose `.gitlab-ci.yml` has CRLF endings and a `script: |`
  block holding `npm publish`, and whose GitHub workflow has CRLF endings and a `run: |` block holding `npm
  \` then `publish`, both jobs read `refused: npm publish`.
  Red when: a CR left on a header or a continued line reads the block as a plain scalar.
- **AC3** — When the same plant runs, a GitLab job whose list item `- npm test` is followed by a deeper `#
  note` line reads `importable`, and 78 AC4's split scalar still reads `refused: unreadable multi-line
  scalar script`.
  Red when: a comment-only continuation line refuses its job.
- **AC4** — When `grep -n 'unreadable multi-line scalar'` runs over the help page `adopt.md` (its path in
  Files touched) at this tip, it prints S3's sentence, and over the page at this pass's start, read with
  `git show`, it prints nothing.
  Red when: the refusal ships with no line on the page.
- **AC5** — When the same plant runs, both plain jobs of 76's `<<: *publish` tree read `refused: opaque step
  << default:<<`.
  Red when: the line reports `alias`, or `<child>` is anything but `<<`.
- **AC6** — When `grep -n 'opaque step'` runs over `adopt_program.py` at this tip, the reason text of a
  file-wide refusal is passed to one function, and its call sites for 71 S2's `include:`, 76 S2's
  `default:` and 84 S2's blocks are printed beside its single definition.
  Red when: a second loop over a file's jobs assigns a file-wide refusal.
- **AC7** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, both plain
  jobs of every refusing tree of 76 S4 and 79 S4 print the `refused:` line their spec states, and both
  jobs of each refusing Azure stage do.
  Red when: a hit refuses only the first job, or only the job after its block.
- **AC8** — When the same plant runs, both plain jobs of the tree holding `after_script: [npm publish]`
  read `refused: npm publish`, and both of the tree holding `after_script: !reference [.cleanup, script]`
  read `refused: opaque step !reference after_script:`.
  Red when: the global `after_script:` reaches no job.
- **AC9** — When `grep -n 'applies to every job'` runs over the help page `adopt.md` at this tip, it prints
  S9's sentence naming `after_script:`, and over the page at this pass's start it prints no line naming
  `after_script:`.
  Red when: the global keys ship with no line on the page.
- **AC10** — When unit 75's S2 resolution is run by hand with `python -I -c` in a scratch repository under
  `%TEMP%/rt86` holding `unit.reuse.run-gates-turnstile-1` and no `run-gates-turnstile.md`, it names the tag
  unresolved; and every rewrite in 75's acceptance ledger has a remainder matching `^[1-9][0-9]*$`.
  Red when: a non-numeric remainder resolves to a prefix stem.
- **AC11** — When `check_reuse_entries` runs over the tree at this tip it reports no part, and in the same
  scratch repository a part `memory-tree-hygiene.1.reuse.toml` carrying `unit.reuse.memory-tree.1` is
  reported and rewritten to `unit.reuse.memory-tree-hygiene.1`.
  Red when: a part's tag is derived by the longest-stem rule rather than its file stem.
- **AC12** — When 75 AC1's predicate `git grep -nE 'unit\.reuse\.[A-Za-z0-9_-]+-[0-9]+([^0-9A-Za-z_]|$)'
  -- tools` runs at this tip it prints nothing, while `python reuse_entries.py --fixture --plant
  hyphen-tag` still reports the part naming the hyphenated tag.
  Red when: the plant's literal joins the predicate's population, or the plant stops staging its red.
- **AC13** — When `grep -n 'population'` runs over this unit's acceptance ledger, it prints the count 75 S1
  printed at 75's pass start and the SHA it was read at.
  Red when: the sweep is certified with no population recorded.
  figure: DERIVED at this pass from 75's pass-start commit.
- **AC14** — When `python -I -c` imports `gotchas.py` and calls S14's comparison with literal readings, an
  `exe` realpath equal to the realpath of the given executable matches; a `comm` of `python3.12` against an
  absolute executable path whose basename is `python3.12` matches; a 15-character `comm` that opens the basename matches; and a
  `comm` of `sleep` does not.
  Red when: a full-path `cmdline[0]` is compared with a basename, or truncation reads a match as foreign.
- **AC15** — When the same function is called with neither reading available, it returns the `cannot look`
  verdict; and `grep -n 'UNVERIFIED\|read_pid_image'` over `gotchas.py` prints the case's comment naming
  the Windows citation and the POSIX departure.
  Red when: an unreadable host reads `grandchild not visible`, or the rule claims a seam it departs from.
- **AC16** — When `python decision_rubric.py --fixture --plant no-local-row-predicate` runs it prints `ok`,
  and over a scratch copy holding `re.compile(r"^- (\S+) · ")` it names that pattern; `grep -c
  -- '--selftest'` over `decision_rubric.py` prints 0.
  Red when: the guard lives under a mode no arm runs.
- **AC17** — When `grep -n 'amended'` runs over 74's and 64's acceptance ledgers, each prints its
  amendment line citing this unit, and `python -I -c` counting `resolve_bash` calls in `gotchas.py` with
  `ast` prints 1, inside `resolve_observed_argv`.
  Red when: an earlier criterion is graded unamended against a later scope, or a second call survives.
- **AC18** — When `git grep -l '^# >>> region_py' -- tools skills` runs at this tip it lists at least one
  file and every kit copy 74 S16 names; the unscoped `git grep -l '^# >>> region_py'` lists unit 18's spec
  record, and no path it prints outside `tools` and `skills` is in that scoped list.
  Red when: the scoped listing is empty, or a record joins the sites.
- **AC19** — When `python -I -c` loads a scratch copy of `tools/run-gates/regen.py` and calls `run_command`
  with a planted `bash -c` argv whose backgrounded grandchild sleeps 3 seconds and then writes a marker,
  under a 1-second bound, no marker exists 4 seconds later; with the copy's `run_tree_kill` call replaced
  by `proc.kill()`, the marker exists.
  Red when: the kill no longer reaches the grandchild.
  cost: about 10 seconds for the two runs.
- **AC20** — When `grep -n '^FLOOR_ASSERTIONS=\|counted off'` runs over the micro-format suite and the
  run-gates canary (their paths in Files touched), each floor equals its value at 74's pass start plus the
  assertions S23 traces, and a comment names the arms counted.
  Red when: a floor is raised by a grep of source text, or by a gated arm a host without `timeout -k`
  skips.
  figure: DERIVED at this pass by tracing 74's arms.
- **AC21** — When S24's free-name read runs by hand with `python -I` over every host S24 lists it names no
  unbound name; over a scratch copy of `tools/check-wiring.sh` whose `resolve_kit_dir` heredoc loses an
  import it names that name, the row and the file.
  Red when: a Python copy hosted in a shell file sits outside the read.
- **AC22** — When `git grep -h -o -E 'gov:kit roles@[0-9][0-9.]*[0-9]' -- tools help .claude` runs at this
  tip, it prints one distinct marker, equal to the roles constant.
  Red when: the committed render keeps the old marker beside a moved template.
- **AC23** — When `git grep -h -o -E 'gov:kit <kit>@[0-9][0-9.]*[0-9]' -- tools help memory/HYGIENE.md
  memory/TEMPLATE-SPEC.md memory/guides ':!*.test.sh'` runs for `memory-tree` and `codebase-map`, each
  prints one distinct marker equal to its constant; without the exclusion the memory-tree run also prints
  `memory-tree@1.5`.
  Red when: a carrier keeps the old marker, or the fixture marker stands in the population.
- **AC24** — When `grep -c` runs over the help page `adopt.md` for 80 S30's job-level phrasing at this tip
  it prints at least 1, and over a scratch copy with 71's paragraph deleted it prints 0, while 76's
  `default:` sentence is still present.
  Red when: a sentence another unit wrote satisfies 80 AC24.
- **AC25** — When 80 S4's range is derived by hand at this tip, it prints the two SHAs it compared; in a
  scratch clone under `%TEMP%/rg86` whose log holds no `build(dLinkedLibrary): TOOL-dLinkedLibrary-74 `
  subject, it exits non-zero naming the missing bound.
  Red when: an empty range reads green, or the base stands in for 74's pass start.
- **AC26** — When `grep -n 'query.py'` runs over this unit's acceptance ledger, it prints one query per
  subject §10 names, each beside the records it surfaced and their reconciliation; and `grep -c 'census
  refuse a ci'` over this spec's §10, cut with `sed -n '/^## 10/,$p'`, prints 0.
  Red when: a subject's recall is the CI-census query, or a surfaced record goes unreconciled.

## 7. Gates

`gotchas selftest` · `policy fixtures` · `build-index selftest` · `micro-format gate selftest` · `run-gates canary` · `python resolver (behaviour + inline parity + idiom ban)` · `kit/dogfood doc parity` · `kit version markers` · `roles render wiring` · `check-wiring self-test` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC5 AC7 AC8 · the `ci-census` plant's step-form, CRLF, comment-continuation, merge-precedence, two-job and global `after_script:` trees, the failing case staged by the units' one-job plants and LF-only read · none
New arm: tools/memory-tree/reuse_entries.py · covers AC12 · the `hyphen-tag` plant composed at run time, the failing case staged by spelling the literal in the module · none
New arm: tools/memory-tree/gotchas.py · covers AC14 AC15 · the POSIX image comparison and the cannot-look verdict, the failing case staged by a `cmdline[0]` basename compare · none
New arm: tools/memory-tree/decision_rubric.py · covers AC16 · the `no-local-row-predicate` fixture case, the failing case staged by a local middot pattern · none
New arm: tools/lib/resolve-python.test.sh · covers AC21 · the free-name read over every host the parity loop reads, the failing case staged by a heredoc copy losing an import · none
New arm: tools/check-microformats.test.sh · covers AC20 · the floor 74's arms owe, the failing case staged by deleting one of those arms · FLOOR_ASSERTIONS raised by the count S23 traces
New arm: tools/run-gates/run-gates.test.sh · covers AC20 · the floor 74's arms owe, the failing case staged by deleting one of those arms · FLOOR_ASSERTIONS raised by the count S23 traces

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. (b) splits clauses the
  repaired units carry whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 75 to 80, 22 MEDIUM and 10 LOW
  findings batched in one unit.
- rev-2 · 2026-10-27 · §3 · the hands-off edges to units 90 and 91, the mirrors of the consumes-from
  edges their specs declare, promoted from the spec audit of units 81 to 86; no scope or criterion moved.

## 10. Reuse audit

Every item extends the seam its finding names: the census's reader and plants in
`tools/memory-tree/adopt_program.py`, 71 S2's file-wide refusal, unit 75's predicate,
`check_reuse_entries`' stem reader, `read_pid_image`'s Windows rule, unit 1's `--fixture --plant` mode,
the parity loop of `tools/lib/resolve-python.test.sh`, each suite's `FLOOR_ASSERTIONS` convention, and the
roles and memory-tree kits' render commands; no item mints a second implementation of any. `python
tools/codebase-map/reuse_lookup.py "check the process holding a pid is the interpreter we started on
posix"` ranked `check`, `checks`, `check_line` and `check_convention`, none a pid-identity reader, so no
existing seam fits beyond those the items name.

The subject queries S31 re-runs, one per subject, and what each surfaced on 2026-10-27:

- 75, reuse tags: `python tools/memory-recall/query.py "how is a reuse entry tag spelled for a feature part" --terms "reuse-entry tag unit.reuse part stem dotted hyphenated feature dossier propose check_reuse_entries sweep"`, which surfaced units 75, 38 and 60 and ask `TOOL-dLinkedLibrary-27`.
- 80, pid identity: `python tools/memory-recall/query.py "how does an observer confirm the process holding a pid is the grandchild it started" --terms "pid image tasklist read_pid_image proc cmdline exe comm grandchild visible tree-kill nonce"`, which surfaced `TOOL-cMendedVintage-12`, `TOOL-aReapedSpinner-10` and `TOOL-dSafePassage-31`.
- 80, BOM and CRLF conf reads: `python tools/memory-recall/query.py "how is a conf value read the way bash source reads it with a bom or crlf" --terms "MAP_CLI bom crlf read_map_cli bash source parse_conf_assignment utf-8-sig conf line"`, which surfaced units 69, `TOOL-aRepatriatedFork-38` and `TOOL-dDeclaredLoop-76`.
- 80, row grammar: `python tools/memory-recall/query.py "how is a decision log row read through the kit row grammar rather than a local pattern" --terms "row_grammar decision row predicate archive log-diff derive_log_departures FAMILIES conf middot"`, which surfaced unit 68 and `TOOL-aLoosenedCeiling-1`.
- 80, region sites and kit versions: `python tools/memory-recall/query.py "how are region parser copies and kit version markers kept in step" --terms "region_py splice_region copy site kit version marker constant gov:kit carrier render parity"`, which surfaced unit 18's scout record and unit 74.
- 80, suite floors: `python tools/memory-recall/query.py "how is a suite assertion floor derived and raised" --terms "FLOOR_ASSERTIONS floor assertion count executed suite canary micro-format say_ok HAVE_TIMEOUT raise"`, which surfaced `TOOL-aWokenSentinel-21` and `TOOL-dBoundRoles-62`, whose §10 names the shrink-only floor convention S23 follows.
