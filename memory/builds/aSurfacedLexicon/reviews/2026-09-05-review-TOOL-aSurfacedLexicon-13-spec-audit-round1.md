**Serves:** spec-audit TOOL-aSurfacedLexicon-13 TOOL-aSurfacedLexicon-14 TOOL-aSurfacedLexicon-7

# Spec audit round 1 — the three specs the re-measure pass left behind

Tier-2 spec audit · 2026-09-05 · node `a` · build `aSurfacedLexicon` · streams tooling · designs
only, no code exists yet. Auditing DESIGNS, not code: every finding below is about what the three
specs say, and the tree is read only to check what they say against it.

**Subjects**, pinned at the blobs this round read, ROUND 1:
`memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-13.md@eff5cfe31cb10f59b6e864f20c32383cde2ed2a0`,
`memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-14.md@a2868da2b9b9e4176a18ceec66b6564486c7f224`,
`memory/builds/aSurfacedLexicon/spec/2026-09-04-spec-aSurfacedLexicon-7.md@c01f6f6a96b063bf3c5c7f673c3226fc87e5c80c`.

## Verdict: BLOCKED

Seven blockers, nine highs, five mediums and one low, after deduplication. Three of the seven are
one cause with three addresses, and it is structural rather than a coincidence of three authors:

```
$ for f in memory/builds/aSurfacedLexicon/spec/*.md; do sed -n '3p' "$f"; done | grep -o 'base [0-9a-f]*'
```

returns `base 6c670b02` for units 2, 3, 4, 5, 6, 8, 9, 10 and 12, and `base d0a18683` for units 1,
7, 11, 13 and 14. The build README already ruled that class — "The spec set was written at a base
this run does not execute on... Seven specs are re-measured and re-pinned" — and **all three subjects
of this round are among the specs that pass did not reach.** Unit 1 is CLOSED and unit 11 is not in
this round, so every live unrepaired spec in the build is on this desk.

The remaining four blockers are not staleness and a re-measure does not touch them. Two are the same
order-5 gap in unit 7 seen from two directions: it writes `py.function` pin rows into a declaration
that has no `py.function` cell until order 7, and it attributes a corpus-wide offender total to one
cell whose own total is 26 short. One is unit 13 staging its only in-tree failing case against that
same absent parent cell. One is unit 14 leaving the convention and the pin value of the cell it arms
unnamed in every section, which is the anti-mirror rule failing at the exact point this build says it
binds hardest.

None of the seven needs a design change. All seven are spelling: re-measure at the base the run
executes on, say which declaration each criterion is measured against, key each figure to the cell it
belongs to, and name the rule before the parser measures the population.

## Review shape

Raw 57 · confirmed 36 · refuted 21 · unverified 0 · precision 0.63. A parallel finder fan followed by
an adversarial skeptic prompted to refute each finding, then this synthesis pass. The thirty-six
confirmed findings deduplicate to the 22 rows below; the raw ids each row folds are named in its
address line so a reader can reconcile this record against the run.

Precision at 0.63 sits just under the 0.65 this build's `TOOL-aSurfacedLexicon-5` round scored and
comfortably above the 0.49 of the round before it. The survivors are again the findings that ran
something: every blocker below carries a command and its output.

**Severity is adjudicated in THIS record**, not inherited from the finders. Three rows moved and each
says so in place: H2 up from medium (raw 4, 32), H6 up from medium (raw 12), H8 down from blocker
(raw 46).

## What was re-measured for this round

Every figure this record asserts was taken on this worktree at `5318ed28`. That tree is
code-identical to the run's BASE for these purposes — `git diff --name-only 6c670b02..HEAD | grep -E
'\.(py|sh|js)$'` returns nothing — so a BASE reading and a HEAD reading are the same reading, and the
specs' `d0a18683` readings are the only ones that differ.

| Reading | Command | `d0a18683` | BASE / HEAD |
|---|---|---|---|
| Tracked `.py` | `git ls-files '*.py' \| wc -l` | 47 | **49** |
| Tracked `.sh` | `git ls-files '*.sh' \| wc -l` | 89 | **94** |
| Tracked `.js` | `git ls-files '*.js' \| wc -l` | 11 | **8** |
| Python function definitions | the walk below | 925 | **976** |
| Leading `test_` | the walk below | 106 | **107** |
| Leading `cmd_` | the walk below | 31 | **32** |
| P1 graded | `python tools/lexicon/lexicon.py --check` | 1047 claimed | **1045** |
| P1 offenders | same | 461 | **461** |
| Coverage | same | "58 of 138" claimed | **armed 57 of 141 (40.4%)** |

The walk is one invocation and this record is the only place it is written down, which is the point:

```
python - <<'PY'   # parse LANGS from .lexicon.conf, then per ext:
                  # lexicon.extract(path, mode, pset) -> got[0] is [(name, lineno)]
                  # classify leading_verb(name): in VERBS -> clean; in canon.build_form_index() -> DEBT; else UNRULED
