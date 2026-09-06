**Serves:** journal TOOL-aSurfacedLexicon-14 TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-7

# Build pass, steps 4 and 5 — the shell parser, the cell refusals, the selector, the P1 split

Node `a` · 2026-09-05 · build `aSurfacedLexicon` · streams tooling. Four units, SEQUENCED, all four
claiming the engine file.

**The headline is coverage.** Before this pass the kit graded `armed 57 of 141 definition-carrying
files (40.4%)`. After it, `armed 140 of 141 (99.3%)`. The single unarmed file is the extensionless
bash carrier the shell unit's own fork rules out of reach, and it is named rather than rounded away.

A verifier ran a **41-revert matrix** over every mechanism the diff adds — reverting each one and
watching whether any arm noticed. That found one genuinely ungated mechanism and two weak arms that
a passing suite hid completely.

**Evidences:** TOOL-aSurfacedLexicon-14
- AC1 — one process over one `git ls-files` list — parser 607 against the naive pattern's 608. They DIFFER, which is what the criterion requires, and the direction is the heredoc body the parser declines.
- AC2 — a definition inside a heredoc BODY — not returned; reverting the heredoc drain reds a named arm.
- AC3 — a quoted run of `<` characters — the ten definitions below it survive. The tracked-file half is measured OUTSIDE the suite deliberately: a shipped kit self-test cannot open a file only this repo has.
- AC4 — the extractor forced to return nothing — RED, `DEAD PROBE`, naming the declared parser rather than reporting a reassuring zero.
- AC5 — the frozen sentinel fixture with one form commented out — RED, naming the forms that survived.
- AC6 — a shell file with an unterminated quote — RED naming the file and the line, with no DEAD PROBE beside it, because the population is non-empty.
- AC7 — amended — NOT OBSERVABLE in a working tree and reported rather than faked. The staleness signal compares the stamp against the COMMIT DATE of the last commit touching the language line, so an uncommitted edit moves it not at all. The re-stamp is written and rides in this change; the red half is unobservable before the commit that makes it so.
- AC8 — `--check` coverage line — 57 of 141 to 140 of 141. Reverting the language row returns it.
- AC9 — the pre-wiring run record — file count, hits, near-misses split three ways, and three things the run caught that the spec did not predict.
- AC10 — `parse_shell_defs.__doc__` — enumerates all four definition forms and all three refusals, asserted against the docstring rather than the README.
- AC11 — the shell cell armed at a declared convention — green at the measured pin; renaming one shell function to a screaming spelling reds it, naming file, line and name.
- AC12 — the pin left unraised with the language armed — RED. The contribution is +507, one below the 508 upper bound the spec carried, because the parser declines the heredoc name the naive pattern counted.

**Evidences:** TOOL-aSurfacedLexicon-6
- AC1 — a cell armed over an empty population — RED, `DEAD CELL`, naming the cell and its convention.
- AC2 — `tools/lexicon/selftest.py` — the undeclared-cell report — three extracted populations with no declaration row, each with its count, and the refusing half observed in the fixture repo with the promotion constant forced on.
- AC3 — `tools/lexicon/selftest.py` — a parity assertion between report rows and parsed rows — reverting it reds two named arms.
- AC4 — `tools/lexicon/selftest.py` — every printed row carries its population RULE — dropping the rule clause reds three named arms. This unit owns population sizes, so a count without its rule is the defect it exists to prevent.
- AC5 — `tools/lexicon/selftest.py` — the census figures in the declaration — read from the ROW that owns each, not by substring over the file. The first cut used a bare substring and a falsified denominator left it green.
- AC6 — `tools/lexicon/selftest.py` — a report that builds no rows — refused rather than printed empty, and so is one that drops a single row while printing the others.
- AC7 — `tools/lexicon/selftest.py` — the dead-cell refusal disabled — reds two arms while the dead-probe arm stays untouched, so the two refusals are distinguishable.
- AC8 — amended rev-2 — STRUCK. Adding the conf to a leg guard reds an unguarded gate, and the kit descriptor had refused that edit in writing.
- AC9 — `python tools/lexicon/lexicon.py --check` — the build's FIRST armed cell — green at its measured pin with its population rule beside it, and a staged module-body constant reds it by name.
- AC10 — `python tools/codebase-map/test_codebase_map.py` — the generated map artifact — the failing case observed, then regenerated in this same commit.

