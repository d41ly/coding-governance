---
slug: aSweptBar
node: a
opened: 2026-10-13
streams: tooling
roster: TOOL
ids: TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6 TOOL-aSweptBar-7
---

# aSweptBar — the full bar with self-tests goes green over local main

## The problem this build exists to solve

Local main at `53b25884` carries six landings that merged without a bar, by the owner's order. The
owner then asked for a full bar over the repository with the kit self-tests, and for every red it
finds to be fixed at its root. `GATE_FULL=1 GATE_SELFTESTS=1` reported 30 of 138 legs red, and the
unattended runner reported its kit gate red and refused its driver suites as uncalibrated. Most reds
are two landings that never met: the v4.0 charter has no numbered sections, and the roles kit that
landed beside it renders agent types from them.

## Expected improvements

- Every leg of the full bar with self-tests reads green over local main, or reads a recorded reason.
- Gov's agent types render again, so a delegated pass can be spawned as its role.
- Each red that was a stale fixture is re-armed rather than waived.

## Detriments if this is not built

- Every agent type and every handoff render refuses, so no role can be spawned at all.
- The next bar-less landing hides its own reds inside thirty inherited ones.
- A push from local main forces a full bar that cannot pass.

## Build-level rules

- **Classification (M2)**: six units, MISSING at open, one mechanism each, authored by the build
  harness from the brief under `prompts/`.
- The roles kit's reds are out of scope: aOrientedCast re-keys `tools/roles/` onto the v4.0 rule
  tags on its own branch, and this build writes nothing under `tools/roles/`, `.claude/agents/`,
  `.claude/skills/build/` or `tools/playbook/`.
- Write sets overlap, so order sequences them: units 1, 2 and 3 are disjoint; 4 follows 1 and 3;
  5 follows 2 and 4; 6, the records and pins, is measured last over the code the others leave.
- Tiers per the manifest's tier rule: every unit is Tier-1, a stale fixture, a registry row, a pin
  or a shipped literal re-derived.
- Owner rulings, 2026-10-13: go; no spec audit; build through the Workflow harness while hand role
  spawns refuse; run the unattended suites serially.
- A leg that timed out under contention is re-run alone before it counts as red.
- Unit 7 is the closing review's promotion (M4): round 1 read CLEAN WITH FIXES, 0 blockers and 0
  highs, so its 3 mediums and 4 lows batch into one unit; owner, 2026-10-13: merge to local main
  once the build is complete, before the full bar and the unattended suites run.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aSweptBar-1` | stale suite fixtures re-armed against the code the bar-less landings left |
| 2 | `TOOL-aSweptBar-2` | every self-test honours the foreign-prefix probe or is declared a whole run |
| 3 | `TOOL-aSweptBar-3` | the run-gates evidence and pre-push suites' standalone reds |
| 4 | `TOOL-aSweptBar-4` | shipped-surface bans: kit-path literals, the remote ladder, encodings, `{prefix}`, a gov path in a template |
| 5 | `TOOL-aSweptBar-5` | fork idioms re-grown past the spawn-idiom registry, converted |
| 6 | `TOOL-aSweptBar-6` | records, pins and ceilings re-measured over the fixed tree |
| 7 | `TOOL-aSweptBar-7` | the closing review's three mediums and four lows, batched (M4) |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 6 unit(s) · node a · opened 2026-10-13 · streams tooling
ids TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6 TOOL-aSweptBar-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aSweptBar-1 — stale suite fixtures re-armed against the code the bar-less landings left](spec/2026-10-13-spec-TOOL-aSweptBar-1.md) | 1 | 1 | CLOSED | rev-1 | 2026-10-13 |
| [TOOL-aSweptBar-2 — the foreign-prefix probe contract: three engine self-tests declared whole, and format-guard's suite takes the probe stop](spec/2026-10-13-spec-TOOL-aSweptBar-2.md) | 1 | 1 | CLOSED | rev-1 | 2026-10-13 |
| [TOOL-aSweptBar-3 — the run-gates evidence and pre-push suites' standalone reds, each at its root](spec/2026-10-13-spec-TOOL-aSweptBar-3.md) | 1 | 1 | CLOSED | rev-2 | 2026-10-13 |
| [TOOL-aSweptBar-4 — shipped-surface bans: each ban's own remedy, applied to the offenders it names](spec/2026-10-13-spec-TOOL-aSweptBar-4.md) | 2 | 1 | CLOSED | rev-1 | 2026-10-13 |
| [TOOL-aSweptBar-5 — fork idioms re-grown past the spawn-idiom registry, converted](spec/2026-10-13-spec-TOOL-aSweptBar-5.md) | 3 | 1 | CLOSED | rev-1 | 2026-10-13 |
| [TOOL-aSweptBar-6 — records, pins and ceilings re-measured over the fixed tree](spec/2026-10-13-spec-TOOL-aSweptBar-6.md) | 4 | 1 | CLOSED | rev-2 | 2026-10-13 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aSweptBar-1`, `TOOL-aSweptBar-2`, `TOOL-aSweptBar-3` | yes |
| 2 | `TOOL-aSweptBar-4` | no |
| 3 | `TOOL-aSweptBar-5` | no |
| 4 | `TOOL-aSweptBar-6` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
