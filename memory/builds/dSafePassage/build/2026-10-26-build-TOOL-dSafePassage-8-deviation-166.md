# TOOL-dSafePassage-8 deviation 166 — the source walk derives its pending steps through the unchanged `derive_pending_steps`, which mints no source-mode branch

**Serves:** deviation TOOL-dSafePassage-8

- **Departs from:** TOOL-dSafePassage-8@rev-5 [§2 S1 "The walk", §4 Inventory]
- **Hand-off:** spec-to-code
- **Before:** `derive_pending_steps` "gains a source-mode branch: every declared step whose id `steps` does not hold as `applied`, in the brief's S5 order", and the Inventory mints that branch.
- **After:** no branch is added. Source mode calls `derive_pending_steps` as it stands, which already returns every row `read_steps` reads at `--to`, in its total order, minus each id the receipt records `applied`, and reads no vintage commit.
- **Cause:** builder discovery
- **Reason:** TOOL-dSafePassage-2 built the derivation vintage-free, so a source-mode branch would return what the existing body returns; a second spelling of one rule is the copy the reuse rule forbids, and YAGNI deletes it.
- **Evidence:** this unit's acceptance ledger, AC3 and AC8: a source receipt with no `steps` walked every declared id, and the re-run read `0 pending`.
- **Risk:** editorial
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-8, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-2
