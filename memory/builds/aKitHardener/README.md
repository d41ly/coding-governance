---
slug: aKitHardener
node: a
opened: 2026-07-14
streams: deployer
roster: DEPL
ids: DEPL-aKitHardener-1
status: CLOSED
---

# DEPL-aKitHardener — govkit Phase 0: kit hardening (2026-07-14)

The first build unit of the **govkit** deployer (research: [../aDeployScout/](../aDeployScout/)).
Makes every kit **version-detectable** and every adopt script **re-run-safe**, so a future deployer can
`plan`/`apply`/`upgrade` them. Lands standalone — worth having even if the deployer never ships (spec §4).

- [spec/2026-07-14-spec-aKitHardener-1.md](spec/2026-07-14-spec-aKitHardener-1.md) — closed scope, the
  version-marker convention, and the two contested calls resolved (no-conf halt; skip set -e on codebase-map).
- [build/2026-07-14-build-aKitHardener-1.md](build/2026-07-14-build-aKitHardener-1.md) — the 7 surfaces, what
  shipped, verification ledger (incl. the no-Python-interpreter caveat), gate deltas, and the closing review.

<!-- gen:build-index -->
**Build status:** CLOSED · 0 unit(s) · node a · opened 2026-07-14 · streams deployer
ids DEPL-aKitHardener-1

*No spec under this build carries a status header; the status above is declared in the front matter.*

Records live under `spec/` and `build/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-07-14-spec-aKitHardener-1.md](spec/2026-07-14-spec-aKitHardener-1.md)
- **`build/`**
  - [2026-07-14-build-aKitHardener-1.md](build/2026-07-14-build-aKitHardener-1.md)
<!-- /gen:build-docs -->
