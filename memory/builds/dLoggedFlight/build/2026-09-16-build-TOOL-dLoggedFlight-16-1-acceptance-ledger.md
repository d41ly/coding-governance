# Acceptance ledger — TOOL-dLoggedFlight-16

**Serves:** journal TOOL-dLoggedFlight-16

Tier-2 · node d · 2026-09-16 · the build pass of extract freshness, against spec rev-2. Nothing in the
spec's design moved, so the pass flips its status and bumps no rev. No suite and no gate leg ran, per
the owner's instruction of 2026-09-13: `tools/runlog/selftest.py` was not run, imported or copied.
The change was observed instead by two throwaway Python scripts kept outside the repository, which
imported `extract`, `model` and `record` from the kit and called `extract_session`, `write_session`,
`resolve_run_sessions`, `check_extract_covers` and `render_record` over synthetic stores and
transcripts, and by the adopter run directly. Every staged break below was applied in memory by
those scripts, or to a working copy restored byte for byte, and never committed. The suite's new arms
are written and its floor is raised from 1291 to 1317; each arm's verdict is owed to the post-build
run, with the break that stages it RED named beside it.

## The criteria

**Evidences:** TOOL-dLoggedFlight-16

- AC1 — `extract_session` — over a synthetic two-record transcript, the extract and the copy
  `write_session` stored each carried an integer `extracted_at` inside the epoch seconds read just
  before and just after the call. The stamp is taken before the first file is opened, so it is the
  extraction's start, floored. Owed: `test_fresh_ac1_extracted_at`, staged RED by deleting the
  `extracted_at` key from `extract_session`'s return.
  MET at the post-build run: `test_fresh_ac1_extracted_at` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC2 — `build_run_model` — observed at the function it calls: `resolve_run_sessions` over a named
  session whose only source is a store extract read `stale` with `extracted_at` one second before a
  whole-second window end and `present` at that end, and the discovered path read the same pair.
  `check_extract_covers` answered True only for an integer at or after the end, and False for the end
  as a string, as a float, for a bool and for null. Staged in memory, a `>` comparison made the extract
  at the end read `stale`. Owed: `test_fresh_ac2_ac3_covers_window`, which builds the model over the
  landed fixture with its window end read from a first build with no store, staged RED by the same
  `>` comparison or by `check_extract_covers` answering True.
  MET at the post-build run: `test_fresh_ac2_ac3_covers_window` is GREEN, inside
  `runlog selftest`'s `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC3 — `extracted_at` — an extract without the field, and one holding the string `"1"`, each read
  `stale` through `resolve_run_sessions`, and so did one holding the window's end as a string. Staged in
  memory, a test defaulting a missing field to the window's end made the field-less extract read
  `present`. Owed: `test_fresh_ac2_ac3_covers_window`, staged RED by that default.
  MET at the post-build run: `test_fresh_ac2_ac3_covers_window` is GREEN there too, on the same
  1543 passed and 0 failed.
- AC4 — `render_record` — observed in two halves. `resolve_run_sessions` read the short, field-less
  and mixed shapes `stale` and a fresh session beside a missing one `partial`, with a note counting the
  short and missing sessions and naming neither. `render_record` over a sparse model wrote `-` for
  every owner-turn, usage and attributed-call count and `judged no` under `stale`, and integers under
  `partial`. Staged in memory, `stale` added to `COUNTED_STATES` rendered `3 of 5` attributed calls.
  `test_record_ac10_unknown_counts` was not edited. Owed: `test_fresh_ac4_three_shapes`, which renders
  all five models through `build_run_model` side by side, staged RED by `stale` in `COUNTED_STATES`,
  by `partial` outranking `stale`, or by the model judging idle gaps under `stale`; and the unedited
  AC10 arm, staged RED by `write_extract` losing its default `extracted_at`.
  MET at the post-build run: `test_fresh_ac4_three_shapes` and the unedited
  `test_record_ac10_unknown_counts` are both GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC5 — `bash tools/runlog/adopt-runlog.sh --check` — run directly after `--scaffold`, it exited 0 and
  printed that the Skill is a fresh render. The rendered Skill names `stale` in its coverage list and in
  its **Stale transcript** bullet beside **No local transcript**. With the template's list edited to
  `stalled` and not re-rendered, `--check` exited 1 printing the drift, and the template came back
  byte-identical. The `runlog skill wiring` leg's verdict is owed to the post-build run.
  MET at the post-build run: `runlog skill wiring` is GREEN in 0.7 s.

## What else the pass carried

- `write_extract` in the suite now writes `extracted_at`, defaulting to `FX_EXTRACTED_AT`, one day past
  the fixtures' clock origin, where every model fixture's window ends inside its first three hours.
  None omits the field. So no arm that does not grade freshness reads a short extract.
- `test_model_ac6_coverage` passes a window to `resolve_run_sessions` and gains a `stale` fixture, so
  its every-member check still holds with the widened `COVERAGE_STATES`.
- The class model behind `test_record_ac4_classes` and the schema leg's clean record gives the `git`
  source the `stale` state, so every member of the `coverage-state` vocabulary still reaches the file.
- The Skill-copies arm's renamed-state break moved from "`dead` or" to "`not-local` or", because the
  list no longer ends at `dead`, which would have left the break unapplied and its RED check failing.
- The fresh fixture gives the landed run's `--landed` END a one-second duration, so its window ends on
  a whole second and an extract can be made exactly at that end. Its liveness check asserts both.
- The runlog dossier claims `TOOL-dLoggedFlight-16` and one Gaps sentence. It sat 56 bytes under check
  6's dossier cap, so two clauses elsewhere were shortened to make room; it now sits 2 bytes under.
  The next unit that adds prose there must split it or trim, and check 6 will say so.

## Owed to the post-build gate run

- `runlog selftest` — the three new arms, every arm whose fixture or staged break moved above, and the
  unedited AC10 arm, at a floor of 1317; and its budget row, which the new arms' model builds move.
- `runlog skill wiring`, `lexicon naming predicates`, `codebase-map coverage + freshness` and `memory
  hygiene`, the gates the spec names.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. `runlog selftest` printed `1543 passed, 0 failed (1543 assertions, floor 1543)`,
so every new arm and the unedited AC10 arm are GREEN; this unit's floor of 1317 has risen with the
units after it. The run settles the hand-derived chain that carried it there: executed equals
floor exactly, so no step in it ever put the floor above the true total. The suite cost 80 s run
directly, under the 93 s its budget row declares, so `tools/run-gates/selftest-budgets.txt` does
not move; inside the bar's 8-wide pool the same leg recorded 93.9 s, a contention reading that
file's own header says to re-read on a quiet box. `runlog skill wiring`,
`lexicon naming predicates`, `codebase-map coverage + freshness` and `memory hygiene` are GREEN
too. The run's one RED, `govkit selftest`, is on none of these legs: its 30 failing assertions are
the IDENTICAL set `origin/main` carries, pre-existing, untouched by this build and being fixed in
a separate session. It is not called green here.
