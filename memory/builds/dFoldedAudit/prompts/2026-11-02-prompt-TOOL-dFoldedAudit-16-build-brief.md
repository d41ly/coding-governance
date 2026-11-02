# Build brief — TOOL-dFoldedAudit-16

**Serves:** research TOOL-dFoldedAudit-16

Build this unit from `memory/builds/dFoldedAudit/spec/2026-11-02-spec-TOOL-dFoldedAudit-16.md`, its latest rev, and nothing else.

- Run no gate leg, no suite and no bar, except the two read-only commands the spec's criteria name, which are this unit's own observation.
- Behaviour stays byte-identical: each conversion is a no-fork form of the same value.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise.
- Commit the CLOSED flip last, after every write under `tools/`.
- An earlier stopped dispatch built and saved this unit's edits as `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-build-m4-spec-audit-694e7b/728ed75b-dc6d-443b-b1e2-72cabd3e91a1/scratchpad/TOOL-dFoldedAudit-16.patch`. Apply it and verify against the spec's latest rev.
