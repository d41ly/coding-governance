---
slug: dRenderedAnchor
node: d
opened: 2026-10-19
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dRenderedAnchor-1 TOOL-dRenderedAnchor-2 TOOL-dRenderedAnchor-3 TOOL-dRenderedAnchor-4 TOOL-dRenderedAnchor-5 TOOL-dRenderedAnchor-6
---

# dRenderedAnchor — an adopter's role index names the harnesses where the review-harness kit landed

## The problem this build exists to solve

In an adopter, govkit lands the review-harness kit at `<prefix>/review-harness/`, its id, while gov
homes it at `tools/workflows/`. Each rendered harness's receipt row carries its TEMPLATE as `source`.
`resolve_kit_dir` matches only a row whose `source` ends in `<home>/<anchor>`, so it misses the
rendered `tier2-review.js` and `unattended-build.js` and falls back to `tools/workflows/`. The
rendered `.claude/roles.json` then names two files that do not exist, and agent-cap refuses gov's
own review and build harnesses. The measurement is
[build/](build/2026-10-19-build-TOOL-dRenderedAnchor-1-1-repro.md).

## Expected improvements

- An adopter's role index names each harness at the path the install holds.
- The spawn guard admits gov's own review and build harnesses in a default adopter.
- A rendered file is found through its receipt row by every caller of the resolver.
- A role index naming an installed harness at a wrong path reds its own leg.

## Detriments if this is not built

- Every adopter with the review-harness kit cannot run `/build` or a Tier-2 review.
- The render note says a kit is not installed when it is.
- The next rendered anchor any kit resolves misses the same way, with no leg to say so.

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-2: a shipped kit edit and a cross-kit
  change to the carried resolver.
- Owner, 2026-10-19: the fix sits in the resolver, its canonical and every inline copy, not in roles.
- Owner, 2026-10-19: a harness found nowhere in the install stays a note, as the roles descriptor's
  accepted absence of review-harness declares; the new red is a listed harness absent while a file
  of its name is installed elsewhere.
- Owner, 2026-10-19: no spec audit.
- Owner, 2026-10-19: unit 1's closing review promoted its 3 mediums and 5 lows as unit 2 (M4), and the
  /build Skill's harness paths, a pre-existing gap the review refuted as not introduced, ride it too.
- Owner, 2026-10-19, after review round 4 (2 lows, precision 0.71): promote them as unit 5 and
  run no further review round; the build closes on unit 5 and one full bar.
- Scratch installs live under the system temp root; no adopter repository is written.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dRenderedAnchor-1` | the resolver finds a rendered file through its receipt row, and the role render reds a harness listed where it is not installed |
| 2 | `TOOL-dRenderedAnchor-2` | unit 1's closing-review findings closed as one batch, and the /build Skill's harness citations resolved like the role index |
| 3 | `TOOL-dRenderedAnchor-3` | the closing review's round-2 findings on unit 2 closed as one batch |
| 4 | `TOOL-dRenderedAnchor-4` | the closing review's round-3 findings on unit 3 closed as one batch |
| 5 | `TOOL-dRenderedAnchor-5` | the closing review's round-4 findings on unit 4 closed as one batch, with no review round after it |
| 6 | `TOOL-dRenderedAnchor-6` | the review protocol and the unattended Skill resolve their harness citations through the receipt-aware resolver |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 6 unit(s) · node d · opened 2026-10-19 · streams tooling
ids TOOL-dRenderedAnchor-1 TOOL-dRenderedAnchor-2 TOOL-dRenderedAnchor-3 TOOL-dRenderedAnchor-4 TOOL-dRenderedAnchor-5 TOOL-dRenderedAnchor-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dRenderedAnchor-1 — the kit resolver finds a rendered file through its receipt row, and the role render reds a harness listed where it is not installed](spec/2026-10-19-spec-TOOL-dRenderedAnchor-1.md) | — | 2 | CLOSED | rev-1 | 2026-10-19 |
| [TOOL-dRenderedAnchor-2 — unit 1's closing-review findings closed as one batch, and the /build Skill's harness citations resolved like the role index](spec/2026-10-19-spec-TOOL-dRenderedAnchor-2.md) | — | 2 | CLOSED | rev-1 | 2026-10-19 |
| [TOOL-dRenderedAnchor-3 — the closing review's round-2 findings on unit 2 closed as one batch](spec/2026-10-19-spec-TOOL-dRenderedAnchor-3.md) | — | 2 | CLOSED | rev-2 | 2026-10-19 |
| [TOOL-dRenderedAnchor-4 — the closing review's round-3 findings on unit 3 closed as one batch](spec/2026-10-19-spec-TOOL-dRenderedAnchor-4.md) | — | 1 | CLOSED | rev-1 | 2026-10-19 |
| [TOOL-dRenderedAnchor-5 — the closing review's round-4 findings on unit 4 closed as one batch, with no review round after it](spec/2026-10-19-spec-TOOL-dRenderedAnchor-5.md) | — | 1 | CLOSED | rev-1 | 2026-10-19 |
| [TOOL-dRenderedAnchor-6 — the review protocol and the unattended Skill resolve their harness citations through the receipt-aware resolver](spec/2026-10-19-spec-TOOL-dRenderedAnchor-6.md) | — | 2 | INPROGRESS | rev-1 | 2026-10-19 |
<!-- /gen:build-units -->

Records: 19 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dRenderedAnchor-1 TOOL-dRenderedAnchor-2 TOOL-dRenderedAnchor-3 TOOL-dRenderedAnchor-4 TOOL-dRenderedAnchor-5 TOOL-dRenderedAnchor-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
