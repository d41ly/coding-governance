# Build brief — TOOL-aWindowedPass-6

**Serves:** journal TOOL-aWindowedPass-6

Built INLINE by the main loop, not through `tools/workflows/unattended-unit.js`, for the reason the
other five briefs give: every unit of this build writes `tools/unattended/`, and this one writes the
driver's `verb_check_commit`, which unit 3 built and the round-1 fold changed.

Build exactly what the unit's spec states, in `memory/builds/aWindowedPass/spec/`. Fast checks only
inside the pass: the unit's own arms run as a slice of `unattended.test.sh`. Nothing held: no merge
bar and no whole suite, which run once at VERIFYING. Observe every new arm RED on a staged break before
it lands. Declare every generated write the pre-commit hook forces in the pass's `--dispatch`.
Temporary files go to the session scratchpad.
