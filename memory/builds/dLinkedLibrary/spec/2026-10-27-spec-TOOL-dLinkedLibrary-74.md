# TOOL-dLinkedLibrary-74 — the spec audit of units 54 to 64: its medium and low findings, batched

**Status:** OPEN · rev-3 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 30 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-74-deviation-741.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-74-deviation-741.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-68 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 54 to 64
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md`) confirmed
19 MEDIUM and 10 LOW findings. BUILD-METHOD M4 promotes them into one batch unit, and this is it; each
finding is its own scope item below, by report id:

- MEDIUM: 1 and 34 (item M1), 3 and 23 (M2), 4 and 38 (M3), 12 (M4), 42 (M5), 11 (M6), 26 (M7), 13
  (M8), 37 (M9), 5 (M10), 7 (M11), 22 (M12), 29 (M13), 30 (M14), 41 (M15), 43 (M16).
- LOW: 6 (L1), 16 (L2), 17 (L3), 28 (L4), 31 (L5), 32 (L6), 44 (L7), 45 (L8), 46 (L9), 36 (L10).

Four of these are the medium or low half of a defect the report also binds at HIGH: M1 of H1
(`TOOL-dLinkedLibrary-65`, `TOOL-dLinkedLibrary-66`), M3 of H3 (`TOOL-dLinkedLibrary-68`), M4 of H2
(`TOOL-dLinkedLibrary-67`); and L10 is M8's at low. Each such item builds only what its higher-grade
unit leaves. The findings land on twelve units, so this unit repairs none in particular and builds after
every unit of the build (order 30). Where an item corrects what a unit's criterion asserts, that unit's
acceptance ledger answers the criterion AMENDED, naming this unit and the item. One unit and not two:
S23 re-renders `memory/map/generated/symbols.json`, the generated index every item that adds a function
moves, so no split by M6's clause 3 leaves two disjoint write sets.

## 2. Scope (IN)

- **S1** — id 1, M1. Unit 55's acceptance ledger answers 55 AC1 AMENDED, naming `TOOL-dLinkedLibrary-66`:
  its red half is observed on the stripped-block copy at exit 2, never on 55 S2's inserted-line copy.
  Observed by AC1.
- **S2** — id 34, M1. Unit 54's ledger answers 54 AC3 AMENDED, naming `TOOL-dLinkedLibrary-65`: the red
  half is the stripped-block copy exiting exactly 2 and printing 65's `region_sh` line; the green half is
  as written. Observed by AC1.
- **S3** — id 3, M2. Unit 54's ledger answers 54 AC1 AMENDED with the narrowed count, a source line
  naming the library directory, `grep -cE '^[[:space:]]*(\.|source)[[:space:]].*lib/'` over
  `tools/check-microformats.sh` printing 0. Observed by AC2.
- **S4** — id 23, M2. The header sentence 54 S4 requires names the library as "the gov library directory"
  and spells no `lib/` token, so 54 AC1's count as written and S3's narrowed count both read 0. Observed
  by AC2.
- **S5** — id 4, M3. 59 S2's order check finds the rows present at base and now through
  `row_grammar.derive_row_re`, the reader 68 S1 gives the classification, so two swapped bold rows are a
  departure; the `log-diff` plant gains that tip. Observed by AC3.
- **S6** — id 38, M3. `decision_rubric.py`'s docstring states that both row spellings are rows, and over
  the real tree `log-diff`'s rotated count equals the number of ids unit 1's routing record names moved.
  Observed by AC3.
- **S7** — id 12, M4. Before the bound, the `observe-tree-hang` case checks that the pid in its pidfile
  names a process the observer can see, `os.kill(pid, 0)` on POSIX and a `tasklist` filter on that pid
  on Windows; a pid it cannot see fails the case as `harness: grandchild not visible to the observer`, so
  the post-kill check never passes on a pid in another namespace. Observed by AC4.
- **S8** — id 42, M5. The same case asserts the pidfile exists and holds an integer before it judges
  liveness; otherwise it fails as `harness: grandchild never started`, never as a pass or fail of the
  kill. Observed by AC4.
- **S9** — id 11, M6. Unit 61's ledger answers 61 AC2 AMENDED: both `tree_kill_py` slices are piped
  through `tr -d '\r'` before `diff`, as `blk` does (`tools/lib/resolve-python.test.sh:221`). Observed
  by AC5.
- **S10** — id 26, M7. `tools/memory-tree/gotchas.py` imports `signal` at module level, outside the
  `tree_kill_py` block, and a `--selftest` case `tree-kill-names-bound` reads the module's own block with
  `ast` and fails naming any free name that is not a module global. Observed by AC6.
- **S11** — id 13, M8. `retire_reuse_lookup.py up` hands `.unattended.conf` to the before-image on every
  row, its bytes, or `null` when absent, whether or not it rewrites the file. Observed by AC7.
- **S12** — id 37, M9. `down` restores only the image entries the step found or wrote: an entry
  recorded `null` before and `null` after is outside its restore set, so where a conf appeared after `up`,
  `down` leaves it untouched, restores the two lookup files and exits 0. Observed by AC8.
- **S13** — id 5, M10. Unit 64's ledger answers 64 AC12 AMENDED, per leg: each leg of 52's S33 to S36 is
  grepped in `tools/run-gates/ceiling-evidence.txt` and in the dossier that claims it, found by `grep -l`
  of the leg name over `memory/map/features/`, the playbook dossier for `adopt instructions selftest`.
  Observed by AC9.
- **S14** — id 7, M11. `reuse_entries.py propose` exits 2 naming the record when any record under the
  build's `build/` folder carries a live proposal, one with no `- **Disposition:**` line, whose body names
  the part `<feature>.<n>`, whatever its date or unit; the `refile-later-date` plant files a part, moves
  the date and files it again. Observed by AC10.
- **S15** — id 22, M12. `region.py --census`'s factory-block list (`TOOL-dLinkedLibrary-43` S1) gains
  `region_nth`, so the inline copy unit 56 puts in `tools/run-gates/run-gates.test.sh` is factory, not a
  site. Observed by AC11.
- **S16** — id 29, M13. 64 S13's `splice_region` refusal lands in every `region_py` copy, the sites
  re-derived at the pass by `git grep -l '^# >>> region_py'`, and each copy's kit version constant moves
  with its marker: `KIT_ROLES_VERSION` (`tools/roles/roles_lib.py:27`), `KIT_PLAYBOOK_RENDER_VERSION`
  (`tools/playbook/render_playbook.py:1887`), `KIT_RUNLOG_VERSION` (`tools/runlog/runlog_lib.py:27`) and
  `KIT_DRIFT_AUDIT_VERSION` (`tools/drift-audit/drift_report.py:95`), beside the memory-tree, codebase-map
  and govkit constants 64 names. Observed by AC12.
- **S17** — id 30, M14. The canary gains an arm that copies `run-gates.sh` alone into a scratch kit
  directory with no library sibling and runs its inline `region_nth` block and its `mempause_sh` slice
  command against that copy, asserting the slice is non-empty and equal to the awk slice; its failing
  case is the same command with the block absent and a source of `region.sh` in its place, which slices
  nothing. Observed by AC13.
- **S18** — id 41, M15. 63 S3's credential rule reads every line of a job, `variables:`, an Azure step's
  `env:`, and GitLab's `secrets:` and `id_tokens:` included; a GitLab job carrying `secrets:` or
  `id_tokens:` reads `refused: unreadable credentials <key>`; the `ci-census` plant gains an Azure step
  whose `env:` maps a token its script never names, and a GitLab job with `id_tokens:`; `help/adopt.md`
  names the keys. Observed by AC14.
- **S19** — id 43, M16. `--observe` writes each run's output to its own `tempfile.TemporaryFile()`, outside
  the scratch clone, as `tools/run-gates/regen.py:289` does, and its selftest asserts the clone's `git
  status --porcelain --untracked-files=all` is empty before each run. Observed by AC15.
- **S20** — id 6, L1. Every reuse-entry tag unit 19's migration writes reads `unit.reuse.<feature>.<n>`;
  a hyphenated `unit.reuse.<feature>-<n>` found in the tree is rewritten to it, and unit 19's ledger
  records the tag form its plan output wrote. Observed by AC16.
- **S21** — id 16, L2. The scope comment of `tools/run-gates/kit.toml` (:35-38) says a copy install's
  suites are described by the canary's header (`tools/run-gates/run-gates.test.sh:30-31`), and no longer
  claims a runbook `cp -r` step for this kit, which `WIRE-INTO-PROJECT.md` does not hold. Observed by
  AC17.
- **S22** — id 17, L3. 64 S19's deletion in `tools/codebase-map/kit.toml` covers the comment above each
  deleted `[[files]]` row, :39-46 for the replay harness and :51-55 for the ranking harness. Observed by AC18.
  **Readers:** by name: `tools/codebase-map/kit.toml`, the one tracked file outside this repository's build
  records that spells the comment's sentences; the files they name keep the readers TOOL-dLinkedLibrary-3
  S1 and TOOL-dLinkedLibrary-52 S41 answer for.
  by value: NO VALUE READERS because the block is a TOML comment, which the TOML reader discards.
- **S23** — id 28, L4. `memory/map/generated/symbols.json` is re-rendered by `gen_map.py` at this pass,
  after the functions units 54, 56 and 61 add, and the `codebase-map coverage + freshness` leg is on this
  unit's §7. Observed by AC19.
- **S24** — id 31, L5. `regen.py`'s bounded kill is re-observed after 61's markers and S25's label: its
  `run_command` over a sleeping `bash` with a 1-second bound returns `TIMEOUT`, and `run-gates canary` is
  on this unit's §7. Observed by AC20.
- **S25** — id 32, L6. The canonical openers carry the label `_scan_install_sites` reads:
  `# >>> region_nth -- canonical copy: region.sh in the gov lib dir (byte-identical; gated)` in
  `tools/lib/region.sh` and `# >>> tree_kill_py -- canonical copy: regen.py in the run-gates kit
  (byte-identical; gated)` in `tools/run-gates/regen.py`, each inline copy carrying the same opener byte
  for byte. Observed by AC21.
