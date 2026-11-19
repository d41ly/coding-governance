---
slug: dSweptScratch
node: d
opened: 2026-11-19
streams: tooling
roster: TOOL
ids: TOOL-dSweptScratch-1
---

# dSweptScratch — selftest scratch that a Windows run actually removes

Node `d` measured ~1M leftover directories (~50 GB) in `%TEMP%` on 2026-11-19, enough to stall the
disk. Most of the gov share was selftest and fixture scratch that the code believed it removed:
`shutil.rmtree(..., ignore_errors=True)` over a scratch git repository, whose objects git writes
READ-ONLY, so on Windows the unlink raises, `ignore_errors` swallows it and the whole tree survives.
The memory-recall selftest fixed exactly this as TOOL-aBranchedMandate-6; the fix never reached the
other kits. A handful of scratch dirs were never removed at all, or were lost to a subshell or a
replaced trap. The gate bar points `TMPDIR` at a trapped work dir, so none of this showed on the bar;
it lands in `%TEMP%` whenever a suite runs directly, which is how sessions run them.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dSweptScratch-1` | 1 | every selftest and fixture removes the scratch it made, read-only git objects included |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node d · opened 2026-11-19 · streams tooling
ids TOOL-dSweptScratch-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dSweptScratch-1 — every selftest and fixture removes the scratch it made, read-only git objects included](spec/2026-11-19-spec-TOOL-dSweptScratch-1.md) | — | 1 | OPEN | rev-1 | 2026-11-19 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-dSweptScratch-1.

Ids no `spec-audit` record has ever named: TOOL-dSweptScratch-1.

Ids whose spec moved past its audited revision: none — 0 of 1 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
