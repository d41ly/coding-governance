# TOOL-dLoggedFlight-15 — a row an owner act can cause carries no time that places the act

**Status:** SPECCED · rev-1 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 15

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The committed record keeps idle gaps away from owner turns, and keeps no other row away. On a POSIX
adopter an owner's interrupt during a driver verb or a bar makes the EXIT trap write an unclean END, or a
`verdict=NONE` gate line, within milliseconds of the transcript's interrupt record. The model publishes
that time as a killed-verb anomaly or a gate row, and the refusal compares whole seconds only. A manual
`/compact` row sits between 0.4 s and 142 s from the owner's command. Closing review round 2 measured
this as R2-H1 and the loop promoted it here. Hold every row an owner act can cause away from owner
turns, as idle gaps already are, and make the renderer unable to emit a new kind of timed row without
deciding which side of that rule it is on.

## 2. Scope (IN)

- **S1** The held set. `OWNER_CAUSED_KINDS` in `tools/runlog/model.py` names the timeline and anomaly
  kinds an owner act can cause: the `killed-verb` anomaly, the `gate` row when its verdict is `NONE`,
  and the `compact` row. A row of those kinds whose time lies within `OWNER_ACT_BAND_S` of an owner turn is kept
  off the committed rows and counted as `near_owner`, the way `derive_idle_gaps` counts a gap. Observed
  by AC1 and AC3.
- **S2** A killed verb's time. A `killed-verb` anomaly takes the verb's START time, never its unclean END
  time, since the START precedes any interrupt of it. Observed by AC2.
- **S3** A window's rendered end. An END reading `exit=unclean` never closes a non-terminal window's
  rendered end; the end is taken from the run's last event that is not an unclean END. Observed by AC2.
- **S4** The refusal. `scan_owner_times` in `tools/runlog/record.py` compares the rendered rows of the
  held kinds against owner turns within `OWNER_ACT_BAND_S`, keeps the same-second comparison for every
  other time, and names the row kind it matched. Observed by AC4.
- **S5** The class gate. `OWNER_INDEPENDENT_KINDS` names every other kind the renderer emits a time for.
  A self-test arm enumerates the kinds the renderer emits a UTC for, from `tools/runlog/record.py`'s
  own layout table, and requires each to be in exactly one of the two sets, in both directions. So the
  next timed kind reds until it is classified. Observed by AC5.
- **S6** The class, recorded. `memory/gotchas/withheld-value-recovered-from-a-derived-one.md` gains
  this instance: an independent event whose time an owner act sets. Observed by AC6.

## 3. Non-goals (OUT)

- Which owner turns are known. `TOOL-dLoggedFlight-14` makes the turns this unit measures against
  come from a source that covers the window.
- Coarsening every rendered time. Round 2's O2 recorded why a band on every UTC trades a leak for
  evidence loss, and the band here is scoped to the kinds an owner act can cause.
