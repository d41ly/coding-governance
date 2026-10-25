# TOOL-dGroundRules-25 deviation 76 — one spec-token waiver row, re-keyed, holds the guards hit the import widening of policy fixtures makes on another build's live spec

**Serves:** deviation TOOL-dGroundRules-25

- **Departs from:** TOOL-dRetiredFork-20@rev-2 [spec-token waivers]
- **Hand-off:** spec-to-code
- **Before:** `memory/project/spec-token-waivers.txt` holds 34 rows in 42 lines and declares itself SHRINK-ONLY: the count may fall, never rise. Its row keyed `policy fixtures <- tools/roles/kit.toml` holds the one `[guards]` hit TOOL-dGroundRules-23's widening made on aScoutedSeam's TOOL-1.
- **After:** that row is re-keyed `policy fixtures <- tools/roles/roles_lib.py` and holds the same one hit, which TOOL-dGroundRules-25's guard widening now names through `roles_lib.py`; the count stays 34 rows in 42 lines, so the shrink-only count F7 allowed to rise does not move. Ask `TOOL-dGroundRules-110` already asks that spec to carry `policy fixtures` in its §7, which deletes the row.
- **Cause:** builder discovery
- **Reason:** S24 adds to the `policy fixtures` guard in `tools/gate-legs.json` each in-kit module a Python census enforcer imports and each in-kit file a shell enforcer sources, because an edit to one changes what the `budgets-cap-` cases run; `check_roles.py` and `handoff.py` import `roles_lib.py`. The guards join of `tools/check-spec-tokens.py` reports one hit per missing leg per spec, its token naming the FIRST declared path that trips the leg, and TOOL-aScoutedSeam-1's files touched list `roles_lib.py` before `kit.toml`: so the widening re-keys the existing hit rather than adding one, the kit.toml row reads `STALE WAIVER` (a stale row reds), and §4's added row with a count of 35 would have red the checker. §8 F7 refused the other two options: leaving the module out lets an edit to it skip the leg whose census case runs its importers, the gap finding 41 names, and revising that spec's §7 is an outside write this build's README refuses.
- **Evidence:** `python tools/check-spec-tokens.py --dispatch` over the widened guard with both rows exited 1 printing `STALE WAIVER policy fixtures <- tools/roles/kit.toml — no spec produces this hit any more`; with the row re-keyed it exited 0, `0 unwaived` hits; `grep -vc "^#" memory/project/spec-token-waivers.txt` printed 34.
- **Risk:** editorial
- **Approver:** author, the run's main loop citing ER:388 (`PLAY-dClosedLoop-6`), recorded in TOOL-dGroundRules-25 §8 F7
- **Follow-through:** ask TOOL-dGroundRules-110
- **Caused-by:** TOOL-dGroundRules-25
- **Bound:** spec-token-waivers shrink-only count
- **Tier:** middle
- **Surface:** memory/project/spec-token-waivers.txt
