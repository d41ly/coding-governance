# TOOL-dRedressedBar-12 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-12

The build pass of the units-10-11 spec audit's report id 23 (H1). It moved two product files.
`_cmd_apply`'s RECEIPT step in `tools/govkit/govkit.py` now carries every kit the prior receipt
claims that the selection does not name, with that kit's rows verbatim, as `_carried_kits` and
`_carried_rows`. `install.sums` and the `STEP_RECEIPT` counts read the written lists, and one `KEEPS`
line names the carried kits. The `carry_out_of_scope` paragraph of `write_gate_legs`'s docstring
says so. `tools/govkit/selftest.py` gains the `[dRB-12]` block and fixture A's third apply in the
`[dRB-11]` block. The pass also wrote this ledger and spec 12's status cell, and the index
generator rendered spec 12's records row for this ledger and the build README's unit-12 row and
record count from the staged tree. The spec-11 correction
is the spec-writer pass `<w12>`, `62f965ccf`. `<p11>` is `b65688cde`, by its `Pass:` trailer; no
unit-11 acceptance ledger exists. `git diff --stat b65688cde 62f965ccf -- tools skills` prints
nothing, so `<w12>`'s engine is `<p11>`'s.

No merge bar, no self-test suite and no gate leg ran in this pass. Every criterion was observed
through a direct probe. A scratch program drove `python tools/govkit/govkit.py apply` over fresh
`git init` targets under `%TEMP%/drb12`, each with `DEPLOY_FULL`'s answers and committed after every
apply. It ran against the tip worktree for the green half, and against a scratch clone at
`%TEMP%/drb12g` checked out at `<p11>` for the red half. The same clone, with the tip's engine and
the carry re-keyed on `f.get("kit") not in selection`, gave AC3's staged break. A second program cut
the two new selftest regions out of `tools/govkit/selftest.py` by their comment anchors and executed
them alone, with stand-in helpers, over the tip engine: all 12 of its `check` lines read ok. These
probes stand in for `govkit selftest` (the two arms' readings), the encoding-posture leg (AC6) and
`memory hygiene` (this ledger). The section 7 gates are owed to the close, with
both `New arm:` lines' RED-first observation: the `[dRB-12]` block and fixture A's third apply, each
over `<p11>`'s engine.

**Evidences:** TOOL-dRedressedBar-12
- AC1 — `.governance/install.json` — at the tip, step 1 exited 0 with `kits` `kickoff-manifest`,
  `settings-merge`, `agent-cap` and 18 rows (`(govkit)` 1, `kickoff-manifest` 5, `settings-merge` 1,
  `agent-cap` 11). Step 2 exited 0 and wrote `kits` `settings-merge`, `kickoff-manifest`,
  `agent-cap`, 18 rows, and the 16 `kickoff-manifest` and `agent-cap` rows equal step 1's as JSON
  objects. It printed one line opening `govkit apply — receipt KEEPS 2 kit(s)`, which went on to
  name 16 rows and `kickoff-manifest, agent-cap`, then `[11/RECEIPT] 18 row(s), 3 kit(s), schema 3`.
  `install.sums` held 14 lines, one per row carrying a `sha256`. Step 3 exited 0, and no line
  carried `already carries`. Over `<p11>`, step 2 wrote `kits` `settings-merge` alone with 2 rows,
  and step 3 exited 2 on one line carrying `already carries agent-cap`, which named
  `kickoff-manifest` too and ended `this target's receipt does not claim it`.
- AC2 — `guard/agent-cap.js` — fixture A, built as the `[dRB-11]` block builds it. At the tip, the
  second apply exited 1, and after the commit its receipt claimed `settings-merge`, `agent-cap` and
  held the planted row equal, as a dict, to the one planted. The third
  `apply --kits settings-merge` exited 1. No line carried `no-agent-cap-to-wire` or
  `[accepted stop]`, and exactly one line opened `govkit: kit 'settings-merge'`. It carried
  `cannot read`, in `Its stderr ended: settings-merge: cannot read .claude\settings.json`, followed
  by the JSON parser's reason. Over the `<p11>` clone, the second apply
  exited 1 and wrote `kits` `settings-merge` with no `agent-cap` row, and the third exited 0, with one
  line carrying `no-agent-cap-to-wire` and one carrying `[accepted stop]`.
- AC3 — `attributes` — at the tip, step 1 applied twice printed no `KEEPS` line on the second run
  and wrote the same `kits` and 18 rows both times. Applied directly after step 1, step 2's receipt
  held exactly one row with role `attributes`. In the staged-break clone, the same step 2 wrote two
  `attributes` rows and 19 rows in all; with step 1 applied twice first, the second run grew 18 to
  19 rows and step 2 then held three.
- AC4 — `ast.get_docstring` — at the tip, the `tr | grep -o | wc -l` pipeline over
  `tools/govkit/govkit.py` printed 0, and over `git show ebce889c7:tools/govkit/govkit.py` it
  printed 1. `ast.get_docstring` of `write_gate_legs` at the tip carries `TOOL-dRedressedBar-12`.
- AC5 — `git diff <w12>~1 <w12> -- memory/builds/dRedressedBar/spec/` — for `62f965ccf`, spec 11's
  header moved `rev-3` to `rev-4`, CLOSED on both sides, and one revision line was added, naming
  report id 23 and TOOL-dRedressedBar-12's AC2. Spec 11's `## 4. Design` cut at `<w12>`, joined,
  names `TOOL-dRedressedBar-12` twice; the same cut over the audited blob `1b4ea08c` names it 0
  times. Before this pass's commit, `git diff --cached --name-only` under
  `memory/builds/dRedressedBar/spec/` named spec 12 alone. This ledger carries
  `**Serves:** journal TOOL-dRedressedBar-12`.
- AC6 — `scan_text_io` — `git diff b65688cde -- tools/govkit/` over the worktree printed no `def` or
  `class` line. `scan_text_io` from `tools/gate-lint/encoding_posture.py` counted 36 `subprocess`
  sites in `govkit.py`, and 24 `subprocess` and 1 `file-io` in `selftest.py`, exactly the rows
  `memory/project/encoding-posture-sites.txt` declares.