- Signal traps. The driver and the hook keep none, per `TOOL-dLoggedFlight-2` §4.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-8` — the anomaly set and the window's end this unit narrows.
- **consumes-from** `TOOL-dLoggedFlight-9` — the renderer's layout table and its refusal.
- **consumes-from** `TOOL-dLoggedFlight-14` — the owner turns, read from a source that covers the window.

## 4. Design

Idle gaps were held because their endpoints are derived from owner turns. These rows are not derived
from owner turns, but an owner act causes them, and their time is the act's time to within the
producer's latency. The rule is the same one: a timed row within reach of an owner turn is counted, not
shown. The band is wider than the interrupt latency because a manual compaction lands up to 142 s after
its command, measured over this node's 31 session extracts on 2026-09-16 by the round-2 synthesis.

The class gate is what keeps this from being a third fold of one class. The renderer already declares
each row kind's columns in one table, so the arm reads the timed kinds from there rather than from a
list typed beside it.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `OWNER_CAUSED_KINDS`, `OWNER_INDEPENDENT_KINDS`, `OWNER_ACT_BAND_S` | constants | none |
| `derive_held_rows` | function | `py.function`, led by `derive` |

### Files touched (estimate)

`tools/runlog/{model.py,record.py,selftest.py,README.md}`,
`memory/gotchas/withheld-value-recovered-from-a-derived-one.md` and `memory/map/features/runlog.md`.

### Alternatives rejected

- A band around every rendered time: rejected by §3 and round 2's O2.
- Dropping killed-verb anomalies and NONE gate rows from the record: rejected, since a Bash-tool
  timeout causes the same rows with no owner involved, and those are evidence.
- A band equal to `IDLE_OWNER_GUARD_S`: rejected as wider than any measured latency, which would hold
  ordinary rows that merely follow an owner's reply.

## 5. Production-readiness checklist

- security — removes the last measured path by which an owner act's time reaches a public record.
- perf / scale — one pass over the timed rows against the owner turns; no git call.
- error / empty / loading states — with no owner turns known, nothing is held and the coverage block
  already says the transcripts were not counted.
- observability — the held count renders beside the idle-gap count, so a reader sees rows were held.
- risks — a genuine killed verb near an owner turn is shown as a count, not a row.
- testing — each AC staged RED on its fixture, including one interrupt in the same second as its END and
  one across a second boundary.
- migration — none.
- user docs — the kit README's record section.

## 6. Acceptance criteria

- **AC1** — When `render_record` renders a fixture run holding an interrupt owner turn followed 10 ms later by
  an END reading `exit=unclean` and a `verdict=NONE` gate line, once within one second and once across a
  second boundary, it refuses nothing, renders no row of either kind within
  `OWNER_ACT_BAND_S` of the turn, and renders the held count.
  Red when: either row renders, or the render is refused.
- **AC2** — When a verb's END reads `exit=unclean` and it is the run's last event, its `killed-verb`
  anomaly carries the START time, and the window's rendered end is not the unclean END's time.
  Red when: the anomaly or the window end carries the unclean END's time.
- **AC3** — When a `compact` row lies 100 s after an owner turn, it is held and counted, and one 400 s
  after is rendered.
  Red when: the near row renders, or the far one is held.
- **AC4** — When `scan_owner_times` is handed a rendered held-kind row within the band of a local owner
  turn, it refuses naming that row's kind, and a same-second match on any other kind still refuses.
  Red when: the refusal names an idle gap for a killed-verb row, or a band match on another kind refuses.
- **AC5** — When the self-test reads the timed kinds from `tools/runlog/record.py`'s layout table, each is
  in exactly one of `OWNER_CAUSED_KINDS` and `OWNER_INDEPENDENT_KINDS`.
  Red when: a timed kind is in neither set, or in both.
- **AC6** — When `python tools/memory-tree/gotchas.py --for-paths tools/runlog/record.py` runs, it selects
  `withheld-value-recovered-from-a-derived-one`, whose record names the owner-caused-row instance.
  Red when: the class record does not name it.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each AC staged RED on its fixture · floor raised by the arm count

## 8. Open questions

- **F1** How wide is `OWNER_ACT_BAND_S`? RESOLVED (agent, 2026-09-16, delegated): 180 s. It covers the
  largest measured latency from an owner's command to its row, 142 s for a manual compaction, with
  margin, and stays well under `IDLE_OWNER_GUARD_S` so ordinary rows after a reply still render.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from closing review round 2's R2-H1 at the loop's
  NON-CONVERGENT exit, with the manual-compaction residue the synthesis sized into the same class.

## 10. Reuse audit

The seam is `derive_idle_gaps` in `tools/runlog/model.py`, whose held-and-counted rule this unit
extends to the kinds an owner act causes, and the renderer's layout table in `tools/runlog/record.py`.
`tools/codebase-map/reuse_lookup.py "hold rows an owner act causes away from owner turns"` returned
name-stem candidates only; the relevant ones are this build's `scan_owner_times`,
`scan_owner_turns` and `build_owner_positions`, and none holds a row near an owner turn.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
