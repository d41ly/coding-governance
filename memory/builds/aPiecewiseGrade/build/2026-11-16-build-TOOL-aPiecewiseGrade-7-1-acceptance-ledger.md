# TOOL-aPiecewiseGrade-7 — acceptance ledger

**Serves:** journal TOOL-aPiecewiseGrade-7

No merge bar, no self-test suite and no gate ran in this pass. AC1 was observed by the spec's pass
probe, `pg7.sh` in the run's scratch, removed after the pass, run against the shipped
`tools/unattended/unattended.sh` at base `b6ae97134`. AC2 and AC3 were observed by running the
commands they spell over the built suite. `bash -n` over the suite parsed it clean.

**Evidences:** TOOL-aPiecewiseGrade-7
- AC1 — `foreign held cut stale` — printed as written: the kept predicate reads the foreign
  runtime's dead pid live, and the copy with `[ "$w" = "${HOSTNAME:-}:${OSTYPE:-}" ] && ` cut by
  `sed` reads it gone.
- AC2 — the `sed -n '/# AC13: /,/each hold the lock/{p;/each hold the lock/q;}'` range printed the
  AC13 loop alone, 18 lines (DERIVED, wc -l over the built suite at this pass), holding exactly one
  line opening `foreign)`, carrying `printf` and `otherhost:otheros` and not `write_pg6_pid`, and its
  last line ends `foreign:1:w-x"`.
- AC3 — `git diff -U0 3300b594c -- tools/unattended/unattended.test.sh | grep -cE '^[-+] *(hit|miss|same) '`
  printed 2, and the same diff piped to `grep -cE '^[-+]FLOOR_'` printed 0.

Owed to the main loop at the close. These were written and not run:
- New arm, the `foreign` kind in the AC13 loop of the TOOL-aPiecewiseGrade-6 block of
  `tools/unattended/unattended.test.sh`, expected `foreign:1:w-x`: RED on deleting
  `[ "$w" = "${HOSTNAME:-}:${OSTYPE:-}" ] && ` from `check_dir_lock_stale` in
  `tools/unattended/unattended.sh`, which turns the entry into `foreign:0:`; GREEN once restored.
- The suite's executed assertion count is unchanged, the kind joining the loop's one `same`, so no
  floor moves; the close confirms it.
- The legs section 6 names.
