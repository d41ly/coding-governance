---
slug: dHonouredPark
node: d
opened: 2026-08-25
streams: tooling
roster: TOOL
ids: TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 TOOL-dHonouredPark-5 TOOL-dHonouredPark-6 TOOL-dHonouredPark-7
parents: dFramedEntrypoint
---

# dHonouredPark — the four rulings dFramedEntrypoint parked, built

## The problem this build exists to solve

`dFramedEntrypoint` landed with five decisions parked because taking them was outside its stated
goal, and the owner has since ruled four of them. Each ruling is real work in a kit that build did
not own: a Definition-of-Done term that passed vacuously on 51 of 62 builds at this build's base
has to become a real check, a governance carrier's declared budget has to move, a waiver registry
has to stop being keyed on a line number that any insertion above it invalidates, and two driver verbs have to
stop answering one question differently. A ruling nobody builds is a park with a nicer name.

## Expected improvements

- `build-complete` term 3 becomes a check that can fail, on every tracked build README instead of the
  eleven that happen to carry a roster pair.
- A waiver registry stops unpinning every time an unrelated line is inserted above a waived hit.
- `--plan` and `--status` answer "which unit is next" from one source and cannot drift apart.

## Detriments if this is not built

- Four owner rulings sit as backlog rows while the conditions that earned them stay live.
- A Definition-of-Done item keeps reporting a pass it did not earn on most of the corpus. The share is
  not written here, because it moves with every build that lands.
- The next insertion above a waived dead-path hit reds the bar for a reason unrelated to the change.

## Build-level rules

- Every unit that moves `tools/memory-tree/gen_build_index.py` or `tools/unattended/unattended.sh`
  bumps its kit version across the DERIVED carrier set — `git grep -l 'gov:kit <kit>@'` outside
  `memory/builds/` and `memory/archive/`, never the set an epoch gate's remedy text names.
- A unit that grows a capped read-path member prices its OWN charge against `READ_PATH_CEILING`.
- Two kits are touched here and they are separate streams. Check `git log origin/main -20` over each
  before starting a unit inside it, per the manifest's own concurrent-rewrite rule.

## Parked decisions

None yet. This build exists to unpark, so a park taken here is a ruling that turned out to need
another one — and it goes on the run-state file with its options, not in this slot.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dHonouredPark-2` | 1 | the build method's declared line budget rises to 350, and the byte half stays where it is |
| 2 | `TOOL-dHonouredPark-3` | 2 | the dead-path waiver registry keys on line TEXT plus an occurrence ordinal, not a line NUMBER |
| 3 | `TOOL-dHonouredPark-1` | 2 | the authored roster pair becomes mandatory on every build README, and its Definition-of-Done... |
| 4 | `TOOL-dHonouredPark-4` | 2 | `--plan` takes its unit SET and its ORDER from the rendered region, so both verbs answer from... |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 4 unit(s) · node d · opened 2026-08-25 · streams tooling
ids TOOL-dHonouredPark-1 TOOL-dHonouredPark-2 TOOL-dHonouredPark-3 TOOL-dHonouredPark-4 TOOL-dHonouredPark-5 TOOL-dHonouredPark-6 TOOL-dHonouredPark-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dHonouredPark-2 — the build method's declared line budget rises to 350, and the byte half stays where it is](spec/2026-08-25-spec-dHonouredPark-2.md) | 1 | 1 | CLOSED | rev-5 | 2026-08-25 |
| [TOOL-dHonouredPark-3 — the dead-path waiver registry keys on line TEXT plus an occurrence ordinal, not a line NUMBER](spec/2026-08-25-spec-dHonouredPark-3.md) | 2 | 2 | CLOSED | rev-5 | 2026-08-25 |
| [TOOL-dHonouredPark-1 — the authored roster pair becomes mandatory on every build README, and its Definition-of-Done term becomes a check that can fail](spec/2026-08-25-spec-dHonouredPark-1.md) | 3 | 2 | CLOSED | rev-5 | 2026-08-25 |
| [TOOL-dHonouredPark-4 — `--plan` takes its unit SET and its ORDER from the rendered region, so both verbs answer from one source](spec/2026-08-25-spec-dHonouredPark-4.md) | 4 | 2 | CLOSED | rev-6 | 2026-08-25 |
<!-- /gen:build-units -->

Records: 6 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dHonouredPark-2` | no |
| 2 | `TOOL-dHonouredPark-3` | no |
| 3 | `TOOL-dHonouredPark-1` | no |
| 4 | `TOOL-dHonouredPark-4` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dFramedEntrypoint](../dFramedEntrypoint/README.md)
<!-- /gen:build-edges -->