PY
```

Its output at BASE, which four of the seven blockers turn on:

```
py fn defs: 976 | test_: 107 | cmd_: 32
graded   {'.py': 976, '.js': 69} = 1045
offenders{'.py': 435, '.js':  26} = 461
debt     {'.py':  44}             = 44
unruled  {'.py': 391, '.js':  26} = 417
distinct DEBT tokens: 24 · distinct UNRULED tokens: 267 · UNRULED singletons: 201
DEBT tokens the conf NOT-clauses name: 6 ['append','compute','count','log','search','validate'] covering 8 definitions
```

## Index

| # | Sev | Subject | Address | One line |
|---|---|---|---|---|
| B1 | blocker | unit 13 | §4 Inventory, §5, §6 AC1/AC2 | Every population figure is `d0a18683`'s; AC1 and AC2 fail on arithmetic |
| B2 | blocker | unit 13 | §2 S6, §6 AC1/AC2 | The only in-tree failing case stages onto a `py.function` cell that does not exist at order 4 |
| B3 | blocker | unit 14 | §4 both tables, §1, §6 AC1/AC8 | The whole shell corpus argument is five files stale; AC1 and AC8 name numbers this tree cannot produce |
| B4 | blocker | unit 14 | §2 S3 | The armed cell's convention and pin value are named in no section and observed by no criterion |
| B5 | blocker | unit 7 | §4 Data model | The eight-figure table has no runnable command and only its sum survives at BASE |
| B6 | blocker | unit 7 | §6 AC4, §4 Migration | A corpus-wide 461 is attributed to `py.function`, whose own pair sums to 435 |
| B7 | blocker | unit 7 | §4 Files touched, §2 S4, §6 AC7 | `py.function` PINS rows land at order 5 into a conf with no `py.function` CELLS row |
| H1 | high | unit 13 | §2 S4 vs §6 | The per-cell ratchet is the one scope item with no criterion |
| H2 | high | unit 13 | §6 AC4, §2 S5 | Two criteria consume unit 6's arms and nothing sequences unit 6 first |
| H3 | high | unit 14 | §6 AC1 vs §8 F1 | AC1 grades the 91-file population its own fork recommends rejecting |
| H4 | high | unit 14 | §6 AC9, §2 S7 | `--measure` is the pin emitter; the sharpest risk's mitigation has no surface |
| H5 | high | unit 14 | §5, §4 Files touched | A whole parser minted against a pin with zero headroom, no delta budgeted |
| H6 | high | unit 7 | §6 AC4/AC7, §4 Migration | A sibling two orders earlier moves the pin to 462; the arithmetic is stated at 461 |
| H7 | high | unit 7 | §3 first paragraph | "Not an enforcement change" is false: per-cell two-sided pins red what the scalar greens |
| H8 | high | unit 7 | §6 AC7 vs unit 4 S10 | A verbatim paste of the two rows is exactly the adjacent pair the grammar refuses |
| H9 | high | unit 7 | §6 AC3 | The precedence criterion cannot fail: conf and canon return the same answer |
| M1 | medium | unit 13 | §4 Decorators | The stated `ValueError` risk runs backwards; the failure is loud, on an unguarded leg |
| M2 | medium | unit 14 | §2 S2 vs §6 | The parser's declared header scope has no criterion |
| M3 | medium | unit 14 | §3 first non-goal | `sh.file` is not armed and unit 5 does not own it |
| M4 | medium | unit 14 | §8 F1 | The shebang deferral routes to a unit at an earlier order that never mentions it |
| M5 | medium | unit 7 | §4 Files touched | Mints a classifier, helpers and emitters; names none, budgets no pin movement |
| L1 | low | unit 7 | §7 last sentence | `memory-tree hygiene` is not a leg in the manifest |

## Blockers

### B1 — unit 13's inventory is measured at a base this run does not execute on, and two criteria fail on arithmetic

**Address:** unit 13 §4 `### Inventory — what this tree can actually exercise, stated plainly`, §5
`perf / scale`, and §6 AC1 and AC2. Folds raw ids 2, 19, 44, 48.

Section 4 states 47 tracked `.py` files, 925 function definitions, 31 leading `cmd_` and 106 leading
`test_`, and 11 tracked `.js` files. Section 5 states a P1 population of 1,047. Measured at BASE
through the kit's own extractor: **49, 976, 32, 107, 8**, and a P1 population of **1045**. Every
figure reproduces exactly at `d0a18683` and none of them reproduces on the tree the build lands on.

Two criteria embed those literals as pass conditions rather than as context.

AC1 requires `--check` to exit non-zero "reporting 106 violations", and stakes the number on "the 47
tracked `.py` files". AC2 requires the parent's graded count to fall "by exactly 106" so "the two sum
to the parent's pre-change count of 925". A correct implementation of the selector produces 107 and
976 and fails both, before the routing mechanism is exercised at all. AC2 is the criterion that
PROVES the exclusion, which is the whole unit, so its failure is not cosmetic.

The 1,047 in section 5 deserves its own sentence, because it is not merely stale. `--check` on the
unstaged tree prints `graded=1045`, and 1047 is the figure sibling unit 6 reports at
`spec/2026-09-04-spec-aSurfacedLexicon-6.md:190` as its own WITH-STAGED reading. So the spec has
inherited a number measured with four names staged into a working tree, as though it were a property
of the corpus.

**Fix.** Re-pin the status header from `d0a18683` to `6c670b02` and re-run the walk there, per the
remedy the build README already applied to seven siblings. Then phrase AC1 and AC2 as an identity
observed in ONE run rather than as literals: the selector's reported count equals the leading-`test_`
count over the tracked python corpus at the landing base, and the parent's post-change count plus the
selector's count equals the parent's pre-change count, both read out of the same `--check` report.
That criterion survives the next commit that adds a test.

**Left-shift.** A spec-lint arm over `memory/builds/*/spec/*.md`: a spec whose status header names a
`base <sha>` that is not the BASE its build's RUN record declares reds. It is a two-line check with a
`git rev-parse` in it, and it would have caught all three of this round's staleness blockers at
authoring time instead of at audit time. Second arm, narrower and worth more: an acceptance bullet
containing a bare integer that also appears in that spec's own §4 measurement table must be
re-derivable — reds unless the bullet also names a command or is phrased as an identity between two
readings of the same run.

### B2 — unit 13's only in-tree failing case stages a selector onto a parent cell that does not exist at its order

**Address:** unit 13 §2 S6 and §6 AC1 and AC2, against §4 `### Files touched`. Folds raw id 1.

AC1 stages "a selector routing the `test_` prefix of the Python function cell" into `.lexicon.conf`
and expects "zero new violations against its parent". AC2 requires "the parent Python function cell's
graded count" to fall. Both presuppose a `py.function` cell that exists before the change.

There is none at order 4. Sibling unit 6 rev-4 names it explicitly at
`spec/2026-09-04-spec-aSurfacedLexicon-6.md:258`: the pairs that are "non-empty and carry no `CELLS`
row" are "`py.function` at 976, `py.type` at 41 and `js.function` at 69". Unit 6 arms exactly one row,
`py.constant`, and unit 12's S14 writes the full matrix at order 7. Unit 5's own files-touched table
says "NO `CELLS` row: this unit arms nothing". And unit 13's §4 Files-touched line says `.lexicon.conf`
changes "for nothing at landing", so this unit does not declare the parent either.

So S6 — "the failing case, observed" — cannot be staged as written, and the build rule that a new
predicate is not landed until its RED has been observed goes unmet for the unit whose §4 spends four
paragraphs arguing which failing case to take.

The rescue idiom already exists in this build and this spec did not take it: unit 5 rev-4 rewrote
seven of its own criteria against "a scratch `CELLS` block written into the working-tree
`.lexicon.conf`", after round 1 raised the identical defect as its B1. Unit 13 was written after that
fold and inherited none of it.

**Fix.** Pick one and say which, in §2 rather than by implication. Either add a scope item declaring
the parent `py.function` cell with its convention in this unit's own commit and reconcile it with
unit 6's arming story; or re-phrase AC1 and AC2 against a scratch declaration in the working tree, the
way unit 5 now does, and say so in the criterion; or move the unit to an order after the `CELLS`
matrix lands and state that dependency in §2.

**Left-shift.** The arm round 1 of the sibling audit already proposed, now with a second population
behind it: a criterion naming `tools/lexicon/lexicon.py --check` against a named cell must also name
the declaration it is measured against — the tracked conf, a scratch conf, or a fixture repo. A
criterion that names none is refused. That single arm produces three of round 1's four blockers and
two of this round's seven, which is the strongest evidence available that it is owed.

