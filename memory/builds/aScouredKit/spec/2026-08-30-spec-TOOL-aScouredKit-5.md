# TOOL-aScouredKit-5 — drift-audit's conf parser matches the source its docstring claims to copy

**Status:** CLOSED · rev-2 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 |
| [2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-spec-audit.md) | spec-audit | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 TOOL-aScouredKit-30 TOOL-aScouredKit-31 TOOL-aScouredKit-32 |

<!-- /gen:spec-records -->

## 1. Goal

Align `tools/drift-audit/drift_report.py`'s conf parser with `tools/codebase-map/map_lib.py`'s, the
source its own docstring calls a deliberate copy, and make the equivalence gate that claims to
police the pair actually able to catch the divergences that exist.

## 2. Scope (IN)

- S1. The fixture in `tools/drift-audit/selftest.py` gains the two spellings that currently diverge:
  an `export FOO=bar` line and a value with a trailing inline comment. RED is confirmed and recorded
  BEFORE any parser edit — the fixture comes first and that ordering is the unit.
- S2. `tools/drift-audit/drift_report.py`'s parser gains the `removeprefix('export ')` rule and the
  ends-at-whitespace rule that `map_lib.py` has.
- S3. The docstring's provenance claim is corrected either way: it currently asserts the parser is a
  copy AND that the drift is gated, and both were false at the base sha.

## 3. Non-goals (OUT)

- Collapsing the two parsers into one. `drift_report.py` ships to adopters who hold no codebase-map,
  so it cannot import one; the duplication is deliberate and only its EQUIVALENCE is in scope.
- The five memory-tree Python conf readers. That is a wider and riskier population, reported as its
  own backlog row rather than half-fixed here.
- The BOM strip `drift_report.py` has and `map_lib.py` lacks. That is a real divergence in the SAFE
  direction and removing it would lose a Windows behaviour; it is documented, not deleted.

## 4. Design

The docstring at `tools/drift-audit/drift_report.py:78` says the parser is "a deliberate COPY of the
twenty lines in codebase-map's `map_lib.load_conf`" and that the drift "is gated by asserting this
parser against BASH sourcing the same file". Measured at the base sha, three things are true and the
docstring is compatible with none of them: the copy dropped `map_lib.py:192`'s `removeprefix('export ')`,
it dropped `:200`'s ends-at-whitespace rule, and the cited gate's four-spelling fixture covers
neither divergence. The gate exists precisely to catch parser divergence and has never observed one.

This is the charter's own rule — a new gate is not landed until its failing case has been observed —
applied to a gate that already landed. S1 is therefore not test-first as a style; it is the only way
to know the gate can red at all.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Fixture | `tools/drift-audit/selftest.py` | two spellings added to the equivalence arm |
| Parser | `tools/drift-audit/drift_report.py` | two rules added, docstring corrected |

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — a conf line with only `export ` and no key stays a non-match.
- observability — the selftest arm's own output.
- risks — the parser is read by every drift signal, so a regression is wide. Mitigated by S1: the
  fixture must be seen RED against the unfixed parser and GREEN after, which is a two-sided proof.
- testing + left-shift gates — `python tools/drift-audit/selftest.py`.
- migration / rollback — N/A. user docs — the docstring, corrected by S3.

## 6. Acceptance criteria

- **AC1** — When the fixture of S1 is staged against the UNFIXED parser,
  `python tools/drift-audit/selftest.py` FAILS on the bash-equivalence arm. Observed and recorded in
  §9 before S2 landed.
- **AC2** — When S2 has landed, `python tools/drift-audit/selftest.py` is green with that same
  fixture in place.
- **AC3** — When `tools/drift-audit/drift_report.py:78`'s docstring is read, every claim it makes
  about the parser's provenance and about what gates it is true of the code beneath it.
- **AC4** — When `python tools/drift-audit/drift_report.py` runs on this tree, no signal value moves
  BECAUSE OF THIS UNIT — no tracked conf here uses either spelling, so the parser fix must be inert
  on this repo. Stated per-unit rather than against the base sha, because `TOOL-aScouredKit-4`
  deliberately moves `shrink_only_lists_not_shrinking` in the same file and a base-sha comparison
  would make the two units' acceptance contradict.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · the full bar at the push
boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.
- rev-2 · 2026-08-30 · AC4 rescoped to this unit. The M2 cross-read found it disagreeing with
  `TOOL-aScouredKit-4`'s AC1: both units touch `tools/drift-audit/drift_report.py`, and -4 moves a
  signal value on purpose, so an against-the-base-sha assertion here made one spec set contradict
  itself. Fixed in this document because -4's criterion is the correct one.

## 10. Reuse audit

The seam is `tools/codebase-map/map_lib.py`'s `load_conf`, which this parser already declares itself
a copy of; this unit makes the claim true rather than introducing a mechanism. Importing it is
refused by §3 for a stated reason. The build's reuse probe is recorded in `TOOL-aScouredKit-1` §10.
