# TOOL-aTunedCompass-1 — the two records this build's parent refuted are corrected in place

**Status:** CLOSED · rev-2 · 2026-09-05 · node a · Tier-1 · base c4fcf5ad · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aTunedCompass-1-closing-diff-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-closing-diff-round1.md) | diff-review | TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |
| [2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md) | spec-audit | TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-9 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |

<!-- /gen:spec-records -->

## 1. Goal

Two records in this repo assert facts their own cited sources refute, and both sit on the path a
session reads at orientation. Correct both in place, so the backlog and the waiver registry stop
handing a false fact to the next reader.

## 2. Scope (IN)

- **S1** — `TOOL-aProvenReuse-4` in `memory/backlog/TOOL.md` moves to `CLOSED`. Its refuted half is
  the claim that `reuse_lookup.py` logs nothing. The writer is at
  `tools/codebase-map/reuse_lookup.py` (`:417`), it landed in commit `5a368d98`, and the log it
  writes holds hundreds of rows.
- **S2** — the rewritten row preserves the half that survives. The map log records the query and a
  count, never the results, so the probe has liveness evidence and still has no efficacy evidence.
  The row names `TOOL-aWeighedCompass-10` as the successor carrying that half.
- **S3** — the rewritten row fits `ENTRY_CAP_CHARS`, the 300-character default declared in
  `tools/memory-tree/check-memory-hygiene.sh` (`:73`). The row it replaces is several times that and
  passes only because the shard is waived, so shortening it removes one dependency on the waiver.
- **S4** — `TOOL-aWeighedCompass-2`, the row that asked for S1, moves to `CLOSED` and names this
  unit as what did it.
- **S5** — the `memory/backlog/TOOL.md` note in `memory/project/curation-debt.txt` loses its claim
  that rotation is the live remedy. It states instead what was measured: rotating every terminal row
  sheds about 56 KB and leaves about 204 KB against the 61440-byte `INDEX_CAP_BYTES`, more than
  three times the cap, because the mass is the OPEN rows rather than the terminal ones.
- **S6** — that note names the live remedy as a split or a shortening sweep, and points at
  `TOOL-aWeighedCompass-3`, which carries the owner call. It keeps its blast-radius paragraph and
  its statement that the waiver currently hides one real status-token fault. Both are still true and
  neither is this unit's subject.
- **S7** — `TOOL-aWeighedCompass-3`'s closing sentence, which instructs a reader to correct the
  note, is amended to record that the note half landed here. An instruction already carried out
  reads as outstanding work, which is a mild form of the same defect this unit removes.

## 3. Non-goals (OUT)

- Not rotating, splitting or shortening `memory/backlog/TOOL.md`. The build README parks that as an
  owner call, and the parent measured that rotation cannot fix it.
- Not removing any row from `memory/project/curation-debt.txt`. The shard still breaches the byte
  cap, so the waiver is still load-bearing; only the note's prose is wrong.
- Not fixing the status-token fault the waiver hides. That is a data fault in one row rather than a
  record contradicting its source, and it belongs with whichever unit drains the shard.
- Not appending anything to `memory/DECISIONS.md`. A backlog is mutable by design and correcting a
  row is not a new ratified decision.
- No code, no kit change, no new gate leg. See §5 for why the class this unit fixes is not gateable.

## 4. Design

### Inventory

| Carrier | The refuted claim | The source that refutes it |
|---|---|---|
| `memory/backlog/TOOL.md`, row `TOOL-aProvenReuse-4` | the reuse probe logs nothing | `tools/codebase-map/reuse_lookup.py` (`:417`) |
| `memory/project/curation-debt.txt`, the backlog-shard note | rotation is the live remedy | the by-status re-derivation in the parent's report |

Both edits are prose replacements inside a mutable record. The backlog row keeps its id, its
position and its pointer field; only the status token and the one-liner change. The registry keeps
all four of its listed paths, so the set membership the hygiene gate reads is untouched and the
shrink-only property of `memory/project/` is not tested by this unit.

### Where the numbers come from

Every figure above is quoted from
`memory/builds/aWeighedCompass/build/2026-09-04-build-TOOL-aWeighedCompass-1-findings.md`, findings
9 and 11. Nothing here re-derives them. The corrected note cites that record by path, so the next
reader can re-measure rather than trust the sentence.

### Files touched (estimate)

`memory/backlog/TOOL.md` and `memory/project/curation-debt.txt`. Two files, both records.

### Alternatives rejected

Appending a correction line beneath the stale row was rejected. The false sentence would stay on the
page a session reads at orientation, which is the entire defect; the backlog is mutable precisely so
that a superseded row can be rewritten rather than annotated.

