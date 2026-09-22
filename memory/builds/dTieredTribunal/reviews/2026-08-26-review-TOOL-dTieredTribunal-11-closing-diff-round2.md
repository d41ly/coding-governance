**Serves:** diff-review TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15

# Review — dTieredTribunal run 2, the FOLD of the closing review

**Measured on:** node `a`, worktree `C:/projects/coding-governance/.claude/worktrees/dtieredtribunal-build-spec-7218ea`, clean.
Every finding below was re-run against the shipped tree before it was written down. The agent-cap
reproductions were piped through `node tools/hooks/agent-cap.js` as real `Workflow` payloads and
compared against the same file at the base sha; the two staged breaks in
`tools/workflows/tier2-review.test.sh` were staged, observed, and reverted. Line numbers are from
that read, not from the finders' reports.

**Range:** `eb4b0660...bc11601c` — one product commit (`bc11601c`) on top of one records-only commit
(`582101dd`), 27 files, +870/-41. The subject is the FOLD, not the original diff: `bc11601c` is the
repair of the eleven defects (D1-D11) the round-1 closing review returned BLOCKED on, plus that
review's own record.

**Round:** 2. Round 1 reviewed run 2's CODE and returned BLOCKED with eleven distinct defects; this
round reviews the FOLD that answers them. The two spec-audit rounds in `reviews/` audited the SPEC
set and are a different subject again.

## Verdict: BLOCKED

Two blockers, and both of them are the merge bar itself. `bash tools/check-testsuite-counts.sh` and
`python tools/memory-tree/gotchas.py --check` each exit 1 on `bc11601c` and each exits 0 at
`eb4b0660`; the legs that run them carry no `guard` key, so they run on every bar including the
pre-push full run. This fold cannot land as it stands, and neither blocker is a matter of taste —
they are two commands returning 1.

The severity distribution beneath that is the more interesting result. Three HIGH findings are bound
escapes in `tools/hooks/agent-cap.js`, and one of them is a **net regression written by the fix for
D3**: a script the hook denied at `eb4b0660` is admitted at `bc11601c`. Two more mediums are new
gates that cannot fail, both of them in the self-test this fold added — including the arm registered
specifically to prevent D9's recurrence, which is blind to D9's own two fields. The pattern across
the whole fold is one thing: **eight of the twelve defects are the fold's own repairs failing in the
class they were written to close.** The repairs were reproduced; their failing cases were not
enumerated far enough.

## Review shape

Raw 24 · confirmed 24 · refuted 0 · unverified 0 · precision 1.00.

Twenty-four confirmed reports collapse to **twelve distinct defects** — the lens fan converged hard,
with four independent reports of the `${}` raw-view defect, four of the D9 args-header arm, three of
the base-ladder coverage claim, three of the reassignment reason, two of the computed-member bypass
and two of the testsuite-counts blocker. Every severity in the table below is this record's own
adjudication, not the finder's; where the fan disagreed (the computed-member bypass came in as both
medium and high) the higher reading is taken, because the failure mode is an unbounded agent fan-out
in the only mechanical control against one.

| # | Sev | Site | Defect |
|---|-----|------|--------|
| 1 | BLOCKER | `tools/workflows/tier2-review.test.sh:119` | the new gate leg reds the always-on `testsuite counts` leg |
| 2 | BLOCKER | `memory/gotchas/INDEX.md:25` | the generated index was not regenerated, so `memory hygiene` reds |
| 3 | HIGH | `tools/hooks/agent-cap.js:234` | the D3 fix dropped the `$` anchor — a truncated marked RHS is now ADMITTED |
| 4 | HIGH | `tools/hooks/agent-cap.js:225` | one `(` inside a template literal strands the depth walk and blesses the receiver |
| 5 | HIGH | `tools/hooks/agent-cap.js:230` | a computed-member link (`["concat"]`) is never inspected by the shrink-only walk |
| 6 | MEDIUM | `tools/hooks/agent-cap.js:875` | the D4 second view reads the RAW line, so rule 5 reds on comments and plain strings |
| 7 | MEDIUM | `tools/workflows/tier2-review.test.sh:116` | the D9 arm is satisfied by the D9 prose, so it cannot fail for `kind` or `subjects` |
| 8 | MEDIUM | `tools/workflows/tier2-review.test.sh:6` | the header claims coverage of the base-shape ladder; the extraction excludes it |
| 9 | LOW | `tools/hooks/agent-cap.js:348` | the D10 reason is written for names that never had a bounded assignment |
| 10 | LOW | `tools/check-kit-versions.sh:51` | "every tracked carrier" is false — the derived population is `*.js` only |
| 11 | LOW | `tools/workflows/check-review-join.sh:7` | the D7 fix added exit-2 meanings the header contract does not document |
| 12 | LOW | `tools/check-agent-cap-restatement.sh:37` | the D8 correction adds a third `6-wide` hit under `tools/`, against spec-11 AC11 |

