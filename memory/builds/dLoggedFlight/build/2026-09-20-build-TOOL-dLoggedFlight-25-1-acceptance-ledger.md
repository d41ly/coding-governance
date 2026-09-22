# Acceptance ledger — TOOL-dLoggedFlight-25

**Serves:** journal TOOL-dLoggedFlight-25

Tier-2 · node d · 2026-09-20 · the build pass of the window's closer, against spec rev-3. The spec
moved from rev-2 to rev-3 in this pass for ONE divergence, recorded in its section 9: rev-2 had the
replay compare the whole record "fact by fact and table by table", and the close placement's replay
moves one Timeline row, because the commit a render rides is itself a record commit and the widened
window holds it as a phase row. That row is the write rather than a lag, so the compared scope is now
DECLARED — every Summary fact plus the Units, Decisions, Conformance and Anomalies tables — and
section 3 states what is out with the measurement behind it, instead of widening a set AC4 pins at
exactly three members.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13: `tools/runlog/selftest.py`
was not run, imported or copied under any name, and neither was any other suite, gate leg or bar. The
change was observed instead by throwaway Python scripts kept outside the repository. They rebuilt the
landed fixture's history themselves — synthetic commits through `git fast-import`, committer times set
through the environment, no transcript and no store — and called `build_run_model`, `render_record`,
`parse_record`, `measure_commitment` and `derive_window_closer` over it. Every observation below held.
The durable arms are owed to the post-build run, each with the break that stages it RED.

## The criteria

**Evidences:** TOOL-dLoggedFlight-25

- AC1 — `derive_window_closer` — over the three placement models built from one fixture history,
  `window opened by` read `git` in all three, and `window closed by` read `terminal-write` on
  `landed`, `last-activity` on `landing` and `terminal-pending` on `pending`. The rendered closing
  bound was the LANDED commit's committer time on `landed` and the last record commit's on the other
  two, `duration` was that bound less the start in each, and every bound was checked against a time
  `git log --format=%ct` printed off the fixture, never against the model that rendered it. Liveness:
  `landing` and `pending` share both bounds and differ in the closer alone, so the three closers are
  three states of one history and not three fixtures. Both of the spec's staged breaks were reproduced
  on the probe and both fired — a renderer copy returning `record_window["end_from"]` unmapped made
  `pending` read `last-activity`, and one returning the half-open end raw moved the `landing` bound by
  a second. Owed: `test_record_placement_windows`, staged RED by either of those two renderer copies.
  MET at the post-build run: `test_record_placement_windows` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC2 — `RECORD_SCHEMA` — `opened-by` reads `("git",)` and `closed-by` reads
  `("terminal-write", "terminal-pending", "last-activity")`, and the three renders of AC1 carried
  every member of both between them, checked as a set equality rather than a membership test. The
  assembled needle for the retired loop finds nothing in `tools/runlog/selftest.py`; it is assembled
  from four pieces, because written as one literal it would BE the text it exists to prove absent.
  The floor's newest comment block names this unit, its `-> 1389` reaches `ASSERTION_FLOOR`, and its
  own `20 + 8 + 6 - 3 = 31` evaluates to the 31 the raise moves it by. All four readings were run over
  the committed suite source by a probe that reads the file as bytes. Owed:
  `test_record_placement_windows`, staged RED by restoring `driver` or `terminal-end` to a
  vocabulary, by re-adding the loop, or by moving the floor with no comment naming this unit.
  MET at the post-build run: `test_record_placement_windows` is GREEN there too, and the floor it
  reads has since moved past this unit's 1389 to 1543 with the units after it.
