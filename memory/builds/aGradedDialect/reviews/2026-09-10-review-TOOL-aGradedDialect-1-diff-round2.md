**Serves:** diff-review TOOL-aGradedDialect-1 TOOL-aGradedDialect-2 TOOL-aGradedDialect-3 TOOL-aGradedDialect-4 TOOL-aGradedDialect-5

# aGradedDialect — Tier-2 diff review of the cumulative landing diff, round 2

*Node `a`, 2026-09-10, branch `branch/lexicon-kit-typescript-34c322`. Adversarial pass over the diff
that lands on `main`: four primed lens passes, five skeptic batches prompted to REFUTE, one
synthesis. Every finding below was re-executed at source in this worktree before it was written
here, and every regression claim was re-executed against the base reader as well.*

**Reviewed range: `5f1815af3411b055341746ab0d0f372ae294b922...HEAD`** (3 commits: `74c30731`
records, `56f1f135` the reader/grader fix, `67964f14` the owner ruling). The subject that carries
every finding is `tools/lexicon/lexicon.py`; `tools/lexicon/selftest.py` and the three records files
drew nothing.

**Round: 2.** Round 1 reviewed the code at `5f1815af` and filed fourteen entries. `56f1f135` is the
remediation for four of them. This round reviews that remediation. Nothing below re-reports a
round-1 entry; four of the five entries are defects `56f1f135` itself introduced.

## Verdict: BLOCKED

Three blockers, one high, one low. All three blockers are regressions: source that the reader at
`5f1815af` read correctly now raises, or is graded under a fabricated name. Two of them live in a
single new state variable, `type_alias`, which was added to fix round-1 entry 2 and which reaches
round-1 entries 9 and 12 as well — it turns the medium-severity swallow those entries described
into an unwaivable whole-file refusal, on mainstream semicolon-free TypeScript. The third
reintroduces the fabricated-identifier class that D3's own arm was written to close, through two
doors the new keyword filter cannot see.

The high is not a regression. It is round-1 entry 2's CLASS still open: the fix landed on two
instances of "a `<` in a type position" and left interface members and object-type parameters
refusing whole files exactly as they did at base. §7 names this shape by name.

Nothing here overturns a design decision. The `.ts`/`.tsx` mechanism pick, the two-parser split, the
frozen corpus as an instrument and the earned-mode rule all held again. The grader half of
`56f1f135` — the `_ts_sides` population fix and the raise-population assertion — drew no findings
and is the strongest part of the commit.

**This repo's green bar still cannot reach any of it.** `.lexicon.conf` line 23 arms `py` and `sh`
as parsers and leaves `ts`/`tsx` undeclared; `git ls-files '*.ts' '*.tsx'` returns 0. Every entry
below is adopter-facing. A green bar on this branch is not evidence about any of them, and saying so
is the whole point of the liveness rule in §7.

### Review shape

Raw 15, confirmed 12, refuted 3, unverified 0. Precision 0.80.

Precision matches round 1 exactly and sits well above the ~0.5 floor §8 names, which says the lens
priming was still right for this surface: a freshly edited hand-written tokenizer is the
"fresh/complex write path" case where multi-lens review earns its tokens. The 12 confirmed findings
consolidate into the 5 entries below. Four groups reached the same root cause from different
addresses and are folded, each entry naming the raw ids it absorbs:

- Entry 1 absorbs raw ids 5, 7 and 12, plus the CLEARING half of raw id 2 — all the one clearing
  site at `lexicon.py:1134`.
- Entry 2 absorbs raw ids 4, 8 and 13, plus the ARMING half of raw id 2 — all the one arming
  lookahead at `lexicon.py:1147`. Raw id 2 is the only finding split across two entries; it
  reported both halves of `type_alias` under one address, and they are two lines with two fixes.
- Entry 3 absorbs raw ids 1 and 6 — both the class-property arm at `lexicon.py:1481`, one reporting
  the annotation door and one reporting the ternary door.
- Entry 4 absorbs raw ids 3 and 9 — both the declarator keying at `lexicon.py:877`.

