**Serves:** journal TOOL-aGradedDialect-3

# Acceptance ledger — TOOL-aGradedDialect-3, the TypeScript reader

Every observation below was made on node `a` on 2026-09-10, in this run's own worktree, against the
corpus exactly as `TOOL-aGradedDialect-2` froze it. The fixture file was not edited and is not in
this unit's declared write set.

**The leg that observes most of this is HELD by the ordinary bar.** `lexicon selftest` is
`subject = kit`, `chunk = selftests`, so `bash tools/run-gates/run-gates.sh` does not run these arms
at all. They were observed by `python tools/lexicon/selftest.py` directly — `OK — 648 arm(s)`, exit
0 — which is what the spec's §7 says this unit's Definition of Done owes. AC8 is the exception and
rides the ordinary bar as `lexicon naming predicates`.

**Evidences:** TOOL-aGradedDialect-3

- AC1 — `tools/lexicon/selftest.py`'s `test_ts_constructs` — six construct arms, each one a shape a
  same-line pattern reads wrong. A `function` keyword inside a template literal yields only the real
  definition beside it; a regex literal carrying `\{a\}` does not open a block; a nested
  `` `a${`b${`c`}`}d` `` closes at the right backtick; JSX text and a JSX expression container
  holding a live arrow yield nothing but the component; a definition written inside a template
  `${}` substitution yields nothing at all; and `render: (el) => string` comes back as a TYPE inside
  an interface and as a DEFINITION inside the object literal one line down. Red when: a word token
  escapes one of those spans, which is what each arm's expected list refuses.
- AC2 — `tools/lexicon/selftest.py`'s `test_ts_sentinel` over the frozen `TS_SENTINEL` and
  `TSX_SENTINEL`: `parse_ts_defs` returns thirteen functions and four types as an exact ordered
  list, each at the line its NAME sits on, and the tsx sentinel returns three functions and two
  types the same way. The sentinels deliberately carry the four forms the conformance corpus does
  NOT — a getter, a setter, a `constructor` and an `enum` — plus a generator, a function
  expression bound to an annotated `let`, an object method, a nested property arrow and a class
  property arrow. Red when: a form is located at its body's line, which the equality refuses by
  value rather than by count.
- AC3 — `tools/lexicon/selftest.py`'s `test_ts_refusals`: eight unterminated constructs, each fed to
  `parse_ts_defs` or `parse_tsx_defs`, each raising `SyntaxError` whose message names the construct
  AND the line it opened on. A ninth arm computes the pairwise containment of the eight needles and
  requires it empty, so no refusal firing first can score a pass for a sibling that is unarmed —
  the defect the shell parser's own arms record, where `$((` sat unarmed while five neighbours
  looked covered. Red when: a construct returns a list instead of raising, which the `else` branch
  of each row reports by name.
- AC4 — `parse_ts_defs.__doc__` is asserted to contain ten tokens, one per refusal plus the
  not-an-interpreter line: `SyntaxError`, `unterminated string`, `` `${…}` substitution ``,
  ``JSX `{…}` expression``, `OVERLOAD SIGNATURE`, `eval`, `import`,
  `COMPUTED or string-literal property key`, `IMPORTS ARE AN EMPTY LIST` and `NOT AN INTERPRETER`.
  Three of the six refusals have no runtime failure to stage and this is their only observation.
  `parse_tsx_defs.__doc__` is asserted non-empty, which is why the pair is two named functions
  rather than a `functools.partial`. Red when: a refusal ships with no line in the header.
