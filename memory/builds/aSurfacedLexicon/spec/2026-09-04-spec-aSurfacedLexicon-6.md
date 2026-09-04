# TOOL-aSurfacedLexicon-6 — the three cell refusals and the per-cell coverage report

**Status:** SPECCED · rev-4 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aSurfacedLexicon-5-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aSurfacedLexicon-5-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-9 |
| [2026-09-04-review-TOOL-aSurfacedLexicon-5-spec-audit-round2.md](../reviews/2026-09-04-review-TOOL-aSurfacedLexicon-5-spec-audit-round2.md) | spec-audit | TOOL-aSurfacedLexicon-5 TOOL-aSurfacedLexicon-9 |

<!-- /gen:spec-records -->

## 1. Goal

Give the (language, surface) cell matrix its refusals, so a declared cell that grades nothing reds
instead of reporting a reassuring zero, and an ungraded population with no cell row reds instead of
being silently skipped. The same unit makes every declared cell — dark rows included — appear in one
report that prints each cell's population RULE beside its count, because a count with no denominator
context reads as coverage when it is only a scope.

## 2. Scope (IN)

- **S1** — `UNDECLARED CELL`: a (extension, surface) pair with a non-empty EXTRACTED population and
  no `CELLS` row is a refusal. **EXTRACTED is the rule, and rev-2 left the word out, which made this
  scope item and AC2 disagree by two pairs.** The only population an UNDECLARED pair has is what
  `extract` at `tools/lexicon/lexicon.py:272` produces for that extension without being asked, which
  is `function` and `type` and nothing else. The `file` and `constant` surfaces are computed by the
  per-cell SELECTOR of section 4's data model, which runs only for a cell a `CELLS` row declares, so
  an undeclared one of those has no population to be non-empty and this arm cannot see it.
- **S1's exclusion is a real hole and the arm's own header states it**, per the charter's rule that
  a gate says what it does NOT check. Its live instances, measured at this base by `git ls-files
  '*.py' | wc -l` and its two siblings: `py.file` at 49, `sh.file` at 94 and `js.file` at 8 tracked
  files are undeclared cells that no run will ever name. Closing that needs a
  declaration-independent selector per surface, which is not scope this unit buys for an arm landing
  report-only, and a reader who takes a silent `UNDECLARED CELL` list as full coverage is exactly
  who the header sentence is written for. `UNDECLARED CELL` is the cell-level sibling of the shipped
  `UNDECLARED EXTENSIONS` arm at `tools/lexicon/lexicon.py:524`, which grades extensions and cannot
  see a surface at all. It lands REPORT-ONLY and is promoted to a refusal by the unit that supplies
  the rows making it green; `### Rollout` in section 4 measures why and states that promotion as an
  owed hand-off rather than as a routing.
- **S2** — `DEAD CELL`: a declared, armed cell whose population is zero is a refusal. Today the same
  fact is printed and does not red: `tools/lexicon/lexicon.py:745-747` emits `armed but grading
  nothing (reported, not a refusal)` and the current tree prints `.js suffix=0` on every green run.
  S2 promotes that line to a verdict and re-keys it from `(extension, predicate)` onto the declared
  cell.
- **S3** — the per-cell report: one row per `CELLS` row, in declaration order, including every
  `dark` row, printed on green as well as red. A declared cell absent from the report is a reporting
  bug and the report's own row count is asserted against the parsed `CELLS` row count.
- **S4** — every report row carries the POPULATION RULE that selected its denominator, as a short
  declared string beside the count, not the count alone. Owner ruling Q6 makes this obligatory
  rather than cosmetic, because `py.constant` arms on a population its own predicate selects.
- **S5** — the `py.constant` cell ships armed at the public-simple-assignment population with its
  rule string, and `.lexicon.conf` carries all three measured readings and the counting rule that
  produced them in a comment, so the next session reads them instead of re-deriving them. **This is
  the build's FIRST armed cell**, three orders ahead of the conf rewrite, and that ordering is
  load-bearing rather than incidental: S7 refuses a zero-row cell report, so this unit cannot land
  its own liveness assertion green without one declared row to print. The verdict the arming
  produces is stated here rather than discovered when the bar reds — 346 graded, 0 violations,
  narrowed from 544 module-body targets, per the walk and counting rule in section 4 — and AC9
  observes it. The `screaming` form itself is `TOOL-aSurfacedLexicon-5`'s and is a HARD
  prerequisite: without its `_FORMS` mapping this row grades nothing at all.
