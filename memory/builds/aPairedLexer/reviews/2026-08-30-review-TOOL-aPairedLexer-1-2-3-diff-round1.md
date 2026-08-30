**Serves:** diff-review TOOL-aPairedLexer-1 TOOL-aPairedLexer-2 TOOL-aPairedLexer-3

# Closing diff review round 1 — the three `aPairedLexer` units in one product commit

*Node a, 2026-08-30, round 1. Three units landed as one product commit `b3d1ecd8`: `-1` makes `blankLiterals` report the mode its state machine finished in and has `capFindings` fall back to the per-line view when that is not `code`; `-2` points `offendingLines` at `renderCodeView` with the same fallback, retaining the block-comment ceiling deliberately; `-3` replaces block-then-line comment stripping in `scan_js_definitions` with `render_comment_free`, one pass that tracks strings without blanking them, and deletes `_BLOCK_COMMENT_RE`. A parallel fan of primed finder lenses over the two scanners and the predecessor's own review corpus, then skeptics prompted to REFUTE each finding by re-deriving it against the source. Nearly every confirmation below carries an exit code measured by driving the real hook with a real payload, not a reading.*

Reviewed range: `14e21399...HEAD` (product commit `b3d1ecd8`; the two preceding commits in the range are spec revisions).

## Verdict: BLOCKED

Counts sit here rather than on the heading, because that token is a closed set and a tally appended to it turns a structural check into a semantic one.

Review shape: raw 15, confirmed 15, refuted 0, unverified 0, precision 1.00. The 15 confirmed rows collapse to **8 distinct defects** — four lenses independently reproduced the same rule-1 fail-open, and two reproduced the same rule-3 one. Adjudicated: **2 blockers, 3 highs, 1 medium, 2 lows.**

Both blockers are measured REGRESSIONS against the shipped 1.9 hook, in the only mechanical control this project has against unbounded agent fan-out, and both were introduced by the units that exist to close exactly this class. The build's spec audit found 8 blockers including two fail-opens; the prompt's instruction to assume more remain was correct.

The shape is the same in both: a repair moved a rule from a stateless per-line view onto a line-carrying lexer, and guarded the move with an **EOF-only signal**. `unterminated` and `endMode` both answer "what mode was I in when the file ran out", and neither answers the question the fallback actually needs — "did I blank a span I cannot prove was a literal". An EVEN number of stray backticks opens and closes the span, the flag never fires, the fallback never runs, and the blanked span is invisible to a denial rule. Every new test arm in this commit uses exactly ONE backtick, so the suite is green over the half that was not fixed. That is the project's own `gate the CLASS, not the instance` rule (§7), broken in the commit that cites it.

`tools/hooks/agent-cap.js` and `.claude/hooks/agent-cap.js` are byte-identical (verified with `cmp`), so every agent-cap row below is carried by the mirror too and every fix owes both files.

The `codebase-map` unit is materially healthier. Its behaviour was checked directly: over all 10 tracked JS files the new one-pass strip loses zero definitions against the old two-pass strip, gains 8, and preserves line count on every file; `gen_map.py --check` is green. One adopter-facing regression and two doc-rot rows, nothing structural.

| # | Sev | Site | Defect | Regression? |
|---|-----|------|--------|-------------|
| D1 | BLOCKER | `tools/hooks/agent-cap.js:92` | Rule 1's fallback is EOF-only, so an EVEN backtick count blanks the span and admits a raw primitive | yes, 1.9 denies |
| D2 | BLOCKER | `tools/hooks/agent-cap.js:707` | Rule 3's fallback view feeds `intConsts` unblanked, so prose or a comment rebinds a real cap downwards | yes, 1.9 denies |
| D3 | HIGH | `tools/hooks/agent-cap.js:656`, `:707` | `endMode` is EOF-only too, so rule 3's fallback misses every spuriously opened-and-closed span | no |
| D4 | HIGH | `tools/hooks/agent-cap.js:656` | `blankLiterals`' unpaired-quote branch swallows the rest of the line and still reports `code` | no |
| D5 | HIGH | `tools/hooks/agent-cap.js:1003` | Rule 5 computes `endMode` and discards it, keeping the fail-open the sibling unit just closed | no |
| D6 | MEDIUM | `tools/codebase-map/map_lib.py:598` | Removing the `//` split exposes string contents to a string-blind comma check — false `MapError` | yes |
| D7 | LOW | `tools/codebase-map/map_lib.py:433` | `render_comment_free`'s line-count rationale is checkable and false; echoed twice in the selftest | no |
| D8 | LOW | `tools/codebase-map/map_lib.py:574` | `enumerate_exports`' ceiling paragraph documents the deleted two-pass strip and omits the new pass's real limit | no |

