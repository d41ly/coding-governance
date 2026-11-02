# Build brief — TOOL-dFairHearing-40

**Serves:** research TOOL-dFairHearing-40

Build this unit from `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-40.md`, its latest rev, and nothing else. The packet `memory/builds/dFairHearing/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md` is the chain context the spec was written from; where the two differ the spec wins.

- This is the build run of dFairHearing: every unit was specced and audited by the spec run, and the owner stopped the spec-audit chain after round 5 (`memory/builds/dFairHearing/prompts/2026-10-23-prompt-TOOL-dFairHearing-1-owner-stop-reviews.md`), so no spec is re-audited before it is built.
- Units ahead of this one in the build order are built; verify each line the spec cites against the file before relying on it, since earlier units moved them.
- Run no gate leg, no suite and no bar. Every `New arm:` line is owed to the main loop at the close.
- Declare with `--dispatch` every path the commit will carry, the generated renders a hook forces into it included (`memory/LIVE.md`, this build's `README.md` and `RUN.md`, the codebase map's `symbols.json` when a shell or Python definition moves).
- Writes stay inside the spec's files touched and this build's folder; a write outside both is a departure, recorded or returned.
- Temp files go in the run's scratch root, never under the repo.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise.
