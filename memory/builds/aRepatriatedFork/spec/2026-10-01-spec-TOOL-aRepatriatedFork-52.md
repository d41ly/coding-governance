# TOOL-aRepatriatedFork-52 — the foreign-prefix leg asks only the prefix question

**Status:** SPECCED · rev-1 · 2026-10-01 · node a · Tier-2 · base 56c7befa · streams tooling · order 25

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-prompt-TOOL-aRepatriatedFork-52-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aRepatriatedFork-52-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aRepatriatedFork-30` built the foreign-prefix leg as a calibrate pass plus three pooled runs
of the whole self-test population, one run per prefix. Its second run took about 1.6 hours to
calibrate at `tools/`, kept running for hours after it had redded at `scripts/` and `vendor/gov/`,
and said nothing while it did. The question the leg exists to answer is narrower: does each suite
still find its subject when gov's tool root sits somewhere else. This unit redesigns the leg to ask
only that, per suite its path-finding prologue plus one arm that touches its subject, at each prefix,
with no calibrate pass, failing fast and printing a line per suite. The owner expects minutes.

## 2. Scope (IN)

- **S1** — THE PROBE MODE. A suite run with `FOREIGN_PREFIX_PROBE=1` in its environment runs its
  prologue, then the first arm that exercises its subject, prints
  `foreign-prefix-probe: stopped after 1 arm`, prints its own trailer for that one arm and exits with
  that arm's verdict. One environment flag for shell and python suites alike, honoured at one site
  per suite, placed by that suite after the arm it chooses. `tools/lib/lib-selftest.sh` honours it
  once inside `run_arms`, which runs only the first declared arm, so every suite on that harness is
  covered by one site. Without the flag every suite runs exactly as at base. Observed by AC2.
- **S2** — THE POPULATION is every row `run-selftests.sh --list` prints, with the argv it prints,
  less this leg's own row, which the leg skips while iterating. The clone's budget file and leg
  manifest are moved with the tool root and otherwise left byte-identical to HEAD, so govkit's
  registry rows and the codebase map still agree with them inside the clone. Observed by AC5 and AC7.
- **S3** — THE WHOLE-RUN DECLARATION. A suite whose prologue cannot be separated from the rest
  runs whole and is NAMED: the leg file carries a declared list of those rows, each with its reason.
  A row on the list that prints the probe marker reds as a stale declaration, and a row off the list
  that prints none reds as an undeclared whole run. Every whole-run row is printed on every run.
  Observed by AC3.
- **S4** — THE MOVE. A scratch clone at HEAD, the whole tool root moved with `git mv` to
  `scripts/`, then `vendor/gov/`, then the repository root, as `TOOL-aRepatriatedFork-30` §8 F1
  (b) ruled. Each move re-spells gov's own declarations by the old root's path head, as an install
  at that prefix carries them: the charter, `.claude/`, the hook config's `GOV_KITROOT`, the conf
  files, the codebase map and the renders `check-install-prefix.sh --list` names. Files the move
  brought in are not re-spelled except those renders, and the record corpus under `memory/builds/`,
  `memory/archive/`, `memory/ledger/`, `memory/backlog/` and `memory/DECISIONS.md` never is. A move
  that lists no render, or re-spells no file, refuses rather than grading blind. This is the VERIFYING
  repair pass R2's re-declaration, landed. Observed by AC8.
- **S5** — THE BASELINE is the bar's own record, never a calibrate. The leg reads the newest
  `<git-dir>/gate-run/<id>/header` whose `head` equals the commit under test and whose `tree_clean`
  is `yes`. A suite whose row in that run is red is named as red at gov's prefix in that run and is
  not graded at a foreign prefix, because the bar's own leg for it already reds. With no such run,
  or no row for a suite, the suite is expected green, and the leg prints once that no recorded run
  covers this tree. Observed by AC6.
- **S6** — THE VERDICT AND ITS COST. At each prefix the population runs through a bounded pool of
  the width `run-gates.sh --print-profile` reports. As each suite completes the leg prints one line,
  `[<prefix>] <row> · probe|whole · rc <n> · <s>s`, which is also its heartbeat for
  `TOOL-aRepatriatedFork-53`'s audit when the run registers the leg's output log. A suite is green
  at a prefix when it exits 0 and, unless declared whole, printed the probe marker. After a prefix
  with any red the leg stops, prints each later prefix as `not run`, and exits 1 naming every red
  suite with its prefix and the tail of its output. The clone's tree must be clean after each
  prefix, or the leg reds naming what a suite wrote outside its scratch. `--kit <substring>` still
  selects a slice. Observed by AC1, AC4 and AC5.
- **S7** — THE HEADER. "What this does not check" states that history-bound arms, such as govkit
  selftest's vintage arms that read gov's history at its historical prefix, are outside the prefix
  question by construction and are not reached by a probe; that whether a suite's probe arm touches
  its subject is that suite's claim and is not graded; that gov's prefix is never probed; and that a
  declaration naming the old root in any spelling but its path head keeps gov's spelling. Observed
  by AC9.
- **S8** — THE CEILING is measured. The leg's `ceiling` in `tools/gate-legs.json` and its row in
  `tools/run-gates/selftest-budgets.txt` are re-derived from AC10's run through
  `derive-ceilings.py --write --observed` and the margin rule, and stay under the profiles' 21600 s
  wall. Observed by AC10 and AC11.
- **S9** — Every kit whose shipped bytes move takes its version bump in every carrier. Observed by
  AC12.

## 3. Non-goals (OUT)

- Amending `TOOL-aRepatriatedFork-30`. It is CLOSED, its S1 leg is the subject redesigned here, and
  its acceptance ledger stays the landed record of the first design.
- Grading gov's history at a relocated prefix. What a relocated gov's history means is an open
  question the repair record states, and a history-bound arm is out of the prefix question.
- A cost verdict per suite. `run-selftests.sh --serial` issues those; this leg grades the prefix.
- Stopping the leg from outside. When a run starts it in the background, registering and watching
  it is `TOOL-aRepatriatedFork-53`'s.
- Gate semantics at a root install. Those are `TOOL-aRepatriatedFork-54`'s, which this leg relies on.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-53` — the task registration and the audit's task line.
  Without them the per-suite progress line has no reader, and a background run of this leg is as
  silent to the idle-wake as the run that motivated both units.