### B3 — unit 14's whole measured argument is five shell files stale, and both its comparators are unreproducible

**Address:** unit 14 §4 `### Why a regex probe is refused` table, §4 `### Inventory — the population
this arms` table, §1, §2 S5, and §6 AC1 and AC8. Folds raw ids 20, 49 and the staleness half of 9.

The spec keys everything to 89 tracked `.sh` files. `git ls-files '*.sh' | wc -l` returns **94**, and
`git ls-tree -r --name-only 6c670b02 | grep -c '\.sh$'` returns 94 as well, so this is not a
HEAD-versus-BASE quibble: the number was already wrong for the run at the moment the run began.
Sibling unit 6 reports `sh.file` at 94 tracked files. S5's "a corpus that contains 89 tracked shell
files" carries the same reading.

The coverage baseline is worse, because a criterion is keyed to it. §4's table and §5's observability
line both state "58 of 138" and AC8 requires the armed share to rise "above the pre-change reading of
58 of 138". Live:

```
$ python tools/lexicon/lexicon.py --check
lexicon: coverage — armed 57 of 141 definition-carrying file(s) (40.4%)
```

The pre-change reading is 57 of 141. The unarmed remainder is 84, not the 80 that §1's headline
sentence — "79 of the 80 unarmed definition-carrying files" — and §4's inventory table both rest on.
That headline is the unit's entire justification for existing, so the number carrying it should be one
somebody can reproduce.

AC1's comparator does not reproduce either. A same-line regex of the shape §4 describes returns 608
matches over the 94 tracked `.sh` files here, against the spec's 581 over 89 and 582 over 91. I do not
claim 608 is the spec's regex — it is my reading of the described shape, and that is exactly the
problem: the spec gives a number and not the pattern, so no second party can land on the same
figure. AC1 requires the parser's count to differ from "the naive regex's 582" and calls a count equal
to it a finding. A criterion whose comparator nobody can re-derive cannot adjudicate anything.

The 1-confirmed-heredoc over-count and the 11-lost-definition under-count are the two live instances
this design is built on, and they may well survive a re-measure — AC2 and AC3 pin them to constructs
rather than to counts, which is the right shape. This finding is about the denominators around them.

**Fix.** Re-pin the header to `6c670b02` and re-run the sniffer, the extractor and both regex passes
there, quoting the regex itself rather than only its result. Restate §1's headline, §4's two tables
and §5's observability line from that run. Re-key AC8 to a rise against the run's OWN pre-change
reading captured at landing, and give AC1 either a quoted pattern or a comparator taken in the same
run as the parser's.

**Left-shift.** The B1 base-drift arm covers the staleness. Add one for the comparator class,
because it is separable: a spec asserting a count produced by an ad-hoc pattern (a regex, a glob, a
grep) must carry the pattern in the spec, not just its result. Reds a table row that states a number
attributed to a "naive regex" nobody can rebuild.

### B4 — unit 14 arms a cell and never says what rule it grades against, or what its pin is

**Address:** unit 14 §2 S3, and its absence from §4, §6 and §8. Folds raw id 7.

S3 says the shell function cell "is declared with its convention and its pin row". Grepped over the
whole spec: `snake` appears **zero** times; `convention` appears only inside S3's own sentence;
`pin` appears in S3, in §4's Files-touched line, and nowhere that gives it a value. No section names
the convention. No criterion in §6 observes either the rule string or the pin. §8's three forks are
about extensionless files, raise-versus-skip, and whether to arm at all — none is about what the cell
grades by.

No sibling supplies it. Unit 7 emits pin VALUES at order 5 and names no shell cell. Unit 12's matrix
is order 7 while S3 puts the cell row in this unit at order 4.

That leaves the unit's central deliverable — the rule the newly armed cell grades against, and the
number its ratchet starts from — to be chosen by the builder, who will be holding the parser's
freshly measured output at the moment they choose it. That is the mirror shape precisely: a standard
derived from the population it grades. The build's own first rule says the corpus is evidence for
exactly one thing, which spellings become debt, and this is the unit where that rule is easiest to
break by omission rather than by intent. A pin chosen after seeing the count is byte-identical to one
measured, and nothing downstream can tell them apart.

**Fix.** Name the convention in §4 with its source OUTSIDE this corpus — a prescriptive shell style
guide, cited — and add a criterion asserting that the shell cell's rule string and denominator appear
in the per-cell report. State in §4 that the pin is emitted by the measure path and pasted, never
typed, and add the RAISED-by-name comment form the conf already uses. If the honest answer is that
the convention cannot be fixed before the parser runs, then say THAT and make the pre-wiring run of
S7 a gate on the ruling, rather than leaving the question unasked.

**Left-shift.** A `.lexicon.conf` reader arm, which is a gate rather than a checklist item: a `CELLS`
row whose pin was not emitted by the measure path in the same commit is refused — the emitted rows
carry a provenance marker the reader checks, so a hand-typed pin reds where it is written. Spec-side
companion: a scope item using the phrase "is declared with its convention" without naming the
convention token is refused by the spec lint.

### B5 — unit 7's measurement table has no runnable command, and only its sum survives at BASE

**Address:** unit 7 §4 `### Data model`, the eight-row table and the paragraph beneath it, against the
status header. Folds raw ids 18, 47.

The table is attributed to "a scratchpad script importing `lexicon.extract`, `lexicon.leading_verb`,
`canon.build_form_index` and `lexicon.build_banned_index`". That script is not in the tree. I
reproduced all eight figures only by writing it myself, which took a working session and is precisely
the cost the build's "every number carries the command that produced it" rule exists to remove.

The table declares `cd8ab0d2` while the status header declares `d0a18683`, a third sha appearing
nowhere else in the build. The two trees measure identically for this purpose, so the third sha is
cosmetic. The staleness is not:

| Fact | Spec (`cd8ab0d2`) | BASE |
|---|---|---|
| P1 graded | 1047 | **1045** |
| DEBT definitions | 43 | **44** |
| UNRULED definitions | 418 | **417** |
| Sum | 461 | 461 |
| Distinct DEBT tokens | 23 | **24** |
| Distinct UNRULED tokens | 258 | **267** |
| UNRULED tokens with one site | 184 | **201** |
| DEBT tokens `--suggest` names a replacement for | 5 | **6** |
| DEBT definitions those cover | 7 | **8** |

Every row but the sum has moved. The sixth row moved for a reason worth carrying into the fix:
`count` joins the DEBT set at BASE, and `count` is one of the declaration's own NOT-clause tokens
(`measure` NOT `count`), so the advice half now works for six tokens rather than five. §4's sentence
"The five tokens are `append`, `compute`, `log`, `search` and `validate`" is a list, not just a
count, and it is one name short.

