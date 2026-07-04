# Wire the coding-governance chain into a project — agent runbook

You are wiring the **full coding-governance chain** into a target project. Follow this top to bottom;
verify after every step. This file is agent-facing: imperative steps, exact commands, explicit
derive-vs-ask calls.

**The chain is three composing layers:**

1. **Governance playbook** (`parallel-coding-governance.template.md`) — the multi-node ruleset (IDs,
   streams, sharded ledger, gates, reviews, memory, output discipline). Lives in the project as one doc.
2. **`/session-kickoff` skill** (`skills/session-kickoff/`) — the project-agnostic kickoff *engine*,
   installed ONCE per machine; it reads a per-project **kickoff manifest** to learn project specifics.
3. **memory-tree kit** (`memory-tree/`) — the gated `memory/` structure that operationalizes the
   playbook's §5/§6. Optional but recommended.

**Precedence (never violate):** project `CLAUDE.md` > kickoff manifest > the skill. The playbook is the
ruleset the manifest points at, not a duplicate of it.

**Posture:** DERIVE everything the repo reveals (gate commands, layout, remote, default branch, id
families); use `AskUserQuestion` ONLY for what it genuinely can't (node registry, stream ownership, tier
policy, whether to adopt memory-tree). Keep it tight — this is wiring, not a meeting.

**Definitions:** `<gov>` = the `coding-governance` checkout (the repo this file lives in); `<project>` =
the target repo root. Commands are bash (git-bash on Windows). If `<gov>` is unknown, ask.

---

## 0 — Preconditions + the decisions to lock first

- Confirm `<project>` is a git repo, on its default branch, clean:
  `git -C <project> status --short` (empty) · `git -C <project> symbolic-ref --short HEAD`.
- **Ask the user** (not derivable):
  - **Fleet** — one node-registry row per machine/agent: tag · machine · primary-tree path · worktree
    root · variances. (Solo/single machine → one row.)
  - **Stream ownership** — which node owns which stream (keeps merges disjoint).
  - **Tier policy** — single-tier, or Tier-1/Tier-2 and what forces Tier-2 (new write path · migration ·
    auth/sanitization/egress surface · shared-contract change · cross-stream merge).
  - **Adopt memory-tree?** yes (recommended) / no. If no: skip §3 and delete the two `{{MEMORY_*}}`
    placeholders + the two §5 memory-tree lines from the playbook.
- **Derive, don't ask:** gate commands (`package.json` / `Makefile` / CI config), repo layout (the tree),
  remote + default branch, id families.

## 1 — Install the kickoff skill (ONCE per machine — NOT per project)

Link the engine into the user-level skills dir so `/session-kickoff` fires in every project:

```powershell
# Windows — junction, no admin needed
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\session-kickoff" -Target "<gov>\skills\session-kickoff"
```

```bash
# POSIX
ln -s <gov>/skills/session-kickoff ~/.claude/skills/session-kickoff
```

**Verify:** restart Claude Code; `/session-kickoff` is listed. (A project MAY keep its own tuned variant
alongside — both then appear; pick by description.) Skip this step on a machine that already has it.

## 2 — Install the governance playbook (per project)

