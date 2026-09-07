# TOOL-aQuenchedHarness-6 — the dominant suites rebuilt onto the harness, arm inventory preserved

**Status:** CLOSED · rev-7 · 2026-09-07 · node a · Tier-2 · base faaea5f5 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-07-build-TOOL-aQuenchedHarness-6-acceptance-ledger-port-and-survey.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-6-acceptance-ledger-port-and-survey.md) | journal | — |
| [2026-09-07-build-TOOL-aQuenchedHarness-6-arm-inventory-check-line-length.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-6-arm-inventory-check-line-length.md) | journal | — |
| [2026-09-07-build-TOOL-aQuenchedHarness-6-portability-survey.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-6-portability-survey.md) | research | — |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-7 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 |

<!-- /gen:spec-records -->

## 1. Goal

Rebuild the self-test suites that hold the cost onto `tools/lib/lib-selftest.sh`, so the on-demand
sweep runs in minutes rather than hours. The rule for choosing which, the rule for proving nothing
was lost, and the FLOOR a port must clear are all fixed here; the suite names are not, because they
come from measurement.

## 2. Scope (IN)

- **S1** — the population is the DECLARED one: every row of `tools/run-gates/selftest-budgets.txt`,
  which `TOOL-aQuenchedHarness-4` S1 establishes. Not the held manifest legs, and not whatever
  happens to have a row in the local ledger — the audit measured this worktree's ledger backing 7 of
  49 held legs against the primary tree's 45, so a selection keyed on it is keyed on where the build
  happened to sit.
- **S2** — SELECTION REFUSES on missing evidence. Before any port, every row in the population must
  carry a reading; the tool names the unbacked rows and stops, and names
  `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` plus a direct invocation of the non-leg suites
  as the step that produces them. A denominator nobody measured is not a majority.
- **S3** — select in descending recorded seconds until the selected set holds a DECLARED majority
  share of the population's summed seconds. The share is declared in the budgets file's header with
  its reading; the SET is computed, so it moves when the readings move.
- **S3a** — THE RANKING NEEDS COMPARABLE READINGS. S3 sorts by recorded seconds, and after
  `TOOL-aQuenchedHarness-4` F2 those readings come from two sources under two conditions: `gate-run`
  leg files for held legs, and direct timed invocations for the six suites carrying no manifest row.
  Sorting them together ranks the conditions as much as the suites. Either every row is re-read under
  ONE stated condition before the ranking, or the ranking is done on the SPAWN COUNT, which
  `TOOL-aQuenchedHarness-5` S6 produces and which the recorded gotcha names as the claim to write
  down. The ranking prints the condition each reading came from, and REDS when a row's condition is
  unstated.
- **S4** — extract each selected suite's ARM INVENTORY before touching it — the staged break, the
  subject invoked, the expected verdict, one row per arm — into a tracked artifact under
  `memory/builds/aQuenchedHarness/build/`.
- **S5** — port, preserving every row. Re-extract afterwards and DIFF against the pre-port artifact.
  A non-empty diff is a defect in the port, not a judgement call.
- **S6** — THE PORT MUST CLEAR A FLOOR. A declared minimum improvement factor per ported suite,
  stated in the budgets file header with its reading, measured as recorded seconds before against
  after in the same conditions. A port that does not clear it is not landed as a port: it is either
  redone or recorded as a candidate that lost, per `TOOL-aQuenchedHarness-5` §8 F1.
- **S7** — record per ported suite: seconds, spawn count and arm count, before and after.
- **S8** — lower each ported suite's budget row to its new reading, in the same commit as the port.
- **S9** — every suite NOT ported is NAMED in the wrap-up with its recorded cost.

## 3. Non-goals (OUT)

- Not porting every suite. S3's majority-share rule bounds it and S9 names the remainder. A full port
  is a follow-up a later build may take with these measurements in hand.
- Not changing any checker under test. Only the suites move.
- Not adding arms. A port that also improves coverage cannot be diffed against its own inventory, and
  S5's diff is the whole safety property. New arms are a separate unit.
- Not removing arms, even ones that look redundant. Same reason.

## 4. Design

### The inventory extractor

