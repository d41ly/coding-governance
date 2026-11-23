# KICK-dKeptSession-17 — acceptance ledger

**Serves:** journal KICK-dKeptSession-17

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32,
node d, at the pass's base `493bf31bf` over the working tree before the commit: by the unit's six new
plants, each run alone by direct CLI (`python tools/loop/loop_lib.py --fixture --plant <case>` and
`python tools/loop/breakpoints.py --fixture --plant <case>`); by the landed `values` and `driver-plan`
plants run the same way, since this unit changes the list they read and moves `driver-plan`'s
`check_sourced` helper up one block so `attendance-plan` shares it; and by the probes and greps AC3, AC5,
AC7, AC8 and AC9 state.

Before the first edit the spec's cited code was probed at the base. Units 24, 10, 25, 21, 6, 7, 35, 42,
8, 11, 43, 52, 53 and 55 read as landed, all ancestors of the base.
`tools/loop/breakpoints.py#derive_breakpoints` takes `(values, steps, tags, facts)` and writes the plan
gate unconditionally through its `write_line`, which keeps a gate already standing at a position and
disposer; `tools/loop/breakpoints.py#read_policy_values` reads each key as a string literal at its
`read_value` call; `tools/loop/breakpoints.py#read_breakpoints` sets `unopened` on a held gate and `main`
prints `breakpoints: held` after the breakpoint lines; `tools/loop/loop_lib.py#read_mail_kinds` and
`tools/loop/loop_lib.py#check_item_declarations` are the seams S2 and S3 name, and `main`'s `--check`
prints the probe lines before `loop: witness classes`. `tools/unattended/unattended.sh#read_held_gates`
reads only `breakpoint: ` lines ending ` · owner · <cause> · held` and passes over any other line, and
`tools/unattended/unattended.sh#print_breakpoint_lines` relays the module's output verbatim, so the
attendance line needs no driver change, as §3 says. The catalogue row `attendance` reads owner
`dKeptSession`, default `unattended` and the four allowed values, the `never` list of
`tools/policy/presets.toml` carries it, and `policy:attendance` stood on
`memory/project/docs-undocumented.txt`. The definition held 81 item rows, 24 of them role items (DERIVED,
`read_items` at `493bf31bf`; unit 25's `item.entry.mailbox-answer`, a `command:` item, is the 81st), and
neither role item nor any other names a step exit or `item.plan.exit`. `PLANTS` held 56 in `loop_lib.py`
and 14 in `breakpoints.py`, the two budget rows `plants=56` and `plants=14` (DERIVED, the AC8 probes and
greps at `493bf31bf`), as §4 expects.

How the build reconciled the spec's text with what landed. Nothing the spec cites had moved: unit 25's
mailbox row is the `command:` item §4 already names, and units 21, 7, 11, 52, 53 and 55 touched
neither the breakpoint list nor the `[mail]` seam. `read_attendance` reads the rows without running
`check_loop`, so a definition whose other tables refuse still answers it, as `read_dispositions` does
not; the `--check` arm grades the rows in every read. `check_attendance_rows` prints a line for a row
it refuses too, so `attendance-twice` prints both `confirm-acts` lines before its refusal. The
`attendance-plan` plant needs `driver-plan`'s sourced-call helper, so `check_sourced` now sits once at
the head of the position-plant block, its body unchanged. The `values` plant read 12.9s on this box
against its 3.7s pin of 2026-11-22 (PINNED 2026-11-23, both by direct CLI), so the breakpoint plants'
readings below are a busy box's and over the spec's estimates; the re-priced `r` stays far under both the
row's budget and the leg's ceiling.

## Criteria

**Evidences:** KICK-dKeptSession-17
- AC1 — `attendance-values` with no policy file: `list` printed exactly the `values` plant's default, the plan gate at `item.plan.exit` released by `authorization` and the closing review after `item.build.recommend`, and no `breakpoints: attendance` line; the plant printed `breakpoints: fixture · attendance-values · held` and exited 0 (DERIVED, that run).
- AC2 — under `attendance = "confirm-steps"` the list read the plan gate, an `owner gate · at item.design.exit · owner · attendance · held`, the closing review, the same at `item.build.exit`, `item.test.exit` and `item.deploy.close`, then `breakpoints: attendance · confirm-steps · adds announce ask-live confirm-step-exit · announce: stand-in dWellOiledMachine · ask-live: stand-in dFurnishedOrders`; beside `autonomy = "every-stage"` every exit read cause `autonomy` and the only added line was that attendance line (DERIVED, that run).
- AC3 — under `attendance = "confirm-acts"` the plant printed `breakpoints: fixture · confirm-acts · 24 attendance gate(s) · 24 role item(s) read`, each gate `before` a role tag and the set equal to the role tags `read_items` reads in process; AC3's `python -I -c` probe printed `24` at the top level (DERIVED, that run and that probe at observation time).
- AC4 — under `attendance = "announce"` the list read the default two lines and ended with `breakpoints: attendance · announce · adds announce ask-live · announce: stand-in dWellOiledMachine · ask-live: stand-in dFurnishedOrders`, no gate added (DERIVED, that run).
- AC5 — `attendance-actor` exited 1 printing `loop: refused · the attendance row confirm-acts carries actor, a key outside value and adds`; `attendance-member` exited 1 naming `adds driver:owner, no member of ATTENDANCE_INTERACTIONS`; `attendance-twice` exited 1 naming `the attendance value confirm-acts is given twice`; each prints its `loop: attendance` lines after the probe lines and before `loop: witness classes`. AC5's `check_attendance_rows` probe over the shipped definition printed the four `loop: attendance` lines and `[]` (DERIVED, those runs).
- AC6 — `attendance-missing`, the rows bound less `confirm-steps` through `unittest.mock.patch.object`, ran `list` to exit 2 printing `breakpoints: refused · attendance is 'confirm-steps', which no [[attendance]] row of the loop definition declares`, and the plant printed its `held` line, exit 0. `attendance-plan`: the driver's `--plan` printed, after `frontier: item.build.base`, the list's seven lines byte for byte, four of them attendance gates and the last the attendance line; the sourced `check_phase_gates tPos SPECCING BUILDING` exited 1 with `UNATTENDED check 82 FAILED` naming `held at item.design.exit`; the plant printed its `held` line, exit 0 (DERIVED, those runs).
- AC7 — the catalogue probe in the policy kit's directory printed `dKeptSession unattended`; `grep -c 'usage: policy:attendance ' loop.md` in `help/` printed `1`, the anchor carrying `603ed07d`, the fingerprint `docs_leg.py --fingerprints` printed and then mapped to `help/loop.md`; `grep -cP '^policy:attendance\t' memory/project/docs-undocumented.txt` printed `0` (DERIVED, those commands at observation time).
- AC8 — the `loop_lib` probe printed `59` and the grep `plants=59`; the `breakpoints` probe printed `17` and the grep `plants=17`; the six plants are keys of the two `PLANTS` (DERIVED, those commands at observation time).
- AC9 — `cmp` of the verb guide's template and its copy exited 0, and the five greps printed `1`, `1`, `1`, `1` and `2` (DERIVED, those commands at observation time).

## The budget rows

The three `loop_lib.py` plants read 0.27s, 0.27s and 0.26s, so `loop definition fixtures` re-reads as
`r` 22.2s, its budget 60 standing (PINNED 2026-11-23, each alone by direct CLI). The three
`breakpoints.py` plants read 14.1s, 13.1s and 19.1s, so `loop breakpoint fixtures` re-reads as `r`
134.6s (PINNED 2026-11-23, each alone by direct CLI);
1.5 `r` is 202s, under the row's 317s, which stands (DERIVED, that sum and the row's value);
and under the leg's ceiling of 300s in `tools/gate-legs.json` (PINNED 2026-11-23). The landed `driver-plan` plant read 66.4s on the same
busy box (PINNED 2026-11-23), against the 27s of the row's first note.

## Owed to the close

The `loop definition`, `loop definition fixtures`, `loop breakpoint fixtures`, budget, policy, docs,
unattended kit and memory legs §7 names, and both `New arm:` lines' RED-first observations, are the
main loop's at the close.
