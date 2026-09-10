**Serves:** journal TOOL-aGradedDialect-2

# Acceptance ledger — TOOL-aGradedDialect-2, the conformance corpus

Every observation below was made on node `a` on 2026-09-10, in the run's own worktree. The corpus was
drawn once, offline, against `C:/projects/incms/main` at `9457e65a2`, read-only; nothing was written
in that tree and nothing was staged from it.

**The one leg that observes any of this is HELD by the ordinary bar.** `lexicon selftest` is
`subject = kit`, `chunk = selftests`, so `bash tools/run-gates/run-gates.sh` does not run these arms
at all. They were observed by `python tools/lexicon/selftest.py` directly, which is what the spec's
§7 says this unit's Definition of Done owes.

**Evidences:** TOOL-aGradedDialect-2

- AC1 — `python tools/lexicon/selftest.py` prints
  `TypeScript conformance corpus: 114 record(s), 118 function and 20 type definition(s)` and passes
  seven loader arms: the record band, all nine declared fields, `kind` in `ts`/`tsx`, unique ids, a
  complete provenance triple with a 40-hex blob, no expectation naming a line its own `src` does not
  have, and no record carrying zero definitions. Five failing cases were STAGED into a copy of the
  corpus and each went red: a `funcs` line of 9999, a dropped field, a duplicated id, an empty
  corpus, and the corpus absent altogether — the last two as a refusal naming the file rather than as
  a skipped arm.
- AC2 — the same run derives the census from the records' own `constructs` tags and prints
  `corpus census: generic 58/20 · jsx 39/25 · nested 49/15 · regex 13/10 · template 49/30 · tsx 62/40 · types 20/20`,
  with `tsx` and `types` counted by predicate rather than by tag. Every
  floor in `TS_FIXTURE_MINIMA` holds. Staged red: stripping the `regex` tag from every record fails
  the arm naming that construct.
- AC3 — `git log --diff-filter=A` and `git log --reverse -S'scan_ts_tokens'`, both run in this
  worktree before the commit, as far as they can be run today. The corpus half — `--diff-filter=A` over
  `tools/lexicon/ts-conformance-fixtures.json` — resolves to this unit's own commit. The extractor
  half — `git log --format=%H --reverse -S'scan_ts_tokens' -- tools/lexicon/lexicon.py` — returns
  EMPTY, because no commit in this repository's history has ever touched a TypeScript extractor. That
  is the ordering property in its strongest available form: the reader does not exist yet, so the
  fixtures cannot have been drawn by it. The spec's trap was confirmed at the same time —
  `--diff-filter=A` over `tools/lexicon/lexicon.py` returns `0007b357`, dated weeks before this
  build, which is exactly the commit that would have refuted a correct ordering had rev-2 not
  replaced it with the pickaxe. The `--is-ancestor` half and the two distinct shas cannot be
  observed until `TOOL-aGradedDialect-3` lands, and per §4 that observation is written into this
  build's closing review record rather than here.
- AC4 — the same run prints a `SKIPPED` line for the TypeScript conformance arm: no TypeScript
  extractor is declared. It names the arm,
  naming `KNOWN_EXTS` and `PARSERS` as the surfaces it looked at, and naming the unit that removes
  the skip. It is a bare `print` rather than a passing `check`, because `check` reaches no output on
  a green run and a skip nobody can see is a comment wearing a check's clothes. Both floor constants
  are declared in `selftest.py` beside the runner, and two arms grade their SHAPE:
  `TS_FLOOR_REFUSAL_SHARE` is asserted to be a share strictly between 0 and 1 and every
  `TS_FIXTURE_MINIMA` value a positive integer, so a later edit zeroing a floor reds rather than
  disarming it quietly. **The branch behind the skip was EXECUTED rather than left for unit 3**, by
  staging `ts` and `tsx` rows into `KNOWN_EXTS` pointing at the shipped `js-regex` set: the arm ran,
  named the reader, and redded on the floor exactly as it should. Staging only the `ts` row found a
  real defect in that branch — it died on `KeyError: 'tsx'`, a traceback where it owed a verdict —
  and a partly armed declaration is a legal outcome, since those are two separate rows owned by
  `TOOL-aGradedDialect-4`. Fixed and re-observed: the arm now scores the 52 records it has a reader
  for, prints how many go unscored, and refuses a kind it cannot read by name. Spec rev-6 records
  the third state.
