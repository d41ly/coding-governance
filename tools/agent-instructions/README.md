# agent-instructions — one canonical instruction file, every AI tool wired to it

A small, project-agnostic kit that installs a single **canonical** agent-instruction file in a target
repo and wires each AI coding tool's expected filename to it — so you maintain ONE source, not one
file per tool.

## Why AGENTS.md is canonical

`AGENTS.md` is the cross-tool open standard (stewarded by the Linux Foundation's Agentic AI
Foundation; released by OpenAI in 2025, now in 28+ tools and 60k+ repos). It is read **natively** by
Codex CLI, GitHub Copilot, Cursor, Windsurf, Amp, Devin, Zed, Aider, Jules, and more. Gemini CLI reads
it when pointed at it via `.gemini/settings.json`. **Claude Code reads `CLAUDE.md`; from 2.1.277 it
also reads `AGENTS.md`, but only in a project with no `CLAUDE.md`** (closed request:
[anthropics/claude-code#6235](https://github.com/anthropics/claude-code/issues/6235)) — so `CLAUDE.md`
stays wired as the `@AGENTS.md` import (or a symlink/copy), which serves a CLI older than 2.1.277 and a
project whose `CLAUDE.md` exists for another reason. One `AGENTS.md` drives most tools natively; the
aliases below cover Claude, Gemini, and the legacy explicit files.

Both facts are stamped where they were checked, because a vendor can move either:

- Codex reads at most 32 KiB of project instructions by default, `project_doc_max_bytes`
  (verified 2026-10-05, node a, against `DEFAULT_PROJECT_DOC_MAX_BYTES` in `openai/codex` at
  `codex-rs/config/src/config_toml.rs`). The adopter announces a canonical over 32768 bytes on install
  and on `--check`, and its exit status does not change: trimming or raising the key is your call.
- Claude Code reads `AGENTS.md` only where no `CLAUDE.md` exists
  (verified 2026-10-05, node a, against the 2.1.277 entry of `anthropics/claude-code`'s `CHANGELOG.md`).

| Tool | File it looks for | How this kit wires it |
|---|---|---|
| Codex, Copilot, Cursor, Windsurf, Amp, Devin, Zed, Aider … | `AGENTS.md` | it IS the canonical; Codex reads only its first 32 KiB by default (`project_doc_max_bytes`), and the adopter announces a file over it |
| Claude Code | `CLAUDE.md`; from 2.1.277 `AGENTS.md` too, only with no `CLAUDE.md` | `CLAUDE.md` = `@AGENTS.md` import (pointer), or symlink/copy |
| Gemini CLI | `GEMINI.md`, or `AGENTS.md` via config | `.gemini/settings.json` `context.fileName: AGENTS.md` (pointer), or `GEMINI.md` symlink/copy |
| GitHub Copilot (explicit) | `.github/copilot-instructions.md` | symlink or synced copy |
| Cursor (legacy) | `.cursorrules` | symlink or synced copy |
| Windsurf (legacy) | `.windsurfrules` | symlink or synced copy |

## Use

```bash
# install a filled instruction doc as AGENTS.md and wire Claude + Gemini + Copilot to it
<prefix>/agent-instructions/adopt-agent-instructions.sh --source my-instructions.md

# choose aliases and mode explicitly
<prefix>/agent-instructions/adopt-agent-instructions.sh --aliases "claude gemini copilot cursor windsurf" --mode symlink

# verify wiring (CI / pre-commit) — non-zero on drift
<prefix>/agent-instructions/adopt-agent-instructions.sh --check
```

## Modes (`--mode`)

- **pointer** (default) — uses each tool's native indirection where one exists, so **no symlinks are
  needed** (robust on Windows without Developer Mode): `CLAUDE.md` becomes a one-line `@AGENTS.md`
  import; Gemini gets `.gemini/settings.json` with `context.fileName`; tools with no native pointer
  get a synced copy.
- **symlink** — real symlinks → `AGENTS.md` (needs Developer Mode / elevation on Windows; the script
  auto-falls back to copy if the link can't be created or would dangle).
- **copy** — real duplicate files, compared with `cmp -s` (byte-exact, EOL-attribute-safe, no git
  needed) and kept honest by `--check`.

Idempotent: re-running converges (already-correct wiring is left untouched). `--check` verifies
symlinks resolve, `@AGENTS.md` imports are intact, the Gemini `context.fileName` actually points at
`AGENTS.md`, and copies still match. **Copy-mode drift is the one non-convergent case** — a changed
canonical leaves stale copies that only `--force` re-syncs (a plain copy is indistinguishable from a
user edit, so overwriting it demands the explicit flag).

## Deploying the governance playbook this way

To make the governance playbook a project's agent instructions: fill
`coding-governance-agents.template.md` with `bash <prefix>/playbook/adopt-playbook.sh --target <repo>`,
which reads the target's `deploy.toml`, then install the result as `AGENTS.md` with this tool. The
charter is ONE file as of v3.0 — there is no companion to copy alongside. See `WIRE-INTO-PROJECT.md`.
