**Serves:** diff-review TOOL-aGradedDialect-4

# aGradedDialect — Tier-2 diff review of the `returns:jsx` selector, round 5

*Node `a`, 2026-09-13, branch `branch/lexicon-body-selector-9e4d71`. Fold review of the round-4
fixes: four primed lens passes over the remediation commit, five skeptic batches prompted to
REFUTE, one synthesis. Every code finding below was re-executed by this synthesis before it was
written here: the worktree's `tools/lexicon/lexicon.py` is blob-identical to `08c71eda`
(`git hash-object` `339b0811` on both sides; the working copy differs by CRLF only), the base
reader was extracted with `git show e6d81f58:tools/lexicon/lexicon.py`, and a third copy carrying
the three fixes this report recommends was built beside them so each verdict is stated base ·
head · fixed. The kit suite was run twice on a frozen `--local` clone at `08c71eda` under a short
TEMP root, redirected to a file and grepped, never tailed: once on the fixed copy, `lexicon
selftest OK — 773 arm(s)`, 115 of 115 conformance records in exact agreement, refusal share 0,
rc 0; once unpatched, the same line (see run integrity). Skeptic measurements this synthesis did
not repeat — the adopter-corpus re-read — are attributed as such where they are used.*

**Reviewed range: `e6d81f587e87c01d716f428e2cb93e954afaff8d...08c71eda7868e2c9f494e01a38fe14538e2b5c73`.**
That is exactly round 4's remediation commit `08c71eda`: `tools/lexicon/lexicon.py` (the `lits`
channel in `scan_ts_tokens` at its three record sites, `:1089` template close, `:1249` string,
`:1264` regex; the `.isspace()` whitespace skip at `:1225`; `read_ts_expr_end` and
`check_ts_returned` taking `lits`; `add_scope`'s literal-valued-arrow refusal at `:1799`;
`check_ts_generic_close`'s two bounds at `:1974-1976` and `:1979-1980`; the `_TS_GENERIC_HEADS`
ceiling comment; the reworded comment in `check_ts_returned`), `tools/lexicon/selftest.py` (R14's
NBSP arm, R21's literal expressions and fourth prefix, R23's two halves alone with the dead half
deleted, R24's `satisfies` / `as unknown as` / ceiling arms, R25; 773 arms), and the `-10` backlog
row's round-4 sentence. The round-4 review record and a one-line spec touch ride in the same range
and were not attacked.

**Round: 5.** Every entry here is a regression the round-4 fold introduced, or a claim the fold
makes about itself. Nothing re-reports a round-4 entry these bytes closed; those are listed as
closed after the findings, with the repro that shows it.

## Verdict: CLEAN WITH FIXES

No blocker, no high, one medium, three low. Round 4's six entries are all closed as stated: the
silent-literal class that round 4 charged as "certified closed and not" is now closed for every
shape round 4 named, the below-zero refusal has its own arm, `satisfies` has its own arm, the NBSP
byte is a statement, the instantiation ceiling is stated and pinned, the stale comment is gone,
and the suite is green at 773 with the conformance corpus at 115 of 115. What is wrong is that two
of the six fixes were written wider than the defect they close, and each widening is a regression
against `e6d81f58` on valid TypeScript.

The medium is `check_ts_generic_close`'s new search bound. Round 4's entry 3 asked for a stop at a
statement boundary so an `as` two statements up could not make a comparison `>` a boundary; the
fold stops on ANY `;` and ANY `_TS_EXPR_WORDS` word met while walking back from the `>`, and that
walk passes THROUGH the type-argument run before it reaches the `<`. `void`, `typeof`, `new`,
`in` and `extends` are legal inside such a run and a `;` separates the members of an object type
inside one, so `return v as Promise<void>` at a line end — the everyday spelling — is now read as
a comparison, continues into the next line, and hands a semicolon-free hook the next statement's
element: a false red at an adopter's bar with no waiver path. Reproduced on eleven shapes in both
readers, all `[]` at base; the `Foo<Bar>` control is `[]` on both. It is medium and not high
because it reaches semicolon-free `.tsx` only — with a `;` after the `>` the line-end token is
the `;` and the bound is never consulted — and because the adopter corpus carries no instance;
round 3's high was on prettier's default output, and this is not.

The three lows are one missing fact and one over-broad test. `lits` records the INDEX after a
silent literal and not the line the literal ENDED on, so every reader infers "the earlier line
closed with a literal" from a line break between two token indexes, and that break can sit inside
a multi-line template or before a literal that opens the later line; and `add_scope`'s refusal is
keyed on `body in lits` alone, so it also fires on a `{` body handed back by `read_ts_body_start`
when the return type before it ends in a string-literal type on an earlier line. Each drops a real
component from the routed set, silently, on a rare shape. The fourth low is the §7 companion to
the medium: R24 pins only bare-word runs, so the over-reach was invisible to all 773 arms, and the
bound's two clauses are staged as one break.

None of the four changes a verdict on the measured adopter corpus, which is why this is CLEAN WITH
FIXES and not BLOCKED; all four are owed before the `check_ts_generic_close` comment's invariant,
the backlog row's "stops at a `;` or a statement keyword", and the R25 comment's "where a literal
ended" are true as written, which is why it is not CLEAN.

### Review shape

Raw 9, confirmed 9, refuted 0, unverified 0. Precision 1.00.

Nothing was refuted and nothing is outstanding. The nine confirmed findings consolidate into the
four entries below. Each folded entry names the raw ids it absorbs:

- Entry 1 absorbs raw ids 1, 4, 6 and 7 — four lenses, one loop at `lexicon.py:1974-1976`, the
  same eleven repros between them, and one of the four (raw id 6) reaching the head walk at
  `:1979-1980` too.
- Entry 2 absorbs raw ids 2 and 5 — three readers, one fact the lexer does not hand over.
- Entry 3 absorbs raw ids 3 and 9 — one condition at `:1799`, two spellings of the same shape.
- Entry 4 is raw id 8.

Severity on each entry is this report's adjudication over the merged evidence. Raw ids 1, 4, 6
and 7 arrived medium, medium, medium and medium; folded at medium. Raw ids 2 and 5 arrived low and
low; folded at low. Raw ids 3 and 9 arrived low and low; folded at low. Raw id 8 arrived low and
stands at low. No severity was raised or lowered against a skeptic's verdict. Blockers 0, highs 0.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts
demoted to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline.
Nothing was lost, so the zero counts here are evidence rather than a gap: the unverified set is
genuinely empty and every lens finding reached a skeptic. The finding set is COMPLETE for the
lenses that ran.

Three measurements this review made itself. The kit suite at the head sha, unpatched, on a frozen
clone: `lexicon selftest OK — 773 arm(s)`, 115 of 115, refusal share 0, rc 0, read from a file.
The same suite on the fixed copy: the same line, 773, 115 of 115, rc 0 — the three fixes below
red no existing arm. Both are review-time verdicts and not the recorded one: the newest
`lexicon_selftest.log` in this worktree's git dir is still the 04:09 one from the 11th at 755
arms, which is `7b54230e`, three folds ago, and the gate ledger's `lexicon selftest` row names a
tree fingerprint from that run. The kit DoD owes a recorded `GATE_SELFTESTS=1` green for this range
and there is still none to cite. And the claims list's twelve staged-break names —
`r5-string-not-in-lits`, `r5-regex-not-in-lits`, `r5-template-not-in-lits`,
`r5-add-scope-ignores-lits`, `r5-forward-ignores-lits`, `r5-backward-ignores-lits`,
`r5-generic-search-unbounded`, `r5-generic-head-walk-unbounded`, `r5-not-isspace`,
`r5-below-zero-gone`, `r5-angle-run-as-pass`, `r5-satisfies-not-a-head` — appear nowhere in the
tree: `git grep r5-` on `08c71eda` is empty, the commit message says "twelve breaks, twelve names"
and names none, and the backlog row says "twelve staged breaks, one per line of the fix". Round 4
raised the same gap for its eight names. "Every new arm seen red" is therefore carried by the
commit message alone, and entry 4 is what that costs this round: a bound staged as one deletion of
two clauses, where one clause alone reds nothing.

The adopter-corpus statement — 1261 of 1265 identical, routed 946, pinned 87, unchanged from the
2026-09-13 read — was re-measured by the skeptic on raw id 6, who reports the adopter tree's `.tsx`
files byte-identical under base, head and the fix below, and by the skeptics on raw ids 5 and 7,
who grepped it for a line-ending run holding a type operator (0 hits) and for a `=>`-then-newline
literal (9 sites, all whole-value templates). It is consistent with the code. This synthesis did
not repeat those measurements, and notes that the skeptic's file count (1477 `.tsx`) is the whole
tree where the row's 1265 is the marker-bearing population; the two are not in conflict.

## The findings, severity-ranked

### 1 — MEDIUM · `check_ts_generic_close`'s new bounds fire INSIDE the type-argument run, so `as Promise<void>` at line end is a comparison again

**Where.** `tools/lexicon/lexicon.py:1974-1976`, the round-4 stop in the backward `<` search:
`if (toks[i][0] == "op" and toks[i][1] == ";") or (toks[i][0] == "word" and toks[i][1] in
_TS_EXPR_WORDS): return False`; `:1979-1980`, the head walk's new `and toks[p][1] not in
_TS_EXPR_WORDS`; `:1971-1973`, the comment stating "No type-argument run holds a `;` or a
statement keyword"; `memory/backlog/TOOL.md:235`, the row's "`check_ts_generic_close` stops at a
`;` or a statement keyword".

**What.** Round 4's entry 3 was that the search walked back across a `return`, so an `as`
anywhere earlier could pair a comparison `>` with its `<`. The fix stops on a statement word — but
it tests every token walked, and the walk visits the whole run BEFORE it reaches the `<` whose
balanced run ends at `j`. `_TS_EXPR_WORDS` (`:816`) holds `typeof`, `in`, `new`, `void` and
`extends`, every one of which is legal inside a type-argument run (`Promise<void>`,
`ReturnType<typeof f>`, `Foo<new () => T>`, `Foo<{ [K in keyof T]: X }>`, `Foo<T extends U ? A :
B>`), and a `;` separates the members of an object type inside one (`Record<string, { a: string;
b: number }>`). On any of those the search returns False before the `<` is tested, the line-end
`>` reads as a comparison, and both readers continue into the next line. The `;` half is also
redundant where it is right: `read_ts_angle_end` (`:1376`) already returns None on a `;` at
bracket depth zero, so the only `;` the backward search can reach that the angle walk would
accept is one inside a bracket group — a type-literal member — where stopping is the wrong
answer. The head walk's stop has the same shape one level down: `v as typeof makeBox<string>`
(a TS 4.7 type query with type arguments) walks `makeBox` → `typeof` and stops on a word that is
not a head, where base walked on to the `as`.

**Reproduced.** Base then head then fixed, `read_ts_jsx_defs`. Block reader, the hook `function
useX(v) {` / `  if (!v) return <tail>` / `  const el = <A />` / `  return el` / `}`:

- `v as Foo<Bar>` (control) — `[]` · `[]` · `[]`.
- `v as Promise<void>` — `[]` · `[('useX', 1)]` · `[]`.
- `v as ReturnType<typeof setTimeout>` — `[]` · `[('useX', 1)]` · `[]`.
- `v as Foo<typeof bar>`, `v satisfies Foo<typeof x>`, `m as jest.Mocked<typeof fetch>` — each
  `[]` · `[('useX', 1)]` · `[]`.
- `v as Record<string, { a: string; b: number }>` — `[]` · `[('useX', 1)]` · `[]`.
- `new Map<string, () => void>`, `v as Foo<new () => T>` — each `[]` · `[('useX', 1)]` · `[]`.
- `v as Foo<{ [K in keyof T]: T[K] }>`, `v as Foo<T extends X ? A : B>` — each `[]` ·
  `[('useX', 1)]` · `[]`.
- `v as typeof makeBox<string>` — `[]` · `[('useX', 1)]` · `[]` (the head-walk half).

Forward reader: `const getP = () => run() as Promise<void>` / `const el = <A />` — `[]` ·
`[('getP', 1)]` · `[]`; `const pick = (v) => v as ReturnType<typeof setTimeout>` / `const el = <A
/>` — `[]` · `[('pick', 1)]` · `[]`. And the two-verdict shape: `function Panel() {` / `  const
getRef = () => ref as Promise<void>` / `  return <div ref={getRef()} />` / `}` — `[('Panel', 1)]`
· `[('getRef', 2)]` · `[('Panel', 1)]`, the component lost and the helper routed.

The shape the bound protects still holds on the fixed copy: R21's fourth prefix, `const n = v as
Foo < h` / `return a >` / `  b ? <B /> : null` — `[]` · `[('A', 1)]` · `[('A', 1)]`; and the
ceiling stays a ceiling, `return makeBox<string>` — `[('useBox', 1)]` on all three.

**Why MEDIUM.** A regression the diff introduced, on valid and everyday TypeScript, in both
readers, that routes a camelCase hook into the PascalCase `returns:jsx` cell and reds a correct
name with no waiver path (`WAIVER_FILES` holds `verb` and `suffix`), or drops a component whose
helper ends so. It reaches semicolon-free `.tsx` only — with a `;` after the `>` the line-end
token is the `;` and the bound is never consulted — and the adopter corpus carries no line-ending
run holding one of these tokens (skeptic, raw id 6, 0 hits), so no measured verdict moves. Round
3's high was a wrong grade on prettier's DEFAULT output; this needs `semi: false`. Medium, as all
four lenses rated it.

**Fix.** One constant and three lines, verified on the fixed copy (773 arms green, 115 of 115,
every repro above back to its base verdict):

- Beside `_TS_GENERIC_HEADS`: `_TS_STMT_WORDS = _TS_EXPR_WORDS - frozenset(("typeof", "void",
  "new", "in", "extends"))` — the words a type-argument run cannot hold. `return`, `throw`,
  `case`, `else`, `do`, `yield`, `await`, `delete`, `instanceof`, `of` stay.
- `:1974-1976` becomes `if toks[i][0] == "word" and toks[i][1] in _TS_STMT_WORDS: return False`
  — the `;` clause is dropped, since `read_ts_angle_end` already refuses a depth-0 `;` and the
  other `;` is a type-literal member.
- `:1980` becomes `and toks[p][1] not in _TS_STMT_WORDS`, so `typeof` in a type query keeps its
  `as` head while `return makeBox<string>` still stops on `return`.
- Rewrite the `:1971-1973` comment: the bound is the statement words a TYPE cannot carry, named by
  the constant, and the `;` case belongs to `read_ts_angle_end`. Correct the backlog row's phrase
  in the round-5 sentence it will gain.

**Left-shift.** Entry 4 is the gate: three tails in R24's `_TAILS`, each RED on head today with no
staging at all, and the two clauses staged as separate breaks. The class one level up — a bound
added to a walk that has not yet found its target, tested against tokens the target legitimately
contains — is the §10 "predicate that never matched its target population" shape and is what
R24's bare-word tails could not see.

### 2 — LOW · `lits` carries the index after a literal and not the line it ended on, so a literal that spans the break or opens the later line reads as the earlier line's close

**Where.** `tools/lexicon/lexicon.py:1089`, `:1249`, `:1264`, the three `lits.add(len(toks))`
record sites; `:985`, the `scan_ts_tokens` docstring ("the INDEX the next token takes"); the three
readers — `:1601` (`j in lits`, `read_ts_expr_end`), `:2029` (`(j + 1) in lits`,
`check_ts_returned`), `:1799` (`body in lits`, `add_scope`) — each pairing that index test with
`toks[idx][2] > toks[idx - 1][2]`; `selftest.py:2920`, the R25 comment's "`lits` is the lexer's
record of where a literal ended".

**What.** The lexer records that a silent literal ended immediately before token `idx`. The
readers need a different fact — that the literal ended on a line EARLIER than token `idx`'s — and
derive it from the line break between `idx - 1` and `idx`. That break is not the literal's: a
template can open on the earlier line and close on the later one, and a string can open the later
line after a token that ended the earlier one. In both, `idx in lits` is true, the two token lines
differ, and every reader concludes the earlier line closed with a literal. The forward reader
then ends the expression at `idx`, the backward reader breaks at `idx - 1` before it reaches
`return`, and `add_scope` refuses the arrow's scope. The word operators are what expose it: a
symbolic operator after the literal sets `pend`, so `conts` rescues the line, which is why
`/x/.test(v) ? <B /> : null` on the next line still routes and `'debug' in window ? <B /> :
null` does not — `in`, `instanceof`, `as` and `satisfies` emit no `pend`.

**Reproduced.** Base then head then fixed:

- ``const A = () => ` `` / ``x` === y ? <B /> : null`` (a template spanning the break) —
  `[('A', 1)]` · `[]` · `[('A', 1)]`; the single-line template routes on all three.
- `function Foo() {` / `  return (` / `    'a' in x ? <A /> : null` / `  )` / `}` — `[('Foo', 1)]`
  · `[]` · `[('Foo', 1)]`; the same on one line routes on all three. `'key' in obj ? <A /> : <B
  />` inside prettier's `return (` wrapping is the realistic spelling.
- `const A = () =>` / `  'debug' in window ? <B /> : null` — `[('A', 1)]` · `[]` · `[('A', 1)]`;
  the `/x/.test(v)` control routes on all three; and the round-4 target `const f = () =>` /
  `  'x'` / `const el = <A />` stays `[]` on head and fixed.

**Why LOW.** Each is a component silently dropped from the routed set — a false green in the
`returns:jsx` cell, never a false red — on a shape that needs a silent literal at a line break
followed by a word operator, and the adopter corpus has no instance (skeptic, raw id 5: 9
`=>`-newline-literal sites, all whole-value templates). Regression from this diff, no ceiling
names it, and `'ontouchstart' in window ? <Touch /> : <Mouse />` is a real idiom.

**Fix.** Carry the line, verified on the fixed copy: `lits` becomes a dict at the three record
sites, `lits[len(toks)] = line` (the lexer's `line` is the literal's END line, since each site
runs after `line += src.count("\n", …)`), `lits: dict = {}` in `parse_ts_source`, and each reader
compares against it — forward `(j in lits and lits[j] < ln)`, backward `((j + 1) in lits and
lits[j + 1] < toks[j + 1][2])`, `add_scope` `lits[body] < toks[body][2]` (with entry 3's guard).
Every `in` test stays as written; the three R25 arms, R21's three literal expressions and R14's
string arm keep their head verdicts.

**Left-shift.** Pin the three shapes above as R25 arms at the base verdict, beside the round-4
target at ITS verdict, and stage the break by reverting the readers to the index-only test
(`lits.get(j, 0) < ln` → `j in lits`). Correct the R25 comment: the record is where a literal
ended, once it carries the line.

### 3 — LOW · `add_scope`'s literal-valued-arrow refusal runs on every body, including a `{` after a return type that ends in a literal type

**Where.** `tools/lexicon/lexicon.py:1799`, `if body in lits and body not in conts and body and
toks[body][2] > toks[body - 1][2]: return`; `:1800-1803`, the comment scoping it to "the arrow's
value was a silent literal"; the two callers that hand it a `{` from `read_ts_body_start`, the
declaration arm and the method arm at `:1855`.

**What.** The refusal was written for `read_ts_arrow_body` handing back the NEXT statement's
first token after a literal-valued arrow, and its comment says so. It keys on `body in lits` and a
line break, which a block body also satisfies whenever the token before its `{` is a silent
string-literal type on an earlier line: `|` is never emitted by the lexer (catch-all, `:1343`), so
`function Badge(x: number):` / `  | 'primary'` / `  | 'secondary' {` tokenizes as `… ) : {` with
the `{` in `lits` and on a later line than the `:`. All four clauses hold, `add_scope` returns
before its `{` branch at `:1804`, and a real block scope is dropped: the component's element
belongs to nobody and the name is graded in the plain `tsx.function` cell, refused for being
PascalCase. `read_ts_body_start`'s `{` is by construction the real body, so the next-statement
rationale cannot apply to it. The method arm reaches it too: `render(): 'a' | 'b' {` loses its
absorbing scope and leaks its element to the enclosing declared function.

**Reproduced.** Base then head then fixed:

- `function Foo(): JSX.Element | 'x'` / `{` / `  return <A />` / `}` — `[('Foo', 1)]` · `[]` ·
  `[('Foo', 1)]`; with `'x' | JSX.Element` (the literal not last) `[('Foo', 1)]` on all three,
  which is the tell that the refusal reads token adjacency, not arrow shape.
- `function Badge(x: number):` / `  | 'primary'` / `  | 'secondary' {` / `  return <A />` / `}`
  — `[('Badge', 1)]` · `[]` · `[('Badge', 1)]`; the same-line union routes on all three.

**Why LOW.** A silent false negative on a rare shape — Allman braces after a trailing literal
type, or a prettier-wrapped return-type union ending in a string literal (`(): | ReactElement |
'n/a' {` is valid, since `ReactNode` admits strings) — with no adopter-corpus verdict moved. Real,
introduced by this diff, and the condition is broader than its comment.

**Fix.** Restrict the refusal to what the comment describes: add `and toks[body - 1][1] == "=>"`
to `:1799`. Every value read by `read_ts_arrow_body` sits directly after `=>` (a comment between
them is not a token), and a `{` from `read_ts_body_start` never does. Verified on the fixed copy:
both shapes route again, `const f = () => 'x'` / `{ const el = <A /> }` still refuses, all R25 arms
hold.

**Left-shift.** Pin the Allman and the wrapped-union shapes beside R25 at the base verdict, and
stage the break by removing the `=>` clause alone.

### 4 — LOW · R24 pins only bare-word runs, so entry 1 was invisible to all 773 arms, and the bound's two clauses are one break

**Where.** `tools/lexicon/selftest.py:2904`, `_TAILS = {"satisfies": "v satisfies Foo<Bar>",
"as-unknown-as": "v as unknown as Foo<Bar>"}`; the other R24 arms at `:2891-2915`, `Foo<Bar>`,
`RefObject<HTMLDivElement>`, `new Map<string, Foo>`, `makeBox<string>`; the claims list's
`r5-generic-search-unbounded`, which stages both clauses of `:1974-1976` as one deletion.

**What.** Every pinned run holds one bare word between its `<` and `>`. No arm places a type
operator or a type literal inside a line-end run under `as`, `satisfies` or `new`, and no arm calls
`check_ts_generic_close` or `read_ts_angle_end` directly; `ts-conformance-fixtures.json` holds
`ReturnType<typeof setTimeout>` only as a `;`-terminated annotation in a `.ts` record, off this
path. So the round-4 bound was landed against the one type-argument shape that cannot trip it, and
head passes 773 of 773 while regressing eleven. The staging has the same gap one level down: the
`;` clause and the keyword clause are deleted together, and the R21 fourth-prefix arm reds under
that because the KEYWORD clause is what it needs (with only the `;` clause present the walk
reaches the `<` after `Foo` and pairs it); the `;` clause alone has no arm that reds when it is
removed, in either direction, and entry 1 shows it can only be shown harmful.

**Reproduced.** Head suite unpatched, this synthesis: `lexicon selftest OK — 773 arm(s)`, while
the eleven entry-1 shapes reproduce wrong on the same bytes. The three tails below, added to
`_TAILS` on the head copy, each route `useX` and would red the `_LEAK2` arm with no staging at
all; on the fixed copy each is `[]`.

**Why LOW.** No wrong verdict of its own; it is the §7 "gate the class, not the instance" entry
whose cost entry 1 already carries.

**Fix.** Three tails: `"as-void": "v as Promise<void>"`, `"as-typeof": "v as ReturnType<typeof
f>"`, `"as-type-literal": "v as Foo<{ a: string; b: number }>"`, and a `new Map<string, () =>
void>` arm beside the `new Map<string, Foo>` one. Stage the keyword clause and the `;` clause as
two breaks: widening `_TS_STMT_WORDS` back to `_TS_EXPR_WORDS` reds the three tails, and there is
no `;` clause left to stage once entry 1 lands, which is the point — a clause that cannot be
shown to guard anything is deleted, not pinned.

**Left-shift.** The tails are the gate. The class above them — a fix pinned only on the shape
that motivated it — is the round-4 entry 1 class again, and this is the second round in which the
break names that would let a reviewer check "seen red" per line are not in the tree; put the
twelve names in the commit message or beside the arms.

## Round 4's six entries, one by one

Each was re-executed at `08c71eda` by this synthesis unless attributed:

1. **Medium, the below-zero refusal pinned by no arm.** CLOSED as a pin. R23 now carries a call
   inside an array member that unbalances the walk below zero (`:2880`) and a method returning
   `Promise<{ a: string }>` scoping on its brace (`:2887`), and R24 carries `satisfies` alone; the
   R23 dead half is gone. This synthesis did not re-stage `r5-below-zero-gone` or
   `r5-angle-run-as-pass`; the names are not in the tree (run integrity).
2. **Medium, a token-less operand at line end.** CLOSED for every shape round 4 named: `open ?
   'Open' : 'Closed'`, `state.value = ''`, `` `k-${i}` ``, `/x/` as helper values inside `Panel`
   and at module level, `return 'none'` and `return a ? b : 'none'` as early returns, `'x' +`
   continuing, all at head as R25 pins them and re-run here. What the `lits` channel records is
   one fact short — entries 2 and 3 are its edges.
3. **Low, the walk across a `return`.** CLOSED for its target — R21's fourth prefix routes `A` at
   head and did not at base — and OVER-CLOSED: entry 1.
4. **Low, the instantiation-expression ceiling.** CLOSED: stated beside `_TS_GENERIC_HEADS`,
   pinned in R24 at `[('useBox', 1)]`, re-run here on all three copies.
5. **Low, non-ASCII whitespace.** CLOSED: `.isspace()` at `:1225`, the R14 NBSP arm, and the
   hook `if (!o) return noop()` / NBSP `const el = <A />` — `[('useX', 1)]` at base, `[]` at
   head.
6. **Low, the stale any-word comment.** CLOSED: `:2020-2023` now names the three heads.

## The claims, one by one

1. **`lits` is recorded at every token-less literal end — string, template close, regex — and
   nowhere else.** HOLDS: three sites, `:1089`, `:1249`, `:1264`, each under `not suppress`, and
   no other writer. What is REFUTED is the fact recorded: an index, no line — entry 2.
2. **A literal inside a suppressed span records nothing and the outer close records once.**
   HOLDS: `` const k = () => `${'a'}` `` / `const el = <A />` is `[]` at head (`[('k', 1)]` at
   base, the round-4 defect), and `return <div title={'a'} />` routes its component on all three.
3. **The forward `j in lits` clause cannot end a legitimate expression after `'x' +`, before a
   `:`- or `,`-opening line, or when an emitted token followed the literal on the same line.**
   HOLDS for each: `'x' +` / `(cond && <B />)` routes, `cond ? 'a'` / `: <B />` routes,
   `'x'.length > 0` / `? <B /> : null` routes, `'x'.length` / `const el = <A />` is `[]`, all
   three copies. REFUTED for a literal that spans the break — entry 2.
4. **The backward `(j + 1) in lits` clause likewise.** HOLDS for the same shapes in a block body;
   REFUTED for a literal opening the line after `return (` — entry 2.
5. **`add_scope`'s refusal cannot drop the scope of an arrow whose body legitimately starts on
   the next line after a literal on the arrow line.** HOLDS for the construction asked for:
   `const f = () => // note` / `  'x'` / `const el = <A />` is `[]` at head and `[('f', 1)]` at
   base, and `[]` is right — the body is the literal, the scope it would open is empty, and the
   module-level element is nobody's. REFUTED for a body that OPENS with a literal followed by a
   word operator — entry 2 — and for a `{` body after a literal type — entry 3.
6. **`check_ts_generic_close`'s bounds cannot refuse a legitimate `return v as Foo<Bar>`.** HOLDS
   for `Foo<Bar>`; REFUTED for any run holding `void`, `typeof`, `new`, `in`, `extends` or a
   type-literal `;` — entry 1.
7. **The head walk stopping at `_TS_EXPR_WORDS` cannot break `as unknown as Foo<T>` or `x
   satisfies Foo<T>`.** HOLDS for both, `[]` on all three copies; REFUTED for `as typeof
   makeBox<string>` — entry 1's head-walk half.
8. **`.isspace()` cannot swallow a `\n` nor change line counting.** HOLDS: the `\n` branch at
   `:1221` precedes it, and `const A = () => <B />` / NBSP `const C = () => <D />` is `[('A', 1),
   ('C', 2)]` on all three copies.
9. **Every new arm was seen red under one of twelve staged breaks.** CANNOT BE CHECKED BY NAME:
   none of the twelve is in the tree or the commit message. HOLDS per ARM as far as the arms
   this synthesis re-derived go; REFUTED per CLAUSE for `r5-generic-search-unbounded` — entry 4.
10. **The adopter-corpus statement is consistent with the code.** HOLDS on the skeptics'
    re-measurements (raw ids 5, 6, 7), not repeated here.

## Landing recommendation

Land after the fixes, in one commit on this branch, and none of them is a redesign: entry 1 is one
constant, two line edits, one deletion and a comment; entry 2 is the `lits` dict, three record
sites and three comparisons; entry 3 is one `=>` clause; entry 4 is three tails and one arm. All
three code fixes were applied together on a copy and the suite is green at 773 with 115 of 115,
so they do not fight. Every new arm goes in red first — the three R24 tails, the three R25 shapes
and the two Allman shapes are red today with no staging at all — and the commit message names the
break per LINE this time, since the previous two did not and each cost a round. Then
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, the recorded green this range has owed since
round 2 and still does not have.

What is in this record was re-executed and is stated as such; what was not — the adopter-corpus
re-read, the `=>`-newline census, the per-name staging of the twelve breaks — is attributed to the
skeptic that made it or named as unchecked; and the `.ts` half of the corpus, `LEXICON.md` and
`README.md` remain unattacked as they were in rounds 3 and 4.
