---
name: session-kickoff
description: >-
  Start a work-unit cleanly in ANY project. Verifies git state (clean-tree + branch guards,
  fetch + fast-forward, pinned BASE SHA), loads the project's kickoff manifest when one
  exists, derives a CLOSED task scope (goal, in/out, acceptance, gates), and surfaces the
  governing docs + first code entrypoints. In a repo without a manifest, offers to scaffold
  one from the parallel-coding-governance template. Invoke explicitly with /session-kickoff
  at the start of a work session. The project's CLAUDE.md and its manifest always outrank
  this skill on any conflict.
---

# Session kickoff (project-agnostic engine)

You are hand-guiding the user through starting a work-unit. This file is the **engine** —
the universal protocol. Everything project-specific (id schemes, ledgers, stream maps, gate
commands, tier rules) comes from the **project layer**: the repo's kickoff manifest (Step 2).
Precedence on conflicts: **project `CLAUDE.md` > project manifest > this skill** — follow the
winner and flag the conflict so it gets fixed.

Posture: do the mechanical checks yourself (shell/Read/Grep), ask the user ONLY for what you
can't derive, use `AskUserQuestion` for genuine forks. Keep it tight — this is a launchpad,
not a meeting.

**Efficiency rules (non-negotiable):**
- Run the whole of Step 1 as **ONE batched shell command**, not a call per check.
- **Never re-derive what's already in context** — `CLAUDE.md` is auto-loaded; a SessionStart
  hook may already have reported worktree/branch state. Consume, don't recompute.
- Read the manifest **exactly once**; grep/offset large files instead of re-reading whole.
- **Skip inapplicable steps silently-but-stated** (no remote → no fetch; no id scheme → no
  slug; say so in one clause, don't ceremonialize).

## Step 0 — Resolve the repo (once)

- If the session cwd is inside a git work tree (`git rev-parse --show-toplevel`) → that's
  `<repo>`.
- Else the cwd may be a **worktree parent** (sibling checkouts under one root — a common
  multi-stream layout): probe the *immediate* child dirs for git checkouts; prefer the one
  holding the default branch (often the dir literally named `main`). Ask only if ambiguous.
- No git anywhere → say so and ask whether to run a scope-only kickoff (Steps 3 + 5) or stop.
- Detect **remote** (`git remote` — prefer `origin`, else the first) and **default branch**
  (`git symbolic-ref --short refs/remotes/<remote>/HEAD`, strip the `<remote>/` prefix;
  fallback: `main` if it exists, else `master`). No remote → note it, skip fetch/ff.
- On Windows under a POSIX shell (MSYS/Git-Bash), give `git -C` **forward-slash** paths
  (`/c/repo`), never backslash — backslash drive paths get mangled.

## Step 1 — Orient (ONE batched command; report ≤5 lines)

In a single shell call, in `<repo>`: current branch · `status --short` · fetch +
`merge --ff-only <remote>/<default>` (only when on the default branch with a clean tree;
report if it moved) · `rev-parse HEAD` → report as **BASE** (pin the immutable SHA for later
diff-scoping, never a moving ref) · `git worktree list` when the layout is multi-tree AND no
hook already reported it.

If the ff moved the default branch AND the project has a codebase map (the manifest declares
one, or `.codebase-map.conf` exists at the repo root): render the feature-level digest of what
came in — the manifest's map-diff command over `<old-sha>..<new-sha>` (default:
`python codebase-map/map_diff.py <old>..<new>`) — and report it (rollup + coverage line;
`--verbose` only if asked).

**STOP and tell the user first** (before any further step) when: a foreign `MERGE_HEAD` or
`UU` conflict entries exist; the ff-merge fails (local diverged from remote); or the
checked-out branch violates the project's stated conventions. A clean tree is NOT proof
you're on the right branch.

## Step 2 — Load the project layer (the manifest)

Search `<repo>` in order — **first hit wins, read it once**:

1. `docs/claude/SESSION-KICKOFF.md`
2. `docs/SESSION-KICKOFF.md`
3. `.claude/SESSION-KICKOFF.md`
4. `SESSION-KICKOFF.md`
5. else an instantiated governance doc: grep `docs/` + the repo root for the
   `governance-template:` marker (e.g. `docs/PARALLEL.md`).

