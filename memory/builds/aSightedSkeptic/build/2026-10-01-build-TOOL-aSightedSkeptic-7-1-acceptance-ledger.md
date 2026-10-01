# TOOL-aSightedSkeptic-7 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-7

`args.intensity` is `full` or `light`. A light diff review runs only `LIGHT_LENSES`, counts a
skipped lens as neither live nor dead, splits the checklist over the running lenses, and announces
what it skipped in the log and in RUN INTEGRITY. The arm readings come from the main loop's one
VERIFYING run of the tier2-review self-test at 149e89d6 (165 passed, 0 failed) and from the same
test file run against the BASE render at 9fdd0c18 in a frozen clone (56 passed, 109 failed). The
greps and the direct checks were re-run on the build's tip, whose `tools/` is byte-identical to
149e89d6.

**Evidences:** TOOL-aSightedSkeptic-7
- AC1 — `intensity: an unknown value is refused` — the six prelude arms printed `ok` at VERIFYING:
  "medium" and 7 threw messages naming `intensity`, light on a diff review resolved "light", an
  absent value resolved "full", light on a spec audit threw, and full on a spec audit resolved
  "full". Against the BASE render all six printed `HARNESS-BROKEN ... intensity is not defined`.
- AC2 — `intensity: light dispatches only the light lenses` — `ok` at VERIFYING, naming
  `find:correctness find:seams find:verification`. Against the BASE render it printed `FAIL` naming
  four labels, `find:security` and `find:regressions` among them.
- AC3 — `intensity: a skipped lens is neither live nor dead` — both halves printed `ok`: "a light run
  completes, three lenses in its agent count" and "three running lenses dead defer, pending only
  those three". Both printed `FAIL` against the BASE render.
- AC4 — `intensity: a light run announces its skipped lenses` — both halves printed `ok`: "in the log
  and RUN INTEGRITY" and "a full run names intensity full and no skipped lens". Both printed `FAIL`
  against the BASE render.
- AC5 — `intensity: LIGHT_LENSES must name live lenses` — both halves printed `ok`: "a renamed key,
  diff review" and "an empty literal, spec audit". Against the BASE render both printed `FAIL` with
  "(accepted)".
- AC6 — `intensity: every checklist item reaches a running lens` — `ok` at VERIFYING, `FAIL` against
  the BASE render.
- AC7 — `intensity: the key differs by intensity` — `ok` at VERIFYING, `FAIL` against the BASE
  render.
- AC8 — `node tools/workflows/check-workflow-syntax.js` — exited 0 with "6 workflow script(s) parsed
  clean", and `bash tools/workflows/check-verifier-fanout.sh` exited 0. The render diff, `sed` of the
  cap 5 over the template piped into `diff` against `tools/workflows/tier2-review.js`, printed 0
  lines.
- AC9 — `grep -c 'intensity' tools/workflows/README.md` — printed 4, and over the BASE file 0. The
  arm `the args header documents all` printed `ok` over 14 fields at VERIFYING, and the header
  carries `intensity:` at line 85 of the template.
