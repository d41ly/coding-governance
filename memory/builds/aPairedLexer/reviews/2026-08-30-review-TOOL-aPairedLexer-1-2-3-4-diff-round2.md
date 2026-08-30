**Serves:** diff-review TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 TOOL-aPairedLexer-3 TOOL-aPairedLexer-4

# Closing diff review round 2 — the four `aPairedLexer` units as one cumulative diff

*Node a, 2026-08-30, round 2. Four Tier-2 units landing as one cumulative diff across three product
commits: `-1` gives `blankLiterals` a mode/dirty signal and has `capFindings` fall back to the
per-line view; `-2` moves rule 1 onto `renderCodeView`; `-3` replaces two-pass comment stripping in
the definition probe with one string-aware pass; `-4` teaches BOTH scanners to model regex literals
and adds a version-parity arm. A parallel fan of primed finder lenses over the two scanners and the
extractor, then skeptics prompted to REFUTE each finding against the source. Every behavioural claim
below is an exit code measured by piping a real `Workflow` payload into the real hook — never a
reading. Every fixture is `node --check` clean under an `async` wrapper, and every fixture, control
and candidate patch cited here was re-run by this synthesis pass rather than inherited from a lens.*

Reviewed range: `14e21399f7dd0559224837a2754fcbf9fc4a754b...1255d5d1ac5ccb84fe3e51f0f59e750658bb70f3` (29 files, +2309/-192; product commits `b3d1ecd8`, `16dfaaef`, `1255d5d1`).

## Verdict: BLOCKED

Counts sit here rather than on the heading, because that token is a closed set and a tally appended
to it turns a structural check into a semantic one.

Review shape: raw 20, confirmed 19, refuted 1, unverified 0, precision 0.95. The 19 confirmed rows
collapse to **13 distinct defects** — two pairs of lenses reproduced the same start-of-input bug, two
reproduced the same cross-check gap, two the same unterminated-quote mask, and two the same stale
inventory. Adjudicated: **5 blockers, 2 highs, 4 mediums, 2 lows.**

**This is the fourth consecutive revision of `agent-cap.js` to ship a fail-open, and the suite is
green.** `bash tools/hooks/agent-cap.test.sh` prints `125 passed, 0 failed` at the tip with every
blocker below live. Four of the five blockers are measured DENY→ADMIT regressions against code that
already shipped, in the only mechanical control this project has against an unbounded agent burst.

The unifying mechanism is stated once here rather than thirteen times below. Both scanners decide
"is this `/` a regex or a division?" by looking at the previous **character**. That decision is wrong
at start of input and wrong after every keyword, and when it is wrong the regex body leaks into code
mode. A leaked backtick opens a phantom template span. **Two** leaked backticks open and close one,
so the span balances, the EOF-only `unterminated` flag never fires, the fallback never runs, and
every line between them is blanked out of the view all four rules read. Unit 4 identified exactly
this and fixed the half of it that `blankLiterals` owns (`dirty`); `renderCodeView` did not get the
same repair, and neither scanner's heuristic was widened past the previous character.

`tools/hooks/agent-cap.js` and `.claude/hooks/agent-cap.js` are byte-identical (`diff` returns
nothing), so every agent-cap row below is carried by the hook wired into this repo's live sessions,
and every fix owes both files — the suite has a mirror-drift arm that reds if only one is patched.

The `codebase-map` unit is the healthier half but is not clean: two regressions, one that loses a
symbol silently and one that invents a symbol that does not exist. `python tools/codebase-map/selftest.py`
is `PASS` at the tip and sees neither.

### The merge bar is RED at the review tip

`python tools/codebase-map/test_codebase_map.py` exits **1** with `FAIL test_generated_artifacts_are_fresh`
/ `STALE symbols.json`. That is the `codebase-map coverage + freshness` leg in `tools/gate-legs.json`
(`subject: repo`, **no `guard` key**, so it runs on every bar including a records-only one), and it is
not among the five legs `fea287b9` records as knowingly red. See D10.

