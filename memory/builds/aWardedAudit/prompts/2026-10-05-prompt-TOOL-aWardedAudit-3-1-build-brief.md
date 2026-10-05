# Build brief — TOOL-aWardedAudit-3

**Serves:** journal TOOL-aWardedAudit-3

Built INLINE by the main loop, not through `tools/workflows/unattended-unit.js`: unit 2 reads the
run-state fact unit 1 decides, and unit 3 documents both, so the passes are sequenced by hand in
roster order and each is one commit. The main loop has already read `check_authorization` and rule 0.

Build exactly what the unit's spec states, in `memory/builds/aWardedAudit/spec/`. Fast checks only
inside the pass: the unit's own suite arms run as a slice, the parity or wiring check its gates name.
Nothing held: no merge bar, no full self-test suite — those run once, at VERIFYING. Observe every new
refusal RED against the base code before it lands. Temporary files go to the session scratchpad.
