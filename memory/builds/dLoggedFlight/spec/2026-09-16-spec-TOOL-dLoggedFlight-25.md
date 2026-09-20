# TOOL-dLoggedFlight-25 — the Summary window's closer names a terminal write its own commit carries, observed over real models at each of the Skill's render placements

**Status:** SPECCED · rev-2 · 2026-09-20 · node d · Tier-2 · base 4cf0944d · streams tooling · order 23

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 TOOL-dLoggedFlight-24 TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27 TOOL-dLoggedFlight-28 TOOL-dLoggedFlight-29 TOOL-dLoggedFlight-30 |
| [2026-09-20-review-TOOL-dLoggedFlight-25-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-dLoggedFlight-25-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-26 TOOL-dLoggedFlight-27 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 21 to 24, round 1, confirmed two defects in how the rendered window behaves
across the moments a record is rendered.

B1, a BLOCKER. The `opened-by` and `closed-by` vocabularies are observed today by one loop in
`test_record_ac4_classes` (`tools/runlog/selftest.py:4335-4339`). It re-renders
`dict(m, window=dict(m["window"], ...))` and asserts that `git`, `terminal-write` and `last-activity`
each reach the file. `TOOL-dLoggedFlight-24` S3 renders both facts from `record_window`, so that edit
stops reaching the render, and the `last-activity` check reds. `TOOL-dLoggedFlight-22` then derives its
vocabulary list from the whole schema, and one record carries one closer.

H3, a HIGH. The model reads `terminal` from the working-tree run-state file
(`tools/runlog/model.py:1432-1438`), while `record_window` reads committed record commits. The unattended
Skill renders the record before it commits the run-state write the verb just staged, at all three
placements (`tools/unattended/SKILL.template.md:840-849`). So the record committed at `--landed` or
`--abort` reads `terminal: yes` beside `window closed by: last-activity`, with its closing bound at the
last record commit before the terminal write. No criterion of unit 24 observes that branch, and its S4
claim that a re-render reproduces the window is false for exactly the record the process commits.

This unit names the pending terminal write in the closer, and observes the window's provenance, bounds
and stability over real models built at each placement, in place of a loop that edits a model field.

Every code line cited here was read at `f7bf9d2f` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The closer. `derive_window_closer(window, terminal)` in `tools/runlog/record.py` returns
  `terminal-pending` when `terminal` is true and the window's `end_from` is `last-activity`, the
  window's `end_from` otherwise, and None for no window. `build_summary_facts`
  (`tools/runlog/record.py:644-645`) renders `window opened by` from `record_window["start_from"]` and
  `window closed by` from `derive_window_closer(record_window, m["terminal"])`. In `RECORD_SCHEMA`
  (`tools/runlog/record.py:156-157`) `opened-by` becomes `git` alone and `closed-by` becomes
  `terminal-write`, `terminal-pending` and `last-activity`. `derive_window`, the model's `window` and
  the schema leg's window are unchanged. This takes `TOOL-dLoggedFlight-24` S3. Observed by AC1, AC2
  and AC5.
- **S2** The placement models. `build_placement_models` in `tools/runlog/selftest.py` builds three
  models through `build_run_model` from the history `build_landed_fixture` makes
  (`tools/runlog/selftest.py:2173-2216`), never by editing a model field:
  - `landed`, the fixture as built, its LANDED write committed at minute 28;
  - `landing`, the history cut before that commit, with the run-state file at LANDING in the working tree;
  - `pending`, the same cut with the LANDED run-state write staged and not committed, which is the
    state the `--landed` and `--abort` placements render in.

  Each model reads the fixture's own journal lines up to the verb that produced its state: `landing`
  stops before the `--landed` lines, and `pending` and `landed` hold them. Observed by AC1 for every
  rendered value. The CONSTRUCTION discipline — built from a history, never by editing a model field
  — is observed by `TOOL-dLoggedFlight-29`, which returns each model beside the repository state it
  was built from and re-derives it; no criterion here can see the difference, which is H1 of the spec
  audit of units 25 to 27.
- **S3** Bounds and stability at each placement. This takes `TOOL-dLoggedFlight-24` S4 and restates it
  per placement. On `landed` the rendered closing bound is the LANDED commit's committer time. On
  `landing` and `pending` it is the committer time of the last record commit before that write. On
  each, `duration` is the closing bound less the start. A later commit of another path, naming no unit,
  leaves the `window`, `duration` and `window closed by` facts byte-identical; on `pending` that commit
  carries only its own path, and the staged write stays staged. On `landed`, a later commit naming a unit
  id on the default branch leaves them byte-identical too, since the rendered window reads no commit
  but the run's start and its record commits. The lag is declared, not hidden: a record
  rendered at a terminal placement names its closer `terminal-pending`, and a re-render once the write
  is committed reads `terminal-write` with the write's time. Observed by AC1 and AC3.
- **S4** The retired loop. The `dict(m, window=...)` loop of `test_record_ac4_classes` is removed, and
  the three renders of S2 observe every member of `opened-by` and `closed-by` in its place. A probe for
  `dict(m, ` over `tools/runlog/selftest.py` at `f7bf9d2f` finds that loop as the only such re-render,
  so no other arm edits a field the render stopped reading. `ASSERTION_FLOOR` moves by the arms S5 and
  AC1 to AC5 add, less the loop's three assertions, with a comment naming this unit. Observed by AC2.
- **S5** The placement replay. `test_record_placement_replay` replays the Skill's order on the landed
  fixture's history, twice. At the close placement it stages the LANDING write, renders, commits,
  and re-renders. At the `--landed` placement it does the same with the LANDED write. It compares each
  render with its re-render through `parse_record`, fact by fact and table by table. Every item that
  differs must be a member of `PLACEMENT_LAG`, a constant in `tools/runlog/selftest.py` whose members
  each carry the reason the commit moves them. The Summary `window`, `duration` and `window closed by`
  facts are members. `terminal`, `phase`, every other Summary fact, and every Units, Decisions,
  Conformance and Anomalies item may never be. Observed by AC4.
- **S6** The docs. The kit README's Summary section states the three closers and the lag S3 declares,
  and the runlog dossier's PROSE names `derive_window_closer`. A dossier cannot CLAIM a Python
  symbol: its `[claims]` block carries no symbol tier, the symbol tier feeds the recall corpus and
  never the ratchet (`tools/codebase-map/map_extractors.py:128`), and `[paths] globs` already covers
  `tools/runlog/**`. NOT OBSERVED: prose. What the `codebase-map coverage + freshness` leg grades at
  the close is that the regenerated map artifacts are committed in the same commit, which is a
  different assertion and is worth stating as itself.

## 3. Non-goals (OUT)

- `derive_window`, the model's `window` and `check_run_states`. The pending state is a fact about when
  a render runs, not about the run, so neither the local model nor the leg changes.
- The rendered bounds, `record_window` and `derive_window_bounds`, which `TOOL-dLoggedFlight-24` S1
  and S2 keep.
- The Skill's placements. They stay where `tools/unattended/SKILL.template.md:840-849` puts them.
- Timeline rows the committed write adds. They are graded only as members of `PLACEMENT_LAG`.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-24` — `record_window` and `derive_window_bounds`, and its S3
  and S4, which moved here.
- **hands-off** `TOOL-dLoggedFlight-26` — the rest of `test_record_ac4_classes`, whose literals that
  unit derives after this unit removes the loop.
- **hands-off** `TOOL-dLoggedFlight-22` — `build_placement_models`, over whose renders that unit's
  derived vocabulary list reaches the fact-only closers.
- **hands-off** `TOOL-dLoggedFlight-23` — the `window`, `duration` and `window closed by` facts at
  each placement, whose time tokens the population arm grades.
- **hands-off** `TOOL-dLoggedFlight-29` — `build_placement_models` and its three placement states,
  which that unit returns beside each model and re-derives, so S2's construction discipline stops
  being a claim only prose makes.

## 4. Design

The closer is derived at render time because only the renderer holds both halves: the working-tree
phase and the committed history. A record cannot carry its own commit's time, so at a terminal
placement the honest window is the committed one, and the closer says which write is still to land.

A field-editing re-render is how B1 went unseen: the edit kept passing while the render stopped
reading the field. Real models built from a history cannot drift that way, and the three placement
states are the only states a committed record is rendered in.

The replay arm gates the class H3 names, a render reading committed history ahead of the commit it
rides. It grades what differs against a declared set rather than what matches, so a new git-derived
slot that lags reds until it is declared with its reason.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `derive_window_closer` | function | `py.function`, led by `derive` |
| `build_placement_models` | function | `py.function`, led by `build` |
| `test_record_placement_replay` | function | `py.function`, led by `test` |
| `test_record_placement_windows` | function | `py.function`, led by `test` |
| `PLACEMENT_LAG` | constant | `py.constant` |
| `terminal-pending` | `closed-by` vocabulary member | `RECORD_SCHEMA` |

### Files touched (estimate)

`tools/runlog/{record.py,selftest.py,README.md}` and `memory/map/features/runlog.md`, with the
regenerated map.

### Alternatives rejected

- Render the closing bound, `duration` and closer as `-` while the terminal write is pending:
  rejected by M3's rule, since every landed and aborted record would carry no closing time at all.
- Keep `last-activity` and state the one-commit lag: rejected by M3's rule, since `last-activity`
  beside `terminal: yes` reads as a run that stopped by inactivity.
- Add a `terminal-pending` branch to `derive_window`: rejected, since `model.py:1553-1556` and the model
  arms read its `end_from`, and the leg's window must stay the one the model derives.
- Render into a second commit after the terminal write: rejected by M3's first veto, since
  `TOOL-dLoggedFlight-11` S2, observed by its AC2, places each render in a commit the run already makes.
- Keep the loop and make it edit `record_window`: rejected, since an edited field is the shape B1 found.

## 5. Production-readiness checklist

- security — no new value reaches the record; `terminal-pending` is a closed vocabulary member.
- perf / scale — one comparison at render time; the arms build three fixture models and one replay.
- error / empty / loading states — a model with no `record_window` renders both provenance facts `-`.
- observability — the closer tells a reader whether the closing bound is final.
- risks — a git-derived slot that lags and is added to `PLACEMENT_LAG` without a true reason; S5 names
  the facts that may never be members.
- testing — each AC staged RED on a renderer copy or on the fixture history.
- migration — no run record is committed in this tree; the vocabularies change before any is.
- user docs — the kit README's Summary section.

## 6. Acceptance criteria

- **AC1** — When `test_record_placement_windows` renders each model `build_placement_models` returns,
  `window opened by` reads `git` in all three, and `window closed by` reads `terminal-write` on
  `landed`, `last-activity` on `landing` and `terminal-pending` on `pending`. The closing bound is the
  committer time S3 names for that model, and `duration` is it less the start.
  Red when: any value differs. Staged RED twice: a renderer copy that renders `record_window["end_from"]`
  unmapped, so `pending` reads `last-activity`, and a copy that prints the half-open end.
  figure: DERIVED — every committer time is read from the fixture repository at observation time.
- **AC2** — When `RECORD_SCHEMA` is read, `opened-by` holds `git` alone and `closed-by` holds
  `terminal-write`, `terminal-pending` and `last-activity`, and the three renders of AC1 carry every
  member between them. `git grep -n 'window=dict(m\["window"\]' -- tools/runlog/selftest.py` finds
  nothing. `ASSERTION_FLOOR`'s newest comment names this unit and its arithmetic reaches the value
  declared beside it, which is what `TOOL-dLoggedFlight-22` AC5 already states for the same constant.
  Red when: `driver` or `terminal-end` is a member, a member reaches none of the three renders, the
  loop is still defined, or the floor moves with no comment naming this unit or with arithmetic that
  does not reach its value.
- **AC3** — When a commit of another path naming no unit lands after each placement model's fixture
  state, and `render_record` re-renders the rebuilt model, the `window`, `duration` and
  `window closed by` facts are byte-identical to the first render. On `landed`, a commit naming a unit
  id on the default branch past the terminal write leaves them byte-identical too.
  Red when: any of them moves. Staged RED against a renderer copy that bounds the window by the era's
  last commit, with that commit in the fixture.
- **AC4** — When `test_record_placement_replay` replays the close and the `--landed` placements, every
  fact or table that differs between a render and its re-render is a member of `PLACEMENT_LAG`, and at
  the `--landed` placement `window closed by` moves from `terminal-pending` to `terminal-write`.
  `PLACEMENT_LAG`'s membership is pinned in BOTH directions: it holds exactly the three Summary facts
  S5 names, `window`, `duration` and `window closed by`, and no fourth member — so the declared set
  cannot widen silently, which is the risk §5 names and the both-directions rule charter §7 applies
  to every declared population.
  Red when: a non-member differs, the closer does not move, `terminal` or `phase` is a member, or
  `PLACEMENT_LAG` holds any member outside S5's three. Staged RED twice: a renderer copy whose
  `terminal` fact reads the phase of the last committed record commit, which reds naming `terminal`,
  and a copy of the constant that declares a Units item a member, which reds on the membership pin
  while the replay itself stays green.
- **AC5** — When `render_record` renders a model that carries no `record_window`, `window opened by`
  and `window closed by` read `-`.
  Red when: either renders a vocabulary member.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC1's two renderer copies, AC3's era-bounded copy and AC4's committed-phase copy · floor moved by S4

## 8. Open questions

- **F1** How does a record rendered at a terminal placement name its window's close, which is H3?
  Options: render the closing bound and closer `-`; keep `last-activity` and state the lag; a closer
  of its own for the pending write; a second commit after the terminal write. RESOLVED (agent,
  2026-09-16, delegated): the `terminal-pending` closer, by M3's feature-rich rule. §4 records why the
  others lost.
- **F2** How are the fact-only vocabularies observed once no loop edits the window, which is B1?
  Options: renders of real models at each placement; an edited `record_window`; a typed exclusion in
  `TOOL-dLoggedFlight-22`'s derived list. RESOLVED (agent, 2026-09-16, delegated): real models at each
  placement, which unit 22 unions over, since the other two are the shapes B1 and unit 22 AC4 refuse.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from B1 and H3 of the spec audit of units 21 to 24,
  round 1, at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-24` rev-1 S3 and S4 with its AC2 and
  AC3.
- rev-2 · 2026-09-20 · S2 · S6 · AC2 · AC4 · §3 · the disposal of the spec audit of units 25 to 27,
  round 1. Promoted elsewhere: H1 to `TOOL-dLoggedFlight-29`, which returns each placement model
  beside the state it was built from, so S2 now names that unit for the construction discipline and
  §3 declares the handoff. Folded: M1, AC4 pins `PLACEMENT_LAG`'s membership in both directions with
  a staged Units-item member; M4, S6 stops saying a dossier CLAIMS a Python symbol and states what
  the map leg actually grades; L1, AC2 reads `ASSERTION_FLOOR`'s comment and arithmetic the way
  `TOOL-dLoggedFlight-22` AC5 does for the same constant.

## 10. Reuse audit

The seams are `build_summary_facts` and `RECORD_SCHEMA` in `tools/runlog/record.py`, `build_run_model`
in `tools/runlog/model.py`, `parse_record` in `tools/runlog/record.py`, and `build_landed_fixture` in
`tools/runlog/selftest.py`, all this build's. `tools/codebase-map/reuse_lookup.py "a render placed before the commit
it rides reads committed history"` returned `render_record` and `measure_commitment` among name-stem
candidates, and no seam compares a render with its re-render, so no existing seam fits the replay.
The recall query returned the audit's H3 and `TOOL-aBoundedCeiling-9`, an open backlog row naming the
same shape for the landing record and the kit gate: the record a commit carries is written after the
check that would grade it.

Recall terms used: window closed-by terminal-write last-activity placement render record commit staged LANDED abort schema leg
