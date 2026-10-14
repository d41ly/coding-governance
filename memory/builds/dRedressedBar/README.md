---
slug: dRedressedBar
node: d
opened: 2026-10-13
streams: tooling
roster: TOOL
ids: TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11
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
- **Amendment (M2 ADD), 2026-10-14**: unit 8 added before the audit. Both canary attempts hung
  in arm 11g AC14, past the 13200 s ceiling: the arm's FIFO server exited on one failed open while
  its nested bar ran with no wall. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-8-brief.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 9 added before the audit, by the owner's resolution of
  unit 3's F1 as (c). A writing `govkit update` that gains `settings-merge` but leaves `agent-cap`
  out fails on settings-merge's adopter; the owner chose to fix it here rather than record it. Its
  brief is `prompts/2026-10-14-prompt-TOOL-dRedressedBar-9-brief.md`, and unit 3's revision record
  is `prompts/2026-10-14-prompt-TOOL-dRedressedBar-3-2-revision.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 11 added after the round-1 spec audit, by the owner's
  resolution of unit 10's F1 as (c). Unit 10 narrows settings-merge's accepted stop to two probed
  paths, and unit 11 adds a receipt-reading probe term to the declared-outcome contract, so a hook at
  a receipt-recorded home also refuses the false accept. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-11-brief.md`, and unit 10's revision record is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-2-revision.md`.
- `GATE_REGEN_CHECK` reaching the canary's nested runners is a separate finding and not this build's.
- Write sets overlap on `tools/roles/adopt-roles.test.sh`, so order sequences them: units 1, 2, 8
  and 9 are disjoint; 3 follows 9, whose fix its three unscoped arms witness; 4 follows 1; 5 follows
  4; 6 follows 5; 7, the records and kit versions, is measured over the code units 1 to 6, 8 and 9
  leave. Units 10 and 11 follow 7 in that order. Each touches only govkit-exempt files and adds no
  function, so neither moves a kit version or the symbol index unit 7 regenerates.
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
| 8 | `TOOL-dRedressedBar-8` | the canary's memory-pause arm 11g AC14 hangs when its FIFO server dies, bounded and its server kept alive |
| 9 | `TOOL-dRedressedBar-9` | govkit update's gained settings-merge no longer fails an update that left agent-cap out |
| 10 | `TOOL-dRedressedBar-10` | PROMOTED: the round-1 spec audit's 12 mediums and 11 lows, batched — report ids 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 and 23 |
| 11 | `TOOL-dRedressedBar-11` | a receipt-reading probe term in govkit's declared-outcome contract, closing settings-merge's last false-accept route |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 11 unit(s) · node d · opened 2026-10-13 · streams tooling
ids TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dRedressedBar-1 — stale suite fixtures re-armed against the code the bar-less landings moved](spec/2026-10-14-spec-TOOL-dRedressedBar-1.md) | 1 | 1 | SPECCED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-2 — the one verb offender over the lexicon pin, renamed to a declared verb](spec/2026-10-14-spec-TOOL-dRedressedBar-2.md) | 1 | 2 | SPECCED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-8 — arm 11g AC14 bounded, and its FIFO server kept alive through MSYS's failed opens and broken pipes](spec/2026-10-14-spec-TOOL-dRedressedBar-8.md) | 1 | 1 | SPECCED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-9 — settings-merge's adopter exit with no agent-cap hook declared an accepted stop, so a gaining update completes](spec/2026-10-14-spec-TOOL-dRedressedBar-9.md) | 1 | 2 | SPECCED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-3 — the govkit selftest's 56 reds, traced to four root causes and re-armed](spec/2026-10-14-spec-TOOL-dRedressedBar-3.md) | 2 | 1 | SPECCED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-4 — the `workflows` homonyms the install-prefix ban reads as a kit path, held in a named constant](spec/2026-10-14-spec-TOOL-dRedressedBar-4.md) | 2 | 2 | SPECCED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-5 — fork idioms past the spawn-idiom registry, converted to their no-fork forms](spec/2026-10-14-spec-TOOL-dRedressedBar-5.md) | 3 | 2 | SPECCED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-6 — the roles adopter's two exit-1 refusals, armed in its own suite](spec/2026-10-14-spec-TOOL-dRedressedBar-6.md) | 4 | 1 | SPECCED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-7 — records, the regenerated index and the kit versions, measured over the fixed tree](spec/2026-10-14-spec-TOOL-dRedressedBar-7.md) | 5 | 2 | SPECCED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-10 — the round-1 spec audit's 12 mediums and 11 lows, batched: each criterion observed in a form that can pass and fail, each false sentence corrected, and settings-merge's accepted stop narrowed](spec/2026-10-14-spec-TOOL-dRedressedBar-10.md) | 6 | 2 | SPECCED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-11 — a receipt-reading probe term in govkit's declared-outcome contract, closing settings-merge's last false-accept route](spec/2026-10-14-spec-TOOL-dRedressedBar-11.md) | 7 | 2 | SPECCED | rev-1 | 2026-10-14 |
<!-- /gen:build-units -->

Records: 13 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dRedressedBar-10 TOOL-dRedressedBar-11.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dRedressedBar-1`, `TOOL-dRedressedBar-2`, `TOOL-dRedressedBar-8`, `TOOL-dRedressedBar-9` | yes |
| 2 | `TOOL-dRedressedBar-3`, `TOOL-dRedressedBar-4` | yes |
| 3 | `TOOL-dRedressedBar-5` | no |
| 4 | `TOOL-dRedressedBar-6` | no |
| 5 | `TOOL-dRedressedBar-7` | no |
| 6 | `TOOL-dRedressedBar-10` | no |
| 7 | `TOOL-dRedressedBar-11` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
