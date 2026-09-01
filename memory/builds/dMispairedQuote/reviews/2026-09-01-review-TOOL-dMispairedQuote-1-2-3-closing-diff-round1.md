**Serves:** diff-review TOOL-dMispairedQuote-1 TOOL-dMispairedQuote-2 TOOL-dMispairedQuote-3

# Closing diff review — build `dMispairedQuote`, all three units

*Node d, 2026-09-01, round 1. Tier-2 closing review of the built diff, not of the specs. Every claim
below was re-derived in this worktree against the actual blobs: the hook was run, the suite was run,
and each reproduction is a probe built and executed here. Node v24.16.0.*

Reviewed range: `d65da7abb562957247720898fba1d7ef983f242a...HEAD`, HEAD = `1c01ce53e4afc22f2031e15dcdf33dcaaf92122d`.

## Verdict: CLEAN WITH FIXES

Nothing here should stop the landing. The diff is a real improvement on every input this repo
actually contains: all 48 tracked files the BASE hook denied are still denied, four of the five rules
stop being defeated by a prose apostrophe, and the suite is 146 passed / 0 failed. What follows are
three HIGH findings — two of them regressions this diff introduces, one a gate that cannot see
either — plus five smaller ones. All three HIGHs have one-line fixes, and the largest was verified
here against the full suite.

## Review shape

Raw 12 · confirmed 10 · refuted 2 · unverified 0 · precision 0.83.

Adjudication note, because the counts below will not match the fan's. The 10 confirmed findings
collapse into **6 distinct defects**: three separate filings named the same `b == 0` predicate at
`agent-cap.test.sh:1177`, and three more named the same stale bullet at
`memory/map/features/agent-cap.md:168`. Each group is merged into one row and re-severitied. Two
further findings were added in this pass (F4, F6), both reproduced, neither in the fan's output.
Eight rows follow.

| # | Severity | Where | What |
|---|----------|-------|------|
| F1 | HIGH | `tools/hooks/agent-cap.js:90` | `checkLiteralOpen` is O(n²) per line — 33.8 s vs 62 ms at BASE on a 253 KB line; past the hook timeout the guard fails OPEN |
| F2 | HIGH | `tools/hooks/agent-cap.js:285`, `:1418` | A throw in the lexed pass kills the process at exit 1 before the shipped pass runs — the "monotone in the DENY direction" claim is false, in the ADMIT direction |
| F3 | HIGH | `tools/hooks/agent-cap.test.sh:1177` | The S9 property arm scores admission as `b == 0`, but runtime admission is `exit != 2` — it is blind to F1 and F2, the exact defects present |
| F4 | MEDIUM | `tools/hooks/agent-cap.js:89` | An apostrophe after punctuation still mispairs and still hides a fan-out; the fix covers only the word-char-preceded subset, and the residual is unrecorded |
| F5 | MEDIUM | `tools/hooks/agent-cap.js:413` | `parseBranches` recurses per nested ternary with no bound — pre-existing, but it is F2's trigger and it contradicts its own contract |
| F6 | LOW | `tools/hooks/agent-cap.js:89` | `for (const c of 'parallel(')` newly DENIES; no population-level arm covers the ADMIT→DENY direction at all |
| F7 | LOW | `memory/map/features/agent-cap.md:168` | The dossier bullet names three symbols this diff deleted or repurposed |
| F8 | LOW | `tools/workflows/check-review-join.sh:70` | Three more cross-file pointers stranded by unit 1's rename, one of them in a file this diff edits |

---

## F1 — HIGH · `tools/hooks/agent-cap.js:90` · the lexer is quadratic in line length, and the tail fails OPEN

`checkLiteralOpen` runs on **every quote character** and does `line.slice(0, p + 1)` followed by an
end-anchored regex over that slice:

```js
const word = /([A-Za-z_$][\w$]*)$/.exec(line.slice(0, p + 1))
```

Both halves are O(line length), and the function is called once per quote, so a line with *q* quotes
costs O(q · n). It is reached from three sites — `renderStrippedLine:114`, `renderLexedView:540`,
`renderBlankedView:861` — so the quadratic runs several times per hook invocation.

Measured here on a minified one-liner of the shape `function pick(k){switch(k){case'key0':return'value0';…}}`
plus `await parallel(all.map(f))`. Both hooks return exit 2 on every row, so the verdict is identical
and only cost differs.

| literals | line bytes | BASE `d65da7ab` | HEAD |
|---|---|---|---|
| 2000 | 61 KB | 51 ms | 2075 ms |
| 4000 | 125 KB | 56 ms | 8259 ms |
| 8000 | 253 KB | 62 ms | 33 801 ms |

