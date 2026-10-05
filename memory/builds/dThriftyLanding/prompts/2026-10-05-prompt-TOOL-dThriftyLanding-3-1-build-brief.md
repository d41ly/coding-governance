# Build brief — TOOL-dThriftyLanding-3

**Serves:** journal TOOL-dThriftyLanding-3

Built INLINE by the main loop, sequenced after units 1 and 2: it hands the runner the knob unit 1 reads
and edits the `.githooks/pre-push` decision block unit 2 changed. The main loop has already read the
decision block, `read_policy_key` and `check_green_record`.

Build exactly what the unit's spec states. Fast checks only inside the pass: scratch clones
driven through the hook with a stub bar that prints what it received. Nothing held: no merge bar, no full
self-test suite. Observe each new arm RED against the base hook and runner first. Temporary files go
to the session scratchpad; a fixture clone goes under a short %TEMP% path.
