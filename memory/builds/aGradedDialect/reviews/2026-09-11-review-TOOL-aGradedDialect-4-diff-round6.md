**Serves:** diff-review TOOL-aGradedDialect-4

# aGradedDialect — Tier-2 diff review of the `returns:jsx` selector, round 6

*Node `a`, 2026-09-13, branch `branch/lexicon-body-selector-9e4d71`. Fold review of the round-5
fixes: four primed lens passes over the remediation commit and its map regeneration, five skeptic
batches prompted to REFUTE, one synthesis. Every code verdict below was re-executed by this
synthesis before it was written here, on three copies of `tools/lexicon/lexicon.py` extracted with
`git show` — the base `08c71eda`, the reviewed head `7afdc134`, and the branch tip `3106058d`,
which is one commit PAST the reviewed range and is where entry 1 is already closed — plus a fourth
copy of the tip carrying entry 2's fix. The kit suite was run twice on scratch copies of
`tools/lexicon/` under a short TEMP root, redirected to a file and grepped, never tailed: once on
the fixed copy of the tip, `3 of 774 arm(s)` red and all three are AC6's `not a git repo` (the
scratch copy's environment, not the code), 115 of 115 conformance records in exact agreement; once
on `7afdc134` with the regex branch's continuation mark staged OUT, the same three AC6 reds of 773
and nothing else — the staging entry 3 rests on. The measurements this synthesis did not repeat —
the skeptics' staged runs at the tip, the string-branch liveness control, the adopter-corpus
re-read — are attributed as such where they are used.*

