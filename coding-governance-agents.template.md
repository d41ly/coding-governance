# {{PROJECT_NAME}} — agent charter

*Rendered from the coding-governance charter template, whose version is the marker below. Section 1
binds every repository that adopts it; section 2 is this repository's own; section 3 is generated
from the kits and answers it selected. Change a source and re-render with
`<prefix>/playbook/adopt-playbook.sh`; never edit the rendered text. Every rule is one line: a tool,
gate or protocol named in section 3 carries the detail.*

<!-- governance-template: v4.5 -->

## 1. Governing practices

<!-- one-line -->
{{PRACTICES}}
<!-- /one-line -->

### Micro-formats — non-negotiable, in every final message

<!-- microformats -->
- `committed — <sha> · <branch> · <subject>`
- `pushed — <remote>/{{DEFAULT_BRANCH}} · <old>..<new> · ff · <n> commits`
- `merged — --no-ff <branch> → {{DEFAULT_BRANCH}} · <sha>[ · post-merge gates GREEN]`
- `gates — GREEN · <leg> · <leg> …`
- `skipped — <leg> · <why>`
- `up — <service> :<port> · <tree> · admin <user> · pw <pw-or-where-it-lives>`
- `READY — <slug> · node <tag> · <branch> · base <sha> · Tier-<n> · gates <list>`
- `BUILD — <slug> · Tier-<n> · <done>/<total> <step> · left <ids|none|unspecced>`
- `SPEC — [<unit-id>](<path>) · review <ids|none>[ · open <ids|none>]`
<!-- kit:roles -->
- `agent — <role> · effort <level> · model <model> · <unit-id|label> · prompt [<name>](<path>) · writes <class> · gates <legs|none> · run <run-id|direct>/<agent-id>`
- `returned — <role> · <outcome> · <wall> · <tokens> out · run <run-id|direct>/<agent-id>`
<!-- /kit:roles -->
- `unchanged — since <link> · delta <text|none>`
- `⏳ — <what is running>`
<!-- /microformats -->

<!-- one-line -->
- [never-omit] Every final message ends with the state block, short answers and conversation included; repeating it is not saying a thing twice, and omitting it is a defect.
- [events] Each event in the turn gets its shape: a commit `committed`, a push `pushed`, a merge `merged`, a bar run `gates` or `skipped`, a server `up`, a kickoff `READY`, a long run `⏳`.
<!-- kit:roles -->
- [agents] Every agent a turn dispatches gets its `agent` line and every agent it receives its `returned` line, both derived by the roles kit and never typed.
<!-- /kit:roles -->
- [r1] Emit each shape as a bare `- ` list item at column 0: no backticks, fence, bold or heading, and one shape per line.
- [grammar] A shape is a head keyword, the ` — ` joiner and fields separated by ` · `; `[ · …]` marks an optional trailing field and never appears in an emission.
- [pair] `BUILD` then `SPEC` sit adjacent in the state block of every final message while a build is in progress, one-line replies included; before a spec exists, `SPEC` is omitted.
- [fields] `SPEC`'s link label is the unit id, `BUILD`'s Tier is the current step's, and `review` and `open` count Tier-2 units build-wide.
- [gates-line] The `gates` line names every leg the gate manifest defines; a leg not run is a `skipped` line, and a failed leg is prose above everything.
- [state] A final message opens with its highest-severity item and ends with ONE state block: branch, shas, gates and servers.
- [links] Cite files as `[text](path)` links, forward-slashed and resolved from the session's working directory.
<!-- /one-line -->

## 2. This repository

<!-- one-line -->
{{ADOPTER_RULES}}
<!-- /one-line -->

## 3. Generated

*From the kits and answers this repository selected. Re-render to change it.*

## Node registry

{{NODE_TABLE}}

<!-- one-line -->
- Identify your node by machine and user, never by path: every node's checkout may sit at one path.
- A node claims its tag once, in gov, with `<prefix>/playbook/render_playbook.py --claim-node`, re-rendering gov's own charter in that commit; other repositories get it at `govkit update`.
- Onboarding a node: clone to its primary tree, claim its tag, seed local memory from the in-repo mirror, and recreate its worktrees, which never sync.
<!-- /one-line -->

## Tools to rely on

