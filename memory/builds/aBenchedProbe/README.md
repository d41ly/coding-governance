---
slug: aBenchedProbe
node: a
opened: 2026-10-09
streams: tooling+deployer
status: INPROGRESS
roster: TOOL+DEPL
ids: DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2 TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2
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

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aBenchedProbe-1` | the three hook self-tests are declared `subject = "kit"`, in the descriptor and gov's manifest |
| 2 | `TOOL-aBenchedProbe-2` | run-gates' held-count summary names its predicate rather than "every self-test" |
| 3 | `DEPL-aBenchedProbe-1` | govkit selfcheck reds a descriptor self-test leg whose subject is not `kit` |
| 4 | `DEPL-aBenchedProbe-2` | a descriptor leg's `ceiling` travels into the adopter's manifest, and pre-push's declares one |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 0 unit(s) · node a · opened 2026-10-09 · streams tooling+deployer
ids DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2 TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 3 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
