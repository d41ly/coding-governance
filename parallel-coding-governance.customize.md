# Customizing the governance playbook (one-time, at instantiation)

Deploy-time companion to `parallel-coding-governance.template.md`. The template is the **operational
ruleset** an agent reads every session; THIS file holds the one-time instructions for filling it into
a project. Not read during normal work — only when instantiating or re-pulling the template.

**Who / how:** the agent, one-time. **TWO files deploy together, and both carry placeholders:**
`parallel-coding-governance.template.md` (the ruleset) and
`parallel-coding-governance.domain-rules.md` (the activity-scoped §-checklists the template reaches
by §-stub). Read the repo to fill the discoverable placeholders in BOTH; ask the user ONLY for what
isn't in the code (the *(ask user)* items below); propose-and-flag anything inferred; write the
filled template to the project's governing doc (its agent-instruction file, e.g. `AGENTS.md` /
`CLAUDE.md`, or `docs/PARALLEL.md`) and place the filled companion beside it under the name the
template's §-stubs spell. Then run `grep -nE '\{\{[A-Z]'` over **both** written files to confirm no
placeholder survived — a template-only grep passes green while 14 of the 36 placeholders sit
unfilled in the companion, and the §-stubs then point at a file the project never received.

## Placeholders

36 in total: 23 in the template and 14 in the companion, which sums to 37 because the groups are
**not disjoint**. **1 shared: `{{MEMORY_ROOT}}`** — it appears in both files and must be filled
IDENTICALLY in each. Every other placeholder is filled in exactly one place.

The counts below are per-file and each is individually correct; the union is what the 36 counts.
Do not read a per-file heading as a share of the total.

### In `parallel-coding-governance.template.md` — 23

- `{{PROJECT_NAME}}` — the repo this governs (discoverable, not an ask).
- **Fleet** *(ask user)*: node-registry rows `{{TAG_A}}` / `{{MACHINE_A}}` / `{{PRIMARY_TREE_A}}` /
  `{{WORKTREE_ROOT_A}}` / `{{VARIANCES_A}}` (one row per node) · `{{STREAM_OWNERSHIP}}` (stream → node).
- **Records & docs**: `{{ID_FAMILIES}}` · `{{DOC_ROUTING_TABLE}}` · `{{PRODUCT_PREAMBLE}}` ·
  `{{REPO_LAYOUT_MAP}}` · `{{COMMAND_CATALOG}}` · `{{PRODUCT_CONTEXT_HOME}}` · `{{HELP_DIR}}` ·
  `{{REVIEW_DIR}}`.
- **Gates & git**: `{{GATE_COMMANDS}}` · `{{CI_FILE}}` · `{{GATE_RUNNER}}` · `{{COMMIT_TRAILER}}` ·
  `{{WORKTREE_SCRIPT}}`.
- **Memory tree** — REQUIRED, not a choice: §5's work-state rules and §6's record protocol both
  assume it. `{{MEMORY_ROOT}}` (default `memory`) — **SHARED: this is the one placeholder that
  also appears in the companion group below, and both must be filled identically** · `{{MEMORY_DISCIPLINES}}`, which is a **closed
  enum of stream values**, space-separated — **not** a list of directories. The tree is flat: every
  build folder sits directly under `<MEMORY_ROOT>/builds/<slug>/` and each spec declares its own
  stream in its status header. The stream→FAMILY map is a **separate** `FAMILIES` key in the
  repo-root `.memory-tree.conf`, not part of this placeholder; `{{ID_FAMILIES}}` supplies the
  families. Adopt with `<kit-dir>/adopt-memory-tree.sh --scaffold` for a new tree, or a one-landing
  migration for an existing one — `<kit-dir>` is wherever the kit was installed (`memory-tree/` at
  the project root by default). The kit README names the remaining conf keys the gate needs armed,
  including the pins that are MEASURED per corpus and never inherited from another repo.
- **Output discipline**: `{{PROSE_AUDIT}}` (the audit-script location, or "none yet — thresholds still bind").

### In `parallel-coding-governance.domain-rules.md` — 14

- **§1 unattended runs**: `{{MEMORY_ROOT}}` — **SHARED with the template group above; fill both
  identically.** The memory tree's root, matching the memory-tree kit's
  conf. It resolves the pointer to the unattended protocol; the block states no rule of its own.
- **§4 runtime & verification**: `{{PORT_OFFSET}}` · `{{BUILD_TIME_BAKES}}` · `{{VERIFY_RECIPE}}`.
- **§11 toolchain**: `{{TOOLCHAIN_NOTES}}`.
- **§12 architecture**: `{{KIND_FACTORY_MAP}}` · `{{SHARED_PRIMITIVES_LOCATION}}`.
- **§13 design system**: `{{TOKENS_LOCATION}}` · `{{SPACING_SCALE}}` · `{{TYPE_SCALE}}` ·
  `{{BREAKPOINTS}}` · `{{MIN_TOUCH_TARGET}}` · `{{GALLERY_ROUTE}}` · `{{VISUAL_CONTRACT_DOC}}`.

## Conditional sections (delete when they don't apply)

- **Codebase-map lines** (§1 DoR, §1 DoD, §5 kit bullet, §7 gates line): keep only if adopting the
  `codebase-map/` kit — else delete all four.
- **Memory-recall line** (the §5 kit bullet): keep only if adopting the `memory-recall/` kit — which
  needs the memory tree, since the kit refuses without `.memory-tree.conf`.
- **Unattended-run lines** (the `, or a committed build folder …` clause in §1's Landing block,
  and companion §1's second block): keep only if adopting the `unattended/` kit — else delete the
  clause, restoring the unamended explicit-ask rule, and delete the companion block. §8 no longer
  carries a second spelling of the landing rule; it points at §1. Companion §1's FIRST block (the kickoff-manifest merge
  exception) is independent of this kit and stays whenever the project keeps a manifest. The clauses
  are written to stay true without the kit — they say the merge bar validates the mandate's shape,
  and a project with no such bar has no mandate — but a repo that keeps them without the kit is
  carrying a rule nothing can make true, which is the drift this row exists to prevent.
- **§9** lines about outbound calls / stored HTML — drop if there's no such surface.
- **§11** — drop for single-OS teams.
- **§4** harness lines and **§13** entirely — drop if the project has no UI.
- **§15** persona is adjustable per project; its facts-over-wit rules are not.
- Everything else is universal core — keep verbatim. The memory-tree kit is NOT droppable: it is the
  only thing §5's derived work-state index and §6's record protocol can be read against.
- Dropping a template §-stub means dropping the matching section in the companion too — a companion
  section no stub routes to is never loaded by anyone.

## Re-pulling an upgraded template

Both files carry `<!-- governance-template: vN.N -->`, and they are re-pulled **in lockstep** — a
stale companion beside a fresh template is the failure this marker exists to make visible, so diff
both and confirm both markers read the same version. Pull improvements by diffing your filled copy
against the current source per §-body (ignore filled placeholders). The v2.0 format rework defeats
§-body diffing against pre-2.0 copies (re-adopt section-by-section once); v2.0+ diffs cleanly.
Version history lives in the `…-v-N-N.md` snapshots (under `memory/archive/` in this repo) and in
git history.