---

## 1. BLOCKER — the new gate leg reds the always-on `testsuite counts` leg

**`tools/workflows/tier2-review.test.sh:119`**, registered at **`tools/gate-legs.json`**.

The fold added `tools/workflows/tier2-review.test.sh` and registered it as the `tier2-review
self-test` leg. That registration puts the file into the derived population of a *different* leg —
`testsuite counts (every bar self-test prints one)`, which greps the manifest's argv strings — and
the suite does not comply with it. It prints `---- 17 passed, 0 failed ----`, a fourth spelling
`compliant()` does not accept; it pins no `FLOOR_ASSERTIONS`; and it is absent from
`memory/project/testsuite-count-waivers.txt`.

**Evidence.** `bash tools/check-testsuite-counts.sh` exits **1**:

> TESTSUITE-COUNTS FAILED — a self-test on the bar prints no executed assertion count against a
> floor, so a block of its arms could be stranded past an exit and the suite would still report
> success: tools/workflows/tier2-review.test.sh

The same command exits **0** at `eb4b0660`. The leg carries `guard = None`, `subject = repo`, so it
is not held off any bar, including the pre-push full run. The fold's commit message notes the new
leg is `subject kit` "so it is held off the default bar like its two siblings" — true of that leg,
and irrelevant to this one. The guard on the *suite* does not scope the *checker* that enumerates it.

**Fix.** Make the suite comply with the three conditions in `check-testsuite-counts.sh`'s
`compliant()`: pin `FLOOR_ASSERTIONS=17` at column 0 in the `.sh`, have `run.js` report the executed
count back to the wrapper, and end with a `PASS (<n> assertions)` line guarded by a comparison
against that floor. `tools/workflows/check-review-join.test.sh` already carries the shape — copy it.
Do **not** add a waiver row: that registry is declared shrink-only, and a brand-new suite is exactly
what it must not absorb.

**Left-shift gate.** The gate already exists and already fired; what failed is that it was not run
before the commit. The durable fix is `tools/check-testsuite-counts.test.sh` gaining an arm that
registers a synthetic non-compliant suite in a scratch manifest and asserts the checker names it —
so the *checker's own* coverage of the newly-registered-leg path is pinned, rather than relying on
the next author running the full bar.

---

## 2. BLOCKER — the generated gotcha index was not regenerated, so `memory hygiene` reds

**`memory/gotchas/INDEX.md:25`**, against **`memory/gotchas/degradation-known-but-unreported.md:32`**.

D11's repair un-backticked the review-record citation in the gotcha record, which drops that
record's DERIVED anchor count from 5 to 4. `memory/gotchas/INDEX.md` is generated from those counts
and was not regenerated in the same commit, so it still reads `| class | 5 |`.

**Evidence.** `python tools/memory-tree/gotchas.py --check` exits **1**:

> HYGIENE check 17: memory/gotchas/INDEX.md is stale — run gotchas.py --write

Exit 0 at `eb4b0660`. `check-memory-hygiene.sh` propagates it, and the `memory hygiene` leg carries
`guard = None`, `subject = repo` — every bar, and the push boundary. The fold that closed *"the
anchor accounting was one short"* left the accounting wrong in the generated artifact instead.

**Fix.** `python tools/memory-tree/gotchas.py --write`, and commit `memory/gotchas/INDEX.md`
alongside the record edit. The only delta is the `5` to `4` on line 25. This is the standing DoD
rule — claim edits regen the generated artifacts in the same commit — not a new obligation.

