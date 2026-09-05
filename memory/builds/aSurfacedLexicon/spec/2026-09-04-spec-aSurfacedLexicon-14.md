# TOOL-aSurfacedLexicon-14 — a real shell parser, arming the shell function cell

**Status:** CLOSED · rev-4 · 2026-09-05 · node a · Tier-2 · base 6c670b02 · streams tooling · order 4 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-aSurfacedLexicon-14-shell-parser-prewiring-run.md](../build/2026-09-05-build-TOOL-aSurfacedLexicon-14-shell-parser-prewiring-run.md) | journal | — |
| [2026-09-05-build-TOOL-aSurfacedLexicon-6-acceptance-ledger.md](../build/2026-09-05-build-TOOL-aSurfacedLexicon-6-acceptance-ledger.md) | journal | TOOL-aSurfacedLexicon-6 TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-7 |
| [2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-7 |
| [2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round2.md) | spec-audit | TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-7 |

<!-- /gen:spec-records -->

## 1. Goal

Extract shell function definitions with a parser rather than a line regex, so the shell function cell
can be armed. Shell is 83 of the 84 unarmed definition-carrying files in this tree, which makes it the
largest coverage gain available in this rebuild, and a regex probe cannot buy it: the naive probe
miscounts in BOTH directions on this corpus, which is worse than the floor the shipped declaration
already refuses.

That gain is not free and rev-2 states the price in the goal rather than burying it in section 5.
Arming the language puts 608 shell function names in front of the P1 verb predicate, of which 508
occurrences lead with a token the declared table does not carry, so this unit raises
`VERB_OFFENDER_PIN` by up to 508 — more than doubling it. That is the NAIVE pattern's figure and
therefore an upper bound the parser is committed to beating; §4 says why. The measurement, the command and the
RAISED-by-name form are `### The pins this unit moves` in section 4, and S8 is the raise.

## 2. Scope (IN)

- **S1** — a shell definition parser inside `tools/lexicon/lexicon.py`, beside `_python_defs` and
  `_probe_defs`, reached through a third `mode` arm in `extract_text` at
  `tools/lexicon/lexicon.py:256`. The `(functions, types, imports)` return shape is unchanged.
- **S2** — the parser's scope, DECLARED in its own header: which shell constructs it reads, which it
  refuses, and what it returns for a file it cannot tokenize. A structural extractor reads as a
  complete one to everybody who did not write it.
- **S3** — the `LANGS` row for shell moves from `dark` to the parser mode, and the shell function cell
  is declared as `sh.function snake` with its `sh.function.conv` pin row. The convention token is
  `snake`, it is fixed by section 4's `### The rule the shell function cell grades by` BEFORE the
  parser runs, and its source is a prescriptive style guide outside this tree. The pin VALUE is
  emitted by the measurement path and pasted, never typed.
- **S4** — the parser's own liveness: a frozen sentinel fixture yielding a non-zero definition count,
  matching the standing requirement on every shipped pattern set at `tools/lexicon/lexicon.py:107`,
  so a parser that goes inert fails in the kit's own suite rather than reporting a clean corpus.
- **S5** — a DEAD PROBE arm over the newly armed language, so a parser reading zero definitions across
  a corpus that contains 94 tracked shell files reds rather than passing green. The denominator is
  `git ls-files '*.sh' | wc -l`, which returns 94 at this base.
- **S6** — the `ratified` stamp is re-written in the SAME commit as the `LANGS` edit, because the
  drift-audit signal compares the stamp's date against the commit date of the last change to that
  declaration and reds otherwise.
- **S7** — a pre-wiring run of the parser over the whole tree, printing hits AND near-misses, before
  the cell is armed. The measured evidence in section 4 says why this is not optional here. **The
  surface is named rather than assumed, because rev-1 named a mode that cannot carry it.** No shipped
  mode can: `--measure` prints the three pins this conf produces, `--list` prints offenders, and both
  read shell through `extract_text`, which returns `None` for a `dark` language at
  `tools/lexicon/lexicon.py:272` — and shell is still `dark` at the moment this run has to happen.
  The run therefore calls the new function directly, from the working tree, with the declaration
  untouched:

  ```
  python -c "import sys,subprocess; sys.path.insert(0,'tools/lexicon'); import lexicon as L
  fs=[f for f in subprocess.run(['git','ls-files'],capture_output=True,text=True).stdout.split()
      if f.endswith('.sh')]
  for f in fs:
      print(f, L.parse_shell_defs(open(f,encoding='utf-8',errors='replace').read()))"
  ```

  **A NEAR-MISS, defined here because a criterion cannot observe an undefined term:** a construct the
  tokenizer REACHED and DECLINED, reported with the file, the line and the reason it declined — a
  heredoc body, an `eval`, a `source`, or a token run it could not resolve to a definition form. A
  hit is a returned `(name, line)` pair. The run reports both populations and their file counts, and
  the build record carries the output. Nothing is added to any shipped mode, so unit 3's standing
  rule that `--check` and `--measure` must not read refusals the other cannot is untouched.

- **S8** — the `VERB_OFFENDER_PIN` raise the arming costs, written in the conf's existing
  RAISED-by-name comment form, naming shell as the arrival and carrying the command that measured it.
  It is a scope item rather than a footnote because it is the largest single pin movement in the
  build and it lands in the same commit as the `LANGS` edit.

## 3. Non-goals (OUT)

- Grading shell FILENAMES. **Rev-1 said that cell "is armed already" and routed its violations to
  `TOOL-aSurfacedLexicon-5`; both halves were false and rev-2 retracts them.** The tracked
  `.lexicon.conf` carries no `CELLS` block at all, so `sh.file` is UNDECLARED and nothing grades it
  today — `python tools/lexicon/lexicon.py --check` reports three predicates and no filename cell.
  `TOOL-aSurfacedLexicon-5` does not own it either: that spec's files-touched table records "NO
  `CELLS` row: this unit arms nothing", and its `sh.file` figures are taken against a scratch
  declaration in a working tree. The first tracked `sh.file` row lands with the `CELLS` matrix of
  `TOOL-aSurfacedLexicon-12` at order 7. That count is not a single number this tree can report,
  because it turns on the stemming rule `TOOL-aSurfacedLexicon-5` forks on: measured here at 5 kebab
  violations of 94 under first-dot stemming and 53 under last-dot, by

  ```
  python -c "import re,subprocess
  fs=[f for f in subprocess.run(['git','ls-files'],capture_output=True,text=True).stdout.split()
      if f.endswith('.sh')]
  K=re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$'); b=lambda f: f.rsplit('/',1)[-1]
  print(sum(not K.match(b(f).split('.')[0]) for f in fs),
        sum(not K.match(b(f).rsplit('.',1)[0]) for f in fs), len(fs))"
  ```

  which prints `5 53 94`. This unit does not close any of it and claims no coverage there.
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
`TOOL-aSurfacedLexicon-6`, deliberately ahead of the conf rewrite —
`TOOL-aSurfacedLexicon-13` was at that order when this sentence was written and moved to order 5
during the same audit fold, which is why this now names one sibling and not two. If
it has not landed by the time that rewrite lands, shell stays `dark`, the shipped conf comment records
owner ruling Q5 as OWED rather than done, and the build's wrap-up says the largest coverage gain was
not taken. It does not quietly become a regex.

## 4. Design

### Why a regex probe is refused, measured on this corpus rather than argued

The research record reports 581 shell definitions from a naive probe over 89 tracked `.sh` files and
calls that number a FLOOR. **Rev-1 carried that 89 forward and every figure in this section rested on
it.** The tracked shell population is 94 — `git ls-files '*.sh' | wc -l` returns 94, and
`git ls-tree -r --name-only 6c670b02 | grep -c '\.sh$'` returns 94 too, so this was never a
HEAD-versus-BASE quibble. Re-measured on this worktree at `6c670b02` on 2026-09-05, with both
patterns QUOTED, because rev-1 reported results for regexes it never wrote down and no second party
could land on its numbers.

The naive same-line pattern, in full:

```
^[ \t]*(?:function[ \t]+)?([A-Za-z_][A-Za-z0-9_]*)[ \t]*\([ \t]*\)[ \t]*\{
|^[ \t]*function[ \t]+([A-Za-z_][A-Za-z0-9_]*)[ \t]*\{
```

The heredoc-aware refinement is that pattern run over a source with heredoc bodies blanked, where a
body opens on `<<-?[ \t]*["']?([A-Za-z_][A-Za-z0-9_]*)["']?` and closes on a line equal to the
captured delimiter. Both passes, `re.M`, over the tracked list:

| Reading | Result | Command |
|---|---|---|
| Naive pattern over the 94 tracked `.sh` files | 608 matches, 0.064 s | the snippet below |
| The same pattern over 96 files, adding the two extensionless bash scripts | 609 matches | same |
| Of those, matches inside a heredoc BODY | 1 confirmed, named below | inspection |
| The heredoc-aware refinement over the same 94 | 336 matches | same |
| Definitions the refinement LOST | 272 | same |

```
python - <<'PY'
import re, subprocess
from pathlib import Path
DEF = re.compile(r"^[ \t]*(?:function[ \t]+)?([A-Za-z_][A-Za-z0-9_]*)[ \t]*\([ \t]*\)[ \t]*\{"
                 r"|^[ \t]*function[ \t]+([A-Za-z_][A-Za-z0-9_]*)[ \t]*\{", re.M)
OPEN = re.compile(r"<<-?[ \t]*[\"']?([A-Za-z_][A-Za-z0-9_]*)[\"']?")
def strip_heredocs(src):
    out, term, dash = [], None, False
    for ln in src.split("\n"):
        if term is None:
            out.append(ln)
            m = OPEN.search(ln)
            if m:
                term, dash = m.group(1), "<<-" in ln
        else:
            out.append("")
            if (ln.strip() if dash else ln) == term:
                term = None
    return "\n".join(out)
fs = [f for f in subprocess.run(["git","ls-files"],capture_output=True,text=True).stdout.split()
      if f.endswith(".sh")]
naive = lost = 0
for f in fs:
    s = Path(f).read_text(encoding="utf-8", errors="replace")
    a = {(m.start(), m.group(1) or m.group(2)) for m in DEF.finditer(s)}
    b = {(m.start(), m.group(1) or m.group(2)) for m in DEF.finditer(strip_heredocs(s))}
    naive += len(a); lost += len(a - b)
print(len(fs), naive, naive - lost, lost)
PY
```

which prints `94 608 336 272`.

The confirmed over-count is `tools/hooks/agent-cap.test.sh:1211`, a JavaScript `function f() { … }`
inside a `<<'EOF'` bash heredoc, which the naive pattern reports as a shell function definition.
Rev-1 cited line 1187; the construct is the same and the line moved, which is why AC2 keys on the
construct.

The under-count is worse than rev-1 reported and reproduces exactly. In
`tools/memory-tree/merge-rows.test.sh`, line 291 carries the grep pattern `'^<<<<<<< ours$'`; the
opener regex finds `<< ours` inside that literal run of `<` characters, takes `ours` as a delimiter
whose terminator never arrives, and blanks every line below it — losing 10 real definitions from
`mkscratch` at line 293 down to `sab` at 1297. `tools/hooks/agent-cap.test.sh` loses 3 the same way,
of which one is the heredoc body it was right to drop and two — `msg` at 529 and `apay` at 678 — are
real. Across the corpus that shape costs 272 definitions.

That is the whole argument in one paragraph. Two hand-rolled regex passes over the same 94 files
disagreed by 272 definitions, 45% of the naive reading, and each was wrong in a way the other was
not. A number a second regex moves by half is not a population, and reporting it as one is the class
the shipped `sh::dark` declaration was written to refuse.

**Rev-1's 570 and 11 are retired rather than corrected.** They were produced by a refinement whose
pattern rev-1 did not record, so they are not reproducible from this document and no re-measure can
recover them. The two figures above replace them and carry their own snippet.

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

Measured on this worktree at `6c670b02` on 2026-09-05, through the kit's own sniffer and extractor.
Rev-1's whole table was taken at `d0a18683` and every row of it has moved.

| Fact | Value | Command |
|---|---|---|
| Tracked shell files by extension | 94 | `git ls-files '*.sh' \| wc -l` |
| Definition-carrying files the sniffer finds and no armed extractor reads | 84 | the snippet below |
| Of those, shell by extension | 83 | same |
| Of those, extensionless bash | 1, at `.githooks/pre-commit` | same |
| Armed share of definition-carrying files today | 57 of 141 | `lexicon.py --check` coverage line |

```
python -c "import sys, collections; sys.path.insert(0,'tools/lexicon')
import lexicon as L
from pathlib import Path
c = L.scan_definition_carriers(Path('.'), L.tracked_files(Path('.')))
u = [f for f in c if L.ext_of(f) not in {'py','js'}]
print(len(c), len(c)-len(u), len(u), collections.Counter(L.ext_of(f) for f in u))"
```

which prints `141 57 84 Counter({'sh': 83, '<none>': 1})`. The coverage line of `--check` reports
`armed 57 of 141 definition-carrying file(s) (40.4%)` on the same tree, so the two readings agree.

The one extensionless carrier is why section 8's first fork exists: the extension key for a file with
no dot in its basename is a distinct declared language, so an extension-keyed shell cell reaches 83 of
the 84 and the eighty-fourth stays dark under a different row.

### The rule the shell function cell grades by

**Rev-1 armed a cell and never said what it grades by.** The word `snake` did not appear in it, no
section named a convention, and no criterion observed one — which would have left the builder to
choose the standard while holding the parser's freshly measured output. That is the mirror shape this
build exists to refuse, arriving by omission rather than by intent, so the rule is fixed here, in
prose, before any shell name has been counted.

**The convention is `snake`.** Its source is the Google Shell Style Guide's Function Names rule —
lower case, with underscores separating words — which is prescriptive, external to this tree, and
predates every file it will grade. That is the whole justification, and it is deliberately not an
argument from what this corpus already does. `snake` is one of the six convention tokens
`tools/lexicon/subtokens.py` already ships, so the cell needs no new predicate.

The corpus is then evidence for exactly one thing: how far it currently sits from that rule. Measured
over the naive pattern's 608 names, with the leading-underscore strip the convention predicate
already applies:

```
python -c "import re, subprocess
from pathlib import Path
DEF = re.compile(r'^[ \t]*(?:function[ \t]+)?([A-Za-z_][A-Za-z0-9_]*)[ \t]*\([ \t]*\)[ \t]*\{'
                 r'|^[ \t]*function[ \t]+([A-Za-z_][A-Za-z0-9_]*)[ \t]*\{', re.M)
SN = re.compile(r'^[a-z0-9]+(?:_[a-z0-9]+)*$')
fs = [f for f in subprocess.run(['git','ls-files'],capture_output=True,text=True).stdout.split()
      if f.endswith('.sh')]
n = [m.group(1) or m.group(2) for f in fs
     for m in DEF.finditer(Path(f).read_text(encoding='utf-8', errors='replace'))]
bad = [x for x in n if not SN.match(x.lstrip('_'))]
print(len(n), len(bad), sorted(set(bad)))"
```

which prints `608 6 ['FAMILY_of', 'GIT', 'GITLS', 'GITSHOW', 'S']` — five distinct names, six
occurrences. **So `sh.function.conv` starts at 6**, and this repo is already 99% snake without ever
having been asked to be, which is the strongest available evidence that the external rule and this
corpus were never in conflict.

That 6 is an ESTIMATE and the spec says so rather than letting a criterion swallow it: it is taken
over the naive pattern's names, and the parser's name set is the thing this unit exists to build. The
pin that LANDS is emitted by the measurement path over the parser's own output and pasted, never
typed, and AC11 observes that the landed value equals the emitted one. If the parser's set differs
from 608 the pin differs from 6, and the criterion still holds.

### The pins this unit moves

Two pins move and rev-1 budgeted neither.

**`VERB_OFFENDER_PIN`, by +508.** Arming the language puts every extracted shell function in front of
the P1 verb predicate, exactly as `.py` and `.js` already are — `--check` reports `graded=1045`, which
is 976 python plus 69 javascript. Of the 608 shell names, 508 occurrences lead with a token the
declared table does not carry:

```
python -c "import re, subprocess, sys
sys.path.insert(0,'tools/lexicon')
import lexicon as L
from lexicon_conf import load_conf
from pathlib import Path
DEF = re.compile(r'^[ \t]*(?:function[ \t]+)?([A-Za-z_][A-Za-z0-9_]*)[ \t]*\([ \t]*\)[ \t]*\{'
                 r'|^[ \t]*function[ \t]+([A-Za-z_][A-Za-z0-9_]*)[ \t]*\{', re.M)
fs = [f for f in subprocess.run(['git','ls-files'],capture_output=True,text=True).stdout.split()
      if f.endswith('.sh')]
n = [m.group(1) or m.group(2) for f in fs
     for m in DEF.finditer(Path(f).read_text(encoding='utf-8', errors='replace'))]
V = set(load_conf(Path('.lexicon.conf'))['VERBS'])
print(len(n), sum(1 for x in n if L.leading_verb(x) and L.leading_verb(x) not in V))"
```

which prints `608 508`. The commonest arrivals are the test-harness idioms this repo writes by the
hundred — `verb`, `fail`, `ok`, `bad`, `mk`, `say`, `is` — none of which is in the table and none of
which this unit renames. **This is the largest single pin movement in the build**, it is a
consequence of arming rather than of any name this unit writes, and it lands as S8's RAISED-by-name
comment naming shell as the sole arrival.

**`508` IS AN UPPER BOUND, NOT THE VALUE, and this spec would contradict itself if it said
otherwise.** The snippet above is the NAIVE same-line pattern, and AC1 requires the parser's
population to DIFFER from that pattern's — a parser count equal to the naive count is a finding
there, not a pass. So the population that produced `508` is one this unit is committed to
replacing. The direction is known and only the direction: the naive pattern over-counts, because
it matches definition-shaped lines inside heredocs and quoted blocks — a heredoc-aware refinement
of the same pattern over the same 94 files returns 336 rather than 608, losing 272, and ten of
those losses are one test script's conflict-marker fixtures. The parser's number will be smaller
than 508 and cannot be stated before the parser exists. **S8 and AC12 therefore raise the pin by
what the PARSER measures at landing, read from its own run, and this figure is here to say the
movement is large rather than to be pasted into the conf.** A spec that pinned `508` would be
gating the naive regex it was written to retire.

The arithmetic is expressed as a READ and not as a literal, because a sibling moves the scalar before
this unit runs: `TOOL-aSurfacedLexicon-5` is order 3 and its files-touched table takes
`VERB_OFFENDER_PIN` from `461` to `462` for its minted `classify`. So S8 raises the value
`grep -n VERB_OFFENDER_PIN .lexicon.conf` returns at landing by 508, whatever that value is by then.
On the tracked conf today that read is `461`, and if unit 5 has landed it is `462`.

**The minted identifiers cost ZERO, and that is measured rather than hoped.** The unit mints
`parse_shell_defs` and `scan_shell_tokens` in `tools/lexicon/lexicon.py`, and
`test_shell_constructs`, `test_shell_refusals` and `test_shell_sentinel` in
`tools/lexicon/selftest.py`. Each was run through
`python tools/lexicon/lexicon.py --suggest <name>` and each answers `OK`, leading with `parse`, `scan`
and `test` respectively — all three are in the declared table. The tempting spellings are NOT: both
`_shell_defs`, which would mirror the existing `_python_defs` and `_probe_defs`, and `tokenize_shell`
answer that the leading token "is not in the declared table", so the sibling naming pattern is
deliberately not followed here and the cost of following it would be two more offenders.

Staged all five stubs and measured: `graded 1045 -> 1050`, `offenders 461 -> 461`. Five definitions
arrive, the offender count does not move, and the staged files were reverted with
`git checkout -- tools/lexicon/lexicon.py tools/lexicon/selftest.py`. `lexicon naming predicates`
guards on `tools/` among others and its ceiling is 300 s, so a commit editing either file selects the
leg and the push bar runs it — which is why the zero is measured and not assumed.

### Files touched (estimate)

- `tools/lexicon/lexicon.py` — the parser, the third `mode` arm, the DEAD PROBE coverage. Mints
  `parse_shell_defs` and `scan_shell_tokens`.
- `tools/lexicon/selftest.py` — the frozen sentinel and the construct table. Mints
  `test_shell_constructs`, `test_shell_refusals` and `test_shell_sentinel`.
- `.lexicon.conf` — the `LANGS` move, the `sh.function snake` cell row, the `sh.function.conv` pin
  row, the `VERB_OFFENDER_PIN` raise of S8, and the `ratified` re-stamp. Mints no identifier.

Every minted name is in `### The pins this unit moves` with its `--suggest` verdict and the measured
offender delta of zero. No new module, for the reason the research
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
- perf / scale — the naive regex covers 96 files in 0.064 s, timed by the section 4 snippet with a
  `time.time()` around the walk, and a tokenizer is a constant factor above that, so the leg cost is
  expected to stay far under the 300 s ceiling `tools/gate-legs.json` declares for `lexicon naming
  predicates`. ESTIMATE: the parser does not exist yet and the landing run must measure it.
- a11y — N/A. A CLI gate with no user interface.
- i18n — the parser reads bytes and reports names verbatim, so a non-ASCII function name is returned
  intact. Whether the VOCABULARY predicate then grades it correctly is review finding D25 against
  `subtokens.py`, which this unit inherits and does not widen.
- error / empty / loading states — an untokenizable file raises and names its position; a zero
  population over a corpus containing shell reds as DEAD PROBE; a sentinel fixture that stops yielding
  definitions reds in the kit's suite.
- observability — the shell cell appears in the per-cell report from `TOOL-aSurfacedLexicon-6` with
  its count, its denominator and its rule `snake`, and the coverage fraction moves from the run's own
  pre-change reading upward on the same run, which is the number this unit exists to move. That
  reading is `armed 57 of 141` on the tracked tree today, and AC8 takes it from the landing run
  rather than from this sentence.
- risks — the sharp one is a false refusal: a hand-written parser meeting a legal shell file it cannot
  tokenize reds the bar on correct work. S7's pre-wiring run over the whole tree, printing hits and
  near-misses, is the mitigation, and rev-2 gives it an actual surface — a direct call on
  `parse_shell_defs` from the working tree, quoted in S7 — because rev-1 pointed the mitigation at
  `--measure`, which is the pin emitter and which returns `None` for a dark language anyway. A
  mitigation with no surface is not a mitigation.
- testing + left-shift gates — a construct table in `tools/lexicon/selftest.py` with one arm per
  recognised form and one per refusal, the frozen sentinel of S4, and the two live miscount instances
  from section 4 pinned as fixtures so a future regex shortcut cannot pass. The five identifiers this
  adds are named and measured in `### The pins this unit moves`: offender delta zero, staged and
  read off `--check`, against a `VERB_OFFENDER_PIN` with no headroom.
- migration / rollback — the conf edit is the whole migration and reverting the commit reverts it.
  Reverting AFTER a landing does owe a mode-ratchet justification marker, because parser back to dark
  is a weakening move, and that is a property of the ratchet rather than a defect of this unit.
- user docs — `tools/lexicon/README.md` gains the parser's declared scope and its three refusals, and
  the coverage-mode table gains the row. The `lexicon wiring` leg's byte-compare forces the Skill
  re-render if the placeholder set moved.

## 6. Acceptance criteria

- **AC1** — When the parser runs with the cell armed, `python tools/lexicon/lexicon.py --check`
  reports a shell function population over the SAME file list section 8's F1 rules for — the
  extension-keyed set, `git ls-files '*.sh'`, which returns 94 files at this base and NOT the 96-file
  set including the two extensionless bash scripts. Rev-1 graded the extensionless-inclusive
  population that F1 recommends against arming, which was a contradiction inside one spec. The
  parser's count is compared against the naive pattern's count taken in the SAME run over the SAME
  list, by running the section 4 snippet immediately beside it, and the two must differ. Both numbers
  come from one run rather than from this document: on the tracked tree today the naive side is 608,
  and a landing where it reads differently still satisfies this criterion. A parser count EQUAL to
  the naive count is a finding, not a pass, because the two readings are known to disagree in this
  tree, and the direction of the difference must be one the parser's header explains.
- **AC2** — When the parser reads `tools/hooks/agent-cap.test.sh`, the JavaScript function inside the
  `<<'EOF'` heredoc — at line 1211 at this base, 1187 at rev-1's — is NOT returned as a shell
  definition, asserted by a
  `python tools/lexicon/selftest.py` arm keyed on that construct rather than on that file's line
  number.
- **AC3** — When the parser reads `tools/memory-tree/merge-rows.test.sh`, it returns the ten
  definitions below the grep pattern `'^<<<<<<< ours$'` — line 291 at this base, 287 at rev-1's —
  that a heredoc-aware line regex loses, asserted by a
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
- **AC8** — The coverage line moves, observed as an identity between two readings of ONE landing run
  rather than against a literal. `python tools/lexicon/lexicon.py --check` is run on the parent commit
  and again on the landing commit; the armed numerator rises by the count of tracked `.sh` carriers,
  the denominator is unchanged, and the unarmed remainder the run names is exactly the extensionless
  carrier at `.githooks/pre-commit` plus whatever section 8's F1 left unreached. Rev-1 keyed this to
  "58 of 138", which this tree cannot produce: the pre-change reading is `armed 57 of 141` and the
  unarmed remainder is 84, of which 83 are `.sh`. Those figures are context here and the criterion
  does not rest on them.
- **AC9** — When the parser is run over the whole tree BEFORE the cell is armed, by the direct call
  S7 quotes rather than by any shipped mode, its hits and its near-misses are recorded in this
  build's record. Rev-1 pointed this at `python tools/lexicon/lexicon.py --measure`, which is the pin
  emitter per its own usage block in `tools/lexicon/lexicon.py` and which cannot reach a `dark`
  language in any case, so the criterion had no surface to observe. The record must state the file
  count the run covered, the hit count, the near-miss count with S7's definition of the term, and
  what the run caught that this spec did not predict — a record reporting no near-misses states that
  as a measured zero over a named file count. A record with no file count, or a wiring commit with no
  record at all, fails this criterion.
- **AC10** — When the parser's own header is read, it enumerates all of: the four recognised
  definition forms of S1 and section 4, the three refusals — untokenizable file, `eval`/`source`
  construction, heredoc body — and what the function returns for a file it cannot tokenize. Asserted
  against the shipped docstring in `tools/lexicon/lexicon.py`, not against
  `tools/lexicon/README.md`, which is a different artifact. This is the only observation S2 gets, and
  it is owed because the `eval`/`source` refusal has NO runtime behaviour to assert: without this
  criterion a header naming one refusal and omitting the other two passes every other criterion here.
- **AC11** — The cell's rule and its pin are both observed. `python tools/lexicon/lexicon.py --check`
  after landing prints the shell function cell's row carrying the convention token `snake` and its
  denominator, and `grep -n 'sh.function' .lexicon.conf` shows the `CELLS` row naming `snake` and the
  `sh.function.conv` pin row. The pin's VALUE equals what the measurement path emitted over the
  parser's own output in the same commit, pasted rather than typed; the estimate from the naive name
  set is 6 and a landed value differing from it is a pass so long as it equals the emitted one. Then
  the RED half, because the green half alone cannot fail: renaming one shell function to `GITX` and
  re-running `--check` reds naming `sh.function.conv` over its pin, and reverting greens.
- **AC12** — The `VERB_OFFENDER_PIN` raise of S8 is observed as arithmetic, not as a literal. Before
  the `LANGS` edit, `grep -n VERB_OFFENDER_PIN .lexicon.conf` is read and `--check` reports its
  offender count; after it, the offender count has risen by the shell contribution and the pin in the
  conf equals the new count exactly. Staging the `LANGS` edit WITHOUT the pin raise reds `lexicon
  naming predicates` with `verb offenders … over pin …`; adding the raise greens. The raise carries
  the RAISED-by-name comment naming shell as the sole arrival and the command that measured it. The
  expected contribution on the tracked tree today is +508, measured by the snippet in `### The pins
  this unit moves`, and the criterion is the equality rather than that number.

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
  of them is a definition carrier — the eighty-fourth of the 84 unarmed carriers. Reaching them needs
  a shebang read, which is a second population selector over the corpus and is the thing the coverage
  sniffer's header argues against. Recommendation: stop at the extension, so the population this unit
  arms is `git ls-files '*.sh'` at 94 files, and have the run NAME the unreached carrier rather than
  let it vanish into the denominator. AC1 grades that same 94-file list, so the ruling and the
  criterion now agree; rev-1's AC1 graded the 96-file set this fork recommends against.

  **The shebang axis is OWED, and rev-2 stops pretending it is routed.** Rev-1 sent it to
  `TOOL-aSurfacedLexicon-9`, which carries `order 3` — one step AHEAD of this unit, so it will already
  have shipped — and whose spec mentions `shebang` zero times and disclaims the axis outright: its S2
  reads "INHERITED, not built here: the row-key grammar … is `TOOL-aSurfacedLexicon-4`'s generic
  `_parse_block` default." It widens `PATTERNS` and `PATTERN_SETS`, not the `LANGS` key axis. A
  hand-off the receiver has never heard of is not a hand-off, so no unit is named here. Stated instead
  in the words a receiver must carry, for the orchestrator to route: **a `LANGS` key axis that selects
  a language by SHEBANG as well as by extension, reaching the two tracked extensionless bash scripts
  `.githooks/pre-commit` and `.githooks/pre-push`, of which `.githooks/pre-commit` is a definition
  carrier this build leaves unreached.** It is a grammar change to the `LANGS` key, it needs a unit at
  an order strictly after 4, and until one accepts it in its own scope the item is open and this spec
  claims no coverage for it. This unit's own obligation is discharged by naming the unreached carrier
  in the run, which AC8 requires.
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
- rev-2 · 2026-09-05 · spec-audit round 1 fold, closing B3, B4, H3, H4, H5, M2, M3 and M4. Re-pinned
  from `d0a18683` to `6c670b02` and re-measured every figure with the command beside it: the shell
  corpus is 94 files and not 89, the naive pattern reads 608 and not 581, coverage is 57 of 141 and
  not 58 of 138, and the unarmed carriers are 84 of which 83 are shell. Both regexes are now QUOTED,
  and rev-1's 570/11 refinement figures are RETIRED as unreproducible rather than corrected. The
  armed cell's convention is fixed at `snake` from the Google Shell Style Guide — an external
  prescriptive source, chosen before any shell name was counted — with its pin estimated at 6 and
  gated by AC11. Two pins are budgeted where rev-1 budgeted none: the five minted identifiers cost a
  measured ZERO offenders, and arming the language itself costs +508, the largest pin movement in the
  build, which is now S8 and AC12. S7's mitigation was pointed at `--measure`, the pin emitter, which
  cannot reach a dark language; it now has a quoted direct-call surface and a definition of
  "near-miss". AC1 was re-keyed from the 96-file population F1 rules against to the 94-file one it
  rules for. The `sh.file` non-goal's two false claims are retracted and the shebang deferral is
  restated as an OWED item in a receiver's words, since `TOOL-aSurfacedLexicon-9` lands at an earlier
  order and never accepted it.
- rev-3 · 2026-09-05 · `508` demoted from a value to an UPPER BOUND. It is the NAIVE pattern's figure, and
  this spec's own AC1 requires the parser's population to DIFFER from that pattern's — so pinning it
  would gate the regex this unit exists to retire. The direction is measured and only the direction:
  a heredoc-aware refinement of the same pattern returns 336 rather than 608. S8 raises by what the
  PARSER measures at landing. Also: `TOOL-aSurfacedLexicon-13` left build order 4 during the same
  fold, so the deferral-risk paragraph no longer names it as a co-resident.
- rev-4 · 2026-09-05 · a line citation into `tools/lexicon/lexicon.py` symbol-anchored.

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
