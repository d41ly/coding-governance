# TOOL-dWitnessedBar-11 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-11

This pass ran no merge bar, no self-test suite and no gate leg except the naming lexicon's
`--suggest`; `leg_factory.py --selftest` was not run. Every criterion below was checked on node d on
2026-11-19 by the unit's own CLI or a `python -c` probe of the changed code, in the worktree or in a
scratch clone under `%TEMP%` carrying the pass's diff. Once `gate-leg conformance` was a manifest row
the role hook refused `--conform` in the worktree, so its live-tree reading is the clone's, taken
before that. Still owed to the close: the RED-first observation of the `New arm:` line in spec
section 7 (`leg_factory.py --selftest`, covering AC1, AC4 and AC5), every leg that section names, the
two new legs `gate-leg conformance` and `leg-factory selftest`, and the criteria below marked owed.

**Evidences:** TOOL-dWitnessedBar-11
- AC1 — `--check` — exits 0 printing `fresh · 200 legs` on the built tree (the clone). In the clone with
  `drift-audit records`' manifest row hand-edited to a ceiling one higher, row count unchanged, it exits 1
  printing `leg 'drift-audit records' changed: ceiling differ from the render`; with a `[[gate_leg]]` row
  `probe leg` appended to `tools/gate-lint/kit.toml` and no `--write`, it exits 1 printing
  `leg 'probe leg' added`.
- AC2 — `True` — the criterion's own `python -c` over `tools/gate-legs.json` against the pass's start
  `18f3dafc3` printed `True` after the migration's `--write`, before S6's tags and the two new legs
  changed rows on purpose. 70 claimed legs gained a `[gate_leg.gov]` sub-table (`chunk` 70, `ceiling` 63,
  `guard` 56, `argv` 8, `reads` 7, `signature` 4, DERIVED; deviation 113 says why `guard` is not 19)
  and 128 exempt rows took their whole manifest row.
- AC3 — `cmp` — owed to the close: the two `govkit apply --all` runs need an intake answer file per
  scratch adopter and were not run. A probe parsed all 28 changed TOML files at HEAD and in the tree,
  dropped each `[gate_leg.gov]` sub-table and the registry rows' moved keys, and found 0 files (DERIVED)
  differing, so every base row an adopter's emitter reads is untouched; the emitter reads named keys
  and never `gov`.
- AC4 — `--conform` — in the clone it exits 0 unplanted and with a 60-character purpose holding a
  multibyte character, and exits 1 naming the leg and the arm under each plant: subject `maybe`
  (`subject ·`), one name in a descriptor and the registry (`one declaration ·`), an `[[exempt_leg]]`
  with an empty why (`exempt reason ·`), a `{gate_file}` token with no gov override (`token ·`), an empty
  `enforces` on an unpended leg (`enforces ·`), a 61-character purpose (`(61 characters)`) and two
  legs sharing one purpose (`share the purpose`).
- AC5 — `core.py new gate-leg` — in the clone, `python tools/playbook/core.py new gate-leg "demo leg"
  --kit gate-lint --argv '["python3","demo.py"]' --subject repo --purpose "a demo leg" --enforces
  practice.verify` exits 0 printing `declared 'demo leg' as leg.gate-lint.demo-leg`, the manifest holds
  201 rows (DERIVED) and `--conform` exits 0; without `--purpose` it exits 2 printing `--purpose is required`
  and `tools/gate-lint/kit.toml`'s md5 is unchanged.
- AC6 — `kind.gate-leg` — `grep -c "kind.gate-leg" tools/playbook/core-pending.txt` prints 0;
  `core.check_kind_row` over the row returns `([], True)`; `render_playbook.py --reference` re-rendered
  `help/reference/kinds.md`, whose `kind.gate-leg` section reads `python <prefix>/playbook/core.py new
  gate-leg <name> --kit <id> ...`. Owed to the close: `core.py kinds` and `render_playbook.py
  --reference --check`, the legs `core kinds` and `help reference pages`.
- AC7 — `regen.py --list` — prints `regen: stage 1 · run-gates · tools/run-gates/../gate-legs.json`
  with `write  python tools/run-gates/leg_factory.py --write` and `check  python
  tools/run-gates/leg_factory.py --check`.
- AC8 — `meta-check` — a probe with `core.read_legs` and `core.read_pending` found 70 pending `leg`
  rows, 70 manifest rows with no `enforces`, the two sets equal, no pending principle or practice row
  naming a tag a leg enforces, and no pending-row red; the enforces review puts those 70 legs (DERIVED) to the
  owner. Owed to the close: `core.py meta-check`, the leg `core meta-check`.
- AC9 — `PURPOSE_MAX_CHARS` — `git grep -nE "is in no leg of|share the purpose|PURPOSE_MAX_CHARS" --
  tools/govkit/govkit.py` prints nothing; `git grep -nP "\b7h(?![0-9a-z])" -- tools/` prints 7 lines (DERIVED),
  `govkit.py`'s two, the selftest's three, `refusal_join.py`'s one and the run-gates README's one.
  Owed to the close: `govkit.py selfcheck` and `govkit selftest`, which the role hook refuses.
- AC10 — `bypass-never` — owed to the close: `core.py fixture --plant bypass-never` and the meta-check
  under `core.bypass = "never"` in a clone. The criterion's own count probe over the built manifest prints
  45 (DERIVED), the rows carrying a non-empty `enforces` and a `guard`, the figure that close reads.
