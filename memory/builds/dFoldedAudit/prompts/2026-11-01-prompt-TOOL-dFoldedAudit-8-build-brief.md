# Build brief — TOOL-dFoldedAudit-8

**Serves:** research TOOL-dFoldedAudit-8

Build this unit from `memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-8.md`, its latest rev, and nothing else. The design it derives from is `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md`; where the two differ the spec wins.

- Run no gate leg, no suite and no bar. Stage a new refusal's RED with the one test file you write, directly, only if the spec's arm is yours to observe; every `New arm:` is otherwise owed to the main loop at the close.
- Closing DIFF review behaviour stays byte-identical. Every change sits on the spec subject's branch.
- Temp files go in the run's scratch root, never under the repo.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise.
- This is a gov-spec-writer pass run outside the unit harness. Re-read `unattended.sh --claims` first; a live claim on dDeclaredLoop or dFairHearing is a park.
