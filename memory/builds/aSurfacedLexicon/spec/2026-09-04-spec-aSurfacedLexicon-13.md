# TOOL-aSurfacedLexicon-13 — the prefix selector, routing a subset of a cell to a second convention

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base 6c670b02 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aSurfacedLexicon-13-spec-audit-round1.md) | spec-audit | TOOL-aSurfacedLexicon-14 TOOL-aSurfacedLexicon-7 |

<!-- /gen:spec-records -->

## 1. Goal

Let one cell's population split, so a named subset is graded against a different convention from the
rest of it. Without this, every language whose case is a function of ROLE rather than of surface — Go's
export rule, React's PascalCase components — can only be declared dark, because a single
`(language, surface)` cell that reds half a correct codebase is worse than no cell at all.

## 2. Scope (IN)

- **S1** — a selector on a `CELLS` row key, so a cell may declare a name-prefix subset routed to its
  own convention and its own arms. The subset leaves the parent cell's population and is graded once.
- **S2** — a declaration-time refusal when two selectors on one cell both match a name. An ambiguous
  route is refused where it is written, never resolved by declaration order.
- **S3** — a decorator selector for the `parser` mode, delivered through an ADDITIVE accessor that
  leaves the `extract` return shape byte-identical, because two drift-audit call sites unpack that
  shape positionally outside any catch that names `ValueError`.
- **S4** — each selector gets its own pin row, keyed on the selector'd cell string, so a subset's
  offender count ratchets separately from its parent's under owner ruling Q2. What an ABSENT selector
  pin means, and what "separately" costs an implementation, are stated in section 4 and observed by
  AC9.
- **S5** — the per-cell report from `TOOL-aSurfacedLexicon-6` prints a selector row beneath its parent
  with its own count, denominator and rule string, so a routed subset is visible rather than being a
  silent hole in the parent's denominator.
- **S6** — the failing case, observed against a NAMED declaration. This repo carries no `py.function`
  cell before order 7, so the break is staged against a SCRATCH `CELLS` block in the working-tree
  `.lexicon.conf`, never committed, the way `TOOL-aSurfacedLexicon-5` stages its own. Section 4 states
  what that declaration is and how much of the mechanism this tree can exercise against it.

## 3. Non-goals (OUT)

- Arming a `go`, `ts` or `tsx` cell. Those need a `LANGS` row and a pattern set, which is
  `TOOL-aSurfacedLexicon-9`, and the ruling on which convention each takes belongs to the owner who
  has that corpus.
- A general predicate language over names. The selector matches a literal prefix or a literal
  decorator name and nothing else; a regex selector is a second grading language inside a naming gate
  and is refused here for the same reason the shell probe is refused in `TOOL-aSurfacedLexicon-14`.
- Suffix and infix selectors. A prefix is what the two motivating populations actually use, and
  widening the matcher before a population needs it is the speculative half.
- Visibility as a first-class axis. Go's export rule is CASE-as-visibility and the prefix selector
  models it only where visibility happens to be spelled in the name; where it is not, the honest
  answer stays `dark`, and section 8 records that this unit does not close that gap.
- Declaring a `py.function` cell in the tracked `.lexicon.conf`. That row lands with
  `TOOL-aSurfacedLexicon-12`'s matrix at order 7 and arming it here would be a scope change, not a
  test fixture. Section 4 says what this unit measures against instead.

## 4. Design

### Data model

The selector rides on the `CELLS` row key rather than in a block of its own. A row key becomes
`<ext>.<surface>` optionally followed by one selector clause, and the selector clause names its kind
and its literal — a prefix, or a decorator name for the parser mode. The parent cell keeps its own
row and grades the complement.

Riding on the key rather than in a second block buys three things that a separate block does not. The
pin block is keyed on the cell string, so a selector'd key gets its own pin row for free (S4). The
report is keyed on the same string, so a selector'd row appears with no second lookup (S5). And one
cell's declaration stays in one place, which matters because the parent and the selector partition a
population and reading only one of them tells a reader the wrong denominator.