- **S5's arming boundary, and what the two siblings ACTUALLY say — both files were opened to write
  this.** `TOOL-aSurfacedLexicon-5` is amended and owes nothing further: its section 3 states the
  split in its own words, that the arming boundary is two units and not one, with this unit arming
  `py.constant` at build order 4 and `TOOL-aSurfacedLexicon-12` pasting the rest at order 7.
  `TOOL-aSurfacedLexicon-4` owes nothing either, because it never made the
  claim rev-2 attributed to it: its `### Migration` says that the conf rewrite pasting the real
  `CELLS` and `PINS` bodies is a later unit, and that a declaration not yet rewritten parses exactly
  as it does now. Both remain true of a tree carrying this unit's single row, so there is no
  contradiction to resolve. **Rev-2 asserted that both siblings denied this arming and that both had
  been amended to allow it. The unit-4 half was false twice — as a quotation of a sentence that file
  does not contain, and as a claim of an edit nobody made — and it was written without opening the
  file.** What survives from rev-2 is the dependency that matters: the conf rewrite must PRESERVE
  the `py.constant` row and its comment rather than author them. `TOOL-aSurfacedLexicon-12` commits
  to the COMMENT by name and to the row not at all — `grep -n "CELLS"` over its rev-4 prints
  nothing — which is the same gap `### Rollout` files as an owed item rather than assuming.
- **S6** — both refusals land with their failing case OBSERVED, and S2's costs nothing to stage:
  `js.type` is a zero population in this tree today. S1's failing case is observed in a
  `tools/lexicon/selftest.py` fixture repo whose declaration carries a complete matrix, with the
  promotion switch forced on — on the real tree at this build order the arm has three live hits and
  refusing them is not this unit's landing to make. See `### Rollout`.
- **S7** — a liveness assertion on the report itself: a run whose cell report has zero rows REFUSES
  rather than printing an empty table under a green line.

## 3. Non-goals (OUT)

- The `CELLS:` and `PINS:` block grammar. That is `TOOL-aSurfacedLexicon-4`, and this unit consumes
  the parsed rows rather than parsing them.
- The convention predicate itself, its six forms and its AMBIGUOUS verdict. That is
  `TOOL-aSurfacedLexicon-5`. This unit refuses cells; it does not grade names.
- The pin comparison in either direction. Owner ruling Q2 made the ratchet two-sided and that lives
  with the pin block in `TOOL-aSurfacedLexicon-4`.
- Deleting the shipped per-extension `DEAD PROBE` arm. Whether it survives alongside `DEAD CELL` is
  the first fork in section 8, and either answer is a separate edit.
- Draining the `py.file` violations. Owner ruling Q3 files those as their own unit. **There are
  EIGHT, not the seven that three records still carry.** Measured at this base by first-dot
  stemming: `git ls-files '*.py' | xargs -n1 basename | cut -d. -f1 | sort -u | grep -cvE
  '^[a-z0-9_]+$'` returns 8, the eighth being `check-kit-placeholders.py`, added by `5169cc8d` after
  the eight were counted. **Rev-2 routed the correction to the wrong file, and
  `TOOL-aSurfacedLexicon-4` was opened at rev-3 to find that out.** That spec declares no pin VALUE
  at all. `py.file.conv` appears there three times and every occurrence is a shape example, never a
  declared value: once in its section 4 key table, once as a non-integer refusal fixture, and once in
  an indented merge example. The load-bearing half of this sentence is that unit 4 declares no pin
  VALUE, which holds; rev-2 said the token appeared once, which does not,
  and its section 3 hands the pin rows' initial values to `TOOL-aSurfacedLexicon-7`, whose
  `--measure` emits them from a run — so no spec carries a 7 that a two-sided comparison could red.
  What does carry it is `memory/backlog/TOOL.md`, whose `TOOL-aSurfacedLexicon-15` row names seven
  basenames and asserts that unit 4's `PINS` block carries `py.file.conv 7`: wrong in the count and
  wrong in the attribution, in the row that sequences the rename after this unit. HAND-OFF owed by
  this unit, because it is the unit that owns population sizes: that backlog row takes the count 8
  and the eighth basename, and an emitted pin row inherits 8 from the measurement rather than from
  prose.
- **Widening the `lexicon naming predicates` leg guard to cover `.lexicon.conf`.** This was rev-1's
  AC8 and its F2 recommendation, and it is refused on prior art that design pass should have read.
  `TOOL-aSurfacedLexicon-4` OWNS the ruling — its own S8 was struck for exactly this at its rev-5,
  its section 3 and its Alternatives carry the measurements — and `tools/lexicon/kit.toml` states it
  in prose directly above the `[[gate_leg]]` block it governs. Re-measured here rather than
  inherited: with the pathspec staged into `tools/gate-legs.json`, `python tools/govkit/govkit.py
  selfcheck` exits 1 reporting that the guard falls into 0 declared classes, and that leg carries no
  `guard` key of its own, so it runs on every bar including the push boundary. rev-1's F2 priced the
  edit as one extra 300 s leg per conf edit; the real price is a red push. **The compensating check,
  because an exemption is not coverage:** a conf-only diff is still graded, by `lexicon wiring`,
  whose guard is empty and which reaches the declaration through `bash
  tools/lexicon/adopt-lexicon.sh --check`. Its guard key is PRESENT and valued `[]`, which is not the
  same thing as absent and is worth spelling because this paragraph said both in one breath; the
  behaviour is identical either way, so it runs on
  every bar — `GATE_FULL` or not, because `tools/run-gates/run-gates.sh:951` drops UNGUARDED legs
  out of the guard PASS rather than out of the run. **That is the whole of the guarantee, and
  rev-2's version of this sentence was false.** Rev-2 wrote that `.githooks/pre-push` sets
  `GATE_FULL=1` so the authoritative run stays total. The hook DECIDES; it does not force. Its
  comment at `.githooks/pre-push:164` records that the unconditional export is retired, and the
  export at `.githooks/pre-push:279` now sits behind eight predicates, EVERY one of which forces and
  none of which makes a run smaller: no recorded full green (`.githooks/pre-push:210`); a record
  that is not an ancestor of the pushed tip; a record more than `GATE_FULL_MAX_LAG=10` commits
  behind it (`.githooks/pre-push:184`); a tree fingerprint that does not reproduce at the sha the
  record names; a merge tip whose second parent the record does not cover; a diff touching the leg
  manifest; a recorded manifest blob differing from this tree's; and a push running the kit
  self-tests against a record earned with them HELD. When none fires, `.githooks/pre-push:282`
  exports `GATE_BASE` instead and every guard applies, so a conf-only push CAN be decided by a
  SCOPED run — and `lexicon naming predicates`, whose guard names `tools/`,
  `skills/session-kickoff/`, `.githooks/` and `.claude/`, is selected by none of those from a
  root-level conf. What the narrow guard loses is therefore an early signal from THAT leg, bounded
  by the eight predicates rather than unbounded, while the declaration itself is still graded at
  every push by the two unguarded legs.

