# TOOL-dRankedPlan-20 — a plan record's `Scenario: none` reads as no re-pick, and a build that never enters `planning` pins on its first transition

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 7 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-20-deviation-201.md](../build/2026-10-26-build-TOOL-dRankedPlan-20-deviation-201.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-74 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) | spec-audit | TOOL-dRankedPlan-27 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-19 TOOL-dRankedPlan-28 TOOL-dRankedPlan-23 TOOL-dRankedPlan-29 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`) confirmed
**finding 2 at HIGH**, item **H1**. `TOOL-dRankedPlan-16` S8 writes a patch's or a repeat's plan record
with every field but `Problem` and `Goal` set to `none`, and its S3 makes `none` the written form of an
empty field. `TOOL-dRankedPlan-14` S1 special-cases `none` only for `Scenario reason`, so `Scenario:
none` reads as a re-pick of `scenario.none`, which S2 refuses as unreasoned or unregistered and S3
runs at every step transition. Its pin is the first transition record into `planning`, which a patch
or a repeat never writes: `TOOL-dPlacedRequest-21` S7 records their first move into `designing`. Once
unit 14 lands, every build `--placed-build` opens is refused at each step boundary. This unit repairs
`TOOL-dRankedPlan-14`'s reader: `none` is no value, and a build with no move into `planning` pins on
its first transition record.

## 2. Scope (IN)

- **S1** — `none` is empty. `read_plan_scenario(repo, slug)` (`tools/loop/scenario.py`,
  `TOOL-dRankedPlan-14` S1) reads a `Scenario` of `none`, matched whole after stripping, as it reads an
  absent or empty one: it answers the pin with source `placement`. The namespacing of a bare tag
  applies only to a value that is not `none`. Observed by AC1 and AC2.
- **S2** — The pin for a build that never enters `planning`. The pin is the `scenario` field of the
  build's first transition record into `planning`, read by `read_transitions`
  (`TOOL-dDeclaredLoop-3` S7), and, where the build has no such record, the `scenario` field of its
  first transition record, which for a patch or a repeat is the claim's move into `designing`
  (`TOOL-dPlacedRequest-21` S7). A build with no transition record has no pin, and `check_plan_scenario`
  exits 2 naming `no transition record pins a scenario for <slug>`, as unit 14 S2 exits 2 on an
  unknown build. Observed by AC1 and AC3.
- **S3** — The plants `plan-patch`, `plan-repeat` and `plan-none-planning` join `scenario.py --fixture`
  (`TOOL-dRankedPlan-14` S4). `plan-patch` and `plan-repeat` carry the exact record
  `TOOL-dRankedPlan-16` S8 writes, so the writer's canonical output is fed to this reader.
  Observed by AC1, AC2 and AC3.
- **S4** — The paragraph `TOOL-dRankedPlan-14` S5 adds to `help/loop.md`'s scenarios section gains
  one sentence: `Scenario: none` keeps the placement's scenario, and a patch or a repeat pins on its
  first transition. Observed by AC4.

## 3. Non-goals (OUT)

- The patch's and the repeat's plan record: `TOOL-dRankedPlan-16` S8 writes it as it stands, `none` in
  every empty field (§4 "Alternatives rejected").
- The re-pick rule, the order check and the after-Plan refusal: `TOOL-dRankedPlan-14` S2 and S3,
  unchanged for every value but `none`.
- Scenario selection at placement: `TOOL-dPlacedRequest-10`'s.

### Edges

- **consumes-from** `TOOL-dRankedPlan-14` — `read_plan_scenario` and `check_plan_scenario`, the reader and check S1 and S2 correct; without them there is no pin to read
- **consumes-from** `TOOL-dRankedPlan-16` — S8's patch and repeat plan record, the canonical writer output whose `Scenario: none` S3's plants feed to the reader
- **hands-off** `TOOL-dRankedPlan-36` — S2's exit 2 and the `plan-patch` record, which that unit narrows to a build with no record and no pin given (spec audit of units 19 to 29, id 29)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-16` S3: each field value is "one line, `none` where the field holds nothing"; S8:
  a patch's record has "every other field `none`"; its AC2 refuses a record missing a field, so an
  empty field cannot be written as an absent line.
- `TOOL-dRankedPlan-14` S1: "a `Scenario reason` of `none` is no reason", and "a `Scenario` that is
  absent, empty or equal to the pin answers the pin"; `none` is not in that list.
- `TOOL-dPlacedRequest-21` S7: the claim writes the build's first transition record, "`new` into
  `planning`, `repeat` into `designing`, and `patch` into `designing`", carrying ` · scenario=<tags>`.

### The reading after this unit