### How the subset is removed from its parent

A name matching a selector is graded ONCE, against the selector's convention and arms, and is
excluded from the parent's population. The alternative — grading it twice, once against each — makes
every routed name a guaranteed violation of one of the two cells, which is the failure mode the whole
mechanism exists to avoid.

The exclusion is what makes S2's ambiguity refusal necessary rather than fussy. If two selectors on a
cell can both match, the name's convention depends on which row the parser read first, and a naming
gate whose verdict depends on declaration order is not a declaration.

### The declaration every criterion is measured against

This repo's tracked `.lexicon.conf` carries no `CELLS` block at all, so there is no `py.function`
cell for a selector to hang off. `TOOL-aSurfacedLexicon-6` measured that gap at its rev-4 and names
`py.function` at 976, `py.type` at 41 and `js.function` at 69 as the non-empty pairs carrying no
`CELLS` row; the first `py.function` row lands with `TOOL-aSurfacedLexicon-12`'s matrix at order 7,
two orders after this unit. Rev-1's S6 staged a selector onto that parent anyway, which is a break
nobody can stage.

So every criterion in section 6 that grades a cell is measured against a SCRATCH DECLARATION, and
each one says so, the way `TOOL-aSurfacedLexicon-5` rev-4 phrases its own after the identical defect
was raised against it. A scratch declaration is a `CELLS` block written into the working-tree
`.lexicon.conf` and never committed: the engine resolves the repo root with
`git rev-parse --show-toplevel` at `tools/lexicon/lexicon.py:1184` and opens `root / CONF_NAME`
(`:89`, read at `:792` and `:935`), so it takes no `--conf` flag and no fixture repo is needed. The
corpus stays the real tracked tree, which is why the denominators below are still this repo's own,
and `.lexicon.conf` still changes for nothing at landing.

The general rule this unit adopts, because this build has now broken it twice: **a criterion naming
`python tools/lexicon/lexicon.py --check` against a NAMED CELL also names the declaration it is
measured against** — the tracked conf, a scratch block, or a synthetic fixture. A criterion naming
none of the three cannot be run, and section 6 no longer contains one.

### Order — this unit lands after TOOL-aSurfacedLexicon-6

Two things this unit observes belong to `TOOL-aSurfacedLexicon-6`: AC4's empty-subset refusal is that
unit's `DEAD CELL` arm, which its rev-4 lands ARMED, and S5's selector row prints beneath that unit's
per-cell report. `memory/guides/BUILD-METHOD.md` M6 permits two passes to run concurrently only when
neither reads a file the other produces as a contract or as an acceptance input; unit 6 is an
acceptance input here by AC4's own wording. Rev-1 sat at order 4 beside it, where a parallel step
makes the sequencing a hope rather than a guarantee.

This unit is therefore **order 5**, and `TOOL-aSurfacedLexicon-6` is a hard prerequisite. The other
unit at order 5, `TOOL-aSurfacedLexicon-7`, is not a dependency in either direction — nothing here
reads its classifier or its pin rows, and nothing there reads the selector. Its Files-touched names
`tools/lexicon/lexicon.py` and `tools/lexicon/selftest.py`, which this unit also writes, so M6's
first clause sequences the two within order 5 on write-set intersection alone.

### The selector's own pin row, and what an absent one means

S4 gives a selector'd key its own `PINS` row under `TOOL-aSurfacedLexicon-4`'s row grammar. Rev-1
left three properties unstated that an implementation could satisfy every criterion without having,
so they are stated here and observed by AC9.

A selector'd key with NO pin row of its own reads as a pin of `0`. It never inherits the parent's
count, and its offenders are never folded back into the parent's row. Folding is the exact
implementation that would satisfy all eight of rev-1's criteria while defeating the ratchet S4 exists
to build, which is why it is refused by name rather than left to taste.

