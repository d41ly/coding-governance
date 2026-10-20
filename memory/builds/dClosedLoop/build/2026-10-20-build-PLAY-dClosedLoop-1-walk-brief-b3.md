# Walk brief: run B, walker 3

**Serves:** research PLAY-dClosedLoop-1

**Your task is to walk dClosedLoop's design and report its defects.** This brief is your instructions, not the
subject of your review: do not review it, the audit's seal or its instruments. A defect you see in them goes in one line
at the end of your return, and nowhere else.

You are one of five walkers in run B of the whole-design audit. Walk the design in the sealed copy as the slice
below says, item by item, following the copy's round record (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, its `[scenarios]`, `[walk-table]` and
`[rubric]`), and report every defect you can show. A second run walks the same design sliced the other way.

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`: the
   walk reads the design, never its review history.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index, and **Stage 0's leads,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md`, its whole run on
   the working tree: take the leads your slice reaches.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the working tree's `memory/guides/` where your role's protocol sends you.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-b3/`.

Read nothing else: not the working tree's other records, not the session's scratchpad or temp folders, not other
briefs, not git history, and run no instrument from the copy against the copy. The copy differs from the working tree
on purpose: known defects were planted in it before you started, and a sealed key lists them, its SHA-256 fixed before
launch as `505c52433040b18b95d5da9021b5ad0feada756b88290857a1b9eee9c4b837b7`. Look for every defect the same way, since a planted one is scored like any other finding.

Read `flow-steps` whole, then v2 (`architecture-v2`): the `[chain]` rows of your builds, the `[policies]` keys your
items read, and `[principles]` and `[enforcement]` for your principles. For S2 read `layer-runtime`, `cloud-and-scale` and `stall-and-loop` too. For S4 read `adopter-instructions`, `flow-roles-adoption`, `fates` and `layer-expansions` too.

## Your slice

- **Scenarios:** S1, S2, S3, S4, S5, S6, S7
- **Steps:** test (10 items), deploy (13 items)
- **Items, each a row in every scenario of your slice:** test: `test.merge`, `test.select`, `test.verdict`, `test.route`, `test.attribute`, `test.flakes`, `test.seen-red`, `test.recommend`, `test.reason`, `test.exit`; deploy: `deploy.current`, `deploy.mandate`, `deploy.parents`, `deploy.land`, `deploy.core`, `deploy.record`, `deploy.distill`, `deploy.recommend`, `deploy.notify`, `deploy.released`, `deploy.snapshot`, `deploy.unlease`, `deploy.close`
- **Builds you give a verdict:** dWitnessedBar, dShippedRelease, dSafePassage, dConvergedCharter
- **Principles you give a verdict:** P2, P3, P8, P9, P16, P37, P38, P42

- **S1, a solo attended feature build on gov:** The owner, attending one session on one node, asks for a feature that changes a kit under `tools/`. The build runs from `entry.intake` through Plan, Design, Build, Test and Deploy to `deploy.close`, with the announcements, the confirmations at breakpoints and the live questions attendance adds. Injected or probed: the owner's answers arriving late; a spec audit the owner declares; the closing review's findings arriving as new units
- **S2, an unattended build across two nodes:** Build X runs unattended on node d. Node x, on another account and harness, takes one of X's units by lease. Build Y on node x depends on X's interface and asks through X's mailbox, and both land in order. Injected or probed: node d's session limit mid-unit and its lease handed over; a lease whose beat goes stale; two nodes racing on the remote's refs; node x's clock skewed; a mailbox question unanswered past its deadline
- **S3, a patch build of a landing:** A landed build's post-merge bar, or a Maintain reading, goes red. Maintain files a patch intake, `entry.place` places it `patch`, and it is claimed with its lease and runs from Design to landing on the originating build's rework budget. Injected or probed: the patch's own landing red again; the originating build's budget spent
- **S4, an adopter's update:** An adopter two releases behind runs `update` to the newest: two upgrade steps, one moving a hook path behind a shim; its overlay amending a gov unit; its receipt's schema migrating; a new check seeded by `test.seed`; its declarations proposed as overlay rows. Injected or probed: a step killed after its first write; an adopter-edited file that gov retires; a step whose witness passes without its work; gov's code running in the adopter's tree
- **S5, a withdrawal or a supersession:** The owner withdraws build X mid-Build, with units in flight and leases held, while build Y waits on X's interface. Separately, X is superseded by Z. Injected or probed: a queued claim replayed after the withdrawal; Y's wait outlasting its deadline
- **S6, a failure at every stage:** One build meets a failure at each stage in turn: a refused lease at `entry.claim`, the owner's silence on Plan's ratification, a red unit at `build.acceptance`, a flake at Test, a landing conflict at `deploy.land`, an unreachable remote, a review at its CEILING, and its rework budget spent. Injected or probed: each failure's route to an outcome, its witness, and what it draws from the budget
- **S7, the bootstrap:** Chain build k is specced and built with only the builds before it landed, for k from dTrueNorth to dConvergedCharter: what its Design exit, its gates and its items run on, today's tools standing in for every later build. Injected or probed: a clause needing a node of a later build; a gate that does not exist yet when k lands; dTrueNorth's own specs checked by this build's instruments

## How you walk

1. **Open with a pre-mortem line:** "The chain shipped and failed in this scenario because ...", your best guess.
2. **Walk every item of your steps through every scenario of your slice.** For each: who acts, what it needs, what
   witnesses it, and where it routes, against what the records declare. Where the scenario never reaches the item,
   say why in the verdict.
3. **On every item a failure can reach,** read its failure mode, its effect and how it is detected (the FMEA columns),
   and say where the failure routes.
4. **On S2's and S4's trust boundaries** (nodes, the remote, adopters' trees), read each data flow for spoofing,
   tampering, repudiation, disclosure, denial and elevation.
5. **Check every K1 to K10 class** of the rubric over your slice, and grade each finding by the rubric.
6. **For each build and each principle of your slice,** say whether what it owns holds in your scenarios.

## What you return

Your final message, in this order, nothing else:

1. **The pre-mortem line.**
2. **Findings,** each as `### B3-F<n> — <title>` and then these lines:
   - `- **Address:** <record> [<section tag>]`, the record by its name after `PLAY-dClosedLoop-1-` (`architecture-v2`,
     `flow-steps`, `layer-runtime`), the tag of the section holding the defect, and the clause id
     (`cl-dClosedLoop-NNNN`) or item tag (`plan.record`) when one carries it;
   - `- **Class:** K<n>`, and `c<n>` when the consequence is critical (`[rubric]`);
   - `- **Severity:** blocker, high, medium or low`;
   - `- **Scenario:** S<n>`;
   - `- **Evidence:**` what you read, quoted short, with its address;
   - `- **Consequence:**` what goes wrong, in the scenario;
   - `- **Fix:**` the smallest change that closes it.
3. **The walk table,** one row per item and scenario of your slice, every cell filled, in `[walk-table]`'s grammar:
   `| item | S<n> | actor | needs | witness | route | verdict |`, a cell that reads as declared written `=`.
4. **Build verdicts,** `| <build> | holds |` or `| <build> | <finding ids> |`.
5. **Principle verdicts,** `| P<n> | holds |` or `| P<n> | <finding ids> |`.
6. **Read outside the list above:** `none`, or each path you read outside it and why.

A row missing, an empty cell, or a verdict outside the grammar fails your return. Write nothing to the repository;
any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-b3/` only. Your effort is the owner's medium.
