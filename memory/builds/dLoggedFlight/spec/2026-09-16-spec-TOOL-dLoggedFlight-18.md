# TOOL-dLoggedFlight-18 — an owner-causable journal line sets neither the window's rendered end nor the commitment's times

**Status:** SPECCED · rev-1 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 18

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-15` holds the rows an owner act causes, and at rev-1 left two derived times
reading the lines behind them. The Summary `commitment` renders `last`, the time of the latest journal
line the run holds (`tools/runlog/record.py:936-972`). An unclean END or a `verdict=NONE` gate line,
written 10 ms after an owner's interrupt, is that line (H1). A non-terminal window ends one second after
its last event (`tools/runlog/model.py:420-422`), and unit 15 S3 kept only an unclean END from closing
it. A NONE gate line that is the last event still sets the `window` and `duration` facts (H2). The spec
audit of units 14 and 15, round 1, confirmed both as HIGH, and the loop promoted them here. No derived
time takes the time of a line an owner's interrupt can make. `verify` still recomputes the commitment
exactly, and the model's window, which bounds every derived set, does not move.

Every code line cited here was read at `a6f9d52e` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The predicate. `check_owner_causable(fields)` in `tools/runlog/model.py` answers True for the
  parsed fields of a journal line an owner's interrupt can make: an `end` line of any producer
  reading `exit=unclean`, and a gates line reading `verdict=NONE`. It reads no owner turn, so a
  machine holding journals and no transcript reaches the same answer. Observed by AC1.
- **S2** The window's rendered end. Each source of the non-terminal end that `build_run_model` passes
  `derive_window` as `last_event` (`model.py:1459`) keeps whether its line is owner-causable. Once the
  owner turns are known, the model records `window["shown_end"]`:
  - equal to `window["end"]`, unless `end_from` is `last-activity`;
  - otherwise one second after the latest end source left once every owner-causable line within
    `OWNER_ACT_BAND_S` of an owner turn the model holds is set aside. A set-aside unclean END is
    replaced by its invocation's START, which precedes the interrupt.

  With no owner turn known, nothing is set aside and `shown_end` equals `end`, the rule unit 15 S1
  keeps for rows. `build_summary_facts` renders the `window` fact's end and the `duration` fact from
  `shown_end` (`record.py:643-646`). The `window closed by` fact is unchanged. Observed by AC2.
- **S3** What does not move, which is M2's question answered. `derive_window`, `check_in_window` and
  every set they bound keep `TOOL-dLoggedFlight-8` S2's rule. The unclean END's verb, the NONE gate
  line and the interrupt all stay inside the window. The gate line stays in the timeline, in
  `journal_lines` and in the commitment's hash. The interrupt keeps its `TOOL-dLoggedFlight-8` S9
  position, `in-window`. So the model carries two values, `end` for bounding and `shown_end` for
  rendering, and the record renders only `shown_end`. Observed by AC3.
- **S4** The commitment's times. `measure_commitment` hashes and counts every line it picks, as today.
  It takes `first` and `last` from the earliest and the latest picked line for which
  `check_owner_causable` is False. The rule is by line kind and not by band, because `verify` rebuilds
  the model from journals alone and holds no owner turn. When every picked line is owner-causable, the
  commitment renders `none`, as a run with no journal line does. Observed by AC4 and AC6.
- **S5** Verify. In its verify form, `measure_commitment(model, journal_root, first=, count=)` picks
  the model's lines at or after `first`, and with them every owner-causable line before it. It sorts
  them by time, takes the first `count`, and recomputes `first` and `last` by S4's rule. At render every
  picked line earlier than `first` is owner-causable by construction, so an unchanged journal
  reproduces all four fields. A line appended after the render still falls past the count, and an edit
  or a deletion still changes the hash. `check_commitment` is otherwise unchanged. Observed by AC5.

## 3. Non-goals (OUT)

- Holding rows. `TOOL-dLoggedFlight-15` owns it.
- Moving the model's window, the other reading of M2. It would drop a NONE gate line from the timeline
  and the commitment, losing a Bash-tool timeout's evidence where no owner acted. It would also class
  the interrupt `post-close` under `TOOL-dLoggedFlight-8` S9, miscounting a turn the record keeps as a
  count.
- The class gate over every time the record carries. `TOOL-dLoggedFlight-19` owns it.
- Coarsening the commitment's times to a minute or an hour. A coarse clock time is still a clock time
  for an interrupt 10 ms before the line.
- The commitment's template, `TOOL-dLoggedFlight-9` S5's. Its four fields stay as they are, and only
  which lines supply `first` and `last` changes.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-8` — `derive_window`'s end sources and the model's window,
  which gains `shown_end` and keeps its bounding rule.
- **consumes-from** `TOOL-dLoggedFlight-9` — `build_summary_facts`, `measure_commitment` and
  `check_commitment`, whose window fact and commitment times change and whose template does not.
- **consumes-from** `TOOL-dLoggedFlight-15` — `OWNER_ACT_BAND_S` and the owner turns the rendered end
  is held against.
- **hands-off** `TOOL-dLoggedFlight-19` — the derived slots, the window's end and the commitment's first
  and last, which the class gate classifies.

## 4. Design

Both derived times rendered a held line's time, and unit 15's rule on rows could not reach them. The
fix answers one question two ways, because the two consumers know different things.

The model knows the owner turns by the time it renders, so the window's rendered end sets a line aside
by the same band unit 15 holds rows by. A NONE gate line that no owner caused, a Bash-tool timeout
say, still ends the window it ends today. That keeps the rendered end at or after every row the record
shows, since a row that is not held is never set aside.

