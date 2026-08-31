**Serves:** diff-review TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12

# Re-review of the fix — aPairedLexer units 6–12, round 2

*Node `a`, 2026-08-31, round 2 of the promoted-units subject. BUILD-METHOD M8: the previous round
returned BLOCKED with five blockers and three highs, the build fixed them in one commit, and this
round reviews THE FIX rather than the diff again — base is the reviewed tip, head is the fix commit,
so the range is exactly the repair. A parallel fan of primed finder lenses over both scanners, the
Python extractor and the two suites, then skeptics prompted to REFUTE each finding against the
source, then this synthesis pass. Every behavioural claim below is an exit code this pass measured
itself by piping a real `Workflow` payload into the real hook at three revisions — the fix tip, the
reviewed base, and the build's own pre-build base — never a reading. Every fixture is `node --check`
clean. Round numbering note: the predecessor record is filed as `…-diff-round3.md` because that
series numbers rounds build-wide; this record is round 2 of the fix loop, as the brief states.*

Reviewed range: `55fa6862b6da9f6c95c3872d8e3e9df3432a9146...26786d7018d68c92d93766b9c7882b2f19d4bc1a`
(20 files, +819/-52; the product change is `tools/hooks/agent-cap.js`, `tools/codebase-map/map_lib.py`
and `tools/codebase-map/selftest.py`).

## Verdict: BLOCKED

Counts sit here rather than on the heading, because that token is a closed set and a tally appended
to it turns a structural check into a semantic one. Five blockers, four highs, one low.

**The central claim of the fix is refuted by measurement.** The commit's diagnosis was right — a
wrongly ACCEPTED slash could never raise `dirty`, so four of five blockers were silent wrong accepts
— and the repair it chose, `SWALLOW_GUARD`, is the wrong remedy for it. The guard's only action is to
set `dirty`. `dirty` does not deny; it makes every rule *switch views*, from the line-aligned code
view to `stripStrings(l).split('//')[0]`, which sees **strictly less** — it leaves backticks alone
and truncates at the first `//`, including one inside a template literal. So widening `dirty` widens
the hole. Declared trade (2) says the guard's cost "is a false DENY rather than a false admit". It is
measurably both, from the same trigger, and the false ADMIT is a fresh DENY-to-ADMIT regression
against the reviewed base off a single ordinary regex literal.

Two of the five round-1 blockers were not fixed and reproduce unchanged, so the commit body's
"OBSERVED RED: all five blocker fixtures ADMIT against the reviewed tip and DENY after" is false for
B4 and B5 — both still ADMIT at the tip. Both suites are green over every finding in this report:
`bash tools/hooks/agent-cap.test.sh` reports `158 passed, 0 failed` and
`python tools/codebase-map/selftest.py` reports `PASS`, including the arm added this commit to
replace a check that could not fail — which also cannot fail, staged three ways.

Answering the brief's aimed questions directly:

- **(a) Can a hunted token still be swallowed by an ACCEPTED regex span with no `dirty`?** Yes, two
  ways. The guard is case-sensitive, so it never matches `boundedParallel(`/`boundedPipeline(` — the
  exact identifiers rule 3 reads the cap number from — and it omits `verdictByRef`, rule 5's third
  ban. B-2.
- **(b) Is the guard's false-DENY cost larger than the record claims?** Yes, and that is the smaller
  half of the problem: it is also a false-ADMIT cost the record does not mention at all. H-2 and B-1.
- **(c) Is `dirty` consumed by all four rules on this path?** Yes — and that is the defect. All four
  consume it by *dropping to a lossier view*. B-1.
- **(d) Do B4, B5 and H1 reproduce?** All three, measured at the tip. B-3, B-4, H-1.
- **(e) Does the clause reorder break a position that previously worked?** Yes. Not the keyword path
  — the `/` expression-ender added beside it. `/* c */ /re/` is now read as division. B-5.
- **(f) Does the Python keyword clause create the mirror of B2?** Not that one. It creates a
  different mirror: the JS side gained two more clauses in the same commit and Python got neither, so
  the two predicates diverge again and a GHOST symbol is measurable through the definition rules. H-3.

## Review shape

Raw 24 · confirmed 24 · refuted 0 · unverified 0 · precision 1.00.

