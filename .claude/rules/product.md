---
paths:
  - "tools/**"
  - "skills/**"
  - "coding-governance-agents.template.md"
  - "WIRE-INTO-PROJECT.md"
---

# What ships here — the product, loaded when you open a product file

- **`coding-governance-agents.template.md`** — the charter template, v4.0: three sections of
  one-line rules. Section 1 is the governing practices every adopter shares; section 2 is the
  adopter's own `[charter] adopter_rules`; section 3 is generated — the node registry from
  `tools/playbook/fleet.toml`, the tools and protocols of the selected kits, the deploy answers, and
  the micro-formats. `tools/playbook/` renders it, grades every one-line region, and drops the
  `kit:`/`when:` blocks a target has no kit for. Size is gated by `tools/check-template-size.sh`
  against a recorded high-water.
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
  mandate, the charter's `[land]` substitute),
  `agent-instructions/`, `pytest-parallel-guardrails/` (bounded,
  attributable pytest-xdist runs: the four-knob ini recipe, the crashprobe worker-death
  attribution plugin, the aiosqlite closed-loop seam patch + forced-race gate), the
  `check-template-size.sh` gate, and `check-wiring.sh` (detects/auto-wires
  installed-but-unwired tools; SessionStart-driven).
- **`WIRE-INTO-PROJECT.md`** — the agent runbook for wiring the whole chain into a target repo.

- Kits live in `tools/`; the session-kickoff skill stays at `skills/` (machine-junction discovery).
- The template holds practices, never procedures: a rule that needs more than one line belongs in the
  tool, gate or protocol that enforces it, and the template points there.