AC4 and AC7 consume 43 and 418 as pin values under unit 4's two-sided equality, where a count that is
too low reds exactly as one that is too high. So this is not a prose defect with a bookkeeping
consequence; it is two criteria that red a correct build.

**Fix.** Fold the derivation into the kit rather than re-writing the scratchpad: the classifier this
unit builds already computes every row of that table inside the corpus walk, so the measure path can
print them and §4 can quote one invocation. Re-measure at `6c670b02`, re-pin the header, correct all
eight rows, and add `count` to the named token list.

**Left-shift.** The B1 arm's second half is the one that binds here: a §4 measurement table whose
rows are cited to a script that is not a tracked path reds. A spec may cite a tracked tool, a git
command, or an inline snippet; "a scratchpad script" is not a citation, and this build's own rule
already says so in prose that nothing enforces.

### B6 — unit 7's AC4 attributes a corpus-wide offender total to a single cell, and cannot pass under its own S4

**Address:** unit 7 §6 AC4 and AC7, against §2 S4 and §4 `### Migration`. Folds raw ids 21, 37, 45.

AC4 requires `--check` to print "a `debt` count of 43 and an `unruled` count of 418 for
`py.function`", and asserts "their sum equals the 461 the single `VERB_OFFENDER_PIN` carries today".
S4 says the rows are emitted "per armed `vocab` cell". Those two statements are incompatible with the
tree, at BASE and at the spec's own base alike.

Measured at BASE, split by cell:

```
offenders {'.py': 435, '.js': 26} = 461
debt      {'.py':  44}            = 44
unruled   {'.py': 391, '.js': 26} = 417
```

`py.function`'s own pair is 44 + 391 = **435**. The missing 26 are `js.function`'s. `.js` is armed
`js-regex:probe` and grades 69 functions, so those offenders are real and sit outside python entirely.
At the spec's own `cd8ab0d2` the same error is present with different digits: `py.function` was
43 + 373 = 416, and the 418 includes js's 45.

So AC4 cannot pass under ANY correct implementation of S4, at any base. Re-measuring does not fix it.
An implementation written to satisfy AC4 literally must fold the js population into python's pin row
— which is the single-bucket-over-two-populations shape §4's own "Alternatives rejected" says the
split exists to remove. The unit would ship the defect it was written to close, and pass its own
criterion doing it.

§4's Migration inherits the same error from the other end: "`VERB_OFFENDER_PIN="461"` retires in
favour of two rows summing to 461". Under S4 over two armed vocab cells the retirement produces
**four** rows — `py.function.debt` 44, `py.function.unruled` 391, `js.function.debt` 0,
`js.function.unruled` 26 — whose grand total is 461 and no pair of which sums to it.

**Fix.** Restate §4 per cell and not per corpus, with the corpus sum on its own line. Rewrite AC4 as
two clauses plus a reconciliation: `py.function.debt` + `py.function.unruled` equals `py.function`'s
own offender count, `js.function.debt` + `js.function.unruled` equals js's, and the four sum to the
scalar the conf carries at the landing order. Rewrite AC7's emitted rows to the re-measured
per-cell values. Add a line on what a `js.function.debt` pin of `0` means under the two-sided
equality, since js has no debt population at all and a zero pin there is a check that can only red
upward.

**Left-shift.** In the code, where it belongs: an arm asserting that for every armed cell, that
cell's `debt` plus `unruled` equals that cell's own offender count, AND that the sum over all armed
cells equals the corpus offender total. It is four lines and it makes the class this finding names
structurally unreachable — a report that attributes a corpus figure to a cell fails its own
reconciliation. Spec-side companion for the lint: a criterion naming a cell key must not assert
equality with a figure the spec elsewhere attributes to the whole corpus.

### B7 — unit 7 writes `py.function` pin rows at order 5 into a declaration with no `py.function` cell

**Address:** unit 7 §4 `### Files touched (estimate)` and `### Migration`, §2 S4 and S5, and §6 AC7.
Folds raw ids 14, 22.

§4 lists `.lexicon.conf` "(the two pin rows)" among the files this unit touches, and AC7 requires that
"pasting its output into `.lexicon.conf` leaves `--check` green". Unit 4's S5 makes "a `PINS` row
naming a cell absent from `CELLS`" a refusal, placed in the TAIL of `load_conf` specifically so that
"every one of the module's four readers refuses identically". No `py.function` cell exists until unit
12's S14 writes the matrix at order 7; unit 7 is order 5.

The consequence is mechanical and reaches the push boundary. The reader that carries the refusal is
reached by `adopt-lexicon.sh --check`, which is the `lexicon wiring` leg, and the manifest gives that
leg `guard []` with ceiling 330 — an empty guard runs on every bar. So the landing commit reds a leg
this unit's own §7 says "must stay green across the pin-row change".

Read the other way, through S4's wording rather than §4's, the unit is inert instead of red: S4 emits
rows "per armed `vocab` cell", S5 repeats "for every armed cell", and at order 5 there is no
vocab-armed cell at all — unit 8, which wires `vocab` to the leading-token path, is order 6. Under
that reading the unit emits zero pin rows at landing and neither AC4 nor AC7 has anything to observe.
The spec never reconciles the two readings, so a builder gets to pick, and one choice reds the bar
while the other silently voids two criteria.

§4's Migration paragraph addresses only the scalar-versus-rows fallback and never names the `CELLS`
prerequisite at all.

**Fix.** Say in Migration that the two pin rows do NOT land until unit 12 writes the `CELLS` matrix at
order 7 — this unit ships the classifier, the report and the emission only — and drop `.lexicon.conf`
from §4's Files-touched. AC7 then observes the emitted OUTPUT rather than a paste. If instead the rows
are wanted at order 5, add a scope item declaring the `py.function` cell here and reconcile it against
unit 6's arming story and unit 12's S14, which is a scope change and should be surfaced as one.

**Left-shift.** A conf-reader arm — mostly already specified by unit 4's S5, so the left-shift is to
make it observable at spec time: the spec lint refuses a §4 Files-touched row naming `.lexicon.conf`
for a `PINS` key whose cell is not declared by that same spec or by a spec at a strictly earlier
order. The order graph is generated into the build README, so the lint can read it rather than being
told.

## Highs

### H1 — unit 13's per-cell ratchet is the one scope item with no criterion

**Address:** unit 13 §2 S4, against the whole of §6. Folds raw ids 3, 31.

