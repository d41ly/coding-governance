# TOOL-aWeldedTribunal-3 — acceptance ledger

**Serves:** journal TOOL-aWeldedTribunal-3

## What changed

`renderBlankedView` returns `{ code, unterminated }`. The `renderBlankedLiterals` dispatcher wraps
the FROZEN `renderShippedBlanks` as `{ code: …, unterminated: false }` without editing it. A new
`perLineBlanked` runs the same scan with the mode reset per line, and `capFindings` (rule 3) and
`scanJoinFindings` (RULE 5) take it when the primary scan ended inside a literal. Seven arms added.

## Each criterion, answered

Every row measured against `git show HEAD:tools/hooks/agent-cap.js` — the tree with units 1 and 2 and
without this one — and against the built tree.

- **AC1** — an over-cap `K` on a BOUNDED receiver, below an unterminated backtick: **0 → 2**. The
  receiver must be bounded or rule 2 denies it in both trees; the first draft of this criterion used
  an unbounded one and measured 2 → 2, observing nothing.
- **AC1 control** — the same script with the backtick terminated: **2 → 2**. The difference is
  attributable to the unterminated literal, not the cap.
- **AC2** — a legal multi-line backticked prompt with a bounded fan: **0**.
- **AC3** — `renderBlankedLiterals` returns `{ code, unterminated }` from both arms.
- **AC4** — a ref-keyed join below an unterminated backtick: **0 → 2**. RULE 5 was blind and is not.
- **AC5** — a legal join under a terminated multi-line literal: **0**.
- **AC5b** — banned text inside a single-line terminated template: **0 → 0**. The narrowing holds
  within a line.
- **AC5c** — banned text on a CONTINUATION line under an unterminated backtick: **0 → 2**. The
  RESIDUAL, and it has an arm.
- **AC6** — `bash tools/hooks/agent-cap.test.sh`: **188 passed, 0 failed, exit 0**.
- **AC7** — every tracked harness still exits 0.

## The gate that caught me, and what it proves

The first cut edited `renderShippedBlanks` to return the new shape. The suite failed with
`FAIL no-regress: a renderShipped* body has drifted from BASE` — a byte-compare arm freezing the
three `renderShipped*` bodies, because they ARE the baseline that makes `runBothViews`'s union sound.
The dispatcher now wraps that arm instead.

That is worth recording as a positive result: this build spent two review rounds on criteria that
could not fail, and here a shipped arm caught a real design error on the first run. The arm was
written by an earlier unit and it earned its keep.

## The trade, stated rather than claimed away

A per-line fallback cannot know a line CONTINUES a template opened above it. So banned text on a
continuation line reads as code and denies — AC5c, 0 before and 2 after. It needs an unterminated
backtick AND banned text on a continuation line, and it errs fail-CLOSED, which is the direction this
file's posture prefers. Rule 2 took the same trade for the same reason.

One fixture looked like a regression and is not: banned text on a line carrying TWO backticks, under
an unterminated one, exits 2 both before and after. The frozen shipped view's cross-line mode makes
that line's first backtick a CLOSER, so the text between them has always read as code. Recorded
because the first reading of it cost twenty minutes.

## Evidence

**Evidences:** TOOL-aWeldedTribunal-3
- AC1 — amended rev-4 — the original criterion could not observe rule 3 at all; respelled onto a bounded receiver with an over-cap K, logged in section 9
- AC2 — `node tools/hooks/agent-cap.js` — a legal multi-line backticked prompt with a bounded fan exits 0
- AC3 — `tools/hooks/agent-cap.js` — the dispatcher returns a code-and-unterminated pair from both arms
- AC4 — `node tools/hooks/agent-cap.js` — a ref-keyed join below an unterminated backtick exits 2 where it exited 0 before
- AC5 — `node tools/hooks/agent-cap.js` — a legal join under a terminated multi-line literal exits 0
- AC5b — `bash tools/hooks/agent-cap.test.sh` — banned text in a single-line terminated template exits 0
- AC5c — amended rev-5 — the narrowing is a TRADE and not a preservation; the residual is pinned by its own arm, logged in section 9
- AC6 — `bash tools/hooks/agent-cap.test.sh` — 215 passed, 0 failed
- AC7 — `node tools/hooks/agent-cap.js` — `tier2-review.js` exits 0