"Ratchets separately" means a move on one row leaves the other's verdict alone, in both directions.
Under `TOOL-aSurfacedLexicon-4`'s S9 the comparison is two-sided — a count that falls reds exactly as
one that rises — so the property has to be observed from both ends, and AC9 stages one break per end.

The two rows are emitted blank-separated, because `TOOL-aSurfacedLexicon-4`'s S10 makes two `PINS`
rows on consecutive lines a refusal inside `load_conf`, on the unguarded `lexicon wiring` leg.

### Decorators without touching the frozen extract contract

`extract` and `extract_text` return `(functions, types, imports)` where each function entry is a
`(name, lineno)` pair, and that shape is frozen by contract because `drift-audit` derives both
operands of its marginal-offense-rate signal from it. Both consumers unpack positionally:
`tools/drift-audit/drift_report.py:835` and `tools/drift-audit/drift_report.py:941` each run
`for nm, _ln in got[0]`. Widening the pair to a triple raises `ValueError` at both. Rev-1 said the
second site catches it and degrades to an empty population. Read at the run's base, it does not:

```
$ sed -n '936,941p' tools/drift-audit/drift_report.py
        try:
            got = lex.extract_text(src, mode, pset)
        except (SyntaxError, ValueError):
            continue
        if got:
            for nm, _ln in got[0]:
```

The unpack at `:941` sits OUTSIDE the `try`, so the catch at `:938` never sees it. The first site has
the same shape: its `try` at `:829-831` catches `(SyntaxError, OSError)`, which does not name
`ValueError` at all, and its unpack sits at `:835`.

So the failure is LOUD, not silent, and it is loud on every bar. Line 941 sits in `_read_defs_at_sha`
(`:896`), called at `:1032` and `:1033` from `build_lexicon_marginal_offense_rate`, which is first in
`SIGNALS` (`:1423`) and runs bare at `:1536` — `out = [s(ctx) for s in SIGNALS]`, with no per-signal
except. The leg that runs it is unguarded:

```
$ python - <<'PY'
import json
legs = json.load(open("tools/gate-legs.json"))
for l in legs:
    if l["name"].startswith("drift-audit"):
        print(l["name"], "|", l.get("guard"), "|", l["chunk"])
PY
drift-audit selftest | ['tools/drift-audit/', 'tools/lib/'] | selftests
drift-audit wiring | None | wiring
drift-audit records | None | declarations
```

`drift-audit records` carries `guard None` and sits in the `declarations` chunk, so a lexicon-only
commit selects it and a widened entry shape reds the landing commit. Rev-1's paragraph about the
break being "invisible to the push bar in two independent ways" described the guarded
`drift-audit selftest` leg, where neither unpack site lives, and it is STRUCK.

The design conclusion is unchanged and now rests on the coupling alone rather than on an invented
silence: two call sites in another kit unpack this shape positionally, and neither of them is this
unit's to edit. So decorators arrive through a separate additive accessor that returns a decorator map
for the parser mode and an empty map for every other mode. Nothing existing changes shape, and a
probe-mode language declaring a decorator selector is a named refusal rather than a silently empty
subset.

### Inventory — what this tree can actually exercise, stated plainly

Measured on this worktree at the run's base `6c670b02`, through the kit's own extractor at
`tools/lexicon/lexicon.py:272`. Rev-1 attributed its figures to that extractor without a runnable
invocation; the walk is one command and it is written down here so a reader reproduces every number
rather than rebuilding the script:

```
$ python - <<'PY'
import subprocess, sys, pathlib
sys.path.insert(0, "tools/lexicon")
import lexicon as lex
files = subprocess.run(["git", "ls-files", "*.py"], capture_output=True, text=True).stdout.split()
names = [n for f in files for n, _ in lex.extract(pathlib.Path(f), "parser", "python-ast")[0]]
print(len(files), len(names),
      sum(n.startswith("test_") for n in names),
      sum(n.startswith("cmd_") for n in names))
PY
49 976 107 32
```

