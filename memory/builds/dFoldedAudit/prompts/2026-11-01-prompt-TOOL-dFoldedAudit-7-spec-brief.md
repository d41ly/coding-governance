# Spec brief — TOOL-dFoldedAudit-7: policy keys switch the disposal, the stop and the ceiling

**Serves:** research TOOL-dFoldedAudit-7

Write this unit's spec at Tier-2 from `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md`, tags [switches], [cutoff]. Those tags are decided: state them exactly, and resolve only what they mark DERIVE. Take the seams and citations from `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-1-orient-enforcement.md`, and verify each cited line against the file before you rely on it.

- Header: `order 10`. Status OPEN.
- Files this unit writes: tools/policy/catalogue.toml and its siblings, .unattended.conf, tools/unattended/.unattended.conf.example, the conf loader in tools/unattended/unattended.sh.
- Acceptance: the matching line of the brief's `### Acceptance`, in `memory/builds/dFoldedAudit/prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md`, as observable arms, each with a `New arm:` line.
- Reads no other unit's unbuilt output except through the [order] tag; declare those edges in §3.
