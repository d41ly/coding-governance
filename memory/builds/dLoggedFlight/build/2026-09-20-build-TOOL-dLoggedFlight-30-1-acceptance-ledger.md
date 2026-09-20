# Acceptance ledger — TOOL-dLoggedFlight-30

**Serves:** journal TOOL-dLoggedFlight-30

Tier-2 · node d · 2026-09-20 · the build pass of the replacement observed, against spec rev-1. The
spec moved once, to rev-2, and its entry is in section 9: two amendments made BEFORE the code, then
the four other halves those amendments left standing, which the bug-class checklist named after the
code commit.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13.
`tools/runlog/selftest.py` was not run, imported or copied under any name, and neither was any other
suite, gate leg or bar. This unit's code lives INSIDE that module, so nothing below observes the
shipped arm executing. Three substitutes were used, and the line between them matters:

- **A probe over a SYNTHETIC model**, kept outside the repository, importing the kit's `record`,
  `model` and `extract` modules alone. It builds a `RunModel` by keyword, makes the two coverage
  copies, builds the re-pointed schema copy, and calls the SHIPPED `render_record`,
  `build_counted_values`, `derive_counted_sources`, `derive_int_slots` and `derive_fact_templates`
  over them. It grades the MECHANISM the arm rests on, never the shipped arm. Every predicate the
  arm uses was mirrored into it and run; every check below that says "observed on the probe" is one
  of its thirteen, and all thirteen passed.
- **A STATIC read of the suite module's source as data**, parsed with `ast` and never executed — the
  same class of read `TOOL-dLoggedFlight-28` and `-29` used. It confirms the spliced module parses,
  that no new module-level name shadows an existing one, that every free name the seven new functions
  reference is bound at module scope, and that the arm makes exactly thirteen `check`/`check_true`
  calls, which is the figure the floor's arithmetic is built from.
- **A READ of the renderer's own source**, which is the arm's AC1 subject and needs no suite at all:
  the predicate the arm ships runs over `tools/runlog/record.py` exactly as written.

## The criteria

**Evidences:** TOOL-dLoggedFlight-30

- AC1 — `tools/runlog/record.py` — MET on the probe, and OWED to the post-build suite run for the
  shipped arm. The probe ran `scan_replaced_spellings` — the same predicate the arm ships — over the
  renderer's real bytes read through the kit directory: neither `derive_known` nor `known = (cov` is
  present, and the liveness that the text read is the renderer held, since it carries
  `def build_summary_facts` and `def build_counted_values`. A repository-wide grep agrees: outside
  this build's own records the only surviving occurrence of either spelling is in a stale
  `__pycache__` blob, which nothing reads. Owed: `test_record_known_replaced`, staged RED by two
  copies of the renderer's source with one replaced spelling each cut back in at the anchor line;
  both were built and scanned on the probe and each was named by exactly its own needle, and the
  anchor was confirmed to occur exactly once, so a splice that missed cannot read as a clean
  refusal. The copies are TEXT and are never imported or executed, so every criterion of
  `TOOL-dLoggedFlight-27` passes on them by construction — none of that unit's criteria reads a
  source at all, which is the finding this unit closes.
- AC2 — `tools/runlog/record.py` — MET on the probe, and OWED to the post-build suite run for the
  shipped arm. On a schema COPY whose four `owner turns` slots are declared counted from `gates`,
  the shipped renderer was given one model in two coverage states. With the transcripts `present`
  and the gates journal `dead`, `owner turns` rendered `- · - · - · -` while `usage main`,
  `usage agent`, `usage workflow` and `attributed calls` each rendered the model's own counts. With
  the two states swapped — transcripts `not-local`, gates `present` — `owner turns` rendered its
  counts and the other four rendered `-` in every slot. The two copies are one model, so the counts
  behind both renders are identical and only the coverage states differ. Owed:
  `test_record_known_replaced`, staged RED by a renderer copy that restores the replaced test over
  the five Summary facts. That break was run on the probe: under it both renders moved all five
  facts together — counts under the transcripts-present copy, `-` under the not-local one — so the
  re-pointed pair no longer disagrees and this criterion reds.
- AC3 — `tools/runlog/record.py` — MET on the probe, and OWED to the post-build suite run for the
  shipped arm. Rendered against the UNMODIFIED schema, the transcripts-counted copy gave the five
  Summary facts exactly the model's own figures — the owner turns by position, the three usage
  splits by field and the attributed calls — and the not-local copy gave `-` in every slot of all
  five. Every expected value was read from the model at observation time and none was typed. The
  same probe then re-ran both renders under the AC2 staged break and got byte-identical fact values:
  the break that reds AC2 leaves AC3 green. That pair of results is H2 of the spec audit of units 25
  to 27 — the behavioural equivalence it argued — measured rather than argued, and it is why a
  criterion reading rendered values alone could not have observed the replacement.
- AC4 — `tools/runlog/selftest.py` — MET by direct read. `ASSERTION_FLOOR` moved 1491 -> 1507. The
  newest move's own predicate was re-implemented from the docstring that states it and run over the
  spliced source: the newest `RAISED`/`LOWERED` line reads `1491 -> 1507`, reaches the declared
  floor, matches `by [A-Z]+-[A-Za-z]+-[0-9]+[,:]` on `by TOOL-dLoggedFlight-30,`, and its last
  arithmetic expression `13 + 3 = 16` evaluates to 16 on both sides, which is 1507 - 1491. The 13 is
  the arm's own `check` and `check_true` calls, counted from the module's syntax tree rather than by
  hand; the 3 is the decoy checks `main` runs after every arm function. The six helpers the unit
  arrives with carry none. The suite run that grades the executed count against the floor is owed to
  the post-build run.

## What the post-build run must watch

- The arm builds its model from `build_landed_fixture` with a store extract, the construction
  `test_record_ac10_unknown_counts` uses. Its two livenesses assume what that arm already asserts:
  the transcripts read `present`, the in-window owner turn is non-zero and the attributed calls are
  non-zero. Nothing here executed the suite's fixture builders, so those three are the one part of
  the arm that the probe could not reproduce — the probe used a synthetic model with the same shape.
  A failure there would name the liveness, not the mechanism.
- The runlog row of `tools/run-gates/selftest-budgets.txt` still reads 93 s, calibrated at 1291
  assertions on 2026-09-16. The suite now declares 1507. No unit of this build moved that row, so the
  wall-clock ceiling is the post-build run's first real reading of it, and a breach is this build's
  condition rather than this unit's.
- `.lexicon.conf`'s armed module-constant row is graded by the lexicon kit's own self-test, which is
  held off the default bar. This unit adds two public screaming module constants to the runlog suite,
  and so did several units before it on this branch without moving that row. `py.constant` is an
  UNDECLARED cell, so the `lexicon naming predicates` leg does not grade them; every function name
  this unit mints was put to `lexicon.py --suggest --as py.function` and came back OK.
