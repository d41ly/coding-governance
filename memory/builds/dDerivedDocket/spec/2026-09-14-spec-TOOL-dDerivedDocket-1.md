# TOOL-dDerivedDocket-1 — held-suite failure baseline

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md) | spec-audit | TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |

<!-- /gen:spec-records -->

## 1. Goal

The kit self-test suites are held off the merge bar, and several are red at BASE for reasons this
build did not cause (TOOL-aHoistedPass-36, TOOL-aHoistedPass-38, TOOL-aQuenchedHarness-9). A unit
that is allowed to run them (D12-h, D12-i8) therefore cannot reach GREEN, and a red run tells it
nothing about its own change. Give the on-demand self-test runners a baseline mode that runs each
selected suite at a named base R as well as at the working tree L, and reports NEW, INHERITED and
FIXED failure sets. "No NEW FAIL" then becomes the verification criterion every later self-test
unit in this build uses. Built first, by owner ruling D12-i11.

## 2. Scope (IN)

- **S1** `tools/run-gates/run-selftests.sh` gains `--attribute <R>`, composable with `--kit <dir>`.
  For every selected suite it runs the suite at L exactly as the no-flag mode does, runs R's copy of
  the same suite in a detached scratch worktree at R, and prints the three sets per suite plus one
  summary line `attributed N of M suite(s) against <R8>`. Observed by AC1 and AC5.
- **S2** One normaliser, applied identically to both sides, reduces each FAIL line to what does not
  vary between two runs of an unchanged suite. Observed by AC1.
- **S3** A suite that exits non-zero on a side without printing its count line or any FAIL line is a
  DEAD PROBE on that side, never an empty set. `N` counts only suites with a verdict on both sides.
  Observed by AC2.
- **S4** The R-side set is cached per (R, suite, suite-file blob at R), written only after an R run
  that completed. Observed by AC4.
- **S5** Exit status under `--attribute`: 1 when any NEW FAIL or DEAD PROBE exists, else 0, with
  INHERITED and FIXED reported and not failing. The no-flag mode's output and exit are unchanged.
  Observed by AC1, AC2 and AC8.
- **S6** `tools/unattended/run-unattended-gates.sh --attribute <R>` forwards the flag to its
  delegated self-test half and prints one line saying its `--checks` half is not attributed.
  Observed by AC6.
- **S7** The one-character `$1` fix in `tools/unattended/unattended.test.sh` that
  TOOL-aHoistedPass-36 cause 1 and TOOL-aTracedSpawn-1 record, so the unsharded suite reaches its
  count line. Observed by AC3.
- **S8** The compensating-check wording moves from "a GREEN verdict" to "no NEW FAIL against the
  build's BASE, and every INHERITED FAIL named by a filed backlog row", in the three places that
  state it: the `tools/unattended/kit.toml` self-test block and both runner headers. Observed by
  AC7.
- **S9** The run-gates and unattended kit version markers move, because shipped bytes change in
  both kits. NOT OBSERVED by a criterion here: the `kit version markers` leg grades it.

## 3. Non-goals (OUT)

- Attributing MERGE-BAR legs. Re-running a red bar leg at R, per-leg signatures and the KF14
  classification belong to the red-attribution unit; this unit handles self-test suites only.
- Fixing any inherited failure. TOOL-aHoistedPass-38's open causes and the suites
  TOOL-aQuenchedHarness-9 measured red stay filed; this unit makes them attributable, not green.
  Whatever the roughly thirty arms S7 makes reachable say is data, as TOOL-aHoistedPass-36 states.
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
- **hands-off** `TOOL-dDerivedDocket-2` — the "no NEW FAIL" criterion over the held push-main
  self-test suite, read through `--attribute` against this build's BASE.
- **hands-off** `TOOL-dDerivedDocket-3` — the same criterion over the unattended suites that unit
  is allowed to run once at its end.
- **hands-off** `TOOL-dDerivedDocket-4` — the same criterion over the unattended suites.
- **hands-off** `TOOL-dDerivedDocket-5` — the same criterion over the unattended suites.
- **hands-off** `TOOL-dDerivedDocket-23` — the FAIL-line normaliser and the detached scratch
  worktree runner at R, which that unit reuses to re-run a red bar leg at R.
