# TOOL-dTracedLattice-4 — acceptance ledger

**Serves:** journal TOOL-dTracedLattice-4

**Evidences:** TOOL-dTracedLattice-4
- AC1 — `python3 tools/codebase-map/selftest.py` — the arm `gate-coverage: an uncompared artifact fails (AC1)` runs the real check against a fixture gate naming only `inventories.json` and `MAP.md`, and asserts exit 1 with `symbols.json` and `does not compare` in the message. The arm's SUBJECT is the failing case, so RED is what it observes rather than something staged around it
- AC2 — `python3 tools/codebase-map/selftest.py` — the arm `gate-coverage: a customised gate passes (AC2)` feeds a gate that differs from the template by a comment, a reordering and an extra function while naming all three artifacts, and asserts exit 0. A byte diff would report customisation as staleness, which is why this compares SETS
- AC3 — `python3 tools/codebase-map/selftest.py` — the arm `gate-coverage: an unset GATE_FILE is a named skip (AC3)` asserts exit 0 with `skipped` and `GATE_FILE` in the output, and that the skip still names what the engine writes, so it is informative rather than a shrug
- AC4 — `tools/codebase-map/kit.toml` — a `[[hole]]` with id `frozen-gate-vs-moving-engine` states the mechanism, why it is declared rather than closed (auto-updating a file the project owns is a different and more dangerous change, and govkit owns update policy), and carries a `discharge` command naming this check. A `[[gate_leg]]` puts the check on an adopter's own bar; `tools/govkit/govkit.py selfcheck` refused until the descriptor, `tools/gate-legs.json` and `tools/govkit/subject-pins.tsv` all agreed, which is three spellings of one fact held in agreement by a gate rather than by care
- AC5 — `tools/codebase-map/check_gate_coverage.py` header — states that it compares the SET each side names and does NOT verify a named artifact is compared correctly, and that it cannot separate a deliberate omission from a stale one because that intent is recorded nowhere it can read. Mirrors `TOOL-dTracedLattice-2` AC3's disclosure on the same kit
- S2 — the report is the adopter-visible consequence, not a diff: which generated artifacts the engine writes that the installed gate does not name
- S3 — the disposition for a customised gate is stated PLAINLY as undecidable, which is the option the spec allows and the honest one. The check reports the omission and names what it cannot decide
- liveness — `python3 tools/codebase-map/selftest.py` — the arm `gate-coverage: a predicate matching nothing REFUSES` swaps both regexes for one that matches nothing and asserts exit 2. Without it, a stale predicate reports every installed gate as complete, which is the vacuous-selector shape and is worse than no check because it is cited as coverage
- on this tree — `python3 tools/codebase-map/selftest.py` — the arm `gate-coverage: green on this tree` runs the check unpatched. gov's own `GATE_FILE` points inside the kit directory, so the SHIPPED pair is graded on every selftest run and not only in a fixture

## The predicate, and its limit

One regex reads both sides, so the two sets cannot be derived by two rules that disagree — which is
the defect this unit exists to fix, one level up. What it cannot see is an artifact either side
reaches by a COMPUTED name; both spell theirs as a literal today, and `--list` exists so an author
can check that assumption rather than assume it.

## What this ledger does not evidence

No arm runs the check against a real upgraded adopter tree. The `codebase-map adopter e2e` leg
installs the kit into a scratch repo, and wiring this check into that flow would grade the install
path as well as the predicate; it is not done here, and the fixture arms grade the predicate only.
