**Serves:** diff-review TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8

# Closing diff review — aWeldedTribunal, the fold of round 1

Tier-2 adversarial review of the FOLD alone: the single commit `15d92203` that closed round 1's
eight findings. The build itself is not re-reviewed — round 1 covered it, and this round asks two
questions only. Is each fix correct and complete, and did the fix introduce something new. A fan of
primed finder lenses over that diff, a skeptic pass prompted to REFUTE each finding, then this
synthesis. Every finding below was re-reproduced by the synthesis pass by running the shipped hook
and the BASE blob side by side; the exit codes quoted are from those runs, not from the lenses'.

**Range — ROUND 2:** `cd51decdb943630f934f50441fb4b4bc2ff8e6ff...HEAD` (`HEAD` = `15d922031f95bfa068bf01ea2e5e2a8a0e355849`, one commit).

## Verdict: BLOCKED

Four blockers, all in `tools/hooks/agent-cap.js`, and all the same shape: the fix regressed the
control it was fixing. Round 1's findings were about the hook DENYING legal harnesses — annoying,
loud, self-announcing. The fold traded that for the opposite failure, which is silent. Five distinct
one-line legal-JavaScript escapes that the BASE hook DENIED are ADMITTED at HEAD, each one handing
an unbounded agent-per-item fan-out past the only mechanical enforcement the §8 cap has. The file's
own header states the posture this breaks — no script this hook denies today may be admitted after
the change — and the fix that cites that posture is the one that broke it.

The self-test suite passes 196/196 over every one of them. The gate leg `agent-cap self-test` is
green right now, on a tree where the control does not work. That is the §7 "gate the CLASS, not the
instance" failure in its purest form: the fold added eight arms, each pinning the exact script from
round 1's report, and none pinning the class any of them belongs to.

Two highs follow. One is why nobody saw the four blockers: the fold recommitted all 1767 lines of
the hook as CRLF, so `git diff` renders a 54-line change as a whole-file rewrite. The other is a fix
applied to one of two sibling sweeps.

## Review shape

- raw 16 · confirmed 12 · refuted 4 · unverified 0 · precision 0.75
- The 12 confirmed reports resolve to **6 distinct defects**. The splice line-lookup was found
  independently four times, the CRLF rewrite three times, and the `GROWS_RECEIVER` left guard twice
  as two different escape mechanisms — merged here into one row because they live in one regex and
  one edit closes both. Merged at synthesis; the harness discarded no duplicates of its own.

## RUN INTEGRITY

- lenses 4/4 returned, 0 DIED
- skeptic batches 4/4 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified · 0 spurious verdict(s) discarded · 0 duplicate(s)

Every counter is zero, so this run is complete and no arm is missing. Where this report reports an
absence — no confirmed finding against the `govkit`, `corpus_ids`, `check-wiring` or `gotchas` legs
of the fold — that absence rests on four lenses that all returned.

## The measured table

Every row is one script, run through `node` against both blobs. `BASE` is
`cd51decd:tools/hooks/agent-cap.js`; `HEAD` is the shipped file. Exit 2 is DENY, exit 0 is ALLOW.
Every script ends in the same fan, `await boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)`,
over an array a preceding mutation genuinely grows.

| The mutation line | BASE | HEAD | |
|---|---|---|---|
| ``const s = `${LENSES.push(x)}` `` | 2 | **0** | R1 |
| `if(x)LENSES.push(y)` | 2 | **0** | R2a |
| `sink.push(LENSES.push(9))` | 2 | **0** | R2b |
| `LENSES.splice(` / `  0, 1)` then an identical opener with `  0, 0, a, b, c)` | 2 | **0** | R3 |
| `LENSES.splice(...more)` | 2 | **0** | R4 |
| control: `LENSES.push(y)` | 2 | 2 | — |
| control: a block comment holding `LENSES = allFindings` | 2 | 2 | R6 |

Five regressions, one control that still denies as it should, and one control that denies when it
should allow. `bash tools/hooks/agent-cap.test.sh` on this tree: `196 passed, 0 failed`.

## Findings

| # | Sev | Site | Defect |
|---|-----|------|--------|
| R1 | BLOCKER | `tools/hooks/agent-cap.js:947` | The growth sweep now reads a view that ERASES `${…}` bodies, so a push inside a template substitution is invisible |
| R2 | BLOCKER | `tools/hooks/agent-cap.js:941` | The new left guard both CONSUMES the character it inspects and excludes `)`/`]` — two escapes out of one regex |
| R3 | BLOCKER | `tools/hooks/agent-cap.js:961` | The splice guard resolves the current line by VALUE, so a duplicate opener line joins the WRONG call's arguments |
| R4 | BLOCKER | `tools/hooks/agent-cap.js:962` | The splice arity test counts top-level commas, and a spread hides the count |
| R5 | HIGH | `tools/hooks/agent-cap.js:1` | The fold recommitted the whole file CRLF, and a lone CR made git classify the blob binary, so it will not normalize back |
| R6 | HIGH | `tools/hooks/agent-cap.js:900` | F2 was applied to ONE of the two take-back sweeps; the reassignment sweep still reads the un-blanked view |

