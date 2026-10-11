# Build brief — TOOL-dRemeasuredRender-1

**Serves:** journal TOOL-dRemeasuredRender-1

Built INLINE by the main loop, not through `tools/workflows/unattended-unit.js`: the build is three
units, the two govkit units share their files, and this unit's write set is mechanical, so the main
loop sequences all three in roster order, one commit each.

Build exactly what the unit's spec states. Apply the scanner's own printed remedy to each bare site,
and refuse any rewrite that changes a line beyond the scrub. Fast checks only inside the pass: the
no-registry scan, gov's own row, and `bash -n` over every touched suite. No merge bar and no suite
inside the pass; the touched suites outside `tools/unattended/` run once at the close, and the six
inside it are not run, under the owner's standing instruction. Temporary files go to the session
scratchpad.