**Reviewed range: `08c71eda7868e2c9f494e01a38fe14538e2b5c73...7afdc134843431a5adedd15cbaf61d7a781e5156`.**
That is round 5's remediation commit `d0eca6fe` plus the one-file map regeneration `7afdc134`:
`tools/lexicon/lexicon.py` (`_TS_STMT_WORDS` at `:1981` and the two bounds it feeds in
`check_ts_generic_close`, `:1997` and `:2002`; `lits` as a dict of END lines at its three record
sites `:1091`, `:1256`, `:1275` and its three readers `:1613`, `:1812`, `:2051`; `add_scope`'s
refusal keyed on the `=>` before the body; the three literal branches marking a continuation,
`:1248` string, `:1259` template, `:1267` regex), `tools/lexicon/selftest.py` (R24's seven-tail
`_TAILS`, R25's `_DROP` and `_BRACE`; 776 arms), the `-10` backlog row's round-5 sentence, and
`memory/map/generated/symbols.json` (five lines for the new constant and the helper, which two bar
legs redded at `d0eca6fe`). The round-5 review record and a one-line spec touch ride in the same
range and were not attacked. The `GATE_SELFTESTS=1` bar at `7afdc134` is GREEN, 67 of 67 with 39
guarded legs skipped as unchanged vs `main`; this synthesis read that from the worktree git dir's
`gate-last-summary.txt`, which says exactly that, and its `gate-last-failure.txt` is the first bar
at `d0eca6fe` with the two `codebase-map` legs RED, which is the regeneration's stated cause.

**Round: 6.** Every entry here is a regression the round-5 fold introduced, a claim the fold makes
about itself, or a pre-existing edge the round-5 claims list put under attack by name. Nothing
re-reports a round-5 entry these bytes closed; those are listed as closed after the findings, with
the repro that shows it.

## Verdict: CLEAN WITH FIXES

No blocker, one high, one medium, four low. The verdict is on what the branch would land, and it
needs saying plainly that the range AS CUT would not get it: at `7afdc134` alone entry 1 is a HIGH
regression against `08c71eda` on prettier-emittable source — a helper ending in a wrapped string,
template or regex swallows the module-level component after it and is credited with its element —
and that alone would be BLOCKED. It is CLEAN WITH FIXES because `3106058d`, the next commit on this
branch, closes it: every one of the seven shapes reproduced here (three literal kinds in the
arrow reader, the `add_scope` path, the block reader, and the chained `n +` / `'a' +` / `'b'`)
returns `[]` at the tip, and the R25 arm that would have caught it is in the tree with its break
named. Entry 1 is recorded as LANDED, and the one condition this verdict carries is that
`7afdc134` never lands without `3106058d` in the same integration unit.

The medium is `_TS_STMT_WORDS`'s invariant. Round 5 narrowed the generic-close bound from every
expression word to the ten words "a type-argument run can NEVER hold", and that is false for every
one of the ten: TypeScript admits any reserved word as a property key or method name in a type
literal, and `.` is not emitted, so `typeof api.delete` tokenizes as the word pair `api delete`.
`return v as Record<string, { delete: boolean }>` at a line end — the shape of every REST-client
permission map — reads as a comparison, the early return continues into the next statement, and a
hook lands in the component cell as a false red. Three lenses found it by three routes (a key, a
method signature, a `typeof` member), all confirmed, all reproducible at base, head and tip; it is
pre-existing rather than a regression, because base bounded on the wider `_TS_EXPR_WORDS`, but the
round-5 comment and the R24 tails certify it closed and it is not.

The four lows are one gate never seen red, two edges of the `lits` end-line that the round-5 claim
"three readers compare the line" overstates, and one stale docstring paragraph. None of the six
changes a verdict on the measured adopter corpus, which the skeptics report unchanged.

### Review shape

Raw 14, confirmed 10, refuted 4, unverified 0. Precision 0.71.

Nothing is outstanding. The ten confirmed findings consolidate into the six entries below. Each
folded entry names the raw ids it absorbs:

- Entry 1 is raw id 3. The skeptic on it names raw id 2 as its duplicate; raw id 2 is among the
  four refuted and is not re-counted here.
- Entry 2 absorbs raw ids 1, 8 and 12 — one bound at `lexicon.py:1997`, three routes into it (a
  `typeof` member, a method signature, a property key), one fix that covers all three.
- Entry 3 absorbs raw ids 4, 9 and 14 — one unpinned fix line at `:1267`, and the backlog row's
  count that disagrees with its list because of it.
- Entry 4 is raw id 13. Entry 5 is raw id 6. Entry 6 is raw id 10.

Severity on each entry is this report's adjudication over the merged evidence. Raw id 3 arrived
high and stands at high, at the reviewed sha; that it is closed one commit later is its
disposition, not its severity. Raw ids 1, 8 and 12 arrived medium, medium and medium; folded at
medium. Raw ids 4, 9 and 14 arrived low, medium and low; folded at LOW, which lowers raw id 9 by
one step: the mark it guards is live and correct on every shape run here, so the cost is a §7 gap
and a count, not a wrong verdict, which is how round 5 graded the same class (its entry 4). Raw
ids 13, 6 and 10 arrived low and stand at low. Blockers 0, highs 1.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts
demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline.
Nothing was lost, so the zero counts here are evidence rather than a gap: the unverified set is
genuinely empty and every lens finding reached a skeptic. The finding set is COMPLETE for the
lenses that ran.

Measurements this review made itself. The seventeen-shape probe (entry repros and their controls)
on base, head and tip, read through `read_ts_jsx_defs`; the composite bound of entry 2 on a
fourth copy, against the same probe, R24's seven tails, R21's fourth prefix, the instantiation
ceiling, `return a >` / `b`, `return a < b && c >` / `d` and the `as`-two-statements-up shape;
the kit suite on that copy (3 AC6 environment reds of 774, no `returns` arm moved, 115 of 115);
and the kit suite at `7afdc134` with the regex branch's mark deleted (3 AC6 reds of 773, nothing
else). Attributed and not repeated: the skeptics' staged runs of the same deletion at the tip
(same result), the liveness control that deleting the STRING branch's mark reds R25's `_DROP`,
and the adopter-corpus statement.

The recorded green this range cites is real and is the round-5 gap closed: `gate-last-summary.txt`
in this worktree's git dir reads `gates GREEN — 67/67 legs passed (39 skipped)` with the
`selftests` chunk at 19 passed and 33 skipped, and the ledger's `lexicon selftest` row carries a
tree fingerprint. The break names, for the first time in three rounds, are in the tree: six
`r6-*` names in the backlog row at `7afdc134`, seven at the tip. Entry 3 is what is missing from
that list.

