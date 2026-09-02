# TOOL-dRetiredFork-6 — the drift-audit note is DERIVED from its counters

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |

<!-- /gen:spec-records -->

## 1. Goal

Take the derived-note contract inCMS carries in both drift-audit harnesses. gov's `note` is a
hand-written ternary; inCMS's is re-derived from the counters the harness already computed. The two
are mechanically incompatible: a gate that re-derives the expected sentence CANNOT be satisfied by a
hand-written one. One un-taken gov design decision is generating two registry rows at that adopter,
which is the argument for taking it rather than a preference about wording.

## 2. Scope (IN)

- **S1** — Replace the hand-written ternary in `tools/workflows/drift-audit-code.js` with
  `livenessOf` and `livenessNote` derived from the run's own counters.
- **S2** — The same replacement in `tools/workflows/drift-audit-state.js`.
- **S3** — A DEAD PROBE assertion: a note derived from counters that cannot move prints DEAD PROBE
  rather than a reassuring zero, which is the property `AGENTS.md` §7 requires of every signal.
- **S4** — Arms proving the derived sentence for each of the three counter states — moved, did not
  move, could not run — with the third observed RED before the arm is wired.
- **S5** — Bump `KIT_DRIFT_AUDIT_VERSION`, both harness `meta.version` fields and every
  `gov:kit drift-audit@` marker, which `tools/check-kit-versions.sh` pairs in four places.

## 3. Non-goals (OUT)

- The `drift_report.py` engine. Only the two harnesses carry the ternary, and the engine's own
  liveness assertions already conform.
- Any new drift signal. `TOOL-dScaffoldedMirror-7` owns that surface.

## 4. Design

### Data model

`livenessOf(counters)` returns one of three states rather than a boolean, because "did not move" and
"could not run" are the two the ternary conflates and the conflation is the defect. `livenessNote`
renders exactly one sentence per state, so a consumer gate can re-derive it and byte-compare.

### Migration

Both harnesses ship to adopters. inCMS already holds the derived form and its two registry rows
retire on the pull; NicoCares holds gov's ternary plus its own cap edit, so its rows converge on
this change and on `TOOL-dRetiredFork-14` together.

### Alternatives rejected

Keeping the ternary and relaxing the consumer gate to a substring match. That makes the gate
satisfiable by prose, which is the class `AGENTS.md` §7 names first: a gate satisfied by its own
comment text.

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path.
- perf / scale — the counters already exist; deriving a sentence from them is free.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the "could not run" state is the whole point and must render
  DEAD PROBE, never an empty note and never a zero.
- observability — this unit IS the observability fix.
- risks — a consumer that byte-compares the note breaks if the sentence changes later. Accepted and
  stated: the sentence becomes a contract, and changing it is a version bump like any other.
- testing + left-shift gates — S4's three arms; the third is the one that has never been observed.
- migration / rollback — additive within one function; reverting restores the ternary.
- user docs — `tools/drift-audit/README.md` gains the three states and their sentences.

## 6. Acceptance criteria

- **AC1** — When a counter moved, `node tools/workflows/drift-audit-code.js` emits the derived
  sentence and a consumer re-deriving it byte-matches.
- **AC2** — When nothing moved, the note says so and is distinguishable from AC3's output. Observed via `node tools/workflows/drift-audit-code.js`.
- **AC3** — When the probe could not run, the note reads DEAD PROBE, and this arm is observed RED
  against the pre-change ternary, which emitted a zero-shaped note instead. Observed via `node tools/workflows/drift-audit-state.js`.
- **AC4** — `node tools/workflows/check-workflow-syntax.js` exits `0` for both harnesses.
- **AC5** — After the bump, `bash tools/check-kit-versions.sh` exits `0`.

## 7. Gates

`workflow script syntax` · `drift-audit selftest` · `kit version markers` · `review-join ban (no ref-keyed join)` · `verifier fan-out`.

## 8. Open questions

- **F1 — does the note's sentence become a declared contract, or stay incidental?** If a consumer
  gate byte-compares it, it is a contract whether declared or not. Recommendation: declare it in the
  kit README so a later editor knows the cost, and let the version bump carry it.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, from the inCMS `KIT_DRIFT_AUDIT_HARNESS_DELTA` rows on
  `drift-audit-code.js` and `drift-audit-state.js`.

## 10. Reuse audit

No existing seam fits for the note derivation itself; `reuse_lookup.py` reports no fan-in-3 helper
for liveness rendering, and the closest prior art is `drift_report.py`'s own per-signal liveness
assertion, which this unit copies in SHAPE rather than in code — the two run in different languages
and the kit ships no shared runtime, so a common helper is not available by construction.

Recall terms used: `drift-audit`, `liveness`, `DEAD PROBE`, `harness`, `note`, `ternary`, `counters`,
`gateable`, `signal`, `derive`, `adopter`, `divergence`.
