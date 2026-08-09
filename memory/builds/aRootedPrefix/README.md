---
slug: aRootedPrefix
node: a
opened: 2026-08-09
streams: tooling
roster: TOOL
ids: TOOL-aRootedPrefix-1
---

# aRootedPrefix — codebase-map at any install prefix

The codebase-map kit resolved the adopting repo's root as the kit dir's grandparent, which encodes
its `<repo-root>/codebase-map/` convention. Any repo installing kits under a prefix landed one
segment short, and the two entrypoints that do not import the project layer answered from the empty
corpus that produced instead of failing. Measured on paired fixture repos: one range with a genuine
shipped reinvention reports `collision_flags: 1` at a root install and `0` at a prefixed one.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node a · opened 2026-08-09 · streams tooling · ids TOOL-aRootedPrefix-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aRootedPrefix-1 — codebase-map: make the kit correct at any install prefix](spec/2026-08-09-spec-aRootedPrefix-1.md) | INPROGRESS | rev-3 | 2026-08-09 |
<!-- /gen:build-index -->
