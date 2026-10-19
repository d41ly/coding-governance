# Brief — dRenderedAnchor: the closing review's findings on unit 1, and the /build Skill's harness paths

**Serves:** research TOOL-dRenderedAnchor-2

## The prompt

> Fold it into the batch unit TOOL-dRenderedAnchor-2 alongside the 8 promoted findings? — Include in unit 2 (Recommended)

## The brief

### Goal
Close every confirmed finding of unit 1's closing diff review as one batch unit, and render the /build Skill's harness citations through the resolver, so an adopter's misplaced-harness red fires only on the review harness's own files, every term of the widened join has a gate that can fail, the blast-radius record is complete, every reader of the role index agrees, and /build calls the harness paths agent-cap admits.

### Items
1. M1 + L1 — `scan_misplaced_harnesses` counts a hit only where the directory shows the file is the review harness's own: the harness's `<stem>.template.js` beside it, or, for an engine harness with no template, a `kit.toml` there declaring `id = "review-harness"`. It still reads the disk, never the receipt or the resolver. Arm 17 plants the marker; a new arm 18 (with a prefix, and at a root install) shows an unrelated namesake prints the note and exits 0.
2. M2 — a `resolve_kit_dir` behaviour arm in `tools/lib/resolve-python.test.sh` replaying the six receipt rows of unit 1's spec §4, plus decoy rows ahead of the real one in arm 16's receipt, each term (role, home) observed RED when dropped.
3. M3 + L2 — the callers record completed: the three `{{TOOL_ROOT}}` citation loops (`tools/lib/render-doc.sh` `derive_kit_paths`, `tools/memory-tree/adopt-memory-tree.sh`, `tools/memory-tree/kit-dogfood-parity.test.sh`), `tools/check-kit-versions.sh`'s `WF_DIR`, and the templates whose citations now resolve differently, in this unit's spec and in the repro record's root-cause paragraph; a `derive_kit_paths` arm asserting the review-harness citation resolves to `<prefix>/review-harness/tier2-review.js` under a rendered receipt row, RED on the `a60b0c7d` block; whether `govkit update` reports the re-rendered guides as drift in an existing adopter, observed and recorded.
4. L3 — `tools/check-wiring.sh`'s roles arm gives the same verdict as `render_agents --check` on a misplaced harness, pinned by a `check-wiring.test.sh` fixture, or the help text names the one reader that says `misplaced`.
5. L4 — `memory/map/features/roles.md` states the final rule, lists TOOL-dRenderedAnchor-1 and -2 in its decisions, and its receipt-contract bullet names the rendered-row join.
6. L5 — `help/roles.md`, the `MISPLACED_LINE` comment, the line's text and the render docstring state the scan's actual predicate, written after item 1 lands.
7. The /build Skill (`tools/roles/SKILL.template.md` rendered by `tools/roles/adopt-roles.sh` to `.claude/skills/build/SKILL.md`) names each harness at the path the install holds, resolved through the same resolver the role index uses, not by plain `{{TOOL_ROOT}}` substitution; gov's own render stays byte-identical.

### Acceptance
1. Arm 18 RED against unit 1's scan, GREEN after; arm 17 still reads `misplaced` with its marker planted.
2. The resolver behaviour arm RED with the role term dropped and, separately, with the home term dropped; GREEN on the shipped block.
3. The `derive_kit_paths` arm RED on the `a60b0c7d` block, GREEN after; the spec's callers table and the repro record name every dynamic caller.
4. On one misplaced tree, check-wiring's roles arm and `render_agents --check` give the same verdict, or the help text says only the render reports it.
5. The roles feature map, `help/roles.md`, the README and the render's text all state the shipped predicate.
6. On a fresh scratch adopter install, `.claude/skills/build/SKILL.md` names `tools/review-harness/tier2-review.js` and `tools/review-harness/unattended-build.js`, and gov's own rendered Skill is unchanged.

### Gates
The unit's spec §7 derives them from the files it touches; at least roles render selftest · roles render wiring · roles adopter self-test · python resolver (behaviour + inline parity + idiom ban) · check-wiring self-test · memory hygiene; then the full bar.

### Non-goals
Where govkit installs a kit; the receipt's `source` semantics; agent-cap.js; a red for a harness found nowhere; the awk reader's join.

### Limitations
Scratch installs only under the system temp root; no write into an adopter repository. Kit versions move through the lander's `mint`. Merge and push wait for the owner's explicit ask.

### Reuse
The review record names each fix and the skeptic's verdict on it: `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md`. Unit 1's spec §4 holds the six-row table and the callers table this unit completes. `derive_kit_paths` in `tools/lib/render-doc.sh` is the citation resolver the /build Skill can reuse.

## Drawn from the session

> **Fix:** the skeptic judged the finder's fix UNSOUND. This is the skeptic's corrected fix:
— agent, closing review round 1, M1

## Owner confirmation

Asked: In an adopter, the rendered /build Skill still tells the agent to call tools/workflows/tier2-review.js and unattended-build.js … Fold it into the batch unit TOOL-dRenderedAnchor-2 alongside the 8 promoted findings?
Answer: Include in unit 2 (Recommended)
