# TOOL-aGraftedHelix-14 — an engine arm observes hygiene check 27 red the leg, and print its summary on a green run

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aGraftedHelix-14-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aGraftedHelix-14-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-15 |
| [2026-10-04-review-TOOL-aGraftedHelix-10-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-10-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-15 |
| [2026-10-05-review-TOOL-aGraftedHelix-1-closing-diff-round1.md](../reviews/2026-10-05-review-TOOL-aGraftedHelix-1-closing-diff-round1.md) | diff-review | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-15 TOOL-aGraftedHelix-16 TOOL-aGraftedHelix-17 TOOL-aGraftedHelix-18 TOOL-aGraftedHelix-19 TOOL-aGraftedHelix-20 TOOL-aGraftedHelix-21 TOOL-aGraftedHelix-22 TOOL-aGraftedHelix-23 TOOL-aGraftedHelix-24 TOOL-aGraftedHelix-25 TOOL-aGraftedHelix-26 TOOL-aGraftedHelix-27 TOOL-aGraftedHelix-28 |

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

- **S1** — The engine run over a fixture whose branch adds a decision row PARAPHRASING a base row,
  under `NEAR_MATCH_GATE="red:0.125"`, exits non-zero and prints a `check 27:` line as its only
  `check <n>:` line. Over the same fixture's `main` it exits 0 and prints the
  `row-grammar: check 27 graded` summary line. Observed by AC1 and AC2.
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
  states why for the pair, and engages the open ask `TOOL-aDeferredBar-8` there.
- **Observing the arm against check 28.** `TOOL-aGraftedHelix-6` adds check 28 at this unit's build
  step, so an assertion here about check 28 cannot be seen to move until that unit has landed. The
  observation is `TOOL-aGraftedHelix-17`'s (§3 Edges).

### Edges

- **consumes-from** `TOOL-aGraftedHelix-9` — the check 27 dispatch block, the
  `row_grammar.py --check-relations` mode, `RELATION_CHECK`, `NEAR_MATCH_GATE` and the summary
  line; without them there is no block to observe.
- **hands-off** `TOOL-aGraftedHelix-17` — this unit's engine arm, its fixture and its paraphrased
  branch row, for that unit to assert the branch run prints no `check 28:` line and to observe that
  assertion red once check 28 exists (round-1 audit of units 10 to 15, finding 16).

## 4. Design

### The fixture

A copy-install fixture, as unit 9's AC12 builds one: the memory-tree and recall kit directories
copied into a scratch repository, so the recall kit's index builder resolves and the id grammar is
the fixture's own. Its conf declares `NEAR_MATCH_GATE="red:0.125"`. The tree is otherwise clean, the
way the hygiene suite's `_b1` fixture is: a charter, a README, `memory/project/stale-header-waiver.txt`,
and `gen_build_index.py --write` run and committed on both commits, so `main` exits 0 under every
check. A base decision row is committed on `main`.

**The branch row is a paraphrase, never a verbatim restatement.** A branch off `main` adds a row
under a new id whose text says what the base row says in other words. Its `derive_content_key`
differs from the base row's, so unit 6's check 28 does not fire on it, and its near-match score
against the base row still clears the 0.125 floor, so check 27 does. The new id is well-formed
under checks 13 to 16. The pass records the row's text and its measured score in the acceptance
ledger. The clean case is the same tree on `main` alone, where the added set is empty and the
summary line reads a graded count of 0.

Both engine runs are made under `GOV_DEFAULT_BRANCH=main`. Unit 9 derives the relation base from
that variable, falling back to `main`, and reds an armed run with no resolvable base, so an exported
value naming another branch would red the fixture's `main` for an ambient reason.

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
- risks — A minimal tree can red other checks, which would hide check 27's block. The fixture is
  built otherwise clean, AC2 asserts it, and AC1 asserts that 27 is the only check the branch run
  names.
- testing — S3's arm, observed RED with the block's `status=1` deleted.
- migration — None.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When the fixture's copy of `tools/memory-tree/check-memory-hygiene.sh` runs at the root
  of its branch under `GOV_DEFAULT_BRANCH=main`, it exits non-zero and prints a line opening
  `check 27:` naming the new id and the base row's id, and no other line opening `check <n>:`. With
  the block's `status=1` deleted in the fixture's copy, the same run exits 0; that red is observed
  once, then restored.
  Red when: the block swallows the mode's exit, so the engine exits 0 over the near match, or
  another check holds the exit.
- **AC2** — When the same command runs on the fixture's `main` under `GOV_DEFAULT_BRANCH=main`, it
  exits 0 and prints a line opening `row-grammar: check 27 graded`. Run again with
  `GOV_DEFAULT_BRANCH` set to a branch the fixture does not hold, the pinned run still exits 0.
  Red when: the green-run print is missing, the clean tree reds, or an ambient value reaches it.
- **AC3** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no memory-tree carrier left behind, and
  `bash skills/session-kickoff/manifest-check.sh` prints no `MANIFEST check 5 FAILED` line.
  Red when: the kit's bytes moved without its version, or the engine moved without the stamp.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · the engine over an otherwise-clean branch adding a paraphrased decision row under red:0.125, asserting 27 is its only offending check, and over its clean main, both under GOV_DEFAULT_BRANCH=main; stage the dispatch block's status=1 deleted, then its green-run print deleted · the suite's floor rises by its new arm count

The close runs the legs and the suite; a pass runs the two engine commands above as its check.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from the round-1 spec audit's finding 27.
- rev-2 · 2026-10-04 · §3 §4 §5 §6 §7 · S1 · AC1 AC2 · folded the round-1 spec audit of units 10 to
  15 on this unit: 24 (the branch row is a paraphrase whose content key differs from the base row's
  and that clears the 0.125 floor, the tree is otherwise clean on the `_b1` shape, the new id passes
  checks 13 to 16, the run's only offending check is 27, and §5's "AC2 separates" sentence is gone);
  and 28 (both runs pin `GOV_DEFAULT_BRANCH=main`, and AC2 observes an ambient value not reaching
  them). §3 gains the hands-off to the unit promoted from finding 16, which observes the arm against
  check 28.

## 10. Reuse audit

The seams are `TOOL-aGraftedHelix-13`'s, probed once for the pair: the hygiene suite's `c6run`
fixture shape, and unit 9's copy-install fixture for anything that reaches the recall kit. The
recall probe returned `TOOL-cSpliceWarden-6` and `TOOL-aCollapsedScan-10`, and no engine arm for a
delegated check.

Recall terms used: hygiene engine dispatch delegated row_grammar check-rotation status offender green-run summary arm staged break
