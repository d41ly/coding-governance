# TOOL-dWitnessedBar-10 deviation 102 — the pass-leg cost read takes each leg's maximum across node rows

**Serves:** deviation TOOL-dWitnessedBar-10

- **Departs from:** `TOOL-dWitnessedBar-10@rev-5 [S6]`
- **Hand-off:** spec-to-code
- **Before:** S6 keys `ceiling-evidence.txt` by `(leg, node)`, and §4 "Evidence keyed by node" names the runner's prior read as the one other reader, already taking each leg's maximum. `tools/run-gates/pass_legs.py` is not in Files touched.
- **After:** `pass_legs.py`'s `read_ceilings` keeps the largest reading per leg across its rows, where it kept the last row it read; `derive-ceilings.py --check` hands the pass-budget arm the same per-leg maxima.
- **Cause:** builder discovery
- **Reason:** `read_ceilings` is a by-value reader of the evidence file keyed by leg: it feeds the pass-budget gate and the `pass_leg` render in `leg_factory.py`. With one row per node, last-wins reads whichever node sorts last, not the leg's maximum its docstring and the README call its cost. At landing every leg carries one row, so no value moves; the fix keeps the cost from depending on the second node's tag once a second node writes.
- **Evidence:** `tools/run-gates/pass_legs.py#read_ceilings`, its callers `derive_pass_legs` and `check_pass_budget`, and `tools/run-gates/leg_factory.py#render_manifest`.
- **Risk:** stricter
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** PLAY-dClosedLoop-2
