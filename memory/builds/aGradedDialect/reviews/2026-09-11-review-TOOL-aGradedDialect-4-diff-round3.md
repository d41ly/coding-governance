**Serves:** diff-review TOOL-aGradedDialect-4

# aGradedDialect — Tier-2 diff review of the `returns:jsx` selector, round 3

*Node `a`, 2026-09-13, branch `branch/lexicon-body-selector-9e4d71`. Fold review of the round-2
fixes: four primed lens passes over the remediation commit, five skeptic batches prompted to
REFUTE, one synthesis. Every code finding below was re-executed at source before it was written
here, with the two readers extracted from git (`git show <sha>:tools/lexicon/lexicon.py`, both
byte-checked; the worktree's kit files are identical to the head sha) and run side by side through
`read_ts_jsx_defs` on the same fixture table. The proposed remedies were applied together to a
scratch copy of the kit, re-measured against that table, run through the whole kit suite in place
(the working copy restored from git afterwards, verified clean), and measured over the adopter's
604 tracked `.tsx` files at `incms/main` `3a2ce818`. Each verdict is stated where it is used.*

**Reviewed range: `7b54230e00cd74e014f8787fb0fcc28763b62bb5...8e4cae2683d6d99ff46d4f62c5c37329cf09c5ba`.**
One commit, `8e4cae26`, the fold of round 2's eight entries: `tools/lexicon/lexicon.py` (the
backward ASI test moved to the head of the loop body under a depth-0 guard; the new
`check_ts_generic_close`; the method scope opened from the `(` op branch inside object and class
blocks; two annotations), `tools/lexicon/scaffold_lexicon.py` (the derived comment),
`tools/lexicon/selftest.py` (R15, R16, R18 and R21 extended; 757 arms), the `-10` backlog row, and
one file outside the kit, `tools/run-gates/run-gates.evidence.test.sh:643`, where a bare
`DC_PY=python` fallback became a named refusal.

**Round: 3.** Every entry here is either a regression the round-2 fold introduced, a residual it
left open for a spelling it did not test, or a claim the fold makes about itself. Nothing
re-reports a round-2 entry these bytes closed; those are listed as closed after the findings, with
the repro that shows it.

## Verdict: BLOCKED

No blocker, one high, two medium, one low. The high is a REGRESSION and it is the same class round
2 rated high and blocked on, re-opened in the opposite direction by the fix for it. Round 2's
closer-ended boundary was closed by running the backward ASI test before the bracket bookkeeping;
that same ordering now reads a depth-0 `)`, `]` or `}` ending a line as a boundary whenever the
next line opens with an operand after an operator the lexer does not emit. Prettier writes exactly
that for a logical test broken at `&&`: `return (` / `isValid(a) &&` / `isValid(b) ? (` / `<B />`
/ `) : null` routes `A` at `7b54230e` and returns `[]` at `8e4cae26`, semicolons or not. A
component whose only element sits behind such a line leaves the `returns:jsx` cell, is graded in
the camel parent cell, and reds the adopter's bar on a correct PascalCase name with no waiver
path, since `WAIVER_FILES` holds `verb` and `suffix` only. The backlog row says round 2's high is
folded; for closer-ended lines it is folded, and for closer-ended lines followed by an operand the
fold is what broke them.

The two mediums are one shape each side of the same walker: the new `(` branch hands every paren
in a member block to `read_ts_body_start`, which counts a comparison `<` or `>` as a bracket and
never refuses below zero, so a member value like `{ ok: (x) => x > 1 }` opens an anonymous scope
over a later `if (a < b) {` block of the enclosing component and absorbs its element; and the
generic-close reading round 2 taught the backward walk was never taught to the forward one, so the
two readers now disagree on the case the fold fixed. The low is the new helper pairing a
line-end `>` with any earlier `<` whose run happens to balance at it.