## The findings, severity-ranked

### 1 — HIGH · the literal-opens-continuation mark lands on the next EMITTED token whatever line it sits on, so a helper ending in a wrapped literal swallows the module-level statement after it — LANDED at `3106058d`

**Where.** `tools/lexicon/lexicon.py:1248-1249` (string), `:1259-1260` (template),
`:1267-1268` (regex): `if pend and conts is not None and not suppress and toks and line >
toks[-1][2]: conts.add(len(toks))`, in `scan_ts_tokens` at `7afdc134`. The three readers that key
on `conts` before they consult `lits`: `read_ts_expr_end` `:1613`, `add_scope` `:1812`,
`check_ts_returned` `:2051`.

**What.** Round 5 found, while staging, that a literal OPENING a continuation line clears `pend`
before any token can be marked, and handed the mark to the token that follows the literal. It
handed it to `len(toks)` — the index the NEXT EMITTED token will take — with no test of which line
that token is on. `x +` / `'a'` / `const el = <B />` therefore marks `const` on line 3 as a
continuation of line 1. Every reader tests `j not in conts` BEFORE the `lits` end-line comparison,
so the ASI break the end-line was recorded to produce never fires: the forward reader runs the
helper's expression through `const`, `add_scope`'s refusal is bypassed because the body index is
in `conts`, and the block reader's backward walk cannot break at `const` and finds the early
`return`.

**Reproduced.** Base then head then tip, `read_ts_jsx_defs`:

- `const label = (n: number) => n +` / `  ' items'` / `const empty = <Empty />` — `[]` ·
  `[('label', 1)]` · `[]`. The template and the regex spellings of the continuation line: the same
  three verdicts each.
- `const f = () => 'a' +` / `  'b'` / `const el = <B />` — `[]` · `[('f', 1)]` · `[]` (the
  `add_scope` path).
- `function useS(v) {` / `  if (!v) return x +` / `  'a'` / `  const el = <B />` / `  return
  el.props` / `}` — `[]` · `[('useS', 1)]` · `[]` (the block reader).

**Why HIGH.** A regression the diff introduced, on source prettier emits by default — a binary
expression wrapped after its operator when it exceeds the print width, its right operand a string
— that credits a camelCase helper with the next component's element and reds it in the
`tsx.function+returns:jsx` cell with no waiver path. Round 3's high was the same class of grade on
the same kind of output. It is not BLOCKED because it is already closed, and the closing is the
right shape: `3106058d` moves the mark into `add_token` behind `lit_line == line` — the string and
regex branches set `lit_line` at their end line, the template via `tmpl_cont` at its close — so
the mark reaches a token on the literal's OWN line only, and adds the R25 arm for all three
literal kinds with its break named `r6-literal-mark-any-next-token`. The six `r6-*` breaks round 5
staged proved the mark is NEEDED and not that it is SCOPED, which is what the skeptic's
disposition says and this synthesis confirms.

**Fix.** None owed. Recorded as landed, outside the reviewed range.

**Left-shift.** The R25 arm at the tip is the gate. The class one level up — a mark keyed on an
index where the reader will key on a line — is the same shape as round 5's `lits` entry, and
entries 4 and 5 below are its remaining edges.

### 2 — MEDIUM · `_TS_STMT_WORDS` bounds `check_ts_generic_close` on words that CAN sit inside a type-argument run — as a property key, a method name, or a `typeof` member — so `as Record<string, { delete: boolean }>` at line end is a comparison