The folding is a synthesis decision, not a pipeline discard. Nothing was dropped, and the severity
on each entry is this report's adjudication over the merged evidence, not the arithmetic mean of
what the raw entries carried.

### Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted
to unverified, 0 spurious verdicts discarded, 0 duplicates discarded by the pipeline. Nothing was
lost, so the zero counts here are evidence rather than a gap: the unverified set is genuinely empty,
and every lens finding reached a skeptic and was adjudicated. The finding set is COMPLETE for the
lenses that ran, which is a statement about the pipeline and not about the corpus — the corpus
caveat is its own section below.

## The findings, severity-ranked

| # | Sev | Subject | Site |
|---|-----|---------|------|
| 1 | BLOCKER | `type_alias` is cleared only by a depth-0 `;`, so ASI leaves it armed | `tools/lexicon/lexicon.py:1134` |
| 2 | BLOCKER | `type_alias` arms on any depth-0 word `type`, name optional | `tools/lexicon/lexicon.py:1147` |
| 3 | BLOCKER | the class-property annotation walk runs past the member boundary | `tools/lexicon/lexicon.py:1481` |
| 4 | HIGH | a `<` in a type position is only recognised under a declarator | `tools/lexicon/lexicon.py:877` |
| 5 | LOW | a newline between `<` and the tag name is not a tag start | `tools/lexicon/lexicon.py:853` |

Entries 1, 2, 3 and 5 are REGRESSIONS against `5f1815af`. Entry 4 reproduces at base and is a class
left open, not a new break.

---

### 1 — BLOCKER · `type_alias` is cleared only by a depth-0 `;`

**Site:** `tools/lexicon/lexicon.py:1134` (raw ids 5, 7, 12, and the clearing half of raw id 2)

The new flag is set at line 1155 and cleared at exactly one place, line 1134, gated on
`c == ";" and len(stack) == 1`. `grep -n type_alias` returns four sites and no other clear. But a
TypeScript alias does not need that semicolon — ASI ends the declaration at the newline — so a
semicolon-free alias leaves JSX suppressed for the remainder of the file, and every later `<` is
emitted as an operator whose following `/` walks into `read_regex`.

**Impact.** Measured in this worktree at HEAD and at base:

| source | HEAD | base `5f1815af` |
|---|---|---|
| `type Props = { a: string }` then a JSX function | RAISE `unterminated regex literal` line 3 | `[('Row', 2)]` |
| `export type X = 1 \| 2` then a fragment | RAISE line 3 | `[('B', 3)]` |
| `type Foo = string` then JSX with an apostrophe | RAISE `unterminated ' string` line 3 | `[('C', 3)]` |

`scan_corpus` at line 1690 turns the `SyntaxError` into ``declared `parser` but does not parse``,
which exits non-zero. `WAIVER_FILES` at line 92 holds `verb` and `suffix` and nothing else, so a
refusal cannot be waived: an adopter's only move is to disarm the language and lose the file
entirely. Prettier's `semi: false` and standard style are mainstream, so this is not an exotic
input. Note the failure mode is exactly the one the comment at lines 1130-1133 says this placement
prevents; the comment is right about the placement and wrong about the terminator.

This also *upgrades* round-1 entries 9 and 12. Those described semicolon-free source silently
swallowing the next block, at MEDIUM and LOW. The same class now costs the whole file, loudly.

**Fix.** Two options, and the first is smaller. (a) Drop the flag: the case it exists for,
`type Mapper = <T>(x: T) => T;`, is decidable from the token tail the way `check_ts_type_position`
already decides its own — extend that function to return True when `toks[-1]` is op `=` and
`toks[-3]` is the word `type`. (b) If the flag stays, clear it at the alias's other terminators:
the `}` that pops back to depth 1, and a depth-1 newline whose last emitted token cannot continue a
type (`= | & , < extends`). Do not add a third clear site without observing the RED first.

**Left-shift.** A `test_ts_refusals` fixture per row of that table, staged RED before the fix lands.
The arm already shipped in `56f1f135` (`type Mapper = <T>(x: T) => T;`) passes either way because it
ends in `;`, so it is not the failing case for this and never was. Beyond the fixtures, one
structural gate is worth more than all three: a `selftest.py` arm that takes each conformance record,
strips its statement-terminating semicolons, and asserts the reader still does not RAISE. That gates
the semicolon-free CLASS rather than these three instances, and it costs one pass over a corpus the
suite already loads.

