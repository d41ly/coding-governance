# Acceptance ledger — TOOL-aClearedLedger-2

**Serves:** journal TOOL-aClearedLedger-2

Built against spec rev-1 in this record's own commit, from base a548d0cec.
The template and its render were each edited by hand with the same replacement, the one the spec's section 4 spells; the pair holds no placeholder, and the adopter was not run.
Each line is a probe the builder made in the pass. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section. The spec declares no new arm.

**Evidences:** TOOL-aClearedLedger-2
- AC1 — `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` — printed nothing and exited 0, and the grep for the reason's clause printed 1 over each file, at line 727 of each, between the headings `## 12.` and `## 13.`.
- AC2 — `git diff --numstat 8db6f4be -- tools/unattended/PROTOCOL.template.md` — printed one row, three lines added and two removed, and the grep for the paragraph's opening over the template printed 1. (PINNED, 2026-11-13)
- AC3 — `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md | wc -c` — printed 68092, the second field of the render's row in the limits file; the grep for `RAISED 68022 -> ` printed 1, on a line naming this unit; and the `git log` over the decisions file named a548d0cec, the base this pass's commit sits on. (PINNED, 2026-11-13)
