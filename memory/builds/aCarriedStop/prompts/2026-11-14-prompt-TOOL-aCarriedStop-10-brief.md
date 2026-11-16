# Brief — aCarriedStop: unit 10, the chain-packet door's kit-path spellings routed through the resolver

**Serves:** research TOOL-aCarriedStop-10

Adopted at once under M10 on the third close of 2026-11-14, which the install-prefix leg blocked; the owner's order "raise the routed-commits ceiling and land it" stands as the mandate.

## The prompt

> raise the routed-commits ceiling and land it

## The brief

### Goal
The leg `install-prefix (shipped surface)` exits 0 on this build's tree, so the close's bar and the push bar can land it.

### Items
1. `tools/chain-packet.py` reaches the memory-tree kit's `tree_lib.py` through the canonical `resolve_kit_dir` block, never through a spelled `"memory-tree"` path segment [planned TOOL-aCarriedStop-10]
2. `tools/chain-packet.test.sh` loads `tree_lib` through the door's resolved kit directory, never through a spelled `"memory-tree"` path segment [planned TOOL-aCarriedStop-10]

### Acceptance
- `bash tools/check-install-prefix.sh` exits 0 and lists no line of `tools/chain-packet.py` or `tools/chain-packet.test.sh`.
- The same checker run at the parent's tree lists the three lines and exits 1.
- With the kit absent from beside the door, the door still prints its `shortcuts off` line and runs the instrument as it stands.

### Gates
The merge bar at the close; `bash tools/check-install-prefix.sh` in the pass.

### Non-goals
- No change to what the door reads, batches or prints, beyond how it finds the kit.
- No change to `tools/check-install-prefix.sh` or to any other kit's spellings.
- No path under `memory/builds/aBatchedPacket/` or `memory/builds/dDeclaredLoop/`.

### Limitations
- The red is inherited: `bash tools/check-install-prefix.sh` at origin/main `0578adb73` lists the same three lines and exits 1.
- The bar reads it OWN only because its grader sits directly under `tools/`, so this build's edit to `tools/gate-legs.json` touches its comparator.

### Reuse
- The `resolve_kit_dir` block, byte-identical to `tools/lib/resolve_kit_dir.py` and gated, as `tools/check-spec-tokens.py` carries it for the same kit.

## Drawn from the session

- The third close's bar at `1f732d9ba` and the checker's run at `0578adb73`, both taken by the main loop of this session.

## Owner confirmation

The order is the owner's own words in chat; nothing else was asked.
