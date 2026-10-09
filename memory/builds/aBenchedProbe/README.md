---
slug: aBenchedProbe
node: a
opened: 2026-10-09
streams: tooling+deployer
roster: TOOL+DEPL
ids: DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2 DEPL-aBenchedProbe-3 DEPL-aBenchedProbe-4 TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2
authorized-by: prompt
---

# aBenchedProbe — the hook self-tests ship held, and the class cannot recur

## The problem this build exists to solve

The push-main descriptor declares its three hook self-tests `subject = "repo"`, so govkit emits them
that way and every adopter bar runs them, under `GATE_FULL=1` too. They test engine files an adopter
ships verbatim. NicoCares paid 815 s to 3500 s per bar for the pre-push self-test alone, with no
ceiling to say so. The owner's prose is the mandate, recorded under
[prompts/](prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1.md).

## Expected improvements

- Adopters hold all three hook self-tests unless `GATE_SELFTESTS=1`, after a normal govkit update.
- run-gates' held count names its predicate instead of claiming every self-test.
- `govkit selfcheck` reds a descriptor that ships a self-test on the adopter bar.
- The pre-push self-test carries its wall-clock ceiling into adopters.

## Detriments if this is not built

- Every adopter push keeps paying up to an hour for a test of code it never edits.
- The next kit self-test declared `repo` lands the same cost with nothing to stop it.
- A pre-push self-test that keeps slowing down stays unbounded and unnoticed in adopters.

## Build-level rules

- **Classification (M2)**: four units, MISSING at open, authored this run, one mechanism each.
- Both DEPL units write `govkit.py`; DEPL-2 and TOOL-1 both write the push-main descriptor. Those
  pairs are sequenced. TOOL-2 is disjoint from the rest.
- DEPL-2 is Tier-2: it changes what the deployer writes into an adopter's leg manifest.
- Out of scope, owned by the concurrent run aThriftyLanding: `.githooks/pre-push`, the stamp
  predicate, `GATE_REUSE` and the turnstile in run-gates, the unattended protocol, the charter's §1.
- One kit-version bump per touched kit, after the last unit.
- Units 5 and 6 are the closing review's promotions (M4); both write `govkit.py` and `selftest.py`, so 6 follows 5.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aBenchedProbe-1` | the three hook self-tests are declared `subject = "kit"`, in the descriptor and gov's manifest |
| 2 | `TOOL-aBenchedProbe-2` | run-gates' held-count summary names its predicate rather than "every self-test" |
| 3 | `DEPL-aBenchedProbe-1` | govkit selfcheck reds a descriptor self-test leg whose subject is not `kit` |
| 4 | `DEPL-aBenchedProbe-2` | a descriptor leg's `ceiling` travels into the adopter's manifest, and pre-push's declares one |
| 5 | `DEPL-aBenchedProbe-3` | 7j4's liveness reds bind only where a self-test population exists (review H1) |
| 6 | `DEPL-aBenchedProbe-4` | regression arms for the keep rule, 7j4 and the 7h ceiling clause (review minors) |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 4 unit(s) · node a · opened 2026-10-09 · streams tooling+deployer
ids DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2 DEPL-aBenchedProbe-3 DEPL-aBenchedProbe-4 TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBenchedProbe-1 — the three hook self-tests are declared `subject = "kit"`](spec/2026-10-09-spec-TOOL-aBenchedProbe-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aBenchedProbe-2 — run-gates' held-count summary names its predicate](spec/2026-10-09-spec-TOOL-aBenchedProbe-2.md) | 1 | 1 | CLOSED | rev-1 | 2026-10-09 |
| [DEPL-aBenchedProbe-1 — govkit selfcheck reds a descriptor self-test leg whose subject is not `kit`](spec/2026-10-09-spec-DEPL-aBenchedProbe-1.md) | 2 | 1 | CLOSED | rev-1 | 2026-10-09 |
| [DEPL-aBenchedProbe-2 — a descriptor leg's `ceiling` travels into the adopter's manifest](spec/2026-10-09-spec-DEPL-aBenchedProbe-2.md) | 3 | 2 | CLOSED | rev-1 | 2026-10-09 |
<!-- /gen:build-units -->

Records: 7 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2 TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aBenchedProbe-1`, `TOOL-aBenchedProbe-2` | yes |
| 2 | `DEPL-aBenchedProbe-1` | no |
| 3 | `DEPL-aBenchedProbe-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