The manifest is **authoritative for everything project-specific**: branch/layout conventions,
id + ledger protocol, stream/pointer maps, tier rules, gate commands, environment traps. Where
it defines a step, its version replaces the generic default below.

**No manifest found** → say so plainly and offer (one `AskUserQuestion`) to scaffold one — see
**Scaffolding** at the bottom. Whether or not they accept, continue with the generic Steps 3–5.

## Step 3 — Derive a CLOSED task scope (from the message + memory; ask only for gaps)

**DERIVE these fields yourself** — from the `/session-kickoff` message plus the adjacent memory
(decision logs, backlog, journals, ledger) and the code — filling every one you can. Use
`AskUserQuestion` ONLY for a field you genuinely cannot derive to any extent (a real fork between
approaches, or a non-code prereq only the owner knows). Don't hand the user a blank form. Press hardest
on the three that prevent mid-build churn:

- **Title** + **Goal** (1–2 sentences) · **IN scope**.
- **OUT / non-goals** — an explicit cut-line (never "high-value first" / a menu; resolve now).
- **Acceptance check** — the observation that proves THIS change (a test it adds, a gate it
  moves, an observed behavior) — *not* an unrelated green check.
- **Gates it must pass** — from the manifest's gate list, else the project's obvious
  build/lint/test commands.
- **Risk tier**, if the project defines tiers. Generic heuristic when it doesn't: a new write
  path / data migration / auth·sanitization·egress surface / shared-contract change is
  high-risk → the DoR is a **design pass**: written spec (goal · scope · non-goals ·
  acceptance) approved BEFORE building, recorded per the project's plan convention.

If a field still can't be filled after you've DERIVED from the message/memory/code AND asked
(`AskUserQuestion`) — acceptance + gates especially — say so plainly: it isn't Ready — split or clarify
before any code.

## Step 4 — Point at the right code + project protocol

From the manifest's pointer map (else a quick grep of the project's docs): the governing
docs to load, prior decisions/records matching the feature's keywords, and the first code
entrypoints — don't make the user hunt. Flag doc claims that tend to drift as "verify against
source".

**Codebase map as the first probe** (when the project has one): read the feature's dossier
(`<MAP_ROOT>/features/<feature>.md`) before grepping decision logs — its keyed claims are
CI-verified, so trust them over prose notes; the generated map is the system inventory. A
high-risk unit touching an UNDOSSIERED feature creates/refreshes that dossier as part of its
design pass (the map's convergence rule).

**Only if the manifest defines an id/ledger protocol:** mint + collision-check the session
slug per its rules and draft the ledger row for the user. No id scheme → skip (one clause).

## Step 5 — READY card, then stop

Echo a compact **READY card**: repo · branch + BASE sha · remote/default branch · scope
in/out · acceptance · gates · governing docs + prior records · slug (or "none"). Then hand
control back: *"Ready — say go and I'll start, or adjust any field."* Do not start building
until the user confirms.

## Scaffolding a manifest (only on user yes)

1. **Locate the templates.** This skill ships in the `coding-governance` repo; the starter is
   `MANIFEST-TEMPLATE.md` beside this file and the full playbook is
   `parallel-coding-governance.template.md` two levels up. If the skill was discovered through
   a junction/symlink, resolve the real path first (PowerShell:
   `(Get-Item <skill-dir>).Target`; POSIX: `readlink -f`). If resolution fails, ask the user
   where their `coding-governance` checkout lives.
2. **Fill `MANIFEST-TEMPLATE.md` from the repo** — gate commands from `package.json` /
   `Makefile` / CI config, docs layout from the tree, remote + default branch from Step 0.
   Ask only for the non-derivable (multi-node? stream ownership? tier policy?). Write the
   result to `docs/SESSION-KICKOFF.md` (create `docs/` if needed, or follow the project's
   docs convention), then `grep '{{'` to confirm no placeholder survived.
3. **Offer separately — don't bundle:** instantiating the full governance playbook
   (`parallel-coding-governance.template.md`, per its own "Customize before use" block) for
   projects that want the whole multi-node ruleset. The manifest is just the kickoff layer.
