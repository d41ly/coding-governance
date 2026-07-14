# Session kickoff manifest — coding-governance

<!-- kickoff-manifest: v1.1 · instantiated from skills/session-kickoff/MANIFEST-TEMPLATE.md -->
<!-- manifest-audit
last-audit: 2026-07-14T23:08:25+03:00 @ c78958c78aa44d128207179e2bb5ef161d0e46bc
watch: tools/memory-tree/check-memory-hygiene.sh; tools/check-template-size.sh; tools/run-gates.sh; skills/session-kickoff/manifest-check.sh; .memory-tree.conf; parallel-coding-governance.template.md
verify-paths: AGENTS.md; parallel-coding-governance.template.md; README.md
check-script: skills/session-kickoff/manifest-check.sh
-->

The project layer read by the generic `/session-kickoff` skill. Precedence on conflicts:
**`AGENTS.md`/`CLAUDE.md` > this file > the skill**. This repo dogfoods its own kits, so the manifest
here is short — `AGENTS.md` (the charter) holds the substance.

## The ratchet — how this file stays true

- Every kickoff audits this file (`manifest-check.sh`, at `check-script:`) and repairs drift on the spot.
- Every unit that changed what this file front-loads (a gate command, entrypoint, governing doc, a
  trap hit, a doc/memory claim found stale, or a fact re-derived it should have front-loaded) re-stamps
  `last-audit` with a delta line in the commit message; no delta → no touch.
- Stamp rule: sha = `HEAD` on `main`, else `git merge-base origin/main HEAD`; datetime always advances.
- Dated entries carry a prune-when condition and are deleted once it holds.

## §A — Task (the agent DERIVES this per kickoff — the user does NOT fill it)

> - **Title / Goal / IN scope / OUT / Acceptance / Gates it must pass / Risk tier** — derived from
>   the `/session-kickoff` message + the adjacent memory (`memory/<discipline>/`) and the code.

## §B — Orientation (derived at instantiation; re-audited every kickoff; accretes)

- **Repo layout:** single checkout at the repo root (`C:/projects/coding-governance`); no worktree fan.
- **Remote · default branch:** `origin` · `main`.
- **Branch conventions:** small units on `main` for a solo tooling repo; `git push` needs an explicit ask.
- **Governing docs:** `AGENTS.md` (the charter — authoritative) · `parallel-coding-governance.template.md`
  (the playbook this repo follows + ships) · `memory/<discipline>/DECISIONS.md` + `BACKLOG.md`.

### Pointer map (load the row(s) the task touches)

| Area / stream | Governing memory | First code entrypoints |
|---|---|---|
| playbook (`PLAY-`) | `memory/playbook/` | `parallel-coding-governance.template.md` + `.customize.md` + `.domain-rules.md` · `tools/check-template-size.sh` |
| kickoff (`KICK-`) | `memory/kickoff/` | `skills/session-kickoff/` (SKILL.md · MANIFEST-TEMPLATE.md · manifest-check.sh) |
| tooling (`TOOL-`) | `memory/tooling/` | `tools/` (memory-tree · codebase-map · hooks · workflows · agent-instructions) |
| deployer (`DEPL-`) | `memory/deployer/` | `WIRE-INTO-PROJECT.md` · `memory/deployer/builds/2026-07-12-DEPL-aDeployScout/` (research) |

### Gate commands (the merge bar)

```bash
bash tools/run-gates.sh    # runs all legs: hygiene · manifest ratchet · template-size · kit self-tests · agent-instructions wiring
```

### Tier rule

Tier 2 (spec + adversarial review before building) for: a change to the governance template's rules,
the manifest-check gate semantics, or a new/changed kit's contract; a cross-kit change. Otherwise
Tier 1 (gates + one focused self-review).

### ID + ledger protocol

`FAMILY-<slug>-<seq>`, families `PLAY`/`KICK`/`TOOL`/`DEPL` (per `.memory-tree.conf`). Slug = node tag
(`a`) + CamelCase adjective-noun, minted once per session; collision-grep `memory/`. Ledger:
`memory/project/in-flight/<tag>.md`.

### Current posture — dated corrections

*Correction OVERRIDES a stale doc/memory claim until fixed; entry: `<date> · <stale where> · <the
correction> · prune when <condition>`. Starts empty; prune per-entry, never delete the section.*

- *(none yet)*

### Environment traps worth front-loading

*Accretes — append the trap that cost time, prune the one that stopped being true.*

- The template is under a STRICT 32 KiB gate — never raise the limit; externalize to a companion instead.
- All `.sh` + memory-tree data files are LF (`.gitattributes`); verify staged bytes with `git diff --cached --check`.
- Editing the shipped `manifest-check.sh` diverges it from adopters' copies — they re-pull on kit update.
- The `agent-cap` PreToolUse hook caps Workflow fan-out at 4 concurrent — route fan-out through the cap-4 helpers.
- Node `a` currently has **no Python interpreter** — the `codebase-map kit selftest` + `settings-merge selftest`
  gate legs (and the `manifest-check` python mutation subcase) show RED as `exit 127`, not logic failures.
  Verify Python-touching changes on a Python host / CI before merge. Prune when python lands on node `a`.
