# Acceptance ledger — TOOL-aPooledSweep-1, -2 and -3, and the measured A/B

**Serves:** journal TOOL-aPooledSweep-1 TOOL-aPooledSweep-2 TOOL-aPooledSweep-3

**Evidences:** TOOL-aPooledSweep-1 TOOL-aPooledSweep-2 TOOL-aPooledSweep-3

Tier-2 · node a · 2026-09-07. One line per numbered criterion, each naming the observation that
answered it. Every arm named below lives in `tools/run-gates/run-selftests.test.sh`, was staged RED
and watched to fail before it was trusted, and the suite is green at 37 arms against a floor of 37.

## The measurement the build turns on

Two A/B runs, same tree, same populations, serial arm then pooled arm, each asserting a positive
artifact — the count of suite verdict lines — before the times are compared. An arm that graded
fewer suites is not a faster arm, and the script refuses the comparison when the two counts differ.

**Nine real suites, `--kit tools/memory-tree`, node `a`, 2026-09-07:**

| | serial | pooled |
|---|---|---|
| wall | **1692 s** | **981 s** |
| sum of the per-suite readings | 1689 s | 1629 s |
| longest single suite | 1126 s | 972 s |
| suites graded | 9 | 9 |
| per-suite verdicts | identical to the pooled arm | identical to the serial arm |

**1.72x, and the shape matters more than the factor.** The pooled wall is 981 s against a longest
member of 972 s — nine seconds of overhead for the other eight suites. The pool reaches its
structural optimum, which is `wall = longest member`; the factor is only 1.72 because THIS
population is dominated by one suite holding two thirds of its serial time.

**What that projects to, stated as a projection and not as a measurement.** Over the whole declared
population the same structure gives `wall = longest member` = 9067 s against a 36146 s serial sum, a
ceiling of 4.0x — roughly ten hours to two and a half. Nobody has run that, and this record does not
claim otherwise. What IS measured is that the pool hits `wall = longest` on a real nine-suite
population, which is the property the projection rests on.

**Three suites, `--kit tools/workflows`: serial 56 s, pooled 62 s — a 10% LOSS**, and it is recorded
rather than dropped. That population is three suites of which one holds 33 s of 54 s, so the best
available factor was 1.4x before any overhead. Both long suites also ran SLOWER under the pool —
33 s to 57 s and 21 s to 36 s — on a sixteen-core box with three processes, which is a shared
serialising resource rather than CPU saturation. `TOOL-aGradedDoorway-8` names the likely one: an
on-access scanner in front of every `exec`, measured here at ~190 ms a spawn.

**The rule that falls out, and it belongs in the runner's guidance rather than only here: a sweep
pays off in proportion to how UNDOMINATED the population is.** Below roughly four suites, or where
one suite holds most of the time, the serial mode is as good or better and it grades budgets too.

## A pre-existing red, surfaced

`memory-hygiene self-test` is RED at HEAD, identically in both arms — the parity check confirms the
two modes returned the same verdict for every one of the nine suites. Its first line is
`FAIL project keys: the fixture is not clean unset (rc=1) — every arm below is meaningless`, and
this repo declares `PROJECT_REGISTRY_EXTRA='pass-order-waiver.txt'` where that fixture expects the
key unset. Nothing in this build touches `tools/memory-tree/`. It is the `TOOL-aQuenchedHarness-9`
class — a held suite red for an unknown length of time — and it gets a backlog row rather than a
fix here.

`codebase-map adopter e2e` and `codebase-map kit selftest` are red too, in the SERIAL mode, at HEAD.
Same class, same disposition. Between them and `memory-hygiene self-test` that is three of the
eleven suites this build ran end to end, which is itself the argument for a sweep somebody can
afford to run.

## TOOL-aPooledSweep-1

- AC1 — MET, OBSERVED — armed as `--sweep reds on a failing suite and prints that suite's OWN output beneath its row`, green; staged red by rendering only the exit code.
- AC2 — MET, OBSERVED — armed as `--sweep prints the width pair it chose BEFORE the first verdict`; the order-stability half is observed by the A/B above, whose pooled and serial verdict lists sort identically across nine suites at two different widths.
- AC3 — MET, OBSERVED — the same arm reads the printed pair; the clamp is exercised by the smoke fixture, where `SELFTEST_OUTER_WIDTH=4` against a resolved width of 2 reports `outer 2`.
- AC4 — MET, OBSERVED — armed as `a --sweep filter matching nothing REFUSES, exactly as the serial mode's does`, exit 2, green.
- AC5 — MET, OBSERVED — the serial mode's sixteen pre-existing arms are unchanged and green, and the A/B's serial arm produces the same line shape it did before this build.
- AC6 — MET, OBSERVED — the pooled arm of the nine-suite A/B ran nine suites in 981 s whose readings sum to 1629 s, so at least two intervals overlapped by 648 s. A collapse to a barrier per suite cannot produce that.
- AC7 — MET, OBSERVED — armed as `--sweep over a green population exits 0`, green; staged red by forcing the exit expression.
- AC8 — MET, OBSERVED — armed as `a suite past its derived bound is TIMEOUT, distinguishable from both ok and FAIL`, green; staged red by rendering it as an ordinary FAIL.
- AC9 — MET, OBSERVED — armed as `a run wall BELOW the largest per-suite bound REFUSES`, exit 2, green. The arithmetic half: over the real population the largest budget is 13600 s and the derived wall is 27200 s, so the wall is above the largest per-suite bound by construction.
- AC10 — MET, OBSERVED, and it took a change to become observable at all. As first built the criterion could not be answered: it asks for PEAK overlap counted from the verdict files, and those files are removed by the run's own `EXIT` trap before an arm could read them. The sweep now COMPUTES the peak from its own stamps before removing them, prints `peak concurrency <n> of outer <m>`, and REDS when the peak exceeds the outer width — a guard rather than a statistic, because the printed pair is what the pool was asked for and cannot notice a pool that ran wider. Armed as `peak concurrency is REPORTED and never exceeds the outer width the run printed`, green, staged red by inverting the comparison. Observed reporting `peak concurrency 2 of outer 8` over a two-suite population.
- AC11 — MET, OBSERVED — armed as `--sweep REFUSES when no timeout binary resolves`, exit 2, green; staged red by defaulting the binary.