The 24 confirmed lens findings consolidate to **10 distinct defects** below (five lenses reached the
`dirty`-fallback root by five different fixtures). Nothing was dropped in consolidation; each row
names the lens ids it absorbs, and where two ids shared a fixture but not a root cause they are
separate rows. Severity in the table is this pass's adjudication, not the lens's.

| # | Sev | File:line | Defect | Lens ids |
|---|---|---|---|---|
| B-1 | blocker | `tools/hooks/agent-cap.js:414` | `dirty` disarms the denial rules; `SWALLOW_GUARD` is a fail-OPEN trigger | 1, 7, 13, 21 |
| B-2 | blocker | `tools/hooks/agent-cap.js:306` | the guard's token list is a retyped copy of the four rules and misses two of them | 2, 10, 14, 15, 22 |
| B-3 | blocker | `tools/hooks/agent-cap.js:360` | B4 unfixed: `//` in a character class guts the line, and the guard cannot see the decline path | 3, 9, 17, 23 |
| B-4 | blocker | `tools/hooks/agent-cap.js:93` | B5 unfixed: ordinary arithmetic raises `dirty`, the fallback truncates at a `//` inside a backtick | 8 |
| B-5 | blocker | `tools/hooks/agent-cap.js:326` | the new `/` ender conflates "regex closed" with "block comment closed" | 20 |
| H-1 | high | `tools/hooks/agent-cap.js:296` | H1's root untouched: a one-character property guard, plus a trailing-dot numeric position | 4, 10, 15 |
| H-2 | high | `tools/hooks/agent-cap.js:414` | the guard's false DENY re-breaks the lens-prompt admit class the build closed | 5, 24 |
| H-3 | high | `tools/codebase-map/map_lib.py:438` | the two regex-start predicates diverge again; a ghost symbol is measurable | 6, 11, 18 |
| H-4 | high | `tools/codebase-map/selftest.py:1399` | the replacement corpus arm has zero discriminating power | 12, 16 |
| L-1 | low | `tools/codebase-map/map_lib.py:499` | a 120-char window re-anchors `_JS_KEYWORD_TAIL`'s start-of-input alternative | 19 |

Exit codes below: **0 = ADMIT**, **2 = DENY**. Three revisions are compared throughout — `tip` =
`26786d70` (the fix), `base` = `55fa6862` (the reviewed tip), `prebase` = `1255d5d1` (the build's own
base).

---

## B-1 — blocker — `tools/hooks/agent-cap.js:414`

**`dirty` disarms every denial rule, so the load-bearing new guard is a fail-OPEN trigger.**

`SWALLOW_GUARD` raises `dirty` at `:414` (and `:799`). `dirty` is folded into `unterminated` at the
return, and all four consumers then swap onto the per-line fallback
`lines.map((l) => stripStrings(l).split('//')[0])` — at `:93`, `:503`, `:508`, `:930` and `:1242`.
`stripStrings` deliberately leaves backticks alone, so that fallback truncates at a `//` living
inside a template literal and the fan-out call after it disappears. `offendingLines`' own comment at
`:86-89` states the rule this breaks: seeing LESS is dangerous for a rule whose findings are denials.

Measured — fresh DENY-to-ADMIT introduced by this commit:

```js
const REF = /\.ref\b/
async function go(D, f) { const u = `docs http://x.dev`; return await parallel(D.map(f)) }
```

tip **0**, base **2**, prebase **2**. Deleting only the first line restores **2** at the tip. The
trigger is a *correctly lexed* regex literal — `prev` is `=`, the accept branch runs, and the guard
fires on its own `\.ref\b` alternative. `--selftest` on that fixture reports `unterminated:true,
dirty:true, clean:false`. The same shape takes rule 3 dark (`await boundedParallel(D, 500)` after the
backtick URL) and rule 5 dark (`M.get(f.ref)`).

The raw-primitive ban is the rule that prevents the ~14-agent burst this hook exists for, and this
commit made the lossy fallback reachable from a one-line regex literal.

**Fix.** A denial rule must never lose reach when a view is distrusted. Either take the UNION for
rules 1/2/3/5 — deny if EITHER the primary or the fallback view shows the token — or build the
fallback so it cannot see less, by blanking backtick spans before the split
(`l.replace(/`[^`]*`/g, '``')` ahead of `.split('//')` in all four expressions). Rule 5's `interp`
second view at `:1269` deliberately keeps backticks and must keep raw `stripStrings`.

