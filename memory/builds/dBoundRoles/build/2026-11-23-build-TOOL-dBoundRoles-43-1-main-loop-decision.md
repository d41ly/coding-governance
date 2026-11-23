**Serves:** journal TOOL-dBoundRoles-43

# TOOL-dBoundRoles-43 — the main loop's decision on the renamed spawn-guard leg the open specs still name

TOOL-dBoundRoles-25, built at `00a96bb43`, renamed the bar leg `agent-cap self-test` to `spawn-guard self-test`
(`tools/gate-legs.json`). Ten open roster specs still name the old leg: units 43, 50, 56, 58, 60, 62, 63, 64, 66
and 69 (DERIVED: `git grep -l 'agent-cap self-test' -- memory/builds/dBoundRoles/spec`). Once a spec is live, the
spec-token checker reds it on two hits: the leg name, and a guards finding naming the renamed leg that the spec's
Files touched trip. `--dispatch` refuses the unit while those hits stand.

The correction is spec text, which only `gov-spec-writer` writes. This session cannot spawn one directly. Its
`PreToolUse` hooks run from the primary tree, whose `agent-cap.js` predates the handoff marker this run's
TOOL-dBoundRoles-17 and -6 built, so rule 6 refuses every rendered handoff ("0 gov:handoff marker lines"). The
handoffs rendered at `ed2b4eb06` for the ten specs were refused that way. The harness `unattended-build.js` leaves
an existing conforming spec alone and folds only audit findings, and the owner stopped this chain's audits. The
builder's role writes a spec's status cell and nothing else.

Each answer below is the option no worse than the others on any principle (P18), decided rather than parked, and
binds over each named spec as the owner's ruling `2026-11-23-build-TOOL-dBoundRoles-20-2-owner-ruling` does.

1. **The leg reads by its new name.** Wherever one of the ten specs names `agent-cap self-test`, the run reads
   `spawn-guard self-test`, and that spec's builder answers each criterion and arm against the renamed leg.
2. **The hits are waived through the register's own door.** While a spec is live, its leg hit and its spawn-guard
   guards hit are rows of `memory/project/spec-token-waivers.txt`, written by
   `python tools/memory-tree/ratchet.py widen spec-token-waivers` with this record's reason. Each row is dropped
   when no live spec produces its hit any more, so the register shrinks back as each unit closes.
3. **The spec text is owed, not abandoned.** Each named spec's leg rename, and TOOL-dBoundRoles-43 S2's rev bump of
   TOOL-dBoundRoles-25's spec with that spec's own renamed leg and guards line, is owed to `gov-spec-writer`. The
   close carries them in its owed list, beside the bumps already owed to specs 53 and 59. TOOL-dBoundRoles-43's
   builder answers S2 AMENDED in its ledger, naming this record, and writes no spec text but its own status cell.

widens: the spec-token waiver register, by the renamed leg's rows while each named spec is live · relaxes: none.