- **hands-off** `TOOL-dDerivedDocket-30` — `--attribute`, under which that unit runs the unattended
  suites once, since they are red at BASE and "no NEW failure" is the only criterion they can meet.

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
attr  <suite name>  DEAD PROBE at L|R — exit <rc>, no count line and no FAIL line
attributed N of M suite(s) against <sha8> · NEW <n> · INHERITED <n> · FIXED <n> · DEAD <n>
```

`absent` means the suite does not exist at R, so all of S(L) is NEW, and the line says so.

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
"each suite once at the unit's end" affordable across the twelve self-test units.

### The `$1` fix

The arm is located by reproduction, not by line: the builder runs the suite unsharded at BASE, sees
`$1: unbound variable`, and escapes that character. The line was NOT re-located at BASE while
writing this spec (UNVERIFIED): a grep for `$1` in a case-pattern position found no candidate.
TOOL-aTracedSpawn-1 records the same stop from the runner's side, so both rows answer to this fix.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` ·
`tools/unattended/run-unattended-gates.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/kit.toml` · the two kit version markers · the run-gates dossier prose.

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
- error / empty / loading states — DEAD PROBE on either side; an unresolvable R exits 2; a `--kit`
  filter matching nothing keeps its existing refusal; a failed `worktree add` refuses naming the
  path.
- observability — one block per suite, the R sha, fresh or cached, and the `attributed N of M`
  summary whose shortfall is visible.
- risks — a flaky arm reads as NEW or FIXED noise, and the legend says so. A fresh worktree
  smudges CRLF on unpinned paths, so a suite reading an unpinned file can differ between R and L
  for that reason alone; it reads NEW, the safe direction.
- testing — `tools/run-gates/run-selftests.test.sh` gains a two-commit fixture repo with fixture
  suites, one arm per criterion, each observed RED before it lands.
- migration — none. The flag is additive and the default mode is byte-identical.
- user docs — both runners' usage text and the run-gates dossier's prose.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-selftests.sh --attribute <R>` runs over a fixture suite
  that fails arm A at R and arms A and B at L, it prints `INHERITED 1` naming A and `NEW 1` naming
  B, and exits 1.
  Red when: the normaliser is dropped, so A's line carries the scratch path at R and the working
  path at L and reads NEW; or sets are replaced by counts.
- **AC2** — When the fixture suite exits non-zero at L before printing any count line or FAIL line,
  its block reads `DEAD PROBE at L`, the summary's N excludes it, and the run exits 1.
  Red when: the abort is read as an empty FAIL set, so the suite reads clean.
- **AC3** — When `bash tools/unattended/unattended.test.sh` runs with no arguments at the unit's end,
  it reaches its count line instead of dying on an unbound positional parameter.
  Red when: the fix is reverted, the run ends `$1: unbound variable`, and S3 reads it DEAD PROBE.
  cost: the suite's declared budget row, run once.
  permission: D12-i8 lifts the standing do-not-run instruction for this unit only.
- **AC4** — When a fixture's R run is killed by a short bound and `--attribute <R>` is then run
  again, the second run reads `fresh` on the R side; a third run after a completed R run reads
  `cached` and `git worktree list` gains no entry during it.
  Red when: the cache is written before the R run completes, so the killed run's partial set is
  served as the baseline from then on.
- **AC5** — When a FAIL present at R is absent at L, `--attribute` prints it under FIXED and the exit
  status is unaffected by it.
  Red when: FIXED is folded into NEW through a symmetric difference.
- **AC6** — When `bash tools/unattended/run-unattended-gates.sh --attribute <R>` runs, attribution
  blocks appear for the self-test half and one line states that the checks half is not attributed.
  Red when: the flag is accepted and not forwarded, so the half runs unattributed and says nothing.
- **AC7** — When `tools/unattended/kit.toml` and the headers of both runners are read, each names
  `--attribute` and the "no NEW FAIL" criterion, and none states a GREEN verdict as the DoD.
  Red when: one of the three keeps the GREEN wording, which leaves two answers to one question.
- **AC8** — When `bash tools/run-gates/run-selftests.sh --kit <dir>` runs without `--attribute` over
  the fixture population, its stdout and exit status equal the BASE runner's.
  Red when: any attribution code path executes in the default mode.

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

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds three edges the brief's table does not list, all inside
  this spec's own group: hands-off to units 3, 4 and 5, which verify with this unit's criterion
  exactly as unit 2 does.

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
  for the compensating-check block or the runners; the `$1` arm's line was not re-located.
- M12 was not reached, because an existing seam fits and the design names the mechanism.
- Recall terms used: `held-suite self-tests inherited-red baseline FAIL-set attribution
  run-selftests run-unattended-gates compensating-check kit-DoD GATE_SELFTESTS dead-probe`
