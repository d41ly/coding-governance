# TOOL-dBoundRoles-16 deviation 162 — the orientation scout kept at high, the owner's later level, not the clause's medium

**Serves:** deviation TOOL-dBoundRoles-16

- **Departs from:** `cl-dClosedLoop-0181@6ebedcff`
- **Hand-off:** design-to-spec
- **Before:** the clause's "the orientation scout at medium and the builder at high (RS-2)", which TOOL-dBoundRoles-16 rev-5's S7 and AC5 carried as the house seed's `gov-orienter` row moved from `high` to `medium`.
- **After:** the builder at high (RS-2) and the orientation scout at high, the level the owner's ruling TOOL-dEasedEffort-1 seeded; S7 moves no seed level and AC5 reads `effort: high` on `.claude/agents/gov-orienter.md`.
- **Cause:** owner ruling
- **Reason:** on 2026-11-02 the owner's prompt for TOOL-dEasedEffort-1 set `gov-orienter` to `high` by name, after the clause was written, and that unit closed with the seed at `high`. Moving the row to `medium` would reverse a later owner ruling on the one role it names, so the ruling outranks the clause it postdates (TOOL-dBoundRoles-16 §8 F5, rung 1). The bound relaxed is the clause's orienter value alone; the builder's level, which the clause and the ruling both set at high, stands.
- **Evidence:** the clause, `memory/builds/dBoundRoles/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md:36`; the ruling, `memory/builds/dEasedEffort/prompts/2026-11-02-prompt-TOOL-dEasedEffort-1-brief.md:7` and `:15`, its spec CLOSED at rev-1; the seed, `tools/roles/house/policy.toml@339f54fa:11`; the render, `.claude/agents/gov-orienter.md@2eb9ec15:7`, `effort: high`; `python handoff.py role-efforts` in `tools/roles/` prints `"gov-orienter":"high"` at `a3efb1d50`.
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer stage of dBoundRoles' build run under `2026-11-22-prompt-TOOL-dBoundRoles-1-spec-fix-1-brief`, citing the owner's ruling TOOL-dEasedEffort-1, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0181@6ebedcff
- **Caused-by:** TOOL-dEasedEffort-1
- **Bound:** the clause's "the orientation scout at medium" (RS-2), for `gov-orienter`
- **Tier:** strongest, a bound the carried clause states in its text, relaxed for a later owner ruling the spec cites
