---
slug: aWeighedCanon
node: a
opened: 2026-09-04
status: OPEN
streams: tooling
roster: TOOL
ids: TOOL-aWeighedCanon-1 TOOL-aWeighedCanon-2
---

# aWeighedCanon — is the spec format earning what it costs?

## The problem this build exists to solve

The spec format is load-bearing twice: every build here starts from a spec written to it, and every
repo adopting the memory-tree kit receives it. Check 12 grades it STRUCTURALLY — sections present,
ordered, non-empty, free of placeholders. Nothing anywhere grades whether a conforming spec was any
use to the agent that built from it. A format can be conformant and still fail its reader, and
nobody had measured which this one is.

The answer this build reached: it is a shape contract enforced hardest where specs least often fail,
its largest gap is that it joins nothing to anything, and its largest cost is an unmanaged revision
loop — not the ceremony everyone assumes.

## Expected improvements

- A ranked, evidenced answer to what the format costs and what it lacks, so the next edit to it is
  argued from the corpus rather than from taste. Eight points, severity against cost.
- Two live hypotheses settled before they drive an edit.

## Detriments if this is not built

- The format keeps being tuned by intuition, and both hypotheses above would have driven an edit —
  one of them a deletion the evidence says buys nothing.
- The revision loop stays unmeasured, and it is where the defects actually are.

## Build-level rules

- **Research only, by owner ruling at kickoff.** No edit to `memory/TEMPLATE-SPEC.md`, to
  `tools/memory-tree/SPEC-TEMPLATE.template.md`, or to check 12. No new gate leg and no spec set.
- **Every finding is quoted post-skeptic.** 34 raised, 29 confirmed, 5 refuted — precision 0.85
  against the charter's 0.5 threshold. Twenty-six survivors were narrowed on verification, several
  with headline numbers corrected downward. Where an earlier number disagrees, the record wins.
- **A fault-hunt selects for faults**, so what the format does well is measured and reported beside
  what it lacks, and the two questions this pass could NOT answer are stated, not implied away.
- **The records are `**Serves:** none`** on the aFerriedDossier and dGaugedVintage precedents: a
  research report precedes the specs, and this build authors none. That moves `RECORD_UNBOUND_PIN`
  12 → 14, the fourth deliberate wrong-way move, recorded beside the pin with its fall-back.

## Parked decisions

- **Whether the 29 findings become backlog rows.** None is filed. §7's left-shift rule wants them
  recorded; 29 rows would flood `memory/backlog/TOOL.md`, and the ranking is the owner's call. The
  records are committed and reachable, so nothing is lost by deciding later.
- **The reading-side cost has no mitigation.** The `aStagedLane` build on the unmerged
  `spec-writing-harness` branch fans spec WRITING over per-unit briefs; its ids are not cited here
  because this tree does not define them. Nothing does the same for the builder that must READ a
  median 61,908 bytes of spec per build, 476,860 at the top.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| — | `TOOL-aWeighedCanon-1` | 1 | the measurements: population, rev distribution, per-section mass and growth, read cost |
| — | `TOOL-aWeighedCanon-2` | 1 | the findings: 29 confirmed, three themes, a ranked build order |

Neither unit is a code change and neither carries a spec — this build is research, by owner ruling.
The ids exist so the two records can be cited and so a later build can supersede them by name.

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aWeighedCanon-1 TOOL-aWeighedCanon-2

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 2 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
