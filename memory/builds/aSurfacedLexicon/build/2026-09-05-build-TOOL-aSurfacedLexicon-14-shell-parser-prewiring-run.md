**Serves:** journal TOOL-aSurfacedLexicon-14

# Build pass, order 4 — the shell parser, and the pre-wiring run that had to precede arming it

Node `a` · 2026-09-05 · build `aSurfacedLexicon` · streams tooling. One unit. The largest coverage
gain in the rebuild and the largest single pin movement: the armed share of definition-carrying
files goes from 57 of 141 to 140 of 141, and `VERB_OFFENDER_PIN` goes from 461 to 968.

## S7 — the pre-wiring run, over the whole tree, before the cell was armed

Run by a direct call on `parse_shell_defs` from the working tree with the declaration still reading
`sh::dark`, because no shipped mode can reach a dark language: `extract_text` returns `None` for one
before either `--check` or `--measure` sees a byte of it. The run below is against the SHIPPED
parser, re-run after the last fix landed, so its figures are the landed code's and not a draft's.

| Reading | Value |
|---|---|
| Tracked `.sh` files the run covered | 94 |
| HITS — definitions returned | 607, in 81 files |
| The naive same-line pattern over the same list, in the same run | 608 |
| NEAR-MISSES — reached and declined | 72, in 26 files |
| Files the tokenizer could not read | 0 |

A near-miss is a construct the tokenizer REACHED and DECLINED, reported with its file, its line and
the reason. They fall into three populations and no others:

- **30 `eval`/`source` constructions in 22 files.** Out of reach of any static extractor by
  construction; the parser's header says so rather than reporting them as absent.
- **41 `word ( )` token runs in 7 files whose word is not a legal function name.** Every one is an
  array assignment — `names=()`, `SPEC_ID=()`, `WAIVE_REASONS=()`. A same-line regex declines these
  too, because its own name class refuses a trailing `=`; the tokenizer declines them for the same
  reason and reports the decline rather than dropping it.
- **1 construct the naive pattern claimed and the parser declined**, and it is the confirmed live
  over-count this unit was written for: `tools/hooks/agent-cap.test.sh`, a JavaScript
  `function f() { return 'parallel (nope)' }` inside a `<<'EOF'` bash heredoc body.

**What the run caught that the spec did not predict**, which is the half of AC9 that earns it:

1. **Zero untokenizable files, after three fixes that the spec's risk section anticipated in kind
   but not in number.** F2 chose RAISE over a reported skip precisely because a hand parser would
   meet legal shell it could not read, and it was right three times before it was wrong none:
   `tools/check-kit-versions.sh` raised on an unterminated `"` under the first draft, and
   `tools/memory-tree/merge-rows.test.sh` raised under the second. Both were the SAME defect seen
   from opposite sides — a command substitution inside a double-quoted string — and the two obvious
   fixes are opposite. Not counting parentheses inside the string closed it early on
   `"$(sed "1s/^x*()/y()/")"` and cost four definitions; counting them closed it early on
   `"$(… sed -n 's/.*FAILED (\(.*\))/\1/p')"` and cost twenty. What works is neither: the string
   state is SUSPENDED across `$(` and restored by the `)` that closes it, because a substitution's
   body is code and not string. Both spellings are pinned as selftest fixtures.
2. **The parser's population is 607 and the naive pattern's is 608, and the difference is exactly
   one name.** The spec expected the parser to find things the regex could not — a body opening on
   a later line, a `name() ( … )` subshell — and this corpus contains none of either. The whole
   difference is the heredoc the regex should not have counted. The spec's `508` upper bound on the
   pin therefore lands at 507, one name lower, for exactly that reason.
3. **The explicit `<<<` here-string branch was deleted rather than shipped.** Reverting it changed
   not one token in the corpus: `<` is already a word break, so a here-string reaches the heredoc
   arm with an empty delimiter and queues nothing. A branch whose removal reds nothing is an
   assertion about nothing, which is this build's own rule applied to its own diff.

## The two live miscount instances, both pinned as fixtures

`tools/hooks/agent-cap.test.sh` — the naive pattern's OVER-count, above. Not returned.

`tools/memory-tree/merge-rows.test.sh` — the heredoc-aware refinement's UNDER-count. The grep
pattern `'^<<<<<<< ours$'` is read by that refinement as an opener whose terminator never arrives,
blanking every line below it. The parser returns all ten definitions the refinement loses, from
`mkscratch` down to `sab`, because the run of `<` is inside single quotes and a tokenizer never
enters the branch. Both are asserted by fixtures keyed on the CONSTRUCT, never on a line in a
tracked file: both of these instances moved line while this spec was being audited.

## Evidences

**Evidences:** TOOL-aSurfacedLexicon-14

- **AC1** — `607` from the parser against `608` from the naive pattern, both taken in the run
  above over the same 94-file `git ls-files '*.sh'` list. They differ, and the direction is the one the parser's header
  explains: it declines a definition-shaped line inside a heredoc body.
