# The owner's prompt — fix the round-2 blockers, re-verify, then merge

**Serves:** research TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-10 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12

Handed to `/unattended --prompt` on 2026-08-31, node `a`. The value carried whitespace and named no
readable file, so it is the prompt itself and is recorded here verbatim. The bytes travel rather than
the reference, because the build folder is the authorization and may not point at a file that can be
edited after the run starts.

```
Fix the 5 blockers + 2 highs, re-verify, then merge
```

## What it refers to, so the record stands alone

The closing diff review of this build, round 2, returned **BLOCKED**: 20 raw findings, 19 confirmed,
precision 0.95, collapsing to 13 distinct defects — 5 blockers, 2 highs, 4 mediums, 2 lows. It is
`reviews/2026-08-30-review-TOOL-aPairedLexer-1-2-3-4-diff-round2.md`.

Four of the five blockers are measured DENY-to-ADMIT regressions against already-shipped code, and
`bash tools/hooks/agent-cap.test.sh` printed `125 passed, 0 failed` with every one of them live.

## Why these become UNITS rather than a fold

M4's convergence rule. Round 1 confirmed **2** blockers; round 2 confirmed **5**. Five is not
strictly smaller than two, so the review loop is **NON-CONVERGENT** and STOPS. Every blocker still
standing is PROMOTED to a unit of this build — specced at its tier, built, closed; not parked, not
waived, and not re-reviewed as a diff. A promoted unit is audited as a SPEC, which is what makes
promotion terminate.

The owner named the 2 highs alongside the 5 blockers, so seven units are promoted rather than five.

## The prior turn this replaces

The owner was asked whether to fix-then-merge or merge as-is, and answered by handing this prompt to
`/unattended`. That is the last owner turn: from preflight onward there is nobody to ask, and the
answers to anything still open have to be derived, adopted, parked or aborted.
