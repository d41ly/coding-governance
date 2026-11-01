# Brief — dEasedEffort: the orienter and builder at high, the closing review's finders and skeptics at medium

**Serves:** research TOOL-dEasedEffort-1

## The prompt

> Change gov-orienter gov-builder builder (spec-write) and builder (build) to 'high' from 'xhigh' by default. Change gov-diff-reviewer gov-skeptic diffFinder (closing-review) and skeptic (closing-review) to 'medium' by default.

## The brief

### Goal
The seeded effort policy holds `gov-orienter` and `gov-builder` at `high`, and `gov-diff-reviewer` and `gov-skeptic` at `medium`, so every route that reads it, the rendered agent types and the harness `efforts` argument alike, carries those levels.

### Items
1. `gov-orienter` and `gov-builder` move from `xhigh` to `high` in `[effort.roles]`, which carries the `builder` stage of `spec-write` and of `build` with them. [planned TOOL-dEasedEffort-1]
2. `gov-diff-reviewer` and `gov-skeptic` move from `high` to `medium` in `[effort.roles]`, which carries the `diffFinder` and `skeptic` stages of `closing-review` with them. [planned TOOL-dEasedEffort-1]
3. `tools/roles/README.md`'s sentence that `gov-skeptic` runs at two levels names a role that still has two levels. [planned TOOL-dEasedEffort-1]
4. The agent types re-render from the policy. [planned TOOL-dEasedEffort-1]

### Acceptance
1. `resolve_effort` over the policy gives `gov-orienter` high, `gov-builder` high, `gov-diff-reviewer` medium and `gov-skeptic` medium, and every other role its current level.
2. `handoff.py stage-efforts` prints spec-write `{"builder":"high","disposal":"high","skeptic":"medium","specFinder":"medium","specWriter":"high","synthesis":"medium"}`, spec-review `{"skeptic":"medium","specFinder":"medium","synthesis":"medium"}`, build `{"builder":"high"}` and closing-review `{"diffFinder":"medium","skeptic":"medium","synthesis":"high"}`.
3. `.claude/agents/` carries the four new `effort:` lines and `render_agents.py --check` exits 0.
4. No document under `help/` or `tools/roles/README.md` states a level this build moved.

### Gates
roles catalogue · roles render wiring · roles render selftest · check-wiring self-test · lexicon naming predicates · kit epoch · kit version markers · memory hygiene · spec tokens; then the full bar at the close.

### Non-goals
Any other role's level or the `default`; `gov-synthesizer` and the closing review's `synthesis` stage; the `[effort.stages.*]` tables, whose `skeptic` rows stay though they now equal the role; the `roles.effort.*` keys in `tools/policy/catalogue.toml`; an adopter's seeded policy, which `govkit update` never rewrites; a CLOSED spec's level table; the fixtures that spell a level their own test writes.

### Limitations
Kit versions move through the lander's `mint`, not by hand. The render is the main loop's second pass. A session started before the render keeps its old agent types until it restarts.

### Reuse
`tools/roles/house/policy.toml` is the one source, read through `roles_lib.load_policy`, `resolve_effort` and `resolve_stage_efforts`; `render_agents.py --write` carries it to the agent types and `handoff.py stage-efforts` to the harnesses. TOOL-aOrientedCast-26 made the same kind of move and its spec is the precedent. Recall returned TOOL-aOrientedCast-10 (the policy file's design) and TOOL-aOrientedCast-26.

## Drawn from the session

none

## Owner confirmation

not asked — the brief draws on nothing outside the prompt
