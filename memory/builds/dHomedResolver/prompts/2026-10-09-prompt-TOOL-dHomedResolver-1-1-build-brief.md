# Build brief — TOOL-dHomedResolver-1

**Serves:** journal TOOL-dHomedResolver-1

Built INLINE by the main loop, not through `tools/workflows/unattended-unit.js`: units 1 and 2 both
write `tools/memory-tree/check-memory-hygiene.test.sh` and the HYGIENE catalogue, so the passes are
not disjoint and are sequenced by hand in roster order, each one commit. The main loop has already
read check 10's loop, `check_rotation` and the cross-reader arm.

Build exactly what the unit's spec states. Fast checks only inside the pass: the new hygiene-suite
arms run as a hermetic slice of the suite's own setup, and `row_grammar.py --selftest`, each against
this code and against the code at 5a836bf0. Nothing held: no merge bar, no full suite. Temporary
files go to the session scratchpad.
