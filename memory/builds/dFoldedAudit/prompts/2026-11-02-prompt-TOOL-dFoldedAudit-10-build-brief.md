# Build brief — TOOL-dFoldedAudit-10

**Serves:** research TOOL-dFoldedAudit-10

Build this unit from `memory/builds/dFoldedAudit/spec/2026-11-02-spec-TOOL-dFoldedAudit-10.md`, its latest rev, and nothing else.

- Run no gate leg, no suite and no bar. Every `New arm:` RED-first is owed to the main loop at the close.
- Closing DIFF review behaviour stays byte-identical. Temp files go in the run's scratch root.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise. A fixture's missing module or a declared-path gap the [refusals] tag of `memory/builds/dFoldedAudit/build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md` covers is not a divergence: fix it and say so in the return.
- Commit the CLOSED flip last, after every write under `tools/`. The write gate refuses a closed unit's next edit.
- A round with no terminal row is attended, not forged.
