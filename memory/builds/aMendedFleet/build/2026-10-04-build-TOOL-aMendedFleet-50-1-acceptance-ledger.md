# TOOL-aMendedFleet-50 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-50

**Evidences:** TOOL-aMendedFleet-50
- AC1 — `python tools/drift-audit/drift_report.py --escape-ratio 2026-09` — on node a against `refs/remotes/origin/main` @ c3ef6742, about 25 s: n 169, escaped 105, ratio 0.621 with the Wilson interval 0.546 to 0.691, direct 5 of 169, unclassified addition-only 6 and stamp-only 9, then the caveat line; `--json` reported `n` 169 and exactly 169 `fixes` entries whose `class` is `escaped` or `contained`. The figure differs from the review's unverified 116 of 297, which was two months and an uncommitted script
- AC2 — `git merge-base --is-ancestor` — run over EVERY entry of that `--json`, not one of each: every `blamed_landings` commit is an ancestor of its fix's landing, every escaped entry names a landing that is an ancestor of its landing's first parent, every contained entry names only its own landing, and every `direct` entry is its own `landing` and a single-parent commit; zero violations across 169 classified fixes
- AC3 — `check_stamp_line` — `python -c` importing `drift_report` from `tools/drift-audit`: true for the `gov:kit drift-audit@1.22` marker, the `KIT_DRIFT_AUDIT_VERSION = "1.22"` line, the `version = "1.0"` line and a `last-audit:` line, false for `x = compute(1)`. Staged red: with the function returning false, all five read false
- AC4 — `derive_wilson_interval` — 116 and 297 rounded to 0.3368 and 0.4471, 0 and 5 to 0.0 and 0.4345, 0 and 0 returned None. Staged red: with the normal approximation's centre, 116 of 297 gave 0.3351 to 0.4461 and 0 of 5 gave 0.0 to 0.0
- AC5 — `python tools/drift-audit/drift_report.py --escape-ratio 2026-9` — exited 2 naming the YYYY-MM shape; `--escape-ratio 2026-09 --check` exited 2 naming `--check`, and `--delta HEAD HEAD` beside it exited 2 naming `--delta`; `grep -c -- "--escape-ratio" tools/drift-audit/README.md` printed 3

## The arm

`test_escape_ratio` in `tools/drift-audit/selftest.py`, nine checks over a `make_repo` fixture whose
arm commits are dated into 2026-03: a merge-landed contained fix, a merge-landed escaped fix, a
direct fix, a stamp-only fix and a fix touching no product path, plus the text form, an empty month,
a malformed month and a `--check` beside the mode. Run ALONE through a scratchpad slice calling it,
fixture under `%TEMP%`: nine `ok`. Staged red three times and restored: with the landing comparison
replaced by false, the n, escaped and direct checks FAILED; with the stamp filter off, the n, direct
and stamp-only checks FAILED; with the caveat line dropped, the text-form check FAILED.
`CHECK_FLOOR` 318 -> 327. The suite did not run.

## Owed at the close

- `drift-audit selftest`, `drift-audit records`, `drift-audit wiring`, `codebase-map coverage +
  freshness`, `recall floor`, `recall floor arms`, `lexicon naming predicates` and `spec tokens`.
- The drift-audit kit version bump, per the brief; `kit epoch` is the close's.
