# Wire the coding-governance chain into a project — agent runbook

You are wiring the **full coding-governance chain** into a target project. Follow this top to bottom;
verify after every step. This file is agent-facing: imperative steps, exact commands, explicit
derive-vs-ask calls.

**The chain is three composing layers:**

1. **Governance playbook** (`parallel-coding-governance.template.md`) — the multi-node ruleset (IDs,
   streams, sharded ledger, gates, reviews, memory, output discipline). Lives in the project as one doc.
2. **`/session-kickoff` skill** (`skills/session-kickoff/`) — the project-agnostic kickoff *engine*,
   installed ONCE per machine; it reads a per-project **kickoff manifest** to learn project specifics.
3. **memory-tree kit** (`tools/memory-tree/`) — the gated `memory/` structure that operationalizes the
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
  - **Adopt codebase-map?** yes (recommended for any repo past ~20 modules) / no. If yes, lock:
    MAP_ROOT (under the memory tree when memory-tree is adopted, e.g. `memory/map`; else `docs/map`),
    GATE_FILE (a path the project's EXISTING test suite collects), and which surfaces to inventory
    (walk `tools/codebase-map/INVENTORY-DERIVATION.md` §1 with the user). If no: skip §3b and delete the
    FOUR codebase-map lines from the playbook (§1 DoR + §1 DoD + §5 kit bullet + §7 gates line).
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

1. Copy the playbook **and its two companions** in (the template's §4/§9/§10/§11/§12/§13 are §-stubs
   that reference `parallel-coding-governance.domain-rules.md` by name — it MUST travel alongside):
   ```bash
   cp <gov>/parallel-coding-governance.template.md    <project>/docs/PARALLEL.md
   cp <gov>/parallel-coding-governance.domain-rules.md <project>/docs/parallel-coding-governance.domain-rules.md
   # the customize companion is deploy-time only — read it, don't ship it
   ```
   (or install the filled playbook as the canonical `AGENTS.md` via the agent-instructions kit — §5.)
   **Keep the `<!-- governance-template: vN.N -->` marker verbatim** — the kickoff engine's Step-2
   fallback and the upstream-re-pull mechanism both read it.
2. Fill every `{{PLACEHOLDER}}` per **`<gov>/parallel-coding-governance.customize.md`** (the deploy-time
   placeholder catalog — externalized from the template as of v2.3). The groups:
   - **Fleet** (ask): node-registry rows + stream ownership.
   - **Records & docs** (derive/ask): id families, doc-routing table, product preamble, repo-layout map,
     command catalog, product-context home, help dir, review dir.
   - **Memory tree** (only if §3 chosen): `{{MEMORY_ROOT}}` + `{{MEMORY_DISCIPLINES}}` — else delete them
     and the two §5 memory-tree lines.
   - **Gates & git** (derive): gate commands, CI file, gate runner, commit trailer, worktree script,
     toolchain notes.
   - **Runtime/verification · architecture/design-system · output-discipline** — fill what applies, delete
     what doesn't per the customize companion's conditional-sections list.
3. The customize companion lists the conditional sections to delete when they don't apply; apply that.

**Verify:** `grep -nE '\{\{[A-Z]' <project>/docs/PARALLEL.md` prints nothing (the template legitimately
holds `${{ }}` / Go-template braces in gate commands — shape-scope the grep). `{{ID_FAMILIES}}` must
match the memory-tree `FAMILIES` (§3) — the ledger and the decision logs share one id scheme.

## 3 — Adopt the memory-tree kit (if chosen in §0)

1. Copy the kit in and configure:
   ```bash
   cp -r <gov>/tools/memory-tree <project>/memory-tree
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

## 3b — Adopt the codebase-map kit (if chosen in §0)

1. Copy the kit dir into the project root **as `codebase-map/`** (the fixed name the gate template
   resolves — don't rename): `cp -r <gov-repo>/tools/codebase-map <project>/codebase-map`.
2. `cp codebase-map/.codebase-map.conf.example .codebase-map.conf` and fill MAP_ROOT · GATE_FILE ·
   MAP_DIFF_CMD (per the §0 decisions).
3. `cp codebase-map/map_extractors.template.py codebase-map/map_extractors.py` and declare the
   project's inventories — this is the real work; follow `codebase-map/INVENTORY-DERIVATION.md`
   (prefer registry imports; fail-closed helpers; full extension sets; POSIX keys).
4. `codebase-map/adopt-codebase-map.sh --scaffold` — scaffolds the map tree, seeds the shrink-only
   baseline from live inventories, installs the gate at GATE_FILE and runs it once (green on a
   fresh seed, by construction). `MAP_PY=python3` overrides the launcher.
5. Verify the project's test suite COLLECTS the gate (run the suite; the map tests must appear) —
   that is the entire CI wiring: zero pipeline changes by design.
6. Fill the manifest's "Codebase map" section (§4) and keep the playbook's map DoR/DoD lines (§2).
7. Commit `codebase-map/ .codebase-map.conf <GATE_FILE> <MAP_ROOT>/` as one landing.

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
   grep + the sharded ledger path `memory/project/in-flight/<tag>.md`) · the environment traps. Fill the
   **`manifest-audit` block** per the template's Customize notes: `watch` = the pathspecs the gate/layout
   claims derive FROM (never lockfiles; ≤~8); `verify-paths` = the 2–3 tracked anchors; stamp
   `last-audit` = ISO-8601 datetime with offset (e.g. `date -Iseconds`) `@` full sha (HEAD on the
   default branch, else `git merge-base <remote>/<default> HEAD`; no remote →
   `git merge-base <local-default> HEAD`); tag claims whose truth lives in another repo
   `(cross-repo — verify at use)`. Keep it SHORT — only what the engine can't derive from
   git/`CLAUDE.md`; reference the playbook, never duplicate it. (§A is derived by the agent per
   kickoff — leave it as the shape, don't fill it.)
3. Delete the "Customize before use" block.
4. **Wire the ratchet gate:**
   ```bash
   mkdir -p <project>/scripts && cp <gov>/skills/session-kickoff/manifest-check.sh <project>/scripts/
   ```
   (Non-default home → record it in the block's `check-script:` and adjust every path below.) Append
   `scripts/manifest-check.sh text eol=lf` (or a repo-wide `*.sh text eol=lf`) to the project's
   `.gitattributes` — the gov repo's EOL rules don't travel with `cp`, and a CRLF checkout kills bash
   silently. Keep the template's standing gate-fence line pointing at the checker. Then `git add` the
   manifest, the checker, and `.gitattributes` — the checker tests TRACKED-ness; an unstaged fresh
   adoption cannot pass.
5. **Offered hardening (each optional, separately):**
   - pre-commit leg, guarded like the memory-tree hook so a scripts-less checkout stays green — note
     it deliberately narrows the drift remedy to "bundle the re-stamp into THIS commit":
     ```sh
     top=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
     if [ -f "$top/scripts/manifest-check.sh" ]; then bash "$top/scripts/manifest-check.sh" --staged || exit 1; fi
     ```
   - CI leg: run `bash scripts/manifest-check.sh` in a job whose checkout uses **`fetch-depth: 0`** —
     MANDATORY, not advisory: the actions/checkout default (depth 1) makes the drift check
     WARN-and-skip on every run, so a shallow CI leg never enforces the one check that matters.

**Verify:** `grep -nE '\{\{[A-Z]' <project>/docs/SESSION-KICKOFF.md` prints nothing, and
`cd <project> && bash scripts/manifest-check.sh; echo $?` → `0` (the checker resolves the repo from
the INVOKING directory, not from its own location — run it with the cwd inside `<project>`).

**Retrofit an existing v1.0 manifest** *(the durable recipe — the checker's C2 failure points here)*:
1. **Body deltas first:** rewrite the §B intro/heading to the v1.1 wording ("derived at
   instantiation; re-audited every kickoff; accretes"); insert the template's ratchet section; insert
   the dated-corrections section (empty — prunable per-entry, never deleted); add the traps-accrete
   note. Without this the file keeps its standing freeze directive and the older in-file contract wins.
2. Insert the `manifest-audit` block (derive `watch`/`verify-paths` as in step 2 above; tag cross-repo
   claims; stamp only AFTER actually re-verifying §B).
3. Copy the checker + `.gitattributes` line + gate-fence line; `git add` everything (step 4 above).
4. `bash scripts/manifest-check.sh` → 0.
5. Re-pull the playbook's v2.2 §1 lines (manifest DoD write-back + Landing reconcile exception) into
   the project's instantiated playbook and bump its `governance-template:` marker to v2.2 — without
   this, the write-back lever never activates for retrofitted projects.
6. Bump the manifest marker to `kickoff-manifest: v1.1` **LAST** — the bump silences the kit's
   version WARN, the only standing signal that the body still predates the ratchet.

## 5 — Optional: worktree tooling + SessionStart nudge

Only if the project runs multiple nodes/worktrees (playbook §3):
- A `new-stream` script (sibling worktree on a fresh branch off fast-forwarded `main` + dependency
  install) → fill `{{WORKTREE_SCRIPT}}`.
- The tracked pre-commit **branch guard** (refuse a primary-tree commit while off the default branch) + its
  per-node install script.
- Optionally a SessionStart hook that nudges `/session-kickoff` and reports `git worktree list` state.

**Concurrency guard (recommended for ANY project that fans out `Workflow` agents — playbook §8):**
- Copy `tools/hooks/agent-cap.js` (+ `tools/hooks/agent-cap.test.sh`) into the project (e.g. `<project>/.claude/hooks/`).
- Wire a `PreToolUse` hook into the discovered `settings.json` (the `.claude/` in the session cwd):
  ```json
  "PreToolUse": [ { "matcher": "Workflow", "hooks": [ { "type": "command",
    "command": "node \"${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js\"" } ] } ]
  ```
  It DENIES any `Workflow` script that calls raw `parallel(`/`pipeline(` instead of the cap-4
  `boundedParallel`/`boundedPipeline` helpers (override the cap with env `AGENT_CAP`). This is the
  mechanical enforcement of the ≤4-concurrent rule — a wide fan-out trips the server rate limiter.
- Copy `tools/workflows/tier2-review.js` for a ready consolidated review harness (~7–9 agents, ≤4 concurrent).
- Verify: `bash <project>/.claude/hooks/agent-cap.test.sh` → exit 0.

## 6 — Verify the whole chain, then commit

- Codebase-map (if adopted): `python codebase-map/selftest.py` (kit contract) · run the gate file
  directly (`python <GATE_FILE>`) · `python codebase-map/gen_map.py --check` (freshness) · make one
  throwaway inventory addition and watch the gate go red with the claim remedy, then revert.

1. **Kickoff resolves:** run `/session-kickoff` in `<project>`. The engine must find your manifest (§4)
   and surface the playbook + gate + ledger protocol. If it can't, re-check the §4 search paths.
2. **Gate green** (if memory-tree adopted): `bash memory-tree/check-memory-hygiene.sh ; echo $?` → 0.
3. **No stray placeholders:** `grep -rn '{{' <project>/docs/PARALLEL.md` → empty, and
   `grep -rnE '\{\{[A-Z]' <project>/docs/SESSION-KICKOFF.md` → empty (the manifest check is
   shape-scoped: its gate fence may legitimately hold `${{ … }}` / Go-template braces).
4. **Commit the chain FIRST:** `cd <project> && git add -A && git commit` (do NOT commit the
   per-machine skill junction — it lives under `~/.claude`, not the repo). The probe below needs the
   chain COMMITTED — §4 leaves it only staged, and a probe commit that sweeps the still-staged
   manifest in would introduce the stamp and stay green instead of demonstrating red.
5. **Ratchet red/green probe** (the drift check reads COMMITTED ranges — an uncommitted touch is
   invisible; use a throwaway branch off the chain commit): *commit* a throwaway change to a watched
   file → `bash scripts/manifest-check.sh` goes red (check 5) → re-stamp `last-audit` (bundled or
   follow-up commit) → green → **revert the throwaway AND the probe re-stamp together in ONE
   commit** → still green (a bare revert touches the watched file again and would end the wiring
   session red). If a CI leg was wired: push the probe branch and confirm the CI job actually reds —
   proof it isn't WARN-skipping on a shallow checkout. Then delete the probe branch.
6. **Ledger sharded:** `ls <project>/memory/project/in-flight/` exists; `IN-FLIGHT.md` is the pointer stub.

## Result — what the project now has

```
<project>/
├── AGENTS.md / CLAUDE.md        # (optional) project charter / agent-instruction file (agent-instructions kit)
├── docs/PARALLEL.md             # governance playbook, filled (governance-template marker kept)
├── docs/parallel-coding-governance.domain-rules.md  # the §4/§9–§13 domain checklists (travels with the template)
├── docs/SESSION-KICKOFF.md      # kickoff manifest (v1.1: manifest-audit block) — the engine reads this
├── scripts/manifest-check.sh    # ratchet gate — engine-identical copy (overwrite wholesale on kit updates)
├── .gitattributes               # EOL rules — the checker (+ the memory tree if §3 adopted)
├── .memory-tree.conf            # memory-tree config           ┐
├── memory-tree/                 # the hygiene kit (copied in)  │ only if §3 adopted
└── memory/                      # scaffolded tree; project/in-flight/<tag>.md = sharded ledger ┘
~/.claude/skills/session-kickoff # the engine (per-MACHINE junction/symlink — not in the repo)
```

- Codebase-map (only if §3b adopted): `codebase-map/` kit dir + project-owned
  `codebase-map/map_extractors.py` · `.codebase-map.conf` · the gate at GATE_FILE ·
  `<MAP_ROOT>/` (FOUNDATION.md, baseline.toml, features/, generated/).

## Maintenance

- Codebase-map engine files (`map_lib.py`, `gen_map.py`, `map_diff.py`, the two templates,
  `selftest.py`) are identical across repos — update by overwriting from `<gov-repo>` wholesale;
  NEVER overwrite the project-owned `codebase-map/map_extractors.py` or `.codebase-map.conf`.

- **Precedence on any conflict:** `CLAUDE.md` > manifest > skill — follow the winner, fix the loser.
- **Pull upstream improvements:** the playbook carries `governance-template: vN.N`; re-pull by diffing your
  filled copy against `<gov>/parallel-coding-governance.template.md` per §-body (ignore filled
  placeholders + the deleted Customize block) — a re-pull carries the v2.2 §1 manifest lines (DoD
  write-back + Landing reconcile exception) into instantiated playbooks. The manifest carries its own
  `kickoff-manifest: vN.N`. The `memory-tree/` scripts are identical across repos — copy the newer
  versions in wholesale.
- **`manifest-check.sh` is engine-identical** across repos — overwrite wholesale from `<gov>` (this also
  delivers the version-WARN constant that flags out-of-date manifest bodies). The `manifest-audit`
  block and the manifest BODY are project-owned — never overwritten by kit updates.
- **Stall review (rides this same Maintenance cadence):** at each kit re-pull, the owner compares the
  manifest's BODY-change commits (diffs touching more than the `last-audit` line) against watch-commit
  volume and elapsed time — **≥10 watch-pathspec commits or ≥3 months with zero body growth = the
  manifest is stalling**; that is the trigger for reconsidering heavier accretion tooling (journal
  mining). Kickoff delta lines are supporting color, not the data source — squash merges and chat
  don't preserve them.
- **memory-tree kit updates** never carry project data (no brand gate, no migrations) — those stay in the
  project. Safe to overwrite `memory-tree/*.sh` + `HYGIENE.template.md` from `<gov>`.
