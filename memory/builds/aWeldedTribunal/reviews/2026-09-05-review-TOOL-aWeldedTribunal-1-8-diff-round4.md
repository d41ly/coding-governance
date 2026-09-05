**Serves:** diff-review TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8

# Closing diff review — aWeldedTribunal, the fold of round 3

Tier-2 adversarial review of the FOLD alone: the single commit `fe6a5010` that closed round 3's
three findings. The build is not re-reviewed — round 1 covered it. This round asks the same two
questions rounds 2 and 3 asked, because the answer has now been "the fold traded a defect in one
direction for a defect in the other" twice running. Is each fix correct and complete, and did it
introduce something new, in either direction. A fan of primed finder lenses over that diff, a
skeptic pass prompted to REFUTE each finding, then this synthesis. **Every exit code quoted below
was re-measured by the synthesis pass against three revisions side by side plus a patched copy, not
carried over from a lens.**

**Range — ROUND 4:** `3ff9cc14...HEAD` (`HEAD` = `fe6a50101fce5981fa1d07b3bf962319f90db8c4`, one commit).

## Verdict: BLOCKED

One defect at blocker severity, reported independently by three lenses (F3, F4, F5) — three rows,
**one line, one fix**. Plus one new fail-open this fold introduced on its own (F1), and one
header-honesty defect (F2) that is the documentation half of the blocker. The fold did close round
3's false-DENY (`LENSES.splice(0, Math.min(...ns))` now allows, measured 2 → 0) and did close the
multi-line phantom span. It also did the thing this build has now done three rounds in a row: it
handed the only mechanical control against an agent burst a **new** blind spot while closing the old
one.

**Review shape:** raw 5 · confirmed 5 · refuted 0 · unverified 0 · precision 1.00.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0
contradictory verdicts demoted to unverified; 0 spurious verdicts discarded; 0 duplicates. Every
count is zero, so the finding set is complete as far as this shape reaches and a zero elsewhere in
this report is evidence rather than an artefact of a dead worker.

## Findings

| # | Sev | File:line | Defect | New in this diff? |
|---|-----|-----------|--------|-------------------|
| F4 | **blocker** | `tools/hooks/agent-cap.js:927` | Per-line strip pairs a regex-literal `/*` with a real `*/` later on the SAME line; the take-back between them is deleted and the bound survives | No — inherited from `3ff9cc14`, half-closed here |
| F3 | **blocker** | `tools/hooks/agent-cap.js:927` | Same defect, independent reproduction across three trees | No — same as F4 |
| F5 | **blocker** | `tools/hooks/agent-cap.js:927` | Same defect, two further spellings + the header claim | No — same as F4 |
| F1 | high | `tools/hooks/agent-cap.js:1005` | The new spread test is a PREFIX test, so a block comment in front of a spread argument hides it and a growing `splice` grades as removal-only | **YES — introduced by this fold** |
| F2 | medium | `tools/hooks/agent-cap.js:922` | The new residual paragraph names only a fail-CLOSED residual; the live fail-OPEN direction is documented as not existing | **YES — the paragraph is new in this fold** |

Severity attaches to the defect, not to the row count. F3/F4/F5 are one blocker at one line and one
patch closes all three; the count reads 3 because three lenses reached it by three different
spellings, which is signal about reachability, not three separate bugs. F1 is a genuine fail-open
newly introduced here and is called high rather than blocker on reachability alone — its trigger
shape is stranger than F4's. It must be fixed in this same round regardless; nothing about "high"
means "later".

---

### F4 / F3 / F5 — BLOCKER — `tools/hooks/agent-cap.js:927`

**The defect.** The line is

```js
const takeBackView = code.map((l) => l.replace(/\/\*.*?\*\//g, ' ').split('//')[0])
```

This file models no regex literal, by its own standing decision. So in a line like
`if (/[/*]/.test(s)) LENSES.push(x) /* ok */`, the `/*` inside the character class is read as a
comment opener, the lazy `.*?` runs to the `*/` of the ordinary trailing comment, and
`LENSES.push(x)` is deleted from the view **both** take-back sweeps read. The growth is never seen,
the bound survives, and a `boundedParallel(LENSES.map(...))` fan-out over the grown array is
admitted.

Round 3's fold moved this strip from the joined text to per line. That closed the *propagation*
across lines. It did not close the *class*: an opener and a closer on one line still pair.

**Measured**, with the real hook, identical payloads, exit 2 = deny and 0 = allow:

