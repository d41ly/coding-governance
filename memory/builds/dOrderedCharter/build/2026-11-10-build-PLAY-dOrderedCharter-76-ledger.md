# PLAY-dOrderedCharter-76 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-76

Each line is a probe this pass ran at rev-1 of the spec, over `d6cc1c11d` with the pass applied in the worktree.
No leg, suite or bar ran in the pass: the plants ran through their own fixtures, the unit-line check and the
page commands through `python -c` probes of `tools/govkit/docs_leg.py`'s functions, and the rest by `grep`.
This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-76
- AC1 — `python tools/playbook/render_playbook.py --reference` exited 0 printing `render-playbook: reference · wrote 4 page(s)` and wrote the units page; `help/reference/kinds.md` changed by its unit line and the one escaped summary, `skills/&lt;name&gt;/`, and `help/reference/units.md` holds two `&lt;prefix&gt;` lines. The `--check` half and its drifted-clone case are owed to the close.
- AC2 — `grep -c "^unit = "` and `grep -c "^h1 = "` over `tools/playbook/references.toml` each counted 4. The tag resolver's `show doc.reference.units` is owed to the close.
- AC3 — `docs_leg.py --fixture --plant unit-lines` exited 1 printing `docs: UNIT help/concepts/fx.md:1 unit.nowhere: names no gov unit`, `docs: UNLINKED help/tasks/fx.md: ...` and `docs: UNPAGED unit-usage:unit.fx: no page's unit line names it`; `--plant none` exited 0, its summary ending `unit lines unarmed`. A `python -c` probe of `check_unit_lines` over the tree's pages, classes and population returned 6 resolved, no finding and no state (DERIVED at d6cc1c11d). The leg's own run over the tree is owed to the close.
- AC4 — `step_gate.py --list` printed `step-gate: unit-usage · 4 members · ...`. In a scratch clone checked out with `core.autocrlf=true`, its manifest `w/crlf`, `write_unit_usage_plant` returned `unit-usage:unit.policy-schema` and staged 12 deletions, and `pins.write_unit_plant` then staged the next row out. A `python -c` probe of `read_usage_classes` printed no `CLASS` finding. The step gate's `--fixture --plant unit-usage` clones HEAD, so it is owed to the close.
- AC5 — `instruction_units.py fixture --plant row-removal` exited 0, its three expectations `ok`; with `remove_unit_row` swapped in process for the old LF-body replace, the same plant failed all three. `grep -F "u.body"` over the two plants printed nothing, and `remove_unit_row` is named in each.
- AC6 — `grep -c "principle.p42"` counted 2 in `tools/gate-legs.json` and 0 in `tools/playbook/core-pending.txt`. The meta-check is owed to the close.
- AC7 — `tools/playbook/kit.toml` parses with a second `optional` row for `render_playbook.py` at `point.runtime.install-target`. The layers check is owed to the close.
- AC8 — `grep -c "<!-- unit: unit.unit-registry -->"` counted one line on the concept page and one on the task page; `units.md` is linked from `help/README.md` and the concept page; `help/docs-leg.md` lists `UNLINKED`.
- AC9 — `help/step-gate.md` points at `step_gate.py --list` and holds no `| Class |` line; `step_gate.py --list` printed a line for each of `unit`, `drive`, `kind` and `unit-usage`.

**Owed to the close.** The RED-first observation of both `New arm:` lines in the spec's Gates section, the
govkit selftest's three `unit-lines` docs cases and its derived `unit-usage` step-gate case, and the
instruction units fixture's `row-removal` plant; and the legs that section names, among them the core
meta-check, the layers check and the tags check.