- **S26** — id 44, L7. `dossier_move.py apply` tests `--build` and `--unit` with `fullmatch` on
  `SLUG_RE` and `GRANT_ID_RE` (`tools/memory-tree/backlog.py:129`, :453), never `match`, and the
  `bad-values` plant gains a value ending in a newline for each flag. Observed by AC22.
- **S27** — id 45, L8. The canary's `mempause_sh` slice keeps `region_nth`'s status apart from `tr`'s:
  `_mpb=$(region_nth …)` is tested before `tr -d '\r'` runs, and an empty or failed slice fails through
  `check_mp_value` (`tools/run-gates/run-gates.test.sh:3450`) naming the absent `mempause_sh` block.
  Observed by AC23.
- **S28** — id 46, L9. Where `region` refuses a pair the count admits, `tools/check-microformats.sh`
  exits 2 saying the fence pair is malformed or reversed and printing the line number of every line that
  begins with either marker; a suite arm plants the exact pair plus a line `<!-- microformats --> (see
  below)`. Observed by AC24.
- **S29** — id 36, L10. The witness reads a before-image holding no `.unattended.conf` entry as a
  failure: it exits 1 saying the image lacks the entry this step's `up` writes on every row (S11).
  Observed by AC7.

## 3. Non-goals (OUT)

