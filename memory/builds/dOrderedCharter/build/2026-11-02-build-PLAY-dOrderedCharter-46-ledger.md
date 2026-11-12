# PLAY-dOrderedCharter-46 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-46

Each line is a probe this pass ran at rev-6 of the spec, with the pass applied. No leg, suite or bar ran in the
pass: every plant ran through `overlay.py --fixture --plant` over a throwaway repository. Each plant but
`check-refuses-candidate` was also run with one function of its path stubbed to its broken form, and each went
red. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-46
- AC1 — `staged-not-landed` — a `repo.local` row written and staged over a committed tree read as no unit with state `absent`, and once committed read as `repo.local` with state `landed`; with the landed read stubbed to the working tree, the first expectation went red.
- AC2 — `unborn-head` — in a repository with no commit, a staged kit and a template holding one unit slot and no practice region, `read_overlay` returned no unit with state `unarmed`, and the render exited 0 printing the `overlay — unarmed:` line once; with the unarmed state stubbed to `absent`, both expectations went red.
- AC3 — `check-refuses-candidate` — `--check-render --scope charter`, bare `--check-render` and `--check`, each with `--overlay-from`, exited 2 naming the flag; the render verb with the same flag exited 0, wrote the candidate's row into the charter and printed the `overlay — candidate:` line.
- AC4 — `write-then-render` — the overlay `add` verb, its guard's point declared in the scratch tree's layer register and standard error a terminal, exited 0 with the new row in the rendered charter; after the fixture committed everything, `--check-render --scope charter` exited 0; with the write door's render stubbed to drop the flag, both expectations went red.
- AC5 — `policy-at-head` — with `refs/remotes/origin/main` one commit behind a `HEAD` that excludes `unit.open-rule`, the landed-ref read lacked the exclusion while the composition left the unit out with state `excluded` and the rendered slot lacked its line; with the composition's policy reader stubbed to the landed ref, the composition expectations went red.

**Owed to the close.** The bar, and the RED-first observation of the `New arm:` line: the render selftest's
arm running `overlay.py --fixture` over every plant, these five included.
