---
slug: aRootedPrefix
node: a
opened: 2026-08-09
streams: tooling
roster: TOOL
ids: TOOL-aRootedPrefix-1 TOOL-aRootedPrefix-2 TOOL-aRootedPrefix-3
---

# aRootedPrefix — codebase-map at any install prefix

The codebase-map kit resolved the adopting repo's root as the kit dir's grandparent, which encodes
its `<repo-root>/codebase-map/` convention. Any repo installing kits under a prefix landed one
segment short, and the two entrypoints that do not import the project layer answered from the empty
corpus that produced instead of failing. Measured on paired fixture repos: one range with a genuine
shipped reinvention reports `collision_flags: 1` at a root install and `0` at a prefixed one.

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node a · opened 2026-08-09 · streams tooling · ids TOOL-aRootedPrefix-1 TOOL-aRootedPrefix-2 TOOL-aRootedPrefix-3

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aRootedPrefix-1 — codebase-map: make the kit correct at any install prefix](spec/2026-08-09-spec-aRootedPrefix-1.md) | CLOSED | rev-3 | 2026-08-10 |

Records live under `spec/` and `reviews/`.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-09-spec-aRootedPrefix-1.md](spec/2026-08-09-spec-aRootedPrefix-1.md)
- **`reviews/`**
  - [2026-08-09-review-aRootedPrefix-1.md](reviews/2026-08-09-review-aRootedPrefix-1.md)
<!-- /gen:build-docs -->
