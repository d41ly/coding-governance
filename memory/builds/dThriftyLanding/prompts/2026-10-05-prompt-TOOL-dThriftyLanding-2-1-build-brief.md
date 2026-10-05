# Build brief — TOOL-dThriftyLanding-2

**Serves:** journal TOOL-dThriftyLanding-2

Built INLINE by the main loop, sequenced after unit 1 because both edit `tools/run-gates/run-gates.sh`
and before unit 3 because both edit `.githooks/pre-push`. The main loop has already read the stamp
block and the hook's record read and `check_green_record`.

Build exactly what the unit's spec states. Fast checks only inside the pass: a scratch clone with a
linked worktree, driven through the hook with a stub bar. Nothing held: no merge bar, no full
self-test suite. Observe each new arm RED against the base hook and runner first. Temporary files go
to the session scratchpad; a fixture clone goes under a short %TEMP% path.
