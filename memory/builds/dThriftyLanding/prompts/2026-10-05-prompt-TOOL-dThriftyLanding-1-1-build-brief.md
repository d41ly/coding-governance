# Build brief — TOOL-dThriftyLanding-1

**Serves:** journal TOOL-dThriftyLanding-1

Built INLINE by the main loop, not through `tools/workflows/unattended-unit.js`: units 1 to 3 share
`tools/run-gates/run-gates.sh` and `.githooks/pre-push`, so the passes are not disjoint and are
sequenced by hand in roster order, each one commit. The main loop has already read the runner's row
parser, its guard pass, `report_one` and the stamp block.

Build exactly what the unit's spec states, in `memory/builds/dThriftyLanding/spec/`. Fast checks only
inside the pass: a fixture bar in the scratchpad, and the canary's arms run as a slice. Nothing held:
no merge bar, no full self-test suite — those run once, at VERIFYING. Observe every new skip and
refusal RED against the base runner before it lands. Temporary files go to the session scratchpad.