Growth is roughly 4x per doubling, so a line around 500 KB clears the 60 s default `PreToolUse`
timeout. A timed-out hook produces no exit 2, and **only exit 2 blocks** — so the failure direction is
ADMIT, on the one preventive lever this file's own header names. `.claude/hooks/agent-cap.js` is
byte-identical (`cmp`), so both wired copies carry it.

The trigger is not exotic. Any quote whose preceding non-space character is a word char, `)`, `]` or
`\` takes the slow path — that is ordinary `return 'x'` and `case 'x':`.

**Fix (verified here).** Replace the slice-plus-regex with a bounded backward walk over the
identifier run only.

```js
let w = p
while (w >= 0 && /[\w$]/.test(line[w])) w--
const word = line.slice(w + 1, p + 1)
return /^[A-Za-z_$]/.test(word) && LITERAL_OPENERS.has(word)
```

This was applied to a copy and the whole suite re-run against it. The 8000-literal line drops from
33 801 ms to **87 ms**, and **145 of 145 behavioural arms return identical verdicts** — the only
failure was the wired-copy drift arm, because only `tools/` was patched and not `.claude/`. Every
probe in this review returns the same exit code before and after.

**Left-shift gate.** Add one arm to `agent-cap.test.sh` that generates the 253 KB one-liner, asserts
exit 2, and asserts wall clock under a declared ceiling (1 s is ample; the fixed hook takes 87 ms).
A cost ceiling that REDS is the only form of this check that ever gets fixed — §7's own rule.

## F2 — HIGH · `tools/hooks/agent-cap.js:285` and `:1418` · a throw in the lexed pass admits the script

`runBothViews` runs the corrected pass with no guard, and the shipped pass is wrapped in `try/finally`
— which restores `VIEW_MODE` but swallows nothing.

```js
const lexed = rule(script)          // :285 — unguarded
VIEW_MODE = 'shipped'
let shipped
try { shipped = rule(script) } finally { VIEW_MODE = 'lexed' }
```

`main()` (`:1259`) is invoked bare at `:1418` with no top-level catch. So any throw anywhere in the
new views propagates out and node exits 1 — a non-blocking `PreToolUse` code — and the shipped pass
that would have denied never runs.

Reproduced in this worktree. Script: line 1 `const r = await parallel(D.map((d) => () => agent(d.p)))`,
line 2 `/* don't */ const X = c0?v0:c1?v1: … (9000 nested ternaries) … + 'z' // gov:fixed-verifiers`,
line 3 `const y = X.map((g) => () => agent(g))`.

- `node <d65da7ab blob>` → **exit 2**, the rule-2 BLOCKED message.
- `node tools/hooks/agent-cap.js` → **exit 1**, `RangeError: Maximum call stack size exceeded`.

The apostrophe in `/* don't */` is load-bearing, and that was checked too: with it removed, BASE also
crashes. So the recursion class pre-dates the diff (that is F5), and what this diff contributes is
precisely the **missing error isolation**, which makes the crash reachable on a script BASE denied.

That falsifies, in the ADMIT direction, the claim written into the file header at `:117-141`, into the
dossier, and into the new gotcha: *monotone in the DENY direction by construction*. It is monotone by
construction only if the construction cannot die halfway.

**Fix.** Two guards, both small. Give each pass its own catch inside `runBothViews`, so a throwing
pass contributes no findings but cannot suppress the other. Then wrap `main()`'s body so an
unexpected throw writes a `BLOCKED by agent-cap: …` line and exits **2** — which is this file's own
stated posture three lines above `parseBranches`: an expression it cannot delimit lands on the deny
side. Today an unreadable script exits 1 and is approved.

**Left-shift gate.** An arm that injects a throw (monkey-patch one view, or stage F5's deep-ternary
fixture) and asserts exit 2, not "no crash". Assert the code, because *did not crash* and *blocked*
are different properties and only one of them is the guarantee.

## F3 — HIGH · `tools/hooks/agent-cap.test.sh:1177` · the property arm cannot see the two findings above

The S9 no-regression arm defines *denied at BASE* correctly and *admitted now* incorrectly.

```python
if a != 2:            # :1173 — right: anything but 2 is not a denial
    continue
denied += 1
b = subprocess.run([...]).returncode
if b == 0:            # :1177 — wrong: admission at runtime is b != 2
    lost.append(str(p))
```