**Where.** `tools/lexicon/lexicon.py:1976-1981`, the constant and its header, "the expression
words a type-argument run can NEVER hold"; `:1993-1998`, the backward bound `if toks[i][0] ==
"word" and toks[i][1] in _TS_STMT_WORDS: return False` and its comment "No type-argument run
holds a statement keyword"; `:2002`, the head walk's `and toks[p][1] not in _TS_STMT_WORDS`;
`selftest.py:2906-2913`, R24's `_TAILS`, seven runs and none holding a keyword in key position.

**What.** The backward search visits the whole run BEFORE it reaches the `<`, and the bound tests
every token visited. Round 5 removed the five words a run holds as TYPE OPERATORS; the ten that
stay — `return instanceof of delete yield await throw case do else` — are every one a legal
property name, and TypeScript admits any reserved word as a key or method name in a type literal
(`{ delete: boolean }`, `{ of: Date }`, `{ delete(id: string): void }`, `{ return: number }`), and
as the member of a `typeof` query (`ReturnType<typeof api.delete>`). The lexer does not emit `.`,
so the last is the word pair `api delete` in the stream. On any of these the search returns False
before the `<` is tested, the line-end `>` reads as a comparison, both readers continue into the
next line, and the hook takes the next statement's element.

**Reproduced.** Base then head then tip, the hook `function useX(v) {` / `  if (!v) return
<tail>` / `  const el = <A />` / `  return el` / `}`:

- `v as Foo<Bar>` (control) — `[]` · `[]` · `[]`.
- `v as Record<string, { delete: boolean }>` — `[('useX', 1)]` on all three.
- `v as ReturnType<typeof api.delete>` — `[('useX', 1)]` on all three.
- `v as Api<{ delete: () => void }>` — `[('useX', 1)]` on all three; the control `v as Api<{ get:
  () => void }>` is `[('useX', 1)]` · `[]` · `[]` — the `void` inside it was round 5's medium,
  now closed, and the keyword key alone is what still flips it.
- Skeptics, attributed: all 30 of the ten words × `key:`, `key?:`, `key():` route at head;
  `Box<{ of: Date }>`, `Parameters<typeof api.do>`, `Fn<(o: { return: number }) => void>`, the
  arrow form `const useX = (v) => v as ReturnType<typeof api.delete>` / `const el = <A />`, and
  `Client<{ get: Fn; delete: Fn }>` route too.

**Why MEDIUM.** Pre-existing, not a regression — at base the wider bound caught the same words —
but the round-5 header, comment and backlog row certify the invariant and it is false; the shape
is one-line, prettier-emittable, and realistic (`delete` is the HTTP-verb key of every REST client
type); and the verdict is the R24 class round 4 and round 5 both fixed as medium, a hook with an
early return graded as a component. It reaches semicolon-free `.tsx` only, as before, and the
adopter corpus carries no instance (skeptics, unchanged corpus statement). Medium, as all three
lenses rated it.

**Fix.** Two rules in the backward walk, both verified on a copy of the tip: count bracket depth,
and skip a statement word in member position. `)`/`]`/`}` raise `depth`; an opener at depth zero
returns False (nothing inside a group the walk has not entered can pair with this `>`), otherwise
lowers it; `if depth: continue` before the word test, so a key or a method name inside `{ }` and a
parameter inside `( )` are never consulted. Then `toks[i][1] in _TS_STMT_WORDS and not (toks[i -
1][0] == "word" and toks[i - 1][2] == toks[i][2])` — a statement word directly after a word ON THE
SAME LINE is an elided `.` member, never a statement head. The same-line clause is load-bearing:
without it R21's fourth prefix (`v as Foo < h` / `return a >` / `b`) reads `h` NL `return` as a
member and routes nothing — observed on the first cut of the patch, then fixed. On the final copy
the seven `_TAILS` runs, the six keyword shapes above, `Foo<Bar>`, `{ get: () => void }`, R21's
fourth prefix, the `makeBox<string>` ceiling, `return a >` / `b`, `return a < b && c >` / `d` and
the `as`-two-statements-up shape all keep the verdict the suite pins, and the kit suite is green
on the copy but for the three AC6 environment arms. Rewrite the `:1976-1980` header: a run holds
no statement word OUTSIDE a bracket group and outside member position, and name both exceptions.
The head walk at `:2002` needs no change — it walks a dotted name and stops on the first
non-word, so `typeof api.delete` never reaches it with `delete` at the head.

**Left-shift.** Three tails in R24's `_TAILS`: `"delete-key": "v as Record<string, { delete:
boolean }>"`, `"delete-method": "v as Api<{ delete(id: string): void }>"`, `"typeof-member": "v
as ReturnType<typeof api.delete>"`. Each is RED at head today with no staging; stage the
depth-count and the member clause as two breaks (`r7-generic-bound-inside-group`,
`r7-generic-bound-on-member`), since each reds a different tail. The class above them — a bound
that asserts what a population can never hold, tested by a pin of the shapes that motivated it —
is round 5's entry 4 again, one bracket deeper, and the header is where the assertion has to
name its exceptions rather than deny them.

