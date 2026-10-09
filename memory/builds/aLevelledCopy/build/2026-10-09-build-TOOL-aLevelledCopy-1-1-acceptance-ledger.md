# TOOL-aLevelledCopy-1 — acceptance ledger

**Serves:** journal TOOL-aLevelledCopy-1

No merge bar and no self-test suite ran in this pass. The criteria were observed with the leg's own
`--selftest` flag and with fixture repositories that a scratchpad script built under a short
`%TEMP%\lcfx` directory, on node a. `--selftest` printed 10 of 10 arms ok in 7.1 s wall. Each new
arm was then observed RED in a scratch copy of the file with its predicate broken. The CR-stripped
sha256 redded arm (c), dropping the raw-blob clause redded arm (d), and dropping the clean-filter
branch redded arm (a). Each of those copies exited 1, and the unbroken file is green again. The
copy read with `git show` at base `ce9192c0` redded the AC1 fixture. The close still owes the
`receipt sync (installed files match the receipt)` leg, `run-gates adopter e2e`, the lexicon leg
and memory hygiene.

**Evidences:** TOOL-aLevelledCopy-1
- AC1 — `eol-only 1` — on the one-row fixture the base copy printed `DRIFTED   f.txt` and exited 1.
  The new file printed `ok  1 engine row(s) match the receipt · eol-only 1` and exited 0. The
  fixture script asserted a CR byte in the working copy before grading.
- AC2 — `DRIFTED` — with one byte of the CRLF copy changed, the row printed `DRIFTED` and the file
  exited 1, with `eol-only 0`.
- AC3 — `--selftest` — it printed `ARM ok` for arms (a) to (d) and `fixtures: 10/10 arm(s) ok`, and
  exited 0. Each git arm asserts `graded == 1`.
- AC4 — `ARM FAIL` — the three staged breaks printed `ARM FAIL` for arms (c), (d) and (a)
  respectively, each with `fixtures: 9/10`, and each exited 1.
- AC5 — amended rev-2 — the trace goes to `GIT_TRACE=<file>`, because the leg captures git's stderr
  and `GIT_TRACE=1` showed nothing. Observed: 4 `hash-object --stdin-paths` lines over the
  all-matching receipt, all from the arms, and 5 over the three-eol-only receipt.
- AC6 — `oid` — with the row's `oid` key removed, the row printed `DRIFTED` and the file exited 1.
- AC7 — `DRIFTED` — the fixture copied without `.git` printed a `GIT` line naming `hash-object`
  as not consulted because the tree holds no `.git`, then `DRIFTED`, and exited 1. With `PATH`
  holding only Python's directory, `--selftest` printed `ARM FAIL` for all four git arms naming
  `[WinError 2]` from git, and exited 1. The live path with git absent printed a `GIT` line saying
  git could not start, then `DRIFTED`.
- AC8 — `grep -c "true reading" tools/run-gates/check-receipt.py` — it printed 0. The rewritten
  bullet names the target's own clean filter.