| Payload line (between a bounded `LENSES` and a `boundedParallel(LENSES.map(...))` fan) | `cd51decd` | `3ff9cc14` | HEAD |
|---|---|---|---|
| `f(/[/*]/); LENSES.push(x); const t = 1 /* c */` | 2 | 0 | **0** |
| `if (/[/*]/.test(s)) LENSES.push(x) /* ok */` | 2 | 0 | **0** |
| `const a = /[/*]/; LENSES.push(x); const b = /[*/]/` | 2 | 0 | **0** |
| `const _r = /[/*]/; LENSES.splice(0, 0, ...allFindings) /**/` | 2 | 0 | **0** |
| control — same line, regex literal removed | 2 | 2 | 2 |
| control — regex literal present, no closer on the line | 2 | 2 | 2 |

The two controls isolate the mechanism: only the *combination* of a phantom opener and a real closer
on one line flips the verdict, so the cause is the strip at :927 and nothing else. The second
spelling above is ordinary JavaScript, not a contrivance — a regex character class containing `/*`
and an ordinary trailing comment.

**On provenance, stated precisely because it changes what this round is being asked to approve.**
The `0` at `3ff9cc14` means this fail-open was already live at the reviewed BASE. It is *not* new in
this diff. It IS a live regression against the build's pre-fold base `cd51decd`, and this fold is
the commit that set out to close it and closed half. Approving the fold approves the half-fix.

**Fix.** Refuse an opener that sits where a regex literal puts one, using the zero-width lookbehind
idiom already in this file's `GROWS_RECEIVER`:

```js
const takeBackView = code.map((l) => l.replace(/(?<![/[\w$])\/\*.*?\*\//g, ' ').split('//')[0])
```

