**Serves:** journal TOOL-dSafePassage-51 TOOL-dSafePassage-59

# TOOL-dSafePassage-51 AC1 — the build run's commit-order check

TOOL-dSafePassage-51 AC1 grades the order of this build run's pass commits, which no write of
TOOL-dSafePassage-51's pass can move, so it is a check of the build run and not of that pass
(TOOL-dSafePassage-59 S1). Its line sits here, in a record committed with `Pass: none`, and left
TOOL-dSafePassage-51's own ledger. The probe is spelled whole-line (TOOL-dSafePassage-59 S3), since
`TOOL-dSafePassage-4` is a prefix of `TOOL-dSafePassage-43` to `-49`. The guard holding the order at
dispatch is `tools/unattended/unattended.sh`'s TOOL-dTrueNorth-16 S2 edge refusal
(TOOL-dSafePassage-59 S2). Observed on node d, 2026-10-28, at HEAD `36bc5d25e`.

**Evidences:** TOOL-dSafePassage-51
- AC1 — `git log --reverse --format='%(trailers:key=Pass,valueonly)' <BASE>..HEAD` — over `60d90cb71db51e651aa1c5efe3f6d48ba21a997d..HEAD`, empty lines dropped, `grep -n -x -m1` put the first line reading `TOOL-dSafePassage-43` at 10, `TOOL-dSafePassage-7` at 12, `TOOL-dSafePassage-4` at 17, `TOOL-dSafePassage-18` at 21 and `TOOL-dSafePassage-19` at 22.

**Evidences:** TOOL-dSafePassage-59
- AC1 — `git grep -n -A6 '^\*\*Evidences:\*\* TOOL-dSafePassage-51' -- memory/builds/dSafePassage/` — run over this record's commit, which carries `Pass: none`, it shows two blocks: this record's, holding the `AC1` line, and TOOL-dSafePassage-51's ledger's, opening at `AC3` and holding no `AC1`.
