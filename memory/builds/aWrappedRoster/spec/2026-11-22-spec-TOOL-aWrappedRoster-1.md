# TOOL-aWrappedRoster-1 — the leg-manifest parser reads an object-wrapped manifest

**Status:** CLOSED · rev-1 · 2026-11-22 · node a · Tier-1 · base 8b8b1374 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`parse_leg_names` reads a leg manifest committed as an object whose `legs` key holds the row list,
as well as a bare row list. inCMS commits the object shape, so today every `Red-fix:` commit there
reds `routed commits name a specced unit` as uncheckable.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/tree_lib.py#parse_leg_names` unwraps a top-level object's `legs` value
  before its list check, and still raises ValueError when neither shape holds. Observed by AC1.
- **S2** — An arm in `routed_commits.py --selftest` pins both shapes and both refusals. Observed by
  AC1.

## 3. Non-goals (OUT)

- Any other manifest reader: `drift_signals.py` already accepts both shapes.
- Rewriting inCMS's manifest into a bare list: the object's `_doc` key is the adopter's own.

### Edges

- **consumes-from** `TOOL-aNimbleMend-8` — the red-fix lane and the one manifest parser it named

## 4. Design

### Mechanism

`rows = rows.get("legs")` when the parsed top level is a dict; the existing list check then refuses
an object with no list under `legs`, so a non-manifest blob still reads as absent.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/routed_commits.py`

## 5. Acceptance criteria

- **AC1** — When `python3 tools/memory-tree/routed_commits.py --selftest` runs, the
  TOOL-aWrappedRoster-1 arm passes and every other arm still does.
  Red when: the parser refuses `{"legs": [...]}`, or reads `{"_doc": "x"}` or a scalar as a manifest.
  Observed red against base `tree_lib.py` on 2026-11-22: the object shape raised ValueError.
- **AC2** — When the fixed parser reads inCMS's `scripts/gate-legs.json`, it returns that file's leg
  names. Red when: it raises.

## 6. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `memory hygiene` · `line length`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-22 · initial draft.
