# TOOL-dRankedPlan-23 — `show` reports a revision's ratification from the record of how the re-entering move was admitted

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 14 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-23-deviation-231.md](../build/2026-10-26-build-TOOL-dRankedPlan-23-deviation-231.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`) confirmed
**finding 4 at HIGH**, item **H3**; finding 38 (MEDIUM, item M17) is its cross-session face, kept
apart by grade and closed by the same change, its own counter-plant being `TOOL-dRankedPlan-29`'s.
`TOOL-dRankedPlan-15` S5's `show` judges a revision's ratification by calling
`read_plan_ratification` afresh, while the gate that actually releases the second `plan.exit` is
`TOOL-dRankedPlan-10`'s `check_plan_exit`, which admits on `intake-not-installed`, `disposition` or
`before-placement`, none of which the predicate counts. A re-entry the owner released through the
fallback makes `show` exit 1 with "design re-entered without ratification", and that line is what
Design receives. This unit has `show` read the gate's own record of the re-entry, the `ratification=`
and `harness=` fields on the move, through `TOOL-dRankedPlan-21`'s reader. It repairs
`TOOL-dRankedPlan-15`.

## 2. Scope (IN)

- **S1** — The read. `derive_revision_state(slug, repo)` (`tools/loop/plan_revision.py`,
  `TOOL-dRankedPlan-15` S5) takes the re-entry's ratification from `read_exit_ratification(repo,
  slug)` (`TOOL-dRankedPlan-21` S1): when the newest `plan.exit` move it answers is newer than the
  revision's B6 move, that move is Design re-entered, and its `how` and `harness` are the
  ratification. `derive_revision_state` calls `read_plan_ratification` nowhere. Observed by AC1, AC2
  and AC4.
- **S2** — The lines. A re-entry prints `revision — <n> · ratified · <how> · harness <h> · design
  re-entered at <sha8>` for any recorded `how`, `before-placement` included, since the revision is
  ratified as the plan is and the gate admitted the move. A re-entry whose move carries no
  `ratification` field prints `revision — <n> · design re-entered without a recorded ratification`
  and exits 1. This supersedes unit 15 S5's "the ratification through `read_plan_ratification(slug)`"
  and its line "design re-entered without ratification", and §8 F3's "the standing request ratifies
  the revision". `revision — none`, the awaiting line and the `no field changed` refusal stand.
  Observed by AC1, AC2 and AC3.
- **S3** — The plants. `fallback-disposition` joins `plan_revision.py --selftest --plant <case>`
  (`TOOL-dRankedPlan-15` S6): a revision whose re-entry `check_plan_exit` admitted under the fallback on
  a disposition record, with no typed request in the fixture, so its move carries
  `ratification=intake-not-installed · harness=codex`. The existing plant `unratified-reentry` plants a
  re-entering move with no `ratification` field in place of a stub predicate answering no witness.
  Observed by AC1 and AC2.
- **S4** — `help/loop.md`'s plan-revision section (`TOOL-dRankedPlan-15` S7) says `show` reads how the
  re-entering move was admitted. Observed by AC5.

## 3. Non-goals (OUT)

- The gate and its admissions: `TOOL-dRankedPlan-10` S4, and its repairs at order 5.
- The cross-session counter-plant of finding 38: `TOOL-dRankedPlan-29`'s, over this unit's `show`.
- The revision's grammar, `revise` and its recovery: `TOOL-dRankedPlan-15` S2 and S3, and
  `TOOL-dRankedPlan-29`'s item for finding 46.

### Edges

- **consumes-from** `TOOL-dRankedPlan-15` — `derive_revision_state`, `show` and their `--selftest` plants, whose ratification read S1 re-points; without them there is no revision to report
- **consumes-from** `TOOL-dRankedPlan-21` — `read_exit_ratification`, the one reader of how a `plan.exit` move was admitted; without it `show` would parse the trailer a second way
- **hands-off** `TOOL-dRankedPlan-29` — `show` over the recorded re-entry, against which that unit plants finding 38's later-session counter-case

## 4. Design

### Evidence

- `TOOL-dRankedPlan-15` S5 reads "the ratification through `read_plan_ratification(slug)` (I6, unit
  9)" and prints "design re-entered without ratification" when it answers no witness.
- `TOOL-dRankedPlan-10` §4 "The record" lists four `ratification=` values, one per admission, and S5
  writes them on the `plan.exit` move's trailer and log record.
- `TOOL-dRankedPlan-15` §4 "The flow" step 6 records the re-entry as `plan.exit`'s B4 move, so the
  re-entering move is a `plan.exit` move.

### The state, after this unit

| Newest entry | Moves after its B6 | `show` prints | Exit |
|---|---|---|---|
| none | — | `revision — none` | 0 |
| `<n>` | no `plan.exit` move | `revision — <n> · awaiting ratification · <what>` | 0 |
| `<n>` | a `plan.exit` move with `ratification=<how>` | `revision — <n> · ratified · <how> · harness <h> · design re-entered at <sha8>` | 0 |
| `<n>` | a `plan.exit` move with no `ratification` | `revision — <n> · design re-entered without a recorded ratification` | 1 |
| `<n>` | a re-entry whose fields equal those at `from` | `revision — <n> · no field changed since <sha8>` | 1 |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `fallback-disposition` | `plan_revision.py` selftest plant | none |

### Rollout

Live at landing; no revision exists before `TOOL-dRankedPlan-15` lands one step earlier.

### Files touched (estimate)

- `tools/loop/plan_revision.py`: S1 to S3
- `help/loop.md`: S4's sentence

### Alternatives rejected

- **`show` re-derives the admission from the gate's inputs.** That is the defect: the inputs, the
  session's `.typed` lines among them, move after the gate has read them.
- **`show` reads the trailer field off `read_transitions` itself.** It would be a second reader of the
  same fact `TOOL-dRankedPlan-21` S1 reads; one reader keeps the `unrecorded` rule in one place.

## 5. Production-readiness checklist

- security — N/A — a read path; the field read is written only past `check_plan_exit`.
- perf / scale — one `read_transitions` call, already made by `show`.
- error / empty / loading states — a re-entry with no recorded ratification exits 1 naming it.
- observability — the line names how and on which harness the re-entry was admitted.
- risks — a re-entry recorded before unit 10's fields exist reads unrecorded; none exists, since
  `TOOL-dRankedPlan-15` lands after unit 10.
- testing — `fallback-disposition` and the re-shaped `unratified-reentry`, red and green.
- migration — none.
- user docs — `help/loop.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `python plan_revision.py --selftest --plant fallback-disposition` runs,
  `plan_revision.py show --build tFix` prints `revision — 1 · ratified · intake-not-installed · harness
  codex` and exits 0.
  Red when: a re-entry the owner released through the fallback reads as unratified.
- **AC2** — When the plant `unratified-reentry` runs, `show` prints `design re-entered without a
  recorded ratification` and exits 1.
  Red when: a move carrying no ratification reads as ratified.
- **AC3** — When the plant `goal-fork` runs to its re-entry, `show` prints `ratified · witness`.
  Red when: the counted witness path changes its answer.
- **AC4** — When `grep -c "read_plan_ratification" plan_revision.py` runs over the loop kit's file at
  the pass tip, it prints 0.
  Red when: `show` still asks the session-scoped predicate.
- **AC5** — When `grep -n "re-entering move" loop.md` runs over the help page, it finds S4's sentence.
  Red when: the page still says `show` asks the predicate.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/plan_revision.py · covers AC1 AC2 AC3 · the `fallback-disposition` plant and the re-shaped `unratified-reentry`, staged by a `show` that asks `read_plan_ratification` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's finding 4 (HIGH, item H3,
  related to finding 38), repairing `TOOL-dRankedPlan-15`.

## 10. Reuse audit

The seam extended is `TOOL-dRankedPlan-15` S5's `derive_revision_state`, whose ratification read is
re-pointed to `TOOL-dRankedPlan-21` S1's `read_exit_ratification`, the one reader of the
`ratification=` field `TOOL-dRankedPlan-10` S5 writes. No code exists at base 0689e7fa; the loop kit
is unbuilt there. `python tools/codebase-map/reuse_lookup.py "read how a gate was passed from the
transition record trailer field"` ranked name stems only (`read`, `read_text`, `records`, `field`), so
no existing seam fits beyond the reader this unit consumes. The recall query returned the audit's H3
and M17 items and `TOOL-dRankedPlan-15`'s S5, which agree.

Recall terms used: `python tools/memory-recall/query.py "how does a plan revision's show line say the re-entry was ratified" --terms "plan revision show ratified re-entry plan.exit ratification trailer intake-not-installed disposition harness derive_revision_state"`
