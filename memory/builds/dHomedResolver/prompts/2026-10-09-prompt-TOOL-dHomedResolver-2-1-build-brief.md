# Build brief — TOOL-dHomedResolver-2

**Serves:** journal TOOL-dHomedResolver-2

Built INLINE by the main loop after unit 1, which also wrote `check-memory-hygiene.test.sh`, the
HYGIENE catalogue and the memory-tree README; this unit adds to all three, so it is sequenced. The
main loop has already read `cmd_check`, `cmd_write`, `collect()` and the hygiene suite's
`rotarchive` fixture.

Build exactly what the unit's spec states. Fast checks only inside the pass: the generator's new
arms through a probe importing the module, and the hygiene suite's `rotarchive` block through the
scratchpad probe, each against this code and against 5a836bf0. Nothing held. Temporary files go to
the session scratchpad.
