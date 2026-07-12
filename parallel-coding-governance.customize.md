# Customizing the governance playbook (one-time, at instantiation)

Deploy-time companion to `parallel-coding-governance.template.md`. The template is the **operational
ruleset** an agent reads every session; THIS file holds the one-time instructions for filling it into
a project. Not read during normal work — only when instantiating or re-pulling the template.

**Who / how:** the agent, one-time — read the repo to fill discoverable placeholders; ask the user
ONLY for what isn't in the code (the *(ask user)* items below); propose-and-flag anything inferred;
write the filled result to the project's governing doc (its agent-instruction file, e.g. `AGENTS.md`
/ `CLAUDE.md`, or `docs/PARALLEL.md`); then `grep -nE '\{\{[A-Z]'` to confirm no placeholder survived.

## Placeholders

- `{{PROJECT_NAME}}` — the repo this governs (discoverable, not an ask).
- **Fleet** *(ask user)*: node-registry rows `{{TAG_A}}` / `{{MACHINE_A}}` / `{{PRIMARY_TREE_A}}` /
  `{{WORKTREE_ROOT_A}}` / `{{VARIANCES_A}}` (one row per node) · `{{STREAM_OWNERSHIP}}` (stream → node).
- **Records & docs**: `{{ID_FAMILIES}}` · `{{DOC_ROUTING_TABLE}}` · `{{PRODUCT_PREAMBLE}}` ·
  `{{REPO_LAYOUT_MAP}}` · `{{COMMAND_CATALOG}}` · `{{PRODUCT_CONTEXT_HOME}}` · `{{HELP_DIR}}` ·
  `{{REVIEW_DIR}}`.
- **Gates & git**: `{{GATE_COMMANDS}}` · `{{CI_FILE}}` · `{{GATE_RUNNER}}` · `{{COMMIT_TRAILER}}` ·
  `{{WORKTREE_SCRIPT}}` · `{{TOOLCHAIN_NOTES}}`.
- **Runtime & verification**: `{{PORT_OFFSET}}` · `{{BUILD_TIME_BAKES}}` · `{{VERIFY_RECIPE}}`.
- **Architecture & design system**: `{{KIND_FACTORY_MAP}}` · `{{SHARED_PRIMITIVES_LOCATION}}` ·
  `{{TOKENS_LOCATION}}` · `{{SPACING_SCALE}}` · `{{TYPE_SCALE}}` · `{{BREAKPOINTS}}` ·
  `{{MIN_TOUCH_TARGET}}` · `{{GALLERY_ROUTE}}` · `{{VISUAL_CONTRACT_DOC}}`.
- **Memory tree** (only if adopting the `tools/memory-tree/` kit — else drop these + the two §5
  memory-tree lines from the template): `{{MEMORY_ROOT}}` (default `memory`) · `{{MEMORY_DISCIPLINES}}`
  (space-separated discipline folders + their discipline→FAMILY id map, written into the repo-root
  `.memory-tree.conf`; `{{ID_FAMILIES}}` supplies the families). Adopt via
  `tools/memory-tree/adopt-memory-tree.sh --scaffold` (new tree) or a one-landing migration (existing).
- **Output discipline**: `{{PROSE_AUDIT}}` (the audit-script location, or "none yet — thresholds still bind").

## Conditional sections (delete when they don't apply)

- **Codebase-map lines** (§1 DoR, §1 DoD, §5 kit bullet, §7 gates line): keep only if adopting the
  `tools/codebase-map/` kit — else delete all four.
- **§9** lines about outbound calls / stored HTML — drop if there's no such surface.
- **§11** — drop for single-OS teams.
- **§4** harness lines and **§13** entirely — drop if the project has no UI.
- **§15** persona is adjustable per project; its facts-over-wit rules are not.
- Everything else is universal core — keep verbatim.

## Re-pulling an upgraded template

The template carries `<!-- governance-template: vN.N -->`. Pull improvements by diffing your filled
copy against the current source per §-body (ignore filled placeholders). The v2.0 format rework
defeats §-body diffing against pre-2.0 copies (re-adopt section-by-section once); v2.0+ diffs cleanly.
Version history lives in the `…-v-N-N.md` snapshots (under `memory/playbook/archive/` in this repo)
and in git history.