## TOOL-aPooledSweep-2

- AC1 — MET, OBSERVED — armed as `every pooled row carries its cost verdict, and that verdict is 'withheld'`, green; and the nine-suite A/B shows `cost withheld` on all nine rows against nine budget verdicts in the serial arm.
- AC2 — MET, OBSERVED — armed as `the sweep STATES how many cost verdicts it withheld`; the A/B's pooled arm reports `9 cost verdict(s) WITHHELD under pooled@8x1` against nine rows.
- AC3 — MET, OBSERVED — `git status --porcelain` over `tools/run-gates/selftest-budgets.txt` is empty after both pooled runs; the sweep writes no reading anywhere.
- AC4 — MET, OBSERVED — `--help` states that `--sweep` issues no cost verdict at all and names the serial mode for one.
- AC5 — MET, OBSERVED — armed as `--rank REFUSES a pooled reading by name`, exit 1, green, and paired with `the same file WITHOUT the pooled row still ranks` so the refusal is a predicate rather than a blanket. Both staged red.
- AC6 — MET, OBSERVED — armed as `the tag --sweep EMITS is the tag --rank refuses, captured rather than hand-typed`. Building it found a real defect the other arms could not see: the wall watchdog inherited the caller's stdout, so a command substitution around `--sweep` blocked for the whole wall.

## TOOL-aPooledSweep-3

- AC1 — MET, OBSERVED — armed as `each pooled suite gets its own TMPDIR`; the fixture suite asserts its own `mktemp -d` lands under `$TMPDIR`, and the arm was staged red by removing the redirection.
- AC2 — MET, OBSERVED — armed as `a suite that writes into a TRACKED file reds the sweep as UNSOUND after the pool drains`, green; staged red by making the comparison inert.
- AC3 — MET, OBSERVED — armed as `a fingerprint that cannot be TAKEN refuses before running anything`, exit 2, green, through a `git` shim that answers every subcommand the runner needs and refuses `status`.
- AC4 — MET, OBSERVED — armed as `a clean sweep STATES that the fingerprint matched`, and both A/B pooled runs print `tree fingerprint MATCHED before and after`.
- AC5 — MET, OBSERVED — armed as `a suite writing into the GIT COMMON DIR does not red the sweep`, green. This is the negative edge, and it is why the second fingerprint arm was deleted rather than narrowed.
- AC6 — MET, OBSERVED — the nine-suite A/B's pooled arm went red and printed `a pooled RED cannot tell a broken mechanism from a busy box. Confirm it with the serial re-run`.
- AC7 — MET, OBSERVED — the baseline is taken before the pool starts, and AC2's arm is what proves it: a suite that dirties a tracked file DURING the sweep is still reported, which is only possible if the reading predates it.

## What the closing diff review moved

Round 1 confirmed eleven findings resolving to six defects, precision 0.92, and all six were folded.
Four were mechanisms that had never been SEEN working, which is the shape §7 names outright.

- **D1 — the wall watchdog killed the runner, not the workers.** `echo $$` inside a backgrounded
  subshell writes the PARENT's pid, because a subshell inherits `$$`. Every pid file held
  `run-selftests.sh`'s own pid, so the watchdog SIGTERMed the runner — exit 143, no verdicts, the
  suites orphaned and the scratch root deleted under them. The worker now records the `timeout`
  child's pid and the kill reaches the work. Observed firing: a 12 s wall over an 18 s run killed
  the third suite and the runner rendered all three rows.
- **D1b, found by that same run.** A TERMed worker still writes its verdict file, so the `WALL`
  branch — which only fired on a MISSING verdict — was unreachable even after D1 was fixed. A
  wall-killed suite renders `WALL` now, distinguished from `TIMEOUT` by exit 143 against 124.