A `PreToolUse` hook blocks **only** on exit 2. Every other code — a crash at 1, an OOM, a timeout — is
non-blocking, i.e. functionally an admit. So F2's reproduction, which exits 2 at BASE and 1 at HEAD,
is a denial lost at runtime that this arm counts as a pass. The arm would print `0 denial(s) lost`
while the guard was disabled.

This repo's own doctrine already says so, one file over. `tools/workflows/check-review-join.sh:104-108`
refuses any status that is neither 0 nor 2, because a status that gate cannot interpret is a refusal
and never a verdict. The property arm applies the opposite rule to the same hook.

Two more gaps in the same twelve lines:

- **No timeout.** Neither `subprocess.run` at `:1171` or `:1176` passes `timeout=`, so F1's class hangs
  the suite instead of failing it.
- **No population floor.** `git ls-files` failing silently shrinks the population from 1273 to the 3
  bundled fixtures — which are themselves BASE-denied, so `denied` is 3, the `denied == 0` liveness
  assertion at `:1182` does not fire, and the arm reports ok.

This matters more than an ordinary predicate bug because this arm **is** the justification for
freezing the three `renderShipped*` bodies and for running every rule twice. It is the one gate
defending the build's central guarantee, and it is blind to both live ways that guarantee currently
breaks.

**Fix.** `if b != 2: lost.append((str(p), b))`, printing the observed code beside the path so a crash
is distinguishable from a clean admit. Pass an explicit `timeout=` to both calls and catch
`subprocess.TimeoutExpired` into `lost` — a hook that cannot answer inside the budget is a hook that
does not block. At `:1173`, count `a not in (0, 2)` into a separate `unscored` list and fail on a
non-empty one, rather than shrinking the population invisibly. Add the floor:
`sys.exit(1 if lost or unscored or denied == 0 or n < 100 else 0)`.

**Left-shift gate.** This finding *is* the gate, and the fix is the left-shift. Verify it the way §7
requires: stage a fixture that exits 2 at BASE and 1 at HEAD, confirm the arm goes RED, unstage. A
property arm nobody has seen fail is an assertion about nothing.

## F4 — MEDIUM · `tools/hooks/agent-cap.js:89` · the apostrophe still wins when it follows punctuation

Not from the fan; found and reproduced in this pass.

