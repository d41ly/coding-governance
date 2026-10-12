# TOOL-aHeardState-5 — the format-guard self-test guard covers the runlog files its parity arm reads

**Status:** CLOSED · rev-1 · 2026-10-13 · node a · Tier-1 · base 2f9dfaf0 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-aHeardState-1-2-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aHeardState-1-2-acceptance-ledger.md) | journal | TOOL-aHeardState-1 TOOL-aHeardState-2 TOOL-aHeardState-3 TOOL-aHeardState-4 TOOL-aHeardState-6 TOOL-aHeardState-7 TOOL-aHeardState-8 |

<!-- /gen:spec-records -->

## 1. Goal

Closing review round 1 id 10 (HIGH), with ids 2 and 25 (MEDIUM): the AC6 parity arm imports
`{prefix}/runlog/prose.py`, which imports `extract.py`, and resolves sibling kits through the inlined
resolvers, but the leg's guard names none of them. A prose.py edit alone skips the arm or reuses its
stale green. Add them to the guard.

## 2. Scope (IN)

- **S1** — the `format-guard self-test` guard in `tools/gate-legs.json` gains
  `{prefix}/runlog/prose.py`, `{prefix}/runlog/extract.py` and `{prefix}/lib/`. Observed by AC1.

## 3. Non-goals (OUT)

- A class gate for every held suite's sibling-kit reads; `TOOL-aHeardState-6` records the class.

### Edges

- **consumes-from** `TOOL-aHeardState-4` — the narrowed guard list this unit extends.

## 4. Design

Three more paths in the guard list `TOOL-aHeardState-4` narrowed.

### Files touched (estimate)

- `tools/gate-legs.json`

## 5. Acceptance criteria

- **AC1** — When `tools/gate-legs.json` is read for the `format-guard self-test` row, its guard holds the
  prose and extract readers of `tools/runlog/prose.py` and `tools/runlog/extract.py`, and `bash tools/run-gates/run-gates.sh
  --print-profile` still parses the manifest. Red when: a runlog path is missing from the guard.

## 6. Gates

`run-gates canary` · `run-gates gov canary`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted from closing review round 1 id 10; closes ids 2 and 25.
