# TOOL-dRenderedAnchor-5 — acceptance ledger

**Serves:** journal TOOL-dRenderedAnchor-5

This is the build pass of the unit, built from spec rev-1. `<p1>` is the pass commit this ledger
lands in. It rewrites the opening of arm 17's comment so it names both layouts on which the two
values of `here` part, moves the line break before the article in the help page and the adopter
header, makes arm 15's comment read "is not a", adds the round-4 L1 and L2 entries to the gotcha
record, and moves the spec's status to CLOSED. `gotchas.py --write` left the gotchas index as it was.

No merge bar, gate leg or self-test suite was run by this pass: not `adopt-roles.test.sh`, in whole
or as a slice. The section 6 legs, and the suite's `PASS (62 assertions)` the spec's section 6 asks
the close to read, are owed to the close. The unit adds and moves no arm, so it owes no RED-first
observation. Every criterion below was observed by a direct probe on this Windows host, over the
bytes this commit holds, read from the index before the commit and from `HEAD` after it. The probe
program `carriers5.py`, section 4's, is saved under the session scratchpad.

**Evidences:** TOOL-dRenderedAnchor-5
- AC1 — `help/roles.md` — the `grep -cF` for the full phrase, article included, printed 1 for each of
  `help/roles.md`, `tools/roles/README.md`, `tools/roles/adopt-roles.sh`,
  `tools/roles/adopt-roles.test.sh` and `tools/roles/roles_lib.py`, a total of 5, and the arm 15
  block piped to the same grep printed 1. Red half: over the five files as at `2ac25483` it printed
  0, 1, 0, 0 and 1, a total of 2, and the arm 15 grep printed 0.
- AC2 — `tools/roles/adopt-roles.test.sh` — `python -I carriers5.py 2ac25483 <p1>` printed
  `same 1 1 98` for `help/roles.md`, `same 1 1 100` for `tools/roles/adopt-roles.sh`,
  `moved 1 1 100` for `tools/roles/adopt-roles.test.sh`, and `same 1 1 0` for the README and the
  library. Red half: run as `2ac25483 2ac25483` it printed `same 1 0 0` for the help page and the
  adopter, and `same 0 0 0` for the suite.
- AC3 — `grep -oF 'one layout only'` — over the arm 17 block, comment marks stripped and lines
  joined, `grep -oF '<kit>/<home>/'` found 1, `grep -oF 'directory above the tool root'` found 1,
  and `grep -oF 'one layout only'` found 0. Red half: the same pipeline over the suite as at
  `2ac25483` found 0, 1 and 1.
- AC4 — `bash -n tools/roles/adopt-roles.sh` — exited 0, and `bash -n tools/roles/adopt-roles.test.sh`
  exited 0. The `git diff -U0 2ac25483` pipeline over both shell files printed 0. Red half: the same
  pipeline over unit 4's range `340be90b..2ac25483` printed 27.
- AC5 — `grep -c 'TOOL-dRenderedAnchor-5' memory/gotchas/two-answers-to-one-question.md` — printed
  2, and `grep -cF "PurePosixPath('/fx/tools/roles')"` over the same file printed 1. Red half: over
  the record as at `2ac25483` both printed 0. The fenced probe, run, printed `/fx/tools` beside
  `/fx/tools/workflows` and `/fx/workflows`, and `/fx/tools/roles` beside
  `/fx/tools/roles/workflows` and `/fx/tools/workflows`.