`checkLiteralOpen` treats a quote as text only when the preceding non-space character is a word char,
`)`, `]` or `\`. Everything else — `-`, `=`, `:`, `;`, `(` — is read as a position where a literal may
legally begin, which as JS is true and as prose is not. The contraction in a block comment therefore
still pairs with the quote opening `agent('a'` and still blanks the fan-out between them.

Reproduced here, one line each.

| script | BASE | HEAD |
|---|---|---|
| `/* rock - 'n roll */ const r = await parallel([() => agent('a'), () => agent('b')])` | 0 | **0** |
| `/* a = 'tis */ …same fan-out…` | 0 | **0** |
| `/* note: 'tis so */ …same fan-out…` | 0 | **0** |
| `const x = 1; /* 'tis */ …same fan-out…` | 0 | **0** |
| `/* rock - n roll */ …same fan-out…` (apostrophe removed) | 2 | **2** |

The control on the last row is what makes it the target class and not something else: remove the
apostrophe and the same script denies.

This is not a regression — BASE admits these too — and honest reachability is genuinely lower than the
fixed cases, which is why it is MEDIUM and not HIGH. `/* it's */` is natural English and
`/* rock - 'n roll */` is not. As a deliberate bypass it is one line either way.

The problem is the **record**, and that is a §7 rule rather than taste. The header at `:50-58` names
exactly one residual, the eleven-keyword clause, and the suite fixtures that residual over its
declared set with three controls — good work, and it is exactly what makes the *unnamed* second
residual read as absent. The dossier, the new gotcha and the backlog rows all describe the class as
closed.

**Fix.** State the residual where the keyword clause is stated, in the header and in the dossier: the
predicate answers *may a literal legally begin here*, which is not the same question as *is this
prose*, and a quote preceded by an operator is admitted as an opener. Add three arms — `-`, `:`, `;` —
asserting the current exit 0 as a **stated residual**, exactly as the eleven keyword arms do, so the
leak is recorded rather than assumed away.

**Left-shift gate.** The eleven keyword arms are already the right pattern; extend them over the
operator set. If closing the class is ever in scope, the shape that closes it is not a wider character
class but a comment-aware pre-pass, and that is its own unit.

## F5 — MEDIUM · `tools/hooks/agent-cap.js:413` · `parseBranches` has no depth bound

`parseBranches` recurses once per nested ternary with no bound, so a long chain overflows the stack
instead of landing on the deny side. Measured here on a `gov:fixed-verifiers` RHS: exit 2 at 6500
levels, `RangeError` and exit 1 at 7000.

That defeats the contract written three lines above the function — *an expression this file cannot
delimit lands on the DENY side rather than being waved through*. It does the opposite.

**Pre-existing, and confirmed as such: the BASE blob crashes in the same 6500–7000 band.** This diff
neither introduced nor widened it. It earns a row because it is F2's concrete trigger, and because
correcting the quote rule is what lets a deep chain reach it on scripts the old mispairing blanked.

**Fix.** Thread a depth counter and return `[null]` past a small bound. A null branch already never
qualifies in `boundedBranch`, so the overflow degrades into the deny the contract promises, with no
new vocabulary. F2's `main()` catch would also contain this, which is why F2 is the higher row: it
bounds the whole class rather than this instance.

**Left-shift gate.** One arm staging the deep-ternary fixture and asserting exit 2.

## F6 — LOW · `tools/hooks/agent-cap.js:89` · a legal shape newly denies, and nothing watches that direction

Not from the fan; found and reproduced in this pass.

`of` is not in `LITERAL_OPENERS` and is a bare word, so the string in `for (const c of 'parallel(')` is
no longer recognised as a literal, is not blanked, and rule 1 sees the primitive. Measured:
`for (const c of 'parallel(') { log(c) }` plus a bounded fan-out gives **BASE 0, HEAD 2**. A false
positive introduced by this diff, in the safe direction.

It was swept: over the repo's 94 tracked `.js`/`.sh` files, **89 allowed at BASE, 0 newly denied**. So
there is no live instance, and the severity is LOW.

The structural half is worth more than the instance. The DENY→ADMIT direction gets a population
property over 1273 files; the ADMIT→DENY direction gets five hand-written allow fixtures. The build's
own reasoning says why that asymmetry is not free — a fixture group that only asserts one direction
cannot catch a fail-closed that became a fail-open, and the mirror of that sentence holds too.

**Left-shift gate.** Add the reverse arm beside S9, over the same population: every file the BASE hook
allowed must still be allowed, with the same liveness assertion (`allowed == 0` fails) and the same
population floor. It costs one more pass over a corpus already being walked twice, and it is where a
future over-tightening shows up first.

## F7 — LOW · `memory/map/features/agent-cap.md:168-172` · the dossier describes the file by dead names

The bullet still reads *"`renderCodeView` models no regex literal … it inherits `blankLiterals`'
code-mode branch set … falls back to the per-line `stripStrings` view"*. All three pointers are wrong
now. `renderCodeView` is the three-line `VIEW_MODE` dispatcher at `:271`, the lexer is
`renderLexedView` at `:518`, and `blankLiterals` and `stripStrings` have no definition anywhere in the
file.

The staleness is conspicuous rather than incidental: this diff appended a five-line refutation
paragraph **inside this same bullet** and rewrote the one above it, so the untouched sentences read as
freshly reviewed. Unit 2 was the prose unit and this is the file it exists to update.

Nothing catches it. `memory/map/generated/symbols.json` was correctly regenerated — `blankLiterals`
gone, `renderLexedView` / `renderBlankedView` / `renderShippedBlanks` added — so the map ratchet's key
check is green while the prose directly above the new bullets is not.

**Fix.** Rewrite `:168-172` against the new names, attributing the regex-literal ceiling to
`renderLexedView` rather than to the dispatcher, and the fallback to `renderStrippedLine`. Re-title the
six `renderCodeView:` arm-label prefixes at `agent-cap.test.sh:871-909` while there — they now label
arms exercising `renderLexedView`.

**Left-shift gate.** The honest one is cheap and narrow: a check that every backticked identifier in a
dossier resolves in that feature's `symbols.json`. Prose drift is otherwise ungateable by construction,
and §7's answer to that is a §10 checklist row — the class here is
`amendment-leaves-its-other-half-standing`, which this build's own new gotcha already names.

## F8 — LOW · three more pointers stranded by the rename

Same class as F7, outside the map.

- `tools/workflows/check-review-join.sh:70` — *"the stripper is the hook's `blankLiterals`"*. This is
  the gate's only cross-file pointer to the predicate it shells out to (`node "$HOOK" --only=join`),
  and the name is not even recoverable by substring: the surviving dispatcher is
  `renderBlankedLiterals`. The gate itself still runs clean.
- `tools/hooks/scratch-guard.js:26` — names `stripStrings`. **This diff edits that file** (the version
  marker) and left the comment standing.
- `tools/hooks/agent-cap.test.sh:732` — names `blankLiterals`.

**Fix.** Point the first at `renderBlankedLiterals` and say it resolves to `renderBlankedView` or the
frozen `renderShippedBlanks` by `VIEW_MODE`, so a reader learns that rule 5 is now evaluated over both.
Fix the other two in place. The one place `stripStrings` may legitimately stay is inside
`renderShippedView`'s frozen body at `:164`, which the byte arm requires verbatim.

**Left-shift gate.** Fold into F7's identifier-resolution check, widened from dossiers to any
backticked identifier in a comment under `tools/`. Print near-misses on the first run — §7's rule about
running a candidate predicate over the real tree before wiring it applies here, and a rename-aware
predicate will red on more than these three.

---

## Cleared — hunted, and not found

These are the things the brief asked for by name. Each was checked, and each came back negative. They
are recorded so the next round does not re-spend the tokens.

- **Every rule's view read goes through a dispatcher.** All ten read sites (`:308`, `:591`, `:592`,
  `:925`, `:1221`, `:1248`) call `renderStrippedView`, `renderCodeView` or `renderBlankedLiterals`.
  There are zero direct calls to `renderLexedView`, `renderShippedView`, `renderBlankedView`,
  `renderShippedBlanks`, `renderStrippedLine` or `renderShippedLine` outside the three dispatchers
  themselves. The "no census" argument in the comment at `:255` holds.
- **`VIEW_MODE` is never left wrong.** `runBothViews` is the only writer, the `finally` restores it on
  every exit path including a throw, no rule function re-enters `runBothViews`, and the lexed pass runs
  before the first write — so a throw there leaves the mode already correct. The only cost of a throw
  is the process dying, which is F2 and is a different defect.
- **The merge cannot drop a finding that matters.** All 13 `push({…})` sites carry `{n, line, why}`, so
  the `(n, why)` key is well-formed everywhere. `why` is templated from view-derived text, so two views
  that disagree produce different keys and both survive. A dropped duplicate changes only the count in
  a `slice(0, 6)` display, and since a denial from either pass stands, no dedup outcome can flip DENY
  to ADMIT.
- **No new arm passes without exercising its rule.** The eleven keyword-residual arms assert exit 0,
  which is the shape that could pass by never reaching the rule — but they ship with five controls
  (`in of do run one`) asserting exit 2 on the identical script skeleton, which proves the shape
  reaches the rule. That is the right construction.
- **The byte-identity arm (S10) is real.** It announces its skip with a reason, compares three function
  bodies against the BASE blob, and prints `bodies-compared 3 drifted 0` as its liveness. It is not the
  arm with the problem.
- **`checkLiteralOpen` is correct for the legal JS shapes that could be constructed against it**, with
  the two exceptions filed as F4 (too permissive after an operator) and F6 (too strict after `of`).
  Line-start quotes, `)`-preceded, `]`-preceded, digit-preceded and escape-preceded cases all behave as
  the header describes.

## Caveats on this review

- **The tree is not clean.** `tools/hooks/agent-cap.test.sh`, `memory/builds/dMispairedQuote/README.md`,
  `RUN.md` and `memory/project/readme-contract.txt` carry uncommitted changes beyond the reviewed
  range. The suite run therefore measured HEAD plus the uncommitted test hunk, which derives `HOOKREL`
  from `git ls-files` instead of a literal path. That hunk is small and safe and touches none of the
  findings above, but the 146/0 figure is HEAD-plus-that, not HEAD.
- **The suite is green and it was run.** `bash tools/hooks/agent-cap.test.sh` → `146 passed, 0 failed`,
  with the property arm reporting `population 1273 scanned, 48 denied at BASE, 0 denial(s) lost`. F3 is
  the reason that last number should not be read as reassurance.
- **F1's timeout threshold is extrapolated; the slowdown is not.** Measurement goes to 253 KB and
  33.8 s directly; the ~500 KB / 60 s crossing follows from a fitted ~4x-per-doubling curve, not from a
  run. The 100x–500x regression at measured sizes stands on its own.
- **F2 and F5 need contrived inputs.** Roughly 7000 nested ternaries on one line is a deliberate bypass,
  not something an honest harness writes. Both are filed on the structural defect — an unguarded pass
  and an uncaught `main()` — and not on the trigger.
- **The full 1273-file corpus was not swept for the ADMIT→DENY direction.** The quadratic in F1 made it
  too slow to finish inside budget, so F6's sweep covers the 94 tracked `.js`/`.sh` files only. Fixing
  F1 makes the full sweep cheap, and F6's suggested gate is where it belongs.
