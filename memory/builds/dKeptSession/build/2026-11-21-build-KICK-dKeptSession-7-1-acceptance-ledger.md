# KICK-dKeptSession-7 — acceptance ledger

**Serves:** journal KICK-dKeptSession-7

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
at the pass's base `eacd93f99` over the working tree before the commit: by the unit's own plants, each
run alone by direct CLI (`position.py --fixture --plant <case>`, `loop_transition.py --fixture --plant
deps-notices`); by three scratch probe scripts of this pass's own, each building its scratch through
`position.write_position_plant` (a bare `origin`, the tree's `.unattended.conf` with `RUN_CLAIMS` on)
and calling the driver sourced through the extended `breakpoints.run_sourced`, the fleet tag from
`placement.read_fleet_user`; and by the greps, `cmp` and Python one-liners AC10, AC12 and AC13 state.

Before the first edit the spec's cited code was probed at the base, units 39, 51, 27, 24, 10, 25, 21
and 6 read as landed: `tools/loop/breakpoints.py#run_sourced` took `(repo, script, driver=None)` with
its 900 s bound (PINNED at `eacd93f99`) and no argument passing; `tools/loop/placement.py#read_build_lease`
runs `( load_driver_conf && main --lease status build … )`; `tools/loop/placement.py#write_foreign_lease`
pushed twelve keys to `FIXTURE_REMOTE`, `upstream`, while the position plants push to `origin`;
`MAIL_GUARD_SECONDS` is 30 (PINNED at `eacd93f99`) and `read_mail_rows` parses the first eleven
columns, `kind`, `from-build` and `subject` among them; `check_interface_notice` answers 0, 1 and 2 over
`read_mailbox`'s fourteenth column, `content-key`; `print_lease_status` is dispatched before
`run_lease_verb`, and `read_claims`' row carries `witness` as its fifteenth field; `verb_landed` returns 0
at two success exits, the in-place observation and the recorded terminal; `run_loop_verb` sets `_bd_out`,
`_bd_rc` and `_bd_why`; `tools/loop/loop.toml`'s `[[step]]` rows carry `order`, `step.build`'s the third,
and its `[mail]` kinds hold `confirmed`, `changed` and `landed`; the catalogue's two `deps.` rows and
`[preset.strict]`'s cells read as §1 states. The two `PLANTS` held 37 and 19 (DERIVED, `len(PLANTS)` at
`eacd93f99`), the counts §4 "The budget rows" expects once units 10 and 24 land; the budget rows read
proxy `r` 80.9 s and 47.1 s (PINNED in the rows' notes, by units 10 and 24) where the spec's table
read 68.5 s and 44.3 s before them, reconciled by re-reading both. The floors read 4162 and 1379
(DERIVED, the last assignment of each at `eacd93f99`), units 27, 24, 25, 21 and 6 having raised the
4100 and 1317 §7 read. `docs_leg.py --fingerprints` printed `verb:unattended.sh:--lease f067f09f`,
`script:tools/loop/loop_transition.py 930359dc` and `script:tools/loop/position.py c1931acf` after the
edits (DERIVED, that run), each the value its anchor in `help/loop.md` already carries, so the
re-stamp moves no byte. `check-arms.py --report`'s ceiling row read the driver at `347/347` after the
edits (DERIVED, that run). No suite arm greps a refusal or NOTE text this pass changes; no message
was changed.

How the build reconciled the spec's text with what landed: `derive_dependency_hold`'s `confirmed` is a
callable, run only in the `confirmed-interfaces` row, so no other row spends a confirmation check;
`read_dependents` parses only a README whose bytes hold `parents:`; a listing that does not derive at
the transition commit adds one `loop: notice · unread · <dependents> · <why>` line, the S4 shape; a
refused policy file refuses both keys, so the bogus scratch prints one NOTE per key; AC11 is driven in
region eight's lease fixture, beside its renew-with-witness arm, where AC8's LANDING fixture holds the
claim block's lease and no transition witness.

## Criteria

**Evidences:** KICK-dKeptSession-7
- AC1 — `deps-wait` held: the Design item answered `act` at `item.design.input` beside `interrupt — dependency · tPar · reachable · not landed (deps.coordination: wait-for-landing)`, and the Build item `blocked` with that subject as its reason, exit 0 (DERIVED, the plant).
- AC2 — `deps-unreachable` held: with no parent lease the Build item answered `blocked`, cause `unreachable`; with the lease live, its `witness` the fixture commit holding tPar's spec, and a `confirmed` keyed by the driver's `derive_gov_id --file` over that listing, `act`, cause `confirmed` (DERIVED, the plant).
- AC3 — `deps-order` held: `order-only`, no lease, the Build item answered `act` beside the `order only` interrupt (DERIVED, the plant).
- AC4 — `deps-confirmed` held: `blocked` `awaiting confirmed` with no confirmation; `act` once a recomputing `confirmed` was planted; still `act` once a newer `changed` keyed `0123456789ab` was; `blocked` `awaiting confirmed` once the witness moved to a commit adding a second tPar spec; and with `breakpoints.run_sourced` answering the check exit 2, `blocked` `confirmation unread` with exactly one note, `position: NOTE · interfaces tPar unread: interface — not read · the fixture's refused check` (DERIVED, the plant).
- AC5 — `deps-design-only` held: Design `act`, Build `blocked` `not landed` (DERIVED, the plant).
- AC6 — `deps-anything` held: reachable and unconfirmed, Build `act` as `coordinated`; the lease deleted, `blocked` `unreachable` (DERIVED, the plant).
- AC7 — `deps-notices` held, exit 0: B5 at the older `--witness` printed `mail — posted 859101bf6a10 · refs/gov/mail/tFix/a/s-notice`; B8 back and B5 again printed a second post; `--mail read tDep` then held one `confirmed` to `build:tDep`, subject `interfaces tFix`, content-key `a90fa6cfcadb`, and one `changed`, content-key `be23cf4decdc`; the keys over the listings at `--witness`, the first move's commit and the second's read `1476fbb0a4a0 a90fa6cfcadb be23cf4decdc` (DERIVED, the plant; the keys are blob ids of fixed fixture bytes, the message id carries the session).
- AC8 — a sourced driver's `write_landed_notices tPar <sha>` over a scratch whose tPos README names tPar printed `mail — posted f15a86cf04c9 · refs/gov/mail/tPar/a/s-landed` and its ring line, rc 0, the origin's message `to: build:tPos`, `kind: landed`, `subject: landing tPar`, its body the sha; with the session unset it printed `mail — not written: no session id`, rc 0; a slug no README names printed nothing; `RUN_CLAIMS` off printed nothing (DERIVED, the probe). `--landed` itself is the suite's arm, the close's.
- AC9 — `deps-strict` held: `resolve` read `deps.coordination wait-for-landing from preset · deps.early-build design-only from preset`; Design `act`, Build `blocked` `not landed`; in the second scratch whose only revision holds `deps.coordination = "bogus"`, Design `act`, Build `blocked` `policy unread`, and a `position: NOTE · deps.coordination unread: policy: refused · …` line naming the invalid value printed (DERIVED, the plant).
- AC10 — in `help/loop.md`'s new section `deps.coordination` 2, `deps.early-build` 2, `unreachable` 2, `landed` 8 and `lease show` 1 lines, and `lease show` and `deps-notices` 1 line each outside it; `grep -c 'lease show build'` printed 1 over the template and over the guide, and `cmp` of the two printed nothing (DERIVED, those greps at observation time).
- AC11 — over the probe's scratch, `--lease show build tPar` printed `-` with no lease and with a lease holding no witness, the witness sha alone once a lease carried it, exit 0; `unit tPar TOOL-tPar-1`, `build tPar x` and `build` alone each printed `lease not written — --lease show takes build <slug> and nothing else`, exit 2; with `RUN_CLAIMS` off `lease — off · tPar/build`, exit 0; `ls-remote` read the same before and after (DERIVED, the probe).
- AC12 — the probe printed `44` and `20`, the greps `plants=44` and `plants=20`, and the eight plants are keys of the two `PLANTS` (DERIVED, those commands at observation time).
- AC13 — `dependents --build` 2 lines in `loop_transition.py` and 1 in the loop README, `deps.coordination` 13 in `position.py`, `lease show build` 1 in the driver (DERIVED, those greps at observation time).

The `loop transition record` plant read 33.0 s alone (PINNED 2026-11-23, `time`), so its proxy `r` is
80.1 s and its row 121 s (DERIVED, x1.5 rounded up), 1 s past the leg's 120 s ceiling (PINNED
2026-11-23, `tools/gate-legs.json`), a raise left to the owner and not made here. The seven position
plants read 8.3, 20.4, 4.8, 40.9, 9.1, 11.1 and 17.3 s alone (PINNED 2026-11-23, `time`), 111.9 s
(DERIVED, their sum), so that row's proxy `r` is 192.8 s and its 432 s stands; `parent-unlanded`, which
now reads its parent's reach and both keys, read 2.9 s alone (PINNED 2026-11-23). No added driver line
carries `exit 1`, `status=1` or a `fail` call, and no added line is a `while` loop fed by `<<<` or a
process substitution (DERIVED, a grep of the diff's added lines). The new suite arms count 8
region-eight `same` (DERIVED, their own lines: AC8 3, AC11 5), raising `FLOOR_ASSERTIONS` to 4170 and
`FLOOR_SHARD_8` to 1387, each with its `RAISED` line; their RED-first observations, the plants', and the
legs of §7 are the close's. `python tools/lexicon/lexicon.py` exited 1 on its verb-offender pin, 1432
over 1421 (DERIVED, that run), the count unit 6 read at its base, and `--offenders` names none of this
unit's functions, nested helpers included. `gen_map.py --write` added the unit's functions, its two
plant runners and the suite's `write_landed_dependent` to `memory/map/generated/symbols.json`, and
rewrote no other map file.
- seen-red — `loop transition record` — red `45016a2c4` — green `45016a2c4` — `deps-notices`: the notice call left out of the Design exit
- seen-red — `loop position fixtures` — red `45016a2c4` — green `45016a2c4` — `deps-wait`: the gate read without the `wait-for-landing` value
- seen-red — `loop position fixtures` — red `45016a2c4` — green `45016a2c4` — `deps-order`: the `order-only` value unread
- seen-red — `loop position fixtures` — red `45016a2c4` — green `45016a2c4` — `deps-unreachable`: an unreachable parent read as reachable
- seen-red — `loop position fixtures` — red `45016a2c4` — green `45016a2c4` — `deps-confirmed`: an unconfirmed interface holds nothing
- seen-red — `loop position fixtures` — red `45016a2c4` — green `45016a2c4` — `deps-design-only`: the `design-only` value unread
- seen-red — `loop position fixtures` — red `45016a2c4` — green `45016a2c4` — `deps-anything`: the `anything-coordinated` value unread
- seen-red — `loop position fixtures` — red `f6a0d7aaf` — green `f6a0d7aaf` — `deps-strict`: the two keys never read from the preset
