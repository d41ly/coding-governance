# TOOL-aQuenchedHarness-4 — one on-demand runner for every kit's self-tests, budget-graded

**Status:** CLOSED · rev-5 · 2026-09-07 · node a · Tier-2 · base faaea5f5 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-07-build-TOOL-aQuenchedHarness-4-acceptance-ledger-on-demand-runner.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-4-acceptance-ledger-on-demand-runner.md) | journal | — |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 |
| [2026-09-07-review-TOOL-aQuenchedHarness-7-closing-diff-review.md](../reviews/2026-09-07-review-TOOL-aQuenchedHarness-7-closing-diff-review.md) | diff-review | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 |

<!-- /gen:spec-records -->

## 1. Goal

Give the whole self-test population one command, with a DECLARED budget per suite that REDS on
breach. `tools/unattended/run-unattended-gates.sh` already does this for one kit under the owner
ruling of 2026-08-23; every other kit's self-tests have no runner at all, so the compensating check
that replaces a bar leg exists for one kit and is imaginary for the rest.

## 2. Scope (IN)

- **S1** — the POPULATION IS DECLARED, in `tools/run-gates/selftest-budgets.txt`: one row per suite
  carrying its name, its argv and its budget. Rev-1 derived the population from held manifest legs;
  the audit measured that the six suites `tools/unattended/run-unattended-gates.sh` runs are in
  NEITHER `tools/gate-legs.json` NOR `tools/unattended/kit.toml`, because the 2026-08-23 ruling
  removed them from both. A derivation over the manifest cannot see a suite the manifest was told to
  forget.
- **S2** — the declaration is asserted in BOTH directions and the assertion is a gate leg. Forward:
  every leg the bar HOLDS has a row. Reverse: every row whose name is not a held leg names an argv
  whose first file argument is TRACKED, so a row cannot name a suite that does not exist. Either
  direction failing is a refusal.
- **S3** — a MISSING budget is a FAILURE, not an exemption. A suite added without one would be exempt
  from the rule by the act of arriving. Lifted verbatim from `run-unattended-gates.sh`, where it
  already exists.
- **S4** — `tools/run-gates/run-selftests.sh` runs the declared population, times each suite, and REDS
  on a breach naming the suite, its seconds and its ceiling.
- **S5** — a `--kit <dir>` filter over the declaration, and a liveness refusal when it matches
  nothing: an unknown filter and a clean sweep are indistinguishable from outside.
- **S6** — the total is DERIVED and printed, never typed. The sum of the declared ceilings is what
  the operator is being asked to spend, and a figure typed beside the declarations that own it is the
  defect this repo keeps re-filing.
- **S7** — `tools/unattended/run-unattended-gates.sh` delegates its `--selftests` half to this runner
  and KEEPS its `--checks` half unchanged, along with the four repo-leg budgets that half owns
  (`BUDGET_kit_gate`, `BUDGET_playbook_validity_gate`, `BUDGET_skill_wiring`,
  `BUDGET_pass_order_history`). Rev-1 dissolved the whole file into a `--kit` call; the audit measured
  that its four `--checks` rows are all `subject = repo` and therefore in no held population, that
  `tools/unattended/kit.toml` declares `--all` as this kit's compensating check, and that
  `TOOL-aQuenchedHarness-7` AC4 invokes both by name.
- **S8** — THE COMPOSITE WIDTH IS DECLARED. This runner resolves the profile row's width W, runs
  suites at an outer width, and EXPORTS the inner arm-pool width as `max(1, W / outer)` in a named
  variable `TOOL-aQuenchedHarness-5` S3 reads. Two pools each reading W independently would give
  W squared — 64 concurrent processes at node `a`'s width 8, on a host where a bare spawn costs
  319 ms.
- **S10** — BOTH NEW FILES ARE WITHHELD FROM ADOPTERS. `tools/run-gates/run-selftests.sh` and
  `tools/run-gates/selftest-budgets.txt` are gov-only: the budgets file is a declaration of GOV's own
  corpus whose rows name paths no adopter has, and the runner reads it. They are claimed with
  `role = "project-owned"` in `tools/run-gates/kit.toml`, exactly as that descriptor already withholds
  `run-gates.gov.test.sh`, and the new gate leg is declared with an `[[exempt_leg]]` row rather than a
  `[[gate_leg]]` one. Without this the descriptor's `include = "**"` rule ships both, and an adopter's
  bar reds on first invocation against a population that is not theirs.
