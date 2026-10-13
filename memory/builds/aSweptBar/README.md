---
slug: aSweptBar
node: a
opened: 2026-10-13
status: OPEN
streams: tooling
roster: TOOL
ids: TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6
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
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-10-13 · streams tooling
ids TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