- AC3 — `build_run_model` — after a commit of `tools/a.txt` naming no unit landed past each
  placement's fixture state, the rebuilt model re-rendered `window`, `duration` and `window closed by`
  byte-identical on all three; on `pending` that commit carried only its own path and
  `git diff --cached --name-only` still listed the run-state file, so the LANDED write stayed staged.
  A second commit naming a unit id on the default branch, past the terminal write, left the same three
  facts byte-identical on `landed`. Owed: `test_record_placement_windows`, staged RED by a renderer
  copy that bounds the window by the era's last commit — both later commits are inside the run's era,
  so the fixture reaches that break.
  MET at the post-build run: `test_record_placement_windows` is GREEN, on the same 1543 passed and
  0 failed.
- AC4 — `test_record_placement_replay` — the close and `--landed` placements were replayed on the
  fixture's own history: stage the write, render, commit it, render again. At the close placement only
  `window` and `duration` moved; at the `--landed` placement `window`, `duration` and
  `window closed by` moved, the closer from `terminal-pending` to `terminal-write`. Nothing else in
  the declared scope moved at either. Liveness: the compared records carried 21 Summary facts, 1 Units
  row, 11 Decisions rows and 5 Conformance rows, so the agreement is over a populated record; the
  clean fixture's Anomalies table is empty and the arm names it as the one empty section. The
  membership pin is a set equality against the three labels in both directions. Owed:
  `test_record_placement_replay`, staged RED by a renderer copy whose `terminal` fact reads the phase
  of the last committed record commit, which reds naming `terminal`, and by a copy of the constant
  declaring a Units item a member, which reds on the membership pin while the replay stays green.
  MET at the post-build run: `test_record_placement_replay` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC5 — `render_record` — the landed model with `record_window` removed from its dict rendered both
  `window opened by` and `window closed by` as `-`. Liveness: the same model WITH the field rendered a
  closed-vocabulary member in the closer, so the two `-` are the field's absence and not the
  fixture's. Owed: `test_record_placement_windows`, staged RED by making either provenance fact fall
  back to the model's journal-bounded `window` when `record_window` is missing.
  MET at the post-build run: `test_record_placement_windows` is GREEN, on the same 1543 passed and
  0 failed.

## What else the pass carried

- **What the Timeline exclusion costs, stated as itself.** The replay reds on a new git-derived
  Summary fact that lags, and on a new row in Units, Decisions, Conformance or Anomalies. It does NOT
  red on a Timeline, Coverage or Data item that lags. The Timeline was measured to move by exactly one
  phase row at the close placement, which is the committed write appearing in the history it
  describes; Coverage and Data were measured not to move at either placement and are out beside it
  because both describe the render's own moment. A reader wanting the Timeline graded needs a unit that
  separates "the row the commit adds" from "the row that lags", which nothing here does.
- **The retired loop was the substituted-value class**, and that is the whole of B1: it re-rendered
  `dict(m, window=dict(m["window"], …))`, so it went on passing after `TOOL-dLoggedFlight-24` S3
  stopped the render reading `window` at all. The three placement renders replace it with real models,
  and no arm in the kit edits a window field any more — checked by an assembled needle, not by eye.
- **The suite's only `git commit` reads the machine it runs on**, and `add_fixture_commit` pins the
  three readings that would reach in: `core.hooksPath`, which is set GLOBALLY on this node, so a
  fixture commit would otherwise run this repository's hooks over a scratch tree; `commit.gpgsign`,
  which a signing machine would apply; and `core.autocrlf`, which would rewrite the run-state bytes an
  arm is about to grade. The bug-class checklist named `fixture-inherits-ambient-machine-state` for
  this diff and this is the answer to it. It follows `build_scratch_clone`, which pins the same three
  for the same reason — a reuse the first draft missed, and which is why the hooks path is a directory
  that exists and is empty rather than a name that happens to be absent. The two date variables go in
  through the environment, since a committer time is settable no other way, and come straight back out.
- **A deliberate two-answers exposure, with its compensating check.** The kit README's Summary section
  now names all three `closed-by` members, which `RECORD_SCHEMA` owns. Spec S6 requires the README to
  state them and declares its prose NOT OBSERVED, so no gate holds the pair. The compensating check is
  the build brief's standing rule that a retired identifier leaves the kit, its README, the map
  dossier and the open specs in the same unit, and `test_record_copied_sets` is the seam a later unit
  would gate it in — it already holds three such copies to their owners in both directions.
