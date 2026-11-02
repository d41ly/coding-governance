# Build brief — TOOL-dFoldedAudit-7

**Serves:** research TOOL-dFoldedAudit-7

Build this unit from `memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-7.md`, its latest rev, and nothing else. The design it derives from is `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md`; where the two differ the spec wins.

- Run no gate leg, no suite and no bar. Stage a new refusal's RED with the one test file you write, directly, only if the spec's arm is yours to observe; every `New arm:` is otherwise owed to the main loop at the close.
- Closing DIFF review behaviour stays byte-identical. Every change sits on the spec subject's branch.
- Temp files go in the run's scratch root, never under the repo.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise.
- `SPEC_FOLD_CUTOFF` stays blank here; the close writes its value, the day after the newest old-contract record.
- An earlier stopped dispatch built and saved the driver half as `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-build-m4-spec-audit-694e7b/728ed75b-dc6d-443b-b1e2-72cabd3e91a1/scratchpad/dfa7-driver-half.patch`. Apply it instead of rewriting it, then verify it against this spec's latest rev before relying on it.
