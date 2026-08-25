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
`READ_PATH_CEILING` is a gating byte budget over the files `AGENTS.md` points a session at, and as a
budget it does not work. Reconstructed against each commit's first parent, the pin moved 26 times
between 2026-08-08 and 2026-08-25: 25 up, 1 down. The single downward move (`95431 -> 86476`,
`d816c30b`) was forced by hygiene check 11's new 400-byte per-entry cap taking a manifest from
20920 B to 12215 B — a different check's doing, not this one's. In seventeen days the budget has
never once caused a trim.

It cannot, and the reason is structural rather than cultural. `memory/DECISIONS.md` is append-only by
charter section 6, so one member of the read path is forbidden by governance to shrink; a breach is
therefore guaranteed and the exit set is permanently raise-or-rotate. `memory/LIVE.md` is generated
and its length tracks OPEN BUILD COUNT, so part of the budget measures parallelism rather than
reading cost — already recorded as `TOOL-aRelaxedShard-3`. And because `corpus_ids.py` only fails
when the total EXCEEDS the pin, a ceiling left high is green forever and nothing re-audits it, which
`cKeyedLaunchpad`'s review recorded as H6.

The half that DOES work is check 16 rule 3: the charter may not point a session at a `memory/` file
that no byte cap covers and no waiver names. That is a structural citation check, it is the only
thing binding the charter's citations to the hygiene caps, and it dies with the budget — the whole
of check 16 sits behind `if conf["READ_PATH_CEILING"]:`, so blanking the pin turns rule 3 off
silently.

## Expected improvements
- The instrument that has cost 26 owner decisions and bought zero trims stops gating, and the
  question it was asking — is mandatory reading growing faster than anyone intended — is answered by
  a signal that derives both operands and cannot be raised.
- Rule 3 survives the change and gains an arming condition of its own, so an adopter who declines
  the budget does not silently lose the citation check.
- `TOOL-aRelaxedShard-3` closes: a rate measured over non-generated members stops reporting
  parallelism as growth.
- Every adopter of the memory-tree kit inherits the fix rather than re-deriving it, and a stale
  `READ_PATH_CEILING` in an adopter's conf becomes inert rather than an error.

## Detriments if this is not built
- The pin keeps ratcheting. At the measured 6184 B/day the raise just taken buys about four days,
  after which the next session pays the same owner decision for the same non-result.
- Every raise is an owner turn spent on bookkeeping, and the alternative a spent budget offers is
  worse: it blocks RECORDING work rather than doing it, which is how this repo has twice been unable
  to log a decision it had already made.
- Rule 3 stays hostage. Anyone who acts on the (correct) reading that the budget is useless and
  blanks the key takes the citation check down with it and gets a green bar for it.

## Build-level rules
- **The owner ruled twice on 2026-08-25, and both rulings narrowed an opening proposal.** The
  opening position was retire check 16 entirely; the ruling is KEEP it, replace the BUDGET half with
  a rate signal, and keep rule 3 gating. The second ruling is blast radius: kit-wide, not gov's pin
  alone.
- **The pin was raised first and deliberately**, at `18cc9b78`, `135677 -> 161120`. This build may
  record decisions because of that raise; it does not get to treat the raise as evidence for its own
  thesis, and the justification block prices it on its own terms.
- **The rate signal derives both operands or it is not built.** A signal with an authored number in
  it is the instrument this build is replacing, one indirection down. It carries a liveness
  assertion, so a derivation that cannot move prints DEAD PROBE rather than a reassuring zero.
- **Rule 3's arming condition is the load-bearing design question**, not a detail of the deletion. A
  unit that removes the budget without giving rule 3 its own condition has shipped a silent coverage
  loss, and the acceptance criterion must observe rule 3 firing with `READ_PATH_CEILING` absent from
  the conf entirely.
- **`read_set` does not move.** Which files count is out of scope; this build changes what is done
  with the measurement, not how the population is derived.

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