**Left-shift gate.** Already gated; the leg caught it. The gap is upstream of the gate: nothing in
the pre-commit fast leg regenerates or checks derived memory artifacts, so the author sees this only
at push time. Add the `gotchas.py --check` call to `.githooks/pre-commit` when the diff touches
`memory/gotchas/`, which is cheap (stdlib, sub-second) and turns a push-time red into a commit-time
one.

---

## 3. HIGH — the D3 fix dropped the `$` anchor, and a truncated marked RHS is now ADMITTED

**`tools/hooks/agent-cap.js:234`** (mirrored byte-identically at `.claude/hooks/agent-cap.js`, which
is the wired copy).

This is a **net regression through the very tightening written to close D3**. The old predicate
anchored the marked right-hand side with `$`; the replacement walks the chain instead, and the walk
only rejects a top-level non-shrink call it can *see*. `rhs` is one stripped LINE. When the marked
assignment is truncated at the line end, the growing call sits on the next line, where nothing reads
it: it never enters `rhs` (so the `grows` veto never sees it) and it carries no `=` (so the bare-
reassignment sweep never sees it either). The walk ends with `links === 1` and `depth === 1` and
returns true.

**Evidence.** Piped as a real `Workflow` payload:

```
const ALL = [1,2,3,4,5]
const B = ALL.filter( // gov:fixed-verifiers
(L) => L.on
).concat(args.big)
await boundedParallel(B.map((x) => () => agent(x)), 5)
```

