# TOOL-dGroundRules-66 deviation 71 — the build run adopted a blocker discovery as a unit

**Serves:** deviation TOOL-dGroundRules-66

- **Departs from:** dGroundRules [roster]
- **Hand-off:** design-to-spec
- **Before:** dGroundRules's roster carries the eleven units its README opened with, one per clause of its v2 row.
- **After:** the roster also carries `TOOL-dGroundRules-66`, `--dispatch`'s sibling set leaves out a terminal unit's keys, through the one open-pass reader `--audit` shares.
- **Cause:** builder discovery
- **Reason:** check 49 refused `TOOL-dGroundRules-7`'s dispatch twice on two keys of the CLOSED unit `TOOL-dGroundRules-19` that `pass_commit` can never close, and it refuses every later unit declaring `tools/policy/policy.py`, `tools/policy/guard.py`, `help/policy.md` or `.governance/policy.json`; the build run adopted the repair as a unit by its rescope add row and builds it before unit 7 (README rule 1). The unit narrows check 49's refusal set, a change its spec's §5 states.
- **Evidence:** the rescope add row for `TOOL-dGroundRules-66` at 2026-10-24T01:12:29Z in `memory/builds/dGroundRules/RUN.md`; the spec brief, `memory/builds/dGroundRules/prompts/2026-10-24-prompt-TOOL-dGroundRules-66-spec-brief.md`; the unit's spec, `memory/builds/dGroundRules/spec/2026-10-24-spec-TOOL-dGroundRules-66.md`, whose §4 Evidence records the two open keys measured at `31aa43f9b`.
- **Risk:** additive
- **Approver:** spec writer, the gov-spec-writer role of the build run's rescope, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dGroundRules-66
- **Caused-by:** TOOL-dGroundRules-19
