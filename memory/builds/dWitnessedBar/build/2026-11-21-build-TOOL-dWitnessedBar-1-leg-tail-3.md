# TOOL-dWitnessedBar-1 leg-tail 3 — shell hygiene (a fork spent on builtin work) failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** shell hygiene (a fork spent on builtin work)
- **Hash:** c5501681a1bf3715f4b85ecc794ebccc4fcc2050
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** f9ee3f8e0f2e994c7bad52ae0779fcf31c9c94db
- **Cause:** run:dWitnessedBar

```
sh-hygiene: registered — tools/unattended/unattended.sh: `path-subst` × 12
sh-hygiene: registered — tools/unattended/unattended.sh: `printf-subst` × 7
sh-hygiene: registered — tools/unattended/unattended.sh: `pure-fn-subst` × 44
sh-hygiene: registered — tools/unattended/unattended.sh: `var-pipe` × 62
sh-hygiene: registered — tools/unattended/unattended.test.sh: `cat-file` × 17
sh-hygiene: registered — tools/unattended/unattended.test.sh: `date-fmt` × 2
sh-hygiene: registered — tools/unattended/unattended.test.sh: `path-subst` × 13
sh-hygiene: registered — tools/unattended/unattended.test.sh: `printf-subst` × 23
sh-hygiene: registered — tools/unattended/unattended.test.sh: `var-pipe` × 19
sh-hygiene: registered — tools/workflows/check-protocol-parity.test.sh: `path-subst` × 5
sh-hygiene: registered — tools/workflows/check-protocol-parity.test.sh: `var-pipe` × 2
sh-hygiene: registered — tools/workflows/check-review-join.sh: `path-subst` × 1
sh-hygiene: registered — tools/workflows/check-review-join.sh: `var-pipe` × 4
sh-hygiene: registered — tools/workflows/check-review-join.test.sh: `path-subst` × 4
sh-hygiene: registered — tools/workflows/check-review-join.test.sh: `var-pipe` × 1
sh-hygiene: registered — tools/workflows/check-verifier-fanout.sh: `path-subst` × 1
sh-hygiene: registered — tools/workflows/check-verifier-fanout.sh: `var-pipe` × 1
sh-hygiene: registered — tools/workflows/check-verifier-fanout.test.sh: `path-subst` × 5
sh-hygiene: registered — tools/workflows/check-verifier-fanout.test.sh: `var-pipe` × 1
sh-hygiene: registered — tools/workflows/tier2-review.test.sh: `path-subst` × 4
sh-hygiene: registered — tools/workflows/tier2-review.test.sh: `var-pipe` × 1
sh-hygiene: registered — tools/workflows/unattended-build.test.sh: `cat-file` × 1
sh-hygiene: registered — tools/workflows/unattended-build.test.sh: `path-subst` × 6
sh-hygiene: registered — tools/workflows/unattended-build.test.sh: `printf-subst` × 83
sh-hygiene: registered — tools/workflows/unattended-build.test.sh: `pure-fn-subst` × 36
sh-hygiene: registered — tools/workflows/unattended-build.test.sh: `var-pipe` × 64
sh-hygiene: 33 finding(s). Each idiom below forks a process for work bash does in-process, at 89 to 315 ms a fork under MSYS.
  .githooks/pre-commit.test.sh: the registry declares `printf-subst` and the scan no longer finds it — delete the row, or a drained site leaves a widened exemption behind
  .githooks/pre-commit.test.sh: the registry declares 6 site(s) at `var-pipe` and the scan measures 2 — the count may fall with the sites and may not rise
  .githooks/pre-push: the registry declares `date-fmt` and the scan no longer finds it — delete the row, or a drained site leaves a widened exemption behind
  .githooks/pre-push: the registry declares 10 site(s) at `pure-fn-subst` and the scan measures 18 — the count may fall with the sites and may not rise
  .githooks/pre-push: the registry declares 9 site(s) at `var-pipe` and the scan measures 10 — the count may fall with the sites and may not rise
  .githooks/pre-push.runlog.test.sh: the registry declares 16 site(s) at `var-pipe` and the scan measures 17 — the count may fall with the sites and may not rise
  .githooks/pre-push.test.sh: the registry declares 17 site(s) at `cat-file` and the scan measures 20 — the count may fall with the sites and may not rise
  tools/codebase-map/adopt-codebase-map.test.sh: the registry declares 4 site(s) at `path-subst` and the scan measures 7 — the count may fall with the sites and may not rise
  tools/codebase-map/adopt-codebase-map.test.sh: the registry declares 10 site(s) at `var-pipe` and the scan measures 16 — the count may fall with the sites and may not rise
  tools/drift-audit/adopt-drift-audit.sh: 1 `var-pipe` site(s) and no registry row declares them — convert each to the no-fork form, or declare the row with its reason
  tools/gate-lint/fork-count.sh: 1 `path-subst` site(s) and no registry row declares them — convert each to the no-fork form, or declare the row with its reason
  tools/lib/refuse-wrong-shell.sh: 1 `path-subst` site(s) and no registry row declares them — convert each to the no-fork form, or declare the row with its reason
  tools/lib/refuse-wrong-shell.sh: 2 `var-pipe` site(s) and no registry row declares them — convert each to the no-fork form, or declare the row with its reason
  tools/lib/resolve-python.test.sh: the registry declares 4 site(s) at `path-subst` and the scan measures 5 — the count may fall with the sites and may not rise
  tools/lib/resolve-python.test.sh: 1 `pure-fn-subst` site(s) and no registry row declares them — convert each to the no-fork form, or declare the row with its reason
  tools/lib/resolve-python.test.sh: the registry declares 8 site(s) at `var-pipe` and the scan measures 16 — the count may fall with the sites and may not rise
  tools/memory-tree/check-memory-hygiene.sh: the registry declares 25 site(s) at `var-pipe` and the scan measures 28 — the count may fall with the sites and may not rise
  tools/memory-tree/check-memory-hygiene.test.sh: the registry declares 19 site(s) at `printf-subst` and the scan measures 16 — the count may fall with the sites and may not rise
  tools/memory-tree/check-memory-hygiene.test.sh: the registry declares 60 site(s) at `var-pipe` and the scan measures 80 — the count may fall with the sites and may not rise
  tools/run-gates/adopt-run-gates.test.sh: the registry declares 8 site(s) at `var-pipe` and the scan measures 14 — the count may fall with the sites and may not rise
  tools/run-gates/post-merge.sh: the registry declares 2 site(s) at `date-fmt` and the scan measures 1 — the count may fall with the sites and may not rise
  tools/run-gates/profile_bar.test.sh: 3 `var-pipe` site(s) and no registry row declares them — convert each to the no-fork form, or declare the row with its reason
  tools/run-gates/run-gates.evidence.test.sh: the registry declares 13 site(s) at `cat-file` and the scan measures 15 — the count may fall with the sites and may not rise
  tools/run-gates/run-gates.evidence.test.sh: the registry declares 72 site(s) at `var-pipe` and the scan measures 78 — the count may fall with the sites and may not rise
  tools/run-gates/run-gates.gov.test.sh: 18 `var-pipe` site(s) and no registry row declares them — convert each to the no-fork form, or declare the row with its reason
  tools/run-gates/run-gates.sh: the registry declares 10 site(s) at `date-fmt` and the scan measures 11 — the count may fall with the sites and may not rise
  tools/run-gates/run-gates.sh: the registry declares 7 site(s) at `pure-fn-subst` and the scan measures 8 — the count may fall with the sites and may not rise
  tools/run-gates/run-gates.test.sh: the registry declares 25 site(s) at `cat-file` and the scan measures 27 — the count may fall with the sites and may not rise
  tools/run-gates/run-gates.test.sh: the registry declares 156 site(s) at `var-pipe` and the scan measures 161 — the count may fall with the sites and may not rise
  tools/unattended/lib-unattended.sh: the registry declares 5 site(s) at `path-subst` and the scan measures 6 — the count may fall with the sites and may not rise
  tools/unattended/unattended.sh: the registry declares 8 site(s) at `date-fmt` and the scan measures 7 — the count may fall with the sites and may not rise
  tools/unattended/unattended.sh: the registry declares 44 site(s) at `pure-fn-subst` and the scan measures 43 — the count may fall with the sites and may not rise
  tools/unattended/unattended.sh: the registry declares 62 site(s) at `var-pipe` and the scan measures 63 — the count may fall with the sites and may not rise
```
