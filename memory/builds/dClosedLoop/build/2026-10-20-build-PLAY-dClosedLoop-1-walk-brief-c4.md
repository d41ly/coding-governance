# Clause walk brief: run C, walker 4

**Serves:** research PLAY-dClosedLoop-1

**Your task is to read dClosedLoop's chain clauses for your builds and report what each one omits or contradicts.**
This brief is your instructions, not the subject of your review: do not review it, the audit's seal or its
instruments. A defect you see in them goes in one line at the end of your return, and nowhere else.

You are one of five walkers in run C of the whole-design audit. Two runs walked the design's items through scenarios;
this run reads its clauses, the `[chain]` rows of v2 (`architecture-v2`) in the sealed copy, each against the records
that settle what it builds. Grade by the copy's round record's `[rubric]` (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`).

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index, and **Stage 0's leads,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md`.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-c4/`.

Read nothing else: not the working tree's other records, not the session's scratchpad or temp folders, not other
briefs, not git history, and run no instrument from the copy against the copy. The copy differs from the working tree
on purpose: known defects were planted in it before you started, and a sealed key lists them, its SHA-256 fixed before
launch as `505c52433040b18b95d5da9021b5ad0feada756b88290857a1b9eee9c4b837b7`. Look for every defect the same way, since a planted one is scored like any other finding.

## Your slice

- **Builds, each given a verdict:** dWellOiledMachine, dWitnessedBar
- **Clauses, each a row of your table:** dWellOiledMachine: `cl-dClosedLoop-0279`, `cl-dClosedLoop-0280`, `cl-dClosedLoop-0281`, `cl-dClosedLoop-0282`, `cl-dClosedLoop-0283`, `cl-dClosedLoop-0284`, `cl-dClosedLoop-0285`, `cl-dClosedLoop-0286`, `cl-dClosedLoop-0287`, `cl-dClosedLoop-0288`, `cl-dClosedLoop-0289`, `cl-dClosedLoop-0290`, `cl-dClosedLoop-0291`, `cl-dClosedLoop-0292`, `cl-dClosedLoop-0293`, `cl-dClosedLoop-0294`, `cl-dClosedLoop-0295`, `cl-dClosedLoop-0296`, `cl-dClosedLoop-0297`, `cl-dClosedLoop-0298`, `cl-dClosedLoop-0299`, `cl-dClosedLoop-0300`, `cl-dClosedLoop-0301`, `cl-dClosedLoop-0302`, `cl-dClosedLoop-0303`, `cl-dClosedLoop-0304`, `cl-dClosedLoop-0305`, `cl-dClosedLoop-0306`, `cl-dClosedLoop-0307`, `cl-dClosedLoop-0308`, `cl-dClosedLoop-0309`, `cl-dClosedLoop-0310`, `cl-dClosedLoop-0311`, `cl-dClosedLoop-0312`, `cl-dClosedLoop-0313`, `cl-dClosedLoop-0314`, `cl-dClosedLoop-0315`, `cl-dClosedLoop-0316`, `cl-dClosedLoop-0317`, `cl-dClosedLoop-0318`, `cl-dClosedLoop-0319`, `cl-dClosedLoop-0320`, `cl-dClosedLoop-0321`, `cl-dClosedLoop-0322`, `cl-dClosedLoop-0323`, `cl-dClosedLoop-0324`, `cl-dClosedLoop-0325`, `cl-dClosedLoop-0326`, `cl-dClosedLoop-0327`, `cl-dClosedLoop-0328`, `cl-dClosedLoop-0329`, `cl-dClosedLoop-0330`, `cl-dClosedLoop-0331`, `cl-dClosedLoop-0332`, `cl-dClosedLoop-0333`, `cl-dClosedLoop-0334`, `cl-dClosedLoop-0335`, `cl-dClosedLoop-0336`, `cl-dClosedLoop-0337`, `cl-dClosedLoop-0338`; dWitnessedBar: `cl-dClosedLoop-0339`, `cl-dClosedLoop-0340`, `cl-dClosedLoop-0341`, `cl-dClosedLoop-0342`, `cl-dClosedLoop-0343`, `cl-dClosedLoop-0344`, `cl-dClosedLoop-0345`, `cl-dClosedLoop-0346`, `cl-dClosedLoop-0347`, `cl-dClosedLoop-0348`, `cl-dClosedLoop-0349`, `cl-dClosedLoop-0350`, `cl-dClosedLoop-0351`, `cl-dClosedLoop-0352`, `cl-dClosedLoop-0353`, `cl-dClosedLoop-0354`, `cl-dClosedLoop-0355`, `cl-dClosedLoop-0356`, `cl-dClosedLoop-0357`, `cl-dClosedLoop-0358`, `cl-dClosedLoop-0359`, `cl-dClosedLoop-0360`, `cl-dClosedLoop-0361`, `cl-dClosedLoop-0362`, `cl-dClosedLoop-0363`, `cl-dClosedLoop-0364`, `cl-dClosedLoop-0365`, `cl-dClosedLoop-0366`, `cl-dClosedLoop-0367`, `cl-dClosedLoop-0368`

## How you read

1. **Open with a pre-mortem line:** "The chain shipped and failed because one of these clauses ...", your best guess.
2. **For each build,** read its `[chain]` row whole: its parents, its planned units and the gaps it owns.
3. **For each clause,** find the records that settle what it builds: the gaps its row owns (`gap-register`), the
   sections of the layer, flow and expansion records that define its items, kinds, keys and routes, and the records
   it cites. Then check that it carries every rule they settle for it, contradicts none of them and no other clause,
   and names only what its build or an ancestor owns, or a stand-in. A rule settled elsewhere that no clause of the
   build carries is a finding at the clause that should carry it.
4. **Read each build's clauses against the principles it enforces** (v2 `[principles]` and `[enforcement]`) and
   every K1 to K10 class of the rubric, and grade each finding by the rubric.

## What you return

Your final message, in this order, nothing else:

1. **The pre-mortem line.**
2. **Findings,** each as `### C4-F<n> — <title>` and then these lines:
   - `- **Address:** architecture-v2 [chain] <clause id>`, or another record and its section when the defect lies
     there;
   - `- **Class:** K<n>`, and `c<n>` when the consequence is critical (`[rubric]`);
   - `- **Severity:** blocker, high, medium or low`;
   - `- **Evidence:**` the settling record's words and the clause's, quoted short, each with its address;
   - `- **Consequence:**` what goes wrong when the build is built from the clause as written;
   - `- **Fix:**` the smallest change that closes it.
3. **The clause table,** one row per clause of your slice: `| clause | build | read against | verdict |`, the clause
   id, its build, the records and sections you read it against (never empty), and `holds` or its findings' ids.
4. **Build verdicts,** `| <build> | holds |` or `| <build> | <finding ids> |`.
5. **Read outside the list above:** `none`, or each path you read outside it and why.

A row missing, an empty cell, or a verdict outside the grammar fails your return. Write nothing to the repository;
any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-c4/` only. Your effort is the owner's medium.
