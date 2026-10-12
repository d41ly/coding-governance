# TOOL-aOrientedCast-12 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-12

Direct checks only: under the owner's rule for this run no gate, suite, slice or self-test ran in
this pass. What ran: the spec's §4 probe, which sources `read_population` out of the runner into a
scratch shell and calls it over a scratch budgets file and over the real declaration; the same
probe against the parent's reader (`git show HEAD:tools/run-gates/run-selftests.sh`) as the RED;
the AC1 `awk` and `grep` lines; the AC4 `grep` lines; and `bash -n` over the runner and its suite.
RED first, for the reader: the parent's reader printed `ok` for the three-field row, `ok` for the
prose-argv row and `ok` for the manifest-backed row; the pass's reader printed `BADROW`, `BADARGV`
and `ok` with the manifest's argv. Owed to the main loop at the close (M8): the two `New arm:`
lines of §6, which are the three arms this pass added to `run-selftests.test.sh` under the
`run-selftests self-test` leg, each RED on its staged break and GREEN restored (`SELFTEST_FLOOR`
moved 141 to 144 by a hand count, not a run); `--check`'s two new refusal branches, which only the
runner exercises; and every leg §6 lists, with `bash tools/check-kit-versions.sh` and the kit epoch
check for the run-gates bump.

**Evidences:** TOOL-aOrientedCast-12
- AC1 — `roles render selftest` — the `awk -F'\t'` field-count line printed nothing over `tools/run-gates/selftest-budgets.txt`, and `grep -c '^roles render selftest'` printed 1.
- AC2 — `measured 1s` — over a scratch file holding a three-field row, a four-field row whose argv is `measured 1s`, the `agent-cap self-test` row with an empty argv and a one-field row, the probe printed `BADROW`, `BADARGV`, `ok` with `bash tools/hooks/agent-cap.test.sh`, and `BADROW`; over the real declaration it printed `ok` on all 94 lines. The scratch file was written by the pass and deleted after it.
- AC3 — owed to the main loop — the `run-selftests self-test` leg: the three new arms of `tools/run-gates/run-selftests.test.sh`, `--check` naming a three-field row and a prose-argv row, and `--serial` refusing the three-field row as `BADROW`, each observed RED against a reader with the field-count or launcher test staged out and GREEN restored.
- AC4 — `KIT_RUN_GATES_VERSION=1.36` — `grep -n 'run-gates@1.36'` printed line 32 of the runner, which sets `KIT_RUN_GATES_VERSION=1.36`, and line 3 of the kit README; `grep -c 'run-gates@1.35'` printed 0 for each. `bash tools/check-kit-versions.sh` and the kit epoch check are owed to the main loop.
