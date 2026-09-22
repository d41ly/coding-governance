# Counterfactual — the Explore arm, recall IN, reuse IN

**Serves:** journal TOOL-aReplayedCard-5

The return of `tools/workflows/orient-counterfactual.js` run `wf_237795b3-22b` on 2026-09-14 at
`7dbbf796`, written by the orchestrator as the harness's README says the caller does. One arm of
the eight-arm matrix; the other seven are the next session's, and the `orient` arms need the
definition present at session start (the AC3 observation in the acceptance ledger).

| run | type | outcome | tokens | wallMs | reason |
|---|---|---|---|---|---|
| 1 | Explore | spawned | 19665 | 299315 | — |
| 2 | Explore | refused-step | 19172 | 266116 | the agent could not execute a step: Step 1 fetch: `git fetch` (ref mutation) not run under the no-mutation rule — substituted `git fetch --dry-run origin` (nothing new); ff-merge was inapplicable anyway (not on default branch). Everything else in Steps 0-4 ran. |
| 2 fallback | default | spawned | 28546 | 472483 | fallback for `Explore` |

- verdict: `partial: 1/2 runs spawned` · sequential: `True`
- tokens: each `tokens` is the budget.spent() delta around that spawn: the OUTPUT tokens the workflow spent while the agent ran, not the subagent's total context and not the main loop's occupancy
- wall: each `wallMs` is endMs - startMs as the agent itself read `date +%s%3N` at its first and last Bash call; the harness stamps no time
- task: Add a --version verb to tools/check-line-length.sh that prints the declared LINE_MAX and exits 0, with one self-test arm; Tier-1, tooling stream. Derive the closed scope, acceptance and gates; do not build.

## The two READY lines the spawned runs returned

Run 1 (Explore):

```
Ready — say go and I'll start, or adjust any field. (repo C:/projects/coding-governance/.claude/worktrees/session-orientation-tooling-2faa9f · branch/session-orientation-tooling-2faa9f · BASE 7dbbf796dbe6b439eb59d96a906a7360895fe215 · origin/main · manifest memory/guides/SESSION-KICKOFF.md audited exit 0, delta none · slug none · Tier-1 tooling)
```

Run 2 fallback (default type):

```
READY — none · node a · branch/session-orientation-tooling-2faa9f · base 7dbbf796dbe6b439eb59d96a906a7360895fe215 · Tier-1 · gates bash tools/check-line-length.test.sh (the `line-length gate selftest` leg, HELD on the default bar — run it directly or with GATE_SELFTESTS=1) · line length · install-prefix (shipped surface) · harness arms (fail branches armed or pinned) · lexicon naming predicates · testsuite counts · govkit acceptance matrix · bash tools/run-gates/run-gates.sh
```

## What the arm says about stage 2, and what it does not

One arm is not the matrix. What it shows: an Explore-typed agent runs Bash, the recall probe and
the reuse probe, derives the closed scope and returns a card of about 8 KB; it refused one step of
the engine — the fetch — on its own reading of a no-mutation rule, which the default type did not;
and the default type spent 45% more output tokens and 58% more wall on the same task. Whether
either occupancy figure beats the inline kickoff is the comparison the matrix run makes, against a
main-loop kickoff measured the same way; nothing here measures the main loop.
