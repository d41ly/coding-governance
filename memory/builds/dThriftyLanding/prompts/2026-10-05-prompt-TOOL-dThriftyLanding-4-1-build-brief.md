# Build brief — TOOL-dThriftyLanding-4

**Serves:** journal TOOL-dThriftyLanding-4

Built INLINE by the main loop, sequenced after unit 1, whose runner version is the floor this unit
reads, and before unit 5, whose descriptor values this unit carries. The main loop has already read
`write_gate_legs`, `check_target_reads_subject` and selfcheck 7h.

Build exactly what the unit's spec states. Fast checks only inside the pass: a probe importing the module
directly, and one selfcheck over this tree with a planted disagreement. Nothing held: no merge bar, no full
self-test suite. Observe each new arm RED against the base module first. Temporary files go
to the session scratchpad.