- **S11** — the profile width is resolved through a SHARED reader, not re-implemented. Profile
  selection is inline in `tools/run-gates/run-gates.sh` today and is unreachable from another script,
  so S8's "this runner resolves the profile row's width W" needs a seam that does not exist: either a
  `--print-profile` verb on `run-gates.sh` that emits the selected row, or a
  `tools/run-gates/lib-profile.sh` both scripts source. One resolver, two readers; two resolvers is
  the drift class this build cites elsewhere by name.
- **S9** — arms staging: a suite over budget, a suite with no budget, a declared row whose argv names
  no tracked file, a held leg with no row, a filter matching nothing, and a sweep whose observed
  concurrent-process count exceeds W.

## 3. Non-goals (OUT)

- Not changing WHICH legs the bar holds. That is `TOOL-aQuenchedHarness-3`, and after its rev-2 the
  answer is "exactly today's set".
- Not making anything run on a bar. No boundary sets `GATE_SELFTESTS`; that is an owner ruling of
  2026-08-27 recorded in `AGENTS.md`, verified at source — `.githooks/gate-env.sh` refuses a bare
  assignment and `govkit.py:1735` gates the pattern.
- Not a hang bound: a budget is a COST verdict. The hang bounds are units 1, 2 and 8, and
  `run-unattended-gates.sh` already records why the two figures must not be confused.
- Not making the suites faster. That is units 5, 6 and 7; this unit is what makes their result
  legible and what stops the next regression from being invisible.
- Not budgeting repo-subject legs. Those keep their budgets where they already live, in
  `run-unattended-gates.sh` per S7. `TOOL-aQuenchedHarness-7` H5's join question is settled there,
  not here.

## 4. Design

### Data model

`tools/run-gates/selftest-budgets.txt` — `<name>\t<budget seconds>\t<argv>\t<the reading it was set
against>`, one row per suite, comments carrying the argument. Rows whose name matches a held leg in
`tools/gate-legs.json` take their argv from the manifest and leave the field empty; rows that do not
carry their own argv, which is how the six unattended suites become nameable at all.

### The split, and why it is not re-expressed

`run-unattended-gates.sh`'s header states the split that justifies the whole ruling: RECORD AND
WIRING checks read the REPOSITORY and stay bar legs; SELF-TESTS read the KIT and have a job only when
kit source changes. The first half lives in `tools/gate-legs.json` as `subject`. The second half
lives, for the unattended kit, nowhere machine-readable — which is the gap S1 fills.

### Rollout

The runner and the declaration land together, seeded from whatever readings exist, so the first run
is a measurement rather than a wall of red. Units 5, 6 and 7 then lower the readings, and each
lowering is a visible edit to this file.

### Inventory

- `tools/run-gates/run-selftests.sh` — the runner.
- `tools/run-gates/selftest-budgets.txt` — the declaration and the population.
- `SELFTEST_INNER_WIDTH` — the exported inner-pool width, S8's named variable.
- `every held leg is budgeted, every budget row resolves` — the new gate leg's name.

### Files touched (estimate)

