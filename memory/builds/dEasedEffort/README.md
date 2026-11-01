---
slug: dEasedEffort
node: d
opened: 2026-11-02
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dEasedEffort-1
status: OPEN
---

# dEasedEffort — the orienter and builder run at high, the closing review's finders and skeptics at medium

## The problem this build exists to solve

The effort policy seeds `gov-orienter` and `gov-builder` at `xhigh`, and `gov-diff-reviewer` and
`gov-skeptic` at `high`. The owner rules those defaults one step lower. The levels live in one file,
`tools/roles/house/policy.toml`, and reach the agent types through a render and the harnesses through
`handoff.py stage-efforts`. The roles README's worked example of a stage override names the skeptic
at two levels, which stops being true once the skeptic is medium everywhere. The prompt is in
`prompts/`.

## Expected improvements

- Orientation and every builder stage run at `high` by default.
- The closing review's finders and skeptics run at `medium` by default.
- The rendered agent types and the harness `efforts` argument agree with the policy.
- The roles README's stage-override example describes a role that still has two levels.

## Detriments if this is not built

- Orientation, builds and closing reviews keep spending at the levels the owner ruled against.
- The roles README keeps a true example that this ruling would otherwise have left unnoticed false.

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-2: `house/policy.toml` and the roles
  README are shipped kit files.
- The render is the main loop's second pass: `--dispatch` refuses a generated output together with
  its generator's input.
- Kit versions move through the lander's `mint`, never by hand.
- The closing review's `synthesis` stage follows `gov-synthesizer`, which stays `high`.
- No spec audit: none is declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dEasedEffort-1` | four role levels move in the effort policy, the roles README's stage-override example follows, and the agent types re-render |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-11-02 · streams tooling
ids TOOL-dEasedEffort-1

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