Rev-3 specced a reader that parses a suite's arm-shaped CALL SITES. Surveying the corpus refuted it
before a line was written: the suites use at least four unrelated idioms — `arm "label" rc want ...`,
`ok`/`nope`, `check(...)`, `say_ok`/`say_fail` — and several use none this survey could name. A parser
for all of them is a large investment in a safety property, and it would grade what the source SAYS
rather than what the suite RAN.

**The inventory comes from the suite's OWN OUTPUT instead.** Run it, keep the per-arm verdict lines,
strip the verdict token and any timing, sort the remaining labels. That set is the arm inventory, and
comparing it across a port is the safety property.

It is better on every axis that matters. UNIVERSAL — any suite printing one line per arm is covered,
whatever its internal idiom. STRONGER — it compares the arms that actually EXECUTED, so an arm lost
to a mis-scoped `if` is caught where a source parse would still see its call site. And FREE — S7
already requires running the suite on both sides for the seconds and the spawn count, so the
inventory rides along.

The escape survives unchanged in shape: a suite whose output carries no per-arm line is reported
UNEXTRACTABLE and is not ported in this unit, because porting a suite whose inventory cannot be
compared is exactly the unfalsifiable claim this design exists to prevent.

### Why a floor, and not just a budget

Rev-1 paired "lower the budget to the new reading" with "assert the suite is inside its budget",
which is a criterion that cannot fail: a 2% improvement satisfies it exactly as a 20x one does. This
unit owns the build's stated target, so its acceptance has to carry a number that can fail. S6 is
that number.

### Ordering

One suite per pass, committed per pass, with the inventory diff and the before/after readings in the
commit message. A batch port would make a failed diff ambiguous across suites.

### Inventory

- `tools/lib/extract-arms.sh` — the inventory extractor: runs a suite, normalises its per-arm
  verdict lines, emits the sorted label set. Named against the lexicon before it was written.
- `memory/builds/aQuenchedHarness/build/<date>-build-TOOL-aQuenchedHarness-6-arm-inventory-<suite>.md`
  — one tracked artifact per ported suite, holding both inventories, the diff and the readings.

### Files touched (estimate)

`tools/lib/extract-arms.sh` (new) · the selected `*.test.sh` files ·
`tools/run-gates/selftest-budgets.txt` · one build record per suite.

### Alternatives rejected

Porting by hand and asserting equivalence in prose was rejected: this repo's own record shows a
derived equivalence claim wrong by 2.6x and unnoticed because nobody could falsify it
(`tools/unattended/run-unattended-gates.sh`, the `TOOL-dNarrowedAnchor-1` note). A diffable artifact
is the cheapest thing that makes the claim falsifiable. The METHOD to copy is the one landed in this
build's own base at `274aa39b` — one pass over history into a cache, byte-identical summary, spawn
count as the claim — which took `check-pass-order.sh` from 10184 s to 510 s and is the larger of the
two prior instances this build cites.

## 5. Production-readiness checklist

- security — N/A: no checker changes, no new execution path.
- perf / scale — the unit's whole subject; measured per suite by S7 and bounded below by S6.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — UNEXTRACTABLE is a named state and is reported. An unbacked
  population is a refusal (S2), not a smaller denominator.
- observability — the per-suite before/after artifact is the record.
- risks — the real hazard is a port that silently loses an arm, since a suite with fewer arms is
  faster AND greener. S5's diff is the guard and it reads the suite rather than the port's own claim.
  The second hazard is a port that clears every criterion while changing nothing; S6 is that guard.
- testing + left-shift gates — each ported suite IS its own test; the extractor gets arms of its own,
  including a suite whose arms it cannot read.
- migration / rollback — each port is one commit and reverts cleanly; the budgets move with it.
- user docs — none owed: the suites are developer surface, and the harness header covers how to write
  a new one.

## 6. Acceptance criteria

- **AC1** — When a suite is ported, `bash tools/lib/extract-arms.sh <suite>` produces an inventory
  identical to the one extracted before the port, and the diff is recorded in that suite's artifact.
- **AC2** — When an arm is deliberately deleted from a ported suite, the diff from
  `bash tools/lib/extract-arms.sh` is non-empty and the port is refused — the guard's own failing
  case, observed before landing.
