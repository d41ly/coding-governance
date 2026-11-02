# Build brief — TOOL-dFoldedAudit-3

**Serves:** research TOOL-dFoldedAudit-3

Build this unit from `memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-3.md`, its latest rev, and nothing else. The design it derives from is `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md`; where the two differ the spec wins.

- Run no gate leg, no suite and no bar. Stage a new refusal's RED with the one test file you write, directly, only if the spec's arm is yours to observe; every `New arm:` is otherwise owed to the main loop at the close.
- Closing DIFF review behaviour stays byte-identical. Every change sits on the spec subject's branch.
- Temp files go in the run's scratch root, never under the repo.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise.
- Regenerate `tools/workflows/unattended-build.js` from its template by the kit's render, never by hand.
