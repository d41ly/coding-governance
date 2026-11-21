# TOOL-dWitnessedBar-40 deviation 403 — `GATE_BASE_FROM` joins the pre-push suite's inert knob class

**Serves:** deviation TOOL-dWitnessedBar-40

- **Departs from:** `TOOL-dWitnessedBar-40@rev-6`
- **Hand-off:** spec-to-code
- **Before:** S2 mints the runner knob `GATE_BASE_FROM` and has the hook export it, and names no push-boundary class for it; S4's suite change is the per-tree plant's two reuse keys alone.
- **After:** `.githooks/pre-push.test.sh` adds `GATE_BASE_FROM` to `BAR_INERT_KNOBS`, with a line in the class comment saying why it is inert: read once and unset before any leg, exported `inherited` by the hook on the inherited-green path, and able only to stop a scoped run writing its per-tree verdict.
- **Cause:** builder discovery
- **Reason:** the bug-class checklist over the pass commit selected `a-runner-knob-owes-a-push-class`: the suite's H49 class arm reds `unclassified-or-twice GATE_BASE_FROM (0)` on any runner knob in no class. A caller's value can only decline a record, which costs a saving and never a leg or a verdict, so it is inert rather than scrubbed; scrubbing it would also put it on the hook's `BAR_SCRUBBED_KNOBS`, whose parity arm in the unattended suite would red against the driver's list that `TOOL-dWitnessedBar-60` owns.
- **Evidence:** `.githooks/pre-push.test.sh#check_knob_classes` extracted alone printed nothing over this tree's runner, and `unclassified-or-twice GATE_BASE_FROM (0)` with the name taken out of the class.
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dWitnessedBar-31
- **Caused-by:** TOOL-dWitnessedBar-40