| # | Sev | Site | Defect | Regression? |
|---|-----|------|--------|-------------|
| D1 | BLOCKER | `tools/hooks/agent-cap.js:295`, `:613` | `prev = ''` plus `'})]'.includes('')` making start of input a DIVISION position — the whole hook goes dark | standing hole; unit 4 claimed to close it |
| D2 | BLOCKER | `tools/hooks/agent-cap.js:305`, `:628` | The regex/division test reads the previous CHARACTER, so `return /.../` mis-lexes — the commonest regex position in real JS | yes, 1.9 denies |
| D3 | BLOCKER | `tools/hooks/agent-cap.js:355` | `renderCodeView.unterminated` is still EOF-only — the exact signal unit 4 declared the root cause and replaced next door | yes, 1.9 denies |
| D4 | BLOCKER | `tools/hooks/agent-cap.js:732` | Rule 3's `!clean` fallback discards the paren-safe view the rule is built on, so a `)` in a prompt eats the cap argument | yes, 1.9 and 1.10 deny |
| D5 | BLOCKER | `tools/hooks/agent-cap.js:742` | The two-view cross-check skips any name only ONE view binds, so a prose `const K = 5` still governs a caller-settable width | yes, 1.9 and 1.10 deny |
| D6 | HIGH | `tools/hooks/agent-cap.js:366` | `fanoutFindings` got no cross-check at all — the defect D5 fixes next door, left standing in rule 2 | no |
| D7 | HIGH | `tools/codebase-map/map_lib.py:464` | `render_comment_free`'s phantom template emits comment text VERBATIM, so a commented-out `export` is indexed as live | yes |
| D8 | MEDIUM | `tools/codebase-map/map_lib.py:583` | `_has_top_level_comma` returns `False` on an unclosed quote, masking the multi-declarator `MapError` into a silent symbol drop | yes |
| D9 | MEDIUM | `tools/hooks/agent-cap.js:1050` | Rule 5's fallback keeps template contents, so the ban table is applied to lens PROSE — a legal workflow denied, at a misleading line | yes, fail-closed |
| D10 | MEDIUM | `memory/map/generated/symbols.json:3112` | Not regenerated after `1255d5d1` added a test function — merge bar leg RED | yes |
| D11 | MEDIUM | `tools/hooks/agent-cap.test.sh:1098` | The parity arm resolves "previous kit" to an intra-build revision, so it compares broken against broken | new gate, born blind |
| D12 | LOW | `tools/hooks/agent-cap.js:46`, `:85` | Two ceiling statements the same diff made false, in the file's own header and in the comment defending a load-bearing fallback | yes |
| D13 | LOW | `tools/hooks/agent-cap.js:681` | `endMode` is returned and read by nobody — unit 1 added it, unit 4 superseded it with `clean` | yes |

---

## The blockers

### D1 — BLOCKER — `tools/hooks/agent-cap.js:295` and `:613` — start of input is a DIVISION position, and the whole hook goes dark

`let prev = ''`, and `'})]'.includes('')` returns **`true`** in JavaScript. So at start of input the
guard `!'})]'.includes(prev)` is **false**, the regex branch never fires, and the first `/` in a
script is read as division. The comment at `:286-287` lists "or start of input" among the positions
where a regex IS recognised. It is the one position where it never is.

`prev` is also never advanced past a whole-line `//` comment (the `two === '//'` branch `break`s
without touching it), so a leading comment does not rescue it.

**Reproduced.** This script is `node --check` clean and exits **0** at the tip:

```js
// tier-2 review harness
/[`]/.test('a')
async function run(work) {
  const verdicts = {}
  for (const f of work) verdicts[f.ref] = f
  return await boundedParallel(work, 500)
}
/[`]/.test('b')
```

Both `/` are read as division, the two backticks open and close a phantom template, and lines 3–7 are
blanked in both views. A raw-primitive check, an unbounded per-item fan, a cap of **500** and a
`.ref`-keyed join are all admitted at once. `renderCodeView` reports `unterminated=false`;
`blankLiterals` reports `endMode=code dirty=false clean=true`. Every fallback signal reports healthy.

**Control:** prepending a bare `;` (so `prev = ';'`) flips the same script to exit **2**. The empty
`prev` is the sole cause.

A syntax-clean variant with the regex as the first code token behaves as a straight regression —
exit **2** at 1.9, exit **0** at 1.10 and the tip:

````js
// pick out the fenced blocks the finders emitted
/^```/.test(args.report);
const r = await parallel(D.map(d => () => agent(d)));
/^```/.test(args.report);
````

**Why the suite cannot see it:** every regex arm in `agent-cap.test.sh` writes the literal as
`const a = /[`]/` — always after `=`, where `prev` is never empty. The version-parity arm cannot see
it either: 1.10 admits too (D11).

**Fix.** `let prev = ';'` at `:295` and `:613`. **Verified by this pass:** both fixtures above flip to
exit **2**, and with the same two lines applied to BOTH copies `bash tools/hooks/agent-cap.test.sh`
stays `125 passed, 0 failed`. (Patching only `tools/hooks/` reds the mirror-drift arm, which is that
arm working.)

**Left-shift gate.** Add both scripts as deny fixtures. Then add a *structural* arm rather than only
instances: assert `renderCodeView('/x/').code[0].trim() === ''` — a one-line assertion that start of
input is a regex position, which no future rewrite of the heuristic can quietly lose.

### D2 — BLOCKER — `tools/hooks/agent-cap.js:305` and `:628` — the regex/division test reads the previous CHARACTER, so `return /.../` mis-lexes

`!/[A-Za-z0-9_$]/.test(prev)` cannot distinguish `return` from an identifier. Every keyword that
cannot end an expression — `return typeof case in of instanceof new delete void throw yield await` —
therefore puts the following `/` in a division position. `return /.../` is the commonest regex
position in real JavaScript.

**Reproduced — DENY→ADMIT against the shipped 1.9.** Exit **2** at 1.9 (`addc6169`), exit **0** at
1.10 and the tip:

```js
function hasTickA(s) { return /`/.test(s) }
const r = await parallel(D.map(d => () => agent(d.p)))
function hasTickB(s) { return /`/.test(s) }
```

And the realistic shape — a workflow that parses a markdown report. Same result, exit **2** at 1.9,
exit **0** at the tip:

````js
const md = await read('report.md')
function isFence(l) { return /^```/.test(l) }
const D = md.split('\n').filter(isFence)
const r = await parallel(D.map(d => () => agent(d)))
function isEnd(l) { return /```$/.test(l) }
````

This is not the accepted ceiling being restated. The comment at `:284-289` excuses the ambiguity as
"after an identifier, a number, or a closing bracket" — an honest description of a *narrow* residual.
The character test makes it far wider than the sentence describes, and then the same comment claims
"the `unterminated` fallback still covers what this cannot", which two balanced phantom backticks
provably defeat (D3).

**Why the suite cannot see it:** the arm `rule1: a raw primitive between TWO regex literals holding
backticks still denies` (`agent-cap.test.sh:1025`) pins the identical two-regex shape with both
regexes after `=` — an *unambiguous* position that IS treated as a regex. It exercises the arm the
fix covers and never the arm it does not. That is this project's own §7 rule, `gate the CLASS, not
the instance`, broken in the commit that cites it.

**Fix.** Decide on the previous **token**, not the previous character. Keep a trailing-word buffer
beside `prev` and treat `/` as a regex start when the preceding word is one of those keywords. Write
it **once** as a shared predicate called from both `:305` and `:628` — the file already carries the
regex block twice, and one view knowing something the other does not caused two of the three prior
fail-opens (`TOOL-aPairedLexer-5`).

**Verified by this pass:** a keyword-aware predicate applied to both scanners flips both fixtures to
exit **2** and leaves every other suite arm green (measured with the version-parity arm skipped, so
the count reads `124 passed, 0 failed` rather than 125 — the skip announces itself).

**Left-shift gate.** Both scripts as deny fixtures, plus a table-driven arm asserting the code view
blanks `return /re/`, `typeof /re/`, `case /re/:`, `throw /re/` and `yield /re/` — the class, not the
two instances that happened to be found.

### D3 — BLOCKER — `tools/hooks/agent-cap.js:355` — `renderCodeView` kept the EOF-only signal unit 4 declared the root cause and replaced next door

`return { code: out, unterminated: stack.length > 0 || mode !== 'code' }`. That answers only "what
mode was I in when the file ran out". `blankLiterals` was given `dirty` for precisely this reason —
its own comment at `:677-680` says `clean` must mean "nothing was blanked that should not have been",
not merely "the file did not end mid-construct". `renderCodeView` never got the same half, so rules 1
and 2 read a view that can be silently gutted.

**This is independent of D2, and the proof matters for fix ordering.** Applying *both* lexer fixes
above still admits this script, which is `node --check` clean, exits **2** at 1.9, and exits **0** at
the tip:

```js
const a = 1
if (a) /`/.test(s)
const r = await parallel(D.map(d => () => agent(d.p)))
if (a) /`/.test(s)
```

The `/` follows `)`, which is a *genuinely* ambiguous position the file deliberately declines — and
declining is defensible. What is not defensible is declining **silently**. The two mis-lexed
backticks balance, `unterminated` stays false, the `:92` fallback never fires, and the raw
`parallel(` between them is blanked out of the view. The residual the ceiling comment says the
fallback covers is exactly the residual the fallback cannot reach.

**Fix.** Give `renderCodeView` the per-line half: when a `/` is DECLINED as a regex and a backtick
occurs later on that same line, set a `dirty` flag, and return
`unterminated: stack.length > 0 || mode !== 'code' || dirty`. Both consumers (`offendingLines:92`,
`fanoutFindings:366`) then fall back to the per-line view, which is the shipped 1.9 verdict and
cannot regress in either direction. Unit 2's prose-in-a-lens-prompt win is unaffected — those lines
carry no ambiguous slash.

**Left-shift gate.** The script above as a deny fixture, and an arm asserting
`renderCodeView(s).unterminated === true` for a script containing one declined-slash-plus-backtick
line. Pin the *signal*, not only the verdict, so a later refactor that keeps the verdict by accident
still reds.

### D4 — BLOCKER — `tools/hooks/agent-cap.js:732` — rule 3's fallback discards the one mechanism the rule is built on

`const code = _bl.clean ? _bl.code : lines.map((l) => stripStrings(l).split('//')[0])`. `stripStrings`
(`:77`) blanks `''` and `""` and leaves backticks alone. So the fallback view retains template
CONTENTS, a `)` inside a prompt short-circuits `joinCall`, the second argument disappears, and the
helper's own `cap = 5` default is read as governing.

`blankLiterals`' docstring at `:604-608` says a `(` inside a prompt string unbalancing a forward paren
join is *"the one mechanism this rule is built on"*. The fallback throws that mechanism away.

**Reproduced — exit 2 at BOTH 1.9 and 1.10, exit 0 at the tip:**

```js
function ok(s) { return /won't/.test(s) }
async function boundedParallel(thunks, cap = 5) {
  const out = []
  for (let i = 0; i < thunks.length; i += cap) out.push(...await parallel(thunks.slice(i, i + cap))) // gov:bounded-fanout
  return out
}
const r = await boundedParallel(pick(`x)y`), 50)
```

**Control:** delete line 1 — the only `dirty` trigger — and the tip DENIES with *"the cap argument at
the `boundedParallel()` CALL SITE is 50, above the 5-agent cap"*. Unit 4's `dirty` repair is precisely
what converts a correct denial into an approval.

**Not merely downstream of D1/D2.** With both lexer fixes applied, the same script with the trigger
rewritten to an ambiguous position (`const a = 1` / `if (a) /won't/.test(s)`) still exits **0** at the
patched hook and **2** at 1.9 and 1.10. The fallback is independently wrong.

**The trigger is live in this repo.** Instrumenting `blankLiterals` over the tracked `.js` files,
`tools/workflows/drift-audit-state.js` — a shipped harness — already returns `dirty=true`, so rules 3
and 5 judge this repo's own drift-audit workflow on the degraded view today.

**Fix.** A view rule 3 cannot do its job on is not a safer view than a blank page — it is a different
fail-open. Keep `_bl.code` for the join and paren work, which is what it is for, and use the fallback
view ONLY to supply `intConsts` bindings (which is the *only* thing the `-1` rationale actually
argued for). Alternatively DENY when `joinCall` returns different text under the two views, naming
the ambiguity.

**Left-shift gate.** The script and its control as a paired arm — the paired form is the point, since
the fixture alone would pass under a fix that simply stopped setting `dirty`.

### D5 — BLOCKER — `tools/hooks/agent-cap.js:742` — the cross-check exempts exactly the case that fabricates a cap

```js
if (!_bl.clean) {
  for (const [k, v] of intConsts(_bl.code).consts) {
    if (consts.has(k) && consts.get(k) !== v) consts.set(k, Math.max(consts.get(k), v))
  }
}
```

The `consts.has(k)` guard means a name the clean view does not bind is never visited. The comment at
`:740-741` is explicit that this is deliberate — *"A name only ONE view binds is not a disagreement"*.
Deliberate is not correct here: for a CAP, a name only the view the file has already declared
untrustworthy binds is not evidence, it is fabrication.

**Reproduced — exit 2 at BOTH 1.9 and 1.10, exit 0 at the tip:**

```js
function ok(s) { return /won't/.test(s) }
const PROMPT = `
  Harness note: the width is set with
  const K = 5
  before the fan is built.
`
const K = args.width
const thunks = [t1, t2, t3]
const r = await boundedParallel(thunks, K)
```

`_bl.code` blanks the template, so it binds no `K` at all; the reconciliation loop has nothing to
compare and the prose value stands. The real bound is `args.width` — a caller-settable knob, the
exact "knob wearing a constant's clothes" this rule refuses at `:146-154`. 1.10's denial names the
same rule and line: *"the cap argument … is `K`, which this file cannot resolve"*.

**Control:** deleting the `/won't/` line makes the tip DENY. **And independent of D1/D2:** with both
lexer fixes applied and the trigger moved to an ambiguous position, the script still exits **0**.

**Fix.** Invert the merge rule so "one view binds it" is a disagreement, not an exemption. When
`!_bl.clean`, iterate the UNION of both key sets: a name both views bind to different integers keeps
the max (as now); a name only ONE view binds is **deleted** from `consts`, so `boundedK` refuses it
and the deny message names the unresolvable form. Also sweep `\b(?:const|let|var)\s+(\w+)\s*=` over
`_bl.code` and delete every name the clean view SAW but refused to resolve — a declaration the
trusted view examined and rejected is stronger evidence than one the untrusted view invented. The
`rule3: an exposed const resolves the cap and the script admits` arm should be re-baselined as a deny
with a clearer message; resolving a cap out of a view the file has declared untrustworthy is the
fail-open direction.

**Left-shift gate.** The script as a deny fixture, plus its mirror — a real reassignment the fallback
RETAINS because `blankLiterals` deleted it. Two directions, one arm each.

---

## The highs

### D6 — HIGH — `tools/hooks/agent-cap.js:366` — rule 2 never got the cross-check rule 3 got

`fanoutFindings` calls `const { consts } = intConsts(code)` on the same kind of possibly-fallback view
with **no** cross-check. `intConsts` matches anywhere in the text and later binding wins, so a
fabricated `const K = 5` still lowers a real `const K = 500`.

**Reproduced at the tip (exit 0), with a control:**

````js
function isFence(l) { return /^```/.test(l) }
const K = 500
/*
 historical note: the verify stage used to hardcode const K = 5
*/
const groups = chunk(args.findings, Math.ceil(args.findings.length / K)) // gov:fixed-verifiers
const r = await boundedParallel(groups.map((g) => () => agent(g)), 5)
````

Delete only the block comment and it exits **2** with *"groups carries gov:fixed-verifiers but its
bounded split names a cap which this file does not show to be bounded"*. The prose `K = 5` buys the
pass: `boundedK` blesses a 500-wide chunk, which is one agent per finding.

Not a regression — 1.9, 1.10, the tip and both candidate lexer patches all admit it. It is the exact
defect the diff fixed next door in rule 3 and left standing here, which is why it is high rather than
medium: the impact is D5's, the novelty is not.

**Fix.** Hoist D5's corrected merge into one helper both rules call. Same code, same rationale, two
consumers instead of one.

**Left-shift gate.** The script and its control as a rule-2 arm — and, better, an assertion that
`fanoutFindings` and `capFindings` resolve the SAME const table for a given script, so the two rules
cannot diverge again.

### D7 — HIGH — `tools/codebase-map/map_lib.py:464` — a phantom template makes `render_comment_free` resurrect commented-out exports

`render_comment_free` models strings and templates but **no regex literal**. A regex holding a
backtick opens a template span, and the string/template arm emits `text[i:j+1]` VERBATIM when the
span closes — so real comments inside it are never blanked and a commented-out `export` is scanned as
live code.

**Reproduced end-to-end through `enumerate_exports`.** This `.ts` file yields `['GHOST', 'RX', 'T']`
at the tip and `['RX', 'T']` at the base `14e21399`:

````ts
export const RX = /`/;
/*
export const GHOST = 1
*/
export const T = `x`;
````

The old `_BLOCK_COMMENT_RE` DOTALL sub was string-blind and therefore blanked that comment. This is a
**third** regex-borne direction and is not one of the two ceilings pinned by
`test_enumerate_exports_regex_borne_comment_opener`: that arm pins two LOSSES; this one silently ADDS
a symbol that does not exist. It corrupts the committed `symbols.json` that a coverage ratchet then
demands be claimed — the map's own "a claim naming a dead key" failure, arriving through the
extractor instead of through a dossier. The docstring's safety claim, *"The only bytes this function
removes are inside a comment, so it cannot delete a definition"*, is about deletion and does not
cover un-blanking.

Adopter-facing rather than local: this repo's map has no `.ts` layer, so its own `symbols.json` is
unaffected today.

**Fix.** Blank comment text *inside* a template span the same way it is blanked outside one, so a
phantom span can never RESURRECT a comment. That is strictly safer than trying to model regexes here
and cannot lose a real definition, because a definition inside a template is not one.

**Left-shift gate.** Add the file above as a third arm on
`test_enumerate_exports_regex_borne_comment_opener`, asserting `GHOST` is absent. The arm name already
promises the class; it currently pins two of its three directions.

---

## The mediums

### D8 — MEDIUM — `tools/codebase-map/map_lib.py:583` — an unterminated quote masks the multi-declarator raise

`_has_top_level_comma` walks characters tracking `quote`, and ends with a bare `return False`. An
apostrophe inside a regex opens a quote span the walk never closes, so the depth-0 comma is consumed
as string content and the multi-declarator `MapError` — which the docstring calls *"the completeness
guarantee"* and whose own text calls the alternative *"the green-by-absence hole"* — never fires.

**Reproduced at both levels.** `_has_top_level_comma("export const RE = /don't/, SECOND = 2")` returns
`False` at the tip and `True` at `14e21399`. End-to-end, `export const RE = /don't/, B = 2` raises
`MapError` at the base and returns `['RE']` at the tip, with `B` gone and no error.

Introduced by this diff's D6 quote tracking. The sibling pass already models the right posture — *"an
unterminated span is abandoned rather than swallowed"* — so this is an inconsistency, not an accepted
ceiling: neither the function's documented ceiling (a bare `<`/`>`) nor the new D6 paragraph mentions
it.

**Fix.** Fail closed: change the trailing `return False` to `return bool(quote)` — a line this walk
cannot finish parsing is a line it cannot prove single-declarator. **Verified by this pass:** the
regex-apostrophe case returns `True`, the URL case D6 fixed
(`export const LINK = "https://x.com/?a=1,b=2"`) still returns `False`, `export const A = 1, B = 2`
still returns `True`, and `python tools/codebase-map/selftest.py` still `PASS`es.

**Left-shift gate.** One arm beside the existing D6 query-string arm asserting
`_has_top_level_comma("export const RE = /don't/, B = 2") is True`, so the two directions are pinned
together and neither can be traded for the other.

### D9 — MEDIUM — `tools/hooks/agent-cap.js:1050` — rule 5's fallback applies the ban table to lens PROSE

Same fallback expression as rule 3, opposite failure direction. `stripStrings` leaves backticks alone,
so once anything anywhere sets `dirty`, the BANS table is run over template contents — refuting the S2
comment three lines above, which describes the `blankLiterals` view as *"a deliberate NARROWING"*
precisely because the old view matched the retired identifier inside a string.

**Reproduced — exit 0 at 1.9 and 1.10, exit 2 at the tip**, with no ref-keyed join anywhere:

```js
function ok(s) { return /won't/.test(s) }
const brief = `
Do not build a map keyed by f.ref — the retired verdictByRef shape is banned.
`
const r = await agent(brief)
```

The reported offending line is the prose on line 3; the actual cause is the apostrophe on line 1. An
operator is told line 3 is a ref-keyed join. Fail-closed and cheap to recover from, hence medium — but
one fallback expression now has two opposite failure directions, and neither is the direction its own
rule wants.

**Fix.** Blank backtick spans in the fallback:
``raws.map((l) => stripStrings(l).replace(/`[^`]*`/g, '``').split('//')[0])``.

**Left-shift gate.** Two arms: the script above must ADMIT, and the same script with a genuine
`byRef[f.ref] = v` line must still DENY.

### D10 — MEDIUM — `memory/map/generated/symbols.json:3112` — stale artifact, merge bar RED

`1255d5d1` added module-level `def test_enumerate_exports_regex_borne_comment_opener()` to
`tools/codebase-map/selftest.py:1272` without regenerating the inventory.

**Verified at the tip with a clean tree.** `python tools/codebase-map/test_codebase_map.py` exits **1**
with `FAIL test_generated_artifacts_are_fresh` / `STALE symbols.json`. Running
`python tools/codebase-map/gen_map.py --write` produces exactly **5 insertions in one file** — the one
missing row for that function — and the tree was restored afterwards.

The sibling arms added by the same unit (`test_enumerate_exports_string_borne_punctuation`,
`test_render_comment_free`) ARE present, so the regeneration ran mid-unit and was never repeated after
the last arm landed. §1's DoD states it directly: claim edits regen the generated artifacts in the
same commit.

**Fix.** `python tools/codebase-map/gen_map.py --write`, commit, before landing.

**Left-shift gate.** This one is already gated and the gate is already red — the gap is the DoD, not
the bar. The cheapest structural close is a `pre-commit` fast leg that runs `gen_map.py --check` when
the commit touches a file the extractors read.

### D11 — MEDIUM — `tools/hooks/agent-cap.test.sh:1098` — the parity arm resolves its baseline to an intra-build revision

The arm walks `git log --format=%H -n 60 -- agent-cap.js` for the first commit carrying a *different*
`KIT_AGENT_CAP_VERSION`. **Walked it directly:** `16dfaaef` = 1.11, `b3d1ecd8` = 1.10,
`addc6169` = 1.9. The first differing version is 1.10 at `b3d1ecd8` — the feat commit of THIS build,
never released. The last version an adopter holds is 1.9.

Raised from the finder's LOW because the impact is measured, not stylistic: D2's and D3's fixtures
exit **2** at 1.9 and **0** at BOTH 1.10 and 1.11. Adding either as a deny fixture would compare
broken against broken, and the arm would still print `ok version parity: none of 59 deny fixtures
admits at 1.11 while denying at 1.10`. The arm's declared limitation — *"cannot catch a fail-open
shipped in the same version as the fixture"* — does not cover this: the fail-open is in a different,
*prior* version, which is exactly the case it claims to bound. A gate that reports coverage it does
not have is the green-by-absence class §7 names, in the gate written to end this build's own defect
class.

**Fix.** Resolve the baseline against the merge-base with the default branch rather than the first
differing version in `git log`, so a multi-unit build is compared against what was actually shipped.
Keep the existing skip-announces-itself branch for adopter trees with no history.

**Left-shift gate.** A meta-arm: assert the resolved `prev_ver` is not reachable from `HEAD` without
crossing the merge-base — i.e. that the baseline is a *released* revision. The arm should red on its
own resolution before it replays a single fixture.

---

## The lows

### D12 — LOW — `tools/hooks/agent-cap.js:46` and `:85` — two ceiling statements this diff made false

The module header still reads *"block comments naming the primitive are NOT [stripped] — still trips
the guard (benign, fail-closed)"*, and `offendingLines`' comment at `:85` still reads
*"`renderCodeView` models no regex literal and no block comment"*. Unit 4 added an explicit regex
branch at `:305-321` and a `block` mode at `:304`/`:348-351`, so both are inverted.

**Measured:** a script whose only `parallel(` sits in a `/* … */` block exits **0** at the tip and **2**
at 1.9, and the suite pins the new behaviour (`rule1: a primitive named in a block comment now ADMITS
(ceiling retired by the regex mode)`). The dossier at `memory/map/features/agent-cap.md:162` was
corrected in this diff; the source was not. One question, two answers, and the SOURCE holds the wrong
one.

The `:85` half is the one that matters. A maintainer reading it believes the `:92` fallback exists for
a reason that no longer applies — which is precisely the reasoning that would delete the guard D1 and
D3 show is still load-bearing.

**Fix.** Rewrite `:44-48` to state the ceilings that actually hold, and `:84-89` to say the fallback
covers an unterminated template or block span — plus the ambiguous-slash case once D3 is fixed.

**Left-shift gate.** This is the class round 1 already left-shifted for its own D8
(`rationale-names-a-consumer-that-does-not-exist`), reproduced in the header of the file the build is
about. Run `python tools/memory-tree/gotchas.py --for-diff` on the *rationale* comments of any file
whose behaviour a diff inverts, and treat a ceiling sentence adjacent to changed control flow as a
required reviewer check.

### D13 — LOW — `tools/hooks/agent-cap.js:681` — `endMode` is returned and read by nobody

`return { code: out, endMode: mode, dirty, clean: … }`. Grep across `tools/`, `.claude/` and the gate
scripts finds `endMode` at `:627` (comment), `:677` (comment) and `:681` (the return) — and nowhere
else in code. Both consumers read `clean`: `capFindings` at `:726`/`:731` and `scanJoinFindings` at
`:1049`/`:1050`. Unit 1 added it; unit 4 superseded it with `clean` and left it behind, along with the
`:677` comment that still reads as if a consumer keyed on it.

Cosmetic, but it is two signals in the safety-critical lexer, one of them inert, in the file where a
future reader repairing the fallback has to pick one.

**Fix.** Drop `endMode` from the returned object; keep `clean` and `dirty`. Reword `:677` to describe
`clean` alone.

**Left-shift gate.** The dead-path checker this repo already ships (`tools/dead-path-waivers.txt` and
its scanner) should cover returned-but-unread object keys on the hook files, or the row goes on the
§10 checklist as a documented manual check for `agent-cap.js` specifically.

---

## Fix ordering, because the fixtures interact

Fixing the lexer (D1 + D2) removes the *trigger* used by the D4, D5, D6 and D9 fixtures above, which
would make those four look fixed when they are not. **Verified:** with a `prev = ';'` sentinel and a
keyword-aware predicate applied to both scanners, the D4 and D5 fixtures rewritten with an
ambiguous-position trigger (`if (a) /won't/.test(s)`) still exit **0**, D6's still exits **0**, and
D9's still exits **2**. D3's fixture also still exits **0**.

Land D3 (the `dirty` half for `renderCodeView`) before or with D1 and D2. It is the one repair that
holds whatever the heuristic decides, because it makes a declined slash *announce itself* rather than
relying on a lexer that is right often enough.

## What was checked and found clean

- `python tools/codebase-map/selftest.py` — `PASS` at the tip, including the two new regex-borne
  ceiling arms. It does not see D7 or D8.
- `bash tools/hooks/agent-cap.test.sh` — `125 passed, 0 failed` at the tip, with all five blockers
  live. Stated as evidence, not reassurance.
- `tools/hooks/agent-cap.js` vs `.claude/hooks/agent-cap.js` — byte-identical; the suite's mirror-drift
  arm works (it red when this pass patched only one copy).
- The D6 URL fix (`export const LINK = "https://x.com/?a=1,b=2"` no longer raising) is real and is
  preserved by the D8 fix.
- `render_comment_free` was checked for the *deletion* direction the docstring claims: over the
  tracked JS it removes only comment bytes. The defect is the un-blanking direction, which the
  docstring does not cover.

## Method

Fixtures were driven through `node tools/hooks/agent-cap.js` with a real `{"tool_name":"Workflow",
"tool_input":{"script":…}}` payload built by the same `json.dumps` path `agent-cap.test.sh`'s `js()`
helper uses — exit 2 DENY, exit 0 ADMIT. Baselines came from `git show 14e21399:tools/hooks/agent-cap.js`
(1.9) and `git show 16dfaaef~1:tools/hooks/agent-cap.js` (1.10). Candidate patches were applied to
copies outside the tree; the two occasions the working tree was modified (a suite run and a
`gen_map.py --write`) were both restored and `git status --porcelain` verified empty afterwards.
`map_lib.py` was exercised by importing both revisions side by side and calling `enumerate_exports`
on temp `.ts` files, so every extractor claim is end-to-end rather than helper-level.
