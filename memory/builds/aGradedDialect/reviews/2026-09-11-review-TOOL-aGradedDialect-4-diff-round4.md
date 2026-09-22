**Serves:** diff-review TOOL-aGradedDialect-4

# aGradedDialect — Tier-2 diff review of the `returns:jsx` selector, round 4

*Node `a`, 2026-09-13, branch `branch/lexicon-body-selector-9e4d71`. Fold review of the round-3
fixes: four primed lens passes over the remediation commit, four skeptic batches prompted to
REFUTE, one synthesis. Every code finding below was re-executed by this synthesis at the head sha
before it was written here — the worktree's `tools/lexicon/` is byte-identical to `e6d81f58`
(`git status` clean under `tools/`), the base reader was extracted with `git show
fbbcb70c:tools/lexicon/lexicon.py`, and a third copy with the one contested line removed was
loaded beside them so each verdict is stated base · head · staged where that is the question.
The kit suite was run once from this worktree, `python3 tools/lexicon/selftest.py`, redirected to
a file and grepped, never tailed: `lexicon selftest OK — 765 arm(s)`, 115 of 115 conformance
records in exact agreement, refusal share 0, rc 0. Skeptic measurements this synthesis did not
repeat are attributed as such where they are used.*

**Reviewed range: `fbbcb70c9be0e2b2013c4196f3ff64c5a19f44e4...e6d81f587e87c01d716f428e2cb93e954afaff8d`.**
The base is the commit AFTER the branch merged `origin/main` and re-stamped the manifest, so
`base...head` is exactly round 3's remediation commit `e6d81f58`: `tools/lexicon/lexicon.py`
(`scan_ts_tokens` gains `conts` and `pend`; `read_ts_body_start` reads `<` as a balanced run or
refuses, and refuses below zero; `read_ts_expr_end` takes `conts` and the generic-close test;
`check_ts_generic_close` keyed on `_TS_GENERIC_HEADS`; `check_ts_returned` takes `conts`;
`parse_ts_source` threads both sets and its header now owns two population exceptions),
`tools/lexicon/selftest.py` (R14 rewritten, R21's list and a third property, R23, R24; 765 arms),
and the `-10` backlog row. The round-3 review record and a one-line spec touch ride in the same
range and were not attacked.

**Round: 4.** Every entry here is either a regression the round-3 fold introduced, a residual it
left open for a spelling it did not test, or a claim the fold makes about itself. Nothing
re-reports a round-3 entry these bytes closed; those are listed as closed after the findings, with
the repro that shows it.

## Verdict: CLEAN WITH FIXES

No blocker, no high, two medium, four low. For the first time in this review the head reader is
RIGHT on every shape the previous round demanded, first-hand: the five prettier shapes of round
3's high route in all three spellings, the member-value comparison opens no scope, the forward and
backward readers agree, and the suite is green at 765 with the conformance corpus at 115 of 115.
What is wrong is smaller than the code and it is in two places the code makes claims about
itself.

The first medium is a §7 matter. `read_ts_body_start`'s below-zero refusal — the half of round
3's entry 2 that removed nine fabricated call-site definitions from the adopter corpus — is
pinned by NO arm: with the two lines `if depth < 0: return None` deleted, the R23 loop leaks
nothing, the 115 fixtures read identically, and a skeptic's full run on a frozen clone printed the
same `765 arm(s)` green, while `parse_tsx_defs` fabricates `blk` again on the header's own
example. The header at `lexicon.py:1760` says "Each is pinned by an arm", and for this half that
is false; the arm that was seen red under `r4-body-start-counts-angle` reds only because that
break reverts BOTH halves of the fix together. Four lenses hit this independently. The second
medium is a class the diff certifies as closed and is not: a line that CLOSES with a token-less
operand — `open ? 'Open' : 'Closed'`, `` (i) => `k-${i}` ``, `state.value = ''` — is still read by
both ASI readers from the last EMITTED token, so in semicolon-free `.tsx` a component whose helper
ends so loses its route and the helper takes it. Pre-existing at base, identical verdicts there;
what is new is the docstring at `:1574` and the R14 comment stating the `(`/`[` ceiling as the
only one, and an R14 arm whose label claims the class while its fixture reaches one instance.

The four lows are two narrow regressions (a non-ASCII whitespace byte sets `pend`, and a TS 4.7
instantiation expression at line end now continues where round 2's any-word key ended it), the
unbounded backward walk in `check_ts_generic_close` crossing a `return`, and one comment in
`check_ts_returned` still describing the predicate round 3 replaced. None of the six changes a
verdict on the measured adopter corpus. All six are owed before the header's "pinned", the
docstring's "the ceiling that remains", and the backlog row's account of round 3 are true as
written, which is why this is CLEAN WITH FIXES and not CLEAN; and none of them is a wrong grade on
prettier's default output, which is why it is not BLOCKED.

### Review shape

Raw 12, confirmed 11, refuted 1, unverified 0. Precision 0.92.

The refuted finding, raw id 9, did not reach this synthesis; nothing is said about it here beyond
the count. The eleven confirmed findings consolidate into the six entries below. Each folded entry
names the raw ids it absorbs:

- Entry 1 absorbs raw ids 1, 4, 7 and 10 — four lenses, one branch at `lexicon.py:1494-1495`,
  one header sentence at `:1760`, four repros that agree.
- Entry 2 absorbs raw ids 5 and 11 — two readers, one missing fact from the lexer.
- Entry 3 absorbs raw ids 6 and 8 — the two loops of `check_ts_generic_close`, `:1945` and `:1948`.
- Entry 4 is raw id 3. Entry 5 is raw id 2. Entry 6 is raw id 12.

Severity on each entry is this report's adjudication over the merged evidence. Raw ids 1, 4, 7
and 10 arrived medium, medium, medium and medium; folded at medium. Raw ids 5 and 11 arrived
medium and medium; folded at medium, and the fold is deliberate: they are one fact the lexer does
not hand over, read wrongly by two readers, and one channel closes both. Raw ids 6 and 8 arrived
low and low; folded at low. Raw ids 3, 2 and 12 arrived low and stand at low. No severity was
raised or lowered against a skeptic's verdict.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED. 0 contradictory verdicts
demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline.
Nothing was lost, so the zero counts here are evidence rather than a gap: the unverified set is
genuinely empty and every lens finding reached a skeptic. The finding set is COMPLETE for the
lenses that ran.

Two measurements this review made itself. The kit suite at the head sha, from this worktree whose
kit bytes equal `e6d81f58`: `lexicon selftest OK — 765 arm(s)`, 115 of 115, refusal share 0,
rc 0, read from a file. That is a review-time verdict and not the recorded one: the newest
`lexicon_selftest.log` in this worktree's git dir is still the 04:09 one from the 11th at 755
arms, which is `7b54230e`, two folds ago; the gate ledger's `lexicon selftest` row names a tree
fingerprint from the same run. The kit DoD owes a recorded `GATE_SELFTESTS=1` green for this
range and there is still none to cite. And the claims list's eight staged-break names —
`r4-conts-never-recorded`, `r4-pend-not-set-in-catchall`, `r4-string-keeps-pend`,
`r4-body-start-counts-angle`, `r4-forward-no-generic-close`, `r4-generic-close-any-word`,
`r4-forward-ignores-conts`, plus the round-3 set — appear nowhere in the tree: the commit message
says "eight breaks" and names none, so "every new arm seen red" is carried by the commit message
alone. Entry 1 is the measured consequence: an arm can be seen red under a break that reverts two
lines at once while one of the two lines is pinned by nothing.

The adopter-corpus statement — 1261 of 1265 files identical, the four that differ lose nine
fabricated call sites and gain nothing, routed 946 on both sides — was re-measured by the skeptic
on raw id 7 (four files, the lost names `W`, `blk`, `mark`, `plan`, nine lost, zero gained, 946
routed both sides) and is consistent with the code. This synthesis did not repeat that
measurement.

## The findings, severity-ranked

### 1 — MEDIUM · the below-zero refusal in `read_ts_body_start` is pinned by no arm, and the header says it is

**Where.** `tools/lexicon/lexicon.py:1494-1495`, the two lines `if depth < 0: return None`
after a `)` or `]` in `read_ts_body_start`; `tools/lexicon/lexicon.py:1755-1760`, the
`parse_ts_source` header's second population exception and its "Each is pinned by an arm";
`tools/lexicon/selftest.py:2847`, the R23 loop whose comment claims "the population change this
fix makes, owned here".

**What.** Round 3's entry 2 had two halves in one function: read `<` as a balanced run or refuse,
and refuse below zero. The first half is what stops `(x) => x > 1` in a member value walking into
a later `if (a < b) {`; the second is what stops a call inside an array member — `rail:
[blk("Callout", { title: "R" })]` — balancing by accident onto a later `{` and being graded as a
method named `blk`, the nine adopter sites the commit says are gone. R23's four members —
`fns[k](el) > 600`, `(x) => x > 1`, `(a + b) > 1`, `measure(el) > 600` — all take the `<`-run
path or end on the member block's depth-0 `}` before any `)` or `]` can drive the depth negative;
the refusal is reachable only through a `]` at depth 0, since a `)` at depth 0 is already caught
by the `(";", ")", "}", ",")` tuple above it. R24 is the forward reader and never enters this
function. So the second half is pinned by nothing, and the header sentence that says otherwise
sits six lines below the exception it describes.

**Reproduced.** Head beside a copy of the head kit with only `:1494-1495` deleted (the `<`-run
branch intact), `parse_tsx_defs` names:

- `const o = { rail: [blk("Callout", { title: "R" })] }` / `const rows = [{ el: <A /> }]` —
  head `[]`, staged `['blk']`; base `fbbcb70c` also `['blk']`, so the fix is real.
- `const o = { rail: [blk('Callout', { title: 'R' })] }` / `run({ a: 1 })` — head `[]`, staged
  `['blk']`.
- `const spec = { rail: [blk("x")], other: [{ a: 1 }] }` — head `[]`, staged `['blk']`; inside a
  component the skeptic on raw id 10 measured `('blk', 2)` beside the component.
- The R23 loop, replicated verbatim against both modules: `leaked=[]` on head AND on the staged
  copy. The arm cannot see the line.
- The skeptic on raw id 10 ran the whole suite on a `--local` clone with the two lines deleted:
  `lexicon selftest OK — 765 arm(s)`, rc 0. The skeptic on raw id 7 ran it in place with the same
  result modulo three out-of-tree AC6 failures present on both sides. Nothing in 765 arms
  observes the refusal.

Three side claims from raw id 7, each measured by that skeptic and consistent with what this
synthesis read: the `<`-run branch replaced by `pass` reds nothing on its own either, though `f():
Promise<{ a: string }> {` as a method inside a component then mis-scopes the method onto the type
literal's brace; `satisfies` in `_TS_GENERIC_HEADS` has no arm (the only `satisfies` in
`selftest.py` or the fixture file is inside a fixture comment) while `new` has R24's third arm;
and the `"fns" in _names` half of R23's assertion can never fire, because `fns[` reaches no `(`,
`:` or `=` arm of the member reader, so that half is vacuous.

**Why MEDIUM.** Head is correct; the population change is real and was measured; the code
review of the branch finds nothing wrong with it. What is wrong is that a future edit can drop or
reorder two lines with a green bar and the nine-site fabrication class returns silently, and that
the diff's own header asserts coverage that does not exist. That is §7's "a gate you have only
ever seen pass" one level up — the fix was seen red, but only bundled with its sibling — and it
is the exact class the backlog row's "every one seen red under a staged break by name" is meant to
exclude. Not high because no verdict at head is wrong and no adopter file moves.

**Fix.** Three arms and one sentence.

1. A fifth R23 member that only the below-zero rule refuses — a `]`-unbalanced tail with no `<`
   and no depth-0 closer before the next `{`: `const spec = { rail: [blk("x")], other: [{ a: 1
   }] }`, both inside `function A() { … return <Empty /> }` asserting `"blk" not in _names` and
   `A` still routed, and at module level followed by `run({ a: 1 })` asserting `"blk" not in
   _names`. Stage the two-line deletion alone and observe the arm RED before the green is
   recorded; the R23 loop as it stands will not red under that staging, which is the finding.
2. One method fixture with a type-literal generic return — `class C { f(): Promise<{ a: string
   }> { return <M /> } }` inside a component that returns `null` — asserting the component is NOT
   routed, so the `<`-run branch is pinned on its own.
3. A `satisfies` twin of R24's `new` arm: `if (!v) return v satisfies Foo<Bar>` then `const el =
   <A />` → `[]` (verified `[]` at head by this synthesis, so the arm lands green and needs its
   staged red: drop `satisfies` from the set).
4. Either make the `"fns"` half of R23 reachable or delete it; a dead assertion reads as coverage.

Then the header sentence is true and can stay.

**Left-shift.** The arms above are the gate. The class one level up — a fix commit whose every
line is pinned only in a bundle — has a documented check and no machine one: a staged break is
named per LINE of the fix, not per arm, and the commit message names the breaks it ran. The
round-3 review asked for the arms "each seen red under a staged break"; this round shows why
"each" must bind to the line.

### 2 — MEDIUM · a line closing with a token-less operand is invisible to both ASI readers and to the arrow-body reader, and the diff certifies the class as closed

**Where.** `tools/lexicon/lexicon.py:1584`, the ASI test in `read_ts_expr_end`, which decides a
line break from `toks[j - 1]`, the last EMITTED token; `:1995`, the backward twin in
`check_ts_returned`, which decides from `toks[j]` the same way; `:1538` and `:1553`, the two
returns of `read_ts_arrow_body`, which hand back `k + 2` / `j + 1` unconditionally; the docstring
at `:1574-1576` and the R14 comment at `selftest.py:2703` stating the `(`/`[` ceiling as the only
one; the R14 arm at `selftest.py:2722` whose label reads "a string, a template or a regex after an
operator is an operand, so the next line's element belongs to nobody".

**What.** Round 3's `conts` channel tells the readers when a line OPENS after a silent operator.
Nothing tells them when a line CLOSES with a silent operand. A string, a template and a regex emit
no token, so after `open ? 'Open' : 'Closed'` the last emitted token is the `:` — in
`_TS_EXPR_CONTINUES` — and both readers continue into the next line; after `state.value = ''` it
is the `=`, same result. And `read_ts_arrow_body` returns the index of the token after `=>`, which
for a literal body is the NEXT statement's first token, so the scope of `` (i) => `k-${i}` ``
opens on the `return` two lines down and `check_ts_returned` grades that line's element as the
arrow's value. The R14 arm pins `a + "x"`, where the last emitted token is the word `a` and the
existing rule already ends the line; the label claims the class, the fixture reaches the one
instance where `pend` is the mechanism, and the instance was green at base.

**Reproduced.** Base then head, `read_ts_jsx_defs`, identical at both — this is a residual, not
a regression:

- `function Panel({ open }) {` / `const label = () => open ? 'Open' : 'Closed'` / `return
  <div>{label()}</div>` / `}` → `[('label', 2)]` at base and head. Control with word operands
  `open ? a : b` → `[('Panel', 1)]`; control with semicolons → `[('Panel', 1)]`.
- `const reset = () => state.value = ''` before `return <input />` in `Form` → `[('reset', 2)]`.
- `function List() {` / `` const key = (i) => `k-${i}` `` / `return <ul />` / `}` → `[('key',
  2)]` at base and head; `List` is not routed. String and regex bodies the same; a `1` body →
  `[]`, and a `;` after the literal → `[]`.
- Module level, `const label = () => 'x'` / `const el = <A />` → `[('label', 1)]` for string and
  regex bodies; `1` → `[]`.

**Why MEDIUM.** Two wrong verdicts from one line, in opposite directions — the helper graded
under the component convention and the component graded in the parent cell, both false reds on
correct names with no waiver path — on a shape prettier `semi: false` emits verbatim, and one
(the template-literal key helper inside a component) that is ordinary React. Pre-existing and
identical at base, so no adopter file moves and the identity measurement cannot see it; the
measured adopter corpus writes semicolons. Medium rather than low because the diff does not leave
it as a known miss: two docstrings and an arm label say the ceiling is `(`/`[` and the class is
closed. Medium rather than high because nothing regressed and the default prettier profile never
reaches it.

**Fix.** One lexer side channel, the pattern `conts` already set, closing both readers and the
arrow-body reader at once rather than one set per reader. At the three sites that clear `pend`
for a silent LITERAL — the string at `:1237`, the template close at `:1250`, the regex — record
`lits.add(len(toks))` when not suppressed: the index the NEXT emitted token will take. Thread it
through `parse_ts_source` beside `conts`. Then:

- `read_ts_expr_end` (`:1584`): a line break at `j` is a boundary when `j in lits and j not in
  conts` and the new line does not open with `:`, `,` or an element — the earlier line closed with
  an operand, whatever it emitted.
- `check_ts_returned` (`:1995`): the same, with `(j + 1) in lits`.
- `add_scope` in `parse_ts_source`: when `body in lits`, the body token sits on a later line than
  its predecessor, and `body not in conts`, the arrow's value was the literal and the scope is
  empty — `=> 'x' +` newline `cond && <A />` still opens at `cond` because `cond` is in `conts`.

The skeptic on raw id 11 prototyped the `add_scope` half by monkeypatch: the three module cases go
to `[]`, `List` routes, R14, R21, R23 and R24 unchanged. The two reader clauses are proposed and
NOT trialed by this review. If the channel is deferred instead, correct the two ceiling
statements and the R14 label, and file a backlog row for the class; a ceiling that is stated is
not a defect, a ceiling that is stated as closed is.

**Left-shift.** Pin the Panel/label shape in both spellings and the three literal bodies at
module level as R14 siblings, and add `open ? 'a' : 'b'` and `` `k-${i}` `` as R21 expressions so
the three-spelling agreement property covers a silent operand at line end. Seen red first: the
arms land red today, which is the cheapest staged break there is.

### 3 — LOW · `check_ts_generic_close` walks back across a `return`, so an `as` anywhere earlier turns a comparison `>` into a boundary

**Where.** `tools/lexicon/lexicon.py:1945`, the loop that searches back up to 400 tokens for a
`<` whose run balances at `j`; `:1948`, the head walk that steps over every consecutive word
until it meets a member of `_TS_GENERIC_HEADS`.

**What.** Neither loop stops at a statement boundary. `read_ts_angle_end` from an unpaired `<`
walks over `MAX`, `return`, `count` (it stops only at `;`, an unbalanced closer or 400 tokens)
and balances at a line-end `>` two statements later; the head walk then steps over `number` to
`as` and returns True. And because `&&`, `||`, `?` and `.` are never emitted, unrelated words are
consecutive, so `return v as Foo && a < b && c >` reaches the `as` at the head of the line, and
`const v = x as Foo` on the line ABOVE reaches it through `return`. The `_TS_GENERIC_HEADS`
comment says "a `>` that pairs with an earlier `<` under any other head is a comparison" without
saying that "earlier" is unbounded.

**Reproduced.** Base then head, `read_ts_jsx_defs`; these are pre-existing at base too, where
the any-word key gave the same verdict by a different route:

- `function A() {` / `const small = size as number < MAX` / `return count >` / `limit ? <B /> :
  null` / `}` → `[]` at base and head; control `const small = w < h` → `[('A', 1)]` (R21 property
  3's fixture); semicolons → `[('A', 1)]`.
- `return v as Foo && a < b && c >` / `d ? <B /> : null` → `[]`; `const v = x as Foo` / `return a
  < b && c >` / `d ? <B /> : null` → `[]`; the control without the cast → `[('A', 1)]`.

`(size as number) < MAX` is valid TS — `as` binds at relational precedence — so the shape is
legal, but prettier parenthesises an `as` inside a binary expression and the `)` stops the head
walk, so only hand-written semicolon-free source with a line broken after a comparison `>` reaches
it.

**Why LOW.** A component losing its route is a wrong grade, and it is reachable; but the reach is
a style prettier never emits, base gave the same verdict, and R21 property 3 already pins the
head-less prefix.

**Fix.** Two one-condition bounds. In the `<`-search at `:1945`, return False on reaching a `;`
op or a word in `_TS_EXPR_WORDS` before the `<` is found — no type-argument run contains either.
In the head walk at `:1948`, stop at a word in `_TS_EXPR_WORDS - _TS_GENERIC_HEADS`, so `return`
reads as a non-head and the cross-statement case returns False. Name the same-line `as Foo && a <
b && c >` shape as a ceiling in the `_TS_GENERIC_HEADS` comment if it is not closed by the second
bound.

**Left-shift.** `size as number < MAX` as a second prefix in R21 property 3, and the two `as`
shapes above as R21 expressions.

### 4 — LOW · a TS 4.7 instantiation expression at line end now continues where round 2 ended it — a ceiling the `as`/`satisfies`/`new` key created and nothing states

**Where.** `tools/lexicon/lexicon.py:1934`, `_TS_GENERIC_HEADS` and its comment; R24, which pins
the three heads and no fourth.

**What.** `return makeBox<string>` followed by a line break is an instantiation expression that
ENDS the statement (TypeScript 4.7+, `canFollowTypeArgumentsInExpression` honours a preceding
line break). Its head chain is `makeBox` → `return`, an expression word and not a head, so the
round-3 predicate reads the `>` as a comparison and continues into the next line. Round 2's
any-word key ended it, correctly by accident.

**Reproduced.** `function useBox() {` / `if (x) return makeBox<string>` / `const el = <A />` /
`return el` / `}` → `[]` at base, `[('useBox', 1)]` at head — a regression in this range; a `;`
or `()` after `<string>` restores `[]` at head, so the line-end `>` is the only thing that moved.
The brace-less spelling `const useBox = () => makeBox<string>` / `const el = <A />` routes at
both shas.

**Why LOW.** Rare shape — zero line-ending instantiation expressions in the 1265-file adopter
corpus by the skeptic's regex — a false red not a false green, and the trade that created it
closed a shape that is common. But it is a reachable regression this round made and neither the
comment nor an arm states it.

**Fix.** A head-free rule cannot tell `return a < b && c >` from `return makeBox<string>`, since
both chains end at `return`; state the ceiling beside `_TS_GENERIC_HEADS` — a bare instantiation
expression ending a line is read as a comparison — and note the round-2→3 trade there.

**Left-shift.** Pin the `useBox` fixture in R24 at the CURRENT verdict, `[('useBox', 1)]`, with
the comment saying it is the ceiling, so a later change is a red and not a surprise.

### 5 — LOW · a non-ASCII whitespace byte falls to the operator catch-all and sets `pend`, so the next line is a continuation

**Where.** `tools/lexicon/lexicon.py:1218`, the code-frame whitespace test `if c in " \t\r":`;
`:1331`, the catch-all `pend = True` it falls through to.

**What.** U+00A0, U+000C, U+2028 and U+3000 are whitespace to TypeScript and not to this test,
so each is consumed as if it were a silent operator: `pend` goes True, and `add_token` records the
next line's first token in `conts`. The same file's other whitespace skip near `:863` was already
moved to `.isspace()` with a comment that skipping only space and tab bit them, so this is the
known class in the one frame that did not get the fix. Regression in this range: base routes
neither shape because base had no `pend`.

**Reproduced.** NBSP indentation, `function useThing() {` / `if (!open) return noop()` / `const
el = <Modal />` / `return el` / `}` → `[]` at base, `[('useThing', 1)]` at head; ASCII indentation
`[]` at both. `const buildX = () => 1` / `export const el = <div />` with NBSP → `[('buildX',
1)]` at head, per the skeptic.

**Why LOW.** A false red only — a false continuation only ever ADDS a route — and the skeptic's
byte scan of the 1265-file adopter corpus finds exactly one NBSP, inside a comment, so the
"common copy-paste artifact" framing does not hold for this corpus. It holds for any corpus that
is not prettier output.

**Fix.** `if c.isspace():` at `:1218`; the `\n` case is handled the line above, so line counting
is unchanged.

**Left-shift.** One R14 arm with an NBSP-indented `const el = <A />` after a closer-ended early
return, asserting `[]`; lands red today.

### 6 — LOW · the comment in `check_ts_returned` still states the any-word predicate the diff replaced

**Where.** `tools/lexicon/lexicon.py:1988-1990`: "a `>` at line end is two things: the close of
a generic run after a word (`return v as Foo<Bar>`), a boundary; or a comparison".

**What.** That is the pre-round-3 predicate — the old `check_ts_generic_close` docstring said "a
type-argument run that follows a word" and the old code was `toks[i - 1][0] == "word"`. This diff
keyed the helper on `_TS_GENERIC_HEADS`, added the `a < b && c >` newline comparison as a THIRD
reading, and edited the comment lines immediately below this sentence while leaving it standing.
Two answers to one question inside the function that calls the predicate.

**Why LOW.** A maintainer restoring the any-word test on the comment's authority would be caught:
this synthesis staged exactly that (the head walk replaced by `return toks[i - 1][0] == "word"`)
and R21 property 3 reds on `a >` newline `b ? <B /> : null` behind a `w < h` statement. Note for
the record that it is property 3 and NOT property 1 that catches it, as raw id 12's rationale
said: under the any-word key all three spellings agree on the wrong verdict, so the agreement
property is silent. One comment line.

**Fix.** Reword to "the close of a generic run under `as`, `satisfies` or `new` (`return v as
Foo<Bar>`), a boundary; a `>` pairing with a `<` under any other head compares and continues", or
drop the sentence and point at `_TS_GENERIC_HEADS`, which owns the rule.

**Left-shift.** None that fits; a comment has no gate. The R21 property 3 staging above is the
compensating check and it was run.

## Round 3's four entries, one by one

Each was re-executed at `e6d81f58` by this synthesis unless attributed:

1. **High, the closer-ended line before a silent operator.** CLOSED. All five round-3 shapes —
   `isValid(a) &&` / `isValid(b) ? (`, `getItems(a)` / `.length > 0`, `items[0] ||` / `fallback`,
   the parenthesised `hasPermission(user) &&` chain, `a < b && c >` / `d ? …` — read alike in all
   three R21 spellings at head (property 1 `[]` disagreements, property 2 `[]` crossed), and the
   word-ended ceiling `cond` / `? a` / `: <B />` is lifted with them (R14 re-pinned). A comment
   after the `&&` before the line break still continues (`return isValid(a) && // note` / `isValid(b) ? <B /> : null` → `[('A', 1)]`). Entry 2 here is the mirror direction this channel
   does not cover.
2. **Medium, the `(` branch walking into a later block.** CLOSED for the `<`/`>` half, R23's
   four members and the module-level `<`-direction fixture; the below-zero half is the code fix
   without its arm — entry 1 here. The method-annotation probes the claims list named hold:
   `render(): Promise<Foo> {`, `f<T>(x: T): T {` as a member, and an arrow function type in a
   member value each leave the enclosing component routed and the method not.
3. **Medium, the forward reader without the generic close.** CLOSED. R24's three arms hold;
   `x as unknown as Foo<T>`, `foo.bar as Baz<Q>` and `new Foo<T>()` before an element line all
   leave the hook unrouted, and `new Foo<T>()` with its `>` mid-line inside a return value reads
   as passed, not returned. The fourth head no arm names is entry 4.
4. **Low, the helper pairing `>` with any earlier `<`.** CLOSED for the head-less prefix, R21
   property 3, seen red by this synthesis under the any-word staging; OPEN across a statement
   boundary when an `as` sits anywhere in the walk — entry 3 here.

## The claims, one by one

1. **`pend` is cleared at every token-less operand end and set at every silent operator.** HOLDS
   for every operand and operator the claims list named — a comment between an operator and the
   next line, a `${}` substitution, a JSX expression container, `!`, `++`, `typeof x`, a numeric
   literal, `=>` — each probed at head and each giving the right verdict. REFUTED for a byte that
   is neither: non-ASCII whitespace is consumed by the operator catch-all, entry 5.
2. **`conts` is consulted only at depth 0 and cannot hide a real boundary except after a silent
   operator.** HOLDS as attacked; no lens constructed the case. The boundary it CANNOT see is the
   opposite one, a silent operand ending the earlier line, entry 2.
3. **The `<`-as-run cannot refuse a legitimate method; the below-zero refusal cannot refuse a
   legitimate body.** HOLDS on the four probes above and on the 115 fixtures. What is refuted is
   the sentence beside it: the refusal is not pinned, entry 1.
4. **`check_ts_generic_close` with the three heads cannot misread the named probes, and `>` at
   line end is all that matters.** HOLDS for the probes; REFUTED for the walk's reach — an `as`
   two statements earlier is a head, entry 3 — and for the head set's completeness — an
   instantiation expression is a fourth, entry 4.
5. **R21's third property is non-vacuous.** HOLDS, staged by this synthesis: with the any-word
   key restored, `_PREFIXED` holds `a >` newline `b ? <B /> : null`; at head it is empty.
6. **Every new arm was seen red under one of eight staged breaks.** HOLDS per ARM and REFUTED
   per LINE: `r4-body-start-counts-angle` reverts both halves of `read_ts_body_start`, so the
   below-zero refusal alone, the `<`-run branch alone and `satisfies` alone each red nothing,
   entry 1. The break names are not in the tree.
7. **1261 of 1265 identical; the four differ only by fabricated call sites.** HOLDS on the
   skeptic's re-measurement (raw id 7), not repeated here.

## Landing recommendation

Land after the fixes, in one commit on this branch, and none of them is a redesign: entry 1 is
three arms, a dead half deleted and a true sentence; entry 5 is one `.isspace()`; entry 6 is one
comment line; entries 3 and 4 are two loop bounds and a stated ceiling with a pinned fixture.
Entry 2 is the one with a design in it, the `lits` channel; it closes a pre-existing class and
the owner may defer it, in which case the two ceiling statements and the R14 label are corrected
and the class takes a backlog row, since a ceiling stated as closed is the only defect this round
is charging. Every new arm goes in red first — entries 2 and 5 are red today with no staging at
all, entry 1's fifth member reds under the two-line deletion this review staged — and the commit
message names the break per LINE. Then `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, the
recorded green this range has owed since round 2 and still does not have.

What is in this record was re-executed and is stated as such; what was not — the adopter-corpus
re-measurement, the full-suite run on the staged copy, the NBSP byte scan, the instantiation-
expression regex — is attributed to the skeptic that made it; and the `.ts` half of the corpus,
`LEXICON.md` and `README.md` remain unattacked as they were in round 3.
