---
slug: aClosedDocket
node: a
opened: 2026-08-31
streams: tooling
roster: TOOL
ids: TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 TOOL-aClosedDocket-3 TOOL-aClosedDocket-4
authorized-by: prompt
---

# aClosedDocket — drain the three rows aProvenReuse filed rather than built

## The problem this build exists to solve

`aProvenReuse` landed and filed three findings it could not take: `TOOL-aProvenReuse-3`, `-4` and
`-6`. Each was filed for a stated reason and each reason has now expired. `-3` is a rule with no
legal disposition for a case that occurs; `-4` leaves one of `BUILD-METHOD` M5's two probes
unobservable, so the liveness half that build added covers half its own obligation; `-6` is a
wall-clock assertion that flaked three times in one session on this fleet. The owner's prose is the
mandate and is recorded under [prompts/](prompts/2026-08-31-prompt-TOOL-aClosedDocket-1.md).

## Expected improvements

- A NON-CONVERGENT exit over a SPEC subject has a disposition a run can follow without departing
  from the rule and writing an explanation, which is what the last two builds both had to do.
- Both of M5's probes leave evidence, so `reuse-probed` stops being blind to the map half.
- The bounded-observation arms measure what the bound measures, so a busy machine stops producing
  red that means nothing.

## Detriments if this is not built

- The next run to hit NON-CONVERGENT over a spec set improvises again, and improvisations diverge.
- `reuse-probed` keeps reporting on one probe while the directive names two.
- A flaky arm trains its readers to discount a red bar, which is the failure that costs most.

## Build-level rules

- **Classification (M2)**: three units, MISSING at open, authored this run. Each is one mechanism.
- **The owner's instruction IS the veto-2 turn, and this build may not pretend otherwise.** Unit 1
  edits `BUILD-METHOD.template.md`, a governance carrier, and M3 veto 2 makes that an owner turn that
  a standing mandate does not delegate. The instruction names the row by id, so the turn was taken;
  what it does NOT license is widening the edit beyond what the row states.
- **Unit 2 may not create a cross-kit dependency**, which is the reason `-4` was filed rather than
  built. `codebase-map` writes its own log under its own name and neither kit learns the other's
  path; the unattended item counts whichever logs exist. `RECALL_CLI` is the declaration idiom that
  makes this possible and it already ships.
- **Unit 3 changes what an arm MEASURES, not what it asserts.** The bound is already observed
  correctly — its own message fires every time — so the mechanism is sound and only the harness's
  clock is wrong. An arm that starts asserting something new here would be a different unit.

## Parked decisions

None yet. Parked entries live in `RUN.md` and are surfaced in the wrap-up.

**The spec-audit loop exited NON-CONVERGENT at 3 then 4 blockers**, and unit 4 is the promotion that
exit calls for — round 2's B2 said unit 1 held a document, a gate and a driver fact under one id
against M2's verbatim rule, and closing that needed a MECHANISM the build did not have, which is a
second unit. That is promotion in its literal sense rather than a departure from it, which is worth
recording because the rule this build is written to fix is the same rule it just obeyed.

**Filed, not folded:** clause 3 is separately VACUOUS on the prompt path. Measured on `aProvenReuse`
— two subjects exited NON-CONVERGENT, the clause wanted two ids new since BASE and found three,
because that run's BASE was its own opening commit with an empty units region. Every original unit
read as promoted; none was. Unit 4's N2 records why closing it needs a signal nothing carries today.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aClosedDocket-1` | OPEN | M4 gains a disposition for a NON-CONVERGENT exit over a spec |
| 2 | `TOOL-aClosedDocket-2` | OPEN | `reuse_lookup.py` logs, and `reuse-probed` counts either probe |
| 3 | `TOOL-aClosedDocket-3` | OPEN | the bounded-observation arms assert on `RB_TOOK`, not the harness clock |
| 4 | `TOOL-aClosedDocket-4` | OPEN | clause 3 accepts a FOLD, and the driver records one |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 4 unit(s) · node a · opened 2026-08-31 · streams tooling
ids TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 TOOL-aClosedDocket-3 TOOL-aClosedDocket-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aClosedDocket-1 — M4 gains a disposition for a NON-CONVERGENT exit over a spec](spec/2026-08-31-spec-TOOL-aClosedDocket-1.md) | 1 | 2 | CLOSED | rev-3 | 2026-08-31 |
| [TOOL-aClosedDocket-2 — `reuse_lookup.py` logs, and `reuse-probed` counts either probe](spec/2026-08-31-spec-TOOL-aClosedDocket-2.md) | 2 | 2 | CLOSED | rev-5 | 2026-08-31 |
| [TOOL-aClosedDocket-3 — the bounded-observation arms assert on `RB_TOOK`, not the harness clock](spec/2026-08-31-spec-TOOL-aClosedDocket-3.md) | 3 | 2 | CLOSED | rev-4 | 2026-08-31 |
| [TOOL-aClosedDocket-4 — clause 3 accepts a FOLD, and the driver records one](spec/2026-08-31-spec-TOOL-aClosedDocket-4.md) | 4 | 2 | WONTDO | rev-2 | 2026-08-31 |
<!-- /gen:build-units -->

Records: 5 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aClosedDocket-1` | no |
| 2 | `TOOL-aClosedDocket-2` | no |
| 3 | `TOOL-aClosedDocket-3` | no |
| 4 | `TOOL-aClosedDocket-4` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
