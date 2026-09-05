# TOOL-aSurfacedLexicon-14 — a real shell parser, arming the shell function cell

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Extract shell function definitions with a parser rather than a line regex, so the shell function cell
can be armed. Shell is 79 of the 80 unarmed definition-carrying files in this tree, which makes it the
largest coverage gain available in this rebuild, and a regex probe cannot buy it: the naive probe
miscounts in BOTH directions on this corpus, which is worse than the floor the shipped declaration
already refuses.

## 2. Scope (IN)

- **S1** — a shell definition parser inside `tools/lexicon/lexicon.py`, beside `_python_defs` and
  `_probe_defs`, reached through a third `mode` arm in `extract_text` at
  `tools/lexicon/lexicon.py:256`. The `(functions, types, imports)` return shape is unchanged.
- **S2** — the parser's scope, DECLARED in its own header: which shell constructs it reads, which it
  refuses, and what it returns for a file it cannot tokenize. A structural extractor reads as a
  complete one to everybody who did not write it.
- **S3** — the `LANGS` row for shell moves from `dark` to the parser mode, and the shell function cell
  is declared with its convention and its pin row.
- **S4** — the parser's own liveness: a frozen sentinel fixture yielding a non-zero definition count,
  matching the standing requirement on every shipped pattern set at `tools/lexicon/lexicon.py:107`,
  so a parser that goes inert fails in the kit's own suite rather than reporting a clean corpus.
- **S5** — a DEAD PROBE arm over the newly armed language, so a parser reading zero definitions across
  a corpus that contains 89 tracked shell files reds rather than passing green.
- **S6** — the `ratified` stamp is re-written in the SAME commit as the `LANGS` edit, because the
  drift-audit signal compares the stamp's date against the commit date of the last change to that
  declaration and reds otherwise.
- **S7** — a pre-wiring run of the parser over the whole tree, printing hits AND near-misses, before
  the cell is armed. The measured evidence in section 4 says why this is not optional here.

## 3. Non-goals (OUT)

- Grading shell FILENAMES. That cell is armed already and its four violations are a `TOOL-aSurfacedLexicon-5`
  concern, not this unit's.
- Shell type names and shell imports. Shell has neither in any sense this kit grades; the parser
  returns empty lists for both and the declaration carries no type cell, which is a refusal rather
  than an omission.
- The two extensionless bash files. Section 8 carries that fork and the recommendation is that they
  stay unreached with the report saying so.
- A general shell interpreter, an expansion engine, or anything that runs what it reads. The parser
  tokenizes and locates; it never evaluates.
- Alias, `eval` and `source` resolution. A definition constructed at runtime is out of reach of any
  static extractor and pretending otherwise is the same green-by-absence claim this unit exists to
  refuse.

**The deferral risk, said plainly, because the owner ruling asks for it.** This is the unit most
likely not to be built: it is the only one in the rebuild whose cost is a new parser rather than a new
declaration, and its whole value arrives at the end. It carries `order 4`, alongside
`TOOL-aSurfacedLexicon-6` and `TOOL-aSurfacedLexicon-13`, deliberately ahead of the conf rewrite. If
it has not landed by the time that rewrite lands, shell stays `dark`, the shipped conf comment records
owner ruling Q5 as OWED rather than done, and the build's wrap-up says the largest coverage gain was
not taken. It does not quietly become a regex.

## 4. Design

### Why a regex probe is refused, measured on this corpus rather than argued

The research record reports 581 shell definitions from a naive probe over the 89 tracked `.sh` files
and calls that number a FLOOR. Re-measured on this worktree at `d0a18683` on 2026-09-04, the probe is
wrong in both directions and the over-count half is new.

| Reading | Result |
|---|---|
| Naive same-line regex over 89 tracked shell files | 581 matches, 0.06 s |
| The same regex over 91 files, adding the two extensionless bash scripts | 582 matches |
| Of those, matches inside a heredoc BODY | 1 confirmed |
| A heredoc-aware refinement of the same regex | 570 matches |
| Real definitions the refinement LOST | 11 |

