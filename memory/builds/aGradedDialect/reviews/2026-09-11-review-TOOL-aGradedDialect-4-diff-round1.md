**Serves:** diff-review TOOL-aGradedDialect-4

# aGradedDialect — Tier-2 diff review of the `returns:jsx` selector, round 1

*Node `a`, 2026-09-11, branch `branch/lexicon-kit-typescript-34c322`. Adversarial pass over the
cumulative diff that adds the third CELLS selector kind to the lexicon kit (1.3 → 1.4): four primed
lens passes, five skeptic batches prompted to REFUTE, one synthesis. Every finding below was
re-executed at source in this worktree before it was written here; the regression claims were
re-executed against the base reader loaded beside the landed one in a single process.*

**Reviewed range: `75b85708c969f8ece0231b5910542447c47748df...400859c6dec336d26c23fc205eb52520ab485a4a`.**
The subject that carries every code finding is `tools/lexicon/lexicon.py`; one blocker sits across
`tools/lexicon/selftest.py` and `tools/lexicon/scaffold_lexicon.py`; the rest is prose carriers.

**Round: 1.** First review of this unit. Nothing here re-reports an entry from the
TOOL-aGradedDialect-1 rounds; every entry is a defect this diff introduced or a claim this diff
makes.

## Verdict: BLOCKED

One blocker, one high, four medium, four low. The blocker is not a reader defect: the kit's own
self-test suite is RED on the landed sha, one arm of 745, and the failing arm is one of the 38 this
diff added. It was never green on the shipped bytes, so the backlog row's "every one seen red under
a staged break" is contradicted by the leg log in this worktree's own git dir. The charter says a
KIT change owes `GATE_SELFTESTS=1` at its DoD; the default bar never runs this leg
(`chunk: selftests`), which is exactly how a red kit suite lands.

The high is the new `check_ts_returned` back-walk. Its stop set is wrong in both directions at
once: too narrow, so it crosses a semicolon-free statement boundary and takes an earlier `return`
as the value expression; too wide, so any `}` closing an object literal inside the return
expression ends the walk before `return` is reached. Both produce deterministic wrong verdicts on
ordinary React, and a `conv` violation has no waiver path.

Three of the seven claims the brief asked this review to attack are refuted by construction:
the definition population is NOT byte-identical with and without the marker, `(path, line)` keying
is NOT safe for `.tsx`, and not every new arm was seen red under a staged break. The other four
stand unattacked, which is stated as such below and is not the same as proven.

### Review shape

Raw 23, confirmed 23, refuted 0, unverified 0. Precision 1.00.

A precision of 1.00 on 23 raw findings is unusual and is explained by the surface: a hand-written
tokenizer extension plus a new selector, reviewed by four lenses that each had the base reader to
diff against. Every finding was a reproduction, not an inference, so the skeptics had nothing to
refute. It is also a warning: four lenses converged on the same six addresses from different
directions, so the raw count overstates the defect count by roughly two to one. The 23 confirmed
findings consolidate into the 10 entries below. Each folded entry names the raw ids it absorbs:

- Entry 1 absorbs raw ids 6, 12 and 17 — the one arm at `selftest.py:1021` and the one comment
  at `scaffold_lexicon.py:401`.
- Entry 2 absorbs raw ids 1, 8 and 9 — all the one back-walk loop at `lexicon.py:1858-1864`,
  two reporting the narrow stop set and one the wide one.
- Entry 3 absorbs raw ids 2 and 13 — the member arm at `lexicon.py:1826`.
- Entry 4 absorbs raw ids 3, 7, 14 and 19 — the mark key at `lexicon.py:2356` and its lookup at
  `lexicon.py:2386`.
- Entry 5 absorbs raw ids 5, 10 and 20 — the `calls` recording at `lexicon.py:1272-1276` and the
  catch-all at `lexicon.py:1301`, two spellings of one lexer-state gap.
- Entry 6 absorbs raw ids 4, 15 and 18 — the header claim at `lexicon.py:960-963`, one reporting
  the benign direction and one a silent shrink.
- Entry 9 absorbs raw ids 11 and 21 — the docstring at `lexicon.py:1435`.

