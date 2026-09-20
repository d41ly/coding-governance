# Acceptance ledger — TOOL-dLoggedFlight-24

**Serves:** journal TOOL-dLoggedFlight-24

Tier-2 · node d · 2026-09-20 · the build pass of the Summary window, against spec rev-2. Nothing in
the spec's design moved, so the pass flips its status and bumps no rev. The spec audit of units 21 to
24, round 1, had already promoted this unit's provenance facts and its Skill-placement claim to
`TOOL-dLoggedFlight-25`; what landed is S1, S2, AC1 and AC4 as rev-2 states them, and nothing else.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13: `tools/runlog/selftest.py`
was not run, imported or copied under any name, and neither was any other suite. The change was
observed instead by one throwaway Python script kept outside the repository. It built two synthetic
git fixtures of its own — committer times set through the environment, no journal, no transcript, no
store — and called `build_run_model`, `check_records`, `render_record` and `derive_window_bounds` over
them. Every one of its observations held, on both fixtures. The durable arm is owed to the post-build
run, with the break that stages it RED named beside it.

## The criteria

**Evidences:** TOOL-dLoggedFlight-24

- AC1 — `record_window` — over a landed fixture whose HEAD holds every record commit, the model's
  `record_window` and the window `check_records` derives for that run were the same dict, start, end
  and both provenance keys. The Summary then rendered `window` as the start commit's time and the
  LANDED write's, and `duration` as their difference in seconds; both bounds were committer times read
  off the fixture's own history with `git log`, never from the model. Liveness on a second, non-terminal
  fixture with a later own commit: the model's journal-and-commit-bounded `window` ended past the leg's,
  the two windows were NOT equal, and the render still closed at the last record commit's own committer
  time, which is the half-open second taken back off. The landed fixture's base commit is not a
  rendered bound, since a run starts at the commit that ADDS its record. The durable arm is owed:
  `test_window_ac1_ac4_git_only_bounds`, staged RED either by handing the second `derive_window` call
  the journal-bound `term_end` and `last_event` the model's own window uses, or by rendering `window`
  in place of `record_window` in `build_summary_facts`.
- AC4 — `render_record` — the same landed model with `record_window` removed from its dict rendered
  `window` as `- to -` and `duration` as `-`, while `values withheld` stayed where it was, so the
  absent field is an absence and not a refused value. Liveness: the same model WITH the field rendered
  a parseable UTC time in each bound, so the `-` is the field's absence and not the fixture's. Owed in
  the same arm, staged RED by making `derive_window_bounds` fall back to the model's `window` when
  `record_window` is missing.

## What else the pass carried

- `derive_window_bounds` is the only new function, and the render is its only caller. It returns
  `(None, None)` for a missing, empty or non-numeric window, subtracts the half-open second only for a
  `last-activity` end, and passes a `terminal-end` through — a case `record_window` cannot produce,
  since the model derives it with no `term_end`, and which would be a journal time if it ever did.
- **The arm's `last-activity` check edits a window rather than building one**, which is the
  substituted-value class: it hands `derive_window_bounds` a copy of the fixture's own
  `record_window` with `end_from` swapped, so it grades the function and not the path. The REAL path
  was observed here on the second probe fixture — a non-terminal run whose later own commit pushed the
  model's window past the leg's, rendering the last record commit's own committer time — and it is
  `TOOL-dLoggedFlight-25`'s AC1 and AC3 that observe it durably, over models built at the Skill's
  `landing` and `pending` placements. This unit does not claim that coverage.
- The model's `window` is untouched and still bounds every timed set. The second `derive_window` call
  reads only `phases_at`, which the model had already built, so the unit adds no git call and no source
  read; `test_model_ac8_git_calls` should not move.
- The rendered `window opened by` and `window closed by` still read the model's `window`, exactly as
  rev-2 leaves them. `TOOL-dLoggedFlight-25` re-points both at `record_window` and adds the
  `terminal-pending` closer, so the loop in `test_record_ac4_classes` that edits those two provenance
  keys still reaches the render and is left alone here.
- The kit README gains one paragraph in the record section saying which of the two windows the Summary
  renders. The model's own window bullet and the schema-leg paragraph are unchanged, so the fact is
  stated once.
- The dossier edit is byte-NEUTRAL by measurement: 20450 bytes before this unit and 20450 after,
  against check 6's cap of 20480. The schema-leg paragraph's window sentences were rewritten to carry
  `record_window`, and the 25 bytes of listing this unit among the feature's decisions — as units 14,
  16 and 21 each did — were paid for by trimming those same sentences. Check 6 is held under the
  pre-commit `--staged` run, so both figures were measured by hand rather than trusted to the hook.
  Units `-20`, `-22`, `-23` and `-27` still owe prose there against 30 bytes of headroom; splitting the
  dossier remains a unit of its own, not an edit a build pass makes in passing.
- `memory/map/generated` was regenerated in the code commit, and `symbols.json` gains
  `derive_window_bounds` and the new arm. Both names lead with a declared verb, `derive` and `test`, so
  `VERB_OFFENDER_PIN` does not move; no module-body constant arrived, so the lexicon's armed row does
  not move either.
- The suite's floor rises from 1348 to 1358: the one new arm's seven checks plus the three decoy checks
  every arm carries. The reason is written into the floor's own comment block.
- No run record is committed in this tree, so no committed record's window changes meaning under this
  unit, and nothing needed re-rendering. The rendered Skill names neither field, so it was not
  re-rendered.

## Owed to the post-build gate run

- `runlog selftest` — `test_window_ac1_ac4_git_only_bounds` at a floor of 1358, plus every record arm
  whose model now carries a second window: `test_record_ac3_shape`, `test_record_ac4_classes`,
  `test_record_ac6_cap` and the schema leg's clean render, none of which asserts the `window` or
  `duration` fact's value. Its budget row gains one landed fixture and one `check_records` call.
- `lexicon naming predicates`, `codebase-map coverage + freshness` and `memory hygiene`, the gates the
  spec's section 7 names.