**Left-shift gate.** For every deny fixture in the suite, assert that prepending a `dirty`-setting
line (`const RE = /[a-z]\.ref/`) does not change its verdict. Independently, assert that on any line
where `dirty` is set, the fallback view is never a strict subset of the primary view.

## B-2 — blocker — `tools/hooks/agent-cap.js:306`

**The guard's token list is a second, hand-typed copy of the four rules' matchers, and it already
disagrees with two of them.**

```js
const SWALLOW_GUARD = /\b(?:bounded)?(?:parallel|pipeline)\s*\(|\bagent\s*\(|\.ref\b/
```

Executed directly: `boundedParallel(D, 500)` → **false**, `boundedPipeline(t, 5)` → **false**,
`verdictByRef` → **false**; `parallel(work)`, `agent(x)` and `a.ref` → true. The alternation is
lowercase-only, so after `bounded` it needs a lowercase `p`, and matching bare `parallel` fails the
`\b` behind the `d`. `HELPERS` at `:743` hunts exactly `boundedParallel|boundedPipeline`, so the
guard is dead plumbing for rule 3 — the one rule that actually reads the cap number. `BANS` at
`:1247-1254` carries `verdictByRef` as its third entry, an identifier with no dot, uncovered by
`\.ref\b`.

Measured:

| Fixture | tip | base | prebase | control |
|---|---|---|---|---|
| `const n = obj . in / boundedParallel(thunks, 500) / 3` | **0** | 0 | 2 | zero-space `obj.in` → 2 |
| `const z = 1. / boundedParallel(D, 500) / 2` | **0** | 0 | 0 | without `1. /` → 2 |
| `const m = obj . in / verdictByRef / 2` | **0** | 0 | 2 | zero-space `obj.in` → 2 |
| `function h(F) { const n = 1. / 2, verdictByRef = new Map(F), m = 3 / 4; return n + m }` | **0** | 0 | 0 | without `1. /` → 2 |

Two of those are DENY-to-ADMIT regressions still standing against the build's own base. A 500-wide
fan-out passes the rule whose whole job is reading the number, and `--selftest` reports the gutted
view as `dirty:false, clean:true`. Round 1's own left-shift text named `boundedParallel(` explicitly
in the token list; the shipped guard dropped it, and no new arm uses a `boundedParallel(` payload,
which is why 158/0 is green over the hole. The comment above `:306` calls this "ONE list because two
copies of the hunted set is the defect this build spent a unit removing" — it *is* the second copy.

**Fix.** Derive the guard from the rules' own sources instead of retyping them:
`new RegExp([raw.source, HELPERS.source, /\bagent\s*\(/.source, /\.ref\b/.source, ...BANS.map(b => b[0].source)].join('|'))`
(drop the `g` flag or reset `lastIndex`). Minimum fix: make it case-insensitive and add
`verdictByRef`. Verified locally that a case-insensitive guard closes both `boundedParallel`
reproducers and leaves all four tracked `tools/workflows/*.js` harnesses at exit 0.

**Left-shift gate.** An arm asserting `SWALLOW_GUARD` matches every token each of the four rules
matches — iterate `raw`, `HELPERS`, the `agent(` probe and every `BANS` row against a positive
sample and require a guard hit. That arm reds the day a ban is added at `:1249` and not at `:306`.

## B-3 — blocker — `tools/hooks/agent-cap.js:360`

**Round 1's B4 reproduces unchanged, and the new guard structurally cannot reach it.**

`checkDeclinedSpan` counts a backtick, a quote and `/*` as openers (`:359-360`) but not `//`, while
both code-mode readers `break` at `two === '//'` (`:384`, `:766`) with no character-class state. So
`[//]` is a character class to the span scanner and a line comment to the reader: the span scanner
finds no ambiguity, `dirty` stays false, and the reader discards the rest of the line.

Measured — ADMIT at tip, base and prebase alike; this commit did not touch it:

```js
async function go(items, s) {
  if (s) /[//]/.test(s), await parallel(items.map((f) => () => agent({ prompt: f })))
  return 1
}
```

tip **0**, base **0**, prebase **0**. Replacing `[//]` with `[x]` gives **2** at all three.
`--selftest` at the tip returns both views truncated to `  if (s) /[` with
`unterminated:false, dirty:false, clean:true` — a raw `parallel(` and an unbounded per-item `agent(`
fan both go dark with every signal reporting clean.

