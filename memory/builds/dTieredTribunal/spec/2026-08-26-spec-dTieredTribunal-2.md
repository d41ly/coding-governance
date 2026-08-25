# TOOL-dTieredTribunal-2 — the fold writes text nobody reviews, and that class is not in the catalogue

**Status:** SPECCED · rev-1 · 2026-08-26 · node a · Tier-1 · base da9e4cd2 · order 1 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`python tools/memory-tree/gotchas.py --for-diff` is the recurring-bug-class checklist the build
method hands every reviewer, and it can only emit classes that exist as records under
`memory/gotchas/`. The highest-value class measured on a recent build is not one of them, so the
checklist cannot select it. Add the record.

## 2. Scope (IN)

- **S1** — a new record at `memory/gotchas/fold-text-is-unreviewed-surface.md`, carrying the front
  matter the existing records use and the sections the hygiene gate's record checks require.
- **S2** — the record's anchors are `memory/guides/BUILD-METHOD.md` and
  `tools/workflows/tier2-review.js`, both tracked paths, so the class selects on a diff that touches
  the fold rule or the harness that primes a fold round.
- **S3** — `python tools/memory-tree/gotchas.py --write` re-renders `memory/gotchas/INDEX.md` in the
  same commit as the record.
- **S4** — the new inventory key is claimed by a map dossier in the same commit, so the codebase-map
  coverage gate stays green.
- **S5** — the record's evidence cites a TRACKED file. The measurement is at
  `memory/builds/dFramedEntrypoint/reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md`,
  which states the by-kind split of that round's surviving findings.

## 3. Non-goals (OUT)

- **Any change to the fold RULE.** The build method's fold-and-stop text stays exactly as written.
  Editing it is a governance-carrier change this build's rules withhold.
- **Extending the harness's fold priming.** The research names two fold instructions that reach no
  prompt today. Adding them is a prompt change to `tools/workflows/tier2-review.js` and belongs
  wherever a kind profile lands, which is the parked proposal.
- **A new gate.** The existing record checks over `memory/gotchas/` already grade the file, and the
  index-freshness check already grades the render.
- **Retrofitting the class onto past review records.**

## 4. Design

The class, stated once so the record can be written against it. A review round finds defects. The
fixes are FOLDED into the spec or the code. That fold is fresh text that nobody has reviewed, and on
the one build that ran the loop to completion it was where most of the next round's findings came
from. The tracked round-2 record splits its 62 surviving findings by kind as 25 the fold created, 17
the fold misreading its own finding, and 20 that round 1 missed. So the fold produced more findings
than the review it was answering had missed.

The consequence for a reader is the useful half. A fold is not bookkeeping and a round that treats it
as bookkeeping will pay for it in the next round. The two mitigations the same record names are
concrete: verify a did-not-land claim by reading the body at HEAD rather than the revision log, and
fold a DELETION rather than appending a negation beside the text it contradicts.

Both mitigations are recorded in the record and neither is imposed as a rule here, because the
record is a checklist entry and not a carrier of obligations.

## 5. Acceptance criteria

- **AC1** — When `ls memory/gotchas/ | grep -i fold` runs, it returns the new record, where today it
  exits non-zero with no output.
- **AC2** — When `python tools/memory-tree/gotchas.py --check` runs, it exits zero, which covers both
  the record's own shape checks and `INDEX.md` freshness.
- **AC3** — When `python tools/memory-tree/gotchas.py --for-paths memory/guides/BUILD-METHOD.md`
  runs, the new class name appears in its stdout.
- **AC4** — When `python tools/codebase-map/reuse_lookup.py` is used to report coverage, the new
  `gotcha-classes` key is claimed by a dossier and does not sit unclaimed in
  `memory/map/baseline.toml`.
- **AC5** — When the full bar runs, the `memory-tree hygiene` leg and the codebase-map coverage leg
  are both green with the record staged.

## 6. Gates

`memory-tree hygiene` · the codebase-map coverage and freshness legs · `gotchas index freshness`
where the leg manifest names it separately. This unit adds no leg.

## 7. Open questions

none.

## 8. Revision log

- rev-1 · 2026-08-26 · initial draft, authored by the unattended run under the standing mandate.

## 9. Reuse audit

The seam is the memory-tree kit's own gotchas catalogue, `memory/gotchas/`, read by
`tools/memory-tree/gotchas.py`. Nothing is built: a record is authored into an existing catalogue
and an existing generator re-renders its index. `tools/codebase-map/reuse_lookup.py` returned
`gotcha-classes` inventory keys among its candidates for the review-harness phrase, which is the
same catalogue.

Recall terms used with `tools/memory-recall/query.py`: `tier2-review harness lens skeptic verdict
spec-audit diff-review blockers convergence trust counters unverified fan-out`. The query surfaced no
existing record of the fold class, which agrees with the direct probe over the catalogue directory.
