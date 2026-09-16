# TOOL-dLoggedFlight-27 — the Timeline's `withheld rows` fact counts each retired kind from a declared source, and renders `-` for a source the model did not read

**Status:** SPECCED · rev-1 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-25 TOOL-dLoggedFlight-26 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-22` at rev-2 retires eight Timeline row kinds and adds a `withheld rows` fact that
renders each retired kind followed by its count. The spec audit of units 21 to 24, round 1, confirmed
two defects in that fact.

H4, a HIGH. The fact renders a count whether or not the kind's source was read, and unit 22's §5 says a
run with no retired events renders every count `0`. `TOOL-dLoggedFlight-9` S4 at rev-7 ruled that an
UNKNOWN value is absent, never the value that reads clean, and the renderer implements that ruling for
the transcript counts through `COUNTED_STATES` (`tools/runlog/record.py:109`, the test at `:627-635`).
The retired kinds come from sources whose coverage can read unknown. `compact`, `limit` and `workflow`
enter only from transcript extracts (`tools/runlog/model.py:1663-1669`). `idle` exists only when idle
gaps were judged, which needs the transcripts `present` (`model.py:1682`, `:1690`). `gate`, `push` and
`push-refused` come from their journals, and `verb` from the driver journal. So a run whose transcripts
read `not-local`, or whose gates journal is dead, would commit `0` for kinds nobody counted.

H2, a HIGH. Unit 22 AC1 requires a count of 1 for each retired kind over `build_class_model`, which
starts from the landed fixture's real model (`tools/runlog/selftest.py:4251-4253`). That model already
holds the fixture's driver verbs, gate lines and landing push before anything is appended, so AC1
cannot pass, and it states the number with no `figure:` sub-field.

This unit owns the fact. Each count declares the source it is counted from, a count whose source was not
read renders `-`, and every expected count is derived from the model the arm renders.

Every code line cited here was read at `f7bf9d2f` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The fact. The Timeline gains `withheld rows`, whose template reads each member of
  `RETIRED_EVENTS` in that constant's order, each followed by `{int}`. A kind's count is the number of
  events of that kind on the model's timeline, which the model has already bounded to the run's window.
  This takes `TOOL-dLoggedFlight-22` rev-2 S1's fact clause; that unit keeps the retirement and the
  dropping of retired events before rows are built. Observed by AC1.
- **S2** The declaration. `RECORD_SCHEMA["count_sources"]` maps each `{int}` slot of six facts to the
  source it is counted from, keyed by section, label and position:
  - `withheld rows`: `transcripts` for `compact`, `limit` and `workflow`; `driver` for `verb`; `gates`
    for `gate`; `pushes` for `push` and `push-refused`; and `idle` for `idle`;
  - the Summary's `owner turns`, `usage main`, `usage agent`, `usage workflow` and `attributed calls`:
    `transcripts` for every slot.

  `idle` names the Coverage `idle` entry's judgement rather than a coverage state. Observed by AC2 and AC4.
- **S3** The rule. A declared slot renders `-` unless its source's coverage state is in
  `COUNTED_STATES`, or, for `idle`, unless idle gaps were judged. `build_summary_facts`' `known` test
  (`tools/runlog/record.py:632-635`) is replaced by that lookup, so the five Summary facts keep their
  present behaviour and the rule is stated once. Observed by AC2 and AC3.
- **S4** The declaration check. `check_count_sources(schema)` refuses, naming the slot, an entry keyed
  to no `{int}` slot of a fact, a source that is neither in `SOURCE_NAMES` nor `idle`, and an `{int}` slot
  of the six facts with no entry. A kind added to `RETIRED_EVENTS` therefore adds a slot that refuses
  until its source is declared. The self-test arm calls it. Observed by AC4.
- **S5** The expectations. The arm observing S1 renders a copy of `build_class_model`'s model whose
  driver, gates, pushes and transcripts coverage read `present` and whose idle gaps are judged, and
  derives each kind's expected count from that model's timeline at observation time, never a typed
  number. This replaces unit 22 rev-2 AC1's count of 1. Observed by AC1.
- **S6** The model-fields arm. `test_record_model_fields` reads its workflow run in `withheld rows`,
  expecting the model's `workflow` event count where that model's transcripts read a counted state and
  `-` otherwise, read from the model. Unit 22 retires that arm's rendered workflow row. Observed by AC5.
- **S7** The docs. The kit README's paragraph on unknown values names `count_sources` and the
  `withheld rows` fact, and `memory/map/features/runlog.md` claims `check_count_sources`. NOT OBSERVED:
  prose, and the map's coverage leg grades the claim at the close.

## 3. Non-goals (OUT)

- Which kinds retire, and dropping their rows. `TOOL-dLoggedFlight-22` owns both.
- Declaring a source for every count the record renders. Counts read from git, the run-state file or
  the build folder, such as `own commits` and `units served`, carry no `-` rule today, and declaring
  them changes readers this unit does not inventory. The arm's header states that an undeclared count
  outside the six facts is not graded.
- The time slots and their sources. `TOOL-dLoggedFlight-20` owns them.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-16` — `COUNTED_STATES` as that unit leaves it, with `stale`
  outside it, which S3 reads unchanged.
- **consumes-from** `TOOL-dLoggedFlight-26` — `build_class_model` with its intruders on kept kinds, over
  which S5 derives the counts.