- The HIGH findings of the same audit: units 65 to 73, one per id.
- Re-opening any unit's design: each item corrects the built code, or records where the finding lands.
- A gate per left-shift the report proposes: every item lands on an existing arm, plant or ledger.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-54` — AC1, AC3, S3's exit and S4's header, which S2 to S4 and S28 amend and complete (ids 34, 3, 23, 46)
- **consumes-from** `TOOL-dLinkedLibrary-55` — AC1, which S1 answers AMENDED (id 1)
- **consumes-from** `TOOL-dLinkedLibrary-56` — the inline `region_nth` copy and its `mempause_sh` slice, which S15, S17, S25 and S27 complete (ids 22, 30, 32, 45)
- **consumes-from** `TOOL-dLinkedLibrary-57` — the before-image read and the witness, which S11 and S29 complete (ids 13, 36)
- **consumes-from** `TOOL-dLinkedLibrary-58` — the absent-conf image and `down`, which S12 completes (id 37)
- **consumes-from** `TOOL-dLinkedLibrary-59` — S2's order check and the module docstring, which S5 and S6 complete (ids 4, 38)
- **consumes-from** `TOOL-dLinkedLibrary-60` — `propose`'s duplicate refusal and its tag, which S14 and S20 complete (ids 7, 6)
- **consumes-from** `TOOL-dLinkedLibrary-61` — `tree_kill_py`, `--observe`'s output file and AC2, which S9, S10, S19, S24 and S25 complete (ids 11, 26, 43, 31, 32)
- **consumes-from** `TOOL-dLinkedLibrary-63` — S3's credential rule and the `ci-census` plant, which S18 completes (id 41)
- **consumes-from** `TOOL-dLinkedLibrary-64` — AC12, S13's `splice_region`, S14's validation and S19's deletion, which S13, S16, S26 and S22 complete (ids 5, 29, 44, 17)
- **consumes-from** `TOOL-dLinkedLibrary-19` — the migration's reuse-entry tags, which S20 keeps dotted (id 6)
- **consumes-from** `TOOL-dLinkedLibrary-65` — the guard's `region_sh` line, which S2 records in 54's ledger (id 34)
- **consumes-from** `TOOL-dLinkedLibrary-66` — the stripped-block arm, which S1 records in 55's ledger (id 1)
- **consumes-from** `TOOL-dLinkedLibrary-67` — the `observe-tree-hang` plant, whose pidfile S7 and S8 check (ids 12, 42)
- **consumes-from** `TOOL-dLinkedLibrary-68` — the classification's `derive_row_re` read, which S5 extends to the order check (id 4)
- **hands-off** `TOOL-dLinkedLibrary-75` — AC16's tag sweep, which unit 75 re-reads with a hyphen-admitting feature class and rewrites (id 25 of the spec audit of units 65 to 74)
- **hands-off** `TOOL-dLinkedLibrary-79` — S18's credential rule and AC14's plants, which unit 79 extends to every block applying to a job, file-level ones included (id 36 of the spec audit of units 65 to 74)
- **hands-off** `TOOL-dLinkedLibrary-80` — S16's copies and constants, S7 and S8's pidfile checks, S14's duplicate refusal, S4's header, S21's pointer, S23's render and S24's re-observation, which unit 80 completes (ids 1, 11, 27, 2, 10, 26, 28, 40, 21, 43, 42, 4, 7, 17, 8 of the spec audit of units 65 to 74)
- **hands-off** `TOOL-dLinkedLibrary-86` — AC12's population, which this pass grades over `-- tools skills` as unit 80 S1 scopes it, writing an amendment line in this unit's acceptance ledger that unit 86's S19 reads (id 4 of the spec audit of units 75 to 80)

## 4. Design

### Evidence

- S3, S4: 54 S4 requires the header to name why the reader is inline; 54 AC1 counts `lib/` over the
  whole gate; `grep -n "lib/" tools/check-microformats.sh` prints nothing at base.
- S7, S8: the audit's re-probe (id 12) found a WSL grandchild cannot write a Windows pidfile path, and
  (id 42) that a 9009 grandchild lets `; true` exit 0 before the bound.
- S10: `tools/memory-tree/gotchas.py:50-57` imports `os`, `pathlib`, `re`, `subprocess`, `sys` and
  `tempfile`; `tools/run-gates/regen.py:257` calls `os.killpg(proc.pid, signal.SIGKILL)`.
- S11, S12, S29: TOOL-dSafePassage-1 §4, the image holds "every path it will write or remove" and a down
  "restores each path only where its bytes are the image's after-hash or before bytes, else exits 1".
- S15: 43 S1 names `region_py`, `region_sh`, `gen_region_awk` and `region_js` as the factory blocks; the
  census regex `index\(ln, ?[oc]\) ?== ?1` matches the house body (`tools/unattended/check-unattended.sh:213`).
- S21: `grep -n 'cp -r' WIRE-INTO-PROJECT.md` lists memory-tree, drift-audit, process-monitor,
  codebase-map, memory-recall, lexicon and branch-reconcile, and no run-gates step.
- S22: `tools/codebase-map/kit.toml:39-46` is the replay-harness comment above the row at :47-49, and
  :51-55 the ranking-harness comment above the row at :56-58.
- S25: `tools/codebase-map/map_lib.py:893-895` skips a file only when its opener names it after
  `canonical copy:`.
- S26: `re.match` with a `$`-anchored pattern accepts a trailing newline, as the audit observed for both
  patterns.
- S28: `region`'s body sets `bad` on a line that begins with a marker and is not equal to it
  (`tools/unattended/check-unattended.sh:213-214`), and the gate's count is `grep -cxF` (:40-41).

### Files touched (estimate)

- `tools/check-microformats.sh`: S4, S28
- `tools/check-microformats.test.sh`: S28
- `tools/memory-tree/decision_rubric.py`: S5, S6
- `tools/memory-tree/gotchas.py`: S7, S8, S10, S19, S25
- `tools/govkit/steps/retire_reuse_lookup.py`: S11, S12, S29
- `tools/memory-tree/reuse_entries.py`: S14
- `tools/lib/region.py`: S15, S16
- `tools/lib/region.sh`, `tools/run-gates/regen.py`: S25
- `tools/run-gates/run-gates.test.sh`: S17, S25, S27
- `tools/memory-tree/adopt_program.py`, `help/adopt.md`: S18
- `tools/memory-tree/gen_build_index.py`, `tools/playbook/render_playbook.py`, `tools/roles/check_roles.py`,
  `tools/roles/roles_lib.py`, `tools/runlog/prose.py`, `tools/runlog/runlog_lib.py`,
  `tools/drift-audit/drift_report.py`, `tools/codebase-map/map_lib.py`, `tools/govkit/selftest.py`: S16
- `tools/run-gates/kit.toml`: S21
- `tools/codebase-map/kit.toml`: S22
- `tools/codebase-map/dossier_move.py`: S26
- `memory/map/generated/symbols.json`: S23
- the acceptance ledgers of units 19, 54, 55, 61 and 64 under `memory/builds/dLinkedLibrary/build/`: S1
  to S3, S9, S13, S20

### Alternatives rejected

- **One unit per finding.** M4 forbids it.
- **Folding each item into its unit's spec.** The owner's 2026-10-05 ruling promotes every minor and folds
  none.
- **S12 by not imaging an absent conf.** It undoes S11, and S29 then cannot tell an absent conf from an
  unrecorded one.

## 5. Production-readiness checklist

- security — S18 refuses a job whose credentials the census cannot read; S26 validates two CLI values
  before a path join; S14 refuses a duplicate live proposal.
- perf / scale — no item changes complexity.
- error / empty / loading states — S7, S8, S27, S28 and S29 each fail naming the cause they observe.
- observability — each refusal names its file, line, key or value.
- risks — S12 leaves a conf the step never wrote, where a stricter down would refuse.
- testing — AC1 to AC24 by fixture, selftest case, plant and probe.
- migration — S20's tag rewrite and S16's version moves, each in its own commit.
- user docs — `help/adopt.md`, S18.

## 6. Acceptance criteria

- **AC1** — When `grep -n "AC1\|AC3"` runs over unit 55's and unit 54's acceptance ledgers, 55's AC1 and
  54's AC3 each read AMENDED, naming this unit and the stripped-block copy's exit 2.
  Red when: a ledger certifies a red half on the inserted-line copy, which exits 0.
- **AC2** — When `grep -cE '^[[:space:]]*(\.|source)[[:space:]].*lib/' tools/check-microformats.sh` and
  `grep -c "lib/" tools/check-microformats.sh` run at this pass's tip, each prints 0, and `grep -n "gov
  library directory"` over the same file prints the header line.
  Red when: the header spells the library directory's path, or the gate sources a library file.
