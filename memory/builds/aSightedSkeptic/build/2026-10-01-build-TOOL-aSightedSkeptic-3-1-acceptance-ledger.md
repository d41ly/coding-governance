# TOOL-aSightedSkeptic-3 — acceptance ledger

**Serves:** journal TOOL-aSightedSkeptic-3

`args.specs` names a review's intent documents, validated before any agent, and `renderIntent()`
puts one INTENT block into every finder and skeptic prompt. A diff review with no specs is handed
the range's commit log, and a run with neither specs nor context is announced. The arm readings come
from the main loop's one VERIFYING run of the tier2-review self-test at 149e89d6 (165 passed, 0
failed) and from the same test file run against the BASE render at 9fdd0c18 in a frozen clone (56
passed, 109 failed). The greps and the direct checks were re-run on the build's tip, whose `tools/`
is byte-identical to 149e89d6.

**Evidences:** TOOL-aSightedSkeptic-3
- AC1 — `specs reach every finder and skeptic prompt` — `ok` at VERIFYING over 10 prompts; against
  the BASE render it printed `FAIL` over 8 prompts.
- AC2 — `no specs: every diff finder is handed the commit log` — the arm "no specs: every diff
  finder is handed the commit log over the resolved shas" printed `ok` at VERIFYING and `FAIL`
  against the BASE render. Per 209162da's `Decided:` trailer it hands base as a 7-hex abbreviation
  and head as HEAD, so a command built from the refs as given cannot pass.
- AC3 — `no specs and no context: announced in the log and RUN INTEGRITY` — `ok` at VERIFYING, and
  its control `specs supplied: no intent warning` printed `ok` as "specs supplied: no intent warning,
  and RUN INTEGRITY counts the two documents". Both printed `FAIL` against the BASE render.
- AC4 — `specs refused before any agent` — all eight values printed `ok` at VERIFYING: not an array,
  a non-string member, an empty member, a leading slash, a drive letter, a `..` segment, a backslash
  and null. Against the BASE render all eight printed `FAIL` with "(accepted)".
- AC5 — `spec-audit: a spec that is also a subject is refused` — `ok` at VERIFYING, as was
  `spec-audit: specs render as sibling context`. Both printed `FAIL` against the BASE render.
- AC6 — `another specs` — "AC3 another specs: a lens file under the old key is dispatched" and
  "...and one under its own key is reused" both printed `ok` at VERIFYING. Against the BASE render the
  dispatch half printed `FAIL`; the reuse half printed `ok` there too, since a file under its own key
  is reused whether or not `specs` reaches the key.
- AC7 — `the args header documents all` — `grep -n 'specs:'` over the template listed line 82,
  inside the `// --- inputs (via Workflow args)` block, and line 602, the `inputPrint` line. The arm
  printed `ok` as "documents all 14 fields" at VERIFYING, where the BASE-render run read 10 fields.
  `grep -c -F 'specs' tools/workflows/README.md` printed 6, and over the BASE file 0.
- AC8 — `python tools/lexicon/lexicon.py --suggest renderIntent --as js.function` — printed a line
  opening `OK — renderIntent leads with render`. `check-workflow-syntax.js`,
  `check-verifier-fanout.sh` and `check-review-join.sh` each exited 0. The parity renderer is
  `check-protocol-parity.test.sh --render`, a test script this pass was not permitted to run; the
  stand-in, the `sed` substitution of the cap piped into `diff` against the render, printed 0 lines,
  and `git status` showed the render unmodified. 209162da's message records the render regenerated
  by that renderer.
