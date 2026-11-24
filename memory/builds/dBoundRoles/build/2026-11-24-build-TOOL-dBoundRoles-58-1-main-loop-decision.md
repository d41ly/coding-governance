**Serves:** journal TOOL-dBoundRoles-58 TOOL-dBoundRoles-60 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69

# TOOL-dBoundRoles-58 — the main loop's decision on the items that rev-bump a CLOSED spec

The specs of units 58, 60 and 62 to 69 were written before the units they repair were built. Many of their items say
"the pass bumps that unit's spec FIRST", and many of their criteria grep the bumped text. Every unit they name as a
target is CLOSED when the item is built. The build method freezes a CLOSED spec and corrects it only by a unit on top
(`doc.build-method#m4-the-spec-audit-owed-only-where-the-build-or-its-project-declares-it`). `TOOL-dBoundRoles-54` §8
F3 (DERIVED, its rev-6) already took that route for unit 49's criterion, with deviation record 543 in place of the
bump. A builder also writes no spec text but its own status cell.

Each answer below is the option no worse than the others on any principle (P18), decided rather than parked, and binds
over each named spec as the owner's ruling `2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling` does.

1. **A CLOSED spec is not edited.** Options: (a) the correction is recorded on top, in the repairing unit's one
   deviation record; (b) a builder bumps the frozen spec; (c) a spec writer bumps each frozen spec before the pass.
   (b) and (c) edit a frozen spec, and (b) is also outside the builder's role. Pick (a), the precedent of
   `TOOL-dBoundRoles-54` §8 F3.
2. **What the record holds.** The deviation record of the unit names, per target, the target's id and revision, the
   criterion or scope item restated, and the restated text in its After field. The restated text is the repairing
   spec's own item. Where a later unit restates the same text again, the later unit's record supersedes the earlier
   one by naming it.
3. **What the ledgers hold.** The target unit's acceptance ledger answers the restated criterion AMENDED, naming the
   repairing unit and its deviation record, in place of `amended rev-<n>`. Where a landed ledger line already says
   what the restated criterion asks, it is left as it stands and the repairing unit's own ledger says so.
4. **How a criterion that greps a frozen spec is observed.** The criterion reads the repairing unit's deviation record
   where it named the target's spec: the same token, present or absent in the record's After text for that target. The
   builder answers it AMENDED in its own ledger, naming this decision and the token it observed. A criterion that reads
   code, a suite, a help page, a registry or a ledger is observed as written.
5. **A target spec that is not CLOSED.** The same route holds: the builder writes no spec text but its own status cell.
   Text a spec writer owes a not-yet-built spec is written before that spec's dispatch, through the spec-write stage.
6. **The floors, code, cases and ledgers stand as written.** Nothing here removes a product change, an arm, a floor
   move, a worktree check or an observation a spec asks for.

widens: none · relaxes: the rev bumps of CLOSED specs that units 58, 60 and 62 to 69 ask for, each replaced by a row of
the repairing unit's deviation record.