Verified on a patched copy: all four leaking spellings return to exit 2, and every intended allow is
unchanged — `/* never do LENSES.push(x) here */` (round 1's finding) stays 0,
`LENSES.splice(0, /* keep ( */ 2)` stays 0, `LENSES.splice(0, Math.min(...ns))` stays 0.

**Left-shift gate.** Adding the same-line spellings beside the three cross-line arms at
`tools/hooks/agent-cap.test.sh:141-147` is necessary and not sufficient — it gates the instance
again, which is how this class has survived three folds. Gate the CLASS: make the view axis a
generated cross product. Keep one list of take-back payloads (`LENSES.push(x)`,
`LENSES.splice(0, 0, x)`, `LENSES = allFindings`) and one list of view wrappers (own line · same
line after a phantom opener · same line before a real closer · between two regex literals · inside a
real single-line comment, which must ALLOW), and emit every pair. One loop replaces a dozen typed
arms, and a future fold cannot close one cell and leave its neighbour open.

---

### F1 — HIGH — `tools/hooks/agent-cap.js:1005` — **introduced by this fold**

**The defect.** The fold replaced the position-independent text scan with a prefix test:

```js
-        if (call && !call.text.includes('...') && topLevelArgs(call.text).length < 3) continue
+        const args = call ? topLevelArgs(call.text) : null
+        if (args && !args.some((a) => a.trim().startsWith('...')) && args.length < 3) continue
```

`.trim().startsWith('...')` only sees a spread that leads its argument. The other half of this same
fold — the per-line strip at :927 — deliberately leaves a multi-line block comment in
`takeBackView`. So a `/*` with no same-line `*/` survives into the argument text, `joinCall` welds
the lines, and the argument reads `/*\n*/ ...rest`. It does not start with `...`, the length test
holds, the `continue` skips the take-back, and a growing `splice` is graded removal-only. The two
halves of one fold combine to make this.

**Measured:**

| Payload | `cd51decd` | `3ff9cc14` | HEAD |
|---|---|---|---|
| `LENSES.splice(0, /*` ⏎ `*/ ...rest)` | 2 | 2 | **0** |
| `LENSES.splice(/*` ⏎ `*/ ...rest)` | 2 | 2 | **0** |
| control — bare `LENSES.splice(...more)` | 2 | 2 | 2 |
| control — `LENSES.splice(0, Math.min(...ns))` must ALLOW | 2 | 2 | 0 |

The last row is the fix working — round 3's false-DENY is genuinely closed. The first two are the
price paid for it, and `splice(0, ...rest)` inserts every element of `rest`, so the array grows
unbounded while `ok` keeps the bound. This is also the direction the code's own header at :922-926
explicitly rejects: it accepts a residual false-DENY as the preferred posture, and this is the
inverse.

The added corpus does not reach it. `agent-cap.test.sh:129` pins only the bare
`LENSES.splice(...more)` spelling, which still denies, so the new arms are green while the class is
open.

**Fix.** Test each top-level argument for a `...` at bracket DEPTH 0 — position-independent like the
old scan, and still blind to the nested `Math.min(...ns)` the fold correctly wanted to allow:

```js
const spreadArg = (a) => { let d = 0; for (let k = 0; k < a.length; k++) { const c = a[k]; if ('([{'.includes(c)) d++; else if (')]}'.includes(c)) d--; else if (d === 0 && a.startsWith('...', k)) return true } return false }
if (args && !args.some(spreadArg) && args.length < 3) continue
```

Verified on a patched copy carrying this and the F4 fix together: both comment spellings return to
exit 2, `LENSES.splice(0, Math.min(...ns))` stays at 0, and no probe in the set regressed.

**Left-shift gate.** Add both comment spellings to the deny corpus next to
`agent-cap.test.sh:129`. Then the class-level arm: for every `deny_growth` splice payload, emit a
second variant with `/*` ⏎ `*/` injected in front of each argument. A comment between a call's
parens must never change a verdict, and that is one assertion covering every future argument test
this file grows.

---

### F2 — MEDIUM — `tools/hooks/agent-cap.js:922` — **introduced by this fold**

The new residual paragraph names one residual and calls it "a false DENY — fail-CLOSED … the
direction this file's posture prefers", and asserts that a `/*` with no `*/` on the same line
"strips NOTHING and the damage cannot propagate". Both statements are true. Together they read as
the fail-open direction being closed, which the table under F4 shows it is not. §7's rule is that a
gate's own header states what it does NOT check; the header currently states a not-checked set that
omits the one direction that leaks.

The corpus reinforces the misreading. All three new view-axis deny arms
(`agent-cap.test.sh:141-147`) spell the phantom across separate lines, which is exactly the half the
per-line strip already handles, so they pass without exercising the spelling that still fails. A
half-fix documented as a fix is worse than an untouched residual, because the next round reads it as
closed — which is the failure mode this build is four rounds into.

**Fix.** With the F4 patch applied, rewrite the paragraph to say what is now true: an opener
preceded by `[`, `/` or a word character is refused rather than trusted, and the surviving residual
is the multi-line false-DENY only. Do not ship the paragraph without the patch — then it would have
to name a live fail-open, which is a worse thing to ship than the patch.

**Left-shift gate.** Not gateable as prose. It joins §10 as a documented check, phrased narrowly
enough to be usable: *when a fold changes `takeBackView`, the residual paragraph is re-derived from
the measured probe table, never edited in place.* The probe table is the artefact that cannot lie;
the paragraph is the copy that rots.

---

## Observed during verification — NOT part of the finding set

One further fail-open surfaced while isolating F4's mechanism, and it is recorded here rather than
counted, because it is out of this diff's scope and no skeptic saw it. **A bare reassignment is
missed whenever another statement precedes it on the same line.** Measured at HEAD:
`const _r = 1; LENSES = allFindings` exits 0, while the same reassignment on its own line exits 2.
It exits 0 at `cd51decd` and at `3ff9cc14` too, so it is pre-existing, not a regression, and not
this fold's doing — the growth sweep has a `deny_growth "after a semicolon"` arm at
`agent-cap.test.sh:133` and the reassignment sweep has no equivalent. It is a fail-open on the same
control and wants its own round. Naming it here so the next reader does not have to rediscover it,
and so nobody mistakes this report's silence for coverage.

## What this fold got right

Recorded because a review that only lists defects mis-prices the fold. Re-measured, not assumed:

- Round 3's false-DENY is closed. `LENSES.splice(0, Math.min(...ns))` went 2 → 0.
- The multi-line phantom span is closed. All three new cross-line deny arms genuinely exercise a
  path that failed at `3ff9cc14`.
- Round 1's case is still correct. `/* never do LENSES.push(x) here */` still allows.
- The corpus grew along the axis that actually broke — the view, not the mutation. That is the right
  axis; it was just spelled one line wide.

## State

- Suite at HEAD: `tools/hooks/agent-cap.test.sh` reports 212 passed, 0 failed. Green is not coverage
  here — every defect above passes it. That is the point of the class-level gates proposed under each.
- Probe harness used for every table in this report: three checked-out revisions plus a patched
  copy, driven by identical JSON payloads through the real hook.