---

### R1 — BLOCKER · `tools/hooks/agent-cap.js:947` · the growth sweep reads a view that deletes the code it is looking for

F2 was correct about the disease. The growth sweep was reading `renderCodeView`, which deliberately
does not blank block comments, so `/* never do LENSES.push(x) */` revoked a live bound. The cure is
the problem: line 947 now reads

```js
const growView = renderBlankedLiterals(script)
const growCode = growView.unterminated ? perLineBlanked(script) : growView.code
```

`renderBlankedLiterals`' lexed arm is `renderBlankedView` (line 1181). Its `tmpl` mode, on a
backtick, does `i++` on every character until the closing backtick and appends nothing — substitution
bodies included. So `${LENSES.push(x)}` is gone before `GROWS_RECEIVER` ever runs. The shipped sibling
`renderShippedBlanks` blanks template contents too, so the union in `runBothViews` does not rescue it.

This is not a subtle inference. The file says it, sixty lines up, about this exact view:

> it blanks template CONTENTS including `${…}` bodies, which hold real code — an `agent(` inside a
> multi-line interpolation is DENIED today and would have been ADMITTED

That comment (lines 620-627) is a warning against using this view for exactly this purpose, written
by the same build, and the fold used the view anyway. `` const s = `${LENSES.push(x)}` `` grows the
array at runtime, the bound survives, and the fan is admitted. Measured 2 → 0.

**Fix.** Do not read real code out of a view that blanks it. Keep the blanked view for the comment
and string suppression F2 actually needed, then put the substitutions back before scanning: per line
`i`, run `GROWS_RECEIVER` over `growCode[i] + ' ' + <the ${…} spans lifted from code[i]>`. Making
`renderBlankedView`'s `tmpl` arm emit substitution contents is the other option, but that view is
shared with `capFindings` and `scanJoinFindings`, so it would need its own arm and its own
re-baselining — the more expensive of the two for no extra coverage here.

**Left-shift.** One arm: `` const s = `${LENSES.push(x)}` `` → deny. And the class arm below (R7).

---

### R2 — BLOCKER · `tools/hooks/agent-cap.js:941` · one regex, two ways out

```js
const GROWS_RECEIVER = /(?:^|[^.\w$)\]])([A-Za-z_$][\w$]*)\s*\.\s*(?:push|unshift|splice)\s*\(/g
```

F3's goal was right: `\b` alone captured the last segment of a member chain, so `state.lenses.push(x)`
revoked an unrelated top-level `lenses`. The implementation leaks twice.

**R2a — the class excludes `)` and `]`.** So a growth call glued to a control-flow header is not
matched: `if(x)LENSES.push(y)` is valid JavaScript, is one keystroke from the shape the fold's own
new arm pins, and is admitted. `while(a[i])`, `for(...)` and `else` all do it too. Those two
characters buy nothing — the shapes they look like they protect (`foo().push(x)`, `(a||b).push(x)`,
`arr[0].push(x)`) cannot match this pattern regardless, because no bare identifier sits immediately
before `.push` in any of them. The exclusion is pure hole.

**R2b — the guard CONSUMES the character it inspects.** With `/g`, `lastIndex` lands past that
character, so a receiver sitting immediately after a previous match's `(` is never seen at all:
`sink.push(LENSES.push(9))` matches `sink`, `lastIndex` lands on the `L`, and `^` cannot match
mid-string without the `m` flag. `LENSES` is invisible. `\b` caught this before the fix.

Both measured 2 → 0. Both fixed by one edit, and the file already uses the correct form elsewhere
(`offendingLines` uses `/(?<![.\w$])(parallel|pipeline)\s*\(/`):

```js
const GROWS_RECEIVER = /(?<![.\w$])([A-Za-z_$][\w$]*)\s*\.\s*(?:push|unshift|splice)\s*\(/g
```

Zero-width kills R2b; dropping `)` and `]` kills R2a. Verified against F3's own population: this
pattern still yields nothing for `state.lenses.push(x)`, `foo().push(x)`, `arr[0].push(x)` and
`a.b.c.push(z)`, so F3's whole point survives.

**Left-shift.** Two arms, because one edit closing two holes is exactly the situation where a single
arm certifies coverage that does not exist: `if(x)LENSES.push(y)` → deny, and
`sink.push(LENSES.push(9))` → deny.

