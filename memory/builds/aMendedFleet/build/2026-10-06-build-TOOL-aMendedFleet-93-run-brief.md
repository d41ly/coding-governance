# The charter A/B: the run brief, written before either arm runs

**Serves:** journal TOOL-aMendedFleet-93

What the main loop runs for this unit, and the rule that reads the result. Everything below was
committed with the instrument, `2026-10-06-build-TOOL-aMendedFleet-93-ab.py`, before either arm ran.
A unit pass cannot start a Workflow, so the arms are the main loop's (spec S3).

## The subject

aWindowedPass's round-1 closing range, base `886b089dfd9c4bf98dc2024e21d7d9607f9b5cc0`, head
`e252bafb3fe306e0118c2771ef627b865528e895`: 74 files, 1596 insertions and 279 deletions by
`git diff --shortstat`, read 2026-10-06. The base is the merge base, so the harness's three-dot diff
reads the same range. Its round-1 record,
`memory/builds/aWindowedPass/reviews/2026-10-04-review-TOOL-aWindowedPass-1-2-3-4-5-closing-diff-round1.md`,
states raw 29, confirmed 26, refuted 3 and precision 0.90 under that day's harness. `aggregate` prints
those figures from the record beside both arms and never compares them.

## The arms, in order

Both are `Workflow` calls on `tools/workflows/tier2-review.js`, sequential, never concurrent. The args
are identical except `workerType`. `repo` is the main loop's worktree, absolute and forward-slashed;
this pass ran in `C:/projects/coding-governance/.claude/worktrees/coding-governance-review-1460c9`.

1. **Arm B, first**, so it reads no lens file arm A would write:
   `{"repo": "<worktree>", "base": "886b089dfd9c4bf98dc2024e21d7d9607f9b5cc0", "head": "e252bafb3fe306e0118c2771ef627b865528e895", "round": 1, "reviewDir": "memory/builds/aMendedFleet/build", "workerType": "Plan"}`
2. **Arm A, second**:
   `{"repo": "<worktree>", "base": "886b089dfd9c4bf98dc2024e21d7d9607f9b5cc0", "head": "e252bafb3fe306e0118c2771ef627b865528e895", "round": 1, "reviewDir": "memory/builds/aMendedFleet/build"}`

No `context`, `specs`, `checklist` or `lensNotes` is passed to either arm. The harness warns about
each absence, and it warns identically in both, so the absence is not a difference between arms.

## The key directories

The harness resumes from `<git-common-dir>/review-lenses/<key>/`, and this clone already holds
`diff-review-r1-886b089dfd9c-e252bafb3fe3-152dab81` from the subject's own review. A run whose key
matches reuses every lens file there and spawns no finder. The input-print suffix of today's key is
known only once the probe runs, so the handling is by prefix and by the key each return names:

1. **Before arm B**, rename every directory under `<git-common-dir>/review-lenses/` whose name begins
   `diff-review-r1-886b089dfd9c-e252bafb3fe3-` to the same name plus `.ab-held`. Never delete one.
2. Run arm B, then arm A.
3. **After arm A**, rename `review-lenses/<arm A's returned key>` to that name plus `.ab-arm-a`. Then
   strip `.ab-held` from every held directory. Arm B's judges write no lens file, so its key directory
   may not exist; if it does, rename it to plus `.ab-arm-b`.

## What the main loop commits, in one commit after both arms

- Each arm's return object, as the Workflow tool returned it, one top-level JSON object per file:
  `2026-10-06-build-TOOL-aMendedFleet-93-arm-b.json` and `...-93-arm-a.json`.
- Each arm's synthesis report, renamed to `...-93-arm-b-report.md` and `...-93-arm-a-report.md`,
  with its `**Serves:**` line rewritten to `**Serves:** journal TOOL-aMendedFleet-93` (spec S7).
- The judges rows, `...-93-judges.tsv`, written by
  `python memory/builds/aMendedFleet/build/2026-10-06-build-TOOL-aMendedFleet-93-ab.py tokens --session <main-loop session id> --arm-a <wf dir> --arm-b <wf dir>`.
  Each `<wf dir>` is the `wf_*` directory under `<session>/subagents/workflows/` holding that call's
  agents. `tokens` exits 1 if any agent is unclassified, and it prints the role counts per arm.

Then `python .../2026-10-06-build-TOOL-aMendedFleet-93-ab.py arms` reads the two committed return
objects. A second build pass runs `aggregate`, writes `...-93-reading.md`, and applies S4 or S5.

## The decision rule, verbatim from the spec's section 4

An arm is VALID when its return reads `exit` `complete`, zero reused lenses and batches, zero dead
lenses and skeptic batches, and `tokens` classifies every agent of its run. Over two VALID arms,
`aggregate` prints `DEFAULT-PLAN` when B's precision is at least A's minus 0.05 AND B's median judge
first-turn context is at most 0.85 of A's; otherwise `KEEP-DEFAULT`. Any arm not VALID prints
`INVALID`. The record also states each arm's confirmed counts by severity, its summed judge output
tokens and the subject's recorded round-1 figures, none of which moves the word.

How the instrument reads two phrases of that rule, fixed here before any arm runs:

- "classifies every agent" — no row of the arm has role `unclassified`, the arm has at least one
  judge row, and every judge row carries a first-turn figure. A judge with no `usage` event was not
  measured, and it reads NOT VALID by name rather than as a zero.
- "precision" — the return object's own `precision` field, compared exactly as a decimal fraction.
  The confirmed counts by severity are what the return object carries: `confirmed`, `blockers` and
  `highs`. A finer split lives only in each arm's report.

## Invalid arms

An arm NOT VALID is re-run once, with the key handling above (spec S6). A session limit kills workflow
agents silently and the call still reports completed, which this rule reads as dead lenses or
batches. A second `INVALID` is parked in the run-state file with the reading, the options and the
reason, and the unit closes on the record without S4 or S5.

## Cost

About twelve agents per arm: five finders, up to five skeptic batches, the synthesis and the resume
probe, never more than five at once. UNVERIFIED, scaled from one earlier closing review on this host
whose four finders each opened at about 86,000 tokens of context and wrote 26,000 to 38,000 output
tokens: on the order of a million context tokens and 300,000 output tokens per arm. The measured
figures are what the reading records.
