**Serves:** diff-review TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-5 TOOL-aLexedStripper-6

# Closing diff review — round 2, scoped to the FIX for round 1

*Node a, 2026-08-30, round 2. Tier-2 review of the fold that answers round 1, NOT of the build again.
Priming: round 1's report at `memory/builds/aLexedStripper/reviews/2026-08-30-review-TOOL-aLexedStripper-1-2-5-6-closing-diff-round1.md`,
whose confirmed findings are not re-reported except where this fold claims to have closed them. Every
row below was reproduced against the wired hook or the installed module before it was written down.*

Reviewed range: `eb76532eac8969da6ba67ad67abe9848e34a28df...HEAD` (HEAD = `b96856b7`; the fix is the
single product commit `df86368b`, plus `b96856b7` which files `TOOL-aLexedStripper-7`).

Round 2.

## Verdict: BLOCKED

Two blockers, both in `tools/hooks/agent-cap.js`, both the same fail-open round 1 filed. Round 1's
blocker 1 was answered with the smaller repair round 1 explicitly measured as insufficient and told
the build not to ship; round 1's blocker 2 was not answered at all, because the refutation measured a
fixture shape in which the defect is invisible. Both are measured today as a DENY at `19d9b328`
becoming an ADMIT at HEAD, on legal JavaScript, through the wired `PreToolUse` command.

`diff -q tools/hooks/agent-cap.js .claude/hooks/agent-cap.js` is clean and
`.claude/settings.json:9` runs that mirror, so the live guard in this tree admits an unbounded
verify-stage fan today and every adopter takes it on the next re-pull.

The `codebase-map` half of the fold is genuinely better and is not blocking. Round 1's finding 6
(the Python prefix backscan) is fully closed in both directions, its finding 7 (two dead regexes) is
closed by deletion, and its finding 5 is closed in the EOF-terminal spelling only.

## Review shape

- raw 16 · confirmed 11 · refuted 5 · unverified 0 · precision 0.69
- confirmed by severity, as adjudicated here: 2 BLOCKER · 1 HIGH · 1 MEDIUM · 1 LOW
- confirmed blockers: 2

The 11 confirmed filings are presented as **5 rows**. Three merges, because the same defect arrived
from more than one lens and double-listing would overstate how many distinct things are wrong: ids
1+8+12 are one defect, ids 2+5+9 are one defect, ids 7+13+15 are one defect. Every filing id appears
on its row.

One severity moved from its filing, stated on the row: **filing 4 was HIGH and is adjudicated
BLOCKER**, because it is the same measured fail-open on the same control as row 1, and round 1
adjudicated the identical defect a blocker. Nothing about it got smaller; only the record's belief
about it did.

Precision 0.69 against round 1's 0.65 on the same target. Two of the five refutations were of
findings that re-filed round-1 rows this fold genuinely closed, which is the outcome a round-2 scope
should produce.

## Confirmed findings

### BLOCKER — 2

---

#### 1. `tools/hooks/agent-cap.js:340` — the fold shipped the repair round 1 measured as insufficient, so a regex-borne `/*` closed by a later ordinary `*/` still blanks the fan and raises no flag

*(filings 1, 8, 12 — one defect)*

The fold changed `unterminated: stack.length > 0` to `unterminated: stack.length > 0 || mode !== 'code'`
at `:340`. That closes the EOF-terminal variant and is a real improvement. It cannot close the
variant round 1 named, because in that variant no mode outlives the scan: the `/*` inside a regex
literal opens block mode at `:300`, block mode blanks every line under it, and an *ordinary*
`/* … */` later in the same file hits `:328` and restores `mode = 'code'`. At EOF the stack is empty
and the mode is `code`, so the widened flag reads false, `fanoutFindings:348` keeps the blanked view,
and rule 2 is handed a script with the fan-out erased out of it.

**Measured.** Fixture, legal JavaScript (`node --check` clean):

```js
const MAX_VERIFIERS = 5
const re = /a\/*/
const all = args.everything
for (const f of all) out.push(await agent(f.prompt))
/* an ordinary block comment later in the same file */
```

