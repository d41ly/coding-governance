# Acceptance ledger — the two-bar check reads the verdict by key and grades rows at their width

**Serves:** journal TOOL-aPairedSlots-13

Observed on node a on 2026-10-12. A script sources the changed check and feeds `check_rows` fixture
`check.tsv` files; the predicate it replaces, copied from the check as it stood, read the same files.

**Evidences:** TOOL-aPairedSlots-13
- AC1 — `check_rows` — over three eleven-field rows of the earlier copy's layout, two whole and one
  whose ledger kept 40 rows for 65 legs, it named only the short row, exit 1, and a whole ten-field row
  passed with exit 0. The replaced predicate named all three rows lost or torn.
- AC2 — `check_rows` — a nine-field row was named `row malformed (9 fields)`, exit 1. The replaced
  predicate graded it with its columns out of place and named it lost or torn.
