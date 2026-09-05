# The closing review's round 2, folded — and what it says about this build

**Serves:** journal TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3

## The finding worth leading with

**The round-1 fold made `tools/hooks/agent-cap.js` WORSE than it was before this build.** Fixing four
false-DENY findings traded them for four fail-OPEN bound escapes: five one-line legal-JavaScript
mutations that the pre-fold tree DENIED were ADMITTED after it, each one letting an unbounded
agent-per-item fan past the only mechanical enforcement of the review protocol's cap.

**And the suite was 196 passed, 0 failed while that was true.** Every arm the first fold added pins
the exact script a review reported; none pinned the class. A green leg over a broken control is the
shape this repo's own charter names, and it happened here, in the file that enforces the cap.

## What was wrong, and what each fix is

| # | Defect | Fix |
|---|---|---|
| R1 | the growth sweep read `renderBlankedLiterals`, whose `tmpl` arm ERASES `${…}` bodies, so a real ``const s = `${LENSES.push(x)}` `` was invisible | a view built here: the lexed view with block comments stripped over the joined text and line comments per line — comments gone, interpolation bodies KEPT |
| R2 | the left guard `[^.\w$)\]]` leaked twice from one regex: it excluded `)`/`]` so `if (x) LENSES.push(y)` never matched, and it CONSUMES, so under `/g` a receiver after a previous match's `(` was unreachable | the zero-width `(?<![.\w$])` this file already uses in `offendingLines` |
| R3 | the splice guard resolved its line by VALUE (`indexOf(l)`), so two identical splice lines graded the later against the earlier | the free `forEach` index |
| R4 | splice arity counted top-level commas and could not see a SPREAD, so `LENSES.splice(...more)` read as a shrink | a spread is growth, which the marked-branch veto forty lines above already says |
| R5 | the fold recommitted all 1767 lines as CRLF with one LONE CR, so `git ls-files --eol` reported `i/-text` — git treated the hook as BINARY, and it ships verbatim to adopters | normalized to LF, and `tools/hooks/*.js text eol=lf` added to `.gitattributes` beside the `tools/workflows/*.js` pin that already existed |
| R6 | the comment-free view went to the growth sweep only; the reassignment sweep still read the un-blanked one | both sweeps read `takeBackView` |

## The measurement, both directions

Each case run against the pre-fold blob (`cd51decd`), the broken fold (`15d92203`) and this tree.

| case | pre-fold | broken | now | wanted |
|---|---|---|---|---|
| growth in a `${…}` interpolation | 2 | **0** | 2 | deny |
| growth after `if (x)` | 2 | 2 | 2 | deny |
| growth nested in another call | 2 | **0** | 2 | deny |
| `splice(...more)` | 2 | **0** | 2 | deny |
| block comment naming a push | **2** | 0 | 0 | allow |
| member chain `state.lenses.push` | **2** | 0 | 0 | allow |
| removal-only `splice(0, 2)` | **2** | 0 | 0 | allow |

Bold is wrong. The fixes hold in both directions at once, which is the thing neither earlier state did.

## R7 — the gate that would have caught all four, and now does

A FROZEN DENY CORPUS: one growth, spelled ten ways legal JavaScript allows, every one of which must
deny. Three of the four blockers exit 0 against the broken blob and 2 against this one, so the corpus
is a gate whose failing case has been OBSERVED rather than assumed.

Adding a spelling is one line. A view change or a regex tightening that blinds any of them reds. That
is the difference between gating an instance and gating a class, and it is the durable output of this
round — more than any individual fix above.

## Suites after the fold

`agent-cap` **206 passed, 0 failed** · `check-wiring` **92 passed, 0 failed** · `govkit selftest` all
arms held · `corpus_ids --selftest` PASS · every reader `--check` rc 0 · `check-wiring.sh --check`
rc 0 · all five shipped harnesses still exit 0.