## 4. Design

### Data model

A cell is the pair already keyed at `tools/lexicon/lexicon.py:546`, widened from
`(extension, predicate)` to `(extension, surface)` where surface is the closed set `function`,
`type`, `file`, `constant`. Each declared cell resolves to a record carrying four fields: the cell
key, the declared convention, the arms (`vocab`, `notail`), and a POPULATION RULE.

The population rule is a pair — a selector the engine runs, and a short human string the report
prints. The string is DECLARED beside the selector in the engine, never derived from a docstring:
a rule string derived from prose rots the moment the selector is edited and nothing compares them.

### Inventory

The report prints one row per declared cell. The row shape carries, in order: the cell key, the
declared convention or `dark`, the graded count, the denominator the rule selected FROM, and the
rule string. For the cell owner ruling Q6 arms, that reads as `py.constant screaming 346 graded of
544 module-body targets (rule: public simple assignments)`.

The denominator is the WIDER population the rule narrowed, not the graded count restated. A row
whose graded count equals its denominator is legal and common — `py.function` grades all 976 — and
the point of printing both is that `py.constant` does not.

**The identifiers this unit mints, with their cell and the `--suggest` verdict for each.** Rev-2
named none of them while `### Files touched` and AC10 both bound themselves to "this unit's public
module-level definitions", so the budget below had nothing to be a budget OF. There are four, all in
`tools/lexicon/lexicon.py`, and each verdict is `python tools/lexicon/lexicon.py --suggest <name>`
run at rev-3.

| Identifier | Cell | `--suggest` verdict |
|---|---|---|
| `measure_cells` | `py.function` | OK, leads with `measure`, which the declaration carries |
| `check_cells` | `py.function` | OK, leads with `check`, which the declaration carries |
| `CELL_POPULATION_RULES` | `py.constant` | refused: `cell` is not in the declared table |
| `UNDECLARED_CELL_ARMED` | `py.constant` | refused: `undeclared` is not in the declared table |

The two refusals are not defects and the distinction is the one `TOOL-aSurfacedLexicon-5` measured:
`--suggest` grades any string handed to it against the verb table, while the P1 predicate grades
FUNCTION DEFINITIONS only, so a module-body assignment sits outside its population entirely. Both
constants are SCREAMING, which is the convention of the `py.constant` cell this unit arms.

**The pin budget, measured rather than reserved.** All four staged into `tools/lexicon/lexicon.py`
at once, `python tools/lexicon/lexicon.py --check` reports `P1 verb graded=1047 offenders=461`
against `graded=1045 offenders=461` on the unstaged tree. **The offender delta is ZERO and this unit
raises no pin.** That is worth measuring rather than assuming, because `VERB_OFFENDER_PIN` has no
headroom at all: it stands at 461, `TOOL-aSurfacedLexicon-5` at order 3 takes it to 462 with the one
name it adds, and this unit lands at order 4 on top of that raise. Zero is not luck — both function
definitions lead with a table verb, and the two constants are invisible to that predicate. The same
staging moves the armed constant cell from 346 graded to 348, still at 0 violations, which is why
AC9 states both figures.

### The three verdicts, and which population each selects

`UNDECLARED CELL` selects (extension, surface) pairs the extractors produced a non-empty population
for, minus the pairs `CELLS` declares. EXTRACTORS, per S1, and that word is doing the work:
`extract` returns functions and types, so the arm's whole candidate space at this base is
`py.function`, `py.type`, `js.function` and `js.type`. Four candidates; `js.type` is empty at 0, and
this unit's one declared row is `py.constant`, which lies outside that space entirely rather than
subtracting from it. Three remain, which is how AC2's count follows from this definition instead of
standing beside it. `DEAD CELL` selects declared non-dark cells whose graded count is zero. The
report selects every `CELLS` row and refuses none of them. The three populations are deliberately
different: two of them can be empty in a healthy tree and the third cannot, which is why only the
third carries the liveness assertion in S7.

