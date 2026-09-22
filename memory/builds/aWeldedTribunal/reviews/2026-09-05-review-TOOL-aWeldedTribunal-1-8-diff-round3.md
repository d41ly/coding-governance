**Serves:** diff-review TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8

# Closing diff review — aWeldedTribunal, the fold of round 2

Tier-2 adversarial review of the FOLD alone: the single commit `3ff9cc14` that closed round 2's six
findings. The build is not re-reviewed — round 1 covered it. This round asks the two questions round
2 asked, because round 2's answer to them was "the fold traded false-DENIES for fail-OPENs". Is each
fix correct and complete, and did it introduce something new, in either direction. A fan of primed
finder lenses over that diff, a skeptic pass prompted to REFUTE each finding, then this synthesis.
Every exit code quoted below was re-measured by the synthesis pass against three revisions side by
side, not carried over from a lens.

**Range — ROUND 3:** `15d92203...HEAD` (`HEAD` = `3ff9cc1409b56cdfe7c1759b2c0d53c5f52da8ea`, one commit).

## Verdict: BLOCKED

One blocker. The fold closed all six of round 2's findings — every one of them re-measured as
genuinely fixed — and introduced two new defects, one in each direction. The fail-OPEN one is a
third-consecutive-round bound escape on the only mechanical control against an agent burst, and it
is the same class round 2 named: a repair that hands the control a new blind spot.

The new view the fold built, `takeBackView`, strips block comments with a regex over text whose
regex literals are untracked. A `/*` inside a regex literal opens a phantom comment that runs to the
next real `*/` and deletes every take-back in between. That blinds BOTH sweeps that read it, and
`runBothViews` cannot recover it because both of its arms build the same stripped view.

Half of that is inherited: the growth sweep has admitted this shape since round 1's fold, and round
2 did not find it. Half is new: R6 moved the reassignment sweep onto the stripped view, so a shape
that DENIED at both `cd51decd` and `15d92203` now ALLOWS. A regression against both baselines the
build is measured on.

## Review shape

Raw 8 · confirmed 8 · refuted 0 · unverified 0 · precision 1.00.

The eight confirmed findings are three distinct defects. Four lenses independently reported the same
line (`agent-cap.js:915`) and two reported the same corpus gap; the table below maps every raw id to
its adjudicated row so nothing reads as dropped. The merge is this synthesis's judgement and is
separate from the run-integrity duplicate counter, which is zero.

## RUN INTEGRITY

- Lenses 4/4 returned, 0 DIED.
- Skeptic batches 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.

The fan is complete, so a zero in a category below is evidence of absence rather than a gap in
coverage.

## The measured table

