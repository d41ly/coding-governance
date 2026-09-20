# TOOL-dDerivedDocket-1 — held-suite failure baseline

**Status:** SPECCED · rev-4 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md) | spec-audit | TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round2.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round2.md) | spec-audit | TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |

<!-- /gen:spec-records -->

## 1. Goal

The kit self-test suites are held off the merge bar, and several are red at BASE for reasons this
build did not cause (TOOL-aHoistedPass-36, TOOL-aHoistedPass-38, TOOL-aQuenchedHarness-9). A unit
that is allowed to run them (D12-h, D12-i8) therefore cannot reach GREEN, and a red run tells it
nothing about its own change. Give the on-demand self-test runners a baseline mode that runs each
selected suite at a named base R as well as at the working tree L, and reports NEW, INHERITED and
FIXED failure sets. The runner's attributed verdict then becomes the verification criterion every
later self-test unit in this build uses. That verdict is `verdict clean`: no NEW FAIL, no DEAD PROBE
at L, and no OVER BUDGET at L. It is stated once, in S10. Built first, by owner ruling D12-i11.

## 2. Scope (IN)

- **S1** `tools/run-gates/run-selftests.sh` gains `--attribute <R>`, composable with `--kit <dir>`.
  For every selected suite it runs the suite at L exactly as the no-flag mode does, runs R's copy of
  the same suite in a detached scratch worktree at R, and prints the three sets per suite plus one
  summary line `attributed N of M suite(s) against <R8>`. Observed by AC1 and AC5.
- **S2** One normaliser, applied identically to both sides, reduces each FAIL line to what does not
  vary between two runs of an unchanged suite. Observed by AC1.
- **S3** A suite that exits non-zero on a side while its FAIL set on that side is empty is a DEAD
  PROBE on that side, with or without a count line (KF14, as the red-attribution unit applies it).
  `N` counts only suites with a verdict on both sides. A DEAD PROBE at R alone gives S(R) no members.
  Every line of S(L) then reads NEW, exactly as for `absent`, and nothing on that suite reads
  INHERITED. Observed by AC2, AC9 and AC12.
- **S4** The R-side set is cached per (R, suite, suite-file blob at R), written only after an R run
  that completed. Observed by AC4.
- **S5** Exit status under `--attribute`: 1 when any NEW FAIL, any DEAD PROBE at L, or any OVER
  BUDGET verdict at L exists, else 0. A DEAD PROBE at L exits 1 whatever R shows, a suite dead on
  both sides included. A DEAD PROBE at R alone never exits 1. INHERITED and FIXED are reported and
  never fail. The R side carries no budget verdict (F3). The summary line names each cause
  separately, with DEAD counted per side, so a reader can tell a cost verdict from a NEW failure and
  an inherited abort from one this tree caused. The line ends in `verdict clean` or `verdict red`,
  which always agrees with the exit status. The no-flag mode's output and exit are unchanged.
  Observed by AC1, AC2, AC3, AC8, AC10 and AC12.
- **S6** `tools/unattended/run-unattended-gates.sh --attribute <R>` forwards the flag to its
  delegated self-test half and prints one line saying its `--checks` half is not attributed.
  Observed by AC6.
- **S7** Two backlog rows are disposed at build time, with commit 8b29f0b9 as the evidence. That
  commit, an ancestor of BASE, already fixed the bare `$1` abort in the case pattern the rows cite
  at line 4107, which sits at `tools/unattended/unattended.test.sh:4123` at BASE. The first row,
  TOOL-aTracedSpawn-1, is CLOSED citing it. The second, TOOL-aHoistedPass-36, records its stop (1)
  as fixed by it and stays OPEN for its stop (2). NOT OBSERVED by a criterion: these are records,
  and check 13 and the row grammar grade their shape.
- **S8** The compensating-check wording moves from "a GREEN verdict" to the S10 criterion. The new
  wording is: "`--attribute` against the build's BASE reads `verdict clean` — no NEW FAIL, no DEAD
  PROBE at L and no OVER BUDGET at L — and every suite reporting an INHERITED FAIL or a DEAD PROBE at
  R is named by a filed backlog record". It lands in the four places that state the old wording: the
  `tools/unattended/kit.toml` self-test block, both runner headers, and the DoD sentence in
  `.githooks/gate-env.sh`. Observed by AC7.
