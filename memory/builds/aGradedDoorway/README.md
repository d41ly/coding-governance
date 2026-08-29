---
slug: aGradedDoorway
node: a
opened: 2026-08-28
streams: tooling
roster: TOOL
ids: TOOL-aGradedDoorway-1 TOOL-aGradedDoorway-2 TOOL-aGradedDoorway-3 TOOL-aGradedDoorway-4 TOOL-aGradedDoorway-5 TOOL-aGradedDoorway-6 TOOL-aGradedDoorway-7
---

# aGradedDoorway — an adopter whose kit does not live at `{prefix}/{kit_id}` can say so again

Node `a` · opened 2026-08-28 · streams tooling. Authored FROM the inCMS adopter, whose own unit is
`ARCH-aBridledVintage-7`.

## What this changes, and why the refusal was too wide

`ce4ef9f3` closed a live injection, and the reproduction in its own message is exact: a target could
put `kit = "pwn.py z"` in `[answers]` and make a READ-ONLY `check` run its script and write a
sentinel. The fix refused `prefix`, `kit_id` and `kit` from both target tables.

That refusal is a SUPERSET of the defect. Twenty lines above it, in the same function, the top-level
`prefix` is ALSO target-supplied, and it is safe for exactly one reason: it is graded by the STRICT
class, which admits no space, quote, semicolon, backtick or pipe, so a value cannot leave its
argument. The two target tables graded EVERY value with the prose class, which admits a space. **The
defect was the class, not the key.**

What the surplus cost: an adopter whose kit does not live at `{prefix}/{kit_id}` lost its only way
to say so. Measured on the inCMS adopter, which homes four kits off that pattern — memory-tree flat
at `scripts/`, memory-recall at `scripts/recall`, review-harness at `scripts/workflows`,
pytest-parallel-guardrails at `scripts/pytest-guardrails`:

| measure | refusal | strict grading |
|---|---|---|
| rows `adopt --re-adopt` would record | 71 | 93 |
| its own receipt paths the run cannot see | 20 | 1 |
| destinations reported `not-installed` | 85 | 61 |

The one path still unseen is the synthesized `.gitattributes` row, which `adopt` never records as a
file. The 61 are files that adopter declines by decision.

## The rule, which is per TABLE and per KEY rather than a name ban

- `[answers]` refuses all three. It is GLOBAL: a `kit` there collapses every entry into one home and
  a `kit_id` renames all of them, so no value is ever legitimate.
- `[kit.<eid>]` accepts `prefix` and `kit`, graded STRICTLY. A per-entry install home is a path
  fragment the operator owns and this engine cannot derive.
- `kit_id` stays refused everywhere. It is the ENTRY's identity, joined to the receipt's `kit`
  field, and not a path.

## Arms

The `(door, key)` sentinel table gains a sixth row for `kit.kit_id`, and three arms hold the other
direction: a strict per-entry `kit` resolves destinations through it, a strict per-entry `prefix`
does the same and `{kit}` follows it, and `kit.<entry>.kit_id` still refuses BY NAME.

**All three needed `--kits` and the first draft did not have it.** `plan` with no selection takes
the REGISTRY default, which carries `playbook`, whose unanswered `playbook_path` refuses before the
per-entry table is ever read — so all three passed by finding nothing, on an error naming a kit the
fixture does not install. Measured, then fixed, then re-measured.

## What is reported rather than fixed here

Four rows, each with its measurement, in `memory/backlog/TOOL.md`. The two fixture-prefix items are
refactors of two 2 700-line suites that cost an hour each to verify, and half-landing them is worse
than reporting them precisely.

## TOOL-aGradedDoorway-2, and what is proven about it

`adopt-unattended.test.sh` and `check-unattended.test.sh` now spell the fixture's kit home through
one `KIT_REL`, defaulting to `tools/unattended`. 145 sites in the second file, and NONE of them sat
inside a single-quoted region — measured with a quote-state walk rather than a `grep` for a
apostrophe, which had put the figure at 93 and made the job look undoable.

**Proven:** `adopt-unattended.test.sh` runs green at `tools/unattended`, `scripts/unattended` and
`vendor/gov/unattended` — 55 assertions each. Both files expand back to their pre-change bytes
EXACTLY when `$KIT_REL` is replaced by its default and the added lines are removed, so this repo's
own behaviour cannot have changed.

**Not proven:** `check-unattended.test.sh` at a foreign prefix. That run costs about an hour and was
skipped by the owner as not viable. The equivalence proof covers the regression risk; it does not
cover the new capability, and this says so rather than implying otherwise.

**Not done:** `check-playbook.test.sh`. Its fixture, `playbook.fixture.md`, hardcodes the prefix in
its own outputs, grain, records and legs and ships `role = "engine"` — verbatim, no placeholder
pass — so the suite cannot follow a variable the fixture does not have. That is
`TOOL-dScrubbedConduit-2`, whose row already names that obstacle.

## The push, and what went unverified in it

Pushed to `origin/main` with `--no-verify`, on the owner's explicit instruction of 2026-08-28. The
full push-boundary bar did not run.

**Known green, from this build rather than from the push:** `govkit selftest` at 986 arms, exit 0,
run after the final needle fix. `drift-audit/selftest.py` green. `adopt-unattended.test.sh` green at
three prefixes — `tools/unattended`, `scripts/unattended`, `vendor/gov/unattended` — 55 assertions
each.

**Unverified:** `check-unattended.test.sh` was not run at all, at either prefix. What stands in for
it is an equivalence proof rather than an execution: expanding `$KIT_REL` back to its default and
removing the added lines reproduces the pre-change file BYTE FOR BYTE, so this repo's own behaviour
cannot have changed. That covers regression and says nothing about the new capability. The
foreign-prefix run for that file remains owed, and `TOOL-aGradedDoorway-2` stays INPROGRESS for
exactly that reason.

## Units

*Seeded from this build's own backlog rows by a later session, because the slot leg requires the
pair and the build landed without one. Status is each row's own token in `memory/backlog/TOOL.md`;
no tier is claimed here, because this session did not author these units and cannot know it.*

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aGradedDoorway-1` | CLOSED | a target may name a per-entry install home again, graded strictly rather than refused |
| 2 | `TOOL-aGradedDoorway-2` | INPROGRESS | the unattended fixture suites spell their kit home once instead of a literal `tools/` |
| 3 | `TOOL-aGradedDoorway-3` | CLOSED | drift_report.py's default-branch probe decodes as UTF-8 like its fourteen siblings |
| 4 | `TOOL-aGradedDoorway-4` | OPEN | check 21's build-README population stops using a `*` pathspec that crosses `/` |
| 5 | `TOOL-aGradedDoorway-5` | OPEN | check 30 stops spawning a `--plan` subprocess per build |
| 6 | `TOOL-aGradedDoorway-6` | OPEN | check-wiring.sh resolves prefix and launcher for a non-`tools` install prefix |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 1 unit(s) · node a · opened 2026-08-28 · streams tooling
ids TOOL-aGradedDoorway-1 TOOL-aGradedDoorway-2 TOOL-aGradedDoorway-3 TOOL-aGradedDoorway-4 TOOL-aGradedDoorway-5 TOOL-aGradedDoorway-6 TOOL-aGradedDoorway-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aGradedDoorway-7 — fold the five expensive legs under a viable wall clock](spec/2026-08-29-spec-TOOL-aGradedDoorway-7.md) | — | 2 | SPECCED | rev-2 | 2026-08-29 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-aGradedDoorway-7.

Ids no `spec-audit` record has ever named: TOOL-aGradedDoorway-7.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
