**Serves:** journal TOOL-dBoundRoles-21

# TOOL-dBoundRoles-21 — the first builder's return, a divergence

Run `wf_db323633-aff`, a parallel pass from `612d66b9c` on rev-5. It wrote no product path and committed nothing;
`diverged: true`. Its pass branch was removed with `pass-tree.sh --remove`.

## The divergence, as returned

(1) BLOCKING. §2 S1, §4 "The order" steps 1-3, §5, AC2 and AC6 assume `read_policy_setting` reads source `default` as
unset. None of the four keys can answer source `default`: each catalogue row carries a derived default
(`tools/policy/catalogue.toml@25076c3d:308-330`), and for an unset key with a derived default
`tools/policy/policy.py#read_default_value` raises `DerivedDefault`, a refusal. Probed in the worktree:
`python tools/policy/policy.py get roles.effort.gov-builder --json` exits 2, "the row roles.effort.<role> carries a
derived default no reader computes yet". So every unset key becomes a RolesError, gov sets none of them, every render
refuses, and AC2's and AC6's unset cases cannot be reached. Candidates it named: (a) read a refusal carrying the
policy kit's `DERIVED_WHY` text as `None`; (b) `get` gains a distinct answer for a derived default, a change to
`tools/policy/policy.py`, another build's mechanism outside the write set; (c) another signal the spec names.

(2) S1's `read_policy_setting(key, root, with_default=False)` has no kit directory, and in `render_agents.py
--selftest` every fixture root is a non-git temp directory where the real `policy.py get` exits 2 ("names no commit in
this repository"). The spec must say where the policy kit search starts and what reader the selftest fixtures see.

(3) S6 and S7 name too few readers of the gate grant: `tools/roles/render_agents.py#run_mode` (its `granted`, which
writes each agent's `## Ceiling` gate legs) and the handoff render's `granted` in `tools/roles/handoff.py` (the
`load_policy(...).get("gates", {})` call before `render_role`) read the house file's `[gates]` alone, and would render
"gate legs: none" once the rows move into the role files. Either S7 lists them, or `load_policy` returns the merged
grant.

(4) S8 regenerates `.governance/policy.json` but neither Files touched nor the write set holds it, and its
`catalogue_blob` goes stale with S8's catalogue edit; `.claude/agents/` and `.claude/roles.json` are in Files touched
but not in the declared write set.

## What held

Every blob pin the spec cites exists; `build`'s `builder` maps to gov-builder and `spec-review`'s `skeptic` to
gov-skeptic; the AC7 greps are clean at base; `unsummarised-keys.txt` holds the four rows; no write-set path is on the
kickoff manifest's watch list.
