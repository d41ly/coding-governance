# TOOL-aHeardState-4 — the format-guard self-test guard names the hook files, not the whole hooks directory

**Status:** SPECCED · rev-1 · 2026-10-13 · node a · Tier-1 · base 2f9dfaf0 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Closing review round 1 id 9 (HIGH): the leg's `{prefix}/hooks/` guard made six legs share that guard,
past `BROAD_LEG_FLOOR=5` in `tools/check-spec-tokens.py`, so the directory dropped out of the
spec-tokens join for every spec. Narrow the guard to the hook files the suite reads.

## 2. Scope (IN)

- **S1** — the `format-guard self-test` row's guard in `tools/gate-legs.json` names
  `{prefix}/hooks/format-guard.js`, `{prefix}/hooks/format-guard.test.sh`,
  `{prefix}/hooks/scratch-guard.js` and `AGENTS.md` instead of `{prefix}/hooks/`. Observed by AC1.

## 3. Non-goals (OUT)

- The runlog files the parity arm reads, which are `TOOL-aHeardState-5`'s.

### Edges

- **hands-off** `TOOL-aHeardState-5` — adding the runlog files to the same guard.

## 4. Design

One guard list in one row, edited to exact paths.

### Files touched (estimate)

- `tools/gate-legs.json`

## 5. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py --list` runs, its broad-guard line no longer names
  `tools/hooks/`. Red when: the list still counts six legs on that guard and excludes it.

## 6. Gates

`spec-tokens self-test` · `run-gates canary` · `run-gates gov canary`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted from closing review round 1 id 9.