S4 gives each selector its own pin row "so a subset's offender count ratchets separately from its
parent's under owner ruling Q2". Reading all eight criteria: AC1 and AC2 observe report counts and the
exclusion, AC3 the ambiguity refusal, AC4 the empty subset, AC5 and AC8 the decorator and the frozen
arity, AC6 the probe-mode refusal, AC7 the synthetic fixtures. **Not one mentions a pin row.** Nothing
observes that a selector'd key gets a row, what value it takes, or that moving one leaves the parent's
alone.

The consequence is not only an unobserved scope item. AC1 expects a non-zero exit, and under unit 4's
S9 two-sided comparison that exit depends on how an ABSENT selector pin reads — as `0`, as inherited
from the parent, or as a refusal. §4 states none of the three. So AC1's expected verdict rests on an
undeclared default, and an implementation that quietly folds the subset's count back into the parent's
pin satisfies every criterion in §6 while defeating the ratchet S4 exists to build. §4 also declines
to declare a selector row in this repo, so nothing on the bar exercises it either.

This build has already ruled the class: unit 5 rev-3 records its own H3 as "S8 as the only scope item
in this spec with no criterion", and fixed it.

**Fix.** Add a criterion beside AC7's synthetic fixtures — that is where it belongs, since this tree
declares no selector — staging a selector plus its two pin rows into a fixture declaration, draining
the selector's count by one, and observing the RED on the selector's row with the parent's row
untouched, then the reverse. State in §4 what an absent selector pin means.

**Left-shift.** A spec lint over §2 against §6: every `**Sn**` bullet must be named by at least one
acceptance criterion, matched on the bullet id. It is a two-file cross-reference, it is mechanical,
and this build has now produced the same finding in two separate audit rounds against two different
specs, which is the definition of a class worth gating.

### H2 — two of unit 13's criteria consume unit 6's machinery, and nothing sequences unit 6 first

**Address:** unit 13 §6 AC4 and §2 S5, against the build README's generated order table.
Folds raw ids 4, 32. **Adjudicated UP from the finders' medium**, for the reason in the last
paragraph.

AC4 observes the empty-subset refusal "as a DEAD CELL through `TOOL-aSurfacedLexicon-6`'s arm". S5
prints the selector's report row beneath "the per-cell report from `TOOL-aSurfacedLexicon-6`". The
README's generated order table puts step 4 as `TOOL-aSurfacedLexicon-13`,
`TOOL-aSurfacedLexicon-14`, `TOOL-aSurfacedLexicon-6` with **Parallel: yes**.

`memory/guides/BUILD-METHOD.md` M6 permits concurrency only when "neither writes a file the other
reads as a contract... or as an acceptance input, and neither depends on the other's output either
way". Unit 6 is an acceptance input to unit 13 by AC4's own wording. M2's cross-read axis says the
same thing from the other side.

The move up from medium is deliberate and is about what the defect voids rather than how likely it is
to bite. The spec as written violates a stated build-method rule, and the thing it costs is the
observability of a criterion — which is the exact class ("a criterion that cannot be observed") this
whole build exists to close. A parallel step is where the ordering guarantee is absent by
construction, so "the orchestrator will probably run 6 first" is a hope, not a sequencing.

The finding's second half — that a selector'd row must be reconciled against unit 6's AC3 row-count
assertion — I am dropping. A selector'd row IS a `CELLS` row, so the row count reconciles by
construction and there is nothing to state.

**Fix.** State the dependency the way unit 6 states its own on unit 5, as "a HARD prerequisite": name
unit 6 in §4, and either give this unit `order 5` or record in BOTH specs that within step 4 unit 6
lands first.

**Left-shift.** A build-index arm, which is cheap because the order table is already generated: a
spec naming a sibling unit id inside an acceptance criterion reds if that sibling's order is not
strictly lower. It reads the front matter that already exists and needs no new declaration.

### H3 — unit 14's AC1 grades the population its own fork recommends rejecting

**Address:** unit 14 §6 AC1 against §8 F1. Folds the contradiction half of raw id 9.

AC1 runs "over the 91 tracked shell-language files" and compares the result against "the naive
regex's 582". Per §4's table, 582 is the 91-file reading — 89 `.sh` plus the two extensionless bash
scripts. §8's F1 then recommends stopping at the extension, which is the 89-file population and the
581 reading.

So the unit's headline criterion is written against a population its own open question recommends
against arming. This survives the re-measure B3 asks for: whatever the corrected file counts are, AC1
must grade the population F1's ruling actually arms, and today it does not.

**Fix.** Re-phrase AC1 against the population F1 rules for, and take the comparator from the same run
and the same file list as the parser's reading, so the two numbers are commensurable by construction
rather than by the author having used the same list twice.

**Left-shift.** Spec lint: a criterion whose population is stated as a count must state the same
count as the §8 fork that rules on that population, where one exists. Narrower and more general
alternative if that proves fiddly — a fork marked with a recommendation must be cross-referenced by
every criterion whose population it changes, and an uncited one reds.

### H4 — unit 14's pre-wiring mitigation names a command that cannot produce what the criterion requires

**Address:** unit 14 §6 AC9 against §2 S7 and §4 Files-touched. Folds raw ids 12, 29. **Adjudicated
UP from one finder's medium** — this is the sole observation of the mitigation for the risk §5 itself
calls the sharp one.

AC9 requires that the parser's "hits and its near-misses are printed by `python
tools/lexicon/lexicon.py --measure`" BEFORE the cell is armed. That mode's shipped contract is at
`tools/lexicon/lexicon.py:1175`:

```
  --measure          print the three pins THIS conf produces; decide nothing
```

It is the pin emitter. The per-name hits printer is `--list`. Sibling unit 7's S5 and AC7 widen
`--measure` further into `PINS:` row emission at order 5, AFTER this unit. Nothing in unit 14's scope
widens it at all — §4's Files-touched names `lexicon.py` "for the parser, the mode arm and the DEAD
PROBE coverage", `selftest.py` and `.lexicon.conf`.

Worse, the run AC9 demands happens while the shell `LANGS` row is still `dark`, and `extract` returns
`None` for a dark language at `tools/lexicon/lexicon.py:272`. So there is no path by which any mode
prints shell hits at that moment. "Near-miss" is also undefined for a tokenizer anywhere in the spec,
so even a correct implementation has no pass condition to hit. And AC9's content requirement — that
the record "names what the run caught that this spec did not predict" — is satisfied by a record
saying nothing was caught.

Quietly adding the output to `--measure` alone is not the fix either: unit 3's standing rule is that
`--check` and `--measure` must not read refusals the other cannot, so widening one owes a
reconciliation.

**Fix.** Give S7 a surface and name it — either a scope item adding hits and near-misses to a named
mode, with the unit-3 symmetry reconciled, or a scratchpad run whose output is pasted into the build
record. Define what a near-miss is for this parser (a construct the tokenizer reached but declined,
with its reason, is the useful definition). Point AC9 at whichever surface it is, and have it name the
file counts the run must report so the record cannot be empty and still pass.

**Left-shift.** A spec lint over criteria that quote a CLI invocation: the mode named must exist in
the target tool's usage block, and if the spec expects new output from an existing mode, some scope
item must name that tool file for that reason. The usage block is a single tracked string at
`lexicon.py:1172-1178`, so the check is a grep, and it would have caught this at authoring time.

### H5 — unit 14 mints a whole parser against a pin with zero headroom and budgets no delta

**Address:** unit 14 §5 `testing + left-shift gates` and §4 `### Files touched (estimate)`.
Folds raw id 53.