The folding is a synthesis decision, not a pipeline discard. Nothing was dropped, and the severity
on each entry is this report's adjudication over the merged evidence, not the arithmetic mean of
what the raw entries carried. Two entries carry a severity above what any single raw finding
held, and each says why.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts
demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline.
Nothing was lost, so the zero counts here are evidence rather than a gap: the unverified set is
genuinely empty and every lens finding reached a skeptic. The finding set is COMPLETE for the
lenses that ran, which is a statement about the pipeline and not about the corpus — the 1257-file
adopter measurement was not available to this review, and every reader finding below was reached
by construction rather than by re-measurement.

## The findings, severity-ranked

### 1 — BLOCKER · the kit self-test is red on the landed sha, and the arm was never green

**Where.** `tools/lexicon/selftest.py:1021` (the assertion) and
`tools/lexicon/scaffold_lexicon.py:401` (the comment it trips over).

**What.** The new helpers-only scaffold arm asserts `"+returns:jsx" not in _txt` over the whole
emitted conf. The rewritten CELLS comment the scaffold emits above every `tsx.function` row is
unconditional, and its line 401 contains the literal `+returns:jsx` ("the `+returns:jsx` row
beneath it can"). So the substring is always present and the arm cannot pass.

**Reproduced.** `<git-dir>/gate-logs/lexicon_selftest.log` in this worktree, stamped 03:07 today,
ends `lexicon selftest FAILED — 1 of 745 arm(s)` and names exactly this arm: `scaffold: over a
.tsx tree where nothing returns an element, the camel parent is seeded and the +returns:jsx row is
NOT`. The captured tail shows the scaffold behaving correctly — `tsx.function   camel` with no
selector row — and the comment line above it. Both the arm and the comment landed in the same
commit and `400859c6` touched neither, so this arm has never been green on shipped bytes. The
backlog row's "38 arms, every one seen red under a staged break" is true of the break and false of
the green.

**Second symptom, same root.** On a helpers-only `.tsx` tree, or on any `tsx` extension read by a
probe set where `extract_jsx_defs` returns `{}`, the emitted comment tells the adopter a
`+returns:jsx` row sits beneath the parent when none was written. The comment was rewritten for
the pair; the conditional seed was not reflected in it — the amendment-leaves-its-other-half-
standing class.

**Fix.** Two lines, both owed. In `scaffold_lexicon.py` emit the selector sentence only when
`f"{_k}+returns:jsx"` is in `seeded_cells`; otherwise emit one line saying nothing in this tree
returns an element yet, so no `+returns:jsx` row is proposed and one may be added when the first
component lands. In the arm, assert on the ROW and not the substring:
`re.search(r"^  tsx\.function\+returns:jsx\b", _txt, re.M) is None`, the same anchored shape the
arm already uses for the camel row. Then run `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`,
record the green in the build record, and stage the break (seed the row unconditionally) to see
the arm red.

**Left-shift.** The class is "a new arm landed without a green observation". The
`lexicon selftest` leg is `chunk: selftests`, so no boundary runs it; the DoD for kit work owes
`GATE_SELFTESTS=1` and this diff did not record one. The gate that fits is not in the kit: it is
the build record carrying a `GATE_SELFTESTS=1` green sha as a required field for any commit that
touches a `subject: kit` leg's guard path, checked by the lander. Short of that, the compensating
check is the sentence in the kit descriptor already required by §7 — and it should now name this
incident.

### 2 — HIGH · `check_ts_returned`'s back-walk has the wrong boundary in both directions

**Where.** `tools/lexicon/lexicon.py:1858-1864`, the `for j in range(mk - 1, start, -1)` loop.

**What.** For a block body the walk from the marker back to the nearest `return` stops only on
`;`, `{` or `}`. That set is wrong two ways.

Too narrow: in semicolon-free source there is no `;` between statements, so the walk crosses a
statement boundary and takes an EARLIER statement's `return` as the value expression of a later
`const el = <A />` initializer. The sibling reader `read_ts_expr_end` already applies the ASI line
rule for arrow bodies (and R14 pins "the rule is the line and not the semicolon" for expression
bodies); the block-body path does not, so the two dialects of one file grade differently and the
semicolon-free one is wrong.

Too wide: the walk breaks on ANY `}`, including one that closes an object literal INSIDE the
return expression, so `return cond ? buildA({ x }) : <B />` finds the `}` of `{ x }` before it
finds `return` and is judged "not returned". The forward `held` walk at lines 1869-1880 balances
the same braces correctly, so the expression-body spelling of the identical expression is routed
and the block-body spelling is not.

**Reproduced.** On the head reader, `read_ts_jsx_defs`:

- `function useModal(open) {\n  if (!open) return null\n  const el = <Modal />\n  return
  createPortal(el, document.body)\n}` → `[('useModal', 1)]`; the byte-identical file with `;` →
  `[]`. `useModal` is a camel hook graded pascal in `+returns:jsx`.
- `if (!x) return\n  const el = <A />\n  mount(el)` routes the enclosing helper; `return\n<A />`
  (ASI `return;`) routes its function.
- `function BuildPage() {\n  return cond ? buildA({ x }) : <B />;\n}` → `[]`, and through
  `--check` with `tsx.function camel` + `+returns:jsx pascal` the engine prints
  `VIOLATION  BuildPage  satisfies pascal, not camel` in the parent cell, while
  `const BuildOther = () => cond ? buildA({ x }) : <B />;` in the same file is routed.

**Why HIGH and not the medium each raw finding carried.** Folded, this is one loop producing a
false RED on helpers (narrow side, every `semi: false` React tree) AND a false RED on components
(wide side, `return cond ? fn({...}) : <Fallback />` is an everyday shape). `WAIVER_FILES` holds
only `verb` and `suffix`, so a `conv` violation has no escape short of deleting the row, which
returns the adopter to the 951-of-3145 blind arming the selector exists to fix. The kit's own
round-2 review ruled semi-free source mainstream.

**Fix.** Rewrite the back-walk once, for both sides. Depth-track closers walking back: `)`, `]`
and `}` push, a matched opener pops; only an UNMATCHED `{` or a depth-0 `;` ends the walk, and an
unmatched `(` or `[` is the grouping enclosing the element and stays transparent (needed so
`return (\n<A/>\n)` and R4's `? (\n<A/>\n) : (` still resolve). At depth 0, apply the ASI line
rule `read_ts_expr_end` already uses: when `toks[j][2] < toks[j + 1][2]` and `toks[j][1]` is not
in `_TS_EXPR_CONTINUES`, stop with no `return` found. One lens verified this on a copy of the
reader: R3-R9 and R14 unchanged, `BuildPage` routes, `return { el: <div /> }` (R6) still does not,
both semicolon-free shapes correct. Pin with three arms: the semicolon-free `useModal`, the
bare `return\n<A />`, and the object-literal-in-ternary block body, each asserting the
semicolon and semicolon-free spellings agree.

**Left-shift.** The class is "block body and expression body grade one expression differently",
and it is gateable in the kit's own suite: an arm that takes every R-series expression-body fixture,
rewrites it as `{ return <expr>; }` and as the semicolon-free block, and asserts all three spellings
produce the same `read_ts_jsx_defs`. That is a property, not an instance, and it would have caught
both halves of this entry and entry 5.

### 3 — MEDIUM · a method body opens no scope, so its element leaks to the enclosing function

**Where.** `tools/lexicon/lexicon.py:1826-1834`, the `cur in ("object", "class")` arm.

**What.** Only `=>` and `function` call `add_scope` (lines 1753, 1767, 1771, 1798). The member
arms append to `funcs` but open no scope, so the innermost scope spanning an element inside a
method body is the enclosing DECLARED function's, and `check_ts_returned` then confirms it because
the method's own `return` sits directly before the marker. The arrow spelling of the same member
(`render: () => <td />`) IS absorbed, so two spellings of one member grade the enclosing function
differently. This contradicts the header's own OWNS clause ("the INNERMOST function spanning the
element, named or not") and README's "a member is never routed" — the member is not routed, but
its container is. R10 covers members at MODULE level only, where there is no enclosing scope to
leak into.

**Reproduced.** `function withLogger(Wrapped) {\n  return class extends React.Component {\n
render() { return <Wrapped {...this.props} />; }\n  };\n}` → `[('withLogger', 1)]`;
`function buildColumns() {\n  return { render() { return <td />; } };\n}` → `[('buildColumns',
1)]`; through `--check`, `export function useColumns() { const cols = { render(r) { return
<td>{r}</td>; } }; return cols; }` prints `VIOLATION  useColumns  satisfies camel, not pascal`.
A getter (`get el() { return <div/>; }`) leaks the same way. A HOC returning a class component and
a factory returning an object with a `render` method are both real React shapes.

**Fix.** One line beside the method append at 1827: after `funcs.append((text, ln))` in the
`nt == "("` case, `add_scope(read_ts_body_start(toks, k + 1), -1)`, so a method body absorbs like
a nameless `function` does. Getters, setters and `constructor` pass through the same arm and are
covered by the same line. Pin with an arm for the HOC-returns-class shape and the object-method
shape inside a declared function, asserting the enclosing name is NOT routed while
`render: () => ...` stays as is.

**Left-shift.** Same property arm as entry 2's: every member spelling (`m() {}`, `m: () =>`,
`m = () =>`, `get m()`) inside a declared function, asserting the container is never routed.

### 4 — MEDIUM · `jsx` marks are keyed on `(path, line)`, and TypeScript puts two definitions on one line

**Where.** `tools/lexicon/lexicon.py:2356` (`out.setdefault((rel, lineno), set()).add("jsx")`)
and `lexicon.py:2386` (`marks.get((path, line), ())`).

**What.** `extract_jsx_defs` iterates `for _name, lineno in read_ts_jsx_defs(src)`, has the
disambiguating name in hand, and discards it. `scan_routes` then matches any `(path, line, name)`
whose `(path, line)` carries the literal, so every declared function on that source line is routed.
`extract_decorators` survives the same key only because Python cannot put two `def`s on one line;
the brief's claim that `(path, line)` keying is safe for the routed populations was carried over
from that population without re-measuring it on TS one-liners.

**Reproduced.** `function useThing() { const Row = () => <tr />; return Row; }` on ONE line — the
header's own R7 example, collapsed — gives funcs `[('useThing', 1), ('Row', 1)]`, owned `{1}`,
`read_ts_jsx_defs` correctly `[('Row', 1)]`, and `scan_routes` routes BOTH; through `--check`,
`VIOLATION  useThing  satisfies camel, not pascal`. `export const Card = () => <div/>; export
const buildX = () => 1;` prints `tsx.function.conv 0 of 0 … population 0 of 2`,
`tsx.function+returns:jsx.conv 1 of 2` and `VIOLATION  buildX  satisfies camel, not pascal`.

**The green-by-absence half.** In the second repro the parent emptied to `0 of 0` with no DEAD
CELL, because routed (2) equals the denominator (2) and the new third exemption reads that as a
complete partition. So the keying bug also passes a parent that is empty because of the bug, not
because the declaration partitioned it. The brief's claim that the exemption "cannot exempt a
genuinely dead cell" holds for a genuinely dead cell and does not hold for one emptied by a
collision upstream.

**Why MEDIUM.** Prettier splits these onto separate lines, so reach needs unformatted or
hand-collapsed `.tsx`; but the false RED is deterministic, undeclared (no README or arm documents
a same-line ceiling), and has no waiver.

**Fix.** Key both additive accessors on the definition site INCLUDING the name:
`out.setdefault((rel, lineno, name), set())` in `extract_jsx_defs` and `(rel, node.lineno,
node.name)` in `extract_decorators`, and read `marks.get((path, line, name), ())` at 2386. One key
shape, no lookup fallback. Add an arm with two declared functions on one line, one returning an
element, asserting only the owner is routed and the parent still holds the other.

**Left-shift.** A structural assertion in `scan_routes` itself: the routed set must be a subset of
the names the accessor returned for that path. It is one set comparison at the seam and would
have red on the first collision regardless of which future accessor reintroduces the shape.

### 5 — MEDIUM · a typed call and an optional call are recorded as groupings, not calls

**Where.** `tools/lexicon/lexicon.py:1272-1276` (the `(` recording and the `>` fallthrough) and
`lexicon.py:1300-1301` (the catch-all that clears `expr_end` on `?` and `.`).

**What.** `calls` records a `(` only when `expr_end` is True. The op arm sets
`expr_end = c in ")]"` after every op, so `>` clears it, and `?` and `.` each fall to the catch-all
that clears it too. So the `(` of `mount<P>(<Host />)` and of `render?.(<Form />)` is absent from
`calls`, `check_ts_returned` does `held.append(j in calls)` → False, treats it as a transparent
grouping, and reports the element under it as returned. The plain `mount(<Host />)` records the
call correctly. R5 pins only the bare-call shape; R13 pins `foo(`, `)(` and `.b(` but not `>(` or
`?.(`, so nothing documents the ceiling.

**Reproduced.** `const buildWrapper = () => shallow<Props>(<Comp />);` → `[('buildWrapper', 1)]`;
`function renderX() {\n  return props.render?.(<A />)\n}` → `[('renderX', 1)]`; through
`--check`, `export function loadHost(x) { return mount<P>(<Card x={x} />); }` prints
`VIOLATION  loadHost  satisfies camel, not pascal`, while `return mount(<Card x={x} />)` stays in
the parent.

**Why MEDIUM.** Three lenses reached it from two spellings; the typed form is enzyme's and
RTL's documented signature for typed helpers, so a test-utils file is the natural victim, and
there is no waiver.

**Fix.** Cheapest is in the lexer: at the `<` op remember whether `expr_end` was True, and at the
`>` that `read_ts_angle_end` pairs with it restore that state rather than clearing it, so a
generic call's `(` is recorded; and in the catch-all keep `expr_end` when `c == "."` and
`src[i-1] == "?"` (optional chaining), so `?.(` records too. Pin both spellings in R5.

**Left-shift.** Entry 2's property arm covers the routing half. For the lexer half, an arm that
asserts `calls` over a fixture holding every call spelling TS has — `f(`, `f<T>(`, `f?.(`, `a.b(`,
`a?.b(`, `)(`, `](` — so the next spelling added to the language is added to the fixture, not
discovered by an adopter.

### 6 — MEDIUM · "the definition population is byte-identical with and without the marker" is false by construction

**Where.** `tools/lexicon/lexicon.py:960-963` (the `scan_ts_tokens` header), repeated at
`memory/backlog/TOOL.md:235` ("byte-identical on all 1257 adopter files") and in the uncommitted
working-copy edit to `memory/map/features/lexicon.md` ("invisible to every definition arm by
construction").

**What.** No arm matches the marker — that half is true. But the marker DISPLACES the token that
used to follow an element. In 1.3 an element emitted nothing, so `check_ts_arrow(toks, j + 1)`
after `=` (line 1796) read the NEXT STATEMENT's head, and `read_ts_block_kind(toks[k - 1])` (line
1735) read the token before the element; in 1.4 both read the marker. The population moves in
both directions.

**Reproduced**, base reader loaded beside the landed one in one process:

- `const icon = <Icon />\nfunction App() { return icon }` → base `[('icon', 1), ('App', 2)]`,
  head `[('App', 2)]`. Base read the next statement's `function` as `icon`'s initializer; head is
  right. Same for a following `async function` and a following `(x) => x`.
- `function f() { return <A/> || { render: () => 1 }; }` → base `[('f', 1), ('render', 1)]`,
  head `[('f', 1)]`. `read_ts_block_kind` now sees `pk == 'jsx'` instead of `return`, classifies
  the brace `statement` instead of `object`, and the member arm never fires. A definition is
  LOST, not gained — a silent shrink.
- `const x = <A/> ?? { render: () => 1 };` → base `[('render', 1)]`, head `[]`. Same shrink.

The R12 arm cannot see any of this: its fixture uses `;` terminators and compares element-vs-`null`
under the NEW lexer only, and substituting `null` for the element moves the prev-token too, so
both sides classify the same way. The 1257-file measurement is evidence about that corpus, which
lacked the shape, not about the construction.

**Why MEDIUM.** The first direction removes a 1.3 false positive, which is benign in itself —
except that pins are "an equality in both directions" (line 3084), so an adopter with
semicolon-free `.tsx` reds on the 1.3 → 1.4 upgrade with a pin message naming a cell nobody
touched. The second direction is a regression on a rare shape. And a false invariant in a gate's
own header is the class §7 names: a reader trusts "measured, not argued" and stops looking.

**Fix.** Three parts. (a) At line 1735 look back past marker tokens when picking the brace's
prev-token: `p = k - 1; while p >= 0 and toks[p][0] == "jsx": p -= 1`, then
`read_ts_block_kind(toks[p] if p >= 0 else None, cur, pend)` — restores the old classification
byte for byte. Do NOT re-hide the marker from `check_ts_arrow`; that would restore the 1.3 false
positive. (b) Rewrite the header and both prose carriers to what is true: no arm matches the
marker, but an arm that reads the token after `=` now sees it instead of the next statement's
head, which drops a 1.3 false positive in ASI-style source; note it beside the kit version bump so
the pin move is declared rather than discovered. (c) Pin both shapes with arms asserting the HEAD
population — `const el = <A />\nfunction f() {}` yields only `f`, and `return <A/> || { render:
() => 1 }` yields `render` — so a future move back is a red.

**Left-shift.** The arm meant to prove the invariant compared the wrong pair. The gate is an
old-vs-new comparison, not element-vs-null: a fixture of every ASI shape run through
`parse_ts_defs` with `jsx=False` and `jsx=True` under the SAME reader, asserting equality. That is
what "byte-identical with and without it" actually means, and it is one boolean away from R12.

### 7 — LOW · the DEAD CELL parent exemption compares against a denominator that is wider than the partitioned population

**Where.** `tools/lexicon/lexicon.py:2941-2944`, and the comment at 2938 asserting the
denominator IS the (ext, surface) population.

**What.** For the `constant` surface, `scan_module_constants` (line 2235) returns every bound
target as the denominator by its own docstring, while the graded population is public simple
names only, so a complete partition of `py.constant` never sums to it and the exemption never
fires there. The same shape on `py.function`, where denominator equals population, is exempt.
The exemption's reach depends on which surface's rule happened to narrow.

**Reproduced.** `core/a.py` = `CFG_A = 1 / CFG_B = 2 / _private = 3` with `py.constant
screaming` + `py.constant+prefix:CFG screaming` prints `py.constant.conv 0 of 0 … population 0 of
3`, `py.constant+prefix:CFG.conv 0 of 2 … population 2 of 3`, then `DEAD CELL — py.constant …
selected NOTHING` and exits 1 on a partition that is complete.

**Fix.** Compare against the partitioned population, not the denominator: carry
`"extracted": len(_all_names)` on each row in `measure_conventions` (it already has `_all_names`
from `pops`) and test `routed == row["extracted"]`. Correct the comment. Add an arm over a fully
routed `py.constant` parent.

**Left-shift.** An arm per surface, not one arm: for every surface the kit reads, a complete
partition is exempt. That is a loop over `SURFACES` in the selftest and it pins the exemption's
reach to the population the engine actually grades.

### 8 — LOW · the measured figure `86` is typed in five carriers, and this diff already had to correct it once

**Where.** `tools/lexicon/lexicon.py:1680`, `tools/lexicon/README.md:100`,
`tools/lexicon/selftest.py:2602`, `memory/backlog/TOOL.md:235`; `951 of 3145` additionally at
`tools/lexicon/LEXICON.md:119`, undated.

**What.** In `3281fcea` `lexicon.py` said "this pins 88" while `README.md` already said "pins 86",
and `400859c6` had to correct it across carriers — the two-answers-to-one-question class biting
inside the same diff. What makes it a defect rather than a sanctioned dated snapshot: README.md
97-99 and LEXICON.md 122-123 both NAME `parse_ts_source`'s header as the owner of the measurement
and then restate the number beside the pointer, which is the charter's "point at the source, or
gate the pair" broken in the shape it describes. The selftest comment and LEXICON.md carry no date.

**Fix.** Deletion, not a gate: keep the dated measurement in the `parse_ts_source` header, point
the README, LEXICON.md and the selftest comment at it, and let the backlog row keep its own dated
copy as the frozen narrative record.

**Left-shift.** None that fits; a number in prose is a documented check. Add it to the kit
descriptor's compensating-check sentence.

### 9 — LOW · `read_ts_body_start`'s docstring names a selector that does not exist

**Where.** `tools/lexicon/lexicon.py:1435`: "the index is what the `body:jsx` selector needs".

**What.** `SELECTOR_KINDS = ("prefix", "decorator", "returns")` at `lexicon_conf.py:72`, and
`parse_cell_key` refuses any other kind; `body:jsx` occurs nowhere else in the tree. The one prose
pointer to this reader's consumer names a selector the grammar refuses, so a reader grepping it
finds nothing and a row typed from it reds at the row.

**Fix.** Replace `body:jsx` with `returns:jsx`.

**Left-shift.** The `lexicon naming predicates` leg already greps the kit for its own vocabulary;
adding a predicate that every backticked `<word>:jsx` in kit prose names a kind in `SELECTOR_KINDS`
is one line there.

### 10 — LOW · the dogfood declaration's PINS comment still enumerates two selector kinds

**Where.** `.lexicon.conf:327` at HEAD: "`kind` is `prefix` or `decorator`; a decorator selector
on a non-`parser` language is a refusal".

**What.** The diff amended the same enumeration in both charter copies (dropped "by prefix or
decorator selector" for a pointer) and in the README (added `returns` plus its refusal clause),
and left this carrier standing. `git diff 75b85708 HEAD -- .lexicon.conf` is empty. A session
copying the conf's comment as the grammar would believe `returns` is a typo.

**Caveat for the fixer.** The working tree already carries an UNCOMMITTED edit to exactly these
lines (`git status` shows ` M .lexicon.conf`), and the new text points at `SELECTOR_KINDS` instead
of enumerating. This is in flight — commit it, do not redo it. A second stale-looking carrier at
`.lexicon.conf:369` sits inside the TOOL-aSurfacedLexicon-23 narrative, is historical prose, and is
still true in substance (no kind is path-scoped); leave it.

**Fix.** Commit the pending edit.

**Left-shift.** The same predicate as entry 9's, pointed at `.lexicon.conf` comments as well as
kit prose.

## The seven claims, one by one

The brief named seven claims to attack. Their status after this round, so the next round knows
which are settled and which merely went unchallenged:

1. **Definition population byte-identical with and without the marker.** REFUTED by construction
   (entry 6): three shapes move, one of them a silent shrink. The measurement stands for the
   corpus it was taken on and for nothing else.
2. **Every new arm was seen red under a staged break.** CONTRADICTED for one arm (entry 1): it was
   seen red, and it was never seen green. The other 37 were not re-staged by this review.
3. **The DEAD CELL exemption cannot exempt a genuinely dead cell.** HOLDS for a genuinely dead
   cell. It does NOT hold for a parent emptied by the keying collision in entry 4, which it reads
   as a complete partition; and it fails in the other direction on `constant` (entry 7).
4. **The conf refusals fire at the row.** No lens found a counter-example. Unattacked, not proven.
5. **The scaffold never proposes a row the first `--check` reds on.** No lens found a row that
   reds. The scaffold's COMMENT does promise a row it did not write (entry 1, second symptom).
6. **`scan_routes`'s parameter rename broke no caller.** Verified: one caller, `lexicon.py:2494`,
   passes the merged `marks` dict. Holds.
7. **`(path, line)` keying is safe for the populations routed.** REFUTED for `.tsx` (entry 4);
   holds for Python by grammar, not by design.

## Landing recommendation

Do not land. Entry 1 alone is a red kit suite on the landed sha, and the charter's DoD for kit work
is a recorded `GATE_SELFTESTS=1` green, which does not exist for this range. Entries 2-6 are one
remediation commit: five addresses in `lexicon.py`, each fix a few lines, each with an arm named
above. Entry 6's prose rewrite and the map dossier edit already pending in the working tree should
ride the same commit, together with entry 10's pending `.lexicon.conf` edit, so the kit version
bump, the header, the backlog row and the dossier say one thing.

Round 2 should re-run every repro in this record against the remediation AND against the base
reader, because entry 6 shows the corpus-measured invariant is not a construction invariant, and a
fix at line 1735 that looks back past markers is exactly the kind of change whose own displacement
effects nobody measured. The property arms suggested under entries 2 and 6 are the cheapest way to
make that true for every round after.
