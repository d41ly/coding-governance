# TOOL-dSafePassage-3 deviation 165 — the step's down never lifts a receipt below schema 3, and neither verb moves a non-number schema

**Serves:** deviation TOOL-dSafePassage-3

- **Departs from:** TOOL-dSafePassage-3@rev-6 [§4 Design, the step program]
- **Hand-off:** spec-to-code
- **Before:** the down "exits 0 at schema 3 without the field; exits 1 ... while `steps` holds an `applied` row for any other step; and otherwise sets `schema` to 3 and takes the field out", so a schema-1 or schema-2 receipt reaching the down is set to schema 3; the up's "otherwise" sets `schema` to 4 on any receipt not below 3, a non-number schema included.
- **After:** the down exits 0 writing nothing at schema 3 or below without the field, and exits 1 writing nothing on a `steps` field below schema 3; up and down both exit 1 writing nothing where `schema` is not a number.
- **Cause:** builder discovery
- **Reason:** setting a schema-1 or schema-2 receipt to 3 skips `update`'s `gov_oid` back-fill, which runs only below 3 since S4, so S9 would refuse that receipt forever — the reason §8 F4 gives for refusing the same lift in the up; and a non-number schema cannot be compared with 3 at all, so moving it would guess.
- **Evidence:** `check_receipt_schema`'s `[dSP-3 S6]` lines, run by this unit's probe: both verbs over a schema of `"4"` exited 1 with the receipt's bytes unchanged; this unit's acceptance ledger.
- **Risk:** stricter
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-3, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-3
