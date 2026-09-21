# Acceptance ledger — TOOL-dLoggedFlight-29

**Serves:** journal TOOL-dLoggedFlight-29

Tier-2 · node d · 2026-09-20 · the build pass of the placement states, against spec rev-1. The spec
moved three times in this pass. Rev-2 declares the one sub-key a re-derivation cannot read and holds
the returned state against git; rev-3 adds a staged break cut into the shipped builder's own source,
which the bug-class checklist asked for after the first commit; rev-4 is that checklist's second hit,
the two clauses rev-3's own amendment left standing. All three entries are in section 9.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13.
`tools/runlog/selftest.py` was not run, imported or copied under any name, and neither was any other
suite, gate leg or bar. This unit's code lives INSIDE that module, so nothing below observes the
shipped arm executing. Three substitutes were used, and the line between them matters:

- **A probe over a SYNTHETIC fixture repository**, kept outside the repository, importing the kit's
  `model` module alone. It builds a small git history with a committed run-state file, calls
  `build_run_model` over it directly, and measures what a re-derivation reproduces and what it does
  not. It grades the MECHANISM this unit rests on, never the shipped arm.
- **A STATIC read of the suite module's source as data**, parsed with `ast` and never executed, which
  is the same class of read `TOOL-dLoggedFlight-28` used. The candidate predicate was mirrored into
  the probe and run over the real module; the shipped copy of it is what the post-build run grades.
- **The git readings the arm makes**, exercised on a second synthetic fixture: `rev-parse HEAD`,
  `rev-parse :<path>` for a staged write, `rev-parse <commit>:<path>` for a committed one, and
  `diff --cached --name-only` for which of the two it is.

## The criteria

**Evidences:** TOOL-dLoggedFlight-29

- AC1 — `test_record_placement_states` — OWED to the post-build suite run. The arm reads each
  placement's `state`, holds all four of its parts against git, re-runs `build_run_model` over it and
  compares the result with the returned model field for field. Observed on the probe over a synthetic
  fixture: `build_run_model` called twice over one fixed repository state produced 36 model fields of
  which exactly one, `cost`, failed to reproduce, and within it exactly `wall_s` — `cost.git_calls`
  came back 6 both times. With that one sub-key masked the two models were equal on all 36 fields, so
  an honest builder passes. The shortcut was then reproduced on the same probe: a model keyword-copied
  out of an earlier state with `terminal` set differed from the model the later state produces on
  `anomalies`, `conformance`, `facts` and `phase`, so the comparison catches it. The state's own
  readings were exercised on a second fixture: a staged write shows in `diff --cached --name-only`
  and `rev-parse :<path>` returns a blob differing from the committed one, while a committed write
  leaves that list empty — so a state claiming `staged` over a repository holding nothing staged
  reds. Owed: `test_record_placement_states`, staged RED by a `build_placement_models` copy that
  produces `pending` as a keyword copy of the `landing` model with `terminal` set, which must red
  here while `TOOL-dLoggedFlight-25` AC1 still passes on the same copy.
  MET at the post-build run: `test_record_placement_states` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC2 — `test_record_placement_states` — OWED to the post-build suite run. The compared field set is
  each model's own `dataclasses.asdict` key set, recorded inside the comparison loop and compared
  afterwards, so a loop that compared nothing reports an empty set rather than three clean placements.
  Observed on the probe: the model carries 36 fields and `build_masked_model` drops only named
  sub-keys, never a field, so the compared FIELD set stays whole. The mask is held in both directions
  — `MODEL_UNREPRODUCIBLE` names `cost.wall_s` with its reason, and the arm asserts the model carries
  it. `tools/runlog/model.py:1820` is where it is set, from `time.perf_counter()`, and a grep of the
  kit's three modules found no other wall-clock reading on `build_run_model`'s path. Owed:
  `test_record_placement_states`, staged RED by a comparison copy that compares an empty field set.
  MET at the post-build run: `test_record_placement_states` is GREEN there too, on the same 1543
  passed and 0 failed.
