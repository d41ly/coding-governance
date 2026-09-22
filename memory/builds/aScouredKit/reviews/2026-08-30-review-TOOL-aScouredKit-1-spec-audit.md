# aScouredKit — spec audit of the whole unit set

**Serves:** spec-audit TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 TOOL-aScouredKit-30 TOOL-aScouredKit-31 TOOL-aScouredKit-32

## Verdict: CLEAN WITH FIXES

*Node `a`, 2026-08-30. Seventeen specs, all authored by this run and therefore unreviewed by
definition. This is the M4 pass, and it is a SELF-REVIEW rather than a multi-agent audit — §8's tier
rule gives Tier-1 units gates plus one focused self-review and forbids a multi-agent one, and every
unit here is Tier 1 except `TOOL-aScouredKit-11` and `-13`. Recorded plainly rather than dressed up
as something heavier: what follows is what a cross-read found, including where it was wrong.*

## What was actually run

M2's four-axis cross-read over the set — **scope** (nothing one spec puts IN is OUT in another),
**interface** (a name, path or key spelled twice is spelled identically), **ordering** (no unit
depends on one sequenced after it), **acceptance** (no two criteria contradict) — performed once
before the first code pass and re-performed after each promotion round added units.

## Findings, and every one of them was a real disagreement

| # | Axis | Where | What was wrong, and what was done |
|---|---|---|---|
| 1 | acceptance | `TOOL-aScouredKit-5` §6 AC4 | Asserted no signal value moves against the BASE sha, while `-4` moves `shrink_only_lists_not_shrinking` on purpose in the same file. Two specs, one tree, contradictory criteria. Fixed in `-5` at rev-2, because `-4`'s criterion is the correct one. |
| 2 | scope | `TOOL-aScouredKit-4` §2 S1 | Restated the wave-1 report's proposed `shrunk_by < 0` after the code deliberately did something else. The code was right; the spec was the half left standing. rev-2. |
| 3 | scope | `TOOL-aScouredKit-6` §2 S3 | Claimed a `carried_population` hoist that was never built, because the measurement it rested on did not reproduce. rev-3, with the re-measurement recorded. |
| 4 | scope | `TOOL-aScouredKit-15` §2, §6 | Described a persistence mechanism `-30` withdrew. rev-2 restates S1, S2 and AC2 as what shipped. |

Four disagreements across seventeen specs, all found by the same axis-by-axis read, all fixed in
exactly one document each with a rev bump and a §9 line, per M2.

## What this pass did NOT do, said rather than implied

- **No multi-agent spec audit.** §8 forbids one at Tier 1 and fifteen of these units are Tier 1. The
  two Tier-2 units, `-11` and `-13`, were instead covered by the closing diff review at three rounds,
  which read their code rather than their prose — a different question, and the weaker one for a
  DESIGN. Stated as a gap rather than counted as coverage.
- **No sub-spec cross-read**, because no unit here has sub-specs.
- **It did not catch the defects the closing review did.** Every blocker this build produced was
  found by reading CODE, not specs: the receipt-ownership wedge, the bare `xargs`, the un-pathed hole
  probe, the vacuous arm. A spec audit grades what a document SAYS, and each of those specs said
  something true about a mechanism that was wrong. That is the honest limit of this pass and it is
  the argument for the diff review that follows it, not against it.

## The promotion, and why the set grew mid-build

`-30`, `-31` and `-32` are PROMOTED units. The closing review's blocker counts ran 4 → 3 → 4, so the
convergence predicate reported NON-CONVERGENT and the loop stopped by rule rather than by judgement.
Every blocker still standing became a unit, specced at its tier and built — which is what makes
promotion terminate instead of re-entering the loop. No round 4 was run, deliberately.
