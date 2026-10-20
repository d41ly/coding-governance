# Second-look brief: run A

**Serves:** research PLAY-dClosedLoop-1

**Your task is to judge each finding below: confirm it or refute it.** This brief is your instructions, not the
subject of your review: do not review it, the audit's seal or its instruments. A defect you see in them goes in one
line at the end of your return, and nowhere else.

Each finding below was returned by a walker reading the sealed copy of the design at
`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Grade a confirmed one by the copy's round record's
`[rubric]` (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`).

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index, and **Stage 0's leads,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md`,
   which some findings cite.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/recheck-a/`.

Read nothing else: not the working tree's other records, not the walkers' returns or the reports, not the session's
scratchpad or temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it
alone, since the working tree may differ from it.

## Findings to judge

### A1-F7 — `design.ready` and `test.exit` wait on the recommend item, not the reason item, so the frontier can pass a review the reason calls for
- **Address:** flow-steps [design] `design.ready`; flow-steps [test] `test.exit`
- **Class:** K1, c3
- **Severity:** high
- **Scenario:** S1
- **Evidence:**
  - `design.ready` needs "`design.recommend`, and the spec audit where it ran". `test.exit` needs "`test.recommend`, and the gate review where it ran".
  - Under the default `review.recommendation.source: scored-signals-and-reasoning`, `design.reason` and `test.reason` route "a review → the spec audit" or "the gate review".
  - [rules] says `next` returns "the unwitnessed items whose needs are witnessed" and that independent items run in parallel. P24 says "An item's witness is resolved before any item that depends on it starts".
- **Consequence:** Once `design.recommend` is witnessed, `design.ready` and `design.reason` are both on the frontier. `design.ready` and `design.exit` can be recorded before the reason asks for the audit, and the route to the audit is then unreachable. Under `review.recommendation: binding`, an owed review is skipped, so a guard loosens. Test has the same defect.
- **Fix:** Set the Needs to "`design.reason` where the source runs it, else `design.recommend`; and the spec audit where it ran", and the same for `test.exit`. Add a planted reason that answers "review" and must place the audit.

### A1-F9 — P14's "review lenses read the active practices' reach" has no enforcing clause
- **Address:** architecture-v2 [enforcement] `P14`; architecture-v2 [principles] P14
- **Class:** K5
- **Severity:** medium
- **Scenario:** S1
- **Evidence:**
  - P14 says "stage contracts, role handoffs and review lenses read the active practices' reach for their stage".
  - Its row names `cl-dClosedLoop-0031` (the catalogue) and `cl-dClosedLoop-0051` ("reach per step rendered as step-scoped units handed in work orders").
  - Probe: `grep -iE 'lens' clauses.txt | grep -iE 'practice|reach'` printed nothing.
- **Consequence:** S1's spec audit and closing review run lenses that read no practice reach, so a practice does not redefine review as P14 says. No dFairHearing or dCalibratedLens spec has a clause to carry this.
- **Fix:** Add a clause, in dFairHearing's lens catalogue or dCalibratedLens's stage lenses, by which each lens loads the active practices' reach for its stage, seen red on a planted practice whose reach a lens omits. Add it to P14's row.

### A2-F8 — Two nodes pushing one build branch: the race is undeclared under the default shared worktree
- **Address:** layer-runtime [isolate], and architecture-v2 [chain] dWellOiledMachine `cl-dClosedLoop-0318` and dPlacedRequest `cl-dClosedLoop-0133`
- **Class:** K10, c2
- **Severity:** high
- **Scenario:** S2
- **Evidence:**
  - layer-runtime:716-719: "shared: the build's one worktree … The commit queue then commits them one at a time". That queue is local to one node.
  - The `build.worktree` default is `shared`, and `build.push` is `every-pass`.
  - 0318 has each role agent "pushing the build's branch".
  - 0133 fences each push on the pusher's own lease tip only.
  - No record names the route when an atomic push is refused because the branch moved.
- **Consequence:** Node x holds only a unit lease, yet pushes X's build branch beside node d's pushes. The second push is refused non-fast-forward, and the refusal cannot be told from a fence refusal. The pass is either dropped or retried with no budget rule, and under `shared` node x has no worktree at all.
- **Fix:** A unit leased on another node always gets a unit branch (per-unit). The build branch is written only by the build-lease holder's merge, as [isolate]'s "Integration before release" says. A refused push routes by class (fence lost vs branch moved, rebase and retry as contention). Seen red on two nodes pushing one branch.

### A3-F14 — `entry.claim`'s own-key idempotency routes a replayed claim into a terminal build
- **Address:** flow-steps [entry] `entry.claim`
- **Class:** K2
- **Severity:** medium
- **Scenario:** S5
- **Evidence:** `entry.claim`: "a retry that finds its own key counts as claimed" → "claimed → Plan, or Design on `patch` or `repeat`". layer-memory: "A slug's claim ref is never pruned". `[transitions]` has no row leaving `withdrawn`.
- **Consequence:** A replayed intake after the withdrawal routes into a withdrawn build. The engine refuses the transition, and the request is neither placed nor answered.
- **Fix:** `entry.claim` reads the slug's last transition. If it is terminal, it mints a fresh slug or returns the request naming the terminal state.

### A4-F7 — The floor step is "the step kind's first step", but its progress field only arrives in the schema-4 step
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0028`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S4
- **Evidence:**
  - cl-0028: "the interpreter floor raised to Python 3.15 as the step kind's first step".
  - cl-0019: "the receipt advancing per completed step".
  - cl-0020: "the receipt's schema 4 gaining `steps` … shipped as an upgrade step whose down restores schema 3".
  - No clause orders the two steps or says where a step completed against a schema-3 receipt records its progress.
- **Consequence:** An adopter on schema 3 runs the floor step first. Its completion has no `steps` field to land in, so a kill after it re-runs it or leaves the receipt unreadable to schema-3 readers.
- **Fix:** Declare the schema-4 `steps` step as step 0, with its witness the schema field itself. Order the floor step after it, and plant a kill between them.

### A5-F5 — A build parked on the owner's silence loses its lease, and nothing takes it back
- **Address:** architecture-v2 [policies] `run.on-owner-silence` `cl-dClosedLoop-0326`; flow-steps [breakpoint]
- **Class:** K10
- **Severity:** medium
- **Scenario:** S6
- **Evidence:**
  - v2 `[policies]` `run.on-owner-silence` and `cl-dClosedLoop-0326`: parking releases the build's lease and leaves the item open.
  - `cl-dClosedLoop-0134`: "each release a hand-over, which any node may take".
  - `[lifecycle]`: "Resume enters its `next`". `plan.lease`'s instance is already witnessed, so `next` never re-runs it.
  - Design's contract takes "a planned, leased build".
- **Consequence:** After the 24-hour silence at Plan's ratification, another node may take over a build that is waiting for the owner. When the owner's late go arrives, the build enters Design holding no lease.
- **Fix:** Release the lease of a build parked for the owner as terminal-for-takeover, or keep it renewed as a paused build's is. Declare a lease re-take item on the owner's disposition of a parked build.

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/recheck-a/` only. Your effort is the one the owner's
role definition sets.
