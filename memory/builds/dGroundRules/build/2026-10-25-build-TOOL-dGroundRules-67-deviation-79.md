# TOOL-dGroundRules-67 deviation 79 — one spec-token waiver row, re-keyed, holds the guards hit the guard-trace sweep of policy fixtures makes on another build's live spec

**Serves:** deviation TOOL-dGroundRules-67

- **Departs from:** TOOL-dRetiredFork-20@rev-2 [spec-token waivers]
- **Hand-off:** spec-to-code
- **Before:** `memory/project/spec-token-waivers.txt` holds 33 rows in 41 lines and declares itself SHRINK-ONLY: the count may fall, never rise. Its row keyed `policy fixtures <- tools/roles/roles_lib.py` holds the one `[guards]` hit TOOL-dGroundRules-25's widening made on aScoutedSeam's TOOL-1.
- **After:** that row is re-keyed `policy fixtures <- tools/workflows/kit.toml` and holds the same one hit, which TOOL-dGroundRules-67's guard sweep now names through that descriptor; the count stays 33 rows in 41 lines. Ask `TOOL-dGroundRules-110` already asks that spec to carry `policy fixtures` in its §7, which deletes the row.
- **Cause:** builder discovery
- **Reason:** deviation 78 left for the close the sweep that adds to the `policy fixtures` guard every path the full `--fixture` run's guard trace reports outside it; `tools/workflows/kit.toml` is one of the twelve. The guards join of `tools/check-spec-tokens.py` names a spec's first declared path per missing leg, and TOOL-aScoutedSeam-1's files touched list `tools/workflows/kit.toml` before `roles_lib.py`, so the sweep re-keys the existing hit rather than adding one, and the `roles_lib.py` row would read `STALE WAIVER`. Revising that spec's §7 is an outside write this build's README refuses.
- **Evidence:** the measurement in TOOL-dGroundRules-67 §4 "The waiver", which reads the guards join's own functions over every live spec before and after the sweep; `python tools/check-spec-tokens.py` over the built tree, `0 unwaived`; `grep -vc "^#" memory/project/spec-token-waivers.txt` printing 33.
- **Risk:** editorial
- **Approver:** author, the run's main loop citing ER:388 (`PLAY-dClosedLoop-6`), recorded in TOOL-dGroundRules-67 §4
- **Follow-through:** ask TOOL-dGroundRules-110
- **Caused-by:** TOOL-dGroundRules-67
- **Bound:** spec-token-waivers shrink-only count
- **Tier:** middle
- **Surface:** memory/project/spec-token-waivers.txt