49 tracked `.py` files, 976 function definitions, of which 107 lead with `test_` and 32 with `cmd_`.
Those 139 are a real, in-repo, routable population and the ROUTING half of this unit is exercised
against them. Rev-1 read 47, 925, 106 and 31; every one of those reproduces exactly at `d0a18683` and
none of them reproduces on the tree this build lands on, which is why the header is re-pinned.

The VERDICT half is not exercised by that population as it stands, and this is the honest limit. All
139 already satisfy `snake`, which is the parent cell's declared convention in the scratch
declaration above, so routing them to `snake` moves no verdict and an arm built on that observation
could not fail. What produces a real RED is routing them to a DIFFERENT convention — declaring the
`test_` subset `pascal` reds all 107 from the tree with nothing staged into the corpus at all — and
that is the failing case this unit takes, deliberately, because it exercises the exclusion and the
verdict at once. The corpus is real; only the declaration grading it is scratch.

The population this mechanism was RULED IN for has no instance here at all. Measured on the same run:
zero PascalCase function definitions across all 49 tracked `.py` files, and zero type definitions
across all 8 tracked `.js` files. The recorded adopter's 1,072 PascalCase function bindings in
`.tsx` are cited from `TOOL-dScaffoldedMirror-13`, measured there against that adopter on 2026-08-24,
and are UNVERIFIED by this build — the rebuild research pass records that adopter's tree as outside
its read-only scope. So the components-and-exports fixtures are SYNTHETIC, and the owner ruling
record says so in as many words.

What the synthetic fixtures must therefore carry, because nothing in this tree will catch it for them:
a fixture corpus where the parent cell and the selector disagree, where a name matches no selector,
where a name matches two, and where a selector's subset is empty. The last one is a DEAD CELL under
`TOOL-aSurfacedLexicon-6` and the two units meet there — a selector matching nothing is a declared
check over an empty population, which is exactly what that unit refuses.

### Files touched (estimate)

`tools/lexicon/lexicon_conf.py` for the row-key grammar, `tools/lexicon/lexicon.py` for the routing,
the exclusion and the decorator accessor, `tools/lexicon/selftest.py` for the synthetic fixtures and
the staged breaks, `.lexicon.conf` for nothing at landing — this repo declares no selector row and no
`py.function` parent for one to hang off, and section 8 carries that fork.

### Alternatives rejected

A separate `SELECTORS:` block keyed back to a cell. Rejected under the three properties in the data
model above: it splits one partition across two blocks and costs a second lookup in both the pin
block and the report.

Widening the function entry to carry decorators. Rejected on the measured drift-audit coupling above:
two call sites in another kit unpack the pair positionally, both outside any catch that names
`ValueError`, and one of them runs on every bar.

Resolving overlapping selectors by declaration order. Rejected: it makes the verdict depend on line
order in a file whose whole job is to be a declaration.

Declaring the `py.function` parent in this unit's own commit so the break could be staged against the
tracked conf. Rejected: it arms a cell two orders before `TOOL-aSurfacedLexicon-12`'s matrix and
reopens the arming story `TOOL-aSurfacedLexicon-6` settled, which is a scope change bought to avoid
writing four words into a criterion.

## 5. Production-readiness checklist

- security — N/A. No write path, no network, no new input surface; the selector reads names the
  extractor already produced.
- perf / scale — the selector is a prefix test per definition over the 1045 P1 definitions this tree
  grades (`python tools/lexicon/lexicon.py --check` prints `graded=1045`), and the decorator accessor
  re-walks only parser-mode files. Rev-1's 1,047 was `TOOL-aSurfacedLexicon-6`'s WITH-STAGED reading
  inherited as though it were a property of the corpus. The `lexicon naming predicates` leg's ceiling
  in `tools/gate-legs.json` is 300 s and the landing run must re-measure rather than assume.
