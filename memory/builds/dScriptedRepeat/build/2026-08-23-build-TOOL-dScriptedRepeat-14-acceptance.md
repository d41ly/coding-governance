**Serves:** journal TOOL-dScriptedRepeat-14

# TOOL-dScriptedRepeat-14 — the acceptance record

Node `d`, 2026-08-23. One line per numbered criterion. One of the eight is UNREACHABLE and says so;
the reason it is unreachable is the most useful thing this unit produced, so it is written out at
length rather than filed as a failure.

**The headline: the signal ships and the fallback ships beside it, not instead of it.** S6 offered the
fold-checklist item as what to do when the machine version could not be built. What actually happened
is that the machine version WAS built, lands inside S5's band at 13% of the corpus, finds real drift in
builds nobody was looking at — and still cannot see the instance that motivated it. Both are true, so
both ship.

## The criteria

**Evidences:** TOOL-dScriptedRepeat-14

- **AC1** — `tools/drift-audit/selftest.py`, `test_readme_mechanism_drift`: a fixture README claiming
  `--counts` takes the recorded facts, dated by `GIT_AUTHOR_DATE`, against a spec revision log whose
  rev-2 entry is dated later and names the same flag. Reported, naming both files and both dates.
  Three negative arms sit in the same fixture: an earlier revision is not a hit, a status word is not
  a mechanism, and a filename is not one either.
- **AC2** — `tools/drift-audit/selftest.py`: a second fixture whose README and spec set agree reports
  0 **and stays LIVE**, so the silence is a verdict rather than a blind spot. Those are two arms
  because a dead probe also reports 0.
- **AC3** — **UNREACHABLE, and not by a clock.** Reconstructed at `5b0d73c0` in a detached worktree
  with the current engine copied in: the signal fires on `dScriptedRepeat` — five rows — but never on
  `--counts`. `git show 5b0d73c0:…spec-dScriptedRepeat-6.md | grep -c -- '--counts'` returns **0**.
  The spec that contradicted the README never spells the flag; the contradiction was between two
  English sentences about one mechanism named two ways. Both comparison variants were run over the
  whole 60-build corpus before concluding it: strict `revised > line_dated` fires on 13% and misses
  it; same-day-inclusive `>=` fires on 30% — outside the band — and misses it too.
- **AC4** — `tools/drift-audit/selftest.py`: a corpus whose README carries no backticked mechanism
  reports `live: False`, which the report renders as DEAD PROBE. The liveness watches the token
  population and the revision population, never "did I find a build" — the tree always has builds.
- **AC5** — **INSIDE THE BAND.** `python tools/drift-audit/drift_report.py --json` over
  `memory/builds/`: 31 rows across **8 of 60** build READMEs, **13%** against a 25% ceiling, with
  **7** of the 8 being builds other than `dScriptedRepeat`. Spot-checked one at random:
  `memory/builds/aTetheredRecord/README.md:84` says unit 2 ships `--print-bindings`, and that unit's
  own revision log says the `--print-bindings` contract was AMENDED by unit 4.
- **AC6** — `python tools/drift-audit/drift_report.py` timed on a quiescent tree: **4.00 s and 5.16 s
  before, 6.43 s and 6.50 s after**. The ~2 s is `git blame`, one process per README, and only for
  the READMEs that carry a token some revision entry mentions — a build with no candidate is never
  blamed. No budget is asserted, because none is declared in the tree.
- **AC7** — taken. `memory/guides/BUILD-METHOD.md` §M8 and `tools/memory-tree/BUILD-METHOD.template.md`
  both gained the re-read item, and it names the limit rather than implying coverage: the signal
  reports the subset where both records spell the mechanism the same way, and the fold owns the rest.
- **AC8** — first clause shipped, second withdrawn. `readme_mechanism_drift` is declared, commented,
  in `tools/drift-audit/drift_signals.template.py`'s PINS with the instruction to seed it from the
  adopter's own first report. The second clause asked for a shipped default other than 0; the kit
  cannot know a number for a corpus it has never seen, and the PINS block forbids a guessed pin by
  name. This repo pins its own measured 31 in `tools/drift-audit/drift_signals.py`.

## What the predicate is, in one paragraph, because the name does not say it

A backticked MECHANISM token in a build README's AUTHORED prose — everything from the first
`<!-- gen:` marker down is rendered from the specs and cannot drift — where some entry in that build's
spec revision logs is dated later than the `git blame` author-date of the README line carrying it and
names the same token. That is "the spec revised this after the README last said anything about it": a
review-me pointer, never a proven contradiction. Three narrowings took it from 42% of the corpus to
13%: the authored region only, mechanism shapes only (the all-caps form requires an underscore so
`LANDED` is vocabulary; the lowercase form forbids a dot so `drift_report.py` is a file), and the
line's own blame clock rather than the file's.

## What M8's bug-class checklist found in this unit's own diff

`python tools/memory-tree/gotchas.py --for-diff abd0f026..HEAD` selected 16 classes. One of them was
live here: **`id-matched-as-a-substring`**. The predicate joined a README token to a revision entry
with `tok in rtext`, so `--check` matches a revision naming only `--check-format`, and every id ending
in a 1-up sequence is a prefix of nine others. It now requires the BACKTICKED form, which is how a
revision log spells a mechanism anyway.

Measured before and after over the whole corpus: **identical, 31 rows over 8 builds either way**. That
is luck rather than equivalence, and the class is left-shifted into an arm rather than into this
sentence — a fixture revision log whose LATEST entry names `--counts-format` while an earlier one
names `--counts`, asserting the row cites the earlier. **Staged RED observed:** restoring the bare
substring makes it fail and name `2026-01-09`; the backticked form makes it cite `2026-01-05`.

Writing that arm also caught a fixture defect worth naming: the first draft's rev-3 prose spelled
`` `--counts` `` inside its own explanation, so the fixture matched itself and the arm failed for a
reason that had nothing to do with the code. A staged break has to be clean of the thing it stages.

## One thing found in passing and not fixed

`live_backlog_rows_per_shard` carries no pin, so it reads `out of tolerance (report only)` at 140 —
which is precisely the failure its own comment names, three lines above where it happens. Left alone:
it is another unit's number to measure and drain, and guessing one here would be the thing that
comment forbids.
