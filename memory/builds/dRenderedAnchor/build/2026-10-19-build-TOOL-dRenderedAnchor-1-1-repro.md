# TOOL-dRenderedAnchor-1 — the defect reproduced on a fresh scratch install

**Serves:** research TOOL-dRenderedAnchor-1

Measured 2026-10-19 on node `d` from gov at `a60b0c7dc`, into an empty scratch repository under the
system temp root. The defect was first reported by dClosedLoop's dispatch 123 (its flow-today record,
section "A defect found on the way"), measured there at `320c79646`. No adopter repository was written.

## Instruments

Each command ran in Git Bash. `T` is `%TEMP%/rh1`, a fresh `git init` with one commit holding a stub
`.github/workflows/ci.yml`, `core.autocrlf false`.

1. `python tools/govkit/govkit.py intake --target $T --all --answer gate_file=.github/workflows/ci.yml
   --answer manifest_path=memory/guides/SESSION-KICKOFF.md --answer
   playbook_path=coding-governance-agents.template.md --answer user_skills=$T.userskills` — rc 0,
   26 kits.
2. `python tools/govkit/govkit.py apply --target $T --all` — rc 0, 255 files landed, 365 receipt rows.
   The four rendered harnesses are SKIPPED by apply ("nothing in this install produces it"), and the
   roles adopter stops at exit 3, no governing doc.
3. In `$T`: `bash tools/review-harness/check-protocol-parity.test.sh --render` — the runbook's
   hand render; it wrote the four harnesses beside their templates.
4. In `$T`: gov's `AGENTS.md` copied in as a stand-in governing doc, then
   `bash tools/roles/adopt-roles.sh --scaffold` — rc 0, `.claude/roles.json` written.
5. In `$T`: a `PreToolUse` `Workflow` payload per `scriptPath`, piped into
   `node tools/hooks/agent-cap.js` with `CLAUDE_PROJECT_DIR` set to the target.

## Results

**Where the kit lands.** `tools/review-harness/`, the entry's id. No `tools/workflows/` exists.
govkit's per-entry `{kit}` is `<tool root>/<id>`, while `workflows.toml` spells
`{prefix}/<home>/<file>`. Three kits differ that way: agent-cap (`hooks`), playbook-render
(`playbook`) and review-harness (`workflows`).

**The receipt rows.** A rendered harness's `source` is its template:

```text
  rendered  tools/workflows/unattended-build.template.js               -> tools/review-harness/unattended-build.js
  rendered  tools/workflows/tier2-review.template.js                   -> tools/review-harness/tier2-review.js
  rendered  tools/workflows/drift-audit-code.template.js               -> tools/review-harness/drift-audit-code.js
  rendered  tools/workflows/drift-audit-state.template.js              -> tools/review-harness/drift-audit-state.js
  engine    tools/workflows/unattended-unit.js                         -> tools/review-harness/unattended-unit.js
```

`resolve_kit_dir("workflows", "tier2-review.js", <tool root>)` compares `source`'s last two segments
with `[workflows, tier2-review.js]`, finds no row, probes `tools/workflows/` and raises.
`roles_lib.resolve_harness_path` catches that and returns `<tool root>/workflows/<file>`, unheld.
`unattended-unit.js` is an engine file, so its row matches.

**The render.** `adopt-roles.sh --scaffold` printed:

```text
render_agents: note — tools/workflows/tier2-review.js is named by the workflow table and absent here; its kit is not installed
render_agents: note — tools/workflows/unattended-build.js is named by the workflow table and absent here; its kit is not installed
```

`.claude/roles.json` `harnesses`: `['tools/review-harness/unattended-unit.js',
'tools/workflows/tier2-review.js', 'tools/workflows/unattended-build.js']`; existence on disk
`True, False, False`.

**The spawn guard.**

| scriptPath | rc | verdict |
|---|---|---|
| `tools/review-harness/tier2-review.js` | 2 | rule 6: not a declared harness |
| `tools/review-harness/unattended-build.js` | 2 | rule 6: not a declared harness |
| `tools/review-harness/unattended-unit.js` | 0 | admitted |
| `tools/workflows/tier2-review.js` | 2 | could not be read (ENOENT) |

So neither spelling of the review harness runs in a default adopter.

## Root cause

Two facts meet. govkit homes an installed kit by its id, so the directory name an adopter holds is
not gov's `home`; the receipt is the one record of that rename. And the receipt row for a rendered
file names the template it was rendered from, so the resolver's receipt step, keyed on
`<home>/<anchor>` in `source`, cannot see any rendered anchor. The resolver's probe step then misses
too, because the directory is renamed. Any caller passing a rendered anchor fails the same way; the
role render is the only one today.
