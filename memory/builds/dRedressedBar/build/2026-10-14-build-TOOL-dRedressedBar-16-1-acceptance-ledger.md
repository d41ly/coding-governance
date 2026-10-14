# TOOL-dRedressedBar-16 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-16

The build pass of the units-12-15 spec audit's report id 7 (H1). It moved two product files.
`_cmd_apply`'s LEGS call to `write_gate_legs` in `tools/govkit/govkit.py` now passes
`carry_out_of_scope=True`, and the comment above it points at the docstring for the reason. The
`carry_out_of_scope` paragraph of `write_gate_legs`'s docstring says both verbs keep every claimed
kit in `kits` and so both pass the carry, names `TOOL-dRedressedBar-16`, and says why the same-argv
rule cannot stand in for it. `tools/govkit/selftest.py` gains the `[dRB-16]` block after the
`DEPL-cMendedVintage-13` arms, built from `build_gov13` and `build_target13`. The pass also wrote
this ledger and spec 16's status cell, and the index generator rendered spec 16's records row for
this ledger and the build README's unit-16 row and record count from the staged tree.

`<p12>` is `fda78c56e`, by its `Pass:` trailer. `<w16>` is `8efbe7e81`, the spec-writer pass whose
subject names `TOOL-dRedressedBar-16`. `<p16>` is the commit that adds this ledger, carrying
`Pass: TOOL-dRedressedBar-16`.

No merge bar, no self-test suite and no gate leg ran in this pass. Every criterion was observed
through a direct probe. A scratch program built one gov and two manifest targets the way
`build_gov13` and `build_target13` build them, under `%TEMP%/drb16f`, and ran section 4's sequence
with the arm's own readings. It ran three times: over the tip's engine for the green halves; over
`tools/govkit/govkit.py` from a local `git clone` under `%TEMP%/drb16g`, checked out at `<p12>`, for
the red halves; and over a copy of the tip's engine with the one keyword removed from the LEGS call,
which is the `New arm:` line's staged break. The `[dRB-16]` block itself was not executed. These
probes stand in for `govkit selftest` (the block's readings), the encoding-posture leg (AC5) and
`memory hygiene` (this ledger). The section 7 gates are owed to the close, with the `New arm:`
line's RED-first observation: the `[dRB-16]` block over the staged break.

**Evidences:** TOOL-dRedressedBar-16
- AC1 — `.governance/install.json` — at the tip, on both targets, step 1 and step 2 exited 0, the
  runner held `demo leg` and `demo2 leg`, and step 2 printed one line opening
  `govkit apply — gate legs: emitted 1 `. After step 2, `gate_runner.emitted` held
  `('demo2 leg', 'demo2')` then `('demo leg', 'demo')`. The argv replacement in gov's `demo2`
  descriptor matched. Step 4, `update --target <t> --write`, exited 0, and no line carried
  `does not claim it` or `the gate-leg step refused`. It printed
  `gate legs: emitted 2 into scripts/gate-legs.json` and re-stamped the receipt. The runner's
  `demo2 leg` row then carried `["bash", "scripts/demo2/engine.sh", "--drb16"]`. Over the `<p12>`
  engine, step 2's `emitted` held `('demo leg', 'demo')` alone, and step 4 exited 1. One line carried
  both `the gate-leg step refused` and `does not claim it`; it named the runner's argv
  `["bash", "scripts/demo2/engine.sh"]` and gov's with `--drb16`. The runner's row kept the old argv.
- AC2 — `apply --target <t2> --kits demo2` — at the tip it exited 0, no line carried
  `already has a leg named`, and the runner's `demo2 leg` row carried `--drb16`. It printed one
  `receipt KEEPS 1 kit(s)` line naming `demo`, then `[11/RECEIPT] 4 row(s), 2 kit(s), schema 3`.
  Over the `<p12>` engine the same apply exited 2, and one line carried
  `already has a leg named 'demo2 leg'`. The staged-break engine read as `<p12>` did in all of AC1's
  and AC2's halves: `emitted` without the `demo2` row, `update` exit 1 on `does not claim it`, and
  `apply --kits demo2` exit 2 on `already has a leg named`.
- AC3 — `ast.get_docstring` — at the tip, `_cmd_apply` holds one call to `write_gate_legs`, and its
  keywords are `orders` and `carry_out_of_scope` with `Constant(value=True)`. The docstring of
  `write_gate_legs` carries `TOOL-dRedressedBar-16`, and joined with `tr '\n' ' ' | tr -s ' '` it
  carries no `passes no carry`. At `<p12>`, the call's keywords are `orders` alone, the docstring
  lacks the id, and the joined docstring carries `passes no carry`.
- AC4 — `git diff <w16>~1 <w16> -- memory/builds/dRedressedBar/spec/` — for `8efbe7e81`, spec 12's
  header moved `rev-5` to `rev-6`, CLOSED on both sides, and one revision line was added. It names
  report id 7 and TOOL-dRedressedBar-16's AC1 and AC2. The other spec-12 hunks are its §3 second
  non-goal, its C5 row and one generated records row; spec 16 took two generated records rows.
  At `<w16>`, spec 12's `## 3. Non-goals` cut, joined, names `TOOL-dRedressedBar-16` once and
  carries no `so it wedges nothing`. The same cut over the audited blob `62910df0` carries it once.
  The `^| C5` row of the Alternatives rejected cut names `TOOL-dRedressedBar-16` once. Before this
  pass's commit, `git diff --cached --name-only` under `memory/builds/dRedressedBar/spec/` named
  spec 16 alone. This ledger carries `**Serves:** journal TOOL-dRedressedBar-16`.
- AC5 — `scan_text_io` — `git diff -- tools/govkit/` over the worktree against `<p16>~1` printed no
  `def` or `class` line. `scan_text_io` from `tools/gate-lint/encoding_posture.py` counted 35
  `subprocess` sites in `govkit.py`, and 24 `subprocess` and 1 `file-io` in `selftest.py`, exactly
  the rows `memory/project/encoding-posture-sites.txt` declares.
