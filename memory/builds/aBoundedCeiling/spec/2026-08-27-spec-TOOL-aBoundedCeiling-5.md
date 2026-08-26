# TOOL-aBoundedCeiling-5 — the ceiling travels, so an adopter's bar is bounded too

**Status:** OPEN · rev-2 · 2026-08-27 · node a · Tier-2 · base 1d83cc94 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aBoundedCeiling-1-live-hang-observed.md](../build/2026-08-27-build-TOOL-aBoundedCeiling-1-live-hang-observed.md) | research | TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-6 |
| [2026-08-27-prompt-TOOL-aBoundedCeiling-1.md](../prompts/2026-08-27-prompt-TOOL-aBoundedCeiling-1.md) | research | TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-6 |
| [2026-08-27-review-TOOL-aBoundedCeiling-1-round1.md](../reviews/2026-08-27-review-TOOL-aBoundedCeiling-1-round1.md) | spec-audit | TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-6 |

<!-- /gen:spec-records -->

## 1. Goal

Teach the deployer to carry a leg's ceiling. `TOOL-aBoundedCeiling-1` bounds gov's own bar and can
reach no further, because `tools/gate-legs.json` is not shipped — an adopter's manifest is
machine-emitted by `govkit apply` from the selected kits' `[[gate_leg]]` rows, and that emitter
writes no ceiling. Without this unit the owner's "apply to this repo and its adopters" is half
delivered, and every adopting tree keeps a bar in which one hung leg wedges the whole run.

## 2. Scope (IN)

- **S1** — a `ceiling` key on `[[gate_leg]]` rows in the kit descriptors that declare legs, carrying
  the same integer seconds `TOOL-aBoundedCeiling-1` puts in gov's manifest.
- **S2** — `govkit`'s leg emitter writes `ceiling` into a target's `gate-legs.json`.
- **S3** — a target-version FLOOR gating that write, resolved from the target's installed runner,
  built as the exact sibling of `check_target_reads_subject` and its `SUBJECT_FLOOR_RUN_GATES`.
- **S4** — a `KIT_RUN_GATES_VERSION` bump, because the floor cannot discriminate against a version
  that did not move.
- **S5** — `govkit.py`'s **selfcheck check 7h** compares `ceiling` between a kit descriptor and
  `tools/gate-legs.json`, beside the `subject` arms it already carries. Named exactly, because the
  first draft said "selfcheck" in one section and `tools/govkit/selftest.py` in two others, and those
  are different programs on different legs — `govkit selfcheck` is `subject: repo` with no guard and
  runs on every bar, while `govkit selftest` is held unless `GATE_SELFTESTS=1`.
- **S6** — repair the `KeyError` the emitter raises on its own below-floor path. `row["subject"]` is
  SET conditionally and READ unconditionally at the `emitted.append(...)` call, so `govkit apply`
  crashes against any target below the subject floor today. Both reads become `.get(...)`. This is
  not scope creep: copying the seam verbatim for `ceiling` reproduces the crash for every target that
  has not yet reached the ceiling floor, which is every current adopter.
- **S7** — a project-owned lever so an adopter on a slower node is not stuck with node `a`'s numbers.
  The emitter never overwrites a leg's ceiling that the target itself declared, and reports when it
  withheld one for that reason.

## 3. Non-goals (OUT)

- **N1** — no ceiling VALUE is chosen for an adopter's own project-authored legs. A kit ships a
  ceiling for the legs the kit owns; a project's own legs are the project's to bound.
- **N2** — no BEHAVIOUR in `run-gates.sh` changes. Its reader, its enforcement and its declaration
  check are `TOOL-aBoundedCeiling-1` and are complete without this unit. The file is still EDITED
  here, by exactly one line: `KIT_RUN_GATES_VERSION` and its inline `gov:kit` marker, which is where
  that constant actually lives. rev-1 routed the bump to `kit.toml`, which holds only a `version_from`
  pointer at it, so the floor this unit needs could never have moved.
- **N3** — no adopter is migrated. The field arrives on their next `govkit apply`, which is how
  every other kit field has arrived.
- **N4** — `.githooks/pre-push`'s hardcoded `tools/gate-legs.json` path is NOT fixed here. It is a
  real defect at a configurable install prefix and it gets a backlog row, not this unit's diff.

## 4. Design

### Why a version floor and not a date cutoff

The date-cutoff idiom this repo uses elsewhere — `UNITS_REGION_CUTOFF`, `LANDED_ANCHOR_CUTOFF` —
answers "is this RECORD old enough to be excused". The question here is different: "can the
software at the other end READ what I am about to write". A date cannot answer that, because an
adopter who has not run `govkit apply` in six months has an old runner and a current calendar.

