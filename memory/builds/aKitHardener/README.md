# DEPL-aKitHardener — govkit Phase 0: kit hardening (2026-07-14)

The first build unit of the **govkit** deployer (research: [../2026-07-12-DEPL-aDeployScout/](../2026-07-12-DEPL-aDeployScout/)).
Makes every kit **version-detectable** and every adopt script **re-run-safe**, so a future deployer can
`plan`/`apply`/`upgrade` them. Lands standalone — worth having even if the deployer never ships (spec §4).

- [spec/2026-07-14-spec-aKitHardener-1.md](spec/2026-07-14-spec-aKitHardener-1.md) — closed scope, the
  version-marker convention, and the two contested calls resolved (no-conf halt; skip set -e on codebase-map).
- [build/2026-07-14-build-aKitHardener-1.md](build/2026-07-14-build-aKitHardener-1.md) — the 7 surfaces, what
  shipped, verification ledger (incl. the no-Python-interpreter caveat), gate deltas, and the closing review.
