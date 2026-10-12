# Acceptance ledger — the A/B instrument reads the verdict by key, and the rule check proves arms from bar rows

**Serves:** journal TOOL-aPairedSlots-12

Observed on node a on 2026-10-12 by one script run twice: over copies of the instrument and the rule
check as they stood before this unit, then over the changed files. It sources the instrument's
functions and runs `measure_bar` over a fixture root, then runs the rule check over the committed rows
and over a copy whose A1 bar rows carry proof `NO`.

**Evidences:** TOOL-aPairedSlots-12
- AC1 — `measure_bar` — over a run record whose verdict file opens with an `ended` line, the changed
  instrument appended a sixteen-field row whose verdict column read `RED`; the previous one appended
  seventeen fields with `ended` in the verdict column and the expected-leg count in the proof column.
- AC2 — `2026-10-11-build-TOOL-aPairedSlots-9-rule-check.py` — over the committed rows both checkers
  printed AGREE. Over the copy with A1's bar proofs set to `NO`, the changed checker refused to decide,
  exit 2, naming A1 unproven; the previous one printed AGREE.