- **S9** The run-gates and unattended kit version markers move, because shipped bytes change in
  both kits. Observed by AC11: the `kit version markers` leg grades only presence and pair agreement,
  which BASE's values already satisfy. This is the build's one move for each of the two kits: every
  later unit's bytes in either kit ride it. The move is read against two values and never against a
  number pinned when the spec was written: the value at BASE, and the value at the tip of
  `origin/main` after a fetch at this unit's pass, on every carrier `tools/check-kit-versions.sh`
  names. The courtesy unattended marker in `tools/unattended/gate-guard.js`, which that gate does not
  read, moves with them. The landing reconcile re-checks both kits against the advertised tip.
- **S10** The criterion this unit hands every self-test unit, stated once. When the unit's single
  `--attribute <BASE>` run is read, its summary reads `verdict clean`, and every suite it reports
  with INHERITED lines or `DEAD PROBE at R` is named by its file path in a filed backlog row or ask
  that is not CLOSED, as `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'`
  shows. A consumer reads the verdict token and never the NEW count alone, and never the exit of a
  wrapper that also runs unattributed checks. `<BASE>` is the base the consuming spec's status
  header names, `fb07ca25` since the 2026-09-16 regrounding, and never the run-state file's pinned
  `base:` fact, which still reads `abac6d59`: against that sha every failure the intervening
  default-branch commits introduced would read NEW. Observed by AC7, where the carriers name it, and
  AC12.

## 3. Non-goals (OUT)

- Attributing MERGE-BAR legs. Re-running a red bar leg at R, per-leg signatures and the KF14
  classification belong to the red-attribution unit; this unit handles self-test suites only.
- Fixing any inherited failure. TOOL-aHoistedPass-38's open causes, stop (2) of
  TOOL-aHoistedPass-36, and the suites TOOL-aQuenchedHarness-9 measured red all stay filed. This unit
  makes them attributable, not green. Whatever the unattended suites report at BASE is data.
- Auto-filing an ask per INHERITED FAIL. That is the inherited-red policy unit's, after the flip.
- A periodic run of the held population. TOOL-aBoundedCeiling-10's periodic half is the remote-CI
  unit's scheduled held-suite run (D12-i12); this unit only advances that row.
- Any change to a budget row in `tools/run-gates/selftest-budgets.txt`, or to how the merge bar
  reads `GATE_SELFTESTS=1`. The bar's verdict stays a boolean here.
- Attributing the `--checks` half of `run-unattended-gates.sh`. Those four legs are repository
  checks on the bar, which the red-attribution unit owns.

### Edges

- **consumes-from** external — a pinned base sha supplied by the caller, normally the run's BASE.
  This unit never chooses R.
- **hands-off** `TOOL-dDerivedDocket-2` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the held push-main self-test suite, read through `--attribute` against this
  build's BASE.
- **hands-off** `TOOL-dDerivedDocket-3` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the unattended suites that unit's verification reads.
- **hands-off** `TOOL-dDerivedDocket-4` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the unattended suites that unit's verification reads.
- **hands-off** `TOOL-dDerivedDocket-5` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the unattended suites that unit's verification reads.
- **hands-off** `TOOL-dDerivedDocket-16` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the unattended suites that unit's verification reads.
- **hands-off** `TOOL-dDerivedDocket-17` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the unattended suites that unit's verification reads.
- **hands-off** `TOOL-dDerivedDocket-18` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the unattended suites that unit's verification reads.
- **hands-off** `TOOL-dDerivedDocket-22` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the unattended suites that unit's verification reads.
- **hands-off** `TOOL-dDerivedDocket-23` — the FAIL-line normaliser and the detached scratch
  worktree runner at R, which that unit reuses to re-run a red bar leg at R.
- **hands-off** `TOOL-dDerivedDocket-24` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the unattended suites that unit's verification reads.
- **hands-off** `TOOL-dDerivedDocket-27` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the unattended suites that unit's verification reads.
- **hands-off** `TOOL-dDerivedDocket-28` — the S10 criterion, `verdict clean` with every inherited
  suite filed, over the unattended suites that unit's verification reads.
- **hands-off** `TOOL-dDerivedDocket-30` — `--attribute` and the S10 criterion, `verdict clean` with
  every inherited suite filed, under which that unit's verification reads the unattended suites,
  since they are red at BASE.
