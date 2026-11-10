# Brief — aProfiledEffort: build unit 2, the handoff verbs take a model

**Serves:** research TOOL-aProfiledEffort-2

## The brief

### Goal
`handoff.py` answers a role's level and a workflow's stage levels for a named model, and unchanged for no model. The design is `memory/builds/aProfiledEffort/spec/2026-11-10-spec-TOOL-aProfiledEffort-2.md`, read whole; this brief adds nothing to it.

### Items
1. Build every Scope item of the spec's §2, in the files its §4 names: `tools/roles/handoff.py` and `tools/roles/adopt-roles.test.sh`.

### Acceptance
1. Each criterion of the spec's §6 that a probe or a fixture of the changed code can observe is observed in the pass and named in the return.
2. Each criterion only a gate, a suite or a new arm's RED-first run can observe is named in the return as owed to the main loop at the close.

### Gates
None in the pass. The legs of the spec's §7 run once, at the close, with the full bar.

### Non-goals
Everything the spec's §3 lists, and any file the spec's §4 does not name. Any kit version, which the lander's mint moves.

### Limitations
No gate, suite, self-test or bar runs in the pass. The spec is not edited beyond its status header at the build commit; a divergence is returned, not built. Every command is bounded.

### Reuse
The seams the spec's §10 names, extended in place.