- a11y — N/A. A CLI gate with no user interface.
- i18n — the prefix matcher compares raw name bytes and does not lowercase, so it is not subject to
  the ASCII truncation filed as review finding D25 against `subtokens.py`. It inherits nothing from
  that path and adds no new instance of it.
- error / empty / loading states — an empty selector subset is a DEAD CELL and refuses; an ambiguous
  overlap refuses at declaration time; a decorator selector on a non-parser language refuses by name;
  a selector'd cell with no pin row of its own reads as a pin of `0` rather than inheriting one.
- observability — every selector prints its own report row under its parent, with its own count and
  denominator, so a routed subset is never a silent subtraction from a parent's number.
- risks — the drift-audit coupling in section 4 is the sharp one. Rev-1 called its failure a silent
  degrade to an empty population; measured at base it is an uncaught `ValueError` that reds
  `drift-audit records`, an unguarded leg, on every bar. It is mitigated by construction rather than
  by remembering: the accessor is additive, so the break cannot be reached by editing this unit's
  files, and AC8 asserts the arity inside this kit's own selftest.
- testing + left-shift gates — one failing case over a real in-tree population, the 107 leading-`test_`
  definitions routed to `pascal` and RED, measured against the scratch declaration section 4 names,
  plus synthetic fixtures for the four cases this tree has no population for, each named in section 4.
- migration / rollback — additive grammar. A conf declaring no selector parses and grades exactly as
  it does today, and reverting the commit reverts the capability with nothing left behind.
- user docs — `tools/lexicon/README.md` gains the selector grammar and the sentence that a selector
  matching nothing reds, and the rendered Skill's routing line gains it if the placeholder set moves,
  which the `lexicon wiring` leg's byte-compare enforces.

## 6. Acceptance criteria

**Every criterion below that grades a cell names the declaration it is measured against**, per
section 4's `### The declaration every criterion is measured against`. That declaration is a scratch
`CELLS` block in the working-tree `.lexicon.conf`, never committed, because this repo has no
`py.function` cell until order 7 and rev-1's criteria were phrased against a parent that does not
exist. The corpus is the real tracked tree either way, so every denominator below is this repo's own.

- **AC1** — With a scratch declaration arming `py.function snake` plus a selector routing the `test_`
  prefix to `pascal`, `python tools/lexicon/lexicon.py --check` exits non-zero, and the violation
  count it reports against that selector EQUALS the leading-`test_` figure section 4's walk returns
  over the same tracked corpus in the same session — 107 at this base, and whatever the walk returns
  on the day the unit lands. Zero new violations are reported against the parent. Removing the
  scratch block returns the run to the tracked declaration's verdict. The RED is observed and
  recorded before this unit is called done.
- **AC2** — With that same selector declared at `snake` in the same scratch declaration, the parent
  `py.function` row's graded count plus the selector row's count EQUALS the parent's graded count
  read with the selector clause removed, all three readings taken from
  `python tools/lexicon/lexicon.py --check` in the same session. That identity is what proves the
  exclusion, and it survives the next commit that adds a test — where rev-1's "falls by exactly 106"
  against a "pre-change count of 925" reds a correct build on arithmetic.
- **AC3** — With a scratch declaration arming `py.function snake` and two selectors on that cell both
  matching one staged definition name, `python tools/lexicon/lexicon.py --check` REFUSES naming both
  selector literals, and neither convention is applied. The break is staged, the RED observed, and
  the break unstaged.
- **AC4** — With a scratch declaration arming `py.function snake` and a selector declaring a prefix
  no name in that parent's population carries, `python tools/lexicon/lexicon.py --check` reds it as a
  DEAD CELL through `TOOL-aSurfacedLexicon-6`'s arm rather than reporting a clean zero. That arm is a
  hard prerequisite and section 4's `### Order` carries the sequencing it needs.
