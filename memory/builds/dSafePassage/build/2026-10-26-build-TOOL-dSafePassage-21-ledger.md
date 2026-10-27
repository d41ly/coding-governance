**Serves:** journal TOOL-dSafePassage-21

# TOOL-dSafePassage-21 — acceptance ledger

The unit as built, at spec rev-3. In `tools/govkit/govkit.py`: `read_plan_destinations(root)` reads
gov's registry, descriptors and own `.governance/deploy.toml`, runs `planned_writes` over `root` as
its own target with the deploy's selection, and returns each destination with no unresolved token,
in plan order, keyed to its `{path, kit, role, source}` receipt row; a plan with problems is a
`Refusal` naming them. Source mode's receipt writer in `_cmd_update` takes its `files` from it. In
`tools/govkit/step_gate.py`: `read_file_members` reads the source receipt's rows where the tree
carries one and `read_plan_destinations` otherwise; `write_file_plant` writes, on a clone with no
source receipt, one whose rows are the class's plan-read members, then drops its first `.md` row as
before; `write_entry_plant` drops its retired id from gov's deploy `kits` (deviation 177). The
class's `summary` and its `help/step-gate.md` row name the second source (deviation 176). In
`tools/govkit/selftest.py`: the AC3 parity arm in `check_source_mode`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
d (Windows) by the unit's own CLI: AC1 in this worktree, AC2 and AC3 over a scratch clone of this
worktree at `%TEMP%/sg21` carrying the working `govkit.py` and `step_gate.py`, committed there, since
the fixture clones its root's HEAD.

- **AC1** — `python tools/govkit/step_gate.py --list` in this worktree, which carries no receipt,
  printed `file · 337 members`, `installable · 304`, `hook · 12`, `command · 7`, `agent · 10`,
  `conf · 16`, `policy · 267`, `verb · 40`, `entry · 30`, exit 0: every class non-zero.
- **AC2** — `python tools/govkit/step_gate.py --fixture --plant file` printed `planted
  file:.claude/skills/build/SKILL.md`, `9 classes · 1022 members at the tip · 1 vanished · 0
  witnessed` and one `RED file:.claude/skills/build/SKILL.md` line, exit 1; with `--with-row`,
  `1 vanished · 1 witnessed`, exit 0. Before this unit the same command printed `REFUSED · the file
  plant needs a source receipt with a .md files row, and the clone carries none`, exit 2.
- **AC3** — in the scratch clone, `python tools/govkit/govkit.py update --target . --write` exited
  0 printing `337 file row(s) recorded`; `read_file_members` over the clone printed `with 337
  without 337 equal True`, no member on either side alone. `git grep -n -e "def
  read_plan_destinations" -e "read_plan_destinations(" -- tools/govkit` printed three lines: the
  definition in `govkit.py`, its call in `_cmd_update`, and its call in `step_gate.py`'s
  `read_file_members`.
- **Sibling cases** — over the same clone, TOOL-dSafePassage-10's other plants: `hook`, `conf`,
  `policy` and `verb` each exit 1 naming one member of their class; `installable`, `command` and
  `agent` exit 1 naming their member and the `file`/`installable` destinations the same move takes
  out of gov's plan; `installable`, `command` and `entry` exit 0 with `--with-row`; `content-edit`
  0 with `0 vanished`; `own-record` 0 with `1 witnessed`. `entry` exited 2 on the plan's refusal
  until deviation 177, then 1 naming `entry:check-install-prefix` and four destinations, and 0 with
  the row.

OWED AT THE CLOSE. The `New arm:` line of §7 (`tools/govkit/selftest.py`): the `file` plant is run
with and without `--with-row` by TOOL-dSafePassage-10's `check_step_gate_fixture`, and the parity is
`[dSP-21] AC3` in `check_source_mode`; its RED-first observation, staged by a `read_file_members`
copy that reads the receipt alone, is the main loop's. §7's legs, and the step gate's leg
re-observing AC1, run at the close.
