---
slug: dNomadicAtlas
node: d
opened: 2026-08-11
streams: tooling
roster: TOOL
ids: TOOL-dNomadicAtlas-1
---

# dNomadicAtlas — durable leg evidence for run-gates.sh

`leg()` already held every leg's merged output in `$out` and printed it, then kept only the ROW for
the durable summary — the reason was in scope at the exact line the durable record was built, and
dropped there. So a `| tail` kept the WHICH and lost the WHY.

The upstream half of `ARCH-dNomadicAtlas-2` in the adopting repo (inCMS), where the same defect cost
a full gate cycle: a red leg inside a push piped through `tail -45`, unidentifiable afterwards, and
the reflexive re-run passed, so the evidence was gone for good.

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node d · opened 2026-08-11 · streams tooling · ids TOOL-dNomadicAtlas-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-dNomadicAtlas-1 — a red leg leaves its reason on disk](spec/2026-08-11-spec-dNomadicAtlas-1-run-gates-evidence.md) | CLOSED | rev-1 | 2026-08-11 |

Records live under `spec/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-11-spec-dNomadicAtlas-1-run-gates-evidence.md](spec/2026-08-11-spec-dNomadicAtlas-1-run-gates-evidence.md)
<!-- /gen:build-docs -->
