# Fix brief — TOOL-dFairHearing-16 and its hook siblings, re-grounded on the hook dGroundRules left

**Serves:** research TOOL-dFairHearing-16 TOOL-dFairHearing-22 TOOL-dFairHearing-26 TOOL-dFairHearing-28 TOOL-dFairHearing-29

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-16.md` so a correct build of it passes on today's `tools/hooks/agent-cap.js`, and re-ground the four unbuilt specs that build on the same hook so they agree with it and with each other. The builder's DIVERGENCE is `memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-16-1-builder-return.md`; read it first. Commit nothing; the main loop commits.

### Items
1. Re-measure unit 16's §4 Evidence at HEAD, not `3708a705`: dGroundRules (TOOL-dGroundRules-10, -18, -21, -61, -73, -78) retired rules 1, 3 and 4, the slot ledger, `EFFECTIVE_CAP` and `loadDeclaredCap`, and the hook keeps rules 6, 7, 0, 2 and 5.
2. S1 and AC1 name the exports that exist at HEAD (`runBothViews`, `extractBuildSlug`, `extractWorkflowArgs`, `MAX_VERIFIERS`, `readWriterBound`), never a retired one.
3. S2, S3, AC3 and AC5: once rules 2 and 5 move out, the hook's `--only=scripts` mode and its script read run no rule. Say what happens to them. If the choice between deleting the mode (both gates stop delegating to the hook) and keeping it is a real fork, mark it in §8 by M3 and resolve it as delegated, `RESOLVED (agent, 2026-11-03, delegated)`, with M3's reason; a mode that runs no rule is the vacuous-selector class and cannot survive the [gate] rule. Rewrite AC3 and AC5 so each can go red.
4. §3 Non-goals stops listing as staying in the hook anything that is already gone. S7 and AC11 read the version baseline at HEAD (agent-cap 1.42).
5. Run M2's cross-read over units 16, 22, 26, 28 and 29 on its four axes. Each of 22, 26, 28 and 29 that cites a retired rule, a stale census, a stale line or a base-pinned comparison today's tree already reds is fixed to HEAD, in that one spec. Units 28 and 29 pin the hook suite's census: re-count at HEAD, and say where the count came from.
6. Every spec touched: rev bump and one §9 line per change, naming this brief. Leave each status header's state as it is.

### Acceptance
Each touched spec at its next rev: every criterion a correct build can pass on today's tree; no export, rule or mode named that HEAD lacks; §9 lines for each change. `python tools/check-spec-tokens.py`, run bounded at 1800000 ms, names no new finding.

### Gates
`python tools/check-spec-tokens.py` only. No gate leg, suite or bar.

### Non-goals
No change to the clause each unit carries. No code, and no write outside those five specs.