`--check` prints `offenders=461` and `.lexicon.conf:164` reads `VERB_OFFENDER_PIN="461"`. Headroom is
exactly zero, offenders count per occurrence, and `lexicon naming predicates` guards on `tools/`, so a
commit editing `tools/lexicon/lexicon.py` selects it and the push bar runs it.

The parser's own siblings are already offenders — `--list` names `_python_defs` ("leading token
`python` is not in the declared VERBS table") and `_probe_defs` — so the naming pressure on this
unit's new code is not hypothetical. `--suggest _shell_defs` answers that `shell` "is not in the
declared table, and no row bans it by name", and neither `shell` nor `tokenize` is among the 24
declared verbs. Any `_shell_defs` or `tokenize_*` helper is a new offender that reds the landing
commit.

The sibling discipline is explicit and this unit is the one that skipped it. Unit 5 spends a whole
"### The pin this unit raises" section and AC11 budgeting `461 -> 462` for ONE minted identifier. Unit
6 measured its four names, found a zero offender delta, and said so. Unit 14 adds the most code in the
build and budgets neither.

**Fix.** Add a Files-touched line naming every definition the parser mints, run each through `python
tools/lexicon/lexicon.py --suggest <name>`, and state the resulting delta — either as zero, by
choosing from the declared table (`parse`, `read`, `scan` and `extract` all pass, and all four fit a
tokenizer), or as a named raise in the conf's RAISED-by-name comment form with the command that
measured it.

**Left-shift.** This one is gateable without a new leg, which matters given the build rule against
adding legs: extend the existing `lexicon naming predicates` failure message to name the pin's
headroom, and add a spec-lint arm requiring any spec whose Files-touched names a guarded path to state
a pin delta — zero counts, as long as it is stated. The zero-headroom pin has now produced a finding
in three separate audit rounds against three different specs.

### H6 — unit 7's arithmetic is stated at 461, and a sibling two orders earlier moves it to 462

**Address:** unit 7 §3 first paragraph, §6 AC4 and AC7, and §4 `### Migration`.
Folds raw ids 13, 25, 46. **Adjudicated DOWN from one finder's blocker**, because the fix is one
Migration line and the error is off-by-one rather than structural.

Unit 5 is order 3 and its §4 states that the landing commit raises `VERB_OFFENDER_PIN` from 461 to 462
in the RAISED-by-name comment form, naming its minted `classify` as the sole arrival — measured there
as `graded 1045 -> 1049` against `offenders 461 -> 462`. Unit 6 at order 4 cites that raise by name
while recording its own delta as zero. Unit 7 is order 5.

`classify` lands UNRULED, not DEBT, which decides which row absorbs it. Verified:
`canon.build_form_index()` returns 120 keys and `classify` is not one of them.

So by the order at which AC4 executes, the correct readings are one higher on the unruled row and the
scalar reads 462. §3's "the gate's reach is unchanged at 461 P1 offenders" and AC4's "the 461 the
single `VERB_OFFENDER_PIN` carries today" are both false on arrival, and AC7 emits a row one short.
Unit 7 is the unit that RETIRES the scalar and cites no sibling that moves it, so every raise landing
between order 3 and order 5 falsifies its arithmetic silently.

**Fix.** Add a Migration paragraph enumerating the pin deltas owed by units landing at orders 3 and 4
— unit 5's +1 is the known one — and state that the retirement absorbs the scalar as it stands at
order 5. Express AC4 as a derived equality against `grep -n VERB_OFFENDER_PIN .lexicon.conf` read at
landing, rather than against a literal. Say which row absorbs a raise once the scalar retires, so
later units know whether to budget against `debt` or `unruled`.

**Left-shift.** Spec lint: a criterion asserting a value read from a tracked declaration must express
it as a read, not as a literal, when a spec at a lower order names that same declaration key in its
own Files-touched. The order graph and the Files-touched tables are both already structured enough to
support this.

### H7 — unit 7's "not an enforcement change" is false: the split reds cases the scalar greens

**Address:** unit 7 §3 first paragraph, against §2 S4 and unit 4's S9. Folds raw id 24.

§3 says the split "narrows nothing", that "the gate's reach is unchanged at 461 P1 offenders", and
that the unit "is a reporting and advice improvement and is not an enforcement change".

Unit 4's S9 makes the pin comparison two-sided: a count that FALLS reds exactly as one that rises
does. Under a single scalar at 461, a rename that moves an offender from `py.function` to
`js.function`, or from DEBT to UNRULED inside one cell, holds the total at 461 and greens. Under S4's
two rows per cell the same rename reds twice — once for the fall, once for the rise.

That is strictly more enforcement reach, not the same reach. The claim §3 is actually defending is the
different, one-directional one in its next clause: no name that reds today greens tomorrow, and the
unruled population is not released. That claim is true. The sentence around it is not, and §5's risks
line half-notices ("the classification changes what a pin COUNTS") while §3 still denies it.

A builder taking §3 at its word lands the split expecting a green bar.

**Fix.** Rewrite §3's first paragraph to state what the split PRESERVES — no name that reds today
greens tomorrow — and what it ADDS: under the two-sided comparison, a within-total redistribution
across buckets or across cells now reds. Then add a criterion staging exactly that redistribution and
observing the RED, since it is a new failing case this unit creates and the build rule says a new
predicate is not landed until its failing case has been observed.

**Left-shift.** The criterion above IS the left-shift, and it is the cheap kind: one staged rename
that moves a name between buckets without changing the total, asserted RED. Nothing else in the build
covers the redistribution case, because until this unit there is only one bucket to redistribute
within.

### H8 — unit 7's AC7 asserts a green that the declaration grammar refuses

**Address:** unit 7 §6 AC7 against §2 S5 and unit 4's S10. Folds raw id 26.

Unit 4 is order 2 and unit 7 is order 5, so S10's refusal is live before this unit runs. S10 makes two
`PINS` rows whose line numbers differ by one a refusal inside `load_conf`, on the unguarded `lexicon
wiring` leg. Unit 4's AC5 note hands the obligation off by name: "whichever unit emits the block emits
it blank-separated, so no cell-arming commit ever authors a dense pair". Unit 12 accepted it as S13
and AC13.

