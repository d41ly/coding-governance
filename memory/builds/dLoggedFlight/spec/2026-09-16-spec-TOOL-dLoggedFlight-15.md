# TOOL-dLoggedFlight-15 — a row an owner act can cause carries no time that places the act

**Status:** WONTDO · rev-2 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 17 · superseded by TOOL-dLoggedFlight-20 (owner, 2026-09-16: the committed record carries no journal or transcript time)

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-review-TOOL-dLoggedFlight-14-spec-audit-round1.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-14-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-14 |

<!-- /gen:spec-records -->

## 1. Goal

The committed record keeps idle gaps away from owner turns, and keeps no other row away. On a POSIX
adopter an owner's interrupt during a driver verb or a bar makes the EXIT trap write an unclean END, or a
`verdict=NONE` gate line, within milliseconds of the transcript's interrupt record. The model publishes
that time as a killed-verb anomaly or a gate row, and the refusal compares whole seconds only. A manual
`/compact` row sits between 0.4 s and 142 s from the owner's command. Closing review round 2 measured
this as R2-H1 and the loop promoted it here. Hold every row an owner act can cause away from owner
turns, as idle gaps already are.

The spec audit of this unit, round 1, moved two halves out. The window's rendered end and the
commitment's times are `TOOL-dLoggedFlight-18` (H1, H2). The class gate over every time the record
carries is `TOOL-dLoggedFlight-19` (H3).

## 2. Scope (IN)

- **S1** The held set. `OWNER_CAUSED_KINDS` in `tools/runlog/model.py` names the timeline and anomaly
  kinds an owner act can cause: the `killed-verb` anomaly, the `gate` row when its verdict is `NONE`,
  and the `compact` row. A row of those kinds whose time lies within `OWNER_ACT_BAND_S` of an owner turn is kept
  off the committed rows and counted as `near_owner`, the way `derive_idle_gaps` counts a gap. Observed
  by AC1 and AC3.
- **S2** A killed verb's time. A `killed-verb` anomaly takes the verb's START time, never its unclean END
  time, since the START precedes any interrupt of it. Observed by AC2.
- **S3** Moved to `TOOL-dLoggedFlight-18`, which keeps every owner-causable line, the `verdict=NONE`
  gate line included, off the window's RENDERED end. `derive_window` and `check_in_window` keep
  `TOOL-dLoggedFlight-8` S2's rule, so no bounded set loses a line and an interrupt keeps its S9
  position. NOT OBSERVED here: that unit's AC2 and AC3 observe it.
- **S4** The refusal. `scan_owner_times` in `tools/runlog/record.py` compares the rendered rows of the
  held kinds within `OWNER_ACT_BAND_S` against every owner turn it holds: the model's, and those
  `TOOL-dLoggedFlight-17` reads independently. It keeps the same-second comparison for every other UTC
  token, and names the row kind it matched. An idle row is not a held kind: beyond the same-second
  comparison, `TOOL-dLoggedFlight-17` S4 holds it to `IDLE_OWNER_GUARD_S`. Observed by AC4.
- **S5** Moved to `TOOL-dLoggedFlight-19`, whose class gate takes its population from every UTC slot
  of `RECORD_SCHEMA` rather than from the Timeline's row kinds. NOT OBSERVED here: that unit's criteria
  observe it.
- **S6** The class, recorded. `memory/gotchas/withheld-value-recovered-from-a-derived-one.md` gains
  this instance: an independent event whose time an owner act sets. Observed by AC6.

## 3. Non-goals (OUT)

- Which owner turns are known. `TOOL-dLoggedFlight-14` makes the turns this unit measures against
  come from a source that covers the window.
- Coarsening every rendered time. Round 2's O2 recorded why a band on every UTC trades a leak for
  evidence loss, and the band here is scoped to the kinds an owner act can cause.
- Signal traps. The driver and the hook keep none, per `TOOL-dLoggedFlight-2` §4.
- The derived times an owner-causable line could set, the window's end and the commitment's first and
  last. `TOOL-dLoggedFlight-18` owns them.
