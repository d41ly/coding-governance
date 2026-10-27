# TOOL-dRankedPlan-36 — a build's first transition is checked against the scenario it pins, and never meets the no-record exit

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 8 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-36-deviation-361.md](../build/2026-10-27-build-TOOL-dRankedPlan-36-deviation-361.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 19 to 29
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`) confirmed
**finding 29 at HIGH**, item **H6**. Finding 5 is the same defect at MEDIUM, item M5, and
`TOOL-dRankedPlan-37` closes it. `TOOL-dRankedPlan-20` S2 makes `check_plan_scenario` exit 2 for a build
with no transition record. `TOOL-dRankedPlan-14` S3 has `derive_step_scenarios` run that check first at
every transition into a step, where "a refusal stops the move". TOOL-dPlacedRequest-21 S7 writes every
build's first record through `write_transition`. Unit 14 S2 lists exit 2 apart from exit 1, so a
builder can read it either way, and a builder who reads it as a refusal leaves no build able to start.
None of unit 20's three plants starts before a first record. The two faces of the finding fix it two
ways, by skipping the check or by pinning on the move, and the report asks for one spelling. This unit
takes finding 5's: on a build's first record, the pin is the move's own `scenario` field, and the check
runs against it. It repairs `TOOL-dRankedPlan-20`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The pin given. `check_plan_scenario(repo, slug, pin=None)` (`tools/loop/scenario.py`,
  `TOOL-dRankedPlan-14` S2, pinned by `TOOL-dRankedPlan-20` S2) takes an optional pin. When the build
  has no transition record and `pin` is given, the pin is `pin`, and every check of unit 14 S2 runs
  against it as against a recorded pin. Exit 2, `no transition record pins a scenario for <slug>`,
  stays only for a build with no transition record and no pin given. That is `scenario.py plan --build
  <slug> --check` asked of a build that has not moved. Observed by AC2 and AC3.
- **S2** — The first move. When `derive_step_scenarios` (TOOL-dDeclaredLoop-27, running unit 14 S3's
  check first) meets a transition into a step and `read_transitions` answers no earlier record for the
  build, it passes the move's own `scenario` field as `pin=`. That field is the one the claim writes on
  the build's first record (TOOL-dPlacedRequest-21 S7). So the first move is checked against the
  scenario it pins and never meets exit 2. This supersedes row 3 of unit 20 §4 "The reading after this
  unit" for a move being written: the row reads "any · none · the move's own `scenario` · checked
  against it". Observed by AC1 and AC2.
- **S3** — The plants. Two plants join `scenario.py --fixture` (`TOOL-dRankedPlan-14` S4).
  `plan-patch-first` carries `TOOL-dRankedPlan-20`'s `plan-patch` record with no transition record and
  writes the claim's first move into `designing`, carrying `scenario=scenario.patch`, through
  `loop_transition.py record`. `plan-first-mismatch` writes the same move over a plan record whose
  `Scenario` is `scenario.feature` and whose `Scenario reason` is `none`. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- A `new` build's first move into `planning` and its own plant (finding 5): `TOOL-dRankedPlan-37`'s
  item, over S2.
- The reading of `none` and the pin for a build that never enters `planning`: `TOOL-dRankedPlan-20` S1
  and S2, unchanged for every recorded build.
- The claim's writing of the first record and its `scenario=` field: dPlacedRequest's, read here.

### Edges

- **consumes-from** `TOOL-dRankedPlan-20` — S2's exit 2 and the `plan-patch` plant's record, the rule S1 narrows and the record S3 reuses; without them there is no exit to bound
- **consumes-from** `TOOL-dRankedPlan-14` — `check_plan_scenario` and S3's call of it inside `derive_step_scenarios`, which S1 widens by a pin and S2 feeds; without them no check runs at a transition
- **consumes-from** external — dDeclaredLoop's `derive_step_scenarios` and `read_transitions` (TOOL-dDeclaredLoop-27 S8, -3 S7); dPlacedRequest's first transition record and its `scenario=` field (TOOL-dPlacedRequest-21 S7)
- **hands-off** `TOOL-dRankedPlan-37` — S2's pin on the first move, over which that unit's item for finding 5 plants a `new` build's first move into `planning`

## 4. Design

### Evidence

- `TOOL-dRankedPlan-20` S2 and its §4 table row 3: "any · none · none · exit 2, `no transition record
  pins a scenario`".
- `TOOL-dRankedPlan-14` S3 and its pseudo-code: `check_plan_scenario(repo, build)  # S2; a refusal stops
  the move`, run first in `derive_step_scenarios`. Its S2 lists "Exit 0 admitted, 1 refused, 2 on an
  unknown build".
- TOOL-dPlacedRequest-21 S7 writes the build's first record, `new` into `planning` and `patch` and
  `repeat` into `designing`, each carrying ` · scenario=<tags>`. TOOL-dDeclaredLoop-27 S8 counts it as a
  transition into a step.

### The two spellings

| Spelling | First move | The plan record checked on the first move |
|---|---|---|
| finding 29's: skip the check, pin the claim's field | admitted | no |
| finding 5's, taken: the move's field is the pin, the check runs | admitted when the record agrees | yes |

Finding 5's spelling satisfies every criterion the skip satisfies, and also refuses a first move whose
plan record re-picks without a reason, which `plan-first-mismatch` observes. So it is the more
feature-rich option by BUILD-METHOD M3's rule, and it leaves no fork open.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `pin` | keyword parameter of `check_plan_scenario` | none |
| `plan-patch-first`, `plan-first-mismatch` | `scenario.py` fixture plants | none |

### Rollout

Live at landing. Every build placed after it moves its first record through the check.

### Files touched (estimate)

- `tools/loop/scenario.py`: S1 to S3

### Alternatives rejected

- **Skip the check on a build's first record.** It admits a first move whose plan record already
  disagrees with the pin, and the disagreement surfaces only at the next boundary.
- **Treat exit 2 as an admission everywhere.** An unknown build would then pass every step boundary,
  which unit 14 S2 lists exit 2 to stop.

## 5. Production-readiness checklist

- security — N/A — a read path; the move's own field is checked, never trusted as a pass.
- perf / scale — one `read_transitions` call, which S2 already makes.
- error / empty / loading states — a build with no record and no pin still exits 2 naming it.
- observability — the `scenario —` line names the source `placement` for the move's own pin.
- risks — a placement whose plan record was hand-edited before the claim is refused at the first move,
  which is the check working on the earliest boundary.
- testing — the two plants and the CLI's no-record answer.
- migration — none.
- user docs — N/A — `help/loop.md`'s sentence from `TOOL-dRankedPlan-20` S4 already says a patch pins on
  its first transition.

## 6. Acceptance criteria

- **AC1** — When `python scenario.py --fixture --plant plan-patch-first` runs, the claim's first move
  through `python loop_transition.py record` exits 0 and its trailer carries `scenario=scenario.patch`.
  Red when: a build's first move is refused or stopped by the no-record exit.
- **AC2** — When the plant `plan-first-mismatch` runs the same first move, it exits 1 printing
  `scenario re-picked without a reason`.
  Red when: the first move skips the scenario check.
- **AC3** — When `scenario.py plan --build tPatch --check` runs in `plan-patch-first` before the
  first move, it exits 2 naming `no transition record`.
  Red when: a build with no record and no pin answers a pin.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/scenario.py · covers AC1 AC2 AC3 · the `plan-patch-first` and `plan-first-mismatch` plants under `--fixture`, staged by a `derive_step_scenarios` that calls the check with no pin on a first record · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 19 to 29, finding 29 (HIGH,
  item H6; finding 5 is its medium face), repairing `TOOL-dRankedPlan-20`.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-14` S2's `check_plan_scenario`, which gains one optional
parameter, fed by the call unit 14 S3 already makes inside `derive_step_scenarios`. No code exists at
base 0689e7fa, where the loop kit is unbuilt. `python tools/codebase-map/reuse_lookup.py "check a
pending transition against the scenario it pins"` ranked name stems only, so no existing seam fits
beyond the check this unit widens. The recall query returned scout B's row for TOOL-dPlacedRequest-10,
this audit's H6 item and `TOOL-dRankedPlan-20`, and they agree.

Recall terms used: `python tools/memory-recall/query.py "how is the scenario pin checked on a build's first transition record" --terms "check_plan_scenario derive_step_scenarios first transition pin scenario field claim patch designing exit 2"`
