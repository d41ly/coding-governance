**Serves:** diff-review TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12

# Closing diff review — aPairedLexer units 6–12, round 3

Tier-2 closing diff review of the aPairedLexer fold. Node `a`, 2026-08-31. This round reads the
CODE, which had never been reviewed: rounds 1 and 2 reviewed an earlier diff and returned BLOCKED
(2 then 5 blockers); that loop went NON-CONVERGENT, its five blockers plus two highs were promoted
to units 6–12 under BUILD-METHOD M4, specced, spec-audited over four further NON-CONVERGENT rounds
(7, 5, 4, 5 blockers), and then built. This diff is that build.

Reviewed range: `1255d5d1ac5ccb84fe3e51f0f59e750658bb70f3...55fa6862b6da9f6c95c3872d8e3e9df3432a9146`

## Verdict: BLOCKED

Five blockers, all in `tools/hooks/agent-cap.js`, and every one of them measured as an ADMIT the
hook must deny. Three are DENY-to-ADMIT **regressions this diff introduced against its own base** —
the base at `1255d5d1` denies the exact fixture the tip admits. The subject is the only mechanical
control stopping an unbounded agent fan-out, so a fail-open here is the whole control, not a corner
of it.

The headline is the fifth fail-open the brief asked for, and there are four of them. This file has
now shipped a regex/division fail-open in five consecutive revisions. The reason is unchanged and is
visible in the numbers below: **both suites are all-green over every finding in this report.**
`tools/hooks/agent-cap.test.sh` reports `148 passed, 0 failed` and
`python tools/codebase-map/selftest.py` reports `PASS`, including an arm literally named
*"enumerate_exports: regex literals modelled; the two loss ceilings retire"* whose two retired
ceilings I reproduced against this tip. That is `fixture-passes-by-finding-nothing` at suite scale.

Answering the brief's aimed questions directly:

- **(b) Do `resolveRegexStart`'s clauses have the right order, and are they each correct?** The
  order is wrong (B2) and the set is incomplete (B3, H2). Its five clauses are one ordering defect
  and two missing cases away from correct.
- **(d) Can the two scanners still disagree?** No — and that is not the reassurance it sounds like.
  Both scanners now call one predicate, so they agree perfectly *on the wrong answer*. Unifying them
  converted three fail-opens into one shared fail-open reported by both views as trustworthy.
- **(e) Can `readJoinAt` pick the wrong occurrence?** Yes, on every line carrying two calls (B1).
- **(f) Does the Python side lose or invent definitions?** Both, measured (H3).

## Review shape

Raw 24, confirmed 20, refuted 4, unverified 0, precision 0.83. The 20 confirmed findings collapse to
**13 distinct defects** after adjudication — the fan re-reported the `readJoinAt` defect three times
(ids 1, 7, 20), the clause-order defect twice (ids 2, 11), the `prev='/'` defect twice (ids 6, 12),
and the Python keyword gap four times (ids 4, 9, 13, 22). Severities below are the ones adjudicated
here, not the ones the finders proposed.

| # | Sev | Site | Defect |
|---|-----|------|--------|
| B1 | blocker | `tools/hooks/agent-cap.js:809` | `readJoinAt` reads the FIRST occurrence, so call #2 on a line is judged on call #1's cap |
| B2 | blocker | `tools/hooks/agent-cap.js:301` | `KEYWORD_TAIL` tested first, and `codeText` never receives literal bytes |
| B3 | blocker | `tools/hooks/agent-cap.js:304` | `prev = '/'` after a regex literal or `*/` is read as a regex START |
| B4 | blocker | `tools/hooks/agent-cap.js:338` | `checkDeclinedSpan` models char classes; the code readers do not, and the fallback is blind the same way |
| B5 | blocker | `tools/hooks/agent-cap.js:93` | `dirty` routes all four rules to a fallback that truncates at `//` inside a backtick |
| H1 | high | `tools/hooks/agent-cap.js:296` | property-name guard is a one-character lookbehind, so `obj . in` defeats it |
| H2 | high | `tools/hooks/agent-cap.js:310` | postfix `++`/`--` missing from the clause set; a wrongly ACCEPTED regex carries no signal at all |
| H3 | high | `tools/codebase-map/map_lib.py:417` | Python predicate has no keyword clause: invents a symbol, loses a real one, and the docstring claims parity |
| M1 | medium | `tools/hooks/agent-cap.js:403` | `codeText` concatenated across lines with no separator, corrupting the word boundary |
| M2 | medium | `tools/codebase-map/selftest.py:1383` | corpus arm asserts `len(seen) > 50` over a corpus of 103 |
| L1 | low | `tools/hooks/agent-cap.js:301` | `KEYWORD_TAIL` rescans unbounded `codeText`, making both scanners quadratic |
| L2 | low | `memory/map/features/agent-cap.md:168` | dossier names `startsRegex`; no such symbol exists |
| L3 | low | `tools/hooks/agent-cap.js:302` | `if (prev === '')` is unreachable after the `';'` re-seed |