`tools/run-gates/run-selftests.sh` (new) · `tools/run-gates/selftest-budgets.txt` (new) ·
`tools/run-gates/run-gates.sh` (S11's shared profile reader) · `tools/unattended/run-unattended-gates.sh`
(its `--selftests` half only) · `tools/gate-legs.json` · `tools/run-gates/kit.toml` (the
`project-owned` rules and the `[[exempt_leg]]` row) · `.lexicon.conf`, for the `VERB_OFFENDER_PIN`
move any new shell function forces · `AGENTS.md` · a self-test beside the runner.

### Alternatives rejected

**Deriving the population from held manifest legs** — rev-1's design — was rejected on measurement:
the ten suites the delegation targets contain zero held legs, so `--kit tools/unattended` resolved to
nothing and S5's own liveness refusal would have fired on the filter the spec mandated.

**A `--selftests` MODE of `tools/run-gates/run-gates.sh`** was rejected: that runner is 1480 lines
carrying a turnstile, a profile table, a reuse key and a run record, and a mode that suppresses most
of it would make the bar's control flow depend on a flag that exists for a different purpose.

## 5. Production-readiness checklist

- security — runs the same executables the bar would; no new surface. S2's reverse direction requires
  a row's argv to name a TRACKED file, which is what stops the declaration becoming a way to run
  arbitrary paths.
- perf / scale — S8's composite bound is the scale question and is answered there rather than left to
  two specs each believing they honour one width.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — over budget, no budget, unresolvable row, no match, and green are
  five distinct lines. The no-match case exits non-zero.
- observability — a per-suite line with its seconds and its ceiling, and a derived total.
- risks — a budget calibrated idle will breach on a busy box, which `run-unattended-gates.sh` records
  at 2.4x for this node. The remedy stated there is kept: read a breach by re-running on an idle box,
  and say so rather than absorbing the load into a bigger number.
- testing + left-shift gates — S9's arms, each observed RED before landing, plus S2's both-direction
  leg.
- migration / rollback — deleting the runner restores today's state, in which only one kit has one.
  `run-unattended-gates.sh` keeps its `--checks` half throughout, so nothing that depends on it
  breaks mid-migration.
- user docs — `AGENTS.md`'s bar section gains the command; the declaration carries its own header.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-selftests.sh` runs, the suites it executes are exactly the
  rows of `tools/run-gates/selftest-budgets.txt`, and that set CONTAINS the six unattended suites by
  name, so the delegation S7 makes is non-empty.
- **AC2** — When a suite exceeds its declared budget, the runner prints `OVER BUDGET` naming the
  suite, its seconds and its ceiling, and exits non-zero.
- **AC3** — When a held leg in `tools/gate-legs.json` has no row, the
  `every held leg is budgeted, every budget row resolves` leg reds naming it.
- **AC4** — When a budget row's argv names a file `git ls-files` does not carry, the same leg reds —
  the reverse direction, so a row cannot name a suite that is not there.
- **AC5** — When `--kit tools/nosuchkit` matches nothing, the runner exits non-zero saying it graded
  nothing, rather than printing a green line.
- **AC6** — When `bash tools/unattended/run-unattended-gates.sh --all` runs, it produces the same
  verdicts as before this unit for BOTH halves, `--checks` and `--selftests`, and
  `BUDGET_kit_gate` still exists and still binds.
- **AC8** — When `govkit` applies to a fixture target, neither `run-selftests.sh` nor
  `selftest-budgets.txt` is present and the new leg is in no emitted manifest row.
- **AC9** — When `bash tools/run-gates/run-selftests.sh` resolves its width, the value is byte-equal to
  the one `bash tools/run-gates/run-gates.sh` prints on its own profile line, on the same host — one
  resolver, two readers.
- **AC7** — When a sweep of `bash tools/run-gates/run-selftests.sh` runs, the observed peak count of
  concurrent descendant processes is at most the profile row's declared width, asserted by an arm
  rather than by the two specs each assuming it.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the new `every held leg is budgeted, every budget row resolves`
leg · `profile-bar selftest`, which owns the width-resolution comparison S11 introduces · the
`lexicon naming predicates` leg, which grades the new runner's function names ·
`unattended kit gate` and `unattended skill wiring`, which grade the script this unit edits ·
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at the Definition of Done, because this is kit
work · `bash tools/unattended/run-unattended-gates.sh --all`, this kit's declared compensating check.

## 8. Open questions

- **F1 — does the runner run suites concurrently?** RESOLVED (agent, 2026-09-06, delegated): yes, at
  an OUTER width, with the inner arm pool bounded by S8's exported `max(1, W / outer)`. A serial
  sweep is the hour-long compensating check `run-unattended-gates.sh` records being abandoned twice;
  two unbounded pools are the 64-process sweep the audit measured. Neither is acceptable and the
  composite is declared rather than assumed.
- **F2 — where do the initial budget readings come from?** RESOLVED (agent, 2026-09-06, delegated):
  from `<git-dir>/gate-run/<runid>/<i>.leg` where the suite is a held leg, and from a direct timed
  invocation where it is not — the six unattended suites have no manifest row and therefore no leg
  file. Each row records the conditions its reading was taken under, because a reading whose
  conditions are unstated is the thing `run-unattended-gates.sh` had to apologise for in prose.

## 9. Revision log

- rev-5 · 2026-09-07 · CLOSED, and it gained the failing case it landed without. `run-selftests.test.sh` gives the runner thirteen arms -- every refusal it carries, each observed RED -- and they found two defects on their first run: the `UNRESOLVED` branch was unreachable because tab is IFS whitespace and the empty argv field collapsed, and underneath it the emitter was writing CRLF, invisible until the field order changed. `--rank` was added here rather than in a new file, and the composite width bound was corrected: its run loop is serial on purpose, so dividing by an outer pool of 4 handed every ported suite a quarter of its width.

- rev-1 · 2026-09-06 · initial draft.
- rev-4 · 2026-09-07 · BUILT. S11's shared width resolver is `bash tools/run-gates/run-gates.sh
  --print-profile`, placed BEFORE the turnstile so asking costs nothing and takes no beacon; the
  runner reads `width` from it and exports `SELFTEST_INNER_WIDTH` as S8 requires. The declaration is
  55 rows — 49 held legs plus the six unattended suites that live in no manifest at all, which is the
  whole reason S1 declares the population rather than deriving it.
  **THE NUMBER THIS UNIT EXISTS TO MAKE VISIBLE: the declared budgets sum to 42020 s — 11.7 HOURS.**
  Nobody runs an eleven-hour check, and `TOOL-aQuenchedHarness-9` is what that costs in practice:
  `govkit selftest` sat with two arms red for long enough that nobody can say when they broke. Units
  5 and 6 are the answer; this unit is what makes their result legible and what stops the next
  regression being invisible.
  Both failing cases observed: a held leg with no row REDs naming it, and a row naming an untracked
  file REDs naming the path. A filter matching nothing exits 2 rather than printing a green line.
- rev-3 · 2026-09-06 · folded spec-audit round 2. B7: both new files were shipping to adopters
  through `tools/run-gates/kit.toml`'s `include = "**"` rule — a declaration of gov's own corpus whose
  rows name paths no adopter has — so S10 withholds them with `role = "project-owned"` and declares
  the leg `[[exempt_leg]]`. H6: profile selection is inline in `run-gates.sh` and unreachable from
  another script, so S8's width resolution had no seam; S11 names one and AC9 asserts byte-equality
  between the two readers. H3: §7 names the lexicon leg and Files touched carries `.lexicon.conf`.
- rev-2 · 2026-09-06 · folded spec-audit round 1. B2: the population is now DECLARED rather than
  derived from held manifest legs, because the ten suites the delegation targets contain zero held
  legs — the 2026-08-23 ruling removed them from the manifest and the descriptor both — and the
  delegation would have matched nothing; S7 now keeps `run-unattended-gates.sh`'s `--checks` half and
  its four repo budgets rather than dissolving the file, which unit 7 AC4 and
  `tools/unattended/kit.toml` both depend on. H4: S8 declares the composite width, since unit 5 S3
  and this unit's F1 each read the same profile width and would have squared it. AC6 now exercises
  `--all`, not `--selftests` alone. AC7 added for the process-count observation.

## 10. Reuse audit

The seam is `tools/unattended/run-unattended-gates.sh`, which already implements this mechanism for
one kit — the split, the per-suite `BUDGET_*` ceilings, the missing-budget failure, the derived total
and the liveness refusal — under an owner ruling recorded in `AGENTS.md`. This unit generalises the
SELF-TEST half of that file and leaves its `--checks` half in place, so the two cannot diverge on the
half that moves and nothing that depends on the half that stays is broken.
`tools/codebase-map/reuse_lookup.py` returned `.unattended.conf` [unattended] and
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as the affordance seams. The declared-value file
shape is `tools/run-gates/gate-profiles.txt`'s, which itself cites `tools/template-size-limits.txt`.
What rev-1 got wrong and the audit corrected: the seam's own suites are declared in that file's
`run_one` literals and nowhere machine-readable, which is the gap S1 fills rather than assumes away.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
