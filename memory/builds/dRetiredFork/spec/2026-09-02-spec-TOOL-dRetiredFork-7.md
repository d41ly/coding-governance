# TOOL-dRetiredFork-7 — the review join gains the dead-agent-wave arity arm

**Status:** CLOSED · rev-3 · 2026-09-03 · node d · Tier-2 · base b0108f13 · streams tooling · order 1 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-build-TOOL-dRetiredFork-7-1-acceptance-ledger.md](../build/2026-09-03-build-TOOL-dRetiredFork-7-1-acceptance-ledger.md) | journal | — |
| [2026-09-03-prompt-TOOL-dRetiredFork-7-1-build-brief.md](../prompts/2026-09-03-prompt-TOOL-dRetiredFork-7-1-build-brief.md) | journal | — |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-03-review-TOOL-dRetiredFork-1-21-and-depl-1-9-closing-diff.md](../reviews/2026-09-03-review-TOOL-dRetiredFork-1-21-and-depl-1-9-closing-diff.md) | diff-review | DEPL-dRetiredFork-1 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

Absorb ARM 2 from inCMS's `scripts/workflows/check-review-join.sh`, which its own registry row
declares as a population repath and which is in fact `+117` residual code lines carrying an entire
second arm plus `isfalsy` and `falsydrop` helpers, armed by a 550-line suite gov has never reviewed.
The arm catches a review harness that dispatches a wave of agents which all return falsy, so the
join silently drops every finding and the run reports a clean bill. Until this lands, that suite is
550 lines of coverage gov will never see and inCMS re-merges on every pull.

## 2. Scope (IN)

- **S1** — Absorb ARM 2 and its two helpers into `tools/workflows/check-review-join.sh`, keeping
  gov's message shapes and gov's exit-code contract.
- **S2** — Absorb the arms that exercise it from inCMS's `check-review-join.test.sh`, reduced to the
  subset that is not keyed on inCMS record ids. An arm keyed on a foreign corpus reds on absence
  rather than on behaviour and must not ship.
- **S3** — A liveness assertion on ARM 2's own population, because an arm that scans nothing reports
  the same zero as an arm that scanned everything and found nothing.
- **S4** — Bump the review-harness version and its `gov:kit` markers.

## 3. Non-goals (OUT)

- The population and hook-path halves of that same inCMS row. Those are `TOOL-dRetiredFork-10`, and
  splitting them is deliberate: one is a behavioural absorption and the other is a path derivation,
  and a closing diff cannot attribute a finding across both.
- Re-keying inCMS's remaining suite. What does not travel stays theirs, and `DEPL-dRetiredFork-7`
  records the residue honestly rather than implying it converged.

## 4. Design

### Inventory

Three things travel: the arm, `isfalsy`, `falsydrop`. Everything else in the `+117` is either the
population filter (unit 10) or inCMS-corpus-keyed test scaffolding (out of scope).

### Migration

gov gains an arm it does not have, so gov's own bar may go RED on landing if gov's harnesses trip
it. That is a finding, not a regression: run the candidate predicate over the tree BEFORE wiring,
print hits and near-misses, and fix whatever it legitimately catches in its own commit.

### Alternatives rejected

Leaving it at the adopter and citing the registry row. That is the status quo, and its cost is
measured: 550 lines of suite and 117 of arm that re-merge every release, for a defect class gov is
equally exposed to.

## 5. Production-readiness checklist

- security — N/A directly, though the arm protects the integrity of a review that gates merges.
- perf / scale — one additional pass over an already-enumerated population.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an empty population REFUSES; that is S3.
- observability — the arm names the wave and the count it found falsy.
- risks — landing an arm gov's own harnesses trip. Mitigated by the pre-wiring predicate run, which
  is a build-level rule here and not optional.
- testing + left-shift gates — S2's arms, plus the existing `check-review-join.test.sh`.
- migration / rollback — additive arm; reverting removes it.
- user docs — the arm and what it does NOT check, in the gate's own header AND in its runtime
  output on BOTH paths. `tools/workflows/README.md` does not exist, and the kit's
  adopter-facing doc is `memory/guides/REVIEW-PROTOCOL.md`, which M11 names a governance
  carrier — so extending it trips M3 veto 2 and is an owner turn, not this unit's. The scope
  lines print on the clean path too, which is stronger than a file nobody opens.

## 6. Acceptance criteria

- **AC1** — When a harness dispatches a wave whose agents all return falsy,
  `bash tools/workflows/check-review-join.sh` exits non-zero naming the wave; the pre-change script
  exited `0` on the same fixture.
- **AC2** — When a wave returns a mix of falsy and real findings, the script exits `0`.
- **AC3** — When ARM 2's population is empty, the script REFUSES rather than passing. Observed via `bash tools/workflows/check-review-join.sh`.
- **AC4** — When run over gov's own tree, the script's hits and near-misses were printed and
  reviewed before the arm was wired, and the record names what it caught. Printed by `bash tools/workflows/check-review-join.sh` before wiring.
- **AC5** — After the bump, `bash tools/check-kit-versions.sh` exits `0` AND, with the review-harness
  marker reverted to its pre-bump value, exits non-zero naming that carrier. A bare post-bump green
  cannot fail: the gate is already green before the unit starts.

## 7. Gates

`review-join ban (no ref-keyed join)` · `review-join self-test` · `workflow script syntax` · `kit version markers` · `testsuite counts (every bar self-test prints one)`.

## 8. Open questions

- **F1 — does ARM 2 ride the same exit code as ARM 1, or its own?** Sharing keeps the contract
  simple; separating lets a consumer distinguish the two failures. Recommendation: share, because
  the script's contract today is one exit code and widening it is a change every adopter inherits.
- **F2 — what does gov's own tree do under this arm?** UNRESOLVED until the predicate is run. This
  is a `FACT-QUESTION` decided by that run, and the liveness assertion in S3 is what lets it produce
  a negative.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, from the inCMS `check-review-join.sh` row classified
  `genuine-fork` and its dishonest registry declaration.
- rev-2 · 2026-09-02 · folded spec-audit round 1, finding M5. AC5 asserted a gate that is green before the unit begins, so
  it could not fail; it now pairs the green with an observed RED against a reverted marker.


- rev-3 · 2026-09-03 · built. THREE corrections the build measured. (a) §5's user-docs row named
  `tools/workflows/README.md`, which does not exist; the doc lives in the gate header and its own
  output, and the kit's real adopter doc is a governance carrier this mandate may not edit.
  (b) S3's liveness refusal, as first written, fired whenever arm 2 judged nothing and broke a
  legitimate existing arm over a fixture tree with no harness at all; it is tightened to "files
  dispatch agents AND none was judged", which is the fact that actually means the arm was retired.
  (c) AC5's required RED could not be produced: the `gov:kit review-harness@` marker was paired by
  NOTHING, so reverting it left the gate green. `check-kit-versions.sh` now pairs both ids on that
  file, which is what made AC5 observable.

## 10. Reuse audit

The seam is `tools/workflows/check-review-join.sh` itself, which this unit extends with a second arm
rather than adding a script beside it — `reuse_lookup.py` reports the review-join predicate as the
single carrier of this class, and `tools/hooks/agent-cap.js` already owns the ref-keyed-join ban that
ARM 2 complements rather than duplicates.

Recall terms used: `review-join`, `verdict`, `ref-keyed`, `fan-out`, `skeptic`, `falsy`, `wave`,
`arity`, `agent-cap`, `harness`, `liveness`, `adopter`, `absorb`.
