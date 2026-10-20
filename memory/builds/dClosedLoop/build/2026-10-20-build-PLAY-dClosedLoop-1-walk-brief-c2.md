# Clause walk brief: run C, walker 2

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
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-c2/`.

Read nothing else: not the working tree's other records, not the session's scratchpad or temp folders, not other
briefs, not git history, and run no instrument from the copy against the copy. The copy differs from the working tree
on purpose: known defects were planted in it before you started, and a sealed key lists them, its SHA-256 fixed before
launch as `505c52433040b18b95d5da9021b5ad0feada756b88290857a1b9eee9c4b837b7`. Look for every defect the same way, since a planted one is scored like any other finding.

## Your slice

- **Builds, each given a verdict:** dFairHearing, dDeclaredLoop, dPlacedRequest, dKeptSession
- **Clauses, each a row of your table:** dFairHearing: `cl-dClosedLoop-0068`, `cl-dClosedLoop-0069`, `cl-dClosedLoop-0070`, `cl-dClosedLoop-0071`, `cl-dClosedLoop-0072`, `cl-dClosedLoop-0073`, `cl-dClosedLoop-0074`, `cl-dClosedLoop-0075`, `cl-dClosedLoop-0076`, `cl-dClosedLoop-0077`, `cl-dClosedLoop-0078`, `cl-dClosedLoop-0079`, `cl-dClosedLoop-0080`, `cl-dClosedLoop-0081`, `cl-dClosedLoop-0082`, `cl-dClosedLoop-0083`, `cl-dClosedLoop-0084`, `cl-dClosedLoop-0085`; dDeclaredLoop: `cl-dClosedLoop-0086`, `cl-dClosedLoop-0087`, `cl-dClosedLoop-0088`, `cl-dClosedLoop-0089`, `cl-dClosedLoop-0090`, `cl-dClosedLoop-0091`, `cl-dClosedLoop-0092`, `cl-dClosedLoop-0094`, `cl-dClosedLoop-0095`, `cl-dClosedLoop-0096`, `cl-dClosedLoop-0097`, `cl-dClosedLoop-0098`, `cl-dClosedLoop-0099`, `cl-dClosedLoop-0100`, `cl-dClosedLoop-0101`, `cl-dClosedLoop-0102`, `cl-dClosedLoop-0103`, `cl-dClosedLoop-0104`, `cl-dClosedLoop-0105`, `cl-dClosedLoop-0106`, `cl-dClosedLoop-0107`, `cl-dClosedLoop-0108`, `cl-dClosedLoop-0109`, `cl-dClosedLoop-0110`, `cl-dClosedLoop-0111`, `cl-dClosedLoop-0112`, `cl-dClosedLoop-0113`, `cl-dClosedLoop-0114`, `cl-dClosedLoop-0115`, `cl-dClosedLoop-0116`, `cl-dClosedLoop-0117`, `cl-dClosedLoop-0118`, `cl-dClosedLoop-0119`; dPlacedRequest: `cl-dClosedLoop-0120`, `cl-dClosedLoop-0121`, `cl-dClosedLoop-0122`, `cl-dClosedLoop-0123`, `cl-dClosedLoop-0124`, `cl-dClosedLoop-0125`, `cl-dClosedLoop-0126`, `cl-dClosedLoop-0127`, `cl-dClosedLoop-0128`, `cl-dClosedLoop-0129`, `cl-dClosedLoop-0130`, `cl-dClosedLoop-0131`, `cl-dClosedLoop-0132`, `cl-dClosedLoop-0133`, `cl-dClosedLoop-0134`, `cl-dClosedLoop-0135`, `cl-dClosedLoop-0136`, `cl-dClosedLoop-0137`, `cl-dClosedLoop-0138`; dKeptSession: `cl-dClosedLoop-0139`, `cl-dClosedLoop-0140`, `cl-dClosedLoop-0141`, `cl-dClosedLoop-0142`, `cl-dClosedLoop-0143`, `cl-dClosedLoop-0144`, `cl-dClosedLoop-0145`, `cl-dClosedLoop-0146`, `cl-dClosedLoop-0147`, `cl-dClosedLoop-0148`, `cl-dClosedLoop-0149`, `cl-dClosedLoop-0150`, `cl-dClosedLoop-0151`, `cl-dClosedLoop-0152`, `cl-dClosedLoop-0153`, `cl-dClosedLoop-0154`, `cl-dClosedLoop-0155`, `cl-dClosedLoop-0156`, `cl-dClosedLoop-0157`, `cl-dClosedLoop-0158`, `cl-dClosedLoop-0159`, `cl-dClosedLoop-0160`, `cl-dClosedLoop-0161`, `cl-dClosedLoop-0162`, `cl-dClosedLoop-0163`, `cl-dClosedLoop-0164`, `cl-dClosedLoop-0165`

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
2. **Findings,** each as `### C2-F<n> — <title>` and then these lines:
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
any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-c2/` only. Your effort is the owner's medium.