- **hands-off** `TOOL-dDerivedDocket-32` — both runner headers as S8 leaves them, whose "nothing
  runs automatically" sentence that unit corrects, and the run-gates and unattended version moves
  (S9) its header edits ride.

## 4. Design

### Data model

For one suite, S(L) and S(R) are sets of normalised FAIL lines.

```
NEW        = S(L) - S(R)
INHERITED  = S(L) & S(R)
FIXED      = S(R) - S(L)
```

A line is a FAIL line when it matches the selector the runner already greps its FAIL tail with,
`^(FAIL|nope|.*FAILED)`. The selector is shared, not re-spelled: one variable feeds both the tail
print and the attribution, so the two cannot disagree about what a failure is. The whole captured
output is read, not the four-line tail the no-flag mode prints.

Output, one block per suite, then the summary:

```
attr  <suite name>  NEW <n> · INHERITED <n> · FIXED <n> · R <sha8> fresh|cached|absent
        NEW        <normalised line>
        INHERITED  <normalised line>
        FIXED      <normalised line>
attr  <suite name>  DEAD PROBE at L|R — exit <rc>, no FAIL line
attr  <suite name>  OVER BUDGET at L — <n>s against <budget>s
attributed N of M suite(s) against <sha8> · NEW <n> · INHERITED <n> · FIXED <n> · DEAD L <n> · DEAD R <n> · OVER <n> · verdict clean|red
```

`absent` means the suite does not exist at R, so all of S(L) is NEW, and the line says so.
A `DEAD PROBE at R` reads the same way for that suite: S(R) has no members, all of S(L) is NEW, and
the block says so. `verdict clean` requires NEW 0, DEAD L 0 and OVER 0.

### The normaliser

It strips, in this order: the absolute root of L and of the scratch worktree, each in forward-slash,
backslash and MSYS `/c/` spellings; `mktemp`-shaped directory names; durations matching
`[0-9]+(\.[0-9]+)?m?s` as whole words; a trailing CR and trailing whitespace. Nothing else is
stripped. Over-normalising collapses two different failures into one line, which reads a NEW
failure as INHERITED, and that is the direction this repo's attribution critique ranked as the
blocker (KF14). A varying value the normaliser does not know reads NEW, which is the safe direction.

### The R side

- R is resolved with `git rev-parse --verify <R>^{commit}` and refused, exit 2, when it names no
  commit.
- The worktree is `git worktree add --detach` under the git COMMON dir, whose path is short. The
  scratch pad on this host exceeds MAX_PATH, and a clone under it silently lost files before
  `core.longpaths` was set, so the location is deliberate.
- The suite's argv is resolved from R's own declaration, `selftest-budgets.txt` and
  `gate-legs.json` read at R. The question being asked is "did this suite fail before this build
  touched anything", so R's copy of the suite is the one that runs.
- A trap removes the worktree on every exit path with `git worktree remove --force`, and the run
  prints the worktree path it created so an orphan can be found.

### The cache

- The key is R's full sha, the suite name, and the blob of the suite's first argv file at R.
- The value is S(R), the R exit code and whether a count line was seen.
- It lives at `<git-common-dir>/selftest-baseline/<R>/<key>.fails`, and is written by rename after a
  COMPLETED R run only. A killed run writes nothing, so a partial set can never become the baseline.
- R is immutable, so nothing invalidates an entry. Deleting the directory re-measures, and the help
  text says so.

### Cost

A cache miss runs a suite twice. The budget verdict is the L side's only, because the no-flag mode's
cost rule is a statement about the suite at the tree being graded. The R side prints its own seconds
and carries no verdict. With the cache, each (R, suite) is paid once per build, which is what makes
"each suite once at the unit's end" affordable across the twelve self-test units. Under
`--attribute` the L side's OVER BUDGET exits 1, exactly as it does with no flag.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` ·
`tools/unattended/run-unattended-gates.sh` · `tools/unattended/kit.toml` ·
`memory/backlog/TOOL.md`, for the two dispositions · the two kit version markers · the run-gates
dossier prose · `.githooks/gate-env.sh`, its DoD comment only.

### Alternatives rejected

- Comparing failure COUNTS. A fixed failure plus a new one nets to zero, which is exactly the break
  the red-attribution design lists for its own first criterion.
- Running R in the same worktree through a checkout or a stash. It moves the tree L is graded on, and
  the stash stack is shared across every worktree and session on the node.