A `dark` cell row is a declared refusal and is exempt from `DEAD CELL` by construction — its
population is zero because nothing extracts it, and redding that would make the honest declaration
the failing one. It still prints a report row, which is the whole reason dark is written down.

### The measured populations this unit ships

Re-measured on this worktree at `693bcf96`, which is records-only ahead of this spec's base: `git
diff --name-only 6c670b02 693bcf96` returns nothing outside `memory/builds/`, so every figure below
reproduces at either sha. The walk is a module-body `ast` pass over the 49 files `git ls-files
'*.py'` returns. rev-1 measured the same three readings at `d0a18683` and is stale by the base
moving under it, not by disagreeing about the population.

**The counting rule, stated so a second party reproduces it**, because rev-1's prose was not precise
enough to and that imprecision is the defect underneath the stale numbers. Module BODY statements
only, with no descent into class or function bodies. Both `ast.Assign` and `ast.AnnAssign` are
counted. A bound name is an `ast.Name` reached through `Tuple`, `List` and `Starred` target nodes
ONLY, so `d[k] = v` and `obj.attr = v` bind nothing at module level here and contribute nothing.
The screaming test strips leading and trailing underscores, then requires a non-empty remainder
matching `[A-Z0-9_]+`.

| Population rule | graded | satisfying screaming | violations |
|---|---|---|---|
| All module-body targets, tuple unpack and `AnnAssign` included | 544 | 436 | 108 |
| Simple single-`Name` targets, `AnnAssign` included | 449 | 430 | 19 |
| Public simple targets, no leading underscore | 346 | 346 | 0 |

Two sensitivities, both of which produced a wrong number before the rule above was written down.
Dropping `AnnAssign` moves the three graded counts to 501, 406 and 312 — a 34-name swing on the
armed row alone. And counting every `ast.Name` under a target, rather than only the ones the rule
binds, moves the first row to 556; the 12-name gap is exactly the subscript and attribute targets.
That gap is the same 12 rev-1 recorded as UNRECONCILED between its own 527 and the research record's
539, so the discrepancy is now reconciled and the note claiming otherwise is withdrawn.

The third row is what owner ruling Q6 arms, and the reason the rule string is not optional is
visible in the table: the clean zero belongs to the population defined by excluding the leading
underscore, and the leading underscore is what correlates with mutable module state in this corpus.

### Rollout

This unit lands with exactly one `CELLS` row, and two of its three verdicts are split by that fact,
so the landing commit's own verdict set is stated here rather than assumed.

**`UNDECLARED CELL` (S1) lands REPORT-ONLY** — computed, printed, refusing nothing — behind a
default-OFF constant, `UNDECLARED_CELL_ARMED`, in `tools/lexicon/lexicon.py`. It has to. Re-measured
at rev-3 by calling `extract` at `tools/lexicon/lexicon.py:272` over the files `git ls-files '*.py'`
and `git ls-files '*.js'` return: the extracted candidate space is four pairs, of which three are
non-empty and carry no `CELLS` row — `py.function` at 976, `py.type` at 41 and `js.function` at 69 —
while `js.type` is 0. Armed at order 4, S1 would fire three refusals on the commit that lands it,
against a declaration whose matrix does not exist until order 7.

**The promotion is an OWED ITEM rather than a routing, because the receiver has never heard of it.**
Rev-2 wrote that the promotion belongs to `TOOL-aSurfacedLexicon-12`. Grepped over the whole spec
set at rev-3: `UNDECLARED CELL`, the report-only landing and the promotion constant appear in no
sibling spec, and `TOOL-aSurfacedLexicon-12` rev-4 contains no occurrence of `CELLS` at all — its
S1 rewrites the `PINS` region and says nothing about the matrix. A hand-off whose receiving spec
does not carry it is a deferral wearing a routing's clothes, which is the shape this unit exists to
abolish. So the item is stated here in the words the receiving unit must carry, for the orchestrator
to route:

> Whichever unit first writes a full `CELLS` matrix into `.lexicon.conf` sets
> `UNDECLARED_CELL_ARMED = True` in `tools/lexicon/lexicon.py` in the SAME commit, PRESERVES
> `TOOL-aSurfacedLexicon-6`'s `py.constant` row and its population comment, and observes the armed
> run green on the tracked tree before landing. A matrix that lands with the constant left off ships
> an arm that reports and can never refuse.

**`TOOL-aSurfacedLexicon-12` ACCEPTED IT** — its S14 and AC14 carry the three obligations above in
these words, and AC14 asserts the matrix and the constant land in the SAME commit over the commit
rather than over the tree, because the two landing separately is precisely the failure this
paragraph exists to prevent. The item was UNOWNED when this revision was written and stating that
plainly is what got it routed, so the sentence stays as the record of how it was closed rather than
being rewritten to look like it was always fine. That is the charter's land-dark-then-flip rule with its second half
actually assigned to someone.

**`DEAD CELL` (S2) lands ARMED and green.** It is re-keyed onto declared cells, so the only cell it
can see at this order is `py.constant` at 346 graded, and the shipped `.js suffix=0` report line
falls outside its population rather than being promoted into a red by it. AC1's failing case is a
`js.type` row, whose probe population is 0 — free to stage, per the same run.

**The report (S3) lands with one row, and that row is why S7 can land armed at all.** A zero-row
report REFUSES, so the `py.constant` arming and the liveness assertion are the same commit and not
two; splitting them would land a refusal that fires on its own landing, which is the shape S1 is
avoiding one paragraph up.

Revert is that one commit: one constant, one call site, one conf row and its comment.

### Files touched (estimate)

`tools/lexicon/lexicon.py` for the two refusals and the report, `tools/lexicon/selftest.py` for the
staged-break arms, `.lexicon.conf` for the `py.constant` row and its comment. No new module: the
research record's zero-new-top-level-modules constraint holds here because `govkit update`
classifies by iterating the receipt, so a file gov newly ships is outside the classification space.

`memory/map/generated/` is regenerated in the SAME commit, and that is a gate rather than tidiness.
Of the four names `### Inventory` mints, TWO reach `memory/map/generated/symbols.json`:
`measure_cells` and `check_cells`. The other two do not, and rev-3 checked rather than assumed —
that artifact's only non-def kind is `const-export`, which its four rows show is JavaScript-only, so
a Python module constant is indexed nowhere in it. The file already carries 21 rows, from `grep -c
'"tools/lexicon/lexicon.py"' memory/map/generated/symbols.json`, and takes 23. The leg that
byte-compares that artifact against a live re-derivation carries NO `guard` key, so it runs on every
bar including the push boundary. Measured at rev-3 with this unit's own four definitions staged:
`python tools/codebase-map/test_codebase_map.py` prints `FAIL test_generated_artifacts_are_fresh`,
and restoring the file returns that arm to `ok`. The regen is `python
tools/codebase-map/gen_map.py --write`, and `memory/map/features/lexicon.md` claims the new keys in
the same commit, which the charter's Definition of Done requires anyway.

