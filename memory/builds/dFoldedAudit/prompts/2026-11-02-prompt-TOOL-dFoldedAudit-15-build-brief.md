# Build brief — TOOL-dFoldedAudit-15

**Serves:** research TOOL-dFoldedAudit-15

Build this unit from `memory/builds/dFoldedAudit/spec/2026-11-02-spec-TOOL-dFoldedAudit-15.md`, its latest rev, and nothing else.

- Run no gate leg, no suite and no bar. Every `New arm:` RED-first is owed to the main loop at the close.
- Closing DIFF review behaviour stays byte-identical. Temp files go in the run's scratch root.
- A divergence from the spec stops the unit: return `DIVERGENCE:`, never improvise. A fixture's missing module or a declared-path gap the [refusals] tag of `memory/builds/dFoldedAudit/build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md` covers is not a divergence: fix it and say so in the return.
- Commit the CLOSED flip last, after every write under `tools/`. The write gate refuses a closed unit's next edit.
- This is one batch by M2's exception. Close each item or state in the return why its finding no longer stands.
- Also fix the comment on `read_spec_audit_switch` near `tools/unattended/unattended.sh:1297`: it says a spec exit and the chain verdict are the only readers, and `--plan --paths` and a folding `--record-round` read it too. Unit 13 could not after its CLOSED flip.