| revision | exit |
|---|---|
| `19d9b328` (the shipped hook, pre-build) | **2 — DENY** |
| `eb76532e` (the fail-open this build introduced) | 0 — ADMIT |
| HEAD (after the fold that claims to fix it) | **0 — ADMIT** |
| `.claude/hooks/agent-cap.js`, the wired `PreToolUse` command | **0 — ADMIT** |

Probed directly, `renderCodeView` returns `unterminated=false` and renders lines 3-6 as empty
strings — the `for (const f of all) out.push(await agent(f.prompt))` fan is simply not in the view.
The control with `const re = 1` in place of the regex exits 2 at HEAD, naming `L4` and its
braceless-loop fan, so the ADMIT is caused solely by the parse bug. Rule 1 does not catch it either:
these fans use `Promise.all`/a loop, not the `parallel|pipeline` primitive.

This is the identical fixture round 1 published as row four of its table, beneath the sentence *"Do
not ship the smaller-looking repair."*

**Fix.** Round 1's actual remedy: delete the block branch from `renderCodeView` — the
`if (two === '/*') { mode = 'block'; i += 2; continue }` at `:300` and its `else` arm at `:327-330` —
so `/*` stays ordinary characters exactly as the per-line `stripStrings` view rule 2 was calibrated
against. No flag can observe the closed-block case even in principle, so `mode !== 'code'` cannot be
made sufficient and pushing `'block'` onto the stack has the same hole. Keep the widened flag anyway;
it is harmless and it closes the EOF variant on its own. Mirror into `.claude/hooks/agent-cap.js`.
Note that `blankLiterals:605` carries the same branch and is out of this diff's scope — it has no
`unterminated` flag at all, so if rule 3 is ever given a fallback the same argument applies there.

**Left-shift gate.** Three arms in `tools/hooks/agent-cap.test.sh`, each staged RED against the tip
before it lands: a fan below `const SEP = /[/*]+/g`; the closed-block fixture above; and one
structural arm that greps the body of `renderCodeView` and reds if it contains `'/*'` at all. The
first two pin two spellings, the third pins the CLASS against the next well-meaning re-addition,
costs one line and cannot drift.

---

#### 2. `tools/hooks/agent-cap.js:302-307` — an unpaired quote still swallows the rest of its line; the refutation that closed this measured a shape in which the defect is invisible

