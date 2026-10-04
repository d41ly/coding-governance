# Build brief — TOOL-aWindowedPass-4

**Serves:** journal TOOL-aWindowedPass-4

Built INLINE by the main loop, not through `tools/workflows/unattended-unit.js`: every unit of this
build writes `tools/unattended/`, and four write `lib-unattended.sh` or `check-unattended.sh`, so the
passes are sequenced by hand in the spec order and each is one commit carrying a `Pass:` trailer.

Build exactly what the unit's spec states, in `memory/builds/aWindowedPass/spec/`. Fast checks only
inside the pass: the unit's own arms run as a slice of their suite, and `govkit selfcheck` where the
unit touches a descriptor. Nothing held: no merge bar and no whole suite, which run once at VERIFYING.
Observe every new arm RED on a staged break before it lands. Declare every generated write the
pre-commit hook forces in the pass's `--dispatch`. Temporary files go to the session scratchpad.
