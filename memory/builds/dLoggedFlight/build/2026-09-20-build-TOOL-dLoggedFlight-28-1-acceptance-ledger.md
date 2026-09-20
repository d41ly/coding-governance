# Acceptance ledger — TOOL-dLoggedFlight-28

**Serves:** journal TOOL-dLoggedFlight-28

Tier-2 · node d · 2026-09-20 · the build pass of the mutation sweep, against spec rev-2. The spec
moved in this pass: rev-2 narrows S2's and AC2's third liveness from every copy to the kinds the base
render writes a row for, because the assertion as rev-1 wrote it could not pass.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13. `tools/runlog/selftest.py`
was not run, imported or copied under any name, and neither was any other suite, gate leg or bar.
This unit's own code lives INSIDE that module, so nothing below observes the shipped arm executing.
Two substitutes were used instead, and the line between them matters:

- **A probe over a SYNTHETIC model**, kept outside the repository, importing the kit's `model` and
  `record` modules alone. It builds a model of the class model's shape — one row of every declared
  kind, an `owner` row, rows of two retired kinds, and the same four intruders on the same read
  fields — and runs the sweep's own logic over it against the REAL renderer. It grades the MECHANISM,
  never the shipped arm.
- **A STATIC read of the suite module's source as data**, parsed and never executed, which is the
  same class of read as the grep the brief already asks for.

## The criteria

**Evidences:** TOOL-dLoggedFlight-28

- AC1 — `test_record_kind_sweep` — OWED to the post-build suite run. The arm renders
  `build_class_model`'s model once as a base and once more per kind its timeline holds, with every
  event of that kind removed by `build_kind_removed`, and compares each expectation
  `TOOL-dLoggedFlight-26` S3 and S5 derive against that copy's own render through
  `read_sweep_expectations`. Observed on the probe over the synthetic model: the base agreed with
  every derived expectation; each of the eight swept kinds' copies agreed with its own; and the
  `values withheld` count fell from four to three on exactly the three kinds carrying an intruder in
  a read field, which `measure_killed` predicted from the builder's own `read_placed` list without a
  kind-to-placement map. The staged RED was reproduced there: a withheld count typed at the base
  render's value disagreed with the copy on `brief`, `commit` and `dispatch` and would red on the
  first of them. Owed: `test_record_kind_sweep`, staged RED by an arm copy that types the
  `values withheld` count at the base render's value.
- AC2 — `test_record_kind_sweep` — OWED to the post-build suite run. Observed on the probe: the
  removals summed to the timeline's length with the input model unmoved, every swept kind took at
  least one event, and every kind the base render writes a row for moved the rendered bytes. The one
  kind that did NOT is `owner`, whose copy rendered byte-identically — which is why rev-2 narrowed
  this criterion; see below. Owed: `test_record_kind_sweep`, staged RED by a `build_kind_removed`
  copy that returns the model unchanged, which reds on the removal counts, the partition, the
  render-moved liveness and every expectation at once.
- AC3 — `test_record_kind_sweep` — OWED to the post-build suite run. The same sweep runs over
  `build_big_model`'s model at the nominal bounds, where the expectations are S6's `events`, `shown`
  and `elided`. Observed on the probe over a synthetic model lengthened to 200, 61 and 60 rows —
  three renders either side of the elision boundary, two Timeline tables at the first two and one at
  the last: the derived counts matched the render at the base and at every copy in all three cases,
  so the elided branch the wide model takes is exercised rather than assumed. The widest record's
  overflow liveness is exempt, as AC3 states. Owed: `test_record_kind_sweep`, staged RED by an arm
  copy that types the event count at the base model's value.
- AC4 — `tools/runlog/selftest.py` — MET for the comment, OWED for the count. `ASSERTION_FLOOR` reads
  1463, its newest move is `# RAISED 1451 -> 1463 by TOOL-dLoggedFlight-28,` and its block's
  arithmetic is `9 + 3 = 12`. Read back through `parse_floor_raise`'s own three regexes, transcribed
  into the static reader: the newest move reaches the declared floor, names a unit id in the shape
  the arm greps for, and its arithmetic sums to the move's own delta. The 9 is this arm's assertion
  count, counted from the parse tree and confirmed to be nine STATIC call sites with none inside a
  loop, so the count cannot vary per run; the 3 is the decoy checks `main` adds for every new arm.
  Owed: the suite run itself, which grades the executed count against the floor and reds if this arm
  executes fewer than nine assertions.

## What else the pass carried

- **The spec moved, and the measurement is why.** Rev-1's AC2 asserted that EVERY copy's render
  differs from the base. The probe measured an `owner` kind's removal leaving the bytes identical:
  that kind is dropped before a row is built and is counted in no fact
  (`tools/runlog/record.py:795`), so its removal is invisible to the render by construction and the
  assertion could never have passed. A retired kind's removal DOES move the bytes, through
  `TOOL-dLoggedFlight-27`'s `withheld rows` fact, so the sweep still subsumes the retirement case B1
  asked for. Rev-2 asserts the render moved over the kinds the base render writes a row for, and adds
  the partition of the timeline as the liveness that a one-kind sweep cannot satisfy.
