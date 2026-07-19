# coding-governance — working guide

Project-agnostic governance + tooling for running Claude Code (or any agent) across several
machines/sessions on one repo. This repo **dogfoods its own kits**: it runs the memory-tree hygiene
gate, the kickoff-manifest ratchet, and the template size gate on itself.

*(Read by every AI tool: `AGENTS.md` is canonical; `CLAUDE.md` is a `@AGENTS.md` import — Claude Code
doesn't read AGENTS.md natively. Wired by `tools/agent-instructions/`.)*

## What ships here (the product)

- **`parallel-coding-governance.template.md`** — the governance playbook template (the operating
  ruleset; **≤32 KiB, strictly gated** by `tools/check-template-size.sh` — trim or externalize, never
  raise the limit). Companions: `.customize.md` (deploy-time placeholder catalog) and `.domain-rules.md`
  (the §4/§9/§10/§11/§12/§13 activity-scoped checklists the template references by §-stub).
- **`skills/session-kickoff/`** — the `/session-kickoff` engine + `MANIFEST-TEMPLATE.md` + the
  ratchet gate `manifest-check.sh` (+ its test). Installed per-machine via a junction (not in-repo).
- **`tools/`** — the copy-in kits: `memory-tree/`, `codebase-map/`, `hooks/agent-cap.js`,
  `workflows/tier2-review.js`, `agent-instructions/`, `pytest-parallel-guardrails/` (bounded,
  attributable pytest-xdist runs: the four-knob ini recipe, the crashprobe worker-death
  attribution plugin, the aiosqlite closed-loop seam patch + forced-race gate), the
  `check-template-size.sh` gate, and `check-wiring.sh` (detects/auto-wires
  installed-but-unwired tools; SessionStart-driven).
- **`WIRE-INTO-PROJECT.md`** — the agent runbook for wiring the whole chain into a target repo.

## Layout

- Root: `README.md`, this charter, `WIRE-INTO-PROJECT.md`, the product template + its two companions.
- `tools/` — the deployable kits (copied into target repos).
- `skills/session-kickoff/` — the kickoff skill (stays at repo root for machine-junction discovery).
- `memory/` — this repo's dogfooded memory tree (disciplines `playbook · kickoff · tooling · deployer`
  + `project/`). Specs, reports, research, and reviews live under each discipline's `builds/`, NOT the
  root. Version snapshots live in `memory/playbook/archive/`.
- `.memory-tree.conf` · `.claude/SESSION-KICKOFF.md` · `.gitattributes` (LF discipline).

## Node registry

| Tag | Machine/user | Primary tree | Remote |
|-----|--------------|--------------|--------|
| `a` | daily-agent | `C:/projects/coding-governance` | `origin` (github `d41ly/coding-governance`) |
| `b` | agent5 @ `DESKTOP-3J1O6CD` | `C:/projects/coding-governance` | `origin` (github `d41ly/coding-governance`) |

IDs are `FAMILY-<slug>-<seq>` (`PLAY`/`KICK`/`TOOL`/`DEPL`); slug = node tag + CamelCase adjective-noun,
minted once per session. Decisions/backlogs live per discipline under `memory/<discipline>/`.

## The gate suite (the merge bar) — `bash tools/run-gates.sh`

The full bar is green at the push boundary (earlier runs are diff-scoped); each leg rides the runner:
- `memory/` hygiene (12 checks) — `tools/memory-tree/check-memory-hygiene.sh`
- kickoff-manifest ratchet — `skills/session-kickoff/manifest-check.sh` (+ self-test)
- template size ≤32 KiB — `tools/check-template-size.sh`
- kit version markers — `tools/check-kit-versions.sh` (every kit's version constant present + the memory-tree marker/constant pair agrees)
- kit self-tests — `tools/hooks/agent-cap.test.sh`, `tools/agent-instructions/adopt-agent-instructions.test.sh`, `tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh`, `python tools/codebase-map/selftest.py`, `python tools/settings-merge.py --selftest`
- run-gates canary — `tools/run-gates.test.sh` (the legs are single-sourced from `tools/gate-legs.json`; the canary asserts the manifest is well-formed and `run-gates.sh` hardcodes no leg command)
- branch guard self-test — `.githooks/pre-commit.test.sh` (the pre-commit refuses primary-tree commits off the default branch)
- pre-push self-test — `.githooks/pre-push.test.sh` (the pre-push runs the full bar on a default-branch push, blocks a red one)
- wiring-health self-test — `tools/check-wiring.test.sh` (`check-wiring.sh` detects/auto-wires unwired tools: `core.hooksPath`, agent-cap)
- agent-instructions wiring — `tools/agent-instructions/adopt-agent-instructions.sh --check`

The full bar's authoritative run is the tracked **`.githooks/pre-push`** hook: a push to the default
branch runs `tools/run-gates.sh` once and blocks a red push (classify on the remote ref; the validated
tree must be the pushed tip; `GOV_GATE_CMD` overrides the gate for testing; `--no-verify` bypasses).
Earlier runs (DoR, post-merge) are diff-scoped. The active hooks are the tracked `.githooks/` dir via
`core.hooksPath`, NOT an out-of-tree copy, so there is no staleness-drift class here (the
`WIRE-INTO-PROJECT.md` copy-install path would reintroduce it — a scoped follow-up). Wire into CI by
running `tools/run-gates.sh` in a workflow (needs a `workflow`-scoped push — a follow-up). A tracked
pre-commit fast leg is in `.githooks/` (install: `git config core.hooksPath .githooks`) — it also
enforces the §3 branch guard (refuses a primary-tree commit off the default branch; pin with
`GOV_DEFAULT_BRANCH`, override with `--no-verify`). A SessionStart hook in `.claude/settings.json`
runs `tools/check-wiring.sh --session`, which auto-sets an unset `core.hooksPath` (never clobbers a
set value) so a fresh clone self-heals instead of running with dormant gates.

## Conventions

- **LF** on all `.sh` + the memory-tree data files (`.gitattributes`); verify staged bytes on Windows.
- Kits live in `tools/`; the session-kickoff skill stays at `skills/` (machine-junction discovery).
- The template is the operating ruleset — keep it ≤32 KiB; anything activity-scoped or one-time goes
  in a companion, not the template.
- Follow the governance playbook (`parallel-coding-governance.template.md`) for the full multi-node
  rules — this repo is its reference dogfood.
- Commit freely; **merge to `main` and `git push` each need an explicit ask.**
