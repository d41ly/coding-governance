# TOOL-cSpliceWarden-2 — hygiene check 10 reaches a backlog archive, and stops reporting a reassuring zero

**Status:** CLOSED · rev-3 · 2026-09-13 · node c · Tier-2 · base 09a22d2b · streams tooling · order 2 · ratified 2026-09-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-cSpliceWarden-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-cSpliceWarden-1-acceptance-ledger.md) | journal | TOOL-cSpliceWarden-1 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-4 TOOL-cSpliceWarden-5 |

<!-- /gen:spec-records -->

## 1. Goal

Check 10 asserts that a rotated archive is referenced from its live index. It has never graded a
backlog archive in this repo: it resolves the live index at a fixed path that no backlog shard
occupies, and the `[ -f ]` guard then `continue`s in silence. Make it resolve the index wherever the
shard actually lives, and fix the two further defects that surface the moment it does.

## 2. Scope (IN)

- **S1** — the live index is resolved by BASENAME anywhere under `$M/` outside `archive/`, not at the
  fixed path `$M/<stem>.md`. Observed by **AC1**.
- **S2** — a stem resolving to zero or to several live indexes is a NAMED finding, never a `continue`.
  Observed by **AC2**.
- **S3** — the filename anchor admits a disambiguating suffix after the date, so a second rotation of
  one day (`TOOL.2026-08-17b.md`) enters the population at all. Observed by **AC1**.
- **S4** — the reference is read from the index's PREAMBLE — the leading run of heading, blank and
  blockquote lines — instead of a fixed `head -3`. Observed by **AC3**.
- **S5** — the stranded self-test arm is re-keyed to the new message text, and a backlog-shard pair
  joins the fixture tree: one archive referenced, one not. Observed by **AC4**.

## 3. Non-goals (OUT)

- Fixing what the check then finds. `memory/archive/TOOL.2026-08-17b.md` is referenced from no shard
  in the tree; adding that reference is unit 4's, with the rest of the header repair.
- Asserting anything about an archive's CONTENTS. Check 10 grades one property — that the live index
  names its archive — and its header will say so, because a structural check reads as a semantic one
  to everybody who did not write it.
- Widening `row_grammar.py`'s file set. Unit 3, which needs the same stem resolution and gets its own.

### Edges

- **hands-off** `TOOL-cSpliceWarden-4` — that unit adds the missing `TOOL.2026-08-17b.md` reference
  this unit's check reds on.
- **hands-off** `TOOL-cSpliceWarden-5` — the two rows that filed S1 are consolidated and closed
  against this unit there.
- **hands-off** `TOOL-cSpliceWarden-3` — that unit reuses the enumeration half of this unit's §10
  contract for `row_docs()`, and its S4 is the arm joining the two readers.
- **hands-off** `TOOL-cSpliceWarden-6` — check 24 reuses this unit's enumeration AND its
  basename resolution rather than spelling a third copy of either.

## 4. Design

### Data model

Four defects, three of them not in the two filed rows. Measured 2026-09-12 on this repo at
`09a22d2b`, by running the candidate over the real tree:

| # | defect | evidence |
|---|---|---|
| 1 | fixed-path resolution — `idx="$M/${base%%.*}.md"` projects onto the memory root only | of four rotated archives the shipped check grades ONE and skips three in silence |
| 2 | the `[ -f ]` guard `continue`s | a skipped archive prints what a referenced one prints |
| 3 | the anchor `<date>\.md$` does not enumerate a suffixed name | `TOOL.2026-08-17b.md` is invisible to the check entirely |
| 4 | the `head -3` window | this repo's shard carries its rotation notes on lines 4 and 5 |

Defects 1 and 2 are the two filed rows from two angles. Defect 3 was named in the brief. **Defect 4
was found only by running the candidate over the real tree**, and it is the one that bites: fixing
the path resolution WITHOUT widening the window reds three files, two of them falsely, against
rotation notes that are plainly present. That is the predicate-reds-innocent-files class, caught the
way §7 says to catch it.

### Migration

None. The check's population grows from 1 graded file to 4 in this repo; no data moves.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` (check 10's block) ·
`tools/memory-tree/check-memory-hygiene.test.sh` (the stranded arm, plus the new fixture pair).

### Alternatives rejected

- **Keep `head -3` and widen it to `head -8`.** Rejected: a magic number that goes stale on the next
  rotation. The preamble is DERIVED — rows begin at the first non-preamble line, so the window cannot
  swallow a row and cannot be outgrown.
- **Resolve the index from the declared `FAMILIES`.** Rejected: it would assert one derived value
  against another the same call derives, the tautology `row_grammar.py` already records; and it would
  miss `DECISIONS`, which is not a family.

