# Build brief — TOOL-dSweptBranches-1

**Serves:** journal TOOL-dSweptBranches-1

Built INLINE by the main loop, not through `tools/workflows/unattended-unit.js`: units 1 to 4 write
one CLI, so the main loop sequences all five in roster order, one commit each, and a cold agent per
unit would re-derive what the loop already holds.

Build exactly what the unit's spec states: the kit directory, the inlined remote ladder, the
inventory, the report and the stub seam, plus the kit's carriers. Verdicts stay `UNKNOWN` here.
Fast checks only inside the pass: the kit self-test run directly, `govkit selfcheck`, the kit
version check and the codebase-map check. No merge bar inside the pass. Temporary files go to the
session scratchpad.