- **D2 — the peak counted closed intervals on whole-second stamps**, so every pool handoff
  double-counted. A strictly serial fixture reported peak 2, and the real 59-row population at outer
  8 makes about fifty handoffs, so the guard would have redded every green sweep. Half-open now, and
  the stamps are MILLISECONDS: at second granularity a handoff and an overlap are the same two
  numbers, and a suite finishing inside one second has an empty interval that counts as nobody.
- **D3 — the diff added root-install kit-path literals** without moving a shrink-only BAN, so
  `tools/check-install-prefix.sh` exited 1 on this worktree with two ROSE rows. The runner's
  self-reference is DERIVED from `$0` now, the fixture's manifest path is one variable rather than
  three spellings, and the prose names kits without spelling their paths. The gate exits 0.
- **D4 — the run wall covered one suite, not the run.** It derived from the largest per-suite bound
  alone, so `SELFTEST_OUTER_WIDTH=1` — a documented setting — killed a perfectly clean run. It is
  `largest bound x waves` now, waves derived from the population and the width.
- **D5 — both knobs discarded a non-numeric value silently**, leaving the operator believing a bound
  they never set. Both REFUSE by name.
- **D6 — the after-fingerprint had no liveness assertion** where the before-reading did, so a `git
  status` that failed at the end reported a clean tree or an unsound sweep depending only on whether
  the tree was already dirty. It now reports UNGRADED, which is neither.

Four arms added, floor 37 → 41, and the suite was run three times consecutively after the fold
because the first version of the wall arm was a coin flip: the wall and the per-suite bound expired
within a second of each other, so whichever won decided whether the row read `WALL` or `TIMEOUT`.
The fixture now puts five seconds between them.

**One announced gap.** The peak arm asserts that a strictly serial pool reports 1, which is the
property that matters, but it no longer discriminates the half-open comparison specifically: with
millisecond stamps a closed-interval bug needs a handoff to land on the same millisecond, so the
staged break for D2 does not reliably red at two suites. Pinning that line on its own means testing
the embedded awk in isolation, which this build does not do. Said here rather than left as a green
row that looks like coverage.

## Round 2 of the closing review, and where the loop ended

Round 2 confirmed fifteen findings resolving to EIGHT distinct defects against round 1's six —
precision 0.94. Eight is not strictly smaller than six, so the loop is NON-CONVERGENT and the
build method's exit applies: every finding still standing is DISPOSED, and all eight are defects in
documents the review read, so all eight were FOLDED. Not promoted, not parked, not waived. The
disposition is recorded on the round.

- **BLOCKER — the wall stopped stopping the run.** Round 1's pid fix pointed the watchdog's kill at
  the workers instead of the runner, which was correct and which removed the only thing that ended
  the run: the dispatch loop never read the breach file, so the pool kept launching the rest of the
  population after the wall had fired. Reproduced three times at 16 s, 17 s and 23 s against a 10 s
  wall. `run-gates.sh` carries the identical one-line guard at the top of its own walk and this is
  that line, not a second invention. Observed after the fix: a 10 s wall over a ~95 s serial
  population returned in 13 s.
- **HIGH — `date +%N` is a GNU extension.** On BSD it prints a literal `N`, so
  `$(( $(date +%s%N) / 1000000 ))` is an arithmetic syntax error that aborts EVERY worker before it
  runs its suite — a total false RED blaming each suite for the runner's own arithmetic. Probed once
  now, with a whole-second fallback whose lost resolution is ANNOUNCED rather than silently taken.
- **MEDIUM — the derived wall could never fire.** `largest bound x waves` assumes every wave is as
  slow as the slowest suite, which over this population is 2x to 15x the real ceiling. It is the
  bounded work over the pool now, floored at the longest single suite.
- **MEDIUM — no arm asserted either the derivation or a post-breach launch**, which is the gap that
  let the blocker land. Both are armed now, and the derivation arm was rebuilt once because equal
  budgets make the two formulas agree exactly: the fixture lowers one row so 140 s and 240 s are
  distinguishable, and the arm was staged red against the old formula.
- **LOW x4** — a leading zero passed the digit test and then read as octal (`10#` now); a comment
  its own commit had falsified; `SELF` came out ABSOLUTE because `cd && pwd` yields an MSYS path
  while `git rev-parse --show-toplevel` yields a Windows one, so the prefix strip silently did
  nothing (git answers both halves now); and a stale wall figure in this ledger.

A ninth defect fell out of running the fix rather than reading it: a suite the wall stops from
LAUNCHING has no result at all, which is a different fact from one that started and was killed.
Reporting both as `killed` would tell an operator the suite had been tried. It renders `UNRUN` and
the summary names those suites as UNGRADED.

**What the exit costs, stated rather than left implicit.** This fold is unreviewed surface: round 1's
fold contained three blockers that round 2 found, and nothing reviews round 2's. That is the price
of the method's termination rule, which forbids re-reviewing at a non-convergent exit. The
compensating check is the arm count — 43 against a floor of 43, every new arm staged red and watched
to fail — and it is a weaker thing than a review.
