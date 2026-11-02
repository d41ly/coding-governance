# TOOL-dFoldedAudit-8 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-8

The spec writer observed AC1 to AC5 over this pass's tree, with no gate, suite or bar, and its return is recorded at `build/2026-11-02-build-TOOL-dFoldedAudit-8-3-pass-return.md`. AC6 and AC7 each hold a clause only this commit can answer, so the close re-reads those clauses after it.

**Evidences:** TOOL-dFoldedAudit-8

- AC1 — `grep -m1 '^\*\*Status:'` over the three specs read rev-3, rev-3 and rev-4; `grep -c 'TOOL-dFoldedAudit-8'` printed 2, 1 and 1, and each §9 holds its new rev line.
- AC2 — `derive_clause_hash` over the record's After line gave `afb50a20`, equal to DL-32's `**Carries:**` pin, and `grep -c 'cl-dClosedLoop-0117@166df103'` printed 0.
- AC3 — `grep -c 'no-fall'` over DL-32 printed 6 and `grep -c 'passes it for every subject'` printed 0.
- AC4 — `grep -c 'built work or for a new mechanism'` over DL-20 printed 1 and `grep -c 'BUILD-METHOD.md:144'` printed 1.
- AC5 — `grep -c "floor's chain rule"` over FH-17 printed 0 and `grep -c 'derived verdict'` printed 2.
- AC6 — `deviation_join.read_record` over the record gave empty `malformed`, and `grep -c 'promote only findings that need new mechanisms'` printed 1. The `git log --format=%H -1` read over the view and the record is owed to the close.
- AC7 — `bash tools/unattended/unattended.sh --claims` read dDeclaredLoop and dFairHearing `landed` before and after the writes; `git diff --name-only 74274869 HEAD -- memory/builds/dSafePassage` is re-read at the close.