The confirmed over-count is `tools/hooks/agent-cap.test.sh:1187`, a JavaScript `function f() { … }`
inside a bash heredoc, which the line regex reports as a shell function definition. The 11 lost
definitions are all in `tools/memory-tree/merge-rows.test.sh`: line 287 of that file carries a grep
pattern containing seven literal `<` characters, which the heredoc-aware pass read as a heredoc opener
whose terminator never arrives, so it swallowed every definition below it.

That is the whole argument in one paragraph. Two hand-rolled regex passes over the same 91 files
disagreed by 12 definitions, and each was wrong in a way the other was not. A number a second regex
moves by 2% is not a population, and reporting it as one is the class the shipped `sh::dark`
declaration was written to refuse.

### What the parser reads

Tokenization with quoting and redirection state, not line matching. It tracks single quotes, double
quotes, dollar-single quotes, backslash escapes, comments, command substitution nesting, heredocs with
both quoted and unquoted delimiters and both the plain and dash-stripped forms, and here-strings —
which is the construct that defeated the refinement above, because `<<<` and a literal run of `<` are
indistinguishable to a line regex and trivially distinguishable to a tokenizer.

It recognises three definition forms: the POSIX `name() { … }`, the bash `function name { … }`, and
the combined `function name() { … }`. It recognises a subshell body, `name() ( … )`. It records a
definition's name and its line, which is exactly what the return contract carries.

### What the parser refuses, and how

Three refusals, each named on the run rather than swallowed.

A file it cannot tokenize RAISES, matching the contract `_python_defs` already documents at
`tools/lexicon/lexicon.py:211` — an unparseable file under an armed declaration is a broken corpus,
and returning an empty list would launder it into a clean run. The run reports the file and the
position it gave up at.

A definition constructed by `eval`, or produced by sourcing another file, is NOT found and the
parser's header says so. The sourced file's definitions are extracted where they are written, which is
the correct answer; a name that only exists after a runtime expansion has no definition site to grade.

A definition inside a heredoc body is not a definition and is not returned. This is the one refusal
with a confirmed live instance in this tree, named above.

### The declaration moves, and what that trips

Shell moves from `dark` to the parser mode. `tools/drift-audit/drift_report.py:259` ranks the modes
with the parser above the probe above dark, and `build_lang_mode_findings` skips any move whose new
rank is at or above its old one, so this is a strengthening move and owes no justification marker. A
later revert to dark would owe one, which is the ratchet working.

The same edit does trip `signal_lexicon_ratified_stale` at
`tools/drift-audit/drift_report.py:846`. That signal compares the ratification stamp's date against
the commit date of the last commit touching the declaration line, and the stamp currently reads a date
in August. The `drift-audit records` leg carries no guard and runs on every bar, so an unrestamped
`LANGS` edit reds the push bar rather than drifting quietly. S6 is that re-stamp, in the same commit.

### Inventory — the population this arms

Measured on this worktree at `d0a18683` on 2026-09-04, through the kit's own sniffer and extractor.

| Fact | Value |
|---|---|
| Tracked shell files by extension | 89 |
| Definition-carrying files the sniffer finds and no armed extractor reads | 80 |
| Of those, shell by extension | 79 |
| Of those, extensionless bash | 1, at `.githooks/pre-commit` |
| Armed share of definition-carrying files today | 58 of 138 |

The one extensionless carrier is why section 8's first fork exists: the extension key for a file with
no dot in its basename is a distinct declared language, so an extension-keyed shell cell reaches 79 of
the 80 and the eightieth stays dark under a different row.

### Files touched (estimate)

`tools/lexicon/lexicon.py` for the parser, the mode arm and the DEAD PROBE coverage,
`tools/lexicon/selftest.py` for the sentinel fixture and the construct table, `.lexicon.conf` for the
`LANGS` move, the cell row, the pin row and the re-stamp. No new module, for the reason the research
record gives: `govkit update` classifies by iterating the receipt, so a file gov newly ships is
outside the classification space, and that shape killed every entry point of the recorded adopter for
six days.

### Alternatives rejected

Arming a regex probe. Rejected on the measurement above, which is this unit's whole justification.

Leaving shell dark. Rejected by owner ruling Q5, which chose the parser over both the probe and the
status quo, and which the rulings record notes is the same posture as the status quo until this unit
actually lands — a commitment, not an outcome.