The remedy is one commit and it was trialed whole: a root fix in `read_ts_body_start`, an
`as`/`satisfies`/`new` key on `check_ts_generic_close`, and a continuation set the lexer already
knows how to compute, threaded into both readers. Under it every row of the fixture table reads the
right way, 756 of 757 arms hold with the one red being R14's ceiling fixture flipping to the
correct verdict, the 115-record conformance corpus stays 115 exact, routing on the 604-file
adopter corpus is byte-identical at 946, and four fabricated definitions vanish from one test
file. Until that lands and the arms named below are seen red under a staged break, the row's
claim about round 2 is not true as written.

### Review shape

Raw 13, confirmed 10, refuted 3, unverified 0. Precision 0.77.

The three refuted findings, raw ids 3, 8 and 13, did not reach this synthesis; nothing is said
about them here beyond the count. The ten confirmed findings consolidate into the four entries
below. Each folded entry names the raw ids it absorbs:

- Entry 1 absorbs raw ids 4 and 11 — two lenses, one loop at `lexicon.py:1934`, six repros.
- Entry 2 absorbs raw ids 1, 6 and 9 — three lenses, one branch at `lexicon.py:1780-1788`, one
  walker at `:1456-1459`.
- Entry 3 absorbs raw ids 7 and 12 — the forward twin at `lexicon.py:1546`.
- Entry 4 absorbs raw ids 2, 5 and 10 — the new helper at `lexicon.py:1890-1892`.

Severity on each entry is this report's adjudication over the merged evidence. Raw id 4 arrived
high and its skeptic confirmed it high with two corrections to the framing that this report
carries; raw id 11 arrived low for the same loop and is folded into entry 1 at the higher grade,
because it is the same defect seen through a narrower fixture. Raw ids 1, 6 and 9 arrived
medium, medium and medium; folded at medium. Raw id 7 arrived medium and raw id 12 low for the
same clause; folded at medium, because the disagreement between the two readers is what the
diff introduced. Raw ids 2, 5 and 10 arrived low; folded at low.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts
demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline.
Nothing was lost, so the zero counts here are evidence rather than a gap: the unverified set is
genuinely empty and every lens finding reached a skeptic. The finding set is COMPLETE for the
lenses that ran.

Two measurements this review made itself, because the record would otherwise rest on relayed
ones. The kit suite at the head sha: `python3 tools/lexicon/selftest.py` from this worktree,
whose kit bytes equal `8e4cae26`, printed `lexicon selftest OK — 757 arm(s)` with the conformance
line at 115 of 115 and refusal share 0. That is a review-time verdict and not the recorded one:
no `gate-logs/lexicon_selftest.log` on this node is newer than `8e4cae26` — the one in this
worktree's git dir is from 04:09 on the 11th and reads 755 arms, which is `7b54230e`; the commit
landed at 04:45. The same is true of `run-gates_evidence.log` at 04:16, which predates the edit
to line 643. The kit DoD owes a recorded `GATE_SELFTESTS=1` green for this range and there is
none to cite. And the adopter corpus: 604 tracked `.tsx` files, 946 routed definitions at
`7b54230e`, 946 at `8e4cae26`, zero files differing, so the backlog row's "the corpus figures
did not move" is TRUE on the only measured corpus, which is prettier output with semicolons and
holds none of the six shapes in entry 1. Zero movement there is a statement about that corpus,
not about the class.

## The findings, severity-ranked

### 1 — HIGH · the ASI test now runs before the closer is matched, so a closer-ended line followed by an operand is a boundary — inside a return expression

**Where.** `tools/lexicon/lexicon.py:1934-1937`, the backward ASI test in `check_ts_returned`,
now the first statement of the loop body; the closer branch it pre-empts at `:1938-1940`.

**What.** Round 2's fix moved the test ahead of the bracket bookkeeping so a depth-0 closer
ending a line breaks the walk. That is right when the next line opens a statement (`return
noop()` then `const el`) and wrong when the next line continues the expression through an
operator the lexer never emits: `&&`, `||`, `?`, `.`, `+`. The token stream cannot tell the two
apart, so the walk breaks at the closer with `r` still `None`, `check_ts_returned` answers False,
and the component leaves the cell. The base `continue`d closers before the test and never treated
a closer-ended line as a boundary, so this is a regression vs `7b54230e` and not the documented
R14 ceiling, which is a WORD-ended line. Semicolons do not mask it: the break sits inside the
expression.