Unit 7 is the OTHER emitter — S5 says `--measure` emits both rows for every armed cell — and neither
S5 nor AC7 says blank-separated. AC7 then asserts that "pasting its output into `.lexicon.conf` leaves
`--check` green". A verbatim paste of `py.function.debt 43` followed by `py.function.unruled 418` is
exactly the adjacent pair S10 refuses.

**Fix.** Add to S5 that the emission separates `PINS:` rows by exactly one blank line, and add the
clause to AC7 so the paste is observed against `adopt-lexicon.sh --check` — the unguarded path that
carries the refusal — rather than against `--check` alone.

**Left-shift.** A selftest arm on the emitter rather than a checklist entry: assert that the measure
path's own output, fed back through `load_conf`, parses. It is round-tripping the emitter against the
reader, it costs one arm, and it makes the whole class — any future emitter producing bytes the reader
refuses — structurally unreachable.

### H9 — unit 7's AC3 cannot fail, and certifies a precedence rule nobody observes

**Address:** unit 7 §6 AC3, against §2 S3. Folds raw id 27.

AC3 requires `--suggest append_row` to answer `add_row` "from the declaration's own NOT clause rather
than from the canon, proving the conf keeps priority over `canon.build_form_index()`".

Both sources return the same representative for `append`:

```
$ python tools/lexicon/lexicon.py --suggest append_row
use `add_row` — the declaration says `add`, NOT `append`: ...
$ python - <<'PY'  # canon.build_form_index()['append']
add
PY
```

So AC3 passes under either precedence order. It is a criterion that cannot fail, attached to prose
claiming it proves something — the could-not-fail class this build exists to close, in the spec that
is closing it elsewhere.

The finder's supporting claim was that no token in this declaration can distinguish the two sources,
and that is wrong in a way that improves the fix. Four tokens disagree today:

| Token | Conf says | Canon says |
|---|---|---|
| `install` | `seed` | `init` |
| `do` | `cmd` | `run` |
| `assert` | `test` | `check` |
| `enable` | `arm` | *(absent)* |

So S3's precedence rule is gateable on this tree right now. AC3 needs re-keying, not deferring to a
synthetic fixture.

**Fix.** Re-key AC3 onto a disagreeing token — `--suggest install_x` must answer `seed_x` from the
declaration and not `init_x` from the canon — and say in the criterion why that token was chosen, so
a future edit to the conf that collapses the disagreement is visibly a criterion-breaking edit.

**Left-shift.** A selftest arm asserting that at least one token in the shipped declaration disagrees
with `canon.build_form_index()`, and that `--suggest` follows the declaration for it. That arm reds if
a future conf edit removes the last disagreeing token, which is the only way the precedence rule
becomes ungateable here — and it reds loudly rather than turning AC3 back into a criterion that
cannot fail.

## Mediums

### M1 — unit 13's stated `ValueError` risk runs backwards, and names the wrong leg

**Address:** unit 13 §4 `### Decorators without touching the frozen extract contract`, and §6 AC8
which repeats the claim verbatim. Folds raw id 38.

§4 says "the second site catches `ValueError` at `tools/drift-audit/drift_report.py:938` and
continues, so the signal would degrade to an empty population rather than fail loudly". Read at BASE:

```
936        try:
937            got = lex.extract_text(src, mode, pset)
938        except (SyntaxError, ValueError):
939            continue
940        if got:
941            for nm, _ln in got[0]:
```

The unpack at 941 is OUTSIDE the try. Same shape at the other site: the try at 829-831 catches
`(SyntaxError, OSError)` — which never mentions `ValueError` — and the unpack sits at 835. So widening
the pair raises an UNCAUGHT `ValueError` at both sites, and the failure is loud, not silent.

It is also not invisible to the push bar. Line 941 sits in `_read_defs_at_sha` (`:896`), called at
`:1032-1033` from `build_lexicon_marginal_offense_rate`, which is FIRST in `SIGNALS` and runs bare at
`:1536` (`out = [s(ctx) for s in SIGNALS]`) with no per-signal except. And `tools/gate-legs.json`
gives `drift-audit records` no guard key at all, so it fires on every bar. §4's paragraph about being
"invisible to the push bar in two independent ways" describes the guarded `drift-audit selftest` leg,
where neither unpack site lives.

The DESIGN survives intact — the additive accessor is still right, and S3 still binds — so this is a
justification defect rather than a mechanism defect, which is why it is a medium and not a high. But
the reason given is the opposite of the truth, and AC8's rationale is built on it.

**Fix.** Rewrite the paragraph to the measured behaviour: widening the pair raises an uncaught
`ValueError` that reds `drift-audit records` loudly on every bar. Keep the additive accessor and
re-justify it on the two-call-site coupling alone. Rewrite AC8's rationale so it stops citing a catch
that does not guard line 941.

**Left-shift.** AC8 already does the real work — asserting the entries still unpack as exactly two
elements — so nothing new is owed in code. The spec-side arm worth having: a line-cited claim about a
`try`/`except` must cite the line of the guarded STATEMENT, not the line of the `except`. That is the
error here, and it is mechanical enough to lint if this class recurs.

### M2 — unit 14's parser header scope has no criterion

**Address:** unit 14 §2 S2, against §6 and §5's user-docs line. Folds raw id 11.

S2 requires the parser's scope DECLARED in its own header: which constructs it reads, which it
refuses, and what it returns for a file it cannot tokenize. No criterion in §6 observes any of it. §5
promises the text in `tools/lexicon/README.md`, a different artifact. AC1 leans on "a direction the
parser's header explains" without requiring the header to exist or be complete.

The `eval`/`source` refusal is header-only — it has no runtime behaviour to assert — so a header
naming one refusal and omitting the other two passes every criterion in §6. The charter rule that a
gate's own header states what it does NOT check is the mitigation §4 leans on for all three refusals,
and it lands unobserved.

**Fix.** Add a criterion enumerating the header's required contents — the four recognised definition
forms, the three refusals, and the untokenizable-file return — asserted against the shipped docstring
rather than the README.

**Left-shift.** The same S2-versus-§6 lint H1 asks for. Both findings are the same shape in two specs,
which is what makes the arm worth building rather than fixing twice by hand.

### M3 — unit 14's first non-goal disowns violations nobody owns

**Address:** unit 14 §3, first bullet. Folds raw id 30.

The non-goal says the shell FILENAME cell "is armed already and its four violations are a
`TOOL-aSurfacedLexicon-5` concern". Both halves are false at every order this unit could land.

