# Acceptance ledger — TOOL-dLoggedFlight-20

**Serves:** journal TOOL-dLoggedFlight-20

Tier-2 · node d · 2026-09-20 · the build pass of the source rule, against spec rev-4. The spec MOVED
in this pass, to rev-4, before the code: section 9's instruction to check each clause of section 2
against what the siblings landed found S7's second clause already discharged, by the leg's header
rule for a record and by this unit's own AC1 for the schema. Writing a third rule for it would have
been one question with two answers, so S7 now says what the source rule does not reach.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13: `tools/runlog/selftest.py`
was not run, imported or copied under any name, and neither was any other suite, gate leg or bar. The
change was observed instead by three throwaway Python scripts kept outside the repository, which
imported the kit's `record` and `model` modules alone. One enumerated the schema's time slots before
the code existed; one exercised `check_time_sources` over the live declaration and three staged
copies; one rendered a SYNTHETIC model through `render_record` and graded its bytes with
`check_record`, the function `check-records` reaches through `check_record_lines`. The synthetic
model is the substituted-value class stated plainly: it has the right SHAPE, and the arm over the
suite's own class-model fixture is owed to the post-build run.

## The criteria

**Evidences:** TOOL-dLoggedFlight-20

- AC1 — `check_time_sources(RECORD_SCHEMA)` — MET on the probe, OWED as an arm. Over the live schema
  it returned an empty refusal list, and `scan_time_slots` returned 11 slots: the Summary `window`'s
  two and its `duration`, the Timeline `elided` fact's two, one per kept Timeline row kind, and the
  Decisions `rounds` table's `UTC`. Every one carries a declared set and every set is a non-empty
  subset of `TIME_SOURCES`; the `elided` fact's two are the pair that made the value a SET, since the
  first and last elided row can be a `commit` row or a `dispatch` row. The population held all three
  key shapes — a fact placeholder, a per-kind row column, a plain table column — and reached both
  classes in `time_classes`, so `refuses nothing` was not a verdict over an empty set. Each staged
  copy was refused exactly once, naming the slot: `driver` added to the Summary window's sources gave
  `Summary/window/0 names the source 'driver', which a committed time may not be read from`; the
  Decisions `rounds` entry removed gave `Decisions/rounds/UTC renders a utc and declares no source`;
  and an entry keyed to a Summary fact that renders no time gave
  `Summary/phase/0 is no time slot the schema declares`.
  The live declaration was re-read afterwards and still refused nothing. Owed:
  `test_record_ac1_time_sources`, staged RED by each of those three copies, and by the check that
  reads the keys and their subset off the DATA rather than off the checker's verdict — which is the
  arm that still reds if `check_time_sources` itself is gutted.
  MET at the post-build run: `test_record_ac1_time_sources` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC5 — `check_record` over a rendered record — MET on the probe, OWED as an arm. A record rendered
  from a synthetic model graded clean, zero refusals, so the grader is not one that refuses
  everything. Its kept `commit` row re-sourced `driver` was then refused exactly once, on that row's
  own line, under the rule `source`, whose refusal names the UTC column, the source it found and the
  fact that the schema does not declare that slot may be filled from it. No other rule named that
  line, which is
  AC5's Red-when: `driver` is a member of the `source` vocabulary and `commit` keeps its layout, so
  every class check passed the row. Three neighbours were observed with it. The same row with its
  source cell `-` is refused too, so an unattributed time is not an absent value. A `phase` row
  sourced `git` is refused, so the rule reads the slot's own declaration and not one allowlist for
  the table. A row whose UTC is `-` is not refused by this rule at all — `first-cell` catches it
  first — which is the documented limit. Owed: the `source` variant of `test_schema_ac2_refusals`,
  staged RED by the same substitution over the class model's record, with the block holding that row
  to the source rule alone; that arm also holds `RECORD_RULES` in both directions, so a new rule
  nobody staged reds it.
  MET at the post-build run: the `source` variant of `test_schema_ac2_refusals` is GREEN, inside
  `runlog selftest` printed `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC7 — `grep -n 'no event times' .claude/skills/runlog/SKILL.md` — MET, run in this pass. It finds
  the sentence twice, in the description and in step 1. The question table's between-two-times row
  now reads the model's `timeline`, which elides nothing, in its first source cell, and the record's
  Timeline, whose rows git and the run-state file timed, in its second. The description routes a question about a time to the local run model first and the
  record second, is 870 characters of the 1024 a description is allowed, still names every keyword
  the Skill arms require, and still disclaims code search with nothing claiming it beforehand. Both
  files were re-rendered together by `bash tools/runlog/adopt-runlog.sh --scaffold`. Owed:
  `test_skill_ac7_time_routing`, staged RED by a copy claiming the record carries every event's time,
  and by the half-amended copy AC7 names — the sentence kept, the row's two source cells swapped back
  and the description's routing clause dropped — which is refused for both routings and not for the
  sentence. Both stagings are DERIVED from the rendered text, never typed, so they cannot quietly
  stage nothing the day the prose is reworded.
  MET at the post-build run: `test_skill_ac7_time_routing` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC8 — `grep -n 'refuses the whole record' memory/gotchas/withheld-value-recovered-from-a-derived-one.md`
  — MET, run in this pass. It exits 1 and prints nothing. The fix section's second bullet is now
  `Withhold the SOURCE, not the value`, which names `check_time_sources`, the schema leg and
  `TOOL-dLoggedFlight-23`'s population arm, and records that grading rendered values ran over a
  narrower population than the leak five revisions running. Two halves of that amendment went with
  it, both found by re-reading the file rather than by grepping the retired phrase: the section's
  lead said the FIRST part was the one that holds, and `What this does NOT say` still explained why a
  coincidence was refused by a text check that no longer exists.

## What this pass did not do

- **It ran no suite, no gate leg and no bar**, so every arm above is owed to the post-build run. The
  floor moved 1404 -> 1422 by 18 — two new arms at 5 and 4 checks with their 6 decoy checks, and 3
  checks inside the schema leg's existing refusal arm — derived by hand, and a floor under the true
  total still passes.
  ANSWERED at the post-build run, which was the whole bar at `9e948546` with every guard lifted
  and the kit self-tests on: `runlog selftest` printed
  `1543 passed, 0 failed (1543 assertions, floor 1543)`, so every arm above is GREEN. The floor
  this unit moved to 1422 by hand has since risen to 1543, and the run settles the arithmetic:
  executed equals floor exactly, so no hand-derived step ever put the floor above the true total.
- **It did not wire `check_time_sources` into the leg's exit code.** It is graded by an arm, exactly
  as `check_count_sources` is: a schema defect is a code defect, and making it a record refusal would
  red every committed record for a fault in none of them.
- **It did not check that a declared source is the one the value really comes from.** Nothing in
  `check_time_sources` reads the renderer or a model. The leg's `source` rule grades that where a
  rendered row states its own source, and `TOOL-dLoggedFlight-23`'s population arm reads the rendered
  text; a fact's time and the Decisions `rounds` column state no source in the record's bytes at all.
- **It corrected one sentence that is unit 22's residue**, in the map dossier: the schema-leg
  paragraph still said the `label` class admits a lowercase UUID, and that class retired with the
  workflow rows. The kit README's twin sentence was rewritten then; the dossier's was not.
- **The dossier edit is byte-neutral or shorter, measured**: 20358 bytes before this unit, 20325
  after, against check 6's 20480 cap. The new bullet was paid for by two cuts — a clause stating that
  the leg grades committed bytes against the schema's data, which the very next paragraph states as
  its heading, and the history behind two bound constants that the constants themselves carry.