<!-- one-line -->
<!-- kit:kickoff-manifest -->
- `/session-kickoff` opens every unit: it orients, loads this repository's kickoff manifest and derives a closed scope.
<!-- /kit:kickoff-manifest -->
<!-- kit:memory-tree -->
- `<prefix>/memory-tree/gotchas.py --for-diff <base>..<head>` lists the bug classes a diff can hit; run it before any review.
<!-- /kit:memory-tree -->
<!-- kit:codebase-map -->
- Read a feature's codebase-map dossier first, and run `reuse_lookup.py "<behaviour>"` before building anything new.
<!-- /kit:codebase-map -->
<!-- kit:memory-recall -->
- `/memory-recall` answers why a thing is the way it is from the decision records; a symbol, caller or filename is still a grep.
<!-- /kit:memory-recall -->
<!-- kit:drift-audit -->
- `/drift-audit` measures whether this repository's records still match its tree; run it when the state feels unclear.
<!-- /kit:drift-audit -->
<!-- kit:lexicon -->
- `/lexicon` answers what to call a new function, type or command from `{{LEXICON_CONF}}`, before the name is written.
<!-- /kit:lexicon -->
<!-- kit:review-harness -->
- `<prefix>/workflows/tier2-review.js` runs a Tier-2 review as one bounded `Workflow`.
<!-- /kit:review-harness -->
<!-- kit:agent-cap -->
- The agent-cap hook refuses an unbounded fan-out at the tool call; consolidate the fan-out rather than routing around it.
- The write gate refuses a product-code write that no specced unit owns; route the unit through `/session-kickoff` first.
<!-- /kit:agent-cap -->
<!-- kit:roles -->
- An attended code build runs through `/build`.
<!-- /kit:roles -->
<!-- kit:unattended -->
- `/unattended` starts, resumes or closes a run that merges and pushes with no owner turn.
<!-- /kit:unattended -->
<!-- kit:runlog -->
- `/runlog` answers what an unattended run did, decided or cost, and why it stopped.
<!-- /kit:runlog -->
<!-- kit:push-main -->
- `<prefix>/push-main.sh` lands and pushes the default branch, and nothing bypasses it.
<!-- /kit:push-main -->
<!-- kit:process-monitor -->
- `<prefix>/process-monitor/reap.py` reaps processes past their declared ceiling; `--dry-run` lists them first.
<!-- /kit:process-monitor -->
<!-- kit:pytest-parallel-guardrails -->
- Parallel pytest runs take the guardrails kit's settings: per-file isolation, per-test timeouts, fail-fast on worker death, crash attribution, structural test classes and opt-in parallelism.
<!-- /kit:pytest-parallel-guardrails -->
<!-- kit:gate-lint -->
- The gate-lint scans catch shell failures that are silent by construction, such as case-colliding PowerShell names and BOM-less non-ASCII.
<!-- /kit:gate-lint -->
<!-- /one-line -->

<!-- kit:roles -->
## Agent roles — hand the work to its role

<!-- one-line -->
{{ROLE_ROSTER}}
<!-- /one-line -->

<!-- /kit:roles -->
## Drive — how to start and advance the loop

<!-- one-line -->
{{DRIVE}}
<!-- /one-line -->

## Protocols — read the one whose trigger holds

<!-- one-line -->
<!-- kit:memory-tree -->
- A build of more than one pass: `{{MEMORY_ROOT}}/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `{{MEMORY_ROOT}}/TEMPLATE-SPEC.md`.
- Any record, index or id under `{{MEMORY_ROOT}}/`: `{{MEMORY_ROOT}}/HYGIENE.md`.
<!-- /kit:memory-tree -->
<!-- kit:review-harness -->
- Any review or `Workflow` fan-out: `{{MEMORY_ROOT}}/guides/REVIEW-PROTOCOL.md`.
<!-- /kit:review-harness -->
<!-- kit:unattended -->
- A run that merges and pushes with no owner turn: `{{MEMORY_ROOT}}/guides/UNATTENDED-PROTOCOL.md`.
<!-- /kit:unattended -->
<!-- /one-line -->

## Facts

- **Product:** {{PRODUCT_PREAMBLE}}.
- **Layout:** {{REPO_LAYOUT_MAP}}.
- **Product context:** {{PRODUCT_CONTEXT_HOME}}.
- **Commands:** {{COMMAND_CATALOG}}.
- **The merge bar:** `{{GATE_RUNNER}}`, wired into remote CI at `{{CI_FILE}}`; {{GATE_COMMANDS}}.
- **Ids and records:** families {{ID_FAMILIES}}; streams {{MEMORY_DISCIPLINES}}; Tier-2 reviews persist under `{{REVIEW_DIR}}`.
- **Reading order:** {{DOC_ROUTING_TABLE}}.
- **Streams:** {{STREAM_OWNERSHIP}}.
- **Worktrees:** {{WORKTREE_SCRIPT}}.
- **Kinds:** {{KIND_FACTORY_MAP}}. Shared primitives: {{SHARED_PRIMITIVES_LOCATION}}.
<!-- when:cross-os -->
- **Toolchain:** {{TOOLCHAIN_NOTES}}.
<!-- /when:cross-os -->
- **Commit trailer:** every agent commit ends with `{{COMMIT_TRAILER}}`.