- **AC3** — When each ported suite is measured after the port, its recorded seconds are at most its
  before-reading divided by the declared minimum factor in
  `tools/run-gates/selftest-budgets.txt`'s header. A port that improves by less than the factor FAILS
  this criterion.
- **AC4** — When the selection tool runs against a `tools/run-gates/selftest-budgets.txt` population
  where any row lacks a reading, it REDS naming the unbacked rows and computes no share at all.
- **AC5** — When the build closes, the selected set satisfies the majority share declared in
  `tools/run-gates/selftest-budgets.txt`'s header, computed over the declared population rather than
  over the local ledger, and shown in the wrap-up. **NOT MET, and recorded as not met.** The
  portability survey — `memory/builds/aQuenchedHarness/build/2026-09-07-build-TOOL-aQuenchedHarness-6-portability-survey.md`
  — read the twelve costliest rows and found that NONE of them is portable under this unit's own
  rules without changing them: three are python suites driving module internals with no CLI
  entrypoint, two print no recoverable inventory, four need arms to share state a per-arm copy
  destroys, and the rest need assertion verbs the harness does not have. The arithmetic, once
  every row carried a reading: the population is 36031 s, the declared 50% is carried by the TOP
  FIVE suites, and the one suite this unit ported carries 208 s of it — **0.6%**. The share is NOT lowered to fit: S6 exists
  because rev-1 paired a criterion with a threshold it could not fail, and moving a threshold to
  match a result is that same defect with the sign flipped. S9's remainder is the survey record and
  it names every one with its recorded cost.
- **AC7** — When the port ranking runs over `tools/run-gates/selftest-budgets.txt`, every row prints
  the condition its reading was taken under, and a row whose condition is unstated REDS rather than
  being sorted against rows measured differently.
- **AC6** — When a suite's arms cannot be extracted, `bash tools/lib/extract-arms.sh` reports
  `UNEXTRACTABLE` naming it, and that suite appears in the unported remainder rather than being
  silently skipped.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `bash tools/run-gates/run-selftests.sh` for the ported suites ·
the `lexicon naming predicates` leg, which guards on `tools/` and grades the new extractor ·
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at the Definition of Done · `memory hygiene`,
which grades the per-suite build records this unit writes.

## 8. Open questions

- **F1 — what majority share and what minimum factor do the headers declare?** ANSWERED in the build,
  2026-09-07, and the numbers are in `tools/run-gates/selftest-budgets.txt`'s header with the reading
  beside each: **share 0.50**, because that is what "majority" means and a share fitted to whatever
  got ported is the criterion-that-cannot-fail rev-1 already had to delete; and **factor 3.0x**, read
  off the first port at 4.03x with 2.35x and 1.37x also measured, so the declared number reds against
  two conditions this same suite was observed in.
- **F2 — what happens to a suite whose arms are unextractable?** RESOLVED (agent, 2026-09-06,
  delegated): it is NOT ported in this unit and is named in the remainder. Porting it would mean
  hand-asserting equivalence, which §4's rejected alternative refuses on this repo's own evidence.
- **F3 — does the unattended `gate selftest` at a recorded 3565 s fall in scope?** RESOLVED (agent,
  2026-09-06, delegated): yes, and it could not have under rev-1. It is in no manifest, so a
  held-legs population could never select it and S9 could never name it; the declared population
  `TOOL-aQuenchedHarness-4` S1 introduces carries it, and on recorded seconds it is the largest thing
  in the set.

## 9. Revision log

- rev-7 · 2026-09-07 · CLOSED with AC5 recorded as NOT MET and the arithmetic beside it, rather than met by a smaller share. What landed: the inventory extractor and its three named refusals, the declared share and factor, `--rank` and its condition grammar, ONE port at 4.03x with its 18 arms diffed identical, and the runner's own thirteen arms. What did not: the other eleven candidate suites, none of them portable under this unit's rules without changing them, each named with its recorded cost in the survey record. Three defects in the unit's OWN product were found and fixed along the way, two of them by reading rather than running, and the third by the extractor's own arms on their first execution.

