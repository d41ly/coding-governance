# TOOL-aSightedSkeptic-5 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-5

The diff review now runs five lenses, security, correctness, seams, verification and intent, with
`regressions` retired. `args.lensNotes` appends a project note to one lens, `REVIEW_SHAPE` and
`lensNotes` join the key, and the harness moved to 1.17. The arm readings come from the main loop's
one VERIFYING run of the tier2-review self-test at 149e89d6 (165 passed, 0 failed) and from the same
test file run against the BASE render at 9fdd0c18 in a frozen clone (56 passed, 109 failed). The
greps and the direct checks were re-run on the build's tip, whose `tools/` is byte-identical to
149e89d6.

**Evidences:** TOOL-aSightedSkeptic-5
- AC1 — `the diff lens set is security correctness seams verification intent` — `ok` at VERIFYING,
  naming the five `find:` labels in order; against the BASE render it printed `FAIL` naming four
  labels ending in `find:regressions`. The `sed` cut of `DIFF_LENSES` through `grep -oE` printed
  `key: 'security'`, `key: 'correctness'`, `key: 'seams'`, `key: 'verification'` and
  `key: 'intent'`, in that order and nothing else.
- AC2 — `client/server|loading|auth/RBAC|SSRF|regressions` — the `grep -ciE` over the `DIFF_LENSES`
  cut printed 0. Over `git show 9fdd0c18:` of the template it printed 3, and 3 at ef1dcdb6.
- AC3 — `a lensNotes entry reaches its own lens prompt and no other` — both halves printed `ok`:
  "find:verification carries the note" and "the other four find: and every verify: prompt do not".
  Both printed `FAIL` against the BASE render.
- AC4 — `a malformed lensNotes refuses before any agent spawns` — all six cases printed `ok` at
  VERIFYING: a string, an array, null, the retired key on a diff review, a diff key on a spec audit
  and an empty note, and the control "a spec-kind key on a spec audit, proceeds" printed `ok`.
  Against the BASE render the six printed `FAIL` with "(accepted)", while the control printed `ok`.
- AC5 — `absent lensNotes is announced in the log and in RUN INTEGRITY` — both halves printed `ok`,
  the second "a supplied note logs no warning and is named there". Both printed `FAIL` against the
  BASE render.
- AC6 — `a lens file written under another review shape is dispatched` — its three halves printed
  `ok`: "the rewrite took and the keys differ", "find:security under the older shape is dispatched"
  and "...and one under the real key is reused". Against the BASE render the first two printed
  `FAIL`. The variant "AC3 another lensNotes" printed `ok` both ways at VERIFYING, and its dispatch
  half printed `FAIL` against BASE.
- AC7 — `grep -c "regressions" tools/workflows/tier2-review.test.sh` — printed 0, and over the file
  at 9fdd0c18 and at ef1dcdb6 it printed 6. The VERIFYING summary read `PASS (165 assertions)`
  against `FLOOR_ASSERTIONS=165`; this unit's own raise was 60 to 77, stated in 3b094694's
  `Decided:` trailer and read back with `git show` at that commit. The arm
  `the args header documents all` printed `ok` over 14 fields, and the header carries `lensNotes:`
  at line 84 of the template.
- AC8 — `bash tools/workflows/check-verifier-fanout.sh` — exited 0, "clean — 6 workflow script(s)
  obey the ≤5-verifier rule". `check-review-join.sh` and `check-workflow-syntax.js` each exited 0,
  the latter "6 workflow script(s) parsed clean".
- AC9 — `bash tools/check-kit-versions.sh` — exited 0. The `grep -c` of the 1.17 version line
  printed 1 for `tools/workflows/tier2-review.template.js` and 1 for `tools/workflows/tier2-review.js`.
- AC10 — `sed "s/{{FANOUT_CAP}}/5/g" tools/workflows/tier2-review.template.js | diff - tools/workflows/tier2-review.js`
  — printed nothing, 0 lines, after `check-verifier-fanout.sh --print-cap` printed 5.
- AC11 — `four finder lenses` — `grep -c` printed 0 for `README.md` and 0 for
  `WIRE-INTO-PROJECT.md`, `4 finder lenses` counted 0 over the template, and `lensNotes` counted 4
  over `tools/workflows/README.md`. At 9fdd0c18 the same four greps printed 1, 1, 1 and 0.
