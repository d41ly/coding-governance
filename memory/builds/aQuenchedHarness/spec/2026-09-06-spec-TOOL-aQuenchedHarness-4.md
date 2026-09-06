# TOOL-aQuenchedHarness-4 — one on-demand runner for every kit's self-tests, budget-graded

**Status:** OPEN · rev-1 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Give the whole held population one command, with a DECLARED budget per suite that REDS on breach.
`tools/unattended/run-unattended-gates.sh` already does this for one kit under the owner ruling of
2026-08-23; every other kit's self-tests have no runner at all, so the compensating check that
replaces a bar leg exists for one kit and is imaginary for the rest.

## 2. Scope (IN)

- **S1** — `tools/run-gates/run-selftests.sh`, which runs exactly the legs the bar HOLDS, taking that
  set from `tools/gate-legs.json` through the same hold predicate the runner uses. The population is
  DERIVED; no list of suite names is typed anywhere.
- **S2** — a declared budget per suite in `tools/run-gates/selftest-budgets.txt`, each carrying the
  reading it was set against, in the idiom `run-unattended-gates.sh` already uses in prose and
  `gate-profiles.txt` uses as a data file.
- **S3** — a MISSING budget is a FAILURE, not an exemption. A suite added without one would be exempt
  from the rule by the act of arriving, which is how every population in this repo has previously
  gone quiet. This rule is lifted verbatim from `run-unattended-gates.sh`, where it already exists.
- **S4** — a `--kit <dir>` filter, so kit work can run only the suites for the kit it touched, and a
  liveness refusal when the filter matches nothing: an unknown filter and a clean sweep are
  indistinguishable from outside.
- **S5** — the total budget is DERIVED and printed, never typed. The sum of the declared ceilings is
  what the operator is being asked to spend, and a figure typed beside the declarations that own it
  is the defect this repo keeps re-filing.
- **S6** — `tools/unattended/run-unattended-gates.sh` becomes a thin `--kit tools/unattended` call
  into this runner, so its budgets and its split survive as data rather than as a second
  implementation. Its record-and-wiring checks stay bar legs, unchanged.
- **S7** — arms staging: a suite over budget, a suite with no budget, a filter matching nothing, and
  a green sweep.

## 3. Non-goals (OUT)

- Not changing WHICH legs are held. That predicate is `TOOL-aQuenchedHarness-3`'s.
- Not making anything run on a bar. No boundary sets `GATE_SELFTESTS`, that is an owner ruling of
  2026-08-27 recorded in `AGENTS.md`, and this unit does not disturb it.
- Not a hang bound: a budget is a COST verdict. The hang bounds are units 1 and 2, and
  `run-unattended-gates.sh` already records why the two figures must not be confused.
- Not making the suites faster. That is units 5, 6 and 7; this unit is what makes their result
  legible and what stops the next regression from being invisible.

## 4. Design

### Data model

`tools/run-gates/selftest-budgets.txt` — `<leg name>\t<seconds>\t<the reading it was set against>`,
one row per held leg, comments carrying the argument. Rows are keyed by the leg NAME from
`tools/gate-legs.json`, so the join is exact and a renamed leg reds as unbudgeted rather than
silently losing its ceiling.

### The split, restated as data

`run-unattended-gates.sh`'s header states the split that justifies the whole ruling: RECORD AND
WIRING checks read the REPOSITORY and stay bar legs, because they go stale with nobody editing the
kit; SELF-TESTS read the KIT and have a job only when kit source changes. That split is already
expressed in `tools/gate-legs.json` as `subject`, so this runner needs no second expression of it —
it runs what the bar holds, and the bar holds by subject and chunk.

### Rollout

The runner lands first and is green over the current population at whatever the current population
costs. The budgets land with it, seeded from the ledger, so the first run is a measurement rather
than a wall of red. Units 5, 6 and 7 then lower the readings, and each lowering is a visible edit to
this file.

### Inventory