- AC5 — the conformance arm scores the reader over the fixtures `TOOL-aGradedDialect-2` commits and
  prints, per side, recall and precision DERIVED at observation time:
  `TypeScript func recall 122/122 (1.0000) · precision 122/122 (1.0000)` and
  `TypeScript type recall 20/20 (1.0000) · precision 20/20 (1.0000)`, each beside the floor it is
  compared to — F1, EXACT agreement, so both figures are 1.0000 or the reading is below it. The
  run's own summary line reads `115 of 115 record(s) in exact agreement, refusal share 0.0000`. No
  score is written into the spec or into this file's assertions; the arm computes `_want`, `_hit`
  and `_found` from the records it actually scored. Red when: the arm reports a score over an empty
  or absent fixture set — refused two ways, by `read_ts_fixtures` raising on an empty or missing
  corpus and by this arm requiring `_want > 0` on both sides before comparing anything.
- AC6 — `read_ts_mode` earns `parser` here, and the same run prints it beside the number that
  decided it:
  `TypeScript coverage mode EARNED: parser — 115 of 115 record(s) in exact agreement, refusal share 0.0000 against the declared ceiling 0.02`.
  The label is `read_ts_mode`'s return and nothing else: one function, `parser` when
  `clears_floor` and `probe` otherwise. THE FAILING CASE WAS OBSERVED, and it is staged outside the
  arm above so it runs whether or not a reader ships: `read_ts_mode` over the shipped `js-regex`
  reading of this corpus returns `probe`, over the oracle's own answer returns `parser`, and over
  the total-refusal reader returns `probe` while F1 alone is still clean — so F2 reaches the label
  and not only F1. Red when: `parser` is printed under a below-floor score, which those three arms
  refuse from both directions.
- AC7 — `run_case` builds a throwaway repo declaring `ts:ts-tokens:probe tsx:tsx-tokens:probe` over
  one `.ts` and one `.tsx` fixture. The run exits 0, `does not ship` appears nowhere, the modes line
  carries `.ts=probe`, and the printed `coverage — armed 2 of 2` line COUNTS both fixture files.
  BOTH HALVES OF §8 F1 WERE STAGED RED separately, through `run_case`'s asserted `patch`. Reverting
  the DISPATCH half — narrowing `resolve_extractor` back to `mode == "parser"` — makes the run
  refuse the row by name. Reverting the REPORTING half — putting the old inline predicate back into
  the coverage walk — leaves the extension extracting while the coverage line prints
  `coverage — armed 0 of 2`, which is the two halves of one run disagreeing about the same file and
  is exactly the state F1 exists to close.
- AC8 — `python tools/lexicon/lexicon.py` over this repo exits 0 and prints `lexicon OK`.
  `VERB_OFFENDER_PIN` does NOT move: `P1 verb graded=` rises 2061 -> 2080 and `offenders=` holds at
  984, because `--suggest --as py.function` was asked for all nineteen new function names BEFORE
  each was written and every one leads with a declared verb. `py.function.conv` rises 1301 -> 1320
  with zero violations. The non-move is recorded beside the pin in `.lexicon.conf` as a
  MEASUREMENT, in the same shape a move would take. Red when: a pin is raised to absorb a new name
  — which is why the names were graded first and the pin was read off the tool afterwards.
- AC9 — `tools/lexicon/selftest.py`'s `SNIFF_FIXTURES` table, one file per ARMED language, with the
  `LANGS` rows, the `CELLS` rows and every assertion derived from that table. THE POSITIVE IS
  ASSERTED FIRST: each declared cell reports a NON-ZERO graded population and the run prints
  `coverage — armed 2 of 2`, so the empty `blind` set is evidence rather than an unarmed corpus.
  Then the negative: the run exits 0 and prints no `DEAD SNIFFER`. Staged red: narrowing
  `DEFINITION_SNIFF` back to the rows shipped before this unit blinds both files and the run reds
  naming `found no definition in 2 file(s)`.
- AC9 — amended rev-4 — its Red-when claimed that dropping the `interface` row alone would blind
  the fixture. Measured against the fixture AC9 itself specifies, it does not: each file sniffs
  positive through TWO of the widened rows, the `.tsx` one through `interface` and through the const
  row because its arrow carries a type annotation, the `.ts` one through `type` and through `enum`.
  The staged break reverts the whole three-row widening instead, which does blind both. §7's
  matching `New arm:` line moved with it. Logged in the spec's §9 rev-4 line.