- Reading R's failures from `<git-dir>/gate-ledger.tsv` or the per-leg logs. Those exist only when
  someone ran the suite at R, they are per git dir and last-write-wins, and `profile_bar.py` records
  why that ledger is not a measurement.
- Parsing each suite's own PASS format. The suites print heterogeneous PASS lines; the FAIL selector
  already exists and is what the runner shows a reader.

## 5. Production-readiness checklist

- security — the R run executes tracked history of this repository at a sha the caller names, which
  is no new input surface. An unresolvable R refuses rather than running anything.
- perf / scale — a cache miss doubles a suite's wall clock; the cache bounds it to once per
  (R, suite). The help text states it, and the R side carries no cost verdict.
- error / empty / loading states — a DEAD PROBE at L fails, and one at R is reported with every L
  failure read as NEW; an unresolvable R exits 2; a `--kit` filter matching nothing keeps its
  existing refusal; a failed `worktree add` refuses naming the path.
- observability — one block per suite, the R sha, fresh or cached, and the `attributed N of M`
  summary whose shortfall is visible.
- risks — a flaky arm reads as NEW or FIXED noise, and the legend says so. A fresh worktree
  smudges CRLF on unpinned paths, so a suite reading an unpinned file can differ between R and L
  for that reason alone; it reads NEW, the safe direction.
- testing — `tools/run-gates/run-selftests.test.sh` gains a two-commit fixture repo with fixture
  suites, one arm per criterion, each observed RED before it lands. Every criterion that runs a
  runner runs it INSIDE that fixture repository, whose working directory carries no
  `.unattended.conf`: `tools/unattended/gate-guard.js` fails open there by its own header, the run
  grades the fixture's suites and never this repository's tree, and it is the direct check the
  child prompt requires for the flag this unit BUILDS. INSIDE is literal, and it is the whole of
  the route: the hook resolves the repository from the WORKING DIRECTORY OF THE TOOL CALL, which
  `tools/unattended/gate-guard.js:649` reads off the payload, and never from a `cd` written inside
  the command — so each of these criteria is issued as a call whose own working directory IS the
  fixture repository, and a `cd <fixture> && bash …` from this worktree is read against THIS
  worktree's `.unattended.conf` and denied. The VERIFYING run the orchestrator makes after the last
  unit DOES execute `--attribute`, in the attributed suite runs every other unit's final criterion
  defers to, but it runs it over the REAL suites: it cannot stage a failure present at R and absent
  at L, an abort on one side only, or a budget breach, so it observes the runs and never the flag's
  own behaviour. That is why this unit alone keeps its runner runs inside the pass. The arms
  themselves land in `tools/run-gates/run-selftests.test.sh`, whose `run-selftests self-test` leg is
  HELD, so the run that executes them afterwards is that VERIFYING run's
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` and never a plain bar.
- migration — none. The flag is additive and the default mode is byte-identical.
- user docs — both runners' usage text and the run-gates dossier's prose.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-selftests.sh --attribute <R>` runs over a fixture suite
  that fails arm A at R and arms A and B at L, it prints `INHERITED 1` naming A and `NEW 1` naming
  B, and exits 1.
  Red when: the normaliser is dropped, so A's line carries the scratch path at R and the working
  path at L and reads NEW; or sets are replaced by counts.
  permission: the run is confined to the two-commit fixture repository this criterion builds, whose
  working directory carries no `.unattended.conf`, so `tools/unattended/gate-guard.js` fails open by
  its own header; it grades the fixture's suites and never this repository's tree, and it is the
  direct check the child prompt requires for the flag this unit BUILDS rather than an evasion of the
  hook. The call's OWN working directory is that repository, because the hook reads the payload's
  (`tools/unattended/gate-guard.js:649`) and not a `cd` inside the command.
  The same reading covers AC2, AC3, AC4, AC5, AC8, AC9, AC10 and AC12; AC6 states its own.
- **AC2** — When the fixture suite exits non-zero at L before printing any count line or FAIL line,
  its block reads `DEAD PROBE at L`, the summary's N excludes it, and the run exits 1 with the summary
  reading `DEAD L 1` and `verdict red`.
  Red when: the abort is read as an empty FAIL set, so the suite reads clean.
  permission: the fixture-confined run AC1's line states, over this criterion's own fixture suites
  and never this repository's tree.
