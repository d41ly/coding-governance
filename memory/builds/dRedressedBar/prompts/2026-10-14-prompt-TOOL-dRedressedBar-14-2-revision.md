# Revision — dRedressedBar: TOOL-dRedressedBar-14 rev-2, F1 resolved, and the edges it implies

**Serves:** research TOOL-dRedressedBar-14

## The brief

### Goal
The owner resolved unit 14's §8 F1 as option (a), 2026-10-14. agent-cap's cross-kit adopter argv is
its own unit, `TOOL-dRedressedBar-15`, ordered after 14, and the reproduction's "exits 0" moves to
unit 15's close. Revise the three specs whose edges this moves, each as a rev bump with its §9 line:
1. **Spec 14** to rev-2: mark F1 `RESOLVED (owner, 2026-10-14): (a)` in place, and add
   `- **hands-off** \`TOOL-dRedressedBar-15\`` for agent-cap's exit 2. AC1's pinned remaining exit 1
   stands.
2. **Spec 11**: its `hands-off external` line for the apply-prefix defect becomes two lines,
   `- **hands-off** \`TOOL-dRedressedBar-14\`` for settings-merge's half and
   `- **hands-off** \`TOOL-dRedressedBar-15\`` for agent-cap's half, matching the
   `consumes-from` each of those specs declares toward it. If spec 15 declares no edge to 11, write
   only the 14 line and keep agent-cap's half external.
3. **Spec 12**: add `- **hands-off** \`TOOL-dRedressedBar-14\``, matching spec 14's `consumes-from`.

Read spec 15, which a sibling writer is authoring concurrently, once it exists, so the mirrored edges
match its declared ones. Do not edit it.

### Items
1. The three revisions above. Nothing else in any spec moves.

### Acceptance
`bash tools/unattended/unattended.sh --plan dRedressedBar --paths` grades 11, 12 and 14 READY, and
every `consumes-from` among units 11, 12, 14 and 15 has its mirrored `hands-off`.

### Gates
`memory hygiene`

### Non-goals
- No code. No edit to spec 15.

### Limitations
- Children run no bar and no whole suite.

### Reuse
The edge grammar in `memory/TEMPLATE-SPEC.md` §3 Edges.
