# PLAY-dConvergedCharter-11 deviation 111 — the house file's `[effort]` readers are not on the `roles.effort.*` keys at base, so their re-point is a precondition and the arm grades once the seed is gone

**Serves:** deviation PLAY-dConvergedCharter-11

- **Departs from:** `cl-dClosedLoop-0485@dde21704`
- **Hand-off:** design-to-spec
- **Before:** `roles_lib.load_policy`'s house-file fallback retired with the seed, its `[effort]` readers, `check_roles.py`, `handoff.py` and `render_agents.py` among them, already on the `roles.effort.*` keys through dGroundRules's reader since dBoundRoles, and its `[gates]` readers on each role definition's gate grant, never the policy reader, seen red on a planted reader still reading the house file
- **After:** `roles_lib.load_policy`'s house-file fallback retired with the seed, its `[effort]` readers, `check_roles.py`, `handoff.py` and `render_agents.py` among them, put on the `roles.effort.*` keys by TOOL-dBoundRoles-21 S1 and S7 through `read_policy_setting`, a build-run precondition of this unit, and its `[gates]` readers on each role definition's gate grant by TOOL-dBoundRoles-21 S6; the house-file arm `arm_house_readers` grades gov's tree once the seed file is absent, printing `house-file arm: unarmed` before, and is seen red on a planted reader of the house file in a fixture tree with no seed
- **Cause:** design defect
- **Reason:** The clause states the `[effort]` readers are "already on" the policy keys since dBoundRoles. At base they are not: `load_policy` reads only `house/policy.toml` and refuses when it is absent (`tools/roles/roles_lib.py:398-419`), the three readers call it (`check_roles.py:367`, `handoff.py:480`, `render_agents.py:140`), `read_policy_setting` exists nowhere in the tree, and TOOL-dBoundRoles-21, which makes the change, is DEFERRED. The clause's intent is kept whole: no reader of the house file survives the seed. Only its tense moves, from a fact the clause assumes to a precondition this spec names, and the arm grades gov's tree at the moment the clause gives, "with the seed", which PLAY-dConvergedCharter-21 retires. The work this departure leaves owed is the build of PLAY-dConvergedCharter-11 under the ask PLAY-dConvergedCharter-24, which its spec header advances.
- **Evidence:** the clause, `memory/builds/dConvergedCharter/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md:31`; scout C finding 3, `memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md:13`; `tools/roles/roles_lib.py:398-419` at `d8a12f046`; TOOL-dBoundRoles-21's status header; this unit's S8 and §8 F5
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer role of dConvergedCharter's spec run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0485@dde21704
- **Caused-by:** PLAY-dConvergedCharter-11