## 5. Production-readiness checklist

- security — N/A — a read-only structural check over tracked paths.
- perf / scale — the inner resolution walks `$FILES` per archive. Four archives against a few hundred
  tracked paths; the check keeps its `(always; cheap)` header.
- error / empty / loading states — zero-resolution and many-resolution are both named findings, which
  is the whole of S2. The empty case is the one that made this check inert.
- observability — every finding names the archive, the stem, and the index it resolved to.
- risks — the message text CHANGES, which strands the existing self-test arm at
  `check-memory-hygiene.test.sh:1182`. This repo has hit `arm-literal-strands-on-message-edit` three
  times in one file in one session; S5 exists because of it.
- testing — AC1-AC4, plus the observed RED on the real tree.
- migration — none.
- user docs — the check's own header, which will state what it does NOT check.

## 6. Acceptance criteria

- **AC1** — When the rewritten check 10 runs over this tree, it enumerates exactly the four real
  archives and reds on exactly `memory/archive/TOOL.2026-08-17b.md`.
  Red when: the population includes the eight `parallel-coding-governance.template-v-2-*.md`
  snapshots or the four `memory/archive/ledger/*.md` shards, which carry no date component and must
  never enter it.
  figure: DERIVED — the criterion re-runs the check rather than restating the count.
- **AC2** — When a fixture tree holds an archive whose stem resolves to no live index,
  `check-memory-hygiene.sh` names that archive and says the stem resolved to 0.
  Red when: the run is silent, which is the shipped behaviour this unit removes.
- **AC3** — When the `Rotated 2026-08-14` note is deleted from `memory/backlog/TOOL.md` line 4 in a
  scratch copy, the check reds on `TOOL.2026-08-14.md`; restoring it returns green.
  Red when: the check stays green with the note gone, which would mean the preamble window is not
  discriminating and AC1's green is only evidence the predicate can be silenced.
- **AC4** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, it exits 0, and its
  check-10 arms assert the NEW message text.
  Red when: the arm still greps `(lines 1-3)`, which passes by matching nothing after the message
  changes.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)`

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · a backlog shard plus two archives, one referenced in the preamble and one not · re-measure `ARMS_FLOORS` for `check-memory-hygiene.sh` in the same commit if the fail-branch count moves.

## 8. Open questions

none — the four defects are established by measurement and the remedy for each follows from it.

## 9. Revision log

- rev-1 · 2026-09-12 · the first draft.
- rev-3 · 2026-09-13 · §3 — the hands-off edge to `TOOL-cSpliceWarden-6`, which consumes this
  unit's enumeration contract and its resolution
- rev-2 · 2026-09-13 · §3 · §10 — the enumeration contract split into its shared ENUMERATION half and check-10-only RESOLUTION half, after the cross-reader arm proved the two readers had drifted; edges completed both ways

## 10. Reuse audit

No existing seam fits: the stem-to-live-index resolution does not exist anywhere in the kit today,
which is precisely defect 1. This unit AUTHORS it in shell, and `TOOL-cSpliceWarden-3` needs the
ENUMERATION half of the same rule in Python for `row_grammar.row_docs()` — two implementations of one
rule, which §12 calls two answers to one question.

The contract is therefore specified once, here, and the two readers are joined by a gate arm rather
than by a promise. It has two halves and only the first is shared:

- **Enumeration (BOTH readers).** A rotated archive is `<M>/archive/<STEM>.<iso-date><suffix?>.md`,
  FLAT — no subdirectory — where `<STEM>` is `DECISIONS` or one of the DECLARED `FAMILIES`. The two
  conditions are a conjunction, and each carries the other's weight: the date anchor keeps a
  family-named file that is not a rotation out, and the `FAMILIES` prefix keeps a dated file that is
  not a row document out. Verified 2026-09-12 that each condition alone selects the same four files
  in this tree and that their conjunction does too, so neither is currently load-bearing and both are
  kept for the case that is not this tree. `FAMILIES` is DECLARED rather than derived from the tree,
  so deleting a shard cannot silently shrink the scanned set.
- **Resolution (check 10 only).** The live index for `<STEM>` is the unique tracked `<STEM>.md` under
  `<M>/` outside `archive/`. Zero or many is a refusal, never a skip. `row_grammar.py` needs no
  resolution — it scans the archive whether or not a live counterpart exists, which is what keeps its
  population from narrowing when check 10's resolution fails.

Unit 3's §10 cites this section rather than restating it, and its S4 is the arm that asserts the two
readers enumerate the same set.
Recall terms used: `rotation archive backlog terminal carry-forward index cap shard hygiene check ratified supersede reconcile`
