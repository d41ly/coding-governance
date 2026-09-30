**Serves:** journal TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-46

# aRepatriatedFork: the round-2 closing diff review, disposed

*Node `a`, 2026-09-30. The disposition of `reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round2.md`
(verdict CLEAN WITH FIXES, CONVERGED), over round 2's recorded tip `ce8a78f5`. BUILD-METHOD M4
disposes each confirmed item by severity and re-arms no round. Each LOW was folded into the spec of
the unit whose line it names, found with `git log -S`, as a rev bump committed before the code. Each
fix was reproduced RED on `ce8a78f5`'s bytes first. No suite ran whole: each arm ran as a slice, the
suite's prologue plus the changed block, in a temp script beside the suite, removed after.*

## Per item

| Item | Severity | Disposition | Owner | Red first | Regression arm |
|---|---|---|---|---|---|
| H1 | HIGH | PROMOTED to `TOOL-aRepatriatedFork-49`, specced and built | new unit | its own acceptance ledger | its own acceptance ledger |
| L1 | LOW | FOLDED, spec rev-4, S8 | `TOOL-aRepatriatedFork-46` (`0a79f19b`) | both gates threw MODULE_NOT_FOUND with `GIT_DIR` exported | one arm in each fan-out gate's suite |

## Beside the items

- **The class is wider than the two gates.** `git grep 'git -C "$HERE" rev-parse --show-toplevel'`
  finds the same second question in the adopters of drift-audit and process-monitor, in
  `tools/run-gates/run-selftests.sh`, `tools/unattended/run-unattended-gates.sh` and
  `tools/unattended/resume-tick.sh`. The two tracked hooks unset `GIT_DIR`, so no bar boundary
  reaches them. They are not folded here, because the review named the two gates and a LOW's fold is
  bounded by its item.
- **review-harness moves 1.22 to 1.23** in both carriers, because the two gates are its shipped bytes.

**Evidences:** TOOL-aRepatriatedFork-46
- AC14 — `GIT_DIR` — `check-review-join.sh` run from a scratch checkout with `GIT_DIR` exported to that checkout's git dir reads `review-join: clean`, and `check-verifier-fanout.sh --print-cap` prints `5`. Red first: both threw MODULE_NOT_FOUND on the `ce8a78f5` gates, and both slice arms failed there