Detecting shell by shebang instead of by extension. Rejected here and carried as section 8's first
fork: a shebang read is a second population selector over the corpus, and the coverage sniffer's own
header at `tools/lexicon/lexicon.py:123` is the standing argument for why a second reading of the
corpus is where a denominator goes wrong.

## 5. Production-readiness checklist

- security — the parser reads tracked source and never evaluates it. It has no eval path, no
  subprocess and no network; the one hazard a shell reader could have is the one it structurally
  does not take.
- perf / scale — the naive regex covers 91 files in 0.06 s and a tokenizer is a constant factor above
  that, so the leg cost is expected to stay far under the 300 s ceiling `tools/gate-legs.json`
  declares for `lexicon naming predicates`. ESTIMATE: the parser does not exist yet and the landing
  run must measure it.
- a11y — N/A. A CLI gate with no user interface.
- i18n — the parser reads bytes and reports names verbatim, so a non-ASCII function name is returned
  intact. Whether the VOCABULARY predicate then grades it correctly is review finding D25 against
  `subtokens.py`, which this unit inherits and does not widen.
- error / empty / loading states — an untokenizable file raises and names its position; a zero
  population over a corpus containing shell reds as DEAD PROBE; a sentinel fixture that stops yielding
  definitions reds in the kit's suite.
- observability — the shell cell appears in the per-cell report from `TOOL-aSurfacedLexicon-6` with
  its count, its denominator and its rule, and the coverage fraction moves from 58 of 138 upward on
  the same run, which is the number this unit exists to move.
- risks — the sharp one is a false refusal: a hand-written parser meeting a legal shell file it cannot
  tokenize reds the bar on correct work. S7's pre-wiring run over the whole tree, printing hits and
  near-misses, is the mitigation and it is the charter's own rule rather than a local invention.
- testing + left-shift gates — a construct table in `tools/lexicon/selftest.py` with one arm per
  recognised form and one per refusal, the frozen sentinel of S4, and the two live miscount instances
  from section 4 pinned as fixtures so a future regex shortcut cannot pass.
- migration / rollback — the conf edit is the whole migration and reverting the commit reverts it.
  Reverting AFTER a landing does owe a mode-ratchet justification marker, because parser back to dark
  is a weakening move, and that is a property of the ratchet rather than a defect of this unit.
- user docs — `tools/lexicon/README.md` gains the parser's declared scope and its three refusals, and
  the coverage-mode table gains the row. The `lexicon wiring` leg's byte-compare forces the Skill
  re-render if the placeholder set moved.

## 6. Acceptance criteria

- **AC1** — When the parser runs over the 91 tracked shell-language files with the cell armed,
  `python tools/lexicon/lexicon.py --check` reports a shell function population and its count differs
  from the naive regex's 582 in a direction the parser's header explains. A count equal to the naive
  regex's is a finding, not a pass, because the two readings are known to disagree in this tree.
- **AC2** — When the parser reads `tools/hooks/agent-cap.test.sh`, the JavaScript function inside the
  heredoc at line 1187 is NOT returned as a shell definition, asserted by a
  `python tools/lexicon/selftest.py` arm keyed on that construct rather than on that file's line
  number.
- **AC3** — When the parser reads `tools/memory-tree/merge-rows.test.sh`, it returns the definitions
  below the grep pattern on line 287 that a heredoc-aware line regex loses, asserted by a
  `python tools/lexicon/selftest.py` arm. This is the second live miscount instance and the two
  together are why the parser exists.
- **AC4** — When the shell extractor is broken so it returns no definition for any file,
  `python tools/lexicon/lexicon.py --check` reds naming DEAD PROBE for the shell language rather than
  exiting `0` with a higher coverage percentage. The break is staged, the RED observed, and the break
  unstaged.
- **AC5** — When the frozen sentinel fixture is edited so it yields zero definitions,
  `python tools/lexicon/selftest.py` reds naming the sentinel; restoring it greens. This is the arm
  that tells an inert parser apart from a corpus with nothing to find, which a single tree cannot.
- **AC6** — When a file of unparseable shell is staged under the armed declaration,
  `python tools/lexicon/lexicon.py --check` REFUSES naming the file and the position, and does not
  report an empty definition list for it.
