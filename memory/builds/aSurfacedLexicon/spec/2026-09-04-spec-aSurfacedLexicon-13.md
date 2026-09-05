# TOOL-aSurfacedLexicon-13 — the prefix selector, routing a subset of a cell to a second convention

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base d0a18683 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

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
  shape positionally and one of them swallows the failure.
- **S4** — each selector gets its own pin row, keyed on the selector'd cell string, so a subset's
  offender count ratchets separately from its parent's under owner ruling Q2.
- **S5** — the per-cell report from `TOOL-aSurfacedLexicon-6` prints a selector row beneath its parent
  with its own count, denominator and rule string, so a routed subset is visible rather than being a
  silent hole in the parent's denominator.
- **S6** — the failing case, observed. This tree carries a real routable population and section 4
  states exactly how much of the mechanism it can and cannot exercise.

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

### Decorators without touching the frozen extract contract

`extract` and `extract_text` return `(functions, types, imports)` where each function entry is a
`(name, lineno)` pair, and that shape is frozen by contract because `drift-audit` derives both
operands of its marginal-offense-rate signal from it. Both consumers unpack positionally:
`tools/drift-audit/drift_report.py:835` and `tools/drift-audit/drift_report.py:941` each run
`for nm, _ln in got[0]`. Widening the pair to a triple raises `ValueError` at both — and the second
site catches `ValueError` at `tools/drift-audit/drift_report.py:938` and continues, so the signal
would degrade to an empty population rather than fail loudly.

That failure would also be invisible to the push bar in two independent ways, which is the reason this
is a design constraint rather than a cleanup: the `drift-audit selftest` leg carries the guard
`tools/drift-audit/` and `tools/lib/`, so a lexicon-only commit does not select it, and it sits in the
`selftests` chunk, which no boundary runs.

So decorators arrive through a separate additive accessor that returns a decorator map for the parser
mode and an empty map for every other mode. Nothing existing changes shape, and a probe-mode language
declaring a decorator selector is a named refusal rather than a silently empty subset.

### Inventory — what this tree can actually exercise, stated plainly

Measured on this worktree at `d0a18683` on 2026-09-04 through the kit's own extractor over the 47
tracked `.py` files: 925 function definitions, of which 31 lead with `cmd_` and 106 lead with `test_`.
Those 137 are a real, in-repo, routable population and the ROUTING half of this unit is exercised
against them.

The VERDICT half is not, and this is the honest limit. All 137 already satisfy `snake`, which is the
parent cell's declared convention, so routing them to `snake` moves no verdict and an arm built on
that observation could not fail. What produces a real RED here is routing them to a DIFFERENT
convention — declaring the `test_` subset `pascal` reds all 106 from the tree with nothing staged —
and that is the failing case this unit takes, deliberately, because it exercises the exclusion and the
verdict at once.

The population this mechanism was RULED IN for has no instance here at all. Measured on the same run:
zero PascalCase function definitions across all 47 tracked `.py` files, and zero type definitions
across all 11 tracked `.js` files. The recorded adopter's 1,072 PascalCase function bindings in
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
the staged breaks, `.lexicon.conf` for nothing at landing — this repo declares no selector row, and
section 8 carries that fork.

### Alternatives rejected

A separate `SELECTORS:` block keyed back to a cell. Rejected under the three properties in the data
model above: it splits one partition across two blocks and costs a second lookup in both the pin
block and the report.

Widening the function entry to carry decorators. Rejected on the measured drift-audit coupling above,
where one of the two break sites swallows the exception and degrades to a clean-looking zero.

Resolving overlapping selectors by declaration order. Rejected: it makes the verdict depend on line
order in a file whose whole job is to be a declaration.

## 5. Production-readiness checklist

- security — N/A. No write path, no network, no new input surface; the selector reads names the
  extractor already produced.
- perf / scale — the selector is a prefix test per definition over a population of 1,047 here, and the
  decorator accessor re-walks only parser-mode files. The `lexicon naming predicates` leg's ceiling in
  `tools/gate-legs.json` is 300 s and the landing run must re-measure rather than assume.
- a11y — N/A. A CLI gate with no user interface.
- i18n — the prefix matcher compares raw name bytes and does not lowercase, so it is not subject to
  the ASCII truncation filed as review finding D25 against `subtokens.py`. It inherits nothing from
  that path and adds no new instance of it.
