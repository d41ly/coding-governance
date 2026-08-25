---
slug: dSpentCeiling
node: d
opened: 2026-08-25
streams: tooling
roster: TOOL
ids: TOOL-dSpentCeiling-1 TOOL-dSpentCeiling-2 TOOL-dSpentCeiling-3 TOOL-dSpentCeiling-4 TOOL-dSpentCeiling-5
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
- A gate that has cost 27 movements and bought no trim stops gating, and nothing replaces it: check
  6's per-member caps were always the real bound.
- Rule 3 survives as a structural check rather than a switch, so declining the budget no longer takes
  the citation check down with it.
- `TOOL-aRelaxedShard-3` closes by deletion — with no budget, nothing measures parallelism as growth.
- Every memory-tree adopter inherits the fix rather than re-deriving it.

## Detriments if this is not built
- The pin keeps ratcheting. At the measured 6184 B/day the raise just taken buys about four days.
- Each raise is an owner turn spent on bookkeeping, and a spent budget blocks RECORDING work rather
  than doing it — twice already this repo could not log a decision it had made.
- Rule 3 stays hostage: anyone acting on the correct reading that the budget is useless blanks the
  key, loses the citation check, and is given a green bar for it.

## Build-level rules
- **The owner ruled three times on 2026-08-25, and each narrowed the one before.** Opening position:
  retire check 16 entirely. Ruling 1: KEEP it, replace the budget with a rate signal, rule 3 stays
  gating. Ruling 2: blast radius kit-wide. Ruling 3, on being shown that six specs for deleting one
  variable is the tail wagging the dog: DROP the replacement signal. One unit, no successor.
- **Nothing replaces the budget, and that is the finding rather than a concession.** Check 6 already
  caps all six members at 61440 B each. Rule 1 was a second bound over an already-bounded population.
- **The pin was raised first and deliberately**, at `18cc9b78`, `135677 -> 161120`. This build may
  record decisions because of that raise; it does not treat the raise as evidence for its thesis.
- **Rule 3 gets no new key.** It becomes structural via the capture-before-source idiom already
  shipped for `SPEC10_CUTOFF`. A fourth blankable pin would be the defect this build closes, renamed.
- **`read_set` does not move.** Which files count is out of scope.
- **The append-only argument is REFUTED and must not be re-opened.** An earlier draft argued the
  breach was structurally guaranteed because `memory/DECISIONS.md` cannot shrink. It can: it ROTATED
  on 2026-08-10, 79 rows to `memory/archive/`. The real argument is composition, above.

## Parked decisions
None yet.

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node d · opened 2026-08-25 · streams tooling
ids TOOL-dSpentCeiling-1 TOOL-dSpentCeiling-2 TOOL-dSpentCeiling-3 TOOL-dSpentCeiling-4 TOOL-dSpentCeiling-5

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dSpentCeiling-1 — retire check 16's byte budget, and make rules 3 and 4 structural](spec/2026-08-25-spec-TOOL-dSpentCeiling-1.md) | — | 2 | INPROGRESS | rev-2 | 2026-08-25 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dSpentCeiling-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
