# Acceptance ledger — TOOL-aNimbleMend-3

**Serves:** journal TOOL-aNimbleMend-3

Built against spec rev-1 in this record's own pass commit. Each line is a probe of the changed code the builder made in the pass: the two scripts copied into a scratch git repository under `%TEMP%`, with one planted manifest per finding and a hand-written cost file, driven by the same commands the new arms of `tools/run-gates/run-gates.evidence.test.sh` hold. No suite, gate leg or bar ran in the pass. Owed to the close: the legs of the spec's Gates section, and the new arm's RED-first observation on its two staged breaks, the limit comparison removed and then the held clause removed.

One reading the close will meet: `python tools/run-gates/pass_legs.py --budget` over this repository's own manifest exits 1 on the held finding, naming `python resolver (behaviour + inline parity + idiom ban)`, the kit-subject row the spec's production-readiness risks name. The carrying leg therefore reds on gov's own declared list until that row leaves it.

**Evidences:** TOOL-aNimbleMend-3
- AC1 — `python <kit>/pass_legs.py --figures` — in this repository it printed one line of three tab-separated integers, 600, 690 and 120, ended by a bare line feed with no carriage return.
- AC2 — `python <kit>/pass_legs.py --budget` — over `green` it exited 0 and its last line was the summary naming 6 legs and a sum of 600.0; over `none` it exited 0 and its last line was `pass-budget: 0 leg(s) declared`; neither printed `WARN`.
- AC3 — `pass-budget: WARN` — over `band` it exited 0 and printed one line opening with the token and naming 665.0, ahead of the summary line.
- AC4 — `PASS-BUDGET FAILED` — over `over` it exited 1 and printed one line opening with the token, naming 700.0 and the 690 limit.
- AC5 — `check_pass_eligible` — over `cap` and over `bare` it exited 1 and named the leg, as over the cap and as holding no cost row, with no pass-leg evidence file in the fixture, so the predicate alone answers `no-red` for both.
- AC6 — `class` — it exited 1 and printed four failure lines, one per leg: `selftest`, `e2e`, `unattended-gate`, and the kit-subject leg's saying the pass-leg runner would hold it.
- AC7 — `python <kit>/derive-ceilings.py --check` — in the fixture, over `over` it exited 1 and its output held the limit finding; over `green` it exited 0 and held both the `ceiling-evidence:` summary and the `pass-budget:` summary. In this repository the same command is a leg's and was not run; the close owes it.
- AC8 — `pass-budget: not graded` — with `pass_legs.py` removed from the fixture's kit copy the check over `over` exited 0, printed a line opening with the token and no traceback.
- AC9 — `grep -c 'PASS_LIMIT_SECONDS' tools/run-gates/README.md` — printed 2, and the grep for `--budget` printed 3.
