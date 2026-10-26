# TOOL-dGroundRules-18 deviation 73 — a spec-token waiver row holds the guards hit the policy fixtures widening makes on another build's live spec

**Serves:** deviation TOOL-dGroundRules-18

- **Departs from:** TOOL-dRetiredFork-20@rev-2 [spec-token waivers]
- **Hand-off:** spec-to-code
- **Before:** `memory/project/spec-token-waivers.txt` holds 28 rows in 36 lines and declares itself SHRINK-ONLY: the count may fall, never rise.
- **After:** one token row, `policy fixtures <- tools/workflows/unattended-build.template.js`, holds the `[guards]` hit TOOL-dGroundRules-18's guard widening makes on `TOOL-aOrientedCast-28`'s live spec; the count is 29 rows in 37 lines. Ask `TOOL-dGroundRules-109` in dGroundRules' `BACKLOG.md` asks that unit's §7 to carry `policy fixtures`, which deletes the row.
- **Cause:** builder discovery
- **Reason:** the `limit-hook-writer-split` case renders `tools/workflows/unattended-build.template.js`, so the `policy fixtures` guard in `tools/gate-legs.json` gains that template, and the guards join of `tools/check-spec-tokens.py` reds `TOOL-aOrientedCast-28` (OPEN), whose files touched list the template while its §7 lacks the leg. §8 F2 refused the other two options: handing the guard to TOOL-dGroundRules-20 lands this unit's template change unguarded, and revising `TOOL-aOrientedCast-28`'s §7 is an outside write this build's README refuses. The waiver raise trips only the registry's own declared count, so the standing ruling takes it, as it took TOOL-dGroundRules-10's and dTrueNorth's rows.
- **Evidence:** the first build of this unit measured the hit: with the guard widened and no row, the next `--dispatch` refused on one unwaived `[guards]` hit on `TOOL-aOrientedCast-28`; `memory/project/spec-token-waivers.txt` at 37 lines after this unit's edit.
- **Risk:** loosening
- **Approver:** author, the run's main loop citing ER:388 (`PLAY-dClosedLoop-6`), recorded in TOOL-dGroundRules-18 §8 F2
- **Follow-through:** ask TOOL-dGroundRules-109
- **Caused-by:** TOOL-dGroundRules-18
- **Bound:** spec-token-waivers shrink-only count
- **Tier:** middle
- **Surface:** memory/project/spec-token-waivers.txt
