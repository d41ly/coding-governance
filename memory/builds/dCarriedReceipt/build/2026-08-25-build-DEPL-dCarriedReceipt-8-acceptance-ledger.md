# Acceptance ledger — DEPL-dCarriedReceipt-8, a merge result never overwrites `gov_oid`

**Serves:** journal DEPL-dCarriedReceipt-8

**Evidences:** DEPL-dCarriedReceipt-8
- AC1 — `python tools/govkit/govkit.py update --write` — RED observed on BOTH trees per §8 F3, and
  the two reds are NOT the same, which is a correction to the spec rather than a detail. At
  `9ddcc5c9`: run 1 reported `diverged 1 · stale 1` and the operator's line survived; run 2 reported
  `stale`, `wrote 2, deleted 0, 0 conflict(s)`, rc 0, and the line count went 1 to 0 with no finding
  printed. On `-7`'s tip the SAME fixture instead refuses at run 2 — rc 2, naming both oids, writing
  nothing, and unupdatable from then on. GREEN: run 1 `diverged`, run 2 `diverged`, line count 1
  after both.
- AC2 — `tools/govkit/selftest.py` — on the merged row `gov_oid` equals gov's blob at `--to` and
  `oid` equals the target's index blob; the two DIFFER, and `commit` advances. Before, one value
  held the merge result in both.
- AC3 — `python tools/govkit/govkit.py check` — RED measured on both trees immediately after a
  successful merge: rc 1, `provenance: 1/2 resolved`, naming the path. GREEN: rc 0 and
  `provenance: 2/2 resolved`.
- AC4 — `tools/govkit/selftest.py` — a four-vintage sequence. All four updates exit 0, every verdict
  on the delta row is `diverged` or `patched` and never `stale` or `missing`, and the operator's line
  survives all four.
- AC5 — `python tools/govkit/govkit.py selfcheck` — RED observed exactly as the spec names it: with
  the `(differs, differs)` grid cell hand-edited to `stale`, selfcheck exits 1 and names the cell.
  GREEN: `raw_write_cells(VERDICT_GRID) == []`. The predicate's LIVENESS half runs on every selftest
  invocation rather than once by hand, driving the engine's own `raw_write_cells` over a hand-edited
  COPY of the grid, and that liveness arm was itself red-verified.
- AC6 — `tools/govkit/selftest.py` — the no-regression arm on the row the operator never touched:
  it still reads `stale`, the index blob equals gov's blob at `--to`, and the two identities agree.
  Its fixture precondition — that gov's copy really moved between the vintages — is asserted first
  and red-verified.
- AC7 — `python tools/govkit/refusal_join.py` — exit 0 at 176 branches against a shrink-only pin of
  161. `-7` left it at 174 and this unit adds exactly the two it predicted. CAVEAT unchanged from
  `-7`: nothing passes `refusal_join` a reached-set, so its join half never executes.

## The spec was wrong and the spec moved

§8 F3 and §3's non-goal both predicted that `-7` preserves the corruption, so the red-first sequence
would reproduce identically on both trees. Measured, it does not. Corrected in place at rev-5; the
RESOLUTION is unchanged — observe on both, fix on `-7`'s tip — because only its grounds were wrong.

## S6 is PARTIAL, deliberately

The provenance loop in `cmd_check` now reads `gov_oid`, falling back to the legacy `sha256`
comparison only for a row that carries none. The INTEGRITY half was NOT repointed at `oid`, and that
is a refusal rather than an oversight: unit 5 AC2 modifies the WORKTREE only and expects `check` to
red, which an index-side comparison cannot see. Adding the `oid` read alongside would leave
`cmd_check` with two readers, which §10 forbids in the same sentence. AC3 is satisfied by the
provenance half alone, which is the half §1 and §6 name as the defect. Left open: the autocrlf-clone
false red on `check` that `-7`'s ledger already recorded as pre-existing is still pre-existing.