- **AC5** — With a scratch declaration arming `py.function snake` and a decorator selector on it,
  `python tools/lexicon/lexicon.py --check` grades the decorated definitions and, with that selector
  present, `python tools/drift-audit/drift_report.py --json` still reports its lexicon signals with
  `live` true and a non-empty population at both shas. A run with the signals degraded to `not_asked`
  fails this criterion.
- **AC6** — When a decorator selector is declared on a `probe`-mode language in a scratch
  declaration, `python tools/lexicon/lexicon.py --check` REFUSES naming the language and the mode,
  rather than grading an empty subset.
- **AC7** — When the synthetic component fixtures are run, `python tools/lexicon/selftest.py` covers
  the four cases this tree has no population for — parent and selector disagreeing, no match, double
  match, empty subset — and its header states that those fixtures are synthetic and why.
- **AC8** — When `python tools/lexicon/selftest.py` runs, an arm asserts that the function entries
  returned by `tools/lexicon/lexicon.py` still unpack as exactly two elements, which is the shape
  `tools/drift-audit/drift_report.py:835` and `:941` unpack positionally OUTSIDE any catch naming
  `ValueError`. Widening the pair raises there uncaught and reds `drift-audit records`, a leg with
  `guard None`, on every bar; this arm exists so the break is caught in this kit's own selftest
  first, not so a silent degrade is noticed later.
- **AC9** — With a scratch declaration arming `py.function snake`, a selector routing `test_` to
  `pascal`, and a `PINS` row for each of the two cells separated by one blank line — the selector's
  `conv` count at section 4's `test_` figure, the parent's at its own reading —
  `python tools/lexicon/lexicon.py --check` is green. Staging `def test_x` into a tracked `.py` file
  then REDS the SELECTOR's row and leaves the parent's green; staging `def loadUserData` instead REDS
  the PARENT's row and leaves the selector's green. With the selector's `PINS` row deleted, the
  selector reads as a pin of `0` and reds on its own count rather than folding it into the parent's.
  Both breaks are staged, both REDs observed, both breaks unstaged. This is the only criterion that
  observes S4, which rev-1 left with none.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `drift-audit selftest` · `drift-audit records` · `memory hygiene`

The two drift-audit legs are named because this unit's one sharp coupling lands in that kit's
consumers, and they have OPPOSITE reachability at the push boundary. `drift-audit records` carries
`guard None` and sits in the `declarations` chunk, so a lexicon-only diff selects it and it is where a
widened entry shape would red. `drift-audit selftest` is guarded on `tools/drift-audit/` and
`tools/lib/` and sits in the `selftests` chunk that no boundary runs, so a lexicon-only diff does not
select it and the landing run must invoke it explicitly rather than trust the bar to reach it. Both
readings are the output quoted in section 4. This unit adds no gate leg and therefore owes no ceiling
row and no `testsuite-count-waivers.txt` entry.

## 8. Open questions

- **F1 — should this repo's own `.lexicon.conf` declare a selector row at landing, or ship the
  capability undeclared?** Declaring the `cmd_` or `test_` subsets at `snake` costs nothing in
  verdicts, because all 139 already satisfy the parent convention, and it puts a live selector row in
  the file every adopter reads as the worked example. Against it: a row that can never fail is exactly
  the shape this build exists to remove, `TOOL-aSurfacedLexicon-6`'s report already prints the
  population rule that a declared row would restate, and a selector needs a parent — the `py.function`
  row does not land until `TOOL-aSurfacedLexicon-12`'s matrix at order 7, so declaring one here is a
  scope change rather than a fixture. Recommendation: ship undeclared, with the commented example in
  the conf beside the `CANON:` example, so the capability is legible from the file before it has been
  used.
