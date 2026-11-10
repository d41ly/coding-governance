# Brief — aProfiledEffort: an effort profile per model, Claude Fable at medium

**Serves:** research TOOL-aProfiledEffort-1 TOOL-aProfiledEffort-2 TOOL-aProfiledEffort-3

## The prompt

> Build a profile system for agent effort levels per LLM model in use. What currently exists is the default for any model, and the first new profile should be for Fable (Claude Fable) of any version - if Fable is used, any role's or workflow stage's effort level should be set to MEDIUM. The system should account for adding more per-model profiles with custom role/stage effort levels in the future.

## The brief

### Goal
The effort policy resolves a role's and a workflow stage's reasoning effort for the model in use: today's levels are the default for any model, a seeded `fable` profile gives every role and stage `medium` on any Claude Fable version, and a further model takes custom role and stage levels by adding one profile table to the policy file.

### Items
1. The policy file declares named per-model profiles beside today's `[effort]` tables, which stay the default for any model no profile matches. [planned TOOL-aProfiledEffort-1]
2. A profile matches a model family at any version, and carries its own default, role and stage levels, so a later profile sets custom levels with no code change. [planned TOOL-aProfiledEffort-1]
3. The seeded `fable` profile matches Claude Fable of any version and resolves every role and every workflow stage to `medium`. [planned TOOL-aProfiledEffort-1]
4. The policy's one validator refuses a malformed profile, and two profiles that match one model, the way it refuses a malformed level today. [planned TOOL-aProfiledEffort-1]
5. `handoff.py` answers a role's level and a workflow's stage levels for a named model, and unchanged for no model. [planned TOOL-aProfiledEffort-2]
6. Every dispatch route, the build Skill's harness calls, the unattended verbs' harness calls and a direct role spawn, passes the model in use and spawns at the level the resolver returns. [planned TOOL-aProfiledEffort-3]
7. The roles README and the `help/` page say how to add a profile and how a profile reaches an agent. [planned TOOL-aProfiledEffort-3]

### Acceptance
1. With no model named, `handoff.py stage-efforts` prints for `spec-write`, `spec-review`, `build` and `closing-review` the four lines it prints at the build's base commit, byte for byte.
2. With a Claude Fable model id of two different versions named, each of those four prints `medium` for every stage key, and every role with `agent: true` resolves to `medium`.
3. With a model id no profile matches, the output equals the no-model output.
4. A fixture policy adding a second profile with one custom role level and one custom stage level resolves those two for its model and leaves the default and `fable` outputs unmoved, with no code edit.
5. `check_roles.py` reds, naming the dotted key under R12, on a profile with an unknown key, a level outside the level set, a role or stage that does not exist, an empty match, and two profiles matching one model.
6. `render_agents.py --check` exits 0 and the agent types' `effort:` lines equal the default profile's.
7. The rendered build Skill, the unattended verbs and the roles documents each name the model argument on every `stage-efforts` call they spell, and state the direct-spawn rule.

### Gates
roles catalogue · roles render wiring · roles render selftest · roles adopter self-test · check-wiring self-test · unattended skill wiring · kit/dogfood doc parity · docs · policy check · lexicon naming predicates · kit epoch · kit version markers · memory hygiene · spec tokens; then the full bar at the close.

### Non-goals
Any level of the default profile. The main session's own effort, which is the owner's setting. A hook that refuses a spawn at a level its profile does not give: the `agent` line already prints effort and model, and the gate is filed as an ask, not built. Re-rendering agent types per model, since a session reads its agent registry once at start. The `roles.effort.*` keys of `tools/policy/catalogue.toml` and their move, which TOOL-dBoundRoles-21 owns. An adopter's seeded policy, which `govkit update` never rewrites. A profile for any model but Fable.

### Limitations
The agent types are `model: inherit`, and nothing in a rendered file knows the model, so a profile reaches an agent only where the dispatcher passes a level: a harness `efforts` argument or a direct spawn's effort argument. TOOL-dBoundRoles-21 and PLAY-dConvergedCharter-21, both DEFERRED, later re-point the policy's readers and retire the house file; this build extends the seam as it stands and their specs inherit the profile tables. Kit versions move through the lander's `mint`. No pass runs a suite or the bar.

### Reuse
`tools/roles/house/policy.toml` is the one source, read through `roles_lib.load_policy`, whose R12 validation the profiles extend, and resolved by `resolve_effort` and `resolve_stage_efforts`, which gain the model. `handoff.py stage-efforts` carries the levels to the harnesses, whose `efforts` argument already wins over an agent type's level. `tools/roles/SKILL.template.md` and `tools/unattended/VERBS.template.md` spell the calls. The reuse probe returned `load_policy` and `resolve_stage_efforts` as the seams; recall returned TOOL-aOrientedCast-10 (the policy's design), TOOL-dEasedEffort-1 (the last level change) and TOOL-dBoundRoles-21. No record ties a level to a model.

## Drawn from the session

none

## Owner confirmation

not asked — the brief draws on nothing outside the prompt
