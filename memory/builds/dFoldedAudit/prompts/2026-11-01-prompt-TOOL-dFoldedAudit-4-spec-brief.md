# Spec brief — TOOL-dFoldedAudit-4: a repair unit edits its unbuilt sibling's spec with a rev bump

**Serves:** research TOOL-dFoldedAudit-4

Write this unit's spec at Tier-2 from `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md`, tags [repair]. Those tags are decided: state them exactly, and resolve only what they mark DERIVE. Take the seams and citations from `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-1-orient-enforcement.md`, and verify each cited line against the file before you rely on it.

- Header: `order 40`. Status OPEN.
- Files this unit writes: tools/workflows/unattended-build.template.js, the rendered harness, its suite, the class gate's home.
- Acceptance: the matching line of the brief's `### Acceptance`, in `memory/builds/dFoldedAudit/prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md`, as observable arms, each with a `New arm:` line.
- Reads no other unit's unbuilt output except through the [order] tag; declare those edges in §3.
