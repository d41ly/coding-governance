# TOOL-dLoggedFlight-24 — the Summary window and its duration render the git-only window the schema leg derives

**Status:** SPECCED · rev-2 · 2026-09-16 · node d · Tier-2 · base 4cf0944d · streams tooling · order 22

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md](../prompts/2026-09-16-prompt-TOOL-dLoggedFlight-14-1-build-brief.md) | journal | TOOL-dLoggedFlight-14 TOOL-dLoggedFlight-16 TOOL-dLoggedFlight-20 TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 |
| [2026-09-16-review-TOOL-dLoggedFlight-21-spec-audit-round1.md](../reviews/2026-09-16-review-TOOL-dLoggedFlight-21-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-21 TOOL-dLoggedFlight-22 TOOL-dLoggedFlight-23 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-dLoggedFlight-20` at rev-1 took the Summary window from "its first and last commits in the
run's era". The era does not bound the run. `derive_run_eras` leaves `t1` None for a build's last run
(`tools/runlog/model.py:349-357`), so its era is open to HEAD, and `era_commits` holds every
descendant of the start commit on the run branch and the default branch (`model.py:1374-1375`). A
git-only window already exists: `check_run_states` derives each run's window with
`derive_window(float(run["t"]), "git", phases, terminal)` over `derive_record_commits`
(`tools/runlog/record.py:1412-1423`), which is shared so the model and the leg "cannot bound a run's
writes differently" (`model.py:393-399`). The spec audit of units 14, 16 and 20, round 1, confirmed
this as H3, a HIGH, and the loop promoted it here.

The same audit's M1, a MEDIUM, found `window opened by` and `window closed by` still rendered from the
model's journal-bounded window (`record.py:644-645`), so a commit-derived window would sit beside a
provenance fact naming a journal close. Those facts describe this unit's window, so M1 was folded here
and decided against this unit's derivation, as the audit asked.

The spec audit of units 21 to 24, round 1, then found the provenance loop B1 names and the unobserved
closer at the Skill's render placements H3 names. Both were promoted to `TOOL-dLoggedFlight-25`, which
takes S3 and S4 with AC2 and AC3. This unit keeps the field and the rendered bounds.

Every code line cited here was read at `ba3bd9fd` on the run branch. The `base` above is the
default-branch sha the format asks for, and `tools/runlog` does not exist there yet.

## 2. Scope (IN)

- **S1** The model field. `build_run_model` records `record_window`, the value of
  `derive_window(float(pick["t"]), "git", phases_at, terminal)` with no `term_end` and no
  `last_event`. That is the call `check_run_states` makes, over the `phases_at` the model already reads
  through `derive_record_commits` (`model.py:1437`). `RunModel` gains the field. The model's `window` is
  unchanged, and it still bounds every timed set. Observed by AC1.
- **S2** The rendered bounds. `derive_window_bounds(window)` in `record.py` returns the window's start
  and its closing time. The closing time is `end` when `end_from` is `terminal-write`, and `end` less
  the one second the half-open window adds when it is `last-activity`. Each bound is therefore a
  commit's committer time: the start commit's, the first terminal write's, or the last record commit's.
  `build_summary_facts` (`record.py:618-646`) renders the `window` fact from those two bounds and the
  `duration` fact as the closing time less the start. A model with no `record_window` renders both
  facts as `-`. Observed by AC1 and AC4.
- **S3** Moved to `TOOL-dLoggedFlight-25` S1, which renders both provenance facts from `record_window`
  and adds the `terminal-pending` closer. NOT OBSERVED here: that unit's AC1, AC2 and AC5 observe it.
- **S4** Moved to `TOOL-dLoggedFlight-25` S3, which states the window's stability at each of the Skill's
  render placements. NOT OBSERVED here: that unit's AC1 and AC3 observe it.

## 3. Non-goals (OUT)

- The model's `window`. It keeps its journal bounds for the local model and bounds every timed set, by
  `TOOL-dLoggedFlight-8` S2.
- Which Timeline rows render. They stay bounded by the model's window, so a kept row can lie between
  the run's terminal END and its terminal write. The rendered window is a git bound, not a row bound,
  and every time either one shows is public.
- The schema leg's refusals, `TOOL-dLoggedFlight-10` S6's, which read the same derivation unchanged.
- The commitment, `TOOL-dLoggedFlight-21`'s, and every other time slot, which `TOOL-dLoggedFlight-20`,
  `-22` and `-23` own.
- The provenance facts and the window's stability at each render placement, which
  `TOOL-dLoggedFlight-25` owns.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-8` — `derive_window`, `derive_record_commits` and `RunModel`,
  which gains `record_window`.
- **consumes-from** `TOOL-dLoggedFlight-9` — `build_summary_facts`, whose `window` and `duration`
  facts S2 renders.
- **consumes-from** `TOOL-dLoggedFlight-10` — `check_run_states`' git-only window, which S1 copies and
  AC1 compares.
- **hands-off** `TOOL-dLoggedFlight-20` — its rev-1 S3 window clause and M1's provenance facts, which
  moved here.
- **hands-off** `TOOL-dLoggedFlight-25` — S3 and S4 with AC2 and AC3: the provenance facts and the
  window's stability, observed over real models at each render placement.
- **hands-off** `TOOL-dLoggedFlight-22` — the Summary window with no journal time, which must land
  before the owner-time refusal retires.
- **hands-off** `TOOL-dLoggedFlight-23` — the `window` and `duration` slots whose tokens the
  population arm holds to commit times.

## 4. Design

The leg's window is the one a fresh clone derives from git alone, so it is the one window already
public. Rendering it removes the era question rather than bounding the era a second way, and the render
and the leg now read one derivation where unit 20 rev-1 would have made three.

The half-open end is a commit time plus one second for `last-activity`, and no public source shows that
value. The render prints the closing commit's own time instead, so every rendered bound is a time
`git log` shows, and `TOOL-dLoggedFlight-23` can hold it to one without a special case.

M1 had two routes: retire both provenance facts, or narrow their vocabularies to what the git-only
window can produce. Under S1 the facts stay true, and a reader keeps which rule closed the window, so
the narrowing is the more feature-rich survivor under M3's rule. `TOOL-dLoggedFlight-25` now carries
that narrowing, with the closer a terminal placement renders.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `record_window` | model field | `RunModel` |
| `derive_window_bounds` | function | `py.function`, led by `derive` |

### Files touched (estimate)

`tools/runlog/{model.py,record.py,selftest.py,README.md}` and `memory/map/features/runlog.md`.

### Alternatives rejected

- The era's first and last commits, `TOOL-dLoggedFlight-20` rev-1 S3: rejected by H3. For a build's
  last run the end moves with every later commit on either branch, which `TOOL-dLoggedFlight-8` S2
  rejected, and it would disagree with the window the leg grades.
- The model's window with each journal bound replaced by the nearest commit: rejected, since it is a
  second derivation, and which commit is nearest is chosen by a journal time.
- Retire `window opened by` and `window closed by` from the committed Summary: rejected by M3's rule,
  as §4 says.
- Render the half-open `end` as the leg holds it: rejected, since a `last-activity` end is no public
  time.

## 5. Production-readiness checklist

- security — the Summary window and duration carry no journal time.
- perf / scale — one more `derive_window` call over data the model already holds; no git call.
- error / empty / loading states — a run whose record commits hold none after its start closes at its
  start, with a duration of `0s`; a model without the field renders `-`.
- observability — the model JSON carries `window` and `record_window` side by side, so the difference is
  readable locally.
- risks — the rendered window can end before a kept Timeline row, as §3 states.
- testing — each AC staged RED on its fixture, the equality arm against the leg's own call.
- migration — no run record is committed in this tree.
- user docs — the kit README's Summary section.

## 6. Acceptance criteria

- **AC1** — When `build_run_model` and `check_run_states` read the same landed fixture, whose HEAD holds
  every record commit, the model's `record_window` equals the leg's window for that run, and
  `render_record` renders the `window` fact as its start and closing time and `duration` as their
  difference.
  Red when: any of the four values differs, or a rendered bound is not the committer time of a fixture
  commit.
  figure: DERIVED — both windows and every commit time are read from the fixture at observation time,
  never typed.
- **AC4** — When `render_record` renders a model that carries no `record_window`, the `window` and
  `duration` facts read `-`.
  Red when: either renders a time.

## 7. Gates

`runlog selftest` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · AC1's equality against the leg's own call, and AC4's model with no `record_window` · floor raised by the arm count

## 8. Open questions

- **F1** Which derivation renders the Summary window? Options: the era's commits; the leg's git-only
  window; the model's window snapped to commits. RESOLVED (agent, 2026-09-16, delegated): the leg's
  git-only window. It is the only one that is a single derivation, public, and stable under later
  commits. §4 records why the others lost.
- **F2** What happens to `window opened by` and `window closed by`, which is M1? Options: retire both;
  narrow their vocabularies. RESOLVED (agent, 2026-09-16, delegated): narrow, by M3's feature-rich rule.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, promoted from H3 of the spec audit of units 14, 16 and 20,
  round 1, at the loop's BOUNDED exit. It takes `TOOL-dLoggedFlight-20` rev-1 S3's window and duration
  clause. It carries that audit's M1, folded here from unit 20 S3 because the two provenance facts
  describe this unit's window.
- rev-2 · 2026-09-16 · S3 · S4 · AC2 · AC3 · §1 · §3 · §4 · §5 · §7 · the disposal of the spec audit of
  units 21 to 24, round 1. B1 (BLOCKER) and H3 (HIGH) were promoted to `TOOL-dLoggedFlight-25`, which
  takes S3 and S4 with AC2 and AC3: the provenance facts render from `record_window` with a
  `terminal-pending` closer, and the window's stability is observed over real models at each of the
  Skill's render placements. The title drops the provenance facts, and §3 gains the reciprocal edge.
  S1, S2, AC1 and AC4 do not change.

## 10. Reuse audit

The seams are `derive_window` and `derive_record_commits` in `tools/runlog/model.py`, and
`check_run_states` and `build_summary_facts` in `tools/runlog/record.py`, all this build's.
`tools/codebase-map/reuse_lookup.py "a run window derived from git commits alone"` returned
`build_run_model` as a seam at fan-in 3, with `derive_run_eras`, `derive_run_starts` and
`measure_commitment` beside it. It did not return `derive_window` or `check_run_states`, which were
found by reading `record.py:1390-1453`, so the probe's miss is recorded rather than trusted. S1 reuses
that call unchanged. The recall query returned this build's own records only, the audit's H3 among
them.

Recall terms used: window era derive_window record commits terminal-write last-activity opened closed git schema leg overlap
