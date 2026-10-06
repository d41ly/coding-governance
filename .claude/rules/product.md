---
paths:
  - "tools/**"
  - "skills/**"
  - "coding-governance-agents.template.md"
  - "WIRE-INTO-PROJECT.md"
---

# What ships here — the product, loaded when you open a product file

- **`coding-governance-agents.template.md`** — the governance playbook template (the operating
  ruleset; **≤48 KiB, gated** by `tools/check-template-size.sh`, which also prices every growth
  against a recorded high-water — prefer externalizing to spending the headroom). **ONE file as of
  v3.0**: the activity-scoped checklists that used to sit in a prose companion converged into the
  charter, and the deploy-time placeholder catalog became a program — `tools/playbook/`, whose
  renderer fills every placeholder from the target's `deploy.toml` and drops the `kit:`/`when:`
  conditional blocks that target has no kit for.
- **`skills/session-kickoff/`** — the `/session-kickoff` engine + `MANIFEST-TEMPLATE.md` + the
  ratchet gate `manifest-check.sh` (+ its test). Installed per-machine via a junction (not in-repo).
- **`tools/`** — `lib/resolve-python.sh` (the one python-launcher resolver: it RUNS the candidate,
  because the MS-Store `python3` stub answers `command -v` and exits 9009) plus the copy-in kits:
  `memory-tree/`, `memory-recall/` (offline conf-driven retrieval
  over the memory tree + the rendered recall Skill and its opt-in `recall-opened` hook),
  `codebase-map/`, `drift-audit/` (does this repo's own RECORD of its state still match reality —
  stdlib+git, seconds, no agents; every signal carries a liveness assertion so a probe
  that cannot move prints DEAD PROBE instead of a reassuring 0), `hooks/agent-cap.js` (the fan-out guard: raw-primitive ban + the verifier-arity rule it resolves),
  `workflows/tier2-review.js`, `workflows/drift-audit-{code,state}.js`,
  `unattended/` (the unattended-run kit: the binding protocol, the four-verb driver, and the leg that
  reads the project's `.unattended.conf` declarations rather than restating them — a run that will
  merge and push with no owner turn replaces the explicit-ask checkpoint with a committed standing
  mandate, §1 Landing's one substitute),
  `agent-instructions/`, `pytest-parallel-guardrails/` (bounded,
  attributable pytest-xdist runs: the four-knob ini recipe, the crashprobe worker-death
  attribution plugin, the aiosqlite closed-loop seam patch + forced-race gate), the
  `check-template-size.sh` gate, and `check-wiring.sh` (detects/auto-wires
  installed-but-unwired tools; SessionStart-driven).
- **`WIRE-INTO-PROJECT.md`** — the agent runbook for wiring the whole chain into a target repo.

- Kits live in `tools/`; the session-kickoff skill stays at `skills/` (machine-junction discovery).
- The template is the operating ruleset — keep it ≤48 KiB; anything activity-scoped or one-time goes
  in a companion, not the template.
