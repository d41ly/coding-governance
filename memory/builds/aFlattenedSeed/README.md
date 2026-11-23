---
slug: aFlattenedSeed
node: a
opened: 2026-11-22
streams: tooling
roster: TOOL
ids: TOOL-aFlattenedSeed-1 TOOL-aFlattenedSeed-2 TOOL-aFlattenedSeed-3 TOOL-aFlattenedSeed-4
---

# aFlattenedSeed — three kit readers that red an adopter's bar on its own layout

## The problem this build exists to solve

inCMS re-pulled the kits to b2eec4b6, and its full bar went red on three gov-side defects. The first is
`product_tests.py#read_manifest_rows`, which refuses the object-wrapped leg manifest that
TOOL-aWrappedRoster-1 taught `parse_leg_names` to read. The second is `eol_class.py`, which crashes
with an IndexError on a submodule gitlink, because `cat-file` answers `missing` for a commit that
lives in another repository. The third is the `legacy_ledger` seed, which cannot seed any population
on an install that lands the memory-tree kit flat, because its argv's `{prefix}/memory-tree/...`
resolves to a directory that install does not have.

## Expected improvements

- An adopter with a wrapped manifest, a submodule, or a flat memory-tree install can arm its ratchet
  populations and run the bar green on its own debt.

## Detriments if this is not built

- inCMS cannot land its re-pull, and the bPliantViewport run it holds stays parked.

## Build-level rules

- Owner go, 2026-11-22, relayed verbatim by the bPliantViewport session on node `a`: "Yes, fix upstream".

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aFlattenedSeed-1` | wrapped-manifest unwrap · gitlinks skipped · seed `{prefix}` through `resolve_kit_dir` |
| 2 | `TOOL-aFlattenedSeed-2` | sh_hygiene's home-graded note on stderr, so a `--measure` seed reads rows only |
| 3 | `TOOL-aFlattenedSeed-3` | adopter ledger legs read their seeded home over the seed's own population |
| 4 | `TOOL-aFlattenedSeed-4` | positional and encoding ledgers leave frozen records (`builds/`, `archive/`) alone |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 4 unit(s) · node a · opened 2026-11-22 · streams tooling
ids TOOL-aFlattenedSeed-1 TOOL-aFlattenedSeed-2 TOOL-aFlattenedSeed-3 TOOL-aFlattenedSeed-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aFlattenedSeed-1 — three kit readers read an adopter's own layout](spec/2026-11-22-spec-TOOL-aFlattenedSeed-1.md) | — | 1 | CLOSED | rev-4 | 2026-11-22 |
| [TOOL-aFlattenedSeed-2 — sh_hygiene's home-graded note rides stderr](spec/2026-11-23-spec-TOOL-aFlattenedSeed-2.md) | — | 1 | CLOSED | rev-1 | 2026-11-23 |
| [TOOL-aFlattenedSeed-3 — an adopter's ledger legs grade the population their seeds armed](spec/2026-11-23-spec-TOOL-aFlattenedSeed-3.md) | — | 1 | CLOSED | rev-2 | 2026-11-23 |
| [TOOL-aFlattenedSeed-4 — the positional and encoding ledgers leave frozen records alone](spec/2026-11-23-spec-TOOL-aFlattenedSeed-4.md) | — | 1 | CLOSED | rev-2 | 2026-11-23 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-aFlattenedSeed-1 TOOL-aFlattenedSeed-2 TOOL-aFlattenedSeed-3 TOOL-aFlattenedSeed-4.

Ids no `spec-audit` record has ever named: TOOL-aFlattenedSeed-1 TOOL-aFlattenedSeed-2 TOOL-aFlattenedSeed-3 TOOL-aFlattenedSeed-4.

Ids whose spec moved past its audited revision: none — 0 of 4 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