- **consumes-from** `TOOL-aRepatriatedFork-54` — the playbook-parity and spec-tokens gates grading
  a root install correctly. Without them both suites red at the root by construction, and the leg
  stops there.

## 4. Design

### Evidence

- The killed second run's output, kept in the session scratch of 2026-10-01 (`fp.out`, not
  committed): the calibrate read 80 suites in a serial sum of 30842 s on node a, the unattended
  driver selftest alone 4175 s, and the run then redded at `vendor/gov/` on 13 rows. PINNED,
  measured at `801fa7e6`.
- The VERIFYING repair record of 2026-10-01: what stayed red at foreign prefixes and why, including
  item 4, the leg's own population edit that left govkit's registry and the map disagreeing with the
  clone's manifest, and item 1, gov's declarations not moving with the tool root.
- `extract-arms.sh`'s header records at least five unrelated per-arm output idioms across the
  suites, which is why no runner can find "the first arm" from outside a suite reliably.
- Gate-run records: each `<git-dir>/gate-run/<id>/` holds a `header` with `head`, `tree_clean` and
  `full`, and one `<n>.leg` row per leg whose first two fields are the leg name and its status.

### Inventory

New identifiers: the environment flag `FOREIGN_PREFIX_PROBE`, the marker line
`foreign-prefix-probe: stopped after 1 arm`, and the leg's whole-run list, one declared array in
`foreign-prefix.gov.test.sh` of row name and reason. Function names in the leg are confirmed with
`python tools/lexicon/lexicon.py --suggest <name>` before writing, and a refusal renames them as a
rev bump here first.

### Files touched (estimate)

