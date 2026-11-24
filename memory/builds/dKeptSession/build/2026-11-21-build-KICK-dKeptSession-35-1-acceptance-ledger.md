# KICK-dKeptSession-35 — acceptance ledger

**Serves:** journal KICK-dKeptSession-35

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
at the pass's base `343bebd3b` over the working tree before the commit: by the unit's two plants, each
run alone by direct CLI (`loop_transition.py --fixture --plant notices-two-dependents` and
`--plant notices-refused`); by two scratch probes of this pass's own over the sourced driver, one
calling `write_landed_notices` for real over a `notices-refused` scratch built by
`loop_transition.write_transition_plant` (a bare `origin`, the tree's `.unattended.conf` with
`RUN_CLAIMS` on, dA and dB naming tFix in `parents:`), the fleet tag from `placement.read_fleet_user`,
and one with `main` and `run_loop_verb` stubbed; and by the greps and Python one-liners AC4 to AC7 state.

Before the first edit the spec's cited code was probed at the base, units 39, 51, 27, 24, 10, 25, 21,
6 and 7 read as landed. `tools/loop/loop_transition.py#write_dependency_notices` posted through
`breakpoints.run_sourced` with six positional values and no pass, discarding the post's exit;
`tools/loop/loop_transition.py#write_transition` binds `before = read_transitions(build, root)` before
any write and calls the notices last on a move from designing to building; `--mail post` takes
`--pass <pass>` into `derive_message_id`'s third field and the record's `pass:` line. `PLANTS` held 20
and the `loop transition record` row `plants=20` at value 121 (DERIVED, `len(PLANTS)` and the grep at
`343bebd3b`); the floors read 4170 and 1387 (DERIVED, the last assignment of each at `343bebd3b`).
Unit 7's spec is CLOSED at rev-9 and its AC7 holds both passages S4 quotes.

How the build reconciled the spec's text with what landed: unit 7 landed the landed notice's post loop
in `tools/unattended/unattended.sh#write_landed_notices`, which `verb_landed` calls at both success
exits with `DP_LANDING` and `head`, rather than inline in `verb_landed`. So S2's `--pass <sha8>` is the
first eight hex of the sha that function is given, S3's `echo` sits inside its loop, and S7's and AC7's
"comment above the post loop" of `verb_landed` is the comment block above `write_landed_notices`. The
pass rides the post argv as two more positional values, `"$7" "$8"` (`--pass` and the ordinal), the
body moving to `"$9"`. A post that raises keeps unit 7's own line,
`loop: notice · <dependent> · the post did not answer`, and adds no `notice — not posted` line, since
it has no exit.

## S4 — the answer to KICK-dKeptSession-7 AC7, superseded by AC1

Unit 7's AC7, as its CLOSED spec spells it, moves a fixture parent out of Design "with one dependent
README naming it in `parents:`", and then "a second move out of Design posts `changed` with a
different key and no second `confirmed`". AC1 below supersedes it by name: two dependents over three
Design exits, each exit's pass read off its message. Neither unit 7's spec nor its ledger is written by
this unit (F1).

## Criteria

**Evidences:** KICK-dKeptSession-35
- AC1 — `notices-two-dependents` held, exit 0: B5, B21 back, B5, B21 back and B5 each exited 0; six posts each printed `mail — posted`; the plant printed `loop: fixture · dA · confirmed pass 1 · changed pass 2 · changed pass 3` and the same line for dB, each pass the `pass:` line of the row's commit, column 10, read by `git log -1 --format=%B` (DERIVED, the plant).
- AC2 — the real-driver probe: `write_landed_notices tFix <sha>` over two landing commits printed four `mail — posted` lines, rc 0, and `--mail read dA` listed two `landed` rows whose commits' `pass:` lines read `082297e1` and `ea6494d3`, the two landed shas' first eight hex (DERIVED, the probe; scratch commits). The stub probe printed the argv `--pass 01234567` for the sha `0123456789ab…`, then `notice — not posted landed to build:tDep2 · rc 1 · mail — duplicate abc · ref` and `… · rc 2 · no output`, returning 0 (DERIVED, the probe). `--landed` run twice is the suite arm, the close's.
- AC3 — `notices-refused` held, exit 0: `record` printed `notice — not posted confirmed to build:dA · rc 1 · mail — duplicate 000000000000 · the plant's refusal`, then dB's `mail — posted`, and `loop: fixture · record · exit 0` (DERIVED, the plant).
- AC4 — in `help/`, `grep -n "notice — not posted" loop.md` printed one line, the notices paragraph's sentence, which names `--pass` (DERIVED, that grep).
- AC5 — `tr -s ' \r\n' ' '` over this ledger into each `grep -c` printed `1`, and `git diff --name-only 343bebd3b HEAD --` over unit 7's spec and ledger printed nothing (DERIVED, those commands at the commit).
- AC6 — the probe printed `22` and the grep `plants=22`; `notices-two-dependents` and `notices-refused` are keys of `PLANTS` (DERIVED, those commands at observation time).
- AC7 — the probe printed `True True`; the README grep piped into `sort -u` printed both plant names; the driver grep printed the comment line above `write_landed_notices` and its `echo` line (DERIVED, those commands at observation time).

The two plants read 39.6 s and 7.8 s alone (PINNED 2026-11-23, `time`, node d), so the
`loop transition record` row's proxy `r` is 127.5 s, over unit 7's 80.1 s (DERIVED, their sum), and its value 192
(DERIVED, x1.5 rounded up), 72 s past the leg's 120 s ceiling (PINNED 2026-11-23, `tools/gate-legs.json`):
the raise is the owner's and is not made here. The real-driver probe's two landings read 6.6 s and 5.7 s
(PINNED 2026-11-23, node d); the shard 8/8 row moves 6587 to 6669 as an ESTIMATE (DERIVED, x1.5 of
54.3 s, its fixture and verb estimated), for the main loop's first reading to re-price. The driver's
refusal census read `347/347` after the edits (DERIVED, `check-arms.py --report`); no added line carries
`exit 1`, `status=1` or a `fail` call, and no arm greps a message this pass changed. The new suite arm
counts 3 region-eight `same` (DERIVED, its own lines), raising `FLOOR_ASSERTIONS` to 4173 and
`FLOOR_SHARD_8` to 1390, each with its `RAISED` line. `docs_leg.py --fingerprints` printed
`script:tools/loop/loop_transition.py 930359dc` after the edits (DERIVED, that run), the value its
anchor carries, so no anchor moves. `python tools/lexicon/lexicon.py` exited 1 on its verb-offender
pin, 1432 over 1421 (DERIVED, that run), the count unit 7 read at its base, and no offender it lists is
in this unit's files. The new arms' RED-first observations and §7's legs are the close's.
- seen-red — `loop transition record` — red `f6a0d7aaf` — green `f6a0d7aaf` — `notices-two-dependents`: `--pass` dropped from the notice post
- seen-red — `loop transition record` — red `f6a0d7aaf` — green `f6a0d7aaf` — `notices-refused`: a refused post said nowhere