---

### R3 — BLOCKER · `tools/hooks/agent-cap.js:961` · the splice guard looks its own line up by value

```js
growCode.forEach((l) => {
  ...
  const call = joinCall(growCode, growCode.indexOf(l), g.index + g[0].length - 1)
  if (call && topLevelArgs(call.text).length < 3) continue
```

`forEach` hands the index in as its second parameter, at line 949, and the callback discards it. The
line is then re-found by CONTENT. `indexOf` returns the FIRST line with that text, so with two
byte-identical `LENSES.splice(` opener lines, the inserting call is graded against the removing
call's arguments: `joinCall` walks forward from the wrong line, reads `0, 1`, `topLevelArgs().length
< 3` is true, `continue` fires, and the take-back never runs. Measured 2 → 0.

It fails the other way too, which matters because the whole point of F6 was to stop false denials: an
earlier identical opener whose call never balances inside `joinCall`'s 200-line bound returns `null`,
the guard falls through, and a legal harness is denied with a reason that is false about it. And a
wrong-line join can invent a third argument out of an unrelated call.

**Fix.** Take the index the iteration already offers.

```js
growCode.forEach((l, li) => {
  ...
  const call = joinCall(growCode, li, g.index + g[0].length - 1)
```

One token. The `O(n)` scan per match goes away as a side effect, which is not the reason to do it.

**Left-shift.** An arm with two byte-identical `LENSES.splice(` opener lines and differing
continuations, the second inserting → deny. The existing single-line splice arms structurally cannot
see this, which is why eight new arms missed it.

---

### R4 — BLOCKER · `tools/hooks/agent-cap.js:962` · arity cannot see through a spread

`topLevelArgs("...more")` has length 1, so `LENSES.splice(...more)` reads as a removal-only shrink
and keeps its bound, while at runtime it inserts an arbitrary number of elements. Measured 2 → 0.

The file already knows this class. The marked-branch veto one screen up explicitly lists `|\.\.\.`
as a growth signal and returns early on it — so the new guard contradicts a rule this same function
enforces forty lines away.

**Fix.** Refuse the shrink shortcut when the arguments carry a spread.

```js
if (call && !/\.\.\./.test(call.text) && topLevelArgs(call.text).length < 3) continue
```

Cheap and deliberately blunt: a spread in a splice argument list means the count is unknowable, and
unknowable resolves to growth on a security control.

**Left-shift.** One arm: `LENSES.splice(...more)` → deny.

---

### R7 — the one gate that would have caught R1 through R4

Not a separate defect, so it has no row in the table, but it is the finding with the most leverage in
this report and it belongs with the four blockers it covers.

All five escapes above are BASE-denies. Every one of them would have been caught by the property the
file already claims in prose and does not test: **no script this hook denies today may be admitted
after a change.** Eight new arms were added by the fold and all eight pin the exact script from round
1's report. That is instance coverage. The class is "a growth mutation the hook can no longer see",
and it is unbounded — five members of it shipped in one commit.

The cheap version, in `tools/hooks/agent-cap.test.sh`, is a frozen deny-corpus replayed on every run:

```sh
# Every line here is a mutation that GROWS the receiver. All of them must DENY, forever.
# A change that flips any one of them to ALLOW is a bound escape, whatever else it fixed.
while IFS= read -r mut; do
  [ -n "$mut" ] || continue
  check "growth corpus: $mut → deny" 2 "$(build_fan "$mut")"
done <<'CORPUS'
LENSES.push(y)
if(x)LENSES.push(y)
sink.push(LENSES.push(9))
const s = `${LENSES.push(x)}`
LENSES.splice(...more)
LENSES.unshift(y)
CORPUS
```

One list, one loop, and every future fix to this file is measured against it. Adding a member costs
one line, which is the only way a corpus like this stays current. Stage each entry as a break and
confirm RED before landing it, per §7 — a gate whose failing case nobody has watched is an assertion
about nothing, and that is precisely how the fold's eight arms came to certify a broken control.

---

### R5 — HIGH · `tools/hooks/agent-cap.js:1` · the fold recommitted the file CRLF, and it cannot self-heal

Verified byte for byte. The BASE blob is 99944 bytes, 1716 LF, **0 CR**. The HEAD blob is 105002
bytes, 1767 LF, **1768 CR**. `agent-cap.js` is the only file in the diff whose bytes flipped.

The 1768th CR is the interesting one. Byte 61058 is `\r\r\n`, at line 989 (`const bad = []`) — a LONE
CR. That is what trips git's `text=auto` binary heuristic, which is why check-in normalization never
ran on this blob while it runs on every other `.js` in the tree. `git ls-files --eol` confirms the
consequence: `i/-text w/-text attr/text=auto`. The file is now classified as binary in the index, so
`* text=auto` will not put it back. It is sticky until the bytes are fixed by hand.

Three costs, all concrete.

1. **It hid this review's subject.** `git diff` reports 1767 insertions and 1716 deletions for this
   file; with `--ignore-cr-at-eol` it is 54 and 3. This round could only read its own subject that
   way, and
   so could the fold's self-review — which is the most plausible reason four blockers cleared it.
2. **It is a merge bomb.** `git worktree list` shows fifteen entries on this repo. Any branch still
   holding the LF blob that touches this file now conflicts on all 1767 lines, on the one file that
   enforces the fan-out cap.
3. **It ships.** `tools/hooks/kit.toml` copies this file verbatim to `{prefix}/hooks/agent-cap.js`,
   so every adopter's next `govkit update` sees a whole-file rewrite of a security hook nobody
   edited, and `install.sums` churns for all of them. The shebang ships as `#!/usr/bin/env node\r`.

The hook itself still runs — `settings.json` invokes it as `node "…/agent-cap.js"`, mode is 100644,
so the CR shebang is inert, and both `check-kit-versions.sh` and `check-playbook-parity.sh` end their
patterns in `.*`, which absorbs the CR. That is luck, not design.

**Fix.** Rewrite in BINARY mode — python text mode eating a bare CR in a shell edit is already a
recorded gotcha in this repo, and this file has a bare CR:

```
python -c "p='tools/hooks/agent-cap.js'; b=open(p,'rb').read().replace(b'\r\n',b'\n').replace(b'\r',b'\n'); open(p,'wb').write(b)"
```

Note the second `replace` — the lone CR at line 989 must go, or the blob stays `-text` and the next
commit reintroduces the whole class.

**Left-shift.** Pin the class, not the instance: add `tools/hooks/*.js text eol=lf` to
`.gitattributes` beside the existing `tools/workflows/*.js text eol=lf`, whose comment already
records this exact failure ("came out of the checkout with 350 CR bytes"). `tools/hooks/scratch-guard.js`
currently reports `i/lf w/crlf attr/text=auto` — same exposure, no pin, one commit away from the same
outcome. There is no CR leg in `tools/gate-legs.json` at all; the `.gitattributes` pin is the whole
gate and it is enough, because it makes the bytes wrong on `git add` rather than on review day.

---

### R6 — HIGH · `tools/hooks/agent-cap.js:900` · F2 fixed one sweep of two

F2's diagnosis was that a take-back sweep must not read a view that keeps comments. It changed the
growth sweep at line 947 and left its sibling, forty-seven lines above, reading `code`:

```js
code.forEach((l) => {
  const m = /(?:^|[;{}]\s*)([A-Za-z_$][\w$]*)\s*=[^=]/.exec(l)
```

`code` is `renderCodeView`, whose own closing comment states as a deliberate property that it does
not blank block comments. So a commented-out reassignment revokes a live bound:

```js
const MAX_VERIFIERS = 5
let LENSES = [1,2,3]
/*
LENSES = allFindings
*/
await boundedParallel(LENSES.map((L) => () => agent(L)), MAX_VERIFIERS)
```

Exit 2, with the reason "`LENSES` was REASSIGNED after its bounded assignment, which takes the bound
back". Remove the comment block and it exits 0.

This one denies at BASE too, so it is not a regression — it is an INCOMPLETE fix, and it is in scope
for exactly that reason. Round 1 graded the identical defect on the sibling sweep a BLOCKER. The
reachability is ordinary: commenting out a block of code is routine, and this file's own style embeds
JavaScript samples inside block comments on nearly every screen.

**Fix.** Hoist `growView`/`growCode` (lines 947-948) above line 900 and iterate that one view in both
sweeps. One blanked view, both take-backs, no third copy of the decision.

**Left-shift.** The mirror arm, beside the two comment arms the fold already added: a block-commented
reassignment → allow. And note that the R7 corpus above is the deny direction; this is the allow
direction, and both belong in the suite.

---

## What the fold got right

Recorded so a re-read does not have to re-derive it. F1 (the `govkit` coverage probe no longer fails
`update --write`), F4 (the take-back cascade, iterated to a fixed point rather than one pass), F5
(`corpus_ids` comment stripping), F7 and F8 all survived four lenses with nothing confirmed against
them. The cascade in particular is the most structurally interesting fix in the diff — it covers the
pre-existing reassignment hole as well as the new growth one, because both write to the same `ok` set
— and it is correct. The prose added to `agent-cap.js` is unusually good at naming its own residuals.

None of that changes the verdict. The four blockers are all in the fifty-four lines that changed one
file, and they all fail the same direction: open.