- AC3 — `test_record_placement_states` — OWED to the post-build suite run for the arm; the predicate
  was run over the real tree before wiring, as charter section 7 requires. Observed on the static
  read of the module at the pass's start: the declared member `build_placement_models` was clean, and
  21 of the module's 257 functions would have been refused had the predicate swept the module —
  `build_model`, whose `MODEL_SEEN["window"] +=` is a subscript into a plain dict, and
  `build_kind_removed`, whose `out["timeline"] =` is a copy, among them. That measured number is why
  the population is DECLARED, and it is the alternative section 4 rejected. Five staged break shapes
  were each refused with a distinct rule — a field assignment, a keyword `replace`, a subscript edit,
  a `setattr`, and a model type called by keyword — and four accepted neighbours were each clean,
  including `dataclasses.asdict` and a comprehension over it. The shipped source was then mutated:
  `build_placement_models` is 48 lines, one model-field assignment cut in at its line 48 is refused
  for `model-field-assign`, and the source it was cut from reads clean. Owed:
  `test_record_placement_states`, staged RED by the constant copy naming
  `build_placement_models_absent`, by `build_placement_models_field_edit`, by
  `build_placement_models_rerender`, and by the mutated shipped source.
  MET at the post-build run for the arm: the shipped predicate ran GREEN inside
  `runlog selftest`'s `1543 passed, 0 failed (1543 assertions, floor 1543)`, so the mirror and the
  shipped copy agree.
- AC4 — `tools/runlog/selftest.py` — MET for the comment, OWED for the count. `ASSERTION_FLOOR` reads
  1491, its newest move is `# RAISED 1463 -> 1491 by TOOL-dLoggedFlight-29,` and its block's
  arithmetic is `25 + 3 = 28`. Read back through `parse_floor_raise`'s own three regexes, transcribed
  into the static reader: the newest move reaches the declared floor, names a unit id in the shape the
  existing arm greps for, and its arithmetic sums to the move's own delta of 28. The 25 is this arm's
  assertion count, counted from the parse tree with the one `for name in PLACEMENTS` loop weighted by
  its three members and every other call site counted once; the 3 is the decoy checks `main` adds for
  every new arm. Owed: the suite run itself, which grades the executed count against the floor.
  MET at the post-build run for the count too: `runlog selftest` printed
  `1543 passed, 0 failed (1543 assertions, floor 1543)`, so the executed count reached the floor
  and the arm is GREEN. The floor has risen from this unit's 1491 to 1543 with the units after it,
  and executed equals floor exactly.

## What else the pass carried

- **The spec moved twice, and both moves are measurements.** Rev-2: rev-1's S2 asked for a comparison
  "field by field through `dataclasses.asdict`", which as written would have red on a correct builder
  every run, because `cost.wall_s` is a wall-clock reading. The probe is what turned that from a guess
  into a figure — 36 fields, one of them unreproducible, and `git_calls` NOT among them, so the mask
  is one sub-key and not a whole field. Rev-2 also stopped the state being a value the arm trusts:
  all four parts are now read back out of git, because a re-derivation over a repository nobody
  checked is a re-derivation over whatever the builder handed it. Rev-3: the checklist's
  `staged-break-substitutes-a-synthetic-value` reached AC3, whose two staged copies are eight lines
  against the shipped builder's forty-eight.
- **What the probes do not prove, stated plainly.** The re-derivation probe grades `build_run_model`
  over a synthetic two-commit fixture with no journals, no store and no merge. It does not grade
  `build_landed_fixture`'s history, the three placement cuts, `write_journals`, or the shipped arm's
  text. Three properties are therefore reasoned about rather than measured, all landing at the
  post-build run: that a model built WITH journals reproduces as one built without them does, which
  rests on the source reading that `cost.wall_s` is the only wall-clock value on the whole path; that
  the three placements' cut commits are two distinct shas and their models three distinct values,
  which the arm asserts as its own liveness rather than assuming; and the arm's wall cost, which
  nothing here can time. The predicate probe is a MIRROR of the shipped predicate, written from the
  same source; it proves what the predicate does to this tree, not that the shipped copy is spelled
  the way the mirror is.
  ANSWERED: all three hold. `runlog selftest` printed
  `1543 passed, 0 failed (1543 assertions, floor 1543)`, so `test_record_placement_states` is
  GREEN over the real `build_landed_fixture` history with its journals, its three distinct
  placement shas and values, and its wall cost inside a suite that finished in 80 s run directly.