### 3 — LOW · the regex branch's continuation mark has no arm that reds when it is deleted, no named break, and row -10 counts seven names and lists six

**Where.** `tools/lexicon/lexicon.py:1267-1268`, the regex branch's `conts.add(len(toks))` at
`7afdc134` (the `opens_cont` / `lit_line = line` pair at `:1277-1282` on the tip);
`selftest.py:2951-2963`, R25's `_DROP`, holding a string and a template after `&&` and no regex;
`:2938`'s `const re = () => /x/`, which exercises the `lits` record and not the mark;
`memory/backlog/TOOL.md:235`, "776 arms, seven more breaks named per line:" followed by six names
at `7afdc134` (the tip appends a seventh, `r6-literal-mark-any-next-token`, and still names no
regex break); `d0eca6fe`'s message, the same six.

**What.** One of the three fix lines this round added landed without its failing case being
observed. Staged here at `7afdc134`: with `:1267-1268` deleted the kit suite reds 3 of 773 and all
three are AC6's `not a git repo`; no R25 arm moves. Skeptics report the same at the tip with the
`opens_cont` pair deleted, and the liveness control holds — deleting the STRING branch's mark
reds `_DROP` — so the harness can fail and the regex arm is the one it cannot see. The mark is
live and reachable: `const A = () => cond &&` / `  /a/ instanceof RegExp ? <B /> : null` and its
block twin route `A` at head and tip and return `[]` at base, while `/a/.test(x)` self-heals
through the silent `.` marking `test` and cannot tell the arm from its absence — which is why no
realistic row reached it.

**Why LOW.** No wrong verdict: the mark is right on every shape run here. It is the §7 "a new
gate is not landed until its failing case has been observed" entry, stated as a documented check
by this diff's own "one break per fix line" discipline and not met for one line, plus a count in
prose disagreeing with the list beside it. Raw id 9 arrived medium; lowered to low for the reason
in the review shape.

**Fix.** Pin it: add `"&& then a regex line, arrow": "const A = () => cond &&" + _NL + "  /a/
instanceof RegExp ? <B /> : null"` to `_DROP` (a word operator after the regex is the only shape
that reaches the mark), stage it red by deleting the regex branch's `opens_cont` pair, and name
the break `r6-regex-opens-no-continuation`. Then make row -10's count match its list — eight
names, or state which line is unpinned and why.

**Left-shift.** The `_DROP` row is the gate. The class — three sibling branches, two pinned, the
third assumed covered by symmetry — is the round-5 entry-4 class, and the counter to it is
mechanical: one named break per fix LINE, with the name in the tree beside the arm.

### 4 — LOW · a literal that ENDED on j's line but STARTED earlier falls through to `toks[j - 1]`, which sits before the literal on an earlier line, so a word operator after a multi-line template breaks the expression

**Where.** `tools/lexicon/lexicon.py:1613`, `lits.get(j, ln) < ln or toks[j - 1][1] not in
_TS_EXPR_CONTINUES` in `read_ts_expr_end`; `:2051`, the same shape in `check_ts_returned`;
`selftest.py:2952`, R25's "template spanning the break" fixture, `` ` `` / `` x` === y ? <B /> :
null ``.

**What.** `lits` now carries the END line, and for a template that spans the break the end line
EQUALS j's line, so `lits.get(j, ln) < ln` is False and the reader falls to the second clause —
`toks[j - 1]`, the token BEFORE the template, on the earlier line. That line ended INSIDE the
literal, so there is no boundary to judge, and the reader judges one anyway: a word token there
breaks the expression. The pinned fixture passes only because `toks[j - 1]` is `=>`, a member of
`_TS_EXPR_CONTINUES`; the round-5 record's "a template spanning the break is not the earlier
line's close" holds for its fixture and not for the class.