### Alternatives rejected

Printing the count alone and putting the rule in the README. Rejected under owner ruling Q6: the
mitigation is the line the reader sees on the run, and a README is not on the run.

Deriving the rule string from the selector function's docstring. Rejected because that is a second
carrier of one fact with no gate comparing them, which is the class this build exists to close.

Making `DEAD CELL` a warning rather than a refusal. Rejected: the shipped code already warns, on
every green run, and the warning has stood for the whole life of the declaration without anything
changing. A warning nobody acts on is the green-by-absence class wearing a different label.

Pulling the whole `CELLS` matrix into this unit so `UNDECLARED CELL` could land armed. Rejected as
scope theft with a hidden cost: the matrix's rows are conventions this unit has not measured and its
predicate does not own, and authoring them here to green one arm would put four cells' worth of
undebated verdicts on the bar. The report-only landing buys the same safety for one constant.

## 5. Production-readiness checklist

- security — N/A. The unit adds no write path, no network call and no new input surface; it reads
  the declaration the engine already reads.
- perf / scale — the report is a walk over declared rows, bounded by the `CELLS` block, and the two
  refusals reuse the corpus walk that already runs. The `lexicon naming predicates` leg's ceiling is
  300 s in `tools/gate-legs.json`; the addition is not expected to approach it and the landing run
  must confirm rather than assume.
- a11y — N/A. A CLI gate with no user interface.
- i18n — N/A. Machine-facing output in one language, and the wider non-ASCII identifier gap is filed
  as review finding D25 against `subtokens.py` rather than owned here.
- error / empty / loading states — the empty case IS the product: a zero-row report refuses (S7), a
  zero-population armed cell refuses (S2), and a dark row prints as a refusal rather than as
  absence.
- observability — every declared cell appears on every run, green included, with its count, its
  denominator and its rule. The report-only `UNDECLARED CELL` list prints on every run too, so the
  three pairs it names are visible for however long the promotion stays unowned, rather than
  accruing invisibly. What that list does NOT show is the `file` and `constant` surfaces S1
  excludes, and the arm's header says so on the same run.
- risks — the live one is the hand-off, and at rev-3 it is worse than rev-2 described. `UNDECLARED
  CELL` ships behind a default-OFF `UNDECLARED_CELL_ARMED`, and rev-2 said the flip belonged to
  `TOOL-aSurfacedLexicon-12`. That spec has never carried it: grepped at rev-3, no sibling spec
  mentions the arm, the report-only landing or the constant, and unit 12's rev-4 names no `CELLS`
  block at all. So the flip is UNOWNED, not merely deferred, and a matrix landing with the constant
  off leaves an arm that reports and can never refuse — the exact shape this unit exists to abolish.
  `### Rollout` states the owed paragraph in the words the receiving unit must carry, which is the
  most this unit can do about a file another agent owns. The former risk here, the leg guard gap, is
  closed: section 3 refuses the widening on measurement.
