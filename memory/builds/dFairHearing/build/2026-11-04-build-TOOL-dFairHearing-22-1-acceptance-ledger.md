# Acceptance ledger — TOOL-dFairHearing-22

**Serves:** journal TOOL-dFairHearing-22

Built against spec rev-4 and committed as the pass commit `a72758e14`, whose parent is `461ec9973`. The main loop drafted this ledger at the close from the builder return `2026-11-03-build-TOOL-dFairHearing-22-1-builder-return.md`, and every observation below is that return's. No suite, gate or bar ran in the pass: the checks were a scratch probe standing in for the `agent-cap self-test` leg, running copies of the hook and `scratch-guard.js` from a directory outside any checkout with `CLAUDE_PROJECT_DIR` unset. The `New arm:` line's red-first observation and the spec's legs are owed to the close.

**Evidences:** TOOL-dFairHearing-22
- AC1 — `govkit update --kits review-harness` — the copy with no pack exited 2, and its stderr named both `spec-audit-optin.js` and `govkit update --kits review-harness`. The hook as it stood at `461ec997` let the call through with exit 0. The spec's rev-2 edge hands this remedy string to unit 27
- AC2 — `kind: "diff-review"` — the hook exited 0 with the pack present, and 0 for a `kind: "diff-review"` call without it
- AC3 — `spec-audit-optin.js` — a `specAudit` call with no `kind` exited 2 against the copy with no pack, and the hook at `461ec997` let it through with exit 0. The return states the exit for this case, and describes the refusal as naming the pack's path without quoting this case's stderr for `spec-audit-optin.js`. At the tip a hook copy with no pack, over a `specAudit` call with no `kind` and with `roles` set, exited 2 and its stderr read `no workflows kit holding spec-audit-optin.js`
- AC4 — `grep -n "spec-audit-optin.js" tools/hooks/README.md` — its grep found the new README paragraph