Every hook defect is carried by BOTH copies: `diff -q tools/hooks/agent-cap.js
.claude/hooks/agent-cap.js` is clean, so the mirror ships them too.

---

## B1 — blocker — `tools/hooks/agent-cap.js:809`

`readJoinAt` resolves the call with `line.indexOf(needle)` — the first occurrence — while the S1
caller at L919-922 loops `HELPERS.exec` over every occurrence on the line and passes only the matched
TEXT, discarding `m.index`. Both iterations therefore re-read the first call's arguments, and the
second call's cap is never read at all. This is a regression: the base used
`joinCall(code, i, m.index + m[0].length - 1)`, the match's own index.

**Measured.** With the standard `boundedParallel` helper defined above it, this last line exits 0 at
the tip and exits 2 at base `1255d5d1`:

```js
const r = [await boundedParallel(A.map((x) => () => work(x)), 5), await boundedParallel(B.map((x) => () => work(x)), 500)]
```

The base denial names it exactly: `the cap argument at the boundedParallel() CALL SITE is 500, above
the 5-agent cap`. Splitting the same two calls onto separate lines denies at the tip, which isolates
the cause to the shared line. A 500-wide fan-out passes rule 3 — the one rule whose only job is
reading that number.

The suite's own `version parity: none of 79 deny fixtures admits at 1.12 while denying at 1.11` arm
exists to catch precisely this and does not, because no fixture puts two helper calls on one line.
The same first-occurrence collapse applies to the S2 definition scan at L897.

**Fix.** Pass the occurrence ORDINAL rather than the needle alone: count how many times `needle`
precedes `m.index` in the detection line, then take that same ordinal in the join view via a loop of
`indexOf(needle, from)`. If the join view holds FEWER occurrences than the detection view, return
`{ambiguous: true}` — that is the S2b rule this helper already states, applied per-occurrence instead
of per-line, and it keeps the misaligned case fail-closed.

**Left-shift gate.** Add deny fixtures with two helper calls on one line — compliant first, over-cap
second — in both `boundedParallel` and `boundedPipeline` spellings, plus one for two DEFINITIONS on
one line. Then strengthen the version-parity arm so it is not satisfied by a fixture set that never
exercises multiplicity: assert that every deny fixture still denies when its call is duplicated onto
a single line with a compliant sibling.

## B2 — blocker — `tools/hooks/agent-cap.js:301`

`resolveRegexStart` tests `KEYWORD_TAIL` against `codeText` FIRST, and `codeText` is only ever
appended on the code fall-through (L403, L770) — the string, template and regex branches never feed
it. After `return "a"` the running code text still ends `return `, so `KEYWORD_TAIL` matches and the
slash opens a phantom regex. This overrides the closing-QUOTE clause added two lines below at L306
for exactly this shape, which is unreachable behind it.

**Measured**, `node --check` clean, exit 0:

```js
async function go() {
  return "a" / await parallel(D.map((x) => () => agent({ prompt: x }))) / 2
}
```