| `Scenario` | Transition records | Pin | Answer |
|---|---|---|---|
| absent, empty or `none` | a move into `planning` | its `scenario` | the pin, `from placement` |
| absent, empty or `none` | no move into `planning` | the first record's `scenario` | the pin, `from placement` |
| any | none | none | exit 2, `no transition record pins a scenario` |
| a tag, equal to the pin | either | as above | the pin, `from placement` |
| a tag, different | either | as above | unit 14 S2's re-pick rules, unchanged |

### The plants

| Plant | Plan record | First transition | Expected |
|---|---|---|---|
| `plan-patch` | unit 16 S8's patch record, `Scenario: none`, `Scenario reason: none` | `designing`, `scenario=scenario.patch` | `scenario — scenario.patch · from placement · reason none`; `--check` exits 0; the next transition into a step is admitted |
| `plan-repeat` | unit 16 S8's repeat record | `designing`, `scenario=scenario.repeat` | the same, its own tag |
| `plan-none-planning` | a feature record whose `Scenario` is `none` | `planning`, `scenario=scenario.feature` | the pin, `from placement`, and `--check` exits 0 |

The tags are the fixture's planted scenario rows; the build run reads the landed names from
`scenario.py members` (`TOOL-dDeclaredLoop-27`) and plants those.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `plan-patch`, `plan-repeat`, `plan-none-planning` | `scenario.py` fixture plants | none |

### Rollout

Live at landing; a build whose record reads `none` behaves as if the field were absent, which is how
unit 14 already reads an absent one.

### Files touched (estimate)

- `tools/loop/scenario.py`: S1 to S3
- `help/loop.md`: S4's sentence

### Alternatives rejected

- **`TOOL-dRankedPlan-16` S8 leaves `Scenario` absent.** The kind requires each of its eleven fields
  (unit 16 AC2), so an absent line is a refused record, and every other reader of a plan field already
  takes `none` as empty.
- **Pin a patch on its claim's placement record instead of its first transition.** The transition
  record is where `TOOL-dDeclaredLoop-27` S8 pins scenarios and where unit 14 already reads; a second
  source would be a second home for one fact.

## 5. Production-readiness checklist

- security — N/A — a read path only; no new write or surface.
- perf / scale — one more transition read in the rare case of no move into `planning`.
- error / empty / loading states — no transition record exits 2 naming it; never a silent pin.
- observability — the `scenario —` line names its source.
- risks — a planner who means a scenario literally named `none` cannot pick it; no scenario row is
  named `none`, and the namespace makes such a tag `scenario.none`.
- testing — the three plants, red and green.
- migration — none.
- user docs — `help/loop.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `python scenario.py --fixture --plant plan-patch` runs, `scenario.py plan
  --build tPatch` prints `from placement · reason none` with the first record's tag, and `scenario.py
  plan --build tPatch --check` exits 0.
  Red when: `Scenario: none` reads as a re-pick, or the patch has no pin.
- **AC2** — When the plant `plan-none-planning` runs, `scenario.py plan --build tFix --check` exits 0
  and prints `from placement`; the existing plant `plan-repick-no-reason` still exits 1.
  Red when: `none` is namespaced into a tag, or a real re-pick without a reason is admitted.
- **AC3** — When the plant `plan-repeat` runs the next transition into a step through `python
  loop_transition.py record`, the move is admitted; with its transition record removed from the
  fixture, `scenario.py plan --build tRepeat --check` exits 2 naming `no transition record`.
  Red when: a repeat build is refused at a step boundary, or a build with no pin answers one.
- **AC4** — When `grep -n "Scenario: none" loop.md` runs over the help page, it finds S4's sentence.
  Red when: the page does not say how `none` reads.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/scenario.py · covers AC1 AC2 AC3 · the `plan-patch`, `plan-repeat` and `plan-none-planning` plants under `--fixture`, staged by a reader that namespaces `none` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's finding 2 (HIGH, item H1),
  repairing `TOOL-dRankedPlan-14`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-36`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-14` S1's `read_plan_scenario`, its empty-value rule widened by
one value and its pin read widened by one fallback through the same `read_transitions`
(`TOOL-dDeclaredLoop-3` S7). No code exists at base 0689e7fa; the loop kit is unbuilt there. `python
tools/codebase-map/reuse_lookup.py "read a plan field whose value none means empty"` returned name
stems only; the one existing rule that `none` is empty is unit 14's own `Scenario reason` reading, which
S1 reuses, so no existing seam fits beyond the reader this unit repairs. The recall query returned
scout A's row for unit 14, the audit's H1 item and `TOOL-dPlacedRequest-21`'s S7, which agree.

Recall terms used: `python tools/memory-recall/query.py "how does a patch build's plan record read its scenario pin" --terms "Scenario none patch repeat placed-build pin first transition record re-pick read_plan_scenario"`
