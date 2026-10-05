# Acceptance ledger — TOOL-aWardedAudit-5

**Serves:** journal TOOL-aWardedAudit-5

Built at `c47342a3`. The arms build a fresh graph with the grant-write builder; a slice ran against
the new checker and the base one, which reported nothing for either opt-in key.

**Evidences:** TOOL-aWardedAudit-5
- AC1 — `spec-audit:` — a run commit adding `spec-audit: 2026-10-05` to tOther3 named by check 19 with its commit and README
- AC2 — `SPEC_AUDIT_DEFAULT` — a run commit dating the default in `.unattended.conf` named by check 19; the blank-default commit not named
- AC3 — `spec-audit: 2026-10-05` — the owner's commit on main adding it to tOther named by nothing