**Evidences:** TOOL-aSurfacedLexicon-13
- AC1 — `python tools/lexicon/lexicon.py --check` — a selector routing a subset of a cell to a second convention — RED on the subset while the parent stays green.
- AC2 — `python tools/lexicon/lexicon.py --check` — three readings in one session — parent alone, selector alone, and both, each with its own population.
- AC3 — two overlapping prefixes over one name — `AMBIGUOUS SELECTOR`, refused rather than silently resolved to whichever matched first.
- AC4 — a selector whose subset is empty — `DEAD CELL`.
- AC5 — `tools/lexicon/selftest.py` — a decorator selector — grades the decorated definitions and nothing else, including a dotted decorator selected by its last segment.
- AC6 — `tools/lexicon/selftest.py` — a selector on a probe-mode language — refused at parse time naming the language and the mode, while the same selector on a `parser` language parses.
- AC7 — `tools/lexicon/selftest.py` — the fixtures are SYNTHETIC and the section header says so, with the reason. A fixture that quietly stood in for a real population would be the staged-break-substitutes-a-synthetic-value class.
- AC8 — `tools/lexicon/selftest.py` — the arity arms — non-vacuous, proven by widening the extractor's tuple and watching them red.
- AC9 — `tools/lexicon/selftest.py` — both pin rows pasted blank-separated — green, and each row reds on its OWN count with the other left alone, so nothing is folded into the parent.

**Evidences:** TOOL-aSurfacedLexicon-7
- AC1 — a name whose leading token the canon holds — `--suggest` answers with the canon's spelling and says which it rejected.
- AC2 — `python tools/lexicon/lexicon.py --suggest` — two more of the same shape — both answered, both naming the source of the ruling.
- AC3 — `tools/lexicon/selftest.py` — a token where the DECLARATION and the CANON disagree — the precedence rule decides it, and the criterion is keyed on a token where they actually differ. Its first spelling tested one where both agree, so it could not fail.
- AC4 — `python tools/lexicon/lexicon.py --check` — one run against a scratch declaration — the four rows reconcile as an identity between readings taken in that ONE run, with no literal in the criterion.
- AC5 — `tools/lexicon/selftest.py` — a DEBT-leading definition staged — RED naming the file, the line and the replacement identifier rather than only the verb.
- AC6 — `tools/lexicon/selftest.py` — an UNRULED-leading definition staged — RED with a textually distinct message and no replacement proposed, because a name no cluster holds is a scoping question rather than a spelling one.
- AC7 — `--measure` emits the four rows blank-separated — verified on the raw lines rather than by eye.
- AC8 — `tools/lexicon/selftest.py` — every canon key classifies DEBT and an absent token UNRULED — reverting the classifier reds it.
- AC9 — `tools/lexicon/selftest.py` — a rename from one class to the other — RED against the pasted pins, in both directions, while the corpus offender TOTAL is unchanged and the same rename under the single scalar exits 0.

## What the revert matrix found, and why it is the rule this build keeps re-learning

**One mechanism was ungated.** The shell tokenizer's end-of-source refusal for an unterminated
heredoc — reverted, and the entire suite stayed green. The pre-existing arm for unterminated heredocs
did not reach it, because an opener followed by a newline is refused earlier by the body-drain loop.
The arm that now covers it uses the one construct the tail raise owns: a heredoc opened on the FINAL
line with no newline after it.

**Two arms were weak rather than absent**, which is worse, because both had been reported satisfied.
One asserted a census figure "cannot rot" by searching the whole declaration for the digits — and the
digits appeared elsewhere in the file, so falsifying the row left it green. It now reads each figure
from the row that owns it.

**And the stale-figure class recurred for the seventh time.** The previous pass corrected six numbers
written in prose beside the code they describe; this pass's own diff ADDED four more, including two
readings of one measurement that contradicted each other in two different files, from a refinement
that was never committed and therefore could not be re-derived by anyone. They are DELETED rather
than corrected. A figure whose only job is to make a sentence feel measured is a liability with no
consumer; a figure that decides something keeps its command beside it.