- `tools/run-gates/run-selftests.sh` — the runner.
- `tools/run-gates/selftest-budgets.txt` — the declarations.
- `--kit` — the filter verb.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` (new) · `tools/run-gates/selftest-budgets.txt` (new) ·
`tools/unattended/run-unattended-gates.sh` (reduced to a delegation) · `tools/run-gates/kit.toml` ·
`AGENTS.md` · a self-test beside the runner.

### Alternatives rejected

A `--selftests` MODE of `tools/run-gates/run-gates.sh` was rejected: the bar's runner is 1480 lines
carrying a turnstile, a profile table, a reuse key and a run record, and a mode that suppresses most
of it would make the bar's own control flow depend on a flag that exists for a different purpose.
A second, small entry point that reads the same manifest is the cheaper seam and cannot destabilise
the bar.

## 5. Production-readiness checklist

- security — runs the same executables the bar would; no new surface.
- perf / scale — the runner adds one process; the cost is the suites, which is the point of the
  budgets.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — over budget, no budget, no match, and green are four distinct
  lines. The no-match case exits non-zero.
- observability — a per-suite line with its seconds and its ceiling, and a derived total.
- risks — a budget calibrated idle will breach on a busy box, which `run-unattended-gates.sh`
  already records at 2.4x for this node. The remedy stated there is kept: read a breach by re-running
  on an idle box, and the file says so rather than absorbing the load into a bigger number.
- testing + left-shift gates — S7's arms, each observed RED before landing.
- migration / rollback — deleting the runner restores today's state, in which only one kit has one.
- user docs — `AGENTS.md`'s bar section gains the command; the budgets file carries its own header.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-selftests.sh` runs, the suites it executes are exactly the
  legs a default `bash tools/run-gates/run-gates.sh` reports as held, compared set-to-set.
- **AC2** — When a suite exceeds its declared budget, the runner prints `OVER BUDGET` naming the suite,
  its seconds and its ceiling, and exits non-zero.
- **AC3** — When a held leg has no row in `tools/run-gates/selftest-budgets.txt`, the runner fails
  naming it, so a suite cannot arrive exempt.
- **AC4** — When `--kit tools/nosuchkit` matches nothing, the runner exits non-zero saying it graded
  nothing, rather than printing a green line.
- **AC5** — When the help text is printed, its total is the sum of the rows in
  `selftest-budgets.txt` computed at run time, and editing a row changes the printed total.
- **AC6** — When `bash tools/unattended/run-unattended-gates.sh --selftests` runs, it produces the
  same verdicts as before this unit, proving the delegation preserved the kit's own behaviour.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `unattended kit gate` and `unattended skill wiring`, which
grade the script this unit reduces · the new runner's own self-test, held like every other ·
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at the Definition of Done, because this is kit
work.

## 8. Open questions

- **F1 — does the runner run suites concurrently?** RESOLVED (agent, 2026-09-06, delegated): yes,
  through the same bounded-width idea the bar uses, because a serial sweep of the held population is
  the hour-long compensating check `run-unattended-gates.sh` records being abandoned twice. The width
  is read from the same `gate-profiles.txt` row rather than declared again.
- **F2 — where do the initial budget readings come from?** RESOLVED (agent, 2026-09-06, delegated):
  from `<git-dir>/gate-ledger.tsv`, the same source `TOOL-aQuenchedHarness-2` derives ceilings from,
  and each row records that its reading was taken UNDER LOAD where it was. A reading whose conditions
  are unstated is the thing `run-unattended-gates.sh` had to apologise for in prose.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.

## 10. Reuse audit

The seam is `tools/unattended/run-unattended-gates.sh`, which already implements this exact mechanism
for one kit — the split, the per-suite `BUDGET_*` ceilings, the missing-budget failure, the derived
total and the liveness refusal — under an owner ruling recorded in `AGENTS.md`. This unit generalises
that file rather than authoring a second one, and reduces it to a delegation so the two cannot
diverge. `tools/codebase-map/reuse_lookup.py` returned `.unattended.conf` [unattended] and
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as the affordance seams. The declared-value file
shape is `tools/run-gates/gate-profiles.txt`'s, which itself cites `tools/template-size-limits.txt`
as this tree's settled answer.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
