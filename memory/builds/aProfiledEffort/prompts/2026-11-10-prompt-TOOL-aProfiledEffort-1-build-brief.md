# Brief — aProfiledEffort: build unit 1, the profile tables, their validation and the resolver

**Serves:** research TOOL-aProfiledEffort-1

## The brief

### Goal
The effort policy gains per-model profile tables, validated under R12 and resolved by model, with the fable profile seeded at medium. The design is `memory/builds/aProfiledEffort/spec/2026-11-10-spec-TOOL-aProfiledEffort-1.md`, read whole; this brief adds nothing to it.

### Items
1. Build every Scope item of the spec's §2, in the files its §4 names: `tools/roles/house/policy.toml`, `tools/roles/roles_lib.py`, `tools/roles/check_roles.py`, `tools/roles/render_agents.py` and `memory/map/generated/symbols.json`.

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
