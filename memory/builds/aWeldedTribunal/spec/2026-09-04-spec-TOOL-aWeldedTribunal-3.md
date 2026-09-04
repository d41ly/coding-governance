# TOOL-aWeldedTribunal-3 — the blanked view reports an unterminated scan, and its readers fall back

**Status:** CLOSED · rev-5 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round1.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |
| [2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md](../reviews/2026-09-04-review-TOOL-aWeldedTribunal-1-8-round2.md) | spec-audit | TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8 |

<!-- /gen:spec-records -->

## 1. Goal

`renderBlankedView` in `tools/hooks/agent-cap.js` carries its `mode` across lines, so one
unterminated template literal blanks every line below it and the two rules that read that view see
nothing under it. The sibling view `renderLexedView` already reports whether its scan ended inside a
literal, and rule 2 falls back to the per-line view when it did. Give the blanked view the same
report and its two readers the same fallback.

## 2. Scope (IN)

- **S1** — `renderBlankedView` returns `{ code, unterminated }` instead of a bare array, matching
  the shape `renderLexedView` already returns.
- **S2** — The `renderBlankedLiterals` DISPATCHER returns one shape from both arms, and it does so
  WITHOUT editing `renderShippedBlanks`. The three `renderShipped*` bodies are FROZEN — a self-test
  arm byte-compares them against BASE, because they ARE the no-regression baseline that makes
  `runBothViews`'s union sound. The shipped arm is wrapped as `{ code: renderShippedBlanks(script),
  unterminated: false }`: the fallback improvement belongs to the corrected view, the union adds its
  findings, and the baseline stays a baseline.
- **S3** — `capFindings` (rule 3) falls back to the per-line view when the scan was unterminated,
  in the exact shape `fanoutFindings` uses: `view.unterminated ? lines.map((l) => renderStrippedView(l).split('//')[0]) : view.code`.
- **S4** — `scanJoinFindings` (the file's **RULE 5**, at `agent-cap.js:1398`) takes the same
  fallback. It reads the same view and has the
  same exposure; fixing one reader and not the other is the `gate-the-class-not-the-instance`
  failure, one level up.
- **S5** — Arms in `tools/hooks/agent-cap.test.sh`: a script whose fan sits BELOW an unterminated
  backtick must be DENIED, and a script with a legal multi-line template literal must still be
  ADMITTED. Both directions, because the whole point of the fallback rather than a fail-closed
  branch is that fail-closed denied legal scripts.
- **S6** — **The fallback preserves the narrowing WITHIN a line, and NOT across a continuation
  line.** That is a trade, it is measured, and it is stated rather than claimed away.
  `TOOL-dTieredTribunal-14 S2` chose the blanked view for RULE 5 so a banned pattern inside a STRING
  would not match, pinned by two fixtures. The fallback is the SAME scan with the mode reset per
  line, so a single-line template still has its contents blanked — but a line that merely CONTINUES
  a template opened above cannot be recognised as one by a per-line view, and its text reads as code.
  §8 F1 resolves the trade and §4 carries the two measurements.

- **S7** — The fallback is run over the tracked harnesses BEFORE wiring, printing hits and
  near-misses, per the charter's §7 rule. Units 1, 2 and 5 all carry this item and rev-2 of this one
  did not; it is what refuted unit 2's vocabulary before a line was written.

## 3. Non-goals (OUT)

- **Failing closed on the flag.** `TOOL-aLexedStripper-5` measured that and it denied a legal script
  carrying a regex literal with a backtick in it. The fallback is the decided disposition and this
  unit copies it rather than re-opening it.
- **Modelling regex literals.** The standing residual of the lexed view, unchanged here. A backtick
  inside `/…/` still opens template mode and never closes; that script now falls back instead of
  being read blind, which is strictly better and is not a claim that the residual is gone.
- **Changing what the blanked view blanks.** It blanks template CONTENTS including `${…}` bodies,
  and that is deliberate for these two rules. Only the REPORT and the FALLBACK are added.

## 4. Design

### Data model

`renderBlankedView` and `renderShippedBlanks` each already carry a `mode` variable across the
per-line loop, for the correct reason that a template literal and a block comment genuinely span
lines. `renderBlankedView` gains the report; `renderShippedBlanks` does NOT, because it is frozen (S2). The
change to the corrected view is one return statement, and the dispatcher supplies the shipped arm's:

```js
  return { code: out, unterminated: mode !== 'code' }        // renderBlankedView
  return { code: renderShippedBlanks(script), unterminated: false }   // the dispatcher's shipped arm
