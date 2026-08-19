---
slug: aMendedLedger
node: a
opened: 2026-08-09
streams: tooling+playbook
roster: TOOL
ids: TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 TOOL-aMendedLedger-9
---

# aMendedLedger — finish the memory rework: drain the ledger, drive the merge, re-true the docs

Node `a` · opened 2026-08-09 · streams tooling + playbook.

Closes the four items `TOOL-aFoldedQuarry-1` left open when it ported upstream
`ARCH-dQuarriedLedger-1`: the authored session ledger, the absent row-keyed merge driver, and the
governing docs that describe a tree this repo no longer has.

The table below is
GENERATED from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** SPECCED · 8 unit(s) · node a · opened 2026-08-09 · streams tooling+playbook
ids TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 TOOL-aMendedLedger-9

<!-- gen:build-units -->
| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aMendedLedger-1 — finish the memory rework: drain the ledger, drive the merge, re-true the docs](spec/2026-08-09-spec-aMendedLedger-1.md) | SPECCED | rev-5 | 2026-08-09 |
| [TOOL-aMendedLedger-2 — U1: the journal relocation pass, plus the three .md stub deletions](spec/units/2026-08-09-spec-aMendedLedger-2-u1-journal-relocation.md) | SPECCED | rev-2 | 2026-08-09 |
| [TOOL-aMendedLedger-3 — U2: retire the authored session ledger and resolve the drift probe](spec/units/2026-08-09-spec-aMendedLedger-3-u2-ledger-retirement.md) | SPECCED | rev-2 | 2026-08-09 |
| [TOOL-aMendedLedger-4 — U3: make the hygiene gate and the adopter scaffold match the drained tree](spec/units/2026-08-09-spec-aMendedLedger-4-u3-hygiene-gate.md) | SPECCED | rev-2 | 2026-08-09 |
| [TOOL-aMendedLedger-5 — U5: the row-keyed merge driver, its launcher shim and its wiring](spec/units/2026-08-09-spec-aMendedLedger-5-u5-merge-driver.md) | SPECCED | rev-3 | 2026-08-09 |
| [TOOL-aMendedLedger-6 — U6: doc truth, the template edit, the residual sweep and the adopter note](spec/units/2026-08-09-spec-aMendedLedger-6-u6-doc-truth.md) | SPECCED | rev-2 | 2026-08-09 |
| [TOOL-aMendedLedger-7 — U8: a fully keyed decision corpus](spec/units/2026-08-09-spec-aMendedLedger-7-u8-keyed-corpus.md) | SPECCED | rev-2 | 2026-08-09 |
| [TOOL-aMendedLedger-8 — U9: the merge driver, redesigned around what git already gets right](spec/units/2026-08-10-spec-aMendedLedger-8-u9-driver-redesign.md) | SPECCED | rev-2 | 2026-08-10 |
<!-- /gen:build-units -->

Records live under `spec/`, `build/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-10-build-TOOL-aMendedLedger-1-1-driver-repro-corpus.md](build/2026-08-10-build-TOOL-aMendedLedger-1-1-driver-repro-corpus.md) | journal | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md](reviews/2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-09-review-TOOL-aMendedLedger-1-2-repair.md](reviews/2026-08-09-review-TOOL-aMendedLedger-1-2-repair.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-09-review-TOOL-aMendedLedger-1-3-regression.md](reviews/2026-08-09-review-TOOL-aMendedLedger-1-3-regression.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |
| [2026-08-10-review-TOOL-aMendedLedger-1-4-u9-redesign.md](reviews/2026-08-10-review-TOOL-aMendedLedger-1-4-u9-redesign.md) | diff-review | TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8 |

Ids no `spec-audit` record has ever named: TOOL-aMendedLedger-1 TOOL-aMendedLedger-2 TOOL-aMendedLedger-3 TOOL-aMendedLedger-4 TOOL-aMendedLedger-5 TOOL-aMendedLedger-6 TOOL-aMendedLedger-7 TOOL-aMendedLedger-8.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-09-spec-aMendedLedger-1.md](spec/2026-08-09-spec-aMendedLedger-1.md)
  - [2026-08-09-spec-aMendedLedger-2-u1-journal-relocation.md](spec/units/2026-08-09-spec-aMendedLedger-2-u1-journal-relocation.md)
  - [2026-08-09-spec-aMendedLedger-3-u2-ledger-retirement.md](spec/units/2026-08-09-spec-aMendedLedger-3-u2-ledger-retirement.md)
  - [2026-08-09-spec-aMendedLedger-4-u3-hygiene-gate.md](spec/units/2026-08-09-spec-aMendedLedger-4-u3-hygiene-gate.md)
  - [2026-08-09-spec-aMendedLedger-5-u5-merge-driver.md](spec/units/2026-08-09-spec-aMendedLedger-5-u5-merge-driver.md)
  - [2026-08-09-spec-aMendedLedger-6-u6-doc-truth.md](spec/units/2026-08-09-spec-aMendedLedger-6-u6-doc-truth.md)
  - [2026-08-09-spec-aMendedLedger-7-u8-keyed-corpus.md](spec/units/2026-08-09-spec-aMendedLedger-7-u8-keyed-corpus.md)
  - [2026-08-10-spec-aMendedLedger-8-u9-driver-redesign.md](spec/units/2026-08-10-spec-aMendedLedger-8-u9-driver-redesign.md)
- **`build/`**
  - [2026-08-10-build-TOOL-aMendedLedger-1-1-driver-repro-corpus.md](build/2026-08-10-build-TOOL-aMendedLedger-1-1-driver-repro-corpus.md)
- **`reviews/`**
  - [2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md](reviews/2026-08-09-review-TOOL-aMendedLedger-1-1-closing-diff.md)
  - [2026-08-09-review-TOOL-aMendedLedger-1-2-repair.md](reviews/2026-08-09-review-TOOL-aMendedLedger-1-2-repair.md)
  - [2026-08-09-review-TOOL-aMendedLedger-1-3-regression.md](reviews/2026-08-09-review-TOOL-aMendedLedger-1-3-regression.md)
  - [2026-08-10-review-TOOL-aMendedLedger-1-4-u9-redesign.md](reviews/2026-08-10-review-TOOL-aMendedLedger-1-4-u9-redesign.md)
<!-- /gen:build-docs -->