`SWALLOW_GUARD` is tested only inside `if (closed)` on the ACCEPT branch (`:414`, `:799`), and here
the slash is DECLINED (`prev` is `)`), so the guard is not on this path by construction. The commit's
diagnosis — "a regex span about to be BLANKED is now checked" — is true only of the regex-consumption
path; the `//` break blanks strictly more line and remains unguarded. `git diff` over the range
touches nothing inside `checkDeclinedSpan` except two comment blocks. Legal shapes like
`p.replace(/[//]+/g, '/')` reach it.

**Fix.** Two parts, and part (a) alone is not enough because the line is still admitted through the
truncating fallback. (a) `:360` — `if (raw.slice(k, k + 2) === '/*' || raw.slice(k, k + 2) === '//') opener = true`.
(b) Land it together with B-1's fallback fix, or apply `readJoinAt`'s own doctrine and DENY the line
as unreadable. Separately, run the same `SWALLOW_GUARD` test over the text discarded by the
`two === '//'` break before breaking, so the decline side is at least as visible as the accept side.

**Left-shift gate.** A `[//]` deny fixture with its `[x]` control, plus the invariant that a blanked
or truncated span never contained a token any of the four rules hunts — applied on both branches, not
just the accept one.

## B-4 — blocker — `tools/hooks/agent-cap.js:93`

**Round 1's B5 reproduces unchanged: one line of ordinary arithmetic turns all four rules dark.**

The `/` after `total` declines (identifier `prev`, no keyword tail). `checkDeclinedSpan` scans the
span ` total, "half", total `, sees a quote that *closes* before the candidate closer, sets `opener`,
and returns true — so `dirty` is raised on plain division. That routes all four rules onto
`stripStrings(l).split('//')[0]`, which truncates the next line at the `//` inside `http://example.com`.

Measured:

```js
console.log("pct", done / total, "half", total / 2)
async function go(D) { const p = `docs at http://example.com`; return await parallel(D.map((f) => () => agent(f))) }
```

tip **0**, base **0**, prebase **2** — still a DENY-to-ADMIT regression against the build's own base,
untouched by this commit. Deleting only the arithmetic line restores **2** at the tip, so the
arithmetic is causal. Same root as B-1, different trigger and different status: B-1 is new and fires
on an accepted regex, this one is pre-existing and fires on a declined slash over legal arithmetic.

**Fix.** B-1's remedy (union or backtick-blanking) removes the damage. Independently, stop
`checkDeclinedSpan` counting a `'`/`"` string that CLOSES before the candidate closer as an opener —
that alone removes this trigger.

**Left-shift gate.** For every deny fixture, assert that prepending
`console.log("a", x / y, "b", y / 2)` does not change its verdict.

## B-5 — blocker — `tools/hooks/agent-cap.js:326`

**The new `/` expression-ender conflates two different facts, and a leading block comment is now a
fail-open.**

`prev = '/'` is set both after a regex literal (division follows) and after a block-comment close
(`:447`, `:826` — a regex may legally start). The new clause `'})]/'.includes(prev)` reads both as
division. The commit's own B3 rationale states the conflation as a single fact: "both scanners set
`prev='/'` after a regex literal and after a block-comment close". They are not one fact — a comment
is not an expression.

Measured — fresh DENY-to-ADMIT introduced by this commit:

```js
/* setup */ /[`]/.test(s)
async function go(D) { const p = `docs at http://example.com`; return await parallel(D.map((f) => () => agent(f))) }
```

tip **0**, base **2**, prebase **2**. Deleting only `/* setup */ ` restores **2** at the tip, so the
block-comment prefix alone is the trigger. `--selftest` at the tip reports `unterminated:true,
dirty:true, clean:false`: the declined slash lets the regex's backtick open a phantom template, every
rule drops to the per-line fallback, and the fallback truncates line 2 at the `//` in the URL.