- testing + left-shift gates — both refusals get a staged-break arm in `tools/lexicon/selftest.py`,
  S2's break needs no staging at all in this tree, and S1's runs in the fixture repo with the
  promotion constant forced on so the refusing half is observed at THIS unit's landing rather than
  at order 7.
- migration / rollback — the conf gains one row and a comment and the engine gains one default-OFF
  constant, per `### Rollout`; reverting the commit reverts all three. No stored state, no artifact
  to migrate — but `memory/map/generated/` is regenerated in the same commit and reverts with it.
- user docs — `tools/lexicon/README.md` gains the three verdicts and what each does NOT check,
  including that `UNDECLARED CELL` reports rather than refuses until the matrix lands, and the
  rendered Skill's byte-compare on the `lexicon wiring` leg forces the re-render if a placeholder
  moved.

## 6. Acceptance criteria

- **AC1** — When a `js.type pascal` row is added to `.lexicon.conf` and nothing else is staged,
  `python tools/lexicon/lexicon.py --check` exits non-zero naming `js.type` as a DEAD CELL; with the
  row removed it exits `0`. The population is zero across the 8 tracked `.js` files that `git
  ls-files '*.js' | wc -l` returns, and `python tools/lexicon/lexicon.py --check` prints `.js
  suffix=0` and exits `0` on this tree today, so the break costs nothing to stage.
- **AC2** — When `python tools/lexicon/lexicon.py --check` runs with nothing staged, the `UNDECLARED
  CELL` report names exactly three pairs — `py.function` at 976, `py.type` at 41 and `js.function`
  at 69 — and the run still exits `0`, because the arm lands report-only per `### Rollout`. **Three
  is DERIVED from S1 and not asserted beside it, which is what rev-2 got wrong.** S1's population is
  the EXTRACTED one, so the candidate space is the four pairs `extract` produces; `js.type` is empty
  at 0 and drops out, and `py.constant` is declared but was never in that space. This criterion
  moves if and only if that walk moves. It does NOT cover `py.file` at 49, `sh.file` at 94 or
  `js.file` at 8, and the arm's header says so — a reader who reads three as the whole undeclared
  population is reading a scope as a coverage claim, which is the defect this unit was written
  against. The REFUSING half is observed in a `tools/lexicon/selftest.py` fixture repo whose
  declaration carries a complete matrix and whose promotion constant is forced on: staging a `class
  Cap {}` definition into that fixture's `.js` file while it declares no `js.type` row exits
  non-zero naming `js.type` as an UNDECLARED CELL, and unstaging returns the fixture run to `0`.
- **AC3** — When `python tools/lexicon/lexicon.py --check` runs green, the cell report prints one
  row for every row of the `CELLS` block in `.lexicon.conf`, dark rows included, and a
  `tools/lexicon/selftest.py` arm asserts the printed row count equals the parsed row count.
- **AC4** — When the report prints the constant cell, the row carries the graded count, the wider
  denominator and the rule string in one line, and a `tools/lexicon/selftest.py` arm reds on a row
  carrying a count with no rule string.
- **AC5** — When `.lexicon.conf` is read, its constant-cell comment carries the counting rule from
  section 4 and all three measured readings — 544 against 436, 449 against 430, and 346 against 346
  — each with the command that produced it, and a `tools/lexicon/selftest.py` arm asserts the armed
  row names the third. The RULE and the command are what the comment is for: three number pairs
  nothing re-derives are a second carrier, and the reading behind them is the half that rotted last
  time.
- **AC6** — When the cell report's row source is emptied so it would print no rows,
  `python tools/lexicon/lexicon.py --check` REFUSES naming the empty report rather than exiting `0`;
  the break is staged, the RED observed, and the break unstaged.
- **AC7** — When the existing per-extension arm is exercised by declaring an armed extension the
  corpus contains no definitions for, `python tools/lexicon/lexicon.py --check` still prints its
  `DEAD PROBE` refusal, so this unit is proven not to have replaced it by accident.
- **AC8** — STRUCK at rev-2, number retained so no cross-reference dangles. It required a conf-only
  diff to select the `lexicon naming predicates` leg, and mandated the guard edit that would buy
  that. The edit reds `govkit selfcheck`, an unguarded leg running on every bar including the push
  boundary; `TOOL-aSurfacedLexicon-4` owns the ruling and struck its own equivalent scope item for
  it, and section 3 carries the disposition with this unit's own re-measurement. The conf-only
  observation AC2 and AC5 need runs through `lexicon wiring`, whose guard is empty, and through the
  direct command.
- **AC9** — When `py.constant screaming` is armed and nothing is staged, `python
  tools/lexicon/lexicon.py --check` reports the constant cell at 0 violations of 346 graded,
  narrowed from 544 module-body targets, with its rule string present; both figures are the section
  4 walk's under the counting rule stated there. Staging a module-body `public_thing = 1` into a
  tracked `.py` file REDS that cell naming the offender, and unstaging returns it to 0 of 346. **346
  of 544 is the BASE tree, and the landing commit's own reading is 348 of 546**, because this unit
  mints two public module-body constants of its own and they are in the population it arms —
  measured at rev-3 by running the section 4 walk with all four `### Inventory` names staged. The
  criterion is observed against the tree AS THE COMMIT LANDS IT, so it reads 348 there; rev-2 stated
  only the base figure, which its own code would have falsified on the commit that landed it.
