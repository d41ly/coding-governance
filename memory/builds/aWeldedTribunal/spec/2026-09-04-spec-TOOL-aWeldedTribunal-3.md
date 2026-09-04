# TOOL-aWeldedTribunal-3 — the blanked view reports an unterminated scan, and its readers fall back

**Status:** OPEN · rev-3 · 2026-09-04 · node a · Tier-2 · base 9b5ae688 · streams tooling · order 3

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
- **S2** — `renderShippedBlanks`, the other half of the `renderBlankedLiterals` dispatcher, returns
  the same shape. A dispatcher whose two arms return different shapes is a defect the caller has to
  know about, which is what the dispatcher exists to prevent.
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
- **S6** — **The fallback branch must PRESERVE the narrowing `TOOL-dTieredTribunal-14 S2` bought.**
  `agent-cap.js:1406-1409` records choosing `renderBlankedLiterals` for the join rule as "a
  deliberate NARROWING: the awk kept string CONTENTS and only stripped comments, so it matched the
  retired identifier inside a string", pinned by two self-test fixtures in both directions. The
  fallback view `renderStrippedView(l).split('//')[0]` LEAVES BACKTICKS ALONE (`:1435-1437`), so on
  the unterminated branch RULE 5 would test template contents intact against its BANS and regain
  exactly that false-positive class — and `runBothViews` UNIONS the views, so a false positive under
  either denies. Either the fallback keeps the narrowing, or the trade is stated and priced. §8
  carries the fork.
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
lines. Neither returns it. The change is the return statement:

```js
  return { code: out, unterminated: mode !== 'code' }
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

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — two return statements, two call sites.
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

- **AC1** — When a script carrying an unterminated backtick above an unmarked per-finding fan is
  piped to `node tools/hooks/agent-cap.js`, it exits `2`. Rule 3 sees the fan under the fallback
  view where it saw nothing under the blanked one.
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
- **AC5b** — When a script carrying an unterminated backtick above a line whose TEMPLATE CONTENTS
  mention a banned pattern is piped to `node tools/hooks/agent-cap.js`, `scanJoinFindings` reports
  NOTHING. This is S6, and it is the arm that pins `TOOL-dTieredTribunal-14 S2`'s narrowing onto the
  fallback branch. Rev-2's AC5 tested only a terminated literal, so the class could ship under it.
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
  view leaves template contents intact, and RULE 5 was deliberately given a view that blanks them.

  **Option A, keep the narrowing:** on the unterminated branch, RULE 5 falls back to a view that
  still blanks template CONTENTS — the per-line stripped view is not it, so this needs the blanked
  view's own per-line degradation rather than `renderStrippedView`.

  **Option B, trade it:** accept the false-positive class on the unterminated branch, on the ground
  that an unterminated backtick is already a degraded input.

  RESOLVED (agent, 2026-09-04, delegated): **Option A**. Option B fails M3's veto 1 — it would
  reintroduce a class two shipped self-test fixtures exist to pin, which is an acceptance criterion
  already written into the file this unit edits. The narrowing was bought deliberately and a unit
  whose goal is to close a fail-OPEN may not open a fail-CLOSED in the same edit. S6 states it and
  AC5b observes it.

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

## 10. Reuse audit

The seam is `renderLexedView` and `fanoutFindings`'s fallback branch in the same file — the file's
existing answer to "the scan ended inside a literal, so do not trust this view". This unit copies
that shape onto the sibling view rather than inventing a second disposition. Located by
`python tools/codebase-map/reuse_lookup.py "fan-out cap hook scans a script for loop shapes and
array literals"`, which ranked `renderBlankedLiterals`, `resolveLiteralEnd` and `checkLiteralOpen`
in that file.

Recall terms used: `--terms "agent-cap blankLiterals capFindings fanoutFindings landed phase check34
lander marker unrepairable govkit renormalize memory-tree conf"`
