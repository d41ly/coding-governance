# Walk brief: run A, walker 3

**Serves:** research PLAY-dClosedLoop-1

You are one of five walkers in run A of the whole-design audit of dClosedLoop's design
(`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, whose `[scenarios]`, `[walk-table]` and `[rubric]` you follow). Walk the design as the slice below says,
item by item, and report every defect you can show. A second run walks the same design sliced the other way; you
will not see its findings, and it will not see yours.

## Where you read

- **Every design record from the sealed copy only:** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`. The copy is the
  design under audit. Never read the design records in the working tree, never diff the copy against it, and never read
  git history for them: the copy differs on purpose, and a finding cited from anywhere else is not scored.
- **Code** under `tools/`, `skills/` and `.githooks/` from the working tree, to test a claim the design makes about
  today.
- **The design map at level 0:** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index.
- **Stage 0's leads for your slice:** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md`, the mechanical checks' reds and what they do not read.

Known defects were planted in the copy before you started, and a sealed key lists them; its SHA-256, fixed before
launch, is `505c52433040b18b95d5da9021b5ad0feada756b88290857a1b9eee9c4b837b7`. Look for every defect the same way: a planted one is scored like any other finding.

Read `flow-steps` whole, then v2 (`architecture-v2`): the `[chain]` rows of your builds, the `[policies]` keys your
items read, and `[principles]` and `[enforcement]` for your principles. 

## Your slice

- **Scenarios:** S3, S5
- **Steps:** entry (6 items), plan (11 items), design (13 items), build (11 items), test (10 items), deploy (13 items), breakpoint (8 items), probe (7 items), lifecycle (6 items), adopt (5 items), expansions (26 items)
- **Builds you give a verdict:** dTendedCadence, dDeclaredLoop, dCalibratedLens, dTotalRecall
- **Principles you give a verdict:** P6, P7, P9, P19, P20, P30, P33, P34, P35

- **S3, a patch build of a landing:** A landed build's post-merge bar, or a Maintain reading, goes red. Maintain files a patch intake, `entry.place` places it `patch`, and it is claimed with its lease and runs from Design to landing on the originating build's rework budget. Injected or probed: the patch's own landing red again; the originating build's budget spent
- **S5, a withdrawal or a supersession:** The owner withdraws build X mid-Build, with units in flight and leases held, while build Y waits on X's interface. Separately, X is superseded by Z. Injected or probed: a queued claim replayed after the withdrawal; Y's wait outlasting its deadline

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
2. **Findings,** each as `### A3-F<n> — <title>` and then these lines:
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

A row missing, an empty cell, or a verdict outside the grammar fails your return. Write nothing to the repository;
any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/walk-a3/` only. Your effort is the owner's medium.