- **What the probe does not prove, stated plainly.** It grades the real renderer over a model of the
  class model's shape. It does not grade `build_class_model`, `build_big_model`, the landed fixture's
  own history, `read_class_values`, or the shipped arm's text. Four properties were therefore reasoned
  about rather than measured, all of them landing at the post-build run: that the class model's
  declared-kind rows stay under twice `TIMELINE_EDGE`, which only decides whether the row-times
  expectation compares a whole table or two edges, both of which the probe exercised; that the class
  model's timeline holds no kind the renderer neither rows nor counts besides `owner`, which its
  existing `values withheld` expectation of exactly four already depends on; that the first `commit`
  and `phase` events survive every removal but their own, which the shaped skip check asserts; and
  the arm's wall cost, which nothing here can time.
- **Two static readings stood in for running the module.** Its source parsed; the four new
  identifiers are each defined exactly once at module level with no name shadowed anywhere in 221
  module-level functions; every free name and every `rl_record.` / `rl_model.` attribute the new code
  reads resolves against the module's own bindings and those two modules' real surfaces, so a typo
  cannot wait until VERIFYING to surface as a `NameError` that kills the whole run.
- **The arm reads no retirement constant**, asserted from the parse tree: neither `RETIRED_EVENTS`,
  nor `RETIRED_FIELDS`, nor `TIMELINE_EVENTS` appears in it. That is what keeps it correct on both
  sides of `TOOL-dLoggedFlight-22` and is the whole reason the sweep is parameterized by the
  timeline's own kinds.
- **Three helpers arrive**, `build_kind_removed`, `measure_killed` and `read_sweep_expectations`, and
  the arm itself. `python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for
  all four: the two in rev-1's inventory before they were written, the two rev-2 adds when it added
  them. `VERB_OFFENDER_PIN` does not move. No module-body constant arrives, and the arm's only nested
  callables are lambdas, which the naming leg has no name to grade.
- **`read_sweep_expectations` reads both sides at observation time.** The rendered side comes off the
  markdown through `parse_record_markdown`, the derived side off the model that render was made from,
  so no figure is compared with itself. Its shown slice follows the renderer's edge rule, which is why
  an elided render is graded on the rows it kept instead of being skipped — the skip a wide model
  would otherwise take silently.
- **The kit README's self-test paragraph replaced a duplicate.** The paragraph
  `TOOL-dLoggedFlight-23` added was present TWICE, byte-identical, at lines 351 and 360; the second
  copy is now this unit's paragraph. The README moved from 44737 to 45060 bytes. The map dossier was
  not touched at all: the `[claims]` block carries no symbol tier and its `[paths] globs` already
  covers `tools/runlog/**`, so it stays at 20323 bytes of check 6's 20480 and this unit spends none
  of the headroom the four units still owing prose there will need.
- **`memory/map/generated/symbols.json` moves in this commit** because four module-level functions
  arrive in a file the map inventories; `MAP.md` and `inventories.json` were regenerated in the same
  run and came back byte-identical.
- **The suite's declared budget was NOT moved.** `tools/run-gates/selftest-budgets.txt` still reads 93
  seconds for `runlog selftest` against the leg's 180-second ceiling. This arm adds two fixture builds
  and about a dozen renders, which cannot be timed without running the suite, so the figure is left
  where it is deliberately and the post-build run is where a breach would show.
- **The bug-class checklist named a live one.** `gotchas.py --for-diff` over the first commit
  selected 18 classes, and `amendment-leaves-its-other-half-standing` was a hit rather than a
  reading: rev-2 changed AC2 and left three clauses standing that only made sense under rev-1 —
  section 4's closing sentence, section 5's error-states row, and AC1's empty-swept-set red-when.
  All three moved in the follow-up commit, and the rev-2 entry records them.
  `staged-break-substitutes-a-synthetic-value` describes this pass's probe exactly, which is why its
  limits are written above rather than left for a reader to infer.
  `ledger-token-wrapped-across-a-line-joins-nothing` was checked against this file: every criterion's
  backticked token sits on its own `- ACn —` line, none wrapped.
- **This pass's own prose is unreviewed surface.** No audit runs beside it, so the spec's rev-2 text,
  the README paragraph and this ledger are read for the first time at the closing diff review.

## Owed to the post-build gate run

- `runlog selftest` — `test_record_kind_sweep`, at a floor of 1463, with the three staged REDs AC1,
  AC2 and AC3 name. No other arm's text changed, and the arm adds no fixture file.
- `lexicon naming predicates` — the four new identifiers, each asked of `--suggest` before it was
  written.
- `memory hygiene` — check 23 over this ledger, and the spec's rev-2 status header.
- `codebase-map coverage + freshness` — the regenerated `symbols.json` rode the same commit as the
  four new symbols.
