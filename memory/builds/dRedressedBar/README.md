---
slug: dRedressedBar
node: d
opened: 2026-10-13
streams: tooling
roster: TOOL
ids: TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7
spec-audit: 2026-10-13
---

# dRedressedBar — every traced red of the full bar with self-tests at ebce889c7, fixed at its root

## The problem this build exists to solve

Local main at `ebce889c7` is two landings that met without a bar running the self-tests:
aOrientedCast's addenda and the reconcile of origin/main `2a9d8191`. The owner asked for the full
bar with every self-test, profiled, and every red it finds fixed. The run refused first on a stale
generated output, then, past that refusal, reported 16 of 140 legs red with the run-gates canary
still in its retry. Every red but the canary is traced to a cause, and all but push-main's two arms
are causes of their own.

## Expected improvements

- Each of the 16 legs red at `ebce889c7` reads `GATE ok` in one full bar with self-tests over the
  build tip, with the regen preflight fresh and no knob overriding it.
- Every stale suite fixture is re-armed against the code that moved, never waived.
- Local main can take a push whose forced full bar is green, canary aside.

## Detriments if this is not built

- Every push from local main forces a full bar that cannot pass.
- The next bar-less landing hides its own reds among sixteen inherited ones.
- Five suites grade nothing while reading red, so a real regression in their subjects goes unseen.

## Build-level rules

- **Classification (M2)**: seven units, MISSING at open, one mechanism each, authored by the build
  harness from the brief under `prompts/`.
- The run-gates canary is out of scope until its retry reports; a red there is added as a unit.
- `GATE_REGEN_CHECK` reaching the canary's nested runners is a separate finding and not this build's.
- Write sets overlap on `tools/roles/adopt-roles.test.sh`, so order sequences them: units 1, 2 and 3
  are disjoint; 4 follows 1; 5 follows 4; 6 follows 5; 7, the records and kit versions, is measured
  last over the code the others leave.
- Tiers per the manifest's tier rule: a unit moving a shipped engine's bytes is Tier-2, a stale
  fixture, a registry row, a pin or a regenerated output Tier-1.
- No `tools/unattended/` self-test suite runs: standing owner instruction, 2026-08-23.
- Owner rulings, 2026-10-13: confirm the four unconfirmed reds, then fix every traced red; spec
  audit declared; go.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dRedressedBar-1` | stale suite fixtures re-armed against the code the bar-less landings moved |
| 2 | `TOOL-dRedressedBar-2` | the one verb offender over the lexicon pin, renamed |
| 3 | `TOOL-dRedressedBar-3` | the govkit selftest's reds, each at its root |
| 4 | `TOOL-dRedressedBar-4` | shipped-surface bans: the `workflows` homonyms install-prefix reads as a kit path |
| 5 | `TOOL-dRedressedBar-5` | fork idioms past the spawn-idiom registry, converted |
| 6 | `TOOL-dRedressedBar-6` | the adopt-roles exits the harness-arms leg finds unarmed, armed |
| 7 | `TOOL-dRedressedBar-7` | records, the regenerated index and the kit versions, measured over the fixed tree |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 7 unit(s) · node d · opened 2026-10-13 · streams tooling
ids TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dRedressedBar-1 — stale suite fixtures re-armed against the code the bar-less landings moved](spec/2026-10-14-spec-TOOL-dRedressedBar-1.md) | 1 | 1 | SPECCED | rev-1 | 2026-10-14 |
| [TOOL-dRedressedBar-2 — the one verb offender over the lexicon pin, renamed to a declared verb](spec/2026-10-14-spec-TOOL-dRedressedBar-2.md) | 1 | 2 | SPECCED | rev-1 | 2026-10-14 |
| [TOOL-dRedressedBar-3 — the govkit selftest's 56 reds, traced to four root causes and re-armed](spec/2026-10-14-spec-TOOL-dRedressedBar-3.md) | 1 | 1 | SPECCED | rev-1 | 2026-10-14 |
| [TOOL-dRedressedBar-4 — the `workflows` homonyms the install-prefix ban reads as a kit path, held in a named constant](spec/2026-10-14-spec-TOOL-dRedressedBar-4.md) | 2 | 2 | SPECCED | rev-1 | 2026-10-14 |
| [TOOL-dRedressedBar-5 — fork idioms past the spawn-idiom registry, converted to their no-fork forms](spec/2026-10-14-spec-TOOL-dRedressedBar-5.md) | 3 | 2 | SPECCED | rev-1 | 2026-10-14 |
| [TOOL-dRedressedBar-6 — the roles adopter's two exit-1 refusals, armed in its own suite](spec/2026-10-14-spec-TOOL-dRedressedBar-6.md) | 4 | 1 | SPECCED | rev-1 | 2026-10-14 |
| [TOOL-dRedressedBar-7 — records, the regenerated index and the kit versions, measured over the fixed tree](spec/2026-10-14-spec-TOOL-dRedressedBar-7.md) | 5 | 2 | SPECCED | rev-1 | 2026-10-14 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dRedressedBar-1`, `TOOL-dRedressedBar-2`, `TOOL-dRedressedBar-3` | yes |
| 2 | `TOOL-dRedressedBar-4` | no |
| 3 | `TOOL-dRedressedBar-5` | no |
| 4 | `TOOL-dRedressedBar-6` | no |
| 5 | `TOOL-dRedressedBar-7` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
