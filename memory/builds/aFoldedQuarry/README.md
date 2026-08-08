---
slug: aFoldedQuarry
node: a
opened: 2026-08-08
streams: tooling
roster: TOOL
ids: TOOL-aFoldedQuarry-1..-6
---

# TOOL-aFoldedQuarry — fold `dQuarriedLedger` + `dWinnowedTrove` into the memory-tree kit

Node `a` · opened 2026-08-08 · streams tooling · base `42c3f4dc`.

Ports two upstream inCMS builds into this repo's parameterised kits, then re-dogfoods every change on
this repo's own `memory/`. The kit change and the dogfood migration are the same work done twice —
once as a tool, once as its first customer.

## Units

| Unit | Sub-spec | What it does |
|---|---|---|
| U6 | [spec/units/2026-08-08-spec-aFoldedQuarry-2-u6-indexed-join.md](spec/units/2026-08-08-spec-aFoldedQuarry-2-u6-indexed-join.md) | Index-keyed verdict join in the Tier-2 review harness |
| U1 | [spec/units/2026-08-08-spec-aFoldedQuarry-3-u1-flatten.md](spec/units/2026-08-08-spec-aFoldedQuarry-3-u1-flatten.md) | Retire the discipline directory axis; keep the discipline signal |
| U2 | [spec/units/2026-08-08-spec-aFoldedQuarry-4-u2-build-index.md](spec/units/2026-08-08-spec-aFoldedQuarry-4-u2-build-index.md) | Generated build index replaces the authored tree |
| U3 | `spec-aFoldedQuarry-5-u3-corpus-ids` — pending | One id grammar, one walk, every consumer |
| U4 | `spec-aFoldedQuarry-6-u4-gotchas` — pending | Bug-class corpus + the reviewer checklist generator |
| U5 | `spec-aFoldedQuarry-7-u5-harness` — pending | Harness disciplines: derived pins, armed branches, batched fixtures |

A row becomes a link when its sub-spec lands. A link to an unwritten file is a broken link, and
hygiene check 2 is right to say so.

Master spec: [spec/2026-08-08-spec-aFoldedQuarry-1.md](spec/2026-08-08-spec-aFoldedQuarry-1.md).

## Order

U6 first in wall-clock terms: every other unit's adversarial review runs on that harness. Then
U1 (it changes every path the rest operate on), U2, then U3 and U4 (independent of each other),
then U5.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 4 unit(s) · node a · opened 2026-08-08 · streams tooling · ids TOOL-aFoldedQuarry-1..-6

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aFoldedQuarry-1 — fold the upstream ledger + trove builds into the memory-tree kit](spec/2026-08-08-spec-aFoldedQuarry-1.md) | INPROGRESS | rev-2 | 2026-08-08 |
| [TOOL-aFoldedQuarry-2 — U6: index-keyed verdict join in the Tier-2 review harness](spec/units/2026-08-08-spec-aFoldedQuarry-2-u6-indexed-join.md) | CLOSED | rev-2 | 2026-08-08 |
| [TOOL-aFoldedQuarry-3 — U1: retire the discipline directory axis, keep the discipline signal](spec/units/2026-08-08-spec-aFoldedQuarry-3-u1-flatten.md) | CLOSED | rev-2 | 2026-08-08 |
| [TOOL-aFoldedQuarry-4 — U2: the generated build index replaces the authored tree](spec/units/2026-08-08-spec-aFoldedQuarry-4-u2-build-index.md) | CLOSED | rev-2 | 2026-08-08 |
<!-- /gen:build-index -->
