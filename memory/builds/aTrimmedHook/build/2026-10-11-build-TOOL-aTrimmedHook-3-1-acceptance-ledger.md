# TOOL-aTrimmedHook-3 — acceptance ledger

**Serves:** journal TOOL-aTrimmedHook-3

No merge bar and no self-test suite ran in this pass. AC1 and AC2 were observed in a scratch repository
under a short `%TEMP%` root on branch `work`, holding a stub `tools/unattended/unattended.sh` that
writes a marker file, an empty `.unattended.conf` and a tracked run-state file. The pre-unit hook,
run the same way with no run-state file naming the branch, wrote the marker: it started the driver
on every commit, which is the cost this unit removes.

**Evidences:** TOOL-aTrimmedHook-3
- AC1 — `bash .githooks/commit-msg <msg>` — with no tracked run-state file naming the branch, the
  marker was not written.
- AC2 — `run-branch: refs/heads/<its branch>` — with that line committed in the run-state file, the
  marker was written; with the pre-filter's `grep` pattern broken to `": NOPE$un_ref"`, it was not,
  which is the arm observed RED.
- AC3 — `grep -in 'first narrowing' .githooks/commit-msg` — printed the header line the unit adds.
