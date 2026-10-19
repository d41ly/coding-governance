# Brief — dRenderedAnchor: the resolver finds rendered harnesses in an adopter, and the role index is gated

**Serves:** research TOOL-dRenderedAnchor-1

## The prompt

> Task:
> 1. Reproduce on a fresh scratch install under the system temp root (never write into an adopter repository, never run govkit update/adopt scripts in write mode against a real repository). Confirm where the kit lands, what the receipt rows' `source` fields hold for rendered harnesses, and the agent-cap verdict.
> 2. Find the root cause (kit install dir vs `home`, and the template-sourced receipt row that `resolve_kit_dir` cannot match), and fix it so `roles.json` lists the paths that exist in the install and the spawn guard admits gov's own harnesses.
> 3. Gate the class: a check that reds when any harness path in a rendered `roles.json` does not exist in the install, seen red on the current behaviour first.
> Follow AGENTS.md: open the unit through the kickoff, spec before code, Tier the change (a shipped kit edit is Tier-2), and land only on the owner's explicit ask.

## The brief

### Goal
In an adopter, `resolve_kit_dir` finds a rendered file through the receipt row that names its template, so `.claude/roles.json` lists the review-harness kit's harnesses where they are installed and agent-cap admits them; and the role render reds a harness it lists at a path the install does not hold while a file of that name is installed elsewhere.

### Items
1. The defect reproduced on a fresh scratch install: where the kit lands, the rendered rows' `source`, the agent-cap verdict.
2. The resolver's receipt step also matches a row whose `source` sits directly under `<home>/` and whose `path` basename is `<anchor>`; the canonical in `tools/lib/resolve_kit_dir.py` and every inline copy, byte-identical.
3. A red in `render_agents.py --check` (the `roles render wiring` leg): a listed harness absent from the install while a tracked file of its basename exists elsewhere.
4. A `render_agents.py --selftest` arm over an adopter-shaped fixture: the kit directory renamed and its rendered harness's receipt row sourced from the template.

### Acceptance
1. The repro record under `build/` names the commands and the measured outputs.
2. On a fresh scratch install after the fix, `roles.json` harnesses are `tools/review-harness/{tier2-review,unattended-build,unattended-unit}.js`, each on disk, and agent-cap returns rc 0 for the `tier2-review.js` payload that returned rc 2.
3. On the pre-fix scratch install, the new `--check` red fires naming both misplaced harnesses; after the fix, it is green.
4. The new selftest arm is RED against the pre-fix resolver and GREEN after.

### Gates
roles render selftest · roles render wiring · roles catalogue · python resolver (behaviour + inline parity + idiom ban) · kit version markers · install-prefix (shipped surface); then the full bar.

### Non-goals
Where govkit installs a kit (`<prefix>/<id>` stays); the receipt's `source` semantics; agent-cap.js; `.claude/rules/product.md`; a red for a harness found nowhere in the install.

### Limitations
Scratch installs only under the system temp root; no write into an adopter repository; no govkit `update --write` or adopt against a real repository. Kit versions move through the lander's `mint`, not by hand. Merge and push wait for the owner's explicit ask.

### Reuse
`tools/lib/resolve_kit_dir.py` is the seam: its receipt step exists and one predicate widens. `tools/roles/render_agents.py`'s `derive_harness_paths`, `--check` and `--selftest` fixture builder carry the gate. `tools/lib/resolve-python.test.sh`'s parity table proves the copies agree. Recall returned TOOL-aRepatriatedFork-2 (the resolver's design), TOOL-aMendedFleet-102 (drifted copies re-synced), TOOL-aOrientedCast-8 (review-harness absence is a note) and TOOL-dRedressedBar-14/-15 (per-kit prefix receipt).

## Drawn from the session

> The resolver's receipt match ignores rendered rows (source = the .template.js). Fixing the resolver itself touches its ~70 byte-identical copies across ~25 kits (all re-versioned at the lander); fixing only roles' harness lookup touches one kit.
— agent, kickoff fork question

## Owner confirmation

Asked: Where should the fix live? · The new gate reds when a harness path in roles.json doesn't exist. roles' descriptor declares 'review-harness not installed' an accepted note. How should that case grade? · Declare `spec-audit:` for this build? · Start the build on this scope?
Answer: Resolver (Recommended) · Exempt not-installed (Recommended) · No · go