The precedent is in-tree and exact. `govkit.py` gates its `subject` write on
`check_target_reads_subject(target, deploy)`, and its own comment states the failure it exists to
prevent:

> `tools/gate-legs.json` has a PINNED key set, asserted by the `run-gates canary` leg that the
> run-gates kit ships and that runs on every adopter's bar — and that pin did not carry `subject`
> before this build. Writing the key into a tree whose run-gates predates it reds their canary as a
> side effect of a routine `apply --kits memory-tree`, which is the deployer breaking a target's
> gate while installing something else.

`ceiling` repeats that situation exactly, so it takes the same shape rather than a new one.

### The asymmetry worth knowing before writing the floor

Gov's own `run-gates canary` leg is held on a default bar, because gov's hand-maintained manifest
gives it `chunk: selftests`. An adopter's emitted manifest carries no `chunk` at all — the emitter
never writes one — so in an adopting tree that same leg is `subject: repo` and runs on EVERY bar.
The canary breaking in an adopter is therefore louder and sooner than it would be here, which is the
argument for the floor being conservative rather than clever.

### Inventory

| site | change |
|---|---|
| kit descriptors declaring `[[gate_leg]]` | a `ceiling` per leg row |
| `govkit.py` leg emitter (~:4305) | write `ceiling` when the floor permits |
| `govkit.py` | `CEILING_FLOOR_RUN_GATES` and its `check_target_reads_ceiling` sibling |
| `tools/run-gates/run-gates.sh:19` | the `KIT_RUN_GATES_VERSION` literal AND its same-line `gov:kit` marker |
| `tools/run-gates/README.md:3` | the matching `gov:kit run-gates@` marker, or `kit version markers` reds |
| `tools/govkit/govkit.py` check 7h | descriptor-to-manifest parity for `ceiling`, beside the subject arms |
| `tools/govkit/selftest.py` | where the failing case for that parity arm is STAGED |

### Alternatives rejected

**Ship `tools/gate-legs.json` itself.** It is exempt from the deploy registry deliberately: a
target's leg set is the set of kits that target selected, which gov cannot know. Shipping gov's
manifest would give every adopter gov's legs.

**Let adopters hand-write ceilings.** They can, and nothing stops them — but a kit-owned leg whose
ceiling is authored downstream drifts from the suite it bounds on the first kit update, and the
descriptor is where every other kit-owned property of that leg already lives.

## 5. Production-readiness checklist

- **security** — no new trust. The value moves from a tracked kit descriptor into a generated
  manifest through the emitter that already writes that file.
- **perf/scale** — one integer per leg in a file written once per `apply`.
- **observability** — the floor's decision is reported the way `check_target_reads_subject`'s is, so
  an operator can see that a ceiling was withheld and why.
- **risks** — the real hazard is writing the field into a tree that cannot read it, which reds that
  target's canary during an unrelated install. That is precisely what S3 exists to prevent and what
  AC3 observes.
- **testing + left-shift gates** — AC1 through AC4, in `tools/govkit/selftest.py` against a target
  fixture pinned below the floor and one at or above it.
- **migration / rollback** — dropping the `ceiling` write restores today's emitter exactly. A target
  already carrying ceilings keeps them; they are inert to a runner that does not read the key.
- **user docs** — the kit descriptor's `[[gate_leg]]` documentation gains the field and the floor.

## 6. Acceptance criteria

- **AC1** — When `govkit apply` runs against a target whose installed run-gates is AT or ABOVE the
  floor, the emitted `gate-legs.json` carries `ceiling` on every kit-owned leg that declares one.
- **AC2** — When the same apply runs against a target BELOW the floor, the emitted manifest carries
  no `ceiling` key at all, and that target's `run-gates canary` stays green — observed against a
  fixture, not asserted.
- **AC3** — When a kit descriptor declares a `ceiling` that `tools/gate-legs.json` does not carry,
  `govkit selfcheck` FAILS naming that leg — the leg that runs on every bar, not the held one.
- **AC5** — When `govkit apply` runs against a target BELOW the subject floor, it completes without
  raising, observed against a fixture pinned below it. That call raises `KeyError` today, so this
  criterion FAILS before the change and passes after, which is what makes it a test.
- **AC6** — When a target's `tools/gate-legs.json` already declares a `ceiling` a kit did not write,
  a subsequent `govkit apply` leaves that value intact and reports that it withheld its own.