1. Copy the playbook in as one governing doc (follow the project's convention):
   ```bash
   cp <gov>/parallel-coding-governance.template.md <project>/docs/PARALLEL.md
   ```
   (or paste its body into `<project>/CLAUDE.md`). **Keep the `<!-- governance-template: vN.N -->` marker
   verbatim** — the kickoff engine's Step-2 fallback and the upstream-re-pull mechanism both read it.
2. Fill every `{{PLACEHOLDER}}` per the doc's own **"Customize before use"** block (at the bottom). The groups:
   - **Fleet** (ask): node-registry rows + stream ownership.
   - **Records & docs** (derive/ask): id families, doc-routing table, product preamble, repo-layout map,
     command catalog, product-context home, help dir, review dir.
   - **Memory tree** (only if §3 chosen): `{{MEMORY_ROOT}}` + `{{MEMORY_DISCIPLINES}}` — else delete them
     and the two §5 memory-tree lines.
   - **Gates & git** (derive): gate commands, CI file, gate runner, commit trailer, worktree script,
     toolchain notes.
   - **Runtime/verification · architecture/design-system · output-discipline** — fill what applies, delete
     what doesn't.
3. Delete the "Customize before use" block once filled.

**Verify:** `grep -n '{{' <project>/docs/PARALLEL.md` prints nothing. `{{ID_FAMILIES}}` must match the
memory-tree `FAMILIES` (§3) — the ledger and the decision logs share one id scheme.

## 3 — Adopt the memory-tree kit (if chosen in §0)

1. Copy the kit in and configure:
   ```bash
   cp -r <gov>/memory-tree <project>/memory-tree
   cp <project>/memory-tree/.memory-tree.conf.example <project>/.memory-tree.conf   # then edit
   ```
   Edit `.memory-tree.conf`: `MEMORY_ROOT` · `DISCIPLINES` (your streams) · `FAMILIES`
   (`discipline:FAMILY`, MUST match the playbook's `{{ID_FAMILIES}}`) · `TOMBSTONE_ROOTS` (blank for a
   fresh tree; set to the old root only when migrating an existing docs tree — see `memory-tree/README.md`).
2. Scaffold + verify:
   ```bash
   cd <project>
   bash memory-tree/adopt-memory-tree.sh --scaffold
   bash memory-tree/check-memory-hygiene.sh ; echo $?    # expect 0
   ```
   The scaffold writes `memory/` with the discipline folders, `TREE.md`, and `project/` — including the
   **sharded in-flight ledger**: `project/IN-FLIGHT.md` (a pointer stub) + `project/in-flight/` (per-node files).
3. Wire the gate in all three places:
   - **CI:** a job running `bash memory-tree/check-memory-hygiene.sh` (no args = full check, incl. TREE drift).
   - **Local gate runner:** add it as a concurrent leg (cheap, parallel with test/typecheck).
   - **pre-commit hook** — guarded so a scripts-less checkout stays green:
     ```sh
     top=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
     if [ -f "$top/memory-tree/check-memory-hygiene.sh" ] &&
        git diff --cached --name-only --diff-filter=ACMR -- 'memory/**' | grep -q .; then
       bash "$top/memory-tree/check-memory-hygiene.sh" --staged || exit 1
     fi
     ```
   - **`.gitattributes`** (Windows-determinism for check 9) — add:
     ```
     memory/**/TREE.md text eol=lf
     memory/project/legacy-files.txt text eol=lf
     memory/project/curation-debt.txt text eol=lf
     ```

**The ledger rule to carry into the manifest/playbook:** each node writes ONLY its own
`memory/project/in-flight/<tag>.md`; read ALL of `in-flight/*.md` for the who's-touching-what /
slug-collision scan; self-prune your own `pushed:/merged:<sha>` rows on session start
(`git merge-base --is-ancestor <sha> main`). One writer per file → the ledger never conflicts on merge.

## 4 — Write the kickoff manifest (the engine's project layer)

The engine (§1) discovers the manifest by searching `<project>`, **first hit wins**:
`docs/claude/SESSION-KICKOFF.md` → `docs/SESSION-KICKOFF.md` → `.claude/SESSION-KICKOFF.md` →
`SESSION-KICKOFF.md` → else it greps `docs/` + root for the `governance-template:` marker (the playbook
from §2). Write the manifest to one of those paths so it resolves.

1. Instantiate it:
   ```bash
   cp <gov>/skills/session-kickoff/MANIFEST-TEMPLATE.md <project>/docs/SESSION-KICKOFF.md
   ```
2. Fill **§B (orientation)** from the repo: repo layout · remote + default branch · branch conventions ·
   governing docs · the **path to the playbook from §2** · the pointer map (area → doc → entrypoints) ·
   the gate commands · the tier rule · the **ID + ledger protocol** (id format + slug rules + collision
   grep + the sharded ledger path `memory/project/in-flight/<tag>.md`) · the environment traps. Keep it
   SHORT — only what the engine can't derive from git/`CLAUDE.md`; reference the playbook, never duplicate it.
   (§A is derived by the agent per kickoff — leave it as the shape, don't fill it.)
3. Delete the "Customize before use" block.

**Verify:** `grep -n '{{' <project>/docs/SESSION-KICKOFF.md` prints nothing.

## 5 — Optional: worktree tooling + SessionStart nudge

Only if the project runs multiple nodes/worktrees (playbook §3):
- A `new-stream` script (sibling worktree on a fresh branch off fast-forwarded `main` + dependency
  install) → fill `{{WORKTREE_SCRIPT}}`.
- The tracked pre-commit **branch guard** (refuse a primary-tree commit while off the default branch) + its
  per-node install script.
- Optionally a SessionStart hook that nudges `/session-kickoff` and reports `git worktree list` state.

**Concurrency guard (recommended for ANY project that fans out `Workflow` agents — playbook §8):**
- Copy `hooks/agent-cap.js` (+ `hooks/agent-cap.test.sh`) into the project (e.g. `<project>/.claude/hooks/`).
- Wire a `PreToolUse` hook into the discovered `settings.json` (the `.claude/` in the session cwd):
  ```json
  "PreToolUse": [ { "matcher": "Workflow", "hooks": [ { "type": "command",
    "command": "node \"${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js\"" } ] } ]
  ```
  It DENIES any `Workflow` script that calls raw `parallel(`/`pipeline(` instead of the cap-4
  `boundedParallel`/`boundedPipeline` helpers (override the cap with env `AGENT_CAP`). This is the
  mechanical enforcement of the ≤4-concurrent rule — a wide fan-out trips the server rate limiter.
- Copy `workflows/tier2-review.js` for a ready consolidated review harness (~7–9 agents, ≤4 concurrent).
- Verify: `bash <project>/.claude/hooks/agent-cap.test.sh` → exit 0.

## 6 — Verify the whole chain, then commit

1. **Kickoff resolves:** run `/session-kickoff` in `<project>`. The engine must find your manifest (§4)
   and surface the playbook + gate + ledger protocol. If it can't, re-check the §4 search paths.
2. **Gate green** (if memory-tree adopted): `bash memory-tree/check-memory-hygiene.sh ; echo $?` → 0.
3. **No stray placeholders:** `grep -rn '{{' <project>/docs/PARALLEL.md <project>/docs/SESSION-KICKOFF.md` → empty.
4. **Ledger sharded:** `ls <project>/memory/project/in-flight/` exists; `IN-FLIGHT.md` is the pointer stub.
5. **Commit the chain:** `cd <project> && git add -A && git commit` (do NOT commit the per-machine skill
   junction — it lives under `~/.claude`, not the repo).

## Result — what the project now has

```
<project>/
├── CLAUDE.md                    # (optional) project charter — outranks the manifest + skill
├── docs/PARALLEL.md             # governance playbook, filled (governance-template marker kept)
├── docs/SESSION-KICKOFF.md      # kickoff manifest — the engine reads this
├── .memory-tree.conf            # memory-tree config           ┐
├── memory-tree/                 # the hygiene kit (copied in)  │ only if §3 adopted
├── memory/                      # scaffolded tree; project/in-flight/<tag>.md = sharded ledger  │
└── .gitattributes               # EOL rules for the tree       ┘
~/.claude/skills/session-kickoff # the engine (per-MACHINE junction/symlink — not in the repo)
```

## Maintenance

- **Precedence on any conflict:** `CLAUDE.md` > manifest > skill — follow the winner, fix the loser.
- **Pull upstream improvements:** the playbook carries `governance-template: vN.N`; re-pull by diffing your
  filled copy against `<gov>/parallel-coding-governance.template.md` per §-body (ignore filled
  placeholders + the deleted Customize block). The manifest carries its own `kickoff-manifest: vN.N`. The
  `memory-tree/` scripts are identical across repos — copy the newer versions in wholesale.
- **memory-tree kit updates** never carry project data (no brand gate, no migrations) — those stay in the
  project. Safe to overwrite `memory-tree/*.sh` + `HYGIENE.template.md` from `<gov>`.
