# Fix brief — the unbuilt specs ordered 12 to 20, re-grounded so each dispatch passes the spec-token checker

**Serves:** research TOOL-dFairHearing-10 TOOL-dFairHearing-22 TOOL-dFairHearing-12 TOOL-dFairHearing-14 TOOL-dFairHearing-1 TOOL-dFairHearing-21 TOOL-dFairHearing-15 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26

## The prompt

> /unattended dFairHearing

— owner, 2026-11-02, the invocation that started this build run.

## The brief

### Goal
Make every spec in this set pass `tools/check-spec-tokens.py` the moment the main loop flips it to INPROGRESS, so no builder pass is spent on a refusal. The checker grades only live specs, so these were never graded against today's tree. The set: units 10, 22, 12, 14, 1, 21, 15, 17, 18, 20, 23, 25 and 26. Read `memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-10-1-builder-return.md` first: it is the refusal this sweep exists to pre-empt. Commit nothing; the main loop commits.

### Items
1. **Guards join.** For each spec, read its §4 Files touched and its §7 leg line, and the leg guards in `tools/gate-legs.json`. Every leg whose guard a files-touched path trips must be named on the §7 leg line; add each missing one. Units 13 to 16 have moved files since these specs were written (`tools/hooks/agent-cap.js` is now 947 lines and lost rules 0, 2 and 5 to `tools/workflows/check-verifier-fanout.js`, `tools/workflows/check-review-join.js` and `tools/workflows/spec-audit-optin.js`); where a spec's files-touched names a path whose content moved, re-point it, never keep a stale path.
2. **Cites past a file's end.** Every `path:line` that points past the file's end today, or at a line whose content moved, is re-cited at HEAD, by symbol where the line will move again.
3. **Base-pinned comparisons.** A criterion comparing against base `3708a705` that today's tree already reds, through other builds' changes, is re-pinned to the tree the build pass starts from (its commit's parent), as unit 13's AC2 was.
4. Unit 10 is the refusal itself: its §7 leg line lacks `policy fixtures`, which `tools/hooks/agent-cap.js` in its §4 trips. Units 22 and 23 cite `agent-cap.js` lines past 947 (`:1491`, `:1782`, `:1880`; `:1362`).
6. Every spec touched: rev bump and one §9 line per change, naming this brief. Leave each status header's state as it is. A finding that needs a design change rather than a re-ground is reported, not made.

### Acceptance
Each spec in the set: its §7 leg line names every leg its §4 trips; no cite past a file's end; no base-pinned criterion today's tree reds. The return lists each spec with its rev and what changed, or "no change".

### Gates
None you run: the spec-token checker is the main loop's.

### Non-goals
No design change, no clause change, no code, no write outside this set's specs.
