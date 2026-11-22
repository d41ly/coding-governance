**Serves:** journal TOOL-dBoundRoles-14

# Brief — dBoundRoles: TOOL-dBoundRoles-14 revised over its second builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 14's second builder (run `wf_37ac53bc-1d1`) stopped before its code
on rev-6 and returned one divergence against §4 "The binding join": the index carries no grouping of a unit's selector
rows. Its return is `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-14-2-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md` to rev-7 so §4 "The binding join", S5
and AC2 state a join the code at HEAD can build.

### Items

1. Record the fork as §8 F7 with the return's three options, RESOLVED (agent, 2026-11-22, delegated): (a),
   `check_role_bindings` re-parses each indexed unit manifest's blob through `instruction_units.parse_unit_rows`, which
   `gov_tag.py` already imports, rung 3, reuse of a seam already imported, with `widens: none · relaxes: none`. (b)
   loses for widening Files touched into `instruction_units.py` and moving the red locations `check_namespace_joins`
   prints for every selector; (c) names no key the code carries.
2. Rewrite §4 "The binding join", S5 and AC2 to that resolution: where the unit rows come from, how a unit's `role.` and
   `practice.` selectors are grouped, and what AC2 observes. Keep AC2's number; keep it passable on a correct build at
   HEAD and red on the break it names. Files touched and §10 agree with it.
3. Change nothing else. Keep the status `INPROGRESS`. One revision-log line names this brief by its file stem and the
   return by its file stem.
4. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### Acceptance

The spec is rev-7 with F7 marked resolved as item 1 states; §4, S5 and AC2 agree with it; both checks exit 0.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. No change beyond the binding join and what it forces.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md` alone.

### Reuse

`tools/playbook/instruction_units.py#parse_unit_rows`, imported by `tools/playbook/gov_tag.py` at HEAD.
