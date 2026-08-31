---
slug: aClosedDocket
node: a
opened: 2026-08-31
streams: tooling
roster: TOOL
ids: TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 TOOL-aClosedDocket-3
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

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aClosedDocket-1` | OPEN | M4 gains a disposition for a NON-CONVERGENT exit over a spec |
| 2 | `TOOL-aClosedDocket-2` | OPEN | `reuse_lookup.py` logs, and `reuse-probed` counts either probe |
| 3 | `TOOL-aClosedDocket-3` | OPEN | the bounded-observation arms assert on `RB_TOOK`, not the harness clock |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 3 unit(s) · node a · opened 2026-08-31 · streams tooling
ids TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 TOOL-aClosedDocket-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aClosedDocket-1 — M4 gains a disposition for a NON-CONVERGENT exit over a spec](spec/2026-08-31-spec-TOOL-aClosedDocket-1.md) | 1 | 2 | OPEN | rev-1 | 2026-08-31 |
| [TOOL-aClosedDocket-2 — `reuse_lookup.py` logs, and `reuse-probed` counts either probe](spec/2026-08-31-spec-TOOL-aClosedDocket-2.md) | 2 | 2 | OPEN | rev-1 | 2026-08-31 |
| [TOOL-aClosedDocket-3 — the bounded-observation arms assert on `RB_TOOK`, not the harness clock](spec/2026-08-31-spec-TOOL-aClosedDocket-3.md) | 3 | 2 | OPEN | rev-1 | 2026-08-31 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 TOOL-aClosedDocket-3.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aClosedDocket-1` | no |
| 2 | `TOOL-aClosedDocket-2` | no |
| 3 | `TOOL-aClosedDocket-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
