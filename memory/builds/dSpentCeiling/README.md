---
slug: dSpentCeiling
node: d
opened: 2026-08-25
streams: tooling
roster: TOOL
ids: TOOL-dSpentCeiling-1
status: OPEN
---

# dSpentCeiling — the read-path budget becomes a rate signal, and rule 3 keeps its teeth

## The problem this build exists to solve
`READ_PATH_CEILING` gates a byte budget over the files `AGENTS.md` points a session at, and it has
never caused a trim: 27 movements since 2026-08-08, 26 of them up, and the one drop forced by a
different check. It was always a SECOND bound — check 6 already caps all six members at 61440 B
each, 368640 B of first bounds against the 135694 B held — and it bound earlier only because it
summed six incommensurable things. Worse, 54.0% of what it measures is RENDERED FROM KIT TEMPLATES
(`memory-tree@2.41`, `unattended@1.8`) and cannot be trimmed by this repo at all, so most raises were
pricing other kits' releases against this kit's budget. The half that works is rule 3 — the charter
may not cite an uncapped `memory/` file — and it dies with the budget, because all of check 16 sits
behind `if conf["READ_PATH_CEILING"]:`.

## Expected improvements
- The instrument stops gating, and the question it asked is answered by a signal that derives both
  operands and so cannot be raised.
- Rule 3 survives with an arming condition of its own, so declining the budget no longer takes the
  citation check down silently.
- `TOOL-aRelaxedShard-3` closes: a rate over non-generated members stops reporting parallelism.
- Every memory-tree adopter inherits the fix rather than re-deriving it.

## Detriments if this is not built
- The pin keeps ratcheting. At the measured 6184 B/day the raise just taken buys about four days.
- Each raise is an owner turn spent on bookkeeping, and a spent budget blocks RECORDING work rather
  than doing it — twice already this repo could not log a decision it had made.
- Rule 3 stays hostage: anyone acting on the correct reading that the budget is useless blanks the
  key, loses the citation check, and is given a green bar for it.

## Build-level rules
- **The owner ruled twice on 2026-08-25, and both narrowed an opening proposal.** The opening
  position was retire check 16 entirely; the ruling is KEEP it, replace the BUDGET half with a rate
  signal, and keep rule 3 gating. The second ruling is blast radius: kit-wide, not gov's pin alone.
- **The pin was raised first and deliberately**, at `18cc9b78`, `135677 -> 161120`. This build may
  record decisions because of that raise; it does not get to treat the raise as evidence for its own
  thesis.
- **The rate signal derives both operands or it is not built.** An authored number in it is the
  instrument being replaced, one indirection down. It carries a liveness assertion, so a derivation
  that cannot move prints DEAD PROBE rather than a reassuring zero.
- **Rule 3's arming condition is the load-bearing design question**, not a detail of the deletion.
  Its acceptance must observe rule 3 firing with `READ_PATH_CEILING` absent from the conf entirely.
- **`read_set` does not move.** Which files count is out of scope.
- **The append-only argument is REFUTED and must not be re-opened.** An earlier draft of this build
  argued the breach was structurally guaranteed because `memory/DECISIONS.md` cannot shrink. It can:
  it ROTATED on 2026-08-10, 79 rows to `memory/archive/`. The real argument is composition, above.
- **drift-audit is undossiered and this build dossiers it.** Its keys sit in `memory/map/baseline.toml`
  and the new signal lands there, so the map's convergence rule makes that a DoR item.

## Parked decisions
None yet.

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-08-25 · streams tooling
ids TOOL-dSpentCeiling-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 0 bound to this build, across 0 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
