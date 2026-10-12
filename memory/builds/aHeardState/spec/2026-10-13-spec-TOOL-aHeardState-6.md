# TOOL-aHeardState-6 — the bug-class checklist names a held suite whose guard misses a sibling kit it reads

**Status:** CLOSED · rev-1 · 2026-10-13 · node a · Tier-1 · base 2f9dfaf0 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-aHeardState-1-2-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aHeardState-1-2-acceptance-ledger.md) | journal | TOOL-aHeardState-1 TOOL-aHeardState-2 TOOL-aHeardState-3 TOOL-aHeardState-4 TOOL-aHeardState-5 TOOL-aHeardState-7 TOOL-aHeardState-8 |

<!-- /gen:spec-records -->

## 1. Goal

Closing review round 1 id 14 (HIGH): the intent lens found the narrow-guard defect `TOOL-aHeardState-5`
fixes. The class is wider than this leg: scratch-guard's suite resolves the run-gates kit and its guard
does not name it. A lint over every suite reds that leg too, so the class goes to the bug-class
checklist, as the charter's `[left-shift]` practice allows where no gate fits yet.

## 2. Scope (IN)

- **S1** — a class record `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`, rendered into the
  catalogue by `python tools/memory-tree/gotchas.py --write`, and claimed by the agent-cap dossier.
  Observed by AC1.

## 3. Non-goals (OUT)

- The lint itself, which reds scratch-guard's leg on arrival and so needs its own build.
- Changing scratch-guard's guard.

### Edges

- **hands-off** external — a gate-legs lint that reads each held suite for the sibling kits it resolves.

## 4. Design

One class record in the shape its siblings carry, its anchors on `tools/gate-legs.json` and the hooks
kit's suites so `gotchas.py --for-paths` selects it for a diff touching either.

### Files touched (estimate)

- `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`
- `memory/map/features/agent-cap.md`

## 5. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --for-paths tools/gate-legs.json` runs, its
  checklist names `held-suite-guard-misses-a-sibling-kit`. Red when: the record is absent or its anchor
  does not select it.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted from closing review round 1 id 14.
