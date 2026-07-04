# coding-governance

Project-agnostic governance + tooling for running Claude Code (or any agent) across several
machines/sessions on the same repo.

**Wiring the whole chain into a new project?** Follow the agent runbook
[WIRE-INTO-PROJECT.md](WIRE-INTO-PROJECT.md) (skill → playbook → memory-tree → manifest → verify).

## Contents

- **`parallel-coding-governance.template.md`** — the governance playbook template (current
  version; `…-v-N-N.md` files alongside are historical snapshots). Copy into a repo and fill
  its `{{PLACEHOLDERS}}` per its own "Customize before use" block.
- **`skills/session-kickoff/`** — the generic `/session-kickoff` skill: the project-agnostic
  *engine* (git-state guards, closed-scope collection, READY card). Project specifics come
  from a per-repo **kickoff manifest** the skill discovers (see its Step 2 search list);
  `MANIFEST-TEMPLATE.md` is the starter it scaffolds into manifest-less projects.
- **`memory-tree/`** — an opt-in kit for a structured, machine-linted `memory/` tree (disciplines,
  per-feature `builds/` folders, index budgets + rotation, status vocabulary, an 11-check hygiene
  gate). Project specifics live in one repo-root `.memory-tree.conf`; the scripts are identical
  across repos. Scaffold a fresh tree with `adopt-memory-tree.sh --scaffold`, or migrate an existing
  one in a single landing. See `memory-tree/README.md`. Operationalizes the playbook's §5/§6.
- **`hooks/agent-cap.js`** — a `PreToolUse` guard that caps `Workflow` fan-out: it DENIES any
  script calling raw `parallel(`/`pipeline(` instead of the cap-4 `boundedParallel`/`boundedPipeline`
  helpers, so a wide agent burst can't trip the server rate limiter. Cap overridable via env
  `AGENT_CAP`. Wire per WIRE-INTO-PROJECT §5; sanity-check with `hooks/agent-cap.test.sh`.
  Operationalizes the playbook's §8 concurrency rule.
- **`workflows/tier2-review.js`** — a ready, consolidated Tier-2 review harness (find → BATCHED
  verify → synth; ~7–9 agents, never >4 concurrent). Run via `Workflow({scriptPath})`, parameterized
  by `args` (base SHA, repo, context). Passes the `agent-cap` guard by construction.

## Install the skill (once per machine)

Link the skill into the **user-level** skills dir so it fires in any project:

```powershell
# Windows (junction, no admin needed)
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\session-kickoff" `
  -Target "<this-repo>\skills\session-kickoff"
```

```bash
# POSIX
ln -s <this-repo>/skills/session-kickoff ~/.claude/skills/session-kickoff
```

Restart Claude Code and confirm `/session-kickoff` is listed. A project may deliberately keep
its own project-tuned variant alongside this one (both then appear in that project's skill
list — pick by description); the generic engine still serves every other project.