Credit where it is due, measured in the same sweep: the no-comment control
(`/[`]/.test(s)` on line 1) ADMITS at prebase **0** and DENIES at base and tip **2**, so the `/`
clause genuinely closed the fail-open it was written for. It just closed it with a predicate that is
wrong for half its inputs.

`.claude/hooks/agent-cap.js` is byte-identical to the tracked copy and needs the same edit.

**Fix.** Do not reuse `prev` to carry "a regex literal just closed". Keep `/` out of the ender set and
track the regex close in its own flag, leaving the block-comment close at a neutral token that
permits a regex — `if (two === '*/') { mode = 'code'; prev = ';'; i += 2; continue }` at `:447` and
`:826`. Mirror whatever is decided into `_js_resolve_regex_start`, which did not take this clause at
all (see H-3).

**Left-shift gate.** A deny fixture for `/* c */ /[`]/.test(s)` with its no-comment control, plus a
general arm: for every deny fixture, prepending `/* c */ ` must not change the verdict.

---

## H-1 — high — `tools/hooks/agent-cap.js:296`

**H1's root is untouched, and a second accept position was never in the clause set at all.**

The diff gated the keyword test behind `/[A-Za-z0-9_$]/.test(prev)` at `:331`, but `KEYWORD_TAIL` at
`:296` still spells its property-name guard as the one-character class `[^.\w$]`. A space between the
dot and the keyword satisfies it, so `codeText` ending `obj . in ` is an ACCEPTED regex position. The
comment at `:331-332` still claims `obj.in`, `x.of`, `m.delete`, `p.new`, `r.case` coverage — true
only for the zero-space spelling.

A second position escapes every clause: a numeric literal ending in `.` leaves `prev === '.'`, which
matches no clause and falls through `resolveRegexStart`'s final `return true`. `1. / x / 2` is legal
JavaScript and is outside the accepted-ceiling list the comments enumerate (identifier, number,
closing bracket, closing quote, postfix).

Both are measured in B-2's table: `obj . in` and `1. /` each ADMIT where their controls DENY. They
survive only where `SWALLOW_GUARD` happens to fire, and B-2 shows exactly where it does not — two
independent defects composing into a fail-open, which is the shape the guard was added to prevent.

**Fix.** Track a boolean `prevWasDot`, set at the `.` character and cleared by the next non-space
token, instead of encoding the guard as a fixed-width lookbehind over concatenated text. Add the
trailing-`.` numeric position to the expression-ender clauses.

**Left-shift gate.** Deny fixtures for `obj . in / 2`, the line-wrapped `obj.` / `in` form, and
`const z = 1. / 2`. More durable: an arm that takes each existing deny fixture and re-runs it with
one space inserted after every `.`, asserting the verdict is unchanged.

## H-2 — high — `tools/hooks/agent-cap.js:414`

**The guard's false-DENY cost re-breaks the lens-prompt admit class this build spent a unit closing.**

Same root as B-1, opposite direction: where B-1 loses the token, this loses the *blanking*. The
fallback is `stripStrings`, which by design leaves backticks alone, so once `dirty` is raised the
prose inside a template literal is read as code.

Measured — fresh ADMIT-to-DENY on a fully compliant harness:

```js
const BAN = /\[[A-Za-z_$][A-Za-z0-9_$.]*\.ref\]/
const LENSES = [{ slug: 'a' }, { slug: 'b' }]
async function go() {
  const prompt = `Never call parallel(...) directly; route every fan-out through the helper.`
  return await boundedParallel(LENSES.map((L) => () => agent(prompt)), 5)
}
```

tip **2**, base **0**, prebase **0**. The deny message blames line 4 — the governance prompt — as a
raw `parallel()` call. Deleting only the `BAN` line restores **0** at the tip. That is precisely the
class TOOL-aPairedLexer-2's line-aligned view was built to remove, and the denied text is the prompt
this hook's own deny message instructs authors to write.

The guard's own file is its first false positive: `cat tools/hooks/agent-cap.js | node tools/hooks/agent-cap.js --selftest`
now reports `unterminated:true, dirty:true, clean:false`, where the base scanner over the base file
reports `dirty:false, clean:true`. The four tracked harnesses under `tools/workflows/` happen to carry
no such literal today, so the bar shows nothing — the break is one regex literal away.

Combined with B-1, the declared trade is wrong in both directions from the same trigger: a false DENY
on compliant code *and* a false ADMIT of the burst-preventing rule.

**Fix.** Fixing B-1's fallback so it blanks backtick spans turns this false DENY back into a correct
ADMIT, since the fallback would then blank the prompt as the primary view does. Independently, narrow
the guard to spans that plausibly are not patterns — exclude a hunted token preceded by a regex
escape `\`, or require an argument list the rule could actually read.

**Left-shift gate.** Pin the four `tools/workflows/*.js` harnesses as ADMIT fixtures *with* a
`.ref`-bearing regex literal prepended, so a guard that re-breaks the lens-prompt class reds.

## H-3 — high — `tools/codebase-map/map_lib.py:438`

**The H3 parity fix closed one divergence and opened two, in the same commit.**

The diff gave `resolveRegexStart` the `/` expression-ender and `POSTFIX_TAIL`; `_js_resolve_regex_start`
received only the keyword clause. Its docstring at `:429` still reads "Same conservative rule the
JavaScript side states". Measured directly:

| Input | Python | JavaScript |
|---|---|---|
| `prev='/'` | `'y'` (regex start) | `false` (division, `:326`) |
| `prev='+'`, `code_text='const y = i++ '` | `'y'` | `false` (`POSTFIX_TAIL`, `:328`) |

`render_comment_free` sets `prev = "/"` after consuming a regex (`:512`), so `/a/ / 2` and `i++ / 2`
open a phantom span on the Python side only. That is not latent — it changes the rendered output and
invents a symbol. Measured through the real definition rules:

```js
const A = /x/ / 2 /*
export function ghost() {}
*/
export const REAL = () => 1
```

yields `['REAL', 'ghost']`; the control with `i + 1 / 2` yields `['REAL']`. The phantom span swallows
the `/*` opener, so the block comment is never blanked and the commented-out export is read as a
definition. The `i++` variant ghosts identically. This is the exact class H3 was raised for,
re-created on the other side. At the base neither predicate had these clauses, so the two agreed —
the divergence is this diff's.

The map's coverage ratchet is a merge-bar leg, so a ghost key forces an adopter to claim a symbol
that does not exist. The residual paragraph at `enumerate_exports` still discloses only the DIVISION
direction and never says the mis-model can ADD a symbol. `selftest.py` is green because the tracked
corpus holds no such position — green by absence (see H-4).

**Fix.** Port both clauses: `if prev in "})]/": return ""` and a
`_JS_POSTFIX_TAIL = re.compile(r"(\+\+|--)\s*$")` test against `code_text` before the alnum clause.
Whichever way B-5 is decided, mirror it here. If any divergence is deliberate, delete the "Same
conservative rule the JavaScript side states" sentence — a docstring that claims parity it does not
have is worse than none.

**Left-shift gate.** The parity arm round 1 already asked for and this commit did not build: one
shared fixture table of `(prev, code_text)` rows, run through both `_js_resolve_regex_start` and the
JS `resolveRegexStart` via `--selftest`, asserting identical verdicts on every row. That is the only
thing that keeps the next clause from landing on one side alone.

## H-4 — high — `tools/codebase-map/selftest.py:1399`

**A check that could not fail was replaced by another check that cannot fail — in the arm written to
remove that shape.**

`assert seen == unmodelled` compares `render_comment_free` against itself with
`_js_resolve_regex_start` stubbed to `""`. Staged three ways from the repo root, monkeypatching the
predicate and calling `test_render_comment_free_corpus_is_unchanged` directly:

| Model | Arm |
|---|---|
| baseline | PASS |
| deleted (`lambda p, c='': ''`) | **PASS** |
| always-on (`lambda p, c='': 'y'`) | **PASS** |

The reason, measured over the 10 tracked `.js` files: the derived symbol set is **103 under all three
models and equal in every pair**, while the rendered TEXT differs on 2 files (base vs off) and 3
(base vs on). The model demonstrably changes the text and provably never changes the symbol set the
arm compares, because `JS_DEFINITION_RULES` are `^\s*`-anchored and no mis-modelled span in this
corpus moves a statement-leading definition.

Worse, `unmodelled` is produced by the SAME pass with only the predicate swapped, so any defect
outside the predicate cancels out of both sides. The arm's comment claims it makes "the
eight-definition regression the docstring records ... runnable instead of remembered" — that
regression was caused by BLANKING STRING CONTENTS, an axis this arm never varies. Simulated: with
string-content blanking re-introduced into a copy of `render_comment_free`, model-on and model-off
both yield 103 and stay equal, so the arm stays green and loses nothing. It is still remembered.

§7's "stage the break, confirm RED" was not satisfied. This is the left-shift gate for the entire
Python-side regex class, and it is inert.

**Fix.** Assert the axis the docstring names: render the corpus a second time with string and
template contents blanked, and require the modelled configuration's symbol set to be a strict
superset — or pin the eight lost definitions as an explicit fixture. Add a liveness assertion that
the model is exercised at all (`assert any(rendered_on[f] != rendered_off[f] for f in files)` — true
for 2 files today, and it reds if regex modelling is ever bypassed). Then correct the comment to
describe what the comparison actually guards.

**Left-shift gate.** Add H-3's GHOST fixture (`const A = /x/ / 2 /* … */`) and the LOSS fixture to the
compared corpus, so the equality has a shape that actually moves when the model breaks. Then delete
the break and confirm RED before landing.

---

## L-1 — low — `tools/codebase-map/map_lib.py:499`

**A 120-character window re-anchors a start-of-input alternative.**

The call site passes `"".join(out)[-120:]` as `code_text`, so `_JS_KEYWORD_TAIL`'s `^` alternative
anchors to the start of a *window*, not the start of input. The JavaScript side never slices
`codeText`, and its comment at `:293-295` states the invariant explicitly: "The leading alternative is
start of INPUT, not start of line."

Measured: `_js_resolve_regex_start('n', 'const q = myreturn ')` → `''` (correct, division), while
`_js_resolve_regex_start('n', 'return ')` → `'y'`. Same source position, resolved differently purely
by where the slice lands. Reachable through `render_comment_free` when the emitted tail `myreturn` is
followed by exactly 114 whitespace characters — pathological, which is why this is low and why the
"latent mis-model rather than a lost symbol" framing is the honest one. It is a third measured
divergence from a sibling predicate whose docstring claims sameness.

**Fix.** Widen the slice by one and drop the `^` branch whenever the slice is not the whole emitted
text, or pass a code-only accumulator the way the JavaScript side does.

**Left-shift gate.** Folds into H-3's parity arm: run the shared fixture rows through the Python side
with the window applied, and require the same verdict as the unwindowed JS side.

---

## What round 1's findings actually did

Re-measured at the tip rather than taken from `priorFindings`.

| Round-1 id | Commit claims | Re-measured |
|---|---|---|
| B1 `readJoinAt` occurrence ordinal | fixed | Not re-measured by this round and not contested by any lens. |
| B2 keyword-tail ordering | fixed | Holds. The reorder itself is sound; its companion `/` clause is not — B-5. |
| B3 `/` expression-ender | fixed | Half fixed. The regex-close position is genuinely closed (control ADMITs at prebase, DENIES at base and tip). The block-comment position is a new fail-open — B-5. |
| B4 `//` in a character class | not fixed directly | Reproduces at all three revisions — B-3. |
| B5 backtick `//` fallback | not fixed directly | Reproduces; DENY at prebase, ADMIT at base and tip — B-4. |
| H1 `obj . in` | not fixed at root | Reproduces, plus a second untested position — H-1. |
| H2 `POSTFIX_TAIL` | fixed | Fixed on the JS side; not ported to Python — H-3. |
| H3 Python keyword parity | fixed | Keyword clause ported; two new divergences opened in the same commit — H-3. |
| M2 corpus arm cannot fail | fixed | Replaced with another arm that cannot fail — H-4. |

The commit body's claim "OBSERVED RED: all five blocker fixtures ADMIT against the reviewed tip and
DENY after" is false for B4 and B5, both measured ADMIT at the tip.

## Method and what this review did not check

- Exit codes measured by piping `{"tool_name":"Workflow","tool_input":{"script": …}}` into the real
  hook at each of the three revisions; the base and pre-base hooks were extracted with `git show`
  into a scratch dir and run unmodified.
- Every fixture quoted here is `node --check` clean. Every table cell was re-run by this synthesis
  pass, not inherited from a lens.
- Both suites were run at the tip: `158 passed, 0 failed` and `PASS`. **Neither suite fails on any
  finding in this report**, which is the single most important number in it.
- Not checked: B1's `readJoinAt` ordinal fix, the map regeneration, the version bumps
  (`agent-cap 1.12 → 1.13`, `codebase-map 1.6 → 1.7`), the record-side edits under
  `memory/builds/aPairedLexer/`, and `.claude/hooks/scratch-guard.js`. The `.claude/hooks/agent-cap.js`
  copy was confirmed byte-identical to the tracked one and inherits every finding above.
- Not checked: whether any *other* rule beyond 1, 2, 3 and 5 consumes `dirty`, and whether the four
  tracked `tools/workflows/*.js` harnesses would still admit after each proposed fix — verified only
  for the case-insensitive guard in B-2, where all four stayed at exit 0.
