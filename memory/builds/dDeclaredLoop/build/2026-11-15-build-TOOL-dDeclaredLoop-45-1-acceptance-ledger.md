# TOOL-dDeclaredLoop-45 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-45

No merge bar, no self-test suite and no gate leg ran in this pass, and `position.py --selftest` was not
run. The criteria were observed on node `d` (win32) by probes of the unit's own code: each of the
twenty-one plants of `tools/loop/position.py` run one at a time by direct CLI, each building its
scratch repository and bare remote under the host temp directory and removing it, the three new ones
and the eighteen of units 7 and 14, which all still read `held`; `derive_unit_step` called from
`python -c` over each row of the spec's rule table, a malformed record naming the unit included;
`read_computed_witnesses` over the shipped definition, every row's writer of the stand-in form; and
`main` with `--json` over a stubbed position, whose unit rows carry `id`, `step` and `state` alone.

Owed to the close: every leg the spec's section 7 names, `docs` and `memory hygiene` among them; the
RED-first observation of the spec's one `New arm:` line, the three built plants staged against unit
7's rule, which reads A `designed` and lets the driver's `next:` line name it; and the `loop position
fixtures` row in `tools/run-gates/selftest-budgets.txt` read against the leg's own timing, since its
hang ceiling in `tools/gate-legs.json` sits below the re-priced budget on a loaded node.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/position.py --selftest` with every function the unit's pass changed in
`tools/loop/position.py` swapped back to its pre-pass source exited 1, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-45
- AC1 — `unit — <A> · built · acceptance unarmed` — `python position.py --fixture --plant built-unarmed` in the loop kit's folder printed `unit — TOOL-tPos-1 · built · acceptance unarmed`, A with its pass commit and no acceptance record under the shipped stand-in writer, and `unit — TOOL-tPos-2 · designed`, then `held`, exit 0.
- AC2 — `executor:build.acceptance` — `--plant built-unheld`, a well-formed record naming A at the plant's `fixture` commit, which no `Pass:` trailer attributes to A, read on a `read —` line, printed `unit — TOOL-tPos-1 · designed` with no tag and `held`; `--plant built-armed` printed that line twice, once with the in-memory row's writer set to `executor:build.acceptance` and once with the `acceptance` row removed, and `held`, exit 0.
- AC3 — `next:` — the `built-unarmed` plant ran the unattended driver's `--plan tPos` over its repository, which printed `next: TOOL-tPos-2 (READY - build it)`, naming B and not A, and the plant held on that line.