- **AC3** — When `bash tools/run-gates/run-selftests.sh --attribute <R>` runs over a fixture suite
  that fails arm A at both R and L, it prints `INHERITED 1` and `NEW 0`, the summary reads
  `verdict clean`, and the run exits 0.
  Red when: the exit derives from S(L) being non-empty, as the no-flag loop's `st=1` does, so every
  inherited failure fails the unit that inherited it.
  permission: the fixture-confined run AC1's line states, over this criterion's own fixture suites
  and never this repository's tree.
- **AC4** — When a fixture's R run is killed by a short bound and `--attribute <R>` is then run
  again, the second run reads `fresh` on the R side; a third run after a completed R run reads
  `cached` and `git worktree list` gains no entry during it.
  Red when: the cache is written before the R run completes, so the killed run's partial set is
  served as the baseline from then on.
  permission: the fixture-confined run AC1's line states, over this criterion's own fixture suites
  and never this repository's tree.
- **AC5** — When a FAIL present at R is absent at L, `--attribute` prints it under FIXED and the exit
  status is unaffected by it.
  Red when: FIXED is folded into NEW through a symmetric difference.
  permission: the fixture-confined run AC1's line states, over this criterion's own fixture suites
  and never this repository's tree.
- **AC6** — When `bash tools/unattended/run-unattended-gates.sh --attribute <R>` runs, attribution
  blocks appear for the self-test half and one line states that the checks half is not attributed.
  Red when: the flag is accepted and not forwarded, so the half runs unattributed and says nothing.
  permission: the fixture-confined run AC1's line states, over this criterion's own fixture suites
  and never this repository's tree. The head word here is `run-unattended-gates.sh`, gate-guard row
  D3 rather than D2, and the fail-open reading is the same one.
- **AC7** — When `git grep -n -e 'GREEN verdict' -e 'prints GREEN' -- tools .githooks` runs, it prints
  nothing; at BASE it prints four lines. `git grep -c 'verdict clean'` over
  `tools/unattended/kit.toml`, `tools/run-gates/run-selftests.sh`,
  `tools/unattended/run-unattended-gates.sh` and `.githooks/gate-env.sh` counts at least one line in
  each. Each of those four names `--attribute`, `DEAD PROBE` and `OVER BUDGET` beside the criterion.
  Red when: one of the four keeps the GREEN wording, which leaves two answers to one question; or
  the wording names NEW alone, so a consumer reading it passes a suite that aborted or broke its
  budget.
- **AC8** — When `bash tools/run-gates/run-selftests.sh --kit <dir>` runs without `--attribute` over
  the fixture population, its stdout and exit status equal the BASE runner's.
  Red when: any attribution code path executes in the default mode.
  permission: the fixture-confined run AC1's line states, over this criterion's own fixture suites
  and never this repository's tree.
- **AC9** — When a fixture suite prints its count line, prints no line the FAIL selector matches,
  and exits non-zero at L, its block reads `DEAD PROBE at L` and the run exits 1.
  Red when: the rule also requires the count line to be absent, so a suite that prints its count and
  then dies reads as an empty set, which is green by absence.
  permission: the fixture-confined run AC1's line states, over this criterion's own fixture suites
  and never this repository's tree.
- **AC10** — When a fixture suite whose budget row is below its runtime runs under `--attribute`,
  its L block reads `OVER BUDGET`, NEW reads 0, and the run exits 1 with `verdict red`.
  Red when: attribute mode drops the budget verdict, so "a runner REDS on breach" stops holding in
  the mode this build's self-test units verify with.
  permission: the fixture-confined run AC1's line states, over this criterion's own fixture suites
  and never this repository's tree.
- **AC11** — When `tools/run-gates/run-gates.sh` is read with `git show` at `fb07ca25`, at the tip of
  `origin/main` after a `git fetch` at this unit's pass, and at this unit's build commit,
  `KIT_RUN_GATES_VERSION` at the build commit is strictly greater than each of the other two,
  compared as a dotted version one integer component at a time, so `1.10` follows `1.9`. The same
  holds for `KIT_UNATTENDED_VERSION` in `tools/unattended/unattended.sh`, and
  `bash tools/check-kit-versions.sh` exits 0 at the build commit.
  Red when: the move is skipped and each marker still agrees with its constant at BASE's values, so
  `kit version markers` stays green over shipped bytes that changed in both kits; or the move clears
  BASE's value while `origin/main` already carries the number it lands on, so adopters receive two
  byte sets under one version; or the values are compared as decimals, which reads a `1.9` to `1.10`
  move as a decrease.
  permission: the two `git show` reads are the pass's own; `bash tools/check-kit-versions.sh` is
  the `kit version markers` leg over the real tree, so that half is observed at the build's one
  post-build bar.