`--selftest` shows the span consumed cleanly — the rendered line is `  return ""` followed by spaces
and `2`, with `unterminated:false, dirty:false, clean:true`. No signal reaches any of the four rules.
The control without the keyword, `const z = "a" / await parallel(...) / 2`, exits 2 — which proves
the quote clause works and is simply ordered second. Template operands and `typeof` behave the same.

This is not the declared decline-side ceiling. At a closing quote the file's own L306 comment says
the slash must be DIVISION.

**Fix.** Only the identifier clause can be a keyword tail, so gate `KEYWORD_TAIL` on it and let the
unambiguous expression-enders win first:

```js
if (prev === '') return true
if ('})]'.includes(prev)) return false
if (prev === '"' || prev === "'" || prev === '`') return false
if (/[A-Za-z0-9_$]/.test(prev)) return KEYWORD_TAIL.test(codeText)
return true
```

Equivalently, append a sentinel to `codeText` whenever a literal is consumed, so a literal can never
leave a keyword as the tail. The first form is preferable — it also fixes L1, since the regex then
runs only at identifier positions.

**Left-shift gate.** A fixture arm that, for each of the nine `REGEX_KEYWORDS`, asserts
`<keyword> "lit" / <raw primitive> / 2` DENIES — generated from `REGEX_KEYWORDS` itself, so a keyword
added later cannot escape the arm. This is the "gate the CLASS, not the instance" rule the charter
states.

## B3 — blocker — `tools/hooks/agent-cap.js:304`

`'})]'` omits `/`, but both scanners set `prev = '/'` after consuming a regex literal (L381, L753)
and after closing a block comment (L412, L778). `resolveRegexStart` has no case for `/` — not empty,
not in `'})]'`, not a word character, not a quote — so it falls through to `return true` and reads
the next slash as a regex START where JavaScript reads division.

**Measured**, both halves, `node --check` clean, both exit 0:

```js
const n = items.length /* how many */ / 2 + (await parallel(items.map((f) => () => agent({ prompt: f })))).length / 3
const n = /a/ / 2 + (await parallel(items.map((f) => () => agent({ prompt: f })))).length / 3
```

The first line's view collapses to `const n = items.length` + spaces + `3`, erasing the raw
primitive. Deleting the block comment restores the DENY. All three signals report the view is
trustworthy (`unterminated:false, dirty:false, clean:true`), because the slash is ACCEPTED rather
than declined and `checkDeclinedSpan` is wired only behind a decline (L366, L740).

The two half-roots differ, and the Python sibling gets one of them right: `render_comment_free`
leaves `prev` untouched across a comment, which is the correct behaviour after `*/`. After a regex
literal `prev` should read as expression-ENDING, since a regex literal is a primary expression.

**Fix, verified.** `if ('})]/'.includes(prev)) return false`. I applied this one-character change to
both copies, confirmed both fixtures flip to exit 2, and ran the full suite: **148 passed, 0 failed**.
It is correct for the regex-close case and conservative for the block-comment case, where a declined
slash raises `checkDeclinedSpan` and routes to the fallback — the fail-closed direction. Tree
restored; nothing is left applied.

**Left-shift gate.** Both shapes as deny arms. More durably: an arm asserting that every character
`prev` can be assigned (`'/'`, `'` `` ` `` `'`, quotes, and any `ch`) is covered by an explicit clause
in `resolveRegexStart`, so a new `prev` assignment cannot silently land in the `return true`
fall-through — that fall-through is where three of the five fail-opens in this report live.

## B4 — blocker — `tools/hooks/agent-cap.js:338`

`checkDeclinedSpan` models character classes, so both slashes inside `[//]` are neither a closer nor
an opener and the span reports NOT ambiguous. But the code-mode readers in both scanners model no
class and `break` at that same `//` (L362, L731), gutting the rest of the line. This is the exact
leak shape the whole unit-6 signal exists to catch, and the signal reports the gutted view as
trustworthy.

**Measured**, `node --check` clean, exit 0:

```js
async function go(items, s) {
  if (s) /[//]/.test(s), await parallel(items.map((f) => () => agent({ prompt: f })))
  return 1
}
```

`--selftest` shows both views truncating the line to `  if (s) /[` with
`unterminated:false, dirty:false, clean:true`.

The second half matters more than the first. Adding `//` to the opener set restores the `dirty`
signal, but the line is STILL admitted, because the fallback view is
`stripStrings(l).split('//')[0]` (L93, L468, L870, L1182) and truncates at the very same `//`. **The
remedy the signal routes to is blind to the shape that raised it.** That is larger than declared
trade (1), which promises an ambiguous decline routes to a per-line view that recovers something;
here it recovers nothing.

**Fix.** Two parts, and part (b) is the load-bearing one. (a) In `checkDeclinedSpan`, treat a
line-comment opener as an opener: `if (raw.slice(k, k + 2) === '/*' || raw.slice(k, k + 2) === '//')
opener = true`. (b) Give the ambiguous line a view that is not blind in the same way — either emit
`raw.slice(i)` verbatim into the view for a declined-and-ambiguous slash while keeping `dirty` set,
or, matching the doctrine `readJoinAt` already applies, DENY that line outright as unreadable rather
than routing it to a stripper that cannot see past the `//`.

**Left-shift gate.** An arm asserting the fallback view is never a strict SUBSET of the primary view
on a line where `dirty` is set — i.e. the routed remedy must not see less than the view it replaces.
That gates the class, where a `[//]` fixture alone gates one instance.

## B5 — blocker — `tools/hooks/agent-cap.js:93`

The new `dirty` signal routes rules 1, 2, 3 and 5 onto the per-line fallback view, and that view
truncates at a `//` living inside a template literal — so one line of ordinary arithmetic turns all
four rules dark on every line carrying a URL in a backtick string.

**Measured base DENY → tip ADMIT**, `node --check` clean:

```js
console.log("pct", done / total, "half", total / 2)
const p = `docs at http://example.com`; const out = await parallel(D.map((f) => () => agent(f)))
```

Base `1255d5d1` exits 2; tip `55fa6862` exits 0. **Deleting only the first line restores the tip
DENY**, so the ordinary arithmetic is the causal trigger, not the fixture shape.

The mechanism: at the first `/`, `prev` is `l` so `resolveRegexStart` declines; `checkDeclinedSpan`
then scans the raw line, sees the `"` of `"half"` as an opener and the second `/` as a closer, and
sets `dirty` — even though both slashes were modelled CORRECTLY. `renderCodeView` reports
`unterminated:true` on a byte-perfect view, the consumers switch to
`stripStrings(l).split('//')[0]`, `stripStrings` leaves backticks alone, and everything right of the
URL's `//` vanishes.

This is strictly larger than declared trade (1), which predicts a false-positive DENY. What ships is
a fail-OPEN of the raw-primitive ban itself. `offendingLines`' own comment at L84-89 states the rule
this breaks: *seeing LESS is safe for a rule whose findings are permissions and dangerous for a rule
whose findings are denials* — and `dirty` makes that lossier view reachable from arithmetic.

**Fix.** A denial rule must never lose reach when a view is distrusted. Either (a) take the UNION for
rules 1/2/3/5 — deny if EITHER view shows the offending token, rather than switching to one; or (b)
build the fallback so it cannot see less, by blanking backtick spans before the `//` split.
Independently, tighten `checkDeclinedSpan` so a span whose opener is a `'`/`"` string that CLOSES
before the candidate closer is not counted as an opener — that alone removes the arithmetic trigger.

**Left-shift gate.** An arm pinning that a raw `parallel(` is DENIED on a line following any
`dirty`-setting line, parameterised over the URL-in-backtick shape. Structurally better: assert for
every one of the 79 deny fixtures that prepending `console.log("a", x / y, "b", y / 2)` does not
change its verdict. That single arm would have caught this, B1 and B5 together.

## H1 — high — `tools/hooks/agent-cap.js:296`

`KEYWORD_TAIL`'s property-name guard is the single-character class `[^.\w$]`, so any whitespace
between the dot and the keyword satisfies it. `obj . in` reads as a bare `in` keyword and opens a
regex position.

**Measured**, `node --check` clean, exit 0:

```js
const n = obj . in / 2, m = await parallel(D.map((f) => () => agent(f))) / 3
```

The view blanks to `const n = obj . in` + spaces + `3`, with `dirty:false, clean:true`. The zero-space
control `obj.in / 2` on the identical line exits 2. `obj . in` is legal JavaScript, and because
`codeText` concatenates lines with no separator (M1), the wrapped form — `obj.` ending one line, the
member starting the next — lands the same way. The comment at L299 claims `obj.in`, `x.of`,
`m.delete`, `p.new` and `r.case` are covered; only the zero-space spelling is.

**Fix.** Track a boolean `prevWasDot`, set at the `.` character and cleared by any non-space token,
rather than encoding the guard as a fixed-width lookbehind in a regex over concatenated text.

**Left-shift gate.** Deny fixtures for `obj . in / 2` and the line-wrapped `obj.` / `in` form, plus
the same pair for each keyword the L299 comment names — the comment currently asserts coverage the
code does not have, which is the gate-satisfied-by-its-own-comment-prose shape.

## H2 — high — `tools/hooks/agent-cap.js:310`

The clause set omits the POSTFIX operators, so `i++ / 2` reads as a regex start. `prev` is `+`, no
clause matches, and the fall-through `return true` opens a phantom span over live code.

**Measured**, `node --check` clean, exit 0:

```js
const y = i++ / 2, z = await parallel(D.map((f) => () => agent(f))) / 3
```

The view collapses to `const y = i++` + spaces + `3`; both scanners report
`unterminated:false, dirty:false, clean:true`. The control `i + 1 / 2` on the identical line exits 2,
so the postfix operator alone flips DENY to ADMIT. This shape is outside the ACCEPTED CEILINGS, which
name only identifier, number, closing-bracket and closing-quote positions.

`++`/`--` are the only expression-enders whose last character escapes all five clauses, apart from
the `prev = '/'` sentinel of B3.

**The asymmetry is the real lesson here, and it generalises past this finding.** `checkDeclinedSpan`
is wired only behind `!resolveRegexStart(...)` (L366, L740), so a wrongly ACCEPTED slash can never
raise `dirty`. A wrong decline is signalled; a wrong accept is silent. Four of the five blockers in
this report are wrong ACCEPTS, and all four report `clean:true`.

**Fix.** Track the last two significant code characters and add a clause returning false on `++` or
`--`. Separately, set `dirty` whenever an ACCEPTED regex span swallows a `(` or an identifier-shaped
token, so a wrong accept is at least as visible as a wrong decline.

**Left-shift gate.** An arm asserting that a blanked span never contained `parallel(`, `pipeline(`,
`boundedParallel(` or `.ref` — i.e. that the lexer never erases the exact tokens the four rules hunt.
That is a single invariant covering B2, B3, H1 and H2 at once, and it does not depend on anyone
predicting the next operator the clause set forgot.

## H3 — high — `tools/codebase-map/map_lib.py:417`

`_js_resolve_regex_start` has exactly four clauses — start-of-input, `})]`, alnum/`_$`, quote — and
NO keyword clause, while the JavaScript `resolveRegexStart` carries `REGEX_KEYWORDS` with nine. Its
docstring says *"Same conservative rule the JavaScript side states"*, which is false in the direction
that matters. `_js_resolve_regex_start('n')` returns `''`, so a `/` after `return` is DIVISION and the
regex is never modelled. Two languages, two answers to one question.

**Both "retired" losses reproduce against this tip**, measured through `enumerate_exports`:

- **INVENTS** — this file:

  ```js
  export const REAL_A = 1
  export function isTick(s) {
    return /[`]/.test(s)
  }
  /*
  export const GHOST = 99
  */
  const msg = `hello`
  export const REAL_B = 2
  ```

  yields `['GHOST', 'REAL_A', 'REAL_B', 'isTick']`. The regex-borne backtick opens a phantom template
  span to the next real backtick, the block comment inside is emitted verbatim, and **`GHOST` — which
  exists only inside a comment** — enters the enumerated set the coverage ratchet demands be claimed.
- **LOSES** — `function g(s) { return /[/*]/.test(s) }` with `export const REAL_B = 2` above a later
  `const c = 1 /* real */` yields `['REAL_A', 'REAL_C']`. `REAL_B` is silently swallowed, defeating
  the loud-raise completeness guarantee `enumerate_exports`' docstring is built on — a swallowed
  export is a silent drop, not a raise.
- **Control** — the same shapes with the regex after `=`, an unambiguous position, return
  `['REAL_A', 'REAL_B']` correctly. So this is a predicate gap, not a language limit.

The docstring at L658-666 claiming TOOL-aPairedLexer-12 *"RETIRED the two losses this paragraph used
to declare"* is therefore false for the whole keyword-position class. The residual paragraph at L671
is written for AMBIGUOUS positions, and `return /` is not ambiguous. Worse, the residual describes
the leftover only as *"still mis-modelled"* — it never discloses that the mis-model can ADD a symbol,
which the retired text at least did for its two losses.

The guarding arm, `test_enumerate_exports_regex_borne_comment_opener`, writes every regex after `=`
and passes. That is the same *"every regex arm wrote the literal after an equals sign"* critique this
build made of its own JavaScript arms, reproduced in the Python arm written to close it.

Latent in gov only because its tracked JS/TS has zero keyword-position regexes, so the selftest is
green by absence. The exposure is the copy-installed kit in adopter corpora, where `return
/.../.test(x)` is ordinary JavaScript, and where the map ratchet would force an adopter to claim a
key that does not exist.

**Fix.** Port the keyword clause: keep a bounded suffix of emitted code characters and test the same
tail regex before the `prev.isalnum()` clause, with the property-name guard. If the divergence is
deliberate, delete the "Same conservative rule" sentence, re-declare the block-opener loss as LIVE
for keyword positions, and state that the mis-model can ADD a symbol.

**Left-shift gate.** Add both positional variants — regex after `return`, and after `)` — to the
GHOST assertion in `test_enumerate_exports_regex_borne_comment_opener`. Then, because the two
predicates are one question, add a parity arm that runs a shared fixture list through both
`_js_resolve_regex_start` and the JS `resolveRegexStart` via `--selftest` and asserts identical
verdicts. That is the only gate that keeps the two languages from drifting again.

## M1 — medium — `tools/hooks/agent-cap.js:403`

`codeText` is declared once outside the line loop (L350, L722) and only ever grows via `codeText +=
ch` (L403, L770) — no newline or separator is ever appended, so lines concatenate. `KEYWORD_TAIL`'s
`(?:^|[^.\w$])` boundary therefore reads the PREVIOUS line's last character.

**Measured** end-to-end. Byte-identical second lines, opposite verdicts, both `node --check` clean:

- `const n = 1` / `typeof /pipeline(x)/` → exit 2 (regex not recognised, `pipeline(` leaks into the
  view, rule 1 fires)
- `const n = (1)` / `typeof /pipeline(x)/` → exit 0 (regex recognised and blanked)

The comment at L293-295 names the running code text as the subject *precisely* to get cross-line
cases right; it gets them wrong in the common direction. Both `codeText` and `KEYWORD_TAIL` are new
in this diff, so this is introduced, not inherited. Ranked medium because the harm here is a
false-positive DENY, but the predicate is shared with the decline path that feeds `dirty`, so the
corruption is not confined to the safe direction — and it is the mechanism that makes H1's
line-wrapped `obj.` form reachable.

**Fix.** Append a separator per line (`codeText += '\n'`) in both scanners.

**Left-shift gate.** A two-line arm whose only variation is the previous line's last character, with
both spellings asserted to reach the same verdict.

## M2 — medium — `tools/codebase-map/selftest.py:1383`

`test_render_comment_free_corpus_is_unchanged` computes the full symbol set `seen` and then asserts
only `len(seen) > 50`. The set is never compared to anything, so the arm cannot detect the regression
its name and docstring claim it makes runnable.

**Measured**: `git ls-files '*.js'` returns 10 files and the arm's own extraction yields **103**
(file, symbol) pairs against a floor of 50. The arm therefore tolerates losing 53 definitions (51%)
and still passes. Its docstring states the point explicitly — *an earlier revision of this function
removed EIGHT real definitions from this repo's tracked JavaScript, and that number was remembered
rather than runnable. Now it is runnable* — and an 8-definition loss passes this assertion untouched.

The inline comment reframes the assertion as a collapse check, which is honest about the weaker
property but leaves the function NAME and the docstring claiming the stronger one. Two answers to one
question, and the weaker one is what ships. This is the only arm touching real code; all other
coverage of the map_lib regex change is fixture-based, which is why M2 and H3 compound.

**Fix.** Assert the set difference is empty against a committed baseline, rather than a floor. If a
floor is genuinely what is wanted, rename the arm and correct the docstring so it stops claiming a
regression guard it does not implement.

**Left-shift gate.** This finding IS the gate repair. Pair it with H3's parity arm so the corpus arm
and the fixture arms cover different failure directions.

## L1 — low — `tools/hooks/agent-cap.js:301`

`KEYWORD_TAIL.test(codeText)` runs against an unbounded, ever-growing `codeText` once per slash — in
fact twice, since `resolveRegexStart` is called separately for the dirty test and the regex branch
(L366/L367, L740/L741). The regex `(?:^|[^.\w$])(…)\s*$` has no left anchor, so each slash rescans
the whole running text and both scanners become quadratic in script size.

**Measured** at the tip: 1000 lines 274 ms, 2000 lines 684 ms, 4000 lines 1868 ms — superlinear —
against base `1255d5d1` at 289 ms for the same 4000-line payload, which is flat. This is a
`PreToolUse` hook, so the cost lands on every `Workflow` tool call. Nothing in the live population
trips it today (the repo's harnesses are 88-624 lines), which is why this is low, but §7 declares no
wall-clock ceiling for this hook and an inline script is exactly where an unusually large one arrives.

**Fix.** The longest keyword is 10 characters, so only the tail can ever match: test
`codeText.slice(-24)`. B2's fix subsumes this by running the regex only at identifier positions —
doing both is one line and restores linear cost.

**Left-shift gate.** Declare a wall-clock ceiling for the hook and assert it in the suite over a
generated large script, per §7's "COST IS A VERDICT" — a checker arriving without a ceiling reds by
that fact.

## L2 — low — `memory/map/features/agent-cap.md:168`

The dossier names the shared predicate `startsRegex`. Grep over the whole tree returns exactly one
hit — this line. The function is `resolveRegexStart`, and `memory/map/generated/symbols.json` already
carries that id. The dossier and the generated symbol table disagree **in the same commit that
regenerated the latter**; `55fa6862` ("conform the new names") did not sweep the dossier prose. No
behaviour, but it is exactly the drift class the map's coverage ratchet exists to catch, in the
dossier for the file it dossiers.

**Fix.** Rename to `resolveRegexStart` at `memory/map/features/agent-cap.md:168`.

**Left-shift gate.** A map leg asserting that every backticked identifier in a dossier body resolves
to an id in `symbols.json` for the file that dossier covers. That converts this whole class from
prose review to a gate.

## L3 — low — `tools/hooks/agent-cap.js:302`

`if (prev === '') return true` is unreachable. TOOL-aPairedLexer-7 re-seeded `prev` to `';'` in both
scanners (L354, L723), and exhaustive grep of every `prev` assignment shows nothing anywhere sets it
back to the empty string — every write is `'/'`, `` '`' ``, `q`, or a `ch` that already passed
`!/\s/.test(ch)`.

The cost is not runtime, it is the contradictory account: L302-303 tells a reader start-of-input is
`''` and describes the resulting darkness in the present tense, while L354 tells the same reader
start-of-input is `';'` precisely so that cannot happen. This is the unobservable-code-path shape
`resolveConsts` (L451-459) explains at length that unit 10's S2 was DROPPED to avoid — the
amendment-leaves-its-other-half-standing class, in the file that names it.

**Fix.** Delete the branch and fold its comment into the `let prev = ';'` seed comment, which is
where the fact now lives.

**Left-shift gate.** None warranted; it is a two-line deletion. If a start-of-input sentinel is still
wanted, assert the seed rather than branching on it.

---

## Bug-class checklist — what the diff actually hit

Run over the area this diff touches, per §10.

| Class | Verdict |
|---|---|
| fixture-passes-by-finding-nothing | **HIT, and it is the dominant failure of this build.** Both suites are all-green over all five blockers. B1 is missed by the arm written to catch it; H3 is missed by the arm named for the direction it fails in; M2 is an arm that structurally cannot fail. |
| two-answers-to-one-question | **HIT.** H3 (JS has nine keywords, Python has none, docstring claims parity), L3 (two accounts of start-of-input), M2 (name and docstring claim one property, assertion implements another). |
| amendment-leaves-its-other-half-standing | **HIT.** L3 — unit 7 re-seeded `prev` and left the branch that existed for the old seed. B2 is the same shape: the quote clause was added and the ordering that makes it reachable was not. |
| rationale-names-a-consumer-that-does-not-exist | **HIT.** L2 — the dossier names `startsRegex`, which exists nowhere. |
| allowlist-narrower-than-the-root-it-guards | **HIT.** B4 — `checkDeclinedSpan` models character classes that the code readers it guards do not model, so the guard's language is richer than the thing it guards; the signal and the readers disagree about what a line contains. |
| staged-break-substitutes-a-synthetic-value | Not hit. |
| heredoc-escape-reaches-the-regex | Not hit in the shipped code. It did affect this review's own tooling; every fixture here was authored via Write rather than a heredoc, per the standing gotcha. |
| concurrency-is-not-a-budget | Not hit as a doctrine error, but B1 is its mechanical failure: the total-bound rule is unenforced on any line carrying two calls. |
| fold-text-is-unreviewed-surface | **HIT.** L2 and the H3/M2 docstrings all landed in the fold, and all three make claims the code does not support. |
| staged-break-never-applied | Not hit. |
| trailing-comma-counted-as-an-element | Not hit; `topLevelArgs` handles it. |

## What this says about the loop

The brief asked where to aim, on the grounds that four fail-opens shipped green because every regex
arm wrote its literal after an equals sign. That diagnosis was right and the build did not act on it:
the new Python arm written to close the gap **also** writes its regex after an equals sign (H3), and
the new corpus arm cannot fail at all (M2).

The structural point is that the fixture set is chosen by the same understanding that wrote the
predicate, so it tests the positions the author already thought of. Three gates above break that
coupling and are worth more than the individual fixtures: the invariant that a blanked span never
contains a hunted token (H2), the parity arm running one fixture list through both languages (H3),
and the mutation arm that prepends a `dirty`-setting line to all 79 deny fixtures (B5). Each fails on
a shape nobody predicted, which is the only property that would have stopped this round.

One credit where it is due: unifying the two scanners onto one predicate did close the
scanners-disagree class — question (d) is genuinely answered. The cost is that a single wrong answer
is now delivered by both views with `clean:true`, so the redundancy that used to make disagreement
detectable is gone. That trade is only sound once the predicate is right, and it is not yet right.

## Method

All findings reproduced against `55fa6862` in a clean worktree, comparing to base `1255d5d1` via `git
show 1255d5d1:tools/hooks/agent-cap.js`. Hook fixtures were driven end-to-end as real `Workflow`
payloads (`tool_name` `Workflow`, `tool_input.script`), not through the seam alone, with
`--selftest` used only to explain a verdict already measured. Every JavaScript fixture was confirmed
`node --check` clean, so no finding rests on invalid syntax. Every fail-open is reported with the
control that denies. Suites run: `bash tools/hooks/agent-cap.test.sh` (148 passed, 0 failed) and
`python tools/codebase-map/selftest.py` (PASS).

B3's fix was applied to both hook copies and the full suite re-run (148 passed, 0 failed) before the
tree was restored with `git checkout`. The working tree is clean; no fix in this report is left
applied.
