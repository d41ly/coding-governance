**Serves:** diff-review TOOL-aGradedDialect-4

# aGradedDialect — Tier-2 diff review of the `returns:jsx` selector, round 2

*Node `a`, 2026-09-11, branch `branch/lexicon-kit-typescript-34c322`. Fold review of the round-1
fixes: four primed lens passes over the remediation commit, four skeptic batches prompted to
REFUTE, one synthesis. Every code finding below was re-executed at source in this worktree before
it was written here, through `read_ts_jsx_defs` and, for the high, through `--check` on a throwaway
repo so the merge-bar symptom is the one quoted. The proposed fix for the high was applied to a
scratch copy of the kit and re-measured against the same case table; the kit self-test was run
against that copy too, and its verdict is stated where it is used.*

**Reviewed range: `400859c6dec336d26c23fc205eb52520ab485a4a...7b54230e00cd74e014f8787fb0fcc28763b62bb5`.**
One commit, `7b54230e`, the fold of round 1's ten entries. The subject that carries every code
finding is `tools/lexicon/lexicon.py`; the rest sits in `tools/lexicon/selftest.py`,
`tools/lexicon/scaffold_lexicon.py` and the prose carriers.

**Round: 2.** Every entry here is either a round-1 entry this commit closed for one spelling and
left open for the others, or a claim the fold makes about itself. Nothing re-reports a round-1
entry that these bytes actually closed; those are listed as closed in the section after the
findings, with the repro that shows it.

## Verdict: BLOCKED

No blocker, one high, seven low. Round 1's blocker is closed: the kit suite ran green on 755 arms
at 04:09 today, six minutes after `7b54230e` landed at 04:03, and the log in this worktree's git
dir names the once-red scaffold arm passing. That is the recorded `GATE_SELFTESTS=1` green the
charter's kit DoD owes, and it exists for this range.

The verdict is BLOCKED on the high alone, and the reason is not its severity in isolation but
what the unit claims about it. Round 1's HIGH was the back-walk crossing a semicolon-free
statement boundary; the backlog row, the header and R15 all say it is closed. It is closed when
the earlier statement ends in a bare word. It is open when that statement ends in `)`, `]` or `}`,
which in semicolon-free JavaScript is the commonest way a line ends: the closer branch of the
backward walk `continue`s before the ASI test is reached, so `if (!open) return noop()` on one line
and `const el = <Modal />` on the next still routes the hook, and `--check` prints `VIOLATION
useModal  satisfies camel, not pascal`. The scaffold seeds the `+returns:jsx` row for any adopter
whose tree returns an element, so a semicolon-free adopter's first `--check` reds on a correct
name with no waiver path — the round-1 claim "the scaffold never proposes a row the first
`--check` reds on" is now false for that dialect. The fix is a three-line move, verified below
with zero movement on every prettier shape and every R-series fixture, and it lands with one new
R15 spelling. Until that is in and observed red-then-green, the row that says round 1's HIGH is
folded is not true, and a record that is not true is the one thing this repo's memory tree exists
to refuse.

The seven lows are residuals of the same shape, each real, none blocking: two more spellings the
backward and member fixes miss, two arms whose comments claim more than their fixtures exercise,
the corpus figures still in two carriers inside the kit, a scaffold comment restating a seed
literal, and two annotations the key change left behind.

### Review shape

Raw 16, confirmed 14, refuted 2, unverified 0. Precision 0.88.

The two refuted findings, raw ids 5 and 9, did not reach this synthesis; nothing is said about
them here beyond the count. The 14 confirmed findings consolidate into the eight entries below.
Each folded entry names the raw ids it absorbs:

- Entry 1 absorbs raw ids 1, 6 and 12 — three lenses, one loop at `lexicon.py:1903`, one repro.
- Entry 2 absorbs raw ids 3 and 11 — the member arm at `lexicon.py:1852`.
- Entry 3 absorbs raw ids 4 and 7 — the R21 comment at `selftest.py:2758`.
- Entry 4 absorbs raw ids 8, 10 and 15 — the corpus figures at `selftest.py:2606` and `:2665`.
- Entries 5 to 8 are raw ids 2, 13, 14 and 16, one each.