- **consumes-from** `TOOL-dLoggedFlight-22` — `RETIRED_EVENTS`, the retired kinds dropped before rows
  are built, and its S1 fact clause, which moved here.

## 4. Design

The fact exists to say what happened per kind in place of the rows. A count from a source nobody read
says something that did not happen, so the fact carries the same unknown rule as every other count from
those sources, and the rule reads a declaration rather than being restated per fact.

The five Summary facts move onto the declaration too. They already render `-` by one hand-written test,
and a second hand-written test for a second fact is how the rule would drift between them.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `count_sources` | schema key | `RECORD_SCHEMA` |
| `check_count_sources` | function | `py.function`, led by `check` |
| `withheld rows` | Timeline fact label | `RECORD_SCHEMA` fact template |

### Files touched (estimate)

`tools/runlog/{record.py,selftest.py,README.md}` and `memory/map/features/runlog.md`, with the
regenerated map.

### Alternatives rejected

- Render every count, reading `0` as unread: rejected by `TOOL-dLoggedFlight-9` S4 at rev-7.
- Retire the `withheld rows` fact: rejected by M3's rule, since the fact is what a reader keeps of the
  retired rows.
- A per-fact `known` test beside the existing one: rejected, since two hand-written tests of one rule
  is the drift S3 removes.
- Strip the base model's retired events so each count is 1, the audit's second route for H2: rejected,
  since `build_class_model` has other readers, and a derived count needs no edit to them.

## 5. Production-readiness checklist

- security — no new value reaches the record; a count is an integer or `-`.
- perf / scale — one lookup per declared slot; one count per retired kind.
- error / empty / loading states — a run with no retired events renders `0` only for a kind whose
  source was read, and `-` otherwise.
- observability — `withheld rows` beside the Coverage table says both what happened and what was read.
- risks — a new count fact outside the six is not graded, as §3 states.
- testing — each AC staged RED on a renderer copy or a schema copy.
- migration — no run record is committed in this tree.
- user docs — the kit README's paragraph on unknown values.

## 6. Acceptance criteria

- **AC1** — When `render_record` renders S5's copy of `build_class_model`'s model, the `withheld rows`
  fact lists every member of `RETIRED_EVENTS` in order, each followed by the number of that kind's
  events on the rendered model's timeline.
  Red when: a member is missing, out of order, or its count differs, or the arm types a count.
  figure: DERIVED — each count is read from the model's timeline at observation time.
- **AC2** — When `render_record` renders a copy of that model whose transcripts read `not-local`, whose
  gates journal reads `dead`, whose pushes journal reads `absent` and whose idle gaps are not judged,
  `withheld rows` reads `-` for `compact`, `limit`, `workflow`, `idle`, `gate`, `push` and `push-refused`,
  and a count for `verb` while the driver reads `partial`. With the driver `absent` too, `verb` reads
  `-`, and every slot of the five Summary facts reads `-`.
  Red when: a digit renders for a slot whose declared source was not read, or `verb` reads `-` while
  the driver is `partial`. Staged RED by a renderer copy that ignores `count_sources` for `gate`.
- **AC3** — When `git show HEAD -- tools/runlog/selftest.py` is read at this unit's build commit, no
  count assertion of `test_record_ac10_unknown_counts` is in its hunks, and that arm's `not-local` model
  renders the five Summary facts as it expects.
  Red when: one of its count assertions is edited, or a Summary fact renders differently on that model.
- **AC4** — When `check_count_sources` reads `RECORD_SCHEMA`, it refuses nothing. On a copy without the
  `gate` entry, a copy naming the source `ledger`, a copy with an entry keyed to no slot, and a copy
  whose `RETIRED_EVENTS` gains a member, it refuses naming that slot.
  Red when: any staged copy passes.
- **AC5** — When `test_record_model_fields` renders its model, `withheld rows` reads that model's
  `workflow` event count where its transcripts read a state in `COUNTED_STATES`, and `-` otherwise.
  Red when: the value differs from the one read from the model, or the arm types it.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC2's renderer copy ignoring `gate`'s entry and AC4's four schema copies · floor raised by the arm count

## 8. Open questions

- **F1** Where is the unknown rule for the new counts stated? Options: a per-kind test inside the fact's
  renderer; a declared source per count slot read by one lookup; retire the fact. RESOLVED (agent,
  2026-09-16, delegated): a declared source per slot, the audit's left-shift for H4, covering the five
  Summary facts that already carry the rule, since one declaration cannot disagree with itself.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from H4 and H2 of the spec audit of units 21 to 24,
  round 1, at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-22` rev-2 S1's `withheld rows` clause,
  its AC1 count and its §5 empty-state line.

## 10. Reuse audit

The seams are `COUNTED_STATES` and `build_summary_facts` in `tools/runlog/record.py`, the model's
coverage block in `tools/runlog/model.py`, and `build_class_model` in `tools/runlog/selftest.py`, all
this build's. `tools/codebase-map/reuse_lookup.py "an unknown count renders absent when its source was
not read"` returned name-stem candidates only, `render_record` and `read_journal` among them, and no
seam declares a source per count, so S2 extends `COUNTED_STATES`' existing use rather than a new seam.
The recall query returned M6 of the first closing diff review, which set the rule for the transcript
counts, `TOOL-dLoggedFlight-9` S4's ruling, and this audit's H4.

Recall terms used: unknown count COUNTED_STATES coverage not-local dead journal withheld rows reads clean zero transcripts