**Reproduced.** Both readers side by side, `read_ts_jsx_defs`; base then head:

- `function A() {\n  return isValid(a) &&\n    isValid(b) ? (\n    <B />\n  ) : null;\n}` →
  `[('A', 1)]` then `[]`.
- `return getItems(a)\n    .length > 0 ? <B /> : null;` → routed then `[]`.
- `return items[0] ||\n    fallback ? <B /> : null;` → routed then `[]`.
- `return (\n    (a || b) &&\n    (c ? <C /> : <D />)\n  );` → routed then `[]`.
- Prettier's commonest spelling, `return (\n    hasPermission(user) &&\n    isEnabled(flag) && (\n
  <X />\n    )\n  );` → routed then `[]`.
- `return (\n    isValid(x) &&\n    isReady(y) && <Foo />\n  )` → routed then `[]`, with `);`
  too. The word-ended control `ok &&` / `ready && <Foo />` is `[]` at both, the pre-existing
  ceiling.

The ten must-route shapes round 2 listed were re-executed and all ten read identically at both
shas, so the round-2 claim holds for the shapes it named and fails for the one it did not test:
a call or index ending a line before an invisible operator.

**Why HIGH.** It is round 2's class, re-opened by round 2's fix, on prettier's own output. The
scaffold seeds the row, the pin is an equality in both directions, and a `conv` violation has no
waiver. R21's `_EXPRS` (`selftest.py:2778-2783`) holds no closer-ended line followed by an
operand, so neither property can see it; R15's new spellings pin only the boundary half; and the
1257-file identity the row still asserts was measured before this reordering — the 604-file
`.tsx` re-measurement above shows zero movement, but only because that corpus carries none of
these shapes. Impact is bounded to a component whose ONLY element sits behind such a line; one
with an early `return <Spinner />` elsewhere still routes on that mark.

**Fix.** The lexer already holds the fact the token walk lacks. Give `scan_ts_tokens` a `conts`
set beside `calls`, and a `pend` flag: set it in the catch-all branch at `:1307` and the division
branch at `:1231` — the two places an operator is consumed without a token — clear it in
`add_token`, and when a token is emitted on a later line than the previous one while `pend` is
set, record its index. Thread the set into `check_ts_returned` like `calls` and add `j + 1 not in
conts` to the backward test, and into `read_ts_expr_end` with `j not in conts` in the forward one
(entry 3 gives that clause its other half). `if (!open) return noop()` then `const el` still
breaks, because nothing but whitespace sits between `)` and `const`; `isValid(a) &&` then
`isValid(b)` continues, because `&` ran the catch-all. Do NOT key the mark on `expr_end`: a `>`
clears `expr_end` too, and the first trial of this fix did exactly that and re-opened round 2's
`return v as Foo<Bar>` boundary — the generic-close ambiguity is the reason `pend` is a separate
flag.

Verified on the scratch copy carrying all four entries' fixes: every shape above routes; the ten
must-route shapes and the two round-2 boundary shapes read as at head; the word-ended ceiling
LIFTS as well — `ok &&` / `ready && <Foo />` and R14's `cond` / `? a` / `: <B />` fixture now
route, which is the correct verdict — so R14's ceiling arm reds under the fix, by design, and is
the one red in `lexicon selftest FAILED — 1 of 757 arm(s)`, conformance 115 of 115. R14's
assertion and the `read_ts_expr_end` and `check_ts_returned` headers then state a smaller ceiling.

**Left-shift.** Add the `&&`-broken ternary, the member-chain break and the prettier
`hasPermission(user) &&` shape to `_EXPRS`, so both R21 properties cover them, and observe the
first property RED on the head ordering before the fix lands — this review saw the fixtures fail
at head, the arm has not. Then the class gate round 2 asked for and this round needed again: the
base reader is importable beside the landed one in one process (this review did it with two
`git show` extractions), so an arm that runs every `_EXPRS` fixture through BOTH and asserts that
nothing routed at the base is unrouted at the head — a one-directional ratchet on the routed
population — reds on the next reordering that trades one boundary spelling for another. It costs
one `git show` per suite run and it is the arm that would have caught rounds 2 and 3 both.

### 2 — MEDIUM · the `(` branch hands every member paren to a walker that counts a comparison as a bracket, so a member value opens an anonymous scope over a later block of the component

**Where.** `tools/lexicon/lexicon.py:1780-1788`, the new `(` op branch inside object and class
blocks; `read_ts_body_start` at `:1439-1461`, whose depth walk counts `<` and `>` at `:1456-1459`
and has no refusal below zero (`read_ts_type_end` at `:1399` has one).

**What.** Round 2 opened the method scope on the syntactic body rather than on the `_TS_NAME (`
population arm, so every `(` in a member block now reaches `read_ts_body_start`. That walker
reads past the paren list for a body brace, stepping over a return-type annotation, and it
counts `<`/`>` as brackets to do so. A comparison in the member VALUE unbalances it: after
`(x) => x > 1` the `>` takes depth to -1, the member's `,` and the literal's `}` and a `;` stop
nothing below zero, a later `if (a < b) {` restores zero through its `<`, and that block's `{`
comes back as the "method body". The branch records it as an owner -1 scope, the owner walk
picks the innermost anonymous scope, and the component's element inside that block is absorbed.
The comment at `:1786-1787` — "a `(` inside a member VALUE that is not a method finds no body
brace and opens nothing" — is measured false.

**Reproduced.** Base then head:

- `function A() {\n  const o = { wide: fns[k](el) > 600 }\n  if (items.length < 3) {\n    return
  <Empty />\n  }\n  return null\n}` → `[('A', 1)]` then `[]`.
- The prettier-stable arrow member, `const o = { ok: (x) => x > 1 }` before the same block →
  routed then `[]`; `const cfg = { n: (a + b) > 1 }` and a class field `class C { big = (a + b) >
  1 }` inside the body → routed then `[]`.
- The `<` direction, with semicolons: `const LIMITS = { fits: (w + h) < MAX };` at module level
  then `function List({ items }) { if (items.length > 0) { return <ul />; } return null; }` →
  `[('List', 2)]` then `[]`; `const cfg = { pred: (x) => x < 5 };` the same. The scope opened is
  `List`'s `if` block.
- The word-key spelling `{ wide: measure(el) > 600 }` is `[]` at BOTH shas — the member arm's
  `check_ts_body` is the same walker — and `parse_tsx_defs` fabricates `('measure', 2)` as a
  definition at both. So the diff did not create the class; it widened the trigger from `_TS_NAME
  (` to every `(` in a member block, and the arrow member is the spelling React writes.

**Why MEDIUM.** A component silently unrouted and graded as a camel offender, on ordinary code,
introduced by this diff. Narrow trigger: the element return must sit inside a later `if (a < b)
{` or `while (i < n) {` block with no depth-0 paren group between, and a top-level literal
before the component does not flip because the function's own `(` `)` stops the walk. Zero
flips on the 604-file corpus.

**Fix.** The root, in `read_ts_body_start`, not the branch: read a `<` through
`read_ts_angle_end` — a balanced run is an annotation's type arguments and is stepped over
whole, an unbalanced one compares and the reader returns `None` — and refuse when `depth` drops
below zero after a closer, since a closer that unbalances the span after a parameter list is
never part of a return type. Six lines. Verified on the scratch copy: every shape above routes,
the `measure` and `count` fabrications vanish from `parse_tsx_defs`, the R16 loop and its
original arm hold, and on the adopter corpus routing is byte-identical (946) while the
definition population moves by exactly four: `('mark', 61)` twice, `('mark', 144)` and `('mark',
151)` in `packages/blocks/src/dsl/whenRender.test.tsx`, each a call site inside an array member
(`children: [mark("HIT")]`) that both shas grade as a definition and the fix does not. That is a
population change to OWN, beside the `function` exception the header already owns, and the
backlog row's identity clause moves with it. The pre-existing ceiling where `(): { a: X } {`
opens the scope on the annotation's brace is untouched and not this diff's.

**Left-shift.** One R-arm with the object-member, arrow-member and class-field spellings, each
followed by a later `if (a < b) {` block returning the component's only element, asserting the
component routes AND `parse_tsx_defs` grades no definition at the call site — the second half
pins the population change. Add the same three to R16 as the branch's negative half, since R16
today asserts only that a method's container is NOT routed and never that a non-method paren
opens nothing.

### 3 — MEDIUM · the generic-close reading was applied to the backward walk only, so the two readers now disagree on the case the fold fixed

**Where.** `tools/lexicon/lexicon.py:1546-1548`, the ASI test in `read_ts_expr_end`, which bounds
every brace-less arrow scope and still reads every `>` in the shared `_TS_EXPR_CONTINUES` as a
continuation; `check_ts_generic_close` at `:1884`, called from the backward test at `:1935` and
from nowhere else.

**What.** Round 2 taught the backward walk that a `>` ending a line is two things — a generic
close after a word is a boundary, a comparison a continuation — and built a helper for it. The
forward twin, which decides where a brace-less arrow body ENDS, was not given the clause, so an
arrow ending in `as Foo<Bar>` still swallows the next statement's element. The instance was
gated (R15's `useGen` fixture is the block spelling), the class was not (§7): the arrow spelling
of the same fixture routes the helper, and a component whose brace-less helper ends in a generic
assertion loses its own element to that helper.

**Reproduced.** Identical at base and head for the arrow spelling, which is why it is a
half-applied fix and not a regression:

- `const useGen = (v) => v as Foo<Bar>\nconst el = <A />` → `[('useGen', 1)]` at both; with a
  `;` → `[]`.
- The block spelling `function useX(v) {\n  if (!v) return v as Foo<Bar>\n  const el = <A />\n
  return el\n}` → `[('useX', 1)]` at base, `[]` at head — the two readers agreed-wrong before and
  disagree now.
- The worse variant: `function Panel() {\n  const getRef = () => ref as RefObject<HTMLDivElement>\n
  return <div ref={getRef()} />\n}` → `[('getRef', 2)]` at both: `Panel` is not routed AND
  `getRef` is falsely routed, two wrong verdicts from one line-end `>`; the word-ended control
  `const getRef = () => ref` gives `[('Panel', 1)]`.

**Why MEDIUM.** Semicolon-free adopters only, and the shape is a brace-less helper ending in a
generic assertion, which is rare. It is medium rather than low because the diff made the two
readers disagree on a stated invariant — R21 property (1) is exactly "three spellings, one
verdict" and its fixtures are single-statement so it cannot see this — and because the `Panel`
variant is two wrong verdicts, one of them a real component lost.

**Fix.** One clause at `:1546`: `and (toks[j - 1][1] not in _TS_EXPR_CONTINUES or
check_ts_generic_close(toks, j - 1))`, plus `j not in conts` from entry 1 so the forward reader
takes the same two facts as the backward one. Verified on the scratch copy: `useGen` refused in
both placements, `Panel` routed and `getRef` not, `arrow_word_eol` still refused, R14 to R22
unchanged except R14's lifted ceiling.

**Left-shift.** The arrow-spelling mirror of R15's `useGen` fixture beside R14's third check,
asserting `[]` and seen red before the clause lands; and the `Panel` fixture asserting `[('Panel',
1)]`, which pins both wrong verdicts at once. Then a fourth spelling in R21 — `const A = () =>
<expr>` followed by a module-level `const el = <div />` — so the forward reader's boundary is
inside the property the way entry 1's fourth spelling puts the backward one there.

### 4 — LOW · `check_ts_generic_close` pairs the `>` with any earlier `<` whose run balances at it, so a comparison pair reads as a generic close

**Where.** `tools/lexicon/lexicon.py:1890-1892`: the helper walks back up to 400 tokens for any
op `<` whose `read_ts_angle_end` lands at `j + 1` and then asks only whether a word precedes it;
`read_ts_angle_end` (`:1316`) stops on `;` or an unbalanced closer and on nothing else.

**What.** Neither reader stops at a line break, a `return` or the body's `start`, so an
unparenthesised comparison `<` earlier in the same block — or earlier in the same line — pairs
with a comparison `>` ending a line of the return expression, `toks[i - 1]` is a word, and the
`>` becomes a statement boundary. The claim that the helper "cannot misread a comparison `>` at
line end" holds for the two probes named — `return a >` newline `b ? <B /> : null` and `x > y`
with a word `x` both route at head — and fails whenever an unpaired `<` precedes.

**Reproduced.** Base then head, semicolon-free (a `;` after the `<` line ends the run, and the
`;` control routes at both):

- `function A() {\n  const small = w < h\n  return a >\n    b ? <B /> : null\n}` → `[('A', 1)]`
  then `[]`; `const isNarrow = width < 400` / `return width >` / `800 ? <Wide /> : <Narrow />`
  the same. Without the earlier `<` line both shas route, isolating the cause.
- Same line: `return a < b && c >\n    d ? <B /> : null;` → routed then `[]` — the stream is
  `a < b c > d`, the `&&` and `?` unemitted, and the run from `<` ends exactly at the `>`.

**Why LOW.** Regression vs base, but reachable only on hand-formatted source: prettier breaks the
test at `&&` and leaves the `>` mid-line, and on that output both readers already stop at the
word-ended earlier line. Zero flips on the corpus. The inline comment at `:1930-1933` states the
comparison case as a continuation, and the fixtures falsify it, so it is a defect against stated
design rather than a declared ceiling.

**Fix.** Key the check on the positions a statement-ending generic close can occupy: after the
`<` at `i`, walk back over consecutive `word` tokens (a dotted name, since `.` is not emitted)
and require the token before them to be `as`, `satisfies` or `new`; anything else answers False.
`return v as Foo<Bar>` and `Foo<{ a: X }>` still pair because `}` is not a stop; `a < b && c >`
does not, because the walk reaches `return`. The `new` key is not decoration: `if (!v) return
new Map<string, Foo>` with no call parens then `const el = <A />` is refused at head and the
two-keyword key re-routed `useX` on the first trial, so the third keyword was added and the
boundary re-measured refused. Verified on the scratch copy: all three comparison fixtures
route, all three boundary spellings refuse with or without an earlier `<` comparison,
conformance 115 of 115.

**Left-shift.** Pin `a < b && c >` newline `d ? <B /> : null` and the `const small = w < h`
prefix form in `_EXPRS` — the second as a fourth spelling with the comparison line before the
`return`, since the property arm today has no fixture with a statement before the return. Then
the next stop-set edit in either reader reds there.

## Round 2's eight entries, one by one

Each was re-executed at `8e4cae26`:

1. **High, the closer-ended boundary.** CLOSED for the instance, RE-OPENED as entry 1 here. `if
   (!open) return noop()` then `const el = <Modal />` → `[]`; `return []`, `return {}` and the
   multi-line object → `[]`; R15 carries all four spellings and R21's second property carries
   the class, seen red under the staged re-ordering by this review (8 of 15 expressions cross).
   The move that closed it is what opened entry 1.
2. **Low, three method spellings leak.** CLOSED. `render<T>(`, `[k](`, `'render'(`, `async
   render(`, `get el(`, `42(` all absorb; R16's loop asserts the seven and was seen red by this
   review with the `(` branch opening nothing (all seven leak, and the original R16 arm reds
   too). The branch's widening is entry 2 here.
3. **Low, R21's comment claims both halves.** CLOSED. The comment names what each property pins
   and says outright that property (1) cannot red on the boundary half; the staging above
   measured property (1) at zero disagreements under the round-2 ordering, which is the sentence
   made true.
4. **Low, the corpus figures in three carriers.** CLOSED within the kit. `951`, `3145` and the
   two `121`s are gone from `selftest.py:2606` and `:2665`; the backlog row's clause now reads
   "now one code carrier, dated, plus this record". `LEXICON.md` and `README.md` were not
   re-checked by this review.
5. **Low, `>` inherited as a continuation.** CLOSED for the backward walk by the helper, which is
   entry 4's subject; NOT applied forward, which is entry 3.
6. **Low, R18's `C` half.** CLOSED. The block sits between the `return` and the element, `return
   f(() => { a; b; }) ? <D /> : null`, and the arm names the `;` above depth zero.
7. **Low, the scaffold comment literal.** CLOSED. `scaffold_lexicon.py:413-415` renders the row
   from `SEED_SELECTORS[("tsx", "function")]` and the arm at `selftest.py:1026` builds its
   expectation from the same tuple.
8. **Low, the two-tuple annotations.** CLOSED. Both accessors read `dict[tuple[str, int, str],
   set]`.

## The claims, one by one

1. **The ASI-first ordering cannot end a walk inside a legitimate return expression on
   prettier-formatted React or on the ten must-route shapes.** HALF REFUTED. All ten must-route
   shapes read identically at both shas, re-executed here. Prettier's `&&` chain with a call or
   index operand at line end — six spellings, entry 1 — routes at base and not at head.
2. **`check_ts_generic_close` cannot misread a comparison `>` at line end as a generic close.**
   REFUTED for an unpaired `<` earlier in the block or the line, entry 4; HOLDS for the two
   probes the claim names.
3. **The `(`-branch method scope cannot open a scope on a non-method `(` in a way that hides a
   component's own returned element.** REFUTED, entry 2, on six spellings including the
   prettier-stable arrow member; the branch's own comment is the claim and it is measured false.
4. **R21's second property genuinely reds on the boundary half.** HOLDS, re-staged by this
   review: with the ASI test moved back below the `if depth: continue` line, `_CROSSED` holds 8
   of the 15 expressions; at head it is empty. Under the same staging property (1) reports zero
   disagreements, which confirms the comment's statement that it cannot see that half.
5. **R16's seven-spelling loop exercises the scope, not just the population arm.** HOLDS,
   re-staged: with `add_scope(read_ts_body_start(toks, k), -1)` replaced by `pass`, all seven
   keys leak and the loop reds; the original R16 arm reds beside it, routing `withLogger` and
   `buildCols`. Nothing else in the diff opens a method scope, so the loop is measuring the
   branch.
6. **The run-gates fix does not weaken the evidence test, and the leg is green.** HOLDS. The
   ban predicate from `tools/lib/resolve-python.test.sh` run over both blobs hits `BASE 643:[ -n
   "$DC_PY" ] || DC_PY=python` and nothing at head; `bash tools/lib/resolve-python.test.sh` at
   HEAD printed `PASS — resolve-python: 55 assertions held`, rc 0, read from a file. The refusal
   is the file's own idiom — five other `exit 2` refusals sit at lines 18, 216, 513, 630 and
   632 — and a leg exiting 2 reds the bar rather than running an unresolved launcher, which is
   stronger, not weaker. The bare fallback arrived in `d4c05068`, another build. What this
   review did NOT run is the `run-gates evidence` leg itself (696 s on the ledger); its
   recorded log predates the edit, so its green at this sha is unrecorded.

## Landing recommendation

Do not land at `8e4cae26`. Entries 1 to 4 are one commit in `lexicon.py`, trialed together on a
scratch copy and through the suite in place: the `conts` set and `pend` flag in `scan_ts_tokens`
threaded into both readers; the `<`-as-run and below-zero refusal in `read_ts_body_start`; the
`as`/`satisfies`/`new` key in `check_ts_generic_close`; the one clause in `read_ts_expr_end`. Under it
the suite reads `1 of 757` red and the red is R14's ceiling fixture routing — re-pin it as routed
and shrink the ceiling sentence in both readers' headers, since the word-ended form is lifted
along with the closer-ended one. Then the arms: the three entry-1 shapes and entry 4's two in
`_EXPRS`, entry 2's three spellings with the no-definition half, entry 3's `useGen` arrow and
`Panel` fixtures, each seen red under a staged break before the suite's green is recorded; and
the base-beside-head ratchet arm if the owner takes it. The backlog row then owns two facts it
does not today: the definition population moved by four fabricated `mark` sites on the adopter
corpus, and the routed population there is 946 at every one of the three readers. Then
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — the recorded green this range owes and
does not have.

What is in this record was re-executed and is stated as such; what was not — `LEXICON.md` and
`README.md` for entry 4 of round 2, the evidence leg's own run, the `.ts` half of the 1257-file
figure — is named as unattacked.
