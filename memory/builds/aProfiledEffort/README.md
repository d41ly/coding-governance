---
slug: aProfiledEffort
node: a
opened: 2026-11-10
streams: tooling
roster: TOOL
authorized-by: prompt
status: OPEN
ids: TOOL-aProfiledEffort-1 TOOL-aProfiledEffort-2 TOOL-aProfiledEffort-3
---

# aProfiledEffort — the effort policy takes a profile per model, and Claude Fable runs every role and stage at medium

## The problem this build exists to solve

The effort policy, `tools/roles/house/policy.toml`, holds one set of levels: a default, a level per
role and a level per workflow stage. Every role agent is `model: inherit`, so it runs on whatever
model the session runs, and the same levels apply to every model. The owner wants the levels to
follow the model: what exists stays as the default for any model, Claude Fable of any version runs
every role and every stage at `medium`, and a later model takes its own levels by adding a profile,
with no change to code. The prompt is in `prompts/`.

## Expected improvements

- The policy declares named profiles, each matching a model and carrying its own levels.
- A session on Claude Fable resolves every role and stage to `medium`.
- A model no profile matches resolves exactly as it does today.
- Each dispatch route names how the model reaches the resolver.

## Detriments if this is not built

- A Fable session keeps running builders, spec writers and synthesis at `high`.
- A per-model level stays a hand edit of the one policy, which then misstates every other model.

## Build-level rules

- **Classification (M2)**: three units, each MISSING at open, each Tier-2: the policy file, the
  roles library, the handoff verbs and the Skill template are shipped kit files.
- Order is 1, 2, 3: the verbs read the resolver, and the dispatch carriers name the verbs.
- The agent types' own `effort:` line stays the default profile's, since a file read at session
  start cannot follow the model; a profile reaches an agent at dispatch.
- Kit versions move through the lander's `mint`, never by hand.
- No spec audit: none is declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aProfiledEffort-1` | the policy's profile tables, their validation and the resolver that picks a profile by model, with the `fable` profile seeded |
| 2 | `TOOL-aProfiledEffort-2` | the handoff verbs resolve a role's and a workflow's stage levels for a named model |
| 3 | `TOOL-aProfiledEffort-3` | the dispatch carriers, the build Skill, the unattended verbs and the roles documents, pass the model and the resolved level on every spawn |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-10 · streams tooling
ids TOOL-aProfiledEffort-1 TOOL-aProfiledEffort-2 TOOL-aProfiledEffort-3

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
