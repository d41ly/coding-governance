# TOOL-aGraftedHelix-13 — an engine arm observes hygiene check 28 red the leg, and print its summary on a green run

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-6 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |
| [2026-10-04-review-TOOL-aGraftedHelix-10-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-10-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-6` wires check 28 into `tools/memory-tree/check-memory-hygiene.sh` as a
dispatch block that must set `status=1`, key offenders under 28 and print the mode's summary on a
green run. Its only observation of that block is `grep -n 'check-content'`, which a comment or a
dead block satisfies, and its other criteria run `row_grammar.py` directly, never the engine. A
block that swallows the mode's exit leaves the `memory hygiene` leg green over a duplicated record.
This unit observes the block through the engine. It closes finding 20 (HIGH) of the round-1 spec
audit.

## 2. Scope (IN)

- **S1** — The engine run over a fixture holding a duplicated record exits non-zero and prints a
  `check 28:` line. Over the same fixture without the duplicate it exits 0 and prints the
  `row-grammar: check 28 graded` summary line, the green-run print check 24's block never had.
  Observed by AC1 and AC2.
- **S2** — Where AC1 or AC2 reds over the block unit 6 built, this unit repairs the block, which
  calls `row_grammar.py --check-content` and keys its offenders under `CONTENT_CHECK`. The kickoff
  manifest's `last-audit` is then re-stamped, because the engine is on its watch list. Observed by
  AC1 and AC2.
- **S3** — `tools/memory-tree/check-memory-hygiene.test.sh` gains the two cases as an engine arm,
  built on the otherwise-clean `_b1` fixture rather than on `c6run`, whose caps tree is red by
  design. The arm asserts that the clean run exits 0 and that the branch run's only offending check
  is 28. NOT OBSERVED by a criterion here: the suite is the close's to run, and its red on a staged
  break is observed there (§7).
- **S4** — The memory-tree kit version moves once after this unit's last move if its shipped bytes
  moved, in every carrier `tools/check-kit-versions.sh` pairs. Observed by AC3.
- **S5** — A gotcha record of the presence-probe class joins `memory/gotchas/`: a `grep -n` for a
  word over a source file is a presence probe, not an observation, because a comment or a dead block
  satisfies it. It names `tools/memory-tree/check-memory-hygiene.sh` as a backticked anchor, so the
  checklist selects it for a diff of the engine, and `gotchas.py --write` re-renders the catalogue
  index. It is the documented check that stands in for the `check-arms.py` class gate §3 declines.
  Observed by AC4.

## 3. Non-goals (OUT)

- **The check's predicate.** The key, the added-set rule and the summary line are unit 6's.
- **Extending `check-arms.py` to count a delegated dispatch block.** The audit offered it as a
  class gate. It changes another leg's predicate and reds check 24's block, which has had no engine
  arm since it landed. That is a third check outside this build; the two engine arms of this unit
  and `TOOL-aGraftedHelix-14` close the two instances this build adds. The open ask
  `TOOL-aDeferredBar-8` already asks `check-arms.py` for a second discovery signature for refusals
  the `fail()` signature misses. The delegated dispatch block is such a signature: it sets
  `status=1` with no `fail <n>` call, which checks 24, 27 and 28 all do. A gate is a mechanism of its
  own, so a fold cannot add it to this spec, and the mandate files no ask; the decline is recorded
  under the build README's "Parked decisions" for the owner, and S5's record is the documented check
  meanwhile.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-6` — the check 28 dispatch block, the
  `row_grammar.py --check-content` mode, `CONTENT_CHECK` and its summary line; without them there is
  no block to observe.

## 4. Design

### The fixture

A scratch git repository built the way the suite's `_b1` fixture is: a conf naming its memory
root, a charter, a README, `memory/project/stale-header-waiver.txt`, and `gen_build_index.py --write`
run and committed. One gotcha is committed on `main`, with the gotcha index re-rendered by
`gotchas.py --write` and whatever gate declaration `gotchas.py --check` demands, so `main` is clean
under every check. A branch off `main` commits a second gotcha whose body is the first's, and
re-renders the index the same way, so the branch's only offence is the duplicate. Check 28 grades
keys held by a record added since the mainline merge-base, so the copy is graded and the original is
not, and the finding names both stems. The clean case is the same tree on `main` alone.

Both engine runs execute the worktree's engine by its path with the working directory at the
fixture root, as `c6run` does, and under `GOV_DEFAULT_BRANCH=main`, so the merge-base derivation
reads the fixture's own `main` whatever the shell exports. The staged break is made in a scratch
copy of the whole kit directory, `tools/memory-tree/*.sh` and `*.py` copied the way the suite's
`kit21` arm copies them, and the copy's engine is run. The tracked engine is never edited.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/check-memory-hygiene.sh`, only where S2 repairs the block
- `memory/guides/SESSION-KICKOFF.md`, only where S2 moves the engine
- `memory/gotchas/INDEX.md`, and one new record under `memory/gotchas/` (S5)
- every other carrier of the memory-tree version marker, which `tools/check-kit-versions.sh`
  enumerates

## 5. Production-readiness checklist

- security — N/A: a test arm, and a repair of a block unit 6 specifies.
- perf / scale — Two engine runs over a minimal tree, seconds each.
- error / empty / loading states — The clean case is the green-run observation.
- observability — The arm's failure names which half went wrong.
- risks — A minimal tree can red other checks, which would hide check 28's block. The fixture is
  built otherwise clean, AC2 asserts it, and AC1 asserts that 28 is the only check the branch run
  names.
- testing — S3's arm, observed RED with the block's `status=1` deleted.
- migration — None.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When the worktree's `tools/memory-tree/check-memory-hygiene.sh` runs by its path, with
  the working directory at the root of the fixture's branch and `GOV_DEFAULT_BRANCH=main`, it exits
  non-zero, prints a line opening `check 28:` naming both gotcha stems, and prints no other line
  opening `check <n>:`. With the block's `status=1` deleted in a scratch copy of the kit directory,
  the copy's engine run the same way exits 0; that red is observed once.
  Red when: the block swallows the mode's exit, so the engine exits 0 over the duplicate, or another
  check holds the exit.
- **AC2** — When the same command runs on the fixture's `main`, it exits 0 and prints a line
  opening `row-grammar: check 28 graded`.
  Red when: the green-run print is missing, or the clean tree reds.
- **AC3** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no memory-tree carrier left behind, and
  `bash skills/session-kickoff/manifest-check.sh` prints no `MANIFEST check 5 FAILED` line.
  Red when: the kit's bytes moved without its version, or the engine moved without the stamp.
- **AC4** — When `python tools/memory-tree/gotchas.py --for-paths tools/memory-tree/check-memory-hygiene.sh`
  runs at the pass's commit, its output names S5's record, and `python tools/memory-tree/gotchas.py --check`
  exits 0.
  Red when: the record carries no anchor on the engine, so a diff of it never selects the class.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · the engine over an otherwise-clean branch adding a duplicated gotcha, asserting 28 is its only offending check, and over its clean main; stage the dispatch block's status=1 deleted, then its green-run print deleted, each in a scratch copy of the kit directory · the suite's floor rises by its new arm count

The close runs the legs and the suite; a pass runs the two engine commands above as its check.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from the round-1 spec audit's finding 20.
- rev-2 · 2026-10-04 · §3 §4 §5 §6 §7 §10 · S3 S5 · AC1 AC4 · folded the round-1 spec audit of
  units 10 to 15 on this unit: 23 (the fixture is built otherwise clean on `_b1`, the branch run's
  only offending check is 28, and §5's "AC2 separates" sentence is gone); 14 (the engine runs by its
  worktree path with the working directory at the fixture, and the staged break edits a scratch copy
  of the kit directory); and 33 (§3 cites `TOOL-aDeferredBar-8` and names the delegated dispatch
  block as a second signature, the decline is parked in the build README, and S5 adds the
  presence-probe gotcha as the documented check, AC4). The fixture also pins `GOV_DEFAULT_BRANCH`,
  as finding 28 asked of this unit's fixture.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "an engine-level arm that runs the hygiene gate over a
fixture tree and asserts a delegated check reds"` ranked name-stem neighbours only, with
`unscanned layers: .sh`. The seam is the hygiene suite's own fixture shape, `c6run` in
`tools/memory-tree/check-memory-hygiene.test.sh`, which asserts the gate ran before reading its
silence. The recall probe returned `TOOL-cSpliceWarden-6`, the ruling that check 24 delegates to
`row_grammar.py`, and `TOOL-aCollapsedScan-10`, which observed check 20 red on a staged break.
The round-1 audit of units 10 to 15 added `TOOL-aDeferredBar-8`, the open ask for a second
`check-arms.py` discovery signature, which §3 now engages. The fixture's seam moved from `c6run` to
`_b1` in the same suite, the one fixture there asserted otherwise clean before it reads a check.

Recall terms used: hygiene engine dispatch delegated row_grammar check-rotation status offender green-run summary arm staged break
