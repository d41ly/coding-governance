---
slug: aBoundedCeiling
node: a
opened: 2026-08-27
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6 TOOL-aBoundedCeiling-7 TOOL-aBoundedCeiling-8 TOOL-aBoundedCeiling-9 TOOL-aBoundedCeiling-10 TOOL-aBoundedCeiling-11
---

# aBoundedCeiling — a leg that cannot hang forever, and a landing that pays for the bar once

Node `a` · opened 2026-08-27 · streams tooling · base pinned at preflight.

Started from an owner prompt, recorded verbatim with its measurements at
[the prompt record](prompts/2026-08-27-prompt-TOOL-aBoundedCeiling-1.md). Read that first: every
figure this file leans on is derived there, from `tools/gate-legs.json` and the runner's own
`gate-ledger.tsv`, and none of it is authored twice.

## The goal

**Make the merge bar's cost a VERDICT rather than a complaint, and make a hang a RED rather than a
wedge — in a way that ships to every adopter of the run-gates kit, not just to this repository.**

That sentence is the build's immutable description. Three symptoms, one root: the bar has no bound of
any kind on a single leg, so a leg may take forever and nothing notices, and the only lever anyone has
ever had is to delete legs from the manifest.

## Why the obvious answers are the wrong ones

**Not "make the self-tests faster."** They are 82% of the bar's leg-seconds and the cost is process
creation on an antivirus-fronted machine, which is a property of the node and not of the tree. The
class is already catalogued and it says outright that no portable gate for it can exist. Speeding one
suite is instance work; it does not stop the ninth suite arriving unbounded.

**Not "arm the profile-wide `timeout=`."** One number must cover a one-second leg and a 1320-second
one, so it catches almost nothing and breaks the turnstile suite besides. The arithmetic and the
turnstile evidence are in `TOOL-aBoundedCeiling-1` §4 and are not restated here, because a number
stated in two places is the drift class this build is otherwise about.

**Not "delete more legs."** That is the move that produced this situation, and it is the move an
adopter cannot audit.

## The shape of the answer

A ceiling belongs to a LEG, declared where the leg population already lives, and the runner enforces
it as that leg's deadline. One mechanism then does two jobs that currently have none: it bounds a
hang, and it makes slowness fail rather than merely annoy. The other two units carry that field to
adopters through the deployer, and bound whatever gate command an unattended close actually runs —
which, as the live observation showed, is frequently not gov's runner at all.

## Units

| id | delivers | tier | deps |
|---|---|---|---|
| TOOL-aBoundedCeiling-1 | per-leg wall-clock ceilings in the leg manifest, enforced by the runner | 2 | — |
| TOOL-aBoundedCeiling-5 | the ceiling travels to adopters through the deployer | 2 | 1 |
| TOOL-aBoundedCeiling-6 | the close's gate run cannot outlive a declared bound | 2 | — |

**TOOL-aBoundedCeiling-6 is the one that reaches the failure the prompt names.** It bounds the
`$GATE_CMD` invocation inside `tools/unattended/unattended.sh`, which is where an unattended
`--close` waits, and it binds whatever gate command a project declares. The hang recorded in
`build/2026-08-27-build-TOOL-aBoundedCeiling-1-live-hang-observed.md` runs `scripts/gate.sh` — a
runner gov neither ships nor can reach — so no ceiling inside gov's own runner would have ended it.

**TOOL-aBoundedCeiling-1** is the spine for gov's own bar. A leg declares its ceiling in
`tools/gate-legs.json`; the runner enforces it as that leg's deadline; a breach is a RED naming the
leg and the number it broke. It closes `TOOL-aCollapsedScan-5` and the still-open per-leg-deadline
half of `TOOL-aBoundedVerdict-10`.

**TOOL-aBoundedCeiling-5** carries that field to adopters. `tools/gate-legs.json` is not shipped —
an adopter's manifest is machine-emitted by `govkit apply` — so without this unit the prompt's "and
its adopters" is half delivered.