- **AC10** — When this unit's two public function definitions, `measure_cells` and `check_cells`,
  are added to `tools/lexicon/lexicon.py`, `python tools/codebase-map/test_codebase_map.py` first
  prints `FAIL test_generated_artifacts_are_fresh`; after `python tools/codebase-map/gen_map.py
  --write` and the matching claim in `memory/map/features/lexicon.md` it returns that arm to `ok`.
  BOTH states are observed, in that order — a passing freshness arm after a regen proves only that
  the regen ran. The two names are stated rather than left as "this unit's public definitions",
  which is what rev-2 wrote and which made the criterion unobservable by anyone but its author; the
  RED half is already observed at rev-3 with exactly these definitions staged.
  `CELL_POPULATION_RULES` and `UNDECLARED_CELL_ARMED` are deliberately absent from this criterion:
  `symbols.json` indexes no Python module constant, so they move that artifact by nothing.

## 7. Gates

| Leg | chunk | subject | guard | ceiling |
|---|---|---|---|---|
| `lexicon naming predicates` | declarations | repo | `tools/` · `skills/session-kickoff/` · `.githooks/` · `.claude/` | 300 s |
| `lexicon selftest` | selftests | kit | `tools/lexicon/` | 880 s |
| `lexicon wiring` | wiring | repo | none | 330 s |
| `codebase-map coverage + freshness` | declarations | repo | none | 300 s |
| `memory hygiene` | records | repo | none | 12720 s |
| `spec tokens (a spec's own names resolve)` | declarations | repo | none | 60 s |

Read out of `tools/gate-legs.json` rather than typed from memory, which is also where a reader
should re-read them.

**`lexicon selftest` IS INVISIBLE TO THE PUSH BAR, and most of this unit's criteria live inside it.**
It is chunk `selftests`, which `GATE_FULL=1` HOLDS rather than runs, and only `GATE_SELFTESTS=1`
reaches it — a variable no boundary sets and which `.githooks/gate-env.sh` explicitly refuses to let
a hook set. The arms behind AC3, AC4, AC5 and AC9, and AC2's fixture-repo half, are all in that leg,
so a green push certifies none of them and a reader must not take one as covering them.
**This unit's DoD run is therefore `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.** The
compensation for the gap is the two unguarded legs that DO fire at a push: `codebase-map coverage +
freshness` catches AC10's stale artifact, and `lexicon naming predicates` grades the real tree, so an
implementation that broke the armed constant cell or the report reds at the push boundary even with
every selftest held.

This unit adds no gate leg, so it owes no wall-clock ceiling row and no
`testsuite-count-waivers.txt` entry. It adds arms to the existing `lexicon selftest` leg, whose
declared ceiling is 880 s; the landing run must re-measure that leg rather than assume the arms are
free, and the current cost is UNVERIFIED here because the research pass did not run it.

## 8. Open questions

- **F1 — does the shipped per-extension `DEAD PROBE` arm survive beside `DEAD CELL`, or is it
  subsumed?** `DEAD CELL` is strictly finer wherever a cell is declared: it fires on `js.type` where
  `DEAD PROBE` cannot, because `DEAD PROBE` sums the verb and suffix populations per extension at
  `tools/lexicon/lexicon.py:606-614` and `.js` keeps a healthy 69 functions — measured by the
  shipped `js-regex` probe over the 8 files `git ls-files '*.js'` returns, correcting rev-1's 122,
  which was an older base's figure. The argument is unchanged by the correction, because 69 is just
  as non-zero. But the two arms select different populations at the edges — an armed extension with
  no `CELLS` row at all is invisible to `DEAD CELL` and visible to `DEAD PROBE`. Recommendation:
  keep both, and make the report say which arm owns which population, because a refusal whose scope
  a reader has to derive is the class this build is closing.
- **F2 — widen the `lexicon naming predicates` guard to include the declaration, or leave the conf
  to the wiring leg?** RESOLVED at rev-2, AGAINST rev-1's own recommendation and by adopting
  `TOOL-aSurfacedLexicon-4`'s disposition by reference rather than re-deriving it: the widening is
  refused, section 3 carries it as a non-goal with the `govkit selfcheck` measurement and the
  compensating check, and AC8 is struck. rev-1 priced the edit at one extra 300 s leg per conf edit
  and the real price is a red push, which is the difference between a cost and a defect. The
  conf-only observation the remaining criteria need runs through `lexicon wiring`, whose guard is
  empty, and through the direct command.
- **F3 — which population does the constant cell arm on?** Three readings are defensible and only
  one yields a clean zero, and it is clean because the predicate selects the names it grades.
  RESOLVED (owner, 2026-09-04): arm it on the public simple targets, with the per-cell report
  printing the population rule beside the count as the non-optional mitigation. Recorded in the
  build's owner-rulings record as Q6. The count that reading yields is 346 at this base; rev-1's 331
  was the same reading at an older one.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, from the rebuild research record's unit U5 plus owner ruling
  Q6, which adds the population-rule obligation and the constant cell that makes it load-bearing.