- **Six helpers arrive** — `scan_model_edits`, `check_built_from_history`, `build_masked_model`,
  `build_placement_models_field_edit`, `build_placement_models_rerender` and
  `build_placement_models_read_only` — plus the arm and one nested `read_call_name`.
  `python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for all seven,
  including the nested one, which the naming leg grades. Three module-body constants arrive,
  `HISTORY_BUILT_BUILDERS`, `MODEL_FIELDS` / `MODEL_TYPES` and `MODEL_UNREPRODUCIBLE`; the last two
  are READ off `rl_model` rather than typed, so a renamed model field is graded the day it lands.
  `VERB_OFFENDER_PIN` does not move.
- **The three staged copies are never called.** The predicate reads SOURCE, so a break is staged by
  writing the shape and naming it. Each takes the models as an argument rather than building them, so
  none of them can cost anything if something ever does call one.
- **The arm itself trips the predicate, and that is the design.**
  `test_record_placement_states` contains the `dataclasses.replace` that builds AC1's shortcut, so a
  module-wide sweep would refuse the arm that enforces the rule. The declared set excludes it by
  construction, and the arm's last check asserts the predicate still fires on more than one function
  outside this unit's own — a liveness, not a count, so it cannot rot.
- **The kit README gained a paragraph** rather than replacing one; it moved from 45060 to 46281
  bytes. The map dossier was NOT touched: the `[claims]` block carries no symbol tier and its
  `[paths] globs` already covers `tools/runlog/**`, so `memory/map/features/runlog.md` stays at 20323
  bytes of check 6's 20480 and this unit spends none of the headroom the units still owing prose
  there will need.
- **`memory/map/generated/symbols.json` moves in the first commit** because six module-level
  functions and three constants arrive in a file the map inventories; `MAP.md` and
  `inventories.json` were regenerated in the same run and came back byte-identical. The follow-up
  commit adds no symbol, and the regeneration confirmed that by rewriting nothing.
- **The suite's declared budget was NOT moved.** `tools/run-gates/selftest-budgets.txt` still reads 93
  seconds for `runlog selftest`. This arm builds three more fixture repositories through
  `build_placement_models` and re-derives three models, which cannot be timed without running the
  suite, so the figure is left where it is deliberately and the post-build run is where a breach
  would show.
  ANSWERED: no breach showed. The suite ran 1543 assertions in 80 s invoked directly, under the 93
  s row, so it stays where it is; inside the bar's 8-wide pool the same leg recorded 93.9 s, a
  contention reading rather than a regression.
- **The bug-class checklist named a live one.** `gotchas.py --for-diff` over the first commit selected
  17 classes, and `staged-break-substitutes-a-synthetic-value` was a hit rather than a reading; the
  follow-up commit and rev-3 are its left-shift. `fixture-passes-by-finding-nothing` was answered by
  the four livenesses the arm carries — the non-empty compared field set, the shortcut contrast, the
  three-distinct-states assertion, and the syntax-node count. `naming-leg-grades-what-python-named`
  was answered by asking `--suggest` for the nested helper as well as the six module-level ones.
  `ledger-token-wrapped-across-a-line-joins-nothing` was checked against this file: every criterion's
  backticked token sits on its own `- ACn —` line, none wrapped. Run again over the ledger commit, the
  checklist selected `amendment-leaves-its-other-half-standing`, and that was a hit too: rev-3 had
  extended AC3 and left S3's builder-count sentence and section 7's `New arm:` line describing one
  builder copy. Rev-4 moved both, and no code moved with it —
  `record-without-serves-or-with-a-round-counter` was checked against this file's own name and its
  `Serves` line, which follow the twenty-eight ledgers before it.
- **This pass's own prose is unreviewed surface.** No audit runs beside it, so the spec's rev-2 and
  rev-3 text, the README paragraph and this ledger are read for the first time at the closing diff
  review.

## Owed to the post-build gate run

- `runlog selftest` — `test_record_placement_states`, at a floor of 1491, with the staged REDs AC1,
  AC2 and AC3 name. `build_placement_models` gained a `state` key and no existing arm reads it, so no
  other arm's text changed, and the arm adds no fixture file.
- `lexicon naming predicates` — the seven new identifiers, each asked of `--suggest` before it was
  written.
- `memory hygiene` — check 23 over this ledger, and the spec's rev-3 status header.
- `codebase-map coverage + freshness` — the regenerated `symbols.json` rode the same commit as the
  nine new symbols.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. `runlog selftest` printed `1543 passed, 0 failed (1543 assertions, floor 1543)`,
so `test_record_placement_states` is GREEN with the three staged REDs' arms passing.
`lexicon naming predicates` is GREEN in 3.9 s, `memory hygiene` in 29.1 s and
`codebase-map coverage + freshness` in 2.5 s. The run's one RED, `govkit selftest`, is on none of
these legs: its 30 failing assertions are the IDENTICAL set `origin/main` carries, pre-existing,
untouched by this build and being fixed in a separate session. It is not called green here.
