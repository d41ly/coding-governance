# TOOL-aQuotedBrief-5 — acceptance ledger

**Serves:** journal TOOL-aQuotedBrief-5

Node a, 2026-10-09. No suite and no bar ran in this pass. The two new arms in `unattended.test.sh`'s
region three were run as SLICES: the suite's prologue, the definitions each arm uses and the arm, in
temp scripts under the kit directory, deleted before the commit. Against this pass's driver the AC1
slice printed `n=24 st=0` and the AC2 slice `n=27 st=0`, each counting the prologue's 20. Against the
pre-pass driver (the HEAD blob) the AC1 slice printed 2 FAIL lines and the AC2 slice 2.

**Evidences:** TOOL-aQuotedBrief-5
- AC1 — `--preflight tBr` over a build whose only record is headed `##  The prompt`, otherwise conforming, printed `UNATTENDED check 113 FAILED` and no `preflight OK` (slice; red on the pre-pass driver, which graded the record and admitted the build)
- AC2 — `--close tRun` over the build-complete fixture with a second record headed `##  The prompt` whose one item is `planned` for the unbuilt `ARCH-tRun-9` printed `close OK` with no term 7 refusal, after its `--preflight` printed `preflight OK`: both readers skip that record (slice; red on the pre-pass driver, whose preflight graded it and refused at check 115, rule 2, while term 7 skipped it)
- AC3 — `git diff 6473ae38 -- tools/unattended/unattended.sh` names `read_audit_ask_record` only in context lines and in the new predicate's comment, and the function's body extracted at `6473ae38` and at the working tree compared equal
