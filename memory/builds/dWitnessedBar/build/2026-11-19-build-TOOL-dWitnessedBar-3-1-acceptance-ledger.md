# TOOL-dWitnessedBar-3 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-3

This pass ran no merge bar, no gate leg and no suite. Every criterion below was checked on node d on
2026-11-20 by a probe of the code this pass changed: the AC commands as section 6 spells them, the
unit's own CLIs over scratch fixtures (`verdict_flow.py --fixture`, `inherited_red.py` over five planted
targets), the hook's and the driver's functions sliced out and run over planted run dirs, and the hook
driven end to end over two fixture repositories under `%TEMP%/vbh` whose R declared `own-mixed-contended`
and `own-only`. The close owes every leg of section 7 and the RED-first observation of both `New arm:`
lines: the runner suite's TOOL-dWitnessedBar-3 AC2 arms (staged red by dropping `lib-verdict.sh` from the
KF3 list, and by writing the stamp on INHERITED rather than on `pass`), and the hook suite's
TOOL-dWitnessedBar-3 AC4 arms (staged red by testing the class for INHERITED in `check_inherited_verdict`,
and by dropping the stamp's `blocks` comparison). The unattended suite's re-pointed arms are owed their
run under the README's self-test waiver rule.

**Evidences:** TOOL-dWitnessedBar-3
- AC1 — `derive_red_blocks` — the section 6 command printed `block pass pass pass block block`,
  `block block block pass block block` and two rows of six `block`, the `bogus` row equal to
  `every-red`'s.
- AC2 — `lib-verdict.sh` — `grep -c 'lib-verdict.sh' run-gates.sh` in `tools/run-gates/` printed 7 (the
  source lines, the KF3 list and the comments naming it). Owed: the runner suite's AC2 arms (ten fields, `blocks` ninth, no stamp
  under every-red, a stamp reading `blocks own-only`, KF3 on an edited table) and their RED-first
  observation.
- AC3 — `route` — `python verdict_flow.py --fixture route` printed `attribute` for OWN, `ask` for MIXED,
  CONTENDED and INHERITED, `probe-repair` for DEAD PROBE and for the leg the attribution omits, six rows
  for six failed, `fixture route ok`. The driver's `run_verdict_route`, sliced, relayed the same lines.
- AC4 — `check_inherited_verdict` — the section 6 `eval` command printed `rc 0` over a RED dir whose
  MIXED and INHERITED rows read `pass`, and `rc 1 y reads OWN and blocks` with one row reading `block`.
  End to end, a MIXED red was refused under `own-mixed-contended` at R and landed under `own-only` at R,
  the value handed to the bar as `GATE_VERDICT_BLOCKS`. Owed: the hook suite's arms, the stamp refusal
  among them, and their RED-first observation.
- AC5 — `red-route` — `python verdict_flow.py --fixture red-route` printed `code-miss -> fix-pass` and
  `spec-wrong -> new-unit` under `fix-pass-or-design`, both `-> new-unit` under `always-new-unit`, and
  exit 2 naming the outcome set for `maybe`, the kit for no loop kit, the verb for a loop kit without it,
  and the route for a row routed `ask`; `git grep -nwE '(import|from) (loop_lib|policy)' -- tools/run-gates`
  printed nothing. Live `judge` exits 2 until TOOL-dWitnessedBar-100's `items --tag` lands.
- AC6 — `INHERITED_RED` — the section 6 grep printed lines of `tools/govkit/steps.toml`'s new row,
  `tools/govkit/steps/inherited_red.py` and the run-gates README's migration note, and nothing else.
- AC7 — `inherited_red.py` — `up` over `INHERITED_RED=park` wrote `blocks = "every-red"` under `[verdict]`
  and took the line out, over `land` wrote `own-mixed-contended`, over a blank value wrote no key, over no
  key wrote nothing; `down` restored each target byte for byte (`diff -r` empty), and a policy file
  already holding another value refused naming the conflict.
- AC8 — `verdict.blocks` — `grep -cxE 'verdict\.(blocks|red-route)' unsummarised-keys.txt` printed 0 and
  `grep -cE '^## .verdict\.(blocks|red-route).$' help/reference/policy.md` printed 2. Owed:
  `policy.py get verdict.blocks` with no `--rev` reads the landed revision, so it prints
  `own-mixed-contended` once this pass lands; on the pass's commit `--rev HEAD` is the reading.