- **Three module-body constants arrive**, `PLACEMENTS`, `PLACEMENT_LAG` and
  `PLACEMENT_LAG_SECTIONS`, every one public, simple and screaming, so `.lexicon.conf`'s armed row
  falls three further behind the tree. It was NOT touched: the brief forbids a unit here touching
  another kit, and `TOOL-dLoggedFlight-21` left the same debt when it added `COMMITMENT_RE` and
  `TEMPLATE_PARSERS`. That row is graded by the lexicon kit's own selftest, which the owner holds off
  the bar, so a `GATE_SELFTESTS=1` run is where it surfaces. Every new function name leads with a
  declared verb — `derive`, `build`, `parse`, `add`, `test`, and the nested `render_state` and
  `build_replay` — so `VERB_OFFENDER_PIN` does not move.
- **`derive_window` and the model's `window` are untouched**, as section 3 requires, and so are
  `record_window`, `derive_window_bounds` and `check_run_states`. The pending state is a fact about
  when a render runs, not about the run.
- The dossier edit is byte-NEGATIVE by measurement: 20450 bytes before this unit and 20448 after,
  against check 6's cap of 20480. Naming `derive_window_closer` was paid for by retiring the dossier's
  copy of a fact `derive_window`'s own header owns, and by tightening the `check_in_window` sentence.
  Check 6 is held under the pre-commit `--staged` run, so both figures were measured with `wc -c`.
  Units `-20`, `-22`, `-23` and `-27` still owe prose there against 32 bytes of headroom.
- `memory/map/generated/symbols.json` was regenerated in the code commit and gains the two helpers,
  the two arms and `derive_window_closer`; `inventories.json` and `MAP.md` did not move, since no
  claim changed. The dossier claims no Python symbol, as S6 says, and `[paths] globs` already covers
  `tools/runlog/**`.
- The rendered Skill names neither field, so `tools/runlog/SKILL.template.md` was not touched and not
  re-rendered. No run record is committed in this tree, so no committed record changes meaning under
  the vocabularies this unit narrows.
- **The rev-3 fold text is unreviewed surface.** The spec audit chain closed at round 7 and no audit
  runs beside this pass, so the closing diff review at the main loop is where it gets read.

## Owed to the post-build gate run

- `runlog selftest` — `test_record_placement_windows` and `test_record_placement_replay` at a floor of
  1389, plus every record and schema-leg arm whose render now reads its provenance facts from
  `record_window`: `test_record_ac3_shape`, `test_record_ac4_classes` minus the loop this unit
  retired, `test_record_ac6_cap`, `test_window_ac1_ac4_git_only_bounds` and the schema leg's clean
  render, none of which asserts either provenance fact's value. Its budget gains five landed fixtures
  and the suite's first `git commit` calls.
- `lexicon naming predicates`, `codebase-map coverage + freshness` and `memory hygiene`, the gates the
  spec's section 7 names. The map leg grades that the regenerated artifacts rode the same commit as the
  dossier edit, which they did.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. `runlog selftest` printed `1543 passed, 0 failed (1543 assertions, floor 1543)`,
so both durable arms and every record and schema-leg arm listed above are GREEN; this unit's floor
of 1389 has risen with the units after it. The suite cost 80 s run directly, under the 93 s its
budget row declares, so `tools/run-gates/selftest-budgets.txt` does not move; inside the bar's
8-wide pool the same leg recorded 93.9 s, a contention reading that file's own header says to
re-read on a quiet box. `lexicon naming predicates`, `codebase-map coverage + freshness` and
`memory hygiene` are GREEN too. The run's one RED, `govkit selftest`, is on none of these legs:
its 30 failing assertions are the IDENTICAL set `origin/main` carries, pre-existing, untouched by
this build and being fixed in a separate session. It is not called green here.