Leaving `TOOL-aWeighedCompass-2` open until the whole build lands was rejected. It is the row that
asked for exactly S1, and a row describing completed work is the same class of stale record.

## 5. Production-readiness checklist

- security — N/A. No surface, no write path, no runtime.
- perf / scale — the rewritten row is shorter than the one it replaces, so the shard shrinks by a
  few hundred bytes. That is not a remedy and is not claimed as one.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — N/A. Nothing executes.
- observability — the corrected note names the record that measured it, so a later reader can
  re-derive the remainder instead of inheriting a second unfalsifiable claim.
- risks — `memory/backlog/TOOL.md` is reconciled by the row-keyed merge driver, so a concurrent node
  editing the same row reconciles per row rather than per file. The stated byte figures are
  measured-at values and will drift as rows land; they are attributed to the record that took them
  rather than presented as current.
- testing + left-shift gates — no gate, and the reason is worth stating plainly. The class is "a
  record asserts something its own cited source contradicts", and deciding it needs a reader who can
  evaluate a natural-language claim against a source. A predicate cannot. The nearest mechanical
  proxies already exist and already fire as report-only `drift-audit` signals, which is why this
  build's parent found both instances by running `python tools/drift-audit/drift_report.py` and then
  reading. The left-shift here is that habit, not a fourteenth signal that would grep for prose it
  cannot evaluate.
- migration / rollback — a one-commit revert restores both files.
- user docs — N/A. Memory records are not `help/` pages.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'TOOL-aProvenReuse-4' memory/backlog/TOOL.md` is run, the row leads with
  the status token `CLOSED` and no longer contains the claim that the probe logs nothing.
- **AC2** — When that row is read, it names `tools/codebase-map/reuse_lookup.py` as the writer and
  `TOOL-aWeighedCompass-10` as the successor for the efficacy half.
- **AC3** — When the rewritten row's length is measured against the `ENTRY_CAP_CHARS` value in
  `tools/memory-tree/check-memory-hygiene.sh`, it is at or under that cap.
- **AC4** — When `grep -n rotation memory/project/curation-debt.txt` is run, no surviving line names
  rotation as the live remedy for the backlog shard.
- **AC5** — When the shard's note in `memory/project/curation-debt.txt` is read, it states the
  measured remainder against `INDEX_CAP_BYTES` and names `TOOL-aWeighedCompass-3` as the row
  carrying the owner call.
- **AC6** — When that same note is read, it still carries its blast-radius paragraph and its
  sentence that `check 8` is hiding one real status-token fault.
- **AC7** — When `grep -n 'TOOL-aWeighedCompass-2' memory/backlog/TOOL.md` is run, the row reads
  `CLOSED` and names `TOOL-aTunedCompass-1`.
- **AC8** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs on the edited tree, it exits
  0, and `memory/project/curation-debt.txt` still lists the same four paths it listed before.

## 7. Gates

The unit must keep `memory hygiene` (`bash tools/memory-tree/check-memory-hygiene.sh`),
`spec tokens (a spec's own names resolve)` (`python tools/check-spec-tokens.py`),
`dead-path carriers (deleted files still named)` (`bash tools/check-dead-paths.sh`) and
`drift-audit records` (`python tools/drift-audit/drift_report.py --check`) green. All four are
records-or-declarations legs that run on an ordinary bar. The full bar is
`bash tools/run-gates/run-gates.sh`. This unit adds no gate.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · M2 cross-read. This spec and `TOOL-aTunedCompass-8` cited the same writer at
  two line numbers, `:442` here against `:417` there. `def write_lookup` is at 417 and `:442` is a
  path assignment inside its body, so the citation here was the defect and both carriers now spell
  the function definition.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "correct a backlog row that states a fact its own cited
source refutes"` found no existing seam, and the evidence is what it returned. Its ranked candidates
were `owners_of`, `append_backlog` and `backlog_keys` in `tools/codebase-map/map_lib.py`, the row
helpers in `tools/memory-tree/merge-rows.py`, and `classify_row` in `tools/govkit/govkit.py`, every
one matched on the name stem `row` or `backlog`. The probe indexes 645 Python symbols and this unit
writes no code at all, so no seam applies by construction. The two carriers it edits are records,
and the only machinery that touches them is the hygiene gate and the row-keyed merge driver, both of
which this unit leaves alone.

Recall terms used: `backlog row stale claim curation-debt waiver rotation index cap orientation
reading liveness evidence`, against the question of why a backlog row that cites its own source
still asserts a fact the source refutes. It returned 40 hits; the ones that bind are the two open
rows recording these corrections, the parent's own finding on the waiver, and
`TOOL-aRelaxedShard-4`, which is why the shard's real bound is its live row count rather than its
byte cap.