- **AC2** — `python tools/lexicon/selftest.py` arm *"shell: a definition inside a heredoc BODY is not
  returned (AC2's construct)"*. Reverting the heredoc drain reds it, printing
  `[('real_one', 1), ('f', 3), ('heredoc_body_def', 4)]`.
- **AC3** — arm *"shell: a quoted run of `<` is not a heredoc opener, and the TEN definitions below
  it survive"*. Discharged over the CONSTRUCT rather than by reading the tracked sibling: a kit
  self-test that reads a file only this repo happens to track is a test no adopter has the fixture
  for. The tracked instance is measured in the S7 run above.
- **AC4** — the shell extractor forced to return nothing. `--check` reds with
  `DEAD PROBE — .sh is declared 'parser' (shell-tokens) and the corpus contains it, but the
  extractor found NO definitions`. Restored, green.
- **AC5** — the frozen `SHELL_SENTINEL` edited so its first form is commented out. `selftest.py`
  reds naming *"shell sentinel: the frozen fixture yields a non-zero definition count"*. Restored,
  green at 281 arms.
- **AC6** — a fixture repo carrying `core/broken.sh` with an unterminated quote under an armed
  declaration. `--check` exits 1 with
  `core/broken.sh: declared 'parser' but does not parse: unterminated ' quote opened at line 2`,
  and reports no empty definition list for it.
- **AC7** — `signal_lexicon_ratified_stale` is NOT OBSERVABLE IN A WORKING TREE, and this is a
  divergence rather than a pass. It compares the stamp against the COMMIT DATE of the last commit
  touching the `LANGS` line, so an uncommitted `LANGS` edit moves it not at all: the signal reads
  `lexicon_ratified_older_than_language_surface 0 of 1 ok (pin 0)` both with the re-stamp and with
  it reverted to `2026-08-24 node d`. The re-stamp is written and rides in the same change, which is
  what S6 asks for; the criterion's red half can only be observed after the commit exists.
- **AC8** — coverage moves `armed 57 of 141 (40.4%)` to `armed 140 of 141 (99.3%)` across one
  landing. Numerator +83, which is the count of tracked `.sh` definition carriers; denominator
  unchanged at 141. The unarmed remainder is exactly one file and the run names it:
  `.githooks/pre-commit`, the extensionless bash carrier F1 rules the extension key out of reach of.
- **AC9** — this record, from `python tools/lexicon/lexicon.py`'s own `parse_shell_defs` over
  the 94-file list, with the file count, the hit count, the near-miss count under S7's
  definition of the term, and the three things the run caught that this spec did not predict.
- **AC10** — the header of `parse_shell_defs` enumerates the four forms, the three refusals and what
  it returns for a file it cannot tokenize, asserted by eight arms in `test_shell_refusals` against
  the shipped docstring rather than against the README.
- **AC11** — `--check` prints `sh.function.conv 6 of 607 against snake`, with
  `violation 4, ambiguous 2, teeth camel=295 kebab=295 pascal=603 screaming=603`. The pin value was read off the run and
  pasted. RED half: renaming `render_skill` to `GITX` in `tools/lexicon/adopt-lexicon.sh` moves the
  cell to 7 and reds `sh.function.conv 7 against declared pin 6`, naming the file, the line and the
  name. Restored, green.
- **AC12** — `grep -n VERB_OFFENDER_PIN .lexicon.conf` read `461` before the `LANGS` edit. Staging
  the edit WITHOUT the raise reds `lexicon: verb offenders 968 over pin 461`. With the raise the
  conf reads `968` and equals the count exactly. The contribution is +507 and the spec budgeted an
  upper bound of 508, which is the one heredoc name the parser declines.

## What the arming cost, measured rather than predicted

| Figure | Before | After | Command |
|---|---|---|---|
| `P1 verb graded` | 1049 | 1665 | `python tools/lexicon/lexicon.py --check` |
| `P1 verb offenders` | 461 | 968 | same |
| coverage, armed of carriers | 57 of 141 | 140 of 141 | same |
| `lexicon selftest` arms | 251 | 281 | `python tools/lexicon/selftest.py` |

The six identifiers this unit mints in `tools/lexicon/lexicon.py` cost ZERO offenders, measured with
the parser in place and shell still dark: `graded` moved 1049 to 1055 and `offenders` did not move
off 461. `parse_shell_defs`, `scan_shell_tokens`, `add_word`, `add_char`, `read_quoted` and
`read_braced` each answer `OK` from `python tools/lexicon/lexicon.py --suggest`, as do the three
selftest arms `test_shell_constructs`, `test_shell_refusals` and `test_shell_sentinel`. The spec
budgeted five names; the tokenizer's four nested helpers are graded too, because `_python_defs`
walks the whole AST rather than the module body, and all four lead with a declared verb.

## The declaration this unit lands

`sh::dark` becomes `sh:shell-tokens:parser`, and the mode token is deliberately the EXISTING
`parser` rather than a new one. A fresh mode name was the other available shape and it is refused:
`LANG_MODE_RANK` in `drift_report.py` reads an unknown mode as ABSENT at rank -1, so a language
moving from `dark` at rank 0 to a freshly named mode would score as a WEAKENING and fire a ratchet
finding on the strongest edit this declaration has ever made. The third extractor arm therefore
keys on the pattern-set id, which is what that field has always been for, and a `parser` row naming
an id this kit does not ship is a named refusal rather than a silent fallthrough to Python.

`CELLS: sh.function snake` with `PINS: sh.function.conv 6` is this declaration's first armed cell.
The convention was fixed in the spec, in prose, before any shell name had been counted, and its
source is the Google Shell Style Guide's Function Names rule — prescriptive, external to this tree,
older than every file it grades. The corpus is evidence for one thing only: six names of 607 sit
outside it, so the external rule and this repo were never in conflict.
