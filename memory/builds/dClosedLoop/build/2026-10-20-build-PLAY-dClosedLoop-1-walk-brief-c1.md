# Clause walk brief: run C, walker 1

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
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-c1/`.

Read nothing else: not the working tree's other records, not the session's scratchpad or temp folders, not other
briefs, not git history, and run no instrument from the copy against the copy. The copy differs from the working tree
on purpose: known defects were planted in it before you started, and a sealed key lists them, its SHA-256 fixed before
launch as `505c52433040b18b95d5da9021b5ad0feada756b88290857a1b9eee9c4b837b7`. Look for every defect the same way, since a planted one is scored like any other finding.

## Your slice

- **Builds, each given a verdict:** dTrueNorth, dGroundRules, dSafePassage, dOrderedCharter
- **Clauses, each a row of your table:** dTrueNorth: `cl-dClosedLoop-0001`, `cl-dClosedLoop-0002`, `cl-dClosedLoop-0003`, `cl-dClosedLoop-0004`, `cl-dClosedLoop-0005`, `cl-dClosedLoop-0006`; dGroundRules: `cl-dClosedLoop-0007`, `cl-dClosedLoop-0008`, `cl-dClosedLoop-0009`, `cl-dClosedLoop-0010`, `cl-dClosedLoop-0011`, `cl-dClosedLoop-0012`, `cl-dClosedLoop-0013`, `cl-dClosedLoop-0014`, `cl-dClosedLoop-0015`, `cl-dClosedLoop-0016`, `cl-dClosedLoop-0017`; dSafePassage: `cl-dClosedLoop-0018`, `cl-dClosedLoop-0019`, `cl-dClosedLoop-0020`, `cl-dClosedLoop-0021`, `cl-dClosedLoop-0022`, `cl-dClosedLoop-0023`, `cl-dClosedLoop-0024`, `cl-dClosedLoop-0025`, `cl-dClosedLoop-0026`, `cl-dClosedLoop-0027`, `cl-dClosedLoop-0028`, `cl-dClosedLoop-0029`, `cl-dClosedLoop-0030`; dOrderedCharter: `cl-dClosedLoop-0031`, `cl-dClosedLoop-0032`, `cl-dClosedLoop-0033`, `cl-dClosedLoop-0034`, `cl-dClosedLoop-0035`, `cl-dClosedLoop-0036`, `cl-dClosedLoop-0037`, `cl-dClosedLoop-0038`, `cl-dClosedLoop-0039`, `cl-dClosedLoop-0040`, `cl-dClosedLoop-0041`, `cl-dClosedLoop-0042`, `cl-dClosedLoop-0043`, `cl-dClosedLoop-0044`, `cl-dClosedLoop-0045`, `cl-dClosedLoop-0046`, `cl-dClosedLoop-0047`, `cl-dClosedLoop-0048`, `cl-dClosedLoop-0049`, `cl-dClosedLoop-0050`, `cl-dClosedLoop-0051`, `cl-dClosedLoop-0052`, `cl-dClosedLoop-0053`, `cl-dClosedLoop-0054`, `cl-dClosedLoop-0055`, `cl-dClosedLoop-0056`, `cl-dClosedLoop-0057`, `cl-dClosedLoop-0058`, `cl-dClosedLoop-0059`, `cl-dClosedLoop-0060`, `cl-dClosedLoop-0061`, `cl-dClosedLoop-0062`, `cl-dClosedLoop-0063`, `cl-dClosedLoop-0064`, `cl-dClosedLoop-0065`, `cl-dClosedLoop-0066`, `cl-dClosedLoop-0067`

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
2. **Findings,** each as `### C1-F<n> — <title>` and then these lines:
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
any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-c1/` only. Your effort is the owner's medium.