Severity on each entry is this report's adjudication over the merged evidence. Raw id 10 arrived
as medium and its skeptic re-graded it low with a reason this report accepts; it is folded at low.
Raw id 2's finding stands and its proposed FIX does not — the skeptic showed the one-token change
loses a live shape, and this report re-executed that and carries the skeptic's fix instead.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED. 0 contradictory verdicts
demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline.
Nothing was lost, so the zero counts here are evidence rather than a gap: the unverified set is
genuinely empty and every lens finding reached a skeptic. The finding set is COMPLETE for the
lenses that ran. That is a statement about the pipeline and not about the corpus: the 1257-file
adopter measurement is a semicolon corpus and cannot see entry 1, and no lens re-measured it.

## The findings, severity-ranked

### 1 — HIGH · the backward ASI rule never runs on a closer, so round 1's boundary half is closed for word-ended statements only

**Where.** `tools/lexicon/lexicon.py:1903-1905`, the `)`/`]`/`}` branch of the backward walk in
`check_ts_returned`; the ASI test it pre-empts is at `:1922-1924`.

**What.** The loop body handles a closer first: `depth += 1; continue`. The line-break test that
implements "a line break after a token that cannot continue an expression is a statement boundary"
sits nineteen lines later and is reached only for tokens that are not closers and not at depth.
So when the earlier statement's last token is `)`, `]` or `}` — a call, an index, an object or
array literal, a parenthesised value — the walk steps INTO that statement, finds its `return`,
and reports the element after it as the value of the function. The docstring's own rule
(`:1883-1884`) is contradicted by the control flow beneath it. R15 (`selftest.py:2716`) pins only
`return null`, a word-ended statement, which is the one spelling the rule handles.

**Reproduced.** At `7b54230e`, `read_ts_jsx_defs`:

- `function useModal(open) {\n  if (!open) return noop()\n  const el = <Modal />\n  return
  createPortal(el, document.body)\n}` → `[('useModal', 1)]`. The `return null` twin → `[]`. The
  `;` twin → `[]`.
- `return []` → `useColumns` routed; `return {}` → `useThing` routed; a multi-line
  `return {\n    a: 1,\n  }` → routed; the assignment spelling `el = <Modal />` → routed; the
  block-body arrow `const useX = (o) => { … }` → routed; `return (x)`, `return f<T>()` and
  `return props.children()` → routed (lens repros, mechanism identical).
- Through `--check` on a throwaway repo with `tsx.function camel` + `tsx.function+returns:jsx
  pascal`, the `useModal` file beside a `Page` component prints `tsx.function.conv 0 of 0`,
  `tsx.function+returns:jsx.conv 1 of 2` and `src/a.tsx:1: VIOLATION  useModal  satisfies camel,
  not pascal`. The parent emptied to `0 of 0` without a `DEAD CELL`, because the routed count is
  positive — the exemption reads a parent emptied by a false route as a complete partition, the
  same shape round 1 entry 4 named for the keying collision.

**Why HIGH.** It is round 1's HIGH, narrow half, re-opened for the commonest line ending in the
dialect the kit's own round-2 review ruled mainstream. A `conv` violation has no waiver
(`WAIVER_FILES` holds `verb` and `suffix`), the scaffold seeds the row, and the pin is an equality
in both directions, so the adopter reds on a correct name and the row's message names a cell they
did not touch. Three lenses reached it independently from three fixtures.

**Fix.** Move the ASI test ahead of the bracket bookkeeping and guard it on depth, as the first
statement of the loop body after the unpack:

```python
if depth == 0 and toks[j][2] < toks[j + 1][2] and text not in _TS_EXPR_CONTINUES \
        and toks[j + 1][0] != "jsx" and toks[j + 1][1] not in (":", ",", "="):
    break
```