`--check` grades three predicates — verb, suffix, layer — and no filename cell; the tracked
`.lexicon.conf` carries no `CELLS` block at all. Unit 6 names `sh.file` at 94 tracked files as one of
the undeclared cells "that no run will ever name", and the first `sh.file` row lands with unit 12's
matrix at order 7. Unit 5's own Files-touched table reads "NO `CELLS` row: this unit arms nothing",
and its `sh.file` numbers come from scratch declarations.

So the four violations this spec disowns are owned by nobody, and a reader takes "armed already" as
coverage that does not exist — which is the green-by-absence class the build is closing.

**Fix.** Rewrite the non-goal to say the shell filename cell is UNDECLARED today and lands with unit
12's matrix at order 7, name the measured violation count with the command that produced it, and say
plainly that this unit does not close it.

**Left-shift.** Spec lint: a non-goal that routes work to a named unit reds if that unit's spec does
not name the same artifact. It is the same cross-reference the M4 fork defect needs, applied to §3
instead of §8, and this build has now produced the class in both sections.

### M4 — unit 14's shebang deferral routes to a unit that lands first and never heard of it

**Address:** unit 14 §8 F1, final sentence. Folds raw id 55.

F1 says "a shebang-keyed language axis is a `LANGS` grammar change and belongs with
`TOOL-aSurfacedLexicon-9`, which is already widening that grammar". Unit 9 carries `order 3` — one
step AHEAD of unit 14's order 4 — so the unit receiving the deferral will already have shipped.
`grep -c shebang` over unit 9's spec returns **0**. And unit 9 does not own the grammar F1 assigns it:
its S2 reads "INHERITED, not built here: the row-key grammar... is `TOOL-aSurfacedLexicon-4`'s generic
`_parse_block` default." Unit 9 widens `PATTERNS` and `PATTERN_SETS`, not the `LANGS` key axis.

So the eightieth unarmed carrier, `.githooks/pre-commit`, is routed to a unit that cannot receive it,
and the deferral reads as handled while nothing handles it.

**Fix.** File the shebang axis as its own backlog row and cite that id in F1, or route it to a unit at
an order after 4. Keep the half of the recommendation that is right — that the run NAMES the unreached
carrier — since that is what keeps it out of the denominator.

**Left-shift.** Spec lint: a fork deferring work to a named unit reds if that unit's order is not
strictly higher, or if that unit's spec does not name the deferred subject. This is the same arm H2
proposes for criteria, widened one section; building it once covers both.

### M5 — unit 7 mints a classifier, helpers and emitters, names none, and budgets no pin movement

**Address:** unit 7 §4 `### Files touched (estimate)`, with no criterion in §6. Folds raw id 15.

The unit mints a classifier in the corpus walk (S1), report helpers (S2, S6) and the pin-row emitters
(S4). Files-touched names no identifier, runs none through `--suggest`, and budgets no pin movement —
in the very unit that redefines what the pin counts.

The consequence is the H5 consequence with a different address: `VERB_OFFENDER_PIN` has zero headroom,
offenders count per occurrence, and one minted name leading with an undeclared verb reds `lexicon
naming predicates`, the leg §7 nominates as the one that carries the verdict. Unit 4's S9 already made
the comparison two-sided, so a minted offender moves the exact counts AC4 and AC7 hard-code, in the
direction that reds.

It is a medium rather than a high only because unit 7's names are more likely to fall inside the table
than unit 14's parser is — `build`, `check`, `read`, `render` and `measure` all fit a classifier and
its report — but "likely" is not the standard this build set, and unit 5 and unit 6 both measured
rather than assumed.

**Fix.** Table the identifiers this unit mints with their `python tools/lexicon/lexicon.py --suggest`
verdicts, and state the resulting delta as zero or as a named raise, absorbed into whichever of the
two new pin rows H6's Migration line says owns it.

**Left-shift.** Covered by the H5 arm: any spec whose Files-touched names a path under a guard of
`lexicon naming predicates` must state a pin delta, and zero counts as long as it is stated.

## Low

### L1 — unit 7's §7 names a gate leg that does not exist

**Address:** unit 7 §7, final sentence. Folds raw ids 34, 56.

§7 says "`memory-tree hygiene` grades this spec". Read out of the single source:

```
'memory hygiene'          | chunk records   | subject repo | guard None                                  | ceiling 12720
'memory-hygiene self-test'| chunk selftests | subject kit  | guard ['tools/lib/','tools/memory-tree/']    | ceiling 900
```

There is no leg named `memory-tree hygiene`. The string typed sits between the two real candidates,
and they have OPPOSITE reachability at the push boundary: one is unguarded and runs on every bar, the
other is a held selftest. Units 13 and 14 both name `memory hygiene` correctly in their own §7 lines,
so the spec set is inconsistent on the one leg all three share.

The three other ceilings §7 quotes — 300 for `lexicon naming predicates`, 880 for `lexicon selftest`,
330 for `lexicon wiring` — all check out against the manifest today. They are still numbers typed
beside the file that owns them, which is the class this build exists to remove, but they are not
wrong.

**Fix.** Replace with `memory hygiene`, read out of `tools/gate-legs.json` the way unit 6's §7 reads
its whole gate table.

**Left-shift.** A spec lint over §7: every backticked leg name must appear in `tools/gate-legs.json`.
One grep against a tracked JSON file, and it is the same single-sourcing rule the charter already
states for prose that nothing currently enforces at the spec layer.

## What this round says about the build

The dominant cause is not authorship, it is a missed pass. Nine of the fourteen specs were re-pinned
from `d0a18683` to `6c670b02` when the build discovered its base had moved. Three of the five that
were not are the three subjects here, and they produced three of the seven blockers between them.
That is a bookkeeping failure with a mechanical fix and a mechanical gate, and it should not be read
as three authors independently estimating.

The four remaining blockers are a different and more interesting shape, and they share one root: **a
spec written against a declaration state its own build order does not reach.** Unit 13 stages onto a
`py.function` cell that arrives at order 7. Unit 7 writes pin rows for the same absent cell and
attributes a two-cell total to it. Unit 14 arms a cell without naming the rule it grades by. Round 1
of the sibling audit produced three blockers of exactly this shape and its round 2 closed them by
saying, in each criterion, which declaration it is measured against. The same sentence closes four of
these. The arm proposed under B2 is now owed by two audit rounds and five blockers, and it is the
single highest-value thing this build could left-shift.

One thing worth naming as healthy: the three specs' DESIGNS survive this round intact. The prefix
selector's exclusion semantics, the shell parser's refusal set, and the DEBT/UNRULED classifier are
all sound, and no finding above asks for a different mechanism. Every one of the twenty-two rows is
spelling, arithmetic, or an unstated dependency.
