# Brief — dRenderedAnchor: the review protocol and the unattended Skill resolve their harness citations

**Serves:** research TOOL-dRenderedAnchor-6

## The prompt

> Do this task here: “Resolve the remaining plain harness citations”

## The brief

### Goal
In an adopter, the rendered `memory/guides/REVIEW-PROTOCOL.md` and `.claude/skills/unattended/SKILL.md` name `tools/workflows/{tier2-review,unattended-build,unattended-unit}.js`, which do not exist there: govkit installs the review-harness kit at `<prefix>/review-harness/`, and both renderers substitute `{{TOOL_ROOT}}` plainly. Render each `{{TOOL_ROOT}}<home>/<file>` citation through the receipt-aware kit resolver first, as `derive_kit_paths` already does for the memory-tree guides and the role kit's citation pass does for the /build Skill, so both documents name the paths the install holds.

### Items
1. `render()` in `tools/workflows/check-protocol-parity.test.sh` (around line 259) applies the resolved citation lines `derive_kit_paths` prints before its plain `{{TOOL_ROOT}}` substitution, each citation replaced whole.
2. The Skill render in `tools/unattended/adopt-unattended.sh` (around line 452) does the same for `tools/unattended/SKILL.template.md`.
3. Each kit carries `derive_kit_paths` inline, byte-identical to the canonical in `tools/lib/render-doc.sh`, so the existing `derive_kit_paths` parity row in `tools/lib/resolve-python.test.sh` holds the new copies.
4. One arm per renderer, each in a suite that already runs on the bar for that kit: an adopter-shaped fixture (a renamed kit directory behind a `rendered` receipt row) whose render names the renamed path, RED with the plain substitution.
5. The review-harness and unattended READMEs and any `help/` page that describe how these documents render say so.

### Acceptance
On a fresh scratch adopter install under `%TEMP%` (govkit intake --all with the four answers, apply --all, the hand render, and whatever project layer the unattended adopter needs to render its Skill), the rendered `REVIEW-PROTOCOL.md` and unattended `SKILL.md` name `tools/review-harness/tier2-review.js`, `unattended-build.js` and `unattended-unit.js`, where the scratch install `%TEMP%/rh3` at `54344d9a7` reads `tools/workflows/`. Gov's own rendered `memory/guides/REVIEW-PROTOCOL.md` and `.claude/skills/unattended/SKILL.md` stay byte-identical. Each new arm is observed RED on the plain substitution, then GREEN.

### Gates
The spec's §7 derives them; at least review-protocol parity (kit vs dogfood) · python resolver (behaviour + inline parity + idiom ban) · the unattended wiring leg · the shell hygiene legs · memory hygiene · kit version markers; then the full bar.

### Non-goals
`roles_lib.resolve_harness_path`'s probe order; `render_doc`'s unanchored substitution loop in `tools/lib/render-doc.sh`; the four inherited reds of the last bar (spec-tokens, measure-legs, govkit selftest, foreign-prefix); govkit's install layout and the receipt; running the unattended kit's own self-test suites (owner standing rule).

### Limitations
Scratch installs only under the system temp root; no write into an adopter repository. New shell lines take the no-fork forms the shell-hygiene legs require, with no registry row added or raised. Kit versions move through the lander's `mint`. Merge and push wait for the owner's explicit ask.

### Reuse
`derive_kit_paths` (canonical `tools/lib/render-doc.sh`; inline copies in `tools/memory-tree/adopt-memory-tree.sh` and `tools/memory-tree/kit-dogfood-parity.test.sh`, gated by the `derive_kit_paths` parity row). The citation-pass shape of `tools/roles/adopt-roles.sh` (TOOL-dRenderedAnchor-2, -3). Units 2 and 3's specs §3 name these two templates as this follow-up.

## Drawn from the session

> `tools/workflows/REVIEW-PROTOCOL.template.md:34` and `:202`, rendered at `tools/workflows/check-protocol-parity.test.sh:259`, and `tools/unattended/SKILL.template.md:125`, rendered at `tools/unattended/adopt-unattended.sh:452`. Both name the dead `<prefix>/workflows/` path in an adopter
— TOOL-dRenderedAnchor-2 spec §3

## Owner confirmation

Asked: Start building unit 6 on this scope?
Answer: go
