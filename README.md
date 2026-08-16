# coding-governance

Project-agnostic governance + tooling for running Claude Code (or any agent) across several
machines/sessions on the same repo.

**Wiring the whole chain into a new project?** Follow the agent runbook
[WIRE-INTO-PROJECT.md](WIRE-INTO-PROJECT.md) (skill → playbook → memory-tree → manifest → verify).

## Contents

- **`parallel-coding-governance.template.md`** — the governance playbook template (the operating
  ruleset; **≤48 KiB, gated** by `tools/check-template-size.sh`). Historical `…-v-N-N.md`
  snapshots live under `memory/archive/`. Two companions ship with it:
  **`.customize.md`** (the deploy-time placeholder catalog — fill `{{PLACEHOLDERS}}` per it) and
  **`.domain-rules.md`** (the §4/§9/§10/§11/§12/§13 activity-scoped checklists the template references
  by §-stub — copy it alongside the template into a target repo).
- **`tools/agent-instructions/`** — install a canonical `AGENTS.md` in a target repo and wire every AI
  tool's file to it (`CLAUDE.md` `@AGENTS.md` import, Gemini config, symlink/copy), with a `--check`
  drift gate. Use it to deploy the filled playbook as a project's agent-instruction file.
- **`skills/session-kickoff/`** — the generic `/session-kickoff` skill: the project-agnostic
  *engine* (git-state guards, closed-scope collection, READY card). Project specifics come
  from a per-repo **kickoff manifest** the skill discovers (see its Step 2 search list);
  `MANIFEST-TEMPLATE.md` (v1.1) is the starter it scaffolds into manifest-less projects. The
  **manifest ratchet** keeps instantiated manifests alive: a machine-readable `manifest-audit`
  block (`last-audit` stamp · `watch` pathspecs · `verify-paths` anchors), the
  `manifest-check.sh` gate (placeholders · block parse · anchor sha · tracked anchors ·
  topological drift-vs-stamp · watch liveness; self-test `manifest-check.test.sh`), a kickoff
  read-repair step in the engine, and a DoD write-back line in the playbook (v2.2). Spec + design
  history: `memory/builds/aRatchetForge/`.
- **`tools/memory-tree/`** — an opt-in kit for a structured, machine-linted `memory/` tree: a FLAT
  `builds/<slug>/` per unit of work, one append-only `DECISIONS.md`, per-family backlog shards, index
  budgets + rotation, status vocabulary, a GENERATED work-state index (`LIVE.md` + `ledger/<month>.md`,
  rendered from build front matter — nothing about status is authored), and a 20-check hygiene gate.
  The discipline is a `streams`
  value in each spec's status header, not a directory, so a build spanning two disciplines is one
  build. Every check that has a population asserts that population is NON-EMPTY, because a
  mis-segmented path selector prints nothing and nothing is what a passing check prints. Project specifics live in one repo-root `.memory-tree.conf`; the scripts are identical
  across repos. Scaffold a fresh tree with `adopt-memory-tree.sh --scaffold`, or migrate an existing
  one in a single landing. See `tools/memory-tree/README.md`. Operationalizes the playbook's §5/§6.
- **`tools/pytest-parallel-guardrails/`** — bounded, attributable pytest-xdist runs: the four-knob
  ini recipe (`timeout` / `session_timeout` / `--max-worker-restart=0` / `faulthandler_timeout`,
  each documented by what it mechanically does), the `crashprobe.py` worker-death attribution
  plugin (a dead worker names its victim test and death mode — timeout-kill vs native crash),
  and the aiosqlite closed-loop seam patch + deterministic forced-race regression gate. See
  `tools/pytest-parallel-guardrails/README.md`.
- **`tools/gate-lint/`** — project-agnostic, drop-in linting for the GATES themselves: two lines to
  adopt, no gate legs of its own. It catches what a green suite cannot — a selector that matches the
  empty set, or an assertion between two values the same code derives. See `tools/gate-lint/README.md`.
- **`tools/hooks/agent-cap.js`** — a `PreToolUse` guard on `Workflow|Agent` that caps fan-out in both
  modalities. A direct `Agent` spawn carries no script, so it is COUNTED at runtime — each claims a
  numbered slot with `O_EXCL` under a session+prompt-keyed dir in the git common dir, and the spawn
  that finds every slot taken is denied; the budget resets on the next user prompt. A `Workflow` call
  is read statically: it DENIES any
  script calling raw `parallel(`/`pipeline(` instead of the cap-5 `boundedParallel`/`boundedPipeline`
  helpers, so a wide agent burst can't trip the server rate limiter. It enforces the second half of
  the rule too: a review's verify stage spawns at most 5 agents TOTAL. The 5 is a FILE CONSTANT and
  not overridable — the guard resolves the number at the call site, at the helper's default parameter
  and at the `gov:bounded-fanout` width, and refuses a set `AGENT_CAP` rather than ignoring it.
  Wire per WIRE-INTO-PROJECT §5; sanity-check with `tools/hooks/agent-cap.test.sh`.
  Operationalizes the playbook's §8 concurrency rule; the binding text is
  `memory/guides/REVIEW-PROTOCOL.md`.
- **`tools/codebase-map/`** — an opt-in kit for a **self-verifying codebase map**: per-feature dossiers
  whose machine claims are CI-verified against live code inventories (a both-directions ratchet —
  new moving parts fail until claimed; claims naming dead keys fail too), a shrink-only baseline,
  freshness-gated generated artifacts, and a `map_diff` git-range digest. Project specifics live in
  `.codebase-map.conf` + `tools/codebase-map/map_extractors.py`; the engine (`map_lib.py`, stdlib-only
  py≥3.11) is identical across repos. Adopt with `adopt-codebase-map.sh --scaffold`; see
  `tools/codebase-map/README.md` + `tools/codebase-map/INVENTORY-DERIVATION.md`. Operationalizes the playbook's §5/§6
  documentation-currency goals with machine enforcement.
- **`tools/workflows/tier2-review.js`** — a ready, consolidated Tier-2 review harness (find → BATCHED
  verify → synth): four finder lenses, at most five batched verifiers, one synthesis pass — 6–10
  agents over the run, of which at most 5 are verify-stage and at most 5 concurrent, per the BINDING
  `memory/guides/REVIEW-PROTOCOL.md`. Run via `Workflow({scriptPath})`, parameterized
  by `args` (base SHA, repo, context). Passes the `agent-cap` guard by construction. Findings join to
  their verdicts on an INTEGER the orchestrator assigns before the skeptic sees them — a `file:line`
  string cannot survive an echo, and two findings at one location cannot share a verdict. A finding
  with no usable verdict is UNVERIFIED, never refuted, and rides into the report as outstanding.
  Two gates guard it: `check-review-join.sh` (no ref-keyed join anywhere under `tools/`) and
  `check-workflow-syntax.js` (every workflow script still parses in the dialect its runtime uses).

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
