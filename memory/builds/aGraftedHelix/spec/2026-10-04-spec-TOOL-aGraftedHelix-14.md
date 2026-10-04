# TOOL-aGraftedHelix-14 — an engine arm observes hygiene check 27 red the leg, and print its summary on a green run

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-15 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-9` wires check 27 into `tools/memory-tree/check-memory-hygiene.sh` as a
dispatch block that must set `status=1`, key offenders under 27 and print the mode's summary on a
green run. Its only observation of that block is `grep -n 'check-relations'`, which a comment or a
dead block satisfies. A block that swallows the mode's exit leaves the `memory hygiene` leg green
over an unsatisfied near match, and unit 9's rollout, "lands armed red, so its own close bar grades
every row", would never happen. This unit observes the block through the engine. It closes finding
27 (HIGH) of the round-1 spec audit.

## 2. Scope (IN)

- **S1** — The engine run over a fixture whose branch adds a decision row restating a base row,
  under `NEAR_MATCH_GATE="red:0.125"`, exits non-zero and prints a `check 27:` line. Over the same
  fixture's `main` it exits 0 and prints the `row-grammar: check 27 graded` summary line. Observed
  by AC1 and AC2.
- **S2** — Where AC1 or AC2 reds over the block unit 9 built, this unit repairs the block, which
  calls `row_grammar.py --check-relations` and keys its offenders under `RELATION_CHECK`. The
  kickoff manifest's `last-audit` is then re-stamped, because the engine is on its watch list.
  Observed by AC1 and AC2.
- **S3** — `tools/memory-tree/check-memory-hygiene.test.sh` gains the two cases as an engine arm.
  NOT OBSERVED by a criterion here: the suite is the close's to run, and its red on a staged break
  is observed there (§7).
- **S4** — The memory-tree kit version moves once after this unit's last move if its shipped bytes
  moved, in every carrier `tools/check-kit-versions.sh` pairs. Observed by AC3.

## 3. Non-goals (OUT)

- **The predicate and the floor.** Both are unit 9's, measured there.
- **Extending `check-arms.py` to count a delegated dispatch block.** `TOOL-aGraftedHelix-13`
  states why for the pair.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-9` — the check 27 dispatch block, the
  `row_grammar.py --check-relations` mode, `RELATION_CHECK`, `NEAR_MATCH_GATE` and the summary
  line; without them there is no block to observe.

## 4. Design

### The fixture

A copy-install fixture, as unit 9's AC12 builds one: the memory-tree and recall kit directories
copied into a scratch repository, so the recall kit's index builder resolves and the id grammar is
the fixture's own. Its conf declares `NEAR_MATCH_GATE="red:0.125"`. A base decision row is
committed on `main`, and a branch off it adds a row restating that one under a new id. The clean
case is the same tree on `main` alone, where the added set is empty and the summary line reads a
graded count of 0.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/check-memory-hygiene.sh`, only where S2 repairs the block
- `memory/guides/SESSION-KICKOFF.md`, only where S2 moves the engine
- every other carrier of the memory-tree version marker, which `tools/check-kit-versions.sh`
  enumerates

## 5. Production-readiness checklist

- security — N/A: a test arm, and a repair of a block unit 9 specifies.
- perf / scale — Two engine runs over a minimal tree; the index build is unit 9's 0.7 s figure or
  less.
- error / empty / loading states — The clean case is the green-run observation, at a graded count
  of 0.
- observability — The arm's failure names which half went wrong.
- risks — Other checks may red over a minimal tree; AC2's clean run is what separates check 27's
  red from theirs.
- testing — S3's arm, observed RED with the block's `status=1` deleted.
- migration — None.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When the fixture's copy of `tools/memory-tree/check-memory-hygiene.sh` runs at the root
  of its branch, it exits non-zero and prints a line opening `check 27:` naming the new id and the
  base row's id. With the block's `status=1` deleted in the working tree, the same run exits 0; that
  red is observed once, then restored.
  Red when: the block swallows the mode's exit, so the engine exits 0 over the near match.
- **AC2** — When the same command runs on the fixture's `main`, it exits 0 and prints a line
  opening `row-grammar: check 27 graded`.
  Red when: the green-run print is missing, or the clean tree reds.
- **AC3** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no memory-tree carrier left behind, and
  `bash skills/session-kickoff/manifest-check.sh` prints no `MANIFEST check 5 FAILED` line.
  Red when: the kit's bytes moved without its version, or the engine moved without the stamp.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · the engine over a branch adding a restated decision row under red:0.125, and over its clean main; stage the dispatch block's status=1 deleted, then its green-run print deleted · the suite's floor rises by its new arm count

The close runs the legs and the suite; a pass runs the two engine commands above as its check.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from the round-1 spec audit's finding 27.

## 10. Reuse audit

The seams are `TOOL-aGraftedHelix-13`'s, probed once for the pair: the hygiene suite's `c6run`
fixture shape, and unit 9's copy-install fixture for anything that reaches the recall kit. The
recall probe returned `TOOL-cSpliceWarden-6` and `TOOL-aCollapsedScan-10`, and no engine arm for a
delegated check.

Recall terms used: hygiene engine dispatch delegated row_grammar check-rotation status offender green-run summary arm staged break