- `tools/run-gates/foreign-prefix.gov.test.sh`
- `tools/lib/lib-selftest.sh`
- `tools/run-gates/selftest-budgets.txt`
- `tools/gate-legs.json`
- `tools/run-gates/ceiling-evidence.txt`
- every suite in the population that is not on `lib-selftest.sh`, one honouring site each
- the version carriers of every kit whose shipped suite moves

### Alternatives rejected

- A per-suite registry naming the arm to run. Every suite would still need a way to run one named
  arm, so it is strictly more mechanism, and arm labels are free text that drifts.
- Stopping each suite from outside at its first per-arm verdict line. It edits no suite, but it
  kills processes mid-run, which on this host leaves detached children and scratch behind, and the
  first verdict a suite prints is not always one that touched its subject.
- Keeping `run-selftests.sh --pooled` as the runner. Its parity needs calibrated readings, which the
  owner ruled out, and its executed-count comparison has no meaning for a one-arm probe.

## 5. Production-readiness checklist

- security — none; a scratch clone, hermetic suites, and a read of the bar's own records.
- perf / scale — one prologue and one arm per suite per prefix, pooled; the owner expects minutes,
  and AC10 measures it.
- error / empty / loading states — an empty population, an empty render list and a move that
  re-spells nothing each refuse by name.
- observability — one line per suite as it completes, the whole-run rows on every run, and a
  `not run` line per prefix skipped.
- risks — a probe arm that does not touch its subject passes vacuously; S7 states it, and AC1 is
  the control that the class the leg exists for still reds.
- testing — AC1 to AC12.
- migration — none; the flag is inert unless set.
- user docs — none; the leg is gov-only and withheld from adopters.

## 6. Acceptance criteria

- **AC1** — Red-first control: in a scratch clone one suite's prologue is given back a literal
  `tools/` path, and the leg run with `--kit <that suite>` exits 1 naming that suite at
  `scripts/`; with the literal gone it exits 0. Staged, recorded and discarded.
  Red when: the leg stays green, so it cannot see the class it exists for.
- **AC2** — When one shell suite and one python suite run with `FOREIGN_PREFIX_PROBE=1`, each prints
  `foreign-prefix-probe: stopped after 1 arm` and a trailer of one executed assertion; without the
  flag each prints its base count.
  Red when: the flag changes nothing, or changes a run without it.
- **AC3** — In a scratch clone, a declared whole-run row made to print
  `foreign-prefix-probe: stopped after 1 arm` reds as a stale declaration, and an undeclared row made to print none reds as an undeclared whole run.
  Red when: either passes.
- **AC4** — In a scratch clone with one suite broken only at `scripts/`, the leg prints `not run` for
  `vendor/gov/` and for the root and exits 1.
  Red when: a later prefix runs after a red one.
- **AC5** — In AC10's run, each prefix prints one `[<prefix>]` line per row of the population S2
  names, less the leg's own.
  Red when: a row has no line, or a line has no `probe` or `whole` field.
  figure: DERIVED at observation time.
- **AC6** — With a fabricated `gate-run` record at HEAD marking one suite red, the leg names that
  suite as red at gov's prefix and does not grade it; with no record at HEAD it prints its
  no-recorded-run line once.
  Red when: an inherited red is graded as a prefix defect, or the absent baseline is silent.
- **AC7** — When the leg's clone sits at each prefix, `git diff --stat` against the move commit
  shows no change to the clone's budget file or leg manifest.
  Red when: the leg edits its own population inside the clone, as the `56c7befa` leg does.
- **AC8** — At each move the leg prints how many declaration files it re-spelled, and a clone where
  `check-install-prefix.sh --list` names no render makes it refuse naming that.
  Red when: a move re-spells nothing and still grades.
- **AC9** — When the leg's header is read, its `WHAT THIS DOES NOT CHECK` list names history-bound arms, the probe arm's choice, gov's own prefix and non-head
  spellings of the old root.
  Red when: any of the four is missing.
- **AC10** — When the main loop runs the leg whole on this tree, it prints `PASS` after all three
  prefixes, every row is probed or declared whole, and its own seconds are under 3600 on node a. The
  acceptance ledger records the per-suite table.
  Red when: any row reds, or the run takes hours.
  permission: a held leg; the main loop runs it once, after this unit's code is committed.
  cost: the run itself, expected minutes.
  figure: 3600 is PINNED from the owner's ruling; the seconds are DERIVED from the run.