- error / empty / loading states — an empty selector subset is a DEAD CELL and refuses; an ambiguous
  overlap refuses at declaration time; a decorator selector on a non-parser language refuses by name.
- observability — every selector prints its own report row under its parent, with its own count and
  denominator, so a routed subset is never a silent subtraction from a parent's number.
- risks — the drift-audit coupling in section 4 is the sharp one, and it is mitigated by construction
  rather than by remembering: the accessor is additive, so the break cannot be reached by editing this
  unit's files.
- testing + left-shift gates — one in-tree failing case that reds 106 real definitions, plus synthetic
  fixtures for the four cases this tree has no population for, each named in section 4.
- migration / rollback — additive grammar. A conf declaring no selector parses and grades exactly as
  it does today, and reverting the commit reverts the capability with nothing left behind.
- user docs — `tools/lexicon/README.md` gains the selector grammar and the sentence that a selector
  matching nothing reds, and the rendered Skill's routing line gains it if the placeholder set moves,
  which the `lexicon wiring` leg's byte-compare enforces.

## 6. Acceptance criteria

- **AC1** — When a selector routing the `test_` prefix of the Python function cell to `pascal` is
  staged into `.lexicon.conf`, `python tools/lexicon/lexicon.py --check` exits non-zero reporting 106
  violations against that selector and zero new violations against its parent; unstaging the row
  returns the run to its pre-change verdict. The 106 is measured by the kit's own extractor over the
  47 tracked `.py` files.
- **AC2** — When that same selector is declared at `snake`, the parent Python function cell's graded
  count falls by exactly 106 and the selector's row reports 106, so the two sum to the parent's
  pre-change count of 925 and the exclusion is proven rather than assumed. Observed in the report
  printed by `python tools/lexicon/lexicon.py --check`.
- **AC3** — When two selectors on one cell both match a staged definition name, `python tools/lexicon/lexicon.py --check`
  REFUSES naming both selector literals, and neither convention is applied. The break is staged, the
  RED observed, and the break unstaged.
- **AC4** — When a selector declares a prefix no name in its parent's population carries,
  `python tools/lexicon/lexicon.py --check` reds it as a DEAD CELL through `TOOL-aSurfacedLexicon-6`'s
  arm rather than reporting a clean zero.
- **AC5** — When a decorator selector is declared, `python tools/lexicon/lexicon.py --check` grades
  the decorated definitions and, with the selector present, `python tools/drift-audit/drift_report.py --json`
  still reports its lexicon signals with `live` true and a non-empty population at both shas. A run
  with the signals degraded to `not_asked` fails this criterion.
- **AC6** — When a decorator selector is declared on a `probe`-mode language,
  `python tools/lexicon/lexicon.py --check` REFUSES naming the language and the mode, rather than
  grading an empty subset.
- **AC7** — When the synthetic component fixtures are run, `python tools/lexicon/selftest.py` covers
  the four cases this tree has no population for — parent and selector disagreeing, no match, double
  match, empty subset — and its header states that those fixtures are synthetic and why.
- **AC8** — When `python tools/lexicon/selftest.py` runs, an arm asserts that the function entries
  returned by `tools/lexicon/lexicon.py` still unpack as exactly two elements, which is the shape
  `tools/drift-audit/drift_report.py:941` unpacks positionally behind a `ValueError` catch.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `lexicon wiring` · `drift-audit selftest` · `drift-audit records` · `memory hygiene`

The two drift-audit legs are named because this unit's one sharp coupling lands in that kit's
consumers. `drift-audit selftest` is not selected by a lexicon-only diff and sits in the `selftests`
chunk that no boundary runs, so the landing run must invoke it explicitly rather than trust the bar to
reach it. This unit adds no gate leg and therefore owes no ceiling row and no
`testsuite-count-waivers.txt` entry.

## 8. Open questions

- **F1 — should this repo's own `.lexicon.conf` declare a selector row at landing, or ship the
  capability undeclared?** Declaring the `cmd_` or `test_` subsets at `snake` costs nothing in
  verdicts, because all 137 already satisfy the parent convention, and it puts a live selector row in
  the file every adopter reads as the worked example. Against it: a row that can never fail is exactly
  the shape this build exists to remove, and `TOOL-aSurfacedLexicon-6`'s report already prints the
  population rule that a declared row would restate. Recommendation: ship undeclared, with the
  commented example in the conf beside the `CANON:` example, so the capability is legible from the
  file before it has been used.
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