---

### 2 — BLOCKER · `type_alias` arms on any depth-0 word `type`, with the name optional

**Site:** `tools/lexicon/lexicon.py:1147` (raw ids 4, 8, 13, and the arming half of raw id 2)

The arming block fires on any word `type` at `len(stack) == 1`, skips spaces, scans an identifier
with `while k2 < n and (src[k2].isalnum() or src[k2] in "_$")` — a loop that happily consumes ZERO
characters — skips spaces again, and arms on `=` or `<`. It never looks BACKWARDS (a `.` is not an
emitted token, so `item.type` is indistinguishable from the `type` keyword) and it does not
distinguish `=` from `==` or `===`. The docstring at line 918 claims the flag "arms only where the
word is followed by a name and an `=`, which is the alias header and nothing else". That is not what
the code does, in three separate ways.

**Impact.** Measured at HEAD and at base:

| source | HEAD | base `5f1815af` |
|---|---|---|
| `const label = item.type === 1 ? <b>on</b> : "off";` then a function | RAISE line 1 | `[('after', 2)]` |
| `const type = 'button'` then a JSX arrow | RAISE line 2 | `[('Bar', 2)]` |
| `type<Foo>(1)` then a JSX arrow | RAISE line 2 | `[('B', 2)]` |
| `Comp.type = 'x'` then a JSX function | RAISE | parses |

The first row matters most, because it carries its semicolon and still refuses: the JSX sits BEFORE
the `;` that would have cleared the flag, so fixing entry 1 does not fix this. A discriminated-union
ternary at module scope is ordinary React and TypeScript. Reachability is narrower than it first
looks and the report should say so: both the arm and the clear gate on `len(stack) == 1`, so a
`.type ===` inside a function body or an object literal cannot arm it. Module scope is enough.

Same unwaivable whole-file refusal chain as entry 1.

**Fix.** Three conditions, all cheap and all on the same block. Require a real name (capture the
scan start and demand it consumed at least one character). Require a lone `=` — check
`src[k2:k2+1] == "=" and src[k2+1:k2+2] != "="` — so `==`, `===` and `=>` cannot arm it. Require the
word to START a statement: the previously emitted token is None, `;`, `{`, `}`, or the word `export`
or `declare`, which kills `const type` and `Comp.type` at the root rather than per-shape. Then fix
the docstring, or delete it; it is currently a claim the code contradicts.

**Left-shift.** A `test_ts_refusals` fixture per row above. The zero-length-name row is the one that
matters most as a regression test, because it is the door that turns entry 1 from "the file declares
an ASI alias" into "the file mentions `.type` at top level". Also add an assertion that the
docstring's claim is testable at all: a fixture named for each of the three arming conditions, so a
future widening of the predicate has to break something.

---

### 3 — BLOCKER · the class-property annotation walk runs past the member boundary

**Site:** `tools/lexicon/lexicon.py:1481`, walk at `:1490` (raw ids 1 and 6)

