# KICK-dKeptSession-42 — acceptance ledger

**Serves:** journal KICK-dKeptSession-42

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32,
node d, at the pass's base `884ca0474` over the working tree before the commit: by the unit's four new
plants, each run alone by direct CLI (`loop_transition.py --fixture --plant <case>`), and by the greps
and the Python one-liner AC5, AC6 and AC7 state.

Before the first edit the spec's cited code was probed at the base, units 27, 24, 10, 25, 21, 6, 7 and
35 read as landed: `tools/loop/loop_transition.py#write_transition` binds one `read_mail_rows(root,
build)` read, appends the unarmed line and raises `MailHeld` over every `open` row before
`derive_move`; `MAIL_COLUMNS` names eleven columns (DERIVED, its source), `first-seen`, `from-build`
and `subject` among them; `tools/unattended/unattended.sh#check_interface_notice` prints
`interface — current <id> · <kind> · key <k>` on exit 0 and `interface — unconfirmed · key <k>` on
exit 1; `tools/unattended/unattended.sh#read_mailbox` orders a `-` first-seen after every stamp and
stamps a sighting to the second; `tools/unattended/unattended.sh#write_mail_ack` refuses an id not
addressed to the slug and otherwise posts an `ack`; `tools/loop/breakpoints.py#run_sourced` takes the
keyword-only `args` and `timeout` unit 7 landed, where §4 Evidence still read the older
three-parameter form at `64e146d9`; `tools/loop/loop_transition.py#check_parent_interfaces` answers
`(rc, line)` with `rc` 0, 1 or 2; `tools/loop/placement.py#write_foreign_lease` takes `fields`, and
`tools/loop/placement.py#read_fleet_user` names the registry's first user; the loop definition's
`[mail]` kinds hold `landed`, `superseded`, `withdrawn`, `confirmed` and `changed`. `len(PLANTS)` read
22 and the `loop transition record` row `plants=22` with a budget of 192 (DERIVED, both at
`884ca0474`), the count §4 "The budget row" expects once units 24, 7 and 35 land.
`docs_leg.py --fingerprints` printed `script:tools/loop/loop_transition.py 930359dc` and the
`#record`, `#check` and `#dependents` anchors after the edits (DERIVED, that run), each the value its
anchor in `help/loop.md` already carries, so no anchor moved. `gen_map.py --write` changed
`memory/map/generated/symbols.json` alone, one entry for `write_consumed_acks` (DERIVED, `git status`
after it).

How the build reconciled the spec's text with what landed: the ack launches through the landed
`run_sourced(root, '( load_driver_conf && main --mail ack "$2" "$3" )', args=(build, id),
timeout=MAIL_GUARD_SECONDS)`, imported inside `write_consumed_acks`; `write_transition` calls it only
over a non-empty read, so an unarmed or empty mailbox imports nothing; a `-` stamp orders as
`read_mailbox` orders it, after every stamp, so a `-` row is never strictly earlier; `acks-confirmed`
commits `fy`'s spec in the plant's first commit, so the lease's `witness` is the plant's witness
commit; `acks-superseded` waits 1.1 s (PINNED 2026-11-23, the plant's source) after the read that
sights `fy`'s `confirmed`, since a sighting is stamped to the second and a tie is never earlier; every
`acks-*` plant wraps `run_sourced` to record its acks, passing each call through but the two
`acks-failed` answers, and `acks-superseded` stands in for `check_parent_interfaces` by rebinding the
module-level name the writer reads, both restored in a `finally`.

The budget row was re-priced from these readings (PINNED 2026-11-23, node d, each plant alone by
direct CLI over base `884ca0474`): `acks-landed` 6.6 s, `acks-confirmed` 10.2 s, `acks-superseded`
16.0 s and `acks-failed` 12.5 s, 45.3 s together, so proxy `r` reads 172.8 s over the row's earlier
127.5 s and 1.5 `r` rounds up to 260 (PINNED 2026-11-23, the sum), over the row's 192; the
`plants=` token moved from 22 to 26 (DERIVED, `len(PLANTS)`). That is 140 s past the leg's 120 s
ceiling in `tools/gate-legs.json` (PINNED 2026-11-23), already passed before this unit; the spec's stop
at the ceiling is superseded for this run by the main loop, which parks the raise for the owner, and
`tools/gate-legs.json` was not edited.

## Criteria

**Evidences:** KICK-dKeptSession-42
- AC1 — `acks-landed` held, exit 0: with one `landed` from `fy` to `build:tFix` on the bare remote and no manual ack, B4 printed `loop: recorded · planning -> designing · forward` and `loop: fixture · record · exit 0`, the read after it printed `loop: fixture · state a1a2a3a4a5a6 · acked`, and the wrapper recorded the one ack `a1a2a3a4a5a6 rc 0` (DERIVED, the plant).
- AC2 — `acks-confirmed` held, exit 0: the driver's `derive_gov_id --file` over `fy`'s spec listing at the lease's witness printed the key `254cd6c106e2` (DERIVED, the plant; a blob id of fixed fixture bytes), the `confirmed` carrying it; B4 ran the real `check_parent_interfaces` chain, recorded with no manual ack, and the read after it printed `loop: fixture · state c1c2c3c4c5c6 · acked`, the one ack `c1c2c3c4c5c6 rc 0` (DERIVED, the plant).
- AC3 — `acks-superseded` held, exit 0: B4 recorded and the wrapper's acks read `d1d2d3d4d5d6 rc 0 · c1c2c3c4c5c6 rc 0`, `fy`'s `changed` and the `confirmed` sighted before it; B5 printed `refused — tFix · mail open e1e2e3e4e5e6 f1f2f3f4f5f6 · …`, naming `fz`'s `changed` `f1f2f3f4f5f6`, and exited 1; the stand-in recorded its calls as `fy` then `fz`; the rows then read `acked`, `acked` and `open` (DERIVED, the plant).
- AC4 — `acks-failed` held, exit 0: the wrapper recorded one ack of the first `landed`, `a1a2a3a4a5a6 rc 0`, across B4 and B5, both exit 0; B7 printed `refused — tFix · mail open b1b2b3b4b5b6 b7b8b9b0b1b2 · …` and exited 1; the captured stderr held `mail — ack not posted b1b2b3b4b5b6 · rc 1` and `mail — ack not posted b7b8b9b0b1b2 · rc -` (DERIVED, the plant).
- AC5 — the grep printed three lines of `help/loop.md` (DERIVED, that grep at observation time): the table's header row `| Kind addressed to your build | Acknowledged by | When |` in the guard paragraph under "Recording a build's move", the sentence `dependent's next move acknowledges each notice it has consumed …` inside `## Coordinating with a parent build`, and the fixture-cases sentence naming `acks-landed`.
- AC6 — the probe printed `26` and the grep `plants=26`, and `acks-landed`, `acks-confirmed`, `acks-superseded` and `acks-failed` are keys of `PLANTS` (DERIVED, those commands at observation time).
- AC7 — the grep printed the README's mail-guard paragraph and its fixture sentence, both naming `write_consumed_acks`, and in `loop_transition.py` the module docstring's mail-guard paragraph and plant sentence and `write_transition`'s docstring, each naming `write_consumed_acks` or `acks-landed` (DERIVED, that grep at observation time).

## Owed to the close

The `loop transition record` leg's run of the seven new `check --selftest` cases, the budget, docs,
lexicon, hygiene, recall and spec-token legs §7 names, and the `New arm:` line's RED-first observation:
the four `acks-*` plants with the `write_consumed_acks` call left out of `write_transition`, each owed
red, then green restored.
