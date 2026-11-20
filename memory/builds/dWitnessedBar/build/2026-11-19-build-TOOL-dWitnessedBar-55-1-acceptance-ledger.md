# TOOL-dWitnessedBar-55 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-55

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed on node d, 2026-11-20, by a scratch probe that cut `read_policy_key` from
`.githooks/pre-push` as the new arm cuts it, ran it under the resolved bash, and drove the step's
verbs under `-I` over fixture repositories at `%TEMP%/ir55p`. The new checks in
`check_inherited_red_step`, `tools/govkit/selftest.py`, hold the same fixtures and were not run: their
run and their RED-first observation are owed to the main loop at the close, with the legs section 7
names.

**Evidences:** TOOL-dWitnessedBar-55
- AC1 — `INHERITED_RED=park` — a `.githooks/gate-env.sh` holding `INHERITED_RED=land` then
  `INHERITED_RED=park`: the up exited 0, `policy.toml` read `blocks = "every-red"` under `[verdict]`,
  and the file was left empty of both lines; the witness exited 1 before and 0 after. Its red-when, a
  reader taking the first assignment, is a staged break owed at the close: the step at base took the
  last line too.
- AC2 — `export INHERITED_RED=park` — that line alone: the up exited 0 writing no policy file and the
  line stayed; `INHERITED_RED=park` then `INHERITED_RED=`: the up exited 0, wrote no `blocks` value,
  and took both lines out.
- AC3 — `not an assignment` — a file holding `INHERITED_RED=land`, `export INHERITED_RED=park` and
  `INHERITED_RED=park`: the up wrote `every-red` and left exactly `export INHERITED_RED=park\n`; the
  witness exited 0 printing `not an assignment .githooks/gate-env.sh:1`, and before the up named the
  same line at `:2`. The step at base printed no such row: the red.
- AC4 — `read_policy_key` — the eleven S4 fixtures, plus a quoted value with a comment and CRLF, a
  quoted value padded with spaces and a tab, and a `#` with no whitespace before it, each read the
  same value from the step's `read_value` and the cut hook function, after the sentinel `K=plain`
  read `plain`. The base reader, `build_line_re`'s, read `land` on the indented, spaced, leading-tab
  and BOM rows where the hook read `park`, `park`, a tab then `land`, and nothing: the red.
- AC5 — `not an assignment` — `grep -n "not an assignment" help/upgrade-steps.md` printed lines 442
  and 461, both inside the section `Where INHERITED_RED's value lives`, and
  `grep -n "line out of each file that held one" help/upgrade-steps.md` printed nothing, exit 1.
