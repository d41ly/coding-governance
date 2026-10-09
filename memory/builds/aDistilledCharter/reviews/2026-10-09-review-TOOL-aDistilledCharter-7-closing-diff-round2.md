**Serves:** diff-review TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 DEPL-aDistilledCharter-2

# Tier-2 closing diff review — aDistilledCharter, ROUND 2

One read-only lens over the round-1 fold only, primed with round 1's record and its blocker, run as
a direct agent on 2026-10-09. The main loop re-read each finding's cited code as the skeptic.

**Reviewed range:** `1f6e9209c...18e3874fe` (the fold of round 1). **ROUND: 2.**

## Verdict: BLOCKED

Round 1's blocker is FIXED: the lens rendered an adopter's real v3.5 template under the fold's
engine with `--check` and got a clean region, and a fresh v4.0 intake asks for none of the legacy
names. One new BLOCKER, introduced by the fold: `review-harness` requires `agent-cap`, which
requires `settings-merge`, and neither is in the default selection, so every default adoption is
refused and `govkit selftest`'s default-selection arm reds. Five MEDIUM and LOW findings are
batched.

## Review shape

- Raw 6, confirmed 6, refuted 0. Fewer than round 1's 26, so the loop re-arms once more over
  this round's fold.

## Findings and their disposition

| # | Sev | Where | Finding | Disposition |
|---|---|---|---|---|
| B1 | BLOCKER | `tools/govkit/registry.toml` | the default selection gained a kit whose requirements it lacks, so default adoptions refuse | fixed: `DEPL-aDistilledCharter-2` retired, its change reverted; `PLAY-aDistilledCharter-5` carries the checklist to every adoption through the memory-tree kit |
| N2 | MEDIUM | `tools/playbook/render_playbook.py` | `project_name` is a product name and not a checkout directory, so an adopter whose clone is named apart renders the wrong path on every row | batched: `TOOL-aDistilledCharter-8` |
| N3 | LOW | `render_playbook.py` `check_user_clash` | one user can no longer hold two machines | batched: documented as the cost of readers matching the user alone |
| N4 | LOW | the template, `AGENTS.md`, the claim message | gov's own charter is not reached by `govkit update`, so a claim must re-render it in the same commit | batched |
| N5 | LOW | `WIRE-INTO-PROJECT.md` | the legacy and retired notes print in write mode only, never under `--check` | batched |
| N6 | LOW | `render_playbook.py`, `playbook.kit.toml` | `TEMPLATE_MAJOR` is a typed copy nothing compares, and the `legacy` key is read by nothing | batched |