---

## D1 — BLOCKER — rule 1 admits a raw primitive between two stray backticks

`tools/hooks/agent-cap.js:92` (mirrored at `.claude/hooks/agent-cap.js:92`). Corroborated independently by lens findings 1, 4, 7 and 11 — four reproductions, two spellings each.

`offendingLines` now reads `renderCodeView(script)` and falls back to the per-line view only on `v.unterminated`. `renderCodeView` models neither a block comment nor a regex literal, so the first stray backtick pushes `tmpl` and the **second pops it**: the scan ends in `code` mode with an empty stack, `unterminated` is `false`, the fallback never runs, and every line between the two backticks was appended to nothing.

Measured, both spellings, exit code taken from the real hook driven with a `Workflow` payload:

- two block comments each holding one backtick, straddling `const out = await parallel(thunks)` — **1.9 exits 2, HEAD exits 0**
- two regex literals, ``const tickA = /[`]/`` … ``const tickB = /[`]/``, straddling the same call — **1.9 exits 2, HEAD exits 0**
- same with `pipeline(`, and with `await parallel(findings.map((f) => () => agent(promptFor(f))))` — same result
- controls behave: no backticks → 2 on both; ONE backtick → 2 on both, because `unterminated` fires

`node --check` accepts every fixture, so this is not a syntax-error-only shape. `renderCodeView`'s own printed output on the regex-pair script is ``code=["const tickA = /[`","","`]/"]`` with `unterminated:false` — the fan-out line is the empty string.

Rule 2 is no backstop: `fanoutFindings` has read the same view since `TOOL-aLexedStripper-5` and gates on the same flag, so it was already blind here. Rule 1 was the last rule denying these scripts, and this unit moved it onto the same blind view. Rules 3 and 5 do not reach them (no helper call, no join), so `main()` runs to `process.exit(0)` and a ~14-agent unbounded burst lands green. This is also a one-line deliberate bypass of the fan-out cap.

Not covered by the file's stated residual either: the comment at `:299` scopes the known hole to a regex literal with an ODD backtick count. This is the even case, and it is recorded nowhere — the dossier residual at `memory/map/features/agent-cap.md:163-170` says such a backtick "never closes", which is true only for an odd count.

**Fix.** Two parts, both verified.

1. Teach `renderCodeView` a comment mode that copies `/* … */` text VERBATIM — so the deliberately retained block-comment ceiling still denies — but does not let backticks inside it toggle template mode: in code mode, `if (two === '/*') { mode = 'cmt'; res += '/*'; i += 2; continue }`, plus a `cmt` branch copying chars until `*/`. Verified: the block-comment repro flips 0 → 2 and all 114 behavioural arms stay green. A mis-detected opener then only ADDS apparent code, which is the fail-closed direction.
2. The regex half needs a second signal. `unterminated` is the wrong question; the right one is "did I enter template mode from a position I cannot prove was a value position". Set a sticky flag when a backtick opens `tmpl` on a line that also carries a `/`-delimited literal candidate, and treat that flag exactly like `unterminated` at `:92`. Cheaper and honest alternative if that is deferred: state the even-count case as a named residual beside the odd-count one and pin it with a ceiling arm — but that is a DEFERRAL of a live regression, not a fix, and it must be an owner call.

