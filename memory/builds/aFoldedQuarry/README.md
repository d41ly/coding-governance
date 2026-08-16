---
slug: aFoldedQuarry
node: a
opened: 2026-08-08
streams: tooling
roster: TOOL
ids: TOOL-aFoldedQuarry-1 TOOL-aFoldedQuarry-2 TOOL-aFoldedQuarry-3 TOOL-aFoldedQuarry-4 TOOL-aFoldedQuarry-5 TOOL-aFoldedQuarry-6 TOOL-aFoldedQuarry-7 TOOL-aFoldedQuarry-8 TOOL-aFoldedQuarry-9
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
| U3 | [spec/units/2026-08-08-spec-aFoldedQuarry-5-u3-corpus-ids.md](spec/units/2026-08-08-spec-aFoldedQuarry-5-u3-corpus-ids.md) | One id grammar, one walk, every consumer |
| U4 | [spec/units/2026-08-08-spec-aFoldedQuarry-6-u4-gotchas.md](spec/units/2026-08-08-spec-aFoldedQuarry-6-u4-gotchas.md) | Bug-class corpus + the reviewer checklist generator |
| U5 | [spec/units/2026-08-08-spec-aFoldedQuarry-7-u5-harness.md](spec/units/2026-08-08-spec-aFoldedQuarry-7-u5-harness.md) | Harness disciplines: derived pins, armed branches, batched fixtures |

A row becomes a link when its sub-spec lands. A link to an unwritten file is a broken link, and
hygiene check 2 is right to say so.

Master spec: [spec/2026-08-08-spec-aFoldedQuarry-1.md](spec/2026-08-08-spec-aFoldedQuarry-1.md).

## Order

U6 first in wall-clock terms: every other unit's adversarial review runs on that harness. Then
U1 (it changes every path the rest operate on), U2, then U3 and U4 (independent of each other),
then U5.

<!-- gen:build-index -->
**Build status:** CLOSED · 7 unit(s) · node a · opened 2026-08-08 · streams tooling · ids TOOL-aFoldedQuarry-1 TOOL-aFoldedQuarry-2 TOOL-aFoldedQuarry-3 TOOL-aFoldedQuarry-4 TOOL-aFoldedQuarry-5 TOOL-aFoldedQuarry-6 TOOL-aFoldedQuarry-7 TOOL-aFoldedQuarry-8 TOOL-aFoldedQuarry-9

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aFoldedQuarry-1 — fold the upstream ledger + trove builds into the memory-tree kit](spec/2026-08-08-spec-aFoldedQuarry-1.md) | CLOSED | rev-3 | 2026-08-08 |
| [TOOL-aFoldedQuarry-2 — U6: index-keyed verdict join in the Tier-2 review harness](spec/units/2026-08-08-spec-aFoldedQuarry-2-u6-indexed-join.md) | CLOSED | rev-2 | 2026-08-08 |
| [TOOL-aFoldedQuarry-3 — U1: retire the discipline directory axis, keep the discipline signal](spec/units/2026-08-08-spec-aFoldedQuarry-3-u1-flatten.md) | CLOSED | rev-2 | 2026-08-08 |
| [TOOL-aFoldedQuarry-4 — U2: the generated build index replaces the authored tree](spec/units/2026-08-08-spec-aFoldedQuarry-4-u2-build-index.md) | CLOSED | rev-2 | 2026-08-08 |
| [TOOL-aFoldedQuarry-5 — U3: one id grammar, one walk, every consumer](spec/units/2026-08-08-spec-aFoldedQuarry-5-u3-corpus-ids.md) | CLOSED | rev-3 | 2026-08-08 |
| [TOOL-aFoldedQuarry-6 — U4: the bug-class corpus and its per-diff checklist](spec/units/2026-08-08-spec-aFoldedQuarry-6-u4-gotchas.md) | CLOSED | rev-3 | 2026-08-08 |
| [TOOL-aFoldedQuarry-7 — U5: the harness disciplines, made mechanical](spec/units/2026-08-08-spec-aFoldedQuarry-7-u5-harness.md) | CLOSED | rev-1 | 2026-08-08 |

Records live under `spec/`, `build/` and `reviews/`.
<!-- /gen:build-index -->
