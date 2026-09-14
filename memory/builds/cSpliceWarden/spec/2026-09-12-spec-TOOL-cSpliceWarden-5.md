# TOOL-cSpliceWarden-5 — two rows filing one gap become one, and a false retirement is superseded

**Status:** CLOSED · rev-2 · 2026-09-13 · node c · Tier-1 · base 09a22d2b · streams tooling · order 5 · ratified 2026-09-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-cSpliceWarden-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-cSpliceWarden-1-acceptance-ledger.md) | journal | TOOL-cSpliceWarden-1 TOOL-cSpliceWarden-2 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-4 |

<!-- /gen:spec-records -->

## 1. Goal

Three backlog rows describe the same check-20/check-10 blindness and disagree about it. Two file the
check-10 gap twice; a third was retired WONTDO on a claim that is false. Consolidate the pair, correct
the retirement, and file what this build deliberately leaves undone.

## 2. Scope (IN)

- **S1** — `TOOL-cTracedPromise-6` and `TOOL-aBoundedVerdict-9` consolidated. They are one defect from
  two angles: fixed-path resolution, and the `[ -f ]` guard that skips because of it. Neither mentions
  the `b`-suffix miss or the `head -3` window. One row survives, CLOSED by `TOOL-cSpliceWarden-2`,
  naming all four defects; the other closes as superseded, pointing at it. Observed by **AC1**.
- **S2** — the `aCollapsedScan` build's sixth row, the retirement, corrected. It reads WONTDO, asserting check 20
  "asserts per-file id uniqueness across `memory/DECISIONS.md`, the backlog shards and the rotated
  archives". That is true only for DECISIONS archives: `row_docs()` admits an archive only when its
  basename starts with `DECISIONS.`, so all three TOOL archives were outside check 20 entirely. The
  row is append-only history and is superseded by a new row, not rewritten. Observed by **AC2**.
- **S3** — the same over-broad claim removed from the two other carriers that state it:
  `row_grammar.py`'s `row_docs()` docstring and `memory/HYGIENE.md`'s check-20 description. Observed
  by **AC3**.
- **S4** — the rows this build leaves undone are filed, each naming why: the ungraded `ROTATION_MODE`,
  and the `TOOL.2026-08-17.md` / `TOOL.2026-08-17b.md` overlap. Observed by **AC4**.

## 3. Non-goals (OUT)

- Rewriting `memory/DECISIONS.md:128`. The decision log is append-only and a landed row is never
  edited; if it inherits the over-broad claim it takes a superseding row, which is S2's form.
- Closing the rows this build only files. Filing is the deliverable; building them is not in scope.

### Edges

- **consumes-from** `TOOL-cSpliceWarden-2` — S1's surviving row is closed BY that unit, so it cannot
  land before it.
- **consumes-from** `TOOL-cSpliceWarden-3` — S3's docstring correction lands with that unit's widening,
  because after the widening the claim becomes true and the correction is the sentence that says so.

## 4. Design

The three rows, and what each gets:

The row at `memory/backlog/TOOL.md:118` reads OPEN and says check 10 resolves by fixed path, blind to
every shard. It SURVIVES, rewritten to name all four defects, and closes against
`TOOL-cSpliceWarden-2`.

The row at `TOOL.md:159` reads OPEN and states the same defect as the `[ -f ]` guard skipping. It
closes as superseded, pointing at the survivor.

The row at `TOOL.md:266` is the `aCollapsedScan` build's sixth, retired WONTDO on the claim that
every premise it was filed on was wrong. It stays the ratified record it is, and a NEW row records
that its own premise was wrong for backlog archives.

Neither `aCollapsedScan`'s id nor either filing row's id is spelled in a table cell or at the head of
a bullet anywhere in this build's records. A leading-cell or dash-led id is a DEFINITION anchor, so
writing one would make this build folder a second claimant of another build's id — check 13's
collision, caused by the record complaining about it.

`TOOL-cTracedPromise-6` survives rather than `TOOL-aBoundedVerdict-9` because it states the remedy
this build actually took — "resolve it anywhere under the memory root" — and because it is the older
id, so the surviving row is the one whose citation history is longer.

**The retirement is not rewritten.** That row is WONTDO and terminal, and this repo
supersedes rather than edits. What makes the correction findable is that the new row cites the old id,
so a grep for either reaches both.

### Files touched (estimate)

`memory/backlog/TOOL.md` · `memory/DECISIONS.md` · `tools/memory-tree/row_grammar.py` (docstring) ·
`tools/memory-tree/HYGIENE.template.md` and its render.

## 5. Acceptance criteria

- **AC1** — When `grep -n 'cTracedPromise-6\|aBoundedVerdict-9' memory/backlog/TOOL.md` runs, both rows
  read a terminal status and exactly one of them names the four defects.
  Red when: both still read OPEN, or the survivor still describes only the fixed-path half.
- **AC2** — When `grep -n aCollapsedScan memory/backlog/TOOL.md` runs, the WONTDO row is unchanged
  byte-for-byte and a second row cites it.
  Red when: the WONTDO row was edited, which is the rewrite this repo forbids.
- **AC3** — When `grep -rn 'rotated archives' tools/memory-tree/row_grammar.py memory/HYGIENE.md` runs,
  no surviving sentence claims check 20 covers archives it does not.
  Red when: a carrier still states the over-broad claim after the widening changed what is true.
- **AC4** — When `python tools/memory-tree/gen_build_index.py --check` runs, it exits 0 and the new
  rows appear in the rendered index.
  Red when: a filed row was written with an id this session did not mint.

## 6. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity`

## 7. Open questions

none.

## 8. Revision log

- rev-1 · 2026-09-12 · the first draft.
- rev-2 · 2026-09-13 · §4 · AC2 — the disposition table rewritten as prose, because a foreign id in a leading table cell is a DEFINITION anchor and made this build a second claimant of another build's id
