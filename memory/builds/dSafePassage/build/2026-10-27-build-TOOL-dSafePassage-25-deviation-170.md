# TOOL-dSafePassage-25 deviation 170 — the prepared path cleans against the snapshot TOOL-dSafePassage-8 already takes before the walk, kept alive across the regeneration

**Serves:** deviation TOOL-dSafePassage-25

- **Departs from:** TOOL-dSafePassage-25@rev-2 [§2 S1, §4 "The prepared path after this unit", §4 Inventory]
- **Hand-off:** spec-to-code
- **Before:** `cmd_prepare` takes a fresh `gfsnap` before `run_gov_first`, removes it with `rm -f` on the walk's success, and refuses with the line "the steps this landing introduces could not be run on gov first (named above)"; the Inventory mints `gfsnap` and that line.
- **After:** `cmd_prepare` keeps the `rgsnap` TOOL-dSafePassage-8 already takes before `run_gov_first`; the walk's refusal now runs `remove_new_untracked "$rgsnap"` before `rm -f`, and a success keeps it for the regeneration's refusal, removed after it. The refusal keeps TOOL-dSafePassage-8's line, "the upgrade steps this landing declares did not hold on gov first (named above)". The attended path mints `gfsnap` as S2 says, under the same kept line.
- **Cause:** builder discovery
- **Reason:** at this branch's HEAD the snapshot S1 adds already exists, taken before the walk (`tools/push-main.sh` cmd_prepare, TOOL-dSafePassage-8 S4); a second identical snapshot is the copy the reuse rule forbids, and removing it at the walk's success would leave the regeneration's refusal blind to the receipt, the defect TOOL-dSafePassage-27 repairs. The refusal's text is not what any AC observes, and renaming it moves nothing an adopter reads.
- **Evidence:** this unit's acceptance ledger, AC1 to AC3: the fixture with the planted failing witness prints an empty `git status --porcelain` after the refusal and the retry exits 0, where the lander at the base leaves `?? .governance/install.json` and the retry exits 1.
- **Risk:** editorial
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-25, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-27
- **Caused-by:** TOOL-dSafePassage-8