then the closer and opener branches unchanged, and delete the later copy at `:1922-1924`.
Closers are already outside `_TS_EXPR_CONTINUES`, so a closer at line end at depth 0 now breaks
before it is pushed. Verified on a scratch copy of the kit at `7b54230e`: the six closer-ended
shapes above read `[]`; the ten must-route shapes — `return (`, `cond ? (…) : (…)`, `open && (…)`,
the bare multi-line ternary, `isReady()` newline `? <A />`, an object literal before `: <B />`,
`cond ? build({ x }) : <B />`, `a >` newline `b ? <B /> : null`, a statement before `return
<div>{x}</div>`, a `useEffect(…)` line before `return <div />` — read identically to HEAD. Through
`--check` the same file prints `tsx.function.conv 0 of 1` and `+returns:jsx.conv 0 of 1` with no
violation. Then pin the CLASS in R15: add `if (!open) return noop()`, `return []` and `return {}`
early-return fixtures asserting no routing, and stage the break (re-order the two branches) to see
the arm red before it is committed.

**Left-shift.** R21 is the property arm round 1 asked for and it cannot see this — every R21
fixture body is one statement (entry 3). The gate that fits is one prefix statement in R21's block
spellings: rewrite each expression as `{ if (!x) return noop()\n  return <expr> }` as a FOURTH
spelling and assert it agrees with the other three. That puts the boundary half inside the
property, so the next stop-set edit that crosses a boundary reds fourteen times instead of never.

### 2 — LOW · the method scope opens only in the `_TS_NAME (` arm, so three method spellings still leak

**Where.** `tools/lexicon/lexicon.py:1852-1857`, the `cur in ("object", "class")` arm.

**What.** Round 1 entry 3's fix opens an owner `-1` scope on a method body, and it does so inside
the arm that requires `_TS_NAME` followed by `(`. A method whose name is followed by a
type-parameter list (`render<T>(x: T) {`), a computed key (`[k]() {`) or a string key
(`'render'() {`) never reaches `add_scope`, so its element is owned by the enclosing declared
function and confirmed by the method's own `return`. The header's "every METHOD body opens such a
scope" overstates by exactly these three. `async render(`, `get el(`, `static` and `#priv` do
absorb, because their name token is still `_TS_NAME` + `(`.

**Reproduced.** At `7b54230e`: `function buildCols() {\n  return { render<T>(x: T) { return <td
/>; } };\n}` → `[('buildCols', 1)]`; `{ [k]() {…} }` and `{ 'render'() {…} }` → `buildCols`
routed; `{ render() {…} }` → `[]` (the R16 shape). A HOC returning `class extends
React.Component { renderItem<T>(i: T) { return <li />; } }` routes `withX` while the plain-method
twin does not.

**Why LOW.** Same false-route class as entry 1 on shapes React source rarely writes; the population
arm never graded these members either, so it is a residual of the confirmed class, not a new one.

**Fix.** Open the scope on the syntactic BODY rather than on the population arm: in the
`cur in ("object", "class")` branch, whenever a `(` — or a balanced angle run via
`read_ts_angle_end` then `(` — is followed by a body per `read_ts_body_start`, call
`add_scope(…, -1)` regardless of whether the key was a `_TS_NAME` word. Add the three spellings to
R16, each asserting the container is not routed.

**Left-shift.** R16 as a loop over every member key spelling TS has — word, `<T>`, `[k]`,
string, number — inside a declared function, asserting the container is never routed. One list,
five iterations, and the next key spelling is added to the list rather than found by an adopter.

### 3 — LOW · R21's comment claims both halves of round 1's HIGH, and its fixtures can red on one