- **AC3** — When `python decision_rubric.py --fixture --plant log-diff` runs, the tip swapping two bold
  rows reads one departure naming a row; and `python decision_rubric.py log-diff 5fede642 --routing <unit
  1's routing record>` prints a rotated count equal to the record's moved ids.
  Red when: a bold reorder passes, or the rotated count misses a spelling.
  figure: DERIVED at the pass from the record.
- **AC4** — When `python tools/memory-tree/gotchas.py --selftest` runs `observe-tree-hang` with its plant
  rewritten to write no pidfile, it fails as `grandchild never started`; with the pid replaced by one no
  process holds, it fails as `grandchild not visible`; unmodified it prints `ok`.
  Red when: a missing or invisible grandchild reads as a passing kill.
- **AC5** — When `grep -n "AC2"` runs over unit 61's acceptance ledger, the answer reads AMENDED with the
  `tr -d '\r'` slices compared equal.
  Red when: the ledger compares CRLF and LF slices raw.
- **AC6** — When `grep -n "^import signal" tools/memory-tree/gotchas.py` runs it prints one line outside
  the block, and the `tree-kill-names-bound` selftest case prints `ok`; with the import deleted it names
  `signal`.
  Red when: a free name of the block is unbound in its host.
- **AC7** — When `python retire_reuse_lookup.py up <target>` runs over scratch targets under
  `%TEMP%/rl74a` with a blank `MAP_CLI` and `%TEMP%/rl74b` with no conf, the image records the conf's bytes
  and `null`; with the conf entry deleted from the image, `witness` exits 1 naming the missing entry.
  Red when: a row `up` does not write leaves the conf out of its image, or a missing entry passes.