Exit codes from `node <rev>/agent-cap.js` on a `Workflow` payload. `2` = DENY, `0` = ALLOW. BASE is
`cd51decd` (pre-build), R1 is `15d92203` (round 1's fold), HEAD is `3ff9cc14`. Every fixture is the
frozen-corpus shape: a bounded `LENSES`, one body, and a bounded-looking `boundedParallel` fan.

Fixtures were passed through a file rather than shell arguments. An argument beginning `//` is eaten
outright by MSYS on this node, which produced two wrong rows in my first pass; the numbers below are
from the file-based harness.

### The escapes — F1

| body | BASE | R1 | HEAD | |
|---|---|---|---|---|
| `LENSES.push(x)` | 2 | 2 | 2 | control |
| `const re = /[/*]/` · `LENSES.push(x)` · `/* c */` | 2 | 0 | **0** | fail-OPEN, inherited |
| `const re = /x\/*/` · `LENSES.push(x)` · `/* c */` | 2 | 0 | **0** | fail-OPEN, inherited |
| `const re = /[/*]/` · `LENSES.push(x)` · `const r2 = /[*/]/` | 2 | 0 | **0** | closer is itself a regex |
| `const re = /[/*]/` · `LENSES.push(x)` (no closer) | 2 | 2 | 2 | control — the span is the mechanism |
| `let LENSES` · `/[/*]/` · `LENSES = allFindings` · `/* note */` | 2 | 2 | **0** | fail-OPEN, **introduced** |
| `let LENSES` · `/x\/*/` · `LENSES = allFindings` · `/* note */` | 2 | 2 | **0** | fail-OPEN, **introduced** |

### The false DENY — F3

| body | BASE | R1 | HEAD | |
|---|---|---|---|---|
| `LENSES.splice(0, Math.min(...ns))` | 2 | 0 | **2** | false DENY, **introduced** |
| `LENSES.splice(0, 2)` | 2 | 0 | 0 | control, removal only |
| `LENSES.splice(...more)` | 2 | 0 | 2 | correct, R4's real hole |
| `LENSES.splice(0, ...rest)` | 2 | 0 | 2 | correct |

BASE denies every splice fixture including the removal-only control, so BASE is not an oracle on
this row — that was round 1's false-DENY finding, and R1 is the correct comparison here.

### What the fold got right, measured

All six of round 2's findings close. None of these is asserted; each was re-run.

| round 2 | fixture | R1 | HEAD |
|---|---|---|---|
| R1 | `const s = ` `` `${LENSES.push(x)}` `` | 0 | 2 |
| R2 | `sink.push(LENSES.push(9))` | 0 | 2 |
| R2 | `state.LENSES.push(x)` (must allow) | 0 | 0 |
| R3 | twin `LENSES.splice(` openers, the second inserting | 0 | 2 |
| R4 | `LENSES.splice(...more)` | 0 | 2 |
| R5 | CR bytes in the committed blob | 1768 | 0 |
| R6 | `/* never do` · `LENSES = allFindings` · `*/` (must allow) | 2 | 0 |

R5 is clean in the index blob, the worktree, and pinned by `tools/hooks/*.js text eol=lf` in
`.gitattributes`. R6 is a genuine false-DENY fix — that fixture really did deny a mention at both
baselines — which is worth saying plainly, because R6 is also the change that opened F1's second
half. The fold did not do a pointless thing badly; it did a correct thing with the wrong tool.

## Findings

### F1 — BLOCKER · `tools/hooks/agent-cap.js:913-917` · the comment strip is blind to regex literals, and it now blinds both sweeps

*Raw ids 1, 2, 4, 7 — four lenses, one line, one mechanism.*

```js
const takeBackView = code
  .join('\n')
  .replace(/\/\*[\s\S]*?\*\//g, ' ')
  .split('\n')
  .map((l) => l.split('//')[0])
```

`code` comes from `renderCodeView`, which models no regex literal — the file says so twice, in its
own words, at lines ~640 and again in `renderLexedView`'s header at ~699. That header goes further
and states this exact hazard as the reason it refuses to blank block comments at all: a regex-borne
opener closed by a later ordinary closer erases the span between, and two closing-review rounds
measured it. The fold reinstated the blanking one layer up, with a blunter tool, over the same
regex-unaware text.

`const re = /[/*]/` is legal JavaScript — an unescaped `/` is permitted inside a character class —
and so is `/x\/*/`. Either supplies a `/*` the source never opened. The strip pairs it with the next
real `*/`, which any ordinary comment below supplies, and deletes everything between. A real
`LENSES.push(x)` or `LENSES = allFindings` in that span is simply gone from the view, `ok` never
loses the name, and the bound survives a growth that actually happened.

Both sweeps read it. The growth sweep at line 971 has been blind since round 1's fold and round 2
missed it; the reassignment sweep at line 924 was moved onto the stripped view by R6 in this fold
and was blind from that moment. `runBothViews` buys nothing: `takeBackView` is constructed inside
`fanoutFindings` from whichever `code` the current `VIEW_MODE` produced, so the lexed arm and the
shipped arm build the same strip and go blind together. The measured ALLOW at HEAD is the union's
verdict, not one arm's.

The closer is phantomable in the same way — `/[*/]/` supplies a `*/` that can end a real comment
early — so the line is ambiguous in both directions, not just one.

**Fix.** Do not strip block comments with a regex over text whose regex literals are untracked.
Either resolve the comment mask with a scan that also skips regex literals — `checkLiteralOpen` and
`resolveLiteralEnd` at lines 111 and 129 are the existing machinery for exactly this shape of
question — or make the strip fail CLOSED, which is cheaper and is the posture the surrounding file
already claims. The fail-closed form: compute the strip, then, for each `.push(` / `.unshift(` /
`.splice(` / `name =` occurrence present in `code` but absent from `takeBackView`, keep the
unstripped line for that sweep. An ambiguous strip then costs a false DENY and can never cost an
admission. Keep it line-aligned while you are there: `.replace(…, ' ')` collapses a multi-line
comment to one line, which is harmless today only because both sweeps index `takeBackView` against
itself, and that is a property nobody has written down.

Separately, `.split('//')[0]` on line 917 is dead and can go. I dumped both views: `renderLexedView`
and `renderShippedView` each already blank line comments, and the fallback at line 725 splits again
on its own. Removing it changes no verdict I could produce.

**Left-shift gate.** Add the regex-borne-opener spellings to the frozen deny corpus, both halves —
growth and reassignment — and both closer forms (an ordinary `*/`, and a second regex supplying it).
Stage each one against the current HEAD and confirm it REDS before the view fix and greens after; a
corpus row nobody has watched fail is the assertion-about-nothing the charter names. See F2 for the
shape change the corpus needs first.

### F2 — HIGH · `tools/hooks/agent-cap.test.sh:106-135` · the new frozen deny corpus gates the receiver, never the view

*Raw ids 5, 8.*

The corpus is the best thing in this fold and it is the reason the fold's own blocker shipped
unnoticed. Its header states its job as gating the CLASS — "ONE GROWTH, spelled every way legal
JavaScript allows" — and it was written specifically because round 1's fold shipped four fail-opens
under a 196/0 green. It is now ten rows at lines 126-135, and every one of them is a bare-code
spelling of the RECEIVER MUTATION. Not one places a block comment, a line comment, or a regex
literal near the mutation, which is the only axis this fold changed.

I ran the suite: **206 passed, 0 failed**, over the live fail-open in F1. Same shape, same file, one
round later.

The neighbouring no-regression arm does not cover the gap either. Its BASE is `d65da7ab` (line
1412), older than `cd51decd`, and its fixture population is the tracked tree plus four files minted
under `$TMP/nrfix` for the PRIOR rounds' backtick and template-borne-comment shapes. I grepped every
tracked `*.js` for a regex literal containing `/*` and found none, so nothing in the population
reproduces the shape. The arm reports zero lost denials while two denials are in fact lost.

Two sub-claims from the lenses are wrong and I am recording them rather than repeating them. "Zero
spellings of the VIEW" overstates: the `inside a template interpolation` row IS a view arm, and it
pins round 2's `${}` escape correctly. And "no multi-line spelling is expressible at all" is false —
the mutation reaches the builder as a shell argument, so a literal newline works today. The second
error cuts against the framing and strengthens the point: one line of shell would have pinned a live
escape, and nobody wrote it.

**Fix.** Give `deny_growth` an optional third and fourth parameter for lines placed before and after
the mutation, then add the view arms: a growth preceded by `const re = /[/*]/` and followed by an
ordinary `/* c */`; the `/x\/*/` spelling; the form whose closer is a second regex; and the mirror
ALLOW arms — `/* never do LENSES.push(x) */` and the multi-line commented reassignment — so both
directions are pinned in one place. Pass the fixture through a file or a here-doc, not a shell
argument, if any row ever needs to lead with `//`.

**Left-shift gate.** The corpus IS the gate; what it needs is the axis it is missing. Add a standing
rule to the corpus header that a change to any VIEW builder owes a corpus row on that view, and make
the reviewable unit "which view did this touch" rather than "which spelling did this break".

**Also worth a row, not a finding.** `GROWS_RECEIVER` is per-line, so an ordinary prettier chain wrap

```js
LENSES
  .push(x)
```

allows at BASE, R1 and HEAD alike. That is a standing hole, not a regression from this fold, and it
is invisible to the corpus for the same structural reason — the builder takes one mutation line.
Once `deny_growth` accepts extra lines it costs one row to pin.

### F3 — LOW · `tools/hooks/agent-cap.js:991` · the spread test scans the whole call, so a nested spread revokes a shrinking splice

*Raw ids 3, 6.*

```js
if (call && !call.text.includes('...') && topLevelArgs(call.text).length < 3) continue
```

R4's fix is correct about the danger — a spread AS a splice argument is unbounded insertion and the
arity count cannot see through it — and wrong about the population. `includes('...')` is a substring
scan over the whole joined argument text, so a spread nested inside an argument EXPRESSION trips it.
`LENSES.splice(0, Math.min(...ns))` is a two-argument removal that can only shrink the array, and it
now exits 2 with the stderr line "`LENSES` was GROWN by a mutation after its bounded assignment".
A denial whose stated reason is false about the array it names — which is the class the `hadBound`
guard three lines above exists to prevent, and which the comment directly above this line claims the
arg-count check exists to avoid.

Only a TOP-LEVEL spread can make the argument count unknowable. `topLevelArgs` splits on depth-0
commas, so `splice(...a)` counts 1 and `splice(0, ...a)` counts 2; a spread at any nesting depth
contributes exactly one argument, and a top-level spread in third position already fails the `< 3`
test on its own.

Fails closed, so it blocks a legal harness rather than admitting a burst, and reachability is narrow
— it needs a bounded lens array spliced with a nested spread in the count expression. Low stands.
But it is round 1's false-DENY class reintroduced in miniature, in the fold whose whole job was to
stop trading one direction for the other, so it should not ship.

**Fix.**

```js
const args = topLevelArgs(call.text)
if (call && !args.some((a) => a.trim().startsWith('...')) && args.length < 3) continue
```

`LENSES.splice(...more)` and `LENSES.splice(0, ...rest)` still deny; the nested-spread removal
allows. Verified against both.

**Left-shift gate.** The corpus has no ALLOW half. Add one beside `deny_growth` — an `allow_shrink`
builder taking the same fixture shape and expecting 0 — and seed it with `LENSES.splice(0, 2)`,
`LENSES.splice(0, Math.min(...ns))`, `state.LENSES.push(x)`, and the two comment-mention rows from
F2. Every false DENY this build produced would have been caught by one of those five, and a corpus
that only ever asserts DENY cannot catch the direction this project keeps failing in.

## Where this leaves the build

The fold's fix rate is genuine: six of six, all re-measured, none asserted. The problem is not
carelessness, it is that three rounds running, the repair has been written against the symptom's
view rather than against the lexer, and the lexer is the thing that cannot answer the question being
asked of it. `renderLexedView`'s header already says it declines this job for this reason. F1's fix
should either give the scan the regex-literal mode it lacks or stop asking it — and if neither is
affordable, the strip must fail closed, because a comment strip that can DELETE a take-back is a
guard that shares its state with the thing it guards.

F2 is the one that matters beyond this build. The corpus is the right idea and it is now the second
green left-shift control to certify a class it does not cover. Until a view change owes a view row,
the next round will find the next view.
