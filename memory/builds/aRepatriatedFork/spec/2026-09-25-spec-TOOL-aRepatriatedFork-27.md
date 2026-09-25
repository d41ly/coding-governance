# TOOL-aRepatriatedFork-27 — canonical-copy markers and comment prose name no install prefix

**Status:** SPECCED · rev-1 · 2026-09-25 · node a · Tier-1 · base 2143b6d6 · streams tooling · order 12

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Two kinds of non-executing text carry gov's prefix in received code. The first is the
`# >>> <block> — canonical copy: tools/lib/<file>` marker on every inline copy of a byte-compared
block. Several ledger reason columns call it underivable, but `kit-rel.sh`'s marker already names
its canonical copy in words. The second is comment prose that cites a kit file by its path at gov's
prefix. This unit rewords both, the marker in lockstep with every copy.

## 2. Scope (IN)

- **S1** — The `resolve_python` and `render_doc` markers are reworded in `tools/lib/resolve-python.sh`
  and `tools/lib/render-doc.sh` and in every inline copy, in one commit, to the form
  `tools/lib/kit-rel.sh:24` uses: the file's name, then "in gov's lib dir". The byte-identity
  compare in `tools/lib/resolve-python.test.sh` stays green because every copy moves together.
  Observed by AC1, AC2.
- **S2** — Comment prose in received, non-test, non-gov-side code names a kit in words or names a
  file by its kit-relative path, never both with gov's prefix. This follows the rule the gate's own
  epoch-4 note gives. It includes the two uncompared preamble lines above each inline resolver
  block, which census §5 found outside the parity compare. Observed by AC3.
- **S3** — Arm 1's two class-G lines, `gen_map.py:47` and `adopt-codebase-map.sh:155`, quote the
  legacy regen literal. They are reworded, and their waiver rows are struck. Observed by AC4.
- **S4** — The ledger rows for these files are lowered, and every kit moved takes its version bump in
  every carrier. Observed by AC5.

## 3. Non-goals (OUT)

- Comments inside test files, which `TOOL-aRepatriatedFork-28` owns, and inside gov-side or withheld
  files, which `TOOL-aRepatriatedFork-29` owns. The marker line in a test file is this unit's
  anyway, because the lockstep cannot be split.
- Any executing line. A comment beside one is still this unit's.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-23` — the epoch-5 ledger rows for directory-only and
  `/`-led comment spellings, which epoch 4 cannot see.

## 4. Design

### Evidence

From the 2026-09-25 prefix census at `2143b6d6` (session scratchpad, not committed). PINNED,
measured 2026-09-25.

- Census §4 lists 24 class-E literals over 22 files: 22 `resolve_python` markers and 2 `render_doc`
  markers. The two canonical files hold one more each, in the 57 files no descriptor resolves
  (`pcensus/unres/occ_unres.tsv`).
- Census §4 lists 128 class-G literals over 74 files.
- The ownership rule (`pcensus/alloc2.py`) gives this unit 120 literals over 57 files: 95 counted
  today, 23 invisible and the 2 canonical markers. The largest are `run-gates/run-gates.sh` with 7,
  `drift-audit/adopt-drift-audit.sh`, `memory-tree/check-memory-hygiene.sh` and
  `memory-tree/merge-rows.sh` with 6 each, and `memory-recall/adopt-memory-recall.sh` and
  `unattended/run-unattended-gates.sh` with 5 each.
- Census §5 found the `manifest-check.test.sh` reason column wrong: `resolve-python.test.sh`'s
  `blk()` compares from the `# >>>` line to `# <<<` only, so the two lines above it are ordinary
  comments. The same two lines sit uncompared in six other files.

### Ownership rule

This unit owns every canonical-copy marker line wherever it sits, and every class-G or comment
literal in a received file that is not a test, not withheld and not gov-side. The rule is
`TOOL-aRepatriatedFork-23` §8 F3's.

### Files touched (estimate)

`tools/lib/resolve-python.sh` · `tools/lib/render-doc.sh` · the 57 files `pcensus/alloc2.py` lists
for this unit, under `tools/run-gates/`, `tools/memory-tree/`, `tools/drift-audit/`,
`tools/memory-recall/`, `tools/unattended/`, `tools/codebase-map/`, `tools/workflows/`,
`tools/hooks/`, `tools/lexicon/`, `tools/process-monitor/`, `tools/runlog/` and
`skills/session-kickoff/`, the loose checkers under `tools/`, and `.githooks/pre-push` ·
`tools/install-prefix-waivers.txt` · `tools/install-prefix-carried.txt`

### Alternatives rejected

- Leaving the markers as literals with a reason column. `kit-rel.sh` shows the literal is not
  needed, and the owner's end state has no reason column to hold one.

## 5. Production-readiness checklist

- security — none; comments.
- perf / scale — none.
- error / empty / loading states — none.
- observability — none.
- risks — a marker reworded in some copies and not others reds the byte-identity compare, which is
  the gate doing its job; S1 is one commit.
- testing — the resolver parity arm over every copy.
- migration — an adopter's copies move on the next `govkit update`, with the kit version.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `git grep -n 'canonical copy: tools/' -- tools skills .githooks` runs, it finds nothing.
  Red when: any marker still names gov's prefix.
- **AC2** — When one copy's marker is left at the old wording in a scratch clone, the byte-identity
  compare of the `resolve_python` block reds naming that copy. Staged and recorded, then discarded.
  Red when: the compare passes with a stale copy, so it no longer covers the marker line.
- **AC3** — When `bash tools/check-install-prefix.sh --list` runs, no ledger row remains for any file
  this unit owns.
  Red when: an owned file keeps a row.
  figure: DERIVED at observation time.
- **AC4** — When `bash tools/check-install-prefix.sh` runs, it reports no stale waiver row for
  `gen_map.py` or `adopt-codebase-map.sh`.
  Red when: a waiver row outlives the line it excused.
- **AC5** — `bash tools/check-kit-versions.sh` exits 0, and `python tools/govkit/govkit.py epoch
  --base 2143b6d6` names no kit this unit moved.
  Red when: a moved kit's carrier was missed.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `line length` · `lexicon naming predicates` · `manifest-check self-test` · `agent-cap self-test` · `scratch-guard self-test` · `row-keyed merge driver replay` · `pre-push run-log line` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `drift-audit selftest` · `process-monitor census selftest` · `process-monitor adopter selftest` · `runlog selftest` · `run-gates run-log line` · `hook destinations self-test` · `lexicon selftest` · `run-selftests self-test`

New arm: `tools/lib/resolve-python.test.sh` · one inline copy left at the old marker wording ·
none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft. Owner rulings of 2026-09-25: drain every hard-coded kit
  prefix, with no class exempted, before `TOOL-aRepatriatedFork-18`'s held leg. This unit is census
  classes E and G; E is one lockstep commit, as census §6 recommends.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "canonical copy marker of an inline block byte
compared"` ranked `canonical_ctx`, `find_block` and `marker_pair` in `tools/govkit/govkit.py`,
which read govkit's own marker pairs and not a shell block's header. The precedent reused is a
spelling: `tools/lib/kit-rel.sh:24`'s marker, which already names its canonical copy in words.

Recall terms used: `canonical copy marker resolve_python render_doc byte-identical parity inline
block kit-rel comment prose`.