`rc=0` on `bc11601c` — **ADMITTED**. `rc=2` at `eb4b0660` ("the branch `ALL.filter(` is not one of
the bounded forms"). The trailing-operator variant escapes the same way with no growing method at
all — `const B = ALL.filter(f) || // gov:fixed-verifiers` with `args.big` on the next line: `rc=0`
new, `rc=2` old. The result is `agent()` fanning over a caller-supplied array of any length, which
is the unbounded burst this hook is the only mechanical control against.

**Fix.** Fail closed on an expression this file cannot see the end of. Either (a) after the walk,
require `depth === 0`, require it never went negative, and require the tail to end on the `)`/`]` of
a shrink link rather than mid-expression; or, better, (b) join the marked assignment forward until
its brackets balance — the array-literal branch already does exactly this with its
`while (j < code.length)` walk — and judge the JOINED text.

**Left-shift gate.** `tools/hooks/agent-cap.test.sh` has **no multi-line marked fixture at all**,
which is why this landed green. Add two arms: a marked assignment truncated at the line end whose
continuation grows the receiver, and the trailing-operator form. Stage both against today's code and
observe RED before wiring the fix.

---

## 4. HIGH — one `(` inside a template literal strands the depth walk

**`tools/hooks/agent-cap.js:225`** (mirror identical).

`fanoutFindings` builds its lines with `stripStrings` (line 70), which blanks `'…'` and `"…"` and
nothing else. The D3 replacement's depth walk counts brackets on that view, so a single unbalanced
`(` inside a backtick strands `depth > 0` and every later chain link is skipped as "nested".

**Evidence.**

```
const ALL = [1,2,3,4,5]
const LENSES = ALL.filter((L) => `(`.length > 0).reduce((acc, b) => args.big, []) // gov:fixed-verifiers
await boundedParallel(LENSES.map((L) => () => agent(L)), 5)
```

`rc=0` — ADMITTED. The byte-identical script with `L.length` in place of the template literal is
correctly DENIED (`rc=2`), so the escape is purely the unbalanced paren. `LENSES` is blessed bounded
while its runtime value is `args.big`: one agent per caller-supplied element, no total cap, in a
guard whose own header preaches FAIL CLOSED.

The file already ships the right view. `blankLiterals` (line 478) exists, and its own header at
lines 473-477 says in as many words that the per-line strip "cannot see a template literal" and that
"a `(` inside a prompt string unbalances a forward paren join". The plumbing was built for this gap
and rule 2 was not wired to it.

**Fix.** Run the depth walk over a template-aware view: give `fanoutFindings` the
`blankLiterals(script)` lines instead of `stripStrings`, or track a `tmpl` flag alongside `depth` in
the loop so backtick regions are skipped.

**Left-shift gate.** Add the repro above to `tools/hooks/agent-cap.test.sh` as an arm expecting exit
2, and confirm it RED against today's code before wiring the fix. While there, add the generalised
class: a marked assignment whose predicate body contains an unbalanced bracket of each kind
(`(`, `[`, `{`) inside a template literal.

---

## 5. HIGH — a computed-member link is never inspected by the shrink-only walk

**`tools/hooks/agent-cap.js:230`** (mirror identical).

The walk classifies only links that start with a literal `.`. A `[` merely increments `depth`, so
the `(` of a computed-member call is never reached by the `ch !== '.'` test. With one legitimate
shrink link in front of it, `links` is already 1 and the loop falls out returning true.

**Evidence.**

```
const ALL = [1,2,3]
const LENSES = ALL.filter((L) => L.on)["concat"](args.big) // gov:fixed-verifiers
await boundedParallel(LENSES.map((L) => () => agent(L)), 5)
```

`rc=0` — ADMITTED. The dotted spelling `.concat(args.big)` is correctly denied (`rc=2`, `grows`
veto), and `ALL["concat"](args.big)` with no preceding shrink link is also denied — the escape needs
exactly one legitimate link in front. The `grows` regex misses it independently, because
`\bconcat\s*\(` does not match `"concat"](`.

This one is **not** a regression — `eb4b0660` admitted it too — but the comment the fold wrote above
the loop asserts *"Every TOP-LEVEL call on the chain must now be shrink-only"*, and the code does not
enforce that. A claim in prose the code does not support, in a guard, is worse than a silent gap: it
tells the next reader the class is closed.

**Fix.** Deny any top-level `[` in the tail. Inside the loop, before the depth increment:
`if (depth === 0 && ch === '[') return false`. A computed member access is not one of the closed list
of qualifying forms, and no shipped caller writes one.

**Left-shift gate.** Add the fixture beside the existing D3 `.reduce` arm in
`tools/hooks/agent-cap.test.sh` and observe the RED. Pair it with the negative — `ALL["concat"](x)`
with no preceding link must stay denied for the *original* reason — so the arm distinguishes the two
paths.

---

## 6. MEDIUM — the D4 second view reads the RAW line, so rule 5 reds on comments and strings

**`tools/hooks/agent-cap.js:875`**.

The D4 fix added `${…}` interpolation spans as a second view for rule 5, and built them from
`raws[i]` — the fully unblanked source line — rather than from the blanked view. Comment text and
plain-string text that `blankLiterals` deliberately removes are therefore re-admitted.

**Evidence.** All three BLOCK (`rc=2`) on `bc11601c` and are clean (`rc=0`) at `eb4b0660`:

- a line comment: ``// The retired join looked like `${verdictByRef[f.ref]}` in the report body.``
- a single-quoted string: `const doc = 'the old shape was ${m[f.ref]} and it is gone'`
- a double-quoted string, where `${}` is not even an interpolation:
  `const doc = "never write ${verdictByRef.get(f.ref)} - it is retired"`

The same comment *without* `${}` exits 0, isolating the cause exactly.

Two things this refutes. `tools/workflows/check-review-join.sh:19-22` records that comment stripping
is **load-bearing** precisely because `tier2-review.js` documents the retired join in prose that has
to spell it — the gate would otherwise red on the documentation of its own fix. And the fold's own
comment at `agent-cap.js:866-873` asserts *"a mention inside a plain string stays out of scope"*,
which is the opposite of what the code does.

Reachability is real but latent: the unguarded `review-join ban (no ref-keyed join)` leg pipes every
tracked `*.js` under `tools/` through this predicate, and it is green today (`rc=0`) only because no
current file documents the join in interpolation form. `tier2-review.js:211` already carries such a
comment in non-interpolated form. The existing green `comment-only.js` fixture survives solely
because it happens to contain no `${}`.

**Fix.** Derive the interpolation spans from a comment-stripped, template-preserving pass over the
CODE line: a mode of the existing `blankLiterals` state machine that keeps `${…}` bodies inside
backticks while still dropping `//` and `/* */` comments and single/double-quoted string bodies.

**Left-shift gate.** Add three GREEN fixtures to `tools/workflows/check-review-join.test.sh` — a
comment carrying `${verdictByRef[f.ref]}`, a single-quoted string carrying `${m[f.ref]}`, and a
double-quoted one — plus one RED fixture that is a real template-literal join, so the narrowing and
the reach are pinned against each other rather than one at a time.

---

## 7. MEDIUM — the D9 arm is satisfied by the D9 prose

**`tools/workflows/tier2-review.test.sh:116`**.

The arm derives every field read off the `a` alias and asserts the args header documents each one,
using `hdr.includes(f)` — a bare substring test over the whole block from
`// --- inputs (via Workflow` to `// S5 (TOOL-aGuardedTally-1)`. That window contains the D9
explanatory paragraph the fold wrote at `tier2-review.js:36-40`, whose first sentence reads
"`kind` and `subjects` were added without extending this block".

**Evidence.** Staged the exact break the arm exists to catch — deleted **both**
`//   kind: "diff-review" | "spec-audit"` and `//   subjects: [{ path, blob }]` from the documented
field list — and the suite reported:

```
ok   the args header documents all 10 fields read off `a`
---- 17 passed, 0 failed ----
```

Restored. Four of the ten fields are satisfied by prose rather than by documentation: `kind` and
`subjects` by the D9 paragraph, `head` by the word "header", `repo` by "repo-relative". `path` would
be satisfied by the `"/path/to/worktree"` example text. The gate registered to prevent D9's
recurrence is blind to D9's own two fields — the two `BUILD-METHOD` M4 sends a reader to this block
for.

**Fix.** Build the documented set from field DECLARATION lines only, not from free text:
`const documented = new Set([...hdr.matchAll(/^\/\/\s*\{?\s*([A-Za-z_$][\w$]*):/gm)].map((m) => m[1]))`,
then `fields.filter((f) => !documented.has(f))`. Alternatively scope `hEnd` to the end of the `{ … }`
field list rather than to the `// S5` marker — but do both, because the substring test is unsound
even over a tight window.

**Left-shift gate.** This *is* the gate; it needs its failing case observed, which is the rule the
fold's own commit message claims to have followed ("every new gate was watched to RED before it was
landed"). Re-stage the two-line deletion, confirm RED, unstage. The generalisable form worth adding
to `tools/hooks/agent-cap.test.sh`'s sibling discipline: any arm asserting a documentation block
covers a derived set must be run against that block with the entries deleted.

---

## 8. MEDIUM — the header claims coverage of the base-shape ladder; the extraction excludes it

**`tools/workflows/tier2-review.test.sh:6`**.

The suite header names three things it covers: the spec-audit subject validator, **the base-shape
ladder**, and the args header. The extraction is `lines.slice(metaEnd + 1, stop)` with `stop` the
index of `const baseLooksPinned` (`tier2-review.js:159`), and `slice`'s end is exclusive — so line
159 and the whole warn-at-round-1 / refuse-at-round-2 moving-ref block below it are never in the
evaluated body. No arm supplies a non-sha base; every fixture inherits `base: 'a'.repeat(40)`.

**Evidence.** Staged the break: rewrote line 159 to `const baseLooksPinned = true`, which accepts a
moving ref like `origin/main` at every round and silently destroys the provenance anchor on every
review record this harness writes. Suite: `---- 17 passed, 0 failed ----`. `/baseLooksPinned/.test(body)`
is `false`.

The sting is placement. That claim sits four lines above a scrupulous `WHAT THIS DOES NOT CHECK`
paragraph, which names only things "downstream of the refusals" — and the base ladder *is* a
refusal, so the omission goes unnamed. A reader who trusts the header believes the base-pin refusal
is regression-covered when nothing touches it. This is the class this same fold added to the gotcha
catalogue as `degradation-known-but-unreported`, one file over.

**Fix.** Either move `stop` past the base block (anchor on `const reviewDir = a.reviewDir`) and add
three arms — moving ref at round 1 warns and proceeds, moving ref at round 2 throws naming
`immutable sha`, spec-audit with a moving ref proceeds because `isSpec` short-circuits — or delete
"the base-shape ladder" from line 6 and name it in the DOES-NOT-CHECK block. The first is preferable:
the refusal is cheap to exercise and has zero coverage anywhere in the repo.

**Left-shift gate.** The suite's own extraction assertion already proves the extraction "moved"; it
does not prove the extraction reaches what the header advertises. Add an assertion that the
evaluated body contains a token from each claim the header makes — e.g. `/baseLooksPinned/`,
`/badSubject/` — so a header claim and an extraction bound cannot drift apart silently.

---

## 9. LOW — the D10 reason is written for names that never had a bounded assignment

**`tools/hooks/agent-cap.js:348`**.

The D10 fix has the reassignment sweep state its own reason. It writes that reason for **every** bare
reassignment, including names that were never in `ok` and never carried the marker, so the refusal
asserts a bound that never existed. `ok.delete(m[1])` is a no-op for such a name; the `markedWhy.set`
beside it is not.

**Evidence.**

```
let items = args.everything
items = args.somethingElse
await boundedParallel(items.map((x) => () => agent(x)), 5)
```

`bc11601c`: "`items` was REASSIGNED after its bounded assignment, which takes the bound back".
`eb4b0660`: "agent() fanned over `items`, which this file does not show to be bounded" — the correct
line. The verdict is right in both, and only the stated reason is false, which is why this is LOW.
It is nonetheless D10's own failure mode inverted, in the same commit whose comment says a guard
whose stated reason is wrong is one an operator cannot act on: the author is sent to hunt a bounded
assignment that is not in the file.

**Fix.** `Set.prototype.delete` already returns whether the name was present, so this is one
character of restructuring: `if (ok.delete(m[1])) markedWhy.set(m[1], …)`.

**Left-shift gate.** Add the negative arm beside the new positive one in
`tools/hooks/agent-cap.test.sh`: a never-bounded name, reassigned, must be denied with the *generic*
text. Asserting on the message and not just the exit code is the point — the exit code was never
wrong.

---

## 10. LOW — "every tracked carrier" is false; the derived population is `*.js` only

**`tools/check-kit-versions.sh:51`**.

The D5 fix replaced a single named file with a derived population, which is the right move and does
catch the half-bump. The comment above it, though, reads *"Every tracked carrier of the marker is
compared to the constant now"*, and the population is `git grep -lE "gov:kit agent-cap@" -- '*.js'`.
Any non-JavaScript carrier is invisible.

**Evidence.** With the pathspec the grep returns the four hook copies. Without it, it also returns
`tools/check-kit-versions.sh` itself and eight `memory/builds/` records — so the pathspec is
genuinely load-bearing self-exclusion, and **nothing in the file says so**. Every sibling block in
this same file (run-gates, memory-recall, drift-audit, pytest-guardrails) asserts a marker in a
README or a shipped template, which is precisely the carrier shape this glob cannot see. No live
drift today: `tools/hooks/README.md` and `kit.toml` carry no version marker.

**Fix.** Either widen the pathspec to the kit's own directories (`-- 'tools/hooks/*' '.claude/hooks/*'`)
so non-`.js` carriers there are covered while records stay out, or narrow the comment to "every
tracked JavaScript carrier" and state that the glob *is* the self-exclusion mechanism. The first is
better; the second is honest.

**Left-shift gate.** Add an arm to the kit-versions self-test that plants a `gov:kit agent-cap@1.7`
marker in a scratch `tools/hooks/README.md` and asserts the checker names it. That turns the comment
into a claim the suite verifies, which is the only way a population claim stops being prose.

---

## 11. LOW — the D7 fix added exit-2 meanings the header contract does not document

**`tools/workflows/check-review-join.sh:7`**.

The header reads `Exit 0 = clean · 1 = a ref-keyed join reappeared · 2 = not a git repo`. The file
now has six exit-2 sites, two of them added by this diff: `:98` ("the predicate returned $rc … which
is neither clean nor a rule hit — refusing rather than reporting") and `:105` ("its own refusal and
not a join"). Exit 1 likewise now covers `:56`, "none of the named files exist", which is not a join
hit either.

One correction to the filing, which does not change the disposition: D7 added **two** of those
exit-2 paths, not four — the hook-absent and node-absent pair at `:74-75` pre-dates it.

An operator or a wrapper reading the header maps a predicate refusal onto "this is not a git repo"
and looks in the wrong place, and the two conditions want opposite responses. Impact is genuinely
low because every refusal prints its own explanatory line — but this is a copy-installed kit whose
header is the adopter's contract, the stale line is two lines from the code that changed, and it is
the same stated-status-is-not-the-real-status class D7 itself was.

**Fix.** Amend line 7 to: `# Exit 0 = clean · 1 = a ref-keyed join reappeared · 2 = the gate could
not run, or the predicate returned a status it cannot classify.`

**Left-shift gate.** Hard to gate honestly, and this repo's rule for that case is a documented check
rather than a fake one. The gateable half: a header that enumerates exit codes should enumerate all
of them, so a check that greps a kit script for `exit N` sites and asserts each distinct `N` appears
in the header's exit line is cheap and would have fired here. If that reads as over-built for one
file, record it in the recurring-bug-class checklist instead — an exemption with its compensating
check named.

---

## 12. LOW — the D8 correction adds a third `6-wide` hit under `tools/`, against AC11

**`tools/check-agent-cap-restatement.sh:37`**, against
**`memory/builds/dTieredTribunal/spec/2026-08-26-spec-dTieredTribunal-11.md:341`**.

AC11 declares: *"When `git grep -n -- "6-wide"` runs over the whole tree, no hit is under `tools/`"*.
At `eb4b0660` that grep returned two hits under `tools/` — `check-agent-cap-restatement.sh:35` and
`tier2-review.js` — so the criterion was already false. The D8 correction quotes the string again at
`:37`, making it three. The fold deepened the criterion's falsity while D8's stated subject was
reconciling exactly this prose.

The same string was raised as spec-audit round-1 finding 15 and round-2 finding 8. Nothing on the bar
watches it: `check-agent-cap-restatement.sh` reads markdown only and cannot see itself, so the
`6-wide` sweep is a manual acceptance criterion. The run has no acceptance ledger for units 11-15
yet, so AC11 is still live and will be graded against a tree where the grep returns three.

**Fix.** Either amend AC11 to permit past-observation quotations in this file, naming the file and
the string — or rewrite `:35` and `:37` without the literal `6-wide` token (e.g. "the second,
disagreeing width comment") so the declared grep and the tree agree without weakening the criterion.
The second keeps the criterion's shape, which is worth more than the example.

**Left-shift gate.** The criterion is a grep and greps are gateable. Add `6-wide` to whatever
forbidden-token sweep the bar already runs over `tools/` — or, if none exists, note in the acceptance
ledger that AC11 is graded by hand and by whom. A criterion that no leg can observe and that has been
false across two commits without anyone noticing is the argument for the leg, not against it.

---

## What the fold got right

Worth stating, because eleven of the twelve findings above are defects in repairs and that reads
harsher than the diff deserves.

D1 (`check-wiring.sh` — the `--only` guard bounded every character class with `[^"]*` against a
command that escapes its inner quotes, so it could never fire) is a real fix with a real observed
failing case: AC7d was watched RED against the old predicate at 75/1 and green at 76/76. D2's refusal
ladder for a zero-subject spec audit is correct at every round. D6's index sentinel is correct, and
the note that the review's own suggested fix reinstated the collapse one line lower — caught by the
new self-test on its first run — is exactly the value a self-test is supposed to return.

The new suite itself is the right thing to have built. Three of its arms are unsound and one of its
header claims is uncovered; seventeen arms over an argument contract that previously had zero remain
seventeen more than the harness had.

## Method

Five finder lenses over the fold's diff at the pinned range, then batched skeptics prompted to REFUTE
each finding by re-deriving it against the shipped file. Raw 24, confirmed 24, refuted 0, unverified
0 — precision 1.00, which is unusually high and reflects convergence rather than breadth: the twenty-
four reports are twelve defects, and the six most-reported are the six with mechanical reproductions
attached. Every reproduction quoted above was re-executed in this synthesis pass against
`tools/hooks/agent-cap.js` (verified byte-identical to the wired `.claude/hooks/agent-cap.js`) and
against the same file at `eb4b0660`, so every "net regression" claim in this record is an old-versus-
new pair, not an inference.

Not covered by this review: the review record `582101dd` added by the range is the round-1 closing
review's own artifact and was read as context, not audited. The fold's manifest re-stamp of
`memory/guides/SESSION-KICKOFF.md` was checked only for the fact that `tools/gate-legs.json` is
watched and the stamp moved; the §B claims it feeds were not independently re-derived.
