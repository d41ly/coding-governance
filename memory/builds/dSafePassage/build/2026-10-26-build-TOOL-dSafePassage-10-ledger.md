**Serves:** journal TOOL-dSafePassage-10

# TOOL-dSafePassage-10 — acceptance ledger

The unit as built, at spec rev-4. `tools/govkit/step_gate.py` reads the nine classes
`tools/govkit/surface-classes.toml` declares, each reader, plant and witness loaded from the tip's
tree; resolves the base through `resolve_landing_base` in `tools/govkit/govkit.py`; reads the base
side in a detached worktree sparse past `memory/`; and reds each vanished member no `[[upgrade]]` or
`[[retired]]` row, read through `upgrade_steps.py`, names in `surfaces`. The leg row `step-gate`, its
`[[exempt_leg]]` row, its subject pin, its ceiling evidence (an `--observed` row, 4.4 s, ceiling 60)
and its dossier claim landed with it, and `help/step-gate.md` with its index line. Departures:
deviations 167 (the base function renamed, not re-extracted), 168 (the witness row names every member
the plant made vanish) and 169 (class rows spell their path through `{prefix}`).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. This branch carries no
`.governance/install.json`, which TOOL-dSafePassage-8 writes only at the lander, so on the branch the
`file` class is empty and the gate refuses: `python tools/govkit/step_gate.py --base HEAD` printed
`step-gate: REFUSED · class file is empty at the tip` and exited 2, and `--list` printed `file · 0
members`. TOOL-dSafePassage-21 gives that class gov's planned destinations, and TOOL-dSafePassage-26
S24 observes AC12 on the branch through it. Every criterion below was therefore observed in a fixture
repository at `%TEMP%/sgv`: a clone of this branch carrying this pass's files, where `python
tools/govkit/govkit.py update --target . --write` wrote gov's source receipt (337 file rows) and one
commit holds both, the prepared merge's shape. The fixtures cloned that repository's HEAD.

Owed at the close: the selftest arm `check_step_gate_fixture` in `tools/govkit/selftest.py` (its
RED-first observation and its run, which on the branch exits 2 on every case until
TOOL-dSafePassage-21 lands), the `step-gate` leg itself (its RED-first observation, and its green at
the prepared merge carrying the receipt), and the §7 legs, the meta-gates a new leg trips among them:
`govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`, `govkit selfcheck`, `kit epoch
(shipped bytes move, the version moves)`, `recall floor`, `recall floor arms`, `measure-legs selftest`,
`run-gates canary`, `run-gates gov canary`, `memory hygiene`, `policy fixtures`, `spec tokens (a
spec's own names resolve)`, plus the install-prefix ban over the new files.

**Evidences:** TOOL-dSafePassage-10
- AC1 — `python "tools/govkit/step_gate.py" --list` in the fixture repository printed nine lines: `file · 337`, `installable · 304`, `hook · 12`, `command · 7`, `agent · 10`, `conf · 16`, `policy · 267`, `verb · 40`, `entry · 30` members, each read from the registry's rows; on the branch `file · 0`, owed to TOOL-dSafePassage-21.
- AC2 — `python "tools/govkit/step_gate.py" --fixture --plant installable` exited 1 with `RED installable:{prefix}/agent-instructions/README.md`, the renamed file's old destination; with `--with-row` it exited 0, `1 vanished · 1 witnessed`.
- AC3 — `python "tools/govkit/step_gate.py" --fixture --plant agent` exited 1 with `RED agent:gov-builder` (and `RED installable:{prefix}/roles/agents/gov-builder.agent.md`, deviation 168); with `--with-row` it exited 0, `2 vanished · 2 witnessed`.
- AC4 — `python "tools/govkit/step_gate.py" --fixture --plant entry` exited 1 with `RED entry:check-install-prefix` and its two installables; with `--with-row`, a `[[retired]]` row naming them, it exited 0.
- AC5 — `python "tools/govkit/step_gate.py" --fixture --plant policy` exited 1 with `RED policy:preset`, the deleted first `[[key]]` of the clone's `tools/policy/catalogue.toml`; with `--with-row` it exited 0.
- AC6 — `python "tools/govkit/step_gate.py" --fixture --plant content-edit` exited 0 with `step-gate: 9 classes · 1023 members at the tip · 0 vanished · 0 witnessed`; with `--with-row` the same.
- AC7 — `python "tools/govkit/step_gate.py" --fixture --plant <class>` exited 1 for `file` (`RED file:.claude/skills/build/SKILL.md`), `hook` (`RED hook:orientation-card`), `command` (`RED command:cleanup`), `conf` (`RED conf:.memory-tree.conf#DISCIPLINES`) and `verb` (`RED verb:govkit.py:intake`), and each exited 0 with `--with-row`.
- AC8 — `python "tools/govkit/step_gate.py" --fixture --plant empty-class` exited 2 with `REFUSED · class sg-fixture is empty at the tip`; `--plant no-plant` exited 2 with `[[class]] row 10 (id sg-fixture) key plant: required`; both exited 2 with `--with-row`.
- AC9 — `python "tools/govkit/step_gate.py" --fixture --plant own-record` exited 0 with `1 vanished · 1 witnessed`; `--plant own-record-unnamed` exited 1 with `RED sg-fixture:gone`, and 0 with `--with-row`, the step row read beside the class's own witness.
- AC10 — `python "tools/govkit/step_gate.py" --print-base --base HEAD~1` printed `4987c13df8686218b1f8c01d6fb87e8da016c7d1`, what `git rev-parse HEAD~1` printed; with no `--base` it printed `60d90cb71db51e651aa1c5efe3f6d48ba21a997d`, what `git merge-base origin/main HEAD` printed; `git grep -n -e "resolve_landing_base(" -- tools/govkit` over the staged tree printed the definition at `tools/govkit/govkit.py:13795`, the call in `cmd_epoch` at `:13873`, and two in `tools/govkit/step_gate.py` (the gate and `--print-base`).
- AC11 — `git grep -n -F "step-gate" -- tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/ceiling-evidence.txt memory/map/features/govkit.md` over the staged tree printed one line per file, five lines.
- AC12 — `python "tools/govkit/step_gate.py" --base HEAD` in the fixture repository exited 0 with `9 classes · 1023 members at the tip · 0 vanished · 0 witnessed`, every class non-zero by AC1; on the branch it exits 2 on the empty `file` class, owed to TOOL-dSafePassage-21 and TOOL-dSafePassage-26 S24.
- AC13 — `git grep -n -e "step-gate" -- help/` over the staged tree printed `help/step-gate.md` and its line in `help/README.md`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: One `New arm:` line, for `tools/govkit/step_gate.py`. The break was `write_hook_plant` committed onto `dsp5b` (`26931dd0f`). `step_gate.py --base HEAD~1` exited 1 with `step-gate: RED hook:orientation-card vanished with no [[upgrade]] or [[retired]] row naming it in surfaces`. Restored by a revert commit, the same range from `83817478f` exited 0 with `0 vanished · 0 witnessed`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_step_gate_fixture`, cut to `file` and `hook`, with and without `--with-row`. Break: `check_step_gate` returns `0`, committed in the scratch clone as described above. RED: `FAIL [dSP-10] step-gate fixture file exits 1 and names ^step-gate: RED file:\S — step-gate: fixture file · planted file:{prefix}/agent-instructions/README.md`, and the same for `hook`. GREEN restored after `reset --hard`: 4 ok, FAILURES=0.
