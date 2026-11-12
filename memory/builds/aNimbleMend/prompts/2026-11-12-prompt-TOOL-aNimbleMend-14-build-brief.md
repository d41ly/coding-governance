# Brief — aNimbleMend: build unit 14, the red-fix lane opens only on a red of this branch's present state: an open red is bounded by its row's own head

**Serves:** research TOOL-aNimbleMend-14

## The brief

### Goal
Build `TOOL-aNimbleMend-14` as its spec states it. The design is `memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-14.md`, read whole; this brief adds nothing to it.

### Items
1. Build every Scope item of the spec's §2, in the files its §4 names under "Files touched".

### Acceptance
1. Each criterion of the spec's §6 that a probe or a fixture of the changed code can observe is observed in the pass and named in the return.
2. Each criterion only a gate, a suite or a new arm's RED-first run can observe is named in the return as owed to the main loop at the close.

### Gates
None in the pass. The legs of the spec's §7 run once, at the close, with the full bar.

### Non-goals
Everything the spec's §3 lists, and any file the spec's §4 does not name. Any kit version, which the lander's mint moves.

### Limitations
No gate, suite, self-test or bar runs in the pass. The spec is not edited beyond its status header at the build commit; a divergence is returned, not built. Every command is bounded. The spec commit is already made, so the pass commits code after it.

### Reuse
The seams the spec's §10 names, extended in place.