**Where.** `tools/lexicon/selftest.py:2758-2761`, the R21 header comment ("Both halves of round
1's HIGH were one spelling grading differently from its siblings, and this is the class").

**What.** Every R21 fixture body holds exactly one statement, so there is no earlier `return` for
the walk to cross into and the boundary half cannot red there. Two lenses measured it two ways.
Against the pre-round-1 reader at `400859c6`, exactly two of the fourteen expressions split:
`cond ? build({ x }) : <B />` (the `}`-stop half) and the bare multi-line ternary (the old forward
ceiling); every other expression, the semicolon-free block spelling included, gave an identical
triple. With the backward ASI rule and the `toks[r][2] > toks[r - 1][2]` check deleted from HEAD,
R21 reports zero disagreements while R15 reds — through its `return null` fixtures alone. So the
only arm holding the boundary half is R15, and R15 holds the one spelling entry 1 shows the rule
handles.

**Why LOW.** A coverage-and-comment defect, but a concrete one under §7's rule that a skip must
announce itself: a reader trusting the comment would drop R15 as redundant, and R15 is the only
guard for the half that is still open.

**Fix.** Either reword the comment to name what it pins — the balanced-group half and the ceiling
— and point at R15 for the boundary half; or, better, take entry 1's left-shift and add the
prefix-statement spelling, after which the comment becomes true.

**Left-shift.** Entry 1's fourth spelling. A property arm's comment should list the halves its
fixtures were seen to red on, and this one was written before the staging that would have shown
one of them never does.

### 4 — LOW · the corpus figures do not live in one carrier, and the comment that says they do types two of them

**Where.** `tools/lexicon/selftest.py:2606-2608` (`951 offenders of 3145`, then "the dated
figures live in `parse_ts_source`'s header alone") and `:2665-2666` (`121`, twice);
`tools/lexicon/lexicon.py:1674-1682` owns the same three figures with the date. Also
`tools/lexicon/LEXICON.md:120` ("and nowhere else"), `tools/lexicon/README.md:101` ("in ONE
place"), and `memory/builds/aGradedDialect/README.md:69` (951/3145, untouched by this range).

**What.** Round 1 entry 8 was the figure CLASS, not the literal `86`. The fold removed
254/162/86 from the selftest comment and inserted the "header alone" sentence into the same
sentence that still restates `951 of 3145`; the R10 comment two screens down still types `121`
twice. `86` is now in the header alone within the kit, so that half is closed. The next
re-measurement updates the header and leaves three undated copies behind with prose beside them
promising there are none — the rot round 1 raised the entry to close, in the file that states the
rule. The backlog row `memory/backlog/TOOL.md:235` carries all five figures beside "now one,
dated"; round 1's fix text sanctioned the row as the frozen narrative copy, so the figures there
are not a defect, but that clause of the row is inaccurate as written.

**Why LOW.** Prose only; nothing grades on it. Raw id 10 arrived as medium and its skeptic
re-graded it, correctly, because the `86` half IS closed and the residue is three numerals in two
comments.

**Fix.** Deletion. In the selftest comment: "read what that spec predicted — the dated figures
live in `parse_ts_source`'s header"; in R10: "the adopter corpus holds render slots spelled by the
API that reads them; the header counts them". Change the backlog row's clause to "now one code
carrier plus this dated record". Leave LEXICON.md and README.md pointing at the header; drop the
"nowhere else" absolute or leave it, since after the deletion it is true within the kit.

**Left-shift.** None that fits; a number in prose is a documented check, as round 1 said. The
kit descriptor's compensating-check sentence should name the header as the one carrier so the
next re-measurement has a checklist line to hit.

### 5 — LOW · the backward walk inherits `>` as a continuation, so a generic close at line end crosses the boundary

**Where.** `tools/lexicon/lexicon.py:1922-1923`, the backward ASI test, reading
`_TS_EXPR_CONTINUES` (`:1524`), which holds `>`.

**What.** `>` is in the shared continuation set for the forward rule's sake. Backward, a `>` that
closes a generic in an early return — `return v as Foo<Bar>`, `return x satisfies Foo<T>` — is
the last token of a statement, and the test treats it as a continuation, so the walk crosses into
that statement's `return`. Only reachable once entry 1 is fixed for the general case, since today
the closer branch crosses first anyway; stated here so the fix for entry 1 is not read as closing
this one.

**Reproduced.** At `7b54230e`: `function useX(v) {\n  if (!v) return v as Foo<Bar>\n  el = <A
/>\n  return el\n}` → `[('useX', 1)]`; the `;` spelling → `[]`. Still routed on the scratch copy
carrying entry 1's fix, as expected.

**The finder's fix is wrong, and the skeptic's is carried.** The finder proposed
`(text == ">" or text not in _TS_EXPR_CONTINUES)` on the grounds that `>` buys the backward walk
nothing. It does: `function Cmp(a, b) {\n  return a >\n    b ? <B /> : null\n}` is routed at HEAD
and on entry 1's scratch fix, and this report applied the finder's change on top of that fix and
watched it drop to `[]`. So the fix must distinguish a balanced angle run after a word — walk back
from the `>` with `read_ts_angle_end`'s pairing and see a `_TS_NAME` before the matching `<` —
from a comparison, and break only on the former.

**Why LOW.** Semicolon-free TypeScript with a generic-close-ended early return before an element
initializer; rare, and a residual of entry 1's class.

**Left-shift.** Entry 1's R15 extension gains the `as Foo<Bar>` spelling once this lands, and the
`a >` newline `b ? <B />` shape goes into R21's expression list so the comparison reading is
pinned against exactly the change the finder proposed.

### 6 — LOW · R18's "nested block" clause is fixture-passes-by-finding-nothing

**Where.** `tools/lexicon/selftest.py:2746-2751`, the `C` half of R18 ("an object literal or a
nested block does not hide the `return`").

**What.** `C`'s block `{ a; b; }` sits in the statement BEFORE the `return`. The backward walk
from `<D />` meets `?`, `)`, `(`, `f`, then `return`, and breaks; the block is never visited. The
half passes identically on the base reader at `400859c6` (both readers route `C`), so it
distinguishes nothing about the round-1 fix. What a block uniquely brings that an object literal
does not — a `;` at depth above zero hitting the `if depth: continue` skip at `:1914` — is pinned
by no fixture: `return f(() => { a; b; }) ? <D /> : null` routes on HEAD and not on base, and
nothing in the suite exercises it. The `A` half does cover the depth arithmetic, since a literal
and a block share the `{`/`}` path.

**Fix.** Put the block between `return` and the element — `return f(() => { a; b; }) ? <D /> :
null` — or rename the arm to claim only what `A` exercises.

**Left-shift.** The base reader is importable beside the landed one, as round 1 did in one process;
an arm whose comment says "this used to fail" should be seen to fail on the base before it is
worded so. That is a review-time check, not a gate, and it is the same one entry 3 needed.

### 7 — LOW · the helpers-only scaffold comment types the seed row as a literal beside the code that derives it

**Where.** `tools/lexicon/scaffold_lexicon.py:414` (the emitted comment "so no
`tsx.function+returns:jsx  pascal` row is proposed beneath"), and `tools/lexicon/selftest.py:1026`,
which asserts that literal string.

**What.** `:376-378` derives the seeded row from `SEED_SELECTORS` (`_sel[0]`, `_sel[1]`); the
comment two lines below it, emitted into the adopter's conf, retypes both halves. S4
(`selftest.py:743`) pins `SEED_SELECTORS[("tsx", "function")] == ("returns:jsx", "pascal")`, so a
change to the row DOES red — at S4. After S4 is updated, `:414` and `:1026` keep agreeing with
each other and the emitted advice names a convention the scaffold would no longer seed, with a
green bar. The charter's prose-beside-owning-source class, applied to a product artifact.

**Fix.** Render it: `f"  # so no `{_e}.{_surface}+{_sel[0]}  {_sel[1]}` row is proposed
beneath"`, and have the scaffold arm build its expectation from `scaffold_lexicon.SEED_SELECTORS`
the same way.

**Left-shift.** S4 is already the gate for the row; the fix makes the comment derive from the
same source, after which there is nothing left to gate.

### 8 — LOW · both accessors still annotate the two-tuple key the fold retired

**Where.** `tools/lexicon/lexicon.py:2389` (`extract_decorators`) and `:2424` (`extract_jsx_defs`):
`out: dict[tuple[str, int], set] = {}`.

**What.** The code keys on `(rel, node.lineno, node.name)` at `:2406` and `(rel, lineno, name)` at
`:2432`, the `extract_jsx_defs` docstring at `:2411` states the three-tuple, and `scan_routes`
reads `marks.get((path, line, name), ())` at `:2462`. The base at `400859c6` had the two-tuple key
with a matching annotation; the fold grew the key and left the annotation. No mypy or pyright leg
exists in `tools/gate-legs.json`, so nothing on the bar sees it. No runtime effect.

**Fix.** `out: dict[tuple[str, int, str], set] = {}` in both.

**Left-shift.** A type-check leg over the kit would have caught it at the fold; that is a
project-level decision the kit does not get to make, and it is noted rather than proposed.

## Round 1's ten entries, one by one

The brief asked whether every round-1 entry is closed by these bytes and not merely re-worded.
Each was re-executed at `7b54230e`:

1. **Blocker, the red scaffold arm.** CLOSED. The arm at `selftest.py:1026` asserts on the anchored
   ROW, the scaffold's helpers-only branch at `scaffold_lexicon.py:411-416` emits the other
   comment, and the suite log in this worktree's git dir reads `lexicon selftest OK — 755 arm(s)`
   at 04:09, after the commit. The residual is entry 7 here, a comment literal.
2. **High, the back-walk boundary.** HALF CLOSED. The wide half is closed: `return cond ?
   buildA({ x }) : <B />` in a block body routes `BuildPage`, and R18/R21 pin it. The narrow half
   is closed for word-ended statements and open for closer-ended ones — entry 1 here — and open
   for generic-close-ended ones — entry 5. The bare `return` newline `<A />` is closed and pinned.
3. **Medium, the method scope.** MOSTLY CLOSED. The HOC-returns-class and factory-returns-object
   shapes and a getter absorb; R16 pins the first two. Three key spellings leak — entry 2.
4. **Medium, the `(path, line)` key.** CLOSED. Both accessors key on the name, `scan_routes` reads
   the three-tuple, and through `--check` the collapsed one-liner grades `1 of 2` in each cell
   with no violation; so does the two-declarations line. The decorator selector on the Python side
   still routes through the same lookup: the AC5 arms at `selftest.py:2596-2602` run `--check`
   end to end and assert `py.function+decorator:load_registered.conv 1 of 1` and the violation on
   `build_x`, so a broken key would have read `0 of 1` there. The residual is entry 8, an
   annotation.
5. **Medium, typed and optional calls.** CLOSED. `shallow<Props>(<Comp />)` and
   `props.render?.(<A />)` both read `[]`; R19 pins them, and the comparison `<` control beside
   them. Not re-attacked beyond the repro.
6. **Medium, "byte-identical by construction".** CLOSED. The header and the backlog row now state
   the measurement rather than the construction; the brace-kind read looks back past markers so
   `return <A/> || { render: () => 1 }` yields `render` again; the next-statement shape yields
   `App` alone; R22 pins both on the HEAD population.
7. **Low, the DEAD CELL denominator.** CLOSED, by a different test than round 1 proposed. The
   exemption at `lexicon.py:3020-3022` is now `routed > 0` rather than `routed == extracted`, with
   a comment saying why the denominator was rejected. The complete `py.constant` partition prints
   `0 of 0` and `2 of 2` with no `DEAD CELL`. A parent empty because every name was routed has
   `routed == graded`, so the two tests agree on that surface; no lens found a case where they
   differ. Not proven, unattacked. The one place `routed > 0` is wrong is when the routing itself
   is wrong, which is entry 1's `--check` output, and that is a defect upstream of the exemption.
8. **Low, the figure `86` in five carriers.** HALF CLOSED — entry 4.
9. **Low, `body:jsx`.** CLOSED. `grep body:jsx tools/lexicon/lexicon.py` is empty.
10. **Low, the conf's PINS comment.** CLOSED. `.lexicon.conf:327-329` points at `SELECTOR_KINDS`.

## The claims, one by one

1. **Every round-1 entry is closed by these bytes.** REFUTED for entries 2, 3 and 8, each closed
   for one spelling and left open for the others; holds for the other seven.
2. **The backward ASI rule cannot end a walk inside a legitimate return expression on
   prettier-formatted React.** HOLDS, re-executed: `return (` newline element, `cond ? (` … `) :
   (` … `)`, `open && (` …, the bare ternary with `?` and `:` opening lines, a call before `?`,
   and an object literal before `:` all route at HEAD and on the scratch fix. The rule ends the
   walk too LATE, never too early — entry 1 is the opposite failure.
3. **The element-at-line-start continuation cannot attribute a module-level element to a
   preceding helper.** HOLDS by the lexer's construction and by probe: the lexer opens an element
   only after an operator, and no statement ends in one, so `const buildX = () => f()` newline
   `<div />` lexes the `<` as a comparison and yields `[]`; `const el = <div />`, `el = <div />`
   and `export default <div />` after a helper all yield `[]`; R14 pins the first. The one
   attribution it makes — `cond ?` newline `<A /> : null` — is correct.
4. **The key change did not break the decorator selector.** HOLDS — round-1 entry 4 above, via
   the AC5 arms that run the whole pipeline.
5. **R21 has a non-trivial split and would red on either half of round 1's HIGH.** HALF REFUTED
   — entry 3. The split is real (the arm asserts `{True, False}` over the arrow spellings). It
   reds on the `}`-stop half and on the old forward ceiling, measured against the base reader,
   and cannot red on the boundary half because no fixture places a statement before its `return`.
6. **Nothing in the new arms is fixture-passes-by-finding-nothing.** REFUTED for one clause —
   entry 6, R18's `C` half. R15, R16, R19, R22 and the scaffold arm each red on a staged reversal
   of the fix they pin, per the lenses' staging; R17 and R20 were not re-staged by this review.
7. **The corpus figures now live in exactly one carrier.** REFUTED — entry 4. One carrier for
   `86` within the kit; three surviving copies of `951`, `3145` and `121`.

## Landing recommendation

Do not land at `7b54230e`. Entries 1 and 2 and 5 are one commit in `lexicon.py`: the three-line
move at `:1903` with its later copy deleted, the member-arm scope opened on the body, and the
angle-run test in the backward rule; entries 3, 4 and 6 to 8 ride the same commit as comment,
annotation and fixture edits. The R15 extension (closer-ended, generic-close-ended) and R21's
fourth spelling are the two arms that turn the closed class into a pinned one, and each is to be
seen red under a staged break before the suite's green is recorded. Then `GATE_SELFTESTS=1 bash
tools/run-gates/run-gates.sh`, and the backlog row's "now depth-tracked, with the ASI line rule
applied backward" becomes true as written.

The kit suite was run against the scratch copy carrying entry 1's fix, from the scratchpad and
not from a git tree: `lexicon selftest FAILED — 3 of 752 arm(s)`, and all three are the AC6
`--expand over THIS repo` arms failing with `lexicon: not a git repo`, which is the copy's
location and not the fix. No `returns` arm and no scaffold arm is among them, so R14 to R22 and
the R21 property hold under the fix. That is a scratch result and not a recorded green; the
recorded one is owed by the remediation commit in this tree. What is in this record was
re-executed and is stated as such; what was not is named as unattacked.
