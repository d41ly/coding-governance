# TOOL-aWrappedRoster-1 — the leg-manifest parser reads an object-wrapped manifest

**Status:** CLOSED · rev-2 · 2026-11-22 · node a · Tier-1 · base 8b8b1374 · streams tooling

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

- **AC1** — When `parse_leg_names` reads a bare row list, an object whose `legs` holds that list, an
  object with no `legs` and a JSON scalar, it returns the leg names for the first two and raises
  ValueError for the last two.
  Red when: the parser refuses the object shape, or reads either refusal as a manifest.
  Observed red against the base `tree_lib.py` on 2026-11-22: the object shape raised ValueError.
- **AC2** — When the fixed parser reads inCMS's committed leg manifest (an object holding `_doc` and
  `legs`), it returns that manifest's leg names. Red when: it raises.
  Observed 2026-11-22 against inCMS branch/admin-mobile-620da1.

## 6. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `memory hygiene` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC1 · `--selftest` parses the four shapes through `parse_leg_names`; staged red by reading them through the base parser · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-22 · initial draft.
- rev-2 · 2026-11-22 · AC1 · AC2 · the bar's spec-tokens leg: AC1 observes the arm, not the suite, and AC2 names the adopter's manifest without a path gov does not track.