- rev-2 · 2026-09-04 · round-1 spec audit folded, ten findings. Re-pinned to the siblings' base and
  re-measured every population with its command and, for the first time, with the counting rule that
  makes it reproducible. AC8 and F2's guard mandate STRUCK on re-measurement, adopting
  `TOOL-aSurfacedLexicon-4`'s ruling. A `### Rollout` subsection added, landing `UNDECLARED CELL`
  report-only so it does not refuse on its own landing commit. Added AC9 for the arming verdict this
  spec never stated and AC10 for the generated-map regen it never budgeted; section 7 became a
  per-leg table that discloses the selftest leg's invisibility to the push bar; section 10
  re-grounded on the CLOSED record rather than a WONTDO one.
- rev-3 · 2026-09-04 · round-2 audit of rev-2's own fold, five defects, every one of them a claim
  rev-2 made about a file it had not opened or a number it had not run. `.githooks/pre-push`,
  `TOOL-aSurfacedLexicon-4`, `TOOL-aSurfacedLexicon-5`, `TOOL-aSurfacedLexicon-7`,
  `TOOL-aSurfacedLexicon-12` and `memory/backlog/TOOL.md` were opened for this revision. The
  compensating check in section 3 rewritten: the push hook DECIDES rather than forcing
  `GATE_FULL=1`, and the guarantee is the two unguarded legs, not a total run. The unit-4 arming
  contradiction WITHDRAWN — that spec never made the claim rev-2 quoted and owes no edit. The
  `py.file` pin correction re-routed off unit 4, which declares no pin value, onto the backlog row
  that actually carries the 7. S1's population rule given the word EXTRACTED it was missing, so
  AC2's three now follows from the definition, with the `file`-surface hole stated rather than
  hidden. The `UNDECLARED CELL` promotion restated as an UNOWNED item with the exact text its
  receiver must carry, because no sibling spec has ever mentioned it. And `### Inventory` now names
  the four identifiers this unit mints, each with its `--suggest` verdict and a measured pin budget:
  zero offender delta, no pin raise.
- rev-4 · 2026-09-04 · cross-spec reconciliation, single-writer. FIVE wrong claims about siblings, all written
  without the sibling open or written before it moved: unit 4 pinned at a rev it has left and called
  untouched, unit 5 placed at build order 2 where its header says 3, `py.file.conv` said to appear
  once in unit 4 where it appears three times, `lexicon wiring` said to carry no `guard` key in the
  same sentence that called its guard empty, and one hyphenated-basename count left at seven. The
  UNOWNED promotion is now OWNED — `TOOL-aSurfacedLexicon-12` accepted it as S14/AC14 — and the
  paragraph that reported it unowned stays, as the record of how it got routed.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a declared check whose graded population is zero
and report each cell's population rule"` ranks `check` and `report` as seams, and the affordance
line for `run-gates` under the stems `declar` and `popul`. None of them is the seam this unit
extends. The seam is inside the lexicon kit and the probe surfaced it obliquely rather than by name:
the verdict half extends `run` in `tools/lexicon/lexicon.py`, which already owns three refusal
populations (`UNDECLARED EXTENSIONS` at `:524`, `DEAD PROBE` at `:612`, `DEAD SNIFFER` at `:665`)
and one report-only line at `:747`. This unit adds a fourth and a fifth refusal to that same list
and promotes the report-only line, rather than adding a checker beside it. The retrieval run also
named `vacuous-selector-empty-population.md` in the gotcha inventory, which is the class both
refusals belong to.

**The prior art that actually decides the report's shape is `TOOL-dScaffoldedMirror-2`, which is
CLOSED**, and rev-2 re-grounds this section on it. That record established print-on-green: split the
population per PREDICATE, print the graded, offender and waived counts on green as well as red, and
red on an armed predicate whose population is zero. Two things about it are worth carrying rather
than merely citing. Its last clause DID NOT SHIP — the tree prints `armed but grading nothing
(reported, not a refusal)` at `:747` and exits `0`, which a live `--check` run confirms — so a CLOSED
row stands claiming a red that does not exist, S2 is rebuilding a dropped half rather than inventing
a refusal, and nothing records the descope. That correction is owed to the backlog row, and this
unit is where it surfaced.

rev-1 cited `TOOL-dScaffoldedMirror-3` here instead, as the ruling that established the report
shape. That row is WONTDO and its own header records that a later unit deleted its justification. A
decision NOT to do something ratifies nothing, so the citation is WITHDRAWN rather than re-labelled,
and the reuse audit no longer certifies prior art that was never built.

Recall terms used: `python tools/memory-recall/query.py "why does the lexicon refuse an armed check
whose population is zero, and what must a per-cell report print beside a count" --terms "lexicon
DEAD PROBE vacuity armed cell green-by-absence population denominator coverage sniffer graded pin
refusal" --k 8`.