- **AC12** — Three fixture suites run under `--attribute <R>`.
  1. A suite that exits non-zero with no FAIL line at R and passes clean at L: its block reads
     `DEAD PROBE at R`, the summary reads `DEAD R 1` and `verdict clean`, and the run exits 0.
  2. The same suite failing arm A at L: A reads NEW, never INHERITED, and the run exits 1.
  3. A suite aborting with no FAIL line on both sides: its block reads `DEAD PROBE at L`, and the run
     exits 1 with `verdict red`.

  Red when: a DEAD PROBE at R exits 1, so the unit that fixes an abort present at BASE can never
  verify its own fix; or an L failure over a dead R reads INHERITED, which is KF14's blocker; or a
  suite dead on both sides exits 0, so a consumer passes with its own arms never run.
  permission: the fixture-confined run AC1's line states, over this criterion's own fixture suites
  and never this repository's tree.

## 7. Gates

`run-selftests self-test` · `testsuite counts (every bar self-test prints one)` · `every held leg is budgeted, every budget row resolves` · `install-prefix (shipped surface)` · `kit version markers` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: `tools/run-gates/run-selftests.test.sh` · a two-commit fixture repo whose suite fails one arm at R and two at L, plus a suite that aborts before any arm · none

## 8. Open questions

- **F1 — FACT-QUESTION · does the R side need a cache at all?** Probe: the declared budgets of the
  unattended suites in `tools/run-gates/selftest-budgets.txt`, against the twelve units allowed to
  run them. Observation: the unattended gate and driver suites alone are declared at thousands of
  seconds each, so an uncached R side re-pays that per unit. Liveness: a population whose summed R
  cost fit inside one unit's budget would decide against the cache.
  RESOLVED (agent, 2026-09-14, delegated): cache, keyed on R, suite and suite blob, written only
  after a completed run.
- **F2 — does `run-unattended-gates.sh --attribute` also attribute its checks half?** Options:
  attribute all four repository checks here, or forward to the self-test half only. The checks are
  bar legs, and bar-leg attribution needs the per-leg signature rules this unit does not build.
  RESOLVED (agent, 2026-09-14, delegated): self-test half only, with an announcing line.
- **F3 — is the R-side run budget-graded?** Options: grade it like L, or print its seconds with no
  verdict. Grading it would red a suite for the cost of evidence nobody asked it to be fast at.
  RESOLVED (agent, 2026-09-14, delegated): no verdict on the R side.
- **F4 — does an L-side budget breach fail under `--attribute`?** Options: (a) yes, reported apart
  from NEW; (b) no, reported only. (b) suspends charter §7's rule that a runner reds on breach.
  RESOLVED (agent, 2026-09-14, delegated): (a).
- **F5 — does a DEAD PROBE at R fail the run?** Options:
  - (a) any DEAD PROBE exits 1;
  - (b) only a DEAD PROBE at L exits 1, and a dead R gives S(R) no members, so every L failure reads
    NEW;
  - (c) additionally, a suite dead on both sides exits 0 as an inherited abort.

  (c) fails AC2 and design U16's acceptance 2, and KF14 reads an empty set on both sides as a DEAD
  PROBE: a consumer would pass with its own arms never executed. (a) leaves the unit that fixes an
  abort present at BASE unable ever to verify its fix. RESOLVED (agent, 2026-09-16, delegated): (b).
  A suite dead at BASE and still dead at L fails every consumer until the abort is fixed, which is
  correct, because none of their arms ran.
- **F6 — what do consumers read, and how is "every INHERITED FAIL filed" observed?** Options:
  - (a) the runner's exit status, with the filing term dropped;
  - (b) a `verdict clean|red` token on the summary line, plus a suite-grain filing check a reader can
    run;
  - (c) the summary fields, with a line-grain filing check.

  (a) conflates the unattributed `--checks` half's exit and drops design U16's filing term. (c) needs
  backlog rows that quote normalised FAIL lines, which no unit builds. RESOLVED (agent, 2026-09-16,
  delegated): (b), stated once as S10. The token rides every hands-off bullet, so unit 37's token
  join reds a consumer that does not spell it.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds three edges the brief's table does not list, all inside
  this spec's own group: hands-off to units 3, 4 and 5, which verify with this unit's criterion
  exactly as unit 2 does.
