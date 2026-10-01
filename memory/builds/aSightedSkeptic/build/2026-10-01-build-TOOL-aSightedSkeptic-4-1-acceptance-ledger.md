# TOOL-aSightedSkeptic-4 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-4

`args.checklist` carries the project's recurring bug classes. `parseChecklist()` reads a string or
an array, and `deriveChecklistShares()` hands item n to one lens round-robin, so each class is swept
by exactly one finder; the split is logged and stated in RUN INTEGRITY. The arm readings come from
the main loop's one VERIFYING run of the tier2-review self-test at 149e89d6 (165 passed, 0 failed)
and from the same test file run against the BASE render at 9fdd0c18 in a frozen clone (56 passed,
109 failed). The greps and the direct checks were re-run on the build's tip, whose `tools/` is
byte-identical to 149e89d6. The round-1 fold (828a5ffa, rev-2) added an arm to AC2; that line was
re-read from the self-test at fe3c29fc (180 passed, 0 failed) and from the same test file against
the BASE render (56 passed, 124 failed).

**Evidences:** TOOL-aSightedSkeptic-4
- AC1 — `checklist string: every item in exactly one finder prompt` — `ok` at VERIFYING, `FAIL`
  against the BASE render.
- AC2 — `checklist string: continuation lines stay with their item` — `ok` at VERIFYING, as was
  `checklist array: each element is one item`. Both printed `FAIL` against the BASE render. Per
  f307976d's `Decided:` trailer the CRLF arm also asserts the CRLF run's key equals its LF twin's.
  The rev-2 arm `checklist string: a line not starting "- " continues its item, indented or not`
  printed `ok` at fe3c29fc and `FAIL` against the BASE render, and the template's refusal text at
  line 254 now reads "every later line not starting "- " continues the item above it, indented or
  not".
- AC3 — `checklist: the log names every lens's share` — `ok` at VERIFYING, and
  `checklist: fewer items than lenses leaves an explicit empty share` printed `ok` naming
  `find:verification find:intent` as the two empty shares. Against the BASE render both printed
  `FAIL`, the second naming no prompt at all.
- AC4 — `checklist absent: announced in the log and RUN INTEGRITY` — `ok` at VERIFYING, with
  `checklist empty: announced as supplied with no item` and the control
  `checklist supplied: no checklist warning` also `ok`. All three printed `FAIL` against the BASE
  render.
- AC5 — `checklist refused before any agent` — all six values printed `ok` at VERIFYING: 7, `{}`,
  null, `[1]`, `['  ']` and a string with no item line. Against the BASE render all six printed
  `FAIL` with "(accepted)".
- AC6 — `spec-audit: the checklist splits over the spec lenses` — `ok` at VERIFYING, `FAIL` against
  the BASE render.
- AC7 — `another checklist` — "AC3 another checklist: a lens file under the old key is dispatched"
  and "...and one under its own key is reused" both printed `ok` at VERIFYING. Against the BASE
  render the dispatch half printed `FAIL` and the reuse half `ok`, since a file under its own key is
  reused whether or not the checklist reaches the key.
- AC8 — `the args header documents all` — `grep -n 'checklist:'` over the template listed line 87,
  inside the `// --- inputs (via Workflow args)` block. The arm printed `ok` as "documents all 14
  fields" at VERIFYING. `grep -c -F 'checklist' tools/workflows/README.md` printed 8. Over the BASE
  file it printed 1, NOT the 0 the criterion states: that one hit is line 38, prose about "the
  bug-class checklist" another workflow hands its review, present unchanged at ef1dcdb6 too. The
  field itself appears nowhere in the BASE README, so the criterion's red condition holds and its
  BASE figure was mis-measured when the spec was written.
- AC9 — `python tools/lexicon/lexicon.py --suggest parseChecklist --as js.function` — printed a line
  opening `OK — parseChecklist leads with parse`, and the same for `deriveChecklistShares` printed
  `OK — deriveChecklistShares leads with derive`. `check-workflow-syntax.js`,
  `check-verifier-fanout.sh` and `check-review-join.sh` each exited 0. The parity renderer is
  `check-protocol-parity.test.sh --render`, a test script this pass was not permitted to run; the
  stand-in, the `sed` substitution of the cap piped into `diff` against the render, printed 0 lines,
  and `git status` showed the render unmodified.