- **AC8** — When a conf is written into the `%TEMP%/rl74b` target after `up` and `python
  retire_reuse_lookup.py down <target>` runs, it exits 0, both lookup files are back, and the conf's bytes
  are unchanged.
  Red when: `down` refuses on a file the step never wrote.
- **AC9** — When `grep -n "AC12"` runs over unit 64's acceptance ledger, it reads AMENDED with one grep per
  leg, `adopt instructions selftest` against `memory/map/features/playbook.md`.
  Red when: a leg is grepped in a dossier that does not claim it.
- **AC10** — When `python reuse_entries.py --fixture --plant refile-later-date` runs, the second `propose`
  of the part on a later date exits 2 naming the live record and writes nothing.
  Red when: a re-file on another date writes a second live proposal.
- **AC11** — When `python region.py --census` runs at this pass's tip, it prints no site in
  the run-gates canary, the file S17 names.
  Red when: the inline `region_nth` copy counts as a region parser outside the factory.
- **AC12** — When `git grep -l '^# >>> region_py'` runs, every file it lists carries a `splice_region` that
  raises on a body line `<open>x`, and each version constant S16 names differs from its base value.
  Red when: a copy keeps the old body, or a kit ships a changed copy at its old version.
- **AC13** — When the canary's lib-less slice arm is reproduced by hand in a scratch kit directory under
  `%TEMP%/rg74`, the slice equals the awk slice; with the block replaced by a source line it is empty.
  Red when: the slice reads a library file a copy install does not hold.
