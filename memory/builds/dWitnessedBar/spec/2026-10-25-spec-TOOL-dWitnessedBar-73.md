# TOOL-dWitnessedBar-73 — the round-1 audit of units 66 and 67, its 23 minors batched: fixtures, populations, the hook guard, every key and filesystem call exercised, predicates and records

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 |
| [2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 66 and 67
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-66-spec-audit-round1.md`)
exited BOUNDED with 28 confirmed findings: one BLOCKER, id 10, which `TOOL-dWitnessedBar-70` takes;
four HIGH, ids 1, 11, 19 and 20, which `TOOL-dWitnessedBar-68`, `-71`, `-69` and `-72` take; and 23
minors. BUILD-METHOD M4 batches every MEDIUM and LOW into one unit, or two only where they split into
disjoint write sets by M6's clauses so that both build concurrently. §4 "Why one unit" says why these
stay one. Each finding is named by report id and is its own scope item, including where the report
merged ids into one item. The minors land on both `TOOL-dWitnessedBar-66` and `TOOL-dWitnessedBar-67`,
so this unit repairs no single unit and builds above every unit in the build (order 41).

| Report item | Severity | Report id | Lands on | Scope item |
|---|---|---|---|---|
| M1 | MEDIUM | 3 | unit 67 S6, AC5 | S1 |
| M1 | MEDIUM | 18 | unit 67 S6, AC5 | S2 |
| M1 | MEDIUM | 21 | unit 67 S6, AC5 | S3 |
| M2 | MEDIUM | 4 | unit 67 S7, AC6 | S4 |
| L9 | LOW | 27 | unit 67 AC6 | S5 |
| M3 | MEDIUM | 15 | unit 66 §4, §7 | S6 |
| M3 | MEDIUM | 16 | unit 67 S2, §4, §7 | S7 |
| M4 | MEDIUM | 17 | unit 67 S15, AC13, §7 | S8 |
| M5 | MEDIUM | 22 | unit 66 S1, AC1, unit 67 S2 | S9 |
| M6 | MEDIUM | 23 | unit 67 S3, S10, AC3, §7 | S10 |
| M7 | MEDIUM | 24 | unit 67 S7, S8, AC7 | S11 |
| M8 | MEDIUM | 25 | unit 67 S17, AC15 | S12 |
| M9 | MEDIUM | 26 | unit 67 §7 | S13 |
| L1 | LOW | 2 | unit 67 S1, AC1 | S14 |
| L2 | LOW | 5 | unit 66 §7, S2 | S15 |
| L3 | LOW | 6 | unit 67 AC14 | S16 |
| L4 | LOW | 7 | unit 67 §4, §7 | S17 |
| L5 | LOW | 8 | unit 67 S16, unit 65 §4 | S18 |
| L6 | LOW | 9 | unit 67 §4 | S19 |
| L6 | LOW | 13 | unit 67 §4, §10, S19, AC17 | S20 |
| L7 | LOW | 12 | unit 66 §7, unit 67 §7 | S21 |
| L8 | LOW | 14 | unit 67 §10, S4 | S22 |
| L10 | LOW | 28 | unit 67 S8, AC7 | S23 |

That is 12 MEDIUM and 11 LOW findings by raw id. Ids 3, 18 and 21 share item M1, which describes the
defect `TOOL-dWitnessedBar-71` closes for id 11 at HIGH; S1 to S3 build what remains of M1's fix under
unit 71's plant.

## 2. Scope (IN)

- **S1** — id 3. The `-c init.defaultBranch=master` flag is graded on its own. Under unit 71 S1's
  hostile plant, section `2l` asserts that each fixture's `git symbolic-ref HEAD` prints
  `refs/heads/master`, so a fixture builder without the flag reds, naming the fixture and
  `refs/heads/main`. Observed by AC1.
- **S2** — id 18. The branch-file read is graded on its own. Each fixture asserts that the branch file
  it wrote exists at `.git/` plus its own `git symbolic-ref HEAD` output, so a builder that writes a
  literal branch name the fixture's HEAD does not name reds, naming the fixture. Observed by AC2.
- **S3** — id 21. Which config wins is stated where unit 67's AC5 is answered. Its acceptance-ledger
  line names both scopes: unit 67 S6's isolation masks the system and global files for every git call
  of section `2l`, the fixture `git init` included, and unit 71 S1's command-scope plant reaches that
  `git init` through the isolation. Observed by AC3.
- **S4** — id 4. Unit 67 AC6's recorder records only the calls unit 67 S7 bounds: a call whose argv
  holds `rev-parse --verify`, `symbolic-ref` or `for-each-ref`. Root discovery
  (`rev-parse --show-toplevel`) and the registration reads (`ls-files`) are outside the recorded set,
  and AC6's Red-when names the same population. Observed by AC4.
- **S5** — id 27. The recorded set is asserted non-empty and to hold each member S7 names, across
  unit 67 AC6's fixtures and an unborn one: the HEAD probe `rev-parse --verify --quiet HEAD^{commit}`,
  `symbolic-ref`, `for-each-ref`, and the `--sha` resolution `rev-parse --verify --quiet <sha>^{commit}`.
  A missing member fails naming it. Observed by AC5.
- **S6** — id 15. The `run-gates gov canary` row of `tools/gate-legs.json` gains `.githooks/pre-push`
  in its `guard`, as the `measure-legs selftest` row already carries it, because units 66, 67, 70 and
  72 make that leg's suite cut and source `read_green_file` from the hook. Observed by AC6.
- **S7** — id 16. A change to `.githooks/pre-push` alone selects the leg. Under the guard S6 writes, the
  runner's `changed()` test (`tools/run-gates/run-gates.sh:419`), a `git diff --quiet` over the guard's
  pathspecs, sees a commit touching only the hook as changed. Observed by AC7.
- **S8** — id 17. Unit 67 S15's comment in `tools/govkit/govkit.py` cites the other Python spelling as
  `<prefix>/memory-tree/gen_build_index.py`, the drained token govkit.py already uses, with no line
  numbers. The literal `tools/memory-tree/` path would be a new offender for
  `tools/check-install-prefix.sh`'s `GOVPFX` rule. This unit's §7 names `install-prefix (shipped surface)`.
  Observed by AC8.
- **S9** — id 22. Every key `read_green_file` reads is planted. The AC12 arm writes a second record
  holding, for each key, `<key><TAB>old<LF>` then `<key><TAB>new<CR><LF>`. The key list and the
  variable each key sets are derived from the `case` labels of the cut function `TOOL-dWitnessedBar-69`
  S1 builds, never typed. The arm asserts that the derived list is not empty and that each derived
  variable reads exactly `new`. Observed by AC9.
- **S10** — id 23. Unit 67 AC3's stand-ins cover the whole grid unit 67 S10 names:
  - `DirEntry.is_file(follow_symlinks=False)` raising `PermissionError`, with stderr naming the entry;
  - the age stat raising `PermissionError`, with stderr naming the entry;
  - an entry `peer-signers-l` whose `is_file(follow_symlinks=False)` is false and whose following
    `is_file()` is true, which must survive.

  The third is a stand-in entry rather than a real symlink, because creating a symlink on Windows
  needs a privilege the bar's host may lack, and a skipped case is no coverage. Unit 67 S3's second
  break, a sweep testing existence in place of `is_file(follow_symlinks=False)`, is named on this
  unit's §7 New-arm line with what it reaches. Observed by AC10.
- **S11** — id 24. Unit 67 AC7 gains stand-ins for the later probes. In an unborn fixture, a stand-in
  raising `subprocess.TimeoutExpired` and one raising `OSError` replace the `symbolic-ref` call, and
  the same two replace the `for-each-ref` call. Each of the four prints
  `unarmed p no HEAD: git not runnable: ` and no `Traceback`. Observed by AC11.
- **S12** — id 25. Unit 67 S17's single-assignment count reads every statement form its Red-when
  names. Comment lines are dropped first, then the count is
  `grep -cE '(^|[;&|[:space:]])((export|declare|readonly|local|typeset)([[:space:]]+-[a-zA-Z]+)*[[:space:]]+)?PM_SCRUB\+?=|printf[[:space:]]+-v[[:space:]]+PM_SCRUB([[:space:]]|$)|(^|[;&|[:space:]])read([[:space:]]+-[a-zA-Z]+)*[^#;]*[[:space:]]PM_SCRUB([[:space:]]|$)'`,
  the report's corrected predicate. It counts lines, so two writes on one line count once, which
  AC15's Red-when states. Observed by AC12.
- **S13** — id 26. Every staged break against a Python module, in unit 67's and this unit's arms, runs
  with that module's `__pycache__` cleared and `PYTHONDONTWRITEBYTECODE=1` exported, so no child
  interpreter writes bytecode either. A red is recorded only when the failing assertion is the one the
  break names: the `timeout=60` keyword for the break that omits `timeout=`, the `--sha` exit 2 for the
  one that omits the prefix check, and the read's exit for the one that omits the sweep's `OSError`
  catch. Observed by AC13.
- **S14** — id 2. The hook reads no `verdict` key, as an arm assertion. In a fresh `bash -c` that
  sources only the cut `read_green_file` and calls it on a record holding only `verdict<TAB>GREEN`,
  `compgen -v rec_` lists exactly the seven `rec_*` names and each is empty. Unit 67 AC1's two greps
  stay. Observed by AC14.
- **S15** — id 5. The gov canary's floor is a number. This unit's builder states `FLOOR_ASSERTIONS`
  absolutely, as the suite's comment at `tools/run-gates/run-gates.gov.test.sh:92-93` asks, at the
  count of assertions the built suite executes on a passing run, counted from its source with each
  loop counted at its population. The comment beside it names units 65 to 73. Unit 66's acceptance
  ledger, beside AC1, states unit 66's own net delta: one `rec_sha` compare in place of unit 65 AC12's
  hook-half assertions. Observed by AC15.
- **S16** — id 6. Unit 67 AC14 is read one line per file, with
  `grep -H '^\*\*Status:\*\*.* order [0-9]* '`, and is recorded as a guard against a later re-tie,
  since unit 67 S16's move was applied at landing. Observed by AC16.
- **S17** — id 7. This unit's §7 names `run-gates canary`, the leg whose suite runs `regen.py --check`,
  `--write` and `--list`, which unit 67 S19 writes and unit 67's §7 omits. NOT OBSERVED: the item is
  this spec's declared gate set, which the close runs; no criterion of a unit observes its own §7.
- **S18** — id 8. Unit 65's acceptance-ledger line for AC4 names the sentence
  `spec/2026-10-25-spec-TOOL-dWitnessedBar-65.md:191`, "Unit 22, the one unit at order 6, writes none
  of unit 47's files", as made stale by unit 67 S16, which found unit 22 writing 26 `kit.toml` files
  unit 47's reader reads. Observed by AC17.
- **S19** — id 9. Unit 67 §4 "Why one unit" counts eight non-seed files, not nine: its Files touched
  lists twelve, four of them the seed half's. NOT OBSERVED: a correction to spec text, which no built
  artifact carries. §4 Evidence gives the count's derivation.
- **S20** — id 13. Unit 67 S19's seam is the function-local `local LC_ALL=C` of `leg_log`
  (`tools/run-gates/run-gates.sh:301`), whose comment at `:296-299` gives S19's reason, and not the
  per-command prefix at `tools/check-wiring.sh:1155`. The report's `lib-unattended.sh:301` most likely
  names that `run-gates.sh` line under the wrong file. Unit 67 AC17's break is staged as
  `tools/run-gates/run-gates.evidence.test.sh:2169-2177` stages its own: a `sed` swapping
  `local LC_ALL=C` for `local LC_UNUSED=C`, then a `diff` count proving the copy changed. Observed by
  AC18.
- **S21** — id 12. The legs a default bar holds are derived, not counted by hand. Every named leg whose
  subject is `kit` or whose chunk is `selftests` is held unless GATE_SELFTESTS is set
  (`tools/run-gates/run-gates.sh:3129-3131`). Of unit 67's eighteen §7 legs that is fourteen, all but
  `govkit selfcheck`, `govkit refusal join`, `govkit acceptance matrix` and `memory hygiene`; of unit
  66's three it is two. The close sets GATE_SELFTESTS through `SELFTESTS_OWED_PATHS="tools/"`
  (`.unattended.conf:40`). Unit 66's and unit 67's acceptance ledgers, beside the criterion each arm
  covers first, state this in place of "the four kit legs". Observed by AC19.
- **S22** — id 14. Unit 67 S4's evaluated compare folds its word list with post-merge's own
  `${PM_SCRUB//$'\n'/ }` (`tools/run-gates/post-merge.sh:43`), so unit 63 S2's seam comment stays
  true. The account is: the evaluated compare reuses the fold, and the awk reader is the
  re-derivation S12's count guards. Observed by AC20.
- **S23** — id 28. The no-HEAD `--all` route states its empty case and its exit status. Where a root
  resolves, HEAD does not, and no registration exists, stdout is empty, stderr carries
  `seed: no HEAD: <reason>`, and the seed exits 0. Where registrations exist it exits 0 after printing
  their lines, as unit 15 S3's unarmed reporting does (§8 F2). Unit 67 AC7's Red-when reads "where a
  root resolves and at least one registration exists". Observed by AC21.

## 3. Non-goals (OUT)

- Re-wording unit 66's or unit 67's spec text. Each item is closed by what this pass builds or
  observes, and a claim or criterion it replaces is answered in that unit's acceptance ledger by name.
- The left-shift gates the report names: the spec lints, the checklist entries, the staged-red record
  refusal and the `gotchas.py` routing of the stale-bytecode class. No clause of this build names them.
  S5's membership, S9's derived key list and S13's matching rule are the regressions this batch builds.
- A real symlink fixture for S10. §2 S10 says why a stand-in entry replaces it.
- An exact-match exit status for `retrofit.unseeded = refuse` on the no-HEAD route. S23 states the
  default policy's status and leaves unit 15 S3's refuse branch as it is.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-66` — the AC12 record, its hook half and its floor clause, which S9, S14, S15 and S21 extend or answer (ids 2, 5, 12, 15, 22)
- **consumes-from** `TOOL-dWitnessedBar-67` — its fixtures, recorder, sweep grid, seed routes, `PM_SCRUB` count and arm, govkit comment, order guard and §7, which every other item amends (ids 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 21, 23, 24, 25, 26, 27, 28)
- **consumes-from** `TOOL-dWitnessedBar-69` — the loop's `case` labels, from which S9 derives every key it plants and S14 every variable it lists (ids 2, 22)
- **consumes-from** `TOOL-dWitnessedBar-71` — the command-scope hostile plant under which S1 to S3 grade the branch defences (ids 3, 18, 21, report item M1)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. The seed half, S1 to S5, S11
and S23, writes `tools/lib/resolve-python.test.sh` and the three `legacy_ledger.py` copies. The rest
writes `tools/run-gates/run-gates.gov.test.sh`, `tools/gate-legs.json` and `tools/govkit/govkit.py`.
So the two write sets are disjoint. Dispatch is strictly sequential, a shared order included
(`tools/workflows/unattended-build.js:76-80`), so a split would buy no concurrency. One unit holds all
23 findings, as `TOOL-dWitnessedBar-67` §4 held its 19.

### Evidence

- The `run-gates gov canary` guard is `["{prefix}/run-gates/", "{prefix}/gate-legs.json"]`
  (`tools/gate-legs.json:1184-1196`), and `measure-legs selftest`'s guard carries `.githooks/pre-push`.
  `changed()` is `! git diff --quiet "$BASE" -- "$@"` (`tools/run-gates/run-gates.sh:419`).
- The comment above `FLOOR_ASSERTIONS=16` says the floor is "Stated ABSOLUTELY, never as a delta"
  (`tools/run-gates/run-gates.gov.test.sh:92-94`). The suite prints `PASS (<n> assertions)` on a
  passing run (`:460-462`).
- `tools/check-install-prefix.sh:266` defines `GOVPFX`, and govkit.py's one `<prefix>/memory-tree`
  spelling is `tools/govkit/govkit.py:9522`. The `install-prefix (shipped surface)` row has no guard.
- S12's predicate, over `tools/run-gates/post-merge.sh` with comment lines dropped, prints 1. With
  `declare PM_SCRUB="x"`, `true; PM_SCRUB+=" y"`, `printf -v PM_SCRUB %s z` or
  `PM_SCRUB="${PM_SCRUB/GATE_SELECTION/}"` appended it prints 2; with `  # note PM_SCRUB="x"` it
  prints 1. Measured at `df0a656d`.
- Unit 67's Files touched lists twelve paths
  (`spec/2026-10-25-spec-TOOL-dWitnessedBar-67.md:220-231`), four of them the seed half's, which
  leaves eight; its line 174 says nine.
- `local LC_ALL=C` sits at `tools/run-gates/run-gates.sh:301` inside `leg_log`.
  `tools/check-wiring.sh:1155` is `LC_ALL=C tr -d '\000'`, a per-command prefix.
  `tools/run-gates/run-gates.evidence.test.sh:2171` swaps `local LC_ALL=C` for `local LC_UNUSED=C`,
  and `:2175-2177` counts the changed lines.
- Walking `tools/gate-legs.json` over unit 67's eighteen §7 names, fourteen have subject `kit` or
  chunk `selftests`. `govkit selfcheck`, `govkit refusal join` and `govkit acceptance matrix` have
  chunk `declarations`, and `memory hygiene` has chunk `records`.
- Unit 15 S3 has `retrofit.unseeded = unarmed` report an unseeded registration and exit 0
  (`spec/2026-10-25-spec-TOOL-dWitnessedBar-15.md:40-41`). Unit 65 S8 gives the no-root `--all` case
  an empty stdout and `seed: no HEAD: <reason>` on stderr, and no spec gives the no-HEAD route an
  exit status.

### Inventory

Minted: the failure lines of S1, S2 and S5, the stand-in entry `peer-signers-l` of S10, and S9's
second record. No function, constant, plant, flag or file. Naming cells: none apply.

### Migration

None: no item changes stored data. S6 changes one leg's guard, which widens when the leg runs and
narrows nothing.

### Rollout

Live at landing, at order 41, after every other unit of the build, the last of them
`TOOL-dWitnessedBar-71` and `TOOL-dWitnessedBar-72` at order 40. S15's floor is stated by this unit's
builder from the source, and the main loop compares it with the count the suite prints at the close.
S3, S16, S18, S20 and S21 are answered in other units' ledgers at the close.

### Files touched (estimate)

- `tools/run-gates/run-gates.gov.test.sh`
- `tools/gate-legs.json`
- `tools/govkit/govkit.py`
- `tools/lib/resolve-python.test.sh`
- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`

### Alternatives rejected

- **Two batches, seed half and the rest.** §4 "Why one unit".
- **Narrow unit 67 AC15's Red-when to the forms its predicate counts (id 25's first option).** A
  `declare` or `;`-joined write would then edit `PM_SCRUB` with the arm green, which is the finding.
- **Widen unit 67 S7's timeout to every git call the seed makes (id 4's second option).** Root
  discovery and `ls-files` sit outside the SHA resolution unit 65 S9's handler covers, so the bound
  would arrive with no handler for its exception.
- **A real symlink for S10.** §2 S10.

## 5. Production-readiness checklist

- security — S8 keeps a gov path out of a shipped file. S6 makes a hook-only change select the arm
  that grades the hook's push-decision read.
- perf / scale — S6 runs the gov canary on hook-only pushes, one suite more on those.
- error / empty / loading states — S10 and S11 turn rare filesystem and git failures into named
  outcomes; S23 states the empty registration case and its exit status.
- observability — S1, S2 and S5 name the fixture or member that failed.
- risks — S12's predicate can over-count a line that only reads `PM_SCRUB` through `read`, which reds
  loudly and names the line.
- testing — AC1 to AC21 by fixture, stand-in, scratch copy and ledger. The arms under §7 at the close.
- migration — none.
- user docs — none under `help/`. No user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When section `2l` runs under `TOOL-dWitnessedBar-71` S1's plant, each fixture's
  `git symbolic-ref HEAD` prints `refs/heads/master`. Against a scratch copy of section `2l` with
  `-c init.defaultBranch=master` deleted from the fixture builder, the arm fails naming the fixture
  and `refs/heads/main`.
  Red when: the flag can be deleted with the arm green.
- **AC2** — When each fixture is built, `test -f ".git/$(git symbolic-ref HEAD)"` holds in it. Against a
  scratch copy whose builder writes the branch file at `.git/refs/heads/main` literally, the arm fails
  naming the fixture.
  Red when: a branch file the fixture's HEAD does not name leaves the arm green.
- **AC3** — When `grep -n 'AC5' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-67*acceptance-ledger*`
  runs at the close, the line names `GIT_CONFIG_GLOBAL` as masked by the isolation and
  `GIT_CONFIG_COUNT` as reaching the fixture `git init`.
  Red when: AC5 is recorded green with no statement of which config scope it graded.
- **AC4** — When unit 67 AC6's probe runs in the missing-object fixture, no recorded call's argv holds
  `--show-toplevel` or `ls-files`, and every recorded call carries `timeout=60`.
  Red when: the recorder fails a correct build on a call S7 does not bound.
- **AC5** — When the same probe runs over the missing-object, unborn and one-commit `--sha` fixtures,
  the union of recorded argvs holds `HEAD^{commit}`, `symbolic-ref`, `for-each-ref` and a `--sha`
  value's `^{commit}`. With the `for-each-ref` call spawned outside `subprocess.run` in a scratch copy
  of the `tools/lib/` copy of `legacy_ledger.py`, the probe fails naming `for-each-ref`.
  Red when: the recorded set is empty or lacks a member, and the probe passes.
- **AC6** — When `python -c "import json, sys; print([l['guard'] for l in json.load(open(sys.argv[1])) if l['name'] == 'run-gates gov canary'])" tools/gate-legs.json`
  runs, the printed guard holds `.githooks/pre-push`.
  Red when: the gov canary's guard omits the hook its suite sources.
- **AC7** — When a scratch clone under `%TEMP%/<short-name>` commits a change to `.githooks/pre-push`
  alone, `git diff --quiet HEAD~1 -- tools/run-gates/ tools/gate-legs.json .githooks/pre-push` exits 1
  there, and the same command without `.githooks/pre-push` exits 0.
  Red when: a hook-only change leaves the gov canary's guard unchanged, so a scoped bar skips it.
- **AC8** — When `grep -n 'tools/memory-tree' tools/govkit/govkit.py` runs on the built tree, it prints
  nothing, and `grep -n '<prefix>/memory-tree/gen_build_index.py' tools/govkit/govkit.py` names a
  comment beside the segment rule's Python form that also names `1:x`.
  Red when: the comment spells the literal gov path, which `GOVPFX` reads as an offender.
- **AC9** — When the AC12 arm reads S9's record, the key list it derives from the cut function's `case`
  labels holds seven keys, and each derived variable is exactly `new`, three bytes. Against a scratch
  copy of `.githooks/pre-push` whose `selftests` case keeps the first of a repeated key, the arm fails
  naming `rec_st`.
  Red when: a key outside a typed sample keeps a CR or its first value with the arm green, or the
  derived list is empty and the arm passes.
- **AC10** — When unit 67 AC3's probe runs with `is_file(follow_symlinks=False)` raising
  `PermissionError` for one entry, and the age stat raising `PermissionError` for another, the read's
  verdict is unchanged, stderr names each entry once and holds no `Traceback`. The stand-in entry
  `peer-signers-l` is still present afterwards.
  Red when: an `is_file` or stat error raises into the read, or a symlink-following test removes the
  entry.
- **AC11** — When the seed runs in an unborn fixture under each of four stand-ins, `TimeoutExpired`
  and `OSError` from `symbolic-ref`, then the same two from `for-each-ref`, stdout opens
  `unarmed p no HEAD: git not runnable: ` and stderr holds no `Traceback`.
  Red when: a builder wraps only the `rev-parse` call and a later probe's failure escapes.
- **AC12** — When the `PM_SCRUB` arm counts over `tools/run-gates/post-merge.sh`, S12's predicate prints
  1. Over scratch copies with `declare PM_SCRUB="x"` and with `true; PM_SCRUB+=" y"` appended, it
  prints 2 and the arm fails naming `PM_SCRUB` and 2. Over one with `  # note PM_SCRUB="x"` appended it
  prints 1.
  Red when: a `declare`, `readonly`, `;`-joined or `printf -v` write of `PM_SCRUB` leaves the count at
  1, or a comment naming it raises the count.
  figure: the base count 1 is DERIVED by the predicate at observation time.
- **AC13** — When `grep -n 'PYTHONDONTWRITEBYTECODE' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-67*acceptance-ledger*`
  runs at the close, the lines for AC3 and AC6 name it, the cleared `__pycache__`, and the failing
  assertion each break names.
  Red when: a staged red against a `.py` module is recorded from a run that could load the previous
  break's bytecode.
- **AC14** — When `bash -c` sources the cut `read_green_file` and calls it on a record holding only
  `verdict<TAB>GREEN`, `compgen -v rec_` lists exactly `rec_blob`, `rec_fp`, `rec_man`, `rec_reused`,
  `rec_reused_cache`, `rec_sha` and `rec_st`, each empty. Against a scratch hook with a `verdict` case
  setting `rec_verdict`, the arm fails naming `rec_verdict`; with one setting `rec_sha` from `verdict`,
  it fails naming `rec_sha`.
  Red when: the hook gains a `verdict` read and the arm stays green.
- **AC15** — When `grep -n '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.gov.test.sh` runs on the built
  tree, it prints one number, with a comment naming units 65 to 73. At the close, the count in the
  suite's `PASS (<n> assertions)` line equals it, recorded in this unit's acceptance ledger beside
  AC15, and unit 66's ledger line for AC1 states unit 66's net delta as a number.
  Red when: the floor exceeds the executed count, or unit 66's floor clause is answered with no number.
  figure: the floor is DERIVED by this unit's builder from the source; the count is DERIVED by the
  close's run.
  permission: the suite runs only at the close.
- **AC16** — When `grep -H '^\*\*Status:\*\*.* order [0-9]* '` runs over unit 64's and unit 65's specs,
  it prints exactly two lines, one reading `order 36` and one `order 37`. Unit 67's acceptance-ledger
  line for AC14 records that reading as a re-tie guard and names `TOOL-dWitnessedBar-73`.
  Red when: AC14 is recorded as evidence the build made the move, or on a grep that matches body lines.
- **AC17** — When `grep -n 'AC4' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-65*acceptance-ledger*`
  runs at the close, the line names the sentence at `spec/2026-10-25-spec-TOOL-dWitnessedBar-65.md:191`
  as made stale by unit 67 S16, and names `TOOL-dWitnessedBar-73`.
  Red when: unit 65 still offers the sentence as the reason order 6's tie is honest, unanswered.
- **AC18** — When unit 67 AC17's break is staged at the close, `sed 's/^  local LC_ALL=C$/  local LC_UNUSED=C/'`
  over the bash reader's scratch copy changes exactly one line by a `diff` count, and the govkit
  selftest arm then fails naming `é:x`.
  Red when: the break is staged by an ad-hoc edit whose effect on the copy is never counted.
- **AC19** — When the `tools/gate-legs.json` walk of §4 Evidence runs over unit 67's eighteen §7 names,
  it prints fourteen held and the four that run. Unit 66's and unit 67's acceptance ledgers name the
  derived held set and `SELFTESTS_OWED_PATHS`.
  Red when: a ledger repeats "the four kit legs".
- **AC20** — When `grep -n 'PM_SCRUB//' tools/run-gates/run-gates.gov.test.sh` runs on the built tree,
  it names the evaluated compare of unit 67 S4.
  Red when: the arm's evaluation splits the list by its own rule while unit 63 S2's comment names the
  fold as its seam.
- **AC21** — When `seed --all` runs in a fixture where a root resolves, HEAD is unborn-broken and no
  registration exists, stdout is empty, stderr carries `seed: no HEAD: `, and the exit status is 0.
  With two registrations, it prints their two lines and exits 0.
  Red when: the empty case prints a placeholder line, or the route's exit status differs between the
  two cases.

## 7. Gates

`run-gates gov canary` · `run-gates canary` · `measure-legs selftest` · `govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `install-prefix (shipped surface)` · `python resolver (behaviour + inline parity + idiom ban)` · `shell-hygiene selftest` · `memory-hygiene self-test` · `codebase-map adopter e2e` · `codebase-map kit selftest` · `drift-audit selftest` · `memory hygiene`

`run-gates canary` is S17's, the leg that grades `regen.py`. `install-prefix (shipped surface)` is
S8's, and it has no guard, so it runs on every bar. Every leg here whose subject is `kit` or whose
chunk is `selftests` is held unless the main loop sets GATE_SELFTESTS at the close
(`tools/run-gates/run-gates.sh:3129-3131`), which `SELFTESTS_OWED_PATHS="tools/"` does
(`.unattended.conf:40`). Every staged break against a `.py` file runs as S13 states.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC9 AC10 AC12 AC14 AC20 · the every-key record, the full sweep grid, the widened `PM_SCRUB` count, the `rec_` listing and the folded compare, staged red by a `selftests` case that keeps its first value (reaches `rec_st`), by a sweep testing existence in place of `is_file(follow_symlinks=False)` (reaches `peer-signers-l`), by a `declare` write of `PM_SCRUB` (reaches the count) and by a `rec_verdict` read (reaches the listing) · FLOOR_ASSERTIONS stated absolutely by S15
New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC4 AC5 AC11 AC21 · the per-fixture branch assertions, the recorder's scope and membership, the later probes' stand-ins and the empty no-HEAD `--all`, staged red by deleting `-c init.defaultBranch=master` (reaches `refs/heads/main`), by a literal branch file (reaches the fixture's `test -f`) and by spawning `for-each-ref` outside `subprocess.run` (reaches the membership) · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. Units 66 and 67 are
  themselves derived and carry no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — What exit status does the no-HEAD route give (id 28)?** Options: (a) 0, with the populations
  reported unarmed, as unit 15 S3's `unarmed` policy reports an unseeded registration; (b) a non-zero
  status naming the missing HEAD. (b) fails a fresh install's seed before its first commit, which
  `TOOL-dWitnessedBar-47` and `TOOL-dWitnessedBar-61` exist to let through; veto 1 discards it.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the one survivor.
  widens: none · relaxes: none
- **F3 — Which account of the `PM_SCRUB` fold holds (id 14)?** Options: (a) unit 67 S4's evaluated
  compare folds with post-merge's own `${PM_SCRUB//$'\n'/ }`, so unit 63 S2's seam comment stays true;
  (b) an item replacing unit 63 S2's mandated comment, answered in unit 63's ledger and listed as an
  exception to this unit's §3. (b) rewords unit 63's required comment, which this unit's §3 first
  non-goal excludes; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, tie-broken
  by reuse of the fold unit 63 S2 already names.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 66 and 67: 12
  MEDIUM and 11 LOW findings, batched.

## 10. Reuse audit

Each item extends the seam its finding names. S1 to S3 extend section `2l` under unit 71's plant. S6
copies the `measure-legs selftest` guard entry for `.githooks/pre-push` (`tools/gate-legs.json`). S9 and
S14 extend the AC12 arm and read unit 69's `case` labels rather than a typed list. S20 reuses the
broken-copy idiom of `tools/run-gates/run-gates.evidence.test.sh:2169-2177` and cites the seam
`tools/run-gates/run-gates.sh:301`. S22 reuses post-merge's fold (`tools/run-gates/post-merge.sh:43`).
S12 takes the report's corrected predicate whole.

`python tools/codebase-map/reuse_lookup.py "assert a planted fixture byte survives the read before counting a mutation red"`
ranked `read`, `read_text`, `before` and `counts`, none a mutation check or a guard reader, so no
existing seam fits beyond those named above.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of units 66 and 67 find" --terms "gov canary guard pre-push PM_SCRUB count FLOOR_ASSERTIONS rec_ compgen peer-signers is_file timeout recorder GIT_CONFIG_COUNT"`