- rev-2 · 2026-09-14 · §2 S3 S5 S7 S9 · §3 · §4 · §6 AC3 AC9 AC10 · §8 F4 · §10 · round-1 spec-audit
  fold (G1 H5, M11, M12, M17, M18, M19, L5; G3 H9; G4 L1; G5 L1). S7's `$1` fix is withdrawn,
  because commit 8b29f0b9, an ancestor of BASE, already carries it; S7 now disposes its two backlog
  rows. The rev-1 AC3 goes with it, M19 is moot, and AC3 is now the inherited-only exit criterion.
  S3's DEAD PROBE takes KF14's definition, with or without a count line (AC9). An L-side OVER BUDGET
  exits 1 under `--attribute` (F4, AC10). S9 is the build's one run-gates and unattended version
  move. Edges beyond the brief's table, which lists only units 2 and 23: hands-off to units 3, 4 and
  5 (rev-1), to unit 30 (rev-1, previously unlisted), and to units 22, 24, 27 and 28 (added here).
  G3 H9 adds hands-off to units 16, 17 and 18, which read `--attribute <BASE>`. G5 L1 adds a
  hands-off to unit 32, which corrects both runner headers S8 leaves and rides S9's version moves.
- rev-3 · 2026-09-16 · spec-audit round 2 fold.
  - G1 H1 (2, 24): the handed-off criterion is stated once as S10, `verdict clean` with every
    inherited suite filed. S5 exits 1 on a DEAD PROBE at L whatever R shows, and never on one at R
    alone, whose S(L) then reads NEW (F5, AC12). The summary gains `DEAD L`, `DEAD R` and the verdict
    token (F6). §1, S3, §4 output block and §5 follow. AC2, AC3 and AC10 read the token. Every
    criterion-carrying hands-off bullet names `verdict clean`.
  - G1 M11 (3): AC11 observes S9's version move against `abac6d59`, comparing the markers as dotted
    versions, component by component (fold verification: BASE's unattended marker is `1.19`, which
    a decimal comparison would read as greater than `1.20`).
  - G1 L8 (47): S8 and AC7 cover the fourth copy in `.githooks/gate-env.sh`, which Files touched
    now lists, and AC7 greps the whole `tools` and `.githooks` population.