- The class gate. `TOOL-dLoggedFlight-19` owns it.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-8` — the anomaly set this unit narrows.
- **consumes-from** `TOOL-dLoggedFlight-9` — the renderer's refusal, which this unit extends to held
  rows.
- **consumes-from** `TOOL-dLoggedFlight-14` — the owner turns, read from a source that covers the window.
- **consumes-from** `TOOL-dLoggedFlight-17` — the independently read owner turns the band also
  compares against.
- **hands-off** `TOOL-dLoggedFlight-18` — `OWNER_ACT_BAND_S` and the owner turns the window's rendered
  end is held against.
- **hands-off** `TOOL-dLoggedFlight-19` — the held kinds the class gate classifies.

## 4. Design

Idle gaps were held because their endpoints are derived from owner turns. These rows are not derived
from owner turns, but an owner act causes them, and their time is the act's time to within the
producer's latency. The rule is the same one: a timed row within reach of an owner turn is counted, not
shown. The band is wider than the interrupt latency because a manual compaction lands up to 142 s after
its command, measured over this node's 31 session extracts on 2026-09-16 by the round-2 synthesis.

A held row still has a time in two derived values, and a new timed slot could be added to the schema
unheld. Those are the two halves this unit's audit moved to `TOOL-dLoggedFlight-18` and
`TOOL-dLoggedFlight-19`.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `OWNER_CAUSED_KINDS`, `OWNER_ACT_BAND_S` | constants | none |
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

- security — removes the row paths by which an owner act's time reaches a public record; the derived
  times are `TOOL-dLoggedFlight-18`'s.
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
  fixture: rendered with `commitment=None`, the renderer's default. The production shape, with the
  commitment `write_record` passes, is `TOOL-dLoggedFlight-18` AC4 and `TOOL-dLoggedFlight-19` AC4.
- **AC2** — When a verb's END reads `exit=unclean` and it is the run's last event, the `t` of its
  `killed-verb` anomaly from `scan_anomalies` equals that verb's START time exactly.
  Red when: the anomaly's `t` is any other value; staged RED against unchanged code, where it is the
  END's time (`tools/runlog/model.py:1136`).
- **AC3** — When a `compact` row lies 100 s after an owner turn, it is held and counted, and one 400 s
  after is rendered.
  Red when: the near row renders, or the far one is held.
- **AC4** — When `scan_owner_times` is handed a rendered held-kind row within the band of an owner turn,
  it refuses naming that row's kind. A same-second match on a kind neither held nor idle still refuses.
  An idle row is graded by `TOOL-dLoggedFlight-17`'s comparison, not by this band.
  Red when: the refusal names an idle gap for a killed-verb row, or a band match on another kind refuses.
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
- rev-2 · 2026-09-16 · §1 · §3 · §4 · S3 S4 S5 · AC1 AC2 AC4 AC5 · folded the spec audit of units 14
  and 15, round 1. M1: AC2 asserts the anomaly's START time by equality and reds against unchanged
  code, and its window-end half, whose red could not fire, moved to `TOOL-dLoggedFlight-18` AC2 in the
  form M1 gives. M2: S3's pointer states which window moves. The model's does not, and only the
  rendered end does, under `TOOL-dLoggedFlight-18` S3. H4's reconciliation: S4 excludes idle rows,
  which `TOOL-dLoggedFlight-17` compares. H1's production shape: AC1 names the criteria that render with
  a real commitment. The promotions: H1 and H2 went to `TOOL-dLoggedFlight-18`, which takes S3. H3 went
  to `TOOL-dLoggedFlight-19`, which takes S5 and AC5, and whose slot classes replace
  `OWNER_INDEPENDENT_KINDS`. The order moves from 15 to 17, after the two units whose turns S4 reads.

## 10. Reuse audit

The seam is `derive_idle_gaps` in `tools/runlog/model.py`, whose held-and-counted rule this unit
extends to the kinds an owner act causes, and the renderer's refusal in `tools/runlog/record.py`.
`tools/codebase-map/reuse_lookup.py "hold rows an owner act causes away from owner turns"` returned
name-stem candidates only; the relevant ones are this build's `scan_owner_times`,
`scan_owner_turns` and `build_owner_positions`, and none holds a row near an owner turn.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