*(filing 4, promoted from HIGH — round 1's blocker 2, deliberately not folded)*

`spec-TOOL-aLexedStripper-5.md:153-155` records this class as REFUTED: *"four fixtures were run and
all four DENY at both BASE and HEAD, because this file's quote handling mirrors `stripStrings`' own
and therefore cannot regress against it."* Both halves of that are wrong.

The mechanism half first. `stripStrings` at `:70` uses regexes that require a matching quote, so it
leaves an unpaired-quote line **intact**. `renderCodeView` at `:302-307` does the opposite: it walks
`while (i < raw.length && raw[i] !== q)`, runs off the end of the line, and then appends a synthetic
closing quote at `:307` that the source never had. The two do not mirror each other; they differ in
precisely the direction that loses code. That difference is also why the fallback view still denies —
which is what the four counter-fixtures were actually measuring.

The measurement half. The swallow completes within one line, so it only changes the verdict when the
fan-out sits on the SAME line as the quote. I reproduced both shapes:

```js
const all = args.findings
if (/won't/.test(args.s)) await Promise.all(all.map((f) => agent(f.prompt)))
```

| revision | exit |
|---|---|
| `19d9b328` | **2 — DENY** |
| `eb76532e` | 0 — ADMIT |
| HEAD | **0 — ADMIT** |
| `.claude/hooks/agent-cap.js` | **0 — ADMIT** |

`renderCodeView` renders line 2 as `if (/won''` with `unterminated=false`: the whole fan is erased and
no fallback fires. The control with `won't` spelled `wont` exits 2 at HEAD. Move the same fan one line
down and it denies at every revision — which is the shape the four counter-fixtures must have had,
and is why the class read as closed. One apostrophe inside a regex literal, on the line that carries
the fan, is the entire cost of entry.

**Fix.** Treat a quote as a string opener only when its partner is found on the same line: scan ahead
for the unescaped partner first, and on end-of-line without one, emit the remainder of the line
verbatim. Leaving the quote characters in the view is harmless — rule 2 counts `agent(` calls and
receiver shapes, not quotes. This is `stripStrings`' own behaviour, which is what the refutation
believed was already true. Mirror into `.claude/hooks/agent-cap.js`, and delete the refutation clause
from the spec changelog (row 5).

**Left-shift gate.** Gate the class, not the spelling: feed `renderCodeView` a single line holding an
unpaired quote followed by known text and assert the rendered line still contains that text. That is
the dropped-tail invariant and it survives any future rewrite of the quote branch. Add the `/won't/`
fixture and a `/['"]/` twin, each with the fan on the SAME line, staged RED first — the same-line
placement is the load-bearing part of both arms and should be stated in their names.

---

### HIGH — 1

---

#### 3. `tools/hooks/agent-cap.test.sh:837` and `tools/codebase-map/selftest.py:1091` — not one of the three code fixes in this fold landed with a regression arm, and the two arms it did add exercise a different rule

*(filings 7, 13, 15 — one defect)*

`§7`: *a new gate is not landed until its failing case has been observed.* Three behaviour changes
shipped here and none of them has an arm.

- **`agent-cap.js:340`, the widened flag.** `grep 'unterminated\|/\*\|renderCodeView'` over
  `tools/hooks/agent-cap.test.sh` returns exactly four hits: `:816`, a `/*` closed on its own line
  inside a pre-existing arm; `:828`, a comment; and `:831-832`, the pre-existing unterminated-backtick
  arm. No fixture in the suite ends a scan in block mode. Filing 13 measured that reverting only
  `|| mode !== 'code'` leaves the suite at **98 passed / 1 failed**, and the single failure is the
  `.claude` file-parity arm rather than a functional one. *I confirmed the structural half by
  inspection but did NOT re-run the reverted suite to completion — my run exceeded a two-minute
  bound and was killed; the working tree was restored and verified clean.* The structural half is
  sufficient on its own: with no arm that ends a scan outside code mode, nothing can observe the flag.
- **The two arms the fold DID add** (`:837-871`) are rule-2 prose fixtures over a stray `)` driving
  `topLevelArgs` depth negative. Neither contains a `/*` or an unpaired quote, so neither reaches
  `renderCodeView`'s mode handling at all. *Correction to filing 13, which claimed both were green at
  every revision: the arm at `:843` exits 2 at `19d9b328` and 0 at HEAD, so that one WAS observed
  RED. The other was not, and says so in its own comment. This does not touch the primary claim.*
- **Both `map_lib` fixes.** `git show df86368b -- tools/codebase-map/selftest.py` is an 8-line diff
  and it is the corpus guard alone. The `test_identifier_tokens_per_language` case table at `:1091`
  gained no row for `${ fn('{') }` and none for the prefix scoping, though its own docstring says the
  `absent` column *"is what stops this test being satisfied by doing no work at all"* and round 1
  prescribed exactly those rows. Both fixes are real behaviour changes — verified by hand that
  `typeof"${leak}"` no longer captures `leak`, that `alive`/`s` are no longer swallowed, and that
  `v = f"{unclosed` no longer leaks the next line — so a later edit to `_string` or to the
  `if triple:` guard silently restores each leak.

This is not a bookkeeping complaint. It is the direct reason rows 1 and 2 above survived a fold aimed
at them: the fold's own comment at `:333-339` asserts the class is closed, and nothing in the suite
could contradict it.

**Fix / left-shift gate.** The two are the same thing here. Stage each RED against the tip first,
then land it: the three `agent-cap` arms from row 1 and the two from row 2; the in-function template
fixture from row 4 in the per-language case table with its prose word in the `absent` column; and the
`typeof"${leak}"` pair — over-capture in `absent`, its under-capture twin asserting `alive` present.
All of those constructs are verified to behave correctly at HEAD and to leak at `eb76532e`, so each
one is a genuine RED-then-GREEN and not a fixture written to pass.

---

### MEDIUM — 1

---

#### 4. `tools/codebase-map/map_lib.py:709-724` — the interpolation walk is still bounded by EOF rather than by the string's own delimiter, so the new `closed` flag closes only the rarer half of round 1's finding 5

*(filings 2, 5, 9 — one defect)*

The fold added `closed` at `:708` and made the emit conditional at `:723-724`. That correctly kills
the run-to-EOF variant. It does not bound the walk: `while k < n` at `:709` still runs to end of
**file**, and `:711` still counts any `{` toward `depth` including one inside a quoted string within
the replacement field. So a `'{'` in the field bumps depth, the field's own `}` is consumed as the
decrement, and the walk continues until some *later* depth-0 `}` — which sets `closed = True` and
emits everything in between as code. `closed` is evidence that some `}` exists downstream, not that
the interpolation closed.

**Measured against the installed module.** JavaScript, in a function body, which is the ordinary
shape:

```js
function build(name) {
  const s = `${ name.replace('{', '') }`
  // PROSE that must never be indexed
  return s
}
```

returns `PROSE be indexed must never that` in the identifier set — the function's own closing brace
supplies the depth-0 close. The control with `'x'` in place of `'{'` returns only
`AFTER build const function name replace return s x`. Python leaks the same way as soon as one stray
`}` follows: round 1's exact fixture is now clean (`BRACE alpha def f return`), but append
`# PROSE from a comment must never reach the index }` and it returns
`PROSE a comment from index must never reach the`. Reachable on the live scan path, not just in the
selftest.

Stays MEDIUM, for round 1's reason: `build_reference_index` feeds a fan-in ranking and a WARN, never
a gate, and its docstring declares it deliberately fail-open. No gate verdict moves. What does move
is the comment at `:720-722`, which asserts this over-capture class is closed.

**Fix.** Round 1's remedy, both halves of which were skipped. Stop the inner walk at an unescaped
`delim` at depth 0 — a replacement field cannot outlive its string, so reaching the delimiter means
not-closed — and skip quoted spans when counting `depth` so a `'{'` inside the field is not read as
nesting. While there, `:724` should use `len(interp[1])` rather than `+ 1`; both profiles close on a
one-character `}` today, so this is correctness-by-construction rather than a live bug.

**Left-shift gate.** Add the in-function JS fixture above to the `test_identifier_tokens_per_language`
case table with `PROSE` in the `absent` column, and the `f"{'{'}"`-plus-stray-`}` Python twin beside
it. That negative column is exactly the direction this defect arrives in, it already exists, and the
fold added nothing to it (row 3).

---

### LOW — 1

---

#### 5. `memory/builds/aLexedStripper/spec/2026-08-30-spec-TOOL-aLexedStripper-5.md:152` — the rev-2 changelog records both round-1 blockers as resolved, and both records are false

*(filing 11)*

Two sentences, both measurably wrong in the safety-optimistic direction:

- `:151-152` — *"Reproduced, then fixed by reporting `stack.length > 0 || mode !== 'code'`. S1 is
  unchanged in intent and the fallback is now reached from any surviving mode."* The clause about
  surviving modes is technically true and beside the point: the counterexample in row 1 is a mode
  that does **not** survive. The paragraph it sits in says the blocker is fixed. It is not.
- `:153-155` — the refutation of blocker 2, refuted in turn by row 2 above.

This is the durable record the next reviewer and any adopter read when deciding whether
`renderCodeView` needs a regex model. Round 1's finding 4 confirmed two other copies of the same
answer — `memory/map/features/agent-cap.md:168` (*"The residual is precision, not safety"*) and the
hook header at `:284-286` (*"it cannot regress in either direction, because it IS the shipped
behaviour"*) — and both are still unrepaired at HEAD. That round-1 row is **not re-reported here**;
what is new is that the fold added a third copy, so there are now three durable records giving one
answer, all wrong the same way, with no fourth to arbitrate.

**Fix.** After rows 1 and 2 land, rewrite this changelog entry to what is then true: the flag widened
to cover every mode surviving to EOF, AND the `/*` branch was deleted so a regex-borne opener cannot
blank code in the first place, AND the quote branch stops synthesizing a closer. Name the
closed-block variant explicitly — it is the one that has now been missed twice.

**Left-shift gate.** Do not gate the trio; delete two of them, per round 1's own prescription. The
hook header and the spec changelog should point at `memory/map/features/agent-cap.md` for the
residual rather than restating it, which is §6's rule and removes the thing that drifts. If a
restatement survives, `tools/check-agent-cap-restatement.sh` is the existing home for a byte
comparison.

---

## Checked and clean

Named in the review brief, exercised, nothing found. Stated so a green here is not read as an
unexamined area.

- **Does the widened `unterminated` flag deny any legal script?** No. It is strictly wider than the
  old flag, and widening it only routes a script to the per-line `stripStrings` fallback, which is
  the verdict the shipped hook already returned. There is no path on which the new flag denies
  something the old one admitted. The full suite is 99 passed / 0 failed at HEAD. The flag's problem
  is that it is too narrow, not too wide.
- **Is the bounded interpolation walk correct at the string boundary?** It is correct at the boundary
  it was given — end of file. It was never given the string's own delimiter, which is row 4. The
  EOF-terminal case it *was* written for genuinely works: `v = f"{unclosed` followed by
  `s = "hello NOT_CODE world"` no longer leaks `NOT_CODE hello world`.
- **Did the corpus-arm guard introduce a way for the arm to pass without measuring?** Not in this
  tree. `repo_root()` resolves to the worktree root here, the
  `coding-governance-agents.template.md` marker is present, and I ran
  `test_identifier_tokens_corpus_recall()` to completion with no SKIP line printed — it measured. The
  guard is a correct fix for round 1's finding 3 first half (git-ness → this-repo-ness). Its second
  half is untouched and not re-reported: the new guard `return`s normally like the two beside it, so
  `check()` prints `ok`, and the fold added a third skip path that can print a green row. Round 1's
  `check()`-sentinel remedy still stands and now covers three arms.
- **The two `map_lib` fixes round 1 asked for, other than row 4.** Finding 6 (the Python prefix
  backscan) is closed in both directions: `typeof"${leak}"` no longer captures `leak`, and the
  under-capture twin no longer swallows `alive` or `s`. Finding 7 (`_LINE_COMMENT_RE`, `_STRING_RE`)
  is closed by deletion, with `_BLOCK_COMMENT_RE` and `_IDENT_TOKEN_RE` correctly kept.
- **`TOOL-aLexedStripper-7` was correctly deferred rather than folded.** The `scan_js_definitions`
  block-before-line stripping order is a real defect, the instance fix (rewording the comment) is
  honest about being an instance, and the backlog row states why it is its own unit: the proper fix
  must preserve line structure because the probe substitutes newlines to keep line numbers and it
  feeds the committed `symbols.json`. Measured in both trees, 0 lost here and 14 across 9 files in
  `d41ly/incms`. Nothing to add.
- **Kit version and mirror parity.** `diff -q tools/hooks/agent-cap.js .claude/hooks/agent-cap.js` is
  clean, and `.claude/settings.json:9` runs the mirror as the `PreToolUse` command — which is how the
  two blockers reach the live guard rather than staying in a kit file.

## What this round says about the fold

The fold answered a review by measurement in one place and by argument in two, and the two arguments
are the ones that failed. Round 1's blocker 1 came with an explicit instruction not to ship the
smaller repair and a measured fixture showing why; the fold shipped it and wrote the claim into
three records. Round 1's blocker 2 was refuted with four fixtures that all placed the fan on a
different line from the quote, which is the one placement where a single-line swallow cannot change
the verdict — the counter-fixtures measured the absence of a defect they were not positioned to see.

Both mistakes have the same shape as the one round 1 diagnosed in `TOOL-aLexedStripper-5` itself: a
safety claim verified only against constructs the author already had in mind. Row 3 is the cheap
structural answer and it is why row 3 is HIGH rather than a bookkeeping note. Three of the arms it
asks for — a grep of `renderCodeView`'s body for `'/*'`, a dropped-tail assertion on the quote
branch, and the `absent` column of the per-language table — pin the branch sets rather than the
spellings, so the next construct added to either scanner has to argue with a test instead of with a
comment.