**Reproduced.** Base then head then tip: `` const A = () => cond ? ` `` / `` x` as string : <B />
`` — `[]` · `[]` · `[]`; the ` in y ? <B /> : null` variant the same; the single-line control
`` cond ? `x` as string : <B /> `` — `[('A', 1)]` on all three. The block-reader (`return cond ?
…`) variants drop too (skeptic, attributed).

**Why LOW.** Pre-existing — index-only `lits` broke it too — and a silent false negative on a
rare shape: a multi-line template as the left operand of `as`, `in` or `instanceof` at call depth
zero in a component's value. No adopter verdict moves. But the claim under attack is this diff's
own, and it is overbroad for its word-operator half.

**Fix.** Decide a literal that ended on j's line by its own record and never by the token before
it: `lits[j] < ln if j in lits else toks[j - 1][1] not in _TS_EXPR_CONTINUES` in both readers.
Verified by the skeptic on a copy: the template-then-`as` fixture reds the index-only AND the
`.get` shapes and goes green under it; not repeated here.

**Left-shift.** The template-then-`as` fixture in `_DROP` for both readers, beside the `=== y`
one it currently pins.

### 5 — LOW · the `return` ASI test reads `return` followed on its own line by a multi-line template as a bare `return`, because `lits` carries the END line and the third reader of the spanning-literal fact was never taught it

**Where.** `tools/lexicon/lexicon.py:2074`, `if r is None or toks[r][2] > toks[r - 1][2]` in
`check_ts_returned` (`:2085` on the tip); `read_ts_expr_end`'s docstring, whose stated ceiling
names `(` and `[` opening a line and not this.

**What.** For `return` `` ` `` / `x` / `` `.length > 0 ? <B /> : null `` the stream is
`('word', 'return', 2)`, `('word', 'length', 4)` with `lits = {6: 4}`: the next emitted token is
on the template's CLOSING line, the test compares token lines only, and neither `lits` nor
`conts` could help it, since an end line cannot separate `return \`...` (a value) from `return`
NL `` `...` `` (ASI). The round-5 commit says the end line reached the two readers and
`add_scope`; this is the third reader of the same fact, and the claim under attack — "the `lits`
end-line comparison cannot misread a literal that ends on the same line as the next token but
started earlier" — is exactly the shape.

**Reproduced.** `function A() {` / `` return ` `` / `x` / `` `.length > 0 ? <B /> : null `` / `}`
— `[]` on base, head and tip; the single-line template control `[('A', 1)]` on all three.

**Why LOW.** Pre-existing, a shape prettier does not emit, a silent drop of a component (graded
under the camel helper cell as a false offender). Real, and unstated.

**Fix.** Either record the START line beside the end (`lits[idx] = (start, end)`) and let this
test accept `r` when a literal in `lits` started on the `return`'s line — the same channel, one
more field — or state the ceiling in `check_ts_returned`'s header and pin the current verdict as
R24 does for the instantiation expression. The second is one comment and one arm and is the lazy
answer that holds; the first is owed only if a corpus ever carries the shape.

**Left-shift.** Whichever is chosen, an arm pins it: `[]` as a stated ceiling, or `[('A', 1)]`
under the start line.

### 6 — LOW · the `conts` paragraph of `scan_ts_tokens`'s header still defines the set as tokens that OPEN a line after a silent operator, and since round 5 it also holds the token AFTER a line-opening literal

**Where.** `tools/lexicon/lexicon.py:975-983`, byte-unchanged since round 4; the `lits` paragraph
at `:985-990` and the inline comment at `:1245-1247` were updated instead.

**What.** For `cond &&` / `'a' in x` the round-5 mark puts `in` in `conts`, and `in` opens
nothing — the last thing consumed before it was the string, not an operator. A reader of the
header alone predicts the marks wrong, and the `lits` paragraph attributes the case to `lits` when
it is `conts` that suppresses the break (`lits.get(j, ln) < ln` is False for a same-line literal,
and `cond` is not in `_TS_EXPR_CONTINUES`). The tip's `lit_line` restriction — same line only —
is also unstated there.

**Why LOW.** Doc only; three readers and `add_scope` key on the set.