```

`renderLexedView` spells the same idea as `stack.length > 0 || mode !== 'code'` because it tracks
interpolation nesting on a stack; the blanked views have no stack, so the mode alone is the whole
condition and the fold records that the two spellings differ for that reason rather than by
accident.

### Why the mode is NOT moved inside the loop

The row that names this defect proposes moving `let mode` inside the per-line loop. That is wrong
and would be a regression: a template literal and a block comment legitimately span lines, and
resetting the mode per line would un-blank the second and later lines of every multi-line template
in every harness this hook reads — which is most of them, because a lens prompt IS a multi-line
backticked literal. The row's own next sentence names the right fix, which is that rule 3 should
consume the same signal rule 2 already has. This unit builds that one.

### Inventory

| Reader | Rule | Reads | Fallback today |
|---|---|---|---|
| `fanoutFindings` | 2 | `renderCodeView` | yes, on `view.unterminated` |
| `capFindings` | 3 | `renderBlankedLiterals` | none — this unit adds it |
| `scanJoinFindings` | 5 | `renderBlankedLiterals` | none — this unit adds it |

### The trade, measured

Five fixtures, each run against `git show HEAD:tools/hooks/agent-cap.js` (the tree with units 1 and
2, without this one) and against the built tree:

| Fixture | pre | post |
|---|---|---|
| an over-cap `K` on a bounded receiver, below an unterminated backtick (rule 3) | 0 | **2** |
| the same with the backtick terminated (control) | 2 | 2 |
| a ref-keyed join below an unterminated backtick (RULE 5) | 0 | **2** |
| banned text inside a single-line, terminated template | 0 | 0 |
| banned text on a CONTINUATION line under an unterminated backtick | 0 | **2** |

Rows one and three are the fix. Row four is the narrowing surviving within a line. **Row five is the
residual**: a per-line view reads a continuation line as code, so banned text there becomes visible.
It needs an unterminated backtick AND banned text on a continuation line, and it errs fail-closed.

A sixth fixture — banned text on a line carrying TWO backticks, under an unterminated one — exits 2
both before and after, because the FROZEN shipped view's cross-line mode makes that line's first
backtick a CLOSER and the text between them reads as code. That is pre-existing baseline behaviour
this unit neither causes nor changes, and it is recorded because a first reading of it looked like a
regression.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — one return statement, one dispatcher wrap, one new per-line view,
  two call sites. `renderShippedBlanks` is NOT touched; S2 says why.
- `tools/hooks/agent-cap.test.sh` — the arms of S5.

### Alternatives rejected

- **Give only rule 3 the fallback.** Rejected: RULE 5 reads the same view through the same
  dispatcher and has the same hole. Fixing the instance the row happened to name and leaving the
  sibling is the shape the charter names as certifying coverage you do not have.
- **A second character scanner for the blanked view.** Rejected: the file already carries four
  views and a fifth is more surface with no new answer.

## 5. Production-readiness checklist

- security — this is the security surface. The change removes a fail-open path in two of the file's
  five rules — rules 3 and 5. `RULE 4` is the direct-`Agent` arity rule at `:1214` and reads neither
  view.
- perf / scale — the fallback runs a second, cheaper per-line render only on the unterminated
  branch, which is rare by construction.
- a11y — N/A — a stdin CLI with no interface.
- i18n — N/A — the surface is JavaScript source.
- error / empty / loading states — N/A.
- observability — no new message. The denial a fallback produces is whatever the per-line view's
  rule already says, so no arm can strand on a message edit.
- risks — the real risk is that the fallback view is a DIFFERENT view and therefore a different
  verdict. `runBothViews` already evaluates every rule over the shipped views too, which is the
  no-regression property `fanoutFindings` relies on for the same branch; this unit inherits it.
- testing + left-shift gates — S5's arms. The class is
  `memory/gotchas/a-pair-exists-and-it-is-the-wrong-one.md`, which the checklist selects for this
  file.
- migration / rollback — none; one file, reverts cleanly.
- user docs — none; the view dispatcher is internal and `tools/hooks/README.md` documents the
  marker grammar, not the views.

## 6. Acceptance criteria

- **AC1** — When a script carrying an unterminated backtick above a line that rule 3 ALONE would
  refuse — a BOUNDED receiver with an OVER-CAP `K`, `boundedParallel(LENSES.map(…), 50)` under
  `const LENSES = [1,2,3]` — is piped to `node tools/hooks/agent-cap.js`, it exits `2`.
  **The receiver must be bounded and the K over-cap**, or the script is denied by rule 2 for its
  receiver and the criterion observes nothing: measured, an `allFindings.map(…)` fixture exits 2
  both before and after this unit. The isolating pair carries a CONTROL — the same script with the
  backtick terminated — which must exit `2` on both sides, so the difference is attributable to the
  unterminated literal and not to the cap.
- **AC2** — When a script with a legal multi-line backticked lens prompt and a bounded fan is piped
  to the hook, it exits `0`. The fallback must not deny what the blanked view correctly admitted.
- **AC3** — When `renderBlankedLiterals` is called under both `VIEW_MODE` values, both arms return
  an object carrying `code` and `unterminated`. A dispatcher with two return shapes is what S2
  closes, and this criterion is what makes S2 observable.
- **AC4** — When a script whose banned JOIN sits BELOW an unterminated backtick is piped to the
  hook, `scanJoinFindings` (RULE 5) reports it. This is S4, and without its own criterion the minimum work that stops
  RULE 5 crashing after S1 changes the return type is appending `.code` at `agent-cap.js:1413` —
  which passes every other criterion here whole while leaving RULE 5 blind. That is the
  gate-the-class-not-the-instance failure S4 exists to prevent, shipped under a green spec.
- **AC5** — When a script carrying a legal multi-line template literal above a legal join is piped
  to `node tools/hooks/agent-cap.js`, `scanJoinFindings` reports nothing. The negative half of the
  AC4 pair, for the same reason AC2 is the negative half of AC1's.
- **AC5b** — When a script whose banned text sits inside a SINGLE-LINE, terminated template is piped
  to `node tools/hooks/agent-cap.js`, `scanJoinFindings` reports NOTHING — 0 before this unit and 0
  after. This is S6's surviving half: the per-line fallback still blanks a template's contents within
  a line, so `TOOL-dTieredTribunal-14 S2`'s narrowing holds there.
- **AC5c** — When the banned text sits on a CONTINUATION line under an unterminated backtick, the
  hook exits `2` where it exited `0` before. This is the RESIDUAL, and it is an acceptance criterion
  rather than a footnote because a residual nobody measured is a residual nobody can price. §8 F1
  resolves the trade and §4 tabulates all five fixtures.
- **AC6** — When `bash tools/hooks/agent-cap.test.sh` runs, every pre-existing arm still passes.
- **AC7** — When `tools/workflows/tier2-review.js` is piped to the hook, it exits `0`. That file
  contains the multi-line prompt literals this change is most likely to mis-read.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for the `agent-cap self-test` leg, which is
`subject = kit` in `tools/gate-legs.json` and is therefore held as `ondemand` by
`tools/run-gates/run-gates.sh:947` on the plain bar. `AGENTS.md` records that no boundary sets
`GATE_SELFTESTS` (owner, 2026-08-27) and that a DoD owes the full pair for KIT work. The
`agent-cap restatement` leg is `subject = repo` and does run on the plain bar.


**The FULL PAIR, not half of it.** `AGENTS.md:488` spells the DoD command for KIT work as
`GATE_FULL=1 GATE_SELFTESTS=1`; `GATE_SELFTESTS=1` alone lifts the `ondemand` hold but leaves every
per-leg GUARD in force, so kit legs outside the touched directory stay held with no `skipped` line
saying which. Rev-2 cited the pair and prescribed one half of it.
## 8. Open questions

- **F1 · Does the fallback branch keep RULE 5's narrowing, or knowingly trade it?** The fallback
  view cannot know a line continues a template opened above it.

  **Option A, keep the narrowing everywhere:** impossible with a per-line view, and a cross-line view
  is the thing that went blind in the first place. Not available.

  **Option B, per-line fallback, narrowing kept WITHIN a line and traded across a continuation:**
  what is built.

  **Option C, no fallback for RULE 5:** leaves the fail-open this unit exists to close.

  RESOLVED (agent, 2026-09-04, delegated): **Option B**, and the trade is MEASURED rather than
  asserted — §4 carries both numbers. Option A does not exist once the view is per-line, which the
  measurement made plain and rev-3's wording did not. Option C fails veto 1: S4 is a scope item and
  leaving RULE 5 blind is the defect. The residual is narrow — it fires only on a script whose scan
  ALREADY ended inside a literal, and only on banned text sitting on a continuation line — and it
  errs fail-CLOSED, which is the direction this file's own posture prefers. Rule 2 took the same
  trade for the same reason and recorded its own residual the same way.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The defect was confirmed by reading
  `tools/hooks/agent-cap.js:1039-1072`, where `let mode` is declared above the per-line loop and the
  function returns a bare array. The row that names it cites a line number and a function name that
  no longer exist in the file; the defect does, at the renamed function.
- rev-2 · 2026-09-04 · folded spec-audit round 1 (H4, H7). **H4, high:** S4 scopes rule 4
  `scanJoinFindings` and rev-1's criteria observed rule 4 nowhere — AC1 was a per-finding fan
  (rule 3), AC3 pinned only the dispatcher's return shape, and the rest were negative or regression
  arms. So the cheapest build satisfying rev-1 was to append `.code` at `:1413` and leave rule 4
  blind, which is the exact failure S4 exists to prevent. AC4 and AC5 are the mirrored pair for rule
  4; the old AC4 and AC5 are renumbered AC6 and AC7. **H7:** §7 named the plain bar for a
  `subject = kit` leg that `run-gates.sh:947` holds; corrected to `GATE_SELFTESTS=1`.

- rev-3 · 2026-09-04 · folded spec-audit round 2 (H4, M10, M11). The loop exited NON-CONVERGENT at
  round 2, so this is the disposing fold and there is no round 3. **H4, high:** the fold's fallback
  re-opened the false-positive class `TOOL-dTieredTribunal-14 S2` narrowed away — the fallback view
  leaves backticks alone, so RULE 5 would test template contents against its BANS, and `runBothViews`
  unions the views so a false positive under either denies. S6, S7, F1 and AC5b close it. **M11:**
  this spec called `scanJoinFindings` "rule 4" throughout; the file's own numbering makes it RULE 5
  (`:1398`), and RULE 4 is the direct-`Agent` arity rule at `:1214` which reads neither view. A wrong
  POINTER, not a stale count — a verifier following the number lands on a function that cannot
  satisfy AC4. **M10:** §7 prescribed half the pair it cited.

- rev-4 · 2026-09-04 · corrected AC1 at BUILD time, before closing. Rev-3's AC1 named "an unmarked
  per-finding fan" below the unterminated backtick, and that fixture exits 2 BEFORE this unit as well
  as after — rule 2 denies it for its unbounded receiver, so the criterion could not observe rule 3
  at all. This is the same class the round-1 and round-2 audits found four times between them, caught
  here by RUNNING the criterion rather than reading it. AC1 now uses a BOUNDED receiver with an
  over-cap K, which only rule 3 refuses, and carries a terminated control. Measured: the isolating
  fixture is 0 before and 2 after; the control is 2 on both sides. The spec was fixed before the unit
  was closed, per M2.

- rev-5 · 2026-09-04 · corrected at BUILD time, twice, both times by RUNNING the thing rather than
  reading it. **First: the frozen shipped view.** Rev-4's S2 had `renderShippedBlanks` return the new
  shape. The self-test caught it — `FAIL no-regress: a renderShipped* body has drifted from BASE` —
  because a byte-compare arm freezes the three `renderShipped*` bodies as the baseline that makes
  `runBothViews`'s union sound. The dispatcher now wraps the shipped arm instead, and that arm firing
  is the gate working exactly as designed. **Second: the narrowing is a TRADE, not a preservation.**
  Rev-4's F1 resolved "keep the narrowing" as though a per-line view could; it cannot know a line
  continues a template above it. §4 now carries five measured fixtures, AC5b keeps the half that
  survives, and AC5c pins the residual rather than leaving it unstated.

## 10. Reuse audit

The seam is `renderLexedView` and `fanoutFindings`'s fallback branch in the same file — the file's
existing answer to "the scan ended inside a literal, so do not trust this view". This unit copies
that shape onto the sibling view rather than inventing a second disposition. Located by
`python tools/codebase-map/reuse_lookup.py "fan-out cap hook scans a script for loop shapes and
array literals"`, which ranked `renderBlankedLiterals`, `resolveLiteralEnd` and `checkLiteralOpen`
in that file.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
