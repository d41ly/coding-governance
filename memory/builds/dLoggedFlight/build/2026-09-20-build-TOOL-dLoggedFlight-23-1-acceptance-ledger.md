# Acceptance ledger — TOOL-dLoggedFlight-23

**Serves:** journal TOOL-dLoggedFlight-23

Tier-2 · node d · 2026-09-20 · the build pass of the time-population arm, against spec rev-3. The
spec MOVED in this pass, before the code, for three divergences the kit's own seams forced. The
render is driven through `build_record_parts`, `build_record_doc` and `render_markdown` at the
nominal bounds rather than through `render_record`, because a staged Summary fact has to reach the
JSON twin as well as the markdown and because AC2 and AC3 grade the document rather than the bytes.
The `ref` class is widened on the LIVE schema and restored in a `finally`, because `build_matchers`
reads the schema off its own module rather than taking one, so a schema copy reaches no render; the
suite's own class arm stages a vocabulary the same way. And the staged duration is the journal
window's END less the rendered start, which is the sum a reader adds to recover a withheld bound,
rather than that window's own span, which no rendered start joins. Section 9 carries all three.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13: the runlog self-test was
not run, imported or copied under any name, and neither was any other suite, gate leg or bar. The
change was observed instead by three throwaway Python scripts kept outside the repository, which
imported the kit's `record` and `model` modules alone. The first built a SYNTHETIC run fixture — a
small git history and a run-state file written the way the driver writes one — and built its model
through `build_run_model`, so every observation below ran over a model the kit produced rather than
a dict typed by hand. The second staged each RED the criteria name over that model and printed what
the rule returned. The third executed the ARM'S OWN SOURCE, sliced verbatim out of the landed file,
with `build_landed_fixture`, `write_journals` and `build_model` replaced by the synthetic fixture's
and `check` and `check_true` replaced by collectors: **26 passed, 0 failed**, which is the assertion
count the floor moves by, plus the three decoy checks `main` adds per arm.

What that does NOT observe is the arm over the suite's own landed fixture, whose journals give the
model real `verb`, `gate`, `push` and `idle` events to be given sentinels and whose commitment is a
real digest rather than absent. That, and every RED below, is owed to the post-build run.

## The criteria

**Evidences:** TOOL-dLoggedFlight-23

- AC1 — `test_record_time_population` — MET on the probe, OWED as an arm. Over the synthetic
  fixture's model the clean render's every time-bearing token obeyed the rule in BOTH copies:
  `check_record_times` returned an empty refusal list over the markdown and over the Data twin
  alike, with 60-odd `utc` tokens and a `duration` token in each, so the verdict was not one over an
  empty scan. The pre-check ran first and by value: every sentinel lay outside every public time,
  outside every public time plus a public difference and that sum plus one second, outside every
  difference of two sentinels and outside every public clock time — which is what stops a
  coincidence from hiding a break or redding a clean render, and is why the sentinels are SEARCHED
  rather than merely spaced. Each of the five staged breaks asserted that its token reached the text
  and lay outside what the rule accepts before the verdict was read. The duration read from the
  journal window gave `7919s` and then, in the B1 shape the spec now names, a span the rule refused
  twice over — as no difference of two public times, and as a rendered time plus a rendered duration
  recovering a withheld second. The journal time on one kept `commit` row was refused as a `utc`
  token that is no public time. The sentinel epoch second in the `run` count was refused by the
  class-blind scan with NO `utc` refusal beside it, which is the point of scanning classes the
  declaration does not call times. The clock time on a widened `ref` was refused the same way and by
  nothing else; the ISO form on that `ref` was refused by both the class-blind scan and the `utc`
  rule. The live `ref` class was the one the staging borrowed, restored. Owed: the arm, staged RED by
  those five renders.
- AC2 — `check_record_times` and the rendered `elided` fact — MET on the probe, OWED as an arm. The
  fixture's kept rows passed twice `TIMELINE_EDGE` — 77 rendered rows, 60 shown, 17 elided — and the
  `elided` fact's two times were exactly the first and last kept rows the two shown tables omit,
  neither of them a sentinel, with the render still at the nominal edge. Read instead from the
  model's UNFILTERED timeline, which still holds every journal event the rows dropped, the range came
  back different and named a withheld second, because the journal events are interleaved among the
  kept rows by list position. Owed: the arm, staged RED by that unfiltered range.
- AC3 — `check_slots_rendered(RECORD_SCHEMA, doc)` — MET on the probe, OWED as an arm. Over the
  clean render every one of the 11 slots `scan_time_slots` returns had rendered a token, and the
  population held all three key shapes a slot can have and both classes `time_classes` names. Three
  staged fixtures each red naming exactly what they took away: the review round removed gave
  `Decisions/rounds/UTC`; the kept rows cut to `TIMELINE_EDGE` gave `Timeline/elided/0` and
  `Timeline/elided/1`, since nothing is elided; and a schema copy declaring one extra `utc` fact the
  record never fills gave `Summary/landed/0`, which is what a typed slot list could not do. The live
  schema's Summary fact labels were unchanged afterwards. Owed: the arm, staged RED by those three.
- AC4 — `check_time_classes(RECORD_SCHEMA, fixture)` — MET on the probe, OWED as an arm. Over the
  live schema no `shaped` class outside `time_classes` fullmatched a public time's rendered form or
  the rendered form of a difference of two. Over a copy whose `time_classes` holds `utc` alone it red
  naming `duration`, as a class matching a rendered difference of public times. The forms it measures
  against held both halves — more than one public time and more than one difference — so neither is
  an empty set. Owed: the arm, staged RED by that copy.

## What else this pass touched

- The floor moved 1422 to 1451: the arm's 26 checks and the three decoy checks `main` adds per arm.
  The comment above `ASSERTION_FLOOR` enumerates them, as the ones before it do.
- The kit README's record section gains the paragraph naming the arm, and the map dossier's
  no-journal-time bullet names it too, two bytes shorter than the sentence it replaced — the dossier
  measured 20323 of check 6's 20480 after the edit, read with `wc -c`.
- `tools/run-gates/selftest-budgets.txt` was NOT moved. Its runlog row is 93 s against 62 s measured
  at 1291 assertions, and this arm builds one more landed fixture and renders a dozen records; the
  cost is real but unmeasured here, since measuring it means running the suite. If the post-build run
  breaches that ceiling, the budget is what moves, with the reading that moved it.
