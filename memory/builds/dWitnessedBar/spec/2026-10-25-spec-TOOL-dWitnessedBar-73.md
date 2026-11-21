# TOOL-dWitnessedBar-73 — the round-1 audit of units 66 and 67, its 23 minors batched: fixtures, populations, the hook guard, every key and filesystem call exercised, predicates and records

**Status:** CLOSED · rev-5 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 41 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-68-round7-fix-return.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 |
| [2026-10-25-build-TOOL-dWitnessedBar-73-deviation-731.md](../build/2026-10-25-build-TOOL-dWitnessedBar-73-deviation-731.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-73-deviation-732.md](../build/2026-10-25-build-TOOL-dWitnessedBar-73-deviation-732.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-73-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-73-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-73-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-73-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-73-widen-17.md](../build/2026-11-21-build-TOOL-dWitnessedBar-73-widen-17.md) | widen | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-round7-fix-brief.md) | research | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-88 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-73-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-73-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-73-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-73-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-73-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-73-reground-spec-writer.md) | journal | — |
| [2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-68-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 |

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
so this unit repairs no single unit and builds at order 41, after every unit it consumes from.

Units 66, 67, 69 and 71 have landed, at `a04b24c97`, `e1d569fc9`, `298369174` and `ced984440`, and
this spec is re-grounded over HEAD `d3b748b94`. Unit 67's own re-ground (its rev-4) and unit 65's (its
rev-5) left three findings no target: ids 7, 8 and 13. S17 and S19 are this spec's gate set and a
spec-text record, S18 and S20 are observed at HEAD, and S4 follows unit 67 S7 as it landed, on every
git call. The rest are built.

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
  plant, `run_planted_git`, which sets `init.defaultBranch=main` at command scope, section `2o` of
  `tools/lib/resolve-python.test.sh` asserts, where `ll_planted` is 1, that each of the corrupt-HEAD
  loop's five fixtures and the `child` fixture has `git symbolic-ref HEAD` printing
  `refs/heads/master`, so a fixture builder without the flag reds, naming the fixture and
  `refs/heads/main`. Observed by AC1.
- **S2** — id 18. The branch-file read is graded on its own. Each of the four loop fixtures whose
  `case` writes a branch file, `garbage`, `missing`, `loop` and `chain`, asserts after that write that
  `.git/` plus its own `git symbolic-ref HEAD` output, the loop's `ll_ref`, is a file, so a builder
  that writes a literal branch name the fixture's HEAD does not name reds, naming the fixture.
  `detached` writes `.git/HEAD` and `child` commits, so neither writes one. Observed by AC2.
- **S3** — id 21. Which config wins is stated where unit 67's AC5 is answered. Its acceptance-ledger
  line names both scopes: unit 67 S6's isolation masks the system and global files for every git call
  of section `2o`'s corrupt-HEAD and child blocks, the fixture `git init` included, and unit 71 S1's
  `GIT_CONFIG_COUNT` plant reaches that `git init` through the isolation. At HEAD the line names only
  an outer `GIT_CONFIG_GLOBAL`, which the isolation masks (§4 Evidence). Observed by AC3.
- **S4** — id 4. Unit 67 AC6's recorder records exactly the calls unit 67 S7 bounds. S7 landed as
  `timeout=60` on `tools/lib/legacy_ledger.py#_run_git`, the block's one git spawn, so root discovery
  (`rev-parse --show-toplevel`) and the registration read (`ls-files`) are bounded beside the SHA
  resolution and stay in the recorded set. The recorder records each call's argv beside its `timeout`,
  and the arm asserts that the missing-object fixture's set holds a `--show-toplevel` call and an
  `ls-files` call, each at 60. AC6's Red-when names that population. Observed by AC4.
- **S5** — id 27. The recorded set is asserted non-empty and to hold each member S7 names, across
  unit 67 AC6's two runs, the `--sha` seed in `child` and the seed in `corrupt-missing`, and a run in
  an unborn fixture, the loop's `chain`, which the seed reads as unborn: the HEAD probe
  `rev-parse --verify --quiet HEAD^{commit}`, `symbolic-ref`, `for-each-ref`, and the `--sha`
  resolution `rev-parse --verify --quiet <sha>^{commit}`. A missing member fails naming it. Observed
  by AC5.
- **S6** — id 15. The `run-gates gov canary` row of `tools/gate-legs.json` gains `.githooks/pre-push`
  in its `guard`, as the `measure-legs selftest` row already carries it, because units 66, 67, 70, 72
  and 74 make that leg's suite cut and source `read_green_file` from the hook. Observed by AC6.
- **S7** — id 16. A change to `.githooks/pre-push` alone selects the leg. Under the guard S6 writes, the
  runner's `tools/run-gates/run-gates.sh#changed`, a `git diff --quiet` over the guard's pathspecs,
  sees a commit touching only the hook as changed. Observed by AC7.
- **S8** — id 17. Unit 67 S15's comment beside `_check_exists_refused` in
  `tools/govkit/govkit.py#selfcheck` names the other Python spelling by file name and by memory-tree's
  `read_asks_args`, with no path. This unit spells it `<prefix>/memory-tree/gen_build_index.py`, the
  drained token govkit.py already uses once (`tools/govkit/govkit.py#_cmd_update`), with no line
  numbers. The literal `tools/memory-tree/` path would be a new offender for the `GOVPFX` rule of
  `tools/check-install-prefix.sh`. This unit's §7 names `install-prefix (shipped surface)`. Observed by
  AC8.
- **S9** — id 22. Every key `read_green_file` reads is planted. The AC12 arm writes a second record
  holding, for each key, `<key><TAB>old<LF>` then `<key><TAB>new<CR><LF>`. The key list and the
  variable each key sets are derived from the `case` labels of `.githooks/pre-push#read_green_file`,
  the loop `TOOL-dWitnessedBar-69` S1 built: each line of the cut reading `<label>) rec_<name>=`, never
  typed. The arm asserts that the derived list is not empty and that each derived variable reads
  exactly `new`, compared inside the subshell that sources the cut, which prints only the names that
  fail. Seven pairs at HEAD (DERIVED 2026-11-21 from the cut). Observed by AC9.
- **S10** — id 23. Unit 67 AC3's stand-ins, the gov suite's probe of
  `tools/run-gates/verdict_backends.py#remove_stale_signer_temps`, cover the whole grid unit 67 S10
  names. At HEAD the probe has three cases, `unlink`, `stat` raising `FileNotFoundError`, and `glob`.
  It gains:
  - `pathlib.Path.is_file(follow_symlinks=False)` raising `PermissionError`, with stderr naming the
    entry;
  - the age read, `Path.stat()`, raising `PermissionError`, with stderr naming the entry;
  - an aged entry `gov-signers-l` whose `is_file(follow_symlinks=False)` is false and whose following
    `is_file()` is true, which must survive.

  The third is a stand-in entry rather than a real symlink, because creating a symlink on Windows
  needs a privilege the bar's host may lack, and a skipped case is no coverage. Unit 67 S3's second
  break, a sweep testing existence in place of `is_file(follow_symlinks=False)`, which unit 67's ledger
  beside AC3 records red and its §7 New-arm line omits, is named on this unit's §7 New-arm line with
  what it reaches. Observed by AC10.
- **S11** — id 24. Unit 67 AC7 gains stand-ins for the later probes. In the unborn `chain` fixture, a
  stand-in for `subprocess.run` raising `subprocess.TimeoutExpired` and one raising `OSError` replace
  the call whose argv holds `symbolic-ref`, and the same two replace the one holding `for-each-ref`, as
  unit 65 AC7's two replace the `--verify` call. Each of the four prints
  `unarmed p no HEAD: git not runnable: ` and no `Traceback`, the reason `_run_git`'s exit-127 route
  gives. Observed by AC11.
- **S12** — id 25. Unit 67 S17's single-assignment count, the arm's `bsp_n` over
  `tools/run-gates/post-merge.sh`, reads every statement form its Red-when names. Comment lines are
  filtered out first, then the count is
  `grep -cE '(^|[;&|[:space:]])((export|declare|readonly|local|typeset)([[:space:]]+-[a-zA-Z]+)*[[:space:]]+)?PM_SCRUB\+?=|printf[[:space:]]+-v[[:space:]]+PM_SCRUB([[:space:]]|$)|(^|[;&|[:space:]])read([[:space:]]+-[a-zA-Z]+)*[^#;]*[[:space:]]PM_SCRUB([[:space:]]|$)'`,
  the report's corrected predicate. It counts lines, so two writes on one line count once, which
  AC15's Red-when states. Observed by AC12.
- **S13** — id 26. Every staged break against a Python module, in unit 67's and this unit's arms, runs
  with that module's `__pycache__` cleared and `PYTHONDONTWRITEBYTECODE=1` exported, so no child
  interpreter writes bytecode either; `-B` alone stops the write, not a stale read. A red is recorded
  only when the failing assertion is the one the break names: the `timeout=60` keyword for the break
  that omits `timeout=`, the `--sha` exit 2 for the one that omits the prefix check, and the read's exit
  for the one that omits the sweep's `OSError` catch. Observed by AC13.
- **S14** — id 2. The hook reads no `verdict` key, as an arm assertion. In a fresh `bash -c` that
  sources only the cut `read_green_file` and calls it on a record holding only `verdict<TAB>GREEN`,
  `compgen -v rec_` lists exactly the variables S9's derivation names, each empty. Unit 67 AC1's two
  greps stay. Observed by AC14.
- **S15** — id 5. The gov canary's floor is a number. This unit's builder states `FLOOR_ASSERTIONS`
  absolutely, as the comment above it asks (`tools/run-gates/run-gates.gov.test.sh@d3b748b94:244-245`),
  at the count of assertions the built suite executes on a passing run, counted from its source with
  each loop counted at its population, beside a `RAISED <old> -> <new>` comment in the suite's form
  naming this unit. It reads 54 at HEAD (PINNED 2026-11-21, `@d3b748b94:246`). Unit 66's acceptance
  ledger, beside AC1, states unit 66's own net delta as a number: 0, its builder having left every
  `a=$((a+1))` line as it was (DERIVED from that ledger's preamble). Units built after this one add arms,
  and `TOOL-dWitnessedBar-83` holds the close's equality. Observed by AC15.
- **S16** — id 6. Unit 67 AC14 is read one line per file. Its rev-4 reads `grep -H '^\*\*Status:\*\*'`,
  which matches each spec's header line alone, so the body-line half of id 6 is closed. Unit 67's
  acceptance-ledger line for AC14 is recorded as a guard against a later re-tie, naming this unit,
  since unit 67 S16's move was applied at landing. Observed by AC16.
- **S17** — id 7. Unit 67 landed writing no `tools/run-gates/regen.py`: its rev-4 S19 is present at
  HEAD and its Files touched omits the file, so id 7's premise has no write behind it. This unit's §7
  keeps `run-gates canary`, the leg whose suite runs `regen.py --check`, `--write` and `--list`, as its
  guard `{prefix}/` covers every file this unit writes under `tools/`. NOT OBSERVED: the item is this
  spec's declared gate set, which the close runs; no criterion of a unit observes its own §7.
- **S18** — id 8. Answered at HEAD. Unit 65's rev-5 (`453dfa886`) took out the sentence "Unit 22, the
  one unit at order 6, writes none of unit 47's files" from its §4, so the build holds one answer to
  whether units 22 and 47 share a read set, unit 67 S16's. Nothing is left for unit 65's ledger to
  name. Observed by AC17.
- **S19** — id 9. Unit 67 §4 "Why one unit", at its rev-4, says the rest writes four other files: its
  Files touched lists nine, four the seed half's, four the rest's, and `memory/project/shell-role.txt`,
  whose rows both halves widened, so its two write sets shared a file. NOT OBSERVED: a correction to
  spec text, which no built artifact carries. §4 Evidence gives the count's derivation.
- **S20** — id 13. Answered at HEAD. Unit 67's rev-4 S19 builds no reader and no `é:x` row, its §10
  cites no `LC_ALL` seam, and its AC17 is a grep with no staged break, so neither the seam citation id
  13 corrects nor the break it re-stages exists. The function-local form stays at
  `tools/run-gates/run-gates.sh#leg_log`, and the broken-copy idiom at
  `tools/run-gates/run-gates.evidence.test.sh@d3b748b94:2979`, for a later unit that builds such a
  reader. Observed by AC18.
- **S21** — id 12. The legs a default bar holds are derived, not counted by hand. Every named leg whose
  subject is `kit` or whose chunk is `selftests` is held unless GATE_SELFTESTS is set
  (`tools/run-gates/run-gates.sh#derive_hold_source`). Of unit 67's twenty-two §7 legs that is sixteen,
  all but `govkit selfcheck`, `govkit refusal join`, `govkit acceptance matrix`, `recall floor`,
  `portability (shell lines only shrink)` and `memory hygiene`; of unit 66's three it is two (DERIVED
  2026-11-21 by AC19's walk). The close sets GATE_SELFTESTS through `SELFTESTS_OWED_PATHS="tools/"`
  (`.unattended.conf@d3b748b94:40`). Unit 66's and unit 67's acceptance ledgers, beside the criterion
  each arm covers first, state the derived held set; at HEAD neither states which legs are held.
  Observed by AC19.
- **S22** — id 14. Unit 67 S4's evaluated compare, the arm's `bsp_bw` subshell, folds its word list
  with post-merge's own `${PM_SCRUB//$'\n'/ }` (`tools/run-gates/post-merge.sh@d3b748b94:46`) before
  it prints, so unit 63 S2's seam comment, the reader's header naming that fold, stays true. At HEAD it
  prints the unquoted `$PM_SCRUB`. The account is: the evaluated compare reuses the fold, and the awk
  reader is the re-derivation S12's count guards. Observed by AC20.
- **S23** — id 28. The no-HEAD `--all` route states its empty case and its exit status. Where a root
  resolves, HEAD does not, and no registration exists, stdout is empty, stderr carries
  `seed: no HEAD: <reason>`, and the seed exits 0, nothing being left unarmed. At HEAD that case prints
  nothing on either stream (§4 Evidence), so `tools/lib/legacy_ledger.py#run_seed_cli` and its two
  copies gain the stderr line. Where a registration with a seed exists the route exits 1 after printing
  every line, as it landed (§8 F2). Unit 67's acceptance-ledger line for AC7 answers its Red-when as
  reading "where a root resolves and at least one registration exists", naming this unit. Observed by
  AC21.

## 3. Non-goals (OUT)

- Re-wording unit 66's or unit 67's spec text, both CLOSED. Each item is closed by what this pass builds
  or observes, and a claim or criterion it replaces is answered in that unit's acceptance ledger by
  name.
- The left-shift gates the report names: the spec lints, the checklist entries, the staged-red record
  refusal and the `gotchas.py` routing of the stale-bytecode class. No clause of this build names them.
  S5's membership, S9's derived key list and S13's matching rule are the regressions this batch builds.
- A real symlink fixture for S10. §2 S10 says why a stand-in entry replaces it.
- An exact-match exit status for `retrofit.unseeded = refuse` on the no-HEAD route. S23 states the
  default policy's status and leaves unit 15 S3's refuse branch as it is.
- The order-41 siblings' arms in the same suite, `TOOL-dWitnessedBar-76`'s `check_canary_keys` among
  them. S9's second record grades values, not the CR-reach canary.
- Unit 28, deferred with three dOrderedCharter asks (TOOL-dWitnessedBar-101 to -103): no item here
  needs it. S6 edits `tools/gate-legs.json` as the tree holds it.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-66` — the AC12 record, its hook half and its floor clause, which S9, S14, S15 and S21 extend or answer (ids 2, 5, 12, 15, 22)
- **consumes-from** `TOOL-dWitnessedBar-67` — its fixtures, recorder, sweep grid, seed routes, `PM_SCRUB` count and arm, govkit comment, order guard and §7, which every other item amends (ids 2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 21, 23, 24, 25, 26, 27, 28)
- **consumes-from** `TOOL-dWitnessedBar-69` — the loop's `case` labels, from which S9 derives every key it plants and S14 every variable it lists (ids 2, 22)
- **consumes-from** `TOOL-dWitnessedBar-71` — the command-scope hostile plant, `run_planted_git`, under which S1 to S3 grade the branch defences (ids 3, 18, 21, report item M1)
- **hands-off** `TOOL-dWitnessedBar-78` — S7 observed through a probe derived from the manifest and seen red, the guard widened to the registry the arm reads, the ask rows the wider guard owes, S9's planting carried to `read_bar_file`, and the ledger lines for AC6 and AC7 (ids 4, 5, 11, 13, 19, 20, 26 of the round-1 spec audit of units 68 to 73)
- **hands-off** `TOOL-dWitnessedBar-82` — S15's absolute floor and its counting rule, which unit 82 restates after unit 78 (id 2 of the round-1 spec audit of units 74 to 78)
- **hands-off** `TOOL-dWitnessedBar-83` — AC15's equality, answered at this unit's pass and held at the close against the floor's derived owner (id 14 of the round-1 spec audit of units 74 to 78)
- **hands-off** `TOOL-dWitnessedBar-84` — S9's every-key arm, whose case-label derivation becomes the shared helper `_derive_case_keys` with a counted output (ids 13 and 22 of the round-1 spec audit of units 74 to 78)

## 4. Design

### Why one unit

M4 admits a second unit only so that the two halves build concurrently. The seed half, S1 to S5, S11
and S23, writes `tools/lib/resolve-python.test.sh` and the three `legacy_ledger.py` copies; the rest
writes `tools/run-gates/run-gates.gov.test.sh`, `tools/gate-legs.json` and `tools/govkit/govkit.py`.
Both halves grow a suite whose `memory/project/shell-role.txt` row equals its measured count, so both
widen that file and the write sets are not disjoint. Dispatch is strictly sequential, a shared order
included (`tools/workflows/unattended-build.js@d3b748b94:78-82`), so a split would buy no concurrency
either. One unit holds all 23 findings, as `TOOL-dWitnessedBar-67` §4 held its 19.

### Evidence

Read at HEAD `d3b748b94` on 2026-11-21; each probe ran on git 2.54.0.windows.1, GNU bash 5.3.9
(`x86_64-pc-cygwin`) and Python 3.15.2, PINNED 2026-11-21.

- The `run-gates gov canary` guard is `["{prefix}/run-gates/", "{prefix}/gate-legs.json"]`, subject
  `repo`, chunk `selftests`, and `measure-legs selftest`'s guard carries `.githooks/pre-push` (read
  from `tools/gate-legs.json`). `changed` is `! git diff --quiet "$BASE" -- "$@"` after its
  `GATE_FULL` and empty-`BASE` exits (`tools/run-gates/run-gates.sh#changed`).
- The gov suite cuts `read_green_file` with `awk '/^read_green_file\(\)/,/^}/'` from `.githooks/pre-push`
  and sources it in the canary and in `tools/run-gates/run-gates.gov.test.sh#check_cr_reached`. The
  cut's loop assigns through seven `case` lines of the form `<label>) rec_<name>=$_rg_v ;;`, labels
  `sha`, `fingerprint`, `manifest_blob`, `manifest`, `selftests`, `reused` and `reused_cache`, and
  resets the seven `rec_` variables first (DERIVED 2026-11-21 from `.githooks/pre-push#read_green_file`).
- In section `2o`, unit 67 S6's block exports `GIT_CONFIG_NOSYSTEM=1` and an empty `GIT_CONFIG_GLOBAL`,
  unit 71's `run_planted_git` prefixes `GIT_CONFIG_COUNT=2` to its one call, and the loop and `child`
  each build with `run_planted_git -c init.defaultBranch=master init -q --ref-format=files`
  (`tools/lib/resolve-python.test.sh@d3b748b94:1547-1555`, `:1609-1610`). The loop reads `ll_ref` and
  asserts `files` but not the branch; `detached` writes `.git/HEAD` (`@d3b748b94:1562-1568`). Unit
  67's ledger beside AC5 records the reading under an outer `GIT_CONFIG_GLOBAL` and names no
  `GIT_CONFIG_COUNT`.
- `_run_git` passes `timeout=60` and turns `OSError` and `subprocess.TimeoutExpired` into exit 127 with
  `git not runnable: <exception>`; `read_registrations` and `run_seed_cli`'s root discovery call it
  (`tools/lib/legacy_ledger.py#_run_git`, `#read_registrations`, `#run_seed_cli`). Unit 67 AC6's
  recorder keeps `kw.get("timeout")` alone and asserts `git calls <n> timeouts ['60']`
  (`tools/lib/resolve-python.test.sh@d3b748b94:1618-1631`). Unit 67's ledger records
  5 calls per run (DERIVED from that ledger). The three `legacy_ledger_py` copies are DERIVED by
  `git grep -l '>>> legacy_ledger_py' -- tools`.
- `read_head_sha` runs `symbolic-ref` only where the HEAD probe exits 1 printing nothing, then
  `for-each-ref`, so only an unborn HEAD such as `chain`'s reaches all three probes
  (`tools/lib/legacy_ledger.py#read_head_sha`).
- The sweep tests `p.is_file(follow_symlinks=False)` and `p.stat().st_mtime` in one `try`, silent on
  `FileNotFoundError`, naming the entry on any other `OSError`
  (`tools/run-gates/verdict_backends.py#remove_stale_signer_temps`).
- The comment above `FLOOR_ASSERTIONS=54` says the floor is "Stated ABSOLUTELY, never as a delta"
  (`tools/run-gates/run-gates.gov.test.sh@d3b748b94:244-246`), and the suite prints
  `PASS (<n> assertions)` on a passing run.
- `GOVPFX` is defined at `tools/check-install-prefix.sh@d3b748b94:425`; `grep -c 'tools/memory-tree'`
  and `grep -c '<prefix>/memory-tree'` over `tools/govkit/govkit.py` print 0 and 1 (PINNED
  2026-11-21). The `install-prefix (shipped surface)` row has no guard.
- S12's predicate, over `tools/run-gates/post-merge.sh` with comment lines dropped, prints 1. With
  `declare PM_SCRUB="x"`, `true; PM_SCRUB+=" y"`, `printf -v PM_SCRUB %s z` or
  `PM_SCRUB="${PM_SCRUB/GATE_SELECTION/}"` appended it prints 2; with `  # note PM_SCRUB="x"` it
  prints 1 (PINNED 2026-11-21 at `d3b748b94`). The arm's count at HEAD is the line-leading form
  (`tools/run-gates/run-gates.gov.test.sh@d3b748b94:1115`).
- The evaluated compare prints `printf '%s\n' $PM_SCRUB` unfolded
  (`tools/run-gates/run-gates.gov.test.sh@d3b748b94:1106`). A `$'\n'` inside `$(...)` keeps its one
  byte on this node, where a `$'\r'` there reads empty, so the fold works inside the subshell (PINNED
  2026-11-21, this probe).
- In a `git init` whose branch file holds `garbage`, one file staged and no `kit.toml`, `seed --all`
  exited 0 printing nothing on either stream (PINNED 2026-11-21, this probe). The route's last line
  is `return 1 if any(reg.seed for reg in picked) else 0`, and unit 67 AC7's arm expects `rc=1` over
  `p` and `x1` (`tools/lib/resolve-python.test.sh@d3b748b94:1586-1597`). Unit 65 S8 gives the no-root
  `--all` an empty stdout, `seed: no HEAD: <reason>` on stderr and exit 1.
- Unit 67 at rev-4 lists nine paths under Files touched and says "four other files" in "Why one unit";
  its §7 names twenty-two legs (DERIVED 2026-11-21 from its spec). Walking `tools/gate-legs.json` over
  those names, sixteen have subject `kit` or chunk `selftests` (DERIVED 2026-11-21).
- `local LC_ALL=C` is `tools/run-gates/run-gates.sh#leg_log`'s first line; `grep -rl 'é:x' tools/`
  prints nothing (PINNED 2026-11-21).

### Inventory

Minted: the failure lines of S1, S2 and S5, the stand-in entry `gov-signers-l` of S10, S9's second
record, and S23's empty-case stderr line. No function, constant, plant, flag or tracked file. Naming
cells: none apply.

### Migration

None: no item changes stored data. S6 changes one leg's guard, which widens when the leg runs and
narrows nothing.

### Rollout

Live at landing, at order 41, after order 40's `TOOL-dWitnessedBar-71`, `-72`, `-74` and `-75`. Order
41 also holds units 76, 77, 79, 80 and 81, and a tie sorts by id string
(`tools/workflows/unattended-build.js@d3b748b94:692-697`), so this unit builds first; unit 76 writes
the gov suite and its shell-role row after it. S15's floor is stated by this unit's builder from the
source. S3, S16, S21 and S23's ledger lines are written in other units' ledgers at the close.

### Files touched (estimate)

The `legacy_ledger.py` population is every copy of the `legacy_ledger_py` block, three files (DERIVED
by `git grep -l '>>> legacy_ledger_py' -- tools`), held identical by the resolver suite's parity part.
Each suite grown past its `memory/project/shell-role.txt` row is widened by `ratchet.py widen`, its
widen record declared through `--dispatch`, as unit 71 did.

- `tools/run-gates/run-gates.gov.test.sh`
- `tools/gate-legs.json`
- `tools/govkit/govkit.py`
- `tools/lib/resolve-python.test.sh`
- `tools/lib/legacy_ledger.py`
- `tools/memory-tree/legacy_ledger.py`
- `tools/gate-lint/legacy_ledger.py`
- `memory/project/shell-role.txt`

### Alternatives rejected

- **Two batches, seed half and the rest.** §4 "Why one unit".
- **Narrow unit 67 AC15's Red-when to the forms its predicate counts (id 25's first option).** A
  `declare` or `;`-joined write would then edit `PM_SCRUB` with the arm green, which is the finding.
- **Narrow the recorder to the SHA-resolution calls (id 4's first option).** Unit 67 S7 landed on
  `_run_git`, which root discovery and `ls-files` go through and whose exit-127 route handles their
  exception, so narrowing would leave two bounded calls unrecorded.
- **A real symlink for S10.** §2 S10.

## 5. Production-readiness checklist

- security — S8 keeps a gov path out of a shipped file. S6 makes a hook-only change select the arm
  that grades the hook's push-decision read.
- perf / scale — S6 runs the gov canary on hook-only pushes, one suite more on those.
- error / empty / loading states — S10 and S11 turn rare filesystem and git failures into named
  outcomes; S23 states the empty registration case and its exit status.
- observability — S1, S2 and S5 name the fixture or member that failed; S23's empty case names its
  reason.
- risks — S12's predicate can over-count a line that only reads `PM_SCRUB` through `read`, which reds
  loudly and names the line.
- testing — AC1 to AC21 by fixture, stand-in, scratch copy and ledger. The arms under §7 at the close.
- migration — none.
- user docs — none under `help/`. No user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When section `2o` runs under `TOOL-dWitnessedBar-71` S1's plant, each loop fixture's and
  `child`'s `git symbolic-ref HEAD` prints `refs/heads/master`. Against a scratch copy of the suite with
  `-c init.defaultBranch=master` deleted from the loop's builder, the arm fails naming the fixture and
  `refs/heads/main`.
  Red when: the flag can be deleted with the arm green.
- **AC2** — When the `garbage`, `missing`, `loop` and `chain` fixtures are built,
  `test -f "$LLC/.git/$ll_ref"` holds in each after its branch file is written. Against a scratch copy
  whose builder writes the branch file at `.git/refs/heads/main` literally, the arm fails naming the
  fixture.
  Red when: a branch file the fixture's HEAD does not name leaves the arm green.
- **AC3** — When `grep -n 'AC5' memory/builds/dWitnessedBar/build/*TOOL-dWitnessedBar-67*acceptance-ledger*`
  runs at the close, the line names `GIT_CONFIG_GLOBAL` as masked by the isolation and
  `GIT_CONFIG_COUNT` as reaching the fixture `git init`.
  Red when: AC5 is recorded green with no statement of which config scope it graded.
- **AC4** — When unit 67 AC6's probe runs in the missing-object fixture, the recorded argvs hold a
  `--show-toplevel` call and an `ls-files` call, and every recorded call carries `timeout=60`.
  Red when: the recorded set departs from the calls `_run_git` spawns, or one of them runs unbounded
  with the arm green.
- **AC5** — When the same probe runs over `corrupt-missing`, `chain` and the `--sha` seed in `child`,
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
  nothing, and `grep -n '<prefix>/memory-tree/gen_build_index.py' tools/govkit/govkit.py` names the
  comment beside `_check_exists_refused`, which also names `1:x`.
  Red when: the comment spells the literal gov path, which `GOVPFX` reads as an offender.
- **AC9** — When the AC12 arm reads S9's record, the key list it derives from the cut function's `case`
  labels holds seven keys, and each derived variable is exactly `new`, three bytes. Against a scratch
  copy of `.githooks/pre-push` whose `selftests` case keeps the first of a repeated key, the arm fails
  naming `rec_st`.
  Red when: a key outside a typed sample keeps a CR or its first value with the arm green, or the
  derived list is empty and the arm passes.
  figure: seven is DERIVED from the cut at observation time.
- **AC10** — When unit 67 AC3's probe runs with `is_file(follow_symlinks=False)` raising
  `PermissionError` for one entry, and the age stat raising `PermissionError` for another, the call
  returns, stderr names each entry once and holds no `Traceback`. The stand-in entry `gov-signers-l` is
  still present afterwards.
  Red when: an `is_file` or stat error raises out of the sweep, or a symlink-following or existence
  test removes the entry.
- **AC11** — When the seed runs in the `chain` fixture under each of four stand-ins, `TimeoutExpired`
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
  tree, it prints one number, and the comment beside it names `TOOL-dWitnessedBar-73`. At the close, in
  a scratch clone checked out at this unit's pass commit, the count in the suite's
  `PASS (<n> assertions)` line equals it, recorded in this unit's acceptance ledger beside AC15, and
  unit 66's ledger line for AC1 states unit 66's net delta as a number.
  Red when: the floor exceeds the executed count, or unit 66's floor clause is answered with no number.
  figure: the floor is DERIVED by this unit's builder from the source; the count is DERIVED by the
  close's run.
  permission: the suite runs only at the close.
- **AC16** — When `grep -H '^\*\*Status:\*\*.* order [0-9]* '` runs over unit 64's and unit 65's specs,
  it prints exactly two lines, one reading `order 36` and one `order 37`. Unit 67's acceptance-ledger
  line for AC14 records that reading as a re-tie guard and names `TOOL-dWitnessedBar-73`.
  Red when: AC14 is recorded as evidence the build made the move, or on a grep that matches body lines.
- **AC17** — When `grep -c "writes none of unit 47's files" memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-65.md`
  runs, it prints 0, and `git log -S` for that sentence over the file names `453dfa886`.
  Red when: unit 65 again offers the sentence as the reason order 6's tie is honest.
- **AC18** — When `grep -rl 'é:x' tools/` runs, it prints nothing, and `grep -cE 'check-wiring[.]sh:[0-9]+'`
  over `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-67.md` prints 0.
  Red when: an `é:x` arm lands with its break staged by an ad-hoc edit whose effect on the copy is never
  counted.
- **AC19** — When the `tools/gate-legs.json` walk of §4 Evidence runs over unit 67's twenty-two §7
  names, it prints sixteen held and the six that run. Unit 66's and unit 67's acceptance ledgers name
  the derived held set and `SELFTESTS_OWED_PATHS`.
  Red when: a ledger repeats "the four kit legs" or states no held set.
  figure: sixteen and six are DERIVED by the walk at observation time.
- **AC20** — When `grep -n 'PM_SCRUB//' tools/run-gates/run-gates.gov.test.sh` runs on the built tree,
  it names the `bsp_bw` line of unit 67 S4's evaluated compare beside the reader's header comment,
  which alone matches at HEAD.
  Red when: the arm's evaluation splits the list by its own rule while unit 63 S2's comment names the
  fold as its seam.
- **AC21** — When `seed --all` runs in a fixture where a root resolves, the branch file holds `garbage`
  and no registration exists, stdout is empty, stderr carries `seed: no HEAD: `, and the exit status is
  0. In the `garbage` fixture with its two registrations, `p` and `x1`, it prints their two lines and
  exits 1.
  Red when: the empty case prints a placeholder line or nothing on stderr, or either case's exit status
  departs from S23's.

## 7. Gates

`run-gates gov canary` · `run-gates canary` · `measure-legs selftest` · `govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `python resolver (behaviour + inline parity + idiom ban)` · `shell-hygiene selftest` · `memory-hygiene self-test` · `codebase-map adopter e2e` · `codebase-map kit selftest` · `drift-audit selftest` · `policy fixtures` · `portability (shell lines only shrink)` · `memory hygiene`

`run-gates canary` is S17's. `install-prefix (shipped surface)` is S8's, and it has no guard, so it
runs on every bar. The two recall legs and `portability (shell lines only shrink)` read the widened
`memory/project/shell-role.txt` rows. Every leg here whose subject is `kit` or whose chunk is
`selftests`, twelve of the nineteen (DERIVED 2026-11-21 by AC19's walk), is held unless the main loop
sets GATE_SELFTESTS at the close (`tools/run-gates/run-gates.sh#derive_hold_source`), which
`SELFTESTS_OWED_PATHS="tools/"` does (`.unattended.conf@d3b748b94:40`). Every staged break against a
`.py` file runs as S13 states.

New arm: tools/run-gates/run-gates.gov.test.sh · covers AC9 AC10 AC12 AC14 AC20 · the every-key record, the full sweep grid, the widened `PM_SCRUB` count, the `rec_` listing and the folded compare, staged red by a `selftests` case that keeps its first value (reaches `rec_st`), by a sweep testing existence in place of `is_file(follow_symlinks=False)` (reaches `gov-signers-d` and `gov-signers-l`), by a `declare` write of `PM_SCRUB` (reaches the count) and by a `rec_verdict` read (reaches the listing) · FLOOR_ASSERTIONS stated absolutely by S15
New arm: tools/lib/resolve-python.test.sh · covers AC1 AC2 AC4 AC5 AC11 AC21 · the per-fixture branch assertions, the recorder's argvs and membership, the later probes' stand-ins and the empty no-HEAD `--all`, staged red by deleting `-c init.defaultBranch=master` from the loop's builder (reaches `refs/heads/main`), by a literal branch file (reaches the fixture's `test -f`), by spawning `for-each-ref` outside `subprocess.run` (reaches the membership) and by dropping S23's stderr line from the `tools/lib/` copy (reaches the empty case) · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec that carries nothing and is derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. Units 66 and 67 are
  themselves derived and carry no clause, so (b) has nothing to split; veto 1 discards it. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none
- **F2 — What exit status does the no-HEAD route give (id 28), now that its populated case has landed
  at 1 (forced by the re-ground)?** The rev-4 answer, 0 for both cases, rested on a fresh install's
  seed taking this route; unit 61's unborn route now arms a commitless tree at the null SHA, and
  `run_seed_cli` exits 1 where a seeded registration is left unarmed. Options: (a) state the landed
  rule, 1 where a registration with a seed is left unarmed and 0 where none is, so the empty case exits
  0, with `seed: no HEAD: <reason>` on stderr; (b) the empty case exits 1, as the no-root `--all` does;
  (c) 0 for both, as rev-4 had it. (c) reverts the status four landed arms grade at `rc=1`, units 63
  AC4, 64 AC1, 65 AC7 and 67 AC7; veto 1 discards it. (b) splits the landed rule, under which a
  `seed = []` registration alone exits 0, and the no-root route exits before it can know whether any
  registration exists. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, tie-broken by reuse of the
  rule `run_seed_cli` already applies.
  widens: none · relaxes: AC21's one exit status across both cases, which the landed populated route's
  1 forbids
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
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring the consumes-from
  edge of TOOL-dWitnessedBar-78, promoted by the round-1 spec audit of units 68 to 73; nothing else
  moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-82, TOOL-dWitnessedBar-83 and TOOL-dWitnessedBar-84, promoted by the
  round-1 spec audit of units 74 to 78; nothing else moved.
- rev-4 · 2026-11-19 · §7 · the leg line gains `policy fixtures`, whose manifest guard holds the §4 path
  `tools/gate-legs.json`, per brief 2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief; nothing else
  moved.
- rev-5 · 2026-11-21 · §1 to §10 · S1 to S23 · AC1 to AC5 · AC8 to AC11 · AC15 · AC17 to AC21 ·
  re-grounded over units 66, 67, 69 and 71 as landed, per 2026-11-19-prompt-TOOL-dWitnessedBar-73-reground-brief:
  section `2l` reads `2o` and the signer prefix `gov-signers-`; S4 follows unit 67 S7's bound on every
  `_run_git` call; S17, S18 and S20 record the premises unit 67's rev-4 and unit 65's rev-5 removed;
  S21's counts are re-derived over unit 67's twenty-two legs; S23's populated status takes the landed 1
  (§8 F2); Files touched gains `memory/project/shell-role.txt` and the leg line `recall floor` and
  `portability (shell lines only shrink)`; citations move to `path#symbol` or blob-pinned lines.

## 10. Reuse audit

Each item extends the seam its finding names. S1 to S3 extend section `2o` under unit 71's
`run_planted_git`. S4 and S5 extend unit 67 AC6's `LL_RECORD` stand-in, and S11 unit 65 AC7's
`--verify` stand-in shape. S6 copies the `measure-legs selftest` guard entry for `.githooks/pre-push`
(`tools/gate-legs.json`). S9 and S14 extend the AC12 arm and read unit 69's `case` labels rather than
a typed list. S10 extends unit 67's sweep probe over
`tools/run-gates/verdict_backends.py#remove_stale_signer_temps`. S22 reuses post-merge's fold
(`tools/run-gates/post-merge.sh@d3b748b94:46`). S12 takes the report's corrected predicate whole.
S23 extends `tools/lib/legacy_ledger.py#run_seed_cli`'s no-HEAD branch with the line its no-root
branch already prints.

`python tools/codebase-map/reuse_lookup.py "derive the keys a shell case statement assigns from its labels"`,
run on 2026-11-21, ranked `key`, `keys`, `run_selftest_cases` and `derive_tool_root`, none a reader of
`case` labels; `tools/run-gates/run-gates.sh#read_record_keys` reads a record's keys, not a function's.
`python tools/codebase-map/reuse_lookup.py "assert a planted fixture byte survives the read before counting a mutation red"`
ranked `read`, `read_text`, `before` and `counts`, none a mutation check or a guard reader. So no
existing seam fits beyond those named above.

Recall terms used: `python tools/memory-recall/query.py "what did the round-1 audit of units 66 and 67 find" --terms "gov canary guard pre-push PM_SCRUB count FLOOR_ASSERTIONS rec_ compgen gov-signers is_file timeout recorder GIT_CONFIG_COUNT"`