## BUILD-LEVEL RULES

**Standing constraint, from the prompt record and not re-argued:** no unit may return the unattended
kit's `*.test.sh` legs to `tools/gate-legs.json`. That removal was an owner ruling of 2026-08-23.

### Classification (M2)

All three live units were MISSING at open and are now SPECCED, authored this run and therefore
unreviewed by definition until M4 runs.

### Three planned units were dropped before any spec existed, and one was added

Recorded here rather than as `--rescope` acts: the driver refuses to retire an id its GENERATED units
region never carried, and at BASE that region was empty, so these three were plan entries and never
units. The refusal is correct and the record belongs here instead.

- **`TOOL-aBoundedCeiling-2`, one landing pays for one bar** — DROPPED to a park. The double bar is
  real and measured, but removing it requires relaxing `.githooks/pre-push` predicate 5, which widens
  what can land unverified. That is M3 veto 3 and an owner turn a standing mandate does not delegate.
- **`TOOL-aBoundedCeiling-3`, a forced full run stops bypassing guards** — DROPPED, premise REFUTED.
  `GATE_FULL` and `GATE_SELFTESTS` are orthogonal and `GATE_FULL` never unlocked kit-subject legs.
  The all-or-nothing guard bypass is load-bearing: the `gate-full-green` stamp requires `skips == 0`,
  so guard-scoping a forced run would kill the stamp and pin the push boundary into forcing forever.
- **`TOOL-aBoundedCeiling-4`, one ceiling implementation** — DROPPED. Five of
  `run-unattended-gates.sh`'s eight suites can never be manifest legs under the standing constraint
  above, so a second declaration site exists regardless; and the two enforcements differ on exactly
  the behaviour they would share, since one kills at the bound and the other must not, because a
  killed suite prints no verdict and the kill then reads as silence. Its three `BUDGET_*` lines whose suites
  ARE legs were to have folded into `TOOL-aBoundedCeiling-1`, and the spec audit refuted that too:
  deleting one makes `run_one` resolve an empty budget and reds `--checks` permanently. They stay.
- **`TOOL-aBoundedCeiling-6` was ADDED** on the strength of a live observation, not a plan. See the
  build record named above.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBoundedCeiling-1` | 2 | per-leg wall-clock ceilings in the leg manifest, enforced by the runner |
| 2 | `TOOL-aBoundedCeiling-5` | 2 | the ceiling travels to adopters through the deployer |
| 3 | `TOOL-aBoundedCeiling-6` | 2 | the close's gate run cannot outlive a declared bound |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 3 unit(s) · node a · opened 2026-08-27 · streams tooling
ids TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6 TOOL-aBoundedCeiling-7 TOOL-aBoundedCeiling-8 TOOL-aBoundedCeiling-9 TOOL-aBoundedCeiling-10 TOOL-aBoundedCeiling-11

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBoundedCeiling-1 — a leg declares how long it may take, and the runner holds it to it](spec/2026-08-27-spec-TOOL-aBoundedCeiling-1.md) | 1 | 2 | INPROGRESS | rev-4 | 2026-08-27 |
| [TOOL-aBoundedCeiling-6 — the close's gate run cannot outlive a declared bound](spec/2026-08-27-spec-TOOL-aBoundedCeiling-6.md) | 1 | 2 | INPROGRESS | rev-3 | 2026-08-27 |
| [TOOL-aBoundedCeiling-5 — the ceiling travels, so an adopter's bar is bounded too](spec/2026-08-27-spec-TOOL-aBoundedCeiling-5.md) | 2 | 2 | OPEN | rev-3 | 2026-08-27 |
<!-- /gen:build-units -->

Records: 6 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aBoundedCeiling-1`, `TOOL-aBoundedCeiling-6` | yes |
| 2 | `TOOL-aBoundedCeiling-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