- **AC11** — `python tools/run-gates/derive-ceilings.py --check` exits 0 with the leg's ceiling
  re-derived from AC10's reading, and that ceiling is below 21600.
  Red when: the ceiling is still the sized figure, or breaks the profiles' wall.
- **AC12** — `bash tools/check-kit-versions.sh` exits 0 and
  `python tools/govkit/govkit.py epoch --base 56c7befa` names no kit whose bytes moved without its
  version.
  Red when: a moved kit's carrier was missed.

## 7. Gates

`every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `testsuite counts (every bar self-test prints one)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `run-gates canary` · `run-gates gov canary` · `selftest harness self-test` · `extract-arms self-test` · `run-selftests self-test` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `python resolver (behaviour + inline parity + idiom ban)`

New arm: the leg itself · AC1's literal prefix given back to one suite in a scratch clone · none

New arm: `tools/lib/lib-selftest.test.sh` · a harness suite run with the probe flag runs one arm and prints the marker · the suite's floor rises by one

## 8. Open questions

- **F1 — how does a suite expose "prologue plus one arm"?** Option (a): one environment flag,
  `FOREIGN_PREFIX_PROBE`, honoured at one site per suite placed after the arm that suite chooses,
  and once in the shared harness. Option (b): a per-suite registry naming an arm the leg asks for.
  Option (c): no suite edit; the leg stops each suite at its first per-arm verdict line.
  Recommendation: (a). It is the one mechanism that works identically in shell and python and lets
  each suite pick an arm that touches its subject; (b) needs (a)'s per-suite site plus a drifting
  registry, and (c) kills processes mid-run and cannot pick the arm.
  RESOLVED (agent, 2026-10-01, delegated): (a).
- **F2 — what is the baseline when the bar has no record at this tree?** Option (a): every suite is
  expected green, announced once. Option (b): refuse until such a record exists. Option (c): probe
  at gov's prefix first. Recommendation: (a). Option (c) is the calibrate the owner ruled out, and
  (b) makes the leg unrunnable inside the very bar that writes the record it waits for.
  RESOLVED (agent, 2026-10-01, delegated): (a).
- **F3 — fail fast at which grain?** Option (a): finish the first red prefix, then stop. Option (b):
  stop at the first red suite. Recommendation: (a). The owner named the prefix as the grain, and
  (a) names every red suite at that prefix in one run instead of one per run.
  RESOLVED (agent, 2026-10-01, delegated): (a).
- **F4 — how are whole-run suites known?** Option (a): derived from the absent marker and named.
  Option (b): declared in the leg with a reason, red in both directions. Recommendation: (b). With
  (a) a suite whose honouring site regresses silently costs hours and is merely named; (b) reds it,
  which is the declared-population rule this repo applies to every other exemption.
  RESOLVED (agent, 2026-10-01, delegated): (b).

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft from the owner's 2026-10-01 ruling adopting this unit, with
  R2's re-declaration patch folded in as S4.

## 10. Reuse audit

The seams are the leg itself, `tools/run-gates/foreign-prefix.gov.test.sh`, redesigned in place;
`run-selftests.sh --list` for the population and its argv; `run-gates.sh --print-profile` for the
pool width; `check-install-prefix.sh --list` for the renders S4 re-spells; and `run_arms` in
`tools/lib/lib-selftest.sh` for the harness suites. `python tools/codebase-map/reuse_lookup.py "run
each self-test suite at a foreign install prefix"` returned only name-stem neighbours and reports
`.sh` as an unscanned layer, so those seams were found by reading the leg and its siblings. The
recall probe's hits were `TOOL-aRepatriatedFork-30`, its acceptance ledger and the VERIFYING repair
record, which this unit's design answers.

Recall terms used: `foreign-prefix parity calibrate pooled held leg prefix scripts vendor root suite arm probe baseline`.
