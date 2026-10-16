# Brief — dRedressedBar: govkit's mint writes a version into another entry's file

**Serves:** research TOOL-dRedressedBar-20

## The prompt

> Fix the class (Recommended)

## The brief

### Goal
TOOL-dRedressedBar-7's builder ran `python tools/govkit/govkit.py mint --base ebce889c7`. It bumped the four kits it should (agent-cap, branch-reconcile, roles, unattended). `write_version_carriers` (`tools/govkit/govkit.py:798`) also rewrote `tools/playbook/render_playbook.py:1646`, a selftest fixture `older_tpl = '<!-- governance-template: v3.5 -->...'`, from v3.5 to v1.28. The `playbook` entry's version pattern `governance-template: v` (`tools/govkit/entries/playbook.kit.toml:6`) matches the line. The line sits in playbook-render's file group, and the file carries only playbook-render's marker, so the ownership clause at `govkit.py:862-869` hands the number to playbook-render's version. That moves playbook-render's shipped bytes without bumping it, and `derive_epoch_state` over the mint's output reads `playbook-render FAILED · moved … · no value change (still 1.28)`. Every later mint that bumps any kit, the lander's included, rewrites the line again. The owner chose to fix the class (2026-10-14): an entry's version pattern counts only inside that entry's own file group.

### Items
1. **TOOL-dRedressedBar-20 — a version pattern counts only inside its own entry's file group.** Tighten `write_version_carriers` and its ownership clause so a match of entry A's pattern in a file that entry A does not ship is never written. Find every other reader of entry version patterns (the epoch check, the markers check, any `version_from` reader) and make them agree, or state why each already does. Reproduce first: a mint over `ebce889c7` on a scratch copy rewrites `render_playbook.py:1646`; over the fix it does not, and the four kits still move. Add a selftest arm that stages a foreign-pattern line in another entry's file and asserts the mint leaves it alone. Run the class predicate over the real registry first: name every file where one entry's pattern matches inside another entry's group.
   - Edges: `hands-off TOOL-dRedressedBar-7`, which mints after this lands.
   - Order: 4, before unit 7 (order 5). Unit 6, the other order-4 unit, is CLOSED, and the write sets are disjoint.
   - `tools/govkit/` is version-exempt, so this unit bumps no kit. If the fix moves another kit's shipped bytes, say so and bump it.
   - If it adds or renames a function in a mapped file, run `python tools/codebase-map/gen_map.py --write` alone and commit `memory/map/generated/symbols.json` with the pass.

### Acceptance
`govkit.py mint --base ebce889c7` over the fix rewrites `render_playbook.py:1646` nowhere and still moves the four kits. The new selftest arm reds when the tightening is removed. `derive_epoch_state` over a scratch commit of the post-fix mint output reads no FAILED for playbook-render.

### Gates
`govkit selftest` · `govkit acceptance matrix` · `govkit selfcheck` · `kit epoch` · `kit version markers` · `codebase-map coverage + freshness` · `memory hygiene`

### Non-goals
- No change to which kits mint, or to any kit's version numbering scheme.
- No hand edit of a generated output.
- No merge to local main and no push without the owner's ask.

## Drawn from the session

> Fix the class (Recommended)
— owner, 2026-10-14, answering unit 7's mint divergence

## Owner confirmation

Asked: Unit 7 found that `govkit mint` falsely rewrites a test-fixture line … How should this build handle it?
Answer: Fix the class (Recommended)