The new arm fires on any `word :` inside a class block and then calls
`read_ts_type_end(toks, k + 2, "=")`. That function stops only at a depth-0 `;` or `,` or an
unbalanced closer (lines 1253-1268). With ASI there is no `;` at the member boundary, so it walks
into the NEXT member, finds THAT member's `=`, `check_ts_arrow` sees THAT member's arrow, the arm
appends the annotation's word as a function name, and `k = e` skips the real name entirely. The `nt
== ":"` test also fires on a value-position ternary colon, which is not an annotation at all.

**Impact.** Measured at HEAD and at base:

| source | HEAD | base `5f1815af` |
|---|---|---|
| `class A { label: string \n onClick = () => {} }` | `[('label', 2)]` | `[('onClick', 3)]` |
| `class A { x = cond ? aVal : bVal \n onClick = () => {} }` | `[('aVal', 2)]` | `[('onClick', 3)]` |

This is the same defect D3 was written to close, reintroduced. A fabricated identifier enters the
graded population — P1 offenders, the `.conv` cell pins, `--list` — and the property that IS a
function is never graded. `aVal` is a pure fabrication out of a ternary. Neither `label` nor `aVal`
is a TypeScript keyword, so the new keyword-refusal arm in `selftest.py`, which the commit message
presents as gating D3's class rather than its instance, does not reject either. It gates one
sub-class of one door.

It is worth recording that the arm does fix what it was written for:
`private onChange: (e: Event) => void = (e) => {}` returns `[('onChange', 2)]` at HEAD against
`[('void', 2)]` at base. The regression is the walk's bound, not the idea.

This one is SILENT. No refusal, no non-zero exit, a green bar and a wrong graded population — which
is worse than entries 1 and 2 for the same severity, because there is nothing to notice.

**Fix.** Two guards. Require `toks[k-1]` to be a member boundary (`{`, `}`, `;`, or a modifier word)
so a ternary colon cannot fire the arm at all. Bound the walk to the member: in
`read_ts_type_end`, return `None` at depth 0 when a `word` token directly follows another `word`
token and the first is not a type operator (`keyof typeof infer extends readonly new`) — that
adjacency IS the ASI member boundary and cannot occur inside one annotation.

**Left-shift.** Both rows above as `test_ts_refusals` fixtures, staged RED first, asserting BOTH
directions: that `onClick` appears and that `label`/`aVal` do not. The keyword arm from `56f1f135`
should stay, but its own docstring needs to say what it does not catch — a non-keyword fabricated
name — because it currently reads as a class gate and is an instance gate. That is the §7 header
rule, and this entry is what it is for. The corpus-wide semicolon-strip arm proposed in entry 1
covers this door too, which is a second reason to build it.

---

### 4 — HIGH · a `<` in a type position is only recognised under a declarator

**Site:** `tools/lexicon/lexicon.py:877` (raw ids 3 and 9)

`check_ts_type_position` returns True only when `toks[-1]` is op `:`, `toks[-2]` is a word, and
`toks[-3]` is a word in `_TS_DECLARATORS` (`const let var readonly public private protected static
declare`). An interface member emits `{` as `toks[-3]`; an inline object type emits `{` or `(`.
Neither reaches the guard, so a generic function type in either position still opens a JSX frame and
still refuses the whole file.

**Impact.** Measured, and identical at HEAD and at base:

| source | both HEAD and base |
|---|---|
| `interface Api { map: <T>(x: T) => T; }` | RAISE `unterminated JSX element` line 2 |
| `function f(o: { cb: <T>(x: T) => T }) {}` | RAISE `unterminated JSX element` line 1 |

Not a regression — this is round-1 entry 2's class with two of its instances closed and the rest
open. Both shapes are ordinary `.tsx`, both cost the whole file, and both hit the same unwaivable
exit as entries 1 and 2. §7: gate the CLASS, not the instance.

The declarator keying is DELIBERATE and correctly argued: the comment at lines 858-860 explains that
`{ icon: <Home/> }` in an object literal has a colon too and its `<` really is an element, and that
39 corpus records carry JSX in that shape. That reasoning is sound. What is missing is the header
disclosure — the docstring says "two shapes" and names no residual, so a reader cannot tell the
narrowing was a decision rather than an oversight.

**Fix.** Widen the predicate from a declarator tail to a real type-position test that also accepts a
`<name> :` whose enclosing frame is an interface body, a type body, or a parameter list. The
tokenizer already carries `stack` and `opens`, and the parser already answers this question in
`read_ts_block_kind`, so the lexer is re-deriving something the code knows. Pass the frame in rather
than inferring it from three tokens. Whatever the shape of the fix, state the residual in the
docstring.

**Left-shift.** Both sources above as `test_ts_constructs` fixtures beside the two D1b arms, staged
RED first. The frozen corpus cannot substitute and this was measured, not assumed: a scan of all 115
records for a `name: <T>(` member returns 0 matches. That is why the new arms could certify the
instance while the class stayed red.

---

### 5 — LOW · a newline between `<` and the tag name is not a tag start

**Site:** `tools/lexicon/lexicon.py:853` (raw id 14)

`check_ts_tag_start` skips only space and tab after the `<`. Its sibling `check_ts_generic` thirty
lines above, at line 825, skips `" \t\n"` for the same lookahead. The inconsistency is internal and
reads as a slip rather than an argument.

**Impact.** `export const A = () => (\n  <\n    div>hi</div>\n);` raises
`unterminated regex literal opened at line 3` at HEAD and returns `[('A', 1)]` at base. JSX permits
any whitespace after `<`, so this is a fresh refusal on legal source. Reachability is close to nil:
no formatter emits a newline directly after `<`. It is filed anyway because it is a REFUSAL rather
than a silent miss, and because it is not among the refusals `parse_ts_defs`' own header declares
and prices against the conformance floor — an undeclared refusal is precisely the one that header
owes its reader.

**Fix.** One character class: `while j < len(src) and src[j].isspace(): j += 1`. Nothing else moves.

**Left-shift.** One `test_ts_constructs` fixture, or, better and no more expensive, an arm asserting
that `check_ts_tag_start` and `check_ts_generic` agree on the whitespace they skip — that gates the
divergence rather than this one instance of it, and the divergence is the actual defect.

## Why the corpus stayed green, again

`56f1f135`'s commit message makes the right argument: the frozen corpus scored 115/115 while the
reader carried all four round-1 defects, because the triggers appear in zero of its records. The
same blindness now hides four of the five entries above. Measured over
`ts-conformance-fixtures.json` in this tree:

- 115 records, **0** with no semicolon anywhere. Entries 1, 2 and 3 all need semicolon-free source.
- 8 records carry a `type X =` alias header. All 8 terminate the declaration with `;`.
- **0** records carry a `name: <T>(` member. That is entry 4's whole population.
- **0** records carry a class ASI property pair (`name: Type` newline `name =`). That is entry 3.
- 2 records contain `.type ===` — `tsx-generic-004` and `tsx-generic-009` — and BOTH carry it at
  stack depth greater than 1, inside an object literal and inside a call's arguments. Entry 2 arms
  only at depth 1, so the two records that hold the trigger WORD hold it in the one position that
  cannot fire.

That last line is the sharpest thing in this report. The corpus contains the token that breaks the
reader and contains it in the only shape that does not break it, so its green is not merely absent
evidence — it looks like coverage. `TOOL-aGradedDialect-2` F1 demands exact agreement with the
frozen corpus and gets it. That is coverage of one private codebase's dialect on one day, and it was
already true in round 1; what round 2 adds is that the corpus also cannot see the regressions
introduced by the fixes it certified.

Two consequences, both of them cheap:

1. The single highest-value gate on this whole surface is the semicolon-strip arm named in entry 1:
   take every conformance record, strip statement-terminating semicolons, assert the reader does not
   RAISE. One pass over an already-loaded corpus, and it gates entries 1, 2 and 3 as CLASSES.
2. `test_ts_constructs` and `test_ts_refusals` — hand-written, adversarial, cheap — remain the
   instrument for everything else. Every left-shift above lands in one of the two.

And the rule that would have caught all four regressions before they landed is already written down
in §7: a new gate is not landed until its failing case has been observed. `56f1f135` staged the
failing case for each defect it FIXED, which is why those fixes hold. It staged none for the new
`type_alias` state variable or for the widened class arm, which is why they do not.

## Landing recommendation

Do not push. Entries 1, 2 and 3 are regressions against a reader that handled all three inputs
correctly one commit ago, and every one of them is adopter-facing in a kit whose whole proposition
is that it grades a repo without lying about it. Two of the three cost an adopter the entire file
with no waiver available; the third is silent and puts a fabricated identifier into the graded
population.

The three of them are one sitting in one file: a clearing rule, an arming predicate, and a walk
bound. Entry 4 is a genuine design question about how the lexer learns its frame and can be a
follow-up unit, but its docstring should get its missing residual disclosure in the same commit as
the blockers, because that costs one sentence. Entry 5 is one character and rides along.

Land the semicolon-strip arm with the fixes, not after them. Without it, the next fix on this
tokenizer will be certified by the same 115/115 that certified this one.