- **AC7** — When the `LANGS` shell mode is edited without re-stamping `ratified` in `.lexicon.conf`,
  `python tools/drift-audit/drift_report.py --check` reds naming the stale ratification; with the
  re-stamp in the same commit it greens. Both halves observed, because the green half alone cannot
  fail.
- **AC8** — When `python tools/lexicon/lexicon.py --check` runs after landing, the coverage line
  reports an armed share above the pre-change reading of 58 of 138 definition-carrying files, and the
  unarmed remainder it names is the extensionless carrier at `.githooks/pre-commit` plus whatever
  section 8's first fork left unreached.
- **AC9** — When the parser is run over the whole tree BEFORE the cell is armed, its hits and its
  near-misses are printed by `python tools/lexicon/lexicon.py --measure` and recorded in this build's
  record, and the record names what the run caught that this spec did not predict. A wiring commit
  with no such record fails this criterion.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `drift-audit records` · `memory hygiene`

`drift-audit records` is named because the declaration move trips a signal on that leg, and that leg
carries no guard so it fires on every bar. This unit adds no gate leg and therefore owes no wall-clock
ceiling row and no `testsuite-count-waivers.txt` entry; it adds arms to `lexicon selftest`, whose
declared ceiling is 880 s and whose current cost is UNVERIFIED here — the rebuild research pass
recorded that it did not run that leg and that the figure circulating for it should not be quoted.

## 8. Open questions

- **F1 — does the shell cell reach the two extensionless bash scripts, or stop at the extension?**
  Both `.githooks/pre-commit` and `.githooks/pre-push` are bash, both carry the same shebang, and one
  of them is a definition carrier — the eightieth of the 80 unarmed carriers. Reaching them needs a
  shebang read, which is a second population selector over the corpus and is the thing the coverage
  sniffer's header argues against. Recommendation: stop at the extension, and have the run NAME the
  unreached carrier rather than let it vanish into the denominator. A shebang-keyed language axis is a
  `LANGS` grammar change and belongs with `TOOL-aSurfacedLexicon-9`, which is already widening that
  grammar.
- **F2 — does an untokenizable file raise, or degrade to a reported skip?** Raising matches the
  contract `_python_defs` documents and keeps a broken corpus from laundering into a clean run.
  Against it: Python has a formal grammar and shell does not, so a hand parser will meet legal files
  it cannot read, and each one reds the bar until somebody fixes the parser. Recommendation: raise,
  because the alternative is a per-file silent zero that is indistinguishable from a file with no
  definitions — and pair it with S7's pre-wiring run, so the population of such files is KNOWN before
  the cell is armed rather than discovered by a red bar.
- **F3 — arm the shell function cell at all?** The research record recommended no: stay dark, keep the
  filename cell armed, and re-take the question deliberately if a real parser is ever wanted.
  RESOLVED (owner, 2026-09-04): arm it, but only behind a real shell parser — the probe is refused in
  both directions. Recorded in the build's owner-rulings record as Q5, which also records that this is
  the unit most at risk of indefinite deferral and that the build must sequence it early or say
  plainly that it will not ship.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, from owner ruling Q5, and from a re-measurement of the naive
  probe that found it over-counts as well as under-counts on this corpus, which the research record
  did not report.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "parse shell script source to extract function
definitions"` ranks `extract` in `tools/lexicon/lexicon.py` at fan-in 7 as a seam, with `extract_text`
beside it, and that IS the seam this unit extends: the mode dispatch there already routes `dark` to
nothing and the parser mode to a real parse, and this unit adds the third arm without changing the
return shape that `drift-audit` derives both operands of its marginal-offense-rate signal from. The
probe also surfaced `scan_js_definitions` in `tools/codebase-map/map_lib.py`, which is NOT reusable
here and is the precedent that decides the question rather than the code: that file refuses to ship a
regex extractor for shell and declares the language dark instead, and this unit is the first thing in
either kit that clears the bar that refusal set. `resolve_shell_argv` in `tools/govkit/govkit.py`
resolves an interpreter to run a script and shares only the word.

Recall terms used: `python tools/memory-recall/query.py "why is shell declared dark in the lexicon and
what would a real shell parser have to do before sh.function could be armed" --terms "lexicon sh dark
shell function definition regex probe floor green-by-absence coverage sniffer parser heredoc
extractor" --k 8`.
