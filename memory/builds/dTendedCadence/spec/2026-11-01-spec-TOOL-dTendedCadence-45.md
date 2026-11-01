# TOOL-dTendedCadence-45 — a cyclic playbook's repeat intake text carries no period, so an open cycle recurs instead of stacking a second build

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 17 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-44 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 42 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, item H10. Unit 11's intake text ends `cycle: <daily|weekly> <period>` (spec-11 §4 "The intake",
:121-126). Unit 8's filing detects a recurrence only by content key, the hash of the text, and
requires the text to carry "no value, period or SHA" (spec-8 :209-210); its AC7 names a period in the
text as the red case (:292-294). Every cycle therefore files a fresh intake, and S6's "a cycle whose
build has not finished never stacks a second build" fails. This unit drops the period from the text.
Its sibling, id 11 (M7, the filing taking no text or filer), is carried by TOOL-dTendedCadence-48.

## 2. Scope (IN)

- **S1** — The text. `run_repeat_intakes` in `tools/drift-audit/playbook_cycle.py` hands the filing
  §4's four lines, `cycle:` naming the kind alone, so the content key depends on the playbook's path,
  its piece count and its cycle kind and on nothing a period moves. Observed by AC1.
- **S2** — The period stays on the run's line: `playbook-cycle — <path> · filed <content key> ·
  <period>` and `· seen <period>`, read from `GOV_CADENCE_KEY` as unit 11 S5 says. Observed by AC1.

## 3. Non-goals (OUT)

- The filing's text and filer parameters on unit 8's call: id 11, TOOL-dTendedCadence-48.
- A shared lint over every caller's intake text: the report's left-shift gate, a separate mechanism
  over units 8, 9, 11 and 15, not built here.

### Edges

- **consumes-from** `TOOL-dTendedCadence-11` — `run_repeat_intakes` and its intake text, which this unit re-states without the period
- **hands-off** `TOOL-dTendedCadence-53` — the period-free four lines, which that unit extends with the `after:` line naming the last finished cycle's build (review id 15)
- **hands-off** `TOOL-dTendedCadence-54` — the repeat filing over unit 11's plant, whose cycles past a built one that unit's arm files (review id 40)
- **hands-off** `TOOL-dTendedCadence-59` — the repeat intake's cross-node dedupe and the Files touched, which the minors batch repairs (review ids 38, 41)

## 4. Design

### The intake

```
repeat <path>
playbook: <path>
pieces: <cycle_pieces>
cycle: <daily|weekly>
```

A playbook whose piece count changes files a new intake, which is a new request: the repeat build
copies `pieces:` into its front matter (unit 11 §4).

### Inventory

Minted: nothing.

### Files touched (estimate)

- `tools/drift-audit/playbook_cycle.py`: S1, S2
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **Key the recurrence on `(playbook-cycle, <path>)` and keep the period in the text.** Unit 8's
  filing keys by text; a second keying rule for one caller is the second spelling the finding warns of.

## 5. Production-readiness checklist

- security — N/A — the text names a tracked path and two counts, as before.
- perf / scale — N/A.
- error / empty / loading states — unchanged from unit 11 S5.
- observability — S2's line still names the period.
- risks — a cycle whose previous intake was closed and not built files nothing new while the content
  key stands on record; the receipt says the cycle came round.
- testing — the criteria of §6.
- migration — N/A — the filer is new in this build.
- user docs — `help/maintain.md`'s section "Cyclic playbooks" shows the four lines.

## 6. Acceptance criteria

- **AC1** — When `python playbook_cycle.py --cycle weekly` runs twice over unit 11's `file-weekly`
  plant, under `GOV_CADENCE_KEY=2026-W44` and then `2026-W45`, with a recording filer, the two recorded
  texts are byte-equal and carry no `W44` or `W45`, and the two run lines name `2026-W44` and
  `2026-W45`.
  Red when: the text carries the period, so the two content keys differ.
- **AC2** — When the same two runs file through `intake.py file` into a scratch intake store, the
  store holds one intake for the playbook with two receipts.
  Red when: a second intake is filed for one open cycle.
  fixture: `intake.py` is TOOL-dWellOiledMachine-27's, absent at `f4597719`.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 · two periods over one plant with a recording filer, staged against the text carrying `<period>` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 42 (HIGH, item H10) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (units 53, 54 and 59); no scope, design or criterion moved.

## 10. Reuse audit

The seam is unit 11's `run_repeat_intakes` and the content-key rule of unit 8's filing (spec-8 S7,
:209-210), which this unit conforms to rather than extends. `python tools/codebase-map/reuse_lookup.py
"file a records-only intake so a written record is committed and landed"` named no intake-text
builder; neither module exists at base, so no existing seam fits beyond those two units.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