**Fix.** One sentence in the `conts` paragraph: a silent literal that opens such a line hands the
mark to the first token emitted on the literal's closing line, and to nothing on a later one.

**Left-shift.** None that fits; a docstring is a documented check by construction.

## Round 5's four entries, one by one

Each was re-executed at `7afdc134` by this synthesis unless attributed:

1. **Medium, the bounds firing inside a type-argument run.** CLOSED for every shape round 5
   named: `Promise<void>`, `ReturnType<typeof f>`, `Record<string, { a: string; b: number }>`,
   `new Map<string, () => void>`, `typeof makeBox<string>` are the seven `_TAILS` runs and each
   is `[]` at head; the `{ get: () => void }` control that routed at base is `[]` at head. OVER-
   CERTIFIED: the header says NEVER and entry 2 is the exception.
2. **Low, `lits` carrying an index and not a line.** CLOSED for its three fixtures (the template
   spanning the break before `===`, `'a' in x` after `return (`, `=>` NL `'debug' in window`),
   each `[('A', 1)]` at head. Two edges remain, entries 4 and 5, and the fix for its staging
   companion was the regression of entry 1.
3. **Low, `add_scope`'s refusal on a `{` body.** CLOSED: the Allman brace and the wrapped union
   route at head (R25's `_BRACE`), and `const f = () =>` / `'x'` / `const el = <A />` still
   refuses.
4. **Low, R24 pinning bare-word runs only, the two clauses one break.** CLOSED as a pin — seven
   tails, the `;` clause gone — and the break names are in the tree for the first time. Entry 3
   is the same class on this round's own new line.

## The claims, one by one

1. **`_TS_STMT_WORDS` can never appear inside a type-argument run (`Awaited<T>` is not
   `await`).** REFUTED — entry 2. `Awaited<T>` indeed is not `await`; `{ await(): void }`,
   `{ delete: boolean }` and `typeof api.delete` are the words themselves, in key, method and
   member position.
2. **Dropping the `;` search clause cannot let `const small = w < h;` NL `return a >` pair,
   because `read_ts_angle_end` refuses the depth-0 `;`.** HOLDS: the walk from `>` reaches
   `return` first and stops on it; and with the `;` it would stop there too. Not reproducible as
   a wrong verdict on any copy.
3. **The `lits` end-line comparison cannot misread a literal that ends on the same line as the
   next token but started earlier.** REFUTED twice — entry 4 (the readers judge `toks[j - 1]`
   across the literal) and entry 5 (the `return` test never consults `lits`).
4. **The `=>` key on `add_scope` cannot miss a literal-valued arrow whose `=>` is followed by a
   comment, a newline, then the literal.** HOLDS: a comment is not a token, `toks[body - 1]` is
   the `=>`, and `const f = () => // note` / `  'x'` / `const el = <A />` is `[]` at head and tip.
5. **The literal-opens-continuation mark cannot mark a token that is NOT a continuation.**
   REFUTED at the reviewed sha, exactly by the construction the claim proposes — `x +` / `'a'` /
   `const el` marks `const` — and CLOSED at `3106058d`: entry 1.
6. **Every new arm was seen red under a named break.** HOLDS for the six named, which are in the
   tree; REFUTED for the regex branch's line, which has no arm and no name: entry 3.
7. **The adopter-corpus statement is consistent.** HOLDS on the skeptics' re-measurements, not
   repeated here.

## Landing recommendation

Land after the fixes, in one commit on this branch, on top of `3106058d` and never without it:
entry 2 is a depth counter, one clause and a header, plus three tails and two breaks; entry 3 is
one `_DROP` row, one break name and one count; entry 4 is one conditional in two readers and one
fixture; entry 5 is one comment and one arm; entry 6 is one sentence. Entry 2's code was applied
on a copy of the tip and the kit suite is green there but for the three AC6 arms that red in any
scratch copy outside a git repo; the other four fixes were not applied by this synthesis and the
verdicts attributed to skeptics are marked as such above. The kit DoD owes a fresh
`GATE_SELFTESTS=1` green at the fold commit; the one at `7afdc134` covers the range and not the
fold.