- **AC14** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the Azure step
  with an `env:`-mapped token reads `refused: unreadable credentials`, and the GitLab job with
  `id_tokens:` reads `refused: unreadable credentials id_tokens`.
  Red when: a credential delivered outside the script lines reads `importable`.
- **AC15** — When `python tools/memory-tree/gotchas.py --selftest` runs its observe cases, each asserts an
  empty porcelain in the scratch clone before its run and prints `ok`.
  Red when: the observer leaves a file inside the tree it grades.
- **AC16** — When `git grep -nE 'unit\.reuse\.[A-Za-z0-9_]+-[0-9]+' -- tools memory/map` runs at this
  pass's tip, it prints nothing.
  Red when: a hyphenated tag survives in the migration's output.
- **AC17** — When `grep -n "cp -r" tools/run-gates/kit.toml` runs, it prints nothing, and a grep for
  the canary's file name over the same file prints the comment's pointer.
  Red when: the descriptor cites a runbook step that does not exist.
- **AC18** — When `grep -ci "replay harness\|rank_harness\|replay-phrases" tools/codebase-map/kit.toml`
  runs at this pass's tip, it prints 0.
  Red when: a comment naming a deleted harness survives.
- **AC19** — When `python tools/codebase-map/gen_map.py` runs at this pass's tip, `git status --porcelain
  memory/map/generated/symbols.json` prints nothing.
  Red when: the committed symbol render is stale.
- **AC20** — When `python -I -c` loads `tools/run-gates/regen.py` by its path and calls `run_command` with
  `["bash", "-c", "sleep 5"]`, the repository root and a bound of 1, it returns `TIMEOUT` within 3
  seconds.
  Red when: the marked kill path no longer bounds a run.
- **AC21** — When `git grep -n '^# >>> region_nth\|^# >>> tree_kill_py'` runs, every line carries
  `canonical copy:`, and the lines naming one stem are byte-identical.
  Red when: a canonical opener is bare, or a copy's opener differs.
- **AC22** — When `python dossier_move.py --fixture --plant bad-values` runs, `--build` and `--unit` values
  ending in a newline each exit 2 naming the value and write nothing.
  Red when: a trailing newline passes validation.
- **AC23** — When the canary's slice is reproduced by hand with the `mempause_sh` block deleted from a
  copy of the gate runner, the check fails naming `mempause_sh`, not a value mismatch.
  Red when: an absent block reads as `127 127`.
- **AC24** — When `bash tools/check-microformats.sh <charter>` runs over a scratch charter holding the exact
  pair plus a `<!-- microformats --> (see below)` line, it exits 2 printing `malformed or reversed` and
  that line's number.
  Red when: the message calls a malformed marker a reversed pair.

## 7. Gates

`micro-format definitions` · `micro-format gate selftest` · `govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `recall floor` · `recall floor arms` · `policy fixtures` · `gotchas selftest` · `run-gates canary` · `python resolver (behaviour + inline parity + idiom ban)` · `marker contracts` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `playbook render selftest` · `roles catalogue` · `roles render selftest` · `runlog selftest` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `drift-audit selftest` · `drift-audit records` · `build-index selftest` · `tier2-review self-test` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gotchas.py · covers AC4 AC6 AC15 · the pidfile, visibility, names-bound and clean-tree cases, the failing case staged by a plant writing no pidfile, a dead pid and a deleted import · none
New arm: tools/memory-tree/reuse_entries.py · covers AC10 · the `refile-later-date` plant, the failing case staged by the dated-name refusal · none
New arm: tools/run-gates/run-gates.test.sh · covers AC13 AC23 · the lib-less slice arm and the absent-block slice, the failing case staged by a source line in place of the block · none
New arm: tools/memory-tree/adopt_program.py · covers AC14 · the `env:` and `id_tokens:` jobs of the `ci-census` plant, the failing case staged by 63's script-only credential read · none
New arm: tools/check-microformats.test.sh · covers AC24 · the prefixed extra marker line, the failing case staged by the reversed-pair message · none
New arm: tools/codebase-map/selftest.py · covers AC22 · the newline values of the `bad-values` plant, the failing case staged by `re.match` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. (b) splits clauses
  the repaired units carry whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — How does `down` meet a conf that appeared after `up` (S12)?** Options: (a) the step leaves a
  `null`-before, `null`-after entry out of the paths its `down` restores; (b) `up` does not image an absent
  conf; (c) an ask to dSafePassage to change the generic down. (b) fails S11 and S29 (veto 1); (c) leaves
  the rollback refusing until another build lands. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the most feature-rich survivor; it discards no later edit, the purpose TOOL-dSafePassage-1 §4 states for
  its refusal. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 54 to 64, 19 MEDIUM and 10
  LOW findings batched in one unit.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-75, TOOL-dLinkedLibrary-79, TOOL-dLinkedLibrary-80, promoted from the spec
  audit of units 65 to 74; nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-86, promoted from the spec
  audit of units 75 to 80; nothing else moved.

## 10. Reuse audit

Every item extends the seam its finding names: the units' acceptance ledgers, `row_grammar.derive_row_re`,
the `observe-tree-hang` case, TOOL-dSafePassage-1's before-image, unit 1's `propose`, the census's
factory list, the `region_py` parity population, the canary's own slice, unit 63's census,
`gen_map.py`'s render, `_scan_install_sites`' label, and `SLUG_RE` and `GRANT_ID_RE`
(`tools/memory-tree/backlog.py:129`, :453); no item mints a second implementation of any. `python
tools/codebase-map/reuse_lookup.py "refuse a micro-format gate whose inline region reader is missing"`
ranked `read`, `read_text`, `read_conf`, `read_journal` and `region`, none of them a seam an item lacks,
so no existing seam fits beyond those the items name.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding of a spec audit repair a unit at the next order step" --terms "spec-audit promoted high finding repairs order staged break conf reader row grammar census indirection"`
