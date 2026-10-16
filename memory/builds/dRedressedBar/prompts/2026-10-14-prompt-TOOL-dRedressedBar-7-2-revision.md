# Revision — dRedressedBar: TOOL-dRedressedBar-7, the builder's divergence on the mint's false carrier

**Serves:** research TOOL-dRedressedBar-7

## The brief

### Goal
DIVERGENCE: §4 step 2 (S3, mint) and §3 (Non-goals) of memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md assume `govkit.py mint --base ebce889c7` writes only version carriers. On this tree it also rewrites a line that is not a carrier. Committing its output as it stands turns AC4 red. Changing that output by hand is an edit §3 does not allow ("No generated output is edited by hand", "The minter computes every value"). Fixing the cause is product logic, and §4 says this unit moves none. The mint moved exactly the four kits in §4's table: agent-cap 1.38->1.39, branch-reconcile 1.4->1.5, roles 1.5->1.6 and unattended 1.106->1.107. `write_version_carriers` (tools/govkit/govkit.py:798) also rewrote tools/playbook/render_playbook.py:1646, the selftest fixture `older_tpl = '<!-- governance-template: v3.5 -->...'`, from v3.5 to v1.28, because the `playbook` entry's version pattern matches the line. The owner chose to fix the class in a new unit, TOOL-dRedressedBar-20, ordered before this one.

### Items
1. **TOOL-dRedressedBar-7** — bump the rev. Add `- **consumes-from** \`TOOL-dRedressedBar-20\`` to §3 Edges: this unit's mint runs over unit 20's tightened carrier writer, and without it the mint writes the false carrier. In §4 step 2, state that the mint must move exactly the four kits in the table and write no file outside their carriers and renders, and that a mint writing any other file stops the pass. Add the `regen.py --check` observation the builder made, `10 fresh · 2 stale` before the write (the gotchas INDEX and the build index), if the spec pins a different count. Nothing else moves.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades TOOL-dRedressedBar-7 READY, and its Edges carry the `consumes-from` to unit 20.

### Gates
`kit epoch` · `memory hygiene`

### Non-goals
- No code. No edit to unit 20's spec, which a sibling writer is authoring concurrently.
