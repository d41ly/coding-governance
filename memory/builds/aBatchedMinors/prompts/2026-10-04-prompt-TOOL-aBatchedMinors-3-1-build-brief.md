# Build brief — TOOL-aBatchedMinors-3

**Serves:** journal TOOL-aBatchedMinors-3

Built INLINE by the main loop, not through `tools/workflows/unattended-unit.js`: units 2 and 3 share
the review row grammar and unit 4 documents both, so the passes are sequenced by hand in roster order
and each is one commit. The main loop has already read `verb_review` and check 2.

Build exactly what the unit's spec states, in `memory/builds/aBatchedMinors/spec/`. Fast checks
only inside the pass: the unit's own suite arms run as a slice, the parity or wiring check its gates
name, and `python tools/govkit/govkit.py epoch` at the last unit. Nothing held: no merge bar, no full
self-test suite — those run once, at VERIFYING. Observe every new refusal or clause RED against the
base code before it lands. Temporary files go to the session scratchpad.
