# Build brief — TOOL-dFoldedAudit-6

**Serves:** research TOOL-dFoldedAudit-6

Build this unit from `memory/builds/dFoldedAudit/spec/2026-11-01-spec-TOOL-dFoldedAudit-6.md`, its latest rev, and nothing else. The design it derives from is `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md`; where the two differ the spec wins.

- Run no gate leg, no suite and no bar. Stage a new refusal's RED with the one test file you write, directly, only if the spec's arm is yours to observe; every `New arm:` is otherwise owed to the main loop at the close.
- Closing DIFF review behaviour stays byte-identical. Every change sits on the spec subject's branch.
- Temp files go in the run's scratch root, never under the repo.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise.
- A live run claim on dRankedPlan, dFurnishedOrders or dDeclaredLoop at this pass is a park, not a write. Read `unattended.sh --claims` first.