## What this unit did NOT observe, stated rather than left out

- **The reader was graded against ONE adopter tree.** The corpus is 115 excerpts from
  `C:/projects/incms/main`, so a construct absent there is untested rather than proven. The named
  instances are the four forms the sentinels carry BECAUSE the corpus does not: a getter, a setter,
  a `constructor` and an `enum`, plus the overload signature unit 1 measured at 0.0% of that tree.
  Those are frozen kit fixtures and can never become a corpus read.
- **`<T,>` in a `.tsx` file is decided by a LOOKAHEAD, and it is the only one in the tokenizer.**
  TypeScript's own tie-break, argued in `check_ts_generic`: in a `.tsx` source `<T>` is an element
  and `<T,>` and `<T extends X>` are type parameters. Without it a `.tsx` file carrying
  `const pick = <T,>(x) => x` scans as an element whose closing tag never arrives and REFUSES the
  whole file. The corpus carries no instance — 66 `.tsx` records and not one — so this is observed
  only by the `TSX_SENTINEL`, which is why the lookahead is written down rather than left to be
  rediscovered as a refusal in an adopter's tree.
- **THERE IS A FIFTH COPY OF THE ARMEDNESS PREDICATE, and it is in another kit.** §8 F1 named four
  sites and all four are in `tools/lexicon/lexicon.py`; `tools/drift-audit/drift_report.py`'s
  `_read_armed` spells the same rule a fifth time — `mode == "probe" and pset not in sets` skips a
  row, with no `pset not in lex.PARSERS` clause beside it — under a docstring whose own words are
  "`lex.PARSERS` IS READ, NEVER RESTATED". It is INERT today, because nothing declares a `ts` or
  `tsx` row until `TOOL-aGradedDialect-4` and the verdict this unit hands it is `parser`, which
  that predicate reads correctly. It would diverge only for a `probe`-declared parser id, which is
  the below-floor path. NOT FIXED HERE: that kit is outside this unit's declared write set and
  outside §8 F1's four sites, and reaching into it would drag its own gate legs into a records-clean
  landing. It is a finding for the closing review, and the class F1 closed is therefore closed
  inside one file rather than across the repo.
- **A `parser` row naming an unshipped id is now armed-by-fact rather than by mode.**
  `resolve_extractor` returns `None` for it, where the old inline predicate counted every `parser`
  row as armed regardless. That state already REDS in `scan_corpus` by name, so no verdict moves;
  the coverage fraction for such a tree is now smaller by that extension, which is the honest
  reading rather than the previous one.
- **Unit 2's own AC4 arm is stricter than this unit's AC6.** That arm asserts the declared reader
  `clears_floor`, so a below-floor reader would RED the suite rather than shipping `probe` and
  reporting incomplete, which is what AC6 says both outcomes may do. It is moot today — the reader
  clears the floor — and it is recorded here rather than edited, because the arm belongs to a closed
  unit and adjusting another unit's floor assertion to fit this one's wording is the shape this
  build's README forbids. It is a finding for the closing review.
- **The two-sha ordering proof is not made here.** `TOOL-aGradedDialect-2` §4 puts it in this
  build's closing review record, and this unit's commit is the first to touch a TypeScript
  extractor — which is what makes the `-S'scan_ts_tokens'` half resolvable at all.
- **`.claude/skills/lexicon/SKILL.md` was not rewritten.** S7 owed a re-render and the declaration's
  graded content did not move: this unit's `.lexicon.conf` edit is a comment beside a pin, so
  `bash tools/lexicon/adopt-lexicon.sh --check` reports `Skill in sync` with nothing to regenerate.
  `memory/map/generated/symbols.json` DID move and was regenerated in the same commit, which the
  write set was widened through `--dispatch` to cover.
