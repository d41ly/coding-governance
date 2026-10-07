# TOOL-aClassedKnob-3 — the verdict epoch reads an adopter's vendored engine against its install receipt

**Status:** SPECCED · rev-1 · 2026-10-07 · node a · Tier-1 · base 56c2b82e · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Stop `check-verdict-epoch.sh` from failing an adopter whose pull wrote gov's engine bytes in two
commits, bump first. Where every scanned file at HEAD is gov's own blob and the constant matches the
receipt's recorded vintage, gov's landing already dated those verdicts and the range's commit order
says nothing about them.

## 2. Scope (IN)

- S1. After W is found and before the bump search, the gate reads the committed
  `.governance/install.json` at HEAD. When every scanned file has a receipt row whose `oid` equals
  its blob at HEAD and equals `gov_oid`, and the engine row's `KIT_MEMORY_TREE_VERSION` value equals
  the constant at HEAD, it prints `clean — vendored at gov's memory-tree <v>` and exits 0.
  Observed by AC1 and AC3.
- S2. Any other case, which includes no receipt, no python, a missing row, a local edit, or a
  version mismatch, falls through to the topological rule unchanged. Observed by AC2.
- S3. The gate's header states what this does not check: that the receipt itself is honest.
  NOT OBSERVED: prose.

## 3. Non-goals (OUT)

No `--full-history` on the bump search. A `--no-ff` merge that only carries a branch's earlier bump
would then excuse every unbumped edit after that bump, which is the hole the topological rule closes.
No change to the minter, the lander or govkit.

### Edges

none

## 4. Design

The receipt is govkit's: per file `path`, `oid` (the adopter's blob), `gov_oid` (gov's blob at the
recorded `gov_commit`) and `version`, the kit's version line. All three equal means gov's bytes,
unmodified, at a vintage gov's own lander dated. A local edit changes the blob at HEAD, so the
exemption cannot cover it. gov has no receipt, so gov's behaviour does not move.

The HEAD blobs come from one `git ls-tree HEAD -- <scan set>`. The receipt is read from HEAD, not
the working tree, which matches what the range is judged on.

### Files touched (estimate)

- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/memory-tree/check-verdict-epoch.test.sh`

## 5. Production-readiness checklist

- security — a hand-edited receipt can claim gov's blob for a local edit. The receipt is govkit's
  record and is graded there; this gate trusts it and says so.
- testing — AC1 to AC3.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When the gate runs in a clone of nc at `803767cd` with `GATE_PUSH_BASE=e955ae4b`, it
  exits 0 naming `vendored at gov's memory-tree 2.133`. Red when: the exemption does not fire on a
  two-commit pull of unmodified gov bytes.
- **AC2** — When a fixture's receipt vouches for the engine and a later commit edits `tree_lib.py`
  without a bump, the gate exits 1. Red when: the exemption covers a blob the receipt does not record.
- **AC3** — When a fixture pulls gov bytes in two commits, bump first, with a receipt vouching for
  them, the gate exits 0 at `GATE_PUSH_BASE`. Red when: the receipt read is skipped.

## 7. Gates

`verdict epoch (kit version dates the engine)` · `verdict-epoch self-test`

New arm: tools/memory-tree/check-verdict-epoch.test.sh · covers AC2 AC3 · a fixture receipt over a two-commit pull, then a local edit · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-07 · initial draft.