- rev-1 · 2026-09-06 · initial draft.
- rev-6 · 2026-09-07 · AC5 is recorded as NOT MET rather than met by a smaller number, on the evidence
  of the portability survey. Two defects in this unit's OWN product were found and fixed in the same
  pass, both by the survey rather than by a run: `build_fixture` did not reset the batch, so a suite
  with two base fixtures silently re-ran the first batch's arms against the second batch's snapshot;
  and `extract-arms.sh` guarded only the EMPTY inventory, so a suite printing 14 readable lines
  against 289 executed assertions came back as a confident 14-arm inventory at exit 0 — the exact
  vacuity that file's header claimed to prevent. The extractor now asserts its own coverage against
  the suite's reported total and has three named refusals, each armed by
  `tools/lib/extract-arms.test.sh`, whose own first run found a third: the harness's summary line
  satisfies the arm grammar, so a red suite counted its verdict as an extra arm.
- rev-5 · 2026-09-07 · the first port landed and it DIVERGED, so this records the divergence rather
  than hiding it. §3 says "not changing any checker under test. Only the suites move" — and the port
  changed `tools/lib/lib-selftest.sh`, which is a sibling unit's product rather than a checker under
  test. It had to: the first port measured 62 s against the 32 s of the suite it replaced, because the
  harness spent eleven processes per arm on bookkeeping around a subject costing one, and its pool's
  `wait -n || wait` reap collapsed to a barrier per arm. A port cannot clear a factor against a
  harness that is itself the cost, so the harness was rewritten to three processes per arm and the
  capability probed once. The same pass corrected `run-selftests.sh`, which divided the declared width
  by an outer pool of 4 that does not exist. §3's fence still holds where it was written — the GATE
  under a ported suite is untouched, and the check-line-length gate has not moved a byte.
  F1's two numbers are now ANSWERED rather than deferred, above.
- rev-4 · 2026-09-07 · the extractor changed shape BEFORE any code, per M2's "to diverge, change the
  spec first". A survey of the corpus found at least four unrelated arm idioms and several suites
  using none of them, so rev-3's source parser was a large investment that would still grade what the
  source says rather than what ran. The inventory now comes from the suite's own OUTPUT — universal,
  stronger, and free, because S7 already runs the suite on both sides.
- rev-3 · 2026-09-06 · folded spec-audit round 2. M5: S3a adds the comparability rule the ranking
  needed — after unit 4 F2 the readings come from two sources under two conditions, and sorting them
  together ranks the conditions; the ranking now prints each row's condition and reds on an unstated
  one. M3: §4 names the larger and closer prior art, `274aa39b`, as the method to copy.
- rev-2 · 2026-09-06 · folded spec-audit round 1. B5: the population is the DECLARED one rather than
  the local ledger's rows — this worktree backs 7 of 49 held legs against the primary's 45, so the
  majority share was computable against wherever the build sat; S2 adds the refusal on missing
  evidence and F3 records that the largest suite in the tree was unreachable under rev-1's
  population. H6: S6 and AC3 add a declared minimum improvement FACTOR, because rev-1's
  lower-the-budget-then-assert-inside-it pair could not fail. M1: the extractor is `extract_arms`,
  checked against the lexicon, and §7 names the lexicon leg.

## 10. Reuse audit

The seam this unit extends is `tools/lib/lib-selftest.sh`, authored by `TOOL-aQuenchedHarness-5` in
this same build, together with the declared population `TOOL-aQuenchedHarness-4` S1 establishes, and
each selected suite's existing arm set, which is preserved rather than rewritten.
`tools/codebase-map/reuse_lookup.py` returned `run` and `check` as the high-fan-in stems over the
thirteen existing `selftest.py` modules, confirming that the arm-running pattern is duplicated per
suite and has no shared owner today. The one prior instance of this exact work in this tree — cutting
a suite's spawn count from 469 to 220 per invocation — is recorded in
`tools/unattended/run-unattended-gates.sh`'s header and was read before writing; its lesson, that a
DERIVED equivalence claim went unfalsified and was wrong by 2.6x, is why S5 exists, and the audit
supplied the second half of that lesson, which is why S6 exists.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