`verify` knows no owner turn, since it rebuilds the model from journals alone. So the commitment's
times skip owner-causable lines by kind, whatever their distance from a turn. The two times are
integrity anchors, not evidence, and skipping a line that no owner caused loses nothing a reader
needs. The hash still covers that line.

The commitment keeps `first` as its verify floor. S5 admits the owner-causable lines before it, the
one population S4 lets precede the floor, so the floor and the skip cannot disagree.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `check_owner_causable` | function | `py.function`, led by `check` |
| `shown_end` | model window key | `window` |

### Files touched (estimate)

`tools/runlog/{model.py,record.py,selftest.py,README.md}` and `memory/map/features/runlog.md`.

### Alternatives rejected

- Move the model's window by skipping owner-causable lines in `derive_window`: rejected in §3, the M2
  reading that loses evidence and misplaces a count.
- Skip every owner-causable line from the rendered end by kind, as the commitment does: rejected, since
  a NONE gate row no owner caused is rendered, and it would then lie after the window's rendered end.
- Hold the commitment's times by band: rejected, since `verify` holds no owner turn and could not
  reproduce them, so every such record would read `mismatch`.
- Drop `first` and `last` from the commitment: rejected, since it changes a closed unit's schema
  template for no gain over S4, and `first` is the verify floor.

## 5. Production-readiness checklist

- security — closes the commitment and window-end paths by which an interrupt's time reached a public
  record.
- perf / scale — one pass over the end sources and one over the picked lines; no git call.
- error / empty / loading states — no owner turn known, so `shown_end` equals `end`; every picked line
  owner-causable, so the commitment is `none`.
- observability — the model JSON carries `end` and `shown_end` side by side, so a difference is
  readable locally.
- risks — a record's rendered end can precede a held line's time by design; a commitment on a run
  whose every line is owner-causable carries no integrity anchor.
- testing — each AC staged RED against unchanged code; renders use the commitment `measure_commitment`
  makes, the production shape.
- migration — none; no run record is committed in this tree.
- user docs — the kit README's record and verify sections.

## 6. Acceptance criteria

- **AC1** — When `check_owner_causable` is handed a driver `end` and a pushes `end` reading
  `exit=unclean`, a gates line reading `verdict=NONE`, and their neighbours reading `exit=clean`,
  `verdict=GREEN`, `verdict=RED` and `verdict=REFUSED`, plus a `start` line, it answers True for the
  first three only.
  Red when: any neighbour answers True, or any of the first three answers False.
- **AC2** — When a non-terminal fixture run's last event is a `verdict=NONE` gate line 10 ms after an
  interrupt owner turn, `window["shown_end"]` equals exactly one second after the latest earlier event
  that is not set aside, and the rendered `window` and `duration` facts read it. The same holds with an
  unclean END as the last event, where the killed verb's START is among the candidates.
  Red when: `shown_end` or either rendered fact lies within `OWNER_ACT_BAND_S` of the turn; staged RED
  against unchanged code, where both read the held line's second plus one.
  figure: DERIVED — the expected end is computed from the fixture's own event times.
- **AC3** — In AC2's fixture, `window["end"]` equals what unchanged code derives, the NONE gate line
  stays in the timeline and in `journal_lines["gates"]`, and `build_owner_positions` classes the
  interrupt `in-window`. With no owner turn within `OWNER_ACT_BAND_S` of the NONE gate line, the
  Bash-tool timeout shape, `shown_end` equals `end`.
  Red when: the model's end moves, the gate line leaves a bounded set, the interrupt classes
  `post-close`, or the timeout shape's `shown_end` differs from `end`.
- **AC4** — When `render_record` renders AC2's fixture with the commitment `measure_commitment` makes
  from its journals, once with the held line in the turn's second and once across a second boundary,
  it refuses nothing, and neither the commitment's `first` nor its `last` lies within
  `OWNER_ACT_BAND_S` of the turn.
  Red when: the render is refused, or either time lies within the band; staged RED against unchanged
  code.
- **AC5** — When `runlog.py verify` checks the record AC4 writes, it reports `match`. After a line is
  appended to the gates journal it still reports `match`, and after the NONE gate line's bytes are
  edited it reports `mismatch`. A fixture whose earliest journal line is an owner-causable gates line
  reports `match`.
  Red when: an unchanged or appended journal reports `mismatch`, or the edited one reports `match`.
  fixture: the earliest-line case needs a run whose first line comes from a held tree before its
  driver START; the tree holds no such fixture today, and the arm builds one.
- **AC6** — When every line `measure_commitment` picks for a fixture run is owner-causable, the rendered
  `commitment` fact reads `none`.
  Red when: it renders a time.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each AC staged RED on its fixture · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from H1 and H2 of the spec audit of units 14 and 15,
  round 1, at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-15` S3, and answers that audit's
  M2 in S3 and its M1 in AC2.

## 10. Reuse audit

The seams are `derive_window` and `build_run_model`'s end sources in `tools/runlog/model.py`, and
`measure_commitment`, `check_commitment` and `build_summary_facts` in `tools/runlog/record.py`, all
this build's. `tools/codebase-map/reuse_lookup.py "the time the commitment and window end take from
journal lines"` returned `measure_commitment`, `check_commitment` and `check_in_window`, which this
unit extends, and `read_journal` and `parse_line` as seams it reads through. No candidate classes a
journal line by what caused it.

Recall terms used: owner turn idle gap held near_owner refusal commitment verify window end stale extract coverage transcripts