**Left-shift gate.** Add both even-count fixtures to `tools/hooks/agent-cap.test.sh` beside the existing odd-count pair, which pins one instance of the class rather than the class: `rule1: a raw primitive between TWO backtick-bearing regex literals denies` and `… between TWO backtick-bearing block comments denies`. Runs on the `agent-cap self-test` leg. Stronger and cheaper than either: a **parity arm** asserting that for a fixed corpus of deny-expected fixtures, no script that denies at the previous kit version admits at this one — that gates the whole "a view repair lost a denial" class rather than these two shapes, and it would have caught both blockers here.

---

## D2 — BLOCKER — a fabricated `const` in prose or a comment rebinds a real cap downwards

`tools/hooks/agent-cap.js:707`. Corroborated by lens findings 2 and 5.

Rule 3's new `endMode !== 'code'` fallback feeds `lines.map((l) => stripStrings(l).split('//')[0])` to `intConsts`. That view strips neither template contents nor block comments, and `intConsts`' `\b(?:const|let|var)\s+ID\s*=\s*(\d+)\s*$` matches text anywhere in it. Later binding wins the `forEach`, so a `const K = 5` written in PROSE overrides the real `const K = 500` and the guard resolves a cap it should have refused.

Measured, three spellings, all `node --check` clean, all **1.9 exits 2 / HEAD exits 0**:

- `const K = 500` … `await boundedParallel(L.map((x) => () => agent(x)), K)` … a template whose prose line reads `Lens A: report file:line. Never let the cap read const K = 5` … ``const tick = /[`]/`` to force `endMode='tmpl'`
- the same with the fabricated const inside a `/* doc … */` block comment plus a trailing unterminated `/*`
- the same with a terminated template and the trailing regex supplying the unterminated state

Deleting only the `const K = 5` prose flips HEAD back to exit 2, so the prose alone is what admits the 500-wide fan. 1.9's `blankLiterals` blanked the template contents, so the text never reached `intConsts` and K stayed 500.

The in-code comment at `:702-706` concedes exactly one direction — an EXPOSED binding resolving a cap that was unresolvable, which REMOVES a finding. It does not concede a FABRICATED binding that contradicts and overrides a real over-cap value, which flips a correct denial of a 500-wide bound into an approval. The one new arm pinning the removing direction uses a genuine `const K = 5` statement, not prose shadowing a larger real binding. A lens-prompt template whose prose happens to end in `const <NAME> = <int>` silently raises the resolved cap, with no diff and no warning.

**Fix.** Do not let the fallback view bind integers on its own. Keep it for locating call sites, then cross-check the bindings: when `_bl.endMode !== 'code'`, also run `intConsts(_bl.code)` and for any name the two views bind to DIFFERENT integers, take the larger (fail-closed) or drop the name entirely so the cap goes unresolvable and denies. Verified both ways: every repro above flips 0 → 2, and the shipped `rule3: an exposed const resolves the cap and the script admits` arm stays green, because the blanked view binds nothing there.

**Left-shift gate.** An arm per direction on `agent-cap self-test`: `rule3: prose inside a template cannot lower a real cap` and `rule3: a const inside a block comment cannot lower a real cap`. Generalize with a property arm — for any fixture, appending a comment or template line must never REMOVE a finding. That is the invariant the whole "the per-line view can only add findings" argument rests on, and it is currently asserted in a comment rather than tested.

---

## D3 — HIGH — `endMode` reports the mode at EOF, not whether a span was blanked

`tools/hooks/agent-cap.js:656`, consumed at `:707`. Corroborated by lens findings 9 and 12.

Same root shape as D1, different function, different flag, different rule — and fixing either leaves the other open, so this is reported separately under the project's own gate-the-class rule rather than folded in. `blankLiterals` returns `mode`, the mode the scan FINISHED in, so a construct that spuriously OPENS and then CLOSES mid-file returns `endMode === 'code'` with a blanked span, and rule 3's new fallback never fires on the very class it was added for.

Measured, all exit 0 at HEAD, all `node --check` clean, control (`const L = [1,2,3,4,5]` + `await boundedParallel(L.map((x) => () => agent(x)), 500)`) exits 2:

- wrapped in ``const a = /[`]/`` … ``const b = /[`]/`` → exit 0
- `const re = /[/*]/` above, an ordinary `/* ordinary */` below → exit 0
- ``const a = /[`]/`` … cap 500 … ``const b = /[`]/``, identical script with `/[x]/` → exit 2

Not a regression — 1.9 admits these too — but the diff presents `endMode` as the completeness check for this view, and it does not cover its own query. Nothing in the code or the comments names this as a residual, unlike `renderCodeView`, which names its odd-backtick one at `:299`.

**Fix.** Make `endMode` report "ever entered a span I cannot justify" rather than "mode at EOF": `blankLiterals` models block comments but not regex literals, so set a sticky flag when a backtick opens `tmpl` on a line also carrying a `/`-delimited literal candidate, and treat that flag exactly like `endMode !== 'code'`. Same signal D1 needs, one function over — build it once and let both consumers read it.

**Left-shift gate.** An even-count arm beside the three existing `rule3:` arms, which today all use a single unterminated opener. If the fix is deferred, it becomes a documented ceiling in `memory/map/features/agent-cap.md` beside the odd-count residual, WITH a suite arm pinning it as a ceiling the way `rule1: a primitive named in a block comment still denies (retained ceiling)` pins its own — a deferral with no arm is a ceiling nobody can tell from a bug.

---

## D4 — HIGH — an unpaired quote swallows its line and still reports `code`

`tools/hooks/agent-cap.js:656`.

`blankLiterals`' code-mode quote branch consumes the rest of the line and appends a closer the source never had, leaving `mode === 'code'`. So the fallback that exists to catch exactly this class never fires for it, and the comment's claim that the machine "reports the mode it FINISHED in" is false for a line-swallow.

Measured: `if (/won't/.test(x)) { await boundedParallel(thunks, 500) }` exits 0 on both 1.9 and HEAD — `blankLiterals` returns `code=["const thunks = items","if (/won''",""]` with `endMode='code'`, the call site is gone, and a cap of 500 is admitted. The same line with `/wont/` exits 2 on both, so the apostrophe is the whole mechanism.

Not a regression, and it is the narrowest of the three fail-opens here — but it is the defect class rule 1 just fixed, sitting in the signal this unit introduced, and `renderCodeView` already repaired this exact branch for its own scan at `:313-325`. `blankLiterals` was left behind. One machine got the fix, its sibling did not, in the same file.

**Fix.** Mirror `renderCodeView`'s rule: require a matching closer before blanking, and leave an unpaired quote as ordinary text.

```js
let e = i + 1
while (e < raw.length && raw[e] !== q) e += raw[e] === '\\' ? 2 : 1
if (e >= raw.length) { res += ch; i++; continue }
```

Verified: the repro flips 0 → 2, with no change on the same script without the regex.

**Left-shift gate.** Arm `rule3: an apostrophe in a regex literal does not swallow a cap` on `agent-cap self-test`. Better, because it gates the class rather than the instance: a shared arm asserting the two lexers agree on a fixture corpus — any script where `renderCodeView` and `blankLiterals` disagree about which lines are code is a bug in one of them, and this repair would have been caught for free.

---

## D5 — HIGH — rule 5 computes `endMode` and throws it away

`tools/hooks/agent-cap.js:1003`.

`scanJoinFindings` was rewritten in this same commit to `const code = blankLiterals(script).code`. The `endMode` that `TOOL-aPairedLexer-1` added at `:656`, and that `capFindings` consumes 350 lines earlier, is computed, returned, and dropped at the call site. So rule 5 still fails open below an unterminated template literal or block comment — the exact class this build closed for rule 3, one function away.

Measured: `const verdicts = {}` / `verdicts[v.ref] = v` denies (exit 2). Prefix `const t = `never closed` or `const c = /* never closed` and both 1.9 and HEAD exit 0. Same for the Map spelling (`m.set(f.ref, verdict)` → 2 bare, 0 with the opener). `blankLiterals` carries `mode` across lines, so every line below the opener is empty and the three-entry BANS table matches nothing. The second view does not rescue it: `views` only adds `${...}` spans from the raw line, and a bare `verdicts[v.ref] = v` has none.

The obvious refutation — that an unterminated literal is a syntax error so nothing runs — does not hold. `blankLiterals` models no regex literal either, so a LEGAL script opens the same hole: ``const re = /[`]/`` and `const re = /[/*]/` above the same join both exit 0 at HEAD and pass `node --check`.

Rule 5 is a denial rule, and ref-keyed verdict joins silently collapse findings. A harness author who opens a template and never closes it turns the rule off with no diff.

**Fix.** The ternary that already exists verbatim eight hundred lines up:

```js
const _bl = blankLiterals(script)
const code = _bl.endMode === 'code' ? _bl.code : raws.map((l) => stripStrings(l).split('//')[0])
```

The interpolation second view already reads the raw line and is unaffected. Note the cross-check from D2 applies here too if the fallback view is ever fed to a resolver — it is not today.

**Left-shift gate.** Two arms mirroring the rule-3 pair: `rule5: the bracket ban below an unterminated backtick denies` and `… below an unterminated BLOCK comment denies`. The durable version is one table-driven arm applying the same "unterminated opener above the trigger line" prefix to EVERY rule's deny fixtures, so a rule added later inherits the coverage instead of needing someone to remember it.

---

## D6 — MEDIUM — a URL in an `export const` now raises a false `MapError`

`tools/codebase-map/map_lib.py:598`.

Deleting `line = raw.split("//", 1)[0]` from `enumerate_exports` exposes string CONTENTS to `_has_top_level_comma`, which is bracket-depth-aware but string-blind. Reproduced end to end: a `.ts` file containing `export const LINK = "https://x.com/?a=1,b=2";` raises `MapError: unmodelled multi-declarator export (capturing only the first name is the green-by-absence hole — split it or use a real parser)` — naming a second declarator that does not exist.

Confirmed as a regression introduced by `b3d1ecd8`: `_has_top_level_comma` on the full line is `True`, while the pre-diff pipeline's `raw.split('//',1)[0]` yielded `export const LINK = "https:` on which it is `False`, so the old code matched const-export and emitted the correct id. `render_comment_free` deliberately emits string contents verbatim (verified byte-identical), so the string is now fully exposed.

The inline comment at `:594` shows the split was removed to avoid truncating inside a string literal. That is correct as far as it goes — the author did not account for that truncation having been the thing masking the downstream string-blindness. An unintended trade, not a design choice.

Reachable for adopters: `map_extractors.template.py:92` documents exactly this `enumerate_exports` usage for a web-ts layer, a query-string URL is ordinary there, and the codebase-map coverage check is a merge-bar leg. So an adopter gets a red bar with a false diagnosis. This repo's own tree does not hit it, which is why the regen in this commit is clean and the leg is green here.

**Fix.** Make `_has_top_level_comma` skip quoted spans — it already walks the string char by char, so track `'` / `"` / `` ` `` the way `render_comment_free` does and ignore commas inside. Do not reinstate the `//` split; the diff was right to remove it.

**Left-shift gate.** An arm on `codebase-map kit selftest` asserting `enumerate_exports` returns `LINK` for `export const LINK = "https://x.com/?a=1,b=2"`. The new selftest exercises `render_comment_free` directly and never reaches `enumerate_exports`, so this whole path is currently uncovered — the arm is worth adding for the coverage alone. Broaden it to a small table of string-borne punctuation (`,`, `//`, `/*`, `{`) so the string-blindness class is gated rather than this one URL.

---

## D7 — LOW — the line-count invariant is justified by a contract that does not exist

`tools/codebase-map/map_lib.py:433`, echoed at `tools/codebase-map/selftest.py:1237` and `:1273`. Corroborated by lens findings 6, 10 and 15.

The docstring says line count is preserved "because the caller reports `file:line` and `symbols.json` is committed". Neither half is true. `render_comment_free` has exactly two callers (`:519` in `scan_js_definitions`, `:596` in `enumerate_exports`) and both build rows of exactly `{id, kind, file}`; the committed `memory/map/generated/symbols.json` has 703 rows whose key union is exactly `{file, id, kind}` — no line field. Grepping `tools/codebase-map/*.py` for line reporting returns nothing outside this claim and the two selftest comments repeating it; every `MapError` interpolates `{layer}: {rel}` or the stripped text, never a line.

The invariant IS load-bearing, for the reason stated correctly 160 lines down at `:590-593`: `JS_DEFINITION_RULES` are `re.M` with `^\s*` anchors and `enumerate_exports` iterates `splitlines()` with `marker_re.match`, so a merged line pushes a definition out of statement-leading position. That reason appears nowhere in the docstring or in the arm that guards it. A maintainer who checks the stated contract finds it absent at the definition site AND at the test, and can delete the line-count arm as vestigial — removing the only guard on the reason that is real.

Behaviour is fine, hence LOW. Two answers to one question in one file is the problem.

**Fix.** Restate the rationale as the statement-leading / `splitlines()` contract, and drop the `file:line` claim from the docstring and both selftest comments. One fact, in the place that owns it.

**Left-shift gate.** Not gateable as prose. It goes on the §10 recurring-class checklist as *a docstring stating a checkable rationale must name a consumer that exists* — the class here is a comment that survives the code it described, which this same diff produced twice (see D8).

---

## D8 — LOW — the `enumerate_exports` ceiling paragraph describes the deleted machine

`tools/codebase-map/map_lib.py:574`.

The docstring sits in the UNCHANGED region of the diff while the body it describes was replaced. Its ceiling text — "comments are stripped naively (`/* */` spans and trailing `//`)" — names the two-pass strip this commit deleted. `render_comment_free` is string-aware, so neither half is how comments are stripped now.

More useful than the staleness: the paragraph is headed "Ceilings (documented, not silent)", and it omits the new pass's actual ceiling. `render_comment_free` models no regex literal, so `/^https?:\/\//` still truncates its line at the `//`, and `export const RX = /a\/*b/;` opens a block-comment span that a later `*/` closes — returning only `RX` and SILENTLY dropping the following `export const KEEP = 1;`. That is a green-by-absence loss, the exact class this function's raise-contract exists to prevent, under a heading promising documented ceilings. Both are pre-existing rather than introduced here, which is why this is LOW and not higher; the finding is omission, not regression.

The sibling claim at `:505` is fine — "stripped the same way `enumerate_exports` strips them" is accurate now that both route through the shared function.

**Fix.** Replace the ceiling sentence with one pointing at `render_comment_free` and naming its real limit: no regex-literal model, so a `//` or `/*` inside a regex still reads as a comment opener, and a definition after a regex-borne `/*` can be silently dropped. One statement, in the function that owns it.

**Left-shift gate.** An arm on `codebase-map kit selftest` pinning the regex-borne `/*` case as a CEILING — assert the known-lost export is lost, so a future parser upgrade trips the arm and gets the docstring updated with it. That is the project's own pattern from `rule1: a primitive named in a block comment still denies (retained ceiling)`, applied here.

---

## What round 2 must clear

Both blockers, and the shared root beneath D1/D3: an EOF-only signal cannot answer "did this view blank something it cannot justify". Repairing `unterminated` and `endMode` separately will produce two half-fixes and a third round. Build the sticky "entered an unjustifiable span" flag once, in both lexers, and let `:92`, `:707` and `:1003` read it.

D5 is one ternary and should ride along rather than wait — it is the same class, already solved, one function away.

The suite is the other half of the exit condition. Every arm this commit added uses a single backtick, which pins the instance and not the class, and the parity idea in D1 is the cheapest thing on this page: a corpus of deny-expected fixtures asserted against the previous kit version would have caught both blockers before either shipped.

Round 2's exit condition is a strictly falling confirmed-blocker count. This round sets the ceiling at 2.
