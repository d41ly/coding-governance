# aTrimmedHook — asks

## Asks
- TOOL-aTrimmedHook-8 · filed 2026-10-11 · after this build a one-file `RUN.md` commit's `.githooks/pre-commit` still costs 51-81 s on node a at 31-61 host bash processes, against the owner's 30 s target: the hygiene leg is about 20 s and the manifest leg about 8 s, and about 28 s is the hook's own plumbing, measured by an `EPOCHREALTIME` trace — the straggler guard, the install-receipt `awk` in `resolve_kit_gate`, and one `git diff --cached | grep -q` probe per guarded leg. Not adopted under protocol §11: no cheaper mechanism was built and measured, and the hook carries govkit-emitted regions and the backlog-relocation guard · seen `.githooks/pre-commit`@b1b5ad68:104 · accept the staged name list is read once and every guarded leg's trigger is a shell match against it, the straggler guard and the receipt read cost no process on a commit that cannot need them, and a one-file `RUN.md` commit's pre-commit measures under 30 s on node a with the bash count beside it
- TOOL-aTrimmedHook-17 · filed 2026-10-12 · held red: suite process-monitor census selftest red at 37200355 on the daily held job, run 38247412830 · seen `{prefix}/process-monitor/selftest.py`@37200355 run `python {prefix}/process-monitor/selftest.py` · accept the suite is green on the daily held job at the default branch's tip

## Dispositions
- SEV · TOOL-aTrimmedHook-8 · MED · wall clock on every commit, no verdict wrong; the push boundary is unaffected
- KEEP · TOOL-aTrimmedHook-8 · filed by this run under protocol section 11; the hook plumbing is outside this build's four owner items
- SEV · TOOL-aTrimmedHook-17 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aTrimmedHook-17 · filed by an unattended run for the owning build; outside this build's goal