- **AC4** — When `bash tools/run-gates/run-gates.sh` runs under `GATE_SELFTESTS=1` after this unit,
  the `govkit selftest` and `govkit acceptance matrix` legs are green.

## 7. Gates

`bash tools/run-gates/run-gates.sh` under `GATE_SELFTESTS=1`, for `govkit selftest`,
`govkit acceptance matrix` and `run-gates adopter e2e`. Plus two legs that run on EVERY bar and that
this unit's edits reach directly: `govkit selfcheck`, which is where S5's arm lands, and
`kit version markers`, which reds on a partial version bump. No new leg is added.

## 8. Open questions

- **F1 — whether the floor is a new constant or a reuse of `SUBJECT_FLOOR_RUN_GATES`.** RESOLVED
  (agent, 2026-08-27, delegated): a new constant. The two fields entered the pinned key set at
  different versions, so one constant answering both questions would let a target below the ceiling
  floor and above the subject floor receive a key it cannot read.
- **F2 — whether a kit-owned leg with no descriptor `ceiling` should red.** RESOLVED (agent,
  2026-08-27, delegated): YES, in `govkit selfcheck` check 7h, mirroring its existing `d_sub is None`
  arm. rev-1 resolved this the other way on a FALSE premise — that gov's hand-maintained manifest and
  the descriptors "do not join" — when check 7h is precisely the join, in both directions, over that
  exact file. The audit caught it; the premise, not the preference, is what changed.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft, grounded on the deploy-surface probe and verified directly
  against `govkit.py`'s leg emitter and `tools/run-gates/kit.toml`.
- rev-2 · 2026-08-27 · folded the round-1 spec audit. Named `govkit.py` check 7h as the parity site,
  where three sections had named two different programs. Re-resolved F2, whose premise was false.
  Routed the version bump to `run-gates.sh:19` and its README marker, where the constant lives.
  Added S6 for a `KeyError` the audit found live in the emitter's below-floor path, and S7 for the
  slow-node adopter, who had no lever. Cited `TOOL-aPacedTurnstile-12`.

## 10. Reuse audit

**The seam is `check_target_reads_subject` and this unit is its second instance.** Verified in
source at `govkit.py` around the leg emitter: `row = {"name": nm, "argv": argv}` followed by
`if check_target_reads_subject(target, deploy): row["subject"] = ...`. The whole shape this unit
needs — resolve the target's installed runner version, compare against a floor, withhold the key
below it, and say so — already exists and is argued in its own comment. Building a second mechanism
beside it would be the `two-answers-to-one-question` class that
`python tools/memory-tree/gotchas.py --for-paths` selects for these very files.

`python tools/codebase-map/reuse_lookup.py "a wall-clock ceiling per gate leg, enforced by the
runner, that turns a hang into a red verdict"` returned `exempt_leg` and `silenced_legs`
[`tools/govkit/govkit.py`] and the `registry.toml` [govkit] affordance seam, which is the deploy
surface this unit extends.

Recall terms used: `leg ceiling timeout deadline hang wedge selftest guard bar budget verdict spawn
profile runner`. It returned no record about carrying a leg FIELD to adopters, which is itself the
answer to record — the `subject` precedent lives in source and in `TOOL-dUnstalledConvoy-26`'s
neighbourhood rather than in a record this phrasing reaches.

**An OPEN row this unit sits directly on top of, missed by rev-1 and found by the audit.**
`TOOL-aPacedTurnstile-12` asks for the general join this unit is about to bypass: govkit's selfcheck
joins descriptor `[[gate_leg]]` rows to `tools/gate-legs.json` by NAME only and never compares the
declared GUARDS. This unit adds `ceiling` as the THIRD hand-written field branch rather than taking
the general join, because the general join is a larger unit with its own acceptance and because
`guard` has a comparison problem `ceiling` does not — a guard is a list whose members are rewritten
per target by the emitter, so equality is not the right predicate for it. That is a reason, not a
dismissal, and the row stays open.

**The seam is copied MINUS a defect.** §4 says the `check_target_reads_subject` shape "already
exists". Two thirds of that is true. The withhold path RAISES rather than reporting, and nothing is
printed when a key is withheld, so §5's observability sentence describes a report that does not exist
yet. S6 repairs the first and this unit writes the second.

**Where a hit was STALE.** Nothing this unit relies on came from a record. Every claim about the
emitter, the floor and the descriptor was read from source at writing time, because the one probe
answer that named line numbers here is a subagent's and the charter's rule is that a hit can be
stale and must be verified before it is built on.
