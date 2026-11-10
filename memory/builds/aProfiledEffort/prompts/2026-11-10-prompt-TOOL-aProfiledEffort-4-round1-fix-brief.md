# Brief — aProfiledEffort: the closing review's four mediums and three lows, batched

**Serves:** research TOOL-aProfiledEffort-4

## The brief

### Goal
Each of the seven items the closing diff review confirmed at round 1 is closed by the fix its report carries, and the self-test arm unit 1 added fails by its own FAIL lines under every staged break. The review record is `memory/builds/aProfiledEffort/reviews/2026-11-10-review-TOOL-aProfiledEffort-1-closing-diff-round1.md`, items 1 to 7; each item's fix is the one under that item, the skeptic's where the report says the finder's was rejected.

### Items
1. Item 1 (id 4): the `agents` verb stops printing the agent type's default-table level as the level an agent ran at under a matched profile.
2. Item 2 (id 6): an arm fails when a matched profile stops being read alone for stage overrides.
3. Item 3 (id 7): an arm fails when the model id is no longer lower-cased before matching.
4. Item 4 (id 12): the three shipped texts stop saying every stage runs at the profile's level where the `committer` and `probe` stages take none.
5. Item 5 (id 5): the seeded policy file's header and its profile comment agree on how a changed value reaches an agent.
6. Item 6 (id 8): a fixture exercises a `match` list of more than one word.
7. Item 7 (id 11): the verb-level whitespace refusal and the exit-1 defect path each have a failing check.
8. `resolve_profile` answers `None` for no model before it reads any profile's `match`, so arm 19 of the render self-test fails by FAIL lines, not a traceback, when the profile checks are staged out of `load_policy`. Unit 1's builder returned this.

### Acceptance
1. Each item's observation is the one its report entry names as the red case, turned into a criterion that is red before the fix and green after.
2. `handoff.py stage-efforts` and `role-efforts` print, with no model and with `claude-fable-5-2`, the lines they print at `c1d1e19f4`.
3. With the profile checks staged out of `load_policy`, the render self-test exits non-zero printing FAIL lines for arm 19 and no traceback.

### Gates
roles catalogue · roles render wiring · roles render selftest · roles adopter self-test · docs · kit/dogfood doc parity · unattended kit gate · lexicon naming predicates · codebase-map coverage + freshness · kit epoch · kit version markers · memory hygiene · spec tokens; then the full bar at the close.

### Non-goals
A re-review: the closing review's subject is terminal. The three CLOSED specs, which stay as written. A level for the `committer` or `probe` stage, which is a new mechanism and is filed as an ask if the spec finds it wanted. Any level of the default tables. The six refuted findings.

### Limitations
No gate, suite or bar runs in the pass. New arms are observed RED then GREEN by the main loop at the close. Kit versions move through the lander's mint.

### Reuse
The fixes extend what units 1 to 3 built: `resolve_profile` and `load_policy` in `tools/roles/roles_lib.py`, arm 19 of `tools/roles/render_agents.py`'s self-test, arm 19 of `tools/roles/adopt-roles.test.sh`, the `agents` verb of `tools/roles/handoff.py`, `tools/roles/house/policy.toml`, and the texts unit 3 moved.
