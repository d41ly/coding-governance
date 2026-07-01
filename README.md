# coding-governance

Project-agnostic governance + tooling for running Claude Code (or any agent) across several
machines/sessions on the same repo.

## Contents

- **`parallel-coding-governance.template.md`** — the governance playbook template (current
  version; `…-v-N-N.md` files alongside are historical snapshots). Copy into a repo and fill
  its `{{PLACEHOLDERS}}` per its own "Customize before use" block.
- **`skills/session-kickoff/`** — the generic `/session-kickoff` skill: the project-agnostic
  *engine* (git-state guards, closed-scope collection, READY card). Project specifics come
  from a per-repo **kickoff manifest** the skill discovers (see its Step 2 search list);
  `MANIFEST-TEMPLATE.md` is the starter it scaffolds into manifest-less projects.

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

Restart Claude Code and confirm `/session-kickoff` is listed. If a project previously shipped
its own copy of the skill (e.g. a repo-local `.claude/skills` junction), remove that wiring —
duplicate same-name skills confuse discovery and drift apart.
