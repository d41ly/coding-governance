---
slug: dTieredTribunal
node: d
opened: 2026-08-25
streams: tooling
roster: TOOL
ids:
status: OPEN
---

# dTieredTribunal — one review harness for every review kind a build needs

## The problem this build exists to solve
`BUILD-METHOD.md` M4 forbids `tier2-review.js` on a spec — it reviews DIFFS, and a spec is not code —
so every spec audit is driven by a script authored from scratch in the session that needs it. That is
the MAJORITY kind: 82 of this corpus's 156 records are `spec-audit` against 73 `diff-review`.
A hand-written driver re-loses the harness's trust accounting — the integer verdict join, the
dead-lens and dead-skeptic counters, unverified-is-not-refuted, the synth-death hole — each a defect
that shipped once and survives only as a comment. The loss is measured: of three agent-spawning
pipelines in `tools/workflows/`, only `tier2-review.js` carries any of it, and the bar is green over
all three. It shows as ABSENCE, not a crash: a field a program emits appears in 77–88% of records,
one a document asks a human to remember in 5–27%.

## Expected improvements
- One hardened engine drives every review a build needs — spec audit, diff review, fold round,
  convergence loop — so a session configures a subject instead of authoring a driver.
- The trust accounting stops being re-derived per session, which is where the regressions come from.
- The majority review kind gets the mechanical enforcement the minority already has.

## Detriments if this is not built
- Every spec audit keeps starting from a blank file, and its failure mode is SILENT: a degraded run
  returns findings and reads as complete.
- M4's ban stays true of the harness as written, so the rule cannot be relaxed until the kit moves.
- The cost is paid per session and is invisible until a review is thrown away.

## Build-level rules
- **This session delivers RESEARCH ONLY.** No spec, no kit edit, no rule edit. The owner narrows the
  proposal set before anything is specced. Settled at kickoff, all three forks.
- **Scope is both halves**: the single review pass AND the round/convergence loop M4 and M8 describe.
- **`BUILD-METHOD.md` M4/M8 and `REVIEW-PROTOCOL.md` are in scope as PROPOSALS**, not as edits. Both
  sit in the kickoff manifest's `watch:` list, so a landed change re-audits the manifest.
- **Any design fits the caps the hook actually resolves.** They are file constants in
  `tools/hooks/agent-cap.js` and are deliberately not restated here.

## Parked decisions
- **`TOOL-aDeclaredBound-6` is OPEN and untouched here**: `tier2-review.js` describes its own find
  phase twice and the two disagree. A research pass records it; fixing it is a unit.
- **`TOOL-aBoundedVerdict-20` is OPEN and untouched here**: the aBoundedVerdict spec audit's unfolded
  residue. It is evidence for this build's problem statement, not work inside it.

<!-- roster:units -->

*No unit is specced yet. This build has run its research pass only; the roster fills when the
owner selects which of the record's twelve proposals become units.*

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-08-25 · streams tooling

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