- AC5 — the same run scores the shipped `js-regex` set against the corpus and prints
  `js-regex against the TypeScript corpus: 68 of 114 record(s) in exact agreement; functions short by 37 of 118 (spurious 1); types short by 20 of 20 (spurious 0)`
  and asserts that the shipped set MISSES the floor, misses on types, and misses on functions too.
  The type row is total: `js-regex.types` matches `class` and nothing else, so it reads none of this
  corpus's 20 type definitions — which reproduces unit 1's 0.6% at fixture scale. Three disagreeing
  record ids print with both readings. The GREEN control sits beside it: a reader returning the
  oracle's own answer clears the floor over every record, without which "js-regex misses" would be
  satisfied by a runner that reds on everything. That control was itself staged red — breaking the
  comparison inside `check_ts_reading` so it ignores LINES makes the green control fail, which is
  how the comparison is known to compare what it claims to.
- AC6 — the refusal share is computed and compared against `TS_FLOOR_REFUSAL_SHARE` on every run,
  printed as
  `refusal budget: one refusal costs 0.0072 of 138 oracle definition site(s), ceiling 0.02`. Four
  staged readers observe it, and the red three are the point: refusing the WHOLE corpus blows the
  budget while satisfying F1, which is the exact hole F2 exists to close; a refusal the reader's own
  header does not name is refused; and a refusal named in the header that no fixture makes it raise
  on is refused. The green one — a single declared, demonstrated refusal inside the budget — clears
  the floor, and an arm first checks that the corpus's smallest record fits inside the ceiling, so
  the green case is known to be stageable rather than assumed. Raising
  `TS_FLOOR_REFUSAL_SHARE` to `0.999` was staged and the total-refusal arm went red, which is what
  proves the ceiling is READ rather than merely readable. The docstring half is enforced as a
  containment test against the reader's own `__doc__` rather than by parsing a header grammar, since
  the grammar of `parse_ts_defs.__doc__` belongs to `TOOL-aGradedDialect-3` and a second parser for
  it living in the grader would be a second answer waiting to disagree.

## What this unit did NOT observe, stated rather than left out

- **The FLOOR itself is unexercised.** No TypeScript reader exists, so F1's exact agreement has been
  observed only against a perfect reader and against `js-regex`. What a real tokenizer scores is
  `TOOL-aGradedDialect-3`'s acceptance, and this corpus is what will refuse it.
- **Nothing checks that an expectation was not hand-edited.** Spec §4 says so plainly and this ledger
  repeats it because it is the residual risk: any digest a later session can recompute, it can
  recompute after editing both halves. Git shows the edit on the path; the rule is that an
  expectation changes only by re-running the oracle; no arm enforces the rule.
- **The construct tags diverge from unit 1's §4.2 census on two rows**, deliberately, and the spec's
  rev-5 line records it. That census was text-level: it counted a backtick anywhere as a template
  literal and a `<Tag`-shaped run as JSX, which in a `.ts` file is a generic or a comparison. These
  tags are read from the compiler's syntax tree instead, because AC2 certifies the corpus from them.
  Measured the same day on the same tree: 1135 and 907 files by the text census against 546 and 531
  by the tree, while the other three rows reproduce to within 2%.
- **The corpus is only as reproducible as that adopter checkout.** The provenance triple names a path
  and a 40-hex blob in a tree this repository does not own. The expectations are the oracle's reading
  of the COMMITTED bytes, so grading needs nothing but this repo — but re-deriving the draw needs
  `C:/projects/incms/main`, and a later session without it should read the provenance as PINNED to
  this date and this machine.