- rev-4 · 2026-09-16 · regrounded on fb07ca25 (origin/main). The two runners, their suite and
  `.githooks/gate-env.sh` are byte-identical there, and AC7's grep still prints four lines. The kit
  markers moved on main: run-gates from 1.6 to 1.7 at the aRatifiedRulings merge, and unattended
  from 1.19 to 1.24 across the aRatifiedRulings, dPolishedVitrine, aDeferredBar and aProbedUnit
  merges. So S9 and AC11 read the move as strictly greater than both BASE's value and the tip of
  `origin/main` at the pass, on every carrier `tools/check-kit-versions.sh` names, by the
  orchestrator's build-wide kit version decision. S9 also carries the courtesy marker in
  aDeferredBar's `gate-guard.js`. S7's line citation moves from 4107 to 4123. S10 names `<BASE>` as
  the consuming spec's header base, not the run-state file's pinned `abac6d59`. §10 records what
  moved and the gate-guard refusal reported to the orchestrator.
  Extended 2026-09-20, regrounding consolidation, folding the conservative reading of the parked
  suite-permission ruling and not deciding it: the §3 hands-off bullets no longer say a consumer
  runs the unattended suites at its own end, because BUILD-METHOD M6 moves that verdict to the one
  post-build run, and §10 names the hook rows as `gate-guard.js` spells them at fb07ca25. This
  unit's own runner criteria are UNCHANGED: they run the runner over fixture suites and observe
  the flag this unit builds, which no post-build bar run would observe. The orchestrator settled
  it on 2026-09-20: every runner criterion runs inside this unit's own fixture repository, whose
  working directory carries no `.unattended.conf`, where rows D2 and D3 fail open by the hook's
  own header, and §5 plus a `permission:` line on AC1 to AC6 and AC8 to AC10 and AC12 now say so.
  The closing verifier added the mechanism that makes INSIDE binding: the hook reads the TOOL
  CALL's working directory and not a `cd` inside the command, so a `cd <fixture> && …` issued from
  this worktree is denied and the route needs the call itself made in the fixture repository.
  AC11 also keeps a
  `permission:` line, because its `bash tools/check-kit-versions.sh` half is a gate leg over the
  real tree and not a fixture run. The `New arm:` line keeps `none`:
  `tools/run-gates/run-selftests.test.sh` pins no executed-assertion floor at fb07ca25. AC7's grep
  was re-run at fb07ca25 and still prints four lines, so it is not a could-not-fail phrase.
  Extended again on 2026-09-20, closing pass. §5 no longer says that no post-build run executes
  `--attribute`: the VERIFYING run's attributed suite runs do, over the REAL suites, and what they
  cannot produce is this unit's fixture conditions, which is the reason the runner criteria stay in
  the pass. §5 also names, in the orchestrator's own terms, the run that executes the new arms once
  they are written: `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, because
  `run-selftests self-test` is a HELD leg and a plain bar does not reach it.

## 10. Reuse audit

- The seam is `tools/run-gates/run-selftests.sh`, TOOL-aQuenchedHarness-4's one on-demand runner,
  which already resolves the declared population, runs each suite and greps its FAIL tail;
  `tools/unattended/run-unattended-gates.sh` delegates its self-test half to it. The probe
  `reuse_lookup.py "held self-test suite failure set baseline attribution inherited new fixed"`
  returned no seam, and its own coverage line explains why: `unscanned layers: .sh`, and both
  runners are shell. Its candidates were name-stem matches in codebase-map, lexicon and
  process-monitor with no failure-set semantics. A grep for `--attribute`, `GATE_ATTRIBUTE` and
  `INHERITED` over `tools/` found nothing but an unrelated word in `profile_bar.py`. Recall surfaced
  the rows this answers: TOOL-aBoundedCeiling-10, TOOL-aHoistedPass-36, TOOL-aTracedSpawn-1 and
  TOOL-aQuenchedHarness-9. Where the design record and the source disagree: nowhere found at BASE
  for the compensating-check block or the runners; commit 8b29f0b9 (2026-09-08), an ancestor of
  BASE, already replaced the bare `$1` in the case pattern now at
  `tools/unattended/unattended.test.sh:4123` with a path-agnostic match, and its message records
  that the arm still fails at check 49. The rev-1 S7 re-specified that fix and is withdrawn.
- BASE is `fb07ca25`, the origin/main tip this branch merged; the spec was written at `abac6d59`.
  Between the two, `run-selftests.sh`, its suite, `run-unattended-gates.sh` and
  `.githooks/gate-env.sh` did not change, and nothing on main builds `--attribute`, a baseline cache
  or an INHERITED set. What moved: `tools/run-gates/selftest-budgets.txt` gained the
  `unattended gate-guard selftest` row, so the unattended population the self-test half resolves has
  one more suite; the kit version markers (S9); and the suite line S7 cites. aDeferredBar landed a
  rule and a hook this spec's consumers meet. `memory/guides/BUILD-METHOD.md` M6 says a pass runs no
  self-test suite and returns the need to the main loop, and `tools/unattended/gate-guard.js` denies
  a command-position `run-selftests.sh` (row D2), `run-unattended-gates.sh` (D3) or `.test.sh` /
  `selftest.py` (D4) word while the branch's run record is before `VERIFYING`, unless the same
  command carries one of its read-only verbs (`--list`, `--check`, `--rank`, `--help`, `--render`);
  `--attribute` is not one of them. That reached this unit's own fixture runs of the runner and
  every consumer's run "once at the unit's end", which owner rulings D12-h and D12-i8 permit. The
  2026-09-20 consolidation moved every consumer's attributed run to the build's one post-build bar;
  this unit's own fixture runs stay, because no post-build run observes `--attribute`. That residue
  is reported to the orchestrator and not decided here.
- M12 was not reached, because an existing seam fits and the design names the mechanism.
- Recall terms used: `held-suite self-tests inherited-red baseline FAIL-set attribution
  run-selftests run-unattended-gates compensating-check kit-DoD GATE_SELFTESTS dead-probe`
