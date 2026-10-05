# Acceptance ledger — TOOL-aWardedAudit-1

**Serves:** journal TOOL-aWardedAudit-1

Built at `1872bdfe`. The arms sit in the second-anchor block of the driver suite; a slice of them
ran against the new driver and against the base driver, which opted the run in on AC1 to AC3.

**Evidences:** TOOL-aWardedAudit-1
- AC1 — `--preflight` — over a prompt README carrying `spec-audit: 2026-10-05`, refused at check 89 naming mode prompt; no RUN.md created
- AC2 — `recipe` — the same README under recipe refused at check 89, and the missing-playbook refusal not printed
- AC3 — `SPEC_AUDIT_DEFAULT` — committed only on the pushed run branch: preflight OK, `not owed`, no spec-audit fact pinned
- AC4 — `opted in by project default` — printed with the default landed on main and the prompt README on the run branch
- AC5 — `recommend spec-audit:` — absent; the two-unit and FORKED arms read the owner-addressed clause instead
- AC6 — `opted in by README spec-audit: 2026-09-20` — the existing slug-README arm, unchanged, passes against the new driver