- **F2 — does an unroutable visibility rule stay dark, or get a named refusal of its own?** The prefix
  selector models Go's export rule only where visibility is spelled in the name, and Go's is spelled
  in the CASE. A `go.function` cell therefore still has no honest convention here. Recommendation:
  stays `dark` with the reason written in the shipped default table, and no new refusal — a refusal
  naming a language nobody has declared is a check over an empty population.
- **F3 — build the selector in this rebuild, or file it as its own unit after?** The research record
  recommended out of scope, flagged not hidden, on the ground that a rebuild at 11 units goes to 13.
  RESOLVED (owner, 2026-09-04): build it in this rebuild, accepting the scope, and record that its
  fixtures are synthetic when they are written. Recorded in the build's owner-rulings record as Q10.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, from owner ruling Q10, which pulled this mechanism into the
  build against the research record's recommendation, and from the drift-audit unpack sites measured
  at writing time.
- rev-2 · 2026-09-05 · round-1 spec audit folded, five findings. Re-pinned from `d0a18683` to the
  run's base `6c670b02` and re-measured every population with the one command that produces it, now
  written into section 4 instead of attributed to an extractor: 49 files, 976 definitions, 107
  `test_`, 32 `cmd_`, 8 `.js` files, and a P1 population of 1045 rather than the with-staged 1,047
  inherited from a sibling. AC1 and AC2 re-phrased as identities read in one run, because rev-1
  embedded the stale literals as pass conditions and a correct build failed them on arithmetic. The
  only in-tree failing case could not be staged at all — it hung off a `py.function` cell that does
  not exist until order 7 — so this spec adopts `TOOL-aSurfacedLexicon-5`'s scratch-declaration idiom
  and every cell-grading criterion now names the declaration it is measured against. Added AC9 for
  the per-cell ratchet, the one scope item rev-1 left unobserved, and stated in section 4 what an
  absent selector pin means so the criterion has something to fail against. Moved from order 4 to
  order 5: two criteria consume `TOOL-aSurfacedLexicon-6`'s arms and BUILD-METHOD M6 forbids running
  the two concurrently. And the `ValueError` risk ran backwards — the unpack at
  `drift_report.py:941` is outside the catch at `:938`, `SIGNALS` runs bare at `:1536`, and
  `drift-audit records` has `guard None`, so the failure is loud on every bar rather than a silent
  degrade on a leg no boundary reaches. `TOOL-aSurfacedLexicon-4`, `TOOL-aSurfacedLexicon-5`,
  `TOOL-aSurfacedLexicon-6`, `TOOL-aSurfacedLexicon-7` and `memory/guides/BUILD-METHOD.md` were
  opened for this revision.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "route a subset of a population to a different naming rule
by name prefix or decorator"` returns no seam that fits. Its ranked candidates are `derive_rule_kind`
and `resolve_rule_pool` in `tools/govkit/govkit.py`, which resolve deploy rules for file copying and
share only the word, plus `eol_population` and `population` in the same kit, which are line-ending and
refusal populations. The one true structural neighbour it surfaced is
`vacuous-selector-empty-population.md` in the gotcha inventory, and that is the class this unit's
empty-subset case belongs to rather than a seam to extend. So: no existing seam fits, and the unit
extends the cell keying inside `tools/lexicon/lexicon.py` that `TOOL-aSurfacedLexicon-4` establishes,
because a selector is a cell key with one more field and building it anywhere else would put one
population's declaration in two files. The retrieval run then named the prior that decides the
decorator design: `TOOL-dScaffoldedMirror-13` is the deferral this unit partly discharges, and it is
where the adopter's 1,072 PascalCase bindings were measured.

Recall terms used: `python tools/memory-recall/query.py "has anything in this repo routed a subset of
a graded population to a different rule by name prefix, and how are synthetic fixtures justified when
no in-repo population exists" --terms "lexicon cell selector prefix decorator PascalCase component
export visibility synthetic fixture population subset convention" --k 8`.
